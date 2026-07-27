COMP_VERDICT: clean_with_limitations
REVIEWED_SNAPSHOT: 85236300a802ebd6cc6f473ba7107f086170fff51743f3a4d832c372eb867af5
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: narrow comp-042 correction/summary only: A1 proxy route states, A2 unresolved, no route qualification
SYNTHESIS_ALLOWED_SCOPE: bounded hypothesis synthesis only; may inform validation §1.32 tracer/KPV-comparator gate
FORBIDDEN_INFERENCES: KPV clinical efficacy; intracellular target engagement; route qualification; physiological selectivity; observed synovial KPV exposure; safety; GSDMD pore-delivery platform validation or refutation; universal complete equilibration; clinical advice

# Independent comp review — comp-042

## Reviewed snapshot
Daemon reviewer; push-review manifest SHA-256 `85236300a802ebd6cc6f473ba7107f086170fff51743f3a4d832c372eb867af5`; shard coverage plus targeted repository reads matched the inspected files. No deterministic binary block was reported. Code was not executed.

## Bottom-line verdict
Clean with limitations for comp-042. The computation is internally coherent for a bounded passive-diffusion engineering prior and correctly refuses route qualification because A2 is unmeasured. `ACTION_REQUIRED: yes` is for corpus hygiene issues in touched broad pages and reproducibility/source-verification limitations, not because the comp-042 quantitative verdict is invalid.

## Implementation and constraint closure
The implemented model fits only the limited question: passive KPV influx through GSDMD pores into a well-mixed cell, plus a heuristic PepT1 comparator. It does not resolve KPV efficacy, target engagement, cytokine timing, or total pyroptotic-versus-intact-cell accumulation.

Load-bearing substitutions are clearly stated: the 10 nM threshold is an extracellular PepT1-positive cell-assay observation, not an intracellular IC50 or pharmacodynamic threshold; route concentrations are design spaces, not measured synovial exposures; pore count/lifetime and hindrance are assumptions/sensitivities, not KPV/GSDMD measurements.

Implementation traced: access-resistance pore permeability → equilibration fraction capped at extracellular concentration → A1 proxy ratio; PepT1 Michaelis-Menten-shaped accumulation heuristic → A2 ratio; route verdict logic blocks qualification when A2 is unresolved and blocks oral on A1. JSON `null` for absent-PepT1 infinity is explicitly disambiguated. No material code/output contradiction was found. Intracellular degradation, concurrent PepT1 in pore-forming cells, efflux, membrane potential, proton coupling, extracellular depletion, cytokine-release dynamics, local safety, and cell loss are not implemented and are correctly named as gaps.

Reproducibility limitation: `README.md` says `python3 analyze.py`, but `analyze.py` rejects every interpreter except CPython 3.14.5. That is deterministic if available, but fragile and stricter than ordinary “Python 3” reproducibility.

## Summary-fidelity audit
`outputs/summary.md`, JSON outputs, README, the interpretive page, `computational-experiments.md`, `validation-experiments.md` §1.32, `chassis-pending-interventions.md`, `gsdmd-pore-delivery-paradox.md`, and `kpv-peptide.md` are materially aligned on the comp-042 boundaries: A1 states are IA GREEN / SC YELLOW / oral RED as exposure-proxy diagnostics; A2 remains unresolved; favorable ≥3× A2 grid corners are equation diagnostics; no route qualifies; KPV is confounded by PepT1 and timing.

The broad `open-questions.md` page contains a comp-042 section that is bounded enough, but the same manifest span also contains unrelated stale/provenance issues and duplicated/forecast-like material. Those do not invalidate comp-042, but they require editorial action before unrestricted synthesis from that page.

## Reader-facing ownership audit
The focused KPV page owns KPV evidence, route/exposure limits, material requirements, and falsification gates. The GSDMD pore page owns the platform conjecture and keeps KPV as a confounded comparator. `validation-experiments.md` owns the wet-lab gate. `chassis-pending-interventions.md` summarizes delivery constraints without turning KPV into a chassis decision. Cross-track rankings are not improperly moved into the KPV page. No personalized treatment instruction was found in comp-042 surfaces.

