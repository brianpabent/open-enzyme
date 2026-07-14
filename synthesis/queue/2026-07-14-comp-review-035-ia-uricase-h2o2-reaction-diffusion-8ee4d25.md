---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-035
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-035

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-035-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-035-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-035

## Bottom-line verdict

**Action required — headline GREEN is not decision-grade as written.** The committed code plausibly reproduces the reported central distributions, but the artifact-summary contract overstates what was modeled. Several load-bearing implementation choices are hardcoded or inconsistent with inputs, edge cases do not perturb all architectures as claimed, sensitivity reports include irrelevant variables, and wiki propagation upgrades a Phase-0 model into “H₂O₂ risk closed” / “chassis selection can advance” language that is stronger than the artifact supports.

## Implementation and constraint closure

I traced the JSON inputs through `analyze.py` and compared them to the committed outputs and wiki summaries.

**What the computation actually answers**

- The executable mostly computes **steady-state bulk [H₂O₂] under assumed constant uricase saturation and catalase first-order scavenging**, not a full synovial-tissue boundary reaction-diffusion exposure model.
- For free co-formulated and fusion cases, the core steady-state is essentially:

  `C_H2O2 = v_URI × [URI active sites] × escape_factor / (k_clear + (kcat/Km)_CAT × [CAT active sites])`

- For Pickering, the code computes a shell escape fraction, but the reported GREEN bulk result is dominated by a hardcoded total catalase amount and fixed URI:CAT ratio; the shell result says nearly all H₂O₂ escapes the shell.
- This is useful first-pass chemistry, but it does **not** close:
  - finite substrate mass and crystal dissolution transport,
  - actual IA residence time and exposure duration,
  - joint surface/tissue diffusion gradients,
  - local peaks at crystals or injection depots,
  - oxygen limitation/replenishment,
  - in vivo catalase degradation/immune inactivation,
  - tissue toxicity for sustained low-µM H₂O₂.

**Stored-but-unused or misleading inputs**

- `absolute_loading_per_dose` is present in `architecture_geometry.json` but the Pickering code does **not** read it. Instead it hardcodes `0.23e-3 g` catalase and `240e3 g/mol`.
- The input values are internally suspicious: `total_protein_concentration_mg_per_mL = 2.39` and `dose_volume_uL = 20` imply ~0.0478 mg total protein per 20 µL, while the same object lists `uri_mg = 0.92` and `cat_mg = 0.23` (~1.15 mg total). That needs source-level reconciliation.
- `URI_to_CAT_ratio` is passed into `pickering_steady_state_h2o2()` but never used.
- Uricase and catalase active-site counts are hardcoded inconsistently:
  - Free model uses 4 uricase active sites and 4 catalase active sites per molecule.
  - Fusion model assumes 1 uricase active site per fusion but 4 catalase active sites.
  - Pickering treats interfacial `n_URI_per_droplet` as production sites without clearly resolving molecule-vs-active-site meaning.
- `stoichiometry.h2o2_per_urate` and `stoichiometry.h2o2_per_catalase_turnover` are present but not used. A factor-of-two catalase convention issue may be buried depending on how `kcat/Km` is defined.
- `Km_h2o2_M` and `kcat_per_s` for catalase are stored but not used directly; only `kcat_over_km_per_M_per_s` is implemented. That is acceptable for the linear regime, but the summary should state that the model depends on the derived specificity constant, not independently on kcat and Km.
- `h2o2_diffusion_in_oil_phase_m2_per_s` is stored but unused; trans-oil escape is not implemented.
- Joint surface area and cartilage thickness are stored but unused; therefore the “synovial-tissue boundary” is not spatially resolved beyond a well-mixed bulk surrogate.

**Edge-case closure problems**

- `low_CAT_dose_1uM`, `high_dose_100uM`, and `uneven_free_URI_100uM_CAT_1uM` do **not** perturb Pickering URI/CAT loading. Pickering uses the hardcoded 0.23 mg catalase and fixed URI fraction.
- `low_CAT_dose_1uM` and `uneven_free_URI_100uM_CAT_1uM` do not create an analogous uneven-stoichiometry fusion case; fusion remains fixed at its central 1:1 architecture unless `fusion_concentration_uM` is changed.
- The summary’s statement that the edge cases show Pickering/fusion robustness against mis-engineered URI:CAT is therefore only partly implemented.
- `small_joint_MTP1_0.3mL` changes joint volume but not concentration/dose in free/fusion, and in Pickering both production and catalase destruction scale in ways that make bulk concentration nearly unchanged. This does not test the stated concern of a fixed injected dose into a smaller joint with realistic residence/local peak consequences.

