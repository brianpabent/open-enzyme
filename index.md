# Open Enzyme

Open source library of engineered, food-grade microbial strains producing therapeutic enzymes. Phase 0 — Research & Design.

**First targets:** Uricase (gout / hyperuricemia + NLRP3-driven inflammation) · Digestive enzymes (EPI) · Koji (*A. oryzae*) as a natural multi-enzyme producer.

---

## Status

**Current platform thesis:** One engineered *A. oryzae* koji strain expressing uricase + NLRP3 inhibitors, fermented on rice bran, positioned as adjunct to allopurinol for gout — not a monotherapy replacement. Derivation in [wiki/synthesis.md](wiki/synthesis.md).

**Two parallel outputs:** (1) A **discovery engine** — a chokepoint-based methodology for mapping every vector that causes, treats, or mitigates a given disease, applied first to gout. Produces a structured cascade map plus a repurposing surface (FDA-approved drugs that hit relevant chokepoints but were never clinically tested for the target disease). (2) An **open-source strain library** — the engineered-koji platform is one synthesis from the discovery engine. (source: open-enzyme-vision.md, §1–2)

**Platform positioning:** Open Enzyme is a **food-derived, multi-target NLRP3 pathway modulator** platform — not an attempt to produce a food-grade analog of the direct NLRP3 inhibitor class (MCC950, dapansutrile, oridonin). The stack hits upstream priming (CP1a/CP1b), K⁺ efflux (CP2), active resolution (CP5b), and neutrophil amplification (CP6a) — chokepoints that pharma has not rigorously tested in gout. (source: open-enzyme-vision.md, §10)

**Synthesis queue:** [wiki/synthesis.md](wiki/synthesis.md) — unreviewed cross-analysis findings. The sweep daemon prepends new findings here after each save; prune by deleting bullets you've acted on. Git preserves the full history.

**Cheapest next experiments** (from current synthesis, ordered by cost/ROI):

| # | Experiment | Cost | Weeks | Decides |
|---|---|---|---|---|
| 0 | **PERT-timing self-experiment (IN PROGRESS)** — BoulderBio dose/timing n=1 | ~$0 | ongoing | Dose framework for engineered platform; split-dose vs. sustained-release formulation |
| 1 | Rice bran vs plain rice substrate → uricase GI survival (§1.15) | $800 | 3 | Free substrate optimization, no engineering |
| 2 | Quercetin + ursolic acid + carnosine combo on MSU-stimulated macrophages (§1.17) | $1,500 | 4 | Whether to engineer one NLRP3 inhibitor or three |
| 3 | WT / SB-1 / OPT-1 engineered uricase variants in koji → GI simulation (§1.16) | $2,000 | 8 | Platform choice (koji vs yeast) |
| **GATE** | **Ward 1995 dual-cassette feasibility (§1.9) — #1 priority gate** | $3–5K | 8–12 | Single-strain vs. two-strain endgame; gates entire koji endgame thesis |
| 4 | Carnosine co-expression in *A. oryzae* (§1.24) — optional third cassette | $1,500–2,500 | 4–6 | Androgen-driven URAT1 countermeasure; gates carnosine module for male/high-T product config |
| LBP-1 | LBP track Phase 2: lit scans (engineering toolkit + commercial landscape + FDA LBP path) — see [`engineered-lbp-chassis.md`](wiki/engineered-lbp-chassis.md) Open Follow-Ups | $0 | 1–2 | Whether the engineered-LBP peer track is technically and commercially viable to pursue |
| LBP-2 | LBP track Phase 2: comp-008 *F. prausnitzii* heterologous expression feasibility | $0 | 1 | Which OE-relevant payloads are tractable in *F. prausnitzii* (uricase / lactoferrin / sCR1 / butyrate boost) |
| 1.23-T1 | Androgen × MSU × NLRP3 macrophage screen (§1.23 Tier 1, THP-1) — fills documented literature gap | $5–10K | 6–8 | Whether direct-androgen contribution to gout inflammation exists; gates Tiers 2–3 |
| siRNA-1 | siRNA / URAT1 track Phase 2: lit scans (kidney-tropic conjugate chemistry + commercial landscape + FDA regulatory path) — see [`sirna-urat1-modality.md`](wiki/sirna-urat1-modality.md) Open Follow-Ups | $0 | 1–2 | Whether kidney-tropic siRNA delivery chemistry is on a 3–5 year first-in-human horizon vs. stalled |
| siRNA-2 | siRNA / URAT1 track Phase 2: comp-009 URAT1 mRNA target site selection (RNAfold + accessibility scoring) | $0 | 1 | Whether URAT1 mRNA has accessible siRNA target sites — cheapest mechanistic killshot for the H03 thesis |
| TCM-1 | TCM track Phase 2: P2-1 lit scan (Si Miao San family + Smilax glabra + Bai Hu Jia Gui Zhi Tang) — **global multilingual sources by default** (ChiCTR, CNKI/WanFang, J-STAGE) — see [`tcm-modern-rigor-intersection.md`](wiki/tcm-modern-rigor-intersection.md) Open Follow-Ups | $0 | 1–2 | Whether classical TCM gout formulas have credible modern Chinese clinical signal vs. tradition-only |
| TCM-2 | TCM track Phase 2: comp-011 ChEMBL cross-check of 8 candidate TCM gout compounds (Smilax glabra, Rheum officinale, Plantago asiatica, Phellodendron, Polygonum cuspidatum, Cinnamomum cassia, Atractylodes, Astragalus) | $0 | 1 | Which TCM compounds have curated bioactivity at gout-relevant chokepoints at achievable gut-luminal concentrations |

