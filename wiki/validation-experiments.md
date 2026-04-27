---
title: Validation Experiments
aliases: [experiments, validation, testing phases]
related: [engineered-yeast-uricase-proposal, engineered-koji-protocol, open-source-platform, supplements-stack]
sources: [engineered-yeast-uricase-proposal.md, engineered-koji-protocol.md, open-enzyme-vision.md, nlrp3-exploit-map.md, gout-deep-dive.md]
---

# Validation Experiments

## Overview

Single-source consolidated experiment library for the Open Enzyme project. The navigable queue/dashboard lives immediately below this overview; full protocols (purpose, protocol, cost, timeline, dependencies, success criteria) follow in the phase sections.

As of 2026-04-24 this is the authoritative experiments file — earlier ambiguity about a separate `experiments.md` has been resolved, and all content lives here. The sweep daemon and human editors update this page in place.

---

## Experiment Queue

Dashboard view of all 23 experiments in the library. Sorted by phase then ID. Detail lives in the phase sections below — click the ID to jump.

**Status legend:**
- **Proposed** — no work done yet; in the design/queue stage.
- **In Progress** — active work underway (wet-lab, self-experiment, or analysis).
- **Done** — completed with results captured in the protocol section or a referenced wiki page.
- **Abandoned** — deprioritized or replaced; reason noted inline.

As of 2026-04-24, all experiments are **Proposed** (Phase 0 — no wet-lab work has been executed yet; self-experiments have not started).

> **#1 priority gate (elevated 2026-04-27 per synthesis Pass 3 review):** [§1.9 Ward 1995 dual-cassette feasibility test](#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate--1-priority-gate) is the single gating experiment for the koji-endgame-strain thesis. If it fails, the single-strain endgame collapses to a two-strain co-fermentation fallback — significant operational consequences for dosing uniformity and home reproducibility. $3–5K / 8–12 weeks but extraordinarily high leverage given what it decides; should run before further investment in the single-strain architecture.

