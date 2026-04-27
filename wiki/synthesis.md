---
title: "Synthesis — Action Queue"
date: 2026-04-27
tags: ["synthesis", "action-queue", "cross-domain"]
related: ["validation-experiments.md", "open-questions.md", "logs/sweep-log.md"]
sources: ["sweep daemon (wiki/*.md saves)", "manual sweeps", "V4 peer-review pass"]
---

# Synthesis — Action Queue

## How to read this file

This is the **action queue** for the sweep daemon and manual synthesis passes. Entries appear when a sweep surfaces a new connection, contradiction, or experiment; entries leave when the work lands in the canonical wiki page (or is folded into [`validation-experiments.md`](./validation-experiments.md) / [`open-questions.md`](./open-questions.md)).

**The full audit trail of every sweep — including findings that have already landed — lives in [`logs/v4-synthesis-*.md`](../logs/) and [`logs/v4-peer-review-*.md`](../logs/).** Don't re-state finished work here; if you want the history, go to the log.

A 2026-04-27 inbox-zero pass pruned everything marked `✓ Actioned` out of this file. The residue below is the genuine open queue. Sweep-history table at the bottom records date / trigger / log link only.

---

## Pending — open items

Eight items survived the inbox-zero pass. Each is a finding that surfaced in a sweep but does not yet have a canonical home in a wiki page. Walk through with Brian.

1. **PNLIP (human pancreatic lipase) cross-species engineering — desk review.**
    - **Where it surfaced:** Sweep 2026-04-25 (`622d2e2`) Connection 2.
    - **What's missing:** No wiki page discusses heterologous human PNLIP in *A. oryzae*. [`digestive-enzyme-optimization.md`](./digestive-enzyme-optimization.md) covers native *tglA* overexpression and *Rhizopus*/*Candida* heterologous lipases, but not human PNLIP + procolipase. [`gi-survival-prediction.md`](./gi-survival-prediction.md) only mentions PNLIP in passing.
    - **Action:** $0 / 1-week desk review. Must answer (a) glycosylation compatibility (filamentous-fungus vs. mammalian pancreas), (b) procolipase co-expression requirement, (c) prior titers in any filamentous fungus, (d) acid/bile stability advantage over fungal lipases (the binding constraint per `gi-survival-prediction.md` §9 — pancreatic lipase GI survival is ~1%), (e) IP landscape (Abbott/Creon).
    - **Decision gate:** if the desk review surfaces a viable expression path AND a stability advantage, add a Year-2-3 module to [`digestive-enzyme-optimization.md`](./digestive-enzyme-optimization.md) and [`engineered-koji-protocol.md`](./engineered-koji-protocol.md). Otherwise close the question.

2. **Tane-koji ↔ master-seed terminology mapping in `open-source-platform.md`.**
    - **Where it surfaced:** Sweep 2026-04-25 (`622d2e2`) Connection 3.
    - **What's missing:** [`open-source-platform.md` §"Proposed Strain Stability Kit"](./open-source-platform.md) exists and describes the master-stock / working-batch model in general organism terms, but does not explicitly map onto the koji tradition's tane-koji → koji rice framework. The cultural framing was the whole pedagogical point.
    - **Action:** Add a short subsection to [`open-source-platform.md`](./open-source-platform.md) §3 framing tane-koji as the lyophilized master stock and koji rice as the single working batch. Cross-link from [`koji-home-fermentation.md` §"Project Relevance"](./koji-home-fermentation.md).
    - **Effort:** 30 minutes of writing.

3. **Androgen-urate "structural ceiling" (not dose variable) reframe in `cross-validation.md` and `koji-endgame-strain.md`.**
    - **Where it surfaced:** Sweep 2026-04-25 (`622d2e2`) Connection 4 + V4 peer-review 2026-04-25.
    - **What's missing:** [`androgen-urate-axis.md`](./androgen-urate-axis.md) frames androgen suppression of ABCG2 as a "dose-sizing consideration." V4-Pro pushed back: it's a **structural ceiling on platform feasibility for the primary demographic** (male gout patients on TRT). Per Claude review: "regardless of dose" overstates — the asymptote is lowered, not eliminated — but the reframing is substantively correct and cascades into stratification logic.
    - **Action:** (a) Update [`cross-validation.md`](./cross-validation.md) gut-lumen-sink section to account for sex-specific transporter biology as a ceiling. (b) Flag in [`koji-endgame-strain.md`](./koji-endgame-strain.md) coverage matrix as a structural ceiling, not a dose variable. (c) Optionally cross-reference in [`androgen-urate-axis.md`](./androgen-urate-axis.md).
    - **Effort:** 1–2 hours.

