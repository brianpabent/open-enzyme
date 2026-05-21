---
title: "Upstream Complement Modulator Sweep — Brief-Scrubbed Verification Re-Run (comp-020)"
date: 2026-05-08
tags:
  - computational
  - complement
  - cp0
  - chokepoint-0
  - c1q
  - masp-2
  - factor-b
  - factor-d
  - factor-h
  - rosmarinic-acid
  - luteolin
  - bupleurum
  - helicteres
  - fucoidan
  - heparin
  - flavonoid
  - lignan
  - polysaccharide
  - natural-product
  - tcm
  - chembl-coverage-gap
  - multilingual
  - verification-rerun
related:
  - complement-c5a-gout.md
  - daf-cd55-scr14-truncated-computational.md
  - cfh-mechanism-dissociation-cp0-candidates-computational.md
  - gout-genetic-variants.md
  - medicinal-mushroom-compound-mapping-computational.md
  - tcm-gout-compound-triage-computational.md
  - validation-experiments.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
  - computational-experiments.md
  - etc/manual-literature-mining.md
sources:
  - "Zhang T, Chen DF. Anticomplementary principles of a Chinese multiherb remedy for the treatment and prevention of SARS. J Ethnopharmacol 117(2):351-61 (2008). PMC7126446"
  - "Yin X, Lu Y, Cheng ZH, Chen DF. Anti-Complementary Components of Helicteres angustifolia. Molecules 21(11):1506 (2016). PMC6273495"
  - "Jin W, Zhang W, Liang H, Zhang Q. The Structure-Activity Relationship between Marine Algae Polysaccharides and Anti-Complement Activity. Mar Drugs 14(1):2 (2015). PMC4728500"
  - "Talsma DT et al. MASP-2 Is a Heparin-Binding Protease; Identification of Blocking Oligosaccharides. Front Immunol 11:732 (2020). PMC7212410"
  - "Wu M, Li H, Zhang YY, Chen DF. Development of a C3c-based ELISA method for the determination of anti-complementary potency of Bupleurum polysaccharides. Acta Pharm Sin B 5(4):316-22 (2015). PMC4629277"
  - "Zou YF et al. Purification and Partial Structural Characterization of a Complement Fixating Polysaccharide from Rhizomes of Ligusticum chuanxiong. Molecules 22(2):287 (2017). PMC6155779"
  - "Sahu A, Rawal N, Pangburn MK. Inhibition of complement by covalent attachment of rosmarinic acid to activated C3b. Biochem Pharmacol 57(12):1439-46 (1999). PMID 10353266"
  - "Peake PW, Pussell BA, Martyn P, Timmermans V, Charlesworth JA. The inhibitory effect of rosmarinic acid on complement involves the C5 convertase. Int J Immunopharmacol 13(7):853-7 (1991). PMID 1761351"
  - "Englberger W, Hadding U, Etschenberg E, Graf E, Leyck S, Winkelmann J, Parnham MJ. Rosmarinic acid: a new inhibitor of complement C3-convertase with anti-inflammatory activity. Int J Immunopharmacol 10(7):729-37 (1988). PMID 3198307"
status: published
---

# Upstream Complement Modulator Sweep — Brief-Scrubbed Verification Re-Run (comp-020)

> **Frozen analysis archived to [`./etc/experiments/comp-020-upstream-complement-verification-rerun/wiki-archive.md`](./etc/experiments/comp-020-upstream-complement-verification-rerun/wiki-archive.md)** (302 lines).
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `etc/experiments/comp-020-upstream-complement-verification-rerun/`.

**Plain-English summary first.** Open Enzyme is mapping every avenue to address gout. One of the seven bottlenecks the platform tracks is "complement priming" — when monosodium urate crystals appear in a joint, they activate the complement immune cascade, which generates C5a, which primes the NLRP3 inflammasome, which drives the gout flare's signature inflammation. That priming step is named CP0 in the platform. So far the platform's main intervention at CP0 is a protein-engineering thread (an engineered shortened version of the human DAF/CD55 receptor expressed in koji — see [comp-012](./daf-cd55-scr14-truncated-computational.md) and […]

**Where the analysis lives:**
- Full archived analysis: [`./etc/experiments/comp-020-upstream-complement-verification-rerun/wiki-archive.md`](./etc/experiments/comp-020-upstream-complement-verification-rerun/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`./etc/experiments/comp-020-upstream-complement-verification-rerun/`](./etc/experiments/comp-020-upstream-complement-verification-rerun/)
- **Helicteres benzofuran lignan replication track (comp-018 Phase 2, 2026-05-17):** [`./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json`](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json) — replication INCONCLUSIVE / ANCHOR-STILL-SINGLE; independent wet-lab replication recommended
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
