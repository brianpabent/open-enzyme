# Input provenance — comp-045

Rechecked 2026-07-13.

- Miyazaki et al. 2025, PMID 40033341, PMCID PMC11877951: direct human jejunal urate measurement. Median baseline 0.59 µM (IQR 0.06–1.16 µM). The conversion was independently verified in comp-044 provenance: 99.5 pg/µL = 99.5 µg/L; divided by urate molecular weight 168.11 g/mol = 0.592 µmol/L. This anchors the 0.59 µM arm.

- Gao et al. *Cell Reports Medicine* 2025, PMID 41038159, PMCID PMC12629798: PULSE compared intracellular smUOX + YgfU, LamB-secreted smUOX, and InakN-displayed smUOX. KatG and VHb were then expressed; chronic-rat dosing used a 1:1:1 mixture of the three topologies. These are the experimental topology anchors.
- Zhao R et al. *Gut Microbes* 2022, PMID 35491895, PMCID PMC9067508: engineered EcN expressed PucL/PucM, YgfU, KatG, and VHb; the complete construct improved urate degradation under restricted dissolved oxygen and lowered ROS. This anchors the intracellular closed-loop architecture.
- Li et al. 2023, PMCID PMC10242094: pBR-pucLM + pAC-ygfU degraded urate in defined medium and FaSSIF-V2. This is an additional intracellular/importer precedent.
- EcN C6 periplasmic UOX, PMCID PMC10013758: chromosomally insulated/periplasmic precedent relevant to containment and localization.

## Mechanistic inference made explicit

The compartment concern is chemical, not a claimed efficacy result: H2O2 is generated where active UOX encounters urate. Intracellular catalase can be directly co-localized with intracellular UOX. For a secreted or surface-displayed UOX, intracellular catalase may reduce cell-associated ROS after H2O2 diffuses inward, but it is not at the extracellular generation site. PULSE nonetheless observed improvement after adding the joint KatG+VHb module to all three topologies. The design therefore uses graded states—direct support, indirect empirical support, proposed direct test, unresolved, or unsupported—rather than binary closure.

KatG and VHb were combined in the principal PULSE/Zhao comparisons; their independent contributions were not fully isolated. The new factorial deliberately separates them. Co-secreted/fused or surface-tethered catalase arms are proposed constructs, not published PULSE configurations.

No numerical ranking is assigned because the primary papers did not test all topology × oxygen × catalase combinations at human jejunal urate concentrations. The 250 µM arm reproduces the PULSE in-vitro benchmark; 0.59 µM is the direct-human jejunal prior; 50 µM is labeled sensitivity only.
