# comp-020 — Search log (audit trail)

This is the audit trail of Paperclip MCP and WebSearch queries run for this experiment, in order of execution. Each row documents the query, the tool, and the result count or notable hits surfaced. Together with `outputs/per-node-findings.md`, this lets a reviewer reproduce the search trail or extend it.

## Paperclip MCP queries

| # | Query | Result count | Notable hits |
|---|---|---|---|
| 1 | "natural product C1q classical pathway inhibitor" -n 10 | 10 | C1qNb75 nanobody (PMC7396675); Helicteres angustifolia (PMC6273495); Bupleurum polysaccharides ELISA (PMC4629277); Anticomplementary multiherb SARS (PMC7126446); PIC1 peptide (PMC4141160) |
| 2 | "complement factor B inhibitor natural compound" -n 10 | 10 | Factor B small-molecule (PMC6475383); Schubart review of low-MW AP inhibitors (PMC10092480); Factor D therapeutic strategy (PMC8458797); danicopan / iptacopan papers |
| 3 | "anticomplementary natural product CH50 alternative pathway" -n 10 | 10 | Marine algae polysaccharide structure-activity (PMC4728500); Floridoside CP-activator (PMC2579733); reinforces Helicteres + multiherb hits |
| 4 | "Bupleurum polysaccharide complement inhibition" -n 8 | 8 | Bupleurum C3c ELISA paper (PMC4629277); Ligusticum chuanxiong polysaccharide (PMC6155779); Bupleurum LPS-TLR4 (PMC3805517); thrombospondin-1 / FH synergy (bio_a432c55080e4) |
| 5 | grep "CH50\|AP50\|IC50\|μM\|mM" /papers/PMC7126446/content.lines | n/a | **Load-bearing data extracted:** Zhang & Chen 2008 Table 1 with CH50/AP50 for all 15 compounds; luteolin 0.19/0.17 mM, rutin 0.58/0.42, quercetin 0.50/1.02 etc. |
| 6 | grep "CH50\|AP50\|IC50\|μM\|mM" /papers/PMC6273495/content.lines | n/a | **Load-bearing data extracted:** Yin 2016 with Helicteres compound 4 (machicendonal): CH50 0.040 mM AP50 0.105 mM. Compound 5 (dihydrodehydrodiconiferyl alcohol): CH50 0.009 mM AP50 0.021 mM. |
| 7 | "Factor H mimetic upregulation natural" -n 8 | 8 | Mini-FH constructs (PMC8696033, PMC4650264); Factor H reviews (PMC4030870, PMC10894998). NO natural-product Factor H upregulator hit. |
| 8 | "MASP-2 inhibitor compound complement lectin" -n 8 | 8 | TFPI1-derived MASP-2 inhibitor (PMC6527154); MASP-2 heparin-binding (PMC7212410); MASP-2 selective small-molecule (PMC12037010 — EVO24L) |
| 9 | grep "IC50\|fucoidan\|heparin\|μg/mL" /papers/PMC4728500/content.lines | n/a | **Load-bearing data extracted:** marine fucoidan IC50 table: SJS 4.51, SJW 7.26, HFS 24.65, HFW 5.51, ANW 0.98, SJW-3 3.11 μg/mL |
| 10 | grep "IC50\|μg/ml\|heparin" /papers/PMC7212410/content.lines | n/a | **Load-bearing data extracted:** Talsma 2020 heparin IC50 table: LP 2 / CP 39 / AP 76 μg/mL. Tetrasaccharide LP-selective 21 μg/mL. Hexasaccharide 4 μg/mL LP. Octasaccharide 3 μg/mL LP. |
| 11 | "rosmarinic acid complement inhibition" -n 5 | 5 | Multiple rosmarinic acid reviews (PMC9143754, PMC8989115, PMC7059186); none had primary IC50 → escalated to WebSearch |
| 12 | "ginsenoside complement classical pathway" -n 5 | 5 | Ginseng polysaccharide C4 biosynthesis enhancement (PMC8461058 — INVERSE direction, immunostimulatory not inhibitory); Rg3 C1q reduction in depression model (PMC12594608) |
| 13 | "saponin Bupleurum saikosaponin complement" -n 5 | 5 | Saikosaponin reviews (PMC6130612, PMC7126585) — broad immunomodulation; not direct upstream complement IC50 |
| 14 | "K76 monoascus complement inhibitor fungus" -n 5 | 5 | Monascus pigments (PMC11877510) antioxidant/antimicrobial; fumagillin (PMC7020470) targets MetAP2 not complement. **Confirms fungal-natural-product gap on direct complement modulation** |
| 15 | "EGCG epigallocatechin complement classical pathway" -n 5 | 5 | EGCG broad reviews; no primary anti-complement IC50 found in matched format |
| 16 | "FDA-approved drug heparin nafamostat complement inhibitor" -n 8 | 7 | Schubart 2022 review (PMC10092480); MASP-2 heparin paper (PMC7212410); small-molecule Factor B inhibitor (PMC6475383) |
| 17 | "iptacopan factor D inhibitor approval" -n 5 | 5 | Danicopan oral Factor D inhibitor (PMC8634185); iptacopan synthesis (PMC11124358); aHUS Factor D inhibition (PMC8222914) |
| 18 | "fucoidan polysaccharide complement inhibition sulfated" -n 5 | 5 | Reinforces marine algae structure-activity (PMC4728500); fucoidan therapy review (PMC3210604); fucoidan microbead coagulation/inflammation (PMC11783016 — caution flag) |
| 19 | grep "IC50\|μg/mL\|complement fixation" /papers/PMC6155779/content.lines | n/a | **Load-bearing data extracted:** Ligusticum chuanxiong LCP-I-I ICH50 26.3 ± 2.2 μg/mL |
| 20 | "compstatin natural complement C3 inhibitor" -n 5 | 5 | Compstatin peptide engineering (PMC4306506, PMC5082644); C3 epitope-specific inhibition (PMC11910092); reaffirms compstatin/pegcetacoplan as engineered, not natural |
| 21 | "andrographolide curcumin baicalein complement" -n 6 | 6 | Andrographolide reviews (PMC9551308, PMC3619690) — broad anti-inflammatory but no direct upstream complement IC50; curcumin DYRK kinase target |
| 22 | "Eucommia ulmoides anti-complementary polysaccharide" -n 4 | 4 | Eucommia leaf polysaccharide network pharmacology (PMC10001223); reviews (PMC11361956). Activity exists but not the primary IC50 paper |
| 23 | "tanshinone Salvia complement inhibition" -n 5 | 5 | Salvia tanshinones / salvianolic acids reviews (PMC10975292) — broad immune regulation but no matched-format IC50 |
| 24 | "rosmarinic acid C5b9 anaphylatoxin in vivo" -n 5 | 5 | Rosmarinic acid asthma model (PMC6274450) anti-inflammatory; reviews. Confirms in vivo activity profile. |
| 25 | "kampo Sho-saiko-to anti-complement" -n 5 | 5 | Sho-saiko-to (TJ-9) IL-12 modulation in cirrhosis (PMC2276037); not direct complement IC50 |
| 26 | "MAC C5b-9 inhibitor natural product membrane attack complex" -n 8 | 8 | CD59 / disulphide-locked C9 / horse C9 (PMC12500384); engineered protein inhibitors. No natural-product MAC inhibitor surfaced. |
| 27 | "CD55 DAF expression upregulation natural compound" -n 5 | 5 | CD55 reviews (PMC4618202, PMC5833118); KLF4-CD55 reciprocal regulation (PMC10884306). NO natural-product CD55 upregulator surfaced. |
| 28 | "properdin inhibitor natural polysaccharide" -n 5 | 5 | Properdin reviews (PMC5096056, PMC3547370); low-properdin CV mortality (PMC12074774 — caution). NO natural-product properdin direct modulator surfaced. |