**Sensitivity-analysis closure problems**

- Sensitivity analysis is run over all sampled variables for every architecture, including variables irrelevant to that architecture.
- This produces spurious “top drivers” such as `pick_interfacial_density_per_um2` appearing in fusion and free-coformulated driver lists.
- Architecture-specific sensitivity summaries should filter to variables actually used by that architecture, or explicitly label cross-architecture unused variables as Monte Carlo noise.

**Output-field derivation issue**

- `escape_flux.json` labels fusion escape as `"fusion_total_escape_fraction_through_intra_and_bulk"`, but the code writes `stats([(1 - p) for p in fusion_Pintra])`, i.e. only the non-intramolecular-capture fraction. It ignores the implemented bulk capture term (`f_total_escape`, `P_capture_bulk`).
- This is an output-label/implementation mismatch.

**Constraint closure**

- **Reaction substrates/products:** Uricase urate + O₂ + H₂O → H₂O₂/allantoin products are named, but O₂ availability is not modeled. Ignoring O₂ is conservative for H₂O₂ safety but means the model cannot address efficacy or local hypoxia/O₂ depletion.
- **Operating regime:** Uricase is usually saturated in the model because urate is sampled 0.5–5 mM vs Km 15–50 µM. This is a high-H₂O₂-flux assumption and may be conservative for safety, but it is not a physiologic reaction-rate validation.
- **Catalase regime:** Linear first-order catalase is reasonable for µM H₂O₂ if the `kcat/Km` value and active-site concentration are correct.
- **Mass balance/time:** The model is steady-state only. It does not integrate cumulative exposure, finite urate crystal mass, injection residence, enzyme decay, lymphatic clearance of enzymes, or replenishment.
- **Localization/access:** Pickering shell diffusion is represented, but joint-scale tissue gradients are not. Fusion active-site separation is a design-space prior, not a measured structure. Free co-formulation assumes uniform mixing.
- **Coproducts/off-targets/safety:** H₂O₂ is the only safety variable. Oxygen production, oxidative damage dynamics, local protein oxidation, methotrexate/mannose/oil components in PEBR, immune response, and injection safety are outside the model.
- **Dominant uncertainties:** Catalase activity is sampled and dominates. But toxicity thresholds, actual dose/loading, fusion geometry, enzyme stability in vivo, and tissue exposure-time thresholds are not adequately propagated into the headline verdict.

## Summary-fidelity audit

**README / `outputs/summary.md` / interpretive wiki**

- The reported numeric outputs match the committed JSON outputs by inspection.
- However, interpretive claims are stronger than the implementation:
  - “H₂O₂ housekeeping risk resolved/closed” should be softened to “not prohibitive under this well-mixed, steady-state, assumed-catalase-capacity model.”
  - “Architecture chassis-selection question can advance” should be gated on dose/loading reconciliation, Amplex Red validation, and corrected edge cases.
  - “Tissue-level effects are downstream; if sub-µM then downstream effects are by-construction low” is too strong for Phase 0 and for an unvalidated steady-state toxicity band.
- The “FRET proximity is not the Pickering safety mechanism” conclusion is supported by the implemented low `Da_shell` and high shell escape fraction, but the alternative “bulk catalase capacity closes safety” conclusion depends on hardcoded and partly inconsistent dosing assumptions.

**`wiki/computational-experiments.md`**

- The comp-035 entry mirrors the artifact numbers.
- It should be updated to state that the result is **model-limited / action-required**, not a clean GREEN closure.
- It should not imply that the “max 120” worst case is a validated physiologic maximum; it is a Monte Carlo corner from the implemented priors.

**`wiki/chassis-pending-interventions.md`**

- The page currently says the H₂O₂ biochemistry gate is “resolved” and that updated chassis-selection criteria follow from comp-035.
- This is too strong until implementation issues are fixed and the Amplex Red handoff is registered/executed.

**`wiki/delivery-route-matrix.md`**

