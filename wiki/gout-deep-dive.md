---
title: Gout — Causal System and Exploit Surface
date: 2026-07-27
tags:
  - gout
  - urate
  - crystals
  - nlrp3
  - complement
  - microbiome
  - delivery
related:
  - gout-pathophysiology.md
  - gout-genetic-variants.md
  - nlrp3-exploit-map.md
  - gout-kill-chain-delivery-routes.md
  - gout-clinical-pipeline.md
status: evidence-map
---

# Gout — Causal System and Exploit Surface

## Mission view

Open Enzyme treats gout as a system to red-team: identify a causal weakness, build the cheapest discriminating test, exploit a real vulnerability, and kill or redirect the exact hypothesis when a required premise fails. Koji, yeast, live biotherapeutics, purified enzymes, peptides, small molecules, local delivery, and data-driven stratification are candidate tracks—not the project.

Gout contains two coupled but separable problems:

1. Urate supersaturation and MSU crystal burden.
2. The inflammatory response to existing crystals.

A result on one axis does not prove an effect on the other. Flare suppression is not urate lowering, and urate lowering does not establish direct inflammatory target engagement.

## Causal chain

| Step | Evidence-supported role | Exploitable question |
|---|---|---|
| Purine supply and turnover | Host and dietary purines feed urate production | Can input or precursor flux be altered without moving the problem to another metabolite or compartment? |
| Xanthine oxidoreductase | Produces urate; clinically validated target | Can production be reduced with an exact material that preserves an acceptable safety boundary? |
| Renal urate handling | URAT1, GLUT9, ABCG2, OAT-family and other transport processes contribute to reabsorption and secretion | Which transporter and cell surface are causal for the selected phenotype, and can the exact product reach them? |
| Intestinal urate handling | Intestinal secretion and microbial or enzymatic degradation can contribute to disposal | Can a measured lumen sink increase net urate disposal under physiological substrate, oxygen, transit, and peroxide conditions? |
| Systemic urate degradation | Product-specific uricase evidence shows circulating urate is enzymatically tractable | Can immunogenicity, persistence, infusion reaction, and peroxide be controlled for a new exact product? |
| Supersaturation and crystals | Sustained urate above the solubility boundary permits MSU deposition; existing crystals can persist | Can crystal burden be reduced in the relevant tissue, and is the effect distinct from temporary serum change? |
| Complement-associated priming | C5a/C5aR1 and related complement inputs can amplify MSU responses in defined human-cell and animal systems | When is complement causal, and is direct receptor, upstream cascade, or crystal removal the cleanest perturbation? |
| NLRP3 activation | Potassium flux, organelle injury, NLRP3/ASC assembly, caspase-1, and GSDMD form separable experimental nodes | Which exact node changes before IL-1β falls? |
| IL-1 signaling | Product-specific human gout studies establish clinical tractability | Can a different product or route reproduce target engagement without importing another product's efficacy? |
| Neutrophil amplification | Recruitment, lipid mediators, NET behavior, and tissue injury shape flare intensity and termination | Can amplification be reduced without blocking necessary host defense? |
| Resolution and repair | Exact RvD1 and MaR1 have distinct MSU mouse evidence; repair is a later, separate phenotype | Can an exact mediator or repair lead improve termination or recovery with measured exposure? |

The fuller mechanistic map is [Gout pathophysiology](./gout-pathophysiology.md). The intervention-node map is [NLRP3 exploit map](./nlrp3-exploit-map.md).

## Clinical anchors without a treatment guide

Established-care classes provide causal comparators:

- Xanthine-oxidoreductase inhibition tests reduced urate production.
- Uricosuric drugs test renal urate disposal.
- Systemic uricase tests enzyme-mediated circulating urate depletion.
- Colchicine tests microtubule- and neutrophil-associated inflammatory control.
- IL-1-directed products test downstream cytokine signaling.
- Dapansutrile supplies compound- and protocol-specific Phase 2a human gout evidence for an NLRP3-directed product (PMID 33005902).
- ALLN-346 Study 201 (NCT04987242) supplies exact-product human evidence that a gut-lumen uricase route reached clinical testing.

These precedents do not select a treatment, dose, route, or combination for a reader. Current regulatory and trial status belongs on the dated [clinical evidence surface](./gout-clinical-pipeline.md) and must be refreshed from primary records.

## Urate-control exploit tracks

### Reduce production

Xanthine oxidoreductase is clinically validated, but upstream purine flux, fructose-driven ATP/AMP turnover, PRPS activity, and microbial precursor handling remain research surfaces. Each needs mass balance; a lower serum value alone may not identify the operative mechanism.

### Increase renal or intestinal disposal

Transporter expression, membrane localization, direction of flux, substrate competition, genotype, kidney function, and intestinal segment can all alter the result. A transcript change is not functional urate transport.