## WebSearch queries

| # | Query | Notable result |
|---|---|---|
| W1 | "CNKI WanFang luteolin rutin anti-complement CH50 sheep erythrocyte hemolytic assay 2024 2025" | Did not return primary-paper IC50 from Chinese databases in time budget. **Phase 2 follow-up flagged.** |
| W2 | "rosmarinic acid C5 convertase complement IC50 hemolytic in vivo allergic" | **Load-bearing data extracted via search snippets:** Sahu 1999 Biochem Pharmacol (PMID 10353266): C3b covalent IC50 34 μM, CP hemolysis 180 μM, AP hemolysis 160 μM, C5 convertase 1500 μM. Peake 1991 PMID 1761351 + Englberger 1988 PMID 3198307 = supporting earlier literature. In vivo activity 3 models. |

## Summary statistics

- Total Paperclip MCP search/grep queries: 28
- Total WebSearch queries: 2
- Unique primary papers grep-verified for load-bearing IC50: 6 (PMC7126446, PMC6273495, PMC4728500, PMC7212410, PMC4629277, PMC6155779)
- Unique compounds with at least one IC50/CH50/AP50/EC50 grep-confirmed: ~20
- Compounds flagged as ChEMBL coverage-gap absent: 6+ (rosmarinic acid, Helicteres lignans, Bupleurum polysaccharides, marine fucoidans, etc.)
- Coverage gaps confirmed: Factor H natural-product upregulators, CD55/CD59/CR1 natural-product upregulators, fungal direct upstream complement modulators, bacterial-metabolite direct upstream complement modulators
