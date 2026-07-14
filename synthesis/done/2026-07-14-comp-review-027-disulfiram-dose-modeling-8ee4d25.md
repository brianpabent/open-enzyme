---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-027
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-027

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-027-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-027-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-027

## Bottom-line verdict

**Quantitative verdict invalid; action required.** The script is deterministic and the committed outputs appear internally consistent with the current code, but the central quantitative claim depends on an unresolved and internally conflicting parent-DSF Cmax anchor, a hard-coded DER/ALDH calibration that makes 100 mg/day exactly the decision boundary, and summary propagation that broadens a single strict-GREEN modeled dose (`100 mg/day`) into a “75–125 mg/day” window not actually tested or derived. The computation is useful as a hypothesis generator, not as a clean dose recommendation.

## Implementation and constraint closure

**Question/model fit.** The implementation answers a narrower question than the stated question: “Given a selected plasma parent-DSF Cmax anchor and a selected Me-DTC scaling rule, which listed oral doses satisfy two Hill-equation thresholds?” It does **not** establish a therapeutically meaningful gout dose window. “Therapeutically meaningful” is substituted by an arbitrary `GSDMD ≥50%` threshold at **parent DSF Cmax**, not by measured synovial/macrophage target engagement, IL-1β suppression, flare outcomes, or time-integrated covalent occupancy.

**Major implementation issues traced:**

- `analyze.py` loads `pk_data.json`, `ec50_data.json`, and `der_threshold_data.json`, but the model’s most load-bearing DSF Cmax anchor is **not taken from JSON**. It is hard-coded:
  - `CMAX_DSF_PARENT_AT_250MG_UM = 1.0`
  - low/high `0.4–2.5`
- `pk_data.json` contains a conflicting older single-dose table:
  - 250 mg predicted Cmax = `0.40 µM`
  - 500 mg predicted Cmax = `0.80 µM`
  - while code/output use 250 mg = `1.00 µM`, 500 mg = `2.00 µM`.
  This is not a harmless stored input; it directly changes whether 100 mg/day clears the 50% GSDMD threshold.
- The code comments contain a unit-conversion red flag: it says parent DSF Cmax after 250 mg is “0.4–1.5 µg/mL (1.3–5.0 µM), with mean ~1 µM.” With MW 296.55 g/mol, **1 µM ≈ 0.297 µg/mL**; a mean near 1 µg/mL would be ~3.4 µM, not 1 µM. Either the µg/mL claim, the µM anchor, or the “mean” statement is wrong.
- Lee 2018 PK parameters (`F`, `CL`, `Vd`, `ka`, half-life) are loaded and cited in outputs, but the Cmax calculation deliberately ignores them. The output summary still says “DSF PK: Lee 2018 (CL=0.53 L/hr, Vd=1.3 L, F=0.875),” which overstates what the implementation uses.
- `ALDH_EC50_MEDTC_NM = 104.3` is hard-coded, not read from `der_threshold_data.json`. The calibration forces ~70 nM Me-DTC at 100 mg/day to produce ~40% ALDH inhibition. Thus the headline GREEN dose sits exactly on the DER ceiling by construction.
- The code labels 100 mg/day as `DER_hypotension_risk: below_threshold` because the unrounded value is just under 0.40. This is a zero-margin classification, not a safety buffer.
- 125 mg/day is marked `DER_hypotension_risk: above_threshold` but still receives `YELLOW` because `YELLOW` allows ALDH ≤50%. This is internally coherent by code rules but conflicts with wording that treats DER threshold crossing as the main ceiling.
- The dose list does **not include 75 mg/day**, yet README/wiki/index repeatedly claim a “75–125 mg/day” window.
- No continuous interpolation or uncertainty propagation is implemented. Bounds are printed for DSF Cmax, but verdicts use only central values.
- Me-DTC variability, metabolite accumulation, CYP genotype, food effect, protein binding, tissue distribution, ethanol exposure, and ALDH interindividual variability are not swept.
- `di_landscape.json` and `formulation_data.json` are not used by the executable model. They can be documentation inputs, but recommendations about ER lipid matrix, drug interactions, compounding workflow, and allopurinol co-administration are not code-derived outputs.
- `formulation_data.json` claims ER can reduce Cmax by ~50% while maintaining AUC, but the script does not model ER release, Cmax compression, or sustained covalent engagement.
- `predicted_cavg_dsf_uM = Cmax/3.5` is a heuristic with no input provenance and is reported but not used for verdict.
- `plasma_total_dithiocarbamate_Cmax_uM = 4× parent` is reported and used for a “total DTC GSDMD blockade” column, but verdicts use parent DSF. The 4× multiplier is an estimate and does not establish equal GSDMD potency for all circulating metabolites.

