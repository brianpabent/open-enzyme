---
type: priority-action
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 2
global_index: 10
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Add the ClockBase-instantiation and proxy-quality lesson to `autonomous-screening-methodology.md`.

2. **Add the ClockBase-instantiation and proxy-quality lesson to `autonomous-screening-methodology.md`.** Cite comp-022 v2 as the first OE operational instantiation of the exhaustive-search-then-rank pattern, and document the GC-clamp → ViennaRNA retrofit (rho = 0.241) as a standing caveat for future comp-NNNs using the pattern. (Rationale: Connection 2.)

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` The proxy-quality lesson is worth adding, but the "first OE operational instantiation" part is already present in `autonomous-screening-methodology.md`: the page cites comp-022 as the operational instantiation, with 43,200 candidates, 5 orthogonal models, N-of-5 ≥4, 71 promoted cassettes, and 100% top-cluster survival. What is missing there is the more cautionary v2 detail from `uricase-cassette-ranking-computational.md` §9.4: the v1 GC-clamp proxy correlated weakly with real ViennaRNA MFE (rho = 0.241) and the v2 gate dropped 430 of 501 v1-shortlisted cassettes. Revise the action to "add the proxy-risk worked example," not "add comp-022 as an instantiation."

---

## ✓ Already actioned 2026-05-15 (closure note — duplicate of Item 25)

Same content as Item 25 (2026-05-15 Connection 2 in this same sweep), framed as a Priority Action instead of a Connection. Pass 3 issued the same "Partial" verdict with the same correction (comp-022 already cited; narrow useful addition is the proxy-failure detail).

Item 25 shipped the action: `wiki/autonomous-screening-methodology.md` got a new "Proxy-quality lesson from comp-022 v2 retrofit (added 2026-05-15)" paragraph appended directly after the existing operational-instantiation paragraph (commit `f2b70b5`). Captures Spearman ρ = 0.241; 430/501 v1-shortlisted cassettes re-ranked by v2; v1 top cluster survived 100%; generalized rule (prefer real biophysical models over cheap heuristics unless proxy-vs-real correlation ≥ 0.7 published).

No new wiki work. Closing as duplicate of Item 25's already-shipped action.
