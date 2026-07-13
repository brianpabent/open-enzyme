---
title: "Lit scan — CBD vs flavonoid gut-luminal metabolic stability (ABCG2-inhibition premise stress-test)"
date: 2026-07-13
tags: [lit-scan, abcg2, gut-lumen-sink, curcumin, quercetin, egcg, cbd, luminal-stability, bioaccessibility]
scope: Resolve the discriminating variable (gut-luminal metabolic stability) behind the "poor bioavailability ⇒ high functional luminal concentration ⇒ real ABCG2 inhibition" premise
status: complete — reported to Brian; NOT propagated to wiki (report-only scan)
---

# CBD vs flavonoid gut-luminal metabolic stability — does the ABCG2-inhibition premise hold?

**Question.** `wiki/abcg2-modulators.md` (§"supplements-stack contradiction") + `wiki/supplements-stack.md` flag quercetin, curcumin, EGCG as functional intestinal-ABCG2 inhibitors risky to the gut-lumen-sink platform, resting on the premise: poorly absorbed ⇒ reaches a HIGH functionally-relevant luminal concentration ⇒ real ABCG2 inhibition. `wiki/cannabinoids-terpenes.md` line ~73 concluded the OPPOSITE for CBD (poorly absorbed, but not retained as active drug in lumen). Discriminating variable = **gut-luminal metabolic stability**: does an active form survive to reach the ABCG2-efflux surface above its inhibition threshold?

**Method.** bio-research MCP: PubMed (`search_articles`, `get_article_metadata`), Consensus (`search`). No language gate. All load-bearing claims line-anchored to primary source below. No wiki edits, no commit.

---

## Load-bearing findings (per compound)

