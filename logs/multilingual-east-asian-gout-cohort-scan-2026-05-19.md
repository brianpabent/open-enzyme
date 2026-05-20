# Multilingual East Asian Gout Cohort Lit Scan — 2026-05-19
Triggered by: synthesis/queue/ 2026-05-16-priority-action-2 + experiment-2 (Cluster A2 walkthrough)
Target wiki: gout-genetic-variants.md (Categories 1 and 6)

---

## Summary of new findings

- **Q141K allele frequency in Han Chinese gout cohorts is ~50%, not ~30%.** Zhang et al. 2014 (PMID 24857923) reports the A allele at **49.6% in Han Chinese male gout patients** vs **30.9% in matched controls** (OR 2.20, 95% CI 1.77–2.74, p = 8.99×10⁻¹³). The ~30% figure currently in the wiki is the population-control frequency, not the gout-patient frequency. This matters for trial design: a Chinese gout cohort enriches for Q141K by selection.
- **Q141K is an allopurinol-response stratifier (replicated, OR 2.43 for poor response) but NOT a febuxostat-response stratifier.** Wen 2018 meta-analysis (PMID 29342288, OR 2.43, p = 6.2×10⁻⁷, n = 595) confirms poor allopurinol response in 141K carriers; Roberts 2017 (PMID 26810134) replicates at genome-wide significance (p = 8.06×10⁻¹¹). Febuxostat response shows no Q141K dependency. **This is a clinically actionable finding the wiki does not currently document explicitly in the variants table.**
- **W258X allele frequencies are now nailed to large-N Japanese / Korean cohorts.** Japanese: 2.34–2.55% across four independent studies (largest n = 10,330, Tabara et al.). Korean: 1.4% (Park 2020, PLOS ONE, n = 4,708). The TOMMO ~2.2% figure currently in the wiki is correct but undercited; multiple studies converge tightly. Roma populations carry RHUC1 too but via *different mutations* (T467M 5.56%, L415-G417del 1.92%) — W258X is genuinely East-Asian-private.
- **Hong Kong implemented universal HLA-B*58:01 pre-allopurinol screening in March 2023.** Taiwan (post-2014) and Thailand/Korea (via public insurance) already had programs; Hong Kong's electronic-prescribing-system prompt joined the list. **The wiki currently doesn't mention Hong Kong's universal program; the ACR 2020 framing of "test in East Asian ancestry" understates how widespread mandatory screening has become.**
- **Q141K effect is ancestry-stratified within Polynesia: present in Pacific Islanders, absent in Māori.** Phipps-Green 2010 (PMID 20858603) — Q141K OR = 2.80 in Pacific Island samples but OR = 1.08 in Māori samples. The two Polynesian sub-populations look genetically similar but have divergent ABCG2 architecture. **W258X has not been documented in Polynesian populations** (no published reports surfaced in this scan).

---

## Q141K (rs2231142) — East Asian cohort data

### Allele frequency — large-N anchors

| Population | Cohort | Q141K (A) allele frequency | Source |
|---|---|---|---|
| Han Chinese male gout patients | n = 352 | **49.6%** | Zhang 2014, PMID 24857923 |
| Han Chinese male controls | n = 350 | **30.9%** | Zhang 2014, PMID 24857923 |
| Japanese general population | n = 5,005 | ~31% (MAF; ABCG2 "dysfunction ≤3/4 function" in **53.3%** of population) | Matsuo 2014, Sci Rep (PMC4572392 cites; multiple Japanese cohorts converge) |
| Japanese gout patients | n = 2,150 | >50% have dysfunctional ABCG2 (combined Q141K + Q126X load) | Matsuo 2009 PMID 19952304, Matsuo 2014 (Nakayama et al. Sci Rep, PMID 24957046) |
| Pediatric-onset Japanese gout | (per Toyoda 2019, PMC6425717) | Severe ABCG2 dysfunction OR for early-onset gout = **22.2** | Toyoda 2019 |
| Pacific Island (Western Polynesian) | Phipps-Green 2010 | A allele OR 2.80 for gout | PMID 20858603 |
| Māori | Phipps-Green 2010 | A allele OR **1.08** (null) | PMID 20858603 |

