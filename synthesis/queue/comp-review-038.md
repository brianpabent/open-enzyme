---
type: comp-review
comp: comp-038
source_commit: 1b57f9c213d67eda156ac41119428b0a09555ea9
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-038

Current receipt: [`wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/reviews/push-review.md`](../../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/reviews/push-review.md)

**Why action remains open:** Action required, but the bounded scientific result is usable with warnings. COMP-038 correctly supports a YELLOW assay-method conclusion: no ready Tier 1/Tier 2 Open Enzyme butyrate assay; HPLC-UV is a Tier 3 culture-supernatant transfer candidate; Gu electrochemical/ANN is a stool-specific Tier 2 candidate not yet adopted. Required corrections are provenance/link hygiene and reproducibility guardrails, not reversal of the core verdict.

## Required actions

1. Correct the Gu citation link target on `wiki/tier-2-butyrate-assay-audit-computational.md` and `wiki/validation-experiments.md`; verification criterion: PMID link resolves to PubMed for PMID 42041444 or the label explicitly says PMCID/PMC when linking to PMC.
2. Add a maintenance guard or documented workflow separation for legacy `analyze.py`; verification criterion: running discovery/packet preparation cannot silently overwrite `results.json`, `summary.md`, or the 2026-07-24 verification-controlled state without an explicit current-output regeneration mode.
3. Update the dry-run/lifecycle expected-output check to include `outputs/primary-source-verification-2026-07-24.json`; verification criterion: artifact integrity fails if the controlling verification JSON is absent.
4. In any future propagation of Gu performance numbers, include “within-study n=30, exact stack, statistically nonzero bias, no independent external transfer”; verification criterion: no index/priority table uses R² alone as adoption evidence.
