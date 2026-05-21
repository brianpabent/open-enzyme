# Helicteres benzofuran lignans — Model A source read (CFH-dependence classification)

**Date:** 2026-05-21
**Author:** Claude Opus 4.7 (Model A in two-model cross-check protocol)
**Scope:** comp-039 mechanism-dissociation classification of *Helicteres angustifolia* benzofuran lignans (Compound 4 = machicendonal; Compound 5 = (7S,8R)-dihydrodehydrodiconiferyl alcohol). The most potent single-compound CH50 in the comp-018/comp-020 corpus, but on a single-paper anchor (Yin 2016) without independent wet-lab replication.

## Primary source read

1. **Yin X, Lu Y, Cheng ZH, Chen DF.** Anti-Complementary Components of *Helicteres angustifolia*. *Molecules* 2016;21(11):1506. PMID 27834928 / PMC6273495. doi:10.3390/molecules21111506 — full text read.

## Binding-site / target evidence

**Yin 2016 (PMC6273495):** complement-depleted-sera assay using anti-C1q, C2, C3, C4, C5, C9 antisera (Calbiochem / Zhejiang Nanfang). Restoration of hemolytic capacity in each C-depleted serum identifies the components NOT acting as the compound's target. Verbatim:

> "compound regained the hemolytic capacity of C5-depleted serum, and compound regained the hemolytic capacity of C4- and C5-depleted sera. These findings suggested that compound [4 = machicendonal] probably acted on C1q, C2, C3, C4 and C9, while compound [5 = dihydrodehydrodiconiferyl alcohol] interacted with the C1q, C2, C3 and C9 components of the complement."

CH50 values verified directly from paper: **Compound 4 CH50 = 0.040 ± 0.009 mM (40 μM); AP50 = 0.105 ± 0.015 mM (105 μM). Compound 5 CH50 = 0.009 ± 0.002 mM (9 μM); AP50 = 0.021 ± 0.003 mM (21 μM).**

