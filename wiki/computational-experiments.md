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

**Convention:** Each active or bounded analysis lives at `wiki/etc/experiments/comp-NNN-<slug>/` with the code/input/output contract required by its current verdict. A fully invalidated COMP may retain only a hash-bound invalidation record in the live tree while Git preserves the retired executable artifacts.

**Peer review:** Runnable COMPs declare their reproduction command and dependencies. Invalidated tombstones are not rerun; their historical artifacts are available through Git. Disagreements should be filed as GitHub issues against the relevant `comp-NNN` folder.

**Relationship to wet-lab experiments:** Computational analyses inform priors; they shift confidence before a wet-lab experiment runs, and help interpret results after. They do not replace wet-lab validation.

---

## Analyses

### comp-046 — Dietary Fate Ledger + Endogenous Capture-Fraction Comparison — YELLOW / TWO CONDITIONAL HYPOTHESES (2026-07-13)

**Question:** Two independent comparisons: when does whole-cell GR-5 reduce modeled absorbed dietary precursor, and when does spatial UOX→PDB access exceed an overlap-adjusted well-mixed endogenous capture architecture?

**Verdict:** **YELLOW — two conditional hypotheses, not one additive efficacy claim.** The dietary 100-unit fate ledger is conserved. The endogenous side is an architecture-level capture-fraction comparison, not a second conserved fate ledger. Neither is summed into ΔSUA.

**Key findings:** two independent 81-cell deterministic full-factorials; explicit conserved dietary fate ledger; separate non-conserved endogenous luminal-urate capture-fraction comparison. Grid occupancy is not probability, and the model does not establish a topology winner or joint three-stage efficacy.

