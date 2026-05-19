# Pass 3 Failure-Mode Retrospective — 2026-05-19

**Triggered by:** Brian's 2026-05-19 walkthrough observation in cluster E (lactoferrin / DAF generalization). Pass 2 errors get caught by Pass 3 + Brian. Pass 3 errors get caught only by Brian. This audit quantifies the Pass 3 failure-mode frequency + types from prior closure annotations in `synthesis/done/`.

**Crawl scope:** 142 closed synthesis items in `synthesis/done/` spanning sweep cycles 2026-05-09 → 2026-05-17, with walkthrough closures dated 2026-05-14, 2026-05-15, 2026-05-16, 2026-05-19. Verdict-tag tally: 49 Confirmed-prioritize, 38 Confirmed, 27 Push back, 24 Partial, 3 Augment, 1 user-introduced (total = 142).

---

## Summary

- **Eight distinct Pass 3 failure modes** identified across the crawl. Three were surfaced in the 2026-05-19 walkthrough (cortisol circular dismissal, substrate-engineering under-claim, anakinra scope confirmation). Five additional modes were documented in earlier walkthroughs and are already named in `scripts/SWEEP-ARCHITECTURE.md` (trigger-file awareness gap, static-rubric bias, stale-recommendation flavor, novelty-over-operational under-weight, named-in-prose vs queued-with-comp-NNN-ID).
- **Pass 3 failure modes cluster into three families:** (a) **epistemic-gate errors** — Pass 3 applies the wrong filter (circular "not documented," novelty-over-operational, scope-confirmation without platform-relevance audit); (b) **structural-architecture errors** — Pass 3 lacks the context to grep correctly (trigger-file blindness, anchor-format mismatch); (c) **recommendation-bias errors** — Pass 3 inherits Pass 2's bias toward additive recommendations without auditing whether the addition is redundant or stale (static-rubric, stale-recommendation, under-deduping).
- **Frequency is low against denominator but consequential per incident.** Roughly **9 walked items out of 71 walkthrough-closed items (~12.7%)** carry an explicit Pass 3 critique annotation; most other items honored Pass 3's verdict cleanly. But each Pass 3 failure that lands unchecked propagates to downstream synthesis (the H2 cortisol case was dismissed in Pass 3, lit scan only fired after Brian's intervention; the J3 substrate case was confirmed-prioritize at 1× scope, only became Platform Principle 9 after Brian's reframe).
- **The structural-architecture failure modes have already been routed to durable infrastructure fixes** — `scripts/SWEEP-ARCHITECTURE.md` carries named sections for trigger-file awareness gap, static-rubric bias, and stale-recommendation bias, each with proposed prompt/orchestrator fixes. The epistemic-gate failure modes (circular dismissal, scope-confirmation, under-claim of operational value) are not yet routed to Pass 3 prompt updates.
- **Single-point-of-failure asymmetry confirmed.** Of the eight failure modes, only one (trigger-file awareness) has had a daemon-side architectural fix queued; six were caught by Brian during walkthrough only. The human-walkthrough gate is currently the sole detector for the epistemic-gate class.

---

## Failure-mode typology (with frequency counts)

### 1. Circular dismissal ("not documented → don't investigate")

**Pattern:** Pass 3 dismisses a Pass 2 connection by noting the proposed mechanism is not yet documented in primary literature, treating absence-of-citation as disqualifying. Inverts the project's curiosity rule (umbrella `CLAUDE.md` §"Curiosity and First-Principles Framing"): connection-the-dots is the work, not the disqualifying condition.

**Frequency:** 1 confirmed instance (H2, 2026-05-19 walkthrough). Recently added 2026-05-19 to the recognized typology — no prior instances were named under this label in the closure-annotation crawl, though the inversion-of-curiosity-rule logic was already articulated in the umbrella CLAUDE.md as a general project discipline.

**Canonical example:** [2026-05-17-connection-7-bhb-s-cp1-cp3-coverage-the-cortisol-fasting-stress-axis-an.md](../synthesis/done/2026-05-17-connection-7-bhb-s-cp1-cp3-coverage-the-cortisol-fasting-stress-axis-an.md) line 30. Pass 3 dismissed the BHB × cortisol × MSU connection with "no documented gout-specific cortisol-rebound mechanism." The lit-scan subagent (fired after Brian overruled) found substantial direct mechanistic evidence including 2026 FASEB J Diaz-Jimenez/Cidlowski PMC12862736 myeloid-GR-knockout MSU peritonitis study.

