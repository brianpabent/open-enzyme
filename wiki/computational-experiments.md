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

### comp-037 — C1-INH (SERPING1) Protease Stability + Glycosylation Feasibility in EcN-Luminal Format — MODERATE (kinetic-competition gated) (2026-05-17)

**Question:** Will human C1-INH (UniProt P05155) survive luminal-secreted expression in engineered *E. coli* Nissle 1917, and is the loss of N-glycosylation a hard block? Closes the C1-INH-on-EcN side of the two-chassis CP0 architecture surfaced 2026-05-16 (C1-INH on LBP-luminal + DAF SCR1-4 on koji-secreted).

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

### comp-032 — ABCG2 Q141K Pharmacological-Chaperone Virtual Screen — GREEN (2026-05-16)

**Question:** Is there an FDA-approved small molecule that binds ABCG2 Q141K's nucleotide-binding domain (NBD) and could rescue trafficking, or does the FDA-approved drug surface lack chaperone-active hits — requiring novel chemistry?

**Verdict:** **GREEN.** Shortlist of 10 candidates passes the four-gate filter (composite ≥ 0.75, chaperone-compatible drug class, 503A-eligible-or-chaperone-class, oral bioavailable). All four CFTR-corrector positive controls (lumacaftor, tezacaftor, ivacaftor, elexacaftor) rank in the top 11% of the 134-molecule library, all above the highest-scoring decoy.

