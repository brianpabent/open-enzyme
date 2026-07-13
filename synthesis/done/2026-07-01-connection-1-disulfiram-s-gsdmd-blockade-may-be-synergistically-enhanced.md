---
type: connection
sweep_date: 2026-07-01
sweep_sha: 18d3696
section_index: 1
global_index: 1
pass3_verdict: Defer
overlap_tag: EXTENSION
---

# Disulfiram's GSDMD blockade may be synergistically enhanced by PDB-derived butyrate via metabolic pathway modulation.

1. **Disulfiram's GSDMD blockade may be synergistically enhanced by PDB-derived butyrate via metabolic pathway modulation.** *Speculative*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `disulfiram.md`, `purine-degrading-bacteria.md`, `chassis-pending-interventions.md`, `disulfiram-dose-modeling-computational.md`
   - *Page-pair linkage:* `chassis-pending-interventions.md` proposes a multi-chassis stack of PDB-engineered *E. coli* Nissle (EcN) and compounded disulfiram, framing them as hitting opposite ends of the urate-to-inflammation cascade (urate disposal vs. pyroptotic exit). This connection is novel because it proposes a direct pharmacological interaction, not just parallel mechanisms.
   - *Why It Matters:* The current model treats the two interventions as independent. However, purine-degrading bacteria (PDB) produce butyrate, a known HDAC inhibitor that can modulate hepatic gene expression. Disulfiram is metabolized by hepatic CYP enzymes. If butyrate alters the expression or activity of the specific CYPs that metabolize disulfiram, it could change disulfiram's pharmacokinetics, altering the therapeutically effective dose and the safety window defined in `comp-027`. This could either enhance the GSDMD-blocking effect (slower clearance) or increase side effects. This interaction is critical for safely co-administering what the platform already considers a promising multi-chassis intervention.
   - *Suggested Action:* Propose a computational experiment (comp-NNN) to perform a literature review on the effects of butyrate and other SCFAs on the specific CYP enzymes responsible for disulfiram metabolism (e.g., CYP2E1). If an interaction is plausible, a low-cost animal study measuring disulfiram/Me-DTC plasma levels in mice with and without butyrate supplementation would be warranted.

> **Pass 3 review — Defer.** `[OVERLAP: EXTENSION]` The central mechanism (PDB-derived butyrate modulates hepatic CYP expression → altered disulfiram PK) is a world-claim the corpus can neither confirm nor refute. No wiki page documents a butyrate × CYP2E1 (or any CYP) interaction — `disulfiram.md` does not mention CYP metabolism of disulfiram at all, and `purine-degrading-bacteria.md` §"SCFA Downstream Effects" documents butyrate's PPARγ, HDAC, XO, and NF-κB effects but nothing on hepatic CYP modulation. The synthesizer correctly tags this speculative, but the corpus has zero anchor for the pharmacokinetic interaction it hypothesizes. `[VERIFY: lit-scan]` butyrate/SCFA × CYP2E1/CYP3A4 expression in human hepatocytes; if no published interaction exists, the PDB × disulfiram stack described in `chassis-pending-interventions.md` §M1 is PK-clean by default (no interaction = no additive risk). The urate-disposal + GSDMD-blockade composition survives independently of this CYP hypothesis.

---

## ✓ Actioned 2026-07-13

Resolved via focused lit scan (do-the-work default, not corpus-absence deferral). **Verdict: PK-CLEAN by default.** The card conflated three things — butyrate's HDAC/CYP effects, disulfiram's own CYP2E1 *inhibition* (disulfiram is an inhibitor, not a substrate → CYP shifts don't swing its clearance), and disulfiram's covalent nM GSDMD blockade. No butyrate×CYP2E1 evidence exists (the two CYP2E1-induction papers used **β-hydroxybutyrate the ketone + palmitate**, not butyrate the SCFA); gut butyrate is exposure-limited (~3–4 µM systemic vs. 0.5–5 mM needed for hepatic CYP effects); GSDMD blockade is CYP-independent. Documented PK-clean in [`chassis-pending-interventions.md` §M1](../../wiki/chassis-pending-interventions.md) + [`disulfiram.md`](../../wiki/disulfiram.md). No dosing caveat, no experiment warranted. (A *pharmacodynamic* interaction via butyrate × pyroptosis-priming is not excluded — but that's upstream, not the CYP-PK claim.) Scan log: `logs/disulfiram-butyrate-cyp-pk-scan-2026-07-13.md`. Closure.
