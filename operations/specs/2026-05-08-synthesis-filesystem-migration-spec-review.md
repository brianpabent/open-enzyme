---
title: "Spec Review — synthesis-filesystem-migration (2026-05-08)"
date: 2026-05-08
reviewer: Claude Opus 4.7 (1M context)
status: independent peer review
related:
  - 2026-05-08-synthesis-filesystem-migration.md
---

# Spec Review — synthesis-filesystem-migration (2026-05-08)

## Verdict

**NEEDS REWORK — major issues, spec should be revised before implementation**

The core architectural choice is sound and the design decisions in §5 are mostly defensible. But the spec materially under-scopes the migration in two load-bearing ways, and ships at least one design decision that will silently break in CI:

1. **§4 file list is incomplete.** The spec names ~15 files, but the actual cross-reference graph for `synthesis.md` touches 27+ wiki pages (`grep -rln "synthesis\.md" wiki/` returns 27 files distinct from `wiki/synthesis.md` itself), 5 `.claude/skills/`, 3 hook scripts, the README, mkdocs.yml, and several other operational files. Success criterion 11 ("no `wiki/synthesis.md` references remain anywhere") cannot be met with §4's list. Either the criterion needs scoping down to "no functional references" + a defined policy for cross-link rewrites, or §4 needs to grow substantially.
2. **§5.7 path-filter design is wrong for GitHub Actions.** Adding `'!synthesis/**'` to a `paths:` filter that already lists `'wiki/**.md'` does not protect against daemon recursion the way the spec claims — `paths:` is a filter on which files trigger the workflow, not a guard that excludes pushes whose touched files include the negated pattern. A push that modifies `synthesis/queue/foo.md` AND `wiki/anything.md` will still fire. The current `'!wiki/synthesis.md'` works only because daemon-emitted commits touch only that one file. The new design needs to be re-thought: either daemon emits ONLY to `synthesis/` (so its commits never touch `wiki/**.md`), or recursion protection moves entirely to the `[skip-wiki-sweep]` marker.
3. **Pass 3 review-blockquote → file mapping is under-specified.** §5.3 says the script writes one file per Pass 2 item with the Pass 3 blockquote appended. But Pass 2 emits items in 7 sections (Connections / Contradictions / Experiments / Open Questions / Priority Actions / Riskiest Assumption / Most Curious Thread), and the merge script today maps `<<<NEXT>>>`-separated blockquotes to `{{PEER-REVIEW}}` markers in order. The spec doesn't describe how the new script extracts Pass 2 items from the synthesizer log (the existing merge script doesn't — it does string substitution within an opaque body). Authoring `synthesis-emit-files.py` requires a real parser for the Pass 2 markdown structure, and the spec hasn't specified what that parser does or how to handle parsing failures.

A revised spec with §4 expanded, §5.7 redesigned, and §5.3 made concrete (or delegated to a separate parser-design subsection) would be approvable.

## Critical findings (must address before implementation)

### 1. §4 — File list is materially incomplete

**What's wrong.** The spec lists ~15 files. A grep across the repo finds substantially more references that fall into several classes:

**Daemon-machinery files the spec misses:**
- `scripts/sweep-1-propagate.py` — line 50 lists `wiki/synthesis.md` in `READ_ONLY_GLOBS` (the model is forbidden to write to it); lines 524 and 528 mention it in the propagation prompt context; line 598 excludes it from the `propagated_files` output. All four references need updating.
- `scripts/synthesize.py` — line 419-420 explicitly excludes `wiki/synthesis.md` from `cited_files`. Needs updating to exclude `synthesis/**` instead.
- `scripts/sweep-3-review.py` — lines 21-22 and 34 reference `synthesis-merge.py` and `wiki/synthesis.md` in docstring. Needs updating.
- `.claude/hooks/validate-commit-msg.py` — line 96 has the exclusion `p != "wiki/synthesis.md"` in the daemon-trigger detection. If `wiki/synthesis.md` no longer exists, this exclusion is harmless but stale; if a future hand-edit creates a file at that path it would now incorrectly trigger validation. Best practice: remove the special case.
- `.claude/hooks/block-push-without-approval.py` — lines 11, 118, 163 all exclude `wiki/synthesis.md` from daemon-triggering paths. The spec doesn't address this hook, but the exclusion logic is exactly the kind of thing that breaks subtly: now a push touching `synthesis/queue/*.md` should NOT trigger the daemon (because daemon doesn't fire on `synthesis/**`), so the hook needs explicit handling for the new directory layout.

