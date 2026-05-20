---
title: "Synthesis — 2026-05-20 (commit 5cafe11)"
date: 2026-05-20
commit: 5cafe11a1be17d8e1625aca0775792b17befbcb6
diff_base: deef00c7264778c88a2993d3c953d176f2173a7e
trigger_files: wiki/abcg2-modulators.md,wiki/bhb-ketones.md,wiki/cannabinoids-terpenes.md,wiki/chaperone-orthogonal-stacking.md,wiki/colchicine.md,wiki/complement-c5a-gout.md,wiki/delivery-route-matrix.md,wiki/engineered-koji-protocol.md,wiki/engineered-lbp-chassis.md,wiki/etc/ai-bio-tools-playbook.md,wiki/etc/autonomous-screening-methodology.md,wiki/etc/bio-ai-tools.md,wiki/etc/experiments/comp-034-lactoferrin-linker-redesign/proteinmpnn_rerun/summary.md,wiki/etc/manual-literature-mining.md,wiki/etc/open-enzyme-vision.md,wiki/etc/open-source-platform.md,wiki/etc/practitioner-toolkit.md,wiki/genotype-informed-supplement-workflow.md,wiki/gout-action-guide.md,wiki/gout-genetic-variants.md,wiki/gout-pathophysiology.md,wiki/hypotheses/H04-tcm-rigor-intersection.md,wiki/hypotheses/H06-medicinal-mushroom-complement-track.md,wiki/koji-endgame-strain.md,wiki/koji-home-fermentation.md,wiki/lactoferrin-linker-redesign-computational.md,wiki/lactoferrin.md,wiki/medicinal-mushroom-complement-track.md,wiki/medicinal-mushroom-compound-mapping-computational.md,wiki/medicinal-mushroom-extract-sops.md,wiki/nlrp3-exploit-map.md,wiki/nlrp3-inflammasome.md,wiki/personal-genome-protocol.md,wiki/quantification-ladder.md,wiki/self-experiment-protocol.md,wiki/sirna-urat1-modality.md,wiki/spm-resolution-pathway.md,wiki/supplements-stack.md,wiki/tcm-gout-compound-triage-computational.md,wiki/tcm-modern-rigor-intersection.md,wiki/upstream-complement-modulator-sweep-computational.md,wiki/validation-experiments.md
reviewer_model: deepseek/deepseek-v4-pro
reviewer_model_served_raw: deepseek/deepseek-v4-pro-20260423
reviewer_model_requested: deepseek/deepseek-v4-pro
reviewer_fallback_used: False
input_tokens: 931736
output_tokens: 10273
cost_usd: 0.4142
corpus_files: 118
---

# Synthesis — 2026-05-20

**Substrate:** Open Enzyme wiki at commit `5cafe11`  
**Trigger files:** `abcg2-modulators.md`, `bhb-ketones.md`, `cannabinoids-terpenes.md`, `chaperone-orthogonal-stacking.md`, `colchicine.md`, `complement-c5a-gout.md`, `delivery-route-matrix.md`, `engineered-koji-protocol.md`, `engineered-lbp-chassis.md`, `etc/ai-bio-tools-playbook.md`, `etc/autonomous-screening-methodology.md`, `etc/bio-ai-tools.md`, `etc/experiments/comp-034-lactoferrin-linker-redesign/proteinmpnn_rerun/summary.md`, `etc/manual-literature-mining.md`, `etc/open-enzyme-vision.md`, `etc/open-source-platform.md`, `etc/practitioner-toolkit.md`, `genotype-informed-supplement-workflow.md`, `gout-action-guide.md`, `gout-genetic-variants.md`, `gout-pathophysiology.md`, `hypotheses/H04-tcm-rigor-intersection.md`, `hypotheses/H06-medicinal-mushroom-complement-track.md`, `koji-endgame-strain.md`, `koji-home-fermentation.md`, `lactoferrin-linker-redesign-computational.md`, `lactoferrin.md`, `medicinal-mushroom-complement-track.md`, `medicinal-mushroom-compound-mapping-computational.md`, `medicinal-mushroom-extract-sops.md`, `nlrp3-exploit-map.md`, `nlrp3-inflammasome.md`, `personal-genome-protocol.md`, `quantification-ladder.md`, `self-experiment-protocol.md`, `sirna-urat1-modality.md`, `spm-resolution-pathway.md`, `supplements-stack.md`, `tcm-gout-compound-triage-computational.md`, `tcm-modern-rigor-intersection.md`, `upstream-complement-modulator-sweep-computational.md`, `validation-experiments.md`  
**Diff base:** `deef00c7264778c88a2993d3c953d176f2173a7e`  
**Reviewer:** deepseek/deepseek-v4-pro