See [wiki/validation-experiments.md](wiki/validation-experiments.md) for the full consolidated experiment list.

---

## Core Pathology & Targets

- **[Gout Pathophysiology](wiki/gout-pathophysiology.md)** — Complete gout cascade: purine metabolism → uric acid → crystallization → NLRP3 → flare; current treatments; clinical pipeline; genomics (351 GWAS loci)
- **[Uricase (Urate Oxidase)](wiki/uricase.md)** — The missing enzyme: evolutionary loss ~15Mya, A. flavus uaZ gene, rasburicase, engineering for gut-lumen degradation
- **[NLRP3 Inflammasome](wiki/nlrp3-inflammasome.md)** — All 7 chokepoints mapped (v1.2: CP0 complement priming, CP1a TNFSF14/LIGHT, CP5b active resolution, CP6a 5-LOX/LTB4); MSU crystal activation; pharmaceutical targets (dapansutrile, firsekibart)
- **[Digestive Enzymes & EPI](wiki/digestive-enzymes.md)** — Lipase, protease, amylase deficits; wild-type koji as immediate solution; commercial supplements (Creon, Zenpep)
- **[SIBO](wiki/sibo.md)** — Lynn's condition; brush-border enzyme damage; NLRP3 involvement; KPV relevance
- **[Fructose Connection](wiki/fructose-connection.md)** — Hidden gout accelerant: fructokinase (no negative feedback), ATP depletion cascade, GLUT9 dual transporter, KHK inhibitors
- **[Androgen-Urate Axis](wiki/androgen-urate-axis.md)** — Sex-hormone layer on urate handling: testosterone ↑URAT1 / ↓ABCG2; estrogen opposite; SHBG and the bound/free picture; TRT/SERM/AAS/AI effects; post-menopausal convergence

## Engineered Organisms & Platforms

