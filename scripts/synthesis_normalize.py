#!/usr/bin/env python3
"""Normalize free-form Pass 2 Markdown into a canonical, hash-bound manifest.

The synthesizer reads roughly one million tokens and is intentionally allowed to
write natural Markdown. Downstream automation must not treat exact heading text
as a wire protocol. This module is the tolerant ingestion boundary:

* common heading variants are mapped to canonical item types;
* numbered structure and ``{{PEER-REVIEW}}`` markers are independent signals;
* every marker must be covered by a normalized item;
* zero items are valid only when Pass 2 explicitly says ``No new synthesis``;
* the raw artifact and normalized item payload are SHA-256 bound.

Ambiguity fails closed. The raw artifact and diagnostic manifest are still
preserved so formatting can be repaired without rerunning the full-corpus model.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


SCHEMA_VERSION = 1
MARKER = "{{PEER-REVIEW}}"

NUMBERED_TYPES = {
    "connection",
    "contradiction",
    "experiment",
    "open-question",
    "priority-action",
}
SINGLE_TYPES = {"riskiest-assumption", "most-curious-thread"}

NUMBERED_ITEM_RE = re.compile(
    r"^(?:###\s+)?(\d+)\.\s+(?:\*\*|[A-Z])", re.MULTILINE
)
NO_OP_RE = re.compile(
    r"^\s*(?:\*\*)?Status:(?:\*\*)?\s*No new synthesis\b.*$",
    re.IGNORECASE | re.MULTILINE,
)
ATX_HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)\s*$", re.MULTILINE)
BOLD_HEADING_RE = re.compile(r"^\s*\*\*([^*\n]+?)\*\*\s*$", re.MULTILINE)


class NormalizationError(ValueError):
    """Raised when a manifest or synthesis artifact violates the contract."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def stable_hash(value: object) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(encoded)


def strip_frontmatter(text: str) -> tuple[dict[str, str], str, int]:
    """Return simple YAML frontmatter, body, and body start offset.

    Pass 2 frontmatter is deliberately flat, so a small parser avoids adding a
    YAML dependency to the daemon runner.
    """
    if not text.startswith("---\n"):
        return {}, text, 0
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text, 0
    block = text[4:end]
    values: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    body_start = end + 5
    return values, text[body_start:], body_start


def normalize_heading(title: str) -> str:
    title = title.strip().strip("#").strip()
    title = title.replace("—", "-").replace("–", "-")
    title = re.sub(r"\s+", " ", title)
    return title.rstrip(":").casefold()


def heading_type(title: str) -> str | None:
    normalized = normalize_heading(title)
    if normalized in {"new connections", "connections", "phase c - synthesize"}:
        return "connection"
    if normalized in {"contradictions", "contradictions found"}:
        return "contradiction"
    if normalized.startswith("proposed experiments"):
        return "experiment"
    if normalized == "open questions":
        return "open-question"
    if normalized == "priority actions":
        return "priority-action"
    if normalized == "riskiest assumption":
        return "riskiest-assumption"
    if normalized == "most curious thread":
        return "most-curious-thread"
    return None


def find_headings(body: str) -> list[dict]:
    """Find section boundaries without confusing item formatting for sections.

    H3-numbered items and bold-only labels frequently occur inside findings, so
    only H1/H2 headings, recognized section headings at any ATX depth, and the
    explicit Sources-cited terminator are boundaries.
    """
    found: list[dict] = []
    for match in ATX_HEADING_RE.finditer(body):
        title = match.group(2).strip()
        level = len(match.group(1))
        if level > 2 and heading_type(title) is None:
            continue
        found.append({
            "start": match.start(),
            "end": match.end(),
            "title": title,
            "style": "atx",
        })
    for match in BOLD_HEADING_RE.finditer(body):
        title = match.group(1).strip()
        if heading_type(title) is None and normalize_heading(title) != "sources cited":
            continue
        found.append({
            "start": match.start(),
            "end": match.end(),
            "title": title,
            "style": "bold",
        })
    found.sort(key=lambda h: (h["start"], h["end"]))
    # An ATX heading whose text is bold can overlap a bold-only match in odd
    # model output. Keep the widest boundary once.
    deduped: list[dict] = []
    for heading in found:
        if deduped and heading["start"] == deduped[-1]["start"]:
            if heading["end"] > deduped[-1]["end"]:
                deduped[-1] = heading
            continue
        deduped.append(heading)
    return deduped


