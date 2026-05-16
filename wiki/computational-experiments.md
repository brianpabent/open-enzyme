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

**Convention:** Each analysis lives at `wiki/etc/experiments/comp-NNN-<slug>/`. The folder contains the script, inputs (with provenance), and raw outputs. This page is a tight index — detailed methodology, full key-finding lists, and Pass-3 review history live in the per-comp interpretive wiki stub (`wiki/<slug>-computational.md`) and the experiment folder.

**Peer review:** Any collaborator can clone the repo, run `python3 analyze.py` in the relevant folder, and reproduce the outputs. Disagreements should be filed as GitHub issues against the relevant `comp-NNN` folder.

**Relationship to wet-lab experiments:** Computational analyses inform priors; they shift confidence before a wet-lab experiment runs, and help interpret results after. They do not replace wet-lab validation.

---

## Analyses

### comp-035 — Intra-articular Uricase H₂O₂ Reaction-Diffusion (3 Architectures) — GREEN (2026-05-16)

**Question:** Across Pickering emulsion / uricase-catalase fusion / free co-formulated catalase, does steady-state [H₂O₂] at the synovial-tissue boundary stay below the <10 µM presumptive-safe threshold?

**Verdict:** **All three architectures GREEN under reference conditions.** Pickering median 0.19 µM (p95 1.1); fusion 0.034 µM (p95 0.20); free 0.19 µM (p95 7.2, max 120 worst-case). Free lands YELLOW at uneven URI:CAT ratio.

**Key findings:**
- FRET-confirmed <10 nm proximity is NOT what closes the diffusion gap; bulk-phase catalase scavenging dominates at joint scale.
- Catalase (kcat/Km) is the dominant load-bearing input across all architectures (Spearman r ≈ −0.95). Chassis selection driven by production economics / regulatory / formulation, not diffusion math.
- Toxicity threshold band (10/100 µM) is itself a comp-035 contribution — no published synovial-tissue H₂O₂ curve exists.

**Informs:** [chassis-pending-interventions §6](./chassis-pending-interventions.md) · [gout-kill-chain-delivery-routes](./gout-kill-chain-delivery-routes.md) · [delivery-route-matrix](./delivery-route-matrix.md) · [engineered-koji-protocol](./engineered-koji-protocol.md)

**Detail:** [interpretive](./intra-articular-uricase-h2o2-reaction-diffusion-computational.md) · [experiments/](./etc/experiments/comp-035-ia-uricase-h2o2-reaction-diffusion/) · Complete v1

---

### comp-034 — Lactoferrin Inter-Lobe Linker Redesign Pilot — Pilot Complete (2026-05-16)

**Question:** Can the hLf inter-lobe linker (P02788 aa 353–363, `SEEEVAARRAR`) be redesigned to reduce predicted shio-koji protease cleavage while preserving fold quality, codon compatibility, and loop flexibility?

**Verdict:** **15 of 60 candidates pass N-of-5 ≥ 3 (GREEN). Zero pass STRICT 5-of-5.** Primary wet-lab variant `EEEEPAARRAR` (S353E + V357P, 82% WT identity) passes 4-of-5; cleavage 0.407 → 0.290 (~29% reduction). Secondary: true single-V357P `SEEEPAARRAR` (91% WT identity, 3-of-5).

**Key findings:**
- WT linker is a high-pLDDT structured α-helix (AF mean 95.6), not flexible loop — redesign premise empirically grounded by 16 cleavage sites.
- ProteinMPNN MCP wrapper loads but `/opt/ProteinMPNN` repo absent; substitute biased sampler used transparently; single-command rerun when installed.
- First concrete use of protein-design-mcp tool stack; documents install gap.

**Informs:** [validation-experiments §1.10](./validation-experiments.md) · [lactoferrin-protease-stability-computational](./lactoferrin-protease-stability-computational.md) · [etc/bio-ai-tools](./etc/bio-ai-tools.md) · [lactoferrin](./lactoferrin.md)

**Detail:** [interpretive](./lactoferrin-linker-redesign-computational.md) · [experiments/](./etc/experiments/comp-034-lactoferrin-linker-redesign/) · Complete pilot v1 (v2: real ProteinMPNN + full ESM2 + epitope screen queued)

---

### comp-029 — Combined CP0 Systems Model (RA + DAF SCR1-4) — YELLOW (2026-05-16)

**Question:** Does dietary rosmarinic acid (C3 convertase) combined with engineered DAF SCR1-4 (decay-accelerator) provide additive CP0 coverage meaningfully larger than either alone?

**Verdict:** **YELLOW at all three DAF accessibility priors.** Combined median 1.08–1.10× the better singleton (below 1.5× GREEN threshold); 95% CI overlaps both singletons. Both arms saturate individually. RED path closed (no interaction blocker).

**Key findings:**
- RA's CP0 leverage is gut-luminal (Kang 2021 252–1100 µM), not systemic plasma (Baba 2004 Cmax ~20 nM, 1700× below IC50). Correct readout is gut-luminal complement-activation assay.
- Dominant uncertainty driver: DAF SCR1-4 MSU-surface accessibility α (the §1.25 load-bearing wet-lab unknown).
- Combined-strategy thesis not refuted; gated on reducing prior uncertainty before co-administration wet-lab spend.

**Informs:** [complement-c5a-gout §9.7](./complement-c5a-gout.md) · [validation-experiments §1.25](./validation-experiments.md) (optional co-treatment arm gated on α ≥ 0.5) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md)

