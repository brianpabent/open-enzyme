---
title: Practitioner Toolkit — Self-Experiments, DIY-Bio, Rigor Disciplines
date: 2026-05-07
tags: [practitioner-toolkit, self-experiments, DIY-bio, rigor, index, kitchen-table]
related:
  - self-experiment-protocol.md
  - personal-genome-protocol.md
  - koji-home-fermentation.md
  - enzyme-quantification-protocol.md
  - manual-literature-mining.md
  - autonomous-screening-methodology.md
sources: []
---

# Practitioner Toolkit

Section umbrella for the practitioner-side wiki: how a single researcher (institutional or independent) works rigorously at kitchen-table or personal scale. Three sub-buckets, each with a distinct character.

## Three-tier structure

1. **[Self-Experiments](#self-experiments-n1)** — n=1 personal protocols + active in-progress experiments. Brian doing things on himself, with discipline.
2. **[DIY Capability Builds](#diy-capability-builds)** — kitchen-table / home / minimal-equipment procedures that **enable** self-experimentation (and, in several cases, double as Open Enzyme platform infrastructure).
3. **[Rigor Disciplines](#rigor-disciplines-cross-cutting)** — cross-cutting methodology that applies to all research modes: literature mining, evidence verification, falsification, AI-driven-discovery prior art. Pages live in their topical homes elsewhere on the wiki; cross-linked here.

## Self-Experiments (n=1)

Personal protocols and in-progress n=1 work.

- **[`self-experiment-protocol.md`](./self-experiment-protocol.md)** — biomarker monitoring framework: blood panels (CBC / CMP / UA / hs-CRP / LDH / HbA1c), 16S stool, daily diary, red-flag halt criteria; specialty biomarkers (C3 / C4 / CH50 / C5a CP0; urinary LTE4 CP6a)
- **[`personal-genome-protocol.md`](./personal-genome-protocol.md)** — kitchen-table sequencing as both personal genome project AND Open Enzyme strain-QC infrastructure; gout pharmacogenomic query list (HLA-B*58:01, ABCG2 Q141K, SLC2A9, URAT1, PDZK1, MEFV)
- **PERT-timing self-experiment** (April 2026 → ongoing) — BoulderBio dose/timing n=1; documented inline in [`digestive-enzyme-optimization.md`](./digestive-enzyme-optimization.md). Splits dose-finding from formulation question for the engineered-platform endgame.

## DIY Capability Builds

Kitchen-table / minimal-equipment procedures. Several of these double as platform infrastructure for the engineered-strain library.

- **[`koji-home-fermentation.md`](./koji-home-fermentation.md)** — wild-type small-batch koji protocol (koji-kin → koji rice → shio-koji / amazake); pre-engineering baseline + n=1 trial bed for the EPI co-target.
- **[`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md)** — tiered methods for measuring amylase / protease / lipase activity (kitchen → smartphone colorimetry → community-college bench → outsourced contract assay).
- **[`engineered-koji-protocol.md`](./engineered-koji-protocol.md)** — engineering-stage protocol for *A. oryzae* multi-enzyme fermentation; bridges DIY-bio capability into platform engineering.
- **[`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md)** — planned extract characterization SOPs (GLPP, cordycepin, ergothioneine); operator-independent reproducibility tolerances.
- **Sequencing capability** (sub-bucket of [`personal-genome-protocol.md`](./personal-genome-protocol.md)) — MinION + Dorado + Flye / Clair3 pipeline for personal genome AND CRISPR integration verification, off-target indel screening, plasmid validation, released-strain genome QC.

## Rigor Disciplines (cross-cutting)

Methodology that applies to **all** research modes — wet-lab, computational, literature, and self-experiment alike. Pages live in their topical homes elsewhere; cross-linked here for discoverability.

- **[`manual-literature-mining.md`](./manual-literature-mining.md)** — five-rule protocol for safe LLM literature use (safe primitives only, anchor to meta.json, grep-verify all numbers, never propagate map / reduce summaries, cite line-anchored). Surfaced 2026-05-05 after documented Paperclip `map` operator hallucination.
- **[`chembl-cross-check.md`](./chembl-cross-check.md)** — quarterly ChEMBL v34 cross-reference of stack compounds; separates direct-inhibitor claims from pathway-modulator claims (e.g., quercetin → 5-LOX, not NLRP3).
- **[`linter-design.md`](./linter-design.md)** — two-linter architecture (Document Lint always-on; Falsification Lint on-demand per-hypothesis with killshot menus, failure-mode ontology, survival scoring).
- **[`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md)** — six-rule methodology for evidence-leveling traditional-medicine claims (chokepoint mapping, ChEMBL cross-check, bioavailability-honest framing, formula decomposition, standardized-extract specification, falsification-card discipline).
- **[`autonomous-screening-methodology.md`](./autonomous-screening-methodology.md)** — peer-track methodology page on ClockBase Agent (Ying et al. bioRxiv v3, late 2025 / early 2026); transferable patterns for comp-NNN: search-space sizing, composite-score ranking across orthogonal predictors, hypothesis-then-verify, autonomy boundary, N-of-M concordance for wet-lab handoff.
- **[`cross-validation.md`](./cross-validation.md)** — thesis stress-test discipline; risk matrix across all tracks; identifies true blockers vs. surmountable obstacles.

## Section conventions

- **Evidence-level discipline applies.** Every personal-protocol claim gets the standard wiki tagging (Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation). n=1 is its own evidence level — useful for personal-protocol decisions, weak for population claims.
- **Privacy-by-default.** Self-experiment data is private unless explicitly published. Genetic data in particular is governed by the privacy gradient in [`personal-genome-protocol.md`](./personal-genome-protocol.md).
- **Project crossover where applicable.** Several self-experiment / DIY-bio capabilities (sequencing, fermentation, enzyme assays) double as Open Enzyme platform infrastructure. Pages flag this crossover explicitly.
- **Pre-commit grep-verify gate** ([CLAUDE.md §4](../CLAUDE.md)) applies to load-bearing numbers in all three sub-buckets equally.

## Open questions

- **Promote to a `wiki/practitioner-toolkit/` subfolder?** Currently 2 LIVE pages in Self-Experiments, 4–5 in DIY Capability Builds, 6 cross-linked in Rigor Disciplines. Promote when the LIVE count exceeds ~10 and the flat structure becomes unwieldy.
- **Pharmacogenomic priors → self-experiment monitoring.** Should findings from `personal-genome-protocol.md` feed `self-experiment-protocol.md` as priors? (e.g., "ABCG2 Q141K homozygote → blunted allopurinol response → adjust biomarker monitoring cadence.") Likely yes; integration not yet drafted.
- **Compound self-trial sub-bucket.** Once the first compound self-trial protocol is written, add a sub-bucket inside Self-Experiments. Candidates from the existing wiki: BHB / ketogenic-state, butyrate, theaflavins, KPV, BPC-157.
- **DIY-bio capability gaps.** What's missing? Likely candidates: home tissue culture (Caco-2 / HepG2 for permeability + HDAC activity assays); home Western blot equivalent (smartphone-based dot blot? lateral flow strip protocol?); home ELISA equivalent for IL-1β / hs-CRP. Each would unlock a tier of comp-NNN follow-ups.

## Why this section exists

Open Enzyme is, structurally, a single-researcher project (Brian as platform / engineering, three PhD-level collaborator roles being recruited per [`team.md`](./team.md)). The practitioner toolkit is what lets that scale stay rigorous: explicit personal protocols with halt criteria, capability builds that work at kitchen-table scale, and rigor disciplines that prevent single-operator failure modes (hallucination, post-hoc rationalization, evidence-level slippage). The three tiers reinforce each other.
