---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-033
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-033

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-033-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-033-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-033

## Bottom-line verdict

Action required — the single-dose systemic Cmax-equivalence RED verdict is plausibly reproducible by inspection, but the artifact has propagation errors, stale partner/cost wording, a wrong protein-structure claim in downstream pages, an incorrect reproduction path, and several load-bearing assumptions remain citation-only rather than independently verified.

The computation answers a narrower question than the title suggests: “can a single 4–24 mg inhaled mRNA dose match systemic anakinra-like plasma Cmax?” It does **not** resolve therapeutic efficacy for gout flares, receptor occupancy, joint IL-1 ligand burden, repeat-dose clinical utility, or pulmonary safety.

## Implementation and constraint closure

I traced the load-bearing calculation from `inputs/model_parameters.json` and `inputs/anakinra_benchmark_pk.json` through `analyze.py` into `outputs/dose_auc_prediction.json` and `outputs/summary.md`.

**Core implemented model:**

- Samples 20,000 Monte Carlo draws with seed 33.
- Dose sampled log-uniform 4–24 mg mRNA.
- Lung delivery fraction, translation efficiency, alveolar-to-systemic bioavailability, expression duration, clearance, and Vd sampled from priors.
- Converts nominal mRNA dose → mRNA reaching alveolus → protein synthesized → protein reaching systemic circulation.
- Models systemic IL-1Ra as zero-order input over expression duration with first-order clearance in a single compartment.
- Computes Cmax and 24h AUC.
- Applies a hard Cmax-centered decision rule.

**Reproducibility by inspection:** the committed output values match the code logic and input ranges. I did not execute the code.

**Implementation concerns / closure gaps:**

- `README.md` reproduction command says:
  ```bash
  cd experiments/comp-033-inhaled-mrna-il1ra-pulse-therapy
  python3 analyze.py
  ```
  but the tracked path is `wiki/etc/experiments/comp-033-inhaled-mrna-il1ra-pulse-therapy`. This is a direct reproducibility-contract error unless an unlisted symlink exists.
- The code loads `il1ra_target_properties.json` into `target` but never uses it. Target validation is narrative/static, not computational.
- `construct_design_priors.json` and most of `inhaled_mrna_precedents.json` are not used by `analyze.py`; their contents are handoff documentation, not implemented model inputs.
- Partner landscape is not derived from partner arrays; the code reads `partners["summary_count"]["tier_A_active_inhaled_mrna_clinical_programs"]` and `total_partner_candidates`. The counts happen to match the visible arrays, but the code would not catch stale counts.
- Economics are mostly precomputed in `mrna_lnp_economics.json`; `analyze.py` reports `usd_per_dose` scenario values and hardcodes some annual-ratio denominators. It does not recompute costs from the mass-basis cost fields.
- The reverse-dose calculation labels `median_cmax_at_median_dose_ug_per_ml` but uses the **overall Monte Carlo median Cmax**, not a model rerun or conditional calculation at the median dose with other inputs held at medians. The linear scaling is probably close enough for an order-of-magnitude gap, but the field label is stronger than the implemented derivation.
- The model computes AUC but the decision rule is governed by Cmax only. That is acceptable for the stated “systemic anakinra-equivalent Cmax” gate, but it does not fully answer “therapeutic exposure.”
- The `decision_rule` in `model_parameters.json` says YELLOW can be based on partner count between 1–2; the code does not implement that branch as written, though it does not affect this run because Tier A count is 4.

**Constraint closure:**

- **Reaction / mechanism:** IL-1Ra is not enzymatic in this use case; it competitively antagonizes IL-1R1. The model does not include IL-1α/IL-1β concentrations, receptor occupancy, IL-1Ra Kd, synovial/joint compartment exposure, or flare-phase timing. Those were later partly addressed by comp-036, not comp-033.
- **Substrates/cosubstrates/cofactors:** for mRNA expression, the true biological constraints are LNP uptake, endosomal escape, translation capacity, secretion, folding/disulfide formation, amino-acid supply, pulmonary epithelial viability, and systemic transport. Most are collapsed into the translation-efficiency and bioavailability priors.
- **Physiological concentration vs operating constants:** comp-033 compares plasma Cmax to anakinra Cmax/trough, not to IL-1Ra–IL-1R1 Kd or receptor occupancy. This is a hidden substitution: systemic anakinra Cmax stands in for physiologic PD sufficiency.
- **Mass balance:** total produced protein is finite and calculated explicitly. However, the dominant translation-efficiency prior is an order-of-magnitude inference and not directly verified in the artifact.
- **Residence/exposure time:** expression duration 24–96 h and systemic clearance 0.10–0.25/h are modeled. Repeat dosing is not modeled in comp-033.
- **Localization/access:** pulmonary expression → systemic exposure is modeled as a scalar alveolar-to-systemic bioavailability. The model does not separately represent alveolar interstitium, lymphatic transit, macrophage uptake, epithelial secretion polarity, local lung retention, or joint access.
- **Safety/off-targets:** pulmonary LNP inflammation, local lung IL-1 blockade, infection risk, anti-PEG or repeat-exposure effects, innate immune activation, and high-dose nebulizer/device tolerability are acknowledged narratively but not included quantitatively.
- **Sensitivity coverage:** the sensitivity analysis covers the implemented PK and delivery parameters. It does not cover Kd/receptor occupancy, IL-1 ligand burden, LNP tolerability, repeat-dose accumulation, high-dose nonlinearity, or partner feasibility.