**Also touches:** [2026-05-17-open-question-1-does-prolonged-fasting-in-gout-patients-produce-a.md](../synthesis/done/2026-05-17-open-question-1-does-prolonged-fasting-in-gout-patients-produce-a.md), [2026-05-17-experiment-1-bhb-cortisol-interaction-during-fasting-in-a-gout-patient-a.md](../synthesis/done/2026-05-17-experiment-1-bhb-cortisol-interaction-during-fasting-in-a-gout-patient-a.md) (same cluster).

---

### 2. Confirmation under-claim (substrate-as-engineering-lever pattern)

**Pattern:** Pass 3 confirms Pass 2's framing of an item as documentation-discipline / QC-anchor / nice-to-have, without recognizing the deeper first-principles question the item points at. The recommendation lands at ~10× lower scope than the substantive insight warrants.

**Frequency:** 1 confirmed instance (J3, 2026-05-19 walkthrough). A second instance (the "novelty over operational" mode below) is closely related but rhetorically distinct.

**Canonical example:** [2026-05-17-connection-6-substrate-accumulated-plant-flavonoids-in-cultivated.md](../synthesis/done/2026-05-17-connection-6-substrate-accumulated-plant-flavonoids-in-cultivated.md) line 25. Pass 3 confirmed-prioritize the "add substrate-accumulated vs biosynthesized annotation column" SOP edit. Brian's reframe: "*if we're growing something, can we get more or better compounds by changing the substrate?*" — substrate as engineering lever, not confound to document. The reframe drove a multilingual lit scan ([logs/substrate-engineering-mushroom-cultivation-lit-scan-2026-05-19.md](./substrate-engineering-mushroom-cultivation-lit-scan-2026-05-19.md)) documenting 1.2×–100× substrate-driven yield effects across multiple species, ultimately promoted to Platform Principle 9.

---

### 3. Scope-confirmation without platform-relevance audit

**Pattern:** Pass 3 confirms an audit / experiment / open-question's full scope without pushing back on platform-irrelevance of one or more sub-questions. Scope-tightening lands only at walkthrough.

**Frequency:** 1 confirmed instance (L2, 2026-05-19 walkthrough). The explicit annotation flags this as "another Pass 3 failure mode worth logging for the end-of-walk retrospective."

**Canonical example:** [2026-05-17-open-question-2-what-is-the-real-world-accessibility-of-off-label-anakinra.md](../synthesis/done/2026-05-17-open-question-2-what-is-the-real-world-accessibility-of-off-label-anakinra.md) line 26. Pass 3 confirmed-prioritize the original accessibility audit's three-part scope (insurance + prescriber-willingness + patient-experience). Brian's scope-tightening: insurance + prescriber-willingness OUT (platform-irrelevant — "easy to find a doctor who will prescribe anything off-label with enough money"); only patient-experience IN.

**Also touches:** [2026-05-17-experiment-3-anakinra-sc-accessibility-audit-insurance-coverage-and.md](../synthesis/done/2026-05-17-experiment-3-anakinra-sc-accessibility-audit-insurance-coverage-and.md) (same cluster, duplicate framing).

---

### 4. Novelty-over-operational under-weight (named-in-prose ≠ queued-with-comp-NNN-ID)

**Pattern:** Pass 3 over-weights "is this novel?" as the verdict axis and under-weights "does this make the corpus better operationally?" If the proposed addition has been "named in passing" in a prose follow-up list, Pass 3 calls it not-novel and downgrades the recommendation, even when the operational consolidation has independent value (deduplication, stale-divergence prevention, comp-NNN ID assignment).

**Frequency:** 2 explicitly named instances (2026-05-09 connection-1 + connection-2, both 2026-05-14 walkthrough). The 2026-05-09-connection-4 closure annotation explicitly logs this as a "Second Pass 3 failure-pattern observation" and proposes prompt-tweak threshold: "if a third instance lands, propose prompt tweak to `scripts/sweep-prompt-3-review.md` adding an operational-improvement axis to the verdict rubric."

