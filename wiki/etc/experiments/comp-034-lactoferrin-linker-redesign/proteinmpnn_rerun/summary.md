# comp-034 — Genuine ProteinMPNN rerun — summary

Sampler: ProteinMPNN v_48_020 (Dauparas et al. 2022), temperature=0.1, seed=42, 60 samples/pool.
WT linker: `SEEEVAARRAR` (UniProt 353-363).

## Constrained pool (permitted-AA pool [E,D,N,Q,H,P] enforced via `--omit_AAs`)

- Candidates evaluated: 61 (60 MPNN + 1 WT control)
- WT N-of-5: 3 (GREEN)
- GREEN: 20 (32.8%)
- STRICT: 5 (8.2%)

### Top-10 GREEN (constrained)

| Rank | Linker | N-of-5 | Tier | ESM2 pseudo-pLDDT | Cleavage | CAI | Loop pLDDT | Sim. to WT | MPNN score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `NEEEQEEQDQQ` | 4/5 | GREEN | 93.69 | 0.039 | 19.71 | 81.1 | 0.27 | 2.429 |
| 2 | `NEEEQQQEEEQ` | 5/5 | STRICT | 93.69 | 0.039 | 19.73 | 81.1 | 0.27 | 2.293 |
| 3 | `NEEEQQQQQEQ` | 4/5 | GREEN | 93.69 | 0.039 | 18.83 | 81.1 | 0.27 | 2.162 |
| 4 | `NEEEQQQEEEQ` | 5/5 | STRICT | 93.69 | 0.039 | 19.73 | 81.1 | 0.27 | 2.186 |
| 5 | `NEEEQQQQEEQ` | 4/5 | GREEN | 93.69 | 0.039 | 19.27 | 81.1 | 0.27 | 2.219 |
| 6 | `NEEEQQQQQQQ` | 4/5 | GREEN | 93.69 | 0.039 | 18.40 | 81.1 | 0.27 | 2.079 |
| 7 | `NEEEEQQEQEQ` | 5/5 | STRICT | 93.69 | 0.039 | 19.73 | 81.1 | 0.27 | 2.302 |
| 8 | `NEEEQQQQEQQ` | 4/5 | GREEN | 93.69 | 0.039 | 18.83 | 81.1 | 0.27 | 2.113 |
| 9 | `NEEEQQQEQEQ` | 4/5 | GREEN | 93.69 | 0.039 | 19.27 | 81.1 | 0.27 | 2.289 |
| 10 | `NEEEQQQEEEQ` | 5/5 | STRICT | 93.69 | 0.039 | 19.73 | 81.1 | 0.27 | 2.273 |

## Unconstrained pool (no AA omission — what genuine ProteinMPNN naturally prefers)

- Candidates evaluated: 61 (60 MPNN + 1 WT control)
- WT N-of-5: 2 (FAIL)
- GREEN: 20 (32.8%)
- STRICT: 0 (0.0%)

### Top-10 GREEN (unconstrained)

| Rank | Linker | N-of-5 | Tier | ESM2 | Cleavage | CAI | Loop pLDDT | Sim. WT | MPNN score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `SDEEIAAREQT` | 4/5 | GREEN | 94.22 | 0.330 | 21.66 | 88.6 | 0.55 | 1.105 |
| 2 | `SDEEIAAQQAT` | 4/5 | GREEN | 94.22 | 0.369 | 22.44 | 88.6 | 0.55 | 1.161 |
| 3 | `SAEEIAAREET` | 3/5 | GREEN | 94.20 | 0.388 | 22.68 | 87.1 | 0.55 | 1.072 |
| 4 | `SAEEIAAREET` | 3/5 | GREEN | 94.20 | 0.388 | 22.68 | 87.1 | 0.55 | 1.107 |
| 5 | `SAEEIAAREET` | 3/5 | GREEN | 94.20 | 0.388 | 22.68 | 87.1 | 0.55 | 1.111 |
| 6 | `SAEEIAAREAT` | 3/5 | GREEN | 94.36 | 0.466 | 23.17 | 89.1 | 0.64 | 1.059 |
| 7 | `SAEEIAAREAT` | 3/5 | GREEN | 94.36 | 0.466 | 23.17 | 89.1 | 0.64 | 1.029 |
| 8 | `SAEEIAAREAT` | 3/5 | GREEN | 94.36 | 0.466 | 23.17 | 89.1 | 0.64 | 1.083 |
| 9 | `SAEEIAAREAT` | 3/5 | GREEN | 94.36 | 0.466 | 23.17 | 89.1 | 0.64 | 1.030 |
| 10 | `SDAEIAARQAT` | 3/5 | GREEN | 94.22 | 0.466 | 22.62 | 88.6 | 0.55 | 1.053 |

