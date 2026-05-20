---
type: contradiction
sweep_date: 2026-05-17
sweep_sha: 768d99c
section_index: 2
global_index: 9
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# Anakinra SC protocol is fully described in gout-action-guide.md and colchicine.md but absent from nlrp3-inflammasome.md CP5 and nlrp3-exploit-map.md CP5a — a propagation gap.

2. **Anakinra SC protocol is fully described in gout-action-guide.md and colchicine.md but absent from nlrp3-inflammasome.md CP5 and nlrp3-exploit-map.md CP5a — a propagation gap.** `[PHASE-A-MATCH: no]`

   - *Locations:* `gout-action-guide.md` §"Default path → This year (advanced)" and §"Active flare" (trigger file, contains full anakinra 100 mg SC × 3 days protocol, mechanism, cost, access). `colchicine.md` §4.3 comparison table (propagated file, lists anakinra SC as an option). `nlrp3-inflammasome.md` §"Chokepoint 5" (propagated file, lists anakinra and canakinumab but without the acute-flare protocol detail). `nlrp3-exploit-map.md` CP5a entry (propagated file, lists anakinra but without the protocol).
   - *Analysis:* The action guide now contains a detailed anakinra protocol — route clarification (SC in thigh/abdomen, NOT intra-articular), dosing (100 mg/day × 3 days), cost (~$900/flare), comparative advantage over prednisone (faster onset, narrower mechanism, cleaner cumulative burden), and the "bridge to inhaled mRNA-IL-1RA" strategic positioning. The research wiki pages (`nlrp3-inflammasome.md`, `nlrp3-exploit-map.md`) list anakinra as a CP5a option but don't carry the protocol detail or the cumulative-burden framing that would help a researcher understand *why* anakinra SC matters for recurrent-flare patients. This is a propagation gap — the action guide has richer clinical detail than the mechanism pages.
   - *Resolution:* Propagate the anakinra SC protocol (dosing, route, cost, cumulative-burden framing) from `gout-action-guide.md` into `nlrp3-inflammasome.md` §"Chokepoint 5" and `nlrp3-exploit-map.md` CP5a entry. The mechanism pages are the canonical research surface; the action guide is the application surface. Both should carry the core clinical detail.

   

---

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The propagation-gap claim is factually wrong for one of its two targets: `nlrp3-exploit-map.md` already includes the anakinra SC acute-flare protocol with route, 100 mg/day × 3 days dosing, NOT-intra-articular clarification, cost around $900/flare, cumulative-burden comparison with prednisone, and inhaled mRNA-IL-1RA bridge framing. `nlrp3-inflammasome.md` is less detailed and could still use propagation, but the finding should not say the protocol is absent from both mechanism pages.

---

**WALKED 2026-05-19 — Closed (anakinra SC protocol propagated to nlrp3-inflammasome.md §Chokepoint 5 only, per Pass 3 correction).**

Pass 3 correctly noted that `nlrp3-exploit-map.md` already had the full anakinra SC protocol detail. The daemon's claim about a propagation gap to BOTH mechanism pages was wrong on one of two targets.

Actioned:
- ✓ Added anakinra SC acute-flare protocol detail to `nlrp3-inflammasome.md` §Chokepoint 5 after the existing Anakinra (Kineret) bullet. Includes:
  - **Dosing/route:** 100 mg SC daily × 3 days, self-administered thigh/abdomen, NOT intra-articular.
  - **Cost framing:** ~$900/flare at retail (Brian's 2026-05-19 framing: cost is the practical access gate; finding an off-label prescriber is solved by cost-of-care budget — not a separate barrier).
  - **Cumulative-burden framing:** 3–6 flares/year × 30 years × prednisone cumulative steroid burden (bone loss, cataracts, adrenal suppression, glucose intolerance, mood/sleep/BP) vs anakinra's minimal cumulative burden (recombinant endogenous IL-1Ra, no bone/glucose/adrenal effects). Cleanest acute-flare-abort option *clinically available today* for recurrent-flare patients with significant lifetime steroid burden.
  - **Strategic-position framing:** anakinra is the near-term bridge while inhaled mRNA-IL-1RA develops on 5–10 yr horizon (same mechanism + chokepoint, different delivery route + economics).

Also closes:
- 2026-05-17 priority-action-1 (same propagation action; Pass 3 partly-obsolete correction noted nlrp3-exploit-map.md doesn't need the propagation).
