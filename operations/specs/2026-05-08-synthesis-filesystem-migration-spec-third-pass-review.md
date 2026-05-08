---
title: "Spec Third-Pass Review — synthesis-filesystem-migration (2026-05-08)"
date: 2026-05-08
reviewer: Claude Sonnet 4.6 (independent third-pass review)
status: third-pass review
related:
  - 2026-05-08-synthesis-filesystem-migration.md
  - 2026-05-08-synthesis-filesystem-migration-spec-rereview.md
  - 2026-05-08-synthesis-filesystem-migration-spec-review.md
---

# Spec Third-Pass Review — synthesis-filesystem-migration (2026-05-08)

## Verdict

**APPROVED — implement as-is**

N1-N6 are all properly addressed. Line numbers for index.md and CLAUDE.md are exact. The chembl-discrepancy type is correctly added to §5.1. The §4.3 N1 sub-bullet clearly specifies the option-2 decision, names all 7 reference lines in chembl-refresh-prompt.md, and calls out the [skip-wiki-sweep] rationale update needed at line 127. The §5.4 N3 reword resolves the ambiguity. The §5.7 N4 git mv language is explicit and consistent with §5.10. The §8 N5 ordering rationale paragraph is one paragraph, clearly stated and sufficient. The §11 N6 retraction is correct — "second-pass spec review is NOT required" is gone, replaced by an honest characterization that the second pass validated the gate by finding N1. No new blockers were introduced by the second revision.

One minor gap found during verification (see Section D, item 1): the spec says "7 references at lines 18, 23, 26, 82, 84, 127, 141, 142" but that list contains 8 line numbers, not 7. The count is wrong but the line list itself is correct — grep confirms all 8 are real. This is a prose-count typo, not a scope gap. An implementer working from the line list will do the right thing. Not a blocker.

The success criterion 11 grep (`grep -rn "wiki/synthesis\.md\|synthesis-merge" scripts/ .claude/ README.md mkdocs.yml CLAUDE.md index.md`) will catch any remaining chembl-refresh-prompt.md references post-implementation, acting as the backstop the spec promises.

## Verification of N1-N6

**N1 — `scripts/chembl-refresh-prompt.md` handling: Properly addressed.**

The spec added a "Parallel workflows that write to `wiki/synthesis.md`" sub-bullet in §4.3 (line 98-99 of spec). It specifies:
- The decision (option 2 — direct write of `synthesis/queue/<date>-chembl-discrepancy-N.md` files)
- The "one per discrepancy finding" output model
- Explicit note that it does NOT go through `synthesis-emit-files.py`
- The `[skip-wiki-sweep]` rationale update needed at line 127
- The new `chembl-discrepancy` type added to §5.1 (confirmed: spec line 163)

Grep evidence:
```
grep -n "synthesis\.md" scripts/chembl-refresh-prompt.md → 8 hits at lines 18, 23, 26, 82, 84, 127, 141, 142
grep -n "chembl-discrepancy" operations/specs/2026-05-08-synthesis-filesystem-migration.md → hits at lines 99 and 163
```

One sub-issue: the spec says "7 references" but lists 8 line numbers. The line list is correct (grep-verified); the count in prose is a typo. Not load-bearing for implementation.

The spec does NOT specify the frontmatter/body structure for chembl-discrepancy files (as distinguished from the §5.4-specified daemon-emitted files). This is a mild underspecification — the implementer updating chembl-refresh-prompt.md will need to decide the format. In practice, the "one file per discrepancy finding, flat-list, not daemon's 7-section format" description is sufficient guidance for an implementer working from the existing prompt. This is a minor gap, not a blocker (the walkthrough flow treats chembl-discrepancy files identically to other queue files).

**N2 — index.md and CLAUDE.md enumeration: Properly addressed.**

Spec §4.5 now enumerates specific lines for both files. Grep verification of actual line numbers in current files:

```
grep -n "synthesis\.md" index.md → lines 15, 21, 176
grep -n "synthesis\.md" CLAUDE.md → lines 27, 130, 247
```

Spec claims: `index.md` lines 15, 21, 176; `CLAUDE.md` lines 27, 130, 247.

All six line numbers are correct. These are the only references in both files (no additional references missed). Full match.

**N3 — §5.4 body parenthetical reword: Properly addressed.**

Spec line 229 now reads: "Body: the Pass 2 item's full content with the `{{PEER-REVIEW}}` marker stripped, followed by the Pass 3 review blockquote. (Reworded per spec re-review N3 — original parenthetical was ambiguous.)"

The reworded sentence is clear: strip the marker, append the blockquote. The ambiguity in the original "verbatim, including the marker stripped" is resolved. Properly addressed.

**N4 — §5.7 git mv consistency with §5.10: Properly addressed.**

Spec §5.7 (line 288) now says: "the file moves (via `git mv` to preserve path history per re-review N4)..." and line 292 explicitly states "Path preservation: full content stays git-tracked; only path changes (consistent with §5.10 done/_archive/ rule)."

The cross-reference to §5.10 is explicit. Both sections now use the same preservation language. Properly addressed.

**N5 — §8 step ordering rationale: Properly addressed.**

Spec added a "Step ordering rationale (clarified per spec re-review N5)" paragraph at the top of §8 (line 422). It explains:
- Why workflow YAML lands last (old `synthesis-merge.py` still on disk ensures no half-state)
- Why cross-link cleanup lands before script writing
- Why deletion is the atomic last step