| ID | Title | Category | Cost | Weeks | Status | Wiki refs |
|----|-------|----------|------|-------|--------|-----------|
| [§1.1](#11-uricase-gene-performance-comparison) | Uricase gene performance comparison | In Vitro | $2,000–3,000 | 4–6 | Proposed | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [uricase-variant-selection](./uricase-variant-selection.md), [uricase](./uricase.md), [codon-optimization-expression-cassette](./codon-optimization-expression-cassette.md) |
| [§1.2](#12-secretion-vs-intracellular-expression) | Secretion vs. intracellular expression | In Vitro | $500–1,000 | 2–3 | Proposed | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [saccharomyces-cerevisiae](./saccharomyces-cerevisiae.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.3](#13-uricase-survival-in-beer-fermentation) | Uricase survival in beer fermentation | In Vitro | $200–400 | 3–4 | Proposed | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [saccharomyces-cerevisiae](./saccharomyces-cerevisiae.md) |
| [§1.4](#14-uricase-stability-after-drying) | Uricase stability after drying | In Vitro | $300–800 | 1–2 | Proposed | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.5](#15-koji-uricase-expression-and-activity) | Koji uricase expression and activity | In Vitro | $1,500–2,500 | 4–6 | Proposed | [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [koji-construct-design](./koji-construct-design.md), [uricase](./uricase.md) |
| [§1.6](#16-koji-enzyme-stability-at-digestive-ph-and-temperature) | Koji enzyme stability at digestive pH/temperature | In Vitro | $300–600 | 1–2 | Proposed | [engineered-koji-protocol](./engineered-koji-protocol.md), [gi-survival-prediction](./gi-survival-prediction.md), [digestive-enzymes](./digestive-enzymes.md) |
| [§1.7](#17-nlrp3-inflammasome-pathway-validation-thp-1-msu-macrophage-assay) | NLRP3 pathway validation (THP-1 MSU macrophage) | In Vitro | $5,000–8,000 | 8–10 | Proposed | [nlrp3-exploit-map](./nlrp3-exploit-map.md), [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md), [egcg](./egcg.md) |
| [§1.8](#18-egcg-dose-escalation-on-msu-stimulated-thp-1-tnfsf14-induced-il-6-readout-cp1a) | EGCG dose-escalation CP1a readout | In Vitro | $500–800 | 3–4 | Proposed | [egcg](./egcg.md), [tnfsf14-gout-target](./tnfsf14-gout-target.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) |
| [§1.9](#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate--1-priority-gate) | **Ward 1995 dual-cassette feasibility (koji endgame gate)** — **#1 priority** | In Vitro | $3,000–5,000 | 8–12 | Proposed | [koji-endgame-strain](./koji-endgame-strain.md), [lactoferrin](./lactoferrin.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md) |
| [§1.10](#110-heterologous-uricase-stability-in-shio-koji-salt-protease-ferment) | Heterologous uricase stability in shio-koji ferment (gates dual-use thesis) | In Vitro | $400–800 | 3–4 | Proposed | [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [synthesis](./synthesis.md) |
| [§2.1](#21-gnotobiotic-mouse-colonization-with-engineered-s-boulardii) | Gnotobiotic mouse colonization (S. boulardii) | Animal | $5,000–15,000 | 8–12 | Proposed | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [gut-lumen-sink](./gut-lumen-sink.md), [team](./team.md) |
| [§2.2](#22-hyperuricemic-rat-model-engineered-yeast-efficacy) | Hyperuricemic rat model (yeast efficacy) | Animal | $8,000–12,000 | 6–8 | Proposed | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [gout-deep-dive](./gout-deep-dive.md), [uricase](./uricase.md) |
| [§2.3](#23-engineered-koji-efficacy-in-digestive-enzyme-deficient-model) | Engineered koji EPI model | Animal | $6,000–10,000 | 8–10 | Proposed | [engineered-koji-protocol](./engineered-koji-protocol.md), [digestive-enzymes](./digestive-enzymes.md), [enzyme-deficit-deep-dive](./enzyme-deficit-deep-dive.md) |
| [§2.4](#24-nlrp3-inflammasome-inhibition-in-msu-crystal-arthritis-model) | NLRP3 inhibition in MSU arthritis model | Animal | $10,000–15,000 | 10–12 | Proposed | [nlrp3-exploit-map](./nlrp3-exploit-map.md), [nlrp3-inflammasome](./nlrp3-inflammasome.md), [gout-deep-dive](./gout-deep-dive.md), [supplements-stack](./supplements-stack.md) |
| [§2.5](#25-pulse-probiotic-validation-in-hyperuricemic-mice) | PULSE probiotic validation (hyperuricemic mice) | Animal | $5,000–8,000 | 8 | Proposed | [gout-deep-dive](./gout-deep-dive.md), [gout-clinical-pipeline](./gout-clinical-pipeline.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§3.1](#31-brian-engineered-yeast-uricase--serum-uric-acid--flare-tracking) | Brian: engineered yeast uricase tracking | Human | $200–400 | 20 | Proposed | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [self-experiment-protocol](./self-experiment-protocol.md), [open-enzyme-vision](./open-enzyme-vision.md) |
| [§3.2](#32-brian-nlrp3-inflammasome-suppression-stack--biomarker-panel) | Brian: NLRP3 suppression stack biomarker panel | Human | $700–1,400 | 20 | Proposed | [nlrp3-exploit-map](./nlrp3-exploit-map.md), [supplements-stack](./supplements-stack.md), [self-experiment-protocol](./self-experiment-protocol.md), [open-enzyme-vision](./open-enzyme-vision.md) |
| [§3.3](#33-lynn-wild-type-koji-digestive-enzyme-supplementation) | Lynn: wild-type koji digestive enzyme trial | Human | $600–1,000 | 12 | Proposed | [engineered-koji-protocol](./engineered-koji-protocol.md), [digestive-enzymes](./digestive-enzymes.md), [sibo](./sibo.md), [open-enzyme-vision](./open-enzyme-vision.md), [koji-home-fermentation](./koji-home-fermentation.md) |
| [§3.4](#34-joint-trial-engineered-koji-both-users) | Joint trial: engineered koji (both users) | Human | $300–500 | 14 | Proposed | [engineered-koji-protocol](./engineered-koji-protocol.md), [open-enzyme-vision](./open-enzyme-vision.md), [self-experiment-protocol](./self-experiment-protocol.md) |
| [§3.5](#35-biomarker-tracking-long-term-flare-prevention-brian-6-month-extension) | Long-term flare prevention (Brian, 6-mo extension) | Human | $400–600 | 26 | Proposed | [open-enzyme-vision](./open-enzyme-vision.md), [self-experiment-protocol](./self-experiment-protocol.md), [gout-deep-dive](./gout-deep-dive.md) |
| [§3.6](#36-brian-urinary-ltb4-assay--validating-quercetins-5-lox-cp6a-mechanism-in-vivo) | Brian: urinary LTB4 (quercetin CP6a in vivo) | Human | $150–300 | 12 | Proposed | [self-experiment-protocol](./self-experiment-protocol.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [synthesis](./synthesis.md) |
| [§3.7](#37-brian-serum-c5a-baseline--week-12--validating-cp0-complement-priming-status) | Brian: serum C5a baseline + week 12 (CP0) | Human | $300–400 | 12 | Proposed | [complement-c5a-gout](./complement-c5a-gout.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [self-experiment-protocol](./self-experiment-protocol.md) |
| [§3.8](#38-brian-dha-vs-epa-split-omega-3-crossover--resolving-the-gout-specific-spm-precursor-question) | Brian: DHA vs. EPA omega-3 crossover | Human | $550–700 | 9 | Proposed | [spm-resolution-pathway](./spm-resolution-pathway.md), [supplements-stack](./supplements-stack.md), [tnfsf14-gout-target](./tnfsf14-gout-target.md), [self-experiment-protocol](./self-experiment-protocol.md) |
| [§3.9](#39-brian-zileuton-off-label-trial--pharma-grade-cp6a-inhibition-in-flare-prevention-protocol) | Brian: zileuton off-label CP6a trial | Human | ~$500 | 16 | Proposed | [zileuton](./zileuton.md), [gout-clinical-pipeline](./gout-clinical-pipeline.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [self-experiment-protocol](./self-experiment-protocol.md) |

---

## Phase 1: In Vitro Validation

### 1.1 Uricase Gene Performance Comparison

**Status**: Proposed | **Cost**: $2,000–3,000 | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [uricase-variant-selection](./uricase-variant-selection.md), [uricase](./uricase.md), [codon-optimization-expression-cassette](./codon-optimization-expression-cassette.md)

**What it tests:** Which uricase gene (Aspergillus flavus, Candida utilis, or Vibrio vulnificus) performs best in S. cerevisiae?

**Proposed in:** engineered-yeast-uricase-proposal.md (§3)

**Protocol:**
- Order codon-optimized synthetic genes for all three candidates (*A. flavus*, *C. utilis*, *V. vulnificus*)
- Each in the same expression cassette (pTEF1 promoter, CYC1 terminator)
- Integrate at the same chromosomal locus in S. cerevisiae
- Compare: (a) expression level by Western blot, (b) specific uricase activity in cell lysate, (c) enzyme stability at 37°C over 24h

**Estimated cost:** $2,000–3,000 (gene synthesis ~$0.10/bp × ~900 bp × 3 genes + reagents)

**Estimated timeline:** 4–6 weeks

**Dependencies:** None

**Success criteria:** Identify highest-performing gene with >50 μmol/h/OD activity

---

### 1.2 Secretion vs. Intracellular Expression

**Status**: Proposed | **Cost**: $500–1,000 | **Weeks**: 2–3 | **Phase**: 1

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [saccharomyces-cerevisiae](./saccharomyces-cerevisiae.md), [gi-survival-prediction](./gi-survival-prediction.md)

**What it tests:** Should uricase be secreted into the medium or retained intracellularly?

**Proposed in:** engineered-yeast-uricase-proposal.md (§3)

**Protocol:**
- Clone A. flavus uaZ into two constructs: (1) with α-factor signal peptide for secretion, (2) without for intracellular accumulation
- Transform both into same yeast strain
- At 48h growth in liquid culture, draw samples and run uricase activity assay:
  - Supernatant (for secreted enzyme)
  - Cell pellet lysate (for intracellular enzyme)
- Compare total enzyme output, specific activity, and fraction secreted

**Estimated cost:** $500–1,000

**Estimated timeline:** 2–3 weeks

**Dependencies:** None (can be done in parallel with 1.1)

**Success criteria:** Identify format with highest bioavailable uricase in food product context

---

### 1.3 Uricase Survival in Beer Fermentation

**Status**: Proposed | **Cost**: $200–400 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [saccharomyces-cerevisiae](./saccharomyces-cerevisiae.md)

**What it tests:** Does uricase remain enzymatically active through beer fermentation?

**Proposed in:** engineered-yeast-uricase-proposal.md (§4)

**Protocol:**
- Brew 1-gallon test batch with engineered yeast
- At each stage—active fermentation (day 3), end of primary (day 7), after conditioning (day 14), after bottling (day 21)—draw samples
- Run uricase activity assay (spectrophotometric at 293 nm, measuring uric acid consumption)
- Control: purified uricase added to finished beer at same stages (distinguishes production from survival)

**Estimated cost:** $200–400 (homebrew supplies + uric acid assay reagents)

**Estimated timeline:** 3–4 weeks

**Dependencies:** Requires engineered yeast strain from Phase 1 optimization

**Success criteria:** Retain >30% activity through bottling (lower indicates degradation during fermentation)

---

### 1.4 Uricase Stability After Drying

**Status**: Proposed | **Cost**: $300–800 | **Weeks**: 1–2 | **Phase**: 1

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [gi-survival-prediction](./gi-survival-prediction.md)

**What it tests:** Can uricase survive lyophilization or heat drying for a shelf-stable product?

**Proposed in:** engineered-yeast-uricase-proposal.md (§4)

**Protocol:**
- Take concentrated pellet of engineered yeast, split into four aliquots:
  1. Fresh lysate (positive control)
  2. Freeze-dried/lyophilized pellet
  3. Heat-killed at 55°C then dried
  4. Spray-dried at 120°C inlet temperature
- Rehydrate each, lyse, and assay uricase activity
- Report as % activity retained vs. fresh lysate

**Estimated cost:** $300–800 (lyophilizer access via core facility)

**Estimated timeline:** 1–2 weeks

**Dependencies:** Requires engineered yeast strain from Phase 1 optimization

**Success criteria:** >40% activity retained via lyophilization for capsule formulation viability

---

### 1.5 Koji Uricase Expression and Activity

**Status**: Proposed | **Cost**: $1,500–2,500 | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [koji-construct-design](./koji-construct-design.md), [uricase](./uricase.md)

**What it tests:** Can A. flavus uricase gene express functionally in A. oryzae?

**Proposed in:** engineered-koji-protocol.md (§3, §5)

**Protocol:**
- Clone uaZ into engineered A. oryzae with PamyB promoter + SPamyB secretion signal + uaZ CDS + TtrpC terminator
- Grow on steamed rice (traditional koji conditions: 30°C, 48–72h)
- Harvest koji, prepare extract, assay uricase activity
- Compare: (a) expression level by Western blot, (b) specific uricase activity, (c) total enzyme yield per gram rice

**Estimated cost:** $1,500–2,500 (gene synthesis, transformation, reagents)

**Estimated timeline:** 4–6 weeks

**Dependencies:** None

**Success criteria:** >20 μmol/h/OD activity; enzyme properly secreted into rice substrate

---

### 1.6 Koji Enzyme Stability at Digestive pH and Temperature

**Status**: Proposed | **Cost**: $300–600 | **Weeks**: 1–2 | **Phase**: 1

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [gi-survival-prediction](./gi-survival-prediction.md), [digestive-enzymes](./digestive-enzymes.md)

**What it tests:** Does koji-produced uricase survive gastric and duodenal conditions?

**Proposed in:** engineered-koji-protocol.md (§6)

**Protocol:**
- Prepare koji extract with active uricase
- Expose to simulated gastric juice (pH 2.0, 37°C, pepsin) for 30 min
- Then simulated intestinal juice (pH 8.0, 37°C, pancreatin) for 120 min
- Assay uricase activity at each stage
- Compare to control uricase (Aspergillus nidulans uricase or rasburicase)

**Estimated cost:** $300–600 (digestive enzyme prep, assay reagents)

**Estimated timeline:** 1–2 weeks

**Dependencies:** Requires koji strain from 1.5

**Success criteria:** Retain >20% activity after duodenal transit (similar to ALLN-346 engineering target)

---

### 1.7 NLRP3 Inflammasome Pathway Validation (THP-1 MSU Macrophage Assay)

**Status**: Proposed | **Cost**: $5,000–8,000 | **Weeks**: 8–10 | **Phase**: 1

**Affected wiki**: [nlrp3-exploit-map](./nlrp3-exploit-map.md), [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md), [egcg](./egcg.md)

**What it tests:** Do proposed compounds in the [[supplements-stack]] actually inhibit NLRP3 at stated chokepoints?

**Proposed in:** nlrp3-exploit-map.md, gout-deep-dive.md

**Protocol:**
- Use macrophage cell line (**THP-1 differentiated with PMA** preferred over primary mouse macrophages — the species-gap caveat in [supplements-stack.md](./supplements-stack.md) makes human cells mandatory for translation)
- Prime with LPS (Signal 1: NF-κB priming)
- Expose to MSU crystals (NLRP3 trigger)
- Treat with individual compounds and read out in parallel
- Measure endpoints: IL-1β secretion (ELISA), caspase-1 activity, ASC specks (fluorescence), **IκBα retention (Western — mechanistic readout for proteasome-pathway inhibitors)**
- Compare dose-response and mechanistic target (which chokepoint affected)

**Priority compounds (ordered by information value of the specific mechanistic claim being tested):**

- **EGCG — highest-priority single-compound assay.** The mechanistic claim in [egcg.md](./egcg.md) (proteasome inhibition → IκBα stabilization → unified CP1 + CP1a + CP4 + CP5a coverage) is specific and testable. Readouts: IL-1β ELISA + **Western for IκBα retention** + TNFSF14-induced IL-6 in HGF co-culture (tests CP1a). If the proteasome mechanism is correct, EGCG should show a steeper dose-response than quercetin or ursolic acid at equimolar concentrations, and IκBα retention should track the proteasome IC50 (86 nM cellular) rather than the reported IKK IC50 (≥10 μM). Phytosome-formulated EGCG recommended alongside free EGCG to test the bioavailability-gated translation question. This brings a falsifiable mechanistic claim to a format that can actually falsify it.
- **Oridonin** — direct NLRP3 NACHT Cys279 covalent binder; 5.18 μM human THP-1 IC50 per ChEMBL. Tests whether the curated human IC50 replicates in our hands.
- **BHB** — tests direct NLRP3 K⁺-efflux-block mechanism; straightforward positive-control-class compound.
- **Sulforaphane** — Nrf2 activator; tests whether the Nrf2/NF-κB crosstalk mechanism translates to MSU-triggered cells at achievable sub-μM doses.
- **Quercetin** — now primarily a CP6a (5-LOX) compound; tests whether the weaker NF-κB/NLRP3 claim holds at μM concentrations.
- **Carnosine + Lactoferrin** — unique mechanism classes (dual UA/NLRP3 and CP5 GSDMD-axis respectively); tests whether the rat/murine evidence translates to human THP-1.

**Estimated cost:** $5,000–8,000 (cell culture, cytokines, assay kits, Western reagents, compound panel)

**Estimated timeline:** 8–10 weeks (larger compound panel than original scope)

**Dependencies:** None

**Success criteria:** 
- Confirm >50% IL-1β reduction at stated compound doses; validate chokepoint targets
- **EGCG-specific:** dose-response for IκBα retention tracks the 86 nM proteasome IC50 (falsifies or confirms the proteasome-pathway reframe); dose-response is steeper than quercetin at equimolar (confirms mechanistic difference between direct-proteasome and NF-κB-pathway-modulator compounds)

---

### 1.8 EGCG Dose-Escalation on MSU-Stimulated THP-1: TNFSF14-Induced IL-6 Readout (CP1a)

**Status**: Proposed | **Cost**: $500–800 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [egcg](./egcg.md), [tnfsf14-gout-target](./tnfsf14-gout-target.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md)

**What it tests:** Does EGCG suppress TNFSF14-induced IL-6 in a gout-relevant cell model at sub-μM concentrations — the specific CP1a readout that would validate EGCG's multi-chokepoint coverage story?

**Proposed in:** `wiki/synthesis.md` 2026-04-24 Pass 2 Proposed Experiments #3; complements Experiment 1.7 (NLRP3 pathway validation) with a TNFSF14-specific readout.

**Protocol:**
- THP-1 monocytes differentiated to macrophages with PMA (25 ng/mL, 24h, then rest 24h)
- Prime with LPS (10 ng/mL, 4h — Signal 1)
- Expose to MSU crystals (100 μg/mL, 6h — Signal 2)
- Add recombinant TNFSF14/LIGHT (100 ng/mL, 16h) to stimulate the CP1a axis specifically
- Treat with EGCG dose-escalation: 10 nM, 30 nM, 100 nM, 300 nM, 1 μM, 3 μM, 10 μM (spans the 86 nM proteasome IC50)
- Positive control: bortezomib (proteasome inhibitor, orthogonal mechanism)
- Negative control: DMSO vehicle
- Primary readout: IL-6 in supernatant (ELISA)
- Secondary readouts: IL-1β (ELISA), IκBα retention (Western blot), HVEM receptor surface expression (flow cytometry)

**Estimated cost:** $500-800 (THP-1 cells, PMA, LPS, MSU, recombinant TNFSF14, EGCG, ELISA kits for IL-6 and IL-1β, Western reagents)

**Estimated timeline:** 3-4 weeks (cell differentiation, assay, readouts)

**Dependencies:** None (can run in parallel with 1.7, or as a focused follow-up)

**Success criteria:**
- IL-6 suppression ≥50% at EGCG ≤1 μM (confirms CP1a activity at achievable concentrations)
- Dose-response for IκBα retention tracks the 86 nM proteasome IC50 (falsifies or confirms the proteasome-pathway reframe of EGCG's mechanism)
- HVEM downregulation at EGCG ≤1 μM (replicates Hosokawa 2010 HGF finding in a macrophage lineage)

**Cross-references:** `wiki/egcg.md` (mechanistic reframe), `wiki/tnfsf14-gout-target.md` (CP1a chokepoint), `wiki/nlrp3-exploit-map.md` (CP1a entry)

---

### 1.9 Ward 1995 Dual-Cassette Feasibility Test (Koji Endgame Strain Gate) — #1 priority gate

**Status**: Proposed | **Cost**: $3,000–5,000 | **Weeks**: 8–12 | **Phase**: 1

**Affected wiki**: [koji-endgame-strain](./koji-endgame-strain.md), [lactoferrin](./lactoferrin.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [uricase-variant-selection](./uricase-variant-selection.md)

**What it tests:** Can the Ward 1995 *A. awamori* glucoamylase-KEX2 lactoferrin architecture (>2 g/L submerged, PMID 9634791) be layered with a second expression cassette for *A. flavus* uricase (*uaZ*) in the same *A. oryzae* genetic background on solid-state rice koji — without silencing either cassette or collapsing the native kojic-acid / ergothioneine metabolite program? This is the single feasibility gate for the endgame strain thesis (one *A. oryzae* strain, 5 NLRP3-pathway chokepoints, 4 molecules — see [koji-endgame-strain.md](./koji-endgame-strain.md)).

**Proposed in:** `wiki/synthesis.md` 2026-04-24 Pass 2 Connection 1 + Proposed Experiment 1; formalized in [koji-endgame-strain.md](./koji-endgame-strain.md) §3. This is the gating experiment that decides whether the endgame strain is engineerable in its one-strain form (go to full development) or needs the two-strain fallback ([koji-endgame-strain.md](./koji-endgame-strain.md) §4.1).

**Protocol:**
- **Construct design.**
  - Cassette A (lactoferrin): `[PamyB — glucoamylase — KEX2site (Lys-Arg) — hLf codon-optimized for *A. oryzae* — TamyB]`. Matches Ward 1995 architecture. Selection marker: pyrG complementation.
  - Cassette B (uricase): `[PTEF1 — amyB signal peptide — *A. flavus uaZ* codon-optimized — TgpdA]`. Distinct promoter (constitutive TEF1) to separate transcriptional program from Cassette A. Selection marker: niaD or amdS.
- **Host strain.** *A. oryzae* RIB40 or NSAR1 (pyrG-deficient auxotroph).
- **Transformation.** PEG/CaCl₂ protoplast, sequential: Cassette A first → select on pyrG-minus → confirm hLf expression by Western → transform Cassette B into validated hLf clone → select on niaD/amdS.
- **Fermentation.** Solid-state rice koji, 48–60 h at 30°C, 35% moisture. Parallel submerged-culture control (100 mL shake flask, 28°C) to isolate solid-state variable.
- **Readouts.**
  - Uricase activity: spectrophotometric UA-disappearance assay (per [engineered-koji-protocol.md](./engineered-koji-protocol.md) §05).
  - Lactoferrin titer: anti-hLf ELISA + Western blot.
  - Iron-binding capacity of Lf: UV-Vis at 465 nm (apo-vs-holo); optional CD spectroscopy for fold confirmation.
  - Native metabolite profile: kojic acid titer (HPLC) + ergothioneine titer (LC-MS) — is WT baseline preserved within 30%?
  - qPCR for both cassette copy numbers (stability check).
  - SDS-PAGE to detect any incompletely-processed glucoamylase-hLf fusion (KEX-2 saturation signal).

**Estimated cost:** $3,000–5,000 — gene synthesis for two codon-optimized cassettes (~$600–1,000), cloning and transformation reagents ($500–1,000), fermentation consumables ($200–400), ELISA + Western antibodies ($800–1,200), metabolite assay reagents ($500–800), CRO or academic lab time if outsourced ($1,000–2,000 per batch).

**Estimated timeline:** 8–12 weeks — 2–3 weeks gene synthesis + construct assembly, 2–3 weeks sequential transformation + clonal screening, 1–2 weeks parallel fermentation (solid-state + submerged), 2–3 weeks full assay suite + write-up.

**Dependencies:** *A. oryzae* genetic-engineering lab access. Candidate pathways: (a) Lauren Collier-Hyams at Emory (see [team.md](./team.md)) if the recruiting conversation converts her to active collaboration; (b) commercial CRO specializing in filamentous-fungus engineering (Lonza, Novozymes, Dyadic) — faster but more expensive; (c) community biolab with protoplast-transformation capability (Genspace NY has precedent on *A. oryzae*).

**Success criteria:**
- **Accept** (go to full endgame strain development per [koji-endgame-strain.md](./koji-endgame-strain.md) §7): lactoferrin titer ≥500 mg/L koji pore-fluid equivalent, uricase activity ≥50 μmol/h/OD retained from single-cassette baseline, native kojic acid + ergothioneine titers within 30% of WT.
- **Iterate** (adjust architecture, re-test): lactoferrin 100–500 mg/L OR uricase activity down >30%. Try protease-knockout host strain (Δalp, Δnpr), alternative integration sites, iron supplementation (10–100 ppm FeCl₃), or alternative signal peptides.
- **Reject** (fall back to two-strain co-ferment per [koji-endgame-strain.md](./koji-endgame-strain.md) §4.1): lactoferrin <100 mg/L after two rounds of optimization, OR native metabolite program collapse (kojic acid down >50% vs. WT). The two-strain fallback preserves the coverage matrix at the cost of single-strain elegance.

**Cross-references:** [koji-endgame-strain.md](./koji-endgame-strain.md) §3 (full protocol rationale + adjacent literature: Li 2024 PMID 39830075 multi-copy in *A. oryzae*, Wang 2023 PMID 37807677 multi-locus in *A. niger*), [engineered-koji-protocol.md](./engineered-koji-protocol.md) §16 (starting single-cassette lactoferrin module that this experiment ladders on top of), [lactoferrin.md](./lactoferrin.md) §7 (Open Enzyme feasibility bet), [synthesis.md](./synthesis.md) 2026-04-24 Connection 1.

---

### 1.10 Heterologous Uricase Stability in Shio-Koji Salt-Protease Ferment

**Status**: Proposed | **Cost**: $400–800 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [synthesis](./synthesis.md)

**What it tests:** Does the 7–14 day shio-koji salt-protease ferment degrade engineered uricase produced by *A. oryzae*? Shio-koji's hallmark feature is active native subtilisin-family proteases at room temperature in 15–20% NaCl — this likely degrades any heterologous peptide payload (carnosine, KPV, BPC-157 — Connection #2 in synthesis 2026-04-27) and may plausibly degrade folded enzymes like uricase too, despite uricase being a ~34 kDa tetrameric folded protein with reasonable intrinsic stability. Resolves the "single highest-stakes open question for the shio-koji dual-use thesis" per Pass 3 review.

**Proposed in:** `wiki/synthesis.md` 2026-04-27 Open Question #2 (sweep on commit `b7df491`). Gates the dual-use product concept that unifies the two project arms (Lynn's EPI track + Brian's gout track) into a single household condiment ([engineered-koji-protocol.md](./engineered-koji-protocol.md) §15).

**Protocol:**
- **Construct:** Use [engineered-koji-protocol.md](./engineered-koji-protocol.md) §6 single-cassette uricase strain. If engineered strain not yet available, run pilot with WT *A. oryzae* spiked with rasburicase as positive control at physiologically-relevant concentration.
- **Ferment matrix:** Prepare shio-koji per [koji-home-fermentation.md](./koji-home-fermentation.md) standard protocol (15–20% NaCl, room temp 22–25°C). Run in parallel with two control matrices: (a) freshly harvested koji (no salt ferment), (b) amazake-style brief warm hold (55–60°C × 6h followed by RT storage) — heat hold partially inactivates proteases.
- **Time-course sampling:** Aliquot at days 0, 3, 7, 10, 14. Freeze at −80 °C immediately after collection.
- **Readouts:**
  - Uricase activity: spectrophotometric UA-disappearance assay at 293 nm per [engineered-koji-protocol.md](./engineered-koji-protocol.md) §05 (quantitative).
  - SDS-PAGE + anti-uricase Western blot: detects intact monomer (~34 kDa) vs. degradation products. Distinguishes "lost activity due to denaturation" from "lost activity due to proteolytic cleavage."
  - Optional CD spectroscopy on extracted uricase: confirms tetramer fold preservation, useful if activity drops without obvious cleavage on Western.
- **Salt-concentration sub-experiment:** Single-timepoint (day 7) panel at 5%, 10%, 15%, 20% NaCl. Determines the salt threshold at which protease activity drops faster than uricase stability — informs whether a low-salt shio-koji variant could preserve the dual-use format.

**Estimated cost:** $400–800 — uricase activity assay reagents ($100–200), SDS-PAGE / Western antibodies and reagents ($200–400), shio-koji ingredients ($20–50), CD spectroscopy if outsourced ($100–200).

**Estimated timeline:** 3–4 weeks — parallel with the active fermentation. Day-by-day sampling continues over the 14-day window; assay batches at days 0/3/7/10/14 are ~2 days each.

**Dependencies:** No specialized lab access required beyond Western blot capability. Doable in a community biolab (Genspace NY, Counter Culture Labs Oakland) or as a small parallel run during the §1.9 Ward 1995 cassette work. Self-contained.

**Success criteria:**
- **Accept dual-use thesis** (engineer for shio-koji delivery is viable): >70% uricase activity retained at day 14 vs. day 0; intact monomer band on Western; no major degradation products.
- **Iterate** (try lower-salt or shorter-ferment formats): 30–70% retention. Document the salt-time tradeoff and propose a modified format (e.g., shio-koji variant at 10% NaCl × 7 days).
- **Reject shio-koji as a delivery format for uricase** (fall back to fresh koji, amazake, or lyophilized powder per synthesis 2026-04-27 Connection #2 review): <30% retention. Same logic extends to any peptide payload (carnosine, KPV, BPC-157).

**Cross-references:** [synthesis.md](./synthesis.md) 2026-04-27 Open Question #2 + Connection #2; [engineered-koji-protocol.md](./engineered-koji-protocol.md) §15 (the dual-use proposal this experiment gates); [koji-home-fermentation.md](./koji-home-fermentation.md) (shio-koji standard protocol); [aspergillus-oryzae.md](./aspergillus-oryzae.md) (native protease characterization).

---

## Phase 2: Animal Model Validation

### 2.1 Gnotobiotic Mouse Colonization with Engineered S. boulardii

**Status**: Proposed | **Cost**: $5,000–15,000 | **Weeks**: 8–12 | **Phase**: 2

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [gut-lumen-sink](./gut-lumen-sink.md), [team](./team.md)

**What it tests:** Can engineered probiotic yeast survive and function in the mouse gut? What dosing is needed?

**Proposed in:** engineered-yeast-uricase-proposal.md (§4.d)

**Protocol:**
- Colonize germ-free mice with engineered S. boulardii expressing uricase
- Measure:
  - Fecal yeast counts daily for 14 days (CFU/g)
  - Fecal and cecal uricase activity assay
  - Serum uric acid in Uox-knockout mice (or potassium oxonate-hyperuricemic model)
- Compare: engineered strain vs. wild-type S. boulardii vs. untreated controls

**Estimated cost:** $5,000–15,000 (gnotobiotic mouse facility time, staff, housing, assays)

**Estimated timeline:** 8–12 weeks

**Dependencies:** 
- Requires optimized S. boulardii uricase strain from Phase 1
- Requires access to a gnotobiotic facility — ideally Rheinallt Jones's Emory Gnotobiotic Animal Core, if he joins as a collaborator

**Success criteria:** 
- Maintain >10⁶ CFU/mL fecal yeast counts through day 7
- Achieve measurable cecal uricase activity
- Reduce serum uric acid by ≥20% vs. controls

---

### 2.2 Hyperuricemic Rat Model: Engineered Yeast Efficacy

**Status**: Proposed | **Cost**: $8,000–12,000 | **Weeks**: 6–8 | **Phase**: 2

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [gout-deep-dive](./gout-deep-dive.md), [uricase](./uricase.md)

**What it tests:** Does oral administration of engineered yeast reduce systemic uric acid in a whole-organism model?

**Proposed in:** engineered-yeast-uricase-proposal.md (§5)

**Protocol:**
- Induce hyperuricemia in Sprague-Dawley rats using oxonic acid + allopurinol (standard model)
- Administer engineered yeast strain (lyophilized powder in capsules) daily for 14 days at varying doses
- Measure:
  - Serum uric acid (HPLC or uricase-catalase assay)
  - Urinary uric acid excretion (24h collection)
  - Fecal uric acid (as proxy for gut lumen degradation)
  - Kidney function markers (BUN, creatinine)
- Compare: treated vs. vehicle control vs. allopurinol positive control

**Estimated cost:** $8,000–12,000 (animal costs, housing, blood assays, LC-MS analysis)

**Estimated timeline:** 6–8 weeks

**Dependencies:** Requires Phase 1 optimization of yeast strain

**Success criteria:** 
- Achieve serum uric acid reduction of ≥30% vs. vehicle
- Increase fecal uric acid by ≥50% vs. vehicle
- Non-inferior to allopurinol in serum uric acid reduction

---

### 2.3 Engineered Koji Efficacy in Digestive Enzyme-Deficient Model

**Status**: Proposed | **Cost**: $6,000–10,000 | **Weeks**: 8–10 | **Phase**: 2

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [digestive-enzymes](./digestive-enzymes.md), [enzyme-deficit-deep-dive](./enzyme-deficit-deep-dive.md)

**What it tests:** Does engineered koji effectively supplement digestive enzymes in vivo?

**Proposed in:** engineered-koji-protocol.md

**Protocol:**
- Use pancreatic lipase knockout mice (or pancreatectomized mice as EPI model)
- Administer koji fermented on rice (whole food) as supplement (10% dietary w/w) for 14 days
- Measure:
  - Fat absorption (coefficient of fecal fat; <7g/day = normal)
  - Protein digestion (fecal nitrogen)
  - Starch digestion (breath hydrogen test)
  - Intestinal inflammation markers (fecal calprotectin)
- Compare: engineered koji vs. wild-type koji vs. no supplement vs. commercial enzyme supplement (Creon)

**Estimated cost:** $6,000–10,000 (genetically modified mice, housing, specialized assays)

**Estimated timeline:** 8–10 weeks

**Dependencies:** Requires koji strain from Phase 1

**Success criteria:** 
- Normalize fat absorption to >92% (vs. <50% in untreated EPI)
- Non-inferior to commercial enzyme supplement

---

### 2.4 NLRP3 Inflammasome Inhibition in MSU Crystal Arthritis Model

**Status**: Proposed | **Cost**: $10,000–15,000 | **Weeks**: 10–12 | **Phase**: 2

**Affected wiki**: [nlrp3-exploit-map](./nlrp3-exploit-map.md), [nlrp3-inflammasome](./nlrp3-inflammasome.md), [gout-deep-dive](./gout-deep-dive.md), [supplements-stack](./supplements-stack.md)

**What it tests:** Do proposed NLRP3 inhibitor compounds reduce gout flare severity in vivo?

**Proposed in:** nlrp3-exploit-map.md, gout-deep-dive.md

**Protocol:**
- Induce acute gout in C57BL/6 mice by intra-articular MSU crystal injection into knee
- Treat with compounds or combinations:
  - Individual compounds (BHB via ketogenic diet, oridonin oral gavage, sulforaphane)
  - Multi-compound stack (BHB + oridonin + sulforaphane)
  - Positive control: colchicine
  - Negative control: vehicle
- Measure:
  - Joint swelling (calipers measurement, MRI)
  - Pain behavior (weight bearing on affected limb, mechanical hyperalgesia)
  - Inflammatory cytokines in joint lavage (IL-1β, TNF-α, IL-6 by multiplex assay)
  - Histology: neutrophil infiltration, synovial inflammation score
- Timeline: measure at 4h, 24h, 48h, 72h post-injection

**Estimated cost:** $10,000–15,000 (transgenic mice, surgical arthritis induction, imaging, cytokine assays)

**Estimated timeline:** 10–12 weeks (including 2-week ketogenic diet adaptation)

**Dependencies:** Requires Phase 1 validation of NLRP3 pathway

**Success criteria:**
- Reduce peak joint swelling by ≥40% vs. vehicle
- Reduce joint IL-1β by ≥50% vs. vehicle
- Reduce neutrophil infiltration by ≥30% vs. vehicle

---

### 2.5 PULSE Probiotic Validation in Hyperuricemic Mice

**Status**: Proposed | **Cost**: $5,000–8,000 | **Weeks**: 8 | **Phase**: 2

**Affected wiki**: [gout-deep-dive](./gout-deep-dive.md), [gout-clinical-pipeline](./gout-clinical-pipeline.md), [gut-lumen-sink](./gut-lumen-sink.md)

**What it tests:** Can PULSE system (urate-responsive engineered E. coli) maintain uric acid homeostasis?

**Proposed in:** gout-deep-dive.md (Section 8)

**Protocol:**
- Colonize Uox-knockout mice with PULSE engineered E. coli Nissle 1917
- Administer at varying doses and dosing frequencies (daily vs. every 3 days)
- Measure:
  - Fecal E. coli counts and uric acid-responsive biosensor activity (reporter assay)
  - Serum uric acid over 28 days (weekly measurements)
  - Response to acute uric acid challenge (potassium oxonate injection)
  - Off-target metabolite accumulation (allantoin, oxaluric acid)
- Compare: PULSE vs. wild-type E. coli Nissle vs. untreated controls

**Estimated cost:** $5,000–8,000 (transgenic mice, E. coli handling, weekly blood draws, biomarker assays)

**Estimated timeline:** 8 weeks

**Dependencies:** Requires PULSE strain (Source: Cell Reports Medicine 2025 reference)

**Success criteria:**
- Maintain serum uric acid within 2.0–4.0 mg/dL range (homeostatic)
- Self-regulate in response to acute uric acid load
- Clear allantoin without accumulation

---

## Phase 3: Human Self-Experimentation and Biomarker Tracking

### 3.1 Brian: Engineered Yeast Uricase — Serum Uric Acid & Flare Tracking

**Status**: Proposed | **Cost**: $200–400 | **Weeks**: 20 | **Phase**: 3

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [self-experiment-protocol](./self-experiment-protocol.md), [open-enzyme-vision](./open-enzyme-vision.md)

**What it tests:** Does daily oral engineered yeast reduce serum uric acid and gout flare frequency in the primary user?

**Proposed in:** engineered-yeast-uricase-proposal.md (§5), open-enzyme-vision.md (§8)

**Protocol:**
- Brian (primary user with gout) takes engineered yeast supplement daily
- Baseline: 4 weeks pre-intervention (establish flare frequency, serum urate baseline)
- Intervention: 12 weeks daily supplementation with engineered yeast (dose TBD from animal studies)
- Biomarkers measured weekly:
  - Serum uric acid (HPLC or uricase-catalase assay)
  - Inflammatory markers (CRP, IL-6 if available)
  - Gout flare frequency and severity (patient-reported, validated scale)
  - Tissue urate (tophi size if present, via ultrasound)
- Control: 4-week washout period after intervention

**Estimated cost:** $200–400 (blood assays, home kit supplies)

**Estimated timeline:** 20 weeks (4 baseline + 12 intervention + 4 washout)

**Dependencies:** 
- Requires Phase 1 & 2 validation
- Requires medical oversight (likely rheumatologist or primary care)

**Success criteria:**
- Reduce serum uric acid by ≥15% vs. baseline
- Reduce flare frequency by ≥50% vs. baseline period
- No adverse events

---

### 3.2 Brian: NLRP3 Inflammasome Suppression Stack — Biomarker Panel

**Status**: Proposed | **Cost**: $700–1,400 | **Weeks**: 20 | **Phase**: 3

**Affected wiki**: [nlrp3-exploit-map](./nlrp3-exploit-map.md), [supplements-stack](./supplements-stack.md), [self-experiment-protocol](./self-experiment-protocol.md), [open-enzyme-vision](./open-enzyme-vision.md)

**What it tests:** Does the multi-compound NLRP3 stack reduce inflammatory markers and flare severity?

**Proposed in:** nlrp3-exploit-map.md, open-enzyme-vision.md (§9)

**Protocol:**
- Brian takes NLRP3 suppression stack (BHB/exogenous ketones + KPV nasal spray + BPC-157 nasal spray + sulforaphane + oridonin + omega-3 + NAC, dosed per [[supplements-stack]])
- Baseline: 4 weeks pre-intervention
- Intervention: 12 weeks daily stack
- Biomarkers measured weekly:
  - Serum IL-1β (high-sensitivity ELISA)
  - Serum CRP, calprotectin, and fibrinogen
  - Blood ketone bodies (BHB) if using exogenous ketones
  - Joint pain (VAS scale, validated)
  - Gout flare frequency
- Control: 4-week washout post-intervention

**Estimated cost:** $300–600 (supplement costs) + $400–800 (blood assays)

**Estimated timeline:** 20 weeks

**Dependencies:**
- Requires Phase 1 NLRP3 pathway validation
- Can run in parallel with 3.1 (same subject, complementary endpoints)
- Requires medical oversight

**Success criteria:**
- Reduce IL-1β by ≥30% vs. baseline
- Reduce CRP by ≥25% vs. baseline
- Reduce flare frequency by ≥40% vs. baseline

---

### 3.3 Lynn: Wild-Type Koji Digestive Enzyme Supplementation

**Status**: In Progress (PERT-timing phase active 2026-04-19 → present) | **Cost**: $600–1,000 | **Weeks**: 12 | **Phase**: 3

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [digestive-enzymes](./digestive-enzymes.md), [sibo](./sibo.md), [open-enzyme-vision](./open-enzyme-vision.md), [koji-home-fermentation](./koji-home-fermentation.md), [digestive-enzyme-optimization](./digestive-enzyme-optimization.md)

**What it tests:** Does traditional koji effectively supplement digestive enzymes in EPI/SIBO?

**Proposed in:** engineered-koji-protocol.md, open-enzyme-vision.md (§4); practical protocol in [koji-home-fermentation.md](./koji-home-fermentation.md) (koji-kin → koji rice → shio-koji / amazake). (source: koji-home-fermentation.md)

**Interim findings — PERT-timing sub-experiment (2026-04-19 → present, ~30 meals tracked):**
A structured self-experiment on BoulderBio (wild-type *A. oryzae* OTC, 40,000 FIP lipase per capsule) dose and timing has been running in parallel. **Evidence level: Clinical n=1, single subject, unblinded, uncontrolled. Suggestive only.** (source: digestive-enzyme-optimization.md)
- 1 cap at first bite (label-default): insufficient for any meal >15 g fat.
- **2 caps at first bite**: markedly improved; 2026-04-25 breakfast produced a clear decoupling of liquid-stool from pain against a long-stable baseline — a meaningful efficacy signal for the platform's mechanism of action even before any engineering.
- **1+1 split** (1 cap at first bite + 1 at ~10 min): successful for >25 g fat meals.
- Pre-emptive enzyme during long cooking sessions: cooking-and-tasting = small-meal eating; enzyme at start of cook prevented pre-dinner symptom buildup.
- **Working dose framework (n=1):** <5 g fat → no enzyme; 15–25 g fat → 2 caps at first bite; >25 g fat or extended eating → 1+1 split; long cook-and-taste → 1 cap at start.
- **Confound flagged:** Lying flat <90 min post-meal is a strong contributor to overnight episodes; must be controlled separately from enzyme-dose effects.
- **Tolerability:** No adverse reactions across 30+ meals; no allergic response.
- **Implication for protocol:** The formal koji trial should use 2-cap-equivalent dosing (not label-default 1 cap) as the comparator, and should track fat content per meal as a covariate. Split-dose arm should be included for high-fat meals.

**Protocol:**
- Lynn (EPI/SIBO patient) takes traditional koji fermented on rice daily; shio-koji marinade is the highest-leverage format for EPI (pre-digests protein in marinade phase before food reaches the eater; see [koji-home-fermentation.md §Stage 2A](./koji-home-fermentation.md)) (Mechanistic Extrapolation; source: koji-home-fermentation.md)
- Baseline: 2 weeks pre-intervention (establish GI symptom baseline, stool frequency/consistency)
- Intervention: 8 weeks daily koji consumption (10–20g dried koji powder or equivalent rice koji)
- Biomarkers measured weekly:
  - GI symptom score (abdominal pain, bloating, diarrhea on validated scale)
  - Stool frequency, consistency (Bristol Scale)
  - Fat absorption assessment (72h fecal fat collection or non-invasive fat absorption test)
  - Inflammatory markers: fecal calprotectin, serum CRP
  - Microbiome composition (stool 16S rRNA at baseline, week 4, week 8 if budget allows)
- Crossover: 2-week washout, then repeat with engineered koji (once available from Phase 1)

**Estimated cost:** $200–400 (koji ingredients, fecal tests) + $400–600 (optional microbiome analysis)

**Estimated timeline:** 12 weeks

**Dependencies:**
- Requires wild-type koji protocol
- Once Phase 1 complete, can compare vs. engineered koji

**Success criteria:**
- Reduce abdominal pain/bloating score by ≥50% vs. baseline
- Normalize stool frequency to 1–2× daily
- Reduce fecal calprotectin by ≥30% (if elevated at baseline)

---

### 3.4 Joint Trial: Engineered Koji (Both Users)

**Status**: Proposed | **Cost**: $300–500 | **Weeks**: 14 | **Phase**: 3

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [open-enzyme-vision](./open-enzyme-vision.md), [self-experiment-protocol](./self-experiment-protocol.md)

**What it tests:** Does engineered koji providing both digestive enzymes and uricase work as a dual-purpose therapeutic food?

**Proposed in:** engineered-koji-protocol.md, open-enzyme-vision.md (§4, dual-enzyme vision)

**Protocol:**
- Both Brian and Lynn take engineered koji daily for 12 weeks
- Brian measures:
  - Serum uric acid, gout flare frequency (as in 3.1)
  - GI tolerance (stool frequency, abdominal symptoms)
- Lynn measures:
  - GI symptom score, stool characteristics (as in 3.3)
  - Serum uric acid (as secondary endpoint; she may have mild hyperuricemia)
  - Inflammatory markers
- Both:
  - Palatability/adherence assessment
  - Adverse event monitoring
  - Serum inflammatory panel (CRP, IL-6)

**Estimated cost:** $300–500 (koji production, bioassays)

**Estimated timeline:** 14 weeks (2 week prep + 12 week trial)

**Dependencies:** 
- Requires Phase 1 completion of engineered koji with both enzyme activities validated
- Requires both 3.1 and 3.3 baseline data for comparison

**Success criteria:**
- Brian: ≥15% reduction serum uric acid, ≥50% reduction flare frequency
- Lynn: ≥50% improvement GI symptoms, normalized stool, ≥30% reduction fecal calprotectin
- Both: tolerate koji at therapeutic doses with >80% adherence
- No safety signals in 12-week course

---

### 3.5 Biomarker Tracking: Long-term Flare Prevention (Brian, 6-month extension)

**Status**: Proposed | **Cost**: $400–600 | **Weeks**: 26 | **Phase**: 3

**Affected wiki**: [open-enzyme-vision](./open-enzyme-vision.md), [self-experiment-protocol](./self-experiment-protocol.md), [gout-deep-dive](./gout-deep-dive.md)

**What it tests:** Does uricase supplementation provide sustained reduction in gout flares?

**Proposed in:** open-enzyme-vision.md (§8)

**Protocol:**
- After Phase 3.1 completes successfully, continue engineered yeast supplementation for additional 6 months
- Measure monthly:
  - Serum uric acid
  - Gout flare frequency and severity
  - Tophi size (if present, ultrasound at months 1, 3, 6)
  - Joint function/mobility scores
  - Adherence and side effect monitoring

**Estimated cost:** $400–600 (monthly blood assays, ultrasound imaging)

**Estimated timeline:** 6 months

**Dependencies:** Requires successful completion and validation of Phase 3.1

**Success criteria:**
- Sustain serum uric acid reduction over 6-month period
- Maintain ≥40% reduction in flare frequency from baseline
- No tophi growth; ideally small reduction in tophi size
- Continued >80% adherence

---

### 3.6 Brian: Urinary LTB4 Assay — Validating Quercetin's 5-LOX (CP6a) Mechanism In Vivo

**Status**: Proposed | **Cost**: $150–300 | **Weeks**: 12 | **Phase**: 3

**Affected wiki**: [self-experiment-protocol](./self-experiment-protocol.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [synthesis](./synthesis.md)

**What it tests:** Does the current supplement stack suppress 5-LOX/LTB4 activity in vivo in Brian specifically? This directly validates quercetin's CP6a mechanism (5-LOX IC50 = 300 nM from ChEMBL, now the stack's most potent curated 5-LOX activity) as the operative mechanism — rather than its weaker NF-κB/NLRP3 effects that currently dominate the stack rationale.

**Proposed in:** `wiki/synthesis.md` 2026-04-24 Pass 2 Proposed Experiment #1 and New Connection #3. Brian's 2026-04-24 annotation: "do it. also, i have recent extensive labs that i can add to the project."

**Protocol:**
- Add urinary LTB4 assay to existing self-experiment timepoints in [self-experiment-protocol.md](./self-experiment-protocol.md): **baseline, week 4, week 12** (three measurements total).
- Collect first-morning urine (~20 mL), freeze at -80°C until shipment (standard for eicosanoid stability).
- Ship to a commercial lab offering LTB4 ELISA or LC-MS/MS (e.g., Cayman Chemical assay kit format via CLIA lab, or direct Mayo Clinic / ARUP specialty testing).
- No additional study visit required — piggybacks on the existing self-experiment draw schedule.
- Compare with hs-CRP and urate trajectories at the same timepoints to separate "stack is working" (hs-CRP drop) from "stack is working via CP6a" (urinary LTB4 drop).

**Estimated cost:** $50-100 per assay × 3 timepoints = **$150-300 total**

**Estimated timeline:** No additional study time — piggybacks on the existing 12-week self-experiment. Results available ~2 weeks after each draw.

**Dependencies:** Existing self-experiment infrastructure (`wiki/self-experiment-protocol.md`). No new study visits or logistics beyond adding a urine collection to existing draws.

**Success criteria:**
- Measurable baseline urinary LTB4 (confirms the assay is sensitive at Brian's baseline state)
- ≥30% reduction at week 4 or week 12 relative to baseline → suggests CP6a engagement in vivo
- No change in LTB4 despite hs-CRP improvement → suggests stack effect is via other chokepoints (NF-κB, NLRP3 assembly), not 5-LOX

**Cross-references:** `wiki/self-experiment-protocol.md` (baseline/week 4/week 12 timepoints), `wiki/nlrp3-exploit-map.md` (CP6a), `wiki/nlrp3-inhibitor-screen.md` (quercetin 5-LOX IC50 = 300 nM)

---

### 3.7 Brian: Serum C5a Baseline + Week 12 — Validating CP0 Complement Priming Status

**Status**: Proposed | **Cost**: $300–400 | **Weeks**: 12 | **Phase**: 3

**Affected wiki**: [complement-c5a-gout](./complement-c5a-gout.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [self-experiment-protocol](./self-experiment-protocol.md)

**What it tests:** Documents complement priming status (C5a, the dominant NLRP3 priming signal per Cumpelik 2016 PMID 26245757 + Khameneh 2017 PMID 28167912) before and after the 12-week supplement stack. The stack currently covers CP1-CP5a but not CP0 — this experiment tests whether it modulates complement at all, and establishes a baseline for future CP0-targeted interventions (e.g., avacopan, flavonoid C5aR1 antagonists per `wiki/complement-c5a-gout.md`).

**Proposed in:** `wiki/synthesis.md` 2026-04-24 Pass 2 Proposed Experiment #2 and New Connection #3.

**Protocol:**
- Add serum C5a to the baseline and week 12 blood panels in `wiki/self-experiment-protocol.md`.
- Alternative marker: **sC5b-9** (soluble terminal complement complex) — often more stable in serum than free C5a and available on standard commercial panels.
- LabCorp (Complement C5a by enzyme immunoassay, test code 142046) or Quest (sC5b-9 panel) both offer this as a routine specialty test with physician order.
- No new study visit — piggybacks on the already-planned week 0 and week 12 draws.
- Cross-reference with CBC, urate, hs-CRP at the same timepoints.

**Estimated cost:** $150-200 per C5a or sC5b-9 test × 2 timepoints = **$300-400 total**

**Estimated timeline:** No additional study time. Results available ~1 week after draw.

**Dependencies:** Existing self-experiment infrastructure; rheumatologist or primary-care order for the specialty test.

**Success criteria:**
- Measurable baseline C5a (confirms assay sensitivity; establishes whether Brian is a "high-complement-priming" or "low-complement-priming" gout patient — relevant for stack design)
- **Predicted: minimal change at week 12**, since the stack doesn't cover CP0. This is a negative-control-type experiment: if C5a drops significantly, that tells us something unexpected is happening and CP0 is engaged. If C5a doesn't change, that validates the wiki's claim that CP0 is an uncovered chokepoint needing dedicated interventions.
- Either result informs next-phase stack design.

**Cross-references:** `wiki/self-experiment-protocol.md` (week 0 and week 12 panels), `wiki/complement-c5a-gout.md` (CP0 chokepoint), `wiki/nlrp3-exploit-map.md` (CP0 entry)

---

### 3.8 Brian: DHA vs. EPA Split Omega-3 Crossover — Resolving the Gout-Specific SPM Precursor Question

**Status**: Proposed | **Cost**: $550–700 | **Weeks**: 9 | **Phase**: 3

**Affected wiki**: [spm-resolution-pathway](./spm-resolution-pathway.md), [supplements-stack](./supplements-stack.md), [tnfsf14-gout-target](./tnfsf14-gout-target.md), [self-experiment-protocol](./self-experiment-protocol.md)

**What it tests:** Is DHA or EPA the optimal omega-3 precursor for gout flare prevention in Brian's specific case? The 2026-04-24 synthesis pass identified a contradiction between the cardiovascular literature (EPA-dominant) and the gout-specific SPM evidence (DHA-derived RvD1 and MaR1 both show direct MSU animal-model efficacy; DHA also inversely associates with circulating TNFSF14/LIGHT per Mendelian randomization). The `supplements-stack.md` currently recommends 2:1 or 3:1 EPA:DHA for gout, which may be a cardiovascular-biased extrapolation.

**Proposed in:** `wiki/synthesis.md` 2026-04-24 Pass 2 Proposed Experiment #4 and New Connection #2 ("DHA should be preferentially dosed over EPA for gout").

**Protocol:**
- **Phase A (4 weeks): High-EPA protocol.** 3 g EPA + 0.5 g DHA daily (≈6:1 ratio — commercial high-EPA omega-3 formulations like Nordic Naturals ProEPA or Minami Platinum-Plus EPA).
- **Washout (1 week):** No omega-3 supplementation. Continue rest of base stack.
- **Phase B (4 weeks): High-DHA protocol.** 3 g DHA + 0.5 g EPA daily (≈6:1 ratio DHA-dominant — e.g., Nordic Naturals ProDHA or Life Extension Mega EPA/DHA adjusted by dropping EPA capsules).
- Biomarkers measured at baseline, end of Phase A, end of washout, end of Phase B:
  - **Urinary LTB4** (from 3.6 above; tests whether DHA or EPA better suppresses 5-LOX/LTB4 output)
  - **hs-CRP** (generic inflammation marker)
  - **Serum SPM panel (RvD1, RvE1, MaR1 metabolites if a CLIA lab offers this — otherwise spot-measure via Cayman Chemical research kit through a lab contact)**
  - **Gout flare count and severity (daily log)**
- Washout rationale: 7-day omega-3 washout is short relative to RBC phospholipid half-life (~8 weeks) but sufficient to allow downstream SPM levels to decay. Accept the limitation — n=1 study, not a clinical trial.

**Estimated cost:** $200 (supplement differentials across 9 weeks) + $300 (SPM panel) + $50-100 × 2-3 additional LTB4 assays = **$550-700 total** on top of 3.6

**Estimated timeline:** 9 weeks (4 + 1 + 4), concurrent with the existing self-experiment or as a post-experiment extension.

**Dependencies:**
- Experiment 3.6 (urinary LTB4 assay infrastructure)
- Availability of a lab offering SPM metabolite measurement (Mayo Clinic has an eicosanoid panel; research-grade SPM kits from Cayman require a CLIA lab partnership)
- Brian's flare calendar (existing self-tracking)

**Success criteria:**
- **Clear directional effect:** one phase (either EPA or DHA) produces lower urinary LTB4, higher serum RvD1 or RvE1, and fewer flares than the other.
- **Ambiguous result** (both phases similar): the ratio doesn't matter clinically for Brian; revert to a balanced 1:1 or the cheaper formulation.
- **Directional toward DHA:** revises `supplements-stack.md` and confirms the 2026-04-24 synthesis recommendation.
- **Directional toward EPA:** the current stack recommendation was right; synthesis flagged a literature signal that doesn't translate for Brian.

**Cross-references:** `wiki/spm-resolution-pathway.md` (RvD1/MaR1 DHA-derived), `wiki/supplements-stack.md` (omega-3 entry, currently EPA-leaning), `wiki/self-experiment-protocol.md` (integration with the existing protocol), `wiki/tnfsf14-gout-target.md` (DHA-TNFSF14 Mendelian randomization link), `wiki/nlrp3-exploit-map.md` (CP5b SPM entry)

---

### 3.9 Brian: Zileuton Off-Label Trial — Pharma-Grade CP6a Inhibition in Flare-Prevention Protocol

**Status**: Proposed | **Cost**: ~$500 | **Weeks**: 16 | **Phase**: 3

**Affected wiki**: [zileuton](./zileuton.md), [gout-clinical-pipeline](./gout-clinical-pipeline.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [self-experiment-protocol](./self-experiment-protocol.md)

**What it tests:** Does the FDA-approved 5-LOX inhibitor **zileuton** (Zyflo / Zyflo CR, asthma indication) abort or prevent gout flares in Brian's specific case? This is the pharma-grade equivalent of quercetin's CP6a mechanism — cleaner readout, stronger effect size expected. Cross-references the `wiki/zileuton.md` dossier (in progress per synthesis queue).

**Proposed in:** `wiki/synthesis.md` 2026-04-24 Pass 2 Proposed Experiment #5 and New Connection #5 ("Zileuton is the closest pharma-grade CP6a analog to quercetin, and has never been tested in gout"). Brian's 2026-04-24 annotation: "yes add it to the clinical pipeline and also let's do a wiki page about it."

**Protocol:**
- **Phase 1: Physician conversation.** Request off-label prescription from rheumatologist or primary-care physician with the CP6a mechanistic rationale. Key talking points:
  - Zileuton (Zyflo CR) is FDA-approved for asthma, dosed 1200 mg BID, generic available, ~$50/month.
  - 5-LOX is mechanistically upstream of neutrophil chemotaxis in gout (LTB4 is a potent neutrophil chemoattractant; colchicine blocks microtubule-dependent chemotaxis downstream).
  - No published gout efficacy trials; this is a genuine off-label novelty.
  - Safety profile: liver enzyme elevation is the primary monitoring concern (~2% patients); monthly LFTs for the first 3 months standard.
  - Duration: 12 weeks, consistent with the existing self-experiment window.
- **Phase 2: Baseline documentation.** Brian's colchicine-era flare frequency (available from existing medication history). 4-week pre-zileuton observation window if feasible.
- **Phase 3: Zileuton 1200 mg BID × 12 weeks.** Continue base supplement stack (including quercetin — zileuton does not contraindicate quercetin and any additive effect is informative).
- Biomarkers:
  - **Urinary LTB4** at baseline and week 12 (from 3.6 — direct pharmacodynamic confirmation)
  - **Gout flare count and severity** (primary endpoint; daily log)
  - **LFTs** (AST, ALT) at baseline, week 2, week 4, week 8, week 12 (safety)
  - **hs-CRP** at baseline and week 12

**Estimated cost:** $150-200/month × 3 months = **$450-600** (prescription) + existing LFT coverage via insurance + $0 additional lab cost (piggybacks on 3.6 and insurance-covered LFTs). **Net additional: ~$500.**

**Estimated timeline:** 12 weeks active treatment + 4-week follow-up for post-treatment flare rate. Single additional physician conversation to set up.

**Dependencies:**
- Rheumatologist or primary-care physician willing to prescribe off-label. The mechanistic rationale + clean safety profile + low cost should clear this bar.
- Completion of `wiki/zileuton.md` dossier (in progress; synthesis queue item) for Brian to share with the prescribing physician.
- Experiment 3.6 (urinary LTB4 as pharmacodynamic confirmation)

**Success criteria:**
- **Urinary LTB4 ≥50% reduction at week 12** (confirms pharmacodynamic engagement — zileuton's on-target effect)
- **Flare frequency reduced ≥50% vs. colchicine-era baseline** (clinical efficacy signal)
- **LFTs remain within normal range throughout** (safety)
- **Negative result (no flare reduction despite LTB4 drop)** is also informative: suggests LTB4/neutrophil-chemotaxis is not rate-limiting for Brian's flare biology, and colchicine's mechanism (microtubule → chemotaxis) is doing more work than expected.

**Cross-references:** `wiki/zileuton.md` (to be created), `wiki/gout-clinical-pipeline.md` (mechanistic gap entry), `wiki/nlrp3-exploit-map.md` (CP6a), `wiki/self-experiment-protocol.md` (integration with existing protocol)

---

## Cross-Experiment Dependencies and Sequencing

```text
Phase 1 (In Vitro)
├─ 1.1: Gene performance [weeks 1-6] ─────┬─→ 1.2, 1.3, 1.5, 1.6
├─ 1.2: Secretion vs. intracellular ──────┤
├─ 1.3: Beer survival ──────────────┬─────→ 2.2 (yeast efficacy)
├─ 1.4: Drying stability ───────────┤ ────→ 3.1 (yeast formulation)
├─ 1.5: Koji expression ────────────┬─────→ 1.6, 1.7 (koji validation)
├─ 1.6: Koji digestive stability ───┤────→ 2.3 (EPI model)
├─ 1.7: NLRP3 pathway validation ───┤────→ 2.4 (MSU arthritis model)
│
├─→ Phase 2 (Animal Models)
    ├─ 2.1: Gnotobiotic S. boulardii [weeks 12-20] ──┬─→ 3.1
    ├─ 2.2: Hyperuricemic rat model [weeks 10-16] ───┤─→ 3.1
    ├─ 2.3: EPI koji model [weeks 12-18] ───────────┬─→ 3.3
    ├─ 2.4: MSU arthritis model [weeks 14-22] ──────┬─→ 3.2
    └─ 2.5: PULSE E. coli probiotic [weeks 12-18] ──┤
    
    ├─→ Phase 3 (Human Self-Experimentation)
        ├─ 3.1: Yeast uricase (Brian) [weeks 24-44] ──┬─→ 3.5
        ├─ 3.2: NLRP3 stack (Brian) [weeks 24-44] ────┼─→ parallel with 3.1
        ├─ 3.3: Koji enzymes (Lynn) [weeks 20-32] ────┤─→ 3.4
        ├─ 3.4: Engineered koji (both) [weeks 36-50] ─┤
        └─ 3.5: Long-term flare prevention [weeks 45-71]
```

---

## Success Metrics Summary

| Phase | Experiment | Primary Endpoint | Target Threshold |
|-------|-----------|------------------|------------------|
| 1 | Gene performance | Uricase specific activity | >50 μmol/h/OD |
| 1 | Secretion | Bioavailable enzyme fraction | >30% extracellular |
| 1 | Beer survival | Enzyme activity retention | >30% post-fermentation |
| 1 | Drying | Lyophilization stability | >40% activity retained |
| 1 | Koji expression | Secreted uricase activity | >20 μmol/h/OD |
| 1 | Koji digestive pH | Duodenal survival | >20% activity post-transit |
| 1 | NLRP3 pathway | IL-1β reduction | >50% at stated doses |
| 2 | S. boulardii colonization | Fecal yeast counts | >10⁶ CFU/mL by day 3 |
| 2 | Yeast efficacy (rat) | Serum uric acid reduction | ≥30% vs. vehicle |
| 2 | Koji EPI model | Fat absorption | >92% (vs. <50% baseline) |
| 2 | MSU arthritis | Joint swelling reduction | ≥40% vs. vehicle |
| 2 | PULSE homeostasis | Uric acid range maintained | 2.0–4.0 mg/dL |
| 3 | Yeast uricase (Brian) | Flare frequency reduction | ≥50% vs. baseline |
| 3 | NLRP3 stack (Brian) | IL-1β reduction | ≥30% vs. baseline |
| 3 | Koji enzymes (Lynn) | GI symptom improvement | ≥50% vs. baseline |
| 3 | Engineered koji (both) | Tolerability + efficacy | >80% adherence + dual benefit |
| 3 | Long-term prevention | Sustained flare reduction | ≥40% reduction sustained 6mo |
| 1 | EGCG CP1a (1.8) | IL-6 suppression at ≤1 μM EGCG | ≥50% |
| 3 | Urinary LTB4 (3.6) | Stack effect on 5-LOX in vivo | ≥30% reduction vs. baseline |
| 3 | Serum C5a (3.7) | CP0 priming documentation | Measurable baseline; informative either direction |
| 3 | DHA vs. EPA (3.8) | Directional omega-3 preference | Clear winner or confirmed null |
| 3 | Zileuton off-label (3.9) | LTB4 reduction + flare reduction | ≥50% LTB4 drop, ≥50% flare reduction |

---

## Notes on Open Questions

- **GLUT9 and urate transport bottleneck:** Could engineered koji produce high fructokinase inhibitors to address the fructose-gout link? (Source: gout-deep-dive.md, Section 9)
- **Delivery route optimization:** Is intestinal lumen degradation sufficient, or would systemic absorption of recombinant uricase be superior? (Source: blood-barrier-exploits.md)
- **Microbiome stability:** Will engineered probiotics persist without colonization, or is daily dosing required long-term? (Source: gout-deep-dive.md, Section 8)
- **Gene therapy as alternative:** Should we pursue CRISPR-based uricase gene therapy in parallel? (Source: gout-deep-dive.md, Section 6)

---

*Document maintained as part of the [[open-source-platform]] initiative. All experiments are designed for replication and community contribution.*
