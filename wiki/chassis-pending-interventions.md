---
title: "Chassis-Pending Interventions — interventions that hit OE chokepoints but await a chassis"
date: 2026-05-15
tags:
  - chassis-pending
  - platform-strategy
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
  - "2026-05-15 strategic reflection: chassis-is-downstream-of-chokepoint (synthesis/strategic-reflections/)"
  - "Umbrella CLAUDE.md §Curiosity and First-Principles Framing"
  - "Origin: 2026-05-15 PDB / GSDMD / kill-chain delivery research surfaced a finding that doesn't fit koji and was almost filtered as 'off-platform' — reframed as chassis-pending"
status: published
---

# Chassis-Pending Interventions

Interventions that hit Open Enzyme chokepoints with mechanism validated, but the engineering / implementation / delivery chassis is not yet identified.

These are **promising things that map to what we want to do**. The mechanism is real. The target chokepoint is documented. The chassis question is open. They are not deprioritized, not off-platform, not "rejected for not fitting koji." They are tracked here so the next time someone asks "what could we be missing?" the answer is visible rather than scattered.

## Why this page exists

Open Enzyme is a **chokepoint-first, chassis-second** platform. The platform mission is to disrupt the gout / NLRP3 / urate-disposal cascade; engineered *A. oryzae* koji is the highest-priority chassis because it harmoniously hits multiple chokepoints in one strain (uricase + lactoferrin + carnosine + DAF SCR1-4) and matches the food-grade / open-source / home-fermentable / democratized-access positioning. Koji is one expression of the mission, not the mission itself.

The risk this page mitigates: when a finding lands that hits a real chokepoint but doesn't fit koji, the recommendation step can quietly filter it as "off-platform." That filter is the failure mode the umbrella `CLAUDE.md` warns against ("don't ask 'does this fit the current chassis,' ask 'what open question might this tool answer?'"). This page makes the no-chassis-filter check structural rather than opportunistic.

**The honest status of an entry here:** the intervention is real, the mechanism is validated, multiple candidate chassis exist or are conceivable, **we don't know which is right yet**. Chassis selection is the next question, not the filter that kills the first one. See [`synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md`](../synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md) for the discipline-level reflection that produced this page.

## How to read this page

Each entry has a fixed shape:

- **Intervention** — what the intervention does, mechanistically
- **Chokepoint(s) hit** — which OE chokepoint(s) the intervention targets, with cross-reference
- **Evidence level** — Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation
- **Why not koji** — the specific reason the current koji chassis isn't right (not a value judgment; a mechanism / regulatory / engineering reason)
- **Candidate chassis** — the chassis options being considered. **The chassis is open. Listed candidates are options, not commitments.**
- **Cheapest first move** — the next step that doesn't require committing to a specific chassis. Usually a lit scan, a low-cost wet-lab experiment, an n=1 self-experiment, or a partner conversation.
- **Cross-reference** — the canonical wiki page(s) where this intervention is treated in mechanism depth

When an entry's chassis question resolves, the entry migrates: either to a new dedicated scope page in the wiki (if a chassis is selected and a new track begins — e.g., `engineered-lbp-chassis.md` if the chassis is engineered LBPs), or to a peer-track page already in the wiki (e.g., `compounding-pharmacy-track.md` if the answer is "compounded small molecule"). The chassis-pending page stays as the index for the open questions, not the implementation roadmap.

---

## Current chassis-pending interventions

### 1. Purine-degrading bacteria (PDB) restoration / engineered PDB pathway expression

**Intervention.** The 2,8-dioxopurine bacterial gene cluster degrades uric acid anaerobically to butyrate + acetate, hits CP6 (urate degradation) directly, and compounds via SCFA effects on multiple downstream nodes (ABCG2 induction + Q141K trafficking rescue + NLRP3 dampening + XO inhibition). The most common gout-associated ABCG2 variant (Q141K, ~3–15% population frequency) is HDAC-rescued by butyrate — making PDB-derived butyrate a natural genotype-targeted therapy via endogenous gut bacteria producing the molecule that fixes a genetic variant.

**Chokepoint(s) hit.** CP6 (urate degradation), CP2 (NLRP3 dampening via butyrate), gut ABCG2 induction (PPARγ axis), Q141K trafficking rescue (HDAC inhibition). See [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) for the full mechanism + evidence inventory.

