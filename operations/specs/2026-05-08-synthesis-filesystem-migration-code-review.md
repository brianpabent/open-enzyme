# Code Review — synthesis-filesystem-migration implementation (2026-05-08)

**Reviewer:** Claude Opus 4.7 (1M context), independent peer code review.
**Branch:** `walk-synthesis-2026-05-08`
**Spec reviewed against:** `operations/specs/2026-05-08-synthesis-filesystem-migration.md` (post-third-pass)

## Verdict

**NEEDS REWORK.**

The directory structure, content migration, parser, and workflow YAML are solid — the load-bearing pieces work correctly and the parser passes 3 of 4 tested historical logs (the 4th fails legitimately because the log is itself truncated, which is the parser doing its fail-fast job). However:

1. **Walk-synthesis SKILL.md still describes the OLD synthesis.md surgical-edit world** in Section 1 (read-end-to-end), Section 2 Steps C-E (no `git mv` flow), Section 7 (manual surgical inbox-zero) and Section 9 (anti-pattern #15 missing). The skill is what humans/agents actually run; shipping with stale guidance defeats the migration's auto-inbox-zero benefit on day one. Spec §4.3 explicitly enumerates these changes; they're not optional.
2. **Mechanical-sed bugs in 5 functional files** produce nonsensical comparisons like `path == "synthesis/queue/"` against wiki/*.md paths (always False — dead code). These are in load-bearing daemon scripts (`sweep-1-propagate.py`, `sweep-state.py`, `synthesize.py`, `validate-commit-msg.py`, `block-push-without-approval.py`).
3. **Three top-level user-facing docs (CLAUDE.md, README.md, index.md) point "Action queue" callouts at `synthesis/README.md`** instead of `synthesis/queue/`. The README is the explainer; the queue is the action queue. The label and the link disagree.
4. **`synthesis-emit-files.py` uses `datetime.date.today()`** for `<sweep-date>` instead of the workflow_run's `event.head_commit` timestamp date (spec §5.1). Filenames generated against historical logs end up dated 2026-05-08, not the trigger commit's date. Functionally cosmetic for forward operation but breaks the spec contract.
5. **chembl-refresh-prompt.md retains 3 stale "synthesis.md" references** in lines 152, 166, 167 outside the rewritten Pass 4 block.
6. **Pass 2 / Pass 3 prompt prose ("bottom-of-file sections", "prepend to synthesis/queue/", "most-recent block of synthesis/queue/")** still describes a single-file-with-sections world.

None of these are catastrophic — the daemon would still produce correct queue files on the first post-merge run, and the parser-as-built handles real Pass 2 output. But (1) and (3) will degrade the very next walkthrough, and (2) is enough sed-induced wrongness in load-bearing files to warrant a cleanup pass before merge.

---

## Critical findings (ship-blocking)

### C1. walk-synthesis/SKILL.md not behaviorally updated for per-file model

**File:** `.claude/skills/walk-synthesis/SKILL.md`

Spec §4.3 is explicit:
> Section 1 (Pre-flight): inventory becomes `ls synthesis/queue/` instead of "read synthesis.md end-to-end."
> Section 2 Step C (Action it) + Step D (Annotate `✓ Actioned`) + Step E (Commit immediately): closure flow becomes append-closure-annotation-to-file + `git mv synthesis/queue/<file>.md synthesis/done/`.
> Section 7 (End-of-walkthrough): inbox-zero is automatic (empty queue/ = inbox zero); no surgical synthesis.md edit.
> Section 9 anti-patterns: add #15 "don't try to edit `wiki/synthesis.md` (it doesn't exist anymore)."

What's actually in the file:
- **Section 1 step 2** (line 42): "Read `synthesis/queue/` end-to-end. Inventory every item. Synthesis files are typically structured: New Connections (N items)..." — frames synthesis/queue/ as a single file with sections. Should be `ls synthesis/queue/` listing per-item files.
- **Section 1 step 3** (line 44): "Look at the Strategic Reflections Queue at the bottom" — there is no "bottom" because synthesis/queue/ is a directory now. Strategic Reflections live at `synthesis/strategic-reflections/`.
- **Section 2 Step C** (line 114): "write a closure note in synthesis/queue/ closure annotation instead of re-doing the work" — no mention of `git mv` to `synthesis/done/`.
- **Section 2 Step D** (lines 117-127): "add this annotation directly under the relevant Claude review block in `synthesis/queue/`" — implies a single shared file. Should describe per-file append + `git mv`.
- **Section 7.1** (lines 495-505): describes the OLD inbox-zero flow — "Delete the entire sweep block", "Update 'Pending — open items'", "Add a row to the Sweep history table", "Target file size after pruning: ~80 lines." All of this is the surgical-edit world. Per spec, inbox-zero is now AUTOMATIC: empty `synthesis/queue/` = inbox zero by construction. Section 7 needs to be replaced wholesale.
- **Section 9 anti-pattern #15** missing.

**Why this matters:** The whole point of the migration's "auto-inbox-zero" benefit (spec §2 reason 3) is that the skill no longer needs the manual prune pass. Shipping the skill with the manual-prune instructions still in it means the next walkthrough will follow them and the auto-inbox-zero benefit is lost on day one.

**Recommendation:** Substantive Section-1, Section-2 Step C-E, Section-7 rewrite. This is the major skill change spec §4.3 calls out. Cannot be a sed pass; the behavioral discipline changes (single-file → per-file + `git mv`, manual prune → auto). Add anti-pattern #15.

---

### C2. Mechanical-sed bugs in load-bearing daemon code

Five files have artifacts where a sed pass converted `wiki/synthesis.md` → `synthesis/queue/` inside string-equality comparisons that originally tested against a file path. The result is dead code that always evaluates to False.

**`scripts/sweep-1-propagate.py`:**
- Line 50: `READ_ONLY_GLOBS = ["synthesis/queue/", ...]` — original entry was `"wiki/synthesis.md"`. Per spec §4.3 line 83: "remove" — not replace with a directory glob that READ_ONLY_GLOBS' fnmatch logic doesn't match the way the spec intends. Either remove the entry or change to `"synthesis/**"` (the spec's "synthesis/** exclusion" framing).
- Line 598: `os.path.normpath(p) != "synthesis/queue/"` — `p` comes from `changed_paths` filtered to `wiki/*.md`. A wiki-namespaced path can never equal `"synthesis/queue/"`. Always True. Per spec §4.3 line 83: "Line 598 excludes it from `propagated_files`; remove (file no longer exists)." → REMOVE the line.

**`scripts/sweep-state.py`:**
- Line 153: `if p and p != "synthesis/queue/"` — `p` comes from a `git diff` already scoped to `wiki/*.md`. Always True for any wiki path. Per spec §4.3 line 86: "replace with `synthesis/**` filter." → either remove the check or write `not p.startswith("synthesis/")`.

**`scripts/synthesize.py`:**
- Line 420: `if path == "synthesis/queue/": continue` — `path` is matched against the regex `wiki/[A-Za-z0-9_\-./]+\.md`. Cannot ever equal `"synthesis/queue/"`. Per spec §4.3 line 84: "replace with `synthesis/**` exclusion." → either remove or write `if path.startswith("synthesis/"): continue` (though impossible to match anyway given the regex anchors `wiki/`).

**`.claude/hooks/validate-commit-msg.py`:**
- Line 96: `p.startswith("wiki/") and p.endswith(".md") and p != "synthesis/queue/"` — third clause is dead. Spec §4.3 line 95: "Remove the special case (file no longer exists)." → drop the clause.

**`.claude/hooks/block-push-without-approval.py`:**
- Lines 11-12 docstring: `EXCEPT changes only to synthesis/queue/ (synthesis is excluded from the daemon trigger to prevent recursion)` — false post-migration. The path filter is `wiki/**.md`; synthesis/** never matches it. There's nothing to "exclude" — the architectures simply don't intersect.
- Lines 117-118 docstring: same stale framing.
- Line 163: `if line == "synthesis/queue/": continue` — `line` is filtered to wiki/-namespaced .md paths. Cannot equal `"synthesis/queue/"`. Always False. Drop the entire `if`/`continue` block.

**Why this matters:** The bugs are functionally inert (dead branches), but they're in five load-bearing scripts and they'll mislead the next maintainer. The spec was specific that these references should be REMOVED, not sed-replaced. The pattern of mechanical-sed-into-equality-comparisons is also a fingerprint of a regex-replace pass that wasn't reviewed for semantic correctness.

**Recommendation:** Hand-edit each of the 5 files. For each, delete the dead clause OR replace it with the correct semantic test (`startswith("synthesis/")` if you want belt-and-suspenders, removal otherwise).

---

### C3. CLAUDE.md / README.md / index.md mislabel synthesis/README.md as the action queue

**`CLAUDE.md`:**
- Line 27: "`synthesis/README.md` — Cross-doc connections, contradictions, proposed experiments. **Action queue.** Daemon prepends new findings after Pass 2..." — the action queue is `synthesis/queue/`, not the README that explains the directory layout.
- Line 130: "`synthesis/README.md` for the action queue" — same.
- Line 247: "Action queue: `synthesis/README.md`" — same.

**`README.md`:**
- Line 63: "[Synthesis](synthesis/README.md) — cross-doc connections and proposed experiments (action queue)" — labels as action queue, links to README.
- Line 86: "Check [synthesis/README.md](synthesis/README.md) for the latest cross-doc connections" — points readers at the README for findings; findings live in `synthesis/queue/` (and historically in `synthesis/done/` and `synthesis/history/`).

**`index.md`:**
- Line 21: "Synthesis queue: [synthesis/README.md](synthesis/README.md) — unreviewed cross-analysis findings. The sweep daemon prepends new findings here after each save" — three errors: link target wrong, "prepends" framing stale (per-file emission now), and the daemon does NOT write to README.md.

**Why this matters:** These are the canonical user-facing labels. CLAUDE.md is the AI-instruction contract; calling synthesis/README.md "the action queue" will mislead every AI session that reads CLAUDE.md. README.md and index.md are visible on GitHub. All three need to point "action queue" callouts at `synthesis/queue/` (or, if the intent is to land readers on a stable URL even when queue/ is empty, point at `synthesis/README.md` AND describe it as "the README for the action queue at synthesis/queue/").

**Recommendation:** Decide where "action queue" should resolve. If the queue dir itself, link to `synthesis/queue/` and update prose to "daemon emits per-item files here." If the README, change the prose label from "action queue" to "synthesis directory README" and let the README's own internal map point at queue/.

---

## Important findings (should address before merge)

### I1. `<sweep-date>` derivation diverges from spec §5.1

**File:** `scripts/synthesis-emit-files.py` line 455.

Spec §5.1: `<sweep-date>` is "ISO date in UTC of the workflow_run's `event.head_commit` timestamp (date the trigger commit landed, not the date the daemon eventually ran). Format `YYYY-MM-DD`."

Implementation: `sweep_date = datetime.date.today().isoformat()`.

Two issues:
- Uses today's date, not the trigger commit's date. If the daemon runs slightly after midnight UTC on a commit landed yesterday, the filename gets tomorrow's date.
- More immediate: when running the parser against historical logs (the multi-log test in §7), all generated filenames get today's date. So a 2026-05-05 log produces `2026-05-08-...` filenames instead of `2026-05-05-...` filenames.

Forward operation: cosmetic-only as long as the daemon runs same-day as the trigger.

**Recommendation:** Take the date from the trigger commit's timestamp. The script already accepts `--commit-sha`; thread the timestamp through (or pass `--sweep-date` explicitly from the workflow). The workflow YAML can compute `git log -1 --format=%cI ${{ github.sha }}` and feed it in.

### I2. chembl-refresh-prompt.md residual stale references

**File:** `scripts/chembl-refresh-prompt.md`

Pass 4 was substantively rewritten correctly per spec §4.3 N1 — the file format is right (`type: chembl-discrepancy`, frontmatter fields match spec §5.5). But three stale references remain elsewhere:

- Line 152: "the refresh already synthesized into synthesis.md" — stale in the `[skip-wiki-sweep]` rationale.
- Line 166: "or any `wiki/*.md` other than `chembl-cross-check.md` and `synthesis.md`" — synthesis.md no longer exists.
- Line 167: "cross-wiki propagation happens through `synthesis.md` and subsequent wiki-sweep runs" — stale.

**Recommendation:** Update the three remaining references to either drop synthesis.md or rewrite to point at `synthesis/queue/`.

### I3. Pass 2 / Pass 3 prompt prose still single-file-shaped

**File:** `scripts/sweep-prompt-2-synthesize.md`

- Line 7: `synthesis/queue/` bottom-of-file sections — `## Sweep history` (audit trail), `## Where actioned items live now`, `## Strategic Reflections Queue`. — synthesis/queue/ is a directory, no "bottom-of-file." The three named sections live in `synthesis/history/`, `synthesis/done/`, and `synthesis/strategic-reflections/` respectively now.
- Line 33: "use `synthesis/queue/` 'Where actioned items live now' as the index" — same.
- Line 171: "would just restate what's already in the most-recent block of `synthesis/queue/`" — "most-recent block" doesn't apply to per-file emission.
- Line 178: "Pass 3 reviewer will see the no-op and prepend a corresponding short entry to `synthesis/queue/`" — Pass 3 emits a no-op history file (`emit_no_op_history` in synthesis-emit-files.py), not a prepend.
- Line 213: "any `wiki/*.md` file (including `synthesis.md`)" — the include is stale.

**File:** `scripts/sweep-prompt-3-review.md`

- Line 50: "synthesis.md, canonical pages, recent sweep logs" — synthesis.md no longer exists.
- Line 116: "prepending a 'no new synthesis' notice to `synthesis/queue/` instead" — should be "emitting a no-op history file to `synthesis/history/`."

**File:** `scripts/sweep-prompt-3-review-gpt55.md`

- Line 53: "synthesis.md, canonical pages..." — same as sweep-prompt-3-review.md line 50.

**Why this matters:** These are read by Pass 2 and Pass 3 models on every run. Stale framing about "bottom-of-file sections" and "most-recent block" will subtly shape model behavior in directions that don't fit the new architecture (e.g., a model trying to enumerate "what's in the most-recent block" of a directory). Most likely: the model will paper over the inconsistency, but the prompt is still wrong.

**Recommendation:** Rewrite to per-file framing. The structural changes are small per file but each prompt needs a coherent pass.

### I4. sweep-status / sweep-catchup skill files have stale references

**File:** `.claude/skills/sweep-status/SKILL.md`

- Line 54: "atomic with the synthesis.md prepend" — should be "synthesis/queue/ + synthesis/history/ writes."

**File:** `.claude/skills/sweep-catchup/SKILL.md`

- Line 21: "(excluding synthesis.md)" — file gone.
- Line 35: "(c) excludes `synthesis/queue/`" — stale; pending-paths is scoped to `wiki/*.md`, no exclusion needed.
- Line 50: `grep -v 'wiki/synthesis\.md'` in fallback command — stale; remove.
- Line 84-85: "synthesis/queue/ should have a new sweep block prepended" — per-file emission now; should describe the directory's new contents.
- Line 102: "Don't pass `synthesis/queue/` in the trigger_paths list. The workflow filter excludes it" — wrong reason; the workflow filter only matches `wiki/**.md`, period.
- Line 108: "atomically, in the same commit as the synthesis.md prepend" — stale.

**Recommendation:** Hand-edit. These are user-invoked skills; stale text matters.

### I5. Multi-log test gap (KNOWN DEFERRAL)

Per the brief, only today's log was tested against the parser. Spec §7 calls for ≥3 historical logs spanning DeepSeek V4-Pro / Gemini 2.5 Pro / GPT-5.5 reviewer combinations. Flagged in the brief as "IMPORTANT scope gap, not critical."

For what it's worth, I ran the parser locally against 4 logs:
- `logs/v4-synthesis-2026-05-08-e842754.md` (12 markers, Gemini 2.5 Pro / GPT-5.5) — PASSES.
- `logs/v4-synthesis-2026-05-07-77d0f6e.md` (8 markers, Gemini 2.5 Pro / Opus 4.7) — FAILS, but the failure is the LOG itself being truncated mid-Priority-Action-#1 (Pass 2 ran out of context). Parser correctly fails-fast with `Item priority-action #1 has no {{PEER-REVIEW}} marker.` This is the parser doing its job, not a parser bug.
- `logs/v4-synthesis-2026-05-06-121731c.md` (12 markers, DeepSeek V4-Pro / Opus 4.7) — PASSES.
- `logs/v4-synthesis-2026-05-05-3e928d3.md` (14 markers, Gemini 2.5 Pro / Opus 4.7) — PASSES.

3 of 4 pass; the 4th fails legitimately. Multi-log validation is effectively proven by my run. The remaining gap is the fail-fast smoke test (intentional truncation).

### I6. Cross-link cleanup in 27 wiki pages (KNOWN DEFERRAL)

Per the brief, deferred to PR #5 follow-up. Confirmed via `grep -rln "synthesis\.md" wiki/` → 26 files (close enough to the spec's "27" count). All matches are inside wiki/*.md (no scripts/, no top-level docs leaking through). Deferred status acceptable per the brief's framing but should NOT be silently forgotten — the migration's success criterion 11 explicitly calls for this verification, and the daemon's path-filter trigger means the deferred PR is itself a daemon-fire event. Worth scoping the follow-up before merge so it doesn't drop.

### I7. mkdocs build --strict not run (KNOWN DEFERRAL)

Per the brief. Recommendation: run before merge — it's a one-line check (`mkdocs build --strict`) that catches the broken-link-on-published-site failure mode the spec calls out as a real risk.

---

## Minor findings / nits

### M1. Parser slug truncation can produce ugly slugs for unicode-heavy headlines

`slugify()` strips non-ASCII via `s.encode("ascii", "ignore").decode("ascii")` BEFORE the kebab-conversion step. For a headline like "Natural ADA‑modulation synergy" (with U+2011 non-breaking hyphen), the non-breaking hyphen vanishes and you get `natural-adamodulation-synergy` instead of `natural-ada-modulation-synergy`. Cosmetic; spec §5.1 doesn't require unicode-hyphen normalization.

Visible in `/tmp/test-queue/2026-05-08-connection-1-natural-adamodulation-synergy-cordycepin-ada-substrate.md`.

**Recommendation:** Optional. Add a unicode-hyphen normalization pre-step (`s = s.replace("‑", "-").replace("‐", "-").replace("–", "-").replace("—", "-")`) before the ascii-strip if you care about slug aesthetics.

### M2. Verdict regex doesn't handle bold-wrapped verdict closing token

The verdict-extraction regex `Pass 3 review\s*[—-]\s*([A-Za-z][A-Za-z\- ,]+?)(?:\.|\`|$)` works on the canonical Pass 3 reviewer format `> **Pass 3 review — Confirmed.** ...`. But if a future model variant outputs `> **Pass 3 review — Confirmed**.` (closing `**` BEFORE the period), the regex misses it and verdict becomes `unknown`. Real Pass 3 prompts (sweep-prompt-3-review-gpt55.md line 25-26) lock the format down, so this is theoretical.

**Recommendation:** Optional. Consider tolerating optional `**` between verdict and period.

### M3. History file frontmatter `trigger_files` is double-quoted YAML string, not list

Per spec §5.6: `trigger_files: [list]`. Implementation emits `trigger_files: "<comma-sep-string>"`. Functionally fine for YAML parsers; technically not a list. Spec is loose enough that this is acceptable.

### M4. `mkdocs.yml` line 60 nav: "Platform Thesis & Synthesis: synthesis/README.md"

Better than 404, but the user-facing nav label "Platform Thesis & Synthesis" pointing at a directory README that's mostly internal-architecture is a small UX miss. Consider renaming the nav entry to "Synthesis Queue (directory README)" or similar — but this is genuinely minor.

### M5. Workflow YAML line 401-407 commit-message string

```yaml
git commit -m "sweep-3-review: Claude review of Gemini 2.5 Pro synthesis → synthesis/queue/ [skip-wiki-sweep]"
```

The reviewer is GPT-5.5 (per line 357: `REVIEWER_MODEL: openai/gpt-5.5`), not Claude. The hardcoded string says "Claude review" — stale framing from before the GPT-5.5 swap. Cosmetic; the commit message is still parseable.

### M6. Workflow YAML lines 401-402: `if git diff --quiet synthesis/queue/`

After `synthesis-emit-files.py` runs, the script writes to BOTH `synthesis/queue/` AND `synthesis/history/`. The diff check looks only at queue/. If a sweep emits zero items (NO_MARKERS no-op), the no-op-history file IS still written and should be committed, but `git diff --quiet synthesis/queue/` returns "no diff" and the workflow exits without committing the history file. Hard to say if this is a real bug or a feature (the no-op case is "nothing actionable happened"), but worth confirming intent.

**Recommendation:** Change to `git diff --quiet synthesis/queue/ synthesis/history/` to commit history-only changes too.

### M7. fresh-synthesis.py line 88 stale comment

```python
# All wiki/*.md including synthesis.md (V4 needs to see Claude's existing
# annotations as quality reference)
```
Now should read "All wiki/*.md (synthesis/ excluded)" or similar. Minor doc bug.

### M8. deepseek-v4-assessment.md residual references

Lines 5, 162, 216 still mention synthesis.md. Per spec §4.3 line 90, this file should be updated. Low priority since it's an assessment doc, not load-bearing infrastructure.

---

## Parser-specific findings

The parser (`scripts/synthesis-emit-files.py`, 583 lines) is the load-bearing piece. Detailed assessment:

### What's correct

- **Section-header recognition** (line 126-129): regex correctly tolerates the `(ranked by ...)` suffix on Proposed Experiments. Anchored at line-start with `re.MULTILINE`. Header normalization (line 180) collapses the suffix back to the canonical key. Good.
- **Numbered-item extraction** (lines 202-227): finds each `^N\. \*\*` start, computes end at next item's start (or section end), counts markers per item, fail-fast on 0 or >1 markers. Matches spec §5.4 exactly.
- **Single-paragraph extraction** (lines 228-242): handles riskiest-assumption / most-curious-thread per spec.
- **Headline extraction** (lines 245-263): numbered uses first complete bold span after `N. **`; single-paragraph uses first sentence with `**` stripped; falls back to `unnamed-item-N`. Matches spec.
- **Slug derivation** (lines 147-167): lowercases, strips non-ASCII, collapses non-alphanumerics to single hyphens, truncates at word boundary if > 60, fallback to `unnamed`. Matches spec §5.1.
- **File naming** (line 294): `<sweep-date>-<type>-<index>-<slug>.md`. Index is the spec's collision-proof disambiguator. Matches.
- **Pass 2 ↔ Pass 3 mapping** (lines 523-536): orderly, deterministic, fail-fast on count mismatch. Both internal-consistency check (parser-vs-marker-count) and external check (markers-vs-reviews) are present.
- **Fail-fast modes** (lines 215-223, 487, 514, 526-528, 532-535, 297-301): all 4 spec-required failure modes implemented with explicit error messages.
- **NO_MARKERS / MARKER_COUNT_MISMATCH special signals** (lines 467-482): handled correctly. NO_MARKERS produces a no-op history file with `no_op_reason` frontmatter field — clean.
- **History file emission** (lines 333-389): YAML frontmatter with all spec §5.6 required fields, narrative paragraph, items table.
- **Frontmatter conditional `overlap_with` field** (lines 314-315): only emitted when verdict tags overlap. Spec-correct.

### What's wrong or worth flagging

1. **`<sweep-date>` derivation** (line 455) — see C4 / I1. Uses `datetime.date.today()` instead of trigger commit timestamp. Fixable in a few lines.

2. **`overlap_with` field uses `f"item-{N}"` for `[DUPLICATE-OF-N]` markers** (line 273) — but spec §5.2 says `overlap_with: <slug-of-other-item>`. The implementation produces `item-3`, not the actual slug like `2026-05-08-connection-3-the-daf-scr14-disulfidecount...`. Without the slug, the field is much less useful. The fix needs a two-pass approach (gather all slugs first, then resolve forward references). Spec-discrepancy but not load-bearing — the field is defensive informational, not load-bearing for any current code path.

3. **Verdict regex `(?:\.|\`|$)` terminator** — see M2. Works on canonical Pass 3 prompt format. Theoretical fragility.

4. **Single-paragraph item content includes the marker** — `extract_items_from_section` for SINGLE_PARAGRAPH_SECTIONS sets `content = section_body.strip()` (line 240), which keeps the `{{PEER-REVIEW}}` marker. The marker is later stripped at emit time (line 544) so this is fine, but the comment at line 236-237 is slightly misleading. Cosmetic.

5. **History-file `Pass 2 log` link uses `../../`** (line 377): from `synthesis/history/<file>.md` two-up gets to repo root, then `logs/v4-synthesis-...md`. Correct relative path. Good.

6. **The `unnamed-item-N` fallback uses global_index, not section_index** (line 263, called with `fallback_index=global_index` per line 503) — produces unique fallback names but they're keyed on global rather than within-section position. Spec §5.4 says "where N is the global Pass-2 marker index." Implementation matches.

### Overall parser assessment

**The parser is correct and robust.** It handles real Pass 2 output across multiple synthesizer models (DeepSeek, Gemini), correctly fails-fast on truncated logs, generates spec-compliant frontmatter, and respects both the marker-count contract and the per-section item structure. The known issues (sweep_date, overlap_with slug resolution) are localized and don't affect the core write flow. If C2 / I1 are addressed and the remaining mechanical-sed / prompt-prose findings are cleaned up, the parser itself is ready.

---

## What's good

- **Directory structure and content migration** are clean (`synthesis/{queue,done,history,strategic-reflections}/` with .gitkeep files; 3 reflection files migrated faithfully; pre-2026-05-08 history archive preserved verbatim).
- **README files** at `synthesis/README.md` and `synthesis/strategic-reflections/README.md` are well-written and match spec §5.8's required-section list.
- **Workflow YAML** correctly invokes `synthesis-emit-files.py`, commits to `synthesis/queue/`, includes `[skip-wiki-sweep]`, has the path filter at `wiki/**.md` without the negation. YAML validates (`python3 -c "import yaml; yaml.safe_load(...)"` passes).
- **Strategic reflections** preserve Reflection / Trigger / Outcome content from the synthesis.md table verbatim. Spot-checked all 3.
- **History archive** at `synthesis/history/_pre-2026-05-08-archive.md` preserves the full sweep history table.
- **Parser fail-fast behavior** is correct on truncated logs and produces useful error messages. The spec §5.4 4-mode failure list is implemented.
- **chembl-refresh-prompt.md Pass 4 rewrite** correctly implements option-2 (direct write) per spec §4.3 N1, with the right frontmatter shape and the per-discrepancy file pattern.
- **The atomic feature-branch approach** (everything on `walk-synthesis-2026-05-08`) means no transition window with mixed state. Good operational hygiene.

The migration's load-bearing pieces (parser, workflow, directory structure, content migration) all work. The remaining issues are concentrated in (1) the walk-synthesis skill's documented behavior not catching up to the new model and (2) mechanical-sed cleanup in scripts and docs.

---

## Files I read for this review

- `operations/specs/2026-05-08-synthesis-filesystem-migration.md` — spec, read end-to-end.
- `scripts/synthesis-emit-files.py` — parser, read entirely (584 lines), tested locally.
- `.github/workflows/wiki-sweep.yml` — workflow YAML, read entirely.
- `scripts/chembl-refresh-prompt.md` — Pass 4 rewrite verification.
- `scripts/sweep-prompt-2-synthesize.md` — checked for stale references.
- `scripts/sweep-prompt-3-review.md` — checked for stale references.
- `scripts/sweep-prompt-3-review-gpt55.md` — checked for stale references.
- `scripts/sweep-1-propagate.py` — checked READ_ONLY_GLOBS + propagated_files filter.
- `scripts/synthesize.py` — checked the cited_files filter.
- `scripts/sweep-state.py` — checked cmd_pending_paths filter.
- `scripts/SWEEP-ARCHITECTURE.md` — spot-checked synthesis references.
- `scripts/fresh-synthesis.py` — checked for residual references.
- `scripts/deepseek-v4-assessment.md` — checked for residual references.
- `.claude/hooks/validate-commit-msg.py` — checked the touches_wiki check.
- `.claude/hooks/block-push-without-approval.py` — checked the daemon-trigger detection.
- `.claude/skills/walk-synthesis/SKILL.md` — read entirely (642 lines); largest gap.
- `.claude/skills/sweep-status/SKILL.md` — read entirely.
- `.claude/skills/sweep-catchup/SKILL.md` — read entirely.
- `.claude/skills/new-comp-experiment/SKILL.md` — spot-checked staging-paths.
- `synthesis/README.md` — verified spec §5.8 sections.
- `synthesis/strategic-reflections/README.md` — verified spec §5.8 sections.
- `synthesis/strategic-reflections/platform-framing-reframe.md` — content fidelity check.
- `synthesis/history/_pre-2026-05-08-archive.md` — content fidelity check.
- `CLAUDE.md` — checked synthesis references at lines 27, 130, 247.
- `README.md` — checked synthesis references at lines 6, 63, 86.
- `mkdocs.yml` — verified line 60 nav rewrite.
- `index.md` (repo root) — checked lines 15, 21, 176.
- `wiki/index.md` — verified line 84 rewrite (good).
- Local parser tests against `logs/v4-synthesis-2026-05-08-e842754.md`, `logs/v4-synthesis-2026-05-07-77d0f6e.md`, `logs/v4-synthesis-2026-05-06-121731c.md`, `logs/v4-synthesis-2026-05-05-3e928d3.md`.

---

**End of code review.**
