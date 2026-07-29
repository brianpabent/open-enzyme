# COMP-016 provenance

## Original inventory collection

- Date: 2026-05-07.
- Method recorded by the original run: Google/Bing-style web search through an
  agent search tool, with direct publisher and PubMed fetch attempts.
- Access limitation: many direct fetches returned HTTP 403 or host-allowlist
  failures. Most original rows were therefore extracted from search summaries
  or abstracts rather than primary full text.
- Consequence: the old narrative and quantitative fields are not retained as
  evidence in the repaired input unless a later source verification named
  below supports them.

### Exact original queries

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

## Source-correction record

The following corrections were independently source-checked during COMP-017 on
2026-07-27. COMP-016 carries only the bounded findings needed to classify the
old inventory.

### Hoque et al. 2020

- DOI `10.1038/s41467-020-16525-w`; PMID `32488095`; PMCID `PMC7265540`.
- Verified against the Nature article HTML, Europe PMC XML, version-of-record
  PDF, supplementary PDF, and publisher source-data workbook.
- The like-for-like Western-blot result is 78% lower jejunal ABCG2 in
  Q140K+/+ versus WT mice (WT n=8; Q140K+/+ n=6; p=0.0046), compared with a
  44% renal reduction.
- Neither 53% nor 88% is supported by the article representations or source
  workbook. Those old COMP-016 numbers are excluded.

### Liu et al. 2021

- DOI `10.1186/s12986-021-00583-y`; PMID `34144706`; PMCID `PMC8212495`.
- Authors: Lei Liu, Tianyi Zhao, Lizhen Shan, Ling Cao, Xiaoxia Zhu, Yu Xue.
- Verified against Europe PMC primary full-text XML.
- In Caco-2 cells, nominal 100 µM estradiol benzoate increased ABCG2 mRNA at
  48 hours without a dose-dependent response; 50 µM LY294002 partially
  blocked that response (p<0.05).
- This is an in-vitro pharmacological condition, not a physiological
  intestinal effect size and not an androgen test.

### Slepnev et al. 2023

- English DOI `10.1134/S1990747823050100`; Russian-original DOI
  `10.31857/S0233475523050109`.
- Authors: A. A. Slepnev, Yu. V. Abalenikhina, N. M. Popova,
  A. V. Shchulkin, E. N. Yakusheva. The old Klyushova attribution is wrong.
- Verified against the official publisher-supplied English abstract.
- Nominal 1, 10, and 100 µM testosterone, estradiol, or progesterone increased
  Caco-2 ABCG2 after 24 hours. PXR/FXR inhibitor conditions reduced the
  testosterone-associated increase, which remained above control.
- The abstract does not establish free-tissue exposure, a physiological
  testosterone effect, or exclusion of androgen-receptor involvement.

### MacLean et al. 2008

- DOI `10.1124/dmd.108.020859`; PMID `18378562`.
- Authors: C. MacLean, U. Moenning, A. Reichel, G. Fricker.
- Verified against the primary PubMed abstract.
- The rat qRT-PCR/Western intestinal scan reported no sex-specific transporter
  expression difference. This is an Animal Model qualitative null, not a
  healthy-human estimate.

## Repaired extraction policy

- `primary_full_text`: claim checked against the primary full text.
- `official_publisher_abstract`: claim checked against the publisher-supplied
  abstract and metadata; no unstated full-text detail is used.
- `primary_database_abstract`: claim checked against a primary bibliographic
  database abstract.
- `legacy_search_summary`: citation remains in the fixed inventory, but the
  repaired artifact emits no quantitative or mechanistic finding from it.
- `unresolved_legacy_placeholder`: original row lacked a stable citable
  identity and cannot contribute evidence.

## Scope not searched

The original run did not execute the project’s current multilingual protocol
across CNKI/WanFang, J-STAGE/CiNii/J-GLOBAL, KISS/RISS, eLIBRARY.RU, TIB/GND,
or SciELO. The fixed-inventory result therefore cannot be read as an exhaustive
literature absence. A multilingual refresh would require a new reviewed scan
and, if made executable, a new COMP lifecycle.

## Translation status

No non-English source text was translated in the original run. Slepnev 2023 is
retained only at the official publisher-supplied English-abstract tier. Any
future use of Russian full text requires the project’s independent
two-translation protocol.