def extract_headline(content: str, type_slug: str, fallback_index: int) -> str:
    if type_slug in NUMBERED_TYPES:
        match = re.search(
            r"^(?:###\s+)?\d+\.\s+\*\*(.+?)\*\*",
            content,
            re.MULTILINE | re.DOTALL,
        )
        if match:
            return match.group(1).strip().rstrip(".")
        match = re.search(r"^###\s+\d+\.\s+(.+?)(?:\.\s*$|\s*$)", content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    else:
        text = re.sub(r"^\s*\*\*", "", content.strip())
        match = re.match(r"([^.!?\n]+[.!?])", text)
        if match:
            return re.sub(r"\*\*", "", match.group(1)).strip()
        first = re.sub(r"\*\*", "", text.splitlines()[0] if text else "").strip()
        if first:
            return first[:160]
    return f"unnamed-item-{fallback_index}"


def clean_item_content(content: str) -> str:
    return content.replace(MARKER, "").strip()


def parse_cited_files(body: str) -> list[str]:
    marker = re.search(r"^\s*(?:\*\*)?Sources cited:(?:\*\*)?\s*$", body, re.MULTILINE)
    if not marker:
        return []
    files = []
    for line in body[marker.end():].splitlines():
        match = re.match(r"^\s*-\s+`?(wiki/[^`\s]+\.md)`?\s*$", line)
        if match:
            files.append(match.group(1))
        elif line.strip() and not line.lstrip().startswith("-"):
            break
    return sorted(set(files))


def _source_metadata(frontmatter: dict[str, str], synthesis_path: Path, raw_hash: str) -> dict:
    trigger_raw = frontmatter.get("trigger_files", "")
    triggers = [part.strip() for part in trigger_raw.split(",") if part.strip()]
    trigger_commit = frontmatter.get("commit", "")
    return {
        "synthesis_log": synthesis_path.as_posix(),
        "sha256": raw_hash,
        # `commit` is the user/trigger boundary that named the sweep. New
        # artifacts separately record the exact repository snapshot whose
        # corpus Pass 2 read. Legacy logs predate that field, so falling back
        # to the trigger commit is conservative: it can cause a harmless
        # re-sweep, never skipped post-trigger work.
        "commit_sha": trigger_commit,
        "trigger_commit_sha": trigger_commit,
        "corpus_commit_sha": frontmatter.get("corpus_commit", "") or trigger_commit,
        "diff_base": frontmatter.get("diff_base", ""),
        "trigger_files": triggers,
        "synthesizer_model": (
            # synthesize.py writes the actually served canonical model here;
            # `reviewer_model_requested` can differ when fallback is used.
            frontmatter.get("reviewer_model")
            or frontmatter.get("reviewer_model_requested")
            or ""
        ),
    }


def normalize_text(text: str, synthesis_path: Path) -> dict:
    frontmatter, body, _body_start = strip_frontmatter(text)
    raw_hash = sha256_bytes(text.encode("utf-8"))
    source = _source_metadata(frontmatter, synthesis_path, raw_hash)
    headings = find_headings(body)
    marker_positions = [m.start() for m in re.finditer(re.escape(MARKER), body)]
    explicit_no_op = bool(NO_OP_RE.search(body))

    items: list[dict] = []
    item_spans: list[tuple[int, int]] = []
    errors: list[str] = []
    warnings: list[str] = []
    recognized_headings: list[dict] = []

    for heading_index, heading in enumerate(headings):
        type_slug = heading_type(heading["title"])
        if not type_slug:
            continue
        recognized_headings.append({
            "raw": heading["title"],
            "type": type_slug,
            "style": heading["style"],
        })
        section_start = heading["end"]
        section_end = (
            headings[heading_index + 1]["start"]
            if heading_index + 1 < len(headings)
            else len(body)
        )
        section = body[section_start:section_end]

        if type_slug in NUMBERED_TYPES:
            starts = list(NUMBERED_ITEM_RE.finditer(section))
            if not starts:
                errors.append(
                    f"recognized {type_slug!r} heading {heading['title']!r} contains no numbered items"
                )
                continue
            for local_i, match in enumerate(starts):
                local_start = match.start()
                local_end = starts[local_i + 1].start() if local_i + 1 < len(starts) else len(section)
                raw_content = section[local_start:local_end]
                span = (section_start + local_start, section_start + local_end)
                item_spans.append(span)
                items.append({
                    "section_index": int(match.group(1)),
                    "type_slug": type_slug,
                    "headline": "",  # filled after document-order sort
                    "content": clean_item_content(raw_content),
                    "source_heading": heading["title"],
                    "source_span": {"start": span[0], "end": span[1]},
                })
        elif type_slug in SINGLE_TYPES:
            raw_content = section.strip()
            if not clean_item_content(raw_content):
                errors.append(
                    f"recognized {type_slug!r} heading {heading['title']!r} contains no prose"
                )
                continue
            leading = len(section) - len(section.lstrip())
            trailing = len(section.rstrip())
            span = (section_start + leading, section_start + trailing)
            item_spans.append(span)
            items.append({
                "section_index": 1,
                "type_slug": type_slug,
                "headline": "",
                "content": clean_item_content(raw_content),
                "source_heading": heading["title"],
                "source_span": {"start": span[0], "end": span[1]},
            })

    items.sort(key=lambda item: item["source_span"]["start"])
    for global_index, item in enumerate(items, 1):
        item["global_index"] = global_index
        item["headline"] = extract_headline(item["content"], item["type_slug"], global_index)

    def covered(position: int) -> bool:
        return any(start <= position < end for start, end in item_spans)

    unaccounted_markers = [position for position in marker_positions if not covered(position)]
    if unaccounted_markers:
        errors.append(
            f"{len(unaccounted_markers)} review marker(s) are outside every normalized item"
        )

    if items and not marker_positions:
        warnings.append(
            "no review markers were present; structurally normalized items were retained"
        )
    elif marker_positions and len(marker_positions) < len(items):
        warnings.append(
            f"marker count ({len(marker_positions)}) is lower than normalized item count ({len(items)}); "
            "structural items were retained"
        )
    if len(marker_positions) > len(items) and not unaccounted_markers:
        warnings.append(
            f"marker count ({len(marker_positions)}) exceeds item count ({len(items)}); "
            "duplicate in-item markers were ignored"
        )

    first_output_start = min((item["source_span"]["start"] for item in items), default=len(body))
    sources_heading = re.search(
        r"^\s*(?:\*\*)?Sources cited:(?:\*\*)?\s*$", body, re.MULTILINE
    )
    output_end = sources_heading.start() if sources_heading else len(body)
    unaccounted_numbered = [
        match.start()
        for match in NUMBERED_ITEM_RE.finditer(body)
        if first_output_start <= match.start() < output_end and not covered(match.start())
    ]
    if unaccounted_numbered:
        errors.append(
            f"{len(unaccounted_numbered)} numbered synthesis block(s) were not normalized"
        )

    if explicit_no_op:
        if items or marker_positions:
            errors.append("explicit no-op status conflicts with substantive items or review markers")
        status = "no_new_synthesis" if not errors else "normalization_failed"
    elif not items:
        errors.append(
            "zero normalized items without an explicit 'Status: No new synthesis' declaration"
        )
        status = "normalization_failed"
    else:
        status = "items" if not errors else "normalization_failed"

    required_source = [
        key for key in ("commit_sha", "corpus_commit_sha", "diff_base")
        if not source.get(key)
    ]
    if required_source:
        errors.append(f"source frontmatter missing required field(s): {', '.join(required_source)}")
        status = "normalization_failed"

    canonical_payload = {
        "schema_version": SCHEMA_VERSION,
        "status": status,
        "source_sha256": raw_hash,
        "items": items,
    }
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "status": status,
        "sweep_id": sha256_bytes(
            f"{source.get('commit_sha', '')}:{raw_hash}".encode("utf-8")
        )[:24],
        "source": source,
        "canonical_items_sha256": stable_hash(canonical_payload),
        "normalization": {
            "method": "deterministic-tolerant-v1",
            "recognized_headings": recognized_headings,
            "marker_count": len(marker_positions),
            "normalized_item_count": len(items),
            "unaccounted_marker_count": len(unaccounted_markers),
            "unaccounted_numbered_count": len(unaccounted_numbered),
            "warnings": warnings,
            "errors": errors,
        },
        "cited_files": parse_cited_files(body),
        "items": items,
    }
    return manifest


