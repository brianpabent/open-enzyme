#!/usr/bin/env python3
"""Reduce legacy COMP review queue files to current context and required actions."""

from __future__ import annotations

import argparse
import importlib.util
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "synthesis" / "queue"


def load_review_module():
    path = ROOT / "scripts" / "comp-review.py"
    spec = importlib.util.spec_from_file_location("comp_review_compactor", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def compact(path: Path, extractor) -> bool:
    text = path.read_text()
    comp_match = re.search(r"^comp:\s*(comp-\d+)\s*$", text, re.M)
    if not comp_match:
        raise SystemExit(f"Missing comp frontmatter: {path}")
    comp = comp_match.group(1)
    snapshot_match = re.search(r"^REVIEWED_SNAPSHOT:\s*(.+?)\s*$", text, re.M)
    snapshot = snapshot_match.group(1) if snapshot_match else "legacy independent review"
    excerpt = extractor(text)
    replacement = (
        "---\n"
        "type: comp-review\n"
        f"comp: {comp}\n"
        f"reviewed_snapshot: {snapshot}\n"
        "action_required: true\n"
        "---\n\n"
        f"# Current COMP actions: {comp}\n\n"
        f"{excerpt.rstrip()}\n\n"
        "The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.\n"
    )
    if replacement == text:
        return False
    path.write_text(replacement)
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    paths = args.paths or sorted(QUEUE.glob("comp-review-*.md"))
    module = load_review_module()
    changed = sum(
        compact(path if path.is_absolute() else ROOT / path, module.queue_action_excerpt)
        for path in paths
    )
    print(f"Compacted {changed} COMP review queue files")


if __name__ == "__main__":
    main()
