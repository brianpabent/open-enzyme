---
id: H02
title: "Engineered *Faecalibacterium prausnitzii* delivering colonic butyrate is a testable peer-track chassis for WT-ABCG2 induction; Q141K rescue remains unvalidated"
committed: 2026-05-05
status: Stub
survival_count: 0
tags:
  - hypothesis
  - engineered-lbps
  - faecalibacterium-prausnitzii
  - butyrate
  - abcg2
  - q141k
  - durable-colonization
  - regulatory-lbp
  - peer-track
related:
  - ../engineered-lbp-chassis.md
  - ../modality-chokepoint-matrix.md
  - ../abcg2-modulators.md
  - ../koji-endgame-strain.md
  - ../open-questions.md
  - ./H01-ward-dual-cassette.md
  - ./README.md
sources:
  - "Basseville A et al. Cancer Res 2012;72(14):3642-51 (PMID 22472121) — HDAC inhibition / Q141K trafficking rescue"
  - "FDA Guidance for Industry: Early Clinical Trials with Live Biotherapeutic Products (2016, updated 2018)"
  - "Synlogic SYNB1934 (engineered E. coli Nissle, phenylketonuria — most-advanced engineered-LBP precedent)"
  - "Vowst (Seres / Ferring 2023, FDA approved) — first oral LBP precedent (FMT-derived, not engineered)"
  - "Sonnenburg lab Bacteroides genome-engineering toolkit (Stanford, 2014–present)"
---

# H02 — Engineered LBP Thesis (Stub)

> **Evidence status:** stub. Assumptions, pre-committed thresholds, kill switches, and failure-mode coverage remain incomplete; see [engineered-lbp-chassis.md](../engineered-lbp-chassis.md).
>
> The pre-registration note on H01 ([H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) §Pre-registration) does not apply until this stub is upgraded to a full card. When the upgrade happens, the upgraded version is what gets pre-registered; the stub is informational scaffolding only.

---

## Claim (provisional, stub-level)

An engineered *Faecalibacterium prausnitzii* strain producing colonic butyrate is a testable peer-track chassis. Its supported primary mechanism is PPARγ-mediated induction of wild-type ABCG2; genotype-agnostic coverage is not established:

- **Wild-type ABCG2:** butyrate → PPARγ → upregulated ABCG2 transcription → increased gut-lumen urate efflux
- **Q141K variant ABCG2 (~10% of gout patients):** butyrate's class-I HDAC inhibitor activity is **proposed to** rescue the broken Q141K trafficking phenotype (restoring functional surface expression) — **unvalidated**: Basseville 2012 demonstrated pharmacological/HDACi Q141K rescue with vorinostat, *not* butyrate; direct butyrate rescue is assumption 6, gated on validation §1.14

The "viable peer-track" claim has multiple sub-components that the full card will decompose:
1. *F. prausnitzii* engineering toolkit is mature enough to produce therapeutic-grade butyrate-augmenting strains (vs. WT colonization establishing the colonic baseline)
2. Lyophilized oxygen-protected capsule formulations achieve sufficient post-ingestion viability to colonize at therapeutic densities
3. FDA LBP regulatory path is traversable within the track's capital constraints
4. WT-ABCG2 induction translates to functional human urate flux at achievable colonic butyrate concentrations

---

## Assumption Stack (placeholder — to be populated in Phase 2 P2-5)

The full assumption stack will be populated after fresh engineering, commercial, and regulatory scans plus an exact-strain genetic-entry test. Retired COMP-008 supplies no feasibility result. Anticipated load-bearing assumptions, to be confirmed:

1. An exact *Faecalibacterium* strain can be transformed reproducibly and maintain reporter expression without unacceptable fitness loss.
2. A qualified oral *F. prausnitzii* preparation can deliver a prespecified viable-cell exposure to the intended colonic compartment; neither the achieved exposure nor a therapeutic threshold is established here.
3. Engineered butyrate overproduction does not destabilize *F. prausnitzii* viability or trigger PFOR-pathway feedback that quenches the augmentation
4. Colonic butyrate concentration thresholds for clinically-meaningful PPARγ activation (WT) and HDAC inhibition (Q141K) are achievable from a single delivered LBP strain rather than requiring a designed consortium
5. The applicable FDA LBP pathway, containment expectations, and evidence package are compatible with the exact engineered strain and intended use; timeline and precedent require a current regulatory assessment.
6. Proposed butyrate-mediated Q141K trafficking rescue—**not directly shown by Basseville 2012**—translates to native human gut epithelium at exposures achievable from the engineered LBP

---

## Killshot Menu (placeholder — to be populated in Phase 2 P2-5)

The full killshot menu will follow the H01 template: ranked by `score = (kill_pr × info_weight) / (cost × time_penalty)`, with each killshot tagged to specific assumptions and failure modes per [linter-design.md](../linter-design.md) §4–5.

Anticipated highest-priority killshots:

- **Lit scan + commercial scan first.** Cheapest possible upstream move — answers whether NextBiotix, Synlogic-adjacent, or other published programs have already killed (or already validated) major sub-claims of this hypothesis. (Phase 2 P2-1 + P2-2 do this.)
- **Exact-strain genetic-entry gate.** Demonstrate stable transformation and reporter expression before evaluating a native-pathway intervention or heterologous payload.
- **In vivo butyrate concentration measurement after engineered-strain colonization** (animal model). Tests assumption 4 directly.
- **Q141K trafficking rescue dose-response in primary human enterocytes.** Tests assumption 6 directly.
- **GMP anaerobic manufacturing feasibility.** Obtain configuration-specific process, release, storage, and dose-cost estimates, then compare them with a prespecified program budget before commercial routing.

---

## Pre-Committed Thresholds (placeholder — to be populated in Phase 2 P2-5)

To be defined when the killshot menu is populated. Anticipated structure follows H01: declared Alive / Killed / Pending thresholds for each load-bearing claim, plus kill switches independent of the scientific thresholds (regulatory-precedent collapse, manufacturing-cost ceiling, etc.).

---

## Failure Modes Probed (placeholder — to be populated in Phase 2 P2-5)

To be populated. Anticipated relevant failure modes from [linter-design.md](../linter-design.md) §5: published-literature-gap, species-gap-translation (mouse colonic butyrate vs. human), expression / localization mismatch, kinetics / concentration, dose-translation scaling, regulatory-precedent gap (a category not in H01).

---

## Status

**Stub.** No killshot executed. No assumption stack pre-registered. Full hypothesis card is queued as Phase 2 P2-5 — see [engineered-lbp-chassis.md § Open Follow-Ups](../engineered-lbp-chassis.md#open-follow-ups).

**Survival count:** 0.

**Survival score:** 0.0 (undefined until full card and first survived killshot).

---

## Cross-References

- [engineered-lbp-chassis.md](../engineered-lbp-chassis.md) — the track this hypothesis formalizes
- [modality-chokepoint-matrix.md](../modality-chokepoint-matrix.md) — "Engineered LBPs" row that surfaced this question
- [abcg2-modulators.md](../abcg2-modulators.md) — supported WT-ABCG2 induction and unvalidated direct-butyrate Q141K-rescue hypothesis
- [koji-endgame-strain.md](../koji-endgame-strain.md) — the falsifiable koji chassis hypothesis (H01)
- [open-questions.md](../open-questions.md) §"Engineered LBP chassis" — meta-index entry
- [linter-design.md](../linter-design.md) — schema for the Falsification Card format
- [H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) — sibling falsification card for the koji chassis; format template
