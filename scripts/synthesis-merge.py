#!/usr/bin/env python3
"""
synthesis-merge.py — deterministic merge of DeepSeek V4-Pro's raw synthesis with Claude's reviews.

Pass 3 of the hybrid sweep architecture. V4-Pro produces a synthesis with
{{PEER-REVIEW}} markers at the end of each numbered item. Claude is then asked
(via scripts/sweep-prompt-3-review.md) to output ONLY the review blockquotes,
separated by <<<NEXT>>> lines. This script:

  1. Reads DeepSeek V4-Pro's synthesis log
  2. Reads Claude's review output (a flat text file or stdin)
  3. Counts {{PEER-REVIEW}} markers in DeepSeek V4-Pro's body
  4. Splits Claude's reviews by <<<NEXT>>>
  5. Verifies count match (fails fast if not)
  6. Substitutes each marker with the corresponding review blockquote
  7. Prepends the merged block to wiki/synthesis.md

DeepSeek V4-Pro's content is preserved verbatim — Claude only generates the review text,
never produces DeepSeek V4-Pro's content as output. The substitution is mechanical.

Special signals from Claude:
  - "NO_MARKERS"            — DeepSeek V4-Pro had no markers (drift-guard no-op). Prepends a notice.
  - "MARKER_COUNT_MISMATCH" — Claude detected mismatch. Script exits non-zero.

Usage in CI:
    python3 scripts/synthesis-merge.py \\
        --synthesis-log logs/v4-synthesis-2026-04-25-abc1234.md \\
        --reviews-file /tmp/claude-reviews.txt \\
        --commit-sha <full-sha> \\
        --diff-base <last-sweep-sha> \\
        --trigger-files "wiki/file1.md,wiki/file2.md" \\
        --synthesizer "deepseek/deepseek-v4-pro" \\
        --reviewer "anthropic/claude-sonnet-4-6"
"""

import os
import sys
import argparse
import datetime
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

MARKER = "{{PEER-REVIEW}}"
SEPARATOR = "<<<NEXT>>>"