## Conjecture preservation audit
Unsupported factual upgrades were mostly avoided: the comp kills only “KPV route qualifies by modeled pore influx/selectivity,” not KPV biology or the transporter-orphan pore-delivery platform. Surviving conjectures are properly framed: (1) transporter-orphan, membrane-impermeant downstream payload as cleaner pore probe; (2) KPV could affect gout-relevant priming through PepT1 before pore formation if measured in a relevant macrophage system.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/central_results.json` | generated_output | yes | Consistent with central physics/A1/A2 semantics. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/monte_carlo.json` | generated_output | yes | Supports reported A1 sampled fractions; unweighted design draws only. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/robustness_sweep.json` | generated_output | yes | Shows grid is not universally equilibrated; 10 pores/60 s fraction 0.749. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/selectivity_grid.json` | generated_output | yes | A2 grid complete; fixed peak fraction and limited varied parameters must not be overread. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/verdicts.json` | generated_output | yes | Correctly blocks route qualification with A2 unresolved. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/summary.md` | generated_output | yes | Faithful to JSON and limitations. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/README.md` | proposed_update/supporting text | yes | Accurate; reproduction requires exact CPython 3.14.5. |
| `wiki/kpv-gsdmd-pore-influx-computational.md` | proposed_update | yes | Faithful focused evidence page. |
| `wiki/computational-experiments.md` | proposed_update | yes | Consistent with comp-042 boundaries. |
| `wiki/validation-experiments.md` | proposed_update | yes | §1.32 is appropriate; unrelated broad-file issues remain. |
| `wiki/chassis-pending-interventions.md` | proposed_update | yes | Correctly says comp-042 qualifies no route and gates tracer test. |
| `wiki/open-questions.md` | proposed_update | yes | Comp-042 mention bounded; unrelated provenance/duplication issues require cleanup. |
| `wiki/gsdmd-pore-delivery-paradox.md` | affected page cross-check | yes | Consistent; preserves platform conjecture. |
| `wiki/kpv-peptide.md` | affected page cross-check | yes | Consistent; separates KPV biology from pore physics. |
| `index.md` | affected page cross-check | targeted | No comp-042 contradiction found in opened span. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 10 nM KPV proxy | inputs/provenance, `pept1...json`, summary | A1 denominator | Citation to Dalmasso; primary not independently verified here | Usable only as extracellular assay proxy. |
| IA 292 µM, SC 0.030 µM, oral 0.001 µM | `route_concentrations.json` | A1 numerator boundary | Design assumptions / named PK spaces; not measured synovial exposure | Dominant limitation; no route qualification. |
| GSDMD pore diameter/length | `pore_geometry.json`, provenance | Per-pore permeability | Structural literature cited; not reverified | Plausible geometry anchor. |
| Pores per cell 200, range 10–10,000 | `pore_geometry.json` | τ_eq and robustness | Explicit unvalidated assumption | Needs empirical pore-count data. |
| Hindrance H 0.5–1.0, central 1.0 | `kpv_properties.json` | Permeability multiplier | Engineering sensitivity, not measured | Central “rapid” result does not prove unimpeded passage. |
| Cell volume 3000 µm³ | `macrophage_geometry.json` | τ_eq denominator | Named geometry assumption | Adequate for model prior only. |
| PepT1 Km/scenarios | `pept1...json` | A2 denominator | Dalmasso/Jurkat/Caco2 anchors plus unvalidated macrophage scenarios | A2 unresolved. |
| No intracellular degradation/efflux | README, summary | Omitted loss terms | Explicit named gap | Prevents intracellular exposure conclusion. |
| CPython 3.14.5 | `analyze.py`, README | Runtime gate | Declared, not independently rerun | Reproducibility warning. |

## Affected wiki pages
- `wiki/kpv-gsdmd-pore-influx-computational.md` — already consistent — focused result page preserves proxy/selectivity limits.
- `wiki/computational-experiments.md` — already consistent — index does not upgrade to efficacy or route qualification.
- `wiki/validation-experiments.md` — change required — §1.32 is consistent, but the broad page contains unrelated future/provenance/species-threshold issues that should not be synthesized as settled evidence.
- `wiki/chassis-pending-interventions.md` — already consistent — keeps GSDMD/KPV as unresolved delivery question.
- `wiki/open-questions.md` — change required — comp-042 status is bounded, but same page has unrelated stale/provenance/duplication issues and speculative forecasting.
- `wiki/gsdmd-pore-delivery-paradox.md` — already consistent — preserves transporter-orphan conjecture and timing caveat.
- `wiki/kpv-peptide.md` — already consistent — owns KPV evidence and falsification path without dosing guidance.
- `index.md` — already consistent in targeted check — no conflicting comp-042 summary found.

## New connections or implications
COMP-042 strengthens the rationale for validation §1.32’s design separation: KPV should be a PepT1-interaction comparator, not the primary pore-delivery proof. A transporter-orphan, membrane-impermeant tracer is the cleaner first discriminating observation. Mechanistic extrapolation: if a tracer passes pore-on/off uptake but KPV shows substantial PepT1 uptake in pore-off cells, KPV remains a biology/timing question rather than a pore-selectivity payload.

## Required actions
1. Add a reproducibility note or environment lock clarifying that reruns require exact CPython 3.14.5 and that other Python 3 versions intentionally fail; verification criterion: README and reproduction contract are unambiguous.
2. Keep all propagation of comp-042 bounded to exposure-proxy/A2-unresolved language; verification criterion: no affected page says KPV route qualified, effective, safe, selective, or platform-validating.
3. Clean unrelated manifest-surfaced corpus issues in `open-questions.md` and broad `validation-experiments.md`: add access dates/provenance where registry/future/absence/cost claims are used, remove or bound speculative forecasts, and move resolved detailed verdicts out of open-question index entries where appropriate.

## Review limits
Shard auditors inspected the listed text spans completely; I performed targeted repository reads for cross-checks. Primary papers were not independently opened or verified. Code was not executed. `grep_repo` was unavailable because repository search tooling errored, so affected-surface discovery relied on shard coverage plus targeted file reads from known links. No binary artifacts were present.
