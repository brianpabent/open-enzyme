ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: 3e3d58c1c8ec957fc3aa9b1108aa0b151553e9083bfeb159c18bc1bcf2b964ca

# Independent comp review — comp-014

## Reviewed snapshot

Independent legacy post-only Gate-2 review of the exact 173-entry manifest:

- 8 design files
- 148 generated outputs
- 17 proposed updates
- 435,198,594 bound bytes

Every file was read byte-for-byte. Recorded byte counts and SHA-256 hashes matched. All 120 JSON files parsed, all 53 text files decoded, and the sole Python file parsed successfully. The manifest’s canonical payload digest and current snapshot check both resolve to the reviewed digest above.

## Bottom-line verdict

COMP-014 is now honestly bounded as a partial retrieval inventory. It no longer supports candidate rankings, feasibility verdicts, dose or exposure conclusions, production or chassis decisions, universal absence claims, or the retired Phase-6 `PURSUE`/`DROP` logic.

The useful scientific leads remain available for primary-source rehydration. Historical outputs are visibly quarantined, raw captures remain unchanged, the sole live validator is deterministic, downstream pages preserve the corrected evidence boundary, and H06’s useful idea survives as a properly labeled exact-material Research Conjecture.

No remaining correction is required for this snapshot.

## Implementation and constraint closure

The surviving implementation is limited to `scripts/scope_validate.py`. It validates the retained Phase-1 input structure and regenerates `outputs/scope-summary.md`; it does not claim to reproduce the historical database pulls, joins, rankings, or retired feasibility triage.

Two independent executions produced identical output:

- 18 historical anchor species
- 19 rendered historical target entries
- output SHA-256 `f6e2cf580ea16084a0cf5e5c3f744fecf02a1e435b4962ffb2fb5cdbf889051f`

The validator correctly renders both object-valued and alias/string-valued bioactivity-source entries. All six recorded bioactivity-source entries appear in the summary.

The retired Phase-6 script and outputs are absent. The retired LOTUS aggregation, target-mapping, and other legacy executable scripts are also absent. `scope_validate.py` is the only executable retained in the COMP directory.

All raw captures and historical caches match `HEAD` byte-for-byte. The correction changes their authority, not their contents.

Repository checks pass:

- relative links
- privacy gradient
- corpus hygiene
- validation-dashboard consistency
- exact manifest verification

## Summary-fidelity audit

The live README and regenerated scope summary agree:

- the artifact is a partial lead inventory;
- database absence is only a bounded non-retrieval;
- historical rank and priority fields have no decision authority;
- plant-origin compounds are not reclassified as fungal products without direct evidence;
- binding, expression, prediction, and phenotype do not substitute for mechanism-matched function;
- each lead requires exact identity, provenance, polarity, substrate, compartment, exposure, direct function, and safety controls.

The scope summary does not quietly restore rankings or Phase-6 authority. Its source counts describe the recorded historical inventory, not successful or comprehensive coverage.

## Reader-facing ownership audit

The medicinal-mushroom page now stands on its own evidence, sourcing, exposure, immune-direction, and falsification gates. It does not use koji as its narrative foil or treat a production chassis as the default filter.

The computational interpretation page clearly separates:

- surviving retrieval leads;
- invalid rankings and feasibility conclusions;
- lead-specific sourcing and delivery;
- the primary-source rehydration workflow.

Cross-track comparisons remain on portfolio surfaces. ADA and PINK1 mechanism context is owned by gout pathophysiology, with independent primary sources rather than COMP-014 serving as evidence authority. C5aR1 non-retrieval is consistently framed as a bounded search gap across the complement, NLRP3, delivery-route, computational-experiment, and validation surfaces.

Editorial Phase-5/6/7 narration and stale H06 references have been removed from active reader-facing prose where corrected by this snapshot.

## Conjecture preservation audit

The deleted H06 card is not silently lost. Its useful idea survives on the mechanism-owning page in the required Research Conjecture form:

- source-backed Animal Model premises;
- an explicit untested leap about exact-material reproducibility;
- the value of an engineerable, reproducible material;
- a discriminating observation using primary-record rehydration, qualified identity/exposure assays, and independent batches.

No direct evidence is claimed for the leap, and no material is prematurely selected. `open-questions.md` links to the owning conjecture rather than duplicating it.

## Generated-output and proposed-update inventory

