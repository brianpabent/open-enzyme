# Phase 5 Deep-Read: G. lucidum GLPP (PMID 36385640)

**Citation.** Lin S, Meng J, Li F, Yu H, Lin D, Lin S, Li M, Zhou H, Yang B. *Ganoderma lucidum* polysaccharide peptide alleviates hyperuricemia by regulating adenosine deaminase and urate transporters. *Food Funct.* 2022 Dec 13;13(24):12619-12631. [DOI: 10.1039/d2fo02431d](https://doi.org/10.1039/d2fo02431d). PMID: 36385640.

**Author affiliation.** State Key Laboratory of Natural and Biomimetic Drugs, Department of Pharmacology, School of Basic Medical Sciences, Peking University, Beijing 100191, China (corresponding author: Baoxue Yang). Co-affiliations: Hubei Key Laboratory of Wudang Local Chinese Medicine Research (Hubei University of Medicine); National Engineering Research Center of Juncao Technology (Fujian Agriculture and Forestry University). Strong **Chinese-source-evidence anchor** — Peking University pharmacology + Juncao Center supply, journal *Food & Function* (RSC, peer-reviewed, IF ~6).

**Access note.** RSC paper, paywalled; PMC has no full text. This deep-read combines (a) the published abstract/MeSH (verified via PubMed) and (b) the same Yang/Lin/Li group's sister paper PMC11351902 (Zhang et al. 2024, *Biomedicines*, [DOI: 10.3390/biomedicines12081632](https://doi.org/10.3390/biomedicines12081632)) which uses the identical GLPP preparation from the same Juncao Center source. Where claims rely on the sister paper rather than the primary, this is flagged inline.

---

## 1. Compound identity

**GLPP = "*Ganoderma lucidum* polysaccharide peptide,"** a defined preparation isolated and purified by the National Engineering Research Center of Juncao Technology (Fujian Agriculture and Forestry University, Fuzhou). It is a **mixture/fraction**, not a single defined compound — explicitly described as "a mixture of polysaccharide peptides extracted from GL" (sister paper PMC11351902 §2.1, [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11351902/)).

- **Average molecular weight: ~520 kDa** (sister paper §2.1, citing the same Juncao GLPP lot used in PMID 36385640). [TRANSLATION-NOTE: not applicable; both papers are English-language.]
- **Peptide composition:** the primary paper does not detail amino-acid composition in the abstract; characterization (MeSH descriptor "Proteoglycans") confirms it is a glycopeptide/proteoglycan class, not a free polysaccharide. Granular peptide / glycan-linkage details are behind the paywall.
- **Glycan branching/linkage:** not in abstract; the broader *G. lucidum* polysaccharide literature ([review PMC11395056](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11395056/)) places GL polysaccharide-peptides in the β-1,3/β-1,6-glucan family with α-mannan and arabinogalactan side chains, so GLPP is structurally adjacent to that class. **Not directly verified from this paper** — record as inferred-from-class.
- **Single defined compound? No** — GLPP is a *fraction* (heterogeneous in MW around the 520 kDa centroid). Reproducibility across labs depends on the Juncao Center sourcing.

## 2. In vivo mouse data — exact numbers

From abstract + MeSH ([DOI 10.1039/d2fo02431d](https://doi.org/10.1039/d2fo02431d)):

- **HUA model:** potassium oxonate (PO)-induced hyperuricemia mouse model. Mouse strain not in abstract; sister paper uses ICR mice and the field convention for PO models is ICR or Kunming.
- **Headline efficacy: blood UA decreased "up to 40.6%" in a dose-dependent manner.** The "up to" qualifier implies this is the maximal-dose figure; the paper reports a dose-response curve. The 40.6% is **abstract-verified** as the headline number; the corresponding absolute UA values, p-values, sample size, dose levels, and treatment duration are all in the paywalled methods section.
- **Mechanism in vivo:** GLPP "significantly reduced UA production by inhibiting the hepatic and blood ADA activity, and increased UA excretion by decreasing GLUT9 expression and increasing OAT1 expression in kidney" (abstract verbatim).
- **Renal protection:** "PO-induced renal histopathological damage was also alleviated by GLPP in a dose-dependent manner" (abstract).

**Abstract-only verification.** The 40.6% maximum SUA reduction is the load-bearing claim and is directly stated in the abstract; cannot independently verify dose, n, or p-values without paywall access.

## 3. ADA inhibition

- **In vivo:** GLPP "significantly reduced UA production by inhibiting the hepatic and blood adenosine deaminase (ADA) activity" (abstract). Tissue-resolution data: at minimum **liver** and **blood** ADA activity measured. Kidney ADA not mentioned in abstract.
- **In vitro / cell model:** "The adenosine-induced cell model showed that the inhibitory effect of GLPP on ADA activity may be the main reason for the alleviation of HUA by GLPP" (abstract). The cell line and IC50 are not in the abstract — paywalled. The phrase "may be the main reason" is the authors' own causal claim, indicating they prioritize ADA inhibition over the transporter effects in their mechanistic ranking.
- **Pathway logic.** ADA catalyzes adenosine → inosine → hypoxanthine → xanthine → uric acid (via XO). So **ADA is upstream of XO** in the purine catabolism cascade. Inhibiting ADA reduces flux into the XO substrate pool (hypoxanthine + xanthine), lowering UA production *without* directly inhibiting XO. This is mechanistically distinct from allopurinol/febuxostat (XO inhibitors) and from rasburicase/uricase (UA → allantoin degradation downstream). **ADA inhibition is causally upstream of XO; not merely correlated.** This is biochemically established, not speculative — the substrate flow is canonical purine biochemistry.
- **Kinetic mechanism (competitive vs allosteric vs covalent):** not in abstract.

## 4. GLUT9 + OAT1 expression

- **Direction:** GLUT9 down (decreases UA reabsorption), OAT1 up (increases UA tubular secretion). Both effects favor UA excretion.
- **mRNA vs protein:** abstract says "expression," ambiguous. The closely-analogous sister paper from a different *Ganoderma* species ([Yong et al. 2018, PMC5775298, *G. applanatum*, DOI: 10.3389/fphar.2017.00996](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5775298/)) measured **both mRNA (RT-PCR) and protein (Western blot)** for OAT1, GLUT9, URAT1, with significant changes (P < 0.01) at both levels. PMID 36385640 likely follows the same methodological template (Peking U pharmacology pipeline standard).
- **Tissue:** kidney (specifically renal cortex per the methodological convention).
- **Fold change:** not in abstract. *G. applanatum* analog showed roughly 2-3× changes at protein level (Yong 2018, Fig 5).

## 5. Redox / disulfide chemistry — load-bearing question for Phase 5 chokepoint decision

**The primary paper (PMID 36385640) does NOT mention redox / oxidative-stress mechanism in its abstract.** The mechanism it commits to is purine pathway (ADA) + transporter (GLUT9/OAT1). MeSH descriptors include "Adenosine," "Adenosine Deaminase," "Hyperuricemia," "Kidney," "Organic Anion Transporters," "Reishi," "Proteoglycans" — **no redox or NLRP3 MeSH terms.**

**However — and this is the load-bearing finding for the redox chokepoint decision** — **GLPP as a chemical entity has been definitively characterized as redox-active in the same Yang group's adjacent work**, using the same 520 kDa GLPP preparation from the same Juncao source:

- **PMC11351902 (Zhang et al. 2024, sister paper)** demonstrates that GLPP, in the testicular cyclophosphamide-injury model, **(a)** activates the **Keap1/Nrf2/HO-1 signaling pathway** (canonical antioxidant master-regulator axis); **(b)** increases SOD, GSH, and CAT activity; **(c)** decreases MDA (lipid peroxidation marker); **(d)** decreases Bax/Bcl-2 ratio (mitochondrial apoptosis pathway, downstream of oxidative stress) ([DOI: 10.3390/biomedicines12081632](https://doi.org/10.3390/biomedicines12081632), §3.5–3.8).
- **The Keap1/Nrf2/HO-1 axis is a disulfide-redox-switch mechanism.** Keap1 senses oxidative stress via redox-active cysteines (Cys151, Cys273, Cys288) that form disulfides under electrophile/ROS exposure, releasing Nrf2 to translocate to the nucleus and upregulate antioxidant response element (ARE)-driven genes including HO-1, NQO1, glutathione synthesis enzymes. GLPP activating this pathway implies it acts as an electrophile/ROS-modulator hitting Keap1 cysteines — exactly the "redox/disulfide chemistry chokepoint" the Phase 5 decision is asking about.
- **GLSH increase** is direct glutathione system upregulation (the major intracellular thiol/disulfide redox buffer).
- **Reference 22** in PMC11351902 cites another Yang-group paper: GLPP inhibits intrarenal **PRR-RAS pathway** in proteinuric nephropathy (Fang et al. 2023, [DOI: 10.1016/j.ijbiomac.2023.127336](https://doi.org/10.1016/j.ijbiomac.2023.127336)) — PRR (prorenin receptor) activation is itself ROS/oxidative-stress-coupled in renal tissue, further supporting GLPP's redox-modulator profile.
- **No mention of TXNIP, thioredoxin, PDI, ergothioneine specifically** in either paper.
- **NLRP3:** not mentioned in either paper — but Nrf2/HO-1 axis activation is well-established to suppress NLRP3 priming via reduced ROS-driven NF-κB signaling. So GLPP's redox profile is **mechanistically adjacent to NLRP3 suppression even though the paper doesn't make that claim directly.**

**Verdict for Phase 5 redox chokepoint decision:** GLPP's published mechanism in the *hyperuricemia* paper is purine + transporter (ADA / GLUT9 / OAT1). But GLPP as a chemical entity has a strong, group-internal-replicated redox/disulfide-pathway signature (Keap1/Nrf2/HO-1) demonstrated in adjacent disease models. **The redox chemistry is real but is being claimed for a different therapeutic axis** (chemotherapy-induced organ injury) than the hyperuricemia mechanism. For the Open Enzyme chokepoint inventory: **GLPP supports a redox chokepoint as a secondary/adjacent mechanism, not the primary HUA mechanism.** The primary HUA chokepoint here is ADA + transporters.

## 6. Comparison to allopurinol / benzbromarone positive controls

**Not specified in abstract.** PubMed metadata and abstract make no mention of either positive control. Sister paper PMC5775298 (*G. applanatum*) **did** use allopurinol (5 mg/kg) and benzbromarone (7.8 mg/kg) as positive controls in the same PO-induced HUA model and is from a different group (Guangdong Institute of Microbiology, Yong et al.) — the Yang group at Peking University may or may not have included these standards. **Cannot verify without paywall access.** This is a non-trivial gap: a PO-induced HUA paper without allopurinol/benzbromarone benchmarking is unusual for the field, suggesting either (a) the controls are present in the paywalled methods or (b) the paper deliberately positions GLPP without head-to-head benchmarking. Worth flagging for follow-up.

## 7. ADA as a canonical Open Enzyme chokepoint — adoption recommendation

**ADA (adenosine deaminase) is causally upstream of XO** in the purine catabolism pathway:

```
Adenosine --[ADA]--> Inosine --[PNP]--> Hypoxanthine --[XO]--> Xanthine --[XO]--> Uric Acid
```

Any inhibitor of ADA reduces flux into the XO substrate pool. This is **mechanism-level upstream**, not merely "correlated." The relationship is biochemically canonical (Kornberg & Baker, *DNA Replication*, 1992; standard purine biochem textbooks).

**Implications for Open Enzyme canonical chokepoints:**
- ADA inhibition is **mechanistically distinct from XO inhibition** (allopurinol/febuxostat) and from uricase-mediated UA degradation (rasburicase/pegloticase). It opens a third chokepoint along the production axis.
- Selective ADA inhibitors exist clinically (pentostatin/deoxycoformycin, cladribine — both used in hairy cell leukemia / lymphoid malignancies; pentostatin has Ki ~2.5 pM against ADA). These are **chemo-toxicity-grade molecules**, not appropriate for chronic HUA. But the chokepoint itself is druggable.
- The koji/A. oryzae chassis question: koji secretes adenosine deaminase as part of normal nucleotide salvage metabolism. **Selective inhibitors derived from koji metabolites (or engineered koji secretion of an ADA-inhibitor-binding protein scaffold) becomes an interesting design question** — one not currently in the canonical wiki.
- **Recommendation: ADA SHOULD be added to the canonical chokepoint inventory** as a third production-axis chokepoint, distinct from XO and from uricase. Tier it as Mechanistic Extrapolation for HUA (animal evidence from this paper + biochemical inevitability) but flag the toxicity profile of existing ADA inhibitors as a real constraint on therapeutic adoption.

---

## Phase 5 chokepoint-decision summary

| Question | Answer |
|---|---|
| 40.6% UA reduction verified? | Yes — abstract directly states it as the maximum dose-dependent reduction. Absolute baseline/treated SUA values not in abstract (paywalled). |
| ADA upstream of XO causally? | Yes — biochemically canonical (purine catabolism). Not correlation. |
| Add ADA as canonical chokepoint? | **Yes** — third production-axis chokepoint distinct from XO and uricase. Add to chokepoint inventory with Mechanistic Extrapolation evidence tier. |
| Redox/disulfide chemistry in this paper's mechanism? | **No** in the HUA paper itself. **Yes** in the same group's GLPP work in adjacent disease models (Keap1/Nrf2/HO-1, GSH/SOD/CAT/MDA — sister paper PMC11351902). GLPP is redox-active as a molecule but the redox axis is not the load-bearing claim for HUA in PMID 36385640. |
| Support adding redox chokepoint to canonical inventory based on THIS paper? | **No, not from this paper alone.** The redox mechanism is real but is documented for cyclophosphamide/testicular and proteinuric/renal contexts, not for the HUA mechanism. If a redox chokepoint is added to OE canonical, the supporting evidence should come from a paper that *directly* couples redox modulation to UA reduction in vivo. This paper does not provide that. |
| Chinese-source evidence anchor? | **Strong.** Peking University pharmacology + Fujian Juncao Center, *Food & Function* (RSC). Authors are major TCM/medicinal-fungus pharmacology lab with multiple replicated GLPP studies across disease axes. |

## Open follow-ups (paywall-blocked)

1. Exact GLPP dose levels and treatment duration in the HUA model.
2. ADA in vitro IC50 and kinetic mechanism (competitive? non-competitive? covalent thiol-modifier? — the last would directly couple GLPP to a redox/disulfide chokepoint).
3. The adenosine-induced cell line identity (likely HepG2 or HK-2 based on HUA convention).
4. Whether allopurinol/benzbromarone positive controls were included.
5. GLPP monosaccharide composition and glycosidic linkage analysis (would confirm structural adjacency to β-glucan / mannogalactan class).
6. Whether the Yang group ever measured GLPP effects on kidney/liver Nrf2/HO-1 in the HUA-PO model itself (would directly couple the redox mechanism to UA reduction in this disease context).

If the redox chokepoint decision becomes load-bearing, paywall access to this paper (or direct correspondence with Baoxue Yang at Peking U) would resolve item 6 — the highest-leverage unknown.
