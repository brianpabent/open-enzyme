---
title: Practitioner Toolkit — Observation, Measurement, and Rigor Disciplines
date: 2026-05-07
tags: [practitioner-toolkit, observation, measurement, rigor, index]
related:
  - ../self-experiment-protocol.md
  - ../personal-genome-protocol.md
  - ../koji-home-fermentation.md
  - ../enzyme-quantification-protocol.md
  - manual-literature-mining.md
  - autonomous-screening-methodology.md
  - ../quantification-ladder.md
sources:
  - "Picolab v2 GitHub repository: https://github.com/OmkarKovvali/picolab_v2"
---

# Practitioner Toolkit

Methods for separating personal observations, low-cost measurement capabilities, and research-quality evidence. This toolkit does not turn an observation or accessible assay into a treatment protocol.

## Three-tier structure

1. **[N-of-1 observations](#self-experiments-n1)** — structured records of direct observations; useful for generating study variables, not population or treatment claims.
2. **[Measurement capability builds](#diy-capability-builds)** — low-cost research measurements. A capability build does not authorize ingestion, organism construction, or clinical use.
3. **[Rigor Disciplines](#rigor-disciplines-cross-cutting)** — literature mining, evidence verification, falsification, and AI-discovery controls that apply across research modes.

## Self-Experiments (n=1)

Structured n=1 records can improve timing, endpoint, and confounder choices for later studies. They do not establish safety, causality, dose, or efficacy.

- **[`self-experiment-protocol.md`](../self-experiment-protocol.md)** — biomarker monitoring framework: blood panels (CBC / CMP / UA / hs-CRP / LDH / HbA1c), 16S stool, daily diary, red-flag halt criteria; specialty biomarkers (C3 / C4 / CH50 / C5a CP0; urinary LTE4 CP6a)
- **[`personal-genome-protocol.md`](../personal-genome-protocol.md)** — kitchen-table sequencing as both personal genome project AND Open Enzyme strain-QC infrastructure; gout pharmacogenomic query list (HLA-B*58:01, ABCG2 Q141K, SLC2A9, URAT1, PDZK1, MEFV)
- **PERT-timing self-experiment** (April 2026 → ongoing) — a direct, single-subject record involving a commercial digestive-enzyme product, documented in [`digestive-enzyme-optimization.md`](../digestive-enzyme-optimization.md). It describes only the product, subject, meals, timing, and outcomes actually observed. It does not establish timing, formulation, manufacturing process, dose, efficacy, or safety for an engineered UOX or koji platform.

## DIY Capability Builds

Minimal-equipment research procedures. Some can support bench measurements for engineered-strain research; none is a personal-consumption protocol for an engineered strain.

- **[`koji-home-fermentation.md`](../koji-home-fermentation.md)** — wild-type food-fermentation reference. It may supply a process baseline for non-engineered koji, but it is not an ingestion or production protocol for engineered UOX material.
- **[`enzyme-quantification-protocol.md`](../enzyme-quantification-protocol.md)** — tiered methods for measuring amylase / protease / lipase activity (kitchen → smartphone colorimetry → community-college bench → outsourced contract assay).
- **[`engineered-koji-protocol.md`](../engineered-koji-protocol.md)** — engineering-stage construct, strain-QC, expression, and assay plan for *A. oryzae*. Its outputs require identity, containment, activity, coproduct, and safety evaluation; they are not for routine or personal consumption.
- **[`medicinal-mushroom-extract-sops.md`](../medicinal-mushroom-extract-sops.md)** — planned extract characterization SOPs (GLPP, cordycepin, ergothioneine); operator-independent reproducibility tolerances.
- **Low-cost liquid-handling automation (Picolab prior art, 2026-05-19).** [Picolab v2](https://github.com/OmkarKovvali/picolab_v2) is an MIT-licensed prototype that repurposes an Ender-style printer gantry into a syringe liquid handler with a FastAPI backend, React dashboard, G-code motion planner, calibration store, camera-assisted OpenAI agent workspace, and operator approval gate before hardware execution. For Open Enzyme, this belongs in the capability-build lane: plausible infrastructure for repeatable tube-scale colorimetric assays, serial dilutions, and [`quantification-ladder.md`](../quantification-ladder.md) Tier 2/3 method development. It is not a sterile, clinical, or production liquid handler. Dedicated page threshold: create `low-cost-lab-automation.md` only after there is OE-specific analysis of bill of materials, positional/volume accuracy, contamination controls, assay compatibility, and first automatable protocols. (Engineering prior art; source: Picolab v2 repository)
- **Sequencing capability** (sub-bucket of [`personal-genome-protocol.md`](../personal-genome-protocol.md)) — candidate infrastructure for research-genome analysis and construct-identity verification. Clinical interpretation requires a clinically validated assay; engineered-strain release requires the applicable controlled QC system.

## Rigor Disciplines (cross-cutting)

Methodology that applies to wet-lab, computational, literature, and n-of-1 observation work.

- **[`manual-literature-mining.md`](./manual-literature-mining.md)** — five-rule protocol for safe LLM literature use (safe primitives only, anchor to meta.json, grep-verify all numbers, never propagate map / reduce summaries, cite line-anchored). Surfaced 2026-05-05 after documented Paperclip `map` operator hallucination.
- **[`chembl-cross-check.md`](./chembl-cross-check.md)** — quarterly ChEMBL v34 cross-reference of stack compounds; separates direct-inhibitor claims from pathway-modulator claims (e.g., quercetin → 5-LOX, not NLRP3).
- **[`linter-design.md`](../linter-design.md)** — two-linter architecture (Document Lint always-on; Falsification Lint on-demand per-hypothesis with killshot menus, failure-mode ontology, survival scoring).
- **[`tcm-modern-rigor-intersection.md`](../tcm-modern-rigor-intersection.md)** — six-rule methodology for evidence-leveling traditional-medicine claims (chokepoint mapping, ChEMBL cross-check, bioavailability-honest framing, formula decomposition, standardized-extract specification, falsification-card discipline).
- **[`autonomous-screening-methodology.md`](./autonomous-screening-methodology.md)** — peer-track methodology page on ClockBase Agent (Ying et al. bioRxiv v3, late 2025 / early 2026); transferable patterns for comp-NNN: search-space sizing, composite-score ranking across orthogonal predictors, hypothesis-then-verify, autonomy boundary, N-of-M concordance for wet-lab handoff.
- **[`cross-validation.md`](../cross-validation.md)** — thesis stress-test discipline; risk matrix across all tracks; identifies true blockers vs. surmountable obstacles.

## Section conventions

- **Evidence-level discipline applies.** Use the standard wiki tags (Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation). An n=1 observation is useful for generating study variables, not for population, safety, dose, or treatment claims.
- **Privacy-by-default.** Self-experiment data is private unless explicitly published. Genetic data in particular is governed by the privacy gradient in [`personal-genome-protocol.md`](../personal-genome-protocol.md).
- **Project crossover where applicable.** Sequencing and enzyme-assay capabilities may support platform measurements. Direct observations from commercial PERT use do not transfer a dose, timing rule, formulation, process, efficacy signal, or safety conclusion to engineered UOX.
- **Pre-commit grep-verify gate** ([CLAUDE.md §4](../../CLAUDE.md)) applies to load-bearing numbers in all three sub-buckets equally.

## Open questions

- Which low-cost measurements remain reproducible after blinded comparison with a reference laboratory?
- Which observations are useful enough to justify a controlled study, and which are too confounded to carry forward?
- Which capability gaps require a partner laboratory rather than an independent setup? Mammalian cell culture, pathogen work, engineered-organism production, and clinical testing require appropriate facilities, oversight, and containment.
