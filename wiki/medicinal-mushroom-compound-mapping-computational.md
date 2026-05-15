---
title: "Medicinal Mushroom Compound × Chokepoint Mapping — Computational Analysis (comp-014)"
date: 2026-05-06
tags:
  - medicinal-mushrooms
  - fungi
  - natural-products
  - chokepoint-mapping
  - breadth-aggregation
  - global-multilingual
  - computational
  - lotus
  - npatlas
  - knapsack
  - tcmsp
  - hit
  - mibig
  - antismash
  - ergothioneine
  - redox-disulfide
  - peer-track
  - scope-page
related:
  - computational-experiments.md
  - modality-chokepoint-matrix.md
  - tcm-modern-rigor-intersection.md
  - tcm-gout-compound-triage-computational.md
  - nlrp3-exploit-map.md
  - complement-c5a-gout.md
  - abcg2-modulators.md
  - manual-literature-mining.md
  - open-source-platform.md
  - open-enzyme-vision.md
sources:
  - "Brian framing 2026-05-06: 'pull in all of the known compounds from as many species as possible and then map that to our chokepoints... whether that's directly in the body or, who knows, something else like helping disulfides'"
  - "Open Enzyme/CLAUDE.md §Global-multilingual research by default — corpus must include CNKI, Wanfang, J-STAGE, KISS — non-English sources are not 'language barrier'"
  - "Open Enzyme/CLAUDE.md §Translation protocol — two-model independent cross-check with inline disagreement annotations for non-English source ingestion"
  - "comp-013 TCM gout compound triage — established the ChEMBL coverage gap pattern for non-Western-pharma compounds; same gap applies to fungi"
  - "wiki/modality-chokepoint-matrix.md — canonical chokepoint inventory used as the right-hand side of the mapping"
status: scoped — Phase 1 only
---

# Medicinal Mushroom Compound × Chokepoint Mapping — Computational Analysis (comp-014)

> **Frozen analysis archived to [`../experiments/comp-014-medicinal-mushroom-compound-mapping/wiki-archive.md`](../experiments/comp-014-medicinal-mushroom-compound-mapping/wiki-archive.md)** (248 lines).
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `experiments/comp-014-medicinal-mushroom-compound-mapping/`.

**Phase 1 (Scope) — Committed 2026-05-06.** Phases 2–6 are queued, not executed. This page documents the scope and the rationale for the multi-phase plan; it is NOT a results page. Per Open Enzyme convention, this page will be revised in place when each subsequent phase lands, with a status promotion (`scoped` → `in progress` → `complete`) tracked in the YAML frontmatter and the [`computational-experiments.md`](./computational-experiments.md) tracking index.

**Where the analysis lives:**
- Full archived analysis: [`../experiments/comp-014-medicinal-mushroom-compound-mapping/wiki-archive.md`](../experiments/comp-014-medicinal-mushroom-compound-mapping/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`../experiments/comp-014-medicinal-mushroom-compound-mapping/`](../experiments/comp-014-medicinal-mushroom-compound-mapping/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
