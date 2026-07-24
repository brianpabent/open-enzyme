---
id: H03
title: "Selective kidney delivery could make URAT1 siRNA a long-horizon gout modality"
committed: 2026-05-05
status: Stub
survival_count: 0
tags:
  - hypothesis
  - sirna
  - urat1
  - slc22a12
  - kidney-tropic-delivery
  - megalin
  - inclisiran
  - benzbromarone
  - discovery-engine
  - long-horizon
related:
  - ../sirna-urat1-modality.md
  - ../modality-chokepoint-matrix.md
  - ../gout-pathophysiology.md
  - ../androgen-urate-axis.md
  - ../engineered-lbp-chassis.md
  - ../open-questions.md
  - ./H01-ward-dual-cassette.md
  - ./H02-engineered-lbp-thesis.md
  - ./README.md
sources:
  - "Inclisiran (Alnylam / Novartis, FDA approved 2021) — GalNAc-ASGPR liver-targeted siRNA precedent"
  - "Patisiran (Alnylam, FDA approved 2018) — LNP-delivered siRNA precedent"
  - "Pozdeutinurad / AR882 (Arthrosi) — Phase 3 small-molecule URAT1 inhibitor competitive context"
  - "Benzbromarone — withdrawn URAT1 inhibitor; off-target metabolite hepatotoxicity precedent that motivates the siRNA approach"
  - "Megalin (LRP2) — multi-ligand endocytic receptor enriched on renal proximal tubule; leading kidney-tropic conjugate target"
---

# H03 — siRNA / URAT1 Discovery-Engine Output Thesis (Stub)

> **Evidence status:** stub. Assumptions, pre-committed thresholds, kill switches, and failure-mode coverage remain incomplete; see [siRNA / URAT1](../sirna-urat1-modality.md).
>
> The pre-registration note on H01 ([H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) §Pre-registration) does not apply until this stub is upgraded to a full card. When the upgrade happens, the upgraded version is what gets pre-registered; the stub is informational scaffolding only.

---

## Claim (provisional, stub-level)