**Detail:** [interpretive](./combined-cp0-systems-model-computational.md) · [experiments/](./etc/experiments/comp-029-combined-cp0-systems-model/) · Complete v1

---

### comp-030 — ClockBase Combinatorial Ranking of A. oryzae DAF SCR1-4 Cassettes — §1.25 baseline confirmed (2026-05-15)

**Question:** Across the DAF SCR1-4 cassette design space (43,200 combinations), which cassettes survive a multi-model concordance gate; does the §1.25 baseline (PamyB + amyB SP + direct) survive, and does the ESM2 pLDDT distribution corroborate α = 0.3–0.6 for CCP/SCR fold?

**Verdict:** **§1.25 baseline survives; one target-specific refinement (max-CAI codon, NOT 5'-softened).** 40 candidates pass N-of-5 = 5 (0.09%); 632 pass N-of-5 ≥ 4. α-coefficient CORROBORATED: ESM2 pseudo-pLDDT mean 88.8, std 0.5, 100% above 80.

**Key findings:**
- Codon optimization is target-specific: 5'-softened for uricase (comp-022); max-CAI for DAF SCR1-4. Run the framework on each new target.
- Glucoamylase-KEX2 fusion is wrong for CCP/SCR (adds ~10 PDI load on top of intrinsic 3.6).
- ESM2 pLDDT distribution is the narrowest/highest seen for any OE target — in silico fingerprint of cooperatively-folding 2-disulfide β-sandwich.

**Informs:** [validation-experiments §1.25](./validation-experiments.md) · [chaperone-orthogonal-stacking §3.5.2](./chaperone-orthogonal-stacking.md) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md)

**Detail:** [interpretive](./daf-cd55-scr14-cassette-ranking-computational.md) · [experiments/](./etc/experiments/comp-030-daf-cassette-ranking/) · Complete v1 (v2: real ESMFold on 40-strict tier when openfold unblocked)

---

### comp-022 — ClockBase Combinatorial Ranking of A. oryzae Uricase Cassettes — §1.9 architecture stands (2026-05-14)

**Question:** Across the *A. oryzae* uricase cassette design space (43,200 combinations), which cassettes survive a multi-model concordance gate and warrant promotion to §1.9 wet-lab?

**Verdict:** **§1.9 architecture stands; refinements at gene-synthesis layer.** Top cluster: PamyB + amyB SP + 5'-softened codon variant + direct-secretion + PTS1-blocking C-terminal tag + N191Q glycosylation ablation. v2: 71 cassettes pass N-of-5 ≥ 4; v1 top cluster survives 4/4 = 100%.

**Key findings:**
- Three zero-cost gene-synthesis refinements: 5'-softened codon optimization; PTS1-blocking C-term tag (addresses comp-010 routing risk at design layer); N191Q glycosylation ablation.
- Glucoamylase-KEX2 fusion is wrong for uricase (no disulfides + no glycosylation = no carrier benefit, plus 10–25× chaperone load). Confirms comp-010: uricase wants direct secretion, Lf wants fusion.
- v1 GC-clamp proxy vs real ViennaRNA MFE Spearman ρ = 0.241 — v1 proxy noisy on mRNA axis; v2 retrofit with ESM2 pseudo-pLDDT + real MFE materially shifted ranks but architecture verdict held.

**Informs:** [validation-experiments §1.9](./validation-experiments.md) · [cassette-compatibility-computational](./cassette-compatibility-computational.md) · [koji-endgame-strain §3.4](./koji-endgame-strain.md) · [etc/autonomous-screening-methodology](./etc/autonomous-screening-methodology.md)

**Detail:** [interpretive](./uricase-cassette-ranking-computational.md) · [experiments/](./etc/experiments/comp-022-clockbase-uricase-cassette-ranking/) · v2 complete (v2.5 deferred until §1.9 wet-lab data lands)

---

### comp-023 — cns1+cns2 Cordycepin Cassette Metabolic Burden (FBA on iWV1314) — GREEN (2026-05-14)

**Question:** Does adding the bacterial cns1+cns2 cordycepin pathway (Jeennor 2023, 564 mg/L/d) on top of dual uricase + Lf impose prohibitive metabolic burden?

**Verdict:** **GREEN; cns1+cns2 burden-feasible at empirical titer.** Growth penalty +0.02% vs WT; kojic + EGT yield headroom 100%; cordycepin demand consumes ~0.02% of cellular carbon. Breakpoint ~1000× empirical titer.

**Key findings:**
- Jeennor titer is three orders of magnitude below the burden breakpoint; cassette effectively free on carbon + ATP + NADPH axes.
- Cordycepin biosynthesis taps intracellular adenosine via SAH hydrolysis (r857); cordycepin export substitutes for ATP-wasting adenosine kinase step.
- Plain FBA does NOT capture PDI/chaperone proteome saturation — orthogonal to chaperone-orthogonal-stacking framework (different burden axes).

**Informs:** [chaperone-orthogonal-stacking](./chaperone-orthogonal-stacking.md) · [koji-endgame-strain §1.9](./koji-endgame-strain.md) · [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md) · [validation-experiments §1.9](./validation-experiments.md) · [cassette-compatibility-computational](./cassette-compatibility-computational.md)

**Detail:** [interpretive](./cordycepin-cassette-burden-computational.md) · [experiments/](./etc/experiments/comp-023-cns1-cns2-metabolic-burden/) · Complete v1 (v2 dynamic-FBA deprioritized 2026-05-16 — koji-cordycepin removed from active stack)