## Comparison vs substitute sampler

- Substitute sampler GREEN set: 15 sequences
- Sequence overlap with constrained MPNN pool: 1
- Sequence overlap with unconstrained MPNN pool: 1

### Substitute-GREEN re-evaluated in constrained MPNN pool cutoffs

| Linker (substitute GREEN) | N-of-5 (in MPNN pool) | Tier | Notes |
|---|---|---|---|
| `EEEQPQEQRHR` | 3/5 | GREEN | failing metrics: linker_cleavage_score, cai_a_oryzae |
| `EEEEPQQDNAP` | 4/5 | GREEN | failing metrics: linker_cleavage_score |
| `PEEEPPAEQED` | 3/5 | GREEN | failing metrics: esm2_pseudo_plddt, linker_cleavage_score |
| `EEEEVPPPRPR` | 3/5 | GREEN | failing metrics: linker_cleavage_score, cai_a_oryzae |
| `DEEDPANPQAH` | 4/5 | GREEN | failing metrics: linker_cleavage_score |
| `QEENNHAQDAH` | 3/5 | GREEN | failing metrics: linker_cleavage_score, cai_a_oryzae |
| `SEHNQAAHPDN` | 3/5 | GREEN | failing metrics: linker_cleavage_score, cai_a_oryzae |
| `EEEEPAAPPAP` | 4/5 | GREEN | failing metrics: linker_cleavage_score |
| `PEEEPAAPPAP` | 4/5 | GREEN | failing metrics: linker_cleavage_score |
| `EEEEPAARRAR` | 4/5 | GREEN | failing metrics: linker_cleavage_score |
| `SEEEPAARRAR` | 3/5 | GREEN | failing metrics: linker_cleavage_score, linker_loop_plddt |
| `SEEEVAAPPPR` | 4/5 | GREEN | failing metrics: linker_cleavage_score |
| `SEEEVAAPPAR` | 4/5 | GREEN | failing metrics: linker_cleavage_score |
| `EEEEVAARRAR` | 3/5 | GREEN | failing metrics: linker_cleavage_score, linker_loop_plddt |
| `SEEEVAARRAR` | 3/5 | GREEN | failing metrics: linker_cleavage_score, linker_loop_plddt |

### Substitute-GREEN re-evaluated in unconstrained MPNN pool cutoffs

| Linker (substitute GREEN) | N-of-5 | Tier | Notes |
|---|---|---|---|
| `EEEQPQEQRHR` | 2/5 | FAIL | failing metrics: esm2_pseudo_plddt, cai_a_oryzae, seq_similarity_to_wt |
| `EEEEPQQDNAP` | 2/5 | FAIL | failing metrics: esm2_pseudo_plddt, cai_a_oryzae, seq_similarity_to_wt |
| `PEEEPPAEQED` | 2/5 | FAIL | failing metrics: esm2_pseudo_plddt, cai_a_oryzae, seq_similarity_to_wt |
| `EEEEVPPPRPR` | 3/5 | GREEN | failing metrics: esm2_pseudo_plddt, cai_a_oryzae |
| `DEEDPANPQAH` | 2/5 | FAIL | failing metrics: esm2_pseudo_plddt, cai_a_oryzae, seq_similarity_to_wt |
| `QEENNHAQDAH` | 2/5 | FAIL | failing metrics: esm2_pseudo_plddt, cai_a_oryzae, seq_similarity_to_wt |
| `SEHNQAAHPDN` | 2/5 | FAIL | failing metrics: esm2_pseudo_plddt, cai_a_oryzae, seq_similarity_to_wt |
| `EEEEPAAPPAP` | 3/5 | GREEN | failing metrics: esm2_pseudo_plddt, cai_a_oryzae |
| `PEEEPAAPPAP` | 3/5 | GREEN | failing metrics: esm2_pseudo_plddt, cai_a_oryzae |
| `EEEEPAARRAR` | 4/5 | GREEN | failing metrics: cai_a_oryzae |
| `SEEEPAARRAR` | 3/5 | GREEN | failing metrics: cai_a_oryzae, linker_loop_plddt |
| `SEEEVAAPPPR` | 4/5 | GREEN | failing metrics: cai_a_oryzae |
| `SEEEVAAPPAR` | 4/5 | GREEN | failing metrics: cai_a_oryzae |
| `EEEEVAARRAR` | 3/5 | GREEN | failing metrics: cai_a_oryzae, linker_loop_plddt |
| `SEEEVAARRAR` | 2/5 | FAIL | failing metrics: linker_cleavage_score, cai_a_oryzae, linker_loop_plddt |