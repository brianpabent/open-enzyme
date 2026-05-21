# Rosmarinic acid — Two-model annotated cross-check

**Date:** 2026-05-21
**Protocol:** Two independent models, inline disagreement annotation per Open Enzyme CLAUDE.md §"Translation protocol".

- **Model A:** Claude Opus 4.7 (anthropic) — see `rosmarinic_acid-source-read-2026-05-21.md`
- **Model B:** DeepSeek (`deepseek/deepseek-chat-v3` via OpenRouter, native-Chinese-trained) — see `rosmarinic_acid-deepseek-counterread-2026-05-21.json`

## Classification consensus

Both models classify rosmarinic acid as **CFH-INDEPENDENT** (Model A: High confidence; Model B: High confidence).

Both models point to the same load-bearing binding-site evidence: **Sahu 1999's covalent attachment to the thioester-containing α'-chain of nascent C3b** (IC50 34 μM) is mechanistically upstream of CFH's regulatory functions on already-deposited C3b.

## Annotated cross-check

The thioester-attachment mechanism of rosmarinic acid (Sahu 1999, PMID 10353266) acts on nascent fluid-phase C3b at the Cys988 α'-chain reactive carbonyl, **before** the C3b covalently attaches to a target surface. CFH's regulatory function (decay-acceleration of C3bBb + Factor-I cofactor for C3b→iC3b) operates on already-deposited surface C3b — downstream of where rosmarinic acid acts. **{Model A: "Y402H carriers retain full benefit; effect size in carriers ≥ non-carriers (negative direction)" | Model B: "Y402H direction is null (no differential effect)"}** [TRANSLATION-DISAGREEMENT: Models agree on CFH-independence but disagree on Y402H × incident-gout interaction direction. Model A reasons that Y402H carriers have *more* unregulated surface C3b at baseline (broken regulator), so removing the upstream substrate produces a *larger absolute* drop in MSU-driven C5a — predicting greater protection in carriers (negative direction). Model B reasons that if mechanism does not engage CFH at all, there is no reason to expect differential effect between Y402H genotypes — predicting null direction. This is a substantive disagreement about whether genotype-baseline severity translates into genotype-stratified intervention-effect-size. Recommend the UKB cross-tab be powered to distinguish both: 'effect ≥ in carriers (Model A)' vs 'effect identical across genotypes (Model B)'. The AMD-paradox direction (+ harm in carriers) is rejected by both models.]

The C3 convertase active-site inhibition mechanism (Englberger 1988 PMID 3198307, optimal 5-10 μM) acts upstream of CFH as well — by preventing convertase assembly / catalysis, the substrate pool that CFH would normally regulate is never generated. Both models agree on this.

The C5 convertase mechanism (Peake 1991 PMID 1761351, mM-range) is a separate kinetic regime that is unlikely to be operative at dietary-intake plasma concentrations of rosmarinic acid. Both models do not weight this as load-bearing for the Y402H prediction.

## Disagreement notes

- **hedging — predicted Y402H direction:** Model A picks "negative (effect ≥ in carriers)"; Model B picks "null". Both agree the AMD-paradox direction (+ harm in carriers) does NOT transfer. The negative-vs-null disagreement is about whether genotype-baseline severity amplifies the intervention's absolute effect size. **For the UKB cross-tab, both predictions need separate falsification thresholds:** a null result (Model B vindicated) at adequate power is informative; a *positive* result (carriers worse, AMD-paradox transfers) refutes both models and would force retiring rosmarinic acid from the upstream-CP0 stack.

- **uncertainty framing:** Both models flag the absence of direct CFH-depletion experiments as the dominant uncertainty. Both recommend the same falsification test (in-vitro CFH-depleted serum + rosmarinic acid + MSU crystal → C5a generation readout).

## Recommended falsification test (consensus)

Run rosmarinic acid (34 μM, 100 μM, 340 μM) on MSU-crystal-driven complement activation in CFH-depleted serum vs CFH-replete serum. If rosmarinic acid retains identical C5a-generation suppression in CFH-depleted serum, CFH-independence is confirmed. If activity drops in CFH-depleted serum, mechanism is partly CFH-dependent and the AMD-paradox direction starts to be in scope.