---

### comp-018 — Upstream Complement Modulator Sweep — Phase 1 complete (2026-05-08)

**Question:** Across all compound classes, which compounds have documented activity at upstream complement cascade nodes proximal to C5a generation, and which are gout-platform-relevant?

**Verdict:** **Direct natural-product C5aR1 antagonists empty (re-confirms comp-014 + §1.21).** Moving one node upstream uncovers substantial literature anchored by **rosmarinic acid** (TIER 1; C3 convertase IC50 5–10 µM, three in vivo precedents, FDA-GRAS sources). TIER 2: luteolin (triple-mechanism with comp-013 XO + URAT1), tiliroside, Bupleurum polysaccharides, falcarindiol, ganoderic acid Sz, quercetin, K-76, complestatin.

**Key findings:**
- "Chokepoint-hacker move" worked; rosmarinic acid is the most well-characterized natural-product upstream-complement modulator.
- **Luteolin triple-convergence** (XO + URAT1 + C3 convertase CP+AP) — highest-leverage single dietary compound surfaced.
- comp-014 β-glucan structure-dependence mechanistically explained; Ganoderma triterpene-enriched preps argued for.
- Engineered C1-INH parallel thread proposed (near-twin to H05 DAF).
- ChEMBL anticomplement coverage 0/32 = 0% — same gap pattern as comp-013/014.

**Informs:** [complement-c5a-gout](./complement-c5a-gout.md) · [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) · [tcm-gout-compound-triage-computational](./tcm-gout-compound-triage-computational.md) · [medicinal-mushroom-compound-mapping-computational](./medicinal-mushroom-compound-mapping-computational.md) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) · [gout-action-guide](./gout-action-guide.md)

**Detail:** [interpretive](./upstream-complement-modulator-sweep-computational.md) · [experiments/](./etc/experiments/comp-018-upstream-complement-modulator-sweep/) · Phase 1 complete (Phase 2 multilingual + C1-INH + complestatin scopes queued). Brief contained user-framing bias; verification re-run is comp-020. See [retrospective](../operations/comp-018-vs-comp-020-retrospective.md).

---

### comp-020 — Upstream Complement Sweep (Brief-Scrubbed Verification Re-Run) — Phase 1 complete (2026-05-08)

**Question:** Across upstream complement nodes (C1q/MBL-MASP-2/C3 tickover/convertases/soluble factors/membrane regulators), which compounds (anchored only to target nodes, no compound names supplied, no prior comp-018 consulted) have documented direct modulator activity?

**Verdict:** **NO single headline compound.** Three classes occupy distinct top-tier mechanistic positions within ~5–20× of each other. **Top per node:** C1q — Helicteres benzofuran lignans + luteolin; MASP-2/LP — heparin oligos + Bupleurum polysaccharide; C3 convertase — rosmarinic acid (covalent IC50 34 µM, distinctive mechanism); marine sulfated polysaccharides 1–3 µg/mL.

**Key findings:**
- **Three independent scans now agree** (comp-013 + comp-014 + comp-020): ChEMBL is structurally biased (~20% NP coverage vs >70% kinase/GPCR). Primary-literature mining is the load-bearing tool.
- Two assay-format spreads documented: rosmarinic acid 44× (C3b 34 µM → C5 convertase 1500 µM); heparin 50× (LP vs AP). Stratifying IC50 by assay type is load-bearing.
- Luteolin convergence-multi-mechanism candidate confirmed; rosmarinic acid is highest mechanistic-distinctiveness candidate (covalent C3b modification).
- Coverage gaps: Factor H upregulators (empty), CD55/CD59/CR1 upregulators (engineering territory), direct fungal upstream modulators (zero — extends comp-014).

**Informs:** [complement-c5a-gout](./complement-c5a-gout.md) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) · [tcm-gout-compound-triage-computational](./tcm-gout-compound-triage-computational.md) · [medicinal-mushroom-compound-mapping-computational](./medicinal-mushroom-compound-mapping-computational.md)

**Detail:** [interpretive](./upstream-complement-verification-rerun-computational.md) · [experiments/](./etc/experiments/comp-020-upstream-complement-verification-rerun/) · Phase 1 complete (Phase 2: CNKI/WanFang/J-STAGE + Helicteres replication + RA/MSU assay + comp-021 mapping queued)

---

### comp-001 — Uricase Shio-Koji Protease Stability — LOW (2026-05-05)

**Question:** Will *A. flavus* uricase (Q00511) survive the shio-koji protease environment with meaningful activity retained?

**Verdict:** **LOW risk.** All 356 recognition sites across 3 proteases are in confidently-folded regions (100% residues pLDDT > 80, mean 97.1). Max risk score 0.039/1.0.

**Key findings:**
- Uricase is exceptionally well-folded (no exposed loops or disordered termini).
- Shio-koji's 15–20% NaCl suppresses ALP to ~19% residual activity (second independent protective factor).

**Informs:** [validation-experiments §1.10](./validation-experiments.md) — reframes from feasibility gate to confirmation experiment

**Detail:** [interpretive](./uricase-protease-stability-computational.md) · [experiments/](./etc/experiments/comp-001-uricase-shio-koji-protease-stability/) · Complete

---

### comp-006 — DAF/CD55 Shio-Koji Protease Stability (full ectodomain) — HIGH (2026-05-05)

**Question:** Would the DAF/CD55 soluble ectodomain (aa 35–353: SCR1–4 + Ser/Thr stalk) survive shio-koji protease conditions?

