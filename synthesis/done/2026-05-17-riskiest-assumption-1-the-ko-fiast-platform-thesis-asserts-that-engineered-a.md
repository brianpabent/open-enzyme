---
type: riskiest-assumption
sweep_date: 2026-05-17
sweep_sha: 768d99c
section_index: 1
global_index: 18
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The ko-fiast platform thesis asserts that engineered *A.

The ko-fiast platform thesis asserts that engineered *A. oryzae* koji can be reliably home- and community-fermented to deliver therapeutic doses of multi-cassette protein — a belief formalized in [`hypotheses/H09-community-fermentation-reliability.md`](./hypotheses/H09-community-fermentation-reliability.md) as the platform's #2 load-bearing risk (the #1 risk being the gut-lumen sink mechanism itself, per [H08](./hypotheses/H08-gut-lumen-sink-platform-thesis.md)). The new Plasmidsaurus QC pipeline in [`engineered-koji-protocol.md` §05](./engineered-koji-protocol.md) makes the strain-verification side of this assumption more tractable — $535 per strain build for outsourced plasmid + amplicon + genotyping + whole-genome sequencing means the "did my strain actually integrate correctly?" question is now answerable at Phase 0 cost. But the **community-fermentation reliability** side of H09 — batch-to-batch CV across N ≥ 10 independent home fermenters, strain retention ≥ 95% at generation 5, contamination < 5% per batch — has zero direct empirical evidence in the corpus. The Plasmidsaurus pipeline verifies that the strain is correct at build time; it does not verify that the strain remains correct after 5 generations of home propagation under variable kitchen conditions. The gap between "we can verify the strain at build time" and "the strain stays stable in 100 different kitchens" is the load-bearing uncertainty that H09 exists to formalize. The Plasmidsaurus pipeline closes the verification gap; the community-fermentation reliability gap remains fully open. Until a multi-user pilot (N=5–10, the H09 Phase 2 P2-2 queued item) returns data, the platform's accessibility thesis rests on the untested assumption that the Plasmidsaurus-verified strain survives home propagation. The cheapest discriminating experiment is the P2-2 multi-user pilot — ~$2,000–5,000 in genotyping + reagents, 4–8 weeks — which directly tests cross-user batch CV under the community-fermentation model. This experiment gates whether the "grow it at home like sourdough" thesis is actually achievable or collapses to the two-strain centralized-manufacturing fallback.



---

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the right riskiest-assumption call: `engineered-koji-protocol.md`'s Plasmidsaurus pipeline can answer build-time identity for plasmid, junction, clone, and final genome for roughly $535 in a typical single-cassette build, but H09 explicitly says community fermentation still lacks direct evidence for cross-user CV <30%, construct retention ≥95% at generation 5, and contamination <5%. The proposed multi-user pilot is the correct gate because sequencing a validated starting strain does not prove stability or dose reliability across kitchens.

---

**WALKED 2026-05-19 — Closed (P2-2 multi-user pilot already queued in H09; gates on wet-lab budget).**

Actioned:
- ✓ Verified `wiki/hypotheses/H09-community-fermentation-reliability.md` line 147 already queues P2-2: "Multi-user community-fermentation pilot trial design (N=5–10, single strain, central QC) | Foreground subagent + protocol authoring | Queued". The riskiest-assumption call is correctly encoded; the experiment exists in H09 Phase 2 Open Follow-Ups.
- Status: experiment design queued; gates on wet-lab budget allocation (~$2,000–5,000 in genotyping + reagents, 4–8 weeks). Same pattern as Cluster A1 — synthesis-level discipline is complete; remaining gate is budget-allocation, tracked in H09 Phase 2 table.
- Plasmidsaurus QC ($535/strain) closes the *build-time* strain-verification gap separately (`engineered-koji-protocol.md` §05); P2-2 specifically tests the *propagation-stability across kitchens* gap that Plasmidsaurus cannot answer.
