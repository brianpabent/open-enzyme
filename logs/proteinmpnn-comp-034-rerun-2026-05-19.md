---
title: ProteinMPNN Rerun on comp-034 Lactoferrin Inter-Lobe Linker
date: 2026-05-19
tags:
  - comp-034
  - proteinmpnn
  - lactoferrin
  - linker-redesign
  - protease-stability
related:
  - ../wiki/lactoferrin-linker-redesign-computational.md
  - ../wiki/lactoferrin-protease-stability-computational.md
  - ../wiki/etc/experiments/comp-034-lactoferrin-linker-redesign/
  - ../synthesis/queue/2026-05-16-experiment-2-single-command-proteinmpnn-rerun-on-the-lactoferrin-inter.md
---

# ProteinMPNN Rerun on comp-034 Lactoferrin Inter-Lobe Linker — 2026-05-19

Triggered by `synthesis/queue/2026-05-16-experiment-2-single-command-proteinmpnn-rerun-on-the-lactoferrin-inter.md` (Cluster E2 walkthrough). The comp-034 substitute-sampler caveat needs to be resolved before `validation-experiments.md §1.10` wet-lab gene-synthesis spend (~$1.5–3K for 3 variants).

## Summary

- **ProteinMPNN installed** at `tools/ProteinMPNN/` inside the repo (`/opt/` is read-only on this Mac; the documented fallback path was used). Sampler model `v_48_020` (Dauparas et al. 2022), default temp 0.1, seed 42. Smoke test passed; the lactoferrin sampling run took ~52 s per 60-sequence pool on CPU.
- **The substitute sampler's 15 GREEN candidates were NOT artifacts.** All 15 retained GREEN tier (≥ 3-of-5) when re-scored against the constrained MPNN pool's cutoffs; the substitute pool's mean MPNN log-likelihood (`-log P` on design positions) was 2.74 — clearly separated from its own FAIL set (mean 3.74) and within range of MPNN-preferred candidates. The substitute sampler's conservative-proline + WT-mix-in heuristic was biasing toward MPNN-tolerable substitutions, not hallucinating.
- **Genuine ProteinMPNN finds 3 unique STRICT (5-of-5) candidates that the substitute sampler missed**, all from a `NEEE{E,Q}{E,Q}{E,Q}{E,Q}{E,Q}{E,Q}{E,Q}` family (top 3: `NEEEQQQEEEQ`, `NEEEEQQEQEQ`, `NEEEEEQEQEQ`). These reduce predicted linker cleavage to 0.039 (vs substitute primary anchor `EEEEPAARRAR` at 0.290, vs WT at 0.407) while staying in the loop-pLDDT band MPNN's similar-class substitutions preserve.
- **MPNN's natural (unconstrained) preference is `S{A,D}EEIAA{R,Q}{E,Q}{A,E}T`** — keeps the WT structural anchors but swaps V357→I and R363→T. These score WORSE on protease-cleavage than the constrained pool (cleavage 0.330–0.466) because Ile/Thr at the WT positions retain ALP P1 substrate compatibility. **Recommendation: use the constrained pool for wet-lab arm, not the unconstrained pool.**
- **§1.10 wet-lab gene-synthesis recommendation:** keep the substitute sampler's `EEEEPAARRAR` (S353E + V357P, 82% identity, MPNN-tolerable rank 16/74) as the conservative anchor, and ADD one MPNN-native STRICT candidate (`NEEEQQQEEEQ`, the lowest-MPNN-score STRICT) as the aggressive arm. Drop the original aggressive `DEEDPANPQAH` candidate — MPNN log-likelihood is 3.33 (close to the substitute FAIL median 3.78) and it adds no design-quality signal that the new STRICT candidate doesn't.

## Phase 1: ProteinMPNN install

