---
type: open-question
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 1
global_index: 7
pass3_verdict: Confirmed
overlap_tag: RESTATEMENT
---

# Does the engineered-koji cordycepin route (cns1+cns2) face an ADA competition problem in *A. oryzae* that would require pentostatin co-engineering, and can the natural ADA-inhibitor pairing from *C. militaris* be replicated in koji?

1. **Does the engineered-koji cordycepin route (cns1+cns2) face an ADA competition problem in *A. oryzae* that would require pentostatin co-engineering, and can the natural ADA-inhibitor pairing from *C. militaris* be replicated in koji?** The comp-023 FBA does not model ADA kinetics; comp-025 is queued to address this. Meanwhile, the medicinal-mushroom-complement track documents that *C. militaris* natively co-produces pentostatin from the same BGC as cordycepin — a built-in ADA safeguard that koji lacks. If ADA competition is significant, the koji cordycepin route either needs pentostatin co-engineering (adding the cns3 kinase and the pentostatin biosynthetic genes) or must rely on exogenous ADA inhibitors (GLPP from the mushroom track). The cross-track synergy proposed in Connection 1 depends on the answer. (context: `cordycepin-cassette-burden-computational.md`, `medicinal-mushroom-complement-track.md`, `computational-experiments.md` comp-025)

> **Pass 3 review — Confirmed.** `[OVERLAP: RESTATEMENT]` This is already a named open gate in `cordycepin-cassette-burden-computational.md`: ADA competition is listed as a remaining risk because native ADA deaminates adenosine to inosine and FBA does not model the kinetic partition between ADA and cns1+cns2. The same page queues comp-025 specifically for ADA pool competition, and `medicinal-mushroom-complement-track.md` documents the natural *C. militaris* cordycepin + pentostatin BGC pairing. The open question is correctly framed, but it mostly restates the current queue rather than adding a new connection.
