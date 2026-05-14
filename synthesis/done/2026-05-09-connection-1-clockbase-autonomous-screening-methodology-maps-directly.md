---
type: connection
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 1
global_index: 1
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# ClockBase autonomous screening methodology maps directly onto comp-NNN strain-engineering search spaces.

1. **ClockBase autonomous screening methodology maps directly onto comp-NNN strain-engineering search spaces.** *Supported*. `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `autonomous-screening-methodology.md`, `computational-experiments.md`
   - *Page-pair linkage:* These two pages currently have **zero cross-references** to each other — a genuinely weakly-connected pair. No wiki entry proposes applying ClockBase’s exhaustive ranking to Open Enzyme’s own computational pipeline.
   - *Why It Matters:* ClockBase achieved discovery by ranking **~43,602 intervention–control comparisons** — roughly the same scale as the combinatorial space for *A. oryzae* expression cassette optimization (~43,200 combos of promoter × signal peptide × codon variant × secretion scaffold). The transferable pattern (composite scoring across orthogonal predictors, hypothesis-then-verify, N-of-M concordance thresholds) is directly applicable to comp-NNN cassette design. Open Enzyme currently designs cassettes one at a time; this connection suggests a **single comp-NNN run could rank thousands of designs via a composite stability-secretion-codon score before synthesising any DNA**. The verification-agent second pass (Claude → DeepSeek, per multi-vendor discipline) would mirror ClockBase’s literature re-check.
   - *Suggested Action:* Draft a comp-NNN brief (`comp-021`) that applies the ClockBase ranking pattern to the *A. oryzae* uricase-expression cassette search space. Use ≥3 orthogonal scoring models (AlphaFold pLDDT, chaperone load per the orthogonal-stacking framework, codon adaptation index, mRNA structure) and report composite scores with explicit concordance thresholds for wet-lab promotion. Cost: in silico only; timeline: 2–4 weeks.

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` The central “zero cross-references / no wiki entry proposes this” claim is wrong: `computational-experiments.md` already has a `comp-NNN verification agent (ClockBase hypothesis-then-verify pattern)` section that cites `autonomous-screening-methodology.md`, and `autonomous-screening-methodology.md` already makes the cassette-design transfer explicit with the ~43,200 promoter × signal peptide × codon variant × secretion scaffold search-space analogy, composite orthogonal scoring, and N-of-M concordance framing. The proposed cassette-ranking workflow is sound, but this is already a first-class methodology entry, not a newly discovered weakly connected pair; any emitted item should be reframed as implementation/prioritization rather than novelty.

---

## ✓ Actioned 2026-05-14

The ClockBase ↔ cassette-design connection itself is already a first-class entry in [`autonomous-screening-methodology.md`](../../wiki/autonomous-screening-methodology.md) (43,602 comparisons → ~43,200 cassette combos, composite orthogonal scoring, N-of-M concordance) and the hypothesis-then-verify pattern is documented in [`computational-experiments.md`](../../wiki/computational-experiments.md) §Infrastructure. Pass 3's RESTATEMENT verdict was correct on that point.

What was **not** documented was an actual queued comp instantiating the pattern. Closed by queuing **comp-022** ("ClockBase-style exhaustive combinatorial ranking of *A. oryzae* uricase expression cassettes (in silico)") in [`computational-experiments.md`](../../wiki/computational-experiments.md) §Planned Analyses. Brief specifies: ~43,200 promoter × signal peptide × codon variant × secretion scaffold combinations, four orthogonal scoring models (AlphaFold pLDDT + chaperone load + codon adaptation index + mRNA structure), N-of-M concordance ≥4/5 with calibration against retrospective comp-001 through comp-014 cassette-design outcomes (per the open methodology question in `autonomous-screening-methodology.md`), verification-agent pass before commit.

Also reserved comp-021 in the Planned Analyses table for the existing "compound × upstream-complement chokepoint × matched-assay-format mapping" Phase 2 candidate (already referenced at `upstream-complement-verification-rerun-computational.md` line 262), preventing ID collision flagged by Pass 3.

Decision deferred per Brian 2026-05-14: comp-022 brief is queued now, actual run gated on later items in this walk possibly refining the brief (e.g., Item 11 [open-question-1] on N-of-M concordance threshold calibration). Closes alongside [2026-05-09-experiment-1](./2026-05-09-experiment-1-clockbase-style-exhaustive-combinatorial-ranking-of-a.md) and [2026-05-09-priority-action-1](./2026-05-09-priority-action-1-draft-a-comp-nnn-brief-for-clockbase-style-exhaustive.md) which propose the same comp.
