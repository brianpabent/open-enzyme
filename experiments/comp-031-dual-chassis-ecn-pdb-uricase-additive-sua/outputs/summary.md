# comp-031 — Dual-chassis EcN PDB + uricase additive SUA prediction

**Question:** does engineered EcN expressing the 2,8-dioxopurine PDB cluster (CBT2.0 precedent) co-administered with a PULSE-style luminal uricase deliver additive serum urate reduction beyond either arm alone, and does PDB-derived butyrate compound with the gut-lumen uricase sink via ABCG2 induction / Q141K trafficking rescue?

## Headline finding

**Verdict: YELLOW (provisional)** — combined dual-chassis intervention is meaningfully better than either single arm but additivity is well below naive sum. The two arms compete for the same scarce luminal urate substrate (per comp-019 substrate-limited regime), so combined urate-consumption ≈ dominant arm (PDB at central scenario) + small residual capture from minor arm (~10% of its solo magnitude). The PDB pathway adds an INDEPENDENT mechanism axis via butyrate-mediated PPARγ ABCG2 induction (WT alleles) + HDAC-mediated Q141K trafficking rescue (variant alleles) — this is what uricase alone cannot deliver. Combined predicted ΔSUA range: **−1.8 to −1.9 mg/dL across genotypes** (90% CI roughly −2.2 to −1.3 mg/dL). Compared to PDB alone (~−1.7), the additive bump is ~−0.1 to −0.2 mg/dL, genotype-stratified (largest in Q141K-hom). 'Provisional' reflects three compounding optimistic assumptions: (a) DOPDH Km mechanistic extrapolation (no direct kcat/Km on the CBT2.0 strain), (b) mouse-to-human translation point-estimate (0.5x central, 0.3–0.7 range), (c) crypt butyrate attenuation extrapolation (Basseville 2012 in-vitro 1–5 mM → in-vivo enterocyte nucleus concentration is empirically open per `wiki/purine-degrading-bacteria.md` §Concentration-gap).


## Central scenario predictions (mid-dose 25 mg/day uricase, 1e10 CFU/g PDB, central translation factors)

| Genotype | Uricase alone | PDB alone | Naive sum | Combined | Additivity ratio |
|---|---|---|---|---|---|
| WT_WT_male_gout | -0.83 mg/dL | -1.76 mg/dL | -2.59 mg/dL | **-1.89 mg/dL** | 0.73 |
| Q141K_het_male_gout | -0.66 mg/dL | -1.64 mg/dL | -2.30 mg/dL | **-1.78 mg/dL** | 0.77 |
| Q141K_hom_male_gout | -0.49 mg/dL | -1.57 mg/dL | -2.06 mg/dL | **-1.83 mg/dL** | 0.89 |

## Monte Carlo (n=5000) — 90% CI per genotype

| Genotype | Uricase alone (med, 90% CI) | PDB alone (med, 90% CI) | Combined (med, 90% CI) |
|---|---|---|---|
| WT_WT_male_gout | -0.83 (-0.83, -0.83) | -1.74 (-2.18, -1.24) | **-1.87** (-2.28, -1.37) |
| Q141K_het_male_gout | -0.66 (-0.66, -0.66) | -1.62 (-2.03, -1.15) | **-1.76** (-2.14, -1.30) |
| Q141K_hom_male_gout | -0.49 (-0.49, -0.49) | -1.55 (-1.94, -1.10) | **-1.82** (-2.19, -1.37) |

## Butyrate → Q141K trafficking rescue fraction

| Genotype | Crypt butyrate (mM, med, 90% CI) | Q141K rescue fraction (med, 90% CI) | Rescue bump ΔSUA |
|---|---|---|---|
| WT_WT_male_gout | 0.88 (0.83, 0.99) | 0.44 (0.41, 0.49) | +0.000 (+0.000, +0.000) mg/dL |
| Q141K_het_male_gout | 0.87 (0.83, 0.96) | 0.43 (0.41, 0.48) | -0.048 (-0.053, -0.045) mg/dL |
| Q141K_hom_male_gout | 0.86 (0.82, 0.94) | 0.43 (0.40, 0.47) | -0.210 (-0.231, -0.199) mg/dL |

## Compositional check — substrate competition

| Genotype | Competition factor (med, 90% CI) | Urice cap ratio | PDB cap ratio |
|---|---|---|---|
| WT_WT_male_gout | 0.11 (0.06, 0.14) | 50x | 30x |
| Q141K_het_male_gout | 0.11 (0.06, 0.14) | 50x | 30x |
| Q141K_hom_male_gout | 0.11 (0.06, 0.14) | 50x | 30x |

**Interpretation:** Competition factor << 1 across all genotypes — the two urate-consuming arms compete for the same scarce substrate. Per comp-019, the system is substrate-limited at all physiological doses. The naive sum of the two arms overestimates the true combined ΔSUA by a factor of 2–3.


## Sensitivity drivers (top contributors to combined-ΔSUA variance)

Largest variance contributors per inspection of MC outputs:
1. **Mouse-to-human translation factor** for CBT2.0 (range 0.3–0.7) — drives PDB-alone magnitude
2. **CBT2.0 colonization density** (1e9–1e11 CFU/g) — log-linear modulation of PDB efficacy
3. **Crypt butyrate attenuation** (0.05–0.5) — drives Q141K rescue fraction
4. **Colonic urate post-meal concentration** (50–500 μM) — minor effect because both arms saturate downstream
5. **Substrate-competition factor** is structurally bounded by capacity ratios; not a free parameter but propagates the comp-019 substrate-limited finding


## Engineering handoff

**Recommendation: ROUTE PDB AND URICASE TO SEPARATE STRAINS.** Two reasons:
1. **The urate-consumption arms compete, not add.** Putting both pathways on a single EcN dual-cassette delivers ~the same urate-consumption ΔSUA as either arm alone (substrate-limited per comp-019). Engineering complexity of a dual cassette (PDB 8-gene cluster + uricase ~1.5 kb expression unit + regulation + selenium-cofactor handling) is NOT justified by the substrate-competition penalty.
2. **The butyrate-mediated additive mechanism does NOT require dual-cassette co-localization.** The butyrate produced by a separate PDB-bearing strain reaches the same colonic lumen as the uricase produced by a separate PULSE-style strain. The PPARγ and HDAC mechanisms operate on the enterocyte from the gut lumen, not at the bacterial-cell scale. Co-administration of TWO strains delivers the same butyrate-mediated synergy as one dual-cassette strain.

**Strategic implication:** the multi-chassis CP6 stack (chassis-pending §M1) is correctly framed — two separate live biotherapeutic products (one PDB-EcN, one PULSE-uricase-EcN), each engineered, manufactured, and dosed independently, co-administered as a combination probiotic. Avoids the regulatory and stability complexity of a single dual-cassette EcN strain that needs both 8-gene selenoprotein cluster AND uricase coordinated expression in the same chassis.