- The route-agnostic “catalase capacity principle” is directionally useful, but as written it leans too hard on comp-035 as a validation anchor.
- It should be framed as a **design rule suggested by the model**, pending empirical H₂O₂ measurement and corrected dose accounting.

**`wiki/gout-kill-chain-delivery-routes.md`**

- The IA uricase section repeats that the H₂O₂ safety gate is resolved by comp-035.
- This should be softened and should carry the same caveats: well-mixed model, central threshold derivation, unresolved dose/loading, no tissue toxicity curve, no local peak/exposure-time validation.

**`wiki/engineered-koji-protocol.md` / `wiki/uricase.md`**

- These pages contain broader H₂O₂/catalase framing. Some language already acknowledges topology and measurement gates, but `uricase.md` still says expected gut-lumen H₂O₂ would be “minimal and rapidly scavenged—not a safety concern,” which is stronger than current evidence.
- The comp-035 result should not be used as blanket proof that any uricase format is safe if catalase is nearby; it only supports a limited IA steady-state model.

**`wiki/validation-experiments.md`**

- The artifact repeatedly names Amplex Red measurement as the cheapest next wet-lab gate, but I did not find a comp-035-specific IA Amplex Red validation section in the inspected part of `validation-experiments.md`. The page scope note says chassis-pending experiments may live on their home pages, so this is not necessarily an index violation, but the handoff should be made explicit somewhere authoritative.

**Reproduction contract**

- README says:

  `cd experiments/comp-035-ia-uricase-h2o2-reaction-diffusion`

  but the tracked path is:

  `wiki/etc/experiments/comp-035-ia-uricase-h2o2-reaction-diffusion`

- The interpretive page uses `cd etc/experiments/...`, also ambiguous depending on starting directory.
- The code is stdlib-only and deterministic by seed, and outputs appear self-consistent with the code. I did not execute it.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| All three architectures GREEN under reference conditions | README; `outputs/summary.md`; `architecture_ranking.json` | Median `C_joint_bulk_uM` compared to 10 µM | Computed from committed code/outputs, not independently executed | **Needs rerun after fixes; current headline overstates closure** |
| Pickering median 0.19 µM, p95 1.1 µM | `steady_state_h2o2.json`; README | Derived from hardcoded CAT mass, sampled kinetics/geometry | Reproducible by inspection but dose/input mismatch unresolved | **Numerically traceable, decision-limited** |
| Fusion median 0.034 µM, p95 0.20 µM | `steady_state_h2o2.json` | Uses assumed 1–100 µM fusion, `r_capture/L` | Active-site separation is design-space prior, not measured | **Model output; not architecture-validated** |
| Free median 0.19 µM, p95 7.2 µM, max ~120 µM | `steady_state_h2o2.json`; `architecture_ranking.json` | Uses sampled URI/CAT concentration priors | Priors are design-space, not sourced to an IA dosing study | **Traceable but prior-dependent** |
| Toxicity GREEN <10 µM, RED >100 µM | `toxicity_thresholds.json`; README; interpretive page | Central thresholds used only; lower/upper uncertainty not propagated | Derived from Schalkwijk + in-vitro bolus literature; no steady-state synovial curve | **Load-bearing mechanistic extrapolation; must stay caveated** |
| Catalase `kcat/Km = 4e7 M⁻¹ s⁻¹`, range 1e7–4e8 | `kinetic_constants.json`; provenance | Dominant rate constant in all models | Citation strings/secondary provenance available; primary sources not in artifact | **Plausible but not independently primary-verified here** |
| Uricase `kcat = 8–20 s⁻¹`, `Km = 15–50 µM` | `kinetic_constants.json` | Drives H₂O₂ production | Provenance says order-of-magnitude verified; primary table fetch deferred | **Accept as broad prior; not primary-verified** |
| Pickering 0.23 mg CAT total | Hardcoded in `analyze.py`; also in `architecture_geometry.json` | Determines Pickering droplet count and bulk catalase | Input object conflicts with total protein concentration × dose volume | **Action required: reconcile source/unit and stop hardcoding** |
| Liu 2025 total protein 2.39 mg/mL; URI 0.92 mg, CAT 0.23 mg; dose 20 µL | `architecture_geometry.json`; provenance | Mostly not used directly | Provenance claims grep verification, but artifact lacks primary source text | **Internally inconsistent as stored; action required** |
| Pickering interfacial density ~1e4/µm² | `architecture_geometry.json` | Used in shell Da/local droplet outputs | Explicitly flagged [UNVERIFIED-AS-LITERAL] | **Caveated; not load-bearing for bulk but load-bearing for Da/local claims** |
| FRET <10 nm not safety mechanism | README; interpretive page; `damkohler_per_architecture.json` | Shell Da median 0.0045; escape fraction median 0.998 | Based on model; Liu FRET source not primary-verified here | **Supported within model** |
| Bulk catalase is safety mechanism | README; interpretive page | Bulk destruction term dominates | Depends on dose/loading, active-site convention, in vivo stability | **Directionally plausible; not closed** |
| Fusion active-site separation 1–5 nm | `architecture_geometry.json` | Controls `P_capture_intra` | [ESTIMATED — DESIGN-SPACE PRIOR] | **Appropriate as prior; cannot support strong fusion ranking** |
| Free uneven URI 100 µM / CAT 1 µM gives 31.6 µM YELLOW | `edge_case_scenarios.json` | Implemented only for free coformulated | Design-space edge case | **Traceable, but not a cross-architecture robustness test** |
| Small MTP1 joint remains GREEN | `edge_case_scenarios.json` | Changes volume only | MTP1 volume estimated | **Misleading; does not test fixed-dose local peaks/residence** |
| Sensitivity: catalase top driver r≈−0.95 | `sensitivity_analysis.json` | Spearman over all sampled variables | Computed, but irrelevant variables included | **Core driver likely real; table needs filtering** |
| Reproduction command | README; output summary; interpretive page | Human reproduction path | Paths inconsistent with tracked repo path | **Action required** |
| Primary-source verification completed | README “Hard constraints honored”; provenance | Not used in code, but supports trust | Artifact contains citation/provenance notes, not primary source files | **Reviewer cannot verify; should not claim more than provenance-note verification** |