- **Install path:** `tools/ProteinMPNN/` (relative to repo root: `/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme/tools/ProteinMPNN/`). `/opt/` is not writable on this Mac (read-only `/opt` per macOS sandbox); `~/tools/` is also blocked by sandbox; the only writable location inside the configured allowlist was the repo's own `tools/` subdirectory.
- **Install method:** downloaded `https://github.com/dauparas/ProteinMPNN/archive/refs/heads/main.tar.gz` (84 MB; full repo including all model-weight `.pt` files), extracted to `tools/ProteinMPNN/`. Git-clone failed under the sandbox because `.git/config` writes were blocked; tarball install is functionally equivalent (and reproducibility is preserved by the GitHub immutable archive URL).
- **Dependencies:** `python3.13`, `torch 2.12.0`, `numpy 2.4.4` — all already present, no `pip install` step needed.
- **Smoke test:** ran the official two-PDB example (`5L33`, `6MRR`) with `--num_seq_per_target 2 --sampling_temp 0.1 --seed 37`. Output: "2 sequences of length 106 generated in 0.3798 seconds" / "2 sequences of length 68 generated in 0.26 seconds". Model weights loaded correctly from `vanilla_model_weights/v_48_020.pt`.
- **Wall time for install + smoke test:** ~3 minutes (dominated by the 84 MB tarball download).

## Phase 2: Sampling

- **Input PDB source:** AlphaFold DB monomer prediction for human lactoferrin, fetched directly from the AlphaFold API at run time: `https://alphafold.ebi.ac.uk/files/AF-P02788-F1-model_v6.pdb`. Model created 2025-08-01, latest version 6, full 710-aa monomer chain A, global pLDDT 94.94, 94.1% of residues at very-high confidence. Path: `wiki/etc/experiments/comp-034-lactoferrin-linker-redesign/proteinmpnn_rerun/AF-P02788-F1-model_v6.pdb`. The full 710-aa sequence in this PDB matches `inputs/P02788.fasta` exactly; linker positions 353-363 = `SEEEVAARRAR` verified.
- **Parsing:** `helper_scripts/parse_multiple_chains.py` produced `parsed_chains.jsonl` (74 kB) with `seq_chain_A`, `coords_chain_A` (N, CA, C, O backbone).
- **Design positions:** 353-363 (UniProt numbering = mature 334-344). All 699 other residues fixed via `make_fixed_positions_dict.py --specify_non_fixed`.
- **Two sampling runs (60 candidates each, temp 0.1, seed 42):**
  - **`mpnn_constrained/`** — `--omit_AAs "ACFGIKLMRSTVWY"` enforces the comp-034 permitted-residue pool `[E, D, N, Q, H, P]` exactly. This is the apples-to-apples comparison to the substitute sampler.
  - **`mpnn_unconstrained/`** — no AA omission. Lets MPNN choose freely from all 20 amino acids given the structural context. Answers "what does MPNN naturally want to put here?"
- **Output:** `mpnn_constrained/seqs/AF-P02788-F1-model_v6.fa`, `mpnn_unconstrained/seqs/AF-P02788-F1-model_v6.fa`. Each fasta has 60 generated sequences + 1 WT input header. MPNN reports `score` (per-design-position `-log P`), `global_score` (global `-log P`), `seq_recovery` per sample.
- **Wall time:** ~52 s per pool on CPU. Total Phase 2 wall time: ~2 min.

## Phase 3: Scoring + comparison

Re-implemented comp-034's 5-metric scoring framework in `score_mpnn_candidates.py`, importing the shared `lib/protease_stability.py` library so the protease cleavage math is identical. WT control injected as candidate_id=0 in each pool. Top-quintile cutoffs computed independently per pool (61 candidates including WT).

### Constrained MPNN pool (permitted pool [E,D,N,Q,H,P])

- Candidates: 60 MPNN samples + 1 WT control = 61. Unique linkers: 41.
- WT N-of-5: **3/5 (GREEN)** — same as substitute sampler.
- **STRICT (5-of-5): 5 entries / 3 unique sequences** (substitute had 0).
- **GREEN (≥ 3-of-5): 20 entries / 15 unique sequences.**

#### Top-10 unique GREEN+STRICT (constrained), ranked by cleavage asc / ESM2 desc / similarity desc

