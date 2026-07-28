---
title: "Unresolved Delivery and Implementation Constraints"
date: 2026-05-15
tags:
  - delivery-constraints
  - first-principles
  - exploration
  - discovery-engine
  - multi-modal
related:
  - modality-chokepoint-matrix.md
  - delivery-route-matrix.md
  - gout-kill-chain-delivery-routes.md
  - etc/open-enzyme-vision.md
  - etc/open-source-platform.md
  - purine-degrading-bacteria.md
  - sirna-urat1-modality.md
  - engineered-lbp-chassis.md
  - gsdmd-pore-delivery-paradox.md
  - compounding-pharmacy-track.md
sources:
  - "Open Enzyme mission and track-portfolio operating principles"
  - "Umbrella CLAUDE.md §Curiosity and First-Principles Framing"
status: published
---

# Unresolved Delivery and Implementation Constraints

This index tracks gout-relevant intervention hypotheses whose biological fit can be evaluated separately from their delivery, manufacturing, formulation, or regulatory route.

Inclusion does not mean that a mechanism is validated or that an intervention is promising. Each entry must state its evidence level, unresolved biological assumptions, delivery constraints, and cheapest discriminating test. An accessible production route cannot rescue a weak mechanism; an awkward delivery route should not hide a strong one.

## Selection rule

Rank candidate weaknesses by gout relevance, evidence, target exposure, safety, and falsifiability. Evaluate sourcing and delivery only after those gates. Koji, live biotherapeutics, purified proteins, small molecules, RNA, devices, and no-chassis interventions are implementation options rather than discovery filters.

An entry remains provisional until its mechanism, relevant exposure, and delivery route survive their respective gates.

## How to read this page

Each entry has a fixed shape:

- **Intervention** — what the intervention does, mechanistically
- **Chokepoint(s) hit** — which OE chokepoint(s) the intervention targets, with cross-reference
- **Evidence level** — Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation
- **Delivery / implementation constraint** — the specific formulation, manufacturing, tissue-access, regulatory, or safety problem
- **Candidate implementation routes** — options, not commitments or ranking criteria
- **Cheapest discriminating test** — the next step that can falsify a biological or delivery assumption without committing to a platform
- **Cross-reference** — the linked evidence page(s) where this intervention is treated in mechanism depth

The linked mechanism dossier supplies the supporting evidence; each entry here states the unresolved delivery question and the experiment that resolves it.

---

## Current intervention and delivery questions

### 1. Purine-degrading bacteria (PDB) restoration / engineered PDB pathway expression

**Intervention.** The 2,8-dioxopurine bacterial gene cluster degrades urate anaerobically. Full-pathway anaerobes have acetate/butyrate isotope-tracing precedent, but engineered EcN CBT2.0's terminal carbon fate is unresolved. Downstream ABCG2/NLRP3 and Q141K-rescue claims are therefore conditional on [validation experiment 1.37](./validation-experiments.md#137-cbt20-carbon-fate-and-pdb-self-niche-test) and direct butyrate trafficking/flux testing; Basseville 2012 did not test PDB-derived butyrate.

**Chokepoint(s) hit.** Demonstrated target: CP6 urate degradation. Conditional extensions, only if the selected organism produces butyrate at sufficient epithelial exposure, are CP2/NLRP3 dampening and wild-type ABCG2 induction through PPARγ. Direct butyrate rescue of Q141K trafficking is a separate unvalidated hypothesis. See [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md).

**Evidence level.** Animal Model (CBT2.0 engineered EcN lowered plasma urate in hyperuricemic mice — Li et al. 2025, PMID 41070194); Human Retrospective Cohort and Human Observational evidence supports an association between microbiome perturbation and urate handling, not a quantitative treatment effect in gout. Exact cohort results and provenance remain on [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md). Translating any of these records to serum-urate change in a typical patient is a **Mechanistic Extrapolation**.

**Delivery / implementation constraint.** DOPDH requires SelD selenophosphate synthase, and the pathway is obligate anaerobic. The eight-enzyme cluster therefore requires a compatible organism and manufacturing environment.

