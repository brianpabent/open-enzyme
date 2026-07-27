COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 0d0148e43ade23213e148e0b97687eb5bb9b857a1f94cd1ec5d299dccca3c253
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective local propagation of COMP-044 as a bounded invalidation of COMP-019’s unconditional flat-dose robustness claim only
SYNTHESIS_ALLOWED_SCOPE: use only as a negative/bounding regime audit; no replacement efficacy, dose, topology, chassis, safety, serum-urate, or genotype model
FORBIDDEN_INFERENCES: true physiological regime identified; oral UOX dose sufficiency; serum urate or ΔSUA prediction; genotype ordering or responder prediction; chassis/topology winner; production sufficiency or economics; peroxide/redox safety; animal or human escalation readiness; clinical advice

# Independent comp review — comp-044

## Reviewed snapshot
Independent daemon reviewer; trigger commit `8ddcf2c354b5478c6e31a74081f68399e2c8f1f2`; push-review manifest SHA-256 `0d0148e43ade23213e148e0b97687eb5bb9b857a1f94cd1ec5d299dccca3c253`. Hash-bound shard audits report complete inspection of all covered text spans, no deterministic binary blocks, and modern valid authoring gates. I performed one targeted repository cross-check by reopening `wiki/open-questions.md` and `wiki/cross-validation.md`; snapshot materially matched the audited files for the checked claims. Repository grep was unavailable because the tool backend lacked `rg`.

## Bottom-line verdict
Action required, but the quantitative COMP-044 verdict is not invalid. The computation faithfully supports a narrow negative conclusion: COMP-019’s unconditional saturated/flat-dose classification is not robust once finite substrate occupancy and finite active windows are imposed. The model remains a fixed-concentration capacity diagnostic against a daily-flux denominator, not a physiologic luminal reaction-rate, serum-effect, or safety model. Required actions are documentation cleanup: reconcile conflicting feasibility-score references in `open-questions.md` and tighten one comp-031 invalidation wording so it does not overstate COMP-044’s blast radius.

## Implementation and constraint closure
The implementation traces from `inputs/model_parameters.json` through `analyze.py` into `outputs/results.json` and `outputs/summary.md`. The core calculation uses saturated substrate fraction `1.0` for the legacy control and `urate/(Km+urate)` for finite-concentration cases, then scales nominal enzyme capacity by pH, oxygen, access, survival, dose, and active hours against a 233 mg/day denominator. The declared full-factorial grid size is internally closed: 5 urate levels × 3 Km × 4 hour windows × 3 oxygen × 3 access × 3 survival = 1,620 scenarios per dose, 4,860 total.

Decision-rule closure is adequate. The legacy saturated control ratios are all ≥1, while the terminal-ileal no-extra-penalty ratios are 0.093, 0.466, and 0.932 for 5/25/50 mg, satisfying the declared non-robust branch. Regression checks anchor the published central diagnostics when default load-bearing inputs are unchanged.

The main model-fit limitation is intentional but load-bearing: this is not a dynamic gut model. It mixes a local terminal-ileal clinical-cohort urate concentration with a whole-day flux denominator. It does not model substrate depletion/replenishment, diffusion, reabsorption, renal compensation, microbiome metabolism, topology, localization, residence-time distribution, or serum mapping. Reaction closure is incomplete by design: urate is represented as substrate; oxygen is only a dimensionless activity multiplier, not a stoichiometric cosubstrate with delivery/depletion; peroxide/product formation and scavenging are excluded. Therefore, ratio ≥1 is only a capacity boundary and cannot prove luminal capture or safety.

Physiological concentration relative to Km is correctly central: the 0.59 µM terminal-ileal prior is far below the central 25 µM Km, making saturation assumptions fragile. The computation tests this fragility but does not establish that 0.59 µM is the patient-general operating concentration.

## Summary-fidelity audit
`outputs/summary.md`, `outputs/results.json`, the experiment README, and `wiki/gut-lumen-uricase-physiologic-regime-computational.md` are mutually faithful on the narrow verdict and limitations. `wiki/computational-experiments.md` correctly reports the non-robust boundary, named scenario ratios, grid occupancy as non-probability, inherited priors, and no replacement model. The comp-019 tombstone correctly limits the impact to the unconditional flat-dose classification.

