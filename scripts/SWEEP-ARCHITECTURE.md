# Sweep Automation Architecture

Permanent reference for the wiki-sweep daemon. Captures the failure modes that motivated a redesign, why convention-as-memory was insufficient, and the five-component recovery architecture. Engineering doc — no evidence-level tags; same prose discipline as the wiki (no marketing language, state limitations explicitly).

The daemon under discussion is defined in [`.github/workflows/wiki-sweep.yml`](../.github/workflows/wiki-sweep.yml) and orchestrates three OpenRouter-routed passes (Sonnet 4.6 propagate → Gemini 2.5 Pro synthesize → Opus 4.7 review). Background context: [`CLAUDE.md` § "Workflow for Updates"](../CLAUDE.md) and the umbrella [`abent/CLAUDE.md` § "Git steward pattern"](../../CLAUDE.md).

---

## Failure modes observed (2026-04-28)

Two concrete failures, both within the same 24-hour window, root-caused below.

### Run [`25051936845`](https://github.com/brianpabent/open-enzyme/actions/runs/25051936845) — race on push

Triggered by commit `5e106e9` (modality × target matrix, 2026-04-28).

- Pass 1 (propagate, Sonnet 4.6) completed and committed `ee28c63`.
- Pass 2 (synthesize, Gemini 2.5 Pro) ran fully — generated `logs/v4-synthesis-2026-04-28-5e106e9.md` (62 lines, $0.7288 via OpenRouter), committed locally on the runner.
- `git push` failed: `! [rejected] main -> main (fetch first)`. A concurrent commit had landed on `main` between Pass 1's push and Pass 2's push.
- Pass 3 never ran. The runner tore down with the synthesis commit only in the ephemeral local clone; the artifact and its commit are unrecoverable.

**Root cause:** no `git pull --rebase origin main` before push in any pass after Pass 1. Concurrent activity on `main` (which is normal during a push-driven sweep — Pass 1 itself pushes) is sufficient to lose the entire downstream pipeline.

### Run [`25049501442`](https://github.com/brianpabent/open-enzyme/actions/runs/25049501442) — transient API outage

Triggered by commit `3beb17f` (open-questions co-engineered substrate-supply, 2026-04-28).

- Pass 1 OpenRouter call returned HTTP 503: `OpenRouter call failed (exit 22): curl: (22) The requested URL returned error: 503`.
- The shell wrapper exited non-zero on the first failed `curl`. No retry.

**Root cause:** no retry-with-backoff in the OpenRouter caller. A single transient upstream blip (OpenRouter is itself a routing layer over multiple vendor APIs; 503s are routine and usually clear within seconds) terminates the full sweep.

### Operational signal

Both failures left no signal beyond the GitHub Actions run status itself. Brian had to ask "what came back from the last sweeps?" to discover them. Both consumed real budget at Pass 1 (and Pass 2 in the first case) without producing the artifact those passes were paid to produce. Neither retried automatically. Neither created an issue, posted a comment, or wrote a ledger entry — the only trace of run `25051936845`'s lost synthesis was the cost line in the OpenRouter dashboard.

---

## Why memory rules don't work for this class of problem

Two operator-side failures from the same week are structurally identical to the workflow failures: a string-matching convention where the cost of a typo is "the next 30 file changes get silently lost."

1. **Over-marking with `[skip-wiki-sweep]`.** The marker convention says "use this on commits the daemon itself produces, to prevent recursion." During the 2026-04-27 walkthrough I added the marker to ~10 hand-authored commits with substantive wiki content (`6fa817b`, `a82296b`, `b110920`, others). Each suppressed the entire workflow. The intent ("don't recursively trigger the daemon") was right; the application ("on every commit because every commit feels internal") was wrong. The convention has no symmetric reminder mechanism — once the operator has internalized it, the only feedback that the application is wrong is "the sweep didn't run, and I won't notice until I look."

2. **`sweep-1-propagate:` prefix on a hand-edit.** Commit `a8f15c3` was a script edit (the dedup-aware-propagation prompt fix), but its message started `sweep-1-propagate: dedup-aware…` because the change was about that pass. The workflow's diff-base computation `git log --grep='^sweep' -n 1` then anchored the next sweep window on this hand-edit, hiding all earlier work from any future sweep. The prefix was descriptively accurate and structurally lethal.

Both errors are easy to make and the cost is delayed. The fix is not "remember harder" — it's hooks-as-enforcement and a registry-as-source-of-truth so the convention is *checked*, not *assumed*. This is the explicit precedent from the Alma project (Brian's note 2026-04-28): conventions that are checked don't drift; conventions that depend on memory always do, eventually.

---

## Architecture (5 components)

### 1. Workflow hardening

**Scope:** `.github/workflows/wiki-sweep.yml`, `scripts/sweep-1-propagate.py`, `scripts/synthesize.py`.

Three concrete changes, all addressing the two observed failure modes without introducing new infrastructure:

