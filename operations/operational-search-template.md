---
title: "Operational Search Artifact — Template & Document Class Definition"
date: 2026-05-06
status: template
tags: [operational, template, recruiting, outreach, resource-acquisition, methodology]
---

# Operational Search Artifact — Template

A reusable structure for any project bottleneck that is **not a scientific question but a resource-acquisition task** — obtaining a specific strain, accessing a specific collaborator, licensing a specific technology, sourcing a specific reagent, or recruiting a specific kind of expertise.

This is a formal document class introduced as part of the operations/ folder reframe (2026-05-05). The first instance is [`ward-1995-lab-access.md`](./ward-1995-lab-access.md) (lab access for the §1.9 koji dual-cassette feasibility experiment). Subsequent peer-track scope pages requiring specialized resources should instantiate this template rather than rediscover the structure.

---

## When to use this template

Create an operational search artifact when **all four of the following are true:**

1. **The bottleneck is resource-acquisition, not scientific question.** The platform has the rationale; what's missing is access to a specific lab, strain, technology, partner, reagent, or person. If the missing piece is "what experiment do we run?" the right artifact is a `validation-experiments.md` entry, not this template. If the missing piece is "who runs the experiment we already designed?" — this template applies.

2. **The space of candidates is multi-region / multi-vendor / multi-actor.** Not "we should call X." More like "we should map who in {Japan, China, Europe, US, commercial CROs} could possibly do this, identify the highest-leverage contact, and pursue the primary path while keeping fallback paths open." If there's only one candidate, this template is overkill — write the outreach plan directly.

3. **The candidates require explicit decision criteria** to compare. Different candidates have different tradeoffs (academic vs. commercial; cost; timeline; quality of fit; expressed interest; collaboration vs. fee-for-service; IP terms; geographic friction). Without a decision tree, the comparison degenerates into ad-hoc preference.

4. **The work is non-trivial enough that future-you (or future-Claude) needs to be able to re-enter it cold.** If the entire operational search would fit in a 5-line bullet list, just put it in `todos.md`. If it sprawls across regions, languages, IP databases, and partial conversations, codify it.

If any of those four are false, the resource-acquisition work is small enough to live in `todos.md` or as inline content in a wiki/scope page.

---

## Required structure

Every operational search artifact MUST contain these eight sections. Optional additional sections (region-specific deep-dives, repository deep-dives, IP landscape, etc.) compose around the required core.

### 1. Bottleneck statement

One paragraph naming what's missing and why it gates a downstream platform decision. Cross-reference the wiki page or experiment that surfaced the bottleneck. Be specific: "lab with *A. oryzae* protoplast transformation capability + protease-deletion strain access" beats "fungal engineering collaborator." The specificity is what makes the candidate-mapping tractable.

### 2. Global landscape map

Multi-region survey of candidates. Per the [global-multilingual research default](../CLAUDE.md) — language is not a barrier; map non-English-speaking regions as first-class options, not afterthoughts. Typical regions to consider:

- Geographic origin of the technology / strain / expertise (often the right primary lead — e.g., Japan for *A. oryzae*; Latin America for native crop-associated microbes; Eastern Europe for cold-adapted fermentation organisms)
- Currently-active research clusters (paper-count metric is a useful proxy)
- Industrial actors (different access posture — usually fee-for-service rather than collaboration, but sometimes spinout-to-startup paths exist)
- Commercial CROs (highest cost, lowest friction — useful as the timeline-gated fallback)
- Culture collections / repositories (strain-acquisition-specific path)

For each region, name **specific candidates** with: lead investigator(s) / institution / what they have / what's missing for them to be useful / contact pathway / language considerations. The lab-access page's §A-§E structure is the canonical pattern.

### 3. Single most-actionable lead

Of the mapped candidates, name the **one** that's the highest-leverage primary path. Justify briefly: why this candidate, why now, what's the asymmetric upside vs. the alternatives. The "single most-actionable lead" framing is load-bearing — it forces the artifact to NAME a primary path rather than offer a menu and leave the choice to the reader.

This is also where the realistic-engagement-note lives: what you actually expect to happen on first contact (warm response / cold rejection / silent / partial), what counts as enough engagement to invest more, what the next-action-after-first-contact is.

### 4. Parallel-path decision tree

