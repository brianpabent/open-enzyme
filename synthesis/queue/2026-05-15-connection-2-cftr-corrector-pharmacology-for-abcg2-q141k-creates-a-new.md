---
type: connection
sweep_date: 2026-05-15
sweep_sha: ebbce26
section_index: 2
global_index: 2
pass3_verdict: Confirmed, prioritize
overlap_tag: RESTATEMENT
---

# CFTR-corrector pharmacology for ABCG2 Q141K creates a new small-molecule repair track orthogonal to butyrate/HDAC rescue.

2. **CFTR-corrector pharmacology for ABCG2 Q141K creates a new small-molecule repair track orthogonal to butyrate/HDAC rescue.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `chassis-pending-interventions.md`, `abcg2-modulators.md`, `compounding-pharmacy-track.md`, `modality-chokepoint-matrix.md`
   - *Page-pair linkage:* The chassis-pending page now lists “Pharmacological chaperones for ABCG2 Q141K folding rescue” as a standalone intervention, explicitly citing the CFTR-corrector precedent (ivacaftor/tezacaftor/elexacaftor for ΔF508 CFTR — same ATP-binding cassette superfamily). The ABCG2 modulators page already covers Q141K rescue via HDAC inhibitors (butyrate) but not via direct pharmacological chaperones. The compounding pharmacy track could serve as the delivery route for any repurposed corrector found in a computational screen.
   - *Why It Matters:* This opens a **genotype-targeted, small-molecule repair strategy** that is entirely independent of the koji chassis and the diet-microbiome axis. If an existing CFTR-corrector or similar compound binds Q141K ABCG2 and restores apical trafficking, it could be compounded as a daily pill for Q141K-positive gout patients — a population the platform has specifically stratified. The CFTR class has proven that small molecules can rescue misfolded ABC transporters; the gap is that no one has applied this chemistry to ABCG2 Q141K.
   - *Suggested Action:* The chassis-pending entry already proposes a comp-NNN (computational screen of FDA-approved correctors against Q141K ABCG2 AlphaFold structure). Prioritize this as a $0, subagent-friendly lit scan + docking study — it is the cheapest possible entry point and could directly surface a repurposing candidate ready for compounding.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` The finding survives, but it is mostly a promotion of an already first-class chassis-pending entry: `chassis-pending-interventions.md` §7 explicitly names “Pharmacological chaperones for ABCG2 Q141K folding rescue,” cites the CFTR-corrector precedent, distinguishes it from HDAC-mediated Q141K rescue, and proposes an AlphaFold / FDA-approved-molecule screen. The practical recommendation is still worth prioritizing because the current ABCG2 page covers HDAC/butyrate rescue in detail while this direct small-molecule conformational-rescue route remains chassis-pending and cheap to test computationally. Good chokepoint fit: gut/renal ABCG2 urate-disposal rescue, independent of koji.
