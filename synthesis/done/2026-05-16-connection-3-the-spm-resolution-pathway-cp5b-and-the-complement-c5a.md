---
type: connection
sweep_date: 2026-05-16
sweep_sha: 91acf49
section_index: 3
global_index: 3
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# The SPM resolution pathway (CP5b) and the complement C5a priming pathway (CP0) are mechanistically linked through the aggNET resolution loop — but the corpus treats them as independent chokepoints with no named cross-talk mechanism.

3. **The SPM resolution pathway (CP5b) and the complement C5a priming pathway (CP0) are mechanistically linked through the aggNET resolution loop — but the corpus treats them as independent chokepoints with no named cross-talk mechanism.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `spm-resolution-pathway.md`, `complement-c5a-gout.md`, `nlrp3-exploit-map.md`
   - *Page-pair linkage:* `spm-resolution-pathway.md` cross-references `complement-c5a-gout.md` (both are v1.2 exploit map pages). Both pages independently describe the aggNET resolution loop (Schauer 2014, PMID 24784231): aggregated neutrophil extracellular traps sequester and degrade cytokines including C5a. `spm-resolution-pathway.md` §7.3 explicitly names the "CP0 → CP6a → CP5b loop" and states "aggNET-mediated C5a degradation reduces further CP0 priming → self-limiting flare." `complement-c5a-gout.md` §3.1 cites Cumpelik 2016 on neutrophil microvesicles resolving gout by inhibiting C5a-mediated priming. But neither page operationalizes this cross-talk as a **testable intervention synergy**: if SPMs promote aggNET formation (CP5b → resolution), and aggNETs degrade C5a (resolution → CP0 dampening), then SPM supplementation should produce a measurable drop in serum C5a during the resolution phase of a flare. This is a falsifiable prediction that neither page makes.
   - *Why It Matters:* The CP0 chokepoint is the platform's most expensive gap — avacopan at ~$150K/year is the only direct antagonist. If SPMs (omega-3, $30/month) can indirectly close CP0 through the aggNET resolution loop, the platform's CP0 coverage story changes from "pharma-only" to "dietary + pharma." The prediction is testable: serum C5a should drop during the resolution phase of a flare in subjects with high omega-3 index, and should NOT drop in subjects with low omega-3 index. This is a zero-cost add-on to the existing self-experiment protocol's C5a measurement (§3.7).
   - *Suggested Action:* Add a specific prediction to `spm-resolution-pathway.md` §7.3: "If SPMs promote aggNET-mediated C5a degradation, then serum C5a should decline during flare resolution in DHA-loaded subjects but not in DHA-deficient subjects." Add a contingent analysis to `self-experiment-protocol.md` §3.7: if C5a is measured at flare onset AND at resolution (not just baseline + week 12), compute the C5a decline slope and correlate with omega-3 index. No additional cost — just an analysis plan on existing data.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The cross-talk is real: `spm-resolution-pathway.md` §7.3 already names the CP0 → CP6a → CP5b loop and says aggNET-mediated C5a degradation reduces further CP0 priming, while `complement-c5a-gout.md` cites Cumpelik 2016 on C5a-mediated priming and resolution. The new element is operational: adding flare-resolution C5a slope analysis stratified by omega-3 index is a testable prediction not already built into `self-experiment-protocol.md`, which currently carries C5a as a baseline/week-12 CP0 marker.

---

**WALKED 2026-05-19 — Closed (falsifiable prediction operationalized in spm-resolution-pathway.md §7.3 + self-experiment-protocol.md C5a row).**

Actioned:
- ✓ Added "Falsifiable prediction — serum C5a decline slope stratified by omega-3 index" subsection to `spm-resolution-pathway.md` §7.3. Documents the operational test (4-step protocol: onset C5a → resolution C5a → compute slope → correlate with omega-3 index), the platform implication (CP0 coverage shifts from "pharma-only" to "dietary + pharma" if confirmed), and the epistemic discipline (mechanism-level prediction, not a clinical-effect-size claim — even if confirmed, the dietary arm doesn't replace avacopan for refractory cases, it shifts the first-line coverage class).
- ✓ Added optional flare-trajectory addition to `self-experiment-protocol.md` C5a row: measure C5a at flare onset + resolution, pair with omega-3 index, compute decline slope. ~$100-200/flare added lab cost; doesn't change intervention protocol.
- Self-experiment relevance flagged to Brian: this is testable in his own protocol on his next flare event. He's flagged he's "open to the self-experiment but doesn't know what flare-resolution C5a measurement is" — the explanation given in walkthrough was: standard 0-24h onset draw + 7-14d resolution draw, pair with omega-3 index from OmegaQuant or equivalent, ~$50-100/draw plus venipuncture cost.

Also closes:
- 2026-05-16 experiment-3 (Serum C5a decline-slope analysis during flare resolution, stratified by omega-3 index — the experiment-card form of the same operational test).
