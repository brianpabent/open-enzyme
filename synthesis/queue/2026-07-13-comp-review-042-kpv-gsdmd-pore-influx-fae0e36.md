---
type: comp-review
sweep_date: 2026-07-13
sweep_sha: fae0e36
comp: comp-042
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-042

Canonical review log: [`logs/comp-reviews/2026-07-13-comp-042-fae0e36.md`](../../logs/comp-reviews/2026-07-13-comp-042-fae0e36.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-042

## Bottom-line verdict

Action required. The central transport arithmetic is plausible and internally reproducible by inspection, but the artifact has material contract issues: non-standard JSON outputs (`Infinity`), inconsistent A2 labels (`YELLOW-unquantifiable` in `verdicts.json` vs. “RED-unquantifiable” in `summary.md`), stored sensitivity inputs not actually propagated into A2, and incomplete propagation of the strongest peer-review caveat (PD timing mismatch) into README/output summary. The quantitative A1 pore-equilibration result is directionally credible; the KPV-specific selective-Trojan-horse conclusion is qualitatively credible but should be tightened and reconciled.

## Implementation and constraint closure

I traced the model from inputs to code to outputs:

- **Pore transport math:** `p_pore = 1/(L/(Dπr²)+1/(2Dr))` is equivalent to the README formula with two-sided access resistance. With D = 5e-10 m²/s, r = 10 nm, L = 7 nm, p ≈ 6.92e-18 m³/s; with V = 3000 µm³ and 200 pores, τ ≈ 2.17 s. The central A1 result is arithmetically coherent.
- **Mass-balance cap:** The model correctly avoids the “moles in over lifetime / cell volume” overestimate by capping intracellular concentration at extracellular concentration through first-order equilibration. This is an important correction and is implemented.
- **Route concentrations:** IA/SC/oral concentrations are not computed from dose/MW/PK in code; they are precomputed JSON inputs. Therefore the MW, IA dose/synovial-volume derivation, SC Vd/partition assumptions, and oral systemic assumptions are documentation/provenance inputs, not executable derivations.
- **Stored-but-unused or under-used inputs:**
  - `hydrodynamic_radius_nm`, `net_charge_pH7p4`, and `conduit_electrostatics` justify `H = 1.0` but are not used; hindrance is hard-coded and not swept.
  - `molecular_weight_Da` is not used by code; route concentrations are already entered as µM.
  - `surface_area_um2` is explicitly non-load-bearing and unused.
  - `Km_epithelial_uM`, `Km_immune_uM`, and `Km_used_uM.lower/upper` are stored, but only `Km_used_uM.central` is used. A2 sensitivity to Km is therefore not actually propagated.
  - `pept1_macrophage_expression` is documentation only; scenario AR values are used.
- **A2 model:** The healthy-cell PepT1 model is explicitly heuristic. It uses a saturating concentration ceiling `C_in_max = AR_lin * Km`, not a transporter/efflux kinetic model. This is acceptable as a scenario tool only because the artifact labels it optimistic; it should not be described as a physiologic steady-state derivation.
- **JSON reproducibility defect:** Committed JSON files contain `Infinity` for absent-PepT1 selectivity. Python can emit/parse this by default, but it is not valid JSON under the JSON standard. This weakens the committed-output contract for non-Python consumers.
- **Time/exposure constraints:** The model answers “if extracellular KPV is present at the stated concentration while pores are open, how fast does the cell equilibrate?” It does not model synovial concentration-time curves, SC peak duration, timing of dosing relative to pyroptotic events, or residence/exposure synchronization. This is most important for the marginal SC claim.
- **Reaction/cofactor closure:** There is no enzymatic reaction modeled for KPV; substrates/products are not relevant except PepT1 proton-coupled transport, which is collapsed into AR scenarios. GSDMD pore consequences for membrane potential are discussed but not explicitly modeled except by capping pyroptotic `C_in` at `C_ext`.
- **Localization/transport closure:** Pore access and compartment mixing are treated simply but plausibly for a ~1 nm solute. The unmeasured dominant localization variable is not pore geometry but synovial-macrophage PepT1 function and timing of KPV target engagement.
- **Safety/off-target closure:** IA KPV is assumed to flood synovial extracellular space; off-target healthy-cell uptake and loss of tissue-level selectivity are discussed, but no toxicity/safety model is implemented. That is acceptable for Phase 0 if not overclaimed.

## Summary-fidelity audit

Several surfaces are already well reconciled, but action is still required.

- **README vs code/outputs:** The README’s central A1 numbers match the code outputs. However, “A2 unquantifiable” is less specific than the output inconsistency: `verdicts.json` calls A2 `YELLOW-unquantifiable`, while `outputs/summary.md` states “A2 is RED-unquantifiable for every route.” This must be reconciled.
- **`outputs/summary.md` vs `selectivity_grid.json`:** `selectivity_grid.json` contains two important caveats:
  1. the healthy-cell selectivity curve is optimistic / not a true transporter steady state;
  2. KPV’s pharmacodynamic timing mismatch: upstream inhibitor delivered after GSDMD pore formation.
  
  The auto-generated `summary.md` only surfaces the PepT1-expression limitation as the “single biggest limitation” and omits the PD timing caveat. The interpretive page includes it, but the output summary contract does not.
- **Interpretive wiki page:** Strong and mostly faithful. It correctly reframes the result as: pore physics works, KPV-specific selectivity fails, platform thesis remains open. It also includes the PD timing caveat, the optimistic selectivity caveat, and the redesigned §1.32 experiment.
- **`wiki/computational-experiments.md`:** Largely consistent with the interpretive page. It does use the strong phrase “KPV as a selective Trojan-horse payload: effectively falsified,” which is supported qualitatively only because it combines PepT1 confounding plus PD timing mismatch; the artifact summary should make that two-part basis explicit.
- **`wiki/validation-experiments.md` §1.32:** Already updated consistently: it replaces naive fluorescent-KPV uptake with a transporter-orphan tracer ± PepT1 blockade design. This is the best propagated surface.
- **`wiki/gsdmd-pore-delivery-paradox.md`:** Already updated consistently: Open Question #4 is marked answered for small solutes; KPV is identified as the wrong proof-of-concept payload; Ac-FLTD-CMK/downstream-acting transporter-orphan payloads are prioritized.
- **`wiki/kpv-peptide.md`:** Already updated consistently: KPV’s pore route is “evaluated, not selective”; KPV’s real delivery edge remains PepT1.
- **`wiki/delivery-route-matrix.md`:** Mentions KPV routes and links the paradox page, but I did not see a direct comp-042-specific update in the inspected portion. Since `computational-experiments.md` says comp-042 informs this page, it should either be marked already consistent by absence of a conflicting claim or get a short note that KPV is PepT1-routed and not a pore-selectivity proof payload.
- **Open questions / hypothesis cards / priority tables:** Tool budget prevented full inspection. `open-questions.md` was partially inspected; I did not verify whether any GSDMD pore-lifetime or KPV-selectivity open question remains stale elsewhere.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| GSDMD inner diameter central 20 nm, range 10–21.5 nm | `inputs/pore_geometry.json`; `inputs/provenance.md` | Used to compute pore radius and permeability | Named Sborgi 2016 / Xia 2021; artifact claims primary full-text verification, not independently re-verified by me | Plausible and low-risk for A1; primary-source verification unresolved in this review |
| Channel length 7 nm, range 4–10 nm | `inputs/pore_geometry.json` | Used in permeability | Estimated from bilayer/β-barrel; low sensitivity | Acceptable estimate; not dominant |
| KPV diffusion coefficient 5e-10 m²/s | `inputs/kpv_properties.json` | Used in permeability and MC | Stokes–Einstein estimate, not directly measured | Plausible; low-to-moderate sensitivity for τ but not qualitative result |
| Hindrance factor H = 1 | `analyze.py` hard-coded; justified by `kpv_properties.json` and `pore_geometry.json` | Directly used in permeability | Charge/radius provenance is estimated/computed; not dynamically used | Acceptable for flux; stored radius/charge should be labeled justification-only |
| Pores per cell central 200, range 10–10000 | `inputs/pore_geometry.json` | Used in central and MC; sweep includes 1–10000 | Named assumption; artifact says no primary per-cell count | Correctly flagged; A1 robust above ~10, but not measured |
| Open pore lifetime 60–1800 s, central 300 s | `inputs/pore_geometry.json` | Used in equilibration fraction and MC | Corpus/open-question plus ESCRT literature, not independently verified | A1 robust; still timing of dosing vs pore opening not modeled |
| Macrophage volume 3000 µm³ | `inputs/macrophage_geometry.json` | Used in τ denominator | Standard cell-biology estimate | Plausible; sensitivity included |
| IA synovial KPV 292 µM central | `inputs/route_concentrations.json` | Used as `C_ext` | Computed in prose from dose/volume; not computed by code | Arithmetic plausible; executable derivation absent |
| SC synovial KPV 30 nM central | `inputs/route_concentrations.json` | Used as `C_ext`; MC samples range | Design-space PK assumption | Load-bearing for SC marginal A1; unresolved |
| Oral synovial KPV 1 nM central | `inputs/route_concentrations.json` | Used as `C_ext`; MC samples range | Design-space PK assumption | Load-bearing for oral RED; unresolved but direction plausible |
| KPV “IC50” 10 nM | `inputs/pept1_and_ic50.json` | Converted to 0.01 µM; denominator for A1 | Dalmasso 2008 reporter-cell effective concentration; artifact claims PMC verification | Not a true intracellular IC50; acceptable only as proxy, especially weak for SC |
| PepT1 Km central 700 µM | `inputs/pept1_and_ic50.json` | Used in healthy-cell model | Dalmasso Jurkat anchor claimed; primary not independently checked | Plausible proxy; synovial macrophage transfer unresolved |
| Km lower/upper 160–1000 µM | `inputs/pept1_and_ic50.json` | Not used in MC or A2 sensitivity | Stored only | Action: either use or state unused |
| PepT1 expression scenarios AR 0/0.3/1/3 | `inputs/pept1_and_ic50.json` | Used in selectivity grid and verdict | Scenario assumptions, not measured | Properly identified as dominant A2 uncertainty |
| Synovial-macrophage PepT1 uncharacterized | `inputs/provenance.md`; interpretive page | Drives A2 uncertainty | Artifact reports PubMed searches; not independently verified | Central unresolved empirical gap |
| Healthy-cell PepT1 saturation model | `analyze.py`; README | Produces selectivity ratios | Heuristic, not source-derived steady-state model | Useful scenario tool; too weak for precise selectivity verdict |
| PD timing mismatch | `selectivity_grid.json`; interpretive page | Not part of verdict code; affects biological interpretation | Mechanistic pathway reasoning | Load-bearing conceptual limitation; under-propagated to README/output summary |
| “No route passes both filters” | `verdicts.json`; `summary.md`; README | Computed by requiring A1 GREEN + A2 GREEN | Depends on decision rule, not raw thresholds alone | Directionally OK, but wording should distinguish “no confident pass” from absent/low PepT1 scenarios that numerically clear |
| Output JSON validity | `central_results.json`, `selectivity_grid.json` | Committed reproducibility outputs | Contains `Infinity` | Action required: not standards-compliant JSON |

## Affected wiki pages

- `wiki/kpv-gsdmd-pore-influx-computational.md` — already consistent / minor change required — strong interpretive page; may add a note that `outputs/summary.md` currently under-reports the PD timing caveat until regenerated.
- `wiki/computational-experiments.md` — already consistent / minor wording check — overall entry matches interpretive result; ensure “effectively falsified” is explicitly grounded in both PepT1 confounding and downstream timing.
- `wiki/validation-experiments.md` §1.32 — already consistent — redesigned transporter-orphan tracer ± PepT1 blockade experiment matches comp-042’s real implication.
- `wiki/gsdmd-pore-delivery-paradox.md` — already consistent — Open Question #4 is resolved for small solutes; KPV-specific selectivity is reframed; platform thesis remains open.
- `wiki/kpv-peptide.md` — already consistent — KPV pore self-delivery is marked evaluated but not selective; PepT1 remains the real delivery route.
- `wiki/delivery-route-matrix.md` — possible change required — inspected portions do not conflict, but since comp-042 is listed as informing this page, consider adding one sentence in the peptide/GSDMD-pore route context: KPV is PepT1-routed and not a clean pore-selectivity probe.
- `wiki/open-questions.md` — unresolved / possible change required — only partially inspected. Verify no stale GSDMD pore-lifetime or “KPV selective pore delivery” open question remains.
- `wiki/hypotheses/*` — unresolved — not inspected due tool-result exhaustion; verify no hypothesis card still treats KPV as an ideal selective Trojan-horse payload.

## New connections or implications

- The artifact sharpens a general design rule for pore self-delivery: **small-solute pore influx is easy; selectivity comes from absence of independent import routes and correct timing relative to target biology.**
- KPV’s properties are anti-selective for this platform demonstration: PepT1 import plus possible intracellular persistence make healthy-cell exposure plausible, while GSDMD pore formation occurs after KPV’s upstream targets have fired.
- The redesigned §1.32 experiment is more valuable than a KPV efficacy assay: a transporter-orphan tracer tests the platform physics; fluorescent-KPV ± PepT1 blockade tests the confounder.
- Ac-FLTD-CMK or similar downstream-acting, membrane-impermeant caspase/GSDMD inhibitors are better mechanistic probes than KPV because their target timing aligns with pore formation.

## Required actions

1. **Fix committed JSON validity** in `outputs/central_results.json` and `outputs/selectivity_grid.json`: replace `Infinity` with a standards-compliant representation (`null`, string `"Infinity"`, or a separate boolean such as `healthy_conc_zero: true`). Verification criterion: strict JSON parser accepts all output files.
2. **Reconcile A2 verdict labeling** across `verdicts.json`, `outputs/summary.md`, README, and interpretive page. Choose one taxonomy (`YELLOW-unquantifiable` vs `RED-unquantifiable`) and explain the decision rule. Verification criterion: same A2 label and rationale appear in code-generated outputs and human pages.
3. **Regenerate or edit `outputs/summary.md` / README to include the PD timing caveat** already present in `selectivity_grid.json` and the interpretive page. Verification criterion: output summary states KPV is upstream-acting while pores open downstream, so transport sufficiency does not imply therapeutic timing sufficiency.
4. **Clarify “no route passes both filters” wording** to avoid implying that no scenario numerically clears both thresholds. Verification criterion: wording says no route passes with confidence / across plausible PepT1 expression, while acknowledging absent/low PepT1 scenarios are the only numerical pass cases.
5. **Either implement or explicitly mark unused sensitivity inputs**: `Km_used_uM.lower/upper`, `hydrodynamic_radius_nm`, `net_charge_pH7p4`, and route derivation fields. Verification criterion: README/provenance says which are executable inputs vs. justification-only, or code sweeps them where relevant.
6. **Add A2 sensitivity to Km or justify omission**. Verification criterion: either selectivity grid includes Km lower/central/upper for IA at minimum, or documentation explains why Km uncertainty does not change the A2 decision.
7. **Verify affected unresolved pages** (`open-questions.md`, hypothesis cards, and any priority tables) for stale KPV-as-selective-pore-payload or pore-lifetime-open claims. Verification criterion: no remaining page treats KPV as the ideal pore-selectivity proof payload without the PepT1/timing caveats.

## Review limits

I did not execute `analyze.py`; reproducibility was assessed by code inspection and arithmetic spot checks. I did not independently fetch PubMed/PMC primary sources; provenance claims marked “verified” remain artifact-author verification, not reviewer verification. Repository `grep_repo` failed because `rg` was unavailable, and later tool-result budget was exhausted, so corpus search was incomplete. I inspected the explicit comp pages plus selected related pages (`delivery-route-matrix.md`, `nlrp3-exploit-map.md`, partial `open-questions.md`, partial `gout-kill-chain-delivery-routes.md`), but not all hypothesis cards or every potentially affected priority table.
