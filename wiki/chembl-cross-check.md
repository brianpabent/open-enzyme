---
title: "ChEMBL Cross-Check: Stack Compounds vs Curated Bioactivity"
date: 2026-04-24
tags: ["ChEMBL", "rigor", "bioactivity", "cross-check", "NLRP3", "off-targets", "polypharmacology"]
related:
  - nlrp3-inhibitor-screen.md
  - nlrp3-exploit-map.md
  - nlrp3-inflammasome.md
  - supplements-stack.md
  - bhb-ketones.md
  - kpv-peptide.md
  - cannabinoids-terpenes.md
  - synthesis.md
sources:
  - "EMBL-EBI ChEMBL v34 (queried via Anthropic life-sciences MCP, 2026-04-24)"
  - "Eur J Med Chem 2018: Resveratrol DPP-4 inhibition"
  - "Eur J Med Chem 2024: Berberine TDO inhibition"
  - "J Nat Prod 2020: Curcumin human NLRP3 IC50"
  - "J Med Chem 2007: EGCG Plasmodium ENR"
  - "J Med Chem 1991: Quercetin 5-LOX"
---

# ChEMBL Cross-Check: Stack Compounds vs Curated Bioactivity

## Purpose

This is a **standing rigor page** that cross-references every NLRP3/gout-relevant compound discussed in the Open Enzyme wiki against the EMBL-EBI ChEMBL v34 curated bioactivity database. The goal: separate "direct inhibitor of target X" claims (supported by a curated binding/inhibition IC50 in a named assay) from "pathway modulator" claims (functional downstream readouts, mechanism inferred from review literature).

**TCM lineage note:** Several compounds in this cross-check table have explicit TCM materia medica lineage — berberine (*Coptis chinensis* / Huang Lian 黄连), EGCG (green tea / Lu Cha 绿茶), resveratrol (*Polygonum cuspidatum* / Hu Zhang 虎杖), curcumin (turmeric / Jiang Huang 姜黄), oridonin (*Rabdosia rubescens* / Dong Ling Cao 冬凌草). The ChEMBL cross-check discipline is one of the six rules in the TCM × modern rigor methodology lens formalized at [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md) — rule #2 specifically. The cross-check results here (e.g., berberine's most potent curated activity is TDO at 30 nM, not NLRP3; resveratrol's is DPP-4 at 0.6 nM, not SIRT1) are exactly the kind of "ChEMBL surprise" that the TCM rigor methodology is designed to surface. (source: tcm-modern-rigor-intersection.md)

Quercetin's 5-LOX finding — surfaced during the 2026-04-23 sweep of [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) — is the template: a compound the wiki frames primarily as an NLRP3 pathway inhibitor actually has its single most potent curated activity on a different enzyme (5-LOX, IC50 300 nM), and that target is relevant to gout biology (leukotriene B4 drives neutrophil chemotaxis in MSU flares). Whenever a similar gap shows up, it goes here first, then propagates to the primary concept page on a follow-up sweep.

**NLRP3 target ID (reference):** CHEMBL1741208 (*NACHT, LRR and PYD domains-containing protein 3*, Homo sapiens, UniProt Q96P20).

**Refresh cadence:** Quarterly, or whenever a new direct NLRP3 inhibitor clinical program publishes pivotal data. Next refresh target: 2026-07-24.

