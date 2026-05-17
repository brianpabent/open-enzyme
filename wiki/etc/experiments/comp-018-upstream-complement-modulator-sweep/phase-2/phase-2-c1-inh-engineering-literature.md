# comp-018 Phase 2 — C1-INH Parallel Engineering Literature Thread

**Date:** 2026-05-17
**Scope:** Literature side of the C1-INH parallel-engineering proposal. Anchors the chronology of recombinant SERPING1 / C1-INH expression precedents, glycosylation-deficient variant activity data, and luminal/mucosal delivery precedents. Companion to the concurrent comp-037 computational track (C1-INH protease-stability run by main agent).

**Why this track exists:** comp-018 Phase 1 §7.4 proposed a "near-twin engineering thesis to DAF SCR1-4 (H05): recombinant C1-INH expression as a second CP0 engineering candidate operating at a different complement node." Phase 1 named the FDA-approved precedents (Berinert plasma-derived; Cinryze plasma-derived; Ruconest transgenic-rabbit-milk-derived) but did not chronologise the heterologous-expression literature. Phase 2 closes that gap.

**Strategic frame:** If recombinant C1-INH can be expressed in food-grade or LBP chassis with retained activity, OE gains a second CP0 engineering thread (in addition to DAF/CD55 SCR1-4) that operates at a different complement node (classical / lectin pathway proteases C1r/C1s/MASP-1/MASP-2 + the contact-system / kinin-system serpin function). The literature-side question: what's the precedent envelope?

---

## TL;DR (one paragraph)

**The recombinant human C1-INH heterologous-expression precedent landscape is dominated by three approaches:** (1) **Pichia pastoris** — the Bos 2003 anchor paper (PMID 12758149) demonstrates 30-180 mg/L active rhC1-INH with same inhibitory capacity as plasma C1-INH for C1s + kallikrein + Factor XIIa + Factor XIa, despite differences in glycosylation. (2) **Transgenic rabbit milk** — the commercialized Ruconest / conestat alfa pathway (Pharming, Netherlands → FDA 2014), with N-glycan profile that differs from plasma-derived C1-INH but retains protease inhibitor function. (3) **Plasma-derived** — Berinert (CSL Behring) and Cinryze (Shire/Takeda) remain the FDA-approved gold standard. Critical Phase 2 finding for the OE platform: **N-linked glycosylation is NOT required for C1-INH protease-inhibitor function but IS required for the heavily-glycosylated N-terminal-domain-mediated LPS-binding endotoxin-protective function** (Liu 2004 PMID 15039314). For a luminal-CP0 application targeting MSU-driven complement activation in joint or gut, the protease-inhibitor function is the load-bearing activity; the LPS-binding function is incidental. **This means a deglycosylated or differently-glycosylated yeast-expressed (Pichia or koji) C1-INH retains the load-bearing function for the OE platform's CP0 use case.**

---

## §1. The C1-INH protein (background for the engineering thread)

C1 inhibitor (C1-INH, gene SERPING1, UniProt P05155) is a 478-residue serpin (serine protease inhibitor) that:

- **Inhibits the classical pathway initiator proteases** C1r and C1s — forming covalent suicide-substrate complexes that consume the protease and leave a cleaved C1-INH inactivated
- **Inhibits the lectin pathway initiator proteases** MASP-1 and MASP-2 — same mechanism
- **Inhibits the contact-system serine proteases** Factor XIIa, plasma kallikrein, and Factor XIa — relevant to bradykinin generation in hereditary angioedema (HAE)
- **Inhibits the fibrinolysis serine protease** plasmin — secondary activity
- Has a **heavily-glycosylated N-terminal "mucin-like" domain** (residues 1-113, with 7 N-linked and ~24 O-linked glycosylation sites) that mediates LPS binding and lipid-A-mediated endotoxin protection (Liu 2004 PMID 15039314, [doi:10.1128/IAI.72.4.1946-1955.2004](https://doi.org/10.1128/IAI.72.4.1946-1955.2004))
- Has a **C-terminal serpin domain** (residues 114-478) that performs the protease-inhibitor function. This is the homologous-to-serpin-family region

**Implication for engineering chassis choice:** The N-terminal mucin-like domain's heavy glycosylation is a known engineering risk for non-mammalian chassis (Pichia, koji, Lactococcus). The Liu 2004 finding (N-glycan removal does NOT abolish protease-inhibitor function, DOES abolish LPS-binding endotoxin protection) tells us the engineering question is which function the platform needs.

**For OE platform CP0 use case (MSU-driven complement activation):** protease-inhibitor function on C1r/C1s + MASP-1/MASP-2 is the load-bearing activity. LPS-binding endotoxin protection is incidental. Therefore N-glycan-deficient or differently-glycosylated yeast / koji / LBP-expressed C1-INH should retain the platform-relevant function.

---

## §2. Heterologous expression chronology (load-bearing literature anchors)

### §2.1 Pichia pastoris — Bos et al. 2003 (load-bearing anchor)

**Bos IGA, de Bruin EC, Karuntu YA, Modderman PW, Eldering E, Hack CE. Recombinant human C1-inhibitor produced in Pichia pastoris has the same inhibitory capacity as plasma C1-inhibitor. Biochim Biophys Acta 1648(1-2):75-83 (2003). PMID 12758149, [doi:10.1016/s1570-9639(03)00107-9](https://doi.org/10.1016/s1570-9639(03)00107-9). Sanquin Research at CLB / Landsteiner Laboratory, AMC University of Amsterdam, Netherlands.**

**Key findings:**
- Maximum yield: **180 mg/L** active rhC1-INH in Pichia pastoris fermentation
- Average yield: **30 mg/L** of 80-100% active C1-INH
- Inhibitory kinetics identical to plasma C1-INH for C1s, kallikrein, coagulation factor XIIa, and XIa (progress-curve analysis)
- Structural integrity comparable to plasma C1-INH as monitored by heat stability, **despite differences in extent and nature of glycosylation**
- Earlier attempts to produce high levels of C1-INH (in CHO, mammalian cells) had resulted in predominantly INACTIVE protein — Pichia overcomes this constraint

**Why this is the load-bearing anchor for the OE thread:** Pichia is a yeast — same Sub-Phylum (Saccharomycotina, Ascomycota) as Aspergillus oryzae (koji, the OE primary chassis), and same trophic kingdom-relationship constraints. The fact that Pichia can produce active C1-INH at 30-180 mg/L means the secretory and folding machinery in a yeast / Ascomycota chassis is sufficient for active C1-INH production. This is direct precedent that the OE koji thread can plausibly express active C1-INH.

**Glycosylation observation:** Pichia uses high-mannose N-linked glycosylation (5-10 mannoses per N-glycan, in contrast to mammalian sialylated complex N-glycans). The Bos 2003 paper reports this difference but the protease-inhibitor activity is preserved. **Combined with Liu 2004 (N-deglycosylated C1-INH retains protease-inhibitor activity, loses LPS-binding endotoxin protection), this means the platform's CP0-relevant function is robust to glycan-pattern differences between mammalian and yeast hosts.**

**verification_status:** abstract-tier (PMID 12758149 abstract accessed; full-text not retrieved in Phase 2 but the abstract states all load-bearing numbers). For wet-lab gating, full-text retrieval mandatory.

### §2.2 Transgenic rabbit milk — Conestat alfa (Ruconest, commercialized)

**Cancian M. Diagnostic and therapeutic management of hereditary angioedema due to C1-inhibitor deficiency: the Italian experience. Curr Opin Allergy Clin Immunol 15(4):383-91 (2015). PMID 26106828, [doi:10.1097/ACI.0000000000000186](https://doi.org/10.1097/ACI.0000000000000186).**

**Key findings:**
- Ruconest (conestat alfa) is recombinant human C1-INH produced from the milk of transgenic rabbits (Pharming Group N.V., Leiden, Netherlands)
- FDA approval: 2014 for treatment of acute HAE attacks in adults and adolescents
- Differs from plasma-derived C1-INH (Berinert, Cinryze) in N-glycan structure (rabbit-mammalian glycan pattern with some non-human galactose-α1,3-galactose epitopes, hence the very-rare anti-drug-antibody risk in patients with rabbit allergy)
- Despite different glycosylation, retains C1s / kallikrein / Factor XIIa / Factor XIa inhibitor function

**Why this matters for the OE platform:** Ruconest demonstrates that NON-PLASMA-DERIVED recombinant C1-INH with non-human glycosylation patterns is sufficient for the protease-inhibitor function at clinical efficacy. This is regulatory precedent that the FDA approves recombinant C1-INH with non-human glycosylation. The OE platform's koji-expressed (mannose-rich, non-mammalian) C1-INH could plausibly follow a similar regulatory path provided the protease-inhibitor function is demonstrated.

**verification_status:** abstract-tier (review article PMID 26106828 abstract). Ruconest FDA approval and Pharming Group manufacturing are widely documented public-domain facts; full-text not load-bearing.

### §2.3 Other heterologous expression literature surface

Phase 2 PubMed searches returned **no PMC-mirrored papers on** Lactococcus / E. coli / Bacillus expression of C1-INH. This is empirically a gap — the C1-INH heterologous expression literature is dominated by Pichia + mammalian + transgenic-animal-milk approaches, with no documented bacterial or other-yeast (Saccharomyces cerevisiae, Hansenula polymorpha, Schizosaccharomyces pombe) precedents in the searchable corpus.

**Inference:** the heavily-glycosylated mucin-like N-terminal domain is a known barrier for bacterial expression (no N-glycosylation machinery in E. coli), and the serpin reactive-center-loop conformation is a known folding challenge that prefers eukaryotic secretory pathway machinery. Yeast (Pichia, plausibly koji) is the empirically-validated chassis. **The Lactococcus / LBP route for C1-INH is novel and unprecedented; expressing it would require either (a) demonstrating N-glycan-deficient C1-INH retains activity in a Lactococcus-secreted form, or (b) co-expressing the glycosylation machinery — substantially harder.**

### §2.4 Plasma-derived C1-INH (Berinert, Cinryze) as regulatory and biological benchmark

Phase 1 named these. Phase 2 adds: plasma-derived C1-INH has full native N-glycan profile (sialylated complex N-glycans), is FDA-approved for HAE acute attacks and prophylaxis, and serves as the kinetic and activity reference point for all recombinant comparisons. Yields are limited by donor plasma availability and processing cost.

---

## §3. Glycosylation-deficient C1-INH activity (load-bearing for OE platform)

### §3.1 Liu et al. 2004 — N-linked glycosylation required for endotoxin protection, NOT required for protease-inhibitor function

**Liu D, Gu X, Scafidi J, Davis AE. N-linked glycosylation is required for C1 inhibitor-mediated protection from endotoxin shock in mice. Infect Immun 72(4):1946-1955 (2004). PMID 15039314, PMC375168, [doi:10.1128/IAI.72.4.1946-1955.2004](https://doi.org/10.1128/IAI.72.4.1946-1955.2004). CBR Institute for Biomedical Research, Harvard Medical School.**

**Key findings:**
- C1-INH protects mice from endotoxin shock via direct interaction with LPS — this interaction requires the heavily-glycosylated amino-terminal mucin-like domain
- C1-INH in which N-linked carbohydrate was removed by N-glycosidase F treatment was markedly LESS effective in LPS protection
- N-deglycosylated C1-INH ALSO failed to suppress FITC-LPS binding to RAW 264.7 macrophages and human whole blood
- N-deglycosylated C1-INH bound to LPS very poorly in ELISA
- **N-deglycosylated C1-INH retained the rate and extent of complex formation with C1s (the protease-inhibitor function)**
- Removal of O-linked carbohydrate had no effect on any of these activities

**Critical extraction for OE platform:**

| Function | Native (glycosylated) C1-INH | N-deglycosylated C1-INH | Implication for OE platform |
|---|---|---|---|
| C1s protease inhibition (suicide-substrate covalent binding) | Yes | **Yes — preserved** | OE koji/LBP-expressed C1-INH (mannose-rich or no N-glycan) RETAINS the load-bearing function for CP0 |
| Reactive-center-loop cleavage by trypsin | Same as native | Same as native | Structural integrity of the serpin domain is preserved without N-glycan |
| LPS binding (endotoxin protection) | Yes | **No — abolished** | Lost in deglycosylated form; not load-bearing for MSU-driven gout / CP0 use case |
| FITC-LPS binding to macrophages | Suppressed | Not suppressed | Same — not relevant to gout / CP0 |

**Verdict:** for the OE platform CP0 use case (preventing MSU-driven complement priming via classical-pathway protease inhibition), the load-bearing function is C1s / C1r / MASP-2 inhibition — which is robust to N-glycan loss. The LPS-binding endotoxin protection function — which would be a "nice-to-have" for septic-shock indications — is lost in deglycosylated forms but is incidental for gout. **This is a major risk-reduction finding for the koji / LBP engineering thread.**

### §3.2 The serpin reactive-center-loop conformation as the engineering risk concentration

The Liu 2004 finding is consistent with the general serpin literature: the **reactive-center loop (RCL) conformation** is the load-bearing structural feature for protease-inhibitor function, not the N-glycan pattern. Serpins fold with the RCL projecting out from the body of the molecule, get "stung" by the cognate protease in a Michaelis-like complex, and then undergo a massive conformational change (loop insertion into β-sheet A) that traps the protease and distorts its active site. This mechanism is glycan-pattern-independent.

**For OE koji expression:** the engineering risk is concentrated in the secretory-pathway folding of the serpin core, NOT in the N-glycan composition. Phase 1 comp-006 / comp-012 demonstrated low-protease-risk koji secretion for DAF/CD55 SCR1-4 (4× CCP/sushi domains, 8 disulfides). The C1-INH serpin domain is structurally distinct from CCP/sushi domains (no disulfides in the canonical serpin core; β-sheet A-mediated loop insertion mechanism) — different folding question. **The comp-037 concurrent computational track should address the serpin RCL stability and koji-secretion-pathway folding compatibility specifically.**

---

## §4. Luminal / mucosal delivery precedents for C1-INH

Phase 2 PubMed searches returned **no PMC-mirrored papers on inhaled / intranasal / luminal C1-INH delivery as established route**. The literature is dominated by IV bolus delivery for acute HAE attacks (Berinert, Cinryze, Ruconest) and subcutaneous prophylactic delivery (Cinryze SC, Haegarda).

**Inference for OE platform:** the LBP-luminal-C1-INH thesis (engineered Lactococcus / probiotic-chassis delivering C1-INH to the gut lumen for systemic absorption or local complement modulation) is **novel and without direct precedent**. The closest precedents are:

- **L. lactis-secreted human interleukin-10 in IBD trials** (Steidler et al. 2000 Science — proved the LBP-secretion concept for human cytokines)
- **L. lactis-secreted human elafin in IBD trials** (Bermúdez-Humarán 2015; elafin is a small serine protease inhibitor)
- **Probiotic-secreted human serpins in gut: no direct C1-INH precedent in the literature surveyed**

**Critical caveat for the LBP thesis:** the gut lumen has its own protease cocktail (pepsin, trypsin, chymotrypsin, elastase, pancreatic proteases) that would proteolytically cleave secreted C1-INH unless protected. Serpins are particularly vulnerable to this because their reactive-center loop is, by design, a protease-cleavable scaffold. Without protective formulation or co-expressed chaperone protection, LBP-luminal-C1-INH may be cleaved before it can reach the local complement system. **This is a substantial engineering risk that comp-037 (or a comp-037 sibling) should address computationally before wet-lab gating.**

---

## §5. Top-3 anchor citations for downstream propagation (comp-037 brief input)

For comp-037 (the concurrent C1-INH protease-stability computational track), the load-bearing literature anchors are:

| Rank | Citation | What it anchors | Verification status |
|---|---|---|---|
| **1** | Bos IGA et al. Biochim Biophys Acta 1648(1-2):75-83 (2003). PMID 12758149, [doi:10.1016/s1570-9639(03)00107-9](https://doi.org/10.1016/s1570-9639(03)00107-9) | Pichia pastoris yields 30-180 mg/L active rhC1-INH; same inhibitory capacity as plasma C1-INH despite different N-glycosylation; demonstrates yeast (Ascomycota) chassis is sufficient | abstract-tier (PMID abstract); full-text retrieval recommended before comp-037 commit |
| **2** | Liu D et al. Infect Immun 72(4):1946-1955 (2004). PMID 15039314, PMC375168, [doi:10.1128/IAI.72.4.1946-1955.2004](https://doi.org/10.1128/IAI.72.4.1946-1955.2004) | N-deglycosylated C1-INH RETAINS protease-inhibitor function but LOSES LPS-binding endotoxin protection. Major risk-reduction for koji / LBP chassis (mannose-rich or absent N-glycan) | abstract-tier + PMC mirror available (PMC375168); full-text grep-verify possible |
| **3** | Cancian M. Curr Opin Allergy Clin Immunol 15(4):383-91 (2015). PMID 26106828, [doi:10.1097/ACI.0000000000000186](https://doi.org/10.1097/ACI.0000000000000186) | Ruconest (conestat alfa) regulatory precedent — recombinant C1-INH from transgenic rabbit milk with non-human glycosylation pattern is FDA-approved (2014). Establishes the regulatory acceptability of non-mammalian-glycosylated C1-INH | abstract-tier |

**Each of these is sufficient for comp-037 brief-level anchoring. For wet-lab gating, full-text retrieval on PMID 12758149 + PMC375168 + Ruconest FDA package is mandatory.**

---

## §6. What the LBP-luminal-C1-INH thesis needs to address

Based on the Phase 2 literature pass, the LBP-luminal-C1-INH thesis has THREE load-bearing technical questions that need resolution before wet-lab gating:

1. **Can Lactococcus lactis (or another LBP chassis without N-glycosylation machinery) secrete a folded C1-INH variant with retained protease-inhibitor activity?**
   - Liu 2004 establishes that N-deglycosylation does NOT abolish protease-inhibitor activity — so an N-glycan-deficient C1-INH variant is mechanistically plausible
   - But Liu 2004 was a deglycosylation-after-secretion experiment, NOT a never-glycosylated-during-folding experiment — these differ. Folding of the serpin core might require N-glycan-mediated chaperone interactions during ER passage even if mature deglycosylated protein retains activity
   - **comp-037 should computationally evaluate this folding question**

2. **Can luminally-secreted C1-INH survive gut-lumen proteolysis long enough to function?**
   - Serpins are inherently protease-cleavable in the reactive-center loop region
   - Phase 2 surfaced no precedent for orally-delivered or luminally-secreted C1-INH
   - **comp-037 should computationally evaluate C1-INH RCL accessibility to gut-lumen proteases** (pepsin pH 1.5-3.0 in stomach; trypsin + chymotrypsin pH 7-8 in small intestine; pancreatic elastase; brush-border peptidases)

3. **What is the load-bearing site of action — gut lumen, gut-mucosal-immune interface, or systemic via gut-uptake?**
   - For MSU-driven gout (joint-localized complement priming), the load-bearing site is systemic
   - For inflammatory bowel disease (lumen-localized complement priming), the site is gut-mucosal
   - The platform's primary indication is gout — implies systemic-uptake or systemic-direct delivery (e.g., subcutaneous, intra-articular) is the more clinically aligned route
   - **The LBP-luminal thesis may need to be reframed as LBP-as-systemic-source rather than LBP-as-luminal-deliverer for the gout use case**

These three questions are inputs to the comp-037 brief and to any future LBP-C1-INH wet-lab scope. Phase 2 surfaces the literature gaps; comp-037 closes the mechanism gaps; wet-lab gates close the empirical gaps.

---

## §7. Cross-references

- Phase 1 wiki anchor: [`upstream-complement-modulator-sweep-computational.md`](../../../upstream-complement-modulator-sweep-computational.md) §7.4 (engineered C1-INH parallel thread proposed)
- comp-020 verification re-run: [`upstream-complement-verification-rerun-computational.md`](../../../upstream-complement-verification-rerun-computational.md)
- Phase 2 multilingual findings: [`./phase-2-multilingual-findings.md`](./phase-2-multilingual-findings.md)
- Helicteres replication: [`./phase-2-helicteres-replication.json`](./phase-2-helicteres-replication.json)
- comp-018 vs comp-020 retrospective: [`../../../../operations/comp-018-vs-comp-020-retrospective.md`](../../../../operations/comp-018-vs-comp-020-retrospective.md)
- DAF SCR1-4 parallel engineering thread: [`../../../daf-cd55-scr14-truncated-computational.md`](../../../daf-cd55-scr14-truncated-computational.md) (comp-012)
- H05 thesis card: [`../../../hypotheses/H05-daf-scr14-cp0-thesis.md`](../../../hypotheses/H05-daf-scr14-cp0-thesis.md)
- Complement strategic frame: [`../../../complement-c5a-gout.md`](../../../complement-c5a-gout.md)

---

## §8. Limitations

1. **Full-text retrieval was NOT performed on PMID 12758149 (Bos 2003 anchor).** All claims about Pichia rhC1-INH yields (30-180 mg/L) and kinetic parameters (same inhibitory capacity as plasma C1-INH) are abstract-tier per CLAUDE.md Rule 4. For wet-lab gating, full-text verification mandatory. Recommend pulling the full-text from BBA Proteins and Proteomics via paywall before comp-037 anchors propagate.

2. **The literature surveyed in Phase 2 is English-language.** A C1-INH heterologous expression paper in Chinese or Japanese vendor journals (e.g., 中华医学杂志 Zhonghua Yi Xue Za Zhi, 蛋白质与细胞 Protein & Cell) might exist with additional precedent. Phase 2 searches with explicit non-English term inclusion returned no novel anchors, but the survey is not exhaustive. Future Phase 3 multilingual could target this specifically.

3. **The "N-deglycosylated C1-INH retains protease-inhibitor function" finding from Liu 2004 was an in vitro and ex vivo demonstration with native-then-deglycosylated protein.** Whether a NEVER-GLYCOSYLATED-DURING-FOLDING protein (as would emerge from E. coli or Lactococcus secretion) retains the same activity is not directly demonstrated by Liu 2004. The Bos 2003 Pichia paper is more directly relevant because Pichia performs N-glycosylation (just in high-mannose pattern); a totally non-glycosylated chassis is a different evidence question. **This is a load-bearing distinction comp-037 should explicitly address.**

4. **No FDA-approved oral, mucosal, or LBP-delivered C1-INH product exists** as of Phase 2 search date (2026-05-17). All FDA-approved C1-INH products are IV or SC parenteral routes. The LBP-luminal-C1-INH thesis is novel and unprecedented at the regulatory level. This is not a deal-breaker but is an important platform-strategic observation: novel-route + novel-chassis combinations face higher regulatory hurdles than novel-chassis-with-established-route combinations.

5. **Phase 2 did not survey the AAV gene-therapy SERPING1 literature.** Adeno-associated-virus delivery of SERPING1 to liver hepatocytes for in vivo C1-INH production is an active clinical area (e.g., BMN331 from BioMarin). This is mechanistically distinct from heterologous-expression for production-then-administration, but is conceptually relevant for the OE platform if the "engineered organism delivering C1-INH" framing is generalized to "engineered delivery system delivering C1-INH-producing-organism / vector." Future Phase 3 could include AAV-SERPING1 as an adjacent precedent class.
