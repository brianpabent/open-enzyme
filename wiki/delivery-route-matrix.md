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
  - "Existing wiki coverage: uricase.md §Hydrogen-peroxide gate; engineered-koji-protocol.md §08 Peroxide and Safety Boundary; aspergillus-oryzae.md §Reaction-site peroxide; bpc-157.md §Delivery Routes; peptide-gout-addendum.md §Delivery Routes and Bioavailability; compounding-pharmacy-track.md"
  - "Schiavon, Veronese et al. uricase-catalase fusion / co-encapsulation literature (early 2000s)"
  - "SEL-212 (Selecta Biosciences) pegadricase + ImmTOR PLGA-rapamycin tolerogenic-NP co-administration; Sands 2022 Nat Commun PMID 35022448"
status: published
---

# Delivery Route × Compound Class Matrix — Exploration Surface

## Research question

[`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) is anchored on the **target** axis — where in the body each modality acts. That page surfaces "what mechanisms haven't we considered." It does not surface a different, equally load-bearing question: **for each compound class we already have a candidate for, have we explored all available delivery routes?**

This matrix tests the **delivery** search space for path-dependent narrowing. Several developed tracks (engineered koji, *S. boulardii*, and LBPs) are intrinsically oral, so route choice can be inherited without being challenged. The 503A/503B compounding-pharmacy track ([`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md)) opens the small-molecule formulation surface, although its current emphasis is oral repurposing. The peptide layer ([`bpc-157.md`](./bpc-157.md), [`peptide-gout-addendum.md`](./peptide-gout-addendum.md)) is the only compound class where multi-route coverage (SC, intranasal, oral, transdermal, intra-articular) is already a first-class question in the wiki.

Outside the peptide row, the platform mostly inherits "oral" as the assumed route and treats other routes as "those are pharma" — a frame that conflates the *chassis economics* (why we picked oral koji) with the *engineering layer's portability* (the strain produces protein that could in principle feed multiple downstream formulation formats).

