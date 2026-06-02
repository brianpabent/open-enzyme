#!/usr/bin/env python3
"""
scripts/check-privacy.py — guard the public Open Enzyme repo against leaking
references to private sibling repos or local-machine paths.

The umbrella privacy gradient is one-way: private → public, NEVER the
reverse. Open Enzyme is the only public repo in the umbrella; its content
(everything pushed to public GitHub) must not link to, or name the on-disk
path of, any private sibling (abent-family*, alma*, wraith, abent-somm,
heads-up, daep-site, gout-care) or any local-machine path.

Two detections over the published corpus:
  1. escapes-repo — a RELATIVE link target that resolves OUTSIDE the repo
     root. A public repo should never reference anything above its own tree.
     This is the name-free generic guard; it caught both leaks in the
     2026-06-02 audit on its own.
  2. private-repo / local-path — a path-shaped reference (in a link,
     inline-code span, or prose) that names a known private sibling repo or
     a local path (/Users, /private/tmp, .claude/, Claude memory files).
     Catches mentions that aren't markdown links.

Companion to check-links.py (shared discovery / skip conventions). Wired
into .githooks/pre-push.

Usage:
  python3 scripts/check-privacy.py [--check] [PATH ...]

Exit codes: 0 = clean, 1 = finding(s).
"""
from __future__ import annotations

import importlib.util
import os
import re
import sys

_spec = importlib.util.spec_from_file_location(
    "check_links",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-links.py"),
)
check_links = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_links)
ROOT = check_links.ROOT

# Private sibling repos (umbrella CLAUDE.md). Longest names first so the
# alternation prefers the most specific match. Matched only as a path
# segment (trailing slash) to avoid flagging the bare word in prose.
PRIVATE_REPOS = [
    "abent-family-health", "abent-family-finance", "abent-family",
    "alma.casa", "alma", "wraith", "abent-somm", "heads-up", "daep-site",
    "gout-care",
]
PRIVATE_RE = re.compile(
    r"(?<![\w./-])(" + "|".join(re.escape(p) for p in PRIVATE_REPOS) + r")/"
)
# Local-machine paths that should never appear in a published page.
# Note: `.claude/skills`, `.claude/agents`, `.claude/hooks` are repo-INTERNAL
# (this repo ships them) and are legitimate self-documentation — only the
# external `.claude/projects/...` memory tree is a leak.
LOCAL_RE = re.compile(
    r"(/Users/|/private/tmp/|/home/[^/\s]+/|\.claude/projects/"
    r"|Documents/Claude/Projects|(?<![\w/])memory/(?:project_|feedback_))"
)


def escapes_root(src_dir: str, target: str) -> bool:
    abspath = os.path.normpath(os.path.join(src_dir, target))
    return not (abspath == ROOT or abspath.startswith(ROOT + os.sep))


def scan_file(path: str):
    findings = []  # (lineno, kind, detail)
    src_dir = os.path.dirname(os.path.abspath(path))
    with open(path, "r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            for m in check_links.LINK_RE.finditer(line):
                raw = m.group(1)
                if check_links.is_external(raw):
                    continue
                tgt = check_links.clean_target(raw)
                if tgt and escapes_root(src_dir, tgt):
                    findings.append((lineno, "escapes-repo", raw))
            for m in PRIVATE_RE.finditer(line):
                findings.append((lineno, "private-repo", m.group(0)))
            for m in LOCAL_RE.finditer(line):
                findings.append((lineno, "local-path", m.group(0)))
    return findings


def main(argv: list[str]) -> int:
    raw_paths = [a for a in argv if not a.startswith("--")] or [ROOT]
    paths = [p if os.path.isabs(p) else os.path.join(ROOT, p) for p in raw_paths]

    total = 0
    nfiles = 0
    for md in sorted(check_links.iter_md_files(paths)):
        fs = scan_file(md)
        if not fs:
            continue
        nfiles += 1
        rel = os.path.relpath(md, ROOT)
        for lineno, kind, detail in fs:
            print(f"{rel}:{lineno}: [{kind}] {detail}")
            total += 1

    if total:
        print(
            f"\n✗ {total} privacy/leak finding(s) in {nfiles} file(s).",
            file=sys.stderr,
        )
        return 1
    print("✓ No private-sibling or local-path references in the public corpus.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
