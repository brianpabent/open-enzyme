---
title: Validation Experiments
aliases: [experiments, validation, testing phases]
related: [engineered-yeast-uricase-proposal, engineered-koji-protocol, etc/open-source-platform, supplements-stack]
sources: [engineered-yeast-uricase-proposal.md, engineered-koji-protocol.md, etc/open-enzyme-vision.md, nlrp3-exploit-map.md, gout-deep-dive.md]
---

# Validation Experiments

## Overview

Consolidated experiment library for testing exploitable gout weaknesses, candidate mechanisms, exposure, safety, and delivery. The queue is ordered by scientific dependency: establish physiological relevance and target engagement before optimizing a production route or combination.

Some early protocols are host-specific because they arose within mature engineering tracks. That history does not set portfolio priority. Cross-route experiments belong here when they test a shared gout mechanism; implementation-only tests remain linked from the relevant dossier.

---

## Experiment Queue

Dashboard view of registered experiments. Detail lives in the phase sections below.

**Status legend:**
- **Proposed** — no work done yet; in the design/queue stage.
- **In Progress** — active wet-lab or analytical work underway.
- **Done** — completed with results captured in the protocol section or a referenced wiki page.
- **Abandoned** — deprioritized or replaced; reason noted inline.

Open Enzyme remains Phase 0 — Research & Design. Wet-lab protocols are Proposed unless their section says otherwise; computational entries carry their own current status.

