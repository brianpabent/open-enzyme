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

**Evidence level.** Animal Model (CBT2.0 engineered EcN, −63% plasma UA in hyperuricemic mice — Li et al. 2025 Life Metabolism PMID 41070194); Human Retrospective Cohort (Stanford n=14K clindamycin vs Bactrim, HR 1.30 for incident gout — Liu et al. 2023 Cell PMID 37541197); Human Observational (FARMM antibiotic depletion n=30 fecal urate +40–50%); Mechanistic Extrapolation (quantitative SUA effect in typical gout patient with intact renal function).

**Delivery / implementation constraint.** DOPDH requires SelD selenophosphate synthase, and the pathway is obligate anaerobic. The eight-enzyme cluster therefore requires a compatible organism and manufacturing environment.

**Candidate implementation routes.** Multiple, all open:
1. **Engineered *E. coli* Nissle 1917 expressing the full PDB cluster** (CBT2.0 precedent in Li 2025) — facultative anaerobe, EcN safety / probiotic record, already used in PULSE uricase work, native SelD present
2. **Defined-strain anaerobic probiotic** (*Clostridium sporogenes*, *Lacrimispora saccharolytica*, *Enterocloster bolteae*) — naturally express the cluster but oxygen-sensitive manufacturing is a barrier
3. **FMT from PDB-rich donors** — case reports exist for gout FMT; regulatory pathway exists for some indications
4. **Prebiotic enrichment** — inulin/FOS/resistant starch enriches PDB-positive Lachnospiraceae and Ruminococcaceae; ~10% SUA reduction in animal/small-human trials; doesn't require an engineered organism
5. **Dietary cofactor adequacy (selenium)** — selenium-dependent DOPDH runs ~27× faster than the sulfur variant; selenium deficiency could phenocopy PDB depletion without changing bacterial abundance; trivially cheap if relevant

**Cheapest first move.** Two parallel:
- Serum selenium on next blood panel (~$40–80 standard clinical) — answers whether the cofactor side of the question is gating Brian's gut PDB function. Already added to [`self-experiment-protocol.md` §11.0](./self-experiment-protocol.md).
- Cranberry juice n=1 (4 weeks unsweetened, ~$20) — tests the parallel *Alistipes indistinctus* / hippuric acid → ABCG2 axis via direct dietary benzoate → glycine conjugation → hippuric acid, without needing bacterial colonization. Different mechanism, same downstream node (ABCG2). See [`abcg2-modulators.md`](./abcg2-modulators.md) Alistipes Tier 2.

**Cross-reference.** [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) (mechanism), [`abcg2-modulators.md`](./abcg2-modulators.md) (PPARγ/ABCG2 axis), [`gut-lumen-sink.md`](./gut-lumen-sink.md) (PULSE context for EcN chassis option), [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) (LBP framework for anaerobic options).

---

### 2. Kidney-tropic siRNA against URAT1 mRNA

**Intervention.** Sequence-specific siRNA knockdown of URAT1 mRNA in renal proximal tubule cells, delivered via kidney-tropic conjugate chemistry (folate-receptor, megalin-binding, or related approaches). Eliminates the dose-dependent off-target profile of small-molecule URAT1 inhibitors (benzbromarone hepatotoxicity, lesinurad cardiovascular signal). Quarterly SC dosing precedent from GalNAc-siRNA approvals (inclisiran for PCSK9, patisiran for TTR — both liver-tropic, kidney-tropic chemistry is the active research class).

**Chokepoint(s) hit.** Renal URAT1 reabsorption — the single largest reabsorption step in the renal urate handling chain. GLUT9 is a parallel target. Renal urate disposal sits on a different mechanism axis from gut-lumen disposal (the koji thesis); the two are complementary, not substitutional. See [`sirna-urat1-modality.md`](./sirna-urat1-modality.md).

**Evidence level.** Mechanistic Extrapolation for gout specifically. Clinical Trial precedent for the delivery class (inclisiran, patisiran approved for non-renal targets). No clinical program for URAT1 specifically as of 2026-05-15.

