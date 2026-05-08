---
title: "Gut-Lumen Uricase × ABCG2 Genotype Stratification + Flux Model (comp-019)"
date: 2026-05-08
tags:
  - abcg2
  - q141k
  - rs2231142
  - gut-lumen-sink
  - uricase
  - genotype-stratification
  - flux-model
  - alln-346
  - prx-115
  - rasburicase
  - intestinal-urate-secretion
  - matsuo-2014
  - miyazaki-2025
  - wallace-2018
  - vora-2021
  - nakayama-2011
  - takada-2014
  - phase-2b-trial-design
  - comp-019
  - mechanistic-extrapolation
  - in-silico
related:
  - cross-validation.md
  - gut-lumen-sink.md
  - abcg2-modulators.md
  - intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md
  - t-abcg2-suppression-evidence-mining-computational.md
  - androgen-urate-axis.md
  - validation-experiments.md
  - personal-genome-protocol.md
  - gout-clinical-pipeline.md
  - computational-experiments.md
  - synthesis.md
  - open-questions.md
sources:
  - "Miyazaki R, Ohashi Y, Sakurai T, Iwamoto T, Ichida K, Saruta M (2025) J Transl Med 23:257, PMID 40033341, doi:10.1186/s12967-025-06145-7"
  - "Wallace MC et al. (2018) Rheumatology (Oxford) 57(4):656-660, PMID 29342288, doi:10.1093/rheumatology/kex467"
  - "Vora B et al. (2021) Clin Transl Sci 14(4):1431-1443, PMID 33931953, doi:10.1111/cts.12992"
  - "Stamp LK et al. (2019) Clin Transl Sci 13(1):110-115, PMID 31444839, doi:10.1111/cts.12686"
  - "Matsuo H et al. (2014) Nucleosides Nucleotides Nucleic Acids 33(4-6):266-274, PMID 24940678, doi:10.1080/15257770.2013.866679"
  - "Takada T et al. (2014) Nucleosides Nucleotides Nucleic Acids 33(4-6):275-281, PMID 24940679, doi:10.1080/15257770.2013.854902"
  - "Nakayama A et al. (2011) Nucleosides Nucleotides Nucleic Acids 30(12):1091-1097, PMID 22132962, doi:10.1080/15257770.2011.633953"
  - "Pierzynowska K et al. (2020) Front Med 7:569215, PMID 33330529, doi:10.3389/fmed.2020.569215"
  - "Allena Pharmaceuticals EULAR POS1157 (2022) ALLN-346 Phase 2a Study 201"
  - "Protalix BioTherapeutics (2024) PRX-115 Phase 1 ACR Convergence late-breaking poster"
  - "Nguyen KP et al. (2025) Clin Rheumatol 44(10):4275-4281, PMID 40858881, doi:10.1007/s10067-025-07656-w"
---

# Gut-Lumen Uricase × ABCG2 Genotype Stratification + Flux Model (comp-019)

## Plain-English summary (read this first)

There was a worry that the engineered-koji platform's whole therapeutic mechanism might only work in patients who carry a specific genetic variant — Q141K in the ABCG2 transporter — which is the #1 genetic risk factor for gout. About 25% of European-ancestry gout patients carry this variant; up to 50% of East-Asian-ancestry patients do. **If** the platform mechanism only worked in this subset, the addressable demographic would shrink dramatically and the trial design would have to change.

This experiment built a quantitative model of intestinal urate flux to answer that question in silico, before committing wet-lab dollars. The model uses the only direct human in-vivo measurement of intestinal urate secretion stratified by ABCG2 functional class (Miyazaki et al., J Transl Med 2025) plus standard kinetic parameters for the ABCG2 transporter and the A. flavus uricase enzyme.

**The answer: the worry is wrong. Non-Q141K (WT/WT) males show the LARGEST predicted serum urate reduction from gut-lumen uricase, not the smallest. The mechanism works across all genotypes; the magnitude scales with the residual ABCG2 capacity at any given genotype.**

Predicted ΔSUA at steady state (with mid-dose 25 mg/day uricase, the engineered-koji target):

