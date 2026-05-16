---
title: "Dual-chassis EcN PDB + uricase additive SUA prediction (comp-031)"
date: 2026-05-16
tags: [comp-031, dual-chassis, ecn, purine-degrading-bacteria, cbt20, uricase, butyrate, abcg2, q141k, substrate-competition, in-silico]
related:
  - purine-degrading-bacteria.md
  - gut-lumen-sink.md
  - abcg2-modulators.md
  - chassis-pending-interventions.md
  - uricase-abcg2-genotype-stratification-computational.md
  - computational-experiments.md
sources:
  - "Li et al. 2025 (PMID 41070194) CBT2.0 anchor; Liu et al. 2023 (PMID 37541197) DOPDH kinetics; Basseville et al. 2012 (PMID 22472121) Q141K HDAC rescue; comp-019 substrate-limited regime"
---

# Dual-chassis EcN PDB + uricase additive SUA prediction (comp-031)

## Question
Does engineered EcN expressing the 2,8-dioxopurine PDB cluster (CBT2.0, Li 2025) co-administered with a PULSE-style luminal uricase deliver additive ΔSUA beyond either arm alone? Does PDB-derived butyrate compound the gut-lumen sink via PPARγ/HDAC ABCG2 modulation? See [`chassis-pending-interventions.md` §M1](./chassis-pending-interventions.md).

## Verdict
**YELLOW (provisional)** — combined > either arm but well below the naive sum. The two urate-consumption arms compete for scarce luminal urate substrate (per [comp-019](./uricase-abcg2-genotype-stratification-computational.md) substrate-limited regime); the PDB pathway adds an INDEPENDENT mechanism axis via butyrate → PPARγ ABCG2 induction (WT alleles) + butyrate → HDAC Q141K trafficking rescue. **Combined ΔSUA: −1.8 to −1.9 mg/dL** across genotypes (90% CI roughly −2.2 to −1.3). Additive bump over PDB-alone: ~−0.1 to −0.2 mg/dL, genotype-stratified (largest in Q141K-hom).

"Provisional" reflects: (a) DOPDH kinetic Km is mechanistic extrapolation from sister Mo-Se hydroxylases, (b) mouse-to-human translation 0.5× point-estimate (range 0.3–0.7), (c) in-vivo crypt butyrate concentration empirically open per [`purine-degrading-bacteria.md` §Concentration-gap](./purine-degrading-bacteria.md).

## Key results

| Genotype | Uricase alone | PDB alone (med, 90% CI) | Combined (med, 90% CI) |
|---|---|---|---|
| WT/WT male gout | −0.83 mg/dL | −1.74 (−2.18, −1.24) | **−1.87** (−2.28, −1.37) |
| Q141K het male gout | −0.66 mg/dL | −1.62 (−2.03, −1.15) | **−1.76** (−2.14, −1.30) |
| Q141K hom male gout | −0.49 mg/dL | −1.55 (−1.94, −1.10) | **−1.82** (−2.19, −1.37) |

Combined ΔSUA ~25–30% larger than PDB-alone (NOT 2–3× as naive addition predicts). Q141K rescue fraction ~0.43 (Basseville 2012 Hill activation at modeled crypt butyrate); rescue bump in Q141K-hom is the genotype-stratified differentiator that uricase alone cannot deliver.

## Compositional finding
The two arms **compete on urate consumption** (combined ≈ dominant + ~10% of minor; substrate-competition factor 0.06–0.14 per comp-019 capacity-vs-supply ratios) but **compose additively on the butyrate-mediated ABCG2 axis** (uricase produces no butyrate). Different mechanism, different math.

## Method summary
Literature-anchored kinetic + flux model, Python stdlib only, n=15000 Monte Carlo. Per-arm ΔSUA (uricase inherits comp-019; PDB anchored on Li 2025 with mouse-to-human attenuation + intact-kidney renal-compensation correction); substrate-competition (combined ≈ dominant + small residual capture); butyrate-mediated additive axis (PPARγ on WT alleles, Hill-function HDAC rescue on Q141K). Sensitivity over CBT2.0 colonization 10⁹–10¹¹ CFU/g, mouse-to-human 0.3–0.7, butyrate yield 0.3–0.7 mol/mol, crypt attenuation 0.05–0.5, colonic urate 50–500 μM. Full provenance + reproduction at [`../experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/`](../experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/).

## Limitations
DOPDH kinetic parameters mechanistic extrapolation from sister enzymes; CBT2.0 anchor single-paper Uox⁻/⁻ mouse; in-vivo crypt butyrate empirically open ([`validation-experiments.md §1.14`](./validation-experiments.md) butyrate dose-response is the wet-lab resolution); butyrate stoichiometry 0.5 mol/mol pathway-extrapolated; PPARγ WT-induction magnitude approximated; no human RCT of CBT2.0-class PDB; first-order steady-state (no circadian / food-effect / CKD-grade modeling).

## Impact on experimental priorities
**Reframes the M1 multi-chassis stack engineering question from "should we build it?" to "build it as TWO strains, not one dual-cassette."** Substrate-competition means a single dual-cassette EcN (PDB 8-gene cluster + uricase + selenium-cofactor coordination) gains ~nothing relative to two separate strains co-administered. The butyrate synergy operates from gut lumen on enterocyte, not at bacterial-cell scale — co-administration captures it. Avoids the regulatory and stability complexity of an 8-gene selenoprotein cluster + uricase coordinated in one chassis.

Does NOT change prioritization of either single arm — PULSE uricase remains independently valuable (~−0.7 mg/dL); PDB-EcN remains the higher-magnitude single intervention (~−1.6 mg/dL). The stack is YELLOW for additivity (modest but real) and a clear NO for single-chassis dual-cassette.

## Cross-references
- [comp-019 substrate-limited regime](./uricase-abcg2-genotype-stratification-computational.md)
- [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) — CBT2.0 anchor + concentration-gap framing
- [`abcg2-modulators.md` §Two distinct modulation modes](./abcg2-modulators.md) — PPARγ vs HDAC separation
- [`chassis-pending-interventions.md` §M1](./chassis-pending-interventions.md) — the engineering question this resolves
- Experiment folder: [`../experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/`](../experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/)
