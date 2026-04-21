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

**Why koji?** *A. oryzae* is GRAS, natively secretes enzymes at high titer, survives GI transit in solid-substrate form, and already co-produces NLRP3-suppressing compounds (kojic acid, 3–5 g/L natively) as a byproduct of fermentation.

**Why gut-lumen?** ~1/3 of uric acid is secreted into the gut via ABCG2. Degrading it there doesn't require systemic absorption — the enzyme never needs to cross the intestinal wall. ALLN-346 (Allena Pharmaceuticals) proved this concept clinically.

---

## First Targets

| Target | Condition | Platform | Status |
|--------|-----------|----------|--------|
| Uricase | Gout / hyperuricemia | *S. cerevisiae* or *A. oryzae* | Design phase |
| Lipase + protease + amylase | EPI (exocrine pancreatic insufficiency) | *A. oryzae* koji | Design phase |
| NLRP3 inhibitors | Gout flare suppression | *A. oryzae* co-production | Design phase |

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
