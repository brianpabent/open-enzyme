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

### comp-043 — Does EcN periplasmic disulfide-folding scale from C1-INH (2) to DAF SCR1-4 (8) and lactoferrin (16)? — C1-INH VIABLE / DAF PROVISIONAL / lactoferrin NOT-VIABLE (2026-07-13)

**Question:** [comp-037](./c1-inh-protease-stability-ecn-computational.md) showed EcN's periplasmic DsbA/DsbC machinery can plausibly fold C1-INH (2 disulfides). A synthesis card overreached: "so EcN is superior to koji for PDI-heavy payloads like DAF SCR1-4 (8) and lactoferrin (16)." Does EcN's periplasmic disulfide-folding + colonic-protease survival actually *scale* with disulfide count, and where does the crossover sit? Explicitly **not** a genome-scale metabolic model (a GEM models flux, not folding-machinery competition — the card's category error) — a [comp-006](./daf-cd55-protease-stability-computational.md)/[comp-037](./c1-inh-protease-stability-ecn-computational.md)-style structural + sequence folding-feasibility analysis.

**Verdict:** **Relative ranking, crossover AT DAF SCR1-4 — not a false-precision GREEN.** C1-INH (2 disulfides) **VIABLE** (disulfide axis; comp-037 kinetic caveat still governs). DAF SCR1-4 (8) **PROVISIONAL** — folding-capacity-gated. Lactoferrin (16) **NOT-VIABLE** — folding-limited across the entire plausible capacity band. **Card claim REFUTED as stated.** Bounded thesis: EcN plausibly extends to low/moderate-disulfide, compact-fold, glyco-independent payloads (C1-INH, DAF SCR1-4-provisional); it does not scale to lactoferrin; and koji is *not* dominated (folds DAF at LOW protease risk per comp-012, >2 g/L lactoferrin in *A. awamori* per Ward 1995).

**Key findings:**
- Three orthogonal axes, limiting-factor (Liebig) composite where **folding is the gate**: (1) architecture-weighted disulfide-folding demand vs. a precedent-derived DsbA/DsbC capacity band; (2) strictly-degradative colonic-protease exposure (pLDDT scan); (3) glycosylation-dependence for function.
- Effective folding demand (loop-length + interleaved-crossing weighted): C1-INH **4.0**, DAF SCR1-4 **10.0**, lactoferrin **23.5** vs. capacity band conservative 5 / moderate 8 / optimistic 12. Folding-nonviability: C1-INH plausible across the band; DAF straddles it; lactoferrin limited even at optimistic capacity (3 C-lobe-spanning long-range bonds = transferrin hierarchical-folding signature).
- Disulfide counts grep-verified against UniProt: C1-INH P05155 = 2, DAF P08174 = 8 (all in SCR1-4), lactoferrin P02788 = 16. Every Cys position asserted in `analyze.py`.
- **Single biggest unresolved question:** no published DsbA/DsbC capacity metric at 8-16 disulfide scale (chaperone-orthogonal-stacking.md §8 item 6) — the capacity band is an *inference, not a measurement*, hence DAF's PROVISIONAL label. The optimistic (SHuffle) anchor is cytoplasmic disulfide formation, compartment-mismatched with the secreted luminal format, biasing the honest read conservative for DAF.
- **Glycosylation does NOT independently kill DAF or lactoferrin function** (DAF decay-acceleration is protein-protein; lactoferrin iron-binding tolerates non-native glycans, Sun 1999) — the dominant filter is Axis 1 (folding), not glycosylation. Over-attributing the lactoferrin problem to glycosylation would be a mechanism error.
- Peer-review-incorporated: interleaved sushi topology folded into DAF's demand; C1-INH softened to "disulfide-axis viable" (serpin metastability = unmodeled fold-attainment risk); compartment-mismatch of the SHuffle anchor flagged.

**Informs:** [engineered-lbp-chassis.md](./engineered-lbp-chassis.md) (chassis assignment: lactoferrin stays on koji, DAF EcN provisional-secondary) · [chaperone-orthogonal-stacking.md](./chaperone-orthogonal-stacking.md) §8 (EcN-side capacity-metric gap, analogue of the koji α-coefficient gap) · [complement-c5a-gout.md](./complement-c5a-gout.md) (two-chassis CP0 architecture stands, chassis assignment does not invert) · [validation-experiments.md](./validation-experiments.md)

**Detail:** [interpretive](./daf-lactoferrin-ecn-folding-feasibility-computational.md) · [experiments/](./etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/) · Complete first pass (next gate: DsbA/DsbC folding-capacity measurement at 8-16 disulfide scale)

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

**Question:** For each top upstream-CP0 candidate from comp-018 / comp-020 — rosmarinic acid, luteolin, *Houttuynia cordata* polysaccharide (HCP / HCPM / CHCP), *Helicteres* benzofuran lignans — does the candidate's anti-complement mechanism *require* functional CFH (and therefore lose efficacy in Y402H carriers, AMD-paradox-style), or does it work *upstream of* CFH (so Y402H carriers retain the benefit)? Generates the per-candidate prediction the UKB collaboration (Merriman/Otago, Major-Wrigley/Auckland, Choi/MGH) needs to run candidate-stratified cross-tabs rather than a generic "any-polyphenol × CFH" query.

**Verdict:** **All four candidates classified CFH-INDEPENDENT.** Rosmarinic acid (High confidence) — Sahu 1999 binds nascent C3b α'-chain thioester (Cys988) upstream of where CFH acts. Luteolin (Medium confidence) — broad CP+AP inhibition with mechanism site under-resolved; matched CP/AP IC50 inconsistent with CFH-competitive mechanism. HCP / HCPM / CHCP (High confidence) — Lu 2018 + Tian 2014 depletion-rescue maps targets to C3 + C4 + partial C5; C4 specificity is mechanistically incompatible with CFH-dependence (CFH is AP-specific). Helicteres benzofuran lignans (Medium confidence, bounded by comp-018 Phase 2 INCONCLUSIVE replication of Yin 2016) — multi-target on C1q + C2 + C3 + C4 + C9, structurally orthogonal to CFH's CCP6-8 binding surface.

**Key findings:**
- Two-model independent cross-check (Claude Opus 4.7 = Model A; DeepSeek `deepseek/deepseek-chat-v3` = Model B): both models AGREE on classification for all four candidates.
- Two-model DISAGREEMENT on predicted Y402H × candidate × incident-gout direction: Model A predicts negative direction (effect ≥ in carriers, because Y402H baseline severity amplifies absolute effect size); Model B predicts null (mechanism independence implies genotype indifference). Both reject the AMD-paradox direction (carriers worse). For UKB cross-tab, both predictions need separate falsification thresholds.
- CFH Y402 structural footprint grep-verified: Sushi/CCP 7 = aa 387-444 of UniProt P08603. The four candidates' binding sites all map to upstream complement nodes (C3 thioester, C3 itself, classical-pathway C2 + C4 + C1q), not the CCP6-8 CRP/GAG-binding surface.
- Recommended lead UKB cross-tab: rs1061170 × Phenol-Explorer-derived rosmarinic-acid intake × incident gout M10.x. Secondary: rs1061170 × Apiaceae-family intake × incident gout (luteolin proxy + 24h-urate intermediate readout). HCP cross-tab deferred to East Asian cohorts (KoGES / CKB / Singapore Chinese Health Study). Helicteres not actionable until comp-018 Phase 2 replication closes.
- Total OpenRouter spend: ~$0.0022 (Model B counter-reads × 4 candidates).
- Follow-ups: comp-040 (proposed) — wet-lab CFH-depleted-serum MSU-crystal assay as definitive falsification test; comp-041 (proposed) — East Asian cohort feasibility scan for Houttuynia × CFH cross-tab.

**Informs:** [gout-genetic-variants.md](./gout-genetic-variants.md) Category 5 CFH row · [complement-c5a-gout.md](./complement-c5a-gout.md) §6.3 · [upstream-complement-modulator-sweep-computational.md](./upstream-complement-modulator-sweep-computational.md) · [upstream-complement-verification-rerun-computational.md](./upstream-complement-verification-rerun-computational.md) · [logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md](../logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md)

**Detail:** [interpretive](./cfh-mechanism-dissociation-cp0-candidates-computational.md) · operations workspace: [`operations/cfh-mechanism-dissociation-2026-05-21/`](../operations/cfh-mechanism-dissociation-2026-05-21/) · Complete first pass (next gate: UKB collaboration ask + comp-040 wet-lab depletion assay)

---

### comp-038 — Tier 2 Butyrate Assay Audit — YELLOW (2026-05-20)

**Question:** Is there a Tier 2 butyrate quantification assay (colorimetric, enzymatic, breath-proxy, electrochemical, or other low-cost intermediate method) that can be validated against Tier 3 GC-MS for stool, serum, breath, or culture-supernatant matrices?

**Verdict:** **YELLOW.** No ready-to-adopt simple/home colorimetric or breath-based butyrate assay was identified. Two plausible Tier 2 candidates identified: HPLC-UV SCFA + lactate assay for culture-supernatant / engineered-strain work, and electrochemical fecal SCFA profiling with ANN deconvolution as an emerging stool-specific direction. Both require full-text/protocol review and paired GC-MS validation before OE adoption.

**Key findings:**
- PubMed snapshot: 27 queries / 74 records; source snapshot committed at `outputs/pubmed-snapshot.json`.
- HPLC-UV for bacterial culture supernatants is the best near-term Tier 2-lab candidate (De Baere 2013, PMID 23542733) — **full-text-verified against the primary source 2026-07-14** (0.5–50 mM, r 0.9951–0.9993, underivatized UV 210 nm, bacterial-culture-supernatant matrix). The remaining gate is OE spike/recovery + paired GC-MS (validation §1.31).
- Electrochemical fecal SCFA profiling is the most promising stool-specific future Tier 2 direction (PMID 42041444), but remains research-platform grade.
- Breath H2/CH4 is useful as a broad fermentation/adherence proxy, not butyrate-specific quantification.
- Generic free-fatty-acid colorimetric kits are a false-friend class; representative protocol excludes acetic, propionic, and butyric acid.
- Completed with Codex/GPT-5.5 in-session synthesis from a committed source packet; no OpenRouter model calls were made.

**Informs:** [quantification-ladder](./quantification-ladder.md) · [genotype-informed-supplement-workflow](./genotype-informed-supplement-workflow.md) · [validation-experiments §1.14](./validation-experiments.md#114-abcg2-response-to-dht-and-tnf-with-butyrate-and-lactoferrin-rescue) · [purine-degrading-bacteria](./purine-degrading-bacteria.md)

**Detail:** [interpretive](./tier-2-butyrate-assay-audit-computational.md) · [experiments/](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/) · Complete first pass (next gate: full-text/protocol verification + small paired Tier 2 vs GC-MS validation)

---

### comp-037 — C1-INH (SERPING1) Protease Stability + Glycosylation Feasibility in EcN-Luminal Format — MODERATE (kinetic-competition gated) (2026-05-17)

**Question:** Will human C1-INH (UniProt P05155) survive luminal-secreted expression in engineered *E. coli* Nissle 1917, and is the loss of N-glycosylation a hard block? Closes the C1-INH-on-EcN side of the two-chassis CP0 architecture (C1-INH on LBP-luminal + DAF SCR1-4 on koji-secreted).

**Verdict:** **MODERATE — kinetic-competition gated.** Strictly-degradative protease risk on the folded serpin body is **LOW (0.1)**. The by-design exposed reactive-center loop (RCL, R466-T467 cleavage by C1s) gives a 0.8 score that reflects the inhibitor *mechanism*, not body degradation. The remaining decision is a wet-lab kinetic question: k_C1s_engagement vs k_DegP_RCL_cleavage on the recombinant construct. **Glycosylation feasibility GREEN** for the serpin-core construct (aa 123–500) in luminal topology — N-glycans not required for catalytic suicide-substrate mechanism; plasma half-life concern is moot for a gut-luminal therapeutic; EcN's lack of N-glycosylation is not a hard block.

**Key findings:**
- **Disulfide count grep-verified against UniProt FT DISULFID: exactly 2 disulfides** (C123-C428, C130-C205) on SV=2 entry. Casual literature sometimes quotes higher counts; the canonical entry has 2. This is the same class of check the DAF SCR1-4 incident (CLAUDE.md Rule 4) exists to enforce.
- **Engineering recommendation: serpin-core construct aa 123–500.** Truncation starts at C123 (first canonical disulfide cysteine; pLDDT > 80 from this position onward); eliminates two boundary-artifact elastase sites (G120-S121, S121-F122).
- **Brief-supplied glycosylation positions did not all align with UniProt features.** Subagent corrected to verified positions: N-glycans at 25, 69, 81, 238, 253, 272-variant, 352 + O-glycans at 47, 48, 64, 71, 83, 88, 92, 96 (mucin-like domain). The mucin-like O-glycan domain (residues ~1–122) is what gets truncated — its function (serum half-life extension via O-glycan shield) is irrelevant for luminal topology.
- Protease panel: DegP P1 V/I/L/F/Y/A (Krojer 2008), OmpT di-basic (Dekker 2001), pancreatic trypsin/chymotrypsin/elastase. Colonic pH 6–7 (Fallingborg 1999) is within DegP active range — load-bearing assumption.
- Glycosylation cross-reference: Bos 1998 (PMID 9799502) + Stavenhagen 2018 (PMID 29381136) — ~26 kDa of glycan on ~52 kDa polypeptide; Liu 2004 (PMID 15039314) — N-deglycosylated C1-INH retains inhibitor function (this is the load-bearing precedent for the GREEN glyco verdict).
- Substantiates comp-024's GREEN-provisional 0.774 EcN prior for C1-INH at higher resolution.

**Informs:** [complement-c5a-gout §9.8](./complement-c5a-gout.md) · [complestatin-bgc-lbp-feasibility-computational](./complestatin-bgc-lbp-feasibility-computational.md) (comp-024 anchor) · [engineered-lbp-chassis](./engineered-lbp-chassis.md) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) (sister-thread DAF SCR1-4 on koji) · [upstream-complement-modulator-sweep-computational](./upstream-complement-modulator-sweep-computational.md) Phase 2 (engineering-literature anchors Bos 2003, Liu 2004, Ruconest 2014)

**Detail:** [interpretive](./c1-inh-protease-stability-ecn-computational.md) · [experiments/](./etc/experiments/comp-037-c1-inh-protease-stability-ecn/) · Complete v1 (wet-lab kinetic-competition assay is the next gate; engineering construct = serpin-core aa 123–500)

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

### comp-024 — Complestatin-Family BGC LBP-Chassis Feasibility — RED for LBP framing; C1-INH parallel GREEN-provisional (2026-05-16)

**Question:** Is the complestatin-family NRPS biosynthetic gene cluster heterologous-expression-tractable in an engineered LBP chassis (*E. coli* Nissle 1917, *Bacteroides thetaiotaomicron*) as the next CP0 (complement priming) engineering payload?

**Verdict:** **RED for the LBP-track framing.** Best host EcN YELLOW 0.544; *Bacteroides* RED 0.225. Dominant blocker: O₂-dependent tailoring chemistry (ComI/ComJ P450 oxidative phenolic coupling + ComH nonheme halogenase + Hmo FMN oxidase) fundamentally incompatible with colonic-anaerobic-resident lifestyle. Without P450-mediated phenolic coupling, the linear peptide lacks the rigid crosslinked architecture that gives complestatin its C1q/C4b affinity (Park 2016 M55/S56 deletions inactive). **C1-INH (LBP-luminal) parallel thread scores GREEN-provisional 0.774 on EcN** — recommended as next CP0 LBP payload instead (→ tracked as comp-037).

**Key findings:**
- Complestatin stays in scope as **aerobic-fermentation production candidate** (Streptomyces-class manufacturing), NOT LBP-track payload.
- Bacterial NRPS BGC + O₂-dependent tailoring + anaerobic chassis is a load-bearing incompatibility worth surfacing as a general design rule.
- Comp-024's recommendation (promote C1-INH to real comp-NNN) is the origin of comp-037.

**Informs:** [complement-c5a-gout §9.8](./complement-c5a-gout.md) · [engineered-lbp-chassis](./engineered-lbp-chassis.md) · [modality-chokepoint-matrix](./modality-chokepoint-matrix.md)

**Detail:** [interpretive](./complestatin-bgc-lbp-feasibility-computational.md) · [experiments/](./etc/experiments/comp-024-complestatin-bgc-lbp-feasibility/) · Complete v1

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

### comp-022 — ClockBase Combinatorial Ranking of A. oryzae Uricase Cassettes — candidate generator (2026-05-14; topology unresolved as of 2026-07-13)

**Question:** Across the *A. oryzae* uricase cassette design space (43,200 combinations), which cassettes survive a multi-model concordance gate?

**Current verdict:** **Useful candidate ranking; topology not selected.** The direct-secretion top cluster and its gene-synthesis refinements survive within comp-022's search space, but comp-044/045 showed that §1.33 must determine whether secretion is physiologically credible before promotion to §1.9B.

**Key findings:**
- Zero-cost gene-synthesis refinements that survive v2 concordance: 5'-softened codon optimization; N191Q glycosylation ablation. PTS1-blocking C-terminal tag remains biologically motivated (addresses comp-010 routing risk) but is **not** a v2-strict-tier requirement—non-PTS1-blocked scaffolds also reach N-of-5 = 5 (see comp-022 `v2/provenance.md`).
- The v2 strict N-of-5 = 5 tier is a distinct 4-cassette set spanning PamyB + PglaA promoters, **not** identical to the v1 top cluster (only 1 of the 4 is a v1-top-cluster member). The v1 top cluster does survive the looser N-of-5 ≥ 4 gate (4 of 4).
- Within the tested koji-secreted cassette space, glucoamylase-KEX2 fusion ranks below direct secretion. This does not compare koji secretion with intracellular, displayed, or bacterial topologies in §1.33.
- v1 GC-clamp proxy vs real ViennaRNA MFE Spearman ρ = 0.241; v2 materially shifted ranks while preserving the internal direct-secretion cluster.

**Informs:** [validation-experiments §1.33 (topology gate) + conditional §1.9B](./validation-experiments.md) · [cassette-compatibility-computational](./cassette-compatibility-computational.md) · [koji-endgame-strain §3.4](./koji-endgame-strain.md) · [etc/autonomous-screening-methodology](./etc/autonomous-screening-methodology.md)

**Detail:** [interpretive](./uricase-cassette-ranking-computational.md) · [experiments/](./etc/experiments/comp-022-clockbase-uricase-cassette-ranking/) · v2 complete (v2.5 deferred until §1.33/§1.9B wet-lab data lands)

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

### comp-018 — Upstream Complement Modulator Sweep — Phase 1 + Phase 2 complete (2026-05-17)

**Question:** Across all compound classes, which compounds have documented activity at upstream complement cascade nodes proximal to C5a generation, and which are gout-platform-relevant?

**Verdict:** **Direct natural-product C5aR1 antagonists empty (re-confirms comp-014 + §1.21).** Moving one node upstream uncovers substantial literature anchored by **rosmarinic acid** (TIER 1; C3 convertase IC50 5–10 µM, three in vivo precedents, FDA-GRAS sources). TIER 2: luteolin (triple-mechanism with comp-013 XO + URAT1), tiliroside, Bupleurum polysaccharides, falcarindiol, ganoderic acid Sz, quercetin, K-76, complestatin.

**Key findings:**
- "Chokepoint-hacker move" worked; rosmarinic acid is the most well-characterized natural-product upstream-complement modulator.
- **Luteolin triple-convergence** (XO + URAT1 + C3 convertase CP+AP) — highest-leverage single dietary compound identified.
- comp-014 β-glucan structure-dependence mechanistically explained; Ganoderma triterpene-enriched preps argued for.
- Engineered C1-INH parallel thread proposed (near-twin to H05 DAF) → grounded in Phase 2 + tracked as comp-037.
- ChEMBL anticomplement coverage 0/32 = 0% — same gap pattern as comp-013/014.
- **Phase 2 (2026-05-17):** new TIER 1 candidate **Houttuynia cordata polysaccharide class** (CH50 79–318 µg/mL, multi-anchor Chen Daofeng Fudan group, widely dietary in SE Asia) — orthogonal to RA/luteolin/Helicteres on mechanism + structure class. Helicteres benzofuran lignan replication INCONCLUSIVE (single-anchor Yin 2016; structural neighbor Styrax egonol 3.7× weaker). C1-INH engineering anchors: Bos 2003 Pichia 30–180 mg/L active rhC1-INH, Liu 2004 N-deglycosylated retains inhibitor function, Ruconest 2014 FDA non-mammalian-glycosylation precedent.
- **Phase 2 reframing — "language barrier" was the wrong diagnosis.** Chen Daofeng / Yamada-Kiyohara groups publish 80–95% in English-language journals; actual barriers are citation-network insularity + traditional-formula-name vs Western-mechanism-name query framing + source-journal impact-factor underweighting. Operational discipline: query by traditional-formula + species + traditional-pathology framings IN ADDITION to mechanism names. "C3 convertase inhibitor" misses Houttuynia; "Houttuynia cordata anti-complementary" catches it.

**Informs:** [complement-c5a-gout](./complement-c5a-gout.md) · [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) · [tcm-gout-compound-triage-computational](./tcm-gout-compound-triage-computational.md) · [medicinal-mushroom-compound-mapping-computational](./medicinal-mushroom-compound-mapping-computational.md) · [hypotheses/H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) · [gout-action-guide](./gout-action-guide.md) · comp-037 (C1-INH protease-stability, concurrent)

**Detail:** [interpretive](./upstream-complement-modulator-sweep-computational.md) · [experiments/](./etc/experiments/comp-018-upstream-complement-modulator-sweep/) · [phase-2/](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/) · **Phase 1 + Phase 2 complete; v2 DeepSeek translation cross-check pending on 4 Chinese-language + 1 Japanese flagged sources.** Brief contained user-framing bias on Phase 1; verification re-run is comp-020. See [retrospective](../operations/comp-018-vs-comp-020-retrospective.md).

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

### comp-001 — Uricase Shio-Koji Protease-Site Proxy (2026-05-05)

**Question:** What prior do P1/P1' sequence rules and AlphaFold per-residue confidence provide for *A. flavus* UOX (Q00511) before a shio-koji proteolysis assay?

**Verdict:** **Proxy only; empirical risk unresolved.** The analysis mapped predicted cleavage positions and their pLDDT values. pLDDT is model confidence, not solvent accessibility or protease resistance.

**Key findings:**
- The predicted cleavage positions occur at residues with high AlphaFold confidence; no solvent-accessibility or SASA calculation was performed.
- The analysis did not measure cleavage, retained activity, salt-conditioned protease behavior in the ferment, or any fermentation outcome.

**Informs:** [validation-experiments §1.10](./validation-experiments.md) — supplies a sequence/structure proxy while the empirical retained-activity assay remains the decision gate.

**Detail:** [interpretive](./uricase-protease-stability-computational.md) · [experiments/](./etc/experiments/comp-001-uricase-shio-koji-protease-stability/) · Complete

---

### comp-006 — DAF/CD55 Shio-Koji Protease Stability (full ectodomain) — HIGH (2026-05-05)

**Question:** Would the DAF/CD55 soluble ectodomain (aa 35–353: SCR1–4 + Ser/Thr stalk) survive shio-koji protease conditions?

**Verdict:** **HIGH / HIGH / HIGH** across full / mature / soluble-ectodomain scopes. Driver: Ser/Thr-rich stalk (aa 286–353, pLDDT 30–52, disordered). SCR1–4 (aa 35–285, pLDDT 85–98) contribute **zero low-pLDDT exposed-by-proxy sites** (pLDDT-based proxy, not a SASA result). Note the ectodomain HIGH is a **conservative stress-test dependent on NPr pH factor = 1.0**; at realistic NPr activity (~0.3–0.5) it shifts toward MODERATE/LOW, leaving the disordered stalk as the liability (corrected 2026-07-14).

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

**Verdict:** **PHASE 3 COMPLETE.** 9,778 unified fungal compounds (LOTUS 6,798 + NPAtlas 4,535 + KNApSAcK 20 InChIKey-resolved; NPASS / TCMSP / HIT unreachable from sandbox — documented gap). 24 chokepoint targets queried via ChEMBL; **323 (compound × chokepoint) empirical hits across 12 chokepoints**; 177 / 9,778 compounds (1.81%) have ≥1 hit. Highest-potency: **Ganoderic acid H × TNFα Kd = 2.45 nM** (pChEMBL 8.61, CHEMBL1922178, *Ganoderma lucidum*); **Berkeleyamides A/D × CASP1 IC50 = 330 / 610 nM** (*Penicillium*); **Quercetin × ABCG2 EC50 = 30 nM** (*Agaricus*); **Ellagic acid × OAT1 IC50 = 270 nM** (*Penicillium* / *Phellinus*).

**Key findings:**
- *Ganoderma* triterpenoid scaffold (ganoderic acids H/D and stereoisomers) emerges as highest-potency direct-binding hit at TNFα, **on top of** the Phase 2 *G. applanatum* 2,4-DAE urate-axis finding — two distinct chokepoint axes, both worth pursuing. *Ganoderma* spp. earn closer look.
- **Berkeleyamides / Berkeleyones** (Penicillium): first fungal natural products with direct sub-µM CASP1 and low-µM IL-1β hits — opens an inflammasome-effector-axis fungal candidate beyond the polysaccharide-priming literature comp-014 Phase 1 + Phase 2 emphasized.
- **Target-orphan rate 98.19%** — SwissTargetPrediction predicted-target layer is the next load-bearing step; sandbox-blocked here, deferred to re-run. 9,601 compounds with zero empirical chokepoint hits.
- **12 of 24 chokepoints have ZERO fungal-source ChEMBL hits**: NLRP3, ASC, GLUT9, C5aR1, Lp-PLA2, KEAP1, OAT4, PINK1, PDI, PDIA3, TXN, TXNIP. Confirms the comp-013 / comp-020 ChEMBL-Western-pharma-bias finding empirically for fungal-source NPs.
- Multi-chokepoint compounds identified: morin (4 chokepoints: ABCG2, CASP1, URAT1, XO); genistein (4: ABCG2, CASP1, PPARG, XO). Both plant-origin flavonoids in mushroom substrate — not biosynthesis attribution.
- Phase 2 partial: 3 of 6 planned compound DBs reachable (LOTUS, NPAtlas, KNApSAcK partial); NPASS / TCMSP / HIT all sandbox-blocked. ChEMBL primary-source pre-commit grep-verify gate applied on top-2 load-bearing potency claims.

**Informs:** [modality-chokepoint-matrix](./modality-chokepoint-matrix.md) · [complement-c5a-gout](./complement-c5a-gout.md) · [tcm-gout-compound-triage-computational](./tcm-gout-compound-triage-computational.md) · [etc/open-source-platform](./etc/open-source-platform.md) · [nlrp3-exploit-map](./nlrp3-exploit-map.md) (Berkeleyamides → CASP1 effector axis) · [abcg2-modulators](./abcg2-modulators.md) (Quercetin × ABCG2 30 nM)

**Detail:** [interpretive](./medicinal-mushroom-compound-mapping-computational.md) · [Phase 3 target-mapping summary](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-3-target-mapping-summary.md) · [Phase 2 findings](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/PHASE-2-FINDINGS.md) · [experiments/](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/) · Phase 3 complete; Phase 2 partial (3 of 6 DBs); Phase 5 multilingual deep-dive + Phase 6 triage queued (SwissTargetPrediction layer is the load-bearing next step)

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
- Current platform decision: retain both variants as candidates. Build and characterize the relevant koji configurations first, then use §1.33 to compare them under controlled reaction-site conditions. Within-host results may advance a configuration and nominate its topology; they do not establish a cross-host winner. Compare both payload variants within the advanced configuration only when the marginal cost remains bounded. The original direct-secretion/$0-fermentation recommendation is superseded.
- Three MODERATE drivers: codon burden 2.3× heavier (CAI 0.65 vs 1.51); 4 free cysteines vs 0; 2 internal KR sites vs 1. ALLN-346 mutation I132R adjacent to position 130 KR.
- Corrects prior P15296 misattribution; canonical UniProt is **P78609**.

**Informs:** [uricase-variant-selection](./uricase-variant-selection.md) · [validation-experiments §1.9](./validation-experiments.md)

**Detail:** [interpretive](./c-utilis-uricase-cassette-compatibility-computational.md) · [experiments/](./etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/) · Complete

---

### comp-010 — Cassette Compatibility for Dual-Cassette Koji Multi-Payload Configuration — LOW (2026-05-05)

**Question:** Does the uricase (Q00511) + lactoferrin (P02788) payload pair have cassette-design-specific issues (codon collisions, KEX2 geometry, secretion burden) that the Ward 1995 glucoamylase-KEX2 architecture won't handle?

**Verdict:** **LOW** overall cassette-design risk for the asymmetric architecture (direct-secretion uricase + glucoamylase-KEX2-fusion Lf). Uricase: 0 disulfides; Lf: 16 disulfides, equal by bulk count to the 16-disulfide Huynh 2020 reference (Notari 2023 count correction propagated 2026-07-13). Fold-specific burden remains empirical; no blocking sequence-level issues.

**Key findings:**
- OE pair equals Huynh 2020 only by bulk disulfide count; protein-architecture-specific ER capacity remains unresolved. Ward 1995 is the protein-specific Lf precedent, while §1.9A is the current-host empirical gate.
- Monitor Lf KEX2 site at mature pos 579 (moderate truncation risk) by SDS-PAGE; verify uricase secretion vs C-terminal SKL PTS1 motif.
- Uricase pos 128 high-risk KR is irrelevant within the direct-secretion candidate but becomes load-bearing for any fusion configuration supplied to §1.33.

**Informs:** [validation-experiments §1.33 and §1.9](./validation-experiments.md) — removes specific sequence-level blockers from one candidate architecture; does not select topology

**Detail:** [interpretive](./cassette-compatibility-computational.md) · [experiments/](./etc/experiments/comp-010-cassette-compatibility/) · Complete

---

### comp-007 — Food-Grade HDAC Inhibitor Candidate Screen — Butyrate ranks first on proxy score (2026-05-05)

**Question:** Which food-grade HDAC inhibitor candidates best combine class I potency, HDAC6 selectivity, and gut-enriched exposure for direct Q141K testing?

**Verdict:** **Butyrate (rank 1, 0.374) >> Sulforaphane (rank 2, 0.090) > PEITC (rank 3, 0.060)** on the artifact's candidate score. This ranks direct-test candidates; it does not demonstrate Q141K trafficking or urate-flux rescue.

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
| ~~comp-008~~ | **Completed 2026-05-16; review actions remain open.** Expert-prior *F. prausnitzii* construct-tractability triage. Native BCoAT overexpression has the highest point estimate, but ranges overlap and increased butyrate is untested; uricase is poorly matched to anaerobic Fp. The complement candidate is not decision-ready because the artifact conflates CR1/P17927 with the DAF/CD55 comp-012 precedent. See [interpretive page](./f-prausnitzii-heterologous-expression-computational.md) and current COMP receipt. | [engineered-lbp-chassis](./engineered-lbp-chassis.md) Phase 2 P2-4 | ⚠ Reviewed; actions open |
| ~~comp-009~~ | **Completed; RERUN 2026-07-14** on the real NM_144585.4 mRNA (original artificial-CDS run invalidated). 8 real-transcript target sites pass design filters; accessibility low (real RNAplfold) + off-target uncleared. See [interpretive page](./urat1-sirna-target-site-selection-computational.md). | [sirna-urat1-modality](./sirna-urat1-modality.md) Phase 2 P2-2 | ✓ Done (rerun) |
| ~~comp-011 TCM~~ | Reassigned 2026-05-05; TCM ChEMBL cross-check landed as comp-013 | — | ✓ Done as comp-013 |
| comp-021 | Compound × upstream-complement chokepoint × matched-assay-format mapping (resolves RA 44× spread) | [upstream-complement-verification-rerun-computational](./upstream-complement-verification-rerun-computational.md) | Low (parked) |
| ~~comp-022~~ | Completed 2026-05-14 — see Analyses above | — | ✓ Done |
| ~~comp-024~~ | Completed 2026-05-16 — RED for LBP framing; C1-INH parallel GREEN-provisional → tracked as comp-037. See Analyses above | — | ✓ Done |
| comp-023 | Completed 2026-05-14 — GREEN; see Analyses above | — | ✓ Done |
| ~~comp-022 v2~~ | Completed 2026-05-14 — see comp-022 Status above | — | ✓ Done |
| ~~comp-023 v2~~ | Deprioritized 2026-05-16 — koji-cordycepin removed from active stack ([koji-endgame-strain §3.5](./koji-endgame-strain.md)) | — | Closed |
| ~~comp-025~~ | Deprioritized 2026-05-16 — koji-cordycepin removed; cultivation-route cordycepin inherits native ADA-inhibitor pairing | — | Closed |
| ~~comp-026~~ | Deprioritized 2026-05-16 — multi-cassette induction interference moot for cordycepin; re-openable for future cytosolic third-cassette candidate | — | Closed |
| ~~comp-027~~ | Completed 2026-05-16; **downgraded to hypothesis-generator 2026-07-14** — single strict-GREEN modeled point at 100 mg/d (not a validated 75–125 window). See Analyses above | — | ✓ Done |
| ~~comp-030~~ | Completed 2026-05-15 — see Analyses above | — | ✓ Done |
| ~~comp-029~~ | Completed 2026-05-16 — YELLOW; see Analyses above | — | ✓ Done |
| ~~comp-031~~ | **Not decision-usable** — its flat-UOX, PDB-derived-butyrate, and compartment assumptions do not support the reported quantitative result or topology recommendation. See [dual-chassis page](./dual-chassis-ecn-pdb-uricase-computational.md), comp-044/046, and §1.34/§1.37. | — | ✓ Done |
| ~~comp-032~~ | Completed 2026-05-16 — ~~GREEN~~ **SUPERSEDED by comp-047 2026-07-14**; verdict retracted (tautological positive-control validation per comp-review 2026-07-13). See Analyses above | — | ✓ Done (superseded) |
| ~~comp-047~~ | **Completed 2026-07-14 — INCONCLUSIVE** (real Vina docking). CFTR-corrector positive controls fail to earn rank (0/4); rigid docking can't discriminate Q141K chaperones; chaperone-rescue ranking not computationally established. Supersedes comp-032. See Analyses above | [Q141K trafficking + urate-flux assay](./validation-experiments.md) | ✓ Done |
| ~~comp-033~~ | Completed 2026-05-16 — RED single-dose Cmax-equivalent; reframed in comp-036 (YELLOW receptor-occupancy). See Analyses above | — | ✓ Done |
| ~~comp-036~~ | Completed 2026-05-16 — YELLOW repeat-dose receptor-occupancy framing; salvages comp-033 RED. See Analyses above | — | ✓ Done |
| ~~comp-037~~ | Completed 2026-05-17 — MODERATE (kinetic-competition gated); glyco GREEN for serpin-core aa 123–500 in luminal topology. See Analyses above | — | ✓ Done |
| ~~comp-038~~ | Completed 2026-05-20 — YELLOW; HPLC-UV culture-supernatant candidate + electrochemical fecal SCFA future direction; no home/colorimetric butyrate assay ready. See Analyses above | — | ✓ Done |
| ~~comp-039~~ | Completed 2026-05-21 — All four upstream-CP0 candidates classified CFH-INDEPENDENT (rosmarinic acid High, luteolin Medium, HCP/HCPM/CHCP High, Helicteres Medium-replication-bounded). See Analyses above | — | ✓ Done |
| comp-040 | Wet-lab in-vitro CFH-depleted-serum MSU-crystal complement-activation assay — definitive falsification test of comp-039 CFH-independence classification for rosmarinic acid, luteolin, and HCP. Defined by [comp-039](./cfh-mechanism-dissociation-cp0-candidates-computational.md) §7. **Sequenced downstream of [`validation-experiments.md` §1.30](./validation-experiments.md)** for HCP specifically — comp-040 only fires if §1.30 prioritization screen returns positive. (Other candidates — rosmarinic acid, luteolin — could fire comp-040 independent of §1.30 since they have their own analogous prioritization gates.) | [comp-039](./cfh-mechanism-dissociation-cp0-candidates-computational.md), [validation-experiments.md §1.30](./validation-experiments.md), [gout-genetic-variants.md](./gout-genetic-variants.md) Category 5, [complement-c5a-gout.md](./complement-c5a-gout.md) §6.3 | Blocked (OE wet-lab access; relevant to lab-partner conversations) |
| comp-041 | East Asian cohort feasibility scan for Houttuynia × rs1061170 × incident gout cross-tab — KoGES, China Kadoorie Biobank, Singapore Chinese Health Study. Parallels the 2026-05-19 UKB feasibility analysis but for the Houttuynia-tractable population (HCP exposure captured; Y402H allele frequency ~5-6%). Defined by [comp-039](./cfh-mechanism-dissociation-cp0-candidates-computational.md) §5 + §7. | [comp-039](./cfh-mechanism-dissociation-cp0-candidates-computational.md), [logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md](../logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md) | Queueable (opens when East Asian collaboration channel becomes available) |
| ~~comp-028~~ | Deprioritized 2026-05-16 — cordycepin-arm moot; general design-escape question non-load-bearing today; re-openable for future cytosolic third-cassette candidate | — | Closed |

---

## Infrastructure proposals

### comp-NNN verification agent (ClockBase hypothesis-then-verify pattern) — Planned (2026-05-08)

Every comp-NNN run produces output from a *generation* agent; add a second-pass *verification* agent (different vendor preferred per the multi-vendor heterogeneity discipline) that re-checks every load-bearing number (disulfide counts, residue indices, IC50/Ki, accession numbers, cohort sizes) against primary databases (UniProt, ChEMBL, PDB, PubMed) before commit. Sister discipline to the per-page Pre-commit verification gate (CLAUDE.md Rule 4) — same pattern at a different scope. Would have caught the 2026-05-06 DAF SCR1-4 disulfide hallucination at generation time. Cost ~$3–5 + 10–30 min per comp.

**Detail:** [etc/autonomous-screening-methodology](./etc/autonomous-screening-methodology.md) §"Hypothesis-then-verify pattern" · [etc/manual-literature-mining](./etc/manual-literature-mining.md) §"Pre-commit verification gate" · [operations/comp-018-vs-comp-020-retrospective](../operations/comp-018-vs-comp-020-retrospective.md)

---

### pcSec-class proteome-constrained *A. oryzae* GEM build — Planned (2026-05-14)

Layer secretion-pathway proteome-cost constraints on iWV1314 (Vongsangnak 2008): explicit PDI/calnexin/BiP saturation, signal-peptide processing capacity, KEX2 flux, Sec61 throughput. Enables rigorous burden evaluation for any future *secreted* third cassette (DAF SCR1-4 per H05; engineered C1-INH per comp-018 Phase 2; complestatin NRPS per comp-024). Validation gate: must reproduce comp-023 GREEN for cytosolic cns1+cns2. Multi-week research project; not a single-subagent task. Current comp-023 v1 limitation.

**Detail:** [chaperone-orthogonal-stacking](./chaperone-orthogonal-stacking.md) · companion to verification-agent proposal (per-run vs per-strain infrastructure scopes)

---

## How to add a new analysis

1. Create `etc/experiments/comp-NNN-<slug>/` with `analyze.py`, `inputs/`, `outputs/`, `README.md`, `inputs/provenance.md`
2. Add an entry to the "Analyses" section above (compact format) or the "Planned Analyses" table
3. Create `wiki/<slug>-computational.md` for the interpretive page
4. Link from the relevant wet-lab experiment in `validation-experiments.md`
5. Commit script + inputs + outputs together (outputs are version-controlled; they are the peer-reviewable artifact)