## Summary-fidelity audit

**README / output summary / dose JSON:** internally consistent on the main RED Cmax-equivalence verdict:

- median Cmax ≈ 0.025 µg/mL;
- p05 ≈ 0.0023 µg/mL;
- p95 ≈ 0.278 µg/mL;
- median AUC24 ≈ 0.455 µg·h/mL;
- reverse dose ≈ 195 mg for 0.5 µg/mL and ≈ 585 mg for 1.5 µg/mL.

**Interpretive page:** mostly consistent with the artifact but stale in one important way: it says repeat dosing was “not modeled quantitatively here” and warrants a follow-up comp-NNN. The corpus already has comp-036, and other pages incorporate that update. The interpretive page should now explicitly point to comp-036 rather than leaving the forward path as merely proposed.

**`wiki/computational-experiments.md`:** main quantitative comp-033 numbers are consistent, but the partner summary is stale/wrong: it lists “Translate Bio (now Sanofi), Moderna, Arcturus, Ethris” while the artifact’s Tier A partner set is Arcturus, ReCode, Ethris, and Sanofi/Translate Bio legacy. Moderna is explicitly **not** a clinical inhaled-mRNA program in the artifact.

**Validation page:** the inspected top of `validation-experiments.md` is consistent at the governance level: chassis-pending interventions have their own validation paths and are not duplicated in the main koji-oriented queue. I did not inspect the full 252 kB file beyond the first large chunk.

**Downstream wiki errors surfaced:**

