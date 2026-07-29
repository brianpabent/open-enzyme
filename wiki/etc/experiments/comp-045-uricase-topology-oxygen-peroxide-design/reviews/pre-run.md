PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: c608b1b5a852497ab8ec74db48b352eb1ce2468ac32d6523f3526b9ee9da4ecb

# Adversarial pre-run review — comp-045

## Reviewed snapshot

Reviewer `comp045_gate1_r3_20260729`; canonical manifest SHA-256 `c608b1b5a852497ab8ec74db48b352eb1ce2468ac32d6523f3526b9ee9da4ecb`; five design files and two prior-output baselines.

The canonical digest recomputed exactly. Every recorded byte count and file SHA-256 matched. The manifest covers every visible non-review artifact: five design files plus the two historical outputs. No repository-local shared dependency is imported.

## Bottom-line verdict

This exact schema-3 design may run. It deterministically validates an evidence vocabulary and candidate plate layout while preventing that layout from becoming a biological, statistical, wet-lab-readiness, efficacy, safety, oxygen-sufficiency, peroxide-closure, or topology-ranking result.

No mandatory design, implementation, provenance, output, or reproducibility action remains.

## Question and model fit

The computation answers the explicitly narrow decision: whether the declared evidence states, 18 candidate configuration classes, 20 block assignments, 16 planned contrasts, controls, regimes, and plate construction are internally valid.

It does not substitute the generated layout for biological comparison. The only allowed design disposition is `CANDIDATE_LAYOUT_GENERATED`; the biological verdict remains `NOT_EVALUATED`. Exact whole-configuration precedent, related precedent, component attribution, reaction-site peroxide alignment, and oxygen support remain separate axes.

## Constraint and implementation audit

The inventory is complete and internally consistent:

- Four intracellular, six LamB, six InaK-N, and two proposed *A. oryzae* configurations total 18 classes.
- Two ten-assignment blocks total 20 assignments; only `lamb_no_support` and `lamb_vhb_only` repeat, exactly as declared.
- Sixteen contrasts have both members in their required block.
- LamB and InaK-N each preserve catalase effects without and with VHb, plus VHb effects without and within reaction-site catalase. No interaction estimand is implied; the statistical model remains blocked.
- Each plate contains 10 assignments × 2 UOX states × 4 concentrations = 80 factorial wells, plus 4 anchors × 4 concentrations = 16 anchor wells.
- Three provisional run slots × 2 oxygen contexts × 2 blocks produce 12 plates. Three is explicitly not a power or precision claim.
- Stable allocation hashes bind seed, run, oxygen context, block, plate, and sample identity.

Biological closure is appropriately absent. Exact active/inactive constructs, expression/activity/localization equivalence, stocks, normalization, dissolved-oxygen targets, sampling, volumes, assay compatibility, low-concentration quantification, and the entire statistical decision contract block wet-lab execution.

The *A. oryzae* no-support row emits `host_catalase_location_and_activity_unresolved_no_reaction_site_closure`; the engineered co-secreted-catalase row remains only a proposed reaction-site-aligned configuration. Native host catalase is not upgraded into peroxide closure.

