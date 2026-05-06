---
id: H06
title: "Open Enzyme can produce reproducible, bioactivity-validated medicinal-mushroom-complement extracts (GLPP, cordycepin, ergothioneine) at quality sufficient to replicate published in vivo effect sizes within 2× — making the medicinal-mushroom-complement track a viable peer to the koji-engineering track"
committed: 2026-05-06
status: Stub
survival_count: 0
tags:
  - hypothesis
  - medicinal-mushroom-complement
  - phase-7
  - cultivation
  - extract-characterization
  - peer-track
  - falsification-card
related:
  - ../medicinal-mushroom-complement-track.md
  - ../medicinal-mushroom-compound-mapping-computational.md
  - ../engineered-lbp-chassis.md
  - ../sirna-urat1-modality.md
  - ../modality-chokepoint-matrix.md
  - ../open-source-platform.md
  - ../open-enzyme-vision.md
  - ./H02-engineered-lbp-thesis.md
  - ./H03-sirna-urat1-thesis.md
  - ./H05-daf-scr14-cp0-thesis.md
  - ./README.md
sources:
  - "comp-014 Phase 6 triage (2026-05-06) — GLPP, cordycepin, ergothioneine routed to cultivation track"
  - "Brian framing 2026-05-06: 'is there another fungus that could be easily grown at home that would be either a better solution than koji or a complementary solution with koji?'"
  - "Phase 7 scope page `medicinal-mushroom-complement-track.md`"
---

# H06 — Medicinal-Mushroom-Complement Track Viability (Stub)

> **Stub status.** Committed 2026-05-06 alongside the Phase 7 scope page launch to register the hypothesis in the falsification-card directory and force the "what would kill this track" framing onto the just-opened parallel track. Full population (assumption stack, killshot menu, pre-committed thresholds, kill switches, failure-mode coverage map) queued as Phase 2 — see [`medicinal-mushroom-complement-track.md`](../medicinal-mushroom-complement-track.md) §"Six Phase 7 follow-ups queued" #5.
>
> Pre-registration discipline (per H01) does not apply until this stub is upgraded to a full card.

---

## Claim (provisional, stub-level)

Open Enzyme can produce reproducible, bioactivity-validated medicinal-mushroom-complement extracts at quality sufficient to make the medicinal-mushroom track a viable **peer** to the koji-engineering track for the Open Enzyme platform thesis. The thesis composes three sub-claims, each independently falsifiable:

1. **Cultivation reproducibility.** For each top Phase 7 candidate species (*G. lucidum* / GLPP, *C. militaris* / cordycepin, *P. ostreatus* / ergothioneine), an Open Enzyme-published cultivation SOP (strain selection + substrate + conditions + cycle time) produces compound yields that vary <50% batch-to-batch when followed by independent contributors. (Industry-wide consumer-supplement variability is currently >100× — Open Enzyme's reproducibility floor needs to be meaningfully better than the unregulated baseline to add value.)

2. **Extract characterization quality.** For each cultivation SOP, an Open Enzyme-published HPLC / SEC-MALS / MS characterization protocol can verify the active fraction's identity + concentration with reproducibility ±15% across operators. Specifically: GLPP molecular weight verification (~520 kDa SEC-MALS) + peptide:polysaccharide ratio quantification + glycan linkage NMR fingerprint; cordycepin HPLC quantification with a reference standard at ≥98% purity; ergothioneine LC-MS quantification with a stable-isotope internal standard.

3. **In vivo effect-size replication.** For ≥1 Phase 6 lead (priority: GLPP given the 40.6% UA reduction headline finding), an Open Enzyme-protocol-produced extract replicates the published in vivo HUA mouse model effect size **within 2×** of the original paper's claim — meaning if published 40.6% reduction, our reproduction lands ≥20% reduction. This sub-claim is the load-bearing one: if cultivation + extraction is reproducible (#1 + #2) but the resulting extract doesn't replicate the published bioactivity, the upstream chain is intact but the published claim is unstable, and the track is not viable in a way that no protocol-improvement fixes.

A track-level success requires all three; failure on any one is sufficient to kill the track or substantially narrow its scope.

---

## Why this hypothesis matters

The medicinal-mushroom-complement track positions Open Enzyme as a **reproducibility + characterization layer** on top of an existing supplement industry that has known quality issues (DNA-barcoded studies of Ganoderma supplements regularly find <50% match the species labeled; mycelium-on-grain products are mostly grain). The track's value-add is precision, not chemistry discovery — the chemistry is in the public domain.

If H06 fails, the track's value proposition collapses regardless of whether the underlying compound mechanisms are real. Reishi GLPP can be a real ADA inhibitor and Open Enzyme's track can still fail — if we can't actually deliver reproducible, characterized extracts at scale, we don't add value over the existing supplement industry.

This is meaningfully different from the koji-engineering track's failure modes (uricase doesn't fold, lactoferrin doesn't secrete, DAF SCR1-4 disulfides don't form). Engineering tracks fail at chemistry; the cultivation-complement track fails at quality systems.

