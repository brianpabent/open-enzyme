---
title: "Testosterone × Intestinal ABCG2 Suppression — Evidence Mining (comp-016)"
date: 2026-05-07
tags:
  - androgens
  - testosterone
  - abcg2
  - intestinal-urate-secretion
  - sex-differences
  - gut-lumen-sink
  - q141k
  - estradiol
  - platform-thesis
  - verification-gate
  - literature-mining
related:
  - androgen-urate-axis.md
  - abcg2-modulators.md
  - gut-lumen-sink.md
  - cross-validation.md
  - koji-endgame-strain.md
  - computational-experiments.md
  - manual-literature-mining.md
sources:
  - Hoque KM et al. Nature Communications (2020) PMID 32488095
  - Sakamoto et al. PLOS One (2018) PMID 30557349
  - Yu et al. Nutrition & Metabolism (2021) PMID 34144706
  - Klyushova et al. Biochemistry (Moscow) (2023) DOI 10.1134/S1990747823050100
  - Jeong et al. Biochim Biophys Acta (2015) PMID 25615818
  - MacLean et al. JPET (2008) PMID 18378562
  - Halperin Kuhns & Woodward IJMS (2020) PMID 32560040
---

# Testosterone × Intestinal ABCG2 Suppression — Evidence Mining (comp-016)

## Question

Does primary literature support the load-bearing claim in [`androgen-urate-axis.md`](./androgen-urate-axis.md) §"Why this matters for the platform" that *androgens directly suppress intestinal ABCG2 expression* at magnitudes consistent with a *structural ceiling on the gut-lumen-sink platform efficacy in male/androgen-dominant patients*?

## Verdict

**WEAK / UNCONFIRMED (provisional — abstract-level scan only; full-text grep-verification pending).**

Of 17 curated primary sources from a focused PubMed scan (2026-05-07), **zero** primary studies demonstrate androgen-driven intestinal ABCG2 suppression directly. No castration-restoration study exists; no testosterone-administration study shows decreased intestinal ABCG2 mRNA or protein in vivo; no published cohort reports increased intestinal ABCG2 protein after androgen ablation. The intestinal compartment IS sex-dimorphic in a urate-relevant way (Hoque 2020 Nature Communications — male Q140K mice show 88% intestinal ABCG2 protein loss + severe hyperuricemia; female Q140K mice are protected), but the mechanistic driver appears to be **estradiol POSITIVE on the female side** (Yu 2021 — estradiol upregulates intestinal ABCG2 via PI3K/Akt) **rather than androgen NEGATIVE on the male side**. One primary study directly contradicts the platform thesis at the in vitro intestinal level (Klyushova 2023 — testosterone INDUCES ABCG2 in Caco-2). One study found NO baseline sex difference in healthy rat intestinal ABCG2 across all four segments (MacLean 2008).

This is the verdict-tier the [`manual-literature-mining.md`](./manual-literature-mining.md) §"Pre-commit verification gate" rule was written for: a load-bearing claim that the primary literature does not directly support, propagated across multiple wiki pages on the strength of summary-tier reasoning.

## Why this matters

The Open Enzyme platform thesis depends on the structural-ceiling argument in two places:

1. **`androgen-urate-axis.md` §"Why this matters for the platform"** says: *"androgen-driven ABCG2 suppression hits the gut-lumen-sink pathway directly... structural ceiling on platform efficacy in the primary demographic."* This is the load-bearing framing the comp-016 scan is testing.
2. **`abcg2-modulators.md` §1 (Androgens entry)** says: *"AR-mediated transcriptional repression of ABCG2 in gut and kidney."* This presupposes a direct AR mechanism on intestinal ABCG2 — which the primary literature does not support.

If the structural-ceiling argument is wrong (or weakly supported), the implications cascade:
- The "men have a lower asymptote on platform efficacy" framing should be softened from a *structural* claim to an *empirical-magnitude-uncertain* claim.
- The "rescue lever" framing changes — instead of "anti-androgen pharmacology to relieve AR repression of intestinal ABCG2" (no primary evidence supports this lever exists at intestinal AR level), the better-supported lever is "estrogenic PI3K/Akt agonism on intestinal enterocytes" or "PPARγ-mediated induction via fermentable-fiber butyrate" (which is the mechanism `abcg2-modulators.md` already favors as Tier 1).
- The Q141K-positive male subset still has the strongest case for a genotype-stratified intervention — but the case rests on the genetic-loss-of-function vulnerability (Hoque 2020), not on additional androgen-driven suppression on top of the variant.

