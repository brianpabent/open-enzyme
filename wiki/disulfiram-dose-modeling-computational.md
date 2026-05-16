---
title: "Disulfiram Dose Modeling — Computational Analysis (comp-027)"
date: 2026-05-16
tags:
  - disulfiram
  - dose-modeling
  - GSDMD
  - NLRP3
  - compounding-pharmacy
  - 503a
  - repurposing-surface
  - computational
related:
  - computational-experiments.md
  - disulfiram.md
  - compounding-pharmacy-track.md
  - nlrp3-exploit-map.md
  - chassis-pending-interventions.md
sources:
  - "Hu et al. 2020 — Nat Immunol — PMC7316630 — GSDMD IC50"
  - "Xu, Pickard, Núñez 2024 — Cell Rep — PMC11398858 — NLRP3 palmitoylation"
  - "Johansson & Stankiewicz 1989 — PMID 2551696 — Me-DTC PK"
  - "Yourick & Faiman 1989 — PMID 2537080 — DER threshold"
  - "Lee et al. 2018 — PMC6379104 — population PK at 500-2000 mg"
  - "Asiri et al. 2025 — PMC12114764 — rat MSU-gout + DSF/ALP combination"
  - "Palatty & Saldanha 2011 — PMC3056183 — 125 mg/d clinical use"
---

# Disulfiram Dose Modeling — Computational Analysis (comp-027)

## Question
Is there a sub-AUD oral disulfiram dose window where plasma DSF engages GSDMD (CP6b pyroptotic-exit block) at therapeutically meaningful levels while plasma Me-DTC stays below the ALDH-inhibition threshold that drives the disulfiram-ethanol reaction (DER)?

## Verdict
**YELLOW-leaning-GREEN — narrow sub-AUD window exists at 75-125 mg/day, centered on 100 mg/day.** At 100 mg/d, predicted parent DSF Cmax ~0.4 μM gives 57% GSDMD blockade while plasma Me-DTC ~70 nM gives 40% ALDH inhibition — right at the Faiman DER hypotension threshold. Below 50 mg/d, GSDMD blockade drops below 40%; above 125 mg/d, ALDH inhibition crosses the DER threshold. The NLRP3-palmitoylation pathway (Xu 2024, 10 μM EC50) is NOT engaged at any sub-AUD dose — sub-AUD DSF is a **selective GSDMD inhibitor**, not a pan-NLRP3 inhibitor.

## Why this matters
The [compounding-pharmacy track](./compounding-pharmacy-track.md) flagged disulfiram as the highest-priority 503A repurposing candidate, but the dose question was unresolved. Without a defensible sub-AUD dose, the 503A pathway can't open — a pharmacy can't compound 250 mg AUD doses for an off-label gout indication. comp-027 closes that question with a specific dose recommendation (100 mg/d IR for titration, 100 mg/d ER lipid-matrix for chronic maintenance) that a 503A pharmacy partner can quote on.

## Method summary
Empirical dose-response model anchored to canonical PK and primary-source IC50 data. Parent DSF Cmax = 1.0 μM at 250 mg PO (clinical literature, consistent with Lee 2018 UPLC-MS/MS); Me-DTC peak = 278 nM at 400 mg (Johansson 1989); linear scaling at sub-AUD doses; CYP-saturation correction above 1000 mg. **GSDMD blockade**: Hill (n=1) on parent DSF; conservative anchor 0.30 μM (Hu 2020 cell-free), optimistic anchor 0.02 μM (cellular preincub, covalent-aware). **NLRP3 palmitoylation**: Hill on parent DSF, EC50 10 μM (Xu 2024). **ALDH inhibition**: Hill on Me-DTC, EC50 104 nM, back-calibrated to Faiman 1989's 40%-ALDH / 110 μM-acetaldehyde DER hypotension threshold. **Verdict**: GREEN ≥50% GSDMD + ≤40% ALDH; YELLOW ≥30% + ≤50%; RED otherwise.

## Key results
Full per-dose table at [`experiments/comp-027-disulfiram-dose-modeling/outputs/summary.md`](../experiments/comp-027-disulfiram-dose-modeling/outputs/summary.md). Headline:

| Dose (mg/d) | DSF Cmax (μM) | Me-DTC (nM) | GSDMD block | ALDH inhib. | Verdict |
|---|---|---|---|---|---|
| 50 | 0.20 | 35 | 40% | 25% | YELLOW |
| **100** | **0.40** | **70** | **57%** | **40%** | **GREEN** |
| 125 | 0.50 | 87 | 62% | 45% | YELLOW |
| 250 (AUD) | 1.00 | 174 | 77% | 62% | RED (DER) |

Two independent layers of the dose-window thesis: (1) **PD separation** — GSDMD (Hu 2020, 0.02-0.5 μM) vs NLRP3 palmitoylation (Xu 2024, 10-30 μM) differ by 1-2 orders of magnitude; sub-AUD selectively engages GSDMD. (2) **PK separation** — parent DSF and Me-DTC scale linearly with dose but with different absolute EC50s; ~100 mg/d satisfies both bounds simultaneously.

## Limitations
- PK uses empirical Cmax anchor (250 mg → 1 μM parent DSF), not fitted compartmental model; ±150% bounds. Lee 2018's fitted Vd = 1.3 L is a fitting-compartment artifact and was deliberately not used.
- Cmax-based GSDMD readout is conservative for a COVALENT inhibitor; multi-day QD cumulative engagement should be higher. Cellular-preincub anchor partially corrects.
- Asiri 2025 rat gout efficacy at 50 mg/kg (≈480 mg HED) doesn't validate or refute the sub-AUD window — only confirms AUD-dose works. The dose-response question Asiri explicitly listed as their primary limitation is what comp-027 addresses.
- DER threshold transfers cleanly from Faiman 1989 only if Me-DTC remains the dominant ALDH-inhibition driver at low doses; CYP saturation could shift metabolite ratios.
- No multilingual primary sources surfaced; translation cross-check not triggered.

## Impact on experimental priorities
This is a computational dose-finding prior, not a wet-lab gate. It reframes [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) §Phase 2 follow-up #6 from "open question" to "answered with 100 mg/d ± formulation-tunable bounds." The wet-lab confirmation question becomes "does the predicted 75-125 mg/d window produce the predicted plasma concentrations + reduce gout-flare incidence over 3-6 month chronic dosing in N=10-20 patients?" — for a 503A-prescribing physician partner, not a feasibility-gate wet-lab. **Reframes 503A pathway from blocked-on-dose-question → unblocked, gated only on pharmacy + prescriber identification (still user-action-required).**

## Cross-references
[Disulfiram (Antabuse)](./disulfiram.md) · [Compounding pharmacy track](./compounding-pharmacy-track.md) · [NLRP3 exploit map](./nlrp3-exploit-map.md) · [Computational experiments registry](./computational-experiments.md) · [Experiment folder](../experiments/comp-027-disulfiram-dose-modeling/)
