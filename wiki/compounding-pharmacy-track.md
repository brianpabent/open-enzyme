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
  - etc/open-enzyme-vision.md
  - etc/open-source-platform.md
  - modality-chokepoint-matrix.md
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
  - "MINX precedent: 5 mg once-daily extended-release oral minoxidil developed via ChatGPT-aided formulation review + lipid-matrix design + 503A compounding pharmacy + dissolution testing; built in days, not the multi-year Veradermics trial track"
  - "FDA 503A (patient-specific) and 503B (outsourcing facility) compounding statutes — Drug Quality and Security Act of 2013"
status: scoped (Phase 1)
---

# Compounding Pharmacy Track — Delivery Route for the Repurposing Surface

## Gout exploit hypothesis

Some approved drugs hit gout-relevant chokepoints but lack a suitable commercial formulation or gout indication. Compounding could provide a testable, patient-specific formulation only when the active ingredient, prescriber, pharmacy, and proposed use fit the applicable legal and safety requirements. Examples under investigation include [disulfiram](./disulfiram.md) at CP6b GSDMD and zileuton at CP6a 5-LOX; neither has established clinical efficacy in gout.

The compounding-pharmacy track asks whether an identified drug–chokepoint match can become a testable formulation under the applicable compounding rules. It covers the gap between mechanism identification and formulation access; it does not establish clinical efficacy or authorize treatment.

## Scope and kill criteria

The track covers small molecules whose formulation, dose form, or availability is the unresolved problem. Eligibility is assessed through the 503A hierarchy described below:

  - Off-patent FDA-approved drugs with USP/NF monographs → **first-class compounding-pharmacy targets** (Tier 1 eligible, the easiest path; allopurinol, colchicine, probenecid sit here)
  - Off-patent FDA-approved drugs without USP/NF monograph but with an active FDA approval → **first-class compounding-pharmacy targets** via Tier 2 (component of FDA-approved drug); the MINX category sits here, as do disulfiram and zileuton
  - FDA-approved drugs that have been commercially withdrawn → **regulatory edge case** — Tier 2 status may or may not survive market withdrawal; needs per-compound verification (lesinurad is the canonical example)
  - Supplements (BHB, ergothioneine, quercetin, etc.) → typically already supplement-grade; compounding adds little value over OTC purchase
  - Research compounds with no FDA approval (MCC950, dapansutrile in some markets) → **not 503A-compoundable** unless they appear on the formal Tier 3 list, which they don't
  - Peptides (KPV, BPC-157) → compoundable but more constrained; KPV / BPC-157 / TB-500 / MOTs-C are under formal Tier-3 consideration at FDA's Pharmacy Compounding Advisory Committee (July 2026 meeting)

The MINX example demonstrates the workflow shape: literature and patent review, formulation design, a 503A pharmacy, and dissolution testing applied to an already approved active ingredient. It is a process precedent, not evidence for any gout candidate.

Kill or redirect a candidate when the bulk substance is ineligible or unavailable, the proposed formulation adds no measurable value, relevant exposure cannot be achieved safely, or the mechanism lacks gout-relevant evidence. Compounding changes formulation and access; it does not validate the target, dose, efficacy, or safety.

Proteins, enzymes, live organisms, novel chemical entities, and products with no lawful bulk-substance basis are outside this route. The [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) owns comparisons with other intervention routes.

## How Section 503A works

