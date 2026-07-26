PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 248abfa19e377c97848a3f5d185df0f92e56b6dd395cffce410fe5c9f63bb7b9

# Adversarial pre-run review — comp-044

## Reviewed snapshot

Reviewer: `/root/comp044_gate1` (context-isolated). Manifest SHA-256: `248abfa19e377c97848a3f5d185df0f92e56b6dd395cffce410fe5c9f63bb7b9`. Five design files and two prior-output baselines. The manifest check passed and every bound file matched the inspected snapshot. Historical outputs and reviews were deferred until after the independent design audit.

## Bottom-line verdict

The experiment may run. The active snapshot consistently corrects the 0.59 µM prior from “jejunal/healthy baseline” to a terminal-ileal clinical-cohort measurement across input keys, named scenarios, decision rules, planned outputs, limitations, and propagation instructions.

Static comparison with the preceding artifact shows no change to numerical inputs, formulae, factor levels, sensitivity-grid membership, dose set, ratio thresholds, or verdict mapping. The old outputs contain the superseded labels but are explicitly bound as historical baselines; the documented rerun will replace them.

Independent primary-source inspection verified the corrected provenance:

- Miyazaki et al. 2025: PMID 40033341; PMCID PMC11877951; DOI 10.1186/s12967-025-06145-7.
- Figure 1 depicts transanal double-balloon sampling in the distal small intestine immediately proximal to the ileocecal junction; the supplementary methods state that all procedures occurred in the terminal ileum of the pelvis.
- The cohort comprised 34 clinically indicated endoscopy patients: Crohn’s disease, n=30; simple ulcers, n=2; obscure gastrointestinal bleeding, n=2.
- Fluid was collected from small-intestinal segments without lesions, but the cohort was not a healthy-population sample.
- The reported baseline median was 99.5 pg/µL, with IQR 10.1–194.0 pg/µL.
- `99.5 pg/µL = 99.5 µg/L`; using urate molecular weight 168.11 g/mol gives 0.591874 µmol/L, correctly represented as 0.59 µM.

## Question and model fit

The computation tests whether COMP-019’s unconditional 5–50 mg/day saturated-capacity classification survives its own concentration and Km assumptions after finite active time and explicit scenario penalties are applied. It does not estimate native dynamic luminal concentration, dose sufficiency, serum-urate change, clinical efficacy, topology, chassis, production sufficiency, or safety.

The terminal-ileal cohort value remains a fixed-concentration diagnostic prior rather than a healthy physiological baseline. The model compares window-limited capacity against a whole-day 233 mg flux denominator, so it is an internal-consistency counterexample/regime audit rather than a local dynamic mass-balance model. The README, provenance, output interpretations, and authoring boundaries state this limitation without converting the measurement into a broader physiological claim.

## Constraint and implementation audit

`capacity_ratio()` traces the bound inputs as:

dose × 8.3 U/mg × 0.75 activity factor × 60 min/hour × active hours × `urate/(Km+urate)` × oxygen × access × survival, followed by µmol-to-mg conversion using 168.11 g/mol and division by 233 mg/day.

Units, signs, denominators, and factor placement are internally coherent for the declared bounded model. The terminal-ileal prior feeds the scenario construction, exhaustive grid, diagnostic selection, regression guard, verdict mapping, provenance output, and summary labels through the renamed key. `assert_config_consistency()` will fail if duplicated grid or named-scenario values drift.

The label correction does not alter:

- 0.59 µM central, 0.06–1.16 µM selected range;
- Km 5/25/100 µM;
- 2/3/4/24-hour windows;
- 5/25/50 mg doses;
- oxygen, access, survival, or pH/activity factors;
- 1,620 grid cells per dose;
- ratio-one mass-balance boundary or descriptive 0.25/4 bins;
- legacy-control, not-robust, and contrary verdict branches.

