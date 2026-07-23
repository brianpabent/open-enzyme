---
title: "Supplement–ABCG2 Assay-Evidence Audit (comp-004)"
date: 2026-05-05
tags: [abcg2, supplement, quercetin, curcumin, egcg, polyphenol, urate, gout, computational, pharmacology]
related:
  - computational-experiments.md
  - validation-experiments.md
  - abcg2-gut-urate-secretion.md
  - nlrp3-inflammasome.md
status: quantitative-verdict-invalid
---

# Supplement–ABCG2 Assay-Evidence Audit (comp-004)

**Question:** Do three cited ABCG2/BCRP interaction records—one each for quercetin, curcumin, and EGCG—support a quantitative prediction of intestinal urate-transport inhibition?

**Result:** No. The calculation that divided nominal bulk gut concentration by IC50 values from drug-substrate assays cannot estimate intestinal urate transport. Its ratios, predicted inhibition percentages, and clinical-risk labels are invalid.

The cited records still carry useful, narrower evidence:

- **Quercetin — In Vitro:** Cooray et al. used mitoxantrone and BODIPY-FL-prazosin in non-intestinal BCRP systems (PMID 15047179).
- **Curcumin — Animal Model:** Karibe et al. found an intestinal BCRP interaction in cynomolgus monkeys using sulfasalazine and rosuvastatin, not urate (PMID 29358184).
- **EGCG — In Vitro:** Farabegoli et al. found reduced mitoxantrone-assayed BCRP activity after EGCG exposure in MCF-7Tam cells without changed BCRP mRNA or protein (PMID 20149610).

These records route the compounds to a direct intestinal assay; they do not rank hazard or predict clinical direction. The discriminating experiment measures free parent compound and metabolites, total and surface ABCG2, ABCG2 attribution, barrier integrity, viability, and basolateral-to-apical urate flux across prespecified exposure times. See [validation §1.14](./validation-experiments.md#114-abcg2-response-to-dht-and-tnf-with-butyrate-and-lactoferrin-rescue).

The bounded machine-readable audit, inputs, provenance, and deterministic summary are in [`etc/experiments/comp-004-supplement-abcg2-antagonism/`](./etc/experiments/comp-004-supplement-abcg2-antagonism/).