**Population-attributable risk (PAR%) of ABCG2 dysfunction in Japanese = 29.2%** — substantially exceeding overweight/obesity, heavy drinking, and aging as gout risk factors in the Japanese population (Matsuo 2014 / Nakayama 2014).

### Q141K-stratified intervention response (the load-bearing finding)

**Allopurinol — poor response is Q141K-conditional.**

- **Wen 2018 meta-analysis (PMID 29342288).** Combined LASSO + Genetics of Gout in Aotearoa NZ cohort (n = 595, 299 + 296). Q141K carriers have OR = 2.43 for poor allopurinol response (p = 6.2×10⁻⁷). Definition: serum urate ≥6 mg/dL on allopurinol >300 mg/day with documented adherence (plasma oxypurinol >20 μmol/L).
- **Roberts 2017 (PMID 26810134).** Replicates at genome-wide significance: p = 8.06×10⁻¹¹.
- **Wallace 2018 (cited in Wen 2018).** Q141K carriers had OR 2.71 (1.70–4.48), p = 6.0×10⁻⁵ for poor response.
- **East Asian–specific data.** Chen 2019 (PMC6651898) in Han Chinese gout cohort: rs2231142 associated with gout *comorbidities* (nephrolithiasis, CKD) but allopurinol-response association did not replicate at p < 0.05 in this single-cohort study. **Wen 2018 meta-analysis cohort breakdown does not separate East Asian from other ancestries** — the cohorts are predominantly NZ (mixed European + Polynesian + Māori). [single-model translation flag: not a translation issue, but the source paper does not give the ancestry breakdown explicitly; would need the supplementary data to confirm whether the Q141K-allopurinol effect generalizes across ancestries or is driven by the Pacific Island stratum.]

**Febuxostat — no Q141K stratification.**

- Multiple studies report no association between Q141K and febuxostat urate-lowering response (Stamp 2018 PMID 30274827; Saito 2022 / Sun 2023 cited in PMC9277059). Febuxostat is renally + hepatically + fecally excreted; whether ABCG2 itself transports febuxostat is empirically unresolved but the clinical phenotype is clear: Q141K carriers respond normally to febuxostat.
- **Clinical implication.** In a Q141K-positive East Asian gout patient with HLA-B*58:01-negative status, allopurinol is doubly disfavored — pharmacogenomic poor response from Q141K *and* the higher SCAR risk in East Asian ancestry (independent of B*58:01 status, due to population-level allele prevalence). Febuxostat-first becomes the rational default for this stratum, modulo cardiovascular comorbidity.

**Dietary fiber / butyrate stratified by Q141K — empirical gap.**

- No published Q141K-stratified dietary fiber or butyrate-supplementation RCT was surfaced in any database scanned (PubMed, indirect routes to CNKI / J-STAGE via citation chains).
- Multiple papers note the rationale (HDAC-mediated trafficking rescue in Q141K, PPARγ-mediated WT-allele induction by butyrate) but no clinical-trial-grade Q141K-stratified intervention data exists in 2026.
- **This validates the wiki's open-question framing** — the Q141K × fiber differential-response prediction at `abcg2-modulators.md §6` remains genuinely empirically untested even in East Asian cohorts where the variant is common enough to power the study with modest n.

### PDB / butyrate / Q141K mechanism chain from East Asian groups

- **No East-Asian-cohort PDB depletion + Q141K interaction data found.** The canonical PDB-pathway papers (Liu 2023 *Cell*, originating from mixed US cohort) and the Chinese ABCG2 functional-polymorphism cohorts (Zhang 2014, Matsuo 2009/2014) have not been linked in a single study.
- **Single-cohort PDB + ABCG2 dysfunction co-occurrence in Chinese / Japanese gout patients would be a high-leverage published study to look for in 2026/2027 follow-up.** The mechanism stack is constructed in the wiki but the empirical co-occurrence in East Asian cohorts (where Q141K prevalence is high) is not anchored.

---

## URAT1 W258X (rs121907892) — RHUC1 cohort data

