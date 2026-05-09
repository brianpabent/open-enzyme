---
type: connection
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 2
global_index: 2
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# Bacterial NRPS anticomplement peptides (complestatin class) are a previously unmapped payload for the engineered-LBP chassis.

2. **Bacterial NRPS anticomplement peptides (complestatin class) are a previously unmapped payload for the engineered-LBP chassis.** *Speculative*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `medicinal-mushroom-compound-mapping-computational.md`, `upstream-complement-modulator-sweep-computational.md`, `engineered-lbp-chassis.md`
   - *Page-pair linkage:* Weak. `comp-014` confirmed zero fungal direct C5aR1 modulators. `comp-018` independently surfaced bacterial NRPS-derived **complestatin** as a C5 inhibitor. Neither page connects this to the LBP chassis, which is the natural host for bacterial NRPS pathways. The LBP chassis page currently focuses on butyrate/Faecalibacterium — complestatin-family peptides are not mentioned.
   - *Why It Matters:* The Open Enzyme platform has only an engineering candidate (DAF SCR1-4) and a dietary-modulator backstop (rosmarinic acid) at CP0/upstream-CP0. A complestatin-producing engineered LBP would add a **third, mechanistically orthogonal** CP0 lever that operates via a completely different chassis (bacterial resident strain, continuous in situ production of anticomplement peptides). This composition would give the platform CP0 coverage via three independent modalities: engineered soluble complement regulator (DAF, expressed in koji), dietary small-molecule C3 convertase inhibition (rosmarinic acid/luteolin), and bacterial NRPS-derived C5 inhibitor (LBP). No other page in the wiki composes this three-avenue redundancy.
   - *Suggested Action:* Queue a Phase 2 follow-up (`comp-022` — complestatin-BGC heterologous-expression feasibility in *Bacteroides*/*E. coli* Nissle) on the engineered-LBP-chassis scope page. This is in silico only (codon usage, cluster size, precursor supply, toxicity) and does not require pharma-partner involvement to start.

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` The claim that “neither page connects this to the LBP chassis” is false: `upstream-complement-modulator-sweep-computational.md` §7.5 explicitly names “Bacterial NRPS complement chemistry as LBP payload class” and queues a complestatin-family BGC heterologous-expression comp-NNN for the engineered-LBP-chassis row; `computational-experiments.md` also lists “complestatin BGC LBP heterologous expression scope” as a comp-018 Phase 2 follow-up. The three-modality CP0 redundancy framing is a useful extension, but the payload/action is already mapped and queued, so the finding should not be emitted as “previously unmapped.”
