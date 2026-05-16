# comp-002 — Uricase Shio-Koji Thermal/pH Stability: Summary

**Protein:** Uricase (urate oxidase), Aspergillus flavus (Q00511)  
**Reference conditions:** 17.5% NaCl, pH 5.25, 22.0°C, 14 days  
**Analysis date:** 2026-05-16  
**Script:** `experiments/comp-002-uricase-shio-koji-thermal-stability/analyze.py`  

---

## Headline verdict: **MODERATE** (YELLOW)

Predicted activity retention at reference shio-koji conditions (17.5% NaCl, pH 5.25, 22.0°C, 14 days): **64.0%** (uncertainty band: 0.2–100.0%).  

Tm gap (Tm − T_ferment) = 5.0°C. Extrapolated half-life at 22.0°C ≈ 22.07 days (Lumry-Eyring two-state model with kinetic refolding protection; empirical anchor: 38 min half-life at 40°C, Imani & Shahmohamadnejad 2017).

---

## Structural axis — tetramer interface integrity (pLDDT)

| Interface region | N residues | Mean pLDDT | Min pLDDT | % > 80 | % > 90 |
|---|---|---|---|---|---|
| Tight dimer (A-B; active-site shared loop) | 81 | 97.7 | 94.1 | 100.0% | 100.0% |
| Tetramer interface (A-C / A-D) | 48 | 96.1 | 81.8 | 100.0% | 97.9% |
| All interface residues | 129 | 97.1 | 81.8 | 100.0% | 99.2% |

**Composite weighted-mean interface pLDDT:** 97.3 → interface integrity score = **1.0** (0-1 scale).

All interface residues sit at pLDDT well above the 80-threshold for confident burial. AlphaFold has high confidence in the interface fold quality — interface flexibility is not the load-bearing failure mode.

---

## Reference-condition decomposition

