---
type: comp-review
comp: comp-044
source_commit: 50ecf5a9d8c3fcffbd0b2114e9fafd79ca907807
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-044

Current receipt: [`wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md`](../../wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md)

**Why action remains open:** Clean with limitations, with action required for non-blocking corpus maintenance. The implemented comp-044 arithmetic supports the narrow verdict: comp-019’s unconditional flat-dose classification is not robust once substrate occupancy and finite active window are applied under inherited priors. The result remains an internal consistency counterexample, not a replacement efficacy model. Corpus pages inspected are mostly faithful for comp-044, but unrelated and adjacent `validation-experiments.md` inconsistencies and a comp-019 invalidation-policy conflict still require correction.

## Required actions

1. Correct `wiki/validation-experiments.md` dashboard/protocol inconsistencies: reconcile §1.10 cost, §1.10 lane count/numbering, dashboard omissions for §§1.26–1.32, §1.22 cost/weeks, §1.20 matrix dimensions, §1.25 host-strain wording, and other shard-noted planning mismatches. Verification: dashboard and detailed sections agree.
2. Fix or justify `wiki/validation-experiments.md` §1.34 “yanthine” analyte. Verification: product/analyte panel uses correct chemical names.
3. Resolve the comp-019 invalidation-policy conflict noted in its prior push review: either align live-tree artifacts with the invalidated-COMP convention or document the exception. Verification: `computational-experiments.md` convention and comp-019 folder contents no longer conflict.
4. Preserve comp-044 forbidden inferences in any future propagation: no ΔSUA, dose sufficiency, topology/chassis winner, production target, safety, or probability claim from this artifact.
