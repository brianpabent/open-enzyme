---
title: "Uricase Thermal/pH Stability in Shio-Koji — Computational Analysis (comp-002)"
date: 2026-05-16
tags: [uricase, shio-koji, thermal-stability, pH-stability, tetramer, alphafold, lumry-eyring, computational, koji-endgame-strain]
related:
  - computational-experiments.md
  - validation-experiments.md
  - uricase.md
  - uricase-variant-selection.md
  - uricase-protease-stability-computational.md
  - engineered-koji-protocol.md
  - koji-home-fermentation.md
sources:
  - "Imani, M. & Shahmohamadnejad, S. 2017. Recombinant production of *Aspergillus flavus* uricase and investigation of its thermal stability in the presence of raffinose and lactose. *3 Biotech* 7:201. DOI:10.1007/s13205-017-0841-3, PMID:28667645."
  - "Rezaeian Marjani, L. et al. 2020. Enhancement of pharmaceutical urate oxidase thermostability by rational design of disulfide bridge. *Iran J Biotechnol* 18:e2662. DOI:10.30498/IJB.2020.2662, PMID:33850949."
  - "Retailleau, P. et al. 2004. Complexed and ligand-free high-resolution structures of urate oxidase (Uox) from *Aspergillus flavus*. *Acta Cryst* D60:453-462. PDB 1R56."
  - "Colloc'h, N. et al. 1997. Crystal structure of the protein drug urate oxidase-inhibitor complex. *Nat Struct Biol* 4:947-952."
  - "Timasheff, S.N. 2002. Protein hydration, thermodynamic binding, and preferential hydration. *Biochemistry* 41:13473."
  - "Privalov, P.L. 1979. Stability of proteins: small globular proteins. *Adv Protein Chem* 33:167. (Van't Hoff enthalpy range for globular proteins.)"
  - "UniProt Q00511 — Uricase, *Aspergillus flavus*, reviewed PE=1, ECO:0000269|PubMed:16478683 confirming homotetramer subunit structure. No native DISULFID features."
  - "AlphaFold Protein Structure Database (EMBL-EBI) — AF-Q00511-F1-model_v6."
---

# Uricase Thermal/pH Stability in Shio-Koji — Computational Analysis

**Question:** Will the *A. flavus* uricase homotetramer (Q00511) maintain integrity and meaningful activity after 7–14 days in a shio-koji ferment (15–20% NaCl, pH 4.5–6.0, ~22°C)? The protease axis was covered by comp-001 (LOW risk); this analysis covers the thermal + pH + tetramer-integrity axes.

**Verdict: MODERATE risk (YELLOW).** Predicted activity retention at reference shio-koji conditions (17.5% NaCl, pH 5.25, 22°C, 14 days) is **64%** (uncertainty band 0.2%–100%). Temperature is the dominant driver — the WT enzyme has a measured Tm of only 27°C, placing the ferment temperature just 5°C below the cooperative-unfolding midpoint. Kinetic refolding protection at sub-Tm conditions (modeled as f_u² scaling in a Lumry-Eyring two-state framework) is what keeps WT viable; without it, predicted retention would be near-zero. Wet-lab confirmation ([`validation-experiments.md` §1.10](./validation-experiments.md)) is necessary to validate the f_u² scaling assumption and to disambiguate the wide uncertainty band.

**Reproducible artifact:** [`experiments/comp-002-uricase-shio-koji-thermal-stability/`](../experiments/comp-002-uricase-shio-koji-thermal-stability/) — script, inputs, and full outputs committed to the repo.

---

## Why this matters

comp-001 established that the protease axis is structurally LOW risk for uricase in shio-koji — all cleavage recognition sites are buried in well-folded regions, and the dominant koji protease (ALP) is salt-suppressed. The remaining feasibility question for the shio-koji uricase-delivery format was the *thermal + pH + tetramer-integrity* axis: even if proteases don't cleave the protein, does the enzyme retain native tetrameric structure and activity over 7–14 days in the ferment?

The answer matters because uricase is a homotetramer with a per-subunit active site that requires the dimer interface for catalytic competence — dissociation of the tetramer means loss of activity even if the monomer fold is preserved. The native enzyme has **no engineered disulfide bonds** (UniProt Q00511 contains zero DISULFID features; this was verified in the comp-002 provenance pass). Tetramer integrity is purely non-covalent — hydrophobic packing, hydrogen bonds, and a small number of interfacial salt bridges.

