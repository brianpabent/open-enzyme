---
prompt_id: 02-abcg2-q141k-factual-quant
prompt_sha256_12: 067cbf19781f
vendor: anthropic
model_requested: anthropic/claude-opus-4-7
model_served: anthropic/claude-4.7-opus
model_served_raw: anthropic/claude-4.7-opus-20260416
call_timestamp_utc: 2026-05-14T16:00:39.360854Z
latency_seconds: 27.95
input_tokens: 386
output_tokens: 1604
cost_usd: 0.1261
finish_reason: stop
response_sha256_12: de394445fe93
status: ok
---

# ABCG2 and the Q141K (c.421C>A, rs2231142) Polymorphism

## 1. Fraction of total uric acid excretion mediated by ABCG2

Approximately **~50% of total daily uric acid excretion** in humans, when considering combined renal + extra-renal (intestinal) routes. The original quantitative claim derives from mouse Abcg2-knockout studies and human SNP–excretion correlations.

- **Primary source:** Ichida K, Matsuo H, Takada T, et al. "Decreased extra-renal urate excretion is a common cause of hyperuricemia." *Nat Commun.* 2012;3:764. This paper estimated that ABCG2 dysfunction reduces extra-renal (gut) urate excretion and that ABCG2 contributes a substantial fraction of overall urate handling. The ~50% figure is an integration across renal secretion + intestinal excretion; the precise human fraction is **uncertain** and model-dependent.

## 2. Functional consequence of Q141K

Q141K reduces ABCG2 urate transport activity by approximately **~50% relative to wild-type** in heterozygous-equivalent expression systems, with greater reduction (~75% or more) in homozygotes. The defect is primarily due to impaired protein folding/stability and reduced plasma-membrane expression rather than altered intrinsic transport kinetics.

- **Primary source:** Woodward OM, Köttgen A, Coresh J, Boerwinkle E, Guggino WB, Köttgen M. "Identification of a urate transporter, ABCG2, with a common functional polymorphism causing gout." *PNAS.* 2009;106(25):10338–10342. Reported ~53% reduction in urate transport for Q141K.
- Supported by: Matsuo H et al., *Sci Transl Med.* 2009;1(5):5ra11.

## 3. Minor allele frequency (MAF) of Q141K (rs2231142, A allele)

- **(a) East Asian:** ~**0.29–0.32** (gnomAD East Asian ≈ 0.29)
- **(b) European (non-Finnish):** ~**0.09–0.11** (gnomAD ≈ 0.09)

Source: gnomAD v2.1/v3 allele frequency database; consistent with 1000 Genomes Project frequencies.

## 4. Published odds ratio for gout/hyperuricemia

- **Matsuo H et al., *Sci Transl Med.* 2009;1(5):5ra11:** In a Japanese case-control study, the Q141K variant was associated with gout with an **OR ≈ 2.3** for heterozygotes and **OR ≈ 5.97** for homozygotes (Q/Q 141K) versus wild-type.
- **Kolz M et al., *PLoS Genet.* 2009;5(6):e1000504** (meta-GWAS of serum urate): per-A-allele effect of ~0.22 mg/dL increase in serum urate.
- **Dehghan A et al., *Lancet.* 2008;372(9654):1953–1961:** OR for gout per Q141K allele ≈ **1.7–1.8** in European cohorts (Rotterdam/ARIC).

## 5. Gut vs kidney as dominant site

**The intestine (gut) is considered the dominant site of ABCG2-mediated urate excretion**, though both contribute.

- **Evidence:** Ichida et al. (*Nat Commun* 2012) showed that ABCG2 dysfunction in humans correlates more strongly with reduced *extra-renal* urate excretion than with reduced renal urate excretion, and that "ABCG2 dysfunction-type" hyperuricemia (overload due to decreased gut excretion) is more common than the renal-underexcretion phenotype attributable to ABCG2. Abcg2-knockout mice show markedly reduced intestinal urate secretion with compensatory increase in renal excretion (Hosomi A, Nakanishi T, Fujita T, Tamai I. *PLoS One.* 2011;6(2):e17317).
- **Caveat:** ABCG2 is expressed apically in both proximal tubule and enterocyte; the "gut-dominant" assignment is based on the relative magnitude of dysfunction-attributable urate retention, not on absolute mass-balance flux measurements in healthy humans, which remain **uncertain**.

---

**Evidence-level summary:** Items 2, 3, and 4 rest on strong primary functional and population-genetic data. Items 1 and 5 are supported by convergent but model-dependent evidence (mouse knockouts + human SNP–phenotype inference); precise human in vivo mass-balance values should be treated as approximations.
