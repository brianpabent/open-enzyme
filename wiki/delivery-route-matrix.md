---
title: "Delivery Route × Compound Class Matrix — Exploration Surface"
date: 2026-05-15
tags:
  - delivery-routes
  - formulation
  - platform-strategy
  - multi-modal
  - first-principles
  - exploration
related:
  - modality-chokepoint-matrix.md
  - gout-kill-chain-delivery-routes.md
  - chassis-pending-interventions.md
  - compounding-pharmacy-track.md
  - engineered-koji-protocol.md
  - aspergillus-oryzae.md
  - uricase.md
  - bpc-157.md
  - peptide-gout-addendum.md
  - gout-clinical-pipeline.md
  - gsdmd-pore-delivery-paradox.md
  - purine-degrading-bacteria.md
  - etc/open-enzyme-vision.md
  - etc/open-source-platform.md
sources:
  - "2026-05-15 conversation: 'are we exploring all available delivery mechanisms, or do we have blinders because of the oral koji chassis?'"
  - "Existing wiki coverage: uricase.md §Hydrogen Peroxide Byproduct; engineered-koji-protocol.md §The Hydrogen Peroxide Question; aspergillus-oryzae.md §Hydrogen Peroxide Byproduct Management; bpc-157.md §Delivery Routes; peptide-gout-addendum.md §Delivery Routes and Bioavailability; compounding-pharmacy-track.md"
  - "Schiavon, Veronese et al. uricase-catalase fusion / co-encapsulation literature (early 2000s)"
  - "SEL-212 (Selecta Biosciences) pegadricase + ImmTOR PLGA-rapamycin tolerogenic-NP co-administration; Sands 2022 Nat Commun PMID 35022448"
status: published
---

# Delivery Route × Compound Class Matrix — Exploration Surface

## Why this page exists

[`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) is anchored on the **target** axis — where in the body each modality acts. That page surfaces "what mechanisms haven't we considered." It does not surface a different, equally load-bearing question: **for each compound class we already have a candidate for, have we explored all available delivery routes?**

The risk this page exists to mitigate is path-dependent narrowing of the **delivery** search space. The Open Enzyme chassis (engineered koji + S. boulardii + LBPs) is intrinsically oral. The platform's most-developed compound (uricase) inherits that route by default. The 503A/503B compounding pharmacy peer track ([`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md)) opens the small-molecule formulation surface, but its current emphasis is on oral repurposing. The peptide layer ([`bpc-157.md`](./bpc-157.md), [`peptide-gout-addendum.md`](./peptide-gout-addendum.md)) is the only compound class where multi-route coverage (SC, intranasal, oral, transdermal, intra-articular) is already a first-class question in the wiki.

Outside the peptide row, the platform mostly inherits "oral" as the assumed route and treats other routes as "those are pharma" — a frame that conflates the *chassis economics* (why we picked oral koji) with the *engineering layer's portability* (the strain produces protein that could in principle feed multiple downstream formulation formats).

This page is the orthogonal-to-modality view: **rows are compound classes**, **columns are delivery routes**, each cell answers "what's the route × class fit, what's currently in OE, what's open." The empty cells (🟡) are the genuine exploration vectors — most of them sit OFF the oral axis and have nothing to do with the chassis economics.

The framing question per cell, paralleling [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md): **"For this compound class delivered via this route, what gout-relevant problem could that combination open?"** — not "does this route fit the chassis?" The inversion is load-bearing.

## How to read this page

Same 6-symbol legend as the modality matrix:

| Symbol | Meaning |
|:-:|---|
| ✅ | OE has live coverage at this cell — see linked wiki page |
| 🧪 | OE has an in silico-validated, wet-lab-gated engineering candidate |
| 🔬 | OE has partial / mechanism-relevant coverage; specific intervention not yet engineered |
| 🟡 | Open exploration vector — combination could plausibly answer a stuck question; not currently in OE |
| ⚪ | Mechanistically possible but no realistic path / contraindicated / overkill / addressed by another route |
| — | Not applicable / mechanism doesn't intersect |

Cells marked 🟡 are where the most interesting nuggets live. The "Open exploration questions" section below pulls the highest-leverage 🟡 cells into a leverage-ordered queue.

---

## The matrix

Routes across the top, compound classes down the side. Routes are grouped by access compartment.

