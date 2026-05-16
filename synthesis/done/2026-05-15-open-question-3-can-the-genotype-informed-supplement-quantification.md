---
type: open-question
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 3
global_index: 12
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Can the genotype-informed supplement quantification workflow (`self-experiment-protocol.md` §12) be validated in a small multi-user pilot (N=5–10) before the larger H09 community-fermentation trial?

3. **Can the genotype-informed supplement quantification workflow (`self-experiment-protocol.md` §12) be validated in a small multi-user pilot (N=5–10) before the larger H09 community-fermentation trial?** The workflow is specified but untested. A pilot where 5–10 users genotype → select a compound → produce or source it → Tier 2 batch QC → track a biomarker would surface the operational failure modes (user error in Tier 2 assay, batch variability exceeding the ±20% Tier 2 tolerance, genotype misclassification from consumer panels) before the larger H09 trial commits. Cost: ~$2,000–5,000 (genotyping + reagents + coordination). This is the cheapest empirical test of the closed-loop pipeline and directly de-risks H09's cross-user CV claim.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the right pilot before H09-scale community reliability work: `self-experiment-protocol.md` §12 defines the closed-loop workflow, `quantification-ladder.md` defines the QC discipline, and H09 explicitly depends on multi-user batch consistency rather than single-user feasibility. A 5–10 user pilot is cheap relative to the information it yields about assay error, batch CV, and user adherence failure modes.

---

## ✓ Actioned 2026-05-16

Added entry to [`wiki/open-questions.md`](../../wiki/open-questions.md) under the existing "comp-018 Phase 2 follow-ups" section (sibling of the dietary rosmarinic acid PK question from Item 19). Names the N=5–10 pilot scope, cost anchor (~$2,000–5,000), practical constraints (IRB review, recruitment, coordination overhead), and cross-references the [`genotype-informed-supplement-workflow.md`](../../wiki/genotype-informed-supplement-workflow.md) Open follow-ups subsection where this pilot already lives as the natural next-step gate before H09.

No pilot execution today — this is real human-subjects work requiring IRB review + recruitment + project commitment, all out of scope for a sweep walkthrough. No protocol drafting today — protocol gets drafted when pilot is scheduled, not before it's approved as a project. The Open Question is now tracked at the canonical surface.