`require_pre_run_gate()` runs before input evaluation or output writes and verifies the manifest digest, phase, COMP directory, bound design hashes and sizes, exact GO receipt, and receipt snapshot. Contract violations stop execution before new outputs. Validation covers schema, frozen categorical vocabularies, exact/related source separation, configuration signatures, module compatibility, repetition, block coverage, contrast mapping, concentration roles, controls, anchors, blocked statistical/readiness contracts, readouts, and plate capacity.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Three PULSE topologies and six exact baseline/joint signatures | Provenance; exact-precedent table; validator | Whole-configuration precedent only | [Gao et al. 2025](https://doi.org/10.1016/j.xcrm.2025.102379), Figure 3B–I, Figure 5C, hypoxia paragraph, and Figure S10 directly support the three baseline-versus-joint KatG+VHb configurations at 250 µM | Pass |
| KatG and VHb were not isolated | Provenance; attribution and oxygen grading | Prevent component-level attribution | Gao Figure S10 and [Zhao et al. 2022](https://doi.org/10.1080/19490976.2022.2070391), Figure 3a–d, compare both modules with neither; no isolated arm is reported | Pass |
| PULSE sealed-tube and Zhao restricted-DO regimes differ | Oxygen contracts | Prevent a source regime from becoming a new DO target | Gao reports filled, sealed tubes without a DO target; Zhao Figure 3d reports approximately 15% of normal-medium DO | Pass |
| Gencer is related, not exact PULSE precedent | Related-precedent table | Preserve construct-family boundary | [Gencer et al. 2023](https://doi.org/10.3389/fbioe.2023.1191162), Figures 4–6, supports PucLM+YgfU in EcN at 250 µM in M9 and FaSSIF-V2 | Pass |
| 0.59 µM terminal-ileum prior | Concentration map and provenance conversion | Human-compartment design regime only | [Miyazaki et al. 2025](https://doi.org/10.1186/s12967-025-06145-7) reports 99.5 pg/µL, IQR 10.1–194.0, in 34 clinically indicated patients; Supplementary Material 2, Additional Methods, “Collection of small intestinal fluid and uric acid measurement,” explicitly states all procedures were in the terminal ileum of the pelvis | Pass |
| Urate molecular weight and conversion | Provenance | Convert 99.5 pg/µL to 0.591874 µM | PubChem CID 1175 reports 168.11 g/mol; median and IQR recompute to 0.591874 and 0.060080–1.154006 µM | Pass |
| No cited exact *A. oryzae* or matched-catalase precedent | Query strategy and no-direct-precedent state | Keep proposed classes separate from direct precedent | Europe PMC counts 25/15/38/6 and explicitly title/abstract-fielded PubMed counts 0/0/1/0 reproduced. Retrieved records were screened within the stated exact microbial scope. The finding remains bounded to those retrievals and is not a universal absence claim | Pass |
| Schema-3 inventory and reciprocal contrasts | Input, frozen expected mappings, outputs | Generate auditable configuration/evidence tables and layouts | Exact manifest-bound design; 18 classes, 20 assignments, 16 contrasts | Pass |
| Provisional occupancy and blocked analysis | Statistical and readiness contracts | Prevent plate occupancy from becoming inferential adequacy | Run count, estimand, thresholds, variance assumptions, power/precision, model, multiplicity, exclusions, failures, missing data, and sensitivities remain explicitly unresolved | Pass |
| Planned outputs and migration | Code, README, historical baseline | Replace schema 2 deterministically after Gate 1 | Schema 3 adds two reciprocal contrasts, statistical blocking, expanded qualifications/readouts, and corrected host-catalase semantics while retaining `NOT_EVALUATED` | Pass |

## Falsification, sensitivity, and output contract

No biological response enters the computation, so no numerical efficacy sensitivity analysis is appropriate. Concentration and oxygen grids remain labeled experimental regimes, not evidence or probability.

The planned JSON exposes the configuration table, 36 configuration-by-oxygen rows, all 16 contrasts, 12 complete plate maps, controls, sampling contract, required readouts, blockers, limitations, and fixed verdict mapping. The summary repeats the evidence boundary and blocked state.

The schema-2 output baseline was inspected only after the independent design findings were recorded. Its 14-contrast, less-qualified structure is correctly treated as historical and is hash-bound for the mandatory first-execution check.

## Downstream authoring contract

The canonical evidence home is `wiki/uricase-topology-oxygen-peroxide-design-computational.md`. The declared direct dependents are the dashboard, computational index, delivery/program pages, COMP-044 interpretation, H08, validation surface, paper draft, and COMP-045 synthesis queue.

Propagation may state only the validated inventory, evidence vocabulary, candidate layout, source boundaries, and unresolved qualification gates. It may not claim activity at 0.59 or 50 µM, oxygen sufficiency, isolated KatG/VHb effects, extracellular peroxide closure, InaK-N surface accessibility, secreted active UOX in *A. oryzae*, safety, efficacy, dose, or a topology/chassis winner.

A later negative result may invalidate only the tested construct × concentration × oxygen × control regime. Adjacent mechanism ideas remain conjectural unless their required premises fail. COMP-044 input changes require a separate lifecycle.

## Required actions before execution

None.

## Review limits

Static, read-only inspection only. `analyze.py` and no result-bearing logic were executed, and no repository files were changed. The bounded negative search was audited only within its declared indexed-record scope; it was not treated as a systematic review or universal absence claim.
