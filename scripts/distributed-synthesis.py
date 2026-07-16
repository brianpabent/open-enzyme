#!/usr/bin/env python3
"""Distributed, source-rehydrated full-corpus synthesis.

The raw corpus is read twice into a provenance-bound atomic ledger. Every
unordered domain pair is then compared. Candidates are reopened against raw
source sections (and exact COMP receipts/outputs where applicable) before a
different-model reviewer may promote them. Successful runs write compatible
raw/review artifacts plus a machine-verifiable coverage receipt to a temporary
work directory; only reviewed queue items and compact state belong in Git.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import itertools
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

MISSION = (
    "Use red-teaming techniques to identify exploitable weaknesses in gout, "
    "then use creative engineering to exploit them. Any chassis, molecule, "
    "enzyme, or delivery method is one falsifiable track—not the project."
)

DOMAINS = (
    "urate-physiology",
    "inflammation-immunity",
    "enzyme-payloads",
    "delivery-chassis",
    "molecules-natural-products",
    "computation-validation",
    "safety-translation",
    "strategy-methods",
)

DOMAIN_TERMS = {
    "urate-physiology": ("urate", "uric", "abcc", "abcg2", "urat1", "glut9", "purine", "xanthine"),
    "inflammation-immunity": ("nlrp3", "inflam", "il-1", "complement", "immune", "neutrophil", "gsdmd"),
    "enzyme-payloads": ("uricase", "enzyme", "protein", "cassette", "fold", "protease", "kinetic"),
    "delivery-chassis": ("koji", "chassis", "delivery", "probiotic", "yeast", "bacteria", "ferment", "ecn"),
    "molecules-natural-products": ("compound", "inhibitor", "tcm", "natural product", "supplement", "molecule", "drug"),
    "computation-validation": ("comput", "model", "simulation", "assay", "experiment", "validation", "screen"),
    "safety-translation": ("safety", "toxic", "regulat", "clinical", "dose", "allergen", "off-target"),
    "strategy-methods": ("strategy", "mission", "method", "priority", "question", "decision", "portfolio"),
}

ATOM_TYPES = {
    "claim", "quantitative_result", "mechanism", "intervention", "assumption",
    "constraint", "negative_result", "contradiction", "open_question",
    "decision_rule", "track_status", "project_claim",
}

TYPE_HEADING = {
    "connection": "New Connections",
    "contradiction": "Contradictions",
    "experiment": "Experiments",
    "open-question": "Open Questions",
    "priority-action": "Priority Actions",
    "riskiest-assumption": "Riskiest Assumptions",
    "most-curious-thread": "Most Curious Threads",
}

MODEL_RATES = {
    "google/gemini-2.5-flash": (0.30, 2.50),
    "deepseek/deepseek-v4-pro": (0.435, 0.87),
    "openai/gpt-5.5": (2.50, 15.00),
}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
COMP_RE = re.compile(r"\bcomp-(\d{3})\b", re.I)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_hash(value: Any) -> str:
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()


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


def parse_json_response(text: str) -> Any:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        return json.loads(stripped)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Model response is not valid JSON: {exc}: {stripped[:500]}") from exc


@dataclass
class CostLedger:
    cap: float
    calls: list[dict[str, Any]] = field(default_factory=list)

    @property
    def actual(self) -> float:
        return sum(float(call["cost_usd"]) for call in self.calls)

    def project(self, model: str, input_chars: int, max_output_tokens: int) -> float:
        in_rate, out_rate = MODEL_RATES.get(model, (10.0, 30.0))
        return input_chars / 4 / 1_000_000 * in_rate + max_output_tokens / 1_000_000 * out_rate

    def authorize(self, model: str, input_chars: int, max_output_tokens: int) -> float:
        projection = self.project(model, input_chars, max_output_tokens)
        if self.actual + projection > self.cap:
            raise RuntimeError(
                f"Next complete stage call projects ${self.actual + projection:.4f}, "
                f"above hard cap ${self.cap:.4f}"
            )
        return projection

    def record(self, *, stage: str, model: str, usage: dict[str, Any], projection: float, latency: float) -> None:
        provider_cost = usage.get("cost")
        estimated = provider_cost is None
        if estimated:
            in_rate, out_rate = MODEL_RATES.get(model, (10.0, 30.0))
            cost = (
                int(usage.get("prompt_tokens") or 0) * in_rate
                + int(usage.get("completion_tokens") or 0) * out_rate
            ) / 1_000_000
            cost = max(cost, projection)
        else:
            cost = float(provider_cost)
        self.calls.append({
            "stage": stage,
            "model": model,
            "input_tokens": int(usage.get("prompt_tokens") or 0),
            "output_tokens": int(usage.get("completion_tokens") or 0),
            "cached_tokens": int((usage.get("prompt_tokens_details") or {}).get("cached_tokens") or 0),
            "cost_usd": cost,
            "cost_estimated": estimated,
            "latency_seconds": round(latency, 3),
        })
        if self.actual > self.cap:
            raise RuntimeError(f"Provider cost ${self.actual:.4f} exceeded hard cap ${self.cap:.4f}")


class OpenRouter:
    def __init__(self, key: str, ledger: CostLedger):
        self.key = key
        self.ledger = ledger

    def json_call(self, *, stage: str, model: str, prompt: str, max_tokens: int) -> Any:
        projection = self.ledger.authorize(model, len(prompt), max_tokens)
        body = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.15,
            "max_tokens": max_tokens,
            "response_format": {"type": "json_object"},
        }
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(body, handle)
            body_path = handle.name
        try:
            for attempt, delay in enumerate((0, 5, 20), start=1):
                if delay:
                    time.sleep(delay)
                started = time.monotonic()
                result = subprocess.run(
                    [
                        "curl", "-sS", "--fail-with-body", "--http1.1",
                        "https://openrouter.ai/api/v1/chat/completions",
                        "-H", f"Authorization: Bearer {self.key}",
                        "-H", "Content-Type: application/json",
                        "-H", "HTTP-Referer: https://github.com/brianpabent/open-enzyme",
                        "-H", "X-Title: Open Enzyme distributed synthesis",
                        "-d", f"@{body_path}", "--max-time", "900",
                    ],
                    cwd=ROOT, text=True, capture_output=True, timeout=920,
                )
                latency = time.monotonic() - started
                if result.returncode == 0:
                    response = json.loads(result.stdout)
                    choice = response["choices"][0]
                    if choice.get("finish_reason") == "length":
                        raise RuntimeError(f"{stage} output truncated")
                    content = (choice.get("message") or {}).get("content") or ""
                    self.ledger.record(
                        stage=stage, model=model, usage=response.get("usage") or {},
                        projection=projection, latency=latency,
                    )
                    return parse_json_response(content)
                if attempt == 3:
                    raise RuntimeError(f"OpenRouter {stage} failed: {(result.stderr or result.stdout)[:1000]}")
        finally:
            os.unlink(body_path)
        raise AssertionError("unreachable")


def source_files() -> list[Path]:
    paths = list((ROOT / "wiki").glob("*.md")) + list((ROOT / "wiki" / "hypotheses").glob("*.md"))
    mission = ROOT / "wiki" / "etc" / "open-enzyme-vision.md"
    if mission.exists():
        paths.append(mission)
    return sorted(set(paths))


def domain_for(path: str, heading: str, text: str) -> str:
    sample = f"{path} {heading} {text[:1200]}".lower()
    scores = {
        domain: sum(sample.count(term) for term in terms)
        for domain, terms in DOMAIN_TERMS.items()
    }
    best = max(DOMAINS, key=lambda domain: (scores[domain], -DOMAINS.index(domain)))
    return best if scores[best] else "strategy-methods"


def sections(path: Path, max_chars: int = 80_000) -> list[dict[str, Any]]:
    rel = path.relative_to(ROOT).as_posix()
    lines = path.read_text(errors="replace").splitlines(keepends=True)
    starts = [(0, "Document")]
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line.rstrip("\n"))
        if match:
            starts.append((index, match.group(2)))
    starts = sorted(set(starts))
    result: list[dict[str, Any]] = []
    for position, (start, heading) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
        text = "".join(lines[start:end])
        if not text.strip():
            continue
        for offset in range(0, len(text), max_chars):
            chunk = text[offset:offset + max_chars]
            prefix_lines = text[:offset].count("\n")
            start_line = start + prefix_lines + 1
            end_line = start_line + chunk.count("\n")
            section_id = sha256(f"{rel}:{start_line}:{end_line}:{sha256(chunk.encode())}".encode())[:20]
            result.append({
                "section_id": section_id,
                "path": rel,
                "heading": heading,
                "start_line": start_line,
                "end_line": end_line,
                "sha256": sha256(chunk.encode()),
                "domain": domain_for(rel, heading, chunk),
                "text": chunk,
            })
    return result


def corpus_inventory() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    all_sections = [section for path in source_files() for section in sections(path)]
    files = []
    for path in source_files():
        raw = path.read_bytes()
        files.append({
            "path": path.relative_to(ROOT).as_posix(), "bytes": len(raw), "sha256": sha256(raw),
            "sections": sum(s["path"] == path.relative_to(ROOT).as_posix() for s in all_sections),
        })
    manifest = {
        "schema_version": 1,
        "coverage_commit": git("rev-parse", "HEAD"),
        "files": files,
        "section_count": len(all_sections),
    }
    manifest["corpus_sha256"] = canonical_hash(manifest)
    return all_sections, manifest


def pack_sections(all_sections: list[dict[str, Any]], max_chars: int = 130_000) -> list[list[dict[str, Any]]]:
    shards: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    chars = 0
    for section in all_sections:
        size = len(section["text"])
        if current and chars + size > max_chars:
            shards.append(current)
            current, chars = [], 0
        current.append(section)
        chars += size
    if current:
        shards.append(current)
    return shards


def extraction_prompt(shard: list[dict[str, Any]], residue: bool) -> str:
    mode = (
        "This is independent residue pass B. Emit only details, exceptions, qualifiers, "
        "numbers, negative evidence, relationships, uncertainties, or disputes that a conventional extraction could miss."
        if residue else
        "This is atomic extraction pass A. Capture every scientifically meaningful claim, number, mechanism, assumption, constraint, negative result, decision rule, track status, and actual project claim."
    )
    header = f"""Mission: {MISSION}
{mode}
Read every SOURCE_SECTION in full. Do not summarize the document. Do not reconcile or improve claims.
Return one JSON object: {{"atoms": [{{"type": one of {sorted(ATOM_TYPES)}, "statement": "atomic statement", "section_id": "supplied id", "path": "supplied path", "start_line": int, "end_line": int, "evidence_level": "Clinical Trial|Animal Model|In Vitro|Mechanistic Extrapolation|Computational|Project decision|Unstated", "excerpt": "short exact source excerpt", "domain": "supplied domain", "dispute": "optional"}}], "covered_section_ids": ["every supplied id"]}}.
Every supplied section id must appear in covered_section_ids even when it yields no atoms.
"""
    bodies = []
    for section in shard:
        bodies.append(
            f"\n<SOURCE_SECTION id={section['section_id']} path={section['path']} "
            f"lines={section['start_line']}-{section['end_line']} domain={section['domain']}>\n"
            f"{section['text']}\n</SOURCE_SECTION>"
        )
    return header + "".join(bodies)


def validate_extraction(payload: Any, expected: set[str]) -> list[dict[str, Any]]:
    if not isinstance(payload, dict) or not isinstance(payload.get("atoms"), list):
        raise RuntimeError("Extraction payload lacks atoms array")
    covered = set(payload.get("covered_section_ids") or [])
    if covered != expected:
        raise RuntimeError(f"Extraction coverage mismatch: missing={sorted(expected-covered)} extra={sorted(covered-expected)}")
    atoms = []
    for atom in payload["atoms"]:
        if atom.get("section_id") not in expected or atom.get("type") not in ATOM_TYPES:
            raise RuntimeError("Extraction emitted invalid atom provenance or type")
        statement = str(atom.get("statement") or "").strip()
        excerpt = str(atom.get("excerpt") or "").strip()
        if not statement or not excerpt:
            raise RuntimeError("Extraction atom lacks statement or source excerpt")
        atom = dict(atom)
        atom["atom_id"] = sha256(
            f"{atom['section_id']}:{atom['type']}:{statement.lower()}:{excerpt}".encode()
        )[:24]
        atoms.append(atom)
    return atoms


def merge_atoms(atoms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    for atom in atoms:
        key = (
            atom["section_id"], atom["type"],
            re.sub(r"\s+", " ", atom["statement"].lower()).strip(), atom["excerpt"],
        )
        if key not in merged:
            merged[key] = dict(atom, extraction_passes=[])
        source_pass = atom.get("extraction_pass")
        if source_pass and source_pass not in merged[key]["extraction_passes"]:
            merged[key]["extraction_passes"].append(source_pass)
        if atom.get("dispute"):
            merged[key].setdefault("disputes", []).append(atom["dispute"])
    return sorted(merged.values(), key=lambda atom: (atom["domain"], atom["path"], atom["start_line"], atom["atom_id"]))


def active_queue_fingerprints() -> str:
    rows = []
    for path in sorted((ROOT / "synthesis" / "queue").glob("*.md")):
        text = path.read_text(errors="replace")
        headline = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), path.stem)
        rows.append(f"- {path.name}: {headline}")
    return "\n".join(rows)[:60_000] or "(active queue empty)"


def bridge_prompt(domain_a: str, domain_b: str, atoms_a: list[dict[str, Any]], atoms_b: list[dict[str, Any]], triggers: list[str]) -> str:
    compact = lambda atoms: [
        {k: atom.get(k) for k in ("atom_id", "type", "statement", "path", "start_line", "end_line", "evidence_level", "excerpt", "disputes")}
        for atom in atoms
    ]
    return f"""Mission: {MISSION}
