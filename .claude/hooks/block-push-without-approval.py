#!/usr/bin/env python3
"""
PreToolUse hook for Claude Code's Bash tool.

Blocks publish-class commands that trigger the wiki-sweep daemon, unless
the env var `CLAUDE_PUSH_AUTHORIZED=1` is set in the shell that invokes
the command (or inline-prefixed on the command itself).

Daemon trigger conditions (per .github/workflows/wiki-sweep.yml):
  1. push to `main` branch where any file in `wiki/**.md` changed.
     Post-2026-05-08 migration: synthesis/ is sibling to wiki/, NOT under
     wiki/, so daemon-emitted writes to synthesis/queue/ + synthesis/history/
     never match the path filter. The `[skip-wiki-sweep]` commit-msg marker
     remains the canonical recursion guard.
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

Authorization (in order of precedence):
  - Already-authorized fast path → allow silently (exit 0): Brian set
    `CLAUDE_PUSH_AUTHORIZED=1` in his shell env, OR the command carries the
    inline prefix (e.g. Brian typed it in a terminal). Either skips the prompt.
  - Otherwise, a daemon-firing push returns an "ask" permission decision →
    Claude Code surfaces an APPROVAL PROMPT that Brian can approve from
    anywhere, INCLUDING remote control. This is the fix for the 2026-05-29
    bug: the hook previously hard-blocked (exit 2) with the prefix as the only
    escape, but a separate auto-mode classifier rejects Claude adding that
    prefix as a self-grant — leaving remote-control authorization with NO
    working path. An "ask" decision is the approvable path the gate always
    should have used. The protection is unchanged (daemon pushes still require
    Brian's explicit OK); only the mechanism changed from un-clearable-block
    to approve-prompt.

Exit semantics (Claude Code hook convention):
  - exit 0 with no output → allow (not push-class, OR doesn't fire daemon,
    OR already-authorized via env/prefix)
  - exit 0 with {permissionDecision: "ask"} JSON → Claude Code prompts Brian
    to approve/deny (the remote-control-approvable gate)
  We deliberately no longer use exit 2 (hard block) for the daemon gate — that
  was the un-approvable path that broke remote-control authorization.

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
    """Return wiki/**.md files in unpushed commits on the current branch,
    IF the current branch is main. Returns empty list if (a) not on main,
    (b) no upstream configured, or (c) no daemon-triggering wiki changes
    pending. Post-2026-05-08 migration: synthesis/ is sibling to wiki/,
    not under it, so synthesis/** paths don't appear here at all.
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
        # Post-2026-05-08 migration: synthesis/ is sibling to wiki/, NOT under it.
        # The wiki-sweep daemon's path filter is `wiki/**.md` only — synthesis/**
        # paths never match the filter, so no recursion guard is needed at the
        # commit-content level. The [skip-wiki-sweep] commit-msg marker remains
        # the canonical recursion guard for daemon-emitted commits.
        # wiki/**.md matches recursive — include hypotheses/, etc.
        daemon_triggering.append(line)

    return daemon_triggering


def ask(reason: str) -> None:
    """Emit a PreToolUse 'ask' permission decision and exit 0.

    Claude Code surfaces this as an interactive approval prompt — which Brian
    can approve from a terminal OR from remote control. Replaces the old
    exit-2 hard block, whose only escape (the CLAUDE_PUSH_AUTHORIZED=1 prefix)
    the auto-mode classifier rejects as a self-grant, leaving no
    remote-control-approvable path (the 2026-05-29 bug).
    """
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


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
        ask(
            "`gh workflow run wiki-sweep` triggers the wiki-sweep daemon "
            "(~$0.65 + ~9-12 min). Approve to run it, or deny to cancel."
        )

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

        # Push WOULD fire the daemon. Surface an approval prompt (approvable
        # from terminal OR remote control) rather than a hard block.
        files_preview = ", ".join(triggering[:6])
        if len(triggering) > 6:
            files_preview += f" (+{len(triggering) - 6} more)"
        ask(
            f"This `git push` fires the wiki-sweep daemon (~$0.65 + ~9-12 min): "
            f"{len(triggering)} unpushed commit(s) on main touch wiki/**.md "
            f"[{files_preview}]. Approve to push + fire the daemon, or deny to hold."
        )

    # Not a publish-class command we gate
    sys.exit(0)


if __name__ == "__main__":
    main()
