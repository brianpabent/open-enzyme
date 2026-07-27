# Luteolin — Model A source read (CFH-dependence classification)

**Date:** 2026-05-21
**Author:** Claude Opus 4.7 (Model A in two-model cross-check protocol)
**Scope:** comp-039 mechanism-dissociation classification — does luteolin's anti-complement mechanism require functional CFH (and therefore lose efficacy in Y402H carriers), or does it bypass CFH?

## Primary sources read

1. **Zhang T, Chen DF.** Anticomplementary principles of a Chinese multiherb remedy for the treatment and prevention of SARS. *J Ethnopharmacol* 2008;117(2):351–61. PMID 18400428 / PMC7126446 — full text read.
2. **Pieroni A, Heimler D, Pieters L, van Poel B, Vlietinck AJ.** In vitro anti-complementary activity of flavonoids from olive (Olea europaea L.) leaves. *Farmaco* 1996;51(11):765–8. PMID 8941947 — abstract only (no PMC).
3. **Park JC, Yu YB, Lee JH, Hattori M, Lee CK, Choi JW.** Effect of flavonoids from olive on complement activation. (Background-corpus convergence with Zhang 2008.)

## Binding-site evidence

**Zhang 2008 (PMC7126446):** luteolin tested in a matched sheep-erythrocyte (CP) + rabbit-erythrocyte (AP) hemolytic assay format using guinea-pig serum (CP) and 1:10 normal human serum (AP). Results:

> Verbatim: "luteolin was found to have most strong anticomplementary activity with CH50 value of 0.19 mM. ... On the AP of complement system, ... luteolin showed higher activity with AP50 values of less than 1 mM [0.17 mM]."

The paper does **not** identify the specific complement-cascade target for luteolin — it confirms broad classical-pathway + alternative-pathway inhibition at hundred-micromolar potency. The discussion attributes activity to the **4'-OH** functional group on the B ring of flavonoids (consistent with the parallel Yin 2016 / Helicteres finding that flavonoids with 4'-OH are more active than those with -OCH3 at C-4'). No mention of CFH or Factor H anywhere in the paper.

**Mechanism class:** broad-spectrum flavonoid complement inhibitor. The CP and AP IC50s being nearly equal (0.19 vs 0.17 mM) suggests luteolin is acting on a node shared by both pathways — most likely **C3 itself** or **the active site of the C3/C5 convertases** (both pathways converge at C3b deposition and amplification).

## Mechanism mapping vs CFH Y402H footprint

CFH Y402 (CCP7) binds CRP and host glycosaminoglycans. CFH regulates surface-deposited C3b via decay-acceleration of C3bBb and Factor-I cofactor activity for C3b → iC3b conversion.

Luteolin's mechanism is **not pinned to a specific site** in the surveyed primary literature. The two structurally plausible attribution candidates are:

(a) **Active-site or substrate-binding inhibition of C3 convertase formation/catalysis.** This would be CFH-independent — same logic as rosmarinic acid's Englberger 1988 C3-convertase inhibition.

(b) **Generic surface adsorption / nonspecific complement-protein binding of polyphenols** — most flavonoids have promiscuous protein-binding profiles, especially the 4'-OH catechol-like flavones. This would be CFH-orthogonal but also could include some CFH-binding-surface effects.

Neither mechanism category implies dependence on a functional CFH-CRP-GAG bridging step. The AMD analog mechanism (zinc + CRP + functional CFH) requires the zinc-induced complement-inactivation pathway, which is specific to AREDS/DHA pharmacology and not characteristic of polyphenol direct-binding complement inhibition.

**Urate-axis boundary:** The former COMP-013 XO potency and URAT1 attribution are invalid and cannot establish a parallel luteolin mechanism. This read therefore supports only the bounded complement interpretation below. Any urate-production or urate-transport claim requires separate primary-source qualification and mechanism-matched evidence.

## Classification

**CFH-dependence: CFH-INDEPENDENT (Medium confidence).**

Lower confidence than rosmarinic acid because: (a) the primary literature does not pin the binding site at single-residue resolution; (b) the broad CP+AP activity could in principle include weak CFH-binding-surface effects. The available complement evidence points toward convertase-level inhibition (CFH-independent), while the AMD-paradox mechanism (zinc-CRP-CFH bridging) is specific to AREDS pharmacology.

**Predicted Y402H × luteolin × incident gout interaction:** **negative direction (effect ≥ in carriers)** — predicted from the complement interpretation, with wider uncertainty than rosmarinic acid because the mechanism site is ambiguous. **Falsification threshold:** UK Biobank candidate-stratified cross-tab HR > 1.4 (Y402HH × luteolin-rich diet vs Y402YY × luteolin-rich diet) would warrant retiring luteolin from the CFH-bypass upstream-CP0 candidate set.

**Confidence:** Medium. Mechanism-site evidence is at "broad CP+AP inhibition" granularity, not C3b-thioester or convertase-active-site granularity.

## Multi-hypothesis discipline — rejected alternative

**Rejected hypothesis: luteolin binds the CCP6-8 CRP-binding surface of CFH itself, competing with CRP for the Y402-adjacent surface.** Would predict CFH-DEPENDENT mechanism. **Weakly rejected** because: (a) flavonoid promiscuous binding could in principle hit CCP7, but no surveyed paper reports CFH as a luteolin target; (b) the AP-pathway inhibition in Zhang 2008 (AP50 = 0.17 mM) is in a serum context (1:10 NHS) where CFH is present and functional — if luteolin worked by competing with CFH for C3b, AP inhibition would be expected to *fall* once CFH is saturated, not match CP inhibition; the matched CP/AP IC50 implies a node common to both pathways (C3 itself or convertase active site), not a CFH-competitive site. Verdict: structurally implausible but not formally falsified — flagged as residual uncertainty in the Medium confidence.

## Limitations

- Luteolin binding site at single-residue resolution is unresolved in the surveyed primary literature.
- Bioavailability of dietary luteolin is reportedly low (chrysanthemum, celery, parsley sources); the operative tissue concentration in a gout flare context is unknown.
- The surveyed complement sources do not establish any parallel urate-production or urate-transport mode. A genotype-by-exposure analysis must therefore remain complement-specific unless separate primary evidence qualifies another mechanism.

## Evidence-tier summary

- **In Vitro:** Zhang 2008 CP+AP hemolytic inhibition (PMID 18400428, PMC7126446) — direct hemolytic functional evidence; mechanism node not pinned.
- **In Vitro:** Pieroni 1996 olive-leaf flavonoid complement inhibition (PMID 8941947) — replicates flavonoid class activity.
- **Mechanistic Extrapolation:** CFH-independence in Y402H carriers — Medium confidence; mechanism site under-resolved at single-residue level, but available evidence points to convertase-level inhibition not CFH-binding-surface displacement.
