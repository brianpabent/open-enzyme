---
title: "Focused scan — disulfiram × PDB-butyrate CYP/PK interaction (deferred synthesis card resolution)"
date: 2026-07-13
tags: [disulfiram, butyrate, SCFA, CYP2E1, CYP3A4, GSDMD, pyroptosis, pharmacokinetics, gout, scan-log]
scan_type: focused-pharmacology-lit-scan
status: resolved
---

# Scan log: does PDB-derived butyrate modulate disulfiram's CYP metabolism / GSDMD blockade?

**Purpose.** Resolve a deferred synthesis card claiming that disulfiram's GSDMD-pore blockade
"may be synergistically enhanced by PDB-derived butyrate via metabolic-pathway modulation" —
specifically that butyrate (HDAC-inhibitor SCFA from purine-degrading gut bacteria) could alter
the hepatic CYP enzymes that metabolize disulfiram, changing its effective dose / safety window.
Corpus had **zero** pages on any butyrate × CYP interaction → "do the work, don't accept
corpus-absence" case.

**Method.** PubMed (via NCBI eutils / MCP), EuropePMC-class metadata, Consensus. Domain is
Western hepatocyte-pharmacology / drug-metabolism → English-language primary literature is the
right corpus; East-Asian sources not forced (per brief; low expected yield). No non-English
source was load-bearing, so the two-model translation cross-check did not trigger. Every
load-bearing number below is grep-verified against a named primary source (PMID + DOI).

**Attribution.** Findings drawn from PubMed-indexed literature; DOIs given per source.

---

## Q1 — Does butyrate/SCFA modulate disulfiram-relevant CYPs (CYP2E1, CYP3A4)?

First, establish disulfiram's actual CYP relationship (verify, don't take on faith):

- **Disulfiram is a mechanism-based INHIBITOR of CYP2E1, not primarily a CYP2E1 substrate.**
  In vivo human confirmation:
  - Ryu 2007, *J Nucl Med* — single oral disulfiram 500 mg inhibited CYP2E1-mediated
    defluorination of ¹⁸F-FCWAY by **~70%** in humans; effect attributed entirely to CYP2E1
    inhibition. PMID 17574977, doi:10.2967/jnumed.107.039933.
  - Doroshyenko 2009, *Cancer Epidemiol Biomarkers Prev* — disulfiram 500 mg single dose used
    as the CYP2E1-blockade arm in a human crossover toxicokinetic trial. PMID 19190172,
    doi:10.1158/1055-9965.EPI-08-0832.
  - Hazai 2002, *BBRC* — human liver microsomes: disulfiram IC₅₀ **8 µM**, diethyldithiocarbamate
    (DDC) IC₅₀ **33 µM** against CYP2E1-mediated NAPQI formation. PMID 11866476,
    doi:10.1006/bbrc.2002.6541.
  - Palmer 2013, *Med Hypotheses* — disulfiram inhibits CYP2E1 at conventional therapeutic
    dosages. PMID 23363738, doi:10.1016/j.mehy.2013.01.011.
  - Background (textbook, not grep-anchored here): disulfiram bioactivation to the CYP2E1-inactivating
    metabolite DETC-MeSO runs through DDC → S-methyl-DDC → CYP3A4-mediated oxidation. So the CYP the
    card should care about is CYP2E1 (target of disulfiram) with CYP3A4 as a bioactivation route —
    NOT a set of enzymes that "clear" disulfiram in a rate-limiting way.

Butyrate/SCFA effects on those CYPs:

- **CYP3A4 — modest induction, immature-model context.** Mun 2021, *Cells* — an
  acetate+propionate+butyrate mixture (**1 µM each**) increased CYP3A4 activity, expression and
  albumin in iPSC-derived liver organoids; propionate was the main CYP3A4/CYP3A7-ratio driver.
  This is metabolic **maturation** of fetal-like organoids, not induction in mature liver.
  In vitro (organoid). doi:10.3390/cells10010126 (Consensus ref).
- **CYP1A / AhR — induction via HDAC inhibition.** Jourová 2022, *J Nutr Biochem* — butyrate
  dose-dependently upregulated AhR and AhR target genes (CYP1A family) in HepG2-C3 and in primary
  human hepatocytes; AhR-dependent, epigenetic (HDAC-inhibition) mechanism. In vitro / primary
  human hepatocytes. doi:10.1016/j.jnutbio.2022.108944 (Consensus ref). (Concentration not stated
  in abstract; butyrate HDAC inhibition classically needs ~0.5–5 mM — see Q2 exposure gap.)
