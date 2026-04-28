#!/usr/bin/env python3
"""
PreToolUse hook for Claude Code's Bash tool.

Mirrors `.githooks/commit-msg` but runs inside the Claude Code session,
catching `git commit` violations before they hit the local repo. The
filesystem hook is the load-bearing enforcement (works for any commit
path, including manual ones); this Claude Code hook is the
sooner-and-louder mirror so violations surface before tool execution.

Exit semantics:
  0 → allow (no violation, or not a `git commit` call we recognize)
  2 → block; stderr message is shown to Claude/user

See scripts/SWEEP-ARCHITECTURE.md §"Hooks for enforcement" for the
full rationale.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        # Not a structured payload — be permissive
        sys.exit(0)

    # Find the tool name + command across the various payload shapes
    # Claude Code has used. We check several plausible locations.
    cmd = ""
    for key in ("tool", "tool_input", "toolInput"):
        node = payload.get(key) or {}
        if isinstance(node, dict):
            params = node.get("parameters") or node.get("input") or node
            if isinstance(params, dict) and "command" in params:
                cmd = params.get("command") or ""
                break
    if not cmd:
        # Try top-level
        cmd = payload.get("command") or ""

    if not cmd or not isinstance(cmd, str):
        sys.exit(0)

    # Only validate `git commit` calls
    if not re.search(r'\bgit\s+commit\b', cmd):
        sys.exit(0)

    # Skip pure read commands
    if re.search(r'\bgit\s+commit\s+--(amend\s+--no-edit|dry-run|verbose|message-only)', cmd):
        # These are unusual; let them through
        sys.exit(0)

    # Extract the message. Three patterns to match:
    #   git commit -m "..."
    #   git commit -m '...'
    #   git commit -m "$(cat <<'EOF' ...)" — heredoc; we extract first line
    msg = ""
    m = re.search(r'-m\s+"([^"]*)"', cmd, re.DOTALL)
    if m:
        msg = m.group(1)
    else:
        m = re.search(r"-m\s+'([^']*)'", cmd, re.DOTALL)
        if m:
            msg = m.group(1)
    # Heredoc form: best-effort first-line extract
    if not msg:
        m = re.search(r"<<['\"]?(\w+)['\"]?\s*\n([^\n]+)", cmd)
        if m:
            msg = m.group(2).strip()

    if not msg:
        # Unable to extract — let the filesystem commit-msg hook handle it
        sys.exit(0)

    first_line = msg.splitlines()[0] if msg else ""
    has_skip = "[skip-wiki-sweep]" in msg
    has_sweep_prefix = bool(re.match(r"^sweep-[123]-(propagate|synthesize|review):", first_line))

    # Check whether staged files include wiki/*.md (excluding synthesis.md)
    try:
        r = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True, text=True, timeout=10,
        )
        staged = (r.stdout or "").splitlines()
    except (subprocess.SubprocessError, OSError):
        staged = []
    touches_wiki = any(
        p.startswith("wiki/") and p.endswith(".md") and p != "wiki/synthesis.md"
        for p in staged
    )

    # Author check
    try:
        author = subprocess.run(
            ["git", "config", "user.name"],
            capture_output=True, text=True, timeout=5,
        ).stdout.strip()
    except (subprocess.SubprocessError, OSError):
        author = ""
    is_bot = (author == "github-actions[bot]")

    # Rule 1: [skip-wiki-sweep] on wiki commits requires sweep-N- prefix
    if has_skip and touches_wiki and not has_sweep_prefix:
        print(
            "✗ Pre-commit hook (Claude Code, sweep automation):\n"
            "\n"
            "  This commit touches wiki/*.md and uses [skip-wiki-sweep], but the\n"
            "  message does NOT start with sweep-1-propagate:, sweep-2-synthesize:,\n"
            "  or sweep-3-review:. The marker is reserved for daemon-generated\n"
            "  commits — applying it to a hand-edit silently suppresses the\n"
            "  entire sweep workflow on this content (root cause of the\n"
            "  2026-04-27 walkthrough's 25-file blind spot).\n"
            "\n"
            "  Fix: remove [skip-wiki-sweep] from the message, OR (rare) prefix\n"
            "  the message with the matching sweep-N-... pattern.\n"
            "\n"
            "  See scripts/SWEEP-ARCHITECTURE.md §\"Hooks for enforcement\".\n",
            file=sys.stderr,
        )
        sys.exit(2)

    # Rule 2: sweep-N- prefix is reserved for the daemon
    if has_sweep_prefix and not is_bot:
        print(
            "✗ Pre-commit hook (Claude Code, sweep automation):\n"
            "\n"
            f"  Commit message starts with sweep-N-... prefix:\n"
            f"    {first_line}\n"
            "\n"
            f"  But author is \"{author}\", not \"github-actions[bot]\". The\n"
            "  sweep-N-... prefix is reserved for daemon commits — using it on\n"
            "  a hand-edit poisons the workflow's diff-base detection (the\n"
            "  legacy git log --grep='^sweep' regex), which hides subsequent\n"
            "  commits from future sweeps.\n"
            "\n"
            "  Fix: rename the commit prefix. Examples: scripts:, workflow:,\n"
            "  docs:, chore:, or any other descriptive prefix.\n"
            "\n"
            "  See scripts/SWEEP-ARCHITECTURE.md §\"Hooks for enforcement\".\n",
            file=sys.stderr,
        )
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
