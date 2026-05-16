# Phase 5 Deep-Read: Sanghuangporus davallialactone (PMID 36801789)

**Paper.** Song J, Wang Z, Chi Y, Zhang Y, Fang C, Shu Y, Cui J, Bai H, Wang J. "Anti-gout activity and the interaction mechanisms between *Sanghuangporus vaninii* active components and xanthine oxidase." *Bioorganic Chemistry* 133:106394 (2023). DOI: [10.1016/j.bioorg.2023.106394](https://doi.org/10.1016/j.bioorg.2023.106394). Citation per PubMed.

**Full-text availability.** Closed-access (Elsevier / *Bioorganic Chemistry*). Not in PMC, not in Paperclip's full-text corpus. This deep-read is anchored on the PubMed abstract (canonical) plus structural-class context from the *Phellinus linteus* phenylpropanoid review (PMC6572527, [DOI 10.3390/molecules24101888](https://doi.org/10.3390/molecules24101888)). All extracted-from-abstract claims are explicitly tagged; class-context claims are explicitly tagged.

**Citation format.** PubMed retrieval per server policy (https://doi.org/10.1016/j.bioorg.2023.106394). No Paperclip URL because the paper is not in the corpus.

---

## 1. Compound identity — davallialactone

**From abstract (canonical):** "isolated an active component of *S. vaninii* using high performance countercurrent chromatography and identified it as davallialactone using mass spectrometry with 97.726% purity." Confirms: defined single compound, 97.7% purity at characterized purity.

**Structural class — extrapolated from related-literature anchor (NOT from this paper's full text):** Davallialactone is a **styrylpyrone-family phenylpropanoid** in the hispidin lineage. Per the *P. linteus* review (PMC6572527, L43): "phelligridimer A, protocatechualdehyde, davallialactone, hypholomine B, interfungin A, and inoscavin A isolated from the fruiting body of *P. linteus* possessed significant rat lens aldose reductase and human recombinant aldose reductase inhibitory activity in vitro, with IC50 values of 0.63, 4.26, **20.52**, 0.33, 0.82, 1.03, and 1.06 μM and 1.37, 7.93, **35.36**, 0.56, 1.28, 1.82, and 1.40 μM, respectively." (davallialactone bolded). Same review (L15): davallialactone listed as compound (13) in the *P. linteus* phenylpropanoid table, alongside hispidin (2), phelligridimer A (9), hypholomine B (10), interfungin A (11), protocatechualdehyde (12), inoscavin A (14).

**IUPAC / SMILES / InChIKey — NOT extracted at full-text level.** ChEMBL has no entry for "davallialactone" by name (compound_search returned 0 hits). PubChem and ChemSpider lookups not run in this phase; these are appropriate Phase 6 follow-ups if the compound advances. Working hypothesis: hispidin-type 4-hydroxy-6-styryl-2-pyrone scaffold with an additional lactone closure (the "lactone" suffix). [Evidence level: mechanistic extrapolation from class anchor — verify before any chemistry-specific claim is committed to a wiki page.]

## 2. Source attribution

**From abstract:** *Sanghuangporus vaninii* — "perennial, medicinal, and edible fungus traditionally used to treat various symptoms." Same organism cluster as the *Phellinus linteus* / *P. baumii* / *P. vaninii* sang hwang complex (Korean: 상황버섯; Chinese: 桑黄). All authors are at **Changchun Normal University, Changchun 130032, China** (Jilin Province, the artificial-cultivation hub for *S. vaninii*; the related polysaccharide paper PMC12429920 explicitly sources from Jilin Sanghuang Biotechnology Group). Author affiliation is **Chinese, not Korean**, despite the Korean-traditional-medicine framing in the breadth-pass brief.

**Fruiting body vs mycelium — NOT extracted at full-text level.** The companion *S. vaninii* polysaccharide paper (PMC12429920) uses 3-year-old artificial-cultivation **fruiting bodies** from Jilin. Most *Sanghuangporus*/Phellinus phenylpropanoid isolations in the related literature are from fruiting bodies (the PMC6572527 review attributes davallialactone to "the fruiting body of *P. linteus*"). Working hypothesis: fruiting body. [Verify at full text if it matters for fermentation strategy.]

**Extraction / purification.** Abstract states **high-performance countercurrent chromatography (HPCCC)** as the separation modality, MS for identification, 97.7% purity. No column-chromatography solvent system extracted at full-text level.

## 3. XO IC50 — assay conditions

**From abstract (canonical):**
- IC50 = **90.07 ± 2.12 μM**. Verified at abstract-level. The 97.7% purity claim is also abstract-canonical.
- **Inhibition type: mixed.** Verbatim: "davallialactone had mixed inhibition of XO activity."
- **Readout: microplate reader** (suggests uric acid spectrophotometric at 290–295 nm — standard for this class of assay; not explicitly stated in abstract).
- **Substrate (xanthine vs hypoxanthine), enzyme source (bovine milk XO vs other), buffer / pH — NOT in abstract.** Standard for this class of assay is bovine-milk XO + xanthine substrate; verify at full text before any quantitative cross-paper comparison.

**Binding-site mechanism (from abstract, mechanistically rich):** Molecular docking places davallialactone "at the center of the molybdopterin (Mo-Pt) of XO" — i.e., the catalytic Mo-cofactor pocket where xanthine binds, same site as allopurinol. Interacting residues: **Phe798, Arg912, Met1038, Ala1078, Ala1079, Gln1194, Gly1260**. Aryl ring of davallialactone forms **face-to-face π-π stacking with Phe914**. Fluorescence quenching of XO confirms binding; conformational change driven by hydrophobicity + H-bonding.

The Mo-Pt active-site occupancy is consistent with the "mixed inhibition" kinetic finding — competitive at the catalytic pocket plus a secondary effect (likely the conformational change).

## 4. Comparison to allopurinol

**NOT EXTRACTED at full-text level.** Abstract does not state the allopurinol same-conditions IC50. Standard literature value for allopurinol against bovine-milk XO is ~5–10 μM, which would put davallialactone ~10–18× weaker than allopurinol. **This is the single most important number to extract at full-text level if davallialactone advances to Phase 6.**

## 5. Selectivity — off-target screen

**Not mentioned in abstract.** No off-target oxidoreductase / dehydrogenase data extracted at this level. The class-context literature (PMC6572527) does provide tangential off-target context: davallialactone is also an **aldose reductase inhibitor (IC50 ~20.5 μM rat lens / 35.4 μM human recombinant)** and a **methylglyoxal-mediated protein modification inhibitor (IC50 213 μM)** — meaning davallialactone is *more* potent against aldose reductase than against XO. This is a **selectivity red flag for clean XO chokepoint thesis**: a compound with a 20 μM aldose reductase IC50 and a 90 μM XO IC50 is more naturally framed as an aldose reductase inhibitor with weak XO secondary activity than as a clean XO inhibitor. This finding alone may downgrade the Phase 6 case.

## 6. In vivo data

**Strictly biochemistry + cell culture in this paper.** From abstract: "Cell biology experiments indicated that davallialactone reduced the expression of the inflammatory factors, tumor necrosis factor alpha and interleukin-1 beta (P < 0.05), can effectively alleviate cellular oxidative stress." This is a cell-line readout, not animal-model. **No mouse / rat data in this paper.**

The companion *S. vaninii* polysaccharide paper (PMC12429920) is also strictly cell-culture (RAW 264.7 + MSU stimulation), so the *S. vaninii* anti-gout literature ecosystem is currently weighted toward in-vitro evidence. The PMC6572527 review reports *P. linteus* polysaccharide in-vivo antidiabetic data, but **no davallialactone-specific in-vivo data** is documented in the related literature reviewed here.

## 7. Other chokepoints mentioned

**TNF-α, IL-1β suppression** — at the protein-expression level in cells, evidence of inflammatory-cytokine modulation. Mechanism not specified (could be NLRP3, NF-κB, or upstream). **NLRP3 not explicitly named in abstract** — but the IL-1β suppression is suggestive (IL-1β is the canonical NLRP3 inflammasome readout in MSU models). The companion polysaccharide paper PMC12429920 explicitly invokes NLRP3 and NF-κB pathways as the *S. vaninii* anti-gout mechanism, so the davallialactone IL-1β data fits within that established framework but is not directly assigned to a specific upstream node in this paper.

**Complement, transporters (ABCG2 / URAT1), redox markers (TXNIP, thioredoxin, ergothioneine, PDI) — NOT mentioned.**

**Oxidative stress** — abstract states "alleviate cellular oxidative stress" but does not name the redox node. The styrylpyrone class generally has antioxidant activity (the hispidin literature is heavy on radical scavenging — see Boulebd et al. PMC11894650).

## 8. Author affiliation + original-source-language anchor

**All 9 authors at Changchun Normal University (Changchun, Jilin, China).** Two are at the Central Laboratory; one (Zhang) has a secondary affiliation at Nanguan Middle School in Zunyi. Corresponding author: **Jing Wang, zixi21@163.com**. **Chinese institution, English-language paper, published in Elsevier's *Bioorganic Chemistry*** — this is a Chinese-research-group paper aimed at the Western literature. The Korean-traditional-medicine framing in the breadth-pass brief is geographic context for *Sanghuangporus* (sang hwang is the Korean name for the *Phellinus linteus*-complex), **not** an indication that this specific paper has Korean-vendor literature evidence behind it.

**Korean-vendor (KISS / RISS) deep-dive justified?** Yes, but for a **different reason** than originally framed. The breadth-pass brief asked whether KISS / RISS would have additional source evidence behind PMID 36801789 itself — answer is **no**, this is a Chinese-group paper. **However**, the broader davallialactone literature *does* have Korean-source anchoring: davallialactone was first reported as an aldose reductase inhibitor by Korean groups (Lee & Yun 2007, 2008, *Bioorg Med Chem Lett* — referenced as [65] in PMC6572527). A KISS / RISS deep-dive on **the original Korean-language davallialactone characterization** would surface (a) the original isolation from *P. linteus* fruiting body, (b) the original SMILES / IUPAC, (c) the original structural elucidation NMR, and (d) any Korean-traditional-medicine clinical evidence on sang hwang for hyperuricemia or gout that's not in PubMed. **Recommended Phase 6 follow-up if davallialactone advances.**

CNKI (Chinese-language) deep-dive is also justified given the Chinese authorship — there may be Chinese-language characterization or clinical-correlate work from Changchun Normal not indexed in PubMed.

---

## Phase 6 triage verdict

**Conditional candidate with two significant caveats.**

**Pro:**
- Single defined compound (not extract, not polysaccharide).
- Characterized purity 97.7%.
- Biochemical XO IC50 90.07 μM — modest but real, in the same ballpark as the comp-014 breadth-pass mid-tier hits.
- Mixed-inhibition mechanism with explicit Mo-Pt active-site docking (Phe798, Arg912, Phe914 π-π stack) — interpretable mechanism, not just empirical inhibition.
- Source organism (*S. vaninii*) is artificially cultivated at scale in Jilin; basidiomycete fermentation is biologically plausible (though not trivial — *Sanghuangporus* is slow-growing, not a koji-grade chassis).
- Class is well-anchored (hispidin/styrylpyrone family); biosynthesis pathway is known (PheG aldol condensation synthase characterized in *P. igniarius* — PMC11924017).

**Con (load-bearing):**
- **Selectivity red flag.** Aldose reductase IC50 ~20.5 μM (rat), ~35.4 μM (human recombinant), per related-literature anchor. Davallialactone is **more potent against aldose reductase than against XO** by a factor of 2–4×. Cleaner-framed as an aldose reductase inhibitor with secondary XO activity than as a primary XO inhibitor. This argues against a clean XO chokepoint thesis.
- **No in-vivo data anywhere.** This paper is biochem + cell. No murine hyperuricemia model, no oral bioavailability data, no PK. The PMC6572527 review documents *no* davallialactone-specific in-vivo data either. Phase 6 would require a substantial in-vivo bridge.
- **Allopurinol same-conditions IC50 not extracted** — without that number, the breadth-pass IC50 of 90 μM cannot be benchmarked rigorously. Likely 10–20× weaker than allopurinol, which is a typical natural-product gap.
- **Source organism is not a fermentation chassis** — *Sanghuangporus* / *Phellinus* are slow-growing wood-decay basidiomycetes, multi-year fruiting-body cultivation, not a Phase 6-friendly koji or yeast chassis. Heterologous expression of the styrylpyrone biosynthesis pathway (PheG + downstream cyclase) in *A. oryzae* or *S. cerevisiae* is conceivable but would itself be a significant project, not a drop-in.

**Recommendation:** **Do not advance davallialactone to Phase 6 as a primary XO chokepoint candidate.** The selectivity profile (aldose reductase preference) and absence of in-vivo data are stronger signals than the modest 90 μM XO IC50. **However**, davallialactone may be a useful **secondary candidate** if comp-014 evolves toward a multi-chokepoint thesis — its aldose reductase activity is mechanistically relevant to **diabetic-comorbidity gout** (hyperuricemia + diabetes is a common co-occurrence and aldose reductase is a major sorbitol-pathway node). The styrylpyrone class as a whole (hispidin, davallialactone, phelligridimer A, hypholomine B, interfungin A, inoscavin A — all from *P. linteus* fruiting body) deserves **a class-level Phase 6 evaluation** rather than a single-compound advance.

**Phase 6-actionable items if davallialactone or the styrylpyrone class advances:**

1. Acquire full text of PMID 36801789 — extract allopurinol same-conditions IC50, substrate conc, enzyme source, exact assay buffer.
2. Pull SMILES / InChIKey from PubChem (CID lookup on "davallialactone") and CAS (literature CAS for davallialactone is 521267-12-9 — verify).
3. KISS / RISS deep-dive on original Korean davallialactone characterization (Lee & Yun groups, ~2007–2008).
4. CNKI search on "桑黄 黄嘌呤氧化酶" (sang hwang xanthine oxidase) for Chinese-language clinical correlates.
5. Class-level evaluation: phelligridimer A (rat aldose reductase IC50 0.63 μM — much more potent than davallialactone) is the more interesting class lead; davallialactone may be a B-team candidate within its own structural family.

---

**Verification note (per CLAUDE.md pre-commit grep-verify gate):** The 90.07 μM XO IC50 and 97.7% purity are verified at PubMed-abstract level only. The closed-access full text was not retrieved. All structural-class claims (hispidin/styrylpyrone family, aldose reductase IC50 values) are extracted from PMC6572527 and explicitly tagged as related-literature anchors, not as claims about PMID 36801789's primary text. SMILES / InChIKey / IUPAC are NOT verified against any primary source in this deep-read and should not be cited from this document.