4. **Chokepoint-biomarker map in `self-experiment-protocol.md`.**
    - **Where it surfaced:** Sweep 2026-04-24 (25-file v1.2 batch) Connection 3 + Proposed Experiment 4.
    - **What's missing:** Not in any wiki page. The biomarker panel exists in [`self-experiment-protocol.md`](./self-experiment-protocol.md) but the explicit chokepoint→biomarker mapping is implicit across three trigger pages (`zileuton.md`, `spm-resolution-pathway.md`, `complement-c5a-gout.md`). Brian's n=1 protocol can't tell which chokepoint the stack is hitting without this mapping.
    - **Action:** Add a chokepoint-biomarker table to [`self-experiment-protocol.md`](./self-experiment-protocol.md): one row per biomarker (serum C5a, urinary LTE4, plasma SPMs, hs-CRP), one column per chokepoint it reads out (CP0, CP6a, CP5b, overall), one "interpretation in context of stack" column. Plus a red-flag decision rule: "C5a elevated + LTE4 normal + CRP elevated → CP0 bottleneck → avacopan conversation."
    - **Effort:** 1 hour.

5. **Lactoferrin + EGCG CP1a super-additivity assay.**
    - **Where it surfaced:** Sweep 2026-04-24 Connection 4 + Proposed Experiment 2.
    - **What's missing:** Not yet in [`validation-experiments.md`](./validation-experiments.md). Two CP1a mechanisms hit the NF-κB cascade from opposite sides — lactoferrin sequesters LPS upstream of TLR4; EGCG inhibits 20S proteasome (86 nM) downstream of NF-κB activation, stabilizing IκBα regardless of upstream signal. Combination should be super-additive on paper.
    - **Action:** Add to [`validation-experiments.md`](./validation-experiments.md) as a §1.x entry. THP-1 macrophage 2×3 dose matrix (lactoferrin 0/low/high × EGCG 0/low/high) + LPS+MSU stimulation, IL-1β ELISA, Loewe combination index. ~$1,500 / 3–4 weeks. Decides whether to dose them together at lower individual doses (relevant for keeping EGCG below the ~600 mg/day hepatotoxicity ceiling).
    - **Effort:** 30 minutes to write up the experiment entry.

6. **Natural-product C5aR1 screening — computational pass.**
    - **Where it surfaced:** Sweep 2026-04-24 Connection 2 + Proposed Experiment 3.
    - **What's missing:** Not yet in [`validation-experiments.md`](./validation-experiments.md). The Open Enzyme stack has zero fermentable C5a / C5aR1 coverage at CP0 — avacopan (FDA-approved 2021) is the pharma adjunct, but a computational scan for natural-product C5aR1 binders is $0 and would either surface a candidate or cleanly lock in the "CP0 requires pharma adjunct" conclusion.
    - **Action:** Add to [`validation-experiments.md`](./validation-experiments.md) as a §1.x entry. ChEMBL + Open Targets queries for known C5aR1 ligands; cross-reference with plant-natural-product database; top 5–10 hits run through AlphaFold + AutoDock Vina against C5aR1 allosteric-site coordinates. $0 / 1–2 days. Output: shortlist for wet-lab follow-up OR clean null.
    - **Effort:** 30 minutes to write up; the actual scan can be queued after.

7. **AggNET / citH3 / cfDNA biomarker add-on for the self-experiment.**
    - **Where it surfaced:** Sweep 2026-04-24 Connection 7 + Proposed Experiment 6.
    - **What's missing:** Not in [`self-experiment-protocol.md`](./self-experiment-protocol.md) or [`validation-experiments.md`](./validation-experiments.md). The v1.2 exploit map describes aggNETs as resolution objects (sequester cytokines) vs. free NETs as inflammation amplifiers. Plasma citH3 reads free-NET load; cfDNA reads total NET load; the ratio is a resolution-competence readout the protocol currently lacks. Note V4-Pro pushback: "impractical for n=1" — the assays are specialty-lab, $200–400/panel.
    - **Action:** Decision gate: is the per-panel cost justified by the resolution-competence signal? If yes, add to the self-experiment protocol as a tertiary biomarker add-on (only in active-flare or post-flare phases). If no, close the question and document why.
    - **Effort:** 30-minute discussion to triage in or out.

8. **Epistemic homogenization warning — explicit citation in process docs.**
    - **Where it surfaced:** V4 peer-review 2026-04-25 Connection 7.
    - **What's missing:** V4-Pro warned: "if a single model becomes the sole source of synthesis, the project's knowledge graph could converge on that model's blind spots and biases." The project already runs multi-model peer review (Sonnet propagate → Gemini synthesize → Opus critique → V4 peer review on top), but the *rationale* for keeping it multi-model is implicit. Worth surfacing in [`open-source-platform.md`](./open-source-platform.md) or in the sweep-prompt scripts as the standing methodological reason.
    - **Action:** Add a one-paragraph note in [`open-source-platform.md`](./open-source-platform.md) (or a sweep-prompt comment) citing the V4 peer-review log entry as the precedent.
    - **Effort:** 15 minutes.

