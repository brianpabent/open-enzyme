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

### comp-014 — Medicinal Mushroom Compound × Chokepoint Mapping

| Field | Value |
|---|---|
| **Question** | Across all known characterized fungal natural products — aggregated globally, not just Western pharma — which compounds map onto Open Enzyme's chokepoints (uricase substrate, URAT1, ABCG2, NLRP3 axis, complement CP0, Lp-PLA2, HDAC6, redox/disulfide), and which fungal species are the highest-leverage producers? |
| **Method (planned)** | 6-phase pipeline. Phase 2: breadth aggregation across LOTUS + NPAtlas + KNApSAcK + NPASS + TCMSP + COCONUT (+ MIBiG/antiSMASH-DB for BGC space). Phase 3: target mapping via ChEMBL + HIT + PubChem BioAssay → SwissTargetPrediction for orphans. Phase 4: chokepoint intersection. Phase 5: multilingual primary-literature deep-dive on top 3-5 species via CNKI/Wanfang/J-STAGE/KISS with two-model translation cross-check per `Open Enzyme/CLAUDE.md` §Translation protocol. Phase 6: comp-013-style per-compound triage with IC50 occupancy + composite scoring. |
| **Verdict** | **PHASE 1 SCOPED — execution pending.** No data pulled yet. 18 candidate fungi (Cordyceps split *militaris* / *Ophiocordyceps sinensis* per peer review) + 19 chokepoint entries (18 canonical incl. OAT4 surfaced as canonical-wiki gap + 1 proposed redox/disulfide) registered. |
| **Key finding (Phase 1)** | Three reasons the experiment is not "ChEMBL only with extra steps": (1) comp-013 already established that 5/9 TCM compounds had no ChEMBL records — same coverage gap will apply to fungi, likely worse, because mycotherapy is a deeper East-Asian-traditional-medicine vertical than most herbs; (2) fungi are biochemically distinctive in ergothioneine, ETP-class disulfide-bridged compounds, and lanostane triterpenoid diversity that adjacent kingdoms don't produce; (3) the redox/disulfide chemistry angle may warrant adding a new chokepoint to `modality-chokepoint-matrix.md` — the wiki's first patient-side disulfide chokepoint, complementing the engineering-side load-bearing-ness already established by the DAF SCR1-4 incident. **Highest single-leverage potential:** if breadth pass surfaces a validated fungal C5aR1 antagonist that `validation-experiments.md` §1.21's ChEMBL/NPASS/LOTUS/Open Targets scan missed, that partially closes the avacopan-dependence "honest platform gap." |
| **Informs** | [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (Phase 5 may write back a new redox/disulfide column); [`complement-c5a-gout.md`](./complement-c5a-gout.md) CP0 platform gap; [`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md) (methodological extension); [`open-source-platform.md`](./open-source-platform.md) (operationalizes global-multilingual claim) |
| **Experiment folder** | [`experiments/comp-014-medicinal-mushroom-compound-mapping/`](../experiments/comp-014-medicinal-mushroom-compound-mapping/) |
| **Interpretive wiki page** | [`wiki/medicinal-mushroom-compound-mapping-computational.md`](./medicinal-mushroom-compound-mapping-computational.md) |
| **Date** | 2026-05-06 |
| **Status** | Scoped — execution pending Brian sign-off |

---

### comp-013 — TCM Gout Compound Triage

| Field | Value |
|---|---|
| **Question** | Which Traditional Chinese Medicine (TCM) compounds with documented gout indication are mechanistically viable when triaged via the comp-004 IC50 occupancy + comp-007 composite scoring frameworks? |
| **Method** | Applied comp-004's IC50 occupancy framework (Hill n=1, dose × (1−BA) ÷ 250 mL gut model, plasma Cmax via Vd≈1 L/kg) + comp-007's composite scoring (potency × selectivity × gut-enrichment), with three adaptations: (1) gut-enrichment is bidirectional (favorable for gut-luminal targets, unfavorable for systemic-with-low-BA); (2) selectivity uses on-target/off-target IC50 ratio; (3) animal-model in vivo evidence is admissible to the verdict (composite remains 0 without biochem IC50). 9 candidate compounds, 8 gout-relevant ChEMBL targets (URAT1 CHEMBL6120, ABCG2 CHEMBL5393, GLUT9 CHEMBL2052034, XO CHEMBL1929, NLRP3 CHEMBL1741208, sEH CHEMBL2409, OAT1 CHEMBL1641347, OAT3 CHEMBL1641348). |
| **Verdict** | **4 GUT-LUMINAL VIABLE** (luteolin rank 1, astilbin, emodin, berberine) **+ 1 MODERATE / VIABLE-WITH-DOSE-CAVEAT** (rhein) **+ 4 MECHANISM UNCLEAR** (aucubin, cylindrin, chlorogenic acid, atractylenolide I). Si Miao San multi-herb formula has the strongest clinical evidence (24-RCT meta-analysis: SUA −90.62 µmol/L vs anti-inflammation control, p<0.00001) but cannot attribute to single component. |
| **Key finding** | **ChEMBL coverage gap is load-bearing for TCM compounds.** 5 of 9 candidates have NO ChEMBL data of any kind (astilbin, aucubin, cylindrin, atractylenolide I; partial for chlorogenic acid). Only luteolin has both ChEMBL biochem IC50 against gout-relevant target (XO 550 nM) AND animal-model URAT1 evidence. The chembl-cross-check discipline (rule #2 of tcm-modern-rigor-intersection.md) has a coverage limit for TCM-specific phytochemicals — workaround: admit animal-model in vivo dose-response data. Most-represented mechanism across viable candidates: URAT1 expression downregulation in murine PO hyperuricemia model (astilbin, luteolin, berberine all show 5-25 mg/kg activity). Berberine ChEMBL cross-check re-confirmed: most-potent target is TDO 30 nM, NOT NLRP3 — verified activity_id 26130523. |
| **Informs** | [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md) — closes P2-2 (originally placed as comp-011, renumbered to comp-013 after comp-011 was assigned to *C. utilis* uricase compatibility 2026-05-05) |
| **Experiment folder** | [`experiments/comp-013-tcm-gout-compound-triage/`](../experiments/comp-013-tcm-gout-compound-triage/) |
| **Interpretive wiki page** | [`wiki/tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md) |
| **Date** | 2026-05-06 |
| **Status** | Complete |

---

### comp-012 — DAF/CD55 SCR1-4 Truncated Shio-Koji Protease Stability

| Field | Value |
|---|---|
| **Question** | Does the stalk-truncated DAF/CD55 SCR1-4 construct (aa 35–285, removing the disordered Ser/Thr stalk that drove comp-006's HIGH verdict) survive shio-koji protease conditions? |
| **Method** | Same shared library as comp-001 / comp-005 / comp-006 (`experiments/lib/protease_stability.py`). Sequence + AlphaFold pLDDT scoped to aa 35–285. Three *A. oryzae* proteases (ALP, NPr, acid_protease) at shio-koji conditions (17.5% NaCl, pH 4.5–5.0). |
| **Verdict** | **LOW** (max risk 0.039, NPr — **identical to uricase** comp-001). Stalk truncation removed 100% of exposed sites: 9 NPr-exposed + 48 ALP-exposed + 1 acid_protease-exposed → 0 exposed in SCR1-4. All 242 recognition sites in the truncated construct are buried. |
| **Key finding** | The CP0 platform-gap closure thesis is now in silico-validated. comp-006's HIGH verdict (0.388) was 100% stalk-driven, not SCR-domain-driven; the truncation hypothesis surfaced by comp-006's own analysis (and elevated to wet-lab proposal by the 2026-05-05 sweep daemon) is computationally confirmed. **A fermentable engineering candidate for the wiki's only "honest platform gap" now exists.** Three wet-lab unknowns remain (disulfide folding, CCP-regulatory function preservation, mucosal delivery geometry) — see [`hypotheses/H05-daf-scr14-cp0-thesis.md`](./hypotheses/H05-daf-scr14-cp0-thesis.md). |
| **Informs** | [`complement-c5a-gout.md`](./complement-c5a-gout.md) — CP0 status reframe from "honest platform gap" to "active engineering candidate"; [`hypotheses/H05`](./hypotheses/H05-daf-scr14-cp0-thesis.md) (new stub); [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) Engineered-soluble-complement-regulators row updated 🟡→🔬 |
| **Experiment folder** | [`experiments/comp-012-daf-cd55-scr14-truncated/`](../experiments/comp-012-daf-cd55-scr14-truncated/) |
| **Interpretive wiki page** | [`wiki/daf-cd55-scr14-truncated-computational.md`](./daf-cd55-scr14-truncated-computational.md) |
| **Date** | 2026-05-05 |
| **Status** | Complete |

---

### comp-011 — *C. utilis* Uricase Cassette Compatibility (Parallel to comp-010 *A. flavus*)

| Field | Value |
|---|---|
| **Question** | Does *Candida utilis* uricase (industry-revealed preference per ALLN-346 + 2 other commercial programs) have the same cassette-compatibility profile as *A. flavus* uricase, or does the alternative payload introduce blocking design issues? |
| **Method** | Same seven-analysis pipeline as comp-010 (KEX2 site geometry, codon usage CAI, signal peptide / secretion routing, disulfide load, glycosylation scan, concurrent secretion-pathway burden, comparison to Huynh 2020 baseline). Run on *C. utilis* uricase (UniProt **P78609** — corrects the prior P15296 misattribution; P15296 returns Drosophila transposable element) paired with human lactoferrin in the Ward 1995 / *A. oryzae* architecture. |
| **Verdict** | **MODERATE** (vs. *A. flavus* LOW per comp-010). Difference is design-driven, not fundamental incompatibility. |
| **Key finding** | The platform decision this enables: **don't pick — run BOTH variants in §1.9 as parallel direct-secretion cassettes** at ~$200–400 in additional gene synthesis costs and $0 additional fermentation cost. Empirical comparison resolves the *A. flavus* vs. *C. utilis* question. Three drivers of the MODERATE verdict: (1) codon burden 2.3× heavier for *C. utilis* (CAI 0.65 vs 1.51 *A. flavus*) — full codon-optimized gene synthesis mandatory; (2) 4 free cysteines in *C. utilis* vs. 0 in *A. flavus* — risk of aberrant ER disulfide formation; mitigation via non-reducing SDS-PAGE QC + Cys→Ser if aggregation observed; (3) 2 internal KR sites (positions 130, 138) vs. 1 in *A. flavus* — non-load-bearing for direct-secretion design. The ALLN-346 mutation I132R sits adjacent to position 130 KR; order ALLN-346 mutations together with codon-optimized synthesis. |
| **Informs** | [`uricase-variant-selection.md`](./uricase-variant-selection.md) (new comp-011 subsection); [`validation-experiments.md` §1.9](./validation-experiments.md) — the dual-cassette wet-lab experiment design now naturally accommodates parallel testing of both uricase variants. |
| **Experiment folder** | [`experiments/comp-011-c-utilis-uricase-cassette-compatibility/`](../experiments/comp-011-c-utilis-uricase-cassette-compatibility/) |
| **Interpretive wiki page** | [`wiki/c-utilis-uricase-cassette-compatibility-computational.md`](./c-utilis-uricase-cassette-compatibility-computational.md) |
| **Date** | 2026-05-05 |
| **Status** | Complete |

---

### comp-010 — Cassette Compatibility for the Dual-Cassette Koji Endgame Strain

| Field | Value |
|---|---|
| **Question** | Does the uricase (Q00511) + lactoferrin (P02788) payload pair have any cassette-design-specific issues — codon collisions, KEX2 site geometry problems, or secretion-pathway burden — that the Ward 1995 glucoamylase-KEX2 architecture will not handle out of the box? |
| **Method** | Seven analyses on protein sequences (stdlib only): (1) codon usage CAI proxy + rare-codon hotspot scan vs. A. oryzae RSCU table; (2) internal K-R dipeptide census + P1' risk scoring (canonical Kex2p family rules); (3) ER-retention / PTS1 / PTS2 secretion-targeting scan; (4) disulfide bonding load vs. Huynh 2020 adalimumab baseline (16 disulfides = 1.00×); (5) N-X-S/T glycosylation site prediction + UniProt cross-reference; (6) combined concurrent-expression burden synthesis; (7) dimension-by-dimension comparison to Huynh 2020. |
| **Verdict** | **LOW** overall cassette-design risk for the proposed asymmetric architecture (direct-secretion uricase + glucoamylase-KEX2-fusion lactoferrin). No blocking issues. Uricase: 0 disulfides, fungal origin, no KEX2 fusion concerns. Lactoferrin: 17 disulfides (1.06× Huynh 2020 baseline), 2 internal K-R sites (1 abolished P1'=D; 1 moderate P1'=K). Uricase has 1 high-risk internal KR site (pos 128) — irrelevant for direct-secretion cassette design; only load-bearing if moved to fusion architecture. |
| **Key finding** | The OE payload pair is within the Huynh 2020 ER-capacity precedent. Uricase contributes zero PDI/disulfide load (fungal, intracellular origin). The 12.6× Lf titer gap vs. Huynh 2020 (39.7 mg/L adalimumab) is not the correct benchmark — Ward 1995 >2 g/L Lf is the appropriate reference. Two design notes: (1) monitor Lf KEX2 site at mature pos 579 (P1'=K, moderate truncation risk) by SDS-PAGE; (2) verify uricase secretion vs. C-terminal SKL PTS1 motif in §1.9. |
| **Informs** | [`validation-experiments.md` §1.9](./validation-experiments.md) — Ward 1995 dual-cassette feasibility test; comp-010 removes cassette architecture as a pre-experiment concern; §1.9 remains a feasibility gate (format risk unresolved) |
| **Experiment folder** | [`experiments/comp-010-cassette-compatibility/`](../experiments/comp-010-cassette-compatibility/) |
| **Interpretive wiki page** | [`wiki/cassette-compatibility-computational.md`](./cassette-compatibility-computational.md) |
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
| ~~comp-011~~ TCM ChEMBL cross-check | _Reassigned: the TCM ChEMBL cross-check work landed as **comp-013** (2026-05-06; see Analyses table above). Original comp-011 number was reassigned 2026-05-05 to the C. utilis uricase cassette compatibility analysis._ | — | ✓ Done as comp-013 |

---

## How to add a new analysis

1. Create `experiments/comp-NNN-<slug>/` with `analyze.py`, `inputs/`, `outputs/`, `README.md`, `inputs/provenance.md`
2. Add a row to the "Analyses" table above
3. Create `wiki/<slug>-computational.md` for the interpretive page
4. Link from the relevant wet-lab experiment in `validation-experiments.md`
5. Commit script + inputs + outputs together (outputs are version-controlled — they are the peer-reviewable artifact)
