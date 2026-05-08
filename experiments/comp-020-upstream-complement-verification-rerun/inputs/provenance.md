# comp-020 provenance + methodology notes

## Independence statement (load-bearing)

This re-run was conducted explicitly without consulting comp-018 / comp-019 outputs. The agent received only the target-node list and compound-class scope; no compound names, no prior findings, no predecessor's recommendations.

The intent — per the brief and per CLAUDE.md §Multi-model synthesis as guard against epistemic homogenization — is to produce an independent second-opinion data point that can be compared against the predecessor to surface (a) narrative-cohesion bias in the predecessor's headline, (b) missed top-tier candidates in either scan, (c) divergent assay-format judgments.

## Pre-commit verification gate compliance (CLAUDE.md Rule 4)

Each load-bearing IC50 / CH50 / AP50 / Ki number in [`outputs/per-node-findings.md`](../outputs/per-node-findings.md) was grep-verified against primary-paper full text in the Paperclip MCP corpus before being written to the page:

| Number | Paper | Verification anchor |
|---|---|---|
| Helicteres compound 5 CH50 0.009 ± 0.002 mM | PMC6273495 | grep result line 18 (verbatim from paper) |
| Helicteres compound 4 CH50 0.040 ± 0.009 mM | PMC6273495 | grep result line 18 |
| Luteolin CH50 0.19 mM, AP50 0.17 mM | PMC7126446 | grep result line 10 + Table 1 |
| Heparin LP 2 / CP 39 / AP 76 μg/mL | PMC7212410 | grep result line 45 |
| Heparin tetrasaccharide LP IC50 21 μg/mL | PMC7212410 | grep result line 45 |
| Bupleurum BCPs LP 0.098 mg/mL | PMC4629277 | grep result line 46 |
| Bupleurum BPs LP 1.057 mg/mL | PMC4629277 | grep result line 46 |
| Marine fucoidan ANW IC50 0.98 μg/mL | PMC4728500 | grep result line 39 |
| Marine SJW-3 IC50 3.11 μg/mL | PMC4728500 | grep result line 23 |
| Ligusticum LCP-I-I ICH50 26.3 ± 2.2 μg/mL | PMC6155779 | grep result line 18 |
| Rosmarinic acid C3b 34 μM, CP 180 μM, AP 160 μM, C5conv 1500 μM | PMID 10353266 (Sahu 1999), 1761351 (Peake 1991), 3198307 (Englberger 1988) | WebSearch result snippet (Sahu 1999 Biochem Pharmacol) — primary-paper full text NOT in Paperclip corpus; numbers carry **[PRIMARY-PAPER-CONFIRMATION-PENDING]** flag |

The rosmarinic acid numbers are the only load-bearing values in this re-run that did not pass through Paperclip-corpus grep verification because the 1988/1991/1999 papers predate PMC's full-text coverage. They are flagged in the wiki page as `[CITATION-CONFIRMED-VIA-WEBSEARCH-SNIPPET, primary-paper full-text fetch deferred to Phase 2]`.

## Anti-pattern guard (DAF SCR1-4 disulfide-count incident)

Every numerical claim above is sourced from a specific paper line, not synthesized from inference. The DAF SCR1-4 hallucination pattern (3 disulfides per SCR domain × 4 = 12, off-by-50% from UniProt P08174 ground truth of 8) was the trigger for CLAUDE.md Rule 4. comp-020 explicitly conforms.

## Multilingual scope — partial execution disclosure

The CLAUDE.md §Global-multilingual research by default rule requires non-English sources to be scanned alongside PubMed. In this re-run:

- **Substantively executed:** English-language scans, including English-journal publications by China-based groups (Daofeng Chen / Fudan; Quanbin Zhang / OUC). Most of the substantive TCM-derived natural-product complement-modulator work IS published in English-language journals by these groups, partially mitigating Western-research bias risk.
- **Partially executed:** WebSearch queries against Chinese-keyword anti-complement topics returned no primary-paper IC50 numbers in the time budget; CNKI / WanFang / J-STAGE direct full-text fetches were NOT executed.
- **Phase 2 follow-up explicitly flagged:** dedicated CNKI/WanFang Chinese-keyword query (补体抑制剂, 经典途径, 旁路途径, 凝集素途径) + J-STAGE Kampo query (補体 + 漢方医学) + KISS Korean query.

This partial-execution disclosure is per CLAUDE.md §Pre-commit verification gate — flag what was NOT done, don't paper over it.

## ChEMBL coverage gap — methodology

For each top-tier compound surfaced, a ChEMBL ID was looked up via PubChem cross-reference. The following compounds returned no ChEMBL anti-complement assay records despite documented primary-literature IC50:

- Rosmarinic acid (CHEMBL165102 exists; anticomplement assays NOT curated despite 30+ year primary-literature record)
- Helicteres lignans (machicendonal, dihydrodehydrodiconiferyl alcohol) — not in ChEMBL at all
- Bupleurum polysaccharides — polysaccharide structural class systematically absent from ChEMBL
- Marine fucoidans — same structural exclusion

The methodology is the same as comp-013 / comp-014 ChEMBL gap analysis: structurally, ChEMBL anti-complement curation is biased toward synthetic clinical-stage compounds (iptacopan, danicopan, compstatin/pegcetacoplan) and away from natural-product / polysaccharide classes.

## What this re-run does NOT do

- Does NOT propose comp-NNN follow-ups to wet-lab any specific compound (recommendations are Phase 2 candidate flags, not gating decisions)
- Does NOT triage compounds by gut-luminal tractability (that's the comp-004/comp-013 framework, separate)
- Does NOT propose engineering routes (e.g., koji biosynthetic pathway expression of rosmarinic acid)
- Does NOT recommend supplements or clinical actions (Phase 0 — Research & Design)
