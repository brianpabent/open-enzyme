---
name: sweep-status
description: Report the current state of the wiki-sweep automation — last successful sweep, pending file count, recent workflow runs (success/failure), and recommended next action. Use when (a) Brian asks "what's the sweep state?" or "what came back from the last sweep?" or "/sweep-status", (b) a long session is ending and you want to confirm whether anything needs catching up before declaring done, (c) before firing /sweep-catchup so we know whether it's needed at all. Skip if the registry doesn't exist yet (run `python3 scripts/sweep-state.py init` first) or if the user asks specifically for git log / synthesis.md content rather than automation state.
---

# /sweep-status — automation state at a glance

This skill answers "what's the wiki-sweep automation up to?" without making the user dig through GitHub Actions, git log, and the registry by hand. It's the diagnostic-first default — call it before /sweep-catchup, before declaring inbox-zero, and any time a sweep cycle's outcome is unclear.

It reads from three sources:

1. `logs/sweep-state.json` — the registry (component #2 of `scripts/SWEEP-ARCHITECTURE.md`). Authoritative for `last_successful_sweep`.
2. `scripts/sweep-state.py pending-paths` — pending wiki files since the cursor.
3. `gh run list --workflow=wiki-sweep.yml --limit 5` — recent workflow run outcomes (success / failure / skipped / in_progress).

## What to report

Render a tight status block. Five fields, in this order:

1. **Last successful sweep:** `<commit-short> at <timestamp>` (`<elapsed>` ago). Pull from `last_successful_sweep.commit` + `last_successful_sweep.timestamp`. Use `date -d` math or just relative-format manually.
2. **Pending paths:** `<count>` files. If 0 → "inbox zero ✓". If >0 → list the first 5 paths and "(+N more)" if applicable.
3. **Recent runs (last 5):** one line per run. Format: `<status> <conclusion> — <trigger> "<head_commit_subject_truncated>"`. Statuses: ✓ success / ✗ failure / ⏭ skipped / ⏳ in_progress. Highlight failures with their failed phase if known.
4. **Workflow currently running?** Yes / No. Pull from `gh run list --workflow=wiki-sweep.yml --limit 1 --json status`. If yes, surface the run URL.
5. **Recommended action:** one of:
   - `Hold — sweep is running` (when #4 is yes)
   - `Inbox zero — no action needed` (when pending count is 0 and no recent failures)
   - `Run /sweep-catchup` (when pending count > 0 and no run in-progress)
   - `Investigate failure: <run-url>` (when most recent run is a failure)
   - `Run sweep-state.py init` (when the registry doesn't exist)

## Concrete steps

```bash
# Registry
python3 scripts/sweep-state.py read

# Pending paths
python3 scripts/sweep-state.py pending-paths

# Recent runs
gh run list --workflow=wiki-sweep.yml --limit 5 --json status,conclusion,event,headBranch,databaseId,createdAt,headSha,displayTitle
```

If the registry file is missing, FIRST suggest running `python3 scripts/sweep-state.py init` rather than reporting partial state.

## Args

- `--json` — output the raw composite (registry + recent runs + pending count) as JSON instead of the human-readable block. Useful when chaining to another tool or skill.
- `--verbose` — include all 20 entries from `recent_runs` in the registry, plus the full `last_successful_sweep` block, plus the `gh run view` summary for the most recent failure if any.

## Don't

- Don't fire `gh workflow run` from this skill. That's `/sweep-catchup`'s job. This skill is read-only.
- Don't update the registry. The registry is updated only by Pass 3 in the workflow (atomic with the synthesis.md prepend) or by `sweep-state.py init` for first-time setup.
- Don't infer pending paths from `git log --grep='^sweep'` — that's the brittle pattern this whole architecture replaces. Always go through `sweep-state.py pending-paths`.
