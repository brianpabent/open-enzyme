---
title: "Rosmarinic Acid + DAF SCR1-4 Combination Question (comp-029)"
date: 2026-05-16
tags: [computational, comp-029, complement, CP0, rosmarinic-acid, DAF, CD55, gout]
related:
  - complement-c5a-gout.md
  - daf-cd55-scr14-truncated-computational.md
  - upstream-complement-verification-rerun-computational.md
  - validation-experiments.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
sources:
  - "Sahu A, Rawal N, Pangburn MK. Biochem Pharmacol 1999;57(12):1439-46 (PMID 10353266)"
  - "Englberger W et al. Int J Immunopharmacol 1988;10(7):729-37 (PMID 3198307)"
  - "Medof MD, Kinoshita T, Nussenzweig V. J Exp Med 1984;160:1558-1578 (PMC2187498)"
  - "Kinoshita T et al. J Exp Med 1987;166:1376-1389 (PMC2189641)"
  - "Wessig AK et al. Sci Rep 2022;12:4423 (PMC8924570)"
status: retired-invalid-model
---

# Rosmarinic Acid + DAF SCR1-4 Combination Question (comp-029)

Could rosmarinic acid and active DAF SCR1-4 suppress MSU-associated complement activation more than either exact material alone?

COMP-029 cannot answer that question. It combined assumed exposure and DAF-accessibility distributions with an uncalibrated composition rule. Every numerical result, confidence interval, category, co-localization claim, complementarity claim, and routing conclusion is invalid. The [COMP-029 tombstone](./etc/experiments/comp-029-combined-cp0-systems-model/) is non-runnable; Git retains the retired implementation and outputs.

## Evidence boundary

Rosmarinic acid changed complement readouts in biochemical assays, with material assay-format variation (**In Vitro**; PMIDs 10353266 and 3198307). DAF accelerates decay of complement convertases (**In Vitro**; PMC2187498 and PMC2189641). MSU-associated complement activation can generate downstream complement products (**In Vitro**; PMC8924570).

Those observations do not establish that rosmarinic acid and DAF reach the same relevant compartment, remain active together, act independently, or produce an additive or synergistic effect. COMP-012 also does not establish DAF expression, folding, protease survival, retained activity, delivery, or MSU-surface access.

> **Research conjecture — two-node complement suppression may outperform either arm alone**{ .research-conjecture-label }
>
> **Grounded premises:** Rosmarinic acid changes complement readouts in biochemical assays (**In Vitro**; PMID 10353266 and PMID 3198307). DAF accelerates decay of complement convertases (**In Vitro**; [PMC2187498](https://pmc.ncbi.nlm.nih.gov/articles/PMC2187498/) and [PMC2189641](https://pmc.ncbi.nlm.nih.gov/articles/PMC2189641/)). MSU-associated complement activation generates measurable downstream products (**In Vitro**; [PMC8924570](https://pmc.ncbi.nlm.nih.gov/articles/PMC8924570/)).
>
> **Novel leap:** If delivered in active form to the same relevant compartment, rosmarinic acid and DAF SCR1-4 may suppress MSU-associated complement activation more than either arm alone. No direct evidence establishes the exact pair, delivery geometry, exposure, or interaction.
>
> **Why it matters:** A genuine combination effect could expose a multi-node weakness that neither intervention can exploit reliably alone.
>
> **Discriminating observation:** Once an active DAF preparation exists, compare vehicle, rosmarinic acid, DAF SCR1-4, and their combination in one matched complement-competent-serum assay. Measure C5a, C5b-9, DAF recovery, retained function, and surface association across prespecified concentrations.

A useful result must show that each exact material remains active in the joint assay and that the combination differs reproducibly from the stronger singleton. A null result kills only the tested pairing and conditions.

Related: [complement evidence](./complement-c5a-gout.md) · [DAF construct question](./daf-cd55-scr14-truncated-computational.md) · [H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) · [validation experiments](./validation-experiments.md)
