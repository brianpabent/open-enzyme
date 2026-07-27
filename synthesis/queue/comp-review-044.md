---
type: comp-review
comp: comp-044
source_commit: 8ddcf2c354b5478c6e31a74081f68399e2c8f1f2
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-044

Current receipt: [`wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md`](../../wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md)

**Why action remains open:** Action required, but the quantitative COMP-044 verdict is not invalid. The computation faithfully supports a narrow negative conclusion: COMP-019’s unconditional saturated/flat-dose classification is not robust once finite substrate occupancy and finite active windows are imposed. The model remains a fixed-concentration capacity diagnostic against a daily-flux denominator, not a physiologic luminal reaction-rate, serum-effect, or safety model. Required actions are documentation cleanup: reconcile conflicting feasibility-score references in `open-questions.md` and tighten one comp-031 invalidation wording so it does not overstate COMP-044’s blast radius.

## Required actions

1. In `wiki/open-questions.md`, reconcile the gut-lumen uricase feasibility references: either remove numeric score duplication or point to the current owner surface with one current value. Verification: no remaining inconsistent 5.5/10 vs 6/10 references for the same COMP-044/cross-validation claim.
2. In `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md`, tighten the invalidation sentence to say COMP-044 invalidates COMP-031’s inherited reliance on COMP-019’s unconditional flat-dose/saturation robustness, not all possible UOX regimes or all UOX/PDB complementarity. Verification: wording preserves adjacent conjectures and points to §§1.33/1.34/1.37 for replacement evidence.
3. Before using COMP-044 numbers for planning rather than audit, primary-source verify 8.3 U/mg activity, Km range, pH multiplier, 2–4 h active window, and 233 mg/day denominator. Verification: each value has a directly checked source and context-matched unit/assay notes.