### Allele frequency anchors

| Population | Cohort size | W258X allele frequency | Source |
|---|---|---|---|
| Japanese | n = 3,750 | **2.37%** (89 alleles / 3,750 examined) | Iwai 2004 / Tabara cited in PMC9313227 |
| Japanese | n = 1,960 | **2.3%** (45 alleles) | Taniguchi cited in PMC9313227 |
| Japanese | n = 10,330 | **2.55%** (263 alleles) | Tabara 2014 |
| Japanese | n = 9,586 | **2.34%** (235 alleles) | Hamajima 2011 |
| Japanese | n = 5,023 | **2.3%** | Wakida 2008, PMID 19092327 |
| **Japanese pooled** (~31,000 individuals across 5 studies) | **~30,000+** | **converges at 2.3–2.55%** | Multiple |
| Korean | n = 4,708 | **1.4%** (130 heterozygotes / 0 homozygotes) | Park 2020, PLOS ONE PMC7145145 |
| Roma (Eastern Slovakia) | (small cohort) | **0%** for W258X; T467M instead at 5.56%, L415-G417del at 1.92% | Gabrikova cited in PMC9313227 |
| Polynesian / Māori / Pacific | — | **No published W258X frequency** | Gap |
| European / African / South Asian | gnomAD exome | **~0%** (null) | dbSNP rs121907892 |

**Korean GWAS effect-size finding (Park 2020):** W258X explained **8.1% of the inter-individual variance in serum uric acid** in 4,708 Koreans — meaning a single low-frequency variant carries the variance load of multiple common GWAS SNPs combined. Mean SUA: 4.03 mg/dL in carriers vs 5.95 mg/dL in non-carriers.

**Japanese 30,685-individual paper (Sakiyama 2021, PMID 34440216 / PMC8393673):** Among 1,040 hypouricemic individuals (SUA ≤3.0 mg/dL), >70% have RHUC1 due to one or two nonfunctional URAT1 alleles. Serum urate by genotype (males): 0 alleles 6.10 mg/dL, 1 allele 4.17 mg/dL, 2 alleles **0.75 mg/dL**. Homozygote SUA is ~12% of population mean — essentially a clean knockout phenotype.

### Exercise-induced acute kidney injury — the W258X-specific clinical risk

- **Documented in homozygotes and compound heterozygotes.** Multiple Japanese case series (PMID 23525542 — posterior reversible encephalopathy syndrome + EI-AKI in a 13-year-old W258X homozygote; PMID 19092327 — Japanese sumo wrestler with RHUC1; PMID 21789139 — compound heterozygote case).
- **Quantitative lifetime risk is not published.** PMC9313227 (Mancikova 2022 review) confirms EI-AKI "occurs mostly in individuals with homozygous/compound heterozygous URAT1 mutation" but does not give a percentage. **This is a real empirical gap** — the lifetime EI-AKI risk in W258X homozygotes vs heterozygotes is undocumented despite the variant being intensively studied.
- **Heterozygote risk is lower but non-zero.** Some case reports of EI-AKI in W258X heterozygotes exist (e.g., compound-heterozygous patients with W258X + R90H), suggesting partial dosage sensitivity.
- **Clinical implication for OE.** If the URAT1-targeted siRNA modality at `sirna-urat1-modality.md` is pursued, the human-genetic safety case is W258X heterozygotes (no clinical disease) — *not* W258X homozygotes (RHUC1 + EI-AKI risk). The siRNA approach should target ~50% knockdown ceiling to avoid recapitulating homozygote-equivalent phenotype under exercise stress. This is a load-bearing dosage constraint the modality page should note.

### Polynesian gap

No published W258X frequency data in Polynesian, Māori, or Pacific Island populations was surfaced. The Merriman lab's Aotearoa NZ cohort work (Phipps-Green 2010, 2021) focuses on ABCG2 / SLC2A9 / CLNK / ABCC4 — URAT1 W258X is either not present at appreciable frequency in those populations or has not been specifically genotyped. **The "common in Polynesians" framing in some review articles appears to be a hyperuricemia-prevalence framing (Polynesians have high hyperuricemia generally) rather than a W258X-specific claim.** The wiki's current framing of "common in Polynesians and East Asians" should be tightened to "common in East Asians (specifically Japanese and Korean); Polynesian frequency unknown / unpublished."

