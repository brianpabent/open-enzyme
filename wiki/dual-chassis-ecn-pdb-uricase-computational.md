---
title: "Dual-Chassis EcN PDB + Uricase Additivity — Invalidated Computational Prior (comp-031)"
date: 2026-05-16
updated: 2026-07-13
status: invalidated
tags: [comp-031, dual-chassis, ecn, purine-degrading-bacteria, cbt20, uricase, butyrate, invalidated]
related:
  - purine-degrading-bacteria.md
  - gut-lumen-sink.md
  - staged-purine-sink-mass-balance-computational.md
  - gut-lumen-uricase-physiologic-regime-computational.md
  - validation-experiments.md
  - computational-experiments.md
sources:
  - "Li et al. 2025 — PMID 41070194; PMCID PMC12507026"
  - "Liu et al. 2023 — PMID 37541197; PMCID PMC10421625"
  - "Basseville et al. 2012 — PMID 22472121; PMCID PMC4163836"
  - "comp-044 and comp-046 audit, 2026-07-13"
---

# Dual-Chassis EcN PDB + Uricase Additivity — Invalidated Prior (comp-031)

## Status

**INVALIDATED 2026-07-13.** The original ΔSUA, substrate-competition, CBT2.0-derived butyrate, Q141K rescue, and dual-chassis additivity results must not guide engineering or clinical decisions.

The frozen artifact remains at [comp-031](./etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/) for provenance and reproducibility of what was run—not because its result remains valid.

## Why the prior failed

1. **Inherited invalid UOX regime:** comp-031 hard-coded comp-019's 32–1,300× saturation finding. [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) shows that conclusion is not robust because comp-019 omitted its own substrate concentration, Km, and finite active window.
2. **Organism/product mismatch:** the CBT2.0 paper establishes urate-pathway products through pyruvate in engineered EcN; it does not establish butyrate production. A *C. sporogenes* butyrate-yield assumption was transferred into EcN without measurement.
3. **False Basseville attribution:** Basseville 2012 tested HDAC inhibitors including vorinostat-class compounds and valproate, not direct 1–5 mM butyrate rescue of Q141K in this system.
4. **Unmatched background:** the model added 0.8 mM background crypt butyrate to the combination arm. Most of the modeled rescue therefore came from a background term not matched across comparators.
5. **Compartment error:** UOX and PDB were modeled as well-mixed consumers even though oxidative UOX and anaerobic PDB are likely to occupy different longitudinal/radial gut niches.

## What remains scientifically open

- CBT2.0 may still lower urate through reductive purine degradation.
- A full-pathway PDB organism may produce butyrate and create a colonocyte-hypoxia persistence loop.
- UOX and PDB may be complementary when they access different spatial residual fluxes.
- None of those possibilities supplies a quantitative human ΔSUA prior yet.

## Replacement priors and experiments

- [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md): reopens the UOX dose/regime question.
- [comp-046](./staged-purine-sink-mass-balance-computational.md): separates dietary and endogenous ledgers and provides a conditional architecture boundary without summing efficacy.
- [Validation §1.34](./validation-experiments.md#134-isotope-resolved-dietary-precursor--uox--pdb-sequential-flux): isotope-resolved sequential flux.
- [Validation §1.37](./validation-experiments.md#137-cbt20-carbon-fate-and-pdb-self-niche-test): CBT2.0 carbon fate and actual butyrate measurement.

## Current decision

Do not build a dual cassette or claim PDB-derived ABCG2/Q141K synergy. First measure CBT2.0 products and the spatial residual-flux terms. Separate strains remain an experimental option, not a computationally validated recommendation.
