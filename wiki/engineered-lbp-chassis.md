---
title: "Engineered Live Biotherapeutic Products (LBP) Chassis — Peer Track to Koji"
date: 2026-05-05
tags:
  - engineered-lbps
  - chassis-class
  - faecalibacterium-prausnitzii
  - akkermansia-muciniphila
  - bacteroides
  - obligate-anaerobes
  - butyrate
  - durable-colonization
  - regulatory-lbp
  - platform-strategy
  - first-principles
related:
  - modality-chokepoint-matrix.md
  - koji-endgame-strain.md
  - abcg2-modulators.md
  - open-questions.md
  - open-enzyme-vision.md
  - synthesis.md
  - hypotheses/H02-engineered-lbp-thesis.md
sources:
  - "Vowst (Seres / Ferring) — FDA approval April 2023, *C. difficile* recurrence prevention (FMT-derived live biotherapeutic)"
  - "FDA Guidance for Industry: Early Clinical Trials with Live Biotherapeutic Products (2016, updated 2018)"
  - "Synlogic SYNB1934 (engineered E. coli Nissle, phenylketonuria — Phase 2)"
  - "Sonnenburg lab Bacteroides genome-engineering toolkit (Stanford, 2014–present)"
  - "Pendulum Therapeutics — non-engineered Akkermansia muciniphila commercial probiotic"
status: scope-page
---

# Engineered Live Biotherapeutic Products (LBP) Chassis — Peer Track to Koji