Compare the COMPLETE atomic ledgers for domains {domain_a} and {domain_b}. Trigger paths are attention hints, never scope filters: {triggers}.
Seek non-obvious connections, contradictions, transferable engineering patterns, shared constraints, discriminating experiments, and real project assumptions worth challenging. Do not invent a project claim to rebut. A track-local failure is not mission failure. Suppress restatements of this active queue:\n{active_queue_fingerprints()}
Return JSON {{"compared_domains": ["{domain_a}", "{domain_b}"], "candidates": [{{"type": "connection|contradiction|experiment|open-question|priority-action|riskiest-assumption|most-curious-thread", "headline": "...", "hypothesis": "...", "atom_ids": ["at least one from each domain unless contradiction is intra-constraint"], "why_novel": "..."}}]}}. Emit at most the single strongest genuinely novel candidate for this pair; use an empty array rather than a weak restatement.
DOMAIN_A_ATOMS={json.dumps(compact(atoms_a), ensure_ascii=False)}
DOMAIN_B_ATOMS={json.dumps(compact(atoms_b), ensure_ascii=False)}
"""


def exact_source_packet(candidate: dict[str, Any], atom_by_id: dict[str, dict[str, Any]], state: dict[str, Any]) -> dict[str, Any]:
    selected = []
    comp_support: dict[str, Any] = {}
    for atom_id in candidate.get("atom_ids", []):
        if atom_id not in atom_by_id:
            raise RuntimeError(f"Candidate cites unknown atom {atom_id}")
        atom = atom_by_id[atom_id]
        path = ROOT / atom["path"]
        lines = path.read_text(errors="replace").splitlines()
        start = max(1, int(atom["start_line"]))
        end = min(len(lines), int(atom["end_line"]))
        source_text = "\n".join(lines[start - 1:end])
        if atom["excerpt"] not in source_text:
            raise RuntimeError(f"Atom excerpt no longer resolves in {atom['path']}:{start}")
        selected.append({"atom": atom, "raw_source": source_text})
        for match in COMP_RE.finditer(source_text):
            comp_id = f"comp-{match.group(1)}"
            review = state.get("comp_reviews", {}).get(comp_id)
            if not review:
                raise RuntimeError(f"Candidate uses {comp_id} without a current push-review receipt")
            if review.get("synthesis_eligibility") == "blocked":
                raise RuntimeError(f"Candidate uses synthesis-blocked {comp_id}")
            receipt_path = ROOT / review["review_receipt"]
            receipt_json = receipt_path.with_suffix(".json")
            manifest_path = ROOT / review["comp_dir"] / "reviews" / "push-review.manifest.json"
            if not receipt_path.exists() or not receipt_json.exists() or not manifest_path.exists():
                raise RuntimeError(f"Current receipt files missing for {comp_id}")
            manifest = json.loads(manifest_path.read_text())
            recorded_digest = manifest.get("manifest_sha256")
            digest_payload = {key: value for key, value in manifest.items() if key != "manifest_sha256"}
            if recorded_digest != canonical_hash(digest_payload):
                raise RuntimeError(f"Push-review manifest digest mismatch for {comp_id}")
            if recorded_digest != review.get("artifact_manifest_sha256"):
                raise RuntimeError(f"State points to a stale push-review manifest for {comp_id}")
            output_entries = [entry for entry in manifest["files"] if entry["kind"] == "generated_output"]
            exact_outputs = []
            output_chars = 0
            for entry in output_entries:
                output_path = ROOT / entry["path"]
                raw = output_path.read_bytes()
                if sha256(raw) != entry["sha256"]:
                    raise RuntimeError(f"Generated output changed after review: {entry['path']}")
                if output_path.suffix.lower() not in {
                    ".md", ".json", ".jsonl", ".csv", ".tsv", ".txt", ".yaml", ".yml", ".xml"
                }:
                    raise RuntimeError(
                        f"Candidate requires non-text generated output {entry['path']} without exact reviewable representation"
                    )
                content = raw.decode("utf-8", errors="replace")
                output_chars += len(content)
                if output_chars > 500_000:
                    raise RuntimeError(f"Exact generated-output packet for {comp_id} exceeds bounded review context")
                exact_outputs.append({"manifest_entry": entry, "content": content})
            comp_support[comp_id] = {
                "state": review,
                "receipt": json.loads(receipt_json.read_text()),
                "exact_generated_outputs": exact_outputs,
            }
    constraint_terms = set(re.findall(r"[a-z0-9-]{5,}", (candidate.get("hypothesis") or "").lower()))
    contrary = []
    for atom in atom_by_id.values():
        if atom["type"] not in {"constraint", "negative_result", "contradiction"}:
            continue
        overlap = constraint_terms & set(re.findall(r"[a-z0-9-]{5,}", atom["statement"].lower()))
        if len(overlap) >= 2 and atom["atom_id"] not in candidate.get("atom_ids", []):
            contrary.append(atom)
    return {
        "candidate": candidate,
        "rehydrated_sources": selected,
        "comp_support": comp_support,
        "contrary_constraint_atoms": contrary[:30],
    }


def review_prompt(packet: dict[str, Any]) -> str:
    return f"""Mission: {MISSION}
