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

**(none — inbox zero as of 2026-04-28).**

The 2026-04-27 walkthrough actioned all seven prior pending items; the work landed in the canonical wiki pages listed in [Where actioned items live now](#where-actioned-items-live-now) below. New entries will appear here when the next sweep daemon run surfaces a finding the canonical pages don't already cover.

For the audit trail of the 2026-04-27 walkthrough specifically, see `git log --since=2026-04-27` on this repo — the seven items each landed in their own commit cluster, with `[skip-wiki-sweep]` markers and one-line descriptions of where each finding's canonical home is.

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

The 2026-04-27 inbox-zero pass pruned ~700 lines of `✓ Actioned` content. The findings are not lost — they're in their canonical homes:

- **Experiment proposals** → [`validation-experiments.md`](./validation-experiments.md) §1.1–§1.19, §2.x, §3.x.
- **Open questions** → [`open-questions.md`](./open-questions.md), organized by topic.
- **Connection findings** → in the relevant per-compound or per-mechanism wiki page (e.g. ergothioneine → ABCG2 lives in [`abcg2-modulators.md`](./abcg2-modulators.md), shio-koji format constraints in [`engineered-koji-protocol.md` §15](./engineered-koji-protocol.md), Q141K population caveat in `abcg2-modulators.md`, etc.).
- **Coverage-matrix and chokepoint findings** → [`nlrp3-exploit-map.md`](./nlrp3-exploit-map.md), [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`open-enzyme-vision.md`](./open-enzyme-vision.md).
- **Methodology standards** (rodent IC50 caveat, two-tier NLRP3 labeling, etc.) → [`validation-experiments.md` §1.19](./validation-experiments.md), [`nlrp3-inhibitor-screen.md`](./nlrp3-inhibitor-screen.md), [`chembl-cross-check.md`](./chembl-cross-check.md).
- **ChEMBL refresh automation** → [`.github/workflows/chembl-refresh.yml`](../.github/workflows/chembl-refresh.yml), runs quarterly (Jan/Apr/Jul/Oct 1st at 12:00 UTC).
- **Cross-doc audit history** → `git log -p wiki/synthesis.md` shows the prior un-pruned state of each sweep block; `logs/v4-synthesis-*.md` shows the original synthesizer outputs.