**Constraint closure.**

- **Reaction substrates/products/cofactors:** The model includes DSF → GSDMD blockade and Me-DTC → ALDH inhibition, but it does not mechanistically model DSF metabolism, thiol exchange, copper effects, protein binding, intracellular access, or metabolite-specific GSDMD potency. Ethanol/acetaldehyde biology is represented only via an ALDH inhibition threshold.
- **Concentration vs operating constants:** GSDMD EC50s and NLRP3 EC50s are represented as Hill n=1 constants. ALDH inhibition is back-calibrated rather than independently fitted. Plasma Cmax is used as the concentration at the biological target, with no tissue/free-fraction correction.
- **Mass balance / exposure time:** Oral dose → Cmax scaling is linear below 1000 mg. No finite absorption/release profile, steady-state daily accumulation, covalent time-integration, or intracellular residence model is implemented beyond a heuristic Cavg.
- **Localization / access:** The modeled concentration is plasma parent DSF, but the relevant therapeutic compartment is likely synovial/tissue-resident inflammatory cells. Access is asserted but not modeled.
- **Coproducts/off-targets/safety:** DER is modeled; other chronic-disulfiram issues are documented elsewhere but not incorporated. The disulfiram page separately flags a ChEMBL LOXL4 IC50 of 59 nM; at modeled 100 mg/day parent DSF Cmax of 0.4 µM, this off-target would be above IC50 if free/tissue-relevant, though relevance is unknown and primary verification was not performed here.
- **Sensitivity ranges:** The dominant uncertainties are the DSF Cmax anchor, free/tissue concentration, GSDMD EC50 choice, Me-DTC/ALDH variability, and DER clinical threshold. The script reports Cmax bounds but does not classify probabilistically or propagate them into final verdicts.

## Summary-fidelity audit

**Artifact summaries are not faithful enough to the code and inputs.**

- `outputs/summary.md` says:
  - Headline: **GREEN**
  - Recommended 503A dose range: **100–100 mg/day**
- README, interpretive wiki page, `computational-experiments.md`, `compounding-pharmacy-track.md`, `disulfiram.md`, `gout-action-guide.md`, and `chassis-pending-interventions.md` broaden this to **“75–125 mg/day”** or **“range 75–125 mg/day, centered on 100.”**
  - 75 mg/day is not evaluated.
  - 125 mg/day is above the modeled DER threshold (`ALDH 45%`, `DER_hypotension_risk: above_threshold`).
  - Strict-GREEN exists only at the single tested dose of 100 mg/day under central assumptions.