---

## Three falsification dimensions (placeholder for full kill criteria)

### Dimension 1 — Cultivation variability ceiling

**Falsifies if:** Standardized SOP-following cultivation produces >50% batch-to-batch variation in target compound yield across ≥3 independent operators.

**Why this matters:** Below the "more reproducible than industry baseline" threshold, Open Enzyme's contribution is null. A published SOP that produces 0.5-5 mg/g cordycepin batch-to-batch isn't a contribution; it's a restatement of the existing supplement-industry problem.

**Mitigation if approached but not crossed:** May require strain narrowing (single accession rather than commercial mixed strains), substrate sourcing standardization (specific brown-rice cultivar specification rather than generic), or environmental control narrowing (temperature/humidity tolerance bands tightened).

### Dimension 2 — Characterization protocol robustness

**Falsifies if:** Open Enzyme HPLC/MS protocol cannot achieve ±15% inter-operator reproducibility on identical samples, OR cannot distinguish target compound (e.g., GLPP) from confounding co-extracted material (other Ganoderma polysaccharides, peptides) with sufficient resolution.

**Why this matters:** Precision claims need precision tools. Without analytical reproducibility, the track devolves to "trust the SOP-follower's word" — same problem as the existing supplement industry.

**Mitigation if approached but not crossed:** May require swapping characterization methods (LC-MS instead of HPLC for some compound classes), commissioning external reference standards, or accepting a narrower compound scope (cordycepin yes; GLPP "polysaccharide-peptide" too imprecisely defined to characterize).

### Dimension 3 — In vivo bioactivity replication

**Falsifies if:** ≥1 Phase 6 lead (priority: GLPP) cannot replicate published in vivo effect size within 2× when administered as Open Enzyme-protocol extract in the same HUA mouse model.

**Why this matters:** This is the load-bearing claim — and the most expensive to test (mouse work, ~$15-30K for a properly-powered replication study). It can be deferred until cultivation + characterization (Dimensions 1+2) are demonstrated, but cannot be skipped without admitting the track is "process improvement of unknown therapeutic value."

**Mitigation if approached but not crossed:** First check operator/protocol error before declaring replication failure. Second check whether the original paper's effect size was inflated (publication bias — many TCM polysaccharide studies in mid-tier journals report effect sizes that don't replicate at higher methodological rigor). If both confirmed and the published effect was inflated, the failure is informative — it tells the field which mushroom-pharmacology claims survive scrutiny and which don't, which is itself a contribution to open science even if the specific compound is dropped from the OE roadmap.

---

## Pre-committed thresholds (placeholder)

To be populated when H06 is upgraded from stub to full card. Will follow the H01 / H03 pattern — specific quantitative gates, declared in advance, no post-hoc threshold migration.

---

## Kill switches (placeholder)

To be populated when full-card. Conceptually similar to other peer-track stubs.

---

## Cross-references

See related list in frontmatter. Particularly:

- [`medicinal-mushroom-complement-track.md`](../medicinal-mushroom-complement-track.md) — the scope page this card is the falsification mirror of
- [`H02-engineered-lbp-thesis.md`](./H02-engineered-lbp-thesis.md), [`H03-sirna-urat1-thesis.md`](./H03-sirna-urat1-thesis.md), [`H05-daf-scr14-cp0-thesis.md`](./H05-daf-scr14-cp0-thesis.md) — sister peer-track hypothesis cards under the broader "explore every avenue" platform thesis
- [`medicinal-mushroom-compound-mapping-computational.md`](../medicinal-mushroom-compound-mapping-computational.md) — comp-014, the computational analysis whose Phase 6 triage spawned this Phase 7 track + hypothesis card

---

**Status:** Stub committed 2026-05-06 with Phase 7 scope page. Full-card upgrade queued as part of Phase 7 follow-up #5.