---

## New Connections

1. **CFH Y402H (rs1061170), the most common complement-dysregulation variant, may interact with dietary upstream‑CP0 candidates (rosmarinic acid, luteolin, Houttuynia cordata polysaccharides) to produce a genotype‑×‑diet interaction on gout flare severity — analogous to the Q141K‑×‑butyrate model already developed for ABCG2.**  
   *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: partial]`

   - *Documents Connected:* `gout-genetic-variants.md` (new CFH Y402H table row + counter‑evidence flag), `complement-c5a-gout.md` (upstream‑CP0 dietary candidates, combined‑coverage hypothesis), `upstream-complement-modulator-sweep-computational.md` (comp‑018 Phase 2 Houttuynia cordata), `upstream-complement-verification-rerun-computational.md` (comp‑020 rosmarinic acid / luteolin / Helicteres ranking).  
   - *Page‑pair linkage:* These pages are **weakly paired**. `complement-c5a-gout.md` names CFH Y402H briefly (§6.3) but never connects it to the dietary‑CP0 thread; `gout-genetic-variants.md` mentions the dietary‑CP0 candidates only in the CFH entry itself and does not cross‑link the complement‑mechanism pages. No existing page models the Y402H‑×‑diet interaction.  
   - *Why It Matters:* If CFH Y402H carriers have exaggerated complement‑priming on MSU crystals, then the dietary C3‑convertase inhibitors already identified by comp‑018/020 could provide a **genotype‑targeted, food‑grade CP0 layer** for ~30–40% of Europeans and Africans — a precision‑prevention lever that would parallel the butyrate‑Q141K thesis and require only dietary adherence, not a new drug. The AMD precedent points in the opposite direction (zinc/antioxidant supplementation *worsens* outcomes in CFH high‑risk carriers), which makes the predicted direction uncertain but also surfaces a testable mechanistic‑dissociation hypothesis: the OE dietary candidates act *upstream* of CFH, so the AMD paradox may not transfer.  
   - *Suggested Action:* The cheapest de‑risker is the **UK Biobank cross‑tabulation** already scoped in `gout-genetic-variants.md` (§Category 5 CFH row): `rs1061170` × dietary polyphenol intake × incident gout, feasible via collaboration with existing UKB gout‑GWAS groups (Merriman/Otago, Major‑Wrigley/Auckland, Choi/MGH). This is a $0, ~3‑month collaboration proposal, not a solo OE application. In parallel, flag the falsifiable prediction in `self-experiment-protocol.md` §4: if SFH DHA‑loaded subjects show faster serum C5a decline during flare resolution than DHA‑deficient subjects, that pattern should be steeper in CFH 402 HH carriers (testable as a within‑subject add‑on to the existing flare‑tracking protocol).  

   {{PEER-REVIEW}}

2. **The generalizable “protease‑vulnerability‑to‑redesign” workflow demonstrated for lactoferrin’s inter‑lobe linker (comp‑034) creates a design rule for future Open Enzyme payloads: secreted proteins with structured‑mandatory‑connectors can be rigidified with proline substitutions, while truncatable‑spacers should be removed entirely — a classification that distinguishes *which* redesign strategy applies and prevents the failure mode of applying the wrong one.**  
   *Supported (by comp‑034 ProteinMPNN rerun + comp‑006/012 DAF precedent).* `[CHAIN-DEPTH: 2]` `[REFRAME]` `[PHASE-A-MATCH: partial]`

   - *Documents Connected:* `lactoferrin-linker-redesign-computational.md` (comp‑034, first concrete use of protein‑design‑mcp), `etc/bio-ai-tools.md` (protease‑vulnerability‑to‑redesign workflow), `chaperone-orthogonal-stacking.md` (folding‑kinetic context for payloads), `validation-experiments.md` §1.10 (the multi‑variant assay gate), `daf-cd55-scr14-truncated-computational.md` (counter‑example solved by truncation, not rigidification).  
   - *Page‑pair linkage:* The workflow is described in `bio‑ai‑tools.md` and instantiated in `lactoferrin-linker-redesign-computational.md`, but the **rule that it is *non‑applicable* to truncatable‑spacer problems (DAF SCR1‑4) has been stated only as a Pass 3 correction caveat** and never as a positive platform‑design principle. The two cases are linked only by the general “protease stability” theme, not by a named classification.  
   - *Why It Matters:* As the platform adds more secreted payloads (C1‑INH serpin, future fusion proteins, therapeutic peptides), the engineering team needs a **decision tree**: (a) is the vulnerable region structured‑mandatory (connects two essential domains, cannot be deleted)? → design‑in‑place via proline rigidification (comp‑034 workflow). (b) Is it an unstructured, removable spacer? → truncate (comp‑012 workflow). Applying the wrong strategy — truncating a mandatory linker or rigidifying a stalk — is the failure mode that the DAF‑scr14‑truncated page was originally built to avoid, and the lactoferrin‑linker‑redesign work now provides the positive exemplar of the other branch. Codifying this as **Platform Design Rule 10** (or similar) in `etc/open-source-platform.md` gives future sub‑agents and human designers a documented heuristic.  
   - *Suggested Action:* Add a new subsection “Protease‑vulnerability classification rule” to `etc/open-source-platform.md` (or to `etc/bio-ai-tools.md`’s workflow section) citing comp‑012 (truncation) and comp‑034 (rigidification) as the two canonical worked examples. The rule fires whenever a new secreted payload is being evaluated for shio‑koji compatibility.

   {{PEER-REVIEW}}

3. **The multi‑modal acute‑flare protocol combining colchicine (CP3/CP2, systemic), topical CBD:THC (CB2‑mediated NLRP3 suppression, local), and DHA‑emphasis omega‑3 (SPM resolution, CP5b) creates a three‑mechanism, three‑route acute intervention that none of the individual wiki pages have composed — each arm is documented separately, but the full composition as a named protocol is absent.**  
   *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `colchicine.md` (CP3/CP2, AGREE trial), `cannabinoids-terpenes.md` (topical CBD:THC protocol + Brian’s n = 1 observation), `spm-resolution-pathway.md` (DHA‑driven RvD1/MaR1 & C5a‑decline prediction), `nlrp3-exploit-map.md` (chokepoint coverage audit).  
   - *Page‑pair linkage:* **Weak.** `colchicine.md` §3.3.1 names the colchicine‑+‑topical‑CBD:THC stack (Protocol A), `gout-action-guide.md` names the four‑route layered protocol (Protocol B) but neither adds DHA‑emphasis omega‑3 as a third mechanism. `spm-resolution-pathway.md`’s C5a‑decline‑slope prediction (§7.3) is not cross‑linked to any acute‑flare protocol.  
   - *Why It Matters:* Gout flares have three temporal phases: onset (minutes‑hours, CP0/CP2), amplification (hours‑days, CP3/CP6a), and resolution (days, CP5b). The current wiki treats interventions as “stacking for chronic prevention” or “acute rescue with one drug,” but a **time‑phased, multi‑route, multi‑chokepoint acute protocol** — early CB2‑suppression + microtubule‑disruption + late SPM‑driven resolution — would address the flare at every phase through independent mechanisms and delivery compartments. This composition has not been named in any page.  
   - *Suggested Action:* Add a named protocol “Triple‑Route Acute Flare Stack” (or similar) to `gout-action-guide.md` and `nlrp3-exploit-map.md`, with explicit timing: (t = 0) colchicine 1.2 mg + topical CBD:THC + ice; (t = +1 h) colchicine 0.6 mg; continue DHA‑emphasis omega‑3 at the existing chronic dose. Flag as Speculative (no RCT of the combination exists). The n = 1 observation in `cannabinoids-terpenes.md` provides a single‑subject anchor.

   {{PEER-REVIEW}}

4. **Substrate composition is now a deliberate, cross‑track engineering variable — it modulates cordycepin:pentostatin ratios in *Cordyceps militaris*, ergothioneine yields in *Pleurotus* and koji, and the protease environment affecting heterologous protein stability in solid‑state fermentation — yet no platform‑level document treats substrate as a unified engineering lever across tracks.**  
   *Supported (by the substrate‑engineering lit scan and SOP‑7).* `[CHAIN-DEPTH: 2]` `[REFRAME]` `[PHASE-A-MATCH: partial]`

   - *Documents Connected:* `medicinal-mushroom-complement-track.md` (substrate‑engineering findings, Platform Principle 9), `medicinal-mushroom-extract-sops.md` (SOP‑7 protocol matrix), `koji-home-fermentation.md` (substrate discussion, methionine supplementation for ergothioneine), `engineered-koji-protocol.md` (substrate effects on native metabolite profile), `validation-experiments.md` §1.29 (cordycepin‑×‑substrate‑matrix experiment).  
   - *Page‑pair linkage:* **Weak across tracks.** `medicinal-mushroom‑complement‑track.md` treats substrate engineering as a cultivation‑track lever; `koji‑home‑fermentation.md` discusses rice bran vs white rice yield but does not frame it as an *engineering* variable. The substrate‑engineering lit scan that produced SOP‑7 explicitly cross‑applied the mechanisms to *A. oryzae* (methionine → ergothioneine via Lee 2009, carbon‑source modulation of secondary metabolites), but this cross‑track implication is stated only in the scan log, not in a permanent wiki page.  
   - *Why It Matters:* Substrate engineering is the **lightest‑effort, highest‑leverage lever** in the platform — every reagent in SOP‑7 is GRAS food‑grade, available at consumer retail, and requires no genetic modification. Yet the platform currently treats substrate as a “documentation discipline” (batch‑QC context) rather than an “engineering discipline” (deliberate yield‑optimisation and compound‑profile tuning). Elevating substrate to a named cross‑track engineering principle would give every distributed contributor a lever they can pull without a lab, and would connect the koji and mushroom tracks at a practical operations layer.  
   - *Suggested Action:* Codify “Substrate composition as a cross‑track engineering variable” as a permanent section in `etc/open-source-platform.md` (promote Platform Principle 9 from the scope page to the platform‑principles document). Cross‑link the SOP‑7 protocol matrix, the methionine‑for‑ergothioneine finding, and the cordycepin‑×‑pentostatin‑ratio experiment as canonical examples.

   {{PEER-REVIEW}}

5. **The Tier 2 butyrate assay gap identified in the genotype‑informed‑supplement‑quantification workflow creates a methodology bottleneck that applies across *all* future microbiome‑derived metabolite interventions (SCFAs, bile acids, indoles) — the quantification‑ladder framework currently has no validated Tier 2 home assay for any of them, which silently undermines every personalised‑medicine workflow that depends on dose‑verification of microbiome‑produced compounds.**  
   *Supported (by the documented absence of a butyrate colorimetric assay).* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: partial]`

   - *Documents Connected:* `genotype-informed-supplement-workflow.md` (Tier 2 butyrate gap, worked example), `quantification-ladder.md` (the framework that needs a new assay class), `purine-degrading-bacteria.md` (butyrate concentration gap at the enterocyte nucleus), `validation-experiments.md` §1.14 (butyrate dose‑response arm that would provide the Tier 3 GC‑MS anchor).  
   - *Page‑pair linkage:* The butyrate gap is named in `genotype‑informed‑supplement‑workflow.md` but **not** connected to the broader methodological risk that any microbiome‑metabolite intervention (future engineered LBP butyrate‑boost strains, bile‑acid modulators, indole‑based AhR agonists) would face the same quantification bottleneck. The `quantification‑ladder.md` framework does not address the special problem of microbiome‑derived metabolites (where the source is not a supplement batch but an in‑vivo fermentation process).  
   - *Why It Matters:* The platform’s personalised‑medicine thesis (genotype → compound‑selection → batch‑QC → calibrated‑dose → biomarker‑tracking) breaks at the QC step for any intervention whose active molecule is produced *in situ* by gut bacteria. The workflow can verify that the precursor was administered (fiber, resistant starch, probiotic strain), but cannot verify that the downstream metabolite (butyrate) reached the target tissue at the intended concentration — the dose remains an unverified variable, indistinguishable from mechanism‑failure noise. Closing this gap with even *one* validated Tier 2 proxy (e.g., an enzyme‑coupled NADH‑readout butyrate assay calibrated against Tier 3 GC‑MS) would unlock the QC loop for every microbiome‑metabolite intervention the platform ever develops.  
   - *Suggested Action:* Add a dedicated methodology‑gap entry to `quantification‑ladder.md` (new section “Open gap: microbiome‑derived metabolites”) naming the three candidate Tier 2 paths (colorimetric, enzymatic, breath‑hydrogen proxy) and their current validation status. Queue a literature‑first desk audit (PubMed + patent search for “butyrate colorimetric assay” and “butyrate enzymatic assay”) before any wet‑lab development. Cross‑link from `genotype‑informed‑supplement‑workflow.md`.

   {{PEER-REVIEW}}

