---
type: contradiction
sweep_date: 2026-05-16
sweep_sha: 91acf49
section_index: 1
global_index: 7
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# The platform's "koji-first" chassis narrative and its "chokepoint-first" discovery engine are in structural tension — and the chassis-pending-interventions.md page resolves this tension at the taxonomy level but not at the narrative level.

1. **The platform's "koji-first" chassis narrative and its "chokepoint-first" discovery engine are in structural tension — and the chassis-pending-interventions.md page resolves this tension at the taxonomy level but not at the narrative level.** Locations: `etc/open-enzyme-vision.md` §4 ("Koji-first platform") vs. `chassis-pending-interventions.md` ("chokepoint-first, chassis-second") vs. `modality-chokepoint-matrix.md` (multi-modality exploration surface). Analysis: The vision page states "The Open Enzyme platform is koji-first: A. oryzae is the primary host for the therapeutic stack." The chassis-pending page states "Open Enzyme is a chokepoint-first, chassis-second platform." These are not contradictory at the operational level — the chassis-pending page explicitly says "Koji is one expression of the mission, not the mission itself." But they are in narrative tension: a new reader arriving at the vision page sees a koji-centric platform; a new reader arriving at the chassis-pending page sees a modality-agnostic discovery engine. The resolution is that the platform has two outputs (strain library + discovery engine) and koji is the primary chassis for the strain library, but this two-output architecture is buried in `open-enzyme-vision.md` §2.2 and not reflected in the page's title or opening paragraphs. The narrative tension is real even if the operational tension is resolved.

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` The claimed narrative gap is overstated by a directly checkable file state: `wiki/etc/open-enzyme-vision.md` now opens with “Two parallel outputs of one project” and explicitly says the discovery engine is chokepoint-based, the strain library is the visible artifact, and “chassis is downstream of chokepoint.” The older Section 4 “Koji-first” language still creates some title/section-level tension, but the resolution is not buried in §2.2 and is absolutely reflected in the opening paragraphs; revise this from “structural narrative tension” to “legacy section-heading cleanup.”

---

**WALKED 2026-05-19 — Closed (heading updated in `wiki/etc/open-enzyme-vision.md`).**

Actioned:
- ✓ Edited `wiki/etc/open-enzyme-vision.md` line 138 heading: "Platform Choice — Koji-First, Yeast Retained for Specific Modules" → "Platform Choice — Koji-Primary Chassis, with Yeast Retained for Specific Modules". Removes the "first" exclusivity-temporal implication so the section heading aligns with the chokepoint-first framing in the page's opening paragraphs.
- Pass 3's verdict that the structural narrative tension was already gone (replaced by legacy section-heading cleanup) was the operational diagnosis; this commit closes the cleanup.
