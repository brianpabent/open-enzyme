# Phase 3 target-mapping summary (unified compound × chokepoint)

**Date:** 2026-05-17  
**Method:** ChEMBL `activity.json` per chokepoint target (resolved by UniProt → target_chembl_id), intersected with the unified InChIKey table by exact + 2D-InChIKey match.

## Coverage statistics

- Unified compounds: 9,778
- Compounds with ≥1 empirical chokepoint hit: 177 (1.81%)
- Target-orphan compounds (no ChEMBL activity at any of the 24 chokepoints): 9,601 (98.19%)
- Predicted-target coverage (SwissTargetPrediction): **NOT RUN** — sandbox-blocked, deferred to re-run plan.

## Per-chokepoint empirical-hit counts

| Chokepoint | UniProt | ChEMBL target | Hits (all) | Hits (toxicity-pass) |
|---|---|---|---:|---:|
| URAT1 | Q96S37 | CHEMBL6120 | 3 | 3 |
| GLUT9 | Q9NRM0 | CHEMBL2052034 | 0 | 0 |
| ABCG2 | Q9UNQ0 | CHEMBL5393 | 52 | 52 |
| XO | P47989 | CHEMBL1929 | 103 | 103 |
| NLRP3 | Q96P20 | CHEMBL1741208 | 0 | 0 |
| ASC | Q9ULZ3 | CHEMBL6067324 | 0 | 0 |
| CASP1 | P29466 | CHEMBL4801 | 54 | 54 |
| IL1B | P01584 | CHEMBL1909490 | 3 | 3 |
| TNFA | P01375 | CHEMBL1825 | 43 | 43 |
| C5aR1 | P21730 | CHEMBL2373 | 0 | 0 |
| Lp_PLA2 | Q13093 | CHEMBL3514 | 0 | 0 |
| HDAC6 | Q9UBN7 | CHEMBL1865 | 12 | 12 |
| PPARG | P37231 | CHEMBL235 | 29 | 29 |
| KEAP1 | Q14145 | CHEMBL2069156 | 0 | 0 |
| NRF2 | Q16236 | CHEMBL1075094 | 10 | 10 |
| OAT1 | Q4U2R8 | CHEMBL1641347 | 3 | 3 |
| OAT3 | Q8TCC7 | CHEMBL1641348 | 7 | 7 |
| OAT4 | Q9NS40 | CHEMBL2362996 | 0 | 0 |
| ADA | P00813 | CHEMBL1910 | 4 | 4 |
| PINK1 | Q9BXM7 | CHEMBL3337330 | 0 | 0 |
| PDI | P07237 | CHEMBL5422 | 0 | 0 |
| PDIA3 | P30101 | CHEMBL4296001 | 0 | 0 |
| TXN | P10599 | CHEMBL2010624 | 0 | 0 |
| TXNIP | Q9H3M7 | — | 0 | 0 |

## Top-5 empirical hits per chokepoint (potency-ranked, toxicity-pass only)

### URAT1

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | bois d,arc | Ganoderma, Ganoderma lucidum | IC50 2000.0 nM | 5.70 | 2007 | CHEMBL28626 |
| 2 | bois d,arc | Ganoderma, Ganoderma lucidum | Ki 2000.0 nM | 5.70 | 2023 | CHEMBL28626 |
| 3 | bois d,arc | Ganoderma, Ganoderma lucidum | Ki 5740.0 nM | 5.24 | 2007 | CHEMBL28626 |