**Canonical example:** [2026-05-09-connection-4-the-tiered-quantification-ladder-kitchen-smartphone-bench.md](../synthesis/done/2026-05-09-connection-4-the-tiered-quantification-ladder-kitchen-smartphone-bench.md) lines 25, 35. Pass 3 called Pass 2's novelty claim overstated (the cross-track transfer was already named in SOP-6). Brian's call: "stale-data risk = consolidate, novelty isn't the right criterion." Resolution: created `wiki/quantification-ladder.md` as the canonical framework page.

**Related:** [2026-05-09-connection-1-clockbase-autonomous-screening-methodology-maps-directly.md](../synthesis/done/2026-05-09-connection-1-clockbase-autonomous-screening-methodology-maps-directly.md) and [2026-05-09-connection-2-bacterial-nrps-anticomplement-peptides-complestatin-class.md](../synthesis/done/2026-05-09-connection-2-bacterial-nrps-anticomplement-peptides-complestatin-class.md) — both flag "Pass 3 conflated 'named in a Phase 2 follow-up list' with 'queued as a formal comp-NNN row.'"

---

### 5. Pass 3 trigger-file awareness gap (structural-architecture)

**Pattern:** Pass 3's grep returns a false-negative against trigger-commit content because the reviewer has no awareness of which content is new in this sweep cycle. The reviewer can't distinguish "Pass 2 hallucinated a section" from "Pass 2 saw a brand-new section just added in the trigger commit."

**Frequency:** 1 explicit instance (2026-05-15-connection-4), but explicitly named as a structural Pass 3 architecture gap that affects every sweep where Pass 2 cites trigger-commit content. Documented in [`scripts/SWEEP-ARCHITECTURE.md` §"Pass 3 trigger-file awareness gap"](../scripts/SWEEP-ARCHITECTURE.md) lines 468–486 with the canonical empirical example and proposed orchestrator+prompt fix.

**Canonical example:** [2026-05-15-connection-4-the-rfdiffusion-proteinmpnn-tool-gap-closed-by.md](../synthesis/done/2026-05-15-connection-4-the-rfdiffusion-proteinmpnn-tool-gap-closed-by.md) line 28. Pass 3 push-back said both "BioDesignBench" and "protein-design-mcp" terms were absent from `wiki/etc/bio-ai-tools.md`. They were present at lines 752 and 810+, added in the trigger commit Pass 3 was reviewing.

**Status:** Daemon-side fix queued (orchestrator computes trigger-commit diff, injects as Pass 3 context). Tracked in SWEEP-ARCHITECTURE.md "Open improvements."

**Also touches:** anchor-format mismatch (a milder variant) — [2026-05-16-contradiction-1-the-chaperone-orthogonal-stacking-framework-s-coefficient.md](../synthesis/done/2026-05-16-contradiction-1-the-chaperone-orthogonal-stacking-framework-s-coefficient.md), [2026-05-16-open-question-1-can-the-chaperone-orthogonal-stacking-framework-s.md](../synthesis/done/2026-05-16-open-question-1-can-the-chaperone-orthogonal-stacking-framework-s.md). Pass 3 grepped literal `1.25` (with period) but the wiki anchor was `#125-…` (no period); the grep missed the section header but found the link text. Same root pattern: Pass 3's grep precision is brittle against the live corpus.

---

### 6. Static-rubric bias (recommend documenting what the daemon already does dynamically)

**Pattern:** Pass 3 confirms Pass 2's recommendation to add a static decision framework / rubric / triage rule for a process the sweep daemon's Pass 2 already implements dynamically against the live corpus. Adding a static doc would be a snapshot of heuristics that drifts from the live evaluator faster than the evaluator updates.

**Frequency:** 1 explicit instance (2026-05-15-contradiction-1, walked 2026-05-16). Named in [`scripts/SWEEP-ARCHITECTURE.md` §"Recommend creating what already exists" bias in Pass 2 + Pass 3](../scripts/SWEEP-ARCHITECTURE.md) lines 420–462, with operational guidance for future walkthroughs.

