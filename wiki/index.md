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

## New This Week (2026-05-05)

The "Open Enzyme as gout-solving research project" framing got concrete this week — two new peer-track scope pages, four computational experiments, three new wet-lab queue entries, and an inbox-zero pass on the synthesis queue.

**Two new peer-track scope pages** (sister to the koji chassis under the broader gout-solving mission):

- **[Engineered LBP Chassis](engineered-lbp-chassis.md)** — engineered obligate-anaerobe colonic residents (*F. prausnitzii*, *Akkermansia*, *Bacteroides*) as a commercial-pharmaceutical sub-track. Butyrate dual-action is the anchor: genotype-agnostic ABCG2 induction (WT via PPARγ + Q141K via class-I HDAC). Six in silico Phase 2 follow-ups queued; falsification card [H02](hypotheses/H02-engineered-lbp-thesis.md) committed at stub level.
- **[siRNA / URAT1 Modality](sirna-urat1-modality.md)** — kidney-tropic siRNA against the dominant renal urate-reabsorption transporter, positioned as discovery-engine output (partner / spinout territory, not in-house manufacture). Sequence-specificity eliminates the off-target metabolite class that withdrew benzbromarone. Six Phase 2 follow-ups queued; falsification card [H03](hypotheses/H03-sirna-urat1-thesis.md) committed at stub level.

**Four new computational experiments** under the new `comp-NNN` framework — reproducible scripts + inputs + outputs committed; tracking index at [computational-experiments.md](computational-experiments.md):

- **[comp-001 — Uricase shio-koji protease stability](uricase-protease-stability-computational.md)** — verdict **LOW**. Reframes the uricase arm of §1.10 from feasibility gate to confirmation experiment.
- **[comp-005 — Lactoferrin shio-koji protease stability](lactoferrin-protease-stability-computational.md)** — verdict **HIGH (full sequence, signal-peptide-driven) / MODERATE (mature protein)**. Lactoferrin arm of §1.10 remains a feasibility gate.
- **[comp-006 — DAF/CD55 shio-koji protease stability](daf-cd55-protease-stability-computational.md)** — verdict **HIGH** on all three scopes, driven by a disordered Ser/Thr stalk; SCR1–4 truncated construct (aa 35–285) would remove all exposed sites.
- **[comp-007 — Food-grade HDACi in silico ranking](food-grade-hdaci-screen-computational.md)** — Stage 1 of §1.22. Butyrate dominates (167× HDAC6 selectivity confirmed); sulforaphane and PEITC advance to Stage 2 wet-lab.

**Three new wet-lab queue entries** in [validation-experiments.md](validation-experiments.md):

- **§1.22 — Gut-selective food-grade HDAC inhibitor screen** for Q141K-ABCG2 trafficking rescue (Stage 1 actioned via comp-007 above)
- **§1.23 — Androgen × MSU × NLRP3 macrophage tiered protocol** (T1 THP-1 / T2 PBMC / T3 mouse air-pouch). Fills a documented literature gap — testosterone × MSU-crystal × NLRP3 in macrophages has zero indexed papers despite both halves being independently well-characterized.
- **§1.24 — Carnosine co-expression validation in *A. oryzae*** (koji endgame optional third cassette — androgen-driven URAT1 countermeasure)

**Other meaningful updates:**

- **[Modality × Target Matrix](modality-chokepoint-matrix.md)** — new "Engineered soluble complement regulators" row closes the only "honest platform gap" (CP0 / complement priming) with a heterologous-protein engineering vector (sCR1, Factor H, DAF/CD55 ectodomain).
- **[Lactoferrin](lactoferrin.md) §4.7** — new "Indirect Substrate-Supply Synergy" section: composed mechanism (lactoferrin → ↓TNFα → ↑ABCG2 expression → ↑uricase substrate). Validated in §1.14 Caco-2 design.
- **[Koji Endgame Strain](koji-endgame-strain.md) §2.5 + §6.4** — new carnosine renal-transporter arm (precision countermeasure for androgen-dominant gout phenotype) and new "Peer Track — Engineered LBP Chassis" subsection framing the two-track platform model.
- **[Self-Experiment Protocol](self-experiment-protocol.md) §11.1** — new ex vivo MSU PBMC challenge add-on for androgen-elevated subjects ($500–1K per quarterly panel).
- **[Androgen-Urate Axis](androgen-urate-axis.md)** — new "Beyond transporters" section documenting the direct androgen → NLRP3 axis (bidirectional: anti-inflammatory in most tissues, pro-inflammatory in cardiac macrophages; gout-specific intersection unstudied).
- **[Synthesis Queue](synthesis.md)** inbox-zero pass — 14-item sweep walked 1-by-1 and pruned; Strategic Reflections Queue added at the bottom for content-triggered platform reframes.

Most weeks don't see this much movement; this was a focused walkthrough of two stale sweep blocks combined with ad-hoc work that emerged from a framing reframe ("Open Enzyme is the first chassis output of a broader gout-solving research project, not the project itself").

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
