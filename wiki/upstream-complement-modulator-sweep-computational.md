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
status: complete (Phase 1)
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
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
