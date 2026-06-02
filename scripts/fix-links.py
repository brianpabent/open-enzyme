#!/usr/bin/env python3
"""
scripts/fix-links.py — repair broken relative markdown links.

Companion to check-links.py. Only ever touches links that check-links.py
reports as BROKEN, and only rewrites a link when a candidate path actually
resolves to a real file on disk — so it cannot invent or mis-aim a working
link into a broken one. Anything it can't resolve is reported as UNFIXABLE
for manual handling (semantic moves it can't infer).

Most repo link-rot comes from a directory-level shift (e.g. the wiki/ →
wiki/etc/ reorg moved pages one level deeper, breaking every relative link
by one ../). The candidate generator handles that generically; genuine
renames go in EXPLICIT_RENAMES.

Usage:
  python3 scripts/fix-links.py            # dry-run: print proposed changes
  python3 scripts/fix-links.py --write    # apply changes
  python3 scripts/fix-links.py --write PATH ...   # limit scope

Then run check-links.py --check to confirm convergence to zero.
"""
from __future__ import annotations

import os
import sys
from urllib.parse import unquote

import importlib.util

_spec = importlib.util.spec_from_file_location(
    "check_links", os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-links.py")
)
check_links = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_links)

ROOT = check_links.ROOT

# Basename → repo-relative destination for genuine moves/renames the
# level-shift heuristic can't infer.
EXPLICIT_RENAMES = {
    "ward-1995-lab-access-global.md": "operations/ward-1995-lab-access.md",
    "ward-1995-lab-access.md": "operations/ward-1995-lab-access.md",
    "07-nlrp3-inhibitor-screen.md": "wiki/nlrp3-inhibitor-screen.md",
}

# Basenames whose link should be UNWRAPPED to plain text (target is not a
# repo file at all — e.g. a local Claude-memory path that leaked in).
UNLINK_BASENAMES = {
    "project_feua_at_ua_retest.md",
    "feedback_dont_treat_single_failed_fetch_as_durable_gate.md",
}


def candidates(target: str):
    """Yield candidate replacement targets, cleanest repairs first. Only a
    candidate that resolves to a real file is ever applied, so ordering only
    affects which *valid* form wins (prefer the tidiest)."""
    # self-reference after a page moved into etc/ (./etc/x → ./x)
    if "./etc/" in target:
        yield target.replace("./etc/", "./")
    if "/etc/" in target:
        yield target.replace("/etc/", "/")
    # explicit-relative subdir that went up a level (./sub/x → ../sub/x)
    if target.startswith("./"):
        yield "../" + target[2:]
    # bare sibling went up a level (x → ../x); also ../x → ../../x
    yield "../" + target
    # a spurious extra ../ left behind (../sub/x → sub/x)
    if target.startswith("../"):
        yield target[3:]
    # insert etc/ before the basename (refs from outside wiki/ to a page that
    # moved wiki/X → wiki/etc/X — e.g. CLAUDE.md's wiki/team.md)
    d, base = os.path.split(target)
    yield os.path.join(d, "etc", base) if d else os.path.join("etc", base)
    yield "../../" + target.lstrip("./")


def split_frag(raw: str):
    """Split a raw link target into (path, suffix) where suffix is the
    #anchor or ?query that must be preserved across a rewrite."""
    for sep in ("#", "?"):
        if sep in raw:
            i = raw.index(sep)
            return raw[:i], raw[i:]
    return raw, ""


def resolve(src_dir: str, target: str) -> bool:
    """A candidate is acceptable only if it exists AND stays within the repo.
    Links that escape ROOT (private sibling repos, local .claude/ memory
    paths) must never be auto-resolved on a public repo — they're reported
    UNFIXABLE for human review instead."""
    abspath = os.path.normpath(os.path.join(src_dir, target))
    if not (abspath == ROOT or abspath.startswith(ROOT + os.sep)):
        return False
    return os.path.exists(abspath)


def relpath_to(src_dir: str, repo_dest: str) -> str:
    dest_abs = os.path.join(ROOT, repo_dest)
    rel = os.path.relpath(dest_abs, src_dir)
    return rel


def plan_file(path: str):
    """Return (replacements, unwraps, unfixable) for one file."""
    src_dir = os.path.dirname(path)
    breaks = check_links.check_file(path)
    replacements = {}   # raw_target -> new_target
    unwraps = set()     # raw_targets to unlink
    unfixable = []      # (lineno, raw_target)
    for lineno, raw in breaks:
        path_part, frag = split_frag(raw)
        target = check_links.clean_target(raw)  # path only, decoded
        base = os.path.basename(target)
        if base in UNLINK_BASENAMES:
            unwraps.add(raw)
            continue
        if base in EXPLICIT_RENAMES:
            new_rel = relpath_to(src_dir, EXPLICIT_RENAMES[base])
            replacements[raw] = new_rel + frag
            continue
        fixed = None
        for cand in candidates(target):
            if resolve(src_dir, cand):
                fixed = cand
                break
        if fixed:
            replacements[raw] = fixed + frag
        else:
            unfixable.append((lineno, raw))
    return replacements, unwraps, unfixable


def apply_file(path: str, replacements: dict, unwraps: set) -> bool:
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    orig = text
    for raw, new in replacements.items():
        text = text.replace(f"]({raw})", f"]({new})")
    for raw in unwraps:
        # [label](raw) -> label  (drop the link, keep visible text)
        import re
        text = re.sub(
            r"\[([^\]]*)\]\(" + re.escape(raw) + r"\)", r"\1", text
        )
    if text != orig:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return True
    return False


def main(argv: list[str]) -> int:
    write = "--write" in argv
    raw_paths = [a for a in argv if not a.startswith("--")] or [ROOT]
    # absolutize so os.walk yields absolute paths → the within-ROOT guard
    # in resolve() compares like with like regardless of CWD
    paths = [p if os.path.isabs(p) else os.path.join(ROOT, p) for p in raw_paths]

    total_fix = total_unwrap = total_unfix = 0
    for md in sorted(check_links.iter_md_files(paths)):
        replacements, unwraps, unfixable = plan_file(md)
        if not (replacements or unwraps or unfixable):
            continue
        rel = os.path.relpath(md, ROOT)
        for raw, new in replacements.items():
            print(f"{'FIX ' if write else 'plan'} {rel}: {raw}  →  {new}")
            total_fix += 1
        for raw in unwraps:
            print(f"{'UNLINK' if write else 'plan-unlink'} {rel}: {raw}")
            total_unwrap += 1
        for lineno, raw in unfixable:
            print(f"UNFIXABLE {rel}:{lineno}: {raw}  (handle manually)")
            total_unfix += 1
        if write:
            apply_file(md, replacements, unwraps)

    print(
        f"\n{'Applied' if write else 'Proposed'}: {total_fix} fix(es), "
        f"{total_unwrap} unlink(s); {total_unfix} unfixable."
    )
    return 1 if total_unfix else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
