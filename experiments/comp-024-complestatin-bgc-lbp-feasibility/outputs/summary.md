# comp-024 Results — Complestatin BGC LBP Feasibility

## Headline

**Verdict: RED (for the LBP-track framing).** Best host is E_coli_Nissle_1917 at score 0.544 (YELLOW); Bacteroides is RED at 0.225. The verdict frame is **the original question** — 'is complestatin BGC the right next CP0 LBP-chassis engineering payload?' — and the answer is no. No host clears the GREEN threshold (0.60); the best is mid-YELLOW with two compounding low-end factors (O2 dependence + heterologous-expression precedent). The decision is RED for committing to this payload now.


The dominant blocking factor for both hosts is **O2-dependent tailoring chemistry** (P450 oxidative phenolic coupling + nonheme halogenase + FMN oxidase) being fundamentally incompatible with colonic-anaerobic-resident lifestyle. Without ComI/ComJ P450 activity, the linear peptide lacks the rigid crosslinked architecture that gives complestatin its C1q/C4b binding (Park 2016 deletion derivatives M55/S56 are inactive).


## BGC architecture (canonical)

- **Compound family:** NRPS-derived cyclic glycopeptide-like; member of the vancomycin/teicoplanin/chloropeptin structural family
- **Producer:** Streptomyces lavendulae (S. chartreusis AN1542 strain also produces complestatin family per Park 2016)
- **Cluster size:** 48.7 kb original / 54.5 kb reconstituted (Park 2016)
- **Total ORFs:** 16
- **NRPS architecture:** 7 modules total (1 loading + 6 extension + terminal thioesterase)
- **NRPS genes:** comA, comB, comC, comD
- **P450 oxidative phenolic coupling:** comI, comJ
- **Nonheme halogenase:** comH
- **Hpg-biosynthesis genes (in-cluster):** hmaS, hmo, hpgT, pd
- **Heterologous-expression precedent:** *S. lividans* TK24 (Park 2016 PMID 27383040) — phylum-internal; sub-mg/L unoptimized. **No precedent for E. coli or Bacteroides.**

## Complestatin feasibility scores (per host)


### E_coli_Nissle_1917
**Geometric mean: 0.544 (YELLOW)**
Limiting factor: **O2_dependence_vs_host_lifestyle** at 0.3

| Factor | Score |
|---|---|
| cluster_size_tractability | 0.55 |
| GC_content_codon_compatibility | 0.65 |
| non_canonical_amino_acid_precursor_supply | 0.75 |
| PPTase_compatibility | 0.85 |
| P450_redox_compatibility | 0.35 |
| O2_dependence_vs_host_lifestyle | 0.3 |
| engineering_toolkit_maturity | 0.9 |
| heterologous_expression_precedent | 0.35 |
| host_toxicity_self_resistance | 0.55 |

### Bacteroides_thetaiotaomicron_VPI_5482
**Geometric mean: 0.225 (RED)**
Limiting factor: **P450_redox_compatibility** at 0.05

| Factor | Score |
|---|---|
| cluster_size_tractability | 0.3 |
| GC_content_codon_compatibility | 0.45 |
| non_canonical_amino_acid_precursor_supply | 0.55 |
| PPTase_compatibility | 0.45 |
| P450_redox_compatibility | 0.05 |
| O2_dependence_vs_host_lifestyle | 0.05 |
| engineering_toolkit_maturity | 0.45 |
| heterologous_expression_precedent | 0.1 |
| host_toxicity_self_resistance | 0.4 |

## Comparator: C1-INH (LBP-luminal) parallel thread


### C1-INH in E_coli_Nissle_1917
**Geometric mean: 0.774 (GREEN)**
Limiting factor: **luminal_protease_stability** at 0.35

| Factor | Score |
|---|---|
| cluster_size_tractability | 0.95 |
| GC_content_codon_compatibility | 0.9 |
| non_canonical_amino_acid_precursor_supply | 1.0 |
| PPTase_compatibility | 1.0 |
| P450_redox_compatibility | 1.0 |
| O2_dependence_vs_host_lifestyle | 1.0 |
| engineering_toolkit_maturity | 0.9 |
| heterologous_expression_precedent | 0.65 |
| host_toxicity_self_resistance | 0.85 |
| luminal_protease_stability | 0.35 |
| glycosylation_for_function | 0.4 |

## Track comparison

- **Best complestatin host:** E_coli_Nissle_1917 (score 0.544, YELLOW)
- **Best C1-INH host:** E_coli_Nissle_1917 (score 0.774, GREEN)
- **More tractable as next CP0 engineering payload:** **C1-INH (LBP-luminal)** (margin 0.23)

C1-INH wins the head-to-head because its dominant feasibility question (luminal-protease stability + glycosylation) is a *single-axis* problem testable with a comp-006-style protease-stability analysis on the SERPING1 sequence. Complestatin's dominant question (O2-dependent tailoring chemistry in an anaerobic-resident host) is a *fundamental-incompatibility* problem with no known engineering workaround. The complestatin BGC remains a candidate for aerobic-fermentation production (food-grade or pharma-grade Streptomyces-class manufacturing), but not for in-situ LBP-luminal delivery.

**C1-INH verdict is GREEN (provisional).** The 0.774 score depends on two C1-INH-specific load-bearing factors (luminal_protease_stability 0.35, glycosylation_for_function 0.40) that are not yet computationally validated. The GREEN→GREEN-confirmed transition requires the comp-006-style protease-stability analysis to land first. The C1-INH track is provisionally GREEN; the complestatin track is unambiguously RED for the LBP-chassis framing. **Also note:** the geometric mean comparison is mildly apples-to-oranges because the C1-INH track has 11 factors (9 base + 2 C1-INH-specific) while the complestatin track has 9. The 11 factors include 5 factors at 1.0 (PPTase / P450 redox / O2 / non-canonical aa / cluster-size) which are non-applicable to a single-gene protein payload — they pull the C1-INH geometric mean up structurally. Conservative interpretation: C1-INH's 7 informative factors (the 9 base minus the 5 non-applicable plus the 2 C1-INH-specific) have geometric mean ~0.70, still meaningfully above complestatin's 0.544. The track comparison verdict (C1-INH more tractable) is robust to this caveat.

## Wet-lab handoff

**Do not invest in complestatin BGC LBP chassis engineering as next CP0 payload.** Instead:
1. Promote C1-INH (LBP-luminal) to a real comp-NNN — protease-stability analysis on SERPING1 in EcN-secreted format, parallel to comp-006 / comp-012 DAF analysis. Sub-mg subagent task. ~$0 cost.
2. Hold complestatin BGC as an aerobic-fermentation-production candidate ONLY (food-grade Streptomyces or pharma-grade actinomycete chassis) — distinct from the LBP track. If pursued, the comp-NNN brief would scope the production-fermentation route, not in-situ delivery.
3. The CP0 engineering payload stack remains:
   - **Engineered DAF SCR1-4 (koji-secreted)** — H05 / validation §1.25, primary near-term path
   - **Engineered C1-INH (LBP-luminal)** — promoted from comp-018 P2 follow-up to next computational gate (proposed comp-NNN); near-twin to H05
   - **Dietary rosmarinic acid / luteolin** — separate non-engineering CP0 axis already documented
   - **Complestatin BGC (Streptomyces production)** — parked as aerobic-fermentation candidate, NOT LBP track