## Method summary

**Approach:** WebSearch + WebFetch via PubMed, PMC, journal landing pages, aggregator sites. Six SKILL-prompt-defined sub-questions queried in parallel; results aggregated into per-study structured records (`inputs/studies.json`). Direction-of-effect for each study scored against the load-bearing claim. Per-study load-bearing-for-the-intestinal-claim flag set on the conjunction of: (a) intestinal tissue measured, (b) hormone or genotype manipulation as the variable, (c) ABCG2 readout. Aggregate verdict by tally of supporting / contradicting / neutral studies in the load-bearing subset.

**Tool limitations encountered:** WebFetch was 403-blocked from PMC, ScienceDirect, Springer, MDPI, Frontiers, PubMed, doi.org redirects. All primary-literature claims were extracted at abstract-level + WebSearch-result-summary-level, NOT full-text grep-verified per [`manual-literature-mining.md`](./manual-literature-mining.md) §"Pre-commit verification gate." This is acknowledged in the limitations section.

**Multilingual scan:** NOT executed in this run (CNKI / J-STAGE / KISS queries deferred to a Phase 2 follow-up — see Limitations).

## Key results

### The load-bearing-for-the-intestinal-claim subset (3 of 17 studies)

| Study | Tissue | Intervention | Direction | Key magnitude |
|---|---|---|---|---|
| **S01 Hoque 2020** Nature Communications PMID 32488095 | mouse intestine + kidney | Q140K knock-in (genetic LoF) | Supports sex-dimorphism (males vulnerable) | **88% intestinal ABCG2 protein loss** in male Q140K homozygotes; 53% heterozygotes; 44% renal — intestinal more vulnerable than renal. Female Q140K protected. |
| **S03 Yu 2021** Nutr Metab PMID 34144706 | mouse intestine + Caco-2 | estradiol benzoate IP | Supports female-positive arm; not male-negative | Estradiol upregulates intestinal ABCG2 via PI3K/Akt; LY294002 partially blocks. Direction confirmed; specific fold-change not extracted from abstract. |
| **S04 Klyushova 2023** Biochem Moscow DOI 10.1134/S1990747823050100 | Caco-2 | T at 1, 10, 100 μM, 24h | **CONTRADICTS** | Testosterone INCREASES ABCG2 in Caco-2 via PXR/FXR (xenobiotic-sensor) pathway, not AR. Direction opposite to platform thesis at in vitro intestinal level. |

**No fourth load-bearing study exists** — no primary paper has done the experiment that would directly answer the question (orchiectomy + measure intestinal ABCG2; or T administration → intestinal ABCG2 mRNA/protein in vivo).

### The supportive-but-not-load-bearing studies (cohort-level androgen → urate)

| Study | Direction | Magnitude | Caveat |
|---|---|---|---|
| **S02 Sakamoto 2018** PMID 30557349 | Supports T → urate up | **−0.66 mg/dL** at 6 months ADT (n=150 ADT vs 339 surgery) | Mechanism not isolated to intestine; consistent with URAT1-only |
| **S08 Yahyaoui 2008** PMID 18349066 | Supports T → urate up | FtM 2-year T administration significantly raised serum UA + decreased FEUA | Renal-FEUA mechanism implied; intestinal ABCG2 not measured |
| **S15 KNIGHT/ENIGI** 2024-2025 | Supports T → urate up, dose-dependent | FtM cohort, magnitude not extracted | Renal-FEUA mechanism cited; intestinal not measured |
| **S16 Adolescent boys** PMC8405811 | Supports T → urate up | Pubertal UA rise correlates with T + low SHBG | Mechanism not measured at tissue level |
| **S14 Hak Choi 2008 NHANES** PMID 18822120 | Supports estrogen → urate down | HRT users −0.24 mg/dL adjusted | Cohort observational |

**These cohort studies confirm androgens are a real and clinically meaningful urate-elevating signal in human physiology.** They do NOT distinguish renal (URAT1) vs intestinal (ABCG2) mechanism. The −0.66 mg/dL Sakamoto magnitude is consistent with URAT1 being the dominant transporter affected — URAT1 changes alone can produce this size of effect (per the Hosoyamada 2010 mouse work).

### The mechanism studies

