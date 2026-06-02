#!/usr/bin/env python3
"""
scripts/check-links.py — validate relative markdown links across the repo.

Catches the drift class that bit us on 2026-06-02: a file moves (e.g.
wiki/open-enzyme-vision.md → wiki/etc/open-enzyme-vision.md) and every
cross-reference to it silently rots. The wiki sweep daemon does not check
link integrity; this does.

What it checks:
  • Standard markdown links  [text](target)
  • Only RELATIVE targets (http(s)://, mailto:, tel:, #anchor-only, and
    absolute / paths are skipped).
  • A target's #fragment is stripped before the file-existence check
    (we validate the file resolves, not the anchor).
  • %20-style URL-encoding is decoded before resolving.
  • Links inside fenced code blocks (``` or ~~~) are ignored.

What it deliberately does NOT check:
  • Obsidian [[wiki-links]] — valid in Obsidian, optional per CLAUDE.md.
  • Anchor fragments — too noisy; file existence is the load-bearing part.

Usage:
  python3 scripts/check-links.py            # report broken links
  python3 scripts/check-links.py --check    # exit 1 if any broken (CI / hook)
  python3 scripts/check-links.py PATH ...   # limit to specific files/dirs

Exit codes: 0 = clean, 1 = broken links found (only nonzero with --check
or when run directly and broken links exist).
"""
from __future__ import annotations

import os
import re
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories never worth scanning:
#   • .claude        — git worktrees + skills (working copies, not corpus)
#   • venvs          — vendored Python envs under wiki/etc/experiments/<comp>/
#                      (torch et al. ship .md files)
#   • experiments    — archived per-experiment snapshots (wiki-archive.md,
#                      outputs/) that are NOT in the published nav; their
#                      links were valid at their original wiki/ location and
#                      are historical, not live.
SKIP_DIRS = {
    ".git", ".claude", "site", "node_modules", "__pycache__", ".obsidian",
    "venv", ".venv", "env", "v2-env", "site-packages", ".pytest_cache",
    "experiments",
}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
# Inline code spans (`...` / ``...``) hold illustrative examples like
# `[text](./path.md)` that must not be treated as real links.
INLINE_CODE_RE = re.compile(r"`+[^`]*`+")


def is_external(target: str) -> bool:
    t = target.strip()
    if not t:
        return True
    if t.startswith(("#",)):
        return True  # pure in-page anchor
    if t.startswith(("http://", "https://", "mailto:", "tel:", "//")):
        return True
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", t):  # any other scheme
        return True
    if t.startswith("/"):
        return True  # site-absolute; not resolvable on disk reliably
    return False


def clean_target(target: str) -> str:
    t = target.strip()
    # Markdown allows an optional title: [x](path "Title")
    if " " in t and not t.startswith("<"):
        t = t.split(" ", 1)[0]
    t = t.strip("<>")
    t = t.split("#", 1)[0]  # drop anchor
    t = t.split("?", 1)[0]  # drop query
    return unquote(t)


def iter_md_files(paths: list[str]):
    for base in paths:
        if os.path.isfile(base):
            if base.endswith(".md"):
                yield base
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if fn.endswith(".md"):
                    yield os.path.join(dirpath, fn)


def check_file(path: str) -> list[tuple[int, str]]:
    broken: list[tuple[int, str]] = []
    src_dir = os.path.dirname(path)
    in_fence = False
    with open(path, "r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            line = INLINE_CODE_RE.sub("", line)  # drop inline-code examples
            for m in LINK_RE.finditer(line):
                raw = m.group(1)
                if is_external(raw):
                    continue
                target = clean_target(raw)
                if not target:
                    continue
                resolved = os.path.normpath(os.path.join(src_dir, target))
                if not os.path.exists(resolved):
                    broken.append((lineno, raw))
    return broken


def main(argv: list[str]) -> int:
    args = [a for a in argv if a != "--check"]
    check_mode = "--check" in argv
    paths = args if args else [ROOT]

    total_broken = 0
    files_with_breaks = 0
    for md in sorted(iter_md_files(paths)):
        breaks = check_file(md)
        if breaks:
            files_with_breaks += 1
            rel = os.path.relpath(md, ROOT)
            for lineno, raw in breaks:
                print(f"{rel}:{lineno}: broken link → {raw}")
                total_broken += 1

    if total_broken:
        print(
            f"\n✗ {total_broken} broken relative link(s) in "
            f"{files_with_breaks} file(s).",
            file=sys.stderr,
        )
        return 1 if check_mode else 1
    print("✓ No broken relative links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
