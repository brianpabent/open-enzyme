---
type: comp-review
comp: comp-038
source_commit: 14833b44e90fe92f7aa6738a3f85edde188dabe9
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-038

Current receipt: [`wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/reviews/push-review.md`](../../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/reviews/push-review.md)

**Why action remains open:** Clean with limitations; action required for documentation polish, not for invalidating the bounded scientific result. The artifact supports a YELLOW result: no ready-to-adopt OE Tier 1/2 butyrate assay; De Baere HPLC-UV is a Tier 3 culture-supernatant transfer candidate; Gu electrochemical/ANN is a stool-specific Tier 2 candidate requiring complete-stack reproduction and external transfer. The result cannot support method adoption, clinical/gout claims, or exhaustive assay-landscape absence.

## Required actions

1. Update `outputs/summary.md` to include the Gu butyrate statistically nonzero negative bias, matching `results.json` and the interpretive page.
2. Reconcile `wiki/validation-experiments.md` §1.14 dashboard “4–6 weeks” with the detailed TBD-after-pilot timeline before using it in scheduling/cost rollups.
3. Preserve the regeneration warning in README/maintenance docs: any future regenerated outputs must include a newly reviewed `primary-source-verification-2026-07-24.json` equivalent and must not interpret mixed discovery/current output sets.