The gut-lumen UOX hypothesis asks whether active enzyme can consume transporter-delivered urate quickly and safely enough to change net disposal. The hard gates are physiological substrate access, reaction-site enzyme activity, oxygen, peroxide, antioxidant loss, transit, epithelial safety, and systemic compensation. See [gut-lumen sink](./gut-lumen-sink.md) and [validation experiments 1.33 and 1.36](./validation-experiments.md).

### Restore or deliver UOX

Purified systemic enzyme, oral purified enzyme, engineered yeast, engineered koji, live biotherapeutics, edited host cells, mRNA, and local enzyme depots are separate product–route hypotheses.

- Systemic uricase precedents validate only their exact products and protocols.
- Active *A. flavus* UOX expression in yeast supplies a manufacturing precedent, not oral efficacy.
- An engineered chassis must demonstrate expression, native activity, reaction-site access, physiological flux, containment, and safety.
- Failure of one sequence, topology, host, or route narrows that configuration rather than the entire uricase track.

## Inflammation and resolution exploit tracks

### Complement and priming

MSU can activate complement, and C5a can potentiate MSU-induced IL-1β in defined systems. Direct C5aR1 antagonism, upstream complement regulation, antioxidant perturbation, and crystal removal answer different questions. The current natural-product search result is bounded, not an empty-class conclusion. See [Complement C5a in gout](./complement-c5a-gout.md).

### NLRP3 assembly and execution

The [NLRP3 evidence page](./nlrp3-inflammasome.md) separates priming, potassium flux, NLRP3/NEK7, ASC, caspase-1, IL-1 signaling, neutrophil amplification, and GSDMD. A candidate earns only the narrowest node supported by a mechanism-proximal measurement.

Examples:

- BHB changes potassium-efflux and ASC-associated readouts in urate-crystal-relevant preclinical systems; it is not a defined direct binder and does not establish a fasting or ketone regimen (PMID 25686106).
- Oridonin and tranilast have source-specific target-level mechanisms; human gout translation remains exact-product work.
- KPV has PepT1-related uptake and an NF-κB reporter effect in named non-MSU cell systems. Direct MSU activity, synovial exposure, and a gout route are unestablished (PMID 18061177).
- BPC-157 is an adjacent repair lead, not a demonstrated gout or NLRP3 intervention.
- Lactoferrin contains several exact-material hypotheses across iron handling, inflammatory signaling, barrier biology, and mitophagy/pyroptosis in adjacent systems. None establishes a generic multi-chokepoint gout effect.

### Resolution and repair

Exact RvD1 and MaR1 materials changed distinct outcomes in MSU mouse systems (PMIDs 35716378 and 37996809). RvD2 has adjacent macrophage and zymosan evidence (PMID 29601102). EPA and DHA are precursors and require measured conversion; there is no established gout-specific precursor ratio. See [SPM resolution pathway](./spm-resolution-pathway.md).

Repair after inflammation is a separate phenotype. A negative acute-inflammation result need not kill a properly specified repair hypothesis, and a repair signal must not be relabeled as flare suppression.

## Genetics and stratification

ABCG2, SLC2A9, SLC22A12, and other variants can alter urate handling, but genotype-to-intervention predictions require functional evidence for the exact material and compartment. A database non-hit is not universal absence. See [Gout genetic variants](./gout-genetic-variants.md) and the genotype-specific hypothesis pages.

## Delivery is part of the hypothesis

A mechanism is not actionable until the exact product reaches the exact compartment on the required time scale. Oral, systemic, local, and living-product configurations cannot inherit one another's bioavailability or safety. See [target-first delivery](./gout-kill-chain-delivery-routes.md) and [product-first delivery](./delivery-route-matrix.md).

## Portfolio decision rules

1. Name the causal weakness, exact material, compartment, and model.
2. Verify load-bearing inputs against primary evidence.
3. Measure exposure and target engagement before final disease markers.
4. Prespecify advance, redirect, and kill thresholds.
5. Test individual arms before claiming an interaction.
6. Kill only the material–route–model claim or failed premise that was tested.
7. Preserve a useful untested connection as a bounded Research Conjecture on its owning page.
8. Compare tracks on shared decision surfaces; do not force every page to defend itself against koji or another modality.

## Highest-value open questions

- Can any exact gut-lumen UOX configuration create physiologically meaningful net urate disposal without peroxide or epithelial injury?
- Which human proximal-tubule delivery handle can reach a causal urate transporter safely?
- Which complement input is causal in human flare material under matched perturbation?
- Which exact NLRP3 or GSDMD probe preserves target engagement at human-relevant exposure?
- Can exact RvD1 or MaR1 change resolution in a human gout-relevant system?
- Which apparent adverse-event or clinical-program failure contains a product-specific weakness that a different route could exploit?
- Which useful cross-domain conjecture emerges only when the full detailed corpus is compared and then rehydrated against primary sources?

The active action queue owns unresolved work. The wiki owns current scientific interpretation. Git owns history.

This is Phase 0 research, not clinical, treatment, dosing, or self-experiment guidance.