**Non-daemon scripts the spec doesn't enumerate:**
- `scripts/eval-propagation.py` line 504 — same "do not edit wiki/synthesis.md (that is Pass 2's job)" prompt-text reference.
- `scripts/wiki-update.sh` lines 5 and 13 — references in usage examples.
- `scripts/deepseek-v4-assessment.md` lines 5, 162, 216 — `synthesis.md` listed in frontmatter `related:`, mentioned as training-data, mentioned as the "Brian still reads" surface.

**Skills the spec misses (only walk-synthesis is named):**
- `.claude/skills/sweep-status/SKILL.md` — line 3 (description) and line 54 references "synthesis.md prepend"; needs update.
- `.claude/skills/sweep-catchup/SKILL.md` — lines 21, 35, 50, 84-85, 102, 108 reference `wiki/synthesis.md` as the daemon-output target and as an exclusion. Needs comprehensive update.
- `.claude/skills/new-comp-experiment/SKILL.md` — line 170 staging-paths list. Needs update.

**User-facing docs the spec partially addresses:**
- `README.md` — lines 63 and 86 link to `wiki/synthesis.md`. Spec doesn't list README at all.
- `mkdocs.yml` — line 60 has `Platform Thesis & Synthesis: synthesis.md` in the nav. The published docs site will 404 if not updated. Spec doesn't address.
- `wiki/index.md` line 84 — "The [Synthesis Queue](synthesis.md)" link.

**Wiki cross-links — the largest category by far:** 27 wiki pages contain at least one `synthesis.md` link (e.g., `engineered-koji-protocol.md`, `computational-experiments.md`, `tcm-modern-rigor-intersection.md`, `chembl-cross-check.md`, `modality-chokepoint-matrix.md`, `chaperone-orthogonal-stacking.md`, `open-questions.md`, `validation-experiments.md`, etc.). Many cite specific items: e.g., `open-questions.md` line 76 cites "synthesis.md Connection 7"; `chaperone-orthogonal-stacking.md` line 215 anchors to "synthesis.md#strategic-reflections-queue". The spec's success criterion 11 ("no `wiki/synthesis.md` references remain anywhere") implies all 27 files need rewrites. That is substantial work and the spec doesn't acknowledge it.

**Why it matters.** Three failure modes:
- The daemon will fail in CI if `sweep-1-propagate.py` still lists `wiki/synthesis.md` in `READ_ONLY_GLOBS` and that path no longer exists (depends on how the glob lib treats missing paths).
- The published docs site (`mkdocs.yml`) will break.
- Success criterion 11 is unverifiable as stated. Either it's wrong, or §4 is wrong.

**Recommendation.** Restructure §4 into three sub-lists:
- **Hard-required updates** (daemon machinery): every file under `scripts/` and `.claude/hooks/` and `.claude/skills/` that mentions `synthesis.md` or `synthesis-merge`. Enumerate exhaustively via grep.
- **Cross-link rewrites in wiki pages**: define a policy. Options: (a) rewrite every link to point to `synthesis/` README or the appropriate done/queue file (heavy lift, brittle if items move); (b) leave the dangling links to be rewritten as the daemon naturally re-touches each page (incremental decay); (c) rewrite to a generic "synthesis queue index" pointer that's stable (recommended).
- **User-facing docs**: README, mkdocs.yml, wiki/index.md.

