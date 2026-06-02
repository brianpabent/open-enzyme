---
title: Open Enzyme
---

# Open Enzyme

An open source effort to disrupt the gout / NLRP3 / urate-disposal cascade — mapping every chokepoint in the disease and finding the right intervention for each, then building the ones that can be made food-grade and grown at home.

**Status:** Phase 0 — Research & Design

---

> **Have gout? Want to know what to do?**
> → Start with the [Gout Action Guide](gout-action-guide.md) — organized by situation (today / this month / this year), it translates the research below into action.
> → Prefer a patient-friendly companion site? [**gout.care**](https://gout.care) is the plain-language translation of this research, written for people living with gout rather than the PhD-research audience.

---

## The Problem

The human body is missing an enzyme. *Urate oxidase* (uricase) was lost ~15 million years ago in the primate lineage. Every other mammal degrades uric acid to allantoin; we accumulate it. The result: gout, kidney stones, and chronic inflammation — affecting ~10 million Americans.

The standard fix (allopurinol) reduces production. We're mapping the *entire* cascade — production, renal and gut handling, crystal formation, and the NLRP3-driven inflammation that follows — and matching each chokepoint to the cheapest intervention that hits it, whether engineered, repurposed, dietary, or behavioral.

---

## Platform Thesis

**The mission is the chokepoint map; the strain library is one output of it.** We map every vector that causes, treats, or mitigates gout, then build interventions chokepoint-by-chokepoint. Chassis is downstream of chokepoint — no single organism reaches every target.

**Highest-priority chassis: engineered koji.** One engineered *Aspergillus oryzae* strain expressing uricase plus a multi-cassette payload (carnosine, lactoferrin, DAF SCR1-4 in the endgame), fermented on rice bran, positioned as an *adjunct to allopurinol* — not a monotherapy replacement.

**Why koji?** *A. oryzae* is GRAS, natively secretes enzymes at high titer, survives GI transit in solid-substrate form, harmoniously hits multiple chokepoints in one strain, and is home-fermentable — which matches the open-source, democratized-access positioning. It also co-produces NLRP3-suppressing compounds (kojic acid, 3–5 g/L natively) as a fermentation byproduct. (source: etc/open-enzyme-vision.md, §4)

**Why gut-lumen?** ~1/3 of uric acid is secreted into the gut via ABCG2. Degrading it there doesn't require systemic absorption — the enzyme never needs to cross the intestinal wall. ALLN-346 (Allena Pharmaceuticals) proved this concept clinically.

**Beyond koji.** Chokepoints koji can't reach — renal URAT1, kidney macrophages, intra-articular crystals, the acute flare window — are pursued through other chassis (kidney-tropic siRNA, engineered live biotherapeutics, purine-degrading bacteria, mRNA-IL-1RA pulse, intra-articular uricase, phage modulation), tracked in [Chassis-Pending Interventions](chassis-pending-interventions.md). The discovery engine also surfaces a **repurposing surface**: FDA-approved drugs that hit relevant chokepoints but were never clinically tested for gout (e.g., zileuton at CP6a, disulfiram at CP6b, avacopan at CP0). (source: etc/open-enzyme-vision.md, §1–2)

**Koji-track positioning:** within the koji chassis specifically, Open Enzyme is a **food-derived, multi-target NLRP3 pathway modulator** — not an attempt to make a food-grade analog of the direct NLRP3 inhibitor class (MCC950, dapansutrile, oridonin). (source: etc/open-enzyme-vision.md, §10)

---

## First Targets

| Target | Condition | Chassis | Status |
|--------|-----------|---------|--------|
| Uricase | Gout / hyperuricemia | *A. oryzae* koji (primary); *S. cerevisiae* for characterized modules | Design phase |
| Carnosine + lactoferrin + DAF SCR1-4 | NLRP3 / complement priming, urate handling | *A. oryzae* co-expression (multi-cassette endgame) | Design phase |
| Lipase + protease + amylase | EPI (exocrine pancreatic insufficiency) | *A. oryzae* koji | Design phase |

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

Research lands continuously: a multi-pass sweep daemon propagates each new finding across every cross-referenced page and emits cross-document connections, contradictions, proposed experiments, and open questions. The live action queue (one file per finding) lives in the [synthesis queue on GitHub](https://github.com/brianpabent/open-enzyme/tree/main/synthesis). Cheapest validated experiments are prioritized first.

---

## Evidence Standard

All claims are tagged with evidence level: **Clinical Trial** · **Animal Model** · **In Vitro** · **Mechanistic Extrapolation**. This library is written for PhD scientists. We distinguish proven from speculative and do not oversell.
