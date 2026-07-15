---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-042
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-042

Canonical review log: [`logs/comp-reviews/2026-07-15-comp-042-eeab5b5.md`](../../logs/comp-reviews/2026-07-15-comp-042-eeab5b5.md)

ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-042

## Reviewed snapshot
Independent API reviewer; daemon snapshot `commit:eeab5b53054b93544c428a476dad06a8f8fe2621`. I inspected the supplied tracked-file inventory, all supplied inputs, all six generated outputs, the trigger diff, and the explicit wiki pages included in the bundle. Repository search tooling failed because `rg` is unavailable, and the bundle truncated `validation-experiments.md` before the load-bearing §1.32 text; I attempted a chunked read but the tool-result budget was exhausted.

## Bottom-line verdict
**Action required.** The central transport arithmetic is internally consistent and the JSON strictness fix is reasonable, but the artifact still needs reconciliation on three material surfaces: README omission of the new pharmacodynamic-timing caveat, incomplete/central-only A2 selectivity sensitivity over route concentration/Km despite those ranges being declared, and independent verification of the full §1.32 validation-protocol propagation because the supplied validation page was truncated before that section.

## Implementation and constraint closure
I traced the main computational chain:

- `kpv_properties.json` supplies `D = 5e-10 m²/s`; code uses it directly in `pore_permeability_m3_s`.
- `pore_geometry.json` supplies inner diameter 20 nm, channel length 7 nm, 200 pores/cell, 300 s lifetime; code converts nm→m and computes two-sided access-resistance permeability.
- `macrophage_geometry.json` supplies 3000 µm³; code converts to `3e-15 m³`.
- `pept1_and_ic50.json` supplies immune-cell `Km_used = 700 µM`, PepT1 AR scenarios, and `IC50 = 10 nM = 0.01 µM`.
- `route_concentrations.json` supplies central IA/SC/oral synovial KPV concentrations, and lower/upper route ranges for the A1 Monte Carlo.
- Outputs are deterministic by `random.seed(42)` and `N_MC = 20000`.

Arithmetic checks by inspection:
- Per-pore permeability central `6.917e-18 m³/s` is consistent with `Dπr²/(L+πr/2)`.
- Central `τ_eq = V/(N·p) = 3e-15/(200·6.917e-18) ≈ 2.17 s`, matching `central_results.json`.
- Central route ratios over IC50 are consistent: IA `292/0.01 = 29200`, SC `0.03/0.01 = 3`, oral `0.001/0.01 = 0.1`.
- Selectivity table matches the implemented heuristic `C_healthy = AR·Km·C_ext/(Km+C_ext)` and `S = C_pyro/C_healthy`.

Constraint closure:
- Reaction/transport system is diffusive influx through GSDMD pores, not an enzyme reaction. The model correctly caps intracellular pyroptotic KPV at extracellular concentration rather than integrating unlimited flux.
- The model explicitly includes pore geometry, cell volume, exposure lifetime, pore count, extracellular concentration, and PepT1 baseline scenarios.
- Localization/access is modeled as a well-mixed macrophage compartment with pores directly connecting extracellular synovial fluid to cytosol. Diffusive intracellular mixing is not explicitly modeled, but the interpretive page notes it as likely faster than equilibration.
- Safety/off-targets are mostly conceptual rather than modeled: IA KPV flooding all synovial cells, PepT1 uptake into non-pyroptotic cells, membrane-potential effects, and intracellular degradation are caveated in the interpretive page and `selectivity_grid.json`.
- The new PD-timing caveat is biologically important: KPV is framed as upstream NLRP3/NF-κB inhibitor, while pore opening is downstream of inflammasome firing. This means the transport model alone cannot establish therapeutic-timing sufficiency for KPV.

Stored-but-unused / underused findings:
- Molecular weight, hydrodynamic radius, net charge, conduit electrostatics, and enzymatic-resistance notes are provenance support for `H = 1.0` and interpretation, but are not parameterized in code. This is acceptable if documented as rationale, but it means no hindrance/electrostatic sensitivity is performed.
- `surface_area_um2` is documented as not directly load-bearing and is unused.
- `Km_used_uM.lower/upper` and route concentration lower/upper are not used in A2 selectivity sweeps. Route ranges are used in the A1 Monte Carlo; Km ranges are not used. This is a material sensitivity gap because A2 is the experiment’s decisive uncertainty.
- PepT1 AR scenarios are deterministic bins, not probabilistic priors; the verdict treats the unknown expression state qualitatively. That is acceptable if kept explicitly “unquantifiable,” but it does not support probability language about selectivity.
- The JSON-safe conversion replaces `Infinity` with `null`. This fixes strict JSON validity, but `null` is semantically ambiguous unless downstream documentation states that `null` in `selectivity_ratio` can mean “infinite because healthy-cell denominator is zero.”

