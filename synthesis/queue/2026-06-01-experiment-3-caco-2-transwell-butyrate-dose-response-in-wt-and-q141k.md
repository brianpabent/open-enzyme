---
type: experiment
sweep_date: 2026-06-01
sweep_sha: 8a97f95
section_index: 3
global_index: 8
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Caco-2 transwell butyrate dose-response in WT and Q141K-transfected monolayers (basolateral application, 0.05–5 mM, dual readouts: ABCG2 apical-membrane surface expression + functional urate efflux).

3. **Caco-2 transwell butyrate dose-response in WT and Q141K-transfected monolayers (basolateral application, 0.05–5 mM, dual readouts: ABCG2 apical-membrane surface expression + functional urate efflux).** Cost: ~$500–1,500 (10 conditions × n=4 = 40 wells; antibody reagents shared with §1.14). Time: 4–6 weeks (can piggyback on §1.14 batch). Decides: minimum butyrate concentration that achieves Q141K rescue at the enterocyte nucleus — directly resolves the PDB-butyrate-Q141K concentration gap named in [`purine-degrading-bacteria.md` §"Q141K + PDB-butyrate + HDAC"](./purine-degrading-bacteria.md). WT response is PPARγ-mediated transcriptional induction; Q141K rescue is HDAC-mediated trafficking restoration. The dose-response shape should differ between WT (gradual induction) and Q141K (threshold-like rescue once HDAC inhibition is achieved). (Speculative — the dual readout is non-optional per Pass 3 tightening; the experiment has not been run.)

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The Caco-2 butyrate dose-response proposal (WT and Q141K-transfected, 0.05-5 mM basolateral, dual readouts) is faithfully derived from the concentration-gap framing in `abcg2-modulators.md` §"Q141K rescue mechanism" and `purine-degrading-bacteria.md`. The Basseville 2012 HDAC-rescue mechanism (1-5 mM in vitro) and the PPARγ WT induction mechanism are correctly separated. The claim that "the dose-response shape should differ between WT (gradual induction) and Q141K (threshold-like rescue)" is a strong, testable prediction that follows from the dual-mechanism biology. Cost estimate ($500-1,500) is plausible given piggybacking on §1.14 infrastructure. This directly resolves the PDB-butyrate-Q141K concentration gap, making it a high-information experiment at low marginal cost.