**Verdict:** **HIGH / HIGH / HIGH** across full / mature / soluble-ectodomain scopes. Driver: Ser/Thr-rich stalk (aa 286–353, pLDDT 30–52, disordered). SCR1–4 (aa 35–285, pLDDT 85–98) contribute **zero exposed sites**.

**Key findings:**
- HIGH verdict is stalk-contingent, not SCR-domain-contingent. Truncation at SCR4 surfaces as the load-bearing follow-up (became comp-012).
- SCR1–4 core compares favorably with uricase (comp-001) in structural stability.

**Informs:** [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) — Engineered soluble complement regulators row

**Detail:** [interpretive](./daf-cd55-protease-stability-computational.md) · [experiments/](./etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/) · Complete

---

### comp-015 — T-axis Adjuvant Urate-Target Mapping (v2) — H-AN-02 PARTIALLY FALSIFIED (2026-05-07)

**Question:** For four T-axis-active compounds (cordycepin, eurycomanone, icariin, echinacoside), what is the curated evidence at five urate-handling + T-axis targets (URAT1, ABCG2, OAT1, SHBG, XO)?

**Verdict:** **H-AN-02 PARTIALLY FALSIFIED.** Cordycepin = **GOUT-FAVORABLE** (URAT1 down + supplementary XO IC50 55.7 µM). Eurycomanone = **GOUT-FAVORABLE** (v1→v2 REVERSED; hURAT1 + GLUT9 down + ABCG2/NPT1 up + PRPS suppression + 2021 RCT SUA −7-11% n=105). Icariin / echinacoside = **MECHANISM-UNCLEAR**.

**Key findings:**
- v2 added XO panel after v1 missed eurycomanone XO mechanism trigger; the trigger was citation-laundering (PMID 31920654/34785103 establish transporter+purine-synthesis, not direct XO) but panel addition still correct.
- v2 finds 5 direct-evidence cells vs v1's 1; eurycomanone now better-characterized than cordycepin on urate axis.
- New chokepoint surfaced: **PRPS (phosphoribosyl pyrophosphate synthetase)** — eurycomanol mechanism, distinct from XO.

**Informs:** [androgen-natural-modulation §10 H-AN-02](./androgen-natural-modulation.md) · [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md) · [androgen-urate-axis](./androgen-urate-axis.md)

**Detail:** [interpretive](./t-axis-adjuvant-urate-mapping-computational.md) · [experiments/](./etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/) · Complete v2

---

### comp-016 — T × Intestinal ABCG2 Suppression Evidence Mining — WEAK / UNCONFIRMED (2026-05-07)

**Question:** Does primary literature support the load-bearing claim that androgens directly suppress intestinal ABCG2 expression at platform-relevant magnitudes?

**Verdict:** **WEAK / UNCONFIRMED (provisional; abstract-tier).** Of 17 studies, zero primary studies demonstrate androgen-driven intestinal ABCG2 suppression directly. 1 supports broader sex-dimorphism (Hoque 2020 Q140K mouse); 1 supports female-positive arm (Yu 2021, estradiol ↑ ABCG2); 1 directly contradicts (Klyushova 2023, T INDUCES via PXR/FXR).

**Key findings:**
- Intestinal compartment IS sex-dimorphic, but driver is **estradiol POSITIVE on female side**, not **androgen NEGATIVE on male side**.
- Platform-thesis "structural ceiling from androgen-driven ABCG2 suppression" should soften to "modest dose-response shift driven by absent estradiol-positive signaling in male physiology."
- Sakamoto 2018 ADT cohort (−0.66 mg/dL at 6 months, n=489) consistent with URAT1-only renal mechanism; no direct AR-ARE on ABCG2 promoter identified.

**Informs:** [androgen-urate-axis](./androgen-urate-axis.md) · [abcg2-modulators](./abcg2-modulators.md) · [gut-lumen-sink](./gut-lumen-sink.md) · [koji-endgame-strain](./koji-endgame-strain.md) · [cross-validation](./cross-validation.md)

**Detail:** [interpretive](./t-abcg2-suppression-evidence-mining-computational.md) · [experiments/](./etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/) · Complete (full-text follow-up → comp-017)

---

### comp-019 — Gut-Lumen Uricase × ABCG2 Genotype Stratification + Flux Model — Mechanism genotype-robust (2026-05-08)

**Question:** Can the gut-lumen uricase sink produce meaningful SUA reduction in non-Q141K males, or does it rely on Q141K-positive disease-state vulnerability?

**Verdict:** **Mechanism does NOT depend on Q141K-positive vulnerability.** WT/WT males show LARGEST predicted ΔSUA (−0.83 mg/dL at 25 mg/day, 90% CI −1.13 to −0.57); Q141K hom smallest among typical genotypes (−0.50); severe dysfunction smallest absolute (−0.28). Genotype ordering INVERTED relative to worry framing.

**Key findings:**
- Across the entire published uricase clinical-trial corpus, ZERO trials have stratified by ABCG2 Q141K genotype (rich Q141K × allopurinol literature; empty Q141K × uricase). Publishable in itself.
- Flux model predicts substrate-limited regime at all dose scenarios (capacity ratios 32–1300×). Yield target stays ~25 mg/dose; engineering effort shifts to GI-survival optimization, not yield.
- Phase 2b RCT design: typical-gout RCT with Q141K + Q126* as **stratification**, NOT enrichment; single ~25 mg/day; pre-stratify by CKD.

