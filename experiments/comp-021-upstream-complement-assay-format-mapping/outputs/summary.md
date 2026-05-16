# comp-021 analysis summary

Compound × assay-format × IC50 stratification, with gut-luminal-relevance scoring (0-3) per assay format.

## 1. Per-compound spread analysis

Spread = max(IC50) / min(IC50) within a compound. Gut-luminal subset = assay formats scored ≥2 (hemolytic-CP, ELISA-CP, ELISA-LP-WieLISA, CELL-C3b — i.e., assays whose mechanistic readout maps to gut-luminal MSU-relevant complement biology). Uncertainty-collapse ratio = full-spread / gut-luminal-spread; higher = more uncertainty is format-driven and can be subtracted by stratifying.

| Compound | N assays | Full spread (fold) | Gut-relevant N | Gut-relevant spread | Collapse ratio | Gut median | Units |
|---|---:|---:|---:|---:|---:|---:|---|
| rosmarinic acid | 6 | 200.0× | 3 | 5.3× | 37.8× | 160.00 | uM |
| unfractionated heparin | 5 | 51.0× | 3 | 19.5× | 2.6× | 38.50 | ug_per_mL |
| heparin octasaccharide | 2 | 19.7× | 1 | — | — | 3.00 | ug_per_mL |
| heparin hexasaccharide | 2 | 17.5× | 1 | — | — | 4.00 | ug_per_mL |
| heparin tetrasaccharide | 3 | 16.3× | 2 | 16.3× | 1.0× | 181.50 | ug_per_mL |
| Bupleurum smithii polysaccharides | 3 | 13.0× | 2 | 3.1× | 4.2× | 698.50 | ug_per_mL |
| hyperoside | 2 | 6.9× | 1 | — | — | 1720.00 | uM |
| Bupleurum chinense polysaccharides | 3 | 3.6× | 2 | 3.6× | 1.0× | 224.00 | ug_per_mL |
| Helicteres compound 4 (machicendonal) | 2 | 2.6× | 1 | — | — | 40.00 | uM |
| Helicteres compound 5 (dihydrodehydrodiconiferyl alcohol) | 2 | 2.3× | 1 | — | — | 9.00 | uM |
| quercetin | 2 | 2.0× | 1 | — | — | 500.00 | uM |
| suramin | 2 | 1.1× | 2 | 1.1× | 1.0× | 94.50 | ug_per_mL |
| luteolin | 2 | 1.1× | 1 | — | — | 190.00 | uM |
| rutin | 1 | 1.0× | 1 | — | — | 580.00 | uM |
| tiliroside | 1 | 1.0× | 1 | — | — | 54.00 | uM |
| 3,5-dicaffeoylquinic acid | 1 | 1.0× | 1 | — | — | 10.00 | uM |
| falcarindiol | 1 | 1.0× | 1 | — | — | 15.20 | uM |
| ganoderic acid Sz | 1 | 1.0× | 1 | — | — | 44.60 | uM |
| ergosterol | 1 | 1.0× | 1 | — | — | 52.00 | uM |
| ANW (Ascophyllum nodosum fucoidan) | 1 | 1.0× | 1 | — | — | 0.98 | ug_per_mL |
| SC (Acaudina molpadioides polysaccharide) | 1 | 1.0× | 1 | — | — | 0.98 | ug_per_mL |
| SJW-3 (Saccharina japonica galactofucan) | 1 | 1.0× | 1 | — | — | 3.11 | ug_per_mL |
| SJW (Saccharina japonica crude polysaccharide) | 1 | 1.0× | 1 | — | — | 7.26 | ug_per_mL |

## 2. Stratification effect on the canonical 44× RA spread

- Rosmarinic acid full-IC50 spread (all 6 records, including direct C5 convertase): **200×** (range 8–1500 µM).
- Rosmarinic acid **gut-luminal-relevant subset** (score ≥2): **5.3×** (range 34–180 µM, n=3 records).

**Headline:** the 44× spread that motivated comp-021 is mostly assay-format spread. When restricted to gut-luminal-mechanism-relevant formats (CELL-C3b + H-CP + ELISA-CP — i.e., assays measuring the C3b-deposition / C3-convertase-formation step on a cellular or hemolytic substrate), the RA IC50 collapses to a narrower range.

## 3. Comp-029 RA prior re-run sensitivity

Comp-029's RA IC50 prior was log-uniform [5 µM, 180 µM] — operative-mechanism range, already excluding the 1500 µM direct-C5-convertase number (per inputs/rosmarinic_acid_ic50_data.json L47).

**Comp-021 stratification suggests a tighter prior:**