**Evidence level.** Animal Model (CBT2.0 engineered EcN, −63% plasma UA in hyperuricemic mice — Li et al. 2025 Life Metabolism PMID 41070194); Human Retrospective Cohort (Stanford n=14K clindamycin vs Bactrim, HR 1.30 for incident gout — Liu et al. 2023 Cell PMID 37541197); Human Observational (FARMM antibiotic depletion n=30 fecal urate +40–50%); Mechanistic Extrapolation (quantitative SUA effect in typical gout patient with intact renal function).

**Why not koji.** DOPDH (the first-step enzyme) requires SelD selenophosphate synthase — prokaryote-specific, not present in *A. oryzae*. The pathway is obligate anaerobic; koji fermentation is aerobic. The gene cluster is 8 enzymes; even if SelD were resolved, koji is the wrong substrate (eukaryote with peroxisomal compartmentalization optimized for different chemistry).

**Candidate chassis.** Multiple, all open:
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

**Why not koji.** RNA platforms are not produced or delivered via engineered fermentation chassis. Different production stack (chemical synthesis or in vitro transcription), different formulation stack (LNP or GalNAc-like conjugates), different regulatory class (NDA pharma route).

**Candidate chassis.** Synthetic siRNA + kidney-tropic conjugate, delivered SC. Commercial pharma manufacturing. The OE platform's role is **discovery-engine output** (we surface URAT1 as a high-value target and the mRNA target-site selection); the chassis is downstream — partner with a pharma company, or spinout development.

**Cheapest first move.** comp-009 (URAT1 mRNA target site selection via RNAfold + accessibility scoring) — $0, ~1 week, queued in [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) Phase 2.

