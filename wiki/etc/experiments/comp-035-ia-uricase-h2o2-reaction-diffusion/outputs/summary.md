# comp-035 Analysis Summary (v1)

Generated: 2026-05-16 — RNG seed 35, N = 20000 Monte Carlo samples — elapsed 1.22s

## Decision rule

| Band | Steady-state [H₂O₂] at joint-tissue boundary |
|---|---|
| GREEN | < 10.0 µM |
| YELLOW | 10.0-100.0 µM |
| RED | > 100.0 µM |

## Predicted steady-state [H₂O₂] at joint-tissue boundary

| Architecture | p5 | median | p95 | Headline verdict (median) |
|---|---|---|---|---|
| Pickering emulsion (Liu 2025 geometry) | 3.43e-02 µM | 1.91e-01 µM | 1.09e+00 µM | **GREEN** |
| Fusion protein | 5.86e-03 µM | 3.38e-02 µM | 1.99e-01 µM | **GREEN** |
| Free co-formulated | 5.21e-03 µM | 1.91e-01 µM | 7.22e+00 µM | **GREEN** |

(Pickering LOCAL [H₂O₂] just outside the droplet shell: p5 5.04e-03, median 4.73e-02, p95 4.47e-01 µM.)

## Damkohler / coupling regime

| Architecture | Quantity | p5 | median | p95 |
|---|---|---|---|---|
| Pickering | Da_shell | 2.58e-04 | 4.55e-03 | 7.93e-02 |
| Pickering | escape fraction | 9.62e-01 | 9.98e-01 | 1.00e+00 |
| Fusion | P_capture_intra | 0.146 | 0.235 | 0.585 |
| Fusion | bulk-capture L (µm) | 1.41e-01 | 6.04e-01 | 2.53e+00 |
| Free | Da_joint | 6.75e+06 | 1.34e+08 | 2.61e+09 |
| Free | capture L (µm) | 1.42e-01 | 5.99e-01 | 2.56e+00 |

## Architecture ranking (lowest to highest predicted [H₂O₂])

1. fusion: 3.38e-02 µM
2. free_co_formulated: 1.91e-01 µM
3. pickering: 1.91e-01 µM

## Verdict distribution

| Architecture | P(GREEN) | P(YELLOW) | P(RED) |
|---|---|---|---|
| Pickering (joint bulk) | 1.000 | 0.000 | 0.000 |
| Fusion | 1.000 | 0.000 | 0.000 |
| Free coformulated | 0.966 | 0.034 | 0.000 |

## Top sensitivity drivers

### Pickering
- kcat_over_km_CAT: r = -0.972
- kcat_URI: r = 0.235
- k_clear_per_s: r = 0.013
- Km_URI_M: r = -0.013
- D_H2O2_synovial: r = 0.007

### Fusion
- kcat_over_km_CAT: r = -0.954
- kcat_URI: r = 0.232
- fusion_active_site_sep_nm: r = 0.165
- k_clear_per_s: r = 0.015
- Km_URI_M: r = -0.013

### Free coformulated
- free_URI_uM: r = 0.603
- free_CAT_uM: r = -0.601
- kcat_over_km_CAT: r = -0.480
- kcat_URI: r = 0.116
- pick_interfacial_density_per_um2: r = 0.019

## Edge-case scenarios

| Scenario | Pickering [H₂O₂] (µM) | Fusion [H₂O₂] (µM) | Free [H₂O₂] (µM) | Picker | Fus | Free |
|---|---|---|---|---|---|---|
| low_CAT_dose_1uM | 3.15e-01 | 5.13e-02 | 3.16e+00 | GREEN | GREEN | GREEN |
| high_dose_100uM | 3.15e-01 | 5.13e-02 | 3.16e-01 | GREEN | GREEN | GREEN |
| high_urate_5mM | 3.23e-01 | 5.25e-02 | 3.23e-01 | GREEN | GREEN | GREEN |
| low_urate_0.1mM | 2.50e-01 | 4.06e-02 | 2.50e-01 | GREEN | GREEN | GREEN |
| low_clearance_0.001 | 3.15e-01 | 5.13e-02 | 3.16e-01 | GREEN | GREEN | GREEN |
| high_kcat_URI_20 | 4.85e-01 | 7.89e-02 | 4.85e-01 | GREEN | GREEN | GREEN |
| low_kcat_over_km_CAT_1e7 | 1.26e+00 | 2.05e-01 | 1.26e+00 | GREEN | GREEN | GREEN |
| small_joint_MTP1_0.3mL | 3.15e-01 | 5.13e-02 | 3.16e-01 | GREEN | GREEN | GREEN |
| uneven_free_URI_100uM_CAT_1uM | 3.15e-01 | 5.13e-02 | 3.16e+01 | GREEN | GREEN | YELLOW |

## Reproduction

```bash
cd experiments/comp-035-ia-uricase-h2o2-reaction-diffusion
python3 analyze.py
```

Stdlib-only Python 3. Deterministic given seed 35. All inputs in `inputs/`, all outputs regenerated under `outputs/`.