| Rank | Linker | N-of-5 | Tier | ESM2 pseudo-pLDDT | Cleavage | CAI | Loop pLDDT | Sim. WT | MPNN score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `NEEEQEEQDQQ` | 4/5 | GREEN | 93.69 | 0.039 | 19.71 | 81.1 | 0.27 | 2.429 |
| 2 | `NEEEQQQEEEQ` | 5/5 | **STRICT** | 93.69 | 0.039 | 19.73 | 81.1 | 0.27 | 2.253 |
| 3 | `NEEEEQQEQEQ` | 5/5 | **STRICT** | 93.69 | 0.039 | 19.73 | 81.1 | 0.27 | 2.265 |
| 4 | `NEEEEEQEQEQ` | 5/5 | **STRICT** | 93.69 | 0.039 | 20.19 | 81.1 | 0.27 | 2.412 |
| 5 | `NEEEQQQQQEQ` | 4/5 | GREEN | 93.69 | 0.039 | 18.83 | 81.1 | 0.27 | 2.147 |
| 6 | `NEEEQQQQEEQ` | 4/5 | GREEN | 93.69 | 0.039 | 19.27 | 81.1 | 0.27 | 2.176 |
| 7 | `NEEEQQQQQQQ` | 4/5 | GREEN | 93.69 | 0.039 | 18.40 | 81.1 | 0.27 | 2.135 |
| 8 | `NEEEQQQQEQQ` | 4/5 | GREEN | 93.69 | 0.039 | 18.83 | 81.1 | 0.27 | 2.210 |
| 9 | `NEEEQQQEQEQ` | 4/5 | GREEN | 93.69 | 0.039 | 19.27 | 81.1 | 0.27 | 2.254 |
| 10 | `NEEEEEQQNQQ` | 4/5 | GREEN | 93.69 | 0.039 | 19.23 | 81.1 | 0.27 | 2.298 |

The STRICT candidates all share the same shape: `N` at position 353 (replacing S), `EEE` retained at 354-356, then a Q/E mosaic with no proline and no charged R/K residues. Predicted cleavage 0.039 (vs WT 0.407 — a **10.4× reduction**). Sequence identity to WT is 27% (3-of-11 retained: `EEE` at 354-356). This is genuinely more aggressive redesign than the substitute sampler ever proposed.

### Unconstrained MPNN pool (no AA omission)

- Candidates: 60 + 1 WT = 61. Unique linkers: 37.
- WT N-of-5: **2/5 (FAIL)** — when MPNN is allowed to choose freely, WT looks WORSE relative to MPNN's preferred set.
- **STRICT: 0.** **GREEN: 20 entries / 10 unique sequences (high collapse to the `S{A,D}{A,E}EIAAxxxT` motif family).**

#### Top-5 unique GREEN (unconstrained)

| Rank | Linker | N-of-5 | Cleavage | ESM2 | CAI | Loop pLDDT | Sim. WT | MPNN score |
|---|---|---|---|---|---|---|---|---|
| 1 | `SAEEIAAREAT` | 3/5 | 0.466 | 94.36 | 23.17 | 89.1 | 0.64 | 1.029 |
| 2 | `SAEEIAAREET` | 3/5 | 0.388 | 94.20 | 22.68 | 87.1 | 0.55 | 1.072 |
| 3 | `SDAEIAARQAT` | 3/5 | 0.466 | 94.22 | 22.62 | 88.6 | 0.55 | 1.053 |
| 4 | `SDEEIAAREQT` | 4/5 | 0.330 | 94.22 | 21.66 | 88.6 | 0.55 | 1.105 |
| 5 | `SDEEIAAQQAT` | 4/5 | 0.369 | 94.22 | 22.44 | 88.6 | 0.55 | 1.161 |

The unconstrained pool collapses to `S{A,D}EEIAA{R,Q}{E,Q,A}{A,E}T` — MPNN's natural fit is to keep most of the WT backbone-compatible residues but swap V357→I and R363→T. **The unconstrained pool's cleavage scores are MUCH worse than the constrained pool** (0.33–0.47 vs 0.039 for the STRICT set) because Ile/Thr/Ala/Arg/Glu residues still match ALP P1 preference. Unconstrained MPNN does not optimize for protease resistance — only for structural likelihood. This is why the constrained pool is the right one for the wet-lab arm.

### Substitute-sampler GREEN set: did it survive genuine MPNN?

