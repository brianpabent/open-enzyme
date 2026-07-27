---
type: comp-review
comp: comp-045
source_commit: 00e535127beae0df3362f88654ddc323d269aba5
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-045

Current receipt: [`wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/reviews/push-review.md`](../../wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/reviews/push-review.md)

**Why action remains open:** Action required, but not because the biological conclusion is overstated in the inspected comp-045 surfaces. The committed outputs and main wiki propagation correctly preserve the narrow result: `CANDIDATE_LAYOUT_GENERATED`, biological verdict `NOT_EVALUATED`, and wet-lab readiness blocked. Required actions remain for implementation/provenance hygiene: the gate is documented in the wrapper command rather than enforced by `analyze.py`, and load-bearing source facts are citation/narrative assertions rather than directly verifiable source excerpts or bibliographic records.

## Required actions

1. Update the comp-045 README or implementation contract: either add manifest/gate enforcement to `analyze.py`, or state plainly that gate enforcement is external to the documented wrapper command and direct `analyze.py` execution is not gate-safe. Verification: direct execution behavior and README wording no longer conflict.
2. Add directly inspectable provenance support for load-bearing source facts, or downgrade wording to “citation asserted/not independently verified in artifact.” This applies to PULSE/Gao topology scope and 250 µM concentration, Zhao oxygen scope, Li related-precedent scope, and the 0.59 µM terminal-ileal concentration conversion. Verification: source excerpts/bibliographic metadata or explicit unverified-provenance labels are present.
3. Before any wet-lab execution from this layout, bind exact active/inactive UOX identities, inactive mutation, expression/localization equivalence criteria, constructs, stocks, cell normalization, dissolved-oxygen targets, sampling/aliquot/destructive-readout plan, and assay quantification at 0.59 µM. Verification: a new reviewed lifecycle or protocol addendum resolves all blockers and regenerates the layout if the qualified set changes.