6. **The Houttuynia cordata polysaccharide (HCP/HCPM) represents the first dual‑CP0+CP1 dietary candidate in the corpus — a widely‑consumed Southeast Asian herb with complement‑inhibitory and NLRP3‑suppressive activity — yet its gout‑specific efficacy has not been tested in any MSU model, and the single‑preparation‑dependent activity (structure‑dependent directionality) creates a consumer‑product caveat that parallels the mushroom β‑glucan structure‑dependence already documented for Ganoderma lucidum.**  
   *Speculative for gout; supported for mechanism.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `upstream-complement-modulator-sweep-computational.md` (comp‑018 Phase 2 Tier 1d), `complement-c5a-gout.md` §9.7 (fourth Tier 1 candidate), `nlrp3-exploit-map.md` §CP1 (new Houttuynia entry), `supplements-stack.md` (new Houttuynia catalog entry).  
   - *Page‑pair linkage:* All references to Houttuynia were added within the **same sweep cluster** (2026‑05‑19 traditional‑name re‑scan). The compound is new to the wiki and has not yet been connected to any downstream validation experiment, biomarker‑tracking protocol, or consumer‑product recommendation.  
   - *Why It Matters:* Houttuynia is the cleanest example of the **query‑framing discipline** that the platform now mandates: it would have been invisible to a “C3 convertase inhibitor” search but is caught by a “Houttuynia cordata anti‑complementary” query. Its dual‑chokepoint coverage (CP0 + CP1) via TLR4‑MD2 partial agonism + complement cascade blockade makes it a uniquely efficient single‑dietary‑agent candidate. However, the **structure‑dependent directionality** (purified 60 kDa HCP‑2 is pro‑inflammatory on naïve PBMCs; the anti‑inflammatory phenotype appears only in disease‑context inflammation) is the same consumer‑product pitfall that the mushroom‑track caveat already warns about — a generic “Houttuynia extract” capsule cannot be assumed equivalent to the Chen‑group HCPM preparation.  
   - *Suggested Action:* The cheapest discriminating experiment is an in‑vitro MSU‑stimulated THP‑1 macrophage assay: HCPM (19.1 kDa Fudan fraction) vs. crude HCP vs. commercial Houttuynia capsule extract, measuring IL‑1β and IL‑6 at dose‑response. Cost: ~$2,000–3,000 for a CRO macrophage assay. Add to `validation-experiments.md` as §1.30. Until this gate is cleared, treat Houttuynia as a “mechanism‑supported, gout‑untested” dietary candidate with an explicit structure‑dependent caveat, parallel to the mushroom β‑glucan structure‑dependence warning already in the corpus.

   {{PEER-REVIEW}}

