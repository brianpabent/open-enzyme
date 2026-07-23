---
type: comp-review
comp: comp-019
source_commit: 6efddd88c579c3827c6fe4a8664e342da976df7c
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-019

Current receipt: [`wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/reviews/push-review.md`](../../wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/reviews/push-review.md)

**Why action remains open:** Action required, but the bounded current result is usable with warnings. The live comp-019 artifact correctly retires the old model: Phase B did not use physiological substrate occupancy/Km and assumed saturated 24 h activity, so the quantitative verdict is invalidated. Current pages mostly enforce that no comp-019 ΔSUA, dose, genotype order, efficacy, safety, or topology claim survives. Required actions are corpus-maintenance issues: add comp-045 to the comp-019 README current evidence-owner/replacement list, and close existing UOX-related validation/provenance inconsistencies before any wider synthesis.

## Required actions

1. Update `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` current evidence owners to include comp-045 / `uricase-topology-oxygen-peroxide-design-computational.md`; verify the README and computational index list the same live UOX evidence surfaces.
2. Resolve the open comp-044 maintenance actions touching UOX propagation: validation dashboard/protocol inconsistencies, validation §1.34 “yanthine” analyte naming/justification, and the comp-019 invalidation-policy conflict; verify by re-reading affected validation and interpretive pages.
3. Do not propagate any comp-019-derived quantitative numbers, genotype ordering, dose, topology, or safety conclusions into synthesis; automated propagation may only carry the tombstone and bounded search observation.