## Summary-fidelity audit
Generated outputs are mostly internally consistent with each other:

- `central_results.json`, `selectivity_grid.json`, `verdicts.json`, and `outputs/summary.md` agree on central A1 and A2 labels.
- The trigger diff’s strict-JSON change is reflected in `central_results.json` and `selectivity_grid.json`: `selectivity_ratio` for PepT1-absent scenarios is now `null`, while the human summary still displays `inf`.
- `outputs/summary.md` now includes the PD-timing caveat and correctly states that transport sufficiency is not therapeutic-timing sufficiency for KPV.
- `verdicts.json` encodes A2 as `YELLOW-unquantifiable`, matching the revised summary language.

Mismatches or propagation gaps:
- **README.md does not include the new PD-timing caveat** even though the trigger diff added it to `outputs/summary.md` and the interpretive page treats it as one of the two decisive reasons KPV is the wrong proof-of-concept payload. The README headline still frames the issue primarily as PepT1 confounding. This is a summary-fidelity gap.
- `README.md` also says “No route clears both a therapeutic AND a meaningful-selectivity threshold,” but the implementation only evaluates A2 at central route concentration and central Km. It should either say “at central assumptions and with confidence” or include the missing A2 sensitivity.
- `wiki/kpv-gsdmd-pore-influx-computational.md`, `wiki/gsdmd-pore-delivery-paradox.md`, `wiki/kpv-peptide.md`, and `wiki/computational-experiments.md` are broadly consistent with the artifact: KPV transport works; KPV selectivity is not established; the platform thesis remains open for transporter-orphan, downstream-acting payloads.
- The explicit computational-experiments entry is stronger than the README by including the PD-timing “conceptual kill” and the “downstream-acting transporter-orphan payload” reframe.
- `delivery-route-matrix.md` does not appear to make a conflicting KPV/GSDMD claim in the inspected portion.
- `nlrp3-exploit-map.md` still lists KPV as a CP1 payload and OE engineering-pending candidate, but does not appear to rely on GSDMD pore selectivity. No direct contradiction found.
- The bundle says `validation-experiments.md` §1.32 is reframed, and the paradox page points to it as canonical. I could not inspect §1.32 itself because the supplied page was truncated before that section and the tool budget was exhausted. This remains an unresolved fidelity check.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/central_results.json` | generated_output | Yes | Arithmetic consistent with code and inputs. `Infinity` now encoded as `null`; needs explicit semantic documentation for absent-PepT1 selectivity. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/monte_carlo.json` | generated_output | Yes | A1 Monte Carlo distributions match the described route-level conclusions. Does not cover A2/PepT1/Km selectivity uncertainty. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/robustness_sweep.json` | generated_output | Yes | Robustness sweep supports A1 flux sufficiency for ≥10 pores/cell under central route/IC50 assumptions. It does not address A2. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/selectivity_grid.json` | generated_output | Yes | Central selectivity grid matches code. Includes useful caveats that the healthy-cell curve is optimistic and that KPV timing is upstream/downstream mismatched. Lacks sensitivity over declared route and Km ranges. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/summary.md` | generated_output | Yes | Faithful to current code outputs and includes the new PD-timing caveat. Strong “wrong proof-of-concept payload” language is supported as mechanistic extrapolation, not clinical evidence. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/verdicts.json` | generated_output | Yes | Matches implemented decision logic. A2 is central-scenario-count based, not a full uncertainty analysis. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/analyze.py` | executable changed in trigger | Yes | Strict JSON conversion is implemented with `allow_nan=False`. Summary text update implemented. A2 sensitivity gap remains. |
| Separate wiki proposed updates | proposed_update | No separate proposed wiki diff in trigger | Existing explicit pages were reviewed from bundle where provided; full `validation-experiments.md` §1.32 was not inspectable. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| KPV aqueous diffusion coefficient `4–6e-10 m²/s`, central `5e-10` | `inputs/kpv_properties.json`, `inputs/provenance.md` | Directly used in permeability and MC | Artifact cites Stokes-Einstein estimate; primary-source verification not independently performed | Acceptable estimated physical input; low sensitivity for qualitative A1. |
| GSDMD inner diameter central 20 nm, range 10–21.5 nm | `inputs/pore_geometry.json`, `inputs/provenance.md` | Directly used in central and MC permeability | Artifact cites Sborgi 2016 and Xia 2021; not independently primary-verified here | Plausible and consistent with corpus; A1 robust over range. |
| Channel length central 7 nm, range 4–10 nm | `inputs/pore_geometry.json` | Directly used in permeability and MC | Estimated from membrane/barrel geometry | Low sensitivity because access resistance dominates; acceptable. |
| Pores/cell central 200, range 10–10000 | `inputs/pore_geometry.json`; robustness sweep | Directly used in central and MC; sweep includes 1–10000 | Named assumption; no primary per-cell count | A1 conclusion depends on ≥10 pores/cell; artifact labels this correctly. |
| Pore lifetime 60–1800 s, central 300 s | `inputs/pore_geometry.json` | Directly used in central/MC/sweep | Corpus open question, not primary measured per KPV context | A1 conclusion robust if pores persist ≥60 s and ≥10 pores/cell. |
| Macrophage volume central 3000 µm³ | `inputs/macrophage_geometry.json` | Directly used in τ_eq | Standard cell-biology estimate; not independently verified | Reasonable order-of-magnitude input. |
| KPV IC50 proxy 10 nM, range 1–100 nM | `inputs/pept1_and_ic50.json`, `provenance.md` | Central and MC A1 threshold | Artifact cites Dalmasso 2008 cell-assay result; primary not independently verified | Important caveat: extracellular reporter value in PepT1+ cells, not direct intracellular target Kd. SC margin remains assumption-limited. |
| PepT1 Km central 700 µM; lower/upper 160–1000 µM | `inputs/pept1_and_ic50.json` | Central selectivity only uses 700 µM; lower/upper not used | Artifact cites Dalmasso 2008 epithelial/Jurkat kinetics; primary not independently verified | **Actionable sensitivity gap** for A2, especially IA. |
| PepT1 AR scenarios 0/0.3/1/3 | `inputs/pept1_and_ic50.json` | Deterministic scenario grid and verdict count | Named scenario band; synovial macrophage expression is a named gap | Correctly treated as unquantifiable, not measured. |
| Synovial IA KPV 292 µM central, 15–1460 µM range | `inputs/route_concentrations.json` | Central A1/A2 uses 292; MC A1 uses range | IA computed from dose/volume; not source-verified beyond arithmetic | A1 robust; A2 should be swept over the range or explicitly central-only. |
| Synovial SC KPV 30 nM central, 3–200 nM range | `inputs/route_concentrations.json` | Central A1/A2 uses 30 nM; MC A1 uses range | Named PK design-space assumption | SC A1 is thin; correctly YELLOW. |
| Oral synovial KPV 1 nM central, 0.1–3 nM range | `inputs/route_concentrations.json` | Central A1/A2 uses 1 nM; MC A1 uses range | Named PK assumption | A1 RED is supported under assumptions. |
| Healthy-cell PepT1 saturation heuristic | `analyze.py`, `selectivity_grid.json caveat_S_is_optimistic` | Determines A2 selectivity ratios | Heuristic; no measured synovial macrophage steady-state | Good that artifact caveats it; should avoid overprecise “passes/fails” language beyond central scenario. |
| KPV is upstream while GSDMD pores are downstream | `outputs/summary.md`, `selectivity_grid.json`, interpretive page | Not encoded in numeric verdict; interpretive caveat | Mechanistic pathway claim from corpus/literature; not computationally modeled | Load-bearing conceptual limitation; must be propagated to README and validation framing. |
| Strict JSON validity after replacing nonfinite floats | trigger diff, output JSON files | `_json_safe` converts `inf`, `nan` to `null`; `allow_nan=False` | Directly inspectable in code and outputs | Fix works technically; add metadata/note so `null` is not mistaken for missing data. |

## Affected wiki pages
- `wiki/kpv-gsdmd-pore-influx-computational.md` — already consistent — includes transport result, PepT1 confounding, PD-timing mismatch, transporter-orphan reframe, limitations, and reproduction.
- `wiki/computational-experiments.md` — already consistent — comp-042 entry includes A1/A2 split, PD-timing conceptual kill, and next-gate framing.
- `wiki/gsdmd-pore-delivery-paradox.md` — already consistent — Open Question #4 is marked answered for small solutes; KPV is reframed as wrong payload; Ac-FLTD-CMK/downstream transporter-orphan payload emphasized.
- `wiki/kpv-peptide.md` — already consistent — adds “GSDMD Pore Self-Delivery — Evaluated, Not Selective for KPV” and keeps KPV evidence preclinical/mechanistic.
- `wiki/delivery-route-matrix.md` — already consistent in inspected portion — no conflicting KPV pore-selectivity claim found.
- `wiki/nlrp3-exploit-map.md` — already consistent in inspected portion — lists KPV as CP1/PepT1-mediated anti-inflammatory, not as a validated GSDMD-pore-selective payload.
- `wiki/validation-experiments.md` — unresolved / change may be required — bundle was truncated before §1.32, which is the key wet-lab propagation surface for the redesigned transporter-orphan tracer + PepT1-blockade experiment. Needs full-section verification.
- `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/README.md` — change required — omits the new PD-timing caveat now present in `outputs/summary.md` and the interpretive wiki page.

## New connections or implications
- The artifact turns pore lifetime from an open KPV-specific worry into a broader small-solute design rule: for ~1 nm solutes, GSDMD-pore lifetime is unlikely to be the limiting transport variable; payload choice and target timing dominate.
- The ideal pore-self-delivery probe should be **transporter-orphan and downstream-acting**. KPV fails both design criteria; Ac-FLTD-CMK or a membrane-impermeant caspase/GSDMD-pathway tracer is a better proof-of-concept.
- Intracellular lability is not just a stability caveat: a labile payload could be more pore-selective because intact cells cannot maintain exposure via low constitutive uptake, whereas an open pore can sustain flux. KPV’s enzymatic resistance cuts against pore selectivity.
- IA brute-force extracellular exposure is not equivalent to pore selectivity. Even if a high-dose IA sensitivity scenario produced a ≥3× heuristic intracellular ratio, it would not establish tissue sparing or a true Trojan-horse mechanism.

## Required actions
1. **Update the comp-042 README.** Add the PD-timing caveat: KPV is upstream of inflammasome firing while GSDMD pores form downstream, so pore influx is not therapeutic-timing sufficiency. Verification criterion: README headline/verdict/limitations name both PepT1 confounding and PD timing as independent reasons KPV is the wrong proof-of-concept payload.
2. **Add or explicitly disclaim A2 sensitivity.** Either extend `analyze.py` outputs to sweep selectivity over declared `Km_used_uM` lower/central/upper and route concentration lower/central/upper, or state in README/summary/verdicts that A2 ratios are central-scenario diagnostics only. Verification criterion: no “no route clears both filters” wording is left ambiguous between central-only and full uncertainty-space claims.
3. **Document JSON `null` semantics.** Add a machine-readable note in relevant JSON outputs or README that `selectivity_ratio: null` in absent-PepT1 rows encodes mathematical infinity after strict-JSON conversion, not missing data. Verification criterion: strict JSON remains valid and downstream readers can distinguish infinite selectivity from unknown selectivity.
4. **Verify `validation-experiments.md` §1.32.** Confirm the full section reflects the comp-042 reframe: primary transporter-orphan membrane-impermeant tracer, KPV only as PepT1-confounded comparator, PepT1 inhibition/knockdown arm, and no claim that KPV efficacy via pores is established. Verification criterion: independent reviewer can inspect the full §1.32 text and mark it consistent.

## Review limits
- I did not execute `analyze.py`; reproducibility was assessed by code and output inspection only.
- I did not independently verify primary sources such as Dalmasso 2008, Sborgi 2016, or Xia 2021; provenance status is based on the artifact’s citation/provenance table plus arithmetic checks.
- Repository fixed-string search failed because the environment lacks `rg`; I used directory listing and targeted file reads instead.
- `validation-experiments.md` was supplied only in a truncated form and the tool-result budget was exhausted before I could inspect §1.32, the most relevant validation section.
- Prior review logs were not inspected; none were included in the tracked-file inventory or supplied bundle.
