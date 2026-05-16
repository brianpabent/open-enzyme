# comp-027 — Disulfiram Dose Modeling Summary

**Headline:** GREEN — sub-AUD GSDMD-dominant window EXISTS under the conservative cell-free EC50 anchor.

**Recommended 503A dose range (mg/day):** 100 - 100

## Per-dose dose-response

| Dose (mg/d) | Cmax parent DSF (μM) | Cmax total DTC (μM) | Me-DTC peak (nM) | GSDMD block (parent, conservative) | GSDMD block (total DTC) | NLRP3-palm block (parent) | ALDH inhibition | Verdict |
|---|---|---|---|---|---|---|---|---|
| 25 | 0.10 [0.04-0.25] | 0.4 | 17 | 25% | 57% | 1.0% | 14% | **RED_below_GSDMD_threshold** |
| 50 | 0.20 [0.08-0.50] | 0.8 | 35 | 40% | 73% | 2.0% | 25% | **YELLOW** |
| 62.5 | 0.25 [0.10-0.62] | 1.0 | 43 | 46% | 77% | 2.4% | 29% | **YELLOW** |
| 100 | 0.40 [0.16-1.00] | 1.6 | 70 | 57% | 84% | 3.8% | 40% | **GREEN** |
| 125 | 0.50 [0.20-1.25] | 2.0 | 87 | 62% | 87% | 4.8% | 45% | **YELLOW** |
| 200 | 0.80 [0.32-2.00] | 3.2 | 139 | 73% | 91% | 7.4% | 57% | **RED_above_DER_threshold** |
| 250 | 1.00 [0.40-2.50] | 4.0 | 174 | 77% | 93% | 9.1% | 62% | **RED_above_DER_threshold** |
| 500 | 2.00 [0.80-5.00] | 8.0 | 348 | 87% | 96% | 16.7% | 77% | **RED_above_DER_threshold** |
| 1000 | 4.00 [1.60-10.00] | 16.0 | 695 | 93% | 98% | 28.6% | 87% | **RED_above_DER_threshold** |
| 2000 | 10.22 [4.09-25.55] | 40.9 | 1775 | 97% | 99% | 50.5% | 94% | **RED_above_DER_threshold** |

## Window summary

- **GREEN doses (mg/d):** [100]
- **YELLOW doses (mg/d):** [50, 62.5, 125]
- **RED-below-GSDMD-threshold (mg/d):** [25]
- **RED-above-DER-threshold (mg/d):** [200, 250, 500, 1000, 2000]

## Key assumptions and load-bearing anchors

- DSF PK: Lee 2018 PMC6379104 (CL=0.53 L/hr, Vd=1.3 L, F=0.875).
- Me-DTC PK: Johansson 1989 PMID 2551696 (278 nM peak at 400 mg).
- GSDMD EC50 (conservative): 0.30 μM cell-free liposome — Hu 2020 PMC7316630.
- GSDMD EC50 (optimistic): 0.02 μM cellular preincub — Hu 2020.
- NLRP3-palmitoylation EC50: 10 μM partial / 30 μM complete — Xu 2024 PMC11398858.
- ALDH EC50: 104 nM Me-DTC (calibrated to Faiman 1989 PMID 2537080 hypotension threshold).
- DER hypotension threshold: 40% ALDH inhibition (Faiman 1989).

Anchored verdict thresholds:
- GREEN: GSDMD blockade ≥ 50% AND ALDH inhibition ≤ 40%
- YELLOW: GSDMD blockade ≥ 30% AND ALDH inhibition ≤ 50%
- RED: outside either bound
