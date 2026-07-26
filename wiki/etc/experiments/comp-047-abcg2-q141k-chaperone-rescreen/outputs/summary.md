# comp-047 — Summary

**Frozen docking run date:** 2026-07-14

**Method:** static-receptor AutoDock Vina at a modeled residue-141 region and Walker-A comparison box, followed by ChEMBL inhibition and UniProt/DrugBank relationship exclusion.

**Vina:** seed 20260714, exhaustiveness 8, cpu 4; N=134 docked.

## VERDICT: INCONCLUSIVE — NO DEFENSIBLE DOCKING-BACKED RANKING

Executable rule output after both Axis-2 checks: **0 yes**, **1 uncertain**. An executable row is not a wet-lab priority: the screen has no validated ABCG2 chaperone positive control, uses a static conformation, and produced unstable fold-site rankings under the recorded perturbations.

## Executable marginal rows (not wet-lab priorities)

| rank | molecule | class | fold@Q141K | Walker A | margin | Q141K−WT proxy | ChEMBL activity | DrugBank relationship | tier |
|---|---|---|---|---|---|---|---|---|---|
| 1 | vorinostat | HDAC inhibitor | -6.19 | -5.64 | 0.55 | 0.23 | no | no | uncertain |

## Base-run fold-site scores (descriptive, not a robust ranking)

The table records the strongest scores in the original box. It is not a fallback shortlist: the sensitivity artifact shows material rank changes under box, seed, and protonation perturbations, and Axis 2 remains an exclusion layer rather than evidence of chaperone activity.

| rank | molecule | class | fold@Q141K | Walker A | margin | excluded by Axis 2? |
|---|---|---|---|---|---|---|
| 1 | avacopan | C5aR1 antagonist | -7.82 | -7.54 | 0.28 | no |
| 2 | lumacaftor | CFTR corrector | -7.35 | -8.77 | -1.42 | no |
| 3 | rosuvastatin | Statin | -6.80 | -6.26 | 0.54 | yes |
| 4 | ver155008 | Hsp70 inhibitor (research) | -6.46 | -7.60 | -1.14 | no |
| 5 | spiperone | Antipsychotic / receptor probe | -6.45 | -7.64 | -1.19 | no |
| 6 | mcc950 | NLRP3 inhibitor (research) | -6.38 | -7.32 | -0.94 | no |
| 7 | novobiocin | n/a | -6.36 | -6.61 | -0.25 | yes |
| 8 | elacridar | P-gp/ABCG2 inhibitor | -6.30 | -8.23 | -1.94 | yes |
| 9 | glycerol_phenylbutyrate | Ammonia scavenger / chaperone | -6.20 | -5.94 | 0.26 | no |
| 10 | vorinostat | HDAC inhibitor | -6.19 | -5.64 | 0.55 | no |
| 11 | tariquidar | P-gp/ABCG2 inhibitor | -6.16 | -7.75 | -1.59 | yes |
| 12 | sorafenib | Multikinase TKI | -6.11 | -7.14 | -1.03 | yes |
| 13 | ezetimibe | Cholesterol absorption inh | -6.06 | -6.23 | -0.17 | yes |
| 14 | lisinopril | ACE inhibitor | -6.06 | -6.69 | -0.63 | no |
| 15 | gefitinib | EGFR TKI / ABCG2 substrate | -5.95 | -7.18 | -1.23 | yes |

**Walker-A comparison diagnostic:** scores span -8.77..-3.51 (median -6.09); modeled fold-site scores span -7.82..-1.85 (median -4.86). The substantial overlap makes the margin rule non-discriminating in this configuration; it does not establish a selective fold-site interaction.

**Sensitivity diagnostic:** among the recorded non-base perturbations, 2–7 of the eight tracked candidate positions changed. The base-run fold ranking is therefore not treated as robust.

## Interpretation boundary

- Rosuvastatin is removed from the executable shortlist because it is independently identified as a BCRP substrate and is also present in the UniProt/DrugBank ABCG2 relationship set.
- Vorinostat is the sole marginal executable row. Its direct Q141K rescue precedent is phenotypic and independent of this docking result; it does not validate the modeled pocket or make the docking row a wet-lab priority.
- Failure to recover the CFTR comparators is a setup-specific diagnostic, not evidence that ABCG2 cannot be pharmacologically rescued.
- The decisive next observation is the registered Q141K surface-trafficking + urate-flux + ABCG2-inhibition counterscreen in validation experiment §1.22, not another pass through the same docking configuration.

## Load-bearing limitations

- Q141K is a static side-chain substitution, not a folding-ΔΔG model.
- A folding intermediate and mutant-selective stabilization are not modeled.
- The receptor is an apo monomer; the Walker-A box is not the physiological composite ATP site or the transmembrane substrate cavity.
- Vina scores and close margins are not binding-affinity measurements.
- Exposure at the intracellular folding compartment is not modeled.

See `controls.md`, `sensitivity.json`, `receptor_verification.json`, and the README.