def strip_frontmatter(text):
    """Return (frontmatter_dict_text, body) tuple. Frontmatter is the leading
    YAML block between --- delimiters; body is everything after."""
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    frontmatter = text[:end + 5]
    body = text[end + 5:]
    return frontmatter, body


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--synthesis-log", required=True,
                        help="Path to DeepSeek V4-Pro's raw synthesis log file")
    parser.add_argument("--reviews-file", required=True,
                        help="Path to Claude's reviews (text with <<<NEXT>>> separators, or NO_MARKERS / MARKER_COUNT_MISMATCH)")
    parser.add_argument("--commit-sha", required=True,
                        help="Sweep commit SHA (short or full)")
    parser.add_argument("--diff-base", default="",
                        help="Last sweep commit SHA")
    parser.add_argument("--trigger-files", default="",
                        help="Comma-separated trigger files")
    parser.add_argument("--synthesizer", default="deepseek/deepseek-v4-pro")
    parser.add_argument("--reviewer", default="anthropic/claude-sonnet-4-6")
    parser.add_argument("--synthesis-md", default="wiki/synthesis.md",
                        help="Path to synthesis.md to prepend into")
    args = parser.parse_args()

    # --- Read DeepSeek V4-Pro log ---------------------------------------------------------
    if not os.path.exists(args.synthesis_log):
        sys.exit(f"DeepSeek V4-Pro synthesis log not found: {args.synthesis_log}")
    with open(args.synthesis_log) as f:
        v4_text = f.read()
    _v4_frontmatter, v4_body = strip_frontmatter(v4_text)

    # --- Read Claude reviews -------------------------------------------------
    with open(args.reviews_file) as f:
        reviews_raw = f.read().strip()

    sha_short = args.commit_sha[:7]
    date_str = datetime.date.today().isoformat()

    # --- Handle special signals ---------------------------------------------
    if reviews_raw == "MARKER_COUNT_MISMATCH":
        sys.exit("Claude reported MARKER_COUNT_MISMATCH — DeepSeek V4-Pro marker count != reviews provided. Investigate.")

    if reviews_raw == "NO_MARKERS":
        # DeepSeek V4-Pro produced a drift-guard no-op. Prepend a short notice.
        merged_section = (
            f"## Sweep — {date_str} (no new synthesis)\n\n"
            f"**Synthesis log:** [`{args.synthesis_log}`](../{args.synthesis_log})\n"
            f"**Substrate:** Open Enzyme wiki at commit `{sha_short}`\n"
            f"**Synthesizer:** {args.synthesizer} (drift-guard: nothing new worth synthesizing)\n"
            f"**Reviewer:** {args.reviewer} (no review needed)\n\n"
            f"---\n\n"
        )
        prepend_to_synthesis(args.synthesis_md, merged_section)
        print("No-op sweep prepended to synthesis.md")
        return

    # --- Normal flow: count markers, split reviews, validate, substitute -----
    marker_count = v4_body.count(MARKER)
    if marker_count == 0:
        sys.exit(f"DeepSeek V4-Pro body has no {MARKER} markers but reviews file is non-special. Aborting.")

    # Split reviews; filter out trailing empties from a final separator
    reviews = [r.strip() for r in reviews_raw.split(SEPARATOR)]
    reviews = [r for r in reviews if r]  # drop empties

    if len(reviews) != marker_count:
        sys.exit(
            f"Marker/review count mismatch — DeepSeek V4-Pro has {marker_count} {MARKER} markers, "
            f"Claude provided {len(reviews)} reviews. Investigate the Pass 3 prompt or model output."
        )

    # Substitute markers in order
    merged_body = v4_body
    for review in reviews:
        # Each review is a blockquote (or multiline blockquote). Replace
        # exactly one marker per iteration to preserve order.
        merged_body = merged_body.replace(MARKER, review, 1)

    # Sanity: no markers should remain
    if MARKER in merged_body:
        sys.exit(f"After substitution, {MARKER} still present. Substitution went wrong.")

    # --- Strip DeepSeek V4-Pro's H1 title from the body (we wrap in our own H2) -----------
    # DeepSeek V4-Pro's body typically opens with "# Synthesis — <date>". Strip that line
    # so the prepend doesn't have an H1 inside an H2 section.
    merged_body = re.sub(r"^\s*#\s+Synthesis\s*[—-].*?\n", "", merged_body, count=1)

    # --- Build the prepend section -------------------------------------------
    merged_section = (
        f"## Sweep — {date_str} (DeepSeek V4-Pro synthesis + Claude review)\n\n"
        f"**Synthesis log:** [`{args.synthesis_log}`](../{args.synthesis_log})\n"
        f"**Substrate:** Open Enzyme wiki at commit `{sha_short}`\n"
        f"**Diff base:** `{args.diff_base}`\n"
        f"**Trigger files:** {args.trigger_files or '(none specified)'}\n"
        f"**Synthesizer:** {args.synthesizer}\n"
        f"**Reviewer:** {args.reviewer}\n"
        f"**Reviews merged:** {marker_count}\n\n"
        f"---\n"
        f"{merged_body.lstrip()}\n"
        f"---\n\n"
    )

    prepend_to_synthesis(args.synthesis_md, merged_section)
    print(f"Merged sweep prepended to {args.synthesis_md} ({marker_count} reviews substituted)")


def prepend_to_synthesis(path, new_section):
    """Insert new_section right after the existing H1 title (`# Synthesis ...`)."""
    with open(path) as f:
        existing = f.read()

    # Find the H1 title line and prepend after it
    h1_pattern = re.compile(r"^(# Synthesis Pass 2:.*?\n)", re.MULTILINE)
    match = h1_pattern.search(existing)
    if not match:
        # No H1 found — just prepend at the very top after frontmatter
        frontmatter, body = strip_frontmatter(existing)
        new_content = frontmatter + "\n" + new_section + body
    else:
        idx = match.end()
        new_content = existing[:idx] + "\n" + new_section + existing[idx:].lstrip()

    with open(path, "w") as f:
        f.write(new_content)


if __name__ == "__main__":
    main()