Then revise success criterion 11 to a verifiable form: "no `wiki/synthesis.md` references in scripts/, .claude/, README, mkdocs.yml, or top-level CLAUDE.md/index.md. Wiki cross-links: see migration policy."

### 2. §5.7 — Path-filter design does not protect against recursion

**What's wrong.** The spec claims `paths: '!synthesis/**'` will prevent the daemon from re-triggering when it writes to `synthesis/queue/` and `synthesis/history/`. This is incorrect for the way GitHub Actions `paths` filters work.

GitHub Actions `paths` filters operate on the SET of files changed in the push. A push triggers the workflow if AT LEAST ONE file matches the include patterns AND no file matches negation. Specifically, if a daemon commit touches `synthesis/queue/foo.md` only, the negation `'!synthesis/**'` excludes the only changed file, so the workflow won't fire — that part works.

But there's a subtlety: when a single push contains MULTIPLE commits (which is normal for the daemon — Pass 1 commits + Pass 2 commits + Pass 3 commits all push together OR sequential pushes overlap), the `paths` filter applies to the AGGREGATE set of files changed across all commits in the push. If Pass 1 propagates to `wiki/some-page.md` AND Pass 3 emits `synthesis/queue/foo.md`, the aggregate includes both — which means `wiki/**.md` matches and `'!synthesis/**'` doesn't override (negation only excludes if ALL changed files are under `synthesis/`).

The current `'!wiki/synthesis.md'` filter avoids this because Pass 1 commits and pushes BEFORE Pass 2 starts (separate pushes). Pass 3 commits + pushes alone, and ONLY touches `wiki/synthesis.md` — so the negation works for that single-file case. The new architecture has Pass 3 touching `synthesis/queue/*.md` + `synthesis/history/*.md` (multiple files, all under `synthesis/`), which would still work for the Pass-3-only push case. BUT: re-read the workflow — Pass 3 also writes `logs/sweep-state.json` (line 426 of wiki-sweep.yml). That file is NOT under `synthesis/`, so the aggregate Pass-3 commit-set includes `synthesis/queue/`, `synthesis/history/`, AND `logs/sweep-state.json`. The path filter is `wiki/**.md` (include) — `logs/sweep-state.json` doesn't match include OR negation, so the workflow doesn't fire on it. But this is fragile — anyone adding a `wiki/**.md` write to Pass 3 in the future will silently re-trigger the daemon.

**Why it matters.** The spec assumes path-filter recursion protection works. If the daemon ever writes to a wiki path during Pass 3 (or during a future enhancement), the daemon re-fires on its own output. The `[skip-wiki-sweep]` marker is the ONLY load-bearing protection.

**Recommendation.** Do one of:
- (Preferred) **Document that `[skip-wiki-sweep]` is the sole recursion guard** and that the path filter is best-effort. Update the `if:` condition on each job to be the canonical defense, and remove the path-filter negation entirely.
- Keep the path-filter negation but ADD an explicit invariant: "Pass 3 must only write to `synthesis/`, never to `wiki/`. Verified by a CI check on the daemon's diff."
- Reverse the polarity: change `paths` from `'wiki/**.md'` to `'wiki/**.md'` AND `'!synthesis/**'`, AND additionally add a job-level `if:` that checks the head commit message for `[skip-wiki-sweep]` (which is already there for Pass 1 — extend to all jobs).

### 3. §5.3 / §4.2 — Pass 2 item parsing is undefined

**What's wrong.** The spec says `synthesis-emit-files.py` "writes one file per Pass 2 item." But the current `synthesis-merge.py` doesn't parse items — it does mechanical `{{PEER-REVIEW}}` ↔ `<<<NEXT>>>` substitution within an opaque body. To emit one file per item, the new script must:

1. Parse the Pass 2 markdown to identify section headers (`## New Connections`, `## Contradictions Found`, `## Proposed Experiments`, `## Open Questions`, `## Priority Actions`, `## Riskiest Assumption`, `## Most Curious Thread`).
2. Within each section, identify numbered items (or single-paragraph blocks for Riskiest Assumption / Most Curious Thread).
3. Extract the headline (first sentence of bolded text? first H3? per-section heuristic?) for slug generation per §5.1.
4. Determine the boundaries between items (blank line + new number? `{{PEER-REVIEW}}` marker as separator?).
5. Map Pass 3 review blockquotes (which are `<<<NEXT>>>`-separated, in order) to the parsed items (which need to also be in order — and the mapping from `{{PEER-REVIEW}}` index to "(section, index_within_section)" matters).
6. Generate the slug — CRITICAL: §5.1 doesn't specify the slug-derivation function. What if two items in the same sweep produce identical slugs? What if a headline produces an empty slug (e.g., starts with a number, has only special characters)?

The Pass 2 log format (verified by reading `logs/v4-synthesis-2026-05-08-e842754.md`) is structured but inconsistent across runs — the synthesizer's bolded headlines are sometimes one sentence, sometimes a multi-clause sentence, and the Riskiest Assumption / Most Curious Thread sections use single paragraphs without a bolded headline.

**Why it matters.** The script's parser is the load-bearing piece of the migration. The spec leaves it undefined. The "local test against today's Pass 2 log" mitigation (§7) tests against ONE example — it can't validate the parser against future Pass 2 outputs that may use slightly different formatting (the synthesizer is a stochastic LLM; output structure varies).

**Recommendation.** Add a §5.X "Parser specification" subsection covering:
- Section-header recognition (exact regex: `^## (New Connections|Contradictions Found|Proposed Experiments|Open Questions|Priority Actions|Riskiest Assumption|Most Curious Thread)$`).
- Item-boundary detection within numbered sections (anchored on `{{PEER-REVIEW}}` marker as the canonical "end of item" — already a hard contract per the Pass 2 prompt).
- Headline extraction (first bolded run between item-number `N. **...**` and the next bolded marker / period — defensive fallback if not found).
- Slug derivation (kebab-case, ASCII-only, max length 60 chars, dedupe collisions by appending `-2`, `-3`).
- Failure modes: what happens if marker count doesn't match section-item count, if a section is missing, if a headline can't be extracted, if a slug collides on disk. Spec should mandate fail-fast behavior with clear error messages — same as `synthesis-merge.py`'s existing fail-fast on marker mismatch.
- Map from Pass 2 marker-index → emitted file: define explicitly so Pass 3 review mapping is deterministic.

### 4. Cross-link policy not defined

**What's wrong.** Many wiki pages cite specific synthesis.md items by anchor: e.g., "synthesis.md Connection 7", "synthesis.md Contradiction 2", "synthesis.md#strategic-reflections-queue", "synthesis.md 2026-05-08 Item 9". These anchors point INTO the file's structured contents. After migration, those contents live at different paths (`synthesis/done/2026-05-08-connection-foo.md`, `synthesis/strategic-reflections/...`). The links break.

The spec acknowledges this implicitly in §10's non-changes ("subagent brief hygiene discipline UNCHANGED") but doesn't address the cross-link rewrites.

**Why it matters.** 27 wiki files have these links. The walk-synthesis discipline depends on annotating items at known anchors. After migration, "synthesis.md Item N" is a dead anchor. Subsequent walkthroughs will lose context about WHICH historical item is being referenced.

**Recommendation.** Define a cross-link policy explicitly in §5 (new subsection). Three options to consider:
- **Frozen-as-historical:** existing links to `synthesis.md` get rewritten to point to `synthesis/history/_pre-2026-05-08-archive.md` with a note "as of pre-migration; this is historical, not actionable." Simple, brittle for navigation.
- **Per-item rewrite:** every `synthesis.md Connection 7` style link gets rewritten to its new home. High effort; needs careful mapping; many of the cited items have already been actioned and live in canonical wiki pages anyway, so they could just lose the synthesis.md cite.
- **Drop the citation:** since items have been actioned and content lives canonically in the linked wiki page, the synthesis.md "provenance breadcrumb" is no longer load-bearing. Rewrite as a `synthesis/` directory pointer or just drop the breadcrumb.

Recommend option 3 for already-actioned items + option 1 for the few still-active cross-references. Should be enumerated in the spec, not improvised at implementation time.

## Important findings (should address before implementation)

### 5. §6 success criteria — several are not testable as written

- Criterion 5: "Local test produces one file in synthesis/queue/ per Pass 2 item, named per §5.1 convention." Per Finding 3, §5.1 doesn't fully specify slug generation, so "per §5.1 convention" is under-specified — the test will pass for any reasonable interpretation.
- Criterion 11: "No `wiki/synthesis.md` references remain anywhere (grep across entire repo returns zero results other than historical commits / archive files)." Per Finding 1 and 4, this is currently unachievable without explicit cross-link rewrite policy.
- Criterion 12: "Daemon CI runs successfully when `walk-synthesis-2026-05-08` merges to main." This is post-merge validation and the spec acknowledges "not gated by spec compliance" — but what's the rollback plan if the first daemon run fails on the new format? Add: "If the post-merge daemon run fails, the rollback path is to revert the migration commit and restore `wiki/synthesis.md` from the previous commit; the daemon will then fall back to the old script. Document this in §8."

### 6. §5.5 Strategic Reflections semantics — _resolved/ pattern is half-built

The spec creates `synthesis/strategic-reflections/` with 3 files but mentions a `_resolved/` subdirectory that's "not created in this migration since no reflections are resolved yet." That's fine but: the spec should specify the resolution criteria (what triggers a move to `_resolved/`?) and the file format (preserve the original Trigger / Outcome columns? add a "resolved on" timestamp?). Otherwise the first reflection-resolution will need a sub-spec.

Recommendation: add a one-line note in §5.5: "Resolution criteria: when the trigger condition fires AND the user-decided outcome is documented, the file moves to `_resolved/` with a frontmatter field `resolved_date: YYYY-MM-DD` and an appended section `## Resolution outcome` capturing what was decided."

### 7. §5.4 history file content — sweep-state.json integration unclear

The history file pointer to "the Pass 2 log file (`logs/v4-synthesis-*.md`)" overlaps with the sweep-state.json registry's `last_successful_sweep.synthesis_log` field. Question: is `synthesis/history/<sweep>.md` redundant with the registry, or does it carry information the registry doesn't? If redundant, why have both? If complementary, the spec should say what each contains.

Recommendation: clarify that `synthesis/history/` is human-browsable narrative (one file per sweep, ~20-50 lines) while sweep-state.json is machine-readable cursor (single file, current state only). They're complementary.

### 8. §7 risk on script-test-against-real-Pass-2-log is insufficient

Per Finding 3, the new script's parser is the load-bearing piece. Testing against ONE Pass 2 log (today's `logs/v4-synthesis-2026-05-08-e842754.md`) doesn't exercise format variation. Recommendation: test against the 3-5 most recent Pass 2 logs spanning different synthesizer models (DeepSeek V4-Pro, Gemini 2.5 Pro, possibly an Opus log if any exist) to catch synthesizer-specific format drift. The repo has many `logs/v4-synthesis-*.md` files; pick 3-5 across different models.

### 9. §8 migration ordering — step 8h leaves the repo broken if step 8i fails

Step 8h deletes `wiki/synthesis.md`. Step 8i greps for remaining references and cleans them up. If 8i fails partway through (e.g., human pause, accidental commit, network issue) the repo is in a state where the file is gone but cross-links still point to it. Better ordering: do the comprehensive cross-link cleanup BEFORE deletion, then delete as the final atomic step.

Also: step 8e updates the workflow + sweep-state.py BEFORE step 8d updates the prompts. If a daemon push happens in this window (e.g., another contributor pushes a wiki edit), the daemon runs with new workflow + old prompts pointing at `wiki/synthesis.md` — which doesn't exist yet because deletion is step 8h. Either work on a feature branch (which the spec does mention via "walk-synthesis-2026-05-08" branch) and merge atomically, OR re-order: prompts first, then script, then workflow, then deletion. Recommendation: do the entire migration on the feature branch and merge in a single PR (already implied — make it explicit in §8).

### 10. Risk table — missing risks

Several risks are not in the §7 table:
- **Cross-link breakage in 27 wiki pages** — no entry. (Per Finding 4.)
- **Published docs site (mkdocs) breaks** — no entry. (Per Finding 1.)
- **Pass 2 log format drift across synthesizer models** — no entry. (Per Finding 8.)
- **`scripts/sweep-1-propagate.py` READ_ONLY_GLOBS pointing at non-existent file** — no entry. (Per Finding 1.) Behavior depends on glob library; could be silent no-op or runtime error.
- **Walk-synthesis skill update interacts with the existing Step F discipline** — Section 2 Step C-E is a tight integration; the new closure flow (`git mv`) is structurally simpler, but Step F's "loose ends" inventory and "carryover to Item X" anchoring need explicit re-grounding in the per-file model. The spec says "Section 2 Step C-E" but Step F was added 2026-05-08 and is now load-bearing — needs explicit treatment.

### 11. README for synthesis/ directory — content not specified

§5.6 says "synthesis/README.md explains the directory structure, daemon flow, walkthrough flow, file naming." That's a one-liner; the README should be specified concretely (or at least: list the headings the README must contain). Otherwise different implementers will produce different READMEs.

Recommendation: spec the README's required sections: (a) what each subdirectory contains; (b) file-naming convention reference (point at §5.1); (c) daemon-write vs human-write boundary; (d) closure flow (queue → done via `git mv`); (e) Strategic Reflections semantics (human-curated); (f) historical pointer to `_pre-2026-05-08-archive.md`; (g) link to the spec for full context.

## Minor findings / nits

### 12. §5.1 — type names

`openquestion` and `priorityaction` (single words) feel ugly. Hyphenated `open-question` and `priority-action` would be more readable in filenames. Same for `riskiest-assumption` and `most-curious-thread` (already hyphenated in §5.2). Make the convention consistent.

Recommendation: use hyphenated forms across the board: `open-question`, `priority-action`, `riskiest-assumption`, `most-curious-thread`, `connection`, `contradiction`, `experiment`.

### 13. §5.6 README files — synthesis/strategic-reflections/ semantics

Per open-question 3 (§9), "Should the Strategic Reflections Queue have its own README?" My recommendation: yes. The semantics are sufficiently different from queue/done (human-curated, content-triggered, not actioned by walkthrough) that a 10-20 line README in `synthesis/strategic-reflections/` would prevent future confusion.

### 14. §3 — out-of-scope for "Migrating today's 28 actioned items as separate `synthesis/done/` entries"

This is right (the items are already in canonical wiki pages), but the spec should explicitly state what happens to historical Pass 2/Pass 3 cross-references that pointed at items now NOT in synthesis/done/. Per Finding 4, this is the cross-link policy issue.

### 15. §5.2 Riskiest Assumption / Most Curious Thread — dedup logic

The spec keeps these in the synthesizer prompt but emits them as separate-typed files. If they continue to be quasi-duplicates of other items in the same sweep, walkthroughs will continue to need manual de-dup. The spec mentions "future spec can drop them from the prompt" — but the migration is a good moment to also propose: emit the file but flag it visibly as "may overlap with item N" (extracted from the Pass 3 review's OVERLAP tag). Cheap, defensive.

### 16. §5.1 — "sweep-date" is ambiguous

Is `<sweep-date>` the date of the trigger commit, the date the synthesizer ran, the date the Pass 3 review committed, or the calendar date the file was emitted? In the daemon flow these are usually the same day but not guaranteed (Pass 1 fires near midnight, Pass 3 finishes after midnight). Recommendation: use the date of the workflow_run's `event.head_commit` timestamp in UTC, ISO format (YYYY-MM-DD). Specify in §5.1.

### 17. §3 — drift between out-of-scope and §4 scope

§3 says "Changing the walk-synthesis skill's per-item discipline (Steps A-F)" is out of scope. §4 says walk-synthesis SKILL.md gets a "major update." These are consistent (I/O format changes; discipline doesn't), but a reader could be confused. Tighten the §3 wording: "Changing the SUBSTANCE of the skill's per-item discipline (the rules in Steps A-F) — only the I/O format changes."

### 18. The spec's own status block

The spec's frontmatter says `status: draft (pending independent peer review before implementation)` and the bottom says "draft, awaiting independent peer review." After this review lands, update both to `status: review-complete (awaiting revision pass before implementation)` or similar.

## Engagement with §9 open questions

### Q1. Is the file-naming convention §5.1 right?

**Recommendation: §5.1 is mostly right, but specify slug-derivation explicitly and add `<index>` for collision robustness.**

`<sweep-date>-<type>-<slug>.md` is human-readable and sorts naturally. The alternative `<sha>-<index>-<slug>.md` loses the date-sort property. Rejecting it is correct.

But: two items in the same sweep with similar headlines could collide on slug. Cheap fix: include `<index>` after `<type>`: `<sweep-date>-<type>-<index>-<slug>.md`, where `<index>` is the Pass 2 item's number within its section (1, 2, 3...). The sort is still date-first, type-second; the index is a tiebreaker. Slug-collision becomes impossible because `<index>` is unique within a (sweep-date, type) tuple.

Example: `synthesis/queue/2026-05-09-connection-1-rosmarinic-acid-c3-convertase.md`.

### Q2. Should `synthesis/done/` items eventually rotate out?

**Recommendation: yes, but defer per spec. Add a §5.X subsection naming the rotation rule, but don't implement it.**

YAGNI is right here. But specify the rule in advance so the future spec is short:
- Rule: after 12 months, items move to `synthesis/done/_archive/<year>/`.
- Trigger: a quarterly cron (or manual `scripts/synthesis-archive.py` invocation).
- Preservation: full content stays git-tracked; only the path changes.

Pre-specifying lets the migration's directory structure anticipate the eventual archive without paying for it now.

### Q3. Should the Strategic Reflections Queue have its own README?

**Recommendation: yes, as a 10-20 line file in `synthesis/strategic-reflections/`.**

Per Finding 13. The semantics differ enough from queue/done (human-curated; content-triggered, not walkthrough-triggered; no closure on a per-walkthrough basis) that conflating them in `synthesis/README.md` makes both READMEs less clear. Cheap to add; high-clarity payoff for future contributors.

### Q4. Should `scripts/SWEEP-ARCHITECTURE.md` be updated as part of this spec, or as a separate documentation pass?

**Recommendation: as part of this spec. SWEEP-ARCHITECTURE.md is the load-bearing reference doc.**

Splitting it into a separate doc-pass PR creates a window where SWEEP-ARCHITECTURE.md is stale relative to the implemented architecture — exactly the failure mode the multi-pass daemon is supposed to prevent. The doc update is small (~50-100 lines of edits to the existing doc, primarily to §"Inter-pass artifact handoff" and §"Architecture (5 components)" subsections). Bundle it in.

## What's good

- **§2 motivation is solid.** The three reasons (separation of concerns, per-item granularity, auto-inbox-zero) are concrete and grounded in observed pain. Per-file items eliminating merge conflicts on synthesis.md is a real, observed benefit.
- **§5.5 strategic-reflections semantics — human-only writes, daemon-doesn't-touch — is the right call.** Mixing daemon-emitted items and human-curated reflections in the same directory would compound the problem the migration aims to solve.
- **§3 out-of-scope list is disciplined.** The spec resists the temptation to also rebuild the synthesizer's prompt structure or the Pass 3 verdict vocabulary. Migrating I/O without changing the daemon's substance is the right scoping.
- **§5.3 "always emit a file regardless of verdict" is the right call.** Auto-deleting RESTATEMENT items at Pass 3 would hide information that the walkthrough discipline depends on (the human reviewer needs to see "Pass 3 said this was a restatement" to make the closure decision).
- **§7 already calls out the YAML-syntax-validation step.** Running yamllint locally before committing is the right defensive move.
- **§8 step ordering with the "spec review BEFORE implementation" gate.** The discipline is correct (peer review on spec, then peer review on code-against-spec) — a 2-stage review pattern that's harder to game than a single end-of-implementation review.
- **The decision to bundle with PR #4 is sensible.** Atomic merge means the daemon's first post-merge run uses the new architecture, no transition window with mixed state.

## Files I read for this review

- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/operations/specs/2026-05-08-synthesis-filesystem-migration.md` — the spec under review.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/SWEEP-ARCHITECTURE.md` — current daemon architecture doc; grounding for what changes.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/synthesis-merge.py` — the script being replaced; key for understanding what `synthesis-emit-files.py` must replicate.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/sweep-prompt-2-synthesize.md` — Pass 2 prompt; revealed the seven-section output structure the new parser must handle.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/sweep-prompt-3-review.md` and `scripts/sweep-prompt-3-review-gpt55.md` — Pass 3 prompts; both must be updated.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/sweep-state.py` — confirmed the line-153 reference and the `cmd_pending_paths` filter; revealed the registry/history overlap (Finding 7).
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/.github/workflows/wiki-sweep.yml` — workflow file; revealed the path-filter design issue (Finding 2) and the multi-step Pass 3 commit pattern (synthesis.md + sweep-state.json) that complicates the negation logic.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/.claude/skills/walk-synthesis/SKILL.md` — skill being updated; revealed Step F's loose-ends discipline that needs explicit re-grounding (Finding 10).
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/wiki/synthesis.md` — file being deleted; verified the 3 strategic reflections + sweep history table; verified the "Where actioned items live now" content as historical anchor for cross-link rewrites.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/CLAUDE.md` — project conventions; confirmed where document-structure references need updating.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/sweep-1-propagate.py` (lines 50, 524-528, 598) — found undocumented `wiki/synthesis.md` references in READ_ONLY_GLOBS and in the propagation prompt.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/synthesize.py` (line 419-420) — found undocumented exclusion in `cited_files` parsing.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/sweep-3-review.py` (lines 21-22, 34) — docstring references.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/eval-propagation.py` (line 504) — propagation prompt reference.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/wiki-update.sh` (lines 5, 13) — usage doc references.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/.claude/hooks/validate-commit-msg.py` (line 96) — daemon-trigger detection has the special-case exclusion.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/.claude/hooks/block-push-without-approval.py` (lines 11, 118, 163) — push-block hook has multiple `synthesis.md` references.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/.claude/skills/sweep-status/SKILL.md` and `sweep-catchup/SKILL.md` and `new-comp-experiment/SKILL.md` — all reference `wiki/synthesis.md`; spec only names walk-synthesis.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/fresh-synthesis.py` — extensive `wiki/synthesis.md` references in prompt and helper text.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/mkdocs.yml` (line 60) — published docs nav.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/README.md` (lines 63, 86) — top-level README.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/wiki/index.md` (line 84) — wiki landing page.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/deepseek-v4-assessment.md` (lines 5, 162, 216) — assessment doc references.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/operations/comp-018-vs-comp-020-retrospective.md` — referenced in the spec; sister operations doc; confirmed style and granularity expectations.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/logs/v4-synthesis-2026-05-08-e842754.md` — current Pass 2 log; verified output format the new parser must handle.
- `grep -rln "synthesis\.md" wiki/` — 27 wiki pages contain references; basis for Finding 4 cross-link policy critique.
