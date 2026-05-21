# Luteolin — Two-model annotated cross-check

**Date:** 2026-05-21
**Protocol:** Two independent models, inline disagreement annotation per Open Enzyme CLAUDE.md §"Translation protocol".

- **Model A:** Claude Opus 4.7 — see `luteolin-source-read-2026-05-21.md`
- **Model B:** DeepSeek (`deepseek/deepseek-chat-v3`) — see `luteolin-deepseek-counterread-2026-05-21.json`

## Classification consensus

Both models classify luteolin as **CFH-INDEPENDENT** (Model A: Medium confidence; Model B: Medium confidence). Both flag the same uncertainty source: the Zhang 2008 paper does not pin luteolin's complement-cascade target at single-residue or even single-component resolution — it confirms broad CP+AP hemolytic inhibition (CH50 0.19 mM / AP50 0.17 mM) and attributes activity to the 4'-OH B-ring substitution, but does not identify a specific cascade node.

## Annotated cross-check

Luteolin's anti-complementary activity per Zhang 2008 (PMC7126446) is **broad-spectrum CP+AP hemolytic inhibition at hundred-micromolar potency**, with the 4'-OH B-ring identified as essential for the activity. **{Model A: "Most likely active-site / substrate-binding inhibition of C3 convertase formation" | Model B: "Mechanism site ambiguity; no direct evidence of luteolin's interaction with CFH"}** [TRANSLATION-DISAGREEMENT: Both models agree on CFH-independence but disagree on whether the mechanism is positively identified. Model A commits to "convertase-level inhibition" as the most likely mechanism based on (a) matched CP/AP IC50 implies a shared node, (b) analogous mechanism in rosmarinic acid (Englberger 1988), (c) flavonoid B-ring 4'-OH protein-binding mode is consistent with hydrophobic-pocket targeting in convertase substructures. Model B is more cautious — declines to commit to a specific mechanism site beyond "non-CFH-dependent". This is a "confidence framing" rather than a "scientific direction" disagreement. For load-bearing downstream reasoning (UKB cross-tab prediction), the conservative framing is to use Model B's stance.]

**{Model A: "negative direction (effect ≥ in carriers) but wider uncertainty than rosmarinic acid" | Model B: "null direction (no differential effect)"}** [TRANSLATION-DISAGREEMENT: Same negative-vs-null disagreement as rosmarinic acid. Same logic — Model A reasons from genotype-baseline-severity amplification, Model B reasons from mechanism-independence-implies-genotype-indifference. The matched IC50 between CP and AP pathways in Zhang 2008 (0.19 vs 0.17 mM) is consistent with a node common to both pathways (C3 itself or convertase active site); this is functionally upstream of CFH's AP-specific regulatory role.]

Luteolin's multi-mode gout-relevance (XO IC50 550 nM + URAT1 downregulation per comp-013) is also CFH-orthogonal. **Both models do not raise this as a CFH-dependence consideration.** Operational caveat (Model A only): the UKB cross-tab for luteolin × Y402H × incident gout would be confounded by the urate-axis mode running in parallel with the complement-mode. Brian's UKB collaborators should consider cross-tabbing against Apiaceae-specific (celery / parsley / chamomile) dietary intake + 24h-urate as an intermediate readout to dissociate the two modes.

## Disagreement notes

- **mechanism specificity:** Model A commits to "convertase-level inhibition" as most-likely; Model B reserves judgement. Model B's more conservative framing is appropriate given the absence of depletion-rescue or single-residue binding data for luteolin specifically.

- **hedging — predicted Y402H direction:** Model A picks "negative (effect ≥ in carriers)"; Model B picks "null". Same logic as rosmarinic acid disagreement.

- **multi-mode confound:** Model A explicitly raises XO + URAT1 modes as a confound for the UKB cross-tab; Model B does not. This is a brief-hygiene gap in Model B's reasoning (the primary-source bundle did not foreground the multi-mode context). Not a science disagreement.

## Recommended falsification test (consensus)

Same as rosmarinic acid: luteolin on MSU-crystal-driven complement activation in CFH-depleted vs CFH-replete serum. If retained activity in CFH-depleted serum, CFH-independence is confirmed. Additionally, for the UKB cross-tab, Model A recommends pre-specifying both the negative (carriers benefit more) and null (no genotype interaction) directions with adequate power for each.
