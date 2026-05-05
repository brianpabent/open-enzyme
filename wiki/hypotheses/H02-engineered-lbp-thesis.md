---
id: H02
title: "Engineered *Faecalibacterium prausnitzii* delivering colonic butyrate is a viable peer-track therapeutic chassis to engineered koji for gout, with genotype-agnostic ABCG2 induction (WT + Q141K) as the primary mechanism of action"
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

> **Stub status.** This card is committed at stub-level on 2026-05-05 to register the hypothesis in the falsification-card directory and force the "what would kill this thesis" framing onto the [LBP chassis page](../engineered-lbp-chassis.md). Full population (assumption stack, killshot menu, pre-committed thresholds, kill switches, failure-mode coverage map) is queued as Phase 2 P2-5 — see [engineered-lbp-chassis.md § Open Follow-Ups](../engineered-lbp-chassis.md#open-follow-ups).
>
> The pre-registration note on H01 ([H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) §Pre-registration) does not apply until this stub is upgraded to a full card. When the upgrade happens, the upgraded version is what gets pre-registered; the stub is informational scaffolding only.

---

## Claim (provisional, stub-level)

An engineered *Faecalibacterium prausnitzii* strain producing therapeutic-relevant levels of colonic butyrate, delivered as an oral lyophilized lipid-encapsulated capsule, is a viable peer-track therapeutic chassis to engineered koji for gout. The primary mechanism of action is genotype-agnostic ABCG2 induction:

- **Wild-type ABCG2:** butyrate → PPARγ → upregulated ABCG2 transcription → increased gut-lumen urate efflux
- **Q141K variant ABCG2 (~10% of gout patients):** butyrate's class-I HDAC inhibitor activity rescues the broken Q141K trafficking phenotype, restoring functional surface expression

The "viable peer-track" claim has multiple sub-components that the full card will decompose:
1. *F. prausnitzii* engineering toolkit is mature enough to produce therapeutic-grade butyrate-augmenting strains (vs. WT colonization establishing the colonic baseline)
2. Lyophilized oxygen-protected capsule formulations achieve sufficient post-ingestion viability to colonize at therapeutic densities
3. FDA LBP regulatory path is traversable within capital constraints reasonable for a research-platform-derived therapeutic
4. The genotype-agnostic ABCG2 mechanism translates from in vitro Caco-2 data to humanized clinical effect at achievable colonic butyrate concentrations

---

## Assumption Stack (placeholder — to be populated in Phase 2 P2-5)

The full assumption stack will be populated after the three Phase 2 lit scans (P2-1 engineering, P2-2 commercial, P2-3 regulatory) and comp-008 (P2-4 expression feasibility) land. Anticipated load-bearing assumptions, to be confirmed:

1. *F. prausnitzii* genetic engineering toolkit supports therapeutic-grade payload modification (current state: research-grade tools published 2018–present; NextBiotix and others driving the engineering envelope; gap to therapeutic-grade unclear)
2. Lyophilized + lipid-encapsulated oral *F. prausnitzii* preparations achieve >10⁸ CFU/dose live delivery to the colon (current best-published: ~10⁶–10⁷ CFU; gap to therapeutic threshold uncharacterized)
3. Engineered butyrate overproduction does not destabilize *F. prausnitzii* viability or trigger PFOR-pathway feedback that quenches the augmentation
4. Colonic butyrate concentration thresholds for clinically-meaningful PPARγ activation (WT) and HDAC inhibition (Q141K) are achievable from a single delivered LBP strain rather than requiring a designed consortium
5. The 2018 FDA LBP regulatory framework supports an engineered-strain BLA filing within current scientific advisory committee precedent (vs. requiring a category-creation pathway that adds 2–4 years)
6. Q141K trafficking rescue by butyrate documented in Basseville 2012 (in vitro on transfected lines) translates to native human gut epithelium at colonic concentrations achievable from an engineered LBP

---

## Killshot Menu (placeholder — to be populated in Phase 2 P2-5)

The full killshot menu will follow the H01 template: ranked by `score = (kill_pr × info_weight) / (cost × time_penalty)`, with each killshot tagged to specific assumptions and failure modes per [linter-design.md](../linter-design.md) §4–5.

Anticipated highest-priority killshots:

- **Lit scan + commercial scan first.** Cheapest possible upstream move — answers whether NextBiotix, Synlogic-adjacent, or other published programs have already killed (or already validated) major sub-claims of this hypothesis. (Phase 2 P2-1 + P2-2 do this.)
- **comp-008 expression feasibility.** Tests whether *F. prausnitzii*'s codon usage, GC content, and secretion machinery support the desired payload class without a multi-year toolkit-development project. (Phase 2 P2-4 does this.)
- **In vivo butyrate concentration measurement after engineered-strain colonization** (animal model). Tests assumption 4 directly.
- **Q141K trafficking rescue dose-response in primary human enterocytes.** Tests assumption 6 directly.
- **GMP anaerobic manufacturing cost ceiling analysis.** If per-dose cost projections exceed ~$5,000 at clinical-relevant scale, the commercial-pharmaceutical case dies regardless of mechanism.

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

- [engineered-lbp-chassis.md](../engineered-lbp-chassis.md) — the platform thesis this hypothesis formalizes
- [modality-chokepoint-matrix.md](../modality-chokepoint-matrix.md) — "Engineered LBPs" row that surfaced this question
- [abcg2-modulators.md](../abcg2-modulators.md) — butyrate dual-action mechanism (PPARγ + HDAC), Q141K rescue
- [koji-endgame-strain.md](../koji-endgame-strain.md) — the peer-track koji chassis hypothesis (H01)
- [open-questions.md](../open-questions.md) §"Engineered LBP chassis" — meta-index entry
- [linter-design.md](../linter-design.md) — schema for the Falsification Card format
- [H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) — sibling falsification card for the koji chassis; format template
