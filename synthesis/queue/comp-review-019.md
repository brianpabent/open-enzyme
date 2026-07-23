---
type: comp-review
comp: comp-019
source_commit: 57c4c1a07de87cd3d6748ec9f51d6fae7e35316e
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-019

Current receipt: [`wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/reviews/push-review.md`](../../wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/reviews/push-review.md)

**Why action remains open:** Quantitative verdict invalid. The live corpus correctly retires comp-019 as a non-runnable invalidated tombstone: Phase B omitted physiological substrate occupancy and finite exposure, and none of its numerical outputs or decisions may be used. Action remains required for minor but material tracking/surface consistency issues: “SUPERSEDED” versus `invalidated_tombstone` status vocabulary, and a methodology page retaining “Monte Carlo n=5000” without equally prominent non-decision historical framing.

## Required actions

1. In `wiki/computational-experiments.md`, reconcile comp-019 status wording with the artifact status `invalidated_tombstone`, or explicitly define “SUPERSEDED” as non-runnable invalidated tombstone for eligibility purposes. Verification: index, tombstone, and interpretive page use compatible status semantics.
2. In `wiki/etc/autonomous-screening-methodology.md`, revise the comp-019 “Monte Carlo n=5000” entry to state it is historical invalidated implementation detail and not decision-grade evidence. Verification: no methodology table can be read as preserving active comp-019 quantitative support.
3. Do not propagate any comp-019 numerical outputs, including via comp-031 or portfolio summaries. Verification: searches for comp-019-derived ΔSUA, −0.83 mg/dL anchors, capacity ratios, flat-dose classifications, genotype ordering, dose/yield, topology/chassis, or safety claims either find none or label them invalidated.
