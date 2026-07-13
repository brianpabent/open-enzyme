---
title: "ChEMBL discrepancy: Ursolic acid now has 16 curated entries pChEMBL ≥ 6 (was zero in v34)"
date: 2026-07-01
type: Connection
priority: Medium
tags: ["ChEMBL", "ursolic-acid", "ROR-gamma", "NF-kB", "SENP1", "Th17", "chembl-refresh"]
related:
  - ../wiki/nlrp3-inhibitor-screen.md
  - ../wiki/supplements-stack.md
  - ../wiki/etc/chembl-cross-check.md
source: "ChEMBL v37 quarterly refresh, 2026-07-01"
---

# ChEMBL Discrepancy: Ursolic Acid — 16 New Curated Entries (Zero at Baseline)

## What Changed

**Compound:** Ursolic acid (CHEMBL169, CAS 77-52-1)
**Baseline (ChEMBL v34, 2026-04-24):** Zero curated bioactivities at pChEMBL ≥ 6.
**Current (ChEMBL v37, 2026-07-01):** 16 curated entries at pChEMBL ≥ 6.

**Top four curated activities (as of ChEMBL v37):**

| Rank | Target | Activity type | Value | pChEMBL | Source |
|---|---|---|---|---|---|
| 1 | ROR-γ (RORC) | IC50 | 0.75 nM | 9.12 | *J Med Chem* 2023 |
| 2 | SENP1 | IC50 | 6.4 nM | 8.19 | *Eur J Med Chem* 2022 |
| 3 | HIV-1 (functional) | EC50 | 10 nM | 8.00 | *Eur J Med Chem* 2019 |
| 4 | NF-κB (p65) | IC50 | 31 nM | 7.51 | *Bioorg Med Chem* 2018 |

Evidence level: In Vitro (curated ChEMBL; multi-lab).

## Why This Matters

**[nlrp3-inhibitor-screen.md](../wiki/nlrp3-inhibitor-screen.md) frames ursolic acid as a Tier 1 NLRP3/NF-κB suppressor** based on functional animal-model data (IL-1β, NF-κB in OA and Kawasaki murine models). The previous ChEMBL note stated "no curated activity pChEMBL ≥ 6" — a zero-biochemistry flag.

That framing was correct for v34. As of v37, it is materially incomplete.

**ROR-γ at 0.75 nM** is the principal new finding. ROR-γ (RAR-related orphan receptor gamma; RORC gene; UniProt P51449) is the master transcription factor for Th17 cell differentiation and IL-17A/F production. Its relevance to gout:
- IL-17A is elevated in synovial fluid from gout patients (*Arthritis Rheum* 2012) and amplifies CXCL8/neutrophil recruitment in MSU-mediated flares.
- Th17 cells participate in chronic tophaceous gout and tophus maturation beyond the acute NLRP3/IL-1β phase that the platform primarily targets.
- ROR-γ inverse agonists are an active clinical-stage immuno-oncology and autoimmune target class; ursolic acid's IC50 is in the same potency range as early-clinical ROR-γ inhibitors.

This adds a Th17/adaptive-immunity coverage dimension to ursolic acid that was not surfaced in any current wiki page.

**NF-κB (p65) at 31 nM** converts the NF-κB claim from "functional/animal" (Mechanistic Extrapolation) to **In Vitro biochemical** (direct binding/inhibition). The wiki has consistently cited animal-model IL-1β reductions as evidence of NF-κB suppression — the curated 31 nM p65 IC50 from *Bioorg Med Chem* 2018 is the missing direct-binding link.

**SENP1 at 6.4 nM** is pharmacologically plausible as an anti-inflammatory mechanism: SENP1 de-SUMOylates and activates IKKβ (IκB kinase β); inhibiting SENP1 → sustained SUMO-IKKβ → reduced NF-κB signaling. This is mechanistically complementary to and partially synergistic with the direct p65 binding above, but through a different step in the cascade.

## Action Required

**Propagate to [nlrp3-inhibitor-screen.md](../wiki/nlrp3-inhibitor-screen.md) Tier 1 ursolic acid entry:**

