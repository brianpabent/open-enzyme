# Phase 3a — LOTUS × ChEMBL chokepoint intersection

**Method:** Exact canonical-SMILES match between LOTUS-pulled fungal compounds and ChEMBL bioactivity records for 5 priority chokepoint targets (ABCG2, C5aR1, NLRP3, URAT1, XO).

**Inputs:** 6,798 LOTUS compounds × 1,000 ChEMBL activity records.
**Hits (compound × target pairs):** 12

| Chokepoint | Activities scanned | LOTUS-fungal hits |
|---|---:|---:|
| ABCG2 | (see raw cache) | 7 |
| C5aR1 | (see raw cache) | 0 |
| NLRP3 | (see raw cache) | 0 |
| URAT1 | (see raw cache) | 1 |
| XO | (see raw cache) | 4 |

## Top hits per target

### ABCG2

| Rank | LOTUS compound | Fungal source(s) | Potency | Year | ChEMBL ID |
|---:|---|---|---|---|---|
| 1 | quercetin | [query-hint] Agaricus | IC50 6900 nM (pChEMBL 5.16) | 2011 | CHEMBL50 |
| 2 | genistein | [query-hint] Cordyceps sinensis, [query-hint] Ophiocordyceps | IC50 6900 nM (pChEMBL 5.16) | 2011 | CHEMBL44 |
| 3 | quercetin | [query-hint] Agaricus | IC50 7600 nM (pChEMBL 5.12) | 2011 | CHEMBL50 |
| 4 | 5,8-dihydroxy-10-methoxy-2-methylbenzo[h]chromen-4-one | [query-hint] Aspergillus niger | IC50 12800 nM (pChEMBL 4.89) | 2010 | CHEMBL454794 |
| 5 | bois d,arc | [query-hint] Ganoderma, [query-hint] Ganoderma lucidum | IC50 21000 nM (pChEMBL 4.68) | 2011 | CHEMBL28626 |
| 6 | bois d,arc | [query-hint] Ganoderma, [query-hint] Ganoderma lucidum | IC50 49000 nM (pChEMBL 4.31) | 2011 | CHEMBL28626 |
| 7 | 5,8-dihydroxy-6-methoxy-2-methylbenzo[g]chromen-4-one | [query-hint] Aspergillus niger | IC50 None None (pChEMBL None) | 2010 | CHEMBL252106 |

### URAT1

| Rank | LOTUS compound | Fungal source(s) | Potency | Year | ChEMBL ID |
|---:|---|---|---|---|---|
| 1 | bois d,arc | [query-hint] Ganoderma, [query-hint] Ganoderma lucidum | IC50 2000 nM (pChEMBL 5.7) | 2007 | CHEMBL28626 |

### XO

| Rank | LOTUS compound | Fungal source(s) | Potency | Year | ChEMBL ID |
|---:|---|---|---|---|---|
| 1 | quercetin | [query-hint] Agaricus | IC50 2620 nM (pChEMBL 5.58) | 1998 | CHEMBL50 |
| 2 | quercetin | [query-hint] Agaricus | IC50 3000 nM (pChEMBL 5.52) | 2002 | CHEMBL50 |
| 3 | quercetin | [query-hint] Agaricus | IC50 3500 nM (pChEMBL 5.46) | 2016 | CHEMBL50 |
| 4 | bois d,arc | [query-hint] Ganoderma, [query-hint] Ganoderma lucidum | IC50 10100 nM (pChEMBL 5) | 1998 | CHEMBL28626 |

## Caveats

- **Exact canonical-SMILES match misses normalization-different records.** ChEMBL and LOTUS may canonicalize differently (stereochemistry, salt forms, tautomers). True intersection is likely 1.5-3× the count reported here.
- **ChEMBL coverage of fungal compounds is severely Western-pharma-biased** (Phase 2a finding). The intersection captures only the small subset of LOTUS compounds that ChEMBL bothered to assay against the priority targets.
- **Phase 3 is incomplete.** Next: HIT (TCM-curated) target mapping, SwissTargetPrediction for orphan compounds, and InChIKey cross-validation via ChEMBL get_admet calls.
