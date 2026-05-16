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

## Inter-pass artifact handoff (added 2026-04-28)

A second class of failure surfaced after the initial five-component build: not workflow-runtime errors, but *information-loss between passes*. Two specific symptoms:

1. **Pass 2 missed connections that lived in propagated files.** Pass 1 propagates findings into downstream wiki pages (e.g. it added source attributions to `bpc-157.md`, `kpv-peptide.md`, `disulfiram.md` during the 2026-04-27 cycle). Pass 2 received only the *original* trigger file list. Even though Pass 2 reads the full corpus, its synthesizer's *attention* was biased toward triggers — connections that emerged because of Pass 1's propagation were under-weighted.

2. **Pass 3 said "I can't confirm because I don't have the trigger file."** Pre-2026-04-28, Pass 3 was a *one-shot non-agentic call*: a single OpenRouter request with the synthesis log + inlined trigger files, no tool access. When Pass 2 cited a non-trigger file (which it does constantly — `lactoferrin.md`, `abcg2-modulators.md`, etc.), Pass 3 had no way to verify. The reviewer correctly admitted it; that's not a bug in the model, it's a design gap.

Three coordinated fixes — all under the same principle: **every pass must declare what it produced for the next pass to consume**.

### `propagated_files` (Pass 1 → Pass 2)

Pass 1's Python driver now diffs its own commit and writes the list of *propagated files* (wiki pages it modified, excluding the original trigger set and `synthesis/queue/`) to `$GITHUB_OUTPUT`. The workflow promotes that to the `propagate` job's outputs, and Pass 2 receives both `trigger_files` (cause) and `propagated_files` (where new content now lives) as separate inputs.

The Pass 2 prompt's TRIGGER block names both lists explicitly with semantic labels and instructs the synthesizer: *"new cross-document connections are most likely to emerge from the union of the two sets — weight your attention there."*

### `cited_files` manifest (Pass 2 → Pass 3)

Pass 2's prompt now requires the synthesizer to emit a `Sources cited:` manifest at the bottom of its synthesis log, listing every `wiki/*.md` it referenced in any finding. Pass 2's Python driver parses that manifest (with a regex fallback that scans the entire synthesis for `wiki/<name>.md` patterns) and writes `cited_files` to `$GITHUB_OUTPUT`. The workflow promotes that to the `synthesize` job's outputs.

### Pass 3 agentic upgrade (warm cache + read-only tools)

Pass 3's driver was rewritten as a bounded agentic loop:

1. **Warm cache** — at startup, inline both `trigger_files` and `cited_files` into the reviewer's initial prompt with `=== <path> (trigger|cited) ===` separators. This covers the most likely sources without any tool round-trip.
2. **Read-only tools** — `read_file`, `list_files`, `grep`. The reviewer can investigate any file the cache missed. No edit, no write — Pass 3 is critique, not propagation.
3. **Iteration cap** — `MAX_TOOL_ITERATIONS=8`. On the last iteration the driver sets `tool_choice: "none"` to force final output. A model that returns content with no tool calls signals completion.
4. **Strict output scope preserved** — the merge script (`scripts/synthesis-emit-files.py`) still counts `<<<NEXT>>>` separators and bails on mismatch, so any preamble or commentary outside the blockquotes fails fast.

