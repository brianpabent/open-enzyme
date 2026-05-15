---
type: priority-action
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 2
global_index: 11
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Surface the compounding pharmacy track in `gout-action-guide.md` as an access path for repurposed drugs.

2. **Surface the compounding pharmacy track in `gout-action-guide.md` as an access path for repurposed drugs.** The action guide is the patient-facing entry surface; it currently references the engineered-strain pipeline and the supplement stack but does not mention that FDA-approved drugs hitting gout chokepoints (disulfiram, zileuton) can be accessed now via compounding pharmacy with a physician partner. Adding a brief “Compounding pharmacy access” subsection under “This year” or “Future” would close the gap between the discovery engine’s output and a patient’s ability to act on it.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` Surfacing compounding in `gout-action-guide.md` is correct and clinically consequential: I verified that the guide currently has no compounding-pharmacy section, while `open-enzyme-vision.md` and `compounding-pharmacy-track.md` already identify compounding as the delivery route for the repurposing surface. The proposed wording must be tighter than Pass 2's: disulfiram can be named as the high-priority candidate, but zileuton should be framed as conditional pending the bulk-API audit because `compounding-pharmacy-track.md` marks its bulk API availability as uncertain.

---

## ✓ Already actioned 2026-05-15 (closure note — covered by Items 7 + 10 in this walk)

Pure closure. Twin of Item 7 (2026-05-13 Connection 4); structurally covered by Item 7's edit and refined by Item 10's bulk-API audit.

**What landed (commits `61d191e` + `e36869d`):**

- `wiki/gout-action-guide.md` Default-path §"This year (advanced)" — new compounding-pharmacy bullet added 2026-05-15 (Item 7).
- Reframed 2026-05-15 (Item 10) with the proper Section-503A Tier-2 framing + discovery-vs-custom-dose distinction.

Current bullet honors Pass 3's caveat — disulfiram is the lead discovery candidate (Tier 2, supply confirmed, comp-027 dose-modeling queued); zileuton + pentostatin + lesinurad are Tier 2 with supplier-side supply questions (not implied as already compoundable); allopurinol + colchicine + probenecid are surfaced as the custom-dose / custom-formulation track distinct from the discovery candidates. Patient-facing copy is honest about which path is which.

No new wiki touch needed for this priority action. Closing.
