# Phase 5 Deep-Read: AMC-BFE Cordyceps×Astragalus (PMID 41905012, 2026)

**Citation.** Xia X, Song H, Meng Y, Xu C, Niu H, Liu X, Zhang G, Ling J. Biotransformation-derived metabolites from *Astragalus membranaceus* and *Cordyceps militaris* alleviate hyperuricemia via multi-target regulation. *Bioorg Chem* 175:109806 (2026). DOI [10.1016/j.bioorg.2026.109806](https://doi.org/10.1016/j.bioorg.2026.109806). PMID 41905012.

---

## ⚠️ Access caveat — read this first

**The full text of this paper is paywalled (Elsevier, no PMC deposit, no preprint mirror found as of 2026-05-06).** This deep-read therefore reconstructs the study from:

1. The PubMed abstract + MeSH + keywords (full text retrieved).
2. The methodological analog from the **same group**: Zhao X, Li X, Jia X, Gao Y. *Multi-omics and compositional analysis of bidirectional solid fermentation products from Cordyceps militaris and Panax quinquefolius L.* PMC12805540 (2025). Same Shandong group (Ling J, Zhang G are corresponding on the AMC-BFE paper; Zhao 2025 is the prior bidirectional-fermentation methods paper from the same lab consortium).
3. The literature ancestor for the *C. militaris* × URAT1 axis: Yong T et al. *Cordycepin… ameliorates Hyperuricemia through URAT1 in Hyperuricemic Mice.* PMC5788910 (2018). The HUA-mouse methodology and URAT1 readout convention this paper inherits.
4. Cross-validation against the closest published 2025 SSF cordycepin co-fermentation paper (Zhao 2025).

**What this means for downstream use.** Every numerical claim in this document that is NOT in the published abstract is marked `[METHODS-INFERRED FROM ANALOG]` or `[NOT IN ABSTRACT]`. The 4 chokepoint hits (URAT1 / GLUT9 / ABCG2 / PPARα) are confirmed by the abstract as **gene-expression measurements**, but the **direction, magnitude, p-values, and tissue specificity at the level of individual transcript fold-change cannot be verified** without the full text. Treat this deep-read as a **provisional read**; the canonical numbers must be lifted from the full PDF before any wiki page cites them.

---

## 1. Extract characterization

**What the abstract states explicitly:** AMC-BFE = "ethanol extract obtained from bidirectional solid-state fermentation of *Astragalus membranaceus* and *Cordyceps militaris*". The naming convention (AMC = Astragalus membranaceus + Cordyceps; BFE = Bidirectional Fermentation Extract) is consistent with the Shandong-Ling-lab pattern for this class of co-fermentation products.

**Whole-extract evidence, not isolated compound.** The abstract says: "Chemical profiling by LC-MS/MS showed that bidirectional fermentation enriched several bioactive metabolites, including **isoflavone aglycones, nucleosides, and polyols**." The active component is NOT identified at single-compound resolution — the abstract explicitly hedges: *"These compositional differences may be related to the observed urate-lowering activity, although the contribution of individual metabolites requires further investigation."*

**Inferred chemical classes (from the named families + the parent biology):**
- **Isoflavone aglycones** — from *Astragalus*: calycosin and formononetin (deglycosylated forms of calycosin-7-O-glucoside / ononin / astragaloside). The "aglycone" word matters: bidirectional SSF deglycosylates the parent isoflavones, producing the more bioavailable aglycone forms. This is a known C. militaris β-glucosidase activity.
- **Nucleosides** — almost certainly cordycepin (3'-deoxyadenosine), adenosine, and possibly cordycepic acid. Cordycepin is the canonical *C. militaris* anti-HUA agent (Yong 2018, PMC5788910 — independently shown to downregulate URAT1).
- **Polyols** — likely mannitol (cordycepic acid) and possibly D-arabinitol/erythritol from the rice substrate processed through fungal metabolism.

**Conclusion:** AMC-BFE is a chemically-defined *fingerprint* (LC-MS/MS profile is reported), but mechanistically a **whole-extract**. No single active component is causally pinned to any single chokepoint. **The 4-chokepoint claim is whole-extract evidence; per-chokepoint compound attribution is absent.**

## 2. Fermentation method

**Confirmed from abstract:** "bidirectional solid-state fermentation". Not liquid; not co-culture in a stirred tank. SSF = the *C. militaris* mycelium colonizes a solid substrate that includes Astragalus.

**`[METHODS-INFERRED FROM ANALOG]` Zhao 2025 (PMC12805540) protocol from the same Shandong consortium**, which is almost certainly the protocol AMC-BFE follows with substrate substitution:
- **Substrate:** rice base + ground botanical (sieved through 65-mesh, ~250 μm). For AMC-BFE, the analogue would be rice + *Astragalus membranaceus* root powder.
- **Inoculum ratio (analog):** 30% botanical / 70% rice by total solid weight, optimized in preliminary experiments. *AMC-BFE may use a different optimum — not verifiable without full text.*
- **Strain:** *C. militaris* (the Zhao paper uses strain X6, ITS-confirmed). Spore solution prepared in PDA liquid medium, 25°C, 180 rpm, 48 h.
- **Inoculation:** ~10 mL spore suspension into solid substrate.
- **Conditions:** 25°C, dark for 5–7 days until mycelial colonization → switch to 10 h:14 h light:dark cycle, 10°C+ day-night gradient, 60% humidity, 200 lux, **total 50 days**.
- **Sample collection:** typical timepoints 7, 15, 20, 25, 30, 40, 50 days. Final material ground and sieved through 65-mesh.
- **Extraction:** abstract says "ethanol extract" — solvent details not specified.

**Bidirectionality clarification:** "Bidirectional" SSF in this literature refers to **mutual biotransformation** — the fungus modifies plant secondary metabolites (deglycosylation, hydroxylation, methylation), AND the plant matrix modifies fungal metabolite output (e.g., the Zhao 2025 paper showed American ginseng addition changes cordycepin yield in *C. militaris*). It is **not** sequential fermentation and **not** co-culture of two organisms; it is a **single fungus on a botanical-supplemented solid substrate**.

**Reproducibility judgment:** The abstract confirms the *category* of method (SSF + bidirectional); the *exact* AMC-BFE recipe (substrate ratio, day count, extraction solvent ratio, yield) is not in the abstract. **Methods section reproducibility cannot be confirmed without the full paper.** The analog paper IS reproducible from its published methods, so we have a strong prior that AMC-BFE methods are likewise reproducible — but we cannot verify the AMC-BFE specifics.

## 3. In vivo mouse data — exact numbers

**`[NOT IN ABSTRACT]` Most numerical detail is inaccessible.** The abstract confirms qualitative findings only:

| Parameter | Abstract says | Full numerical detail |
|---|---|---|
| Model | Potassium oxonate + adenine HUA mouse | Confirmed |
| Strain | C57BL/6 mice (from MeSH terms) | Confirmed |
| Sex | Male (from MeSH) | Confirmed |
| n per group | — | NOT IN ABSTRACT |
| Dose | — | NOT IN ABSTRACT (MeSH includes "Dose-Response Relationship, Drug" → suggests multi-dose) |
| Route | — | NOT IN ABSTRACT (gavage is conventional for this model) |
| Duration | — | NOT IN ABSTRACT |
| Baseline SUA | — | NOT IN ABSTRACT |
| Treated SUA | — | NOT IN ABSTRACT |
| % reduction | "significantly lowered serum uric acid levels" — direction confirmed, magnitude not stated | NOT IN ABSTRACT |
| p-values | — | NOT IN ABSTRACT |

**Confirmed qualitative findings:**
- SUA significantly reduced ✅
- XOD activity suppressed ✅
- ALT, AST, BUN, serum creatinine ameliorated ✅
- Total cholesterol and triglycerides reduced ✅
- Multi-dose study likely (MeSH "Dose-Response Relationship") ✅

**Pattern from analog (Yong 2018, PMC5788910 cordycepin paper):** typical n=10 per group, gavage administration, 7-day treatment, baseline SUA in HUA mice ~3.5–6 mg/dL elevation over normal (normal mouse SUA ~1.5 mg/dL → HUA SUA ~5–7 mg/dL), allopurinol positive control at 5 mg/kg, test compound 5–50 mg/kg dose range, % reduction commonly 30–60% at the high dose. **AMC-BFE numbers should fall in this range but cannot be confirmed.**

## 4. Per-chokepoint evidence

**`[CONFIRMED FROM ABSTRACT]` All four chokepoints are measured at the gene-expression level.** No protein-level Western blot or activity assay is referenced in the abstract. No reporter assay for PPARα is referenced.

| Chokepoint | Evidence type | Direction | Tissue | Magnitude / p-value |
|---|---|---|---|---|
| **URAT1** (SLC22A12) | mRNA (qRT-PCR implied) | **Downregulated** ✅ | Kidney ✅ | NOT IN ABSTRACT |
| **GLUT9** (SLC2A9) | mRNA | **Downregulated** ✅ | Kidney ✅ | NOT IN ABSTRACT |
| **ABCG2** | mRNA | "Altered expression" — **direction not specified in abstract** ⚠️ | **Liver** ✅ (hepatic ABCG2, NOT intestinal) | NOT IN ABSTRACT |
| **PPARα** | "Activated the hepatic… signaling pathway" | Activated (gene expression downstream targets implied) | Liver | NOT IN ABSTRACT — no reporter, no co-IP, just pathway-level inference from RNA |

**Two important hedges that the Phase 4 hit summary may have glossed over:**

1. **ABCG2 is hepatic, not intestinal.** This is unusual. The canonical ABCG2 chokepoint for urate is the **intestinal** one — *ABCG2* in the gut secretes urate into the lumen, and gut ABCG2 dysfunction causes ~1/3 of all hyperuricemia (the "extra-renal underexcretion" phenotype). Hepatic ABCG2 is a different story — it likely affects bile-route urate excretion, which is a minor pathway in mice and humans. **The chokepoint mapping to "ABCG2 = the intestinal Open Enzyme target" is therefore weaker than first read.**

2. **ABCG2 direction is "altered," not "upregulated."** This is the abstract author's word — vague. If AMC-BFE *downregulated* hepatic ABCG2, that's neutral or net-negative for the urate-handling story. If *upregulated*, that increases bile-route excretion. The Phase 4 hit-list interpretation should be re-examined when the full text is read.

3. **PPARα activation is not measured by reporter assay** (per abstract). It is "pathway activation" — typically meaning downstream PPARα target gene transcription (acyl-CoA oxidase, CPT1, FGF21, etc.) is upregulated by qRT-PCR. This is suggestive but not direct ligand-binding evidence. **The PPARα claim should be tier-2 evidence (gene-expression downstream targets, not direct receptor activation).**

## 5. Compound identification — fractionation?

**No.** The abstract explicitly states: *"the contribution of individual metabolites requires further investigation."* This is the authors' own caveat that the per-compound mapping is not done. **AMC-BFE is whole-extract evidence end-to-end.** No bioassay-guided fractionation is referenced. No compound-by-compound URAT1 / GLUT9 / ABCG2 / PPARα assay is referenced.

**Implication for Open Enzyme triage:** the candidate hits among the LC-MS/MS-identified metabolite classes (cordycepin, calycosin, formononetin, mannitol/cordycepic acid, adenosine) all have prior literature linking them to one or another of these chokepoints. Cordycepin → URAT1 (Yong 2018). Calycosin → PPARα (multiple Chinese-source papers). Mannitol → osmotic / non-specific. **The mechanism diversity is plausible and aligns with prior single-compound literature**, but the AMC-BFE paper does not deconvolve which compound drives which chokepoint.

## 6. Other mechanisms — NLRP3 / complement / Lp-PLA2 / HDAC6 / redox?

**`[NOT IN ABSTRACT — full-text check needed]`**

- **NLRP3:** not mentioned in abstract or MeSH.
- **Complement:** not mentioned.
- **Lp-PLA2:** not mentioned.
- **HDAC6:** not mentioned.
- **PDI / TXNIP / thioredoxin / ergothioneine:** not in abstract. **However**, abstract says "Untargeted metabolomics further identified alterations in **gut microbiota-derived metabolites linked to antioxidant pathways**." This is a weak signal that the redox/antioxidant axis is touched, but the specific molecules (ergothioneine — *C. militaris* is a known ergothioneine producer; TXNIP — NLRP3-relevant; thioredoxin — redox poise) are NOT named in the abstract.

**Action item for the full-text follow-up:** specifically grep the full PDF for: "ergothioneine," "TXNIP," "thioredoxin," "PDI," "NLRP3," "complement," "Lp-PLA2," "HDAC6." If ergothioneine is identified by LC-MS/MS, this is a major plus — *C. militaris* ergothioneine production is well-documented (PubMed 30+ papers), and ergothioneine is one of the few mammalian-relevant fungal antioxidants with a dedicated transporter (OCTN1/SLC22A4).

## 7. Author affiliation, Chinese-source evidence

**Corresponding authors:**
- Guoying Zhang, School of Pharmacy, Shandong University of Traditional Chinese Medicine, Jinan 250355, China.
- Jianya Ling, School of Pharmacy + State Key Laboratory of Microbial Technology, Shandong University, Qingdao 266237, China.

**All authors Chinese-affiliated.** The paper is published in *Bioorganic Chemistry* (Elsevier, English-language journal; SCImago Q1; impact factor in 2026 not yet final but historically ~5). This is a **Chinese-research, English-publication** paper — exactly the class of research the umbrella-CLAUDE.md global-multilingual rule says we should NOT discount. The Shandong U TCM + Shandong U State Key Lab Microbial Tech consortium has a track record of bidirectional SSF papers (Zhao 2025 Cordyceps×Panax is the same consortium's prior work).

**Chinese-source cross-check:** the related-Chinese-literature on *Astragalus* + *C. militaris* co-fermentation in CNKI / WanFang would likely show 5–15 prior Chinese-language papers from the same lab and adjacent labs. None checked here yet — but **the existence of the lineage suggests this is a mature methodological line, not a one-off finding.** Confidence in the methods reproducibility is therefore higher than a first-paper-from-a-new-group claim of similar magnitude.

---

## Summary of what's verified vs. what needs the full PDF

| Claim | Status |
|---|---|
| AMC-BFE reduces SUA in HUA mice | ✅ Confirmed (abstract) |
| AMC-BFE inhibits XOD activity | ✅ Confirmed (abstract) |
| Renal URAT1 downregulated | ✅ Confirmed direction (abstract); magnitude unverified |
| Renal GLUT9 downregulated | ✅ Confirmed direction; magnitude unverified |
| Hepatic ABCG2 modulated | ⚠️ Direction NOT specified in abstract |
| Hepatic PPARα pathway activated | ✅ Pathway-level, not direct ligand binding |
| Liver/kidney function markers improved | ✅ Confirmed |
| Whole-extract, no compound-level deconvolution | ✅ Confirmed by author hedge |
| Gut microbiota antioxidant metabolites altered | ✅ Confirmed (abstract) |
| Bidirectional SSF chemistry shifted (isoflavone aglycones, nucleosides, polyols enriched) | ✅ Confirmed (abstract) |
| **Exact mouse n, dose, % SUA reduction, p-values, fold-changes** | ❌ Need full PDF |
| **NLRP3, ergothioneine, TXNIP, complement, HDAC6, Lp-PLA2** | ❌ Need full PDF (not in abstract) |
| **Toxicity / body-weight / safety data** | ❌ Need full PDF |

## Citation hygiene

Per umbrella CLAUDE.md and the "Pre-commit grep-verify gate" rule in `Open Enzyme/CLAUDE.md` §4, **no number from this paper should propagate to wiki pages until the full PDF is retrieved and grep-verified.** The four-chokepoint mechanism diversity claim (the basis for triaging this as the highest-priority Phase 6 hit) holds at the *qualitative* level from the abstract. Quantitative claims (e.g., "URAT1 downregulated 0.4×", "% SUA reduction = X%") are placeholder-only until full-text verification.

**Recommended action for Phase 6:**
1. Retrieve full PDF (institutional access, interlibrary loan, or contact corresponding author Ling J at lingjian-ya@sdu.edu.cn).
2. Grep PDF for: load-bearing numbers per the table above + the redox/NLRP3/ergothioneine list.
3. Update this deep-read in place; remove `[NOT IN ABSTRACT]` markers as numbers are verified.
4. Then and only then, propagate the canonical AMC-BFE numbers to `wiki/comp-014-medicinal-mushroom-compound-mapping.md` and `wiki/synthesis.md`.

## References

PubMed: [Xia 2026, PMID 41905012](https://pubmed.ncbi.nlm.nih.gov/41905012/), DOI [10.1016/j.bioorg.2026.109806](https://doi.org/10.1016/j.bioorg.2026.109806).

Methodological analog from same Shandong consortium: [Zhao et al 2025, PMC12805540](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12805540/), https://citations.gxl.ai/papers/PMC12805540 — bidirectional SSF *C. militaris* × *Panax quinquefolius* L., same lab pattern (rice substrate, 65-mesh sieve, 25°C, 50-day SSF).

URAT1-axis prior art: [Yong et al 2018, PMC5788910](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5788910/), https://citations.gxl.ai/papers/PMC5788910 — cordycepin downregulates URAT1 in HUA mice (independent confirmation that the *C. militaris* → URAT1 axis is real, regardless of fermentation context).
