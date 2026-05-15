---
title: "comp-030: DAF/CD55 SCR1-4 Cassette Ranking (ClockBase-Style)"
date: 2026-05-15
experiment_id: comp-030
target: "DAF/CD55 SCR1-4 truncated construct (aa 35-285, UniProt P08174)"
host: "Aspergillus oryzae"
author: "Open Enzyme (claude/sonnet-4-6 via Agent tool, walkthrough Item 29)"
status: "complete"
---

# comp-030: DAF/CD55 SCR1-4 Cassette Ranking

## What this experiment is

Exhaustive ClockBase-style combinatorial ranking of *A. oryzae* expression cassette designs for
the DAF/CD55 SCR1-4 truncated construct (amino acids 35–285 of UniProt P08174; 251 residues,
8 disulfide bonds — verified against UniProt DISULFID feature annotations 2026-05-15).

Mirrors comp-022 v2 (uricase cassette ranking) methodology, with two upgrades applied from
the start:
1. **Real ViennaRNA 2.7.2 MFE** (no GC-clamp proxy; comp-022 v1 proxy had Spearman rho = 0.241)
2. **ESM2 t33 650M pseudo-pLDDT** (ESMFold v1 authorized fallback; same as comp-022 v2)

## What this experiment decides

1. Whether the §1.25 baseline cassette design (PamyB + amyB SP + direct secretion) is the
   optimal architecture, or whether the exhaustive ranking surfaces a better-scored alternative.

2. An empirical check on the `chaperone-orthogonal-stacking.md` §3.5.2 prediction that CCP/SCR
   architecture has α = 0.3–0.6 (low PDI load coefficient). The ESM2 pLDDT distribution across
   the 720 protein-distinct candidate space provides in silico evidence for/against fast/robust
   folding of the SCR domains.

## Design space

| Axis | Count | Values |
|------|-------|--------|
| Promoters | 6 | PamyB, PglaA, PenoA, PgpdA, PtefI, PnmtA |
| Signal peptides | 12 | amyB, amyB_pro, glaA, glaA_pro, pepO, pepO_pro, alpA, alpA_pro, lipase, lipase_pro, cbhI, cbhI_pro |
| Codon variants | 10 | native_daf, cai_max, cai_balanced, cai_max_gc54, harmonized, rare_avoid, low_gc, high_gc, 5p_softened, 5p_softened_balanced |
| Scaffolds | 60 | 10 base × 3 propeptide × 2 N-glyc states |
| **Total** | **43,200** | |

## Five scoring models

| # | Model | Direction | Method |
|---|-------|-----------|--------|
| 1 | CAI | Higher better | Sharp & Li 1987 (PMID 3547335) under A. oryzae codon table |
| 2 | ViennaRNA 2.7.2 MFE | Higher (less negative) better | 150-nt 5' region; Kudla 2009 (PMID 19359587) |
| 3 | Chaperone load | Lower better | 8 disulfides × α=0.45 central (range 0.3–0.6); Schmidt 2010 PMC2806952 |
| 4 | Promoter × SP prior | Higher better | Literature-derived bounded multipliers |
| 5 | ESM2 pseudo-pLDDT | Higher better | ESM2 t33 650M; ESMFold v1 fallback; Verkuil 2022; Hsu 2022 |

Concordance gate: **N-of-5 ≥ 4** (80%), same as comp-022 v2.

## Key source files

| File | Description |
|------|-------------|
| `inputs/P08174_scr14.fasta` | DAF SCR1-4 AA sequence (aa 35-285, 251 aa, 16 Cys) |
| `inputs/a_oryzae_codon_usage.json` | A. oryzae codon usage table (Machida 2005 + Nakao 1992) |
| `inputs/protein_candidates.fasta` | All 720 protein-distinct candidate sequences for ESM2 |
| `inputs/protein_candidates_keymap.csv` | seq_id → (SP, scaffold_base, propeptide, nglyc) mapping |
| `code/analyze.py` | Step 1: design-space enumeration + Models 1-4 scoring + ViennaRNA |
| `code/run_esm2.py` | Step 2: ESM2 pseudo-pLDDT scoring + alpha-coefficient check |
| `code/rerank_final.py` | Step 3: N-of-5 concordance + final ranking |
| `results/all_candidates_scores.csv` | All 43,200 candidate scores (Models 1-4) |
| `results/shortlist_n5ge4.csv` | Candidates passing N-of-5 ≥ 4 |
| `results/shortlist_n5eq5.csv` | Strictest tier (N-of-5 = 5) |
| `results/top25.md` | Top-25 cassette ranking |
| `results/esm2_pseudo_pLDDT.csv` | ESM2 scores for all 720 protein-distinct candidates |
| `results/plddt_distribution.csv` | pLDDT distribution stats (alpha-coefficient check) |
| `results/alpha_coefficient_check.json` | Alpha-coefficient verdict |
| `results/final_summary.json` | Headline numbers |
| `figures/plddt_histogram.tsv` | pLDDT histogram data |
| `provenance.md` | Primary source verification for all load-bearing numbers |

## Reproducibility

```bash
# Use the comp-022 v2 environment (ViennaRNA + ESM2 + torch available):
ENV=/path/to/Open\ Enzyme/experiments/comp-022-clockbase-uricase-cassette-ranking/v2-env/bin/python3
cd experiments/comp-030-daf-cassette-ranking
$ENV code/analyze.py      # Step 1: ~2 min
$ENV code/run_esm2.py     # Step 2: ~5-15 min (CPU; GPU faster)
$ENV code/rerank_final.py  # Step 3: <1 min
```

## Pre-commit verification

All load-bearing numbers verified per CLAUDE.md Rule 4. See `provenance.md`.

## Interpretive wiki page

`wiki/daf-cd55-scr14-cassette-ranking-computational.md`
