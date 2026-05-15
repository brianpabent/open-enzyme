---
type: open-question
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 1
global_index: 10
pass3_verdict: Confirmed
overlap_tag: RESTATEMENT
---

# What N-of-M concordance threshold (across orthogonal comp-NNN scoring models) should gate wet-lab promotion?

1. **What N-of-M concordance threshold (across orthogonal comp-NNN scoring models) should gate wet-lab promotion?** ClockBase used ~30/40 aging clocks (75%). Open Enzyme’s cassette-engineering models are fewer — likely ~4/5 (80%) — but the exact threshold has not been calibrated against retrospective comp-001 through comp-014 outcomes. This is a pre-investment calibration question for any ClockBase-style pipeline. (Connection #1)

> **Pass 3 review — Confirmed.** `[OVERLAP: RESTATEMENT]` This is already an open methodological question in `autonomous-screening-methodology.md`, which asks for calibration of the N-of-M concordance threshold and explicitly contrasts ClockBase’s ~30/40 clocks (~75%) with a likely Open Enzyme threshold of ~4/5 (~80%) across fewer orthogonal models. The Pass 2 item is correct, but it is a restatement of an existing methodology follow-up rather than a new open question.

---

## ✓ Already actioned 2026-05-15 (closure note)

No new wiki work needed — the question is already tracked, and has been partially answered empirically:

- **Question itself:** [`wiki/autonomous-screening-methodology.md` line 128](../../wiki/autonomous-screening-methodology.md) — listed under "Open follow-ups" with explicit framing: *"What's the right threshold for promoting comp-NNN candidates to wet lab? ClockBase uses ~30/40 (75%); we likely need 4/5 (80%) or higher for our smaller orthogonal-model set. Pin via retrospective analysis of comp-001 through comp-014 verdicts."*
- **Operational answer:** [`wiki/autonomous-screening-methodology.md` line 95](../../wiki/autonomous-screening-methodology.md) — comp-022 (2026-05-14) instantiated the pattern at full cardinality (43,200 uricase cassette candidates, 5 orthogonal scoring models, **N-of-5 ≥ 4 gate (80%)** → 71 promoted cassettes). The v1→v2 retrofit confirmed the v1 top cluster at 100% survival. The 4/5 threshold is now production-instantiated; what's still open is retrospective calibration against comp-001 through comp-014 outcomes.

Pass 3's `RESTATEMENT` verdict was correct. Closing here to avoid duplicate surfaces.
