# comp-002 — Uricase Shio-Koji Thermal/pH Stability

**Question:** Will the *A. flavus* uricase tetramer (Q00511) maintain integrity and activity under shio-koji conditions (15–20% NaCl, pH 4.5–6.0, ~22°C, 7–14 days)? comp-001 covered the *protease* axis; comp-002 covers the *thermal + pH + tetramer-integrity* axis.

**Short answer:** Computational analysis predicts **MODERATE risk (YELLOW)**. Predicted activity retention at reference conditions is 64% (uncertainty band 0.2–100%). Temperature is the dominant driver — WT *A. flavus* uricase has a measured Tm of only 27°C (Imani & Shahmohamadnejad 2017, PMID:28667645), placing shio-koji at 22°C just 5°C below the cooperative unfolding midpoint. Kinetic refolding protection at sub-Tm conditions is what keeps WT viable; disulfide-engineered variants raising T_optimum by 10°C (Rezaeian Marjani 2020) are the highest-value protein-engineering intervention if WT fails §1.10.

**Verdict:** §1.10 wet-lab uricase stability experiment is now a **YELLOW gate** rather than the GREEN confirmation suggested by comp-001's protease-only analysis. The combined comp-001 + comp-002 picture: protease risk is LOW, thermal risk is MODERATE, the dominant uncertainty is whether kinetic refolding protection (modeled as f_u² scaling) accurately reflects the true sub-Tm behavior of this enzyme. Multi-temperature DSF on Q00511 in shio-koji-mimicking buffer is the single highest-value follow-up.

## How to reproduce

```bash
python3 analyze.py
# Outputs: outputs/stability_predictions.json, outputs/summary.md
```

Requirements: Python 3.8+, stdlib only (json, math, pathlib). No packages to install.

## Re-running with updated data

- **New Tm measurement:** Edit `inputs/biophysical_priors.json` → `thermal_kinetics.wt_Tm_celsius` and the `wt_Tm_source` field. Re-run.
- **Updated AlphaFold model:** Replace `inputs/alphafold_Q00511_plddt.json` and update `inputs/provenance.md`. Re-run.
- **Refined interface footprint (e.g., from PDB-coordinate analysis):** Edit `inputs/tetramer_interface_residues.json` and update `_method_note`. Re-run.
- **Different protein:** Replace FASTA + pLDDT + interface JSON with inputs for the new target. The analysis script is generic across uricase variants.

## File index

```
inputs/
  Q00511.fasta                          UniProt sequence (copied from comp-001/inputs, fetched 2026-05-05)
  alphafold_Q00511_plddt.json           Per-residue pLDDT from AlphaFold v6 PDB (copied from comp-001/inputs)
  tetramer_interface_residues.json      Interface residue footprint + key salt-bridge pairs, from published PDB 1R56 analyses
  biophysical_priors.json               Tm, half-life, pH-activity curve, salt-stability factor, sensitivity-sweep grid
  provenance.md                         Data sources, fetch dates, version notes, multilingual-search audit
outputs/
  stability_predictions.json            Full machine-readable results (reference prediction + sensitivity sweep)
  summary.md                            Human-readable findings — this is the artifact cited in the wiki
analyze.py                              Analysis script (stdlib only; Lumry-Eyring two-state thermal model + Henderson-Hasselbalch pH + Hofmeister salt + pLDDT interface integrity)
README.md                               This file
wiki-archive.md                         Long-form narrative (≤archived from sweep daemon synthesis)
```

## Method summary

Composite biophysical scoring framework with four orthogonal axes:

1. **Thermal kinetics — Lumry-Eyring two-state model.** Empirical anchor: k_obs(40°C) = ln(2)/38 min from Imani & Shahmohamadnejad 2017. Native-state ⇌ unfolded-state equilibrium via van't Hoff (Tm = 27°C, ΔH_vH = 400 kJ/mol). Sub-Tm regime applies f_u² kinetic-refolding-protection scaling.

2. **pH-dependent interface integrity — Henderson-Hasselbalch.** Three key acidic/basic salt-bridge pairs at the published tetramer interface; deprotonation fraction at the ferment pH gives the integrity score.

3. **Tetramer interface pLDDT integrity.** AlphaFold v6 confidence at published interface residues (tight dimer + tetramer interfaces, weighted 3:1 by buried-surface contribution).

4. **Salt (Hofmeister) factor.** Net kosmotrope effect at 17.5% NaCl: preferential hydration of native state (×1.15) modulated by ion-pair screening at interface (×0.92) → net ×1.058 stabilization.

Composite: `retention = thermal × (a + b × ph_intact × iface_intact) × salt`, with a = 0.30 (monomer-level floor) and b = 0.70 (tetramer-mediated stabilization). Uncertainty band: worst-case / best-case bracket perturbing Tm ±2°C, ΔH_vH ±100 kJ/mol, pKa ±0.5, salt-factor ±0.05.

## Limitations (high-level — full list in `outputs/summary.md` and `wiki-archive.md`)

- Stdlib only — no MD simulation, no Rosetta ΔΔG, no PDB-coordinate extraction. Interface footprint is from published analyses, not extracted in this run. MD remains the rigorous next step.
- Tm = 27°C from a single primary source (Imani & Shahmohamadnejad 2017). A second independent DSF measurement on Q00511 would harden the load-bearing anchor.
- Lumry-Eyring f_u² sub-Tm scaling is a heuristic; the true refolding-vs-aggregation rate ratio could shift retention significantly higher or lower.
- Tetramer dissociation is approximated via interface salt-bridge integrity, not directly modeled. AUC or SEC at ferment pH would confirm.

## Wiki links

- Interpretive page: [`wiki/uricase-shio-koji-thermal-stability-computational.md`](../../wiki/uricase-shio-koji-thermal-stability-computational.md)
- Frozen long-form analysis: [`wiki-archive.md`](./wiki-archive.md)
- Tracking index: [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md)
- Wet-lab experiment this informs: [`wiki/validation-experiments.md` §1.10](../../wiki/validation-experiments.md) and §1.16
- Sister analysis (protease axis): [`experiments/comp-001-uricase-shio-koji-protease-stability/`](../comp-001-uricase-shio-koji-protease-stability/) and [`wiki/uricase-protease-stability-computational.md`](../../wiki/uricase-protease-stability-computational.md)
- Platform context: [`wiki/uricase.md`](../../wiki/uricase.md), [`wiki/engineered-koji-protocol.md`](../../wiki/engineered-koji-protocol.md), [`wiki/koji-home-fermentation.md`](../../wiki/koji-home-fermentation.md)
