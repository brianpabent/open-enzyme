---
title: P0-2 East Asian gout genetics source read
date: 2026-05-20
status: source-read-complete
---

# P0-2 East Asian gout genetics source read

## Protocol

This pass used the local-network retrieval route for J-STAGE PDFs (`curl` from Brian's laptop path), then applied the two-model non-English protocol:

- Model A: Codex / GPT-5.5 source read over the Japanese J-STAGE PDFs.
- Model B: DeepSeek (`deepseek/deepseek-chat-v3` via OpenRouter) independent counter-read over the same Japanese source excerpts; saved at [`p0-2-jstage-deepseek-counterread-2026-05-20.json`](./p0-2-jstage-deepseek-counterread-2026-05-20.json).

No load-bearing translation disagreement survived the counter-read. DeepSeek's main correction was wording hygiene: Sakiyama 2017's 4,902 health-check controls include both men and women, and the sex-specific serum-urate values should be described as cohort averages, not universal effects.

## Sources read

1. Sakiyama M. et al. `URAT1/SLC22A12遺伝子の機能消失型変異が血清尿酸値および痛風・高尿酸血症の発症に与える影響`. *Gout and Nucleic Acid Metabolism* 41(1):143 (2017). [J-STAGE](https://www.jstage.jst.go.jp/article/gnam/41/1/41_143/_article/-char/ja), DOI `10.6032/gnam.41.143`.
2. Yoshioka K. et al. `腎性低尿酸血症3例における尿酸トランスポーター(URAT1)遺伝子異常の解析`. *Gout and Nucleic Acid Metabolism* 28(2):115-120 (2004). [J-STAGE](https://www.jstage.jst.go.jp/article/gnam1999/28/2/28_115/_article/-char/ja), DOI `10.6032/gnam1999.28.2_115`.
3. Ichida K. `尿酸代謝・尿酸トランスポーターと尿酸異常症`. *YAKUGAKU ZASSHI* 144(6):659-674 (2024). [J-STAGE](https://www.jstage.jst.go.jp/article/yakushi/144/6/144_23-00217/_article/-char/ja), DOI `10.1248/yakushi.23-00217`.
4. Dean L, Kane M. `Allopurinol Therapy and HLA-B*58:01 Genotype`. NCBI Medical Genetics Summaries, updated 2020. [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK127547/).

## Source facts promoted

### URAT1/SLC22A12 W258X and R90H

Sakiyama 2017 directly supports the protective-direction claim for URAT1/SLC22A12 loss-of-function variants in Japanese gout/hyperuricemia cohorts:

- W258X (`rs121907892`) and R90H (`rs121907896`) are representative loss-of-function variants causing renal hypouricemia type 1.
- Cohort: 1,993 Japanese male gout patients plus 4,902 health-check participants (3,305 men, 1,597 women).
- No gout patients carried W258X/R90H.
- The two variants were protective against hyperuricemia (`P = 0.016`, `OR = 0.80`).
- One/two variant copies lowered mean serum urate in Japanese men from 6.2 mg/dL to 4.0/0.8 mg/dL and in Japanese women from 4.5 mg/dL to 3.5/0.6 mg/dL.

Yoshioka 2004 supports the renal-hypouricemia caution:

- Three renal-hypouricemia cases had serum urate below 1.0 mg/dL.
- One patient had homozygous W258X; two sibling patients had heterozygous W258X.
- The authors explicitly caution that whether heterozygous W258X alone can cause renal hypouricemia needs further investigation, including promoter-region analysis.

Ichida 2024 adds population and risk calibration:

- W258X/c.G774A accounts for about 70% of Japanese renal-hypouricemia mutations.
- c.G774A allele frequency: Japanese 2.23-2.55%, Korean 0.9-1.4%, markedly lower in China.
- Exercise-induced acute kidney injury occurs in about 6-7% of renal-hypouricemia patients overall.

### ABCG2 Q141K / Q126X

Ichida 2024 directly supports the East Asian ABCG2 emphasis:

- ABCG2 participates in urate secretion at kidney and intestinal/luminal surfaces.
- Reduced-function ABCG2 SNPs are common in Japanese populations and can produce hyperuricemia through reduced extrarenal excretion.
- Q126X (`rs72552713`) allele frequency is about 3% and abolishes ABCG2 urate transport.
- Q141K (`rs2231142`) allele frequency is about 32% and halves transport activity.

This corroborates the existing OE framing that ABCG2 is not a minor side transporter in East Asian gout genetics. It is a trial-stratification variable for gut-lumen urate interventions, especially any fiber/butyrate/ABCG2-rescue experiment.

### HLA-B*58:01 / allopurinol safety

The NCBI/ACR/CPIC source read tightened wording:

- ACR 2020 conditionally recommends HLA-B*58:01 testing before allopurinol in Southeast Asian ancestry patients (for example Han Chinese, Korean, Thai) and African American patients; it conditionally recommends against universal testing in other groups.
- CPIC states allopurinol is contraindicated in HLA-B*58:01 carriers and recommends alternative medication.
- NCBI summarizes the original Han Chinese finding as 51/51 allopurinol-induced SJS/TEN cases carrying HLA-B*58:01 versus 20/135 allopurinol-tolerant controls.

The wiki previously compressed this to "ACR 2020 strong recommendation." That is now corrected: ACR testing is conditional; CPIC carrier-avoidance is strong.

## OE implications

1. **URAT1 loss-of-function is protective but not a free therapeutic mimic.** W258X/R90H support the URAT1-knockdown thesis, but renal hypouricemia and exercise-induced AKI set the dose ceiling. The siRNA/URAT1 track should keep the <=50% knockdown guardrail until a better dose-risk model exists.
2. **ABCG2 should remain a first-class stratification variable.** Q141K is common enough in Japanese/East Asian cohorts and functionally large enough that gut-lumen urate interventions should pre-specify ABCG2 genotype strata rather than treat East Asian ancestry as a generic prevalence factor.
3. **HLA-B*58:01 is safety/pharmacogenetics, not urate biology.** It belongs in allopurinol comparator/screening logic and patient-action guidance. It does not alter the mechanism of gut-lumen uricase or ABCG2-rescue interventions except by shaping the adjunct-drug landscape.

## Not safe to claim

- Do not claim heterozygous W258X alone is proven sufficient to cause renal hypouricemia; Yoshioka 2004 explicitly leaves that unresolved.
- Do not apply Sakiyama 2017 serum-urate effect sizes outside the Japanese cohort as universal variant effects.
- Do not claim W258X founder-effect explanation as settled causal history; Ichida 2024 presents founder effect as a likely explanation for Japanese enrichment, not a trial-relevant mechanism.
- Do not describe ACR HLA-B*58:01 guidance as a strong recommendation; ACR is conditional, CPIC carrier-avoidance is strong.
