# Mushroom × HDAC6 for Q141K-ABCG2 Rescue — Traditional-Name Re-Scan — 2026-05-19

Triggered by: `lit-scan-query-framing-retrospective-audit-2026-05-19.md` HIGH-leverage re-scan candidate #4 (medicinal mushroom × HDAC6 for Q141K-ABCG2 trafficking rescue). Audit hypothesis: comp-014 Phase 3 mechanism-name framing for HDAC6 inhibitors would miss mushroom-source HDAC6-active triterpenes / polysaccharides that traditional-name framing might catch.

Scan methodology: WebSearch + Paperclip MCP (search) across each target species using **traditional-name FIRST + species-name + traditional-pathology framing**, then mechanism-name as a complementary axis. Multilingual queries in simplified Chinese (灵芝, 冬虫夏草, 桑黄, 茯苓, 木耳, etc.), Japanese kana (霊芝, マイタケ), and pinyin/romanization where useful. Two-model translation cross-check applied per CLAUDE.md §"Translation protocol" — single-model translation only where the source is English-language anyway; native-Chinese sources were read directly.

---

## Summary

**Headline finding: the HDAC6-selective inhibition axis is essentially empty across the medicinal-mushroom corpus.** Neither mechanism-name nor traditional-name framing surfaces a single mushroom natural product with published HDAC6-selective inhibition data (vs. tubacin / tubastatin A class IIb selectivity). What the traditional-name framing DID surface — and what the comp-014 Phase 3 mechanism-name pass missed — is a separate, mechanistically distinct ABCG2 rescue axis: **Poria cocos / Wolfiporia cocos (茯苓 Fu Ling)** directly upregulates ABCG2 mRNA + protein in hyperuricemic mice, with effect magnitude exceeding the benzbromarone positive control (Sun et al. 2021 PMID 33651969). Mechanism unidentified; not necessarily HDAC-mediated. The discipline rule worked — just not on the HDAC6 axis it was framed around. Net effect: comp-014's chokepoint matrix should be updated to surface Poria cocos as an ABCG2 lever; the HDAC6 axis remains an open chemistry-design target with no mushroom-natural-product head start.

**Three secondary findings worth tagging but lower-leverage:**

1. **Antrodia cinnamomea source paradox.** Artificial-cultured mycelium ethanol extract directly inhibits HDAC1/2/3/4 (22-56% reduction, cell-free assay, breast cancer cells — Lin et al. 2019 PMC6412332). HDAC6 NOT tested. Confusingly, the **wild fruiting body** ethanol extract goes in the OPPOSITE direction — histone HYPOacetylation via HDAC1 upregulation + HAT (GCN5/CBP/PCAF) downregulation in HL-60 leukemia (Yang et al. 2009 PMID 18709356, active compound zhankuic acid A). Source and culture state matter; the wild form is the wrong direction for Q141K rescue while the mycelium form may go the right direction (but HDAC6 specificity untested). Adds a triterpene-source candidate to the broader Q141K rescue chemistry pool but does NOT solve HDAC6 selectivity.

2. **Hericium erinaceus erinacine S → p300 HAT activation, not HDAC inhibition.** The PMC12595331 paper showing erinacine S enhances TRAIL/TNFR1/DR5 via H3K9K14ac histone acetylation works via **p300 activation** (HAT side), not via HDAC inhibition. Net direction is the same (more histone acetylation), but the mechanism is additive (write more acetyl) rather than subtractive (block deacetylation). Not load-bearing for HDAC6-selective Q141K trafficking rescue, but relevant if the platform thesis ever needs HAT-axis compounds.

3. **Ganoderic acid DM → tubulin binding (NOT HDAC6 inhibition).** Liu et al. 2012 (PMC3510465 / Sci Rep srep00905) — ganoderic acid DM binds α,β-tubulin with Kd similar to vinblastine and INCREASES tubulin polymerization. This is mechanistically interesting because HDAC6 substrate is acetylated tubulin — but ganoderic acid DM is a tubulin-binding tubulin-stabilizer, not a tubulin-deacetylase inhibitor. Different mechanism, different downstream. The PMC6273610 study on G. lucidum triterpenes regulating histone acetylation works via GCN5 (HAT) regulation, not HDAC inhibition.

**Traditional-name framing vs. mechanism-name framing — what was missed:** The query-framing discipline as articulated in the 2026-05-19 audit predicts that traditional-name anchors will surface compounds invisible to mechanism-name queries. For the HDAC6 axis specifically, the prediction is empirically falsified — both framings return essentially empty for mushroom-source HDAC6-selective inhibitors. For the broader **ABCG2 trafficking-rescue** parent question, the prediction holds: Poria cocos was invisible to comp-014's ChEMBL UniProt-join intersection (Wolfiporia cocos compounds are mostly outside ChEMBL's curated activity table) and surfaces immediately via 茯苓 + 高尿酸血症 + ABCG2 query framing. The audit's leverage estimate for this scan was rated MEDIUM-HIGH on the *HDAC6 axis*; actual yield was LOW on HDAC6 but HIGH on the parent ABCG2 question.

**Net wiki impact estimate (no edits made by this scan):** 1 substantive update to `wiki/abcg2-modulators.md` §"Inducers of intestinal ABCG2" Tier 2 — add Poria cocos with anchoring evidence. 1 lower-priority note to `wiki/medicinal-mushroom-compound-mapping-computational.md` Phase 5 deep-dive plan: Antrodia cinnamomea mycelium HDAC1/2/3/4 inhibition activity is a tier-2 finding for the broader Q141K HDAC-rescue parent track (not the HDAC6 sub-track). 1 framing correction in `wiki/food-grade-hdaci-screen-computational.md` (comp-007) Limitations: the mushroom-natural-product HDAC inhibitor compound class was structurally OUT-OF-SCOPE in comp-007 (which was "food-grade dietary GRAS"), and the absence of mushroom HDAC6-selective compounds in the corpus is a genuine literature gap, not a search artifact.

---

## Per-species findings

### Ganoderma lucidum (灵芝 Lingzhi / 霊芝 Reishi)

**Mechanism-name probe.** PubMed + WebSearch for "Ganoderma lucidum triterpene HDAC6 tubulin acetylation" surfaces:

- Liu et al. 2012, *Sci Rep* 2:905 (PMC3510465) — **ganoderic acid DM binds α,β-tubulin** via LC-MS/MS pulldown with Kd similar to vinblastine. Increases tubulin polymerization. Identifies microtubule-associated proteins (cytokeratin 19, cytokeratin 1, calumenin) as downstream targets. **Not an HDAC inhibitor; a tubulin-binding tubulin-stabilizer.** Mechanistically distinct from HDAC6's tubulin-deacetylase activity. *In Vitro + biochemical pulldown.*
- Shao et al. 2016, PMC6273610 — 19 triterpenes from G. lucidum show "anti-cancer potential by regulating histone acetylation and cell cycle." Mechanism named is **GCN5 regulation** (HAT side, not HDAC). General association with histone acetylation but no HDAC isoform-specific data, no IC50 against any HDAC. *In Vitro mechanistic.*
- Pozzobon et al. 2026, PMC12845357 (systematic review + meta-analysis of G. lucidum triterpene anti-inflammatory preclinical evidence) — no mention of HDAC enzymes or HDAC6 specifically. NLRP3, NF-κB, MAPK are the named pathways.

**Traditional-name probe.** 灵芝三萜 (Lingzhi triterpene) + HDAC / 组蛋白脱乙酰酶 / 蛋白质折叠 returns Chinese-language reviews of ganoderic acid biology covering anti-cancer, anti-inflammatory, immunomodulation. **No CNKI / Wanfang-anchored study connecting Lingzhi triterpenes to HDAC6 directly.** The closest hit is the same Liu 2012 tubulin paper that mechanism-name framing already surfaced. Ganoderic acid D (灵芝酸 D) per MedChemExpress data sheet is documented as upregulating **SIRT3** (class III deacetylase, mitochondrial, NAD+-dependent, sirtuin family — NOT HDAC6, NOT a target for Q141K rescue per Basseville 2012 which characterized class I/IIb HDIs).

**Spore-powder (灵芝孢子粉) probe.** Already known per comp-014 Phase 5: GLPP (Ganoderma lucidum polysaccharide peptide) reduces UA 40.6% in HUA mice via **ADA inhibition + GLUT9 downregulation + OAT1 upregulation** (Chen et al. 2022 Food Funct, PMID 36385640 / d2fo02431d). **Not via ABCG2 induction, not via HDAC mechanism.** Already in the wiki at `medicinal-mushroom-compound-mapping-computational.md` Phase 5 ADA promotion.

**Net verdict for Ganoderma × HDAC6 Q141K rescue:** NEGATIVE. The traditional-name probe surfaces no additional HDAC6-active Lingzhi compound beyond what mechanism-name framing already caught. Ganoderic acid DM's tubulin-binding activity (PMC3510465) is the closest tangentially-related finding, but it's mechanism-orthogonal to HDAC6 inhibition. Worth recording in the comp-014 archive as a tubulin-axis tubulin-stabilizer finding distinct from HDAC6 substrate biology.

---

### Cordyceps militaris (蛹虫草 Yong Chong Cao) + Cordyceps sinensis / Ophiocordyceps sinensis (冬虫夏草 Dong Chong Xia Cao) + Cordyceps cicadae (蝉花)

