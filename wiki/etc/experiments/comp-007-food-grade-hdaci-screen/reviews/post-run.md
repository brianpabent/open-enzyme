ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: ff92421517641997a6fee07c0e74dfccd0eb59bdc96bcbaa4e4b8f7f4d95bfe0

# Independent comp review — comp-007

## Reviewed snapshot

Reviewer: Codex `/root/comp007_tombstone_gate2_refresh`, fresh authoring-time Gate‑2 reviewer.

`python3 scripts/comp-review-manifest.py check --manifest wiki/etc/experiments/comp-007-food-grade-hdaci-screen/reviews/post-run.manifest.json` returned the snapshot digest above. Every listed file matched its recorded byte count and SHA‑256.

The retirement record was also independently checked against Git commit `35fd84865925592d42cbc89c84f45b1c8a81ad9f`: all eight retired-file byte counts and SHA‑256 values matched, and the canonical invalidation digest recomputed to `6bba6541f53060b84ea20ad6a5d5e36a47f1ad3c8c31d1e737e474ff32ff4e8e`.

## Bottom-line verdict

**Clean with limitations.** The exact current artifact is a coherent, non-runnable tombstone. It withdraws the full quantitative and decision-bearing COMP-007 model without overextending the negative result. The surviving seven-name inventory is explicitly unranked, the butyrate dual-route idea is preserved as an untested Research Conjecture, and the current reader-facing and validation surfaces consistently require direct trafficking, urate-flux, exposure, inhibition, and safety evidence.

The narrative-only COMP-015 delta is accurate: COMP-015 is now itself a non-runnable invalidated tombstone, and its falsely attributed achievable-concentration/IC50 thresholds, rankings, matrix verdicts, and decision use are withdrawn.

## Implementation and constraint closure

Inspection of the hash-bound retired implementation independently confirms the stated defects:

- Unknown HDAC6 activity received the arbitrary constant `0.30`.
- Selectivity used the arbitrary normalization midpoint `10`.
- Gut selectivity was calculated as `1 − oral_bioavailability_fraction`.
- Recombinant IC50 values, nuclear-extract results, cellular protein effects, inferred IC50 values, and an analogical PEITC estimate were treated as comparable potency inputs.
- `typical_gut_concentration_uM` was copied into output rows but never entered the score.
- Ranking was therefore not tied to epithelial free concentration, uptake, exposure duration, Q141K trafficking, ABCG2-attributed urate flux, transporter inhibition, finite compartment behavior, or a complete safety model.
- The archived narrative overassigned HDAC1/2/3 causality, an HSF1–Hsp90 explanation, and HDAC6 avoidance as the governing safety discriminator.

Because no quantitative output or decision survives, deleting executable files and retaining the exact archived tree through Git plus `invalidation.json` is appropriate. No reproduction command should exist.

## Summary-fidelity audit

The tombstone, invalidation record, focused COMP page, computational index, root index, ABCG2 evidence map, LBP chassis page, open-questions index, and validation plan agree on the material points:

- No rank, score, confidence label, shortlist, Stage‑2 advancement, causal isoform assignment, exposure inference, or HDAC6-centered safety conclusion survives.
- The seven materials remain only an unranked historical/evidence inventory.
- Basseville supplies an **In Vitro** selected-pharmacological-HDI Q141K rescue precedent using drug-substrate efflux, not direct butyrate rescue, urate flux, intestinal exposure, or clinical evidence.
- Xie supplies non-Q141K-specific, non-urate preclinical endogenous-BCRP/ABCG2 induction evidence; the stronger PPARγ perturbation inference is correctly limited to Caco‑2, while the rat PPARγ observation is not promoted to causal proof.
- Validation §1.22 requires positive/contrast-control reproduction before candidate interpretation and then direct polarized-intestinal trafficking, urate-flux, exposure, inhibition, viability, barrier, and route/safety measurements.
- The retired cost and timeline are not retained.
- COMP-015’s false dependency is described as retired rather than still queued.

No stale COMP-007 quantitative verdict or advancement instruction remains in the manifest-bound pages.

## Reader-facing ownership audit

The focused page owns the current COMP verdict, evidence/source boundaries, delivery constraints, and falsifying experiment. `wiki/abcg2-modulators.md` owns the compact Research Conjecture. `wiki/validation-experiments.md` owns the empirical resolver. Cross-track ranking language has been removed rather than relocated to another focused track.

The operational tombstone README appropriately carries retirement provenance and correction-closure language; the focused reader-facing page does not narrate queue history or page-placement mechanics. No personalized treatment instruction, narrative foil, or duplicated portfolio comparison was found.

## Conjecture preservation audit

Unsupported factual claims were corrected without erasing the useful connection:

