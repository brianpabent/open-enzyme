# comp-029 — Inputs Provenance

All input values used by `analyze.py` with source, fetch date, and verification status. CLAUDE.md Rule 4 (pre-commit grep-verify gate) discipline.

## Rosmarinic acid IC50 data

| Value | Source | Fetched | Verification |
|---|---|---|---|
| C3b covalent attachment IC50 = **34 μM** | Sahu A, Rawal N, Pangburn MK 1999 (PMID 10353266) Biochem Pharmacol 57(12):1439-46 | 2026-05-16 (carried forward from comp-020 search-log W2) | Verified against comp-020 `outputs/per-node-findings.md` L62 and `inputs/provenance.md` L25. Primary paper text not in Paperclip corpus (pre-PMC era); comp-020 carries `[PRIMARY-PAPER-CONFIRMATION-PENDING]` flag. Number is identically stated across complement-c5a-gout.md, upstream-complement-modulator-sweep-computational.md, upstream-complement-verification-rerun-computational.md. |
| Classical-pathway hemolytic IC50 = **180 μM** | Sahu 1999 (PMID 10353266) | 2026-05-16 | Same paper. Different assay format. |
| Alternative-pathway hemolytic IC50 = **160 μM** | Sahu 1999 (PMID 10353266) | 2026-05-16 | Same paper. |
| C5 convertase direct IC50 = **1500 μM** | Sahu 1999 (PMID 10353266) | 2026-05-16 | Same paper. Upper bound of the 44× spread (34 → 1500). |
| Englberger 1988 C3-convertase IC50 = **5–10 μM** | Englberger W et al. 1988 (PMID 3198307) Int J Immunopharmacol 10(7):729-37 | 2026-05-16 (via wiki/upstream-complement-modulator-sweep-computational.md L33 + complement-c5a-gout.md L58) | Abstract-tier; flagged in wiki as the LOWER bound (5–10 μM) of the IC50 spread. comp-018/comp-020 carry CITATION-CONFIRMED-VIA-WEBSEARCH-SNIPPET flag. |

