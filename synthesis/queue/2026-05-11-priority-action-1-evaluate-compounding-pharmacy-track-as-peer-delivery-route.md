---
type: priority-action
sweep_date: 2026-05-11
sweep_sha: user-introduced
section_index: 1
global_index: 17
pass3_verdict: User-introduced (not daemon-emitted)
overlap_tag: NEW
---

# Evaluate compounding-pharmacy delivery route as peer track to engineered fermentation

1. **Evaluate the compounding-pharmacy track as a peer delivery route alongside engineered koji / LBP / siRNA / medicinal-mushroom / TCM.** Scope page committed at [`wiki/compounding-pharmacy-track.md`](../../wiki/compounding-pharmacy-track.md). Trigger: Brian shared MINX/Veradermics screenshots 2026-05-11 with the framing "had not considered the compounding pharmacy angle. we should! we have identified lots of compounds and it might be easier to just make a pill than grow mold lol." The cleavage rule is sharp: small-molecule + FDA-approved API + off-patent or off-label → compoundable today (the MINX pattern); proteins / enzymes / biologics → fermentation chassis remains the route. The track is a delivery mechanism for the discovery engine's **repurposing surface** output (disulfiram, zileuton, and successors) — turning identification into patient access without the Veradermics-style multi-year NDA path.

**Phase 2 follow-ups queued on the scope page** (do not need separate queue items unless prioritized):

- Bulk API audit against FDA 503A and 503B lists for each candidate compound (disulfiram, colchicine custom doses, allopurinol custom doses, probenecid, zileuton, pentostatin).
- Compounding pharmacy partner identification (Empower, Olympia, others — primary-source verification).
- Physician partner pathway (rheumatology / functional medicine cross-section; possibly a fourth collaborator role per [`team.md`](../../wiki/team.md)).
- USP dissolution / characterization protocol library — mirrors `medicinal-mushroom-extract-sops.md` for the supplement track.
- Insurance / cost reality assessment.
- **Disulfiram dose modeling (comp-NNN candidate)** — what's the GSDMD-blockade-relevant plasma concentration vs. the alcohol-deterrent dose? Is there a dose window where GSDMD blockade dominates without producing the alcohol-flush effect? Highest-leverage single compound, would benefit from explicit dose modeling before any 503A prescription pathway opens.
- Sweep-daemon hook: flag whenever a new discovery-engine output has bulk API on the 503A list, making the compounding-track-relevance call automatic rather than ad hoc.

**Why this matters for the platform thesis:** Open Enzyme's two parallel outputs (per [`open-enzyme-vision.md`](../../wiki/open-enzyme-vision.md) §1–2) are the discovery engine and the strain library. The repurposing surface is a discovery-engine output that has historically been **scientifically interesting but operationally orphaned** — no canonical path from "FDA-approved drug X hits gout chokepoint Y" to "patient can take it." Compounding pharmacy closes that gap for the subset where the API is already approved. The MINX precedent (5 mg ER oral minoxidil → 503A pharmacy → dissolution test, days not years) is the proof-of-pattern: AI-aided formulation review + lipid matrix design + compounding pharmacy is the modern small-team analog of pharma reformulation.

**Why this is a queue Priority Action rather than a one-line wiki update:** the scope page exists now, but it crosses several open questions (regulatory, formulation, partner, evidence-development) that don't naturally belong to any single existing wiki page. The Priority Action lives here until the highest-leverage follow-up (almost certainly the disulfiram dose-modeling comp-NNN) gets queued as its own item.

**Closure criteria:** archive to `synthesis/done/` once (a) bulk API audit is published, (b) disulfiram dose modeling is queued as its own comp-NNN, and (c) at least one compounding pharmacy partner is identified with primary-source verification. Until all three land, this stays on the queue.