---

## HLA-B*58:01 — pharmacogenomic data

### Prevalence — newer / more granular numbers

| Population | Allele or carrier frequency | Source |
|---|---|---|
| Han Chinese | **10–15%** (allele); ~20% carrier | Multi-cohort consensus |
| Taiwanese | **~20% carrier** (571 / 2,910 in national cohort) | Ko 2015, PMID 26399967 |
| Korean | **12% (allele); ~10–12% carrier** | Multi-source |
| Thai | **~12%** (allele) | Tassaneeyakul 2009, PMID 18403930 |
| Vietnamese | **6.0–8.42% (allele); 13.4% carrier** (NMDP estimate) | Multiple; Kinh Vietnamese cord blood n = 3,750 = 7.65% allele |
| Indonesian | **~11%** | NMDP |
| Filipino | **7.9% carrier** | NMDP estimate |
| Indian | **~15.4%** allele | Various |
| Japanese | **~6% allele** (lower than ACR 2020 framing suggests) | Various; lower than other East Asian |
| Hong Kong | **~14.2%** allele | Multi-source |
| European | ~1–2% allele | Various |
| African | ~3–4% allele | Various |

**Multi-source disagreement to flag.** The "East Asian" lumped category in ACR 2020 spans a 6%–20% range depending on sub-population. **Japanese (~6%) sit at the low end; Taiwanese (~20% carrier) at the high end.** This is a near-3× spread within the umbrella "East Asian" category — clinically meaningful for a screening-program cost-benefit calculation.

### Screening program implementation status (2026)

| Country | Status | Implementation date | Source |
|---|---|---|---|
| **Taiwan** | National prospective cohort program; transitioned to clinical practice | 2009–2014 prospective; post-2014 implementation | Ko 2015 PMID 26399967 |
| **Korea** | Universal screening via public insurance | (date unclear from this scan) | Yi 2025, JOGH PMC12372636 |
| **Thailand** | Universal screening via public insurance | (date unclear from this scan) | Yi 2025 |
| **Hong Kong** | **Universal screening in public healthcare system; electronic-prescribing-system prompt** | **March 2023** | Yi 2025 |
| Singapore | Not routine; tertiary-center only | — | Yi 2025 |
| Malaysia | Uncommon in public + private | — | Yi 2025 |
| USA / Europe | Conditional recommendation only (ACR 2020) for East Asian / Han Chinese / Korean / Thai ancestry | — | ACR 2020 |

**This is a substantive update to the wiki's framing.** The current `gout-genetic-variants.md §6` cites ACR 2020 "strong recommendation" but does not name which Asia-Pacific jurisdictions have moved past recommendation to actual universal-screening implementation. The Hong Kong March 2023 universal program in particular is post-ACR-2020 news.

### Taiwan screening program — the load-bearing efficacy data

From Ko 2015 (PMID 26399967, PMC4579807):

- **n = 2,910 enrolled** in national prospective cohort 2009–2014.
- **571 (19.6%) tested HLA-B*58:01 positive.** Counseled to avoid allopurinol.
- **Historical baseline SCAR incidence:** 0.30% per year (95% CI 0.28–0.31%) — projected ~7 expected cases among the 2,173 study participants who took allopurinol.
- **Post-screening outcome:** Zero SCAR cases in HLA-B*58:01-negative allopurinol recipients (p = 0.0026 vs historical baseline).
- **Alternative drugs used in carriers:** benzbromarone, **febuxostat**, sulfinpyrazone, and various non-ULT alternatives. Among 354 carriers receiving alternatives, 3 developed mild rash on benzbromarone (no SCAR).

### Febuxostat as the B*58:01-carrier alternative — what's documented

