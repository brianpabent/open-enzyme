# comp-016 Provenance

Literature mining run: 2026-05-07.
Method: WebSearch (Google + Bing-style result aggregation through the Claude WebSearch tool) + WebFetch attempts to PMC/journal pages (mostly 403-blocked; abstracts pulled via WebSearch result summaries).

## Search queries used (chronological)

1. `testosterone DHT intestinal ABCG2 expression castration orchiectomy rodent gut tissue mRNA protein`
2. `sex difference intestinal ABCG2 expression human male female biopsy duodenum jejunum`
3. `androgen ABCG2 BCRP renal kidney intestine sex hormone regulation tissue compartment`
4. `androgen deprivation therapy ADT prostate cancer urate uric acid serum gout`
5. `androgen receptor ABCG2 BCRP transcriptional regulation promoter molecular mechanism`
6. `testosterone intestinal urate excretion gut secretion fecal urate sex difference`
7. `"Sakamoto" "androgen deprivation" "urate" 2018 PLOS retrospective abstract`
8. `"Effect of Sex Hormones on the ABCG2 Transport Protein in Caco-2 Cells" Klyushova testosterone progesterone`
9. `"sex differences" "ABCG2" intestinal expression mouse rat male female kidney protein quantification`
10. `"transgender" testosterone gender-affirming "uric acid" "urate" cohort longitudinal`
11. `"ABCG2" sex difference intestine human Drozdzik proteomics protein abundance multidrug transporter`
12. `"Tanaka" "Bcrp" "Abcg2" "tissue distribution" "hormonal regulation" rats mice testosterone estrogen 2005`
13. `"hepatic" ABCG2 testosterone induce upregulate male mice female castration replacement`
14. `"intestinal" ABCG2 mRNA testosterone DHT in vivo upregulate downregulate male mice castration`
15. `Hoque Halperin Kuhns Woodward Q140K ABCG2 mouse intestinal expression protein male female magnitude`
16. `"Yu" 2021 "estradiol" intestinal ABCG2 hyperuricemia "ovariectomy" male mice fold change Western blot magnitude`
17. `"Hoque" 2020 ABCG2 Q140K intestinal expression male female "ileum" protein abundance baseline wild-type`
18. `"sex differences in urate handling" review 2020 2021 testosterone ABCG2 intestinal Halperin Asplin`
19. `"androgen response element" ABCG2 BCRP promoter ChIP direct binding sequence analysis`
20. `"Naud" 2007 "Gender differences" ABCG2 efflux bile acid 5/6 nephrectomy intestine kidney rat male female`
21. `"intestinal ABCG2" "does not differ" OR "no sex difference" review human male female`
22. `"Yahyaoui" 2008 testosterone female-to-male transgender uric acid fractional excretion mechanism URAT1 ABCG2`
23. `"Closing the Gaps" ABCG2 intestinal expression P-glycoprotein BCRP rat male female full scan`

## Tools and access notes

- **WebSearch:** all queries above ran 2026-05-07. Returned abstract-level summaries from PubMed, PMC, journal landing pages, and aggregator sites.
- **WebFetch:** repeatedly 403-blocked from PMC, PubMed, ScienceDirect, Springer, Frontiers, PLOS, MDPI, journals.physiology.org, doi.org redirects. Curl from sandbox blocked by host-allowlist.
- **Effect on rigor:** all primary-literature claims are abstract-level + WebSearch-summary-level, NOT full-text grep-verified per CLAUDE.md Rule 4 / `wiki/manual-literature-mining.md`. Numerical claims (e.g., "−0.66 mg/dL urate at 6 months ADT" from Sakamoto 2018; "88% intestinal ABCG2 protein loss in male Q140K homozygotes" from Hoque 2020) are taken from search-summary abstracts of the published paper, not from grep-verification of the paper's text. Treat all numbers as "summary-tier verified" not "primary-source verified." This is acknowledged in the limitations section of the wiki page.

## What's NOT in this scan (deliberate gaps)

- **CNKI / J-STAGE / KISS multilingual searches** — per CLAUDE.md global-multilingual default, Chinese/Japanese/Korean databases should have been queried for testosterone × intestinal ABCG2 literature. Not done in this 60-90 minute time-budget run; flagged as a Phase 2 follow-up. Likelihood-of-finding-something-new is uncertain — the field is dominated by the Western pharma-DMPK and rheumatology literature for ABCG2 specifically. Some Chinese-language gout/TCM literature touches on ABCG2 indirectly (per comp-014, Ganoderma 2,4-DAE in Fitoterapia 2022 reduces SUA via XO + URAT1; ABCG2 not directly probed in those).
- **Direct paper full-text reads** — blocked by WebFetch 403. A future run with Paperclip MCP (per `wiki/manual-literature-mining.md`) could pull full-text content.lines for grep-verification of the specific magnitudes cited (especially the Hoque 2020 88% intestinal protein loss number and the Sakamoto 2018 mg/dL figures).

## Translation cross-check

Not triggered. All sources surfaced were English-language.

## Provenance summary

| Study | Source | Confidence in extraction |
|---|---|---|
| S01 Hoque 2020 (NatComms) | PMC summary via WebSearch result text | MEDIUM — magnitude figures (88%, 53%, 44%) from search-result abstract summary; not grep-verified against paper text |
| S02 Sakamoto 2018 (PLOS One) | WebSearch result text | MEDIUM — magnitude (−0.66 mg/dL) from abstract |
| S03 Yu 2021 (Nutr Metab) | WebSearch result text | MEDIUM — direction confirmed; specific fold-change not extracted |
| S04 Klyushova 2023 (Biochem Moscow) | WebSearch result text | MEDIUM — direction confirmed |
| S05 Tanaka 2005 (BBRC) | WebSearch result text | MEDIUM |
| S06 Naud 2008 (DMD) | WebSearch result text | MEDIUM |
| S07 Jeong 2015 (BBA) | WebSearch result text | MEDIUM |
| S08 Yahyaoui 2008 (JCEM) | WebSearch result text | MEDIUM — direction confirmed; FEUA specifics extracted |
| S09 Halperin Kuhns 2020 review (IJMS) | WebSearch result text | MEDIUM |
| S10 MacLean 2008 (JPET) | WebSearch result text | MEDIUM — null finding directionally clear |
| S11 Drozdzik 2014 (Mol Pharm) | WebSearch result text | MEDIUM |
| S12 Hosoyamada 2010 | WebSearch result text + cross-ref to wiki/androgen-urate-axis.md | HIGH (already in wiki) |
| S13 Takiue 2011 | WebSearch result text + cross-ref to wiki/androgen-urate-axis.md | HIGH (already in wiki) |
| S14 Hak Choi 2008 NHANES | WebSearch result text + cross-ref to wiki/androgen-urate-axis.md | HIGH (already in wiki) |
| S15 KNIGHT/ENIGI cohorts | WebSearch result text | LOW — recent, abstract only |
| S16 Adolescent boys 2021 | WebSearch result text | MEDIUM |
| S17 Halperin Kuhns FASEB abstract | WebSearch result text | MEDIUM (abstract-stage publication) |
