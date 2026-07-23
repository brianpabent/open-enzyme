# Provenance — comp-004 assay-evidence audit

The revised artifact contains no dose, bioavailability, solubility, gut-volume, free-exposure, IC50-occupancy, percent-inhibition, clinical-risk, or genotype parameters. Those inputs belonged to the invalidated quantitative model and remain available through Git history.

## Quercetin

- Cooray HC, Janvilisri T, van Veen HW, et al. "Interaction of the breast cancer resistance protein with plant polyphenols." *Biochem Biophys Res Commun.* 2004;317(1):269-275. PMID 15047179.
- The primary abstract reports functional BCRP modulation using the drug substrates mitoxantrone and BODIPY-FL-prazosin in BCRP-overexpressing cell lines. That record does not establish intestinal urate transport.
- Earlier comp-004 versions averaged two ChEMBL IC50 values from different cell systems and treated the mean as one assay context. That average is retired and is not present in the revised input or output.

## Curcumin

- Karibe T, Imaoka T, Abe K, Ando O. "Curcumin as an In Vivo Selective Intestinal Breast Cancer Resistance Protein Inhibitor in Cynomolgus Monkeys." *Drug Metab Dispos.* 2018;46(5):667-679. PMID 29358184; DOI 10.1124/dmd.117.078931.
- This is direct Animal Model evidence for intestinal BCRP interaction, but the reported probe substrates were drugs rather than urate. The cited record supports including curcumin in an intestinal urate-flux assay, not a quantitative urate-inhibition or clinical-risk estimate.

## EGCG

- Farabegoli F, Papi A, Bartolini G, Ostan R, Orlandi M. "(-)-Epigallocatechin-3-gallate downregulates Pg-P and BCRP in a tamoxifen resistant MCF-7 cell line." *Phytomedicine.* 2010;17(5):356-362. PMID 20149610; DOI 10.1016/j.phymed.2010.01.001.
- EGCG exposure reduced BCRP functional activity in a mitoxantrone assay while BCRP mRNA transcription and protein level did not change. The cited record does not report an applicable kinetic IC50 or Ki or establish intestinal urate transport.

## Separate EGCG animal evidence

- Yu H, Lou Z, Wu T, et al. "Mechanisms of epigallocatechin gallate (EGCG) in ameliorating hyperuricemia: insights into gut microbiota and intestinal function in a mouse model." *Food Funct.* 2024;15(11):6068-6081. PMID 38757391; DOI 10.1039/D4FO01606H.
- EGCG lowered serum urate in potassium-oxonate hyperuricemic mice. The primary abstract reports renal Oat1/Oct1 upregulation and Urat1/Glut9 downregulation, plus microbiome and intestinal-transcriptome changes; it does not report an ABCG2 result or Nrf2-mediated ABCG2 sign switch. That abstract therefore cannot support the corpus's claimed favorable ABCG2 phenotype.

## Decision boundary

These three cited records establish assay signals in different systems. They do not supply the combination of measured free intestinal exposure, intestinal ABCG2 protein, and urate flux needed to rank intestinal-urate hazard. The revised code therefore emits an evidence-bounded experimental disposition and prohibits quantitative or clinical inference.
