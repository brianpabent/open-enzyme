---
title: "Ginkgo Cloud Lab — Wet-Lab Partner Evaluation"
date: 2026-05-13
tags:
  - Wet Lab
  - Partners
  - Cloud Lab
  - Cell-Free Expression
  - Strain Engineering
  - Ginkgo Bioworks
  - Uricase
  - DAF CD55
related:
  - engineered-koji-protocol.md
  - engineered-yeast-uricase-proposal.md
  - uricase-variant-selection.md
  - daf-cd55-scr14-truncated-computational.md
  - validation-experiments.md
  - etc/ai-bio-tools-playbook.md
sources:
  - "EstiMate (Ginkgo Bioworks Cloud Lab compatibility & pricing assistant) — 2026-05-12 chat session, Brian Abent"
status: working-note
---

# Ginkgo Cloud Lab — Wet-Lab Partner Evaluation

**Working note — partner evaluation, not primary research.** Brian probed Ginkgo Bioworks' Cloud Lab via their **EstiMate** sales bot on 2026-05-12 using the Open Enzyme GitHub Pages link as the protocol input. This page captures the substantive offer, an analysis of what it actually buys per construct, and where it fits the OE wet-lab plan.

All pricing on this page is from a vendor sales agent, dated 2026-05-12, and **was not obtained through a formal service request**. Treat as a quote-shaped marketing message until verified.

---

## TL;DR

- **Two offers surfaced.** Cell-Free Protein Expression Validation at **$39/protein** (≤1,800 bp, ~5–10 day turnaround) confirms a designed sequence produces folded polypeptide in cell-free lysate. A **96-construct S. cerevisiae strain-engineering campaign at ≈$2,340 total (≈$24.38/sample)** was also quoted.
- **Decision (2026-05-13): skip the $39 cell-free for now.** The offer is real and the price is right, but it was originally scoped as a pre-gate for the *fungal* wet-lab work, and the current priority stack has that wet-lab work as downstream — Ginkgo doesn't need to happen before, during, or after current Phase 0 work. The cell-free test would surface no information the existing computational corpus (comp-019 flux model, comp-022 cassette ranking, comp-023 cordycepin burden, ViennaRNA mRNA folding + ESM2 pseudo-pLDDT proxies) doesn't already give to high confidence. Revisit when a wet-lab experiment actually needs the pre-gate to be load-bearing; until then, save the $39 and the calendar drag.
- **Don't budget against the $24/sample number.** The $2,340 strain-engineering quote is almost certainly a lead-magnet teaser, not what a formal Ginkgo service request will return — historic Ginkgo strain-engineering campaigns at this scope have priced mid-five to six figures. Real strain-engineering campaigns at the OE scope are $3,000–$50,000+ per the academic-collaboration cost framing in [`ward-1995-lab-access.md`](./ward-1995-lab-access.md) and [`validation-experiments.md`](./validation-experiments.md) §1.9.
- **Construct fit is mixed (preserved for future revisit).** Cell-free is a clean test for **uricase variants** (no glycosylation requirement, E. coli-lysate-compatible fold). It is a **weak test for DAF/CD55 SCR1-4** (SCR domains carry O-glycans; aglyco backbone tells you the ORF works but not functional folding). This analysis stands; the skip-for-now decision is about timing and incremental value, not technical fit.
- **Ginkgo Cloud Lab and the community-college / grad-student path are complementary, not competing.** Cell-free answers an earlier gate ("does the sequence produce a folded protein at all?"); the CC path answers the gate Ginkgo's plate-based Cloud Lab cannot ("does it secrete from a fungal host in a real fermentation context?"). Ambr 250 / bioreactor work is, per EstiMate, a separate downstream Ginkgo service.

---

## Transcript (substantive content; sales prompts elided)

Brian shared `https://brianpabent.github.io/open-enzyme/` with EstiMate as the protocol input. The bot's response surfaced two service tiers.

### EstiMate's compatibility evaluation

| Protocol Step | Required Instrument | Cloud Lab Instrument | Available |
|---|---|---|---|
| DNA Assembly | Liquid Handler / Thermal Cycler | Echo 525 / Thermo ATC | ✅ |
| Transformation | Plate Shaker / Incubator | Bioshake 3000-T / Cytomat | ✅ |
| Strain Selection | Plate Reader (Fluorescence/Abs) | Pherastar / Tecan Spark | ✅ |
| Uricase Activity Assay | Plate Reader (Kinetic Absorbance) | BMG Pherastar | ✅ |
| Protein Analysis | Capillary Electrophoresis | AATI Fragment Analyzer | ✅ |
| Metabolite Analysis | LC-MS or GC-MS | Thermo QE Plus / Sciex Echo MS | ✅ |