A primary literature search surfaced a load-bearing biophysical anchor that comp-001 did not have access to: WT *A. flavus* uricase has a measured Tm of only **27°C** (Imani & Shahmohamadnejad 2017, [DOI:10.1007/s13205-017-0841-3](https://doi.org/10.1007/s13205-017-0841-3)). Shio-koji fermentation at ~22°C sits 5°C below this transition midpoint. That is a tighter margin than is typical for industrial enzymes and motivated the moderate-not-low verdict.

---

## Method summary

The composite biophysical scoring framework combines four orthogonal stability axes into a per-condition retention prediction, with explicit ±sigma uncertainty bracketing and a 240-cell sensitivity sweep over NaCl, temperature, pH, and duration.

**Stdlib-only constraint.** The original brief proposed GROMACS / OpenMM MD simulation (50–100 ns trajectory of the tetramer in 15% NaCl at 295K) or Rosetta ΔΔG. This run honored the comp-001-established stdlib-only constraint and replaced the MD/Rosetta path with a composite biophysical-prior framework. MD remains the rigorous next step if §1.10 wet-lab results deviate from these predictions.

### Axis 1 — Thermal kinetics (Lumry-Eyring two-state)

The empirical anchor is k_obs(40°C) ≈ 0.018 min⁻¹ (38-min half-life from Imani & Shahmohamadnejad 2017, with independent cross-check from Rezaeian Marjani et al. 2020 at 38.5 min). At 40°C the protein is overwhelmingly unfolded (40°C is 13°C above Tm = 27°C), so k_obs at 40°C reports the rate of irreversible loss from the unfolded ensemble.

Below Tm, the native state dominates and irreversible loss requires a transient unfolding excursion that loses the kinetic refolding race. We use the standard Lumry-Eyring scheme:

```
N ⇌ U → I       (N native, U unfolded, I irreversibly inactivated)
```

Population fraction unfolded from van't Hoff: f_u(T) = 1 / (1 + exp(-ΔH_vH/R × (1/Tm − 1/T))), with ΔH_vH = 400 kJ/mol (typical 35-kDa globular protein; Privalov 1979).

In the supra-Tm regime (T ≥ Tm): k_obs(T) = k_irr × f_u(T)
In the sub-Tm regime (T < Tm): k_obs(T) = k_irr × f_u(T)² × residual_Arrhenius

The f_u² scaling captures both reduced unfolded population AND kinetic refolding protection (refolding outcompetes aggregation when native is energetically favored). This is a standard heuristic for explaining sub-Tm storage stability of proteins with nominally low Tm. The residual Arrhenius factor (Ea = 50 kJ/mol) captures the temperature dependence of the irreversible-loss chemistry itself (deamidation, oxidation, aggregation), separate from the folding equilibrium.

At reference conditions (22°C, 14 days): f_u = 6.2%, k_eff = 2.2×10⁻⁵ min⁻¹, half-life ≈ 22 days → thermal retention 64.4%.

### Axis 2 — pH-dependent interface integrity (Henderson-Hasselbalch)

Three key acidic/basic salt-bridge pairs at the published *A. flavus* uricase tetramer interface (from PDB 1R56 / Retailleau et al. 2004 and Colloc'h et al. 1997). At each ferment pH, the fraction of acidic partner in the charged (deprotonated, ion-pair-active) form is computed via Henderson-Hasselbalch with pKa estimates of 4.0–4.4 (typical surface-exposed Asp/Glu).

Mean interface integrity at pH 5.25 = 91.4%; at pH 4.5 = 88%; at pH 6.0 = 96%.

### Axis 3 — Tetramer interface pLDDT integrity (AlphaFold)

Per-residue pLDDT from the AlphaFold v6 model, restricted to published tetramer interface residue ranges (tight dimer A-B: residues 11-13, 53-65, 161-179, 184-208, 250-270; tetramer interface A-C/A-D: 73-80, 123-135, 222-232, 275-290). Composite weighted mean (3:1 tight-dimer:tetramer): 97.3 / 100. All interface residues are at pLDDT > 80; 99% are at > 90. Interface structural confidence is extraordinarily high — the AlphaFold model places no flexible loops at the interface.

Interface integrity score (0–1 scale, linear ramp from pLDDT 70 to 90): **1.0** (saturated).

### Axis 4 — Salt (Hofmeister) factor

NaCl at moderate-to-high concentration is a kosmotrope on the Hofmeister series. Preferential hydration of the native state contributes ×1.15 stabilization (Timasheff 2002); ion-pair screening at the interface contributes ×0.92 (counterbalancing). Net at 17.5% NaCl: **×1.058** — mild net stabilization, opposite direction from the protease-activity effect in comp-001.

### Composite

```
retention = thermal × (0.30 + 0.70 × ph_intact × iface_intact) × salt
```

The 0.30 floor reflects the "monomer-level" residual activity if the tetramer dissociates — a fold-intact monomer retains some catalytic competence transiently. The 0.70 coefficient is the tetramer-mediated stabilization that depends on both pH integrity (axis 2) and interface integrity (axis 3).

### Uncertainty bracketing

Worst-case / best-case bracket perturbing all four dominant uncertainties simultaneously: Tm ±2°C (25–29°C), ΔH_vH ±100 kJ/mol (300–500), interface pKa ±0.5 pH units, salt-factor ±0.05. Uncertainty band: 0.2%–100% at the reference condition. The wide band reflects real biophysical uncertainty — Tm and ΔH_vH are not measured for Q00511 with the precision needed to tighten the prediction.

---

## Key results

### Sensitivity sweep — temperature is the dominant driver

Sweep across the 5×4×4×3 grid (NaCl × T × pH × duration = 240 conditions). Driver sensitivity:

| Parameter | Range scanned | Retention range | Spread (pp) |
|---|---|---|---|
| Temperature | 22–32°C | 0%–61% | **61** |
| Duration | 7–30 days | 37%–76% | 39 |
| pH | 4.5–6.0 | 52%–67% | 15 |
| NaCl | 5%–20% | 59%–62% | **3** |

**Temperature dominates.** A warm-kitchen ferment at 28-30°C (above the WT Tm of 27°C) destroys retention. The shio-koji format's reliance on room-temperature fermentation is the load-bearing condition for WT uricase viability. Geographic and seasonal effects: a 24°C summer kitchen vs. an 18°C winter kitchen makes a measurable difference in the predicted retention.

**Salt is essentially neutral.** Unlike the protease analysis (where 15-20% NaCl was strongly protective), the thermal-stability axis has NaCl as a mild kosmotrope — net positive but only ×1.058. The Hofmeister effect is small at the relevant concentrations for this protein.

### Failure-mode ranking at reference conditions

| Failure mode | Loss contribution | Notes |
|---|---|---|
| Thermal kinetics (Lumry-Eyring two-state) | 36% | Dominant. f_u = 6.2% at 22°C; k_eff_22 ≈ 2×10⁻⁵ min⁻¹; 14-day exposure depletes 36% via the irreversible-loss channel. |
| pH-dependent interface ion-pair disruption | 9% | Modest. pH 5.25 is well above the pKa of interfacial Asp/Glu (~4.0-4.4) — most salt bridges remain intact. |
| Salt destabilization (net) | 0% | NaCl is net stabilizing at 17.5% (×1.058). |
| Structural interface flexibility (pLDDT proxy) | 0% | AlphaFold places all interface residues at pLDDT > 80; structural confidence is saturated. |

### Worst-case and best-case conditions

The lowest-retention region of the sweep (T=25°C, pH=4.5, 30 days) gives ~0% retention — driven by the temperature edge crossing into the cooperative-unfolding regime combined with maximum pH stress and longest exposure.

The highest-retention region (T=22°C, pH=6.0, 7 days, any NaCl%) gives ~84% retention — short ferment, upper-edge pH (above interfacial pKa), and ferment temperature comfortably sub-Tm.

The practical takeaway: **temperature control of the ferment matters far more than the NaCl level or pH within the shio-koji range**. Brewing at 18-20°C (refrigerator-adjacent kitchen counter or wine-fridge) instead of 22-25°C (standard kitchen counter) is the highest-impact retrofit available without protein engineering.

---

## Multilingual literature audit

Per the global-multilingual default. Sources checked:

- **J-STAGE / J-GLOBAL (Japanese):** The primary Japanese contribution to koji enzymology in this question domain is Tominaga & Tsujisaka 1976 and Ikeda et al. 1975 (cited via comp-001). No additional Japanese-language primary thermal-stability data on heterologous proteins in shio-koji conditions identified. Ito & Matsuyama 2021 (*J Fungi*, PMC8399179) is a Japanese-authored English-language review covering koji-enzyme salt-tolerance — same biophysical regime.
- **CNKI / WanFang (Chinese):** No Chinese-language primary stability data on *A. flavus* Q00511 identified. The accessible literature is dominated by Iranian groups (Imani, Rezaeian Marjani) and crystallography groups (Retailleau et al. ESRF; Colloc'h et al. France) publishing in English.

For this specific question, the primary literature is predominantly English-language. The multilingual search was performed and the result is empirical, not a "language barrier" excuse.

---

## Limitations (full list)

Stated explicitly per the comp-001 design pattern — some incorporated into the uncertainty band, others noted for transparency.

- **Stdlib-only constraint.** No MD simulation (no GROMACS/OpenMM trajectory). No Rosetta ΔΔG. No PDB-coordinate parsing (interface footprint is from published structural analyses, not extracted in this run). MD is the rigorous follow-up if §1.10 wet-lab data deviates.

- **Tm = 27°C is from a single primary source** (Imani & Shahmohamadnejad 2017). The result is biologically plausible (fungal cytosolic enzyme, no PTMs, no native disulfides — low Tm consistent with these features) but a second independent DSF measurement on Q00511 would harden this load-bearing anchor. Uncertainty bracket: Tm ± 2°C → retention band widens substantially. If the true Tm is ~32°C (modestly higher than measured) the picture shifts toward GREEN; if the true Tm is ~25°C the picture shifts toward RED.

- **ΔH_vH = 400 kJ/mol is a generic biophysical prior**, not directly measured for Q00511. Literature range for globular proteins is 300-600 kJ/mol (Privalov 1979; Robertson & Murphy 1997). Uncertainty bracket uses 300-500 → contributes most of the model uncertainty.

- **Lumry-Eyring f_u² sub-Tm scaling is a heuristic.** The exact power of f_u depends on the ratio of refolding to aggregation rate constants, which are protein-specific and not measured here. f_u² is a conservative middle ground; the true exponent could be anywhere from 1 (no refolding protection) to 3+ (strong protection). Multi-temperature inactivation kinetics at sub-Tm temperatures (e.g., 22°C, 25°C, 27°C, 30°C, 33°C in buffer) would empirically determine this — this is the highest-value follow-up experiment if §1.10 results are ambiguous.

- **Interface salt-bridge pKa values are estimated, not measured.** Three salt-bridge pairs were inferred from the published interface footprint and the sequence pKa pattern; per-residue pKa shift (from local electrostatic environment) was approximated as ±0.5 in the uncertainty band. PROPKA or H++ on PDB 1R56 coordinates would tighten these by ~0.2 pH units.

- **Activity ≠ stability.** The pH-activity curve values measure catalytic competence at the assay pH, not tetramer integrity during storage. The thermal/pH retention prediction is for *post-ferment residual activity at assay pH*, which after return to assay pH 7.5–8.5 recovers catalytic activity if the tetramer survived storage at low pH.

- **Tetramer dissociation not directly modeled.** The pH axis approximates interface fragility via salt-bridge integrity, but actual dimer-to-monomer dissociation requires AUC or SEC measurements at the ferment pH — not done here. If the tetramer dissociates and monomers reassemble on dilution to assay pH, the activity readout would not detect transient dissociation.

- **Single ferment-pH endpoint modeled.** Real shio-koji ferments may drift in pH over 7-14 days as residual koji enzymes process the matrix. pH drift toward 4.0-4.5 over the ferment would worsen the verdict; pH stable at 5.5-6.0 would improve it. §1.10 should measure pH over time as part of data collection.

- **Interface salt-bridge pairs inferred from sequence + interface footprint**, not directly coordinate-extracted. The three salt-bridge pairs in `inputs/tetramer_interface_residues.json` are reasonable assignments given the interface footprint and the pKa pattern, but a proper PDB-coordinate analysis (Biopython on PDB 1R56) would either confirm them or substitute different pairs.

- **No protective-osmolyte effect modeled.** Lactose was shown to shift Tm from 27°C to 37°C (Imani & Shahmohamadnejad 2017). Shio-koji contains residual carbohydrates (rice-derived oligosaccharides, glucose, maltose) from koji metabolism that may exert similar osmotic-protection effects. If even 1/3 of the lactose Tm-shift effect carries over to shio-koji's native carbohydrate matrix, the operative Tm in the ferment matrix could be 3-5°C higher than the buffer-measured 27°C — moving the verdict closer to GREEN. This is an additional protective factor the model does NOT capture.

---

## Comparison to comp-001 (protease axis)

| Axis | comp-001 verdict | comp-002 verdict | Reframe |
|---|---|---|---|
| Protease degradation | LOW (provisional) | n/a | comp-001 |
| Thermal/pH/tetramer integrity | n/a | MODERATE | comp-002 |
| Combined | — | **MODERATE-overall** | Protease is solved; thermal is the residual risk |

The combined comp-001 + comp-002 picture: proteases are not the load-bearing failure mode for uricase in shio-koji; **thermal cooperative unfolding is**. The single highest-value engineering intervention available is the disulfide-engineered thermal-stability boost (Ala6Cys or Ser282Cys; Rezaeian Marjani 2020) — measured effects: optimum-activity temperature increased by 10°C, thermal half-life increased ~3.6× (38.5 → 138 min at thermal stress for Ala6Cys, → 115 min for Ser282Cys). The Tm effect specifically is correlated with but not identical to the optimum-activity-temperature effect; a DSF measurement on the disulfide mutants would tighten the predicted Tm-gap improvement. Best estimate: the mutants would move the operative thermal stability range significantly into a comfortable margin for shio-koji conditions.

---

## Impact on experimental priorities

**For §1.10 (Uricase + lactoferrin stability in shio-koji):** comp-001 reframed this as a confirmation experiment (LOW protease risk); comp-002 reverts it partially to a **YELLOW gate** specifically for thermal/tetramer integrity. The §1.10 experimental design should be extended:

1. **(EXISTING)** SDS-PAGE band intensity for the 34-kDa monomer at day 0/7/14 — proteolysis check
2. **(NEW — motivated by comp-002)** Native-PAGE for the ~135-kDa tetramer band at day 0/7/14 — tests tetramer integrity directly. The most sensitive single readout for the comp-002 hypothesis.
3. **(NEW — motivated by comp-002)** Specific activity per total protein at each timepoint — combines fold + tetramer assembly into one functional readout
4. **(NEW — motivated by comp-002)** pH measurement of the ferment matrix over the 14-day window — lactic acid from residual koji metabolism may push pH below 5.0, the lower edge of the modeled range
5. **(NEW — motivated by comp-002, if §1.10 shows tetramer loss)** Replicate the ferment at 18°C vs. 22°C vs. 25°C in parallel — directly tests the temperature-driver hypothesis from this analysis's sensitivity sweep

**For §1.16 (OPT-1 disulfide-engineered uricase vs. WT — GI survival head-to-head):** this analysis reinforces the strategic value of the OPT-1 variant. The thermal-stability boost from disulfide engineering (10°C in optimum-activity temperature, ~3.6× in thermal half-life; Rezaeian Marjani 2020) is the cleanest single intervention to address the comp-002 Tm-gap risk. If §1.10 confirms the thermal axis is the limiting failure mode for WT, §1.16 becomes higher-priority — it directly addresses the chokepoint identified here. **Recommendation: do not pre-commit gene-synthesis budget to the OPT-1 variants until §1.10 distinguishes between (a) WT works fine (thermal failure mode does not materialize → OPT-1 is not load-bearing for shio-koji format) and (b) WT fails on tetramer integrity (thermal failure mode confirmed → OPT-1 is the resolution).**

---

## Cross-references

- [`validation-experiments.md` §1.10](./validation-experiments.md) — wet-lab uricase + lactoferrin stability in shio-koji ferment
- [`validation-experiments.md` §1.16](./validation-experiments.md) — OPT-1 disulfide-engineered uricase vs. WT GI survival head-to-head
- [`computational-experiments.md`](./computational-experiments.md) — tracking index for all computational analyses
- [`uricase-protease-stability-computational.md`](./uricase-protease-stability-computational.md) — sister analysis (protease axis, comp-001)
- [`uricase.md`](./uricase.md) — uricase platform context
- [`uricase-variant-selection.md`](./uricase-variant-selection.md) — disulfide engineering precedents (Rezaeian Marjani 2020)
- [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) — shio-koji delivery format constraints
- [`koji-home-fermentation.md`](./koji-home-fermentation.md) — home-fermentation conditions
- [`aspergillus-oryzae.md`](./aspergillus-oryzae.md) — koji organism context
