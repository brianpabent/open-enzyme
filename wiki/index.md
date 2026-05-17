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

**Why koji?** *A. oryzae* is GRAS, natively secretes enzymes at high titer, survives GI transit in solid-substrate form, and already co-produces NLRP3-suppressing compounds (kojic acid, 3–5 g/L natively) as a byproduct of fermentation. The platform is **koji-first**: *A. oryzae* is the primary host, with *S. cerevisiae* retained for specific modules where yeast expression is better characterized. (source: etc/open-enzyme-vision.md, §4)

**Why gut-lumen?** ~1/3 of uric acid is secreted into the gut via ABCG2. Degrading it there doesn't require systemic absorption — the enzyme never needs to cross the intestinal wall. ALLN-346 (Allena Pharmaceuticals) proved this concept clinically.

**Two parallel outputs:** The strain library is one synthesis from a broader **discovery engine** — a chokepoint-based methodology for mapping every vector that causes, treats, or mitigates a given disease. The discovery engine also produces a repurposing surface: FDA-approved drugs that hit relevant chokepoints but were never clinically tested for the target disease (e.g., zileuton at CP6a, disulfiram at CP6b, avacopan at CP0). (source: etc/open-enzyme-vision.md, §2)

**Platform positioning:** Open Enzyme is a **food-derived, multi-target NLRP3 pathway modulator** platform — not an attempt to produce a food-grade analog of the direct NLRP3 inhibitor class (MCC950, dapansutrile, oridonin). (source: etc/open-enzyme-vision.md, §10)

---

## First Targets

| Target | Condition | Platform | Status |
|--------|-----------|----------|--------|
| Uricase | Gout / hyperuricemia | *S. cerevisiae* or *A. oryzae* | Design phase |
| Lipase + protease + amylase | EPI (exocrine pancreatic insufficiency) | *A. oryzae* koji | Design phase |
| NLRP3 inhibitors | Gout flare suppression | *A. oryzae* co-production | Design phase |

---

## New This Week (2026-05-17)

This sweep propagated three clinical-surface findings from trigger files into the research wiki:

**BHB active-flare contraindication** propagated to `nlrp3-exploit-map.md` — the "ketosis paradox resolved" framing (BHB suppresses NLRP3 while uricase handles UA) is correct for prophylaxis, but BHB/ketosis is NOT a rescue intervention during active flare. Transient ketotic UA rise of 5–10% can compound the flare. Suspend ketosis + intermittent fasting during active flares; resume after 1–2 weeks. (source: gout-action-guide.md)

**Anakinra SC for acute gout flare** propagated to `nlrp3-exploit-map.md` CP5a section and `colchicine.md` comparison table — 100 mg/day × 3 days SC in thigh/abdomen off-label for gout. Same IL-1R1 chokepoint as canakinumab but ~100× cheaper (~$900/flare) with cleaner cumulative burden vs prednisone over decades of recurrent flares. Faster onset than prednisone, narrower mechanism, none of the bone/glucose/adrenal/mood effects. (source: gout-action-guide.md, gout-clinical-pipeline.md)

**Topical CBD+THC acute-flare protocol** propagated to `nlrp3-exploit-map.md`, `supplements-stack.md`, and `GRAPH.md` — 1:1 CBD:THC (high-mg/oz) applied to affected joint + ice cycling. CB2-mediated NLRP3 suppression + TRPV1 desensitization. For recurrent-flare patients with cumulative steroid burden, may reduce prednisone need. Jurisdiction-dependent. (source: cannabinoids-terpenes.md, gout-action-guide.md)

**Plasmidsaurus QC pipeline** and **consumer SNP data-quality gap** already well cross-referenced in `validation-experiments.md`, `personal-genome-protocol.md`, and `genotype-informed-supplement-workflow.md` — no propagation needed. (source: engineered-koji-protocol.md, gout-action-guide.md)

---

## Where to Start

**New to the project?**
→ [Open Enzyme Vision](etc/open-enzyme-vision.md) — the problem, insight, and platform vision (10 min read)

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

The [Synthesis Queue](../synthesis/README.md) captures cross-document connections, proposed experiments, and open questions. Updated by the sweep daemon as new research lands. Cheapest validated experiments are prioritized first.

---

## Evidence Standard

All claims are tagged with evidence level: **Clinical Trial** · **Animal Model** · **In Vitro** · **Mechanistic Extrapolation**. This library is written for PhD scientists. We distinguish proven from speculative and do not oversell.
