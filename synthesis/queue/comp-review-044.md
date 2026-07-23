---
type: comp-review
comp: comp-044
source_commit: 3ede1f4d7cc0d4978138b0b5e0a7cea487c0a075
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-044

Current receipt: [`wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md`](../../wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md)

**Why action remains open:** **Action required, but not blocked.** The core comp-044 artifact supports only the narrow verdict that comp-019’s unconditional flat-dose uricase regime is not robust to adding substrate occupancy and finite exposure-window diagnostics. The experiment does **not** establish physiological efficacy, dose sufficiency, topology, chassis, safety, or serum-urate effect. Corpus propagation is mostly faithful, but a provenance-label correction is needed in `wiki/etc/GRAPH.md`, and carryover non-comp-044 validation/wiki hygiene issues remain outside the safe synthesis lane.

## Required actions

1. In `wiki/etc/GRAPH.md`, relabel the comp-044-to-§1.33 relationship to separate “deterministic computational audit” from the downstream “experimental-routing inference.” Verification: graph text no longer implies comp-044 itself is mechanistic biological validation.
2. Keep propagation receipts/summaries scoped to: “legacy flat-dose robustness not supported under comp-044 diagnostics.” Verification: no page uses comp-044 for ΔSUA, dose sufficiency, genotype order, topology/chassis winner, production target, or safety conclusion.
3. Track non-comp-044 carryover wiki hygiene issues separately, especially the `open-questions.md` “yanthine” biomarker wording and unrelated `validation-experiments.md` methodological/budget inconsistencies. Verification: corrected or explicitly justified in their owning reviews; not synthesized as comp-044 evidence.
