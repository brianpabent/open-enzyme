---
title: Open Enzyme
---

# Open Enzyme

An open source library of food-grade engineered microbial strains — each producing a therapeutic enzyme, each growable at home, each freely available to anyone.

**Status:** Phase 0 — Research & Design

---

## The Problem

The human body is missing an enzyme. *Urate oxidase* (uricase) was lost ~15 million years ago in the primate lineage. Every other mammal degrades uric acid to allantoin; we accumulate it. The result: gout, kidney stones, and chronic inflammation — affecting ~10 million Americans.

The standard fix (allopurinol) reduces production. We're engineering a complementary approach: gut-lumen degradation via an enzyme-producing probiotic strain that never needs to be absorbed.

---

## Platform Thesis

One engineered *Aspergillus oryzae* koji strain expressing uricase + NLRP3 inhibitors, fermented on rice bran, positioned as an adjunct to allopurinol — not a monotherapy replacement.

**Why koji?** *A. oryzae* is GRAS, natively secretes enzymes at high titer, survives GI transit in solid-substrate form, and already co-produces NLRP3-suppressing compounds (kojic acid, 3–5 g/L natively) as a byproduct of fermentation. The platform is **koji-first**: *A. oryzae* is the primary host, with *S. cerevisiae* retained for specific modules where yeast expression is better characterized. (source: open-enzyme-vision.md, §4)

**Why gut-lumen?** ~1/3 of uric acid is secreted into the gut via ABCG2. Degrading it there doesn't require systemic absorption — the enzyme never needs to cross the intestinal wall. ALLN-346 (Allena Pharmaceuticals) proved this concept clinically.

**Two parallel outputs:** The strain library is one synthesis from a broader **discovery engine** — a chokepoint-based methodology for mapping every vector that causes, treats, or mitigates a given disease. The discovery engine also produces a repurposing surface: FDA-approved drugs that hit relevant chokepoints but were never clinically tested for the target disease (e.g., zileuton at CP6a, disulfiram at CP6b, avacopan at CP0). (source: open-enzyme-vision.md, §2)

**Platform positioning:** Open Enzyme is a **food-derived, multi-target NLRP3 pathway modulator** platform — not an attempt to produce a food-grade analog of the direct NLRP3 inhibitor class (MCC950, dapansutrile, oridonin). (source: open-enzyme-vision.md, §10)

---

## First Targets

| Target | Condition | Platform | Status |
|--------|-----------|----------|--------|
| Uricase | Gout / hyperuricemia | *S. cerevisiae* or *A. oryzae* | Design phase |
| Lipase + protease + amylase | EPI (exocrine pancreatic insufficiency) | *A. oryzae* koji | Design phase |
| NLRP3 inhibitors | Gout flare suppression | *A. oryzae* co-production | Design phase |

---

## New This Week (2026-05-07)

This week's sweep was a propagation pass — seven trigger files, seven affected pages updated. The major changes:

**LF disulfide count correction (17→16) propagated across four pages.** Notari 2023 (PMC10465537) explicitly states 16 disulfides for human lactoferrin. The correction flows through [koji-endgame-strain.md](koji-endgame-strain.md), [lactoferrin.md](lactoferrin.md), [cassette-compatibility-computational.md](cassette-compatibility-computational.md), and [aspergillus-oryzae.md](aspergillus-oryzae.md). The architecture-adjusted effective PDI load for LF is 24–40 (16 disulfides × transferrin-lobe α = 1.5–2.5), substantially higher than the bulk count suggests. (source: chaperone-orthogonal-stacking.md §3.5, §10.2)

**Chaperone-orthogonal stacking framework refined with per-architecture PDI residence time coefficients.** Three fold architectures scored: CCP/SCR sushi (α = 0.3–0.6), Ig-like (α = 1.0 reference), transferrin-lobe (α = 1.5–2.5). The triple-cassette prediction (uricase + Lf + DAF SCR1-4) revised from 0.45–0.70 to **0.35–0.65 (central 0.45–0.55)** — firmly below the 0.6 decision gate. DAF SCR1-4 routed to separate-strain or LBP-chassis peer track. (source: chaperone-orthogonal-stacking.md §3.5, §5.5)

**DAF/CD55 SCR1-4 single-cassette wet-lab gate formalized** as [validation-experiments.md §1.25](validation-experiments.md). $2.5–4K, 6–8 weeks. Tests expression, correct disulfide folding (8 disulfides, corrected from 12 per UniProt P08174), and CCP-regulatory activity in *A. oryzae*. (source: validation-experiments.md §1.25, daf-cd55-scr14-truncated-computational.md §1.5)

**Medicinal mushroom complement track expanded.** *P. citrinopileatus* (golden oyster) confirmed as highest fungal EGT producer at 7.0 mg/g DW (vs. *P. ostreatus* at 2.4 mg/g). Cordycepin koji-engineering route documented (cns1+cns2 in *A. oryzae* at 564 mg/L/day per Jeennor 2023 PMID 38071331) — sequential cultivation-first default with koji-engineering as documented contingency. GLPP+cordycepin synergy wet-lab gate refined to 4-arm comparison with the natural *C. militaris* pentostatin ADA-inhibitor pairing. Phase 7-4b follow-up (koji × mushroom additivity arm) queued. (source: medicinal-mushroom-complement-track.md, medicinal-mushroom-extract-sops.md)

**Multi-track urate transporter coverage map** added to [gout-pathophysiology.md](gout-pathophysiology.md). Engineered koji, medicinal mushroom, and TCM × rigor tracks collectively cover URAT1, GLUT9, ABCG2, OAT1/OAT3, and xanthine oxidase — emergent designed-coverage, not planned. (source: gout-pathophysiology.md §"Multi-track urate transporter coverage")

**Concept graph updated** with new chaperone subsystem nodes (per-architecture α coefficients, DAF SCR1-4 single-cassette routing) and LF disulfide count correction. (source: GRAPH.md)

---

## Where to Start

**New to the project?**
→ [Open Enzyme Vision](open-enzyme-vision.md) — the problem, insight, and platform vision (10 min read)

**Scientist evaluating the thesis?**
→ [Cross-Validation](cross-validation.md) — rigorous stress test: feasibility ratings, risk matrix, clinical bridges

**Engineer interested in the construct design?**
→ [Protein Engineering Strategy](protein-engineering-strategy.md) — SB-1 / BAL-1 / OPT-1 mutation tiers with full lookup table  
→ [Engineered Yeast Uricase Proposal](engineered-yeast-uricase-proposal.md) — full *S. cerevisiae* construct design  
→ [Koji Construct Design](koji-construct-design.md) — *A. oryzae* uricase expression

**Clinician or pharma reviewer?**
→ [Gout Deep Dive](gout-deep-dive.md) — full pathophysiology and current standard of care  
→ [GI Survival Prediction](gi-survival-prediction.md) — transit model and bioavailability estimates

---

## Latest Synthesis

The [Synthesis Queue](synthesis.md) captures cross-document connections, proposed experiments, and open questions. Updated by the sweep daemon as new research lands. Cheapest validated experiments are prioritized first.

---

## Evidence Standard

All claims are tagged with evidence level: **Clinical Trial** · **Animal Model** · **In Vitro** · **Mechanistic Extrapolation**. This library is written for PhD scientists. We distinguish proven from speculative and do not oversell.
