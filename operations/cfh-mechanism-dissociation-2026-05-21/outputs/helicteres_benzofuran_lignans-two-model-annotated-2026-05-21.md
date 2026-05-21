# Helicteres benzofuran lignans — Two-model annotated cross-check

**Date:** 2026-05-21
**Protocol:** Two independent models, inline disagreement annotation per Open Enzyme CLAUDE.md §"Translation protocol".

- **Model A:** Claude Opus 4.7 — see `helicteres_benzofuran_lignans-source-read-2026-05-21.md`
- **Model B:** DeepSeek (`deepseek/deepseek-chat-v3`) — see `helicteres_benzofuran_lignans-deepseek-counterread-2026-05-21.json`

## Classification consensus

Both models classify Helicteres benzofuran lignans as **CFH-INDEPENDENT** (Model A: Medium confidence — bounded by replication risk; Model B: High confidence — taking Yin 2016 target identification at face value).

The Yin 2016 (PMC6273495) depletion-rescue mapping is the load-bearing anchor: compound 4 (machicendonal) targets C1q, C2, C3, C4, C9; compound 5 (dihydrodehydrodiconiferyl alcohol) targets C1q, C2, C3, C9 (NOT C4). None of these targets overlap with CFH's regulatory substrates.

## Annotated cross-check

The depletion-rescue target identification in Yin 2016 (compound 4: C1q + C2 + C3 + C4 + C9; compound 5: C1q + C2 + C3 + C9) is **structurally orthogonal to CFH's regulatory function on surface-deposited C3b and the C3bBb convertase**. {Model A: "Multi-target lignan pattern (C1q + C2 + C3 + C4 + C9) is structurally orthogonal to CFH's CCP6-8 binding surface" | Model B: "CFH does not regulate C1q, C2, C4, or C9, and its binding site (CCP6-8) is structurally orthogonal to the multi-target lignan pattern"} — same framing. No TRANSLATION-DISAGREEMENT.

CH50 values verified directly from PMC6273495: compound 4 CH50 = 40 μM (AP50 105 μM); compound 5 CH50 = 9 μM (AP50 21 μM). Both models accept these. **The CP-pathway IC50 is the more-potent regime** (9 μM CH50 vs 21 μM AP50 for compound 5), inconsistent with a CFH-binding-surface mechanism (CFH is AP-specific; a CFH-binding mode would predict AP-selective potency).

**{Model A: "Medium confidence — bounded by single-paper anchor; comp-018 Phase 2 verdict = INCONCLUSIVE replication" | Model B: "High confidence — taking Yin 2016 target identification at face value"}** [TRANSLATION-DISAGREEMENT — confidence-framing-only, not science direction: Model A explicitly weights the replication risk into the confidence call (comp-018 Phase 2 flagged Yin 2016 as a single-paper unreplicated anchor; Styrax egonol structurally-adjacent analogs are 3.7× weaker). Model B treats the published target-identification data as the primary input without weighting replication risk. For load-bearing downstream reasoning, Model A's Medium-confidence framing is more conservative and is the version that should propagate into the comp-039 wiki page.]

**{Model A: "negative direction (effect ≥ in carriers) — predicted by mechanism but with very wide uncertainty bands; candidate is wrong shape for UKB cross-tab anyway (Helicteres NOT dietary)" | Model B: "null direction (no differential effect)"}** [TRANSLATION-DISAGREEMENT: Same negative-vs-null pattern as the other candidates. Operational note both models implicitly agree on: Helicteres is not part of any dietary corpus tractable in UK Biobank — the candidate's CFH-classification value is more relevant to a future TCM-supplement clinical-context evaluation than to the present UKB cross-tab.]

## Disagreement notes

- **confidence framing:** Model A bounds confidence by replication risk (comp-018 Phase 2 verdict); Model B does not. Model A's framing is the appropriate one for OE's evidence-discipline rules (replication risk is a published Phase 2 finding, not informal speculation).

- **hedging — predicted Y402H direction:** Model A picks "negative"; Model B picks "null". Same logic divergence as the other candidates.

- **UKB tractability:** Model A explicitly flags Helicteres as not in any UKB-tractable dietary corpus; Model B does not. Practical implication for the UKB cross-tab: Helicteres is a deferred candidate, not a current one.

## Recommended falsification test (consensus, with priority)

**Priority 1 (load-bearing):** independent wet-lab replication of Yin 2016 CH50 9/40 μM benzofuran lignan finding on a matched assay format. This is the comp-018 Phase 2 open follow-up and must close before the CFH-dependence classification is operationally trusted.

**Priority 2 (downstream):** if replication confirms, run compound 5 (dihydrodehydrodiconiferyl alcohol, 9 μM CH50) on MSU-crystal-driven complement activation in CFH-depleted vs CFH-replete serum. Retained activity in CFH-depleted serum confirms CFH-independence.

**Priority 3 (operational):** consider whether Helicteres has a route to clinical translation at all given its non-dietary status. If the candidate is only actionable through a formulated-supplement channel, the CFH-classification is less time-critical than the supply-chain / GRAS-pathway question.