- **Rebase before push.** Every pass that pushes runs `git pull --rebase origin main` immediately before `git push`. On rebase conflict (rare; Pass artifacts are write-only into `logs/` and `wiki/` updates are the daemon's exclusive lane), abort the pass and fall to the failure ledger.
- **Retry with backoff on OpenRouter calls.** Wrap the `curl` invocation in a 3-attempt retry: 5s, 15s, 45s backoff. Treat HTTP 5xx and curl exit codes 6/7/22/28 as retryable; treat HTTP 4xx as fatal (those indicate prompt or auth bugs, not transient outages). Log each retry to the run output.
- **Push-failure ledger.** On any non-recoverable failure, write `logs/failed-sweep-<sha>.md` capturing pass number, model, prompt path, error message, and cost-so-far. Upload as a workflow artifact via `actions/upload-artifact@v4` so the artifact survives runner teardown even when the commit doesn't. The ledger is also the input to component #5 (cron watchdog).

This is the immediate code-level fix. Eliminates the two observed failure modes without touching the rest of the pipeline.

**Complexity:** Low. ~3 file edits.

### 2. State registry

**Scope:** new file `logs/sweep-state.json` (or `.sweep/cursor.json` if we want it out of the artifact stream). Atomic-write at Pass 3 success.

Replaces the brittle `git log --grep='^sweep' -n 1` regex as the source of truth for "what has been swept and what hasn't." The registry is canonical; commit-message patterns become a debugging aid only.

```json
{
  "schema_version": 1,
  "last_full_sweep_commit": "ee28c63a4f...",
  "last_full_sweep_timestamp": "2026-04-28T14:32:11Z",
  "last_full_sweep_run_id": "25051936845",
  "pending_paths": [
    "wiki/uricase.md",
    "wiki/engineered-koji-protocol.md",
    "wiki/nlrp3-exploit-map.md"
  ],
  "recent_failures": [
    {
      "run_id": "25049501442",
      "commit": "3beb17f",
      "pass": 1,
      "error": "OpenRouter 503",
      "timestamp": "2026-04-28T09:14:02Z"
    }
  ]
}
```

`pending_paths` is computed at Pass 1 entry as the diff between `last_full_sweep_commit` and `HEAD` filtered to `wiki/*.md`. It's persisted so that a Pass-1 failure doesn't lose the work-list — Pass 1 retries (manual via `/sweep-catchup` or automatic via component #5) read the same list.

**Migration:** one-shot script that reads the existing `logs/v4-synthesis-*.md` filenames (which embed the trigger commit) to seed `last_full_sweep_commit` to the most recent successful synthesis.

**Complexity:** Low-Medium. New file format, Pass 3 writer, one-shot migration.

### 3. Hooks for enforcement

Two layers, both checking the same invariants:

- `[skip-wiki-sweep]` is permitted **only** on commits that also carry a `^sweep-[123]-` subject prefix (i.e., daemon-authored).
- `^sweep-[123]-` subject prefix is permitted **only** when the commit author is `github-actions[bot]`.

#### 3a. Filesystem `pre-commit` hook

`.git/hooks/pre-commit` (installed via `scripts/install-hooks.sh` so it's reproducible across clones):

```bash
#!/usr/bin/env bash
set -euo pipefail

msg_file=".git/COMMIT_EDITMSG"
[[ -f "$msg_file" ]] || exit 0
subject=$(head -n1 "$msg_file")
author_email=$(git config user.email)
touches_wiki=$(git diff --cached --name-only | grep -E '^wiki/.*\.md$' || true)

if grep -q '\[skip-wiki-sweep\]' <<<"$subject"; then
  if ! [[ "$subject" =~ ^sweep-[123]- ]]; then
    echo "ERROR: [skip-wiki-sweep] is reserved for daemon commits." >&2
    echo "       Subject must start with 'sweep-{1,2,3}-' to use it." >&2
    exit 1
  fi
fi

if [[ "$subject" =~ ^sweep-[123]- ]]; then
  if [[ "$author_email" != *"github-actions[bot]"* ]]; then
    echo "ERROR: 'sweep-N-' prefix is reserved for the daemon." >&2
    echo "       Use a different verb (e.g., 'fix sweep-1 prompt: ...')." >&2
    exit 1
  fi
fi
```

#### 3b. Claude Code `PostToolUse` hook on `Bash`

Catches violations *inside* the Claude Code session, before the bad commit hits the local repo (and before the filesystem hook would refuse it — same check, earlier surface, with a Claude-readable error so the agent can self-correct).

Wired via `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "command": "scripts/hooks/check-sweep-commit.sh",
        "match_command_regex": "^git commit"
      }
    ]
  }
}
```

The script reads the just-attempted commit message and applies the same regex. On violation it returns a non-zero exit, which Claude Code surfaces back to the agent as a tool error.

**Complexity:** Low. ~30 lines bash + one settings.json entry.

### 4. Skills (user-invocable ops)

Three slash commands at `.claude/skills/*.md`. All read the registry from component #2.

- **`/sweep-status`** — reads `logs/sweep-state.json`, reports cursor age (HEAD distance from `last_full_sweep_commit`), `pending_paths` count, the last 3 entries of `recent_failures`, and a recommended action ("registry current; nothing to do" / "29 paths pending, run `/sweep-catchup`" / "3 consecutive failures — investigate before retry").

- **`/sweep-catchup`** — fires `gh workflow run wiki-sweep.yml -f trigger_paths="<paths>"` with paths sourced from the registry's `pending_paths` (or an explicit override list as argument). Bypasses the diff-base regex entirely. **Ships before component #2** so the existing 29-file backlog can be tested against the hardened workflow; refactored to read the registry once #2 lands.

- **`/sweep-validate`** — end-of-session sanity check. Compares registry state against actual git state (does `last_full_sweep_commit` exist? Is it ancestor of `HEAD`? Do `pending_paths` exist on disk?). Designed to be wired as a Claude Code `Stop` hook so it runs automatically at conversation end without operator action.

**Complexity:** Low each. ~50 lines of skill markdown.

### 5. Catch-up cron (safety net)

**Scope:** new file `.github/workflows/sweep-watchdog.yml`. Runs daily on a cron trigger (`0 13 * * *` — 9am ET, after Brian's typical morning review).

Logic:

1. Read `logs/sweep-state.json`.
2. If `last_full_sweep_commit` is >24h behind `HEAD` AND `pending_paths` is non-empty, fire `workflow_dispatch` against `wiki-sweep.yml` with the pending paths as input.
3. If `recent_failures` shows ≥3 consecutive failures with no intervening success, **do not retry**. Open a GitHub issue with the failure ledger contents and stop.

The 3-failure brake is the load-bearing protection against runaway cost. Bounded cost: 1 watchdog run per day, plus at most 1 sweep run it can trigger.

**Complexity:** Low. ~50-line YAML + small bash watchdog.

---

## Priority sequencing

Order Brian agreed to on 2026-04-28:

1. **Workflow hardening (#1)** — first. Eliminates the two observed failure modes immediately.
2. **`/sweep-catchup` skill (minimal version)** — second, in parallel with this doc. Needed to test #1 against the current 29-file backlog before any further work.
3. **State registry (#2)** — third. Refactor `/sweep-catchup` to read from the registry once it exists.
4. **Hooks (#3)** — fourth. Filesystem `pre-commit` and Claude Code `PostToolUse`.
5. **Remaining skills (#4)** — fifth. `/sweep-status`, `/sweep-validate`.
6. **Catch-up cron (#5)** — last. Final safety net, only meaningful once #2 exists.

Note: `/sweep-catchup` ships before the registry deliberately, so the backlog test of #1 can happen as early as possible. After the registry lands, refactor the skill to read from it instead of taking explicit path arguments.

---

## Cost / scope estimate

Per the [umbrella `CLAUDE.md` § "Estimates and Scoping"](../../CLAUDE.md), framed in complexity rather than wall time.

| # | Component | Complexity | Iteration risk | Context load |
|---|---|---|---|---|
| 1 | Workflow hardening | Low | Low — testable against current backlog | Small — 3 files |
| 2 | State registry | Low-Medium | Medium — schema choices propagate | Medium — touches every pass |
| 3 | Hooks (filesystem + Claude) | Low | Low — pure validation logic | Small — isolated |
| 4 | Skills (3 commands) | Low each | Low — read-only against registry | Small each |
| 5 | Cron watchdog | Low | Medium — autonomous trigger; brake is load-bearing | Small — single workflow |

Total scope: **medium project**. The system goes from "memory + ad-hoc commit-message conventions" to "self-healing pipeline with a typed state file, enforced invariants, and operator visibility into pending and failed work."

---

## Cross-references

- The Alma project's hooks-and-skills pattern is the explicit precedent (Brian, 2026-04-28). Same structural insight: conventions that are checked don't drift; conventions that depend on memory always do, eventually.
- Global `CLAUDE.md` "Curiosity and First-Principles Framing" — invert the usual filter, ask "what open question might this tool answer?" rather than "does this fit the chassis?" Applied here: the chassis is "the sweep daemon"; the open question is "how do we make it self-healing under realistic operating conditions (concurrent pushes, transient API failures, operator typos)?"
- The two race-condition / API-503 failures ([run `25051936845`](https://github.com/brianpabent/open-enzyme/actions/runs/25051936845), [run `25049501442`](https://github.com/brianpabent/open-enzyme/actions/runs/25049501442)) are the load-bearing evidence that motivated this architecture. Anything in this doc that doesn't trace back to a real observed failure should be regarded with skepticism.
- The daemon protocol itself: [`.github/workflows/wiki-sweep.yml`](../.github/workflows/wiki-sweep.yml), [`scripts/sweep-1-propagate.py`](./sweep-1-propagate.py), [`scripts/synthesize.py`](./synthesize.py), [`scripts/sweep-3-review.py`](./sweep-3-review.py).
