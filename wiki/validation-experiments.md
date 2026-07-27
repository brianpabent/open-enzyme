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
| [§1.10](#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) | Uricase + lactoferrin stability in shio-koji ferment (gates dual-use thesis for both payloads) | In Vitro | $520–900 core reagents; condition matrix, oligomer assay, and microbial QC TBD | 3–4 | Proposed — UOX decision after §1.33 | [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [lactoferrin](./lactoferrin.md), [synthesis/](../synthesis/README.md) |
| [§1.11](#111-ergothioneine--abcg2-expression-and-function-in-caco-2) | Ergothioneine → ABCG2 expression and function in Caco-2 | In Vitro | $1,000–1,500 | 3–4 | Proposed — source and exposure qualification required | [abcg2-modulators](./abcg2-modulators.md), [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.12](#112-local-h2o2-stress-in-caco-2-from-the-selected-uox-configuration) | Selected-UOX epithelial H₂O₂ characterization | In Vitro | $800–1,200 | 2–3 | Proposed — after §1.33 | [uricase](./uricase.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.13](#113-limonene-abcg2-induction-in-caco-2-tier-3-stack-synergy-test) | Limonene → ABCG2 Caco-2 (Tier-3 stack synergy) | In Vitro | $800–1,200 | 3–4 | Proposed | [supplements-stack](./supplements-stack.md), [abcg2-modulators](./abcg2-modulators.md), [cannabinoids-terpenes](./cannabinoids-terpenes.md) |
| [§1.14](#114-abcg2-response-to-dht-and-tnf-with-butyrate-and-lactoferrin-rescue) | Direction-finding DHT × TNFα ABCG2 factorial + butyrate/lactoferrin response + supplement interaction/urate-flux gate + Q141K arm | In Vitro | TBD | 4–6 | Proposed | [abcg2-modulators](./abcg2-modulators.md), [androgen-urate-axis](./androgen-urate-axis.md), [gut-lumen-sink](./gut-lumen-sink.md), [lactoferrin](./lactoferrin.md), [supplements-stack](./supplements-stack.md), [koji-endgame-strain](./koji-endgame-strain.md) |
| [§1.15](#115-rice-bran-substrate-koji-uricase-gi-survival) | Matrix comparison for the selected koji UOX configuration | In Vitro | $800–1,200 | 3 | Proposed — after §§1.33 and 1.5 | [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.16](#116-candidate-uox-variants-in-koji-sequential-retained-activity-screen) | Candidate UOX variants in an advanced koji configuration | In Vitro | TBD | TBD | Proposed — after §§1.5 and 1.33 | [engineered-koji-protocol](./engineered-koji-protocol.md), [uricase-variant-selection](./uricase-variant-selection.md), [protein-engineering-strategy](./protein-engineering-strategy.md) |
| [§1.17](#117-quercetin-ursolic-acid-carnosine-three-way-synergy-on-msu-stimulated-thp-1) | Quercetin × ursolic × carnosine 3-way synergy (THP-1 MSU) | In Vitro | $1,500–2,000 | 3–4 | Proposed | [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md), [carnosine](./carnosine.md) |
| [§1.18](#118-native-koji-enzyme-sgf-survival-free-extract-vs-whole-biomass-2-arm) | Native koji enzyme SGF (free extract vs. whole biomass) | In Vitro | $300–500 | 2 | Proposed | [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [gi-survival-prediction](./gi-survival-prediction.md) |
| [§1.19](#119-methodological-standard-rodent-cellular-ic50-translation-caveat) | Methodology — rodent cellular IC50 translation caveat | Standing | $0 | ongoing | Standing | [chembl-cross-check](./etc/chembl-cross-check.md), [nlrp3-inhibitor-screen](./nlrp3-inhibitor-screen.md), [supplements-stack](./supplements-stack.md) |
| [§1.20](#120-lactoferrin-egcg-cp1a-super-additivity-assay-thp-1-macrophage-33-full-factorial--prespecified-midpoint) | Lactoferrin + EGCG CP1a interaction (THP-1 3×3 full factorial + prespecified midpoint); recombinant Lf can run now | In Vitro | $1,500 | 3–4 | Proposed | [lactoferrin](./lactoferrin.md), [egcg](./egcg.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [supplements-stack](./supplements-stack.md), [koji-endgame-strain](./koji-endgame-strain.md) |
| [§1.21](#121-natural-product-c5ar1-antagonist-screening--historical-computational-pass) | Natural-product C5aR1 antagonist screen — historical bounded query | Computational | $0 | 0.5 | Historical bounded no-hit; class remains open | [complement-c5a-gout](./complement-c5a-gout.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [open-enzyme-vision](./etc/open-enzyme-vision.md) |
| [§1.22](#122-gut-compartment-hdac-directed-candidate-screen-for-q141k-abcg2-trafficking-rescue) | Direct gut-compartment test of HDAC-directed candidates for Q141K-ABCG2 trafficking rescue | In Vitro | TBD | TBD | Proposed | [abcg2-modulators](./abcg2-modulators.md), [gut-lumen-sink](./gut-lumen-sink.md) |
| [§1.23](#123-androgen-msu-nlrp3-in-macrophages-tiered-mechanistic-protocol) | Androgen × MSU × NLRP3 macrophage tiered protocol (T1 THP-1 / T2 PBMC / T3 mouse air-pouch) — fills literature gap | In Vitro | Tier 1: $5–10K; full T1+T2+T3 cascade $105–160K | Tier 1: 6–8; full cascade ~12 months | Proposed | [androgen-urate-axis](./androgen-urate-axis.md), [nlrp3-inflammasome](./nlrp3-inflammasome.md) |
| [§1.24](#124-carnosine-co-expression-validation-in-a-oryzae-koji-endgame-optional-third-cassette) | Carnosine co-expression in *A. oryzae* (koji multi-payload optional third cassette) | In Vitro | $1,500–2,500 | 4–6 | Proposed | [koji-endgame-strain](./koji-endgame-strain.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [carnosine](./carnosine.md), [androgen-urate-axis](./androgen-urate-axis.md) |
| [§1.25](#125-dafcd55-scr1-4-truncated-single-cassette-expression-in-a-oryzae-cp0-engineering-candidate-wet-lab-gate) | DAF SCR1-4 route × host single-cassette comparison in *A. oryzae* (CP0 candidate + matched chaperone-conjecture test) | In Vitro | TBD after route-factorial and disulfide-mapping quotes | TBD | Proposed | [daf-cd55-scr14-truncated-computational](./daf-cd55-scr14-truncated-computational.md), [hypotheses/H05-daf-scr14-cp0-thesis](./hypotheses/H05-daf-scr14-cp0-thesis.md), [chaperone-orthogonal-stacking](./chaperone-orthogonal-stacking.md), [complement-c5a-gout](./complement-c5a-gout.md) |
| [§1.26](#126-ada-driven-cordycepin-loss--exact-material-interaction-screen) | ADA-driven cordycepin loss across exact materials and controls | In Vitro | TBD after pilot | TBD | Proposed — pilot design required | [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [gout-pathophysiology](./gout-pathophysiology.md) |
| [§1.27](#127-ergothioneine--lactoferrin-interaction-assay-in-msu-stimulated-thp-1-macrophages) | Ergothioneine × lactoferrin interaction in MSU-stimulated THP-1 macrophages | In Vitro | TBD | TBD | Proposed | [lactoferrin](./lactoferrin.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) |
| [§1.28](#128-tier-2-colorimetric-cordycepin-assay-validation) | Tier 2 colorimetric cordycepin assay validation | In Vitro | ~$200 | 2 | Proposed | [quantification-ladder](./quantification-ladder.md), [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md) |
| [§1.29](#129-cordycepin--pentostatin--substrate-matrix) | Cordycepin × pentostatin exact-configuration medium effects | In Vitro | TBD | TBD | Proposed — pilot design required | [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [medicinal-mushroom-extract-sops](./medicinal-mushroom-extract-sops.md) |
| [§1.30](#130-houttuynia-cordata-polysaccharide-fraction-comparison-in-msu-stimulated-thp-1-macrophages--prioritization-screen) | *Houttuynia cordata* polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages | In Vitro | TBD | TBD | Proposed — material and assay pilots required | [Houttuynia](./houttuynia-cordata.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) |
| [§1.31](#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms) | Butyrate culture-supernatant HPLC-UV method transfer against GC-MS | In Vitro | TBD | TBD | Proposed — partner design required | [tier-2-butyrate-assay-audit-computational](./tier-2-butyrate-assay-audit-computational.md), [quantification-ladder](./quantification-ladder.md) |
| [§1.32](#132-gsdmd-pore-self-delivery--matched-uptake-and-selectivity-probe) | GSDMD-pore matched uptake and selectivity probe | In Vitro | ~$2,000–5,000 | 4–6 | Proposed (wet-lab gated) | [gsdmd-pore-delivery-paradox](./gsdmd-pore-delivery-paradox.md), [kpv-gsdmd-pore-influx-computational](./kpv-gsdmd-pore-influx-computational.md) |
| [§1.44](#144-thymulin--msu--nlrp3-in-aged-macrophages-thy-1--age-stratified-priming-to-flare-test) | Thymulin (+Zn²⁺) × MSU × NLRP3 in **aged** macrophages (THY-1) — tests whether NF-κB priming block translates to reduced crystal-driven IL-1β; age-stratified | In Vitro | Tier 1: $5–10K; full T1+T2+T3 cascade $85–130K | Tier 1: 6–8; full cascade ~11 months | Proposed | [thymulin](./thymulin.md), [nlrp3-inflammasome](./nlrp3-inflammasome.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md), [peptide-gout-addendum](./peptide-gout-addendum.md) |
| [§1.45](#145-fecal-butyrate-electrochemicalann-reproducibility-and-transfer-gate) | Fecal butyrate electrochemical/ANN reproducibility and transfer | In Vitro method | TBD | TBD | Proposed — author package and partner design required | [tier-2-butyrate-assay-audit-computational](./tier-2-butyrate-assay-audit-computational.md), [quantification-ladder](./quantification-ladder.md), [open-questions](./open-questions.md) |
| [§1.46](#146-pth1r-agonist--abcg2-surface-trafficking-and-urate-flux) | PTH1R agonist → ABCG2 surface-trafficking and urate-flux test | In Vitro | TBD | TBD | Proposed — staged mechanism transfer | [abcg2-modulators](./abcg2-modulators.md), [open-questions](./open-questions.md) |
| [§1.47](#147-bempedoic-acid--oat2-urate-flux-attribution-and-rescue) | Bempedoic acid → OAT2 urate-flux attribution and rescue | In Vitro + human-data reanalysis | TBD | TBD | Proposed — human probe localization | [gout pathophysiology](./gout-pathophysiology.md), [open questions](./open-questions.md) |
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
| [§2.6](#26-glpp--cordycepin-interaction-in-hyperuricemia--matched-wet-lab-gate) | GLPP + cordycepin interaction in hyperuricemia — matched wet-lab gate | Animal | TBD | TBD | Proposed — design pending exact material and pilot data | [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md) |
| [§2.7](#27-koji--cordyceps-co-formulation-stability-test--ada-challenge-assay--deprioritized-2026-05-16-archived-2026-05-29) | Koji × *Cordyceps* co-formulation stability test | In Vitro | N/A (archived) | N/A (archived) | Abandoned — recover from Git only if decision-relevant | [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md) |
| [§2.8](#28-exact-material-androgen--urate-dual-axis-validation) | Exact-material androgen × urate dual-axis validation | Animal | TBD after material and exposure pilot | TBD | Proposed — one material/configuration per qualified study | [androgen-natural-modulation](./androgen-natural-modulation.md), [t-axis-adjuvant-urate-mapping-computational](./t-axis-adjuvant-urate-mapping-computational.md), [prps-purine-biosynthesis-chokepoint](./prps-purine-biosynthesis-chokepoint.md) |
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

**Secondary role — matched chaperone-conjecture test:** the lactoferrin-only arm and §1.25's DAF SCR1-4 arm can establish comparable single-payload baselines only when host, promoter, format, quantification, and construct context are harmonized. Their separate results do not establish an interaction or fold-class rule. A later matched combination must report expression, native fold, secretion, retained activity, host stress, and growth for every payload.

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

**Single-cassette comparator:** The lactoferrin-only arm measures expression, native fold, secretion, and retained function for one exact NSlD-ΔP10 solid-state configuration. Compare it directly with the dual-cassette arm. Do not use its titer alone to infer a fold-class coefficient, a PDI ceiling, or why Huynh 2020 and Ward 1995 reported different outputs in different hosts and formats.

**Plasmidsaurus QC pipeline:** apply the canonical [§05 Plasmidsaurus QC pipeline](./engineered-koji-protocol.md#step-5-strain-qc-infrastructure-plasmidsaurus-pipeline-for-plasmid--transformant--strain-verification) across the §1.9 build:
- **Pre-transformation:** Whole Plasmid Sequencing of both cassette plasmids before any transformation work ($15 × 2 = **$30**, 1 day). Catches construct errors before the $500–1,000 cloning/transformation reagent spend.
- **Post-transformation clone screening (Cassette A round):** Genotyping Analysis on 6–10 hLf-alone transformants to pick clean on-target integrants before committing to Western screening ($30 × 8 = **$240**, 1–2 days).
- **Post-transformation clone screening (Cassette B round):** Genotyping Analysis on 6–10 dual-cassette transformants ($30 × 8 = **$240**, 1–2 days). Same logic — screen on integration cleanliness before fermentation panel.
- **Junction PCR sequencing (both rounds):** Amplicon Sequencing on 2–4 junction PCRs per integration ($15 × 6 = **$90**, next-day).
- **Final platform-strain release:** Whole Genome Sequencing on the validated dual-cassette strain (Eukaryotic tier for *A. oryzae*, $250 + $15 DNA extraction = **$265**, 3–6 days). This is the "publish-grade" sequence for the open-source-strain-library release.

**Plasmidsaurus QC pipeline subtotal: ~$865, ~15% of the §1.9 envelope.** Replaces piecemeal Sanger + multiple junction PCRs + qPCR copy-number — the qPCR copy-number assay can be retained as a sanity check or replaced entirely by Whole Genome Sequencing readout from the final-strain step.

**Host-stress transcriptome readout:** Compare WT NSlD-ΔP10, lactoferrin-only, uricase-only, and dual-cassette conditions with at least three biological replicates. Quantify UPR targets (`hac1`, `bipA`, `pdiA`, `ero1`), broader secretion/trafficking programs, native biosynthesis transcripts, and growth-state markers. Analyze these alongside per-payload protein, fold, secretion, activity, metabolites, and growth. Transcript changes alone cannot identify saturation or a causal bottleneck.

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

**Retired computational prior (comp-010) — cassette compatibility:** The LOW cassette-risk verdict, codon-collision result, KEX2 cleavage classifications, glycosylation mapping, bulk-disulfide capacity comparison, and routing recommendations are invalid. The exact planned CDS, carrier–junction–payload boundaries, produced termini, compartment, abundance, folding, and retained function must be measured. Internal sequence matches may nominate terminal mapping but do not justify a prespecified mutation or exclude a topology. Full evidence boundary: [`cassette-compatibility-computational.md`](./cassette-compatibility-computational.md). Evidence level: Mechanistic Extrapolation until measured.

**Retired computational prior (comp-022) — cassette ranking:** The artifact's 43,200-row enumeration survives only as historical inventory. Every score, rank, N-of-five tier, shortlist, direct-secretion cluster, gene-synthesis refinement, component preference, and GlaA-KEX2 ordering is invalidated. Direct secretion, GlaA-KEX2 processing, promoter, signal-peptide, codon, terminal, propeptide, and glycosylation choices remain unranked factors for the matched construct matrix. Measure expression, processing and termini, localization, native or oligomeric state, fraction-specific intact active UOX, oxygen/peroxide behavior, host viability, and process retention. See the [evidence boundary](./uricase-cassette-ranking-computational.md) and [non-runnable tombstone](./etc/experiments/comp-022-clockbase-uricase-cassette-ranking/).

**Cordycepin cassette boundary (comp-023):** Jeennor et al. directly demonstrated *cns1+cns2*-enabled cordycepin production in *A. oryzae* in their tested configuration (**In Vitro**, PMID 38071331). COMP-023 is invalidated and supplies no burden, flux, yield, breakpoint, product, feasibility, or multi-cassette result. If the deprioritized engineered-cordycepin track reopens, use the matched four-arm isogenic experiment on the [cordycepin route page](./cordycepin-cassette-burden-computational.md) to measure product, secreted-payload function, growth, and ER/cell-state effects directly.

**Cross-references:** [koji-endgame-strain.md](./koji-endgame-strain.md) §3 (full protocol rationale + adjacent literature: Li 2024 PMID 39830075 multi-copy in *A. oryzae*, Wang 2023 PMID 37807677 multi-locus in *A. niger*), [engineered-koji-protocol.md](./engineered-koji-protocol.md) §16 (starting single-cassette lactoferrin module that this experiment ladders on top of), [lactoferrin.md](./lactoferrin.md) §7 (Open Enzyme feasibility bet), [synthesis/](../synthesis/README.md) 2026-04-24 Connection 1, [cassette-compatibility-computational.md](./cassette-compatibility-computational.md) (retired comp-010 evidence boundary).

---

### 1.10 Heterologous Uricase + Lactoferrin Stability in Shio-Koji Salt-Protease Ferment

**Status**: Proposed | **Cost**: $520–900 core reagents; condition matrix, oligomer assay, and microbial QC TBD | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [koji-home-fermentation](./koji-home-fermentation.md), [engineered-koji-protocol](./engineered-koji-protocol.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [synthesis/](../synthesis/README.md), [lactoferrin](./lactoferrin.md)

**What it tests:** Does the 7–14 day shio-koji salt-protease ferment degrade engineered uricase and/or lactoferrin produced by *A. oryzae*? **Two proteins are tested in the same run** because their sequence and structural priors differ. For UOX, comp-001 maps adjacent-pair matches to unverified legacy filters and their pLDDT context but does not establish cleavage specificity, solvent exposure, or protease survival; for lactoferrin, the model likewise remains a proxy. Both arms are empirical feasibility tests, and retained activity—not an intact-looking band or model score—is decisive.

**Gate:** tests whether both payload classes retain activity in the intended shio-koji format.

**Protocol:**
- **Constructs:** Use the exact §1.5 koji configuration advanced by §1.33, plus a co-expressing or separate lactoferrin strain if available. A spiked-material pilot may use characterized research-grade proteins to estimate process and assay variance, but those concentrations are controls rather than physiological or dose assumptions.
- **Ferment matrix:** Prepare shio-koji per [koji-home-fermentation.md](./koji-home-fermentation.md) standard protocol (15–20% NaCl, room temp 22–25°C). Run in parallel with two control matrices: (a) freshly harvested koji (no salt ferment), (b) amazake-style brief warm hold (55–60°C × 6h followed by RT storage) — heat hold partially inactivates proteases.
- **Process recording:** Log matrix temperature continuously and measure pH at every protein-sampling point. A spiked-material pilot defines the observed day-0 and day-14 pH anchors; freeze those two pH levels before the main controlled-condition run rather than importing an assumed range.
- **Controlled-condition matrix:** Test 22°C and 25°C × the two pilot-derived pH anchors × 5%, 10%, 15%, and 20% NaCl at matched protein concentration and sampling time. This factorial separates temperature, pH, and salt effects; the live ferment time course tests their joint process behavior.
- **Time-course sampling:** Aliquot at days 0, 3, 7, 10, 14. Record temperature and pH, then freeze at −80 °C immediately after collection.
- **Readouts — uricase:**
  - Uricase activity: spectrophotometric UA-disappearance assay at 293 nm per [engineered-koji-protocol.md](./engineered-koji-protocol.md) §05 (quantitative).
  - SDS-PAGE + anti-uricase Western blot: detects intact monomer (~34 kDa) vs. degradation products. Distinguishes "lost activity due to denaturation" from "lost activity due to proteolytic cleavage."
  - Oligomeric state: predeclare a validated SEC-MALS or analytical-SEC method with tetramer and monomer controls. Native PAGE is acceptable only after those controls establish band interpretation.
  - Optional CD spectroscopy on extracted uricase: measures secondary-structure change if activity drops without obvious cleavage; CD alone does not establish tetrameric assembly.
- **Readouts — lactoferrin:**
  - Lactoferrin protein integrity: SDS-PAGE + anti-lactoferrin Western blot, detecting intact protein and mapping observed fragments without prespecifying COMP-005-derived candidate regions.
  - Lactoferrin iron-binding capacity (optional functional assay): iron-binding ELISA or colorimetric ferrozine assay at day 0 and day 14; iron-binding is the functional proxy for intact bilobal structure.
  - Note: computational priors for both proteins are non-decision-grade. The Western blot and retained-activity results are the primary feasibility determinations.
- **Linker variants:** Do not select a variant from COMP-034's unverified legacy protease filter. First establish reproducible WT fragment formation in this assay. If a linker-associated fragment is confirmed, commission a new sequence-design lifecycle with verified specificity inputs and a prespecified diversity panel; test variants as matched hypotheses rather than as ranked winners.

**Microbial-community QC (optional until the exact assay is qualified):** bacterial 16S profiling cannot measure *A. oryzae* abundance or establish fungal dominance. To distinguish bacterial contamination from fungal-biomass change, use paired bacterial 16S plus fungal ITS profiling, or validated taxon-specific qPCR/ddPCR with spike-in and extraction controls. Sample the engineered and WT matrices at day 0 / day 7 / day 14. Treat relative-abundance profiles as compositional rather than as biomass measurements. Freeze reportable limits and a decision rule only after the pilot establishes assay precision and background distributions; the former 5% and 10% relative-abundance cutoffs are not binding gates. A community shift can trigger targeted contaminant identification and reinterpretation of protein loss, but it cannot by itself assign protease causality.

**Estimated cost:** $520–900 core reagents — uricase activity assay reagents ($100–200), lactoferrin iron-binding assay reagents ($50–100), SDS-PAGE / Western antibodies for both proteins ($300–500), bovine lactoferrin standard ($50), and shio-koji ingredients ($20–50). Price the controlled-condition matrix, validated oligomeric-state assay, and optional microbial QC after the exact sample count, method, controls, and provider are fixed. No linker-variant synthesis belongs in the core budget.

**Estimated timeline:** 3–4 weeks — parallel with the active fermentation. Day-by-day sampling continues over the 14-day window; assay batches at days 0/3/7/10/14 are ~2 days each.

**Dependencies:** The UOX product-format decision follows §1.5 construct supply and §1.33 advancement of that exact koji configuration. A spiked-material pilot may run earlier to estimate assay and process variance, but it cannot promote a configuration or delivery format.

**Success criteria:**
- Estimate assay and process variance, then prespecify the retained-active-UOX and integrity margins for the selected configuration before assigning an accept, iterate, or reject result to shio-koji processing.
- An intact band without retained activity does not pass; retained activity without §1.33-condition product formation does not establish physiological sufficiency.
- Interpret lactoferrin integrity and function separately. Neither payload's result is automatically transferable to another protein or peptide.

**Computational prior (comp-001) — uricase only:** comp-001 maps Q00511 adjacent pairs that match three unverified legacy preference filters and reports AlphaFold per-residue pLDDT. The arrays are not established exhaustive protease-specificity rules. The computation does not calculate solvent exposure or SASA and does not measure protease survival, retained activity, salt-conditioned behavior in the ferment, or fermentation performance. The UOX arm of §1.10 therefore remains an empirical feasibility gate; comp-001 supplies only a fixed-filter and structural-confidence inventory. Full analysis: [`wiki/uricase-protease-stability-computational.md`](./uricase-protease-stability-computational.md) and [`etc/experiments/comp-001-uricase-shio-koji-protease-stability/`](./etc/experiments/comp-001-uricase-shio-koji-protease-stability/).

**Computational prior (comp-005) — lactoferrin:** The inherited model maps sequence-filter matches and AlphaFold pLDDT but incorrectly used pLDDT confidence as an accessibility class. Its HIGH/MODERATE labels and pLDDT-derived region priorities do not establish solvent exposure, cleavage, degradation, or survival. The exact inter-lobe connector is not a lower-confidence segment in the retired input. Both the lactoferrin and UOX arms remain empirical feasibility gates. If degradation is observed, map fragments without prespecifying their origin; only a reproducible linker-associated failure activates the separate redesign conjecture. Full analysis: [`wiki/lactoferrin-protease-stability-computational.md`](./lactoferrin-protease-stability-computational.md) and [`etc/experiments/comp-005-lactoferrin-shio-koji-protease-stability/`](./etc/experiments/comp-005-lactoferrin-shio-koji-protease-stability/).

**Cross-references:** [synthesis/](../synthesis/README.md) 2026-04-27 Open Question #2 + Connection #2; [engineered-koji-protocol.md](./engineered-koji-protocol.md) §06 (process and transit comparison); [koji-home-fermentation.md](./koji-home-fermentation.md) (shio-koji standard protocol); [aspergillus-oryzae.md](./aspergillus-oryzae.md) (native protease characterization); [uricase-protease-stability-computational.md](./uricase-protease-stability-computational.md) (comp-001 fixed-filter/pLDDT-context inventory); [computational-experiments.md](./computational-experiments.md).

---

### 1.11 Ergothioneine → ABCG2 Expression and Function in Caco-2

**Status**: Proposed — source and exposure qualification required | **Cost**: $1,000–1,500 | **Weeks**: 3–4 | **Phase**: 1

**Affected wiki**: [abcg2-modulators](./abcg2-modulators.md), [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [gut-lumen-sink](./gut-lumen-sink.md)

**What it tests:** Whether source-qualified ergothioneine changes ABCG2 expression and mechanism-matched transport function in human enterocyte-lineage cells across an analytically verified, noninjurious exposure range. The proposed ergothioneine → redox/Nrf2 → ABCG2 connection is a **Mechanistic Extrapolation**; neither antioxidant activity nor ABCG2 expression alone establishes useful urate transport.


**Protocol:**
- **Cells:** Caco-2 (ATCC HTB-37), differentiated 21 days on transwell inserts to recapitulate apical/basolateral polarity.
- **Treatment arms:**
  - Vehicle control
  - Ergothioneine at no fewer than three concentrations selected only after primary-source exposure review, analytical confirmation in the assay medium, and a viability pilot
  - Sulforaphane at 1 μM (positive control — established Nrf2 → ABCG2 inducer per Xie 2020)
  - Combination: one pilot-supported ergothioneine concentration plus a prespecified subthreshold sulforaphane concentration; declare the interaction model before result-bearing use
- **Time-course:** 6, 24, 48 h.
- **Readouts:**
  - ABCG2 mRNA (qPCR, normalized to GAPDH)
  - ABCG2 protein (Western, apical-membrane fraction)
  - Mechanism-matched function: urate-direct transport in bidirectional transwells, with an ABCG2-attribution control; a generic BCRP probe may be secondary but cannot replace the urate endpoint
  - Nrf2 nuclear translocation (immunofluorescence, 6 h timepoint)
- **Analytical and injury controls:** verify free ergothioneine exposure in medium and prespecify viability/barrier-integrity exclusions.

**Estimated cost:** $1,000–1,500 — Caco-2 culture + transwell inserts ($300), ergothioneine + sulforaphane standards ($150), qPCR primers + reagents ($200), Western antibodies for ABCG2 + Nrf2 ($300), Hoechst probe + plate reader time ($100), urate-transport reagents ($150) if pursuing the bidirectional transwell.

**Estimated timeline:** 3–4 weeks.

**Dependencies:** Primary-source exposure review; exact material and purity record; analytical exposure check; viability/barrier pilot; Caco-2 access. The same cell infrastructure may be shared with §1.13.

**Success criteria:**
- **Advance:** A qualifying ABCG2 expression change is accompanied by ABCG2-attributed urate transport at an analytically verified, noninjurious exposure. Any combination claim additionally requires the predeclared interaction criterion.
- **Redirect or kill within the tested scope:** No mechanism-matched functional effect, an effect explained by injury, or failure of the prespecified interaction criterion closes only the tested material, exposure range, and combination—not ergothioneine or fungal sourcing as a class.

**Cross-references:** [abcg2-modulators.md](./abcg2-modulators.md) §2 (Nrf2 transcriptional axis); [medicinal-mushroom-complement-track.md](./medicinal-mushroom-complement-track.md) (ergothioneine exact-material and exposure boundary).

---

<a id="112-local-h2o2-stress-in-caco-2-from-the-selected-uox-configuration"></a>
### 1.12 Local H₂O₂ Stress in Caco-2 from the Selected UOX Configuration

**Status**: Proposed | **Cost**: $800–1,200 | **Weeks**: 2–3 | **Phase**: 1

**Affected wiki**: [uricase](./uricase.md), [aspergillus-oryzae](./aspergillus-oryzae.md), [gut-lumen-sink](./gut-lumen-sink.md), [engineered-koji-protocol](./engineered-koji-protocol.md)

**What it tests:** Whether an exact UOX configuration advanced by §1.33 produces epithelial H₂O₂ exposure and barrier effects under the substrate, oxygen, localization, and activity conditions measured in that screen. Sensitivity conditions must remain labeled as sensitivity conditions; they are not human-baseline premises. The catalase-neutralization assumption in [`uricase.md`](./uricase.md) and [`aspergillus-oryzae.md`](./aspergillus-oryzae.md) remains unquantified.


**Protocol:**
- **Cells:** Caco-2 transwell monolayer, 21-day differentiated.
- **Treatment arms:**
  - Matched vehicle, inactive-UOX, and matrix- or chassis-only controls under the §1.33 terminal-ileal clinical-cohort substrate prior.
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

**Status**: Proposed | **Cost**: TBD | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [abcg2-modulators](./abcg2-modulators.md), [androgen-urate-axis](./androgen-urate-axis.md), [gut-lumen-sink](./gut-lumen-sink.md), [supplements-stack](./supplements-stack.md), [lactoferrin](./lactoferrin.md), [koji-endgame-strain](./koji-endgame-strain.md), [purine-degrading-bacteria](./purine-degrading-bacteria.md)

**What it tests:** Four questions in one experiment. (1) What is the direction and magnitude of DHT's effect on ABCG2, and does DHT interact with TNFα rather than add a presumed second suppression axis? (2) Does butyrate increase ABCG2 surface expression or urate flux under TNFα and in Q141K cells? (3) Does lactoferrin alter epithelial signaling or urate flux in the presence of fixed exogenous TNFα? This arm does not test upstream TNFα production or reproduce luminal delivery from koji. (4) Across measured free exposure and time, do quercetin, EGCG, or curcumin change ABCG2-attributed intestinal urate flux, and does any verified effect interact with Q141K?

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
  - **Supplement ABCG2 interaction arms:** First run solubility, viability, barrier-integrity, and analytical range finding for quercetin, EGCG, and curcumin. For each compound, prespecify at least two apical conditions within the barrier-intact, noncytotoxic range and quantify free parent compound plus major detected metabolites in the assay medium. Compare vehicle, compound, an ABCG2 reference-inhibitor control, and an ABCG2-attribution condition such as matched knockout/knockdown or a validated selective blocker. Measure basolateral-to-apical urate flux with mass balance; do not substitute a drug-probe IC50 for urate transport. Advance a compound to WT-versus-Q141K comparison only after the WT experiment shows a reproducible ABCG2-attributed flux effect.
- **Time-course:** Prespecify short and extended exposure windows for every supplement arm. Measure exposure, protein, barrier integrity, viability, and urate flux at each window rather than assuming an acute-inhibition/chronic-induction switch.
- **Readouts:** ABCG2 mRNA (qPCR), total and apical-surface ABCG2 protein, functional urate efflux (transwell basolateral-to-apical flux with mass balance and ABCG2 attribution), measured free parent compound and metabolites, TEER or equivalent barrier integrity, and viability. The DHT/TNFα/lactoferrin arms also retain a validated AR reporter or Caco-2 AR-responsive target, PXR/FXR response markers, NF-κB activation, and free plus total TNFα as applicable. CYP3A4 alone is not an AR-specific manipulation control.

**Estimated cost:** TBD. Re-estimate after confirming the matrix-qualified exposure/metabolite assay, ABCG2-attribution control, range-finding workload, and pilot variance for the powered confirmation.

**Computational evidence audit (comp-004):** the cited quercetin, curcumin, and EGCG records use different substrates and systems and do not support a quantitative intestinal urate-transport prediction. The nominal concentration/IC50 ratios, predicted inhibition percentages, and risk tiers are invalid. The surviving result is the direct-assay route above. Full analysis: [`supplement-abcg2-antagonism-computational.md`](./supplement-abcg2-antagonism-computational.md) and [`etc/experiments/comp-004-supplement-abcg2-antagonism/`](./etc/experiments/comp-004-supplement-abcg2-antagonism/).

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

### 1.21 Natural-Product C5aR1 Antagonist Screening — Historical Computational Pass

**Status**: Historical bounded search result — no validated natural-product hit in the recorded query set | **Cost**: $0 | **Weeks**: 0.5 | **Phase**: 1 (computational)

**Affected wiki**: [complement-c5a-gout](./complement-c5a-gout.md), [nlrp3-exploit-map](./nlrp3-exploit-map.md) (CP0), [open-enzyme-vision](./etc/open-enzyme-vision.md) (CP0 gap statement).

**What it tests:** The recorded search asked whether its specified databases and literature queries surfaced a natural-product C5aR1 antagonist worth wet-lab triage. It can bound only that query set and date. A no-hit result does not close natural products as a class, establish structural impossibility, select a pharmaceutical answer, or determine the rest of the portfolio.


**Protocol — what was actually run:**

1. **ChEMBL target confirmation and bioactivity pull.** Query ChEMBL REST API for target CHEMBL2373 (confirmed: human C5AR1, UniProt P21730, "C5a anaphylatoxin chemotactic receptor 1", G-protein-coupled receptor, single protein, *Homo sapiens*). Total bioactivity records at CHEMBL2373: **4,873** (April 2026 query). Filter the curated potent tail at pChEMBL ≥ 6 (sub-μM IC50, Ki, or EC50 against human receptor).
2. **Manual classification of the potent tail.** Walk the top ~20 highest-pChEMBL entries; classify each as synthetic vs. natural-product by inspecting molecule_type, structure_type, pref_name, and the `natural_product` flag on each ChEMBL molecule record. Distinguish "natural-product-derived synthetic peptide" (e.g., C5a C-terminal mimics) from true small-molecule natural products.
3. **Cross-database verification.** Search NPASS (Natural Products Activity & Species Source) and LOTUS (Naturally Occurring Chemical Compounds Storage) for any curated natural-product entry at C5AR1. Search NPAtlas for microbial natural products with reported C5aR1 activity.
4. **Open Targets cross-check.** Pull the C5AR1 known-drugs list from the Open Targets Platform (target ENSG00000197405) — surfaces clinical/preclinical compounds that ChEMBL may not have indexed yet, plus any natural-product-derived clinical assets.
5. **Targeted primary-literature search.** PubMed-via-WebSearch queries for: `"C5aR1" antagonist plant`, `"C5aR1" natural product flavonoid OR terpenoid OR alkaloid`, `"C5a receptor" inhibitor flavonoid IC50 cell-based`, `"C5aR1" inhibitor marine fungus`. Catches any plant- or microbe-source antagonist reported in primary literature without ChEMBL curation.
6. **Avacopan structural-class check.** Quick SwissSimilarity / pharmacophore scan against avacopan's cyclohexanecarboxamide / piperidine motif — most plant secondary metabolites won't share this scaffold but worth a fast pass. *(Skipped after step 5 returned <5 candidates — see "what was not run" below.)*

**What was not run, and why:** AlphaFold + AutoDock Vina docking against a curated natural-product library was deferred. The protocol gated docking on at least five wet-lab-validated or strongly prior-supported candidates emerging from steps 1–5; the recorded search found none meeting that gate. Docking-only leads would not have supplied the missing functional evidence. This decision applies to that search and gate, not to every future library or candidate.

**Result:**

- **Total ChEMBL bioactivities at human C5AR1 (CHEMBL2373):** 4,873 (April 2026; up from the 506 figure cited in the existing [`complement-c5a-gout.md`](./complement-c5a-gout.md) §10.1 — that older count was likely distinct compounds at a higher-confidence cutoff or an earlier ChEMBL release, not total bioactivity records; see cross-reference correction note in §10.1 follow-up).
- **Curated natural-product hits at human C5AR1 with wet-lab functional or binding data: 0.** No compound flagged `natural_product=1` in ChEMBL appears in the sub-μM potency tail. The full pChEMBL ≥ 6 list at CHEMBL2373 is dominated by synthetic cyclic peptides (PMX-53/PMX-205 series, 1995–2006 BMCL/JMC papers, IC50 18–60 nM in [125I]-C5a binding or PMN glucosaminidase release), synthetic imidazolidinones / piperazines / piperidines (the CO13 binding-competition series, IC50 25–450 nM), and clinical-stage allosteric small molecules in the avacopan structural class.
- **Apparent peptide hit, not a natural product:** CHEMBL217378 (sequence ISHKDMQLGR, EC50 1.3 nM in PMN polarization) initially looked natural-product-flavored at the sequence level but is curated as `molecule_type: "Protein"`, `natural_product: 0`, `pref_name: "ISHKDMQLGR"` — a synthetic decapeptide derived from C5a's own C-terminal sequence, designed as a receptor-engagement probe, not an isolated natural product.
- **Computational-only natural-product candidates from primary literature (no wet-lab confirmation):**
  - **Acteoside** (verbascoside; phenylethanoid glycoside; plant natural product widely distributed in *Olea europaea*, *Plantago*, *Verbascum*, *Rehmannia*, *Lamiales* generally) — Shaikh & Siu 2016, *Med Chem Res* 25:1564–1573 (PMID 27499603). Homology model of C5aR1 (Glide XP docking + MM-GBSA), ΔG_bind = −113.9 kcal/mol, XP GScore = −12.4 kcal/mol. Authors explicitly state: "biological experiments to validate this inhibitor are being planned as a future work." The recorded follow-up search did not find a validating functional study. Evidence level: *Computational / homology-model docking only.*
  - **Toxicarioside** (cardiac glycoside from *Antiaris toxicaria*, the upas tree; latex traditionally used as a dart poison in Southeast Asia) — same Shaikh & Siu 2016 paper, ΔG_bind = −90.1 kcal/mol. **Safety flag:** the docking lead cannot advance without a primary toxicology, selectivity, and exposure review of the exact compound and comparator scaffold. Evidence level: *Computational only.*
  - **Resveratrol** — Mishra et al. 2020, *J Biomol Struct Dyn* (PMID 32131707). Molecular dynamics + automated docking + MM-GBSA + circular dichroism + steady-state fluorescence biophysics. Critically, resveratrol binds **hC5a (the ligand)**, not C5aR1 (the receptor) — a "neutraligand" approach that prevents C5a from engaging C5aR1 by sequestering the soluble anaphylatoxin. Mechanistically distinct from receptor antagonism (direct receptor antagonism) but tangentially relevant. No reported potency in standard inhibitor units; the biophysics suggest binding but do not establish a functional IC50 on C5a-driven C5aR1 signaling. Evidence level: *Computational + cell-free biophysical binding; no functional assay.* This signal does not qualify resveratrol for CP0 placement.
- **Open Targets known-drugs list at C5AR1 (ENSG00000197405):** The recorded query surfaced avacopan as a synthetic C5aR1 antagonist and upstream C5-binding biologics that are not C5aR1-directed. It did not surface a natural-product-derived clinical or preclinical asset in that query result.
- **NPASS / LOTUS:** The recorded queries did not surface a curated natural-product C5aR1 entry in either database. Database non-retrieval is not biological absence and does not show whether an uncurated material has been tested.
- **Plant flavonoid CH50 literature:** The records summarized in [`complement-c5a-gout.md`](./complement-c5a-gout.md) §10.2 concern broad complement-pathway readouts rather than selective C5aR1 function. They did not satisfy this experiment's receptor-specific triage gate.

**Bounded interpretation:** The recorded search returned no wet-lab-validated natural-product C5aR1 antagonist. It surfaced two computational-only plant leads and a mechanistically distinct cell-free hC5a-binding lead. That result lowers the priority of repeating the same query unchanged; it does not prove absence outside the searched sources, close the class, select avacopan, or imply that an engineered or natural-product route is structurally incapable of reaching CP0.

**Next-search triggers:** Revisit when a new database release or primary paper supplies functional C5aR1 evidence for an exact natural product, when a current computational lead receives functional validation, or when a meaningfully different multilingual/source query is proposed. Any new lead still requires primary-source verification, exact-material identity, exposure, functional attribution, and safety counterscreens.

**Cross-references:** [complement-c5a-gout.md](./complement-c5a-gout.md) §9 (CP0 platform gap) + §10 (natural-product modulator literature); [nlrp3-exploit-map.md](./nlrp3-exploit-map.md) (CP0 chokepoint); [open-enzyme-vision.md](./etc/open-enzyme-vision.md) ("CP0 gap — honest acknowledgment"); [synthesis/](../synthesis/README.md) 2026-04-24 Connection #2 + Proposed Experiment #3. Source: ChEMBL CHEMBL2373 (April 2026); Open Targets ENSG00000197405; Shaikh F, Siu SWI. *Med Chem Res* 25:1564–1573 (2016, PMID 27499603); Mishra et al. *J Biomol Struct Dyn* 2020 (PMID 32131707).

---

### 1.22 Gut-Compartment HDAC-Directed Candidate Screen for Q141K-ABCG2 Trafficking Rescue

**Status**: Proposed | **Cost**: TBD | **Weeks**: TBD | **Phase**: 1

**Affected wiki**: [abcg2-modulators](./abcg2-modulators.md), [ABCG2 Q141K chaperone re-screen](./abcg2-q141k-chaperone-rescreen-computational.md), [superseded comp-032 screen](./abcg2-q141k-chaperone-screen-computational.md), [chassis-pending interventions](./chassis-pending-interventions.md), [supplements-stack](./supplements-stack.md), [gut-lumen-sink](./gut-lumen-sink.md)

**What it tests:** Whether a defined material, at measured intracellular exposure, restores Q141K ABCG2 apical-surface localization and ABCG2-attributed urate flux without directly inhibiting the transporter, injuring the epithelial barrier, or causing unacceptable off-target activity. Basseville et al. 2012 (PMID 22472121) supplies pharmacological positive and contrast controls; it did not test butyrate or urate.

**Mechanistic boundary:** Basseville reported rescue with romidepsin, panobinostat, and vorinostat; valproate did not rescue, and HDAC6-selective tubastatin did not reproduce the effect. Rescue required new protein synthesis and appeared after an approximately 16-hour delay. BiP, Hsc70, Hsp70, and Hsp90 expression did not explain the result; dynamitin-associated retrograde transport was implicated but did not establish one causal HDAC isoform. The experiment must reproduce this control pattern before interpreting a candidate failure or hit.

**Direct-chaperone hypotheses enter here unranked.** [COMP-047](./abcg2-q141k-chaperone-rescreen-computational.md) excludes rosuvastatin and leaves vorinostat as one marginal executable docking row, not a docking-backed priority. Its CFTR correctors are cross-protein mechanism comparators rather than ABCG2-positive controls, and the recorded rank instability invalidates that static ordering without proving that no rescue site exists. The superseded [COMP-032](./abcg2-q141k-chaperone-screen-computational.md) compounds therefore remain an unranked hypothesis inventory.

Vorinostat's role in this experiment comes from Basseville's **In Vitro** Q141K rescue result, not from COMP-047. This section is the decisive empirical surface for both HDAC-directed and direct-chaperone hypotheses: reproduce the within-target Basseville control pattern, then require surface trafficking, ABCG2-attributed urate flux, direct-inhibition exclusion, measured intracellular exposure, viability, and barrier integrity. Folding-ensemble or ΔΔG work may generate future hypotheses but is not a prerequisite for running this assay.

**Protocol:**

**Stage 1 — Control-pattern reproduction and material qualification:**
- In the Basseville-compatible cell system, reproduce surface-trafficking and drug-substrate-efflux rescue with at least one reported positive HDI condition, with vehicle, valproate, and tubastatin contrasts. Prespecify minimum assay responsiveness before candidate interpretation.
- Qualify each test material by identity, purity, stability, conversion products, free concentration, intracellular exposure, and exposure time. Food occurrence or low oral bioavailability is not an exposure measurement.
- Carry the seven COMP-007 labels—butyrate, sulforaphane, allyl mercaptan, diallyl disulfide, phenethyl isothiocyanate, caffeic acid, and ferulic acid—as an unranked inventory. Do not eliminate or advance a material from nominal HDAC IC50, HDAC6 selectivity, or `1 − bioavailability`.

**Stage 2 — Direct polarized-intestinal test:**
- Use WT-only, Q141K-only, and WT/Q141K co-expression arms in a polarized intestinal model.
- Measure total and apical-surface ABCG2, ABCG2-attributed basolateral-to-apical urate flux, intracellular material exposure, viability, and barrier integrity.
- Include a direct ABCG2-inhibition counterscreen so greater surface abundance cannot hide impaired transporter function.
- Run a concentration-time series inside the qualified exposure range; one nominal concentration cannot define a hit or failure.

**Stage 3 — Route and safety qualification for direct hits:**
- Use PPARγ antagonism or silencing to distinguish endogenous-ABCG2 induction from Q141K trafficking rescue.
- Measure HDAC isoform activity only as follow-up mechanism evidence; do not require or infer a class-I/HDAC6 profile before direct rescue is observed.
- Compare intestinal and hepatocyte exposure and effects, then add compound-specific off-target and toxicity assays. HDAC6 is one possible axis, not a complete safety model.

**Cost and timeline:** Requote after selecting the control system, exposure-analytics method, and number of candidate concentration-time points. The retired $5,000–8,000 / 8–10-week estimate was tied to an invalid preselection design and is not retained.

**Success criteria:**
- **A candidate reproduces positive-control surface trafficking and functional urate flux without ABCG2 inhibition or unacceptable toxicity:** advance that exact material to independent replication and exposure validation.
- **No candidate, including butyrate, reproduces positive-control surface trafficking plus functional urate flux:** no tested material/exposure is validated. This result does not kill the pharmacological-rescue class or untested materials and exposures.
- **A candidate changes surface abundance without ABCG2-attributed urate flux, or inhibits ABCG2 directly:** do not advance it as a urate-export rescue.
- **The positive-control pattern does not reproduce:** the screen is uninterpretable; repair the assay before judging candidates.

**COMP-007 status:** Its in-silico ranking, scores, and shortlist are invalidated. The seven materials enter this experiment unranked. Full current evidence: [food-associated HDAC-directed candidates](./food-grade-hdaci-screen-computational.md); [non-runnable tombstone](./etc/experiments/comp-007-food-grade-hdaci-screen/).

**Cross-references:** [abcg2-modulators.md](./abcg2-modulators.md) §6; [ABCG2 Q141K chaperone re-screen](./abcg2-q141k-chaperone-rescreen-computational.md); [superseded comp-032 screen](./abcg2-q141k-chaperone-screen-computational.md); [chassis-pending interventions §7](./chassis-pending-interventions.md); [gut-lumen-sink.md](./gut-lumen-sink.md); and [food-grade-hdaci-screen-computational.md](./food-grade-hdaci-screen-computational.md).

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

**Status**: Proposed | **Cost**: TBD after route-factorial and disulfide-mapping quotes | **Weeks**: TBD | **Phase**: 1

**Affected wiki**: [daf-cd55-scr14-truncated-computational](./daf-cd55-scr14-truncated-computational.md), [hypotheses/H05-daf-scr14-cp0-thesis](./hypotheses/H05-daf-scr14-cp0-thesis.md), [chaperone-orthogonal-stacking](./chaperone-orthogonal-stacking.md), [koji-endgame-strain](./koji-endgame-strain.md), [complement-c5a-gout](./complement-c5a-gout.md), [modality-chokepoint-matrix](./modality-chokepoint-matrix.md)

**What it tests:** For the truncated DAF/CD55 SCR1-4 construct (aa 35–285, residues immediately following the signal-peptide cleavage site through the end of SCR4 — see [comp-012](./daf-cd55-scr14-truncated-computational.md)), does direct secretion or a GlaA-KEX2 processing route recover more correctly processed, natively folded, complement-regulatory-active soluble protein in each tested *A. oryzae* host? This is the wet-lab gate for the CP0 closure thesis. COMP-012 supplies a sequence-filter proxy, not confirmed protease stability, and COMP-030 supplies no route preference.

**Single-cassette scope.** This experiment measures expression, folding, and activity of DAF SCR1-4 alone. The [chaperone-orthogonal stacking framework](./chaperone-orthogonal-stacking.md) is a research conjecture, not evidence that a triple cassette will fail or that separate strains are preferred. A positive result qualifies this exact single-cassette material for replication; it does not select a combined architecture or chassis.

**Co-primary role — matched chaperone-conjecture test:** this experiment supplies an exact CCP/SCR configuration that can be compared with §1.9's exact lactoferrin configuration. The NSlD-ΔP10 arm must match §1.9's host, promoter, format, and readouts; the RIB40 arm independently tests the candidate configuration. Even harmonized single-payload results do not establish co-expression compatibility; that requires matched pairwise and combined configurations with complete readouts for every payload.

**Gate:** COMP-012 leaves empirical protease risk unresolved. The current design uses the eight intrachain disulfide annotations recorded for the SCR1-4 construct from UniProt P08174 and directly measures expression, folding, retained function, and processing stability.

**Background on the gating context:** COMP-012 compared the stalk-truncated SCR1-4 sequence with the full ectodomain using a known-invalid pLDDT-as-accessibility proxy. It supports testing stalk truncation as a candidate design but does not establish protease stability or a relative survival advantage over UOX. H05 registers the CP0 closure thesis with four wet-lab unknowns: (1) retained complement-regulatory activity without the stalk, (2) correct formation of the 8 annotated intrachain disulfides, (3) useful expression, and (4) retained function through the intended processing and delivery conditions. This experiment addresses all four.

**Fold-annotation context:** UniProt P08174 supplies the eight intrachain disulfide annotations used to design the mapping assay. Those annotations are not a folding-demand score. §1.25 supplies the relevant expression, connectivity, fold, activity, stress, and growth data for the exact configuration.

**Chassis boundary:** [COMP-043](./daf-lactoferrin-ecn-folding-feasibility-computational.md) is invalidated. It supplies no EcN capacity, fallback, or priority conclusion. A future EcN DAF configuration would require its own matched expression, native-fold, retained-function, and route-stability evidence and would not inherit a positive or negative result from this koji experiment.

**Protocol:**

- **Construct design — matched processing-route factor.**
  - Direct-secretion route: `[one prespecified promoter — validated *A. oryzae* signal peptide — DAF SCR1-4 mature sequence (aa 35–285 of UniProt P08174) — one prespecified terminator]`.
  - GlaA-KEX2 route: the same promoter, DAF mature sequence, terminator, tag policy, integration target, and copy-number target, with an exact GlaA carrier and KEX2 junction replacing the direct-secretion leader. Freeze and sequence-verify the predicted produced termini before transformation.
  - Use one prespecified DAF coding sequence across both routes. If codon variants are later tested, cross the same variants with both routes and analyze codon as an independent factor; COMP-030 supplies no preferred variant.
  - Selection-marker choice does not establish safety or regulatory status. Ward 1995 supports GlaA-KEX2 as an adjacent-payload production precedent, not as a DAF route winner.
  - **Disulfide assessment design:** UniProt P08174 annotates eight intrachain pairs across SCR1–4. Reducing/nonreducing SDS-PAGE can screen monomer, aggregate, and gross reduction states but cannot establish residue-pair connectivity. Use a qualified nonreducing proteolytic-digest LC-MS/MS disulfide-mapping workflow with reduced/alkylated controls, free-thiol quantification, and functional readout.

- **Host × route factorial — four mandatory configuration arms.**
  - **RIB40 × direct secretion** and **RIB40 × GlaA-KEX2** test the route comparison in the genome-sequenced reference host.
  - **NSlD-ΔP10 × direct secretion** and **NSlD-ΔP10 × GlaA-KEX2** repeat the same route comparison in the 10-protease-deletion host used for the matched §1.9 context.
  - Include parental-host and matched vector controls for each host. Do not pair one route with one host and the other route with the other host; that would confound route with host.

- **Transformation.** PEG/CaCl₂ protoplast, single-step transformation → select on pyrG-minus → confirm cassette integration by PCR + qPCR for copy number stability across 5 serial passages.

- **Fermentation.** Solid-state rice koji, 48–60 h at 30°C, 35% moisture (the project's standard koji condition; matches §1.9 dual-cassette fermentation conditions for downstream comparability). Parallel submerged-culture control (100 mL shake flask, 28°C) to isolate solid-state vs. submerged variable.

- **Readouts.**
  - **Secretion + apparent MW:** reducing and nonreducing SDS-PAGE plus anti-DAF/CD55 Western on culture supernatant. Use the gels to screen intact protein, gross reduction-state shifts, and high-molecular-weight aggregates; do not infer native intramolecular connectivity from band position or aggregate absence.
  - **Quantitative titer:** anti-DAF/CD55 ELISA on culture supernatant. The legacy ≥50 mg/L value is a provisional engineering-routing constant, not a literature-derived therapeutic or pore-fluid threshold.
  - **Disulfide connectivity and free thiols:** on purified protein, use peptide-level LC-MS/MS disulfide mapping after a nonreducing digest, with reduced/alkylated controls and a qualified search/acceptance workflow. Report recovery of each annotated P08174 pair, any alternative linkages above the validated detection limit, and free-thiol abundance. Intact mass alone is insufficient.
  - **CCP-regulatory activity assay:** measure a concentration-response for purified DAF SCR1-4 in a zymosan-activated human-serum C5a assay against buffer, inactive-material, and reference-material controls where a qualified reference is available. Freeze the concentration series and confirmatory effect threshold after a pilot; the legacy 30% value is a provisional experiment-design constant, not a therapeutic benchmark.
  - **Native metabolite profile** (process-stress screen): kojic acid titer by HPLC and ergothioneine titer by LC-MS. The legacy ±30% band is a provisional process-screening constant, not a safety or efficacy threshold.

**Construct and strain QC:** apply the canonical [§05 construct-identity workflow](./engineered-koji-protocol.md#step-5-strain-qc-infrastructure-plasmidsaurus-pipeline-for-plasmid--transformant--strain-verification) to the full four-configuration factorial:
- sequence-verify both route plasmids before transformation;
- genotype and junction-sequence candidate integrants independently for each of the four route × host configurations;
- verify copy number and retain at least two independent integrants per configuration for the pilot;
- whole-genome sequence the final selected strain for each configuration that enters the confirmatory comparison.

The initial planning count is therefore two route constructs, four configuration-level transformant screens, four junction/QC sets, and up to four final-strain genome checks. Current provider pricing, disulfide-mapping coverage, clone count, fermentation replication, and assay-precision requirements must be quoted together before freezing cost or duration.

**Estimated cost and timeline:** TBD. The previous $4,445–6,745 / 6–8-week estimate covered one route across two hosts and is not valid for this four-configuration factorial. Freeze the budget and schedule only after current quotes cover both constructs, four transformation arms, independent integrants, matched fermentations, peptide-level disulfide mapping, and the functional concentration-response assay.

**Dependencies:** Same lab-access pathway as §1.9 — a Role 2 (Pharma Translation) collaborator (per [`etc/team.md`](./etc/team.md)) if recruiting converts; commercial CRO specializing in filamentous-fungus engineering (Lonza, Novozymes, Dyadic); community biolab with protoplast-transformation capability (Genspace NY has *A. oryzae* precedent). Global parallel options mapped in [`operations/ward-1995-lab-access.md`](../operations/ward-1995-lab-access.md). **This experiment shares lab-access infrastructure with §1.9** — both are *A. oryzae* protoplast transformation + solid-state koji fermentation + standard mammalian-protein readout assays. If §1.9 is running in a partner lab, §1.25 is a natural co-batch experiment with marginal infrastructure cost (sequential transformations on the same host, parallel fermentations under the same conditions).

**Decision rule:** Pilot data must establish assay precision, mapping coverage, concentration range, and provisional routing constants before the confirmatory run.

- **Advance an exact configuration:** within each host, compare the two routes using the same prespecified product-quality and function criteria. A configuration advances only with reproducible intact-protein recovery; all eight annotated pairs recovered by the qualified peptide-level mapping workflow without a dominant alternative-connectivity species at the validated detection limit; free-thiol results consistent with that mapped oxidized form; reproducible concentration-dependent complement activity versus inactive-material and buffer controls; and no prespecified process-stress failure. The legacy 50 mg/L, 30% activity, and ±30% metabolite bands are provisional design constants until that pilot.
- **Iterate:** measurable expression or activity with a mapping, precision, or process-stress failure that can be assigned to one changeable construct, host, or process variable. Change one variable and repeat the complete workflow.
- **Reject this configuration:** after the prespecified optimization limit, no reproducible intact product, unresolved or dominant alternative connectivity, or no activity above the validated assay detection limit. Update H05 and redirect the construct or host; do not reject soluble complement regulation as a mechanism.

**Computational priors that informed this design:**
- [comp-012](./daf-cd55-scr14-truncated-computational.md) — stalk-truncation sequence/pLDDT proxy; empirical protease stability remains part of the wet-lab feasibility question
- [chaperone-orthogonal-stacking framework](./chaperone-orthogonal-stacking.md) — configuration-specific interaction conjecture and matched-test design; construct annotations do not predict tractability or support chassis routing
- **[comp-030](./daf-cd55-scr14-cassette-ranking-computational.md)** — invalidated and non-runnable. It supplies no candidate ranking, codon preference, processing-route preference, fold inference, or secretion verdict. Direct secretion and GlaA-KEX2 remain unranked configurations for a matched test; if codon variants are included, prespecify them as an independent factor. This preserves a Research Conjecture, not a COMP result or evidence level.

**Limitations:**
- Single-cassette testing does not answer whether DAF SCR1-4 interacts with uricase or lactoferrin in a multi-cassette configuration; that requires a separate matched experiment measuring every payload.
- Disulfide mapping depends on purification, digest coverage, ionization, search controls, and validated detection limits; absence of an alternative linkage is not proof of absolute absence
- CCP-regulatory activity assay measures one specific complement readout (C5a generation in zymosan-activation); doesn't directly measure C3 convertase decay-acceleration (the canonical DAF activity) — that would be a follow-up assay if C5a-arm is positive
- No in vivo gut-lumen activity readout in this experiment — that's a Phase 2 / Phase 3 follow-up gated on positive in vitro result

**Cross-references:** [daf-cd55-scr14-truncated-computational.md](./daf-cd55-scr14-truncated-computational.md) (comp-012 sequence/pLDDT prior); [hypotheses/H05-daf-scr14-cp0-thesis.md](./hypotheses/H05-daf-scr14-cp0-thesis.md) (falsification card); [chaperone-orthogonal-stacking.md](./chaperone-orthogonal-stacking.md#matched-experiment) (configuration-specific interaction conjecture and matched-test design); [koji-endgame-strain.md](./koji-endgame-strain.md) (portfolio context); [engineered-lbp-chassis.md](./engineered-lbp-chassis.md) (independent chassis research track); [complement-c5a-gout.md](./complement-c5a-gout.md) (CP0 biology); [operations/ward-1995-lab-access.md](../operations/ward-1995-lab-access.md) (lab access shared with §1.9).

---

### 1.26 ADA-Driven Cordycepin Loss — Exact-Material Interaction Screen

**Status:** Proposed — pilot design required | **Cost:** TBD after pilot | **Weeks:** TBD

**What it tests:** Whether purified pentostatin, one composition-defined GLPP fraction, or one fully characterized *C. militaris* material changes ADA-driven cordycepin loss relative to matched controls. Co-production does not establish a fixed ratio, protection, or beneficial interaction; the actual material composition and free concentrations must be measured.

**Entry requirements:** verify the exact materials and primary-source assay boundaries; quantify cordycepin and pentostatin in any whole material; validate the analytical method; and run a pilot to choose concentrations, sampling times, controls, replication, and the interaction estimand. Include GLPP only if its proposed ADA effect is independently source-qualified.

**Readouts:** cordycepin and 3'-deoxyinosine over time, direct ADA activity, material identity, free concentrations, and assay-interference controls. The final arm count follows the estimand and pilot rather than an inherited five- or six-arm layout.

**Decision rule:** advance only an exact material or pair that reproducibly beats its matched null while preserving assay validity. A null GLPP interaction removes only that fraction under those conditions; a null whole-material result rejects only the tested composition and ratio. No in-vitro result establishes an oral product, dose, urate effect, safety, delivery route, production chassis, or clinical use.

**Cross-references:** [medicinal-mushroom source and material boundaries](./medicinal-mushroom-complement-track.md); [ADA open question](./gout-pathophysiology.md); and the later [matched exposure/function study §2.6](#26-glpp--cordycepin-interaction-in-hyperuricemia--matched-wet-lab-gate).

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
  - Ergothioneine alone: concentration range to be set from a verified human-exposure source, analytical confirmation in the assay medium, and a viability pilot
  - Apo-lactoferrin alone: concentration range selected from exact-material characterization, analytical verification in the assay medium, and a viability pilot
  - Holo-lactoferrin: matched molar concentrations to the advancing apo-lactoferrin arm, with iron saturation measured rather than assumed; this comparator tests whether iron loading changes the result
  - Combination: one ergothioneine concentration selected from the verified range and pilot plus apo-lactoferrin at a prespecified pilot-supported concentration; define the interaction model and reference point before result-bearing use

- **Primary readout:** secreted IL-1β, paired with a mechanism-proximal NLRP3/caspase-1 readout so a cytokine change is not treated as target attribution by itself
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

**Status:** Proposed — material and assay pilots required | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1

**Scope:** This is a direct-macrophage directionality screen. It asks whether an exact, qualified *Houttuynia* polysaccharide material suppresses, amplifies, or does not change IL-1β release in a THP-1 LPS/MSU model. It does not test oral delivery, product equivalence, serum complement, CFH dependence, or human gout efficacy.

**Affected wiki:** [Houttuynia evidence home](./houttuynia-cordata.md), [NLRP3 exploit map](./nlrp3-exploit-map.md), [complement C5a in gout](./complement-c5a-gout.md), and [COMP-040](./computational-experiments.md).

**Evidence prior:** Zhou 2022 characterized HCPM as a 19.1 kDa acidic heteropolysaccharide isolated from crude HCP by sequential ultrafiltration and reported anti-complement activity plus an H1N1 mouse phenotype (**In Vitro + Animal Model**; PMID 36252625). Li 2025 found that both HCPM and crude HCP reduced intestinal complement and NLRP3-related readouts in H1N1–MRSA coinfection mice (**Animal Model**; PMID 40654358). Cheng 2014 found that a different 60 kDa HCP-2 material increased IL-1β in naïve human PBMCs through a TLR4-sensitive response (**In Vitro**; PMID 24528726). These records justify a directionality test but do not predict its result.

### Stage 0 — material and assay qualification

- **HCPM reference:** obtain the originating-group material or reproduce the sequential-ultrafiltration preparation described by Zhou 2022. Confirm molecular-weight distribution, carbohydrate and uronic-acid content, monosaccharide profile, and batch identity.
- **Crude HCP:** document plant identity and part, extraction, precipitation, deproteinization, drying, composition, and lot.
- **Independent extract lots:** include only lots with documented identity, composition, contaminants, and extraction method. A retail label is not an equivalence claim.
- **Directionality reference:** include HCP-2 only if an exact material can be sourced or reproduced and qualified; it is a source-anchored pro-inflammatory comparator, not a substitute for HCPM.
- **Endotoxin gate:** quantify endotoxin with spike-recovery controls and include an appropriate contamination control before attributing any priming signal to a polysaccharide.
- **Range finding:** determine soluble, non-aggregating, noncytotoxic exposure conditions for each material. Then prespecify at least three concentrations and a result margin from pilot variance. Concentrations from hemolysis, PBMC, or animal studies do not transfer directly to THP-1/MSU.

### Stage 1 — priming × activation matrix

For vehicle and every advancing material/concentration, cross two priming states (no LPS, LPS) with two activation states (no MSU, MSU):

| Condition | What it can reveal |
|---|---|
| No LPS, no MSU | Basal material response |
| LPS, no MSU | Interaction with an established signal-1 stimulus |
| No LPS, MSU | Whether the material itself supplies enough priming for an MSU response |
| LPS, MSU | Suppression, amplification, or null effect in the conventional gout-relevant cell model |

Use a qualified THP-1 differentiation and LPS/MSU procedure. Include vehicle and an NLRP3-pathway inhibitor control such as MCC950; an orthogonal activator such as nigericin may be used for assay characterization but does not need to exceed the MSU response by an arbitrary multiple.

**Readouts:**

- **Primary:** IL-1β in supernatant.
- **Secondary:** IL-6 as a general signal-1/inflammatory readout, plus cell viability. IL-6 is not a TNFSF14-specific probe unless TNFSF14 is separately introduced and controlled.
- **Follow-up only after a reproducible signal:** add a mechanism-proximal readout such as pro-IL-1β transcription, caspase-1 cleavage, or ASC specks to distinguish altered priming from altered inflammasome activation.

Cytotoxicity can masquerade as cytokine suppression. A concentration with morphology or viability failure is not evidence of anti-inflammatory activity.

### Decision rules

- **Advance the direct-macrophage route:** a qualified material produces a prespecified, concentration-responsive direction with acceptable viability, no endotoxin explanation, and independent replication.
- **Retain a material-specific caution:** the material increases signal-1 or LPS/MSU output under qualified conditions.
- **Close only the tested direct route:** no qualified material changes the prespecified endpoint. This does not refute complement suppression, intestinal mediation, another material, or another exposure condition.
- **Do not infer product equivalence:** similar responses among the tested lots apply only to those materials and endpoints.

[COMP-040](./computational-experiments.md) tests the separate CP0/CFH hypothesis in MSU-exposed serum and is not gated by the §1.30 result. The two experiments may be prioritized independently and compared only after each produces interpretable data.

**Cost and schedule:** obtain a quote after confirming HCPM acquisition or preparation, number of independent lots, material analytics, endotoxin controls, pilot plate design, and replication plan.

**Dependencies:** qualified THP-1/MSU capability; exact HCPM or another prespecified material; material analytics; and a pilot-derived analysis plan.

**Cross-references:** [Houttuynia](./houttuynia-cordata.md), [COMP-039](./cfh-mechanism-dissociation-cp0-candidates-computational.md), [complement C5a in gout](./complement-c5a-gout.md), and the dated [structure–activity scan](../logs/houttuynia-polysaccharide-structure-activity-lit-scan-2026-07-14.md).

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

**Dependencies:** SOP-2 HPLC infrastructure (cordycepin reference standard from [Sigma C3394](https://www.sigmaaldrich.com/US/en/product/sigma/c3394) or equivalent; pentostatin reference standard from [Cayman 14878](https://www.caymanchem.com/product/14878/pentostatin) or equivalent); *C. militaris* working strain with ITS-verified provenance (per SOP-5).

**Cross-references:** [medicinal-mushroom-complement-track.md §Sourcing and delivery](./medicinal-mushroom-complement-track.md#sourcing-and-delivery); [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) §SOP-2 and §SOP-7; [Culture configuration](./etc/open-source-platform.md#culture-configuration).

---

### 1.31 Butyrate Culture-Supernatant HPLC-UV Method Transfer Against GC-MS

**Status:** Proposed — partner design required | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1

**Affected wiki:** [`tier-2-butyrate-assay-audit-computational.md`](./tier-2-butyrate-assay-audit-computational.md) (comp-038); [`quantification-ladder.md`](./quantification-ladder.md); [`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md); §1.14; and [`open-questions.md`](./open-questions.md).

**What it tests:** Whether the De Baere HPLC-UV method can quantify butyrate in one exact engineered-strain culture-supernatant matrix with agreement adequate for the prespecified research decision. HPLC-UV is a **Tier 3 bench method** under the OE ladder. GC-MS is the reference comparator: Tier 3 when run in-house and Tier 4 when outsourced. This experiment validates a production measurement, not intestinal exposure, ABCG2 trafficking rescue, gout efficacy, or safety.

**Primary-source anchor:** The De Baere primary abstract reports direct UV detection at 210 nm for bacterial culture supernatants after acidification below pH 2 and liquid-liquid back-extraction with diethyl ether. Matrix-matched calibration covered 0.5–50 mM, and the method quantified four short-chain fatty acids plus lactate. The accessible abstract does not supply analyte-specific LOQ values or explicitly state “underivatized” (**In Vitro**, [PMID 23542733](https://pubmed.ncbi.nlm.nih.gov/23542733/)).

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

**Separate stool candidate:** Gu et al. reported an electrochemical/ANN workflow compared with GC-MS in a within-study independent 30-sample fecal test set, with butyrate MAE/RMSE of 0.029/0.034 mM (**In Vitro**, [PMID 42041444](https://pubmed.ncbi.nlm.nih.gov/42041444/), [DOI](https://doi.org/10.3390/bios16040223)). It neither failed nor belongs in this culture-supernatant experiment. Its hardware–chemistry–model reproduction and independent external transfer are defined separately in [§1.45](#145-fecal-butyrate-electrochemicalann-reproducibility-and-transfer-gate).

**Dependencies:** An analytical partner with HPLC-UV and GC-MS access; the exact production strain and medium; a pilot sufficient to set the result-bearing design.

**Cross-references:** [`tier-2-butyrate-assay-audit-computational.md`](./tier-2-butyrate-assay-audit-computational.md); [`quantification-ladder.md`](./quantification-ladder.md); [`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md); §1.14; §1.28; and [`open-questions.md`](./open-questions.md).

### 1.32 GSDMD-Pore Self-Delivery — Matched Uptake and Selectivity Probe

**Status**: Proposed (wet-lab gated) | **Cost**: ~$2,000–5,000 | **Weeks**: 4–6 | **Phase**: 1

**Affected wiki**: [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md); [`kpv-gsdmd-pore-influx-computational.md`](./kpv-gsdmd-pore-influx-computational.md) (comp-042); [`kpv-peptide.md`](./kpv-peptide.md); [`disulfiram.md`](./disulfiram.md).

**What it tests:** Whether one exact, membrane-impermeant payload has greater intracellular accumulation in GSDMD-pore-forming macrophages than in matched intact-membrane cells under a defined exposure, cell model, and time window. It separates a pore-only physical-delivery test from the KPV/PepT1 transport question.

**Computational prior (comp-042):** **YELLOW-A2-unresolved.** Against a 10 nM extracellular cell-assay effective-concentration proxy—not an intracellular IC50 or efficacy threshold—the modeled A1 engineering states are intra-articular GREEN, subcutaneous YELLOW, and oral RED. The A2 heuristic contains favorable corners: absent and low PepT1 scenarios are at or above 3× in all 9/9 route-concentration × Km cases for every route; intra-articular is also at or above 3× in 2/9 moderate and 1/9 high cases. These values describe the modeled passive pore contribution divided by a heuristic healthy-cell accumulation baseline. They do not model concurrent PepT1 transport in the pore-forming cell and therefore do not establish total-cell selectivity. Synovial-macrophage PepT1 function and matched healthy-cell accumulation remain unmeasured. KPV acts upstream of pore formation, so the pathway ordering makes therapeutic-timing sufficiency uncertain; it does not prove that pore-mediated arrival is too late.

**Entry requirements:**
- Prequalify the exact tracer as operationally transporter-orphan and membrane-impermeant in the chosen cell model, concentration, and time window. The qualification must show no measurable transporter-dependent uptake in intact cells under the tested controls and must record which uptake routes were tested; a catalog description or molecular-class analogy is insufficient.
- Define matched pore-on and pore-off conditions and verify pore state with a mechanism-proximal readout. Freeze the cell model, tracer lot and labeling chemistry, extracellular concentration, exposure duration, wash procedure, viability window, and analysis plan before the result-bearing comparison.
- Pilot recovery, detection limits, background, and cell-loss bias, then prespecify the uptake margin and statistical rule.

**Protocol:**
- **Primary tracer experiment:** cross matched pore-on/off conditions with the prequalified transporter-orphan tracer and quantify intracellular tracer by the locked assay. Keep extracellular exposure identical across pore states.
- **KPV uptake comparator:** use a matched 2 × 2 design—pore on/off × PepT1 on/off—with the same KPV exposure, cell background, and time window. Implement PepT1-off with a qualified inhibitor or knockdown and matched vehicle or non-targeting controls. This arm estimates uptake contributions; it has no KPV efficacy endpoint.
- **Readouts:** intracellular tracer or KPV, extracellular carryover control, pore-state verification, PepT1-state verification for the comparator, and viability/cell-recovery measures needed to interpret uptake.

**Decision rules:**
- **GREEN for the tested physical-delivery configuration:** the exact tracer clears the prespecified pore-on versus pore-off uptake margin, the effect tracks the verified pore state, and assay-suitability criteria pass. This supports only that tracer, concentration, cell model, and time window; it justifies testing additional transporter-orphan payloads but does not establish therapeutic delivery.
- **YELLOW:** pore-associated uptake is detectable but fails the prespecified margin, is sensitive to assay qualification, or cannot be separated from viability or cell-loss bias. Resolve the named ambiguity before escalation.
- **RED for the tested physical-delivery configuration:** the exact tracer fails to clear the prespecified uptake margin with assay suitability and pore-state controls passing. This deprioritizes that tracer, concentration, cell model, and time window; it does not close the broader transporter-orphan platform.
- Interpret the KPV 2 × 2 arm only as an uptake interaction across the tested pore and PepT1 states. It neither proves nor refutes KPV therapeutic efficacy or timing.

**Limitations:** A transporter-orphan tracer is a physical proxy, not a therapeutic payload. Results are bounded to the exact tracer, concentration, cell model, pore induction, and time window. Cell-line pore behavior may not transfer to primary synovial macrophages. The KPV comparator does not resolve therapeutic timing, and an uptake result does not establish target engagement or efficacy.

**Cross-references:** [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md); [`kpv-gsdmd-pore-influx-computational.md`](./kpv-gsdmd-pore-influx-computational.md) (comp-042); [`kpv-peptide.md`](./kpv-peptide.md); [`disulfiram.md`](./disulfiram.md).

<a id="133-physiological-uox-topology--oxygen--peroxide-factorial"></a>
### 1.33 Configuration-Level Physiological UOX × Oxygen × Peroxide Factorial

**Status:** Proposed — first physiological reaction-site gate after construct supply | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1 | **Affected wiki:** [gut-lumen sink](./gut-lumen-sink.md), [engineered koji protocol](./engineered-koji-protocol.md), [delivery-route matrix](./delivery-route-matrix.md)

**What it tests:** Whether an already built and characterized UOX configuration forms product under the terminal-ileal clinical-cohort substrate prior and defined oxygen contexts without a configuration-specific peroxide or viability penalty. It can compare localization strategies within a controlled host background. It cannot declare a topology transferable across EcN, yeast, koji, purified enzyme, or another chassis when the configurations differ in more than localization.

**Entry requirements:**
- Every arm must exist before randomization and must have sequence identity, host or matrix, localization, active-UOX recovery, batch variance, and supporting machinery recorded.
- Yeast arms come from §1.2; koji arms come from §1.5; a PULSE/EcN arm requires the exact characterized strain or an explicitly bounded reconstruction. Catalase- or VHb-bearing arms require their own matched inactive-UOX and support-module controls.
- Within-host topology comparisons must freeze payload, host background, copy state, promoter class, and support modules as far as technically possible. Unmatched features make the result configuration-specific.

**Computational priors:** [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) shows that the legacy unconditional flat-dose robustness claim does not survive the tested diagnostics; it does not select a topology. [comp-045](./uricase-topology-oxygen-peroxide-design-computational.md) supplies a schema-2 candidate randomized layout with biological verdict `NOT_EVALUATED`; it is blocked pending exact control and sampling qualification. Use only the subset for which qualified materials and matched controls exist, and regenerate the randomization under a new exact lifecycle if that subset changes. Primary topology precedents: Gao et al. 2025 ([PMID 41038159](https://pubmed.ncbi.nlm.nih.gov/41038159/)) and Zhao et al. 2022 ([PMID 35491895](https://pubmed.ncbi.nlm.nih.gov/35491895/)).

**Protocol:** Run at least three independent biological batches under separately measured oxygen contexts. Test the terminal-ileal clinical-cohort substrate prior plus prespecified sensitivity and source-benchmark conditions. At every substrate condition include matched inactive-UOX, host- or matrix-only, support-module, no-urate, and medium controls appropriate to that exact configuration. Measure urate and oxidative product, H₂O₂, dissolved oxygen, viability, localization, and active UOX at the reaction site. Report within-host contrasts separately from cross-configuration observations.

**Decision rule:** Advance an exact configuration only if it shows reproducible product formation at the terminal-ileal clinical-cohort prior without a prespecified extracellular-H₂O₂ or viability penalty relative to its matched controls. A result confined to a high-substrate benchmark remains benchmark-positive but physiologically unproven. A within-host localization effect may nominate a topology for that host; a cross-host rank does not. No serum-urate, dose, production, or chassis conclusion is allowed from this assay.

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

### 1.45 Fecal Butyrate Electrochemical/ANN Reproducibility and Transfer Gate

**Status:** Proposed — author package and analytical-partner design required | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1

**Affected wiki:** [Tier 2 butyrate assay audit](./tier-2-butyrate-assay-audit-computational.md), [quantification ladder](./quantification-ladder.md), [open questions](./open-questions.md), and [genotype-informed workflow](./genotype-informed-supplement-workflow.md).

**What it tests:** Whether the complete Gu et al. hardware–chemistry–model stack can be reproduced locally and retain prespecified agreement with GC-MS for fecal butyrate. A pass would qualify one implementation as a Tier 2 research method for one defined stool workflow and concentration range. It would not establish intestinal-wall exposure, ABCG2 engagement, Q141K rescue, gout efficacy, a clinical diagnostic, or a method for another metabolite.

**Primary-source anchor:** Gu et al. used a VBS-100 portable workstation and single-use G3 planar gold electrodes, two stool-preparation streams, alkaline pretreatment for the butyrate route, voltammetric feature extraction, and a TensorFlow multilayer perceptron. The propionate/butyrate model used 72 training cases, including 18 authentic fecal samples, and a within-study independent 30-sample fecal test set; reported butyrate MAE/RMSE/R² were 0.029 mM/0.034 mM/0.998 against GC-MS. The butyrate bias was −0.015 mM with limits of agreement from −0.065 to 0.035 mM and was statistically different from zero (**In Vitro method study**; [PMID 42041444](https://pubmed.ncbi.nlm.nih.gov/42041444/)). The article reports model architecture but does not link reusable code, weights, or a public data package; de-identified study data require an author request.

### Stage 0 — reproducibility package and feasibility

- Request the feature-extraction code, trained weights or complete training code, de-identified calibration/reference data, split identifiers, GC-MS reference method, and electrode/workstation specifications from the authors, subject to their approval process.
- Confirm availability, lot specifications, and pricing for the VBS-100 workstation and G3 electrodes, or define an alternative implementation whose transfer must be validated rather than assumed.
- Obtain analytical-partner and human-specimen-governance review before fixing sample counts, budget, schedule, or acceptance limits. No human sample is collected outside an appropriate consent and ethics framework.
- If the package or exact hardware is unavailable, decide explicitly whether the paper and supplement support a ground-up recreation. Inability to transfer the implementation is an infrastructure result, not evidence that electrochemical SCFA measurement is biologically impossible.

### Stage 1 — analytical replication

- Reproduce the published standard-mixture fingerprints before introducing stool.
- Use qualified archived or prospectively collected specimens, matrix-matched standards, spike/recovery, defined interferents, and paired GC-MS measurements on the same aliquots.
- Test electrode lots, days, and operators. Preserve the published preprocessing branches and pretreatment conditions unless a deviation is registered and requalified.
- Lock feature extraction, normalization, model weights, working range, and reference-agreement rules before evaluating a blinded hold-out set. Set sample count and acceptance limits from the pilot, analytical objective, and GC-MS precision—not from the synthesis queue.

### Stage 2 — independent transfer

Only after Stage 1 passes, evaluate the locked implementation in a separately sourced cohort spanning the intended preanalytical, dietary, and clinical variability. Keep the model locked for the primary transfer analysis; any recalibration creates a new version requiring its own hold-out test.

### Decision rules

- **GREEN:** standards, matrix controls, lots/operators, blinded GC-MS agreement, and independent transfer all meet the prespecified limits. Adopt only the tested implementation as a Tier 2 fecal-butyrate research method.
- **YELLOW:** within-lab performance passes but hardware, electrode-lot, operator, or cohort transfer fails. Retain a local or recalibration-dependent method and define the failing boundary.
- **RED:** the stack cannot meet its prespecified analytical objective in the intended workflow. Use a matrix-qualified Tier 3 reference method; do not generalize the failure to other electrochemical designs.

**Cost and schedule:** obtain quotes only after the author package, hardware path, GC-MS partner, specimen source, replication design, and ethics requirements are known.

**Cross-references:** [§1.31 culture-supernatant HPLC-UV transfer](#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms), [Tier 2 butyrate assay audit](./tier-2-butyrate-assay-audit-computational.md), [quantification ladder](./quantification-ladder.md), and [matrix-specific open question](./open-questions.md#matrix-specific-assay-gap-for-microbiome-derived-metabolites).

---

### 1.46 PTH1R Agonist → ABCG2 Surface-Trafficking and Urate-Flux

**Status:** Proposed — staged mechanism transfer | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1

**Affected wiki:** [ABCG2 modulators](./abcg2-modulators.md) and [open questions](./open-questions.md).

**What it tests:** Whether abaloparatide reproduces the PTH(1-34)-dependent loss of surface ABCG2 reported by Sugimoto et al. and whether any surface change alters ABCG2-attributed urate flux. The controlled human serum-urate rise does not by itself identify ABCG2, kidney versus intestine, or altered production versus excretion.

**Stage 1 — reproduce the mechanism control:** In polarized Caco-2 cells, reproduce the published PTH(1-34) time/concentration response with inactive PTH(13-34) and vehicle controls. Measure ABCG2 mRNA, total protein, apical-surface protein, barrier integrity, viability, and basolateral-to-apical urate flux. Attribute flux with a qualified ABCG2 loss-of-function or selective-inhibition control.

**Stage 2 — test the new bridge:** Compare measured exposures of abaloparatide and teriparatide in the same system, with PTH1R loss-of-function or blockade. Repeat the advancing condition in a qualified human proximal-tubule model with the same surface-versus-total and urate-flux readouts. Measure other prespecified urate transporters only to resolve a discordant flux result, not as post hoc mechanism fishing.

**Decision rule:** Advance the PTH1R→ABCG2 explanation only if the drug changes surface ABCG2 and ABCG2-attributed urate flux in a PTH1R-dependent direction while total protein, viability, and barrier controls exclude simpler artifacts. A surface change without urate-flux change rejects functional transfer. A flux change without ABCG2 dependence redirects to another transporter or hemodynamic mechanism. A null result narrows this mechanism and exact model; it does not erase the controlled human serum-urate effect.

**Human follow-up:** If the cell mechanism passes, seek appropriately consented stored-trial samples or a prospective monitored study with paired serum urate, urine urate, and creatinine to estimate fractional urate excretion. Serum urate alone cannot localize the mechanism.

**Primary anchors:** Sugimoto et al. 2017 (**In Vitro + Animal Model**; [PMID 27988213](https://pubmed.ncbi.nlm.nih.gov/27988213/)); FDA NDA 208743 and PMDA Ostabalo controlled safety analyses (**Clinical Trial**).

---

### 1.47 Bempedoic Acid → OAT2 Urate-Flux Attribution and Rescue

**Status:** Proposed — human probe localization | **Cost:** TBD | **Weeks:** TBD | **Phase:** 1

**Affected wiki:** [Gout pathophysiology](./gout-pathophysiology.md) and [open questions](./open-questions.md).

**What it tests:** Whether the reproducible serum-urate rise caused by bempedoic acid is materially mediated by loss of OAT2-dependent renal urate secretion. The drug is a positive perturbation control, not a proposed gout intervention. The initial EMA assessment reported strongly substrate-dependent OAT2 inhibition—urate IC50 1.24 µg/mL, creatinine 88.9 µg/mL, and cGMP 142 µg/mL—so creatinine or cGMP cannot substitute for direct urate transport.

**Stage 0 — localize the human phenotype if samples or data exist:** Reanalyse appropriately consented trial data for paired serum urate, urine urate, and creatinine; calculate fractional urate excretion; model bempedoic-acid exposure, baseline urate, kidney function, urate-lowering therapy, and gout history. Add SLC22A7 genotype only if it was collected. A serum-urate-only analysis cannot distinguish secretion, reabsorption, production, or another transporter.

**Stage 1 — reproduce substrate-specific inhibition:** In a human OAT2 expression system, measure bidirectional urate flux across a concentration series covering measured unbound bempedoic-acid exposures. Test parent drug, active metabolite ESP15228, and each glucuronide separately. Run creatinine and cGMP in parallel as substrate-dependence controls, not urate surrogates. Include vehicle, OAT2-null, and rescue controls and prespecify solubility, protein binding, viability, and non-specific permeability limits.

**Stage 2 — establish proximal-tubule attribution:** Repeat the advancing conditions in a qualified human proximal-tubule model with OAT2 knockout and matched rescue. Quantify apical and basolateral urate movement, intracellular urate, OAT2 surface abundance, and cell integrity. Use OAT1/OAT3 perturbations only as prespecified specificity controls.

**Stage 3 — exploit only after attribution:** If OAT2 loss explains a material share of the urate-flux phenotype, screen for interventions that restore OAT2-dependent urate movement or prevent bempedoic-acid inhibition without increasing reabsorption elsewhere. Do not begin a rescue screen after a merely correlative serum-urate or expression result.

**Decision rule:** Advance OAT2 as an exploitable urate-secretion node only if bempedoic acid reduces direct urate flux in an exposure-relevant, OAT2-dependent manner and knockout/rescue reproduces the direction. A substrate-specific effect confined to cGMP or creatinine rejects urate transfer. A human fractional-excretion signal without OAT2 dependence redirects to broader renal handling. A null OAT2 result kills this mechanism attribution, not the controlled human urate phenotype.

**Primary anchors:** Sato et al. 2010 (**In Vitro**; [PMID 20190416](https://pubmed.ncbi.nlm.nih.gov/20190416/)); CLEAR Outcomes (**Clinical Trial**; [PMID 36876740](https://pubmed.ncbi.nlm.nih.gov/36876740/)); [Nilemdo EMA initial assessment](https://www.ema.europa.eu/en/documents/assessment-report/nilemdo-epar-public-assessment-report_en.pdf).

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

### 2.6 GLPP + Cordycepin Interaction in Hyperuricemia — Matched Wet-Lab Gate

**Status**: Proposed — design pending exact material and pilot data | **Cost**: TBD | **Weeks**: TBD | **Phase**: 2

**Affected wiki**: [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md), [medicinal-mushroom-extract-sops](./medicinal-mushroom-extract-sops.md), [medicinal-mushroom-compound-mapping-computational](./medicinal-mushroom-compound-mapping-computational.md), [modality-chokepoint-matrix](./modality-chokepoint-matrix.md)

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

**Cross-references:** the [medicinal-mushroom exact-material conjecture](./medicinal-mushroom-complement-track.md#research-conjecture--a-reproducible-medicinal-fungal-material-may-expose-a-gout-weakness) and the [draft material-identity methods](./medicinal-mushroom-extract-sops.md). COMP-014 is a partial retrieval inventory, not evidence authority for the study.

#### Conditional follow-up — UOX × mushroom interaction arm

**Status**: Conditional conjecture (opens only if §2.6 and §§1.33, 1.36, and 2.1 independently justify it) | **Cost and duration:** TBD from the final model, arm count, variance, and analytical plan

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
- Engineered-koji UOX readiness requires an exact §1.5-built configuration to pass §1.33, reproduce in the §1.9B solid-state context, clear §1.36, and be characterized under §2.1. The lactoferrin cassette and §1.9C dual-cassette result are not required for a UOX-only combination arm. If that sequence is incomplete when §2.6 concludes, this follow-up remains closed; a surrogate must independently clear the same configuration-specific gates before use. No Huynh 2020 “koji-uricase strain” precedent is assumed.
- The final exposure window may still answer only an acute interaction question; chronic durability requires a separate design.
- Model and strain consistency with the qualifying individual-arm studies must be maintained; do not use cross-cohort comparisons as an interaction estimate.

**Cross-references:** [gout-pathophysiology.md §"Multi-track urate transporter coverage"](./gout-pathophysiology.md) (the coverage map this follow-up tests); §2.6 base (parent study); [§1.33](#133-physiological-uox-topology--oxygen--peroxide-factorial) (configuration-level physiological gate); [§1.9](#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate) Stage B (solid-state UOX-only readiness); [§1.36](#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) (pre-animal safety gate); [§2.1](#21-selected-uox-configuration-in-vivo-persistence-and-localization) (configuration-specific in-vivo characterization); [`koji-endgame-strain.md`](./koji-endgame-strain.md) (koji track context).

### 2.7 Koji × *Cordyceps* Co-Formulation Stability Test — ADA-Challenge Assay — **Deprioritized 2026-05-16, archived 2026-05-29**

**Status**: Abandoned — recover from Git only if decision-relevant | **Cost**: N/A (archived) | **Weeks**: N/A (archived) | **Phase**: 2

This experiment is not active. Reconstruct it from Git only if the koji-cordycepin hypothesis becomes decision-relevant again.

---

### 2.8 Exact-Material Androgen × Urate Dual-Axis Validation

**Status**: Proposed — one material/configuration per qualified study | **Cost**: TBD after material and exposure pilot | **Weeks**: TBD | **Phase**: 2

**Affected wiki:** [androgen-natural-modulation](./androgen-natural-modulation.md),
[t-axis-adjuvant urate mapping](./t-axis-adjuvant-urate-mapping-computational.md),
and [PRPS / PRPP supply](./prps-purine-biosynthesis-chokepoint.md).

**What it tests:** Whether one identity-verified material at a measured,
tolerated exposure produces an androgen effect and an independently localized
urate effect in the same study. It does not compare "cordyceps" with "tongkat
ali" as classes, transfer a result among extracts and purified quassinoids, or
infer either mechanism from serum urate alone.

**Entry gates:**

- Lock the exact purified compound or compositionally characterized extract,
  including lot, marker panel, purity or constituent concentrations,
  preparation method, vehicle, stability, and storage.
- Choose a species and disease state capable of answering both prespecified
  axes. Justify the androgen endpoint for that material independently of its
  urate evidence.
- Run a pharmacokinetic and tolerability pilot. Measure the candidate and
  relevant metabolites in the compartments needed by the proposed mechanism;
  do not convert administered dose into assumed exposure.
- Freeze the estimand, clinically or biologically meaningful margins, sample
  size, randomization, blinding, exclusion rules, and safety stops from the
  pilot. Do not inherit COMP-015's ordinal scores or concentration heuristics.

**Candidate-specific design:** Run each exact material as its own study with
healthy and disease controls, matched vehicle, a prespecified exposure range,
and axis-appropriate positive controls. A cross-material comparison is
permitted only if the materials use the same model, schedule, analytical
platforms, and adequately overlapping measured exposures; otherwise report
parallel source-specific results without a rank.

**Readouts:**

- **Identity and exposure:** quantitative material markers, parent/metabolite
  pharmacokinetics, target-tissue exposure, stability, and batch consistency.
- **Androgen axis:** the endpoint implicated by the material's own evidence,
  such as total and free testosterone, SHBG, LH/FSH, estradiol, and
  tissue-specific steroidogenic markers. Select and preregister the primary
  endpoint rather than treating the panel as interchangeable.
- **Urate axis:** serum-urate time course plus urinary and fecal urate mass
  balance. Add direct renal or intestinal URAT1, GLUT9, ABCG2, or NPT1
  function only when that mechanism is prespecified.
- **Production-side localization:** for an eurycomanol study, measure hepatic
  PRPS protein and activity and isotope-resolved purine flux; PRPS expression
  alone is insufficient.
- **Safety:** clinical observations, weight, hematology, liver and renal
  chemistry, histology, and material-specific toxicology.

**Decision rule:** Advance only the exact material–exposure configuration that
meets both prespecified axis margins, shows exposure-consistent target
engagement, localizes the urate change, and clears safety. A favorable androgen
result with null or adverse urate findings fails the dual-axis conjecture for
that configuration. A favorable urate result without the prespecified androgen
effect does the same. A null result kills only the tested material, dose,
formulation, schedule, and model; it does not erase a different source-specific
lead.

**Interpretation limits:** This is an animal validation gate, not a treatment
protocol or human-efficacy claim. It cannot turn Physta's null human urate
comparison into efficacy, assign extract activity to pure eurycomanone, or
establish superiority among unpaired materials.

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
| 1 | Physiological UOX system (§1.33) | Product formation at terminal-ileal clinical-cohort substrate prior | Exact configuration reproducible vs. matched inactive-UOX control, with no prespecified H₂O₂ or viability penalty |
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

- **KHK and fructose-driven urate production:** Can a compositionally verified
  KHK inhibitor reduce fructose-driven ATP depletion, AMP catabolism, and
  urate output at a tolerable measured exposure? This question does not imply
  a production chassis. (Source:
  [fructose-connection.md](./fructose-connection.md))
- **Delivery route optimization:** Is intestinal lumen degradation sufficient, or would systemic absorption of recombinant uricase be superior? (Source: blood-barrier-exploits.md)
- **Microbiome stability:** Will engineered probiotics persist without colonization, or is daily dosing required long-term? (Source: gout-deep-dive.md, Section 8)
- **Gene therapy as alternative:** Should we pursue CRISPR-based uricase gene therapy in parallel? (Source: gout-deep-dive.md, Section 6)

---

*Research protocols only. Human translation requires appropriate oversight and cannot be inferred from computational, cell, animal, or n=1 results.*