def normalize_file(synthesis_log: Path, output: Path | None = None) -> tuple[dict, Path]:
    text = synthesis_log.read_text()
    manifest = normalize_text(text, synthesis_log)
    if output is None:
        name = synthesis_log.name
        if name.startswith("v4-synthesis-"):
            name = "normalized-synthesis-" + name[len("v4-synthesis-"):]
        output = synthesis_log.with_name(Path(name).with_suffix(".json").name)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    return manifest, output


def verify_manifest(manifest_path: Path, verify_source: bool = True) -> dict:
    manifest = json.loads(manifest_path.read_text())
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise NormalizationError(
            f"unsupported manifest schema {manifest.get('schema_version')!r}; expected {SCHEMA_VERSION}"
        )
    if manifest.get("status") not in {"items", "no_new_synthesis"}:
        errors = (manifest.get("normalization") or {}).get("errors") or []
        raise NormalizationError(
            f"manifest is not reviewable (status={manifest.get('status')!r}): " + "; ".join(errors)
        )
    items = manifest.get("items")
    if not isinstance(items, list):
        raise NormalizationError("manifest items must be a list")
    if manifest["status"] == "items" and not items:
        raise NormalizationError("status='items' requires at least one item")
    if manifest["status"] == "no_new_synthesis" and items:
        raise NormalizationError("status='no_new_synthesis' requires zero items")

    canonical_payload = {
        "schema_version": manifest["schema_version"],
        "status": manifest["status"],
        "source_sha256": manifest.get("source", {}).get("sha256"),
        "items": items,
    }
    expected_canonical = stable_hash(canonical_payload)
    if manifest.get("canonical_items_sha256") != expected_canonical:
        raise NormalizationError("canonical item hash mismatch")

    if verify_source:
        source_path = Path(manifest.get("source", {}).get("synthesis_log", ""))
        if not source_path.is_file():
            raise NormalizationError(f"source synthesis log not found: {source_path}")
        source_text = source_path.read_text()
        actual_source = sha256_bytes(source_text.encode("utf-8"))
        if actual_source != manifest.get("source", {}).get("sha256"):
            raise NormalizationError("raw synthesis SHA-256 mismatch")
        # The raw hash alone does not stop someone from changing unhashed
        # manifest metadata such as diff_base, trigger paths, corpus snapshot,
        # or served model. Re-normalize the preserved raw artifact and require
        # exact semantic identity. Any future normalization behavior change
        # must therefore bump SCHEMA_VERSION and migrate intentionally.
        expected_manifest = normalize_text(source_text, source_path)
        if manifest != expected_manifest:
            raise NormalizationError(
                "manifest differs from deterministic normalization of its raw source"
            )
    return manifest


