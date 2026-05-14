---
prompt_id: 02-abcg2-q141k-factual-quant
prompt_sha256_12: 067cbf19781f
vendor: openai
model_requested: openai/gpt-5.5
model_served: openai/gpt-5.5
model_served_raw: openai/gpt-5.5-20260423
call_timestamp_utc: 2026-05-14T15:21:34.437224Z
latency_seconds: 157.08
input_tokens: 249
output_tokens: 7583
cost_usd: 0.0917
finish_reason: stop
response_sha256_12: 3c4d7a2003ec
status: ok
---

### ABCG2 c.421C>A / p.Q141K / rs2231142 and urate handling

| Item | Answer | Evidence level / key sources |
|---|---:|---|
| **1. Fraction of total urate excretion mediated by ABCG2** | **Best estimate: ~30% of whole-body urate elimination**, i.e. roughly the **extra-renal/intestinal** component. **Direct ABCG2-specific flux in healthy humans has not been cleanly measured**, so the precise ABCG2-attributable fraction is **uncertain**; the ~30% number is an inference from human urate-balance physiology plus ABCG2 genetic/functional data. | Human physiology: extra-renal urate disposal is about one-third of total urate elimination (Sorensen, *Arthritis Rheum*, 1965). Human genetic/clearance evidence that ABCG2 dysfunction reduces extra-renal urate excretion: Ichida et al., *Nat Commun*, 2012. |
| **2. Functional consequence of Q141K** | Q141K is a **loss-of-function / reduced-function** allele. In urate-transport assays it retains roughly **~50% of wild-type activity**; Matsuo et al. used **~53% residual activity**, i.e. **~47% reduction** relative to WT. Mechanistically, Q141K reduces ABCG2 protein stability/trafficking and cell-surface expression. | Matsuo et al., *Sci Transl Med*, 2009; Woodward et al., *PNAS*, 2009. |
| **3a. Minor-allele frequency, East Asian** | A allele ≈ **0.29–0.31**. | 1000 Genomes Phase 3; similar in gnomAD East Asian datasets. |
| **3b. Minor-allele frequency, European** | A allele ≈ **0.09–0.11**. | 1000 Genomes Phase 3; similar in gnomAD non-Finnish European datasets. |
| **4. Example risk estimate** | In Japanese men, the ABCG2 reduced-function genotype corresponding mainly to **Q141K heterozygosity** was associated with gout with an odds ratio of about **OR ~2.3** versus full-function ABCG2 genotype. More severe ABCG2 dysfunction showed higher risk. | Matsuo et al., *Sci Transl Med*, 2009. Large GWAS/meta-analyses also find rs2231142-A associated with gout/hyperuricemia, typically OR ~1.6–1.8 per A allele, but those are usually additive per-allele estimates rather than clean heterozygote/homozygote contrasts. |
| **5. Dominant site of ABCG2-mediated urate excretion** | **Gut/intestine is generally considered the dominant physiologic site** for ABCG2-mediated urate elimination, not kidney, although ABCG2 is expressed in both intestinal epithelium and renal proximal tubule. | Human evidence: ABCG2 dysfunction produces a “renal-overload” pattern—reduced calculated extra-renal urate excretion with compensatory increased urinary urate excretion—rather than a simple renal underexcretion phenotype (Ichida et al., *Nat Commun*, 2012). Animal/mechanistic evidence: Abcg2/Bcrp at the intestinal apical membrane mediates intestinal urate efflux; knockout or inhibition reduces intestinal urate excretion and shifts burden to kidney (Hosomi et al., *PLoS One*, 2012). |

**Bottom line:** Q141K is a common, population-stratified ABCG2 hypomorphic allele that roughly halves transporter urate activity. The physiologically important ABCG2-dependent urate-disposal route is best assigned to the **intestinal/extra-renal pathway**, accounting for approximately **one-third of total urate elimination**, but the exact ABCG2-specific fraction in healthy humans remains **not directly quantified**.
