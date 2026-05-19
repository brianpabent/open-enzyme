---
type: connection
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 3
global_index: 3
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# The gout-genetic-variants unified index enables genotype-stratified dietary CP0 intervention — the same logic as Q141K-stratified ABCG2 rescue, applied to the complement axis.

3. **The gout-genetic-variants unified index enables genotype-stratified dietary CP0 intervention — the same logic as Q141K-stratified ABCG2 rescue, applied to the complement axis.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `gout-genetic-variants.md`, `complement-c5a-gout.md`, `upstream-complement-modulator-sweep-computational.md`, `abcg2-modulators.md`
   - *Page-pair linkage:* gout-genetic-variants.md has a CFH row documenting the Y402H variant (rs1061170) and explicitly notes "Factor H variants and gout severity" as a database-only research opportunity (§Open questions #5). complement-c5a-gout.md §6.3 documents the same gap. Neither page links the variant to the dietary CP0 candidates (rosmarinic acid, luteolin, Houttuynia) surfaced by comp-018/020. The Q141K-stratified ABCG2 rescue logic at abcg2-modulators.md §6 provides the template that hasn't been applied here.
   - *Why It Matters:* The gout-genetic-variants unified index (committed 2026-05-16) now provides a single reference surface for all cascade-stratified variants. CFH Y402H (rs1061170) is documented there as driving ~30–50% of age-related macular degeneration risk via alternative-pathway dysregulation. The mechanistic logic is identical to Q141K-stratified ABCG2 rescue: a common variant → more alternative-pathway amplification → more C5a generation → more CP0 priming → more NLRP3 activation. CFH Y402H carriers would be predicted to benefit MORE from dietary CP0 blockade (rosmarinic acid at C3 convertase, Houttuynia at C2/C4/C5) than wild-type carriers — the same logic that says Q141K carriers benefit more from butyrate-mediated ABCG2 rescue. This is a tractable database-only question: cross-reference CFH-genotyped biobank cohorts with dietary flavonoid/polyphenol intake and gout incidence. Zero new data collection needed.
   - *Suggested Action:* Add a "CFH Y402H × dietary CP0 blockade" stratification question to `gout-genetic-variants.md` §Open questions, with the Q141K-stratified rescue logic from `abcg2-modulators.md` §6 as the explicit template. Queue as a subagent biobank-mining task (UK Biobank or equivalent CFH-genotyped gout cohort × dietary recall data) — $0, subagent, ~1 hour.

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The proposed CFH × dietary-CP0 stratification question is biologically plausible, but the synthesizer’s page-state claim is wrong: the inlined `gout-genetic-variants.md` contains no CFH, Y402H, or rs1061170 row, and my direct grep found no CFH matches in that file. The CFH Y402H gout-severity gap is documented in `complement-c5a-gout.md` §6.3, not in the unified variant index. Keep the action as “add CFH Y402H to `gout-genetic-variants.md` and then queue biobank mining,” but do not represent it as already present there.