Oxygen kinetics, depletion, coproduct peroxide, dynamic substrate replenishment, reabsorption, renal compensation, microbiome metabolism, topology, and tissue safety remain outside the model and are explicitly retained as limitations or downstream experimental gates.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 0.59 µM terminal-ileal clinical-cohort prior | `model_parameters.json`; `provenance.md`; named scenarios | Michaelis–Menten occupancy numerator in the central diagnostic | Primary paper, Figure 1, and supplementary methods independently verified; correct compartment and cohort boundary | Pass |
| 99.5 pg/µL median; 10.1–194.0 pg/µL IQR | `provenance.md` | Source basis for the selected terminal-ileal range | Verified directly in Miyazaki et al. | Pass |
| 99.5 pg/µL → 0.591874 µM → 0.59 µM | `provenance.md`; `model_parameters.json` | Central concentration input | Unit conversion independently verified with 168.11 g/mol | Pass |
| 8.3 U/mg and 0.75 multiplier | `model_parameters.json`; `capacity_ratio()` | Converts enzyme mass to scenario-adjusted capacity | Explicitly labeled inherited/non-planning-grade rather than newly primary-verified | Pass for bounded audit |
| Km 5–100 µM, central 25 µM | Inputs; consistency checks; scenarios/grid | Occupancy denominator and sensitivity axis | Explicitly inherited and enzyme-context dependent | Pass for bounded audit |
| 2–4-hour active window | Inputs; scenarios/grid | Limits active capacity duration | Explicitly inherited, not a measured cohort parameter | Pass for bounded audit |
| 233 mg/day denominator | Inputs; `capacity_ratio()` | Legacy regime-comparison denominator | Explicitly derived corpus prior, not a local or patient-specific flux | Pass for bounded audit |
| Ratio = 1 decision boundary | `regime()`; `derive_verdict()`; output contract | Direct mass-balance comparison and verdict mapping | Predeclared; contrary branches are executable and self-checked | Pass |
| Terminal-ileal output labels | `analyze.py` result and summary builders | Replace stale historical scenario/provenance labels on regeneration | Consistently renamed through every output path | Pass |
| Conditional propagation | `README.md` | Controls canonical and downstream authoring by actual regenerated verdict | Canonical evidence home and branch-specific correction inventory are named | Pass |

## Falsification, sensitivity, and output contract

Contrary results can win. The decision rule separately emits:

- `LEGACY CONTROL NOT REPRODUCED` if the saturated control fails;
- `LEGACY ROBUSTNESS NOT REJECTED` if the control passes and every central terminal-ileal diagnostic dose remains at or above one;
- `LEGACY FLAT-DOSE REGIME NOT ROBUST` if the control passes and at least one diagnostic dose falls below one.

The self-check exercises all three branches. The output schema retains per-dose named-scenario ratios and regimes; grid counts, minima, maxima, and fractions on each side of ratio one; the selected verdict; explicit provenance status; and model limitations. Grid fractions are labeled design-space occupancy, not probabilities.

The two historical outputs use old scenario names, but they are prior-output baselines rather than authority for the proposed run. The new code emits the corrected names and adds the terminal-ileal provenance field without changing computational values or verdict semantics.

## Downstream authoring contract

The canonical evidence home is `wiki/gut-lumen-uricase-physiologic-regime-computational.md`. The README requires the regenerated verdict—not historical output—to control propagation and requires a search for stale `jejunal` or `healthy baseline` descriptions after regeneration.

The permitted claim remains narrow: COMP-044 may adjudicate robustness of COMP-019’s unconditional flat-dose classification under the tested diagnostics. It may not establish a replacement dose, physiological regime, serum-urate effect, genotype ordering, efficacy, topology/chassis choice, production sufficiency, or safety conclusion.

The gut-lumen sink and neighboring chassis/configuration ideas remain open where not tested. Configuration-level physiology and peroxide safety stay assigned to downstream wet-lab gates. Cross-track rankings remain confined to portfolio surfaces, and the authoring plan prohibits personalized treatment instructions, home-production recommendations, unsupported serum-effect claims, and editorial-history residue.

## Required actions before execution

None.

## Review limits

This was a static, read-only review. I did not execute `analyze.py` or any result-bearing logic. Primary-source verification covered the publisher PDF, Figure 1, main-text cohort/concentration reporting, and supplementary methods. The inherited specific-activity, Km, transit-window, and 233 mg/day priors were not independently upgraded to quantitative-planning evidence; the artifact explicitly preserves that limitation.