---

## Contradictions Found

1. **CFH Y402H × dietary supplementation: the predicted beneficial interaction (carriers respond better to upstream‑CP0 dietary candidates) is opposed by the closest empirical analog (CFH × diet × AMD progression), where CFH high‑risk carriers paradoxically *worsened* on zinc/antioxidant supplementation.**  
   Locations: `gout-genetic-variants.md` §Category 5 CFH Y402H row (counter‑evidence flag), `logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md`. Analysis: The AMD paradox may not transfer because the AREDS formulation works *through* CFH‑mediated complement regulation (which Y402H impairs), whereas the OE dietary CP0 candidates (rosmarinic acid, luteolin, Houttuynia) work *upstream of* CFH — they inhibit C3 convertase assembly, a step that does not require functional CFH. The mechanistic dissociation is plausible but untested, and the contradiction should be acknowledged rather than assumed away when proposing CFH‑stratified dietary interventions. *Mechanistic Extrapolation.*  

   {{PEER-REVIEW}}

---

## Proposed Experiments (ranked by insight per cost)

1. **CFH Y402H × dietary polyphenol intake × incident gout — UK Biobank cross‑tabulation via existing gout‑GWAS collaborator.**  
   Cost: $0 (collaboration request). Time: ~3 months. Decides: whether the CFH‑×‑diet interaction hypothesis survives a real‑world association test; negative result would close the question at near‑zero cost. See `gout-genetic-variants.md` §Category 5 CFH row for the full biobank‑mining feasibility analysis.  

   {{PEER-REVIEW}}