Add a note (append, do not overwrite existing animal-model citations):

> As of 2026-07-01 ChEMBL v37 refresh: ursolic acid now has 16 curated entries pChEMBL ≥ 6 (zero in ChEMBL v34). Top targets: **ROR-γ IC50 = 0.75 nM** (*J Med Chem* 2023); **SENP1 IC50 = 6.4 nM** (*Eur J Med Chem* 2022); **NF-κB (p65) IC50 = 31 nM** (*Bioorg Med Chem* 2018). Evidence level: In Vitro.
>
> **ROR-γ inhibition** adds a Th17-axis mechanism not previously attributed to ursolic acid. ROR-γ drives IL-17A production in Th17 cells; IL-17A amplifies neutrophil recruitment in MSU-driven gout flares and contributes to chronic tophus biology (mechanistic extrapolation for gout-specific link; ROR-γ IC50 is direct biochemistry from *J Med Chem* 2023).
>
> **NF-κB (p65) IC50 = 31 nM** upgrades the NF-κB claim from Mechanistic Extrapolation to In Vitro (direct binding/inhibition curated in ChEMBL). This is the strongest direct-biochemistry support for the NF-κB dimension of ursolic acid's mechanism that the wiki has cited to date.
>
> Do not weaken the functional/animal citations — they are additive to this new biochemical evidence. Update the evidence-level label from "Mechanistic Extrapolation" to "In Vitro" for the NF-κB dimension.

**Also note in [supplements-stack.md](../wiki/supplements-stack.md)** ursolic acid entry: the ChEMBL update and ROR-γ finding.

## Pre-commit Verification Notes

Load-bearing numbers from this item:
- ROR-γ IC50 = 0.75 nM, pChEMBL 9.12: sourced from ChEMBL v37 activity record; journal listed as *J Med Chem* 2023. Not independently grep-verified against the primary paper. Flag if downstream propagation requires primary-source DOI verification.
- NF-κB IC50 = 31 nM: *Bioorg Med Chem* 2018, ChEMBL v37. Same caveat.
- SENP1 IC50 = 6.4 nM: *Eur J Med Chem* 2022, ChEMBL v37. Same caveat.

The ChEMBL REST API is treated as the primary source for this cross-check document; the above citations are from the ChEMBL-curated records themselves. A future literature deep-dive should verify the specific assay conditions (protein vs. cellular, concentration range, inhibitor type) before propagating to a primary mechanism wiki page.

## Status

Open — awaiting propagation to [nlrp3-inhibitor-screen.md](../wiki/nlrp3-inhibitor-screen.md) and [supplements-stack.md](../wiki/supplements-stack.md).

---

## ✓ Actioned 2026-07-13

Verified all three headline numbers directly against ChEMBL (CHEMBL169): **NF-κB p65 31 nM** (*Bioorg Med Chem* 2018, direct p65–DNA-binding ELISA) + **SENP1 6.4 nM** (*Eur J Med Chem* 2022) both SOLID; **ROR-γ 0.75 nM is REAL but cherry-picked** — the most-potent of 5+ records spanning **0.75–680 nM** (human 130–680, mouse 500–1,000). The propagation already existed in [`nlrp3-inhibitor-screen.md`](../../wiki/nlrp3-inhibitor-screen.md) (~line 113, 2026-07-01) but carried BOTH the cherry-picked 0.75 nM AND a "chronic gout/tophus biology" relevance claim. **Corrected the note:** ROR-γ as a range; NF-κB direct-biochemistry upgrade flagged as the load-bearing gout value; ROR-γ/Th17 reframed **curiosity-not-priority** because the 2026-07-13 chronic-tophus scoping scan found Th17/IL-17 is a **bystander not a driver** of tophus biology (single-cell tophus data + zero IL-17 gout trials incl. ChiCTR). No `supplements-stack.md` ursolic entry exists, so that half of the proposed propagation is n/a. Tophus finding captured in [`open-questions.md` §"Chronic tophaceous gout"](../../wiki/open-questions.md) + [`gout-pathophysiology.md`](../../wiki/gout-pathophysiology.md). Closure.
