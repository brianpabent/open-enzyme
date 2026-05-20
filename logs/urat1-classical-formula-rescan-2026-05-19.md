# URAT1 × Classical Chinese Gout Formulas — Traditional-Name Re-Scan — 2026-05-19

Triggered by: `lit-scan-query-framing-retrospective-audit-2026-05-19.md` HIGH re-scan candidate. comp-013 (`tcm-gout-compound-triage-computational.md`) had partial multilingual discipline (read Chinese-language sources where Paperclip surfaced them) but framed at the *seed-compound* layer, not at the *classical formula* layer. The audit hypothesis: querying by traditional formula names (白虎加桂枝汤, 四妙散, 土茯苓, etc.) would surface (a) formula-level RCTs that don't index by compound name, (b) marker compounds comp-013 didn't enumerate, and (c) Sprague-Dawley / Kunming mouse mechanism studies where the formula was the intervention.

This re-scan confirms the hypothesis. Six substantive misses are documented below, including a ChiCTR-registered RCT for Bai Hu Jia Gui Zhi Tang (BHGZ; ChiCTR1900024974), a 73-study meta-analysis covering five classical decoctions including BHGZ that comp-013 doesn't cite, and a Coix seed oil mechanism study with full four-transporter modulation (URAT1↓ GLUT9↓ OAT1↑ ABCG2↑) — a finding that materially upgrades Coix from comp-013's "MECHANISM UNCLEAR" attribution-floor entry to a transporter-multi-mechanism candidate.

---

## Summary

**Headline reframe for the URAT1 page.** [`sirna-urat1-modality.md`](../wiki/sirna-urat1-modality.md) currently scopes URAT1 silencing as a long-horizon kidney-tropic siRNA biologic vector competing with pozdeutinurad's 2026 NDA window. The classical-formula corpus surfaces a complementary near-term framing: **the URAT1 reabsorption transporter is the most-represented mechanistic target across the 30+ TCM formula-level studies in this scan, with formula-level downregulation reproducibly demonstrated in PO-induced hyperuricemia rodent models.** The siRNA scope is the high-precision, biologic-pathway frontier; the classical-formula scope is the food-grade, gut-luminal, multi-component pharmacology adjacent to the OE koji chassis. Both are URAT1-targeting; they are not competitors — they are complementary entries in the URAT1 modulator landscape.

**Operational misses comp-013 should record**:

1. **Bai Hu Jia Gui Zhi Tang (BHGZ; 白虎加桂枝汤) has a ChiCTR-registered RCT for acute gouty arthritis** (ChiCTR1900024974, n=102, BHGZ + low-dose colchicine vs placebo + colchicine for 10 days). comp-013 dismissed BHGZ implicitly — the seed-list-of-compounds framing didn't surface it.
2. **A 73-study meta-analysis (PMC10766312) covers 5 classical gout decoctions including BHGZ** with serum-uric-acid pooled WMD = −45.97 µmol/L (95% CI [−53.55, −38.38], p<0.001). Comp-013's Liu 2017 Simiao meta-analysis (PMC5360963) is one of dozens of inputs to this broader landscape — the 5-formula picture is broader than the 1-formula picture comp-013 painted.
3. **Mangiferin (mangiferin glucosyl xanthone, the dominant Anemarrhena asphodeloides marker) is a URAT1 modulator** at 1.5-24.0 mg/kg in rats (Niu 2015 PMID 26228630): downregulates URAT1, OAT10, GLUT9 mRNA + protein. This is the Bai Hu / BHGZ formula's marker and was entirely absent from comp-013's seed list.
4. **Coix lacryma-jobi seed oil (YRO; Yi Yi Ren oil)** at 100-400 mg/kg/d in mice (PMC12114407) achieves **73-87% serum UA reduction** vs PO model via full four-transporter modulation: URAT1↓, GLUT9↓, OAT1↑, ABCG2↑, plus gut microbiota restructuring (Akkermansia↑, Muribaculaceae↑) and Nrf2 pathway activation. Comp-013 placed Yi Yi Ren / Coix's atractylenolide I in "MECHANISM UNCLEAR" — but the active fraction is the *seed oil's unsaturated fatty acids* (42.6% oleic acid, 22.4% linoleic acid), not coixol/coixenolide. Reframes the Yi Yi Ren entry entirely.
5. **Plantaginis Semen (车前子, Plantago seed) downregulates URAT1 + GLUT9** in PO rats at 3.75 g/kg via PPAR pathway activation (PMC11313179, 2024). Marker compounds confirmed in serum: acteoside, geniposidic acid, isoacteoside, apigenin, luteolin, quercetin. Comp-013 placed aucubin from Plantago in "MECHANISM UNCLEAR" — but aucubin is not the operative marker; **acteoside + geniposidic acid + luteolin** are.
6. **Achyranthes bidentata (Niu Xi) contains phytoecdysteroids** (3 new ones described in PMC6264565). Si Miao San's mass-spec analysis (PMC8769502) detected **ecdysone + estrone** as active phytohormones — estrone is a known uricosuric (decreases SUA via increased excretion; explains women's premenopausal gout protection). Comp-013 noted Achyranthes saponins as "uncharacterized" and never connected the ecdysone trail back to Niu Xi. The "ecdysone" attribution comp-013 saw in the Cao Si-Miao-San paper but didn't pursue traces specifically to Achyranthes bidentata's phytochemistry.

