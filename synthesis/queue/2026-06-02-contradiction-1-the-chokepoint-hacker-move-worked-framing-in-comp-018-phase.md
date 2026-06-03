---
type: contradiction
sweep_date: 2026-06-02
sweep_sha: 405b50a
section_index: 1
global_index: 4
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# The "chokepoint-hacker move worked" framing in comp-018 Phase 2 is contradicted by the Phase 3 ChEMBL-verified empty chokepoints for NLRP3/ASC/Caspase-1.

1. **The "chokepoint-hacker move worked" framing in comp-018 Phase 2 is contradicted by the Phase 3 ChEMBL-verified empty chokepoints for NLRP3/ASC/Caspase-1.** *Locations:* upstream-complement-modulator-sweep-computational.md §"Chokepoint-hacker move worked"; nlrp3-exploit-map.md §CP2–CP4; medicinal-mushroom-compound-mapping-computational.md Phase 3. *Analysis:* comp-018 claimed that moving one node upstream from C5aR1 to C3 convertase opened dense TCM evidence (rosmarinic acid, luteolin, Bupleurum, Helicteres). comp-014 Phase 3 (6,798 fungal compounds) independently confirmed NLRP3, ASC, and Caspase-1 have zero fungal-source ChEMBL hits. The 2026-05-19 traditional-name re-scan resolves this: the chokepoints are not empty, they were query-framing empty. The "move worked" claim is directionally correct but overstated — it worked for CP0 (complement) but not for NLRP3 (CP2–CP4). This is a partial contradiction, not a full refutation. (source: medicinal-mushroom-compound-mapping-computational.md, upstream-complement-modulator-sweep-computational.md, logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md)

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The contradiction between comp-018's "chokepoint-hacker move worked" framing (dense TCM evidence surfaced by moving upstream to C3 convertase) and comp-014 Phase 3's initial "empty chokepoints" verdict for NLRP3/ASC/Caspase-1 is a real corpus-internal tension. The synthesis correctly identifies the resolution: the chokepoints were query-framing empty, not biology-empty — the 2026-05-19 traditional-name re-scan (documented at `medicinal-mushroom-compound-mapping-computational.md` §"Phase 3 NLRP3 empty chokepoint reversal") found ≥18 fungal sub-form × NLRP3-axis papers with ≥5 at the gout indication. The "partial contradiction, not a full refutation" framing is accurate: comp-018's move worked for CP0 but did not transfer to NLRP3, and the comp-014 verdict required revision. This contradiction was not previously named as such — the synthesis is doing genuine multi-document composition.