### Row 1: Enteral routes

| Compound class | Oral (whole-cell chassis) | Oral (free / formulated) | Sublingual / buccal | Rectal (colonic depot) |
|---|:-:|:-:|:-:|:-:|
| Small molecules / supplements | — | ✅ ([allopurinol / febuxostat / supplements](./supplements-stack.md); [BHB](./bhb-ketones.md), [oridonin](./oridonin.md), [colchicine](./colchicine.md)) | 🟡 (rapid-onset sublingual colchicine for flare-window kinetics; not in OE) | 🟡 (allopurinol/colchicine suppositories exist in non-US markets; distal-colon ABCG2 proximity unexplored for OE) |
| Peptides | 🔬 (PepT1-transported tripeptides like [KPV](./kpv-peptide.md), [carnosine](./carnosine.md) — gut barrier targets only, systemic poor) | 🔬 (same — oral peptide bioavailability is route-by-PepT1-only) | 🔬 ([KPV troches](./peptide-gout-addendum.md) exist; variable absorption) | ⚪ |
| Recombinant proteins / enzymes (uricase, lactoferrin, catalase, DAF/CD55 ectodomain) | ✅ ([engineered koji uricase](./engineered-koji-protocol.md), [engineered yeast uricase](./engineered-yeast-uricase-proposal.md), [DAF SCR1-4 candidate](./daf-cd55-scr14-truncated-computational.md); **chassis solves H2O2 housekeeping in situ** — see §"Chassis-as-formulation" below) | 🔬 (purified rasburicase oral attempted — [ALLN-346 Phase 2a](./uricase.md) — gut-lumen sink; lacks the host-catalase co-localization; needs co-formulation) | ⚪ (MW too large for buccal mucosa absorption; gastric proteolysis on swallow) | 🟡 (distal-colon depot of free or encapsulated uricase — bypasses gastric proteolysis, lands at ABCG2-rich distal colon — unexplored for OE) |
| Live engineered organisms (yeast, koji, E. coli Nissle, LBPs) | ✅ ([engineered koji](./engineered-koji-protocol.md), [PULSE-style Nissle](./engineered-yeast-uricase-proposal.md), [engineered LBP chassis](./engineered-lbp-chassis.md)) | — (live organisms ARE the formulation) | ⚪ (rapid swallow, no colonization opportunity) | 🟡 (rectal LBP instillation enables obligate-anaerobe colonization that oral cannot; precedent: FMT enema, *F. prausnitzii* engineered colonization — relevant to [engineered-lbp-chassis.md](./engineered-lbp-chassis.md)) |
| Engineered NPs (PLGA, LNPs, liposomes, exosomes) | — | 🔬 (oral NP absorption efficiency low; M-cell uptake routes are research-active) | ⚪ | 🔬 (rectal NP suppositories for colonic delivery — research class) |
| RNA platforms (mRNA, siRNA, ASOs) | — | ⚪ (naked RNA degraded by gut) | ⚪ | ⚪ |

### Row 2: Parenteral systemic routes