**Canonical example:** [2026-05-15-contradiction-1-the-chassis-pending-intervention-list-risks-diluting-the.md](../synthesis/done/2026-05-15-contradiction-1-the-chassis-pending-intervention-list-risks-diluting-the.md) line 24. Pass 3 confirmed-prioritize Pass 2's "chassis triage rubric" recommendation. Brian's pushback: "the daemon's Pass 2 already re-evaluates every chassis-pending entry against current corpus state on every sweep, and the walkthrough operator's per-item decision IS the promote / park / falsify call. A static rubric would be documentation that re-derives what Pass 2 already does, drifting from the live evaluator faster than the evaluator updates."

---

### 7. Stale-recommendation bias (recommend adding what already exists)

**Pattern:** Pass 2 / Pass 3 recommends adding a wet-lab experiment section / comp-NNN / cross-link that was already added in an earlier sweep cycle. Pass 3 sometimes catches this with `[GAP: tool-gap]`, but the cycle of "recommend additions of stale artifacts" is itself a bias both passes inherit.

**Frequency:** 1 explicit instance where Pass 3 correctly flagged it (2026-05-15-priority-action-1). Named in `scripts/SWEEP-ARCHITECTURE.md` lines 441–445 as the "stale-recommendation flavor" of the broader "recommend creating what already exists" bias.

**Canonical example:** [2026-05-15-priority-action-1-add-validation-experiments-md-2-7-koji-cordyceps-co.md](../synthesis/done/2026-05-15-priority-action-1-add-validation-experiments-md-2-7-koji-cordyceps-co.md). Pass 3 correctly flagged the staleness with `[GAP: tool-gap]`. The walkthrough closed by marking the existing sections Deprioritized in-place. **Note:** This is a case where Pass 3 caught the failure mode rather than failing — included here for completeness because the architectural pattern is named in the SWEEP-ARCHITECTURE doc.

---

### 8. Under-deduping (Pass 3 doesn't catch Pass 2 emitting duplicate items)

**Pattern:** Pass 2's "bias toward inclusion" produces ~5-item-density duplicate clusters within a single sweep. Pass 3 reviews each item independently, doesn't compare items to each other, doesn't deduplicate. Walkthrough operator absorbs the duplicate density as a manual close-as-companion-item cost.

**Frequency:** Flagged as systemic in [2026-05-16-priority-action-1-execute-the-caco-2-butyrate-dose-response-arm-in-validation.md](../synthesis/done/2026-05-16-priority-action-1-execute-the-caco-2-butyrate-dose-response-arm-in-validation.md): "5-item duplicate density traced to Pass 2's deliberate 'bias toward inclusion' + Pass 3 under-deduping in practice. Flagged for end-of-session daemon-prompt-tightening pass." Multiple clusters across 2026-05-15, 2026-05-16, 2026-05-17 sweeps show 2–5 items framed as connection / open-question / experiment / priority-action versions of the same underlying thread.

---

## Per-walkthrough breakdown

| Walkthrough date | Items walked | Explicit Pass 3 critique annotations | New failure-mode patterns surfaced |
|---|---|---|---|
| 2026-05-14 | ~15 (Actioned 2026-05-14 marker) | 2 (named-in-prose ≠ comp-NNN-ID; novelty over operational) | Modes #4 (novelty under-weight); name-vs-queue conflation |
| 2026-05-15 | ~24 (Actioned 2026-05-15 marker, includes partial / drafted-only) | 2 (chassis-rubric static-rubric bias; rfdiffusion trigger-file gap) | Modes #5 (static-rubric); #6 (trigger-file awareness gap) |
| 2026-05-16 | ~14 (Actioned 2026-05-16 marker) | 2 (Pass 3 grep anchor-format mismatch on §1.25; stale-recommendation flag for §2.7 + §1.26) | Mode #5/6 variants; mode #7 (stale-recommendation, but Pass 3 caught it correctly here) |
| 2026-05-19 | 32 walked items in `synthesis/done/` from sweep 2026-05-16 + 38 from sweep 2026-05-17 (70 items) | 3 explicit (H2 circular, J3 under-claim, L2 scope-confirm) + 1 implicit (under-deduping flagged) | Modes #1 (circular dismissal); #2 (confirmation under-claim); #3 (scope-confirmation without platform-relevance) |

