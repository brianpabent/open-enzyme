---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-029
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-029

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-029-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-029-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-029

## Bottom-line verdict
Action required — the YELLOW decision-rule table is internally plausible for the toy fractional-reduction model, but the artifact does not close the biological system it claims to model, and several summary/wet-lab handoff statements are unsupported or contradicted by the code. Most importantly, the “α ≥ 0.5 re-runs to GREEN” claim is mathematically impossible under the artifact’s own gut-luminal RA singleton median (~0.886), because the combined fraction is capped at 1.0 and thus cannot reach the 1.5× better-singleton GREEN threshold.

## Implementation and constraint closure
What I traced:

- `analyze.py` loads all five JSON input files, but most scientific inputs are **not traced from JSON into code**. The script hardcodes the load-bearing IC50 range, RA concentration ranges, DAF concentration range, accessibility priors, DAF max acceleration, DAF half-saturation, and decision thresholds.
- `model_parameters.json` is used only for `rng_seed` and `n_draws`; its decision-rule thresholds are not used dynamically.
- `rosmarinic_acid_ic50_data.json`, `rosmarinic_acid_bioavailability.json`, `daf_decay_kinetics_prior.json`, and `msu_c3b_deposition_rate.json` are effectively provenance/documentation stores, not executable inputs.
- `T_HALF_INTRINSIC_MIN = 7.5` is written to output but cancels from the implemented DAF fractional-reduction formula. It is not a load-bearing numeric input in the calculation.
- MSU deposition rate, MSU load, serum complement availability, C5a generation rate, CRP/IgM dependence, and residence/exposure time are not implemented. The model is a dimensionless fractional composition, not a finite kinetic/mass-balance model.

Key hidden substitutions / model-fit issues:

1. **Gut-luminal RA is substituted for gout-relevant systemic/synovial complement control.**  
   The model correctly shows free systemic RA is essentially inactive at plasma Cmax, then uses gut-luminal RA as the RA arm for the combined model. That may be a legitimate gut-mucosal hypothesis, but it is not a demonstrated route to suppressing MSU-crystal C5a generation in synovial fluid. No gut → systemic complement-cascade coupling, transit time, absorption/metabolism, or flare timing model is implemented.

2. **Synovial-effective DAF concentration is assumed, not derived.**  
   The DAF arm assumes 10–500 nM effective DAF at the MSU surface after engineered-koji secretion/delivery. No delivery, epithelial transport, systemic exposure, synovial penetration, proteolysis in vivo, or local retention model is present. This is a nominal concentration prior standing in for a physiologic exposure process.

3. **The combined model multiplies two geographically different effects as if they act on the same residual pool.**  
   `f_combined = 1 - (1 - f_RA)(1 - f_DAF)` is mathematically standard for independent fractional reductions on the same outcome, but the artifact does not establish that gut-luminal RA inhibition and synovial/MSU-surface DAF decay act on a common denominator over the same exposure window.

4. **No finite mass balance or residence time.**  
   RA gut concentrations are transient; DAF surface engagement is assumed steady; MSU complement activation occurs over minutes to hours. These time bases are not reconciled.

5. **Sensitivity analysis omits dominant structural uncertainties.**  
   The reported Spearman analysis samples RA IC50, RA gut concentration, and DAF concentration at fixed α = 0.20. It does not sample α, DAF half-saturation, max acceleration, gut-to-joint coupling, RA residence time, complement availability in the gut, or DAF delivery. The output text nevertheless elevates α as the single wet-lab uncertainty that can upgrade the verdict.

6. **Several output interpretations are numerically stale or wrong.**
   - `daf_alone_predicted.json` says α changes median decay fraction from “~0.03 to ~0.78 — a 26× range,” but the same file reports medians 0.568, 0.815, 0.914. That statement is false for the committed output.
   - `outputs/summary.md` and the generated summary in `analyze.py` say α ≥ 0.5 would re-run comp-029 to GREEN. Under the implemented decision rule and RA median 0.886, GREEN is impossible because even a perfect combined effect has ratio ≤ 1 / 0.886 ≈ 1.13.
   - The “no interaction blocker” section is a narrative literature assertion, not a coded derivation. It may be reasonable as absence-of-known-evidence, but it should not be framed as a closed RED path without primary-source verification of the interaction space.

Constraint closure:

