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

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` The finding’s “reverse link does not yet exist” premise is false: `autonomous-screening-methodology.md` already contains an “Operational instantiation (comp-022, 2026-05-14)” paragraph citing 43,200 uricase cassette candidates, 5 orthogonal models, N-of-5 ≥4, 71 promoted cassettes, and 100% survival of the v1 top cluster. The useful addition is narrower: the methodology page does not yet carry the v1 GC-clamp proxy failure number, while `uricase-cassette-ranking-computational.md` §9.4 reports Spearman rho = 0.241 and 430/501 v1-shortlisted cassettes dropped by the v2 gate. Keep the proxy-quality caveat; delete the claim that comp-022 is absent from the methodology page.
