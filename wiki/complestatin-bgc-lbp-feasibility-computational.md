---
title: "Complestatin-Family BGC LBP-Chassis Feasibility — Computational Analysis (comp-024)"
date: 2026-05-16
tags:
  - complestatin
  - nrps
  - bgc
  - engineered-lbp
  - cp0
  - upstream-complement
  - heterologous-expression
  - computational
related:
  - computational-experiments.md
  - upstream-complement-modulator-sweep-computational.md
  - engineered-lbp-chassis.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
  - complement-c5a-gout.md
  - chassis-pending-interventions.md
sources:
  - "Chiu HT et al. PNAS 2001;98(15):8548-53 PMID 11447274 — original BGC sequencing (48.7 kb, 16 ORFs, 7 NRPS modules)"
  - "Park OK et al. ChemBioChem 2016;17(18):1725-31. DOI 10.1002/cbic.201600241; PMID 27383040 — 54.5 kb cluster reconstituted in S. lividans TK24; gene deletions produced monocyclic M55 and linear S56"
  - "MIBiG BGC0000326 — isocomplestatin from S. lavendulae"
status: retired-invalid-model
---

# Complestatin-Family BGC LBP-Chassis Feasibility (comp-024)

COMP-024 is [invalidated and non-runnable](./etc/experiments/comp-024-complestatin-bgc-lbp-feasibility/). Its hand-assigned factors, geometric means, color thresholds, host ordering, and C1-INH comparison have no predictive or decision status. The model does not establish that an LBP route fails, that another host wins, or that C1-INH should receive priority.

## Evidence that survives

Chiu et al. described a 48.7 kb complestatin biosynthetic gene cluster with 16 open reading frames and seven NRPS modules (**In Vitro** molecular and biochemical characterization; PMID 11447274). Park et al. reconstituted a 54.5 kb cluster in *Streptomyces lividans* TK24; their gene-deletion experiments produced the monocyclic derivative M55 and linear derivative S56 (**In Vitro** heterologous production and structural characterization; PMID 27383040). The accessible primary record does not establish that either derivative lacked biological activity.

These records support treating complete tailoring and active-product recovery as experimental gates. They do not establish transfer to *E. coli* Nissle 1917 or *Bacteroides thetaiotaomicron*, nor do they show that either host is incapable of producing the molecule.

> **Research conjecture — production phase may determine complestatin viability**{ .research-conjecture-label }
>
> **Grounded premises:** The complestatin cluster includes cytochrome P450 genes, and Park et al. showed that deleting two of those genes changed the recovered products to monocyclic M55 and linear S56 (**In Vitro**; source: PMID 27383040). Cytochrome P450 catalysis is oxygen-dependent (**Mechanistic Extrapolation**; source: established P450 reaction chemistry). *S. lividans* TK24 produced products from the reconstituted cluster under the tested manufacturing conditions (**In Vitro**; source: PMID 27383040). Transfer to an LBP chassis has not been demonstrated.
>
> **Novel leap:** Active complestatin may require an oxygenated manufacturing phase even if the eventual product is delivered to an anaerobic compartment. No direct evidence establishes complete active-product formation in EcN or *Bacteroides*.
>
> **Why it matters:** This separates the molecule from the production chassis. Failure of live colonic manufacture would not by itself kill an ex-situ production-and-delivery route.
>
> **Discriminating observation:** In a prespecified host × oxygen-regime matrix, measure intact crosslinked product by analytical chemistry, complement-inhibitory activity, production rate, and host fitness. Advance the active-product-formation hypothesis only if active product—not merely expressed genes or linear peptide—is recovered. Delivery, compartmental access, safety, and portfolio priority require separate evidence.

C1-INH remains a separate CP0 candidate. Its exact construct, folding, glycosylation dependence, luminal stability, retained inhibition, and access require their own measurements; COMP-024 supplies none of them.