> **Research conjecture — Selective kidney delivery could make URAT1 siRNA useful**{ .research-conjecture-label }
>
> **Grounded premises:** URAT1 is an established renal urate-reabsorption pharmacology target (**Clinical Trial**; evidence map: [gout pathophysiology](../gout-pathophysiology.md)). Liver-targeted inclisiran and patisiran establish human RNAi-delivery precedents (**Clinical Trial**; [DOI 10.1056/NEJMoa1912387](https://doi.org/10.1056/NEJMoa1912387), [DOI 10.1056/NEJMoa1716153](https://doi.org/10.1056/NEJMoa1716153)). An oligonucleotide would not generate benzbromarone's reactive small-molecule metabolites, but it has different sequence, immune, formulation, biodistribution, reversibility, and renal-hypouricemia risks.
>
> **Novel leap:** A selectively delivered, off-target-cleared siRNA might reduce URAT1 in human proximal-tubule cells enough to improve urate handling with a useful safety and dosing profile. No direct study tests that complete chain.
>
> **Why it matters:** If the chain holds, URAT1 could be attacked with a modality whose exposure and duration differ from oral inhibitors.
>
> **Discriminating observation:** First identify a selective human proximal-tubule entry route, then require transcriptome-wide guide clearance, intracellular URAT1 knockdown, urate-transport change, dose-response, reversibility, and renal and immune safety.

This vector is positioned as a **discovery-engine output** (per [`open-enzyme-vision.md`](../etc/open-enzyme-vision.md) §2.2), not a strain-library output. The thesis is that Open Enzyme contributes mechanistic clarity, target validation, and design rationale — partner companies, academic groups, or future spinouts execute the development.

---

## Assumption Stack (placeholder — to be populated in Phase 2 P2-5)

The full assumption stack will be populated after the Phase 2 delivery, commercial, competitive, and regulatory work lands. Anticipated load-bearing assumptions, to be confirmed:

1. A validated, off-target-cleared siRNA can knock down relevant SLC22A12 transcripts across the intended human population. This remains unresolved and downstream of delivery: [COMP-009 is invalid](../urat1-sirna-target-site-selection-computational.md) and supplies no guide or tractability evidence.
2. A delivery architecture can reach the relevant human proximal-tubule cells selectively enough for a therapeutic window.
3. The selected route supports internalization and cytosolic guide activity rather than uptake without productive silencing.
4. Liver-targeted siRNA durability transfers sufficiently to the selected renal-cell and formulation context; the dosing interval remains unmeasured.
5. Partial URAT1 knockdown produces a useful urate-transport effect without a knockout-equivalent renal-hypouricemia phenotype; neither the target knockdown nor the safety ceiling is established.
6. The measured efficacy, safety, reversibility, convenience, and cost profile remains competitive with contemporary small-molecule URAT1 inhibition.

---

## Killshot Menu (placeholder — to be populated in Phase 2 P2-5)

The full killshot menu will follow the H01 / H02 template: ranked by `score = (kill_pr × info_weight) / (cost × time_penalty)`, with each killshot tagged to specific assumptions and failure modes per [linter-design.md](../linter-design.md) §4–5.

Anticipated highest-priority killshots:

- **Lit scan first.** P2-1 (conjugate chemistry state-of-the-art) and P2-3 (commercial landscape) are the cheapest possible upstream moves. They answer whether the kidney-tropic delivery problem is being actively solved by competent groups (validation) or has been quietly stalled / abandoned (kill).
- **COMP-048 proximal-tubule delivery-handle screen.** If no sufficiently selective, accessible, and plausibly internalizing human proximal-tubule surface handle survives, receptor-targeted delivery loses its current entry hypothesis. That negative result would not kill other delivery architectures.
- **Conditional guide-design gate.** Only after a delivery route survives, use a validated current pipeline with relevant transcript and variation coverage plus transcriptome-wide off-target analysis, then require empirical URAT1 knockdown. [COMP-009](../urat1-sirna-target-site-selection-computational.md) supplies no surviving guide, rank, or availability verdict.
- **Current URAT1-therapy comparison.** Re-run the clinical, regulatory, safety, convenience, and cost comparison when delivery and guide evidence exist. The siRNA route loses priority if it cannot offer a measured advantage over the then-current standard.
- **Kidney-delivery program read.** Track clinical and discontinued kidney-targeted RNA programs with exact failure attribution. Repeated delivery-chemistry failures would weaken the route; failures caused by another payload or indication would not adjudicate URAT1 siRNA.

---

## Pre-Committed Thresholds (placeholder — to be populated in Phase 2 P2-5)

To be defined when the killshot menu is populated. Anticipated structure follows H01: declared Alive / Killed / Pending thresholds for delivery selectivity, productive uptake, guide specificity, URAT1 knockdown, urate transport, renal and immune safety, reversibility, durability, and competitive value. No maturation timeline, dose ceiling, or dosing interval is precommitted without evidence.

---

## Failure Modes Probed (placeholder — to be populated in Phase 2 P2-5)

To be populated. Anticipated relevant failure modes from [linter-design.md](../linter-design.md) §5: published-literature gap, species-to-human translation, receptor-expression or localization mismatch, uptake without cytosolic delivery, sequence and seed off-targets, innate-immune or formulation toxicity, insufficient knockdown at tolerated exposure, excessive uricosuria or renal hypouricemia, poor reversibility, and competitive displacement by small-molecule URAT1 inhibitors.

---

## Status

**Stub.** No killshot executed. No assumption stack pre-registered. Full hypothesis card is queued as Phase 2 P2-5 — see [sirna-urat1-modality.md § Falsification program](../sirna-urat1-modality.md#falsification-program).

**Survival count:** 0.

**Survival score:** 0.0 (undefined until full card and first survived killshot).

---

## Cross-References

- [sirna-urat1-modality.md](../sirna-urat1-modality.md) — the track this hypothesis formalizes
- [modality-chokepoint-matrix.md](../modality-chokepoint-matrix.md) — siRNA / ASOs row that surfaced this question (#1 open exploration vector)
- [gout-pathophysiology.md](../gout-pathophysiology.md) §"URAT1 (SLC22A12) — THE REABSORPTION VILLAIN" — URAT1 mechanism background
- [androgen-urate-axis.md](../androgen-urate-axis.md) — androgen–urate evidence and the unresolved effect of hormone state on SLC22A12 expression and knockdown response
- [engineered-lbp-chassis.md](../engineered-lbp-chassis.md) — sister peer-track exploration vector (commercial-pharma, durable-colonization angle)
- [open-enzyme-vision.md](../etc/open-enzyme-vision.md) §2.2 (discovery-engine outputs / repurposing surface)
- [open-questions.md](../open-questions.md) — meta-index entry
- [linter-design.md](../linter-design.md) — schema for the Falsification Card format
- [H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) — sibling falsification card for the koji chassis
- [H02-engineered-lbp-thesis.md](./H02-engineered-lbp-thesis.md) — sibling falsification card for the LBP chassis peer track
