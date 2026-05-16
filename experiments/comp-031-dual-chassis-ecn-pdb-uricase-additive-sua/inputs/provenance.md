# Inputs provenance — comp-031

All parameters in `model_parameters.json` are literature-anchored. This document records source, fetch method, and verification tier for each input. Stdlib-only Python; no external dependencies.

## CBT2.0 / PDB-pathway empirical anchor

**Li et al. 2025 — Life Metabolism 4(6):loaf031. PMID 41070194.** "A reductive uric acid degradation pathway in anaerobic bacteria." Defines CBT2.0 (engineered *E. coli* Nissle expressing the 2,8-dioxopurine cluster). Reported: **plasma UA 463 → 172 μmol/L over 6 weeks in hyperuricemic mice (−63%)**. Verification tier: corpus-tier (cited in `wiki/purine-degrading-bacteria.md` lines 30, 284, 311). Not full-text grep-verified against original PDF — use as anchor magnitude with ±50% uncertainty band.

**Liu et al. 2023 — Cell 186(16):3400–3413. PMID 37541197.** Establishes 8-gene PDB cluster, screening data: 59/240 isolates consumed >50% uric acid after 48h anaerobic culture. DOPDH selenium-dependent variant ~412 s⁻¹ turnover (vs. sulfur-dependent bovine XOR ~15 s⁻¹). Verification tier: corpus-tier (`wiki/purine-degrading-bacteria.md` line 83).

**Liu, Zhou, Jarman et al. 2025 — Nature Microbiology 10(9):2291–2305. PMID 40770490.** Full pathway biochemistry. 2,102 MAGs from 1,350 taxa harbor the cluster. Verification tier: corpus-tier.

## Uricase kinetic priors

Inherits from comp-019 `inputs/flux_model_parameters.json`. Anchor:
- **Km_uricase ≈ 25 μM** (Sanofi rasburicase label; range 5–100 μM across assay conditions).
- **Specific activity 8.3 U/mg** (1 U = 1 μmol urate/min at pH 8.5, 37°C). Effective in colonic pH 7–8: ~75% of label value = **6 U/mg in vivo central estimate**.
- **ALLN-346** (Allena Phase 2a): engineered *C. utilis* uricase, ~50 mg/day dosing in CKD subgroup. Validates that gut-lumen uricase reduces SUA in a clinically detectable range (statistically significant in Study 201 CKD subgroup, days 5–7).
- **PULSE probiotic** (Cell Reports Medicine, Oct 2025): engineered EcN with HucR-driven uricase expression. Reduced persistent hyperuricemia in mice/rats.
- **comp-019 prediction:** mid-dose 25 mg/day uricase → ΔSUA −0.83 mg/dL (WT/WT male gout, 90% CI −1.13 to −0.57), −0.67 mg/dL (Q141K het), −0.50 mg/dL (Q141K hom). Mechanism substrate-limited at all tested doses.

## Luminal urate concentration

**Miyazaki et al. 2025 — J Transl Med 23:257, PMID 40033341, PMC11877951.** Double-balloon endoscopy direct human jejunal urate measurement, n=34. Baseline jejunal urate **0.59 μM (median, IQR 0.06–1.16)**. Verification tier: direct grep-verified from full-text PMC (per comp-019 inputs).

**Post-meal / colonic upper bound:** Brian's brief specifies 50–500 μM range to test. The 500 μM upper bound is post-fructose / high-purine-meal physiological spike (post-meal jejunal/ileal); colonic concentrations are typically lower due to dilution and reabsorption. The model bounds the sensitivity sweep over 1 μM → 500 μM to capture all physiologically plausible regimes.

## Butyrate flux from PDB pathway

**Stoichiometric ceiling.** Per Liu 2023 pathway: pyruvate → fermentation → acetate + butyrate. Bacterial purinolytic fermentation of *Clostridium sporogenes* produces approximately **0.5–0.7 mol butyrate per mol uric acid degraded** (estimated from the bicarbonate / 8-carbon stoichiometry; partition between acetate and butyrate is strain-dependent and roughly 1:1 at the molar level for full pathway). Use **0.5 mol butyrate / mol urate** as a conservative central estimate. Verification tier: mechanistic extrapolation from pathway stoichiometry.

**Net butyrate yield from PDB at expected luminal urate flux** is fundamentally bounded by the urate substrate flux. **Independent of CBT2.0 colonization density.** If only ~200–300 mg/day of urate enters the colonic lumen (humans secrete ~33% of 700 mg/day daily production through the gut, ~233 mg/day), and PDB consumes some fraction of that, the maximum butyrate yield is in the low-millimolar-pulse range, NOT sustained mM concentrations across the entire colon.

**Background colonic butyrate** (high-fiber diet): 5–20 mM luminal, ~0.5–2 mM at the epithelial surface (per `wiki/purine-degrading-bacteria.md` line 232 "Concentration gap" framing). PDB-pathway butyrate is **additive on top of this background**.

## CBT2.0 colonization density

**Sensitivity range:** 10⁸–10¹¹ CFU/g intestinal content. Brian's brief specifies 10⁹–10¹¹. Standard engineered probiotic colonization is 10⁷–10⁹ CFU/g for transit organisms; engineered LBP can transiently reach 10¹⁰–10¹¹ with adequate dosing. Use central 10¹⁰ CFU/g.

## Basseville 2012 HDAC threshold

**Basseville et al. 2012 — Cancer Res, PMID 22472121.** HDAC-mediated Q141K ABCG2 trafficking rescue demonstrated at **1–5 mM butyrate in cell culture**. Verification tier: corpus-tier (`wiki/abcg2-modulators.md` line 198, `wiki/purine-degrading-bacteria.md` line 232).

**Concentration gap caveat:** rescue mechanism is in vitro at 1–5 mM applied directly to cells. In vivo enterocyte-nucleus concentrations after the mucus + epithelial gradient drop may be an order of magnitude lower than luminal. Model uses a Hill-function activation curve with EC50 = 1 mM (in vitro Basseville threshold), n = 2 (cooperative HDAC inhibition typical), and an in-vivo crypt-attenuation factor (central 0.1, range 0.05–0.5) mapping luminal to crypt concentration. The Hill function gives fractional Q141K trafficking rescue (0–1) — the model multiplies this by Q141K-positive residual ABCG2 capacity to get rescued substrate flux.

## Daily mass balance constants

Inherited from comp-019:
- Total daily urate production: 700 mg/day (range 600–900).
- Renal excretion fraction (normal kidney): 0.67 (range 0.60–0.70).
- Intestinal excretion fraction: 0.33 (range 0.30–0.40).
- Total miscible urate pool (gout): 1200 mg.
- Renal compensation fraction (when intestinal flux changes): 0.30 (range 0.0–0.50).
- SUA conversion: 1 mg/dL = 59.48 μM.
- Typical gout SUA baseline: 8.0 mg/dL (male), 7.0 mg/dL (female).

## Fetch metadata

- Fetch date: 2026-05-16.
- All numbers either inherit from comp-019 inputs (already verified) or are corpus-tier from `wiki/purine-degrading-bacteria.md` (which carries Pass 3 sweep review).
- Pre-commit grep-verify gate per CLAUDE.md Rule 4: load-bearing numbers (CBT2.0 −63%, Basseville 1–5 mM, Miyazaki 0.59 μM, Nakayama Km 8.24 mM, rasburicase 8.3 U/mg) were grep-verified against `wiki/purine-degrading-bacteria.md` (lines 284, 232, 30) and comp-019 `inputs/flux_model_parameters.json` (lines 70, 88, 30) before this file was authored.
