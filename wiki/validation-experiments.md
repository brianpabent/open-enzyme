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

Dashboard view of all 34 experiments in the library. Sorted by phase then ID. Detail lives in the phase sections below — click the ID to jump.

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
| [§1.11](#111-ergothioneine--abcg2-induction-in-caco-2-native-koji-synergy-test) | Ergothioneine → ABCG2 Caco-2 (native koji synergy) | In Vitro | $1,000–1,500 | 3–4 | Proposed | [abcg2-modulators](./abcg2-modulators.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.12](#112-local-h2o2-stress-in-caco-2-from-high-gut-lumen-uricase) | Local H₂O₂ epithelial stress from gut-lumen uricase | In Vitro | $800–1,200 | 2–3 | Proposed | [uricase](./uricase.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.13](#113-limonene--abcg2-induction-in-caco-2-tier-3-stack-synergy-test) | Limonene → ABCG2 Caco-2 (Tier-3 stack synergy) | In Vitro | $800–1,200 | 3–4 | Proposed | [supplements-stack](./supplements-stack.md), [abcg2-modulators](./abcg2-modulators.md), [cannabinoids-terpenes](./cannabinoids-terpenes.md) |
| [§1.14](#114-additive-abcg2-suppression-by-androgens--tnfα--butyrate-rescue--lactoferrin-synergy) | DHT + TNFα additive ABCG2 suppression + butyrate/lactoferrin rescue + supplement ABCG2 antagonism + Q141K arm | In Vitro | $2,100–3,200 | 4–6 | Proposed | [abcg2-modulators](./abcg2-modulators.md), [androgen-urate-axis](./androgen-urate-axis.md), [gut-lumen-sink](./gut-lumen-sink.md), [lactoferrin](./lactoferrin.md), [supplements-stack](./supplements-stack.md), [koji-endgame-strain](./koji-endgame-strain.md) |
| [§1.15](#115-rice-bran-substrate--koji-uricase-gi-survival) | Rice-bran substrate × koji uricase GI survival | In Vitro | $800–1,200 | 3 | Proposed | [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.16](#116-opt-1-disulfide-engineered-uricase-in-koji-vs-wt--gi-survival-head-to-head) | OPT-1 disulfide uricase in koji vs. WT (GI survival) | In Vitro | $1,800–2,500 | 6–8 | Proposed | [engineered-koji-protocol](./engineered-koji-protocol.md), [uricase-variant-selection](./uricase-variant-selection.md), [protein-engineering-strategy](./protein-engineering-strategy.md) |
| [§1.17](#117-quercetin--ursolic-acid--carnosine-three-way-synergy-on-msu-stimulated-thp-1) | Quercetin × ursolic × carnosine 3-way synergy (THP-1 MSU) | In Vitro | $1,500–2,000 | 3–4 | Proposed | [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md), [carnosine](./carnosine.md) |
| [§1.18](#118-native-koji-enzyme-sgf-survival--free-extract-vs-whole-biomass-2-arm) | Native koji enzyme SGF (free extract vs. whole biomass) | In Vitro | $300–500 | 2 | Proposed | [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.19](#119-methodological-standard--rodent-cellular-ic50-translation-caveat) | Methodology — rodent cellular IC50 translation caveat | Standing | $0 | ongoing | Standing | [chembl-cross-check](./chembl-cross-check.md), [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md) |
| [§1.20](#120-lactoferrin--egcg-cp1a-super-additivity-assay-thp-1-macrophage-23-dose-matrix) | Lactoferrin + EGCG CP1a super-additivity (THP-1 2×3 matrix) — **gated on §1.9** | In Vitro | $1,500 | 3–4 | Proposed | [lactoferrin](./lactoferrin.md), [egcg](./egcg.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [supplements-stack](./supplements-stack.md), [koji-endgame-strain](./koji-endgame-strain.md) |
| [§1.21](#121-natural-product-c5ar1-antagonist-screening--computational-pass-closes-the-cp0-fermentable-coverage-question) | Natural-product C5aR1 antagonist screen (CP0 fermentable-coverage question) | Computational | $0 | 0.5 | **Closed (negative, 2026-04-27)** | [complement-c5a-gout](./complement-c5a-gout.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [open-enzyme-vision](./open-enzyme-vision.md) |
| [§1.22](#122-gut-selective-food-grade-hdac-inhibitor-screen-for-q141k-abcg2-trafficking-rescue) | Gut-selective food-grade HDAC inhibitor screen for Q141K-ABCG2 trafficking rescue | In Vitro | $5,000–8,000 | 8–10 | Proposed | [abcg2-modulators](./abcg2-modulators.md), [supplements-stack](./supplements-stack.md), [gut-lumen-sink](./gut-lumen-sink.md) |
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
| [§3.10](#310-brian-fructose-challenge-test-as-acute-n1-uricase-efficacy-readout) | Brian: fructose challenge test (acute n=1 uricase readout) | Human | ~$50 | 0.1 + 4 wk gap | Proposed | [fructose-connection](./fructose-connection.md), [self-experiment-protocol](./self-experiment-protocol.md), [synthesis](./synthesis.md) |

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

**Computational prior (comp-001, 2026-05-05):** AlphaFold structural analysis + P1/P1' cleavage-site prediction for all three *A. oryzae* koji proteases (ALP, NPr, acid protease) under shio-koji conditions found **zero exposed recognition sites** — all 356 sites across all three proteases map to buried/well-folded regions (100% of residues pLDDT > 80, mean 97.1). ALP is also strongly salt-inhibited (~19% residual activity at 17.5% NaCl). Verdict: LOW structural risk. This shifts §1.10 from a **feasibility gate** to a **confirmation experiment** — the structural evidence argues the shio-koji format will work; §1.10 confirms and quantifies it. Full analysis: [`wiki/uricase-protease-stability-computational.md`](./uricase-protease-stability-computational.md) and [`experiments/comp-001-uricase-shio-koji-protease-stability/`](../experiments/comp-001-uricase-shio-koji-protease-stability/).

**Cross-references:** [synthesis.md](./synthesis.md) 2026-04-27 Open Question #2 + Connection #2; [engineered-koji-protocol.md](./engineered-koji-protocol.md) §15 (the dual-use proposal this experiment gates); [koji-home-fermentation.md](./koji-home-fermentation.md) (shio-koji standard protocol); [aspergillus-oryzae.md](./aspergillus-oryzae.md) (native protease characterization); [uricase-protease-stability-computational.md](./uricase-protease-stability-computational.md) (comp-001 structural prior); [computational-experiments.md](./computational-experiments.md).

---

### 1.11 Ergothioneine → ABCG2 Induction in Caco-2 (Native Koji Synergy Test)

**Status**: Proposed | **Cost**: $1,000–1,500 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [abcg2-modulators](./abcg2-modulators.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [gut-lumen-sink](./gut-lumen-sink.md)

**What it tests:** Does ergothioneine — natively produced by *A. oryzae* at ~20 mg/g dry mass — induce ABCG2 expression in human enterocyte-lineage cells at concentrations achievable from koji-derived dietary intake? **Tag: Mechanistic Extrapolation testing a two-step inference (ergothioneine → Nrf2 stabilization → ABCG2 induction).** Ergothioneine's "Nrf2 inducer" classification is weaker than canonical activators (sulforaphane, CDDO-Me) — it is more accurately a ROS scavenger that may indirectly stabilize Nrf2. This experiment disambiguates whether the engineered-koji platform has a "free" ABCG2-induction synergy via its native metabolite chorus, or whether the connection is too distant to matter at koji-achievable luminal doses. **Verify substrate claim before running:** confirm `aspergillus-oryzae.md` ergothioneine titer (~20 mg/g dry mass) against primary literature; the L223 sweep flagged that pass-2 cited this without a verified primary source.

**Proposed in:** `wiki/synthesis.md` 2026-04-27 sweeps (Connection #1, multiple sweep blocks: ergothioneine→Nrf2→ABCG2 chain).

**Protocol:**
- **Cells:** Caco-2 (ATCC HTB-37), differentiated 21 days on transwell inserts to recapitulate apical/basolateral polarity.
- **Treatment arms (n=4 wells per arm):**
  - Vehicle control
  - Ergothioneine at 1, 10, 100 μM (apical) — brackets the koji-luminal-bioavailability range (OCTN1 transport is the rate-limiter)
  - Sulforaphane at 1 μM (positive control — established Nrf2 → ABCG2 inducer per Xie 2020)
  - Combination: ergothioneine 100 μM + sulforaphane 0.1 μM (sub-threshold sulforaphane to test additivity)
- **Time-course:** 6, 24, 48 h.
- **Readouts:**
  - ABCG2 mRNA (qPCR, normalized to GAPDH)
  - ABCG2 protein (Western, apical-membrane fraction)
  - Functional efflux (Hoechst 33342 accumulation assay; or urate-direct transport in bidirectional transwell if budget allows — strongly preferred per the L243-area review note that prior assays should ground in urate not just BCRP probe substrates)
  - Nrf2 nuclear translocation (immunofluorescence, 6 h timepoint)
- **Substrate-claim verification (parallel, $0):** desk-check `aspergillus-oryzae.md` against primary literature (Cheah & Halliwell 2012, Borodina 2020) before committing wet-lab spend.

**Estimated cost:** $1,000–1,500 — Caco-2 culture + transwell inserts ($300), ergothioneine + sulforaphane standards ($150), qPCR primers + reagents ($200), Western antibodies for ABCG2 + Nrf2 ($300), Hoechst probe + plate reader time ($100), urate-transport reagents ($150) if pursuing the bidirectional transwell.

**Estimated timeline:** 3–4 weeks.

**Dependencies:** None — Caco-2 is a standard cell line. Could pair with §1.13 (limonene) to amortize fixed costs.

**Success criteria:**
- **Confirms synergy claim:** ABCG2 mRNA and protein induction at koji-achievable ergothioneine concentrations (10–100 μM apical), with functional efflux upregulation. Promotes the "free synergy" claim from speculative to supported in [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) and [`aspergillus-oryzae.md`](./aspergillus-oryzae.md).
- **Falsifies / scopes down:** No detectable ABCG2 induction at koji-achievable doses. Removes the synergy claim from the platform thesis; positive sulforaphane control remains the canonical ABCG2 inducer route.

**Cross-references:** [synthesis.md](./synthesis.md) 2026-04-27 Connection #1 (multiple sweep blocks); [abcg2-modulators.md](./abcg2-modulators.md) §2 (Nrf2 transcriptional axis); [aspergillus-oryzae.md](./aspergillus-oryzae.md) (native ergothioneine claim — verify before spending).

---

### 1.12 Local H₂O₂ Stress in Caco-2 from High Gut-Lumen Uricase

**Status**: Proposed | **Cost**: $800–1,200 | **Weeks**: 2–3 | **Phase**: 1

**Affected wiki**: [uricase](./uricase.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [gut-lumen-sink](./gut-lumen-sink.md), [engineered-koji-protocol](./engineered-koji-protocol.md)

**What it tests:** Does high local uricase activity in proximity to enterocytes generate H₂O₂ flux that exceeds local catalase scavenging capacity, causing oxidative stress / barrier compromise? Uricase generates H₂O₂ stoichiometrically 1:1 with urate consumption. Gut-lumen urate concentrations reach hundreds of μM; near a koji particle expressing uricase, peak local H₂O₂ flux could locally overwhelm host- and microbe-derived catalase. The catalase-neutralization assumption in [`uricase.md`](./uricase.md) and [`aspergillus-oryzae.md`](./aspergillus-oryzae.md) is currently un-quantified.

**Proposed in:** `wiki/synthesis.md` 2026-04-27 Open Question #1 (ergothioneine sweep).

**Protocol:**
- **Cells:** Caco-2 transwell monolayer, 21-day differentiated.
- **Treatment arms (n=4):**
  - Vehicle (apical buffer + 500 μM urate, no enzyme)
  - Uricase apical only (rasburicase or *A. flavus* recombinant uricase) at 0.1, 1, 10 U/mL
  - Uricase + catalase apical (1000 U/mL catalase) — tests whether exogenous catalase rescues
  - Uricase + ergothioneine 100 μM apical — tests whether co-delivered native koji metabolite mitigates
- **Readouts:**
  - Apical H₂O₂ time-course (Amplex Red probe, fluorescent plate reader, every 5 min × 60 min).
  - TEER (trans-epithelial electrical resistance) — barrier-integrity readout, baseline + 1, 4, 24 h.
  - LDH release (apical and basolateral) — cytotoxicity proxy.
  - Tight-junction protein localization (ZO-1, occludin) by IF after 24 h.
- **Optional:** add an *A. oryzae* whole-koji-extract arm (delivers uricase + native catalase + ergothioneine simultaneously) to test whether the native chorus is naturally self-buffering.

**Estimated cost:** $800–1,200 — Caco-2 + transwell ($300), Amplex Red kit ($200), rasburicase (research grade, $100), catalase ($50), TEER electrodes (already standard), IF antibodies ($200), reagents ($150).

**Estimated timeline:** 2–3 weeks.

**Dependencies:** Caco-2 cell access. Could co-run with §1.11 (ergothioneine arm transfers directly).

**Success criteria:**
- **No barrier compromise** at any uricase dose tested in the koji-realistic dose range: removes the open question from the platform-risk register.
- **Barrier compromise at high doses** (TEER drop >25%, LDH increase, ZO-1/occludin disruption): triggers a redesign of the engineered-strain expression cassette toward a regulated/dose-capped uricase output, OR mandates ergothioneine co-delivery as a safety feature, OR informs an enteric-coated dose-limiting formulation strategy.

**Cross-references:** [synthesis.md](./synthesis.md) 2026-04-27 Open Question #1; [uricase.md](./uricase.md) (catalase-neutralization assumption); [aspergillus-oryzae.md](./aspergillus-oryzae.md) (native catalase + ergothioneine).

---

### 1.13 Limonene → ABCG2 Induction in Caco-2 (Tier 3 Stack Synergy Test)

**Status**: Proposed | **Cost**: $800–1,200 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [supplements-stack](./supplements-stack.md), [abcg2-modulators](./abcg2-modulators.md), [cannabinoids-terpenes](./cannabinoids-terpenes.md)

**What it tests:** Does limonene induce ABCG2 expression in Caco-2 enterocytes at supplement-relevant doses? Limonene was promoted to Tier 3 in `supplements-stack.md` based on the Venkatesan 2025 MSU rat model (50 mg/kg ≈ 0.5 g/day BSA-scaled human dose, close to typical supplement range), citing Nrf2 activation as a key mechanism. `abcg2-modulators.md` independently identifies Nrf2 as an ABCG2 transcriptional inducer (sulforaphane precedent, EC50 = 580 nM). This experiment tests whether limonene's putative Nrf2 activation translates to ABCG2 induction — gating whether the supplements-stack entry should be augmented with a "gut-lumen sink synergy" claim.

**Proposed in:** `wiki/synthesis.md` 2026-04-26 Connection #3.

**Protocol:**
- **Cells:** Caco-2 transwell, 21-day differentiated.
- **Treatment arms (n=4):**
  - Vehicle
  - Limonene at 1, 10, 50, 100 μM (DMSO-solubilized; correct for DMSO at <0.1%)
  - Sulforaphane 1 μM (positive control)
  - Limonene + sulforaphane combination at sub-threshold doses
- **Time-course:** 24, 48 h.
- **Readouts:** ABCG2 mRNA (qPCR), ABCG2 protein (Western, apical-membrane fraction), functional efflux (Hoechst 33342 or urate-direct in bidirectional transwell).

**Estimated cost:** $800–1,200 — Caco-2 + transwell ($300), limonene + sulforaphane standards ($100), qPCR ($200), Western antibodies ($300), efflux probe ($100), reagents ($150).

**Estimated timeline:** 3–4 weeks (parallelizable with §1.11).

**Dependencies:** Caco-2 access; pairs cleanly with §1.11.

**Success criteria:**
- **Confirms synergy claim:** ABCG2 induction at supplement-achievable limonene doses. Updates [`supplements-stack.md`](./supplements-stack.md) limonene entry to include the gut-lumen-sink synergy and promotes the compound from Nrf2-activator-only to Nrf2 + ABCG2-inducer.
- **Falsifies:** No ABCG2 induction at any tested dose. Removes the synergy claim; limonene remains a Tier 3 NLRP3 modulator without the ABCG2 angle.

**Cross-references:** [synthesis.md](./synthesis.md) 2026-04-26 Connection #3; [supplements-stack.md](./supplements-stack.md) limonene entry; [abcg2-modulators.md](./abcg2-modulators.md) §2.

---

### 1.14 Additive ABCG2 Suppression by Androgens + TNFα + Butyrate Rescue + Lactoferrin Synergy

**Status**: Proposed | **Cost**: $1,800–2,800 | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [abcg2-modulators](./abcg2-modulators.md), [androgen-urate-axis](./androgen-urate-axis.md), [gut-lumen-sink](./gut-lumen-sink.md), [supplements-stack](./supplements-stack.md), [lactoferrin](./lactoferrin.md), [koji-endgame-strain](./koji-endgame-strain.md)

**What it tests:** Four questions in one experiment. (1) Are androgen (DHT) and inflammatory (TNFα) suppression of ABCG2 **additive**, producing a "worst-case" phenotype for the gut-lumen sink in patients with both elevated androgens and chronic inflammation? (2) Does butyrate co-treatment **rescue** the suppressed phenotype via PPARγ induction, restoring substrate flow for the engineered uricase? (3) Does lactoferrin co-treatment **also rescue** the TNFα-suppressed phenotype via TNFα suppression (independent of PPARγ) — testing whether the koji endgame strain's engineered lactoferrin payload would synergize with its co-expressed uricase by relieving the inflammatory brake on ABCG2? (4) Do stack supplements (quercetin, EGCG, curcumin) **inhibit** ABCG2-mediated urate efflux at supplement-relevant gut-lumen concentrations, and is this antagonism genotype-dependent (Q141K vs. WT)?

**Proposed in:** `wiki/synthesis.md` 2026-04-27 Connection #1 + Proposed Experiment #2 (DHT + TNFα additive ABCG2 suppression); 2026-05-05 Connection #1 (lactoferrin → TNFα → ABCG2 derepression as substrate-supply synergy). Per the Pass 3 review augmentation: bundle the lactoferrin arm into the same Caco-2 factorial rather than queue a parallel experiment — the marginal cost is small relative to running two batches.

**Protocol:**
- **Cells:** Caco-2 transwell (used in both Xie 2020 and Solbakk 2025 per `abcg2-modulators.md`), 21-day differentiated.
- **Treatment arms (3 × 3 + rescue arms, n=4 per arm):**
  - DHT: 0, 10, 100 nM
  - TNFα: 0, 5, 20 ng/mL
  - All 9 combinations (DHT × TNFα factorial)
  - **Butyrate rescue arm:** repeat the highest-suppression combination (DHT 100 nM + TNFα 20 ng/mL) ± butyrate 1 mM apical.
  - **Lactoferrin rescue arm:** repeat the TNFα-only suppression (TNFα 20 ng/mL, DHT 0) and the worst-case combination (DHT 100 nM + TNFα 20 ng/mL) ± bovine lactoferrin 100 µg/mL basolateral (mimicking gut-lumen-side delivery from the koji endgame strain). Compare to the butyrate rescue arm — lactoferrin's mechanism (TNFα suppression upstream) is mechanistically distinct from butyrate's (PPARγ induction), so the two should not be redundant in the worst-case phenotype.
  - **Supplement ABCG2 antagonism arms (added 2026-05-05, per synthesis Proposed Experiment #1):** Using the basal (DHT 0, TNFα 0) monolayer, apply each of the three named stack supplements at supplement-relevant gut-lumen concentrations, apical side: quercetin 10 µM and 50 µM; EGCG 1 µM and 10 µM; curcumin 5 µM and 20 µM. Measure urate flux in all six conditions vs. DMSO vehicle. These concentrations reflect achievable post-oral-dose enterocyte exposure, not plasma concentrations (gut-lumen levels are 10–50× higher than plasma due to incomplete absorption). Note: the Yu 2024 EGCG in vivo data (PMID 38757391) shows net-favorable ABCG2/URAT1/GLUT9 effect in hyperuricemic mice, contradicting the in vitro inhibition story — include both 1 µM and 10 µM EGCG arms to see whether the inhibitory or the inductive effect dominates at supplement-achievable concentrations. **Q141K-variant arm:** if a Q141K-expressing Caco-2 line or patient-derived matched organoid is available, repeat the highest-effect supplement conditions (quercetin 50 µM + curcumin 20 µM) in both WT and Q141K backgrounds — this directly tests the stratification hypothesis that the contradiction is clinically significant for the highest-risk genotype but manageable for WT.
- **Time-course:** 48 h.
- **Readouts:** ABCG2 mRNA (qPCR), ABCG2 protein (Western, apical-membrane fraction), functional urate efflux (transwell, basolateral-to-apical urate flux — *primary readout per Pass 3 critique that expression ≠ function*), AR activation (CYP3A4 mRNA as positive control), NF-κB activation (IκBα Western), TNFα abundance in lactoferrin arms (ELISA, confirming that lactoferrin actually suppressed the added TNFα).

**Estimated cost:** $2,100–3,200 — Caco-2 + transwell ($400), DHT + TNFα + butyrate standards ($200), bovine lactoferrin (research-grade, ~$150 for 1 g), quercetin + EGCG + curcumin standards (~$150 total; all available as research-grade), urate analytics ($400, expanded for supplement arms), qPCR + Western antibodies ($600), TNFα ELISA ($150), assay reagents ($400), labor ($250 for added factorial arms). Original Proposed Experiment #1 ($1,500 parallel Caco-2 assay) is subsumed — shared Caco-2 infrastructure + urate-flux readout amortize fixed costs; this extended factorial is ~$600–700 more than the original §1.14 but replaces a separate experiment.

**Computational prior (comp-004, 2026-05-05):** IC50 occupancy analysis finds quercetin and curcumin both reach VERY HIGH ABCG2 inhibition at standard supplement doses — 6.8× and 8.3× their IC50 respectively (quercetin IC50 7,250 nM; curcumin IC50 1,630 nM), predicting 87–89% ABCG2 transport inhibition. Curcumin's < 1% bioavailability concentrates > 99% of the dose in the gut lumen, making it the highest-risk compound despite lower lumenal concentration than quercetin. EGCG operates via ABCG2 expression downregulation (24–72h transcriptional effect), not acute transport inhibition — a separate 72h treatment arm with ABCG2 Western blot is needed to capture this mechanism; the 48h transwell assay will miss it. This shifts supplement arms in §1.14 from screening ("is there an effect?") to testing a pharmacologically-predicted effect ("how large is it?"). Full analysis: [`wiki/supplement-abcg2-antagonism-computational.md`](./supplement-abcg2-antagonism-computational.md) and [`experiments/comp-004-supplement-abcg2-antagonism/`](../experiments/comp-004-supplement-abcg2-antagonism/).

**Estimated timeline:** 4–6 weeks (unchanged — supplement arms run in the same batch).

**Dependencies:** Caco-2 access. Stand-alone or paired with §1.11/§1.13 in the same Caco-2 batch run. Bovine lactoferrin is over-the-counter (Jarrow / NOW supplements work for pilot; research-grade Sigma L9507 for the actual experiment).

**Success criteria:**
- **Additive suppression confirmed AND butyrate rescue confirmed AND lactoferrin rescue confirmed:** elevates the "dense-downstream + dual gate-opening stack" framing to supported. Strengthens the personalized-medicine case for fiber/butyrate in [`abcg2-modulators.md`](./abcg2-modulators.md). Validates the lactoferrin-as-substrate-supply-synergist hypothesis in [`lactoferrin.md`](./lactoferrin.md) §4.7 and the [`koji-endgame-strain.md`](./koji-endgame-strain.md) §2.2 positive-feedback framing — making the case for layering both cassettes (uricase + lactoferrin) substantially stronger than either alone.
- **Lactoferrin rescues but butyrate doesn't (or vice versa):** identifies which gate-opener is operative in which subphenotype — informs whether the koji endgame strain payload is sufficient (lactoferrin built-in) or requires fermentable-fiber adjunct (butyrate-via-microbiome).
- **Neither rescues the worst-case phenotype:** triggers a redesign of the gut-lumen-sink dosing model — uricase output capacity must compensate for unrescuable ABCG2 capping in the male/inflamed subgroup.
- **Suppression sub-additive (synergistic-suppression rather than additive):** triggers same redesign as the no-rescue case.

**Cross-references:** [synthesis.md](./synthesis.md) 2026-04-27 Connection #1 + Proposed Experiment #2; 2026-05-05 Connection #1 (lactoferrin substrate-supply synergy); [abcg2-modulators.md](./abcg2-modulators.md) §3 (TNFα suppression — Ferrer-Picón 2020 PMID 31211831); [androgen-urate-axis.md](./androgen-urate-axis.md) (AR-mediated ABCG2 suppression); [lactoferrin.md](./lactoferrin.md) §4.1 (Habib 2023 PMID 37926296 — Lf → ↓TNFα in vivo) and §4.7 (substrate-supply synergy framing); [koji-endgame-strain.md](./koji-endgame-strain.md) §2.2.

---

### 1.15 Rice-Bran Substrate × Koji Uricase GI Survival

**Status**: Proposed | **Cost**: $800–1,200 | **Weeks**: 3 | **Phase**: 1

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [koji-construct-design](./koji-construct-design.md), [gi-survival-prediction](./gi-survival-prediction.md)

**What it tests:** Does substrate composition (white rice vs. rice bran vs. rice bran + soybean) affect GI survival of koji-produced uricase via food-matrix protection — phytic acid, polyphenols, fiber binding to the tetramer, or transit-time effects? `digestive-enzyme-optimization.md` identifies rice bran as the optimal substrate for native enzyme yield (2,280 U/g lipase vs. ~1,800 U/g on plain rice), but no current experiment tests whether substrate effects propagate to GI survival of heterologous payloads.

**Proposed in:** `wiki/synthesis.md` Pass 2 Connection #7 (rice bran interaction) + Proposed Experiment #3 (rice bran composition impact on uricase GI survival). L829, L1002.

**Protocol:**
- **Strain:** Wild-type *A. oryzae* RIB40 (no genetic modification — isolates the substrate variable from construct effects). Optional second arm with engineered uricase strain from §1.5 if available.
- **Substrate matrix:**
  - Plain white rice (baseline)
  - Rice bran alone
  - Rice bran + 10% soybean (full optimization per `digestive-enzyme-optimization.md`)
- **Fermentation:** 48 h at 30°C, 35% moisture.
- **Process:** Lyophilize, grind to powder.
- **GI simulation:** Resuspend in SGF (pH 2, pepsin, 2 h, 37°C) → SIF (pH 7, trypsin, 2 h, 37°C). Sample at 0, post-SGF, post-SIF.
- **Readouts:**
  - Uricase activity at each stage (293 nm UV-Vis or rasburicase-style assay)
  - HPLC quantification of kojic acid, ferulic acid, ergothioneine in each koji type (secondary — does substrate change native metabolite production?)
  - LC-MS for phytic acid + polyphenol residuals (does rice bran's phytic acid bind divalent cations and affect tetramer stability?)

**Estimated cost:** $800–1,200 — koji ingredients ($50), assay reagents ($300), HPLC time ($200), LC-MS time ($300), labor ($150).

**Estimated timeline:** 3 weeks.

**Dependencies:** Standard fermentation lab + HPLC/LC-MS access.

**Success criteria:**
- **Rice bran improves survival ≥10% over plain rice:** substrate optimization is a "free" stability lever; lock in rice bran + soybean as the production substrate.
- **No effect or destabilization:** plain rice or other non-bran substrate becomes the production default; rules out bran as a stability variable.
- **Ferulic acid / phytic acid correlation:** if survival tracks specific native metabolites, the variable is identifiable and tunable in future engineered constructs.

**Cross-references:** [synthesis.md](./synthesis.md) Pass 2 Connection #7 + Proposed Experiment #3; [engineered-koji-protocol.md](./engineered-koji-protocol.md) §08 (substrate optimization); [gi-survival-prediction.md](./gi-survival-prediction.md) (food-matrix model).

---

### 1.16 OPT-1 Disulfide-Engineered Uricase in Koji vs. WT — GI Survival Head-to-Head

**Status**: Proposed | **Cost**: $1,800–2,500 | **Weeks**: 6–8 | **Phase**: 1

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [uricase-variant-selection](./uricase-variant-selection.md), [protein-engineering-strategy](./protein-engineering-strategy.md), [gi-survival-prediction](./gi-survival-prediction.md)

**What it tests:** Does the OPT-1 engineered uricase variant (A6C + R290C + S119C + C220C + K234E + K236E — disulfide-bond-stabilized) achieve higher GI survival when expressed in *A. oryzae* koji compared to wild-type *A. flavus* uricase in the same construct? OPT-1 was designed in [`uricase-variant-selection.md`](./uricase-variant-selection.md) and validated in *S. cerevisiae* context; the *A. oryzae* redox environment differs and disulfide formation may not transfer cleanly. If OPT-1 koji achieves ~55–70% GI survival vs. ~25–35% for WT, koji becomes the preferred platform and obviates parallel yeast fermentation for stability gains.

**Proposed in:** `wiki/synthesis.md` Pass 2 Proposed Experiment #1 (Disulfide-engineered uricase in koji). L948.

**Protocol:**
- **Constructs:**
  - WT control: `[PamyB — SP — A. flavus uaZ codon-optimized — TamyB]`
  - OPT-1: same construct with the 6-mutation cassette (A6C + R290C + S119C + C220C + K234E + K236E)
- **Strain background:** *A. oryzae* NSAR1.
- **Fermentation:** Solid-state rice bran (per §1.15 result, or default white rice) 48–60 h.
- **Readouts:**
  - Titer (HPLC + Western on lyophilized koji)
  - Thermal stability (Tm by DSF — confirms disulfide formation)
  - Disulfide bond formation: non-reducing SDS-PAGE + DTNB free-thiol assay
  - GI survival via SGF → SIF (per §1.6 / §1.10 protocol)
- **Comparators:** Purified engineered yeast OPT-1 from `engineered-yeast-uricase-proposal.md`; rasburicase positive control.

**Estimated cost:** $1,800–2,500 — OPT-1 gene synthesis ($600), yeast OPT-1 control purification or vendor ($300), DSF + thermal stability ($200), gel electrophoresis + Western ($300), SGF/SIF reagents ($150), labor ($300).

**Estimated timeline:** 6–8 weeks.

**Dependencies:** Engineered koji strain transformation capacity; *A. oryzae* construction tooling. Could fold into the §1.9 Ward 1995 dual-cassette program if shared infrastructure is available.

**Success criteria:**
- **OPT-1 koji ≥55% GI survival** AND ≥80% titer vs. WT: koji becomes preferred platform; eliminates need for parallel yeast OPT-1 production. Locks in OPT-1 as the default uricase variant for engineered koji.
- **Disulfide formation fails (non-reducing gel shows monomer at expected MW):** *A. oryzae* redox environment incompatible with OPT-1's six engineered cysteines. Either revert to WT or design a pH-stability-only variant.
- **Activity preserved but GI survival not improved:** suggests survival is gated by gastric pH not protease, and disulfides don't help enough — pivot to enteric-coated formulation rather than further protein engineering.

**Cross-references:** [synthesis.md](./synthesis.md) Pass 2 Proposed Experiment #1; [uricase-variant-selection.md](./uricase-variant-selection.md) (OPT-1 design rationale); [protein-engineering-strategy.md](./protein-engineering-strategy.md); [engineered-koji-protocol.md](./engineered-koji-protocol.md) §02–§05 (uricase construct).

---

### 1.17 Quercetin × Ursolic Acid × Carnosine Three-Way Synergy on MSU-Stimulated THP-1

**Status**: Proposed | **Cost**: $1,500–2,000 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md), [carnosine](./carnosine.md), [engineered-koji-protocol](./engineered-koji-protocol.md)

**What it tests:** Does combining the three Tier-1 NLRP3 modulators (quercetin, ursolic acid, carnosine) produce greater than additive IL-1β suppression in MSU-stimulated human macrophages? If super-additive, the engineered-koji platform should target all three (uricase + carnosine + secondary metabolite cassette for ursolic acid/quercetin precursors). If only one or two compounds carry the signal, simplifies the construct design.

**Proposed in:** `wiki/synthesis.md` Pass 2 Proposed Experiment #2 (synergy testing — three Tier-1 NLRP3 inhibitors). L974.

**Protocol:**
- **Cells:** THP-1 PMA-differentiated to M1 phenotype (24 h LPS prime).
- **Stimulus:** MSU crystals (100 μg/mL, 4 h post-prime).
- **Treatment matrix:**
  - Quercetin alone: 5, 10, 20 μM
  - Ursolic acid alone: 2.5, 5, 10 μM
  - Carnosine alone: 1, 2, 5 mM
  - **3-way combinations** at IC50 of each compound (single, all pairs, full triplet)
- **Readouts:**
  - IL-1β (apical + basolateral if transwell) — primary readout, ELISA
  - Caspase-1 activity (luminescence-based assay)
  - ASC speck formation (immunofluorescence; manual or automated count)
  - **Loewe combination index** computed for all combinations (CI <0.7 super-additive, 0.7–1.3 additive, >1.3 antagonistic)

**Estimated cost:** $1,500–2,000 — THP-1 + reagents ($300), IL-1β ELISA ($400), caspase-1 luminescence ($200), MSU crystals + LPS ($100), compounds standards ($100), labor ($400).

**Estimated timeline:** 3–4 weeks.

**Dependencies:** THP-1 cell culture capacity. Independent or pairs with §1.7 (broader NLRP3 pathway validation).

**Success criteria:**
- **3-way super-additive (CI <0.7):** justifies engineering all three into the koji endgame strain. Strengthens the multi-target food-grade pathway-modulator thesis.
- **2-way super-additive only:** simplifies construct design — drop the redundant compound from the engineering list.
- **No synergy beyond additive:** revert to single-compound prioritization; carnosine is the strongest standalone candidate per evidence tier.

**Cross-references:** [synthesis.md](./synthesis.md) Pass 2 Proposed Experiment #2; [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) (Tier-1 candidates); [carnosine.md](./carnosine.md) (URAT1/GLUT9 angle).

---

### 1.18 Native Koji Enzyme SGF Survival — Free Extract vs. Whole Biomass (2-Arm)

**Status**: Proposed | **Cost**: $300–500 | **Weeks**: 2 | **Phase**: 1

**Affected wiki**: [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [gi-survival-prediction](./gi-survival-prediction.md), [digestive-enzyme-optimization](./digestive-enzyme-optimization.md)

**What it tests:** A 2-arm sharpening of §1.6: does cell-wall encapsulation in intact mycelium provide food-matrix protection that free enzyme extract lacks? Resolves the Koji-S vs. Koji-I default question for **native** koji enzymes (lipase, protease, amylase) in one experiment rather than two. Per the L81 Pass 3 review augmentation, both arms must be run in parallel.

**Proposed in:** `wiki/synthesis.md` 2026-04-27 Proposed Experiment #3 (Simulated GI survival assay of native koji enzymes — 2-arm augmentation). L81.

**Protocol:**
- **Material:** Wild-type *A. oryzae* fermented on rice (or rice bran per §1.15 result), 48 h.
- **Two parallel arms:**
  - **Arm A — Free extract:** Buffer-extract koji enzymes (sodium phosphate, 4°C, 30 min). Clarify by centrifugation. Measure activity in supernatant.
  - **Arm B — Whole biomass:** Lyophilize whole koji, grind to powder. Resuspend at equivalent enzyme load to Arm A.
- **GI simulation:** Both arms through SGF (pH 2, pepsin, 2 h) → SIF (pH 7, pancreatin, 2 h).
- **Readouts at each stage:**
  - Lipase: pNPP hydrolysis or tributyrin titration
  - Protease: azocasein assay
  - Amylase: starch-iodine or DNS reducing-sugar
- **Positive control:** Pancrelipase (Creon) at equivalent enzyme load.

**Estimated cost:** $300–500 — pNPP, azocasein, starch ($100), Creon control ($30), SGF/SIF reagents ($50), labor ($150).

**Estimated timeline:** 2 weeks.

**Dependencies:** Standard wet-lab. Pairs cleanly with §1.6 (extends it to the 2-arm design) — could replace §1.6 outright if budget is tight.

**Success criteria:**
- **Whole biomass survival ≥30% AND free extract survival <10%:** cell-wall encapsulation is the protective mechanism; **Koji-I (intracellular) is the default** for engineered constructs. Updates [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) §06.
- **Both arms survive ≥30%:** extract-vs-biomass distinction doesn't matter for native enzymes; substrate or food-matrix is the driver. Decouples the construct decision.
- **Both arms <10%:** native enzyme delivery via koji is inherently limited to pre-ingestion (marinade) effects; engineered delivery requires enteric coating regardless of intracellular vs. secreted strategy.

**Cross-references:** [synthesis.md](./synthesis.md) 2026-04-27 Proposed Experiment #3; [engineered-koji-protocol.md](./engineered-koji-protocol.md) §06 (Koji-S vs. Koji-I trade-off); [digestive-enzyme-optimization.md](./digestive-enzyme-optimization.md) §4 (native enzyme activity).

---

### 1.19 Methodological Standard — Rodent Cellular IC50 Translation Caveat

**Status**: Standing | **Cost**: $0 | **Weeks**: ongoing | **Phase**: 1 (methodology)

**Affected wiki**: [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [chembl-cross-check](./chembl-cross-check.md), [supplements-stack](./supplements-stack.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), all per-compound pages citing rodent IC50 values.

**Standard (not an experiment — methodology):** Rodent cellular IC50 values for NLRP3 inhibitors and other inflammasome-pathway compounds may diverge from human cellular IC50 by up to 3 orders of magnitude. Anchoring example: **dapansutrile IC50 = 1 nM in mouse J774A.1 vs. 1,000 nM (1 μM) in human MDM** under LPS+nigericin stimulation (ChEMBL v34). Apply across the wiki:

1. **Tag every rodent-derived IC50 citation** with the species and assay format. Do not present rodent IC50 as if it were a clinical-grade potency claim.
2. **Prefer human-cell data** (THP-1, U937, primary human MDM, PBMC) over rodent cellular data when evaluating new compound candidates.
3. **For mouse-only compounds (β-caryophyllene, BHB rodent ketogenic-diet gout model, ursolic acid Kawasaki mouse, carnosine hyperuricemia rat),** propose human-cell follow-up assays before promoting from animal to clinical evidence tier.
4. **For compounds with no curated human IC50,** plan species-bridging experiments (THP-1 MSU IC50 head-to-head with rodent benchmark) as part of the validation queue rather than relying on rodent extrapolation.
5. **Counter-example to flag:** repurposing candidates with strong adjacent-indication human data (zileuton, disulfiram, avacopan) may translate **cleaner** than a compound with strong rodent gout data — species-gap failures stack, while existing human safety + PK data skip the failure mode.

**Proposed in:** `wiki/synthesis.md` 2026-04-23 Connection #2 (dapansutrile species-gap). L584.

**Cross-references:** [chembl-cross-check.md](./chembl-cross-check.md) (curated ChEMBL evidence per compound), [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) §"Species-gap caveat" line 38, every per-compound wiki page citing rodent data.

---

### 1.20 Lactoferrin + EGCG CP1a Super-Additivity Assay (THP-1 Macrophage 2×3 Dose Matrix)

**Status**: Proposed (gated on §1.9) | **Cost**: $1,500 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [lactoferrin](./lactoferrin.md), [egcg](./egcg.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [supplements-stack](./supplements-stack.md), [koji-endgame-strain](./koji-endgame-strain.md)

**What it tests:** Does combining lactoferrin (LPS sequestration upstream of TLR4 — CP1a input-blocking) with EGCG (20S proteasome inhibition at IC50 = 86 nM, ChEMBL v34 — IκBα stabilization downstream of NF-κB activation, CP1a output-blocking) produce **super-additive** IL-1β suppression in MSU-stimulated human macrophages? **Tag: In Vitro (EGCG 86 nM proteasome target) + Mechanistic Extrapolation (super-additivity prediction from independent-barrier cascade logic).** The textbook conditions for super-additivity in a cascade are two independent barriers to the same output — lactoferrin neutralizes the input (LPS) before signal-1 priming can occur; EGCG blocks the output (NF-κB nuclear translocation) regardless of upstream signal. The operationally load-bearing question is dosing: EGCG carries a hepatotoxicity ceiling at ~600 mg/day (well-established; see [`egcg.md`](./egcg.md), [`disulfiram.md`](./disulfiram.md) for the hepatic-stress stacking concern). If the combination is super-additive, dosing both compounds at sub-maximal individual amounts beats either at maximum, keeping EGCG below the liver ceiling while still hitting the CP1a target. If only additive (CI 0.7–1.3), no dosing flexibility is gained. The result changes both the supplement-stack recommendations and the koji-endgame-strain priority list.

**Proposed in:** `wiki/synthesis.md` 2026-04-24 sweep (25-file v1.2 batch), Connection #4 + Proposed Experiment #2.

**Protocol:**
- **Cells:** PMA-differentiated THP-1 macrophages (or equivalent human macrophage source — primary MDM if available).
- **Stimulus:** LPS prime (signal 1) + MSU crystals (NLRP3 trigger, signal 2).
- **Treatment matrix (2×3 + combination arm, n=4 per arm):**
  - Lactoferrin: 0, low, high (apo or holo recombinant; bracket plasma-achievable and koji-luminal-achievable concentrations)
  - EGCG: 0, low, high (bracket the 86 nM proteasome IC50)
  - Mid-range combination arm at the IC50 of each compound (tests for super-additivity at the response midpoint where Loewe analysis is most sensitive)
- **Readouts:**
  - **IL-1β ELISA** (primary endpoint)
  - **IκBα Western blot** (mechanistic — confirms the EGCG arm is engaging the proteasome target; IκBα retention should track the 86 nM cellular IC50)
  - **LPS-binding assay** on lactoferrin-treated medium (mechanistic — confirms the lactoferrin arm is sequestering LPS rather than acting through an off-target mechanism)
- **Analysis:** Compute Loewe combination index across the matrix. CI <0.7 super-additive; 0.7–1.3 additive; >1.3 antagonistic.

**Estimated cost:** $1,500 — THP-1 cells + reagents (~$300), recombinant lactoferrin apo or holo form (~$400), EGCG standard (~$50), LPS + MSU (~$100), IL-1β ELISA kit (~$300), Western antibodies for IκBα (~$200), labor/materials (~$150).

**Estimated timeline:** 3–4 weeks (THP-1 differentiation 1 wk + assay 1–2 wk + analysis 1 wk).

**Dependencies:** **Gated on [§1.9](#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate--1-priority-gate) Ward 1995 dual-cassette feasibility test.** Per V4-Pro peer review (2026-04-25), this assay is "premature before feasibility": if the engineered koji platform cannot co-express both lactoferrin and uricase in one strain, the platform-level synergy claim collapses — Brian would source supplement-grade lactoferrin separately, which still works for the experiment in isolation but removes the engineered-strain motivation. Independent of [§1.7](#17-nlrp3-inflammasome-pathway-validation-thp-1-msu-macrophage-assay) (broader NLRP3 panel), but the IL-1β readout can fold into §1.7 if both run together to amortize THP-1 differentiation and ELISA fixed costs.

**Success criteria:**
- **Super-additive (CI <0.7):** justifies dosing both compounds together at sub-maximal individual doses, keeping EGCG under the ~600 mg/day hepatotoxicity ceiling while achieving full CP1a coverage. Strengthens the case for engineering both into the [koji endgame strain](./koji-endgame-strain.md) (and conversely, the §1.9 dual-cassette result becomes operationally consequential, not just architecturally elegant).
- **Additive (CI 0.7–1.3):** no dosing flexibility gained. Stack-level recommendation: dose each at its individual optimum if both are tolerated; no specific synergy claim added to [`supplements-stack.md`](./supplements-stack.md).
- **Antagonistic (CI >1.3):** unexpected — investigate whether the lactoferrin matrix interferes with EGCG bioavailability or proteasome access. Plausible mechanism: iron–EGCG chelation. Lactoferrin is a high-affinity iron-binding protein and EGCG is a known iron chelator; the apo vs. holo form of lactoferrin should differentiate iron-mediated antagonism from a direct interaction. Likely indicates one compound should be dosed alone, not in combination.

**Cross-references:** [synthesis.md](./synthesis.md) 2026-04-24 Connection #4 + Proposed Experiment #2; [lactoferrin.md](./lactoferrin.md) §3 (LPS/CD14 sequestration mechanism); [egcg.md](./egcg.md) (20S proteasome 86 nM target, hepatotoxicity ceiling); [nlrp3-exploit-map.md](./nlrp3-exploit-map.md) v1.2 CP1a (independent input/output barrier framing); [supplements-stack.md](./supplements-stack.md) (current standalone entries for both compounds); [koji-endgame-strain.md](./koji-endgame-strain.md) (downstream engineering implication, gated on §1.9).

---

### 1.21 Natural-Product C5aR1 Antagonist Screening — Computational Pass (Closes the CP0 Fermentable-Coverage Question)

**Status**: Closed (negative result, 2026-04-27) | **Cost**: $0 | **Weeks**: 0.5 | **Phase**: 1 (computational, complete)

**Affected wiki**: [complement-c5a-gout](./complement-c5a-gout.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) (CP0), [open-enzyme-vision](./open-enzyme-vision.md) (CP0 gap statement).

**What it tests:** The Open Enzyme platform has a structural gap at **CP0** — the complement-priming chokepoint where MSU crystals → classical-pathway activation → C5a → C5aR1 binding on neutrophils/macrophages → non-transcriptional NLRP3 priming. CP0 is the upstream-most chokepoint in the gout cascade, and the engineered koji / yeast / supplements stack has zero coverage at this step (see [`complement-c5a-gout.md`](./complement-c5a-gout.md) §9 for the full gap analysis and [`open-enzyme-vision.md`](./open-enzyme-vision.md) "CP0 gap — honest acknowledgment"). Avacopan (Tavneos, FDA-approved 2021 for ANCA vasculitis, oral C5aR1 allosteric antagonist) is the pharma adjunct here — and it is a synthetic small molecule, not a natural-product analog. This experiment runs a fast, free computational scan to either (a) surface a natural-product C5aR1 antagonist worth wet-lab triage — opening a fermentable lead at CP0 — or (b) definitively close the door on natural-product CP0 coverage and lock in "CP0 requires a pharma adjunct" as the platform thesis. The hit-rate prior was low: known C5aR1 antagonists are dominated by synthetic constrained peptides (PMX-53 series, JPE-1375) and synthetic small-molecule allosterics (avacopan, NDT-9513727, JNJ-27141491); the binding pocket is not a typical plant-secondary-metabolite scaffold target. Negative result was the expected and operationally useful outcome.

**Proposed in:** `wiki/synthesis.md` 2026-04-24 sweep (25-file v1.2 batch), Connection #2 + Proposed Experiment #3. Run on 2026-04-27.

**Protocol — what was actually run:**

1. **ChEMBL target confirmation and bioactivity pull.** Query ChEMBL REST API for target CHEMBL2373 (confirmed: human C5AR1, UniProt P21730, "C5a anaphylatoxin chemotactic receptor 1", G-protein-coupled receptor, single protein, *Homo sapiens*). Total bioactivity records at CHEMBL2373: **4,873** (April 2026 query). Filter the curated potent tail at pChEMBL ≥ 6 (sub-μM IC50, Ki, or EC50 against human receptor).
2. **Manual classification of the potent tail.** Walk the top ~20 highest-pChEMBL entries; classify each as synthetic vs. natural-product by inspecting molecule_type, structure_type, pref_name, and the `natural_product` flag on each ChEMBL molecule record. Distinguish "natural-product-derived synthetic peptide" (e.g., C5a C-terminal mimics) from true small-molecule natural products.
3. **Cross-database verification.** Search NPASS (Natural Products Activity & Species Source) and LOTUS (Naturally Occurring Chemical Compounds Storage) for any curated natural-product entry at C5AR1. Search NPAtlas for microbial natural products with reported C5aR1 activity.
4. **Open Targets cross-check.** Pull the C5AR1 known-drugs list from the Open Targets Platform (target ENSG00000197405) — surfaces clinical/preclinical compounds that ChEMBL may not have indexed yet, plus any natural-product-derived clinical assets.
5. **Targeted primary-literature sweep.** PubMed-via-WebSearch queries for: `"C5aR1" antagonist plant`, `"C5aR1" natural product flavonoid OR terpenoid OR alkaloid`, `"C5a receptor" inhibitor flavonoid IC50 cell-based`, `"C5aR1" inhibitor marine fungus`. Catches any plant- or microbe-source antagonist reported in primary literature without ChEMBL curation.
6. **Avacopan structural-class check.** Quick SwissSimilarity / pharmacophore scan against avacopan's cyclohexanecarboxamide / piperidine motif — most plant secondary metabolites won't share this scaffold but worth a fast pass. *(Skipped after step 5 returned <5 candidates — see "what was not run" below.)*

**What was not run, and why:** AlphaFold + AutoDock Vina docking against a curated natural-product library was deferred. The protocol gates docking on ≥5 wet-lab-validated or strongly-prior-supported natural-product candidates emerging from steps 1–5; the actual count was **0 wet-lab-validated natural-product C5aR1 antagonists**, with only 2 computational-only docking hits and 1 indirect "neutraligand" surfacing in the literature (detailed below). At <5 candidates, docking adds no signal — it would either re-derive the existing computational hits (already published) or surface novel docking-only leads of the same evidence tier as those already discounted. The wet-lab triage gate is the binding constraint, and there is nothing to triage.

**Result:**

- **Total ChEMBL bioactivities at human C5AR1 (CHEMBL2373):** 4,873 (April 2026; up from the 506 figure cited in the existing [`complement-c5a-gout.md`](./complement-c5a-gout.md) §10.1 — that older count was likely distinct compounds at a higher-confidence cutoff or an earlier ChEMBL release, not total bioactivity records; see cross-reference correction note in §10.1 follow-up).
- **Curated natural-product hits at human C5AR1 with wet-lab functional or binding data: 0.** No compound flagged `natural_product=1` in ChEMBL appears in the sub-μM potency tail. The full pChEMBL ≥ 6 list at CHEMBL2373 is dominated by synthetic cyclic peptides (PMX-53/PMX-205 series, 1995–2006 BMCL/JMC papers, IC50 18–60 nM in [125I]-C5a binding or PMN glucosaminidase release), synthetic imidazolidinones / piperazines / piperidines (the CO13 binding-competition series, IC50 25–450 nM), and clinical-stage allosteric small molecules in the avacopan structural class.
- **Apparent peptide hit, not a natural product:** CHEMBL217378 (sequence ISHKDMQLGR, EC50 1.3 nM in PMN polarization) initially looked natural-product-flavored at the sequence level but is curated as `molecule_type: "Protein"`, `natural_product: 0`, `pref_name: "ISHKDMQLGR"` — a synthetic decapeptide derived from C5a's own C-terminal sequence, designed as a receptor-engagement probe, not an isolated natural product.
- **Computational-only natural-product candidates from primary literature (no wet-lab confirmation):**
  - **Acteoside** (verbascoside; phenylethanoid glycoside; plant natural product widely distributed in *Olea europaea*, *Plantago*, *Verbascum*, *Rehmannia*, *Lamiales* generally) — Shaikh & Siu 2016, *Med Chem Res* 25:1564–1573 (PMID 27499603). Homology model of C5aR1 (Glide XP docking + MM-GBSA), ΔG_bind = −113.9 kcal/mol, XP GScore = −12.4 kcal/mol. Authors explicitly state: "biological experiments to validate this inhibitor are being planned as a future work." **No follow-up validation has been published in the decade since.** Evidence level: *Computational / homology-model docking only.*
  - **Toxicarioside** (cardiac glycoside from *Antiaris toxicaria*, the upas tree; latex traditionally used as a dart poison in Southeast Asia) — same Shaikh & Siu 2016 paper, ΔG_bind = −90.1 kcal/mol. **Not pursuable on safety grounds:** the *A. toxicaria* cardenolides (toxicariosides J/K/L/O, antiarin) are cytotoxic Na+/K+-ATPase inhibitors at sub-μM doses; this is a fundamentally toxic scaffold, fermentable or not. Evidence level: *Computational only.*
  - **Resveratrol** — Mishra et al. 2020, *J Biomol Struct Dyn* (PMID 32131707). Molecular dynamics + automated docking + MM-GBSA + circular dichroism + steady-state fluorescence biophysics. Critically, resveratrol binds **hC5a (the ligand)**, not C5aR1 (the receptor) — a "neutraligand" approach that prevents C5a from engaging C5aR1 by sequestering the soluble anaphylatoxin. Mechanistically distinct from receptor antagonism (the question this scan was framed around) but tangentially relevant. No reported potency in standard inhibitor units; the biophysics suggest binding but do not establish a functional IC50 on C5a-driven C5aR1 signaling. Evidence level: *Computational + cell-free biophysical binding; no functional assay.* Resveratrol is already on Brian's near-term radar for SIRT1 activation / NLRP3 modulation but is not promoted on this CP0-related signal alone.
- **Open Targets known-drugs list at C5AR1 (ENSG00000197405):** Avacopan (CCX-168, FDA-approved 2021, oral C5aR1 antagonist, 30 mg BID dosing, the canonical pharma reference) plus the upstream C5-binding biologics (eculizumab, ravulizumab, zilucoplan) which are not C5aR1-directed. **No natural-product-derived clinical or preclinical asset.**
- **NPASS / LOTUS:** No curated natural-product entries at C5AR1 / CHEMBL2373 surface in either database (queried 2026-04-27). NPASS contains 222,092 NP-target pairs across 5,863 targets; the absence of C5AR1 in this corpus is itself informative — it means that across the full curated natural-product activity landscape, C5AR1 has not been assayed with sufficient hit confirmation to merit a database entry.
- **Plant flavonoid CH50 literature:** As already documented in [`complement-c5a-gout.md`](./complement-c5a-gout.md) §10.2, broad complement-pathway inhibition (CH50, AP50) by quercetin, EGCG, baicalein, curcumin, resveratrol falls in the 50–500 μM range — 100–1000× weaker than synthetic C5aR1 antagonists, multi-target rather than C5aR1-selective, and not pursuable as CP0 coverage at dietary or supplement-achievable doses.

**Conclusion — CP0 fermentable coverage is closed for natural products.** The scan returned zero wet-lab-validated natural-product C5aR1 antagonists. The two computational-only plant hits (acteoside, toxicarioside) have not been functionally validated in the decade since publication despite the original authors' stated plans, and toxicarioside is non-pursuable on safety grounds anyway. Resveratrol's hC5a binding is mechanistically distinct (neutraligand, not antagonist) and biophysically weak. Avacopan remains the pharma adjunct at CP0; the engineered koji / yeast / supplements stack does not have, and structurally is unlikely to acquire, fermentable CP0 coverage. This is a useful negative result — it converts the existing CP0 gap statement from "we don't have natural-product coverage at CP0" to "we ran the scan; here is exactly what we found and exactly why avacopan is the answer," removing this question from the platform's open backlog.

**Re-open conditions:** (a) a new ChEMBL release (v35+) curates a sub-μM natural-product C5aR1 antagonist with primary-literature wet-lab confirmation; (b) a primary-literature paper reports a fermentable C5aR1 antagonist with functional cell-based or in vivo evidence; (c) avacopan loses regulatory or supply availability, raising the value of even weak fermentable backups; (d) the Shaikh & Siu 2016 group (or an independent group) publishes the long-promised in vitro validation of acteoside on C5aR1-expressing cells. Until one of these triggers, the CP0 question stays closed and the platform thesis stays "Open Enzyme covers crystal elimination upstream of CP0 + downstream chokepoints CP1–CP6; avacopan covers CP0 itself."

**Cross-references:** [complement-c5a-gout.md](./complement-c5a-gout.md) §9 (CP0 platform gap) + §10 (natural-product modulator literature); [nlrp3-exploit-map.md](./nlrp3-exploit-map.md) (CP0 chokepoint); [open-enzyme-vision.md](./open-enzyme-vision.md) ("CP0 gap — honest acknowledgment"); [synthesis.md](./synthesis.md) 2026-04-24 Connection #2 + Proposed Experiment #3. Source: ChEMBL CHEMBL2373 (April 2026); Open Targets ENSG00000197405; Shaikh F, Siu SWI. *Med Chem Res* 25:1564–1573 (2016, PMID 27499603); Mishra et al. *J Biomol Struct Dyn* 2020 (PMID 32131707).

---

### 1.22 Gut-Selective Food-Grade HDAC Inhibitor Screen for Q141K-ABCG2 Trafficking Rescue

**Status**: Proposed | **Cost**: $5,000–8,000 | **Weeks**: 8–10 | **Phase**: 1

**Affected wiki**: [abcg2-modulators](./abcg2-modulators.md), [supplements-stack](./supplements-stack.md), [gut-lumen-sink](./gut-lumen-sink.md)

**What it tests:** The Q141K variant of ABCG2 (~12% population allele frequency; ~25% of East Asian, ~4% of European populations) produces a misfolded protein that is retained in the endoplasmic reticulum rather than trafficked to the apical membrane. HDAC inhibition (specifically class I HDACs — HDAC1/2/3) rescues this trafficking defect by upregulating Hsp90 chaperoning via HSF1 activation (Basseville et al. 2012, PMID 22472121). Butyrate (sodium butyrate, food-grade) is the known food-grade class I HDACi that rescues Q141K ABCG2 trafficking at ~1 mM concentrations achievable in the colon via fermentable fiber. However, butyrate's efficacy depends on microbiome composition and fiber intake — there is no reliable way to deliver a specific dose from diet. This experiment screens alternative food-grade HDACi candidates for (a) class I HDAC selectivity over HDAC6, (b) gut-enriched activity (Caco-2 ≥ hepatocyte potency), (c) trafficking-rescue efficacy at concentrations achievable via food or supplement, and (d) absence of hepatotoxicity signal (the reason vorinostat/SAHA remains oncology-restricted).

**Proposed in:** `wiki/synthesis.md` 2026-05-05 Proposed Experiment #3. Per the Pass 3 review: the design must include a tissue-selectivity assay (Caco-2 vs. hepatocyte HDAC activity as primary screen discriminator) and explicit HDAC1/2/3 isoform focus; HDAC6 inhibition is off-target for this purpose and is a pan-tissue toxicity risk. Original cost estimate ($5,000) was flagged as optimistic if the selectivity criterion is operationalized; revised to $5,000–8,000 to include paired Caco-2/hepatocyte HDAC activity assays.

**Background on Q141K mechanism:** ABCG2-Q141K's ATP-binding domain folds incorrectly at the NBD2 interface → ERAD (ER-associated degradation) retention → reduced apical transporter density → impaired urate efflux. HDACi → Hsp90α/β upregulation + HSF1 nuclear translocation → ↑chaperone-assisted folding of the misfolded NBD2 → partial membrane-trafficking rescue. Cells transfected with Q141K ABCG2 show ~30–50% restoration of surface expression at butyrate 1 mM (Basseville 2012). The clinical relevance: Q141K homozygotes on clomid/TRT with low fermentable-fiber intake are the hardest-to-rescue subgroup; a direct food-grade HDACi supplement would be meaningful.

**Protocol:**

**Stage 1 — In silico candidate selection ($500):**
- Compile known food-grade or GRAS-adjacent compounds with documented HDAC inhibition: butyrate/short-chain fatty acids (the known benchmark), sulforaphane (indirect via Nrf2/keap1, class I-relevant), allyl mercaptan (garlic-derived, reported class I HDACi), phenethyl isothiocyanate (PEITC, cruciferous), hydroxycinnamic acids (caffeic acid, ferulic acid), diallyl disulfide (DADS).
- Screen each candidate against: class I HDAC (HDAC1/2/3) IC50 from ChEMBL / primary literature; HDAC6 IC50 (if known — selectivity check); Caco-2 permeability / gut-lumen-achievable concentration estimate; reported hepatotoxicity signal (LD50 or NOAEL from TOXNET / EFSA).
- Select top 5–7 candidates by gut-enriched concentration × class I HDAC potency ratio.

**Stage 2 — Paired Caco-2 / hepatocyte HDAC activity assay ($2,000–3,000):**
- **Cell lines:** Caco-2 (enterocyte model) and HepG2 or primary human hepatocytes (hepatocyte model). The primary screen discriminator is Caco-2 HDAC activity ÷ hepatocyte HDAC activity for each candidate at matched concentrations. Gut-selective candidates have ratio > 2 (more HDAC inhibition in enterocytes than hepatocytes).
- **Readout:** Fluorometric HDAC activity assay (FLUOR DE LYS-based or equivalent) in nuclear extracts from each cell type + 24h candidate treatment.
- **HDAC1/2/3 vs. HDAC6 isoform specificity:** use a class I-selective substrate (acetylated H3K9/H4K12 peptide) and a HDAC6-selective substrate (acetylated tubulin peptide) to distinguish isoform selectivity within the Caco-2 data.

**Stage 3 — Q141K ABCG2 trafficking rescue in HEK293T or Caco-2 Q141K-transfected cells ($2,500–4,500):**
- Transfect cells with ABCG2-Q141K-GFP construct (standard overexpression assay, as in Basseville 2012).
- Treat with top 3 candidates (from Stage 2) at Caco-2-achievable concentrations ± butyrate 1 mM (positive control).
- Readouts: ABCG2 surface expression (flow cytometry / confocal — ratio of membrane-localized to total GFP signal), urate efflux (transwell if Caco-2-based), ABCG2 protein abundance (Western — total vs. glycosylated mature form).

**HDAC isoform note:** HDAC1/2/3 (class I, nuclear) → histone deacetylation → Hsp90/HSF1 → Q141K rescue. HDAC6 (class IIb, cytoplasmic) → tubulin deacetylation → autophagy regulation. Pan-HDAC inhibitors (vorinostat, romidepsin) hit HDAC6 → actin dysregulation, cardiac ion-channel effects → cardiotoxicity. Any candidate that shows Caco-2 vs. hepatocyte selectivity AND class I >> HDAC6 selectivity is safe to advance; pan-inhibitors are excluded regardless of efficacy.

**Estimated cost:** $5,000–8,000 (in silico $500 + Caco-2/HepG2 HDAC assay $2,000–3,000 + trafficking rescue $2,500–4,500). Original synthesis proposal ($5,000) was optimistic for a design that includes paired tissue-selectivity assay; $8,000 covers the paired hepatocyte arm + Q141K-transfected cell assay.

**Estimated timeline:** 8–10 weeks.

**Success criteria:**
- **A food-grade HDACi candidate that outperforms butyrate on selectivity (higher Caco-2:hepatocyte ratio AND HDAC1/2/3 >> HDAC6) AND rescues Q141K surface expression ≥20%:** advances to Q141K-targeted supplement protocol, potentially as a co-expression candidate in the koji endgame strain.
- **No candidate outperforms butyrate on selectivity:** confirms butyrate as the best available food-grade Q141K-rescue agent and locks in the fermentable-fiber adjunct recommendation for Q141K carriers.
- **A candidate with class I selectivity and hepatocyte-sparing profile emerges but doesn't rescue trafficking:** updates the Q141K rescue model (suggests additional misfolding mechanism beyond class I HDAC).

**Cross-references:** [abcg2-modulators.md](./abcg2-modulators.md) §6 (butyrate + PPARγ/HDACi mechanism; Basseville 2012 PMID 22472121); [supplements-stack.md](./supplements-stack.md) §"Q141K-personalized recommendations"; [gut-lumen-sink.md](./gut-lumen-sink.md); [synthesis.md](./synthesis.md) 2026-05-05 Proposed Experiment #3.

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

### 3.10 Brian: Fructose Challenge Test as Acute n=1 Uricase Efficacy Readout

**Status**: Proposed | **Cost**: ~$50 | **Weeks**: 0.1 per run (single 2-hour session); ~4 wk gap between baseline and post-intervention | **Phase**: 3

**Affected wiki**: [fructose-connection](./fructose-connection.md), [self-experiment-protocol](./self-experiment-protocol.md), [synthesis](./synthesis.md), [open-enzyme-vision](./open-enzyme-vision.md)

**What it tests:** Whether engineered uricase is active in the gut in real-time, using a fructose bolus as a predictable acute UA challenge. Per [fructose-connection.md](./fructose-connection.md), oral fructose loads generate a serum UA spike within 60–120 min via the unregulated KHK pathway. A blunted post-fructose UA spike after starting koji therapy directly validates uricase action in the gut — without waiting weeks for baseline UA to drift on chronic monitoring.

**Proposed in:** `wiki/synthesis.md` 2026-04-27 Proposed Experiment #1 (sweep on commit `b7df491`). Pass 3 review: highest insight-per-dollar experiment in the queue, elevated to Priority Action status. Within-subject before/after design controls for most confounders (genetics, kidney function, baseline diet) — the only systematic variable changing between runs is the koji intervention.

**Protocol:**
- **Subject:** Brian (n=1).
- **Pre-load conditions:** 8-hour fasted; baseline UA established (UASure home meter or equivalent, **duplicate readings at each timepoint** per Pass 3 review to manage UASure CV ~10–15%).
- **Challenge:** 50 g fructose load (oral) — standardized matrix (water-dissolved); record exact dose and dissolution medium.
- **Sampling:** Fingerstick UA at t = 0, 30, 60, 90, 120 minutes. Duplicate at each timepoint. Record peak UA delta from baseline.
- **Run #1 (baseline):** Before any engineered-koji intervention. Establishes Brian's individual fructose-induced UA spike profile under current stack.
- **Run #2 (post-intervention):** After ≥4 weeks of stable koji therapy (engineered when available; wild-type baseline as interim per the multi-vendor metabolite campaign). Same protocol exactly.
- **Optional Run #3 (washout):** Off-koji washout after the post-intervention run to confirm reversibility (rules out baseline drift or concurrent variable shifts).

**Estimated cost:** ~$50 — UASure meter ~$25, strips ~$15 for the panel (10 readings × 2 runs = 20 strips minimum), fructose ~$5, miscellaneous.

**Estimated timeline:** 2 hours per session; ~4 weeks elapsed between baseline and post-intervention runs (matches stable plateau on a new koji regimen).

**Dependencies:** No specialized lab access. Self-administered. Slots cleanly into the operational backlog tracked separately on the personal-health side.

**Success criteria:**
- **Validates engineered uricase activity:** post-intervention UA spike at t = 60–90 min is ≥30% reduced vs. baseline run, with the koji intervention as the only changed variable. Effect size scales with how much of the fructose-derived urate is degraded by gut-lumen uricase before systemic absorption.
- **Null result:** spike unchanged. Possible interpretations: insufficient uricase expression / activity, fructose absorbs faster than uricase can degrade the resulting urate, or the koji format isn't delivering active enzyme to the lumen. Triages next experimental questions (e.g., §1.10 stability, §1.6 enzyme survival).
- **Adverse:** spike worsens — suggests run-to-run variance dominated by other factors. Add additional baseline runs to characterize variance before re-interpreting.

**Caveats and confounds:**
- UASure CV ~10–15% — duplicate readings + ≥30% effect-size threshold helps separate signal from noise.
- Brian's clomid taper is in flight (UA mobilization risk during T transition). Schedule the runs to either bracket or sit firmly inside one phase of that taper to avoid confounding.
- Hydration status confounds UA: standardize water intake (e.g., 500 mL on waking, no other fluids during the 2-hour window).
- Recent flares within 4 weeks change baseline UA dynamics — defer until 4+ weeks post-flare.

**Cross-references:** [synthesis.md](./synthesis.md) 2026-04-27 Proposed Experiment #1; [fructose-connection.md](./fructose-connection.md); [self-experiment-protocol.md](./self-experiment-protocol.md).

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
