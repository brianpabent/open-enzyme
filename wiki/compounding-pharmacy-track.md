---
title: "Compounding Pharmacy Track — Delivery Route for the Repurposing Surface"
date: 2026-05-11
tags:
  - delivery-route
  - peer-track
  - platform-strategy
  - repurposing-surface
  - small-molecules
  - 503a
  - 503b
  - regulatory
  - scope-page
  - first-principles
related:
  - open-enzyme-vision.md
  - open-source-platform.md
  - modality-chokepoint-matrix.md
  - engineered-koji-protocol.md
  - engineered-lbp-chassis.md
  - sirna-urat1-modality.md
  - medicinal-mushroom-complement-track.md
  - tcm-modern-rigor-intersection.md
  - disulfiram.md
  - oridonin.md
  - bhb-ketones.md
  - colchicine.md
  - purine-degrading-bacteria.md
  - chassis-pending-interventions.md
sources:
  - "Brian framing 2026-05-11 (from MINX/Veradermics screenshots): 'had not considered the compounding pharmacy angle. we should! we have identified lots of compounds and it might be easier to just make a pill than grow mold lol'"
  - "MINX precedent: 5 mg once-daily extended-release oral minoxidil developed via ChatGPT-aided formulation review + lipid-matrix design + 503A compounding pharmacy + dissolution testing; built in days, not the multi-year Veradermics trial track"
  - "FDA 503A (patient-specific) and 503B (outsourcing facility) compounding statutes — Drug Quality and Security Act of 2013"
status: scoped (Phase 1)
---

# Compounding Pharmacy Track — Delivery Route for the Repurposing Surface

## Why this page exists

Open Enzyme's two parallel outputs (per [`open-enzyme-vision.md`](./open-enzyme-vision.md) §1–2) are (1) a **discovery engine** for chokepoint-to-intervention mapping, and (2) an **open-source strain library** as one synthesis of that engine. The discovery engine produces, among other things, a **repurposing surface** — FDA-approved drugs that hit gout-relevant chokepoints but were never clinically tested for gout (canonical examples: [disulfiram](./disulfiram.md) at CP6b GSDMD, zileuton at CP6a 5-LOX, avacopan at CP0 C5aR1).

The wiki has historically treated that repurposing surface as **scientifically interesting but operationally orphaned**: we identify a drug-chokepoint match, write it up, and move on. There is no canonical Open Enzyme path from "FDA-approved drug X hits gout chokepoint Y at off-label dose Z" to "patient can actually take it." That gap is exactly what the compounding pharmacy track closes.

**The cleavage rule:** Open Enzyme's compound catalog splits cleanly along a delivery-route axis:

- **Proteins / enzymes / biologics** → fermentation chassis (engineered koji, yeast, LBPs). Uricase, lactoferrin, DAF/CD55, digestive enzymes (lipase/protease/amylase), engineered probiotics. Compounding pharmacies cannot make these.
- **Small molecules** → potentially compoundable, with sub-cleavage by 503A-eligibility category (see "How Section 503A actually works" below for the three-tier hierarchy):
  - Off-patent FDA-approved drugs with USP/NF monographs → **first-class compounding-pharmacy targets** (Tier 1 eligible, the easiest path; allopurinol, colchicine, probenecid sit here)
  - Off-patent FDA-approved drugs without USP/NF monograph but with an active FDA approval → **first-class compounding-pharmacy targets** via Tier 2 (component of FDA-approved drug); the MINX category sits here, as do disulfiram and zileuton
  - FDA-approved drugs that have been commercially withdrawn → **regulatory edge case** — Tier 2 status may or may not survive market withdrawal; needs per-compound verification (lesinurad is the canonical example)
  - Supplements (BHB, ergothioneine, quercetin, etc.) → typically already supplement-grade; compounding adds little value over OTC purchase
  - Research compounds with no FDA approval (MCC950, dapansutrile in some markets) → **not 503A-compoundable** unless they appear on the formal Tier 3 list, which they don't
  - Peptides (KPV, BPC-157) → compoundable but more constrained; KPV / BPC-157 / TB-500 / MOTs-C are under formal Tier-3 consideration at FDA's Pharmacy Compounding Advisory Committee (July 2026 meeting)