2. **MSU‑stimulated THP‑1 macrophage assay of Houttuynia cordata polysaccharide fractions (HCPM vs. crude HCP vs. commercial extract).**  
   Cost: ~$2,000–3,000 (CRO macrophage assay). Time: 4–6 weeks. Decides: whether Houttuynia’s NLRP3‑suppressive and complement‑inhibitory activities translate to a gout‑relevant cell model; distinguishes the Chen‑group purified fraction from generic commercial extracts. See Connection 6 above.  

   {{PEER-REVIEW}}

---

## Open Questions

1. **Can the three‑mechanism acute‑flare protocol (colchicine + topical CBD:THC + DHA‑emphasis omega‑3) be tested as a named n = 1 protocol under the existing self‑experiment framework?** The colchicine arm is Clinical Trial‑grade; the CBD:THC arm is In Vitro/Animal Model with an n = 1 anchor; the DHA/SPM arm is Animal Model with a falsifiable C5a‑decline prediction. The combination is Speculative but compositionally coherent.  

   {{PEER-REVIEW}}

2. **Is there a Tier 2 butyrate assay — colorimetric, enzymatic, or breath‑hydrogen proxy — that can be validated against Tier 3 GC‑MS to close the microbiome‑metabolite quantification gap?** Without it, every future microbiome‑derived intervention (engineered LBP butyrate‑boost, bile‑acid modulators, indole‑based AhR agonists) will face the same QC blind spot. A desk audit of existing assay literature is the $0 first step.  

   {{PEER-REVIEW}}

