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

---

## ✓ Actioned 2026-05-15

Added a single bullet to `wiki/gout-action-guide.md` Default-path §"This year (advanced)" between self-experiment and Future-Phase-0:

- Names compounding-pharmacy access as a path, with the **requires physician partner; not DIY** qualifier in the bullet header.
- Disulfiram surfaced as the lead candidate (bulk API **confirmed**); references comp-027 for the dose-modeling gate.
- Zileuton + custom-dose colchicine / allopurinol / probenecid named in passing as "tracked at compounding-pharmacy-track.md, **pending bulk API verification**" — honoring the Pass 3 caveat that zileuton bulk API is uncertain.
- Cross-links to `compounding-pharmacy-track.md` for the full candidate list rather than duplicating it.
- Scoped to the **Default path only** for now; if the bulk API audit (Item 11, this walk) confirms broader candidates, the bullet can extend to the Androgen-elevated / Q141K-positive / Prevention paths in a follow-up sweep.

**Loose end picked up in same commit:** the existing "Genotype yourself — 23andMe or a clinical-grade panel" bullet at line 60 was reworked. Patient-facing copy now leads with clinical-grade testing (via rheumatologist or CLIA-grade direct-to-consumer service); consumer panels (23andMe, AncestryDNA) explicitly not recommended for gout-stack-relevant SNPs, with a brief note on data-ownership concerns. The reframe aligns the action guide with Brian's "doesn't trust consumer genetic testing" stance without making it Brian-internal — the patient-facing rationale (uneven data quality on specific variants + ToS data-ownership ambiguity) generalizes beyond Brian's personal preference.