## Affected wiki pages

- `wiki/intra-articular-uricase-h2o2-reaction-diffusion-computational.md` — **change required** — soften “resolved/closed” language; add implementation caveats, dose/input inconsistency, edge-case limitations, and corrected reproduction path.
- `wiki/computational-experiments.md` — **change required** — comp-035 index entry should no longer present a clean GREEN; mark as action-required/model-limited pending rerun.
- `wiki/chassis-pending-interventions.md` — **change required** — §6 currently treats comp-035 as closing the H₂O₂ gate and advancing chassis selection; this should be gated on corrected model + Amplex Red validation.
- `wiki/delivery-route-matrix.md` — **change required** — catalase-capacity principle should be labeled as a model-derived design rule, not as an empirically validated route-agnostic closure.
- `wiki/gout-kill-chain-delivery-routes.md` — **change required** — IA uricase section repeats “H₂O₂ safety gate resolved”; needs same caveats and validation handoff.
- `wiki/engineered-koji-protocol.md` — **partly consistent / minor change required** — newer topology-gate language is cautious, but any blanket use of comp-035 to generalize H₂O₂ closure should be softened.
- `wiki/uricase.md` — **change required** — “minimal and rapidly scavenged—not a safety concern” for gut-lumen H₂O₂ is too strong and should be harmonized with topology/catalase-capacity measurement gates.
- `wiki/validation-experiments.md` — **change required or explicit deferral required** — if Amplex Red is the load-bearing comp-035 handoff, add an IA uricase/catalase H₂O₂ measurement entry or explicitly keep it on the chassis-pending page with a verification criterion.
- `wiki/etc/experiments/comp-035-ia-uricase-h2o2-reaction-diffusion/README.md` — **change required** — fix hardcoded/reproduction-path/dose language and summary claims after rerun.
- `wiki/etc/experiments/comp-035-ia-uricase-h2o2-reaction-diffusion/outputs/summary.md` — **change required** — regenerate after code fixes; current summary inherits misleading edge-case and sensitivity tables.

## New connections or implications

