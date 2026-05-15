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

---

## ✓ Actioned 2026-05-15

Pass 3 was right that `validation-experiments.md` §1.1 line 102 already had the Ginkgo cell-free pre-gate option — no addition needed.

But Item 8 (immediately prior in this walk) just landed the **skip-for-now decision** on `ginkgo-cloud-lab-evaluation.md`. Without propagation, the two pages would self-contradict: the evaluation page now says "skip the $39 cell-free for now," while §1.1 still actively recommended "run the $39 cell-free as a pre-gate."

**Propagation shipped:** `wiki/validation-experiments.md` §1.1 line 102 reworded with the same "deferred 2026-05-13 / priority-stack decision" framing used in the evaluation page TL;DR. The pre-gate option itself is preserved (rationale, negative/positive decision logic, link to source) — only the status is changed from active recommendation to deferred-with-revisit-trigger. Cross-link back to `ginkgo-cloud-lab-evaluation.md` for full context.

The two pages are now consistent. Pass 3's "the experiment is sound, but..." verdict landed cleanly.