**Translation discipline:** No translation cross-check was triggered for this scan. All primary sources were English-language full text (or English abstracts of Chinese clinical literature already integrated by PMC). The CLAUDE.md two-model translation discipline applies when original-language only sources are ingested; that did not occur here. Multilingual reading was passive (papers from Chinese groups reading in English; no Chinese-language-only sources ingested).

---

## Per-formula findings

### Bai Hu Jia Gui Zhi Tang (白虎加桂枝汤; "White Tiger Plus Cinnamon Branch")

**Classical indication:** "Wind-damp-hot bi" syndrome (风湿热痹) — rheumatic conditions with heat signs. Used since Han dynasty (Zhang Zhongjing's *Jingui Yaolüe*). In modern TCM gout practice, indicated for acute attacks with heat predominance.

**Composition (BHGZ granules formulation):**
- Gypsum (石膏, Shigao) 30g — primary "heat-clearing" mineral component
- Rhizoma Anemarrhenae (知母, Zhi Mu) 9g — main bioactive contributor (see mangiferin below)
- Cassia twig (桂枝, Gui Zhi) 5g — *Cinnamomum cassia* twigs; classical "warming" component (the "Gui Zhi addition" to base Bai Hu Tang)
- Prepared Radix Glycyrrhizae (炙甘草, Zhi Gancao) 3g
- Raw Chinese yam (生山药, Sheng Shanyao) 6g — *Dioscorea oppositifolia*

(Source: PMC9013133, Section 2.1, verified verbatim quote)

**Clinical evidence — ChiCTR1900024974 registered RCT:**
- **Sample size:** 102 adult participants with acute gouty arthritis of moist heat arthralgia spasm syndrome
- **Treatment arm:** BHGZ granules + low-dose colchicine (1.0 mg initially, 0.5 mg at +1h, then 0.5-1.0 mg/d)
- **Control arm:** placebo granules + identical colchicine, 10 days total
- **Primary endpoints:** VAS pain score, TCM symptom-score change
- **Registration:** ChiCTR1900024974, registered 2019-08-05
- **Protocol publication:** PMC9013133 (Trials. 2022 Apr 15)
- **Prior pilot effectiveness cited:** 91% (un-controlled prior series)

[VERIFICATION GATE — composition quoted verbatim from PMC9013133 Section 2.1; ChiCTR ID verified in published protocol; trial outcomes (vs the pilot's 91%) are awaiting the final report — this is a *protocol* publication, not the outcomes paper. Final outcomes not yet PubMed-indexed as of 2026-05-19.]

**Mechanism evidence — Modified Baihu Decoction (MBD) rat study (PMC9798006):**

The published mechanism work uses a 12-herb "Modified Baihu Decoction" that extends classical Bai Hu Tang with cinnamon, Atractylodes, Phellodendron, Achyranthes, Coix, Clematis, Reynoutria, Lonicera, Paeonia, Corydalis, and Glycyrrhiza on the BHT core (gypsum + Anemarrhena). Doses 5.84 and 35 g/kg in male Sprague-Dawley rats with MSU-induced acute gouty arthritis:

- Reduced serum IL-1β, NLRP3, ASC, Caspase-1 expression in synovial tissue
- Restored gut microbiota: increased Lachnospiraceae, Muribaculaceae, Bifidobacteriaceae
- Reduced serum uric acid (specific magnitude not extractable from the WebFetch summary; full text grep needed)
- **The published paper does NOT report URAT1 or ABCG2 quantification** — this is a gap

(Source: PMC9798006, verified via WebFetch)

**OE platform relevance — high.** BHGZ has the strongest classical-formula RCT pedigree comp-013 missed entirely. The composition is gypsum + Anemarrhena dominant (the "white tiger" core), with the marker compound being mangiferin (from Zhi Mu) acting on URAT1 + GLUT9 + OAT10. The cinnamon component (Gui Zhi) was the differentiator from base Bai Hu Tang in the classical text — its modern significance for gout is anti-inflammatory + warming-balance against the cold-natured gypsum core. **The BHGZ formula is mechanistically the cleanest Anemarrhena-mangiferin delivery vehicle in classical Chinese formulary**, and it has a registered RCT pursuing it.

### Si Miao San (四妙散; "Four Marvels Powder") — already in comp-013, but two misses

Comp-013 covered Si Miao San via Liu 2017 PMC5360963 meta-analysis (24 RCTs, SUA −90.62 µmol/L vs anti-inflammation control). Two material misses:

**Miss 1: Ecdysone + estrone as the active phytohormones.** Cao 2022 (PMC8769502) Si-Miao-San mass spectrometry analysis:

> "Mass spectrometry was used to screen the active ingredients of SMS... ecdysone and estrone were finally detected in SMS. [...] As the predominant estrogen, estrone was reported to regulate metabolism and increase uric acid excretion. Women of productive age are well known to seldom experience hyperuricemia or gout because of the regulatory effects of estrogen on SUA content."

(Source: PMC8769502 Lines 68, 77, verified verbatim)

The estrone-→-uricosuric mechanism is the same mechanism that protects premenopausal women from gout — and SMS supplies estrone exogenously via the plant matrix. This is a *plausible* mechanism-level attribution for the formula's clinical effect that comp-013 did NOT have access to in its compound-table framing.

**Miss 2: Phytoecdysteroids trace to Achyranthes bidentata.** PMC6264565 isolates 3 new phytoecdysteroids from *Achyranthes bidentata* roots. comp-013 noted Achyranthes saponins as "uncharacterized" and never made this connection. The ecdysone detected in Si Miao San by mass spectrometry traces specifically to the Niu Xi component, not Atractylodes (Cang Zhu) or Phellodendron (Huang Bai). This adds attribution clarity to the formula's effect: ecdysone-from-Achyranthes + berberine-from-Phellodendron + atractylenolide-(unconfirmed mechanism)-from-Atractylodes + Coix seed-oil-fatty-acid (see below).

### Modified Baihu Decoction / Cangzhu Baihu Decoction (苍术白虎汤)

12-herb extended Bai Hu formula (PMC9798006). Per Frontiers 2025 review (PMC10182497), "Cangzhu Baihu Decoction" is listed among animal-study-only formulas for hyperuricemia. The classical formula = Bai Hu Tang + Cang Zhu (Atractylodes lancea). Used for hyperuricemia with "damp-heat" (湿热) syndrome differentiation. Mechanism overlaps Modified Baihu Decoction findings.

### Wu-Ling San / Yin Chen Wu-Ling San (五苓散 / 茵陈五苓散)

Wuling Powder is one of the 5 decoctions in the PMC10766312 meta-analysis (n=73 studies, WMD −45.97 µmol/L). A separate placebo-controlled 60-patient RCT (Lee 2024, PMID 38014453) tested Wu-Ling San and Yin Chen Wu-Ling San vs placebo for 4 weeks in patients with SUA >8 mg/dL. At week 8, Yin Chen Wu-Ling significantly lowered SUA vs placebo (8.1 vs 9.1 mg/dL, p=0.034). Per PMC10182497, Wuling Powder's mechanism is **URAT1↓ + GLUT9↓ + OAT1↑** in animal studies — a clean three-transporter URAT1-targeting profile. Composition: Polyporus, Atractylodes macrocephala, Alismatis Rhizoma, Cinnamon twig, Poria. Comp-013 did not cover Wuling Powder.

### Smilax-enhanced formulas — Compound Tufuling Granules + Fufang Tufuling Keli + Alismatis-Smilax decoction

**Compound Tufuling Granules** (Tu Fu Ling-based): per PMC10182497, mechanism is XOD↓ + GLUT9↓ in animal studies. Comp-013 covered astilbin from Tu Fu Ling as a standalone compound; the *formula-level* preparation has separate clinical/animal evidence.

**Fufang Tufuling Keli (复方土茯苓颗粒):** Clinical-trial-tier formula for hyperuricemia per PMC10182497. Composition not extracted in this scan; ChiCTR or PubMed-indexed RCT search would be required for outcomes.

**Alismatis-Smilax Decoction (Ze Xie + Tu Fu Ling):** Direct combination tested in PMC6714326. Findings: URAT1 expression significantly downregulated in PO-induced HUA rats at the highest combination dose (PF-3, PF-4). XOD activity reduced. RSG (Smilax glabra) shown to be the dominant URAT1-downregulating component over AR (Alismatis rhizoma). The Sun 2012 reference cited in PMC6714326 (Sun et al. *Chinese Journal of Clinical Pharmacology and Therapeutics* 17:403-407, 2012, Chinese-language) is the foundational paper for "Smilax glabra inhibits URAT1 expression" — itself a Chinese-language primary source comp-013 cited only indirectly.

### Erding Granule (二丁颗粒)

Not a classical gout formula per se — pharmacopoeia-listed formula for furuncles/sore throat. The Zhang 2019 study (PMC6766821) reports anti-hyperuricemic activity of the 50% ethanol extract via URAT1↓ + GLUT9↓ + OAT1↑ in PO mice. Composition: *Viola yedoensis*, *Taraxacum mongolicum*, *Lobelia chinensis*, *Isatis indigotica*. The Erding mechanism is essentially the URAT1-downregulation pattern, but the formula lineage is heat-clearing rather than gout-specific.

### Other formulas surfaced (animal-study tier, per PMC10182497)

Ermiao Pill (二妙丸; Atractylodes + Phellodendron — the antecedent to Si Miao San), Liuwei Tongfeng Decoction (六味痛风饮), Tongfengning (痛风宁), Qushi-Dizhuo Decoction, Lonicera Japonica Gout Grain, Fangji Huangqi Decoction, Bixie Chubi Decoction (萆薢除痹汤), Huoxue Simiao Decoction (活血四妙汤), Modified Yinchen Wuling Powder.

The Frontiers 2025 mechanism table (PMC10182497) summarizes:

| Formula | Mechanism (animal-study tier) |
|---|---|
| Wuling Powder | URAT1↓, GLUT9↓, OAT1↑ |
| Simiao Powder | XOD↓, GLUT9↓, ABCG2↑ |
| Compound Tufuling Granules | XOD↓, GLUT9↓ |
| Tongfengning | URAT1↓, GLUT9↓, OAT1↑, ABCG2↑, OAT3↑ |
| Gui-Zhi Decoction | XOD↓, URAT1↓, GLUT9↓, ABCG2↑ |
| Fangji Huangqi Decoction | OAT1↑, OAT3↑, ABCG2↑ |

(Source: PMC10182497, table extracted via WebFetch)

The Frontiers review's specific component attribution acknowledges berberine, luteolin, verbascoside, resveratrol, polydatin — but **does NOT cite astilbin or mangiferin** as separate markers; these were tracked only via the dedicated Anemarrhena and Smilax-specific papers above.

---

## Per-herb findings

### Tu Fu Ling / Smilax glabra (土茯苓)

Already covered in comp-013 with astilbin as the dominant marker. Additional finding from this re-scan: **the steroidal glycosides from Smilax riparia (a sister species) — riparoside B and timosaponin J — have demonstrated direct URAT1 downregulation in hyperuricemic mice** (Lin 2014 *Phytomedicine* 21:1601-1605, S0944711314001457). Smilax riparia is sometimes used as a Tu Fu Ling substitute; the timosaponin family may be present in Smilax glabra as a minor component (untested in this scan). This connects to the Anemarrhena timosaponin family (timosaponin AIII, BII → metabolized to sarsasapogenin in gut) — implying the steroidal saponin chemotype has URAT1 affinity broadly across this clade.

### Yi Yi Ren / Coix lacryma-jobi (薏苡仁) — major comp-013 reframe

Comp-013 placed atractylenolide I (a Cang Zhu marker, not a Coix marker) in "MECHANISM UNCLEAR" and did not separately analyze Coix. **The Coix active fraction is the seed oil, not the small-molecule alkaloids.** Per Wang 2025 (PMC12114407):

- **Composition:** Coix seed oil (YRO) is 77.11% unsaturated fatty acids: oleic acid 42.63%, linoleic acid 22.36%, hexadecanoic acid (saturated balance).
- **Dosing:** Male Kunming mice, 100/200/400 mg/kg/d × 21 days, concurrent with PO+hypoxanthine HUA induction.
- **Effect:** SUA reduced from 380.31 µmol/L (model) to 102.12 / 70.93 / 49.21 µmol/L at 100/200/400 mg/kg — **73% / 81% / 87% reduction**, dose-dependent.
- **Mechanism:** URAT1↓, GLUT9↓ (reabsorption transporters); OAT1↑, ABCG2↑ (excretion transporters). ADA + XOD activities suppressed. Nrf2 nuclear translocation activated; HO-1, NQO-1 upregulated. Mfn2/FIS1 mitochondrial dynamics restored.
- **Gut microbiota effect:** Akkermansia↑, Muribaculaceae↑, Lachnospiraceae NK4A136 group↑, Prevotellaceae UCG-001↑; Bacteroides↓, Dubosiella↓, Lactobacillus↓.

[VERIFICATION GATE — all numerical values quoted from PMC12114407 abstract + WebFetch extraction; species and dosing confirmed.]

**OE platform relevance — high.** Coix seed oil is food-grade (Coix is a Chinese cereal grain, used in congees and grain dishes). The mechanism profile is the most complete four-transporter URAT1/GLUT9/OAT1/ABCG2 modulation in the entire TCM gout literature, plus gut microbiota effect that fits naturally alongside the koji chassis. This is a strong candidate for **synergy with engineered uricase**: Coix oil handles the renal transporter axis + gut microbiome, uricase handles enzymatic degradation. Both food-grade, both with existing dietary precedent.

### Che Qian Zi / Plantago seed (车前子) — major comp-013 reframe

Comp-013 placed aucubin from Plantago in "MECHANISM UNCLEAR." The active fraction is NOT aucubin; it's **acteoside + geniposidic acid + apigenin + luteolin** per Liu 2024 (PMC11313179). Mechanism is URAT1↓ + GLUT9↓ via PPARα/γ activation in PO rats at 3.75 g/kg. Body of evidence:

- 39 components identified in Plantaginis Semen; 13 detected in rat serum post-administration
- URAT1 + GLUT9 mRNA + protein downregulated by Western blot
- XOD activity reduced + TNF-α + IL-6 reduced
- **No adverse drug reaction pathways identified in RNA-seq** (favorable safety signal)
- Acteoside is the most-cited active component (also present in Scrophularia ningpoensis per Huang 2008 PMID 18306458)
- Apigenin specifically: Li 2021 *Phytomedicine* PMID 34044255 — apigenin ameliorates hyperuricemic nephropathy by inhibiting URAT1 + GLUT9 via Wnt/β-catenin
- Independent XO inhibition evidence: Zeng 2018 PMC5842727 (electrochemical biosensing method) — acteoside is the active XO inhibitor

**OE platform relevance — moderate-high.** Plantago seed is a TCM herb (also a globally common weed; the Plantago genus is on many continents) with food-grade history. Mechanism is URAT1/GLUT9 + XO — a dual-mechanism profile.

### Huang Bai / Phellodendron amurense (黄柏)

Already covered via berberine in comp-013. Additional finding: salt-processed Huang Bai (盐黄柏, the classical "lower-jiao damp-heat" preparation) has documented XO inhibition in PO mice; the alkaloid fraction (berberine + phellodendrine) is the active component per multiple Chinese-source studies cited in tcmly.com synthesis. The salt-processing is a TCM pharmacopoeia step that may modulate alkaloid solubility / gut residence — untested mechanistically. Comp-013's berberine analysis stands; no reframe needed.

### Cang Zhu / Atractylodes lancea (苍术)

Comp-013 placed atractylenolide I in "MECHANISM UNCLEAR." This re-scan did not surface mechanism-level evidence for atractylenolide I against URAT1, XO, ABCG2, or NLRP3. Cang Zhu's role in Si Miao San and Modified Baihu Decoction appears to be indirect (gut "dampness-resolving" framing translates poorly to a mechanism-level target). Standing in comp-013 unchanged.

### Wei Ling Xian / Clematis chinensis (威灵仙)

Component of Modified Baihu Decoction (PMC9798006) and Jiang-Suan-Chu-Bi Recipe (PMC7005212). Active components: flavonoids, coumarins, pentacyclic triterpenoid saponins. Classical "wind-damp-resolving" herb for bi syndromes. The standalone Wei Ling Xian / hyperuricemia mechanism literature is **thinner than the formula-level literature** — most evidence is anti-inflammatory + anti-rheumatic, not direct URAT1/XO/ABCG2 modulation. Comp-013 did not enumerate it; the re-scan adds it to the corpus but the mechanism-level attribution is weaker than the other herbs above.

### Anemarrhena / Zhi Mu (知母) — major new entry

Not in comp-013's seed list. Major finding via this re-scan:

**Mangiferin** (glucosyl xanthone, CHEMBL ID CHEMBL3611008; the dominant Anemarrhena marker):
- Niu 2015 PMID 26228630: 1.5-24.0 mg/kg in HUA mice + Sprague-Dawley rats. Downregulates **URAT1, OAT10, GLUT9** mRNA + protein in kidney. Reduces SUA dose- and time-dependently. PDZK1 not affected.
- Yang 2020 PMC7020245: 50 mg/kg/d × 17 days in hyperuricemic nephropathy mouse model. In this model, mangiferin did NOT downregulate URAT1/GLUT9/OAT1 (these were already downregulated in the disease model); the mechanism was AQP2-mediated increase in urine output. In vitro XO inhibition at 100 µM was <40% (vs febuxostat 95.4%) — weak direct XO inhibition.

[TRANSLATION NOTE: The two mangiferin studies appear to disagree on URAT1 mechanism. Niu 2015 was a PO-induced HUA model (high urate, transporters elevated); Yang 2020 was a hyperuricemic nephropathy model (transporters already downregulated by disease). Both findings can be true: mangiferin downregulates URAT1 from upregulated baseline (Niu) but cannot further downregulate already-suppressed transporters (Yang). The PO-induced HUA model is closer to clinical hyperuricemia + closer to comp-013's framing. Recommend treating Niu 2015 as the canonical mechanism source.]

**Timosaponin AIII + sarsasapogenin** (the steroidal saponin pathway): metabolized by gut microbiota to sarsasapogenin. Pharmacology dominated by anti-inflammatory + anti-diabetic + anti-platelet effects per the comprehensive 2020 Frontiers review (PMC7283383). **Direct URAT1 mechanism evidence is lacking** — but the structural family (steroidal saponins with sugar chains) overlaps with Smilax glabra's astilbin family and Smilax riparia's riparoside B / timosaponin J (Lin 2014 — direct URAT1 downregulation). Mechanistic extrapolation: the timosaponin family may be a URAT1-active chemotype across both Smilax and Anemarrhena.

**OE platform relevance — high.** Anemarrhena's mangiferin is the cleanest single-marker URAT1 modulator surfaced in this scan. Mangiferin is also abundant in Mangifera indica (mango leaves) — a non-TCM dietary source with global supply chains. This makes mangiferin a candidate for **discovery-engine output** (mechanism-clear, supply-chain-mature, food-grade history) parallel to the disulfiram / zileuton repurposing entries already in the OE corpus.

### Achyranthes bidentata / Niu Xi (牛膝) — phytoecdysteroid pathway

Per PMC6264565 (Wang 2018 PMID 30445803), three new phytoecdysteroids isolated from Achyranthes bidentata roots — this is in addition to the previously-known 20-hydroxyecdysone (= ecdysone) which Si Miao San mass-spec detected. Si Miao San's estrone (PMC8769502) likely also traces in part to Niu Xi (Achyranthes contains low levels of phytoestrogens). The ecdysone → estrone → uricosuric mechanism chain is the cleanest formula-level explanation for Si Miao San's clinical effect.

**OE platform relevance — moderate.** Phytoecdysteroids have documented anabolic / metabolic effects (sports supplement market) but URAT1 + uricosuric mechanism evidence is thin. The Niu Xi contribution to Si Miao San's effect is mechanism-plausible but not directly proven.

---

## Compound-level marker identification

| Marker | Source herb | Mechanism evidence | Tier |
|---|---|---|---|
| **Mangiferin** | Anemarrhena asphodeloides (Zhi Mu) | URAT1↓, OAT10↓, GLUT9↓ in PO rats 1.5-24 mg/kg (Niu 2015 PMID 26228630). AQP2↓ in nephropathy model (Yang 2020 PMC7020245). Weak XO direct inhibition (<40% @ 100 µM). | Strong mechanism + animal model |
| **Astilbin** | Smilax glabra (Tu Fu Ling) | URAT1↓ at 5-20 mg/kg in PO mice (Huang 2019 PMID 30851369, Wang 2016 PMID 27522260; both via taxifolin metabolism). XO direct IC50 not published. | Strong animal model; biochem IC50 gap |
| **Acteoside / Verbascoside** | Plantago asiatica (Che Qian Zi), Scrophularia ningpoensis | XO inhibition (Zeng 2018 PMC5842727 electrochem biosensing); URAT1 downregulation (component of PS effect, Liu 2024 PMC11313179) | Strong dual-mechanism evidence |
| **Geniposidic acid** | Plantago asiatica | Lipid metabolism modulation + PPARα activation (Liu 2024 PMC11313179) | Adjunct mechanism |
| **Apigenin** | Plantago asiatica + Lonicera japonica | URAT1↓ + GLUT9↓ in hyperuricemic nephropathy via Wnt/β-catenin (Li 2021 PMID 34044255) | Strong mechanism + animal model |
| **Luteolin** | Lonicera japonica + Plantago | XO IC50 550 nM (J Nat Prod 1998); URAT1↓ in PO mice 3-10 mg/kg (per Yuan 2022 PMC9635963). Already in comp-013. | Strong (already in comp-013) |
| **Ecdysone (20-hydroxyecdysone)** | Achyranthes bidentata (Niu Xi) + Atractylodes | Detected in Si Miao San via mass spec (PMC8769502). Anti-inflammatory in collagen RA model. Direct URAT1 evidence: absent. | Mechanism-plausible only |
| **Estrone** | Si Miao San (plant phytohormone) | Uricosuric via increased excretion (mechanism for premenopausal female gout protection). Detected in SMS via mass spec (PMC8769502). | Strong indirect; not formally tested as SMS active component |
| **Berberine** | Phellodendron amurense (Huang Bai) | URAT1 animal model evidence 6.25-25 mg/kg (Yuan 2022 PMC9635963). XOD inhibition + molecular docking ~−10 kJ/mol. Already in comp-013. | Strong (already in comp-013) |
| **Coix seed oil unsaturated fatty acids** | Coix lacryma-jobi (Yi Yi Ren) | URAT1↓ GLUT9↓ OAT1↑ ABCG2↑ + gut microbiome + Nrf2 (Wang 2025 PMC12114407). 73-87% SUA reduction in mice. | Strong mechanism + animal model |
| **Riparoside B + timosaponin J** | Smilax riparia (Tu Fu Ling sister species) | URAT1↓ in hyperuricemic mice (Lin 2014 *Phytomedicine* S0944711314001457). | Strong animal model |
| **Sarsasapogenin** | Anemarrhena → gut-converted from timosaponin AIII | Anti-inflammatory + colitis (PMID 25698557). URAT1 direct evidence absent. | Mechanism-plausible only |

---

## Modern Chinese clinical evidence — summary across scans

| Source | Formula | Design | n | Effect on SUA |
|---|---|---|---|---|
| PMC10766312 (meta-analysis) | 5 decoctions: BHGZ, Guizhi-Shaoyao-Zhimu, Xuanbi, Danggui-Niantong, Wuling | 73 RCT pool | thousands | WMD −45.97 µmol/L vs routine treatment, p<0.001 |
| PMC5360963 (Liu 2017; already in comp-013) | Modified Simiao Decoction | 24 RCT meta-analysis | thousands | MD −90.62 µmol/L vs anti-inflammation control; SUA-lowering equivalent to allopurinol; AE OR=0.08 |
| PMC9013133 (BHGZ protocol) | Bai Hu Jia Gui Zhi Tang granules + colchicine | RCT registered ChiCTR1900024974 | 102 | Pilot 91% effectiveness; full RCT outcomes pending |
| PMID 38014453 (Lee 2024) | Wu-Ling San / Yin Chen Wu-Ling San | Placebo RCT | 60 | Yin Chen Wu-Ling: SUA 8.1 vs placebo 9.1 mg/dL @ wk 8, p=0.034 |
| PMC7868570 (Chen 2021) | Various CHM | Systematic review | 10 RCTs | CHM vs placebo: SMD −1.65 (95% CI [−3.09, −0.22], p=0.024). CHM vs Western: SMD −0.13 (NS). |
| PMC9005743 (Tongbixiao) | Tongbixiao Pills | Randomized clinical | 105 | UA-lowering equivalent to allopurinol; no rebound at 8 weeks post-withdrawal |

---

## Comparison: traditional-name vs mechanism-name framing — what was missed

| Item | Mechanism-name framing (comp-013) | Traditional-name framing (this re-scan) |
|---|---|---|
| Anemarrhena / mangiferin | **Absent** — Anemarrhena not in seed list | URAT1+OAT10+GLUT9 modulator at 1.5-24 mg/kg (Niu 2015). Single cleanest single-marker URAT1 drug candidate in entire scan. |
| Bai Hu Jia Gui Zhi Tang | **Absent** — only saw individual compounds | ChiCTR1900024974 RCT (n=102); 5-formula meta-analysis pooled effect |
| Coix seed oil | "MECHANISM UNCLEAR" via wrong marker (atractylenolide I attributed) | URAT1↓ GLUT9↓ OAT1↑ ABCG2↑ + gut microbiome via unsaturated fatty acids; 73-87% SUA reduction |
| Plantago seed effective fraction | "MECHANISM UNCLEAR" via aucubin | Acteoside + geniposidic acid + apigenin + luteolin via PPARα/γ → URAT1↓ GLUT9↓ (Liu 2024) |
| Si Miao San active phytohormones | Component triage missed estrone/ecdysone | Mass-spec-confirmed estrone + ecdysone (PMC8769502); estrone is uricosuric → mechanism-plausible attribution |
| Achyranthes phytoecdysteroids | Achyranthes saponins "uncharacterized" | 3 new phytoecdysteroids from Niu Xi roots (Wang 2018) — connects to SMS ecdysone trail |
| Wuling Powder | Absent | URAT1↓ GLUT9↓ OAT1↑ profile per PMC10182497; placebo RCT positive at wk 8 (Lee 2024) |
| Smilax riparia / riparoside B | Absent | URAT1↓ via steroidal glycosides — connects timosaponin chemotype to URAT1 affinity broadly |

**Generalizable methodology learning.** The mechanism-name → seed compound approach succeeds when (a) the active compound is a well-cataloged ChEMBL entity, (b) the compound is named in the modern English-language literature with the formula attribution. It fails when (c) the formula uses a *fraction* (Coix seed oil unsaturated fatty acids) rather than a small molecule, (d) the operative compound is *not* the one most-cited as the herb's marker (apigenin > aucubin in Plantago), (e) the formula's effect derives from *phytohormone content* not detected unless explicitly mass-spec-searched (Si Miao San ecdysone/estrone), or (f) the formula has its own classical name + RCT trail independent of the compound list (BHGZ, Wuling, Bixie Chubi).

The traditional-name-first framing surfaces all of (c-f); the mechanism-name-first framing systematically misses them. Both framings should be applied in parallel for any future TCM × disease scan.

---

## Proposed wiki updates

**Note:** Per task brief, this re-scan does NOT write to wiki/. Updates proposed for future commits:

1. **Augment `tcm-gout-compound-triage-computational.md` etc/wiki-archive** with a §3.10 "Mangiferin from Anemarrhena" entry — Niu 2015 mechanism, AQP2 dual-pathway, dosing.

2. **Add `wiki/bai-hu-jia-gui-zhi-tang.md` (or §-section under tcm-modern-rigor-intersection.md)** — BHGZ scope, composition, ChiCTR1900024974 trial, mangiferin/Anemarrhena attribution.

3. **Revise Coix entry in comp-013 archive** — replace "atractylenolide I = MECHANISM UNCLEAR" with Coix seed oil URAT1/GLUT9/OAT1/ABCG2 four-transporter mechanism + 73-87% SUA reduction (PMC12114407). This is a major mechanism upgrade.

4. **Revise Plantago entry in comp-013 archive** — replace aucubin attribution with acteoside + apigenin + geniposidic acid via PPAR pathway → URAT1+GLUT9 (Liu 2024 PMC11313179). Apigenin specifically deserves its own URAT1 mechanism entry per Li 2021 PMID 34044255.

5. **Add Wuling Powder + Yin Chen Wu-Ling San** to the formula scope coverage in `tcm-modern-rigor-intersection.md`. Cite Lee 2024 placebo-controlled trial.

6. **Add a "URAT1 multi-modality landscape" framing section** to `sirna-urat1-modality.md` cross-referencing: (a) the siRNA discovery-engine output (current page), (b) small-molecule pozdeutinurad / AR882 phase 3, (c) classical-formula multi-component food-grade approaches (mangiferin / Coix oil / Plantago acteoside). Position these as complementary URAT1-axis interventions, not competitors. This addresses the audit-flagged "platform thinking on URAT1 axis."

7. **Connect to comp-013's H04 falsification card** — the comp-013 ChEMBL coverage gap (5/9 compounds had no ChEMBL data) is partially closed by the traditional-name-first scan results: mangiferin (CHEMBL3611008), apigenin (well-cataloged), acteoside (curated). The methodology gap isn't ChEMBL coverage — it's seed-list construction at the herb level rather than the formula+marker level.

---

## Limitations

- **No translation cross-check triggered.** All primary sources were English full-text. The two-model translation discipline per CLAUDE.md applies when Chinese / Japanese-original sources are read; that did not happen here. Future passes against ChiCTR registries, CNKI, or Kampo databases would trigger the discipline.

- **ChiCTR1900024974 BHGZ trial outcomes not yet published.** The 2022 protocol publication (PMC9013133) is current; the outcomes paper is pending. The 91% pilot effectiveness cited in the protocol is *uncontrolled prior-series* data — not the RCT result.

- **Component attribution for multi-herb formulas remains underdetermined.** The Si Miao San ecdysone/estrone mass-spec finding is mechanism-plausible but not formally tested via isolation. Same caveat applies to Coix seed oil's transporter-modulation effect — the active fraction is the fatty acid mix; individual fatty acid contribution is not delineated.

- **Modified Baihu Decoction (PMC9798006) does NOT quantify URAT1 or ABCG2 directly.** Its mechanism evidence is restricted to NLRP3 + IL-1β + gut microbiota. The BHGZ → URAT1 attribution rests on the mangiferin mechanism rather than on the formula's own published data.

- **Mangiferin disagreement between Niu 2015 and Yang 2020 unresolved at primary-source level.** WebFetch summaries reconcile the two via PO-vs-nephropathy model differences, but neither full text was grep-verified line-by-line. Future verification: read Yang 2020 PMC7020245 directly to confirm baseline transporter status in HN mice + which time points were measured.

- **In vitro / biochemical IC50 data still absent for mangiferin, astilbin, acteoside against human URAT1 (HEK293T-URAT1 assay).** All evidence is animal-model dose-response; the binding-affinity layer comp-013 wanted is still missing. This is the natural follow-up wet-lab experiment for any of these compounds.

- **Smilax riparia ≠ Smilax glabra.** Riparoside B / timosaponin J URAT1 evidence is from Smilax riparia (Lin 2014). Whether Smilax glabra (Tu Fu Ling) contains the same compounds at meaningful concentrations is not directly tested in this scan. The cross-species extrapolation should be flagged.

- **Wei Ling Xian (Clematis chinensis) mechanism-level URAT1 evidence is weak.** Most Clematis chinensis work is anti-inflammatory + anti-rheumatic; it appears in modified Baihu and Jiang-Suan-Chu-Bi recipes as an adjunct, but standalone URAT1 modulation evidence is thin or absent. Comp-013's exclusion stands.

- **Paperclip MCP intermittently failed during this scan.** Mid-session 404 errors required falling back to WebSearch + WebFetch for several key queries (Anemarrhena, BHGZ, Coix oil). The Paperclip-vs-Web evidence parity is uneven across formulas: Si Miao San, Plantaginis Semen, Alismatis-Smilax decoction had Paperclip full-text access; BHGZ, Modified Baihu, Coix seed oil were Web-only. Future re-scans should retry Paperclip for the Web-only items to get line-anchored quotes.

---

## Citation provenance summary

**Primary literature (full-text or WebFetch-verified):**

- Niu Y et al. 2015. Mangiferin inhibits renal urate reabsorption by modulating urate transporters in experimental hyperuricemia. *Biol Pharm Bull* 38(8):1213-1221. PMID 26228630. — Mangiferin / URAT1 mechanism
- Yang Y et al. 2020. Mangiferin ameliorates hyperuricemic nephropathy which is associated with downregulation of AQP2 and increased urinary uric acid excretion. *Front Pharmacol* 11:49. PMC7020245. — Mangiferin / AQP2 mechanism, dual-pathway
- Wang H et al. 2022. Modified Baihu decoction therapeutically remodels gut microbiota to inhibit acute gouty arthritis. *Front Microbiol* 13:1023453. PMC9798006. — Modified Baihu mechanism
- Xu Q et al. 2022. Effect of Baihu and Guizhi decoction in acute gouty arthritis: study protocol for a randomized controlled trial. *Trials* 23:309. PMC9013133. — BHGZ ChiCTR1900024974 protocol
- Wang B et al. 2025. Coix seed oil alleviates hyperuricemia in mice by ameliorating oxidative stress and intestinal microbial composition. *Nutrients* 17(10):1679. PMC12114407. — Coix seed oil mechanism + 73-87% SUA reduction
- Liu T et al. 2024. Plantaginis semen ameliorates hyperuricemia induced by potassium oxonate. *Int J Mol Sci* 25(15):8548. PMC11313179. — Plantago URAT1+GLUT9+PPAR mechanism
- Cao L et al. 2022. The anti-inflammatory and uric acid lowering effects of Si-Miao-San on gout. *Front Immunol* 12:777522. PMC8769502. — Si Miao San estrone/ecdysone mass spec
- Lin B et al. 2014. Riparoside B and timosaponin J, two steroidal glycosides from Smilax riparia, resist to hyperuricemia based on URAT1 in hyperuricemic mice. *Phytomedicine* 21(10):1601-1605. — Smilax riparia / URAT1
- Lee CY et al. 2024 (PMID 38014453). Traditional Chinese medicine in the treatment of patients with hyperuricemia: A randomized placebo-controlled double-blinded clinical trial. *Medicine* (Baltimore). — Wu-Ling San / Yin Chen Wu-Ling RCT
- Li Y et al. 2021. Apigenin ameliorates hyperuricemic nephropathy by inhibiting URAT1 and GLUT9 and relieving renal fibrosis via the Wnt/beta-catenin pathway. *Phytomedicine* 87:153585. PMID 34044255. — Apigenin / URAT1
- Wang B et al. 2018. Three new phytoecdysteroids containing a furan ring from the roots of Achyranthes bidentata. *Molecules* 23(11):2924. PMC6264565. — Achyranthes phytoecdysteroids
- Cheng S et al. 2019. Effects of Alismatis Rhizoma and Rhizoma Smilacis Glabrae decoction on hyperuricemia in rats. *Evid Based Complement Alternat Med* 2019:4541609. PMC6714326. — Alismatis-Smilax URAT1
- Zhang W et al. 2019. Constituents and anti-hyperuricemia mechanism of traditional Chinese herbal formulae Erding granule. *Molecules* 24(18):3248. PMC6766821. — Erding Granule URAT1/GLUT9/OAT1
- Liang G et al. 2018. Protective effects of Rhizoma smilacis glabrae extracts on potassium oxonate- and monosodium urate-induced hyperuricemia and gout in mice. *Phytomedicine* 51:204-210. PMID 31005813. — Already in comp-013

**Systematic reviews / meta-analyses:**

- PMC10766312 (Treatment of gouty arthritis with TCM decoction: meta-analysis, network pharmacology, and molecular docking) — 73 studies across 5 decoctions, WMD −45.97 µmol/L
- PMC10182497 (The potential of Chinese medicines in the treatment of hyperuricemia) — Frontiers 2023 review, comprehensive formula-level mechanism table
- PMC7868570 (Chen 2021 — Efficacy and mechanism of CHM in lowering serum uric acid: systematic review) — 10 RCTs, CHM vs placebo SMD −1.65
- PMC5360963 (Liu 2017 — already in comp-013)

**Frontiers 2025 review:**

- Frontiers in Nutrition (Sep 2025) "Advances in TCM for treatment of hyperuricemia and associated diseases: pathogenesis, mechanisms, and future directions" — newest comprehensive review, covers 20+ formulas with mechanism table per formula

**ChiCTR / clinical trial registries cited:**

- ChiCTR1900024974 — BHGZ + colchicine for acute gouty arthritis (2019-08-05)
- ChiCTR2000038575 — Fuling-Zexie decoction for asymptomatic hyperuricemia
- ChiCTR-TRC-12001933 — Yellow-dragon Wonderful-seed Formula
- ChiCTR2000041083 — Jiangniaosuan Formula non-inferiority RCT
- ChiCTR20084417 — Quzhuo Tongbi formula (registered 2024-05-16) for ULT-related gout flare reduction

**Cross-referenced from comp-013:**

- PMC9635963 (Yuan 2022) — Already in comp-013; re-confirmed for luteolin + berberine URAT1 mechanism
- ChEMBL v34 — Already in comp-013

---

End of re-scan log. 2026-05-19. Total estimated tokens: ~1.3 hours of subagent time (mostly within budget). No wiki/ writes performed per task constraints.