### ABCG2

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | (1s,12r,15r,23r)-16-acetyl-12-methyl-23-(2-methylbut-3-en-2-yl)-3,11,14,16-tetraazahexacyclo[12.10.0.0²,¹¹.0⁴,⁹.0¹⁵,²³.0 | Aspergillus, Aspergillus terreus | Inhibition 21.8 % |  | 2015 | CHEMBL3402065 |
| 2 | 16-acetyl-12-methyl-23-(2-methylbut-3-en-2-yl)-3,11,14,16-tetraazahexacyclo[12.10.0.0²,¹¹.0⁴,⁹.0¹⁵,²³.0¹⁷,²²]tetracosa-2 | Aspergillus terreus | Inhibition 21.8 % |  | 2015 | CHEMBL3402065 |
| 3 | quercetin | Agaricus | EC50 30.0 nM | 7.52 | 2018 | CHEMBL50 |
| 4 | 5,8-dihydroxy-10-methoxy-2-methylbenzo[h]chromen-4-one | Aspergillus niger | Inhibition 31.0 % |  | 2010 | CHEMBL454794 |
| 5 | quercetin | Agaricus | Inhibition 39.0 % |  | 2021 | CHEMBL50 |

### XO

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | (2e)-4-{[(2e,6e,10e,14e)-16-hydroxy-2,6,10,14-tetramethylhexadeca-2,6,10,14-tetraen-1-yl]oxy}-4-oxobut-2-enoic acid | Suillus | Inhibition -7.0 % |  | 2004 | CHEMBL470056 |
| 2 | 4-[(16-hydroxy-2,6,10,14-tetramethylhexadeca-2,6,10,14-tetraen-1-yl)oxy]-4-oxobut-2-enoic acid | Suillus | Inhibition -7.0 % |  | 2004 | CHEMBL470056 |
| 3 | 16-[(3-carboxy-2-methylprop-2-enoyl)oxy]-2,6,10,14-tetramethylhexadeca-2,6,10,14-tetraenoic acid | Suillus | Inhibition -5.0 % |  | 2004 | CHEMBL471069 |
| 4 | (2e,6e,14e)-16-{[(2e)-3-carboxy-2-methylprop-2-enoyl]oxy}-2,6,10,14-tetramethylhexadeca-2,6,10,14-tetraenoic acid | Suillus | Inhibition -5.0 % |  | 2004 | CHEMBL471069 |
| 5 | (2e,6e,10e,14e)-16-{[(2e)-3-carboxy-2-methylprop-2-enoyl]oxy}-2,6,10,14-tetramethylhexadeca-2,6,10,14-tetraenoic acid | Suillus | Inhibition -5.0 % |  | 2004 | CHEMBL471069 |

### CASP1

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | Berkeleyamide A | Penicillium | IC50 330.0 nM | 6.48 | 2008 | CHEMBL466565 |
| 2 | Berkeleyamide D | Penicillium | IC50 610.0 nM | 6.21 | 2008 | CHEMBL466747 |
| 3 | arachidonic acid | Agaricus | Potency 31622.8 nM | 4.50 |  | CHEMBL15594 |
| 4 | bois d,arc | Ganoderma, Ganoderma lucidum | Potency 39810.7 nM | 4.40 |  | CHEMBL28626 |
| 5 | DEHP | Penicillium | IC50 |  |  | CHEMBL402794 |

### IL1B

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | Berkeleyone A | Penicillium | IC50 2700.0 nM | 5.57 | 2011 | CHEMBL1911627 |
| 2 | Berkeleyone B | Penicillium | IC50 3700.0 nM | 5.43 | 2011 | CHEMBL1911628 |
| 3 | Berkeleyone C | Penicillium | IC50 37800.0 nM | 4.42 | 2011 | CHEMBL1911630 |

### TNFA

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | Ganoderic acid H | Ganoderma | Kd 2.45 nM | 8.61 | 2014 | CHEMBL1922178 |
| 2 | (2r,6r)-6-[(1r,3as,5as,7s,9as,11s,11ar)-11-(acetyloxy)-7-hydroxy-3a,6,6,9a,11a-pentamethyl-3,4,10-trioxo-1h,2h,5h,5ah,7h | Ganoderma, Ganoderma lucidum | Kd 2.45 nM | 8.61 | 2014 | CHEMBL1922178 |
| 3 | 6-[(3ar,9as,11ar)-11-(acetyloxy)-7-hydroxy-3a,6,6,9a,11a-pentamethyl-3,4,10-trioxo-1h,2h,5h,5ah,7h,8h,9h,11h-cyclopenta[ | Ganoderma, Ganoderma lucidum | Kd 2.45 nM | 8.61 | 2014 | CHEMBL1922178 |
| 4 | 6-[11-(acetyloxy)-7-hydroxy-3a,6,6,9a,11a-pentamethyl-3,4,10-trioxo-1h,2h,5h,5ah,7h,8h,9h,11h-cyclopenta[a]phenanthren-1 | Ganoderma, Ganoderma lucidum | Kd 2.45 nM | 8.61 | 2014 | CHEMBL1922178 |
| 5 | (2r,6s)-6-[(1r,3ar,5ar,7s,9as,11s,11ar)-11-(acetyloxy)-7-hydroxy-3a,6,6,9a,11a-pentamethyl-3,4,10-trioxo-1h,2h,5h,5ah,7h | Ganoderma, Ganoderma lucidum | Kd 2.45 nM | 8.61 | 2014 | CHEMBL1922178 |

### HDAC6

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | Monacolin K | Aspergillus, Aspergillus terreus | IC50 16283.0 nM | 4.79 | 2016 | CHEMBL503 |
| 2 | 8-[2-(4-hydroxy-6-oxooxan-2-yl)ethyl]-3,7-dimethyl-1,2,3,7,8,8a-hexahydronaphthalen-1-yl 2-methylbutanoate | Aspergillus terreus | IC50 16283.0 nM | 4.79 | 2016 | CHEMBL503 |
| 3 | lovastatin | Aspergillus terreus, Pleurotus, Pleurotus ostreatus | IC50 16283.0 nM | 4.79 | 2016 | CHEMBL503 |
| 4 | Monacolin K | Aspergillus, Aspergillus terreus | IC50 16285.0 nM | 4.79 | 2013 | CHEMBL503 |
| 5 | 8-[2-(4-hydroxy-6-oxooxan-2-yl)ethyl]-3,7-dimethyl-1,2,3,7,8,8a-hexahydronaphthalen-1-yl 2-methylbutanoate | Aspergillus terreus | IC50 16285.0 nM | 4.79 | 2013 | CHEMBL503 |

### PPARG

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | Mycophenolic acid | Aspergillus, Penicillium roqueforti | Inhibition 74.0 % |  | 2007 | CHEMBL866 |
| 2 | arachidonic acid | Agaricus | Ki 1500.0 nM | 5.82 | 1997 | CHEMBL7594 |
| 3 | (2s)-2-({[(3r)-5-chloro-8-hydroxy-3-methyl-1-oxo-3,4-dihydro-2-benzopyran-7-yl](hydroxy)methylidene}amino)-3-phenylpropa | Aspergillus, Aspergillus niger | Potency 1995.3 nM |  |  | CHEMBL589366 |
| 4 | propylparaben | Cordyceps sinensis, Ophiocordyceps | Potency 5623.4 nM |  |  | CHEMBL194014 |
| 5 | genistein | Cordyceps sinensis, Ophiocordyceps | Potency 10000.0 nM |  |  | CHEMBL44 |

### NRF2

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | β-ara c | Boletus | Potency 231.1 nM |  |  | CHEMBL803 |
| 2 | cytidine | Boletus | Potency 231.1 nM |  |  | CHEMBL803 |
| 3 | 2-(2-hydroxy-4-iminopyrimidin-1-yl)-5-(hydroxymethyl)oxolane-3,4-diol | Boletus | Potency 231.1 nM |  |  | CHEMBL803 |
| 4 | 6-[2-(3,4-dihydroxyphenyl)ethenyl]-4-hydroxypyran-2-one | Inonotus, Phellinus, Polyporus | Potency 16360.1 nM |  |  | CHEMBL1224512 |
| 5 | Hispidin | Polyporus, Inonotus, Phellinus | Potency 16360.1 nM |  |  | CHEMBL1224512 |

### OAT1

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | Ellagic acid | Penicillium, Phellinus | IC50 270.0 nM | 6.57 | 2005 | CHEMBL6246 |
| 2 | Octanoic acid | Ganoderma lucidum, Ganoderma, Ganoderma lucidum | Ki 5410.0 nM | 5.27 | 2001 | CHEMBL324846 |
| 3 | salicyclic acid | Cordyceps sinensis, Ophiocordyceps | IC50 280000.0 nM |  | 2000 | CHEMBL424 |

### OAT3

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | Octanoic acid | Ganoderma lucidum, Ganoderma, Ganoderma lucidum | Ki 8600.0 nM | 5.07 | 2001 | CHEMBL324846 |
| 2 | 6-[(1-hydroxy-2-phenylethylidene)amino]-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylic acid | Penicillium chrysogenum | Ki 97600.0 nM | 4.01 | 2002 | CHEMBL29 |
| 3 | (2s,5r,6r)-6-[(1-hydroxy-2-phenylethylidene)amino]-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylic aci | Penicillium chrysogenum | Ki 97600.0 nM | 4.01 | 2002 | CHEMBL29 |
| 4 | salicyclic acid | Cordyceps sinensis, Ophiocordyceps | Ki 1020000.0 nM |  | 2002 | CHEMBL424 |
| 5 | 6-aminopenicillanic acid | Penicillium, Penicillium chrysogenum | Inhibition |  | 2013 | CHEMBL1236749 |

### ADA

| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |
|---:|---|---|---|---|---|---|
| 1 | (2s,3r,4s,5s)-2-(hydroxymethyl)-5-(purin-9-yl)oxolane-3,4-diol | Phellinus | Ki 7000.0 nM | 5.16 | 2011 | CHEMBL1399702 |
| 2 | purine nucleoside | Phellinus | Ki 7000.0 nM | 5.16 | 2011 | CHEMBL1399702 |
| 3 | adenosine | Cordyceps, Cordyceps sinensis, Ganoderma | Ki 2180000.0 nM |  | 1993 | CHEMBL477 |
| 4 | adenosine | Cordyceps sinensis, Ophiocordyceps | Ki 2180000.0 nM |  | 1993 | CHEMBL477 |