Relevant propagation surfaces are mostly aligned: `delivery-route-matrix.md`, `dual-chassis-ecn-pdb-uricase-computational.md`, `GRAPH.md`, `gout-action-guide.md`, `gout-multihop-research-program.md`, H08, and `validation-experiments.md` preserve the “no dose / no ΔSUA / no topology / no safety / no chassis winner” boundary. `validation-experiments.md` §1.33 appropriately makes exact-configuration physiological substrate, oxygen, product, peroxide, viability, localization, and active-UOX recovery the next gate.

Two summary-fidelity issues remain. First, `open-questions.md` contains inconsistent cross-reference language for gut-lumen uricase feasibility: one reference says cross-validation rates it 5.5/10, another says 6/10, while the reopened current `cross-validation.md` no longer presents a score. Second, the comp-031 invalidation README says it inherited comp-019’s invalid uricase saturation regime; this is directionally true but should be narrowed to COMP-044’s exact finding: the unconditional flat-dose classification is not robust under the tested substrate-occupancy/finite-window diagnostics.

## Reader-facing ownership audit
Focused COMP-044 and gut-lumen-UOX pages own their evidence and limits; they do not delegate a hidden stronger claim to portfolio pages. Portfolio-wide rankings and route comparisons are mostly kept out of focused pages. Reader-safety framing is acceptable: pages state this is research, not treatment guidance, and preserve requirements for manufactured product, ethics/regulatory review, exposure, safety, FEUA, and attribution controls before human study. No personalized dosing or self-administration instruction follows from the inspected material.

The open-questions score duplication is the main ownership defect: it turns a portfolio/cross-validation concept into stale duplicated quantitative residue. That should be either removed or reconciled at the owner surface.

## Conjecture preservation audit
COMP-044 kills only the exact legacy claim that flat saturated UOX dose classifications were robust to tested finite-substrate and finite-window diagnostics. It does not kill H08, gut-lumen sink biology, oral UOX as a track, PDB/UOX complementarity, genotype stratification as a future question, or topology comparisons. Those remain research conjectures or open empirical gates requiring exact configurations, physiological-substrate testing, peroxide/redox safety, and translation data.

Grounded adjacent conjectures survive if rewritten with explicit unsupported leaps: transporter-supply plus UOX consumption may interact; UOX/PDB staging may matter; genotype may alter substrate delivery or response. None may be presented as established additivity, genotype ordering, serum effect, or chassis preference.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md` | experiment source/contract | yes | Faithful; bounded propagation contract. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/analyze.py` | experiment code | yes | Implements declared fixed-concentration capacity diagnostic. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/model_parameters.json` | input | yes | Factorial dimensions and defaults internally consistent. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/provenance.md` | input/provenance | yes | 0.59 µM corrected; several priors inherited/unverified. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/query-strategy.json` | input/provenance | yes | No independent issue found. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/results.json` | generated_output | yes | Supports non-robust branch; limitations explicit. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md` | generated_output | yes | Faithful rounded summary. |
| `wiki/computational-experiments.md` | proposed_update | yes | Correct COMP-044 and COMP-019 boundary. |
| `wiki/delivery-route-matrix.md` | proposed_update | yes | Correctly avoids route promotion/economic sufficiency. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | proposed_update | yes | Correctly invalidates inherited UOX saturation without ranking topology. |
| `wiki/etc/GRAPH.md` | proposed_update | yes | Dependency boundaries preserved. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md` | affected/proposed_update | yes | Needs slight tightening of invalidation scope. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/inputs/provenance.md` | affected | yes | No separate issue reported. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/outputs/summary.md` | affected | yes | No separate issue reported. |
| `wiki/gout-action-guide.md` | proposed_update | yes | Research-roadmap boundary preserved. |
| `wiki/gout-multihop-research-program.md` | proposed_update | yes | Correct sequencing: construct characterization, §1.33, §1.36. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | proposed_update | yes | Accurate bounded interpretive page. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | proposed_update | yes | H08 remains Open; no numeric ΔSUA overclaim. |
| `wiki/open-questions.md` | proposed_update | yes | Substantively bounded, but feasibility-score references conflict. |
| `wiki/validation-experiments.md` | proposed_update/affected | yes | §1.33 and related gates preserve COMP-044 constraints; unrelated later-section provenance issues not load-bearing for COMP-044. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Terminal-ileal urate 0.59 µM | `inputs/provenance.md`, model defaults | Substrate occupancy `S/(Km+S)` | Direct arithmetic conversion plausible; source not independently primary-verified here | Usable as bounded clinical-cohort prior, not general baseline. |
| Uricase activity 8.3 U/mg | inputs/code/results | Capacity numerator | Inherited, not newly primary-source verified | Planning use requires verification. |
| Km range 5–100 µM, central 25 µM | inputs/code/grid | Dominant occupancy uncertainty | Inherited, not newly primary-source verified | Adequate for audit sensitivity; not final kinetic truth. |
| pH multiplier 0.75 | inputs/code | Capacity multiplier | Inherited/unverified | Scenario variable only. |
| Active window 2–4 h, central 3 h | inputs/code/grid | Capacity multiplier | Inherited/unverified | Bounded residence proxy, not transit model. |
| 233 mg/day urate flux denominator | inputs/code/results | Ratio denominator | Population prior; not local compartment rate | Valid for legacy-stress audit only. |
| Oxygen/access/survival multipliers | inputs/code/grid | Nonmechanistic capacity penalties | Scenario assumptions | Do not infer oxygen stoichiometry, diffusion, or viability. |
| Legacy ratios ≥1 and terminal-ileal central ratios <1 | outputs/results/summary | Decision branch | Computed and internally checked | Supports non-robust verdict. |
| Grid fractions <1 | outputs/results/summary | Descriptive sensitivity | Full-factorial design occupancy only | Not probabilities. |
| No peroxide/safety conclusion | outputs limitations/wiki | Boundary | Explicitly stated | Must be preserved downstream. |

