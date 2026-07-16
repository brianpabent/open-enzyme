PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: fa59c318a2e6835201d4613e2f6aa765ee81f1cf3b43a94c3bf4ffb10ec11fcd

# Adversarial pre-run review — comp-046

## Reviewed snapshot
Reviewer `/root/comp046_pre_review2`; `pre-run.manifest.json` binding SHA-256 `fa59c318a2e6835201d4613e2f6aa765ee81f1cf3b43a94c3bf4ffb10ec11fcd`; 5 design files; 2 prior-output baselines. The canonical manifest payload, every individual file SHA-256, and every byte count matched the files inspected. Design inspection preceded opening the historical outputs and prior review.

## Bottom-line verdict
This exact snapshot may execute. It now poses and implements two independent conditional questions: an 81-case conserved dietary fate ledger and an 81-case non-conserved endogenous capture-architecture comparison. It does not claim joint three-stage complementarity, single-sink counterproductivity, serum-urate efficacy, or biological probabilities. The earlier required corrections are closed without introducing a new mandatory design, implementation, provenance, output, or reproducibility defect.

## Question and model fit
The dietary model asks when whole-cell GR-5 interception changes absorbed dietary purine precursor. It compares a matched untreated absorbed quantity against absorbed unintercepted nucleoside plus absorbed liberated base, while explicitly crediting microbial salvage/retention only as a modeled fate. This answers a conditional mass-balance question rather than substituting DeoD expression for purine destruction.

The endogenous model separately asks when sequential UOX→residual transfer→PDB access captures a larger fraction than a specified overlap-adjusted well-mixed architecture. It does not treat this capture comparison as a conserved fate ledger. The analytic inequality and signed architecture difference directly answer that architecture question.

The model cannot infer combined three-stage efficacy, counterproductivity relative to either sink alone, dose, or serum urate. Those are now explicit exclusions rather than hidden proxy substitutions. Its downstream value is to identify which effective fractions require measurement in isotope-resolved dietary studies and sequential microoxic→anoxic reactor experiments.

## Constraint and implementation audit
The dietary path conserves the fixed 100-unit input across five mutually exclusive modeled fates, with an assertion enforcing closure. Intercepted and unintercepted signs are correct; free-base absorption is calculated as nucleoside absorption multiplied by the relative factor and capped at one. The matched-control denominator is strictly positive across the declared grid. The precursor-reduction sign is therefore interpretable as benefit, equality, or harm relative to matched untreated absorption.

The architecture functions use dimensionless fractions and assert outputs remain within `[0,1]`. Well-mixed capture and staged capture follow the equations declared in the input artifact. UOX always operates first in the staged hypothesis, transfer applies only to its residual, and PDB capture applies only to the transferred residual.

The two four-factor Cartesian products are genuinely separate. Each produces 81 unique cases; dietary sensitivity uses only the four dietary factors, and architecture sensitivity uses only the four architecture factors. No irrelevant replicated dimensions remain.

Time, microbial turnover and re-release, cross-feeding, oxygen/residence constraints, products, PDB viability, renal compensation, inflammation, colonization, and serum dynamics are not resolved. Their omission is appropriate to the stated effective-fraction boundary model and is explicitly disclosed. The proposed experimental consequence calls for direct measurement of residuals, products, transfer, and viability rather than treating these constraints as established.

`endogenous_luminal_urate_units` remains intentionally unused because the endogenous side reports fractions rather than a conserved quantity; this is explicitly disclosed in both provenance and generated limitations and does not enter a claimed calculation.

## Load-bearing pre-run table
| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Conserved 100-unit dietary input | `inputs/model_parameters.json`; `dietary_ledger()` | Normalize and close five modeled dietary fates | Explicit normalization policy, not an empirical human quantity | Pass |
| GR-5 interception fraction | `full_factorial_levels`; dietary factorial | Partition input into intercepted and unintercepted material | Broad scenario values; GR-5 anchor labeled **Animal Model** | Pass |
| Microbial salvage/retention fraction | `full_factorial_levels`; `dietary_ledger()` | Remove a scenario fraction of intercepted material from immediate liberated-base absorption | Explicit scenario parameter; whole-cell pathway evidence distinguished from DeoD causality | Pass |
| Nucleoside and relative free-base absorption | `full_factorial_levels`; `base_absorption` | Compare liberated-base absorption with matched untreated nucleoside absorption | Rat tissue evidence labeled **In Vitro / isolated tissue**; values explicitly not source estimates | Pass |
| Matched-control precursor reduction | dietary factorial | Compute signed change relative to untreated absorbed precursor | Derived normalized quantity with positive denominator | Pass |
| UOX and PDB capture fractions | architecture factorial | Parameterize effective capture by each sink | Engineering precedents labeled **Animal Model and In Vitro** and **In Vitro / mechanistic microbiology** | Pass as scenario inputs |
| Shared-pool overlap | well-mixed equation | Discount access by the lower-capture sink under overlap | Explicitly hypothetical broad scenario range | Pass |
| Residual-transfer efficiency | staged equation | Gate PDB access to post-UOX residual | Explicitly hypothetical broad scenario range | Pass |
| Two independent 81-case factorials | `main()` dietary and architecture loops | Prevent cross-product replication and maintain separate denominators | Fully code-derived | Pass |
| Separate Pearson sensitivities | `sensitivity_precursor`; `sensitivity_architecture` | Summarize signed linear association within each fixed grid | Deterministic descriptive sensitivity, not causal importance or probability | Pass |
| Architecture boundary | `architecture_boundary` output | State the exact condition under which staging wins | Analytic consequence of the declared equations | Pass |
| Output accounting distinction | `results` schema and generated summary | Emit one conserved ledger and one non-conserved comparison | Explicit `accounting_type` and repeated non-additivity disclaimer | Pass |
| Reproducibility | README reproduction command; standard-library code | Regenerate deterministic JSON and Markdown | Fixed local inputs, no randomness, external service, or third-party dependency | Pass |

## Falsification, sensitivity, and output contract
Contrary outcomes can win. The dietary grid permits absorbed precursor to increase, and the output reports that adverse-cell fraction. The architecture comparison permits staging, well-mixed access, or equality to win using a predefined zero-sign rule with a numerical equality tolerance. The fixed headline verdict is structural—two conditional hypotheses—not a preferred efficacy sign.

The independent full-factorials span the declared dominant effective fractions at three broad levels each. Separate Pearson summaries avoid the former irrelevant-factor artifacts. They are appropriately presented as descriptive sensitivity over a discrete design grid, not as biological probabilities.

The planned machine output retains per-question case counts, distribution summaries, the adverse dietary fraction, a complete central dietary ledger, architecture winner counts, central captures, signed differences, sensitivities, accounting type, analytic boundary, and limitations. Although per-cell rows are not committed, every cell and aggregate is deterministically reconstructible from the fixed inputs and inspected code. The generated human summary preserves the same accounting distinction and experimental requirements.

The historical outputs have the prior 6,561-row schema and old endogenous-ledger key, but the manifest correctly binds them only as prior-output baselines. Current code will replace them with separate 81-case schemas; they do not create a design ambiguity.

## Required actions before execution
None.

## Review limits
This was static, read-only inspection; the experiment was not executed. Primary papers were not independently retrieved because no numerical scenario level is represented as a source-derived estimate. The prior outputs and prior review were inspected only after independent design findings had been recorded, for baseline-schema and required-action closure checks. External wiki propagation surfaces are outside this pre-run manifest.
