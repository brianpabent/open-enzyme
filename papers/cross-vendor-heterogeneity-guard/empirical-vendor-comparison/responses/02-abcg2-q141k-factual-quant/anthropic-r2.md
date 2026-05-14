---
prompt_id: 02-abcg2-q141k-factual-quant
prompt_sha256_12: 067cbf19781f
vendor: anthropic
replicate: 2
model_requested: anthropic/claude-opus-4-7
model_served: anthropic/claude-4.7-opus
model_served_raw: anthropic/claude-4.7-opus-20260416
call_timestamp_utc: 2026-05-14T17:02:50.580054Z
latency_seconds: 26.77
input_tokens: 386
output_tokens: 1524
cost_usd: 0.1201
finish_reason: stop
response_sha256_12: cab58114db05
status: ok
---

# ABCG2 and Q141K (rs2231142): Focused Summary

## 1. Fraction of total uric acid excretion mediated by ABCG2

Approximately **~25–30% of total uric acid excretion** is attributable to ABCG2 in healthy humans, based on extrapolation from murine knockout data and human dysfunction studies.

- Matsuo et al., *Sci Transl Med* 2009;1(5):5ra11 — demonstrated ABCG2 dysfunction shifts uric acid handling and quantified its contribution to extra-renal (intestinal) excretion.
- Ichida et al., *Nat Commun* 2012;3:764 — "Decreased extra-renal urate excretion is a common cause of hyperuricemia" — showed ABCG2 dysfunction reduces gut excretion; estimated ABCG2 handles a substantial fraction of total urate elimination.

The precise human percentage is **uncertain**; the ~25–30% figure is a reasonable approximation but not directly measured in healthy humans.

## 2. Functional consequence of Q141K

Q141K reduces ABCG2 urate transport activity by **~50% relative to wild-type** in heterologous expression systems (Xenopus oocytes, membrane vesicles). The defect is primarily due to impaired protein expression/stability (ER-associated degradation), not catalytic incompetence per se.

- Woodward et al., *PNAS* 2009;106(25):10338–10342 — first showed Q141K reduces urate transport by ~53%.
- Furukawa et al. and subsequent structural work attribute the defect to destabilization of the nucleotide-binding domain.

## 3. Minor allele frequency

- **East Asian**: ~**29–32%** (gnomAD v2/v3; 1000 Genomes EAS)
- **European (non-Finnish)**: ~**9–11%** (gnomAD; 1000 Genomes EUR)
- African MAF is substantially lower (~3–5%) for context.

## 4. Odds ratio for gout/hyperuricemia

Multiple large studies; representative figures:

- **Dehghan et al., *Lancet* 2008;372(9654):1953–1961** (Rotterdam + Framingham + ARIC meta-analysis): per-allele OR for gout ≈ **1.74 (95% CI 1.41–2.16)** in whites of European descent.
- **Matsuo et al., *Ann Rheum Dis* 2010;69(7):1407–1408** and follow-ups in Japanese cohorts: homozygous Q141K (KK) OR for gout ≈ **2.4–3.2** vs. QQ; with combined ABCG2 dysfunction (Q141K + Q126X), OR can exceed 10.
- Kolz et al., *PLoS Genet* 2009 — GWAS meta-analysis confirms genome-wide significant association with serum urate.

## 5. Gut vs. kidney as dominant site

**The intestine (gut) is the dominant site affected functionally by ABCG2 dysfunction**, though under normal physiology the kidney excretes more total urate.

Key distinction: ABCG2 is expressed in both apical proximal tubule (kidney) and apical enterocyte (intestine). When ABCG2 is dysfunctional, **extra-renal (intestinal) excretion decreases disproportionately**, and renal excretion paradoxically *increases* as compensation — the so-called "extra-renal urate underexcretion" phenotype.

Evidence:
- **Ichida et al., *Nat Commun* 2012;3:764** — directly demonstrated in Abcg2-knockout mice that intestinal urate secretion is markedly reduced while renal excretion increases; classified human Q141K carriers as "extra-renal underexcretors."
- **Matsuo et al., *Sci Rep* 2014;4:3755** — showed in a Japanese gout cohort that ABCG2 dysfunction predominantly causes the "renal overload" (extra-renal underexcretion) gout subtype rather than classical renal underexcretion.

So: **kidney handles more urate in absolute terms, but ABCG2's non-redundant role is in the gut** — this is where loss-of-function variants manifest most clearly.

---

**Caveats**: The ~25–30% total excretion figure and ~50% activity reduction are commonly cited but derived from limited model systems; both should be treated as order-of-magnitude estimates rather than precise physiological constants in humans.
