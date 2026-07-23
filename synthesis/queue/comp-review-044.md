---
type: comp-review
comp: comp-044
source_commit: 2f2b3b73e8a77f78f75ece3bce11f9a95b7555b5
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-044

Current receipt: [`wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md`](../../wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md)

**Why action remains open:** Clean with limitations for the comp-044 scientific result: the code and summaries support the narrow conclusion that comp-019’s unconditional saturated, 24-hour flat-dose classification is not robust once substrate occupancy and a finite active window are applied under inherited priors. Action is still required because the broad `validation-experiments.md` surface contains unrelated material QA issues found during full-page audit; those do not block bounded comp-044 propagation.

## Required actions

1. Triage `wiki/validation-experiments.md` non-comp-044 QA issues found during full-page audit, especially the 16S-versus-fungal-dominance error and threshold/provenance ambiguities. Verification criterion: affected sections either corrected, explicitly marked provisional, or moved to a separate QA issue without relying on them as binding gates.
2. When propagating comp-044, include the forbidden-inference boundary verbatim or equivalently: no serum effect, dose, genotype order, true physiological regime, topology/chassis selection, production sufficiency, safety, or probabilistic grid interpretation.
