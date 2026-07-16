#!/usr/bin/env python3
"""Enforce current-state and token-efficiency rules on reader-facing content."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATHS = [ROOT / "README.md", ROOT / "index.md", ROOT / "CLAUDE.md", ROOT / "wiki"]
ALLOWLIST = ROOT / "scripts" / "corpus-duplicate-allowlist.json"
MIN_PARAGRAPH_CHARS = 500
MISSION_SURFACES = {
    "README.md", "index.md", "CLAUDE.md", "wiki/index.md",
    "wiki/etc/open-enzyme-vision.md", "wiki/cross-validation.md",
}
FORBIDDEN_MISSION_PATTERNS = {
    "fabricated sourdough claim": re.compile(r"as easy as sourdough|grow it at home like sourdough", re.I),
    "project-level feasibility score": re.compile(r"(?:platform|project)\s+(?:feasibility\s+)?(?:score|rating)\s*[:=]?\s*\d+(?:\.\d+)?\s*/\s*10", re.I),
    "Koji-first mission framing": re.compile(r"koji[- ]first|koji[- ]primary|highest-priority chassis", re.I),
    "Koji as primary platform": re.compile(r"primary (?:host|platform|chassis).{0,60}koji|koji.{0,60}primary (?:host|platform|chassis)", re.I),
}
RETIRED_REF = re.compile(
    r"synthesis/(?:done|history|strategic-reflections)/|logs/(?:comp-reviews|v4-synthesis-|normalized-synthesis-)"
)
REVISION_HEADING = re.compile(r"^#{1,6}\s+(?:document\s+|revision\s+|update\s+)?(?:change\s*log|changelog|revision history)\s*$", re.I | re.M)
ADVERSARIAL_HEADING = re.compile(r"^#{1,6}\s+.*(?:myth|strawman|objection|as easy as).*$", re.I | re.M)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def markdown_files(paths: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            files.add(path.resolve())
        elif path.is_dir():
            files.update(p.resolve() for p in path.rglob("*.md"))
    return sorted(files)


def normalized_paragraphs(path: Path) -> list[tuple[int, str]]:
    text = path.read_text(errors="replace")
    results = []
    offset = 0
    for block in re.split(r"\n\s*\n", text):
        line = text[:offset].count("\n") + 1
        offset += len(block) + 2
        normalized = re.sub(r"\s+", " ", block).strip()
        if len(normalized) >= MIN_PARAGRAPH_CHARS and not normalized.startswith("|"):
            results.append((line, normalized))
    return results


def load_allowlist() -> set[str]:
    if not ALLOWLIST.exists():
        return set()
    return set(json.loads(ALLOWLIST.read_text()).get("allowed_sha256", []))


def check_content(files: list[Path]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    reports: list[str] = []
    allowlist = load_allowlist()
    paragraphs: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    similarity_buckets: dict[str, list[tuple[str, int, str]]] = defaultdict(list)

    for path in files:
        name = rel(path)
        text = path.read_text(errors="replace")
        if name in MISSION_SURFACES:
            for label, pattern in FORBIDDEN_MISSION_PATTERNS.items():
                for match in pattern.finditer(text):
                    line = text[:match.start()].count("\n") + 1
                    errors.append(f"{name}:{line}: {label}: {match.group(0)!r}")
        if name in MISSION_SURFACES or name.startswith("wiki/"):
            for match in RETIRED_REF.finditer(text):
                line = text[:match.start()].count("\n") + 1
                errors.append(f"{name}:{line}: retired live-artifact reference: {match.group(0)}")
            for match in REVISION_HEADING.finditer(text):
                line = text[:match.start()].count("\n") + 1
                errors.append(f"{name}:{line}: Git is history; remove {match.group(0).strip()!r}")
            for match in ADVERSARIAL_HEADING.finditer(text):
                following = text[match.end():match.end() + 1400]
                if not re.search(r"(?:claim source|project claim)\s*:|\[[^]]+\]\([^)]+\)", following, re.I):
                    line = text[:match.start()].count("\n") + 1
                    errors.append(f"{name}:{line}: adversarial section lacks a real-claim source anchor")

        if name.startswith("wiki/etc/experiments/"):
            continue
        for line, paragraph in normalized_paragraphs(path):
            digest = hashlib.sha256(paragraph.encode()).hexdigest()
            paragraphs[digest].append((name, line, paragraph))
            similarity_buckets[re.sub(r"\W+", " ", paragraph.lower())[:80]].append((name, line, paragraph))

    for digest, occurrences in paragraphs.items():
        locations = {(name, line) for name, line, _ in occurrences}
        if len(locations) > 1 and digest not in allowlist:
            where = ", ".join(f"{name}:{line}" for name, line in sorted(locations))
            errors.append(f"exact duplicate paragraph {digest[:12]} ({len(occurrences[0][2])} chars): {where}")

    seen: set[tuple[str, int, str, int]] = set()
    for bucket in similarity_buckets.values():
        if len(bucket) < 2 or len(bucket) > 12:
            continue
        for i, left in enumerate(bucket):
            for right in bucket[i + 1:]:
                key = (left[0], left[1], right[0], right[1])
                if key in seen or left[2] == right[2]:
                    continue
                seen.add(key)
                ratio = difflib.SequenceMatcher(None, left[2], right[2], autojunk=False).ratio()
                if ratio >= 0.92:
                    reports.append(f"similarity {ratio:.1%}: {left[0]}:{left[1]} ↔ {right[0]}:{right[1]}")
    return errors, reports[:25]


def token_delta(base: str, files: list[Path]) -> list[str]:
    tracked = {rel(path): path for path in files}
    result = subprocess.run(
        ["git", "diff", "--name-only", base, "--", "*.md"], cwd=ROOT,
        text=True, capture_output=True, check=False,
    )
    rows = []
    for name in result.stdout.splitlines():
        path = tracked.get(name)
        if not path or not path.exists():
            continue
        current = len(path.read_text(errors="replace")) // 4
        prior = subprocess.run(
            ["git", "show", f"{base}:{name}"], cwd=ROOT, text=True,
            capture_output=True, check=False,
        )
        previous = len(prior.stdout) // 4 if prior.returncode == 0 else 0
        rows.append((abs(current - previous), current - previous, current, name))
    return [f"{name}: {delta:+,} estimated tokens ({current:,} current)" for _, delta, current, name in sorted(rows, reverse=True)[:12]]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--base", default="HEAD^", help="Git base for token-delta reporting")
    args = parser.parse_args()
    paths = [(ROOT / path).resolve() if not path.is_absolute() else path for path in args.paths] or DEFAULT_PATHS
    files = markdown_files(paths)
    errors, reports = check_content(files)
    for row in token_delta(args.base, files):
        print(f"TOKEN_DELTA {row}")
    for report in reports:
        print(f"REPORT {report}")
    if errors:
        print("\n".join(f"ERROR {error}" for error in errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"Corpus hygiene passed for {len(files)} Markdown files")


if __name__ == "__main__":
    main()