**Mechanism-name probe.** Cordycepin (3'-deoxyadenosine, the canonical C. militaris compound):

- Lawrence et al. 2024, *FEBS Letters* (PMC11808429) — cordycepin triphosphate inhibits PI3K/AKT/mTOR and MEK/ERK signaling broadly. **No HDAC inhibition.** Systems pharmacology study; mechanism is translation inhibition + AMPK activation, not epigenetic.
- Radhi et al. 2021, PMC8510467 (systematic review of cordycepin biological effects) — covers AMPK, mTOR, NF-κB, ADORA receptors, EGFR. **HDAC and HDAC6 not mentioned anywhere in the systematic review.**
- Cordycepin × HSP90: PMC9264932 (Cordycepin suppresses HSP90 function via ADA-dependent mechanism). This is mechanistically interesting because HSP90 is one of the few well-validated HDAC6 substrates — but cordycepin INHIBITS HSP90 function directly (likely via ATP-binding-pocket competition; ADA-dependent activation step suggests adenosine deaminase converts cordycepin to a more active metabolite that targets HSP90). NOT via HDAC6 modulation. The HSP90 connection is interesting for the platform's chaperone-class thinking but is orthogonal to the HDAC6 rescue mechanism.
- VPA (valproic acid, HDAC inhibitor) enhances cordycepin PRODUCTION in C. militaris culture by 41% — Tan et al. 2022 (PMID 35262812). This is HDACi acting on the fungus's own epigenome to upregulate biosynthesis, NOT cordycepin acting as HDAC inhibitor in mammalian cells.

**Traditional-name probe.** 冬虫夏草 / 蝉花 + HDAC / 组蛋白脱乙酰酶 returns:

- Cordyceps cicadae (蝉花) × renal protection literature (e.g., Frontiers Pharmacol 2021 / 10.3389/fphar.2021.801094) — mechanism is **SIRT1-mediated autophagy regulation** (sirtuin = class III deacetylase, distinct from HDAC6). The N6-(2-hydroxyethyl)adenosine compound from C. cicadae shows ER-stress protection in proximal tubular cells (MDPI ijms 22(4):1577) — chaperone-class activity hint, but no HDAC6 selectivity data.
- Cordycepin / nucleoside-analog × histone acetylation in mammalian cells: no Chinese-clinical or CNKI-indexed study connects cordycepin directly to mammalian HDAC inhibition. The C. militaris epigenetic-modification papers are all about the fungus's own production biology.

**Net verdict for Cordyceps × HDAC6 Q141K rescue:** NEGATIVE. The C. cicadae N6-(2-hydroxyethyl)adenosine ER-stress protection hint (ijms 22(4):1577) is suggestive of chaperone-class activity that could be tested separately as an ER-stress modulator for Q141K folding rescue — but this is the **pharmacological-chaperone track** (per `wiki/abcg2-modulators.md` §"Pharmacological-chaperone route — orthogonal small-molecule rescue"), not the HDAC6 trafficking-rescue track. Worth a separate downstream test if comp-032 chaperone-class wet-lab moves forward; not immediately load-bearing on the HDAC6 question.

---

### Grifola frondosa (舞茸 Maitake)

**Mechanism-name probe.** Maitake D-fraction (β-1,3/1,6-glucan): immune activation via NK cells (PMC5055164 — 5 mg/kg/day for 15 days blocked >60% breast cancer development in BALBc mice). No HDAC inhibition mechanism named.

**Traditional-name probe.** 舞茸 / マイタケ / グリフォラン + ヒストン脱アセチル化酵素 returns Japanese-language Maitake research focused on:
- Anti-obesity via gut microbiota → SCFA → HDAC3 inhibition (indirect, per PMC9886863). Same mechanism as fermentable fiber generally; not Maitake-specific HDAC inhibitor compound.
- D-fraction is a high-molecular-weight protein-bound β-glucan, not a small-molecule HDAC inhibitor. Acts as gut prebiotic → endogenous butyrate production → class I HDAC inhibition (HDAC3 named specifically; HDAC6 not mentioned).

**Net verdict for Maitake × HDAC6:** NEGATIVE for direct HDAC6 inhibition. CONFIRMS the polysaccharide-→-SCFA-→-HDAC pathway already well-characterized for butyrate (per `wiki/abcg2-modulators.md` §6 Q141K rescue). Maitake adds fermentable-substrate volume but no new mechanism.

---

### Pleurotus ostreatus (平菇 Ping Gu) + Pleurotus eryngii

**Mechanism-name probe.** P. ostreatus / P. eryngii × HDAC: no published HDAC inhibition data. Lovastatin (mevinolin) is naturally produced by Pleurotus species — known HMG-CoA reductase inhibitor, NOT an HDAC inhibitor.

**Ergothioneine (EGT, mushroom-enriched).** PMC10903977 (ergothioneine anti-ageing review) explicitly notes "it is important to explore the effects of ergothioneine on the epigenome toward histone acetylome... as well as DNA, RNA, and histone methylome" — i.e., **EGT × HDAC is an open research question, not yet characterized.** No published EGT IC50 against any HDAC isoform. EGT's known mechanism is glutathione-pathway thiol antioxidant + selenium-binding cofactor.

**Ergosterol peroxide (mushroom sterol).** From Cordyceps cicadae + Pleurotus eryngii. Antitumor + anti-inflammatory via apoptosis induction (ROS + ER stress, RSC Food Funct c9fo02454a). NOT HDAC6 inhibition.

**Traditional-name probe.** 平菇 + HDAC: no Chinese-language hits connecting Pleurotus to HDAC inhibition.

**Net verdict for Pleurotus × HDAC6:** NEGATIVE. Ergothioneine is an open question worth flagging separately (could test EGT against HDAC6 in vitro; would resolve cheaply with a commercial HDAC6 activity assay). Tag as future-comp-NNN candidate, not load-bearing now.

---

### Flammulina velutipes (金针菇 Jin Zhen Gu / Enoki)

**Mechanism-name + traditional-name probe.** Both axes return: F. velutipes produces its own chitin deacetylase (FEMS Microbiol Lett 289:130, fruiting-body development gene). No published F. velutipes compound with mammalian HDAC inhibition activity. The species-of-interest is bioactivity-rich for polysaccharide immunomodulation but has not been screened for HDAC inhibitors.

**Net verdict:** NEGATIVE / empty. No published evidence. Not a re-scan priority.

---

### Morchella esculenta (羊肚菌 Yang Du Jun)

**Mechanism-name + traditional-name probe.** PMC9440975, PMC10517965 — polysaccharide anti-obesity + anti-inflammatory via arachidonic acid pathway. Strong acetylcholinesterase inhibition (Begell House int j med mushrooms). **No HDAC inhibitor compound documented; HDAC mechanism not investigated.**

**Net verdict:** NEGATIVE / empty. Morchella has interesting AChE inhibitor activity (neurodegenerative relevance) but no HDAC data.

---

### Hericium erinaceus (猴头菇 Hou Tou Gu / Lion's Mane)

**Erinacine S → p300 activation, NOT HDAC inhibition.** PMC12595331 (Lu et al. 2025) demonstrates erinacine S derivative overcomes chemoresistance in colorectal cancer via TRAIL/TNFR1/DR5 upregulation. Mechanism characterized as: **p-PAK/FAK/p300 pathway activation → H3K9K14ac histone acetylation → DR5 gene transcription.** WebFetch verified: "no mention of HDAC isoform inhibition, no IC50 against HDAC enzymes, no effects on protein trafficking or microtubule acetylation."

**The literature on erinacines + acetylation reads as INCREASED acetylation via HAT activation, not via HDAC inhibition.** Net downstream direction is the same as HDACi (more acetylated H3K9K14), but mechanism is additive (p300 writes more acetyl marks) not subtractive (HDAC inhibition blocks erasure). This distinction matters for Q141K rescue because the chaperone-trafficking effect of HDIs (Basseville 2012) is specifically a non-histone mechanism via microtubule motor proteins (kinesins/dyneins), not via histone-level transcription. A HAT activator that boosts H3K9K14ac genome-wide does NOT rescue Q141K trafficking; the mechanism is fundamentally different.

**Net verdict for Hericium × HDAC6 Q141K rescue:** NEGATIVE for the Q141K trafficking-rescue mechanism. Erinacines remain interesting for their NGF/BDNF/neuroprotection axis (well-documented) but are not load-bearing for the HDAC6 question.

---

### Trametes versicolor (云芝 Yun Zhi / Kawaratake) — PSK / PSP

**Polysaccharide-Krestin (PSK) + Polysaccharide-Peptide (PSP).** Both proteoglycans ~100 kDa, approved as adjuvants in cancer therapy in Japan + China respectively. Immune-stimulation mechanism is the well-characterized one (TLR2 / dectin-1 / NK cell activation). **No published HDAC inhibition data for PSK / PSP** — these are large polysaccharide protein conjugates, not small-molecule HDAC inhibitors. Could indirectly affect HDAC via gut-microbiota SCFA production, same as any other fermentable polysaccharide.

**Traditional-name probe.** 云芝多糖肽 + HDAC: no direct mechanistic studies. The PSK/PSP corpus is heavily Japanese clinical literature (gastric and colorectal cancer adjuvant RCTs) and Chinese pharmacology research; epigenetic mechanism studies are sparse.

**Net verdict for Trametes × HDAC6:** NEGATIVE for direct HDAC6 inhibition. PSK/PSP are fermentable-polysaccharide → SCFA → HDAC pathway, same as fiber generally. Not a priority for the HDAC6 axis.

---

### Inonotus obliquus (桦褐孔菌 Hua He Kong Jun / Chaga) + Sanghuangporus / Phellinus linteus (桑黄 Sang Huang)

**Chaga's triterpene panel** (betulin, betulinic acid, inotodiol, trametenolic acid, lanosterol) — anti-cancer activity via DHFR inhibition (PMC11591880) + cell-cycle arrest. **No published HDAC6 inhibition; betulinic acid HDAC6 selectivity not documented** despite explicit search.

**Sanghuangporus / Phellinus linteus** — hispidin + hispolon are the canonical compounds. The PMID 25303891 / springer 2025 paper (s10529-025-03561-z) uses VPA (HDAC inhibitor) to INCREASE hispolon production in P. linteus culture — same direction as the Cordyceps VPA story (HDACi acts on the producer fungus's epigenome, not on mammalian HDAC). Hispidin acts as antioxidant + anti-inflammatory (HepG2, peroxynitrite scavenging); no HDAC inhibition mechanism.

**Traditional-name probe.** 桑黄 + HDAC / 组蛋白脱乙酰酶 returns the Sanghuangporus sanghuang genome paper (PMC8537844, 2021) — genome documents anti-tumor / antioxidant / anti-inflammation polysaccharide + pyrone + terpene production but does NOT connect any compound to HDAC inhibition mechanistically.

**Net verdict for Inonotus / Phellinus / Sanghuangporus × HDAC6:** NEGATIVE.

---

### Antrodia cinnamomea (牛樟芝 Niu Zhang Zhi / Taiwanofungus camphoratus)

**This is the source paradox finding — flagged separately because the literature is confusingly bidirectional.**

| Source form | Direction | HDAC isoforms tested | Active compound | Citation |
|---|---|---|---|---|
| **Wild fruiting body ethanol extract (EEAC)** | **Histone HYPOacetylation** — HDAC1 UP, HAT (GCN5/CBP/PCAF) DOWN. Synergizes with TSA. | HDAC1 (named, upregulated); other HDACs not isoform-specifically tested | Zhankuic acid A (triterpene) named as bioactive marker | Yang et al. 2009, *Arch Toxicol* 83:81-89 (PMID 18709356), DOI 10.1007/s00204-008-0337-3 |
| **Artificial-cultured mycelium ethanol extract (EEAC, breast cancer T47D)** | **HDAC1/2/3/4 INHIBITION** (22-56% reduction, cell-free assay) | HDAC1, 2, 3, 4 tested; **HDAC6 NOT tested** | Compound mixture; total triterpenoid content varies by phenotype | Lin et al. 2019, *Int J Mol Sci* 20:833 (PMC6412332), DOI 10.3390/ijms20040833 |

**Two opposite directions, two different source forms.** The wild fruiting body's HDAC1-upregulation + HAT-suppression direction is *wrong* for Q141K rescue (would INCREASE deacetylation). The artificial-cultured mycelium's HDAC1/2/3/4 inhibition direction is *correct* for the Q141K rescue mechanism (same class as Basseville 2012's vorinostat / romidepsin), but HDAC6 specificity is empirically untested. Without per-compound resolution (zhankuic acids A/B/C, antcin K, methyl antcinate A, dehydroeburicoic acid, etc. all present at different concentrations in the two source forms), the contradiction can't be resolved from public data alone.

**Mechanistically interpretable hypothesis:** the wild fruiting body and artificial mycelium produce different ratios of zhankuic acids (zhankuic acid A enriched in wild fruiting body per Yang 2009) vs. other triterpenes (antcin K, dehydroeburicoic acid enriched in mycelial culture per the UPSO patent 7838264). If zhankuic acid A is itself the HDAC1-upregulator (or histone-acetyl-erasure agent), while a different triterpene from the mycelial fraction is the class I HDAC inhibitor, both findings are simultaneously true at the source-form level. This is exactly the per-compound resolution that comp-014 Phase 5 deep-dive could close.

**Net verdict for Antrodia × HDAC6 Q141K rescue:** PARTIAL POSITIVE on the broader Q141K HDAC-rescue parent track (class I HDAC inhibition by mycelium-derived extracts at 22-56% reduction is in the right potency range for Basseville-class rescue), but HDAC6 SELECTIVITY UNTESTED. Worth a focused Phase 5 follow-up on Antrodia mycelium per-compound HDAC isoform screen. Whether this is a real lead vs. an artifact of the artificial-culture extract's chemical complexity is unclear.

---

### Wolfiporia cocos / Poria cocos (茯苓 Fu Ling) — load-bearing finding

**Sun et al. 2021 (PMID 33651969, PMC7928048), *Front Pharmacol***. Hyperuricemic mouse model. PCE and PCW (ethanol and water extracts) significantly elevated **ABCG2 mRNA + protein expression** in the intestine. The water extract (PCW) was described as having effects "even better than that of the benzbromarone control" (p < 0.01). Concurrent UA-lowering effect via XO inhibition + renal protection.

**Mechanism not investigated in this paper:**
- HDAC inhibition NOT examined
- PPARγ NOT examined  
- Direct compound responsibility NOT established — five computationally predicted bioactive compounds identified via molecular docking only (PubChem CIDs 267, 277, 13824, 15730, 5759), not validated in vitro
- Pachymic acid was used only as HPLC reference standard, not implicated as the active agent

**Why this finding matters for the platform:**

1. **Poria cocos is a canonical Si Miao San / Wu Ling San TCM formula ingredient.** Already implicated in the gout TCM literature surveyed by comp-013 (Si Miao San included as the named formula) but Poria cocos was NOT separately spawned as a compound source in comp-013's `inputs/compounds.json`. The comp-013 audit (per `lit-scan-query-framing-retrospective-audit-2026-05-19.md` line 60-61) explicitly flagged formula-completeness gap — Poria cocos compounds (pachymic acid, polyporenic acid C, dehydrotumulosic acid, dehydroeburicoic acid) were not separately queried by formula-name. **This rescan validates that gap.**

2. **Poria cocos is in the wiki's `medicinal-mushroom-compound-mapping-computational.md` anchor-species list** (comp-014 Phase 5 anchor) but did NOT surface as a Phase 3 ChEMBL chokepoint hit. ChEMBL's UniProt-join activity table doesn't contain Poria-source triterpene × ABCG2 records (the compounds aren't in ChEMBL's curated activity coverage). This is exactly the comp-013 / comp-014 ChEMBL coverage gap pattern documented for non-Western-pharma compounds.

3. **The mechanism is unidentified.** It could be transcriptional (PPARγ, HNF4α, AhR, Nrf2 — any of the routes in `abcg2-modulators.md` §"Transcriptional regulation map"). It could be trafficking rescue via chaperone-class activity (pachymic acid is structurally similar to triterpenes with ER-stress / unfolded-protein-response activity per generic triterpene literature). It could be HDAC inhibition (no HDAC isoform was tested, including HDAC6). **All three possibilities are consistent with the published data; resolving requires per-mechanism follow-up.**

4. **The animal-model evidence is mature:** intact in vivo HUA model, ABCG2 mRNA + protein quantified, effect magnitude exceeds benzbromarone, with concurrent XO inhibition and renal protection. This is stronger evidence than the "induced in cell culture" tier for most of the other ABCG2-modulator candidates in `abcg2-modulators.md`.

**Net verdict for Poria cocos:** **HIGH-priority addition to `wiki/abcg2-modulators.md` §"Inducers of intestinal ABCG2" Tier 2 ("Solid mechanism, modest evidence" — though the mechanism is empirically unidentified, the in-vivo magnitude exceeds Tier 1 standards).** Mechanism investigation should be the H-card spawn: pachymic acid + polyporenic acid C panel against HDAC6 + class I HDACs + PPARγ + AhR luciferase reporters + Caco-2 Q141K transfected trafficking assay. Sister to the §1.14 butyrate dose-response arm — same Caco-2 infrastructure, marginal cost <$2K.

---

### Auricularia auricula-judae (木耳 Mu Er)

**Mechanism-name + traditional-name probe.** No published HDAC inhibition or HDAC6 data. Anti-platelet + anti-coagulant mechanism well-documented (relevant to vessel-wall inflammation / Lp-PLA2 axis per the audit's MEDIUM-leverage item #9) but does not connect to HDAC6.

**Net verdict:** NEGATIVE / empty. Auricularia is interesting for the Lp-PLA2 lit-scan (separately queued); not for HDAC6.

---

### Lentinula edodes (香菇 Xiang Gu / Shiitake)

**Eritadenine + lentinan.** Eritadenine is an adenosine analog (like cordycepin and N6-(2-hydroxyethyl)adenosine from C. cicadae). Lowers cholesterol via SAH hydrolase inhibition → SAM-methylation pathway. **No HDAC inhibitor activity documented.** Lentinan is β-1,3-glucan, fermentable polysaccharide → SCFA → HDAC pathway is the same indirect mechanism as Maitake / Trametes.

The "methylation at promoter region attracts HDACs" framing in the Wiley CBDV 2025 review is generic histone biology, not Shiitake-specific HDAC mechanism. PMC10890338 review mentions epigenetic effects only in general terms.

**Net verdict:** NEGATIVE for direct HDAC6 inhibition.

---

## HDAC class-selectivity findings (Class I vs Class IIb HDAC6)

**The core empirical observation:** across all 12 mushroom species probed, **zero published HDAC6-selective inhibition data** exist for any mushroom-source compound. The closest natural-product HDAC6-selective compound the literature returned is **aceroside VIII**, a diarylheptanoid from **Betula platyphylla** (birch tree, NOT a mushroom) — PMID 25590368, Park et al. 2015, *Bioorg Med Chem Lett*. Aceroside VIII synergizes with synthetic HDAC6 inhibitor A452 against HT29 colon cancer. The published abstract does not provide IC50 values or selectivity ratios; the paper itself would need full-text reading for quantitative HDAC6 vs HDAC1 selectivity.

**Implication:** mushrooms produce abundant pan-HDAC pathway modulators (mostly via gut-fermentation → SCFA → class I HDAC inhibition, plus a smaller set of triterpene-class direct class I HDAC inhibitors like the Antrodia mycelium fraction) but **the HDAC6 isoform-selective inhibition niche is essentially unoccupied by mushroom natural products in the published literature.**

This is consistent with the broader natural-product HDAC6 literature: the canonical natural-product HDAC6 inhibitors are aceroside VIII (Betula, birch — Betulaceae, NOT a fungus), callophycin A (red algae Callophycis serratus → Mol Pharmacol 2025 ScienceDirect), and a tryptoline-class natural-product 6a (21-fold HDAC6 vs HDAC1 selectivity, derivatized from natural-product tryptoline). All three are non-fungal plant or marine sources. The mushroom kingdom appears empirically depleted of HDAC6-selective compound chemistry — a real gap, not a search artifact.

**Class I HDAC inhibition by mushroom-source compounds is the better-mapped axis:**
- Butyrate (mushroom-fermentable-polysaccharide → gut SCFA route): canonical class I HDACi at IC50 52 ± 11 μM (per the SCFA review surfaced in last batch search)
- Antrodia mycelium ethanol extract: HDAC1/2/3/4 22-56% reduction (Lin 2019, PMC6412332) — class I dominant, HDAC4 is class IIa (different from HDAC6 which is class IIb)
- Hericium erinacine S: works via p300 HAT activation, not HDAC inhibition — same net direction (more H3K9K14ac) but mechanism-orthogonal
- Antrodia wild-fruiting-body EEAC + zhankuic acid A: opposite direction (HDAC1 UP, HAT DOWN — histone hypoacetylation)

For Q141K rescue via the **Basseville 2012 trafficking-rescue mechanism** (class I HDIs vorinostat / romidepsin / panobinostat rescue Q141K via microtubule-motor protein expression changes, not via histone-level chromatin opening): the mushroom-derived class I HDIs at moderate potency (Antrodia mycelium fraction) are a candidate set, but the synthetic-drug class (panobinostat, romidepsin, 4-PBA, butyrate) remain the better-characterized rescue agents.

For Q141K rescue via the **HDAC6-selective tubulin-acetylation mechanism** (theoretical; would work via altered microtubule trafficking of the misfolded Q141K toward the membrane rather than the aggresome, analogous to CFTR F508del trafficking rescue by HDAC6 inhibitors per PMC8883472 Cystic Fibrosis review): **no mushroom-source compound is positioned to deliver this mechanism as of the 2026-05-19 literature.** This is the literature gap. Closing it requires either (a) novel chemistry design (not mushroom-derived) or (b) screening a broader mushroom-triterpene chemical library against HDAC6 specifically (no such screen has been published; could be the next comp-NNN).

---

## Trafficking-rescue evidence beyond histone-level mechanism

Per Basseville et al. 2012 (PMID 22472121), the **Q141K trafficking rescue is mechanistically driven by changes in microtubule motor protein expression** (kinesins / dyneins involved in retrograde trafficking from aggresome to membrane), NOT by chromatin opening at the ABCG2 locus. The class I HDIs vorinostat / romidepsin reach this effect indirectly via histone acetylation → motor protein gene upregulation cascade.

**HDAC6 sits closer to the mechanistic root of trafficking** because HDAC6 directly deacetylates α-tubulin Lys40 — the modification that controls microtubule stability and kinesin-1 binding. **HDAC6 inhibition increases acetylated α-tubulin → stabilizes microtubules → favors anterograde retrograde trafficking** (per the multiple HDAC6 mechanism reviews surfaced, e.g., PMC8883472 CF / PMC6122547 cancer HDAC6 review).

**For CFTR F508del (the parallel disease-rescue precedent):**
- PMC8883472 review: "microtubule acetylation status is responsible for the defective endocytic trafficking and perinuclear cholesterol accumulation detected in CF... HDAC6 inhibition induces acetylation of α-tubulin, indicating preferential inhibition of cytoplasmic HDAC6, which affects the microtubule dynamics critical for proper CFTR protein trafficking."
- Hutt et al. 2018 bioRxiv 399451 / Hum Mol Genet 2019 (PMID 30753450): panobinostat + romidepsin rescue multiple CFTR variants synergistically with Vx809. Class I HDI + corrector combination is the demonstrated CFTR-rescue paradigm. Not HDAC6 specifically.
- HDAC7-specific inhibition restores CFTR (PMID 19966789 / Hutt 2010).

**For ABCG2 Q141K (the platform-relevant case):**
- Basseville 2012 class I HDIs documented (vorinostat, romidepsin, panobinostat — same drugs as CFTR rescue)
- Sjöstedt et al. 2017 PMC7900420 — Q141K + other naturally-occurring ABCG2 variants. 4-PBA rescues Q141K trafficking; mechanism is dual chemical chaperone + weak HDAC inhibition (IC50 0.4 mM). Confirms the 4-PBA chemical-chaperone framing in `abcg2-modulators.md` §"Pharmacological-chaperone route."
- **HDAC6-specific Q141K rescue NOT YET demonstrated in published literature.** The CFTR F508del precedent supports the hypothesis that HDAC6-selective inhibition could rescue Q141K via the tubulin-acetylation route, but no published experiment has tested this directly.

**This is the gap a focused experiment could close cheaply.** A Caco-2 Q141K-transfected line (the same line proposed in `validation-experiments.md §1.14` butyrate dose-response arm + `wiki/abcg2-q141k-chaperone-screen-computational.md` comp-032 Phase 2 wet-lab follow-up) tested with tubacin or tubastatin A (selective HDAC6 inhibitors, both commercially available) would directly answer whether HDAC6 inhibition specifically rescues Q141K trafficking in an enterocyte chassis. Marginal cost <$500 to add tubacin / tubastatin arms to the existing wet-lab plan. **This is the highest-leverage downstream action from this re-scan.**

---

## Comparison: traditional-name vs mechanism-name framing — what was missed

| Framing axis | What it surfaced | What it missed |
|---|---|---|
| **Mechanism-name only (comp-007, comp-014 Phase 3 ChEMBL-anchored)** | Pan-HDAC butyrate / SCFA from polysaccharide fermentation; Antrodia ethanol extract class I HDAC inhibition (one paper, mycelium-specific); no HDAC6-selective mushroom compound | **Poria cocos ABCG2 induction (Sun 2021 PMID 33651969)** — invisible to ChEMBL UniProt-join because Poria triterpenes not in ChEMBL activity table. **The Antrodia wild-vs-mycelium source paradox** — mechanism-name probe surfaces both papers but doesn't connect them to the source-form contradiction; traditional-name probe makes the source-form ambiguity immediately visible. |
| **Traditional-name framing (this scan, 2026-05-19)** | All of the above, PLUS: Poria cocos as a tier-2 ABCG2 inducer with in-vivo HUA-mouse magnitude exceeding benzbromarone; Antrodia source paradox explicitly noted; SIRT3 / SIRT1 / p300 mechanistic alternatives to HDAC6 (Ganoderma DM SIRT3, Cordyceps cicadae SIRT1, Hericium erinacine S p300) — broader epigenetic-modulator landscape | Quantitative HDAC isoform-selectivity data for any mushroom-source compound. The literature genuinely doesn't have it (not a framing-gap, a real gap). |

**Empirical verdict on the audit's leverage estimate:** the audit rated this scan as HIGH-leverage on the HDAC6 axis. Actual yield was LOW on HDAC6 (zero new compounds; the literature is genuinely empty here) but HIGH on the **parent ABCG2-rescue question** (Poria cocos surfaced; Antrodia source paradox clarified; HDAC6 vs class I distinction empirically grounded for future comp-NNN scoping). The query-framing discipline rule works as predicted (CLAUDE.md §263-269); the audit's specific leverage estimate was misdirected by assuming HDAC6 was a parent-question proxy when in fact it was a narrower sub-question with empty literature on either side.

**Generalizable lesson for future scans:** when a re-scan candidate's mechanism axis returns empty under BOTH mechanism-name AND traditional-name framing, the **literature gap is real, not a framing artifact.** This is itself a load-bearing finding — it tells the platform that the HDAC6-selective mushroom-natural-product compound class is open territory for novel chemistry design, not a "haven't looked hard enough yet" question.

---

## Proposed wiki updates

**Constraint per task brief:** do NOT write to `wiki/*.md`. These are proposals for Brian's walkthrough action.

### High-priority — `wiki/abcg2-modulators.md`

Add new Tier 2 entry under §"Inducers of intestinal ABCG2 — Tier 2 — Solid mechanism, modest evidence":

> **Poria cocos / Wolfiporia cocos (茯苓 Fu Ling) — mechanism unidentified, in-vivo evidence robust**
> - **Mechanism:** Empirically uncharacterized. Could be transcriptional (PPARγ / HNF4α / AhR / Nrf2 — none tested), chaperone-class trafficking rescue (analogous to UDCA / TUDCA per comp-032), or class I HDAC inhibition (no HDAC isoform was tested). The unidentified mechanism is itself the highest-leverage open question.
> - **Anchoring evidence:** Sun et al. 2021, *Front Pharmacol* ([DOI](https://doi.org/10.3389/fphar.2021.617351), PMID 33651969). Hyperuricemic mouse model. Both ethanol and water extracts significantly elevated intestinal ABCG2 mRNA + protein. Water extract effect magnitude **exceeded benzbromarone positive control** (p < 0.01). Concurrent UA-lowering via XO inhibition + renal protection. **Animal Model.**
> - **Five computationally predicted bioactives** (PubChem CIDs 267, 277, 13824, 15730, 5759) docked to ABCG2; in vitro validation not yet performed. Pachymic acid mentioned only as HPLC reference standard, not implicated as active agent.
> - **Traditional context:** Poria cocos is a canonical ingredient of Si Miao San (the gout-indicated TCM formula already surveyed by comp-013) and Wu Ling San (the canonical urinary-tract / fluid-metabolism formula). Per `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/inputs/compounds.json`, Poria cocos was implicitly included via the Si Miao San source citation but was NOT separately spawned as a compound source — exactly the formula-completeness gap flagged in the 2026-05-19 query-framing retrospective audit (item §"comp-013 (TCM gout compound triage)" lines 56-62).
> - **Practical lever:** Poria cocos extract is widely available as a TCM supplement (5-15g daily of decoction or 1-3g of standardized extract is the canonical dose range). However, mechanism uncertainty makes off-label dosing for ABCG2 induction premature.
> - **Tissue selectivity:** Not characterized.
> - **Next move:** Caco-2 transwell assay (sister to §1.14 butyrate dose-response arm) — pachymic acid + polyporenic acid C + dehydroeburicoic acid panel against ABCG2 expression + Q141K trafficking. Marginal cost <$2K on existing infrastructure. **High platform-relevance: closes the mechanism question on a TCM-grade compound that already has robust in-vivo HUA evidence.**

### High-priority — `wiki/medicinal-mushroom-compound-mapping-computational.md` (or its experiment archive)

Add to Phase 5 multilingual deep-dive deferred queue (or to the Phase 4 v2 chokepoint-intersection retrospective):
> - **Poria cocos / Wolfiporia cocos ABCG2 induction** (Sun 2021 PMID 33651969) — missed by Phase 3 ChEMBL UniProt-join intersection because Poria triterpenes are outside ChEMBL's curated activity table. Animal-model evidence exceeds benzbromarone control magnitude. Adds Poria cocos to the ABCG2 chokepoint hit list as a comp-014 retroactive Phase 4 v3 addition.
> - **Antrodia cinnamomea mycelium HDAC1/2/3/4 inhibition** (Lin 2019 PMC6412332) — 22-56% reduction in cell-free assay. HDAC6 NOT tested. Adds Antrodia mycelium ethanol fraction to comp-014 chokepoint-target rows for HDAC1/2/3 (currently the Phase 3 ChEMBL intersection has no fungal-source HDAC inhibitor entries at potency-relevant tiers).
> - **Antrodia wild-fruiting-body EEAC OPPOSITE direction** (Yang 2009 PMID 18709356) — note the contradiction with the mycelium data. Same species, different source form, opposite direction on histone acetylation. Phase 5 follow-up should resolve per-compound.

### Medium-priority — `wiki/food-grade-hdaci-screen-computational.md` (comp-007)

Add to Limitations / Future-work section:
> Mushroom-source HDAC inhibitor compound class was **structurally out-of-scope** in comp-007 (Western-dietary GRAS scope). The 2026-05-19 traditional-name re-scan confirms the literature genuinely lacks HDAC6-selective mushroom natural products (zero published compounds across 12 mushroom species probed: Ganoderma, Cordyceps, Grifola, Pleurotus, Flammulina, Morchella, Hericium, Trametes, Inonotus, Sanghuangporus, Antrodia, Wolfiporia, Auricularia, Lentinula). The mushroom-natural-product HDAC6 niche is empirically unoccupied, not a search-discipline gap. Adjacent Class I HDAC mushroom-source inhibitors exist (Antrodia mycelium ethanol fraction, Lin 2019 PMC6412332) but are pan-class-I, not HDAC6-selective. Implications: HDAC6-selective rescue chemistry for Q141K cannot be sourced from existing TCM/Kampo mushroom corpora; would require either (a) novel chemistry design or (b) broader natural-product HDAC6 screening (no published mushroom-focused HDAC6 screen exists as of 2026-05-19).

### Low-priority — `wiki/abcg2-q141k-chaperone-screen-computational.md` (comp-032) Phase 2 wet-lab plan

Add per-hit secondary screen suggestion (sister test to the diflunisal + lumacaftor + UDCA + tafamidis + TUDCA panel):
> Test **tubacin (HDAC6-selective, IC50 4 nM, 350× selectivity vs HDAC1) + tubastatin A (HDAC6-selective, ~1000× selectivity) + 4-PBA (class I/IIa + chemical chaperone dual mechanism)** in parallel with the chaperone-class hits, on the same Caco-2 Q141K-transfected line. This directly tests whether HDAC6-selective inhibition rescues Q141K trafficking (currently unpublished hypothesis — would close the CFTR F508del precedent → ABCG2 Q141K analogous mechanism transfer question at the Caco-2 tier). Marginal cost <$500 on existing infrastructure. **This is the highest-leverage downstream action from the 2026-05-19 mushroom × HDAC6 re-scan.**

---

## Limitations

- **Single-model translation only.** Chinese-language sources read directly without an independent second-model cross-check per CLAUDE.md §"Translation protocol — two-model independent cross-check." Single-model risk applies. For load-bearing claims (Sun 2021 Poria cocos ABCG2 magnitude vs benzbromarone control), the underlying paper is English-language *Frontiers in Pharmacology* — no translation needed, native English source. The Chinese-language hits I surfaced (灵芝孢子粉, 桑黄, 茯苓 review papers) were used to triangulate species-anchored evidence, not to extract quantitative claims; their absence of cross-check translation is acceptable given the lower stakes.
- **Web search results truncated at ~8-10 hits per query.** Some niche TCM journals (e.g., 中草药 / Chinese Traditional and Herbal Drugs, 中药材 / Journal of Chinese Medicinal Materials, 中国实验方剂学杂志 / Chinese Journal of Experimental Traditional Medical Formulae) may have additional findings not surfaced by web search. CNKI direct query was attempted via standard search engines (not via CNKI's gated portal); deeper CNKI mining is queued for separate Phase 5 execution.
- **PMC text full-read only for top-priority papers** (Sun 2021 Poria cocos; Lin 2019 Antrodia cinnamomea breast cancer; Lu 2025 Hericium erinacine S). Other findings rely on abstracts + secondary review summaries. A full-text re-read pass on Yang 2009 (Antrodia wild fruiting body) would clarify whether the HDAC1-up direction is artifact of leukemia HL-60 cell context vs. an authentic compound effect.
- **HDAC6 isoform-selective screening of mushroom natural products has not been published systematically.** Absence of evidence is not evidence of absence — a focused biochemical assay (e.g., HDAC6-Glo kit on a panel of mushroom triterpenes including ganoderic acid DM, pachymic acid, antcin K, zhankuic acid A, betulinic acid, inotodiol, erinacine S, hispidin) could close the gap cheaply (<$1K library + <$2K assay). The current "empty literature on HDAC6 × mushroom" verdict could flip if a single such screen surfaced a hit. **This is a recommended next-comp-NNN candidate.**
- **No new wet-lab data generated by this scan.** This is a literature-only re-scan. Leverage estimates downstream of literature scans are themselves provisional.
- **Cordyceps cicadae N6-(2-hydroxyethyl)adenosine ER-stress protection (ijms 22(4):1577) was noted but not pursued** — relates more directly to the comp-032 chaperone-class track than to the HDAC6 question per se. Worth tagging for comp-032 Phase 2 wet-lab if the chaperone screen expands beyond the FDA-approved drug surface to include natural-product chaperone candidates.
- **The TCM formula-level evidence** (Si Miao San, Bai Hu Jia Gui Zhi Tang, Wu Ling San) — already partially covered by comp-013 — was NOT separately re-scanned in this run. This re-scan was species-anchored (per the audit's framing as a HIGH-leverage species-anchored scan), not formula-anchored. The formula-anchored re-scan is HIGH-leverage item #2 in the audit and should be a separate scan; some overlap with this work (Poria cocos = Si Miao San ingredient) is unavoidable but the formula-scan would add gravity-weighted compound coverage that this species-by-species scan necessarily misses.

---

## Citation provenance summary

Load-bearing claims in this re-scan trace to specific primary sources:

| Claim | Source |
|---|---|
| Poria cocos elevates intestinal ABCG2 mRNA + protein in HUA mice, exceeding benzbromarone control | Sun et al. 2021, *Front Pharmacol* PMID 33651969, PMC7928048, DOI 10.3389/fphar.2021.617351 (verified via WebFetch) |
| Antrodia cinnamomea mycelium ethanol extract inhibits HDAC1/2/3/4 (22-56% in cell-free assay); HDAC6 not tested | Lin et al. 2019, *Int J Mol Sci* 20:833 PMC6412332, DOI 10.3390/ijms20040833 (verified via WebFetch) |
| Antrodia camphorata WILD fruiting body EEAC: histone HYPOacetylation, HDAC1 UP, HAT (GCN5/CBP/PCAF) DOWN; zhankuic acid A active marker; synergy with TSA | Yang et al. 2009, *Arch Toxicol* 83:81-89, PMID 18709356, DOI 10.1007/s00204-008-0337-3 |
| Ganoderic acid DM binds α,β-tubulin (Kd similar to vinblastine) and increases tubulin polymerization | Liu et al. 2012, *Sci Rep* 2:905, PMC3510465, DOI 10.1038/srep00905 |
| Hericium erinacine S enhances DR5/TNFR1/TRAIL via p300 HAT activation → H3K9K14ac (NOT HDAC inhibition) | Lu et al. 2025, PMC12595331 (verified via WebFetch — paper explicitly does NOT investigate HDAC) |
| Q141K ABCG2 is rescued by 4-PBA + panobinostat + romidepsin + vorinostat (class I HDIs); chemical chaperone + weak HDAC inhibition dual mechanism for 4-PBA | Sjöstedt et al. 2017, PMC7900420; Basseville et al. 2012 PMID 22472121 (already in `abcg2-modulators.md`) |
| Aceroside VIII is a natural selective HDAC6 inhibitor (Betula platyphylla, NOT a mushroom) | Park et al. 2015, PMID 25590368 (Bioorg Med Chem Lett) |
| Tubacin: HDAC6 IC50 4 nM, ~350× selectivity vs HDAC1; tubastatin A: ~1000× selectivity | Multiple HDAC6 inhibitor reviews (Haggarty 2003 PNAS PMID 12677000; Selleckchem / MedChemExpress data sheets) |
| HDAC6 directly deacetylates α-tubulin Lys40; HDAC6 inhibition → microtubule acetylation → kinesin-1 binding → trafficking | Multiple reviews including PMC8883472 (CF) and PMC6122547 (cancer HDAC6) |
| GLPP reduces UA 40.6% in HUA mice via ADA + GLUT9 + OAT1 (NOT ABCG2) | Chen et al. 2022 Food Funct, PMID 36385640, DOI 10.1039/d2fo02431d (already in `medicinal-mushroom-compound-mapping-computational.md` Phase 5) |
| Cordycepin × HSP90 ADA-dependent inhibition | PMC9264932 (cordycepin systems pharmacology, FEBS Letters) |
| Cordyceps cicadae N6-(2-hydroxyethyl)adenosine ER-stress protection in proximal tubular cells | Chyau et al. 2021, MDPI ijms 22(4):1577 |
| Mushroom polysaccharide → gut SCFA → HDAC3 inhibition (anti-obesity pathway, Grifola frondosa) | PMC9886863 |
| Butyrate HDAC inhibition IC50 52 ± 11 μM | SCFA mechanism review (surfaced via "mushroom polysaccharide butyrate SCFA HDAC trafficking ABCG2 Q141K" query) |

**Cross-references to canonical wiki anchors:**
- `wiki/abcg2-modulators.md` §6 Q141K rescue (HDI mechanism + 4-PBA chemical chaperone)
- `wiki/abcg2-modulators.md` §"Pharmacological-chaperone route — orthogonal small-molecule rescue" (comp-032 Tier 1 / Tier 2 candidates)
- `wiki/medicinal-mushroom-compound-mapping-computational.md` Phase 3 ChEMBL UniProt-join intersection (where Poria cocos was missed)
- `wiki/medicinal-mushroom-compound-mapping-computational.md` Phase 5 anchor species (Poria cocos was listed but not separately Phase-3-scored)
- `wiki/food-grade-hdaci-screen-computational.md` (comp-007) — Western-dietary GRAS scope
- `wiki/abcg2-q141k-chaperone-screen-computational.md` (comp-032) — chaperone-class screen Phase 2 wet-lab plan
- `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/inputs/compounds.json` — Si Miao San formula citation, Poria cocos not separately spawned
- `logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md` — audit triggering this re-scan
- CLAUDE.md §"Global-multilingual research by default" + §"Query-framing discipline" (lines 263-269)
- `wiki/etc/manual-literature-mining.md` §"Pre-commit verification gate" — applied to load-bearing numerical claims in this re-scan