| Manifest entries | Kind | Review result |
|---|---|---|
| `.gitignore`, `README.md`, four input files, `inputs/provenance.md`, `scripts/scope_validate.py` — 8 files | Design | Exact, internally consistent |
| `_chembl_molecule_inchikey_cache.json`, `_chokepoint_chembl_targets.json`, `_knapsack_inchikey_cache.json` — 3 files | Historical cache/intermediate | Unchanged, non-authoritative |
| `_chembl_raw/*.json` — 28 files | Raw capture | Unchanged, parsed |
| `_knapsack_raw/*.html` — 12 files | Raw capture | Unchanged, decoded |
| `_lotus_raw/*.json` — 56 files | Raw capture | Unchanged, parsed |
| `_npatlas_raw/*.json` — 20 files | Raw capture | Unchanged, parsed |
| Nine top-level derived Phase-2/3/4 JSON files | Historical derived output | All carry `historical_snapshot`, `non_authoritative`, `lead_only`, and `_authority_note` |
| `PHASE-2-FINDINGS.md`, `PHASE-5-FINDINGS.md`, Phase-2/3/4 summaries, five Phase-5 deep reads, DeepSeek cross-check, and four Phase-7 files — 19 files | Historical narrative output | Exact non-authoritative banner present |
| `outputs/scope-summary.md` | Live generated output | Deterministic and faithful |
| `index.md` | Proposed update | Mission/portfolio framing correct |
| `operations/todos.md` | Proposed update | Queue state consistent |
| `wiki/complement-c5a-gout.md` | Proposed update | C5aR1 absence claim bounded |
| `wiki/computational-experiments.md` | Proposed update | COMP verdict faithful |
| `wiki/cross-validation.md` | Proposed update | Real-claim rule and portfolio semantics restored |
| `wiki/etc/manual-literature-mining.md` | Proposed update | Evidence workflow consistent |
| `wiki/gout-genetic-variants.md` | Proposed update | Evidence tiers and GLUT9/ADA boundaries corrected |
| `wiki/gout-kill-chain-delivery-routes.md` | Proposed update | Search gap does not select a route |
| `wiki/gout-pathophysiology.md` | Proposed update | ADA/PINK1 independently anchored |
| `wiki/hypotheses/README.md` | Proposed update | H06 removal correctly reflected |
| `wiki/medicinal-mushroom-complement-track.md` | Proposed update | Correct evidence owner; conjecture preserved |
| `wiki/medicinal-mushroom-compound-mapping-computational.md` | Proposed update | Partial-inventory authority boundary clear |
| `wiki/medicinal-mushroom-extract-sops.md` | Proposed update | Draft methods and reagent identities corrected |
| `wiki/modality-chokepoint-matrix.md` | Proposed update | Portfolio comparison correctly located |
| `wiki/nlrp3-exploit-map.md` | Proposed update | Fungal non-retrieval bounded |
| `wiki/open-questions.md` | Proposed update | Current method/conjecture descriptions accurate |
| `wiki/validation-experiments.md` | Proposed update | §1.21 and mushroom-related experiments bounded |

## Load-bearing verification table

| Claim or boundary | Verification | Verdict |
|---|---|---|
| Manifest binds current files | Canonical digest plus all file hashes and sizes checked | Pass |
| Raw retrieval payloads were preserved | All raw/cache paths compared with `HEAD` | Pass |
| Validator is deterministic | Two runs, identical output hash | Pass |
| Historical Markdown is quarantined | 19/19 narrative files carry the exact warning banner | Pass |
| Historical derived JSON is quarantined | 9/9 top-level derived JSON files carry all authority flags | Pass |
| Phase-6 ranking remains executable | Script and outputs absent | Pass: retired |
| Historical safety filter can authorize inclusion | Explicitly non-authoritative and unused except structural presence | Pass: cannot authorize |
| Trial registration or missing mycotoxin flag proves safety | Explicitly rejected | Pass |
| C5aR1 search proves universal absence | Rewritten as query-bound non-retrieval | Pass |
| §1.21 closes natural products as a class | It closes only repetition of the recorded query unchanged | Pass |
| Toxicarioside is rejected without source review | Replaced by a primary-toxicology/selectivity/exposure gate | Pass |
| ADA and PINK1 depend on COMP-014 as evidence | Independent primary sources now anchor the mechanism | Pass |
| ADA-SCID/xanthinuria are clinical trials | Corrected to human observational/clinical phenotype and functional evidence | Pass |
| Ergothioneine or lactoferrin concentrations are asserted chassis-achievable | Replaced by source-qualified, analytically verified, pilot-set ranges | Pass |
| Cordycepin reference identity | Sigma C3394 verified | Pass |
| Pentostatin reference identity | Cayman 14878 verified; erroneous valinomycin ID removed | Pass |
| Xiong 2024 composition figures | Publisher record supports 35.86%, 27.05%, 0.21%, and 0.83% for the exact whole extract | Pass |
| H06 scientific idea was deleted | Preserved as exact-shape owner-page conjecture | Pass |
| SOP-6 index still promises specific unvalidated color chemistry | Updated to generic candidate assays requiring analytical validation | Pass |

## Affected wiki pages

The correction propagates through the medicinal-fungal evidence home, COMP interpretation, experiment registry, gout pathophysiology and genetics, NLRP3/complement maps, delivery analysis, portfolio matrix, hypothesis index, open questions, computational-experiment index, cross-validation page, and repository dashboard.

The propagated message is consistent: COMP-014 can nominate records for primary review but cannot rank interventions or choose efficacy, dose, safety, sourcing, production, delivery, or chassis.

## New connections or implications

The cleanup leaves three productive research directions without overclaiming:

1. An exact fungal material can be treated as an engineering object only after identity, composition, exposure, and independent-batch reproducibility are established.
2. ADA remains interesting because purine-flux reduction and adenosine-mediated resolution may move together or oppose one another; both axes must be measured.
3. A bounded C5aR1 database no-hit argues for a direct human-receptor functional screen, not abandonment of natural-product chemical space.

These are research-generating connections, not COMP-014 results.

## Required actions

None.

## Review limits

This was an independent exact-snapshot review of the retained artifact, its authority boundaries, and all bound proposed updates. The historical 435 MB source corpus was parsed and integrity-checked, but the legacy database pulls were not rerun and every historical source claim was not independently re-retrieved. That limitation is now explicit in the artifact itself: historical rows are retrieval leads until primary-source rehydration.

The only executable run was the retained structural scope validator; no retired result-bearing analysis was executed.

ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: 3e3d58c1c8ec957fc3aa9b1108aa0b151553e9083bfeb159c18bc1bcf2b964ca
