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
  - etc/manual-literature-mining.md
  - etc/open-source-platform.md
  - etc/open-enzyme-vision.md
sources:
  - "Brian framing 2026-05-06: 'pull in all of the known compounds from as many species as possible and then map that to our chokepoints... whether that's directly in the body or, who knows, something else like helping disulfides'"
  - "Open Enzyme/CLAUDE.md §Global-multilingual research by default — corpus must include CNKI, Wanfang, J-STAGE, KISS — non-English sources are not 'language barrier'"
  - "Open Enzyme/CLAUDE.md §Translation protocol — two-model independent cross-check with inline disagreement annotations for non-English source ingestion"
  - "comp-013 TCM gout compound triage — established the ChEMBL coverage gap pattern for non-Western-pharma compounds; same gap applies to fungi"
  - "wiki/modality-chokepoint-matrix.md — canonical chokepoint inventory used as the right-hand side of the mapping"
status: Phase 2 partial + Phase 3 complete (Phase 4 re-run); Phase 5+ queued
---

# Medicinal Mushroom Compound × Chokepoint Mapping — Computational Analysis (comp-014)

> **Frozen analysis archived to [`./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/wiki-archive.md`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/wiki-archive.md)** (248 lines).
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `etc/experiments/comp-014-medicinal-mushroom-compound-mapping/`.

## Phase status

| Phase | What ran | When | Status |
|---|---|---|---|
| 1 | Scope: chokepoint targets, anchor species, toxicity filter, data-source inventory, multilingual literature plan | 2026-05-06 | Complete |
| 2 | Breadth aggregation across LOTUS + NPAtlas + KNApSAcK (NPASS / TCMSP / HIT unreachable from sandbox — documented gap with re-run plan) | 2026-05-06 + 2026-05-17 | **Partial** (3 of 6 planned DBs pulled) |
| 3 | Target mapping: ChEMBL `activity.json` per chokepoint UniProt → InChIKey intersection across 24 chokepoint targets, 26,830 unique ChEMBL molecules resolved, 323 (compound × chokepoint) empirical hits | 2026-05-17 | **Complete** for ChEMBL-empirical; SwissTargetPrediction prediction layer NOT RUN (sandbox-blocked, deferred) |
| 4 (v2) | Re-run chokepoint intersection on the unified compound table (9,778 compounds vs. the LOTUS-only 6,798 from Phase 2b) | 2026-05-17 | Complete |
| 5 | Multilingual literature deep-dive (CNKI / Wanfang / J-STAGE / KISS with two-model translation cross-check) per Phase 4 chokepoint-hit species | — | Queued |
| 6 | Per-compound triage (comp-013-style IC50 occupancy + composite scoring) on Phase 4 candidates | — | Queued |

## Phase 2 unified table — what's in / what's out

- **Total unique compounds (deduped by InChIKey):** 9,778 (up from LOTUS-only 6,798)
- **By source:** LOTUS 6,798 · NPAtlas 4,535 · KNApSAcK 20 (InChIKey-resolved subset of 398 raw records; PubChem InChIKey resolution wall-time-capped at 60 s per run)
- **Toxicity-pass:** 9,747 compounds (after FDA GRAS / EFSA QPS / pharmacopoeia / clinical-trial inclusion + WHO 2022 / mycotoxin / Schedule I/II exclusion per `inputs/toxicity-filter.json`)
- **Hard-excluded:** 31 compounds (mostly *Aspergillus fumigatus* + *Stachybotrys chartarum* + *Penicillium expansum* mycotoxin producers)
- **Anchor-species sanity check:** all 18 anchor species from `inputs/phase-5-anchor-species.json` resolve in the unified table (passed)

## Phase 2 database-coverage gap (NPASS / TCMSP / HIT / SwissTargetPrediction)

Three East-Asian-hosted compound DBs and the SwissTargetPrediction prediction service were **not** reachable from the comp-014 execution sandbox on 2026-05-17:

| DB | Endpoint probed | Status | Re-run plan |
|---|---|---|---|
| NPASS | `bidd.group/NPASS/` | 200 once, then `000` (intermittent) | Retry from non-sandboxed environment; prefer bulk-CSV download (`NPASSv2.0_download_naturalProducts*.txt`) |
| TCMSP | `old.tcmsp-e.com/tcmsp.php` | 502 Bad Gateway; alternate hosts unreachable | Retry via BATMAN-TCM-2 endpoints (TCMSP folded into BATMAN-TCM-2) or Mendeley Data bulk archive |
| HIT | `hit2.badd-cao.net` and `badd-cao.net` | 000 timeout (both) | Download HIT 2.0 Excel file per upstream paper PMID 35136829 |
| SwissTargetPrediction | `swisstargetprediction.ch` POST endpoint | Not verified accessible from sandbox | Batch the target-orphan compound subset (~98% of the table) through POST API in connected environment |

The LOTUS-only Phase 2 outputs are not wrong, just incomplete. The unified table here is LOTUS + NPAtlas + KNApSAcK. The East-Asian-DB gap is documented and slated for re-run; do not over-interpret the absence of NPASS/TCMSP/HIT-only compounds as "no evidence."

## Phase 3 — target mapping headline findings