| Study | Tissue | Mechanism finding |
|---|---|---|
| **S07 Jeong 2015** PMID 25615818 | LNCaP prostate cancer | Androgen withdrawal → ↑CREB-P → ↑CRTC2 nuclear translocation → ↑BCRP via −329 CRE on promoter. **Indirect mechanism in cancer cells**; no direct AR-ARE on the BCRP promoter. |
| **S05 Tanaka 2005** PMID 15567169 | rat kidney + mouse liver | Sex-dimorphic ABCG2 driven by estradiol-suppressive on females, not testosterone-inductive on males. The female-low pattern is the load-bearing direction. |

**Receptor mechanism finding:** there is no published direct AR → ABCG2 promoter binding. The closest mechanism is the indirect CREB/CRTC2 axis in prostate cancer cells (Jeong 2015). No data extending this to intestinal epithelium.

### The contradictory studies

| Study | Tissue | Finding |
|---|---|---|
| **S04 Klyushova 2023** | Caco-2 | T induces ABCG2 (direction opposite to thesis) |
| **S10 MacLean 2008** PMID 18378562 | rat intestine (full scan) | NO sex difference in baseline ABCG2 across duodenum, jejunum, ileum, colon — explicit null finding |

## Mechanism reframing — what the evidence actually supports

The wiki's current implicit model:

```
Androgens → AR → ↓ABCG2 transcription → ↓intestinal ABCG2 protein → ↓luminal urate → structural ceiling on gut-sink platform
```

The literature-supported model:

```
Females have estradiol-driven intestinal ABCG2 upregulation (Yu 2021, PI3K/Akt) → higher gut-sink baseline
Males lack this estradiol drive → lower gut-sink baseline (modest, magnitude uncertain)
Q141K-positive males (regardless of androgen state) are vulnerable to severe loss-of-function (Hoque 2020) — independent of androgen
ADT in human cohorts lowers serum UA at clinically meaningful magnitude (Sakamoto 2018, −0.66 mg/dL) but mechanism likely renal URAT1-dominant
```

The two models have **substantially different platform-design implications:**