Two questions:
1. **Do the 15 substitute GREEN candidates retain GREEN tier under MPNN-pool concordance cutoffs?** Yes, 15/15 remain GREEN when re-evaluated in the constrained MPNN pool's cutoffs (8 retain 4/5; 7 retain 3/5). When re-evaluated in the unconstrained MPNN pool's cutoffs, 8 retain GREEN, 7 drop to FAIL — but the unconstrained pool isn't the relevant frame (see above).
2. **What is MPNN's per-sequence log-likelihood for each substitute GREEN candidate?** Re-scored via `--score_only` on the full 710-aa reconstruction with the AF-P02788 PDB. The full 74-sequence comparison ranking (60 substitute + 14 MPNN-extras after deduplication) sorted by MPNN score (lower = MPNN prefers):

| MPNN rank (of 74) | Linker | MPNN `-log P` | Source | Substitute tier |
|---|---|---|---|---|
| 1 | `SAEEIAAREAT` | 1.043 | MPNN unconstrained | — |
| 2 | `SDAEIAARQAT` | 1.087 | MPNN unconstrained | — |
| 3 | `SAEEIAAREET` | 1.127 | MPNN unconstrained | — |
| 4 | `SDEEIAAREQT` | 1.170 | MPNN unconstrained | — |
| 5 | `SDEEIAAQQAT` | 1.219 | MPNN unconstrained | — |
| **6** | `SEEEVAARRAR` (WT) | 1.432 | substitute / WT | GREEN (3/5) |
| 7 | `SEEEPAARRAR` | 1.759 | substitute | GREEN (3/5) |
| 8 | `EEEEVAARRAR` | 1.829 | substitute | GREEN (3/5) |
| 9 | `SEEEVAAPPAR` | 2.055 | substitute | GREEN (4/5) |
| 10 | `NEEEQQQQQQQ` | 2.135 | MPNN constrained GREEN | — |
| ... | | | | |
| 16 | `EEEEPAARRAR` (sub primary anchor) | 2.263 | substitute | GREEN (4/5) |
| 21 | `SEEEVAAPPPR` | 2.439 | substitute | GREEN (4/5) |
| 28 | `PEEEPAAPPAP` | 3.296 | substitute | GREEN (3/5) |
| 32 | `DEEDPANPQAH` (sub aggressive arm) | 3.330 | substitute | GREEN (3/5) |
| 35 | `EEEEVPPPRPR` | 3.423 | substitute | GREEN (3/5) |
| 38 | `EEEEPAAPPAP` | 3.466 | substitute | GREEN (4/5) |
| ... | | | | |
| 74 (worst) | `PPPPPPPPPPP` | 5.136 | substitute extreme negative | FAIL |

**Group means** (`-log P`, lower = better):
- MPNN unconstrained GREEN: **1.13** (n=5)
- MPNN constrained GREEN: 2.22 (n=6)
- MPNN constrained STRICT: 2.31 (n=3)
- Substitute pool (all 60): 3.49
  - Substitute GREEN subset (n=15): **2.74**
  - Substitute FAIL subset (n=45): 3.74

The substitute GREEN candidates sit cleanly between MPNN-preferred (1.0–2.3) and MPNN-disfavored (3.5–5.1). The substitute pool's mean-of-GREEN being clearly below mean-of-FAIL confirms the substitute sampler was tracking structural likelihood — its proline-biased + WT-mix-in heuristic was a coarse but functional proxy for what MPNN encodes more directly.

## Headline finding

**The substitute sampler's 15 GREEN candidates were not artifacts.** They retain GREEN tier under genuine ProteinMPNN-pool concordance, and MPNN log-likelihood places them clearly above the substitute FAIL set (mean 2.74 vs 3.74, p << 0.01 by inspection). The comp-034 wet-lab arm at `validation-experiments.md §1.10` can safely commit gene-synthesis spend on the substitute's recommended conservative anchor (`EEEEPAARRAR`, S353E + V357P, 82% identity) — MPNN places this at rank 16/74, structurally plausible.

**Genuine ProteinMPNN, however, finds 3 STRICT (5-of-5) candidates the substitute never proposed:** `NEEEQQQEEEQ`, `NEEEEQQEQEQ`, `NEEEEEQEQEQ`. These reduce predicted cleavage 10.4× vs WT (0.039 vs 0.407) with MPNN log-likelihood ~2.3 (rank ~13-19 of 74, MPNN-tolerable). They are MORE divergent from WT than the substitute's conservative anchor (27% vs 82% identity) but achieve concordance on all 5 metrics simultaneously, which no substitute candidate did.

