#!/usr/bin/env python3
"""
synthesis-emit-files.py — emit per-item files from Pass 2 + Pass 3 daemon outputs.

Replaces synthesis-merge.py (which prepended to wiki/synthesis.md) per the
2026-05-08 synthesis filesystem migration spec
(operations/specs/2026-05-08-synthesis-filesystem-migration.md).

Same inputs as synthesis-merge.py:
  1. The Pass 2 synthesizer log (logs/v4-synthesis-<date>-<sha>.md)
  2. The Pass 3 reviewer output (Claude / GPT-5.5 review blockquotes,
     <<<NEXT>>>-separated, one per {{PEER-REVIEW}} marker in Pass 2)

New outputs:
  - synthesis/queue/<sweep-date>-<type>-<index>-<slug>.md, one per Pass 2 item
  - synthesis/history/<sweep-date>-<short-sha>.md, the per-sweep summary

Per-item file format (per spec §5.4):
    ---
    type: <connection|contradiction|experiment|open-question|priority-action|riskiest-assumption|most-curious-thread>
    sweep_date: <YYYY-MM-DD>
    sweep_sha: <short-sha>
    section_index: <N within section>
    global_index: <M global marker index>
    pass3_verdict: <Confirmed|Push back|Augment|Partial|Restatement|...>
    overlap_with: <slug-of-other-item>      # only when verdict tags OVERLAP / DUPLICATE
    ---

    # <Item headline>

    <Pass 2 item content with {{PEER-REVIEW}} marker stripped>

    > **Pass 3 review — <verdict>** ...
    > [Pass 3 review blockquote]

History file format (per spec §5.6):
    ---
    sweep_date: <YYYY-MM-DD>
    sweep_sha: <short-sha>
    trigger_files: [list]
    synthesizer: <model>
    reviewer: <model>
    log: <path-to-pass2-log>
    items_emitted: <N>
    items_by_type: { connection: n, ... }
    ---

    # Sweep <date> — <short-sha>

    [narrative paragraph]

    ## Items emitted

    [table: type / index / slug / verdict / queue-path]

Special signals from Pass 3 reviewer:
  - "NO_MARKERS"            — Pass 2 had no markers (drift-guard no-op).
                               Emits ONLY a history file noting the no-op.
  - "MARKER_COUNT_MISMATCH" — Pass 3 detected mismatch. Script exits non-zero.

Failure modes (fail-fast with explicit error messages, per spec §5.4):
  - Marker count mismatch between Pass 2 and Pass 3 reviews → exit 1
  - Section header recognition misses a section → exit 1
  - Headline extraction fails for >50% of items → exit 1
  - Slug collision after <index> disambiguator (should be impossible) → exit 1

Usage in CI:
    python3 scripts/synthesis-emit-files.py \\
        --synthesis-log logs/v4-synthesis-2026-05-08-e842754.md \\
        --reviews-file /tmp/claude-reviews.txt \\
        --commit-sha <full-sha> \\
        --diff-base <last-sweep-sha> \\
        --trigger-files "wiki/file1.md,wiki/file2.md" \\
        --synthesizer "google/gemini-2.5-pro" \\
        --reviewer "openai/gpt-5.5"

Local test (spec §7):
    python3 scripts/synthesis-emit-files.py \\
        --synthesis-log logs/v4-synthesis-2026-05-08-e842754.md \\
        --reviews-file /tmp/synthetic-reviews.txt \\
        --commit-sha e842754 \\
        --queue-dir /tmp/test-queue \\
        --history-dir /tmp/test-history
"""

from __future__ import annotations

import argparse
import datetime
import os
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
os.chdir(REPO_ROOT)

MARKER = "{{PEER-REVIEW}}"
SEPARATOR = "<<<NEXT>>>"

# Section header → type slug
SECTION_TYPE_MAP = {
    "New Connections": "connection",
    "Contradictions Found": "contradiction",
    "Proposed Experiments": "experiment",  # tolerates "(ranked by ...)" suffix
    "Open Questions": "open-question",
    "Priority Actions": "priority-action",
    "Riskiest Assumption": "riskiest-assumption",
    "Most Curious Thread": "most-curious-thread",
}