Host-organism notes from EstiMate:
- ***S. cerevisiae*** — fully supported for automated transformation and screening.
- ***A. oryzae*** — supported, but filamentous fungi need 24-well or 96-well deep-well formats to manage morphology. Liquid dispensing and OD measurements are not the default workflow.
- **Fermentation** — Ginkgo Cloud Lab is optimized for microtiter-plate screening only. Bioreactor work (Ambr 250) is a separate downstream service.

### Pricing tiers quoted

**Strain Engineering & Activity Assay campaign — 96 S. cerevisiae variants:**

| Line Item | Total (96 batch) | Per-sample |
|---|---|---|
| Consumables (plates, tips, reagents) | ≈$1,150 | $11.98 |
| Instrument time (Echo, incubators, reader) | ≈$840 | $8.75 |
| QC & data delivery | ≈$350 | $3.65 |
| **Total** | **≈$2,340** | **$24.38** |

**Cell-Free Protein Expression Validation — flat $39/protein.** EstiMate's description: DNA synthesis (≤1,800 bp), expression in cell-free system, confirmation that the protein is produced and folds, data report. ~5–10 day turnaround.

---

## Deep dive

### What "cell-free expression" actually buys you

Cell-free protein expression in this price tier almost certainly means an **E. coli-derived lysate system** (S30 extract or a PURE-class reconstituted system). EstiMate didn't disclose which — that's the first thing to clarify in a real quote. The mechanism difference matters for OE's constructs:

- **S30 extract** — lysate retains native E. coli chaperones, foldases, and most of the translation machinery. Good for soluble proteins with no special chaperone needs.
- **PURE / reconstituted systems** — purified components only. Cleaner but worse at folding complex multi-domain or disulfide-rich proteins.
- **Eukaryotic lysates** (wheat germ, rabbit reticulocyte, HeLa, insect) — needed for some glycosylation, more native eukaryotic chaperone handling. Almost certainly NOT what's priced at $39.

What the $39 cell-free run **confirms**:
1. The ORF translates without ribosomal stalling or premature termination from rare codons. Mechanistic extrapolation: gives signal that codon-optimized constructs are functional at the polypeptide level.
2. The polypeptide chain folds into a soluble (non-aggregated) state in an E. coli-cytosolic-like environment. Caveat: "soluble" ≠ "functional" — see below.
3. The protein is detectable (typically by tag — His6, FLAG — or by SDS-PAGE / capillary electrophoresis migration). In vitro evidence of expression.

What the $39 cell-free run **does NOT confirm**:
- Folding in a **fungal host** (different chaperone repertoire, different ER/Golgi machinery, different translocation pathway). For Aspergillus oryzae secreted constructs, this gap is large.
- **Glycosylation** (no glycan transfer in E. coli lysate; PURE is even worse). For glycoproteins, the aglyco polypeptide may misfold or fold differently than the native form.
- **Secretion** — cell-free runs are batch reactions in a tube. No signal-peptide cleavage, no Sec/SRP pathway test, no ER quality control.
- **Activity in physiological context** — kinetic assays may be possible as add-ons but require the substrate and a defined readout.

### Construct-by-construct fit

#### Uricase variants — strong fit for the $39 gate

Aspergillus flavus uricase (the rasburicase parent) is a **homotetrameric, non-glycosylated, non-disulfide-bonded** ~34 kDa enzyme. It folds in E. coli expression systems routinely — recombinant production for crystallography, activity studies, and rasburicase manufacturing is well-established. Mechanistic extrapolation: a cell-free run of an A. flavus uricase variant should produce active, soluble enzyme; if it doesn't, the variant has a real folding problem.

Activity is straightforward to test in-tube — urate has a characteristic UV absorbance at 293 nm that drops as uricase converts it to allantoin. Kinetic absorbance readout. EstiMate explicitly listed BMG Pherastar for the uricase activity assay, so the readout is supported in their main strain-engineering tier; the question for the $39 cell-free tier is whether activity-measurement is bundled or a separate line item.

**Suggested first run (deferred per the skip-for-now decision in the TL;DR):** the lead uricase variant from [`uricase-variant-selection.md`](./uricase-variant-selection.md) would be the construct most fit for the $39 test if/when the cell-free pre-gate becomes load-bearing for downstream wet-lab work. Held as a future option, not a current action.