---

## Priority Actions

1. **Codify “Substrate composition as a cross‑track engineering variable” as a permanent platform‑design principle in `etc/open-source-platform.md`**, citing the SOP‑7 protocol matrix, the methionine‑for‑ergothioneine finding, and the cordycepin‑×‑pentostatin‑ratio experiment as canonical examples. This connects the koji and mushroom tracks at a practical operations layer and gives distributed contributors a lever they can pull without lab access.  

   {{PEER-REVIEW}}

2. **Add the CFH‑×‑dietary‑CP0 biobank‑mining proposal to `gout-action-guide.md`’s “This year (advanced)” section** as the next‑step action for CFH Y402H carriers who want to contribute to platform‑level evidence. The UKB collaboration path (not a solo OE application) should be named explicitly.  

   {{PEER-REVIEW}}

---

## Riskiest Assumption

The chaperone‑orthogonal stacking framework’s α‑coefficients — the transferrin‑lobe coefficient (α = 1.5–2.5) for lactoferrin and the CCP/SCR coefficient (α = 0.3–0.6) for DAF SCR1‑4 — are the single load‑bearing belief in the current platform‑architecture design space that is least supported by the corpus. Every multi‑cassette decision (DAF separate‑strain routing, triple‑cassette feasibility, the endgame strain’s single‑organism thesis) rests on these coefficients, but they were **derived from non‑koji in vitro folding kinetics** (Notari 2023 for lactoferrin, Schmidt 2010 crystallography for CCP domains) and have never been measured in *A. oryzae* solid‑state fermentation. The framework’s own §8 item 6 explicitly names this as the calibration‑uncertainty limitation: “the architecture‑adjusted synergy coefficients are more differentiated than the bulk‑count model but carry the same calibration uncertainty.” The §1.9 + §1.25 paired calibration set — now explicitly mandated under harmonised NSlD‑ΔP10 / solid‑state / matching‑promoter conditions — is designed to resolve this, but until that data lands, the platform is committing architecture decisions on coefficients that could be wrong by 2–3×. The worst‑case outcome (transferrin‑lobe α = 2.5, DAF α = 0.3) collapses triple‑cassette synergy to 0.35, forcing a two‑strain fallback; the best‑case (α = 1.0 for both, in‑vivo ER‑assisted folding) would validate the single‑strain endgame thesis. The gap between those two outcomes is the platform’s architecture risk.  