- `chassis-pending-interventions.md` and `nlrp3-inflammasome.md` state or imply IL-1Ra has “no disulfide bonds.” The artifact’s `il1ra_target_properties.json`, `README.md`, and `provenance.md` say IL-1Ra has one intramolecular disulfide C91–C141. This is a concrete propagation error.
- `gout-action-guide.md` and `gout-clinical-pipeline.md` quote canakinumab as about `$3,000/dose`, while comp-033 uses `$21,000/dose` and `$105K–300K/year`. Those pages should be reconciled or clearly explain different pricing assumptions.
- `modality-chokepoint-matrix.md` still frames “mRNA-IL-1RA pulse therapy IV” in one row and does not reflect the comp-033/036 inhaled pulmonary modeling result.
- `delivery-route-matrix.md` says inhaled mRNA gout relevance is unclear without a tissue-tropic lung target, but comp-033/036 have now made that route a specific modeled chassis-pending candidate with RED single-dose and YELLOW repeat-dose status.
- `etc/open-enzyme-vision.md` includes stale cost language such as `$25–200/year/patient`, while the comp-033 artifact’s own economics span about `$10–1,200/year` depending on flares and scenario, before comp-036 repeat-dose changes.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Dose range 4–24 mg mRNA per administration | `inputs/model_parameters.json`; README | Directly sampled log-uniform | Citation strings to Translate Bio MRT5005 and Arcturus ARCT-032; primary sources not included | Used correctly; source not independently verified here |
| Translation efficiency 1,000–50,000 ng protein/µg mRNA | `inputs/model_parameters.json`; `inputs/provenance.md` | Directly sampled log-uniform; top sensitivity driver | Explicitly order-of-magnitude inference; primary-paper verification queued | Load-bearing and unresolved; action to verify/tighten |
| Lung delivery efficiency 0.10–0.40 | `inputs/model_parameters.json` | Directly sampled uniform | Citation strings to Geller/PARI; not directly available | Plausible prior; not independently verified |
| Alveolar-to-systemic bioavailability 0.10–0.50 | `inputs/model_parameters.json` | Directly sampled uniform | Patton & Byron / Afrezza cited; IL-1Ra-specific data absent | Major unresolved biological assumption |
| Expression duration 24–96 h | `inputs/model_parameters.json` | Directly sampled uniform | Narrative pulmonary mRNA precedent; no primary artifact included | Plausible but unverified; repeat-dose relevance high |
| IL-1Ra clearance 0.10–0.25/h | `inputs/model_parameters.json` | Directly sampled uniform | Kineret/Yang cited; no primary source file | Implemented correctly; source not independently verified |
| Vd 12–25 L | `inputs/model_parameters.json` | Directly sampled uniform | Anakinra PK cited; no primary source file | Implemented correctly; source not independently verified |
| Anakinra Cmax 1.5 µg/mL | `inputs/anakinra_benchmark_pk.json` | Benchmark and Cmax ratio denominator | FDA label/Yang/Granowitz cited; no primary source file | Load-bearing; not independently verified |
| Anakinra AUC24 12 µg·h/mL | `inputs/anakinra_benchmark_pk.json` | AUC ratio denominator | Estimate formula provided, not direct source value | Adequate as rough benchmark; not primary-verified |
| Minimum Cmax gate 0.5 µg/mL | `inputs/anakinra_benchmark_pk.json`; code | GREEN/RED decision gate | Rationale narrative only; not receptor-occupancy-derived in comp-033 | Hidden PD substitution; comp-036 partly supersedes |
| p05 Cmax gate 0.1 µg/mL | `analyze.py`; `outputs/dose_auc_prediction.json` | Decision gate | Decision-rule choice, not sourced physiological constant | Explicit but arbitrary; label as model gate |
| Tier A partners = 4 | `inputs/partner_landscape.json`; code | Partner gate and summary | Static landscape scan; not code-derived from array | Count matches visible arrays, but provenance not independently verified |
| Total partner candidates = 15 | `inputs/partner_landscape.json`; `outputs/summary.md` | Summary only | Static count | Internally consistent; not computed |
| Canakinumab $21,000/dose, $105K–300K/year | `inputs/anakinra_benchmark_pk.json`; `outputs/economic_comparison.json` | Economic comparison | Pricing sources cited; no primary file | Needs corpus reconciliation; source not independently verified |
| Cost per inhaled mRNA dose $2/$18/$120 | `inputs/mrna_lnp_economics.json`; `outputs/economic_comparison.json` | Economic comparison | Order-of-magnitude economics; not source-verified | Not independent of dose feasibility if repeat dosing changes dose count |
| IL-1Ra has one disulfide C91–C141 | `inputs/il1ra_target_properties.json`; `inputs/provenance.md` | Target characterization, not code | UniProt verification claimed; primary dump not included | Artifact internally clear; downstream pages contradict it |
| Reverse-dose 195/585 mg | `analyze.py`; `outputs/dose_auc_prediction.json` | Load-bearing RED framing | Derived by linear scaling from median Cmax and geometric median dose | Directionally valid; field label overstates conditional derivation |
| Reproduction command | `README.md` | Reproducibility path | N/A | Incorrect path relative to tracked repo layout |

## Affected wiki pages

- `wiki/computational-experiments.md` — change required — comp-033 partner summary includes Moderna and omits ReCode; artifact Tier A list is Arcturus, ReCode, Ethris, Sanofi/Translate Bio legacy.
- `wiki/inhaled-mrna-il1ra-pulse-computational.md` — change required — repeat-dose path is described as not yet modeled; comp-036 now exists and should be linked as the quantitative follow-up.
- `wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md` — already consistent — explicitly reframes comp-033 Cmax-equivalence to receptor occupancy and states YELLOW repeat-dose result.
- `wiki/chassis-pending-interventions.md` — change required — states IL-1Ra has no disulfide bonds; comp-033 artifact says one disulfide C91–C141. Also should keep comp-033/036 split explicit: RED single-dose Cmax, YELLOW repeat-dose occupancy.
- `wiki/nlrp3-inflammasome.md` — change required — repeats the “no disulfides” IL-1Ra claim; should be corrected to “one intramolecular disulfide; no glycosylation required.”
- `wiki/gout-action-guide.md` — change required — canakinumab cost per dose conflicts with comp-033 benchmark; inhaled mRNA projected per-flare economics should distinguish comp-033 single-dose cost from comp-036 repeat-dose cost.
- `wiki/gout-clinical-pipeline.md` — change required — canakinumab cost per flare conflicts with comp-033 benchmark; acute-flare comparator table should reconcile pricing assumptions.
- `wiki/modality-chokepoint-matrix.md` — change required — mRNA-IL-1RA row still says IV in one place and lacks comp-033/036 RED/YELLOW status for the inhaled pulmonary route.
- `wiki/delivery-route-matrix.md` — change required — inhaled mRNA gout-relevance language is stale now that comp-033/036 specifically modeled it.
- `wiki/etc/open-enzyme-vision.md` — change required — comp-033/036 narrative mostly propagated, but cost language should be reconciled to artifact economics and repeat-dose implications.
- `wiki/validation-experiments.md` — already consistent in inspected portion — top-level scope note says chassis-pending validation paths live on their own pages; no comp-033-specific wet-lab gate was found in the inspected chunk.