- **Reaction substrates/products/cofactors:**  
  RA inhibition is modeled only as a Hill fraction against C3 convertase/C3b deposition; actual C3, C3b thioester chemistry, serum proteins, RA conjugation/oxidation, and complement pathway components are not represented. DAF decay is modeled as a scalar acceleration of convertase decay; C2a/Bb dissociation, C3b/C4b binding, CP vs AP differences, and Factor H/I regulation are not represented.
- **Operating concentration vs constants:**  
  Fluid RA is far below IC50 and correctly predicted near zero. Gut RA reaches/exceeds IC50 in the model, but the relevant complement compartment is not established. DAF 10–500 nM and half-saturation 50 nM are assumed, not measured for soluble SCR1-4 on MSU.
- **Mass balance/replenishment/time:**  
  Not implemented. No finite C3/C5 pool, no MSU surface area, no complement replenishment, no RA degradation/residence, no DAF clearance.
- **Localization/access/transport:**  
  The largest biological gap. Oral/gut-luminal RA and engineered DAF are treated as if they can affect gout-relevant MSU-surface complement without a transport model.
- **Coproducts/off-targets/safety:**  
  Complement suppression off-targets, infection risk, gut barrier effects, RA catechol/redox behavior, and DAF immunogenicity/host-complement interference are not modeled.
- **Sensitivity coverage:**  
  Convenient kinetic/concentration priors are sampled; dominant topology and delivery uncertainties are mostly scenario labels, not variables.

