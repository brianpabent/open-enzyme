---
title: "Chassis is downstream of chokepoint — operational discipline against chassis-filter narrowing"
status: open
created: 2026-05-15
class: strategic-reflection
related:
  - ./platform-framing-reframe.md
  - ../../wiki/chassis-pending-interventions.md
  - ../../wiki/modality-chokepoint-matrix.md
  - ../../wiki/delivery-route-matrix.md
  - ../../wiki/etc/open-enzyme-vision.md
  - ../../wiki/engineered-lbp-chassis.md
  - ../../wiki/sirna-urat1-modality.md
  - ../../wiki/purine-degrading-bacteria.md
---

# Chassis is downstream of chokepoint — operational discipline against chassis-filter narrowing

## Reflection

The platform's working thesis is **chokepoint-first, chassis-second**: identify what we want to hit (CP0–CP6b in the gout/NLRP3 cascade, plus urate disposal nodes), then choose the chassis based on what each intervention needs. The umbrella `CLAUDE.md` already encodes this in its "Curiosity and First-Principles Framing" section ("don't ask 'does this fit the current chassis,' ask 'what open question might this tool answer?'"). The Open Enzyme vision page already states it as project framing.

The discipline is not yet operationally enforced.

The 2026-05-15 PDB finding is the canonical case. The 2,8-dioxopurine pathway (Liu et al. 2023 Cell PMID 37541197 + Liu et al. 2025 Nat Microbiol PMID 40770490 + Li et al. 2025 Life Metabolism PMID 41070194) hits CP6 (urate degradation) and compounds via butyrate → ABCG2/Q141K rescue / NLRP3 dampening. **PDB is a real intervention against chokepoints we already prioritize.** The DOPDH enzyme is selenium-dependent, obligate anaerobic, prokaryote-specific (requires SelD selenophosphate synthase) — none of which fit *A. oryzae* koji. The recommendation step in the source research surfaced this as "not suitable for koji chassis → propose dual-chassis EcN" — itself a chassis-filter answer at a wider radius (which chassis covers which chokepoints) rather than a chokepoint-first answer (this is a real intervention; chassis is the next question).

The right framing: **PDB is a chassis-pending intervention.** Mechanism validated. Multiple candidate chassis exist (engineered EcN per the CBT2.0 precedent in Li 2025; FMT; defined-strain anaerobic probiotic; prebiotic enrichment). The chassis is open, not absent.

The risk this reflection names: the next finding may be one whose mechanism is real and important, but whose chassis we haven't built yet. If the recommendation step quietly filters that finding by current-chassis-fit, it dies before reaching the platform-question stage. The PDB finding survived this round because the mechanism was strong enough that the filter caught attention. Weaker findings in the same shape won't.

## What this reflection does NOT argue

- **Not "expand the platform to include EcN"** — that's still a chassis-filter answer, just at wider radius. The reframe is about *how* findings get evaluated, not *which* chassis we add.
- **Not "abandon koji"** — koji is the highest-priority chassis BECAUSE it harmoniously hits multiple chokepoints (uricase + lactoferrin + carnosine + DAF SCR1-4 in one strain), is food-grade, home-fermentable, and matches the open-source / democratized-access mission. Chokepoint-fit, not chassis-loyalty, is what makes it the priority.
- **Not "track everything"** — interventions still need to hit a documented chokepoint to land in chassis-pending. Mechanism without chokepoint-fit is not the target. The discipline is "don't filter by chassis-fit"; it is not "don't filter at all."

## Concrete operational changes

Four discipline-level changes operationalize the reframe. Each is small. Together they shift the default behavior from "filter quietly" to "track openly."

### 1. New canonical landing page: `wiki/chassis-pending-interventions.md`

Index of interventions that hit OE chokepoints with mechanism validated, but engineering / implementation / delivery chassis is not yet identified. PDB lands here as "needs anaerobic LBP or engineered EcN." Inhaled mRNA-IL-1RA lands here as "needs LNP + clinical partner." Phage-mediated selective gut suppression lands here as "needs phage manufacturing." Kidney-tropic siRNA against URAT1 lands here. Each entry frames the intervention as load-bearing, the chassis as open engineering question.

The page exists. The frame: these are *promising things* that *map to chokepoints we want to hit*; we don't know the chassis yet. Different from "deprioritized off-platform" (negative). Different from "chassis-agnostic" (implies findings don't care about chassis — they do, they need one).

### 2. Walk-synthesis closure question

Add to `.claude/skills/walk-synthesis/SKILL.md`: one explicit question per item — *"Does this finding hit a chokepoint we care about? If yes — does it have a chassis? If no chassis yet, log to `chassis-pending-interventions.md`."* Forces every closure to declare. The expand-cases get surfaced as platform questions, not buried.

### 3. Sweep daemon Pass 2/3 prompt language

Add to `scripts/sweep-prompt-2-synthesize.md` and `scripts/sweep-prompt-3-review.md`: "When evaluating a finding, ask first whether it hits a documented chokepoint. If yes, surface as an intervention regardless of current-chassis-fit. If no chassis is currently identified, route to chassis-pending-interventions, not to a deprioritized status."

### 4. Surgical wording reframe in existing pages

Where current pages say "doesn't fit our chassis" as if that closes the question, reframe to "Koji is the wrong chassis for this — [reason]. Candidate chassis: [enumerate]. Chassis selection is open." This is a 1–2 sentence edit in PDB / engineered-lbp-chassis / sirna-urat1-modality / medicinal-mushroom-complement-track pages. Same content; different framing.

## Why this is a discipline reflection, not a content reflection

The previous strategic reflection (`platform-framing-reframe.md`) asked whether substance had accumulated to justify expanding the project framing. Different question. That one is **content-triggered** — when the LBP / siRNA / TCM peer tracks reach Phase 2 maturity, decide whether to reframe vision pages.

This reflection is **discipline-triggered** — the chokepoint-first framing already exists at the umbrella level; the operational machinery to enforce it doesn't. The fix is workflow, not vocabulary. The vocabulary already says the right thing.

## Trigger

Already triggered. The PDB finding (2026-05-15) is the case study that surfaces the gap. No further accumulation needed before acting.

## Outcome

Three artifacts land in the same commit batch:

1. `wiki/chassis-pending-interventions.md` — the index page, populated with the current backlog (PDB, kidney-tropic siRNA, mRNA-IL-1RA pulse, phage selective suppression, intra-articular Pickering bioreactor, etc.).
2. Walk-synthesis SKILL.md addition — closure question.
3. Sweep daemon prompt addition — anti-chassis-filter language.
4. Surgical reframes in 3–4 existing pages where chassis-fit was used as a filter framing.

The reflection itself stays open as the discipline anchor — referenced by the index page, the walk-synthesis skill, and the sweep daemon prompts.

## Cross-reference

- Origin conversation: 2026-05-15 walk-through of PDB / GSDMD / kill-chain delivery research surfaced by parallel session, plus the chassis-pending reframe surfaced by Brian when reviewing the verification report. Specific framing: *"we're not looking for solutions that fit Koji. We're looking for solutions, sometimes Koji will fit the solution, and sometimes we'll need other things to fit the solution."*
- Sister reflection: [`platform-framing-reframe.md`](./platform-framing-reframe.md) — content-triggered project-framing reframe. This one is the discipline that ensures findings reach that reframe rather than being filtered before it.