- The interpretive page says comp-027 “closes” or “answers” the dose question and “unblocks” the 503A pathway. The artifact only provides a fragile computational prior with unresolved PK/source conflicts.
- The README says the experiment “gates whether the compounding-pharmacy track’s 503A disulfiram pathway has a defensible dosing protocol.” Given the PK anchor conflict and zero-margin DER classification, the dosing protocol is not yet defensible as a handoff.
- `outputs/summary.md` and README cite Lee 2018 PK parameters as key assumptions even though the code does not use Lee’s compartmental parameters for Cmax. This is stale or misleading provenance language.
- The `pk_data.json` table remains stale relative to the code’s hard-coded Cmax anchor; this should be reconciled before any summary claim is trusted.
- The disulfiram page uses strong wording such as “most accessible,” “safest,” “excellent safety,” “no hepatotoxicity,” and gives a gout prophylaxis dose line. Those claims exceed the comp-027 artifact’s evidentiary tier and should be softened to Phase 0 / mechanistic-extrapolation language.
- `gout-action-guide.md` is patient-facing. Its compounding-pharmacy section propagates the 75–125 mg/day framing and should be corrected or caveated because this review finds the quantitative dose verdict unresolved.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Parent DSF Cmax = 1.0 µM at 250 mg PO | `analyze.py` hard-coded constants; README methodology; `outputs/dose_response.json` metadata | Directly determines all DSF Cmax values and GSDMD blockade verdict | Named as “canonical clinical PK literature” and “consistent with Lee 2018,” but no specific primary table verified here; `papers/` paths unavailable | **Unresolved / action required**; conflicts with `pk_data.json` and contains unit-conversion red flag |
| Parent DSF Cmax bounds 0.4–2.5 µM at 250 mg | `analyze.py` constants | Printed as low/high bounds; not used in verdict | Citation string only; not verified | **Unresolved**; verdict ignores bounds |
| `pk_data.json` single-dose Cmax values: 250 mg = 0.40 µM, 500 mg = 0.80 µM | `inputs/pk_data.json` | Not used by code | Internal input contradicts executable model | **Change required**; stale/conflicting input |
| Lee 2018 F=0.875, CL=0.53 L/hr, Vd=1.3 L, ka=0.08 hr⁻¹ | `inputs/pk_data.json`; `outputs/summary.md` | Loaded, but not used for Cmax verdict; KEL computed then unused | Citation string; primary not inspected | **Misleading in summary**; not the implemented PK basis |
| Me-DTC peak = 278 nM at 400 mg DSF | `pk_data.json`; `analyze.py` `MEDTC_PEAK_AT_400MG_NM` | Direct linear scaling for Me-DTC at all doses | Named Johansson 1989 PMID 2551696; primary not inspected | **Plausible but unverified here**; needs source check |
| Linear Me-DTC scaling to 25–500 mg | `analyze.py` comments; `pk_data.json` dose_scaling | Directly determines ALDH inhibition | Extrapolated from 100–300/400 mg data per artifact | **Assumption-heavy**; no uncertainty propagated |
| ALDH EC50 = 104.3 nM Me-DTC | `analyze.py` hard-coded | Directly determines DER ceiling | Back-calibrated from Faiman/Johansson assumptions, not independent source | **Action required**; makes 100 mg exactly the boundary |
| DER hypotension threshold = 40% ALDH inhibition / 110 µM acetaldehyde | `der_threshold_data.json`; `analyze.py` threshold | GREEN cutoff uses ≤40% | Named Faiman 1989 rat model; primary not inspected | **Unverified and translationally uncertain** |
| 100 mg DSF + ethanol challenge observed DER | `der_threshold_data.json` clinical_DER_dose_response | Not directly used except via ALDH calibration narrative | Named Johansson 1989 | **Tension with GREEN label**; if DER observed at 100 mg, “below threshold” is too strong |
| GSDMD EC50 conservative = 0.30 µM | `ec50_data.json`; `analyze.py` | Directly determines GSDMD blockade and GREEN/YELLOW | Named Hu 2020 PMC7316630; primary unavailable here | **Plausible but unverified**; translation to plasma/tissue unresolved |
| GSDMD cellular preincub EC50 = 0.02 µM | `ec50_data.json`; `analyze.py` | Reported optimistic output; not verdict | Named Hu 2020 | **Not verdict-bearing but overused in summary language** |
| NLRP3 palmitoylation EC50 partial/complete = 10/30 µM | `ec50_data.json`; `analyze.py` | Output comparison only | Named Xu 2024 | **Plausible but unverified**; different assay/cell context |
| Total DTC multiplier = 4× parent | `analyze.py` constant | Output column only; not verdict | Estimated from Lee summed-AUC scaling | **Speculative**; do not use as independent efficacy support |
| Cavg = Cmax / 3.5 | `analyze.py` | Output column only | Heuristic; no direct source | **Weak support**; not a real exposure-time model |
| GREEN threshold = GSDMD ≥50% and ALDH ≤40% | `analyze.py` | Final per-dose classification | Chosen decision rule, not biological validation | **Arbitrary but explicit**; must be labeled as model convention |
| YELLOW threshold = GSDMD ≥30% and ALDH ≤50% | `analyze.py` | Allows 125 mg despite DER risk above threshold | Chosen decision rule | **Creates summary ambiguity**; clarify DER-borderline vs acceptable |
| Recommended range = 100–100 mg/day | `outputs/summary.md` | Output of strict-GREEN doses | Derived from code | **Faithful to code** |
| Recommended range = 75–125 mg/day | README and wiki pages | Not code-derived; 75 not tested; 125 above DER threshold | Interpretive extrapolation | **Change required** |
| ER lipid matrix reduces Cmax ~50% while maintaining AUC | `formulation_data.json`; README/compounding page | Not modeled | Formulation extrapolation | **Not supported by executable output** |
| Allopurinol + DSF synergy | `di_landscape.json`; README handoff | Not modeled | Rat Asiri 2025 at 50 mg/kg DSF, ~480 mg HED per artifact | **Not supportive of sub-AUD 100 mg human synergy claim** |