## Summary-fidelity audit
- **README:** Mostly matches the headline YELLOW table, but overstates the wet-lab upgrade path by saying DAF accessibility measurement could “confirm GREEN.” Under the implemented model, higher α does not produce GREEN; the high α = 0.80 case remains YELLOW.
- **`outputs/summary.md`:** Contains a major unsupported handoff: “If §1.25 returns α ≥ 0.5, comp-029 re-runs to GREEN.” This directly contradicts the committed high-α output and the mathematical cap from RA’s singleton median. Also uses the stale/incorrect DAF uncertainty text indirectly through outputs.
- **`combined_predicted.json`:** Numeric verdicts are internally consistent for independent composition, but the coupled-scenario outputs saturate to 1.0 for medium/high α and are not integrated into a transparent decision table. The interaction-blocker assessment is narrative, not computational.
- **`daf_alone_predicted.json`:** The dominant-uncertainty sentence is numerically wrong relative to the medians in the same file.
- **Interpretive page `wiki/combined-cp0-systems-model-computational.md`:** Repeats the α ≥ 0.5 → GREEN claim and should be corrected. It also says the top wet-lab measurement can upgrade the prediction most; it can tighten DAF-alone uncertainty, but it cannot clear the comp-029 GREEN rule while RA gut-luminal singleton remains ~0.886.
- **`wiki/computational-experiments.md`:** The compact entry’s YELLOW numbers are consistent, but the “optional co-treatment arm gated on α ≥ 0.5” implication is unsupported if it implies GREEN upgrade.
- **`wiki/validation-experiments.md` §1.25:** The actual §1.25 protocol, as inspected, does not appear to add the RA co-treatment arm; that is consistent with the YELLOW result. External pages should not instruct §1.25 to add RA based solely on α ≥ 0.5.
- **`wiki/complement-c5a-gout.md` §9.7:** Needs correction where it propagates the comp-029 wet-lab handoff and gut-luminal RA reframe. The “combined thesis parked” statement is fine; the α-to-GREEN re-open condition is not.
- **H05 hypothesis card:** Already emphasizes DAF folding/function/access as wet-lab unknowns. It should be updated to reflect comp-029’s YELLOW cap if it continues to cite RA + DAF as a complementary combined strategy.
- **Reproducibility contract:** README command says `cd experiments/comp-029-combined-cp0-systems-model`, but the tracked path is `wiki/etc/experiments/comp-029-combined-cp0-systems-model`. Also, `analyze.py` would generate a `summary.md` link to `../../wiki/validation-experiments.md`, while the committed `outputs/summary.md` contains `../../../validation-experiments.md`. That suggests code/output drift for at least the generated Markdown link.

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| RA IC50 sampled log-uniform [5, 180] µM | `analyze.py` constants; `rosmarinic_acid_ic50_data.json`; `provenance.md` | Hardcoded, not read from JSON | Sahu/Englberger values are citation/abstract/snippet tier; primary full text deferred | Usable as provisional prior, but provenance is not primary-verified and input file is not executable source |
| Exclusion of 1500 µM C5-convertase IC50 | `analyze.py`; README; IC50 JSON | Hardcoded modeling choice | Citation-level; mechanistic rationale stated | Reasonable mechanistic choice, but should be explicitly sensitivity-tested because it controls optimistic RA potency |
| Fluid-phase RA 5–100 nM | `analyze.py`; RA bioavailability JSON | Hardcoded | Baba 2004 quoted via Kang 2021 review, primary not fetched | Correctly shows systemic free RA is near-zero; primary verification unresolved |
| Gut-luminal RA 50–1100 µM | `analyze.py`; RA bioavailability JSON | Hardcoded; used for combined model | Kang 2021 review/calculation; not a direct measured gout-relevant exposure | Load-bearing and biologically under-closed; gut-luminal-to-gout coupling not implemented |
| RA GI stability 69–75% intestinal recovery | RA bioavailability JSON | Not used | Veras 2022 PMC cited | Stored but unused; gut RA exposure likely over-idealized |
| Plasma protein binding 91.4% bound / 8.6% free | RA bioavailability JSON | Not used directly; fluid range already free | Kang 2021, partly unpublished rat-plasma data | Stored but unused; systemic conclusion still likely robust |
| DAF concentration 10–500 nM | `analyze.py`; DAF JSON | Hardcoded | Derived from comp-030 secretion-stage expectation and assumed synovial dilution | Major unverified exposure substitution; no delivery/transport model |
| DAF accessibility α = 0.05/0.20/0.80 | `analyze.py`; DAF JSON | Hardcoded | Explicit wet-lab unknown | Scenario grid is useful, but α cannot upgrade to GREEN under current decision rule |
| DAF half-saturation 50 nM | `analyze.py` only | Hardcoded | Described as order-of-magnitude prior; not measured | Load-bearing for DAF medians; absent from JSON/provenance table as a verified source |
| DAF max acceleration 20× | `analyze.py`; README | Hardcoded | Membrane DAF literature cited; soluble SCR1-4 likely lower | Optimistic ceiling; no sensitivity despite importance |
| Intrinsic C4b2a half-life 7.5 min | `analyze.py`; DAF JSON | Output only; cancels from implemented fraction | Fischer 1981 abstract-tier | Presented as kinetic input but not load-bearing in current formula |
| MSU C5a generation / deposition rate | `msu_c3b_deposition_rate.json`; DAF JSON | Not used | Wessig/Khameneh cited | Stored but unused; no finite MSU/complement mass balance |
| Decision rule GREEN ratio 1.5 + CI separation | `model_parameters.json`; README | Hardcoded in code, not read from JSON | Internal rule | Correctly yields YELLOW, but later α ≥ 0.5 → GREEN text violates the same rule |
| Combined median 1.08–1.10× better singleton | `combined_predicted.json`; `summary.md` | Derived from Monte Carlo | Reproducible by inspection of formulas/output | Internally consistent for toy model |
| “α ≥ 0.5 re-runs to GREEN” | `outputs/summary.md`; interpretive page; complement page | Not derived; contradicted by high α output | No support | False; must be removed or replaced |
| “DAF median changes ~0.03 to ~0.78, 26×” | `daf_alone_predicted.json` dominant uncertainty text | Generated narrative | No support in same output file | False/stale; medians are 0.568 to 0.914 |
| No RA–DAF interaction blocker | `combined_predicted.json`; `summary.md` | Narrative assessment only | Literature absence asserted; no primary interaction search in artifact | Should be softened to “no blocker identified in searched/cited corpus,” not RED path closed |