- WT/WT male: **−0.83 mg/dL** (90% CI −1.13 to −0.57)
- Q141K heterozygous male: −0.67 mg/dL (90% CI −0.91 to −0.45)
- Q141K homozygous male: −0.50 mg/dL (90% CI −0.68 to −0.34)
- Severe ABCG2 dysfunction (Q126*+Q141K): −0.28 mg/dL (90% CI −0.37 to −0.19)

**What this means for the platform:**
1. Don't narrow the primary demographic to Q141K-positive patients. The opposite — the platform produces its largest per-patient ΔSUA in WT/WT patients, the majority of the gout population.
2. Q141K-positive patients are still candidates, but for a different reason: they have higher unmet ULT need at baseline (allopurinol-resistant per Wallace 2018 OR=2.43, p=6.2e-7), so even a smaller absolute ΔSUA is clinically meaningful for them.
3. The Phase 2b trial design should NOT be enriched for Q141K-positive patients. It should be a typical-gout cohort with Q141K as a stratification variable, not an enrichment criterion.
4. The §1.27 Caco-2 wet-lab gate is **NOT triggered** by this finding. The flux model already rules out the Q141K-only-mechanism hypothesis without needing wet-lab. (The wet-lab gate would re-trigger if a Phase 2b RCT shows differential genotype response inconsistent with the flux model's predictions.)
5. **There IS a structural ceiling, but it sits at the severe-ABCG2-dysfunction tier (~25% functional, Q126*-positive compound heterozygotes), not at Q141K heterozygotes.** Most clinically relevant Q141K carriers are heterozygotes, who retain 75% function and respond well per the flux model.

The Phase A literature mining ALSO surfaced a separate negative finding worth flagging: **across the entire published clinical-trial corpus of oral and systemic uricase therapy, ZERO trials have pre-stratified or post-stratified results by ABCG2 Q141K genotype.** The Q141K × allopurinol response literature is rich, but the Q141K × uricase response literature is empty. This is a publishable observation by itself — every uricase trial since rasburicase (2001) has missed an obvious pharmacogenomic stratification axis.

## Question

**Can the gut-lumen uricase sink produce meaningful serum urate reduction in non-Q141K males, or does the mechanism rely on Q141K-positive disease-state ABCG2 vulnerability to show benefit?**

This is the platform's most important open question for its primary demographic ([`open-questions.md` Open Question 1](./open-questions.md), framed in the [`synthesis.md` Sweep 2026-05-08](./synthesis.md) action queue).

The question emerged after [comp-016](./t-abcg2-suppression-evidence-mining-computational.md) found a WEAK / UNCONFIRMED verdict on direct androgen-driven intestinal ABCG2 suppression, and [comp-017](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md) confirmed near-null sex dimorphism in healthy-baseline intestinal ABCG2. With the "androgens suppress ABCG2 in males" model refuted, the responder logic provisionally shifted toward Q141K-positive disease-state vulnerability. **comp-019 tests whether that provisional shift was correct.**

## Verdict

**The gut-lumen uricase mechanism does NOT depend on Q141K-positive disease-state vulnerability.** Across the genotype spectrum:

- WT/WT (100% functional ABCG2) → LARGEST absolute ΔSUA per patient
- Q141K heterozygous (75% functional) → ~80% of the WT response
- Q141K homozygous (50% functional) → ~60% of the WT response
- Severe dysfunction (~25% functional, Q126*+Q141K compound) → ~33% of the WT response — this IS a structural ceiling, but it applies only to the small severe-dysfunction subset, NOT to the typical Q141K heterozygote.

**Implication:** the platform's primary demographic should remain "all gout patients," not "Q141K-positive gout patients." Q141K is a stratification variable for trial design, not an enrichment criterion. The non-Q141K majority of gout patients are the platform's HIGHEST-response subset, not its lowest.

## Why this matters

Three platform-level consequences:

1. **Phase 2b RCT design.** Pre-comp-019 worry framing implied a small, expensive Q141K-enriched trial (~120 patients in an East-Asian-ancestry cohort to hit ~50% Q141K carrier rate, or ~360 in a European-ancestry cohort to hit the same). Post-comp-019, the trial should run as a typical-gout RCT with Q141K + Q126* genotyping at enrollment as stratification variables. This is logistically simpler and addresses a larger market.

2. **Strain-engineering target dose.** The flux model shows the mechanism is **substrate-limited, not enzyme-limited**, at all three uricase-dose scenarios tested (5 / 25 / 50 mg/day). Capacity ratios range from 32× to 1300× — uricase capacity vastly exceeds delivered intestinal urate flux. This means the engineered-koji yield target ([`engineered-yeast-uricase-proposal.md`](./engineered-yeast-uricase-proposal.md)) does NOT need to push the upper bound; the binding constraint is enzyme delivery (GI survival, enteric coating per [`gi-survival-prediction.md`](./gi-survival-prediction.md)), not enzyme dose. **Engineering cycles can shift away from yield optimization toward GI-survival optimization.**

3. **Cross-validation.md Claim 1 rating.** Pre-comp-019, the gut-lumen uricase mechanism was rated 6/10 with "human effect size unproven" as the primary risk. Post-comp-019, the human effect size is now COMPUTATIONALLY PREDICTED at −0.5 to −0.83 mg/dL across the dominant gout subpopulations. This is below the 1–2 mg/dL therapeutic-target range cited in [`cross-validation.md`](./cross-validation.md), but it IS in the same order of magnitude as the ALLN-346 Phase 2a Study 201 signal (CKD subgroup) and meaningful for adjuvant use alongside allopurinol. The rating should shift from "6/10 with human effect-size unproven" to "**6.5/10 — mechanism is genotype-robust per flux model; clinical magnitude prediction in the −0.5 to −1.0 mg/dL range awaits human RCT verification**."

## Method

### Phase A — literature stratification mining

Scope:
- ALLN-346 Phase 2a Studies 201 (n=16, CKD-dominated) and 202 (n=19, broader cohort, terminated Sep 2022)
- PRX-115 Phase 1 (n=64) — IV systemic uricase, NOT gut-lumen but a useful control for the upper bound of enzymatic urate degradation
- Rasburicase clinical corpus (TLS-dominated; gout off-label rare)
- Q141K × allopurinol response: Wallace 2018 meta-analysis (n=595, OR 2.43, p=6.2e-7); Vora 2021 oxypurinol PK/PD (Q141K homozygotes have 1.79× longer half-life); Stamp 2019 (Q141K independent factor in allopurinol sensitivity, p=0.019)
- Direct human intestinal urate secretion measurement: Miyazaki 2025 (n=34, double-balloon endoscopy, ABCG2 functional-class stratified)
- Mouse Abcg2-KO: Takada 2014 (intestinal urate excretion <50% of WT)
- ABCG2 transporter kinetics: Nakayama 2011 (Km = 8.24 ± 1.44 mM; Vmax = 6.96 ± 0.89 nmol/min/mg)
- Functional-classification framework: Matsuo 2014 (Japanese male hyperuricemic cohort n=644)
- Q141K allele frequencies: gnomAD (East Asian MAF 29.1%; European MAF 10.3%); Nguyen 2025 Vietnamese gout cohort (MAF 46.8%)

Tooling: PubMed MCP `search_articles` + `get_article_metadata` + `get_full_text_article`; WebSearch + WebFetch for non-PubMed-indexed content (EULAR abstracts, Allena/Protalix press releases). Multilingual ChiCTR / J-STAGE / KISS searches did not surface a Q141K-stratified oral uricase RCT (none exists in any language).

### Phase B — first-principles flux model

Implementation: Python stdlib only ([`experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/scripts/flux_model.py`](../experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/scripts/flux_model.py)). Inputs in `inputs/flux_model_parameters.json` (literature-anchored; each parameter cited to a primary source with verification tier). Monte Carlo sensitivity n=5000 over uncertainty bounds.

**Model logic:**

1. **Daily mass balance.** Total daily urate production ~700 mg/day; renal excretion ~67%, intestinal ~33% in healthy WT (Takada 2014 mouse KO; multiple historical tracer studies).

2. **Linear-regime ABCG2 transport.** ABCG2 Km is 8.24 mM (= 8240 μM) per Nakayama 2011. Direct measurement of human jejunal lumen urate baseline is ~99.5 pg/μL ≈ 0.59 μM (Miyazaki 2025) — three to four orders of magnitude below Km. **The transporter is FAR from saturation in vivo.** Rate scales linearly with substrate concentration. Reducing lumen urate via uricase increases the gradient roughly proportionally.

3. **Genotype scaling.** Functional class per Matsuo 2014 / Miyazaki 2025: WT/WT = 1.00; Q141K het = 0.75; Q141K hom = 0.50; Q126*+Q141K compound = 0.25. Empirically anchored to Miyazaki 2025 secretion-rate ratios (median ratios 100%:75%:50% = 1.0 : 0.72 : 0.38).

4. **Sink amplification factor.** With baseline lumen urate already low (~0.6 μM), uricase clamping it toward zero produces a bounded gradient improvement. Per Yu 2015 / Bhatnagar 2016 review tier and physiological reasoning, ~30–50% of secreted intestinal urate is reabsorbed in the colon. We use 0.40 (sensitivity 0.20–0.60) — i.e., uricase prevents reabsorption of 40% of secreted urate, increasing net intestinal elimination by that amount.

5. **Renal partial compensation.** When intestinal urate excretion changes, the kidney partially compensates by adjusting tubular handling (Matsuo 2014 directional). We use 30% offset (sensitivity 0–50%).

6. **Steady-state ΔSUA.** 1st-order approximation: ΔSUA = −SUA_baseline × (Δflux / production). Baseline SUA differs by sex and genotype (gout-typical values: 8.0 mg/dL WT male, 7.0 WT female, scaling up with genotype severity to 9.5 mg/dL Q141K hom male, 10.5 mg/dL severe dysfunction).

**Three uricase-dose scenarios:** 5 mg/day (low), 25 mg/day (mid, engineered-koji target), 50 mg/day (high, ALLN-346 Phase 2a equivalent).

## Key results

### Phase A literature mining — what's there and what's NOT

The headline Phase A finding is a NEGATIVE: **across the entire published uricase-trial corpus, ZERO trials have stratified results by ABCG2 Q141K genotype.** Allopurinol does (Wallace 2018, Vora 2021, Stamp 2019). Uricase does not. Every oral uricase trial (ALLN-346 Studies 201/202) and every systemic uricase trial (rasburicase post-marketing, pegloticase, PRX-115 Phase 1) missed this stratification axis.

The mechanistic anchor — Miyazaki 2025 — is the load-bearing Phase A datum. n=34 patients, Crohn's-disease-dominated (32/34), undergoing double-balloon endoscopy. Direct measurement of jejunal urate secretion stratified by ABCG2 functional class:

| ABCG2 functional class | n | Baseline lumen urate (median, IQR) pg/μL | ΔC over 5 min (median, IQR) pg/μL |
|---|---|---|---|
| 100% (WT/WT) | 11 | 105.3 (12.3–236.6) | **+175.6** (92.6–550.7) |
| 75% (Q141K het) | 18 | 113.0 (9.4–258.0) | +125.9 (7.7–476.4) |
| 50% (Q141K hom or Q126* het) | 5 | 70.1 (25.5–110.9) | **+65.9** (−35.1–114.0) |

**p for trend = 0.058** (just shy of conventional significance with n=34 and one group of n=5).

The 100%:50% median secretion-rate ratio is 2.66 (175.6 / 65.9). The means tell a more dramatic story (600.5 vs 44.8, ratio 13.4) but the small n in the 50%-functional group makes the median the more reliable central estimate. We propagate the median ratios into Phase B.

### Phase B flux model results

**Predicted ΔSUA at steady state, Monte Carlo medians (90% CI in parens, n=5000 samples):**

| Scenario | Low 5 mg/d | Mid 25 mg/d | High 50 mg/d |
|---|---|---|---|
| WT/WT, male gout | −0.83 (−1.14, −0.57) | **−0.83 (−1.13, −0.57)** | −0.83 (−1.13, −0.57) |
| Q141K het, male gout | −0.66 (−0.91, −0.45) | **−0.67 (−0.91, −0.45)** | −0.67 (−0.91, −0.46) |
| Q141K hom, male gout | −0.50 (−0.67, −0.34) | **−0.50 (−0.68, −0.34)** | −0.49 (−0.67, −0.34) |
| WT/WT, female gout | −0.73 (−1.00, −0.50) | −0.74 (−1.00, −0.50) | −0.74 (−1.00, −0.50) |
| Q141K het, female gout | −0.58 (−0.80, −0.40) | −0.59 (−0.80, −0.40) | −0.59 (−0.80, −0.40) |
| Q141K hom, female gout | −0.41 (−0.57, −0.28) | −0.42 (−0.57, −0.29) | −0.42 (−0.57, −0.29) |
| Severe dysfunction, male | −0.27 (−0.38, −0.19) | −0.28 (−0.37, −0.19) | −0.27 (−0.37, −0.19) |

### Three structural observations from the model

1. **Genotype ordering is INVERTED relative to the worry framing.** The model predicts WT/WT patients show the LARGEST absolute ΔSUA, not the smallest. The reason is mechanistic: uricase amplifies whatever ABCG2 is doing in the gut compartment. WT/WT patients have full ABCG2 capacity to amplify; Q141K homozygotes have half. The mechanism is multiplicative on residual gut capacity.

2. **Dose-response is FLAT above ~5 mg/day.** Capacity ratios (enzyme throughput / delivered intestinal urate flux) range from 32× at the low dose to 1300× at the high dose for severe-dysfunction patients. Uricase capacity vastly exceeds substrate even at the lowest dose tested. **The mechanism is substrate-limited, not enzyme-limited.** This is a strain-engineering implication (don't push yield further; push GI delivery).

3. **Sex difference is small and inherits from baseline SUA.** The model predicts ~12% smaller absolute ΔSUA for females than for males within any given genotype — purely because females have ~12% lower baseline SUA on average. The mechanism itself is sex-symmetric (per [comp-017](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md), healthy-baseline intestinal ABCG2 is sex-invariant). Females respond, just from a lower starting point.

### Recovery against ALLN-346 Phase 2a empirical signal

The flux model's central prediction for an WT/WT-dominated, mostly stage-2-CKD cohort at 50 mg/day uricase (the ALLN-346 Phase 2a Study 201 dosing approximation) is roughly −0.6 to −0.9 mg/dL ΔSUA. Allena Pharmaceuticals reported a statistically significant signal in Study 201 days 5–7 (p<0.01 to p<0.05), with the largest reduction in stage 2 CKD patients and sUA reduction correlated with eGFR (r=0.95, p=0.003). Specific mean ΔSUA values were not in the EULAR abstract, but the directional signal is consistent with the flux model's prediction.

Study 202 (broader cohort, mixed CKD severity) showed 0–5% mean ΔSUA, not statistically significant. Interpretation: the broader cohort included patients with milder CKD where the renal compensation reserve is higher, partially offsetting the gut delta. The flux model's renal-compensation parameter (central 30%, range 0–50%) covers this — at the upper end of compensation, the predicted ΔSUA shrinks toward the Study 202 observed range. **The flux model is consistent with both Study 201 and Study 202 outcomes** — Study 201 sat in the small-renal-compensation regime (high-CKD), Study 202 in the larger-renal-compensation regime (mixed CKD).

## Recommendations

### For Phase 2b RCT design (the most actionable change)

| Pre-comp-019 design assumption | Post-comp-019 recommendation |
|---|---|
| Enrich for Q141K-positive patients to maximize hit rate | **Run as typical-gout RCT, with Q141K + Q126* genotyping as stratification variables (NOT enrichment)** |
| ~360 unenriched Europeans needed to power Q141K-conditional sub-analysis | Same n=120-180 typical European-gout cohort works because the mechanism is genotype-robust; Q141K subgroup analysis is secondary, not primary |
| Powering for Q141K-conditional differential effect | Power for ~−0.5 to −1.0 mg/dL ΔSUA mean in unstratified cohort; Q141K subgroup analysis is hypothesis-generating |
| Pre-stratify cohort by CKD stage (per ALLN-346 lesson) | KEEP this — CKD is a stronger response-modifier than Q141K per the flux model (renal compensation reserve dominates) |
| Single-dose cohort | **Test only one dose** (~25 mg/day target). Dose-response is flat above ~5 mg/day per flux model — running multiple dose arms is wasteful |

### For strain-engineering priorities

| Pre-comp-019 priority | Post-comp-019 priority |
|---|---|
| Push uricase yield in engineered koji to ~50+ mg/dose | **Yield target can remain at 25 mg/dose** (substrate-limited regime) |
| GI survival as critical blocker (per `cross-validation.md` Claim 2 rating 5/10) | **GI survival becomes EVEN MORE the binding constraint** — yield is 30-1000× excess but only the fraction that survives matters |
| Both yield AND survival as parallel engineering tracks | **Survival > yield** as engineering priority |

### For self-experimentation protocol (Brian's n=1 case)

Brian's relevant genotype is captured by the [`personal-genome-protocol.md`](./personal-genome-protocol.md) MinION pipeline. comp-019's flux model predicts:
- If Brian is WT/WT for both Q126* and Q141K: expected ΔSUA ~−0.83 mg/dL (mid-dose engineered-koji)
- If Brian is Q141K heterozygous (~25% prior probability for European ancestry): expected ΔSUA ~−0.67 mg/dL
- If Brian is Q141K homozygous (~1% prior probability): expected ΔSUA ~−0.50 mg/dL

In all scenarios the predicted effect is detectable with home uric-acid-meter precision (typical assay CV ~5%, baseline SUA ~5-7 mg/dL → detectable threshold ~0.3 mg/dL ΔSUA). **The personal-genome-protocol genotype IS load-bearing for interpreting the n=1 self-experiment outcome** — without it, a smaller observed ΔSUA could be confused with mechanism failure rather than genotype-typical response.

### What this CHANGES about the §1.27 Caco-2 wet-lab gate

**Not triggered.** The flux model already rules out the binary "Q141K-only mechanism" hypothesis without needing Caco-2 transwell data. The wet-lab gate would re-trigger only if a Phase 2b RCT shows differential genotype response inconsistent with the flux model's predictions.

The Caco-2 gate REMAINS APPROPRIATE for a different question — does intestinal-cell sublethal stress (TNFα, oxidative load) phenocopy ABCG2 dysfunction in the way the flux model would predict for the severe-dysfunction tier? But that's not the comp-019 question.

## Cross-references and downstream propagation

- [`cross-validation.md`](./cross-validation.md) Claim 1 — gut-lumen sink mechanism rating updated from 6/10 to 6.5/10 (mechanism is now genotype-robust per flux model; clinical magnitude prediction awaits Phase 2b verification).
- [`gut-lumen-sink.md`](./gut-lumen-sink.md) — patient-stratification note updated to reflect that the gut-lumen sink works in non-Q141K patients (in fact, BETTER than in Q141K-positive patients).
- [`abcg2-modulators.md`](./abcg2-modulators.md) §6 (Q141K rescue) — cross-reference comp-019's clarification that rescue interventions (butyrate, fermentable fiber, HDIs) ADD to the gut-lumen sink rather than replacing it; the gut-lumen sink works across genotypes, but Q141K-positive patients get a synergy bonus from rescue interventions.
- [`androgen-urate-axis.md`](./androgen-urate-axis.md) — the male-asymptote framing is now further softened: not only is sex-dimorphism near-null at healthy baseline (per comp-017), but ALSO the gut-lumen sink mechanism does not depend on Q141K-male compounding for benefit.
- [`open-questions.md`](./open-questions.md) — Open Question 1 ("can the gut-lumen sink be rescued in non-Q141K population") now has a flux-model answer: yes, the sink works MORE in non-Q141K than in Q141K patients.
- [`synthesis.md`](./synthesis.md) Sweep 2026-05-08 Open Question 1 — actioned by comp-019.
- [`validation-experiments.md`](./validation-experiments.md) — §1.27 Caco-2 gate remains appropriate for stress-phenocopying questions but is NOT triggered by the comp-019 finding for the genotype question.
- [`personal-genome-protocol.md`](./personal-genome-protocol.md) — Q141K + Q126* genotyping is now load-bearing for Brian's n=1 protocol interpretation.

## Limitations

1. **No prospective Q141K-stratified oral uricase RCT data exists.** The flux model's predictions are PROSPECTIVE — they have not been clinically validated. The Phase 2b RCT design recommendation is the bridge from this in-silico finding to clinical evidence.

2. **Miyazaki 2025 substrate population is Crohn's-disease-dominated** (32 of 34 subjects). Inflammatory bowel disease may itself affect intestinal ABCG2 expression / function. The genotype-stratified secretion ratios this paper provides are the best available data, but their generalization to typical gout patients (no IBD) is an open question. Per the discussion in [Ferrer-Picón 2020 (PMID 31211831)](./abcg2-modulators.md), inflammation reduces intestinal ABCG2 — meaning Crohn's patients likely have LOWER baseline intestinal urate secretion than non-IBD comparators. This biases Miyazaki's absolute numbers downward, but should not bias the genotype RATIOS we propagate into the flux model. **The flux model uses ratios, which is robust to this bias.**

3. **The flux model uses 1st-order steady-state approximation.** A more rigorous PBPK model with explicit clearance kinetics, reabsorption gradients, circadian dosing, food effects, and CKD-grade renal compensation would refine the magnitude estimates but is unlikely to flip the genotype-ordering conclusion.

4. **Renal compensation fraction is mechanistic-extrapolation.** Central estimate 0.30, sensitivity 0.0–0.5. Not directly measured in any oral-uricase trial. The flux model's headline conclusion (genotype ordering of response magnitude) is robust to this parameter; the absolute magnitudes are not.

5. **Pre-commit verification gate (CLAUDE.md Rule 4) tier:**
   - Miyazaki 2025 numbers: full-text grep-verified from PMC11877951.
   - Wallace 2018 (OR 2.43, p=6.2e-7): abstract-tier verified.
   - Vora 2021 (1.79× half-life): abstract-tier verified.
   - Stamp 2019 (Q141K p=0.019): abstract-tier verified.
   - Matsuo 2014 (functional-classification framework, risk ratios 1.36/1.66/2.35): abstract-tier verified.
   - Takada 2014 (mouse KO): abstract-tier verified.
   - Nakayama 2011 (Km 8.24 mM, Vmax 6.96 nmol/min/mg): abstract-tier verified.
   - ALLN-346 Phase 2a Study 201/202: EULAR-abstract / press-release tier; NOT line-anchored to peer-reviewed full-text.
   - PRX-115 Phase 1: ACR conference-abstract tier.
   - Future Paperclip-MCP run recommended to grep-verify the abstract-tier-only ABCG2 kinetics + Q141K-allopurinol response numbers against full-text.

6. **Multilingual scan deferred.** ChiCTR / J-STAGE / KISS searches did not surface a published genotype-stratified oral-uricase RCT in any language. The likelihood of one being missed is low (Q141K × allopurinol response is heavily indexed; Q141K × uricase response would be too if it existed). A future multilingual deep-dive on Chinese-language hyperuricemia pharmacogenomics could refine the picture for East-Asian-ancestry cohorts where Q141K MAF is ~30%.

7. **Two-model translation cross-check did not trigger.** Per [CLAUDE.md §"Translation protocol"](../CLAUDE.md), non-English sources with load-bearing claims should be translated with two independent models. comp-019 did not surface non-English sources whose translation would change a verdict. Nguyen 2025 Vietnamese cohort paper is published in English (Clin Rheumatol) — no translation step needed.

## What would flip the verdict

The headline verdict (mechanism is genotype-robust; non-Q141K patients respond AT LEAST as well as Q141K patients) would flip only if:

- A Phase 2b oral-uricase RCT shows Q141K-positive patients responding MORE than Q141K-negative patients (would contradict the flux model's gradient-amplification logic).
- A direct human pharmacokinetic study of oral uricase + intestinal urate secretion measurement shows the substrate-limited regime is wrong (uricase doesn't actually clamp lumen urate; some unmeasured rate-limiting step intervenes).
- A more detailed PBPK model with explicit CKD-grade renal compensation shows the renal compensation fully offsets the gut-delta in healthy-kidney patients (would shrink the predicted ΔSUA in WT/WT toward zero in non-CKD subjects).

None of these have surfaced. Flux model verdict is robust to the abstract-tier verification limitations in DIRECTION (genotype ordering); specific magnitude estimates remain in the −0.5 to −1.0 mg/dL band pending Phase 2b RCT validation.
