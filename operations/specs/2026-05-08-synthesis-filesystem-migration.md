---
title: "Synthesis Filesystem Migration Spec"
date: 2026-05-08
status: revised post-spec-rereview (pending Sonnet third-pass before implementation)
authors: brian + claude
reviewers: claude opus 4.7 (first + second pass, see §11) → claude sonnet 4.6 (third pass, pending)
related:
  - 2026-05-08-synthesis-filesystem-migration-spec-review.md
  - ../../scripts/SWEEP-ARCHITECTURE.md
  - ../../scripts/sweep-prompt-2-synthesize.md
  - ../../scripts/synthesis-merge.py
  - ../../.github/workflows/wiki-sweep.yml
  - ../../.claude/skills/walk-synthesis/SKILL.md
  - ../comp-018-vs-comp-020-retrospective.md
---

# Synthesis Filesystem Migration Spec

## 1. Goal

Replace the single growing `wiki/synthesis.md` action queue with a filesystem-based per-item structure under a top-level `synthesis/` directory (sibling to `wiki/`, NOT inside it). The wiki sweep daemon's output, the walk-synthesis skill's input/output, and all internal references migrate together in one PR (bundled with the existing `walk-synthesis-2026-05-08` branch / PR #4) so that the next post-merge daemon run uses the new format from the start.

## 2. Why

Three reasons:

1. **Separation of concerns.** `wiki/` is research findings (science). The synthesis queue is project-management — what items the daemon proposed, which got actioned, what's pending. These are categorically different content classes; mixing them was a path-of-least-resistance choice that's grown awkward as synthesis.md hit 500+ lines of pending work mid-walkthrough. Putting synthesis/ outside wiki/ makes the boundary explicit.

2. **Per-item granularity.** A single growing file forces every item-level annotation into surgical Markdown edits to a shared file (with merge conflicts when subagents and humans both edit it concurrently — exactly what happened in today's walkthrough). Per-file items eliminate that conflict class entirely. Each item is a standalone unit: easy to read, link, blame, grep, mv.

3. **Auto-inbox-zero.** Currently inbox-zero is a manual end-of-walkthrough pass that surgically deletes actioned content. With per-file items, inbox-zero is automatic: walkthrough closes an item by appending closure annotation + `git mv`-ing to `synthesis/done/`. Empty queue/ directory = inbox zero, by construction.

Plus a smaller benefit: files persist forever in git as text. Full provenance, durable, works offline, doesn't depend on GitHub Issues' database.

## 3. Out of scope / non-goals

This spec deliberately does NOT address:

- **Migrating today's 28 actioned items as separate `synthesis/done/<file>.md` entries.** Today's items are already in canonical wiki pages per the "Where actioned items live now" section of synthesis.md. Their audit trail is in commits `ba981ee..156dfe1` on `walk-synthesis-2026-05-08`. The done/ directory starts empty.
- **Changing daemon Pass 1 (propagate) behavior.** Pass 1 still propagates findings between wiki pages. Only Pass 2 / Pass 3 / synthesis-merge change.
- **Changing the synthesizer's output structure.** Pass 2 still produces Connections / Contradictions / Proposed Experiments / Open Questions / Priority Actions. The CHANGE is how that output is written to disk after Pass 3 review (per-file vs prepend-to-synthesis.md), not WHAT is written.
- **Changing Pass 3 verdict vocabulary.** Verdicts stay: Confirmed / Confirmed-prioritize / Augment / Partial / Push back / Restatement / etc.
- **Changing the SUBSTANCE of the walk-synthesis skill's per-item discipline (the rules in Steps A-F).** Only the I/O format changes: the skill reads from `synthesis/queue/` instead of synthesis.md, and closure is `git mv` to `synthesis/done/` instead of synthesis.md surgical edit. Step F's loose-ends inventory and "carryover to Item X" anchoring are preserved with explicit re-grounding in the per-file model (see §4.5).
- **Building a `fresh-stack.py` script** (Strategic Reflections Queue entry — separate future work).
- **Auto-pruning duplicates at Pass 2 generation time** (mentioned as future possibility in earlier conversation; not part of this migration).

## 4. Concrete scope

### 4.1 New directory + files

```
synthesis/
├── README.md                                       ← explains the structure (§5.8 specifies content)
├── queue/
│   └── .gitkeep                                    ← empty initial state
├── done/
│   └── .gitkeep                                    ← empty initial state
├── strategic-reflections/
│   ├── README.md                                   ← human-curated semantics (§5.8)
│   ├── platform-framing-reframe.md                 ← migrated from wiki/synthesis.md
│   ├── chaperone-framework-validation.md           ← migrated from wiki/synthesis.md
│   └── application-layer-surface-architecture.md   ← migrated from wiki/synthesis.md
└── history/
    └── _pre-2026-05-08-archive.md                  ← archived sweep history table from wiki/synthesis.md
```

### 4.2 New scripts

- **`scripts/synthesis-emit-files.py`** — REPLACES `synthesis-merge.py`. Same inputs (Pass 2 log + Pass 3 review output), but emits per-file output to `synthesis/queue/` plus a sweep-header file to `synthesis/history/`. Parser specification at §5.4.

### 4.3 Hard-required updates — daemon machinery (exhaustive)

Every file in this list contains a `wiki/synthesis.md` or `synthesis-merge` reference that must be updated. Discovered via `grep -rn "synthesis\.md\|synthesis-merge" .github/ scripts/ .claude/`.

**`.github/` and `scripts/`:**
- `.github/workflows/wiki-sweep.yml` — three changes:
  - Path filter: remove `'!wiki/synthesis.md'`. **Recursion protection moves to the `[skip-wiki-sweep]` commit-msg marker** (per §5.9 redesign). Path filter stays at `wiki/**.md` (unchanged include pattern).
  - Pass 3 step: replace `python3 scripts/synthesis-merge.py` invocation with `python3 scripts/synthesis-emit-files.py`. Update commit message + commit-paths from `wiki/synthesis.md` to `synthesis/queue/` + `synthesis/history/`. Pass 3 commit message must include `[skip-wiki-sweep]` (already required for the marker discipline).
  - Step name / comments: update prose references from "interleaved into wiki/synthesis.md" to "emitted to synthesis/queue/."
- `scripts/sweep-prompt-2-synthesize.md` — update §"Useful context (read but do not let it filter your output)" references: `wiki/synthesis.md` bottom-of-file → `synthesis/history/`, `synthesis/done/`, `synthesis/strategic-reflections/`.
- `scripts/sweep-prompt-3-review.md` + `scripts/sweep-prompt-3-review-gpt55.md` — same reference updates as Pass 2 prompt.
- `scripts/sweep-prompt-1-propagate.md` — review for any `synthesis.md` references in prompt body; update if found.
- `scripts/sweep-1-propagate.py` — line 50 `READ_ONLY_GLOBS` lists `wiki/synthesis.md`; remove. Lines 524, 528 mention it in propagation prompt context; update. Line 598 excludes it from `propagated_files`; remove (file no longer exists).
- `scripts/synthesize.py` — line 419-420 explicitly excludes `wiki/synthesis.md` from `cited_files`; replace with `synthesis/**` exclusion.
- `scripts/sweep-3-review.py` — lines 21-22 + 34 docstring references `synthesis-merge.py` and `wiki/synthesis.md`; update to reference `synthesis-emit-files.py` and the new output paths.
- `scripts/sweep-state.py` — line 153 `wiki/synthesis.md` filter in `cmd_pending_paths`; replace with `synthesis/**` filter.
- `scripts/synthesis-merge.py` — DELETE (replaced by `synthesis-emit-files.py`).
- `scripts/eval-propagation.py` — line 504 prompt-text reference; update.
- `scripts/wiki-update.sh` — lines 5 + 13 usage examples; update.
- `scripts/deepseek-v4-assessment.md` — lines 5 (frontmatter `related:`), 162, 216 (training-data + "Brian still reads" surface); update.
- `scripts/fresh-synthesis.py` — extensive `wiki/synthesis.md` references in prompt and helper text; update to read from `synthesis/queue/` + `synthesis/done/` + `synthesis/strategic-reflections/` + `synthesis/history/`.
- `scripts/SWEEP-ARCHITECTURE.md` — comprehensive update to reflect the new architecture (§"Inter-pass artifact handoff", §"Architecture (5 components)" subsections; ~50-100 lines of edits).

**`.claude/hooks/`:**
- `.claude/hooks/validate-commit-msg.py` — line 96 has the special-case exclusion `p != "wiki/synthesis.md"` in daemon-trigger detection. Remove the special case (file no longer exists).
- `.claude/hooks/block-push-without-approval.py` — lines 11, 118, 163 exclude `wiki/synthesis.md` from daemon-triggering paths. Update logic: a push touching `synthesis/queue/*.md` or `synthesis/history/*.md` should NOT trigger the daemon (because daemon doesn't fire on `synthesis/**`). The hook's daemon-detection logic needs to be updated to reflect the new architecture.

**Parallel workflows that write to `wiki/synthesis.md` (added per spec re-review N1):**
- `scripts/chembl-refresh-prompt.md` — separate quarterly workflow (NOT the wiki-sweep daemon) that prepends to `wiki/synthesis.md` from its Pass 4. 7 references at lines 18, 23, 26, 82, 84, 127, 141, 142. Post-migration this workflow would either fail with file-not-found OR silently re-create the deleted file, putting the repo in mixed state. **Decision (per spec re-review N1, option 2 — direct write):** chembl-refresh's Pass 4 changes from "prepend to `wiki/synthesis.md`" to "write `synthesis/queue/<date>-chembl-discrepancy-N.md` files directly," one per discrepancy finding. Does NOT go through `synthesis-emit-files.py` (its findings are flat-list, not the daemon's structured 7-section format). Walkthrough flow handles the resulting queue/ files identically (read queue/, action, mv to done/) — they're just produced by a different upstream. The new `<type>` value `chembl-discrepancy` is added to §5.1's enumeration. The chembl-refresh prompt's `[skip-wiki-sweep]` rationale (line 127, "prevents wiki-sweep from firing on the chembl-refresh's synthesis.md edit") needs updating: post-migration, chembl-refresh writes to `synthesis/**` which the daemon path-filter doesn't trigger on AND `[skip-wiki-sweep]` marker still applies as belt-and-suspenders per §5.9.

**`.claude/skills/`:**
- `.claude/skills/walk-synthesis/SKILL.md` — major update. Section 1 (Pre-flight): inventory becomes `ls synthesis/queue/` instead of "read synthesis.md end-to-end." Section 2 Step C (Action it) + Step D (Annotate `✓ Actioned`) + Step E (Commit immediately): closure flow becomes append-closure-annotation-to-file + `git mv synthesis/queue/<file>.md synthesis/done/`. Section 2 Step F (end-of-item summary): explicit re-grounding in the per-file model — "loose ends" inventory still applies; "carryover to Item X" anchoring becomes explicit cross-references between queue files. Section 7 (End-of-walkthrough): inbox-zero is automatic (empty queue/ = inbox zero); no surgical synthesis.md edit. Section 6 templates (actioned annotation, end-of-item summary): updated for per-file format. Section 9 anti-patterns: add #15 "don't try to edit `wiki/synthesis.md` (it doesn't exist anymore)."
- `.claude/skills/sweep-status/SKILL.md` — line 3 (description) and line 54 references "synthesis.md prepend"; update to reference `synthesis/queue/` + `synthesis/history/` outputs.
- `.claude/skills/sweep-catchup/SKILL.md` — lines 21, 35, 50, 84-85, 102, 108 reference `wiki/synthesis.md` as daemon-output target and as exclusion. Comprehensive update for new architecture.
- `.claude/skills/new-comp-experiment/SKILL.md` — line 170 staging-paths list. Update.

### 4.4 Cross-link rewrites in wiki pages — policy + scope

**Policy (per §5.5):** the cross-link policy is **drop-or-stub**, not per-item-rewrite.

- Most `synthesis.md`-cite-by-anchor links (e.g., "synthesis.md Connection 7", "synthesis.md Item 9") cite items that have already been actioned. Their content lives in canonical wiki pages already. The synthesis.md "provenance breadcrumb" is no longer load-bearing; **drop the breadcrumb**, leaving the substantive content in the canonical wiki page.
- Links to `synthesis.md`-as-a-whole or to `#strategic-reflections-queue`, `#sweep-history`, `#where-actioned-items-live-now` are rewritten to point at `synthesis/strategic-reflections/`, `synthesis/history/_pre-2026-05-08-archive.md`, or `synthesis/README.md` respectively.
- Old anchor cites that point at NO longer recoverable content (e.g., "synthesis.md 2026-04-21 Open Question 3") are dropped silently.

**Scope:** the 27 wiki pages with `synthesis.md` references identified by the spec reviewer's grep. Discovered via:

```bash
grep -rln "synthesis\.md" wiki/
```

Files (verified by reviewer):
- `wiki/index.md` line 84 — "[Synthesis Queue](synthesis.md)" link → rewrite to `synthesis/README.md`
- 26+ other wiki pages cited in the spec review's Finding 1 — each gets a per-file pass during implementation (mostly drop-the-breadcrumb).

The implementation step for cross-link rewrites is §8 step before deletion, not after, so the repo is never in a state where the file is deleted but cross-links still point to it.

### 4.5 User-facing docs

Enumerated per spec re-review N2 — each line location explicitly named:

- **`README.md`** (top-level) — lines 63 + 86 link to `wiki/synthesis.md`. Rewrite both to `synthesis/README.md`.
- **`mkdocs.yml`** — line 60 has `Platform Thesis & Synthesis: synthesis.md` in the nav. Rewrite to `synthesis/README.md` so the published docs site doesn't 404.
- **`wiki/index.md`** line 84 — "[Synthesis Queue](synthesis.md)" link → rewrite to `synthesis/README.md`.
- **`CLAUDE.md`** (`Open Enzyme/CLAUDE.md`) — three references:
  - Line 27 §"Document Structure" — `wiki/synthesis.md` mention. Update.
  - Line 130 §"Workflow for Updates" — reference if present. Update.
  - Line 247 §"Version Control & Maintenance" — "Action queue: wiki/synthesis.md" line. Update.
- **`index.md`** (repo root) — three references:
  - Line 15 — "Derivation in [wiki/synthesis.md]" pointer. Update.
  - Line 21 — "Synthesis queue" pointer. Rewrite to `synthesis/queue/`.
  - Line 176 — "Synthesis (current)" link in concept index. Update.

### 4.6 Files deleted

- `wiki/synthesis.md` — DELETED. Content already in canonical wiki pages (per "Where actioned items live now"). 3 strategic reflections + sweep history are migrated to synthesis/strategic-reflections/ and synthesis/history/_pre-2026-05-08-archive.md respectively.
- `scripts/synthesis-merge.py` — DELETED (replaced by synthesis-emit-files.py).

### 4.7 Files unchanged

- All `wiki/*.md` content pages (the canonical research) other than the cross-link rewrites in §4.4.
- `scripts/synthesize.py` core flow (Pass 2 driver still writes to `logs/`; only the line 419-420 reference is updated).
- `scripts/sweep-3-review.py` core flow (only docstring updates).

## 5. Design decisions

These are choices the peer reviewer can challenge. (Reviewer engaged with these in §11 review history; current values reflect post-review revisions.)

### 5.1 File naming convention for queue/ and done/ items

Format: `<sweep-date>-<type>-<index>-<slug>.md`

- `<sweep-date>`: ISO date in UTC of the workflow_run's `event.head_commit` timestamp (date the trigger commit landed, not the date the daemon eventually ran). Format `YYYY-MM-DD`.
- `<type>`: one of `connection`, `contradiction`, `experiment`, `open-question`, `priority-action`, `riskiest-assumption`, `most-curious-thread`, **`chembl-discrepancy`** (added per spec re-review N1 — produced by chembl-refresh-prompt.md direct-write, not by `synthesis-emit-files.py`). **Hyphenated** for readability.
- `<index>`: the Pass 2 item's number within its section (1, 2, 3...). Tiebreaker for slug collisions; guaranteed unique within a `(sweep-date, type)` tuple.
- `<slug>`: kebab-case ASCII slug derived from the synthesizer's headline. Max length 60 chars. Generated by:
  - Take the bolded headline of the Pass 2 item (per §5.4 parser).
  - Lowercase. Strip non-ASCII. Replace runs of non-alphanumerics with single hyphens. Trim leading/trailing hyphens. Truncate to 60 chars at a word boundary.
  - If empty/invalid, fall back to `unnamed`.
  - Slugs CAN be non-unique since `<index>` is the actual disambiguator.

Example: `synthesis/queue/2026-05-09-connection-1-rosmarinic-acid-c3-convertase-mining.md`

### 5.2 Riskiest Assumption / Most Curious Thread

The Pass 2 prompt currently asks for these as separate single-paragraph output sections. Today's walkthrough showed they were **always quasi-duplicates of other items** in the same sweep (Item 11 ↔ Item 8; Item 12 ↔ Items 1+7).

**Decision:** keep them in the synthesizer's prompt for now (out-of-scope to change synthesizer behavior), but emit them as files of type `riskiest-assumption` and `most-curious-thread` respectively.

**Defensive de-dup:** when Pass 3's review tags an `[OVERLAP: RESTATEMENT]` or `[DUPLICATE-OF-N]` marker in the review of a Riskiest Assumption / Most Curious Thread item, the emitted file's frontmatter includes `overlap_with: <other-item-slug>` so the walkthrough can see "this is flagged as overlapping with X" without having to re-read the verdict.

If they continue to be duplicates, a future spec can drop them from the prompt.

### 5.3 Pass 3 verdict-driven file lifecycle

Pass 3 verdicts vocabulary: Confirmed / Confirmed-prioritize / Augment / Partial / Push back / Restatement / Push-back-restatement / [other tags].

**Decision:** the `synthesis-emit-files.py` script writes one file per Pass 2 item, regardless of Pass 3 verdict. Pass 3's review blockquote is appended to the file (same content as today, just attached to the file rather than interleaved into synthesis.md). The walk-synthesis discipline reads the verdict and decides closure path (closure note for restatement; substantive action for confirmed/prioritize; etc.).

**Why:** auto-deleting items at Pass 3 (e.g., on RESTATEMENT) hides information. The walkthrough should see Pass 3 said "this is a restatement" and explicitly close it, not have items silently disappear. Future spec can add auto-prune as a separate pass if the manual closure-of-restatements becomes high-volume.

### 5.4 Pass 2 parser specification

The new `synthesis-emit-files.py` script must parse the Pass 2 log to extract individual items. Spec:

**Input:** the Pass 2 log file (`logs/v4-synthesis-<date>-<sha>.md`) and the Pass 3 review file (a sequence of blockquotes separated by `<<<NEXT>>>`).

**Section recognition:** match section headers via regex anchored at line-start:
```
^## (New Connections|Contradictions Found|Proposed Experiments( \(.*\))?|Open Questions|Priority Actions|Riskiest Assumption|Most Curious Thread)$
```
The `Proposed Experiments` regex tolerates the optional `(ranked by insight per cost)` suffix the synthesizer sometimes includes.

**Item-boundary detection:**
- For numbered sections (Connections / Contradictions / Experiments / Open Questions / Priority Actions): items start with `^N\. \*\*` (numbered Markdown bold). Items end at the `{{PEER-REVIEW}}` marker. The marker is a hard contract per the Pass 2 prompt — every numbered item has exactly one marker.
- For Riskiest Assumption / Most Curious Thread (single-paragraph sections): the entire section between header and `{{PEER-REVIEW}}` is one item.

**Headline extraction:**
- Numbered items: the bolded run between `N. **` and the closing `**` (greedy match for the first complete bold span).
- Riskiest Assumption / Most Curious Thread: the first sentence (up to first `.`, `!`, `?`) of the section body, with bolded text stripped of `**` markup.
- Defensive fallback: if extraction yields empty/whitespace-only string, use `unnamed-item-N` where N is the global Pass-2 marker index.

**Pass 2 → Pass 3 mapping:**
- The Pass 3 review file has blockquotes separated by `<<<NEXT>>>`. The number of blockquotes must equal the count of `{{PEER-REVIEW}}` markers in Pass 2 — same hard contract `synthesis-merge.py` enforces today. Fail-fast if mismatch with explicit error message naming both counts.
- Mapping order: blockquotes are matched to markers in source order. Pass 3 review N → Pass 2 marker N → the item containing that marker → emitted file for that item.

**Emitted file contents:**
- YAML frontmatter:
  ```
  ---
  type: <connection|contradiction|...>
  sweep_date: <YYYY-MM-DD>
  sweep_sha: <short-sha>
  section_index: <N>  # Pass 2 item number within section
  global_index: <M>   # global marker index across all sections
  pass3_verdict: <Confirmed|Push-back|...>  # parsed from blockquote first line
  overlap_with: <slug-of-other-item>  # only when verdict tags OVERLAP / DUPLICATE
  ---
  ```
- Body: the Pass 2 item's full content with the `{{PEER-REVIEW}}` marker stripped, followed by the Pass 3 review blockquote. (Reworded per spec re-review N3 — original parenthetical was ambiguous.)

**Sweep-history file emission:** in addition to the per-item files, the script emits one file at `synthesis/history/<sweep-date>-<short-sha>.md`. Content per §5.6.

**Failure modes (fail-fast with named errors):**
- Marker count mismatch between Pass 2 and Pass 3 → exit code 1 with explicit count comparison.
- Section header recognition misses a section the prompt is supposed to produce → exit code 1 (defends against silent drops).
- Headline extraction fails with empty fallback for >50% of items in a sweep → exit code 1 (defends against parser break on format drift).
- Slug collision after `<index>` disambiguator (should be impossible by §5.1 design, but defend) → exit code 1.

**Test plan:** §7 specifies validation against multiple historical Pass 2 logs spanning different synthesizer models — DeepSeek V4-Pro, Gemini 2.5 Pro, GPT-5.5 (where Pass 3 only). Specific files listed in §7.

### 5.5 Cross-link rewrite policy

Per §4.4 — **drop-or-stub**, not per-item-rewrite. Three rules:

- **Already-actioned-content links** (e.g., "synthesis.md Connection 7" where the canonical content lives in a wiki page anyway): drop the synthesis.md breadcrumb. Leave the substantive cross-reference to the canonical page.
- **Whole-file links** (e.g., "[Synthesis Queue](synthesis.md)"): rewrite to `synthesis/README.md`.
- **Anchor links to structured sections of synthesis.md** (e.g., `#strategic-reflections-queue`, `#sweep-history`, `#where-actioned-items-live-now`): rewrite to `synthesis/strategic-reflections/`, `synthesis/history/_pre-2026-05-08-archive.md`, or `synthesis/README.md` respectively.
- **Dangling old anchors** (e.g., "2026-04-21 Open Question 3" pointing at long-deleted content): drop silently.

**Implementation:** the cross-link cleanup happens in §8 step *before* deletion of `wiki/synthesis.md`, so the repo is never in a state where the file is deleted but cross-links still point to it.

### 5.6 history/ file content + sweep-state.json relationship

**`synthesis/history/<sweep-date>-<short-sha>.md`** is human-browsable narrative. One file per sweep run. Content:

```markdown
---
sweep_date: <YYYY-MM-DD>
sweep_sha: <short-sha>
trigger_files: [list]
synthesizer: <model-name>
reviewer: <model-name>
log: <relative-path-to-logs/v4-synthesis-*.md>
items_emitted: <N>
items_by_type:
  connection: <n>
  contradiction: <n>
  ...
---

# Sweep <date> — <short-sha>

[Brief narrative paragraph summarizing what the sweep emitted, generated by the script from the Pass 2 + Pass 3 metadata.]

## Items emitted

[Table: type / index / slug / verdict / queue-path]
```

**`logs/sweep-state.json`** is the machine-readable cursor (what the daemon uses to track its position). It contains `last_successful_sweep` with `commit + timestamp + synthesis_log` only. Single-file, current-state-only. NOT human-browsable.

**Distinction:** `synthesis/history/` files are sticky per-sweep narratives. `sweep-state.json` is a transient registry. They're complementary; both stay.

### 5.7 Strategic Reflections semantics

`synthesis/strategic-reflections/` is **human-curated only**. Daemon does NOT write here. Walk-synthesis skill checks the directory (lists open reflections) but does not action them — they fire on substance maturity, not on walkthrough cadence.

**Resolution criteria:** when a reflection's trigger condition fires AND the user-decided outcome is documented, the file moves (via `git mv` to preserve path history per re-review N4) to `synthesis/strategic-reflections/_resolved/<original-filename>.md`. The migration includes the move:
- Frontmatter gets a new field: `resolved_date: YYYY-MM-DD`
- File body gets an appended section: `## Resolution outcome` documenting what was decided
- Original Trigger / Outcome sections preserved verbatim above the resolution section
- **Path preservation: full content stays git-tracked; only path changes** (consistent with §5.10 done/_archive/ rule).

The `_resolved/` directory is NOT created in this migration since no reflections are resolved yet. First resolution will create it.

### 5.8 README files — explicit content specification

**`synthesis/README.md`** — required sections:
1. **What is this directory?** — one paragraph: "This directory holds the action queue and history of the wiki sweep daemon (`scripts/sweep-1-propagate.py` etc.). It is project-management content, not science. Research findings live in `wiki/`."
2. **Subdirectory map** — one line per subdirectory: queue/ done/ history/ strategic-reflections/.
3. **File-naming convention** — point at the spec at `operations/specs/2026-05-08-synthesis-filesystem-migration.md` §5.1.
4. **Daemon-write vs human-write boundary** — daemon writes to queue/ + history/ via `scripts/synthesis-emit-files.py`. Humans write to strategic-reflections/. Walkthrough moves files queue/ → done/.
5. **Closure flow** — link to walk-synthesis skill at `.claude/skills/walk-synthesis/SKILL.md`.
6. **Historical pointer** — one line: pre-2026-05-08 sweep history archived at `synthesis/history/_pre-2026-05-08-archive.md`.
7. **Spec link** — full context at `operations/specs/2026-05-08-synthesis-filesystem-migration.md`.

**`synthesis/strategic-reflections/README.md`** — required sections:
1. **What lives here?** — content-triggered platform-level reflections; humans write here.
2. **Why separate from queue/?** — one paragraph: queue/ is daemon-emitted unit-of-work items; reflections are platform reframes that fire on substance maturity, not on walkthrough cadence.
3. **Resolution flow** — link to spec §5.7.
4. **Currently-open reflections** — list with one-line description each.

### 5.9 Recursion protection — `[skip-wiki-sweep]` marker is load-bearing

Per spec review Finding 2: the GitHub Actions `paths` filter is best-effort, NOT a robust recursion guard. A push that contains MULTIPLE commits (which is normal for sequential daemon pushes) applies path filters to the AGGREGATE file set across all commits. If any commit in the push touches a `wiki/**.md` path, the workflow fires regardless of `'!synthesis/**'` negation.

**Decision:** the **`[skip-wiki-sweep]` commit-msg marker is the canonical recursion guard.** All daemon-emitted commits MUST include the marker. The path-filter is kept as an additional defensive layer (catches the simple case where a push is daemon-only) but is NOT relied upon.

**Implementation:**
- Path filter: `paths: ['wiki/**.md']` (NO negation; the simpler form). The previous `'!wiki/synthesis.md'` exclusion is removed because the file no longer exists.
- Job-level `if:` conditions on every job in `.github/workflows/wiki-sweep.yml` check the head-commit-message for `[skip-wiki-sweep]` and skip if present. (This pattern is already in use; verify it's applied to all jobs.)
- Daemon-emitted commits in `synthesis-emit-files.py`: explicit `[skip-wiki-sweep]` in commit message; assert at script exit that the message contains the marker.
- Hooks (`.claude/hooks/validate-commit-msg.py`, `.claude/hooks/block-push-without-approval.py`) already understand the marker; verify they handle the new `synthesis/**` paths correctly.

**CI invariant added:** "Pass 3 must only write to `synthesis/` and `logs/`, never to `wiki/`." Verified by a CI check on the daemon's diff (out-of-scope to add the check itself; documented as an invariant the new architecture must preserve).

### 5.10 done/ archive rotation rule (deferred but pre-specified)

Per spec review Q2: YAGNI applies — no archive rotation today. But pre-specifying the rule in advance lets the future spec be short:

- **Rule:** after 12 months in `synthesis/done/`, items move to `synthesis/done/_archive/<year>/`.
- **Trigger:** quarterly cron OR manual `scripts/synthesis-archive.py` invocation.
- **Preservation:** full content stays git-tracked; only path changes.

NOT implemented in this migration. Documented here so the directory structure anticipates it.

## 6. Success criteria

All of these must be verifiable post-implementation, before declaring done:

1. **Directory structure exists:** `synthesis/` directory at repo root with `queue/`, `done/`, `strategic-reflections/`, `history/` subdirectories. Each non-content directory has `.gitkeep`.

2. **Strategic reflections migrated:** `synthesis/strategic-reflections/` contains exactly 3 reflection files + 1 README:
   - `platform-framing-reframe.md`
   - `chaperone-framework-validation.md`
   - `application-layer-surface-architecture.md`
   - `README.md` (per §5.8)
   Each reflection file contains the Trigger / Outcome columns from the synthesis.md row, preserved verbatim.

3. **History migrated:** `synthesis/history/_pre-2026-05-08-archive.md` exists and contains the sweep-history table from `wiki/synthesis.md` (all rows).

4. **`wiki/synthesis.md` deleted.**

5. **`scripts/synthesis-emit-files.py` exists; replaces `synthesis-merge.py` (which is deleted).** Local test: invoking the new script with EACH of the test logs in §7 produces:
   - One file in `synthesis/queue/` per Pass 2 item, named per §5.1 with all required parts (`<sweep-date>-<type>-<index>-<slug>.md`)
   - Frontmatter with all fields per §5.4 emitted file contents
   - One file in `synthesis/history/` named `<sweep-date>-<short-sha>.md` with all required frontmatter fields per §5.6
   - No write to `wiki/synthesis.md` (file shouldn't exist anyway)
   - Exit code 0
   - For at least one of the test logs: the script's defensive parsing (failure modes per §5.4) is exercised in a "fail-fast" smoke-test by intentionally truncating the log mid-item and verifying exit code 1.

6. **Workflow file updated:** `.github/workflows/wiki-sweep.yml` has:
   - Path filter is `paths: ['wiki/**.md']` with no `'!wiki/synthesis.md'` negation.
   - Pass 3 step calls `synthesis-emit-files.py` not `synthesis-merge.py`.
   - Pass 3 step commits to `synthesis/queue/` + `synthesis/history/`, not `wiki/synthesis.md`.
   - Pass 3 commit message contains `[skip-wiki-sweep]`.
   - Step name / comments updated to reflect new outputs.
   - YAML syntax verified: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/wiki-sweep.yml'))"` exits 0.

7. **Pass 1 + Pass 2 + Pass 3 prompts updated:** all references to `wiki/synthesis.md` in the four prompt files (sweep-prompt-1-propagate.md, sweep-prompt-2-synthesize.md, sweep-prompt-3-review.md, sweep-prompt-3-review-gpt55.md) point at the new paths.

8. **`scripts/sweep-1-propagate.py`, `scripts/synthesize.py`, `scripts/sweep-3-review.py`, `scripts/sweep-state.py`, `scripts/eval-propagation.py`, `scripts/wiki-update.sh`, `scripts/deepseek-v4-assessment.md`, `scripts/fresh-synthesis.py`** updated per §4.3.

9. **Hooks updated:** `.claude/hooks/validate-commit-msg.py` line 96 special-case removed; `.claude/hooks/block-push-without-approval.py` understands new `synthesis/**` paths.

10. **Skills updated:** all four `.claude/skills/walk-synthesis`, `sweep-status`, `sweep-catchup`, `new-comp-experiment` files updated per §4.3. walk-synthesis Section 1, Step C-F, Section 7, Section 6 templates, and Section 9 anti-patterns explicitly reflect the per-file model.

11. **No `wiki/synthesis.md` references in scripts/, .claude/, README.md, mkdocs.yml, top-level CLAUDE.md, or index.md.** Verifiable via:
    ```bash
    grep -rn "wiki/synthesis\.md\|synthesis-merge" scripts/ .claude/ README.md mkdocs.yml CLAUDE.md index.md
    ```
    Expected: zero results.
    **Wiki cross-links per §4.4 cross-link policy:** `grep -rn "synthesis\.md" wiki/` shows the post-migration state — each remaining match either (a) was rewritten to point at the new structure per §5.5, OR (b) was dropped per the §5.5 drop-the-breadcrumb rule. Verify each match falls into one of these categories during code review.

12. **mkdocs nav builds without breakage:** local test `mkdocs build --strict` (or equivalent) exits 0 with no broken-link warnings about `wiki/synthesis.md`.

13. **Daemon CI runs successfully** when `walk-synthesis-2026-05-08` merges to main. **Rollback plan if CI fails:** `git revert <merge-commit>` restores the pre-migration state; the daemon will fall back to the old `synthesis-merge.py` script (assuming the revert is clean). Document this in §8.

## 7. Risks + mitigations

| Risk | Mitigation |
|---|---|
| `synthesis-emit-files.py` parsing breaks on real Pass 2 output | Multi-log local test against ≥3 historical Pass 2 logs spanning different synthesizer models (target list below). Defensive parsing with fail-fast behavior per §5.4 failure modes. |
| Pass 2 log format drift across synthesizer models / future model upgrades | Multi-log test surfaces format variance NOW; future format drift surfaces as a fail-fast script error in CI rather than silent corruption. |
| Workflow YAML syntax error → daemon CI broken | Run `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/wiki-sweep.yml'))"` locally before committing per success criterion 6. |
| Some `wiki/synthesis.md` reference missed → daemon writes to or reads from a non-existent file | Comprehensive grep at end of implementation per success criterion 11. |
| Cross-link breakage in 27 wiki pages | §5.5 drop-or-stub policy; each match verified to fall into the policy categories during code review per success criterion 11. |
| Published docs site (`mkdocs build`) breaks | `mkdocs build --strict` smoke test per success criterion 12; mkdocs.yml nav rewrite explicitly listed in §4.5. |
| `scripts/sweep-1-propagate.py` `READ_ONLY_GLOBS` pointing at non-existent `wiki/synthesis.md` after deletion | The reference is removed from the list per §4.3; verified in the §11 grep. |
| Walk-synthesis skill update interacts badly with Step F discipline | Step F's "loose ends" inventory and "carryover to Item X" anchoring are explicitly preserved with re-grounding in the per-file model per §3 + §4.3 (skill update). The re-grounding is a documentation pass, not a behavioral change; failure mode is "skill is unclear" (surfaces fast — next walkthrough), not "skill silently breaks." |
| Migration loses content from synthesis.md | Sweep-history is in `synthesis/history/_pre-2026-05-08-archive.md`; reflections in `synthesis/strategic-reflections/`; today's actioned-item annotations are in commit history (`ba981ee..156dfe1`); canonical content is in wiki/ pages per "Where actioned items live now." Multiple redundant preservation surfaces. |
| Path-filter recursion guard fails in subtle edge cases | §5.9 redesign — `[skip-wiki-sweep]` marker is canonical; path filter is best-effort. Belt-and-suspenders. |
| Independent peer reviewer disagrees with a §5 design decision | Spec review happens BEFORE implementation. Reviewer findings get addressed (or explicitly defended in spec) before code is written. (Per §11 review history — this gate has now run.) |
| Code peer review surfaces issues after implementation | Code review against this spec happens BEFORE local script test (per §8 step ordering); fix loop is small. |

**Multi-log test list for synthesis-emit-files.py validation (§7 risk mitigation):**

The local test must successfully process ≥3 of these historical Pass 2 logs — chosen to span synthesizer models and Pass 3 reviewers:

1. `logs/v4-synthesis-2026-05-08-e842754.md` — Gemini 2.5 Pro synthesizer + GPT-5.5 reviewer (today's most recent; the format the next post-merge sweep will produce)
2. `logs/v4-synthesis-2026-05-07-abc8de9.md` — Gemini 2.5 Pro + Opus 4.7 (older Pass 3 reviewer)
3. `logs/v4-synthesis-2026-05-07-77d0f6e.md` — Gemini 2.5 Pro + Opus 4.7
4. `logs/v4-synthesis-2026-05-06-121731c.md` — DeepSeek V4-Pro synthesizer + Opus 4.7 reviewer
5. `logs/v4-synthesis-2026-05-05-3e928d3.md` — Gemini 2.5 Pro + Opus 4.7 (older format)

Test execution: run the new script against EACH log with a synthetic Pass 3 review file (just the marker count must match). Verify per-file output, frontmatter, history file, exit code 0. If any single log fails, investigate the format variance and either fix the parser or document the unhandled format as a known limitation.

## 8. Migration plan (operational sequence)

**Atomic feature-branch merge.** All steps execute on `walk-synthesis-2026-05-08` branch; merge to main is a single PR (#4) so the daemon's first post-merge run uses the new architecture, no transition window with mixed state.

**Step ordering rationale (clarified per spec re-review N5):** the workflow YAML update lands LAST (step 4.x) intentionally — until that step, the daemon's old entry point (`synthesis-merge.py`) is still on disk and would still execute correctly if a daemon push fired during the transition. The workflow is the daemon's true entry point; updating it last ensures the daemon either runs the OLD pipeline end-to-end OR the NEW pipeline end-to-end, never a half-state. Wiki cross-link cleanup (step 4.viii) lands before script writing (step 4.ix) because cross-link rewrites are content-only changes that don't affect daemon execution. Deletion of `wiki/synthesis.md` + `synthesis-merge.py` (step 4.xi) is the truly atomic last step before final grep verification.

1. ~~Author this spec~~ → done
2. ~~**Independent Opus subagent — spec review**~~ → done; report at `operations/specs/2026-05-08-synthesis-filesystem-migration-spec-review.md`
3. ~~Address spec findings~~ → done in this revision; see §11 review history
4. **Implement against reviewed spec** — order matters; specifically, cross-link cleanup MUST happen before deletion of `wiki/synthesis.md` so the repo is never in a state with deletion + dangling cross-links.
   1. Create `synthesis/` directory + READMEs + .gitkeep files (§4.1, §5.8)
   2. Migrate Strategic Reflections + sweep history (§4.1)
   3. Update prompts (Pass 1, Pass 2, Pass 3 ×2) per §4.3 — references-only updates, no content changes
   4. Update scripts: `sweep-1-propagate.py`, `synthesize.py`, `sweep-3-review.py`, `sweep-state.py`, `eval-propagation.py`, `wiki-update.sh`, `deepseek-v4-assessment.md`, `fresh-synthesis.py` per §4.3
   5. Update hooks per §4.3
   6. Update skills per §4.3 — walk-synthesis is the major one
   7. Update `scripts/SWEEP-ARCHITECTURE.md`, `CLAUDE.md`, `index.md` (repo root), `wiki/index.md`, `README.md`, `mkdocs.yml` per §4.5
   8. **Cross-link cleanup in 27 wiki pages per §4.4 + §5.5** — must happen before step 9
   9. Write `scripts/synthesis-emit-files.py` (defensive parsing per §5.4)
   10. Update `.github/workflows/wiki-sweep.yml` per §4.3 — last because it's the daemon's actual entry point; want everything else in place first
   11. **Delete `wiki/synthesis.md` and `scripts/synthesis-merge.py`** — atomic last step; previous steps ensure no dangling references
   12. Final grep verification per success criterion 11
5. **Independent Opus subagent — code review against spec** (gate)
6. Address code findings
7. Local test: invoke `synthesis-emit-files.py` with each Pass 2 log in the §7 test list; verify per-file output + history file + frontmatter + fail-fast smoke test
8. Run `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/wiki-sweep.yml'))"` (success criterion 6)
9. Run `mkdocs build --strict` if mkdocs is locally invokable (success criterion 12)
10. Commit + push to `walk-synthesis-2026-05-08`; PR #4 picks up changes
11. PR #4 merges to main → daemon fires using new architecture → validation in production
12. **If daemon CI fails on first post-merge run:** `git revert <merge-commit>` restores pre-migration state; daemon falls back to the old `synthesis-merge.py` script. Document the failure cause; address in a follow-up PR; re-attempt.

## 9. Open questions — resolved in spec review

All 4 open questions from the original spec draft are resolved per the §11 review-history engagement.

(See §5.1 for naming-convention resolution, §5.7+§5.10 for done/-rotation resolution, §5.8 for Strategic Reflections README resolution, §4.3 for SWEEP-ARCHITECTURE.md inclusion resolution.)

## 10. Non-changes (explicit no's)

- Daemon's underlying multi-vendor architecture (Pass 1 / Pass 2 / Pass 3 with different vendors) — UNCHANGED
- Pass 2 + Pass 3 prompt content beyond reference updates — UNCHANGED
- Synthesizer's output structure (Connections / Contradictions / etc) — UNCHANGED
- `[skip-wiki-sweep]` commit-msg marker semantics — UNCHANGED (it's now load-bearing per §5.9; was previously belt-and-suspenders)
- Pre-commit grep-verify gate (CLAUDE.md Rule 4) — UNCHANGED
- Subagent brief hygiene discipline — UNCHANGED
- comp-NNN verification-agent infrastructure proposal — UNCHANGED (this spec is independent of that proposal)
- The substance of the walk-synthesis skill's per-item discipline (Steps A-F rules) — UNCHANGED. Only the I/O format changes.

---

## 11. Review history

### 2026-05-08 — Independent peer review (Opus 4.7)

**Reviewer:** Claude Opus 4.7 (1M context), spawned with brief-hygiene-clean instructions (no leading framing, no "I think this is right" anchor; reviewer read spec + 11 supporting files; surfaced findings independently).

**Verdict:** NEEDS REWORK — major issues, spec should be revised before implementation.

**Full review report:** [`2026-05-08-synthesis-filesystem-migration-spec-review.md`](./2026-05-08-synthesis-filesystem-migration-spec-review.md).

**Critical findings addressed:**

1. **§4 file list incomplete (Finding 1).** Reviewer enumerated ~30+ additional files referencing `wiki/synthesis.md` that the original spec missed. The original spec listed ~15 files; the revised §4 enumerates exhaustively across daemon machinery (`scripts/`, `.github/workflows/`, `.claude/hooks/`, `.claude/skills/`), user-facing docs (`README.md`, `mkdocs.yml`, `wiki/index.md`), and 27 wiki cross-links. Success criterion 11 rewritten to be verifiable.

2. **§5.7 path-filter design wrong (Finding 2).** The original spec claimed `'!synthesis/**'` would prevent daemon recursion. Reviewer correctly noted that GitHub Actions `paths` filters apply to the AGGREGATE file set across multiple commits in a push — so a daemon push touching `wiki/**.md` (via Pass 1 propagation) AND `synthesis/queue/*.md` (via Pass 3 emit) would still fire. The revised §5.9 documents `[skip-wiki-sweep]` as the canonical recursion guard with the path filter as best-effort; CI invariant added that Pass 3 never writes to `wiki/`.

3. **§5.3 / §4.2 Pass 2 parsing undefined (Finding 3).** Original spec said the new script "writes one file per Pass 2 item" without specifying the parser. Reviewer noted `synthesis-merge.py` does opaque string substitution, not parsing — a real parser must be specified. New §5.4 "Pass 2 parser specification" subsection added with explicit section-recognition regex, item-boundary detection, headline extraction, slug derivation, Pass 2 → Pass 3 mapping, emitted file contents, and 4 fail-fast failure modes.

4. **Cross-link policy not defined (Finding 4).** 27 wiki pages cite synthesis.md by anchor; original spec didn't address what happens to those references. New §5.5 "Cross-link rewrite policy" subsection specifies drop-or-stub policy with three rules (drop-the-breadcrumb for already-actioned content; rewrite for whole-file-links; rewrite for anchor-links to structured sections; drop dangling old anchors silently).

**Important findings addressed:**

5. **Success criteria not testable (Finding 5).** Criteria 5, 11, 12 rewritten in revised §6 to be specifically verifiable — naming the test logs, the grep command, the rollback plan.

6. **Strategic Reflections `_resolved/` half-built (Finding 6).** Revised §5.7 specifies resolution criteria, frontmatter changes, and section appendage explicitly.

7. **history file vs sweep-state.json relationship unclear (Finding 7).** Revised §5.6 distinguishes the two: history/ is human-browsable narrative (sticky per-sweep), sweep-state.json is machine-readable cursor (current state). Complementary.

8. **Single-log test insufficient (Finding 8).** Revised §7 specifies multi-log test against 5 historical Pass 2 logs spanning different synthesizer models; ≥3 must pass.

9. **§8 ordering issue (Finding 9).** Step 8h (delete synthesis.md) → 8i (cleanup remaining refs). Revised §8 reorders so cross-link cleanup happens BEFORE deletion (§8 step 4.viii), so the repo is never in a state with deletion + dangling refs.

10. **Risk table missing entries (Finding 10).** Revised §7 adds: cross-link breakage, mkdocs breakage, format drift, READ_ONLY_GLOBS, Step F skill interaction.

11. **README under-specified (Finding 11).** Revised §5.8 specifies content for both `synthesis/README.md` and `synthesis/strategic-reflections/README.md` with 7 + 4 required sections respectively.

**Minor findings addressed:**

12. **Type names (Finding 12).** Revised §5.1 uses hyphenated forms throughout: `connection`, `contradiction`, `experiment`, `open-question`, `priority-action`, `riskiest-assumption`, `most-curious-thread`.

13. **Strategic Reflections separate README (Finding 13).** Yes — added per §5.8.

14. **§3 cross-link policy mention (Finding 14).** Revised §3 explicitly mentions cross-link policy lives at §5.5.

15. **Riskiest Assumption / Most Curious Thread overlap flagging (Finding 15).** Revised §5.2 adds defensive `overlap_with` frontmatter field.

16. **`<sweep-date>` ambiguous (Finding 16).** Revised §5.1 specifies: workflow_run's `event.head_commit` timestamp in UTC, ISO format.

17. **§3 "Steps A-F" wording (Finding 17).** Revised §3 says "the SUBSTANCE of the skill's per-item discipline" — clarifying I/O format is in scope, behavior rules are not.

18. **Spec status block (Finding 18).** Frontmatter `status:` updated to `revised post-spec-review (ready for implementation)`.

**Open questions resolved:**

- **Q1 file naming:** added `<index>` for collision robustness per reviewer Q1 recommendation. Format: `<sweep-date>-<type>-<index>-<slug>.md`.
- **Q2 done/ rotation:** rule pre-specified in §5.10; not implemented in this migration (YAGNI).
- **Q3 Strategic Reflections README:** yes; added per §5.8.
- **Q4 SWEEP-ARCHITECTURE.md inclusion:** yes; bundled in this spec per §4.3 (avoids doc-drift window).

**What's good (preserved from review):**
- §2 motivation — concrete and grounded
- §5.7 (now §5.7 in revised spec) Strategic Reflections semantics — human-only writes
- §3 out-of-scope discipline — resists scope creep
- §5.3 always-emit-regardless-of-verdict — preserves walkthrough information
- §7 YAML validation — defensive
- §8 spec-review-before-implementation discipline — 2-stage review pattern
- Atomic-merge-with-PR-#4 decision — sensible

**Status after revision:** spec is approvable for implementation contingent on second-pass review. (The original closing line "second-pass spec review is NOT required" was retracted per re-review N6 — it was the spec author's self-assessment, not the reviewer's; the second pass DID surface a real critical finding (N1 chembl-refresh-prompt.md), validating the gate.)

### 2026-05-08 — Independent peer re-review (Opus 4.7)

**Reviewer:** Claude Opus 4.7 (1M context), spawned as a fresh independent reviewer (not the same process as the first review; SendMessage tooling unavailable in the session). Briefed with the first review's findings + the revised spec; tasked with verifying each prior finding was properly addressed plus checking for new issues.

**Verdict:** APPROVED WITH MINOR CHANGES — 17 of 18 prior findings properly addressed; 1 partially addressed (Finding 1 — `scripts/chembl-refresh-prompt.md` was missed); 5 minor nits (N2-N6) introduced or surfaced by the revision.

**Full re-review report:** [`2026-05-08-synthesis-filesystem-migration-spec-rereview.md`](./2026-05-08-synthesis-filesystem-migration-spec-rereview.md).

**Critical-tier remaining issue (N1) addressed:**

- **`scripts/chembl-refresh-prompt.md`** — separate quarterly workflow (NOT the wiki-sweep daemon) writes to `wiki/synthesis.md` from its Pass 4. 7 references the spec author missed. Same root cause as Finding 1: grepped daemon-direct files only, missed parallel-workflow files. **Resolution:** Brian decision 2026-05-08 — option 2 (direct write of `synthesis/queue/<date>-chembl-discrepancy-N.md` files; new `chembl-discrepancy` type added to §5.1; chembl-refresh's Pass 4 changes accordingly; documented in §4.3 under new "Parallel workflows that write to `wiki/synthesis.md`" sub-bullet).

**Minor findings (N2-N6) addressed:**

- **N2 (incomplete index.md / CLAUDE.md enumeration):** §4.5 expanded with explicit line-by-line callouts (`index.md` lines 15, 21, 176; `CLAUDE.md` lines 27, 130, 247).
- **N3 (confusing parenthetical in §5.4):** reworded — "Pass 2 item's full content with the `{{PEER-REVIEW}}` marker stripped, followed by the Pass 3 review blockquote."
- **N4 (verb consistency between §5.7 and §5.10):** §5.7 explicitly notes `git mv` and "full content stays git-tracked; only path changes" consistent with §5.10.
- **N5 (§8 step ordering rationale):** added one-line note explaining why workflow update lands last.
- **N6 (§11 over-confident "no second-pass needed" claim):** retracted; this re-review entry documents the second-pass gate validating its own value.

**§11 review-history accuracy (per re-review):** "honest and accurate; the only over-claim was the closing line." That's now corrected.

**Strongest improvements over original spec (preserved from re-review):** §5.4 parser specification (concrete enough to write the script); §5.9 recursion-protection redesign with `[skip-wiki-sweep]` as canonical guard; §5.1 `<index>` tiebreaker (slug collision structurally impossible); §7 multi-log test list; §8 cleanup-before-deletion ordering with explicit atomic feature-branch merge.

### 2026-05-08 — Independent peer third-pass review (Sonnet 4.6)

**Reviewer:** Claude Sonnet 4.6, spawned as fresh independent reviewer. Briefed with the prior review reports + the now-twice-revised spec. Tasked with mechanical verification that N1-N6 are properly addressed + catch any new issues introduced by the second revision.

**Status:** pending.

**Status after this third-pass review:** spec implementation gate. If approved → §8 step 4 begins.

---

## End of spec

**Status:** twice-revised; pending Sonnet third-pass spec review.

**Implementation gate:** §8 step 4 may begin AFTER the third-pass review approves the revisions. Code review against spec (§8 step 5) remains the gate before local testing and merge.
