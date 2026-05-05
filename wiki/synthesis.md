---
title: "Synthesis — Action Queue"
date: 2026-05-05
tags: ["synthesis", "action-queue", "cross-domain"]
related: ["validation-experiments.md", "open-questions.md", "logs/sweep-log.md"]
sources: ["sweep daemon (wiki/*.md saves)", "manual sweeps", "V4 peer-review pass"]
---

# Synthesis — Action Queue

## How to read this file

This is the **action queue** for the sweep daemon and manual synthesis passes. Entries appear when a sweep surfaces a new connection, contradiction, or experiment; entries leave when the work lands in the canonical wiki page (or is folded into [`validation-experiments.md`](./validation-experiments.md) / [`open-questions.md`](./open-questions.md)).

**The full audit trail of every sweep — including findings that have already landed — lives in [`logs/v4-synthesis-*.md`](../logs/) and [`logs/v4-peer-review-*.md`](../logs/).** Don't re-state finished work here; if you want the history, go to the log.

Inbox-zero passes (2026-04-27, 2026-05-05) prune everything marked `✓ Actioned` out of this file. The residue below is the genuine open queue. Sweep-history table at the bottom records date / trigger / log link only.

---

## Pending — open items

**(none — inbox zero as of 2026-05-05).**

The 2026-05-05 walk-through actioned all 14 items from the 2026-05-05 sweep (which substantively duplicated the unprocessed 2026-04-28 sweep — same Connections / Contradictions / Open Questions / Priority Actions). The work landed in the canonical wiki pages listed in [Where actioned items live now](#where-actioned-items-live-now) below. New entries will appear here when the next sweep daemon run surfaces a finding the canonical pages don't already cover.

For the audit trail of the 2026-05-05 walk-through specifically, see `git log --since=2026-05-05` on this repo — the items landed across a series of commits (commits `7ee8f93` through `36a605b` covering comp-005, comp-006, comp-007, the engineered-LBP scope page, the siRNA / URAT1 scope page, the androgen×NLRP3 lit scan, the §1.23 androgen×MSU tiered protocol, and the cross-link / tracking infrastructure across all of the above).

---

## Strategic Reflections Queue

Content-triggered (not calendar-triggered) reflections that need to fire when accumulated substance crosses a maturity threshold. Distinct from the action queue above — these are platform-level reframes, not unit-of-work tasks. The daemon surfaces them on each sweep so they don't get lost.

| Reflection | Trigger | Outcome |
|---|---|---|
| **Open Enzyme platform-framing reframe** — does the broader matrix-tracks portfolio justify expanding the project framing from "engineered enzymes in koji" to "solve gout, every avenue, fully open"? Two scope-pages now exist as concrete instances: [LBP chassis](./engineered-lbp-chassis.md) (peer-track strain-library; commercial-pharma sub-track) and [siRNA / URAT1 modality](./sirna-urat1-modality.md) (discovery-engine output; non-microbial). Other matrix tracks (Q141K pharmacological chaperones, mRNA-IL-1RA pulse therapy, engineered exosomes, phages) remain as matrix-row scope only. | After both peer-track Phase 2 queues accumulate substance — LBP track P2-1 through P2-6 (engineering + commercial + regulatory lit scans; comp-008; H02 full; chassis matrix) AND siRNA / URAT1 track P2-1 through P2-6 (kidney-tropic conjugate chemistry + commercial + regulatory lit scans; comp-009; H03 full; vs. pozdeutinurad comparative). Reflection note pre-positioned in [`open-enzyme-vision.md` §4](./open-enzyme-vision.md). | Decide whether to reframe `open-enzyme-vision.md` §4's leading sentence, the README, and platform-thesis pages. The project name itself (Open Enzyme) is a downstream decision after that reframe — naming follows substance. The accumulated peer-track substance is the trigger; the absence of that substance keeps the koji-first framing intact by default. |

---

## Sweep history

Audit trail. Date / trigger / synthesizer / reviewer / log link. **Findings landed in canonical wiki pages and were pruned from this file** during the 2026-04-27 and 2026-05-05 inbox-zero passes.

| Date | Trigger | Synthesizer | Reviewer | Log |
|---|---|---|---|---|
| 2026-05-05 | 10-file batch (blood-barrier-exploits, enzyme-deficit-deep-dive, gout-deep-dive, gout-pathophysiology, nlrp3-inhibitor-screen, open-questions, supplements-stack, theaflavins, uricase-variant-selection, zileuton) | DeepSeek V4-Pro / Gemini 2.5 Pro | Claude Opus 4.7 | [`v4-synthesis-2026-05-05-734bf51.md`](../logs/v4-synthesis-2026-05-05-734bf51.md) — 14 items walked 1-by-1 in 2026-05-05 session; substantively duplicated the unprocessed 2026-04-28 sweep |
| 2026-04-28 | 25-file batch (abcg2-modulators, androgen-urate-axis, bpc-157, colchicine, complement-c5a-gout, crispr-uricase, cross-validation, digestive-enzyme-optimization, disulfiram, engineered-koji-protocol, gout-pathophysiology, GRAPH, gut-lumen-sink, koji-endgame-strain, koji-home-fermentation, kpv-peptide, modality-chokepoint-matrix, nlrp3-inflammasome, open-enzyme-vision, open-questions, open-source-platform, self-experiment-protocol, spm-resolution-pathway, supplements-stack, validation-experiments) | Gemini 2.5 Pro | Claude Opus 4.7 | [`v4-synthesis-2026-04-28-3943bfc.md`](../logs/v4-synthesis-2026-04-28-3943bfc.md) — substantively subsumed by the 2026-05-05 sweep above (same Connections / Contradictions / Open Questions / Priority Actions); pruned together in the 2026-05-05 inbox-zero pass |
| 2026-04-27 | `wiki/open-enzyme-vision.md` | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-27-b7df491.md`](../logs/v4-synthesis-2026-04-27-b7df491.md) |
| 2026-04-27 | aspergillus-oryzae + colchicine + cross-validation + 6 others | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-27-c602f32.md`](../logs/v4-synthesis-2026-04-27-c602f32.md) — duplicate finding (ergothioneine→ABCG2), collapsed into the b7df491 sweep |
| 2026-04-26 | `wiki/supplements-stack.md` | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-26-1aea93d.md`](../logs/v4-synthesis-2026-04-26-1aea93d.md) |
| 2026-04-26 | GRAPH + abcg2-modulators + androgen-urate-axis + gut-lumen-sink | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-26-1237ff0.md`](../logs/v4-synthesis-2026-04-26-1237ff0.md) |
| 2026-04-25 | `wiki/digestive-enzyme-optimization.md` | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-25-622d2e2.md`](../logs/v4-synthesis-2026-04-25-622d2e2.md) |
| 2026-04-25 | `wiki/digestive-enzyme-optimization.md` (re-run on commit `b5c9116`) | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-25-b5c9116.md`](../logs/v4-synthesis-2026-04-25-b5c9116.md) — substantive duplicate of the 622d2e2 sweep on the same trigger; carnosine + androgen-urate axis finding overlaps with 622d2e2 Connection 6 |
| 2026-04-25 | `wiki/koji-home-fermentation.md` | DeepSeek V4-Pro | Sonnet 4.6 | [`v4-synthesis-2026-04-25-a280c0d.md`](../logs/v4-synthesis-2026-04-25-a280c0d.md) — substantive duplicate of the 622d2e2 sweep, collapsed |
| 2026-04-25 | V4 peer-review pass on the 2026-04-24 sweep (`4a40f74`) | DeepSeek V4-Pro | (peer-review of Opus 4.7) | [`v4-peer-review-2026-04-25-deepseek.md`](../logs/v4-peer-review-2026-04-25-deepseek.md) |
| 2026-04-25 | Peer-review pass on the 2026-04-24 sweep (`4a40f74`) | Gemini 2.5 Pro | (peer-review of Opus 4.7) | [`v4-peer-review-2026-04-25-gemini.md`](../logs/v4-peer-review-2026-04-25-gemini.md) — second peer-review pass on the same Claude substrate; cross-vendor heterogeneity per `open-source-platform.md §"Multi-model synthesis"` |
| 2026-04-24 | 25-file v1.2 batch (nlrp3-exploit-map restructure + 24 co-triggered) | (manual session) | Opus 4.7 | (in-session log; see commit `4a40f74` and surrounding) |
| 2026-04-23 | `wiki/nlrp3-inhibitor-screen.md` (ChEMBL appendix) | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-23 | `wiki/gout-clinical-pipeline.md` | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-23 | `wiki/cannabinoids-terpenes.md` | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-21 (origin) | All 8 April 2026 AI analyses (initial Pass 2 brainstorm) | (manual) | (manual) | This file's original content; everything from that brainstorm has either landed in canonical wiki pages (carnosine module, koji-endgame-strain, validation-experiments §1.x) or surfaced again in later sweeps. |

