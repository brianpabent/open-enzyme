---
title: Saccharomyces cerevisiae (Baker's Yeast)
aliases:
  - S. cerevisiae
  - baker's yeast
  - brewer's yeast
  - budding yeast
related:
  - uricase
  - aspergillus-oryzae
  - etc/open-enzyme-vision
  - engineered-yeast-uricase-proposal
  - delivery-formats
sources:
  - engineered-yeast-uricase-proposal.md
  - etc/open-enzyme-vision.md
  - gout-deep-dive.md
  - nlrp3-exploit-map.md
---

# Saccharomyces cerevisiae (Baker's Yeast)

## Overview

*Saccharomyces cerevisiae* is the most genetically tractable eukaryotic organism on Earth, with GRAS (Generally Recognized As Safe) status from the FDA and a millennia-long history of safe use in baking and brewing. It offers a mature toolkit of characterized promoters, selectable markers, transformation protocols, and expression systems for rapid enzyme-production work. Critically, the exact gene-host combination of *Aspergillus flavus* uricase expressed in *S. cerevisiae* forms the basis of **rasburicase (Elitek/Fasturtec)**, the FDA-approved intravenous uricase drug used since 2002. The oral-delivery track asks whether that gene-host precedent can be adapted to a food-format route rather than IV administration. (Source: engineered-yeast-uricase-proposal.md, etc/open-enzyme-vision.md)

## GRAS Status and Food Safety

*S. cerevisiae* holds FDA GRAS status and has been safely consumed by humans for at least 4,000 years in bread, beer, wine, and other fermented foods. The organism does not produce mycotoxins or pathogenic compounds. It is one of the safest food organisms available. Beyond fermentation, nutritional yeast (dried, inactive *S. cerevisiae*) is marketed as a dietary supplement and food additive for its nutritional content (B vitamins, amino acids, chromium). (Source: engineered-yeast-uricase-proposal.md)

## Genetic Tractability: The Premier Toolkit

*S. cerevisiae* is the eukaryotic model organism with the most mature genetic engineering toolkit. This represents decades of academic and industrial investment in making this organism amenable to genetic modification.

### Expression Systems

**Inducible Promoters:**
- **GAL1, GAL7, GAL10** — Galactose-inducible promoters; repressed by glucose, derepressed when glucose is depleted and galactose is present
- Strong expression levels in GAL conditions; enables temporal control of gene expression
- Less practical for food fermentation (requires external galactose induction)

**Constitutive Promoters (Preferred for Food Applications):**
- **pTEF1** (Translation Elongation Factor 1α promoter) — THE STRONGEST constitutive promoter in *S. cerevisiae*; active across all carbon sources; extensively characterized; default choice for maximal expression
- **pPGK1** (Phosphoglycerate Kinase promoter) — Strong constitutive; slightly lower than TEF1 in most conditions; very well characterized
- **pGPD/pTDH3** (Glyceraldehyde-3-Phosphate Dehydrogenase promoter) — Comparable strength to TEF1; constitutive

For a food-product application, you want the enzyme expressed throughout normal growth and fermentation without requiring external inducers. Constitutive promoters like pTEF1 are the practical choice. (Source: engineered-yeast-uricase-proposal.md)

### Vector Strategies

**Episomal (High-Copy) Plasmids:**
- 2μ-based plasmids: 20–50 copies per cell
- Higher expression per cell
- Disadvantage: unstable without continuous selection pressure; cells that lose the plasmid grow faster and outcompete engineered strains
- Impractical for a food product without antibiotic selection

**Chromosomal Integration (Preferred for Food):**
- Insert the gene directly into yeast chromosomes via homologous recombination or CRISPR
- Single-copy or multi-copy integration at defined loci
- Stable over cell divisions and fermentation
- More predictable expression levels
- Strain stability over generations (critical for home fermentation)
- CRISPR/Cas9-based integration enables markerless insertion, important for regulatory considerations

For a therapeutic food product, **chromosomal integration is the more realistic path**. (Source: engineered-yeast-uricase-proposal.md)

### Selectable Markers

**Auxotrophic Markers (Standard for Lab Work):**
- URA3 (uracil prototrophy)
- LEU2 (leucine prototrophy)
- HIS3 (histidine prototrophy)
- Suitable for laboratory-scale development

**Dominant Markers (Food-Grade Alternatives):**
- kanMX (G418 antibiotic resistance) — not ideal for food products
- For food-grade applications: consider markerless CRISPR integration or marker excision after successful transformation

(Source: engineered-yeast-uricase-proposal.md)

## The Rasburicase Precedent

This is the critical piece: **rasburicase (Elitek/Fasturtec), the FDA-approved intravenous uricase drug, is *Aspergillus flavus* uricase expressed in genetically modified *S. cerevisiae*.** (Source: engineered-yeast-uricase-proposal.md)

- **Approval dates:** EMA approval in 2001, FDA approval in 2002
- **Use:** Intravenous enzyme therapy for tumor lysis syndrome in cancer patients
- **Manufacturing:** Commercial-scale production using this exact gene-host combination for over 20+ years
- **Clinical validation:** Decades of safety and efficacy data in human patients

This means the proof that *S. cerevisiae* can express active, correctly folded, therapeutically relevant *A. flavus* uricase is not theoretical—it is an approved pharmaceutical product.

### Expression Levels

Published academic work demonstrated that *S. cerevisiae* transformants accumulated active, soluble *A. flavus* uricase (Uox) to levels exceeding **13% of total cellular protein** using a hybrid GAL7/ADH2 promoter, with good proportionality between gene copy number (1–10 copies) and expression level. This is exceptionally high for a heterologous protein in yeast. (Source: engineered-yeast-uricase-proposal.md)

### Secretion vs. Intracellular Expression

The uricase-product design choice — secrete via the α-factor signal peptide vs. accumulate intracellularly and release on autolysis — and its resolution experiment live in the uricase proposal, not this chassis page. See [proposal §2 — Secretion vs. Intracellular Expression](./engineered-yeast-uricase-proposal.md#why-yeast). The organism-level fact that matters here: rasburicase manufacturing uses intracellular expression, and yeast secretion of the ~135 kDa tetramer is often inefficient.

## Gene Construct, Delivery, Dosing, and Regulatory — see the Proposal

The uricase **product plan** — source-gene selection (*A. flavus* uaZ vs. *C. utilis* vs. *V. vulnificus*), codon optimization, delivery formats (fermented beverages, nutritional yeast, *S. boulardii* probiotic, lysate, beer), dosing mathematics (the uric-acid budget and yeast-to-dose calculation), and the GMO-food regulatory pathway — is documented in the primary-research doc and is not duplicated on this chassis page:

- Gene construct design (source gene, codon optimization, promoter, markers): [proposal §3](./engineered-yeast-uricase-proposal.md#construct)
- Delivery formats (a–f, with honest credibility assessments): [proposal §4](./engineered-yeast-uricase-proposal.md#delivery)
- Dosing mathematics (uric-acid budget, yeast-mass-per-dose, koji cross-check): [proposal §5](./engineered-yeast-uricase-proposal.md#dosing)
- Regulatory framework (food / supplement / LBP / drug pathways): [proposal §6, Q4](./engineered-yeast-uricase-proposal.md#questions)

## Role in the Open Enzyme Portfolio

*S. cerevisiae* is a candidate production and validation chassis when its expression precedent, folding environment, process, or delivery format fits the payload. It is not a fallback required to wait for a koji result; host choice is an empirical decision within each track. (source: etc/open-enzyme-vision.md)

**When yeast is the right choice:**
- Tetrameric proteins where the rasburicase precedent (13% of total cellular protein in *S. cerevisiae*) is directly applicable
- Ursolic acid (8.59 g/L record in engineered *S. cerevisiae*; untested in koji)
- Carnosine (biosynthesis requires heterologous carnosine synthase; host choice open)
- Uricase itself — the *S. cerevisiae* path is proven (rasburicase); the koji path needs to be developed

**When koji is preferred:**
- Secreted enzymes where koji's 25–30 g/L secretion capacity (vs. 0.5–2 g/L for *S. cerevisiae*) is decisive
- Multi-enzyme products where native lipase/protease/amylase production is needed alongside engineered targets
- Home-fermentation formats where solid-state rice fermentation is simpler than liquid culture

(source: etc/open-enzyme-vision.md, §4)

## Comparison to Aspergillus oryzae

| Feature | S. cerevisiae | A. oryzae (Koji) |
|---|---|---|
| **Genetic tools** | Most mature yeast toolkit on Earth | Modern, CRISPR-ready, industrial standard |
| **Native enzymes** | None relevant to enzyme therapy | Lipase, protease, amylase (therapeutic) |
| **GRAS status** | Yes (4,000+ years) | Yes (1,000+ years food use) |
| **Fermentation** | Liquid (3–7 days, climate-controlled) | Solid-state on rice (36–48h, ambient) |
| **Native co-product scope** | Limited in this configuration | Native digestive enzymes alongside candidate uricase expression |
| **Expression level precedent** | 13% of total protein (rasburicase) | Comparable expected from strong promoters |
| **Therapeutic credibility** | Very high (rasburicase precedent) | Very high (GRAS, ancient safety history) |
| **Strategic role** | Candidate chassis with strong yeast precedent | Candidate chassis with secretion and solid-state advantages |

For Open Enzyme, the comparison is track-specific. Koji may be attractive for secreted or solid-state configurations; yeast may be attractive where expression and manufacturing precedent are stronger. The discriminating assay, not a global chassis hierarchy, selects the host. (source: etc/open-enzyme-vision.md; engineered-yeast-uricase-proposal.md)

## Immunogenicity Considerations

### Yeast Cell Wall Recognition

*S. cerevisiae* cell wall components (β-glucan, mannan, chitin) are recognized by:
- **Dectin-1 and Dectin-2** (C-type lectin receptors on immune cells)
- **TLR2** (toll-like receptor on epithelial cells)

These could trigger innate immune responses.

### Oral Tolerance Mechanism

However, oral delivery naturally encounters the **mucosal immune system**, which is inherently **tolerogenic**—designed for tolerance to dietary proteins. The oral tolerance literature from allergen immunotherapy supports the hypothesis that repeated oral exposure to yeast would induce tolerance rather than sensitization. (Source: engineered-yeast-uricase-proposal.md)

### Phase 1 Precedent

ALLN-346 (oral engineered uricase, a different organism/gene but same principle) Phase 1 trials showed:
- No serious adverse events
- No systemic absorption of enzyme
- No immune reactions at any dose tested

(Source: engineered-yeast-uricase-proposal.md)

### Validation Path

Expose intestinal epithelial cell monolayers (Caco-2 or HT-29) to: (a) wild-type *S. cerevisiae*, (b) engineered *S. cerevisiae* expressing uricase, (c) purified uricase alone, (d) LPS positive control. Measure cytokine panel (IL-8, TNF-α, IL-1β, IL-10) at 4h and 24h by ELISA. Monitor transepithelial electrical resistance (TEER) for barrier integrity. If engineered strain shows significantly different immune activation than wild-type, flag for further investigation. Cost: ~$2,000–4,000; Time: 3–4 weeks. (Source: engineered-yeast-uricase-proposal.md)

## Safety: No Novel Pathogenicity

*S. cerevisiae* does not produce mycotoxins or virulence factors. Engineered strains carry only the uricase transgene—no foreign pathogenic elements. The genetic modifications are purely additive (expressing one additional protein). Safety profile is expected to be excellent. (Source: engineered-yeast-uricase-proposal.md)

## Engineering implications

The optimized uricase expression cassette (TDH3p constitutive promoter, intracellular localization, ADH1t terminator, predicted 800–1200 mg/L equivalent, codon-optimization parameters) is product-plan detail and lives with the proposal. See [Codon Optimization & Expression Cassette](./codon-optimization-expression-cassette.md) and [proposal §3](./engineered-yeast-uricase-proposal.md#construct).

## References

- Source: engineered-yeast-uricase-proposal.md — Detailed technical proposal, dosing math, delivery format analysis, validation experiments
- Source: etc/open-enzyme-vision.md — Mission and track context
- Source: gout-deep-dive.md — Uric acid biology and treatment context