**Informs:** [validation §1.34](./validation-experiments.md#134-isotope-resolved-dietary-precursor--uox--pdb-sequential-flux) · [purine-degrading bacteria](./purine-degrading-bacteria.md) · [purine load](./purine-load-koji-vs-yeast.md)

**Detail:** [interpretive](./staged-purine-sink-mass-balance-computational.md) · [experiment folder](./etc/experiments/comp-046-staged-purine-sink-mass-balance/) · Complete first pass

---

### comp-045 — Uricase Topology × Oxygen × Peroxide Design — YELLOW / NO TOPOLOGY ELIMINATED (2026-07-13)

**Question:** How should intracellular+YgfU, LamB-secreted, InakN-displayed, and koji-secreted UOX be compared across urate, oxygen, catalase localization, and VHb support?

**Verdict:** **YELLOW — joint empirical comparison required; no topology eliminated.** PULSE supplies three valid EcN precedents. Intracellular UOX has direct co-localization precedent; secreted/displayed forms have indirect empirical KatG+VHb support but unresolved extracellular peroxide exposure. Free secreted koji remains testable but cannot claim automatic peroxide closure from intracellular catalase.

**Key findings:** 19 non-duplicative factorial conditions × three urate concentrations; three independent biological runs in separate oxic/microoxic contexts; six randomized 96-well plates with substrate-matched inactive-UOX, chassis, and PULSE-mixture controls plus explicit zero-urate controls (81 wells/plate). Peer review removed a duplicate intracellular-catalase arm and made every control's substrate assignment executable.

**Informs:** [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) · [gut-lumen sink](./gut-lumen-sink.md) · [engineered koji protocol](./engineered-koji-protocol.md)

**Detail:** [interpretive](./uricase-topology-oxygen-peroxide-design-computational.md) · [experiment folder](./etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/) · Complete first pass

---

### comp-044 — Gut-Lumen Uricase Physiological-Regime Robustness Audit (2026-07-13)

**Question:** Is comp-019's unconditional flat-dose classification robust to explicit substrate occupancy and a finite active window under the inherited priors?

**Verdict:** **COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics.** Using the inherited central priors, the 0.59 µM, Km 25 µM, three-hour diagnostic gives capacity ratios 0.093 / 0.466 / 0.932 at 5 / 25 / 50 mg before additional oxygen, access, or survival penalties, versus the legacy 32.3 / 161.7 / 323.4 saturated-capacity calculation. This is an internal-consistency counterexample. It supplies no replacement ΔSUA, dose, genotype order, physiological regime, efficacy model, topology/chassis selection, production-sufficiency target, or safety conclusion.

**Key findings:** 1,620-cell discrete full-factorial per dose; grid occupancy is not probability; no serum-urate mapping. The 8.3 U/mg activity, Km range, 2–4-hour window, and 233 mg/day denominator are inherited or derived, non-planning-grade inputs. Oxygen, access, survival, and pH attenuation are nonmechanistic scenario multipliers; oxygen stoichiometry and peroxide safety are not modeled. Only the ratio-one boundary has direct meaning within the diagnostic.

**Informs:** [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) · [H08](./hypotheses/H08-gut-lumen-sink-platform-thesis.md) · [comp-019 interpretation](./uricase-abcg2-genotype-stratification-computational.md)

**Detail:** [interpretive](./gut-lumen-uricase-physiologic-regime-computational.md) · [experiment folder](./etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/) · Complete first pass

---

### comp-043 — EcN Periplasmic Disulfide-Folding Arithmetic — INVALIDATED MODEL (2026-07-13)

**Question:** Which exact-configuration measurements are needed before assigning an EcN configuration to C1-INH, DAF SCR1-4, or lactoferrin?

**Verdict:** **Invalidated and retired.** The arbitrary weighting formula and pLDDT-as-accessibility axis cannot establish periplasmic folding capacity, protease survival, viability, priority, or a chassis winner.

**Key findings:**
- The live corpus does not preserve the invalid numerical outputs; Git is the audit trail.
- DAF and lactoferrin have distinct disulfide-containing native folds, but annotation does not predict native-fold attainment. Reverify exact feature counts against the current primary record before using them as design inputs.
- **Single biggest unresolved question:** exact-configuration expression, native-fold attainment, secretion, stability, and retained function. No calibrated DsbA/DsbC capacity rule was identified for the proposed secreted configurations.
- Compare baseline and DsbC-co-expression arms; either result applies only to the tested construct × route × folding-support configuration.

**Informs:** [engineered-lbp-chassis.md](./engineered-lbp-chassis.md) (measurement priorities, not chassis assignment) · [chaperone-orthogonal-stacking.md](./chaperone-orthogonal-stacking.md) (capacity-calibration gap) · [validation-experiments.md](./validation-experiments.md)

**Detail:** [interpretive](./daf-lactoferrin-ecn-folding-feasibility-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/) · Next gate: exact-configuration expression, native-fold attainment, and retained-function measurement

---

### comp-042 — KPV self-delivery through GSDMD pyroptotic pores vs. the PepT1 baseline — YELLOW (provisional) (2026-07-13)

**Question:** Does the physics support KPV (Lys-Pro-Val) flooding into pyroptotic macrophages through GSDMD pores fast enough to clear its intracellular IC50 (A1 — flux sufficiency), and — the quietly weak assumption — does the pore confer real *selectivity* over the PepT1 (SLC15A1) transporter route KPV already has (A2)? Stress-tests the [GSDMD pore self-delivery paradox](./gsdmd-pore-delivery-paradox.md) "Trojan-horse" thesis for KPV specifically.

**Verdict:** **YELLOW (provisional).** Split three ways — (a) **KPV as a *selective* Trojan-horse payload: effectively falsified**; (b) **KPV reaching therapeutic intracellular levels via the pore: GREEN (intra-articular), marginal (SC), RED (oral)**; (c) **the *platform* thesis (pore delivery of a transporter-orphan membrane-impermeant payload): genuinely open.** A ~20 nm pore equilibrates intracellular [KPV] to the extracellular synovial concentration within **~2 s** (τ_eq ≪ the minutes-scale pore lifetime), so flux is never the constraint — but because KPV already enters cells via PepT1, the pore confers no demonstrable selectivity, gated entirely by uncharacterized synovial-macrophage PepT1 expression.

**Key findings:**
- **Answers [paradox-page](./gsdmd-pore-delivery-paradox.md) Open Question #4 (pore lifetime):** for a ~1 nm solute through a 20 nm pore, equilibration is complete in seconds; even the short end of the 1–30 min lifetime range is far longer than needed. Peak intracellular [KPV] is *capped at synovial [KPV]* (the naive moles-in/volume estimate overshoots by ~140×, confirming saturation).
- **A1 flux:** IA clears the 10 nM IC50 (Dalmasso 2008) by ~29,000×; SC ~3× (assumption-limited); oral ~0.1× (fails). Robust for pores/cell ≥ ~10.
- **A2 selectivity:** meaningful (≥3×) only if synovial macrophages lack functional PepT1 — but immune-cell PepT1 is *demonstrated* (Jurkat; Dalmasso 2008). At moderate/high PepT1, selectivity collapses to ~1 or below (healthy cells accumulate KPV *more* via concentrative electrogenic PepT1 + intact Vm). No route passes both a therapeutic and a selectivity threshold.
- **Conceptual kill:** PD timing mismatch — KPV is an *upstream* inhibitor (NLRP3 assembly / NF-κB priming); pores open *downstream* of inflammasome firing, so pore-delivery arrives after KPV's target has acted and IL-1β is released.
- **KPV is the wrong molecule to *demonstrate* pore-selectivity** (it has a transporter and resists intracellular degradation — both anti-selective). A transporter-orphan, intracellularly-labile impermeant payload is the clean probe.
- Method: diffusive-flux / mass-balance with two-sided access resistance; MM PepT1 baseline; 20k Monte Carlo; lifetime × pores/cell robustness sweep. No MD, no docking. Grep-verify gate passed; ≥3 compounding named assumptions → provisional.

**Informs:** [gsdmd-pore-delivery-paradox.md](./gsdmd-pore-delivery-paradox.md) (Open Question #4 + KPV-payload stress-test) · [kpv-peptide.md](./kpv-peptide.md) · [validation-experiments.md §1.32](./validation-experiments.md) (reframes the fluorescent-KPV-uptake wet-lab: adds mandatory PepT1-blockade arm + transporter-orphan tracer) · [delivery-route-matrix.md](./delivery-route-matrix.md)

**Detail:** [interpretive](./kpv-gsdmd-pore-influx-computational.md) · [experiments/](./etc/experiments/comp-042-kpv-gsdmd-pore-influx/) · Complete first pass (next gate: synovial-macrophage PepT1 expression measurement + transporter-orphan pore-selectivity delivery test)

---

### comp-039 — CFH-dependence mechanism-dissociation of dietary upstream-CP0 candidates — CFH-INDEPENDENT (rosmarinic acid High, luteolin Medium, HCP/HCPM/CHCP High, Helicteres Medium-replication-bounded) (2026-05-21)

**Question:** For rosmarinic acid, luteolin, exact *Houttuynia cordata* polysaccharide materials, and *Helicteres* benzofuran lignans, does the candidate's anti-complement mechanism require functional CFH? Candidate identity comes from current evidence homes, not a COMP-018 ranking.

**Verdict:** **All four candidates classified CFH-INDEPENDENT within the cited mechanism records.** The *Helicteres* classification is conditional on a single-paper anchor and requires independent replication before translational use.

**Key findings:**
- Two-model independent cross-check (Claude Opus 4.7 = Model A; DeepSeek `deepseek/deepseek-chat-v3` = Model B): both models AGREE on classification for all four candidates.
- Two-model DISAGREEMENT on predicted Y402H × candidate × incident-gout direction: Model A predicts negative direction (effect ≥ in carriers, because Y402H baseline severity amplifies absolute effect size); Model B predicts null (mechanism independence implies genotype indifference). Both reject the AMD-paradox direction (carriers worse). For UKB cross-tab, both predictions need separate falsification thresholds.
- CFH Y402 structural footprint grep-verified: Sushi/CCP 7 = aa 387-444 of UniProt P08603. The four candidates' binding sites all map to upstream complement nodes (C3 thioester, C3 itself, classical-pathway C2 + C4 + C1q), not the CCP6-8 CRP/GAG-binding surface.
- Recommended lead UKB cross-tab: rs1061170 × Phenol-Explorer-derived rosmarinic-acid intake × incident gout M10.x. Secondary: rs1061170 × Apiaceae-family intake × incident gout. *Helicteres* is not actionable until independent replication closes.
- Total OpenRouter spend: ~$0.0022 (Model B counter-reads × 4 candidates).
- Follow-ups: comp-040 (proposed) — wet-lab CFH-depleted-serum MSU-crystal assay as definitive falsification test; comp-041 (proposed) — East Asian cohort feasibility scan for Houttuynia × CFH cross-tab.

**Informs:** [gout-genetic-variants.md](./gout-genetic-variants.md) Category 5 CFH row · [complement-c5a-gout.md](./complement-c5a-gout.md) §6.3 · [upstream-complement-modulator-sweep-computational.md](./upstream-complement-modulator-sweep-computational.md) · [upstream-complement-verification-rerun-computational.md](./upstream-complement-verification-rerun-computational.md) · [logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md](../logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md)

**Detail:** [interpretive](./cfh-mechanism-dissociation-cp0-candidates-computational.md) · operations workspace: [`operations/cfh-mechanism-dissociation-2026-05-21/`](../operations/cfh-mechanism-dissociation-2026-05-21/) · Complete first pass (next gate: UKB collaboration ask + comp-040 wet-lab depletion assay)

---

### comp-038 — Tier 2 Butyrate Assay Audit — YELLOW (2026-05-20)

**Question:** Is there a Tier 2 butyrate quantification assay (colorimetric, enzymatic, breath-proxy, electrochemical, or other low-cost intermediate method) that can be validated against Tier 3 GC-MS for stool, serum, breath, or culture-supernatant matrices?

**Verdict:** **YELLOW.** No ready-to-adopt Tier 1 or Tier 2 butyrate assay was established for current OE use. The scan surfaced a Tier 3 HPLC-UV method for culture supernatants and a separate electrochemical/ANN Tier 2 candidate for stool. Neither has been validated for an OE matrix or workflow.

**Key findings:**
- PubMed snapshot: 27 queries / 74 records; source snapshot committed at `outputs/pubmed-snapshot.json`.
- HPLC-UV is a Tier 3 bench method under the current ladder. De Baere 2013 (PMID 23542733) supports bacterial-culture-supernatant use; the remaining gate is transfer into one exact OE strain–medium matrix with a GC-MS comparison ([validation §1.31](./validation-experiments.md#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms)).
- Gu 2026 (PMID 42041444) supports an electrochemical/ANN stool-specific Tier 2 candidate compared with GC-MS in a 30-sample fecal test set. Independent reproduction of the complete hardware–chemistry–model stack and external transfer remain open ([validation §1.45](./validation-experiments.md#145-fecal-butyrate-electrochemicalann-reproducibility-and-transfer-gate)).
- Breath H2/CH4 is useful as a broad fermentation/adherence proxy, not butyrate-specific quantification.
- Generic free-fatty-acid colorimetric kits are a false-friend class; representative protocol excludes acetic, propionic, and butyric acid.
- Completed with Codex/GPT-5.5 in-session synthesis from a committed source packet; no OpenRouter model calls were made.

**Informs:** [quantification-ladder](./quantification-ladder.md) · [genotype-informed-supplement-workflow](./genotype-informed-supplement-workflow.md) · [validation-experiments §1.14](./validation-experiments.md#114-abcg2-response-to-dht-and-tnf-with-butyrate-and-lactoferrin-rescue) · [purine-degrading-bacteria](./purine-degrading-bacteria.md)

**Detail:** [interpretive](./tier-2-butyrate-assay-audit-computational.md) · [experiments/](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/) · Complete first pass; corrective artifact/provenance review and matrix-specific validation remain open.

---

### comp-037 — C1-INH (SERPING1) EcN-Luminal Protease/Glycosylation Proxy — INVALIDATED MODEL (2026-05-17)

**Question:** Which sequence-filter, structure-confidence, glycosylation, and kinetic questions should be tested for a human C1-INH (UniProt P05155) payload produced by engineered *E. coli* Nissle 1917?

**Verdict:** **Proxy only; empirical protease and glycosylation effects unresolved.** The inherited LOW/RED labels used pLDDT as accessibility. Polypeptide-encoded serpin chemistry motivates testing an unglycosylated core, but exact-configuration folding, luminal stability, productive target engagement, and retained inhibition remain empirical gates.

**Key findings:**
- **Disulfide count grep-verified against UniProt FT DISULFID: exactly 2 disulfides** (C123-C428, C130-C205) on the SV=2 entry. This is a sequence annotation, not folding evidence.
- **Candidate construct: serpin core aa 123–500.** This exact boundary preserves the two annotated disulfides and RCL while making mucin-domain truncation directly testable; the proxy does not validate the construct.
- UniProt features record N-glycans at 25, 69, 81, 238, 253, 272-variant, and 352 plus O-glycans at 47, 48, 64, 71, 83, 88, 92, and 96. The effect of removing the native N-terminal region remains empirical.
- The retired five-enzyme filter panel did not model concentration, extended specificity, matrix, export topology, or kinetics and supplies no survival result.
- Glycosylation precedents justify an unglycosylated test arm; they do not establish that an EcN-produced construct will fold or retain activity in the intended compartment.

**Informs:** [complement-c5a-gout §9.8](./complement-c5a-gout.md) · [complestatin-bgc-lbp-feasibility-computational](./complestatin-bgc-lbp-feasibility-computational.md) (comp-024 boundary) · [engineered-lbp-chassis](./engineered-lbp-chassis.md) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) (sister-thread DAF SCR1-4 on koji) · [current C1-INH evidence](./c1-inh-protease-stability-ecn-computational.md)

**Detail:** [interpretive](./c1-inh-protease-stability-ecn-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-037-c1-inh-protease-stability-ecn/) · Exact-configuration folding, stability, kinetics, and function remain open

---

### comp-035 — Intra-articular Uricase H₂O₂ Reaction-Diffusion (3 Architectures) — NON-DECISION-GRADE PHASE-0 PRIOR (2026-05-16; downgraded 2026-07-14)

**Question:** What does a first-pass, well-mixed steady-state model predict for H₂O₂ handling by Pickering emulsion, uricase-catalase fusion, and free co-formulated catalase architectures?

**Verdict:** **Non-decision-grade Phase-0 prior; no architecture is cleared or selected.** The frozen v1 runs produced historical median/p95 values of 0.19/1.1 µM for Pickering, 0.034/0.20 µM for fusion, and 0.19/7.2 µM for free co-formulation. Those values describe the implemented assumptions only. They do not establish tissue safety because the steady-state threshold was unverified, loading and active-site accounting were unresolved, and local gradients and exposure time were not modeled.

**Key findings:**
- Within the model, the low Pickering shell Damköhler result suggests that proximity alone did not drive the predicted bulk values; the alternative bulk-catalase explanation remains input-dependent and empirically unvalidated.
- comp-035 does not establish a safe steady-state threshold, an architecture or chassis winner, or a basis for economics-driven selection.
- Remaining gates are a matched reaction-site H₂O₂ time course; catalase activity, stoichiometry, retention, and diffusion; local exposure; and tissue safety.

**Informs:** [chassis-pending-interventions §6](./chassis-pending-interventions.md) · [gout-kill-chain-delivery-routes](./gout-kill-chain-delivery-routes.md) · [delivery-route-matrix](./delivery-route-matrix.md) · [engineered-koji-protocol](./engineered-koji-protocol.md)

**Detail:** [interpretive](./intra-articular-uricase-h2o2-reaction-diffusion-computational.md) · [frozen v1 artifact](./etc/experiments/comp-035-ia-uricase-h2o2-reaction-diffusion/) · Reviewed; non-decision-grade

---

### comp-034 — Lactoferrin Inter-Lobe Linker Redesign — INVALIDATED MODEL

**Question:** If direct testing identifies a reproducible linker-associated failure, can the exact connector be redesigned while preserving lactoferrin fold and function?

**Verdict:** **No candidate ranking survives.** The model reused COMP-005's unverified protease-preference table as a biological cleavage axis. ProteinMPNN and Rosetta supplied additional model scores but did not validate that target. Cleavage values, GREEN/STRICT tiers, concordance claims, winners, and wet-lab priorities are invalid.

**What survives:** The exact connector remains a candidate engineering region only after WT fragment mapping or retained-function data identify a reproducible failure. A new design COMP must bind verified specificity and structural constraints before generating a matched diversity panel.

**Informs:** [validation-experiments §1.10](./validation-experiments.md) · [lactoferrin-protease-stability-computational](./lactoferrin-protease-stability-computational.md) · [etc/bio-ai-tools](./etc/bio-ai-tools.md) · [lactoferrin](./lactoferrin.md)

**Detail:** [interpretive](./lactoferrin-linker-redesign-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-034-lactoferrin-linker-redesign/) · Historical artifact retained in Git

---

### comp-029 — Combined CP0 Scenario (RA + DAF SCR1-4) — INVALIDATED MODEL

**Question:** Could rosmarinic acid and active DAF SCR1-4 suppress MSU-associated complement activation more than either exact material alone?

**Result boundary:** Every numerical result, interval, category, co-localization claim, complementarity claim, and routing conclusion is invalid. The live corpus does not preserve those outputs; Git is the audit trail.

**Next test:** Once an active DAF preparation exists, compare vehicle, rosmarinic acid, DAF SCR1-4, and their combination in one matched MSU-associated complement assay. Measure C5a, C5b-9, DAF recovery, retained function, and surface association; do not route the experiment with an inferred accessibility coefficient.

**Informs:** [complement-c5a-gout §9.7](./complement-c5a-gout.md) · [validation experiments](./validation-experiments.md) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md)

**Detail:** [current evidence](./combined-cp0-systems-model-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-029-combined-cp0-systems-model/)

---

### comp-036 — Repeat-Dose Inhaled mRNA-IL-1Ra PK/PD (Receptor-Occupancy Framing) — YELLOW (2026-05-16)

**Question:** Does multi-administration inhaled mRNA-IL-1Ra dosing achieve clinically-meaningful sustained IL-1R1 receptor occupancy over the 72h acute gout flare window — how many doses, at what frequency, with what confidence bounds?

**Verdict:** **YELLOW.** Repeat dosing partially salvages comp-033's RED single-dose Cmax verdict, but the high-confidence GREEN bar (median 95% of the 0-72h flare window above 80% receptor occupancy AND p25 ≥ 50%) is NOT reached by any of three regimens tested (QD ×1–14, BID ×2–28, Loading 2× + QD-maintenance ×0–14). Modality viable but at the edge — wet-lab dose-finding needed.

**Key findings:**
- Reframe from plasma Cmax-vs-anakinra (comp-033) to receptor-occupancy fraction over the 0–72h gout flare window — the clinically-relevant metric for a competitive antagonist. 80%-occupancy plasma threshold: median 73 ng/mL (p05–p95: 9–553).
- Kd_nM is now the #1 sensitivity driver (Spearman ρ = −0.69), surfacing previously-implicit uncertainty. IL-1Ra-IL-1R1 Kd ~1 nM (Arend 1990 JCI, range 0.1–10 nM).
- comp-033 RED single-dose verdict does not close the modality; repeat-dose receptor-occupancy is the right gate going forward.

**Informs:** [chassis-pending-interventions §4](./chassis-pending-interventions.md) · [inhaled-mrna-il1ra-pulse-computational](./inhaled-mrna-il1ra-pulse-computational.md) · [etc/open-enzyme-vision §10](./etc/open-enzyme-vision.md)

**Detail:** [interpretive](./repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md) · [experiments/](./etc/experiments/comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd/) · Complete v1

---

### comp-033 — Inhaled mRNA-IL-1Ra Pulse Therapy Dose Modeling — RED on systemic anakinra-equivalent (2026-05-16)

**Question:** Does dose modeling show pulmonary IL-1Ra expression can plausibly reach anakinra-equivalent therapeutic exposure at currently-feasible inhaled-mRNA doses (4–24 mg per administration), and which inhaled-mRNA programs / CDMOs are forkable partners?

**Verdict:** **RED on the systemic-anakinra-equivalent gate.** Median predicted plasma Cmax 0.025 µg/mL = 1/60th anakinra (1.5 µg/mL); only p95 (0.28 µg/mL) approaches anakinra-trough (0.05 µg/mL). Reverse-dose calc: ~195 mg mRNA per administration to reach 0.5 µg/mL median; ~585 mg for full anakinra benchmark — both 8–25× the highest disclosed inhaled-mRNA clinical dose (24 mg, Translate Bio MRT5005). Verdict does NOT close the modality — comp-036 reframed to receptor-occupancy and pulls it back to YELLOW.

**Key findings:**
- Dose-feasibility gap is the load-bearing finding; current inhaled-mRNA platforms are 1–2 orders below what plasma-Cmax-equivalence would require.
- Three honest paths forward: (a) repeat dosing (→ comp-036), (b) reframe to local-pulmonary IL-1Ra exposure for inflammation-of-lung indications, (c) different target where lower Cmax suffices.
- Partner-ID surface: Translate Bio (now Sanofi), Moderna, Arcturus, Ethris — none currently aimed at IL-1Ra; chassis-pending §4 stays active as a temporal-stack platform-positioning entry.

**Informs:** [chassis-pending-interventions §4](./chassis-pending-interventions.md) · [etc/open-enzyme-vision §10](./etc/open-enzyme-vision.md) · [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) · [delivery-route-matrix](./delivery-route-matrix.md) · [repeat-dose-inhaled-mrna-il1ra-pkpd-computational](./repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md) (comp-036 reframe)

**Detail:** [interpretive](./inhaled-mrna-il1ra-pulse-computational.md) · [experiments/](./etc/experiments/comp-033-inhaled-mrna-il1ra-pulse-therapy/) · Complete v1

---

### comp-047 — ABCG2 Q141K Pharmacological-Chaperone Re-screen (real docking) — INCONCLUSIVE (2026-07-14)

**Question:** Same as comp-032 — is there an FDA-approved molecule that binds a fold-stabilizing NBD site on Q141K ABCG2 (not the ATP pocket), not a known ABCG2 inhibitor, worth a wet-lab trafficking assay? Re-asked with **real AutoDock Vina docking** instead of comp-032's descriptor heuristic.

**Verdict:** **INCONCLUSIVE (honest null).** Of 134 docked molecules: 0 high-confidence candidates, 2 marginal "uncertain" (rosuvastatin, vorinostat). The decisive result is in the controls: the **4 CFTR-corrector positive controls failed to earn rank** (0/4 reached candidate tier, no class prior), while all 13 known ABCG2 inhibitors were correctly rejected (0 false positives). Because the positive controls don't separate from the field, the screen has no demonstrated power to find real chaperones.

**Key findings:**
- **Empirically confirms the comp-032 audit.** Removing comp-032's class prior and making the same CFTR-corrector controls earn rank from docking → they fail (ivacaftor rank 91/134; lumacaftor is the #2 fold binder but binds the ATP pocket harder, margin −1.42). comp-032's "chaperone signal" was the prior.
- **Two failure reasons:** (1) the fold-vs-transport margin is confounded — the ATP/Walker-A pocket is a strong generic binder (median transport −6.09 vs fold −4.86 kcal/mol), so "prefers fold site" selects against almost everything; boxes are disjoint (32.6 Å apart), not an overlap artifact. (2) Rigid-receptor docking can't model the chaperone mechanism (folding-intermediate stabilization / ΔTm).
- **Two honest residual gaps:** sensitivity analysis did not run (no sensitivity.json); Axis 2 (ChEMBL) populated for only 3/135 molecules — known-inhibitor disqualification otherwise rests on curated role-tags. Neither changes the null (which rests on Axis 1 controls failing).
- **Next step is not another docking pass** — it's folding-ΔΔG modeling (MD / Rosetta) or a wet-lab Q141K trafficking + urate-flux + ABCG2-inhibition counterscreen.

**Detail:** [interpretive](./abcg2-q141k-chaperone-rescreen-computational.md) · [experiments/](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/) · supersedes comp-032

---

### comp-032 — ABCG2 Q141K Pharmacological-Chaperone Virtual Screen — ~~GREEN~~ SUPERSEDED (2026-05-16; superseded by comp-047 2026-07-14)

> **⚠️ Verdict RETRACTED.** The GREEN below is a descriptor/class-prior heuristic whose positive-control validation was tautological (comp-review 2026-07-13). [comp-047](./abcg2-q141k-chaperone-rescreen-computational.md) re-ran it with real docking → INCONCLUSIVE (positive controls failed to earn rank). Retained as frozen record; do not cite as support.

**Question:** Is there an FDA-approved small molecule that binds ABCG2 Q141K's nucleotide-binding domain (NBD) and could rescue trafficking, or does the FDA-approved drug surface lack chaperone-active hits — requiring novel chemistry?

**Verdict (retracted):** ~~**GREEN.** Shortlist of 10 candidates passes the four-gate filter.~~ The shortlist is a prior-weighted descriptor ranking, not binding/rescue evidence; the "all four CFTR controls above decoy max" claim is a formula artifact of the 0.15 decoy prior (0.15^(1/5) = 0.684), not independent validation.

**Key findings (historical, retracted as evidence):**
- Three chemistry classes scored ≥ 0.85 (CFTR correctors, tetramer stabilizers, bile-acid chaperones) — but the ranking is driven by the hand-assigned class prior, and ABCG2 *inhibitors* also scored high (the confound comp-047's Axis 2 targets).
- Real-docking re-screen (comp-047) is now **complete → INCONCLUSIVE**, not the hypothesis-confirming step comp-032 anticipated. Do NOT treat the repurposing surface as empirically supported; do NOT queue a compounding-pharmacy conversation on this route.

**Informs (now downgraded to hypothesis-only):** [chassis-pending-interventions §7](./chassis-pending-interventions.md) · [abcg2-modulators](./abcg2-modulators.md) §"Pharmacological-chaperone route" · [compounding-pharmacy-track](./compounding-pharmacy-track.md)

**Detail:** [interpretive (superseded)](./abcg2-q141k-chaperone-screen-computational.md) · [experiments/](./etc/experiments/comp-032-abcg2-q141k-chaperone-screen/) · superseded by [comp-047](./abcg2-q141k-chaperone-rescreen-computational.md)

---

### comp-031 — Dual-chassis EcN PDB + Uricase Additive SUA Prediction — **INVALIDATED 2026-07-13**

**Original question:** Would PDB-EcN plus luminal UOX produce additive ΔSUA and a PDB-derived butyrate→ABCG2/Q141K synergy?

**Current verdict:** **INVALIDATED.** The model inherited comp-019's unsupported saturation regime, transferred *C. sporogenes* butyrate yield into CBT2.0/EcN without product measurement, misattributed direct butyrate rescue to Basseville 2012, and added unmatched background butyrate to the combination arm. Its ΔSUA, competition, butyrate, Q141K-rescue, and two-strain engineering recommendations are retired.

**Replacement work:** [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) reopens the UOX regime; [comp-046](./staged-purine-sink-mass-balance-computational.md) conserves dietary fate, treats the endogenous side as a capture-fraction comparison, and supplies a conditional architecture boundary; [validation §1.37](./validation-experiments.md#137-cbt20-carbon-fate-and-pdb-self-niche-test) measures actual CBT2.0 products.

**Detail:** [invalidated interpretive page](./dual-chassis-ecn-pdb-uricase-computational.md) · [current invalidation record](./etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/) · obsolete model preserved only in Git history

---

### comp-027 — Disulfiram Dose Modeling for GSDMD Blockade vs DER Ceiling — hypothesis-generator (2026-05-16; downgraded from YELLOW-leaning-GREEN by comp-review 2026-07-14)

**Question:** Is there a sub-AUD oral disulfiram dose window where plasma DSF engages GSDMD (CP6b pyroptotic-exit block) at a therapeutically meaningful level while plasma Me-DTC stays below the ALDH-inhibition threshold driving the disulfiram-ethanol reaction (DER)?

**Verdict (downgraded to hypothesis-generator, comp-review 2026-07-14):** a **single strict-GREEN modeled point at 100 mg/day** under current (unverified) Cmax + ALDH-calibration assumptions — **NOT a validated "75–125 mg/day window"** (those bounds were broadened from the single point, and 100 mg/day sits exactly on a hard-coded decision boundary). Hypothesis to test, not a dose recommendation. At 100 mg/d: ~57% GSDMD blockade (DSF Cmax ~0.4 µM) at ~40% ALDH inhibition (Me-DTC ~70 nM, right at Faiman DER hypotension threshold). Below 50 mg/d, GSDMD blockade drops <40%; above 125 mg/d, ALDH inhibition crosses DER threshold. Strict-GREEN at 100 mg/d under conservative cell-free EC50 anchor; cellular-preincub anchor extends GREEN down to 50 mg/d. Gates the 503A compounding-pharmacy disulfiram pathway.

**Key findings:**
- Sub-AUD DSF is a **selective GSDMD inhibitor**, not a pan-NLRP3 inhibitor — the NLRP3-palmitoylation pathway (Xu 2024, 10 µM EC50) is NOT engaged at any sub-AUD dose.
- DER threshold is the load-bearing ceiling; alcohol-abstention requirement is a compliance question for the 503A protocol.
- Two EC50 anchors (cell-free vs cellular-preincub) bracket the GREEN window; cellular-preincub captures covalent-accumulation kinetics and is the more defensible anchor for chronic dosing.

**Informs:** [compounding-pharmacy-track §6](./compounding-pharmacy-track.md) · [disulfiram](./disulfiram.md) · [nlrp3-exploit-map](./nlrp3-exploit-map.md) CP6b

**Detail:** [interpretive](./disulfiram-dose-modeling-computational.md) · [experiments/](./etc/experiments/comp-027-disulfiram-dose-modeling/) · Complete v1

---

### comp-024 — Complestatin-Family BGC / LBP Proxy — INVALIDATED MODEL (2026-05-16)

**Question:** Can the historical hand-scored model establish a tractable LBP chassis or choose complestatin versus C1-INH as the next CP0 payload?

**Verdict:** **Invalidated and retired.** Hand-assigned factors, arbitrary color thresholds, and an incomparable nine-factor-versus-eleven-factor composite cannot establish feasibility, a chassis, comparator superiority, or portfolio priority.

**Key findings:**
- Chiu 2001 reported a 48.7 kb cluster with 16 open reading frames and seven NRPS modules; Park 2016 reconstituted a 54.5 kb cluster in *S. lividans* and recovered monocyclic M55 and linear S56 from gene-deletion experiments.
- The accessible Park primary record does not establish that M55 or S56 was inactive.
- An exact host × oxygen-regime experiment must recover chemically identified, functionally active crosslinked product before the active-product-formation hypothesis advances. Delivery, access, safety, and priority require separate evidence.
- C1-INH is a separate conjecture requiring exact-construct expression, folding, glycosylation-dependence, stability, function, and access measurements.

**Informs:** [complement-c5a-gout §9.8](./complement-c5a-gout.md) · [engineered-lbp-chassis](./engineered-lbp-chassis.md) · [modality-chokepoint-matrix](./modality-chokepoint-matrix.md)

**Detail:** [current evidence](./complestatin-bgc-lbp-feasibility-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-024-complestatin-bgc-lbp-feasibility/)

---

### comp-030 — DAF SCR1-4 Cassette Ranking — INVALIDATED MODEL (2026-05-15)

**Question:** Which expression and processing configuration can produce intact, natively folded, functional DAF SCR1-4 in *A. oryzae*?

**Verdict:** **Invalidated and retired.** The candidate scores, promoted sets, codon preference, direct-secretion ranking, ESM2 pseudo-pLDDT inference, chaperone-load coefficients, and cross-target generalizations do not support candidate selection or experimental routing.

**Key findings:**
- No numerical rank, count, preferred codon strategy, promoter, signal peptide, processing route, or fold/secretion conclusion survives.
- Direct secretion and GlaA-KEX2 remain unranked candidate routes. Codon variants may be an independent factor, but the retired model supplies no preferred variant.
- Compare exact constructs under matched conditions and measure expression, processing fidelity, native-fold attainment, intact secreted product, and retained complement-regulatory function.

**Informs:** [validation-experiments §1.25](./validation-experiments.md) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md)

**Detail:** [current evidence](./daf-cd55-scr14-cassette-ranking-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-030-daf-cassette-ranking/)

---

### comp-022 — *A. oryzae* Uricase Cassette Search Space — CORRECTIVE REVIEW OPEN

**Question:** Across the *A. oryzae* uricase cassette design space (43,200 combinations), which cassettes survive a multi-model concordance gate?

**Current verdict:** **Enumeration survives; the shortlist does not currently authorize candidate selection.** One ranking axis uses uncalibrated chaperone-load coefficients inherited from the retired folding-score framework. The other axes describe different intermediate properties and were not calibrated to one shared biological outcome. The open review must recompute or retire every shortlist and “winner” claim dependent on that axis; §1.33 separately determines whether an exact configuration works under the intended physiological conditions.

**Key findings:**
- The enumerated promoter, signal-peptide, codon, scaffold, and routing choices remain a hypothesis inventory, not a ranked build list.
- The reported N-of-5 tiers, direct-secretion cluster, gene-synthesis refinements, and GlaA-KEX2 ordering depend on the current scoring system and are not decision-eligible.
- PTS1 masking, codon design, direct secretion, GlaA-KEX2 processing, and other topologies remain separate empirical configuration questions.
- v1 GC-clamp proxy vs real ViennaRNA MFE Spearman ρ = 0.241; v2 materially shifted ranks while preserving the internal direct-secretion cluster.

**Informs:** [validation-experiments §1.33 (topology gate) + conditional §1.9B](./validation-experiments.md) · [cassette-compatibility-computational](./cassette-compatibility-computational.md) · [koji-endgame-strain §3.4](./koji-endgame-strain.md) · [etc/autonomous-screening-methodology](./etc/autonomous-screening-methodology.md)

**Detail:** [current evidence boundary](./uricase-cassette-ranking-computational.md) · [open corrective review](../synthesis/queue/comp-review-022.md) · [artifact](./etc/experiments/comp-022-clockbase-uricase-cassette-ranking/)

---

### comp-023 — *cns1+cns2* Cordycepin-Burden FBA — INVALIDATED

**Question:** Could the encoded iWV1314 scenario establish the metabolic burden or multi-cassette compatibility of a *cns1+cns2* cordycepin route?

**Verdict:** **Invalidated, non-runnable artifact.** The model converted source-reported batch-average productivity into a fixed continuous mmol/gDW/h demand using an assumed biomass density without time-resolved, condition-matched calibration. Together with unverified pathway assumptions, an artificial export bound, broken scenario boundaries, and separate capacity maxima mislabeled as yields, this prevents any burden, flux, breakpoint, product, feasibility, or compatibility conclusion.

**What survives independently:** Jeennor et al. directly demonstrated *cns1+cns2*-enabled cordycepin production in *A. oryzae* in their tested configuration (PMID 38071331). A cytosolic route avoiding direct ER-folding competition remains an unranked research conjecture; the exact four-arm isogenic product-and-cell-state experiment is specified on the evidence page.

**Informs:** [cordycepin route and experimental gate](./cordycepin-cassette-burden-computational.md) · [chaperone-orthogonal-stacking](./chaperone-orthogonal-stacking.md) · [validation-experiments](./validation-experiments.md)

**Detail:** [evidence page](./cordycepin-cassette-burden-computational.md) · [non-runnable tombstone](./etc/experiments/comp-023-cns1-cns2-metabolic-burden/)

---

### comp-018 — Upstream Complement Modulator Sweep — INVALIDATED CATALOG (2026-05-17)

**Question:** Across all compound classes, which compounds have documented activity at upstream complement cascade nodes proximal to C5a generation, and which are gout-platform-relevant?

**Verdict:** **Retired as a computational experiment.** The script counted fields in a hand-curated catalog; it did not rerun searches, verify primary evidence, enforce translation review, or validate tiers. Cross-assay rankings, counts, dietary conclusions, chassis extrapolations, and engineering priorities are invalid.

**Key findings:**
- Rosmarinic acid, luteolin, and *Helicteres* compounds remain assay-specific leads governed by the independently scrubbed COMP-020 evidence boundary.
- *Houttuynia cordata* polysaccharides remain exact-material leads governed by the Houttuynia evidence page.
- C1-INH remains a separate exact-configuration expression, folding, stability, function, and access question.
- None of those leads inherits a rank, dietary inference, or chassis assignment from COMP-018.

**Current evidence homes:** [COMP-020](./upstream-complement-verification-rerun-computational.md) · [Houttuynia](./houttuynia-cordata.md) · [C1-INH](./c1-inh-protease-stability-ecn-computational.md)

**Detail:** [current routing page](./upstream-complement-modulator-sweep-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-018-upstream-complement-modulator-sweep/) · [brief-contamination retrospective](../operations/comp-018-vs-comp-020-retrospective.md)

---

### comp-020 — Upstream Complement Sweep (Brief-Scrubbed Verification Re-Run) — Phase 1 complete (2026-05-08)

**Question:** Across upstream complement nodes (C1q/MBL-MASP-2/C3 tickover/convertases/soluble factors/membrane regulators), which compounds (anchored only to target nodes, no compound names supplied, no prior comp-018 consulted) have documented direct modulator activity?

**Verdict:** **NO single headline compound.** Three classes occupy distinct top-tier mechanistic positions within ~5–20× of each other. **Top per node:** C1q — Helicteres benzofuran lignans + luteolin; MASP-2/LP — heparin oligos + Bupleurum polysaccharide; C3 convertase — rosmarinic acid (covalent IC50 34 µM, distinctive mechanism); marine sulfated polysaccharides 1–3 µg/mL.

**Key findings:**
- **Three independent scans now agree** (comp-013 + comp-014 + comp-020): ChEMBL is structurally biased (~20% NP coverage vs >70% kinase/GPCR). Primary-literature mining is the load-bearing tool.
- Published assay records span 34–1500 µM for rosmarinic acid and 2–102 µg/mL for heparin across different formats and conditions. Those descriptive ranges motivate matched-format replication; they do not establish format as the cause or supply an operative potency.
- Luteolin convergence-multi-mechanism candidate confirmed; rosmarinic acid is highest mechanistic-distinctiveness candidate (covalent C3b modification).
- Coverage gaps: Factor H upregulators (empty), CD55/CD59/CR1 upregulators (engineering territory), direct fungal upstream modulators (zero — extends comp-014).

**Informs:** [complement-c5a-gout](./complement-c5a-gout.md) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) · [tcm-gout-compound-triage-computational](./tcm-gout-compound-triage-computational.md) · [medicinal-mushroom-compound-mapping-computational](./medicinal-mushroom-compound-mapping-computational.md)

**Detail:** [interpretive](./upstream-complement-verification-rerun-computational.md) · [experiments/](./etc/experiments/comp-020-upstream-complement-verification-rerun/) · Phase 1 complete (Phase 2: CNKI/WanFang/J-STAGE + *Helicteres* replication + RA/MSU assay; matched assay-format stratification remains a separate conjecture)

---

### comp-001 — Uricase Shio-Koji Protease-Site Proxy (2026-05-05)

**Question:** Which Q00511 adjacent pairs match three fixed legacy preference filters, and what AlphaFold confidence surrounds each match?

**Verdict:** **Proxy only; empirical risk unresolved.** The analysis mapped adjacent-pair matches to unverified legacy filters and their pLDDT context. The filters are not established exhaustive protease-specificity rules, and pLDDT is model confidence rather than solvent accessibility or protease resistance.

**Key findings:**
- The fixed filters returned 215 ALP, 97 NPr, and 44 acid-protease adjacent-pair matches. These counts describe the encoded filters, not demonstrated cleavage sites.
- Q00511 has mean pLDDT 97.14 and minimum 80.50; no solvent-accessibility or SASA calculation was performed.
- The analysis did not measure cleavage, retained activity, salt-conditioned protease behavior in the ferment, or any fermentation outcome.

**Informs:** [validation-experiments §1.10](./validation-experiments.md) — supplies a fixed-filter and structural-confidence inventory while the empirical retained-activity assay remains the decision gate.

**Detail:** [interpretive](./uricase-protease-stability-computational.md) · [experiments/](./etc/experiments/comp-001-uricase-shio-koji-protease-stability/) · Complete

---

### comp-006 — DAF/CD55 Shio-Koji Protease Proxy (full ectodomain) (2026-05-05)

**Question:** What sequence-filter and AlphaFold-confidence prior does the inherited model provide for the DAF/CD55 soluble ectodomain (aa 35–353)?

**Verdict:** **Proxy verdict invalid; empirical protease risk unresolved.** The reported HIGH labels used pLDDT confidence as accessibility. The Ser/Thr-rich stalk has lower AlphaFold confidence than SCR1–4 and remains a testable engineering liability, but the model does not establish solvent exposure, cleavage, degradation, or survival.

**Key findings:**
- Removing the lower-confidence stalk is a falsifiable construct-design hypothesis, not a computationally validated stability improvement.
- SCR1–4 has high AlphaFold confidence, but COMP-001 is not a validated protease-stability benchmark and cannot support a cross-payload survival comparison.

**Informs:** [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) — Engineered soluble complement regulators row

**Detail:** [interpretive](./daf-cd55-protease-stability-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/) · Historical filter inventory only

---

### comp-015 — T-axis Adjuvant Urate-Target Mapping (v2) — H-AN-02 PARTIALLY FALSIFIED (2026-05-07)

**Question:** For four T-axis-active compounds (cordycepin, eurycomanone, icariin, echinacoside), what is the curated evidence at five urate-handling + T-axis targets (URAT1, ABCG2, OAT1, SHBG, XO)?

**Verdict:** **H-AN-02 PARTIALLY FALSIFIED.** Cordycepin = **GOUT-FAVORABLE** (URAT1 down + supplementary XO IC50 55.7 µM). Eurycomanone = **GOUT-FAVORABLE** (v1→v2 REVERSED; hURAT1 + GLUT9 down + ABCG2/NPT1 up + PRPS suppression + 2021 RCT SUA −7-11% n=105). Icariin / echinacoside = **MECHANISM-UNCLEAR**.

**Key findings:**
- v2 added XO panel after v1 missed eurycomanone XO mechanism trigger; the trigger was citation-laundering (PMID 31920654/34785103 establish transporter+purine-synthesis, not direct XO) but panel addition still correct.
- v2 finds 5 direct-evidence cells vs v1's 1; eurycomanone now better-characterized than cordycepin on urate axis.
- New chokepoint identified: **PRPS (phosphoribosyl pyrophosphate synthetase)** — eurycomanol mechanism, distinct from XO.

**Informs:** [androgen-natural-modulation §10 H-AN-02](./androgen-natural-modulation.md) · [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md) · [androgen-urate-axis](./androgen-urate-axis.md)

**Detail:** [interpretive](./t-axis-adjuvant-urate-mapping-computational.md) · [experiments/](./etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/) · Complete v2

---

### comp-016 — T × Intestinal ABCG2 Suppression Evidence Mining — WEAK / UNCONFIRMED (2026-05-07)

**Question:** Does primary literature support the load-bearing claim that androgens directly suppress intestinal ABCG2 expression at platform-relevant magnitudes?

**Verdict:** **WEAK / UNCONFIRMED (provisional; abstract-tier).** Of 17 studies, zero primary studies demonstrate androgen-driven intestinal ABCG2 suppression directly. 1 supports broader sex-dimorphism (Hoque 2020 Q140K mouse); 1 supports female-positive arm (Yu 2021, estradiol ↑ ABCG2); 1 directly contradicts (Klyushova 2023, T INDUCES via PXR/FXR).

**Key findings:**
- Intestinal compartment IS sex-dimorphic, but driver is **estradiol POSITIVE on female side**, not **androgen NEGATIVE on male side**.
- The platform thesis should not assume an androgen-driven ABCG2 ceiling or absent estradiol-positive signaling in healthy male physiology; hormone effects are context-dependent and require direct transport measurement.
- Sakamoto 2018 ADT cohort (−0.66 mg/dL at 6 months, n=489) consistent with URAT1-only renal mechanism; no direct AR-ARE on ABCG2 promoter identified.

**Informs:** [androgen-urate-axis](./androgen-urate-axis.md) · [abcg2-modulators](./abcg2-modulators.md) · [gut-lumen-sink](./gut-lumen-sink.md) · [koji-endgame-strain](./koji-endgame-strain.md) · [cross-validation](./cross-validation.md)

**Detail:** [interpretive](./t-abcg2-suppression-evidence-mining-computational.md) · [experiments/](./etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/) · Complete (full-text follow-up → comp-017)

---

### comp-019 — Gut-Lumen Uricase × ABCG2 Genotype Stratification + Flux Model — INVALIDATED TOMBSTONE

**Question:** Can the gut-lumen uricase sink produce meaningful SUA reduction in non-Q141K males, or does it rely on Q141K-positive disease-state vulnerability?

**Current verdict:** **INVALIDATED TOMBSTONE — non-runnable and not eligible for quantitative decision use.** Phase A found no Q141K-stratified uricase clinical outcome in the sources searched for comp-019 as of 2026-05-08; this is not a universal absence claim. COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics. COMP-044 supplies no replacement ΔSUA, dose, genotype order, physiological regime, efficacy model, topology/chassis selection, production-sufficiency target, or safety conclusion.

**Key findings:**
- No Q141K-stratified uricase clinical outcome was identified in the comp-019 searched corpus as of 2026-05-08.
- Physiological substrate, oxygen, access, survival, topology, and transit are now explicit gates.
- Q141K remains a prospective stratification variable; adequate dose and responder ordering are open.

**Replacement:** [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) · [comp-045](./uricase-topology-oxygen-peroxide-design-computational.md) · [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial)

**Detail:** [historical interpretation](./uricase-abcg2-genotype-stratification-computational.md) · [hash-bound tombstone](./etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/)

---

### comp-017 — Intestinal ABCG2 Sex-Dimorphism Public-Data Mining + 4-Paper Full-Text Re-Read — NULL OR NEAR-NULL at healthy baseline (2026-05-07)

**Question:** What do GTEx/HPA and four primary papers show about sex-stratified intestinal ABCG2? This was originally framed against H07 sub-claims 1 and 3; [H07](./hypotheses/H07-clomid-intestinal-er-antagonism.md) is now retracted, while the transporter result remains relevant.

**Verdict:** **NULL OR NEAR-NULL SEX-DIMORPHISM at healthy baseline (provisional).** Sex-dimorphism emerges only under **disease-state genetic stress** (Q140K LOF, Hoque) or **strong pharmacological perturbation** (100 µM E2, Yu; 1–100 µM sex hormones, Klyushova). Healthy-baseline literature converges on null.

**Key findings:**
- Hoque 2020 correction: Western-jejunum 78% : Western-kidney 44% (~1.8×), NOT comp-016's 88%:44%. Female FEUA unchanged (p=0.6263) — strong null on female protection.
- Yu 2021: Caco-2 active at 100 µM EB (5–6 orders above physiological serum E2); mechanism real at strong-pharmacological tier; physiological magnitude unestablished.
- Klyushova 2023: T/E2/P at 1/10/100 µM all increased ABCG2 via PXR/FXR rather than AR; this argues against direct AR-mediated intestinal ABCG2 repression at those supraphysiological exposures.
- Hosoyamada 2010 showed: T affects renal URAT1 mRNA only (protein unchanged); actual androgen-responsive renal urate transporter is **Smct1**, GLUT9 attenuated.

**Informs:** [retracted H07](./hypotheses/H07-clomid-intestinal-er-antagonism.md) · [t-abcg2-suppression-evidence-mining-computational](./t-abcg2-suppression-evidence-mining-computational.md) · [androgen-urate-axis](./androgen-urate-axis.md) · [abcg2-modulators §1](./abcg2-modulators.md) · [gut-lumen-sink](./gut-lumen-sink.md)

**Detail:** [interpretive](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md) · [experiments/](./etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/) · Complete (provisional; sandbox-blocked GTEx/HPA direct; Paperclip line-anchored re-run recommended)

---

### comp-014 — Medicinal Mushroom Compound × Chokepoint Mapping — Phase 3 complete (2026-05-17)

**Question:** Across all known characterized fungal natural products (globally, not Western pharma only), which compounds map onto OE chokepoints, and which fungal species are highest-leverage producers?

**Verdict:** **PHASE 3 COMPLETE as a bioactivity map.** 9,778 unified fungal compounds (LOTUS 6,798 + NPAtlas 4,535 + KNApSAcK 20 InChIKey-resolved; NPASS / TCMSP / HIT unreachable from sandbox — documented gap). ChEMBL returned **323 compound × target records across 12 of 24 queried chokepoints**; 177 / 9,778 compounds (1.81%) have at least one record. These are not uniformly favorable hits: assay context, substrate, and target-effect polarity must be verified before mechanistic interpretation. The mapped quercetin × ABCG2 EC50 = 30 nM record is polarity- and urate-context-unresolved.

**Key findings:**
- *Ganoderma* triterpenoid scaffold (ganoderic acids H/D and stereoisomers) emerges as highest-potency direct-binding hit at TNFα, **on top of** the Phase 2 *G. applanatum* 2,4-DAE urate-axis finding — two distinct chokepoint axes, both worth pursuing. *Ganoderma* spp. earn closer look.
- **Berkeleyamides / Berkeleyones** (Penicillium): first fungal natural products with direct sub-µM CASP1 and low-µM IL-1β hits — opens an inflammasome-effector-axis fungal candidate beyond the polysaccharide-priming literature comp-014 Phase 1 + Phase 2 emphasized.
- **Target-orphan rate 98.19%** — SwissTargetPrediction predicted-target layer is the next load-bearing step; sandbox-blocked here, deferred to re-run. 9,601 compounds with zero empirical chokepoint hits.
- **12 of 24 chokepoints have ZERO fungal-source ChEMBL hits**: NLRP3, ASC, GLUT9, C5aR1, Lp-PLA2, KEAP1, OAT4, PINK1, PDI, PDIA3, TXN, TXNIP. Confirms the comp-013 / comp-020 ChEMBL-Western-pharma-bias finding empirically for fungal-source NPs.
- Multi-target records identified: morin (ABCG2, CASP1, URAT1, XO) and genistein (ABCG2, CASP1, PPARG, XO). These are mapping leads, not favorable multi-target mechanisms; both are plant-origin flavonoids found in mushroom substrate, not fungal-biosynthesis attributions.
- Phase 2 partial: 3 of 6 planned compound DBs reachable (LOTUS, NPAtlas, KNApSAcK partial); NPASS / TCMSP / HIT all sandbox-blocked. ChEMBL primary-source pre-commit grep-verify gate applied on top-2 load-bearing potency claims.

**Informs:** [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) · [complement-c5a-gout](./complement-c5a-gout.md) · [tcm-gout-compound-triage-computational](./tcm-gout-compound-triage-computational.md) · [etc/open-source-platform](./etc/open-source-platform.md) · [nlrp3-exploit-map](./nlrp3-exploit-map.md) (Berkeleyamides → CASP1 effector axis) · [abcg2-modulators](./abcg2-modulators.md) (quercetin record requires polarity, substrate, and urate-context verification)

**Detail:** [interpretive](./medicinal-mushroom-compound-mapping-computational.md) · [Phase 3 target-mapping summary](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-3-target-mapping-summary.md) · [Phase 2 findings](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/PHASE-2-FINDINGS.md) · [experiments/](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/) · Phase 3 complete; Phase 2 partial (3 of 6 DBs); Phase 5 multilingual deep-dive + Phase 6 triage queued (SwissTargetPrediction layer is the load-bearing next step)

---

### comp-013 — TCM Gout Compound Triage — evidence inventory; viability ranking invalid

**Question:** Which TCM compounds with documented gout indications have source-backed target evidence worth advancing to context-matched exposure and functional testing?

**Verdict:** The curated lead inventory survives, but the biological viability ranking does not. Its `assign_verdict` logic counted off-target ABCG2 occupancy toward viability and did not preserve target-effect polarity. The inherited comp-004 nominal gut-concentration/IC50 component is also invalid as a direct biological decision metric.

**Key findings:**
- Compound/source/target records remain leads that can be re-read independently of the invalid score.
- Any renewed triage must preserve target-effect polarity, distinguish direct from off-target assays, and measure or justify free exposure in the relevant compartment.
- “Viable” and “non-viable” require context-matched functional evidence; nominal bulk concentration divided by an assay IC50 is insufficient.

**Informs:** [tcm-modern-rigor-intersection](./tcm-modern-rigor-intersection.md) — closes P2-2

**Detail:** [interpretive](./tcm-gout-compound-triage-computational.md) · [experiments/](./etc/experiments/comp-013-tcm-gout-compound-triage/) · Complete

---

### comp-012 — DAF/CD55 SCR1-4 Truncated Shio-Koji Protease Proxy (2026-05-05)

**Question:** What sequence-filter and AlphaFold-confidence prior does the inherited model provide for stalk-truncated DAF SCR1-4 (aa 35–285)?

**Verdict:** **Proxy verdict invalid; empirical risk unresolved.** The reported LOW score used pLDDT confidence as an accessibility class. COMP-001 cannot validate that mapping or serve as a protease-stability benchmark. The stalk-truncation hypothesis remains separately reviewable under comp-012 and requires direct retained-activity testing.

**Key findings:**
- Removing the lower-confidence stalk remains a testable construct-design hypothesis; the computation does not establish improved protease survival.
- Expression, correct disulfide folding, retained complement function, processing stability, and mucosal delivery remain empirical gates.

**Informs:** [complement-c5a-gout](./complement-c5a-gout.md) (CP0 evidence boundary) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) (stalk-truncation hypothesis) · [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) (portfolio status)

**Detail:** [interpretive](./daf-cd55-scr14-truncated-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-012-daf-cd55-scr14-truncated/) · Historical filter inventory only

---

### comp-011 — *C. utilis* Uricase Cassette Compatibility — INVALIDATED MODEL (2026-05-05)

**Question:** What exact processing, folding, and secretion failures should be tested when wild-type P78609 or a patent-mutation proxy is placed in a Ward-style *Aspergillus* cassette?

**Verdict:** **Invalidated and retired.** The model lacked a planned CDS, mixed wild type with a synthetic mutation proxy, mis-mapped glycosylation coordinates, and converted unverified processing and cysteine proxies into categorical risk. No MODERATE verdict or exact-ALLN-346 interpretation survives.

**Key findings:**
- UniProt P78609 identifies the wild-type sequence; the patent-disclosed mutation set does not establish the exact clinical ALLN-346 parent.
- Retain wild type and a precisely defined mutation proxy only when a matched construct comparison is decision-relevant.
- Produced termini, intact abundance, folding/assembly, compartment, and retained activity are the discriminating readouts.

**Informs:** [uricase-variant-selection](./uricase-variant-selection.md) · [validation-experiments §1.9](./validation-experiments.md)

**Detail:** [interpretive](./c-utilis-uricase-cassette-compatibility-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/)

---

### comp-010 — Cassette Compatibility for Dual-Cassette Koji Multi-Payload Configuration — INVALIDATED MODEL (2026-05-05)

**Question:** Does the uricase (Q00511) + lactoferrin (P02788) payload pair have cassette-design-specific issues (codon collisions, KEX2 geometry, secretion burden) that the Ward 1995 glucoamylase-KEX2 architecture won't handle?

**Verdict:** **Invalidated and retired.** The model inferred codon burden without an actual CDS, transferred KEX2-family specificity without an *A. oryzae* matrix, mis-mapped glycosylation coordinates, and converted bulk sequence proxies into a LOW secretion-burden verdict. No LOW, codon-collision, cleavage-certainty, host-capacity, or combined-cassette conclusion survives.

**Key findings:**
- Ward 1995 remains a production precedent, not validation of the proposed sequence–junction–host configuration.
- Internal sequence matches can nominate terminal mapping; they cannot predict cleavage or exclude a topology.
- Build single-cassette controls first and measure transcript, produced termini, compartment, abundance, and retained function before a combined configuration.

**Informs:** [validation-experiments §1.33 and §1.9](./validation-experiments.md) — exact-configuration measurement requirements; no topology selected

**Detail:** [interpretive](./cassette-compatibility-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-010-cassette-compatibility/)

---

### comp-007 — Food-Associated HDAC-Directed Candidate Screen — Invalidated

**Question:** Could heterogeneous HDAC and exposure evidence support a quantitative priority order for direct Q141K testing?

**Verdict:** **Invalidated and retired.** The model mixed assay types and analogical estimates, used arbitrary selectivity constants and `1 − oral bioavailability` as an exposure surrogate, and did not use its stored concentration estimates. No rank, score, shortlist, causal HDAC-isoform assignment, HDAC6-centered safety inference, or advancement decision survives.

**Key findings:**
- Seven compound names survive only as an unranked evidence inventory.
- Selected pharmacological HDAC inhibitors provide an in-vitro Q141K-rescue precedent, but direct butyrate rescue, epithelial exposure, ABCG2-attributed urate flux, causal isoform mapping, and safety remain unestablished.
- The possible combination of butyrate-associated endogenous ABCG2 induction and Q141K trafficking rescue is preserved as a Research Conjecture, not a COMP result.

**Informs:** [validation-experiments §1.22](./validation-experiments.md#122-gut-compartment-hdac-directed-candidate-screen-for-q141k-abcg2-trafficking-rescue) — direct, unranked candidate testing

**Detail:** [current evidence](./food-grade-hdaci-screen-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-007-food-grade-hdaci-screen/)

---

### comp-005 — Lactoferrin Shio-Koji Protease Proxy (2026-05-05)

**Question:** What sequence-filter and AlphaFold-confidence prior does the inherited protease proxy provide for human lactoferrin (P02788)?

**Verdict:** **Proxy only; empirical protease risk unresolved.** The reported HIGH/MODERATE labels used pLDDT confidence as an accessibility class and do not establish exposure, cleavage, degradation, or survival.

**Key findings:**
- The exact inter-lobe connector is not a lower-confidence segment in the retired input. COMP-005 supplies no fragment-region priority.
- Signal-peptide processing, glycosylation, context-specific protease activity, and retained function were not measured.
- Inter-lobe-linker redesign remains a separate hypothesis that activates only if untargeted WT fragment mapping identifies a reproducible linker-associated failure.

**Informs:** [validation-experiments §1.10](./validation-experiments.md) — both lactoferrin and UOX arms remain empirical feasibility gates

**Detail:** [current evidence](./lactoferrin-protease-stability-computational.md) · [invalidated, non-runnable tombstone](./etc/experiments/comp-005-lactoferrin-shio-koji-protease-stability/)

---

### comp-004 — Supplement–ABCG2 assay-evidence audit — quantitative verdict invalid

**Question:** Do three cited ABCG2/BCRP interaction records—one each for quercetin, curcumin, and EGCG—support a quantitative prediction of intestinal urate-transport inhibition?

**Verdict:** No. The nominal bulk-concentration/drug-substrate-IC50 ratios, predicted inhibition percentages, and clinical-risk labels are invalid. The three records support ABCG2/BCRP interaction signals in different systems; they do not quantify intestinal urate transport.

**Key findings:**
- Karibe supplies intestinal BCRP interaction evidence for curcumin with drug probes, not urate.
- Cooray and Farabegoli supply non-intestinal drug-substrate signals for quercetin and EGCG.
- The next gate is measured free parent/metabolites, ABCG2 protein and attribution, barrier integrity and viability, and basolateral-to-apical urate flux in an intestinal epithelial model.

**Informs:** [validation-experiments §1.14](./validation-experiments.md) — direct context-matched urate-flux assay

**Detail:** [interpretive](./supplement-abcg2-antagonism-computational.md) · [experiments/](./etc/experiments/comp-004-supplement-abcg2-antagonism/) · Complete

---

## Planned Analyses

| ID | Scope | Primary informs | Priority |
|---|---|---|---|
| ~~comp-002~~ | Invalidated, non-runnable thermal/pH composite model; source-backed thermal sensitivity and the multi-day attrition conjecture now route directly to §1.10 measurement | [§1.10 follow-up](./validation-experiments.md) | Retired |
| ~~comp-003~~ | Reassigned 2026-05-05 → comp-005 (lactoferrin cleavage-site analysis) | — | ✓ Done as comp-005 |
| ~~comp-008~~ | Invalidated, non-runnable hand-scored payload rubric. Stable transformation + reporter expression is the common genetic-entry gate; native-pathway, uricase, lactoferrin, and CR1 tests remain separate unranked configuration questions. | [engineered-lbp-chassis](./engineered-lbp-chassis.md) | Retired |
| ~~comp-009~~ | **Completed; RERUN 2026-07-14** on the real NM_144585.4 mRNA (original artificial-CDS run invalidated). 8 real-transcript target sites pass design filters; accessibility low (real RNAplfold) + off-target uncleared. See [interpretive page](./urat1-sirna-target-site-selection-computational.md). | [sirna-urat1-modality](./sirna-urat1-modality.md) Phase 2 P2-2 | ✓ Done (rerun) |
| ~~comp-011 TCM~~ | Reassigned 2026-05-05; TCM ChEMBL cross-check landed as comp-013 | — | ✓ Done as comp-013 |
| ~~comp-021~~ | Invalidated, non-runnable mixed-tier assay-format model. Matched-format replication planning survives only as a conjecture; no quantitative range, candidate rank, or operative gut potency survives. | [assay-format conjecture](./upstream-complement-assay-format-mapping-computational.md) | Retired |
| comp-022 | Corrective review open; enumeration survives, current shortlist non-authoritative | [open actions](../synthesis/queue/comp-review-022.md) | Open |
| ~~comp-024~~ | Invalidated, non-runnable hand-scored model. Complestatin tailoring and C1-INH expression/folding/function require separate configuration-level tests. See Analyses above | — | Retired |
| ~~comp-023~~ | Invalidated, non-runnable FBA. Jeennor's direct *A. oryzae* production evidence and one ER-orthogonality conjecture survive independently; burden, flux, yield, breakpoint, and feasibility results do not. | [cordycepin route](./cordycepin-cassette-burden-computational.md) | Retired |
| comp-022 v2 | Included in the same open corrective review | [open actions](../synthesis/queue/comp-review-022.md) | Open |
| ~~comp-023 v2~~ | Deprioritized 2026-05-16 — koji-cordycepin removed from active stack ([koji-endgame-strain §3.5](./koji-endgame-strain.md)) | — | Closed |
| ~~comp-025~~ | Deprioritized 2026-05-16 — koji-cordycepin removed; cultivation-route cordycepin inherits native ADA-inhibitor pairing | — | Closed |
| ~~comp-026~~ | Deprioritized 2026-05-16 — multi-cassette induction interference moot for cordycepin; re-openable for future cytosolic third-cassette candidate | — | Closed |
| ~~comp-027~~ | Completed 2026-05-16; **downgraded to hypothesis-generator 2026-07-14** — single strict-GREEN modeled point at 100 mg/d (not a validated 75–125 window). See Analyses above | — | ✓ Done |
| ~~comp-030~~ | Invalidated, non-runnable cassette-ranking model. Direct secretion and GlaA-KEX2 remain unranked configurations for a matched experiment. See Analyses above | — | Retired |
| ~~comp-029~~ | Invalidated, non-runnable toy scenario. The matched singleton/combination conjecture is grounded in independent single-arm evidence, not in the retired arithmetic. See Analyses above | — | Retired |
| ~~comp-031~~ | **Not decision-usable** — its flat-UOX, PDB-derived-butyrate, and compartment assumptions do not support the reported quantitative result or topology recommendation. See [dual-chassis page](./dual-chassis-ecn-pdb-uricase-computational.md), comp-044/046, and §1.34/§1.37. | — | ✓ Done |
| ~~comp-032~~ | Completed 2026-05-16 — ~~GREEN~~ **SUPERSEDED by comp-047 2026-07-14**; verdict retracted (tautological positive-control validation per comp-review 2026-07-13). See Analyses above | — | ✓ Done (superseded) |
| ~~comp-047~~ | **Completed 2026-07-14 — INCONCLUSIVE** (real Vina docking). CFTR-corrector positive controls fail to earn rank (0/4); rigid docking can't discriminate Q141K chaperones; chaperone-rescue ranking not computationally established. Supersedes comp-032. See Analyses above | [Q141K trafficking + urate-flux assay](./validation-experiments.md) | ✓ Done |
| ~~comp-033~~ | Completed 2026-05-16 — RED single-dose Cmax-equivalent; reframed in comp-036 (YELLOW receptor-occupancy). See Analyses above | — | ✓ Done |
| ~~comp-036~~ | Completed 2026-05-16 — YELLOW repeat-dose receptor-occupancy framing; salvages comp-033 RED. See Analyses above | — | ✓ Done |
| ~~comp-037~~ | Invalidated, non-runnable proxy — exact-configuration folding, stability, kinetics, glycosylation effects, and function remain open. See Analyses above | — | Retired |
| ~~comp-038~~ | Completed 2026-05-20 — YELLOW; HPLC-UV culture-supernatant candidate + electrochemical fecal SCFA future direction; no home/colorimetric butyrate assay ready. See Analyses above | — | ✓ Done |
| ~~comp-039~~ | Completed 2026-05-21 — All four upstream-CP0 candidates classified CFH-INDEPENDENT (rosmarinic acid High, luteolin Medium, HCP/HCPM/CHCP High, Helicteres Medium-replication-bounded). See Analyses above | — | ✓ Done |
| comp-040 | Wet-lab in-vitro CFH-replete/depleted-serum MSU-crystal complement-activation assay — direct falsification test of the comp-039 CFH-independence classification for rosmarinic acid, luteolin, and qualified HCP materials. The HCP complement arm is independent of [validation §1.30](./validation-experiments.md), which tests direct macrophage directionality; either may run when its exact material and assay capability are available, and failure in one does not adjudicate the other. | [comp-039](./cfh-mechanism-dissociation-cp0-candidates-computational.md), [Houttuynia](./houttuynia-cordata.md), [validation §1.30](./validation-experiments.md), [gout-genetic-variants.md](./gout-genetic-variants.md) Category 5, [complement-c5a-gout.md](./complement-c5a-gout.md) §6.3 | Blocked (OE wet-lab access and exact-material sourcing; relevant to lab-partner conversations) |
| comp-041 | East Asian cohort feasibility scan for Houttuynia × rs1061170 × incident gout cross-tab — KoGES, China Kadoorie Biobank, Singapore Chinese Health Study. Parallels the 2026-05-19 UKB feasibility analysis but for the Houttuynia-tractable population (HCP exposure captured; Y402H allele frequency ~5-6%). Defined by [comp-039](./cfh-mechanism-dissociation-cp0-candidates-computational.md) §5 + §7. | [comp-039](./cfh-mechanism-dissociation-cp0-candidates-computational.md), [logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md](../logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md) | Queueable (opens when East Asian collaboration channel becomes available) |
| ~~comp-028~~ | Deprioritized 2026-05-16 — cordycepin-arm moot; general design-escape question non-load-bearing today; re-openable for future cytosolic third-cassette candidate | — | Closed |

---

## Infrastructure proposals

### comp-NNN verification agent (ClockBase hypothesis-then-verify pattern) — Planned (2026-05-08)

Every comp-NNN run produces output from a *generation* agent; add a second-pass *verification* agent (different vendor preferred per the multi-vendor heterogeneity discipline) that re-checks every load-bearing number (disulfide counts, residue indices, IC50/Ki, accession numbers, cohort sizes) against primary databases (UniProt, ChEMBL, PDB, PubMed) before commit. Sister discipline to the per-page Pre-commit verification gate (CLAUDE.md Rule 4) — same pattern at a different scope. Would have caught the 2026-05-06 DAF SCR1-4 disulfide hallucination at generation time. Cost ~$3–5 + 10–30 min per comp.

**Detail:** [etc/autonomous-screening-methodology](./etc/autonomous-screening-methodology.md) §"Hypothesis-then-verify pattern" · [etc/manual-literature-mining](./etc/manual-literature-mining.md) §"Pre-commit verification gate" · [operations/comp-018-vs-comp-020-retrospective](../operations/comp-018-vs-comp-020-retrospective.md)

---

### pcSec-class proteome-constrained *A. oryzae* GEM build — Planned (2026-05-14)

Layer secretion-pathway proteome-cost constraints on iWV1314 (Vongsangnak 2008): explicit PDI/calnexin/BiP saturation, signal-peptide processing capacity, KEX2 flux, and Sec61 throughput. This could evaluate a future *secreted-protein* cassette such as DAF SCR1-4 or an engineered C1-INH configuration. Complestatin NRPS biosynthesis is not a secreted-protein cassette and does not belong in this model. Any future *cns1+cns2* analysis needs verified pathway boundaries and calibration against exact product and cell-state measurements; it must not reproduce COMP-023's retired scenario. Multi-week research project; not a single-subagent task.

**Detail:** [chaperone-orthogonal-stacking](./chaperone-orthogonal-stacking.md) · companion to verification-agent proposal (per-run vs per-strain infrastructure scopes)

---

## How to add a new analysis

1. Create `etc/experiments/comp-NNN-<slug>/` with `analyze.py`, `inputs/`, `outputs/`, `README.md`, `inputs/provenance.md`
2. Add an entry to the "Analyses" section above (compact format) or the "Planned Analyses" table
3. Create `wiki/<slug>-computational.md` for the interpretive page
4. Link from the relevant wet-lab experiment in `validation-experiments.md`
5. Commit script + inputs + outputs together (outputs are version-controlled; they are the peer-reviewable artifact)