NUMBERED_SECTIONS = {
    "connection",
    "contradiction",
    "experiment",
    "open-question",
    "priority-action",
}

SINGLE_PARAGRAPH_SECTIONS = {
    "riskiest-assumption",
    "most-curious-thread",
}

SECTION_HEADER_RE = re.compile(
    r"^## (New Connections|Contradictions Found|Proposed Experiments(?:\s*\([^)]*\))?|Open Questions|Priority Actions|Riskiest Assumption|Most Curious Thread)\s*$",
    re.MULTILINE,
)

# Matches numbered items in two formats observed across Pass 2 model versions:
#   Old: "N. **Bolded title**..."         (Gemini 2.5 Pro pre-2026-05-16)
#   New: "### N. Sentence-cased title..." (Gemini 2.5 Pro 2026-05-16+, observed
#        under the A2 tool-use-enabled regime — format drift from the prompt)
# The captured group is the item number in either case.
NUMBERED_ITEM_RE = re.compile(r"^(?:###\s+)?(\d+)\.\s+(?:\*\*|[A-Z])", re.MULTILINE)
HEADLINE_RE = re.compile(r"\*\*([^*]+(?:\*[^*]+)*)\*\*", re.DOTALL)
# Fallback headline extractor for the H3-numbered format ("### N. Title.") —
# captures the title text up to the first period or end of line.
HEADLINE_H3_RE = re.compile(r"^###\s+\d+\.\s+(.+?)(?:\.\s*$|\s*$)", re.MULTILINE)
VERDICT_RE = re.compile(r"Pass 3 review\s*[—-]\s*([A-Za-z][A-Za-z\- ,]+?)(?:\.|`|$)")
OVERLAP_RE = re.compile(r"\[OVERLAP:\s*([A-Z]+(?:-[A-Z0-9]+)*)\]|\[DUPLICATE-OF-(\d+)\]")


