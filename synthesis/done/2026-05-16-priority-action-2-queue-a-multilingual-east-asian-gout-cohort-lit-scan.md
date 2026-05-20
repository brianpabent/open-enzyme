---
type: priority-action
sweep_date: 2026-05-16
sweep_sha: 91acf49
section_index: 2
global_index: 15
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Queue a multilingual East Asian gout-cohort lit scan subagent task.

2. **Queue a multilingual East Asian gout-cohort lit scan subagent task.** Scope: CNKI, WanFang, J-STAGE, CiNii. Targets: ABCG2 Q141K (rs2231142) allele frequency + gout association in Chinese, Japanese, Korean cohorts; URAT1 W258X (rs121907892) frequency + RHUC1 phenotype data; HLA-B*58:01 frequency + allopurinol-SCAR association; any Q141K-stratified intervention response data (allopurinol, febuxostat, fiber/butyrate) not in the English-language corpus. Output: updated allele frequency ranges and intervention-response evidence for `gout-genetic-variants.md` Categories 1 and 6. Cost: $0, ~1–2 hours. This is a direct operationalization of CLAUDE.md's global-multilingual research default rule and closes the single largest population coverage gap in the platform's personalized-medicine thesis.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is a concrete operationalization of two existing corpus commitments: the multilingual-default rule in `CLAUDE.md` and the ancestry-stratified variant index in `gout-genetic-variants.md`. The task is cheap, likely to improve Q141K/HLA-B*58:01/URAT1 W258X frequency estimates, and directly affects pharmacogenomic recruitment and exclusion criteria.

---

**WALKED 2026-05-19 — Closed (subagent executed; 5 load-bearing findings propagated).**

Actioned:
- ✓ Fired multilingual lit scan subagent during walkthrough. Output: `logs/multilingual-east-asian-gout-cohort-scan-2026-05-19.md`. ~45 min wall time, 11 primary-source PMID anchors per CLAUDE.md Rule 4.
- ✓ Propagated 9 wiki edits to `gout-genetic-variants.md` (Categories 1, 6, Open Questions) + 1 dose-ceiling subsection to `sirna-urat1-modality.md`:
  - **Q141K row:** Han Chinese gout-cohort enrichment 49.6% vs 30.9% controls (Zhang 2014); Pacific Islander vs Māori ancestry split (Phipps-Green 2010 OR 2.80 vs 1.08); Q141K → allopurinol-failure stratifier (Wen 2018 OR 2.43, Roberts 2017 p=8×10⁻¹¹); Q141K NOT a febuxostat stratifier (Stamp 2018); febuxostat-first as rational default for Q141K+ East Asian patients.
  - **W258X row:** Japanese MAF 2.34–2.55% across 5 cohorts (~31,000 pooled); Korean 1.4% with 8.1% SUA-variance load (Park 2020); Roma RHUC1 via different mutations; Polynesian gap explicit; homozygote SUA = 0.75 mg/dL anchor (Sakiyama 2021 n=30,685); ≤50% siRNA knockdown ceiling.
  - **HLA-B\*58:01 row:** sub-population granularity (3× range Japanese ~6% to Taiwanese ~20% carrier); universal screening implementation (Taiwan, Korea, Thailand, Hong Kong March 2023 per Yi 2025); Taiwan cohort efficacy (zero SCAR in negative arm vs ~7 expected, p=0.0026).
  - **Multi-source disagreement footnote:** updated with new sub-population spread + febuxostat-substitution residual-uncertainty flag.
  - **Open Questions:** new items 7 (Q141K × fiber RCT empirical gap), 8 (W258X homozygote lifetime EI-AKI risk), 9 (HLA-B\*58:01-positive febuxostat prospective safety cohort); old item 7 renumbered to 10 with CNKI / WanFang / J-STAGE / CiNii credential gap explicit.
  - **`sirna-urat1-modality.md`:** new "Dose-ceiling constraint from W258X homozygote phenotype" subsection encoding the ≤50% knockdown ceiling.

**Clinically actionable finding worth surfacing forward:** Q141K is a replicated allopurinol-failure stratifier but NOT a febuxostat stratifier. In Q141K+ East Asian patients (≥50% of Han Chinese gout patients), febuxostat is rational first-line, not allopurinol — inverts the global standard-of-care default for the largest single gout-genotype subgroup.

**Honest scan limitations carried into new Open Question 10:** direct CNKI / WanFang / J-STAGE / CiNii required authenticated browser sessions not available to subagent. Two-model translation protocol not exercised (no non-English citations were load-bearing). Regional sub-cohort breakdowns and TCM-context intervention studies likely remain untranslated and unsearched.

Also closes:
- 2026-05-16 experiment-2 (same multilingual lit scan task, experiment-card form).
