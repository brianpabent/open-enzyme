---
title: "Pre-2026-05-08 sweep history (archived)"
status: archive
period: 2026-04-21 → 2026-05-08
---

# Pre-2026-05-08 sweep history (archived)

This file preserves the sweep-history table from `wiki/synthesis.md` as it stood at the moment of the synthesis filesystem migration (2026-05-08). After this date, each sweep gets its own per-file entry at `synthesis/history/<sweep-date>-<short-sha>.md` per [spec §5.6](../../operations/specs/2026-05-08-synthesis-filesystem-migration.md).

Audit trail. Date / trigger / synthesizer / reviewer / log link. **Findings landed in canonical wiki pages** during the 2026-04-27, 2026-05-05, 2026-05-06, and 2026-05-08 inbox-zero passes.

| Date | Trigger | Synthesizer | Reviewer | Log |
|---|---|---|---|---|
| 2026-05-08 | 5-file batch (bio-ai-tools, manual-literature-mining, medicinal-mushroom-compound-mapping-computational, open-source-platform, paperclip-deep-dive — commit `e842754`, diff base `440a73a`) | Gemini 2.5 Pro | **OpenAI GPT-5.5** *(first run on the swapped-in Pass 3 reviewer; replaced Claude Opus 4.7 in the Pass 3 slot)* | [`v4-synthesis-2026-05-08-e842754.md`](../../logs/v4-synthesis-2026-05-08-e842754.md) — 12 items walked 1-by-1 in 2026-05-08 session. Surfaced cordycepin × pentostatin × GLPP ADA synergy thesis (formalized as `validation-experiments.md` §1.26 five-arm assay) + the meta-pivot to a patient/practitioner-facing application surface (new [`gout-action-guide.md`](../../wiki/gout-action-guide.md) + top-of-page triage on [`supplements-stack.md`](../../wiki/supplements-stack.md) + Strategic Reflections Queue entry on `fresh-stack.py` propagation discipline). Triggered comp-018 (Upstream Complement Modulator Sweep), brief-contamination caught mid-walkthrough, comp-020 verification re-run; meta-discipline codified at [`scripts/SWEEP-ARCHITECTURE.md` §"Subagent brief hygiene"](../../scripts/SWEEP-ARCHITECTURE.md). Triggered comp-019 (gut-lumen uricase × ABCG2 genotype mining + flux model). |
| 2026-05-07 | 17-file batch (commit `abc8de9`) | Gemini 2.5 Pro | Claude Opus 4.7 | [`v4-synthesis-2026-05-07-abc8de9.md`](../../logs/v4-synthesis-2026-05-07-abc8de9.md) — 7 items walked. PRPS chokepoint propagation, MinION dual-use cross-refs, H07 cross-ref. |
| 2026-05-07 | 7-file batch (commit `77d0f6e`) | Gemini 2.5 Pro | Claude Opus 4.7 | [`v4-synthesis-2026-05-07-77d0f6e.md`](../../logs/v4-synthesis-2026-05-07-77d0f6e.md) — 9 items walked. Cross-track URAT1 redundancy, TCM tiered SOPs, ROS/CP1b row, §1.27 EGT+Lf assay. |
| 2026-05-06 | 35-file batch (commit `121731c`, diff base `3e928d3`) | DeepSeek V4-Pro | Claude Opus 4.7 | [`v4-synthesis-2026-05-06-121731c.md`](../../logs/v4-synthesis-2026-05-06-121731c.md) — 12 items walked in second-pass session. |
| 2026-05-05 | 13-file batch (commit `3e928d3`) | Gemini 2.5 Pro | Claude Opus 4.7 | [`v4-synthesis-2026-05-05-3e928d3.md`](../../logs/v4-synthesis-2026-05-05-3e928d3.md) — 14 items. Triggered CLAUDE.md Rule 4 codification (DAF SCR1-4 disulfide hallucination 12 → 8). |
| 2026-05-05 | 4-file batch (commit `d6b4210`) | Gemini 2.5 Pro | Claude Opus 4.7 | [`v4-synthesis-2026-05-05-d6b4210.md`](../../logs/v4-synthesis-2026-05-05-d6b4210.md) — 6 items. |
| 2026-05-05 | Pass-3-prepend-bug block (commit `487fad3`) | DeepSeek V4-Pro | (manual transcription) | [`v4-synthesis-2026-05-05-487fad3.md`](../../logs/v4-synthesis-2026-05-05-487fad3.md) |
| 2026-05-05 | engineered-koji-protocol + koji-endgame-strain (commit `6e3614d`) | Gemini 2.5 Pro | Claude Opus 4.7 | [`v4-synthesis-2026-05-05-6e3614d.md`](../../logs/v4-synthesis-2026-05-05-6e3614d.md) — duplicate; collapsed |
| 2026-05-05 | 10-file batch | DeepSeek V4-Pro / Gemini 2.5 Pro | Claude Opus 4.7 | [`v4-synthesis-2026-05-05-734bf51.md`](../../logs/v4-synthesis-2026-05-05-734bf51.md) |
| 2026-04-28 | 25-file batch | Gemini 2.5 Pro | Claude Opus 4.7 | [`v4-synthesis-2026-04-28-3943bfc.md`](../../logs/v4-synthesis-2026-04-28-3943bfc.md) — subsumed by 2026-05-05 |
| 2026-04-27 | open-enzyme-vision | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-27-b7df491.md`](../../logs/v4-synthesis-2026-04-27-b7df491.md) |
| 2026-04-27 | aspergillus-oryzae + colchicine + 6 others | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-27-c602f32.md`](../../logs/v4-synthesis-2026-04-27-c602f32.md) — duplicate; collapsed |
| 2026-04-26 | supplements-stack | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-26-1aea93d.md`](../../logs/v4-synthesis-2026-04-26-1aea93d.md) |
| 2026-04-26 | GRAPH + abcg2-modulators + androgen-urate-axis + gut-lumen-sink | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-26-1237ff0.md`](../../logs/v4-synthesis-2026-04-26-1237ff0.md) |
| 2026-04-25 | digestive-enzyme-optimization | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-25-622d2e2.md`](../../logs/v4-synthesis-2026-04-25-622d2e2.md) |
| 2026-04-25 | digestive-enzyme-optimization re-run | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-25-b5c9116.md`](../../logs/v4-synthesis-2026-04-25-b5c9116.md) — duplicate of 622d2e2 |
| 2026-04-25 | koji-home-fermentation | DeepSeek V4-Pro | Sonnet 4.6 | [`v4-synthesis-2026-04-25-a280c0d.md`](../../logs/v4-synthesis-2026-04-25-a280c0d.md) — duplicate; collapsed |
| 2026-04-25 | V4 peer-review pass on 2026-04-24 sweep | DeepSeek V4-Pro | (peer-review of Opus 4.7) | [`v4-peer-review-2026-04-25-deepseek.md`](../../logs/v4-peer-review-2026-04-25-deepseek.md) |
| 2026-04-25 | Peer-review pass on 2026-04-24 sweep | Gemini 2.5 Pro | (peer-review of Opus 4.7) | [`v4-peer-review-2026-04-25-gemini.md`](../../logs/v4-peer-review-2026-04-25-gemini.md) — second peer-review on same Claude substrate; cross-vendor heterogeneity |
| 2026-04-24 | 25-file v1.2 batch (nlrp3-exploit-map restructure) | (manual session) | Opus 4.7 | (in-session log; commit `4a40f74`) |
| 2026-04-23 | nlrp3-inhibitor-screen (ChEMBL appendix) | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-23 | gout-clinical-pipeline | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-23 | cannabinoids-terpenes | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-21 (origin) | All 8 April 2026 AI analyses (initial Pass 2 brainstorm) | (manual) | (manual) | Original brainstorm content; everything has either landed in canonical wiki pages or surfaced again in later sweeps. |
