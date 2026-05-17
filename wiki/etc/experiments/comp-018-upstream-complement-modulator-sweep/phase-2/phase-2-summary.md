# comp-018 Phase 2 — Synthesis Summary

**Date:** 2026-05-17
**Position in comp-018 lifecycle:** Phase 1 complete (2026-05-08); comp-020 brief-scrubbed verification re-run complete (2026-05-08); Phase 2 multilingual + Helicteres replication + C1-INH engineering literature thread (this document).

---

## Headline (one sentence)

**Phase 2 confirms the comp-020 tier-1 ranking holds at the small-molecule level (rosmarinic acid + luteolin + Helicteres benzofuran lignans tied; Helicteres replication remains single-anchor INCONCLUSIVE), surfaces a new orthogonal tier-1 candidate (Houttuynia cordata polysaccharides — Chinese folk medicine, dietary, mass-action mechanism via C2 + C4 + C5), and grounds the C1-INH parallel engineering thread on three load-bearing literature anchors (Pichia 30-180 mg/L active production per Bos 2003; deglycosylation-robust protease-inhibitor function per Liu 2004; Ruconest FDA regulatory precedent for non-mammalian glycosylation per Cancian 2015) — together informing the concurrent comp-037 C1-INH protease-stability computational track and reframing the LBP-luminal-C1-INH thesis as novel/unprecedented at the regulatory level but mechanistically plausible.**

---

## §1 What changed vs Phase 1

### §1.1 New tier-1 single-compound candidates

| Candidate | Source | Mechanism | Tier-1 evidence | Phase 1 status |
|---|---|---|---|---|
| **Houttuynia cordata crude polysaccharide (CHCP)** | Chinese / Japanese / Korean / Vietnamese dietary herb (鱼腥草 / どくだみ) | CH50 79 µg/mL crude (Zhang 2012 PMID 23126186, source-lang Chinese); 254 µg/mL purified HCPM (Zhou 2022 PMID 36252625); 272-318 µg/mL HC-PS1/3 (Lu 2019 PMID 31250410). Targets C2 + C4 + C5 | In vivo: H1N1-ALI protection, LPS fever, hemorrhagic-shock + LPS two-hit ALI model (Lu 2017 PMC5925397) | MISSED entirely |
| **Quercus glauca tetragalloyl glucose** | Korean folk medicine (Quercus species leaves + stem bark) | CP IC50 32.3 µM matched-assay hemolytic (Chung 2010 PMID 21078772) | Single-anchor in vitro | MISSED entirely |
| **Glycyrrhiza uralensis pectic polysaccharide PG-1c** | Licorice (FDA GRAS, dietary tier) | Matched-assay anti-complementary; rhamnogalacturonan core + neutral side chains load-bearing (Kiyohara 1996 PMID 8720381) | Single-group anchor (Kitasato / Yamada), 5+ companion papers in Yamada corpus | MISSED (Phase 1 caught glycyrrhizin not polysaccharide layer) |
| **Caffeic acid (Rabdosia japonica context)** | Coffee, apple, prune, blueberry dietary tier; widespread phenolic acid | CH50 0.041 g/L (≈230 µM) classical pathway (Yao 2013 PMID 23672041, source-lang Chinese) | Single-anchor in vitro | MISSED entirely (Phase 1 had caffeic acid for XO inhibition, not CP) |

### §1.2 New tier-2 candidates (orthogonal to Phase 1's tier-1)