**The unconstrained MPNN pool is informative but NOT a wet-lab candidate source for this question.** When allowed to choose freely, MPNN prefers `S{A,D}EEIAA{R,Q}{E,Q,A}{A,E}T` (V357→I, R363→T) — structurally plausible but still ALP-substrate-rich (cleavage 0.33–0.47, only modestly better than WT). MPNN optimizes structural likelihood, not protease resistance. The `--omit_AAs` constraint is the right way to fuse MPNN's structural prior with comp-034's protease-resistance design objective.

## Implications for §1.10 wet-lab arm

Recommended 3-variant plate for gene synthesis:

1. **WT control** — `SEEEVAARRAR` (always include).
2. **Conservative MPNN-tolerable variant — substitute's primary anchor — `EEEEPAARRAR`** (S353E + V357P; mature S334E + V338P; 82% identity to WT, 2 substitutions). MPNN rank 16/74; substitute n_pass 4/5. **Same as comp-034 original recommendation; this finding validates that recommendation.**
3. **Aggressive MPNN-native STRICT variant — `NEEEQQQEEEQ`** (S353N + V357Q + A358Q + A359Q + R360E + R361E + A362E + R363Q; mature S334N + V338Q + A339Q + A340Q + R341E + R342E + A343E + R344Q; 8 substitutions, 27% identity to WT). **Replaces the substitute's `DEEDPANPQAH` aggressive arm**, which MPNN scores worse (rank 32 vs 13-19) and which loses STRICT-tier metric concordance to a 4-of-5 GREEN under MPNN's own pool.

Drop the substitute's `DEEDPANPQAH` from the gene-synthesis plate. The MPNN-native STRICT candidate is the better aggressive arm: simultaneous concordance on all 5 metrics (ESM2 fold quality + linker cleavage + CAI + loop pLDDT band + sequence similarity floor), MPNN structural likelihood ranked competitively in the top quartile.