**Status:** scope-page (2026-05-05). This page defines the chassis class and queues the deep-dive follow-ups. The lit scans, falsification card, and comp-008 feasibility analysis are tracked under [Open Follow-Ups](#open-follow-ups) and will populate this page as they land.

---

## Why this page exists

The Open Enzyme platform was named for its first chassis (engineered enzymes expressed in koji and yeast). But the broader mission — *"solve gout via every available modality, fully open-source"* — is bigger than any single chassis. The [Modality × Target Matrix](./modality-chokepoint-matrix.md) was built to make that distinction visible. This page is the first attempt to develop one of the matrix's highest-leverage rows into a peer track to the koji chassis: **engineered Live Biotherapeutic Products (LBPs)**, specifically engineered obligate anaerobes that durably colonize the colon.

The motivation is structural. The koji and yeast chassis are **transit organisms**: they pass through the gut over hours-to-a-day. To maintain therapeutic effect the user has to keep eating them. By contrast, *Faecalibacterium prausnitzii*, *Akkermansia muciniphila*, and selected *Bacteroides* species are **resident anaerobes** — they evolved to live in the mammalian colon and, when delivered as a live therapeutic, can persist for **weeks to months** after a single dose. That changes the dosing model from "daily condiment" to "quarterly capsule."

This is a peer track, not a pivot. The koji chassis remains the clearest expression of the "democratized home access" thesis. The LBP chassis is the clearest expression of the "durable colonization, broad genotype coverage" thesis. Both serve the same mission, on different regulatory and distribution tracks.

---

## What an obligate anaerobe is, and why it matters

An **obligate anaerobe** is an organism that dies on contact with oxygen. *F. prausnitzii*, *Akkermansia muciniphila*, and most *Bacteroides* species evolved to live in the deep colon, where O₂ partial pressure is effectively zero. They cannot survive the small intestine (too aerobic), cannot grow under normal lab atmosphere, and cannot be home-fermented under any realistic kitchen conditions.

**This is the load-bearing limitation.** The Open Enzyme home-fermentation thesis (grow koji at home, make shio-koji or amazake condiment) does **not** transfer to obligate anaerobes. They require:

- **Anaerobic bioreactor manufacturing** (commercial-scale, oxygen-excluded)
- **Cold-chain stabilization** (lyophilized, oxygen-blocking capsule, often with cryoprotectant)
- **FDA Live Biotherapeutic Product (LBP) regulatory pathway** — distinct from the GRAS food path the koji chassis uses
- **Commercial pharmaceutical distribution** — pharmacy / mail order, not "buy spores online and grow them"

This is the structural reason the LBP chassis is a "commercial pharmaceutical product" track, not a "grow at home" track.

---

## Candidate species

### *Faecalibacterium prausnitzii* (primary candidate)

One of the most abundant species in a healthy human colon (3–5% of total gut bacteria). Strict anaerobe. Strain A2-165 is the model laboratory strain. Native producer of **butyrate** — a short-chain fatty acid with the cleanest known dual mechanism for ABCG2 induction (see [§ butyrate dual-action below](#butyrate-as-the-highest-leverage-payload)). Reduced abundance is documented in IBD and metabolic syndrome cohorts (In Vitro / Animal Model / human observational), making *F. prausnitzii* a target of multiple commercial probiotic and LBP programs already.

### *Akkermansia muciniphila* (mucus-layer specialist)

Strict anaerobe; resides in the mucus layer overlying the colonic epithelium. Documented to support gut barrier integrity and mucin turnover (Animal Model + human cohort). Already commercial as a non-engineered probiotic (Pendulum Therapeutics). For the Open Enzyme mission, *Akkermansia* is the natural chassis for engineered **gut-barrier repair** payloads — the TNFα-cycle relief vector documented in [`abcg2-modulators.md`](./abcg2-modulators.md) and [`lactoferrin.md`](./lactoferrin.md).

### *Bacteroides* species (broadest engineering toolkit)

Several *Bacteroides* species (notably *B. thetaiotaomicron*, *B. fragilis*) tolerate brief oxygen exposure and have the most mature genetic engineering toolkit among gut anaerobes (Sonnenburg lab at Stanford has driven much of this work). For payloads where genetic complexity is the bottleneck — multi-cassette constructs, conditional expression circuits, biosensor-driven payload release — *Bacteroides* may be the right starting chassis even if *F. prausnitzii* is the eventual target species.

### *Akkermansia* + *Faecalibacterium* + *Bacteroides* as a designed consortium

A future direction surfaced by the matrix: rather than picking one chassis, engineer a small designed consortium where each species carries a different payload optimized for its native niche. This is a more ambitious construct than any single-species LBP and is parked as a Phase 3 question.

---

## Butyrate as the highest-leverage payload

The cleanest reason to pursue *F. prausnitzii* engineering for gout specifically is that **butyrate hits two ABCG2-induction mechanisms at the same time:**

1. **Wild-type ABCG2 (everyone):** butyrate → PPARγ activation → upregulated ABCG2 transcription → more urate efflux from blood into the gut lumen. Mechanism: well-characterized; DASH RCT shows 0.25–0.73 mg/dL UA reduction in fiber-rich diets. (Clinical Trial / Mechanistic; source: [`abcg2-modulators.md`](./abcg2-modulators.md) §Inducers.)

2. **Q141K variant ABCG2 (~10% of people, Brian-relevant):** butyrate is also a class-I HDAC inhibitor → rescues the broken trafficking of the Q141K mutant protein → gets it to the cell surface where it can actually transport urate. Mechanism: Basseville 2012 PMID 22472121. (In Vitro; source: [`abcg2-modulators.md`](./abcg2-modulators.md) §Q141K rescue mechanism.)

This is **genotype-agnostic coverage** — a rare property. Most ABCG2-relevant interventions either work for WT (PPARγ inducers) or for Q141K (HDAC inhibitors), but not both. A live colonic strain producing butyrate continuously hits both populations simultaneously.

The ranking work in [`food-grade-hdaci-screen-computational.md`](./food-grade-hdaci-screen-computational.md) (comp-007, 2026-05-05) further validates butyrate's profile: it is the only food-grade HDAC inhibitor with biochemical IC50 data for all four relevant HDAC isoforms (HDAC1/2/3/6), and its 167× class-I-over-HDAC6 selectivity puts it ahead of every screened alternative. The challenge with butyrate is **continuous gut-luminal availability** — orally dosed butyrate is rapidly absorbed in the small intestine and does not reach the colon. A colonically-resident butyrate producer solves the bioavailability problem at the dose-frequency level.

---

## Other plausible payloads (Phase 2 to scope)

Beyond a butyrate-pathway boost, the LBP chassis class plausibly supports:

- **Heterologous uricase** (replicating the koji chassis function in a colonically-resident format — possibly a more direct route than rasburicase-class IV biologics for refractory gout)
- **Lactoferrin** (TNFα-cycle relief — the Open Enzyme endgame strain's CP1a/CP4/CP6b/CP5b coverage molecule)
- **Soluble complement regulators (sCR1, Factor H, DAF/CD55)** — the CP0 platform gap, see [comp-006](./daf-cd55-protease-stability-computational.md) for the koji-feasibility analysis (HIGH risk, stalk-driven; an LBP chassis avoids the koji protease environment entirely)
- **IL-22 secretion** (gut barrier repair — already in clinical development as engineered E. coli Nissle by Synlogic-adjacent programs)
- **Carnosine** (URAT1 / GLUT9 modulation — see [`carnosine.md`](./carnosine.md) and [`koji-endgame-strain.md` §2.5](./koji-endgame-strain.md))

Which of these are tractable in *F. prausnitzii* specifically (vs. *Bacteroides* vs. *Akkermansia*) is an open feasibility question — see [comp-008 in Open Follow-Ups](#open-follow-ups).

---

## Regulatory path

**FDA Live Biotherapeutic Products (LBP) framework:** introduced via the 2016 (updated 2018) Guidance for Industry "Early Clinical Trials with Live Biotherapeutic Products." Establishes a Biologic License Application (BLA) pathway distinct from food, supplement, or drug. Requires CMC characterization of the live product (strain identity, purity, viability, genetic stability), preclinical safety, and standard IND-enabling toxicology.

**Approved precedents:**
- **Vowst** (Seres → Ferring, April 2023) — first FDA-approved oral LBP. FMT-derived, *Firmicutes* spore preparation, *C. difficile* recurrence prevention. Establishes the regulatory template but is not engineered (taken from healthy human donor stool).
- **Engineered LBPs** — none yet FDA-approved. Synlogic's SYNB1934 (engineered *E. coli* Nissle for phenylketonuria) is in Phase 2 and is the most advanced engineered-LBP program. The path is being built.

**Implication for Open Enzyme:** an engineered *F. prausnitzii* therapeutic would be the second-or-third-in-class engineered LBP. Timeline from preclinical to BLA approval is conservatively **5–8 years** with a $50–200M capital requirement. This is squarely a **commercial pharmaceutical product** — incompatible with the home-fermentation thesis but well-aligned with Open Enzyme's broader mission of being a research platform that licenses or partners on commercial-grade outputs.

A detailed regulatory-landscape lit scan is queued — see [Open Follow-Ups](#open-follow-ups).

---

## Commercial / clinical landscape (preliminary)

The known active-program landscape, to be filled in by the Phase 2 commercial lit scan:

| Company | Chassis | Indication | Stage |
|---|---|---|---|
| Synlogic | engineered *E. coli* Nissle | Phenylketonuria (SYNB1934), homocystinuria, others | Phase 2 |
| Vedanta Biosciences | designed bacterial consortia | C. difficile, IBD, others | Phase 2 / 3 |
| NextBiotix | engineered *F. prausnitzii* | IBD (focus on the species itself, not specific to gout) | Preclinical / early clinical |
| Pendulum Therapeutics | non-engineered *Akkermansia muciniphila* + butyrate-producers | Metabolic syndrome (commercial probiotic) | Marketed as supplement |
| Seres Therapeutics | post-Vowst pivot | Multiple LBP indications | Various |

**Gout-specific engineered-LBP programs: zero known.** This matches the matrix's framing of *F. prausnitzii* engineering for gout as a genuinely empty exploration vector. The commercial landscape lit scan will refine this picture and identify potential partner profiles.

---

## Comparison with the koji chassis

| Dimension | Koji chassis (Open Enzyme primary) | LBP chassis (this page) |
|---|---|---|
| **Resident vs. transit** | Transit (hours to a day) | Resident (weeks to months) |
| **Dosing** | Daily — eat the condiment | Quarterly — swallow a capsule |
| **Manufacturing** | Home-fermentable; community-scale | Anaerobic bioreactor; commercial-scale only |
| **Cold chain** | Not required (live spore-form koji) | Required (lyophilized, O₂-blocking capsule) |
| **Regulatory path** | GRAS food / DSHEA supplement | FDA LBP / BLA biologic |
| **Distribution model** | Open-source spores / starter cultures | Pharmacy / mail-order pharmaceutical |
| **Genotype-coverage example** | WT ABCG2 (uricase + lactoferrin payload) | WT + Q141K simultaneously (butyrate dual-action) |
| **Capital to first commercial dose** | $0–500K (community / DIY-path realistic) | $50–200M (commercial-pharma realistic only) |
| **Time to first commercial dose** | Months (community-validated strains) | 5–8 years (BLA approval) |
| **Open-source compatibility** | Native — strain library on GitHub | Strain genetics open; manufacturing + clinical IP closed |
| **Home access** | Yes — defining property | No — fundamentally incompatible |

**The two tracks serve different patient populations and intervention philosophies.** The koji track serves the broader market (mild-to-moderate gout, dietary management, prevention, EPI applications). The LBP track serves the high-severity / Q141K / refractory-gout subset where pharmaceutical-grade durability and genotype-specific coverage is worth the cost-and-distribution overhead.

A future strategic question (Phase 3): does the LBP track justify expanding Open Enzyme's project framing from "engineered enzymes in koji" to "solve gout, every avenue, fully open"? Tracked in [Open Follow-Ups](#open-follow-ups) and queued in [`open-enzyme-vision.md`](./open-enzyme-vision.md).

---

## Open Follow-Ups

These are the queued deep-dive items that will populate this page over the coming sweeps. Each is a discrete, scoped piece of in silico work with no pharma-partner dependency. Tracked in multiple redundant surfaces (this page, [`open-questions.md`](./open-questions.md), [`computational-experiments.md`](./computational-experiments.md), [`index.md`](../index.md), [`hypotheses/H02-engineered-lbp-thesis.md`](./hypotheses/H02-engineered-lbp-thesis.md), and [`synthesis.md`](./synthesis.md)) so the daemon surfaces them on each sweep cycle.

| ID | Item | Type | Status |
|---|---|---|---|
| **P2-1** | Lit scan: *F. prausnitzii* engineering state-of-the-art (genetic toolkit, heterologous payload titers achieved, gap to therapeutic-grade) | Literature review (Opus subagent) | Queued |
| **P2-2** | Lit scan: commercial / clinical engineered-LBP landscape (Synlogic, Vedanta, NextBiotix, Seres, Pendulum, others — current programs, partnership / licensing profile) | Literature review (Opus subagent) | Queued |
| **P2-3** | Lit scan: FDA LBP regulatory path (2018 guidance, Vowst precedent, IND-enabling package, timeline + capital requirements) | Literature review (Opus subagent) | Queued |
| **P2-4** | comp-008: *F. prausnitzii* heterologous expression feasibility — codon usage, GC content, secretion machinery, payload tractability ranking | Computational analysis (Sonnet subagent) | Queued |
| **P2-5** | Falsification card H02: engineered LBP thesis — full claim, assumption stack, killshot menu, pre-committed thresholds | Hypothesis formalization | [Stub committed](./hypotheses/H02-engineered-lbp-thesis.md); full population queued |
| **P2-6** | Comparative chassis matrix for gout indication: *F. prausnitzii* vs. *Akkermansia* vs. *Bacteroides* vs. engineered *E. coli* Nissle — payload tractability, native-niche fit, engineering complexity | Synthesis (could be added to this page or stand alone) | Queued |
| **P3** | Platform-framing reflection: does the LBP track justify expanding Open Enzyme's framing from "engineered enzymes in koji" to "solve gout, every avenue, fully open"? Trigger: after Phase 2 items have accumulated enough substance to assess track maturity. | Strategic reflection | Queued, content-triggered |

---

## Limitations of this page

- **This is a scope-page, not a deep-dive.** The technical depth on engineering toolkit, regulatory specifics, commercial landscape, and species-specific payload feasibility comes from the Phase 2 follow-ups. Until those land, this page is the framing skeleton.
- **No wet-lab work proposed yet.** Engineering an obligate anaerobe is itself a substantial wet-lab capital commitment (anaerobic chamber + bioreactor + characterization assays, ~$500K–2M facility). The Phase 2 in silico work tells us whether to take that step.
- **Open Enzyme's expertise center-of-mass is fungal / yeast, not anaerobic bacteriology.** Pursuing an LBP track meaningfully would require recruiting collaborators with anaerobic-bacterium genetic engineering experience (Sonnenburg-lab alumni, Synlogic alumni, NextBiotix alumni, etc.). This is a known gap, not a fatal one.
- **The home-fermentation thesis is genuinely incompatible with this chassis.** Pursuing the LBP track is an explicit acceptance that not every Open Enzyme output will be home-fermentable. The mission ("solve gout, every avenue") supersedes the chassis ("home-fermentable food-grade strains") — that reframe is what makes this page possible. If that reframe is rejected at the platform level, this page should be retired.

---

## Cross-References

- [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) — the source matrix; this page is the deep-dive of the "Engineered LBPs" row
- [`koji-endgame-strain.md`](./koji-endgame-strain.md) — the koji-chassis peer track; both serve the broader mission
- [`abcg2-modulators.md`](./abcg2-modulators.md) — butyrate dual-action mechanism, Q141K rescue, PPARγ pathway
- [`open-questions.md`](./open-questions.md) — meta-index where the Phase 2 follow-ups are also tracked
- [`computational-experiments.md`](./computational-experiments.md) — comp-008 (Phase 2 P2-4) is queued in the Planned Analyses table
- [`open-enzyme-vision.md`](./open-enzyme-vision.md) — platform mission framing; the Phase 3 reflection note lives here
- [`food-grade-hdaci-screen-computational.md`](./food-grade-hdaci-screen-computational.md) — comp-007; validated butyrate's HDAC isoform profile
- [`daf-cd55-protease-stability-computational.md`](./daf-cd55-protease-stability-computational.md) — comp-006; the koji chassis HIGH-risk verdict for soluble complement regulators is one of the structural arguments for an LBP-chassis alternative
- [`hypotheses/H02-engineered-lbp-thesis.md`](./hypotheses/H02-engineered-lbp-thesis.md) — falsification card stub
- [`synthesis.md`](./synthesis.md) 2026-05-05 Open Question #3 — the originating action