Other candidates that should be pursued in parallel (or as gated fallbacks) while the primary path develops. Decision tree format:

- **Primary path** (Section 3): contact, expected response time, decision criteria for "this is working" vs. "this is stalling"
- **Parallel paths**: 1-2 alternates pursued simultaneously to avoid single-point-of-failure on the primary
- **Gated fallbacks**: paths that activate only if primary + parallels stall (typically commercial CROs or fee-for-service routes — higher cost / faster timeline)

The structure is decision-tree, not menu — each branch has a trigger condition and a next-action.

### 5. Order-of-operations / timeline

Time-sequenced plan. What to do this week, this month, this quarter. Anchor each step to a measurable trigger (response received / 14 days elapsed / decision made / etc.). Avoid "we'll see what happens" — name the decision points.

This section is what lets future-you (or future-Claude) re-enter the search cold and know what step we're on.

### 6. Draft outreach (if applicable)

If the primary path involves contacting specific people, include the draft outreach (email, LinkedIn DM, call script, etc.) as actual text. Not "send a message describing the project" — the literal draft text, with the recipient's specific context referenced and the specific ask named.

This is the operational equivalent of "show your work." A draft outreach in the artifact lets a collaborator (or future-you, or future-Claude) review tone / framing / specificity before sending. It also serves as a record of what was actually sent if the outreach goes ahead.

If outreach is multi-channel, include drafts for each channel.

### 7. Decision criteria — when to declare success / shift / abandon

Explicit thresholds. What outcome means the search succeeded? What outcome means we should shift to the gated fallback? What outcome means we should abandon the search entirely (e.g., "no path to *A. oryzae* protoplast transformation in any region within 6 months → fall back to *A. niger* chassis instead")?

Without this section, an operational search drifts indefinitely. With it, the search has a built-in resolution.

### 8. Cross-references

Link to:
- The wiki page or experiment entry that surfaced the bottleneck (the upstream gating)
- Any related falsification card (`wiki/hypotheses/H<NN>-*.md`) where the bottleneck shows up as a load-bearing assumption
- Sister operational search artifacts (other instances of the template — read each other for patterns)
- The platform-level reference: this template page itself + [`open-source-platform.md`](../wiki/open-source-platform.md) §"Platform Principles"

---

## Optional sections (compose as needed)

Per-instance, these compose around the required core when relevant:

- **Region-specific deep-dive** (per-country or per-cluster sub-sections — see lab-access page §A-§E for the canonical pattern)
- **Strain / repository deep-dive** (when the bottleneck involves obtaining a specific biological resource — see lab-access page §D)
- **IP / freedom-to-operate considerations** (when the bottleneck involves licensing or patent-cleared use)
- **Funding / cost structure** (when different candidates have different cost models that affect the decision)
- **Realistic engagement notes** (per-region cultural context: what works in Japan vs. China vs. Europe vs. US academic vs. industrial — the lab-access page §B "Realistic engagement note (China)" is a canonical example)

---

## Pattern-level guidance

### Bias toward inclusion of non-English-speaking candidates

Per [`CLAUDE.md` §"Global-multilingual research by default"](../CLAUDE.md): language is not a barrier in 2026. Map Japanese / Chinese / Korean / German / Russian / Spanish / Portuguese candidates as first-class options. Read original-language papers, websites, contact pages directly. The lab-access page treats Japan as the natural geographic + cultural fit primary lead specifically because Japan is the *A. oryzae* origin region — a Western-centric search would have missed Maruyama / Kitamoto entirely.

### The "single most-actionable lead" framing is doing real work

It's tempting to offer a balanced menu of options ("here are 5 candidates, pursue whichever resonates"). Don't. The whole point of the template is to FORCE the artifact to name a primary path. The reader can override, but they should override against a stated default rather than choose from a menu. Naming the primary path also forces the analytical work of *why* — which surfaces decision criteria that would otherwise stay implicit.

### Drafts before sends — collaborate on the outreach text

Section 6's "draft outreach (if applicable)" is the most-skipped section in early drafts. Include it. The literal draft text in the artifact is what lets a collaborator (or future-you reading after a 3-month gap) catch tone problems, missing context, or wrong-target framing before it goes out. Outreach that gets sent without this review step is the most-common source of "we tried that lab and got no response — wonder why" — usually because the message implicitly assumed shared context the recipient didn't have.