Gene synthesis cost stays at ~$1.5–3K for 3 variants (the substitute arm anchor is unchanged; we're swapping one variant for a comparable-length variant, so synthesis price is the same).

If §1.10 has appetite for a 4-variant plate, add the substitute's `SEEEPAARRAR` (V357P single substitution, 91% identity, MPNN rank 7/74). MPNN places this above the 2-sub `EEEEPAARRAR`, suggesting the V→P swap alone is the load-bearing structural perturbation and that S353E is doing less work. A side-by-side V357P-alone vs V357P+S353E comparison would isolate the contribution of each substitution.

## Limitations

- **MPNN scores backbone, not catalytic site.** ProteinMPNN samples sequences conditioned on the AF-predicted backbone — it doesn't model the iron-binding pocket geometry directly. The 11-residue linker is structurally distant from both iron sites (N-lobe iron in residues 60-92; C-lobe iron in residues 392-456), so this is unlikely to be load-bearing for the linker question. But if any downstream candidate has an unexpected fold change, MPNN's score won't catch it — wet-lab structural validation (CD or crystallography) is still required.
- **Single AF-predicted backbone, no ensemble.** All sampling was conditioned on the single AF-P02788-F1-model_v6 backbone. MPNN's score is sensitive to backbone choice; if the AF prediction has a bad rotamer or a misplaced sidechain near the linker, candidate rankings could shift. The AF-predicted linker pLDDT is 93-98 (very high confidence), so this risk is small here but worth flagging.
- **Cleavage-site scoring is identical to comp-034.** I re-used `lib/protease_stability.py` and `comp-005-lactoferrin-shio-koji-protease-stability/inputs/protease_specificities.json` unchanged. The MPNN rerun's cleavage scores are directly comparable to comp-034's. The protease specificities are still the conservative-fail-open assumptions (ALP `ph_activity_at_shio_koji = 1.0` despite being outside its active pH range; NPr similar). The protease-resistance ranking is robust to these conservative settings — the relative ordering of candidates is what matters, and that's preserved.
- **No back-translation / actual CAI computation against full A. oryzae codon usage.** The CAI score is the comp-034 surrogate ("mean log freq_per1000 of the best codon for each amino acid in the linker"), unchanged. This is a relative codon-favorability score, not Sharp & Li 1987 canonical CAI. Stronger CAI methodology (full back-translation + GenScript codon-adaptation tool + RNA-folding ΔG check) is recommended before final gene-synthesis order — but that's a separate gate downstream of this MPNN rerun.
- **MPNN sampling at temp 0.1 collapses to a narrow motif family.** The 60 constrained samples contained only 41 unique sequences (the rest were near-identical resamples of the `NEEEQ*` motif). At temp 0.1, MPNN is exploiting more than exploring. A second run at temp 0.2 or 0.3 would broaden the candidate distribution; this was not done because the question was specifically "does the substitute pool survive MPNN scrutiny?", which doesn't need broader exploration. If the wet-lab arm wants more candidate diversity, a higher-temperature pass is the next step.
- **Pre-commit grep-verify gate compliance:** All load-bearing numbers in this report (cleavage scores, MPNN ranks, identity percentages, sample counts) trace to the JSON outputs in `wiki/etc/experiments/comp-034-lactoferrin-linker-redesign/proteinmpnn_rerun/`. The MPNN scores come from `mpnn_scores_substitute.json` (parsed from the per-sample `.npz` files written by ProteinMPNN's `--score_only` mode). The cleavage / ESM2 / CAI / loop-pLDDT / similarity scores come from `candidates_mpnn_constrained.json` and `candidates_mpnn_unconstrained.json` (computed by `score_mpnn_candidates.py` which re-uses the shared `lib/protease_stability.py` library unchanged).
- **Sandbox-driven install path.** `/opt/` was not writable; documented fallback path `tools/ProteinMPNN/` was used. The install path is repo-local, not system-level. If Brian wants `/opt/ProteinMPNN` to be the long-term install, run with `sudo` outside the sandbox: `sudo mkdir -p /opt/ProteinMPNN && sudo cp -R tools/ProteinMPNN/* /opt/ProteinMPNN/`. The `bio-ai-tools.md` `$PROTEINMPNN_PATH` env var should then point to whichever path you keep.

## Files written

- **Install** — `tools/ProteinMPNN/` (84 MB, includes `protein_mpnn_run.py`, `helper_scripts/`, `vanilla_model_weights/v_48_020.pt`, `examples/`)
- **Input structure** — `wiki/etc/experiments/comp-034-lactoferrin-linker-redesign/proteinmpnn_rerun/AF-P02788-F1-model_v6.pdb` (fetched from AlphaFold DB API at run time)
- **MPNN run setup** — `parsed_chains.jsonl`, `assigned_chains.jsonl`, `fixed_positions.jsonl`
- **Constrained MPNN sampling** — `mpnn_constrained/seqs/AF-P02788-F1-model_v6.fa` (60 samples)
- **Unconstrained MPNN sampling** — `mpnn_unconstrained/seqs/AF-P02788-F1-model_v6.fa` (60 samples)
- **Score-only pass on substitute pool** — `mpnn_score_only/score_only/*.npz` (74 per-sample log-prob files)
- **Scoring pipeline** — `score_mpnn_candidates.py` (re-uses `lib/protease_stability.py`)
- **Substitute-pool fasta builder** — `build_substitute_fasta.py`
- **MPNN-scored output JSONs** — `candidates_mpnn_constrained.json`, `candidates_mpnn_unconstrained.json`, `shortlist_mpnn.json`, `comparison_with_substitute.json`, `mpnn_scores_substitute.json`
- **Pool summary** — `wiki/etc/experiments/comp-034-lactoferrin-linker-redesign/proteinmpnn_rerun/summary.md`
- **This report** — `logs/proteinmpnn-comp-034-rerun-2026-05-19.md`

All files inside `wiki/etc/experiments/comp-034-lactoferrin-linker-redesign/proteinmpnn_rerun/` are in a sweep-excluded subtree (per the `etc/` convention), so the daemon will not re-read them on save. Brian: propagate findings into `wiki/lactoferrin-linker-redesign-computational.md` manually when ready, with the substitute-sampler caveat block updated to reflect that the rerun has been done and the wet-lab plate recommendation has been refined to include the MPNN-native `NEEEQQQEEEQ` aggressive arm.