---

## Where actioned items live now

The 2026-04-27 inbox-zero pass pruned ~700 lines of `✓ Actioned` content. The 2026-05-05 inbox-zero pass pruned the 14-item 2026-05-05 sweep + the duplicate 2026-04-28 sweep. The findings are not lost — they're in their canonical homes:

- **Computational experiments** → [`computational-experiments.md`](./computational-experiments.md) (tracking index for all comp-NNN); per-experiment interpretive pages: [`uricase-protease-stability-computational.md`](./uricase-protease-stability-computational.md), [`lactoferrin-protease-stability-computational.md`](./lactoferrin-protease-stability-computational.md), [`daf-cd55-protease-stability-computational.md`](./daf-cd55-protease-stability-computational.md), [`food-grade-hdaci-screen-computational.md`](./food-grade-hdaci-screen-computational.md), [`supplement-abcg2-antagonism-computational.md`](./supplement-abcg2-antagonism-computational.md). Reproducible scripts + inputs + outputs at `experiments/comp-NNN-*/`.
- **Peer-track scope pages** (chase-every-avenue framing, 2026-05-05) → [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) (engineered LBP chassis as commercial-pharma peer track); [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) (siRNA / URAT1 as discovery-engine output).
- **Falsification cards** → [`hypotheses/H01-ward-dual-cassette.md`](./hypotheses/H01-ward-dual-cassette.md) (full), [`hypotheses/H02-engineered-lbp-thesis.md`](./hypotheses/H02-engineered-lbp-thesis.md) (stub; full population queued as P2-5), [`hypotheses/H03-sirna-urat1-thesis.md`](./hypotheses/H03-sirna-urat1-thesis.md) (stub; full population queued as P2-5).
- **Experiment proposals** → [`validation-experiments.md`](./validation-experiments.md) §1.1–§1.23, §2.x, §3.x. New since 2026-05-05: §1.23 Androgen × MSU × NLRP3 four-tier mechanistic protocol.
- **Self-experiment monitoring** → [`self-experiment-protocol.md`](./self-experiment-protocol.md). New since 2026-05-05: §11.1 ex vivo MSU PBMC challenge add-on for androgen-elevated subjects (Tier 4 of §1.23).
- **Open questions** → [`open-questions.md`](./open-questions.md), organized by topic. New since 2026-05-05: "Engineered LBP chassis" section + "siRNA against URAT1" section under Platform / Strategic > Novel modalities.
- **Connection findings** → in the relevant per-compound or per-mechanism wiki page (e.g. ergothioneine → ABCG2 lives in [`abcg2-modulators.md`](./abcg2-modulators.md), shio-koji format constraints in [`engineered-koji-protocol.md` §15](./engineered-koji-protocol.md), Q141K population caveat in `abcg2-modulators.md`, lactoferrin → TNFα → ABCG2 substrate-supply synergy in [`lactoferrin.md`](./lactoferrin.md) §4.7, carnosine renal-transporter arm in [`koji-endgame-strain.md`](./koji-endgame-strain.md) §2.5, native metabolite chorus in [`open-enzyme-vision.md`](./open-enzyme-vision.md) §4, androgen × NLRP3 direct axis in [`androgen-urate-axis.md`](./androgen-urate-axis.md) §"Beyond transporters", LBP peer track in [`koji-endgame-strain.md`](./koji-endgame-strain.md) §6.4 + [`abcg2-modulators.md`](./abcg2-modulators.md) Engineering Implications, etc.).
- **Coverage-matrix and chokepoint findings** → [`nlrp3-exploit-map.md`](./nlrp3-exploit-map.md), [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`open-enzyme-vision.md`](./open-enzyme-vision.md), [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md). Engineered soluble complement regulators row + per-modality scope added 2026-05-05.
- **Methodology standards** (rodent IC50 caveat, two-tier NLRP3 labeling, etc.) → [`validation-experiments.md` §1.19](./validation-experiments.md), [`nlrp3-inhibitor-screen.md`](./nlrp3-inhibitor-screen.md), [`chembl-cross-check.md`](./chembl-cross-check.md).
- **ChEMBL refresh automation** → [`.github/workflows/chembl-refresh.yml`](../.github/workflows/chembl-refresh.yml), runs quarterly (Jan/Apr/Jul/Oct 1st at 12:00 UTC).
- **Cross-doc audit history** → `git log -p wiki/synthesis.md` shows the prior un-pruned state of each sweep block; `logs/v4-synthesis-*.md` shows the original synthesizer outputs.
