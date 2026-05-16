# comp-027 inputs — provenance

All inputs grep-verified against primary sources per `wiki/manual-literature-mining.md` §Pre-commit verification gate. Bounded estimates flagged inline. Fetch date: 2026-05-16.

## pk_data.json — disulfiram + DETC plasma pharmacokinetics

Compartmental PK at oral dosing. Sources:

- **Lee et al. 2018** — *Population Pharmacokinetics and Pharmacodynamics of Disulfiram on Inducing Latent HIV-1 Transcription in a Phase 2b Trial* — Clin Pharmacol Ther 105(3):692-702. PMID 30137649. DOI [10.1002/cpt.1220](https://doi.org/10.1002/cpt.1220). Doses 500/1000/2000 mg PO daily × 3 days. Median cumulative AUC_72h: 3,420 / 8,942 / 23,834 mg·hr/L (sum across all five analytes — parent + 4 metabolites). DSF apparent clearance 0.53 L/hr (CV 36%); apparent Vd ~1.3 L; absorption rate constant 0.08 hr⁻¹; half-life ~7 hr; non-linear elimination above 1000 mg (CYP2E1/3A4 saturation). DSF bioavailability 80-95% (text).
- **Johansson & Stankiewicz 1989** — *Inhibition of erythrocyte ALDH and elimination kinetics of Me-DDC and Me-DTC after disulfiram* — Eur J Clin Pharmacol 37(2):133-8. PMID 2551696. DOI [10.1007/BF00558220](https://doi.org/10.1007/BF00558220). Single 400 mg PO disulfiram → mean Me-DDC tmax 1.8 h, t1/2 6.3 h; mean Me-DTC tmax 3.3 h, t1/2 11.2 h. Mean peak plasma Me-DTC = 278 nmol/L (0.278 μM) at 400 mg dose. DER (disulfiram-ethanol reaction) clinically observed at 100, 200, 300 mg doses with ethanol challenge — Me-DTC steady-state plasma was dose-proportional within and across groups.
- **Palatty & Saldanha 2011** — *Status of disulfiram in present day alcoholic deaddiction therapy* — Indian J Psychiatry. PMC3056183. **125 mg PO once-daily for 60 days in 51 patients** — well-tolerated, 76.5% completed full course; ADR profile (drowsiness 27%, tiredness 21%, skin 7.8%); ALT/AST elevations mild. Confirms sub-AUD dosing is clinically feasible. Low-dose disulfiram showed good adherence and reduced adverse effects.
- **Faiman 1989** — *Comparative aspects of disulfiram and its metabolites in the DER in the rat* — Biochem Pharmacol 38(3):413-21. PMID 2537080. DOI [10.1016/0006-2952(89)90380-8](https://doi.org/10.1016/0006-2952(89)90380-8). **DER hypotension threshold = blood acetaldehyde 110 μM, requires ~40% ALDH inhibition.** Me-DTC (DDTC-Me) is the active alcohol-deterrent metabolite; identical ALDH-inhibition kinetics across DSF / DDTC / DDTC-Me.

Bioavailability anchor: 80-95% per Lee 2018 (consistent with Hoffmaster 1980s PK literature).

## ec50_data.json — GSDMD blockade + NLRP3 pathway EC50 data

- **Hu et al. 2020** — *FDA-approved disulfiram inhibits pyroptosis by blocking gasdermin D pore formation* — Nat Immunol 21(7):736-745. PMID 32367036. PMC7316630. DOI [10.1038/s41590-020-0669-6](https://doi.org/10.1038/s41590-020-0669-6). **Liposome (cell-free) GSDMD pore-formation IC50: 0.3 μM** (single concentration in titration, range 0.01-50 μM tested). **Cellular pyroptosis IC50: 0.02 μM (20 nM) after 1-h preincubation**, ~24-fold lower than naive cellular IC50. C191A GSDMD mutant: IC50 ~8-fold higher than wildtype, confirming covalent Cys191 mechanism. Disulfiram allows GSDMD cleavage by caspase-1 to proceed; blocks only pore oligomerization.
- **Xu, Pickard, Núñez 2024** — *FDA-approved disulfiram inhibits the NLRP3 inflammasome by regulating NLRP3 palmitoylation* — Cell Rep 43:114609. PMC11398858. DOI [10.1016/j.celrep.2024.114609](https://doi.org/10.1016/j.celrep.2024.114609). Cellular NLRP3 inhibition (BMDMs, ATP-stimulated): **partial at 10 μM, complete at 30-50 μM disulfiram** (caspase-1 p20 + GSDMD processing readout). Mechanism: covalent modification of NLRP3 Cys126 blocking palmitoylation → loss of TGN localization. Upstream of Hu 2020's GSDMD-Cys191 mechanism. In vivo: 50 mg/kg IP × 2 doses in mice → reduced IL-1β in LPS, Salmonella, MSU (gout) peritonitis.
- **Asiri et al. 2025** — *Targeting Hyperuricemia and NLRP3 Inflammasome in Gouty Arthritis: A Preclinical Evaluation of Allopurinol and Disulfiram Combination Therapy* — PMC12114764. **50 mg/kg PO daily × 9 days** in Wistar rat MSU-gout model → significant reduction in paw swelling, IL-1β, TNF-α, IL-6, serum urate (combination > allopurinol monotherapy). Limitation noted in their paper: "single, relatively high dose; future investigations should explore dose-response relationships."
- **Deng et al. 2020** — *Disulfiram suppresses NLRP3 inflammasome activation to treat peritoneal and gouty inflammation* — Free Radic Biol Med 156:57-69. PMID 32561321. DOI 10.1016/j.freeradbiomed.2020.03.007. (Cited via Asiri 2025; not full-text grep-verified here. Treated as secondary evidence.)

## der_threshold_data.json — alcohol-deterrent threshold

- **Faiman 1989** (above): DER hypotension acetaldehyde threshold = **110 μM blood acetaldehyde**, requires **~40% ALDH inhibition**.
- **Johansson 1989** (above): clinically valid DER reactions at oral DSF 100, 200, 300 mg dose challenges in human volunteers. Me-DTC steady-state concentration scales linearly with dose at this dose range.
- DSF + ethanol clinical text (Antabuse FDA label, Hoffmaster Drug Metab Dispos historical): standard 250 mg/day DSF + 14 g ethanol (1 standard drink) produces moderate DER symptoms; severity scales with both DSF dose and ethanol load.

## di_landscape.json — bundled drug-interaction set

Sources: `wiki/disulfiram.md` lines 117-145 (synthesized from supplements-stack.md 2026-04-26 grep-verified entries); FDA Antabuse label (https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/008891s029lbl.pdf via supplement-stack canonical citations). Categories captured:

1. **DER-stacking agents** (additive disulfiram-like reactions): metronidazole, tinidazole, cefoperazone, griseofulvin, isoniazid, certain MAOIs.
2. **CYP-mediated PK interactions** (DSF inhibits CYP2E1, CYP3A4, CYP1A2):
   - Warfarin (CYP2C9 + 3A4) → INR ↑
   - Phenytoin (CYP2C9) → toxicity risk
   - Theophylline, caffeine (CYP1A2) → ↓ clearance
   - Benzodiazepines metabolized by CYP3A4 (alprazolam, midazolam) → sedation
3. **Gout-relevant pharmacology co-administration**:
   - **Allopurinol** — synergistic anti-inflammatory effect in Asiri 2025 rat gout model; no major DI reported (allopurinol is metabolized by XO to oxypurinol; DSF doesn't significantly alter XO).
   - Colchicine — no specific DI reported; both can cause GI side effects; share hepatic stress profile.
   - Probenecid — uricosuric; competes for OAT-mediated renal excretion. DSF metabolites (DDC) renally excreted; minor interaction theoretically plausible, not clinically documented.
   - NSAIDs — additive hepatic / GI stress.
4. **Ethanol stacking from incidental sources**: kombucha, koji-fermented foods (>0.1% residual ethanol), some IV/elixir formulations with ethanol vehicle. Critical at AUD-dosing; effectively irrelevant at GSDMD-only dose if ALDH inhibition <40%.

## formulation_data.json — extended-release / micronization context

Sources: MINX precedent referenced in `wiki/compounding-pharmacy-track.md` (lipid-matrix ER tablets developed via AI-aided formulation review); USP <711> dissolution standards; standard pharmaceutical references for disulfiram (Antabuse is immediate-release; no commercial ER formulation as of 2026).

- Disulfiram: poor aqueous solubility (~0.4 mg/L water); micronization increases dissolution rate ~3-5x.
- Lipid-matrix ER (HPMC, glyceryl behenate): extends absorption window, lowering Cmax but maintaining AUC.
- 503A compounding pharmacies (PCCA, Empower, Olympia) routinely compound ER formulations of off-label-dose drugs.

## human_dose_scaling.md — animal → human dose scaling

- Standard FDA allometric scaling: rat dose × (rat_BW / human_BW)^0.33 × correction for species.
- For rat 50 mg/kg PO → human equivalent dose (HED): 50 mg/kg × (60 kg / 0.2 kg)^(-0.33) ≈ 8 mg/kg × 60 kg ≈ **480 mg human-equivalent** (close to standard 500 mg AUD dose). Approximate; published FDA HED conversion factor for rat is /6.2 → 50/6.2 = 8 mg/kg × 60 kg = 480 mg, same answer.
- Caveat: PK varies considerably between rats and humans (rat oral DSF BA ~30%, human ~80-95%); plasma concentrations are NOT linearly scaled. Better anchor: match human plasma [DSF + DETC] to the in vitro / cellular effective concentration directly.