## Affected wiki pages
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — bounded negative verdict and limitations preserved.
- `wiki/computational-experiments.md` — already consistent — COMP-044 index and COMP-019 tombstone are faithful.
- `wiki/validation-experiments.md` — already consistent for COMP-044 — §1.33/§1.36 keep topology, peroxide, and physiological-regime gates empirical.
- `wiki/delivery-route-matrix.md` — already consistent — no route or economic promotion from COMP-044.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — keeps UOX/PDB complementarity open.
- `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md` — change required — narrow invalidation wording to the exact COMP-044 blast radius.
- `wiki/gout-action-guide.md` — already consistent — no treatment protocol or self-experiment implication.
- `wiki/gout-multihop-research-program.md` — already consistent — construct characterization and safety gates precede escalation.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — H08 remains Open; COMP-044 is not a biological killshot.
- `wiki/open-questions.md` — change required — reconcile/remove stale 5.5/10 vs 6/10 feasibility references to `cross-validation.md`.
- `wiki/cross-validation.md` — already consistent in reopened text — current page does not present a single feasibility score.

## New connections or implications
COMP-044 strengthens the rationale for validation §1.33 measuring product formation, oxygen, peroxide, viability, localization, and active UOX at the reaction site instead of using urate disappearance or nominal retained activity alone. It also redirects UOX/PDB topology speculation: PDB staging or co-localization may be useful, but only as a Research Conjecture until physiological UOX activity and PDB carbon fate are separately measured. The result suggests that any future genotype-stratified UOX study must first establish a real luminal operating regime; genotype cannot rescue an invalid saturated-dose premise.

## Required actions
1. In `wiki/open-questions.md`, reconcile the gut-lumen uricase feasibility references: either remove numeric score duplication or point to the current owner surface with one current value. Verification: no remaining inconsistent 5.5/10 vs 6/10 references for the same COMP-044/cross-validation claim.
2. In `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md`, tighten the invalidation sentence to say COMP-044 invalidates COMP-031’s inherited reliance on COMP-019’s unconditional flat-dose/saturation robustness, not all possible UOX regimes or all UOX/PDB complementarity. Verification: wording preserves adjacent conjectures and points to §§1.33/1.34/1.37 for replacement evidence.
3. Before using COMP-044 numbers for planning rather than audit, primary-source verify 8.3 U/mg activity, Km range, pH multiplier, 2–4 h active window, and 233 mg/day denominator. Verification: each value has a directly checked source and context-matched unit/assay notes.

## Review limits
I did not execute code; daemon mode review is by inspection only. Primary sources behind inherited kinetic/activity/transit/flux priors were not independently retrieved. Repository fixed-string search failed because the backend `rg` binary was unavailable; targeted reopening was limited to `open-questions.md` and `cross-validation.md`, with the rest relying on complete hash-bound shard audits. Unrelated provenance issues in later `validation-experiments.md` sections were not treated as COMP-044 blockers unless they affected COMP-044 propagation.
