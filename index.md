# Open Enzyme

**Use red-teaming techniques to identify exploitable weaknesses in gout, and use creative engineering to exploit them.**

Open Enzyme is Phase 0 research and design. It maps gout as a system, creates falsifiable intervention tracks, and runs the cheapest experiments that can kill or redirect them. The intervention is not predetermined. See [Mission and operating principles](wiki/etc/open-enzyme-vision.md).

---

> **Researching a particular gout context?** Start with the [`gout-action-guide.md`](wiki/gout-action-guide.md) research decision guide, which maps contexts to mechanisms, evidence, and falsification gates. It is not a treatment protocol.
>
> **Looking for patient-facing information?** [**gout.care**](https://gout.care) is the patient-friendly companion site.

---

## Status

**Portfolio rule:** No chassis, payload, modality, or production model is the project. Koji is one active engineering track. If it fails, the result should narrow or kill that track and inform the next one. See [koji-track.md](wiki/koji-track.md) and [cross-validation.md](wiki/cross-validation.md).

**Shared versus local assumptions:** [H08 — Gut-Lumen Sink](wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md) affects oral luminal urate-degradation tracks. [H09 — Community Fermentation Reliability](wiki/hypotheses/H09-community-fermentation-reliability.md) affects one production option within the koji track. Neither is silently treated as a verdict on unrelated exploits.

**Active synthesis queue:** [`synthesis/queue/`](synthesis/queue/) contains unresolved reviewed findings. Closing an item means applying the action and deleting the queue file in the same commit; Git preserves the record. Architecture: [`synthesis/README.md`](synthesis/README.md).

**Wet-lab decision sequence and cheapest next experiments** (current synthesis; cost/ROI ordering applies within ungated work):

**Research-program front door:** [Gout Multihop Research Program](wiki/gout-multihop-research-program.md) connects the system model to computational experiments 044–046 and wet-lab protocols 1.33–1.43.

| # | Experiment | Cost | Weeks | Decides |
|---|---|---|---|---|
| **UOX-0 / MATERIALS** | **Matched UOX configuration build and characterization (§§1.1, 1.2, 1.5; exact external configurations where used)** | TBD | TBD | Supplies sequence-verified, localized, active configurations and matched controls before the physiological screen |
| **UOX-1 / PHYSIOLOGY** | **Configuration-level UOX × oxygen × peroxide (§1.33)** | TBD | TBD | Tests qualified configurations at the human-baseline substrate prior; topology can be nominated only within a controlled host comparison |
| 1 | Quercetin + ursolic acid + carnosine combo on MSU-stimulated macrophages (§1.17) | $1,500 | 4 | Whether to engineer one NLRP3 inhibitor or three |
| **KOJI GATE 1** | **Ward 1995 staged Lf-only → advanced UOX-only → dual-cassette feasibility (§1.9)** | $5,265–8,065 full path | 8–12 | Conditional multi-cassette gate: Stage A can parallel the UOX build/screen; Stage B consumes an exact §1.5-built, §1.33-advanced configuration; Stage C starts only after both single-cassette arms pass |
| **UOX-2 / SAFETY** | **Luminal urate antioxidant-loss × UOX-H₂O₂ (§1.36)** | TBD | TBD | Whether a §1.33-surviving configuration avoids epithelial injury when urate is depleted, including the indomethacin context; no efficacy inference |
| 2 | Carnosine co-expression in *A. oryzae* (§1.24) — optional third cassette | $1,500–2,500 | 4–6 | Whether this track-local carnosine module reaches its titer gate |
| LBP-1 | Engineering-toolkit, commercial-landscape, and FDA-LBP scans — see [`engineered-lbp-chassis.md`](wiki/engineered-lbp-chassis.md) Open Technical Questions | $0 | 1–2 | Whether a candidate organism supports controllable local payload activity and a viable delivery path |
| LBP-2 | LBP track Phase 2: comp-008 *F. prausnitzii* heterologous expression feasibility | $0 | 1 | Which candidate constructs are tractable in *F. prausnitzii* (uricase / lactoferrin / sCR1 / native BCoAT overexpression) |
| 1.23-T1 | Androgen × MSU × NLRP3 macrophage screen (§1.23 Tier 1, THP-1) — fills documented literature gap | $5–10K | 6–8 | Whether direct-androgen contribution to gout inflammation exists; gates Tiers 2–3 |
| THY-1 | Thymulin (+Zn²⁺) on MSU-primed **aged** macrophages — mature IL-1β + cleaved caspase-1, young-donor arm — see [`validation-experiments.md §1.44`](wiki/validation-experiments.md#144-thymulin--msu--nlrp3-in-aged-macrophages-thy-1--age-stratified-priming-to-flare-test) / [`thymulin.md`](wiki/thymulin.md) | $5–10K | 6–8 | Whether thymulin's NF-κB priming block translates to reduced crystal-driven IL-1β; graduates thymulin from CP1a extrapolation to gout-validated or kills it as priming-only |
| siRNA-1 | Kidney-tropic conjugate, clinical-landscape, and regulatory scans — see [`sirna-urat1-modality.md`](wiki/sirna-urat1-modality.md) Falsification Program | $0 | 1–2 | Whether any delivery class has credible selective proximal-tubule exposure |
| siRNA-2 | comp-009 URAT1 mRNA target-site selection (RNAfold + accessibility scoring) | $0 | 1 | Whether URAT1 mRNA has accessible, selective target sites before delivery work |
| TCM-1 | TCM track Phase 2: P2-1 lit scan (Si Miao San family + Smilax glabra + Bai Hu Jia Gui Zhi Tang) — **global multilingual sources by default** (ChiCTR, CNKI/WanFang, J-STAGE) — see [`tcm-modern-rigor-intersection.md`](wiki/tcm-modern-rigor-intersection.md) Open Follow-Ups | $0 | 1–2 | Whether classical TCM gout formulas have credible modern Chinese clinical signal vs. tradition-only |
| TCM-2 | TCM track Phase 2: comp-011 ChEMBL cross-check of 8 candidate TCM gout compounds (Smilax glabra, Rheum officinale, Plantago asiatica, Phellodendron, Polygonum cuspidatum, Cinnamomum cassia, Atractylodes, Astragalus) | $0 | 1 | Which TCM compounds have curated bioactivity at gout-relevant chokepoints at achievable gut-luminal concentrations |

See [wiki/validation-experiments.md](wiki/validation-experiments.md) for the full consolidated experiment list.

---

## Core Pathology & Targets

- **[Gout Pathophysiology](wiki/gout-pathophysiology.md)** — System map from purine metabolism through urate crystallization, NLRP3 activation, clinical interventions, and genomics.
- **[Uricase (Urate Oxidase)](wiki/uricase.md)** — Evolutionary loss, established systemic enzyme replacement, candidate luminal and local routes, and the reaction-site gates that separate them.
- **[NLRP3 Inflammasome](wiki/nlrp3-inflammasome.md)** — Seven chokepoints spanning complement priming, inflammasome assembly, cytokine signaling, resolution, and neutrophil recruitment.
- **[Digestive Enzymes & EPI](wiki/digestive-enzymes.md)** — Lipase, protease, and amylase deficits, replacement products, and wild-type koji as one candidate delivery format.
- **[SIBO](wiki/sibo.md)** — Brush-border damage, enzyme loss, NLRP3 involvement, and candidate barrier-repair mechanisms.
- **[Fructose Connection](wiki/fructose-connection.md)** — Fructokinase-driven ATP depletion, purine synthesis, GLUT9 transport, and KHK inhibition as a research target.
- **[Androgen-Urate Axis](wiki/androgen-urate-axis.md)** — Evidence and open questions linking sex hormones, URAT1, ABCG2, SHBG, and urate handling.
- **[PRPS / Purine Biosynthesis Chokepoint](wiki/prps-purine-biosynthesis-chokepoint.md)** — PRPS as a production-side chokepoint distinct from urate transport and xanthine-oxidase catabolism.
- **[Gout Genetic Variants — Unified Index](wiki/gout-genetic-variants.md)** — Cascade-stratified catalog of gout variants spanning transport, purine production, inflammation, pharmacogenetics, and comorbidity.
- **[Mechanical Flare Triggers — Open Questions](wiki/mechanical-flare-triggers.md)** — Competing mechanical and metabolic explanations for conversion of subclinical MSU crystal beds into inflammatory flares.
- **[Genotype-Informed Supplement Quantification Workflow](wiki/genotype-informed-supplement-workflow.md)** — Genotype-stratified research workflow with separate production, exposure, mechanism, and biomarker gates.

## Engineered Organisms & Platforms

- **[Saccharomyces cerevisiae](wiki/saccharomyces-cerevisiae.md)** — Candidate UOX chassis with direct active-expression evidence, matched build options, and unresolved reaction-site and safety gates.
- **[Aspergillus oryzae](wiki/aspergillus-oryzae.md)** — Koji biology, native products, transformation methods, and limits as a candidate expression chassis.
- **[Koji Multi-Payload Strain Hypothesis](wiki/koji-endgame-strain.md)** — Falsifiable multi-cassette koji configuration gated by single- and dual-cassette expression tests.
- **[Chaperone-Orthogonal Cassette Stacking](wiki/chaperone-orthogonal-stacking.md)** — Framework for testing whether payloads compete for or partition across fungal folding and secretion machinery.
- **[Engineered LBP Chassis](wiki/engineered-lbp-chassis.md)** — Independent local-delivery track using engineered colonic residents; direct Q141K rescue remains unvalidated.
- **[Duckweed Edible Biomanufacturing Chassis](wiki/duckweed-aquatic-chassis.md)** — Oral factory-and-delivery hypothesis for uricase and native urate-active flavonoids, gated by active enzyme yield, GI survival, exposure, and food-grade cultivation.
- **[siRNA / URAT1 Modality](wiki/sirna-urat1-modality.md)** — Sequence-specific URAT1 knockdown track gated by kidney-tropic delivery chemistry.
- **[TCM × Modern Rigor — Discovery-Engine Lens](wiki/tcm-modern-rigor-intersection.md)** — Multilingual discovery track that maps traditional formulas and species to modern gout chokepoints and falsification gates.
- **[Medicinal Mushroom Native-Compound Sources](wiki/medicinal-mushroom-complement-track.md)** — Fungal compounds and extracts evaluated by gout mechanism, preparation identity, exposure, immune direction, and falsification gate.
- **[Medicinal Mushroom Compound × Chokepoint Mapping (comp-014)](wiki/medicinal-mushroom-compound-mapping-computational.md)** — Fungal-natural-product mapping across target databases, literature, and gout chokepoints.
- **[Medicinal Mushroom Extract Characterization SOPs](wiki/medicinal-mushroom-extract-sops.md)** — Planned fractionation, quantification, functional-readout, and strain-authentication methods.
- **[Compounding Pharmacy Track](wiki/compounding-pharmacy-track.md)** — Formulation-and-delivery track for suitable off-patent small molecules, separate from biologic chassis work.
- **[Ward 1995 §1.9 Lab Access — Global Landscape](operations/ward-1995-lab-access.md)** — Candidate laboratories for the staged lactoferrin-only, UOX-only, and dual-cassette feasibility tests.
- **[Open Source Platform](wiki/etc/open-source-platform.md)** — GitHub strain library vision; software analogy; no patents; community validation; forkable strains

## Delivery & Barrier Biology

- **[Gut-Lumen Sink](wiki/gut-lumen-sink.md)** — Hypothesis that luminal UOX can consume transporter-delivered urate without the enzyme entering blood; human effect size, dose, topology, and safety remain open.
- **[ABCG2 Modulators](wiki/abcg2-modulators.md)** — Induction, inhibition, and Q141K-rescue hypotheses for the intestinal urate-export pathway.
- **[Blood Barrier](wiki/blood-barrier.md)** — Decision layer for matching a payload to luminal, local-tissue, or systemic exposure without presuming one route wins.

## Gene Therapy

- **[CRISPR Uricase](wiki/crispr-uricase.md)** — An ancestral UOX construct lowered intracellular urate in edited human hepatocyte cultures; in-vivo delivery, durability, reaction safety, and circulating-urate effects remain untested.

## Peptides & Compounds

- **[BPC-157](wiki/bpc-157.md)** — 15-amino-acid gastric peptide with indirect, evidence-limited relevance through gut-barrier hypotheses.
- **[KPV Tripeptide](wiki/kpv-peptide.md)** — α-MSH fragment with NF-κB/NLRP3 pathway evidence and unresolved gout exposure and selectivity.
- **[Thymulin](wiki/thymulin.md)** — Zinc-dependent thymic nonapeptide; CP1a NF-κB priming inhibition proven in aged macrophages + human PBMCs (Kanemaru 2026 *Nat Commun*), age-dependent; untested against MSU/crystal (priming only).
- **[Apelin-13](wiki/apelin-13.md)** — Exact-form-sensitive APLNR/APJ agonist with one hyperuricemic-rat/uric-acid adipocyte study and separate non-gout NLRP3 evidence; no MSU or gout experiment.
- **[BHB / Ketones](wiki/bhb-ketones.md)** — Evidence and uncertainties for ketone-mediated effects across three NLRP3 chokepoints.
- **[Oridonin](wiki/oridonin.md)** — Natural NLRP3 inhibitor; covalent NACHT domain Cys279 binding; traditional medicine origin
- **[Disulfiram](wiki/disulfiram.md)** — Gasdermin D blocker (Antabuse); repurposed drug; CP6b in v1.2 NLRP3 map
- **[Colchicine](wiki/colchicine.md)** — CP2/CP3 inflammasome effects, gout and cardiovascular evidence, and the narrow therapeutic and interaction window.
- **[EGCG](wiki/egcg.md)** — Green tea catechin; 20S proteasome 86 nM (ChEMBL); unifies CP1a (IκBα) + CP4 (caspase-1) + CP5 (IL-1β) via single mechanism
- **[Theaflavins](wiki/theaflavins.md)** — Black-tea polyphenols with animal evidence across inflammasome assembly and renal urate transport.
- **[Houttuynia cordata polysaccharides](wiki/houttuynia-cordata.md)** — Exact-material CP0 complement and CP1 macrophage hypotheses with likely intestinal delivery, structure-dependent directionality, and separate falsification gates.
- **[Lactoferrin](wiki/lactoferrin.md)** — Single protein, four-chokepoint coverage (CP1a/CP4/CP6b/CP5b); fermentable in *A. oryzae* (Ward 1992 25 mg/L → Ward 1995 >2 g/L *A. awamori*); Year 2-3 engineering target
- **[Zileuton](wiki/zileuton.md)** — FDA-approved asthma 5-LOX inhibitor with direct CP6a target engagement, liver-monitoring constraints, and no gout efficacy trial.

## Strategy & Practice

- **[Gout Action Guide](wiki/gout-action-guide.md)** — Situation-first research decision guide mapping contexts to mechanisms, evidence, and falsification gates; not a treatment protocol.
- **[Gout Clinical Pipeline](wiki/gout-clinical-pipeline.md)** — Clinical-development status for oral uricase, NLRP3 inhibitors, IL-1 blockade, and systemic uricase programs.
- **[Supplements Stack](wiki/supplements-stack.md)** — Compound catalog covering mechanisms, exposures, contraindications, interactions, and stack-level antagonisms.
- **[Purine-Degrading Bacteria (PDB)](wiki/purine-degrading-bacteria.md)** — anaerobic microbial urate disposal with engineered-EcN animal precedent. Terminal products are organism-specific: full-pathway anaerobes have isotope-resolved acetate/butyrate evidence, but CBT2.0 carbon fate is unresolved. Any downstream SCFA/ABCG2/NLRP3 benefit is therefore conditional, not part of the demonstrated CBT2.0 result.
- **[Gout Kill Chain — Delivery Route Analysis](wiki/gout-kill-chain-delivery-routes.md)** — Route-by-route pharmacokinetic analysis across the gout kill chain, including local, systemic, and gut-luminal gaps.
- **[GSDMD Pore Self-Delivery Paradox](wiki/gsdmd-pore-delivery-paradox.md)** — Hypothesis that GSDMD pores could admit normally impermeant inhibitors, with timing and selectivity unresolved.
- **[Complement C5a in Gout](wiki/complement-c5a-gout.md)** — Evidence that MSU activates complement and that C5a can prime NLRP3, with direct and upstream intervention hypotheses.
- **[TNFSF14 / LIGHT in Gout](wiki/tnfsf14-gout-target.md)** — CP1a: Second-highest gout-flare biomarker; LIGHT amplifies NF-κB; EGCG and DHA as natural moderators; CERC-002 mAb precedent
- **[SPM Resolution Pathway](wiki/spm-resolution-pathway.md)** — CP5b: RvD1/MaR1 direct MSU gout animal model evidence; ALX/FPR2 agonism; aspirin-triggered resolvins
- **[Self-Experiment Protocol](wiki/self-experiment-protocol.md)** — N-of-1 monitoring framework with biomarker, diary, attribution, and halt-criteria controls.
- **[Enzyme Quantification Protocol](wiki/enzyme-quantification-protocol.md)** — Tiered assays for amylase, protease, and lipase activity from kitchen-scale through outsourced testing.
- **[Medicinal Mushroom Extract SOPs](wiki/medicinal-mushroom-extract-sops.md)** — Planned characterization methods for mushroom extracts, active compounds, functional readouts, and strain identity.
- **[Open Questions](wiki/open-questions.md)** — Cross-wiki index of unresolved scientific questions organized by chokepoint and mechanism.
- **[Modality × Target Matrix](wiki/modality-chokepoint-matrix.md)** — Crosses intervention modalities with anatomical and cellular targets to expose underexplored combinations.
- **[Delivery Route × Compound Class Matrix](wiki/delivery-route-matrix.md)** — Crosses compound classes with enteral, systemic, and local delivery routes to expose route-specific gaps.
- **[Chassis-Pending Interventions](wiki/chassis-pending-interventions.md)** — Interventions that hit gout chokepoints but still have an open engineering, delivery, or production question. Chassis selection follows exploit selection; it does not define project scope.
- **[Carnosine](wiki/carnosine.md)** — Dual-phenotype (hyperuricemia + NLRP3) in rats; unique in the stack for addressing both UA and inflammation in a single compound
- **[ChEMBL Cross-Check](wiki/etc/chembl-cross-check.md)** — Standing cross-reference of candidate compounds against curated bioactivity records.
- **[Cannabinoids & Terpenes](wiki/cannabinoids-terpenes.md)** — CBD, CBG, CBC, THCV, beta-caryophyllene, myrcene: NLRP3 mechanisms, gout evidence, EPI applications; beta-caryophyllene has direct MSU gout animal model data
- **[Validation Experiments](wiki/validation-experiments.md)** — Proposed in vitro, animal, observational, and human-method studies with explicit decision gates.
- **[Bio-AI Tools](wiki/etc/bio-ai-tools.md)** — Protein-design, docking, omics, and literature tools mapped to Open Enzyme research workflows.
- **[Paperclip (GXL)](wiki/etc/paperclip-deep-dive.md)** — Literature-search tool whose synthesis output requires primary-source verification before use.
- **[Manual Literature Mining Protocol](wiki/etc/manual-literature-mining.md)** — Primary-source verification discipline for literature search, extraction, translation, and citation.
- **[Linter Design (Falsification + Document Lint)](wiki/linter-design.md)** — Architecture for document-quality checks and hypothesis-specific falsification review.
- **[Autonomous AI Screening Methodology](wiki/etc/autonomous-screening-methodology.md)** — Search-space, composite-scoring, verification, and human-handoff lessons from autonomous screening systems.
- **[Hypotheses Index](wiki/hypotheses/README.md)** — Falsification cards for committed claims, their evidence, kill criteria, and open tests.
- **[Computational Experiments](wiki/computational-experiments.md)** — Tracking index for current and invalidated COMPs, with verdicts and supersession state.
- **[Cordycepin Cassette Metabolic Burden (comp-023)](wiki/cordycepin-cassette-burden-computational.md)** — **GREEN:** FBA finds negligible cytosolic burden, with ER folding assessed separately.
- **[Disulfiram Dose Modeling (comp-027)](wiki/disulfiram-dose-modeling-computational.md)** — **Hypothesis generator:** one boundary-dependent GREEN point does not establish a dose window.
- **[Dual-Chassis EcN PDB + Uricase (comp-031)](wiki/dual-chassis-ecn-pdb-uricase-computational.md)** — **INVALIDATED:** no efficacy, competition, additivity, genotype, or topology conclusion survives.
- **[Inhaled mRNA-IL-1RA Pulse Therapy (comp-033)](wiki/inhaled-mrna-il1ra-pulse-computational.md)** — **RED:** modeled single-dose exposure reaches 2% of the anakinra benchmark.
- **[Repeat-Dose Inhaled mRNA-IL-1RA PK/PD (comp-036)](wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md)** — **YELLOW:** partial receptor occupancy remains gated by translation efficiency and binding affinity.
- **[Lactoferrin Inter-Lobe Linker Redesign (comp-034)](wiki/lactoferrin-linker-redesign-computational.md)** — ProteinMPNN found three strict 5-of-5 candidates; `NEEEQQQEEEQ` leads the wet-lab plate but remains a computational hypothesis.
- **[Intra-Articular Uricase H₂O₂ Reaction-Diffusion (comp-035)](wiki/intra-articular-uricase-h2o2-reaction-diffusion-computational.md)** — **Phase-0 prior, not decision-grade:** modeled catalase control still requires Amplex Red and §§1.33/1.36 validation.
- **[Combined CP0 Systems Model (comp-029)](wiki/combined-cp0-systems-model-computational.md)** — **YELLOW:** the combination adds little over the better singleton and remains accessibility-gated.
- **[C1-INH Protease Stability + Glycosylation in EcN (comp-037)](wiki/c1-inh-protease-stability-ecn-computational.md)** — **MODERATE / glycosylation GREEN:** luminal C1-INH remains kinetic-competition gated.
- **[CFH-Dependence Mechanism-Dissociation of CP0 Candidates (comp-039)](wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md)** — Four upstream CP0 candidates classify as CFH-independent under the stated mechanism tests.
- **[KPV GSDMD Pore Influx (comp-042)](wiki/kpv-gsdmd-pore-influx-computational.md)** — **YELLOW:** pore flux survives, but KPV selectivity is falsified.
- **[DAF+Lactoferrin EcN Folding Feasibility (comp-043)](wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md)** — C1-INH viable, DAF provisional, and lactoferrin not viable in the modeled EcN folding regime.
- **[Gut-Lumen Uricase Physiological-Regime Audit (comp-044)](wiki/gut-lumen-uricase-physiologic-regime-computational.md)** — COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics. The audit supplies no replacement dose, ΔSUA, genotype order, regime, efficacy model, topology/chassis, production target, or safety conclusion.
- **[Uricase Topology × Oxygen × Peroxide (comp-045)](wiki/uricase-topology-oxygen-peroxide-design-computational.md)** — **YELLOW:** no topology is eliminated; the factorial wet-lab test remains decisive.
- **[Staged Purine Sink Mass Balance (comp-046)](wiki/staged-purine-sink-mass-balance-computational.md)** — Two separate conditional models; neither grid is probabilistic or establishes joint efficacy.
- **[ABCG2 Q141K Chaperone Re-screen (comp-047)](wiki/abcg2-q141k-chaperone-rescreen-computational.md)** — **INCONCLUSIVE:** failed positive controls show rigid docking cannot discriminate chaperones.
- **[Cassette Compatibility — Dual-Cassette Koji Configuration (comp-010)](wiki/cassette-compatibility-computational.md)** — **LOW design risk:** two sequence-level uncertainties remain for the dual-cassette test.
- **[C. utilis Uricase Cassette Compatibility (comp-011)](wiki/c-utilis-uricase-cassette-compatibility-computational.md)** — **MODERATE design risk:** variant comparison is conditional on topology selection.
- **[Uricase Cassette Ranking, ClockBase-Style (comp-022)](wiki/uricase-cassette-ranking-computational.md)** — Candidate-level cassette priors that do not decide secretion topology.
- **[TCM Gout Compound Triage (comp-013)](wiki/tcm-gout-compound-triage-computational.md)** — Source/compound/target evidence inventory survives; the viability ranking is invalid because it did not preserve target-effect polarity and inherited nominal gut-concentration/IC50 occupancy.
- **[Medicinal Mushroom Compound Mapping (comp-014)](wiki/medicinal-mushroom-compound-mapping-computational.md)** — Fungal compound-to-chokepoint map with ADA and PINK1/mitophagy as open candidate nodes.
- **[DAF/CD55 SCR1-4 Truncated Protease Stability (comp-012)](wiki/daf-cd55-scr14-truncated-computational.md)** — **LOW protease risk:** the truncated construct remains gated by three wet-lab unknowns.
- **[DAF SCR1-4 Cassette Ranking (comp-030)](wiki/daf-cd55-scr14-cassette-ranking-computational.md)** — Corroborates the direct-secretion baseline and rejects GlaA-KEX2 for this target.
- **[Uricase Protease-Site Proxy (comp-001)](wiki/uricase-protease-stability-computational.md)** — P1/P1' sequence mapping plus AlphaFold pLDDT supplies a structural-confidence prior; it does not measure solvent exposure, protease survival, retained activity, or fermentation performance. The shio-koji assay remains the gate.
- **[Lactoferrin Protease Stability (comp-005)](wiki/lactoferrin-protease-stability-computational.md)** — HIGH (full sequence, signal-peptide-driven) / MODERATE (mature protein); lactoferrin arm of §1.10 remains a feasibility gate.
- **[DAF/CD55 Protease Stability (comp-006)](wiki/daf-cd55-protease-stability-computational.md)** — HIGH verdict for soluble ectodomain (aa 35–353); stalk-contingent (Ser/Thr stalk aa 286–353 drives all exposed sites); SCR1-4 core contributes zero exposed sites; stalk-truncated construct (aa 35–285) is the logical follow-up.
- **[Food-Grade HDAC Inhibitor Screen (comp-007)](wiki/food-grade-hdaci-screen-computational.md)** — Stage 1 in silico screen: butyrate rank 1 (composite 0.374, HIGH confidence, 167× HDAC6 selectivity); sulforaphane rank 2 (LOW confidence); PEITC rank 3. Advances to Stage 2 Caco-2/HepG2 paired HDAC activity assay.
- **[Supplement–ABCG2 Assay-Evidence Audit (comp-004)](wiki/supplement-abcg2-antagonism-computational.md)** — Quantitative occupancy/risk verdict invalid; three cited interaction records route quercetin, curcumin, and EGCG to direct intestinal ABCG2-attributed urate-flux testing.

## Practitioner Toolkit

How a single researcher (institutional or independent) works rigorously at kitchen-table or personal scale. Three-tier structure under [`practitioner-toolkit.md`](wiki/etc/practitioner-toolkit.md) umbrella.

**Self-Experiments (n=1):**
- **[Self-Experiment Protocol](wiki/self-experiment-protocol.md)** — Brian's biomarker monitoring framework: blood panels, 16S stool, daily diary, red-flag halt criteria; specialty biomarkers (C3/C4/CH50/C5a CP0; urinary LTE4 CP6a)
- **[Personal Genome Protocol](wiki/personal-genome-protocol.md)** — Pharmacogenomic query design, privacy tradeoffs, and strain-QC uses for small-scale sequencing.
- **PERT-timing self-experiment (in progress)** — Documented inline in [`digestive-enzyme-optimization.md`](wiki/digestive-enzyme-optimization.md).

**DIY Capability Builds:**
- **[Koji Home Fermentation](wiki/koji-home-fermentation.md)** — wild-type small-batch protocol (koji-kin → koji rice → shio-koji / amazake); pre-engineering baseline + n=1 trial bed for EPI co-target
- **[Enzyme Quantification Protocol](wiki/enzyme-quantification-protocol.md)** — tiered methods (kitchen → smartphone colorimetry → community-college bench → outsourced contract assay)
- **Low-Cost Liquid-Handling Automation / Picolab Prior Art** — Small-scale infrastructure for repeatable serial dilution and colorimetric assay setup; see [`practitioner-toolkit.md`](wiki/etc/practitioner-toolkit.md) and [`quantification-ladder.md`](wiki/quantification-ladder.md).
- Sequencing capability (sub-bucket of Personal Genome Protocol) — MinION + Dorado + Flye / Clair3 pipeline

**Rigor Disciplines (cross-cutting; pages live in topical homes, listed in Strategy & Practice above):**
- [`manual-literature-mining.md`](wiki/etc/manual-literature-mining.md) — five-rule LLM literature discipline
- [`chembl-cross-check.md`](wiki/etc/chembl-cross-check.md) — quarterly bioactivity cross-reference
- [`linter-design.md`](wiki/linter-design.md) — falsification + document lint architecture
- [`autonomous-screening-methodology.md`](wiki/etc/autonomous-screening-methodology.md) — ClockBase Agent prior-art methodology for comp-NNN
- [`tcm-modern-rigor-intersection.md`](wiki/tcm-modern-rigor-intersection.md) — six-rule traditional-medicine evidence-leveling
- [`quantification-ladder.md`](wiki/quantification-ladder.md) — Four-tier framework from kitchen measurement through outsourced assays.
- [`cross-validation.md`](wiki/cross-validation.md) — thesis stress-test discipline

## Team

- **[Team](wiki/etc/team.md)** — Current team, open collaborator roles, and linked laboratory-access paths.

---

## Primary Research (long-form)

Long-form research documents supporting the concept pages above.

- **[Open Enzyme Vision](wiki/etc/open-enzyme-vision.md)** — North Star: problem statement, insight, platform vision
- **[Enzyme Deficit Deep Dive](wiki/enzyme-deficit-deep-dive.md)** — Epidemiology and clinical burden of enzyme deficiencies
- **[Gout Deep Dive](wiki/gout-deep-dive.md)** — Uric acid metabolism, NLRP3, current therapies
- **[Engineered Yeast UOX Research Plan](wiki/engineered-yeast-uricase-proposal.md)** — Matched yeast builds, reaction-site measurements, safety gates, and stop rules.
- **[Engineered Koji UOX Plan](wiki/engineered-koji-protocol.md)** — Matched *A. oryzae* builds, process measurements, and falsification gates; no chassis or product precommitment.
- **[NLRP3 Exploit Map](wiki/nlrp3-exploit-map.md)** — NLRP3 inhibition strategies (oridonin, disulfiram, peptides)
- **[Systemic UOX Delivery Attack Surface](wiki/blood-barrier-exploits.md)** — Route-specific hypotheses and gates for recovering active UOX in blood or a defined tissue compartment; evidence does not transfer from the luminal route.
- **[AI Bio Tools Playbook](wiki/etc/ai-bio-tools-playbook.md)** — Computational strain design, optimization, and tool access (includes Codex Life Sciences plugin setup and Hugging Science triage for open datasets/models)
- **[Ginkgo Cloud Lab Evaluation](wiki/ginkgo-cloud-lab-evaluation.md)** — Evaluation of cell-free and strain-engineering services against specific wet-lab gates.
- **[Peptide Gout Addendum](wiki/peptide-gout-addendum.md)** — BPC-157, KPV, immunomodulatory peptides

---

## Cross-Analysis & Synthesis

- **[Synthesis queue](synthesis/README.md)** — Unresolved reviewed connections, contradictions, and proposed experiments.

### Engineering & Design (deep dives)

Detailed technical analyses for the uricase, yeast, and koji engineering tracks.

**Uricase / *S. cerevisiae* track:**
- **[Uricase Variant Selection](wiki/uricase-variant-selection.md)** — Matched candidate screen in which sequence, topology, reaction site, and process are interacting variables; no universal parent-enzyme ranking.
- **[GI Survival Prediction](wiki/gi-survival-prediction.md)** — Empirical gate for activity retained across processing, gastric/intestinal transit, topology, and formulation; no validated survival fraction or oral dose.
- **[Protein Engineering Strategy](wiki/protein-engineering-strategy.md)** — Matched wild-type, single-change, and combination screen for retained active UOX; no predicted survival or dose.
- **[Yeast UOX Expression Cassette](wiki/codon-optimization-expression-cassette.md)** — Sequence-controlled build matrix; expression and topology remain measured gates.

**Koji / *A. oryzae* track:**
- **[Koji UOX Construct Screen](wiki/koji-construct-design.md)** — Matched intracellular, secreted, displayed, and cell-free configurations; no preselected winner.
- **[Digestive Enzyme Optimization](wiki/digestive-enzyme-optimization.md)** — Koji enzyme-production benchmarks, substrate choices, engineering targets, and an uncontrolled PERT-timing observation.
- **[Koji Home Fermentation](wiki/koji-home-fermentation.md)** — Separate wild-type small-batch process; engineered-strain work requires controlled containment and release criteria.

**Compound screening:**
- **[NLRP3 Inhibitor Screen](wiki/nlrp3-inhibitor-screen.md)** — Candidate comparison by gout-relevant mechanism, evidence, exposure, safety, and discriminating experiments; production routes are considered only when biologically relevant.

**Cross-platform:**
- **[Cross-Validation (Thesis Stress Test)](wiki/cross-validation.md)** — Portfolio-level stress tests and scope boundaries across independently falsifiable tracks; current evidence lives in the linked source pages.

---

## Cross-Domain Relationships

**Luminal UOX dependency:** candidate sequence and chassis → verified active construct → physiological topology × oxygen × peroxide test (§1.33) → urate-antioxidant-loss and epithelial-safety test (§1.36) → later compartmental and translational work. Expression, protein mass, or a favorable high-substrate assay cannot skip those gates.

**Other UOX routes:** local-tissue and systemic delivery have separate active-enzyme, peroxide, PK, immunogenicity, and tissue-safety gates. A result from the luminal route does not validate or invalidate those routes.

**Portfolio boundary:** urate production, renal and intestinal transport, inflammatory signaling, local delivery, and other disposal mechanisms remain independent exploit surfaces. A failed UOX sequence, topology, chassis, or route narrows only the claim it tested.

---

## Reference & Conventions

- **`wiki/`** — Living research documents written in markdown with standard links (`[text](./path.md)`).
- **`logs/`** — Compact automation state.
- **`reference/`** — Read-only published papers, external reports, vendor data, and generated source material.
- **Evidence levels** on every claim: `Clinical Trial`, `Animal Model`, `In Vitro`, or `Mechanistic Extrapolation`.
- **Research Conjecture** is not an evidence level. It marks a grounded but untested connection, separates sourced premises from the novel leap, and names the observation that could advance or kill it.
- **Inline provenance** on factual claims: `(source: <filename>)`.
- **Git is the revision history** — no inline changelogs; use `git log -p <file>` to see what changed.
