> **INVALIDATED / SUPERSEDED by comp-044.** These historical quantitative outputs omit physiological luminal-urate occupancy and finite residence/exposure time. Do not use them for dose, efficacy, genotype ranking, flat-dose, yield, or trial-design decisions. Phase A found no Q141K-stratified uricase clinical outcome in the sources searched for comp-019 as of 2026-05-08.

# comp-019 — Flux Model Results Summary

Predicted delta-SUA (mg/dL) at steady state by ABCG2 genotype and uricase dose.

Negative values = serum urate reduction.


## Central estimates (deterministic)

| Scenario | Low 5 mg/d | Mid 25 mg/d | High 50 mg/d |
|---|---|---|---|
| WT/WT, male gout patient | -0.74 | -0.74 | -0.74 |
| Q141K heterozygous, male gout patient | -0.59 | -0.59 | -0.59 |
| Q141K homozygous, male gout patient | -0.44 | -0.44 | -0.44 |
| WT/WT, female gout patient | -0.65 | -0.65 | -0.65 |
| Q141K heterozygous, female gout patient | -0.52 | -0.52 | -0.52 |
| Q141K homozygous, female gout patient | -0.37 | -0.37 | -0.37 |
| Severe ABCG2 dysfunction (Q126*+Q141K compound), male | -0.24 | -0.24 | -0.24 |


## Monte Carlo 90% CI (n=5000)

| Scenario | Low 5 mg/d (median, 90% CI) | Mid 25 mg/d (median, 90% CI) | High 50 mg/d (median, 90% CI) |
|---|---|---|---|
| WT/WT, male gout patient | -0.83 (-1.14 to -0.57) | -0.83 (-1.13 to -0.57) | -0.83 (-1.13 to -0.57) |
| Q141K heterozygous, male gout patient | -0.66 (-0.91 to -0.45) | -0.67 (-0.91 to -0.45) | -0.67 (-0.91 to -0.46) |
| Q141K homozygous, male gout patient | -0.50 (-0.67 to -0.34) | -0.50 (-0.68 to -0.34) | -0.49 (-0.67 to -0.34) |
| WT/WT, female gout patient | -0.73 (-1.00 to -0.50) | -0.74 (-1.00 to -0.50) | -0.74 (-1.00 to -0.50) |
| Q141K heterozygous, female gout patient | -0.58 (-0.80 to -0.40) | -0.59 (-0.80 to -0.40) | -0.59 (-0.80 to -0.40) |
| Q141K homozygous, female gout patient | -0.41 (-0.57 to -0.28) | -0.42 (-0.57 to -0.29) | -0.42 (-0.57 to -0.29) |
| Severe ABCG2 dysfunction (Q126*+Q141K compound), male | -0.27 (-0.38 to -0.19) | -0.28 (-0.37 to -0.19) | -0.27 (-0.37 to -0.19) |


## Capacity-vs-substrate diagnostic

Whether enzyme capacity exceeds delivered intestinal urate flux at this genotype + dose.
Ratio >= 1.0 means substrate-limited (uricase clamps lumen, sink amplification factor 0.40 applies).
Ratio < 1.0 means capacity-limited (delta-intestinal bounded by enzyme dose).

| Scenario | Low 5 mg/d ratio | Mid 25 mg/d ratio | High 50 mg/d ratio |
|---|---|---|---|
| WT/WT, male gout patient | 32.62 | 163.09 | 326.18 |
| Q141K heterozygous, male gout patient | 43.49 | 217.45 | 434.90 |
| Q141K homozygous, male gout patient | 65.24 | 326.18 | 652.35 |
| WT/WT, female gout patient | 32.62 | 163.09 | 326.18 |
| Q141K heterozygous, female gout patient | 43.49 | 217.45 | 434.90 |
| Q141K homozygous, female gout patient | 65.24 | 326.18 | 652.35 |
| Severe ABCG2 dysfunction (Q126*+Q141K compound), male | 130.47 | 652.35 | 1304.71 |


## Model assumptions

- ABCG2 operates in linear regime in vivo (lumen urate ~0.6 uM << Km 8240 uM)
- Uricase clamps lumen urate to ~0; sink amplification factor 0.40 (40% of secreted urate would have been reabsorbed without uricase)
- Genotype scales secretion capacity linearly per Matsuo 2014 + Miyazaki 2025 framework
- Renal compensation offsets 30% of gut delta-flux (sensitivity: 0-50%)
- 1st-order steady-state approximation for delta-SUA


## Retired historical interpretation — invalid; do not use

The original model mapped nominal enzyme capacity to ΔSUA, responder ordering, and dose/yield conclusions without physiological luminal-urate occupancy or finite residence/exposure time. No Phase B interpretation survives. The numerical tables above remain only to reproduce the invalid artifact.
