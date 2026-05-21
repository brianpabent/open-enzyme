---
type: experiment
sweep_date: 2026-05-21
sweep_sha: 3edb643
section_index: 1
global_index: 6
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Add concurrent omega-3 index measurement to the self-experiment protocol §13 pre-flare baseline panel and the C5a onset/resolution draws.

1. **Add concurrent omega-3 index measurement to the self-experiment protocol §13 pre-flare baseline panel and the C5a onset/resolution draws.** Cost: ~$50/flare (OmegaQuant add-on to existing blood draw). Time: 0 incremental — piggybacks on existing protocol. Decides: whether the C5a decline-slope prediction from `spm-resolution-pathway.md` §7.3 holds at n=1, and whether DHA SPMs provide genotype-informed CP0 coverage in a CFH 402H-positive subject. This is the single cheapest experiment that composes three previously disconnected threads (SPM resolution, CP0 complement, CFH genetics) into one falsifiable n=1 test. See Connection #2 above for the composition logic.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The experiment logic is good, but the proposed addition is already partly present: `self-experiment-protocol.md` §13 lists serum omega-3 index in the Protocol C pre-flare baseline panel, and the chokepoint-biomarker map already says C5a onset/resolution slope should be paired with concurrent omega-3 index. The useful remaining change is narrower: require omega-3 index to be event-linked for every C5a slope analysis and add the CFH 402H interpretation from `spm-resolution-pathway.md` §7.3 + `cfh-mechanism-dissociation-cp0-candidates-computational.md`. Do not file this as a de novo $50 add-on; file it as a protocol-tightening and genotype-annotation fix.
