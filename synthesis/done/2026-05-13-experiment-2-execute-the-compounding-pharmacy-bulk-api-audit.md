---
type: experiment
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 2
global_index: 7
pass3_verdict: Confirmed, prioritize
overlap_tag: RESTATEMENT
---

# Execute the compounding pharmacy bulk-API audit.

2. **Execute the compounding pharmacy bulk-API audit.** Cost: $0 (desk research). Time: ~1 week. Decides: which of the repurposing-surface candidates (disulfiram, zileuton, allopurinol, probenecid, colchicine) are actually on the FDA 503A and 503B bulk drug substances lists. This is the gating empirical question for the entire compounding-pharmacy track — without it, the track is a theoretical delivery route with no verified candidates. Queued as Phase 2 follow-up #1 in `wiki/compounding-pharmacy-track.md`; should be executed before any further compounding-track content is developed.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` This is the correct next action for the compounding track. `compounding-pharmacy-track.md` lists the "Bulk API audit" as Phase 2 follow-up #1 and calls it the gating empirical question for every candidate, with disulfiram marked available and zileuton explicitly uncertain. Because 503A/503B list status decides whether the entire delivery route exists for each compound, this desk audit should precede more formulation prose.

---

## ✓ Actioned 2026-05-15

**Brian flagged a red flag** in the candidate list: colchicine, allopurinol, probenecid are already first-line gout therapy — why would they appear on a "research these as potential repurposing candidates" list? Investigation revealed two layers of inaccuracy:

### Inaccuracy 1: Two different tracks were conflated

The original list mixed:
- **Discovery-engine repurposing candidates** — drugs NOT currently used for gout, identified by the discovery engine as hitting gout chokepoints (disulfiram, zileuton, pentostatin, lesinurad). For these, the 503A question is real.
- **Established gout drugs with custom-dose / custom-formulation potential** — drugs already in clinical use whose compounding play is *custom-dose / custom-formulation*, not novel mechanism (allopurinol, colchicine, probenecid). For these, the 503A question is settled public knowledge; the interesting question is clinical value-add of custom formulations.

The audit framing ("which compounds are on the FDA 503A list?") was wasted effort for the established-gout-drug subset.

### Inaccuracy 2: "On the FDA 503A list" was structurally wrong

The wiki implied a flat "is this drug on the list?" lookup. Per FDA's actual Section 503A guidance ([Bulk Drug Substances Used in Compounding Under Section 503A of the FD&C Act](https://www.fda.gov/drugs/human-drug-compounding/bulk-drug-substances-used-compounding-under-section-503a-fdc-act)), 503A allows three tiers:

- **Tier 1** — USP / NF monograph substances (first priority)
- **Tier 2** — Components of FDA-approved drug products (if no monograph applies)
- **Tier 3** — Formal FDA 503A bulks list — **only ~6 substances total** as of 2026-05-15 (Brilliant Blue G, cantharidin, diphenylcyclopropenone, NAG, squaric acid dibutyl ester, thymol iodide; all obscure topical compounds; none gout-relevant)

None of OE's candidates appear on Tier 3, and they don't need to — they qualify under Tier 1 or Tier 2:

| Compound | Tier | Real gating question |
|---|---|---|
| Disulfiram | Tier 2 (FDA-approved Antabuse) | Settled — bulk API widely available |
| Zileuton | Tier 2 (FDA-approved Zyflo) | Supplier-side bulk API supply (Zyflo distribution is small) |
| Pentostatin | Tier 2 (FDA-approved Nipent, IV) | Supplier-side bulk API supply + oral bioavailability unknown |
| Lesinurad | Tier 2 (FDA-approved 2015, withdrawn 2019) | **Regulatory edge case** — does Tier 2 survive market withdrawal? Only genuinely uncertain regulatory case in the set |
| Allopurinol | Tier 1 (USP) + Tier 2 (FDA-approved 1966) | Settled — clinical value-add of custom dose |
| Colchicine | Tier 1 (USP) + Tier 2 (Colcrys) | Settled — clinical value-add |
| Probenecid | Tier 1 (USP) + Tier 2 (FDA-approved 1951) | Settled — clinical value-add |

### Files shipped

- **`wiki/compounding-pharmacy-track.md`** — new "How Section 503A actually works" subsection between "Platform thesis expansion" and "What goes on this track" explaining the three-tier hierarchy with concrete examples. Updated "cleavage rule" sub-bullets to reflect Tier 1/Tier 2/Tier 3 distinction. Split "Routed to the compounding-pharmacy track" into two sub-subsections ("Discovery-engine repurposing candidates" and "Established gout drugs (custom-dose / custom-formulation track)"); re-ordered candidates accordingly; per-compound "Regulatory status" lines replaced with "503A eligibility: Tier N" framing.
- **`wiki/compounding-pharmacy-track.md` Phase 2 §1** — updated from "queued" to "completed 2026-05-15, finding reshapes the question" with summary of findings.
- **`wiki/gout-action-guide.md` compounding-pharmacy bullet** — Item 7's bullet reworded to reflect the two-track distinction (discovery candidates vs. custom-dose-of-established) and Tier 2/Tier 1 framing.

### Loose end carried forward

Lesinurad's post-withdrawal Tier 2 status is the only OE candidate where 503A eligibility is structurally uncertain rather than supply-chain-uncertain. Resolving it would require a state-board-of-pharmacy precedent search (have any 503A pharmacies compounded lesinurad post-withdrawal? has FDA explicitly opined?). Probably worth a future literature/regulatory scan but not load-bearing — probenecid is the URAT1 stand-in until lesinurad gets resolved. Logged as a Phase 2 follow-up in `compounding-pharmacy-track.md`.

Pass 3's "confirmed, prioritize" was correct that the audit was the right next action. The audit's finding — that the original framing was wrong — IS the audit's value. The compounding-pharmacy track now has a structurally accurate 503A eligibility model.
