#!/usr/bin/env python3
"""Exact-artifact, cost-bounded push review for one Open Enzyme COMP.

Every tracked design/input/output file, imported repository-local decision
library, and current wiki page that names the COMP is assigned to a complete
shard inventory. Each shard is inspected; the final independent verdict
separates artifact validity from propagation and synthesis eligibility. One
current receipt replaces the previous receipt.
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

DEFAULT_MODEL = "openai/gpt-5.5"
DEFAULT_PROMPT = Path("scripts/comp-review-prompt.md")
DEFAULT_MAX_COST_USD = 2.50
DEFAULT_ESTIMATED_INPUT_USD_PER_M = 5.0
DEFAULT_ESTIMATED_OUTPUT_USD_PER_M = 20.0
SHARD_CHARS = 180_000
MAX_TOOL_RESULT_CHARS = 80_000
MAX_TOTAL_TOOL_RESULT_CHARS = 240_000
MAX_TOOL_ITERATIONS = 8
SHARD_OUTPUT_MAX_TOKENS = 8_000
FINAL_OUTPUT_MAX_TOKENS = 16_000
TEXT_SUFFIXES = {
    ".md", ".py", ".json", ".csv", ".tsv", ".txt", ".yaml", ".yml",
    ".fasta", ".fa", ".toml", ".sh", ".r", ".xml", ".html", ".jsonl",
    ".pdb", ".pdbqt", ".gitignore", ".gitkeep",
}
COMP_RE = re.compile(r"^(comp-\d{3})(?:-|$)")
ELIGIBILITY = {"eligible", "eligible_with_warning", "blocked"}
VERDICTS = {"clean", "clean_with_limitations", "action_required", "quantitative_verdict_invalid"}


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=check)


def safe_path(raw: str) -> Path:
    candidate = (ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw).resolve()
    if candidate != ROOT and ROOT not in candidate.parents:
        raise ValueError(f"path escapes repository: {raw}")
    return candidate


def resolve_comp(raw: str) -> tuple[Path, str, str]:
    direct = safe_path(raw.rstrip("/"))
    if direct.is_dir():
        candidates = [direct]
    else:
        token = Path(raw.rstrip("/")).name
        candidates = [Path(p).resolve() for p in glob.glob(f"wiki/etc/experiments/{token}*") if Path(p).is_dir()]
    if len(candidates) != 1:
        raise SystemExit(f"Expected one COMP for {raw!r}; found {len(candidates)}")
    comp_dir = candidates[0]
    match = COMP_RE.match(comp_dir.name)
    if not match:
        raise SystemExit(f"Not a comp-NNN directory: {comp_dir}")
    return comp_dir, comp_dir.relative_to(ROOT).as_posix(), match.group(1)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def tracked_files(comp_rel: str) -> list[Path]:
    result = run(["git", "ls-files", "--", comp_rel])
    return [safe_path(line) for line in result.stdout.splitlines() if line and "/reviews/" not in f"/{line}/"]


def create_push_manifest(comp_rel: str, manifest_path: Path) -> str:
    command = [
        sys.executable, "scripts/comp-review-manifest.py", "create",
        "--phase", "push", "--comp-dir", comp_rel, "--output", str(manifest_path),
    ]
    result = run(command)
    return result.stdout.strip().splitlines()[-1]


def verify_authoring_gates(comp_dir: Path) -> dict[str, object]:
    if (comp_dir / "quarantine.json").is_file():
        result = run(
            [
                sys.executable,
                "scripts/check-comp-disposition.py",
                "--comp-dir",
                str(comp_dir),
            ],
            check=False,
        )
        if result.returncode:
            return {
                "status": "quarantined",
                "valid": False,
                "details": [
                    "quarantine binding invalid: "
                    + (result.stderr or result.stdout).strip()[:1000]
                ],
            }
        return {
            "status": "quarantined",
            "valid": True,
            "details": [
                "Current artifact is hash-bound by quarantine.json and excluded "
                "from execution, routine push review, propagation, and synthesis; "
                "historical authoring receipts remain provenance, not current approval"
            ],
        }
    reviews = comp_dir / "reviews"
    pre_paths = (
        reviews / "pre-run.manifest.json",
        reviews / "pre-run.md",
    )
    post_paths = (
        reviews / "post-run.manifest.json",
        reviews / "post-run.md",
    )
    paths = pre_paths + post_paths
    present = [path.exists() for path in paths]
    if not any(present):
        return {"status": "legacy", "valid": True, "details": ["COMP predates authoring-time gates"]}
    if not any(path.exists() for path in pre_paths) and all(
        path.is_file() for path in post_paths
    ):
        result = run(
            [
                sys.executable,
                "scripts/comp-review-manifest.py",
                "check-legacy-post",
                "--comp-dir",
                str(comp_dir),
            ],
            check=False,
        )
        if result.returncode:
            return {
                "status": "legacy_post_run_review",
                "valid": False,
                "details": [
                    "legacy post-run binding invalid: "
                    + (result.stderr or result.stdout).strip()[:1000]
                ],
            }
        return {
            "status": "legacy_post_run_review",
            "valid": True,
            "details": [
                "COMP predates Gate 1; an independent exact post-run review "
                "binds the current artifact and proposed interpretation surfaces"
            ],
        }
    result = run(
        [
            sys.executable,
            "scripts/comp-review-manifest.py",
            "check-lifecycle",
            "--comp-dir",
            str(comp_dir),
        ],
        check=False,
    )
    if result.returncode:
        return {
            "status": "modern",
            "valid": False,
            "details": [
                "authoring lifecycle invalid: "
                + (result.stderr or result.stdout).strip()[:1000]
            ],
        }
    return {
        "status": "modern",
        "valid": True,
        "details": [
            "pre-run design matches post-run design; current COMP artifact "
            "matches the post-run snapshot; later wiki evolution is push-reviewed"
        ],
    }


def _segments(path: Path, role: str) -> list[dict[str, object]]:
    rel = path.relative_to(ROOT).as_posix()
    raw = path.read_bytes()
    file_hash = sha256_bytes(raw)
    if path.suffix.lower() in {".pdb", ".pdbqt"}:
        text = raw.decode("utf-8", errors="replace")
        lines = text.splitlines()
        atoms = [line for line in lines if line.startswith(("ATOM  ", "HETATM"))]
        residues = sorted({line[17:20].strip() for line in atoms if len(line) >= 20})
        summary = (
            f"Deterministic complete-file representation for {rel}\n"
            f"sha256: {file_hash}\nbytes: {len(raw)}\nlines: {len(lines)}\n"
            f"ATOM/HETATM records: {len(atoms)}\nunique residue names: {', '.join(residues)}\n"
            "The raw coordinate file is manifest-bound. Review topology, provenance, and use through "
            "the generating/preparation code and derived tabular outputs; individual coordinate rows are not narrative evidence."
        )
        return [{
            "path": rel, "role": role, "start": 0, "end": len(raw),
            "file_sha256": file_hash, "content": summary, "binary": False,
            "representation": "deterministic_molecular_structure_summary",
        }]
    if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {".gitignore", ".gitkeep"}:
        return [{
            "path": rel, "role": role, "start": 0, "end": len(raw),
            "file_sha256": file_hash, "content": None, "binary": True,
        }]
    text = raw.decode("utf-8", errors="replace")
    if not text:
        return [{
            "path": rel, "role": role, "start": 0, "end": 0,
            "file_sha256": file_hash, "content": "", "binary": False,
        }]
    result = []
    for start in range(0, len(text), SHARD_CHARS):
        end = min(len(text), start + SHARD_CHARS)
        result.append({
            "path": rel, "role": role, "start": start, "end": end,
            "file_sha256": file_hash, "content": text[start:end], "binary": False,
        })
    return result


def build_shards(
    comp_rel: str,
    _comp_id: str,
    manifest_path: Path,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    segments: list[dict[str, object]] = []
    for path in tracked_files(comp_rel):
        segments.extend(_segments(path, "comp_artifact"))
    manifest = json.loads(manifest_path.read_text())
    for item in manifest.get("files", []):
        if item.get("kind") == "shared_dependency":
            segments.extend(
                _segments(safe_path(str(item["path"])), "shared_dependency")
            )
        elif item.get("kind") == "proposed_update":
            segments.extend(
                _segments(
                    safe_path(str(item["path"])),
                    "referencing_wiki_surface",
                )
            )

    binary = [segment for segment in segments if segment["binary"]]
    text_segments = [segment for segment in segments if not segment["binary"]]
    shards: list[dict[str, object]] = []
    current: list[dict[str, object]] = []
    current_chars = 0
    for segment in text_segments:
        size = len(str(segment["content"]))
        if current and current_chars + size > SHARD_CHARS:
            shards.append({"segments": current, "chars": current_chars})
            current, current_chars = [], 0
        current.append(segment)
        current_chars += size
    if current:
        shards.append({"segments": current, "chars": current_chars})
    for index, shard in enumerate(shards, start=1):
        shard["id"] = f"shard-{index:03d}"
        canonical = json.dumps(
            [{k: v for k, v in seg.items() if k != "content"} for seg in shard["segments"]],
            sort_keys=True, separators=(",", ":"),
        ).encode()
        shard["coverage_sha256"] = sha256_bytes(canonical)
    return shards, binary


def estimate_cost(chars: int, output_tokens: int = 4_000, *, input_rate: float, output_rate: float) -> float:
    return (chars / 4 / 1_000_000 * input_rate) + (output_tokens / 1_000_000 * output_rate)


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a repo-relative text file for a load-bearing follow-up check.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "start_byte": {"type": "integer", "minimum": 0},
                    "max_bytes": {"type": "integer", "minimum": 1, "maximum": MAX_TOOL_RESULT_CHARS},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "grep_repo",
            "description": "Fixed-string search across current repository text.",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}, "scope": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
]


def execute_tool(name: str, args: dict[str, object]) -> str:
    try:
        if name == "read_file":
            path = safe_path(str(args["path"]))
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                return "ERROR: readable text file not found"
            start = max(0, int(args.get("start_byte") or 0))
            limit = min(MAX_TOOL_RESULT_CHARS, int(args.get("max_bytes") or MAX_TOOL_RESULT_CHARS))
            with path.open("rb") as handle:
                handle.seek(start)
                chunk = handle.read(limit)
            return chunk.decode("utf-8", errors="replace")
        if name == "grep_repo":
            query = str(args["query"])
            scope = str(args.get("scope") or "wiki")
            safe_path(scope)
            result = run(["rg", "-n", "-F", "--glob", "*.md", "--glob", "*.py", "--", query, scope], check=False)
            return (result.stdout or "(no matches)")[:MAX_TOOL_RESULT_CHARS]
        return f"ERROR: unknown tool {name}"
    except (KeyError, OSError, ValueError) as exc:
        return f"ERROR: {exc}"


def api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if key:
        return key
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise SystemExit("OPENROUTER_API_KEY is not set")


def call_openrouter(key: str, body: dict[str, object]) -> dict[str, object]:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as handle:
        json.dump(body, handle)
        body_path = handle.name
    try:
        for attempt, delay in enumerate((0, 10, 30), start=1):
            if delay:
                time.sleep(delay)
            result = subprocess.run(
                [
                    "curl", "-sS", "--fail-with-body", "--http1.1",
                    "https://openrouter.ai/api/v1/chat/completions",
                    "-H", f"Authorization: Bearer {key}",
                    "-H", "Content-Type: application/json",
                    "-H", "HTTP-Referer: https://github.com/brianpabent/open-enzyme",
                    "-H", "X-Title: Open Enzyme exact COMP review",
                    "-d", f"@{body_path}", "--max-time", "900",
                ],
                cwd=ROOT, text=True, capture_output=True, timeout=920,
            )
            if result.returncode == 0:
                try:
                    parsed = json.loads(result.stdout)
                except json.JSONDecodeError:
                    parsed = {}
                if parsed.get("choices"):
                    return parsed
            if attempt == 3:
                raise SystemExit(f"OpenRouter failed: {(result.stderr or result.stdout)[:1200]}")
    finally:
        os.unlink(body_path)
    raise AssertionError("unreachable")


def review(
    key: str,
    model: str,
    prompt: str,
    *,
    tools: bool = True,
    max_tokens: int = FINAL_OUTPUT_MAX_TOKENS,
    reasoning_effort: str = "medium",
    max_cost_usd: float | None = None,
    stage: str = "review",
) -> tuple[str, dict[str, float]]:
    messages: list[dict[str, object]] = [{"role": "user", "content": prompt}]
    totals = {"input_tokens": 0.0, "output_tokens": 0.0, "tool_calls": 0.0, "cost_usd": 0.0}
    tool_chars = 0
    for iteration in range(MAX_TOOL_ITERATIONS + 1):
        body: dict[str, object] = {
            "model": model,
            "messages": messages,
            "temperature": 0.1,
            "max_tokens": max_tokens,
            "reasoning": {"effort": reasoning_effort, "exclude": True},
        }
        if tools and iteration < MAX_TOOL_ITERATIONS:
            body["tools"] = TOOLS
        response = call_openrouter(key, body)
        choice = response["choices"][0]
        message = choice.get("message") or {}
        usage = response.get("usage") or {}
        totals["input_tokens"] += float(usage.get("prompt_tokens") or 0)
        totals["output_tokens"] += float(usage.get("completion_tokens") or 0)
        totals["cost_usd"] += float(usage.get("cost") or 0)
        if max_cost_usd is not None and totals["cost_usd"] > max_cost_usd:
            raise SystemExit(
                f"{stage} exceeded its remaining ${max_cost_usd:.4f} cost budget; "
                "partial review rejected"
            )
        calls = message.get("tool_calls") or []
        content = str(message.get("content") or "")
        if content and not calls:
            if choice.get("finish_reason") == "length":
                raise SystemExit(
                    f"{stage} output reached its {max_tokens}-token ceiling; "
                    "partial review rejected"
                )
            return content.strip(), totals
        if not calls:
            raise SystemExit("Reviewer returned neither content nor tool calls")
        messages.append({"role": "assistant", "content": content, "tool_calls": calls})
        for call in calls:
            fn = call.get("function") or {}
            try:
                arguments = json.loads(fn.get("arguments") or "{}")
            except json.JSONDecodeError:
                result = "ERROR: invalid tool arguments"
            else:
                result = execute_tool(str(fn.get("name") or ""), arguments)
            remaining = MAX_TOTAL_TOOL_RESULT_CHARS - tool_chars
            result = result[:max(0, remaining)]
            tool_chars += len(result)
            messages.append({
                "role": "tool", "tool_call_id": call.get("id") or "",
                "name": fn.get("name") or "", "content": result,
            })
            totals["tool_calls"] += 1
    raise SystemExit("Reviewer exhausted tool loop")


def shard_prompt(comp_id: str, shard: dict[str, object]) -> str:
    parts = [
        f"You are inspection pass {shard['id']} for {comp_id}. Read every supplied character. "
        "Audit implementation facts, load-bearing quantitative claims, constraints, provenance, "
        "summary fidelity, conjecture boundaries, and required follow-ups. Do not issue the final "
        "COMP verdict and do not retell or summarize the source. Return a compact audit ledger with "
        "exactly two sections: COVERAGE and MATERIAL_FINDINGS. COVERAGE has one INSPECTED_COMPLETE "
        "line per supplied segment with its exact path/range. MATERIAL_FINDINGS contains only "
        "distinct decision-relevant findings, each no more than 55 words and anchored to a supplied "
        "path/range. Consolidate duplicate evidence across segments. Use `none` when no material "
        "finding exists. Emit at most 60 findings; prioritize anything that could change validity, "
        "eligibility, a quantitative verdict, a claim boundary, or a required action.\n"
    ]
    for segment in shard["segments"]:
        parts.append(
            f"\n--- {segment['path']} [{segment['start']}:{segment['end']}] "
            f"role={segment['role']} sha256={segment['file_sha256']} ---\n{segment['content']}"
        )
    return "".join(parts)


def parse_final(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines()[:20]:
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    required = {
        "COMP_VERDICT", "PROPAGATION_ELIGIBILITY", "SYNTHESIS_ELIGIBILITY",
        "ACTION_REQUIRED", "REVIEWED_SNAPSHOT", "PROPAGATION_ALLOWED_SCOPE",
        "SYNTHESIS_ALLOWED_SCOPE", "FORBIDDEN_INFERENCES",
    }
    missing = required - fields.keys()
    if missing:
        raise SystemExit(f"Reviewer omitted structured fields: {sorted(missing)}")
    if fields["COMP_VERDICT"] not in VERDICTS:
        raise SystemExit("Reviewer returned invalid COMP_VERDICT")
    if fields["PROPAGATION_ELIGIBILITY"] not in ELIGIBILITY or fields["SYNTHESIS_ELIGIBILITY"] not in ELIGIBILITY:
        raise SystemExit("Reviewer returned invalid eligibility")
    if fields["ACTION_REQUIRED"] not in {"yes", "no"}:
        raise SystemExit("Reviewer returned invalid ACTION_REQUIRED")
    return fields


def queue_action_excerpt(final_text: str) -> str:
    """Keep the active queue actionable; Git and the receipt hold review detail."""
    sections: dict[str, str] = {}
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", final_text, re.M))
    for index, match in enumerate(matches):
        heading = match.group(1).strip().lower()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(final_text)
        sections[heading] = final_text[match.end():end].strip()

    verdict = sections.get("bottom-line verdict", "")
    actions = sections.get("required actions", "")
    if not actions:
        return "The review left an action open. Read the current receipt and resolve the finding."

    context = re.split(r"\n\s*\n", verdict, maxsplit=1)[0].strip() if verdict else ""
    parts = []
    if context:
        parts.append(f"**Why action remains open:** {context}")
    parts.append("## Required actions\n\n" + actions)
    return "\n\n".join(parts)


def write_receipts(
    *, comp_dir: Path, comp_rel: str, comp_id: str, commit_sha: str,
    manifest_sha: str, model: str, final_text: str, fields: dict[str, str],
    authoring_gates: dict[str, object], shards: list[dict[str, object]],
    binary: list[dict[str, object]], usage: dict[str, float], projected_cost: float,
) -> tuple[Path, Path, Path | None]:
    reviews = comp_dir / "reviews"
    reviews.mkdir(parents=True, exist_ok=True)
    receipt_json = reviews / "push-review.json"
    receipt_md = reviews / "push-review.md"
    coverage = [
        {
            "shard_id": shard["id"], "coverage_sha256": shard["coverage_sha256"],
            "segments": [
                {k: v for k, v in segment.items() if k not in {"content"}}
                for segment in shard["segments"]
            ],
        }
        for shard in shards
    ]
    document = {
        "schema_version": 1,
        "comp": comp_id,
        "comp_dir": comp_rel,
        "source_commit": commit_sha,
        "artifact_manifest_sha256": manifest_sha,
        "reviewer_model": model,
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "comp_verdict": fields["COMP_VERDICT"],
        "propagation_eligibility": fields["PROPAGATION_ELIGIBILITY"],
        "synthesis_eligibility": fields["SYNTHESIS_ELIGIBILITY"],
        "action_required": fields["ACTION_REQUIRED"] == "yes",
        "authoring_gates": authoring_gates,
        "coverage": coverage,
        "unsupported_binary_entries": [{k: v for k, v in item.items() if k != "content"} for item in binary],
        "projected_cost_usd": round(projected_cost, 6),
        "actual_cost_usd": round(usage["cost_usd"], 6),
        "input_tokens": int(usage["input_tokens"]),
        "output_tokens": int(usage["output_tokens"]),
        "tool_calls": int(usage["tool_calls"]),
        "review_sha256": sha256_bytes(final_text.encode()),
        "lane_adjudication": {
            "date": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "method": "exact push review",
            "new_artifact_review_performed": True,
            "queue_action_remains_open": fields["ACTION_REQUIRED"] == "yes",
            "propagation_allowed_scope": fields["PROPAGATION_ALLOWED_SCOPE"],
            "synthesis_allowed_scope": fields["SYNTHESIS_ALLOWED_SCOPE"],
            "forbidden_inferences": [
                item.strip() for item in fields["FORBIDDEN_INFERENCES"].split(";")
                if item.strip() and item.strip().lower() != "none"
            ],
        },
    }
    receipt_json.write_text(json.dumps(document, indent=2) + "\n")
    receipt_md.write_text(final_text.rstrip() + "\n")

    queue_path: Path | None = None
    stable_queue_path = ROOT / "synthesis" / "queue" / f"comp-review-{comp_id.removeprefix('comp-')}.md"
    if (
        document["action_required"]
        or fields["PROPAGATION_ELIGIBILITY"] == "blocked"
        or fields["SYNTHESIS_ELIGIBILITY"] == "blocked"
    ):
        queue_path = stable_queue_path
        queue_path.write_text(
            "---\n"
            "type: comp-review\n"
            f"comp: {comp_id}\n"
            f"source_commit: {commit_sha}\n"
            f"propagation_eligibility: {fields['PROPAGATION_ELIGIBILITY']}\n"
            f"synthesis_eligibility: {fields['SYNTHESIS_ELIGIBILITY']}\n"
            "---\n\n"
            f"# Current independent artifact review: {comp_id}\n\n"
            f"Current receipt: [`{receipt_md.relative_to(ROOT)}`](../../{receipt_md.relative_to(ROOT).as_posix()})\n\n"
            + queue_action_excerpt(final_text).rstrip() + "\n"
        )
    elif stable_queue_path.exists():
        stable_queue_path.unlink()
    return receipt_md, receipt_json, queue_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--comp-dir", required=True)
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--diff-base")  # retained for workflow compatibility
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--prompt-file", default=str(DEFAULT_PROMPT))
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--max-cost-usd", type=float, default=DEFAULT_MAX_COST_USD)
    parser.add_argument("--estimated-input-usd-per-million", type=float, default=DEFAULT_ESTIMATED_INPUT_USD_PER_M)
    parser.add_argument("--estimated-output-usd-per-million", type=float, default=DEFAULT_ESTIMATED_OUTPUT_USD_PER_M)
    args = parser.parse_args()

    comp_dir, comp_rel, comp_id = resolve_comp(args.comp_dir)
    commit_sha = run(["git", "rev-parse", args.commit_sha]).stdout.strip()
    reviews = comp_dir / "reviews"
    reviews.mkdir(parents=True, exist_ok=True)
    manifest_path = reviews / (
        "push-review.preflight.manifest.json" if args.prepare_only
        else "push-review.manifest.json"
    )
    manifest_sha = create_push_manifest(comp_rel, manifest_path)
    authoring_gates = verify_authoring_gates(comp_dir)
    shards, binary = build_shards(comp_rel, comp_id, manifest_path)
    prompt_template = safe_path(args.prompt_file).read_text()
    total_chars = sum(int(shard["chars"]) for shard in shards) + len(prompt_template)
    projected = estimate_cost(
        total_chars,
        output_tokens=(
            len(shards) * SHARD_OUTPUT_MAX_TOKENS
            + FINAL_OUTPUT_MAX_TOKENS
        ),
        input_rate=args.estimated_input_usd_per_million,
        output_rate=args.estimated_output_usd_per_million,
    )
    metadata = {
        "comp": comp_id, "manifest_sha256": manifest_sha,
        "shards": len(shards), "segments": sum(len(s["segments"]) for s in shards),
        "binary_entries": len(binary), "projected_cost_usd": round(projected, 6),
        "max_cost_usd": args.max_cost_usd, "authoring_gates": authoring_gates,
    }
    print(json.dumps(metadata, indent=2), file=sys.stderr)
    if projected > args.max_cost_usd:
        raise SystemExit(
            f"Projected complete-review cost ${projected:.4f} exceeds cap ${args.max_cost_usd:.4f}; "
            "COMP remains unreviewed"
        )
    if args.prepare_only:
        print(json.dumps(metadata))
        manifest_path.unlink(missing_ok=True)
        try:
            reviews.rmdir()
        except OSError:
            pass
        return

    key = api_key()
    audits: list[str] = []
    totals = {"input_tokens": 0.0, "output_tokens": 0.0, "tool_calls": 0.0, "cost_usd": 0.0}
    for shard in shards:
        audit, usage = review(
            key,
            args.model,
            shard_prompt(comp_id, shard),
            tools=False,
            max_tokens=SHARD_OUTPUT_MAX_TOKENS,
            reasoning_effort="low",
            max_cost_usd=max(0.0, args.max_cost_usd - totals["cost_usd"]),
            stage=f"{comp_id} {shard['id']}",
        )
        audits.append(f"## {shard['id']} ({shard['coverage_sha256']})\n\n{audit}")
        for key_name in totals:
            totals[key_name] += usage[key_name]
        if totals["cost_usd"] > args.max_cost_usd:
            raise SystemExit("Provider-reported cost exceeded cap before complete review; no eligibility receipt written")

    deterministic_blocks = []
    if not authoring_gates["valid"]:
        deterministic_blocks.append("authoring-time gate binding is incomplete or invalid")
    if binary:
        deterministic_blocks.append("one or more binary artifacts lack an inspectable text/rendered representation")
    final_prompt = (
        prompt_template
        + "\n\nDAEMON REVIEW MODE\n"
        + f"COMP: {comp_id}\nREVIEWED_SNAPSHOT: {manifest_sha}\nSOURCE_COMMIT: {commit_sha}\n"
        + f"AUTHORING_GATES: {json.dumps(authoring_gates)}\n"
        + f"DETERMINISTIC_BLOCKS: {json.dumps(deterministic_blocks)}\n"
        + "The shard auditors below inspected every text segment in the coverage receipt. "
          "Consolidate them, perform cross-file checks, and use repository tools only for targeted verification. "
          "Any deterministic block forces both eligibility fields to blocked.\n\n"
        + "\n\n".join(audits)
    )
    final_text, final_usage = review(
        key,
        args.model,
        final_prompt,
        tools=True,
        max_tokens=FINAL_OUTPUT_MAX_TOKENS,
        reasoning_effort="medium",
        max_cost_usd=max(0.0, args.max_cost_usd - totals["cost_usd"]),
        stage=f"{comp_id} final consolidation",
    )
    for key_name in totals:
        totals[key_name] += final_usage[key_name]
    if totals["cost_usd"] > args.max_cost_usd:
        raise SystemExit("Provider-reported complete-review cost exceeded cap; no eligibility receipt written")
    fields = parse_final(final_text)
    if fields["REVIEWED_SNAPSHOT"] != manifest_sha:
        raise SystemExit("Reviewer did not bind verdict to exact push manifest")
    if deterministic_blocks and (
        fields["PROPAGATION_ELIGIBILITY"] != "blocked" or fields["SYNTHESIS_ELIGIBILITY"] != "blocked"
    ):
        raise SystemExit("Reviewer attempted to override a deterministic eligibility block")

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", dir=ROOT, delete=False
    ) as handle:
        handle.write(final_text.rstrip() + "\n")
        verification_path = Path(handle.name)
    try:
        verification = run(
            [
                sys.executable, "scripts/comp-review-manifest.py", "check",
                "--manifest", str(manifest_path), "--review", str(verification_path),
                "--required-line", f"COMP_VERDICT: {fields['COMP_VERDICT']}",
            ],
            check=False,
        )
    finally:
        verification_path.unlink(missing_ok=True)
    if verification.returncode:
        raise SystemExit(
            "Push review receipt failed exact manifest verification: "
            + (verification.stderr or verification.stdout).strip()
        )

    receipt_md, receipt_json, queue = write_receipts(
        comp_dir=comp_dir, comp_rel=comp_rel, comp_id=comp_id,
        commit_sha=commit_sha, manifest_sha=manifest_sha, model=args.model,
        final_text=final_text, fields=fields, authoring_gates=authoring_gates,
        shards=shards, binary=binary, usage=totals, projected_cost=projected,
    )
    print(f"COMP_ID={comp_id}")
    print(f"MANIFEST_SHA256={manifest_sha}")
    print(f"REVIEW_RECEIPT={receipt_md.relative_to(ROOT)}")
    print(f"REVIEW_JSON={receipt_json.relative_to(ROOT)}")
    print(f"COMP_VERDICT={fields['COMP_VERDICT']}")
    print(f"PROPAGATION_ELIGIBILITY={fields['PROPAGATION_ELIGIBILITY']}")
    print(f"SYNTHESIS_ELIGIBILITY={fields['SYNTHESIS_ELIGIBILITY']}")
    print(f"ACTION_REQUIRED={fields['ACTION_REQUIRED']}")
    print(f"ACTUAL_COST_USD={totals['cost_usd']:.6f}")
    if queue:
        print(f"QUEUE_FILE={queue.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
