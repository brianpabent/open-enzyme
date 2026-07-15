# comp-047 — Summary

**Generated:** 2026-07-15  
**Method:** AutoDock Vina docking (2 sites × WT/Q141K) + empirical ChEMBL ABCG2 grounding. Supersedes comp-032's descriptor/class-prior heuristic.  
**Vina:** seed 20260714, exhaustiveness 8, cpu 4. N=134 docked.

## VERDICT: INCONCLUSIVE — only weak/uncertain candidates; no high-confidence fold-selective hit

Candidates (fold-selective AND not known ABCG2): **0 yes**, **2 uncertain**.

## Ranked shortlist (candidates only)

| rank | molecule | drug_class | fold@Q141K | transport | margin | Q141K−WT sel. | ChEMBL ABCG2 | tier |
|---|---|---|---|---|---|---|---|---|
| 1 | rosuvastatin | Statin | -6.80 | -6.26 | 0.54 | 0.95 | no | uncertain |
| 2 | vorinostat | HDAC inhibitor | -6.19 | -5.64 | 0.55 | 0.23 | no | uncertain |

## Raw fold-site ranking (Axis 1a alone — box-choice-robust view)

Top fold@Q141K binders regardless of transport margin. Use with Axis 2: a strong fold binder that is a known ABCG2 inhibitor is still disqualified. This table exists so the shortlist is not hostage to the transport-box choice (see distribution note below).

| rank | molecule | drug_class | fold@Q141K | transport | margin | known ABCG2? |
|---|---|---|---|---|---|---|
| 1 | avacopan | C5aR1 antagonist | -7.82 | -7.54 | 0.28 | no |
| 2 | lumacaftor | CFTR corrector | -7.35 | -8.77 | -1.42 | no |
| 3 | rosuvastatin | Statin | -6.80 | -6.26 | 0.54 | no |
| 4 | ver155008 | Hsp70 inhibitor (research) | -6.46 | -7.60 | -1.14 | no |
| 5 | spiperone | Antipsychotic / receptor probe | -6.45 | -7.64 | -1.19 | no |
| 6 | mcc950 | NLRP3 inhibitor (research) | -6.38 | -7.32 | -0.94 | no |
| 7 | novobiocin | n/a | -6.36 | -6.61 | -0.25 | yes |
| 8 | elacridar | P-gp/ABCG2 inhibitor | -6.30 | -8.23 | -1.94 | yes |
| 9 | glycerol_phenylbutyrate | Ammonia scavenger / chaperone | -6.20 | -5.94 | 0.26 | no |
| 10 | vorinostat | HDAC inhibitor | -6.19 | -5.64 | 0.55 | no |
| 11 | tariquidar | P-gp/ABCG2 inhibitor | -6.16 | -7.75 | -1.59 | yes |
| 12 | sorafenib | Multikinase TKI | -6.11 | -7.14 | -1.03 | no |
| 13 | ezetimibe | Cholesterol absorption inh | -6.06 | -6.23 | -0.17 | no |
| 14 | lisinopril | ACE inhibitor | -6.06 | -6.69 | -0.63 | no |
| 15 | gefitinib | EGFR TKI / ABCG2 substrate | -5.95 | -7.18 | -1.23 | no |

**Transport-box distribution diagnostic:** transport affinities span -8.77..-3.51 (median -6.09); fold@Q141K span -7.82..-1.85 (median -4.86). If the transport (Walker A, apo-monomer) box binds most molecules as strongly as the fold box, the margin filter is over-permissive and the verdict should lean on fold-site absolute affinity + Axis 2, not margin. See interpretation in controls.md.

Margin = transport − fold@Q141K (>0 = prefers fold site over ATP site). 
Q141K−WT sel. = fold@WT − fold@Q141K (>0 = binds mutant better than WT — weak chaperone-selectivity proxy). 
See `controls.md` for the validity check and `../README.md` for limitations.

## Honest limitations (see README for full list)
- **Q141K is a static side-chain substitution**, not a folding-ΔΔG calculation. Docking to a static modeled mutant is a proxy for a fold-stabilizing interaction, not evidence of folding rescue.
- **Misfolded-state selectivity not modeled** — a true chaperone preferentially stabilizes the mutant folding intermediate; the WT/Q141K docking delta is a weak surrogate.
- **Apo monomer** — the physiological ATP-bound NBD dimer is not represented; the transport box is the Walker A P-loop only and tests ATP-competitive binding, NOT the TMD drug/urate cavity where most clinical ABCG2 inhibitors act. Axis 2 (ChEMBL) is the real inhibitor filter.
- **Vina scores are noisy** (~±1 kcal/mol); use ranks, not absolute affinities. See sensitivity.json.