**Assay-format spread:** 44× across Sahu 1999 alone (34 μM → 1500 μM). If Englberger 1988 5 μM is included, the spread is **300×** (5 → 1500). Operative-mechanism range for fluid-phase / gut-luminal C3 convertase inhibition: **5 μM to 180 μM** (excluding the 1500 μM C5-convertase-direct because rosmarinic acid does not operate at the C5-convertase-direct step — that's just an artifact of assay format).

## Rosmarinic acid bioavailability

| Value | Source | Fetched | Verification |
|---|---|---|---|
| Rat oral absolute bioavailability F = **0.9–1.7%** (dose 12.5–50 mg/kg) | Wang J et al. 2017 RSC Adv 7:9057-63 (DOI 10.1039/C6RA28237G) | 2026-05-16 | Verified via Paperclip cat /papers/PMC7828042/content.lines L14 (Kang 2021 review citing Wang 2017 verbatim) and L59 (same number, second citation in same paper). |
| Human free plasma RA Cmax = **20 nM** after 200 mg Perilla single dose, Tmax 1 h | Baba S et al. 2004 (PMID 15120569) Life Sci 75:165-78 | 2026-05-16 | Verified via Paperclip cat /papers/PMC7828042/content.lines L14: "plasma concentrations of the parent rosmarinic acid and conjugated rosmarinic acid in human subjects were reported about 20 nM and 1200 nM, respectively, at 1 h after oral intake of the Perilla frutescens extract." |
| Human conjugated plasma RA Cmax = **1200 nM** at same time | Baba S et al. 2004 | 2026-05-16 | Same source. Note: conjugated metabolites likely inactive at C3b covalent modification (RA's mechanism requires the free catechol). |
| Plasma protein binding fraction free = **0.086** (91.4% bound) | Kang YJ et al. 2021 PMC7828042 Pharmaceutics 13:83 | 2026-05-16 | Verified via Paperclip cat /papers/PMC7828042/content.lines L25 + L69: "the protein binding of rosmarinic acid (91.4% in rat plasma, our unpublished data)" and L69: "higher binding protein value (91.4%) of RA." |
| Gut-luminal RA concentration after 200 mg oral = **252–1100 μM** | Kang YJ et al. 2021 PMC7828042 (calculated estimate) | 2026-05-16 | Verified via Paperclip cat /papers/PMC7828042/content.lines L15: "rosmarinic acid concentrations in the intestine following the oral administration of rosmarinic acid (200 mg) could be calculated as 252-1100 μM, which can plausibly induce drug interactions." |
| GI stability (gastric recovery ≥98%, intestinal recovery 69–75%) | Veras KS et al. 2022 PMC9784852 Pharmaceutics 14:2663 | 2026-05-16 | Verified via Paperclip cat /papers/PMC9784852/content.lines L19. |

## DAF/CD55 SCR1-4 engineered construct

| Value | Source | Fetched | Verification |
|---|---|---|---|
| Intrinsic C4b2a (CP convertase) half-life at 37°C = **7.5 min** | Fischer E, Kazatchkine MD 1981 PMC2186394 J Exp Med 153(7):1671-1681 | 2026-05-16 | Verified via Paperclip cat /papers/PMC2186394/content.lines L3 (abstract). Verbatim: "prolongs the half-life of surface-bound C4b2a from 7.5 min to greater than 5 h." |
| DAF dissociates C2a from C4b2a and Bb from C3bBb (mechanism) | Kinoshita T et al. 1987 PMC2189641 J Exp Med 166(5):1376-1389 | 2026-05-16 | Verified via Paperclip cat /papers/PMC2189641/content.lines L3 (abstract). |
| As few as 10² DAF molecules/cell profoundly inhibit C3/C5 convertase assembly | Medof MD, Kinoshita T, Nussenzweig V 1984 PMC2187498 J Exp Med 160(5):1558-1578 | 2026-05-16 | Verified via Paperclip cat /papers/PMC2187498/content.lines L3 (abstract). |
| Soluble DAF detected in synovial fluid + plasma | Medof MD et al. 1987 PMC2188295 J Exp Med 165(3):848-864 | 2026-05-16 | Verified via Paperclip cat /papers/PMC2188295/content.lines L3 (abstract). |
| DAF/CD55 UniProt = P08174 (canonical) | comp-012 + comp-030 | (carried forward) | Cross-referenced at experiments/comp-012-daf-cd55-scr14-truncated/inputs/P08174.fasta. |
| DAF SCR1-4 construct = aa 35–285 | comp-012 design | (carried forward) | wiki/daf-cd55-scr14-truncated-computational.md + comp-030 outputs. |

## MSU surface kinetics

| Value | Source | Fetched | Verification |
|---|---|---|---|
| MSU 20 mg/mL + healthy human serum 30 min 37°C generates measurable C5a; IgM + CRP required | Wessig AK et al. 2022 PMC8924570 Sci Rep 12:4423 | 2026-05-16 | Verified via Paperclip cat /papers/PMC8924570/content.lines L23 (assay conditions) + L27-28 (anaphylatoxin readout). |
| Murine i.p. 3 mg MSU → C5a-dependent IL-1β + neutrophil recruitment at 6 h | Khameneh HJ et al. 2017 PMC5253373 Front Pharmacol 8:10 | 2026-05-16 | Verified via Paperclip cat /papers/PMC5253373/content.lines L23 (in vitro stimulation) + L26 (in vivo i.p. MSU dose). |
| MSU activates classical + alternative pathways | Doherty M et al. 1983 PMID; Russell IJ et al. 1982 PMID 6749358 | (cited via Khameneh 2017 + OE corpus) | Cross-referenced from complement-c5a-gout.md §3. |

## Multilingual sources surfaced

Searched CNKI / Chinese-language web for rosmarinic acid (迷迭香酸) bioavailability and clinical data via WebSearch 2026-05-16. Chinese sources (MCE compound description, biopurify spec sheet, x-mol review of rosmarinic acid in food industry, tiprpress review of rosmarinic acid pharmacology + delivery systems 2023) **corroborate** the English-language picture: low oral bioavailability, hepatic-glucuronidation-limited, drug delivery system improvements active. **No new quantitative bioavailability value beyond the Wang 2017 / Baba 2004 anchors** was surfaced. No clinical Chinese trial reports higher human plasma Cmax than the 20 nM free RA from Baba 2004. Verdict: language barrier is not load-bearing here; the canonical PK numbers are the Western primary literature and the Chinese reviews cite the same Wang 2017 / Baba 2004 data.

Japanese-language sources not separately searched because Baba 2004 is itself the canonical Japanese-led primary study and is already in the English-translated primary literature.

## Items NOT verified to primary-paper full text

Per CLAUDE.md Rule 4, every load-bearing value should grep against primary source. Items where we used abstracts or review citations instead of primary papers:

1. **Sahu 1999 IC50 values (34, 180, 160, 1500 μM)** — primary paper not in Paperclip corpus (pre-PMC era). Carried forward from comp-020's `inputs/provenance.md` L25 with the same `[PRIMARY-PAPER-CONFIRMATION-PENDING]` flag. Number is consistent across 3 wiki pages.
2. **Englberger 1988 5-10 μM IC50** — abstract-tier (not in Paperclip corpus). Carried forward from wiki/upstream-complement-modulator-sweep-computational.md L33. Used as the lower bound of the spread, not as the central value.
3. **Wang 2017 RA bioavailability 0.9-1.7%** — primary paper not in Paperclip corpus. Number is verified verbatim in Kang 2021 PMC7828042 review (twice).
4. **Baba 2004 plasma Cmax 20 nM / 1200 nM** — primary paper not in Paperclip corpus. Verbatim quoted in Kang 2021 PMC7828042 review.
5. **Fischer 1981 C4b2a 7.5 min half-life** — Paperclip-indexed abstract only (not full text). Number is in the abstract, not derived from a re-analysis of the figures.
6. **Medof 1984 102 DAF/cell threshold** — abstract-tier (Paperclip-indexed abstract only).

These six items all rely on the abstract or review-paper quotation. Primary full-text fetch deferred to Phase 2; the comp-029 model treats them as best-available priors, not bedrock numbers. Sensitivity analysis (see `outputs/sensitivity_analysis.json`) shows the comp-029 verdict is NOT particularly sensitive to ±2× variation in any single one of these — the dominant uncertainty drivers are the DAF surface-engagement prior and the choice of fluid-phase vs. gut-luminal RA concentration regime.
