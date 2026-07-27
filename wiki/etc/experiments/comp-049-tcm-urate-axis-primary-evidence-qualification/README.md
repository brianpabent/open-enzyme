# comp-049 — TCM urate-axis evidence qualification

**Status:** Pre-run design. Do not execute until this exact snapshot receives `PRE_RUN_GATE: GO`.

## Question

Can a fixed correction set of TCM-derived and formula-level urate-axis records preserve tested-material identity, traditional occurrence, source tier, target-effect polarity, assay context, exposure status, attribution boundaries, and mechanism-matched function—then expose every missing-evidence gap and select one next research route without producing a viability rank?

## Decision this COMP may inform

This COMP may identify and retain these independent gaps:

- underlying primary-trial review for a secondary evidence synthesis;
- tested-material identity, preparation, botanical authentication, reagent purity, and component attribution;
- causal molecular-target attribution;
- mechanism-matched function for each claimed gout weakness;
- free exposure in the relevant compartment;
- intestinal barrier and viability controls.

After emitting every gap, it may select one next route by a fixed priority and retain the others as deferred work. It may not rank compounds or formulas, infer dose feasibility, calculate target occupancy or percent inhibition, assign a clinical-risk tier, recommend a delivery route, or infer clinical efficacy.

## Fixed correction set

`inputs/evidence_records.json` contains four primary animal studies and one secondary systematic review selected to correct specific surviving COMP-013/TCM claims:

- a *Smilax glabra* total-flavonoid fraction containing four astilbin stereoisomers;
- a commercial emodin reagent;
- coix seed oil;
- *Plantaginis Semen* extract;
- a systematic review of modified Simiao decoctions.

This is not a systematic, multilingual, or comprehensive natural-product search. New candidates must enter through a literature scan using mechanism, species/original-language, traditional-formula, and traditional-pathology query frames. Changing the fixed records requires a new Gate 1 snapshot and review.

## Pre-registered method

The code will:

1. validate the exact five-record set, tested-material schema, controlled gout-weakness, compartment, exposure, intestinal-control, effect-scope, material-gap, and observation vocabularies, source design/tier/phenotype-modality contracts, Boolean fields, source-identifier syntax, and nonempty verification locations;
2. preserve tested-material provenance separately from traditional occurrence or formula context;
3. require every declared gout weakness to map to an observation and a compartment-specific free-exposure record, distinguishing measured, verified-not-measured, and not-verified-in-the-available-source states, while preserving every observation's target, polarity, treatment-group scope, endpoint kind, compartment, measurement directness, attribution state, and relevant weakness;
4. treat an associated target measure, expression result, null result, or whole-animal function as distinct from direct causal molecular-target attribution;
5. distinguish physiological weakness-scale function from molecular-target attribution: a non-null FEUA result can establish renal-excretion function without identifying its transporter, while enzyme activity or transport flux can establish target-level function when explicitly mapped to the weakness;
6. emit every independently detected gap before selecting a next route;
7. evaluate causal molecular-target attribution separately for every declared weakness and retain the exact missing-weakness set;
8. verify the exact disposition, complete gap set, complete deferred-gap set, and missing target-attribution weakness set for all five records with static assertions;
9. distinguish general intestinal histology or tight-junction evidence from barrier-integrity and viability controls attached to a direct flux assay;
10. reject duplicate weaknesses, duplicate or conflicting scoped observations, and mechanism/weakness/compartment combinations outside the preregistered contract;
11. emit no score, rank, occupancy, percent inhibition, viability label, dose, risk tier, efficacy inference, or delivery recommendation.

`test_validation.py` contains preregistered fail-closed fixtures for duplicate weaknesses, duplicate and conflicting scoped observations, and incompatible mechanism/weakness/compartment mappings.

Source-identifier checks validate syntax only. They do not verify source contents; `inputs/provenance.md` records the manual source-verification boundary.

## Pre-registered disposition priority

All gap flags survive in the output. The selected next route uses this order:

1. `PRIMARY_TRIAL_REVIEW_REQUIRED` for a secondary source;
2. `TESTED_MATERIAL_IDENTITY_REQUIRED` for a variable material family;
3. `PREPARATION_VERIFICATION_REQUIRED`, `REAGENT_PURITY_ATTRIBUTION_REQUIRED`, or `BOTANICAL_AUTHENTICATION_REQUIRED` for the corresponding material boundary;
4. `MATERIAL_ATTRIBUTION_REQUIRED` when an extract, fraction, or formula lacks individual-component causality;
5. `TARGET_ATTRIBUTION_REQUIRED` when a reported phenotype lacks direct causal molecular-target attribution;
6. `MECHANISM_MATCHED_FUNCTION_REQUIRED`;
7. `FREE_EXPOSURE_REQUIRED`;
8. `INTESTINAL_BARRIER_AND_VIABILITY_REQUIRED`;
9. `EVIDENCE_RECORD_COMPLETE_REVIEW_REQUIRED` only when no gap remains.

A selected route is not a favorable verdict. The output lists all deferred gaps and their reasons. Malformed, contradictory, duplicate, or unexpected records or routes fail closed.

## Fixed record expectations

The design preregisters the exact gap set and selected route for each record:

- Smilax fraction: preparation verification first; component, exposure, target-attribution, and renal-function gaps retained.
- Emodin: reagent-purity attribution first because the commercial reagent had stated 90% purity; exposure and renal target-attribution gaps retained. FEUA supplies physiological renal-excretion function; unchanged hepatic xanthine oxidase cannot fill the renal target gap.
- Coix seed oil: botanical authentication first; component, exposure, target-attribution, renal and intestinal function, and intestinal-control gaps retained.
- Plantaginis extract: material attribution first; exposure, target attribution, renal reabsorption-function, and urate-production-function gaps retained. Its reported serum xanthine-oxidase ELISA signal is not preregistered as a catalytic activity measurement.
- Modified Simiao review: underlying primary-trial review first; variable material, component, exposure, and target-attribution gaps retained.

## Sensitivity and falsification

There is no numerical sensitivity analysis because the COMP produces no numerical biological verdict. The relevant categorical distinctions remain visible in the output: material identity, source tier, expression versus function, compartment, polarity, direct attribution, free exposure, and intestinal controls.

This COMP adjudicates only the exact fixed records. A new record or any newly verified measurement requires a new Gate 1 snapshot; the design does not join observations, exposure, and controls from separate experimental regimes into a positive direct-intestinal verdict. Independent gaps are never erased by first-match routing.

## Planned outputs

- `outputs/evidence_qualification.json`
- `outputs/summary.md`

The Markdown output includes source design, tier, underlying reported evidence level and verified location; phenotype provenance; assay and biological system; declared weakness mappings; exact tested-material source, identity, preparation, explicit material gaps, and authentication boundary; traditional context; compartment-specific exposure; general and direct-assay intestinal controls; endpoint, polarity, treatment-group scope, directness and attribution; per-weakness function-evidence status; weaknesses lacking direct target attribution; every gap and reason; the selected gap and route; and deferred gaps.

The run is deterministic, uses Python's standard library only, has no randomness or external calls, reads and writes UTF-8 explicitly, and writes only those two files. Supported runtime: CPython 3.11 or newer.

## Reproduce after Gate 1 approval

From the repository root:

```bash
python3 -m unittest discover wiki/etc/experiments/comp-049-tcm-urate-axis-primary-evidence-qualification -p 'test_validation.py'
python3 wiki/etc/experiments/comp-049-tcm-urate-axis-primary-evidence-qualification/analyze.py
```

Run the validation fixtures, then run the analysis twice and compare output hashes before creating the post-run manifest.

## Planned downstream authoring

If this COMP later runs and Gate 2 passes, the canonical evidence home is `wiki/tcm-modern-rigor-intersection.md`. It must describe the result as mixed-source evidence qualification, not primary-evidence verification.

- `wiki/tcm-modern-rigor-intersection.md` may receive only the evidence-bound lead table and experiment routes;
- `wiki/tcm-gout-compound-triage-computational.md` may link from the COMP-013 tombstone to the replacement result;
- `wiki/computational-experiments.md` may record the bounded result;
- `wiki/open-questions.md` may receive at most a one-line link to unresolved experiments;
- target-specific mechanistic evidence remains on the page that owns that target;
- cross-track or delivery rankings remain forbidden without a separate portfolio experiment.

A negative or incomplete disposition kills only the unsupported ranking or attribution. It does not delete the source material, traditional-formula lead, or a neighboring untested mechanism.