## Affected wiki pages

- `wiki/disulfiram-dose-modeling-computational.md` — **change required** — broad “75–125 mg/day” and “dose question closed/unblocked” language exceeds code output and depends on unresolved PK anchor.
- `wiki/computational-experiments.md` — **change required** — comp-027 entry should not state a clean 75–125 mg/day window; strict result is single central dose 100 mg/day and quantitative verdict is currently unresolved.
- `wiki/compounding-pharmacy-track.md` — **change required** — disulfiram candidate entry and Phase 2 closure currently treat comp-027 as a defensible two-phase protocol. Needs downgrade to fragile computational prior pending PK/source reconciliation.
- `wiki/disulfiram.md` — **change required** — dosing section propagates 100 mg/day / 75–125 mg/day as a gout prophylaxis window and uses safety/economic claims stronger than this artifact supports.
- `wiki/gout-action-guide.md` — **change required** — patient-facing compounding section repeats the disulfiram dose window; should be softened or removed until the PK/DER anchor is fixed.
- `wiki/chassis-pending-interventions.md` — **change required** — M1 PDB × disulfiram stack calls comp-027 YELLOW-leaning-GREEN and repeats “75–125 mg/d”; should be reconciled with this review and with comp-031 invalidation language already present.
- `wiki/nlrp3-exploit-map.md` — **already mostly consistent / minor change required** — mechanistic GSDMD role is consistent, but “most accessible pharma-grade” / “black hat dream” style should not be read as comp-027 dose validation; cross-link caveat to unresolved dosing would help.
- `wiki/validation-experiments.md` — **minor change required if a disulfiram validation entry is added or cited elsewhere** — current validation page does not appear to contain a dedicated comp-027 wet-lab gate in inspected portion; a concrete HPLC PK + ex vivo IL-1β/GSDMD engagement validation would be the appropriate follow-up surface if this track stays active.

## New connections or implications

- The model’s **only strict-GREEN dose is a zero-margin boundary**: 100 mg/day is simultaneously the modeled GSDMD success point and the modeled DER ceiling. This makes per-person HPLC PK/Me-DTC measurement much more important than the summaries imply.
- The corpus already flags a disulfiram LOXL4 off-target at 59 nM. If the modeled parent DSF Cmax at 100 mg/day is 0.4 µM, chronic off-target review becomes more important, even if LOXL4 relevance to gout is unclear.
- The Asiri rat gout/allopurinol synergy evidence is at an AUD-equivalent human dose, not the sub-AUD modeled window. It should not be used to support the 100 mg/day compounding protocol except as broad proof that DSF can affect gout-model inflammation at much higher exposure.
- ER formulation is currently a separate unmodeled hypothesis. If ER halves Cmax while maintaining AUC, it could also reduce Cmax-based GSDMD blockade under the current verdict rule unless covalent time-integration is explicitly modeled.