Aggregate: **~9 explicit Pass 3 critique annotations across 71 walkthrough-closed items, ~12.7% rate.** Lower bound only — annotations may not have captured every Pass 3 failure Brian caught silently during walkthroughs.

---

## Comparison: Pass 2 catches vs Pass 3 catches vs Brian catches

| Cluster | Pass 2 error | Pass 3 catch | Brian catch | Failure mode |
|---|---|---|---|---|
| 2026-05-19 H2 (cortisol × NLRP3 × MSU) | Speculative connection without explicit lit citation | — | Pass 3's circular dismissal logic | Mode #1 |
| 2026-05-19 J3 (substrate as engineering lever) | Documentation-discipline framing | — | Pass 3 confirmed 1× scope; missed 10× under-claim | Mode #2 |
| 2026-05-19 L2 (anakinra accessibility) | Three-part scope (insurance + prescriber + patient) | — | Pass 3 confirmed full scope; missed platform-irrelevance of insurance + prescriber | Mode #3 |
| 2026-05-19 cluster E (DAF analogy) | Surface-pattern-match without structural-functional check | DAF analogy correction held | Brian ratified Pass 3 + named broader Pass 2 pattern | Pass 3 worked correctly here |
| 2026-05-15 connection-4 (RFdiffusion + ProteinMPNN) | Citation to trigger-commit content | — | Pass 3 grep false-negative on new content | Mode #5 |
| 2026-05-15 contradiction-1 (chassis-pending rubric) | "Need static framework" recommendation | — | Pass 3 amplified Pass 2's static-rubric framing | Mode #6 |
| 2026-05-09 connection-1 + 2 (ClockBase + NRPS) | Novelty framing | Pass 3 noted prior-art correctly | But novelty wasn't the right criterion — Brian | Mode #4 |
| 2026-05-09 connection-4 (quantification ladder) | Novelty claim overstated | Pass 3 confirmed overstatement | But Pass 3 framed consolidation as nice-to-have; stale-divergence risk = load-bearing — Brian | Mode #4 |
| 2026-05-13 connection-3 (paperclip Km misreport) | Original paperclip-deep-dive entry off by 1 order | Pass 3 grep-verify caught it | — | Pass 3 worked correctly |
| 2026-05-15 priority-action-1 (§2.7 + §1.26) | "Add these sections" — already exist | Pass 3 flagged `[GAP: tool-gap]` (correct) | Brian closed as Deprioritized | Mode #7 (Pass 3 worked) |
| 2026-05-16 connection-1/2 (PDB-butyrate triple-mechanism) | Novelty claim false | Pass 3 pushed back correctly | — | Pass 3 worked correctly |
| 2026-05-16 contradiction-1 (§1.25 harmonization) | Item itself was factually wrong against current wiki | Pass 3 ALSO factually wrong via anchor-format mismatch | Brian verified directly | Mode #5 variant (Pass 3 grep brittleness) |

**Net pattern:** Pass 3 is reliably useful when (a) Pass 2 has emitted a verifiable factual claim ("X is novel," "Y is at concentration Z") and (b) the verification is a direct grep / number-check. Pass 3 is unreliable when (a) Pass 2's claim is about novelty in a "named in prose vs queued with ID" gradient, (b) Pass 2's recommendation is to *add* documentation / rubric / framework (Pass 3 inherits the additive bias), (c) the verification depends on context Pass 3 doesn't have (trigger-commit awareness, anchor-format conventions), or (d) the verification is about platform-relevance / first-principles framing rather than factual checking.

---

## Process improvement recommendations

### Pass 3 prompt updates (epistemic-gate failure modes)

These are the failure modes the human-walkthrough gate currently catches alone. Adding prompt-level checks could shift detection upstream.

