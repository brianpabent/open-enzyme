# comp-034 — Lactoferrin inter-lobe linker redesign pilot — summary

- **Target**: Human lactoferrin (UniProt P02788), inter-lobe linker, residues 353-363 (UniProt) / 334-344 (mature)
- **WT linker**: `SEEEVAARRAR` (11 aa)
- **WT linker pLDDT (AF, mean)**: 95.61
- **Candidates evaluated**: 60 (59 redesigns + WT control)
- **Concordance gate**: N-of-5 ≥ 3 (GREEN) / N-of-5 = 5 (STRICT)
- **GREEN count**: 15 (25.0%)
- **STRICT count**: 0 (0.0%)

## Metric cutoffs (top-quintile thresholds)

- `esm2_pseudo_plddt`: higher-is-better, top-quintile cutoff = 93.810
- `linker_cleavage_score`: lower-is-better, top-quintile cutoff = 0.039
- `cai_a_oryzae`: higher-is-better, top-quintile cutoff = 20.472
- `seq_similarity_to_wt`: higher-is-better, top-quintile cutoff = 0.364
- `linker_loop_plddt`: banded, must be inside [60.0, 90.0]

## WT control

- WT linker `SEEEVAARRAR` passes 3/5 metrics (GREEN)
  - esm2_pseudo_plddt: PASS
  - linker_cleavage_score: FAIL
  - cai_a_oryzae: PASS
  - linker_loop_plddt: FAIL
  - seq_similarity_to_wt: PASS

## Top-10 GREEN candidates (ranked: cleavage asc, ESM2 desc, similarity desc)

| Rank | Linker | N-of-5 | Tier | ESM2 pseudo-pLDDT | Cleavage | CAI | Loop pLDDT | Sim. to WT |
|---|---|---|---|---|---|---|---|---|
| 1 | `EEEQPQEQRHR` | 3/5 | GREEN | 93.81 | 0.077 | 18.10 | 79.6 | 0.36 |
| 2 | `EEEEPQQDNAP` | 3/5 | GREEN | 93.78 | 0.097 | 20.47 | 77.6 | 0.36 |
| 3 | `PEEEPPAEQED` | 3/5 | GREEN | 93.67 | 0.117 | 21.17 | 70.6 | 0.36 |
| 4 | `EEEEVPPPRPR` | 3/5 | GREEN | 93.89 | 0.155 | 19.30 | 67.6 | 0.55 |
| 5 | `DEEDPANPQAH` | 3/5 | GREEN | 93.82 | 0.155 | 20.44 | 80.6 | 0.36 |
| 6 | `QEENNHAQDAH` | 3/5 | GREEN | 93.88 | 0.175 | 19.18 | 84.6 | 0.36 |
| 7 | `SEHNQAAHPDN` | 3/5 | GREEN | 93.83 | 0.194 | 18.99 | 81.1 | 0.36 |
| 8 | `EEEEPAAPPAP` | 4/5 | GREEN | 93.89 | 0.233 | 22.31 | 67.6 | 0.55 |
| 9 | `PEEEPAAPPAP` | 3/5 | GREEN | 93.79 | 0.233 | 21.97 | 60.6 | 0.55 |
| 10 | `EEEEPAARRAR` | 4/5 | GREEN | 94.64 | 0.290 | 20.90 | 89.6 | 0.82 |

## Methodology audit notes

Per BioDesignBench (Kim & Romero 2026; see `wiki/etc/bio-ai-tools.md` §BioDesignBench):
- **Multi-candidate**: YES, 60 unique candidates evaluated head-to-head
- **Multi-metric**: YES, 5 orthogonal axes (fold-quality, cleavage, codon usage, loop flexibility, conservation)
- **Head-to-head comparison**: YES, all candidates ranked against each other on each metric
- **Explicit filter step**: YES, N-of-5 ≥ 3 concordance gate + tier reporting

### ProteinMPNN substitution flag

Per the analyze.py module docstring: candidate generation uses a structure-conditioned
biased sampler (permitted-residue-pool + WT-mix-in + proline-boost at ALP-hot positions)
rather than full ProteinMPNN. The MCP wrapper loads on this host but the external ProteinMPNN
scripts at /opt/ProteinMPNN are not present (auto-mode classifier blocked the clone). When
ProteinMPNN is installed, the same candidate set can be regenerated with the genuine MPNN
sampler and the rest of the pipeline (scoring + concordance) is unchanged.