---
type: comp-review
comp: comp-016
source_commit: 14833b44e90fe92f7aa6738a3f85edde188dabe9
propagation_eligibility: eligible_with_warning
synthesis_eligibility: blocked
---

# Current independent artifact review: comp-016

Current receipt: [`wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/reviews/push-review.md`](../../wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/reviews/push-review.md)

**Why action remains open:** Action required. The repaired COMP-016 artifact supports a narrow fixed-inventory result: no record in the 17-record inventory directly demonstrates androgen-driven suppression of intestinal ABCG2; this is not a universal literature absence, not a healthy-human sex-stratification result, and not a quantitative physiology result. The core artifact is bounded and mostly internally coherent, but downstream wiki text overstates mechanistic absence/legacy evidence and imports adjacent quantitative claims without adequate provenance separation. Synthesis should be blocked until those surfaces are corrected.

## Required actions

1. In `wiki/abcg2-modulators.md`, revise the ChIP-seq/ARE sentence to avoid claiming published-study absence or promoter-location nonfinding unless a citable ChIP-seq/promoter source is added and verified. Verification criterion: wording is limited to “not established by COMP-016 fixed inventory” or independently sourced.
2. In `wiki/abcg2-modulators.md`, remove or relabel Jeong 2015 as a COMP-016 legacy-adjacent, non-intestinal lead rather than “closest mechanistic anchor,” unless primary-source verification is added outside COMP-016. Verification criterion: no legacy-summary row carries mechanistic authority.
3. In `wiki/abcg2-modulators.md`, attach the 84.2% modeled jejunal urate-flux number to the correct COMP-017/source-workbook provenance or remove it from the COMP-016-context paragraph. Verification criterion: readers can distinguish COMP-016 Western-only corrected anchor from COMP-017 flux/source verification.
4. Update `outputs/results.json` generation or schema so `record_classifications` include `verification_tier`, matching the summary’s auditability. Verification criterion: rerendered `results.json` exposes verification tier for each classification row.
5. Do not enable synthesis from COMP-016 until the above summary-fidelity corrections are reviewed.