You are the independent adversarial reviewer. Judge this candidate only from the rehydrated raw sources, exact computational support, and contrary evidence below. Verify evidence tiers; reject invented project claims and restatements; test compartment, dose, timing, topology, host, assay, population, and safety constraints. A negative result kills only the supported scope. If genuinely novel and actionable, give the cheapest discriminating next step.
Return JSON {{"status": "supported|partial|contradicted|restatement|speculative-but-testable|rejected", "promote": true|false, "type": "connection|contradiction|experiment|open-question|priority-action|riskiest-assumption|most-curious-thread", "headline": "...", "body": "grounded Markdown with source paths and evidence levels", "review": "concise adversarial verdict", "cheapest_next_step": "... or none", "comp_limitations_carried": ["..."]}}.
PACKET={json.dumps(packet, ensure_ascii=False)}
"""


def raw_markdown(promoted: list[dict[str, Any]], manifest: dict[str, Any], diff_base: str, triggers: list[str], model: str) -> tuple[str, str]:
    frontmatter = (
        "---\n"
        f"commit: {manifest['coverage_commit']}\n"
        f"corpus_commit: {manifest['coverage_commit']}\n"
        f"diff_base: {diff_base}\n"
        f"trigger_files: {','.join(triggers)}\n"
        f"reviewer_model: {model}\n"
        "---\n\n"
        f"# Distributed synthesis — {dt.date.today().isoformat()}\n\n"
    )
    if not promoted:
        return frontmatter + "**Status:** No new synthesis. All candidates were rejected or restatements.\n", "EXPLICIT_NO_OP\n"
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in promoted:
        grouped.setdefault(item["type"], []).append(item)
    chunks = [frontmatter]
    reviews = []
    for kind in TYPE_HEADING:
        if kind not in grouped:
            continue
        chunks.append(f"## {TYPE_HEADING[kind]}\n\n")
        for index, item in enumerate(grouped[kind], start=1):
            chunks.append(f"### {index}. {item['headline']}\n\n{item['body'].strip()}\n\n{{{{PEER-REVIEW}}}}\n\n")
            reviews.append(
                f"> **Pass 3 review — {item['status']}.** {item['review']}"
                + (f" Cheapest next step: {item['cheapest_next_step']}" if item.get("cheapest_next_step") not in {None, "", "none"} else "")
            )
    return "".join(chunks), "\n<<<NEXT>>>\n".join(reviews) + "\n"


def deduplicate_promoted(items: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]:
    """Suppress same-run duplicate headlines before they enter the active queue."""
    kept: list[dict[str, Any]] = []
    removed: list[str] = []
    seen: set[tuple[str, str]] = set()
    for item in items:
        headline = re.sub(r"[^a-z0-9]+", " ", item["headline"].lower()).strip()
        key = (item["type"], headline)
        if key in seen:
            removed.append(item["candidate_id"])
            continue
        seen.add(key)
        kept.append(item)
    return kept, removed


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def validate_coverage_receipt(receipt: dict[str, Any]) -> None:
    errors = []
    if receipt.get("status") != "complete":
        errors.append("status is not complete")
    section_count = receipt.get("section_count")
    if receipt.get("pass_a_covered_sections") != section_count:
        errors.append("pass A section coverage is incomplete")
    if receipt.get("pass_b_covered_sections") != section_count:
        errors.append("pass B section coverage is incomplete")
    expected_pairs = len(list(itertools.combinations(DOMAINS, 2)))
    if receipt.get("domain_pairs_expected") != expected_pairs or receipt.get("domain_pairs_completed") != expected_pairs:
        errors.append("domain-pair coverage is incomplete")
    rehydrated = receipt.get("rehydrated_candidate_ids") or []
    reviewed = receipt.get("reviewed_candidate_ids") or []
    if len(rehydrated) != receipt.get("candidate_count") or set(rehydrated) != set(reviewed):
        errors.append("not every candidate was rehydrated and reviewed")
    if not set(receipt.get("promoted_candidate_ids") or []).issubset(set(reviewed)):
        errors.append("a promoted candidate lacks review")
    if float((receipt.get("cost") or {}).get("actual_usd", 0)) > float((receipt.get("cost") or {}).get("hard_cap_usd", 0)):
        errors.append("actual cost exceeds hard cap")
    recorded = receipt.get("coverage_receipt_sha256")
    payload = {key: value for key, value in receipt.items() if key != "coverage_receipt_sha256"}
    if recorded != canonical_hash(payload):
        errors.append("coverage receipt digest mismatch")
    if errors:
        raise RuntimeError("Invalid coverage receipt: " + "; ".join(errors))


def validate_trigger_comp_eligibility(trigger_paths: list[str], state: dict[str, Any]) -> None:
    """Fail before model spend when changed surfaces cite unavailable computation."""
    for raw_path in trigger_paths:
        path = ROOT / raw_path
        if not path.is_file():
            continue
        for match in COMP_RE.finditer(path.read_text(errors="replace")):
            comp_id = f"comp-{match.group(1)}"
            review = state.get("comp_reviews", {}).get(comp_id)
            if not review:
                raise RuntimeError(f"Trigger surface {raw_path} cites {comp_id} without current push review")
            if review.get("synthesis_eligibility") == "blocked":
                raise RuntimeError(f"Trigger surface {raw_path} cites synthesis-blocked {comp_id}")
            manifest_path = ROOT / review["comp_dir"] / "reviews" / "push-review.manifest.json"
            if not manifest_path.exists():
                raise RuntimeError(f"Push-review manifest missing for {comp_id}")
            manifest = json.loads(manifest_path.read_text())
            recorded = manifest.get("manifest_sha256")
            payload = {key: value for key, value in manifest.items() if key != "manifest_sha256"}
            if recorded != canonical_hash(payload) or recorded != review.get("artifact_manifest_sha256"):
                raise RuntimeError(f"Push-review binding is stale for {comp_id}")


def run_pipeline(args: argparse.Namespace) -> dict[str, Any]:
    work = Path(args.work_dir).resolve()
    work.mkdir(parents=True, exist_ok=True)
    state = json.loads((ROOT / "logs" / "sweep-state.json").read_text())
    validate_trigger_comp_eligibility(args.trigger_path, state)
    ledger = CostLedger(args.max_cost_usd)
    client = OpenRouter(api_key(), ledger)
    all_sections, corpus = corpus_inventory()
    write_json(work / "corpus-manifest.json", corpus)
    shards = pack_sections(all_sections)

    atoms: list[dict[str, Any]] = []
    coverage_a: set[str] = set()
    coverage_b: set[str] = set()
    for index, shard in enumerate(shards, start=1):
        expected = {section["section_id"] for section in shard}
        for pass_name, residue, model, coverage in (
            ("A", False, args.extractor_a_model, coverage_a),
            ("B", True, args.extractor_b_model, coverage_b),
        ):
            payload = client.json_call(
                stage=f"extract-{pass_name}-{index:03d}", model=model,
                prompt=extraction_prompt(shard, residue), max_tokens=args.extraction_max_tokens,
            )
            extracted = validate_extraction(payload, expected)
            for atom in extracted:
                atom["extraction_pass"] = pass_name
            atoms.extend(extracted)
            coverage.update(expected)
            write_json(work / f"extract-{pass_name}-{index:03d}.json", payload)

    expected_all = {section["section_id"] for section in all_sections}
    if coverage_a != expected_all or coverage_b != expected_all:
        raise RuntimeError("Dual extraction did not cover every section")
    merged = merge_atoms(atoms)
    write_json(work / "atomic-ledger.json", merged)
    by_domain = {domain: [atom for atom in merged if atom["domain"] == domain] for domain in DOMAINS}
    for domain, domain_atoms in by_domain.items():
        encoded = json.dumps(domain_atoms, ensure_ascii=False)
        if len(encoded) > args.max_domain_chars:
            raise RuntimeError(f"Atomic domain {domain} exceeds complete-pair context bound; refine atomization")

    pairs = list(itertools.combinations(DOMAINS, 2))
    candidates: list[dict[str, Any]] = []
    pair_receipts = []
    for domain_a, domain_b in pairs:
        payload = client.json_call(
            stage=f"bridge-{domain_a}--{domain_b}", model=args.bridge_model,
            prompt=bridge_prompt(domain_a, domain_b, by_domain[domain_a], by_domain[domain_b], args.trigger_path),
            max_tokens=args.bridge_max_tokens,
        )
        if payload.get("compared_domains") != [domain_a, domain_b] or not isinstance(payload.get("candidates"), list):
            raise RuntimeError(f"Bridge output invalid for {domain_a}/{domain_b}")
        if len(payload["candidates"]) > 1:
            raise RuntimeError(f"Bridge exceeded one-candidate bound for {domain_a}/{domain_b}")
        for candidate in payload["candidates"]:
            if candidate.get("type") not in TYPE_HEADING:
                raise RuntimeError("Bridge candidate has invalid type")
            candidate["domain_pair"] = [domain_a, domain_b]
            candidate["candidate_id"] = canonical_hash(candidate)[:24]
            candidates.append(candidate)
        receipt = {"domains": [domain_a, domain_b], "candidate_count": len(payload["candidates"])}
        pair_receipts.append(receipt)
        write_json(work / f"bridge-{domain_a}--{domain_b}.json", payload)

    atom_by_id = {atom["atom_id"]: atom for atom in merged}
    promoted = []
    rehydrated_ids = []
    reviewed_ids = []
    for candidate in candidates:
        packet = exact_source_packet(candidate, atom_by_id, state)
        write_json(work / "packets" / f"{candidate['candidate_id']}.json", packet)
        rehydrated_ids.append(candidate["candidate_id"])
        verdict = client.json_call(
            stage=f"review-{candidate['candidate_id']}", model=args.reviewer_model,
            prompt=review_prompt(packet), max_tokens=args.review_max_tokens,
        )
        if verdict.get("status") not in {
            "supported", "partial", "contradicted", "restatement", "speculative-but-testable", "rejected"
        } or not isinstance(verdict.get("promote"), bool):
            raise RuntimeError("Adversarial reviewer violated verdict contract")
        verdict["candidate_id"] = candidate["candidate_id"]
        write_json(work / "reviews" / f"{candidate['candidate_id']}.json", verdict)
        reviewed_ids.append(candidate["candidate_id"])
        if verdict["promote"]:
            if verdict.get("type") not in TYPE_HEADING or not verdict.get("headline") or not verdict.get("body"):
                raise RuntimeError("Promoted verdict lacks type, headline, or grounded body")
            promoted.append(verdict)

    promoted, deduplicated_ids = deduplicate_promoted(promoted)
    raw, reviews = raw_markdown(promoted, corpus, args.diff_base, args.trigger_path, args.bridge_model)
    raw_path = work / "distributed-synthesis.md"
    reviews_path = work / "distributed-reviews.txt"
    raw_path.write_text(raw)
    reviews_path.write_text(reviews)
    receipt = {
        "schema_version": 1,
        "status": "complete",
        "coverage_commit": corpus["coverage_commit"],
        "corpus_sha256": corpus["corpus_sha256"],
        "file_count": len(corpus["files"]),
        "section_count": len(expected_all),
        "pass_a_covered_sections": len(coverage_a),
        "pass_b_covered_sections": len(coverage_b),
        "domain_pairs_expected": len(pairs),
        "domain_pairs_completed": len(pair_receipts),
        "candidate_count": len(candidates),
        "rehydrated_candidate_ids": rehydrated_ids,
        "reviewed_candidate_ids": reviewed_ids,
        "promoted_candidate_ids": [item["candidate_id"] for item in promoted],
        "deduplicated_candidate_ids": deduplicated_ids,
        "raw_synthesis_sha256": sha256(raw.encode()),
        "reviews_sha256": sha256(reviews.encode()),
        "cost": {"actual_usd": ledger.actual, "hard_cap_usd": ledger.cap, "calls": ledger.calls},
        "models": {
            "extractor_a": args.extractor_a_model,
            "extractor_b": args.extractor_b_model,
            "bridge": args.bridge_model,
            "reviewer": args.reviewer_model,
        },
    }
    receipt["coverage_receipt_sha256"] = canonical_hash(receipt)
    validate_coverage_receipt(receipt)
    write_json(work / "coverage-receipt.json", receipt)
    return receipt


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--work-dir", required=True)
    result.add_argument("--diff-base", required=True)
    result.add_argument("--trigger-path", action="append", default=[])
    result.add_argument("--max-cost-usd", type=float, default=5.0)
    result.add_argument("--extractor-a-model", default="google/gemini-2.5-flash")
    result.add_argument("--extractor-b-model", default="deepseek/deepseek-v4-pro")
    result.add_argument("--bridge-model", default="deepseek/deepseek-v4-pro")
    result.add_argument("--reviewer-model", default="openai/gpt-5.5")
    result.add_argument("--extraction-max-tokens", type=int, default=6_000)
    result.add_argument("--bridge-max-tokens", type=int, default=2_500)
    result.add_argument("--review-max-tokens", type=int, default=2_500)
    result.add_argument("--max-domain-chars", type=int, default=500_000)
    return result


def main() -> None:
    args = parser().parse_args()
    receipt = run_pipeline(args)
    print(json.dumps({
        "coverage_commit": receipt["coverage_commit"],
        "coverage_receipt_sha256": receipt["coverage_receipt_sha256"],
        "promoted": len(receipt["promoted_candidate_ids"]),
        "cost_usd": receipt["cost"]["actual_usd"],
    }))


if __name__ == "__main__":
    main()
