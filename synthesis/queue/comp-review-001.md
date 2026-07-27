---
type: comp-review
comp: comp-001
source_commit: 0ef99dcc9102323608fc4e5384e09617e95e17e8
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-001

Current receipt: [`wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/reviews/push-review.md`](../../wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/reviews/push-review.md)

**Why action remains open:** Action required, but the scientific result is usable only in a narrow corrective/proxy scope. The implementation appears to answer the stated narrow question—enumerating Q00511 adjacent-pair matches to three fixed legacy filters and reporting local AlphaFold pLDDT context—but it does not and cannot resolve protease stability, cleavage, accessibility, retained activity, or shio-koji survival. One reader-facing issue remains: the interpretive page’s registry anchor is likely stale/mismatched and should be corrected. Primary sources were not independently re-fetched in this review.

## Required actions

1. Fix the registry link in `wiki/uricase-protease-stability-computational.md` so it resolves to the actual COMP-001 heading in `wiki/computational-experiments.md`; verify by checking the rendered anchor or using a stable file/folder link if heading slugs remain fragile.
2. Preserve propagation limits in any downstream synthesis: COMP-001 may be cited only for deterministic fixed-filter match counts and pLDDT context, never as protease stability, ferment survival, or benchmark evidence.
3. If COMP-001 source provenance becomes load-bearing beyond committed-input reproducibility, independently re-fetch/verify UniProt Q00511 and AlphaFold `AF-Q00511-F1-model_v6` rather than relying on citation strings.