### CBD (cannabidiol)
- **Not actually an ABCG2 story** — CBD's mechanism in the corpus is P2X7/NLRP3 (upstream), not ABCG2 functional inhibition. It is the *analogy* the flavonoid premise is being tested against ("poor bioavailability ≠ high functional luminal conc").
- **Acid-labile in the STOMACH, not the colon.** In simulated gastric fluid (with SDS surfactant) CBD degraded ~85% at 60 min and >98% at 120 min (first-order, k = −0.031 min⁻¹), cyclizing to Δ9-/Δ8-THC. **CBD in physiological (neutral) buffer control did NOT convert.** Merrick et al. 2016, *Cannabis Cannabinoid Res* — PMID 28861485, [DOI](https://doi.org/10.1089/can.2016.0004).
- Gastric CBD degradation is surfactant-catalyzed and formulation-dependent (only water-soluble products; no conversion without anionic surfactant). Kumagai et al. 2025, *Chem Pharm Bull* (Consensus; PMID lookup pending).
- Review consensus: CBD is chemically unstable in acidic environments + extensively PRESYSTEMICALLY (host CYP) metabolized; low oral bioavailability is driven by physicochemical unavailability (lipid sequestration / poor solubilization) and host metabolism. Šitovs et al. 2024, *J Drug Deliv Sci Technol* (review).
- **Direct evidence of colonic MICROBIAL degradation of CBD is thin.** The microbiome literature shows CBD *modulates* the microbiota (He 2023; Geng 2024 CIA) and that microbiota can metabolize cannabinoids (THC noted; Al-Khazaleh 2024 review) — but no clean "CBD is degraded to inactive forms by colonic bacteria" primary datum. The wiki's line-73 mechanism ("majority likely degraded in the colon") is itself an extrapolation; the better-supported mechanisms for low free luminal CBD are lipid sequestration + gastric acid degradation + host metabolism.

### Quercetin
- Dietary quercetin is largely **glycosides** → require bacterial β-glucosidase **deglycosylation** as the obligate first step (glucosides partly absorbed proximally; rutinosides reach colon). Jaganath et al. 2009, *Free Radic Biol Med* (rutin: deglycosylation is initial step, then catabolism) — via Consensus.
- Aglycone then undergoes **C-ring fission + dehydroxylation to simple phenolic acids** (3-hydroxyphenylacetic acid, 3-(3-hydroxyphenyl)propionic acid, 3,4-dihydroxyphenylacetic acid). Rechner et al. 2004, *Free Radic Biol Med* — PMID 14744633 ("extensive metabolism of dietary polyphenols in the colon… small number of phenolic degradation products"). Di Pede et al. 2020, *Foods* (native quercetin time-dependently degraded by fecal microbiota → phenylpropanoic/phenylacetic/benzoic acid derivatives).
- **Quercetin IS a genuine ABCG2/BCRP inhibitor** — le Roux-Pullen et al. 2025, *Toxicol In Vitro* PMID 40796067 (quercetin >30% inhibition of human BCRP; apigenin/kaempferol Ki <0.1 µM as class context); Fleisher et al. 2014, *J Pharm Sci* PMID 25418056 (quercetin inhibits BCRP-mediated efflux at 50 µM).
- **Net:** high FREE aglycone concentration is achievable in the **proximal** small intestine immediately post-supplement-dose (real acute inhibition window), but the parent does **not** survive to the colon intact — it is deglycosylated + ring-fissioned to weak phenolic acids.

### Curcumin
- **Chemically unstable at neutral/alkaline pH** and extensively **biotransformed by colonic microbiota** to tetrahydro-/hexahydrocurcumin + demethyl catabolites. Bresciani et al. 2020, *Molecules* PMID 32093121 (curcumin/DMC/bis-DMC metabolized by colonic microbiota within 24 h → bis(demethyl)-hexahydrocurcumin etc.); Luo (Minna) et al. 2024, *Food Chem* + Luo (Fudi) et al. 2025, *JAFC* (microbiota-dependent biotransformation; microbiota also *protects* curcumin from non-microbial degradation and deconjugates back to bioactive forms).
- **BUT — demonstrated IN VIVO selective intestinal BCRP/ABCG2 inhibitor.** Karibe et al. 2018, *Drug Metab Dispos* PMID 29358184, [DOI](https://doi.org/10.1124/dmd.117.078931): oral curcumin markedly elevated oral AUC/bioavailability of the BCRP substrates sulfasalazine and rosuvastatin in cynomolgus monkeys with minimal change in systemic clearance (i.e., intestinal-lumen-side ABCG2 inhibition), selective vs P-gp. Corroborated mechanistically by Ge et al. 2015, *Pharm Res* PMID 26502886 (curcumin inhibits BCRP + MRP2 in vivo/in vitro).
- **Net:** despite chemical instability + colonic biotransformation, enough parent acts on intestinal ABCG2 to produce a real in vivo functional-inhibition signal at oral doses. Strongest "premise holds" case.

### EGCG
- **Unstable at intestinal pH.** EGCG (and its epimer GCG) are not stable in pH 7.4 buffer or DMEM/F12 at 37 °C; degrade to gallocatechin + gallic acid (+ autoxidation to theasinensins). Wu et al. 2019, *J Sci Food Agric* PMID 31215023.
- **Small-intestinal:** rapidly methylated/sulfated; effluxed principally via **MRP2, not BCRP** (Kikuchi et al. 2022, *J Nutr Biochem* — via Consensus).
- **Colonic:** "promptly degraded" by human fecal microbiota via ester hydrolysis → C-ring opening → A-ring fission → dehydroxylation → phenolic acids (4-phenylbutyric acid, dihydroxyphenylpropionic acids). Liu et al. 2020, *J Agric Food Chem* PMID 32808768.
- **In vivo the net ABCG2 phenotype is FAVORABLE, not inhibitory** — Yu et al. 2024, *Food Funct* PMID 38757391 (corpus; HUA mouse net-favorable ABCG2/URAT1/GLUT9), mirrored by theaflavins (Tai 2020). Provisional Nrf2-inducer bucket per `abcg2-modulators.md`.
- **Net:** parent does not persist; in vivo effect is favorable. Most OVERSTATED premise of the three flavonoids.

### ABCG2-metabolite note
Simple gut phenolic-acid catabolites of quercetin/EGCG are generally weak/non-inhibitors of ABCG2, though some phenolic acids retain activity (e.g., propyl gallate, sinapic acid, ellagic acid inhibit ABCG2 — Tan et al. 2013, *Food Chem*). Gallic acid (EGCG catabolite) is a borderline case. This does not rescue the premise: the potent parent species are the ones that degrade.

---

## Verdict table

| Compound | Gut-microbial/chemical fate | Active parent to colon > ABCG2 threshold? | Verdict |
|---|---|---|---|
| CBD | Lipid-sequestered (low free luminal); acid-labile in stomach (→THC), stable in neutral buffer; extensive host metabolism; direct colonic-microbial degradation weakly evidenced | No (and not an ABCG2 inhibitor anyway) | **Premise fails / OVERSTATED** — conclusion right, wiki's "microbial degradation" mechanism mislabeled |
| Quercetin | Glycoside → bacterial deglycosylation → C-ring fission to phenolic acids; parent extensively catabolized in colon | Proximal SI: yes (real acute window). Colon: no | **MIXED** — holds acutely/proximally, overstated for colonic/sustained |
| Curcumin | Chemically unstable at neutral pH; colonic biotransformation to THC-curcumin/hexahydro/demethyl | Functionally yes — in vivo selective intestinal BCRP inhibitor in primates (Karibe 2018) | **Premise HOLDS** (strongest) |
| EGCG | Unstable at pH 7.4; SI methyl/sulfate + MRP2 efflux; colonic ring-fission to phenolic acids; in vivo net-favorable ABCG2 | No — parent doesn't persist; in vivo favorable | **Premise most OVERSTATED** |

**Stability spectrum (as an ABCG2-relevant active parent, most→least gut-stable):**
Curcumin (functionally survives enough to inhibit in vivo) > Quercetin (survives proximally, degraded distally) > EGCG (rapidly degraded; in vivo favorable) ≈ CBD (sequestered/acid-labile; not an ABCG2 inhibitor).

**Does the CBD "gets degraded" conclusion generalize to the flavonoids?** Partially to **EGCG** (both rapidly transformed, both in vivo favorable/neutral). **Not to curcumin** (in vivo primate inhibitor — the counterexample). Partially to **quercetin** (colonic degradation real, but a genuine proximal-gut inhibition window exists that CBD lacks).

---

## Biggest evidence gap
No study measures the actual **free luminal concentration** of any of these four compounds **along the gut** (segment-resolved) after a realistic supplement dose AND tests it against **urate** efflux (not a drug substrate) via intestinal ABCG2. Karibe 2018 used sulfasalazine/rosuvastatin, not urate; the in vivo HUA-mouse EGCG data measure net transporter *expression*, not acute luminal inhibition. The load-bearing quantity — [free compound]_lumen vs Ki(ABCG2-for-urate) at each gut segment — is unmeasured for all four. This is exactly `abcg2-modulators.md` open-question #4 (EGCG) generalized to the whole flavonoid set.

## Queries run
PubMed: quercetin/curcumin/EGCG/CBD × {colonic microbial metabolism, glycoside deglycosylation, intestinal stability/pH degradation, ABCG2/BCRP inhibition IC50/Ki, fecal excretion}. Consensus: curcumin/EGCG/quercetin/CBD gut-degradation survival questions + phenolic-acid-metabolite ABCG2 activity. Multi-term PubMed auto-AND suppressed recall on several runs; simpler 2–4-word queries used. No non-English source produced a load-bearing datum that Western-indexed primary sources didn't already cover (curcumin/EGCG microbial-metabolism literature is heavily Chinese-authored but published in English-language JAFC/Food Chem — no translation cross-check triggered).

## Primary sources (PMID / DOI)
- Merrick 2016 CBD SGF degradation — PMID 28861485, DOI 10.1089/can.2016.0004
- Rechner 2004 colonic polyphenol ring fission — PMID 14744633
- Jaganath 2009 rutin catabolism; Di Pede 2020 quercetin fecal metabolism (Foods) — Consensus
- Bresciani 2020 curcuminoid colonic metabolism — PMID 32093121
- Luo 2024 (Food Chem); Luo 2025 (JAFC) curcumin microbiota biotransformation — Consensus
- Karibe 2018 curcumin in vivo intestinal BCRP inhibitor (primate) — PMID 29358184, DOI 10.1124/dmd.117.078931
- Ge 2015 curcumin BCRP/MRP2 — PMID 26502886
- Wu 2019 GCG/EGCG instability pH 7.4 — PMID 31215023
- Liu 2020 EGCG colonic ring-fission — PMID 32808768
- Kikuchi 2022 EGCG MRP2 efflux (SI) — Consensus
- le Roux-Pullen 2025 phytochemical BCRP Ki — PMID 40796067
- Fleisher 2014 quercetin BCRP inhibition 50 µM — PMID 25418056
- Tan 2013 phenolic-acid ABCG2 inhibitors — Food Chem (Consensus)
- Yu 2024 EGCG in vivo favorable ABCG2 (HUA mouse) — PMID 38757391 (corpus)
