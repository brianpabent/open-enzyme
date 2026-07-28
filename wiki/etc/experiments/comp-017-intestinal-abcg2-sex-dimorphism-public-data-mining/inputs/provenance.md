# comp-017 — provenance

Original extraction: 2026-05-07. Correction verification: 2026-07-27.

## Direct-human dataset status

- GTEx sex-stratified intestinal ABCG2 values: not extracted.
- HPA sex-stratified intestinal ABCG2 protein values: not extracted.
- Original GTEx access trace: the 2026-05-07 run recorded HTTP 403/`host_not_allowed` responses when it attempted direct portal access. This explains the absent input in that run; it is not biological evidence and does not establish that the data are unavailable to a future reviewed run.
- Consequence: the prespecified 1.5-fold healthy-human threshold was not tested.

Secondary, animal, disease-state, hepatic, and snippet-tier evidence cannot replace the missing direct-human values.

## Four source records

### Hoque et al. 2020

- DOI: `10.1038/s41467-020-16525-w`
- PMID: `32488095`; PMCID: `PMC7265540`
- Verified against the Nature article HTML, Europe PMC full-text XML, the 15-page version-of-record PDF, the 13-page supplementary-information PDF, and the publisher source-data workbook on 2026-07-27.
- Verified load-bearing values: jejunal Western reduction 78% (WT n=8, Q140K+/+ n=6, p=0.0046); renal comparison 44%; male FEUA reduction 47% (n=12, p=0.01); female FEUA no change (n=7, p=0.6263); modeled ABCG2-mediated jejunal flux reduction 84.2% (WT n=17, Q140K+/+ n=10, p<0.0001).
- Article-representation audit: neither `53%` nor `88%` appears in the article HTML/XML, version-of-record PDF, or supplementary-information PDF. Figure 7A and Supplemental Figure 6B in the publisher source-data workbook contain the underlying WT, heterozygote, and homozygote values; a diagnostic simple-mean check yields a 77.66% homozygote reduction, consistent with the published 78%, and does not reproduce 88%. The heterozygote values yield a 46.07% reduction by the same check, not 53%; that unreported diagnostic value is not emitted as a study finding.
- Provenance trace: COMP-016 recorded the 53%/88% magnitudes as search-result-summary tier and explicitly said they had not been checked against the paper. Historical COMP-017 then mislabeled the same sentence as a `verbatim_snippet`. It is not a primary-source quotation and is excluded. The verified Western result and the separately significant immunofluorescence reduction remain distinct measurements.

### Liu et al. 2021

- DOI: `10.1186/s12986-021-00583-y`
- PMID: `34144706`; PMCID: `PMC8212495`
- Authors: Lei Liu, Tianyi Zhao, Lizhen Shan, Ling Cao, Xiaoxia Zhu, Yu Xue.
- Verified against the primary full-text XML at `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8212495/fullTextXML` on 2026-07-27.
- Verified Caco-2 conditions: 10^-4, 10^-6, and 10^-8 mol/L estradiol benzoate; 24, 48, and 72 hours. The 10^-4 mol/L (100 µM) condition increased ABCG2 mRNA at 48 hours without a dose-dependent effect. LY294002 at 50 µM partially blocked the response (p<0.05).
- These values describe nominal culture exposure, not physiological free-tissue exposure.

### Slepnev et al. 2023

- English translation DOI: `10.1134/S1990747823050100`
- Russian original DOI: `10.31857/S0233475523050109`
- Correct authors: A. A. Slepnev, Yu. V. Abalenikhina, N. M. Popova, A. V. Shchulkin, E. N. Yakusheva.
- Correct English-translation metadata: *Biochemistry (Moscow), Supplement Series A: Membrane and Cell Biology* 17(4):293–300.
- Verified against the official publisher-supplied English abstract at `https://journals.eco-vector.com/0233-4755/article/view/667335` on 2026-07-27.
- Abstract methods/results mapping: Caco-2 cells were exposed for 24 hours to progesterone, estradiol, or testosterone at nominal 1, 10, or 100 µM, with ABCG2 measured by Western blot; every hormone/concentration condition increased ABCG2.
- Abstract inhibitor mapping: PXR/FXR inhibition prevented the progesterone-associated increase; CAR/PXR suppression reduced the estradiol-associated increase while ABCG2 remained above control; PXR/FXR inhibition reduced the testosterone-associated increase while ABCG2 remained above control.
- Full numerical fold changes were not extracted. No serum-total or serum-free testosterone multiplier is reported because nominal culture concentration is not measured free-tissue exposure.

### MacLean et al. 2008

- DOI: `10.1124/dmd.108.020859`
- PMID: `18378562`
- Verified against the primary PubMed abstract at `https://pubmed.ncbi.nlm.nih.gov/18378562/` on 2026-07-27.
- The abstract reports qRT-PCR and Western blot across rat duodenum, jejunum, ileum, colon, and a complete 3-cm intestinal segmentation, with no sex-specific differences observed.
- This is a qualitative Animal Model null; it is not a healthy-human effect-size estimate.

## Reproduction boundary

`analyze.py` performs no retrieval. It validates and renders these fixed inputs. Any future direct-human analysis requires its own fixed dataset version, donor and tissue inclusion rules, sex-variable provenance, normalization, uncertainty model, and authoring reviews.