**Key findings:**
- Three mechanistically-distinct chemistry classes pass with composite ≥ 0.85: CFTR correctors (lumacaftor top hit, 1.000; same ABC superfamily); tetramer/aggregate stabilizers (tafamidis, diflunisal — anionic aromatics matching Q141K's +1 pocket); bile-acid chemical chaperones (ursodiol, TUDCA — Hsp70 axis, F508del-CFTR rescue precedent).
- Heuristic independently re-elevates sodium butyrate + vorinostat — the HDAC-class Q141K rescuers the wiki already names (Basseville 2012). Independent corroboration.
- Next step: real-docking re-screen (AutoDock Vina) on top 10 + targeted HEK293-Q141K trafficking assay. Do NOT pivot to novel-binder design — the repurposing surface is empirically non-empty.

**Informs:** [chassis-pending-interventions §7](./chassis-pending-interventions.md) (promotes placeholder comp-NNN to comp-032) · [abcg2-modulators](./abcg2-modulators.md) §"Pharmacological-chaperone route" · [compounding-pharmacy-track](./compounding-pharmacy-track.md)

**Detail:** [interpretive](./abcg2-q141k-chaperone-screen-computational.md) · [experiments/](./etc/experiments/comp-032-abcg2-q141k-chaperone-screen/) · Complete v1

---

### comp-031 — Dual-chassis EcN PDB + Uricase Additive SUA Prediction — YELLOW (2026-05-16)

**Question:** Does a dual-chassis stack of engineered EcN expressing the 2,8-dioxopurine PDB cluster (CBT2.0, Li 2025 PMID 41070194) co-administered with a PULSE-style luminal uricase deliver additive SUA reduction beyond either arm alone? Does PDB-derived butyrate compound with the gut-lumen uricase sink via ABCG2 induction / Q141K trafficking rescue?

**Verdict:** **YELLOW (provisional)** — combined > either arm but well below naive sum. Two urate-consumption arms compete for scarce luminal urate substrate (per comp-019 substrate-limited regime); PDB pathway adds INDEPENDENT mechanism via butyrate → PPARγ ABCG2 induction (WT alleles) + butyrate → HDAC Q141K trafficking rescue. **Combined ΔSUA: −1.8 to −1.9 mg/dL across genotypes** (90% CI roughly −2.2 to −1.3). Additive bump over PDB-alone: ~−0.1 to −0.2 mg/dL.

**Key findings:**
- Engineering handoff: route PDB and uricase to **separate strains, not a dual-cassette EcN.** Substrate competition means single-chassis dual-cassette engineering gains ~nothing in additional SUA reduction relative to two co-administered strains. Avoids 8-gene PDB cluster + uricase coordinated-expression complexity.
- Largest genotype-stratified additive bump in Q141K-hom (HDAC trafficking-rescue axis is alleles-specific).
- Independent of comp-019 single-chassis verdict; complements rather than supersedes.

**Informs:** [chassis-pending-interventions](./chassis-pending-interventions.md) §"Multi-chassis stacks" M1 · [purine-degrading-bacteria](./purine-degrading-bacteria.md) · [uricase-abcg2-genotype-stratification-computational](./uricase-abcg2-genotype-stratification-computational.md) (comp-019 anchor)

**Detail:** [interpretive](./dual-chassis-ecn-pdb-uricase-computational.md) · [experiments/](./etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/) · Complete v1

---

### comp-027 — Disulfiram Dose Modeling for GSDMD Blockade vs DER Ceiling — YELLOW-leaning-GREEN (2026-05-16)

**Question:** Is there a sub-AUD oral disulfiram dose window where plasma DSF engages GSDMD (CP6b pyroptotic-exit block) at a therapeutically meaningful level while plasma Me-DTC stays below the ALDH-inhibition threshold driving the disulfiram-ethanol reaction (DER)?

**Verdict:** **YELLOW-leaning-GREEN** — narrow sub-AUD window exists around **75–125 mg/day**, centered on 100 mg/day. At 100 mg/d: ~57% GSDMD blockade (DSF Cmax ~0.4 µM) at ~40% ALDH inhibition (Me-DTC ~70 nM, right at Faiman DER hypotension threshold). Below 50 mg/d, GSDMD blockade drops <40%; above 125 mg/d, ALDH inhibition crosses DER threshold. Strict-GREEN at 100 mg/d under conservative cell-free EC50 anchor; cellular-preincub anchor extends GREEN down to 50 mg/d. Gates the 503A compounding-pharmacy disulfiram pathway.

**Key findings:**
- Sub-AUD DSF is a **selective GSDMD inhibitor**, not a pan-NLRP3 inhibitor — the NLRP3-palmitoylation pathway (Xu 2024, 10 µM EC50) is NOT engaged at any sub-AUD dose.
- DER threshold is the load-bearing ceiling; alcohol-abstention requirement is a compliance question for the 503A protocol.
- Two EC50 anchors (cell-free vs cellular-preincub) bracket the GREEN window; cellular-preincub captures covalent-accumulation kinetics and is the more defensible anchor for chronic dosing.

**Informs:** [compounding-pharmacy-track §6](./compounding-pharmacy-track.md) · [disulfiram](./disulfiram.md) · [nlrp3-exploit-map](./nlrp3-exploit-map.md) CP6b

**Detail:** [interpretive](./disulfiram-dose-modeling-computational.md) · [experiments/](./etc/experiments/comp-027-disulfiram-dose-modeling/) · Complete v1

---

### comp-024 — Complestatin-Family BGC LBP-Chassis Feasibility — RED for LBP framing; C1-INH parallel GREEN-provisional (2026-05-16)

**Question:** Is the complestatin-family NRPS biosynthetic gene cluster heterologous-expression-tractable in an engineered LBP chassis (*E. coli* Nissle 1917, *Bacteroides thetaiotaomicron*) as the next CP0 (complement priming) engineering payload?

**Verdict:** **RED for the LBP-track framing.** Best host EcN YELLOW 0.544; *Bacteroides* RED 0.225. Dominant blocker: O₂-dependent tailoring chemistry (ComI/ComJ P450 oxidative phenolic coupling + ComH nonheme halogenase + Hmo FMN oxidase) fundamentally incompatible with colonic-anaerobic-resident lifestyle. Without P450-mediated phenolic coupling, the linear peptide lacks the rigid crosslinked architecture that gives complestatin its C1q/C4b affinity (Park 2016 M55/S56 deletions inactive). **C1-INH (LBP-luminal) parallel thread scores GREEN-provisional 0.774 on EcN** — recommended as next CP0 LBP payload instead (→ promoted to comp-037).

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
- Engineered C1-INH parallel thread proposed (near-twin to H05 DAF) → grounded in Phase 2 + promoted to comp-037.
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

### comp-014 — Medicinal Mushroom Compound × Chokepoint Mapping — Phase 3 complete (2026-05-17)

**Question:** Across all known characterized fungal natural products (globally, not Western pharma only), which compounds map onto OE chokepoints, and which fungal species are highest-leverage producers?

**Verdict:** **PHASE 3 COMPLETE.** 9,778 unified fungal compounds (LOTUS 6,798 + NPAtlas 4,535 + KNApSAcK 20 InChIKey-resolved; NPASS / TCMSP / HIT unreachable from sandbox — documented gap). 24 chokepoint targets queried via ChEMBL; **323 (compound × chokepoint) empirical hits across 12 chokepoints**; 177 / 9,778 compounds (1.81%) have ≥1 hit. Highest-potency: **Ganoderic acid H × TNFα Kd = 2.45 nM** (pChEMBL 8.61, CHEMBL1922178, *Ganoderma lucidum*); **Berkeleyamides A/D × CASP1 IC50 = 330 / 610 nM** (*Penicillium*); **Quercetin × ABCG2 EC50 = 30 nM** (*Agaricus*); **Ellagic acid × OAT1 IC50 = 270 nM** (*Penicillium* / *Phellinus*).

**Key findings:**
- *Ganoderma* triterpenoid scaffold (ganoderic acids H/D and stereoisomers) emerges as highest-potency direct-binding hit at TNFα, **on top of** the Phase 2 *G. applanatum* 2,4-DAE urate-axis finding — two distinct chokepoint axes, both worth pursuing. *Ganoderma* spp. earn closer look.
- **Berkeleyamides / Berkeleyones** (Penicillium): first fungal natural products with direct sub-µM CASP1 and low-µM IL-1β hits — opens an inflammasome-effector-axis fungal candidate beyond the polysaccharide-priming literature comp-014 Phase 1 + Phase 2 emphasized.
- **Target-orphan rate 98.19%** — SwissTargetPrediction predicted-target layer is the next load-bearing step; sandbox-blocked here, deferred to re-run. 9,601 compounds with zero empirical chokepoint hits.
- **12 of 24 chokepoints have ZERO fungal-source ChEMBL hits**: NLRP3, ASC, GLUT9, C5aR1, Lp-PLA2, KEAP1, OAT4, PINK1, PDI, PDIA3, TXN, TXNIP. Confirms the comp-013 / comp-020 ChEMBL-Western-pharma-bias finding empirically for fungal-source NPs.
- Multi-chokepoint compounds surfaced: morin (4 chokepoints: ABCG2, CASP1, URAT1, XO); genistein (4: ABCG2, CASP1, PPARG, XO). Both plant-origin flavonoids in mushroom substrate — not biosynthesis attribution.
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
| ~~comp-024~~ | Completed 2026-05-16 — RED for LBP framing; C1-INH parallel GREEN-provisional → promoted to comp-037. See Analyses above | — | ✓ Done |
| comp-023 | Promoted to Analyses 2026-05-14 (GREEN) | — | ✓ Done |
| ~~comp-022 v2~~ | Completed 2026-05-14 — see comp-022 Status above | — | ✓ Done |
| ~~comp-023 v2~~ | Deprioritized 2026-05-16 — koji-cordycepin removed from active stack ([koji-endgame-strain §3.5](./koji-endgame-strain.md)) | — | Closed |
| ~~comp-025~~ | Deprioritized 2026-05-16 — koji-cordycepin removed; cultivation-route cordycepin inherits native ADA-inhibitor pairing | — | Closed |
| ~~comp-026~~ | Deprioritized 2026-05-16 — multi-cassette induction interference moot for cordycepin; re-openable for future cytosolic third-cassette candidate | — | Closed |
| ~~comp-027~~ | Completed 2026-05-16 — YELLOW-leaning-GREEN (sub-AUD window 75–125 mg/d). See Analyses above | — | ✓ Done |
| ~~comp-030~~ | Completed 2026-05-15 — see Analyses above | — | ✓ Done |
| ~~comp-029~~ | Completed 2026-05-16 — YELLOW; see Analyses above | — | ✓ Done |
| ~~comp-031~~ | Completed 2026-05-16 — YELLOW; combined ΔSUA −1.8 to −1.9 mg/dL; separate-strain handoff. See Analyses above | — | ✓ Done |
| ~~comp-032~~ | Completed 2026-05-16 — GREEN; 10-candidate FDA-approved shortlist; lumacaftor top hit. See Analyses above | — | ✓ Done |
| ~~comp-033~~ | Completed 2026-05-16 — RED single-dose Cmax-equivalent; reframed in comp-036 (YELLOW receptor-occupancy). See Analyses above | — | ✓ Done |
| ~~comp-036~~ | Completed 2026-05-16 — YELLOW repeat-dose receptor-occupancy framing; salvages comp-033 RED. See Analyses above | — | ✓ Done |
| ~~comp-037~~ | Completed 2026-05-17 — MODERATE (kinetic-competition gated); glyco GREEN for serpin-core aa 123–500 in luminal topology. See Analyses above | — | ✓ Done |
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
