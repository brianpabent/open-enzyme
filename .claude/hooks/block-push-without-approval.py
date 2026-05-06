#!/usr/bin/env python3
"""
PreToolUse hook for Claude Code's Bash tool.

Blocks publish-class commands that trigger the wiki-sweep daemon, unless
the env var `CLAUDE_PUSH_AUTHORIZED=1` is set in the shell that invokes
the command (or inline-prefixed on the command itself).

Daemon trigger conditions (per .github/workflows/wiki-sweep.yml):
  1. push to `main` branch where any file in `wiki/**.md` changed,
     EXCEPT changes only to `wiki/synthesis.md` (synthesis is excluded
     from the daemon trigger to prevent recursion)
  2. workflow_dispatch (manual run via `gh workflow run wiki-sweep.yml`)

Pushes to feature branches do NOT fire the daemon (only main triggers it).
Pushes touching only scripts/, operations/, .claude/, logs/, README, etc.
do NOT fire the daemon. Those are allowed without authorization — Brian
specifically scoped this hook to daemon-triggering pushes only (2026-05-06
clarification: "It should block when we're pushing to things that trigger
a sweep, which I think is wiki. Other things don't really matter.").

The intent: pushes that fire the daemon (~$0.65 + ~9-12 minutes per run)
are the moment Brian wants to be present for. Empirically, Claude has
treated long-running auto-mode sessions as license to push without asking,
which violates the walk-synthesis skill's per-batch-confirmation discipline.
This hook is the structural backstop.

Authorization:
  - Brian runs the command himself in his terminal (always works)
  - Brian prefixes the specific command with the one-shot env var:
      `CLAUDE_PUSH_AUTHORIZED=1 git push`
  - Brian sets `CLAUDE_PUSH_AUTHORIZED=1` in his Claude Code shell
    environment (grants session-level authorization; use sparingly)

Exit semantics (Claude Code hook convention):
  0 → allow (command not push-class, OR doesn't fire daemon, OR authorized)
  2 → block; stderr message is shown to Claude/user

See:
  - .claude/skills/walk-synthesis/SKILL.md §7.2 (push at end of batch)
  - umbrella CLAUDE.md "Executing actions with care" rule
  - .github/workflows/wiki-sweep.yml (the daemon trigger this hook gates)
  - 2026-05-06 incident where Claude pushed 24 commits during a
    walkthrough without per-item user approval, robbing Brian of
    being present for the first end-to-end test of caching + DeepSeek
    Pass 1 infrastructure he had spent the day building

Companion to .claude/hooks/validate-commit-msg.py.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Push-class command patterns. We DO NOT block all `git push` — only
# pushes that would actually fire the daemon (see check_daemon_triggering_push).
GIT_PUSH_RE = re.compile(r"\bgit\s+push\b")

# `gh workflow run wiki-sweep` is always a manual daemon trigger
WORKFLOW_RUN_WIKI_SWEEP_RE = re.compile(r"\bgh\s+workflow\s+run\s+(wiki-sweep|\.github/workflows/wiki-sweep\.yml)")


def find_command(payload: dict) -> str:
    """Extract the bash command from the various payload shapes Claude
    Code has used over time. Returns empty string if none found.
    """
    for key in ("tool", "tool_input", "toolInput"):
        node = payload.get(key) or {}
        if isinstance(node, dict):
            params = node.get("parameters") or node.get("input") or node
            if isinstance(params, dict):
                cmd = params.get("command")
                if isinstance(cmd, str):
                    return cmd
    cmd = payload.get("command")
    if isinstance(cmd, str):
        return cmd
    return ""


def find_tool_name(payload: dict) -> str:
    """Best-effort extraction of the tool name."""
    for key in ("tool_name", "toolName", "tool"):
        v = payload.get(key)
        if isinstance(v, str):
            return v
        if isinstance(v, dict):
            inner = v.get("name")
            if isinstance(inner, str):
                return inner
    return ""


def is_authorized(command: str) -> bool:
    """Check the env var in the parent shell, OR an inline prefix on the
    command itself. Either grants authorization for this single command.
    """
    if os.environ.get("CLAUDE_PUSH_AUTHORIZED") == "1":
        return True
    if re.search(r"\bCLAUDE_PUSH_AUTHORIZED=1\b", command):
        return True
    return False


def get_daemon_triggering_files() -> list[str]:
    """Return wiki/**.md files (excluding synthesis.md) in unpushed
    commits on the current branch, IF the current branch is main.
    Returns empty list if (a) not on main, (b) no upstream configured,
    or (c) no daemon-triggering wiki changes pending.
    """
    try:
        branch_proc = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, cwd=REPO_ROOT, check=True,
        )
        branch = branch_proc.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Conservative: if we can't determine branch, don't block
        return []

    if branch != "main":
        # Daemon only fires on push to main
        return []

    # Find the upstream branch
    try:
        upstream_proc = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "@{upstream}"],
            capture_output=True, text=True, cwd=REPO_ROOT,
        )
        if upstream_proc.returncode != 0:
            # No upstream configured — can't determine what would be pushed
            return []
        upstream = upstream_proc.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []

    # List files changed in unpushed commits, scoped to wiki/
    try:
        diff_proc = subprocess.run(
            ["git", "diff", "--name-only", f"{upstream}..HEAD", "--", "wiki/"],
            capture_output=True, text=True, cwd=REPO_ROOT, check=True,
        )
    except subprocess.CalledProcessError:
        return []

    daemon_triggering = []
    for line in diff_proc.stdout.strip().splitlines():
        if not line.endswith(".md"):
            continue
        if line == "wiki/synthesis.md":
            # Excluded from daemon trigger per workflow path filter
            continue
        # wiki/**.md matches recursive — include hypotheses/, etc.
        daemon_triggering.append(line)

    return daemon_triggering


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        # Not a structured payload — be permissive
        sys.exit(0)

    tool_name = find_tool_name(payload)
    if tool_name and tool_name != "Bash":
        sys.exit(0)

    command = find_command(payload)
    if not command:
        sys.exit(0)

    # Check #1: explicit workflow dispatch of the wiki-sweep
    if WORKFLOW_RUN_WIKI_SWEEP_RE.search(command):
        if is_authorized(command):
            sys.exit(0)
        print(
            f"BLOCKED: `gh workflow run wiki-sweep` always triggers the daemon\n"
            f"(~$0.65 + ~9-12 min) and Brian wants to be present for daemon\n"
            f"runs he didn't initiate. Authorize with:\n"
            f"  CLAUDE_PUSH_AUTHORIZED=1 {command}\n"
            f"\n"
            f"Or use the /sweep-catchup skill which Brian explicitly invokes.\n",
            file=sys.stderr,
        )
        sys.exit(2)

    # Check #2: git push that would fire the daemon
    if GIT_PUSH_RE.search(command):
        if is_authorized(command):
            sys.exit(0)

        triggering = get_daemon_triggering_files()
        if not triggering:
            # Not daemon-triggering — pushes touching only scripts/,
            # operations/, .claude/, logs/, hypotheses outside wiki/, etc.
            # are allowed without authorization per Brian's 2026-05-06 scope:
            # "block when we're pushing to things that trigger a sweep, which
            # I think is wiki. Other things don't really matter."
            sys.exit(0)

        # Push WOULD fire the daemon. Block.
        files_preview = "\n  ".join(triggering[:10])
        if len(triggering) > 10:
            files_preview += f"\n  (+{len(triggering) - 10} more)"
        print(
            f"BLOCKED: `git push` would fire the wiki-sweep daemon (~$0.65 +\n"
            f"~9-12 min) because {len(triggering)} unpushed commit(s) on main\n"
            f"touch daemon-triggering wiki paths:\n"
            f"\n"
            f"  {files_preview}\n"
            f"\n"
            f"Per the walk-synthesis skill §7.2 + the 2026-05-06 incident,\n"
            f"Claude must ask Brian explicitly before firing the daemon. Two\n"
            f"ways to authorize:\n"
            f"\n"
            f"  1. Brian runs the push himself in his terminal\n"
            f"  2. Brian types in conversation:  CLAUDE_PUSH_AUTHORIZED=1 git push\n"
            f"     (Claude can include this prefix only because Brian typed it.)\n"
            f"\n"
            f"Pushes touching only scripts/, operations/, .claude/, logs/, etc.\n"
            f"are allowed without authorization — only wiki-changes-that-would-\n"
            f"fire-the-daemon are gated.\n"
            f"\n"
            f"Command that triggered the block:\n"
            f"  {command}\n",
            file=sys.stderr,
        )
        sys.exit(2)

    # Not a publish-class command we gate
    sys.exit(0)


if __name__ == "__main__":
    main()
