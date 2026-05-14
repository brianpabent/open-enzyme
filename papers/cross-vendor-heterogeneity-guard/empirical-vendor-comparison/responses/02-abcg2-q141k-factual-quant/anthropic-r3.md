---
prompt_id: 02-abcg2-q141k-factual-quant
prompt_sha256_12: 067cbf19781f
vendor: anthropic
replicate: 3
model_requested: anthropic/claude-opus-4-7
model_served: anthropic/claude-4.7-opus
model_served_raw: anthropic/claude-4.7-opus-20260416
call_timestamp_utc: 2026-05-14T17:29:55.829844Z
latency_seconds: 24.92
input_tokens: 386
output_tokens: 1492
cost_usd: 0.1177
finish_reason: stop
response_sha256_12: 25b6ff9a5ed4
status: ok
---

# ABCG2 and Q141K (rs2231142): Key Parameters

## 1. Fraction of total uric acid excretion mediated by ABCG2

**~10% of total urate excretion** in mice under baseline conditions, but ABCG2 is estimated to handle a substantially larger share of *extra-renal* (intestinal) excretion. In humans, precise fractional attribution is **uncertain**; the most cited figure is that ABCG2 dysfunction shifts the balance such that ~2/3 of hyperuricemia cases with ABCG2 variants show an "extra-renal underexcretion" phenotype.

- Primary source: Ichida K et al., *Nat Commun* 2012;3:764. "Decreased extra-renal urate excretion is a common cause of hyperuricemia." This study established that ABCG2 dysfunction causes extra-renal (gut) underexcretion rather than renal underexcretion.
- Matsuo H et al., *Sci Transl Med* 2009;1:5ra11 (original identification of ABCG2 as a urate transporter).

## 2. Functional consequence of Q141K

**~50% reduction** in urate transport activity relative to wild-type ABCG2.

- Woodward OM et al., *PNAS* 2009;106(25):10338–10342. Xenopus oocyte expression: Q141K showed ~53% reduction in urate transport vs. WT. This is the canonical reference.
- The defect is primarily due to reduced protein expression/stability (ATP-binding domain destabilization) rather than altered intrinsic transport kinetics — Furukawa T et al., *Mol Pharm* 2009.

## 3. Minor allele frequency (gnomAD v2/v3, 1000G)

- **East Asian: ~29–32%** (highest of any major population)
- **European (non-Finnish): ~9–11%**
- African: ~1–3% (for context)

Source: gnomAD; 1000 Genomes Project. Consistent with Cleophas MC et al., *Rheumatology* 2017 review.

## 4. Odds ratio for gout/hyperuricemia

**OR ≈ 1.74 per risk allele** for gout in European populations (Dehghan A et al., *Lancet* 2008;372:1953–61, meta-analysis of Framingham + Rotterdam + ARIC).

More striking effect in homozygotes:
- **Matsuo H et al., *Ann Rheum Dis* 2010;69:1248–51**: For Q141K homozygotes (Japanese), **OR ≈ 3.26** for gout vs. wild-type. For Q126X (a rarer null), effects were larger. Combined ABCG2 dysfunction showed OR up to ~25 for severe early-onset gout (Matsuo H et al., *Sci Rep* 2013;3:2014).

## 5. Gut vs. kidney as dominant site

**The intestine (gut) is the dominant site of ABCG2-mediated urate excretion**, although ABCG2 is expressed on the apical membrane of both renal proximal tubule cells and enterocytes.

Evidence:
- **Ichida K et al., *Nat Commun* 2012;3:764**: In *Abcg2*-knockout mice, serum urate rose and intestinal urate excretion fell markedly, while renal urate excretion actually *increased* (compensatory). Human carriers of dysfunctional ABCG2 variants showed elevated fractional renal excretion of urate, indicating the primary defect was extra-renal.
- **Hosomi A et al., *PLoS One* 2012;7:e30456**: Direct demonstration of ABCG2-mediated intestinal urate secretion in mice; ABCG2 inhibition raised plasma urate via reduced gut excretion.
- This is why Q141K hyperuricemia is classified as the "extra-renal underexcretion / renal overload" phenotype rather than renal underexcretion (Matsuo H et al., *Sci Rep* 2014;4:3755).

---

**Caveats**: Exact fractional contribution (item 1) in humans remains model-dependent — the ~1/3 renal, ~2/3 gut split often quoted for total urate disposal is approximate and predates ABCG2-specific quantification. Q141K functional reduction estimates range from ~40–60% depending on system (oocyte vs. mammalian cell, membrane vs. whole-cell).