- **[Saccharomyces cerevisiae](wiki/saccharomyces-cerevisiae.md)** — GRAS yeast; rasburicase expression precedent; S. boulardii; expression systems (TEF1p, GPDp); delivery formats
- **[Aspergillus oryzae](wiki/aspergillus-oryzae.md)** — Koji mold; native enzyme production; transformation methods; dual-purpose strain vision; fermentation on rice
- **[Koji Endgame Strain](wiki/koji-endgame-strain.md)** — platform thesis: one engineered *A. oryzae* strain, 5 chokepoints from 4 molecules (uricase + lactoferrin engineered; kojic acid + ergothioneine native); Ward 1995 dual-cassette architecture as gating feasibility test
- **[Engineered LBP Chassis](wiki/engineered-lbp-chassis.md)** — peer track to koji: engineered obligate-anaerobe colonic residents (*F. prausnitzii*, *Akkermansia*, *Bacteroides*) for durable colonization; butyrate dual-action (PPARγ WT ABCG2 + HDAC Q141K rescue); commercial-pharmaceutical track; 6 Phase 2 in silico follow-ups queued (source: engineered-lbp-chassis.md)
- **[siRNA / URAT1 Modality](wiki/sirna-urat1-modality.md)** — discovery-engine output: kidney-tropic siRNA against URAT1 mRNA; sequence-specific renal reabsorption knockdown; eliminates benzbromarone-class off-target metabolite risk; gated on kidney-tropic conjugate delivery chemistry maturation (3–5 yr horizon); 6 Phase 2 in silico follow-ups queued (source: sirna-urat1-modality.md)
- **[TCM × Modern Rigor — Discovery-Engine Lens](wiki/tcm-modern-rigor-intersection.md)** — fourth peer-track exploration vector: applies six-rule methodology (chokepoint mapping, ChEMBL cross-check, bioavailability-honest framing, formula decomposition, standardized-extract specification, falsification-card discipline) to TCM materia medica with documented gout/hyperuricemia indications; 8 candidate compounds tabulated; Si Miao San and Smilax glabra as highest-priority targets; 6 Phase 2 in silico follow-ups queued; H04 stub committed; global multilingual sources by default (ChiCTR, CNKI/WanFang, J-STAGE). (source: tcm-modern-rigor-intersection.md)
- **[Ward 1995 §1.9 Lab Access — Global Landscape](wiki/ward-1995-lab-access-global.md)** — active-search resource mapping Japan / China / Europe parallel options for executing the #1 priority gate (§1.9 dual-cassette feasibility test); Maruyama lab at University of Tokyo is the single most important contact globally (only verified source of NSlD-ΔP10); Jiangnan University (C19 chassis) and DTU Mortensen group (CRISPR toolkit) are parallel-path options; includes draft email to Maruyama and order-of-operations parallel-pursuit plan. (source: ward-1995-lab-access-global.md)
- **[Open Source Platform](wiki/open-source-platform.md)** — GitHub strain library vision; software analogy; no patents; community validation; forkable strains

## Delivery & Barrier Biology

