---
title: "Comparative Analysis of Codon Optimization Tools: Advancing toward a Multi-Criteria Framework for Synthetic Gene Design"
authors: "Demissie, E.A. et al."
journal: "Journal of Microbiology and Biotechnology"
year: 2025
doi: "10.4014/jmb.2411.11066"
pubmed: "40223268"
pmc: "PMC12010093"
tags: [codon-optimization, synthetic-gene-design, CAI, GC-content, mRNA-secondary-structure, codon-pair-bias, E-coli, Saccharomyces-cerevisiae, CHO, JCat, OPTIMIZER, GeneOptimizer]
---

# Comparative Analysis of Codon Optimization Tools: Advancing toward a Multi-Criteria Framework for Synthetic Gene Design

**Authors:** Eden A. Demissie, Seo-Young Park, Je Hun Moon, Dong-Yup Lee  
**Journal:** Journal of Microbiology and Biotechnology, Volume 35, Article e2411066  
**Year:** 2025  
**DOI:** https://doi.org/10.4014/jmb.2411.11066  
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/40223268/

## Abstract

This research conducts a thorough examination of widely-used codon optimization tools, evaluating their capacity to mirror host-specific codon preferences and design methodologies. Testing industrially relevant target proteins in Escherichia coli, Saccharomyces cerevisiae, and CHO cells revealed substantial variability in sequence outcomes across different tools. Tools including JCat, OPTIMIZER, ATGme, and GeneOptimizer demonstrated strong alignment with codon usage patterns, achieving elevated CAI values and efficient codon-pair utilization. Conversely, TISIGNER and IDT employed divergent strategies producing notably different results. Analysis encompassed GC content, mRNA secondary structure stability (ΔG), and codon-pair bias (CPB) parameters. The authors conclude that "single-metric approaches" prove insufficient and advocate for "multi-criteria frameworks integrating CAI, GC content, mRNA folding energy, and codon-pair considerations" to create tailored genetic sequences meeting host-specific requirements.

## Relevance to Open Enzyme

This paper directly supports Open Enzyme's synthetic gene design decisions for expressing uricase (or other enzymes) in S. cerevisiae or S. boulardii. The benchmarking of JCat, OPTIMIZER, ATGme, and GeneOptimizer against a yeast host — with the finding that no single metric (CAI alone) is sufficient — is the methodological justification for using a multi-criteria codon optimization approach. Specifically, integrating CAI + GC content + mRNA ΔG + codon-pair bias (CPB) is the recommended framework. The tool comparison also identifies which specific tools perform best for yeast hosts, directly informing the wet-lab gene synthesis workflow.