def render_for_review(manifest: dict) -> str:
    """Render canonical items in their authoritative review order."""
    if manifest["status"] == "no_new_synthesis":
        return "STATUS: NO NEW SYNTHESIS (explicitly declared by Pass 2).\n"
    parts = [
        "CANONICAL NORMALIZED SYNTHESIS ITEMS",
        f"sweep_id: {manifest['sweep_id']}",
        f"canonical_items_sha256: {manifest['canonical_items_sha256']}",
        "Review items in the exact order below.",
    ]
    for item in manifest["items"]:
        parts.extend([
            "",
            f"<<<ITEM {item['global_index']} | {item['type_slug']} | section {item['section_index']}>>>",
            item["content"],
            "<<<END ITEM>>>",
        ])
    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)

    normalize_parser = sub.add_parser("normalize")
    normalize_parser.add_argument("--synthesis-log", required=True, type=Path)
    normalize_parser.add_argument("--output", type=Path)

    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("--manifest", required=True, type=Path)
    validate_parser.add_argument("--no-source-check", action="store_true")

    count_parser = sub.add_parser("count")
    count_parser.add_argument("--manifest", required=True, type=Path)

    render_parser = sub.add_parser("render")
    render_parser.add_argument("--manifest", required=True, type=Path)

    args = parser.parse_args()
    try:
        if args.command == "normalize":
            manifest, output = normalize_file(args.synthesis_log, args.output)
            print(output)
            if manifest["status"] == "normalization_failed":
                for error in manifest["normalization"]["errors"]:
                    print(f"NORMALIZATION ERROR: {error}", file=sys.stderr)
                raise SystemExit(2)
        elif args.command == "validate":
            manifest = verify_manifest(args.manifest, verify_source=not args.no_source_check)
            print(json.dumps({
                "status": manifest["status"],
                "sweep_id": manifest["sweep_id"],
                "item_count": len(manifest["items"]),
                "source_commit": manifest["source"]["commit_sha"],
            }))
        elif args.command == "count":
            manifest = verify_manifest(args.manifest)
            print(len(manifest["items"]))
        elif args.command == "render":
            manifest = verify_manifest(args.manifest)
            sys.stdout.write(render_for_review(manifest))
    except (OSError, json.JSONDecodeError, NormalizationError) as exc:
        print(f"synthesis-normalize: {exc}", file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