| Compound class | Subcutaneous (SC) | Intravenous (IV) | Intramuscular (IM) | Intranasal |
|---|:-:|:-:|:-:|:-:|
| Small molecules / supplements | 🔬 (research-grade injectable colchicine, IV BHB infusion; uncommon for chronic gout) | 🔬 (IV colchicine historically — withdrawn; corticosteroids for acute flare) | ⚪ (uncommon for chronic small-molecule gout therapy) | 🟡 (nasal-absorbed small molecules give faster onset for acute flare; unexplored for gout-specific compounds) |
| Peptides | ✅ ([BPC-157 SC](./bpc-157.md), [KPV SC](./peptide-gout-addendum.md), [TB-500 SC](./peptide-gout-addendum.md), [GHK-Cu SC](./peptide-gout-addendum.md) — >80% bioavailability per [bpc-157.md §Delivery Routes](./bpc-157.md)) | 🔬 (less common for chronic peptide therapy — SC depot replaces; IV PPS is the exception per [peptide-gout-addendum.md](./peptide-gout-addendum.md)) | ⚪ (rare for the gout-relevant peptide stack) | ✅ ([BPC-157 intranasal](./bpc-157.md) — 30-50% bioavailability per [bpc-157.md §Delivery Routes](./bpc-157.md); [KPV intranasal](./peptide-gout-addendum.md) reported) |
| Recombinant proteins / enzymes | ⚪ (substrate access poor at depot, H2O2 generation in tissue without local catalase, immunogenicity — see §"Why SC uricase doesn't work" below) | ✅ ([rasburicase](./uricase.md), [pegloticase](./gout-clinical-pipeline.md), [SEL-212 / pegadricase + ImmTOR](./uricase.md) — clinically established; immunogenicity-ceilinged without tolerogenic adjuvant) | ⚪ (same H2O2 / substrate-access / immunogenicity issues as SC) | ⚪ (MW way above nasal mucosa absorption cutoff — uricase ~34 kDa subunits, nasal route limit ~1 kDa for efficient transit) |
| Live engineered organisms | ⚪ (septicemia risk — live organisms are not injectable) | ⚪ | ⚪ | 🟡 (nasal probiotics for upper-airway are a research class; gout-relevance via systemic dissemination unclear) |
| Engineered NPs (PLGA, LNPs, liposomes, exosomes) | 🟡 (SC PLGA depot for slow-release antigen/payload — research class; ImmTOR co-administration evaluated IV but SC adaptable) | ✅ ([SEL-212 pegadricase + ImmTOR](./uricase.md) — Phase 3 PEG-uricase + PLGA-rapamycin tolerogenic NP IV co-administration; [LNP-mRNA standard for systemic mRNA](./modality-chokepoint-matrix.md)) | 🔬 (vaccine standard — IM mRNA-LNP for COVID precedent) | 🔬 (intranasal LNP research class — flu vaccines, mucosal-immunity programs) |
| RNA platforms | ✅ ([GalNAc-siRNA SC](./sirna-urat1-modality.md) — inclisiran, patisiran approved for liver; **kidney-tropic siRNA conjugate SC is the highest-leverage cell in [modality-chokepoint-matrix.md §"Open exploration questions" #1](./modality-chokepoint-matrix.md)**) | ✅ (LNP-mRNA IV) | ✅ (mRNA vaccines) | 🟡 (intranasal mRNA vaccine research-active; pediatric flu mRNA programs; gout-relevance unclear) |

### Row 3: Local / regional routes

| Compound class | Intra-articular (joint cavity) | Inhaled (pulmonary) | Transdermal / topical | Intrathecal / CNS |
|---|:-:|:-:|:-:|:-:|
| Small molecules / supplements | ✅ ([corticosteroid intra-articular for acute gout flare](./colchicine.md) — clinical standard; colchicine intra-articular research-stage) | 🟡 (pulmonary absorption excellent for small molecules — dapansutrile / oridonin / MCC950 inhaled is unexplored; bypasses first-pass hepatic metabolism) | 🟡 (transdermal patches for chronic urate-lowering — improves adherence; not in clinical use for allopurinol/febuxostat) | ⚪ (overkill; no CNS gout indication) |
| Peptides | 🔬 ([BPC-157 intra-articular for joint repair](./bpc-157.md) — case reports, not formal protocol) | ⚪ (peptide pulmonary absorption variable; no gout-relevant programs) | 🔬 (compounded peptide creams for joint pain exist; protein-class skin penetration poor — most "transdermal" peptide claims are aspirational) | ⚪ |
| Recombinant proteins / enzymes | 🟡 (**intra-articular uricase ± co-formulated catalase for direct tophi dissolution at the affected joint — unexplored for the platform's lead enzyme; H2O2 issue is bounded locally and catalase co-formulation is established literature** — see §"Open exploration questions" #1 below) | ⚪ (pulmonary delivery of protein-class is possible — Afrezza insulin precedent — but uricase + H2O2 generation in lung tissue is contraindicated) | ⚪ (protein MW vastly exceeds skin penetration limit) | ⚪ |
| Live engineered organisms | ⚪ (septic arthritis risk) | ⚪ | ⚪ | ⚪ |
| Engineered NPs | 🟡 (joint-depot NPs with anti-inflammatory payload — research class; intra-articular PLGA-corticosteroid is in clinical use under different indications) | 🔬 (LNP pulmonary delivery for CF, asthma — research-active; gout-relevance via systemic absorption is open) | 🔬 (NP-loaded transdermal patches — research class for slow-release small molecules) | ⚪ |
| RNA platforms | 🟡 ([mRNA-IL-1RA pulse intra-articular for acute flare](./modality-chokepoint-matrix.md) — already a top exploration cell in modality matrix; transient expression matches flare window) | 🟡 (inhaled mRNA for CF, asthma is an active research class; gout-relevance unclear without a tissue-tropic lung target) | ⚪ | ⚪ |

---

## Per-row details

### Small molecules / supplements

**Current OE coverage is heavily oral.** Allopurinol, febuxostat, the [supplements stack](./supplements-stack.md), [BHB](./bhb-ketones.md), [oridonin](./oridonin.md), [EGCG](./egcg.md), [colchicine](./colchicine.md) — all assumed oral by default. Intra-articular corticosteroid for acute flare is the lone established non-oral standard.

**Underexplored cells worth naming:**

- **Inhaled small-molecule NLRP3 inhibitors.** Pulmonary surface area is ~70 m², absorption is rapid, first-pass hepatic metabolism is bypassed. Dapansutrile (Olatec) is in IV trials; inhaled would change cost and access. [MCC950](./oridonin.md) and [oridonin](./oridonin.md) are NLRP3-active small molecules — no inhaled formulation programs exist for any of them. (Mechanistic Extrapolation)
- **Transdermal patches for chronic urate-lowering.** Allopurinol and febuxostat are taken daily for life; adherence is a known clinical problem. Patch chemistry is mature for many small molecules at the appropriate logP / MW range. No clinical programs for urate-lowering transdermals. (Mechanistic Extrapolation)
- **Sublingual rapid-onset colchicine.** Gout flares often onset in hours and the swallowed-colchicine onset is part of why patients hesitate. Sublingual would be the fastest oral route, bypassing gastric transit. No clinical program. (Mechanistic Extrapolation)
- **Rectal allopurinol / colchicine.** Suppositories exist in some non-US markets; the route puts the active agent close to the distal-colon ABCG2-rich epithelium that does ~33% of gut urate excretion. Unexplored as a deliberate ABCG2-proximity strategy. (Mechanistic Extrapolation)

### Peptides

**Multi-route coverage is the strongest of any compound class in the wiki.** [`bpc-157.md`](./bpc-157.md) and [`peptide-gout-addendum.md`](./peptide-gout-addendum.md) document SC (>80% bioavailability, gold standard), intranasal (30-50%, convenient), oral (PepT1-routed for local gut effect), intra-articular (case reports for joint repair), and transdermal (creams, limited efficacy) for BPC-157, KPV, TB-500, GHK-Cu, and PPS.

The compounding pharmacy peer track ([`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md)) is the access path for most of these — research-grade peptides + 503A formulation. This is one of the platform's least-blinded compound classes.

**Genuinely open peptide cells:**
- Intra-articular BPC-157 / KPV as a formal protocol — case reports exist, no controlled studies. (Animal Model / case reports)
- Sublingual peptide formulations beyond the existing KPV troche — variable absorption is the gating issue. (In Vitro / mechanistic)

### Recombinant proteins / enzymes (the load-bearing class for OE)

This is where the blinder lives. The OE chassis produces uricase, lactoferrin, carnosine (peptide), [DAF/CD55 SCR1-4](./daf-cd55-scr14-truncated-computational.md) ectodomain via fermentation. Once produced, the question is: what format does the patient ingest?

**The current implicit answer is "oral whole-cell shio-koji / amazake / S. boulardii capsule."** That's the chassis economics talking. The engineering layer (the strain + the construct) is portable across formats — purified enzyme could in principle be IV, SC, intra-articular, rectal, or inhaled.

**Why the non-oral routes have been deprioritized — honestly:**

- **IV:** Already the clinical state of art ([rasburicase](./uricase.md), [pegloticase](./gout-clinical-pipeline.md), [SEL-212](./uricase.md)). The immunogenicity ceiling (~60% ADA rate for non-PEGylated, PEGylation cuts it but doesn't eliminate, [ImmTOR co-administration](./uricase.md) solves it per Sands 2022 PMID 35022448). OE's value-add against the IV path is the chassis economics — same drug, $5-40K/dose IV vs cents/dose oral koji. Not the engineering, the formulation economics.
- **SC:** Substrate access is poor at the depot (urate is a plasma analyte, interstitial concentration tracks plasma but the depot has limited diffusion exchange); H2O2 byproduct accumulates in tissue without endogenous catalase to clear; immunogenicity is identical to IV. See §"Why SC uricase doesn't work" below.
- **Intra-articular:** Genuinely unexplored. Tophi-bearing joints have local urate concentrated as monosodium urate crystals; uricase activity at the joint cavity could in principle dissolve crystals directly, analogous to how steroid intra-articular addresses local inflammation. H2O2 issue is bounded locally and catalase co-formulation is established (Schiavon, Veronese et al. early 2000s; PEG-uricase + PEG-catalase, uricase-catalase fusion proteins). See §"Open exploration questions" #1 below.
- **Rectal:** Distal-colon depot bypasses gastric proteolysis and puts the enzyme adjacent to the ABCG2-rich epithelium that does the bulk of gut urate excretion. Same chassis logic as oral koji but with shorter transit and no gastric-survival pressure on the construct. Unexplored. (Mechanistic Extrapolation)
- **Intranasal, inhaled:** Uricase tetramer is ~134 kDa (4 × ~34 kDa subunits — see [`uricase.md`](./uricase.md)), far above the nasal mucosa absorption cutoff (~1 kDa for efficient transit). Pulmonary tissue could absorb the protein but H2O2 generation in alveolar tissue is contraindicated. (Mechanistic Extrapolation)
- **Transdermal, sublingual:** Protein MW vastly exceeds skin / buccal mucosa penetration limits. (Mechanistic Extrapolation)

### Live engineered organisms

The chassis path. Constrained to enteral (oral whole-cell, rectal LBP instillation) and intranasal (research-stage upper-airway probiotic class). All injectable / parenteral routes are contraindicated by septicemia / septic-arthritis risk. The matrix here is naturally sparse — and that's not a blinder, it's a structural property of live-organism delivery.

**Genuinely open cell:** rectal LBP instillation for obligate-anaerobe colonization. *F. prausnitzii*, *Akkermansia muciniphila*, and *Bacteroides* species are strict anaerobes that struggle with oral transit through the stomach and proximal small bowel (oxygen-rich, acidic). Rectal instillation puts them in the right compartment (anaerobic distal colon) immediately. FMT enema is the clinical precedent. Engineered colonic-tropic LBPs via rectal instillation is mechanistically the cleanest delivery for that chassis class — relevant to [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) but not yet surfaced there as a route question. (Mechanistic Extrapolation)

### Engineered NPs (PLGA, LNPs, liposomes, exosomes)

NPs sit at the intersection of formulation and delivery — they're not a compound class on their own, they're an *encapsulation layer* that travels with another payload (small molecule, protein, RNA). For OE's purposes, the cells that matter:

- **IV PLGA + payload:** SEL-212 is the canonical proof — pegadricase + ImmTOR PLGA-rapamycin tolerogenic NP, Phase 3 in refractory gout. Solves the immunogenicity ceiling for systemic uricase. The OE-relevant question is whether an **open-source equivalent** (open-source PEG-uricase strain + published tolerogenic-NP recipe + open dose-finding data) is buildable. See §"Open exploration questions" #6.
- **SC PLGA depot:** Research class for slow-release antigen/payload delivery. ImmTOR was evaluated IV in SEL-212 but the PLGA depot concept is portable to SC.
- **Intra-articular NP depot:** Research class. PLGA-corticosteroid depots are in clinical use under different indications. NP-delivered uricase ± catalase ± rapamycin (tolerance) at the joint is an open thought experiment.

### RNA platforms (mRNA, siRNA, ASOs)

Already extensively treated in [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md). Delivery-route-specific notes here:

- **Kidney-tropic SC siRNA against URAT1** is the #1 cell in the modality matrix's exploration queue. SC route mirrors the inclisiran / patisiran GalNAc-conjugate precedent. See [`sirna-urat1-modality.md`](./sirna-urat1-modality.md).
- **Intra-articular mRNA-IL-1RA** for acute flare termination is also already in the modality matrix queue. Transient expression matches the flare window.
- **Inhaled mRNA** is an active research class for CF / asthma; gout-relevance via systemic absorption is unclear without a specific tissue-tropic lung target.

---

## Chassis-as-formulation — the silent advantage of oral whole-cell delivery for protein enzymes

The wiki has documented the H2O2 byproduct of uricase activity in three places — [`uricase.md` §"Hydrogen Peroxide Byproduct"](./uricase.md), [`engineered-koji-protocol.md` §"The Hydrogen Peroxide Question"](./engineered-koji-protocol.md), and [`aspergillus-oryzae.md` §"Hydrogen Peroxide Byproduct Management"](./aspergillus-oryzae.md) — each in a "byproduct safety reassurance" framing.

That framing under-states what's actually happening. **The whole-cell oral chassis is doing free formulation work for the H2O2 housekeeping problem.** Concretely:

- Uricase catalyzes: urate + O2 + H2O → 5-hydroxyisourate + **H2O2** (1:1 stoichiometry; source: [`engineered-koji-protocol.md:86`](./engineered-koji-protocol.md))
- *A. oryzae* expresses catalase as part of normal aerobic peroxisomal metabolism (catA, catR among others; multiple homologs in the genome). Catalase converts 2 H2O2 → 2 H2O + O2, kcat ~10^7 s⁻¹, near the diffusion limit — one of the most efficient enzymes in biology. (Mechanistic Extrapolation from established A. oryzae biology)
- *A. flavus* uricase has a C-terminal PTS1 (SKL) peroxisomal targeting signal; native uricase is peroxisomal. If retained in the engineered construct, uricase and catalase are **co-localized in the same organelle** — H2O2 is intercepted within the peroxisome, never reaching the cytoplasm. (Mechanistic Extrapolation; the PTS1 targeting biology is established but compartmental H2O2 flux in the engineered strain has not been directly measured)
- Even with PTS1 removed (the engineered koji-protocol asks the question — see [`engineered-koji-protocol.md`](./engineered-koji-protocol.md):101), cytoplasmic catalase still buffers H2O2 before secretion.
- The patient ingests **a whole cell containing both the engineered uricase and the host catalase**. H2O2 housekeeping is solved before the protein leaves the chassis.

This is a positive argument for whole-cell oral delivery, not just a safety reassurance. Any **non-whole-cell** delivery format (purified IV uricase, SC depot uricase, intra-articular uricase, free oral rasburicase ALLN-346-style) loses this co-localized catalase and has to **either**:

1. Pre-clear H2O2 via the host's circulating catalase (works for IV — endogenous catalase in RBCs and tissue clears systemic H2O2; this is part of why pegloticase / SEL-212 IV is biochemically clean), OR
2. **Co-formulate catalase explicitly** (the Schiavon / Veronese uricase-catalase fusion approach, or NP co-encapsulation of both enzymes — established literature class, not in clinical use for uricase therapy currently).

**Implication for OE platform thesis:** the whole-cell oral chassis is doing more than chassis-economics work. It's solving a real biochemistry problem (H2O2 housekeeping for an oxidase enzyme) that **every alternative format has to re-solve through formulation engineering.** This is a non-obvious advantage that doesn't show up when the comparison is framed as "oral koji vs IV rasburicase" on cost alone. The catalase co-localization is *intrinsic* to the chassis and *acquired* to any other format.

It is also a *transferable* concept: any oxidase or peroxidase-byproduct-generating enzyme considered for OE production (D-amino acid oxidase, monoamine oxidases, etc.) would inherit the same co-localized catalase housekeeping if expressed in the same chassis. The chassis is generic; the housekeeping is generic.

---

## Why SC uricase doesn't work (even with catalase co-formulation, even with tolerogenic NP)

A 2026-05-15 conversation surfaced the obvious-to-ask-but-not-obvious-to-answer question: could uricase be delivered SC? Brief answer: no, for layered reasons that compound and that are not solved by adding components.

1. **Substrate access at the depot is poor.** Urate is a plasma analyte (~5-7 mg/dL in normals, 8-10+ in hyperuricemics — see [`gout-pathophysiology.md`](./gout-pathophysiology.md)). Interstitial fluid urate roughly tracks plasma. A SC depot is in interstitial space — bathed in interstitial fluid with normal urate concentration but no continuous flux delivery the way circulating blood delivers urate to an IV-circulating enzyme. The enzyme either sits in the depot with limited substrate exchange (slow local degradation, minimal systemic effect) or gets absorbed into circulation over days (essentially becomes a slow-release IV — the depot is doing PK work but the substrate-access advantage of IV is what makes IV work in the first place).
2. **H2O2 byproduct accumulates in tissue without local catalase.** Per §"Chassis-as-formulation" above. Endogenous catalase is abundant in circulation (RBCs, liver) but sparse in subcutaneous interstitial space. Whatever H2O2 uricase generates at the depot oxidizes nearby tissue before circulating catalase clears it. Co-formulated catalase helps but doesn't fully solve — H2O2 diffuses faster (small, uncharged, crosses membranes) than catalase (240 kDa tetramer) can scavenge it spatially. A uricase-catalase fusion (Schiavon class) tightens the spatial coupling but doesn't change the fundamental substrate-access problem in #1.
3. **Immunogenicity is identical to IV.** SC depot of foreign protein triggers ADAs in the same dose range as IV. PEGylation reduces but doesn't eliminate (pegloticase is ~60% ADA over a course). The SEL-212 / ImmTOR PLGA-rapamycin co-administration approach addresses immunogenicity but doesn't address #1 or #2.
4. **H2O2 issue persists with co-formulated catalase to a degree that depends on spatial coupling.** See §"Open exploration questions" #7 below — fusion protein engineering tightens the coupling and may unlock some non-IV protein-delivery formats. Not a free unlock.

**Net:** the right route for systemic uricase is IV, where (a) substrate access is maximal, (b) endogenous catalase is abundant, (c) PEGylation + ImmTOR solves immunogenicity (SEL-212 Phase 3 proof). SC is not just "harder to make work" — it's the wrong route for the biochemistry. The right routes for OE's chassis are (a) oral whole-cell (chassis solves H2O2, substrate is gut-luminal urate which DOES exchange with plasma via ABCG2-mediated secretion) and (b) the unexplored intra-articular and rectal cells described in §"Open exploration questions."

The general principle: **before assuming a delivery route is "blocked on engineering," check whether the route is the wrong route for the biochemistry.** Most of the time it's the latter.

---

## Open exploration questions surfaced by the matrix

Ordered by leverage (highest-leverage first; "leverage" = how much an underexplored cell could open if pursued).

1. **Intra-articular uricase ± co-formulated catalase for direct tophi dissolution at the affected joint.** Bypasses the systemic immunogenicity issue (locally bounded immune exposure), bypasses the substrate-access issue at SC depot (tophi ARE locally concentrated urate, ~100× plasma concentration in the crystal phase), bypasses the H2O2-in-tissue issue with co-formulated catalase or uricase-catalase fusion (Schiavon class literature precedent, early 2000s). Clinical analog: intra-articular corticosteroid for acute gout flare. Zero programs for intra-articular uricase. The matrix's highest-leverage 🟡 cell for the platform's lead enzyme. (Mechanistic Extrapolation)
2. **Rectal depot of engineered uricase formulations for distal-colon ABCG2 proximity.** ~33% of gut urate excretion is via the ABCG2-rich distal-colon epithelium ([`abcg2-modulators.md`](./abcg2-modulators.md), [`gut-lumen-sink.md`](./gut-lumen-sink.md)). Oral chassis has to survive gastric transit, navigate the small bowel, and arrive at the distal colon with enough remaining activity. Rectal delivery puts the enzyme at the target tissue with minutes of transit and no gastric pressure. Format options span the chassis spectrum: live-organism rectal (engineered LBP enema), purified-enzyme suppository (catalase co-formulated), or NP-encapsulated slow-release. Zero programs for rectal uricase or rectal engineered LBPs in gout. (Mechanistic Extrapolation)
3. **Inhaled small-molecule NLRP3 inhibitors (dapansutrile / oridonin / MCC950).** Pulmonary surface area (~70 m²) gives rapid systemic absorption with first-pass hepatic metabolism bypass. Dapansutrile is in IV trials (Olatec); inhaled would change cost and access (handheld inhaler vs IV infusion). Mechanism is identical across routes; the change is formulation engineering. (Mechanistic Extrapolation)
4. **Transdermal patches for chronic urate-lowering (allopurinol, febuxostat).** Daily oral dosing has known adherence drop-off; weekly patch would change the kinetics of compliance. Patch chemistry is mature for many small molecules; the gating questions are skin-flux rate at the required steady-state plasma concentration and skin-irritation profile. No clinical programs. (Mechanistic Extrapolation)
5. **Sublingual rapid-onset colchicine or IL-1RA-equivalent peptide for acute flare onset.** Flare onset is often within hours, the swallowed-colchicine onset adds hours more. Sublingual is the fastest oral route. (Mechanistic Extrapolation)
6. **Open-source SEL-212-equivalent.** Engineered PEG-uricase strain (already on platform trajectory) + open-source PLGA-rapamycin tolerogenic NP recipe with published characterization protocol + open dose-finding data. SEL-212's IP is primarily the formulation and the co-administration regimen, not the underlying biology. Tolerogenic-NP immunology is established (Selecta Biosciences PMID 35022448 and follow-on literature). Dose-finding is the gating empirical loop — would need a clinical partner or CRO. Extends the OE engineering layer downstream into systemic delivery. (Clinical Trial precedent + Mechanistic Extrapolation for the open-source version)
7. **Catalase + uricase fusion proteins as a chassis-portable H2O2 housekeeping solution.** Schiavon / Veronese early-2000s precedent for chimeric uricase-catalase. Solves the H2O2 housekeeping problem independent of delivery route — fusion protein could in principle feed SC, intra-articular, rectal, IV-without-host-catalase-dependence formats. Open-source fusion construct + comp-NNN protease-stability check for shio-koji conditions (same framework as [`daf-cd55-scr14-truncated-computational.md`](./daf-cd55-scr14-truncated-computational.md)) would be a tractable platform extension. Note: does NOT solve the substrate-access issue at SC depot (#1 above), so doesn't unlock SC uricase by itself. (Mechanistic Extrapolation; Schiavon literature is In Vitro)
8. **Pulmonary mRNA-IL-1RA for acute flare termination.** Fastest onset of any IL-1RA-equivalent — lung surface area maximizes mRNA-LNP uptake and translation. Research-active for other indications (CF, asthma). Gout-relevance is mechanistically defensible but no programs exist. Lower priority than intra-articular mRNA-IL-1RA (already in modality matrix) because intra-articular puts the IL-1RA directly at the inflamed joint. (Mechanistic Extrapolation)

---

## Cross-references

- [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) — companion page, complementary axis (target × modality vs route × class)
- [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) — the 503A/503B formulation delivery layer for repurposed small molecules
- [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) — chassis-as-formulation H2O2 housekeeping precedent
- [`aspergillus-oryzae.md`](./aspergillus-oryzae.md) — host catalase biology
- [`uricase.md`](./uricase.md) — peroxisomal targeting, IV uricase clinical landscape (rasburicase, pegloticase, SEL-212)
- [`bpc-157.md`](./bpc-157.md), [`peptide-gout-addendum.md`](./peptide-gout-addendum.md) — the peptide multi-route precedent
- [`gout-clinical-pipeline.md`](./gout-clinical-pipeline.md) — IV uricase pipeline state
- [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) — kidney-tropic SC siRNA conjugate
- [`open-questions.md`](./open-questions.md) — meta-index; matrix exploration questions should propagate as named open questions when the sweep daemon reads this page

## Maintenance

- **When a new delivery technology lands** (new conjugate chemistry, new NP platform, new oral protein-delivery breakthrough): add it as a column or note in the relevant existing column; ask the framing question per cell.
- **When OE adds a new compound class** (e.g., terpenoid discovery via the medicinal-mushroom track): add it as a row; mark which routes are mechanistically applicable.
- **When OE makes a build commitment on a non-oral cell:** mark the cell ✅ or 🧪 and link to the canonical wiki page; the matrix becomes the index.
- **The matrix is a meta-tool for exploration, not a roadmap.** A 🟡 cell is an unexplored vector, not a committed program. A ⚪ cell may flip when a new technology lands.

### Origin

This page exists because of a 2026-05-15 conversation that explicitly asked: "are we exploring all available delivery mechanisms, regardless of how we get the compounds — or do we have blinders because the koji chassis is oral?" The answer surfaced in that conversation was: peptides are well-explored, uricase has IV named but treated as "pharma's lane," everything else has inherited oral by default. The matrix is the navigable view of that answer.