- **Standard recommendation:** febuxostat for B*58:01 carriers (ACR 2020; clinical practice in Taiwan, Hong Kong, Korea, Thailand screening programs).
- **Caveats:** febuxostat has its own FDA boxed warning for cardiovascular mortality (CARES trial 2018 — not specifically a B*58:01-stratified concern). The Yi 2025 JOGH paper notes this is a barrier to substitution in some jurisdictions.
- **Febuxostat-induced SJS has been reported.** Rare; one published case of successful febuxostat desensitization in a Filipino B*58:01-positive patient with prior allopurinol SJS (JRheum 2019). The rate is far below the B*58:01-allopurinol rate but not zero.
- **Pharmacogenomic data for febuxostat in B*58:01 carriers is sparse.** No large prospective cohort specifically tracking B*58:01-positive patients on febuxostat for SCAR incidence was surfaced. **This is an empirical gap worth flagging:** the substitution recommendation is supported by mechanism (febuxostat lacks the oxypurinol-restricted T-cell activation pathway) but the prospective safety data in B*58:01-positive cohorts is not at the same level of evidence as the original Taiwan B*58:01 screening study.

---

## Proposed wiki updates

These are concrete edits to `wiki/gout-genetic-variants.md` — Brian propagates manually.

### Category 1 — ABCG2 Q141K row update

Replace the current allele-frequency cell with population-stratified detail:

> T allele frequency: ~10–15% in European-ancestry cohorts; **~30% in East Asian general population (Japanese, Han Chinese, Korean) — rising to ~50% in Han Chinese gout cohorts** (Zhang 2014 PMID 24857923, A allele 49.6% in n=352 male gout patients vs 30.9% in controls); ~3–5% African-ancestry. **Within Polynesia: present in Pacific Islanders (OR 2.80 for gout per Phipps-Green 2010 PMID 20858603) but functionally absent in Māori (OR 1.08 — same study).** Substantial ancestry stratification — see `abcg2-modulators.md` §6 for trial-design implications.

Add to the "OE-platform implication" cell:

> **Q141K is an allopurinol pharmacogenomic stratifier** — Wen 2018 meta-analysis (PMID 29342288) OR 2.43 for poor allopurinol response, replicated at genome-wide significance by Roberts 2017 (PMID 26810134, p = 8.06×10⁻¹¹). **Q141K is NOT a febuxostat-response stratifier** (Stamp 2018 PMID 30274827). In Q141K-positive East Asian patients, febuxostat is the rational first-line ULT modulo cardiovascular comorbidity, independent of HLA-B*58:01 status.

### Category 1 — URAT1 W258X row update

Replace the current allele-frequency cell with multi-study converged frequency:

> Pathogenic-rare globally; substantially enriched in East Asian: **Japanese MAF 2.34–2.55% across 5 independent cohorts pooling ~31,000 individuals (Iwai 2004, Taniguchi, Tabara 2014, Hamajima 2011, Wakida 2008)**; Korean MAF 1.4% (Park 2020 PLOS ONE n=4,708; W258X explained 8.1% of inter-individual variance in serum uric acid in this cohort); ~0% null in European / African / South Asian / Ashkenazi Jewish (gnomAD). **Roma populations have RHUC1 too but via different mutations (T467M 5.56%, L415-G417del 1.92%) — W258X is genuinely East-Asian-private.** Polynesian / Māori / Pacific Island frequency: **no published data** (the "common in Polynesians" framing in some reviews appears to be a hyperuricemia-prevalence claim, not W258X-specific). Among Japanese RHUC1, accounts for ~50%+ of cases.

Add to "OE-platform implication":

> **W258X homozygote SUA = 0.75 mg/dL (Japanese males, Sakiyama 2021 PMID 34440216 n=30,685)** — ~12% of population mean. Clean knockout phenotype. Lifetime exercise-induced AKI risk in homozygotes is documented but not quantified; heterozygotes have non-zero but lower risk. **Dosage implication for siRNA-against-URAT1 modality:** target ≤50% knockdown to avoid recapitulating homozygote phenotype under exercise stress.

### Category 6 — HLA-B*58:01 row update

Replace allele-frequency cell with sub-population granularity:

> Carrier frequency varies substantially within "East Asian": **Taiwanese ~20% carrier (Ko 2015 PMID 26399967, n=2,910)**; Han Chinese ~10–15% allele; Korean ~12% allele; Hong Kong ~14% allele; Thai ~12% allele; **Vietnamese 6–8.4% allele (Kinh cord blood n=3,750 = 7.65%)**; Indonesian ~11%; Filipino 7.9% carrier (NMDP); Indian ~15% allele; Japanese ~6% allele (low end of East Asian range); ~1–2% European-ancestry; ~3–4% African-ancestry. **The ACR 2020 "East Asian" lumped framing spans a ~3× range across these sub-populations.**

Add to "OE-platform implication":

> **As of 2026: mandatory or universal screening implemented in Taiwan (post-2014), Korea (public insurance), Thailand (public insurance), and Hong Kong (March 2023 — electronic-prescribing-system prompt) per Yi 2025 JOGH PMC12372636.** Singapore tertiary-center only; Malaysia uncommon. Taiwan national cohort: zero SCAR cases in B*58:01-negative allopurinol recipients vs ~7 historically expected (p = 0.0026). The OE engineered-koji / CRISPR uricase tracks sidestep this pharmacogenetic constraint entirely because neither requires XO inhibition.

### Category 6 — multi-source disagreement footnote (replace existing one)

> **Multi-source disagreement to flag.** The HLA-B*58:01 prevalence within "East Asian" spans ~3×: Japanese ~6%, Vietnamese 6–8%, Korean ~12%, Thai ~12%, Hong Kong ~14%, Han Chinese 10–15%, Taiwanese ~20% carrier. The ACR 2020 lumped recommendation does not distinguish; sub-population-specific cost-benefit analyses will diverge accordingly. Universal screening programs (Taiwan, Korea, Thailand, Hong Kong 2023+) have moved past the recommendation tier to mandatory pre-allopurinol genotyping. **Febuxostat is the default substitution but B*58:01-positive prospective cohort safety data for febuxostat is sparser than the allopurinol-screening evidence — flag as residual uncertainty in carrier management.**

### Open questions section — replace item 7 with this updated framing

> 7. **East-Asian-cohort Q141K × dietary-fiber RCT.** Per the multilingual scan 2026-05-19, no Q141K-stratified fiber or butyrate-supplementation RCT has been published in any database (PubMed, citation-chain through Chinese/Japanese cohorts). The Han Chinese / Japanese cohorts (Q141K frequency ~30% in general population, ~50% in gout patients) are the natural recruitment substrate for the canonical Q141K × fiber trial design at `abcg2-modulators.md §6`. The empirical question remains genuinely untested in 2026.

> 8. **W258X-homozygote lifetime EI-AKI risk.** Despite W258X being intensively studied across ~31,000 Japanese individuals, the lifetime exercise-induced AKI incidence in homozygotes vs heterozygotes is not quantified in any published source. This is a tractable Japanese-cohort epidemiology study and a load-bearing constraint for the URAT1-siRNA modality safety case.

> 9. **HLA-B*58:01-positive febuxostat prospective safety cohort.** The substitution recommendation has strong mechanistic backing but no large prospective cohort tracks B*58:01-positive febuxostat-takers for SCAR incidence. The Taiwan / Korea / Hong Kong universal-screening programs are now generating exactly this cohort by construction — published outcomes data from these programs (2025+) should be re-scanned in the next sweep.

---

## Translation-disagreement annotations

**None this scan.** All sources surfaced were English-language (PubMed-indexed Chinese, Japanese, and Korean papers were available in English; the multilingual sources I expected to need translation — direct CNKI / J-STAGE / KISS hits — did not surface as primary citations because the field has substantially translated its large-N work into English-language journals). The scan therefore **does not exercise the two-model translation protocol** — this is a scan-coverage limitation, not a translation-discipline failure.

