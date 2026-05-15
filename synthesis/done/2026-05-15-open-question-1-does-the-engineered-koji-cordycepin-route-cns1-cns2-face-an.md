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

---

## ✓ Already actioned 2026-05-15 (closure note — fully covered by existing queue + this walk's items)

Pass 3's RESTATEMENT verdict held. The ADA-competition question is already:

- **Named as an open gate** in [`cordycepin-cassette-burden-computational.md`](../../wiki/cordycepin-cassette-burden-computational.md) §"Impact on experimental priorities" #1 (ADA competition, FBA doesn't model the kinetic partition)
- **Queued as comp-025** in [`computational-experiments.md`](../../wiki/computational-experiments.md) Planned Analyses (ADA × cns1 substrate competition modeling — three orthogonal approaches: kinetic ADA Km vs. cns1 Km, FBA with stratified adenosine pool, Jeennor 2023 strain-background ADA-suppression check)
- **Documented in terms of the three downstream paths** if ADA competition is real:
  1. **Cassette-complexity path** — co-engineer pentostatin biosynthesis into koji (additional cassette + cns3 + pentostatin pathway genes; high complexity)
  2. **Cross-chassis-pairing path** — engineered koji cordycepin + whole-fermentate *C. militaris* extract for native pentostatin (Item 19; §2.7 stability test)
  3. **GLPP-supplement path** — engineered koji cordycepin + GLPP polysaccharide-binding ADA inhibition (Item 28; §1.26 sixth-arm assay)

comp-025's GREEN/YELLOW/RED verdict determines which downstream path wins. All three paths have wet-lab gates already queued in this walk (§2.7 + §1.26 sixth arm) OR documented as cassette-design follow-ups.

No new wiki work needed. Closing.
