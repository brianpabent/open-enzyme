# Provenance — comp-049 mixed-source correction set

This is a bounded correction set, not a literature census. It contains four primary animal studies and one secondary systematic review. The checks below support only the fields encoded in `evidence_records.json`.

## Smilax glabra total-flavonoid fraction

Huang L, Deng J, Chen G, et al. “The anti-hyperuricemic effect of four astilbin stereoisomers in Smilax glabra on hyperuricemic mice.” *Journal of Ethnopharmacology* (2019). PMID 30851369. DOI `10.1016/j.jep.2019.03.004`.

**Verified location:** primary PubMed abstract. The tested material was a total-flavonoid fraction containing neoastilbin, astilbin, neoisoastilbin, and isoastilbin, reported as 55.6% of the fraction in combination. In potassium-oxonate hyperuricemic mice, the source reports lower serum urate, lower hepatic xanthine-oxidase activity in one treatment group, and higher renal OAT1 and OCTN2 expression in at least one tested group. The abstract does not isolate an individual stereoisomer as causal and does not report free exposure, direct renal urate function, or intestinal urate flux. The full text and full preparation details were not verified in this COMP, so abstract nonreporting is not encoded as study-level nonmeasurement.

## Emodin

Hou SW, Chen SJ, Shen JD, et al. “Emodin, a Natural Anthraquinone, Increases Uric Acid Excretion in Rats with Potassium Oxonate-Induced Hyperuricemia.” *Pharmaceuticals* (2023). PMID 37375737; PMCID PMC10304951. DOI `10.3390/ph16060789`.

**Verified location:** primary full text, Methods §4.1, Results §§2.1 and 2.4, and Discussion. The experiment used commercial emodin from Combi-Blocks, product ST-7788, with stated purity of 90%; the plants in which emodin traditionally occurs were not the source of the tested material. The stated purity does not establish impurity-free single-component attribution. Treatment in the rat model lowered serum urate in reported groups and increased fractional urate excretion in at least one tested group; hepatic xanthine-oxidase activity did not change in the tested groups. The study did not measure a causal renal transporter or intestinal urate flux. A null hepatic enzyme result cannot supply the missing renal target attribution.

## Coix seed oil

Wu G, et al. “Coix Seed Oil Alleviates Hyperuricemia in Mice by Ameliorating Oxidative Stress and Intestinal Microbial Composition.” *Nutrients* (2025). PMCID PMC12114407. DOI `10.3390/nu17101679`.

**Verified location:** primary full text, Methods and Results. The study used oil prepared by petroleum-ether extraction of vendor-procured *Coix lacryma-jobi* seeds; the paper reports the seed identity but no independent botanical-authentication record. In a mouse hyperuricemia model, the oil lowered serum urate and changed hepatic enzyme activities plus renal and intestinal urate-transporter expression. ABCG2 expression increased in kidney and intestine. The study also reports intestinal histology and ZO-1, Occludin, and Claudin-1 measures. These general barrier observations do not substitute for barrier-integrity and viability controls in a direct urate-flux assay, which the paper did not run. It did not measure ABCG2-attributed urate flux, free epithelial exposure, an individual causal oil component, or human efficacy.

## Plantaginis Semen extract

Liu T, et al. “Plantaginis Semen Ameliorates Hyperuricemia Induced by Potassium Oxonate.” *International Journal of Molecular Sciences* (2024). PMCID PMC11313179. DOI `10.3390/ijms25158548`.

**Verified location:** primary full text, Results §§2.2, 2.3, and 2.7 and Methods §§4.2 and 4.6. An authenticated *Plantago asiatica* seed lot was extracted with eightfold 65% ethanol by three 2-hour refluxes and concentrated for gavage. The rat study reports lower serum urate, lower renal Urat1 and Glut9 mRNA, and lower URAT1 protein after extract treatment. The xanthine-oxidase result was produced with an ELISA kit and reported as activity/level; the Methods do not establish a catalytic substrate-turnover assay, so this COMP encodes it as an associated assay signal rather than direct enzyme function. Serum-borne extract components were identified in a separate arm, but the study did not establish any one component as the cause of the transporter or phenotype results.

## Modified Simiao decoctions

Liu YF, Huang Y, Wen CY, et al. “The Effects of Modified Simiao Decoction in the Treatment of Gouty Arthritis: A Systematic Review and Meta-Analysis.” *Evidence-Based Complementary and Alternative Medicine* (2017). PMID 28373889; PMCID PMC5360963. DOI `10.1155/2017/6037037`.

**Verified location:** secondary full text, Abstract, Methods, Results §3.3, and conclusion. This record encodes the serum-urate signal reported for the meta-analyzed trial set only. Most included trials were rated low quality because randomization, allocation concealment, blinding, and attrition reporting were inadequate or unclear. This secondary source can route the lead to primary-trial review; it does not itself verify the underlying trials, their exposure measurements, or a standardized formula, causal herb, compound, target, or synergy.

## Authoring boundary

These records support evidence qualification and experiment routing only. If the COMP later runs and passes post-run review, `wiki/tcm-modern-rigor-intersection.md` is the canonical evidence home. The records do not support a compound rank, standardized dose, viability label, clinical recommendation, delivery choice, or mechanistic attribution beyond the measured endpoint.
