> **INVALIDATED TOMBSTONE — NOT RUNNABLE.** The retired artifact converted heterogeneous and estimated HDAC evidence plus exposure surrogates into a quantitative candidate ranking that could not support the claimed wet-lab priority.

# comp-007 — Food-Associated HDAC-Directed Candidate Screen

**Status:** Invalidated for candidate ranking, composite scores, confidence-ranked verdicts, causal isoform assignment, safety inference, and Stage 2 advancement.

No rank, score, “confirmed” label, top-three shortlist, or advancement decision survives. The model used an arbitrary penalty for unknown HDAC6 activity, an arbitrary selectivity midpoint, `1 − oral bioavailability` as a gut-exposure surrogate, and mixed-assay or analogical potency estimates. It stored estimated gut concentrations but did not use them in the score.

The artifact also attributed Q141K rescue to an HDAC1/2/3–HSF1–Hsp90 pathway and treated HDAC6 avoidance as the principal safety discriminator. Basseville et al. did not establish that causal chain: selected pharmacological HDAC inhibitors rescued Q141K trafficking and substrate-efflux function **in vitro**, but HDAC6-selective inhibition did not reproduce rescue and the measured chaperone proteins did not explain it.

## What survives

The seven labels—butyrate, sulforaphane, allyl mercaptan, diallyl disulfide, phenethyl isothiocyanate, caffeic acid, and ferulic acid—survive only as an unranked historical candidate inventory. Their compound-specific evidence, exposure, Q141K trafficking effect, ABCG2-attributed urate flux, and safety must be tested independently.

One unranked connection also survives. Xie et al. found that butyrate increased endogenous intestinal BCRP/ABCG2 expression and drug-substrate function in rat, primary mouse-enterocyte, and Caco-2 systems that were not Q141K-specific and did not use urate as the substrate. PPARγ antagonism and silencing supported dependence in Caco-2 cells; the rat PPARγ result was correlational. Selected pharmacological HDAC inhibitors provide a separate Q141K-rescue precedent. Whether one butyrate exposure can combine the induction route with any Q141K trafficking rescue is directly untested.

## Current evidence owners and correction cascade

The [focused COMP page](../../../food-grade-hdaci-screen-computational.md) owns the invalidated verdict and unranked evidence inventory. The [ABCG2 evidence map](../../../abcg2-modulators.md) owns the surviving Research Conjecture and its discriminating experiment.

Correction targets in this retirement batch are:

- `wiki/food-grade-hdaci-screen-computational.md`
- `wiki/abcg2-modulators.md`
- `wiki/validation-experiments.md`
- `wiki/computational-experiments.md`
- `wiki/engineered-lbp-chassis.md`
- `wiki/open-questions.md`
- `index.md`

The remaining repository references are adjudicated as follows:

- `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/analyze.py`, `README.md`, `inputs/provenance.md`, `outputs/results.json`, and `outputs/summary.md` incorrectly attribute local achievable-concentration/IC50 thresholds to COMP-007. COMP-007 supplies no such method. The already-open `synthesis/queue/comp-review-015.md` owns that correction under COMP-015's lifecycle; those thresholds are not decision-eligible as COMP-007 evidence.
- `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/README.md` and `outputs/summary.md` describe historical method lineage inside a viability ranking that its current focused page already invalidates. They do not preserve a usable COMP-007 result.
- `wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/inputs/provenance.md` and `outputs/scope-summary.md`, plus `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/outputs/per-node-findings.md`, contain descriptive historical references only; they do not reuse a rank, score, advancement decision, causal isoform map, exposure proxy, safety inference, or decision rule.
- References inside this tombstone and its review receipts are retirement provenance, not active scientific evidence.

After the seven correction targets are reconciled and the COMP-015 dependency is handed to its existing queue item, `synthesis/queue/comp-review-007.md` is deleted in the same commit.

## Hash-bound retirement record

[`invalidation.json`](./invalidation.json) binds every retired non-review file to the exact pre-retirement Git tree by byte count and SHA-256 and defines the invalidated and surviving scopes.

There is no reproduction command. Git retains the retired code, inputs, outputs, and reviews.
