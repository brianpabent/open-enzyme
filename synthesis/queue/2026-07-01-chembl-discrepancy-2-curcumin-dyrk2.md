---
title: "ChEMBL discrepancy: Curcumin — DYRK2 IC50 = 2.5 nM (new rank-2 target, not in v34 baseline)"
date: 2026-07-01
type: Connection
priority: Low
tags: ["ChEMBL", "curcumin", "DYRK2", "proteasome", "kinase", "chembl-refresh"]
related:
  - ../wiki/nlrp3-inhibitor-screen.md
  - ../wiki/supplements-stack.md
  - ../wiki/etc/chembl-cross-check.md
source: "ChEMBL v37 quarterly refresh, 2026-07-01"
---

# ChEMBL Discrepancy: Curcumin — DYRK2 IC50 = 2.5 nM (New in ChEMBL v37)

## What Changed

**Compound:** Curcumin (CHEMBL140, CAS 458-37-7)
**Baseline (ChEMBL v34, 2026-04-24):** Top curated molecular target: amyloid-β Ki = 0.208 nM (*J Med Chem* 2006, pChEMBL 9.68). Rank-3 compound with direct human NLRP3 entry (IC50 = 24.2 μM, *J Nat Prod* 2020). No DYRK2 entry.
**Current (ChEMBL v37, 2026-07-01):** DYRK2 IC50 = 2.5 nM (*J Med Chem* 2023, pChEMBL 8.60) is now rank-2 molecular target.

**Updated top-5 curated bioactivity profile:**

| Rank | Target | Activity type | Value | pChEMBL | Source |
|---|---|---|---|---|---|
| 1 | Amyloid-β precursor protein | Ki | 0.208 nM | 9.68 | *J Med Chem* 2006 |
| 2 | **DYRK2** | **IC50** | **2.5 nM** | **8.60** | ***J Med Chem* 2023 (NEW)** |
| 3 | Lactoylglutathione lyase | Ki | 5.0 nM | 8.30 | *Bioorg Med Chem* 2020 |
| 4 | NLRP3 (human THP-1) | IC50 | 24.2 μM | 4.62 | *J Nat Prod* 2020 |
| 5 | (Various, pChEMBL 6–8 range) | — | — | — | — |

Evidence level: In Vitro (curated ChEMBL; single paper for DYRK2).

## Why DYRK2 Is Worth Noting

**DYRK2 (dual-specificity tyrosine-phosphorylation-regulated kinase 2)** is a serine/threonine kinase (and dual-specificity) with three functions relevant to Open Enzyme:

1. **Proteasome regulation via PA28γ phosphorylation.** DYRK2 phosphorylates the proteasome activator PA28γ (also called PSME3), which is required for 26S proteasome assembly. Curcumin's DYRK2 inhibition at 2.5 nM could disrupt 26S assembly — placing curcumin mechanistically at the proteasome, adjacent to EGCG's 20S chymotrypsin-like inhibition (IC50 = 86 nM, *Bioorg Med Chem* 2010). Two stack compounds, two different proteasome entry points.

2. **Snail/c-Myc degradation.** DYRK2 phosphorylates Snail (SNAI1) and c-Myc, tagging them for ubiquitin-proteasome degradation. This is primarily a cancer biology mechanism; gout-relevance is indirect (Snail is not a primary inflammatory target in MSU flare biology).

3. **AMPK–mTOR interface.** DYRK2 contributes to AMPK pathway crosstalk; AMPK suppression of mTOR is the canonical autophagy-induction pathway that berberine and resveratrol operate through in the stack. The connection is weak and should be treated as Mechanistic Extrapolation.

## Connection to the Stack

The proteasome-regulation angle creates a previously unseen biochemical bridge between curcumin and EGCG:

- **EGCG inhibits the 20S proteasome** (chymotrypsin-like, IC50 = 86 nM). 20S is the core catalytic unit; inhibiting it slows protein degradation and can lead to accumulation of ubiquitinated substrates.
- **Curcumin inhibits DYRK2** (IC50 = 2.5 nM). DYRK2 facilitates 26S proteasome assembly (the 26S is the active form: 20S + two 19S regulatory caps). DYRK2 inhibition → disrupted 26S assembly → reduced proteasomal capacity by a different mechanism.

Whether these effects are additive or antagonistic in a combined stack depends on dosing and cellular context. At realistic oral doses of curcumin (~5% bioavailability, typical supplemental dose 500–1500 mg/day), the systemic curcumin concentration is unlikely to reach the 2.5 nM threshold except in the portal vein and upper GI. The DYRK2 hit may matter more for locally-produced curcumin in fermented-food or microbiome-delivery contexts.

## Why Priority Is Low (Not High)

- Single paper (*J Med Chem* 2023); not yet independently replicated in ChEMBL.
- Curcumin bioavailability crisis means systemic DYRK2 inhibition is pharmacologically implausible at typical oral doses.
- The proteasome connection is mechanistically interesting but gout-biology-distant compared to the direct NLRP3 IC50 = 24.2 μM or the EGCG 20S proteasome story.
- No pathway from DYRK2 inhibition → NLRP3 suppression is established in the literature.

## Action Required

**Minor propagation** to [nlrp3-inhibitor-screen.md](../wiki/nlrp3-inhibitor-screen.md) Tier-3 curcumin entry (do not elevate tier):

> As of 2026-07-01 ChEMBL v37 refresh: DYRK2 IC50 = 2.5 nM (*J Med Chem* 2023, pChEMBL 8.60) is now curcumin's rank-2 curated molecular target (between amyloid-β Ki = 0.208 nM at rank 1 and lactoylglutathione lyase Ki = 5.0 nM at rank 3). Evidence level: In Vitro. DYRK2 regulates proteasome activity via PA28γ phosphorylation — mechanistically adjacent to EGCG's 20S inhibition in the stack, through a different entry point. Gout-specific relevance is indirect; tier ranking unchanged.

## Pre-commit Verification Notes

Load-bearing number: DYRK2 IC50 = 2.5 nM, pChEMBL 8.60, *J Med Chem* 2023. Sourced from ChEMBL v37 REST API activity record. Not independently grep-verified against the primary paper. A future literature scan should confirm assay conditions (kinase activity assay? Cellular? Inhibitor concentration range?). Single-paper replication status is weak; mark as "requires independent replication" in any wiki entry.

## Status

Open — awaiting minor propagation to [nlrp3-inhibitor-screen.md](../wiki/nlrp3-inhibitor-screen.md). Low urgency; may bundle with a subsequent walkthrough.
