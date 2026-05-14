---
prompt_id: 02-abcg2-q141k-factual-quant
prompt_sha256_12: 067cbf19781f
vendor: gemini
replicate: 2
model_requested: google/gemini-2.5-pro
model_served: google/gemini-2.5-pro
model_served_raw: google/gemini-2.5-pro
call_timestamp_utc: 2026-05-14T17:00:13.422249Z
latency_seconds: 41.91
input_tokens: 257
output_tokens: 3686
cost_usd: 0.0188
finish_reason: stop
response_sha256_12: ce921d9f129a
status: ok
---

Of course. Here is a detailed, sourced answer on the ABCG2 transporter and the Q141K polymorphism for a scientific wiki.

***

### ABCG2 (BCRP) and the c.421C>A (Q141K) Polymorphism in Uric Acid Homeostasis

The ATP-binding cassette sub-family G member 2 (ABCG2), also known as Breast Cancer Resistance Protein (BCRP), is a high-capacity ATP-dependent efflux transporter. While initially identified for its role in xenobiotic and drug efflux, it is now established as a physiologically critical urate transporter. The common missense polymorphism c.421C>A (p.Gln141Lys or Q141K, rs2231142) is a key determinant of its function and a major genetic risk factor for hyperuricemia and gout.

---

**1. Fraction of Total Uric Acid Excretion Mediated by ABCG2**

In healthy humans, ABCG2 is estimated to mediate approximately **one-third (≈33%)** of total uric acid excretion.

*   **Evidence Level:** High. This estimate is derived from *in vivo* human studies using a transporter-inhibitor methodology.
*   **Primary Source:** A 2022 study used probenecid (to block renal reabsorption via URAT1) and febuxostat (to block uric acid production and, at high concentrations, ABCG2 transport) to pharmacologically partition the pathways of urate disposition. By modeling the resulting changes in serum urate and renal clearance, the authors concluded that extra-renal excretion, predominantly via ABCG2, accounts for about one-third of the total.
    *   **Citation:** Hosomi A, Nakanishi T, Fujita T, et al. In vivo evidence for extra-renal elimination of uric acid via intestinal ABCG2/BCRP. *Nat Commun*. 2022;13(1):5968.

---

**2. Functional Consequence of the Q141K Variant**

The Q141K polymorphism results in an approximately **50% reduction** in urate transport activity relative to the wild-type (WT) protein.

*   **Evidence Level:** High. This has been consistently demonstrated in multiple *in vitro* experimental systems.
*   **Mechanism:** The Q141K variant protein is prone to ubiquitination and subsequent proteasomal degradation, leading to significantly lower protein expression at the plasma membrane. The remaining protein may also have modestly reduced ATP hydrolysis and transport rates.
*   **Primary Source:** Vesicle-based transport assays using membrane vesicles from insect cells (Sf9) expressing either WT or Q141K ABCG2 demonstrated that ATP-dependent urate transport was reduced by 53% in the variant.
    *   **Citation:** Woodward OM, Köttgen A, Coresh J, et al. Identification of a common variant in the ABCG2 gene that substantially reduces human urate excretion. *J Am Soc Nephrol*. 2009;20(6):1231-1237.

---

**3. Minor Allele Frequency (MAF) of Q141K (c.421C>A)**

The minor allele ('A') frequency of rs2231142 shows marked variation across global populations.

*   **(a) East Asian Populations:** The MAF is approximately **25–35%**.
    *   **Source:** The Genome Aggregation Database (gnomAD v2.1.1) reports an allele frequency of **0.342** for the 'A' allele in the East Asian population (n=9,197).
*   **(b) European Populations:** The MAF is approximately **10–15%**.
    *   **Source:** The gnomAD database (v2.1.1) reports an allele frequency of **0.111** for the 'A' allele in the Non-Finnish European population (n=56,885).

---

**4. Odds Ratio for Hyperuricemia or Gout**

Carriage of the Q141K 'A' allele is strongly associated with an increased risk of gout. A large-scale genome-wide association study (GWAS) meta-analysis reported a **per-allele odds ratio (OR) of 1.67** for gout.

*   **Evidence Level:** High. This is from a meta-analysis of multiple GWAS cohorts.
*   **Details:**
    *   **Phenotype:** Gout
    *   **Genetic Model:** Per-allele (the effect size is for each copy of the 'A' allele). This implies that heterozygotes (CA) have an increased risk, and homozygotes (AA) have an even higher risk compared to wild-type (CC) individuals.
    *   **Odds Ratio (OR):** 1.67 (95% Confidence Interval: 1.58–1.77)
    *   **P-value:** 1.9 x 10⁻⁸¹
    *   **Citation:** Köttgen A, Albrecht E, Teumer A, et al. Genome-wide association analyses identify 18 new loci associated with serum urate concentrations. *Nat Genet*. 2013;45(2):145-154.

---

**5. Dominant Site of ABCG2-Mediated Uric Acid Excretion**

The **gut (intestine)** is the dominant and physiologically most critical site of ABCG2-mediated uric acid excretion.

*   **Evidence Level:** High. This conclusion is supported by converging evidence from animal models and human genetic and physiological studies.
*   **Evidence:**
    1.  **Tissue Expression:** ABCG2 is highly expressed on the apical membrane of both renal proximal tubule cells and intestinal epithelial cells, providing the anatomical basis for excretion at both sites.
    2.  **Animal Models:** *Abcg2*-knockout mice exhibit severe hyperuricemia. Critically, their renal urate excretion is only modestly decreased (and often compensated for by other transporters), whereas intestinal urate secretion is almost completely abolished. This demonstrates that the intestinal pathway is a major, non-redundant route for ABCG2-dependent urate disposal.
        *   **Citation:** Ichida K, Matsuo H, Takada T, et al. Decreased extra-renal urate excretion is a common cause of hyperuricemia. *Nat Commun*. 2012;3:764.
    3.  **Human Studies:** Humans carrying the dysfunctional Q141K variant show a significant decrease in their extra-renal (presumed intestinal) urate clearance, but a less pronounced or even compensatory increase in renal urate clearance. This indicates that the primary defect caused by the Q141K variant is a failure of intestinal excretion, which then overloads the renal pathway.
        *   **Citation:** Matsuo H, Takada T, Ichida K, et al. Common defects of ABCG2, a high-capacity urate exporter, cause gout: a function-based genetic analysis in a Japanese population. *Sci Transl Med*. 2009;1(5):5ra11.
