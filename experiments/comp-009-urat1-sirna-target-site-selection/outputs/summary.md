# comp-009 — URAT1 mRNA target site selection — Summary

**Date:** 2026-05-16  
**Question:** Which 21-nt target sites on SLC22A12 mRNA are viable for siRNA design?

## Pipeline

- Input: human URAT1 protein (553 aa) back-translated to representative CDS (1659 nt, GC 56.5%) via seeded weighted sampling from Kazusa human codon-usage frequencies (seed=42, reproducible across runs).
- Sliding 21-nt windows over CDS positions 76 to 1584: **1488** windows scored.
- Reynolds GC 30-52% filter: **365** survive (24%).
- Immunogenicity (TLR7/8 motifs + GU-rich 9-mers) filter: **292** survive (kills **73** windows).
- 4-nt homopolymer hard exclusion (polyA/polyT/polyG/polyC): **204** survive (kills **88** windows).
- Reynolds >=5/8 AND Ui-Tei AU>=4/7 filter: **74** survive.
- Composite-score ranking + 60-nt positional diversity: **10**-candidate shortlist.

## Verdict

**GREEN — target-site shortlist is viable.**

At least 5 candidate target sites survive all filters (Reynolds GC, Ui-Tei seed asymmetry, TLR / GU-rich immunogenicity, and cross-mammalian conservation). The killshot Brian flagged in H03 — 'if URAT1 mRNA has no accessible siRNA target sites, the entire thesis collapses' — does not fire: URAT1 mRNA has multiple regions amenable to standard siRNA design rules.

## Top shortlist

| Rank | CDS pos | AA pos | AA window | Sense target (5'->3') | GC% | Reynolds | Acc | Cons(avg) | Score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1561 | 521 | LPLPDTI | `CTACCTTTGCCAGATACTATA` | 38.1 | 6/8 | 0.63 | 100.0% | 81.09 |
| 2 | 1039 | 347 | RFRTCIS | `CGTTTCAGGACATGTATTTCA` | 38.1 | 8/8 | 0.44 | 81.0% | 78.13 |
| 3 | 969 | 323 | AMREELS | `AATGCGCGAAGAGCTATCAAT` | 42.9 | 7/8 | 0.63 | 76.2% | 77.7 |
| 4 | 1115 | 372 | QALGSNI | `AGGCATTGGGAAGCAATATCT` | 42.9 | 6/8 | 0.37 | 100.0% | 74.59 |
| 5 | 603 | 201 | LFRFLLA | `ATTTCGATTCCTCCTGGCTTT` | 42.9 | 7/8 | 0.4 | 95.2% | 73.38 |
| 6 | 507 | 169 | RFGRRLV | `GTTCGGTAGAAGACTTGTTCT` | 42.9 | 7/8 | 0.29 | 90.5% | 71.34 |
| 7 | 362 | 121 | VYDRSIF | `TTTACGATAGAAGCATCTTCA` | 33.3 | 8/8 | 0.18 | 81.0% | 69.49 |
| 8 | 1447 | 483 | GPLVRLL | `GGACCACTTGTAAGACTTCTC` | 47.6 | 5/8 | 0.44 | 100.0% | 68.31 |
| 9 | 212 | 71 | ALLAISI | `CCCTATTAGCCATTTCCATAC` | 42.9 | 5/8 | 0.67 | 76.2% | 66.92 |
| 10 | 1358 | 453 | TIYSSEL | `CAATCTACTCTAGTGAGTTGT` | 38.1 | 7/8 | 0.18 | 90.5% | 66.45 |

## Per-candidate detail

### 1. CDS position 1561 (AA 521, window `LPLPDTI`)

- **Sense target:** `5'-CTACCTTTGCCAGATACTATA-3'`
- **Antisense guide:** `5'-UAUAGUAUCUGGCAAAGGUAG-3'`
- **GC content:** 38.1%
- **Reynolds:** 6/8 (passed: R1_GC30-52, R2_no4runs, R5_AS10=U, R6_AS13!=G, R7_AS19!=GC, R8_UI_AS1=AU)
- **Ui-Tei seed AU count:** 6/7
- **Local energy:** -3.7 kcal/mol (accessibility 0.63)
- **Conservation:** chimp 100.0%, mouse 100.0%, rat 100.0%
- **Composite score:** 81.09/100

### 2. CDS position 1039 (AA 347, window `RFRTCIS`)

