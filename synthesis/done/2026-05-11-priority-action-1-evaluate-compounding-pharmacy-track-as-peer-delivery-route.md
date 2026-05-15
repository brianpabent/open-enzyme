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

---

## ✓ Actioned 2026-05-15 (partial-closure annotation)

Closing the queue item now and migrating the three closure-criteria checkpoints onto the canonical scope page. The queue surface was a tracking placeholder; once the criteria are explicitly mirrored at their proper home + the disulfiram dose-modeling comp-NNN is queued, the queue duplication is more cost than benefit. Specifically:

**Closure-criteria status:**

- **(a) Bulk API audit** — DEFERRED. Tracked at `synthesis/queue/2026-05-13-experiment-2-execute-the-compounding-pharmacy-bulk-api-audit.md`, which is **Item 11 of the current walkthrough**. The audit will be executed when that item comes up in this same walk. The scope page's Phase 2 §1 now points at the queue entry explicitly.
- **(b) Disulfiram dose modeling queued as own comp-NNN** — DONE. Queued as **comp-027** in [`computational-experiments.md` Planned Analyses](../../wiki/computational-experiments.md). Brief covers (i) disulfiram + DETC plasma PK, (ii) GSDMD-blockade EC50 in macrophage NLRP3-pyroptosis models, (iii) ratio of GSDMD-blockade-relevant plasma concentration to alcohol-deterrent threshold, (iv) sub-AUD dose window analysis. Priority: Medium-High. Scope page Phase 2 §6 now points at comp-027.
- **(c) Pharmacy partner identification with primary-source verification** — DEFERRED indefinitely as **user-action-required**. This is real-world outreach (Brian + collaborators), not Claude-actionable. Stays on the scope page Phase 2 §2 with `user-action-required` tag; not re-queued in the synthesis surface.

**Files shipped:**
- `wiki/computational-experiments.md` Planned Analyses — added comp-027 (Disulfiram dose modeling) row, brief drafted with primary-source citations (Hu 2020 Nat Immunol PMID 32152506).
- `wiki/compounding-pharmacy-track.md` Phase 2 list — added tracking-status preamble; each of the three criteria now annotated with **Tracked at:** pointer + **Status:** label.

**Six-surface tracking (per walk-synthesis skill §5):**
1. Scope page own Phase 2 list (above) — bulk API audit → Item 11 / comp-027 disulfiram → comp-027 / partner → user-action-required
2. `wiki/computational-experiments.md` Planned Analyses — comp-027 row
3. `synthesis/queue/2026-05-13-experiment-2-execute-the-compounding-pharmacy-bulk-api-audit.md` — still queued for Item 11
4. (no falsification card for compounding-pharmacy track yet; the scope page is the canonical surface)
5. (not surfaced on `index.md` — compounding-pharmacy track is a delivery menu, not a primary platform anchor)
6. This closure annotation + the queue→done move

The compounding-pharmacy track is **structurally** complete as a scope page; the three follow-ups have been moved to their proper canonical surfaces. The Phase 1 ask — "make the compounding-pharmacy option legible alongside the other peer tracks" — has been delivered.