The note also implicitly addresses N5's specific observation about why the ordering "works" even if a daemon push fires mid-transition. Properly addressed.

**N6 — §11 over-confidence retraction: Properly addressed.**

The §11 first-pass entry now says (line 536): "Status after revision: spec is approvable for implementation contingent on second-pass review. (The original closing line 'second-pass spec review is NOT required' was retracted per re-review N6 — it was the spec author's self-assessment, not the reviewer's; the second pass DID surface a real critical finding (N1 chembl-refresh-prompt.md), validating the gate.)"

The over-confident claim is gone. The characterization that the second-pass "validated its own value" is accurate. Properly addressed.

## Other parallel workflows besides chembl-refresh

Four `.github/workflows/` files exist: `wiki-sweep.yml`, `chembl-refresh.yml`, `deploy-docs.yml`, `sweep-watchdog.yml`.

Grep check:
```
grep -rn "synthesis\.md" .github/workflows/ → hits only in wiki-sweep.yml (10 hits)
grep -n "synthesis" .github/workflows/chembl-refresh.yml → no hits
grep -n "synthesis" .github/workflows/sweep-watchdog.yml → no hits
```

`chembl-refresh.yml` invokes `scripts/chembl-refresh-prompt.md` via `cat scripts/chembl-refresh-prompt.md` at runtime — so the workflow YAML itself does not contain synthesis.md references, and does not need updating. Only `chembl-refresh-prompt.md` needs updating, which the spec covers.

No other parallel workflows writing to `wiki/synthesis.md` are present. The spec's coverage is complete on this dimension.

## New issues introduced by the second revision (if any)

**Item 1 — Minor prose typo in §4.3 N1 sub-bullet: reference count "7" should be "8".**

The spec's §4.3 N1 sub-bullet reads: "7 references at lines 18, 23, 26, 82, 84, 127, 141, 142."

That list has 8 line numbers (18, 23, 26, 82, 84, 127, 141, 142 = 8 entries). Grep confirms all 8 are real hits:
```
grep -c "synthesis\.md" scripts/chembl-refresh-prompt.md → 8
```

The error is "7" vs "8" in the prose count. The actual line list is correct. An implementer will follow the line list. Not a blocker; the success criterion 11 grep catches any missed lines post-implementation regardless.

**Item 2 — chembl-discrepancy file format underspecified (minor).**

The §4.3 N1 sub-bullet specifies the decision (direct write, one file per discrepancy) and the filename pattern (`synthesis/queue/<date>-chembl-discrepancy-N.md`). The §5.4 emitted-file frontmatter spec applies to daemon-emitted files only — it explicitly notes chembl-discrepancy is "produced by chembl-refresh-prompt.md direct-write, not by `synthesis-emit-files.py`."

The chembl-discrepancy file format (frontmatter fields, body structure) is not specified anywhere in the spec. The implementer updating `chembl-refresh-prompt.md` must invent this. The walkthrough skill will need to parse or at minimum read these files, so the format does matter.

The impact is limited: the walkthrough reads chembl-discrepancy files the same way it reads any queue file (read, action, mv to done). The only functional requirement is that the file be human-readable and have a `type: chembl-discrepancy` frontmatter field for classification. The §5.1 naming convention is sufficient for the implementer to make a reasonable choice without spec guidance.

Classification: minor underspecification, not a blocker. An implementer can make a defensible format choice. If format consistency with daemon-emitted files is desired, a future spec can standardize it after the first quarterly refresh.

**No other new issues found.** The second revision added approximately 200 lines. Cross-references introduced are internally consistent. No scope creep beyond the N1-N6 remit. No contradictions between newly-added sections and pre-existing sections.

## Verification of cited line numbers

Spec §4.5 cites:
- `index.md` lines 15, 21, 176 — **all correct** (grep-verified, exact match)
- `CLAUDE.md` lines 27, 130, 247 — **all correct** (grep-verified, exact match)

Both files have exactly three `synthesis.md` references each. The spec enumerates all of them. No references missed.

## Files I read for this review

- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/operations/specs/2026-05-08-synthesis-filesystem-migration.md` — the twice-revised spec; primary review target.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/operations/specs/2026-05-08-synthesis-filesystem-migration-spec-rereview.md` — second-pass review report; source of N1-N6 to verify.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/operations/specs/2026-05-08-synthesis-filesystem-migration-spec-review.md` (first 50 lines) — first-pass review; context for Findings 1-18.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/scripts/chembl-refresh-prompt.md` — verified N1 resolution; confirmed 8 synthesis.md references at lines 18, 23, 26, 82, 84, 127, 141, 142; confirmed Pass 4 prepend behavior.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/index.md` — verified spec's claimed line numbers 15, 21, 176.
- `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/CLAUDE.md` — verified spec's claimed line numbers 27, 130, 247.
- `.github/workflows/` (all four files) — verified no other workflow beyond wiki-sweep.yml and chembl-refresh.yml touches synthesis.md; confirmed chembl-refresh.yml invokes prompt via `cat` and doesn't itself contain synthesis.md references.
- `grep -rn "synthesis\.md" .github/workflows/` — no hits outside wiki-sweep.yml.
- `grep -rn "wiki/synthesis\.md\|synthesis-merge" scripts/ .claude/ README.md mkdocs.yml CLAUDE.md index.md` — ran the success criterion 11 grep; confirmed chembl-refresh-prompt.md is captured by it.
