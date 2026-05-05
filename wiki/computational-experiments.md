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

### comp-006 — DAF/CD55 Shio-Koji Protease Stability

| Field | Value |
|---|---|
| **Question** | Would the DAF/CD55 soluble ectodomain (aa 35–353: SCR1–4 + Ser/Thr stalk) survive the shio-koji protease environment if expressed in *A. oryzae*? |
| **Method** | AlphaFold pLDDT structural analysis + P1/P1' cleavage-site prediction for 3 *A. oryzae* koji proteases (ALP, NPr, acid protease) + shio-koji condition corrections (17.5% NaCl, pH 4.5–5.0). Shared library with comp-001/comp-005; **three verdicts** computed: full sequence, mature protein (excl. signal peptide aa 1–34), and soluble ectodomain (excl. signal peptide + GPI-anchor propeptide aa 354–381). |
| **Verdict** | **HIGH / HIGH / HIGH** — all three scopes. Driver: Ser/Thr-rich stalk (aa 286–353, pLDDT 30–52, fully disordered) within the soluble ectodomain itself. NPr has 9 exposed stalk sites; ALP has 48. SCR1–4 domains (aa 35–285, pLDDT 85–98) contribute **zero exposed sites** — they are structurally well-folded and largely buried. |
| **Key finding** | The HIGH verdict is stalk-contingent, not SCR-domain-contingent. A construct truncated at SCR4 (aa 35–285) would remove all NPr- and ALP-exposed ectodomain sites. The SCR1–4 core compares favorably with uricase (comp-001) in structural stability. A comp-007 analysis of the SCR1-4-only construct is the logical follow-up before concluding the CD55 engineering thesis is unviable. |
| **Informs** | [`wiki/modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) — "Engineered soluble complement regulators" row (CP0 platform gap) |
| **Experiment folder** | [`experiments/comp-006-daf-cd55-shio-koji-protease-stability/`](../experiments/comp-006-daf-cd55-shio-koji-protease-stability/) |
| **Interpretive wiki page** | [`wiki/daf-cd55-protease-stability-computational.md`](./daf-cd55-protease-stability-computational.md) |
| **Date** | 2026-05-05 |
| **Status** | Complete |

---

### comp-007 — Food-Grade HDAC Inhibitor Screen for Q141K-ABCG2 Trafficking Rescue

| Field | Value |
|---|---|
| **Question** | Which food-grade or GRAS-classified HDAC inhibitor candidates best combine class I HDAC potency (HDAC1/2/3), HDAC6 selectivity (off-target cardiotoxicity avoidance), and gut-enriched exposure for Q141K-ABCG2 trafficking rescue? |
| **Method** | Composite scoring across three axes: (1) potency_score = 1/geomean(HDAC1/2/3 IC50), max-normalized; (2) selectivity_score = HDAC6_IC50/(HDAC6_IC50+mean_classI_IC50), midpoint ratio=10, unknown-HDAC6 penalty 0.30; (3) gut_selectivity_score = 1 − oral bioavailability fraction. IC50 data from ChEMBL MCP + PubMed primary literature (butyrate HIGH confidence; others LOW or DATA_UNAVAILABLE). |
| **Verdict** | **Butyrate (rank 1, 0.374) >> Sulforaphane (rank 2, 0.090) > PEITC (rank 3, 0.060).** Only Butyrate has confirmed class I selectivity (167× over HDAC6, HIGH confidence). Caffeic acid and ferulic acid score 0 (DATA_UNAVAILABLE — no isoform IC50). |
| **Key finding** | Butyrate is the only food-grade compound with biochemical-assay IC50 data against all four HDAC isoforms; its 167× HDAC1/2/3 over HDAC6 selectivity is structurally explained (carboxylate zinc coordination, insufficient for bulkier HDAC6 active site). Sulforaphane's ranking is fragile — HDAC isoform selectivity is uncharacterized and the mechanism (indirect, via mercapturic acid metabolites) differs from butyrate's direct zinc chelation. |
| **Informs** | [`validation-experiments.md` §1.22](./validation-experiments.md#122-gut-selective-food-grade-hdac-inhibitor-screen-for-q141k-abcg2-trafficking-rescue) — Stage 1 complete; top 3 advance to Stage 2 (paired Caco-2/HepG2 HDAC activity assay) |
| **Experiment folder** | [`experiments/comp-007-food-grade-hdaci-screen/`](../experiments/comp-007-food-grade-hdaci-screen/) |
| **Interpretive wiki page** | [`wiki/food-grade-hdaci-screen-computational.md`](./food-grade-hdaci-screen-computational.md) |
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
| comp-008 | *Faecalibacterium prausnitzii* heterologous expression feasibility — codon usage, GC content, secretion machinery, payload tractability ranking | [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) Phase 2 P2-4; informs whether *F. prausnitzii* is engineering-tractable for OE-relevant payloads (uricase, lactoferrin, soluble complement regulators, butyrate-pathway boost) | Medium (LBP track Phase 2) |
| comp-009 | URAT1 mRNA structural analysis for siRNA target site selection — SLC22A12 transcript variants, RNAfold secondary structure, accessibility scoring, mammalian-ortholog conservation | [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) Phase 2 P2-2; cheapest mechanistic killshot for the siRNA / URAT1 thesis (no accessible target sites = thesis collapse before delivery is even considered) | Medium (siRNA / URAT1 track Phase 2) |

---

## How to add a new analysis

1. Create `experiments/comp-NNN-<slug>/` with `analyze.py`, `inputs/`, `outputs/`, `README.md`, `inputs/provenance.md`
2. Add a row to the "Analyses" table above
3. Create `wiki/<slug>-computational.md` for the interpretive page
4. Link from the relevant wet-lab experiment in `validation-experiments.md`
5. Commit script + inputs + outputs together (outputs are version-controlled — they are the peer-reviewable artifact)