The MINX example sharpens the framing: 5 mg once-daily extended-release oral minoxidil was developed in days using literature + patent landscape review (ChatGPT-aided), a lipid-matrix release-control design, a 503A compounding pharmacy, and dissolution testing — not a multi-year FDA trial with patents and premium pricing. **The active ingredient was already familiar.** The work was formulation engineering, not drug discovery.

The OE equivalent: for the subset of compounds where the active is FDA-approved and the only barrier between the patient and a useful dose is "no one has commercialized this specific formulation," compounding is the delivery mechanism. The discovery engine's repurposing surface is the input. Compounding is the output side that turns identification into access.

This page formalizes the **compounding pharmacy track** as a peer track to the engineered-koji, engineered-LBP, siRNA, medicinal-mushroom-complement, and TCM tracks under the broader Open Enzyme platform thesis. Same posture: an exploration vector, not a commitment to abandon any other track.

## Platform thesis expansion

| Track | Chassis / mechanism | Engineering effort | Therapeutic class | Consumption UX | Regulatory path |
|---|---|---|---|---|---|
| **Engineered koji** ([protocol](./engineered-koji-protocol.md)) | *A. oryzae* recombinant cassette | Heavy — secretion engineering | Therapeutic enzymes (uricase, lactoferrin, DAF SCR1-4) | Shio-koji / amazake / miso (daily food) | GRAS-pathway; food, not drug |
| **Engineered LBPs** ([chassis](./engineered-lbp-chassis.md)) | *F. prausnitzii* / *Akkermansia* / Bacteroides | Heavy — anaerobe engineering | Live biotherapeutic (butyrate, IL-22, anti-complement) | Refrigerated capsule | FDA LBP path (commercial pharma) |
| **siRNA / kidney-tropic discovery** ([modality](./sirna-urat1-modality.md)) | Synthetic ASO/siRNA + conjugate | Heavy — sequence design, delivery chemistry | Sequence-specific knockdown (URAT1) | Subcutaneous injection | FDA NDA (commercial pharma) |
| **Medicinal mushroom complement** ([track](./medicinal-mushroom-complement-track.md)) | *G. lucidum*, *C. militaris*, *Pleurotus*, etc. | Light — strain selection + cultivation | Native-compound supplements (GLPP, cordycepin, ergothioneine) | Dried fruiting body / tincture / powder | GRAS food / supplement-grade |
| **TCM × modern rigor** ([intersection](./tcm-modern-rigor-intersection.md)) | Standardized multi-herb formulas | Light–medium — extract characterization | Standardized formula extracts (Si Miao San family, Smilax glabra) | Standardized extract capsule | Supplement-grade (US) / TCM-licensed (Asia) |
| ***Compounding pharmacy (THIS page)*** | 503A pharmacy (patient-specific) or 503B outsourcing facility (bulk) | **Minimal — formulation engineering only (release matrix, dose, dissolution profile). NO genetic engineering, NO drug discovery.** | Repurposed FDA-approved drugs at off-label dose / combination / release profile | Custom-formulated tablet, capsule, or troche dispensed against prescription | 503A (per-patient Rx) or 503B (registered outsourcing); off-label prescribing is physician's discretion |

The compounding pharmacy track is the **lowest engineering effort of any peer track and the fastest path from identification to patient access**, but it is also the most narrowly scoped — it only works for compounds where someone has already done the FDA-approval work (and the drug subsequently went off-patent or is being repurposed off-label).

## How Section 503A actually works (correction added 2026-05-15)

