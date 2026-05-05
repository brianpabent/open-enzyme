---
title: "Computational Experiments"
date: 2026-05-05
tags: [computational, experiments, tracking, structural-biology, protease, alphafold]
related:
  - validation-experiments.md
  - koji-endgame-strain.md
  - engineered-koji-protocol.md
---

# Computational Experiments

Tracking index for computational analyses in the Open Enzyme platform. Distinct from [`validation-experiments.md`](./validation-experiments.md) (wet-lab), these use structure prediction, sequence analysis, and simulation to generate evidence-based priors before committing wet-lab resources.

**Convention:** Each analysis lives at `experiments/comp-NNN-<slug>/` at the repo root. The folder contains the script, inputs (with provenance), and raw outputs. This page and a dedicated wiki page carry the interpretation.

**Peer review:** Any collaborator can clone the repo, run `python3 analyze.py` in the relevant folder, and reproduce the outputs. The script, inputs, and provenance are all committed. Disagreements should be filed as GitHub issues against the relevant `comp-NNN` folder.

**Relationship to wet-lab experiments:** Computational analyses inform priors — they shift confidence before a wet-lab experiment runs, and help interpret results after. They do not replace wet-lab validation. Each analysis notes the wet-lab experiment it informs and whether it functions as a feasibility gate or a confirmation experiment.

---

## Analyses

### comp-001 — Uricase Shio-Koji Protease Stability

| Field | Value |
|---|---|
| **Question** | Will *A. flavus* uricase (Q00511) survive the shio-koji protease environment with meaningful activity retained? |
| **Method** | AlphaFold pLDDT structural analysis + P1/P1' cleavage-site prediction for 3 *A. oryzae* koji proteases (ALP, NPr, acid protease) + shio-koji condition corrections (17.5% NaCl, pH 4.5–5.0) |
| **Verdict** | **LOW risk** — all 356 recognition sites across 3 proteases are in confidently-folded regions (100% of residues pLDDT > 80, mean 97.1). Max risk score 0.039/1.0. |
| **Key finding** | Two independent protective factors: (1) uricase is exceptionally well-folded (no exposed loops or disordered termini); (2) shio-koji's 15–20% NaCl suppresses ALP to ~19% residual activity. |
| **Informs** | [`validation-experiments.md` §1.10](./validation-experiments.md) — reframes from feasibility gate to confirmation experiment |
| **Experiment folder** | [`experiments/comp-001-uricase-shio-koji-protease-stability/`](../experiments/comp-001-uricase-shio-koji-protease-stability/) |
| **Interpretive wiki page** | [`wiki/uricase-protease-stability-computational.md`](./uricase-protease-stability-computational.md) |
| **Date** | 2026-05-05 |
| **Status** | Complete |

---

## Planned Analyses

| ID | Question | Informs | Priority |
|---|---|---|---|
| comp-002 | Uricase thermal/pH stability under shio-koji conditions (MD simulation or Rosetta ΔΔG) | §1.10 follow-up if wet-lab shows unexpected degradation | Low (pending §1.10 result) |
| comp-003 | Lactoferrin cleavage-site analysis under same shio-koji conditions | §1.10 extension — endgame strain carries both payloads | Medium |

---

## How to add a new analysis

1. Create `experiments/comp-NNN-<slug>/` with `analyze.py`, `inputs/`, `outputs/`, `README.md`, `inputs/provenance.md`
2. Add a row to the "Analyses" table above
3. Create `wiki/<slug>-computational.md` for the interpretive page
4. Link from the relevant wet-lab experiment in `validation-experiments.md`
5. Commit script + inputs + outputs together (outputs are version-controlled — they are the peer-reviewable artifact)