---

## Sweep history

Audit trail. Date / trigger / synthesizer / reviewer / log link. **Findings landed in canonical wiki pages and were pruned from this file** during the 2026-04-27 inbox-zero pass.

| Date | Trigger | Synthesizer | Reviewer | Log |
|---|---|---|---|---|
| 2026-04-27 | `wiki/open-enzyme-vision.md` | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-27-b7df491.md`](../logs/v4-synthesis-2026-04-27-b7df491.md) |
| 2026-04-27 | aspergillus-oryzae + colchicine + cross-validation + 6 others | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-27-c602f32.md`](../logs/v4-synthesis-2026-04-27-c602f32.md) — duplicate finding (ergothioneine→ABCG2), collapsed into the b7df491 sweep |
| 2026-04-26 | `wiki/supplements-stack.md` | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-26-1aea93d.md`](../logs/v4-synthesis-2026-04-26-1aea93d.md) |
| 2026-04-26 | GRAPH + abcg2-modulators + androgen-urate-axis + gut-lumen-sink | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-26-1237ff0.md`](../logs/v4-synthesis-2026-04-26-1237ff0.md) |
| 2026-04-25 | `wiki/digestive-enzyme-optimization.md` | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-25-622d2e2.md`](../logs/v4-synthesis-2026-04-25-622d2e2.md) |
| 2026-04-25 | `wiki/koji-home-fermentation.md` | DeepSeek V4-Pro | Sonnet 4.6 | [`v4-synthesis-2026-04-25-a280c0d.md`](../logs/v4-synthesis-2026-04-25-a280c0d.md) — substantive duplicate of the 622d2e2 sweep, collapsed |
| 2026-04-25 | V4 peer-review pass on the 2026-04-24 sweep (`4a40f74`) | DeepSeek V4-Pro | (peer-review of Opus 4.7) | [`v4-peer-review-2026-04-25.md`](../logs/v4-peer-review-2026-04-25.md) |
| 2026-04-24 | 25-file v1.2 batch (nlrp3-exploit-map restructure + 24 co-triggered) | (manual session) | Opus 4.7 | (in-session log; see commit `4a40f74` and surrounding) |
| 2026-04-23 | `wiki/nlrp3-inhibitor-screen.md` (ChEMBL appendix) | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-23 | `wiki/gout-clinical-pipeline.md` | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-23 | `wiki/cannabinoids-terpenes.md` | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-21 (origin) | All 8 April 2026 AI analyses (initial Pass 2 brainstorm) | (manual) | (manual) | This file's original content; everything from that brainstorm has either landed in canonical wiki pages (carnosine module, koji-endgame-strain, validation-experiments §1.x) or surfaced again in later sweeps. |

---

## Where actioned items live now

The 2026-04-27 inbox-zero pass pruned ~700 lines of `✓ Actioned` content. The findings are not lost — they're in their canonical homes:

- **Experiment proposals** → [`validation-experiments.md`](./validation-experiments.md) §1.1–§1.19, §2.x, §3.x.
- **Open questions** → [`open-questions.md`](./open-questions.md), organized by topic.
- **Connection findings** → in the relevant per-compound or per-mechanism wiki page (e.g. ergothioneine → ABCG2 lives in [`abcg2-modulators.md`](./abcg2-modulators.md), shio-koji format constraints in [`engineered-koji-protocol.md` §15](./engineered-koji-protocol.md), Q141K population caveat in `abcg2-modulators.md`, etc.).
- **Coverage-matrix and chokepoint findings** → [`nlrp3-exploit-map.md`](./nlrp3-exploit-map.md), [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`open-enzyme-vision.md`](./open-enzyme-vision.md).
- **Methodology standards** (rodent IC50 caveat, two-tier NLRP3 labeling, etc.) → [`validation-experiments.md` §1.19](./validation-experiments.md), [`nlrp3-inhibitor-screen.md`](./nlrp3-inhibitor-screen.md), [`chembl-cross-check.md`](./chembl-cross-check.md).
- **ChEMBL refresh automation** → [`.github/workflows/chembl-refresh.yml`](../.github/workflows/chembl-refresh.yml), runs quarterly (Jan/Apr/Jul/Oct 1st at 12:00 UTC).
- **Cross-doc audit history** → `git log -p wiki/synthesis.md` shows the prior un-pruned state of each sweep block; `logs/v4-synthesis-*.md` shows the original synthesizer outputs.
