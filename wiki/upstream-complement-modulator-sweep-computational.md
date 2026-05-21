---
title: "Upstream Complement Modulator Sweep — Computational Analysis (comp-018)"
date: 2026-05-08
tags:
  - complement
  - upstream-cp0
  - cp0
  - c3-convertase
  - rosmarinic-acid
  - luteolin
  - bupleurum-polysaccharide
  - ganoderic-acid
  - natural-products
  - dietary
  - chokepoint-mapping
  - global-multilingual
  - computational
related:
  - computational-experiments.md
  - complement-c5a-gout.md
  - cfh-mechanism-dissociation-cp0-candidates-computational.md
  - gout-genetic-variants.md
  - daf-cd55-scr14-truncated-computational.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
  - medicinal-mushroom-compound-mapping-computational.md
  - tcm-gout-compound-triage-computational.md
  - modality-chokepoint-matrix.md
  - nlrp3-exploit-map.md
  - etc/manual-literature-mining.md
  - gout-action-guide.md
sources:
  - "Brian framing 2026-05-08: 'What are all the things upstream of CP0 that we could exploit, and any compound — fungal, plant, bacterial, marine — that affects them. If the answer is rosemary, I'll grow rosemary.'"
  - "Open Enzyme/CLAUDE.md §Tool discipline (Pass 3 review 2026-05-08): Paperclip restricted to PMC/arXiv/bioRxiv/medRxiv corpus; CNKI/WanFang/J-STAGE handled by direct multilingual searches"
  - "complement-c5a-gout.md §2.6 — classical pathway is the dominant initiator of MSU complement activation; therefore C3 convertase is the highest-leverage upstream node"
  - "Englberger W et al., Int J Immunopharmacol 1988;10(6):729-37 (PMID 3198307) — rosmarinic acid as C3 convertase inhibitor, IC50 5-10 µM optimal"
  - "Zhang T, Chen D, J Ethnopharmacol 2008;117(2):351-61 (PMID 18400428) — luteolin most potent flavonoid CP+AP, CH50/AP50 0.19/0.17 mM"
  - "Wu M et al., Acta Pharm Sin B 2015;5(4):316-22 (PMID 26579461) — Bupleurum polysaccharides lectin pathway IC50 ~1 mg/mL"
  - "Seo HW et al., Arch Pharm Res 2009;32(11):1573-9 (PMID 20091270) — Ganoderma triterpenes CP convertase, ganoderic acid Sz IC50 44.6 µM"
status: complete (Phase 2)
---

# Upstream Complement Modulator Sweep — Computational Analysis (comp-018)

> **Frozen analysis archived to [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/wiki-archive.md`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/wiki-archive.md)** (336 lines).
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `etc/experiments/comp-018-upstream-complement-modulator-sweep/`.

> **⚠️ Read this before propagating any finding from this page.** > > The brief that produced this experiment was contaminated by a contrived user-framing example ("if it's in rosemary I'll grow rosemary"), which biased the headline-promotion of rosmarinic acid as the singular Tier-1 candidate. **An independent brief-scrubbed verification re-run (comp-020)** ran 2026-05-08 and produced a meaningfully different ranking: three tied tier-1 candidates instead of one, with ***Helicteres* benzofuran lignans** (CH50 9/40 µM, single-paper anchor PMC6273495) as the highest-potency single hit in the corpus — beating rosmarinic acid by 4-20× on a matched assay. comp-020 also […]

**Where the analysis lives:**
- Full archived analysis: [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/wiki-archive.md`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/)
- **Phase 2 multilingual + Helicteres replication + C1-INH engineering literature:** [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)

---

## Phase 2 — Multilingual + Helicteres Replication + C1-INH Engineering Literature (2026-05-17)

> **Phase 2 deliverables live in [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/).** The Phase 1 contamination warning above remains in force; Phase 2 is additive, not a replacement.

### Headline finding

Phase 2 confirms the comp-020 tier-1 ranking holds at the small-molecule level (rosmarinic acid + luteolin + Helicteres benzofuran lignans tied), surfaces a new **orthogonal tier-1 candidate Phase 1 missed entirely — Houttuynia cordata polysaccharides** (Chinese / Japanese / Korean / Vietnamese dietary herb, CH50 79-318 µg/mL across crude + purified fractions, multi-target C2 + C4 + C5, multiple in vivo precedents), and grounds the C1-INH parallel engineering thread on three load-bearing literature anchors:

- **Bos 2003 ([PMID 12758149](https://pubmed.ncbi.nlm.nih.gov/12758149/), [doi:10.1016/s1570-9639(03)00107-9](https://doi.org/10.1016/s1570-9639(03)00107-9))** — Pichia pastoris yields 30-180 mg/L active rhC1-INH with same inhibitory capacity as plasma C1-INH despite different N-glycosylation. Direct precedent that yeast (Ascomycota) chassis is sufficient for active C1-INH production → koji thread plausible.
- **Liu 2004 ([PMID 15039314](https://pubmed.ncbi.nlm.nih.gov/15039314/), [PMC375168](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC375168/), [doi:10.1128/IAI.72.4.1946-1955.2004](https://doi.org/10.1128/IAI.72.4.1946-1955.2004))** — N-deglycosylated C1-INH RETAINS protease-inhibitor function (C1s complex formation) but LOSES LPS-binding endotoxin protection. For OE platform CP0 use case (MSU-driven complement priming), protease-inhibitor function is load-bearing → major risk reduction for non-mammalian (koji, LBP) chassis with different or absent N-glycan.
- **Cancian 2015 ([PMID 26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/), [doi:10.1097/ACI.0000000000000186](https://doi.org/10.1097/ACI.0000000000000186))** — Ruconest (conestat alfa, transgenic rabbit milk, non-human glycosylation) FDA-approved 2014 for HAE. Establishes regulatory precedent that FDA accepts recombinant C1-INH with non-human glycosylation provided protease-inhibitor function is demonstrated.

### New tier-1 ranking (Phase 2 final)

| Rank | Compound class | Lead candidate | Potency | Dietary access | Anchor status |
|---|---|---|---|---|---|
| 1a | Phenolic acid | Rosmarinic acid | C3b 34 µM; CP 137-180 µM; bell-shape | FDA GRAS rosemary / lemon balm / spearmint | Multi-anchor |
| 1b | Flavone (multi-mechanism) | Luteolin | CH50 190 µM (CP), AP50 170 µM | Dietary (parsley, celery, honeysuckle) | Multi-anchor across XO + URAT1 + CP |
| 1c | Benzofuran sesquilignan glucoside | Helicteres compound 5 | CH50 9 µM (highest single-compound potency) | Not dietary; tropical Sterculiaceae | SINGLE-ANCHOR — replication INCONCLUSIVE per Phase 2 ([`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json)) |
| **1d (NEW; DUAL-CHOKEPOINT, upgraded 2026-05-19)** | Pectic polysaccharide multi-target | **Houttuynia cordata polysaccharide class (HCP / HCPM)** | CH50 79-318 µg/mL across crude + purified (CP0); intestinal NLRP3↓ + tight junction↑ + TLR4-MD2 direct binding (CP1) | Widely dietary in Southeast Asia (鱼腥草 / どくだみ / diếp cá) | Multi-anchor: 3+ Chen Daofeng group papers (CP0) + Li 2025 [PMC12254813](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12254813/) (dual CP0+CP1) + Yu 2026 [PMC12937656](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12937656/) (TLR4 docking) + Cheng 2014 [PMC7112369](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7112369/) (structure-dependent caveat) |

### Helicteres replication outcome

INCONCLUSIVE / ANCHOR-STILL-SINGLE. Phase 2 found no independent group has reproduced the Yin 2016 ([PMC6273495](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6273495/), [doi:10.3390/molecules21111506](https://doi.org/10.3390/molecules21111506)) CH50 9/40 µM benzofuran lignan finding on a matched assay format. The Helicteres angustifolia genus has substantial cancer + antifibrotic + triterpene pharmacology literature but the upstream-complement angle is isolated to the single Yin 2016 paper. Structurally-adjacent benzofuran lignans (Styrax japonica egonol [PMID 15643559](https://pubmed.ncbi.nlm.nih.gov/15643559/), CP IC50 33 µM per Min 2004) are 3.7× weaker — possibly real exceptional pharmacology, possibly assay-format artifact. **Independent wet-lab replication on a different laboratory's CH50 protocol remains the load-bearing risk-closure step. Full structured analysis at [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json).**

### Multilingual-citation gap reframing

Phase 1 §10 listed "language barrier" as a limitation. **Phase 2 reframes this:** the upstream-complement natural product subfield is overwhelmingly Chinese-group (Chen Daofeng / Fudan, 14+ papers post-1999) and Japanese-group (Yamada / Kiyohara / Kitasato, 13+ papers since 1985) dominated, but these groups publish 80-95% in English-language journals (Planta Med, Carbohydr Res, Acta Pharm Sin B, Int J Biol Macromol, Phytomedicine). The actual barriers operational in Phase 1 were:

1. **Citation-network insularity** — the Chen / Yamada matched-assay anti-complementary CH50/AP50 hemolytic discipline is a self-contained methodology stream that doesn't get heavily cited outside its immediate field
2. **Topic-discovery framing** — traditional Chinese / Japanese terminology framings ("heat-clearing," "toxin-eliminating," 鱼腥草 vs Houttuynia cordata vs "anti-complementary polysaccharide") don't map cleanly to Western pharma mechanism-name queries
3. **Source-journal weighting** — Zhongguo Zhong Yao Za Zhi and Acta Pharm Sin B are PubMed-indexed but underweighted in Web of Science impact-factor rankings

**Implication for OE platform:** the CLAUDE.md "global-multilingual research by default" rule operates correctly. The operational discipline is to query by traditional-formula-name + species-name + traditional-pathology-framing in addition to mechanism-name. **A "C3 convertase inhibitor" query misses Houttuynia; a "Houttuynia cordata anti-complementary" query catches it.** Mechanism-name is the wrong starting point for non-Western literature.

### Phase 2 status

**Phase 2 complete — 2026-05-17.** Files:
- [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-multilingual-findings.md`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-multilingual-findings.md) — Tier 1/2/3 candidates surfaced from non-English-corpus + Chinese-group + Japanese-group English-corpus
- [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json) — Helicteres benzofuran lignan replication attempt + verdict + recommendation
- [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-c1-inh-engineering-literature.md`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-c1-inh-engineering-literature.md) — C1-INH heterologous expression literature thread + top-3 anchors for comp-037
- [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-summary.md`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-summary.md) — synthesis + new tier-1 ranking + comp-037 inputs

**Open follow-ups:** Independent wet-lab Helicteres replication; Houttuynia in vitro replication on OE protocol; comp-037 commit with explicit reference to Bos 2003 + Liu 2004 + Cancian 2015; Phase 3 multilingual extension for other mechanism classes; DeepSeek V4-Pro translation cross-check for 4 Chinese-language Phase 2 sources flagged `[TRANSLATION-SINGLE-MODEL]`.
