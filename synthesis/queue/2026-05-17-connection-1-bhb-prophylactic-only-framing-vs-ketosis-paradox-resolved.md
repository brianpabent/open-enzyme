---
type: connection
sweep_date: 2026-05-17
sweep_sha: 768d99c
section_index: 1
global_index: 1
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# BHB prophylactic-only framing vs. "ketosis paradox resolved" in NLRP3 exploit map — an unresolved clinical-integration gap.

1. **BHB prophylactic-only framing vs. "ketosis paradox resolved" in NLRP3 exploit map — an unresolved clinical-integration gap.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: partial]`

   - *Documents Connected:* `bhb-ketones.md`, `nlrp3-exploit-map.md`, `gout-action-guide.md`
   - *Page-pair linkage:* `bhb-ketones.md` ↔ `nlrp3-exploit-map.md` are heavily linked (BHB is the canonical CP1-CP3 compound in the exploit map). `gout-action-guide.md` is a recent application surface (2026-05-08) with weaker linkage to both research pages.
   - *Why It Matters:* The propagated `nlrp3-exploit-map.md` retains the longstanding "ketosis paradox resolved" framing: *"With the engineered koji handling uric acid levels, ketosis becomes pure upside — all NLRP3 suppression, no uric acid penalty."* The trigger file `gout-action-guide.md` §"Active flare" and `bhb-ketones.md` §"Contraindications" now both carry an explicit **active-flare contraindication**: ketone bodies and urate compete for renal MCT/URAT1 reabsorption, producing a documented transient UA spike of 5–10% that can compound the flare. The two framings are not factually contradictory — one describes prophylaxis, the other describes active flare — but the exploit map's "ketosis paradox resolved" language reads as if the paradox is universally resolved, when in fact it is only resolved during intercritical periods. A reader of the exploit map alone would conclude that BHB + uricase = always safe, which is clinically dangerous during an active flare. The gap is not a mechanism error but a **clinical-integration gap** — the exploit map's mechanistic frame and the action guide's clinical frame disagree on the temporal boundaries of safety.
   - *Suggested Action:* Add a `⚠️ Active-flare contraindication` callout to `nlrp3-exploit-map.md` CP2 entry (BHB section), cross-referencing `gout-action-guide.md` §"Active flare," and soften the "ketosis paradox resolved" language to explicitly name the prophylaxis-only temporal boundary. The fix is a single sentence addition to the exploit map.

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The clinical-boundary concern is real, but the synthesizer's factual premise is stale: `nlrp3-exploit-map.md` already contains an explicit `⚠️ Active-flare contraindication` callout stating that BHB/ketosis is prophylactic only, that ketone bodies and urate compete for renal MCT/URAT1 handling, and that the transient ketotic UA rise of 5–10% can compound an active flare. The residual gap is narrower: the later "Ketosis Paradox Resolved" / "purely beneficial" language still needs softening, but a reader of the current exploit map alone would not miss the active-flare warning.