### Living document, not write-once

Operational searches evolve. Update the artifact when:
- A primary contact responds (move them from "primary path / pending" to "primary path / engaged" with a brief note on response substance)
- A parallel path gets explicitly ruled out (delete from active candidates; preserve in archive section if useful for future reference)
- A new candidate surfaces (add with the same structure; reassess primary lead if the new candidate is dominant)
- An order-of-operations step completes (mark done; queue the next step)
- The search criteria change (e.g., the underlying experiment design shifts and now needs different lab capabilities — restate the bottleneck and re-survey)

The artifact is the operational state of the search, not a one-shot scoping document.

---

## Provenance

This template was extracted from [`ward-1995-lab-access.md`](./ward-1995-lab-access.md) — the first instance of the operational search artifact document class — on 2026-05-06. Surfaced by the 2026-05-05 wiki sweep (Sweep B Connection 3 + Priority Action 3) which identified the lab-access page as introducing a wiki document class the existing taxonomy didn't have a slot for.

Existing taxonomy before this template:
- **Compound dossiers** (`wiki/<compound>.md`) — research content per compound
- **Experiment protocols** (`wiki/validation-experiments.md` § entries) — experimental design with cost / timeline / readouts
- **Scope pages** (`wiki/<modality-or-vector>-modality.md` / `<chassis>.md`) — peer-track exploration
- **Hypothesis cards** (`wiki/hypotheses/H<NN>-*.md`) — falsification cards with pre-registered thresholds
- **Computational experiment interpretive pages** (`wiki/<comp-NNN>-*.md`) — paired with `experiments/comp-NNN-*/` reproducible artifacts

The operational search artifact is a fifth document class — bottleneck-specific, decision-tree-structured, multi-region, with explicit primary-path naming. It lives in `operations/` rather than `wiki/` because it's transactional working state, not research content (per [`operations/README.md`](./README.md)).

---

## Cross-References

- [`ward-1995-lab-access.md`](./ward-1995-lab-access.md) — first instance; canonical example for §A-§E region-specific deep-dive structure
- [`README.md`](./README.md) — operations/ folder framing and document-class boundaries
- [`../CLAUDE.md`](../CLAUDE.md) — global-multilingual research default that operational searches inherit by default
- [`../wiki/open-source-platform.md`](../wiki/open-source-platform.md) — platform principles; this template is an operational complement to the methodology principles documented there
- [`todos.md`](./todos.md) — for resource-acquisition tasks that don't need the full template (single candidate, trivial scope, etc.)

---

## Candidate future instances (Phase 2 backlog)

When peer-track scope pages reach a resource-acquisition bottleneck, instantiate this template. Currently identified candidates:

| Bottleneck | Triggering scope page | When to instantiate |
|---|---|---|
| Engineered LBP chassis collaborators (Sonnenburg-lab alumni / Synlogic alumni / NextBiotix alumni / Pendulum alumni) | [`engineered-lbp-chassis.md`](../wiki/engineered-lbp-chassis.md) | When the LBP comp-008 feasibility analysis lands and the chassis selection narrows |
| Kidney-tropic siRNA conjugate-chemistry partner (Alnylam / Arrowhead / Dicerna / Acuitas / Genevant) | [`sirna-urat1-modality.md`](../wiki/sirna-urat1-modality.md) | When the comp-009 target-site selection lands and the conjugate-chemistry approach narrows |
| Standardized TCM extract sourcing (Smilax glabra, Si Miao San components, etc.) — Chinese suppliers | [`tcm-modern-rigor-intersection.md`](../wiki/tcm-modern-rigor-intersection.md) | When P2-2 / comp-013 ChEMBL cross-check identifies which TCM compounds are platform-relevant |
| Recombinant DAF SCR1-4 expression in *A. oryzae* — wet-lab capacity if H05 advances | [`hypotheses/H05-daf-scr14-cp0-thesis.md`](../wiki/hypotheses/H05-daf-scr14-cp0-thesis.md) | If the §1.9 dual-cassette result encourages triple-cassette OR if the LBP-chassis-as-DAF-host route is pursued |

These are pre-positioned, not assigned — the trigger is the upstream wiki / scope work reaching the resource-acquisition bottleneck, not a calendar date.