- The model’s most robust useful insight is **not “IA uricase is safe,” but “same-ratio uricase+catalase steady-state H₂O₂ is controlled primarily by the URI:CAT activity ratio, not by total dose, under catalase-dominated well-mixed assumptions.”** That implies safety and efficacy can decouple: lowering both URI and CAT may keep [H₂O₂] low while also failing to dissolve meaningful urate.
- The Pickering result weakens “nanometer proximity” marketing claims, but it also weakens some OE chassis rhetoric: **peroxisomal or residue-level co-localization is not automatically the key variable; effective catalase capacity at the reaction site is.** That should be framed as a hypothesis/design principle pending empirical H₂O₂ flux data.
- A proper next model should jointly report **H₂O₂ steady state and urate-dissolution flux**. The current code can make unsafe and ineffective designs look similarly GREEN if URI:CAT ratio is preserved.
- The edge-case results imply a practical wet-lab design: titrate **URI:CAT ratio independently from total enzyme dose** in Amplex Red assays. The current written handoff asks for Amplex Red but does not explicitly require ratio × dose factorial separation.

## Required actions

1. **Fix Pickering dose/input handling in `analyze.py` and `architecture_geometry.json`.**  
   Verification criterion: no hardcoded `0.23e-3` or `240e3` values remain where JSON inputs exist; Liu 2025 loading units are reconciled so `total_protein_concentration_mg_per_mL × dose_volume_uL` matches stored URI/CAT mass or the discrepancy is explicitly represented as separate source quantities.

2. **Correct molecule-vs-active-site and URI:CAT stoichiometry handling across all architectures.**  
   Verification criterion: active-site counts come from `kinetic_constants.json`, `URI_to_CAT_ratio` is either used or removed, and Pickering/fusion/free formulas document whether concentrations are molecules, tetramers, monomers, or active sites.

3. **Repair edge-case scenarios.**  
   Verification criterion: every named edge case perturbs all architectures where conceptually applicable, or is renamed as architecture-specific. Include at minimum a URI:CAT ratio sweep and a total-dose × ratio sweep, with fixed-dose small-joint cases separated from fixed-concentration cases.

4. **Repair sensitivity analysis.**  
   Verification criterion: architecture-specific sensitivity tables include only variables used by that architecture; irrelevant variables no longer appear as top drivers.

5. **Fix `escape_flux.json` fusion field derivation.**  
   Verification criterion: the reported fusion escape fraction uses the implemented total escape term (`f_total_escape`) or the label is changed to “non-intramolecular-capture fraction.”

6. **Propagate toxicity-threshold uncertainty.**  
   Verification criterion: outputs show verdict sensitivity for 5/10/20 µM GREEN thresholds and 50/100/200 µM RED thresholds, or explicitly state why central-only thresholding is being retained.

7. **Regenerate all outputs and summaries after code changes.**  
   Verification criterion: committed JSON and `outputs/summary.md` correspond to the corrected code, with updated `elapsed`/seed metadata and no stale numbers.

8. **Fix reproduction paths.**  
   Verification criterion: README and output summary use a repo-correct command such as `cd wiki/etc/experiments/comp-035-ia-uricase-h2o2-reaction-diffusion && python3 analyze.py`, or document the intended working directory unambiguously.

9. **Update affected wiki pages to downgrade closure language.**  
   Verification criterion: no top-level page says comp-035 “resolved,” “closed,” or “cleared” the H₂O₂ risk without immediately qualifying that this is a Phase-0, steady-state, well-mixed model pending corrected rerun and Amplex Red validation.

10. **Register the wet-lab handoff explicitly.**  
   Verification criterion: either `validation-experiments.md` or the chassis-pending IA uricase section contains a concrete Amplex Red URI:CAT ratio × total-dose assay with pass/fail criteria and realistic substrate loading.

11. **Primary-source verification follow-up.**  
   Verification criterion: Liu 2025 loading/density/activity units and catalase/uricase kinetic constants are verified against accessible primary source text or marked as citation-string/provenance-only, not “primary verified.”

## Review limits

- I did not execute `analyze.py`; reproducibility was assessed by code/output inspection.
- Repository fixed-string search failed because the tool backend lacked `rg`; affected-page discovery relied on the provided bundle plus direct reads of selected omitted/relevant pages.
- I did not independently fetch or verify primary literature. Provenance statuses are therefore assessed from artifact notes, not primary-source inspection.
- Only bounded portions of large wiki pages were inspected where needed; `validation-experiments.md` is very large and was sampled around relevant sections.
- I did not inspect every hypothesis card or priority table; no explicit comp-035 hypothesis card was included in the bundle.
