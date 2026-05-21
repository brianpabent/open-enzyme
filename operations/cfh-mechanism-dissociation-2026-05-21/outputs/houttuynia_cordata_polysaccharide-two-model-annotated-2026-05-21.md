# Houttuynia cordata polysaccharide (HCP / HCPM / CHCP) — Two-model annotated cross-check

**Date:** 2026-05-21
**Protocol:** Two independent models, inline disagreement annotation per Open Enzyme CLAUDE.md §"Translation protocol".

- **Model A:** Claude Opus 4.7 — see `houttuynia_cordata_polysaccharide-source-read-2026-05-21.md`
- **Model B:** DeepSeek (`deepseek/deepseek-chat-v3`, native-Chinese-trained) — see `houttuynia_cordata_polysaccharide-deepseek-counterread-2026-05-21.json`

## Classification consensus

Both models classify HCP/CHCP as **CFH-INDEPENDENT** (Model A: High confidence; Model B: High confidence).

The Lu 2018 (PMC5925397) depletion-rescue data is the load-bearing anchor: CHCP blocks at C3 (rescue only 9.29%) and C4 (rescue only 12.34%), with partial C5 effect (rescue 44.54%). C1q, C2, C9 are NOT primary targets (rescue 67-73%). C4 binding specifically is mechanistically incompatible with CFH-dependence — CFH is AP-specific and does not regulate C4.

## Annotated cross-check

CHCP's anti-complementary mechanism (Lu 2018) targets **C3 and C4 with partial C5 activity**, with C3 and C4 being the dominant nodes. {Model A: "C4 specificity is mechanistically incompatible with CFH-dependence — CFH does not regulate the classical pathway's C4-axis" | Model B: "Polysaccharide's action is adsorptive surface contact, distinct from CFH's CCP-fold protein recognition"} — both routes converge on the same conclusion. **No TRANSLATION-DISAGREEMENT here; the framings are complementary, not contradictory.**

The Xu 2015 (PMC7127486) full text confirms in-vivo translation: HCP at 40, 80, 160 mg/kg PO reduces C3d deposition in LPS-ALI lung tissue, reduces TLR4 expression, suppresses C5a-induced macrophage chemotaxis, and reduces NLRP3-axis cytokines (IL-1β, TNF-α, IL-6). Both models accept the multi-target picture (complement + TLR4 + NLRP3 axis).

The TLR4-MD2 docking model (Yu 2026 PMC12937656) adds an explicitly CP1-level (TLR-priming) mechanism that bypasses complement entirely. {Model A: "entirely orthogonal to complement and CFH — represents a separate CP1 chokepoint where HCP could be effective regardless of CFH status" | Model B: does not raise this as a separate consideration} — Model A's reasoning is foregrounded by the dual-CP0+CP1 framing in comp-018 Phase 2; Model B treats it implicitly through the broader "polysaccharide multi-target" framing. No science disagreement.

**{Model A: "negative direction, possibly notably greater in carriers — dual chokepoint should compound benefit in Y402H carriers where both CP0 (complement) and CP1 (TLR4 priming) axes can be more dysregulated" | Model B: "null direction (no differential effect)"}** [TRANSLATION-DISAGREEMENT: Same negative-vs-null disagreement pattern as the other candidates. Model A's HCP-specific reasoning is that the dual-chokepoint (CP0 + CP1) should especially benefit carriers with elevated CRP and complement priming baseline. Model B reserves judgement. Both reject the AMD-paradox direction (+ harm in carriers). For UKB cross-tab, both predictions need separate falsification thresholds — but note that Houttuynia is rare in UK Biobank dietary corpus; the cross-tab is more tractable in a Chinese / Vietnamese / Korean / Japanese cohort.]

## Disagreement notes

- **dual-chokepoint framing:** Model A raises Houttuynia's CP0 + CP1 dual mechanism as a candidate-specific reason for *amplified* effect in Y402H carriers; Model B does not. Operational implication: the UKB-equivalent cross-tab for HCP should ideally have an intermediate-phenotype readout (e.g., baseline CRP, IL-1β) to distinguish whether the carrier-amplified-benefit comes from the complement-mode or the TLR4-mode or both.

- **hedging — predicted Y402H direction:** Model A picks "negative, possibly notably greater"; Model B picks "null". Same logic divergence as the other candidates.

- **mechanism-class framing:** Model A explicitly notes C4 specificity is mechanistically incompatible with CFH-dependence; Model B notes polysaccharide structural mode is distinct from CFH-CCP recognition. **These are different routes to the same High-confidence call** — Model A's framing is more falsifiable (C4 specificity is a check-able prediction), Model B's framing is more structurally cautious. Both are appropriate.

## Recommended falsification test (consensus)

CHCP / HCP-1 on MSU-crystal-driven complement activation in (i) CFH-depleted serum, (ii) Factor B-depleted serum, (iii) C4-depleted serum. The C4-depletion arm specifically tests the classical-pathway-CFH-independent prediction: if HCP retains activity in C4-depleted serum, the classical-pathway mechanism is not the only mode; if HCP loses activity in C4-depleted serum, the classical-pathway mechanism is dominant and the CFH-independence call is bullet-proofed.

Additionally, for the UKB-equivalent cross-tab: the cohort needs Houttuynia / fish-mint / 鱼腥草 / どくだみ / diếp cá dietary exposure data, which is best captured in Asian cohorts (Korean Genome Epidemiology Study, China Kadoorie Biobank, Singapore Chinese Health Study). UK Biobank's Oxford WebQ is unlikely to capture Houttuynia consumption at adequate frequency.