Citable pages: `chaperone-orthogonal-stacking.md` §3.5.2 (coefficient derivation), §3.5.4 (calibration set design), §8 item 6 (framework’s own calibration‑uncertainty caveat); `koji-endgame-strain.md` §3.3 (capacity‑vs‑titer benchmark ambiguity).

{{PEER-REVIEW}}

## Most Curious Thread

The *Houttuynia cordata* polysaccharide (鱼腥草 / どくだみ) is the most intriguing single thread in this sweep’s corpus: a dietary staple across China, Japan, Korea, and Vietnam that has **published dual‑chokepoint activity** (CP0 complement inhibition, CH50 79–318 µg/mL; CP1 NLRP3 inflammasome suppression, intestinal tight‑junction restoration, and direct TLR4‑MD2 binding) from a single well‑characterised research group (Chen Daofeng / Fudan), yet was **completely invisible** to the platform’s earlier mechanism‑name‑based literature scans. It was surfaced only when the comp‑018 Phase 2 scan switched to traditional‑name + traditional‑pathology query framing — the exact discipline upgrade the corpus now mandates for all natural‑product searches. The compound class (pectic polysaccharide) is orthogonal to everything else in the OE dietary catalogue (flavonoids, terpenoids, nucleotides, peptides), meaning it adds genuinely new chemistry and receptor biology to the platform’s CP0/CP1 coverage. The cheapest discriminating experiment is an in‑vitro MSU‑stimulated macrophage assay (§1.30 in the Connections above), which would either confirm Houttuynia as the platform’s first dual‑CP0+CP1 dietary candidate or rule it out cleanly. Multi‑vendor signal: I suspect another sweep model would converge on this pick — the combination of dietary accessibility, dual‑chokepoint novelty, mechanism‑class orthogonality, and the serendipity of its discovery makes Houttuynia a paradigmatic example of what the daemon is optimised to find.

{{PEER-REVIEW}}

---

## Sources cited

- `wiki/gout-genetic-variants.md`
- `wiki/complement-c5a-gout.md`
- `wiki/upstream-complement-modulator-sweep-computational.md`
- `wiki/upstream-complement-verification-rerun-computational.md`
- `wiki/lactoferrin-linker-redesign-computational.md`
- `wiki/etc/bio-ai-tools.md`
- `wiki/chaperone-orthogonal-stacking.md`
- `wiki/validation-experiments.md`
- `wiki/daf-cd55-scr14-truncated-computational.md`
- `wiki/colchicine.md`
- `wiki/cannabinoids-terpenes.md`
- `wiki/spm-resolution-pathway.md`
- `wiki/nlrp3-exploit-map.md`
- `wiki/gout-action-guide.md`
- `wiki/medicinal-mushroom-complement-track.md`
- `wiki/medicinal-mushroom-extract-sops.md`
- `wiki/koji-home-fermentation.md`
- `wiki/engineered-koji-protocol.md`
- `wiki/genotype-informed-supplement-workflow.md`
- `wiki/quantification-ladder.md`
- `wiki/purine-degrading-bacteria.md`
- `wiki/supplements-stack.md`
- `wiki/etc/open-source-platform.md`
- `wiki/self-experiment-protocol.md`
- `wiki/koji-endgame-strain.md`
