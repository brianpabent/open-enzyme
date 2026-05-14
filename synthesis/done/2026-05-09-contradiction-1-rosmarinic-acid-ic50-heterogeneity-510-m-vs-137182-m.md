---
type: contradiction
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 1
global_index: 6
pass3_verdict: Confirmed, prioritize
overlap_tag: RESTATEMENT
---

# Rosmarinic acid IC50 heterogeneity (5–10 μM vs 137–182 μM) between comp-018 and its brief-scrubbed verification re-run comp-020 remains unresolved.

1. **Rosmarinic acid IC50 heterogeneity (5–10 μM vs 137–182 μM) between comp-018 and its brief-scrubbed verification re-run comp-020 remains unresolved.** Locations: `upstream-complement-modulator-sweep-computational.md §5.1` vs `upstream-complement-verification-rerun-computational.md §3.3`; also flagged inline as a limitation in comp-018. Analysis: This is not a contradiction between wiki pages (they acknowledge each other and the discrepancy) but a **load-bearing methodological warning** that propagates into any wet-lab gate or dietary recommendation involving rosmarinic acid. The 20–30× spread is assay-format-driven (Englberger 1988 classical hemolysis vs. Cimanga 1999 / Mu 2013 alternate setups) and neither value has been full-text grep-verified (both are abstract-tier). The “rosmarinic acid as headline CP0 dietary candidate” framing in comp-018 was also flagged as potentially contaminated by brief-level user phrasing — the verification re-run c omp-020 found three tied tier-1 candidates rather than one. The platform currently lacks a load-bearing, primary-source-anchored IC50 for the most-cited dietary CP0 compound. This contradiction is operational, not epistemic — it surfaces the need for a single full-text-verified, MSU-crystal-surface-specific rosmarinic acid complement assay before any downstream dietary recommendations are made.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` The operational warning is correct and load-bearing: `upstream-complement-modulator-sweep-computational.md` explicitly flags rosmarinic acid’s 5–10 µM Englberger 1988 value as abstract-tier, notes a 137–182 µM downstream-assay discrepancy, and discloses brief-contamination that over-promoted rosmarinic acid; `upstream-complement-verification-rerun-computational.md` further reframes the canonical prioritization as “no single headline compound” with rosmarinic acid, *Helicteres* lignans, and sulfated polysaccharides occupying different top-tier surfaces. This should change downstream behavior: no dietary CP0 recommendation or wet-lab gate should depend on the 5–10 µM rosmarinic-acid number without a full-text-anchored, MSU-surface-specific assay.

---

## ✓ Actioned 2026-05-14

Pass 3 verified the operational warning is real and load-bearing: the 5–10 µM Englberger 1988 lower-bound number is what `complement-c5a-gout.md` and patient-facing pages cite, while the 20–30× spread to 137–182 µM (Cimanga 1999, Mu 2013) is only flagged in the comp-018 / comp-020 analysis pages where someone reaching for the compound wouldn't necessarily look. The 2026-05-14 walkthrough question for this item was: *Pass 3 said this should change downstream behavior, but does the warning actually show up where a future reader would trip over the lower-bound number?*

Closed by adding an inline assay-format-spread caveat at the point of use in [`wiki/complement-c5a-gout.md`](../../wiki/complement-c5a-gout.md) §"Upstream-CP0 dietary axis newly active per comp-018 (2026-05-08)" — immediately after the "C3-convertase IC50 5-10 µM optimal (Englberger 1988)" citation. Caveat names the spread, calls both values abstract-tier (not full-text-verified), forbids load-bearing use until resolved, and points to the resolution path (comp-021 in Planned Analyses + comp-020 §3.3 for the discussion).

comp-021 reservation in `wiki/computational-experiments.md` §Planned Analyses (done in Item 1's walk) carries the resolution work forward formally. Sister analysis pages (`upstream-complement-modulator-sweep-computational.md`, `upstream-complement-verification-rerun-computational.md`) already discuss the spread, so no additional propagation there.

`gout-action-guide.md:119` already mentions the brief-contamination retrospective in the comp-018 / comp-020 context; the IC50 spread itself stays out of the action guide because the guide doesn't surface a specific IC50 number — it surfaces "rosmarinic acid + luteolin + Bupleurum" as candidate compounds at the candidate level.