**Candidate implementation routes.** Multiple, all open:
1. **Engineered *E. coli* Nissle 1917 expressing the full PDB cluster** (CBT2.0 precedent in Li 2025) — facultative anaerobe, EcN safety / probiotic record, already used in PULSE uricase work, native SelD present
2. **Defined-strain anaerobic probiotic** (*Clostridium sporogenes*, *Lacrimispora saccharolytica*, *Enterocloster bolteae*) — naturally express the cluster but oxygen-sensitive manufacturing is a barrier
3. **FMT from PDB-rich donors** — case reports exist for gout FMT; regulatory pathway exists for some indications
4. **Prebiotic enrichment** — a non-engineered route to test whether enriching PDB-associated taxa changes pathway flux; efficacy and attribution remain unresolved
5. **Selenium-defined pathway testing** — DOPDH cofactor dependence makes selenium status an experimental variable, not yet a supported intervention

**Cheapest first move.** In a controlled culture or gnotobiotic system, measure pathway activity across selenium-defined media and identify terminal carbon products by isotope tracing. Test the separate *Alistipes indistinctus* / hippuric-acid → ABCG2 hypothesis as its own controlled perturbation; dietary exposure or an n=1 observation cannot establish that mechanism.

**Cross-reference.** [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) (mechanism), [`abcg2-modulators.md`](./abcg2-modulators.md) (PPARγ/ABCG2 axis), [`gut-lumen-sink.md`](./gut-lumen-sink.md) (PULSE context for EcN chassis option), [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) (LBP framework for anaerobic options).

---

### 2. Kidney-tropic siRNA against URAT1 mRNA

**Intervention.** Synthetic siRNA intended to reduce URAT1 mRNA in renal proximal-tubule cells through a kidney-targeted delivery route. An oligonucleotide would not generate benzbromarone's reactive small-molecule metabolites, but no cleaner overall safety profile is established: guide off-targets, innate-immune activation, formulation toxicity, unintended biodistribution, excessive uricosuria, renal hypouricemia, reversibility, and dosing interval remain open. Approved liver-targeted siRNAs provide a modality precedent, not evidence for kidney delivery or quarterly URAT1 dosing.

**Chokepoint(s) hit.** Renal URAT1 reabsorption — the single largest reabsorption step in the renal urate handling chain. GLUT9 is a parallel target. Renal urate disposal sits on a different mechanism axis from gut-lumen disposal (the koji thesis); the two are complementary, not substitutional. See [`sirna-urat1-modality.md`](./sirna-urat1-modality.md).

**Evidence level.** Mechanistic Extrapolation for gout specifically. Clinical Trial precedent for the delivery class (inclisiran, patisiran approved for non-renal targets). No clinical program for URAT1 specifically as of 2026-05-15.

**Delivery / implementation constraint.** Kidney-tropic RNA delivery, formulation, and target-cell uptake remain the central implementation problems.

**Candidate implementation route.** Synthetic siRNA plus a kidney-tropic conjugate, with commercial manufacturing and a clinical development partner.

**Cheapest first move.** [COMP-048](./etc/experiments/comp-048-human-proximal-tubule-delivery-handle-screen/) screens for a selective, plausibly internalizing surface handle on SLC22A12-positive human proximal-tubule cells. Guide design is downstream: [COMP-009 is invalid](./urat1-sirna-target-site-selection-computational.md) and supplies no candidate, rank, accessibility, specificity, or tractability verdict.

