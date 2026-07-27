---
type: comp-review
comp: comp-014
source_commit: 510fb3a3ece81d906e50d1fa5fbc98a720b0da02
propagation_eligibility: eligible_with_warning
synthesis_eligibility: blocked
---

# Current independent artifact review: comp-014

Current receipt: [`wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/reviews/push-review.md`](../../wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/reviews/push-review.md)

**Why action remains open:** Action required. The current reader-facing COMP-014 boundary is mostly corrected: it presents a partial, non-authoritative, unranked lead inventory and retires Phase 6. However, retained generated outputs still contain obsolete ranks, operational “what to buy”/SOP-style language, inconsistent quantitative cost/yield arithmetic, permissive “toxicity pass” semantics, query-hint species provenance, and mixed endpoint/polarity target mappings. These cannot support synthesis or automated prioritization. Corrective propagation is safe only to reinforce the quarantine.

## Required actions

1. Add or strengthen quarantine banners inside retained Phase 3/4/5/7 generated outputs that still contain ranks, KEEP/DROP/Tier/readiness, “recommended,” “optimal,” “what to buy,” SOP, cost, or chassis language; verification: no historical output can be mistaken for current decision authority.
2. Correct or annotate known mapping/identity defects: OAT4 ChEMBL mismatch, PPARα/PPARγ label mismatch, ATP/adenylosuccinate-like record, DPPH-under-XO row, and Phase 2a 4-versus-5 row boundary.
3. Define table semantics for future use: `toxicity_filter_pass` as retained-for-review, query-hint as non-provenance, and full-InChIKey versus 2D/name deduplication.
4. Prevent synthesis from Phase 7 production/cultivation outputs until cost/yield arithmetic, substrate comparator, strain/material identity, and biosafety constraints are recalculated from primary sources.
5. Inspect linked validation/SOP pages for accidental propagation of Phase 6/7 rankings, purchase guidance, or wet-lab priorities.
