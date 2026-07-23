---
type: comp-review
comp: comp-019
source_commit: 75f4e13aa65eb3b1e0a9f904c38039ea077c5195
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-019

Current receipt: [`wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/reviews/push-review.md`](../../wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/reviews/push-review.md)

**Why action remains open:** **Action required, but bounded propagation/synthesis remains eligible with warning.** The active corpus now correctly treats comp-019 Phase B as invalidated and non-decision-usable. The only surviving result is a bounded Phase A negative search: no Q141K-stratified uricase clinical outcome or direct human ΔSUA-per-luminal-uricase-unit measurement was found in searched sources as of 2026-05-08. Required action is process/documentation cleanup: the computational-experiments policy says fully invalidated COMPs retain only a hash-bound invalidation record and are not rerun, while comp-019 retains guarded executable reproduction scripts and outputs.

## Required actions

1. Reconcile `wiki/computational-experiments.md` policy with comp-019’s retained guarded executable scripts: either revise the convention to allow clearly marked archival reproduction or move comp-019 to a non-rerunnable hash-only record. Verification: no reader-facing contradiction remains.
2. Keep all comp-019 numerical outputs marked provenance-only in any future propagation. Verification: no page cites comp-019 ΔSUA, capacity ratios, genotype ordering, flat-dose status, yield sufficiency, or trial design as evidence.
3. If UOX validation sections are used operationally, resolve the UOX-adjacent `validation-experiments.md` protocol/dashboard ambiguities identified by shards before execution scheduling. Verification: queue, dependencies, assay panels, and success criteria are internally consistent.