**Informs:** [cross-validation Claim 1](./cross-validation.md) (rating 6/10 → 6.5/10) · [gut-lumen-sink](./gut-lumen-sink.md) · [abcg2-modulators §6](./abcg2-modulators.md) · [open-questions](./open-questions.md) Q1 · [personal-genome-protocol](./personal-genome-protocol.md) · [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md)

**Detail:** [interpretive](./uricase-abcg2-genotype-stratification-computational.md) · [experiments/](./etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/) · Complete (prospective; awaits Phase 2b RCT validation)

---

### comp-017 — Intestinal ABCG2 Sex-Dimorphism Public-Data Mining + 4-Paper Full-Text Re-Read — NULL OR NEAR-NULL at healthy baseline (2026-05-07)

**Question:** Tier-0 killshot for H07 sub-claims 1 and 3, closing comp-016's full-text-verification follow-up. Part A: GTEx + HPA sex-stratified intestinal ABCG2. Part B: full-text re-read of Yu 2021 / Klyushova 2023 / MacLean 2008 / Hoque 2020.

**Verdict:** **NULL OR NEAR-NULL SEX-DIMORPHISM at healthy baseline (provisional).** Sex-dimorphism emerges only under **disease-state genetic stress** (Q140K LOF, Hoque) or **strong pharmacological perturbation** (100 µM E2, Yu; 1–100 µM sex hormones, Klyushova). Healthy-baseline literature converges on null.

**Key findings:**
- Hoque 2020 correction: Western-jejunum 78% : Western-kidney 44% (~1.8×), NOT comp-016's 88%:44%. Female FEUA unchanged (p=0.6263) — strong null on female protection.
- Yu 2021: Caco-2 active at 100 µM EB (5–6 orders above physiological serum E2); mechanism real at strong-pharmacological tier; physiological magnitude unestablished.
- Klyushova 2023: T/E2/P at 1/10/100 µM all INCREASE ABCG2 via PXR/FXR (NOT AR) — **H07 sub-claim 3 ("NOT AR-mediated") strongly supported.**
- Hosoyamada 2010 surfaced: T affects renal URAT1 mRNA only (protein unchanged); actual androgen-responsive renal urate transporter is **Smct1**, GLUT9 attenuated.

**Informs:** [hypotheses/H07](./hypotheses/H07-clomid-intestinal-er-antagonism.md) · [t-abcg2-suppression-evidence-mining-computational](./t-abcg2-suppression-evidence-mining-computational.md) · [androgen-urate-axis](./androgen-urate-axis.md) · [abcg2-modulators §1](./abcg2-modulators.md) · [gut-lumen-sink](./gut-lumen-sink.md)

**Detail:** [interpretive](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md) · [experiments/](./etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/) · Complete (provisional; sandbox-blocked GTEx/HPA direct; Paperclip line-anchored re-run recommended)

---

### comp-014 — Medicinal Mushroom Compound × Chokepoint Mapping — Phase 2 ran (2026-05-06)

**Question:** Across all known characterized fungal natural products (globally, not Western pharma only), which compounds map onto OE chokepoints, and which fungal species are highest-leverage producers?

**Verdict:** **PHASE 2 RAN.** ChEMBL sweep + LOTUS pull (6,798 unique fungal compounds, 55 species) + PubMed scan (14 high-signal hits). Highest-leverage: *Ganoderma applanatum* 2,4-DAE shows in vivo dual XO + URAT1 SUA reduction 407→134 µmol/L (Fitoterapia 2022).

**Key findings:**
- C5aR1 platform-gap (§1.21) confirmed empirically — zero direct fungal antagonists in either ChEMBL or PubMed.
- ChEMBL coverage of canonical mushroom compounds near-zero; CLAUDE.md global-multilingual warning empirically validated.
- Two new chokepoint candidates surfaced: ADA (purine catabolism) and PINK1/mitophagy (NLRP3-priming-adjacent).

**Informs:** [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) · [complement-c5a-gout](./complement-c5a-gout.md) · [tcm-gout-compound-triage-computational](./tcm-gout-compound-triage-computational.md) · [etc/open-source-platform](./etc/open-source-platform.md)

**Detail:** [interpretive](./medicinal-mushroom-compound-mapping-computational.md) · [Phase 2 findings](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/PHASE-2-FINDINGS.md) · [experiments/](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/) · Phase 2 complete; Phase 3 in progress

---

### comp-013 — TCM Gout Compound Triage — 4 viable + 1 caveat (2026-05-06)

**Question:** Which TCM compounds with documented gout indication are mechanistically viable when triaged via comp-004 IC50 occupancy + comp-007 composite scoring?

**Verdict:** **4 GUT-LUMINAL VIABLE** (luteolin rank 1, astilbin, emodin, berberine) **+ 1 MODERATE / VIABLE-WITH-DOSE-CAVEAT** (rhein) **+ 4 MECHANISM UNCLEAR** (aucubin, cylindrin, chlorogenic acid, atractylenolide I). Si Miao San formula has strongest clinical evidence (24-RCT meta SUA −90.62 µmol/L, p<0.00001) but multi-component.

**Key findings:**
- ChEMBL coverage gap is load-bearing for TCM: 5 of 9 candidates have NO ChEMBL data. Workaround: admit animal-model in vivo dose-response.
- Most-represented mechanism: URAT1 expression downregulation in murine PO hyperuricemia (astilbin, luteolin, berberine all 5–25 mg/kg).
- Berberine ChEMBL cross-check: most-potent target is TDO 30 nM, NOT NLRP3.