The orthogonal-to-modality view uses **compound classes as rows** and **delivery routes as columns**. Each cell asks what the route × class fit is, what evidence exists, and what remains open. The empty cells (🟡) are exploration vectors; most sit off the oral axis and do not depend on chassis economics.

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
| Recombinant proteins / enzymes (uricase, lactoferrin, catalase, DAF/CD55 ectodomain) | 🔬 ([engineered koji uricase](./engineered-koji-protocol.md), [engineered yeast uricase](./engineered-yeast-uricase-proposal.md), [DAF SCR1-4 candidate](./daf-cd55-scr14-truncated-computational.md); intracellular topology offers a co-localization hypothesis, but reaction-site UOX, catalase, oxygen, substrate, and H₂O₂ remain unmeasured) | 🔬 (purified oral uricase precedent: [ALLN-346](./uricase.md); formulation-specific survival and peroxide control required) | ⚪ (MW too large for buccal mucosa absorption; gastric proteolysis on swallow) | 🟡 (distal-colon depot of free or encapsulated uricase — bypasses gastric proteolysis, lands near an intestinal urate-excretion compartment — unexplored for OE) |
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
| Recombinant proteins / enzymes | 🟡 (**intra-articular UOX ± catalase is an unvalidated local-reaction hypothesis; substrate access, peroxide control, tissue safety, persistence, and immunogenicity remain open** — see §"Open exploration questions" #1 below) | ⚪ (pulmonary UOX lacks a demonstrated peroxide-safety and delivery path) | ⚪ (protein MW vastly exceeds passive skin penetration) | ⚪ |
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

The route remains an explicit comparison among whole-cell, purified-enzyme, local, and systemic configurations. The engineering layer may be portable across formats, but each route changes purification, formulation, substrate access, peroxide handling, safety, and manufacturing requirements.

**Why the non-oral routes remain constrained:**

- **IV:** Established clinical uricase precedents include [rasburicase](./uricase.md) and [pegloticase](./gout-clinical-pipeline.md), but immunogenicity, monitoring, and formulation remain route constraints. Current evidence does not establish the oral-koji dose, production yield, release standard, or comparative cost, so no per-dose economic advantage can be assigned.
- **SC:** Substrate access is poor at the depot (urate is a plasma analyte, interstitial concentration tracks plasma but the depot has limited diffusion exchange); H2O2 byproduct accumulates in tissue without endogenous catalase to clear; immunogenicity is identical to IV. See §"Why SC uricase doesn't work" below.
- **Intra-articular:** Gout-specific use remains untested. UOX could in principle act near an intra-articular MSU deposit, but local injection does not establish that peroxide exposure is spatially bounded or safe. Catalase-containing constructs provide a design precedent, not a validated joint formulation. Any candidate must measure UOX and catalase activity and stoichiometry, their spatial coupling to substrate, peroxide time course and local exposure, crystal dissolution, and tissue safety before this route can advance. See §"Open exploration questions" #1 below. (**Mechanistic Extrapolation**.)
- **Rectal:** Distal-colon depot bypasses gastric proteolysis and puts the enzyme adjacent to the ABCG2-rich epithelium that does the bulk of gut urate excretion. Same chassis logic as oral koji but with shorter transit and no gastric-survival pressure on the construct. Unexplored. (Mechanistic Extrapolation)
- **Intranasal, inhaled:** Uricase tetramer is ~134 kDa (4 × ~34 kDa subunits — see [`uricase.md`](./uricase.md)), far above the nasal mucosa absorption cutoff (~1 kDa for efficient transit). Pulmonary tissue could absorb the protein but H2O2 generation in alveolar tissue is contraindicated. (Mechanistic Extrapolation)
- **Transdermal, sublingual:** Protein MW vastly exceeds skin / buccal mucosa penetration limits. (Mechanistic Extrapolation)

### Live engineered organisms

The chassis path. Constrained to enteral (oral whole-cell, rectal LBP instillation) and intranasal (research-stage upper-airway probiotic class). All injectable / parenteral routes are contraindicated by septicemia / septic-arthritis risk. The matrix here is naturally sparse — and that's not a blinder, it's a structural property of live-organism delivery.

**Genuinely open cell:** rectal LBP instillation for obligate-anaerobe colonization. *F. prausnitzii*, *Akkermansia muciniphila*, and *Bacteroides* species are strict anaerobes that struggle with oral transit through the stomach and proximal small bowel (oxygen-rich, acidic). Rectal instillation puts them in the right compartment (anaerobic distal colon) immediately. FMT enema is the clinical precedent. Engineered colonic-tropic LBPs via rectal instillation is mechanistically the cleanest delivery for that chassis class — relevant to [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) but not yet surfaced there as a route question. (Mechanistic Extrapolation)

### Engineered NPs (PLGA, LNPs, liposomes, exosomes)

NPs sit at the intersection of formulation and delivery — they're not a compound class on their own, they're an *encapsulation layer* that travels with another payload (small molecule, protein, RNA). For OE's purposes, the cells that matter:

- **IV PLGA + payload:** SEL-212 is a clinical precedent for pegadricase plus an ImmTOR PLGA-rapamycin tolerogenic nanoparticle. It supports testing immune-tolerance strategies but does not remove product-specific efficacy, safety, manufacturing, dose, or regulatory gates. See §"Open exploration questions" #6.
- **SC PLGA depot:** Research class for slow-release antigen/payload delivery. ImmTOR was evaluated IV in SEL-212 but the PLGA depot concept is portable to SC.
- **Intra-articular NP depot:** Research class. PLGA-corticosteroid depots are in clinical use under different indications. NP-delivered uricase ± catalase ± rapamycin (tolerance) at the joint is an open thought experiment.

### RNA platforms (mRNA, siRNA, ASOs)

Already extensively treated in [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md). Delivery-route-specific notes here:

- **Kidney-tropic SC siRNA against URAT1** is the #1 cell in the modality matrix's exploration queue. SC route mirrors the inclisiran / patisiran GalNAc-conjugate precedent. See [`sirna-urat1-modality.md`](./sirna-urat1-modality.md).
- **Intra-articular mRNA-IL-1RA** for acute flare termination is also already in the modality matrix queue. Transient expression matches the flare window.
- **Inhaled mRNA** is an active research class for CF / asthma; gout-relevance via systemic absorption is unclear without a specific tissue-tropic lung target.

---

## Reaction-site peroxide gate

UOX generates H₂O₂ wherever catalysis occurs. A chassis that contains catalase is not sufficient evidence that peroxide is controlled: UOX, substrate, oxygen, and adequate scavenger capacity must overlap in the same reaction compartment for the relevant duration.

Test each topology directly:

- intracellular UOX: measure co-localized UOX and catalase activity, oxygen access, urate access, viability, and H₂O₂ inside and outside the cell;
- secreted or surface-displayed UOX: measure extracellular scavenger capacity and local H₂O₂;
- cell-free or tissue-depot UOX: measure formulation or tissue scavenger capacity, residence, diffusion, and injury markers.

[Comp-045](./uricase-topology-oxygen-peroxide-design-computational.md) supplies the topology comparison design, and [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) owns the measurement. [Comp-035](./intra-articular-uricase-h2o2-reaction-diffusion-computational.md) is a Phase-0 prior for a different compartment; its review explicitly leaves the wet-lab H₂O₂ gate open. Neither computation establishes a generally safe catalase ratio or a preferred route.

## Why SC uricase remains unresolved

Subcutaneous UOX has several coupled constraints that cannot be closed by a formulation analogy alone.

1. **Substrate access at the depot is poor.** Urate is a plasma analyte (~5-7 mg/dL in normals, 8-10+ in hyperuricemics — see [`gout-pathophysiology.md`](./gout-pathophysiology.md)). Interstitial fluid urate roughly tracks plasma. A SC depot is in interstitial space — bathed in interstitial fluid with normal urate concentration but no continuous flux delivery the way circulating blood delivers urate to an IV-circulating enzyme. The enzyme either sits in the depot with limited substrate exchange (slow local degradation, minimal systemic effect) or gets absorbed into circulation over days (essentially becomes a slow-release IV — the depot is doing PK work but the substrate-access advantage of IV is what makes IV work in the first place).
2. **Peroxide control is unmeasured.** Per the reaction-site gate above, local UOX flux, catalase/scavenger capacity, diffusion, and tissue injury must be measured in the depot configuration. A fusion or co-formulation does not answer the substrate-access question in #1.
3. **Immunogenicity remains a systemic-protein risk.** Route, formulation, exposure duration, and immune-modulating components may change the response, but no SC configuration here has been validated.
4. **H2O2 issue persists with co-formulated catalase to a degree that depends on spatial coupling.** See §"Open exploration questions" #7 below — fusion protein engineering tightens the coupling and may unlock some non-IV protein-delivery formats. Not a free unlock.

**Current boundary:** SC UOX has unresolved substrate-exchange, peroxide, tissue-safety, persistence, and immunogenicity constraints. Oral whole-cell, intra-articular, rectal, and other routes remain separate hypotheses with route-specific gates; this page does not promote one from the comp-044 or comp-035 calculations.

The general principle: test substrate access, reaction coproduct control, exposure, and immune handling together before promoting or killing a route.

---

## Open exploration questions surfaced by the matrix

Ordered by leverage (highest-leverage first; "leverage" = how much an underexplored cell could open if pursued).

1. **Intra-articular UOX ± co-formulated catalase.** Local crystal access is a hypothesis, not a demonstrated escape from immunogenicity or peroxide injury. [Comp-035](./intra-articular-uricase-h2o2-reaction-diffusion-computational.md) supplies a non-decision-grade reaction-diffusion prior; its review leaves the Amplex Red and tissue-safety gates open. See [`chassis-pending-interventions.md` §6](./chassis-pending-interventions.md). (Mechanistic Extrapolation + Computational)
2. **Rectal depot of engineered uricase formulations for distal-colon ABCG2 proximity.** ~33% of gut urate excretion is via the ABCG2-rich distal-colon epithelium ([`abcg2-modulators.md`](./abcg2-modulators.md), [`gut-lumen-sink.md`](./gut-lumen-sink.md)). Oral chassis has to survive gastric transit, navigate the small bowel, and arrive at the distal colon with enough remaining activity. Rectal delivery puts the enzyme at the target tissue with minutes of transit and no gastric pressure. Format options span the chassis spectrum: live-organism rectal (engineered LBP enema), purified-enzyme suppository (catalase co-formulated), or NP-encapsulated slow-release. Zero programs for rectal uricase or rectal engineered LBPs in gout. (Mechanistic Extrapolation)
3. **Inhaled small-molecule NLRP3 inhibitors (dapansutrile / oridonin / MCC950).** Pulmonary surface area (~70 m²) gives rapid systemic absorption with first-pass hepatic metabolism bypass. Dapansutrile is in IV trials (Olatec); inhaled would change cost and access (handheld inhaler vs IV infusion). Mechanism is identical across routes; the change is formulation engineering. (Mechanistic Extrapolation)
4. **Transdermal patches for chronic urate-lowering (allopurinol, febuxostat).** Daily oral dosing has known adherence drop-off; weekly patch would change the kinetics of compliance. Patch chemistry is mature for many small molecules; the gating questions are skin-flux rate at the required steady-state plasma concentration and skin-irritation profile. No clinical programs. (Mechanistic Extrapolation)
5. **Sublingual rapid-onset colchicine or IL-1RA-equivalent peptide for acute flare onset.** Flare onset is often within hours, the swallowed-colchicine onset adds hours more. Sublingual is the fastest oral route. (Mechanistic Extrapolation)
6. **Open-source SEL-212-equivalent.** Engineered PEG-uricase strain (already on platform trajectory) + open-source PLGA-rapamycin tolerogenic NP recipe with published characterization protocol + open dose-finding data. SEL-212's IP is primarily the formulation and the co-administration regimen, not the underlying biology. Tolerogenic-NP immunology is established (Selecta Biosciences PMID 35022448 and follow-on literature). Dose-finding is the gating empirical loop — would need a clinical partner or CRO. Extends the OE engineering layer downstream into systemic delivery. (Clinical Trial precedent + Mechanistic Extrapolation for the open-source version)
7. **Catalase + UOX fusion proteins as a portable peroxide-control hypothesis.** A fusion could enforce proportional co-delivery, but still requires measured retained activity, local H₂O₂, substrate and oxygen access, tissue safety, and immunogenicity in each route. It does not unlock SC or any other route by itself. (Mechanistic Extrapolation)
8. **Pulmonary mRNA-IL-1RA for acute flare termination.** Fastest onset of any IL-1RA-equivalent — lung surface area maximizes mRNA-LNP uptake and translation. Research-active for other indications (CF, asthma). Gout-relevance is mechanistically defensible but no programs exist. Lower priority than intra-articular mRNA-IL-1RA (already in modality matrix) because intra-articular puts the IL-1RA directly at the inflamed joint. (Mechanistic Extrapolation)

---

## Cross-references

- [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) — companion page, complementary axis (target × modality vs route × class)
- [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) — the 503A/503B formulation delivery layer for repurposed small molecules
- [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) — intracellular, secreted, and cell-free peroxide-control questions
- [`aspergillus-oryzae.md`](./aspergillus-oryzae.md) — host catalase biology
- [`uricase.md`](./uricase.md) — peroxisomal targeting, IV uricase clinical landscape (rasburicase, pegloticase, SEL-212)
- [`bpc-157.md`](./bpc-157.md), [`peptide-gout-addendum.md`](./peptide-gout-addendum.md) — the peptide multi-route precedent
- [`gout-clinical-pipeline.md`](./gout-clinical-pipeline.md) — IV uricase pipeline state
- [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) — kidney-tropic SC siRNA conjugate
- [`open-questions.md`](./open-questions.md) — unresolved delivery questions
