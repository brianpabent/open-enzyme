---
id: H08
title: "The gut-lumen uricase sink produces a clinically meaningful serum urate reduction in a typical (non-CKD) gout cohort, with effect size in the −0.5 to −1.0 mg/dL band predicted by the comp-019 flux model"
committed: 2026-05-15
status: Stub
survival_count: 0
tags:
  - hypothesis
  - core-thesis
  - gut-lumen-sink
  - uricase
  - abcg2
  - clinical-translation
  - riskiest-assumption
related:
  - ../gut-lumen-sink.md
  - ../uricase.md
  - ../cross-validation.md
  - ../uricase-abcg2-genotype-stratification-computational.md
  - ../open-enzyme-vision.md
  - ../validation-experiments.md
  - ../open-questions.md
  - ./H01-ward-dual-cassette.md
  - ./README.md
sources:
  - "ALLN-346 Phase 2a Studies 201 (CKD signal) + 202 (broader cohort null) — terminated program, 19/200 enrolled in 202"
  - "Miyazaki 2025 (PMID 40033341) — first direct human in-vivo measurement of jejunal urate secretion stratified by ABCG2 functional class"
  - "comp-019 flux model — uricase-abcg2-genotype-stratification-computational.md (2026-05-08)"
  - "Rasburicase (FDA 2001) — IV uricase clinical use; benchmark for in-vivo uricase activity at biologically relevant scale"
  - "PRX-115 (Protalix, Phase 1, 2024 ACR) — PEGylated uricase Phase 1 update"
  - "PULSE probiotic (Cell Reports Medicine, Oct 2025) — humanized-microbiome model of barrier repair + uricase signal"
---

# H08 — Gut-Lumen Sink Platform Thesis (Stub)

> **Stub status.** Committed at stub-level on 2026-05-15 to register the platform's load-bearing scientific claim in the falsification-card directory and force the "what would kill this thesis" framing onto the canonical [gut-lumen-sink.md](../gut-lumen-sink.md) and [cross-validation.md](../cross-validation.md) Claim 1. Full population (assumption stack, killshot menu, pre-committed thresholds, kill switches, failure-mode coverage map) is queued as Phase 2 — see "Open Follow-Ups" at the bottom of this file.
>
> Identified as the platform's **#1 riskiest assumption** in the 2026-05-09 sweep (synthesis/done/2026-05-09-riskiest-assumption-1) with Pass 3 verdict "Confirmed, prioritize." The pre-registration note on H01 ([H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) §Pre-registration) does not apply until this stub is upgraded to a full card. When the upgrade happens, the upgraded version is what gets pre-registered; the stub is informational scaffolding only.

---

## Claim (provisional, stub-level)

Placing active uricase in the intestinal lumen of typical (non-CKD) gout patients produces a sustained serum urate reduction of **−0.5 to −1.0 mg/dL** at the comp-019 mid-dose (25 mg/day delivered functional uricase), with magnitudes stratified by ABCG2 genotype as predicted by the flux model:

| Scenario | comp-019 Predicted ΔSUA at 25 mg/day (Monte Carlo median, 90% CI) |
|---|---|
| WT/WT, male gout | **−0.83 mg/dL (−1.13 to −0.57)** |
| Q141K heterozygous, male gout | −0.67 mg/dL (−0.91 to −0.45) |
| Q141K homozygous, male gout | −0.50 mg/dL (−0.68 to −0.34) |
| Severe ABCG2 dysfunction (Q126*+Q141K compound) | −0.28 mg/dL (−0.39 to −0.20) |

The claim has multiple sub-components that the full card will decompose:

1. The in-silico flux model magnitudes translate from Monte Carlo prediction to human RCT outcomes within a band that distinguishes clinical efficacy from placebo (mean ΔSUA ≥ 0.5 mg/dL with p<0.05 in a powered RCT).
2. ABCG2-mediated intestinal urate secretion is rate-limiting enough in non-CKD patients that adding luminal uricase materially changes the serum-urate equilibrium (vs. renal compensation fully offsetting the gut delta).
3. ALLN-346 Study 202's null result in the broader cohort reflects fixable formulation / dose / cohort-selection problems, not a fundamental ceiling on the gut-lumen sink mechanism in typical gout.
4. The OE engineered strain achieves GI-survival sufficient to deliver therapeutic luminal uricase to the secretion-rich ileum/colon at therapeutic densities (Claim 2 binding constraint at 5/10 in `cross-validation.md`).
5. The mechanism is genotype-robust per comp-019 — non-Q141K patients show the largest per-patient response, not the smallest — so the platform demographic does not narrow to Q141K carriers.

---

## Why this is the riskiest assumption

The biological logic is sound: ABCG2 secretes ~33% of daily urate elimination into the gut lumen, and a luminal uricase sink amplifies whatever ABCG2 delivers. comp-019's flux model is internally consistent (substrate-limited regime at all dose scenarios tested, capacity ratios 32–1300×, anchored against Miyazaki 2025's direct human in-vivo jejunal urate secretion measurements).

But the **clinical-translation link** — from modelled intestinal urate flux to a measured, patient-meaningful SUA change in typical gout — is entirely unvalidated in vivo:

- **ALLN-346 Phase 2a Study 201** showed signal in CKD patients.
- **ALLN-346 Phase 2a Study 202** (broader cohort, ~typical gout) showed **0–5% SUA reduction, no significance vs. placebo**, and the program terminated with 19/200 patients enrolled.
- **Zero** uricase trials (oral or systemic — ALLN-346, PRX-115, rasburicase, pegloticase) have stratified results by ABCG2 Q141K genotype. The Q141K × allopurinol response literature is rich; the Q141K × uricase response literature is empty.
- The comp-019 flux model is prospective and unvalidated.

The cross-validation feasibility rating is **6.5/10** ([cross-validation.md §Claim 1](../cross-validation.md)): mechanism validated preclinical, clinical signal exists but is marginal and inconsistent, the 3.5 remaining points await Phase 2b RCT validation. If the real-world typical-gout effect is <0.5 mg/dL, the platform's urate-lowering value proposition collapses from "core mechanism" to "mild adjunct" — reshaping the commercial framing, the self-experiment framing, and the priority of downstream peer tracks ([LBP chassis](../engineered-lbp-chassis.md), [siRNA / URAT1](../sirna-urat1-modality.md), [medicinal-mushroom complement track](../medicinal-mushroom-complement-track.md), [compounding pharmacy delivery](../compounding-pharmacy-track.md) where it exists).

---

## Assumption Stack (placeholder — to be populated in Phase 2)

Anticipated load-bearing assumptions, to be confirmed and weighted in the full card:

1. comp-019's Monte Carlo flux model predicts human RCT outcomes within a band of ±0.3 mg/dL of the mean (i.e., the modelled −0.83 mg/dL WT/WT prediction translates to a measured −0.5 to −1.1 mg/dL human RCT mean).
2. Renal compensation in patients with normal eGFR does not fully offset the gut delta. comp-019's renal-compensation parameter sensitivity spans 0–50%; this card commits the assumption that ≤30% offset preserves clinical efficacy.
3. ALLN-346 Study 202's null result is explained by either (a) insufficient effective dose at the secretion-rich ileum/colon, (b) insufficient cohort enrichment for likely responders, or (c) insufficient duration to reach steady-state — NOT by a fundamental mechanism failure.
4. Comparator candidates currently in clinical development (PRX-115, any post-ALLN-346 oral-uricase program) do not preempt or invalidate the OE-specific delivery thesis.
5. The OE strain achieves >10⁸ functional uricase units delivered post-stomach to the ileum/colon at a per-dose cost compatible with typical-gout commercial pricing (or, for the open-source/self-experiment surface, compatible with the koji-strain-library distribution model).
6. Q141K trafficking rescue by ABCG2 modulators (butyrate via HDAC, see [abcg2-modulators.md](../abcg2-modulators.md)) does not invalidate the H08 mechanism — it complements it.

