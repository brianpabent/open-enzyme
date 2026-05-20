---
type: experiment
sweep_date: 2026-05-17
sweep_sha: 768d99c
section_index: 2
global_index: 11
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# Combined colchicine + topical CBD:THC acute-flare protocol — retrospective n=1 data mining.

2. **Combined colchicine + topical CBD:THC acute-flare protocol — retrospective n=1 data mining.** *Cost: $0. Time: retrospective analysis (existing flare logs).* `[PHASE-A-MATCH: no]`

   - *What it tests:* Whether any of Brian's past flares (logged in private self-experiment storage per `self-experiment-protocol.md` §7) occurred during periods where both colchicine and topical CBD:THC were co-administered, and whether those flares had different duration/severity than colchicine-only flares. This is the cheapest possible first-pass test of Connection #2 — retrospective n=1, no new data collection.
   - *Protocol:* Review Brian's existing flare logs. Tag each flare by intervention status at onset (colchicine-only vs colchicine + topical CBD:THC vs prednisone vs other). Compare flare duration (hours from onset to 50% pain reduction) and peak pain score (0-10) across groups. n=1, uncontrolled, retrospective — purely hypothesis-generating.
   - *Decides:* Whether the dual-receptor, dual-route hypothesis (Connection #2 above) is worth a prospective n=1 A/B test.

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The retrospective-analysis idea is reasonable, but the cited support is wrong: `self-experiment-protocol.md` §7 says personal n=1 logs live in private storage and describes how to keep them out of the public repo; it does not establish that Brian has existing flare logs containing both colchicine and topical CBD:THC exposure. Reframe as "if historical logs exist with timestamped interventions and pain outcomes, mine them"; otherwise the cheapest first move is prospective logging, not retrospective analysis.

---

**WALKED 2026-05-19 — Closed (premise broken — Brian doesn't use colchicine; n=1 anchor captured for the actual protocol he uses instead).**

Pass 3 was directionally right but for a different reason than stated. Brian confirmed during the 2026-05-19 walkthrough: he doesn't take colchicine. He has topical CBD:THC logs but no colchicine logs to mine for the proposed combination. The retrospective-mining premise is broken at the data level, not the protocol level.

**However, Brian DOES have an n=1 observation for a different combined protocol** — the four-route layered (prednisone + topical CBD:THC + inhaled cannabis + ice) flare-interrupt used during a disc-golf-triggered prodromal rebound in 2026-05. That observation has been captured in `cannabinoids-terpenes.md` §4a "Brian's n=1 observation — four-route layered flare-interrupt" with appropriate epistemic-tier tags (n=1, uncontrolled, single observation, multi-intervention).

The colchicine + topical CBD:THC protocol (Protocol A in `gout-action-guide.md`) remains documented as a speculative future option for users on colchicine, but the retrospective n=1 test of it isn't runnable from Brian's current data. Future logging discipline going forward (per the prospective option Pass 3 noted) would generate the data if any combination user wanted to characterize it.
