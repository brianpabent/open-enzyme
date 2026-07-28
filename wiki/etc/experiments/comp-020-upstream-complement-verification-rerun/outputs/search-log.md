# comp-020 — Search log (audit trail)

This is the historical audit trail of Paperclip MCP and WebSearch queries. Each
row records the query and contemporaneous result note.

> **Quarantine boundary:** Result counts and “notable hit” annotations are
> historical search notes, not current scientific findings. They do not support
> an empty class, systematic absence, coverage rate, target attribution,
> potency comparison, or independent confirmation. Evolving sources must be
> queried again and load-bearing claims reverified from primary records.

## Paperclip MCP queries

| # | Query | Result count | Notable hits |
|---|---|---|---|
| 1 | "natural product C1q classical pathway inhibitor" -n 10 | 10 | C1qNb75 nanobody (PMC7396675); Helicteres angustifolia (PMC6273495); Bupleurum polysaccharides ELISA (PMC4629277); Anticomplementary multiherb SARS (PMC7126446); PIC1 peptide (PMC4141160) |
| 2 | "complement factor B inhibitor natural compound" -n 10 | 10 | Factor B small-molecule (PMC6475383); Schubart review of low-MW AP inhibitors (PMC10092480); Factor D therapeutic strategy (PMC8458797); danicopan / iptacopan papers |
| 3 | "anticomplementary natural product CH50 alternative pathway" -n 10 | 10 | Marine algae polysaccharide structure-activity (PMC4728500); Floridoside CP-activator (PMC2579733); reinforces Helicteres + multiherb hits |
| 4 | "Bupleurum polysaccharide complement inhibition" -n 8 | 8 | Bupleurum C3c ELISA paper (PMC4629277); Ligusticum chuanxiong polysaccharide (PMC6155779); Bupleurum LPS-TLR4 (PMC3805517); thrombospondin-1 / FH synergy (bio_a432c55080e4) |
| 5 | grep "CH50\|AP50\|IC50\|μM\|mM" /papers/PMC7126446/content.lines | n/a | Historical values recorded from Zhang & Chen 2008; reverify before reuse. |
| 6 | grep "CH50\|AP50\|IC50\|μM\|mM" /papers/PMC6273495/content.lines | n/a | Historical values recorded from Yin 2016; reverify before reuse. |
| 7 | "Factor H mimetic upregulation natural" -n 8 | 8 | Mini-FH constructs and Factor H reviews were noted; the query supports no class-absence claim. |
| 8 | "MASP-2 inhibitor compound complement lectin" -n 8 | 8 | TFPI1-derived MASP-2 inhibitor (PMC6527154); MASP-2 heparin-binding (PMC7212410); MASP-2 selective small-molecule (PMC12037010 — EVO24L) |
| 9 | grep "IC50\|fucoidan\|heparin\|μg/mL" /papers/PMC4728500/content.lines | n/a | Historical marine-polysaccharide values recorded; reverify before reuse. |
| 10 | grep "IC50\|μg/ml\|heparin" /papers/PMC7212410/content.lines | n/a | Historical heparin values recorded; reverify exact material and assay before reuse. |
| 11 | "rosmarinic acid complement inhibition" -n 5 | 5 | Multiple rosmarinic acid reviews (PMC9143754, PMC8989115, PMC7059186); none had primary IC50 → escalated to WebSearch |
| 12 | "ginsenoside complement classical pathway" -n 5 | 5 | Ginseng polysaccharide C4 biosynthesis enhancement (PMC8461058 — INVERSE direction, immunostimulatory not inhibitory); Rg3 C1q reduction in depression model (PMC12594608) |
| 13 | "saponin Bupleurum saikosaponin complement" -n 5 | 5 | Saikosaponin reviews (PMC6130612, PMC7126585) — broad immunomodulation; not direct upstream complement IC50 |
| 14 | "K76 monoascus complement inhibitor fungus" -n 5 | 5 | Historical nearby records: Monascus pigments (PMC11877510) antioxidant/antimicrobial; fumagillin (PMC7020470) targets MetAP2 rather than complement. This unsnapshotted query supports no class-level conclusion. |
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
| 26 | "MAC C5b-9 inhibitor natural product membrane attack complex" -n 8 | 8 | CD59 and engineered-protein records were noted; the query supports no class-absence claim. |
| 27 | "CD55 DAF expression upregulation natural compound" -n 5 | 5 | CD55 reviews and a KLF4-CD55 record were noted; the query supports no class-absence claim. |
| 28 | "properdin inhibitor natural polysaccharide" -n 5 | 5 | Properdin reviews and a low-properdin cohort record were noted; the query supports no class-absence or safety-causality claim. |

## WebSearch queries

| # | Query | Notable result |
|---|---|---|
| W1 | "CNKI WanFang luteolin rutin anti-complement CH50 sheep erythrocyte hemolytic assay 2024 2025" | Did not return primary-paper IC50 from Chinese databases in time budget. **Phase 2 follow-up flagged.** |
| W2 | "rosmarinic acid C5 convertase complement IC50 hemolytic in vivo allergic" | Search snippets named Sahu 1999 (PMID 10353266), Peake 1991 (PMID 1761351), and Englberger 1988 (PMID 3198307). The values were not verified from primary full text and are withheld from current use. |

## Summary statistics

- Total Paperclip MCP search/grep queries: 28
- Total WebSearch queries: 2
- Unique primary papers grep-verified for load-bearing IC50: 6 (PMC7126446, PMC6273495, PMC4728500, PMC7212410, PMC4629277, PMC6155779)
- Compound and value counts were not independently reconciled and are not used
  as evidence.
