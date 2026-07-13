# Input provenance — comp-046

Rechecked 2026-07-13.

## Direct evidence anchors

- Ji et al. *npj Science of Food* 2025, DOI 10.1038/s41538-025-00556-y; PMCID PMC12375036: *Pediococcus acidilactici* GR-5 from Jiangshui expressed purine nucleoside phosphorylase DeoD and lowered serum urate in a purine-nucleoside/oxonate mouse model. DeoD phosphorolysis produces free purine base; it does not destroy the purine ring. The paper also reports whole-cell salvage-pathway changes but does not isolate DeoD causality with a knockout. The model therefore names stage 1 whole-cell GR-5 cleavage plus salvage/retention and credits it only when material is retained or becomes less absorbable.
- Wilson and Wilson, PMID 8254512, and Bronk & Hastewell, PMID 6716178: isolated rat jejunal work supports rapid epithelial metabolism/transport of dietary purine nucleosides and bases. These studies motivate an upstream stage but do not provide human fractions for this model.
- Gao et al. 2025 (PMID 41038159) and Zhao et al. 2022 (PMID 35491895): engineered oxidative UOX stages.
- Liu et al. 2023, PMCID PMC10421625: anaerobic microbial purine degradation and species-dependent end products; anchors the distal PDB stage.

## Parameter policy

All fractions are broad scenario levels, not measured human effect sizes. The dietary input and endogenous luminal-urate input are each normalized to 100 units and kept as separate conserved ledgers. The full-factorial occupancy is not a probability distribution.

The architecture equations explicitly sweep same-pool overlap and staged residual-transfer efficiency. They illustrate a falsifiable boundary; they do not establish that staging is superior. The analysis does not convert to mg/dL serum urate, mouse-to-human efficacy, or product dose.