| Implication | "Androgens suppress ABCG2" model | "Females have estradiol-driven ABCG2 upregulation; males lack it" model |
|---|---|---|
| Intervention lever | Anti-androgen pharmacology on intestinal AR | Estrogenic PI3K/Akt induction OR PPARγ butyrate route |
| Magnitude expected from rescue | Substantial (relieve a strong tonic suppression) | Modest (induce signal that's normally absent) |
| Q141K stratification | Genotype × androgen status | Genotype × estrogen status; androgen status secondary |
| Female-specific therapy | Less needed (no androgen-suppression) | Females already at higher baseline; therapy more leveraged in males |
| Confidence interval on the asymptote difference | Predicted to be substantial | Empirically near-null in healthy baseline (MacLean 2008); only emerges under disease/genetic stress |

## Correction note (post-comp-017 full-text re-read, 2026-05-07)

A subsequent Tier-0 follow-up experiment ([comp-017](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md)) did the full-text re-read of the four anchor papers (Hoque 2020, Yu 2021, Klyushova 2023, MacLean 2008) and surfaced numerical and methodological refinements to comp-016's abstract-level numbers. **The qualitative direction of comp-016's verdict (T → intestinal ABCG2 suppression WEAK / UNCONFIRMED) is unchanged and arguably strengthened.** The corrections:

- **Hoque 2020 PMID 32488095 — "88% intestinal protein loss" is the COMBINED Western + apical IHC measurement for homozygotes.** The Western-jejunum-only number is **78%** (~1.8× the 44% renal loss, not 2.0× as comp-016's framing implied). The 53% number is the heterozygote combined. UA flux loss in the ligation loop is 40%. Female FEUA p=0.6263 (strong null). Paper does NOT invoke AR. Both numbers (78% and 88%) are real measurements; comp-016's "88%" framing is correct as the combined-assay result but the Western-only number is more conservative for the platform-thesis ceiling argument.
- **Yu 2021 PMID 34144706 — Caco-2 active concentration is 100 µM EB, 5–6 orders above physiological serum E2** (~30–500 pmol/L). Paper notes "without a dose-dependent effect." Female mouse arm is OVARIECTOMIZED + EB replacement (high-contrast pharmacological model, NOT healthy comparison). The mechanism EXISTS at strong-pharmacological tier; magnitude at physiological E2 is unestablished. The "estradiol upregulates intestinal ABCG2 via PI3K/Akt" reframe in this page is correct as a mechanism claim but should not be cited as supporting a measurable population-level sex-dimorphism in healthy adults.
- **Klyushova 2023 — ALL three sex hormones (T, E2, P) at all three concentrations (1, 10, 100 µM) INCREASE ABCG2 via PXR/FXR.** This is a xenobiotic-sensor response, not hormone-receptor-specific. Lowest active T concentration is ~30–100× above physiological free T. The "T INDUCES not suppresses ABCG2" framing in this page is correct, but the mechanism is xenobiotic-tier, not androgen-axis-specific.
- **MacLean 2008 null finding STRENGTHENED** by Tubic-Grozdanis 2020 replication (P-gp dimorphic, BCRP not).
- **NEW finding (Hosoyamada 2010 PMID 20589576 full-text):** T → renal Smct1 mRNA AND protein ↑, GLUT9 attenuated, BUT URAT1 mRNA-only (protein UNCHANGED in non-orchiectomized animals). The renal-arm mechanism propagated into [`androgen-urate-axis.md`](./androgen-urate-axis.md) was overstated; the protein-level driver of male hyperuricemia in mouse renal tissue is Smct1 + GLUT9 attenuation, not URAT1 protein elevation. comp-017's full-text re-read surfaced this; the parent page is updated correspondingly.

**Net implication for the platform thesis:** comp-016's WEAK / UNCONFIRMED verdict survives unchanged in qualitative direction. The "structural ceiling on platform efficacy in androgen-dominant patients" framing **softens further than comp-016 already softened it** — at healthy baseline, the sex-dimorphism magnitude is empirically near-null; the asymptote difference manifests primarily under disease-state genetic stress (Q141K) or strong-pharmacological perturbation. The Q141K rescue thesis is unaffected and remains the platform's strongest pharmacogenomic differentiator.

## Limitations

1. **Abstract-level + search-summary-level only.** All 17 studies are anchored to abstracts and WebSearch-result-summary text, NOT full-text grep-verified per [`manual-literature-mining.md`](./manual-literature-mining.md) Rule 4. The Hoque 2020 "88% intestinal protein loss" magnitude, the Sakamoto 2018 "−0.66 mg/dL" magnitude, and the Yu 2021 PI3K/Akt mechanism are all from search-summary abstracts — should be grep-verified against the published papers in a follow-up Paperclip MCP run before they are quoted as load-bearing in any wiki page that depends on those magnitudes. **Confidence tier: "verified-against-summary" not "verified-against-primary."** [comp-017 partially closed this for the four anchor papers — see Correction note above.]

2. **WebFetch 403-blocked across PMC, journals, PubMed.** A future run with Paperclip MCP (per the methodology in [`manual-literature-mining.md`](./manual-literature-mining.md)) could pull full-text content.lines for grep verification.

3. **Multilingual scan NOT executed.** Per [`CLAUDE.md`](../CLAUDE.md) §"Global-multilingual research by default," CNKI / J-STAGE / KISS / WanFang queries should have run for testosterone × intestinal ABCG2. Deferred to Phase 2. Likelihood-of-finding-something-new is uncertain — the field is dominated by Western pharma-DMPK and rheumatology research for ABCG2 specifically; Chinese/Japanese gout literature tends to focus more on URAT1 and XO than ABCG2.

4. **The 17-study scan is non-exhaustive.** Other relevant primary literature may exist that this scan missed. The verdict is robust to this in the qualitative direction (it would take a single primary study showing direct T → intestinal ABCG2 suppression in vivo to flip the verdict to PARTIAL; that study has not surfaced in this scan).

5. **The verdict logic is conservative.** A different reviewer could reasonably argue the indirect Hoque 2020 + Sakamoto 2018 + Yu 2021 + FtM-cohort triangulation supports a PARTIAL verdict ("the sex-dimorphism is real even if the mechanism is estradiol-positive rather than androgen-negative"). This page records the WEAK_UNCONFIRMED verdict as the strict literal answer to the SPECIFIC claim "androgens directly suppress intestinal ABCG2"; the broader claim "intestinal ABCG2 is sex-dimorphic in a urate-relevant way" is well-supported and downstream pages should retain it.

6. **The directionality difference matters substantively.** "Androgens suppress" vs "estradiol upregulates the female arm and males lack the signal" sound similar but predict different rescue interventions and different platform-design choices. The conservative verdict on the SPECIFIC claim is meaningful for the platform design.

## Impact on experimental priorities

| Wet-lab / experimental question | Pre-comp-016 priority | Post-comp-016 priority |
|---|---|---|
| `validation-experiments.md` §1.14 (TNFα + butyrate ABCG2 rescue in Caco-2) | Confirmation experiment | **Stays as confirmation** — TNFα suppression and butyrate induction are well-supported; orthogonal to androgen question |
| `validation-experiments.md` §1.22 (Q141K rescue HDAC inhibitor screen — comp-007) | Confirmation experiment | **Stays as confirmation** — Q141K rescue is butyrate-mediated, orthogonal to androgen direct suppression |
| Hypothetical animal-model experiment: castration → intestinal ABCG2 measurement | Not yet specified | **Now PROMOTED** — the cheapest experimental killshot for this question. Direct measurement that would either confirm or falsify the androgen-direct-suppression mechanism. Estimated cost: ~$30K–60K, 8 weeks; standard mouse castration + T-replacement + jejunal/ileal Western blot + qPCR for ABCG2. Could potentially extend to FtM cohort biopsy data if a collaborating clinical group exists. |
| Hypothetical pharmacogenomic Q141K × androgen-status stratification of fiber RCT | Not yet specified | **Worth noting as Phase 2** — would resolve whether the platform thesis is androgen-modulated or estrogen-driven at the human level. Higher cost and longer timeline. |

## Cross-references

- [`androgen-urate-axis.md`](./androgen-urate-axis.md) — the parent page; primary propagation target
- [`abcg2-modulators.md`](./abcg2-modulators.md) §1 (Androgens entry) — secondary propagation target
- [`gut-lumen-sink.md`](./gut-lumen-sink.md) — softens the male-asymptote framing
- [`koji-endgame-strain.md`](./koji-endgame-strain.md) §1 (if structural-ceiling argument cited)
- [`cross-validation.md`](./cross-validation.md) Claim 1 (if dependent on androgen-ABCG2 link)
- [`computational-experiments.md`](./computational-experiments.md) — comp-016 row
- [`manual-literature-mining.md`](./manual-literature-mining.md) — methodology for the literature-mining shaped comp-NNN flow + the verification gate this experiment exemplifies
- [`experiments/comp-016-t-abcg2-suppression-evidence-mining/`](../experiments/comp-016-t-abcg2-suppression-evidence-mining/) — reproducible artifact

## Pre-commit verification gate disclosure

Per [`manual-literature-mining.md`](./manual-literature-mining.md) §"Pre-commit verification gate":

**Sources WebSearch-summary-verified, NOT full-text grep-verified (the limitation that bounds confidence on this page's quantitative claims):**
- All 17 primary studies were extracted at abstract / search-summary level. The page cites magnitudes (88%, 53%, 44%, −0.66 mg/dL, etc.) that come from search-result text describing the published abstracts.
- This is **explicitly acknowledged as a verification gap.** The page should not be cited as a primary source for any of these magnitudes; consumers should grep-verify against the published papers via Paperclip or full-text PDF before using the magnitudes in load-bearing downstream analyses.

**The qualitative verdict (WEAK_UNCONFIRMED) is robust to this caveat** because it turns on the direction of evidence ("no primary paper directly demonstrates T → intestinal ABCG2 suppression in vivo"), not on the magnitudes. A future Paperclip-MCP run would refine the magnitudes and confirm/refute exact numbers, but is unlikely to surface a primary study that would flip the qualitative verdict.

**What WOULD flip the verdict:**
- A primary paper showing castration → measurable increase in intestinal ABCG2 mRNA or protein (would shift verdict toward PARTIAL or CONFIRMED)
- A primary paper showing T administration → measurable decrease in intestinal ABCG2 in vivo (would shift verdict toward PARTIAL or CONFIRMED)
- A pharmacogenomic study with sex-stratified Q141K data showing androgen status modulates the variant's effect on serum UA at meaningful magnitude (would partially support the platform thesis)
- A direct AR-ARE binding ChIP-seq result on the ABCG2 promoter (would shift the receptor-mechanism question toward CONFIRMED for the molecular arm)

If any of these surface in a future scan, the verdict should be revisited and this page updated.
