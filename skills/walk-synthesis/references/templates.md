# Templates

Copy-paste scaffolds for the walkthrough. All dates ISO 8601 (YYYY-MM-DD); the annotation date is the calendar date the work shipped, not the originating sweep date.

## Actioned annotation (under the Claude review block)

```markdown
**✓ Actioned YYYY-MM-DD:** [What shipped — files, decisions, where canonical content lives now]. 
[Any new pages or sections created, with cross-links]. [Phase 2 follow-ups queued, with the 6-surface 
tracking pointers if applicable]. [Phase 3 reflection note location if relevant].
```

## Closure annotation (when nothing new needs to ship)

```markdown
**✓ Already actioned YYYY-MM-DD** (closure note): [Why no new work needed — point at where the canonical 
content already lives, with file/line references]. No additional wiki work needed for this [Connection / 
Contradiction / Open Question / Priority Action].
```

## End-of-item summary (Step F discipline — between every item and the next)

Post this as a Brian-facing message AFTER the closure-note commit and BEFORE briefing the next item. It forces explicit user disposition before walking on.

```markdown
**Item N done — summary + loose ends:**

**What landed:**
- [File 1] — [one-line what changed] (commit `<hash>`)
- [File 2] — [one-line what changed] (commit `<hash>`)
- [Key decisions taken]

**Loose ends:**

*Acceptably deferred* (already queued elsewhere; listing for completeness):
- [Loose end] → queued at [`location.md` §X]
- [Loose end] → queued as Phase 2 follow-up in [scope page]

*Needs disposition now* (could change the next item's framing or downstream work):
- [Loose end] — options: defer / action now / ignore. My recommendation: [option] because [reason].

*Carries over to Item X* (will surface in that future briefing):
- [Loose end] → anchored to Item X for explicit disposition there

**Item N closed?** [Wait for explicit user yes/next/go before briefing Item N+1.]
```

**Skip the loose-ends sub-headers if a category is empty.** A clean walk with no loose ends is just:

```markdown
**Item N done — summary:**
- [Files changed + commits]
- No loose ends.
**Item N closed?** Ready for Item N+1.
```

## Peer-track scope-page skeleton (frontmatter through cross-references)

```markdown
---
title: "[Modality / Vector] — [Peer Track Description]"
date: YYYY-MM-DD
tags: [primary, secondary, tertiary, platform-strategy, first-principles]
related:
  - modality-chokepoint-matrix.md
  - [parent-mechanism-page.md]
  - open-questions.md
  - open-enzyme-vision.md
  - synthesis/queue/
  - hypotheses/HNN-<thesis>.md
sources:
  - "[Key precedent 1 — citation]"
  - "[Key precedent 2 — citation]"
status: scope-page
---

# [Modality / Vector] — [Peer Track Description]

**Status:** scope-page (YYYY-MM-DD). [One-sentence mission statement].

## Why this page exists

[Frame the modality as a peer-track exploration vector under the broader gout-solving mission. Cite the 
matrix entry that surfaced it. Position relative to existing tracks: koji (primary), and any sister 
peer-tracks already scoped — e.g., LBP and siRNA / URAT1 are sister tracks under the chase-every-avenue 
framing established 2026-05-05].

## [Mechanism / What this is and why it matters]

[2–3 paragraphs. Plain English. Mechanism + why it matters for gout specifically.]

## Candidate [species / chemistries / approaches]

### Primary candidate
[Why this is the lead]

### Secondary candidates
[Why these are also in scope]

## [Key strength — the dual-action / sequence-specificity / durability angle]

[The mechanistic claim that makes this vector distinctive]

## The hard part: [delivery / regulatory / cost / etc.]

[The honest engineering / commercial / regulatory gating problem. Don't sugar-coat. Name the timeline 
honestly — "5–8 years" or "10+ years" if that's the truth.]

## Competitive / clinical landscape

[Existing programs, partner profile, what would compete with this and what wouldn't]

## Position in the Open Enzyme platform

[Discovery-engine output vs. strain-library output. Reference open-enzyme-vision.md §2.2 for the 
two-track narrative.]

## Comparison with [koji and any sister peer tracks]

[Table comparing dimensions: chassis, manufacturing, regulatory, distribution, capital, timeline, 
patient population, OE output type]

## Open Follow-Ups

[Numbered table P2-1 through P2-6 with ID / Item / Type / Status. Phase 3 entry at the end if relevant.]

## Limitations of this page

[Scope-page caveats; OE expertise gaps; honest uncertainty]

## Cross-References

[Bulleted list of every related wiki page]
```

## Falsification card stub (for new theses created during the walkthrough)

Modeled on `wiki/hypotheses/H02-engineered-lbp-thesis.md` and `H03-sirna-urat1-thesis.md`. Stub-level commit registers the hypothesis; full population is queued as Phase 2 P2-5. Stubs MUST include:

- Frontmatter (id, title, committed date, status: Stub, related, sources)
- Stub-status note (full population queued, pre-registration applies only on upgrade)
- Provisional Claim (the thesis in 1–2 paragraphs)
- Placeholder sections for: Assumption Stack, Killshot Menu, Pre-Committed Thresholds, Failure Modes Probed
- Status block (Pending / Survival count 0)
- Cross-references including sibling H-cards

## Tiered wet-lab protocol entry (for `validation-experiments.md`)

When a new wet-lab experiment has cost-escalating tiers gated on prior-tier results (e.g., §1.23 androgen × MSU × NLRP3):

```markdown
### 1.X [Title — Tiered Mechanistic Protocol]

**Status**: Proposed | **Cost**: Tier 1: $A; full T1+T2+T3 cascade $B–C | **Weeks**: Tier 1: D–E; full cascade ~F months | **Phase**: 1

**Affected wiki**: [list of related pages]

**What it tests:** [1 paragraph framing the literature gap and why this matters]

**Proposed in:** [synthesis/queue/ entry]

**Background on the gap:** [1 paragraph]

**Protocol — Tiered, gating logic:**

**Tier 1 — [Lowest-cost, broadest-cohort assay] ($A; D–E weeks):**
- [Cells / system]
- [Pre-treatment / variables]
- [Challenge]
- [Readouts]
- **Success criterion (Tier 1 → Tier 2):** [Specific quantitative threshold for advancement]

**Tier 2 — [Mid-cost, more-relevant assay] (gated on Tier 1 positive):**
- [Same structure]
- **Success criterion (Tier 2 → Tier 3):** [...]

**Tier 3 — [In vivo or gold-standard assay] (gated on Tier 2 confirmation):**
- [Same structure]
- **Success criterion:** [Causal demonstration or platform-implication threshold]

**Tier 4 (n=1, parallel and independent) — [if applicable]:** see [`self-experiment-protocol.md` §X].

**Estimated cost (full cascade):** [breakdown]
**Estimated timeline (full cascade):** [breakdown]

**Success criteria (overall):** [What each outcome means for the platform]

**Limitations:** [explicit list]

**Cross-references:** [related pages and sections]
```
