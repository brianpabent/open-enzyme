---
name: sweep-catchup
description: Fire the wiki-sweep workflow against the unsweept-wiki backlog — i.e., `wiki/*.md` files modified since the last successful Pass 3 (sweep-3-review) commit but not yet re-synthesized. Use when (a) the daemon failed silently and the backlog needs to be cleared, (b) `[skip-wiki-sweep]` markers were over-applied and substantive wiki edits were never seen by the daemon, (c) Brian explicitly says "fire a catchup sweep" or "/sweep-catchup", or (d) before declaring inbox-zero state at end of session and `git diff` shows wiki content the daemon hasn't processed. Skip when no wiki files have changed since the last successful sweep, or when the daemon is currently running (would race).
---

# /sweep-catchup — fire wiki-sweep against the backlog

This skill exists because the workflow's default diff-base computation (`git log --grep='^sweep' -n 1`) is brittle to commits with `sweep-N-...` prefixes that aren't actually daemon-generated, and to `[skip-wiki-sweep]` markers applied to substantive wiki edits. When that brittleness causes wiki files to be in a blind spot, this skill produces a clean recovery: explicit trigger paths, no diff-base regex.

It also catches up after silent workflow failures (race-on-push, transient API outage), where the daemon ran but didn't produce the expected outputs.

This is the **minimal version**. Once `logs/sweep-state.json` exists (component #2 of `scripts/SWEEP-ARCHITECTURE.md`), this skill should be refactored to read `pending_paths` directly from the registry rather than computing them from git diff. For now, the registry doesn't exist; we compute.

## When to invoke

| Situation | Invoke? | Notes |
|---|---|---|
| Brian says "/sweep-catchup" or "fire a catchup sweep" | Yes | Explicit ask. |
| End of a long session that committed substantive wiki content with `[skip-wiki-sweep]` markers | Yes | The walkthrough pattern from 2026-04-27. |
| `gh run list --workflow=wiki-sweep --limit 5` shows recent failure(s) on real wiki commits | Yes | Recovery from race / 503. |
| `git diff --name-only <last-sweep> HEAD -- 'wiki/*.md'` returns ≥1 file (excluding synthesis.md) | Yes | Pending backlog. |
| No wiki files changed since last successful Pass 3 | No | Nothing to do. Report "no backlog". |
| A wiki-sweep run is currently in-progress | No | Wait for it to finish (would race on push). Use `gh run list --workflow=wiki-sweep --limit 1` to check. |

## What to do

### Step 1 — Get the pending paths from the registry

The canonical cursor is `logs/sweep-state.json`'s `last_successful_sweep.commit`. Read it via the helper:

```bash
python3 scripts/sweep-state.py pending-paths
```

That command (a) reads the registry, (b) computes `git diff --name-only <last_successful_sweep.commit> HEAD -- 'wiki/*.md'`, (c) excludes `wiki/synthesis.md`, (d) prints one path per line, sorted and deduplicated.

If the registry is missing (`logs/sweep-state.json` doesn't exist), bootstrap it once:

```bash
python3 scripts/sweep-state.py init
```

That backfills from the latest existing `logs/v4-synthesis-*.md` log and the most recent `^sweep-3-review:` commit on main.

### Step 2 — (Validation; no separate compute step)

The list comes back already validated and sorted from Step 1. If the user passed `--base <SHA>` as an override, use this fallback path instead:

```bash
git diff --name-only <override-base> HEAD -- 'wiki/*.md' | grep -v 'wiki/synthesis\.md' | sort -u
```

### Step 3 — Validate the list

- **Empty list** → report "no backlog; nothing to sweep" and exit. Don't fire an empty dispatch.
- **Non-empty list** → show Brian the count and the first 5–10 paths. Confirm before firing. Pass 2 of the workflow costs ~$0.65 per run; firing against an empty or wrong-base list wastes that.

### Step 4 — Fire the workflow

```bash
PATHS="<space-separated paths>"
gh workflow run wiki-sweep.yml -f trigger_paths="$PATHS"
```

The `trigger_paths` input is a single space-separated string. GitHub Actions has a 1024-char limit on workflow inputs; with ~30-char path averages, you can fit ~30 files. If the backlog exceeds that, either (a) split into multiple dispatches by topic, or (b) propose to Brian that we batch them differently.

### Step 5 — Watch the run

```bash
sleep 5
gh run list --workflow=wiki-sweep --limit 1
```

Report the run URL to Brian. If they want live status, suggest `gh run watch <run-id>` (interactive). The hardened workflow takes ~9–12 minutes for a full Pass 1 + Pass 2 + Pass 3 cycle on a 29-file batch.

### Step 6 — On completion, verify outputs landed

After the run finishes:

```bash
# New synthesis log should exist
ls -lt logs/v4-synthesis-*.md | head -3

# wiki/synthesis.md should have a new sweep block prepended
git log -1 wiki/synthesis.md --format='%h %s'
```

If the workflow run failed, surface the failure mode (Pass 1 / Pass 2 / Pass 3) and which step. The hardened workflow should retry rebase 3× and retry transient API errors with backoff, so any remaining failures are likely real (auth, quota, prompt bug) rather than transient.

## Args (optional overrides)

The skill accepts free-text args from the user:

- `--base <SHA>` — override the base commit. Use this when the auto-detected base is wrong (e.g., a `sweep-3-review:` commit that landed on a partial state).
- `--paths "<list>"` — override the path list entirely. Use when the user wants to test a specific subset rather than the full backlog.
- `--dry-run` — compute the path list and show it, but don't fire the workflow. Useful for sanity-checking before spending Pass 2's $0.65.
- `--yes` — skip the "confirm before firing" prompt. Only use when the user explicitly opted in upfront.

## Don't

- Don't fire if a wiki-sweep run is already in progress. Check `gh run list --workflow=wiki-sweep --limit 1` first; if status is `in_progress`, wait or skip.
- Don't pass `wiki/synthesis.md` in the trigger_paths list. The workflow filter excludes it; passing it is silently ignored but signals you didn't read this skill.
- Don't fall back to `git log --grep='^sweep'` (the workflow's brittle default). The whole point of this skill is to bypass that regex.
- Don't update the registry yet — `logs/sweep-state.json` doesn't exist. After component #2 ships, update both this skill and the workflow to read/write it.

## Implementation note

The skill reads from the registry (`logs/sweep-state.json`) via `scripts/sweep-state.py pending-paths`. This bypasses the workflow's brittle `git log --grep='^sweep'` regex and is robust to hand-edited commits with `sweep-N-...` prefixes. The registry is updated only on Pass 3 success (atomically, in the same commit as the synthesis.md prepend), so a partial sweep cycle never moves the cursor forward.