The wiki previously used "is this drug on the FDA 503A list?" as if the 503A list were a single flat lookup. **That's not how the statute works.** Per [21 CFR 216 + FDA's Section 503A guidance](https://www.fda.gov/drugs/human-drug-compounding/bulk-drug-substances-used-compounding-under-section-503a-fdc-act), a 503A compounding pharmacy may use bulk drug substances that fall into any one of three tiers, in priority order:

1. **Tier 1 — USP / NF monograph substances.** The substance is the subject of an applicable USP or NF monograph and compounded in compliance with USP <795>/<797>. Most of the well-established small-molecule drugs sit here — allopurinol, colchicine, probenecid all have long-standing USP monographs.
2. **Tier 2 — Components of FDA-approved drug products.** If no applicable USP/NF monograph exists, the bulk substance qualifies if it's an active component of an FDA-approved drug product (with a valid certificate of analysis from an FDA-registered facility). Disulfiram, zileuton, pentostatin sit here — all FDA-approved drugs, all eligible for 503A compounding via Tier 2 regardless of whether they have a current USP monograph.
3. **Tier 3 — The formal FDA 503A bulks list.** Substances that don't qualify under Tier 1 or Tier 2 can still be 503A-compoundable if FDA has placed them on the formal 503A bulks list. **The formal list is short** — only six substances as of 2026-05-15 (Brilliant Blue G, cantharidin, diphenylcyclopropenone, N-acetyl-D-glucosamine, squaric acid dibutyl ester, thymol iodide), all obscure topical compounds; none are gout-relevant. Peptide nominations (KPV, BPC-157, TB-500, MOTs-C) are under PCAC review for July 2026.

**Implications for the OE candidate list.** For all the compounds OE has identified as gout-chokepoint hits, the question is which tier they qualify under, not whether they appear on the formal Tier 3 list. The gating empirical questions are:

- **Tier 1 / Tier 2 confirmation per compound** — mostly trivial: every OE candidate except lesinurad is an FDA-approved drug, so Tier 2 applies at minimum. Most also have USP monographs (Tier 1).
- **Bulk API commercial supply** — a *supply-chain* question, not a regulatory one. Some FDA-approved drugs (notably pentostatin, which is parenteral and hospital-pharmacy-distributed) have bulk API that's hard to source for 503A pharmacies regardless of regulatory eligibility.
- **Post-withdrawal Tier 2 status** — for lesinurad (FDA-approved 2015, commercially withdrawn 2019), does Tier 2 eligibility survive market withdrawal? This is the only genuinely uncertain regulatory question in the OE candidate set.

The "bulk API audit" originally queued as Phase 2 §1 was scoped against a flat-list framing that doesn't match how 503A actually works. The audit's actual finding, captured here, is that 503A eligibility is structurally not the gating question for OE's discovery-engine outputs — supply availability and off-label prescribing infrastructure are.

## What goes on this track vs. the koji / fermentation track

### Discovery-engine repurposing candidates (compounding-pharmacy track, properly so called)

These are drugs NOT currently used for gout, identified by the OE discovery engine as hitting gout-relevant chokepoints. Compounding turns identification into patient access.

For each entry: chokepoint mapping, 503A-eligibility tier, evidence level for the gout / NLRP3 application, what a compounding formulation would actually look like.

**1. Disulfiram (Antabuse) — CP6b GSDMD inhibitor.**
- 503A eligibility: Tier 2 (component of FDA-approved drug). FDA-approved 1951 for alcohol-use disorder; off-patent; bulk API widely available from compounding-pharmacy suppliers.
- Gout-relevant evidence: **In vitro** — Hu et al. 2020 (*Nat Immunol*) — disulfiram directly inhibits gasdermin D pore formation, blocking IL-1β release downstream of NLRP3. No human gout trials.
- Compounding play: **Low-dose extended-release tablet** (current Antabuse is 250–500 mg immediate-release for alcohol deterrence; the NLRP3-relevant dose is unknown but likely lower). Compounded ER formulation at sub-deterrent doses would allow exploring the GSDMD-inhibitor effect without the alcohol-flush mechanism dominating. See [`disulfiram.md`](./disulfiram.md) for full mechanism and the "repurposing surface" framing.
- Evidence level for the application: **Mechanistic extrapolation + in vitro.** Wet-lab gate before patient use.

**2. Zileuton — CP6a 5-LOX inhibitor.**
- 503A eligibility: Tier 2 (component of FDA-approved drug Zyflo, 1996, asthma); off-patent. Bulk API availability is a supplier-side question, not a regulatory listing question — current Zyflo distribution is small enough that compounding-pharmacy supplier networks may not stock the API even though 503A eligibility is structurally clean.
- Gout-relevant evidence: **Mechanistic extrapolation + in vitro** — 5-LOX produces LTB4, a neutrophil chemoattractant active in gout flares. Zileuton blocks 5-LOX. No gout clinical trials.
- Compounding play: if a compounding supplier carries the bulk API, **low-dose ER zileuton for flare prophylaxis** is a clean repurposing experiment. Risk: zileuton has known hepatotoxicity signal in asthma cohorts; compounded use needs liver monitoring.
- Evidence level: **Mechanistic extrapolation.**

**3. Pentostatin (Nipent) — ADA inhibitor; whole-fermentate Cordyceps stabilization.**
- 503A eligibility: Tier 2 (component of FDA-approved drug Nipent; FDA-approved for hairy-cell leukemia, IV). Off-patent. **Bulk API supply is the real bottleneck** — Nipent is parenteral and hospital-pharmacy-distributed; 503A pharmacies don't typically carry it. Supplier-side verification needed before any prescription pathway opens. Oral bioavailability also unknown (Nipent is IV-only).
- Gout-relevant evidence: **Mechanistic extrapolation** — in C. militaris whole fermentate, pentostatin naturally inhibits ADA, extending cordycepin's half-life (Xia 2017, PMID 29056419, in vitro biochemistry). A compounded **micro-dose oral pentostatin + cordycepin combination** would replicate the natural Cordyceps pairing without the cultivation step.
- Compounding play: highly conditional on bulk API supply AND oral bioavailability. Probably **not first-line** compared to whole-fermentate Cordyceps from the medicinal-mushroom-complement track.
- Evidence level: **Mechanistic extrapolation** with significant pharmacokinetic unknowns.

**4. Lesinurad — URAT1 inhibitor (withdrawn but mechanism-relevant).**
- 503A eligibility: **Tier 2 survives the commercial withdrawal.** FDA-approved 2015 for combination with XOI (Zurampic, NDA 207988); **commercially withdrawn 2019** for *business* reasons, not safety/effectiveness. Per [21 CFR 216.24](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-216/subpart-B/section-216.24), the FDA "drug products withdrawn or removed from the market for reasons of safety or effectiveness" list is specifically scoped to safety/efficacy withdrawals; lesinurad is not on this list. Resolved 2026-05-15 via direct FDA-source check: a 503A pharmacy CAN compound lesinurad via Tier 2 (component of FDA-approved drug) provided they source bulk API from a registered supplier with a valid CoA. *Remaining gating question is supply-chain, not regulatory* — bulk API supply is uncertain because no commercial product means compounding-pharmacy suppliers don't typically stock it.
- State-board caveat: some state boards of pharmacy may apply additional conservatism to commercially-withdrawn drugs even when 21 CFR 216.24 doesn't apply. Per-state precedent search would be the next-step verification if a prescription pathway opens.
- Gout-relevant evidence: **Clinical Trial** — efficacy established before withdrawal.
- Compounding play: depends on bulk API sourcing and per-state precedent. Could be revived as a compounded formulation if a 503B outsourcing facility sourced it. Defer to probenecid as the URAT1 stand-in for now, but **lesinurad is no longer an OE candidate with structurally-uncertain regulatory status** — it's the same supply-chain question that applies to zileuton and pentostatin.
- Evidence level: **Clinical Trial** (for the withdrawn product); 503A pathway clean per FDA's own framework.

### Established gout drugs (custom-dose / custom-formulation track)

These drugs are already first-line gout therapy. The compounding play is **custom-dose / custom-formulation**, not discovery — the clinical question is whether a custom formulation adds value over the commercial product, not whether the mechanism is novel.

**5. Allopurinol — XO inhibition (custom doses + combinations).**
- 503A eligibility: Tier 1 (USP monograph) + Tier 2 (FDA-approved 1966); off-patent; bulk API widely available from compounding-pharmacy suppliers. **No regulatory uncertainty.**
- Gout-relevant evidence: **Clinical Trial** — first-line urate-lowering therapy.
- Compounding play: **Pediatric / weight-based custom doses** (commercial tablets are 100/300 mg only — patients needing 50 mg or 75 mg are stuck splitting); **liquid suspensions** for swallow-impaired patients; **fixed-dose combinations** with low-dose colchicine for prophylaxis-bundled therapy.
- Evidence level: **Clinical Trial** for allopurinol itself; compounded forms inherit profile.

**6. Colchicine — CP6 prophylaxis.**
- 503A eligibility: Tier 1 (USP monograph) + Tier 2 (FDA-approved); bulk API widely available. The Colcrys (FDA-approved formulation) and unbranded generic both exist. **No regulatory uncertainty.**
- Gout-relevant evidence: **Clinical Trial** — extensively validated for acute flare prophylaxis at 0.6 mg/day.
- Compounding play: **Low-dose extended-release for chronic flare suppression**, or **fixed-dose combinations with allopurinol** for the patient who would otherwise carry two pill bottles. Commercial fixed-dose combos exist intermittently (Colcrys + allopurinol has been on/off market) — compounding fills the gap when commercial isn't available.
- Evidence level: **Clinical Trial** for colchicine itself; compounded reformulations would inherit the established safety/dose profile.
- See [`colchicine.md`](./colchicine.md).

**7. Probenecid — URAT1 inhibitor (custom doses + combinations).**
- 503A eligibility: Tier 1 (USP monograph) + Tier 2 (FDA-approved 1951); off-patent; bulk API widely available. **No regulatory uncertainty.**
- Gout-relevant evidence: **Clinical Trial** — uricosuric (renal excretion via URAT1 / OAT1 / OAT3 blockade).
- Compounding play: **Low-dose probenecid + allopurinol combinations** for patients who fail allopurinol monotherapy and where lesinurad is unavailable (lesinurad-allopurinol Duzallo was withdrawn 2019; probenecid is the mechanistic stand-in). **Extended-release probenecid** for QD dosing instead of BID/TID.
- Evidence level: **Clinical Trial** for probenecid itself.

### Off-label nutraceutical formulations (separate from both above)

**8. Off-label nutraceutical formulations.**
- Compounded **liposomal quercetin / luteolin** at higher doses than commercial supplements deliver, with documented bioavailability targeting. Several compounding pharmacies offer liposomal nutraceutical formulations.
- Compounded **BHB ester at therapeutic doses** in stable formulations (commercial BHB esters are typically diester salts; compounded monoester formulations have better PK).
- Evidence level: **Mechanistic extrapolation** from upstream NLRP3 / xanthine oxidase data.

### Stays with the koji / fermentation track (not compoundable)

- **Recombinant uricase** ([engineered-yeast-uricase-proposal.md](./engineered-yeast-uricase-proposal.md), [engineered-koji-protocol.md](./engineered-koji-protocol.md)) — biologic; can be made by 503B outsourcing facility theoretically but the only currently approved uricase is rasburicase (IV, hospital-only); oral compounded uricase is not a 503A pathway because the protein degrades in stomach.
- **Lactoferrin** ([lactoferrin.md](./lactoferrin.md)) — biologic; available as supplement-grade but engineered variants are koji-route.
- **DAF SCR1-4** ([daf-cd55-scr14-truncated-computational.md](./daf-cd55-scr14-truncated-computational.md)) — engineered protein.
- **Digestive enzymes (lipase / protease / amylase)** — Creon / Zenpep are FDA-approved pancrelipase preparations; compounding analog exists (compounded pancreatic enzymes) but the OE thesis is engineered koji as a fermentation-route alternative, not a compounding-route alternative.
- **Native koji products (kojic acid, ergothioneine, KPV peptide)** — fermentation-route is the OE thesis; compounding could deliver KPV but doesn't add over the koji approach.

### Combined / hybrid candidates

- **Compounded repurposing pill + engineered-koji daily food** as a layered intervention: e.g., compounded low-dose disulfiram ER for CP6b GSDMD blockade + daily shio-koji delivering uricase for CP0 substrate degradation. The two routes target non-overlapping chokepoints and consumption modes (Rx pill + daily food), so combination is mechanistically clean.

## 503A vs. 503B — regulatory mechanics (brief)

The Drug Quality and Security Act of 2013 created two distinct compounding pharmacy regulatory categories. Open Enzyme work in this space needs to be honest about which lane applies.

| | **503A** | **503B** |
|---|---|---|
| Statute | Section 503A of FDCA | Section 503B of FDCA (added 2013) |
| Who | Traditional compounding pharmacies | Outsourcing facilities (FDA-registered) |
| Trigger | Valid patient-specific prescription | Can compound without patient-specific Rx |
| Bulk API source | Must be on FDA 503A bulk drug substances list (or be a component of an FDA-approved drug) | Must be on FDA 503B bulk drug substances list |
| GMP | Not required at 503A level (state-board oversight) | Full cGMP compliance required |
| Distribution | Single patient at a time, in response to Rx | Can ship to hospitals/clinics in bulk |
| Best for | Custom doses, low-volume, individualized formulations | Repeated production of a stable repurposing formulation across many patients |

For OE: most identification → access work runs through 503A initially (individual patients getting compounded scripts for off-label gout indications). If a specific formulation gets traction and accumulates evidence, the path could later shift to a 503B outsourcing facility for higher-volume distribution, or further to a sponsored 505(b)(2) NDA if the formulation is novel enough to warrant FDA approval (the Veradermics path).

**The MINX precedent uses the 503A route** — patient-specific Rx, compounded against the formulation instructions, dissolution-tested as quality control. That's the template.

## Formulation engineering — what's actually involved

Compounding is not "buy bulk powder, press into pill." The real work is **release-profile engineering**: matching the dissolution kinetics to the desired plasma concentration curve, given the API's solubility, half-life, and absorption window.

Levers a compounding pharmacist can pull (drawing on the MINX-style protocol):

- **Lipid matrix tablets** — slow dissolution via hydrophobic matrix; lengthens absorption window for short-half-life drugs. (MINX's approach for minoxidil.)
- **HPMC / cellulose-ether matrices** — swellable hydrophilic matrix for sustained release.
- **Multi-particulate capsules** — beads with different release coatings inside one capsule for layered release profile.
- **Solid lipid nanoparticles (SLN) / liposomal formulations** — bioavailability enhancement for low-permeability APIs.
- **Enteric coatings** — protect acid-labile APIs through stomach (relevant for any compound that's degraded by gastric HCl).
- **Sublingual / buccal troches** — bypass first-pass for drugs with high hepatic metabolism.
- **Topical / transdermal** — relevant for systemic delivery of drugs with poor oral bioavailability.

The AI-aided literature + patent landscape review (the MINX innovation) collapses formulation design from a months-long pharma-industry workflow to a days-long workflow accessible to a small team. **This is the part of the track that scales with current AI tooling.**

The verification step (dissolution testing per USP <711>, content uniformity per USP <905>) is non-negotiable and runs at the compounding pharmacy or a contract analytical lab. **Without dissolution data, you don't know what you made.**

## Discovery-engine integration

The compounding pharmacy track is the natural delivery mechanism for OE's **repurposing surface** output. The discovery engine identifies FDA-approved drugs hitting gout-relevant chokepoints (see [`open-enzyme-vision.md`](./open-enzyme-vision.md) §2.2 for the canonical framing). The current repurposing surface contains:

- **Disulfiram** (CP6b GSDMD) — approved for AUD; [`disulfiram.md`](./disulfiram.md)
- **Zileuton** (CP6a 5-LOX) — approved for asthma
- **Avacopan** (CP0 C5aR1) — approved for ANCA vasculitis; still on-patent so compounding doesn't apply

Each on-patent + off-label combination needs a per-compound assessment for:
1. Bulk API availability on FDA 503A/503B lists.
2. Off-label dose estimation from preclinical / mechanistic data.
3. Formulation requirements (release profile, bioavailability targets).
4. Physician partner willing to prescribe off-label.
5. Patient population fit.

The discovery engine outputs items 1–3 readily (it's already mining mechanism); items 4–5 require collaborator development outside OE's current team.

## Open questions / Phase 2 follow-ups

> **Tracking status (2026-05-15):** the original 2026-05-11 priority-action ticket had three explicit closure criteria — bulk API audit, disulfiram dose modeling, pharmacy partner identification. Each is now tracked at the surface noted below.

1. **Bulk API audit — completed 2026-05-15, finding reshapes the question.** The audit was originally scoped against a flat "is this drug on the FDA 503A list?" framing that turned out to be structurally inaccurate. Per the new §"How Section 503A actually works" above: 503A allows three tiers of bulk drug substances, and the formal 503A bulks list (Tier 3) contains only six obscure topical compounds — none gout-relevant. The OE candidates are 503A-compoundable via Tier 1 (USP monograph; allopurinol, colchicine, probenecid) or Tier 2 (component of FDA-approved drug; disulfiram, zileuton, pentostatin). The real gating questions are *bulk API commercial supply* (a supplier-side question for zileuton + pentostatin) and *post-withdrawal Tier 2 status* (for lesinurad, the only genuinely uncertain regulatory case in the OE candidate set). The candidate list above is now annotated with the correct tier per compound. **Status:** closed (audit findings landed in the candidate list above).
2. **Pharmacy partner identification.** What 503A compounding pharmacies have track record with gout / inflammation / off-label dose work? Empower Pharmacy, Olympia Pharmacy, others — needs primary-source verification. **Status:** user-action-required (real-world outreach, not Claude-actionable). Stays on this scope page; not in the synthesis queue. **Fires when:** Brian decides to pursue a 503A prescription pathway for any candidate. Until then, dormant.

2a. **Bulk API supplier verification (zileuton, pentostatin, lesinurad).** Per-compound check with compounding-pharmacy supply networks (Spectrum Chemical, PCCA, Letco, FAGRON) for current bulk-API availability + cost + CoA. **Status:** user-action-required (supplier phone/email outreach, not Claude-actionable). **Fires when:** Brian decides to pursue a 503A prescription pathway for any of these three compounds. Until then, dormant — Tier 2 eligibility is confirmed for all three (see candidate list above), so the question is purely supply-chain.
3. **Physician partner pathway.** Off-label prescribing is the physician's discretion but needs a real prescriber. Rheumatology / functional medicine cross-section. The team-building work overlaps with [`team.md`](./team.md) — possibly a fourth collaborator role. **Status:** user-action-required (overlaps team.md).
4. **Dissolution / characterization protocol library.** What standard USP / in-house assays should OE publish as a quality framework for compounded gout formulations? Mirrors [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) for the supplement track.
5. **Insurance / cost reality.** Compounded prescriptions are often not insurance-covered; patient out-of-pocket is the typical reality. What's the cost-per-month for a representative compounded gout repurposing pill, and how does it compare to (a) name-brand alternatives and (b) the engineered-koji daily-food UX?
6. **Disulfiram-specific computational prior.** A comp-NNN-style scoping pass on disulfiram dosing — what's the GSDMD-blockade-relevant plasma concentration vs. the alcohol-deterrent dose? Is there a dose window where GSDMD blockade dominates without producing the alcohol-flush effect? This is the highest-leverage repurposing-surface compound currently in OE and would benefit from explicit dose modeling before any 503A prescription pathway opens. **Tracked at:** [`computational-experiments.md`](./computational-experiments.md) Planned Analyses table as **comp-027** (queued 2026-05-15; Medium-High priority).
7. **Discovery engine output → 503A list intersection.** Build a recurring mechanism in the sweep daemon to flag whenever a new discovery-engine output (e.g., a newly identified repurposing surface compound) has bulk API on the 503A list — making the compounding-track-relevance call automatic rather than ad hoc.

## What this track is NOT

To prevent the "everything is now a compounding pharmacy problem" failure mode, here is what this track explicitly does not cover:

- **Novel chemical entities.** Compounding cannot create molecules that are not already on the FDA bulk drug substances list. New molecules require FDA NDA (the Veradermics path), not compounding.
- **Biologics / proteins / enzymes.** Uricase, lactoferrin, DAF, etc. — fermentation chassis remains the route.
- **Most supplements.** If it's already supplement-grade and OTC, compounding adds cost without value. The exception is documented bioavailability deficits where compounded liposomal / nanoemulsion formulations meaningfully outperform OTC.
- **Replacement for clinical trials.** Off-label compounded prescriptions are not a substitute for the evidence-development work clinical trials produce. They are an *access* path, not an *evidence* path. The evidence still needs to be developed — possibly via real-world data, possibly via investigator-initiated trials downstream.
- **DEA-scheduled substances** unless the prescribing physician has the relevant DEA registration and the pharmacy is licensed to handle scheduled drugs.

The honest summary: compounding pharmacy expands OE's *delivery menu* without expanding OE's *evidence base*. The discovery engine still has to do the science; compounding just makes the science prescribable for the subset of compounds where the API already has FDA approval.

## Related

- [Open Enzyme vision](./open-enzyme-vision.md) — §2.2 repurposing surface framing
- [`open-source-platform.md` §External Service Acceleration](./open-source-platform.md) — names the productized-external-services pattern this page instantiates on the small-molecule / repurposing-surface side
- [Ginkgo Cloud Lab evaluation](./ginkgo-cloud-lab-evaluation.md) — the complementary external-service track on the strain-library / protein-validation side. Ginkgo answers "does the protein fold?"; compounding answers "can the small-molecule reach a patient?". Different sides of the platform, same pattern.
- [Modality × Target Matrix](./modality-chokepoint-matrix.md) — small-molecule rows are the candidate cells for this track
- [Disulfiram](./disulfiram.md) — canonical repurposing surface compound; the highest-priority compounding candidate currently in OE
- [Colchicine](./colchicine.md) — clinical-grade CP6 prophylaxis with custom-dose / combination compounding plays
- [Gout clinical pipeline](./gout-clinical-pipeline.md) — on-patent commercial pipeline that defines the gaps compounding can fill
- [Medicinal mushroom complement track](./medicinal-mushroom-complement-track.md) — peer track for native-compound delivery
- [Engineered koji protocol](./engineered-koji-protocol.md) — peer track for enzyme delivery

---

**Status:** Phase 1 scoped. Phase 2 follow-ups (bulk API audit, pharmacy partner identification, disulfiram dose modeling) queued separately. No commitments to any specific compounded product or patient pathway at this stage — this page exists to make the delivery-route option legible alongside the other peer tracks.