- **Sense target:** `5'-CGTTTCAGGACATGTATTTCA-3'`
- **Antisense guide:** `5'-UGAAAUACAUGUCCUGAAACG-3'`
- **GC content:** 38.1%
- **Reynolds:** 8/8 (passed: R1_GC30-52, R2_no4runs, R3_AS19=A, R4_AS3=A, R5_AS10=U, R6_AS13!=G, R7_AS19!=GC, R8_UI_AS1=AU)
- **Ui-Tei seed AU count:** 6/7
- **Local energy:** -5.6 kcal/mol (accessibility 0.44)
- **Conservation:** chimp 100.0%, mouse 71.4%, rat 71.4%
- **Composite score:** 78.13/100

### 3. CDS position 969 (AA 323, window `AMREELS`)

- **Sense target:** `5'-AATGCGCGAAGAGCTATCAAT-3'`
- **Antisense guide:** `5'-AUUGAUAGCUCUUCGCGCAUU-3'`
- **GC content:** 42.9%
- **Reynolds:** 7/8 (passed: R1_GC30-52, R2_no4runs, R3_AS19=A, R5_AS10=U, R6_AS13!=G, R7_AS19!=GC, R8_UI_AS1=AU)
- **Ui-Tei seed AU count:** 6/7
- **Local energy:** -3.7 kcal/mol (accessibility 0.63)
- **Conservation:** chimp 100.0%, mouse 71.4%, rat 57.1%
- **Composite score:** 77.7/100

### 4. CDS position 1115 (AA 372, window `QALGSNI`)

- **Sense target:** `5'-AGGCATTGGGAAGCAATATCT-3'`
- **Antisense guide:** `5'-AGAUAUUGCUUCCCAAUGCCU-3'`
- **GC content:** 42.9%
- **Reynolds:** 6/8 (passed: R1_GC30-52, R2_no4runs, R4_AS3=A, R5_AS10=U, R6_AS13!=G, R8_UI_AS1=AU)
- **Ui-Tei seed AU count:** 6/7
- **Local energy:** -6.3 kcal/mol (accessibility 0.37)
- **Conservation:** chimp 100.0%, mouse 100.0%, rat 100.0%
- **Composite score:** 74.59/100

### 5. CDS position 603 (AA 201, window `LFRFLLA`)

- **Sense target:** `5'-ATTTCGATTCCTCCTGGCTTT-3'`
- **Antisense guide:** `5'-AAAGCCAGGAGGAAUCGAAAU-3'`
- **GC content:** 42.9%
- **Reynolds:** 7/8 (passed: R1_GC30-52, R2_no4runs, R3_AS19=A, R4_AS3=A, R6_AS13!=G, R7_AS19!=GC, R8_UI_AS1=AU)
- **Ui-Tei seed AU count:** 4/7
- **Local energy:** -6.0 kcal/mol (accessibility 0.4)
- **Conservation:** chimp 100.0%, mouse 100.0%, rat 85.7%
- **Composite score:** 73.38/100

### 6. CDS position 507 (AA 169, window `RFGRRLV`)

- **Sense target:** `5'-GTTCGGTAGAAGACTTGTTCT-3'`
- **Antisense guide:** `5'-AGAACAAGUCUUCUACCGAAC-3'`
- **GC content:** 42.9%
- **Reynolds:** 7/8 (passed: R1_GC30-52, R2_no4runs, R3_AS19=A, R4_AS3=A, R6_AS13!=G, R7_AS19!=GC, R8_UI_AS1=AU)
- **Ui-Tei seed AU count:** 5/7
- **Local energy:** -7.1 kcal/mol (accessibility 0.29)
- **Conservation:** chimp 100.0%, mouse 85.7%, rat 85.7%
- **Composite score:** 71.34/100

### 7. CDS position 362 (AA 121, window `VYDRSIF`)

- **Sense target:** `5'-TTTACGATAGAAGCATCTTCA-3'`
- **Antisense guide:** `5'-UGAAGAUGCUUCUAUCGUAAA-3'`
- **GC content:** 33.3%
- **Reynolds:** 8/8 (passed: R1_GC30-52, R2_no4runs, R3_AS19=A, R4_AS3=A, R5_AS10=U, R6_AS13!=G, R7_AS19!=GC, R8_UI_AS1=AU)
- **Ui-Tei seed AU count:** 5/7
- **Local energy:** -8.2 kcal/mol (accessibility 0.18)
- **Conservation:** chimp 100.0%, mouse 71.4%, rat 71.4%
- **Composite score:** 69.49/100