**Delivery / implementation constraint.** Kidney-tropic RNA delivery, formulation, and target-cell uptake remain the central implementation problems.

**Candidate implementation route.** Synthetic siRNA plus a kidney-tropic conjugate, with commercial manufacturing and a clinical development partner.

**Cheapest first move.** comp-009 (URAT1 mRNA target site selection via RNAfold + accessibility scoring) — $0, ~1 week, queued in [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) Phase 2.

**Cross-reference.** [`sirna-urat1-modality.md`](./sirna-urat1-modality.md), [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (Renal compartment row), [`delivery-route-matrix.md`](./delivery-route-matrix.md) (RNA platforms × SC cell).

---

### 3. Engineered LBP (obligate anaerobe) chassis — *F. prausnitzii*, *Akkermansia*, *Bacteroides*

**Intervention.** Live biotherapeutic products engineered from gut-native obligate anaerobes. Payload-dependent possibilities include *F. prausnitzii* for local butyrate (supported WT-ABCG2 induction plus an unvalidated Q141K-rescue extension), *Akkermansia muciniphila* for mucus-layer repair, and *Bacteroides* for broader metabolic engineering. Durable human colonization, product titer, epithelial exposure, and clinical effect remain development gates.

**Chokepoint(s) hit.** Depends on engineered payload. Gut ABCG2 induction (via SCFA), gut barrier repair (CP1 LPS / TNFα leak), gut microbiome shaping (community-level). See [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md).

**Evidence level.** Mechanistic Extrapolation + Animal Model precedent (Sonnenburg lab Bacteroides editing toolkit; Pendulum probiotic commercial *Akkermansia*-containing product). LBP regulatory framework (FDA 2018 guidance) defined; clinical programs exist for other indications.

**Delivery / implementation constraint.** Obligate anaerobic manufacturing, stabilization, colonization, epithelial exposure, and the Live Biotherapeutic Product regulatory framework.

**Candidate implementation routes.** *F. prausnitzii*, *Akkermansia muciniphila*, or *Bacteroides*, with commercial manufacturing, distribution, and cold chain.

**Cheapest first move.** LBP track Phase 2 lit scans (engineering toolkit + commercial landscape + FDA LBP regulatory path) — queued in [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md). $0 cost, ~1–2 weeks via subagent.

**Cross-reference.** [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) is the canonical scope page.

---

### 4. Inhaled mRNA-IL-1RA pulse therapy for acute gout flare

**Intervention.** Lipid nanoparticle-formulated mRNA encoding IL-1 receptor antagonist (anakinra-equivalent), delivered via pulmonary inhaler. Transient expression matches the short flare window (12–72 hours). The pulmonary surface area (~70 m²) maximizes uptake; mRNA-LNP delivery for pulmonary indications is mature (CF, RSV, asthma research programs). Eliminates SC injection requirement for flare management; cost-competitive with $300K/yr canakinumab if mRNA manufacturing economics hold.

**Chokepoint(s) hit.** CP5a (IL-1β receptor blockade). Companion target for the existing SC anakinra / canakinumab options. See [`modality-chokepoint-matrix.md` §"Open exploration questions" #5](./modality-chokepoint-matrix.md).

**Evidence level.** Mechanistic Extrapolation. No clinical program in any indication uses mRNA-IL-1RA for flare-window therapy. Adjacent precedents (mRNA vaccines IM, mRNA pulmonary research) establish the chassis feasibility.

**Delivery / implementation constraint.** Pulmonary LNP delivery, repeat-dose tolerability, exposure duration, and receptor occupancy remain unresolved.

**Candidate implementation route.** Synthetic mRNA plus LNP and an inhaler device; commercial manufacturing and a clinical partner are required.

**Cheapest first move.** Mechanism + delivery feasibility lit scan: "mRNA-IL-1RA pulse" + "pulmonary LNP for acute inflammatory indications" — $0, subagent task. Result: either confirms novel territory + bounds the chassis question, or surfaces an existing program OE didn't know about.

**Computational gate — [comp-033](./computational-experiments.md) RED single-dose + [comp-036](./computational-experiments.md) YELLOW repeat-dose (2026-05-16):** comp-033 found single-dose plasma Cmax 0.025 µg/mL = 2% of anakinra benchmark (1.5 µg/mL). comp-036 followed up with multi-dose accumulation + receptor-occupancy framing (IL-1Ra Kd vs IL-1R1: 0.1–10 nM log-uniform per Arend 1990 JCI + Schreuder 1997 Nature crystal — **nM regime, not pM as initially speculated**). 80%-occupancy plasma threshold: **73 ng/mL median [9–553 p05-p95]**. Per-regimen verdict: **QD RED** (24h troughs drop below threshold; mean occupancy 0.66 but median 0% of 72h flare window above 80%); **BID × 4–28 doses YELLOW** (median 50–56% of flare window above 80% occupancy; best regimen but doesn't clear 95% high-confidence bar); **Loading 2× + QD × 14 YELLOW** (median 32% above 80%; first-day boost decays). No regimen clears the GREEN bar at current input uncertainty. Top sensitivities: Kd_nM (ρ −0.69) + translation-efficiency mass ratio (ρ +0.58) + dose (ρ +0.24). **Two wet-lab measurements would tip the verdict**: (1) integrated translation-efficiency mass ratio in human alveolar epithelium (ferret/NHP inhaled-LNP + BAL protein quant); (2) modern SPR Kd measurement IL-1Ra vs IL-1R1 ectodomain. Full analyses: [`inhaled-mrna-il1ra-pulse-computational.md`](./inhaled-mrna-il1ra-pulse-computational.md) (comp-033) + [`repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md`](./repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md) (comp-036).

**Research comparison.** The relevant test is not an assumed clinical substitution for prednisone or anakinra. It is whether the measured exposure and receptor occupancy produce a reproducible flare-model effect with acceptable repeat-dose pulmonary safety. The two wet-lab measurements above gate any clinical or economic comparison.

**Why IL-1Ra over anti-IL-1β monoclonal as the mRNA payload (partner-conversation argument):** the alternative mRNA cassette would encode an anti-IL-1β antibody (canakinumab-equivalent). IL-1Ra wins for four reasons that partners ask about:

1. **Mechanism breadth.** IL-1Ra blocks both IL-1α AND IL-1β at the single IL-1R1 receptor — broader pathway coverage. Anti-IL-1β monoclonals only neutralize IL-1β. For gout the difference is small (IL-1β is the dominant ligand), but for COPD / ARDS / IPF the cross-indications, IL-1α also drives sterile inflammation, so the broader-mechanism payload is a feature, not a quirk.
2. **Protein size + structure.** IL-1Ra is **~17 kDa, no disulfide bonds, no glycosylation required for activity** — easier mRNA expression and lung-tissue translation. Antibodies are **~150 kDa with mandatory glycosylation + paired heavy/light chain assembly** — substantially harder for transient pulmonary mRNA expression. Translation-efficiency mass ratio (comp-033's dominant sensitivity driver, ρ = +0.78) favors small non-glycosylated payloads by ~10×.
3. **Immunogenicity.** Human IL-1Ra is endogenous (body makes its own — see [`nlrp3-inflammasome.md`](./nlrp3-inflammasome.md) §"Chokepoint 5"); recombinant IL-1Ra is therefore essentially zero-immunogenicity. Humanized antibodies retain low but non-zero immunogenicity (anti-drug antibody response over chronic dosing).
4. **Cleanness of mechanism.** IL-1Ra is purely competitive antagonism — no agonism, no ADCC, no CDC, no off-target effector function. Antibodies have Fc-mediated effector functions (ADCC / CDC / opsonization) that can produce off-target activity in some contexts.

The payload choice is structurally similar to why ankakinra and not canakinumab is the preferred reference for the inhaled-mRNA cassette: same mechanism, smaller protein, broader pathway coverage, lower immunogenicity. Partners evaluating the cassette should land on IL-1Ra not anti-IL-1β.

**Cross-indication leverage — the commercial case is not gout alone:** gout is a low-priority indication for big pharma; nobody develops inhaled mRNA-IL-1RA *for gout*. But the IL-1 axis is implicated across many indications with much larger markets: **COPD exacerbations** (~16M US patients, ~$50B annual healthcare cost, clear IL-1β-driven neutrophilic inflammation), **severe asthma — T2-low/neutrophilic phenotype** (large unmet need; T2-high has biologics like dupilumab/mepolizumab, T2-low does not), **ARDS / acute lung injury** (~190K US cases/yr, 40% mortality), **IPF**, **CRS from CAR-T**, **recurrent pericarditis**. The regulatory strategy that actually works: approve for a primary indication first (most likely COPD exacerbations or ARDS by market size × mechanism fit), then off-label use spreads to gout — same playbook as anakinra (approved 2001 for RA, now widely off-label for gout / pericarditis / Schnitzler / sJIA / CAPS / COVID-CRS). **Implication for partner conversations:** the comp-033 Tier-A inhaled-mRNA companies (Arcturus LUNAR-CF, ReCode RCT2100, Ethris/AstraZeneca, Sanofi/Translate Bio) develop for CF/RSV/asthma, not gout. Open Enzyme's role is **target validation + the multi-indication cross-leverage argument** — making the case to a partner that IL-1Ra has indications beyond their initial target so an mRNA-IL-1RA cassette swap is platform-justifiable. Gout-patient access comes off-label after primary-indication approval, like anakinra. **Near-term bridge for gout patients while this 5–10 year development horizon plays out: anakinra SC** — see [`gout-action-guide.md` §"This year (advanced)"](./gout-action-guide.md) for the off-label gout protocol (100 mg/day SC × 3 days, NOT intra-articular).

**Cross-reference.** [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (CP5a × mRNA cell), [`delivery-route-matrix.md`](./delivery-route-matrix.md) (RNA platforms × inhaled cell), [`inhaled-mrna-il1ra-pulse-computational.md`](./inhaled-mrna-il1ra-pulse-computational.md) (comp-033 full analysis), [`disulfiram.md`](./disulfiram.md) + [`gout-action-guide.md`](./gout-action-guide.md) (anakinra SC bridge protocol).

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

**Intervention.** Direct injection of uricase (with co-formulated catalase or as a uricase-catalase fusion protein) into a tophi-bearing joint. Bypasses systemic immunogenicity issue (locally bounded immune exposure), bypasses substrate-access issue at SC depot (tophi ARE concentrated urate at ~100× plasma), bypasses H2O2-in-tissue issue via co-localized catalase (Schiavon / Veronese early-2000s precedent for uricase-catalase fusion). Clinical analog: intra-articular corticosteroid for acute gout flare.

**Chokepoint(s) hit.** CP6 (uricase mechanism), local tophi dissolution. Sister to the existing IV pegloticase / SEL-212 system at a different delivery target (one specific joint with crystal deposition rather than systemic). See [`delivery-route-matrix.md` §"Open exploration questions" #1](./delivery-route-matrix.md).

**Evidence level.** Animal Model (Pickering emulsion uricase + catalase IA — *J Nanobiotechnology* 2025 cited in [`gout-kill-chain-delivery-routes.md`](./gout-kill-chain-delivery-routes.md)); In Vitro precedent for the uricase-catalase fusion class (Schiavon, Veronese). No clinical program.

**Delivery / implementation constraint.** Direct intra-articular delivery requires a sterile purified formulation, controlled H₂O₂ handling, tissue-depot kinetics, and a correctly folded uricase–catalase product.

**Candidate implementation routes.** Recombinant production in any suitable expression host, followed by formulation as PLGA nanoparticles, Pickering emulsion, or hydrogel depot and evaluation with a clinical partner.

**Cheapest first move.** comp-NNN protease-stability + folding feasibility analysis of a uricase-catalase fusion construct under shio-koji conditions (extends the comp-006 / comp-007 framework to a chimeric protein). Then a single-construct expression test if the comp-NNN returns LOW risk.

**H₂O₂ biochemistry gate — [comp-035](./intra-articular-uricase-h2o2-reaction-diffusion-computational.md) 2026-05-16: GREEN across all three architectures, but the GREEN is NOT decision-grade (comp-review 2026-07-14).** Treat H₂O₂ safety as a **testable Phase-0 prior gated on the Amplex Red wet-lab measurement** (validation §1.33/§1.36), not as closed — **do not promote the IA uricase route on this result alone**; several load-bearing choices are hardcoded. Reaction-diffusion analysis with Damköhler-number coupling, 20,000 Monte Carlo samples per architecture over kinetic / diffusion / geometric / joint-condition priors. Predicted steady-state [H₂O₂] at joint-tissue boundary (median, 5th–95th percentile):
- **Pickering emulsion** (Liu 2025 PEBR geometry): **0.19 µM** [0.034–1.1 µM] — GREEN
- **Fusion protein** (Schiavon class, 1–5 nm separation): **0.034 µM** [0.006–0.20 µM] — GREEN
- **Free co-formulated**: **0.19 µM** [0.005–7.2 µM, max 120 µM in worst-case URI:CAT 100:1 corner] — GREEN at reasonable stoichiometry; YELLOW at uneven URI:CAT

All three clear the 10 µM safe threshold by 5–50× margin under reference conditions. Toxicity threshold band (GREEN < 10 µM, YELLOW 10–100 µM, RED > 100 µM) was itself a comp-035 contribution — no published steady-state synovial-tissue toxicity curve existed; anchored on Schalkwijk 1986/87 (PMID 3707631) injected-GOx model + 26+ in vitro chondrocyte bolus studies + endogenous synovial baseline (~1 µM).

**Substantive proximity-claim reframe (load-bearing for chassis selection):** **The FRET <10 nm proximity advertised in Liu 2025 is NOT the safety mechanism in the Pickering architecture.** Da_shell ~5 × 10⁻³ means the 5 nm catalase shell is too thin to scavenge H₂O₂ in transit — escape fraction ~0.998. The actual safety mechanism is **bulk-phase catalase scavenging from catalase distributed across all dispersed droplets in the joint volume** — mathematically equivalent to free co-formulated at the same total dose. Catalase is so fast (kcat 10⁷–10⁸ s⁻¹) that bulk first-order destruction dominates regardless of proximity geometry. Pickering's actual load-bearing advantages are (a) fixed URI:CAT stoichiometry preservation in vivo, (b) catalase activity protection during storage / immune exposure, (c) mannose-targeted retention to tophi — **not the FRET proximity claim.**

**Chassis-selection criteria:** choose architecture on **production economics + regulatory pathway + manufacturing complexity + in vivo retention + immunogenicity**, not advertised proximity claims. Catalase (kcat/Km) is the dominant safety-margin driver across all three architectures (Spearman r = −0.95 to −0.97); **catalase preparation quality + in vivo stability + proportional dosing** are first-order chassis-selection variables.

**Cheapest next wet-lab step (comp-035 handoff):** **Amplex Red microelectrode H₂O₂ measurement** in synovial-fluid mimic with dispersed architecture + 0.5 mM urate substrate (~$2–5K per architecture). Tissue-level effects (cartilage damage, synoviocyte response) are downstream of [H₂O₂] exposure — sub-µM Amplex Red readout makes those low by construction. Chondrocyte-cytotoxicity titration only needed if Amplex Red surfaces unexpectedly high [H₂O₂].

**Cross-reference.** [`delivery-route-matrix.md`](./delivery-route-matrix.md), [`gout-kill-chain-delivery-routes.md`](./gout-kill-chain-delivery-routes.md), [`engineered-koji-protocol.md` §"The Hydrogen Peroxide Question — and why the chassis solves it for free"](./engineered-koji-protocol.md), [`intra-articular-uricase-h2o2-reaction-diffusion-computational.md`](./intra-articular-uricase-h2o2-reaction-diffusion-computational.md) (comp-035 full analysis).

---

### 7. Pharmacological chaperones for ABCG2 Q141K folding rescue

**Intervention.** Small molecules that bind misfolded Q141K ABCG2 and rescue trafficking from the ER aggresome to the apical brush border membrane. CFTR-corrector class precedent (ivacaftor / tezacaftor / elexacaftor for ΔF508 CFTR — multibillion-dollar therapeutic class). Same ATP-binding cassette superfamily as CFTR; same design problem. Q141K is the #1 gout-risk GWAS variant.

**Chokepoint(s) hit.** Gut and renal ABCG2 simultaneously (oral systemic small molecule). This direct chaperone hypothesis is distinct from the separate, still-unvalidated proposal that butyrate could reproduce pharmacologic HDAC-inhibitor rescue of Q141K.

**Evidence level.** In Vitro (academic mechanism literature, Basseville 2012 PMID 22472121 for HDAC-mediated rescue precedent); no Q141K-specific chaperone clinical programs. Mechanistic Extrapolation from CFTR-corrector class.

**Delivery / implementation constraint.** The hypothesis requires a validated binding or folding-rescue mechanism, medicinal-chemistry screening, and a Q141K trafficking-and-flux assay.

**Candidate implementation routes.** Structure-based or folding-focused screening against ABCG2 Q141K, followed by medicinal chemistry; formulation and regulatory route come only after a validated hit.

**Current computational verdict: INCONCLUSIVE ([comp-047](./abcg2-q141k-chaperone-rescreen-computational.md), 2026-07-14), superseding comp-032.** Comp-032's GREEN was a descriptor/class-prior heuristic with a tautological positive-control validation; comp-047 used AutoDock Vina without a class prior, and the CFTR-corrector positive controls failed to earn rank (0/4). **The list below is a hypothesis set, not validated priorities or empirical support**, retained only as input to a folding-ΔΔG or wet-lab study:

The superseded comp-032 hypothesis list and comp-047 correction live in [`abcg2-modulators.md`](./abcg2-modulators.md); this index does not duplicate them.

**Next move:** neither comp-032 nor comp-047 supplies a validated candidate, so **no compounding-pharmacy conversation is warranted yet.** Rigid docking can't discriminate chaperones here (mechanism mismatch). The real next step is a folding-ΔΔG calculation (MD / Rosetta) or a wet-lab Q141K trafficking-rescue assay (Caco-2 Q141K line) paired with basolateral→apical urate flux + an ABCG2-inhibition counterscreen; any compounding-pharmacy conversation is gated behind that wet-lab result. (source: abcg2-modulators.md, abcg2-q141k-chaperone-rescreen-computational.md)

**Cross-reference.** [`abcg2-modulators.md`](./abcg2-modulators.md) §"Pharmacological-chaperone route", [`abcg2-q141k-chaperone-rescreen-computational.md`](./abcg2-q141k-chaperone-rescreen-computational.md) (comp-047, current) · [`abcg2-q141k-chaperone-screen-computational.md`](./abcg2-q141k-chaperone-screen-computational.md) (comp-032, superseded).

---

### 8. Duckweed (Lemnaceae) — aquatic-sibling chassis class

**Intervention.** Duckweed (*Lemna* / *Spirodela* / *Wolffia*) as an edible, photosynthetic biomanufacturing chassis where the organism is simultaneously the factory and the oral delivery vehicle — the aquatic structural sibling of the koji thesis. Distinctive adds koji lacks: a photosynthetic feedstock (light + CO₂ + waste N/P, no sugar), tractable human-like N-glycosylation (Cox 2006 *Lemna* mAb, up to 50× ADCC vs CHO), and a documented multi-decade edible-vaccine track record. Notable adjacency: the lead bioreactor species *Spirodela polyrhiza* is botanically the TCM herb 浮萍/紫萍 and natively produces luteolin (XO inhibitor, IC₅₀ 4.79 µM) — a possible built-in hypouricemic background (extrapolation; no whole-duckweed urate study exists).

**Chokepoint(s) hit.** Depends on payload. Strongest *proven* fit is the oral/mucosal delivery axis (factory = delivery vehicle, demonstrated in vivo: 100% protection chicken IBV edible vaccine, *Plant Biotechnol J* 2025; 63.3% RPS fish *LamB*, *Front Immunol* 2020). Option value at CP6 (a duckweed-expressed uricase — never attempted; urate oxidase is natively peroxisomal in plants, so plausible) and any future systemic/injectable enzyme needing human glycans.

**Evidence level.** Animal Model (oral vaccines in chickens/fish/mice); In Vitro (recombinant titers — hGH 609 mg/L secreted; glyco-engineering); Commercial (food/feed lane only — Plantible *Lemna* protein 2025, EU novel-food approval; **zero** marketed duckweed *biologic*). Duckweed→urate = Mechanistic Extrapolation via isolated flavonoids.

**Delivery / implementation constraint.** For gut-luminal uricase, duckweed has not shown a biological or delivery advantage that compensates for stable-line development time. Its potential advantages concern other protein formats and must be tested against those use cases rather than used to rank the gout target.

**Candidate implementation routes.** *S. polyrhiza*, *L. minor*, and *W. australiana* remain unranked options; no consensus host has been established.

**Cheapest first move.** DW-1/DW-2 lit-scan + in-silico expression-feasibility prior for uricase in *S. polyrhiza* ($0, ~1–2 wks) before any wet-lab. Full follow-up table in [`duckweed-aquatic-chassis.md`](./duckweed-aquatic-chassis.md) §Open follow-ups.

**Cross-reference.** [`duckweed-aquatic-chassis.md`](./duckweed-aquatic-chassis.md) is the canonical scope page. Sibling peer-track: [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md).

---

## Cross-modality combinations

Compositions where two interventions on *different* chassis hit complementary chokepoints and stack additively without competing for the same production / delivery resource. These are not chassis-pending entries themselves — both arms have selected chassis — but the *composition* is worth surfacing here because the same chassis-is-downstream-of-chokepoint discipline applies: don't filter a stack as "off-platform" just because one arm doesn't live in the koji track.

### M1. Engineered PDB EcN × compounded disulfiram — urate-disposal upstream + CP6b pyroptotic-exit blockade

**Composition.** Engineered *E. coli* Nissle CBT2.0 has animal-model urate-lowering precedent; its butyrate output and human magnitude are unresolved. Disulfiram targets downstream GSDMD. The mechanisms remain conceptually separated, but biological additivity and any SCFA-mediated host effect are unproven; comp-031's quantitative combination result is invalidated. Product carbon fate and drug–microbe compatibility now gate this stack.

**Chokepoint(s) hit.** Urate disposal is upstream of the NLRP3 cascade; disulfiram targets CP6b GSDMD pyroptotic exit. They are not two branches of CP6.

**Candidate implementation routes.** PDB arm via an engineered LBP; disulfiram arm via a regulated small-molecule route. Neither route establishes biological additivity.

**Why this entry exists here.** The combination has a nonredundant mechanistic rationale, but it remains gated by carbon fate, exposure, compatibility, and additivity experiments.

**Cheapest first move.** Two parallel comp-NNNs, both completed 2026-05-16:
- **[comp-027](./disulfiram-dose-modeling-computational.md)** — downgraded to hypothesis-generator (comp-review 2026-07-14). It produced one modeled point on a hard-coded decision boundary, not a validated dose window or regimen. A dose-finding and drug–interaction study must precede any formulation or combination claim.
- **[comp-031](./dual-chassis-ecn-pdb-uricase-computational.md)** — **fully INVALIDATED 2026-07-13.** Its ΔSUA, substrate-competition, PDB-derived butyrate, Q141K-rescue, additivity, and two-strain recommendation are all retracted. The model validates neither a dual-cassette EcN nor separate strains. One strain, separate strains, and temporal staging remain unranked options pending comp-044/045/046 and validation §§1.33/1.34/1.37.

**Inter-arm PK interaction — resolved PK-clean (2026-07-13 lit scan).** A synthesis card proposed that PDB-derived butyrate might modulate the hepatic CYP enzymes that metabolize disulfiram, altering its effective dose. A focused scan ([`logs/disulfiram-butyrate-cyp-pk-scan-2026-07-13.md`](../logs/disulfiram-butyrate-cyp-pk-scan-2026-07-13.md)) found **no material interaction** and no dosing caveat: (1) disulfiram is a mechanism-based *inhibitor* of CYP2E1 (not a substrate whose clearance a CYP shift would swing), and no study shows butyrate-the-SCFA modulating CYP2E1 — the two CYP2E1-induction papers the claim leaned on used **β-hydroxybutyrate (a ketone) + palmitate**, which the card conflated with butyrate; (2) gut butyrate is exposure-limited — colonocytes oxidize ~70–80%, systemic butyrate is ~3–4 µM (portal tens of µM transiently), while HDAC-mediated hepatic CYP effects need ~0.5–5 mM (2–3 orders higher); (3) disulfiram's GSDMD-Cys191 blockade is covalent and nanomolar, insensitive to any modest CYP shift. The two arms stack **PK-clean** on the butyrate × CYP axis. (Butyrate does touch pyroptosis separately and *bidirectionally* — at upstream inflammasome priming, not the GSDMD pore step disulfiram blocks — so a *pharmacodynamic* interaction is not excluded, just not the CYP-PK one the card proposed.)

**Cross-reference.** [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) §"Companion intervention: compounded disulfiram"; [`disulfiram.md`](./disulfiram.md) §"Companion intervention: PDB-engineered EcN"; [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md); [`computational-experiments.md`](./computational-experiments.md) comp-027 + comp-031.

---

## Unresolved delivery questions

These hypotheses need the same mechanism, evidence, exposure, and delivery audit before admission:

- **Engineered exosomes** carrying NLRP3 inhibitors targeted to CD163+ macrophages — see [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md).
- **CRISPR / base editing in patient** for Q141K → Q141 in crypt stem cells — see [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md). Probably "delivery unsolved on a 5–10 year horizon" status.
- **Wearable / microneedle continuous UA monitoring** — not an intervention per se, but a monitoring tool that changes intervention-titration kinetics. Different shape; possibly belongs in a separate monitoring-pending page.
- **GSDMD pore-mediated self-delivery of OE-relevant biologics** (KPV / nanobodies / single SCR domains / IL-1RA — see [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md) §"Implication for OE biologics") — chassis-pending status: koji can produce the payloads; the chassis-question is the **delivery format** that gets the payload to the synovial fluid in time for the pore-opening window. Different chassis question than "what produces the molecule"; same general shape (real intervention, chassis open).
- **Engineered C1-INH (SERPING1, recombinant complement regulator) in an LBP-luminal chassis** — the next CP0 LBP engineering gate. [Comp-024](./computational-experiments.md) (2026-05-16) ranked complestatin-family BGC heterologous expression RED for the LBP track and C1-INH GREEN-provisional 0.774 by comparison. The remaining single-axis problem is luminal-protease stability plus glycosylation, testable with a comp-006-style analysis of SERPING1 in EcN-secreted format. **Sister to DAF SCR1-4:** DAF accelerates convertase decay at the MSU crystal surface; C1-INH inactivates C1r/C1s + MASP-2 at the classical/lectin pathway entry point. **Next move:** protease-stability and glycosylation feasibility for SERPING1 in EcN luminal-secreted format.

---

## Decision rule

Advance an entry only when its gout-relevant mechanism, evidence level, target exposure, safety constraints, and cheapest discriminating experiment are explicit. Select a delivery or production route only after those questions survive scrutiny. Retire or revise the entry when the mechanism is falsified; place implementation detail in the linked intervention dossier when a route is selected.