#### Digestive enzymes (lipase, protease, amylase) — likely strong fit

Generally similar to uricase: many bacterial and fungal digestive enzymes express in E. coli lysate (with activity-screening considerations per enzyme). Lipase folding is sometimes finicky due to interfacial activation requirements; protease activity assays in cell-free lysate need careful background-protease subtraction. Detailed per-enzyme analysis deferred — this evaluation is scoped to the offer, not to per-construct planning. See [`digestive-enzymes.md`](./digestive-enzymes.md) for the construct list.

#### DAF/CD55 SCR1-4 — weak fit for the $39 gate

DAF/CD55 is a **GPI-anchored, O-glycosylated, disulfide-bonded** complement regulator. The SCR (sushi/CCP) domains carry the canonical 2-disulfides-per-domain fold (verified against UniProt P08174 — 8 DISULFID features across SCR1-4 — see the discipline note in OE's [`CLAUDE.md`](../CLAUDE.md) and the comp-012 incident retrospective). E. coli lysate:

- **Cannot make GPI anchors** (no GPI-transamidase, no GPI-PI biosynthesis machinery). The aglyco / non-anchored construct is a different molecule from the native one.
- **Cannot add O-glycans** (no O-GlcNAc transferase, no mucin-type GalNAc-T machinery). The SCR-domain O-glycans, where they sit on the protein-protein interaction surfaces, won't be present.
- **Disulfide bond formation in cytosolic E. coli lysate is poor.** Specialized strains (Origami, SHuffle) or oxidizing-environment systems (CyDisCo) help, but EstiMate didn't specify which lysate. Default expectation: cytosolic, reducing, poor disulfide formation. For a protein with 8 disulfides in 4 small domains, this is a real folding obstacle.

The $39 cell-free on DAF/CD55 SCR1-4 would still surface whether the ORF is translatable and whether the polypeptide is detectable at all. It would NOT tell you whether the truncated-SCR construct from [`daf-cd55-scr14-truncated-computational.md`](./daf-cd55-scr14-truncated-computational.md) is functional. Mechanistic extrapolation: a negative result is informative (the ORF has a fundamental translation problem); a positive result is NOT informative (the protein exists but probably misfolded, and you've learned almost nothing about behavior in a fungal secretory pathway).

**For DAF/CD55 specifically:** skip the $39 cell-free as the validation gate. Go directly to a eukaryotic-secretory-pathway expression system or wait for the fungal-host work.

### Pricing analysis: the $24/sample strain-engineering quote

The $2,340-for-96-samples number is the part of EstiMate's offer that doesn't pass a sniff test. A 96-well S. cerevisiae construction + transformation + growth + activity-assay campaign typically involves:

- DNA synthesis or assembly for 96 distinct constructs (gBlocks, twist fragments, or Golden Gate assembly — easily $5–15 per fragment for the DNA alone)
- Transformation media, recovery, selection plates
- Plate-based growth, OD monitoring, induction
- Activity assays (substrate, buffer, plate reader time)
- Genotyping at least a subset to confirm the correct construct landed
- QC + data delivery

Conservatively, the consumables-alone floor for this scope is in the **$3,000–$8,000** range before any instrument time, FTE labor, or margin. Quoted $24/sample is **below cost-to-serve** for a real foundry. Three possibilities:

1. **Lead-magnet pricing** — the bot quotes an attractive number to capture an email; the real quote (the "submit a service request" path EstiMate flagged) is much higher.
2. **Heavily-discounted intro tier** — Ginkgo may have a one-time discounted onboarding for new academic/open-source customers. Possible but worth verifying explicitly.
3. **Bot hallucination** — EstiMate may be confidently generating a number from a price-list template that doesn't apply to this scope. The chat-bot framing of estimates as ranges with the explicit disclaimer "Actual pricing will be confirmed when you submit a service request" suggests Ginkgo themselves know the quotes are loose.

**Don't budget Open Enzyme work against the $24/sample number.** The $39 cell-free is, by contrast, a small flat-rate offering that's plausibly real at that price — it's a productized SKU, not a campaign.

### Where this fits the OE wet-lab plan

The active wet-lab strategy across OE has two parallel candidate paths, answering different gates:

| Gate | Path | Cost order | Turnaround |
|---|---|---|---|
| Does the designed sequence produce a folded polypeptide at all? | Ginkgo Cloud Lab cell-free ($39/protein) | $10s–$100s | ~1 week |
| Does the construct work in a fungal host with secretion, real fermentation, and downstream activity? | Community-college / grad-student thesis path (see [`etc/team.md`](./etc/team.md) and the wet-lab-search memory) | Time-only (if a willing grad student lands) | months |

The Ginkgo cell-free pre-gate is **upstream** of the fungal/fermentation gate. Negative cell-free result = redesign the construct before any fungal work. Positive cell-free result = construct is worth committing fungal-host effort to. Either way, $39 buys earlier information than the fungal path can provide.

Ginkgo's full strain-engineering tier sits **in the same niche** as the CC path — but plate-based, not fermentation-based, and at unknown true cost. Worth a real quote before deciding it's the right tool.

### Recommended next move (revised 2026-05-13: none — deferred)

**No action.** The $39 cell-free pre-gate was originally framed as a sequence-validation step upstream of the fungal wet-lab work. The current priority stack has that wet-lab work downstream of in-flight in-silico work; the cell-free test would not surface information the existing computational corpus (comp-019, comp-022, comp-023, ViennaRNA mRNA folding + ESM2 pseudo-pLDDT) doesn't already provide to high confidence.

Revisit when a downstream wet-lab experiment becomes load-bearing and an independent E. coli-lysate fold-check would meaningfully de-risk it. Until then, save the $39 and the calendar drag.

For reference, the original (now-deferred) recommendation rationale:
- Cheap. Single-construct, productized SKU, no campaign commitment.
- Real test of EstiMate's claims — does the $39 actually deliver what the bot described, on what turnaround, with what data product.
- Construct-appropriate — uricase is the OE construct best matched to E. coli-lysate cell-free.
- Establishes a vendor relationship useful for downstream work.

The rationale stands; the *timing* is what changed.

---

## Open questions to resolve before committing

- **What lysate?** S30, PURE, or eukaryotic? Affects disulfide and glycoprotein fits significantly. Ask Ginkgo directly.
- **Is activity assay bundled in the $39 or extra?** EstiMate listed the activity assay as part of the strain-engineering tier; the cell-free description mentioned only expression confirmation. For uricase, the in-tube absorbance assay is cheap; it might be add-on-able for nominal cost.
- **What data product?** EstiMate said "data report" — verify whether you get raw traces, processed numbers, both. For an open-source project, raw data matters more than a PDF.
- **DNA synthesis IP / data ownership.** For a public open-source project, confirm Ginkgo claims no rights to the sequences submitted or the data generated. This is typically clean for productized SKUs but worth confirming explicitly.
- **What's the real strain-engineering quote?** Submit a service request for one well-defined campaign (e.g., 12 uricase variants in S. cerevisiae with the standard cassette from [`codon-optimization-expression-cassette.md`](./codon-optimization-expression-cassette.md)) and see what the actual number is.
- **Academic / open-source pricing.** Whether Ginkgo offers structured discounts for non-commercial / open-source projects. EstiMate did not surface a specific program; worth asking the sales team directly.

---

## Evidence levels

All claims on this page are at one of two levels:

- **Vendor quote (2026-05-12)** — pricing, instrument list, turnaround, available SKUs. Source: EstiMate chat session. Not verified by formal service request.
- **Mechanistic extrapolation** — claims about what cell-free expression does/doesn't capture for specific OE constructs. Based on standard knowledge of E. coli S30 / PURE systems and the structural biology of the named proteins.

No clinical, animal, or in vitro evidence is generated on this page. The recommended $39 cell-free run, if executed, would produce **In Vitro** evidence on a specific OE construct.

---

## References

- EstiMate (Ginkgo Bioworks Cloud Lab compatibility & pricing assistant) — 2026-05-12 chat session transcript, on file in Brian's notes.
- UniProt P08174 (DAF / CD55 *H. sapiens*) — disulfide annotations (8 DISULFID features in SCR1-4).
- [`etc/ai-bio-tools-playbook.md`](./etc/ai-bio-tools-playbook.md) — prior mention of Ginkgo as a lab-in-the-loop routing destination via Amazon Bio Discovery.

---

## Related

- [`open-source-platform.md` §External Service Acceleration](./etc/open-source-platform.md) — names the productized-external-services pattern this page instantiates on the strain-library side.
- [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) — the complementary external-service track on the small-molecule / repurposing-surface side. Ginkgo answers "does the protein fold?"; compounding answers "can the small-molecule reach a patient?". Different sides of the platform, same pattern.
- [`ward-1995-lab-access.md`](./ward-1995-lab-access.md) — the academic-collaboration wet-lab path; Ginkgo's $39 pre-gate sits *upstream* of this path, not in competition with it.