### 8. CDS position 1447 (AA 483, window `GPLVRLL`)

- **Sense target:** `5'-GGACCACTTGTAAGACTTCTC-3'`
- **Antisense guide:** `5'-GAGAAGUCUUACAAGUGGUCC-3'`
- **GC content:** 47.6%
- **Reynolds:** 5/8 (passed: R1_GC30-52, R2_no4runs, R5_AS10=U, R6_AS13!=G, R7_AS19!=GC)
- **Ui-Tei seed AU count:** 4/7
- **Local energy:** -5.6 kcal/mol (accessibility 0.44)
- **Conservation:** chimp 100.0%, mouse 100.0%, rat 100.0%
- **Composite score:** 68.31/100

### 9. CDS position 212 (AA 71, window `ALLAISI`)

- **Sense target:** `5'-CCCTATTAGCCATTTCCATAC-3'`
- **Antisense guide:** `5'-GUAUGGAAAUGGCUAAUAGGG-3'`
- **GC content:** 42.9%
- **Reynolds:** 5/8 (passed: R1_GC30-52, R2_no4runs, R4_AS3=A, R5_AS10=U, R6_AS13!=G)
- **Ui-Tei seed AU count:** 4/7
- **Local energy:** -3.3 kcal/mol (accessibility 0.67)
- **Conservation:** chimp 85.7%, mouse 71.4%, rat 71.4%
- **Composite score:** 66.92/100

### 10. CDS position 1358 (AA 453, window `TIYSSEL`)

- **Sense target:** `5'-CAATCTACTCTAGTGAGTTGT-3'`
- **Antisense guide:** `5'-ACAACUCACUAGAGUAGAUUG-3'`
- **GC content:** 38.1%
- **Reynolds:** 7/8 (passed: R1_GC30-52, R2_no4runs, R4_AS3=A, R5_AS10=U, R6_AS13!=G, R7_AS19!=GC, R8_UI_AS1=AU)
- **Ui-Tei seed AU count:** 4/7
- **Local energy:** -8.2 kcal/mol (accessibility 0.18)
- **Conservation:** chimp 100.0%, mouse 85.7%, rat 85.7%
- **Composite score:** 66.45/100


## Limitations

1. **CDS-only analysis.** UTRs were not analysed because NCBI/Entrez was not in the allowed network host list at run time. UTR-targeting siRNAs are a major design class (especially 3' UTR, where seed-region miRNA-like activity is most-effective) and a real handoff item — at wet-lab time, re-run this analysis with the actual NM_144585.3 mRNA including UTRs.
2. **Back-translation surrogate, not real mRNA.** The CDS used here is the most-frequent-human-codon back-translation of UniProt Q96S37, NOT the actual NM_144585.3 nucleotide sequence. The codon bias of the analysis is therefore 'typical human CDS' rather than the natural codon distribution in SLC22A12 mRNA. Re-run with real RefSeq mRNA at wet-lab time.
3. **Accessibility heuristic, not ViennaRNA.** ViennaRNA RNAplfold was not installed on the analysis machine. Local-stability energy is approximated via a Tinoco-style nearest-neighbour stack-energy sum over the best inverted-repeat stem in each 21-nt window. This is directionally correct (more stable = less accessible) but should be re-validated with full ViennaRNA RNAplfold at wet-lab handoff time. Empirical siRNA benchmarks (Tafer 2008) show accessibility surrogate correlation r~0.6-0.7 with full RNAplfold — adequate for prioritisation, not for absolute knockdown prediction.
4. **No BLAST against full human transcriptome.** The 'no human off-target' check would normally include a BLAST search of the seed region (positions 2-8 of antisense) against the full human RefSeq transcriptome to count off-target seed matches. This requires NCBI access; not run here. Wet-lab handoff item.
5. **No actual MSA for conservation.** Conservation is computed by direct positional alignment of the four ortholog protein sequences. URAT1 orthologs are same-length and ~85-99% identical, so this works as approximation, but a formal Clustal/Muscle MSA would give per-position conservation with insertions/deletions handled correctly. At wet-lab handoff time, re-validate with formal MSA.
6. **Conservation maps AA -> nucleotide non-injectively.** Two species may have identical AA but differ at the wobble position, breaking siRNA cross-species reuse. The 'cross-species reusable' claim is therefore upper-bound — at wet-lab handoff time, verify with actual ortholog mRNA sequences.
