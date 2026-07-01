---
type: connection
sweep_date: 2026-07-01
sweep_sha: 18d3696
section_index: 2
global_index: 2
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# The LBP chassis (*E. coli* Nissle) may be superior to koji for expressing disulfide-rich proteins, offering a solution to the chaperone-load bottleneck.

2. **The LBP chassis (*E. coli* Nissle) may be superior to koji for expressing disulfide-rich proteins, offering a solution to the chaperone-load bottleneck.** *Supported*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `chaperone-orthogonal-stacking.md`, `engineered-lbp-chassis.md`, `koji-endgame-strain.md`, `daf-cd55-scr14-truncated-computational.md`, `c1-inh-protease-stability-ecn-computational.md`
   - *Page-pair linkage:* These pages are weakly connected. The chaperone framework documents a bottleneck in koji for PDI-heavy payloads like lactoferrin (16 disulfides) and DAF SCR1-4 (8 disulfides). The LBP chassis page discusses payloads like butyrate but doesn't explicitly frame the chassis as a solution for complex protein folding.
   - *Why It Matters:* The `koji-endgame-strain.md` aims to co-express multiple complex, disulfide-bonded proteins, but `chaperone-orthogonal-stacking.md` predicts this will lead to an "expression burden" from competition for the PDI/ERO1 folding machinery in *A. oryzae's* ER. The computational analysis for C1-INH (comp-037) demonstrates that *E. coli* Nissle's periplasmic DsbA/DsbC system can handle disulfide bond formation for a complex human serpin. This suggests that for PDI-heavy payloads like DAF SCR1-4 or lactoferrin, the EcN LBP chassis might be a superior production host, bypassing the eukaryotic ER bottleneck entirely. This reframes the LBP track from just a "durable colonization" play to a "superior protein folding" play for a specific class of difficult targets.
   - *Suggested Action:* Propose a computational experiment (comp-NNN) to model the expression and folding burden of DAF SCR1-4 and lactoferrin in an *E. coli* Nissle model, leveraging existing literature on prokaryotic disulfide bond formation systems. This would provide a direct in-silico comparison to the koji chaperone framework's predictions and inform which chassis is optimal for which payload.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The narrowing-to-C1-INH case is correct: comp-037 (`c1-inh-protease-stability-ecn-computational.md`) returned LOW (0.1) for strictly-degradative protease risk on the serpin body and GREEN for glycosylation feasibility in EcN — the DsbA/DsbC system can handle C1-INH's 2 disulfides. The synthesizer overreaches when generalizing to "PDI-heavy payloads like DAF SCR1-4 or lactoferrin" (8 and 16 disulfides respectively): comp-037 explicitly states its verdict applies *only* to the serpin-core construct and does NOT test EcN's capacity for 8–16 disulfide mammalian payloads. No comp-NNN has modeled DAF SCR1-4 or lactoferrin folding in EcN's periplasm. The correct framing: "C1-INH (2 disulfides) is computationally viable in EcN; whether the chassis scales to DAF SCR1-4 (8) or lactoferrin (16) is an open question requiring its own comp-NNN." The LBP-as-folding-chassis thesis is a worthwhile exploration vector — just tighten the claim to what comp-037 actually demonstrates.