> **Planning-number contract:** In Proposed and Design-only sections, a cost, vendor quote, assay concentration, or pass/fail threshold is a provisional design hypothesis unless the section ties it to a primary method, a qualified-assay specification, or pilot data. Before result-bearing execution, freeze the exact material, controls, assay precision, smallest useful effect, decision thresholds, cost, and stopping rules with explicit provenance. An unverified threshold may organize a pilot; it is not a binding biological gate or evidence that the target is achievable.
>
> **Current gout-program decision order:** First create and characterize candidate UOX configurations in the relevant host or delivery material ([§§1.1, 1.2, and 1.5](#11-uricase-gene-performance-comparison)). [§1.33](#133-physiological-uox-topology--oxygen--peroxide-factorial) then compares those extant configurations under the same substrate, oxygen, product, peroxide, localization, and viability framework. Within-host comparisons may nominate a topology; cross-host comparisons remain configuration-specific because chassis, expression, localization, and support machinery are confounded. [§1.36](#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) follows for each surviving configuration before animal escalation. [§1.34](#134-isotope-resolved-dietary-precursor--uox--pdb-sequential-flux) independently tests staged precursor/PDB flux. In the track-local §1.9 sequence, lactoferrin-only Stage A may run in parallel; Stage B uses a koji configuration advanced by §1.33; and dual-cassette Stage C starts only after both single-cassette arms pass. These host-specific experiments do not determine which gout weakness ranks first.
>
> Shared-batch expression work may reduce cost, but it does not change the biological dependency order or establish combination value.

| ID | Title | Category | Cost | Weeks | Status | Wiki refs |
|----|-------|----------|------|-------|--------|-----------|
| [§1.1](#11-uricase-gene-performance-comparison) | Uricase gene performance comparison | In Vitro | $2,000–3,000 | 4–6 | Proposed | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [uricase-variant-selection](./uricase-variant-selection.md), [uricase](./uricase.md), [codon-optimization-expression-cassette](./codon-optimization-expression-cassette.md) |
| [§1.2](#12-secretion-vs-intracellular-expression) | Yeast topology-panel build and characterization | In Vitro | $500–1,000 | 2–3 | Proposed — supplies §1.33 | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [saccharomyces-cerevisiae](./saccharomyces-cerevisiae.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.3](#13-uricase-survival-in-beer-fermentation) | Selected UOX configuration through beer processing | In Vitro | $200–400 | 3–4 | Proposed — conditional after §1.33 | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [saccharomyces-cerevisiae](./saccharomyces-cerevisiae.md) |
| [§1.4](#14-uricase-stability-after-drying) | Selected UOX configuration through drying | In Vitro | $300–800 | 1–2 | Proposed — conditional after §1.33 | [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.5](#15-koji-uricase-expression-and-activity) | Koji topology-panel build and characterization | In Vitro | $1,500–2,500 | 4–6 | Proposed — supplies §1.33 | [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [koji-construct-design](./koji-construct-design.md), [uricase](./uricase.md) |
| [§1.33](#133-physiological-uox-topology--oxygen--peroxide-factorial) | **Configuration-level physiological UOX × oxygen × peroxide factorial** | In Vitro | TBD | TBD | Proposed — after construct supply | [gut-lumen-sink](./gut-lumen-sink.md), [uricase-topology-oxygen-peroxide-design-computational](./uricase-topology-oxygen-peroxide-design-computational.md) |
| [§1.6](#16-koji-enzyme-stability-at-digestive-ph-and-temperature) | Advanced koji UOX configuration through digestive challenge | In Vitro | $300–600 | 1–2 | Proposed — after §§1.5 and 1.33 | [engineered-koji-protocol](./engineered-koji-protocol.md), [gi-survival-prediction](./gi-survival-prediction.md), [digestive-enzymes](./digestive-enzymes.md) |
| [§1.7](#17-nlrp3-inflammasome-pathway-validation-thp-1-msu-macrophage-assay) | NLRP3 pathway validation (THP-1 MSU macrophage) | In Vitro | $5,000–8,000 | 8–10 | Proposed | [nlrp3-exploit-map](./nlrp3-exploit-map.md), [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md), [egcg](./egcg.md) |
| [§1.8](#18-egcg-dose-escalation-on-msu-stimulated-thp-1-tnfsf14-induced-il-6-readout-cp1a) | EGCG dose-escalation CP1a readout | In Vitro | $500–800 | 3–4 | Proposed | [egcg](./egcg.md), [tnfsf14-gout-target](./tnfsf14-gout-target.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) |
| [§1.9](#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate) | **Ward 1995 staged Lf-only → selected UOX-only → dual-cassette feasibility** — conditional #1 koji multi-payload gate | In Vitro | $5,265–8,065 (full path) | 8–12 | Proposed | [koji-endgame-strain](./koji-endgame-strain.md), [lactoferrin](./lactoferrin.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md) |
| [§1.10](#110-heterologous-uricase-lactoferrin-stability-in-shio-koji-salt-protease-ferment) | Uricase + lactoferrin stability in shio-koji ferment (gates dual-use thesis for both payloads) | In Vitro | $2,100–4,100 core; microbial QC TBD | 3–4 | Proposed — UOX decision after §1.33 | [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [lactoferrin](./lactoferrin.md), [synthesis/](../synthesis/README.md) |
| [§1.11](#111-ergothioneine-abcg2-induction-in-caco-2-native-koji-synergy-test) | Ergothioneine → ABCG2 Caco-2 (native koji synergy) | In Vitro | $1,000–1,500 | 3–4 | Proposed | [abcg2-modulators](./abcg2-modulators.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.12](#112-local-h2o2-stress-in-caco-2-from-the-selected-uox-configuration) | Selected-UOX epithelial H₂O₂ characterization | In Vitro | $800–1,200 | 2–3 | Proposed — after §1.33 | [uricase](./uricase.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.13](#113-limonene-abcg2-induction-in-caco-2-tier-3-stack-synergy-test) | Limonene → ABCG2 Caco-2 (Tier-3 stack synergy) | In Vitro | $800–1,200 | 3–4 | Proposed | [supplements-stack](./supplements-stack.md), [abcg2-modulators](./abcg2-modulators.md), [cannabinoids-terpenes](./cannabinoids-terpenes.md) |
| [§1.14](#114-abcg2-response-to-dht-and-tnf-with-butyrate-and-lactoferrin-rescue) | Direction-finding DHT × TNFα ABCG2 factorial + butyrate/lactoferrin response + supplement antagonism + Q141K arm | In Vitro | $2,300–4,300 | 4–6 | Proposed | [abcg2-modulators](./abcg2-modulators.md), [androgen-urate-axis](./androgen-urate-axis.md), [gut-lumen-sink](./gut-lumen-sink.md), [lactoferrin](./lactoferrin.md), [supplements-stack](./supplements-stack.md), [koji-endgame-strain](./koji-endgame-strain.md) |
| [§1.15](#115-rice-bran-substrate-koji-uricase-gi-survival) | Matrix comparison for the selected koji UOX configuration | In Vitro | $800–1,200 | 3 | Proposed — after §§1.33 and 1.5 | [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.16](#116-candidate-uox-variants-in-koji-sequential-retained-activity-screen) | Candidate UOX variants in an advanced koji configuration | In Vitro | TBD | TBD | Proposed — after §§1.5 and 1.33 | [engineered-koji-protocol](./engineered-koji-protocol.md), [uricase-variant-selection](./uricase-variant-selection.md), [protein-engineering-strategy](./protein-engineering-strategy.md) |
| [§1.17](#117-quercetin-ursolic-acid-carnosine-three-way-synergy-on-msu-stimulated-thp-1) | Quercetin × ursolic × carnosine 3-way synergy (THP-1 MSU) | In Vitro | $1,500–2,000 | 3–4 | Proposed | [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md), [carnosine](./carnosine.md) |
| [§1.18](#118-native-koji-enzyme-sgf-survival-free-extract-vs-whole-biomass-2-arm) | Native koji enzyme SGF (free extract vs. whole biomass) | In Vitro | $300–500 | 2 | Proposed | [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.19](#119-methodological-standard-rodent-cellular-ic50-translation-caveat) | Methodology — rodent cellular IC50 translation caveat | Standing | $0 | ongoing | Standing | [chembl-cross-check](./etc/chembl-cross-check.md), [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md) |
| [§1.20](#120-lactoferrin-egcg-cp1a-super-additivity-assay-thp-1-macrophage-33-full-factorial--prespecified-midpoint) | Lactoferrin + EGCG CP1a interaction (THP-1 3×3 full factorial + prespecified midpoint); recombinant Lf can run now | In Vitro | $1,500 | 3–4 | Proposed | [lactoferrin](./lactoferrin.md), [egcg](./egcg.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [supplements-stack](./supplements-stack.md), [koji-endgame-strain](./koji-endgame-strain.md) |
| [§1.21](#121-natural-product-c5ar1-antagonist-screening-computational-pass-closes-the-cp0-fermentable-coverage-question) | Natural-product C5aR1 antagonist screen (CP0 fermentable-coverage question) | Computational | $0 | 0.5 | **Closed (negative, 2026-04-27)** | [complement-c5a-gout](./complement-c5a-gout.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [open-enzyme-vision](./etc/open-enzyme-vision.md) |
| [§1.22](#122-gut-compartment-hdac-directed-candidate-screen-for-q141k-abcg2-trafficking-rescue) | Gut-compartment HDAC-directed candidate screen for Q141K-ABCG2 trafficking rescue | In Vitro | $5,000–8,000 | 8–10 | Proposed | [abcg2-modulators](./abcg2-modulators.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.23](#123-androgen-msu-nlrp3-in-macrophages-tiered-mechanistic-protocol) | Androgen × MSU × NLRP3 macrophage tiered protocol (T1 THP-1 / T2 PBMC / T3 mouse air-pouch) — fills literature gap | In Vitro | Tier 1: $5–10K; full T1+T2+T3 cascade $105–160K | Tier 1: 6–8; full cascade ~12 months | Proposed | [androgen-urate-axis](./androgen-urate-axis.md), [nlrp3-inflammasome](./nlrp3-inflammasome.md) |
| [§1.24](#124-carnosine-co-expression-validation-in-a-oryzae-koji-endgame-optional-third-cassette) | Carnosine co-expression in *A. oryzae* (koji multi-payload optional third cassette) | In Vitro | $1,500–2,500 | 4–6 | Proposed | [koji-endgame-strain](./koji-endgame-strain.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [carnosine](./carnosine.md), [androgen-urate-axis](./androgen-urate-axis.md) |
| [§1.25](#125-dafcd55-scr1-4-truncated-single-cassette-expression-in-a-oryzae-cp0-engineering-candidate-wet-lab-gate) | DAF SCR1-4 single-cassette expression in *A. oryzae* (CP0 candidate + downstream chaperone calibration) | In Vitro | $4,445–6,745 (two-arm) | 6–8 | Proposed | [daf-cd55-scr14-truncated-computational](./daf-cd55-scr14-truncated-computational.md), [hypotheses/H05-daf-scr14-cp0-thesis](./hypotheses/H05-daf-scr14-cp0-thesis.md), [chaperone-orthogonal-stacking](./chaperone-orthogonal-stacking.md), [complement-c5a-gout](./complement-c5a-gout.md) |
| [§1.26](#126-cordycepin--pentostatin--glpp--five-arm-ada-half-life-assay-ada-chokepoint-synergy-validation) | Cordycepin × pentostatin × GLPP five-arm ADA half-life assay | In Vitro | $1,500–2,500 | 3–4 | Proposed | [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [gout-pathophysiology](./gout-pathophysiology.md) |
| [§1.27](#127-ergothioneine--lactoferrin-interaction-assay-in-msu-stimulated-thp-1-macrophages) | Ergothioneine × lactoferrin interaction in MSU-stimulated THP-1 macrophages | In Vitro | TBD | TBD | Proposed | [lactoferrin](./lactoferrin.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) |
| [§1.28](#128-tier-2-colorimetric-cordycepin-assay-validation) | Tier 2 colorimetric cordycepin assay validation | In Vitro | ~$200 | 2 | Proposed | [quantification-ladder](./quantification-ladder.md), [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md) |
| [§1.29](#129-cordycepin--pentostatin--substrate-matrix) | Cordycepin × pentostatin exact-configuration medium effects | In Vitro | TBD | TBD | Proposed — pilot design required | [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [medicinal-mushroom-extract-sops](./medicinal-mushroom-extract-sops.md) |
| [§1.30](#130-houttuynia-cordata-polysaccharide-fraction-comparison-in-msu-stimulated-thp-1-macrophages--prioritization-screen) | *Houttuynia cordata* polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages | In Vitro | ~$1,500–2,500 | 4–6 | Proposed | [nlrp3-exploit-map](./nlrp3-exploit-map.md), [medicinal-mushroom-extract-sops](./medicinal-mushroom-extract-sops.md) |
| [§1.31](#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms) | Butyrate culture-supernatant HPLC-UV method transfer against GC-MS | In Vitro | TBD | TBD | Proposed — partner design required | [tier-2-butyrate-assay-audit-computational](./tier-2-butyrate-assay-audit-computational.md), [quantification-ladder](./quantification-ladder.md) |
| [§1.32](#132-gsdmd-pore-self-delivery--selectivity-probe-transporter-orphan-tracer--pept1-blockade) | GSDMD-pore self-delivery selectivity probe | In Vitro | ~$2,000–5,000 | 4–6 | Proposed (wet-lab gated) | [gsdmd-pore-delivery-paradox](./gsdmd-pore-delivery-paradox.md), [kpv-gsdmd-pore-influx-computational](./kpv-gsdmd-pore-influx-computational.md) |
| [§1.44](#144-thymulin--msu--nlrp3-in-aged-macrophages-thy-1--age-stratified-priming-to-flare-test) | Thymulin (+Zn²⁺) × MSU × NLRP3 in **aged** macrophages (THY-1) — tests whether NF-κB priming block translates to reduced crystal-driven IL-1β; age-stratified | In Vitro | Tier 1: $5–10K; full T1+T2+T3 cascade $85–130K | Tier 1: 6–8; full cascade ~11 months | Proposed | [thymulin](./thymulin.md), [nlrp3-inflammasome](./nlrp3-inflammasome.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [peptide-gout-addendum](./peptide-gout-addendum.md) |
| [§1.34](#134-isotope-resolved-dietary-precursor--uox--pdb-sequential-flux) | Isotope-resolved precursor → UOX → PDB sequential flux — parallel first-wave architecture gate | In Vitro | TBD | TBD | Proposed | [purine-degrading-bacteria](./purine-degrading-bacteria.md), [staged-purine-sink-mass-balance-computational](./staged-purine-sink-mass-balance-computational.md) |
| [§1.36](#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) | Luminal urate antioxidant-loss × UOX-H₂O₂ safety — post-topology safety gate | In Vitro | TBD | TBD | Proposed | [uricase](./uricase.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.35](#135-enterocyte-nlrp3pdzk1abcg2-tissue-paradox-assay) | Enterocyte NLRP3–PDZK1–ABCG2 tissue-paradox assay | In Vitro | TBD | TBD | Proposed | [nlrp3-exploit-map](./nlrp3-exploit-map.md), [abcg2-modulators](./abcg2-modulators.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.37](#137-cbt20-carbon-fate-and-pdb-self-niche-test) | CBT2.0 carbon-fate and PDB self-niche test | In Vitro | TBD | TBD | Proposed — before renewed UOX/PDB modeling | [purine-degrading-bacteria](./purine-degrading-bacteria.md), [dual-chassis-ecn-pdb-uricase-computational](./dual-chassis-ecn-pdb-uricase-computational.md) |
| [§1.38](#138-t0ss-uox-omv-gut-to-systemic-bridge-assay) | T0SS UOX-OMV gut-to-systemic bridge assay | In Vitro | TBD | TBD | Proposed — alternate-route gate | [blood-barrier-exploits](./blood-barrier-exploits.md), [delivery-route-matrix](./delivery-route-matrix.md) |
| [§1.39](#139-fructose--khk--nox--abcg2-human-enteroid-test) | Fructose × KHK × NOX × ABCG2 human-enteroid test | In Vitro | TBD | TBD | Proposed | [fructose-connection](./fructose-connection.md), [abcg2-modulators](./abcg2-modulators.md) |
| [§1.40](#140-cd39cd73adenosine-gout-resolution-time-course) | CD39/CD73–adenosine gout-resolution time course | In Vitro | TBD | TBD | Proposed | [gout-pathophysiology](./gout-pathophysiology.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) |
| [§1.41](#141-parallel-fxrabcg2-and-tgr5nlrp3-bile-acid-screen) | Parallel FXR–ABCG2 and TGR5–NLRP3 bile-acid screen | In Vitro | TBD | TBD | Proposed | [abcg2-modulators](./abcg2-modulators.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [open-questions](./open-questions.md) |
| [§1.42](#142-succinate-compartment-dissociation-hepatic-ampd2-vs-immune-sucnr1) | Succinate compartment-dissociation: hepatic AMPD2 vs. immune SUCNR1 | In Vitro | TBD | TBD | Proposed | [tcm-gout-compound-triage-computational](./tcm-gout-compound-triage-computational.md), [gout-pathophysiology](./gout-pathophysiology.md) |
| [§1.43](#143-pdb--allopurinoloxypurinolfebuxostat-interaction-assay) | PDB × allopurinol/oxypurinol/febuxostat interaction assay | In Vitro | TBD | TBD | Proposed | [purine-degrading-bacteria](./purine-degrading-bacteria.md), [gout-deep-dive](./gout-deep-dive.md) |
| [§2.1](#21-selected-uox-configuration-in-vivo-persistence-and-localization) | Selected UOX configuration: in-vivo persistence and localization | Animal | TBD after model selection | TBD | Proposed — after §§1.33 and 1.36 | [gut-lumen-sink](./gut-lumen-sink.md), [uricase](./uricase.md), [team](./etc/team.md) |
| [§2.2](#22-selected-oral-uox-configuration-in-vivo-efficacy-and-safety) | Selected oral UOX configuration: in-vivo efficacy and safety | Animal | TBD after model selection | TBD | Proposed — after §2.1 | [gut-lumen-sink](./gut-lumen-sink.md), [gout-deep-dive](./gout-deep-dive.md), [uricase](./uricase.md) |
| [§2.3](#23-engineered-koji-efficacy-in-digestive-enzyme-deficient-model) | Engineered koji EPI model | Animal | $6,000–10,000 | 8–10 | Proposed | [engineered-koji-protocol](./engineered-koji-protocol.md), [digestive-enzymes](./digestive-enzymes.md), [enzyme-deficit-deep-dive](./enzyme-deficit-deep-dive.md) |
| [§2.4](#24-nlrp3-inflammasome-inhibition-in-msu-crystal-arthritis-model) | NLRP3 inhibition in MSU arthritis model | Animal | $10,000–15,000 | 10–12 | Proposed | [nlrp3-exploit-map](./nlrp3-exploit-map.md), [nlrp3-inflammasome](./nlrp3-inflammasome.md), [gout-deep-dive](./gout-deep-dive.md), [supplements-stack](./supplements-stack.md) |
| [§2.5](#25-pulse-probiotic-validation-in-hyperuricemic-mice) | PULSE probiotic validation (hyperuricemic mice) | Animal | TBD after pilot and model selection | TBD | Proposed — after §§1.33, 1.36, and 2.1 | [gout-deep-dive](./gout-deep-dive.md), [gout-clinical-pipeline](./gout-clinical-pipeline.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§2.6](#26-glpp--cordycepin-interaction-in-hyperuricemia--matched-wet-lab-gate-phase-7-4-stub) | GLPP + cordycepin interaction in hyperuricemia — matched wet-lab gate | Animal | TBD | TBD | Proposed — design pending exact material and pilot data | [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [hypotheses/H06-medicinal-mushroom-complement-track](./hypotheses/H06-medicinal-mushroom-complement-track.md) |
| [§2.7](#27-koji--cordyceps-co-formulation-stability-test--ada-challenge-assay--deprioritized-2026-05-16-archived-2026-05-29) | Koji × *Cordyceps* co-formulation stability test | In Vitro | N/A (archived) | N/A (archived) | Abandoned — recover from Git only if decision-relevant | [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md) |
| [§3.3](#33-wild-type-fungal-enzyme-timing-study-design) | Wild-type fungal-enzyme timing study design | Human | TBD | TBD | Design only — gated on characterized material and oversight | [digestive-enzymes](./digestive-enzymes.md), [enzyme-quantification-protocol](./enzyme-quantification-protocol.md) |

---

## Phase 1: In Vitro Validation

### 1.1 Uricase Gene Performance Comparison

**Status**: Proposed | **Cost**: $2,000–3,000 | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [uricase-variant-selection](./uricase-variant-selection.md), [uricase](./uricase.md), [codon-optimization-expression-cassette](./codon-optimization-expression-cassette.md)

**What it tests:** Which uricase gene (Aspergillus flavus, Candida utilis, or Vibrio vulnificus) performs best in S. cerevisiae?


**Protocol:**
- Order codon-optimized synthetic genes for all three candidates (*A. flavus*, *C. utilis*, *V. vulnificus*)
- Each in the same expression cassette (pTEF1 promoter, CYC1 terminator)
- Integrate at the same chromosomal locus in S. cerevisiae
- Compare: (a) expression level by Western blot, (b) specific uricase activity in cell lysate, (c) enzyme stability at 37°C over 24h

**Estimated cost:** $2,000–3,000 (gene synthesis ~$0.10/bp × ~900 bp × 3 genes + reagents)

**Estimated timeline:** 4–6 weeks

**Dependencies:** None

**Success criteria:** Estimate assay precision, then identify any reproducible gene-level difference under matched construct conditions. This screen does not use a fixed activity threshold and cannot establish physiological luminal sufficiency; any winner must enter §1.33 before topology or dose promotion.

**Pre-gate option (deferred 2026-05-13; rationale narrowed 2026-07-13) — Ginkgo Cloud Lab cell-free expression ($39/protein, ~5–10 day turnaround):** A cell-free run can test whether an ORF translates and remains soluble in an *E. coli*-lysate-like environment. It cannot resolve fungal-host folding or the physiological luminal regime, and comp-019 no longer supports skipping those gates. Use this only if translation/solubility becomes the immediate bottleneck; §1.33 is the relevant UOX-system gate.

---

### 1.2 Secretion vs. Intracellular Expression

**Status**: Proposed | **Cost**: $500–1,000 | **Weeks**: 2–3 | **Phase**: 1

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [saccharomyces-cerevisiae](./saccharomyces-cerevisiae.md), [gi-survival-prediction](./gi-survival-prediction.md)

**What it tests:** Whether a matched set of intracellular, released, secreted, or displayed UOX configurations can be built and characterized in *S. cerevisiae* well enough to enter §1.33. This is construct supply and baseline characterization; it does not select a physiological winner.


**Protocol:**
- Build the prespecified yeast configurations in the same host background with matched active-UOX, inactive-UOX, and chassis-only controls.
- Freeze the payload sequence and all construct features except the localization variable for a within-host topology comparison. Record any feature that cannot be matched.
- Quantify total, soluble, and active UOX in the relevant cellular and extracellular fractions.
- Verify sequence identity, localization, baseline product formation, H₂O₂, dissolved oxygen, viability, and batch variance under a common characterization condition before supplying qualified material to §1.33.

**Estimated cost:** $500–1,000

**Estimated timeline:** 2–3 weeks

**Dependencies:** A prespecified payload and matched construct plan. §1.1 may nominate the payload or run in parallel if the baseline comparator is frozen in advance.

**Success criteria:** Supply sequence-verified configurations with interpretable localization, active-UOX recovery, viability, and batch variance. A configuration that cannot be built or characterized is excluded transparently; this stage does not infer physiological sufficiency.

---

### 1.3 Uricase Survival in Beer Fermentation

**Status**: Proposed | **Cost**: $200–400 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [saccharomyces-cerevisiae](./saccharomyces-cerevisiae.md)

**What it tests:** Whether a yeast configuration advanced by §1.33 retains active enzyme through the proposed fermentation process, if that process remains in scope.


**Protocol:**
- Brew a test batch with the selected yeast configuration and matched inactive-UOX control.
- At each stage—active fermentation (day 3), end of primary (day 7), after conditioning (day 14), after bottling (day 21)—draw samples
- Run uricase activity assay (spectrophotometric at 293 nm, measuring uric acid consumption)
- Control: purified uricase added to finished beer at same stages (distinguishes production from survival)

**Estimated cost:** $200–400 (controlled fermentation supplies + urate/product assay reagents)

**Estimated timeline:** 3–4 weeks

**Dependencies:** Run only after §1.33 and §1.2, and only if beer is still an intended delivery format.

**Success criteria:** Estimate process and assay variance, then prespecify the minimum retained-active-UOX margin needed for the intended format. A result below that margin rejects or redirects the beer process; it does not reject UOX or choose a different topology.

---

### 1.4 Uricase Stability After Drying

**Status**: Proposed | **Cost**: $300–800 | **Weeks**: 1–2 | **Phase**: 1

**Affected wiki**: [engineered-yeast-uricase-proposal](./engineered-yeast-uricase-proposal.md), [gi-survival-prediction](./gi-survival-prediction.md)

**What it tests:** Which drying process, if any, preserves retained active UOX in a §1.33-advanced configuration well enough for a prespecified research format.


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

**Dependencies:** Run after §1.33 and the relevant host-transfer confirmation, and only if a dry product remains in scope.

**Success criteria:** Estimate process and assay variance, then prespecify the retained-active-UOX and formulation margins before comparing drying methods. This experiment selects a process for the chosen configuration; it does not establish physiological sufficiency or choose UOX topology.

---

### 1.5 Koji Uricase Expression and Activity

**Status**: Proposed | **Cost**: $1,500–2,500 | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [koji-construct-design](./koji-construct-design.md), [uricase](./uricase.md)

**What it tests:** Whether a matched set of candidate UOX configurations can be built and characterized in *A. oryzae* well enough to enter §1.33. This stage supplies test material; it does not select a physiological winner.


**Protocol:**
- Build the prespecified candidate configurations in the same *A. oryzae* background with matched active-UOX, inactive-UOX, and host-only controls.
- Freeze the payload sequence and all construct features except the localization variable for any within-host topology comparison. Record unavoidable construct differences.
- Grow on steamed rice (traditional koji conditions: 30°C, 48–72h)
- Harvest koji and quantify UOX localization, total and active UOX, and active yield per gram of final product.
- Verify baseline product formation, H₂O₂, dissolved oxygen, viability, localization, sequence identity, and batch variance under common characterization conditions before supplying qualified material to §1.33.

**Estimated cost:** $1,500–2,500 (gene synthesis, transformation, reagents)

**Estimated timeline:** 4–6 weeks

**Dependencies:** A prespecified payload and matched construct plan. §1.1 may nominate the payload or run in parallel if the baseline comparator is frozen in advance.

**Success criteria:** Supply sequence-verified configurations with interpretable localization, active-UOX recovery, viability, and batch variance. Failure to build one arm narrows the §1.33 comparison but does not establish a host-wide failure.

---

### 1.6 Koji Enzyme Stability at Digestive pH and Temperature

**Status**: Proposed | **Cost**: $300–600 | **Weeks**: 1–2 | **Phase**: 1

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [gi-survival-prediction](./gi-survival-prediction.md), [digestive-enzymes](./digestive-enzymes.md)

**What it tests:** How much active UOX and product-forming capacity a §1.33-advanced koji configuration retains across the complete gastric-to-intestinal challenge.


**Protocol:**
- Challenge the selected whole-product configuration and matched inactive-UOX matrix through the prespecified gastric and intestinal sequence.
- Sample before processing and after each stage for active UOX, urate-to-product conversion under the §1.33 conditions, release/localization, aggregation, H₂O₂, and viability where a living configuration is used.
- Include a free-enzyme comparator only as an assay control; do not use it to choose the reaction-site topology.

**Estimated cost:** $300–600 (digestive enzyme prep, assay reagents)

**Estimated timeline:** 1–2 weeks

**Dependencies:** Requires §1.5 to build the configuration, followed by §1.33 to advance that exact configuration. Matrix comparisons in §1.15 may run from the same qualified batch.

**Success criteria:** Estimate assay and process variance, then prespecify the minimum retained-active-UOX and product-formation margins for the intended configuration. No fixed survival percentage establishes physiological sufficiency.

---

### 1.7 NLRP3 Inflammasome Pathway Validation (THP-1 MSU Macrophage Assay)

**Status**: Proposed | **Cost**: $5,000–8,000 | **Weeks**: 8–10 | **Phase**: 1

**Affected wiki**: [nlrp3-exploit-map](./nlrp3-exploit-map.md), [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md), [egcg](./egcg.md)

**What it tests:** Do proposed compounds in the [[supplements-stack]] actually inhibit NLRP3 at stated chokepoints?


**Protocol:**
- Use macrophage cell line (**THP-1 differentiated with PMA** preferred over primary mouse macrophages — the species-gap caveat in [supplements-stack.md](./supplements-stack.md) makes human cells mandatory for translation)
- Prime with LPS (Signal 1: NF-κB priming)
- Expose to MSU crystals (NLRP3 trigger)
- Treat with individual compounds and read out in parallel
- Measure endpoints: IL-1β secretion (ELISA), caspase-1 activity, ASC specks (fluorescence), **IκBα retention (Western — mechanistic readout for proteasome-pathway inhibitors)**
- Compare dose-response and mechanistic target (which chokepoint affected)

**Priority compounds (ordered by information value of the specific mechanistic claim being tested):**

- **EGCG.** Test IL-1β together with IκBα retention and a TNFSF14-induced IL-6 readout. Compare defined EGCG materials only when their composition and free exposure can be matched; formulation availability does not select a product or establish translation.
- **Oridonin** — direct NLRP3 NACHT Cys279 covalent binder; 5.18 μM human THP-1 IC50 per ChEMBL. Tests whether the curated human IC50 replicates in our hands.
- **BHB** — tests direct NLRP3 K⁺-efflux-block mechanism; straightforward positive-control-class compound.
- **Sulforaphane** — Nrf2 activator; tests whether the Nrf2/NF-κB crosstalk mechanism translates to MSU-triggered cells at achievable sub-μM doses.
- **Quercetin** — now primarily a CP6a (5-LOX) compound; tests whether the weaker NF-κB/NLRP3 claim holds at μM concentrations.
- **Carnosine + Lactoferrin** — unique mechanism classes (dual UA/NLRP3 and CP5 GSDMD-axis respectively); tests whether the rat/murine evidence translates to human THP-1.

**Estimated cost:** $5,000–8,000 (cell culture, cytokines, assay kits, Western reagents, compound panel)

**Estimated timeline:** 8–10 weeks (larger compound panel than original scope)

**Dependencies:** None

**Decision criteria:** Prespecify assay-validity, concentration-response, cytotoxicity, and mechanism-proximal margins after a pilot. An IL-1β change alone does not validate a named chokepoint; advancement requires concordant target-proximal readouts and independent replication.

---

### 1.8 EGCG Dose-Escalation on MSU-Stimulated THP-1: TNFSF14-Induced IL-6 Readout (CP1a)

**Status**: Proposed | **Cost**: $500–800 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [egcg](./egcg.md), [tnfsf14-gout-target](./tnfsf14-gout-target.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md)

**What it tests:** Does EGCG suppress TNFSF14-induced IL-6 in a gout-relevant cell model at sub-μM concentrations — the specific CP1a readout that would validate EGCG's multi-chokepoint coverage story?


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

<a id="19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate"></a>
### 1.9 Ward 1995 Dual-Cassette Feasibility Test (Koji Multi-Payload Strain Gate)

**Status**: Proposed | **Cost**: $5,265–8,065 (full path) | **Weeks**: 8–12 | **Phase**: 1

**Affected wiki**: [koji-endgame-strain](./koji-endgame-strain.md), [lactoferrin](./lactoferrin.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [uricase-variant-selection](./uricase-variant-selection.md)

**What it tests:** After §1.5 builds a koji UOX configuration and §1.33 advances that exact configuration under the physiological reaction-site screen, can the Ward 1995 *A. awamori* glucoamylase-KEX2 lactoferrin architecture (>2 g/L submerged, PMID 9634791) and the UOX configuration coexist in the same *A. oryzae* genetic background on solid-state rice koji — without silencing either cassette or collapsing the native kojic-acid / ergothioneine metabolite program? This remains the decisive one-strain-versus-two-strain feasibility gate for the koji multi-payload hypothesis, but it is downstream of the core UOX system gate.

**Current sequence:** §1.5 first supplies characterized koji UOX configurations to §1.33. §1.9 then executes as three stop/go stages: **A, Lf-only; B, a §1.33-advanced UOX-only configuration reproduced in the §1.9 solid-state context; C, dual-cassette.** Stage A may proceed in parallel with the UOX build and physiological screen; Stage C begins only after both single-cassette arms pass.

**Secondary role — chaperone-framework calibration set:** the lactoferrin-alone arm of this experiment is the transferrin-lobe data point in the calibration-set candidate documented in [`chaperone-orthogonal-stacking.md` §3.5.4](./chaperone-orthogonal-stacking.md) (paired with §1.25's DAF SCR1-4 CCP/SCR data point). Pre-registered framework prediction: **≥500 mg/L** lactoferrin-alone if the framework's α coefficients transfer to koji; **<40 mg/L** if PDI-saturation dominates. This calibration role does NOT change §1.9's primary objective or design — it just means the lactoferrin-alone titer should be reported with enough precision to compare against §1.25's DAF SCR1-4 titer under harmonized conditions (same host = NSlD-ΔP10, same format = solid-state shio-koji, same titer units = mg/L mature protein by ELISA).

**Protocol:**
- **Construct design.**
  - Cassette A (lactoferrin): `[PamyB — glucoamylase — KEX2site (Lys-Arg) — hLf codon-optimized for *A. oryzae* — TamyB]`. Matches Ward 1995 architecture. Selection marker: pyrG complementation.
  - Cassette B (UOX): use the exact sequence, localization, promoter, and support modules qualified in §1.5 and advanced by §1.33. *A. flavus* and *C. utilis* source families remain unranked until matched configuration data exist.
- **Host strain.** Compare exact qualified *A. oryzae* host configurations when protease background or integration architecture could change either payload. Adjacent antibody or enzyme-expression precedents justify candidates, not a preselected host.
- **Stage A — lactoferrin-only.** PEG/CaCl₂ protoplast transformation with Cassette A → select on pyrG-minus → confirm expression, fold, iron binding, and titer. This stage is independently informative and may run while §1.33 is underway.
- **Stage B — advanced UOX-only.** Reproduce the exact koji configuration advanced by §1.33 in the §1.9 solid-state context plus submerged control. A saturating-substrate specific-activity number is an expression benchmark, not a physiological-system pass.
- **Stage C — dual-cassette.** Only after Stages A and B pass, transform the validated Lf clone with the selected UOX cassette → select on niaD/amdS → compare both outputs directly with their matched single-cassette baselines.
- **Fermentation.** Solid-state rice koji, 48–60 h at 30°C, 35% moisture. Parallel submerged-culture control (100 mL shake flask, 28°C) to isolate solid-state variable. **Add Lf-alone single-cassette arm** (no uricase cassette, otherwise identical) to resolve the capacity-vs-titer benchmark ambiguity flagged 2026-05-06 — see "Capacity-vs-titer side-product readout" below.
- **Readouts.**
  - UOX system performance: urate plus oxidative product at the §1.33 human-baseline and sensitivity conditions, with matched inactive-UOX controls; retain the saturating-substrate spectrophotometric UA-disappearance assay only as construct characterization (per [engineered-koji-protocol.md](./engineered-koji-protocol.md) §05).
  - UOX safety/localization: extracellular H₂O₂, dissolved oxygen, biomass viability, and supernatant/cell-associated UOX localization, using the same decision definitions as §1.33.
  - Lactoferrin titer: anti-hLf ELISA + Western blot.
  - Iron-binding capacity of Lf: UV-Vis at 465 nm (apo-vs-holo); optional CD spectroscopy for fold confirmation.
  - Native metabolite profile: kojic acid titer (HPLC) + ergothioneine titer (LC-MS) — is WT baseline preserved within 30%?
  - qPCR for both cassette copy numbers (stability check).
  - SDS-PAGE to detect any incompletely-processed glucoamylase-hLf fusion (KEX-2 saturation signal).

**Capacity-vs-titer side-product readout:** The Lf-alone single-cassette arm above resolves a load-bearing benchmark ambiguity in the OE wiki: the [chaperone-orthogonal stacking framework](./chaperone-orthogonal-stacking.md) used the Huynh 2020 antibody result as a comparator (39.7 mg/L adalimumab in NSlD-ΔP10, 16 disulfides), while [koji-endgame-strain.md](./koji-endgame-strain.md) §3.1 cites Ward 1995 (>2 g/L Lf in *A. awamori*) as the protein-specific lactoferrin precedent. Bulk disulfide equality cannot decide which result is informative for Lf in the current host/format. The §1.9A Lf-alone arm directly measures that missing point in NSlD-ΔP10 solid-state koji, neither of which matches Ward 1995 (*A. awamori*, submerged). Three actionable readouts:

| Lf-alone titer | Implication for chaperone framework | Implication for multi-payload strain |
|---|---|---|
| ≥500 mg/L | Supports the interpretation that Huynh's low titer is antibody-architecture-specific in this host/format; does not by itself calibrate dual-cassette synergy | Authorizes Stage C if Lf function also passes; additional PDI-loaded payloads still need their own coexistence data |
| 100–500 mg/L | Genuine intermediate regime; the framework remains weakly calibrated for single-chain payloads | Stage A may require optimization before Stage C; third PDI-loaded cassettes remain conservatively routed |
| <100 mg/L | Supports a host/format constraint under these conditions; does not prove an architecture-independent ceiling | Dual-PDI-cassette risk rises and two-strain co-fermentation becomes more attractive |

This is a free byproduct of the §1.9 readout — no additional fermentation cost, only the Lf-alone strain construction (which is already a prerequisite for the dual-cassette construction sequence per "Transformation" above: Cassette A first → confirm hLf expression → transform Cassette B). The Lf-alone titer was previously reported only as part of the construct-validation step; this addendum elevates it to a load-bearing platform readout.

**Plasmidsaurus QC pipeline:** apply the canonical [§05 Plasmidsaurus QC pipeline](./engineered-koji-protocol.md#step-5-strain-qc-infrastructure-plasmidsaurus-pipeline-for-plasmid--transformant--strain-verification) across the §1.9 build:
- **Pre-transformation:** Whole Plasmid Sequencing of both cassette plasmids before any transformation work ($15 × 2 = **$30**, 1 day). Catches construct errors before the $500–1,000 cloning/transformation reagent spend.
- **Post-transformation clone screening (Cassette A round):** Genotyping Analysis on 6–10 hLf-alone transformants to pick clean on-target integrants before committing to Western screening ($30 × 8 = **$240**, 1–2 days).
- **Post-transformation clone screening (Cassette B round):** Genotyping Analysis on 6–10 dual-cassette transformants ($30 × 8 = **$240**, 1–2 days). Same logic — screen on integration cleanliness before fermentation panel.
- **Junction PCR sequencing (both rounds):** Amplicon Sequencing on 2–4 junction PCRs per integration ($15 × 6 = **$90**, next-day).
- **Final platform-strain release:** Whole Genome Sequencing on the validated dual-cassette strain (Eukaryotic tier for *A. oryzae*, $250 + $15 DNA extraction = **$265**, 3–6 days). This is the "publish-grade" sequence for the open-source-strain-library release.

**Plasmidsaurus QC pipeline subtotal: ~$865, ~15% of the §1.9 envelope.** Replaces piecemeal Sanger + multiple junction PCRs + qPCR copy-number — the qPCR copy-number assay can be retained as a sanity check or replaced entirely by Whole Genome Sequencing readout from the final-strain step.

**Host-stress transcriptome readout via Plasmidsaurus RNA-Seq:** the planned readout panel covers known native metabolites (kojic acid, ergothioneine) via HPLC/LC-MS but does not assay genome-wide host stress — UPR activation, secretory-pathway saturation, broader biosynthesis-transcript collapse — which is the empirical signal most directly relevant to chaperone-orthogonal-stacking α-coefficient calibration ([`chaperone-orthogonal-stacking.md` §3.5.4](./chaperone-orthogonal-stacking.md), [`combined-cp0-systems-model-computational.md`](./combined-cp0-systems-model-computational.md) comp-029). Plasmidsaurus launched an Illumina-based RNA-Seq service in 2026 priced at $50/sample academic / $80/sample industry, ~3-day turnaround, 10M deduplicated 3' end counting reads from 300 ng purified RNA, with interactive volcano + functional-enrichment outputs. Proposed addendum panel: 4 conditions (WT NSlD-ΔP10, lactoferrin-alone arm, uricase-alone, dual-cassette) × 3 biological replicates = 12 samples = ~$600 academic. Add ~$200 for RNA-extraction reagents (TRIzol or RNeasy) — koji is fungal and Plasmidsaurus does not accept fungal cells directly, only purified RNA at ≥10 ng/μL — total adder ~$800, ~15% of the §1.9 envelope.

| α-signature in transcriptome | Implication for chaperone framework |
|---|---|
| UPR target genes (hac1, bipA, pdiA, ero1) elevated in dual-cassette by <2× vs Lf-alone | α ≥ 0.8 (near-additive); framework predicts dual-PDI stacking scales well |
| UPR targets elevated 2–5× | α ≈ 0.4–0.6 (intermediate); third PDI-loaded cassette (DAF SCR1-4) needs conservative framing |
| UPR targets elevated >5× OR ergothioneine biosynthesis transcripts (egt1, egt2) collapsed >50% | α < 0.4 (saturating); strain compromised, two-strain co-fermentation fallback (§4.1 koji-endgame-strain.md) becomes more attractive regardless of titer outcome |

**Technology caveat:** Plasmidsaurus RNA-Seq is short-read Illumina 3' end counting — good for differential expression and transcript abundance, **not capable of** cryptic-splicing detection, transcript-isoform analysis, or read-through detection. If a load-bearing splicing question emerges post-§1.9 (e.g., heterologous ORF showing antibody-positive Western but no activity), use a validated full-transcript method. The construct-identity workflow in [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) §05 is a separate requirement; its service provider is replaceable.

**Estimated cost:** $5,265–8,065 — gene synthesis for two codon-optimized cassettes (~$600–1,000), cloning and transformation reagents ($500–1,000), fermentation consumables ($200–400), ELISA + Western antibodies ($800–1,200), metabolite assay reagents ($500–800), Plasmidsaurus QC pipeline (plasmid + amplicon + genotyping + whole-genome, ~$865), Plasmidsaurus RNA-Seq 12-sample panel + extraction reagents ($800), CRO or academic lab time if outsourced ($1,000–2,000 per batch).

**Estimated timeline:** 8–12 weeks — 2–3 weeks gene synthesis + construct assembly, 2–3 weeks sequential transformation + clonal screening, 1–2 weeks parallel fermentation (solid-state + submerged), 2–3 weeks full assay suite + write-up.

**Dependencies:** *A. oryzae* genetic-engineering lab access for all stages; §1.5 construct supply followed by a configuration-specific §1.33 pass before Stage B is frozen and before Stage C begins. Candidate access pathways remain: (a) a Role 2 collaborator; (b) a commercial CRO specializing in filamentous-fungus engineering; or (c) a community biolab with protoplast-transformation capability. **Global parallel options are mapped in [`ward-1995-lab-access.md`](../operations/ward-1995-lab-access.md).** Lab-access outreach may continue in parallel; it does not change the scientific stop/go order.

**Success criteria:**
- **Entry into Stage C:** Stage A lactoferrin meets its fold/function criterion, and Stage B reproduces the §1.33 physiological-system pass in solid-state koji. A saturating-substrate expression result cannot by itself authorize the dual build or support a serum-urate inference.
- **UOX comparison rule:** use the UOX-only and dual-cassette pilot variance to prespecify a noninferiority margin for physiological-condition product formation together with peroxide and viability limits; do not use a fixed retained-activity percentage as the product-selection rule.
- **Accept** (go to full multi-payload strain development per [koji-endgame-strain.md](./koji-endgame-strain.md) §7): lactoferrin titer ≥500 mg/L koji pore-fluid equivalent; UOX clears the prespecified product-formation, peroxide, and viability criteria versus the matched UOX-only strain; native kojic acid + ergothioneine titers remain within 30% of WT.
- **Iterate** (adjust architecture, re-test): lactoferrin 100–500 mg/L, UOX misses its prespecified noninferiority margin, or a peroxide/viability penalty is unique to the dual strain. Try alternative integration sites, promoter pairing, iron supplementation, or the next-ranked §1.33-compatible UOX implementation.
- **Reject** (fall back to two-strain co-ferment per [koji-endgame-strain.md](./koji-endgame-strain.md) §4.1): lactoferrin <100 mg/L after two rounds of optimization, OR native metabolite program collapse (kojic acid down >50% vs. WT). The two-strain fallback preserves the coverage matrix at the cost of single-strain elegance.
- **Post-accept safety gate:** a Stage C winner does not proceed to animal efficacy until [§1.36](#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) clears the joint urate-antioxidant-loss/peroxide risk.

**Computational prior (comp-010, 2026-05-05; disulfide count corrected 2026-07-13) — cassette compatibility:** Seven sequence-level analyses (codon usage, KEX2 geometry, secretion targeting, disulfide load, N-glycosylation, combined burden, Huynh 2020 comparison) found **no blocking cassette-design issues** for the proposed asymmetric architecture. Overall cassette-design risk: **LOW**. Key design notes: (1) Lactoferrin has one moderate-risk internal KEX2 site at mature position 579 (P1'=K) — monitor by SDS-PAGE for a ~67 kDa truncated band; if seen, mutate K597→Q in the codon-optimized gene. (2) Uricase C-terminal SKL resembles a PTS1 peroxisomal signal — verify secretion by anti-uricase ELISA on culture supernatant vs. cell lysate; if misrouted, append 3×Ala C-terminal tag. Combined ER disulfide count = 1.00× the Huynh 2020 adalimumab reference (16 disulfides, all on Lf; uricase contributes zero), using the primary-source count in Notari 2023 (PMC10465537). This count does not prove equivalent folding burden because Lf and IgG have different architectures. The titer gap versus Huynh 2020 is likewise not a direct capacity comparison; Ward 1995 >2 g/L is the protein-specific precedent. Full analysis: [`cassette-compatibility-computational.md`](./cassette-compatibility-computational.md). Evidence level: Mechanistic Extrapolation.

**Computational prior (comp-022 v2, 2026-05-14) — uricase cassette ranking:** ClockBase-style exhaustive enumeration of 43,200 uricase cassette candidates (6 promoters × 12 signal peptides × 10 codon variants × 60 secretion scaffolds). v2 retrofit with ESM2 pseudo-pLDDT (Tier 3 fold-quality proxy) + ViennaRNA 2.7.2 MFE (replacing v1's weak GC-clamp proxy; Spearman rho = 0.241). **71 cassettes pass N-of-5 ≥ 4; 4 cassettes pass N-of-5 = 5.** The v1 top cluster (PamyB + amyB SP + 5'-softened codon + direct-secretion + PTS1-blocking C-terminal tag + N191Q glycosylation-sequon ablation) survives v2 at 100%. Three gene-synthesis-time refinements remain useful within the direct-secretion candidate: (1) 5'-softened codon optimization, (2) PTS1-blocking C-terminal tag, and (3) N191Q glycosylation-sequon ablation. Comp-022 ranked glucoamylase-KEX2 below direct secretion on its modeled sequence features; it did not test physiological product formation and therefore cannot exclude fusion or retention topologies from §1.33. Full analysis: [`uricase-cassette-ranking-computational.md`](./uricase-cassette-ranking-computational.md) and [`etc/experiments/comp-022-clockbase-uricase-cassette-ranking/`](./etc/experiments/comp-022-clockbase-uricase-cassette-ranking/). Evidence level: Mechanistic Extrapolation (in silico only).

**Computational prior (comp-023, 2026-05-14) — cordycepin cassette metabolic burden:** FBA on the Vongsangnak 2008 iWV1314 GEM with dual + cns1-cns2 + carnS + panD scenarios. Verdict: **GREEN** at the Jeennor 2023 empirical titer (564 mg/L/day). Growth penalty +0.02% vs WT; kojic acid + EGT yield headroom 100% of dual-cassette baseline. Cordycepin demand at 564 mg/L/d consumes ~0.02% of cellular carbon flux. FBA breakpoint ~1,000× the empirical titer. Carnosine + panD third-cassette alternatives also GREEN. Three open follow-up gates: ADA competition (comp-025), dynamic FBA validation (comp-023 v2), multi-cassette induction interference (comp-026). Full analysis: [`wiki/cordycepin-cassette-burden-computational.md`](./cordycepin-cassette-burden-computational.md). Evidence level: Mechanistic Extrapolation (in silico only). (source: cordycepin-cassette-burden-computational.md)

**Cross-references:** [koji-endgame-strain.md](./koji-endgame-strain.md) §3 (full protocol rationale + adjacent literature: Li 2024 PMID 39830075 multi-copy in *A. oryzae*, Wang 2023 PMID 37807677 multi-locus in *A. niger*), [engineered-koji-protocol.md](./engineered-koji-protocol.md) §16 (starting single-cassette lactoferrin module that this experiment ladders on top of), [lactoferrin.md](./lactoferrin.md) §7 (Open Enzyme feasibility bet), [synthesis/](../synthesis/README.md) 2026-04-24 Connection 1, [cassette-compatibility-computational.md](./cassette-compatibility-computational.md) (comp-010 cassette design analysis).

---

### 1.10 Heterologous Uricase + Lactoferrin Stability in Shio-Koji Salt-Protease Ferment

**Status**: Proposed | **Cost**: $2,100–4,100 core; microbial QC TBD | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [synthesis/](../synthesis/README.md), [lactoferrin](./lactoferrin.md)

**What it tests:** Does the 7–14 day shio-koji salt-protease ferment degrade engineered uricase and/or lactoferrin produced by *A. oryzae*? **Two proteins are tested in the same run** because their sequence and structural priors differ. For UOX, comp-001 maps P1/P1' sites and pLDDT but does not measure solvent exposure or protease survival; for lactoferrin, the model likewise remains a proxy. Both arms are empirical feasibility tests, and retained activity—not an intact-looking band or model score—is decisive.

**Gate:** tests whether both payload classes retain activity in the intended shio-koji format.

**Protocol:**
- **Constructs:** Use the exact §1.5 koji configuration advanced by §1.33, plus a co-expressing or separate lactoferrin strain if available. A spiked-material pilot may use characterized research-grade proteins to estimate process and assay variance, but those concentrations are controls rather than physiological or dose assumptions.
- **Ferment matrix:** Prepare shio-koji per [koji-home-fermentation.md](./koji-home-fermentation.md) standard protocol (15–20% NaCl, room temp 22–25°C). Run in parallel with two control matrices: (a) freshly harvested koji (no salt ferment), (b) amazake-style brief warm hold (55–60°C × 6h followed by RT storage) — heat hold partially inactivates proteases.
- **Time-course sampling:** Aliquot at days 0, 3, 7, 10, 14. Freeze at −80 °C immediately after collection.
- **Readouts — uricase:**
  - Uricase activity: spectrophotometric UA-disappearance assay at 293 nm per [engineered-koji-protocol.md](./engineered-koji-protocol.md) §05 (quantitative).
  - SDS-PAGE + anti-uricase Western blot: detects intact monomer (~34 kDa) vs. degradation products. Distinguishes "lost activity due to denaturation" from "lost activity due to proteolytic cleavage."
  - Optional CD spectroscopy on extracted uricase: confirms tetramer fold preservation if activity drops without obvious cleavage on Western.
- **Readouts — lactoferrin:**
  - Lactoferrin protein integrity: SDS-PAGE + anti-lactoferrin Western blot, detecting intact 80 kDa band vs. characteristic bilobal cleavage products (~40 kDa N-lobe + ~40 kDa C-lobe). Lactoferrin's linker region between the two lobes is the most proteolytically accessible site.
  - Lactoferrin iron-binding capacity (optional functional assay): iron-binding ELISA or colorimetric ferrozine assay at day 0 and day 14; iron-binding is the functional proxy for intact bilobal structure.
  - Note: unlike uricase, lactoferrin has no comp-001 computational prior. The Western blot result is the primary feasibility determination.
- **Salt-concentration sub-experiment:** Single-timepoint (day 7) panel at 5%, 10%, 15%, 20% NaCl. Run both proteins in the same panel — determines whether uricase and lactoferrin have different salt-threshold protection profiles, which would inform whether a low-salt variant could preserve one but not the other.
- **Linker-variant arm — comp-034 multi-variant plate:** four-lane core gel comparing WT lactoferrin against three redesigned inter-lobe linker variants from [comp-034](./lactoferrin-linker-redesign-computational.md), ordered by the current PyRosetta ΔΔG and structure-gated-cleavage result:

  **★ Arm ordering inverted 2026-05-30 (PyRosetta ΔΔG + structure-gated cleavage).** The proline-rigidification arms (`EEEEPAARRAR`, `SEEEPAARRAR`), previously framed as "conservative/safe", are in fact destabilizing (ΔΔG +20/+21 REU) and deliver little net protease benefit (−17%/−24%), because proline breaks the protective inter-lobe helix. The MPNN-native `NEEEQQQEEEQ` is stability-neutral (ΔΔG +0.23 REU), keeps the helix, and cuts structure-gated cleavage −66% — it should be the **primary** arm, not the "aggressive" one. Full analysis: [comp-034 rosetta_concordance/README.md](./etc/experiments/comp-034-lactoferrin-linker-redesign/rosetta_concordance/README.md). (Mechanistic Extrapolation; source: lactoferrin-linker-redesign-computational.md)

  - Lane 1: WT lactoferrin (`SEEEVAARRAR` linker, residues 353–363 / mature 334–344) — baseline / positive control
  - Lane 2: **Primary candidate `NEEEQQQEEEQ`** (multi-substitution, 5-of-5 metrics, **10.4× cleavage reduction vs WT** — 0.039 vs 0.407; ΔΔG +0.23 REU, structure-gated cleavage −66%, helix preserved at 0.818). **Primary arm** — wins on both fold-stability and protease-resistance axes. It outperforms the proline arms on the current physics analysis.
  - Lane 3: **Sibling backup `NEEEQEEQDQQ`** (MPNN-native, 5-of-5 metrics, ΔΔG +2.39 REU, helix-preserved)
  - Lane 4: **Proline single-mutant `SEEEPAARRAR`** (V357P, 91% WT identity, ΔΔG +20.11 REU, structure-gated cleavage −17%) — **diagnostic comparison**

  The proline double-mutant `EEEEPAARRAR` (S353E+V357P, 82% WT identity, ΔΔG +21.26 REU, structure-gated cleavage −9%) is not part of the core plate. Add it only as a separately costed fifth lane if distinguishing the two destabilizing proline designs becomes decision-relevant.

  Readout: same SDS-PAGE + anti-Lf Western + iron-binding ELISA as the WT lane, run at day 0 / day 7 / day 14. Outcome: maps comp-034's in silico predictions to wet-lab protease resistance + bilobal-cleavage product pattern. Marginal cost +$1.5–3K (gene synthesis for 3 variants at typical custom-synthesis pricing; reagent costs amortized into the existing §1.10 panel). **comp-034 substitute-sampler caveat RESOLVED 2026-05-19:** genuine ProteinMPNN rerun validated that the substitute sampler's 15 GREEN candidates are NOT artifacts (mean MPNN log-likelihood 2.74 GREEN vs 3.74 FAIL — clean separation). Substitute sampler's proline-bias + WT-mix-in heuristic was a coarse but functional proxy for what ProteinMPNN encodes structurally. Genuine MPNN additionally found 3 STRICT (5-of-5) candidates the substitute sampler missed: NEEEQQQEEEQ (the primary candidate above), NEEEEQQEQEQ, NEEEEEQEQEQ — all 10.4× cleavage reduction. Full rerun report: [`logs/proteinmpnn-comp-034-rerun-2026-05-19.md`](../logs/proteinmpnn-comp-034-rerun-2026-05-19.md). See also [`etc/bio-ai-tools.md` §"Protease-vulnerability-to-redesign workflow"](./etc/bio-ai-tools.md) for the generalizable workflow pattern.

**Microbial-community QC (optional until the exact assay is qualified):** bacterial 16S profiling cannot measure *A. oryzae* abundance or establish fungal dominance. To distinguish bacterial contamination from fungal-biomass change, use paired bacterial 16S plus fungal ITS profiling, or validated taxon-specific qPCR/ddPCR with spike-in and extraction controls. Sample the engineered and WT matrices at day 0 / day 7 / day 14. Treat relative-abundance profiles as compositional rather than as biomass measurements. Freeze reportable limits and a decision rule only after the pilot establishes assay precision and background distributions; the former 5% and 10% relative-abundance cutoffs are not binding gates. A community shift can trigger targeted contaminant identification and reinterpretation of protein loss, but it cannot by itself assign protease causality.

**Estimated cost:** $2,100–4,100 core; microbial QC TBD — uricase activity assay reagents ($100–200), lactoferrin iron-binding assay reagents ($50–100), SDS-PAGE / Western antibodies for both proteins ($300–500), bovine lactoferrin standard ($50), shio-koji ingredients ($20–50), CD spectroscopy if outsourced ($100–200), and comp-034 linker-variant gene synthesis ($1,500–3,000 for 3 variants). Price paired-community or taxon-specific microbial QC only after the assay, sample matrix, controls, and provider are fixed.

**Estimated timeline:** 3–4 weeks — parallel with the active fermentation. Day-by-day sampling continues over the 14-day window; assay batches at days 0/3/7/10/14 are ~2 days each.

**Dependencies:** The UOX product-format decision follows §1.5 construct supply and §1.33 advancement of that exact koji configuration. A spiked-material pilot may run earlier to estimate assay and process variance, but it cannot promote a configuration or delivery format.

**Success criteria:**
- Estimate assay and process variance, then prespecify the retained-active-UOX and integrity margins for the selected configuration before assigning an accept, iterate, or reject result to shio-koji processing.
- An intact band without retained activity does not pass; retained activity without §1.33-condition product formation does not establish physiological sufficiency.
- Interpret lactoferrin integrity and function separately. Neither payload's result is automatically transferable to another protein or peptide.

**Computational prior (comp-001, 2026-05-05) — uricase only:** comp-001 maps P1/P1' sequence-recognition positions for three *A. oryzae* proteases and reports AlphaFold per-residue pLDDT. It does not calculate solvent exposure or SASA and does not measure protease survival, retained activity, salt-conditioned behavior in the ferment, or fermentation performance. The UOX arm of §1.10 therefore remains an empirical feasibility gate; comp-001 supplies only a sequence/structure-confidence prior. Full analysis: [`wiki/uricase-protease-stability-computational.md`](./uricase-protease-stability-computational.md) and [`etc/experiments/comp-001-uricase-shio-koji-protease-stability/`](./etc/experiments/comp-001-uricase-shio-koji-protease-stability/).

**Computational prior (comp-005, 2026-05-05) — lactoferrin:** AlphaFold structural analysis + P1/P1' cleavage-site prediction for the same three koji proteases, with two verdicts: **HIGH (full sequence including signal peptide) / MODERATE (mature protein aa 20–710).** The HIGH score is driven entirely by the fully disordered signal peptide (aa 1–19, pLDDT 35–54) — all top-5 sites across all three proteases map to signal peptide residues. Mature-protein max risk is 0.188 (ALP, 3 exposed sites). If *A. oryzae* signal peptidase processes the heterologous signal sequence, operative risk is MODERATE. Signal peptide processing is common for secreted proteins in *A. oryzae* but not guaranteed for foreign sequences. The **lactoferrin arm of §1.10 remains a feasibility gate** — unlike the uricase arm, the MODERATE mature-protein verdict is insufficient to reframe this as a confirmation experiment. If wet-lab shows lactoferrin degradation while uricase survives, first diagnostics are: (1) Western blot for ~40 kDa bilobal cleavage products (inter-lobe linker); (2) N-terminal sequencing to determine signal peptide processing status. Full analysis: [`wiki/lactoferrin-protease-stability-computational.md`](./lactoferrin-protease-stability-computational.md) and [`etc/experiments/comp-005-lactoferrin-shio-koji-protease-stability/`](./etc/experiments/comp-005-lactoferrin-shio-koji-protease-stability/).

**Cross-references:** [synthesis/](../synthesis/README.md) 2026-04-27 Open Question #2 + Connection #2; [engineered-koji-protocol.md](./engineered-koji-protocol.md) §06 (process and transit comparison); [koji-home-fermentation.md](./koji-home-fermentation.md) (shio-koji standard protocol); [aspergillus-oryzae.md](./aspergillus-oryzae.md) (native protease characterization); [uricase-protease-stability-computational.md](./uricase-protease-stability-computational.md) (comp-001 structural prior); [computational-experiments.md](./computational-experiments.md).

---

### 1.11 Ergothioneine → ABCG2 Induction in Caco-2 (Native Koji Synergy Test)

**Status**: Proposed | **Cost**: $1,000–1,500 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [abcg2-modulators](./abcg2-modulators.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [gut-lumen-sink](./gut-lumen-sink.md)

**What it tests:** Does ergothioneine—reported as natively produced by *A. oryzae*—induce ABCG2 expression in human enterocyte-lineage cells at concentrations achievable from koji-derived dietary intake? **Tag: Mechanistic Extrapolation testing a two-step inference (ergothioneine → Nrf2 stabilization → ABCG2 induction).** Ergothioneine's "Nrf2 inducer" classification is weaker than canonical activators (sulforaphane, CDDO-Me); it is more accurately a ROS scavenger that may indirectly stabilize Nrf2. This experiment tests whether the koji track gets incidental ABCG2-induction synergy from a native metabolite or whether the connection is too distant to matter. **Verify before running:** the achievable koji titer remains unverified against primary literature.


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
- **Falsifies / scopes down:** No detectable ABCG2 induction at koji-achievable doses. Removes this synergy from the koji-track configuration; positive sulforaphane control remains the canonical ABCG2 inducer route.

**Cross-references:** [abcg2-modulators.md](./abcg2-modulators.md) §2 (Nrf2 transcriptional axis); [aspergillus-oryzae.md](./aspergillus-oryzae.md) (native ergothioneine claim — verify before spending).

---

<a id="112-local-h2o2-stress-in-caco-2-from-the-selected-uox-configuration"></a>
### 1.12 Local H₂O₂ Stress in Caco-2 from the Selected UOX Configuration

**Status**: Proposed | **Cost**: $800–1,200 | **Weeks**: 2–3 | **Phase**: 1

**Affected wiki**: [uricase](./uricase.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [gut-lumen-sink](./gut-lumen-sink.md), [engineered-koji-protocol](./engineered-koji-protocol.md)

**What it tests:** Whether an exact UOX configuration advanced by §1.33 produces epithelial H₂O₂ exposure and barrier effects under the substrate, oxygen, localization, and activity conditions measured in that screen. Sensitivity conditions must remain labeled as sensitivity conditions; they are not human-baseline premises. The catalase-neutralization assumption in [`uricase.md`](./uricase.md) and [`aspergillus-oryzae.md`](./aspergillus-oryzae.md) remains unquantified.


**Protocol:**
- **Cells:** Caco-2 transwell monolayer, 21-day differentiated.
- **Treatment arms:**
  - Matched vehicle, inactive-UOX, and matrix- or chassis-only controls under the §1.33 human-baseline substrate prior.
  - The §1.33-advanced active-UOX configuration at a series derived from its measured product formation and H₂O₂, rather than a fixed enzyme-activity range.
  - Matched catalase and candidate antioxidant-rescue arms.
  - Separately labeled sensitivity-substrate arms where needed to define the response surface.
- **Readouts:**
  - Apical H₂O₂ time-course (Amplex Red probe, fluorescent plate reader, every 5 min × 60 min).
  - TEER (trans-epithelial electrical resistance) — barrier-integrity readout, baseline + 1, 4, 24 h.
  - LDH release (apical and basolateral) — cytotoxicity proxy.
  - Tight-junction protein localization (ZO-1, occludin) by IF after 24 h.
- **Optional:** if the selected topology is implemented in koji, add a matched whole-product arm to test the complete matrix without assuming that host membership closes reaction-site peroxide handling.

**Estimated cost:** $800–1,200 — Caco-2 + transwell ($300), Amplex Red kit ($200), rasburicase (research grade, $100), catalase ($50), TEER electrodes (already standard), IF antibodies ($200), reagents ($150).

**Estimated timeline:** 2–3 weeks.

**Dependencies:** §1.33 must first advance an exact built UOX configuration and define the measured substrate, oxygen, product-formation, and peroxide conditions. This assay may inform §1.36 but does not replace that post-screen safety gate.

**Success criteria:**
- **No barrier compromise** across the prespecified active-UOX series: bounds the tested range only; it does not establish a dose or human safety.
- **Barrier compromise at any tested activity:** stop escalation and characterize whether UOX flux, H₂O₂, matrix components, or another factor drives the signal before redesigning the configuration.

**Cross-references:** [§1.33](#133-physiological-uox-topology--oxygen--peroxide-factorial); [§1.36](#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay); [uricase.md](./uricase.md) (catalase-neutralization assumption); [aspergillus-oryzae.md](./aspergillus-oryzae.md) (native catalase + ergothioneine).

---

### 1.13 Limonene → ABCG2 Induction in Caco-2 (Tier 3 Stack Synergy Test)

**Status**: Proposed | **Cost**: $800–1,200 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [supplements-stack](./supplements-stack.md), [abcg2-modulators](./abcg2-modulators.md), [cannabinoids-terpenes](./cannabinoids-terpenes.md)

**What it tests:** Does limonene induce ABCG2 expression in Caco-2 enterocytes at supplement-relevant doses? Limonene is Tier 3 in `supplements-stack.md` based on the Venkatesan 2025 MSU rat model (50 mg/kg ≈ 0.5 g/day BSA-scaled human dose, close to typical supplement range), citing Nrf2 activation as a key mechanism. `abcg2-modulators.md` independently identifies Nrf2 as an ABCG2 transcriptional inducer (sulforaphane precedent, EC50 = 580 nM). This experiment tests whether limonene's putative Nrf2 activation translates to ABCG2 induction — gating whether the supplements-stack entry should be augmented with a "gut-lumen sink synergy" claim.


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

**Cross-references:** [synthesis/](../synthesis/README.md) 2026-04-26 Connection #3; [supplements-stack.md](./supplements-stack.md) limonene entry; [abcg2-modulators.md](./abcg2-modulators.md) §2.

---

### 1.14 ABCG2 Response to DHT and TNF With Butyrate and Lactoferrin Rescue

**Status**: Proposed | **Cost**: $2,300–4,300 | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [abcg2-modulators](./abcg2-modulators.md), [androgen-urate-axis](./androgen-urate-axis.md), [gut-lumen-sink](./gut-lumen-sink.md), [supplements-stack](./supplements-stack.md), [lactoferrin](./lactoferrin.md), [koji-endgame-strain](./koji-endgame-strain.md), [purine-degrading-bacteria](./purine-degrading-bacteria.md)

**What it tests:** Four questions in one experiment. (1) What is the direction and magnitude of DHT's effect on ABCG2, and does DHT interact with TNFα rather than add a presumed second suppression axis? (2) Does butyrate increase ABCG2 surface expression or urate flux under TNFα and in Q141K cells? (3) Does lactoferrin alter epithelial signaling or urate flux in the presence of fixed exogenous TNFα? This arm does not test upstream TNFα production or reproduce luminal delivery from koji. (4) Do quercetin, EGCG, and curcumin alter ABCG2-mediated urate efflux at gut-lumen-relevant concentrations, and is any effect genotype-dependent?

**Design rationale:** the shared Caco-2 system can direction-find DHT, TNFα, butyrate, lactoferrin, and supplement effects on the same functional endpoint. Claims about lactoferrin lowering local TNFα production require a later immune–epithelial co-culture with a defined apical-delivery model.

**Protocol:**
- **Cells:** Caco-2 transwell (used in both Xie 2020 and Solbakk 2025 per `abcg2-modulators.md`), 21-day differentiated.
- **Treatment arms (3 × 3 + response arms):** the initial n=4 per arm consists of independent biological replicates distributed across at least two passages and supplies variance for a confirmatory power calculation. Advance/kill decisions require a confirmatory run powered to 80% at two-sided α=0.05 for a 20% urate-flux difference.
  - DHT: 0, 10, 100 nM
  - TNFα: 0, 5, 20 ng/mL
  - All 9 combinations (DHT × TNFα factorial)
  - **Butyrate interaction arm:** compare TNFα 20 ng/mL with DHT 0 and 100 nM, each ± butyrate 1 mM apical. Interpret DHT direction from the factorial rather than presuming the combined arm is maximally suppressed.
  - **Butyrate dose-response arm — direct Q141K attribution test (corrected 2026-07-13):** in WT and Q141K-transfected polarized intestinal cells, apply butyrate across 0.05, 0.2, 1, 2, and 5 mM with vehicle and a Basseville-class positive-control rescue compound. Basseville 2012 did not test butyrate directly. Measure total and apical-surface ABCG2 plus basolateral-to-apical urate flux. This experiment asks whether butyrate reproduces the pharmacological rescue phenotype; it does not assume that it will.
  - **Lactoferrin response arm:** compare TNFα 20 ng/mL with DHT 0 and 100 nM, each with vehicle, apical lactoferrin, or basolateral lactoferrin at the same verified concentration. With exogenous TNFα fixed, this tests compartment-dependent neutralization/signaling response, not reduced TNF production. Measure both free and total TNFα so ligand binding is not mislabeled as lower production.
  - **Supplement ABCG2 antagonism arms:** Using the basal (DHT 0, TNFα 0) monolayer, apply each of the three named stack supplements at supplement-relevant gut-lumen concentrations, apical side: quercetin 10 µM and 50 µM; EGCG 1 µM and 10 µM; curcumin 5 µM and 20 µM. Measure urate flux in all six conditions vs. DMSO vehicle. These concentrations reflect achievable post-oral-dose enterocyte exposure, not plasma concentrations (gut-lumen levels are 10–50× higher than plasma due to incomplete absorption). Note: the Yu 2024 EGCG in vivo data (PMID 38757391) shows net-favorable ABCG2/URAT1/GLUT9 effect in hyperuricemic mice, contradicting the in vitro inhibition story — include both 1 µM and 10 µM EGCG arms to see whether the inhibitory or the inductive effect dominates at supplement-achievable concentrations. **Q141K-variant arm:** if a Q141K-expressing Caco-2 line or patient-derived matched organoid is available, repeat the highest-effect supplement conditions (quercetin 50 µM + curcumin 20 µM) in both WT and Q141K backgrounds — this directly tests the stratification hypothesis that the contradiction is clinically significant for the highest-risk genotype but manageable for WT.
- **Time-course:** 48 h for the DHT × TNFα, butyrate, lactoferrin, quercetin, and curcumin arms; both 48 h and 72 h for EGCG so the stated delayed transcriptional mechanism is observable.
- **Readouts:** ABCG2 mRNA (qPCR), ABCG2 protein (Western, apical-membrane fraction), functional urate efflux (transwell, basolateral-to-apical urate flux — *primary readout because expression does not establish function*), a validated AR reporter or Caco-2 AR-responsive target plus PXR/FXR response markers, NF-κB activation (IκBα Western), and free plus total TNFα in lactoferrin arms. CYP3A4 alone is not an AR-specific manipulation control.

**Estimated cost:** $2,300–4,300 — the upper bound reserves the powered confirmation, 72-hour EGCG arm, compartment-matched lactoferrin arms, and free/total TNFα measurements. Re-estimate after the n=4 pilot variance is available.

**Computational prior (comp-004, 2026-05-05):** IC50 occupancy analysis generated strong inhibition predictions for quercetin and curcumin, but free segment-specific exposure and urate-substrate transfer remain unverified. The 72-hour EGCG arm is retained because its proposed transcriptional effect may not appear at 48 hours. Full analysis: [`wiki/supplement-abcg2-antagonism-computational.md`](./supplement-abcg2-antagonism-computational.md) and [`etc/experiments/comp-004-supplement-abcg2-antagonism/`](./etc/experiments/comp-004-supplement-abcg2-antagonism/).

**Computational prior (comp-038, 2026-05-20):** The assay-infrastructure question remains **YELLOW**. No ready-to-adopt Tier 1 or Tier 2 butyrate method has been established for current OE use. HPLC-UV is a Tier 3 bench method for culture-supernatant development, while electrochemical/ANN profiling is a separate stool-specific Tier 2 candidate. Neither transfers to this cellular exposure matrix without validation. If concentration verification becomes load-bearing in §1.14, use a matrix-qualified Tier 3 analytical method directly. Full analysis: [`tier-2-butyrate-assay-audit-computational.md`](./tier-2-butyrate-assay-audit-computational.md) and [`etc/experiments/comp-038-tier-2-butyrate-assay-audit/`](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/).

**Estimated timeline:** 4–6 weeks (unchanged — supplement arms run in the same batch).

**Dependencies:** Caco-2 access, research-grade lactoferrin, and a pilot-to-confirmatory power calculation. Testing luminal koji-derived lactoferrin as an upstream TNFα-production intervention is a separate immune–epithelial co-culture and delivery experiment.

**Success criteria:**
- **DHT direction:** on the powered confirmatory run, classify suppression or induction only when the adjusted urate-flux difference is at least 20% and its 95% confidence interval excludes zero. Classify functional equivalence only when the 90% confidence interval lies wholly within ±15%; otherwise the result is inconclusive. Report the DHT × TNFα interaction from the prespecified two-factor model.
- **Butyrate effect:** support requires at least 20% higher urate flux versus matched vehicle with a 95% confidence interval excluding zero; expression without flux is insufficient.
- **Lactoferrin effect:** the fixed-TNFα arm can support compartment-specific neutralization or signaling rescue only if urate flux improves by at least 20% with a 95% confidence interval excluding zero and NF-κB changes concordantly. It cannot establish reduced TNFα production or efficacy of luminal koji delivery.
- **Q141K and supplement effects:** genotype interaction and functional flux, not expression alone, determine whether either response is relevant to stratification.

**Cross-references:** [synthesis/](../synthesis/README.md) 2026-04-27 Connection #1 + Proposed Experiment #2; 2026-05-05 Connection #1 (lactoferrin substrate-supply synergy); [abcg2-modulators.md](./abcg2-modulators.md) §3 (TNFα suppression — Ferrer-Picón 2020 PMID 31211831); [androgen-urate-axis.md](./androgen-urate-axis.md) (hormone-sensitive urate handling); [lactoferrin.md](./lactoferrin.md) §4.1 (Habib 2023 PMID 37926296 — Lf → ↓TNFα in vivo) and §4.7 (substrate-supply synergy framing); [koji-endgame-strain.md](./koji-endgame-strain.md) §2.2.

---

### 1.15 Rice-Bran Substrate × Koji Uricase GI Survival

**Status**: Proposed | **Cost**: $800–1,200 | **Weeks**: 3 | **Phase**: 1

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [koji-construct-design](./koji-construct-design.md), [gi-survival-prediction](./gi-survival-prediction.md)

**What it tests:** Whether substrate composition changes retained active UOX and product formation for an exact §1.5 koji configuration advanced by §1.33 across the complete processing and digestive challenge. Native-enzyme yield does not establish the direction of this heterologous-UOX result.


**Protocol:**
- **Configuration:** Use the same §1.5-built, §1.33-advanced koji configuration in every arm, with matched inactive-UOX and host-only controls.
- **Substrate matrix:**
  - Plain white rice (baseline)
  - Rice bran alone
  - Rice bran + 10% soybean (full optimization per `digestive-enzyme-optimization.md`)
- **Fermentation:** 48 h at 30°C, 35% moisture.
- **Process:** Lyophilize, grind to powder.
- **GI simulation:** Resuspend in SGF (pH 2, pepsin, 2 h, 37°C) → SIF (pH 7, trypsin, 2 h, 37°C). Sample at 0, post-SGF, post-SIF.
- **Readouts:**
  - Active UOX, urate, product, H₂O₂, and localization at each stage under the §1.33 reaction-site conditions
  - HPLC quantification of kojic acid, ferulic acid, ergothioneine in each koji type (secondary — does substrate change native metabolite production?)
  - LC-MS for phytic acid + polyphenol residuals (does rice bran's phytic acid bind divalent cations and affect tetramer stability?)

**Estimated cost:** $800–1,200 — koji ingredients ($50), assay reagents ($300), HPLC time ($200), LC-MS time ($300), labor ($150).

**Estimated timeline:** 3 weeks.

**Dependencies:** §1.5 must first supply the koji configuration and §1.33 must then advance that exact configuration. This is a downstream matrix/process comparison, not a free pre-screen optimization.

**Success criteria:**
- Estimate assay and process variance in a pilot, then prespecify the minimum reproducible improvement and noninferiority margins for retained active UOX, product formation, and peroxide handling.
- If a matrix clears those margins, carry it forward for that selected configuration. If none does, retain the simplest compatible matrix or redirect the product format.
- This experiment does not select UOX topology, establish an oral dose, or predict serum urate.

**Cross-references:** [engineered-koji-protocol.md](./engineered-koji-protocol.md) §06 (process and transit comparison); [gi-survival-prediction.md](./gi-survival-prediction.md) (food-matrix gate).

---

<a id="116-candidate-uox-variants-in-koji-sequential-retained-activity-screen"></a>
### 1.16 Candidate UOX Variants in Koji: Sequential Retained-Activity Screen

**Status**: Proposed; decision thresholds require assay-precision pilot and independent review | **Cost**: TBD | **Weeks**: TBD | **Phase**: 1

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [uricase-variant-selection](./uricase-variant-selection.md), [protein-engineering-strategy](./protein-engineering-strategy.md), [gi-survival-prediction](./gi-survival-prediction.md)

**What it tests:** Within an exact §1.5-built koji configuration already advanced by §1.33, does any structurally verified UOX candidate retain more active enzyme than wild type after expression, processing, and the complete sequential challenge in the same *A. oryzae* background? No candidate has been validated in yeast or koji, and this experiment does not choose topology or chassis.

**Minimum design:**

- wild-type *A. flavus* UOX;
- each combination candidate that passes residue-numbering and biological-assembly review;
- single-change controls needed to attribute any combination effect;
- matched empty-host and assay controls;
- the same integration locus, promoter, process, matrix, and challenge sequence across constructs.

**Readouts:**

- construct identity and copy state;
- total, soluble, and active UOX before processing;
- oligomeric state and disulfide formation where relevant;
- retained active UOX after each processing, gastric, and intestinal stage;
- aggregation, release/localization, oxygen use, and H₂O₂;
- batch and assay variance.

**Dependencies:** §1.5 must first supply the host implementation and §1.33 must advance the exact baseline configuration. Freeze processing and matrix conditions before ranking variants.

**Decision rule:** Estimate assay precision in a pilot, then prespecify the minimum reproducible improvement and noninferiority margins for baseline activity, expression, product formation, peroxide, and viability. Promote the simplest candidate that clears those margins only within the selected topology and after confirmation under the §1.33 reaction-site conditions. A null result retains wild type; a deleterious combination returns to component-level testing. Neither result establishes a dose, serum effect, formulation, topology, or host winner.

**Cross-references:** [uricase-variant-selection.md](./uricase-variant-selection.md), [protein-engineering-strategy.md](./protein-engineering-strategy.md), [engineered-koji-protocol.md](./engineered-koji-protocol.md), and [validation §1.33](#133-physiological-uox-topology--oxygen--peroxide-factorial).

---

### 1.17 Quercetin × Ursolic Acid × Carnosine Interaction in MSU-Stimulated THP-1

**Status**: Proposed | **Cost**: $1,500–2,000 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md), [carnosine](./carnosine.md), [engineered-koji-protocol](./engineered-koji-protocol.md)

**What it tests:** Whether the exact three materials change IL-1β suppression individually or in combination under one defined macrophage assay. An interaction in this assay would not select a chassis, expression construct, formulation, or product.


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
- **Positive interaction under the prespecified model:** supports independent replication and exposure/safety work on the exact tested materials. It does not select a multi-payload strain or product architecture.
- **Two-material interaction only:** independently replicate the exact pair before any exposure or delivery work.
- **No interaction beyond the prespecified additive model:** retain any reproducible individual-material effects as separate hypotheses; do not infer a preferred compound from this assay alone.

**Cross-references:** [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) (Tier-1 candidates); [carnosine.md](./carnosine.md) (URAT1/GLUT9 angle).

---

### 1.18 Native Koji Enzyme SGF Survival — Free Extract vs. Whole Biomass (2-Arm)

**Status**: Proposed | **Cost**: $300–500 | **Weeks**: 2 | **Phase**: 1

**Affected wiki**: [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [gi-survival-prediction](./gi-survival-prediction.md), [digestive-enzyme-optimization](./digestive-enzyme-optimization.md)

**What it tests:** Whether intact wild-type koji biomass protects its **native** lipase, protease, and amylase activities through the digestive challenge better than a matched free extract. Because the payloads and localization biology differ, this result cannot select secretion versus intracellular retention for engineered UOX.


**Protocol:**
- **Material:** Wild-type *A. oryzae* fermented on one fixed, matched rice substrate for both arms.
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

**Dependencies:** Standard wet-lab. It may share digestive-simulation infrastructure with §1.6, but it neither depends on §1.33 nor replaces the selected-UOX configuration test.

**Success criteria:**
- Estimate assay precision in a pilot, then compare retained activity for each native enzyme using prespecified reproducibility and noninferiority margins.
- A reproducible whole-biomass advantage supports that matrix for the native-enzyme track; no advantage keeps free extract and whole biomass unresolved or equivalent within the prespecified margin.
- No outcome from this native-enzyme assay selects engineered-UOX topology, formulation, or coating.

**Cross-references:** [§1.6](#16-koji-enzyme-stability-at-digestive-ph-and-temperature) (separate selected-UOX configuration test); [digestive-enzyme-optimization.md](./digestive-enzyme-optimization.md) §4 (native enzyme activity); [enzyme-quantification-protocol.md](./enzyme-quantification-protocol.md) §3 + §5 (assay methodology + sample preparation for the readouts above).

---

### 1.19 Methodological Standard — Rodent Cellular IC50 Translation Caveat

**Status**: Standing | **Cost**: $0 | **Weeks**: ongoing | **Phase**: 1 (methodology)

**Affected wiki**: [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [chembl-cross-check](./etc/chembl-cross-check.md), [supplements-stack](./supplements-stack.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), all per-compound pages citing rodent IC50 values.

**Standard (not an experiment — methodology):** Rodent cellular IC50 values for NLRP3 inhibitors and other inflammasome-pathway compounds may diverge from human cellular IC50 by up to 3 orders of magnitude. Anchoring example: **dapansutrile IC50 = 1 nM in mouse J774A.1 vs. 1,000 nM (1 μM) in human MDM** under LPS+nigericin stimulation (ChEMBL v34). Apply across the wiki:

1. **Tag every rodent-derived IC50 citation** with the species and assay format. Do not present rodent IC50 as if it were a clinical-grade potency claim.
2. **Prefer human-cell data** (THP-1, U937, primary human MDM, PBMC) over rodent cellular data when evaluating new compound candidates.
3. **For mouse-only compounds (β-caryophyllene, BHB rodent ketogenic-diet gout model, ursolic acid Kawasaki mouse, carnosine hyperuricemia rat),** propose human-cell follow-up assays before promoting from animal to clinical evidence tier.
4. **For compounds with no curated human IC50,** plan species-bridging experiments (THP-1 MSU IC50 head-to-head with rodent benchmark) as part of the validation queue rather than relying on rodent extrapolation.
5. **Counter-example to flag:** repurposing candidates with strong adjacent-indication human data (zileuton, disulfiram, avacopan) may translate **cleaner** than a compound with strong rodent gout data — species-gap failures stack, while existing human safety + PK data skip the failure mode.


**Cross-references:** [chembl-cross-check.md](./etc/chembl-cross-check.md) (curated ChEMBL evidence per compound), [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) §"Species-gap caveat" line 38, every per-compound wiki page citing rodent data.

---

### 1.20 Lactoferrin + EGCG CP1a Super-Additivity Assay (THP-1 Macrophage 3×3 Full Factorial + Prespecified Midpoint)

**Status**: Proposed | **Cost**: $1,500 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [lactoferrin](./lactoferrin.md), [egcg](./egcg.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [supplements-stack](./supplements-stack.md), [koji-endgame-strain](./koji-endgame-strain.md)

**What it tests:** Does combining lactoferrin-mediated LPS sequestration with EGCG-associated proteasome inhibition change IL-1β suppression in MSU-stimulated human macrophages relative to the prespecified additive null? **Tag: In Vitro for the component assays; Mechanistic Extrapolation for the interaction hypothesis.** This assay can identify an interaction under its tested cell conditions. It cannot establish a human combination, oral exposure, dose, or safety.


**Protocol:**
- **Cells:** PMA-differentiated THP-1 macrophages (or equivalent human macrophage source — primary MDM if available).
- **Stimulus:** LPS prime (signal 1) + MSU crystals (NLRP3 trigger, signal 2).
- **Treatment matrix (3×3 full factorial, n=4 per condition):**
  - Lactoferrin: 0, low, high (apo or holo recombinant; bracket plasma-achievable and koji-luminal-achievable concentrations)
  - EGCG: 0, low, high (bracket the 86 nM proteasome IC50)
  - If the prespecified IC50 × IC50 midpoint is not already one of those nine conditions, run it as a separately declared tenth condition.
- **Readouts:**
  - **IL-1β ELISA** (primary endpoint)
  - **IκBα Western blot** (mechanistic — confirms the EGCG arm is engaging the proteasome target; IκBα retention should track the 86 nM cellular IC50)
  - **LPS-binding assay** on lactoferrin-treated medium (mechanistic — confirms the lactoferrin arm is sequestering LPS rather than acting through an off-target mechanism)
- **Analysis:** Compute Loewe combination index across the matrix. CI <0.7 super-additive; 0.7–1.3 additive; >1.3 antagonistic.

**Estimated cost:** $1,500 — THP-1 cells + reagents (~$300), recombinant lactoferrin apo or holo form (~$400), EGCG standard (~$50), LPS + MSU (~$100), IL-1β ELISA kit (~$300), Western antibodies for IκBα (~$200), labor/materials (~$150).

**Estimated timeline:** 3–4 weeks (THP-1 differentiation 1 wk + assay 1–2 wk + analysis 1 wk).

**Dependencies:** Not gated on the dual-cassette build. Recombinant apo/holo lactoferrin can answer the biological combination question immediately. If the objective is specifically to compare koji-produced lactoferrin with commercial recombinant material, wait only for §1.9A Lf-only material, not §1.9C. Independent of [§1.7](#17-nlrp3-inflammasome-pathway-validation-thp-1-msu-macrophage-assay), but the IL-1β readout can fold into §1.7 to amortize THP-1 differentiation and ELISA fixed costs.

**Success criteria:**
- **Super-additive (CI <0.7):** advance the interaction to independent replication, concentration-response mapping, exposure assessment, and safety work.
- **Additive (CI 0.7–1.3):** retain the components as separate hypotheses; do not claim synergy.
- **Antagonistic (CI >1.3):** test whether apo-versus-holo lactoferrin distinguishes an iron-mediated interaction from another mechanism before deciding whether the pair warrants further study.

**Cross-references:** [synthesis/](../synthesis/README.md) 2026-04-24 Connection #4 + Proposed Experiment #2; [lactoferrin.md](./lactoferrin.md) §3 (LPS/CD14 sequestration mechanism); [egcg.md](./egcg.md) (20S proteasome 86 nM target, hepatotoxicity ceiling); [nlrp3-exploit-map.md](./nlrp3-exploit-map.md) v1.2 CP1a (independent input/output barrier framing); [supplements-stack.md](./supplements-stack.md) (current standalone entries for both compounds); [koji-endgame-strain.md](./koji-endgame-strain.md) (downstream engineering implication).

---

<a id="124-carnosine-co-expression-validation-in-a-oryzae-koji-endgame-optional-third-cassette"></a>
### 1.24 Carnosine Co-Expression Validation in *A. oryzae*

**Status**: Proposed | **Cost**: $1,500–2,500 | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [koji-endgame-strain](./koji-endgame-strain.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [carnosine](./carnosine.md), [androgen-urate-axis](./androgen-urate-axis.md)

**What it tests:** Whether an exact CarnS configuration, with a separately tested *panD* substrate-supply extension if needed, produces measurable carnosine without an unacceptable effect on host growth or any independently qualified payload. This is an expression and compatibility assay, not a product, demographic, dose, or efficacy claim.


**Protocol:**
- Transform *A. oryzae* RIB40 (or NSAR1 for auxotrophic selection) with single-copy `[PTEF1–CarnS–TamyB]` cassette integrated at a characterized neutral locus (specific locus TBD; see [koji-construct-design.md](./koji-construct-design.md) and [engineered-koji-protocol.md §03](./engineered-koji-protocol.md) for current standard choices). Selection marker: separate auxotrophic marker from uricase cassette (e.g., niaD or adeA if uricase uses pyrG).
- Ferment 100 mL on polished rice at 30°C, 48–60 h at 35% moisture.
- If β-alanine bottleneck is suspected after first pass, add a second construct with `[PTEF1–panD–TamyB]` and re-test.
- **Primary readout:** Carnosine titer by LC-MS (OPA/FMOC derivatization, quantify against a carnosine standard curve; β-alanine and histidine pools measured in the same run). Accept: ≥500 mg/L in pore fluid. Reject: <100 mg/L.
- **Secondary readouts:** Uricase titer (if dual-cassette strain; spectrophotometric urate-degradation assay at 293 nm), growth rate vs. parental strain (radial extension on PDA at 30°C), kojic acid baseline (HPLC), β-alanine and histidine pool sizes (LC-MS), carnosine stability through standard workup (measure before and after lyophilization + grinding).

**Dependencies:** Build and characterize the exact carnosine configuration before any multi-payload comparison. A combination test begins only after each single-payload configuration passes independently.

**Decision criteria:** Use qualified assay precision to prespecify carnosine-production, host-burden, and compatibility margins. A positive single-cassette result permits an independently designed combination assay; it does not select a UOX host or multi-payload architecture. A null result applies to the tested configuration and substrate-supply design.

**Cross-references:** [koji-endgame-strain.md §2.5](./koji-endgame-strain.md) (carnosine as optional third cassette, androgen-axis alignment); [engineered-koji-protocol.md §15](./engineered-koji-protocol.md) (full co-expression protocol, decision point, format constraints); [carnosine.md](./carnosine.md) (mechanism, gout-specific evidence, bioavailability); [androgen-urate-axis.md](./androgen-urate-axis.md) (URAT1 upregulation mechanism).

---

### 1.21 Natural-Product C5aR1 Antagonist Screening — Computational Pass (Closes the CP0 Fermentable-Coverage Question)

**Status**: Closed (negative result, 2026-04-27) | **Cost**: $0 | **Weeks**: 0.5 | **Phase**: 1 (computational, complete)

**Affected wiki**: [complement-c5a-gout](./complement-c5a-gout.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) (CP0), [open-enzyme-vision](./etc/open-enzyme-vision.md) (CP0 gap statement).

**What it tests:** The then-current engineered-koji / yeast / supplement composition had a gap at **CP0**—the complement-priming chokepoint where MSU crystals → classical-pathway activation → C5a → C5aR1 binding → non-transcriptional NLRP3 priming. Avacopan is a synthetic small-molecule option. This experiment scans for a natural-product C5aR1 antagonist worth wet-lab triage or closes that candidate class pending new evidence. The hit-rate prior was low because known antagonists are dominated by synthetic constrained peptides and small molecules. A negative result is operationally useful: it narrows this exploit route without defining what the rest of the project must do.


**Protocol — what was actually run:**

1. **ChEMBL target confirmation and bioactivity pull.** Query ChEMBL REST API for target CHEMBL2373 (confirmed: human C5AR1, UniProt P21730, "C5a anaphylatoxin chemotactic receptor 1", G-protein-coupled receptor, single protein, *Homo sapiens*). Total bioactivity records at CHEMBL2373: **4,873** (April 2026 query). Filter the curated potent tail at pChEMBL ≥ 6 (sub-μM IC50, Ki, or EC50 against human receptor).
2. **Manual classification of the potent tail.** Walk the top ~20 highest-pChEMBL entries; classify each as synthetic vs. natural-product by inspecting molecule_type, structure_type, pref_name, and the `natural_product` flag on each ChEMBL molecule record. Distinguish "natural-product-derived synthetic peptide" (e.g., C5a C-terminal mimics) from true small-molecule natural products.
3. **Cross-database verification.** Search NPASS (Natural Products Activity & Species Source) and LOTUS (Naturally Occurring Chemical Compounds Storage) for any curated natural-product entry at C5AR1. Search NPAtlas for microbial natural products with reported C5aR1 activity.
4. **Open Targets cross-check.** Pull the C5AR1 known-drugs list from the Open Targets Platform (target ENSG00000197405) — surfaces clinical/preclinical compounds that ChEMBL may not have indexed yet, plus any natural-product-derived clinical assets.
5. **Targeted primary-literature search.** PubMed-via-WebSearch queries for: `"C5aR1" antagonist plant`, `"C5aR1" natural product flavonoid OR terpenoid OR alkaloid`, `"C5a receptor" inhibitor flavonoid IC50 cell-based`, `"C5aR1" inhibitor marine fungus`. Catches any plant- or microbe-source antagonist reported in primary literature without ChEMBL curation.
6. **Avacopan structural-class check.** Quick SwissSimilarity / pharmacophore scan against avacopan's cyclohexanecarboxamide / piperidine motif — most plant secondary metabolites won't share this scaffold but worth a fast pass. *(Skipped after step 5 returned <5 candidates — see "what was not run" below.)*

**What was not run, and why:** AlphaFold + AutoDock Vina docking against a curated natural-product library was deferred. The protocol gates docking on ≥5 wet-lab-validated or strongly-prior-supported natural-product candidates emerging from steps 1–5; the actual count was **0 wet-lab-validated natural-product C5aR1 antagonists**, with only 2 computational-only docking hits and 1 indirect "neutraligand" surfacing in the literature (detailed below). At <5 candidates, docking adds no signal — it would either re-derive the existing computational hits (already published) or surface novel docking-only leads of the same evidence tier as those already discounted. The wet-lab triage gate is the binding constraint, and there is nothing to triage.

**Result:**

- **Total ChEMBL bioactivities at human C5AR1 (CHEMBL2373):** 4,873 (April 2026; up from the 506 figure cited in the existing [`complement-c5a-gout.md`](./complement-c5a-gout.md) §10.1 — that older count was likely distinct compounds at a higher-confidence cutoff or an earlier ChEMBL release, not total bioactivity records; see cross-reference correction note in §10.1 follow-up).
- **Curated natural-product hits at human C5AR1 with wet-lab functional or binding data: 0.** No compound flagged `natural_product=1` in ChEMBL appears in the sub-μM potency tail. The full pChEMBL ≥ 6 list at CHEMBL2373 is dominated by synthetic cyclic peptides (PMX-53/PMX-205 series, 1995–2006 BMCL/JMC papers, IC50 18–60 nM in [125I]-C5a binding or PMN glucosaminidase release), synthetic imidazolidinones / piperazines / piperidines (the CO13 binding-competition series, IC50 25–450 nM), and clinical-stage allosteric small molecules in the avacopan structural class.
- **Apparent peptide hit, not a natural product:** CHEMBL217378 (sequence ISHKDMQLGR, EC50 1.3 nM in PMN polarization) initially looked natural-product-flavored at the sequence level but is curated as `molecule_type: "Protein"`, `natural_product: 0`, `pref_name: "ISHKDMQLGR"` — a synthetic decapeptide derived from C5a's own C-terminal sequence, designed as a receptor-engagement probe, not an isolated natural product.
- **Computational-only natural-product candidates from primary literature (no wet-lab confirmation):**
  - **Acteoside** (verbascoside; phenylethanoid glycoside; plant natural product widely distributed in *Olea europaea*, *Plantago*, *Verbascum*, *Rehmannia*, *Lamiales* generally) — Shaikh & Siu 2016, *Med Chem Res* 25:1564–1573 (PMID 27499603). Homology model of C5aR1 (Glide XP docking + MM-GBSA), ΔG_bind = −113.9 kcal/mol, XP GScore = −12.4 kcal/mol. Authors explicitly state: "biological experiments to validate this inhibitor are being planned as a future work." **No follow-up validation has been published in the decade since.** Evidence level: *Computational / homology-model docking only.*
  - **Toxicarioside** (cardiac glycoside from *Antiaris toxicaria*, the upas tree; latex traditionally used as a dart poison in Southeast Asia) — same Shaikh & Siu 2016 paper, ΔG_bind = −90.1 kcal/mol. **Not pursuable on safety grounds:** the *A. toxicaria* cardenolides (toxicariosides J/K/L/O, antiarin) are cytotoxic Na+/K+-ATPase inhibitors at sub-μM doses; this is a fundamentally toxic scaffold, fermentable or not. Evidence level: *Computational only.*
  - **Resveratrol** — Mishra et al. 2020, *J Biomol Struct Dyn* (PMID 32131707). Molecular dynamics + automated docking + MM-GBSA + circular dichroism + steady-state fluorescence biophysics. Critically, resveratrol binds **hC5a (the ligand)**, not C5aR1 (the receptor) — a "neutraligand" approach that prevents C5a from engaging C5aR1 by sequestering the soluble anaphylatoxin. Mechanistically distinct from receptor antagonism (direct receptor antagonism) but tangentially relevant. No reported potency in standard inhibitor units; the biophysics suggest binding but do not establish a functional IC50 on C5a-driven C5aR1 signaling. Evidence level: *Computational + cell-free biophysical binding; no functional assay.* This signal does not qualify resveratrol for CP0 placement.
- **Open Targets known-drugs list at C5AR1 (ENSG00000197405):** Avacopan (CCX-168, FDA-approved 2021, oral C5aR1 antagonist, 30 mg BID dosing, the canonical pharma reference) plus the upstream C5-binding biologics (eculizumab, ravulizumab, zilucoplan) which are not C5aR1-directed. **No natural-product-derived clinical or preclinical asset.**
- **NPASS / LOTUS:** No curated natural-product entries at C5AR1 / CHEMBL2373 surface in either database (queried 2026-04-27). NPASS contains 222,092 NP-target pairs across 5,863 targets; the absence of C5AR1 in this corpus is itself informative — it means that across the full curated natural-product activity landscape, C5AR1 has not been assayed with sufficient hit confirmation to merit a database entry.
- **Plant flavonoid CH50 literature:** As already documented in [`complement-c5a-gout.md`](./complement-c5a-gout.md) §10.2, broad complement-pathway inhibition (CH50, AP50) by quercetin, EGCG, baicalein, curcumin, resveratrol falls in the 50–500 μM range — 100–1000× weaker than synthetic C5aR1 antagonists, multi-target rather than C5aR1-selective, and not pursuable as CP0 coverage at dietary or supplement-achievable doses.

**Conclusion — CP0 fermentable coverage is closed for natural products.** The scan returned zero wet-lab-validated natural-product C5aR1 antagonists. The two computational-only plant hits (acteoside, toxicarioside) have not been functionally validated in the decade since publication despite the original authors' stated plans, and toxicarioside is non-pursuable on safety grounds anyway. Resveratrol's hC5a binding is mechanistically distinct (neutraligand, not antagonist) and biophysically weak. Avacopan remains the pharma adjunct at CP0; the engineered koji / yeast / supplements stack does not have, and structurally is unlikely to acquire, fermentable CP0 coverage. This is a useful negative result — it converts the existing CP0 gap statement from "we don't have natural-product coverage at CP0" to "we ran the scan; here is exactly what we found and exactly why avacopan is the answer," removing this question from the platform's open backlog.

**Re-open conditions:** (a) a new ChEMBL release (v35+) curates a sub-μM natural-product C5aR1 antagonist with primary-literature wet-lab confirmation; (b) a primary-literature paper reports a fermentable C5aR1 antagonist with functional cell-based or in vivo evidence; (c) avacopan loses regulatory or supply availability, raising the value of weaker fermentable backups; or (d) acteoside receives functional validation in C5aR1-expressing cells. Until then, this natural-product CP0 route stays closed.

**Cross-references:** [complement-c5a-gout.md](./complement-c5a-gout.md) §9 (CP0 platform gap) + §10 (natural-product modulator literature); [nlrp3-exploit-map.md](./nlrp3-exploit-map.md) (CP0 chokepoint); [open-enzyme-vision.md](./etc/open-enzyme-vision.md) ("CP0 gap — honest acknowledgment"); [synthesis/](../synthesis/README.md) 2026-04-24 Connection #2 + Proposed Experiment #3. Source: ChEMBL CHEMBL2373 (April 2026); Open Targets ENSG00000197405; Shaikh F, Siu SWI. *Med Chem Res* 25:1564–1573 (2016, PMID 27499603); Mishra et al. *J Biomol Struct Dyn* 2020 (PMID 32131707).

---

### 1.22 Gut-Compartment HDAC-Directed Candidate Screen for Q141K-ABCG2 Trafficking Rescue

**Status**: Proposed | **Cost**: $5,000–8,000 | **Weeks**: 8–10 | **Phase**: 1

**Affected wiki**: [abcg2-modulators](./abcg2-modulators.md), [supplements-stack](./supplements-stack.md), [gut-lumen-sink](./gut-lumen-sink.md)

**What it tests:** Q141K ABCG2 has a folding/trafficking defect that can be rescued by pharmacological/chemical-chaperone perturbation (Basseville et al. 2012, PMID 22472121). Direct Q141K rescue by butyrate was not shown in that paper. This experiment screens defined candidates for class selectivity, compartment-relevant activity, surface-trafficking rescue, functional urate efflux, and safety, with a Basseville-class rescue condition as the positive control.

**Design requirement:** include a tissue-selectivity assay (Caco-2 versus hepatocyte HDAC activity) and explicit HDAC1/2/3 focus; HDAC6 inhibition is off-target. The $5,000–8,000 estimate includes paired Caco-2/hepatocyte assays.

**Background on Q141K mechanism:** ABCG2-Q141K has a folding/processing defect that reduces surface transporter. Basseville 2012 provides a positive-control pharmacological/chemical-chaperone rescue pathway, but it did not report ~30–50% restoration at 1 mM butyrate. Butyrate must be treated as an unvalidated candidate in this assay, not as its established benchmark.

**Pharmacological-chaperone candidate class — computational route came back inconclusive (2026-07-14).** A parallel small-molecule pharmacological-chaperone route (CFTR correctors, bile-acid chaperones, tetramer stabilizers) was triaged computationally in [comp-032](./abcg2-q141k-chaperone-screen-computational.md) (descriptor screen, GREEN) and then re-screened with real AutoDock Vina docking in [comp-047](./abcg2-q141k-chaperone-rescreen-computational.md) → **INCONCLUSIVE**: the CFTR-corrector positive controls failed to earn rank (0/4), and rigid-receptor docking cannot discriminate chaperones (mechanism mismatch — a chaperone stabilizes a folding intermediate / raises ΔTm, which static-structure docking can't model). **No computationally validated chaperone candidate survives.** Consequence for this experiment: if the pharmacological-chaperone class is ever added as an arm here, comp-032's candidate list (lumacaftor, tafamidis, ursodiol, diflunisal, TUDCA) enters as **hypothesis-only** — this wet-lab assay would be the *first* real test of that route, not confirmation of a computational hit. The decisive computational next step, if pursued before wet-lab, is a folding-ΔΔG calculation (MD / Rosetta on the Q141K mutant), not another docking pass. This assay's readouts (WT/Q141K surface trafficking + basolateral→apical urate flux + ABCG2-inhibition counterscreen + cytotoxicity) are exactly what a chaperone-class test would require — so it doubles as the registered validation surface the comp-032 audit (2026-07-13) asked for.

**Protocol:**

**Stage 1 — In silico candidate selection ($500):**
- Compile defined candidates with documented HDAC inhibition: butyrate/short-chain fatty acids (test candidates, not established Q141K-rescue benchmarks), sulforaphane, allyl mercaptan, phenethyl isothiocyanate, hydroxycinnamic acids, and diallyl disulfide. Dietary occurrence does not establish safety or regulatory transfer at the tested exposure.
- Screen each candidate against: class I HDAC (HDAC1/2/3) IC50 from ChEMBL / primary literature; HDAC6 IC50 (if known — selectivity check); Caco-2 permeability / gut-lumen-achievable concentration estimate; reported hepatotoxicity signal (LD50 or NOAEL from TOXNET / EFSA).
- Select top 5–7 candidates by gut-enriched concentration × class I HDAC potency ratio.

**Stage 2 — Paired Caco-2 / hepatocyte HDAC activity assay ($2,000–3,000):**
- **Cell lines:** Caco-2 (enterocyte model) and HepG2 or primary human hepatocytes (hepatocyte model). The primary screen discriminator is Caco-2 HDAC activity ÷ hepatocyte HDAC activity for each candidate at matched concentrations. Gut-selective candidates have ratio > 2 (more HDAC inhibition in enterocytes than hepatocytes).
- **Readout:** Fluorometric HDAC activity assay (FLUOR DE LYS-based or equivalent) in nuclear extracts from each cell type + 24h candidate treatment.
- **HDAC1/2/3 vs. HDAC6 isoform specificity:** use a class I-selective substrate (acetylated H3K9/H4K12 peptide) and a HDAC6-selective substrate (acetylated tubulin peptide) to distinguish isoform selectivity within the Caco-2 data.

**Stage 3 — Q141K ABCG2 trafficking rescue in HEK293T or Caco-2 Q141K-transfected cells ($2,500–4,500):**
- Transfect cells with ABCG2-Q141K-GFP construct (standard overexpression assay, as in Basseville 2012).
- Treat with top candidates at Caco-2-achievable concentrations, including butyrate as a test candidate. Use a Basseville-demonstrated pharmacologic HDAC-inhibitor rescue condition as the positive control, with matched vehicle and ABCG2-inhibition counterscreens.
- Readouts: ABCG2 surface expression (flow cytometry / confocal — ratio of membrane-localized to total GFP signal), urate efflux (transwell if Caco-2-based), ABCG2 protein abundance (Western — total vs. glycosylated mature form).

**HDAC isoform note:** HDAC1/2/3 and HDAC6 activity helps interpret mechanism and off-target risk. Isoform and tissue selectivity alone cannot establish Q141K rescue or safety; advancement requires the trafficking, functional-flux, cytotoxicity, and inhibition counterscreens above.

**Estimated cost:** $5,000–8,000 (in silico $500 + Caco-2/HepG2 HDAC assay $2,000–3,000 + trafficking rescue $2,500–4,500). Original synthesis proposal ($5,000) was optimistic for a design that includes paired tissue-selectivity assay; $8,000 covers the paired hepatocyte arm + Q141K-transfected cell assay.

**Estimated timeline:** 8–10 weeks.

**Success criteria:**
- **A candidate reproduces positive-control surface trafficking and functional urate flux without ABCG2 inhibition or unacceptable toxicity:** advance that exact material to independent replication and exposure validation.
- **No candidate, including butyrate, reproduces positive-control surface trafficking plus functional urate flux:** no Q141K-rescue agent is validated; do not infer rescue from HDAC selectivity alone.
- **A candidate with class I selectivity and hepatocyte-sparing profile emerges but doesn't rescue trafficking:** updates the Q141K rescue model (suggests additional misfolding mechanism beyond class I HDAC).

**Stage 1 results (comp-007, 2026-05-05):** In silico screen completed. Composite scoring (potency × HDAC6 selectivity × gut-enrichment proxy) across 7 candidates ranked: **Butyrate** (0.374, HIGH confidence — confirmed 167× HDAC6 selectivity, biochemical IC50 data from ChEMBL/ACS Med Chem Lett 2011) >> **Sulforaphane** (0.090, LOW — estimated IC50, HDAC6 profile uncharacterized) > **PEITC** (0.060, LOW — estimated IC50 by analogy with SFN). Caffeic acid and ferulic acid score 0 (no isoform-specific IC50 available). **Advancing to Stage 2:** Butyrate, Sulforaphane, PEITC. Stage 2 must include HDAC6 isoform-selective substrate assay for SFN and PEITC; butyrate's HDAC6 selectivity is confirmed. Full analysis: [`etc/experiments/comp-007-food-grade-hdaci-screen/`](./etc/experiments/comp-007-food-grade-hdaci-screen/). Interpretive wiki: [`wiki/food-grade-hdaci-screen-computational.md`](./food-grade-hdaci-screen-computational.md). Evidence level: Mechanistic Extrapolation.

**Cross-references:** [abcg2-modulators.md](./abcg2-modulators.md) §6; [gut-lumen-sink.md](./gut-lumen-sink.md); and [food-grade-hdaci-screen-computational.md](./food-grade-hdaci-screen-computational.md).

---

### 1.23 Androgen × MSU × NLRP3 in Macrophages — Tiered Mechanistic Protocol

**Status**: Proposed | **Cost**: Tier 1: $5–10K; full T1+T2+T3 cascade $105–160K | **Weeks**: Tier 1: 6–8; full cascade ~12 months | **Phase**: 1

**Affected wiki**: [androgen-urate-axis](./androgen-urate-axis.md) §"Beyond transporters: direct androgen effects on NLRP3 priming" and [nlrp3-inflammasome](./nlrp3-inflammasome.md).

**What it tests:** Whether testosterone/DHT directly modulates MSU-crystal-induced NLRP3 inflammasome activation in macrophages. The cited literature reports context-dependent androgen effects on innate-immune signaling but does not resolve the direction in an MSU challenge. This is a mechanistic experiment; it cannot by itself establish clinical stratification or treatment.

**Protocol — Tiered, gating logic:**

**Tier 1 — THP-1 macrophage in vitro screen ($5,000–10,000; 6–8 weeks):**
- **Cell line:** THP-1 monocytes differentiated to macrophages with PMA (50–100 nM, 48–72 hr).
- **Pre-treatment:** ± DHT at 1 nM, 10 nM, 100 nM, 1 μM (physiological → supraphysiological) × 24–72 hr. Vehicle control (ethanol or DMSO matched). Androgen receptor antagonist arm (flutamide 1 μM or enzalutamide 1 μM) for AR-dependence.
- **Challenge:** MSU crystals (50–200 μg/mL × 6 hr; ATP 5 mM × 30 min as orthogonal NLRP3 trigger control).
- **Readouts:** IL-1β secretion (ELISA, primary endpoint); caspase-1 cleavage (Western, p20/p10); ASC speck formation (immunofluorescence, % cells with specks); NLRP3 mRNA (qPCR baseline + post-priming); pyroptosis (LDH release).
- **Success criterion (Tier 1 → Tier 2):** ≥30% modulation of MSU-induced IL-1β by DHT pre-treatment at any concentration AND AR-dependence confirmed by antagonist arm. Either direction (suppression or amplification) is interpretable; null result closes the question without needing Tier 2.

**Tier 2 — Primary human PBMC-derived macrophages (gated on a Tier 1 signal):**
- Recruit a justified donor set without preselecting sex or a high-androgen phenotype. Record sex, age, measured androgen exposure, relevant medications, and inflammatory covariates prospectively.
- Repeat the Tier 1 perturbation and MSU challenge in primary cells with IL-1β, IL-18, target engagement, and cell-state controls.
- Prespecify whether the estimand is a direct concentration response, receptor dependence, or effect modification by measured donor exposure. Do not treat a donor's circulating concentration as the in-vitro dose.
- A null result closes only the direct macrophage effect under the tested cells, exposures, timing, and readouts.

**Tier 3 — In-vivo MSU model (gated on primary-cell confirmation):**
- Select sex, model, perturbation, exposure range, and controls from the Tier 1–2 mechanism and safety results; do not preselect a male-only or high-androgen design.
- **Standard gout model:** Subcutaneous air pouch raised over 6 days; MSU crystal injection (3 mg in PBS); 6-hr or 24-hr lavage.
- **Readouts:** Lavage neutrophil count (primary endpoint — this is the standard gout-model readout); IL-1β + cytokine cascade (IL-6, CXCL1, KC); pouch-tissue NLRP3 / ASC / caspase-1 by Western.
- **Success criterion:** Demonstrate whether manipulating circulating testosterone changes MSU-induced inflammation in the selected model, with measured exposure and a reproducible effect direction. The result remains model-specific and does not define a human regimen.

**BHB interaction arm:** Cross a prespecified BHB concentration-response with the DHT × MSU Tier 1 design. The primary readout is MSU-induced IL-1β stratified by DHT condition; HCAR2 expression can be exploratory. A reproducible interaction would justify receptor-dependence and primary-cell follow-up, not a human BHB dose.

**Estimated cost (full cascade):** Tier 1 $5–10K → +Tier 2 $20–30K → +Tier 3 $80–120K = **$105–160K total** if all tiers fire. Tier 1 alone is the entry cost; Tier 2/3 only proceed if signal warrants. The BHB interaction arm is a marginal add to Tier 1, not a separate tier.

**Estimated timeline (full cascade):** Tier 1: 6–8 weeks. + Tier 2: +12 weeks (gated). + Tier 3: +6 months (gated). Best case (early null at Tier 1): 8 weeks. Worst case (full cascade): ~12 months.

**Success criteria (overall):**
- **Concordant positive Tier 1 + Tier 2 + Tier 3:** establishes a model-specific direct androgen contribution and motivates a separately designed human observational or interventional study. It does not select an anti-inflammatory treatment.
- **Null at Tier 1:** Closes only the tested direct THP-1 macrophage effect. It does not establish that transporters are the sole androgen–urate mechanism or resolve effects in other cells, tissues, exposures, or time windows.
- **Tier 1 positive but Tier 2 null:** Indicates immortalized-line artifact; updates the literature scan and closes the in vivo escalation. No platform changes.

**Limitations:**
- Tier 1 uses an immortalized line — known limitations of THP-1 vs. primary cells (stable phenotype, possibly less responsive to MSU than monocyte-derived primary cells).
- Tier 2's donor stratification will have confounders (BMI, fiber intake, baseline inflammation). Statistical power calculation needed before recruitment.
- Tier 3's murine air-pouch model is the standard gout model but is acute, not chronic. Translating to chronic-flare biology requires additional model considerations.
- All three tiers focus on the priming + activation step. They do not address resolution (SPM pathway) or aggregated-NET amplification — those would be separate experiments.

**Cross-references:** [androgen-urate-axis.md](./androgen-urate-axis.md) §"Beyond transporters: direct androgen effects on NLRP3 priming" and [nlrp3-inflammasome.md](./nlrp3-inflammasome.md).

---

### 1.25 DAF/CD55 SCR1-4 Truncated Single-Cassette Expression in *A. oryzae* (CP0 Engineering Candidate Wet-Lab Gate)

**Status**: Proposed | **Cost**: $4,445–6,745 (two-arm) | **Weeks**: 6–8 | **Phase**: 1

**Affected wiki**: [daf-cd55-scr14-truncated-computational](./daf-cd55-scr14-truncated-computational.md), [hypotheses/H05-daf-scr14-cp0-thesis](./hypotheses/H05-daf-scr14-cp0-thesis.md), [chaperone-orthogonal-stacking](./chaperone-orthogonal-stacking.md), [koji-endgame-strain](./koji-endgame-strain.md), [complement-c5a-gout](./complement-c5a-gout.md), [modality-chokepoint-matrix](./modality-chokepoint-matrix.md)

**What it tests:** Can engineered *A. oryzae* (RIB40 or NSlD-ΔP10) secrete the truncated DAF/CD55 SCR1-4 construct (aa 35–285, residues immediately following the signal peptide cleavage site through the end of SCR4 — see [comp-012](./daf-cd55-scr14-truncated-computational.md)) as a correctly-folded, complement-regulatory-active soluble protein? This is the wet-lab gate for the CP0 closure thesis: comp-012 confirmed protease stability (LOW risk in shio-koji), but expression + correct disulfide folding + retained CCP-regulatory activity have to be demonstrated empirically before the construct becomes a real platform component.

**Single-cassette scope.** This experiment measures expression, folding, and activity of DAF SCR1-4 alone. The [chaperone-orthogonal stacking framework](./chaperone-orthogonal-stacking.md) is a computational prior, not evidence that a triple cassette will fail or that separate strains are preferred. A positive result qualifies this exact single-cassette material for replication; it does not select a combined architecture or chassis.

**Co-primary role — chaperone-framework calibration set (re-scoped 2026-05-16, mandatory):** this experiment is the CCP/SCR data point in the calibration set documented in [`chaperone-orthogonal-stacking.md` §3.5.4](./chaperone-orthogonal-stacking.md) (paired with §1.9's lactoferrin transferrin-lobe data point). Pre-registered framework prediction: **≥100 mg/L** DAF SCR1-4 if the framework's α coefficients transfer to koji — substantially higher per-cassette titer than lactoferrin because of the lower α (CCP/SCR 0.3–0.6 vs. transferrin-lobe 1.5–2.5). **The NSlD-ΔP10 calibration arm is now mandatory** (was "optional" through 2026-05-15; re-scoped 2026-05-16 after the riskiest-assumption verdict named the framework's α coefficients as the single load-bearing belief least supported by the corpus — see [`chaperone-orthogonal-stacking.md` §8 item 6](./chaperone-orthogonal-stacking.md) for the framework's own calibration uncertainty). Calibration-arm conditions: matching host = NSlD-ΔP10, matching format = solid-state shio-koji, matching promoter as §1.9, matching titer units (mg/L mature protein by ELISA). Without this arm under harmonized conditions, the host/format mismatch confounds the §1.9 + §1.25 comparison and the framework cannot recalibrate α — leaving every downstream architecture decision (separate-strain DAF routing, triple-cassette feasibility, single-strain multi-payload hypothesis) resting on un-validated coefficients. **The RIB40 arm runs in parallel** as the primary CP0 engineering candidate validation; the two arms together satisfy both §1.25's original objective and the framework calibration role.

**Gate:** comp-012 returned LOW protease risk. The current design uses the verified eight-disulfide count from UniProt P08174.

**Background on the gating context:** comp-012 (2026-05-05) confirmed the SCR1-4 truncated construct is shio-koji protease-stable (LOW verdict, max risk score 0.039 — identical to uricase, 10× drop from the comp-006 full ectodomain HIGH verdict driven by removing the Ser/Thr-rich stalk aa 286–353). H05 stub (2026-05-05) registered the CP0 closure thesis as a falsification card with three named wet-lab unknowns: (1) does SCR1-4 retain complement-regulatory activity without the stalk, (2) can *A. oryzae* fold 8 intrachain disulfides per molecule (corrected from 12, per UniProt P08174 DISULFID feature annotations: Cys36-Cys81, Cys65-Cys94 [SCR1]; Cys98-Cys145, Cys129-Cys158 [SCR2]; Cys163-Cys204, Cys190-Cys220 [SCR3]; Cys225-Cys267, Cys253-Cys283 [SCR4]), and (3) does the construct express at therapeutic-relevant titer. This experiment addresses all three.

**Effective PDI load context (from chaperone framework refinement, 2026-05-06):** 8 disulfides × CCP/SCR architecture coefficient α=0.3-0.6 = effective PDI load **2.4-4.8 disulfide-equivalents** — substantially lighter than the 16-disulfide lactoferrin transferrin-lobe load of 24-40 effective (Notari 2023, PMC10465537). This predicts that single-cassette DAF SCR1-4 is comparatively tractable, including on wild-type RIB40, but does not demonstrate secretion capacity; §1.25 is the empirical gate.

**Protocol:**

- **Construct design.**
  - Candidate cassette: `[PamyB — *A. oryzae* α-amylase signal peptide — DAF SCR1-4 mature sequence (aa 35–285 of UniProt P08174, codon-optimized for *A. oryzae*) — TamyB]`. Direct secretion via amyB SP, no glucoamylase fusion. Selection-marker choice does not establish safety or regulatory status.
  - Codon optimization: full optimization for *A. oryzae* codon table — DAF/CD55 native codon preferences are mammalian (high-GC) and broadly compatible with *A. oryzae* (~54% GC) but standard gene synthesis optimization captures any remaining suboptimal codons. Cost: ~$300-500 for codon-optimized gene synthesis (~750 bp).
  - **Disulfide assessment design:** the 8 disulfides form 2 per SCR domain in the canonical sushi/CCP fold (Cys1-Cys3, Cys2-Cys4 motif within each ~60-aa domain). Misfolding modes to detect: (a) intermolecular disulfide-linked aggregates (would show up as high-MW bands on non-reducing SDS-PAGE), (b) within-domain mis-pairing (would not show up on SDS-PAGE but would compromise CCP-regulatory activity), (c) mature protein with reduced free Cys (would show up as smaller MW on non-reducing SDS-PAGE indicating fewer than 8 disulfides formed). All three are detectable with the Western + activity assay readouts below.

- **Host strain — two parallel mandatory arms.**
  - **RIB40 arm** (genome-sequenced reference) — primary CP0 engineering candidate validation. Per the chaperone framework, single-cassette DAF SCR1-4 (effective PDI load 2.4–4.8) should be well within RIB40's secretion capacity; this arm carries the §1.25 primary objective.
  - **NSlD-ΔP10 arm** (10-protease-deletion via Maruyama lab path per [`operations/ward-1995-lab-access.md`](../operations/ward-1995-lab-access.md)) — chaperone-framework calibration arm, mandatory. Run under matching solid-state shio-koji format and matching promoter as §1.9 so the §1.9 + §1.25 titer comparison is the framework's α-recalibration measurement. The reason this arm is mandatory (not "optional pending RIB40 results") is that recalibration only works on harmonized-condition data; RIB40-only execution forfeits the calibration role even if RIB40 succeeds on the engineering objective.

- **Transformation.** PEG/CaCl₂ protoplast, single-step transformation → select on pyrG-minus → confirm cassette integration by PCR + qPCR for copy number stability across 5 serial passages.

- **Fermentation.** Solid-state rice koji, 48–60 h at 30°C, 35% moisture (the project's standard koji condition; matches §1.9 dual-cassette fermentation conditions for downstream comparability). Parallel submerged-culture control (100 mL shake flask, 28°C) to isolate solid-state vs. submerged variable.

- **Readouts.**
  - **Secretion + apparent MW:** SDS-PAGE under reducing AND non-reducing conditions on culture supernatant. Reducing condition: detect monomeric ~28 kDa band (predicted from 251-aa mature protein × ~110 Da/aa average + glycosylation if any). Non-reducing condition: confirm intramolecular disulfide formation (band shifts to slightly lower apparent MW vs. reducing) AND absence of high-MW aggregation bands (absence = no intermolecular Cys mis-pairing). Western blot with anti-DAF/CD55 antibody (commercial — Abcam ab1422 or similar) to confirm identity.
  - **Quantitative titer:** anti-DAF/CD55 ELISA on culture supernatant. Target: ≥50 mg/L pore-fluid equivalent (mirroring the H01 lactoferrin floor scaled for the smaller protein).
  - **Disulfide folding fidelity:** mass spectrometry (MALDI-TOF or LC-MS) on purified protein under non-reducing conditions to confirm correct disulfide pairing (8 expected) vs. mispaired isoforms. This is the load-bearing readout for the CP0 thesis — protease-stable + secreted ≠ functionally folded.
  - **CCP-regulatory activity assay:** zymosan-activation assay measuring C5a generation in human serum + purified recombinant DAF SCR1-4 vs. control (heat-denatured DAF SCR1-4 + buffer-only). Target: ≥30% C5a-generation inhibition vs. control at therapeutically-plausible DAF concentration (rough target ~1-10 μg/mL based on literature soluble DAF activity ranges). This is the H05 third wet-lab unknown — does SCR1-4 retain complement-regulatory activity without the stalk?
  - **Native metabolite profile** (carryover check): kojic acid titer (HPLC) + ergothioneine titer (LC-MS) — confirm WT baseline preserved within 30% on the engineered strain (i.e., the heterologous DAF cassette doesn't perturb the native koji metabolite chorus that contributes to the CP1a + CP1b coverage per `koji-endgame-strain.md` §1).

**Plasmidsaurus QC pipeline:** apply the canonical [§05 Plasmidsaurus QC pipeline](./engineered-koji-protocol.md#step-5-strain-qc-infrastructure-plasmidsaurus-pipeline-for-plasmid--transformant--strain-verification) across both arms (RIB40 + NSlD-ΔP10):
- **Pre-transformation:** Whole Plasmid Sequencing of the single DAF SCR1-4 cassette plasmid ($15 × 1 = **$15**, 1 day).
- **Post-transformation clone screening (per arm):** Genotyping Analysis on 6–10 transformants per arm to pick clean on-target integrants ($30 × 8 × 2 arms = **$480**, 1–2 days each).
- **Junction PCR sequencing (per arm):** Amplicon Sequencing on 2–4 junction PCRs per integration ($15 × 4 × 2 arms = **$120**, next-day each).
- **Final platform-strain release (per arm):** Whole Genome Sequencing on each validated arm strain (Eukaryotic tier, $250 + $15 extraction = $265 × 2 = **$530**, 3–6 days each). Both arms get publish-grade sequences for the open-source-strain-library release since the dual-arm framework-calibration role means both are platform-relevant outputs.

**Plasmidsaurus QC pipeline subtotal: ~$1,145, ~25–35% of the §1.25 envelope.** Higher fraction than §1.9 because §1.25 has two parallel arms (mandatory per the 2026-05-16 re-scope) each requiring its own full QC pass.

**Estimated cost ($4,445-6,745 breakdown):**
- Codon-optimized gene synthesis: $300-500
- Cloning + transformation reagents: $400-600
- Fermentation consumables: $200-300
- Anti-DAF antibody (commercial): $400-600
- ELISA reagents + Western consumables: $500-700
- Mass spec analysis (outsourced to core facility): $300-500
- Zymosan + complement activity assay reagents: $200-400
- Plasmidsaurus QC pipeline (both arms: plasmid + amplicon + genotyping + whole-genome): ~$1,145
- CRO or academic lab time if outsourced: $1,000-2,000 (otherwise embedded in lab partnership)

**Estimated timeline (6-8 weeks breakdown):**
- 2-3 weeks: gene synthesis + construct assembly + cloning verification
- 2 weeks: transformation + clonal screening + copy-number stability check
- 1 week: parallel fermentation (solid-state + submerged controls)
- 2 weeks: full assay suite (SDS-PAGE + Western + ELISA + MS + activity assay) + write-up

**Dependencies:** Same lab-access pathway as §1.9 — a Role 2 (Pharma Translation) collaborator (per [`etc/team.md`](./etc/team.md)) if recruiting converts; commercial CRO specializing in filamentous-fungus engineering (Lonza, Novozymes, Dyadic); community biolab with protoplast-transformation capability (Genspace NY has *A. oryzae* precedent). Global parallel options mapped in [`operations/ward-1995-lab-access.md`](../operations/ward-1995-lab-access.md). **This experiment shares lab-access infrastructure with §1.9** — both are *A. oryzae* protoplast transformation + solid-state koji fermentation + standard mammalian-protein readout assays. If §1.9 is running in a partner lab, §1.25 is a natural co-batch experiment with marginal infrastructure cost (sequential transformations on the same host, parallel fermentations under the same conditions).

**Success criteria:**
- **Accept** (proceed to integration with the koji track — sister-strain co-ferment with uricase + Lf multi-payload strain, OR queue for LBP-chassis transfer): secreted titer ≥50 mg/L pore-fluid equivalent + correct apparent MW on non-reducing SDS-PAGE + ≥40% native disulfide-folded form on mass spec + ≥30% C5a-generation inhibition vs. control at therapeutically-plausible DAF concentration + native metabolite program preserved within 30% of WT.
- **Iterate** (adjust architecture, re-test): titer 10-50 mg/L OR 20-40% native folded form OR 10-30% C5a inhibition. Compare the mandatory RIB40 and NSlD-ΔP10 arms, then optimize the better-performing background with alternative integration sites or an alternative signal peptide (TamyG or glaA SP).
- **Reject** (DAF SCR1-4 not viable in koji chassis; route to LBP chassis or shelve CP0 closure thesis): titer <10 mg/L after two optimization rounds, OR <20% native folded form, OR no detectable CCP-regulatory activity, OR native metabolite program collapse (kojic acid down >50% vs. WT). Reject outcome triggers H05 falsification card update (Killshot #1 fired) and re-routing of CP0 closure to the [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) peer track or the soluble-Factor-H-fragment alternative documented in `complement-c5a-gout.md`.

**Computational priors that informed this design:**
- [comp-012 (2026-05-05)](./daf-cd55-scr14-truncated-computational.md) — protease stability LOW verdict for the SCR1-4 construct; gates the wet-lab feasibility question
- [chaperone-orthogonal-stacking framework](./chaperone-orthogonal-stacking.md) §3.5 + §4 — per-architecture α coefficient for CCP/SCR fold (0.3-0.6) gives effective PDI load 2.4-4.8 for single-cassette DAF SCR1-4, predicting tractability but not substituting for §1.25
- [chaperone-orthogonal-stacking framework](./chaperone-orthogonal-stacking.md) §5.5 — triple-cassette prediction lands below 0.6 decision gate, supporting the **separate-strain (single-cassette) routing** decision encoded in this experiment design
- **[comp-030 (2026-05-15)](./daf-cd55-scr14-cassette-ranking-computational.md)** — exhaustive cassette ranking (43,200 candidates; 6 promoters × 12 SP × 10 codon variants × 60 scaffolds). Top cluster: **PamyB + SPamyB + max-CAI codon variant + direct-secretion scaffold (His6 or no C-term tag) + no propeptide**. §1.25 baseline survives; one gene-synthesis-time refinement warranted: use **max-CAI codon optimization** (NOT 5'-softened — DAF SCR1-4's first-30 aa generate favorable 5' MFE under max-CAI; 5'-softening is target-specific to uricase). α-coefficient **CORROBORATED**: ESM2 pseudo-pLDDT mean = 88.8, std = 0.5, 100% of 720 protein-distinct candidates above pseudo-pLDDT 80 — consistent with CCP/SCR fast-folding, α = 0.3–0.6. (Mechanistic Extrapolation; in silico only.) Full analysis: [`wiki/daf-cd55-scr14-cassette-ranking-computational.md`](./daf-cd55-scr14-cassette-ranking-computational.md).

**Limitations:**
- Single-cassette test does not directly answer whether DAF SCR1-4 can co-express with uricase + Lf in a triple cassette (that would be a separate, gated experiment if the chaperone framework's prediction proves too pessimistic in the §1.9 readout)
- Mass spec disulfide-pairing analysis assumes high-quality purification; if the purification step is suboptimal, mis-paired isoforms may be undercounted
- CCP-regulatory activity assay measures one specific complement readout (C5a generation in zymosan-activation); doesn't directly measure C3 convertase decay-acceleration (the canonical DAF activity) — that would be a follow-up assay if C5a-arm is positive
- No in vivo gut-lumen activity readout in this experiment — that's a Phase 2 / Phase 3 follow-up gated on positive in vitro result

**Cross-references:** [daf-cd55-scr14-truncated-computational.md](./daf-cd55-scr14-truncated-computational.md) (comp-012, the in silico prior); [hypotheses/H05-daf-scr14-cp0-thesis.md](./hypotheses/H05-daf-scr14-cp0-thesis.md) (the falsification card this experiment addresses); [chaperone-orthogonal-stacking.md](./chaperone-orthogonal-stacking.md) §5.5 (the triple-cassette prediction that motivated single-cassette routing); [koji-endgame-strain.md](./koji-endgame-strain.md) (sister-strain co-fermentation context); [engineered-lbp-chassis.md](./engineered-lbp-chassis.md) (alternative chassis if reject outcome); [complement-c5a-gout.md](./complement-c5a-gout.md) (the CP0 chokepoint biology); [operations/ward-1995-lab-access.md](../operations/ward-1995-lab-access.md) (lab-access shared with §1.9).

---

### 1.26 Cordycepin × Pentostatin × GLPP — Five-Arm ADA Half-Life Assay (ADA Chokepoint Synergy Validation)

**Status**: Proposed | **Cost**: $1,500–2,500 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [gout-pathophysiology](./gout-pathophysiology.md), [medicinal-mushroom-compound-mapping-computational](./medicinal-mushroom-compound-mapping-computational.md)

**What it tests:** Whether pentostatin, a characterized GLPP fraction, or their source-material combinations change ADA-driven cordycepin loss in vitro relative to the corresponding single-material controls. The assay measures biochemical stability; it does not establish an oral product, dose, urate effect, or clinical use.

**Design requirement:** the fifth arm tests the two-organism combination, which is not represented by purified pairings or whole-fermentate alone.

**Background — the ADA chokepoint:** ADA deaminates cordycepin. Pentostatin is co-produced with cordycepin in *C. militaris* in the cited BGC study (Xia 2017, PMID 29056419); the GLPP arm tests a separate proposed inhibition mechanism. The matched arms are required because source-material composition and inhibition cannot be inferred from the purified compounds alone.

**Protocol — Five-arm in-vitro design:**

| Arm | Composition | Tests |
|---|---|---|
| **1. Cordycepin alone** | Recombinant human ADA (Sigma A6535) + cordycepin standard (Sigma C3394, 100 µM) in PBS pH 7.4, 37°C | Baseline ADA-driven cordycepin deamination kinetics |
| **2. Cordycepin + pentostatin** | Arm 1 + research-grade pentostatin (Sigma P3650, 1 µM and 10 µM dose-response) | Pentostatin's quantitative ADA-inhibition contribution at gut-relevant concentrations |
| **3. Cordycepin + GLPP** | Arm 1 + GLPP-enriched fraction from a SEC-MALS-characterized *G. lingzhi* dual-decoction extract (per [SOP-1](./medicinal-mushroom-extract-sops.md), 100 µg/mL polysaccharide-peptide) | GLPP's ADA-inhibition contribution alone, mechanistically distinct from pentostatin |
| **4. Whole-fermentate *Cordyceps***  | Total water/ethanol-coextract from *C. militaris* (GYS60 strain or commercial fruiting-body extract; cordycepin-equivalent dose normalized to 100 µM via SOP-2 HPLC quantification) | Whole-fermentate co-delivery of cordycepin + native pentostatin in their natural ratio — single-organism baseline |
| **5. Whole-fermentate *Cordyceps* + GLPP** | Arm 4 + GLPP from Arm 3 | The two-organism combination — does adding mechanistically-orthogonal GLPP-mediated ADA inhibition further extend cordycepin half-life beyond what whole-fermentate's native pentostatin already delivers? |

**Primary readout:** cordycepin remaining at t = 0, 15, 30, 60, 120, 240 min, measured by HPLC (per [SOP-2](./medicinal-mushroom-extract-sops.md) cordycepin quantification — calibrated reference standard). Compute half-life per arm. Loewe combination index for arms 2/3/5 vs. additive expectation.

**Secondary readout:** ADA enzyme activity (residual deamination rate) measured directly via commercial ADA assay kit (Diazyme, 1064-330) — confirms the ADA-inhibition mechanism rather than off-target cordycepin protection.

**Success criteria:**
- If Arm 5 shows the prespecified half-life extension over Arm 4 and the secondary readout supports ADA inhibition, advance that exact material pair to independently designed pharmacokinetic and safety work.
- If Arm 5 does not improve on Arm 4, GLPP does not advance as an incremental component under these assay conditions.
- If Arm 4 does not improve on Arm 1, the whole-fermentate protection hypothesis is not supported under these assay conditions.

**Limitations:**
- In vitro ADA assay does not capture gut-microbiome metabolism of cordycepin (which may matter for in vivo half-life). The half-life extension demonstrated here is necessary but not sufficient for clinical effect.
- Recombinant human ADA (Sigma A6535) is the standard substrate but doesn't model intestinal mucosa-localized ADA dynamics. Mouse PK study (queued as gated follow-on) is the next-step de-risker.
- GLPP fraction quality is load-bearing — Tier 3 SEC-MALS characterization per SOP-1 is non-negotiable. Generic "reishi extract" cannot substitute. Per the [structure-dependent β-glucan caveat](./medicinal-mushroom-complement-track.md#consumer-product-caveat--structure-dependent-β-glucan-nlrp3-directionality), wrong-fraction substitution would produce uninterpretable results.

**Cross-references:** [medicinal-mushroom-complement-track.md §"Combined / synergy candidates"](./medicinal-mushroom-complement-track.md); [gout-pathophysiology.md §"ADA (Adenosine Deaminase) — Purine Catabolism Chokepoint Candidate"](./gout-pathophysiology.md); [medicinal-mushroom-compound-mapping-computational.md](./medicinal-mushroom-compound-mapping-computational.md) (comp-014 Phase 2).

#### Sixth-arm extension — engineered-koji cordycepin + GLPP (**Deprioritized 2026-05-16**; gated on strain availability)

> **Deprioritized 2026-05-16 — koji-cordycepin engineering removed from active cassette stack.** The sixth arm tests engineered-koji cordycepin + GLPP for ADA half-life protection; with the koji-cordycepin engineering effort deprioritized (full reasoning at [`koji-endgame-strain.md` §3.5](./koji-endgame-strain.md)), the §1.26 base assay (Arms 1–5) stands as the canonical ADA-protection investigation — those arms use whole-fermentate *Cordyceps* and purified compounds, all available via the cultivation track. Sixth arm is moot until/unless koji-cordycepin engineering is re-prioritized.


**Status**: Proposed extension to §1.26 base | **Cost**: ~$500–1,000 adder | **Weeks**: same as §1.26 base | **Phase**: 2 | **Hard gating**: engineered-koji cordycepin strain must exist (downstream of §1.9-extended design + comp-025 ADA-competition GREEN + comp-028 three-axis GREEN)

**What it tests:** Can koji-track cordycepin (lacking the native pentostatin that *C. militaris* co-produces from the same BGC) achieve ADA half-life protection equivalent to whole-fermentate *Cordyceps* by leveraging GLPP's polysaccharide-binding ADA inhibition? Specifically: does engineered-koji cordycepin extract + GLPP match the whole-fermentate *Cordyceps* native arms (§1.26 Arms 4 + 5) on ADA half-life?

**Why a sixth arm:** the base assay does not test an independently characterized engineered-koji cordycepin material. If that material ever exists, a sixth arm could compare its ADA-driven loss with the other exact materials. The assay would remain a biochemical interaction test, not a delivery or product decision.

**Distinction from §2.7:** §1.26 measures ADA-driven loss under defined in-vitro conditions. §2.7 would measure stability of a different exact material pairing. Neither assay establishes a preferred combination, exposure, efficacy, or safety.

**Arm 6 protocol:** identical to §1.26 base — ADA challenge (recombinant human ADA, Sigma A6535) at defined enzyme concentration, sampling at 0/15/30/60/120/240 min, LC-MS cordycepin vs. 3'-deoxyinosine quantification — but the substrate is engineered-koji cordycepin extract (cns1+cns2 strain, post-fermentation extraction per [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) SOP-2) co-administered with Tier 3-anchored GLPP (per SOP-1 SEC-MALS characterization).

**Success criteria (sixth arm → next phase):**
- **Pass:** the sixth arm meets a prespecified half-life and ADA-activity margin versus the matched controls, justifying independent replication and material-specific exposure/safety work.
- **Ambiguous:** repeat only after resolving material identity, assay precision, or concentration selection.
- **Fail:** the sixth arm misses the prespecified margin; do not advance that exact interaction.

**Estimated cost:** $500–1,000 adder
- Engineered-koji cordycepin extract preparation (one-time, gated on strain): ~$200
- Additional LC-MS quantification samples (1 arm × 6 timepoints × 3 replicates = 18 samples × $35 ≈ $630)
- Tier 3-anchored GLPP reagent (shared with §1.26 base): negligible adder

**Estimated timeline:** same as §1.26 base — sixth arm runs in parallel with Arms 1–5 once the strain exists; no incremental wall-clock time.

**Limitations:**

1. Same in-vitro-ADA limitation as §1.26 base — recombinant human ADA doesn't model gut-microbiome metabolism of cordycepin.
2. The cordycepin extract from engineered koji may have different impurity profile than whole-fermentate *Cordyceps* extract; this affects interpretation only if impurities themselves modulate ADA activity (unlikely but flagged).
3. GLPP fraction quality is the same load-bearing requirement as §1.26 base — Tier 3 SEC-MALS characterization per SOP-1 non-negotiable.

**Cross-references:** §1.26 base (parent five-arm assay); [§2.7](#27-koji--cordyceps-co-formulation-stability-test--ada-challenge-assay--deprioritized-2026-05-16-archived-2026-05-29) (sister Tier 2 stability test on engineered-koji + whole-fermentate *Cordyceps* pairing — different ADA inhibitor source); [`medicinal-mushroom-complement-track.md` §"Combined / synergy candidates"](./medicinal-mushroom-complement-track.md) (the interaction hypothesis this optional arm tests); [`cordycepin-cassette-burden-computational.md`](./cordycepin-cassette-burden-computational.md) (comp-023 engineering thread); [`computational-experiments.md`](./computational-experiments.md) comp-025 (ADA × cns1 kinetic gate — must clear before this experiment runs).

---

### 1.27 Ergothioneine × Lactoferrin Interaction Assay in MSU-Stimulated THP-1 Macrophages

**Status**: Proposed | **Cost**: TBD | **Weeks**: TBD | **Phase**: 1

**Affected wiki**: [gout-pathophysiology.md](./gout-pathophysiology.md) (multi-track coverage map ROS / CP1b row), [lactoferrin.md](./lactoferrin.md), [medicinal-mushroom-complement-track.md](./medicinal-mushroom-complement-track.md), [koji-endgame-strain.md](./koji-endgame-strain.md)

**What it tests:** Whether ergothioneine and apo-lactoferrin change ROS and IL-1β individually and together under one defined macrophage assay. Distinct proposed mechanisms do not establish additivity, oral exposure, clinical sufficiency, or a product architecture.

**Design requirement:** Use measured free concentrations and prespecify the interaction null. The apo-versus-holo comparison tests whether iron loading changes the result; it does not by itself prove a Fenton mechanism.

**Sequencing:** run after or alongside §1.20 to share THP-1 macrophage + MSU stimulation + IL-1β ELISA infrastructure. Neither macrophage combination assay requires the full §1.9 dual-cassette strain; recombinant lactoferrin is sufficient for the biological question, with §1.9A material as an optional later equivalence arm.

**Protocol:**

- **Cells:** THP-1 monocytes differentiated to macrophages (PMA, 100 nM × 24h then rest 24h). Human cells chosen to avoid the rodent-IC50 translation gap per [§1.19 standing methodology](./validation-experiments.md).
- **Priming:** LPS (100 ng/mL × 4 h).
- **Stimulation:** MSU crystals (250 µg/mL × 6 h) — gout-relevant inflammasome trigger.
- **Treatment arms** (treatment 1 h before MSU, continued through readout):
  - Vehicle control
  - Ergothioneine alone: 1, 10, 100 µM (brackets dietary-achievable plasma range ~5–25 µM per [P. citrinopileatus correction in `medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) Phase 7-1c)
  - **Apo-lactoferrin alone: 10, 100, 500 µg/mL** (covers koji-pore-fluid-achievable concentrations)
  - **Holo-lactoferrin (iron-loaded) at 500 µg/mL — apo-vs-holo comparator arm** (tests whether additivity depends on iron sequestration rather than a generic anti-inflammatory effect)
  - Combination: ergothioneine 10 µM + apo-lactoferrin 100 µg/mL (mid-range × mid-range, Loewe-index reference point)

- **Primary readout:** IL-1β ELISA (gold-standard NLRP3 activation readout)
- **Secondary readouts:** intracellular ROS (DCFDA fluorescence), NF-κB priming (IκBα Western blot)
- **Analysis:** Prespecify an interaction model appropriate to the concentration-response data and report the interaction estimate with uncertainty. Analyze apo-versus-holo material as a mechanistic comparator.

**Decision criteria:** Independent replication of a prespecified interaction with concordant ROS, IL-1β, viability, and mechanism-proximal readouts can justify a later exposure and safety study of the exact pair. A null or antagonistic interaction keeps the components separate. No cell-assay outcome selects a chassis, formulation, dose, or combined product.

**Limitations:**
- THP-1 is a single human macrophage line; primary human MDM replication is required for translation.
- LPS + MSU stimulation is a two-signal model that doesn't capture all in vivo gout-flare priming pathways.
- Fenton chemistry in cell culture and a gut-lumen exposure are different compartments; an interaction in one does not establish the other.

**Cross-references:** [gout-pathophysiology.md §"Multi-track urate transporter coverage" ROS / CP1b row](./gout-pathophysiology.md) (the speculative claim this experiment gates); [lactoferrin.md §4.1](./lactoferrin.md) (Fenton-iron mechanism); [medicinal-mushroom-complement-track.md](./medicinal-mushroom-complement-track.md) (P. citrinopileatus EGT source); [validation-experiments.md §1.19](./validation-experiments.md) (rodent-IC50 species-gap discipline); [validation-experiments.md §1.20](./validation-experiments.md) (sister CP1a super-additivity assay sharing THP-1 + MSU infrastructure).

### 1.28 Tier 2 Colorimetric Cordycepin Assay Validation

**Status**: Proposed | **Cost**: ~$200 | **Weeks**: 2 | **Phase**: 1

**Affected wiki**: [medicinal-mushroom-extract-sops.md](./medicinal-mushroom-extract-sops.md) SOP-6; [quantification-ladder.md](./quantification-ladder.md); [cordycepin-cassette-burden-computational.md](./cordycepin-cassette-burden-computational.md); and [medicinal-mushroom-complement-track.md](./medicinal-mushroom-complement-track.md).

**What it tests:** Whether the diazo-coupling colorimetric assay proposed in [`medicinal-mushroom-extract-sops.md` SOP-6](./medicinal-mushroom-extract-sops.md) can quantify cordycepin against a reference method, or whether UV absorbance is the more defensible low-instrumentation fallback. This validates an analytical method; it does not validate an extract, dose, or intervention.


**Background on the gap:** SOP-6 proposes a Bratton-Marshall-style diazo-coupling colorimetric assay for cordycepin (3'-deoxyadenosine — a nucleoside analog with a primary aromatic amine accessible under hydrolysis conditions). The mechanism is plausible by analogy to nitrite-based colorimetric detection of aromatic amines (sulfanilamide, dapsone, etc.), but **no primary-literature precedent for cordycepin-specific diazo-coupling has been verified.** Until validated, the SOP carries the speculative caveat. UV 260 nm absorbance is the conservative fallback — cordycepin absorbs at λmax ~260 nm with ε ~14,500 M⁻¹·cm⁻¹, comparable to adenosine — but requires no derivatization and gives lower specificity (any 260-nm-absorbing contaminant interferes).

**Protocol:**

- **Reference standard:** Cordycepin reference standard (Sigma-Aldrich C3394 or equivalent, ≥98% purity, ~$50–80 for 10 mg). Prepare calibration series at 1, 5, 10, 25, 50, 100 µg/mL in 10% methanol/water (mirrors expected extract matrix).
- **Arm A — Diazo-coupling colorimetric:** Per SOP-6 draft — acid hydrolysis (1 N HCl, 60 °C, 30 min) to expose the primary amine, neutralize, then react with sodium nitrite + N-(1-naphthyl)ethylenediamine (NEDA) per the standard Bratton-Marshall procedure. Read absorbance at 540–560 nm. Record: linearity (R² of standard curve), LoD (signal:noise ≥ 3), LoQ (signal:noise ≥ 10).
- **Arm B — UV 260 nm fallback:** Direct absorbance at 260 nm in 10% methanol/water. Same calibration series. Same metrics.
- **Cross-validation:** Send 3 calibration concentrations (low, mid, high) to a Tier 3 anchor (HPLC-UV, contract lab e.g. Eurofins or university analytical service, ~$50/sample × 3 = $150). Compare Tier 2 result (both arms) vs. Tier 3 ground truth.
- **Specificity check:** Spike each calibration point with 100 µg/mL adenosine (the most likely cross-reactant — also a primary-amine-bearing nucleoside that diazo-couples). Quantify cross-reactivity: < 5% interference = clean; 5–20% = needs hydrolysis-condition optimization or column cleanup before diazo step; > 20% = method-fail for crude *Cordyceps* extracts (which contain orders-of-magnitude more adenosine than cordycepin by mass).

**Success criterion (test → next phase):**

- **Diazo-coupling GREEN:** linearity R² ≥ 0.98 across 1–100 µg/mL, LoD ≤ 2 µg/mL, adenosine cross-reactivity < 20%, Tier 2 vs. Tier 3 agreement within 20% on all three concentrations. → Promote SOP-6 from Speculative to Validated; update `medicinal-mushroom-extract-sops.md` to remove the caveat.
- **Diazo-coupling YELLOW:** linearity + LoD pass but adenosine cross-reactivity is 20–50%. → Investigate hydrolysis-condition optimization or simple C18 SPE cleanup before assay. Iterate.
- **Diazo-coupling RED** (linearity < 0.95 OR adenosine cross-reactivity > 50% OR Tier 2 vs. Tier 3 disagreement > 30%): use UV 260 nm fallback. Update SOP-6 to explicitly recommend UV 260 nm + downgrade the diazo path to "experimental, not for production quantification."

**Estimated cost:** ~$200 (cordycepin reference standard $50–80; diazo + UV reagents $20; Tier 3 anchor HPLC-UV $150; misc consumables $20).

**Estimated timeline:** 2 weeks (1 week reagent procurement + calibration; 1 week assay runs + Tier 3 turnaround).

**Limitations:**

1. The Bratton-Marshall-style diazo-coupling mechanism's applicability to cordycepin specifically is the speculative element this experiment tests. If literature surfaces a published precedent during execution, that may obviate the experimental validation step; check PubMed (English) + CNKI / J-STAGE per `Open Enzyme/CLAUDE.md` §"Global-multilingual research by default" before running.
2. Adenosine cross-reactivity is the most likely failure mode. If detected, the workflow may require a brief solid-phase cleanup (C18 SPE cartridge separates polar adenosine from less-polar cordycepin) before diazo, adding ~$5/sample.
3. Tier 3 HPLC-UV anchor cost is vendor-variable; $50/sample is a mid-range estimate. Verify quoting before committing.
4. The validation is on pure cordycepin reference standard. Real-world extract performance (cordycepin in a *C. militaris* fermentate matrix) is a separate downstream question — typically the next experiment after a clean reference-standard validation.

**Cross-references:** [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) SOP-6; [`quantification-ladder.md`](./quantification-ladder.md); [`cordycepin-cassette-burden-computational.md`](./cordycepin-cassette-burden-computational.md); and [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md).

---

### 1.30 Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages — prioritization screen

**Status:** Proposed | **Cost:** ~$1,500–2,500 | **Weeks:** 4–6 | **Phase:** 1

**Scope discipline: this is a prioritization screen, NOT a mechanism-confirmation assay.** The single question it answers is: *does any form of Houttuynia suppress MSU-induced IL-1β in THP-1 macrophages, and does purification vs. commercial sourcing matter?* Mechanism-specific work (CP0 complement-axis, CFH-dependence) is sequenced downstream in [comp-040](./computational-experiments.md) only if §1.30 returns a positive signal. Per the anti-pattern: do not try to make one cheap assay answer six scientific questions simultaneously.

**Affected wiki:** [`complement-c5a-gout.md`](./complement-c5a-gout.md) §9.7 (HCP/HCPM as Tier 1d dual-chokepoint candidate); [`nlrp3-exploit-map.md`](./nlrp3-exploit-map.md) §CP1 (Houttuynia entry); [`upstream-complement-modulator-sweep-computational.md`](./upstream-complement-modulator-sweep-computational.md) (comp-018 Phase 2); [`cfh-mechanism-dissociation-cp0-candidates-computational.md`](./cfh-mechanism-dissociation-cp0-candidates-computational.md) §3.3 (comp-039 HCP CFH-independence classification — sequenced after §1.30); [`supplements-stack.md`](./supplements-stack.md) (Houttuynia catalog entry).

**Why this matters:** Houttuynia is the corpus's first dual-CP0+CP1 dietary candidate. comp-039 classified HCP/HCPM/CHCP as CFH-independent on mechanism-site grounds, but cell-model translation is a separate question. Cheng 2014 (PMC7112369) documents structure-dependent directionality — purified 60 kDa HCP-2 is pro-inflammatory on naïve PBMCs while the anti-inflammatory phenotype appears in disease-context inflammation — so a generic "Houttuynia extract" capsule cannot be assumed equivalent to the Chen-group HCPM preparation without direct comparison.


**Protocol — three-arm fraction comparison:**

- **Arm A: HCPM (19.1 kDa Fudan RG-I fraction)** — the mechanistically-cleanest anti-inflammatory candidate: an acidic RG-I heteropolysaccharide, and **the only HC fraction with a direct NLRP3 / caspase-1 / IL-1β / IL-18-suppression readout** (Li 2025, PMID 40654358 / PMC12254813). Characterized in **Zhou 2022 (PMID 36252625)** — *not* Lu 2018 (PMID 29719782), which is the CHCP *crude* paper (citation corrected 2026-07-14 per the [structure-activity lit scan](../logs/houttuynia-polysaccharide-structure-activity-lit-scan-2026-07-14.md)). Sourcing: direct request to Chen Daofeng / Fudan group OR independent preparation following the Zhou 2022 protocol (ethanol precipitation + DEAE-Sepharose ion-exchange + Sephadex G-100 size-exclusion).
- **Arm B: Crude HCP** — a compositionally characterized boiled-water whole-herb extract, used to compare crude and purified material.
- **Arm C: Independent standardized extracts** — multiple lots with identity, composition, contaminants, and extraction method documented. This tests material equivalence, not consumer products.

Each arm: **three log-spaced doses (10, 100, 1000 μg/mL)** in MSU-stimulated THP-1 macrophages (1 × 10⁶/well, LPS pre-prime 100 ng/mL × 3 hr, MSU challenge 100 μg/mL × 6 hr). Vehicle-only and nigericin (NLRP3 activator) controls.

**Readouts (narrow):**
- **IL-1β supernatant ELISA** — primary endpoint. NLRP3-axis output; the signature gout-inflammation signal.
- **IL-6 supernatant ELISA** — secondary; serves triple duty at marginal cost: (a) broader inflammatory readout / technical-fail safeguard; (b) **CP1b amplifier probe** — Houttuynia's NF-κB suppression should hit TNFSF14-driven IL-6 amplification too ([`tnfsf14-gout-target.md`](./tnfsf14-gout-target.md)), tested on the same plate; (c) with the extract-alone arm (below), a **TLR4-priming detector** — a rise in extract-alone IL-6 flags signal-1 priming (see the directionality safety caution).
- **Cell viability (CCK-8 or MTT)** — confounder check. Required to interpret null results (cytotoxicity at high doses can masquerade as "no effect").

**Dropped vs. earlier draft:** C3a + sC5b-9 readouts removed. THP-1 macrophages don't reproduce serum complement biology cleanly — a positive complement signal could be "the CP0 mechanism translates" OR "local-macrophage complement leaked" OR "assay format artifact," indistinguishable. The CP0 mechanism question is answered in [comp-040](./computational-experiments.md) (CFH-depleted serum + MSU) where the full complement cascade is operative.

**Directionality safety caution + priming-only control arm.** The [Houttuynia polysaccharide structure-activity literature](../logs/houttuynia-polysaccharide-structure-activity-lit-scan-2026-07-14.md) establishes a mechanism-grounded risk this screen must control for:
- **Structure → direction.** *Homogalacturonan* (pure linear 1,4-α-GalA, ~60 kDa; the HCP-2 fraction) is a **direct TLR4/MD-2 agonist that raises IL-1β on naïve monocytes** (Cheng 2014, PMID 24528726; In Vitro). *RG-I / branched* fractions (HCPM, HC-PS1/3, HBHP-3) are anti-complement → anti-inflammatory in disease models. Same receptor (TLR4/MD-2), opposite outcomes — TLR4 engagement is necessary but not sufficient to predict direction; structure (HG vs RG-I) **and** context (naïve vs challenge) both move it.
- **The amplification risk.** MSU supplies signal-2 (NLRP3 assembly). If a Houttuynia material supplies **signal-1** (TLR4→NF-κB→pro-IL-1β priming) — which an HG-rich or crude/capsule extract can — it could **amplify** IL-1β rather than suppress it, inverting the readout. Xu 2015's same-material bidirectionality (pro-inflammatory alone, anti-inflammatory vs LPS; PMID 26190353) is the empirical proof the sign flips.
- **Required control — priming-only / extract-alone arm.** Run each arm **without MSU** (extract + vehicle, no MSU challenge) as a priming-detection control. A rise in IL-1β / IL-6 in the extract-alone condition flags TLR4-priming and makes the with-MSU result interpretable (suppression vs amplification). Without it, an amplifying extract is indistinguishable from a failed suppressor.
- **Arm guidance.** Purified HCPM is the mechanistic reference. Independent extracts are interpretable only when HG:RG-I composition and other material attributes are measured; a label or source category cannot substitute for characterization.
- **Context.** No HC polysaccharide has **ever** been tested in an MSU / urate / gout model (confirmed EN + Chinese corpora) — §1.30 would be the first, so the directionality caution is load-bearing, not hypothetical.

**Decision rules:**
- If **HCPM suppresses IL-1β under the prespecified margin and independent extracts fail to match**: record a material-specific in-vitro signal and retain the material-equivalence caveat. Then run the separately designed complement-mechanism assay.
- If **all three arms suppress IL-1β equivalently**: record equivalence only for the tested materials and assay endpoints. Human exposure, safety, and efficacy remain separate gates. **Fire [comp-040](./computational-experiments.md) next**.
- If **none of the three arms suppress IL-1β**: the mechanism does not translate to the macrophage model. **Deprioritize Houttuynia**; do NOT proceed to comp-040 — the mechanism work is wasted if cell-model translation fails.
- If **crude HCP performs ≥ HCPM**: purification is not required for this in-vitro endpoint; preparation reproducibility, composition, exposure, and safety remain open. **Fire [comp-040](./computational-experiments.md) next** for mechanism confirmation.

**Success criteria:**
- Detectable IL-1β baseline in MSU-stimulated vehicle controls (≥500 pg/mL by ELISA standard curve).
- Nigericin positive control reaches ≥3× MSU IL-1β (confirms NLRP3 axis intact).
- All three Houttuynia arms tested at full dose-response with cell viability ≥85% throughout.

**Dependencies:** Qualified THP-1 macrophage assay capability; verified HCPM identity; and independently prepared extracts with composition, contaminants, extraction, and lot provenance documented.

**Sequential gate logic** (this assay's position in the Houttuynia validation cascade):

| Gate | Question | Cost | Fires if... |
|---|---|---|---|
| **§1.30 (this assay)** | Does Houttuynia suppress MSU-induced IL-1β in a gout-relevant cell model, and does sourcing matter? | $1.5–2.5K | Always (prioritization screen) |
| **comp-040** | Is the CFH-independence classification correct? (mechanism confirmation) | Similar order | Only if §1.30 returns positive on at least one arm |
| **Controlled translational study** | Does an exact characterized material reach the target compartment and change a gout-relevant endpoint safely? | Design after preclinical evidence | Only after mechanism, exposure, and safety gates pass |

**Cross-references:** [`cfh-mechanism-dissociation-cp0-candidates-computational.md`](./cfh-mechanism-dissociation-cp0-candidates-computational.md) §3.3 (comp-039 HCP CFH-independence — mechanism-side analysis sequenced downstream); [`complement-c5a-gout.md`](./complement-c5a-gout.md) §9.7 (HCP/HCPM Tier 1d dual-chokepoint candidate); [`upstream-complement-modulator-sweep-computational.md`](./upstream-complement-modulator-sweep-computational.md) (comp-018 Phase 2 HCP discovery); [`logs/houttuynia-cp1-dual-mechanism-lit-scan-2026-05-19.md`](../logs/houttuynia-cp1-dual-mechanism-lit-scan-2026-05-19.md).

---

### 1.29 Cordycepin × Pentostatin × Substrate Matrix

**Status:** Proposed — pilot design required | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1

**Affected wiki:** [medicinal-mushroom-complement-track.md §Sourcing and delivery](./medicinal-mushroom-complement-track.md#sourcing-and-delivery); [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) §SOP-2 (cordycepin + pentostatin HPLC quantification) and [§SOP-7](./medicinal-mushroom-extract-sops.md#sop-7--substrate-engineering-protocol-matrix) (source-configuration registry).

**What it tests:** How substrate composition modulates the cordycepin:pentostatin ratio in an exact *C. militaris* configuration. The Xia 2017 BGC study (PMID 29056419) establishes co-production, not a stable ratio, protective interaction, exposure advantage, or clinical effect.

**Why this matters:** Ratio variability determines whether source materials can be compared and supplies defined inputs for a later ADA-interaction assay. It does not by itself establish cordycepin protection, pharmacokinetics, safety, or a preferred material.

**Design rule:** Do not combine solid PDA, submerged broth, insect substrate, and rice grain into one four-arm comparison. Culture format, strain, base medium, harvest, and extraction would be confounded. Run one matched control/intervention pair at a time.

**Stage 0 — analytical qualification**

- Confirm that SOP-2 resolves and quantifies cordycepin and pentostatin in the selected matrix using blanks, standards, spike recovery, and replicate precision.
- Set detection, precision, and biological effect margins from the qualified method and pilot variance before preregistering the result-bearing comparison.

**Stage 1 — reproduce one source configuration while adding the missing analyte**

- **Solid option:** *C. militaris* CM01 on the Yu 2024 PDA/light schedule, comparing 0 with 12 g/L L-alanine ([PMC11698586](https://pmc.ncbi.nlm.nih.gov/articles/PMC11698586/)).
- **Submerged option:** *C. militaris* GDMCC5.270 in the Chang 2024 base medium, comparing 5.0 g/L peptone with 1.5 g/L corn-steep-liquor hydrolysate plus 3.5 g/L peptone ([PMC10931215](https://pmc.ncbi.nlm.nih.gov/articles/PMC10931215/)).
- Hold strain, base medium, format, inoculum, temperature, timing, harvest, extraction, and assay constant within the selected option. Measure biomass or dry weight, cordycepin, pentostatin, and the cordycepin:pentostatin ratio.

The Turk 2022 oleic-acid result remains a candidate, but the article text does not report the supplement dose; it is not ready to serve as an exact replication arm. A rice-grain configuration should be tested separately with its own matched control, not used as the control for PDA or submerged culture.

**Stage 2 — transfer only an advancing result**

If Stage 1 reproduces the cordycepin direction and reveals a decision-relevant ratio change, test the same single variable in the intended production format with the intended strain. Treat that transfer as a new configuration with no assumed effect size.

**Decision rules:**
- If the ratio is stable within the prespecified analytical margin, carry the characterized material into the ADA-interaction assay; do not infer protection from co-production.
- If the ratio varies, treat substrate and harvest conditions as configuration variables and repeat the interaction assay for any advancing material.
- If either analyte is absent or unstable, narrow or close the corresponding co-production hypothesis for that configuration.

**Success criteria:**
- The assay passes its prespecified matrix-specific suitability criteria for both analytes.
- The selected source configuration is reproduced closely enough to interpret a matched pentostatin measurement; failure to reproduce the cordycepin direction closes or revises that configuration before transfer.
- Biological replicates support a prespecified confidence interval for the ratio effect. Analytical replicates do not substitute for biological replication.

**Dependencies:** SOP-2 HPLC infrastructure (cordycepin + pentostatin reference standards from Sigma C3394 + Cayman 10009152); *C. militaris* working strain with ITS-verified provenance (per SOP-5).

**Cross-references:** [medicinal-mushroom-complement-track.md §Sourcing and delivery](./medicinal-mushroom-complement-track.md#sourcing-and-delivery); [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) §SOP-2 and §SOP-7; [Culture configuration](./etc/open-source-platform.md#culture-configuration).

---

### 1.31 Butyrate Culture-Supernatant HPLC-UV Method Transfer Against GC-MS

**Status:** Proposed — partner design required | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1

**Affected wiki:** [`tier-2-butyrate-assay-audit-computational.md`](./tier-2-butyrate-assay-audit-computational.md) (comp-038); [`quantification-ladder.md`](./quantification-ladder.md); [`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md); §1.14; and [`open-questions.md`](./open-questions.md).

**What it tests:** Whether the De Baere HPLC-UV method can quantify butyrate in one exact engineered-strain culture-supernatant matrix with agreement adequate for the prespecified research decision. HPLC-UV is a **Tier 3 bench method** under the OE ladder. GC-MS is the reference comparator: Tier 3 when run in-house and Tier 4 when outsourced. This experiment validates a production measurement, not intestinal exposure, ABCG2 trafficking rescue, gout efficacy, or safety.

**Primary-source anchor:** De Baere et al. validated direct UV detection at 210 nm for bacterial culture supernatants after acidification below pH 2 and liquid-liquid back-extraction with diethyl ether. Matrix-matched calibration covered 0.5–50 mM, and the method quantified four short-chain fatty acids plus lactate (**In Vitro**, [PMID 23542733](https://pubmed.ncbi.nlm.nih.gov/23542733/)).

**Protocol-development requirements:**

- Select one exact strain, complete medium, culture format, harvest time, and sample-preparation workflow before setting acceptance criteria.
- Prepare matrix-matched sodium-butyrate calibration and spike/recovery samples across the decision-relevant range, bounded by the published 0.5–50 mM method range.
- Run sterile-medium, spent-medium, and analyte-interference controls. Detection at 210 nm is non-selective, so chromatographic separation and matrix effects are load-bearing.
- Measure the same biological samples by HPLC-UV and GC-MS. Set the biological-sample count after pilot variance and analytical-partner review.
- Prespecify method-suitability criteria for recovery, within- and between-day precision, calibration fit, chromatographic resolution, and HPLC-UV/GC-MS agreement before the result-bearing comparison.

**Decision rules:**

- **GREEN:** the prespecified method-suitability and reference-agreement criteria pass in the exact matrix. Adopt HPLC-UV as a matrix-qualified Tier 3 method for that configuration.
- **YELLOW:** standards pass but the biological matrix causes resolvable interference or unstable recovery. Revise extraction or chromatography and repeat qualification.
- **RED:** the method cannot meet the prespecified matrix or reference-agreement criteria. Use the GC-MS reference path for that configuration.

**Separate stool candidate:** Gu et al. reported an electrochemical/ANN workflow compared with GC-MS in an independent 30-sample fecal test set, with butyrate MAE/RMSE of 0.029/0.034 mM (**In Vitro**, [PMID 42041444](https://pubmed.ncbi.nlm.nih.gov/42041444/), [DOI](https://doi.org/10.3390/bios16040223)). That is a separate Tier 2 candidate for stool. It neither failed nor belongs in this culture-supernatant experiment; independent implementation and external validation remain open.

**Dependencies:** An analytical partner with HPLC-UV and GC-MS access; the exact production strain and medium; a pilot sufficient to set the result-bearing design.

**Cross-references:** [`tier-2-butyrate-assay-audit-computational.md`](./tier-2-butyrate-assay-audit-computational.md); [`quantification-ladder.md`](./quantification-ladder.md); [`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md); §1.14; §1.28; and [`open-questions.md`](./open-questions.md).

### 1.32 GSDMD-Pore Self-Delivery — Selectivity Probe (transporter-orphan tracer ± PepT1 blockade)

**Status**: Proposed (wet-lab gated) | **Cost**: ~$2,000–5,000 | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md) (the thesis under test); [`kpv-gsdmd-pore-influx-computational.md`](./kpv-gsdmd-pore-influx-computational.md) (comp-042 — the computational prior that reframed this experiment); [`kpv-peptide.md`](./kpv-peptide.md); [`disulfiram.md`](./disulfiram.md) (GSDMD-pore blocker for the control arm).

**What it tests:** Whether a membrane-impermeant payload is **selectively** concentrated in pyroptotic (GSDMD-pore-forming) macrophages versus intact-membrane cells — the load-bearing selectivity claim of the pore self-delivery paradox.

**Computational prior (comp-042, 2026-07-13):** A transport model returned **YELLOW (provisional)** — the flux physics is sound (a ~20 nm pore equilibrates the cell interior to the extracellular concentration in ~2 s; lifetime not limiting), but selectivity is the real decision variable and it is **falsified for KPV specifically**: KPV already enters cells via PepT1 ([Dalmasso 2008, PMID 18061177](https://doi.org/10.1053/j.gastro.2007.10.026)), and as an upstream inhibitor it arrives downstream of inflammasome firing. **This reframes the experiment** — a fluorescent-KPV uptake assay is PepT1-confounded and tests the wrong molecule. The clean test uses a transporter-orphan tracer.

**Protocol (redesigned per comp-042):**
- THP-1 (or primary human) macrophages, LPS + MSU-stimulated to induce GSDMD-mediated pyroptosis; ± controlled pore induction (low-dose nigericin as the pore-on lever).
- **Primary probe — transporter-orphan, membrane-impermeant tracer** (e.g. a small charged fluorescent dextran / calcein derivative with no peptide-transporter route): quantify intracellular fluorescence in pore-forming vs. intact cells by flow cytometry / confocal. Isolates the *pore* contribution with no transporter confounder.
- **PepT1-confounder control arm:** fluorescent-KPV ± a PepT1 inhibitor (or PepT1-knockdown), to directly demonstrate the confounder comp-042 predicts and quantify pore- vs. transporter-mediated KPV uptake.
- **Selectivity readout:** intracellular tracer (pyroptotic) ÷ (intact) — the pyroptotic-vs-healthy ratio.

**Success criterion:**
- **GREEN (pore-selectivity real):** transporter-orphan tracer uptake significantly higher in pore-forming vs. intact cells, reversed by a GSDMD-pore blocker (e.g. disulfiram). Green-lights a payload search under the comp-042 spec (transporter-orphan + downstream-acting).
- **RED (thesis fails at the physical step):** no differential uptake of the transporter-orphan tracer → the mechanism confers no selectivity; deprioritize the paradox.

**Sequencing:** This delivery/selectivity probe is the cheap first gate. KPV-specific efficacy work is deprioritized — comp-042 shows KPV is the wrong molecule to prove the concept with (PepT1 confounder + upstream/downstream timing). Supersedes the naive fluorescent-KPV design in the [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md) §"Open questions" Tier-1 precursor.

**Limitations:** Cell-line pyroptosis may not match primary synovial-macrophage pore kinetics; the transporter-orphan tracer is a physical proxy, not a therapeutic payload (a real payload must independently satisfy the downstream-acting criterion); synovial-macrophage PepT1 expression — the datum that gates KPV-route selectivity in vivo — is not resolved by this in vitro assay.

**Cross-references:** [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md); [`kpv-gsdmd-pore-influx-computational.md`](./kpv-gsdmd-pore-influx-computational.md) (comp-042); [`kpv-peptide.md`](./kpv-peptide.md); [`disulfiram.md`](./disulfiram.md).

<a id="133-physiological-uox-topology--oxygen--peroxide-factorial"></a>
### 1.33 Configuration-Level Physiological UOX × Oxygen × Peroxide Factorial

**Status:** Proposed — first physiological reaction-site gate after construct supply | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [gut-lumen sink](./gut-lumen-sink.md), [engineered koji protocol](./engineered-koji-protocol.md), [delivery-route matrix](./delivery-route-matrix.md)

**What it tests:** Whether an already built and characterized UOX configuration forms product under the human-baseline substrate prior and defined oxygen contexts without a configuration-specific peroxide or viability penalty. It can compare localization strategies within a controlled host background. It cannot declare a topology transferable across EcN, yeast, koji, purified enzyme, or another chassis when the configurations differ in more than localization.

**Entry requirements:**
- Every arm must exist before randomization and must have sequence identity, host or matrix, localization, active-UOX recovery, batch variance, and supporting machinery recorded.
- Yeast arms come from §1.2; koji arms come from §1.5; a PULSE/EcN arm requires the exact characterized strain or an explicitly bounded reconstruction. Catalase- or VHb-bearing arms require their own matched inactive-UOX and support-module controls.
- Within-host topology comparisons must freeze payload, host background, copy state, promoter class, and support modules as far as technically possible. Unmatched features make the result configuration-specific.

**Computational priors:** [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) shows that the legacy unconditional flat-dose robustness claim does not survive the tested diagnostics; it does not select a topology. [comp-045](./uricase-topology-oxygen-peroxide-design-computational.md) supplies a candidate randomized plate layout. Use only the subset for which qualified materials and matched controls exist, and regenerate the randomization before execution if that subset changes. Primary topology precedents: Gao et al. 2025 ([PMID 41038159](https://pubmed.ncbi.nlm.nih.gov/41038159/)) and Zhao et al. 2022 ([PMID 35491895](https://pubmed.ncbi.nlm.nih.gov/35491895/)).

**Protocol:** Run at least three independent biological batches under separately measured oxic and microoxic contexts. Test the human-baseline substrate prior plus prespecified sensitivity and source-benchmark conditions. At every substrate condition include matched inactive-UOX, host- or matrix-only, support-module, no-urate, and medium controls appropriate to that exact configuration. Measure urate and oxidative product, H₂O₂, dissolved oxygen, viability, localization, and active UOX at the reaction site. Report within-host contrasts separately from cross-configuration observations.

**Decision rule:** Advance an exact configuration only if it shows reproducible product formation at the human-baseline prior without a prespecified extracellular-H₂O₂ or viability penalty relative to its matched controls. A result confined to a high-substrate benchmark remains benchmark-positive but physiologically unproven. A within-host localization effect may nominate a topology for that host; a cross-host rank does not. No serum-urate, dose, production, or chassis conclusion is allowed from this assay.

### 1.34 Isotope-Resolved Dietary Precursor → UOX → PDB Sequential Flux

**Status:** Proposed — two-stage feasibility gate | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [purine-degrading bacteria](./purine-degrading-bacteria.md), [purine load](./purine-load-koji-vs-yeast.md), [gut-lumen sink](./gut-lumen-sink.md)

**What it tests:** Whether whole-cell GR-5 retains dietary purine atoms rather than merely converting nucleosides to absorbable bases, and whether residual urate transfers from a microoxic UOX compartment into an active anoxic PDB compartment.

**Computational prior:** [comp-046](./staged-purine-sink-mass-balance-computational.md) shows that these are separate conditional hypotheses. GR-5 primary evidence is a purine-nucleoside/oxonate mouse model ([Ji et al. 2025](https://www.nature.com/articles/s41538-025-00556-y)); DeoD cleavage itself is not purine-ring destruction.

**Protocol:** First assay actual engineered yeast and koji biomass for adenine, guanine, hypoxanthine, xanthine, and urate using the USDA/NIH-compatible HPLC-MS approach. Then expose isotope-labeled adenosine/inosine/guanosine to control or GR-5 in simulated digestion followed by an intestinal Transwell; quantify nucleosides, free bases, microbial-biomass incorporation, and apical/basolateral isotope flux. Separately route isotope-labeled urate through a microoxic UOX reactor followed by an anoxic PDB reactor; measure residual urate, allantoin or oxidative products, yanthine/UMH/albizziin/pyruvate, and viability.

**Analyte nomenclature:** `yanthine` is intentional, not a misspelling of xanthine. Li et al. use it for 2,8-dioxopurine, the first reported reductive-pathway intermediate, and distinguish it from xanthine (2,6-dioxopurine) ([Life Metabolism 2025, DOI 10.1093/lifemeta/loaf031](https://doi.org/10.1093/lifemeta/loaf031)).

**Decision rule:** Advance the upstream stage only if isotope mass balance shows lower basolateral purine transfer plus recoverable microbial or unabsorbed retention. Advance staging only if PDB removes transferred residual urate without loss of viability and without unaccounted isotope. Nucleoside disappearance alone does not pass.

### 1.35 Enterocyte NLRP3–PDZK1–ABCG2 Tissue-Paradox Assay

**Status:** Proposed | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [NLRP3 exploit map](./nlrp3-exploit-map.md), [ABCG2 modulators](./abcg2-modulators.md), [gut-lumen sink](./gut-lumen-sink.md)

**What it tests:** Whether candidate NLRP3 inhibitors suppress intestinal PDZK1/ABCG2 trafficking or transepithelial urate export while reducing inflammatory signaling. The direct prior is human intestinal-cell work ([Chen et al. 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5803867/)); acute-gout compensation is supported by human/mouse/Caco-2 work ([PMID 37042723](https://pubmed.ncbi.nlm.nih.gov/37042723/)).

**Protocol:** Polarized human ileal and colonic enteroid Transwells; basolateral urate ± the project's lead NLRP3 inhibitors, with vehicle, inactive analogue where available, and matched viability controls. Measure PDZK1, total and surface ABCG2, basolateral-to-apical urate flux, IL-1β pathway readouts, and barrier integrity. Add FXR-agonist or butyrate rescue arms only after the inhibitor effect is established.

**Decision rule:** A flare-suppressive candidate that reproducibly reduces functional urate export is not a neutral gut-axis intervention; it requires tissue-selective delivery or an independently validated epithelial rescue. Surface localization without urate flux does not pass.

### 1.36 Luminal Urate Antioxidant-Loss × UOX-H2O2 Safety Assay

**Status:** Proposed — safety gate | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [uricase](./uricase.md), [validation §1.12](#112-local-h2o2-stress-in-caco-2-from-the-selected-uox-configuration), [engineered koji protocol](./engineered-koji-protocol.md)

**What it tests:** The joint effect of removing luminal urate and generating H2O2, including the flare-treatment context of NSAID exposure. Animal/cell priors indicate luminal urate can protect against indomethacin enteropathy ([PMID 33569665](https://pubmed.ncbi.nlm.nih.gov/33569665/); [Yasutake et al. 2017](https://onlinelibrary.wiley.com/doi/10.1111/jgh.13785)); H2O2 can promote TXNIP–NLRP3 association ([PMID 20023662](https://pubmed.ncbi.nlm.nih.gov/20023662/)).

**Protocol:** Human enteroid monolayers with urate alone, active UOX, inactive UOX, UOX+compartment-matched catalase, and UOX+catalase+non-urate antioxidant or butyrate, each ±indomethacin. Match urate depletion across relevant arms. Measure TEER, viability, H2O2, lipid peroxidation, TXNIP–NLRP3 association, IL-1β, and epithelial oxygen consumption.

**Decision rule:** Catalase is insufficient if it lowers H2O2 but barrier injury persists when urate antioxidant capacity is removed. Any protective add-back must be demonstrated independently and cannot be inferred from antioxidant labels.

### 1.37 CBT2.0 Carbon Fate and PDB Self-Niche Test

**Status:** Proposed — required before any renewed UOX/PDB model | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [purine-degrading bacteria](./purine-degrading-bacteria.md), [invalidated comp-031](./dual-chassis-ecn-pdb-uricase-computational.md)

**What it tests:** What engineered EcN actually produces from urate, and whether a full-pathway butyrate-producing PDB creates a colonocyte-hypoxia persistence loop. The CBT2.0 paper establishes pathway products through pyruvate but not EcN butyrate ([PMCID PMC12507026](https://pmc.ncbi.nlm.nih.gov/articles/PMC12507026/)); wild-type EcN lacks detectable butyrate without an engineered pathway ([PMCID PMC7279287](https://pmc.ncbi.nlm.nih.gov/articles/PMC7279287/)).

**Protocol:** Anaerobic `[U-13C5]`-urate tracing in WT EcN, CBT2.0, full-pathway *C. sporogenes*, and a pathway-deficient control. Quantify all PDB intermediates plus pyruvate, D/L-lactate, acetate, succinate, ethanol, and butyrate. Only if an arm produces butyrate, move it into colonocyte co-culture and measure epithelial oxygen consumption, HIF stabilization, PPARγ dependence, and strain persistence. Byndloss et al. anchors the colonocyte-oxygen mechanism ([PMCID PMC5642957](https://pmc.ncbi.nlm.nih.gov/articles/PMC5642957/)).

**Decision rule:** No CBT2.0-derived butyrate/ABCG2 claim survives without isotope-resolved butyrate. D-lactate elevation is a safety flag because impaired D-lactate metabolism can associate with hyperuricemia/gout ([PMID 31638601](https://pubmed.ncbi.nlm.nih.gov/31638601/)).

### 1.38 T0SS UOX-OMV Gut-to-Systemic Bridge Assay

**Status:** Proposed — alternate-route gate | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [blood-barrier exploits](./blood-barrier-exploits.md), [delivery-route matrix](./delivery-route-matrix.md)

**What it tests:** Whether UOX-loaded EcN OMVs cross a human intestinal barrier model with retained activity without unacceptable barrier, endotoxin/TLR4, or peroxide effects. The route has mouse and ex-vivo human-serum precedent ([Nature Communications 2025](https://www.nature.com/articles/s41467-025-57153-6)); it is no longer a purely speculative delivery idea.

**Protocol:** Human enteroid Transwells with apical T0SS UOX-OMVs, matched inactive-UOX OMVs, free UOX, T1SS comparator, and vehicle. Measure basolateral OMV markers, UOX protein/activity, ex-vivo urate degradation, TEER, paracellular leakage, H2O2, endotoxin/TLR4 signaling, and cytokines. Do not infer safe systemic exposure from transport alone.

**Decision rule:** Advance only if basolateral active UOX is reproducible while barrier integrity and inflammatory readouts remain within matched inactive-OMV controls. This remains a systemic-UOX branch with immunogenicity and H2O2 liabilities.

### 1.39 Fructose × KHK × NOX × ABCG2 Human-Enteroid Test

**Status:** Proposed | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [fructose connection](./fructose-connection.md), [ABCG2 modulators](./abcg2-modulators.md)

**What it tests:** Whether fructose simultaneously depletes epithelial ATP through KHK and reduces functional ABCG2-mediated urate export through NOX/ROS-dependent loss of active transporter dimerization. Priors: rat ileum ([Kaneko et al. repository full text](https://eprints.lib.hokudai.ac.jp/repo/huscap/all/68654/)) and KHK-dependent enterocyte ATP depletion ([PMID 24177030](https://pubmed.ncbi.nlm.nih.gov/24177030/)).

**Protocol:** Polarized human ileal enteroids exposed to matched fructose or glucose across a pilot-tolerated concentration series, ±KHK inhibitor and ±NOX inhibitor. Measure ATP, ROS, nonreducing ABCG2 dimer/monomer state, surface ABCG2, functional urate flux, and viability.

**Decision rule:** The double-hit model passes only if fructose reduces flux and the KHK and NOX arms dissociate ATP loss from ABCG2 dimer/flux loss. A high-dose toxicity-only result does not pass.

### 1.40 CD39/CD73–Adenosine Gout-Resolution Time Course

**Status:** Proposed | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [gout pathophysiology](./gout-pathophysiology.md), [NLRP3 exploit map](./nlrp3-exploit-map.md), [medicinal-mushroom track](./medicinal-mushroom-complement-track.md)

**What it tests:** Whether shifting extracellular ATP toward AMP/adenosine accelerates resolution after MSU inflammasome activation, and whether ADA inhibition acts through purinergic resolution as well as precursor control. The direct acute-gout prior is Luo et al. 2024 ([PMID 38055119](https://pubmed.ncbi.nlm.nih.gov/38055119/)).

**Protocol:** Human macrophage LPS+MSU time course ±ATP, apyrase/CD39 augmentation, CD39 inhibition, ADA inhibition, and A2A-receptor antagonism. Sample ATP, ADP, AMP, adenosine, inosine, IL-1β, cell death, and resolution markers before priming, during activation, and after washout.

**Decision rule:** A resolution mechanism requires time-ordered ATP loss, adenosine gain, and reduced inflammatory persistence that is reversed by receptor blockade. Systemic ADA inhibition is not implied by an in-vitro pass.

### 1.41 Parallel FXR–ABCG2 and TGR5–NLRP3 Bile-Acid Screen

**Status:** Proposed | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [ABCG2 modulators](./abcg2-modulators.md), [NLRP3 exploit map](./nlrp3-exploit-map.md), [open questions](./open-questions.md)

**What it tests:** Whether the same defined bile-acid or tool-ligand panel can increase intestinal ABCG2 urate flux through FXR and suppress macrophage NLRP3 through TGR5 without barrier toxicity. Priors: FXR/ABCG2 animal work ([DOI 10.1002/rai2.70039](https://onlinelibrary.wiley.com/doi/10.1002/rai2.70039)) and TGR5/PKA/NLRP3 mechanism ([Guo et al. 2016](https://www.sciencedirect.com/science/article/pii/S1074761316303521)).

**Protocol:** Run the same concentration-verified panel in human ileal enteroids and MSU-stimulated human macrophages. Enteroid readouts: FXR target engagement, surface ABCG2, urate flux, TEER. Macrophage readouts: TGR5/cAMP/PKA engagement, NLRP3 phosphorylation/ubiquitination, IL-1β, viability. Include receptor-selective antagonists or knockdown to assign mechanism.

**Decision rule:** Promote only ligands with receptor-dependent activity in both assays and no enteroid barrier injury. FXR-only and TGR5-only hits remain single-node tools rather than failed dual hits.

### 1.42 Succinate Compartment-Dissociation: Hepatic AMPD2 vs. Immune SUCNR1

**Status:** Proposed | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [TCM gout compound triage](./tcm-gout-compound-triage-computational.md), [gout pathophysiology](./gout-pathophysiology.md), [NLRP3 exploit map](./nlrp3-exploit-map.md)

**What it tests:** Whether succinate exposure can reduce hepatic purine production through AMPD2 while amplifying macrophage inflammation through SUCNR1, making compartment and exposure—not metabolite name—the decision variable. Priors: *B. fragilis*/berberine gut–liver work ([PMCID PMC12541614](https://pmc.ncbi.nlm.nih.gov/articles/PMC12541614/)), gout fecal metabolomics ([PMCID PMC5318445](https://pmc.ncbi.nlm.nih.gov/articles/PMC5318445/)), and SUCNR1 arthritis biology ([PMID 27481132](https://pubmed.ncbi.nlm.nih.gov/27481132/)).

**Protocol:** Establish a measured succinate exposure range first. In hepatocytes, quantify AMPD2 activity and AMP→IMP→inosine→hypoxanthine→xanthine→urate flux. In MSU-stimulated macrophages, quantify SUCNR1 dependence, HIF-1α, IL-1β, and viability at the same exposures. Keep fecal, portal, plasma, and joint exposure claims separate.

**Decision rule:** A useful window requires AMPD2-pathway suppression at exposures below those that amplify SUCNR1 inflammatory signaling. If the windows overlap, producer- or compartment-targeted delivery becomes mandatory.

### 1.43 PDB × Allopurinol/Oxypurinol/Febuxostat Interaction Assay

**Status:** Proposed | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [purine-degrading bacteria](./purine-degrading-bacteria.md), [gout deep dive](./gout-deep-dive.md)

**What it tests:** Whether standard XOR inhibitors suppress the reductive bacterial purine-degradation entry enzyme or remove the urate-derived fitness advantage needed for persistence. A selenium-containing XDH-family enzyme from *Eubacterium barkeri* was inhibited by allopurinol in vitro, but transfer to modern *C. sporogenes* PDB and physiological gut exposure is unknown ([Schräder et al. 1999](https://doi.org/10.1046/j.1432-1327.1999.00678.x)).

**Protocol:** First measure or obtain defensible human intestinal/fecal exposure distributions for allopurinol, oxypurinol, and febuxostat. Then run anaerobic dose–response studies in full-pathway *C. sporogenes*, CBT2.0, and pathway-deficient controls at those observed concentrations. Measure growth, urate disappearance, every pathway intermediate/product, and enzyme activity where isolatable.

**Decision rule:** Claim additivity with XOR inhibitors only if no pathway inhibition or persistence loss occurs across measured intestinal exposures. A millimolar in-vitro effect outside human exposure does not fail the combination.

---

### 1.44 Thymulin × MSU × NLRP3 in Aged Macrophages (THY-1) — Age-Stratified Priming-to-Flare Test

**Status**: Proposed | **Cost**: Tier 1: $5–10K; full T1+T2+T3 cascade $85–130K | **Weeks**: Tier 1: 6–8; full cascade ~11 months | **Phase**: 1

**Affected wiki**: [thymulin](./thymulin.md), [nlrp3-inflammasome](./nlrp3-inflammasome.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) §CP1a, [peptide-gout-addendum](./peptide-gout-addendum.md)

**What it tests:** Whether thymulin's demonstrated NF-κB priming block (Signal 1) translates into reduced **MSU-crystal-driven** mature IL-1β and caspase-1 activation in macrophages — i.e. whether suppressing the transcriptional priming arm is sufficient to blunt a crystal-triggered flare, or whether the untested assembly/caspase-1 steps (CP2–CP4) proceed regardless. Kanemaru et al. 2026 (*Nat Commun* 17:6534, [DOI 10.1038/s41467-026-75383-0](https://doi.org/10.1038/s41467-026-75383-0)) established, in aged bone-marrow macrophages and human PBMCs, that thymulin inhibits NF-κB p65 DNA-binding and IκBα phosphorylation and suppresses IL-1α/IL-1β/IL-6/TNF-α — but every stimulus was LPS or the aging state, never a urate crystal, and every readout was priming-level, never crystal-driven mature IL-1β secretion. This experiment supplies the missing MSU trigger and the assembly/output readouts.

**The design pivot vs. §1.23:** thymulin's anti-inflammatory effect is **age-dependent** (present in aged cells, essentially absent in young; Kanemaru 2026). Cell/donor age is therefore the primary experimental variable here, not a nuisance covariate. A protocol run only in a standard (effectively "young"-phenotype) immortalized line could return a false null. Every tier is age-stratified.

**Background on the gap:** No thymulin × MSU-crystal experiment exists in the indexed literature (2026-07 lit review, [thymulin.md](./thymulin.md)). The 2026 paper's framing is inflammaging and cancer immunotherapy; the gout-relevant CP1a mechanism is a spin-out from that work. Both halves are otherwise well-characterized — MSU × macrophage NLRP3 is textbook, and thymulin × NF-κB is now directly measured — so the assays are standard; only the intersection is new.

**Protocol — Tiered, gating logic:**

**Tier 1 — Age-contrasted macrophage in vitro screen ($5,000–10,000; 6–8 weeks):**
- **Cells (age contrast is the core comparison):**
  - *Aged-phenotype arm:* primary human monocyte-derived macrophages (MDMs) from older donors (≥60 yr), OR replicatively/inflammatory-aged THP-1 macrophages (extended PMA + serial passage) as a lower-cost proxy. The aged arm is where a thymulin effect is predicted.
  - *Young-phenotype arm:* MDMs from young donors (≤35 yr), OR standard-passage PMA-differentiated THP-1. Predicted near-null — this arm tests the age-dependence, not just efficacy.
- **Pre-treatment:** ± thymulin acetate at 0.1, 1, 10, 100 nM, **each co-administered with equimolar ZnCl₂** (zinc is obligatory for activity; a zinc-only vehicle arm is the matched control, mirroring the Kanemaru in vivo control) × 24 hr.
- **Priming + challenge:** LPS prime (signal 1) followed by **MSU crystals (100–200 μg/mL, 4–6 hr)** as the gout-relevant activation trigger. Include an LPS+ATP (5 mM, 30 min) arm as an orthogonal non-crystal NLRP3 trigger, and an LPS-only (no crystal) arm to separate priming suppression from assembly effects.
- **Readouts:**
  - **Mature secreted IL-1β (ELISA) — primary endpoint** (this is the crystal-driven output the 2026 paper never measured).
  - Cleaved caspase-1 (p20, Western) — tests whether the effect reaches the assembly/executioner step or stops at priming.
  - ASC speck formation (immunofluorescence, % speck-positive cells).
  - NF-κB priming confirmation: pro-IL-1β + NLRP3 mRNA (qPCR) and IκBα phosphorylation (Western) — replicates the Kanemaru priming readout in the MSU context and anchors the mechanism.
  - IL-1α, IL-6, TNF-α (multiplex) — the broader cytokine set thymulin suppressed.
  - Pyroptosis (LDH release).
- **Success criterion (Tier 1 → Tier 2):** ≥30% suppression of MSU-induced mature IL-1β by thymulin in the **aged** arm at any concentration, with a demonstrably smaller effect in the young arm (age-dependence preserved). Interpretation branches:
  - *IL-1β down AND caspase-1/ASC down:* priming suppression propagates to the output — strongest result; thymulin blunts the crystal flare, not just transcription.
  - *IL-1β down but caspase-1/ASC unchanged:* priming reduction lowers substrate without blocking assembly — a partial, mechanistically bounded effect.
  - *pro-IL-1β/NLRP3 mRNA down but mature IL-1β unchanged:* the priming-only limitation is confirmed — thymulin does not blunt crystal-driven output. Closes the flare hypothesis; thymulin remains a systemic-immunomodulation entry only.
  - *No effect even on priming in the aged arm:* fails to replicate the 2026 mechanism under an MSU (vs. LPS) trigger; closes the question.

**Tier 2 — Donor-age-stratified primary MDMs, expanded n ($20,000–30,000; 12 weeks; gated on Tier 1 positive):**
- **Cells:** MDMs from older donors (≥60 yr, n=8) vs. young donors (≤35 yr, n=8); if a serum thymulin/zinc-status assay is feasible, stratify the aged arm further by endogenous thymulin activity.
- **Same thymulin (+Zn²⁺) × LPS+MSU protocol as Tier 1.**
- **Readouts:** mature IL-1β + IL-18 (gout-relevant cytokines); caspase-1; donor-age effect size.
- **Success criterion (Tier 2 → Tier 3):** aged-donor MDMs show MSU-IL-1β suppression matching the Tier 1 direction with effect size ≥20%, and the young-donor arm confirms the age gap. Positive Tier 1 + null Tier 2 indicates an immortalized-line artifact and is itself useful (closes escalation).
- **Ethics note:** donor recruitment and consent through standard IRB-approved protocols.

**Tier 3 — Aged-mouse MSU air-pouch ± thymulin ($60,000–90,000; 6 months; gated on Tier 2 confirmation):**
- **Animals:** aged (≥18-mo) vs. young (2–3-mo) C57BL/6 mice; arms: vehicle (ZnCl₂ only), thymulin + ZnCl₂ (1.5 mg/kg + equimolar ZnCl₂ i.p. daily, the Kanemaru regimen), across both age groups.
- **Standard gout model:** subcutaneous air pouch raised over 6 days; MSU crystal injection (3 mg in PBS); 6-hr and 24-hr lavage.
- **Readouts:** lavage neutrophil count (primary — standard gout-model readout); IL-1β + cascade (IL-6, CXCL1/KC); pouch-tissue NLRP3/ASC/caspase-1 (Western).
- **Success criterion:** causal demonstration that thymulin reconstitution reduces MSU-induced gouty inflammation specifically in aged animals, with a quantified effect size. This is the in vivo test of the age-dependent-repurposing thesis.

**BHB / KPV comparison arm (marginal add to Tier 1):** run thymulin head-to-head against KPV (the other CP1a peptide) and against BHB on the same aged-macrophage MSU plate. **What it adds:** thymulin, KPV, and BHB all touch CP1; whether they are additive (distinct routes into NF-κB / assembly) or redundant is untested, and the aged-cell context is exactly where thymulin is predicted to differentiate. Primary readout: MSU-induced IL-1β with single agents vs. pairs (Loewe combination index, CI <0.7 super-additive). Near-zero marginal cost (added arms on the existing plate).

**Estimated cost (full cascade):** Tier 1 $5–10K → +Tier 2 $20–30K → +Tier 3 $60–90K = **$85–130K total** if all tiers fire. Tier 1 alone is the entry cost.

**Estimated timeline (full cascade):** Tier 1: 6–8 weeks. + Tier 2: +12 weeks (gated). + Tier 3: +6 months (gated). Best case (early null): 8 weeks. Worst case (full cascade): ~11 months.

**Success criteria (overall):**
- **Crystal-driven output suppression, age-dependent (positive T1+T2+T3):** thymulin graduates from a CP1a mechanistic-extrapolation entry to a gout-validated priming inhibitor with an age-targeted use case. Updates [thymulin.md](./thymulin.md), the [exploit map CP1a](./nlrp3-exploit-map.md) evidence tier, and the age-demographic framing.
- **Priming-only confirmed (mRNA down, mature IL-1β unchanged):** the untested-assembly limitation becomes a measured limitation; thymulin stays a systemic-immunomodulation hypothesis, not a flare intervention. Publishable gap-fill.
- **Age-dependence not preserved (equal effect young + aged, or effect only young):** contradicts the 2026 mechanism under an MSU trigger; flags the age-dependent-repurposing thesis for revision.

**Limitations:**
- Tier 1's "aged-phenotype" immortalized-line proxy is an approximation of true replicative/inflammatory aging; the primary-MDM arm (Tier 1 optional / Tier 2) is the real age test.
- Zinc co-administration is obligatory and must be matched in every control — an apparent thymulin effect that is actually a zinc effect is the key confound (the zinc-only vehicle arm controls for it).
- Tiers focus on priming + activation + output; they do not address resolution (SPM) or T-cell/systemic immunomodulation — the latter is thymulin's other documented axis and a separate safety question for any gout use.
- The murine air-pouch model is acute, not chronic-tophaceous.

**Cross-references:** [thymulin.md](./thymulin.md) (dossier + falsification gate); [nlrp3-exploit-map.md §CP1a](./nlrp3-exploit-map.md); [nlrp3-inflammasome.md](./nlrp3-inflammasome.md); §1.23 (androgen × MSU × NLRP3, shared assay family); §1.17 (MSU-macrophage synergy readouts).

---

## Phase 2: Animal Model Validation

<a id="21-selected-uox-configuration-in-vivo-persistence-and-localization"></a>
### 2.1 Selected UOX Configuration: In-Vivo Persistence and Localization

**Status**: Proposed — gated | **Cost**: TBD after model selection | **Weeks**: TBD | **Phase**: 2

**Affected wiki**: [gut-lumen-sink](./gut-lumen-sink.md), [uricase](./uricase.md), [team](./etc/team.md)

**What it tests:** Whether the UOX configuration that passes §1.33 and §1.36 reaches its intended reaction compartment in vivo with retained activity, measurable product formation, and acceptable local safety. The topology, chassis, product matrix, species, and model are not chosen in advance.


**Protocol:**
- Select the animal species and model only after the surviving configuration and remaining translational question are known.
- Compare the active selected configuration with matched inactive-UOX, vehicle, and matrix- or chassis-only controls where applicable.
- Derive the dose range and sampling schedule from measured §1.33 product formation and the exposure bounds that pass §1.36; do not back-calculate from an assumed serum-urate effect.
- Measure active UOX, urate and product in the intended reaction compartment, H₂O₂, localization, persistence across the intended exposure window, barrier and tissue safety, and systemic urate only as a secondary readout at this stage.
- Measure viable-organism counts only if the selected configuration uses a living chassis; CFU is not a universal UOX endpoint.

**Estimated cost:** TBD after configuration, species, model, and analytical plan are selected.

**Estimated timeline:** TBD after model selection.

**Dependencies:** 
- §1.33 must first advance the exact configuration on physiological-condition product formation and configuration-specific peroxide and viability readouts.
- §1.36 must then clear the selected configuration for animal escalation.
- Route-specific implementation and process tests are required only for the route carried forward.

**Success criteria:** 
- Demonstrate reproducible reaction-compartment target engagement and retained active UOX relative to matched inactive-UOX controls.
- Prespecify configuration-specific persistence and safety margins after pilot variance is measured.
- A null result redirects the configuration or dose design; it does not establish a chassis-wide or UOX-wide failure.

---

<a id="22-selected-oral-uox-configuration-in-vivo-efficacy-and-safety"></a>
### 2.2 Selected Oral UOX Configuration: In-Vivo Efficacy and Safety

**Status**: Proposed — gated | **Cost**: TBD after model selection | **Weeks**: TBD | **Phase**: 2

**Affected wiki**: [gut-lumen-sink](./gut-lumen-sink.md), [gout-deep-dive](./gout-deep-dive.md), [uricase](./uricase.md)

**What it tests:** Whether the selected oral UOX configuration produces a reproducible whole-organism urate effect with concordant reaction-compartment target engagement and acceptable safety.


**Protocol:**
- Select the species and hyperuricemia model for the mechanism and configuration that survive §2.1; do not default to a rat, mouse, yeast, or koji study.
- Use the active, inactive-UOX, vehicle, and route-matched controls from §2.1, with a model-appropriate positive control when it answers the prespecified question.
- Set dose levels from the §2.1 exposure and target-engagement data within the §1.36 safety bounds.
- Measure serum urate together with urinary and fecal urate and UOX products, reaction-compartment active UOX, H₂O₂ and barrier readouts, and kidney and systemic safety markers.

**Estimated cost:** TBD after configuration, species, model, and analytical plan are selected.

**Estimated timeline:** TBD after model selection.

**Dependencies:** §1.33 → §1.36 → §2.1. Route-specific process tests apply only to the selected configuration.

**Success criteria:** 
- Prespecify the systemic-effect and safety margins after §2.1 supplies exposure and variance estimates.
- Require a reproducible serum-urate response relative to matched controls together with concordant reaction-compartment target engagement and mass-balance readouts.
- Do not promote a configuration from serum urate alone when local activity, product formation, or safety is unresolved.

---

### 2.3 Engineered Koji Efficacy in Digestive Enzyme-Deficient Model

**Status**: Proposed | **Cost**: $6,000–10,000 | **Weeks**: 8–10 | **Phase**: 2

**Affected wiki**: [engineered-koji-protocol](./engineered-koji-protocol.md), [digestive-enzymes](./digestive-enzymes.md), [enzyme-deficit-deep-dive](./enzyme-deficit-deep-dive.md)

**What it tests:** Does engineered koji effectively supplement digestive enzymes in vivo?


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

**Status**: Proposed — configuration-specific extension | **Cost**: TBD after pilot and model selection | **Weeks**: TBD | **Phase**: 2

**Affected wiki**: [gout-deep-dive](./gout-deep-dive.md), [gout-clinical-pipeline](./gout-clinical-pipeline.md), [gut-lumen-sink](./gut-lumen-sink.md)

**What it tests:** Whether an identity-verified PULSE/EcN configuration reproduces reaction-compartment target engagement in vivo and, only after that is shown, produces a whole-organism urate effect with acceptable safety. This does not test a generic probiotic topology.

**Entry and staging gate:** Acquire or reconstruct the exact PULSE/EcN strain, verify its sequence and biosensor behavior, and qualify it for the configuration-level §1.33 screen. That exact configuration must then pass §1.33 and §1.36 and establish in-vivo localization, target engagement, persistence, and exposure bounds under §2.1. A different configuration passing those gates does not authorize PULSE.

**Protocol:**
- Select the species and hyperuricemia model only after the surviving configuration and unresolved translational question are known; do not assume stable colonization or default to a Uox-knockout model.
- Use a pilot to measure persistence, biosensor response, target engagement, variance, and tolerable exposure. Derive sample size, dose range, schedule, and stopping rules from those data and the §1.36 safety bounds.
- Compare active PULSE with the exact inactive-UOX construct, biosensor/control construct, parental EcN, vehicle, and model-appropriate positive control.
- Measure reaction-compartment active UOX, urate and products, reporter state, organism abundance or clearance where relevant, H₂O₂, barrier and inflammatory safety, fecal and urinary urate mass balance, and serum urate as a later efficacy readout.
- Add an acute urate challenge only if it answers the prespecified biosensor-control question and the configuration has already cleared the steady-state safety stage.

**Estimated cost and timeline:** Determine after strain access, model selection, pilot variance, analytical endpoints, and containment requirements are fixed.

**Dependencies:** Exact strain access or bounded reconstruction; configuration characterization; §1.33 → §1.36 → §2.1. The efficacy/challenge portion is a route-specific application of §2.2 and cannot begin from strain availability alone.

**Decision rule:** Prespecify configuration-specific target-engagement, biosensor-response, systemic-effect, and safety margins from the pilot. Advance only if local activity and product formation agree with any serum effect and no new barrier, inflammatory, peroxide, persistence, or metabolite signal appears. A null or unsafe result applies to this configuration, not every UOX or probiotic route.

---

### 2.6 GLPP + Cordycepin Interaction in Hyperuricemia — Matched Wet-Lab Gate (Phase 7-4 Stub)

**Status**: Proposed — design pending exact material and pilot data | **Cost**: TBD | **Weeks**: TBD | **Phase**: 2

**Affected wiki**: [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [hypotheses/H06-medicinal-mushroom-complement-track](./hypotheses/H06-medicinal-mushroom-complement-track.md), [medicinal-mushroom-extract-sops](./medicinal-mushroom-extract-sops.md), [medicinal-mushroom-compound-mapping-computational](./medicinal-mushroom-compound-mapping-computational.md), [modality-chokepoint-matrix](./modality-chokepoint-matrix.md)

**What it tests:** Whether a compositionally verified *C. militaris* material, purified cordycepin, and defined GLPP or pentostatin combinations differ in cordycepin exposure, urate handling, and safety in a model chosen for that question. Native co-production does not establish a fixed cordycepin:pentostatin exposure or a beneficial interaction.

**Why this matters:** The track currently combines results from different materials and studies. A matched experiment can determine whether the materials reproduce individually and whether an interaction remains after identity, exposure, and assay variance are controlled.

**Entry requirements:**
- Verify the exact GLPP fraction, source organism, extraction, and primary-study dose before using its reported effect as a planning prior.
- Quantify cordycepin and pentostatin in the proposed whole material and verify the identity and purity of every isolated material.
- Select species and hyperuricemia model only after the mechanism and comparator question are frozen.
- Run a tolerability/PK and endpoint-variance pilot; use it to set exposure levels, sample size, schedule, and stopping rules.

**Candidate matched design:** Include the verified whole material, exposure-matched purified cordycepin, purified cordycepin plus the exact GLPP fraction, and purified cordycepin plus pentostatin only if the latter arm is justified and safely accessible. Add vehicle, healthy or disease controls, and single-agent GLPP where needed to identify the interaction. Measure cordycepin and 3'-deoxyinosine PK, ADA activity, serum/urinary/fecal urate, transporter protein and functional readouts, material-specific exposure markers, and hepatic, renal, weight, and clinical safety. The final arm count follows the estimand and pilot, not the inherited four-arm label.

**Estimated cost and timeline:** Determine after material identity, arm count, model, sample size, PK schedule, and analytical plan are fixed.

**Dependencies:** Operational material-identity and fractionation methods; primary-source verification of the exact comparators; qualified analytical methods; preclinical oversight; and a pilot that supplies variance and safety bounds. Pentostatin is optional, not a required arm.

**Decision rule:** Prespecify the individual-material replication margin, interaction estimand, PK margin, and safety limits after the pilot. Advance a combination only if its effect exceeds the prespecified additive expectation or achieves the same biological effect at lower verified exposure without a new safety signal. A null interaction keeps the materials separate; failure of an individual material narrows that material-specific hypothesis rather than the whole Open Enzyme portfolio.

**Cross-references:** [medicinal-mushroom-complement-track.md](./medicinal-mushroom-complement-track.md) (parent scope); [H06](./hypotheses/H06-medicinal-mushroom-complement-track.md) Dimension 3; [SOP-1](./medicinal-mushroom-extract-sops.md) (material-identity dependency); and the [comp-014 evidence files](./medicinal-mushroom-compound-mapping-computational.md).

#### Phase 7-4b follow-up — UOX × mushroom interaction arm (queued, gated on §2.6 and the UOX safety chain)

**Status**: Queued (gated on §2.6 base-study success and §§1.33, 1.36, and 2.1 for the exact UOX configuration) | **Cost and duration:** TBD from the final model, arm count, variance, and analytical plan

**What it tests:** whether a mushroom-track intervention and an independently cleared luminal-UOX configuration interact additively, antagonistically, or not detectably in the selected animal model. The §2.6 base study tests cordycepin × GLPP × pentostatin within the medicinal-mushroom track only; it does not establish how a separate UOX mechanism will compose.

**Why this matters:** coverage of different nodes does not establish that two interventions compose favorably. A direct interaction study can determine whether later work should test the tracks together or keep them independent. It cannot authorize a consumer product or a human combination recommendation.

**Sequencing rationale:** Queue this follow-up behind two independent prerequisites: §2.6 must establish a mushroom arm worth extending, and the exact UOX-only koji configuration must be built in §1.5, pass §1.33, reproduce in §1.9B, clear §1.36, and complete §2.1. This preserves attribution and prevents animal use of an uncleared UOX configuration.

**Proposed protocol (stub-level, fires only after both prerequisite chains pass):**
- **Combination arm:** the prespecified advancing arm from §2.6 plus the §1.5-built, §1.33-advanced, §1.9B-reproduced, §1.36-cleared, and §2.1-characterized UOX-only koji configuration. Match route and measured exposure to the individual-arm studies. Do not use Huynh 2020 antibody production as a uricase-activity baseline.
- **Sample size:** set prospectively from the §2.6 and §2.1 variance estimates and the smallest interaction effect worth detecting; do not inherit `n=8` as a power claim.
- **Model, schedule, and shared readouts:** use the model, exposure window, sampling schedule, and core endpoints qualified by the completed §2.6 and §2.1 studies. Freeze them before randomization; do not inherit the old PO+HX, day-14, or transporter-mRNA settings unless those exact choices remain justified for both arms.
- **Additional readouts:** fecal urate and downstream products, urinary urate, serum urate time course, and delivered UOX activity, so a change can be localized rather than assigned automatically to a gut-lumen sink.

**Decision rule:** Prespecify the additive null and confidence interval after the individual-arm effects and variance are measured. Advance the combination only if the interaction estimate is compatible with a useful incremental effect and no new safety signal. A null, antagonistic, or unsafe interaction keeps the tracks separate. Do not infer mechanism from serum urate alone.

**Decision gate to fire this follow-up:** Both conditions are required: (1) §2.6 identifies an advancing material under its pilot-informed replication, interaction, and safety rule; and (2) the exact UOX-only koji configuration completes §1.5 → §1.33 → §1.9B → §1.36 → §2.1. Failure or incompleteness of either chain keeps the combination study closed.

**Limitations:**
- Engineered-koji UOX readiness requires an exact §1.5-built configuration to pass §1.33, reproduce in the §1.9B solid-state context, clear §1.36, and be characterized under §2.1. The lactoferrin cassette and §1.9C dual-cassette result are not required for a UOX-only combination arm. If that sequence is incomplete when §2.6 concludes, Phase 7-4b waits; a surrogate must independently clear the same configuration-specific gates before use. No Huynh 2020 “koji-uricase strain” precedent is assumed.
- The final exposure window may still answer only an acute interaction question; chronic durability requires a separate design.
- Model and strain consistency with the qualifying individual-arm studies must be maintained; do not use cross-cohort comparisons as an interaction estimate.

**Cross-references:** [gout-pathophysiology.md §"Multi-track urate transporter coverage"](./gout-pathophysiology.md) (the coverage map this follow-up tests); §2.6 base (parent study); [§1.33](#133-physiological-uox-topology--oxygen--peroxide-factorial) (configuration-level physiological gate); [§1.9](#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate) Stage B (solid-state UOX-only readiness); [§1.36](#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) (pre-animal safety gate); [§2.1](#21-selected-uox-configuration-in-vivo-persistence-and-localization) (configuration-specific in-vivo characterization); [`koji-endgame-strain.md`](./koji-endgame-strain.md) (koji track context).

### 2.7 Koji × *Cordyceps* Co-Formulation Stability Test — ADA-Challenge Assay — **Deprioritized 2026-05-16, archived 2026-05-29**

**Status**: Abandoned — recover from Git only if decision-relevant | **Cost**: N/A (archived) | **Weeks**: N/A (archived) | **Phase**: 2

This experiment is not active. Reconstruct it from Git only if the koji-cordycepin hypothesis becomes decision-relevant again.

---

## Phase 3: Observational and human-method development

Human observations in this section are feasibility signals, not treatment recommendations or efficacy evidence. Prospective intervention studies require appropriate oversight, established-care comparators, prespecified stopping rules, and a design capable of separating exposure from regression to the mean and background changes.

### 3.3 Wild-type fungal-enzyme timing study design

**Status**: Design only | **Cost**: TBD | **Weeks**: TBD | **Phase**: 3

**Affected wiki**: [digestive-enzymes](./digestive-enzymes.md) and [digestive-enzyme-optimization](./digestive-enzyme-optimization.md).

**What it can test:** Whether exposure timing changes measured gastrointestinal outcomes for a characterized wild-type fungal-enzyme preparation under a controlled study design. It cannot establish an EPI/SIBO treatment effect, transfer to an engineered organism, or validate a gout intervention.

**Design requirements if advanced:**
- Use a characterized preparation, an appropriate comparator, clinician-reviewed inclusion and exclusion criteria, and prespecified stopping rules.
- Select exposure levels and timing from product characterization, established-use boundaries, and safety review; do not derive them from an uncontrolled observation.
- Randomize or counterbalance timing where feasible and record meal composition, background care, concurrent exposures, and post-meal behavior as potential confounders.
- Prespecify validated symptom measures, stool frequency and consistency, a direct fat-absorption measure where relevant, adverse events, adherence, and the analysis plan.
- Use a pilot to estimate variance and determine sample size, duration, and meaningful-effect margins.
- Keep engineered organisms outside this study; they require separate preclinical, containment, and regulatory gates.

**Decision rule:** A controlled, reproducible timing effect can inform a larger study of that exact preparation. A null or unstable result does not support a timing claim. No result from this study establishes an engineered-platform mechanism or a reader-facing dose.

---

Uncontrolled observations may identify covariates, but they do not estimate efficacy, safety, or dose.


## Cross-Experiment Dependencies and Sequencing

```text
Phase 1: UOX decision path
1.1: payload screen or frozen baseline comparator
├─→ 1.2: matched yeast configuration build + characterization
├─→ 1.5: matched koji configuration build + characterization
└─→ exact external configuration acquisition/reconstruction (for example PULSE/EcN)

Qualified output from any configuration-supply branch
└─→ 1.33: configuration-level physiological UOX × oxygen × peroxide
     ├─→ within-host topology nomination only where construct variables are controlled
     ├─→ 1.3 / 1.4 / 1.6 / 1.15: route/process retention for an advanced configuration
     ├─→ 1.16: candidate-variant screen; any changed payload returns to 1.33
     └─→ 1.12 + 1.36: epithelial characterization and antioxidant-loss/H2O2 safety
          └─→ 2.1: exact-configuration in-vivo persistence/localization
               └─→ 2.2: exact-configuration in-vivo efficacy/safety
                    └─→ 2.5: PULSE-specific extension only if PULSE followed the same chain

Independent native-enzyme path
1.18: native koji free extract vs whole biomass ──→ native-enzyme delivery only

Other validation paths
1.7: NLRP3 pathway validation ──→ 2.4: MSU arthritis model
2.3: EPI koji model ──→ 3.3

Human translation only after mechanism, exposure, safety, and relevant animal gates pass
```

---

## Success Metrics Summary

UOX promotion criteria are tied to matched controls and pilot-measured assay precision rather than fixed survival, expression, CFU, or serum-urate thresholds. Construct supply precedes §1.33; §1.33 advances exact configurations and may nominate topology only within a controlled host comparison; §1.36 gates animal escalation.

| Phase | Experiment | Primary Endpoint | Target Threshold |
|-------|-----------|------------------|------------------|
| 1 | Gene performance | Active UOX under matched construct conditions | Precision-aware reproducible difference; no topology or dose inference |
| 1 | Configuration supply (§§1.2, 1.5) | Sequence identity, localization, active UOX, viability, variance | Qualified material and matched controls for §1.33; no physiological inference |
| 1 | Physiological UOX system (§1.33) | Product formation at human-baseline substrate prior | Exact configuration reproducible vs. matched inactive-UOX control, with no prespecified H₂O₂ or viability penalty |
| 1 | Route-specific process retention (§§1.3, 1.4, 1.6, 1.15) | Retained active UOX and product formation | Pilot-derived reproducibility and noninferiority margins; no fixed survival fraction |
| 1 | Candidate UOX variants (§1.16) | Retained active UOX in the advanced configuration | Simplest candidate clearing prespecified precision-aware activity and safety margins; changed payload returns to §1.33 |
| 1 | UOX epithelial safety (§§1.12, 1.36) | Barrier, H₂O₂, antioxidant-loss, viability | §1.36 must pass before animal escalation |
| 1 | NLRP3 pathway | IL-1β reduction | >50% at stated doses |
| 2 | Selected UOX persistence/localization (§2.1) | Reaction-compartment active UOX and product formation | Configuration-specific margins prespecified from pilot variance; CFU only for a living chassis |
| 2 | Selected oral UOX efficacy/safety (§2.2) | Serum urate with concordant local target engagement and mass balance | Prespecified after §2.1; no fixed SUA threshold or chassis assumption |
| 2 | Koji EPI model | Fat absorption | >92% (vs. <50% baseline) |
| 2 | MSU arthritis | Joint swelling reduction | ≥40% vs. vehicle |
| 2 | PULSE configuration (§2.5) | Local target engagement, biosensor response, mass balance, systemic effect, and safety | Pilot-informed configuration-specific margins; no fixed serum target or colonization assumption |
| 1 | EGCG CP1a (1.8) | IL-6 suppression at ≤1 μM EGCG | ≥50% |
| 1 | Carnosine co-expression (1.24) | Carnosine titer in koji pore fluid | ≥500 mg/L (promote); <100 mg/L (de-prioritize koji track) |

---

## Notes on Open Questions

- **GLUT9 and urate transport bottleneck:** Could engineered koji produce high fructokinase inhibitors to address the fructose-gout link? (Source: gout-deep-dive.md, Section 9)
- **Delivery route optimization:** Is intestinal lumen degradation sufficient, or would systemic absorption of recombinant uricase be superior? (Source: blood-barrier-exploits.md)
- **Microbiome stability:** Will engineered probiotics persist without colonization, or is daily dosing required long-term? (Source: gout-deep-dive.md, Section 8)
- **Gene therapy as alternative:** Should we pursue CRISPR-based uricase gene therapy in parallel? (Source: gout-deep-dive.md, Section 6)

---

*Research protocols only. Human translation requires appropriate oversight and cannot be inferred from computational, cell, animal, or n=1 results.*