- **CYP2E1 — no evidence of butyrate (SCFA) modulation.**
  - Zangar & Novak 1997, *Arch Biochem Biophys* — in primary rat hepatocytes, ketone bodies and
    fatty acids regulate CYP2B but **NOT** CYP2E1. PMID 9016816, doi:10.1006/abbi.1996.9785.
  - CAUTION / do-not-conflate: the two papers that DO show CYP2E1 up-regulation use β-hydroxybutyrate
    (a ketone body, ≠ SCFA butyrate) and palmitate (a long-chain FA), not butyrate:
    Peng 2019 *J Dairy Res* (BHB ↑ CYP2E1 in cow hepatocytes, PMID 30732670,
    doi:10.1017/S0022029919000025); Raucy 2004 *Toxicol Sci* (palmitate ↑ CYP2E1 mRNA in human
    hepatocytes but ethanol did not raise CYP2E1 protein — "isolated hepatocytes may not be an
    adequate tool", PMID 15056802, doi:10.1093/toxsci/kfh126).
  - Csikó 2014, *J Vet Pharmacol Ther* — dietary sodium butyrate in chickens ↑ avian CYP2H1,
    ↓ CYP3A37 in vitro; authors conclude co-administration with CYP substrates is **"unlikely to
    cause clinically significant feed-drug interaction."** Avian. PMID 24628435, doi:10.1111/jvp.12109.
- Direct butyrate→CYP2E1 regulation paper: **none found** (targeted query returned 0).
- Direct butyrate × disulfiram interaction/co-administration study: **none found** (query returned 0).

**Q1 verdict:** Butyrate can modestly **induce** some hepatic CYPs (CYP1A via AhR/HDAC; CYP3A4 in
immature organoids) but there is **no evidence it materially modulates CYP2E1**, the enzyme
disulfiram actually targets. Evidence tier: **in vitro only**, small magnitude, partly in fetal-like
models. Not a validated modulation of a disulfiram-rate-limiting CYP.

---

## Q2 — Does gut-derived butyrate reach the liver at those concentrations? (exposure reality)

- **Colonocytes are the primary butyrate sink.** Gasaly 2021, *IJMS* — butyrate oxidation supplies
  **70–80%** of mature-colonocyte energy requirements; consumed locally, generating epithelial
  hypoxia. (The "~95%" heuristic is directionally right; 70–80% is the better-anchored figure.)
  doi:10.3390/ijms22063061 (Consensus ref). Martínez-Ruiz 2025 *Crit Rev Food Sci Nutr* concordant
  (Consensus ref).
- **Human portal-vein data — the liver DOES see butyrate, but extracts most first-pass:**
  - Neis 2016, *PLoS One* — direct portal/hepatic-vein/arterial sampling in 30 patients: gut
    produces butyrate at 9.5 ± 2.6 µmol·kg⁻¹·h⁻¹; hepatic butyrate uptake ~9.9–11.5 µmol·kg⁻¹·h⁻¹;
    **arterial (systemic) butyrate only 4.3 → 3.6 µmol/L.** Liver clears acetate/propionate/butyrate
    from portal blood. PMID 27835668, doi:10.1371/journal.pone.0166161.
  - van der Beek 2015, *J Nutr* — rectal butyrate enema → **portal butyrate peak 92.2 ± 27.0 µmol/L**
    at 5 min (vs 14.3 placebo), but **hepatic uptake prevented any rise in systemic butyrate**;
    splanchnic release ≈ 0. "Hepatic Uptake of Rectally Administered Butyrate Prevents an Increase in
    Systemic Butyrate Concentrations in Humans." PMID 26156796, doi:10.3945/jn.115.211193.
  - Wang & Mackay 2023, *JACI* (editorial) — frames high **portal** metabolite (incl. SCFA)
    concentrations vs low systemic as the mechanism for gut-microbiota→liver effects. PMID 37992816,
    doi:10.1016/j.jaci.2023.10.029.
  - Caveat on "high serum butyrate": Chen 2018 *Ann Clin Biochem* reports serum "FA 4:0" 162 µmol/L
    but **98.2% esterified** — free butyrate is low; do not cite 162 as free systemic butyrate.
    PMID 30185055, doi:10.1177/0004563218801393.
- **Exposure synthesis:** systemic/arterial free butyrate ≈ **3–4 µM** (low). Hepatocytes are
  exposed to **portal** butyrate ≈ 10–30 µM baseline, transiently up to ~90 µM after heavy colonic
  delivery. So the liver's butyrate exposure (portal) exceeds the 1 µM used in the organoid CYP3A4
  study — BUT the HDAC-mediated induction effects (CYP1A/AhR) classically require ~0.5–5 mM
  butyrate, which is **not reached even in portal blood**. The one reachable in-vitro effect (1 µM
  organoid CYP3A4) is a maturation phenomenon in fetal-like tissue, small, and not a mature-liver
  induction signal.

**Q2 verdict:** Gut-derived butyrate is **largely exposure-limited at the liver for CYP-modulation
purposes.** Systemic butyrate is very low; portal butyrate reaches tens of µM but stays 2–3 orders
of magnitude below the mM range where butyrate's HDAC-mediated hepatic CYP effects operate. The
in-vitro biology is real but the exposure needed to translate it to disulfiram-relevant CYP change
is not physiologically reached.

---

## Q3 — Any DIRECT pharmacodynamic butyrate × GSDMD or butyrate × disulfiram interaction?

- **Disulfiram's GSDMD action is a direct covalent event, CYP-independent.** Hu et al. 2020,
  *Nat Immunol* — disulfiram covalently modifies human **Cys191 / mouse Cys192** in GSDMD at
  **nanomolar** concentration, blocking pore formation (not IL-1β/GSDMD processing). PMID 32367036,
  doi:10.1038/s41590-020-0669-6. A stoichiometric covalent warhead at nM is **insensitive to modest
  CYP shifts** in parent-drug clearance.
- **Butyrate's own effect on GSDMD/pyroptosis is separate, upstream, and bidirectional:**
  - Anti-pyroptotic: Wu 2022, *Mil Med Res* — propionate (C3) and butyrate (C4) suppress GSDMD-NT
    generation, caspase-1/IL-1β cleavage and NLRP3 activation in wear-particle osteolysis; via
    HDAC / GPR41/43/109A. PMID 35996168, doi:10.1186/s40779-022-00404-0. Concordant: Wu 2020,
    *Mol Med Rep* (butyrate-producer *R. intestinalis* flagellin ↓ NLRP3/pyroptosis, PMID 32700754,
    doi:10.3892/mmr.2020.11351).
  - Pro-inflammasome (context-dependent): Park 2023, *Cell Death Discov* — butyrate + bacterial LTA
    **synergistically enhances** caspase-1/IL-1β and GSDMD cleavage via HDAC inhibition. PMID 36977666,
    doi:10.1038/s41420-023-01404-2.
  - Mechanism site: butyrate acts on inflammasome **assembly/priming** (NLRP3, ASC, caspase-1) and
    HDAC — **not** on the GSDMD pore-formation step that disulfiram covalently blocks.
- No study couples butyrate to disulfiram or to disulfiram's GSDMD blockade (0 hits).

**Q3 verdict:** No direct PD interaction on GSDMD or on disulfiram is documented. The card's
"synergistically enhanced GSDMD blockade" is **speculative**. Butyrate and disulfiram both touch the
inflammasome→pyroptosis axis but at different nodes (butyrate = upstream priming, bidirectional;
disulfiram = terminal GSDMD pore), and there is no CYP link between them.

---

## Bottom line

The card conflates three separable pharmacologies: (a) butyrate's HDAC/AhR effects on hepatic CYPs,
(b) disulfiram's CYP2E1 inhibition, and (c) disulfiram's covalent GSDMD-Cys191 blockade — fusing
them into a "CYP-mediated PD synergy" that the literature does not support.

**The PDB + disulfiram stack is PK-clean by default on the butyrate × CYP axis:** gut-derived
butyrate does not reach the liver at concentrations that would materially modulate disulfiram-relevant
CYPs (systemic butyrate ~3–4 µM; portal tens-of-µM; HDAC-mediated hepatic CYP effects need ~mM),
disulfiram's therapeutic GSDMD action is a nanomolar stoichiometric covalent modification insensitive
to modest CYP shifts, and disulfiram is itself a CYP2E1 *inhibitor* rather than a CYP2E1 substrate —
so no butyrate-driven dosing caveat is warranted on the mechanism the card proposed. (Disulfiram's own
CYP2E1/CYP3A/ALDH inhibition remains its established DDI profile, independent of butyrate.)

## Evidence-tier summary

| Question | Verdict | Direction | Best tier |
|---|---|---|---|
| Q1 butyrate → disulfiram-relevant CYP | No material CYP2E1 effect; modest CYP1A/CYP3A induction only | Induce (CYP1A/3A) | In vitro / organoid |
| Q2 gut butyrate reaches liver at effective conc. | Exposure-limited for CYP modulation | — | Human portal-vein (clinical) |
| Q3 direct butyrate × GSDMD/disulfiram PD synergy | Not supported; speculative | Butyrate bidirectional, upstream | In vitro + animal |

## Queries run (provenance)

PubMed: `butyrate CYP2E1 cytochrome P450 hepatocyte expression` (8); `butyrate CYP3A4 hepatocyte`
(29); `short chain fatty acids portal blood concentration humans` (56); `disulfiram CYP2E1 inhibition
diethyldithiocarbamate metabolism cytochrome P450` (27); `disulfiram gasdermin D GSDMD pyroptosis`
(68); `butyrate gasdermin D pyroptosis inflammasome` (5); `disulfiram inhibits gasdermin D pore
formation pyroptosis FDA-approved` (5); `butyrate disulfiram co-administration drug interaction` (0);
`short chain fatty acid butyrate CYP2E1 regulation liver microbiome drug metabolism` (0).
Consensus: butyrate/SCFA × hepatic CYP3A4/CYP2E1; colonocyte 95% butyrate consumption.

## Key PMIDs / DOIs

- 32367036 — Hu 2020 Nat Immunol — disulfiram → GSDMD Cys191, nM — doi:10.1038/s41590-020-0669-6
- 17574977 — Ryu 2007 J Nucl Med — disulfiram 500mg ~70% CYP2E1 inhibition (human) — doi:10.2967/jnumed.107.039933
- 19190172 — Doroshyenko 2009 — disulfiram 500mg CYP2E1 blockade (human) — doi:10.1158/1055-9965.EPI-08-0832
- 11866476 — Hazai 2002 — disulfiram IC₅₀ 8µM / DDC 33µM vs CYP2E1 (microsomes) — doi:10.1006/bbrc.2002.6541
- 23363738 — Palmer 2013 — disulfiram inhibits CYP2E1 at therapeutic doses — doi:10.1016/j.mehy.2013.01.011
- 9016816 — Zangar & Novak 1997 — FA/ketones regulate CYP2B not CYP2E1 (rat) — doi:10.1006/abbi.1996.9785
- 15056802 — Raucy 2004 — palmitate ↑ CYP2E1 mRNA; hepatocyte-model caveat — doi:10.1093/toxsci/kfh126
- 30732670 — Peng 2019 — BHB (ketone, ≠ SCFA) ↑ CYP2E1 (cow) — doi:10.1017/S0022029919000025
- 24628435 — Csikó 2014 — dietary butyrate, no clinically significant CYP DDI (chicken) — doi:10.1111/jvp.12109
- Mun 2021 Cells — SCFA mix (1µM) ↑ CYP3A4 in iPSC liver organoids — doi:10.3390/cells10010126
- Jourová 2022 J Nutr Biochem — butyrate ↑ AhR/CYP1A via HDAC (primary human hepatocytes) — doi:10.1016/j.jnutbio.2022.108944
- 27835668 — Neis 2016 PLoS One — human portal SCFA; arterial butyrate 4.3→3.6 µM — doi:10.1371/journal.pone.0166161
- 26156796 — van der Beek 2015 J Nutr — portal butyrate 92µM peak, hepatic uptake blocks systemic rise — doi:10.3945/jn.115.211193
- 37992816 — Wang & Mackay 2023 JACI — portal>systemic metabolite gradient — doi:10.1016/j.jaci.2023.10.029
- 30185055 — Chen 2018 — serum butyrate 98% esterified — doi:10.1177/0004563218801393
- 35996168 — Wu 2022 Mil Med Res — C3/C4 ↓ GSDMD-NT/pyroptosis — doi:10.1186/s40779-022-00404-0
- 36977666 — Park 2023 — butyrate + LTA ↑ GSDMD cleavage (HDAC) — doi:10.1038/s41420-023-01404-2
- 32700754 — Wu 2020 — butyrate-producer ↓ NLRP3/pyroptosis — doi:10.3892/mmr.2020.11351
- Gasaly 2021 IJMS — colonocyte butyrate oxidation 70–80% energy — doi:10.3390/ijms22063061