## Required actions

1. **Reconcile the parent DSF Cmax anchor.** Update `pk_data.json`, `analyze.py`, README, and outputs to use one verified Cmax basis, with correct µg/mL↔µM conversion. Verification criterion: named primary-source table/figure or explicitly labeled secondary estimate; no internal conflict between JSON and code.
2. **Move hard-coded load-bearing constants into inputs or document them as model choices.** At minimum: parent Cmax anchor/bounds, total-DTC multiplier, ALDH EC50 calibration, Cavg/Cmax ratio, verdict thresholds. Verification criterion: every output headline number traces to an input field or clearly labeled decision rule.
3. **Rerun outputs after reconciliation.** Verification criterion: `dose_response.json`, CSV, and `summary.md` regenerated from the corrected script and checked for consistency.
4. **Replace “75–125 mg/day window” with the actual modeled result or derive it.** Either test/interpolate 75 mg and justify 125 mg despite above-threshold DER, or restrict summaries to “single central strict-GREEN point at 100 mg/day under current assumptions.” Verification criterion: README, interpretive page, computational index, compounding track, disulfiram page, gout action guide, and chassis-pending M1 agree.
5. **Downgrade clinical/action wording.** Owner surfaces: `disulfiram.md`, `gout-action-guide.md`, `compounding-pharmacy-track.md`. Verification criterion: clearly states Phase 0, mechanistic/in silico only, not a dosing recommendation or clinical evidence.
6. **Add a validation gate for the disulfiram track if it remains active.** Suggested gate: small measured PK/source verification plan for parent DSF and Me-DTC at 50/75/100/125 mg plus ex vivo GSDMD/IL-1β readout. Verification criterion: validation page or compounding track names the gate before patient/pathway handoff.
7. **Primary-source verification pass.** Verification criterion: Hu 2020, Johansson 1989, Faiman/Yourick 1989, Lee 2018, Xu 2024, and Asiri 2025 load-bearing values are checked against directly available text/tables, with “not verified” retained where only citation strings are present.

## Review limits

- I did not execute the code. Reproducibility was assessed by inspection only.
- The repository search tool failed because `rg` was unavailable, so affected-surface discovery relied on the supplied bundle and selected direct file reads.
- Primary-source paper directories referenced by the artifact (`papers/PMC...`) were not available via the read tool; no primary-source verification occurred in this review.
- The `validation-experiments.md` file was only partially inspected before tool-result budget was exhausted.
- Bundle references to `compounding-pharmacy-track.md`, `disulfiram.md`, `gout-action-guide.md`, and `nlrp3-exploit-map.md` were inspected directly, but other possible downstream pages may still exist and need a full grep-based propagation sweep once repository search is functional.

---

## ✓ Actioned 2026-07-14

**Disposition: downgrade to hypothesis-generator** (not a rerun — the single-point model is fine, but the corpus over-broadened it into a validated dose window).

- **Interpretive page (`disulfiram-dose-modeling-computational.md`):** added a ⚠️ downgrade banner + reframed the verdict — a **single strict-GREEN modeled point at 100 mg/day** under current (unverified Cmax + hard-coded-ALDH-calibration) assumptions, **NOT a validated "75–125 mg/day window"**; hypothesis to test, not a dose recommendation (audit #4). The banner states any "75–125" wording elsewhere inherits this caveat.
- **`computational-experiments.md`** verdict + Planned-row updated to the downgraded framing.

**Residuals (noted):** the "range 75–125 mg/d" phrasing still appears verbatim on 6 downstream pages (`disulfiram.md`, `compounding-pharmacy-track.md` ×2, `chassis-pending-interventions.md`, `gout-action-guide.md`, `supplements-stack.md`) — consistent-by-reference via the interpretive banner, but a mechanical sweep should update each (audit #4). Deeper artifact reconciliation (single verified Cmax anchor, hard-coded constants → inputs, rerun) is audit #1–3, a follow-up.
