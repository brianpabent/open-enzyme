#!/usr/bin/env python3
"""Emit reviewed full-synthesis findings into the active action queue.

Raw synthesis and review inputs are short-retention recovery artifacts. Git and
the compact coverage receipt are the run history; successful narratives are not
copied into the live tree.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

from synthesis_normalize import NormalizationError, verify_manifest

REPO_ROOT = Path(__file__).resolve().parent.parent
os.chdir(REPO_ROOT)

SEPARATOR = "<<<NEXT>>>"

VERDICT_RE = re.compile(r"Pass 3 review\s*[—-]\s*([A-Za-z][A-Za-z\- ,]+?)(?:\.|`|$)")
OVERLAP_RE = re.compile(r"\[OVERLAP:\s*([A-Z]+(?:-[A-Z0-9]+)*)\]|\[DUPLICATE-OF-(\d+)\]")


def slugify(headline: str, max_len: int = 60) -> str:
    """ASCII kebab-case slug per spec §5.1."""
    if not headline:
        return "unnamed"
    s = headline.lower()
    # Strip non-ASCII
    s = s.encode("ascii", "ignore").decode("ascii")
    # Replace runs of non-alphanumeric with single hyphen
    s = re.sub(r"[^a-z0-9]+", "-", s)
    # Strip leading/trailing hyphens
    s = s.strip("-")
    if not s:
        return "unnamed"
    # Truncate at word boundary if over max_len
    if len(s) > max_len:
        truncated = s[:max_len]
        last_hyphen = truncated.rfind("-")
        if last_hyphen > max_len // 2:  # only break at hyphen if reasonable
            truncated = truncated[:last_hyphen]
        s = truncated.rstrip("-")
    return s or "unnamed"




def parse_verdict(review_text: str) -> tuple[str, str | None, int | None]:
    """Extract (verdict, overlap_tag, duplicate_of_index) from a Pass 3 review blockquote.

    Per spec §5.2, the OVERLAP tag and DUPLICATE-OF-N marker are distinct things:
      - [OVERLAP: NOVEL|EXTENSION|RESTATEMENT] — the reviewer's classification of how
        much of this finding is already in the wiki. Belongs in `overlap_tag` frontmatter.
      - [DUPLICATE-OF-N] — the reviewer asserts this item is a near-duplicate of another
        item by section_index N within this same sweep. The frontmatter `overlap_with`
        gets resolved to the other item's emitted filename in a second pass over all items.

    The pre-2026-05-08 implementation conflated these into a single `overlap_with` string
    which was either the OVERLAP type ("NOVEL", etc.) — meaningless as a slug — or a bare
    "item-N" placeholder rather than a real cross-link. Now they're separate fields.
    """
    m = VERDICT_RE.search(review_text)
    verdict = m.group(1).strip() if m else "unknown"
    overlap_match = OVERLAP_RE.search(review_text)
    overlap_tag = None
    duplicate_of_index = None
    if overlap_match:
        if overlap_match.group(1) is not None:
            overlap_tag = overlap_match.group(1)
        elif overlap_match.group(2) is not None:
            duplicate_of_index = int(overlap_match.group(2))
    return verdict, overlap_tag, duplicate_of_index


def compute_filename(
    sweep_date: str,
    artifact_id: str,
    type_slug: str,
    section_index: int,
    headline: str,
) -> str:
    """Compute a filename unique to this normalized synthesis artifact."""
    base_slug = slugify(headline)
    return f"{sweep_date}-{artifact_id}-{type_slug}-{section_index}-{base_slug}.md"


def emit_item_file(
    queue_dir: Path,
    sweep_date: str,
    sweep_sha: str,
    type_slug: str,
    section_index: int,
    global_index: int,
    headline: str,
    canonical_body: str,
    review_blockquote: str,
    verdict: str,
    overlap_tag: str | None,
    overlap_with_filename: str | None,
    used_slugs: set,
    manifest_meta: dict | None = None,
) -> Path:
    """Write one item file. Returns the path."""
    if not manifest_meta or not manifest_meta.get("sweep_id"):
        sys.exit("Cannot emit queue item without a hash-derived sweep_id")
    artifact_id = manifest_meta["sweep_id"][:8]
    filename = compute_filename(
        sweep_date, artifact_id, type_slug, section_index, headline
    )
    path = queue_dir / filename

    if filename in used_slugs:
        sys.exit(
            f"Slug collision after disambiguation: {filename!r}. "
            f"This should be impossible (artifact hash + type + index are unique). "
            f"Aborting."
        )
    used_slugs.add(filename)

    frontmatter_lines = [
        "---",
        f"type: {type_slug}",
        f"sweep_date: {sweep_date}",
        f"sweep_sha: {sweep_sha}",
        f"section_index: {section_index}",
        f"global_index: {global_index}",
        f"pass3_verdict: {verdict}",
    ]
    if manifest_meta:
        frontmatter_lines.extend([
            f"sweep_id: {manifest_meta['sweep_id']}",
            f"source_synthesis_sha256: {manifest_meta['source_sha256']}",
            f"canonical_items_sha256: {manifest_meta['canonical_items_sha256']}",
        ])
    if overlap_tag:
        # Reviewer's [OVERLAP: NOVEL|EXTENSION|RESTATEMENT] classification —
        # how much of this finding is already in the wiki.
        frontmatter_lines.append(f"overlap_tag: {overlap_tag}")
    if overlap_with_filename:
        # Resolved cross-link to another emitted item in this same sweep
        # (from a [DUPLICATE-OF-N] marker, where N is the other item's section_index).
        frontmatter_lines.append(f"overlap_with: {overlap_with_filename}")
    frontmatter_lines.append("---")
    frontmatter = "\n".join(frontmatter_lines)

    file_content = (
        f"{frontmatter}\n"
        f"\n"
        f"# {headline}\n"
        f"\n"
        f"{canonical_body.strip()}\n"
        f"\n"
        f"{review_blockquote.strip()}\n"
    )

    path.write_text(file_content)
    return path



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--synthesis-log", required=True,
                        help="Path to Pass 2 synthesizer log file")
    parser.add_argument("--normalized-manifest", required=True,
                        help=("Canonical JSON emitted by synthesis_normalize.py. "
                              "This, not free-form Markdown, is the downstream wire contract."))
    parser.add_argument("--count-items", action="store_true",
                        help="Validate the manifest, print its canonical item count, "
                             "and exit. The workflow uses this to tell Pass 3 how "
                             "many items to review.")
    parser.add_argument("--reviews-file", default=None,
                        help="Path to Pass 3 reviewer output (text with <<<NEXT>>> separators, "
                             "or EXPLICIT_NO_OP). Required in emit mode.")
    parser.add_argument("--commit-sha", default="",
                        help="Sweep commit SHA (full or short). Required in emit mode.")
    parser.add_argument("--diff-base", default="",
                        help="Last sweep commit SHA")
    parser.add_argument("--trigger-files", default="",
                        help="Comma-separated trigger files")
    parser.add_argument("--synthesizer", default="google/gemini-2.5-pro")
    parser.add_argument("--reviewer", default="openai/gpt-5.5")
    parser.add_argument("--queue-dir", default="synthesis/queue",
                        help="Directory for per-item queue files")
    parser.add_argument("--sweep-date", default=None,
                        help="ISO date (YYYY-MM-DD) of the trigger commit. "
                             "Per spec §5.1: workflow_run's event.head_commit timestamp date in UTC. "
                             "If unset, falls back to today's date — acceptable for local testing but "
                             "the workflow MUST pass --sweep-date for correct filenames.")
    args = parser.parse_args()

    queue_dir = Path(args.queue_dir)
    queue_dir.mkdir(parents=True, exist_ok=True)

    sweep_sha_short = args.commit_sha[:7]
    sweep_date = args.sweep_date or datetime.date.today().isoformat()

    # --- Verify canonical manifest + raw-artifact binding -------------------
    pass2_path = Path(args.synthesis_log)
    if not pass2_path.exists():
        sys.exit(f"Pass 2 synthesis log not found: {pass2_path}")
    manifest_path = Path(args.normalized_manifest)
    try:
        manifest = verify_manifest(manifest_path)
    except (OSError, json.JSONDecodeError, NormalizationError) as exc:
        sys.exit(f"Normalized synthesis manifest failed validation: {exc}")
    if Path(manifest["source"]["synthesis_log"]) != pass2_path:
        sys.exit(
            "Normalized manifest source path does not match --synthesis-log: "
            f"{manifest['source']['synthesis_log']!r} != {str(pass2_path)!r}"
        )
    manifest_meta = {
        "sweep_id": manifest["sweep_id"],
        "source_sha256": manifest["source"]["sha256"],
        "canonical_items_sha256": manifest["canonical_items_sha256"],
    }

    # --- Count-items mode: print canonical item count and exit ----------------
    if args.count_items:
        print(len(manifest["items"]))
        return

    # Emit mode needs the Pass 3 reviews + a commit SHA.
    if not args.reviews_file:
        sys.exit("--reviews-file is required in emit mode (omit it only with --count-items).")
    if not args.commit_sha:
        sys.exit("--commit-sha is required in emit mode.")

    # --- Read Pass 3 reviews -------------------------------------------------
    reviews_raw = Path(args.reviews_file).read_text().strip()

    # --- Special signals -----------------------------------------------------
    if manifest["status"] == "no_new_synthesis":
        if reviews_raw != "EXPLICIT_NO_OP":
            sys.exit(
                "Normalized manifest is an explicit no-op, but reviews file did not contain "
                "the EXPLICIT_NO_OP sentinel. Aborting."
            )
        print("Explicit no-op verified; no live artifact retained")
        return

    if reviews_raw == "EXPLICIT_NO_OP":
        sys.exit("EXPLICIT_NO_OP is invalid for a manifest containing synthesis items.")

    # --- Consume canonical items; raw Markdown is audit evidence only --------
    all_items = manifest["items"]
    headline_extraction_failures = sum(
        1 for item in all_items if item.get("headline", "").startswith("unnamed-item-")
    )
    if not all_items:
        sys.exit("No items parsed from Pass 2 body. Aborting.")

    if headline_extraction_failures > len(all_items) // 2:
        sys.exit(
            f"Headline extraction failed for {headline_extraction_failures}/{len(all_items)} items "
            f"(>50% threshold). Pass 2 format may have drifted. Aborting."
        )

    # --- Validate Pass 3 review count against canonical item count ------------
    # Pass 3 emits exactly one <<<NEXT>>>-separated review per manifest item,
    # in canonical document order.
    # Strip any leading preamble before each review's first blockquote. Some
    # Pass 3 models (notably DeepSeek when it self-terminates before the
    # iteration cap) leak a preamble line ("Now I have enough...") before the
    # first "> **... review —" blockquote despite the prompt's output-only
    # instruction; that corrupts the positional merge. Defensive + model-agnostic:
    # for each <<<NEXT>>>-separated segment, drop leading non-blockquote lines.
    def _strip_review_preamble(seg: str) -> str:
        lines = seg.split("\n")
        for i, ln in enumerate(lines):
            if ln.lstrip().startswith(">"):
                return "\n".join(lines[i:]).strip()
        return seg.strip()  # no blockquote found — leave intact; count check catches it

    reviews = [_strip_review_preamble(r) for r in reviews_raw.split(SEPARATOR) if r.strip()]
    if len(reviews) != len(all_items):
        sys.exit(
            f"Review/item count mismatch — Pass 2 has {len(all_items)} items, "
            f"Pass 3 provided {len(reviews)} reviews. Pass 3 must emit one review "
            f"per item, in document order."
        )

    # --- Parse Pass 3 verdicts + build (type_slug, section_index) → filename map ---
    # Two-pass emission: pass 1 builds the filename map so DUPLICATE-OF-N markers can
    # resolve to actual filenames; pass 2 writes the files with resolved cross-links.
    parsed_reviews = [parse_verdict(r) for r in reviews]
    artifact_id = manifest["sweep_id"][:8]
    section_index_to_filename: dict[tuple[str, int], str] = {}
    for item in all_items:
        section_index_to_filename[(item["type_slug"], item["section_index"])] = compute_filename(
            sweep_date,
            artifact_id,
            item["type_slug"],
            item["section_index"],
            item["headline"],
        )

    # --- Emit per-item files -------------------------------------------------
    used_slugs = set()
    emitted_records = []
    for item, review, (verdict, overlap_tag, duplicate_of_index) in zip(
        all_items, reviews, parsed_reviews
    ):
        # Resolve [DUPLICATE-OF-N] to an emitted filename. N is a section_index, but the
        # marker doesn't say which type's section_index — best effort: prefer the same
        # type as the current item, then fall back to any type with that index. If we
        # can't resolve, leave overlap_with unset rather than emitting a broken pointer.
        overlap_with_filename: str | None = None
        if duplicate_of_index is not None:
            same_type = section_index_to_filename.get((item["type_slug"], duplicate_of_index))
            if same_type:
                overlap_with_filename = same_type
            else:
                for (t, idx), fn in section_index_to_filename.items():
                    if idx == duplicate_of_index and (t, idx) != (item["type_slug"], item["section_index"]):
                        overlap_with_filename = fn
                        break

        path = emit_item_file(
            queue_dir,
            sweep_date,
            sweep_sha_short,
            item["type_slug"],
            item["section_index"],
            item["global_index"],
            item["headline"],
            item["content"],
            review,
            verdict,
            overlap_tag,
            overlap_with_filename,
            used_slugs,
            manifest_meta,
        )
        emitted_records.append({
            "type_slug": item["type_slug"],
            "section_index": item["section_index"],
            "filename": path.name,
            "verdict": verdict,
        })

    print(f"Emitted {len(emitted_records)} items to {queue_dir}")


if __name__ == "__main__":
    main()
