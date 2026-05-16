# Phase A — Query Strategy

## Mission

Identify post-hoc stratification of existing oral-uricase + systemic-uricase + ABCG2-axis ULT response data by ABCG2 Q141K (rs2231142) genotype, scoping whether the gut-lumen uricase mechanism's effect size depends on Q141K-positive disease-state vulnerability.

## Source list

| Source | Sub-question |
|---|---|
| PubMed (MCP `search_articles` + `get_article_metadata` + `get_full_text_article`) | Q141K x ULT response, oral uricase trials, intestinal urate kinetics, ABCG2 transporter Vmax/Km |
| ClinicalTrials.gov + WebSearch | ALLN-346 (NCT04987242 / NCT04987294 — Study 201/202) trial design + per-arm SUA reductions; PRX-115 IND + Phase 1 results |
| WebSearch | Trade-press / SEC filings for Allena Pharmaceuticals + Protalix BioTherapeutics |
| ChiCTR (via WebSearch) | Any China-registered oral-uricase-class trial in hyperuricemic Asian cohorts (Q141K-enriched populations) |
| GWAS Catalog / dbSNP / 1000 Genomes (via WebSearch citations) | Q141K allele frequency by ancestry |

## Targeted queries (keywords)

- `ABCG2 Q141K rs2231142 allopurinol response`
- `ABCG2 Q141K febuxostat response gout` (no hits → confirms gap)
- `ABCG2 Q141K Mendelian randomization serum urate`
- `ABCG2 dysfunction extra-renal urate excretion Ichida` (Matsuo / Ichida group, the Japanese functional-classification line)
- `intestinal urate secretion ABCG2 polymorphism human` → Miyazaki 2025 (the load-bearing direct-measurement paper)
- `ABCG2 urate transport Vmax Km Matsuo functional` → Nakayama 2011 transporter kinetics
- `ALLN-346 uricase` → Pierzynowska 2020 mouse paper (PMID 33330529); plus EULAR / Allena press releases for human data
- `PRX-115 Protalix` → not PubMed-indexed; ACR 2024 abstract + Protalix 2025 SEC filings
- `Aspergillus flavus uricase Km kcat` → enzyme kinetic priors for the flux model

## Pre-commit verification gate (CLAUDE.md Rule 4)

Every load-bearing number propagated into the wiki (effect size, allele frequency, Km, Vmax, sample size, p-value) is grep-verified against its primary-source full text or a directly-quoted snippet from the source paper. Where the verification tier is snippet-not-line-anchored (e.g., a press release or an abstract), the wiki page flags the verification level explicitly.

## Translation cross-check

For non-English sources (any China- or Japan-language clinical-trial protocols or post-marketing reports), translate with two independent models per CLAUDE.md §"Translation protocol." This run did not surface any non-English-source load-bearing claims that drove a verdict, so the two-model cross-check did not trigger.

## What this query will NOT find (operational scoping)

- An RCT of oral uricase pre-stratified by Q141K genotype. **Does not exist.** ALLN-346 Phase 2a Studies 201 and 202 did not report ABCG2 stratification; PRX-115 Phase 1 (n=64) did not pre-specify genotype.
- A direct human flux measurement of ΔSUA per gut-lumen uricase activity unit. **Does not exist.** The direct-flux datapoint (Miyazaki 2025) measured intestinal urate secretion in pg/µL/5min stratified by ABCG2 functional class, but did not pair it with luminal uricase to compute ΔSUA. This is exactly the gap Phase B's flux model fills computationally.