**Cross-reference.** [`sirna-urat1-modality.md`](./sirna-urat1-modality.md), [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (Renal compartment row), [`delivery-route-matrix.md`](./delivery-route-matrix.md) (RNA platforms × SC cell).

---

### 3. Engineered LBP (obligate anaerobe) chassis — *F. prausnitzii*, *Akkermansia*, *Bacteroides*

**Intervention.** Live biotherapeutic products engineered from gut-native obligate anaerobes. Hits multiple chokepoints depending on the engineered payload: engineered *F. prausnitzii* for local butyrate at the gut crypt (ABCG2 + Q141K + NLRP3 — same compounding effect as PDB); engineered *Akkermansia muciniphila* for mucus-layer repair (gut barrier / TNFα leak); engineered *Bacteroides* for broader metabolic engineering. Solves the "transit organism vs. colonization" problem the koji chassis has — these are gut-resident, durably colonizing.

**Chokepoint(s) hit.** Depends on engineered payload. Gut ABCG2 induction (via SCFA), gut barrier repair (CP1 LPS / TNFα leak), gut microbiome shaping (community-level). See [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md).

**Evidence level.** Mechanistic Extrapolation + Animal Model precedent (Sonnenburg lab Bacteroides editing toolkit; Pendulum probiotic commercial *Akkermansia*-containing product). LBP regulatory framework (FDA 2018 guidance) defined; clinical programs exist for other indications.

**Why not koji.** Obligate anaerobic organisms; koji is aerobic fermentation. Manufacturing requires anaerobic bioreactor + cold-chain stabilization — categorically not home-fermentable. Regulatory: Live Biotherapeutic Product framework, not food chassis.

**Candidate chassis.** *F. prausnitzii*, *Akkermansia muciniphila*, *Bacteroides* (with established engineering toolkits). Commercial pharma manufacturing + distribution + cold chain — explicitly **not** the democratized-home-access track the koji chassis enables.

**Cheapest first move.** LBP track Phase 2 lit scans (engineering toolkit + commercial landscape + FDA LBP regulatory path) — queued in [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md). $0 cost, ~1–2 weeks via subagent.

**Cross-reference.** [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) is the canonical scope page.

---

### 4. Inhaled mRNA-IL-1RA pulse therapy for acute gout flare

**Intervention.** Lipid nanoparticle-formulated mRNA encoding IL-1 receptor antagonist (anakinra-equivalent), delivered via pulmonary inhaler. Transient expression matches the short flare window (12–72 hours). The pulmonary surface area (~70 m²) maximizes uptake; mRNA-LNP delivery for pulmonary indications is mature (CF, RSV, asthma research programs). Eliminates SC injection requirement for flare management; cost-competitive with $300K/yr canakinumab if mRNA manufacturing economics hold.

**Chokepoint(s) hit.** CP5a (IL-1β receptor blockade). Companion target for the existing SC anakinra / canakinumab options. See [`modality-chokepoint-matrix.md` §"Open exploration questions" #5](./modality-chokepoint-matrix.md).

**Evidence level.** Mechanistic Extrapolation. No clinical program in any indication uses mRNA-IL-1RA for flare-window therapy. Adjacent precedents (mRNA vaccines IM, mRNA pulmonary research) establish the chassis feasibility.

**Why not koji.** mRNA / LNP is not produced or delivered via engineered fermentation. Different production stack, different formulation stack, different regulatory class.

**Candidate chassis.** Synthetic mRNA + LNP + inhaler device. Commercial pharma manufacturing. Clinical partner required.

**Cheapest first move.** Mechanism + delivery feasibility lit scan: "mRNA-IL-1RA pulse" + "pulmonary LNP for acute inflammatory indications" — $0, subagent task. Result: either confirms novel territory + bounds the chassis question, or surfaces an existing program OE didn't know about.

**Computational gate — [comp-033](./computational-experiments.md) returned RED on single-dose anakinra-Cmax-equivalence (2026-05-16):** single inhale predicted plasma Cmax 0.025 µg/mL is 2% of anakinra benchmark (1.5 µg/mL); 24h AUC 4% of anakinra; reverse-dose math says ~195 mg mRNA for 1/3-anakinra Cmax (8–25× above the highest currently-disclosed inhaled-mRNA clinical dose, Translate Bio MRT5005 at 24 mg). **Three paths forward keep the entry active (not closed):** (a) repeat-dose receptor-occupancy framing — gated on [comp-036](./computational-experiments.md) (in flight) which models IL-1R1 occupancy over the 72h flare window with multi-dose accumulation; (b) intra-articular mRNA delivery instead of pulmonary (separate chassis question); (c) accept sub-anakinra exposure with cost-edge framing. Sensitivity dominated by translation-efficiency mass ratio (ρ = +0.78); not dose itself. Economic edge holds independently: cost/flare $2–120 vs canakinumab $300K/yr → 50–3,000× cost edge. Full analysis: [inhaled-mrna-il1ra-pulse-computational.md](./inhaled-mrna-il1ra-pulse-computational.md).

**Why IL-1Ra over anti-IL-1β monoclonal as the mRNA payload (partner-conversation argument):** the alternative mRNA cassette would encode an anti-IL-1β antibody (canakinumab-equivalent). IL-1Ra wins for four reasons that partners ask about:

1. **Mechanism breadth.** IL-1Ra blocks both IL-1α AND IL-1β at the single IL-1R1 receptor — broader pathway coverage. Anti-IL-1β monoclonals only neutralize IL-1β. For gout the difference is small (IL-1β is the dominant ligand), but for COPD / ARDS / IPF the cross-indications, IL-1α also drives sterile inflammation, so the broader-mechanism payload is a feature, not a quirk.
2. **Protein size + structure.** IL-1Ra is **~17 kDa, no disulfide bonds, no glycosylation required for activity** — easier mRNA expression and lung-tissue translation. Antibodies are **~150 kDa with mandatory glycosylation + paired heavy/light chain assembly** — substantially harder for transient pulmonary mRNA expression. Translation-efficiency mass ratio (comp-033's dominant sensitivity driver, ρ = +0.78) favors small non-glycosylated payloads by ~10×.
3. **Immunogenicity.** Human IL-1Ra is endogenous (body makes its own — see [`nlrp3-inflammasome.md`](./nlrp3-inflammasome.md) §"Chokepoint 5"); recombinant IL-1Ra is therefore essentially zero-immunogenicity. Humanized antibodies retain low but non-zero immunogenicity (anti-drug antibody response over chronic dosing).
4. **Cleanness of mechanism.** IL-1Ra is purely competitive antagonism — no agonism, no ADCC, no CDC, no off-target effector function. Antibodies have Fc-mediated effector functions (ADCC / CDC / opsonization) that can produce off-target activity in some contexts.

The payload choice is structurally similar to why ankakinra and not canakinumab is the preferred reference for the inhaled-mRNA cassette: same mechanism, smaller protein, broader pathway coverage, lower immunogenicity. Partners evaluating the cassette should land on IL-1Ra not anti-IL-1β.

**Cross-indication leverage — the commercial case is NOT gout alone (added 2026-05-16):** gout is a low-priority indication for big pharma; nobody develops inhaled mRNA-IL-1RA *for gout*. But the IL-1 axis is implicated across many indications with much larger markets: **COPD exacerbations** (~16M US patients, ~$50B annual healthcare cost, clear IL-1β-driven neutrophilic inflammation), **severe asthma — T2-low/neutrophilic phenotype** (large unmet need; T2-high has biologics like dupilumab/mepolizumab, T2-low does not), **ARDS / acute lung injury** (~190K US cases/yr, 40% mortality), **IPF**, **CRS from CAR-T**, **recurrent pericarditis**. The regulatory strategy that actually works: approve for a primary indication first (most likely COPD exacerbations or ARDS by market size × mechanism fit), then off-label use spreads to gout — same playbook as anakinra (approved 2001 for RA, now widely off-label for gout / pericarditis / Schnitzler / sJIA / CAPS / COVID-CRS). **Implication for partner conversations:** the comp-033 Tier-A inhaled-mRNA companies (Arcturus LUNAR-CF, ReCode RCT2100, Ethris/AstraZeneca, Sanofi/Translate Bio) develop for CF/RSV/asthma, not gout. Open Enzyme's role is **target validation + the multi-indication cross-leverage argument** — making the case to a partner that IL-1Ra has indications beyond their initial target so an mRNA-IL-1RA cassette swap is platform-justifiable. Gout-patient access comes off-label after primary-indication approval, like anakinra. **Near-term bridge for gout patients while this 5–10 year development horizon plays out: anakinra SC** — see [`gout-action-guide.md` §"This year (advanced)"](./gout-action-guide.md) for the off-label gout protocol (100 mg/day SC × 3 days, NOT intra-articular).

**Cross-reference.** [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (CP5a × mRNA cell), [`delivery-route-matrix.md`](./delivery-route-matrix.md) (RNA platforms × inhaled cell), [`inhaled-mrna-il1ra-pulse-computational.md`](./inhaled-mrna-il1ra-pulse-computational.md) (comp-033 full analysis), [`disulfiram.md`](./disulfiram.md) + [`gout-action-guide.md`](./gout-action-guide.md) (anakinra SC bridge protocol).

---

### 5. Bacteriophage-mediated selective gut microbiome modulation

**Intervention.** Selective phage suppression of LPS-producing gram-negative gut species (CP1 priming relief), purine-fermenting *Bacteroides* species (substrate reduction upstream of urate generation), or specific dysbiosis patterns identified by 16S/metagenomics. Different from "add an organism" — phages are subtractive ecosystem-shaping, complementary to probiotic addition.

**Chokepoint(s) hit.** Gut microbiome shaping (community-level); CP1 (NF-κB priming via LPS reduction); upstream substrate reduction for urate generation. See [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (Bacteriophages row).

**Evidence level.** Animal Model + early-stage clinical for adjacent indications (AMR-associated infection, IBD). No gout programs. Approved in Eastern European jurisdictions; compassionate-use in the US.

**Why not koji.** Phage manufacturing is a different chassis — bacterial host strains for phage propagation, downstream purification, cold-chain stability. Not a fermentation chassis problem; a viral production chassis problem.

**Candidate chassis.** Established phage manufacturing companies (Adamas, Locus, Phaxiam, BiomX) for production. Clinical partner for gout-specific indication. Discovery-engine output: OE surfaces *which* bacterial targets are gout-relevant; production is downstream.

**Cheapest first move.** Bacteriophage track Phase 1 lit scan: "phage selective gut microbiome modulation × hyperuricemia / gout" — $0, subagent task.

**Cross-reference.** [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md).

---

### 6. Intra-articular uricase ± co-formulated catalase for direct tophi dissolution

**Intervention.** Direct injection of uricase (with co-formulated catalase or as a uricase-catalase fusion protein) into a tophi-bearing joint. Bypasses systemic immunogenicity issue (locally bounded immune exposure), bypasses substrate-access issue at SC depot (tophi ARE concentrated urate at ~100× plasma), bypasses H2O2-in-tissue issue via co-localized catalase (Schiavon / Veronese early-2000s precedent for uricase-catalase fusion). Clinical analog: intra-articular corticosteroid for acute gout flare.

**Chokepoint(s) hit.** CP6 (uricase mechanism), local tophi dissolution. Sister to the existing IV pegloticase / SEL-212 system at a different delivery target (one specific joint with crystal deposition rather than systemic). See [`delivery-route-matrix.md` §"Open exploration questions" #1](./delivery-route-matrix.md).

**Evidence level.** Animal Model (Pickering emulsion uricase + catalase IA — *J Nanobiotechnology* 2025 cited in [`gout-kill-chain-delivery-routes.md`](./gout-kill-chain-delivery-routes.md)); In Vitro precedent for the uricase-catalase fusion class (Schiavon, Veronese). No clinical program.

**Why not koji.** Whole-cell oral koji is the wrong format for direct intra-articular injection (live organisms in joints → septic arthritis). The chassis-as-formulation advantage of koji for H2O2 housekeeping (peroxisomal co-localization) doesn't transfer to a tissue depot. A purified uricase-catalase fusion protein needs a different production format (recombinant production in any expression system that produces correctly folded fusion protein).

**Candidate chassis.** Recombinant production of uricase-catalase fusion in any suitable expression host (could be koji-produced as purified protein, could be *E. coli*, could be *Pichia pastoris*). Formulation engineering layer (PLGA nanoparticles, Pickering emulsion, hydrogel depot). Clinical partner for the IA delivery trial.

**Cheapest first move.** comp-NNN protease-stability + folding feasibility analysis of a uricase-catalase fusion construct under shio-koji conditions (extends the comp-006 / comp-007 framework to a chimeric protein). Then a single-construct expression test if the comp-NNN returns LOW risk.

**H₂O₂ biochemistry gate — resolved by [comp-035](./computational-experiments.md) 2026-05-16: GREEN across all three architectures.** Reaction-diffusion analysis with Damköhler-number coupling, 20,000 Monte Carlo samples per architecture over kinetic / diffusion / geometric / joint-condition priors. Predicted steady-state [H₂O₂] at joint-tissue boundary (median, 5th–95th percentile):
- **Pickering emulsion** (Liu 2025 PEBR geometry): **0.19 µM** [0.034–1.1 µM] — GREEN
- **Fusion protein** (Schiavon class, 1–5 nm separation): **0.034 µM** [0.006–0.20 µM] — GREEN
- **Free co-formulated**: **0.19 µM** [0.005–7.2 µM, max 120 µM in worst-case URI:CAT 100:1 corner] — GREEN at reasonable stoichiometry; YELLOW at uneven URI:CAT

All three clear the 10 µM safe threshold by 5–50× margin under reference conditions. Toxicity threshold band (GREEN < 10 µM, YELLOW 10–100 µM, RED > 100 µM) was itself a comp-035 contribution — no published steady-state synovial-tissue toxicity curve existed; anchored on Schalkwijk 1986/87 (PMID 3707631) injected-GOx model + 26+ in vitro chondrocyte bolus studies + endogenous synovial baseline (~1 µM).

**Substantive proximity-claim reframe (load-bearing for chassis selection):** **The FRET <10 nm proximity advertised in Liu 2025 is NOT the safety mechanism in the Pickering architecture.** Da_shell ~5 × 10⁻³ means the 5 nm catalase shell is too thin to scavenge H₂O₂ in transit — escape fraction ~0.998. The actual safety mechanism is **bulk-phase catalase scavenging from catalase distributed across all dispersed droplets in the joint volume** — mathematically equivalent to free co-formulated at the same total dose. Catalase is so fast (kcat 10⁷–10⁸ s⁻¹) that bulk first-order destruction dominates regardless of proximity geometry. Pickering's actual load-bearing advantages are (a) fixed URI:CAT stoichiometry preservation in vivo, (b) catalase activity protection during storage / immune exposure, (c) mannose-targeted retention to tophi — **not the FRET proximity claim.**

**Updated chassis-selection criteria (post-comp-035):** choose architecture on **production economics + regulatory pathway + manufacturing complexity + in vivo retention + immunogenicity** — NOT on advertised proximity claims. Catalase (kcat/Km) is the dominant safety-margin driver across all three architectures (Spearman r = −0.95 to −0.97); **catalase preparation quality + in vivo stability + proportional dosing** are first-order chassis-selection variables.

**Cheapest next wet-lab step (comp-035 handoff):** **Amplex Red microelectrode H₂O₂ measurement** in synovial-fluid mimic with dispersed architecture + 0.5 mM urate substrate (~$2–5K per architecture). Tissue-level effects (cartilage damage, synoviocyte response) are downstream of [H₂O₂] exposure — sub-µM Amplex Red readout makes those low by construction. Chondrocyte-cytotoxicity titration only needed if Amplex Red surfaces unexpectedly high [H₂O₂].

**Cross-reference.** [`delivery-route-matrix.md`](./delivery-route-matrix.md), [`gout-kill-chain-delivery-routes.md`](./gout-kill-chain-delivery-routes.md), [`engineered-koji-protocol.md` §"The Hydrogen Peroxide Question — and why the chassis solves it for free"](./engineered-koji-protocol.md), [`intra-articular-uricase-h2o2-reaction-diffusion-computational.md`](./intra-articular-uricase-h2o2-reaction-diffusion-computational.md) (comp-035 full analysis).

---

### 7. Pharmacological chaperones for ABCG2 Q141K folding rescue

**Intervention.** Small molecules that bind misfolded Q141K ABCG2 and rescue trafficking from the ER aggresome to the apical brush border membrane. CFTR-corrector class precedent (ivacaftor / tezacaftor / elexacaftor for ΔF508 CFTR — multibillion-dollar therapeutic class). Same ATP-binding cassette superfamily as CFTR; same design problem. Q141K is the #1 gout-risk GWAS variant.

**Chokepoint(s) hit.** Gut and renal ABCG2 simultaneously (oral systemic small molecule). Pharmacologically distinct from butyrate-mediated HDAC rescue of Q141K (which is a different rescue mechanism).

**Evidence level.** In Vitro (academic mechanism literature, Basseville 2012 PMID 22472121 for HDAC-mediated rescue precedent); no Q141K-specific chaperone clinical programs. Mechanistic Extrapolation from CFTR-corrector class.

**Why not koji.** Small-molecule discovery + medicinal chemistry development is not a fermentation chassis output. The CFTR-corrector class came from pharma-style screening + structure-based design.

**Candidate chassis.** Small-molecule discovery campaign — AI-assisted binder design (RFdiffusion-style or related), structure-based virtual screening against ABCG2 Q141K. Compounding pharmacy track if a hit candidate has off-patent precedent in another indication (unlikely for novel chemistry, but worth checking).

**Cheapest first move.** comp-NNN: AlphaFold structure of ABCG2 Q141K + computational screen for known FDA-approved small molecules with conformational stabilizer activity in ABC transporter family (could surface a repurposing candidate; unlikely but cheap).

**Cross-reference.** [`abcg2-modulators.md`](./abcg2-modulators.md) §"Q141K trafficking rescue".

---

## Multi-chassis stacks (compositions across existing entries)

Compositions where two interventions on *different* chassis hit complementary chokepoints and stack additively without competing for the same production / delivery resource. These are not chassis-pending entries themselves — both arms have selected chassis — but the *composition* is worth surfacing here because the same chassis-is-downstream-of-chokepoint discipline applies: don't filter a stack as "off-platform" just because one arm doesn't live in the koji track.

### M1. Engineered PDB EcN × compounded disulfiram — urate-disposal upstream + CP6b pyroptotic-exit blockade

**Composition.** Engineered *E. coli* Nissle expressing the 2,8-dioxopurine cluster (CBT2.0 precedent, Li 2025 PMID 41070194, −63% plasma UA in mice) consumes luminal urate and produces butyrate → ABCG2 induction + NLRP3 dampening, *before* MSU crystals seed an inflammasome. Compounded oral disulfiram (250 mg/day; covalently modifies GSDMD Cys191) blocks the pyroptotic pore *after* NLRP3 fires, preventing IL-1β release and the inflammatory amplification cascade. The two arms hit the urate→inflammation axis at opposite ends — one drains the substrate, one closes the exit — and share no production stack, no formulation stack, no regulatory pathway. Disulfiram is sub-AUD dose (see [comp-027 planned analysis](./computational-experiments.md)) so co-administration with ethanol-producing live biotherapeutics is bounded by the strain's residual ethanol output, not by the pill.

**Chokepoint(s) hit.** CP6 urate-disposal (PDB arm, upstream of NLRP3) + CP6b GSDMD pyroptotic-exit (disulfiram arm, downstream of NLRP3). *Pass 3 label correction (2026-05-15): the synthesizer's original framing "both branches of CP6" is tightened — urate-disposal is upstream of CP6 even though one wiki entry loosely labels PDB as CP6.*

**Chassis (both selected, neither pending).** PDB arm → engineered EcN LBP (entry 1 above, chassis option A). Disulfiram arm → compounding pharmacy track ([`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md)). Multi-chassis stack, not a chassis-pending question.

**Why this entry exists here.** The composition was almost not surfaced because neither arm is novel individually — both are documented in their respective canonical pages. The *stack* is what's new, and absent an explicit "compositions" index, multi-chassis stacks risk being lost in the gap between single-modality pages. Per [`synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md`](../synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md), stacks composed across chassis deserve the same chokepoint-first treatment as single interventions.

**Cheapest first move.** Two parallel comp-NNNs, both completed 2026-05-16:
- **[comp-027](./disulfiram-dose-modeling-computational.md)** — YELLOW-leaning-GREEN: narrow sub-AUD window centered on **100 mg/day** (range 75–125 mg/d), where parent DSF Cmax engages GSDMD pore-formation blockade at therapeutic levels (1.3× cell-free IC50) while Me-DTC stays at or below DER hypotension threshold. Compounding-pharmacy handoff: IR capsule for 14-day titration → ER lipid-matrix 100 mg QD chronic. Gout co-administration clean (allopurinol synergistic).
- **[comp-031](./dual-chassis-ecn-pdb-uricase-computational.md)** — YELLOW provisional: combined effect ~25–30% larger than PDB-alone (not 2–3× as naive sum predicts). **Critical engineering handoff: route PDB and uricase to SEPARATE strains, NOT a dual-cassette EcN** — substrate-competition for luminal urate means single-chassis dual-cassette gains ~nothing in additional urate consumption vs two separate strains co-administered. The butyrate-axis synergy (PDB → PPARγ/HDAC ABCG2 rescue) operates at the enterocyte nucleus from gut lumen — does NOT require co-localization at the bacterial scale. The M1 multi-chassis-stack framing here is correctly a two-strain combination probiotic, not a dual-cassette engineering target.

**Cross-reference.** [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) §"Companion intervention: compounded disulfiram"; [`disulfiram.md`](./disulfiram.md) §"Companion intervention: PDB-engineered EcN"; [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md); [`computational-experiments.md`](./computational-experiments.md) comp-027 + comp-031.

---

## Pending entries to triage into this list

These are interventions surfaced in the OE corpus that map to chokepoints but haven't yet been formalized as chassis-pending entries. Each warrants a short audit pass to confirm chassis-status:

- **Engineered exosomes** carrying NLRP3 inhibitors targeted to CD163+ macrophages — see [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md).
- **CRISPR / base editing in patient** for Q141K → Q141 in crypt stem cells — see [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md). Probably "delivery unsolved on a 5–10 year horizon" status.
- **Wearable / microneedle continuous UA monitoring** — not an intervention per se, but a monitoring tool that changes intervention-titration kinetics. Different shape; possibly belongs in a separate monitoring-pending page.
- **GSDMD pore-mediated self-delivery of OE-relevant biologics** (KPV / nanobodies / single SCR domains / IL-1RA — see [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md) §"Implication for OE biologics") — chassis-pending status: koji can produce the payloads; the chassis-question is the **delivery format** that gets the payload to the synovial fluid in time for the pore-opening window. Different chassis question than "what produces the molecule"; same general shape (real intervention, chassis open).
- **Engineered C1-INH (SERPING1, recombinant complement regulator) in LBP-luminal chassis** — promoted from "named-but-unscoped" to "next CP0 LBP engineering gate" by [comp-024](./computational-experiments.md) (2026-05-16). comp-024 ranked complestatin-family BGC heterologous expression as RED for LBP track (best host *E. coli* Nissle YELLOW 0.544; O₂-dependent NRPS tailoring chemistry incompatible with anaerobic-resident lifestyle) and surfaced C1-INH as GREEN-provisional 0.774 by comparison — single-axis problem (luminal-protease stability + glycosylation), testable via a comp-006-style protease-stability comp-NNN on SERPING1 in EcN-secreted format. **Sister-to-DAF SCR1-4** ([H05](./hypotheses/H05-daf-scr14-cp0-thesis.md)) — both are soluble human complement regulators expressed heterologously, both target CP0, but DAF SCR1-4 routes through koji secretion (engineered koji endgame strain) while C1-INH routes through LBP-luminal (engineered EcN). The two are mechanistically complementary: DAF accelerates convertase decay at the MSU crystal surface; C1-INH inactivates C1r/C1s + MASP-2 at the classical/lectin pathway entry point. Together they would cover convertase-formation (C1-INH) + convertase-disassembly (DAF) at two different cascade points and two different chassis. **Next move:** comp-NNN protease-stability + glycosylation feasibility for SERPING1 in EcN luminal-secreted format. Cross-reference: [comp-024](./computational-experiments.md), [`complestatin-bgc-lbp-feasibility-computational.md`](./complestatin-bgc-lbp-feasibility-computational.md), [`complement-c5a-gout.md`](./complement-c5a-gout.md), [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md).

---

## When an entry leaves this page

An entry migrates off this page when its chassis is selected. Two outflows:

1. **Chassis selected → new dedicated scope page in `wiki/`** — example: PDB selects engineered EcN as chassis → new `engineered-ecn-pdb-track.md` scope page with Phase 2 follow-ups, comp-NNN, falsification card. The entry on this page becomes a one-line pointer to the new track page.
2. **Chassis selected → folds into existing peer-track page** — example: a chassis-pending intervention turns out to be best-fit for the compounding pharmacy track → folds into [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md).

If an entry is **falsified** (chokepoint-fit turns out to be wrong, or mechanism doesn't survive scrutiny), it migrates to a falsification card or gets removed with a closure note. Falsification is OK; quiet filtering is not.

### How decisions actually get made — there's no static rubric, by design

There is intentionally **no static "promote / park / falsify" rubric** on this page (or anywhere else). The decision mechanism is the wiki sweep daemon's Pass 2 (synthesizer), which re-evaluates every entry against the current corpus state on every sweep cycle. When new information lands that would shift an entry's status — a new comp-NNN output, a new wet-lab result, a new published clinical-trial readout, a new chokepoint analysis — the next sweep surfaces it as a Connection / Contradiction / Experiment / Open Question / Priority Action. The walkthrough operator then makes the actual promote / park / falsify call per-item, with each call grounded in the corpus state at that moment.

A static rubric here would be a snapshot of heuristics that drifts from the live evaluator. Items 1–5 of the 2026-05-15 sweep walkthrough are concrete evidence the mechanism works as designed: the daemon surfaced promotion-worthy recommendations (PDB×disulfiram CP6 stack, CFTR-corrector Q141K chaperone, inhaled mRNA-IL-1RA temporal complement) from chassis-pending entries; the walkthrough operator decided per-item; the actions shipped without anyone ever consulting a documented rubric. The dynamic process IS the rubric implementation.

This is why "park" and "falsify" don't appear as named statuses in the entries above — the page records *interventions and their current chassis-question state*, not *decisions about resource allocation*. Decisions live in walkthrough closure annotations (`synthesis/done/`) and in the canonical wiki pages that come out of promotions. The chassis-pending page is the index of the open chokepoint-fit-without-chassis state, not the decision log.

## Maintenance

- Updated on any walk-synthesis closure where a finding hits a chokepoint but lacks a chassis (see closure question in `.claude/skills/walk-synthesis/SKILL.md`).
- Updated when the sweep daemon's Pass 2/3 review surfaces a chassis-expanding finding (see anti-chassis-filter language in `scripts/sweep-prompt-2-synthesize.md` and `scripts/sweep-prompt-3-review.md`).
- The strategic reflection in [`synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md`](../synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md) is the discipline anchor. The page itself is the operational manifestation of that discipline.
- The page is **not** a deprioritization queue. Entries here are real interventions waiting on a real next step — not "won't-fix" or "off-platform." Treat as active research, just on a different chassis track from the koji-engineering track.