---

## Killshot Menu (placeholder — to be populated in Phase 2)

The full menu will follow H01's `score = (kill_pr × info_weight) / (cost × time_penalty)` ranking, with each killshot tagged to specific assumptions and failure modes per [linter-design.md](../linter-design.md) §4–5.

Anticipated highest-priority killshots, ranked roughly by leverage:

- **Lit scan: post-ALLN-346 oral-uricase Phase 2 typical-gout efficacy.** Has any program reported a typical-gout Phase 2 readout since ALLN-346 termination? If yes, that's a strong external prior on H08. Cheapest possible upstream move.
- **Re-analysis of ALLN-346 Study 202 publicly available cohort-level data.** No published uricase trial has stratified by ABCG2 Q141K. A retrospective genotype-stratified re-analysis of Study 202 (if obtainable via FOIA / sponsor request / published supplementary data) would be a low-cost, high-info killshot — does the WT/WT subset show the largest effect, as comp-019 predicts? If the genotype-stratified pattern matches comp-019, H08 strengthens dramatically; if it doesn't, H08's flux-model translation is wrong.
- **n=1 self-experiment.** See [`self-experiment-protocol.md`](../self-experiment-protocol.md) and the FEUA protocol in [`memory/project_feua_at_ua_retest.md`](../../../memory/project_feua_at_ua_retest.md). Brian's own serum UA + spot urinary FEUA at baseline / mid / post a koji-engineered uricase strain delivery, decomposing renal (URAT1) vs. intestinal (ABCG2) compartments. Tier 4 in the validation-experiments hierarchy; gives directional signal without a Phase 2b cohort.
- **Recombinant rasburicase oral-delivery N=1 pilot.** Lower-cost upstream test — does any oral-delivered uricase produce the predicted SUA drop in a typical-gout subject? Decouples the OE strain delivery question from the mechanism question. If the mechanism fails with an off-the-shelf enzyme, H08 dies before strain engineering matters.
- **Phase 2b RCT, typical-gout cohort with Q141K + Q126* stratification.** The gold standard. comp-019's RCT design recommendation: typical-gout cohort, 25 mg/day, stratification not enrichment, single-dose, pre-stratify by CKD stage. Definitive killshot; highest cost.
- **In vivo ileal/colonic urate concentration measurement post-OE-strain delivery (humanized microbiome model or human pilot).** Tests whether the strain actually delivers functional uricase to the secretion-rich segment. If luminal urate doesn't drop measurably, the platform thesis fails upstream of SUA outcomes.
- **Renal compensation magnitude measurement** in a human pilot. If renal reabsorption compensates ≥50% of the gut delta, comp-019's prediction band is wrong on the high side — H08 needs to retract to a smaller predicted ΔSUA, possibly below the 0.5 mg/dL clinical threshold.

---

## Pre-Committed Thresholds (placeholder — to be populated in Phase 2)

To be defined when the killshot menu is populated. Anticipated structure follows H01: declared Alive / Killed / Pending thresholds for each load-bearing claim, plus kill switches independent of the scientific thresholds.

Provisional anchor (to be confirmed in full card):

- **Alive:** any future Phase 2b-class data showing mean ΔSUA ≤ −0.5 mg/dL in typical (non-CKD) gout with p < 0.05.
- **Killed:** any Phase 2b-class data showing mean ΔSUA > −0.3 mg/dL in typical gout with adequate dose and adherence (i.e., the predicted band of −0.5 to −1.0 is materially missed on the high side, not on the noise side).
- **Pending:** anything in between, including n=1 self-experiment signal that is directionally positive but not powered.

---

## Failure Modes Probed (placeholder — to be populated in Phase 2)

To be populated. Anticipated relevant failure modes from [linter-design.md](../linter-design.md) §5:

- **species-gap-translation** (mouse ABCG2 vs. human; mouse intestinal anatomy vs. human ileal-colonic axis)
- **dose-translation scaling** (predicted 25 mg/day functional uricase vs. delivered active enzyme at the secretion segment)
- **published-literature-gap** (zero Q141K-stratified uricase trials in the entire clinical corpus)
- **renal-compensation offset** (model assumes ≤30%; could be higher in practice)
- **formulation gap** (ALLN-346's formulation choices may have under-delivered active enzyme to the secretion segment)
- **trial-design selection** (Study 202's broader cohort may have included responders the design failed to detect)

---

## Status

**Stub.** No killshot executed. No assumption stack pre-registered. Full hypothesis card is queued as Phase 2 — see "Open Follow-Ups" below.

**Survival count:** 0.

**Survival score:** 0.0 (undefined until full card and first survived killshot).

---

## Open Follow-Ups (Phase 2)

| ID | Item | Type | Status |
|---|---|---|---|
| P2-1 | Lit scan: any post-ALLN-346 (2024+) oral or gut-targeted uricase Phase 2 typical-gout readout | Opus subagent literature scan | Queued |
| P2-2 | Re-analysis attempt: ALLN-346 Study 202 cohort-level genotype data accessibility (FOIA / sponsor request / supplementary data grep) | Foreground subagent + procedural | Queued |
| P2-3 | Populate full assumption stack, weights, and confidence tiers per H01 template | Inline upgrade | Queued |
| P2-4 | Populate full killshot menu with score-ranking per linter-design.md §4–5 | Inline upgrade | Queued |
| P2-5 | Populate pre-committed thresholds + kill switches | Inline upgrade (requires P2-1, P2-2 results to anchor magnitudes) | Queued |
| P2-6 | Failure-mode coverage map (lint cross-check against linter-design.md §5) | Inline upgrade | Queued |
| P2-7 | n=1 self-experiment design integration with FEUA protocol per `memory/project_feua_at_ua_retest.md` | Cross-link to `self-experiment-protocol.md` | Queued |

Tracked across the 6 follow-up surfaces per the walk-synthesis skill §5:
1. This page's "Open Follow-Ups" section (above)
2. [`open-questions.md`](../open-questions.md) — to be added in same commit
3. [`computational-experiments.md`](../computational-experiments.md) — Planned Analyses table addition (cross-link to ALLN-346 Study 202 re-analysis attempt)
4. This H08 falsification card stub (current)
5. [`index.md`](../../index.md) — one-line surfacing of H08 as the platform's riskiest-assumption anchor
6. `synthesis/done/2026-05-09-riskiest-assumption-1*.md` — closure annotation

---

## Cross-References

- [gut-lumen-sink.md](../gut-lumen-sink.md) — the platform thesis this hypothesis formalizes
- [uricase.md](../uricase.md) — enzyme-level page; carries the same mechanistic claim
- [cross-validation.md](../cross-validation.md) §Claim 1 — feasibility rating 6.5/10 and the explicit "core scientific bet" framing
- [uricase-abcg2-genotype-stratification-computational.md](../uricase-abcg2-genotype-stratification-computational.md) — comp-019, the flux model anchoring the magnitude predictions
- [open-enzyme-vision.md](../open-enzyme-vision.md) — platform-level framing
- [validation-experiments.md](../validation-experiments.md) — wet-lab and self-experiment dependencies
- [self-experiment-protocol.md](../self-experiment-protocol.md) — n=1 framework
- [open-questions.md](../open-questions.md) — meta-index entry for the residual open questions on this thesis
- [linter-design.md](../linter-design.md) — schema for the Falsification Card format
- [H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) — sibling falsification card (Ward dual-cassette architecture); format template
- [H02-engineered-lbp-thesis.md](./H02-engineered-lbp-thesis.md) — peer-track LBP hypothesis (depends on a non-koji ABCG2-induction mechanism, partially independent of H08)
- [H03-sirna-urat1-thesis.md](./H03-sirna-urat1-thesis.md) — peer-track URAT1 hypothesis (renal-axis bypass, fully independent of H08)