## Affected wiki pages
- `wiki/combined-cp0-systems-model-computational.md` — change required — remove/correct the α ≥ 0.5 → GREEN re-open condition; clarify that DAF α measurement tightens DAF-alone uncertainty but cannot satisfy the current GREEN ratio while RA gut-luminal singleton is saturated.
- `wiki/computational-experiments.md` — change required — compact comp-029 entry is numerically consistent, but any “optional co-treatment gated on α ≥ 0.5” framing should be softened or removed because the artifact does not support GREEN upgrade.
- `wiki/complement-c5a-gout.md` — change required — §9.7 repeats the comp-029 handoff and should distinguish gut-luminal RA as a local/transient hypothesis from synovial CP0 coverage; remove the α ≥ 0.5 → GREEN claim.
- `wiki/validation-experiments.md` — already consistent / monitor — inspected §1.25 does not add the RA co-treatment arm; keep it gated off unless a corrected model justifies it.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` — change required — add comp-029’s YELLOW/structural-cap result if the card continues to cite RA + DAF complementarity; preserve DAF folding/function/access as the real wet-lab gates.
- `wiki/upstream-complement-assay-format-mapping-computational.md` — already consistent — it notes comp-021 would narrow RA IC50 while YELLOW likely holds; if comp-029 is rerun, cite this as the updated RA prior.
- `wiki/chaperone-orthogonal-stacking.md` — already consistent — §1.25 calibration role is about DAF expression/folding, not comp-029 co-treatment efficacy.

## New connections or implications
- **The comp-029 GREEN rule is structurally unreachable under the selected RA regime.** With RA gut-luminal median ≈0.886, even perfect DAF can only raise combined median to 1.0, giving a maximum combined/better-singleton ratio of ≈1.13. Therefore, α measurement can never be the “cheapest path to GREEN” unless the decision rule or RA operating regime changes.
- **Comp-021 weakens the need to prioritize RA IC50 uncertainty for comp-029.** The later assay-format mapping narrows gut-relevant RA IC50 to 34–180 µM and says YELLOW likely holds. The comp-029 artifact has not incorporated that update; the result probably remains YELLOW, but with different RA singleton median/CI.
- **The real unresolved system is not α alone; it is compartment coupling.** DAF α is important for a DAF-on-MSU assay, but comp-029’s combined biological claim depends more fundamentally on whether gut-luminal RA and delivered DAF act on the same gout-relevant complement pool within the same flare window.
- **A better wet-lab design implication:** §1.25 should first measure DAF SCR1-4 expression, folding, and functional C5a suppression alone. A RA co-treatment arm should be justified by a corrected same-compartment assay rationale, not by α ≥ 0.5.

## Required actions
1. **Correct comp-029 generated summaries and wiki propagation.** Owner surface: `outputs/summary.md`, README, `wiki/combined-cp0-systems-model-computational.md`, `wiki/complement-c5a-gout.md`, `wiki/computational-experiments.md`. Verification criterion: no page claims α ≥ 0.5 or high DAF accessibility re-runs comp-029 to GREEN under the current decision rule.
2. **Fix stale/false DAF uncertainty text.** Owner surface: `analyze.py` output text and `outputs/daf_alone_predicted.json`. Verification criterion: narrative medians/ranges match reported medians 0.568, 0.815, 0.914, or the text is removed.
3. **Reconcile code and committed outputs.** Owner surface: `analyze.py` and `outputs/summary.md`. Verification criterion: rerunning the stated command regenerates byte-equivalent or intentionally versioned outputs, including links.
4. **Fix the reproduction command/path.** Owner surface: README. Verification criterion: command works from repo root, likely `cd wiki/etc/experiments/comp-029-combined-cp0-systems-model && python3 analyze.py`.
5. **Make executable inputs real or label them documentation-only.** Owner surface: `analyze.py` and input JSONs. Verification criterion: load-bearing values are read from JSON with assertions, or README explicitly states the JSON files are provenance records and the code hardcodes priors.
6. **Add a model-limit statement for compartment coupling.** Owner surface: README, output summary, interpretive page. Verification criterion: readers are told the model does not establish gut-luminal RA → synovial MSU complement suppression or oral DAF → synovial effective concentration.
7. **If rerun/revision is desired, include dominant uncertainties.** Owner surface: future comp-029 v2. Verification criterion: sensitivity or scenario analysis includes DAF α, DAF half-saturation, max acceleration, same-compartment RA scenarios, RA residence/GI loss, and DAF delivery/access, not only convenient concentration/IC50 draws.
8. **Primary-source verification remains unresolved.** Owner surface: `inputs/provenance.md`. Verification criterion: Sahu 1999, Englberger 1988, Baba 2004, Wang 2017, Fischer 1981, and Medof 1984 are either primary-source checked or explicitly retained as secondary/abstract-tier priors.

## Review limits
- I did not execute `analyze.py`; reproducibility was assessed by code/output inspection only.
- Repository `grep_repo` failed because the environment lacks `rg`; affected-page discovery therefore relied on the provided bundle plus targeted `read_file` calls.
- `wiki/validation-experiments.md` is very large; I inspected the provided bundle and the region containing §1.25, not every later byte.
- Primary papers were not independently fetched; provenance status is reported as the artifact states it.
- Numeric Monte Carlo values were not independently recomputed, but the formulas and reported outputs were checked for internal consistency and contradictions.