Targets:
- **Compound 4 (machicendonal):** C1q, C2, C3, C4, C9 — broad multi-target across both classical-pathway initiation (C1q, C2, C4), central amplification (C3), and terminal MAC (C9).
- **Compound 5 (dihydrodehydrodiconiferyl alcohol):** C1q, C2, C3, C9 — broad multi-target but NOT C4 (its CH50 inhibition is rescued by C4 depletion → C4 is NOT compound 5's target).

The paper does not mention Factor H / CFH anywhere.

## Mechanism mapping vs CFH Y402H footprint

The Yin 2016 targets are dominated by:

- **C1q:** initiator of classical pathway; pattern-recognition. CFH does not regulate C1q. Binding upstream of CFH.
- **C2:** classical-pathway C3 convertase building block (C4b2a). CFH does not regulate C2. Binding upstream.
- **C3:** central amplification node. CFH regulates C3b (the cleavage product); both lignans bind C3 itself, upstream of cleavage.
- **C4:** classical-pathway initiator (compound 4 only). CFH does not regulate C4.
- **C9:** terminal MAC component. CFH does not regulate C9.

**None of the identified targets overlap with CFH's regulatory substrates** (which are surface-deposited C3b and the C3bBb convertase via decay-acceleration). The lignan-multi-target pattern across early-pathway initiation (C1q, C2, C4) and terminal effector (C9) is structurally orthogonal to the alternative-pathway-amplification axis where CFH operates.

**Polyphenolic / lignan binding mode:** the benzofuran-sesquilignan scaffold (3,5-disubstituted aromatic with phenylpropanoid side chains, multiple phenolic OH groups, glucosidic linkage at C-7'' for compounds 4 and 5 in this paper) is consistent with protein-binding via H-bond + π-stacking interactions to hydrophobic / aromatic pockets in C1q globular heads, C2/C4 active-site regions, and C3's TED-MG ring interfaces. None of these binding modes correspond to the CCP6-8 CRP-binding surface of CFH.

## Classification

**CFH-dependence: CFH-INDEPENDENT (Medium confidence — limited by single-anchor replication risk, not by mechanism uncertainty).**

The mechanism per Yin 2016 is clearly upstream / orthogonal to CFH. The Medium-vs-High confidence call is dominated by the **comp-018 Phase 2 INCONCLUSIVE replication verdict**: no independent group has reproduced the Yin 2016 CH50 9/40 μM benzofuran lignan finding on a matched assay format. Structurally-adjacent benzofuran lignans (*Styrax japonica* egonol, Min 2004 PMID 15643559) are 3.7× weaker. The mechanistic classification is robust *conditional on the Yin 2016 finding being correct*; the replication risk is the larger uncertainty.

**Predicted Y402H × Helicteres × incident gout interaction:** **negative direction (effect ≥ in carriers)** — predicted by mechanism (multi-target upstream-of-CFH), but with very wide uncertainty bands because (a) Helicteres benzofuran lignans are NOT dietary (Helicteres angustifolia is a tropical Sterculiaceae plant from southern China/India/SE Asia, used in folk medicine but not widely consumed as food); (b) the single-paper finding has not been independently replicated; (c) UK Biobank Oxford WebQ does not capture Helicteres exposure. **The candidate is the wrong shape for the UKB cross-tab anyway** — it would need a focused Chinese/SE Asian folk-medicine-user cohort, not a UK dietary panel.

**Falsification threshold:** for this candidate, the more urgent falsification is the **independent wet-lab replication of Yin 2016** before the Y402H cross-tab is run at all (comp-018 Phase 2 already flagged this). If replication confirms the CH50 9/40 μM activity and target identification, the CFH-independence classification follows directly from the binding-target pattern.

**Confidence:** Medium. Mechanism is clear from Yin 2016. Replication risk is the dominant uncertainty source.

## Multi-hypothesis discipline — rejected alternative

**Rejected hypothesis: Helicteres benzofuran lignans act via CFH binding-site competition (CCP6-8 occupation displacing CRP / GAG).** Would predict CFH-dependence. **Rejected** because: (a) the Yin 2016 depletion-rescue data identifies C1q, C2, C3, C4, C9 as targets — none of which involve CFH; (b) if compounds 4 / 5 worked by CFH-binding-site competition, the alternative pathway should be specifically inhibited (CFH is AP-specific), but the experimentally measured CH50 (classical-pathway) is the more potent activity (9 μM CH50 vs 21 μM AP50 for compound 5), inconsistent with a CFH-binding-surface mechanism; (c) no surveyed paper mentions CFH as a Helicteres-lignan target.

## Limitations

- **Single-paper anchor; comp-018 Phase 2 verdict = INCONCLUSIVE replication.** Independent wet-lab replication on Yin 2016's CH50 9/40 μM activity is the load-bearing first step. The CFH-dependence classification rests on this paper holding up.
- Binding site at single-residue resolution is not characterized. Depletion-rescue identifies "the cascade component whose absence rescues hemolysis" but does not pin the specific epitope.
- Helicteres is **not dietary in any meaningful sense for OE's UKB cross-tab strategy.** Even if mechanism is CFH-independent, the candidate is not actionable through dietary intake adjustment — it would need to be a herbal-supplement / formulated-product channel.
- The Yin 2016 paper does not report Y402H × Helicteres carrier-stratification data. Classification is mechanistic extrapolation from binding-target identification.

## Evidence-tier summary

- **In Vitro:** Yin 2016 depletion-rescue target identification + CH50/AP50 hemolytic IC50 (PMID 27834928, PMC6273495) — single-paper anchor, target-identification approach is methodologically sound (Calbiochem antisera, NHS source).
- **Mechanistic Extrapolation:** CFH-independence in Y402H carriers — Medium confidence; mechanism is clear from binding-target data, replication risk is the dominant uncertainty source.
- **Operational note:** the candidate's CFH-classification value is limited by the fact that Helicteres is not part of dietary exposure tractable in UKB. The candidate is more relevant to a future TCM-supplement clinical-context evaluation than to the present UKB CFH × diet × gout cross-tab.
