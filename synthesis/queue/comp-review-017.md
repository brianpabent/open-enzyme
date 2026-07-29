---
type: comp-review
comp: comp-017
source_commit: 14833b44e90fe92f7aa6738a3f85edde188dabe9
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current independent artifact review: comp-017

Current receipt: [`wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/reviews/push-review.md`](../../wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/reviews/push-review.md)

**Why action remains open:** Action required. The core scientific result is bounded and usable: COMP-017 did **not** extract direct sex-stratified healthy-human intestinal GTEx/HPA values and therefore did **not** test the prespecified 1.5× baseline threshold. The correction of Hoque/Liu/Slepnev/MacLean evidence contexts is mostly faithful. Required actions are documentation/contract issues: dependent-page ownership drift, inconsistent provenance-tier reporting, missing machine-output propagation of a forbidden inference, and non-executable provenance/gate dependencies.

## Required actions

1. In `wiki/abcg2-modulators.md` and `wiki/androgen-urate-axis.md`, replace extended COMP-017-derived exposition with compact local correction/status plus link to the COMP-017 evidence home. Verification: dependent pages no longer duplicate source-by-source audit narrative or portfolio implications.
2. Reconcile Hoque provenance wording across `inputs/provenance.md`, `inputs/full_text_extract.json`, `outputs/results.json`, and `outputs/summary.md`. Verification: outputs either report the full checked-source set or explicitly say why a lower/conservative verification tier is emitted.
3. Add a machine-readable and human-visible forbidden-inferences section to generated outputs, including “pan-male responder rule.” Verification: rerendered `results.json`/`summary.md` carry the full input forbidden-inference list or an explicitly validated subset.
4. Close the provenance-validation gap: either make `analyze.py` validate required provenance/forbidden-inference fields or document that provenance is manually reviewed and outside deterministic reproduction. Verification: code or README states the contract unambiguously.
5. Clarify the Gate 1 reproduction dependency by linking or naming the hash-bound Gate 1 receipt, or remove it from the executable reproduction contract. Verification: a reader can tell what must exist before rerunning.
