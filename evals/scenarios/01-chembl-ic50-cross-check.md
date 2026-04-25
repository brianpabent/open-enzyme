---
name: 01-chembl-ic50-cross-check
date: 2026-04-25
description: ChEMBL IC50 cross-check appendix on the inhibitor-screen page should propagate two-tier potency framing, species-gap caveats, and pathway-modulator vs direct-inhibitor distinctions across the rest of the wiki.
before_sha: c55ec09331283079fde836a65a02c8c0b9993c35
trigger_files: wiki/nlrp3-inhibitor-screen.md
expected_targets: wiki/oridonin.md, wiki/nlrp3-exploit-map.md, wiki/nlrp3-inflammasome.md, wiki/supplements-stack.md, wiki/cannabinoids-terpenes.md, wiki/gout-clinical-pipeline.md, wiki/GRAPH.md
golden_diff_sha: 9d09dcbad8992fbd1416f4034e86302001d80f7b
---

The trigger commit `c55ec09` added a ChEMBL IC50 cross-check appendix to
`wiki/nlrp3-inhibitor-screen.md`. Three findings in that appendix have
broad cross-doc implications:

1. **Two-tier potency framing**: most "NLRP3 inhibitors" in the wiki had
   no curated human IC50 in ChEMBL — only oridonin and dapansutrile do.
   Everything else should be re-tagged "pathway modulator" rather than
   "NLRP3 inhibitor."

2. **Dapansutrile species gap**: the published 1 nM mouse IC50 vs the
   1,000 nM human cellular IC50 is a 1000× gap that recontextualizes the
   2020 Phase 2a trial.

3. **Oridonin two-tier potency**: the cell-free covalent kinetics number
   (0.5–2 µM, Nat Commun 2018) and the cellular human THP-1 IC50 (5.18 µM,
   Eur J Med Chem 2023 via ChEMBL) measure different things and both are
   correct in context.

A good Pass 1 propagation would update the canonical concept pages
(`oridonin.md`, `nlrp3-inflammasome.md`, `nlrp3-exploit-map.md`), the
ranking tables (`supplements-stack.md`, `nlrp3-inhibitor-screen.md` itself
is already the source — should not be re-edited), the related compound
class page (`cannabinoids-terpenes.md` for beta-caryophyllene), the
clinical pipeline page (`gout-clinical-pipeline.md` for the dapansutrile
caveat), and the graph (`GRAPH.md` to reflect two-tier labeling). It
should NOT touch `wiki/synthesis.md` (Pass 2's job).
