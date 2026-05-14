---
type: experiment
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 1
global_index: 7
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# ClockBase-style exhaustive combinatorial ranking of *A. oryzae* uricase expression cassettes (in silico).

1. **ClockBase-style exhaustive combinatorial ranking of *A. oryzae* uricase expression cassettes (in silico).** Cost: ~$0. Time: 2–4 weeks. Decides: which cassette designs (promoter × signal peptide × codon variant × secretion scaffold) to synthesise for §1.9, replacing the current one-at-a-time design with a ranked shortlist backed by orthogonal scoring models. Directly instantiates Connection #1 above. Models: AlphaFold pLDDT, chaperone-load per the orthogonal-stacking framework, codon adaptation index, mRNA secondary structure. Concordance threshold ≥4/5 models for wet-lab promotion.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The action is correct and high-leverage even though the methodology is already documented: `autonomous-screening-methodology.md` explicitly analogizes ClockBase’s 43,602 intervention-control comparisons to ~43,200 cassette combinations and recommends composite orthogonal scoring plus N-of-M concordance, but that pattern has not yet been instantiated as a queued uricase-cassette comp run. Use the next free comp ID rather than hard-coding `comp-021`, because the corpus already uses “comp-021 candidate” language elsewhere for upstream-complement assay-format mapping and the Pass 2 log also assigns comp-021 to cns1+cns2.

---

## ✓ Actioned 2026-05-14

Queued as **comp-022** in [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) §Planned Analyses during Item 1's walk (commit c08c4cb). Brief specifies: ~43,200 promoter × signal peptide × codon variant × secretion scaffold combinations; four orthogonal scoring models (AlphaFold pLDDT + chaperone load per `chaperone-orthogonal-stacking.md` + codon adaptation index + mRNA secondary structure); N-of-M concordance ≥4/5 with calibration against retrospective comp-001 through comp-014 outcomes (per the open methodology question in `autonomous-screening-methodology.md`); verification-agent pass before commit per the existing infrastructure proposal in the same page.

ID collision Pass 3 flagged (avoid comp-021) honored: comp-021 reserved in the same walk for the existing "compound × upstream-complement chokepoint × matched-assay-format mapping" Phase 2 candidate from comp-020.

Brief queued; run deferred until later walkthrough items have a chance to refine it (e.g., Item 11 [open-question-1] on N-of-M concordance threshold calibration). Closes alongside [2026-05-09-connection-1](./2026-05-09-connection-1-clockbase-autonomous-screening-methodology-maps-directly.md) and [2026-05-09-priority-action-1](./2026-05-09-priority-action-1-draft-a-comp-nnn-brief-for-clockbase-style-exhaustive.md).
