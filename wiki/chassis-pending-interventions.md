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
  - open-enzyme-vision.md
  - open-source-platform.md
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

**Cross-reference.** [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (CP5a × mRNA cell), [`delivery-route-matrix.md`](./delivery-route-matrix.md) (RNA platforms × inhaled cell).

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

**Cross-reference.** [`delivery-route-matrix.md`](./delivery-route-matrix.md), [`gout-kill-chain-delivery-routes.md`](./gout-kill-chain-delivery-routes.md), [`engineered-koji-protocol.md` §"The Hydrogen Peroxide Question — and why the chassis solves it for free"](./engineered-koji-protocol.md).

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

**Cheapest first move.** Two parallel comp-NNNs, both queued in [`computational-experiments.md`](./computational-experiments.md):
- **comp-027** (already planned): disulfiram dose modeling for GSDMD-blockade clinical efficacy vs. AUD-deterrent ceiling. Gates the compounded-pill arm.
- **comp-031** (new, queued by this entry): dual-chassis EcN additive SUA prediction — PDB cluster from CBT2.0 + PULSE-style uricase co-expression vs. PDB alone vs. uricase alone. Maps predicted additive serum urate reduction; also tests whether ABCG2 induction from PDB-butyrate compounds with the gut-lumen sink.

**Cross-reference.** [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) §"Companion intervention: compounded disulfiram"; [`disulfiram.md`](./disulfiram.md) §"Companion intervention: PDB-engineered EcN"; [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md); [`computational-experiments.md`](./computational-experiments.md) comp-027 + comp-031.

---

## Pending entries to triage into this list

These are interventions surfaced in the OE corpus that map to chokepoints but haven't yet been formalized as chassis-pending entries. Each warrants a short audit pass to confirm chassis-status:

- **Engineered exosomes** carrying NLRP3 inhibitors targeted to CD163+ macrophages — see [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md).
- **CRISPR / base editing in patient** for Q141K → Q141 in crypt stem cells — see [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md). Probably "delivery unsolved on a 5–10 year horizon" status.
- **Wearable / microneedle continuous UA monitoring** — not an intervention per se, but a monitoring tool that changes intervention-titration kinetics. Different shape; possibly belongs in a separate monitoring-pending page.
- **GSDMD pore-mediated self-delivery of OE-relevant biologics** (KPV / nanobodies / single SCR domains / IL-1RA — see [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md) §"Implication for OE biologics") — chassis-pending status: koji can produce the payloads; the chassis-question is the **delivery format** that gets the payload to the synovial fluid in time for the pore-opening window. Different chassis question than "what produces the molecule"; same general shape (real intervention, chassis open).

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