- Killed: COMP-007’s ranking, composite score, confidence order, Stage‑2 shortlist, candidate-specific rescue/urate/exposure/safety claims, causal HDAC1/2/3 chain, and HDAC6-primary-safety inference.
- Preserved: selected pharmacological HDIs can rescue Q141K trafficking and drug-substrate function **In Vitro**.
- Preserved: butyrate can induce endogenous BCRP/ABCG2 in non-Q141K-specific preclinical systems, with PPARγ perturbation support in Caco‑2.
- Explicitly untested: one measured butyrate exposure might combine endogenous ABCG2 induction with some Q141K trafficking rescue.
- Correct discriminator: genotype-resolved polarized models, PPARγ blockade, Basseville-matched controls, apical surface abundance, ABCG2-attributed urate flux, intracellular exposure, direct inhibition, viability, and barrier integrity.

The null/invalidated computation does not kill pharmacological rescue as a class, butyrate induction, untested butyrate exposures, or the other six materials.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/README.md` | design | Yes | Accurate non-runnable tombstone; COMP-015 closure delta is current. |
| `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/invalidation.json` | design | Yes | Retired tree, invalidated scope, surviving scope, and canonical digest verified. |
| `index.md` | proposed_update | Yes | Concise invalidated-ranking entry; no stale decision. |
| `wiki/abcg2-modulators.md` | proposed_update | Yes | Correct evidence separation and conjecture ownership. |
| `wiki/computational-experiments.md` | proposed_update | Yes | COMP-007 and COMP-015 both accurately marked invalidated. |
| `wiki/engineered-lbp-chassis.md` | proposed_update | Yes | Butyrate rationale remains preclinical and conditional; no COMP-007 priority. |
| `wiki/food-grade-hdaci-screen-computational.md` | proposed_update | Yes | Standalone evidence, delivery, and falsification contract is complete. |
| `wiki/open-questions.md` | proposed_update | Yes | Surviving leads remain questions, not inherited results. |
| `wiki/validation-experiments.md` | proposed_update | Yes | Direct unranked resolver replaces invalid preselection. |

No `generated_output` entry exists, appropriately for a non-runnable tombstone.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Unknown-HDAC6 penalty `0.30` | Retired `analyze.py` | Multiplied into score | Internal arbitrary constant | Correctly invalidated |
| Selectivity midpoint `10` | Retired `analyze.py` | Normalized selectivity | Internal arbitrary constant | Correctly invalidated |
| `1 − oral BA` | Retired `analyze.py` | Multiplied into score | Exposure surrogate, not epithelial measurement | Correctly invalidated |
| Gut concentrations | Retired candidate input/output | Stored only | Estimated heterogeneous values | Correctly identified as unused |
| Mixed/analogical potency | Retired bioactivity/provenance | Produced potency ordering | Assay-incommensurate and partly inferred | Correctly invalidated |
| Basseville Q141K precedent | Focused page; ABCG2 map; validation | Positive/contrast-control basis only | PMID 22472121; **In Vitro** | Scope is faithful |
| Xie butyrate induction | Focused page; conjecture | Grounds endogenous-induction premise only | PMID 32555444; **In Vitro + Animal Model** | Scope is faithful |
| COMP-015 false dependency | COMP-007 README; current COMP-015 tombstone | No surviving decision use | Current repository retirement record | Closure language accurate |
| Retired-tree digest | `invalidation.json` | Binds deleted artifact | Independently recomputed from Git | Pass |

## Affected wiki pages

- `index.md` — already consistent; no quantitative priority survives.
- `wiki/food-grade-hdaci-screen-computational.md` — already consistent; current evidence home.
- `wiki/abcg2-modulators.md` — already consistent; owns surviving conjecture.
- `wiki/validation-experiments.md` — already consistent; owns direct resolver.
- `wiki/computational-experiments.md` — already consistent; both COMP-007 and COMP-015 are retired.
- `wiki/engineered-lbp-chassis.md` — already consistent; delivery remains conditional.
- `wiki/open-questions.md` — already consistent; no inherited ranking.
- `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/README.md` and `invalidation.json` — already consistent; corroborate the narrative delta.

## New connections or implications

No additional propagation is required. The useful cross-page implication is already represented: endogenous ABCG2 induction and Q141K trafficking rescue are separable mechanisms and must be experimentally dissociated before any combined-route claim. Direct evidence for the combined butyrate effect remains absent and is correctly confined to a Research Conjecture.

## Required actions

1. None.

## Review limits

No result-bearing code was executed. The archived implementation, inputs, outputs, and provenance were inspected from the hash-bound Git tree solely to verify the retirement rationale. This review does not independently re-establish every compound-specific historical bioactivity or exposure value because none remains decision-eligible; it verifies that those values are withdrawn and that the two surviving biological anchors are used only within their stated evidence boundaries.
