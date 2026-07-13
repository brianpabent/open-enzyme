#!/usr/bin/env python3
"""Independent, bounded review for one Open Enzyme comp-NNN artifact.

The full wiki sweep intentionally excludes ``wiki/etc/experiments`` because
the artifact tree is too large for the shared synthesis context.  This driver
restores artifact-level scrutiny without putting every comp into every sweep:

* build a bounded evidence bundle from one comp's code, inputs, and outputs;
* inline every top-level wiki page that explicitly references the comp;
* surface a heuristic list of input keys not named literally in code;
* give a read-only reviewer repository tools for targeted follow-up;
* always write an auditable review log; and
* write a synthesis-queue item only when action is required.

The input-key scan is a search aid, not proof that a parameter is unused.
Dynamic iteration and renamed variables create false positives; the reviewer
must inspect the implementation before reaching a verdict.

Usage:
    python3 scripts/comp-review.py \
      --comp-dir wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime \
      --commit-sha HEAD --diff-base HEAD~1

    # Validate bundle construction without calling a model or writing files.
    python3 scripts/comp-review.py --comp-dir comp-044 --prepare-only
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
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
MAX_BUNDLE_CHARS = 750_000
MAX_INLINE_FILE_CHARS = 140_000
MAX_REFERENCE_CHARS = 220_000
MAX_TOOL_RESULT_CHARS = 80_000
MAX_TOTAL_TOOL_RESULT_CHARS = 240_000
MAX_TOOL_ITERATIONS = 8
TEXT_SUFFIXES = {
    ".md", ".py", ".json", ".csv", ".tsv", ".txt", ".yaml", ".yml",
    ".fasta", ".fa", ".toml", ".sh", ".r",
}
COMP_RE = re.compile(r"^comp-(\d{3})(?:-|$)")


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=check)


def safe_path(rel: str) -> Path:
    if "\0" in rel:
        raise ValueError("path contains a null byte")
    candidate = (ROOT / rel).resolve()
    if candidate != ROOT and ROOT not in candidate.parents:
        raise ValueError(f"path escapes repository: {rel}")
    return candidate


def resolve_comp(raw: str) -> tuple[Path, str, str]:
    raw = raw.rstrip("/")
    direct = safe_path(raw)
    candidates: list[Path]
    if direct.is_dir():
        candidates = [direct]
    else:
        token = Path(raw).name
        candidates = [Path(p).resolve() for p in glob.glob(
            f"wiki/etc/experiments/{token}*"
        ) if Path(p).is_dir()]
    if len(candidates) != 1:
        raise SystemExit(
            f"Expected exactly one comp directory for {raw!r}; found "
            f"{len(candidates)}: {[str(p) for p in candidates]}"
        )
    comp_dir = candidates[0]
    try:
        rel = comp_dir.relative_to(ROOT).as_posix()
    except ValueError as exc:
        raise SystemExit(f"Comp directory is outside repository: {comp_dir}") from exc
    match = COMP_RE.match(comp_dir.name)
    if not match:
        raise SystemExit(f"Not a comp-NNN directory: {rel}")
    return comp_dir, rel, f"comp-{match.group(1)}"


def tracked_files(comp_rel: str) -> list[Path]:
    result = run(["git", "ls-files", "--", comp_rel])
    return [safe_path(line) for line in result.stdout.splitlines() if line.strip()]


def priority(path: Path, comp_dir: Path) -> tuple[int, str]:
    rel = path.relative_to(comp_dir).as_posix()
    name = path.name.lower()
    if rel == "README.md" or name == "wiki-archive.md":
        return (0, rel)
    if path.suffix.lower() in {".py", ".r", ".sh"}:
        return (1, rel)
    if rel.startswith("inputs/") and (
        name == "provenance.md" or "parameter" in name or "query" in name
    ):
        return (2, rel)
    if rel.startswith("outputs/") and (
        "summary" in name or "result" in name or "sensitivity" in name
    ):
        return (3, rel)
    if rel.startswith("inputs/"):
        return (4, rel)
    if rel.startswith("outputs/"):
        return (5, rel)
    return (6, rel)


def read_text_bounded(path: Path, limit: int = MAX_INLINE_FILE_CHARS) -> tuple[str, str | None]:
    try:
        raw = path.read_text(errors="replace")
    except (OSError, UnicodeError) as exc:
        return "", f"unreadable: {exc}"
    if len(raw) > limit:
        return raw[:limit], f"truncated from {len(raw):,} to {limit:,} chars"
    return raw, None


def comp_references(comp_id: str, comp_rel: str) -> list[Path]:
    result = run(
        [
            "git", "grep", "-l", "-F", comp_id, "--",
            "wiki/*.md", "wiki/hypotheses/*.md",
        ],
        check=False,
    )
    paths = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line or line.startswith(comp_rel + "/"):
            continue
        parts = Path(line).parts
        is_top_level_wiki = len(parts) == 2 and parts[0] == "wiki"
        is_hypothesis = len(parts) == 3 and parts[:2] == ("wiki", "hypotheses")
        if not (is_top_level_wiki or is_hypothesis):
            continue
        path = safe_path(line)
        if path.is_file():
            paths.append(path)
    return sorted(set(paths))


def json_named_paths(value: object, prefix: str = "") -> list[str]:
    """Return dictionary-key paths at every depth, not only scalar leaves."""
    paths: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_prefix = f"{prefix}.{key}" if prefix else str(key)
            paths.append(child_prefix)
            paths.extend(json_named_paths(child, child_prefix))
    elif isinstance(value, list):
        for child in value[:25]:
            paths.extend(json_named_paths(child, prefix + "[]"))
    return paths


def input_key_heuristic(comp_dir: Path, files: list[Path]) -> list[str]:
    code = "\n".join(
        read_text_bounded(path, 250_000)[0]
        for path in files
        if path.suffix.lower() in {".py", ".r", ".sh"}
    )
    if not code:
        return ["(no executable text found; heuristic unavailable)"]

    candidates: set[str] = set()
    for path in files:
        rel = path.relative_to(comp_dir).as_posix()
        if not rel.startswith("inputs/") or path.suffix.lower() != ".json":
            continue
        if path.stat().st_size > 2_000_000:
            continue
        try:
            data = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        for named_path in json_named_paths(data):
            terminal = named_path.replace("[]", "").rsplit(".", 1)[-1]
            if terminal.startswith("_") or terminal in {
                "source", "sources", "tier", "note", "notes", "rationale",
                "citation", "citations", "url", "doi", "pmid", "date",
                "central", "low", "high", "min", "max", "mean", "median",
            }:
                continue
            if len(terminal) >= 4 and terminal not in code:
                candidates.add(named_path)
    high_signal_terms = (
        "km", "concentration", "oxygen", "peroxide", "residence", "time",
        "dose", "activity", "capacity", "rate", "fraction", "mass", "flux",
        "volume", "temperature", "ph", "survival", "access", "turnover",
    )
    return sorted(
        candidates,
        key=lambda path: (
            0 if any(term in path.lower() for term in high_signal_terms) else 1,
            path,
        ),
    )[:120]


def reference_priority(path: Path, comp_id: str) -> tuple[int, str]:
    """Put the summary/registry/decision surfaces ahead of incidental mentions."""
    name = path.name
    text = path.read_text(errors="replace")[:12_000]
    if name == "computational-experiments.md":
        return (0, name)
    if name == "validation-experiments.md":
        return (1, name)
    if path.parent.name == "hypotheses":
        return (2, path.as_posix())
    if name.endswith("-computational.md") and comp_id in text:
        return (3, name)
    if name in {"index.md", "open-questions.md"}:
        return (4, name)
    return (5, path.as_posix())


def diff_text(diff_base: str | None, commit_sha: str, comp_rel: str) -> str:
    if not diff_base:
        return "(no diff base supplied)"
    result = run(
        ["git", "diff", "--no-ext-diff", f"{diff_base}..{commit_sha}", "--", comp_rel],
        check=False,
    )
    text = result.stdout
    if len(text) > 160_000:
        return text[:160_000] + "\n... (diff truncated)"
    return text or "(no diff in comp directory for supplied range)"


def build_bundle(
    comp_dir: Path,
    comp_rel: str,
    comp_id: str,
    commit_sha: str,
    diff_base: str | None,
) -> tuple[str, dict[str, object]]:
    files = tracked_files(comp_rel)
    refs = comp_references(comp_id, comp_rel)
    inventory = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        inventory.append(f"- {rel} ({path.stat().st_size:,} bytes)")

    sections = [
        f"# Artifact review bundle: {comp_id}\n",
        f"Comp directory: `{comp_rel}`\nCommit: `{commit_sha}`\n",
        "## Complete tracked-file inventory\n\n" + "\n".join(inventory),
        "## Trigger diff\n\n```diff\n" + diff_text(diff_base, commit_sha, comp_rel) + "\n```",
    ]

    heuristic = input_key_heuristic(comp_dir, files)
    sections.append(
        "## Heuristic: input JSON leaf paths not named literally in executable code\n\n"
        "This is a search lead, not an unused-parameter verdict. Dynamic iteration, "
        "renaming, and documentation-only inputs produce false positives.\n\n" +
        ("\n".join(f"- `{key}`" for key in heuristic) if heuristic else "- (none)")
    )

    used = sum(len(s) for s in sections)
    included: list[str] = []
    skipped: list[str] = []
    for path in sorted(files, key=lambda p: priority(p, comp_dir)):
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() not in TEXT_SUFFIXES:
            skipped.append(f"{rel} (non-text suffix)")
            continue
        if path.stat().st_size > 5_000_000:
            skipped.append(f"{rel} ({path.stat().st_size:,} bytes; inventory only)")
            continue
        content, note = read_text_bounded(path)
        section = f"## Artifact file: `{rel}`\n\n```\n{content}\n```"
        if note:
            section += f"\n\n_Bundle note: {note}._"
        if used + len(section) > MAX_BUNDLE_CHARS:
            skipped.append(f"{rel} (bundle budget reached)")
            continue
        sections.append(section)
        included.append(rel)
        used += len(section)

    ref_used = 0
    ref_included: list[str] = []
    for path in sorted(refs, key=lambda p: reference_priority(p, comp_id)):
        rel = path.relative_to(ROOT).as_posix()
        content, note = read_text_bounded(path, 90_000)
        section = f"## Explicit referencing page: `{rel}`\n\n{content}"
        if note:
            section += f"\n\n_Bundle note: {note}._"
        if ref_used + len(section) > MAX_REFERENCE_CHARS:
            skipped.append(f"{rel} (reference-page budget reached)")
            continue
        sections.append(section)
        ref_included.append(rel)
        ref_used += len(section)

    sections.append(
        "## Bundle omissions\n\n" +
        ("\n".join(f"- {item}" for item in skipped) if skipped else "- (none)") +
        "\n\nUse repository tools when an omitted file is needed for a load-bearing check."
    )
    bundle = "\n\n".join(sections)
    metadata = {
        "comp_id": comp_id,
        "comp_dir": comp_rel,
        "tracked_files": len(files),
        "inlined_artifact_files": included,
        "explicit_reference_pages": [p.relative_to(ROOT).as_posix() for p in refs],
        "inlined_reference_pages": ref_included,
        "skipped": skipped,
        "bundle_chars": len(bundle),
        "rough_bundle_tokens": len(bundle) // 4,
        "heuristic_candidates": len(heuristic),
    }
    return bundle, metadata


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a repo-relative text file for a load-bearing audit check.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "start_byte": {
                        "type": "integer",
                        "minimum": 0,
                        "description": "Optional byte offset for chunked reads",
                    },
                    "max_bytes": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 80000,
                        "description": "Optional chunk size; maximum 80000 bytes",
                    },
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_directory",
            "description": "List a repo-relative directory before selecting files to read.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "grep_repo",
            "description": (
                "Fixed-string search across repository text. Use it to find affected wiki "
                "pages by mechanism or conclusion, not only by comp number."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "scope": {
                        "type": "string",
                        "description": "Optional repo-relative directory; default wiki",
                    },
                },
                "required": ["query"],
            },
        },
    },
]


def execute_tool(name: str, args: dict[str, object]) -> str:
    try:
        if name == "read_file":
            rel = str(args["path"])
            path = safe_path(rel)
            if not path.is_file():
                return f"ERROR: file not found: {rel}"
            if path.suffix.lower() not in TEXT_SUFFIXES:
                return f"ERROR: non-text file cannot be read: {rel}"
            start = max(0, int(args.get("start_byte") or 0))
            length = min(
                MAX_TOOL_RESULT_CHARS,
                max(1, int(args.get("max_bytes") or MAX_TOOL_RESULT_CHARS)),
            )
            total = path.stat().st_size
            if start >= total:
                return f"ERROR: start_byte {start} is beyond file size {total}"
            with path.open("rb") as handle:
                handle.seek(start)
                raw_chunk = handle.read(length)
            chunk = raw_chunk.decode("utf-8", errors="replace")
            note = (
                f"\n... [bytes {start:,}-{start + len(raw_chunk):,} of {total:,}]"
                if start + len(raw_chunk) < total or start > 0 else ""
            )
            return chunk + note
        if name == "list_directory":
            rel = str(args["path"])
            path = safe_path(rel)
            if not path.is_dir():
                return f"ERROR: directory not found: {rel}"
            entries = []
            for child in sorted(path.iterdir())[:500]:
                entries.append(child.name + ("/" if child.is_dir() else ""))
            return "\n".join(entries) or "(empty)"
        if name == "grep_repo":
            query = str(args["query"])
            if not query or len(query) > 300:
                return "ERROR: query must be 1-300 characters"
            scope = str(args.get("scope") or "wiki")
            safe_path(scope)
            result = run(
                ["rg", "-n", "-F", "--glob", "*.md", "--glob", "*.py",
                 "--glob", "*.json", "--", query, scope],
                check=False,
            )
            text = result.stdout or "(no matches)"
            return text[:MAX_TOOL_RESULT_CHARS]
        return f"ERROR: unknown tool {name!r}"
    except (KeyError, OSError, ValueError) as exc:
        return f"ERROR: {type(exc).__name__}: {exc}"


def api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if key:
        return key
    env_file = ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise SystemExit("OPENROUTER_API_KEY is not set")


def call_openrouter(key: str, body: dict[str, object]) -> dict[str, object]:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as handle:
        json.dump(body, handle)
        body_path = handle.name
    try:
        for attempt, delay in enumerate((0, 10, 30, 60), start=1):
            if delay:
                time.sleep(delay)
            result = subprocess.run(
                [
                    "curl", "-sS", "--fail-with-body", "--http1.1",
                    "https://openrouter.ai/api/v1/chat/completions",
                    "-H", f"Authorization: Bearer {key}",
                    "-H", "Content-Type: application/json",
                    "-H", "HTTP-Referer: https://github.com/brianpabent/open-enzyme",
                    "-H", "X-Title: Open Enzyme comp artifact review",
                    "-d", f"@{body_path}", "--max-time", "900",
                ],
                text=True,
                capture_output=True,
                timeout=920,
            )
            if result.returncode == 0:
                try:
                    parsed = json.loads(result.stdout)
                except json.JSONDecodeError:
                    parsed = None
                if parsed and parsed.get("choices"):
                    message = parsed["choices"][0].get("message") or {}
                    if message.get("content") or message.get("tool_calls"):
                        return parsed
            if attempt == 4:
                raise SystemExit(
                    f"OpenRouter failed after {attempt} attempts. "
                    f"stdout={result.stdout[:1200]!r} stderr={result.stderr[:1200]!r}"
                )
            print(f"OpenRouter attempt {attempt} failed; retrying", file=sys.stderr)
    finally:
        os.unlink(body_path)
    raise AssertionError("unreachable")


def review(key: str, model: str, prompt: str) -> tuple[str, dict[str, int]]:
    messages: list[dict[str, object]] = [{"role": "user", "content": prompt}]
    totals = {"input_tokens": 0, "output_tokens": 0, "tool_calls": 0}
    total_tool_result_chars = 0
    for iteration in range(MAX_TOOL_ITERATIONS + 1):
        force_final = iteration == MAX_TOOL_ITERATIONS
        body: dict[str, object] = {
            "model": model,
            "messages": messages,
            "tools": TOOLS,
            "temperature": 0.2,
            "max_tokens": 12_000,
        }
        if force_final:
            body["tool_choice"] = "none"
        response = call_openrouter(key, body)
        choice = response["choices"][0]
        message = choice.get("message") or {}
        usage = response.get("usage") or {}
        totals["input_tokens"] += int(usage.get("prompt_tokens") or 0)
        totals["output_tokens"] += int(usage.get("completion_tokens") or 0)
        tool_calls = message.get("tool_calls") or []
        content = message.get("content") or ""
        if content and not tool_calls:
            if choice.get("finish_reason") == "length":
                raise SystemExit("Comp review output truncated at max_tokens; refusing partial audit")
            return content.strip(), totals
        if not tool_calls:
            raise SystemExit("Reviewer returned neither content nor tool calls")
        messages.append({
            "role": "assistant",
            "content": content,
            "tool_calls": tool_calls,
        })
        for call in tool_calls:
            fn = call.get("function") or {}
            name = fn.get("name") or ""
            try:
                args = json.loads(fn.get("arguments") or "{}")
            except json.JSONDecodeError:
                result = "ERROR: tool arguments were not valid JSON"
            else:
                result = execute_tool(name, args)
            remaining = MAX_TOTAL_TOOL_RESULT_CHARS - total_tool_result_chars
            if remaining <= 0:
                result = (
                    "ERROR: total tool-result budget exhausted; finish the review from "
                    "the evidence already collected"
                )
            elif len(result) > remaining:
                result = result[:remaining] + "\n... (total tool-result budget reached)"
            total_tool_result_chars += len(result)
            messages.append({
                "role": "tool",
                "tool_call_id": call.get("id") or "",
                "name": name,
                "content": result,
            })
            totals["tool_calls"] += 1
    raise SystemExit("Comp review exhausted tool loop without a final answer")


def parse_action_required(text: str) -> bool:
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if first == "ACTION_REQUIRED: yes":
        return True
    if first == "ACTION_REQUIRED: no":
        return False
    raise SystemExit(
        "Reviewer violated output contract: first non-empty line must be "
        "ACTION_REQUIRED: yes or ACTION_REQUIRED: no"
    )


def write_outputs(
    comp_id: str,
    comp_rel: str,
    commit_sha: str,
    model: str,
    review_text: str,
    action_required: bool,
    metadata: dict[str, object],
    usage: dict[str, int],
) -> tuple[Path, Path | None]:
    date = dt.datetime.now(dt.timezone.utc).date().isoformat()
    sha7 = run(["git", "rev-parse", "--short=7", commit_sha]).stdout.strip()
    log_dir = ROOT / "logs" / "comp-reviews"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{date}-{comp_id}-{sha7}.md"
    header = (
        "---\n"
        "type: comp-review\n"
        f"date: {date}\n"
        f"comp: {comp_id}\n"
        f"comp_dir: {comp_rel}\n"
        f"trigger_sha: {sha7}\n"
        f"reviewer_model: {model}\n"
        f"action_required: {'true' if action_required else 'false'}\n"
        f"bundle_chars: {metadata['bundle_chars']}\n"
        f"rough_bundle_tokens: {metadata['rough_bundle_tokens']}\n"
        f"tool_calls: {usage['tool_calls']}\n"
        "---\n\n"
    )
    log_path.write_text(header + review_text + "\n")

    queue_path: Path | None = None
    if action_required:
        slug = Path(comp_rel).name.removeprefix(comp_id + "-")
        queue_path = ROOT / "synthesis" / "queue" / (
            f"{date}-comp-review-{comp_id.removeprefix('comp-')}-{slug}-{sha7}.md"
        )
        queue_header = (
            "---\n"
            "type: comp-review\n"
            f"sweep_date: {date}\n"
            f"sweep_sha: {sha7}\n"
            f"comp: {comp_id}\n"
            f"reviewer_model: {model}\n"
            "pass3_verdict: Independent comp audit\n"
            "overlap_tag: N/A\n"
            "---\n\n"
        )
        queue_path.write_text(
            queue_header +
            f"# Independent artifact review requires action: {comp_id}\n\n" +
            f"Canonical review log: [`{log_path.relative_to(ROOT)}`]"
            f"(../../{log_path.relative_to(ROOT).as_posix()})\n\n" +
            review_text + "\n"
        )
    return log_path, queue_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--comp-dir", required=True, help="Full path or comp-NNN prefix")
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--diff-base")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--prompt-file", default=str(DEFAULT_PROMPT))
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()

    comp_dir, comp_rel, comp_id = resolve_comp(args.comp_dir)
    commit_sha = run(["git", "rev-parse", args.commit_sha]).stdout.strip()
    bundle, metadata = build_bundle(
        comp_dir, comp_rel, comp_id, commit_sha, args.diff_base
    )
    print(json.dumps(metadata, indent=2), file=sys.stderr)
    if args.prepare_only:
        print(
            f"Prepared {comp_id}: {metadata['bundle_chars']:,} chars, "
            f"~{metadata['rough_bundle_tokens']:,} tokens, "
            f"{metadata['tracked_files']} tracked files, "
            f"{len(metadata['explicit_reference_pages'])} explicit reference pages"
        )
        return

    prompt_path = safe_path(args.prompt_file)
    prompt_template = prompt_path.read_text()
    initial_prompt = (
        prompt_template + "\n\n---\n\n" + bundle
    )
    review_text, usage = review(api_key(), args.model, initial_prompt)
    action_required = parse_action_required(review_text)
    log_path, queue_path = write_outputs(
        comp_id, comp_rel, commit_sha, args.model, review_text,
        action_required, metadata, usage,
    )
    print(f"REVIEW_LOG={log_path.relative_to(ROOT)}")
    print(f"ACTION_REQUIRED={'yes' if action_required else 'no'}")
    if queue_path:
        print(f"QUEUE_FILE={queue_path.relative_to(ROOT)}")
    print(
        f"USAGE=input:{usage['input_tokens']} output:{usage['output_tokens']} "
        f"tools:{usage['tool_calls']}"
    )


if __name__ == "__main__":
    main()