- **[Gut-Lumen Sink](wiki/gut-lumen-sink.md)** — ABCG2 pathway; ~1/3 of UA excretion; the insight that systemic absorption isn't needed; ALLN-346, PULSE probiotic
- **[ABCG2 Modulators](wiki/abcg2-modulators.md)** — Pharmacological levers on the gut urate sink: PPARγ-mediated induction via butyrate (DASH RCT shows 0.25–0.73 mg/dL UA reduction); HDAC-inhibitor rescue of the Q141K polymorphism (the #1 gout-causing ABCG2 variant); the supplement-stack contradiction (curcumin/quercetin/EGCG as functional inhibitors); CKD failure caveat
- **[Blood Barrier](wiki/blood-barrier.md)** — Every delivery route evaluated; why systemic delivery is hard; why gut-lumen wins

## Gene Therapy

- **[CRISPR Uricase](wiki/crispr-uricase.md)** — Georgia State breakthrough (2025); ancestral uricase reconstruction; pseudogene reactivation; delivery vectors (LNP, AAV, base editing)

## Peptides & Compounds

- **[BPC-157](wiki/bpc-157.md)** — 15-amino-acid gastric peptide; NO system modulation; gut healing; gout relevance via gut-UA axis
- **[KPV Tripeptide](wiki/kpv-peptide.md)** — α-MSH fragment; dual NF-κB + NLRP3 inhibition; gut anti-inflammatory; strongest mechanistic case for gout
- **[BHB / Ketones](wiki/bhb-ketones.md)** — Hits 3 of 7 NLRP3 chokepoints (CP1, CP2, CP3); endogenous via fasting/keto; may be more impactful than any single peptide
- **[Oridonin](wiki/oridonin.md)** — Natural NLRP3 inhibitor; covalent NACHT domain Cys279 binding; traditional medicine origin
- **[Disulfiram](wiki/disulfiram.md)** — Gasdermin D blocker (Antabuse); repurposed drug; CP6b in v1.2 NLRP3 map
- **[Colchicine](wiki/colchicine.md)** — Tropolone alkaloid; dual-hit NLRP3 disruptor: CP3 (ASC speck via microtubule depolymerization) + CP2 (P2X7 pore block); AGREE trial low-dose regimen; COLCOT/LoDoCo2 cardiovascular repositioning; Lodoco FDA 2023; narrow therapeutic index; CYP3A4/P-gp interaction surface
- **[EGCG](wiki/egcg.md)** — Green tea catechin; 20S proteasome 86 nM (ChEMBL); unifies CP1a (IκBα) + CP4 (caspase-1) + CP5 (IL-1β) via single mechanism
- **[Theaflavins](wiki/theaflavins.md)** — Black-tea polyphenols (oxidation products of EGCG/ECG); distinct mechanism from EGCG: NLRP3-NEK7 disruption (CP2/CP3 inflammasome assembly) + multi-transporter renal urate handling (↓URAT1, ↓GLUT9, ↑OAT1/OCTN1/OAT2) + secondary TNFSF14/HVEM coverage. Direct MSU peritonitis Animal Model. Tier 2 supplement candidate (added 2026-05-05).
- **[Lactoferrin](wiki/lactoferrin.md)** — Single protein, four-chokepoint coverage (CP1a/CP4/CP6b/CP5b); fermentable in *A. oryzae* (Ward 1992 25 mg/L → Ward 1995 >2 g/L *A. awamori*); Year 2-3 engineering target
- **[Zileuton](wiki/zileuton.md)** — FDA-approved 5-LOX inhibitor (asthma); perfect CP6a mechanism match; zero ClinicalTrials.gov gout entries — latent repurposing candidate

## Strategy & Practice

- **[Gout Clinical Pipeline](wiki/gout-clinical-pipeline.md)** — Current ClinicalTrials.gov + PubMed snapshot (2026-04-23): ALLN-346 program terminated 2022, dapansutrile gout development stalled, canakinumab FDA-approved for gout Aug 2023, PRX-115 is the new systemic-uricase competitor. Refreshable quarterly via MCP.
- **[Supplements Stack](wiki/supplements-stack.md)** — Practical NOW/SOON/FUTURE recommendations with dosing and evidence levels
- **[Complement C5a in Gout](wiki/complement-c5a-gout.md)** — CP0: MSU directly activates complement; C5a dominant NLRP3 priming signal; avacopan repurposing candidate; stack gap
- **[TNFSF14 / LIGHT in Gout](wiki/tnfsf14-gout-target.md)** — CP1a: Second-highest gout-flare biomarker; LIGHT amplifies NF-κB; EGCG and DHA as natural moderators; CERC-002 mAb precedent
- **[SPM Resolution Pathway](wiki/spm-resolution-pathway.md)** — CP5b: RvD1/MaR1 direct MSU gout animal model evidence; ALX/FPR2 agonism; aspirin-triggered resolvins
- **[Self-Experiment Protocol](wiki/self-experiment-protocol.md)** — Brian's minimum-viable monitoring plan: blood panels (CBC/CMP/UA/hs-CRP/LDH/HbA1c), 16S stool, daily diary, red-flag halt criteria; specialty biomarkers (C3/C4/CH50/C5a CP0; urinary LTE4 CP6a)
- **[Open Questions](wiki/open-questions.md)** — Cross-wiki index of unresolved questions organized by chokepoint/mechanism — living action queue for research prioritization
- **[Modality × Target Matrix](wiki/modality-chokepoint-matrix.md)** — Exploration surface: rows = modalities (small molecules, peptides, engineered yeast/koji, engineered LBPs, phages, exosomes, mRNA/siRNA, base editing, pharmacological chaperones, biologics, monitoring tech); columns = anatomical/cellular targets (gut compartment, renal compartment, tissue-resident NLRP3 sites, monitoring). Surfaces ~10 high-leverage open exploration vectors where novel modalities could open stuck nodes. **OE is the mission, not the koji chassis** — the matrix keeps the orthogonal "what tools haven't we considered" search visible.
- **[Carnosine](wiki/carnosine.md)** — Dual-phenotype (hyperuricemia + NLRP3) in rats; unique in the stack for addressing both UA and inflammation in a single compound
- **[ChEMBL Cross-Check](wiki/chembl-cross-check.md)** — Standing rigor tool: quarterly ChEMBL v34 cross-reference of stack compounds; curcumin 24.2 μM NLRP3, berberine→TDO, resveratrol→DPP-4, EGCG→proteasome 86 nM
- **[Cannabinoids & Terpenes](wiki/cannabinoids-terpenes.md)** — CBD, CBG, CBC, THCV, beta-caryophyllene, myrcene: NLRP3 mechanisms, gout evidence, EPI applications; beta-caryophyllene has direct MSU gout animal model data
- **[Validation Experiments](wiki/validation-experiments.md)** — All proposed experiments consolidated: in vitro, animal, and human self-experimentation phases
- **[Bio-AI Tools](wiki/bio-ai-tools.md)** — Open source protein AI (ESM-2, ColabFold, Boltz-2, RFdiffusion2, ProteinMPNN, SPURS, DiffDock, CodonTransformer) + commercial tools (GPT-Rosalind, Amazon Bio Discovery, Coefficient Bio) + **Anthropic life-sciences marketplace** (17 à la carte plugins — PubMed, bioRxiv, ChEMBL, Open Targets, ClinicalTrials.gov MCP servers as Phase 0 core); project-specific prompts and workflow
- **[Paperclip (GXL)](wiki/paperclip-deep-dive.md)** — Agent-native scientific literature MCP: 11M full-text papers (PMC + arXiv + bioRxiv/medRxiv) + 150M abstracts (OpenAlex), with stateful `--from` chaining and `map` synthesis primitive. Complementary to the Anthropic MCP marketplace (Paperclip wins on full-text search and cross-source synthesis; marketplace wins on per-source depth like MeSH and ChEMBL bioactivities). **Sweep-daemon integration DECIDED 2026-05-05: do not integrate** — `map` operator systematically hallucinates quantitative data and misattributes organisms (verified against known-correct ground truths); manual-research-only tool with grep-verify discipline. (source: paperclip-deep-dive.md)
- **[Linter Design (Falsification + Document Lint)](wiki/linter-design.md)** — Design doc for the two-linter architecture: Document Lint (always-on, non-blocking, regex + semantic rules over the wiki) and Falsification Lint (on-demand, per-hypothesis Card generation with killshot menus, failure-mode ontology, survival scoring). Implementation out of scope for this phase.
- **[Hypotheses Index](wiki/hypotheses/README.md)** — Committed scientific claims in Falsification Card form. H01 Ward dual-cassette (koji endgame gate); H02 Engineered LBP thesis (stub); H03 siRNA/URAT1 thesis (stub); H04 TCM × Modern Rigor methodology lens (stub, committed 2026-05-05).
- **[Computational Experiments](wiki/computational-experiments.md)** — Tracking index for all computational analyses (comp-001 through comp-010). comp-001: uricase shio-koji protease stability (LOW risk — reframes §1.10 uricase arm as confirmation experiment); comp-004: supplement ABCG2 antagonism (VERY HIGH risk for quercetin/curcumin at supplement doses); comp-005: lactoferrin shio-koji protease stability (HIGH/MODERATE — signal-peptide-contingent); comp-006: DAF/CD55 ectodomain protease stability (HIGH — stalk-contingent; SCR1-4 core is LOW); comp-007: food-grade HDAC inhibitor screen (butyrate rank 1, 167× HDAC6 selectivity confirmed); **comp-010: dual-cassette cassette compatibility (LOW overall risk — no blocking issues; KEX2 pos 579 moderate risk in Lf; uricase C-terminal SKL PTS1 verify; combined ER burden 1.06× Huynh 2020 baseline)**. (source: computational-experiments.md)
- **[Cassette Compatibility — Dual-Cassette Koji Endgame Strain (comp-010)](wiki/cassette-compatibility-computational.md)** — In silico sequence analysis of the uricase (Q00511) + lactoferrin (P02788) payload pair: codon usage, KEX2 geometry, secretion targeting, disulfide load, N-glycosylation, combined ER burden vs. Huynh 2020 adalimumab baseline. Overall cassette-design risk: LOW. Two actionable design notes: (1) monitor Lf KEX2 site at mature pos 579 by SDS-PAGE; (2) verify uricase secretion vs. C-terminal SKL PTS1 motif. Informs §1.9 Ward 1995 dual-cassette feasibility test. (source: cassette-compatibility-computational.md)
- **[Uricase Protease Stability (comp-001)](wiki/uricase-protease-stability-computational.md)** — AlphaFold + P1/P1' analysis: zero exposed cleavage sites, mean pLDDT 97.1; LOW risk verdict; shio-koji delivery thesis structurally supported.
- **[Lactoferrin Protease Stability (comp-005)](wiki/lactoferrin-protease-stability-computational.md)** — HIGH (full sequence, signal-peptide-driven) / MODERATE (mature protein); lactoferrin arm of §1.10 remains a feasibility gate.
- **[DAF/CD55 Protease Stability (comp-006)](wiki/daf-cd55-protease-stability-computational.md)** — HIGH verdict for soluble ectodomain (aa 35–353); stalk-contingent (Ser/Thr stalk aa 286–353 drives all exposed sites); SCR1-4 core contributes zero exposed sites; stalk-truncated construct (aa 35–285) is the logical follow-up.
- **[Food-Grade HDAC Inhibitor Screen (comp-007)](wiki/food-grade-hdaci-screen-computational.md)** — Stage 1 in silico screen: butyrate rank 1 (composite 0.374, HIGH confidence, 167× HDAC6 selectivity); sulforaphane rank 2 (LOW confidence); PEITC rank 3. Advances to Stage 2 Caco-2/HepG2 paired HDAC activity assay.
- **[Supplement ABCG2 Antagonism (comp-004)](wiki/supplement-abcg2-antagonism-computational.md)** — IC50 occupancy analysis: quercetin 6.8× IC50 (87% predicted inhibition), curcumin 8.3× IC50 (89% predicted inhibition) at standard supplement doses; EGCG operates via expression downregulation (not scored by this framework). VERY HIGH risk for quercetin and curcumin.

## Team

- **[Team](wiki/team.md)** — Brian Abent (Platform/Engineering, sole current member); potential collaborators: Rheinallt Jones PhD (Gut Microbiome), Lauren Collier-Hyams PhD (NF-κB/Pharma), Valerie Jones PhD (Innate Immune Safety). Active lab-access search for §1.9 Ward 1995 dual-cassette: Lauren Collier-Hyams (Emory, primary US lead) + global parallel options mapped in [`ward-1995-lab-access-global.md`](wiki/ward-1995-lab-access-global.md).

---

## Primary Research (long-form)

These are the long-form research documents that the shorter concept pages above are synthesized from. Living documents — the sweep daemon updates them as new findings land.

- **[Open Enzyme Vision](wiki/open-enzyme-vision.md)** — North Star: problem statement, insight, platform vision
- **[Enzyme Deficit Deep Dive](wiki/enzyme-deficit-deep-dive.md)** — Epidemiology and clinical burden of enzyme deficiencies
- **[Gout Deep Dive](wiki/gout-deep-dive.md)** — Uric acid metabolism, NLRP3, current therapies
- **[Engineered Yeast Uricase Proposal](wiki/engineered-yeast-uricase-proposal.md)** — *S. cerevisiae* uricase engineering
- **[Engineered Koji Protocol](wiki/engineered-koji-protocol.md)** — *A. oryzae* multi-enzyme fermentation
- **[NLRP3 Exploit Map](wiki/nlrp3-exploit-map.md)** — NLRP3 inhibition strategies (oridonin, disulfiram, peptides)
- **[Blood Barrier Exploits](wiki/blood-barrier-exploits.md)** — Intestinal barrier biology and optimization
- **[AI Bio Tools Playbook](wiki/ai-bio-tools-playbook.md)** — Computational strain design, optimization, and tool access (includes Codex Life Sciences plugin setup)
- **[Peptide Gout Addendum](wiki/peptide-gout-addendum.md)** — BPC-157, KPV, immunomodulatory peptides

---

## Cross-Analysis & Synthesis

- **[Synthesis (current)](wiki/synthesis.md)** — Cross-doc connections, contradictions, and proposed experiments. The sweep daemon prepends new findings here after each save. **This is the action queue — read it, then prune what you've acted on.**
- **[Concept Graph](wiki/GRAPH.md)** — Mermaid diagram of all concept relationships (produces / inhibits / activates / requires / synergizes / degrades)

### Engineering & Design (deep dives)

Detailed technical analyses for the uricase and koji engineering tracks.

**Uricase / *S. cerevisiae* track:**
- **[Uricase Variant Selection](wiki/uricase-variant-selection.md)** — Six variants evaluated; *A. flavus* primary, *A. globiformis* secondary. Rasburicase FDA precedent. Engineering roadmap.
- **[GI Survival Prediction](wiki/gi-survival-prediction.md)** — Transit model: 15–25% baseline survival → 40–50% with enteric coating + disulfide engineering.
- **[Protein Engineering Strategy](wiki/protein-engineering-strategy.md)** — Three mutation tiers (SB-1 / BAL-1 / OPT-1) for acid stability, protease resistance, and catalytic retention. Includes full mutation lookup table.
- **[Codon Optimization & Expression Cassette](wiki/codon-optimization-expression-cassette.md)** — *S. cerevisiae* cassette: TDH3p constitutive promoter, intracellular uricase, ADH1 terminator. Predicted yield 800–1,200 mg/L.

**Koji / *A. oryzae* track:**
- **[Koji Construct Design](wiki/koji-construct-design.md)** — *A. oryzae* uricase via amyB promoter (starch-inducible, 6–10× baseline). Expected 40–80 mg/g koji.
- **[Digestive Enzyme Optimization](wiki/digestive-enzyme-optimization.md)** — RIB40 strain; lipase 1,813–2,280 U/g koji (~50,000–60,000 FIP/g); rice bran optimal substrate; CRISPR tglA target. 10–15 g koji ≈ Creon equivalence. **New (Apr 2026):** Wild-type OTC benchmark = BoulderBio 40,000 FIP/cap (≈9–10k USP); n=1 PERT-timing self-experiment active — 2-cap protocol produced a clear decoupling of liquid-stool from pain against a long-stable baseline; split-dose (1+1) successful for >25 g fat meals. (Clinical n=1, uncontrolled; source: digestive-enzyme-optimization.md)
- **[Koji Home Fermentation](wiki/koji-home-fermentation.md)** — Wild-type small-batch protocol (koji-kin → koji rice → shio-koji / amazake). Pre-engineering baseline that the engineered strain must outperform; n=1 / household trial bed for the EPI co-target.
- **[NLRP3 Inhibitor Screen](wiki/nlrp3-inhibitor-screen.md)** — Top candidates: ursolic acid (8.59 g/L yeast), quercetin (930 mg/L), carnosine. Kojic acid native production (3–5 g/L) flagged as free bonus.

**Cross-platform:**
- **[Cross-Validation (Thesis Stress Test)](wiki/cross-validation.md)** — Risk matrix across all tracks; NLRP3 suppression confirmed; variant redundancy tested; ALLN-346 clinical bridge.

---

## Cross-Domain Relationships

**Uricase engineering loop:** uricase → *S. cerevisiae* / *A. oryzae* → gut-lumen-sink → NLRP3 inflammasome suppression → gout flare prevention

**Barrier repair loop:** BPC-157 + KPV → blood-barrier integrity → NLRP3 suppression via barrier signal transduction → oridonin / disulfiram (optional intensification)

**Metabolic synergy:** BHB (ketogenic diet or supplementation) → NLRP3 inhibition + probiotic fitness advantage → enzyme-producing strains outcompete pathogenic flora (SIBO prevention)

**Full-stack example (gout):** Engineered *A. oryzae* koji (uricase + NLRP3 inhibitors) + rice bran substrate + allopurinol adjunct → multi-target gout resolution (current platform thesis)

---

## Reference & Conventions

- **`wiki/`** — Living research documents. Updated as new findings land. Written in markdown with standard links (`[text](./path.md)`) so they render on GitHub.
- **`logs/`** — Sweep daemon log (`logs/sweep-log.md`). One entry per triggered sweep.
- **`reference/`** — Canonical read-only material (published papers, external reports, vendor data). The sweep daemon reads but never writes here.
- **Evidence levels** on every claim: `Clinical Trial`, `Animal Model`, `In Vitro`, or `Mechanistic Extrapolation`.
- **Inline provenance** on new content: `(source: <filename>)`.
- **Git is the revision history** — no inline changelogs; use `git log -p <file>` to see what changed.