1. **Circular-reasoning check.** Add to `scripts/sweep-prompt-3-review.md` and the GPT-5.5 variant: "If your verdict relies on 'no documented X exists' or 'the proposed mechanism is not in the literature,' check whether Pass 2's connection requires investigation BECAUSE it's not documented (curiosity rule, umbrella CLAUDE.md §'Curiosity and First-Principles Framing'). 'Not documented → don't investigate' is circular reasoning if the connection itself is the proposal to investigate. State explicitly whether the connection is (a) factually wrong against existing literature (legitimate push back) or (b) speculative and uninvestigated (legitimate as an open question or cheap experiment)." [Targets Mode #1.]

2. **Operational-improvement axis.** Already proposed by the 2026-05-14 walkthrough's "Second Pass 3 failure-pattern observation": add an operational-improvement axis to the verdict rubric. A recommendation can score "novelty: low / operational improvement: high" and still warrant prioritization (deduplication, stale-divergence prevention, single-source-of-truth consolidation). [Targets Mode #4.]

3. **First-principles upgrade check.** When confirming a Pass 2 recommendation framed as "documentation discipline," "QC anchor," "annotation column," prompt the reviewer to ask whether the underlying question is actually a first-principles engineering / mechanism question being miniaturized. The substrate-as-engineering-lever case is the canonical empirical example. [Targets Mode #2.]

4. **Scope platform-relevance audit.** When confirming the scope of an audit / experiment / open-question with multiple sub-questions, prompt the reviewer to evaluate each sub-question against platform relevance. "Cost of intervention" and "individual prescriber willingness" are typically operational-variability questions, not platform-research questions; "patient-reported clinical experience" is platform-research. [Targets Mode #3.]

### Daemon-architecture changes (structural failure modes)

5. **Trigger-file awareness fix.** Already queued in `scripts/SWEEP-ARCHITECTURE.md` §"Pass 3 trigger-file awareness gap" → orchestrator computes trigger-commit diff, injects as Pass 3 context. Ship the fix. [Targets Mode #5.]

6. **Anchor-format robustness.** Pass 3's grep should use anchor-flexible matching (try both `1.25` and `125`, try with/without periods). Could be a small prompt update or a grep-helper utility. [Targets Mode #5 variant.]

7. **Pass 2 deduplication pass.** Insert a Pass 2.5 or extend Pass 2's prompt with "before emitting, cluster items by underlying thread; collapse 2+ items framed as different surface forms of the same underlying connection into a single item with cross-surface annotations." Currently Pass 2's "bias toward inclusion" produces high duplicate density that Brian absorbs at walkthrough. [Targets Mode #8.]

### Honest assessment: is human-walkthrough gate acceptable, or warrant daemon changes?

**Acceptable today; not at scale.** The 2026-05-19 walkthrough surfaced 3 distinct Pass 3 epistemic-gate failure modes in 14 clusters (~21% miss rate on epistemic-gate questions). The aggregate 12.7% explicit-critique rate across 71 walked items is a lower bound — many critiques happen silently in walkthrough conversation without becoming closure annotations. The cost is currently absorbed by Brian's walkthrough discipline. Two scaling pressures will make this less tenable:

- **Item velocity:** as the corpus grows, sweeps emit more items per cycle; walkthrough load grows linearly.
- **Collaborator onboarding:** the three PhD-level collaborator roles being recruited (per `wiki/team.md`) will operate the walkthrough surface eventually. The Pass 3 epistemic-gate failure modes assume a specific operator (Brian) who already holds the curiosity rule, platform-relevance heuristics, and first-principles reframe instincts. Other operators won't catch the same patterns reliably without prompt-level codification.

**Recommended priority order:**
1. Ship the trigger-file awareness fix (already queued; mechanical engineering work).
2. Update Pass 3 prompts with the four epistemic-gate checks (1–4 above). Each is a one-paragraph addition; the empirical exemplars exist in closure annotations.
3. Add operational-improvement axis to the Pass 3 verdict rubric.
4. Pilot a Pass 2 deduplication pass; evaluate against duplicate-density telemetry from the 2026-05-19 walkthrough.
5. Consider a Pass 4 dedicated to Pass 3 critique (cross-vendor heterogeneity-guard logic extended one layer further). The DeepSeek peer-review pass already exists in spirit; making it explicitly target Pass 3's verdicts rather than only Pass 2's content would close the single-point-of-failure asymmetry on the Pass 3 side.

**A Pass 4 dedicated to Pass 3 review is the cleanest architectural answer to the asymmetry Brian named.** Currently the cross-vendor heterogeneity guard runs Pass 1 → Pass 2 → Pass 3 across DeepSeek / Gemini / GPT-5.5; an explicit Pass 4 (different vendor again, e.g., Claude Opus or DeepSeek-Pro independently) reviewing Pass 3's verdicts the way Pass 3 reviews Pass 2's content would mirror the existing pattern at the next layer. The cost is one additional OpenRouter call per item with critical Pass 3 verdicts. This is the most defensible structural fix; the prompt updates above are the cheap intermediate.

---

## Limitations

- **Sample is biased toward recent walkthroughs.** Closure annotation discipline matured between 2026-05-14 and 2026-05-19; earlier walks (pre-2026-05-09) may have absorbed Pass 3 failures silently without writing them up. The 142-item denominator is what's documented, not what happened.
- **Annotations are walkthrough-operator framing.** Brian writes the closure annotations. Pass 3 failure modes Brian DIDN'T notice are by definition absent from the corpus. The audit measures what was caught, not the underlying failure rate.
- **"Pass 3" routing has rotated across vendors and prompts.** GPT-5.5 vs DeepSeek vs Gemini Pass 3 implementations are not separately analyzed here. Some failure modes may be vendor-specific (e.g., anchor-format grep brittleness might be a model-specific artifact rather than a structural Pass 3 weakness). A vendor-stratified analysis would require correlating closure annotations to the model used per sweep cycle, which is recoverable from `logs/sweep-state.json` and sweep-log entries but was not included in this audit.
- **"Pass 3 caught Pass 2" vs "Pass 3 failure" gradient.** Several closure annotations note both: Pass 3 caught one error AND introduced another (e.g., 2026-05-16-contradiction-1 — Pass 3 grep was wrong but its underlying critique was directionally right). Counting these as "failures" or "successes" depends on framing. The 12.7% rate captures explicit critique annotations only.
- **Confirmation bias risk in typology construction.** The three 2026-05-19 walkthrough failure modes were used to construct the hypothesis taxonomy that was then tested against prior closures. The five additional modes found in the prior corpus were not predicted by the H2/J3/L2 typology; they emerged from the crawl. This is consistent with the audit being more discovery than confirmation, but a confirmatory pass with the eight-mode typology against new walkthroughs would strengthen the claim.
- **No counterfactual analysis.** "What would have happened if Pass 3 had emitted a different verdict?" is not tractable from the closure record. The H2 case is the closest counterfactual: lit scan fired AFTER Brian overruled, found mechanism Pass 3 said didn't exist. That's one data point in favor of "Pass 3 epistemic-gate failures have real downstream cost." Generalizing requires more such counterfactuals.

---

## Citation provenance

All Pass 3 failure-mode examples trace to specific closure annotations in `synthesis/done/`. Line numbers reference the file's current state on disk (2026-05-19).

| Failure mode | Source file | Key line(s) |
|---|---|---|
| Mode #1 — Circular dismissal | [2026-05-17-connection-7-bhb-s-cp1-cp3-coverage-the-cortisol-fasting-stress-axis-an.md](../synthesis/done/2026-05-17-connection-7-bhb-s-cp1-cp3-coverage-the-cortisol-fasting-stress-axis-an.md) | line 30 ("Pass 3 dismissed this connection with 'no documented gout-specific cortisol-rebound mechanism' — that's circular reasoning") |
| Mode #2 — Confirmation under-claim | [2026-05-17-connection-6-substrate-accumulated-plant-flavonoids-in-cultivated.md](../synthesis/done/2026-05-17-connection-6-substrate-accumulated-plant-flavonoids-in-cultivated.md) | line 25 ("flipped this from a documentation-QC problem to a first-principles question worth investigating") |
| Mode #3 — Scope-confirmation | [2026-05-17-open-question-2-what-is-the-real-world-accessibility-of-off-label-anakinra.md](../synthesis/done/2026-05-17-open-question-2-what-is-the-real-world-accessibility-of-off-label-anakinra.md) | line 26 ("Pass 3 confirmed the original audit's full scope... without pushing back on the platform-irrelevance of the insurance + prescriber-willingness questions") |
| Mode #4 — Novelty-over-operational under-weight | [2026-05-09-connection-4-the-tiered-quantification-ladder-kitchen-smartphone-bench.md](../synthesis/done/2026-05-09-connection-4-the-tiered-quantification-ladder-kitchen-smartphone-bench.md) | lines 25, 35 ("Pass 3 over-weights 'is this novel?' and under-weights 'does this make the corpus better operationally?'") |
| Mode #4 (related) — named-in-prose vs comp-NNN | [2026-05-09-connection-1-clockbase-autonomous-screening-methodology-maps-directly.md](../synthesis/done/2026-05-09-connection-1-clockbase-autonomous-screening-methodology-maps-directly.md), [2026-05-09-connection-2-bacterial-nrps-anticomplement-peptides-complestatin-class.md](../synthesis/done/2026-05-09-connection-2-bacterial-nrps-anticomplement-peptides-complestatin-class.md) | conflation flag in both closure annotations |
| Mode #5 — Trigger-file awareness gap | [2026-05-15-connection-4-the-rfdiffusion-proteinmpnn-tool-gap-closed-by.md](../synthesis/done/2026-05-15-connection-4-the-rfdiffusion-proteinmpnn-tool-gap-closed-by.md) | line 28 ("Pass 3's grep returned a false-negative because Pass 3 has no trigger-file awareness") |
| Mode #5 variant — Anchor-format mismatch | [2026-05-16-contradiction-1-the-chaperone-orthogonal-stacking-framework-s-coefficient.md](../synthesis/done/2026-05-16-contradiction-1-the-chaperone-orthogonal-stacking-framework-s-coefficient.md), [2026-05-16-open-question-1-can-the-chaperone-orthogonal-stacking-framework-s.md](../synthesis/done/2026-05-16-open-question-1-can-the-chaperone-orthogonal-stacking-framework-s.md) | "Pass 3's grep was anchor-format mismatch (file uses `#125-…` anchor without period; literal `1.25` grep with period missed the section header)" |
| Mode #6 — Static-rubric bias | [2026-05-15-contradiction-1-the-chassis-pending-intervention-list-risks-diluting-the.md](../synthesis/done/2026-05-15-contradiction-1-the-chassis-pending-intervention-list-risks-diluting-the.md) | lines 24–28 ("Both Pass 2 (synthesizer) and Pass 3 (reviewer) fell into a 'name a rule and document it' frame") |
| Mode #7 — Stale-recommendation (Pass 3 caught) | [2026-05-15-priority-action-1-add-validation-experiments-md-2-7-koji-cordyceps-co.md](../synthesis/done/2026-05-15-priority-action-1-add-validation-experiments-md-2-7-koji-cordyceps-co.md) | "Pass 3 was right that §2.7 and §1.26 sixth-arm were already in validation-experiments.md" |
| Mode #8 — Under-deduping | [2026-05-16-priority-action-1-execute-the-caco-2-butyrate-dose-response-arm-in-validation.md](../synthesis/done/2026-05-16-priority-action-1-execute-the-caco-2-butyrate-dose-response-arm-in-validation.md) | "5-item duplicate density traced to Pass 2's deliberate 'bias toward inclusion' + Pass 3 under-deduping in practice" |
| Architecture context — broader Pass 2 / Pass 3 bias | [scripts/SWEEP-ARCHITECTURE.md](../scripts/SWEEP-ARCHITECTURE.md) | §"Recommend creating what already exists" (lines 420–462), §"Pass 3 trigger-file awareness gap" (lines 468–486), §"Tool-gap / science-gap pilot" (lines 365–418) |
| Single-point-of-failure framing | [2026-05-16-connection-4-the-lactoferrin-inter-lobe-linker-redesign-comp-034-and-the.md](../synthesis/done/2026-05-16-connection-4-the-lactoferrin-inter-lobe-linker-redesign-comp-034-and-the.md) | "The Pass 2 failure modes are caught by Pass 3 + Brian; the Pass 3 failure modes are caught only by Brian — that single-point-of-failure asymmetry is the systemic gap the retrospective will quantify" |