def strip_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_block, body) tuple."""
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[: end + 5], text[end + 5 :]


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


def parse_pass2_sections(body: str) -> dict:
    """Split Pass 2 body into sections by section-header regex.

    Returns dict mapping type-slug → section body text.
    """
    sections = {}
    matches = list(SECTION_HEADER_RE.finditer(body))
    for i, match in enumerate(matches):
        header_text = match.group(1).strip()
        # Normalize "Proposed Experiments (ranked by ...)" → "Proposed Experiments"
        header_normalized = re.sub(r"\s*\([^)]*\)\s*$", "", header_text).strip()
        type_slug = SECTION_TYPE_MAP.get(header_normalized)
        if not type_slug:
            sys.exit(
                f"Unrecognized section header: {header_text!r}. Spec expected one of "
                f"{list(SECTION_TYPE_MAP.keys())}."
            )
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        sections[type_slug] = body[start:end].strip()
    return sections


def extract_items_from_section(section_body: str, type_slug: str) -> list[dict]:
    """Extract items from a section body. Returns list of {index, content, marker_pos}.

    For numbered sections: items begin at `^N. **` and end at the {{PEER-REVIEW}} marker
    that closes that item.
    For single-paragraph sections (riskiest-assumption / most-curious-thread): the entire
    body up to the first {{PEER-REVIEW}} marker is one item.
    """
    items = []
    truncation_drops = []
    if type_slug in NUMBERED_SECTIONS:
        # Find each numbered item start
        item_starts = list(NUMBERED_ITEM_RE.finditer(section_body))
        if not item_starts:
            return items, truncation_drops  # empty section is OK
        for i, m in enumerate(item_starts):
            index_str = m.group(1)
            start = m.start()
            end = item_starts[i + 1].start() if i + 1 < len(item_starts) else len(section_body)
            content = section_body[start:end]
            is_last_item = (i + 1 == len(item_starts))
            # Item should contain exactly one marker
            marker_count = content.count(MARKER)
            if marker_count == 0:
                # Pass 2 (Gemini) routinely truncates mid-output on this workload —
                # 3 of 5 historical logs and the 2026-05-09 dfd05a0 run all had a
                # final item cut off mid-prose with no marker emitted. Treat the
                # LAST item with no marker as truncation: drop it with a warning
                # and proceed with the items that DO have markers. A mid-section
                # missing marker (i.e. not the last item) is real corruption — fail.
                if is_last_item:
                    print(
                        f"WARNING: Item {type_slug} #{index_str} has no {MARKER} marker — "
                        f"likely Pass 2 truncation. Dropping this item and continuing.",
                        file=sys.stderr,
                    )
                    truncation_drops.append({"type_slug": type_slug, "index": int(index_str)})
                    continue
                sys.exit(
                    f"Item {type_slug} #{index_str} has no {MARKER} marker, and is not "
                    f"the last item in the section. This indicates real corruption "
                    f"(not just trailing truncation). Pass 2 prompt requires one marker per item."
                )
            if marker_count > 1:
                sys.exit(
                    f"Item {type_slug} #{index_str} has {marker_count} {MARKER} markers. "
                    f"Pass 2 prompt requires exactly one."
                )
            items.append({
                "index": int(index_str),
                "content": content.strip(),
            })
    elif type_slug in SINGLE_PARAGRAPH_SECTIONS:
        # Whole section between header and first marker is one item.
        marker_pos = section_body.find(MARKER)
        if marker_pos == -1:
            # Same truncation-tolerance reasoning as above — riskiest-assumption
            # and most-curious-thread sections come AFTER the numbered sections,
            # so a missing marker here typically means Pass 2 truncated before
            # writing it. Drop the section with a warning rather than fail-fast.
            print(
                f"WARNING: Single-paragraph section {type_slug} has no {MARKER} marker — "
                f"likely Pass 2 truncation. Dropping this section and continuing.",
                file=sys.stderr,
            )
            truncation_drops.append({"type_slug": type_slug, "index": 1})
            return items, truncation_drops
        # Include content through the marker (so the item body retains the marker
        # location for the substitution step). End-of-item is end of section body.
        items.append({
            "index": 1,
            "content": section_body.strip(),
        })
    return items, truncation_drops


def extract_headline(content: str, type_slug: str, fallback_index: int) -> str:
    """Extract headline per spec §5.4. Handles two Pass-2 formats:
      - Old: "N. **Bolded title**..."         (pre-2026-05-16)
      - New: "### N. Sentence-cased title."   (Gemini 2.5 Pro 2026-05-16+ drift
             under the A2 tool-use-enabled regime)"""
    if type_slug in NUMBERED_SECTIONS:
        # Old format first: `N. **headline**`
        m = re.search(r"^\d+\.\s+\*\*(.+?)\*\*", content, re.MULTILINE | re.DOTALL)
        if m:
            return m.group(1).strip()
        # New H3 format fallback: `### N. Title.`
        m = HEADLINE_H3_RE.search(content)
        if m:
            return m.group(1).strip()
    elif type_slug in SINGLE_PARAGRAPH_SECTIONS:
        # First sentence (up to . ! ?) of section body, with bold markers stripped
        # Strip leading whitespace + any markdown structure
        text = content.strip()
        # Strip any leading **bold** wrapper
        text = re.sub(r"^\*\*", "", text)
        # First sentence
        m = re.match(r"([^.!?\n]+[.!?])", text)
        if m:
            return re.sub(r"\*\*", "", m.group(1)).strip()
    # Fallback
    return f"unnamed-item-{fallback_index}"


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


def compute_filename(sweep_date: str, type_slug: str, section_index: int, headline: str) -> str:
    """Compute the per-item filename. Used in pass 1 (filename map) and pass 2 (write)."""
    base_slug = slugify(headline)
    # <index> is the section_index, providing collision-proof disambiguation
    return f"{sweep_date}-{type_slug}-{section_index}-{base_slug}.md"


def emit_item_file(
    queue_dir: Path,
    sweep_date: str,
    sweep_sha: str,
    type_slug: str,
    section_index: int,
    global_index: int,
    headline: str,
    body_with_marker_stripped: str,
    review_blockquote: str,
    verdict: str,
    overlap_tag: str | None,
    overlap_with_filename: str | None,
    used_slugs: set,
) -> Path:
    """Write one item file. Returns the path."""
    filename = compute_filename(sweep_date, type_slug, section_index, headline)
    path = queue_dir / filename

    if filename in used_slugs:
        sys.exit(
            f"Slug collision after disambiguation: {filename!r}. "
            f"This should be impossible by spec §5.1 design (index makes (date,type,index) unique). "
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
        f"{body_with_marker_stripped.strip()}\n"
        f"\n"
        f"{review_blockquote.strip()}\n"
    )

    path.write_text(file_content)
    return path


def emit_history_file(
    history_dir: Path,
    sweep_date: str,
    sweep_sha: str,
    trigger_files: str,
    synthesizer: str,
    reviewer: str,
    pass2_log_path: str,
    items: list[dict],
    truncation_drops: list[dict] | None = None,
) -> Path:
    """Write the per-sweep history file."""
    truncation_drops = truncation_drops or []
    by_type = Counter(item["type_slug"] for item in items)
    by_type_yaml = "\n".join(f"  {t}: {n}" for t, n in sorted(by_type.items()))

    trigger_yaml = trigger_files.replace(",", ", ")

    table_rows = []
    for item in items:
        table_rows.append(
            f"| {item['type_slug']} | {item['section_index']} | "
            f"`{item['filename']}` | {item['verdict']} | "
            f"`synthesis/queue/{item['filename']}` |"
        )
    table_body = "\n".join(table_rows)

    truncation_yaml = ""
    truncation_section = ""
    if truncation_drops:
        # YAML list of {type_slug, index} dicts. Compact inline form keeps the
        # frontmatter readable when audit trail matters.
        drop_entries = [
            f"  - {{type: {d['type_slug']}, index: {d['index']}}}"
            for d in truncation_drops
        ]
        truncation_yaml = (
            f"truncation_drops_count: {len(truncation_drops)}\n"
            f"truncation_drops:\n"
            f"{chr(10).join(drop_entries)}\n"
        )
        drop_lines = [
            f"- `{d['type_slug']}` #{d['index']}" for d in truncation_drops
        ]
        truncation_section = (
            f"\n"
            f"## Truncation drops\n"
            f"\n"
            f"Pass 2 output appears to have been cut off mid-stream by the synthesizer "
            f"({synthesizer}). The following trailing items were dropped because they had "
            f"no `{{{{PEER-REVIEW}}}}` marker:\n"
            f"\n"
            f"{chr(10).join(drop_lines)}\n"
            f"\n"
            f"This is an audit signal, not an error — the well-formed items were emitted "
            f"normally. If truncation drops persist across sweeps, investigate Pass 2's "
            f"output token budget or split the corpus.\n"
        )

    content = (
        f"---\n"
        f"sweep_date: {sweep_date}\n"
        f"sweep_sha: {sweep_sha}\n"
        f"trigger_files: \"{trigger_yaml}\"\n"
        f"synthesizer: {synthesizer}\n"
        f"reviewer: {reviewer}\n"
        f"log: {pass2_log_path}\n"
        f"items_emitted: {len(items)}\n"
        f"items_by_type:\n"
        f"{by_type_yaml}\n"
        f"{truncation_yaml}"
        f"---\n"
        f"\n"
        f"# Sweep {sweep_date} — {sweep_sha}\n"
        f"\n"
        f"Pass 2 synthesizer ({synthesizer}) emitted {len(items)} items across "
        f"{len(by_type)} section types; Pass 3 reviewer ({reviewer}) reviewed each. "
        f"Items written to `synthesis/queue/`. Trigger files: {trigger_yaml}.\n"
        f"\n"
        f"Pass 2 log: [{pass2_log_path}](../../{pass2_log_path}).\n"
        f"\n"
        f"## Items emitted\n"
        f"\n"
        f"| Type | Index | File | Verdict | Path |\n"
        f"|---|---|---|---|---|\n"
        f"{table_body}\n"
        f"{truncation_section}"
    )

    filename = f"{sweep_date}-{sweep_sha}.md"
    path = history_dir / filename
    path.write_text(content)
    return path


def emit_no_op_history(
    history_dir: Path,
    sweep_date: str,
    sweep_sha: str,
    trigger_files: str,
    synthesizer: str,
    reviewer: str,
    pass2_log_path: str,
) -> Path:
    """Write a no-op history entry when Pass 2 had no markers (drift-guard)."""
    content = (
        f"---\n"
        f"sweep_date: {sweep_date}\n"
        f"sweep_sha: {sweep_sha}\n"
        f"trigger_files: \"{trigger_files}\"\n"
        f"synthesizer: {synthesizer}\n"
        f"reviewer: {reviewer} (no review needed)\n"
        f"log: {pass2_log_path}\n"
        f"items_emitted: 0\n"
        f"no_op_reason: drift-guard (synthesizer found nothing new worth surfacing)\n"
        f"---\n"
        f"\n"
        f"# Sweep {sweep_date} — {sweep_sha} (no new synthesis)\n"
        f"\n"
        f"Pass 2 synthesizer ({synthesizer}) ran the drift-guard no-op — "
        f"trigger commit substantively duplicated prior synthesis or trivially modified "
        f"a wiki page (typo fix, link update, etc.). No items emitted to `synthesis/queue/`.\n"
        f"\n"
        f"Pass 2 log: [{pass2_log_path}](../../{pass2_log_path}).\n"
    )
    filename = f"{sweep_date}-{sweep_sha}.md"
    path = history_dir / filename
    path.write_text(content)
    return path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--synthesis-log", required=True,
                        help="Path to Pass 2 synthesizer log file")
    parser.add_argument("--reviews-file", required=True,
                        help="Path to Pass 3 reviewer output (text with <<<NEXT>>> separators, "
                             "or NO_MARKERS / MARKER_COUNT_MISMATCH)")
    parser.add_argument("--commit-sha", required=True,
                        help="Sweep commit SHA (full or short)")
    parser.add_argument("--diff-base", default="",
                        help="Last sweep commit SHA")
    parser.add_argument("--trigger-files", default="",
                        help="Comma-separated trigger files")
    parser.add_argument("--synthesizer", default="google/gemini-2.5-pro")
    parser.add_argument("--reviewer", default="openai/gpt-5.5")
    parser.add_argument("--queue-dir", default="synthesis/queue",
                        help="Directory for per-item queue files")
    parser.add_argument("--history-dir", default="synthesis/history",
                        help="Directory for per-sweep history files")
    parser.add_argument("--sweep-date", default=None,
                        help="ISO date (YYYY-MM-DD) of the trigger commit. "
                             "Per spec §5.1: workflow_run's event.head_commit timestamp date in UTC. "
                             "If unset, falls back to today's date — acceptable for local testing but "
                             "the workflow MUST pass --sweep-date for correct filenames.")
    args = parser.parse_args()

    queue_dir = Path(args.queue_dir)
    history_dir = Path(args.history_dir)
    queue_dir.mkdir(parents=True, exist_ok=True)
    history_dir.mkdir(parents=True, exist_ok=True)

    sweep_sha_short = args.commit_sha[:7]
    sweep_date = args.sweep_date or datetime.date.today().isoformat()

    # --- Read Pass 2 log -----------------------------------------------------
    pass2_path = Path(args.synthesis_log)
    if not pass2_path.exists():
        sys.exit(f"Pass 2 synthesis log not found: {pass2_path}")
    pass2_text = pass2_path.read_text()
    _fm, pass2_body = strip_frontmatter(pass2_text)

    # --- Read Pass 3 reviews -------------------------------------------------
    reviews_raw = Path(args.reviews_file).read_text().strip()

    # --- Special signals -----------------------------------------------------
    if reviews_raw == "MARKER_COUNT_MISMATCH":
        sys.exit("Pass 3 reported MARKER_COUNT_MISMATCH — Pass 2 marker count != reviews provided. Investigate.")

    if reviews_raw == "NO_MARKERS":
        path = emit_no_op_history(
            history_dir,
            sweep_date,
            sweep_sha_short,
            args.trigger_files,
            args.synthesizer,
            args.reviewer,
            args.synthesis_log,
        )
        print(f"No-op sweep recorded at {path}")
        return

    # --- Parse Pass 2 sections + items ---------------------------------------
    sections = parse_pass2_sections(pass2_body)
    if not sections:
        sys.exit("No recognized section headers in Pass 2 body. Aborting.")

    # Flatten into ordered list of items (preserving Pass 2 marker order)
    all_items = []
    all_truncation_drops = []
    global_index = 0
    headline_extraction_failures = 0
    for section_text, type_slug in [(sections.get(t), t) for t in [
        "connection", "contradiction", "experiment",
        "open-question", "priority-action",
        "riskiest-assumption", "most-curious-thread",
    ]]:
        if section_text is None:
            continue
        section_items, section_drops = extract_items_from_section(section_text, type_slug)
        all_truncation_drops.extend(section_drops)
        for item in section_items:
            global_index += 1
            headline = extract_headline(item["content"], type_slug, global_index)
            if headline.startswith("unnamed-item-"):
                headline_extraction_failures += 1
            all_items.append({
                "global_index": global_index,
                "section_index": item["index"],
                "type_slug": type_slug,
                "headline": headline,
                "content": item["content"],
            })

    if not all_items:
        sys.exit("No items parsed from Pass 2 body. Aborting.")

    if headline_extraction_failures > len(all_items) // 2:
        sys.exit(
            f"Headline extraction failed for {headline_extraction_failures}/{len(all_items)} items "
            f"(>50% threshold). Pass 2 format may have drifted. Aborting."
        )

    # --- Validate Pass 2 ↔ Pass 3 marker count ------------------------------
    pass2_marker_count = pass2_body.count(MARKER)
    if pass2_marker_count != len(all_items):
        sys.exit(
            f"Internal inconsistency: parsed {len(all_items)} items but Pass 2 has "
            f"{pass2_marker_count} {MARKER} markers. Parser is wrong. Aborting."
        )

    reviews = [r.strip() for r in reviews_raw.split(SEPARATOR) if r.strip()]
    if len(reviews) != pass2_marker_count:
        sys.exit(
            f"Marker/review count mismatch — Pass 2 has {pass2_marker_count} {MARKER} markers, "
            f"Pass 3 provided {len(reviews)} reviews. Investigate."
        )

    # --- Parse Pass 3 verdicts + build (type_slug, section_index) → filename map ---
    # Two-pass emission: pass 1 builds the filename map so DUPLICATE-OF-N markers can
    # resolve to actual filenames; pass 2 writes the files with resolved cross-links.
    parsed_reviews = [parse_verdict(r) for r in reviews]
    section_index_to_filename: dict[tuple[str, int], str] = {}
    for item in all_items:
        section_index_to_filename[(item["type_slug"], item["section_index"])] = compute_filename(
            sweep_date, item["type_slug"], item["section_index"], item["headline"]
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

        # Strip the marker from the body content
        body_content = item["content"].replace(MARKER, "").rstrip()
        path = emit_item_file(
            queue_dir,
            sweep_date,
            sweep_sha_short,
            item["type_slug"],
            item["section_index"],
            item["global_index"],
            item["headline"],
            body_content,
            review,
            verdict,
            overlap_tag,
            overlap_with_filename,
            used_slugs,
        )
        emitted_records.append({
            "type_slug": item["type_slug"],
            "section_index": item["section_index"],
            "filename": path.name,
            "verdict": verdict,
        })

    # --- Emit history file ---------------------------------------------------
    history_path = emit_history_file(
        history_dir,
        sweep_date,
        sweep_sha_short,
        args.trigger_files,
        args.synthesizer,
        args.reviewer,
        args.synthesis_log,
        emitted_records,
        all_truncation_drops,
    )

    print(f"Emitted {len(emitted_records)} items to {queue_dir}")
    print(f"History summary at {history_path}")


if __name__ == "__main__":
    main()