"Is this drug on the FDA 503A list?" is the wrong gate because Section 503A is not a single flat lookup. Per [21 CFR 216 + FDA's Section 503A guidance](https://www.fda.gov/drugs/human-drug-compounding/bulk-drug-substances-used-compounding-under-section-503a-fdc-act), a 503A compounding pharmacy may use bulk drug substances that fall into any one of three tiers, in priority order:

1. **Tier 1 — USP / NF monograph substances.** The substance is the subject of an applicable USP or NF monograph and compounded in compliance with USP <795>/<797>. Most of the well-established small-molecule drugs sit here — allopurinol, colchicine, probenecid all have long-standing USP monographs.
2. **Tier 2 — Components of FDA-approved drug products.** If no applicable USP/NF monograph exists, the bulk substance qualifies if it's an active component of an FDA-approved drug product (with a valid certificate of analysis from an FDA-registered facility). Disulfiram, zileuton, pentostatin sit here — all FDA-approved drugs, all eligible for 503A compounding via Tier 2 regardless of whether they have a current USP monograph.
3. **Tier 3 — The formal FDA 503A bulks list.** Substances that don't qualify under Tier 1 or Tier 2 can still be 503A-compoundable if FDA has placed them on the formal 503A bulks list. **The formal list is short** — only six substances as of 2026-05-15 (Brilliant Blue G, cantharidin, diphenylcyclopropenone, N-acetyl-D-glucosamine, squaric acid dibutyl ester, thymol iodide), all obscure topical compounds; none are gout-relevant. Peptide nominations (KPV, BPC-157, TB-500, MOTs-C) are under PCAC review for July 2026.

**Implications for the OE candidate list.** For all the compounds OE has identified as gout-chokepoint hits, the question is which tier they qualify under, not whether they appear on the formal Tier 3 list. The gating empirical questions are:

- **Tier 1 / Tier 2 confirmation per compound** — mostly trivial: every OE candidate except lesinurad is an FDA-approved drug, so Tier 2 applies at minimum. Most also have USP monographs (Tier 1).
- **Bulk API commercial supply** — a *supply-chain* question, not a regulatory one. Some FDA-approved drugs (notably pentostatin, which is parenteral and hospital-pharmacy-distributed) have bulk API that's hard to source for 503A pharmacies regardless of regulatory eligibility.
- **Post-withdrawal Tier 2 status** — for lesinurad (FDA-approved 2015, commercially withdrawn 2019), does Tier 2 eligibility survive market withdrawal? This is the only genuinely uncertain regulatory question in the OE candidate set.

For the candidates assessed here, formal 503A-list status is usually not the gating question; commercial bulk-API supply and off-label prescribing infrastructure are.

## Candidate repurposing formulations

### Discovery-engine repurposing candidates (compounding-pharmacy track, properly so called)

These are drugs NOT currently used for gout, identified by the OE discovery engine as hitting gout-relevant chokepoints. Compounding turns identification into patient access.

For each entry: chokepoint mapping, 503A-eligibility tier, evidence level for the gout / NLRP3 application, what a compounding formulation would actually look like.

**1. Disulfiram (Antabuse) — CP6b GSDMD inhibitor.**
- 503A eligibility: Tier 2 (component of FDA-approved drug). FDA-approved 1951 for alcohol-use disorder; off-patent; bulk API widely available from compounding-pharmacy suppliers.
- Gout-relevant evidence: **In vitro** — Hu et al. 2020 (*Nat Immunol*) — disulfiram directly inhibits gasdermin D pore formation, blocking IL-1β release downstream of NLRP3. No human gout trials.
- **Dose modeling — [comp-027](./disulfiram-dose-modeling-computational.md) (2026-05-16) → downgraded to hypothesis-generator (comp-review 2026-07-14).** A **single strict-GREEN modeled point at 100 mg/day** (the 75–125 mg/d range was broadened from that single point, not independently derived; it sits exactly on a hard-coded decision boundary — a dose-finding hypothesis to test, not a validated window), where parent DSF Cmax (0.40 µM, 1.3× cell-free GSDMD IC50 of 0.30 µM per Hu 2020) engages pore-formation blockade while plasma Me-DTC peak (~70 nM) stays at or below the Faiman-1989 DER hypotension threshold (~70 nM at 40% ALDH inhibition). NLRP3-palmitoylation EC50 (Xu 2024, 10 µM) requires AUD-dose+ plasma — **sub-AUD is selectively GSDMD-engaging, not pan-NLRP3-engaging**. Sensitivity dominated by GSDMD EC50 anchor choice + parent DSF Cmax PK at 100 mg (single empirical HPLC measurement in N=3–5 volunteers would collapse this uncertainty).
- Formulation status: **no dose, titration, release profile, combination, or patient-use protocol is validated.** Comp-027 supplies a hypothesis-generating boundary point, not a formulation specification. Empirical exposure, interaction, and safety work must precede any formulation claim.
- Safety constraint: disulfiram has clinically important alcohol and drug interactions. No gout combination should be described as clean without direct evidence and current-label review.
- Evidence level for the application: **Mechanistic extrapolation + in vitro + in silico dose modeling.** Per-patient HPLC-anchored dose-finding is the wet-lab gate before broader patient use.

**2. Zileuton — CP6a 5-LOX inhibitor.**
- 503A eligibility: Tier 2 (component of FDA-approved drug Zyflo, 1996, asthma); off-patent. Bulk API availability is a supplier-side question, not a regulatory listing question — current Zyflo distribution is small enough that compounding-pharmacy supplier networks may not stock the API even though 503A eligibility is structurally clean.
- Gout-relevant evidence: **Mechanistic extrapolation + in vitro** — 5-LOX produces LTB4, a neutrophil chemoattractant active in gout flares. Zileuton blocks 5-LOX. No gout clinical trials.
- Formulation status: no gout dose or release profile is validated. Bulk-API availability, hepatic safety, exposure, and a gout-relevant efficacy assay gate further formulation work.
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

## 503A vs. 503B — regulatory mechanics (brief)

The Drug Quality and Security Act of 2013 created two distinct compounding pharmacy regulatory categories. Open Enzyme work in this space needs to be honest about which lane applies.

| | **503A** | **503B** |
|---|---|---|
| Statute | Section 503A of FDCA | Section 503B of FDCA |
| Who | Traditional compounding pharmacies | Outsourcing facilities (FDA-registered) |
| Trigger | Valid patient-specific prescription | Can compound without patient-specific Rx |
| Bulk API source | Must be on FDA 503A bulk drug substances list (or be a component of an FDA-approved drug) | Must be on FDA 503B bulk drug substances list |
| GMP | Not required at 503A level (state-board oversight) | Full cGMP compliance required |
| Distribution | Single patient at a time, in response to Rx | Can ship to hospitals/clinics in bulk |
| Best for | Custom doses, low-volume, individualized formulations | Repeated production of a stable repurposing formulation across many patients |

Candidate development may begin with a patient-specific 503A route only when the legal, prescribing, and safety requirements are satisfied. Repeated higher-volume production would require a different route, such as a qualified 503B facility or a sponsored development program.

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

AI-assisted literature and patent review can accelerate formulation reconnaissance. It does not replace pharmacist design, current regulatory review, compatibility work, or analytical validation.

The verification step (dissolution testing per USP <711>, content uniformity per USP <905>) is non-negotiable and runs at the compounding pharmacy or a contract analytical lab. **Without dissolution data, you don't know what you made.**

## Discovery-engine integration

The repurposing surface includes approved drugs with plausible gout-relevant mechanisms but no established gout indication. Current examples include:

- **Disulfiram** (CP6b GSDMD) — approved for AUD; [`disulfiram.md`](./disulfiram.md)
- **Zileuton** (CP6a 5-LOX) — approved for asthma
- **Avacopan** (CP0 C5aR1) — approved for ANCA vasculitis; still on-patent so compounding doesn't apply

Each candidate needs a per-compound assessment of:
1. Bulk API availability on FDA 503A/503B lists.
2. Whether preclinical or mechanistic evidence justifies an exposure-finding study.
3. Formulation requirements (release profile, bioavailability targets).
4. Physician partner willing to prescribe off-label.
5. A defined population, safety boundary, and evidence-development plan.

## Unresolved requirements

1. **Bulk-substance basis.** The candidates assessed here fall under Tier 1 (USP monograph: allopurinol, colchicine, probenecid) or Tier 2 (component of an FDA-approved drug: disulfiram, zileuton, pentostatin). Verify this basis again against current FDA materials before acting.
2. **Pharmacy capability.** Identify a licensed pharmacy with relevant formulation and analytical capability only after a candidate passes the evidence and legal gates.
3. **Bulk API supply.** Verify current availability, certificate of analysis, cost, and supplier registration for each candidate.
4. **Clinical governance.** A qualified prescriber and an explicit evidence-development and monitoring plan are prerequisites, not implementation details.
5. **Dissolution / characterization protocol.** Define release, content-uniformity, stability, and impurity requirements before interpreting a formulation.
6. **Cost and added value.** Determine whether the proposed formulation solves a real access, exposure, or adherence problem that an approved commercial product does not.
7. **Disulfiram dose finding.** [Comp-027](./disulfiram-dose-modeling-computational.md) is a hypothesis generator with one boundary-dependent modeled point, not a validated dose window. Empirical exposure and safety data are required before formulation work.

## What this track is NOT

To prevent the "everything is now a compounding pharmacy problem" failure mode, here is what this track explicitly does not cover:

- **Novel chemical entities.** Compounding cannot create molecules that are not already on the FDA bulk drug substances list. New molecules require FDA NDA (the Veradermics path), not compounding.
- **Biologics / proteins / enzymes.** Uricase, lactoferrin, DAF, and similar payloads fall outside this small-molecule compounding route.
- **Most supplements.** If it's already supplement-grade and OTC, compounding adds cost without value. The exception is documented bioavailability deficits where compounded liposomal / nanoemulsion formulations meaningfully outperform OTC.
- **Replacement for clinical trials.** Off-label compounded prescriptions are not a substitute for the evidence-development work clinical trials produce. They are an *access* path, not an *evidence* path. The evidence still needs to be developed — possibly via real-world data, possibly via investigator-initiated trials downstream.
- **DEA-scheduled substances** unless the prescribing physician has the relevant DEA registration and the pharmacy is licensed to handle scheduled drugs.

Compounding can change formulation or access for a narrow eligible subset. It does not expand the evidence base or turn a mechanistic hypothesis into a treatment.

## Related

- [Open Enzyme vision](./etc/open-enzyme-vision.md) — repurposing-surface framing
- [Modality × Target Matrix](./modality-chokepoint-matrix.md) — portfolio-level route comparison
- [Disulfiram](./disulfiram.md) — GSDMD mechanism and evidence limits
- [Colchicine](./colchicine.md) — clinical-grade CP6 prophylaxis with custom-dose / combination compounding plays
- [Gout clinical pipeline](./gout-clinical-pipeline.md) — on-patent commercial pipeline that defines the gaps compounding can fill
