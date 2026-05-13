---
type: experiment
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 1
global_index: 6
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# Run the Ginkgo $39 cell-free pre-gate on the lead uricase variant.

1. **Run the Ginkgo $39 cell-free pre-gate on the lead uricase variant.** Cost: $39. Time: ~1 week. Decides: whether the designed uricase ORF translates and folds in a cell-free lysate before committing to fungal-host expression. This is the cheapest possible killshot for a uricase variant — a negative result at $39 saves the $2,000–3,000 full gene-synthesis + transformation pipeline of `validation-experiments.md` §1.1. Already recommended in `wiki/ginkgo-cloud-lab-evaluation.md`; should be added as a pre-gate option in `validation-experiments.md` §1.1. (Note: only appropriate for non-glycosylated, non-disulfide-bonded constructs — uricase is a strong fit; DAF/CD55 is a weak fit per the evaluation.)

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` The experiment is sound, but the page-state claim is wrong: `validation-experiments.md` §1.1 already contains a subsection titled "Pre-gate option — Ginkgo Cloud Lab cell-free expression ($39/protein, ~5–10 day turnaround)" with exactly the lead-uricase-variant rationale and the negative/positive decision logic. Keep the recommendation to run the $39 uricase cell-free test, but delete the claim that §1.1 still needs this option added.