**Informs:** [tcm-modern-rigor-intersection](./tcm-modern-rigor-intersection.md) — closes P2-2

**Detail:** [interpretive](./tcm-gout-compound-triage-computational.md) · [experiments/](./etc/experiments/comp-013-tcm-gout-compound-triage/) · Complete

---

### comp-012 — DAF/CD55 SCR1-4 Truncated Shio-Koji Protease Stability — LOW (2026-05-05)

**Question:** Does the stalk-truncated DAF SCR1-4 construct (aa 35–285, removing the disordered Ser/Thr stalk that drove comp-006 HIGH) survive shio-koji protease conditions?

**Verdict:** **LOW (max risk 0.039, identical to uricase comp-001).** Stalk truncation removed 100% of exposed sites: 9 NPr + 48 ALP + 1 acid → 0 exposed in SCR1-4. All 242 recognition sites buried.

**Key findings:**
- CP0 platform-gap closure thesis in silico-validated. comp-006's HIGH was 100% stalk-driven, not SCR-driven.
- Fermentable engineering candidate for the wiki's only "honest platform gap" now exists. Three wet-lab unknowns remain (disulfide folding, CCP function preservation, mucosal delivery geometry).

**Informs:** [complement-c5a-gout](./complement-c5a-gout.md) (CP0 status reframe) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) (new stub) · [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) (row updated 🟡→🔬)

**Detail:** [interpretive](./daf-cd55-scr14-truncated-computational.md) · [experiments/](./etc/experiments/comp-012-daf-cd55-scr14-truncated/) · Complete

---

### comp-011 — *C. utilis* Uricase Cassette Compatibility — MODERATE (2026-05-05)

**Question:** Does *C. utilis* uricase (industry-revealed preference per ALLN-346) have the same cassette-compatibility profile as *A. flavus* uricase, or does the alternative payload introduce blocking issues?

**Verdict:** **MODERATE** (vs *A. flavus* LOW per comp-010). Design-driven, not fundamental incompatibility.

**Key findings:**
- Platform decision: **don't pick; run BOTH variants in §1.9 as parallel direct-secretion cassettes** at ~$200–400 additional gene synthesis. Empirical comparison resolves *A. flavus* vs *C. utilis*.
- Three MODERATE drivers: codon burden 2.3× heavier (CAI 0.65 vs 1.51); 4 free cysteines vs 0; 2 internal KR sites vs 1. ALLN-346 mutation I132R adjacent to position 130 KR.
- Corrects prior P15296 misattribution; canonical UniProt is **P78609**.

**Informs:** [uricase-variant-selection](./uricase-variant-selection.md) · [validation-experiments §1.9](./validation-experiments.md)

**Detail:** [interpretive](./c-utilis-uricase-cassette-compatibility-computational.md) · [experiments/](./etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/) · Complete

---

### comp-010 — Cassette Compatibility for Dual-Cassette Koji Endgame Strain — LOW (2026-05-05)

**Question:** Does the uricase (Q00511) + lactoferrin (P02788) payload pair have cassette-design-specific issues (codon collisions, KEX2 geometry, secretion burden) that the Ward 1995 glucoamylase-KEX2 architecture won't handle?

**Verdict:** **LOW** overall cassette-design risk for the asymmetric architecture (direct-secretion uricase + glucoamylase-KEX2-fusion Lf). Uricase: 0 disulfides; Lf: 17 disulfides (1.06× Huynh 2020). No blocking issues.

**Key findings:**
- OE payload pair within Huynh 2020 ER-capacity precedent. Ward 1995 >2 g/L Lf is the correct benchmark (not adalimumab 39.7 mg/L).
- Monitor Lf KEX2 site at mature pos 579 (moderate truncation risk) by SDS-PAGE; verify uricase secretion vs C-terminal SKL PTS1 motif.
- Uricase pos 128 high-risk KR is irrelevant for direct-secretion (load-bearing only if moved to fusion).

**Informs:** [validation-experiments §1.9](./validation-experiments.md) — removes cassette architecture as pre-experiment concern

**Detail:** [interpretive](./cassette-compatibility-computational.md) · [experiments/](./etc/experiments/comp-010-cassette-compatibility/) · Complete

---

### comp-007 — Food-Grade HDAC Inhibitor Screen for Q141K-ABCG2 Trafficking Rescue — Butyrate rank 1 (2026-05-05)

**Question:** Which food-grade HDAC inhibitor candidates best combine class I HDAC potency, HDAC6 selectivity, and gut-enriched exposure for Q141K-ABCG2 trafficking rescue?

**Verdict:** **Butyrate (rank 1, 0.374) >> Sulforaphane (rank 2, 0.090) > PEITC (rank 3, 0.060).** Only Butyrate has confirmed class I selectivity (167× over HDAC6, HIGH confidence). Caffeic + ferulic acid score 0 (DATA_UNAVAILABLE).

**Key findings:**
- Butyrate is the only food-grade compound with biochemical IC50 against all four HDAC isoforms; 167× HDAC1/2/3-over-HDAC6 structurally explained (carboxylate zinc coordination).
- Sulforaphane ranking fragile; isoform selectivity uncharacterized; indirect mercapturic-metabolite mechanism differs from butyrate.

