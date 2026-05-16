---
type: connection
sweep_date: 2026-05-15
sweep_sha: ebbce26
section_index: 1
global_index: 1
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The PDB-Engineered EcN + Compounded Disulfiram bridge forms a dual CP6 intervention spanning two delivery modalities.

1. **The PDB-Engineered EcN + Compounded Disulfiram bridge forms a dual CP6 intervention spanning two delivery modalities.** *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `purine-degrading-bacteria.md`, `compounding-pharmacy-track.md`, `chassis-pending-interventions.md`, `disulfiram.md`, `engineered-lbp-chassis.md`
   - *Page-pair linkage:* The PDB page recently documented the 2,8-dioxopurine anaerobe pathway and the CBT2.0 engineered *E. coli* Nissle strain achieving −63% plasma UA in mice (Li et al. 2025, PMID 41070194). The compounding pharmacy track and chassis-pending indices independently list disulfiram (CP6b GSDMD inhibitor) as a top repurposing candidate. None of these pages, however, propose the **combination** of an engineered anaerobic PDB probiotic for sustained gut urate → SCFA conversion with a compounded oral disulfiram pill for systemic GSDMD pore blockade.
   - *Why It Matters:* This pairing covers **both branches of CP6 simultaneously** — luminal urate disposal (CP6-upstream) via PDB + pyroptotic exit blockade (CP6b) via disulfiram — through non-overlapping chassis (EcN LBP vs. small-molecule Rx). Unlike the koji uricase platform, the PDB route is substrate-augmenting (generates butyrate that induces ABCG2), and disulfiram adds a mechanistically orthogonal anti-pyroptotic effect. Together they could achieve additive flare suppression and urate lowering without requiring a single organism to carry all functions. This is a **multi-chassis, multi-compound precision stack** that exploits the fact that neither arm requires koji’s secretion machinery or aerobic fermentation.
   - *Suggested Action:* Queue a comp-NNN feasibility analysis for dual-chassis EcN (PDB cluster from CBT2.0 + PULSE’s uricase, or PDB alone) and map the additive SUA reduction predicted from comp-019 + PDB butyrate ABCG2 induction. Simultaneously, model disulfiram’s GSDMD dose window (comp-027) to ensure co-administration timing aligns with the gut transit of the EcN product.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The combination is real and actionable: `chassis-pending-interventions.md` already records engineered PDB restoration / EcN CBT2.0 as an Animal Model urate-disposal intervention with −63% plasma UA in hyperuricemic mice (Li et al. 2025, PMID 41070194), and `disulfiram.md` documents disulfiram as a CP6b GSDMD Cys191 pore inhibitor with FDA-approved access and compounding-track relevance. Tighten the label from “both branches of CP6” to “urate-disposal / gut-lumen PDB + CP6b pyroptotic-exit blockade,” because urate disposal is upstream of the NLRP3 CP6 branches even if one wiki entry loosely labels PDB as CP6. Chassis is correctly downstream here: engineered EcN / LBP plus compounded small molecule should route as a multi-chassis stack, not be filtered for non-koji fit.

---

## ✓ Actioned 2026-05-16

Named the dual-chassis CP6 stack across four canonical surfaces with Pass 3's label tightening applied (urate-disposal upstream + CP6b pyroptotic-exit, not "both branches of CP6"):

- [`wiki/chassis-pending-interventions.md`](../../wiki/chassis-pending-interventions.md) — added new "## Multi-chassis stacks" section with entry M1 (PDB EcN × disulfiram) between the seven chassis-pending entries and the pending-triage list. Frames the strategic-reflection discipline directly: chassis is downstream of chokepoint, and stacks composed across chassis deserve the same chokepoint-first treatment.
- [`wiki/purine-degrading-bacteria.md`](../../wiki/purine-degrading-bacteria.md) — added "### Companion intervention: compounded disulfiram (CP6b downstream)" subsection at end of "Where This Fits in the OE Kill Chain," cross-linking disulfiram + chassis-pending M1 + comp-027/031.
- [`wiki/disulfiram.md`](../../wiki/disulfiram.md) — added "Companion intervention: PDB-engineered EcN" callout after the compounding-pharmacy callout, cross-linking PDB + chassis-pending M1 + comp-027/031.
- [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) — added comp-031 to Planned Analyses table (dual-chassis EcN PDB + uricase additive SUA prediction). comp-027 (disulfiram dose window) was already queued — no duplicate created. Both queued, neither spawned today; this item's action was the surfacing, not the running.

No new wiki page created (the composition lives across existing canonical pages with chassis-pending acting as the index). No new pages or sections beyond what's listed. No Phase 2 / Phase 3 follow-ups queued beyond the two comp-NNNs already in the Planned Analyses table.
