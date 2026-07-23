---
title: Digestive Enzymes & EPI
aliases:
  - Exocrine Pancreatic Insufficiency
  - EPI
  - Enzyme Replacement
  - Fungal Enzymes
related:
  - enzyme-deficit
  - sibo
  - aspergillus-oryzae
  - enzyme-quantification-protocol.md
sources:
  - enzyme-deficit-deep-dive.md
  - enzyme-quantification-protocol.md
---

# Digestive Enzymes & Enzyme Insufficiency

Exocrine pancreatic insufficiency (EPI) is a clinical enzyme-deficit state. Symptoms alone do not distinguish it from mucosal disease, altered bile delivery, small-intestinal bacterial overgrowth, or other causes. This page separates established enzyme replacement from fungal-enzyme and engineered-production research.

## Physiological enzyme sources

| Source | Representative enzymes or cofactors | Main substrates |
|---|---|---|
| Saliva | Amylase, lingual lipase | Starch, lipid |
| Stomach | Pepsin activated by gastric acid | Protein |
| Pancreas | Proteases, lipase, amylase, nucleases | Protein, lipid, carbohydrate, nucleic acid |
| Intestinal brush border | Lactase, sucrase, maltase, peptidases | Disaccharides, small peptides |
| Bile | Bile salts; not enzymes | Lipid emulsification and lipase access |

Reactome's human digestion pathway `R-HSA-8935690` contains dietary-carbohydrate digestion (`R-HSA-189085`) and dietary-lipid digestion (`R-HSA-192456`). These identifiers standardize pathway vocabulary; they do not establish the activity of a fungal preparation or efficacy in EPI. **Evidence level: curated pathway infrastructure.**

## Causes and differential diagnosis

Loss of pancreatic tissue, chronic pancreatic injury, and cystic-fibrosis-associated duct dysfunction can reduce delivery of pancreatic enzymes to the intestine. Mucosal disease, bile-flow abnormalities, and altered microbial metabolism can produce overlapping symptoms through different mechanisms. A research design must therefore define the deficient function and compartment instead of treating nonspecific digestive symptoms as proof of EPI. **Evidence level: established clinical physiology.**

## Three different evidence objects

### Pancreatic enzyme replacement

Porcine pancrelipase formulations are established enzyme replacement for diagnosed EPI. Product activity, release profile, substrate contact, and the underlying disease state determine response. Clinical efficacy for an approved preparation does not transfer to an uncharacterized fungal mixture. **Evidence level: Clinical Trial / established clinical practice.**

### Native fungal enzymes

Species used in industrial fermentation can produce proteases, amylases, glucoamylases, lipases, lactases, cellulases, and pectinases. Their potential advantage is biochemical rather than categorical: a characterized enzyme may retain useful activity across a defined pH and substrate range. Activity in an extract or simulated-digestion assay does not establish efficacy in EPI. **Evidence level: In Vitro.**

### Engineered enzyme material

An engineered host or recombinant protein is a separate product. Parent-organism food history does not establish the identity, purity, exposure, efficacy, or safety of the engineered material. Host choice matters only when it changes an active production, formulation, containment, or delivery decision. **Evidence level: Mechanistic Extrapolation until configuration-specific data exist.**

## Research requirements

For each candidate material:

1. Define the missing digestive activity and intended gastrointestinal compartment.
2. Measure identity, specific activity, substrate range, and pH profile with matched controls.
3. Test gastric and intestinal stability in a configuration-specific simulated-digestion system.
4. Measure lot-to-lot reproducibility, impurities, coproducts, and formulation release.
5. Compare against an appropriate enzyme-replacement control in a disease-relevant model.
6. Prespecify the result that advances, redirects, or kills the candidate.

The [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md) provides the activity-measurement framework. Disease-specific efficacy and safety require separate evidence.

## Fungal production as a process reference

Wild-type *Aspergillus oryzae* produces several digestive-enzyme classes during food fermentation. That makes it useful as a process and sourcing reference, not as evidence that a particular preparation treats EPI. A recombinant configuration still requires direct characterization of enzyme activity, stability, coproducts, batch reproducibility, containment, and product-specific safety. **Evidence level: In Vitro / Mechanistic Extrapolation.**

## Falsification boundary

A candidate fails at the scope supported by the experiment: absent activity, loss of activity in the intended compartment, irreproducible production, or unacceptable impurities can kill a material or configuration without resolving the broader enzyme-replacement question. Conversely, biochemical activity alone cannot support a clinical-use claim.