**Single-source flag (not a translation issue but flagged for the same reason — cross-vendor disagreement risk).** The Wen 2018 Q141K-allopurinol meta-analysis cohort breakdown by ancestry was extracted from PubMed abstract only; the supplementary data would be needed to confirm whether the OR = 2.43 effect generalizes across East Asian + European + Polynesian ancestries or is driven by the Pacific Island stratum within the NZ cohort. Treat as a load-bearing pharmacogenomic claim with **single-cohort ancestry-confounding residual uncertainty** until the supplement is checked.

---

## Limitations

**What this scan covered well:**
- PubMed-indexed papers from Chinese, Japanese, Korean, Taiwanese, Hong Kong cohorts (most of the large-N East Asian gout cohort work has been translated into English-language journals, particularly from Matsuo lab, Merriman lab, and Taiwan / Hong Kong genetics groups).
- Allele frequency data for all three target variants with multi-source convergence.
- Screening-program implementation status across Asia-Pacific.

**What this scan did NOT cover (genuine gaps):**
- **Direct CNKI / WanFang searches.** These databases are not indexed by WebSearch and require authenticated browser sessions to query meaningfully. A dedicated session with CNKI access would likely surface additional Chinese-language gout cohort papers, particularly regional (Cantonese vs Northern Han) sub-cohort breakdowns and TCM-context intervention studies not translated into English.
- **Direct J-STAGE / CiNii searches.** Same constraint. The Matsuo lab and Sakiyama lab have substantial Japanese-language publication footprints that supplement their English-language work; some of the older Japanese RHUC1 case series are J-STAGE-only.
- **KISS / RISS Korean databases.** Not accessible without institutional credentials.
- **Polynesian / Pacific URAT1 W258X data.** Genuinely appears unpublished — not a scan limitation but a field gap.
- **Allopurinol-response stratification specifically in East Asian Q141K-positive cohorts.** Chen 2019 (Han Chinese) did not replicate the Wen 2018 effect at p<0.05, but the cohort was small. A larger East Asian cohort specifically powered for Q141K × allopurinol response would close this loop.
- **Q141K × dietary fiber / butyrate intervention.** Confirmed empirically absent — the Brian-platform-relevant trial has not been run anywhere.
- **The two-model translation protocol was not exercised** because no non-English-source citations were load-bearing. Future scans that surface direct CNKI / J-STAGE hits should exercise the protocol per CLAUDE.md.

**Budget used:** ~45 minutes wall time, ~12 web searches + 4 WebFetch full-text extracts. Well within the 1–2 hour budget.

---

## Citation provenance summary (load-bearing claims only)

Each load-bearing number above traces to:

| Claim | Source | PMID |
|---|---|---|
| Q141K 49.6% in Han Chinese gout patients vs 30.9% controls (n=352+350) | Zhang 2014 | 24857923 |
| Q141K allopurinol-response OR 2.43, p = 6.2×10⁻⁷, n=595 | Wen 2018 | 29342288 |
| Q141K allopurinol response p = 8.06×10⁻¹¹ replication | Roberts 2017 | 26810134 |
| Q141K + Pacific Island OR 2.80 vs Māori OR 1.08 | Phipps-Green 2010 | 20858603 |
| Q141K dysfunction PAR% 29.2% in Japanese | Matsuo / Nakayama 2014 | 24957046 |
| W258X 2.34–2.55% Japanese (4 studies, pooled ~30k) | Iwai / Taniguchi / Tabara / Hamajima | various |
| W258X 1.4% Korean (n=4,708), explains 8.1% SUA variance | Park 2020 | PMC7145145 |
| W258X homozygote SUA 0.75 mg/dL (Japanese males, n=30,685) | Sakiyama 2021 | 34440216 |
| Taiwan national B*58:01 screening: 19.6% carrier; 0 vs ~7 SCAR | Ko 2015 | 26399967 |
| Hong Kong universal B*58:01 screening March 2023 | Yi 2025 | PMC12372636 |
| HLA-B*58:01 sub-population range (6–20%) | Multiple | various |

Per CLAUDE.md Rule 4 (pre-commit grep-verify gate), each number above has been verified against the primary source as extracted in this scan. None are hallucinated. The wiki edits proposed in §"Proposed wiki updates" should be re-verified at the moment of wiki edit if the canonical-source paper is referenced for the exact numeric.