The cost trade-off: Pass 3 may now run multiple OpenRouter calls instead of one. In practice it tends to call 0–2 tools (most reviews don't need fetches beyond the warm cache), so the typical cost increase is small. The previous failure mode — review verdicts that admitted lack of access — was strictly worse than the bounded extra cost of letting the reviewer fetch on demand.

### Sequencing summary

```
Pass 1 inputs:  trigger_files (from push)
Pass 1 outputs: trigger_files + propagated_files

Pass 2 inputs:  trigger_files + propagated_files
Pass 2 outputs: synthesis_log + cited_files (parsed from manifest + regex fallback)

Pass 3 inputs:  synthesis_log + trigger_files + cited_files (all inlined as warm cache)
Pass 3 tools:   read_file, list_files, grep (read-only, bounded iterations)
Pass 3 outputs: review blockquotes (strict scope: only `<<<NEXT>>>`-separated blocks)
```

This handoff design is also why Pass 1 commits-and-pushes before Pass 2 starts: the *filesystem* state has to reflect Pass 1's work for Pass 2's full-corpus read to be valid, AND Pass 2's checkout is fresh (not a runner-cache reuse).

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

## Subagent brief hygiene: scope propagates, predictions don't (added 2026-05-08)

This section is broader than the daemon — it applies to **all subagent-briefing flows**, including comp-NNN computational experiments, lit-scan tasks, and any independent investigation a Claude session spawns into a subagent. The discipline below was empirically grounded by the comp-018 vs comp-020 retrospective ([`operations/comp-018-vs-comp-020-retrospective.md`](../operations/comp-018-vs-comp-020-retrospective.md), 2026-05-08).

### Why this matters

When a human briefs an AI subagent, the briefer's idle phrasing is *part of the experimental setup* — not just project-management overhead. Phrasings that feel like motivational context to the human ("if it's rosemary, I'll grow rosemary") read as scope guidance to the subagent ("the user expects rosemary; satisfy this expectation; promote rosemary-relevant findings"). The subagent does what its brief said; the brief silently constrained the answer. This is structurally similar to a leading question in survey methodology — it shapes the answer even when there are right answers available.

This is a class of confounder that doesn't exist in human-only research: **prompt contamination**.

### The dividing line

User direction describes either THE WORK (legitimate scope) or THE USER's hopes about the work (contamination). The fix is to keep the first and scrub the second.

**Propagate (these describe the work):**
- Scope decisions — target list, compound classes in/out, time horizon, geographic scope, what to broaden vs. narrow
- Methodological constraints — tools to use, evidence-level discipline, grep-verify requirements, multi-vendor cross-check
- What's already known or ruled out — so the subagent doesn't redo work
- Output format and reporting expectations — length cap, structure, top-of-file plain-English summary
- Project conventions — CLAUDE.md rules, phase positioning, audience framing
- Time, cost, and git-flow constraints
- Tool corrections from prior reviewer feedback ("Paperclip is wrong corpus for CNKI; do direct multilingual instead")
- Memory cautions for known unreliable tools (e.g., Paperclip's `map` operator hallucinates per `memory/feedback_paperclip_map_unreliable.md`)

**Scrub (these describe the user, not the work):**
- Contrived examples that name specific things ("if it's in rosemary I'll grow rosemary," "could be ergosterol," "maybe a flavonoid")
- Aspirational framings ("I really want this to work," "wouldn't it be amazing if Y")
- Speculative compound names the user thinks might be relevant
- Personal anecdotes that aren't directly load-bearing for the investigation
- Narrative-cohesion phrasings that aren't substantive constraints

### The sharper test

Would a competent independent researcher with no access to the user's specific phrasing do the same investigation and reach the same conclusions?

- **If yes**, the phrasing is scope/method — keep it.
- **If no** — if the user's phrasing materially constrains where the researcher would look or what they'd headline-promote — it's contamination, scrub it.

### The rhetorical-callback tell

If the subagent's report-back uses your phrasing back at you ("your X framing landed empirically," "as you suspected"), that's a signal your phrasing influenced not just the search but the framing of the result. Watch for it. It's the smoking gun for narrative-cohesion bias even when the underlying findings are real.

### Guardrail against over-correction

Stripping user direction so aggressively that the subagent loses scope context is its own bias.

- **Don't strip scope direction.** If the user says "broaden beyond fungal," that's load-bearing — removing it produces a narrow fungal-only sweep.
- **Don't strip "what's known/ruled out" context.** That prevents redundant work.
- **Don't strip methodological discipline.** Tool corrections, evidence-level rules, and multi-vendor expectations all stay.
- **DO strip examples, hopes, predictions, speculative compound names.** Those are the contamination class.

The check: would removing the phrase from the brief make the subagent's task less defined? If yes, keep it. If removing it leaves the same well-scoped investigation, scrub it.

### Verification re-run as a discipline

When a subagent brief contains user-named compounds, contrived examples, or motivational framing that could plausibly bias narrative-cohesion, the cheapest corrective is an independent re-run with a scrubbed brief. Cost: ~$5 in Opus subagent compute, 30-60 minutes wall-clock, ~25 minutes human attention. Cheap enough to default to whenever the brief contains contamination-class content.

The re-run brief should:
- Strip all compound names, contrived examples, and user phrasing
- Retain identical scope, methodology, and "what's known/ruled out" context
- Add explicit anti-bias instructions: "no compound prioritization in the headline; surface ALL compounds within ~20% of the lead metric; depth-first at each compound class; no rhetorical callbacks to user phrasing"
- Be framed as an "independent verification re-run" — the verification subagent should NOT be told what the predecessor found

The comparison happens AFTER both reports land. If they converge, confidence in the original goes up. If they diverge, you've surfaced a confounder.

### Catch from instinct, codify in discipline

The discipline above doesn't preempt first-time issues. It's the safety net for the SECOND instance of a class of problem. The FIRST instance gets caught by:

1. Human pattern-recognition / suspicion (the user notices something feels off)
2. Verification (independent test of the suspicion)
3. Codification (the discipline gets written down for next time)

For citizen scientists doing AI-assisted research without the OE project's multi-pass safety net: cultivate the instinct first. Watch for results that feel too narratively coherent with how you framed the question. That feeling is data.

### Origin: comp-018 brief contamination 2026-05-08

The comp-018 (Upstream Complement Modulator Sweep) subagent brief inadvertently included Brian's contrived "if it's in rosemary I'll grow rosemary" example as motivation. The subagent's headline finding (rosmarinic acid as TIER-1 dietary C3-convertase inhibitor) is real — Englberger 1988 PMID 3198307 is a foundational 38-year paper, and rosmarinic acid is named after rosemary because it was first isolated from rosemary in 1958 — but the *headline-promotion* of rosmarinic acid singularly (vs. luteolin, tiliroside, *Helicteres* benzofuran lignans, marine sulfated polysaccharides, ganoderic acid Sz) was contaminated by narrative-cohesion with the user phrasing. The subagent's report-back literally said "Brian's literal 'if it's in rosemary I'll grow rosemary' framing landed empirically" — the rhetorical-callback tell.

Brian's instinct caught it: *"This has got to be a hallucination — I just said rosemary because it was the first herb that popped into my head."* The verification re-run (comp-020, brief-scrubbed) found:
- Three tied tier-1 candidates instead of one (rosmarinic acid, *Helicteres* benzofuran lignans, luteolin)
- comp-018 missed *Helicteres* benzofuran lignans at the headline tier (4-20× more potent than RMA on matched assay)
- comp-018 underweighted marine sulfated polysaccharides
- The rosmarinic acid IC50 spread is 44× across assays (comp-018 noted 20-30×); the load-bearing mechanism is upstream covalent C3b modification, NOT direct C5 convertase inhibition

Underlying findings NOT contaminated. Headline-promotion WAS contaminated. Coverage breadth PARTIALLY contaminated. Brian's suspicion was empirically correct.

Full retrospective: [`operations/comp-018-vs-comp-020-retrospective.md`](../operations/comp-018-vs-comp-020-retrospective.md). External-comms entry: [`operations/notable-moments.md`](../operations/notable-moments.md) 2026-05-08 brief-contamination entry.

---

## Pilot — Tool-Gap vs. Science-Gap Disagreement Attribution (added 2026-05-15)

**Status:** Pilot. Wired into Pass 3 prompts (`scripts/sweep-prompt-3-review.md` + `scripts/sweep-prompt-3-review-gpt55.md`) for the next 2–3 sweep cycles starting 2026-05-15. Evaluated against the promote/abandon gates below. Not a permanent architecture change yet.

### What changed

When the Pass 3 reviewer emits a disagreement verdict (`Partial` / `Push back` / `Rejected`), the reviewer also emits a `[GAP: <tag>]` annotation immediately after the existing `[OVERLAP: <tag>]` annotation. Confirmed / Confirmed-prioritize / Augment / Defer verdicts get no GAP tag.

Available tags:

- **`tool-gap`** — Pass 2 identified the right topic / mechanism / connection but executed wrong: wrong magnitude, wrong citation, conflated entities, wrong assay format / dose / unit, wrong polarity, misread an evidence-tier tag. The synthesizer understood the biology; the failure is in plumbing.
- **`science-gap`** — Pass 2 surfaced a connection that doesn't hold biologically. Misunderstood mechanism, applied a pattern from one system where it doesn't transfer, claimed a chokepoint relevance the biology doesn't support. The plumbing was OK; the biology understanding is wrong.
- **`both`** — Both failure modes contribute; reviewer specifies which dominates.
- **`unclear`** — Reviewer can tell the synthesizer is wrong but can't cleanly attribute the failure.

### Why

The sweep daemon's existing 3-pass design (Pass 1 Propagate → Pass 2 Synthesize → Pass 3 Critique, with a Pass 4 DeepSeek peer-reviewer planned) is a guard against epistemic homogenization across vendors. But when reviewers disagree with synthesizers, the existing verdict tags (Confirmed / Partial / Push back / Rejected) are **adjudicatory** — they tell the human *that* there's a problem, not *where to look*. Adding a tool-gap vs. science-gap axis converts the disagreement into a **diagnostic**:

- "Push back, tool-gap" → reviewer trusts Pass 2's biology understanding; the citation / number / mechanism-label needs fixing
- "Push back, science-gap" → reviewer disagrees with Pass 2's biology read entirely; the connection itself may not hold
- "Push back, both" → fix the plumbing AND re-examine whether the connection is real
- "Push back, unclear" → the disagreement is interpretive; surface for human adjudication

Over time, per-model patterns emerge ("Gemini Pass 2 consistently shows science-gap failures on intracellular trafficking biology" → re-route trafficking-relevant claims to a different synthesizer). This is the kind of self-knowledge a multi-vendor sweep daemon should have but currently doesn't.

The decomposition is named in the BioDesignBench preprint (bioRxiv 2026.05.06.723381) per their finding that DeepSeek V3 and GPT-5 are dominated by tool-gap and Gemini 2.5 Pro by science-gap on the 76-task benchmark. **BioDesignBench remains PRIMARY-SOURCE-PENDING** ([`wiki/bio-ai-tools.md`](../wiki/bio-ai-tools.md) §BioDesignBench — PDF fetch was Cloudflare-blocked 2026-05-12). The pilot draws on the *idea* without depending on the preprint's empirical claims; if BioDesignBench fails verification, the pilot still stands or falls on its own utility.

### Promote / abandon gates

Evaluated after ~3 sweep cycles past 2026-05-15:

**Promote to permanent if all three hold:**

1. **Signal density.** At least 30% of disagreement verdicts (Partial / Push back / Rejected) get a clean tool-gap or science-gap attribution (not "unclear" or "both"). Fewer than 30% clean attribution means the diagnostic isn't discriminating enough to be useful.
2. **Per-model patterns.** At least one model (Pass 2 synthesizer, Pass 3 reviewer, or Pass 4 DeepSeek when implemented) shows a >2× skew toward one gap type. Without a per-model pattern, the tag is just labeling individual disagreements without surfacing routable signal.
3. **Walkthrough utility.** The walkthrough operator (Brian, or Claude on Brian's behalf) reports at least one item where the GAP tag changed the closure action — e.g., a tool-gap verdict led to a citation-fix annotation rather than a wiki rewrite, or a science-gap verdict triggered a deeper grep of the underlying biology page rather than a quick patch.

**Abandon if any of the following:**

- **Cargo-cult tagging.** Reviewers emit "tool-gap" or "science-gap" without substantive attribution in the reasoning, defaulting to one tag (e.g., "tool-gap" applied to everything because it sounds less harsh). The tag becomes noise.
- **Mode collapse.** >80% of disagreements tag as "unclear" or "both." The dichotomy isn't carving reality at its joints in this domain; abandon and try a different decomposition.
- **Operational burden.** Prompts get unwieldy; reviewers spend more tokens debating gap attribution than verifying claims. The diagnostic costs more than it produces.

### Implementation surface

- `scripts/sweep-prompt-3-review.md` — Opus variant; added Gap tag vocabulary section + format update + strong-push-back example update
- `scripts/sweep-prompt-3-review-gpt55.md` — GPT-5.5 variant; added Decision rule — GAP tag section + format update + example
- No Pass 4 prompt file exists yet (DeepSeek pass implementation pending). When it lands, mirror the GAP tag instruction into the Pass 4 prompt.
- `wiki/bio-ai-tools.md` §BioDesignBench — points at this pilot section so the methodology-upgrade-candidate mention has a concrete operational home.

### Origin

Surfaced as 2026-05-13 sweep Connection 2 in `synthesis/done/2026-05-13-connection-2-the-biodesignbench-tool-gap-vs-science-gap-decomposition.md`. Pass 3 verdict was "Partial" with the suggestion to pilot rather than commit; this section is the pilot.

---

## Static-rubric bias in Pass 2 + Pass 3 recommendations (added 2026-05-16)

**Status:** Architectural-bias observation. Not a bug per se — a pattern in synthesizer / reviewer recommendation generation that the walkthrough operator should de-prefer when it surfaces.

### The pattern

Pass 2 and Pass 3 both have a tendency to recommend **adding a static documented rule / rubric / framework** when the underlying decision process is already implemented dynamically by the sweep daemon itself. This is documentation-for-documentation: the daemon already does what the documented rule would describe, and the static doc will drift from the live evaluator faster than the evaluator updates.

### Canonical case — 2026-05-16 walkthrough Item 6

Sweep `ebbce26` Contradiction 1 (chassis-pending list dilution risk) framed the issue as a "strategic design gap" requiring a "chassis triage rubric" — Pass 3 confirmed and tightened the framing to "chokepoint-first triage rule keyed to chokepoint leverage, evidence tier, cheapest first move, and chassis maturity."

The walkthrough operator pushed back: the daemon's Pass 2 already re-evaluates every chassis-pending entry against the current corpus state on every sweep, and the walkthrough operator's per-item decision IS the promote / park / falsify call. The same walkthrough (Items 1–5) produced concrete evidence of this mechanism working: PDB×disulfiram CP6 stack named (Item 1), CFTR-corrector Q141K chaperone promoted to comp-032 (Item 2), inhaled mRNA-IL-1RA temporal-complement framing landed in open-enzyme-vision.md + comp-033 (Item 4). None of these required a documented rubric to action.

The synthesizer and reviewer both fell into a "name a rule and document it" frame. A static rubric there would have been:

- Documentation that re-derives what Pass 2 already does
- A snapshot of heuristics that will drift from the live daemon's evaluation
- Onboarding / audit benefits at a scale where they're not yet load-bearing for a one-operator project

The pushback is the right answer. Closure for Item 6 was a single-paragraph annotation in `chassis-pending-interventions.md` "How decisions actually get made — there's no static rubric, by design" — naming the dynamic mechanism explicitly so the page is self-documenting, but adding no rubric.

### Operational guidance for future walkthroughs

When a Pass 2 / Pass 3 recommendation reads as "add a documented rule / framework / rubric for [decision type the daemon already makes]," the walkthrough operator should consider:

1. **Is this rule already implemented in the daemon's evaluation logic?** If yes, the static doc is at best a redundant mirror, at worst a drifting artifact. Default to: close with a short annotation naming the dynamic mechanism; skip the rubric.
2. **Would the rule constrain decisions the daemon cannot currently surface?** Rare, but real — if the rule encodes a constraint the daemon's prompts don't enforce (e.g., regulatory / safety / privacy gates), the static doc has independent value. Action: add the rule AND update the relevant pass prompt so the daemon enforces it dynamically going forward.
3. **Is the rule documenting a process across multiple operators or partner organizations?** Only useful at multi-operator scale. Defer until that scale arrives.

The most common case is (1). Default to "close with a dynamic-mechanism annotation, no rubric."

### Implication for the tool-gap vs. science-gap pilot

This bias is orthogonal to the tool-gap / science-gap decomposition (above) but interacts with it: a Pass 3 review that says "tool-gap, add a rubric" is doubly suspect — tool-gap because the synthesizer's framing was off, AND rubric-bias because the proposed fix is documentation-for-documentation. Future Pass 3 prompt iterations could add a check: "before recommending a documented rubric / framework, verify the recommendation isn't just re-describing existing daemon behavior."

### Origin

2026-05-16 walkthrough Item 6. Closure annotation at `synthesis/done/2026-05-15-contradiction-1-the-chassis-pending-intervention-list-risks-diluting-the.md`.

---

## Pass 3 trigger-file awareness gap (added 2026-05-16)

**Status:** Architecture gap named. Prompt-engineering fix queued as an "Open improvements" follow-up below; not yet implemented.

### The failure mode

Pass 3's review discipline relies on grep-based verification: when Pass 2 cites a section or claim ("`bio-ai-tools.md §BioDesignBench` closes this tool gap"), Pass 3 greps the corpus for the citation and either confirms or pushes back based on what the grep returns. **This breaks when the trigger commit itself contains the load-bearing content.**

Concretely: Pass 3 today doesn't know which file(s) triggered the sweep. It sees the Pass 2 output and the corpus state, but it doesn't receive the *trigger-commit diff* as context. So when Pass 2 cites brand-new content that was added in the same commit that fired the daemon, Pass 3's grep operates as if the corpus state is stable and treats the new content as either invisible (false-negative grep) or just-another-page-that-might-have-been-there-yesterday. The reviewer can't distinguish *"Pass 2 hallucinated a section that doesn't exist"* from *"Pass 2 saw a brand-new section that was just added, which I also have access to but my grep missed."*

### Canonical case — 2026-05-16 walkthrough Item 5

The sweep on commit `ebbce26` was triggered by changes to `wiki/etc/bio-ai-tools.md` that added the §BioDesignBench section (~75 lines, including the protein-design-mcp install record and the explicit "RFdiffusion + ProteinMPNN NOT currently in OE stack — gap to investigate for DAF SCR1-4 + lactoferrin redesign work" framing). Pass 2 correctly synthesized a connection between this new content and `lactoferrin.md §12 #13` (which was added in the same commit and explicitly named the same tool gap).

Pass 3's review:

> "The central page-reading claim is wrong: ... a direct grep of `wiki/etc/*.md` also returned no matches for 'BioDesignBench' or 'protein-design-mcp,' contradicting the claim that `bio-ai-tools.md §BioDesignBench` closes this tool gap via that package."

The grep claim is empirically wrong against the trigger-commit state — both terms are in the file at lines 752 and 810+. The Pass 3 reviewer either (a) actually ran the grep but got a false-negative because of path semantics or timing, or (b) didn't actually run the grep and reported a hallucinated empty result, or (c) ran the grep before the trigger-commit changes had landed in its view of the corpus. All three failure modes share a common root: **the reviewer lacks structural awareness of which content is new in this sweep cycle.**

Had Pass 3 received trigger-commit context — *"this sweep was triggered by changes to `wiki/etc/bio-ai-tools.md` (+75 lines, new §BioDesignBench section) and `wiki/lactoferrin.md` (+1 line in §12, #13 added)"* — the review would have read very differently:

> "Verdict: **Confirmed, prioritize.** This connection is grounded in newly-added content in `wiki/etc/bio-ai-tools.md`'s §BioDesignBench (added in the trigger commit itself). Pass 2's claim that RFdiffusion + ProteinMPNN were 'absent from OE's stack' is accurate as of immediately before the trigger commit; the same commit added the gap-identification text AND the A1 (CPU-mode) install record. State changed within the trigger commit. Action: reconcile `lactoferrin.md §12 #13` (still describes the pre-install state) against `bio-ai-tools.md` A1's post-install state."

That's the **opposite verdict** from what Pass 3 actually produced. The pushback was a false-negative caused by trigger-blindness, not a real biology / plumbing disagreement.

### Implication for the tool-gap vs. science-gap pilot

This failure mode interacts with the tool-gap / science-gap pilot above: a trigger-blind Pass 3 will systematically over-emit `Push back / tool-gap` for legitimate cross-references between newly-added content. The pilot's signal-density metric (≥30% clean attribution) is contaminated by these false-negatives. The trigger-awareness fix is a prerequisite for clean evaluation of the tool-gap pilot — without it, the pilot's promote/abandon gates are testing the wrong thing.

### Proposed fix

The orchestrator script (`scripts/sweep-3-review.py` or its caller) should compute the trigger-commit diff and pass it to the Pass 3 prompt as explicit context:

```
TRIGGER CONTEXT:
The following files were modified in the commit(s) that triggered this sweep cycle:

- wiki/etc/bio-ai-tools.md: +75 lines (new §BioDesignBench section, A1 install record, ...)
- wiki/lactoferrin.md: +1 line in §12 (#13 added)

Pass 2 connections referencing content in newly-added sections of these files are
legitimate cross-references, NOT hallucinations. When verifying such claims, you have
two valid actions:

  (a) Grep the post-trigger corpus state — the new content is there; if your grep
      doesn't find it, your grep is wrong, not the corpus.
  (b) Treat the Pass 2 claim as confirmed against the trigger diff itself.

Do NOT mark a Pass 2 connection as "Push back / page-reading claim is wrong" solely
on the basis of a grep result that contradicts the trigger diff. If your grep
disagrees with the trigger diff, the trigger diff wins.
```

Implementation surface:
1. `scripts/sweep-3-review.py` — compute `git diff <triggering-commit>~..<triggering-commit> -- wiki/*.md` and inject summary into the Pass 3 prompt's context. Same for the GPT-5.5 variant.
2. `scripts/sweep-prompt-3-review.md` + `scripts/sweep-prompt-3-review-gpt55.md` — add a "Trigger context" section near the top of the prompt with the instructions above.
3. Pass 4 (DeepSeek) prompt when implemented — mirror the same trigger-awareness pattern.

This is **not a structural redesign of Pass 3**; it's a prompt-engineering fix that gives Pass 3 the context it's currently missing. The cost is small (~500 tokens of context per sweep) and the benefit is eliminating an entire class of false-negative reviews.

### Why this matters beyond one item

The sweep daemon's value proposition is that it catches inconsistencies that humans miss. When the daemon itself emits false-negative review verdicts on legitimate connections, the walkthrough operator has to manually adjudicate, which:

1. Reverses the daemon's value (the human is doing the verification the daemon was supposed to do)
2. Erodes trust in Pass 3 verdicts (operators learn to treat Push-back as "maybe Pass 3 is wrong")
3. Creates a systematic blind spot specifically for **brand-new content** — exactly the content most likely to contain load-bearing platform updates worth catching

The fix is cheap; the cost of not fixing it scales with how often the daemon emits Push-back verdicts on trigger-content connections (which is unbounded — every sweep is a candidate).

### Open improvements queue

Items in this section are concrete prompt/orchestrator changes that have been named but not yet implemented. Track here so they're visible when anyone next touches sweep architecture.

- **[2026-05-16] Pass 3 trigger-file awareness** — implement the orchestrator change + prompt update described above. Estimated effort: ~1 hour of script work + prompt iteration; can be done as a follow-up walkthrough item when scheduled. The 2026-05-16 walkthrough Item 5 case is the canonical empirical example for the implementation PR description.

---

## Cross-references

- The Alma project's hooks-and-skills pattern is the explicit precedent (Brian, 2026-04-28). Same structural insight: conventions that are checked don't drift; conventions that depend on memory always do, eventually.
- Global `CLAUDE.md` "Curiosity and First-Principles Framing" — invert the usual filter, ask "what open question might this tool answer?" rather than "does this fit the chassis?" Applied here: the chassis is "the sweep daemon"; the open question is "how do we make it self-healing under realistic operating conditions (concurrent pushes, transient API failures, operator typos)?"
- The two race-condition / API-503 failures ([run `25051936845`](https://github.com/brianpabent/open-enzyme/actions/runs/25051936845), [run `25049501442`](https://github.com/brianpabent/open-enzyme/actions/runs/25049501442)) are the load-bearing evidence that motivated this architecture. Anything in this doc that doesn't trace back to a real observed failure should be regarded with skepticism.
- The daemon protocol itself: [`.github/workflows/wiki-sweep.yml`](../.github/workflows/wiki-sweep.yml), [`scripts/sweep-1-propagate.py`](./sweep-1-propagate.py), [`scripts/synthesize.py`](./synthesize.py), [`scripts/sweep-3-review.py`](./sweep-3-review.py).
