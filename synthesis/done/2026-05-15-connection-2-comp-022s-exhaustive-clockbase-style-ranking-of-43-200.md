---
type: connection
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 2
global_index: 2
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# comp-022’s exhaustive ClockBase-style ranking of 43,200 uricase cassettes is a transferable platform methodology — and its v2 retrofit exposes a critical lesson about proxy quality in computational screening that feeds back into the autonomous-screening-methodology page.

2. **comp-022’s exhaustive ClockBase-style ranking of 43,200 uricase cassettes is a transferable platform methodology — and its v2 retrofit exposes a critical lesson about proxy quality in computational screening that feeds back into the autonomous-screening-methodology page.** *Supported*. `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `uricase-cassette-ranking-computational.md`, `autonomous-screening-methodology.md`, `computational-experiments.md`, `cassette-compatibility-computational.md`, `daf-cd55-scr14-truncated-computational.md`, `chaperone-orthogonal-stacking.md`
   - *Page-pair linkage:* `uricase-cassette-ranking-computational.md` cross-references `autonomous-screening-methodology.md` as the source pattern, but the reverse link does not yet exist — the methodology page does not cite comp-022 as its first operational instantiation. The v2 retrofit (ViennaRNA MFE vs. GC-clamp proxy, Spearman rho = 0.241) is not yet discussed in `autonomous-screening-methodology.md`’s §“Composite ranking across orthogonal predictors.”
   - *Why It Matters:* comp-022 v1 used a GC-content + GC-clamp + palindromic-4mer proxy for mRNA 5′ secondary structure. The v2 retrofit with real ViennaRNA MFE showed the proxy was weakly correlated (rho = 0.241) and materially shifted the ranking of 430 of 501 shortlisted cassettes. This is a concrete, grep-verified example of the exact failure mode that `autonomous-screening-methodology.md` §“Composite ranking across orthogonal predictors” warns against: “disagreement across orthogonal models = uncertainty signal.” The lesson — that cheap proxies can be noise and should be replaced by real biophysical models before wet-lab commitment — generalizes to every future comp-NNN that uses computational screening. The ClockBase pattern (exhaustive enumeration → multi-model concordance → wet-lab promotion) is now instantiated in the OE corpus; the proxy-quality lesson should be documented as a standing caveat for any new application of the pattern.
   - *Suggested Action:* Add a paragraph to `autonomous-screening-methodology.md` §“Composite ranking across orthogonal predictors” citing comp-022 v2 as the first OE instantiation and the GC-clamp → ViennaRNA retrofit as a worked example of proxy risk. In `computational-experiments.md`, add a note that future comp-NNNs using the ClockBase pattern should budget for real biophysical models (RNAfold, ESMFold, AlphaFold) rather than cheap proxies, unless the proxy’s correlation is explicitly validated.

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` The finding's "reverse link does not yet exist" premise is false: `autonomous-screening-methodology.md` already contains an "Operational instantiation (comp-022, 2026-05-14)" paragraph citing 43,200 uricase cassette candidates, 5 orthogonal models, N-of-5 ≥4, 71 promoted cassettes, and 100% survival of the v1 top cluster. The useful addition is narrower: the methodology page does not yet carry the v1 GC-clamp proxy failure number, while `uricase-cassette-ranking-computational.md` §9.4 reports Spearman rho = 0.241 and 430/501 v1-shortlisted cassettes dropped by the v2 gate. Keep the proxy-quality caveat; delete the claim that comp-022 is absent from the methodology page.

---

## ✓ Actioned 2026-05-15

Pass 3's correction held: `autonomous-screening-methodology.md` already had the "Operational instantiation (comp-022, 2026-05-14)" paragraph citing the comp-022 numbers. The narrow real addition was the v1→v2 proxy-failure detail.

**Files shipped:**

- **`wiki/autonomous-screening-methodology.md`** — new "Proxy-quality lesson from comp-022 v2 retrofit (added 2026-05-15)" paragraph appended directly after the existing comp-022 operational-instantiation paragraph. Captures: Spearman ρ = 0.241 between v1 GC-clamp proxy and v2 ViennaRNA MFE; 430/501 v1-shortlisted cassettes re-ranked by v2; v1 top cluster survived intact at 100%; the lesson generalizes (cheap proxies can be near-uncorrelated with the real biophysical quantity; proxy-vs-real correlation must be explicitly validated before wet-lab promotion of long-tail candidates); operational rule for new comp-NNNs (prefer real biophysical models over cheap heuristics unless a published proxy-vs-real correlation ≥ 0.7 exists). Cross-link to where the discipline lives operationally: walk-synthesis SKILL.md §4 briefing rule #9 + Pass 3 review prompts' "Evaluation depth > tool coverage" anchor (both BioDesignBench-anchored, now empirically corroborated by comp-022's own retrofit).

**Pass 2's secondary suggestion declined:** adding a note in `computational-experiments.md` about future comp-NNNs budgeting for real biophysical models would be triplicate — the discipline already lives in `autonomous-screening-methodology.md` (this edit), the walk-synthesis SKILL.md briefing rules, and the Pass 3 prompts. Further surfacing on `computational-experiments.md` would dilute, not clarify.

Pass 3 verdict honored. Closing.