Six additional tier-2 candidates from Phase 2 multilingual: Amomum tsao-ko diarylheptanoid, Viola kunawarensis sterols, Myricaria wardii (Tibetan), Juniperus pingii (Tibetan), Bupleurum chinense BC-PS1/2 + B. smithii D3-S1 (companions to Phase 1's Wu 2015), Scutellaria barbata B3-PS1, Styrax japonica egonol (Korean — relevant as potential drop-in replacement for Helicteres replication testing).

### §1.3 Mechanistic reframings

- **Scutellaria baicalensis aglycone-vs-glycoside metabolic-activation thread.** Baicalin (glycoside, dominant in Scutellaria root) is INACTIVE at complement in vitro; baicalein/oroxylin A/wogonin/chrysin (aglycones, generated in vivo by gut-microbiome β-glucuronidase) ARE active. IAV-infected mice have ELEVATED gut-microbiome β-glucuronidase activity vs healthy mice — implying inflammation state up-regulates the active form. Phase 1 caught baicalein and the aglycones but missed the metabolic-activation mechanism (Zhi 2019 PMID 31525575). **Triple-convergence pattern** (compound + multiple-mechanism + state-dependent activation) extends to Scutellaria baicalensis.
- **The "language barrier" framing in Phase 1 limitations was empirically incorrect.** Phase 2 finding: the upstream-complement natural product subfield is dominated by Chinese-group (Chen Daofeng / Fudan, 14+ papers post-1999) and Japanese-group (Yamada / Kitasato, 13+ papers since 1985) labs that publish overwhelmingly in English. The actual barrier was citation-network insularity and traditional-medicine-formula-name vs Western-pharma-mechanism-name query discoverability — NOT translation cost. CLAUDE.md's global-multilingual rule operates correctly, but the operational discipline is to query by traditional-formula-name + species-name in addition to mechanism-name.

---

## §2 What changed vs comp-020 verification re-run

### §2.1 Tier-1 small-molecule ranking — UNCHANGED

comp-020 tier-1 ranking (rosmarinic acid + luteolin + Helicteres benzofuran lignans, with Helicteres at highest single-compound potency CH50 9 µM single-anchor) remains the **load-bearing tier-1 single-compound ranking** post-Phase 2. Phase 2 did not displace any of these.

### §2.2 Helicteres replication status — INCONCLUSIVE / ANCHOR-STILL-SINGLE

Phase 2 attempted independent replication of the Yin 2016 CH50 9/40 µM Helicteres benzofuran lignan finding (PMC6273495). Result:
- No independent group has reproduced the CH50 metric on a matched assay format
- Helicteres genus has substantial cancer + antifibrotic + triterpene pharmacology literature but the upstream-complement angle is isolated to Yin 2016
- Structurally-adjacent benzofuran lignans (Styrax japonica egonol, IC50 33 µM per Min 2004 PMID 15643559) have much weaker reported potency on matched assays — possibly real exceptional pharmacology, possibly assay-format artifact
- **The verdict is INCONCLUSIVE. Independent wet-lab replication on a different laboratory's CH50 protocol with positive-control compounds (rosmarinic acid + luteolin + egonol) remains the load-bearing risk-closure step. Details in [`phase-2-helicteres-replication.json`](./phase-2-helicteres-replication.json).**

### §2.3 New orthogonal tier-1 — Houttuynia cordata polysaccharides

Houttuynia adds a **fourth tier-1 candidate orthogonal to the comp-020 small-molecule trio**:
- **Different chemical class:** polysaccharide vs small-molecule phenolic/lignan
- **Different mechanism:** C2 + C4 + C5 multi-target vs single-node convertase inhibition
- **Different evidence base:** in vivo H1N1-ALI + LPS-fever + two-hit ALI rodent models, plus matched-assay in vitro
- **Different dietary access:** widely eaten as vegetable in Vietnam, southern China, Korea, Japan (Houttuynia cordata leaf is a standard culinary herb)
- **Different therapeutic surface:** active at mass-action concentrations (microgram/mL, achievable via dietary or supplement use)

The comp-020 ranking should be UPDATED to reflect a **4-way tier-1**: rosmarinic acid + luteolin + Helicteres benzofuran lignans + Houttuynia cordata polysaccharide class. The single-compound-potency winner remains Helicteres (CH50 9 µM); the dietary-access winner is Houttuynia.

---

## §3 New tier-1 ranking — Phase 2 final

| Rank | Compound class | Lead candidate | Potency | Evidence tier | Dietary access | Single/Multi anchor |
|---|---|---|---|---|---|---|
| 1a | Phenolic acid | Rosmarinic acid | C3b 34 µM (Sahu 1999); CP 137-180 µM hemolytic (multiple groups); bell-shape 5-10 µM optimal per Englberger 1988 abstract-tier | 3 in vivo precedents; 1 clinical proxy (spearmint tea OA RCT) | FDA GRAS rosemary / lemon balm / spearmint | Multi-anchor (Englberger, Sahu, Peake, Proctor, Su, Connelly) |
| 1b | Flavone (multi-mechanism) | Luteolin | CH50 190 µM (CP), AP50 170 µM (Zhang & Chen 2008) | XO + URAT1 + CP convergent (triple-convergence) | Dietary tier (parsley, celery, honeysuckle, chamomile) | Multi-anchor across mechanisms |
| 1c | Benzofuran sesquilignan glucoside | Helicteres compound 5 (hedyotol-D-7''-O-β-D-glucopyranoside) | CH50 9 µM (highest single-compound potency in OE corpus) | SINGLE-ANCHOR (Yin 2016 PMC6273495), Phase 2 replication INCONCLUSIVE | Not dietary; tropical genus Sterculiaceae | Single-anchor — REPLICATION-FIRST |
| 1d | Pectic polysaccharide multi-target | Houttuynia cordata polysaccharide class | CH50 79-318 µg/mL (Zhang 2012, Lu 2019, Zhou 2022) | In vivo H1N1-ALI + LPS-fever + two-hit ALI rodent precedents | Widely dietary in Southeast Asia (鱼腥草 / どくだみ) | Multi-anchor (3 Chen Daofeng group papers) |

**Tier 2** remains as comp-020 + Phase 2 additions: Bupleurum (multiple species + fractions), marine sulfated polysaccharides (fucoidan with anticoagulation caveat), ganoderic acid Sz + ergosterol, falcarindiol, tiliroside, 3,5-dicaffeoylquinic acid, plus Phase 2 additions Amomum tsao-ko diarylheptanoid, Viola kunawarensis sterols, Quercus tetragalloyl glucose, caffeic acid (CP context), Glycyrrhiza pectic PG-1c, Scutellaria barbata B3-PS1, Styrax japonica egonol, Tibetan-medicine surface (Myricaria + Juniperus).

---

## §4 What informs comp-037 (the concurrent C1-INH protease-stability computational track)

The Phase 2 C1-INH engineering literature thread ([`phase-2-c1-inh-engineering-literature.md`](./phase-2-c1-inh-engineering-literature.md)) produces FOUR specific inputs for comp-037:

### §4.1 Yeast/Ascomycota chassis is sufficient — Pichia precedent at 30-180 mg/L

Bos 2003 (PMID 12758149) establishes that Pichia pastoris (Saccharomycotina, Ascomycota — same trophic kingdom as Aspergillus oryzae koji) yields active rhC1-INH at 30-180 mg/L with same inhibitory capacity as plasma C1-INH. This is direct precedent that the koji secretory and folding machinery is plausibly compatible with active C1-INH production. **comp-037 should benchmark its koji-protease-stability prediction against Bos 2003 as a positive control: if comp-037 predicts koji can produce active C1-INH at >30 mg/L equivalent, the prediction is consistent with empirical Pichia precedent.**

### §4.2 Deglycosylation-robust protease-inhibitor function — risk reduction for non-mammalian chassis

Liu 2004 (PMID 15039314, PMC375168) establishes that N-deglycosylated C1-INH RETAINS protease-inhibitor function (C1s complex formation) but LOSES LPS-binding endotoxin protection. For OE platform CP0 use case (MSU-driven complement priming), the protease-inhibitor function is load-bearing; LPS-binding is incidental. **comp-037 should explicitly note that the koji-expressed (mannose-rich N-glycan) or LBP-expressed (N-glycan-deficient) C1-INH retains the platform-relevant function.** Major risk reduction.

### §4.3 Regulatory precedent for non-mammalian glycosylation — Ruconest

Cancian 2015 (PMID 26106828) establishes that Ruconest / conestat alfa (transgenic rabbit milk, non-human glycosylation) is FDA-approved (2014) for HAE. **This provides regulatory precedent for the OE platform: FDA accepts recombinant C1-INH with non-human glycosylation pattern provided protease-inhibitor function is demonstrated. comp-037's downstream wet-lab gating can reasonably target the Ruconest activity benchmark.**

### §4.4 The LBP-luminal route is novel and unprecedented at the regulatory level

Phase 2 surfaced no FDA-approved oral, mucosal, or LBP-delivered C1-INH product. All FDA-approved C1-INH is IV or SC parenteral. **comp-037 should evaluate the LBP-luminal-C1-INH thesis with explicit acknowledgment of this regulatory novelty**, and may want to reframe the LBP thesis as "LBP-as-systemic-source" rather than "LBP-as-luminal-deliverer" for the gout indication where systemic action is needed. comp-037 should also computationally evaluate gut-lumen protease vulnerability of the C1-INH reactive-center loop (pepsin / trypsin / chymotrypsin / elastase) — the serpin RCL is by design protease-cleavable, which is a load-bearing risk for any luminal-delivery thesis.

---

## §5 Files created in Phase 2

```
wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/
├── phase-2-multilingual-findings.md     (Tier 1/2/3 candidates from non-English-corpus + Chinese-group + Japanese-group English-corpus)
├── phase-2-helicteres-replication.json  (Helicteres benzofuran lignan replication attempt + verdict + recommendation)
├── phase-2-c1-inh-engineering-literature.md  (C1-INH heterologous expression literature thread + top-3 anchors for comp-037)
└── phase-2-summary.md                   (this document — synthesis + tier-1 ranking + comp-037 inputs)
```

---

## §6 Cross-link updates needed (handled in the wiki update commit, NOT by this subagent)

The Phase 2 work informs these wiki cross-links the main agent will land:

1. **`wiki/upstream-complement-modulator-sweep-computational.md`** — add a Phase 2 section at the bottom (preserving the contamination warning and Phase 1 content). Status promotion: Phase 1 → Phase 2 complete.

2. **`wiki/upstream-complement-verification-rerun-computational.md`** — add a one-line pointer to Phase 2's Helicteres replication track ([`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json)).

3. **`wiki/computational-experiments.md`** — Phase 2 promotion row markdown snippet for the tracking-index (in this document's final report, NOT applied by this subagent):

```markdown
| comp-018 Phase 2 | 2026-05-17 | Upstream-CP0 modulator multilingual sweep + Helicteres replication + C1-INH engineering literature | 4-way tier-1 with Houttuynia added; Helicteres replication INCONCLUSIVE single-anchor; C1-INH engineering anchored on Bos 2003 Pichia + Liu 2004 deglyc + Ruconest 2014 | `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/` |
```

---

## §7 Open follow-ups

1. **Independent wet-lab Helicteres replication** — the comp-018 / comp-020 / Phase 2 corpus's single-anchor highest-potency lead. Cost ~$5000-15000 + 2-4 weeks calendar time. Highest single-action-item priority.

2. **Houttuynia cordata in vitro replication on OE wet-lab protocol** — Phase 2's new tier-1, has multi-anchor evidence base, but OE-platform-specific assay confirmation would substantiate the dietary-tier proposition.

3. **comp-037 commit** (concurrent computational track for C1-INH protease stability) — Phase 2 anchors are ready; comp-037 should land with explicit reference to PMID 12758149 (Bos 2003 Pichia), PMID 15039314 (Liu 2004 deglycosylation), and PMID 26106828 (Cancian 2015 Ruconest regulatory).

4. **Phase 3 multilingual extension** — Phase 2 found that the upstream-complement subfield is English-anchored despite being Chinese-group-and-Japanese-group dominated. Other mechanism classes (antiviral plant compounds, urate-lowering TCM, NLRP3-modulating Kampo) may have more Chinese-language-only literature; future Phase 3 multilingual sweeps for those classes should NOT assume the same English-coverage as observed in upstream-complement.

5. **Translation cross-check for the 4 Chinese-language Phase 2 sources flagged `[TRANSLATION-SINGLE-MODEL]`** (PMID 23126186, PMID 29192453, PMID 23672041, PMID 21548362) — DeepSeek V4-Pro cross-check before any wet-lab gate depends on their specific numeric claims, per CLAUDE.md §Translation protocol mandatory rule.

6. **The "global-multilingual research by default" rule in CLAUDE.md needs an operational refinement note** — the Phase 2 finding that the upstream-complement subfield is English-anchored-despite-being-Chinese-group-dominated reframes the rule's underlying assumption. Recommend adding to the rule: "the multilingual discipline catches different failure modes for different mechanism fields — sometimes the gap is translation cost (true non-English-only literature), sometimes it's citation-network insularity (Chinese/Japanese groups publishing in English but underweighted in Western database curation), sometimes it's topic-discovery framing (traditional-medicine-formula-name vs Western-pharma-mechanism-name query mismatch). The operational discipline is to query by traditional-formula-name + species-name + traditional-pathology-framing in addition to mechanism-name." This recommendation goes to the main agent for CLAUDE.md edit consideration (NOT performed by this subagent).