## New connections or implications

1. **Cmax-equivalence and receptor-occupancy framing must be treated as different evidence layers.** comp-033’s RED verdict is valid for single-dose plasma Cmax matching, but comp-036 shows why that should not be paraphrased as “therapeutically impossible.”
2. **Economics become regimen-dependent after comp-036.** comp-033’s `$2/$18/$120 per flare` assumes one administration. If BID multi-day regimens are the surviving path, public-facing annual and per-flare cost estimates should be recomputed for dose count.
3. **IL-1Ra structural simplicity is still favorable, but not “no disulfides.”** The correct partner-facing claim is “small, endogenous, non-glycosylated, one intramolecular disulfide,” not “no disulfides.”
4. **Partner landscape should separate active clinical inhaled mRNA programs from general mRNA capacity.** ReCode belongs in Tier A per artifact; Moderna does not, unless separately justified as a manufacturing/LNP-capacity partner rather than an active inhaled-mRNA clinical-program partner.
5. **The dominant experimental next measurement is not more Monte Carlo.** The model already identifies translation-efficiency mass ratio and alveolar-to-systemic bioavailability as decisive; these need direct pulmonary expression / BAL / plasma quantification in a relevant model before the dose gap can be tightened.

## Required actions

1. Correct `README.md` reproduction command to the actual tracked path, and verify that `python3 analyze.py` from that directory regenerates the committed outputs byte-for-byte or within deterministic formatting expectations.
2. Correct downstream IL-1Ra structure claims in `chassis-pending-interventions.md` and `nlrp3-inflammasome.md`: one intramolecular disulfide C91–C141, non-glycosylated.
3. Reconcile partner lists in `computational-experiments.md`: replace the stale “Moderna” Tier A wording with ReCode, or explicitly move Moderna to a non-Tier-A manufacturing/platform-adjacent category.
4. Update `inhaled-mrna-il1ra-pulse-computational.md` to point to comp-036 as completed repeat-dose follow-up rather than a proposed future comp.
5. Reconcile canakinumab pricing across `gout-action-guide.md`, `gout-clinical-pipeline.md`, and comp-033 economics; document whether `$3,000/dose` or `$21,000/dose` is being used and why.
6. Recompute or clearly label inhaled mRNA cost estimates under repeat-dose regimens; do not reuse single-dose `$2/$18/$120 per flare` as if it applies to BID multi-day dosing.
7. Tighten output labels for reverse-dose calculation: either compute Cmax conditional at the median dose or rename the field to say it scales from the overall Monte Carlo median Cmax.
8. Add explicit provenance status in public summaries for the translation-efficiency prior and alveolar-to-systemic bioavailability prior: these are order-of-magnitude inferences, not primary-source-verified IL-1Ra pulmonary data.
9. Update `modality-chokepoint-matrix.md` and `delivery-route-matrix.md` to reflect comp-033/036 status: inhaled pulmonary mRNA-IL-1Ra is modeled, single-dose RED, repeat-dose YELLOW, not merely an abstract unexplored route.

## Review limits

- I did not execute `analyze.py`; reproducibility was assessed by static inspection of code, inputs, and committed outputs.
- The repository fixed-string search tool failed because `rg` was unavailable, so affected-page discovery relied on the provided bundle plus targeted file reads.
- Primary sources cited in `inputs/provenance.md` were not directly available in the artifact; I did not independently verify FDA labels, UniProt, Yang 2003, Patton & Byron 2007, Rowe 2023, Arcturus disclosures, pricing databases, or manufacturing-cost sources.
- I inspected the beginning and relevant exposed portions of large wiki pages, but not every byte of `validation-experiments.md` or every possible hypothesis/priority table.
- This review stays at Phase 0 computational-evidence level and does not convert model outputs into clinical efficacy claims or medical advice.