**323 empirical (compound × chokepoint) hits** across 24 chokepoint targets, after toxicity filter. Coverage:

- Compounds with ≥1 empirical chokepoint hit: **177 of 9,778 (1.81%)**
- Target-orphan compounds (no ChEMBL activity at any of the 24 chokepoints): **9,601 (98.19%)** — Phase 3 SwissTargetPrediction layer is the load-bearing next step for closing this gap
- Empty chokepoints (zero ChEMBL fungal-compound hits in this corpus): GLUT9, NLRP3, ASC, C5aR1, Lp-PLA2, KEAP1, OAT4, PINK1, PDI, PDIA3, TXN, TXNIP — twelve of 24 chokepoints have no fungal-source small molecule in ChEMBL with measurable activity at the target

**Top empirical findings (potency-ranked, toxicity-pass only):**

1. **Ganoderic acid H** / *Ganoderma lucidum* — **TNFα Kd = 2.45 nM** (pChEMBL 8.61, ChEMBL1922178, 2014). The highest-potency single-compound × chokepoint hit in the entire breadth pass. Multiple stereoisomer / numbered-position variants of the same scaffold cluster at this Kd. *Ganoderic acid D* hits TNFα at Kd 8.39 nM (pChEMBL 8.08).
2. **Berkeleyamides A and D** / *Penicillium* — **CASP1 IC50 = 330 / 610 nM** (pChEMBL 6.48 / 6.21, ChEMBL466565 / CHEMBL466747, 2008). The highest-potency direct caspase-1 fungal natural-product hits — distinct from the inflammasome-priming literature, this is direct effector-caspase inhibition.
3. **Berkeleyones A / B / C** / *Penicillium* — **IL-1β IC50 = 2.7 / 3.7 / 37.8 μM** (pChEMBL 5.57-4.42, 2011). Modest potency but a direct IL-1β fungal-source hit.
4. **Quercetin** / *Agaricus* — **ABCG2 EC50 = 30 nM** (pChEMBL 7.52, ChEMBL50, 2018). Plant-origin flavonoid that accumulates in mushroom substrates; the most-potent ABCG2 hit in the corpus.
5. **Ellagic acid** / *Penicillium* / *Phellinus* — **OAT1 IC50 = 270 nM** (pChEMBL 6.57, 2005). Fungal-source organic anion transporter modulator.

**Multi-chokepoint compounds** (≥2 chokepoints hit, suggesting platform-level rather than single-target mechanism):

- **bois d'arc / morin** (ChEMBL28626, *Ganoderma*): 4 chokepoints — ABCG2, CASP1, URAT1, XO
- **genistein** (ChEMBL44, *Cordyceps sinensis*, *Ophiocordyceps*): 4 chokepoints — ABCG2, CASP1, PPARG, XO
- **Quercetin** (ChEMBL50, *Agaricus*): 2 chokepoints — ABCG2, XO
- **Daidzein** (*Hericium*, *Cordyceps sinensis*): 2 chokepoints — NRF2, XO
- **Disulfiram** (*Coprinopsis*): 2 chokepoints — CASP1, NRF2

The "fungal-source" attribution for plant-origin flavonoids (quercetin, genistein, daidzein) reflects accumulation in mushroom substrates rather than fungal biosynthesis; see Phase 4 caveats.

## Phase 3 implications for Phase 2 narrative

The Phase 2 LOTUS-only headline — Ganoderma applanatum 2,4-DAE as "strongest single-compound finding" — was correct as far as the LOTUS × PubMed pull went, but the unified ChEMBL intersection surfaces a **substantially higher-potency direct hit**: ganoderic acid H at TNFα Kd 2.45 nM. The 2,4-DAE finding is a (different, animal-model in vivo) Ganoderma applanatum hit at the urate axis (XO + URAT1); ganoderic acid H is a Ganoderma lucidum direct-binding finding at the cytokine axis (TNFα). Both belong in the candidate set; the breadth pass argues for taking *Ganoderma* triterpenoids more seriously across two distinct chokepoint axes, not just one.

The Phase 2 cordycepin → URAT1 finding (PMID 29422889, animal model) is preserved — ChEMBL has no direct cordycepin × URAT1 record. PubMed-derived in-vivo animal-model evidence and ChEMBL-derived in-vitro biochemical-assay evidence are complementary, not redundant.

## Where the analysis lives

- Phase 3 reproducibility script: [`./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/scripts/phase_3_target_mapping.py`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/scripts/phase_3_target_mapping.py)
- Phase 2 unified table: [`./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-2-unified-fungal-compounds.json`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-2-unified-fungal-compounds.json) + [summary](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-2-unified-summary.md)
- Phase 3 compound × target table: [`phase-3-compound-x-target.json`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-3-compound-x-target.json) + [summary](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-3-target-mapping-summary.md)
- Phase 4 v2 intersection (re-run on unified table): [`phase-4-chokepoint-intersection-v2.json`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-4-chokepoint-intersection-v2.json)
- Earlier Phase 2 findings (LOTUS-only, 2026-05-06): [`PHASE-2-FINDINGS.md`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/PHASE-2-FINDINGS.md)
- Full archived analysis: [`wiki-archive.md`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