**Cross-reference.** [`sirna-urat1-modality.md`](./sirna-urat1-modality.md), [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (Renal compartment row), [`delivery-route-matrix.md`](./delivery-route-matrix.md) (RNA platforms × SC cell).

---

### 3. Engineered LBP (obligate anaerobe) chassis — *F. prausnitzii*, *Akkermansia*, *Bacteroides*

**Intervention.** Live biotherapeutic products engineered from gut-native obligate anaerobes. Payload-dependent possibilities include *F. prausnitzii* for local butyrate (supported WT-ABCG2 induction plus an unvalidated Q141K-rescue extension), *Akkermansia muciniphila* for mucus-layer repair, and *Bacteroides* for broader metabolic engineering. Durable human colonization, product titer, epithelial exposure, and clinical effect remain development gates.

**Chokepoint(s) hit.** Depends on engineered payload. Gut ABCG2 induction (via SCFA), gut barrier repair (CP1 LPS / TNFα leak), gut microbiome shaping (community-level). See [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md).

**Evidence level.** Mechanistic Extrapolation + Animal Model precedent (Sonnenburg lab Bacteroides editing toolkit; Pendulum probiotic commercial *Akkermansia*-containing product). LBP regulatory framework (FDA 2018 guidance) defined; clinical programs exist for other indications.

**Delivery / implementation constraint.** Obligate anaerobic manufacturing, stabilization, colonization, epithelial exposure, and the Live Biotherapeutic Product regulatory framework.

**Candidate implementation routes.** *F. prausnitzii*, *Akkermansia muciniphila*, or *Bacteroides*, with commercial manufacturing, distribution, and cold chain.

**Cheapest first move.** LBP track Phase 2 lit scans (engineering toolkit + commercial landscape + FDA LBP regulatory path) — queued in [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md). $0 cost, ~1–2 weeks via subagent.

**Cross-reference.** [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) owns the detailed scope.

---

### 4. Inhaled mRNA-IL-1RA pulse therapy for acute gout flare

**Intervention.** Lipid nanoparticle-formulated mRNA encoding IL-1 receptor antagonist, delivered by inhalation as a transient-expression hypothesis. Pulmonary expression, systemic exposure, receptor occupancy, efficacy, and repeat-dose safety are all unestablished.

**Chokepoint(s) hit.** CP5a (IL-1β receptor blockade). Companion target for the existing SC anakinra / canakinumab options. See [`modality-chokepoint-matrix.md` §"Open exploration questions" #5](./modality-chokepoint-matrix.md).

**Evidence level.** Mechanistic Extrapolation. No clinical program in any indication uses mRNA-IL-1RA for flare-window therapy. Adjacent precedents (mRNA vaccines IM, mRNA pulmonary research) establish the chassis feasibility.

**Delivery / implementation constraint.** Pulmonary LNP delivery, repeat-dose tolerability, exposure duration, and receptor occupancy remain unresolved.

**Candidate implementation route.** Synthetic mRNA plus LNP and an inhaler device; commercial manufacturing and a clinical partner are required.

**Cheapest first move.** Mechanism + delivery feasibility lit scan: "mRNA-IL-1RA pulse" + "pulmonary LNP for acute inflammatory indications" — $0, subagent task. Result: either confirms novel territory + bounds the chassis question, or surfaces an existing program OE didn't know about.

**Computational gate — [comp-033](./computational-experiments.md) RED single-dose + [comp-036](./computational-experiments.md) YELLOW repeat-dose (2026-05-16):** the single-dose model's central Cmax was 0.025 µg/mL versus a 1.5 µg/mL anakinra benchmark, a ratio of 1.67%. The repeat-dose model evaluated a different endpoint: mean receptor occupancy and the fraction of a 72-hour window above an 80% threshold. Its QD central mean occupancy of 0.66 can coexist with zero time above the stricter 80% threshold; these are not interchangeable statistics. No tested regimen cleared the model's GREEN criterion. The result remains dominated by assumed IL-1Ra/IL-1R1 affinity, pulmonary translation efficiency, and dose. Measure integrated protein production after inhaled mRNA-LNP and a modern matched-condition binding affinity before using the model for regimen or economic claims. Full analyses: [`inhaled-mrna-il1ra-pulse-computational.md`](./inhaled-mrna-il1ra-pulse-computational.md) (comp-033) and [`repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md`](./repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md) (comp-036).

**Research comparison.** The relevant test is not an assumed clinical substitution for prednisone or anakinra. It is whether the measured exposure and receptor occupancy produce a reproducible flare-model effect with acceptable repeat-dose pulmonary safety. The two wet-lab measurements above gate any clinical or economic comparison.

**IL-1Ra versus an anti-IL-1β monoclonal as an mRNA payload:** the alternative cassette would encode an anti-IL-1β antibody. IL-1Ra has four candidate design advantages:

1. **Mechanism breadth.** IL-1Ra blocks both IL-1α AND IL-1β at the single IL-1R1 receptor — broader pathway coverage. Anti-IL-1β monoclonals only neutralize IL-1β. For gout the difference is small (IL-1β is the dominant ligand), but for COPD / ARDS / IPF the cross-indications, IL-1α also drives sterile inflammation, so the broader-mechanism payload is a feature, not a quirk.
2. **Protein size + structure.** IL-1Ra is a small, non-glycosylated single-chain payload; an antibody requires paired-chain assembly and appropriate Fc glycosylation. That makes IL-1Ra a reasonable initial engineering candidate, but comp-033's translation-efficiency sensitivity does not itself prove a payload-size advantage or a 10× expression gain.
3. **Immunogenicity.** Human IL-1Ra is endogenous, but an encoded or formulated product can still generate innate, delivery-system, impurity, or anti-drug responses. Immunogenicity must be measured rather than inferred to be zero.
4. **Cleanness of mechanism.** IL-1Ra is purely competitive antagonism — no agonism, no ADCC, no CDC, no off-target effector function. Antibodies have Fc-mediated effector functions (ADCC / CDC / opsonization) that can produce off-target activity in some contexts.

These properties nominate IL-1Ra as the initial payload for direct comparison. They do not establish pulmonary expression, exposure, efficacy, or safety; an anti-IL-1β payload remains a comparator rather than a clinically inferior option.

**Cross-indication research boundary.** IL-1 signaling is relevant across several inflammatory diseases, but indication choice, commercial value, and regulatory sequencing require disease-specific efficacy and safety evidence. For gout, the inhaled mRNA–IL-1Ra hypothesis remains a delivery and exposure experiment; existing anakinra use does not validate a pulmonary mRNA product.

**Cross-reference.** [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (CP5a × mRNA cell), [`delivery-route-matrix.md`](./delivery-route-matrix.md) (RNA platforms × inhaled cell), and [`inhaled-mrna-il1ra-pulse-computational.md`](./inhaled-mrna-il1ra-pulse-computational.md) (comp-033 full analysis).

---

### 5. Bacteriophage-mediated selective gut microbiome modulation

**Intervention.** Selective phage suppression of LPS-producing gram-negative gut species (CP1 priming relief), purine-fermenting *Bacteroides* species (substrate reduction upstream of urate generation), or specific dysbiosis patterns identified by 16S/metagenomics. Different from "add an organism" — phages are subtractive ecosystem-shaping, complementary to probiotic addition.

**Chokepoint(s) hit.** Gut microbiome shaping (community-level); CP1 (NF-κB priming via LPS reduction); upstream substrate reduction for urate generation. See [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (Bacteriophages row).

**Evidence level.** Animal Model + early-stage clinical for adjacent indications (AMR-associated infection, IBD). No gout programs. Approved in Eastern European jurisdictions; compassionate-use in the US.

**Delivery / implementation constraint.** Phage target specificity, propagation, downstream purification, microbiome effects, and cold-chain stability require a distinct development route.

**Candidate implementation routes.** Established phage manufacturing companies for production and a clinical partner for a gout-specific indication; target selection remains upstream of that choice.

**Cheapest first move.** Bacteriophage track Phase 1 lit scan: "phage selective gut microbiome modulation × hyperuricemia / gout" — $0, subagent task.

**Cross-reference.** [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md).

---

### 6. Intra-articular uricase ± co-formulated catalase for direct tophi dissolution

**Intervention.** Test UOX with co-formulated catalase or a UOX–catalase fusion in a controlled intra-articular model. Local crystal access, peroxide control, tissue safety, persistence, immunogenicity, sterility, and formulation behavior all remain empirical gates.

**Chokepoint(s) hit.** Local urate or crystal burden, if an exact configuration can demonstrate active enzyme, substrate access, peroxide control, residence, tissue safety, and immune safety. Systemic uricase precedents do not qualify this route. See the [delivery route × product class matrix](./delivery-route-matrix.md).

**Evidence level.** Animal Model (Pickering emulsion uricase + catalase IA — *J Nanobiotechnology* 2025 cited in [`gout-kill-chain-delivery-routes.md`](./gout-kill-chain-delivery-routes.md)); In Vitro precedent for the uricase-catalase fusion class (Schiavon, Veronese). No clinical program.

**Delivery / implementation constraint.** Direct intra-articular delivery requires a sterile purified formulation, controlled H₂O₂ handling, tissue-depot kinetics, and a correctly folded uricase–catalase product.

**Candidate implementation routes.** Recombinant production in any suitable expression host, followed by formulation as PLGA nanoparticles, Pickering emulsion, or hydrogel depot and evaluation with a clinical partner.

**Cheapest first move.** Use sequence and structure analysis to identify fusion-junction and folding questions, then test the actual uricase-catalase construct for expression and retained activity under shio-koji conditions. A pLDDT-based proxy cannot issue a LOW-risk gate.

**H₂O₂ biochemistry gate.** [comp-035](./intra-articular-uricase-h2o2-reaction-diffusion-computational.md) is a non-decision-grade Phase-0 prior. It does not establish a safe steady-state threshold, clear any architecture, or select a chassis. Its review leaves Amplex Red, catalase activity, retention, stoichiometry, diffusion, and tissue safety open.

The modeled result supports one bounded design lesson: advertised nanoscale proximity is not enough; total reaction-site catalase capacity must be measured. Pickering, fusion, and free co-formulation remain unranked until they are compared under matched conditions.

**Cheapest next wet-lab step (comp-035 handoff):** Compare H₂O₂ time courses under matched UOX and catalase activity in a synovial-fluid mimic, then test tissue safety for any architecture that advances. A low bulk H₂O₂ readout does not close local-exposure or tissue-safety questions.

**Cross-reference.** [`delivery-route-matrix.md`](./delivery-route-matrix.md), [`gout-kill-chain-delivery-routes.md`](./gout-kill-chain-delivery-routes.md), [`engineered-koji-protocol.md`](./engineered-koji-protocol.md), [`intra-articular-uricase-h2o2-reaction-diffusion-computational.md`](./intra-articular-uricase-h2o2-reaction-diffusion-computational.md) (comp-035 full analysis).

---

### 7. Pharmacological chaperones for ABCG2 Q141K folding rescue

**Intervention.** Small molecules that bind misfolded Q141K ABCG2 and rescue trafficking from the ER aggresome to the apical brush border membrane. CFTR correctors provide a precedent for pharmacological rescue of a misfolded ABC transporter, but they do not establish rescue of Q141K ABCG2. The gout-risk association motivates a trafficking assay; it does not identify a compound.

**Chokepoint(s) hit.** Gut and renal ABCG2 simultaneously (oral systemic small molecule). This direct chaperone hypothesis is distinct from the separate, still-unvalidated proposal that butyrate could reproduce pharmacologic HDAC-inhibitor rescue of Q141K.

**Evidence level.** In Vitro (academic mechanism literature, Basseville 2012 PMID 22472121 for HDAC-mediated rescue precedent); no Q141K-specific chaperone clinical programs. Mechanistic Extrapolation from CFTR-corrector class.

**Delivery / implementation constraint.** The hypothesis requires a validated binding or folding-rescue mechanism, medicinal-chemistry screening, and a Q141K trafficking-and-flux assay.

**Candidate implementation routes.** Structure-based or folding-focused screening against ABCG2 Q141K, followed by medicinal chemistry; formulation and regulatory route come only after a validated hit.

**Current computational verdict: INCONCLUSIVE ([comp-047](./abcg2-q141k-chaperone-rescreen-computational.md), superseding comp-032).** Comp-032 encoded drug-class priors. COMP-047's corrected executable result excludes rosuvastatin and leaves vorinostat as one marginal `uncertain` row, not a docking-backed priority. The CFTR correctors are cross-protein mechanism comparators rather than validated ABCG2 positives; their failure to earn a tier limits this setup but does not kill the rescue route.

Vorinostat remains relevant for a different reason: Basseville et al. reported Q141K expression, surface-trafficking, and efflux rescue (**In Vitro**; PMID 22472121). That evidence supplies a validation control and does not validate direct fold-site binding. The unranked comp-032 hypothesis inventory and the COMP-047 correction live in [`abcg2-modulators.md`](./abcg2-modulators.md); this index does not duplicate them.

**Next move:** [validation §1.22](./validation-experiments.md#122-gut-compartment-hdac-directed-candidate-screen-for-q141k-abcg2-trafficking-rescue) is the decisive surface: Q141K trafficking, basolateral-to-apical urate flux, direct ABCG2 inhibition, intracellular exposure, viability, and barrier integrity. Folding-ensemble or ΔΔG modeling is an optional new computational route, not a prerequisite. Any compounding-pharmacy conversation remains gated behind a reproduced functional rescue with acceptable counterscreens.

**Cross-reference.** [`abcg2-modulators.md`](./abcg2-modulators.md) §"Pharmacological-chaperone route", [`abcg2-q141k-chaperone-rescreen-computational.md`](./abcg2-q141k-chaperone-rescreen-computational.md) (comp-047, current) · [`abcg2-q141k-chaperone-screen-computational.md`](./abcg2-q141k-chaperone-screen-computational.md) (comp-032, superseded).

---

### 8. Duckweed (Lemnaceae) — edible biomanufacturing chassis

**Intervention.** Duckweed (*Lemna* / *Spirodela* / *Wolffia*) as an edible, photosynthetic biomanufacturing chassis where the organism may serve as both factory and oral-delivery material. The evidence home documents glycoengineered antibodies, secreted recombinant proteins, oral vaccines in animals, and isolated duckweed flavonoids; none establishes a whole-duckweed urate-lowering effect.

**Chokepoint(s) hit.** Payload-dependent. Animal vaccine studies support the oral/mucosal delivery premise for their exact antigens and protocols. A duckweed-expressed uricase remains an untested CP6 concept; antibody-like payloads may instead exploit the chassis's glycoengineering option.

**Evidence level.** Animal Model (oral vaccines in chickens, fish, and mice); In Vitro / protein characterization (recombinant secretion and glycoengineering). Duckweed-to-urate translation remains a **Mechanistic Extrapolation**. Exact quantitative records and commercial-status claims belong on [`duckweed-aquatic-chassis.md`](./duckweed-aquatic-chassis.md) and require dated refresh before use.

**Delivery / implementation constraint.** For gut-luminal uricase, duckweed has not shown a biological or delivery advantage that compensates for stable-line development time. Its potential advantages concern other protein formats and must be tested against those use cases rather than used to rank the gout target.

**Candidate implementation routes.** *S. polyrhiza*, *L. minor*, and *W. australiana* remain unranked options; no consensus host has been established.

**Cheapest first move.** DW-1/DW-2 lit-scan + in-silico expression-feasibility prior for uricase in *S. polyrhiza* ($0, ~1–2 wks) before any wet-lab. Full follow-up table in [`duckweed-aquatic-chassis.md`](./duckweed-aquatic-chassis.md) §Open follow-ups.

**Cross-reference.** [`duckweed-aquatic-chassis.md`](./duckweed-aquatic-chassis.md) provides the duckweed evidence and falsification gates; [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) compares intervention routes by gout weakness.

---

## Cross-modality interaction questions

Mechanistic separation can justify an interaction experiment, but it does not establish biological additivity, compatible exposure, safety, or a product architecture. Each arm must first pass independently; any combination then needs a prespecified additive null, compatibility controls, and configuration-specific safety readouts.

### M1. Engineered PDB configuration × disulfiram — upstream disposal and downstream pyroptotic-exit blockade

**Composition.** CBT2.0 has animal-model urate-lowering precedent; its terminal carbon products and human magnitude are unresolved. Disulfiram targets downstream GSDMD. The mechanisms are conceptually separated, but biological additivity, exposure compatibility, and any SCFA-mediated host effect are unproven.

**Chokepoint(s) hit.** Urate disposal is upstream of the NLRP3 cascade; disulfiram targets CP6b GSDMD pyroptotic exit. They are not two branches of CP6.

**Candidate implementation routes.** PDB arm via an engineered LBP; disulfiram arm via a regulated small-molecule route. Neither route establishes biological additivity.

**Why this entry exists here.** The combination has a nonredundant mechanistic rationale, but it remains gated by carbon fate, exposure, compatibility, and additivity experiments.

**Next evidence.** [comp-027](./disulfiram-dose-modeling-computational.md) is a hypothesis generator, not a dose or regimen model. [comp-031](./dual-chassis-ecn-pdb-uricase-computational.md) is unusable for current decisions because it inherits an unsupported flat UOX regime, assigns unmeasured butyrate production to engineered EcN, and mixes compartments. COMP-044 establishes only that the legacy unconditional flat-dose classification is not robust to the tested substrate-occupancy and finite-window diagnostics. It does not identify the true physiological regime or choose one strain, separate strains, or temporal staging.

Run carbon-fate and residual-flux experiments before choosing a microbial configuration. Then test the exact microbial configuration and disulfiram separately and together under a prespecified interaction model, with drug–microbe compatibility, exposure, GSDMD activity, urate disposal, carbon products, and safety measured directly. The literature scan rules out one conflation—β-hydroxybutyrate is not butyrate—but does not establish that the pair is pharmacokinetically or pharmacodynamically clean.

**Cross-reference.** [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) §"Companion intervention: compounded disulfiram"; [`disulfiram.md`](./disulfiram.md) §"Companion intervention: PDB-engineered EcN"; [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md); [`computational-experiments.md`](./computational-experiments.md) comp-027 + comp-031.

---

## Unresolved delivery questions

These hypotheses need the same mechanism, evidence, exposure, and delivery audit before admission:

- **Engineered exosomes** carrying NLRP3 inhibitors targeted to CD163+ macrophages — see [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md).
- **CRISPR / base editing** for Q141K → Q141 in crypt stem cells — see [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md). Delivery, off-target effects, durability, and tissue access remain unresolved.
- **Wearable / microneedle continuous UA monitoring** — not an intervention per se, but a monitoring tool that changes intervention-titration kinetics. Different shape; possibly belongs in a separate monitoring-pending page.
- **GSDMD pore-mediated self-delivery** (see [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md)) — the open engineering question is whether an exact payload can be sourced and delivered at a defined extracellular exposure while pore formation supplies a selective intracellular entry route. comp-042 leaves KPV A2 unresolved and does not qualify any route; its favorable A2 cases are pore-only heuristic diagnostics, not total-cell selectivity. The empirical gate is [§1.32](./validation-experiments.md#132-gsdmd-pore-self-delivery--matched-uptake-and-selectivity-probe): first test an empirically prequalified transporter-orphan, membrane-impermeant tracer under matched pore-on/off conditions, then treat payload sourcing and formulation as candidate-specific decisions.
- **Engineered C1-INH (SERPING1, recombinant complement regulator) in an LBP-luminal chassis** — a CP0 LBP candidate. The [retired COMP-024 model](./complestatin-bgc-lbp-feasibility-computational.md) supplies no priority or viability evidence. **Sister to DAF SCR1-4:** DAF accelerates convertase decay at the MSU crystal surface; C1-INH inactivates C1r/C1s + MASP-2 at the classical/lectin pathway entry point. **Next move:** characterize an exact EcN-secreted SERPING1 configuration and directly measure folding, glycosylation dependence, luminal stability, and retained inhibitory function; do not use a pLDDT-accessibility score as the gate.

---

## Decision rule

Advance an entry only when its gout-relevant mechanism, evidence level, target exposure, safety constraints, and cheapest discriminating experiment are explicit. Select a delivery or production route only after those questions survive scrutiny. Retire or revise the entry when the mechanism is falsified; place implementation detail in the linked intervention dossier when a route is selected.