**How to refresh:** See the three-line recipe in the [Appendix](#appendix-refresh-recipe) at the bottom of this page.

---

## Master Cross-Check Table

| # | Compound | ChEMBL ID | Most potent curated target + IC50/Ki | Wiki's current framing | Discrepancy? | Last refreshed |
|---|---|---|---|---|---|---|
| 1 | **Quercetin** | CHEMBL50 | **5-lipoxygenase: IC50 = 300 nM** (*J Med Chem* 1991) | NLRP3 pathway modulator (IL-1β in MSU model) | **YES** — 5-LOX is stronger and gout-relevant (LTB4 neutrophil chemotaxis); not surfaced in exploit map | 2026-04-23 |
| 2 | **Oridonin** | CHEMBL1164920 | Human NLRP3: **IC50 = 5.18 μM** (THP-1, *Eur J Med Chem* 2023) | "0.5–2 μM" covalent Cys279 binder | **YES** — curated human cellular IC50 is 5.18 μM; the 0.5–2 μM number comes from cell-free / mouse-derived assays | 2026-04-23 |
| 3 | **Dapansutrile (OLT1177)** | CHEMBL3989943 | Human NLRP3: **IC50 = 1.0 μM** human MDM; **IC50 = 1 nM mouse J774A.1** | Direct NLRP3 ATPase inhibitor, Phase 2a gout success | **YES** — 1000× mouse-vs-human potency gap; clinical efficacy is consistent with human μM potency, not sub-nM | 2026-04-23 |
| 4 | **β-Caryophyllene** | CHEMBL445740 | No direct human NLRP3 in ChEMBL; CB2 agonist Ki ~155 nM from external literature | CB2 agonist + NLRP3/caspase-1/TLR4 suppressor (MSU gout, rat) | Partial — "direct NLRP3 binding" claim from 2021 docking paper not confirmed by ChEMBL curation; CB2 agonism is well-established | 2026-04-23 |
| 5 | **BHB (beta-hydroxybutyrate)** | CHEMBL1162496 | **No curated bioactivity with pChEMBL ≥ 6** against any target | "Direct NLRP3 signaling molecule; hits CP1/CP2/CP3" | **Soft** — BHB's "direct NLRP3 binding" is from Youm et al. 2015 *Nat Med*, not represented in ChEMBL; also no off-target red flags — it is genuinely a signaling metabolite, not a high-affinity ligand | 2026-04-24 |
| 6 | **KPV (tripeptide)** | **Not indexed** | — (peptide below ChEMBL small-molecule threshold; no salt/synonym match) | Direct NLRP3 assembly inhibitor + NF-κB stabilizer via PepT1 uptake | N/A — peptides of this size are poorly covered by ChEMBL; absence is not a discrepancy, but wiki should note "not small-molecule-curated" | 2026-04-24 |
| 7 | **Carnosine** | CHEMBL242948 | ROR-γ potency 2.24 μM (qHTS, inconclusive); SH-SY5Y neuroprotection EC50 3 μM | NLRP3/NF-κB/p-JNK suppressor; URAT1/GLUT9 downregulator (hyperuricemia rat) | **Soft** — no curated high-potency activity anywhere; the direct hyperuricemia evidence (Zhang et al. 2024) is functional, not represented | 2026-04-24 |
| 8 | **Ursolic acid** | CHEMBL169 | **No curated activity with pChEMBL ≥ 6**; zero direct human NLRP3 entries | NLRP3/NF-κB suppressor (triterpene), OA + Kawasaki animal models | **Soft** — wiki framing comes entirely from functional IL-1β readouts; ursolic acid has 0 ChEMBL-curated high-affinity targets despite being a Tier-1 candidate | 2026-04-23 |
| 9 | **Taurine** | CHEMBL239243 | BLM helicase (qHTS, *inconclusive*) potency 12.6 nM; taurine transporter EC50 10 μM (substrate) | NLRP3 K⁺-efflux-block upstream (sepsis, cardiac animal models) | **Soft** — no curated direct NLRP3 or pathway-target; BLM hit is qHTS noise flagged "inconclusive"; TauT substrate is physiological, not a drug activity | 2026-04-24 |
| 10 | **EGCG** | CHEMBL297453 | **Plasmodium falciparum enoyl-ACP reductase: Ki = 8 nM** (*J Med Chem* 2007); human 20S proteasome chymotrypsin IC50 86 nM; DNMT inhibition Ki 28 nM | TLR4/NF-κB/NLRP3 cascade blocker; ROS reduction | **YES** — strongest curated target is an anti-malarial enzyme; **20S proteasome inhibition (IC50 86 nM) is a human off-target not surfaced** in NLRP3 screen and matters for safety at high oral doses | 2026-04-24 |
| 11 | **Sulforaphane** | CHEMBL48802 | **iNOS IC50 = 400 nM** (mouse RAW, *J Med Chem* 2015); **Nrf2/Keap1 EC50 = 580 nM** (human U2OS, *J Med Chem* 2019) | Nrf2 activator → NLRP3 priming block; xanthine oxidase + 5-LOX | No discrepancy — curated potency lines up with wiki's Nrf2/iNOS framing; the XO and 5-LOX claims in supplements-stack.md are functional, not ChEMBL-curated, but are consistent | 2026-04-24 |
| 12 | **Berberine** | CHEMBL295124 | **Tryptophan 2,3-dioxygenase: IC50 = 30 nM** (*Eur J Med Chem* 2024); CYP1B1 Ki 44 nM; AChE IC50 100 nM | AMPK activator / gut metabolism / SIBO modulator / NLRP3 | **YES** — top curated activity is TDO (kynurenine pathway), then CYP1B1 (estrogen metab) and AChE — none reflected in current wiki; TDO especially relevant because kynurenine modulates T-cell/NLRP3 crosstalk | 2026-04-24 |
| 13 | **Resveratrol** | CHEMBL165 | **Dipeptidyl peptidase-4: IC50 = 0.6 nM** (human, *Eur J Med Chem* 2018, pChEMBL 9.22) | SIRT1 activator / mitochondrial homeostasis / weak NLRP3 | **YES** (large) — DPP-4 at sub-nM is resveratrol's single strongest curated activity; DPP-4 is a validated anti-diabetic target (gliptins) and the wiki frames resveratrol purely through SIRT1; this is a new mechanism worth surfacing | 2026-04-24 |
| 14 | **Curcumin** | CHEMBL140 | **Amyloid-β precursor protein: Ki = 0.208 nM** (*J Med Chem* 2006); **NLRP3 human THP-1 IC50 = 24.2 μM** (*J Nat Prod* 2020, pChEMBL 4.62) | Direct NLRP3 pathway inhibitor (MSU gout animal model) | **YES** — curcumin IS curated against human NLRP3 (24.2 μM), making it the 3rd compound in this screen with direct human NLRP3 data (after dapansutrile, oridonin). But its most potent curated activity is amyloid-β binding, and the NLRP3 IC50 (24.2 μM) is 5× weaker than even the oridonin human-cell IC50 (5.18 μM) | 2026-04-24 |
| 15 | **Ergothioneine** | **Not indexed** | — (name search and SMILES similarity both return zero) | Potent antioxidant / ROS scavenger / indirect NLRP3 suppression | N/A — ergothioneine's absence from ChEMBL is consistent with its unusual sulfur-containing betaine structure; the wiki's "indirect via ROS" framing is appropriate | 2026-04-24 |
| 16 | **Ferulic acid** | CHEMBL32749 | Amyloid fibril binding Ki = 0.77 nM (*Bioorg Med Chem Lett* 2007, [¹²⁵I]TZDM displacement — imaging ligand); carbonic anhydrases Ki 2–10 μM | Autophagy induction + caspase-1 blocker (NLRP3 pathway) | **Soft** — the 0.77 nM amyloid binding is an imaging-probe displacement Ki, not functional inhibition; wiki framing is fine, but ferulic acid's curated potency profile is weak in absolute terms | 2026-04-24 |
| 17 | **Kojic acid** | CHEMBL287556 | Tyrosinase IC50 7–10 μM (mushroom + human) | Antioxidant + melanin synthesis inhibitor (cosmetic); NLRP3 untested | No discrepancy — curated tyrosinase data match wiki's cosmetic/melanin framing; NLRP3 silence in wiki is honest | 2026-04-24 |

**Legend:**
- **YES** — wiki materially mis-states or omits a target that ChEMBL curation supports at a comparable or better potency than the wiki's current framing; propagate to the primary concept page.
- **Soft** — no strong curated signal one way or the other; the wiki's functional/animal-model framing is defensible, but worth noting that ChEMBL does not have direct binding/inhibition data to back it up.
- **No discrepancy** — wiki framing and ChEMBL data converge on the same target class and potency range.
- **N/A / Not indexed** — compound is not in ChEMBL (peptides, unusual structures); absence is not evidence of weakness, just outside the database's scope.

---

## Expanded Findings: Compounds with Propagation-Worthy Discrepancies

### Resveratrol → DPP-4 inhibition (sub-nM, curated)

**Evidence Level:** In Vitro (curated ChEMBL entry)

**Finding:** Resveratrol (CHEMBL165) has a curated human DPP-4 IC50 of **0.6 nM** (pChEMBL 9.22, *Eur J Med Chem* 2018). This is the single strongest curated activity in resveratrol's entire ChEMBL bioactivity profile — stronger than any of its reported SIRT1, Nrf2, or quinone reductase activities, and stronger than the approved gliptin class of DPP-4 inhibitors (sitagliptin IC50 ~19 nM).

**Current wiki framing:** [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) frames resveratrol as a "stilbenoid polyphenol; non-covalent NLRP3 binding; primary mechanisms: mitochondrial integrity preservation, SIRT1-dependent autophagy." No mention of DPP-4.

**Suggested reframing:** Add a mechanism note to [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) Tier 2 entry: "Resveratrol's single most potent ChEMBL-curated human activity is DPP-4 inhibition (IC50 = 0.6 nM, pChEMBL 9.22, *Eur J Med Chem* 2018) — a validated type-2 diabetes target. This does not directly improve the gout case, but flags resveratrol as mechanistically more similar to the gliptin class than to SIRT1 activators at physiologically achievable concentrations. If resveratrol is co-administered, DPP-4 inhibition may contribute to glucose homeostasis effects independent of SIRT1." Also worth a note in [gout-deep-dive.md](./gout-deep-dive.md) given the gout-T2D comorbidity cluster.

**Caveat:** The 2018 DPP-4 paper is a single curated entry; replication in independent labs would strengthen the claim. But the datum itself (human enzyme, purified protein, standard Gly-Pro-AMC substrate, pChEMBL 9.22) is high-confidence.

---

### Berberine → Tryptophan 2,3-dioxygenase (TDO, sub-100 nM)

**Evidence Level:** In Vitro (curated ChEMBL entry)

**Finding:** Berberine (CHEMBL295124) has a curated TDO IC50 of **30 nM** (*Eur J Med Chem* 2024, pChEMBL 7.52), and a curated CYP1B1 Ki of 44 nM (*Eur J Med Chem* 2017), and AChE IC50 of 100 nM (*Bioorg Med Chem* 2015). All three are sub-100 nM against human targets, all three are medicinal-chem quality data.

**Current wiki framing:** Berberine appears in [nlrp3-exploit-map.md](./nlrp3-exploit-map.md), [nlrp3-inflammasome.md](./nlrp3-inflammasome.md), [sibo.md](./sibo.md), [gut-lumen-sink.md](./gut-lumen-sink.md), [digestive-enzymes.md](./digestive-enzymes.md) — almost always framed as "AMPK activator / gut antimicrobial / dysbiosis modulator / NLRP3 suppressor." TDO, CYP1B1, and AChE are not mentioned.

**Suggested reframing:** TDO is the most interesting because tryptophan → kynurenine metabolism sits at the T-cell / NLRP3 / inflammation crossroads, and TDO inhibition has been explored as an adjunctive immuno-oncology and anti-inflammatory strategy. Add a mechanism note to [nlrp3-inflammasome.md](./nlrp3-inflammasome.md) under berberine: "ChEMBL-curated TDO IC50 = 30 nM (*Eur J Med Chem* 2024) places berberine's strongest validated target at the kynurenine-pathway entry point, not AMPK. This is consistent with berberine's broader anti-inflammatory phenotype and may partially explain its NLRP3-downstream effects (kynurenine metabolites modulate aryl hydrocarbon receptor signaling, which crosstalks with NF-κB priming)." The CYP1B1 inhibition is a drug-drug-interaction flag worth noting in [supplements-stack.md](./supplements-stack.md).

---

### EGCG → 20S proteasome (IC50 86 nM, human)

**Evidence Level:** In Vitro (curated ChEMBL entry, replicated across two papers)

**Finding:** EGCG (CHEMBL297453) has a curated human 20S proteasome chymotrypsin-like activity IC50 of **86 nM** (*Bioorg Med Chem* 2010, confirmed in *Eur J Med Chem* 2019, both pChEMBL 7.07). It also has sub-30 nM activity against *Plasmodium falciparum* enoyl-ACP reductase (Ki = 8 nM, *J Med Chem* 2007) and DNMT1 (Ki = 28 nM), but the human proteasome hit is the most translationally relevant.

**Current wiki framing:** EGCG in [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) is framed as a "green tea catechin; suppresses ROS-driven NLRP3 activation; direct binding to NLRP3 and/or TLR4." No mention of proteasome.

**Suggested reframing:** 20S proteasome inhibition is a double-edged datapoint. On one hand, proteasome inhibitors (bortezomib, carfilzomib) are cancer drugs with significant cardiotoxicity and neuropathy profiles at clinical doses. On the other hand, EGCG's proteasome hit is ~100× weaker than bortezomib's, and dietary EGCG exposure is orders of magnitude below therapeutic proteasome-inhibitor plasma levels. Still: add a safety note to [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) and [supplements-stack.md](./supplements-stack.md) that high-dose EGCG (>800 mg/day) is a known hepatotoxicity risk (EMA 2018), and the sub-100-nM proteasome activity is a plausible contributing mechanism that should be factored into dose-ceiling recommendations.

---

### Curcumin → human NLRP3 IC50 = 24.2 μM (curated)

**Evidence Level:** In Vitro (curated ChEMBL entry — rare for a natural product)

**Finding:** Curcumin (CHEMBL140) has a **curated direct human NLRP3 IC50 of 24.2 μM** in LPS-primed PMA-differentiated THP-1 cells with nigericin challenge (*J Nat Prod* 2020, pChEMBL 4.62). This makes curcumin the **third compound** in the entire Open Enzyme stack with a ChEMBL-curated direct human NLRP3 number, after dapansutrile (1.0 μM) and oridonin (5.18 μM). Its strongest curated activity overall is amyloid-β Ki = 0.208 nM (*J Med Chem* 2006), which is a well-known off-target and the basis for curcumin's Alzheimer's-research positioning.

**Current wiki framing:** [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) Tier 3 entry cites "In vitro: Curcumin (10–50 μM) blocked MSU-induced NLRP3 inflammasome assembly and IL-1β secretion." This is consistent with the curated 24.2 μM IC50.

**Suggested reframing:** Minor — update the Tier-3 entry to cite the specific curated human NLRP3 IC50 (24.2 μM, THP-1, pChEMBL 4.62, *J Nat Prod* 2020) and rank curcumin's NLRP3 potency relative to dapansutrile and oridonin: curcumin is **24× weaker than dapansutrile** and **5× weaker than oridonin** in the same human cellular assay format. Combined with curcumin's ~5% oral bioavailability, the functional gout-arthritis animal data probably reflects very high local GI/portal exposure more than systemic NLRP3 block.

---

### Quercetin → 5-LOX (300 nM, already documented in 2026-04-23 sweep)

Already propagated in [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) appendix. Listed here for continuity and as the reference template for the other expanded sections above.

---

## Compounds Not Indexed in ChEMBL

| Compound | Reason | Implication |
|---|---|---|
| **KPV (Lys-Pro-Val)** | Tripeptide below ChEMBL's small-molecule curation focus; no salt/synonym match | Absence does not indicate weakness — the [peptide-gout-addendum.md](./peptide-gout-addendum.md) framing (direct NLRP3 + NF-κB, PepT1-transported) is from peptide-pharmacology literature not in ChEMBL's scope. Note in wiki: "KPV is not small-molecule-curated; mechanistic claims rest on α-MSH fragment pharmacology papers." |
| **Ergothioneine** | Name search and SMILES similarity both return zero hits | Ergothioneine is a sulfur-containing trimethylammonium betaine; its unusual structure and physiological (rather than drug-like) pharmacology likely explain the absence. The wiki's "indirect ROS scavenger" framing in [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) is honest and appropriate. |
| **β-Caryophyllene** | Present as CHEMBL445740 but zero direct human NLRP3 entries | See [2026-04-23 sweep](./nlrp3-inhibitor-screen.md#appendix-chembl-ic50-cross-check-2026-04-23). CB2 agonism is well-established; the "direct NLRP3 binding" claim from 2021 docking is not ChEMBL-curated. |

**These absences are the single most important meta-observation from this cross-check:** a large fraction of the Open Enzyme stack is not represented in ChEMBL with direct binding/inhibition data, because the database is curated for medicinal-chemistry lead compounds, not nutraceuticals, peptides, or endogenous metabolites. This is neither surprising nor damning — but it does mean that **the evidence base for most stack compounds is functional (cell/animal IL-1β readouts, downstream markers), not biochemical (Kd/IC50 on purified protein)**. Any claim of "direct NLRP3 inhibitor" for a stack compound should be treated with the same two-tier labeling introduced in the 2026-04-23 sweep:

1. **Direct NLRP3 inhibitor (binding/inhibition IC50 curated):** dapansutrile, oridonin, curcumin, MCC950 (per external literature), tranilast (per external literature).
2. **NLRP3 pathway modulator (functional IL-1β reduction):** everything else in the stack.

---

## Implications for the Platform Thesis

1. **"Koji-yeast hybrid" engineering logic is unchanged.** Ursolic acid and quercetin remain the top microbial-production candidates; this ChEMBL cross-check doesn't invalidate production feasibility or functional efficacy. It does clarify that the mechanism claims are pathway-level, not direct-binding.

2. **Resveratrol's DPP-4 activity opens a gout-diabetes comorbidity angle.** Gout and T2D cluster strongly (shared hyperuricemia, insulin resistance, NLRP3-driven inflammation). If resveratrol is included in a formulation, the DPP-4 contribution should be explicit, and drug-drug interactions with clinical DPP-4 inhibitors flagged.

3. **Berberine's TDO + CYP1B1 profile is a drug-interaction flag.** SIBO patients on berberine alongside NLRP3-modulating or CYP-metabolized drugs (many common) should have the CYP1B1 hit noted. Kynurenine-pathway modulation is also worth flagging in any future biomarker panel.

4. **EGCG dose-ceiling should factor in proteasome activity.** Existing hepatotoxicity concerns at high-dose green tea extract (EMA 2018, 800 mg/day threshold) are consistent with sub-100 nM human 20S proteasome inhibition. Any supplementation protocol should stay well below that threshold.

5. **BHB, ursolic acid, carnosine, taurine, ferulic acid all come up "soft"** — no ChEMBL-curated high-affinity target. This is *not* a negative finding; it reflects the database's small-molecule medicinal-chemistry focus. But it does reinforce that these compounds' inclusion in the stack rests entirely on **functional IL-1β / hyperuricemia / animal-model data**, not on biochemical target engagement. The wiki already states this correctly in most places.

---

## Appendix: Refresh Recipe

```text
# 1. Get the NLRP3 target ID (stable)
target_search(gene_symbol="NLRP3", organism="Homo sapiens")   # → CHEMBL1741208

# 2. Per compound: find ChEMBL ID
compound_search(name="<compound>")                             # → molecule_chembl_id

# 3. Per compound: direct NLRP3 check
get_bioactivity(molecule_chembl_id=<ID>,
                target_chembl_id="CHEMBL1741208",
                activity_type="IC50")

# 4. Per compound: top off-target scan (what is this compound actually most potent against?)
get_bioactivity(molecule_chembl_id=<ID>, min_pchembl=6, limit=10)

# 5. If target of interest is known:
get_bioactivity(molecule_chembl_id=<ID>, target_chembl_id=<target>)
```

**Interpretation rules:**
- pChEMBL ≥ 7 (100 nM or better) against a human target with assay_type="B" = treat as a real biochemical target.
- pChEMBL 5–7 with "Inconclusive" activity_comment or "qHTS" in assay description = PubChem HTS noise; discount.
- Zero bioactivities against NLRP3 (CHEMBL1741208) = "NLRP3 pathway modulator" not "NLRP3 inhibitor" — apply the two-tier labeling.
- Zero curated bioactivities anywhere above pChEMBL 6 = compound is primarily supported by functional/animal data; state this explicitly in wiki framing.

**Refresh cadence:** Quarterly. Next refresh: **2026-07-24**.

---

## Sources

- EMBL-EBI ChEMBL v34 database, accessed via Anthropic life-sciences MCP plugin, 2026-04-24.
- Resveratrol DPP-4: *Eur J Med Chem* 2018 (CHEMBL4229387 assay; pChEMBL 9.22).
- Berberine TDO: *Eur J Med Chem* 2024 (CHEMBL5617618 assay; pChEMBL 7.52).
- Berberine CYP1B1: *Eur J Med Chem* 2017 (CHEMBL4035349 assay; pChEMBL 7.36).
- EGCG 20S proteasome: *Bioorg Med Chem* 2010 and *Eur J Med Chem* 2019 (CHEMBL4433382 assay; pChEMBL 7.07).
- EGCG *P. falciparum* ENR: *J Med Chem* 2007 (CHEMBL910789 assay; pChEMBL 8.10).
- Curcumin human NLRP3: *J Nat Prod* 2020 (CHEMBL4702878 assay; pChEMBL 4.62).
- Curcumin amyloid-β: *J Med Chem* 2006 (CHEMBL907197 assay; pChEMBL 9.68).
- Sulforaphane iNOS: *J Med Chem* 2015 (CHEMBL3579718 assay; pChEMBL 6.40).
- Sulforaphane Nrf2/Keap1: *J Med Chem* 2019 and *Eur J Med Chem* 2020 (pChEMBL 6.06–6.24).
- Kojic acid tyrosinase: *Bioorg Med Chem Lett* 2008–2014 (multiple curated entries; pChEMBL 5.00–5.13).
- Ferulic acid amyloid fibril imaging: *Bioorg Med Chem Lett* 2007 (CHEMBL888360; pChEMBL 9.11, imaging probe displacement).
- Quercetin 5-LOX: *J Med Chem* 1991 (see [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) 2026-04-23 appendix).
- Oridonin human NLRP3 THP-1: *Eur J Med Chem* 2023 (see same appendix).
- Dapansutrile human/mouse NLRP3: *Eur J Med Chem* 2023 and *Bioorg Med Chem Lett* 2021 (same appendix).