**Informs:** [validation-experiments §1.22](./validation-experiments.md#122-gut-selective-food-grade-hdac-inhibitor-screen-for-q141k-abcg2-trafficking-rescue) — top 3 advance to Stage 2

**Detail:** [interpretive](./food-grade-hdaci-screen-computational.md) · [experiments/](./etc/experiments/comp-007-food-grade-hdaci-screen/) · Complete

---

### comp-005 — Lactoferrin Shio-Koji Protease Stability — HIGH (full) / MODERATE (mature) (2026-05-05)

**Question:** Will human lactoferrin (P02788) survive the shio-koji protease environment with meaningful structural integrity retained?

**Verdict:** **HIGH (full sequence) / MODERATE (mature aa 20–710).** All top-5 sites in signal peptide (pLDDT 35–54). Mature max risk 0.188 (ALP, 3 exposed sites). If signal peptide cleaved by *A. oryzae*, operative risk is MODERATE.

**Key findings:**
- HIGH verdict is signal-peptide-contingent. Mature Lf less resistant than uricase (LOW) but substantially more resistant than full-sequence headline.
- ALP's conservative pH factor (1.0, outside active pH 6–12) likely overstates mature-protein risk. Glycosylation at N137/N478/N623 not modelled; may further reduce accessibility.
- Inter-lobe linker flagged as most plausible secondary vulnerability → became comp-034.

**Informs:** [validation-experiments §1.10](./validation-experiments.md) — Lf arm remains feasibility gate (unlike uricase)

**Detail:** [interpretive](./lactoferrin-protease-stability-computational.md) · [experiments/](./etc/experiments/comp-005-lactoferrin-shio-koji-protease-stability/) · Complete

---

### comp-004 — Supplement ABCG2 Antagonism — VERY HIGH risk (provisional) (2026-05-05)

**Question:** Do quercetin, EGCG, and curcumin reach gut-lumen concentrations sufficient to inhibit ABCG2-mediated urate efflux at standard supplement doses?

**Verdict:** **VERY HIGH risk (provisional)** for quercetin and curcumin; 6.8× and 8.3× IC50, predicting 87–89% ABCG2 inhibition. EGCG acts via expression downregulation, not scored by this framework.

**Key findings:**
- **Curcumin paradox:** <1% bioavailability concentrates >99% of oral dose in gut lumen, reaching 8.3× IC50 (1,630 nM) despite lower gut concentration than quercetin.
- Supplement-induced ABCG2 inhibition may reduce gut urate excretion, paradoxically worsening hyperuricemia.

**Informs:** [validation-experiments §1.14](./validation-experiments.md) — shifts supplement arms from screening to quantification

**Detail:** [interpretive](./supplement-abcg2-antagonism-computational.md) · [experiments/](./etc/experiments/comp-004-supplement-abcg2-antagonism/) · Complete

---

## Planned Analyses

| ID | Scope | Primary informs | Priority |
|---|---|---|---|
| comp-002 | Uricase thermal/pH stability under shio-koji conditions (MD or Rosetta ΔΔG) | [§1.10 follow-up](./validation-experiments.md) | Low (pending §1.10 result) |
| ~~comp-003~~ | Reassigned 2026-05-05 → comp-005 (lactoferrin cleavage-site analysis) | — | ✓ Done as comp-005 |
| comp-008 | *F. prausnitzii* heterologous expression feasibility (codon, GC, secretion, payload tractability ranking) | [engineered-lbp-chassis](./engineered-lbp-chassis.md) Phase 2 P2-4 | Medium |
| comp-009 | URAT1 mRNA structural analysis for siRNA target site selection | [sirna-urat1-modality](./sirna-urat1-modality.md) Phase 2 P2-2 | Medium |
| ~~comp-011 TCM~~ | Reassigned 2026-05-05; TCM ChEMBL cross-check landed as comp-013 | — | ✓ Done as comp-013 |
| comp-021 | Compound × upstream-complement chokepoint × matched-assay-format mapping (resolves RA 44× spread) | [upstream-complement-verification-rerun-computational](./upstream-complement-verification-rerun-computational.md) | Low (parked) |
| ~~comp-022~~ | Completed 2026-05-14 — see Analyses above | — | ✓ Done |
| comp-024 | Complestatin-family BGC heterologous expression feasibility in engineered-LBP chassis | [engineered-lbp-chassis](./engineered-lbp-chassis.md) Phase 2 | Medium |
| comp-023 | Promoted to Analyses 2026-05-14 (GREEN) | — | ✓ Done |
| ~~comp-022 v2~~ | Completed 2026-05-14 — see comp-022 Status above | — | ✓ Done |
| ~~comp-023 v2~~ | Deprioritized 2026-05-16 — koji-cordycepin removed from active stack ([koji-endgame-strain §3.5](./koji-endgame-strain.md)) | — | Closed |
| ~~comp-025~~ | Deprioritized 2026-05-16 — koji-cordycepin removed; cultivation-route cordycepin inherits native ADA-inhibitor pairing | — | Closed |
| ~~comp-026~~ | Deprioritized 2026-05-16 — multi-cassette induction interference moot for cordycepin; re-openable for future cytosolic third-cassette candidate | — | Closed |
| comp-027 | Disulfiram dose modeling for GSDMD-blockade vs alcohol-deterrent ceiling (CP6b; 503A pathway gate) | [compounding-pharmacy-track](./compounding-pharmacy-track.md) §6 · [disulfiram](./disulfiram.md) · [nlrp3-exploit-map](./nlrp3-exploit-map.md) CP6b | Medium-High |
| ~~comp-030~~ | Completed 2026-05-15 — see Analyses above | — | ✓ Done |
| ~~comp-029~~ | Completed 2026-05-16 — YELLOW; see Analyses above | — | ✓ Done |
| comp-031 | Dual-chassis EcN PDB + uricase additive SUA prediction (CP6 multi-chassis stack) | [purine-degrading-bacteria](./purine-degrading-bacteria.md) · [chassis-pending-interventions](./chassis-pending-interventions.md) M1 | Medium |
| comp-032 | Pharmacological-chaperone virtual screen against ABCG2 Q141K. Promotes the placeholder "comp-NNN" in [`chassis-pending-interventions.md §7`](./chassis-pending-interventions.md) ("Pharmacological chaperones for ABCG2 Q141K folding rescue") to a concrete numbered comp. Approach: (a) AlphaFold structure of wild-type ABCG2 + AlphaFold structure of Q141K mutant — compare to surface the misfolded NBD region as a binding pocket of interest; (b) virtual screen of the FDA-approved drug set (DrugBank / ChEMBL approved-drugs subset, ~3,000–5,000 molecules) against the Q141K NBD pocket using AutoDock Vina or DiffDock, with positive controls drawn from the CFTR-corrector class (ivacaftor / tezacaftor / elexacaftor) and from documented ABC-transporter-binding compounds; (c) rank-order hits by binding-pose stability + drug-class diversity; (d) cross-check top 20 against known PK / safety profile + 503A bulk-API availability for the compounding-pharmacy delivery route. Outcome: a defensible shortlist of 0–10 repurposing candidates worth a per-hit cell-based Q141K trafficking-rescue assay, or a defensible empty-shortlist verdict that the FDA-approved drug surface lacks chaperone-active hits for Q141K and any chaperone campaign would need novel chemistry (informs the next-step decision: empty shortlist → drop the repurposing-surface thesis for this target, pivot to AI-aided novel binder design per RFdiffusion; non-empty → compounding-pharmacy partner conversation). | [`chassis-pending-interventions.md` §7](./chassis-pending-interventions.md) (promotes the placeholder comp-NNN); [`abcg2-modulators.md`](./abcg2-modulators.md) §"Pharmacological-chaperone route" (the orthogonal rescue mechanism); [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) (delivery route if a hit lands); [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) and [`abcg2-modulators.md`](./abcg2-modulators.md) §"Q141K rescue mechanism" (the HDAC/butyrate rescue track this is orthogonal to) | Medium (cheap subagent task; bounds a "repurposing surprise" hypothesis cheaply; non-blocking for any other track) |
| comp-033 | Inhaled mRNA-IL-1RA pulse therapy — target validation, dose modeling, pharma-partner identification | [open-enzyme-vision §10](./etc/open-enzyme-vision.md) · [chassis-pending-interventions §4](./chassis-pending-interventions.md) | Medium-High |
| ~~comp-028~~ | Reframed and deprioritized 2026-05-16 — cordycepin-arm moot; general design-escape question non-load-bearing today; re-openable for future cytosolic third-cassette candidate | — | Closed |

---

## Infrastructure proposals

### comp-NNN verification agent (ClockBase hypothesis-then-verify pattern) — Planned (2026-05-08)

Every comp-NNN run produces output from a *generation* agent; add a second-pass *verification* agent (different vendor preferred per the multi-vendor heterogeneity discipline) that re-checks every load-bearing number (disulfide counts, residue indices, IC50/Ki, accession numbers, cohort sizes) against primary databases (UniProt, ChEMBL, PDB, PubMed) before commit. Sister discipline to the per-page Pre-commit verification gate (CLAUDE.md Rule 4) — same pattern at a different scope. Would have caught the 2026-05-06 DAF SCR1-4 disulfide hallucination at generation time. Cost ~$3–5 + 10–30 min per comp.

**Detail:** [etc/autonomous-screening-methodology](./etc/autonomous-screening-methodology.md) §"Hypothesis-then-verify pattern" · [etc/manual-literature-mining](./etc/manual-literature-mining.md) §"Pre-commit verification gate" · [operations/comp-018-vs-comp-020-retrospective](../operations/comp-018-vs-comp-020-retrospective.md)

---

### pcSec-class proteome-constrained *A. oryzae* GEM build — Planned (2026-05-14)

Layer secretion-pathway proteome-cost constraints on iWV1314 (Vongsangnak 2008): explicit PDI/calnexin/BiP saturation, signal-peptide processing capacity, KEX2 flux, Sec61 throughput. Enables rigorous burden evaluation for any future *secreted* third cassette (DAF SCR1-4 per H05; engineered C1-INH per comp-018 Phase 2; complestatin NRPS per comp-024). Validation gate: must reproduce comp-023 GREEN for cytosolic cns1+cns2. Multi-week research project; not a single-subagent task. Surfaced as comp-023 v1 limitation.

**Detail:** [chaperone-orthogonal-stacking](./chaperone-orthogonal-stacking.md) · companion to verification-agent proposal (per-run vs per-strain infrastructure scopes)

---

## How to add a new analysis

1. Create `etc/experiments/comp-NNN-<slug>/` with `analyze.py`, `inputs/`, `outputs/`, `README.md`, `inputs/provenance.md`
2. Add an entry to the "Analyses" section above (compact format) or the "Planned Analyses" table
3. Create `wiki/<slug>-computational.md` for the interpretive page
4. Link from the relevant wet-lab experiment in `validation-experiments.md`
5. Commit script + inputs + outputs together (outputs are version-controlled; they are the peer-reviewable artifact)