| Axis | Contribution | Notes |
|---|---|---|
| Thermal retention (two-regime, native+unfolded) | 64.4% | k_eff(22.0°C) = 2.18e-05 min⁻¹; half-life ≈ 22.07 days |
| Fraction unfolded at ferment T (van't Hoff) | 6.2069% | Tm = 27°C; ΔH_vH = 400 kJ/mol; cooperative transition |
| Fraction unfolded at 40°C anchor (reference) | 99.9% | For comparison — at the empirical-anchor temperature |
| pH-interface integrity (mean over 3 modeled salt-bridge pairs) | 91.4% | Henderson-Hasselbalch on Asp/Glu at interface, pH 5.25, pKa ~4.0-4.4 |
| Salt stabilization factor | ×1.058 | Hofmeister kosmotrope effect at 17.5% NaCl |
| Composite retention | **64.0%** | (0.2%–100.0% band) |

---

## Sensitivity sweep — which parameters drive the verdict?

Variance in retention prediction when each parameter is varied across its grid (other parameters held at reference values):

| Parameter | Range scanned | Retention range | Spread |
|---|---|---|---|
| temperature_C | 22.0–32.0 | 0.0%–61.3% | 61.3 pp |
| duration_days | 7–30 | 37.1%–76.4% | 39.3 pp |
| pH | 4.5–6.0 | 52.0%–67.4% | 15.4 pp |
| NaCl_pct | 5.0–20.0 | 58.9%–61.5% | 2.6 pp |

**Top driver:** the parameter with the largest spread is the load-bearing condition for the verdict.

---

## Failure-mode ranking

| Failure mode | Loss contribution (1 − axis term) | Verdict-load |
|---|---|---|
| Thermal kinetics (Lumry-Eyring two-state) | 35.6% |  ← **dominant** |
| pH-dependent interface ion-pair disruption | 8.6% |  |
| Salt destabilization (net) | 0.0% |  |
| Structural interface flexibility (pLDDT proxy) | 0.0% |  |

---

## Per-condition sweep — full grid

Top 5 worst-case conditions (lowest retention):

| T (°C) | pH | NaCl% | Days | Retention | Band |
|---|---|---|---|---|---|
| 25.0 | 4.5 | 5.0 | 30 | 0.0% | 0.0–27.2% |
| 25.0 | 4.5 | 10.0 | 30 | 0.0% | 0.0–27.6% |
| 25.0 | 4.5 | 15.0 | 30 | 0.0% | 0.0–28.1% |
| 25.0 | 4.5 | 17.5 | 30 | 0.0% | 0.0–28.1% |
| 25.0 | 4.5 | 20.0 | 30 | 0.0% | 0.0–28.1% |

Top 5 best-case conditions (highest retention):

| T (°C) | pH | NaCl% | Days | Retention | Band |
|---|---|---|---|---|---|
| 22.0 | 6.0 | 20.0 | 7 | 84.1% | 5.2–100.0% |
| 22.0 | 6.0 | 17.5 | 7 | 83.9% | 5.2–100.0% |
| 22.0 | 6.0 | 15.0 | 7 | 83.2% | 5.2–100.0% |
| 22.0 | 5.5 | 20.0 | 7 | 82.1% | 4.9–100.0% |
| 22.0 | 5.5 | 17.5 | 7 | 81.9% | 4.9–100.0% |

---

## Verdict reasoning

**MODERATE (YELLOW).** 
Predicted retention at the reference condition is 64.0% (band 0.2–100.0%) — 
this is the model's best estimate combining Lumry-Eyring thermal kinetics with kinetic refolding protection, pH-mediated interface salt-bridge integrity, AlphaFold structural confidence, and salt-Hofmeister effects. The wide uncertainty band reflects the sensitivity of the prediction to Tm and ΔH_vH — biophysical anchors that should be tightened by direct DSF on Q00511.

### Key factors driving the verdict

1. **Temperature is the dominant driver.** Sensitivity sweep spread for T (22–32°C) is 61 percentage points — far larger than pH (15 pp) or NaCl (3 pp). A few degrees of summer-side ferment temperature (28-30°C in a warm kitchen) drops retention sharply because it pushes the enzyme across its measured Tm = 27°C.
2. **Tm gap is narrow (5°C).** WT *A. flavus* uricase has a measured Tm of only 27°C (Imani & Shahmohamadnejad 2017, PMID:28667645; DOI:10.1007/s13205-017-0841-3). Shio-koji at 22°C sits 5°C below the cooperative-unfolding midpoint — within the sub-Tm kinetic-refolding-protected regime, but not comfortably so. Engineered disulfide variants (Ala6Cys, Ser282Cys; Rezaeian Marjani 2020, PMID:33850949; DOI:10.30498/IJB.2020.2662) raise the optimum-activity temperature by 10°C and thermal half-life ~3.6× — the dominant single engineering intervention available if §1.10 wet-lab data indicates thermal instability is the limiting failure mode.
3. **Kinetic refolding protection is what keeps WT viable at all.** The Lumry-Eyring model applies an f_u² scaling in the sub-Tm regime: irreversible loss requires both unfolding (6% population at 22°C) and aggregation outcompeting refolding (modeled by the second f_u factor). Without this protection, predicted retention would be near-zero. The model is most uncertain in this scaling — wet-lab data is the right tool to disambiguate.
4. **Interface salt-bridge integrity is the secondary pH-dependent risk.** At pH 4.5 (lower edge of shio-koji range), modeled Asp/Glu salt-bridge partners are ~88% deprotonated (still mostly intact). At pH 5.25 (midpoint), 91%; at pH 6.0, 96%. The pH axis contributes 15 pp of retention spread — meaningful but not dominant.
5. **Salt is mildly stabilizing, not destabilizing.** Unlike the protease-activity axis (where 15-20% NaCl suppresses protease activity, comp-001), the thermal-stability axis has NaCl acting as a kosmotrope — net +5.8% stabilization via preferential hydration of the native tetramer state. NaCl sensitivity sweep spread is only 3 pp — salt is essentially neutral on this axis.

### Limitations (named explicitly; some incorporated into the uncertainty band, others stated for transparency)

- **Tm = 27°C is from a single primary source** (Imani & Shahmohamadnejad 2017). The result is biologically plausible (fungal cytosolic enzyme, no PTMs, no native disulfides per UniProt Q00511 — low Tm consistent with these features) but a second independent DSF measurement on Q00511 would harden this load-bearing anchor. Uncertainty bracket: Tm ± 2°C → retention band widens substantially. If the true Tm is ~32°C (modestly higher than measured) the picture shifts toward GREEN; if the true Tm is ~25°C the picture shifts toward RED.
- **ΔH_vH = 400 kJ/mol is a generic biophysical prior**, not directly measured for Q00511. Literature range for globular proteins is 300-600 kJ/mol. Uncertainty bracket uses 300-500 → contributes most of the model uncertainty.
- **Lumry-Eyring f_u² sub-Tm scaling is a heuristic.** The exact power of f_u depends on the ratio of refolding to aggregation rate constants, which are protein-specific and not measured here. f_u² is a conservative middle ground; the true exponent could be anywhere from 1 (no refolding protection) to 3+ (strong protection). Multi-temperature inactivation kinetics at sub-Tm temperatures (e.g., 22°C, 25°C, 27°C, 30°C, 33°C in buffer) would empirically determine this — this is the highest-value follow-up experiment if §1.10 results are ambiguous.
- **Interface salt-bridge pKa values are estimated, not measured.** Three salt-bridge pairs were inferred from the published interface footprint and the sequence pKa pattern; per-residue pKa shift (from local electrostatic environment) was approximated as +/- 0.5 in the uncertainty band. PROPKA or H++ on the PDB coordinates would tighten these by ~0.2 pH units.
- **No PDB coordinate extraction.** Interface footprint is from published structural analyses (Retailleau et al. 2004, PDB 1R56; Colloc'h et al. 1997), not directly extracted from PDB coordinates in this run (stdlib-only constraint). A future MD-based comp-NNN with explicit PDB parsing would tighten the interface residue set by 1-3 positions per range.
- **No MD simulation.** Brief proposed GROMACS/OpenMM trajectory of the tetramer in 15% NaCl at 295K; this analysis is the composite-prior version. MD remains the rigorous next step if §1.10 wet-lab data deviates from predictions.
- **Activity ≠ stability.** The pH-activity curve values (12% at pH 4.5, 25% at pH 5.0) measure catalytic competence, not tetramer integrity. The thermal/pH retention prediction is for *post-ferment residual activity at assay pH*, which after return to assay pH 7.5-8.5 recovers catalytic activity if the tetramer survived storage at low pH.
- **Tetramer dissociation not directly modeled.** The pH axis approximates interface fragility via salt-bridge integrity, but actual dimer-to-monomer dissociation requires AUC or SEC measurements at the ferment pH — not done here. If the tetramer dissociates and monomers reassemble on dilution to assay pH, the readout would not detect transient dissociation.
- **Single ferment-pH endpoint modeled.** Real shio-koji ferments may drift in pH over 7-14 days as residual koji enzymes process the matrix. pH drift toward 4.0-4.5 over the ferment would worsen the verdict; pH stable at 5.5-6.0 would improve it. §1.10 should measure pH over time as part of the data collection.

---

## Wet-lab handoff

This analysis informs `validation-experiments.md` §1.10 (uricase + lactoferrin stability in shio-koji ferment) and §1.16 (OPT-1 disulfide-engineered uricase in koji vs. WT — GI survival head-to-head).

**For §1.10:** comp-001 already established the protease axis as LOW risk; comp-002 establishes the thermal/pH axis as **YELLOW (MODERATE)** — driven primarily by the narrow Tm gap (5°C below T_ferment) and the pH 4.5 lower-edge vulnerability of interface salt bridges. §1.10 should specifically measure: (i) day-0/7/14 SDS-PAGE band intensity for the 34-kDa monomer (proteolysis check, already in §1.10); (ii) **native-PAGE for ~135-kDa tetramer band intensity** at each timepoint (NEW addition motivated by this analysis — tests tetramer integrity directly); (iii) **specific activity per total protein** at each timepoint (combines fold + tetramer assembly into one readout); (iv) pH measurement of the ferment (lactic acid from native koji metabolism may push pH below 5.0 — the lower edge of the modeled range).

**For §1.16:** this analysis reinforces the strategic value of the OPT-1 disulfide-engineered variant. The thermal-stability boost from disulfide engineering (10°C in T_opt, ~3.6× in thermal half-life; Rezaeian Marjani 2020) is the cleanest single intervention to address the comp-002 Tm-gap risk. If §1.10 confirms the thermal axis is the limiting failure mode for WT, §1.16 becomes higher-priority — it directly addresses the chokepoint identified here.

---

*Generated by `analyze.py` on 2026-05-16. Re-run after any updated Tm measurement, multi-temperature inactivation experiment, or PDB-based interface refinement. See `inputs/provenance.md` for data sources.*
