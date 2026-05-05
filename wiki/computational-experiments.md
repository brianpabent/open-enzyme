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

### comp-005 — Lactoferrin Shio-Koji Protease Stability

| Field | Value |
|---|---|
| **Question** | Will human lactoferrin (P02788) survive the shio-koji protease environment with meaningful structural integrity retained? |
| **Method** | AlphaFold pLDDT structural analysis + P1/P1' cleavage-site prediction for 3 *A. oryzae* koji proteases (ALP, NPr, acid protease) + shio-koji condition corrections (17.5% NaCl, pH 4.5–5.0). Shared library with comp-001; two verdicts computed: full sequence and mature protein (excl. signal peptide). |
| **Verdict** | **HIGH (full sequence) / MODERATE (mature protein aa 20–710)**. All top-5 sites across all 3 proteases are in the signal peptide (pLDDT 35–54). Mature-protein max risk 0.188 (ALP, 3 exposed sites). Signal peptide processing by *A. oryzae* is uncertain — if cleaved, operative risk is MODERATE. |
| **Key finding** | The HIGH verdict is signal-peptide-contingent. Mature lactoferrin (aa 20–710) is MODERATE — less resistant than uricase (LOW) but substantially more resistant than the full-sequence headline implies. ALP's conservative pH factor (1.0, outside active pH 6–12) likely overstates mature-protein risk. Glycosylation at N137, N478, N623 not modelled — may further reduce accessibility. |
| **Informs** | [`validation-experiments.md` §1.10](./validation-experiments.md) — lactoferrin arm remains a feasibility gate (unlike uricase arm, which comp-001 reframed as confirmation) |
| **Experiment folder** | [`experiments/comp-005-lactoferrin-shio-koji-protease-stability/`](../experiments/comp-005-lactoferrin-shio-koji-protease-stability/) |
| **Interpretive wiki page** | [`wiki/lactoferrin-protease-stability-computational.md`](./lactoferrin-protease-stability-computational.md) |
| **Date** | 2026-05-05 |
| **Status** | Complete |

---

### comp-004 — Supplement ABCG2 Antagonism

| Field | Value |
|---|---|
| **Question** | Do quercetin, EGCG, and curcumin reach gut-lumen concentrations sufficient to inhibit ABCG2-mediated urate efflux at standard supplement doses? |
| **Method** | IC50 occupancy framework: effective dissolved gut-lumen concentration ÷ ABCG2 IC50 (from ChEMBL). Two-step concentration model: dose-limited capped by intestinal solubility. Hill equation (n=1) for fractional inhibition prediction. |
| **Verdict** | **VERY HIGH risk (provisional)** for quercetin and curcumin — 6.8× and 8.3× IC50 respectively, predicting 87–89% ABCG2 inhibition. EGCG acts via expression downregulation, not scored by this framework. |
| **Key finding** | Curcumin paradox: < 1% bioavailability concentrates > 99% of oral dose in gut lumen, reaching 8.3× its IC50 (1,630 nM) despite lower gut concentration than quercetin. Supplement-induced ABCG2 inhibition may reduce gut urate excretion, paradoxically worsening hyperuricemia. |
| **Informs** | [`validation-experiments.md` §1.14](./validation-experiments.md) — shifts supplement arms from screening to quantification of a pharmacologically-predicted effect |
| **Experiment folder** | [`experiments/comp-004-supplement-abcg2-antagonism/`](../experiments/comp-004-supplement-abcg2-antagonism/) |
| **Interpretive wiki page** | [`wiki/supplement-abcg2-antagonism-computational.md`](./supplement-abcg2-antagonism-computational.md) |
| **Date** | 2026-05-05 |
| **Status** | Complete |

---

## Planned Analyses

| ID | Question | Informs | Priority |
|---|---|---|---|
| comp-002 | Uricase thermal/pH stability under shio-koji conditions (MD simulation or Rosetta ΔΔG) | §1.10 follow-up if wet-lab shows unexpected degradation | Low (pending §1.10 result) |
| ~~comp-003~~ → **comp-005** | Lactoferrin cleavage-site analysis under same shio-koji conditions | §1.10 extension — completed 2026-05-05; see comp-005 above | ✓ Done |

---

## How to add a new analysis

1. Create `experiments/comp-NNN-<slug>/` with `analyze.py`, `inputs/`, `outputs/`, `README.md`, `inputs/provenance.md`
2. Add a row to the "Analyses" table above
3. Create `wiki/<slug>-computational.md` for the interpretive page
4. Link from the relevant wet-lab experiment in `validation-experiments.md`
5. Commit script + inputs + outputs together (outputs are version-controlled — they are the peer-reviewable artifact)