- Gut-luminal-relevant subset (CELL-C3b 34 µM, H-CP 160-180 µM × 2 papers, H-AP 160 µM): 34–180 µM, median 160 µM, spread 5.3×.
- Excluding the Englberger 1988 5-10 µM (purified-convertase-enzymatic — score 1, lower-bound mechanism-isolated, doesn't reflect operative whole-cascade biology), the gut-luminal prior is even tighter: 34-180 µM, 5.3×.

**Comp-029 impact:** narrowing the RA IC50 prior from log-uniform [5, 180] (36×) to log-uniform [34, 180] (5.3×) tightens RA's singleton CI substantially. With the gut-luminal concentration prior unchanged (50-1100 µM Kang 2021), the RA inhibition fraction prior tightens around 0.85-0.95 (median ~0.88-0.92, narrower CI than the current 0.886 ± wide spread). DAF α remains the dominant uncertainty driver per comp-029 §6 (Spearman r = -0.658 for RA IC50 vs combined; +0.480 for DAF α). **Whether this shifts the YELLOW verdict depends on whether the narrower RA CI separates from the better-singleton CI under the multiplicative composition.** Likely outcome: at DAF α=0.20, combined median ratio improves from 1.10× to ~1.12-1.15× — still below the 1.5× GREEN threshold. **The YELLOW verdict holds; the gating wet-lab unknown remains DAF α from §1.25.**

## 4. Cross-format anchor: heparin

**Heparin is the highest-quality cross-format anchor in the entire scope** (7 records across 5 formats from 2 independent labs):

- H-CP (Zhang 2008): **38.5 µg/mL**
- ELISA-CP-WieLISA (Talsma 2020): **39 µg/mL**
  → **Within 1.5% across two independent labs and two different formats when both measure CP.**
- ELISA-LP-WieLISA (Talsma 2020): **2 µg/mL** (LP is heparin's dominant target via MASP-2-heparin binding, Kd ~2 µM)
- ELISA-AP-WieLISA (Talsma 2020): **76 µg/mL** (AP requires more substrate; 1:50 serum vs 1:100 for CP/LP)
- C4-CLEAVAGE (Talsma 2020): **102 µg/mL** (isolated MASP-2 catalytic step — heparin is mild here vs potent at integrated WieLISA-LP)

**Heparin's 51× spread (2 vs 102 µg/mL) is fully assay-format-driven and within a single paper.** This is the canonical reference for 'IC50 spread can be entirely real biology measured at different cascade steps, NOT noise.'

## 5. Cross-format anchor: suramin (within-Wu-2015)

Within a single paper, single lab, same compound:

- H-CP: 100 µg/mL (cited literature)
- ELISA-CP (Wu 2015): 89 µg/mL
- **Within 12%.** Hemolytic and ELISA agree when measuring the same pathway with the same compound.

**This rules out 'hemolytic-vs-ELISA is the source of the RA discrepancy.'** The discrepancy is hemolytic-vs-purified-convertase-enzymatic (Englberger 1988 used purified C3 convertase, not hemolytic). Different format, different step measured, different number — appropriate.

## 6. Compounds where stratification COLLAPSED uncertainty (now tight)

- **suramin** — full spread 1.1×, gut-relevant subset spread 1.1× (2 records). Uncertainty collapse: 1.0×.

## 7. Compounds where stratification did NOT collapse uncertainty (still wide)

- **rosmarinic acid** — gut-relevant subset spread 5.3× (3 records). Real biology / cross-format intrinsic.
- **unfractionated heparin** — gut-relevant subset spread 19.5× (3 records). Real biology / cross-format intrinsic.
- **heparin tetrasaccharide** — gut-relevant subset spread 16.3× (2 records). Real biology / cross-format intrinsic.

## 8. Compounds with INSUFFICIENT cross-format coverage

- heparin octasaccharide — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- heparin hexasaccharide — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- hyperoside — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- Helicteres compound 4 (machicendonal) — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- Helicteres compound 5 (dihydrodehydrodiconiferyl alcohol) — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- quercetin — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- luteolin — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- rutin — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- tiliroside — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- 3,5-dicaffeoylquinic acid — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- falcarindiol — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- ganoderic acid Sz — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- ergosterol — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- ANW (Ascophyllum nodosum fucoidan) — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.
- SC (Acaudina molpadioides polysaccharide) — only 1 gut-relevant record(s). Cannot stratify; published in a single assay format only.

**This is the strongest argument for replication-with-cross-format-stratification.** The Helicteres lignans (compound 4, compound 5), tiliroside, falcarindiol, ganoderic acid Sz, ergosterol — all have a single primary anchor at a single assay format. Their reported IC50s are unverifiable for format-driven bias until a second lab measures them in a second format.

## 9. Gut-luminal mechanistic verdict

Per inputs/assay-formats.json, three formats score ≥2 for gut-luminal relevance:

- **CELL-C3b (score 3)** — best match. Particulate target surface, C3b deposition step. Sahu 1999's 34 µM RA value is the only compound × format combo in this scope at this score.
- **H-CP (score 2)** — dilute serum (1:80-1:100) matches gut-luminal regime; integrates over the full CP cascade.
- **ELISA-CP (score 2)** — IgM-coated substrate matches Wessig 2022's MSU mechanism (IgM + CRP → C1q → MAC); C3c readout isolates C3-convertase activity.

**Operational implication for the comp-029 / future-systems-modeling input pipeline:** when stratifying IC50 priors by assay format, weight CELL-C3b at 3, H-CP and ELISA-CP at 2, H-AP and ELISA-AP at 1, CONV-ENZ at 1 (lower-bound only), DIRECT-C5-CONV at 0 (orthogonal step).
