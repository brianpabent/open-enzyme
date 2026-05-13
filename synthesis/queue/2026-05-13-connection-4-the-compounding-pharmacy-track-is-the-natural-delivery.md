---
type: connection
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 4
global_index: 4
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# The compounding pharmacy track is the natural delivery mechanism for the discovery engine’s repurposing surface, and it completes a missing link in the platform’s “identify → validate → access” pipeline for small-molecule candidates.

4. **The compounding pharmacy track is the natural delivery mechanism for the discovery engine’s repurposing surface, and it completes a missing link in the platform’s “identify → validate → access” pipeline for small-molecule candidates.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `wiki/compounding-pharmacy-track.md`, `wiki/open-enzyme-vision.md`, `wiki/gout-action-guide.md`, `wiki/disulfiram.md`, `wiki/zileuton.md`
   - *Page-pair linkage:* `compounding-pharmacy-track.md` already cross-references `open-enzyme-vision.md` and the individual drug pages. However, `gout-action-guide.md` — the patient-facing entry surface — does not yet mention compounding pharmacy as an access path for repurposed drugs. The connection between “discovery engine identifies a candidate” and “patient can actually take it” is currently implicit; the compounding track makes it explicit.
   - *Why It Matters:* The Open Enzyme platform has a well-developed discovery engine that surfaces FDA-approved drugs hitting gout chokepoints (disulfiram, zileuton, avacopan). Until the compounding-pharmacy-track page, those candidates were scientifically interesting but operationally orphaned — there was no canonical path from identification to patient access. The compounding track closes that gap for the subset of candidates that are off-patent small molecules with available bulk API. For a patient reading `gout-action-guide.md`, the compounding angle converts “here’s an interesting mechanism” into “here’s how you might actually try this, with physician supervision.” The missing link is now explicit in the research wiki; it should also be surfaced in the action guide.
   - *Suggested Action:* Add a “Compounding pharmacy access” subsection to `gout-action-guide.md` under the “Future” or “This year” sections, linking to `compounding-pharmacy-track.md` and naming disulfiram and zileuton as the highest-priority candidates. Flag that this requires a physician partner and is not DIY.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` The pipeline gap is real: `compounding-pharmacy-track.md` explicitly says the repurposing surface was "operationally orphaned" and that compounding is the natural output side for FDA-approved small molecules, while `gout-action-guide.md` contains no compounding-pharmacy access path. The overreach is the access wording for specific candidates: the compounding page says disulfiram bulk API is available, but zileuton's bulk API availability is **uncertain** and queued for verification, so a patient-facing action-guide subsection should not imply zileuton is already compoundable.
