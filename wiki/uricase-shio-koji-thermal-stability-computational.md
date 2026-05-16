---
title: "Uricase Thermal/pH Stability in Shio-Koji — Computational Analysis (comp-002)"
date: 2026-05-16
tags: [uricase, shio-koji, thermal-stability, tetramer, computational]
related:
  - computational-experiments.md
  - validation-experiments.md
  - uricase.md
  - uricase-variant-selection.md
  - uricase-protease-stability-computational.md
  - engineered-koji-protocol.md
sources:
  - "Imani & Shahmohamadnejad 2017, 3 Biotech 7:201, DOI:10.1007/s13205-017-0841-3, PMID:28667645 — WT *A. flavus* uricase Tm = 27°C, t½ = 38 min at 40°C"
  - "Rezaeian Marjani et al. 2020, Iran J Biotechnol 18:e2662, DOI:10.30498/IJB.2020.2662, PMID:33850949 — disulfide-engineered Tm-boost, independent t½ cross-check"
  - "Retailleau et al. 2004, Acta Cryst D60:453, PDB 1R56 — tetramer interface footprint"
  - "UniProt Q00511 — homotetramer (ECO:0000269|PubMed:16478683); zero native DISULFID features"
---

# Uricase Thermal/pH Stability in Shio-Koji — Computational Analysis (comp-002)

**Question:** Will the *A. flavus* uricase homotetramer maintain integrity and activity under shio-koji conditions (15–20% NaCl, pH 4.5–6.0, ~22°C, 7–14 days)? Sister to comp-001 (protease axis, LOW); this covers the thermal + pH + tetramer-integrity axes.

**Verdict: MODERATE (YELLOW).** Predicted activity retention at reference shio-koji (17.5% NaCl, pH 5.25, 22°C, 14 days) = **64%** (band 0.2–100%). The wide band reflects sensitivity to Tm and ΔH_vH — biophysical anchors not yet measured precisely for Q00511.

## Key findings

- **Temperature is the dominant driver** (sensitivity sweep spread 61 pp over 22–32°C, vs. 15 pp for pH and 3 pp for NaCl). A warm-kitchen ferment at 28–30°C (above Tm = 27°C) destroys retention.
- **Tm gap is narrow (5°C).** WT Tm = 27°C (Imani & Shahmohamadnejad 2017); shio-koji at 22°C sits 5°C below the cooperative-unfolding midpoint. Kinetic refolding protection (modeled as f_u² in the Lumry-Eyring sub-Tm regime) is what keeps WT viable — without it, predicted retention is near-zero.
- **Salt is essentially neutral** (×1.058 net stabilization at 17.5% NaCl). Unlike the protease axis where NaCl was strongly protective, the thermal axis treats it as a mild Hofmeister kosmotrope.
- **Interface pH integrity is intact at shio-koji pH** (91% at pH 5.25, 96% at pH 6.0; weakens to 88% at pH 4.5). Three modeled interface salt-bridge pairs with pKa ~4.0–4.4.
- **Tetramer interface pLDDT is exceptional** (mean 97.3, all residues > 80) — structural confidence is not the limiting factor.
- **Disulfide-engineered variants** (Ala6Cys, Ser282Cys; Rezaeian Marjani 2020) raise T_optimum by 10°C and thermal half-life ~3.6× (38.5 → 138 min at thermal stress) → would substantially relax the Tm-gap constraint. (T_opt boost is correlated with but not identical to Tm boost; magnitude on Tm specifically needs a DSF measurement on the mutants.) Single highest-value engineering intervention if WT fails the §1.10 thermal axis.

## Cross-references

- **Wet-lab informed:** [`validation-experiments.md` §1.10](./validation-experiments.md) (uricase + lactoferrin shio-koji stability) — comp-002 adds three §1.10 readouts: native-PAGE for tetramer band, specific activity per total protein, ferment-pH-over-time tracking. [§1.16](./validation-experiments.md) (OPT-1 disulfide variant) — strategic value reinforced; recommend not pre-committing gene-synthesis budget until §1.10 confirms thermal is the limiting failure mode for WT.
- **Sister analysis (protease):** [`uricase-protease-stability-computational.md`](./uricase-protease-stability-computational.md) (comp-001, LOW). Combined picture: proteases are not the load-bearing failure mode; **thermal cooperative unfolding is.**
- **Tracking index:** [`computational-experiments.md`](./computational-experiments.md)
- **Platform context:** [`uricase.md`](./uricase.md), [`uricase-variant-selection.md`](./uricase-variant-selection.md), [`engineered-koji-protocol.md`](./engineered-koji-protocol.md)

> **Frozen long-form analysis** — method details, limitations (10+ items), failure-mode ranking, multilingual literature audit, comparison to comp-001: [`./etc/experiments/comp-002-uricase-shio-koji-thermal-stability/wiki-archive.md`](./etc/experiments/comp-002-uricase-shio-koji-thermal-stability/wiki-archive.md). Reproducible artifact: [`./etc/experiments/comp-002-uricase-shio-koji-thermal-stability/`](./etc/experiments/comp-002-uricase-shio-koji-thermal-stability/).
