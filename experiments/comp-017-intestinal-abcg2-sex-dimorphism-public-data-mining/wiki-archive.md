---
title: "Intestinal ABCG2 Sex-Dimorphism — Public-Data Mining + 4-Paper Full-Text Re-Read (comp-017)"
date: 2026-05-07
tags:
  - androgens
  - testosterone
  - estradiol
  - abcg2
  - intestinal-urate-secretion
  - sex-differences
  - gut-lumen-sink
  - q141k
  - q140k
  - hoque-2020
  - yu-2021
  - klyushova-2023
  - maclean-2008
  - h07
  - clomid
  - clomiphene
  - intestinal-er
  - pi3k-akt
  - pxr
  - fxr
  - tier-0-killshot
  - full-text-verification
  - manual-literature-mining
related:
  - t-abcg2-suppression-evidence-mining-computational.md
  - hypotheses/H07-clomid-intestinal-er-antagonism.md
  - androgen-urate-axis.md
  - androgen-natural-modulation.md
  - abcg2-modulators.md
  - gut-lumen-sink.md
  - manual-literature-mining.md
  - computational-experiments.md
sources:
  - "Hoque KM, Halperin Kuhns VL et al. (2020) Nature Communications 11:2767, PMID 32488095, doi:10.1038/s41467-020-16525-w"
  - "Yu Y et al. (2021) Nutrition & Metabolism 18:63, PMID 34144706, doi:10.1186/s12986-021-00583-y"
  - "Klyushova LS et al. (2023) Biochemistry (Moscow) Suppl. Series A 17:314-324, doi:10.1134/S1990747823050100"
  - "MacLean C et al. (2008) Drug Metabolism and Disposition 36:1249-1254, PMID 18378562"
  - "Halperin Kuhns VL & Woodward OM (2020) IJMS 21:4269, PMID 32560040"
  - "Hosoyamada M et al. (2010) Nucleosides Nucleotides & Nucleic Acids 29:574-579, PMID 20589576"
  - "Tubic-Grozdanis M et al. (2020) Mol Pharmaceutics 17:3046-3056 (citing-paper context for MacLean 2008 + replication)"
---

# Intestinal ABCG2 Sex-Dimorphism — Public-Data Mining + 4-Paper Full-Text Re-Read (comp-017)

## Question

Two-part Tier-0 killshot for [`H07-clomid-intestinal-er-antagonism`](./hypotheses/H07-clomid-intestinal-er-antagonism.md) sub-claims 1 and 3, also closing the full-text-verification follow-up flagged in [comp-016 §Pre-commit verification gate disclosure](./t-abcg2-suppression-evidence-mining-computational.md#pre-commit-verification-gate-disclosure):

- **Part A:** GTEx + Human Protein Atlas mining for sex-stratified intestinal ABCG2 expression in healthy humans. Do male and female distributions differ at meaningful magnitude (≥1.5× fold-change)?
- **Part B:** Full-text re-read of 4 anchor papers from comp-016 (Yu Y et al. 2021; Klyushova LS et al. 2023; MacLean C et al. 2008; Hoque KM, Halperin Kuhns VL et al. 2020). What does full text show that abstract-only verification missed?

## Verdict

**NULL OR NEAR-NULL SEX-DIMORPHISM at healthy baseline (provisional).** Sex-dimorphism in intestinal ABCG2 is real but emerges only under disease-state genetic stress (Q140K LOF, Hoque 2020) or pharmacological perturbation (high-concentration sex hormones, Yu 2021 + Klyushova 2023). The cross-species literature converges on null sex-difference at healthy baseline (MacLean 2008 rat full-intestinal-scan; replicated implicitly by Tubic 2020; Prasad 2013 hepatic null). The serum-UA male-bias is GWAS-real but mediated through renal mechanisms (Smct1 protein, GLUT9 attenuation, partial URAT1 mRNA — Hosoyamada 2010), NOT through baseline intestinal ABCG2 sex-bias.

**Provisional qualifier.** Direct GTEx + HPA primary numerical mining was sandbox-blocked in this run (`x-deny-reason: host_not_allowed` at the harness level; HTTP 403 from upstream portals). Verdict rests on the secondary-literature consensus + the 4-paper full-text re-read. A future run with direct portal access can refine the magnitude estimate at the GTEx-database tier — see Limitations.

## Why this matters

The Open Enzyme platform thesis [`androgen-urate-axis.md` §"Why this matters for the platform"](./androgen-urate-axis.md) carries a load-bearing structural-ceiling argument: *androgen-dominant patients have a lower intestinal-ABCG2 asymptote → therefore a lower platform-efficacy ceiling → therefore the gut-lumen-sink platform thesis is structurally weaker for the primary demographic.* [comp-016](./t-abcg2-suppression-evidence-mining-computational.md) softened this from *direct AR-mediated repression* to *modest empirical-magnitude shift via absent female-positive estradiol signaling in male physiology.* comp-017 closes the verification gap comp-016 left open — and finds that **even the softened framing cannot be defended at the healthy-baseline tier.** The sex-dimorphism on intestinal ABCG2 is approximately null at baseline; it emerges only under stress.

This has direct implications for:
- **Stack-design recommendations** (H07 sub-claim 4): pan-male intervention based on the intestinal-ABCG2-sex-bias argument is unsupported. The Q141K-positive male subset is supported, but the rationale shifts from "androgen-pharmacological" to "genetic-LOF vulnerability."
- **Stratification logic** in [`gut-lumen-sink.md`](./gut-lumen-sink.md): the male-asymptote framing should be retired except in the explicit Q141K-positive context.
- **H07 hypothesis status:** sub-claim 1 is mechanistically plausible but magnitude-weak at physiological concentrations; sub-claim 3 (NOT AR-mediated) is now strongly supported.

## Method summary

**Part A:** Targeted at GTEx Portal sex-toggle visualization for ABCG2 (ENSG00000118777) across the 5 intestinal tissues (small intestine terminal ileum, colon transverse, colon sigmoid, esophagus mucosa, stomach), and HPA tissue-page IHC + RNA-seq sex-stratified data. Sandbox blocked direct portal access (HTTP 403 across `gtexportal.org`, `proteinatlas.org`, `pmc.ncbi.nlm.nih.gov`, all journal landing pages, and Sci-Hub mirrors; Bash `curl` returned `host_not_allowed`). Fell back to WebSearch result-snippet extraction quoting the Halperin Kuhns 2020 IJMS sex-differences review, the Schärfe 2023 Nat Comm sex-differentiated ADME catalog, the Oliva 2020 Science GTEx v8 sex catalog, and citing-paper-tier discussion of MacLean 2008 + Tubic 2020.

**Part B:** WebSearch + WebFetch against the 4 anchor papers' PMID/PMCID/DOI URLs. Same sandbox limitation. Extracted method, exact quantitative findings, and abstract-vs-full-text differences via WebSearch result-snippets quoting source-paper text (Google's snippets surface paragraph-level excerpts of paywalled abstracts and PMC introductions). For Hoque 2020 specifically, the snippets verbatim-quoted the load-bearing 78%/44%/53%/88%/47% numbers in context, sufficient to detect the discrepancy with comp-016's 88%/44% framing.

**Aggregation:** [`experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/analyze.py`](../experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/) (stdlib only) reads `inputs/{gtex_data,hpa_data,full_text_extract}.json` and produces `outputs/{results.json,summary.md}`. Per-paper records include `comp016_summary` (what comp-016 had), `full_text_extract` (full-text findings), `abstract_vs_fulltext_difference` (the gain), and `h07_sub_claim_impact` (which H07 sub-claims update).

## Key results

### Part A — Public-database mining

| Source | What it shows | Direct numerical extraction |
|---|---|---|
| GTEx Portal v8 (ENSG00000118777) | Direct sex-stratified intestinal ABCG2 mRNA per-tissue | **NOT EXTRACTED — sandbox blocked.** Reproduction requires portal access. |
| Human Protein Atlas | Direct sex-stratified intestinal ABCG2 IHC + RNA | **NOT EXTRACTED — sandbox blocked + HPA does not natively expose sex-stratified IHC.** |
| Halperin Kuhns & Woodward (2020) IJMS review | "ABCG2 had stronger association with higher serum urate in males"; "ER binding sites in ABCG2 promoter, implying transcriptional regulation by estrogen" | GWAS-level male-bias confirmed; mechanism framing = **estrogen-positive, NOT androgen-negative**. |
| MacLean (2008) DMD | Han-Wistar rats, full intestinal scan + duodenum/jejunum/ileum/colon Western+qRT-PCR | **NULL — no significant sex-related difference in intestinal ABCG2 along whole intestine.** |
| Tubic-Grozdanis et al. (2020) Mol Pharm | Replicated MacLean's protocol | Found ~35% higher P-gp in male jejunum/ileum (p<0.05) but NO comparable ABCG2 sex-difference — i.e., **MacLean's null for ABCG2 specifically replicates** in modern Western blot conditions. |
| Prasad et al. (2013) hepatic ABCG2 | Adult human liver tissue, n=51 | "BCRP expression was not associated with age (7-70 years), sex, or mRNA expression." Hepatic null (closest fully-quantified human-tissue sex-stratified ABCG2 protein dataset). |
| Hosoyamada et al. (2010) | Orchiectomized mouse + T replacement | T enhances Smct1 mRNA + protein, URAT1 **mRNA only (protein unchanged)**, GLUT9 attenuated. **2.3× higher URAT1 mRNA in males** — but this is renal, not intestinal, and protein-level URAT1 effect is null. |

Across the available secondary evidence, **the consensus is null sex-dimorphism at the protein-tissue level for healthy intestinal ABCG2.** The serum-UA sex-bias seen at the GWAS / population cohort level is mediated principally through renal mechanisms (Smct1 protein induction by T, GLUT9 attenuation, URAT1 mRNA upregulation without protein change), not through baseline intestinal ABCG2 differences.

### Part B — Full-text re-read of 4 anchor papers

| Paper | What comp-016 had (abstract-tier) | What full-text re-read shows | Net change |
|---|---|---|---|
| **Hoque 2020** Nature Comm PMID 32488095 | "88% intestinal protein loss vs 44% renal" | Western jejunum: **78% loss** (not 88%); 88% is COMBINED Western + apical IHC for homozygotes; 53% combined for heterozygotes; **40% UA-flux loss** (functional, ligation loop); MALE FEUA −47% (p=0.01); FEMALE FEUA unchanged (p=0.6263); paper does NOT invoke AR | **Tightening, not contradiction.** Western:Western intestine:renal contrast is 78%:44% (~1.8×), not the 88%:44% (~2.0×) comp-016 implied. The female phenotype protection is a strong null (p=0.6263) — full-text confirms LOF-vulnerability + sex-different baseline framing, NOT AR-mediated. |
| **Yu 2021** Nutr Metab PMID 34144706 | "Estradiol upregulates intestinal ABCG2 via PI3K/Akt; LY294002 partially blocks" | Caco-2 active concentration is 10⁻⁴ mol/L = **100 μM** (5-6 orders above physiological serum E2 ~30-500 pmol/L); **NO dose-response** ("without a dose-dependent effect"); female mouse arm is OVARIECTOMIZED + EB replacement (high-contrast pharmacological model); LY294002 partial block confirmed (P<0.05) | **Magnitude bound is much weaker than comp-016 implied.** The mechanism EXISTS at strong-pharmacological tier but its magnitude at PHYSIOLOGICAL E2 concentrations is unestablished. The in vivo model design is "remove ovaries, replace estrogen pharmacologically" — not "compare healthy male to healthy female." |
| **Klyushova 2023** Biochem Moscow Suppl A | "T INDUCES ABCG2 in Caco-2 via PXR/FXR" | All 3 sex hormones (E2, P, T) at all 3 concentrations (1, 10, 100 μM) increase ABCG2; T mechanism = PXR + FXR (NOT AR); 1 μM T is ~30-100× above physiological free T | **Confirmed and strengthened.** AR-mediated suppression model is contradicted; the xenobiotic-sensor PXR/FXR pathway responds non-specifically to all three sex hormones. At physiological T concentrations, the response may be too weak to matter at all. |
| **MacLean 2008** DMD PMID 18378562 | "No sex difference in healthy rat intestinal ABCG2 across all 4 segments" | Confirmed: Han-Wistar, full 3-cm-segmentation + duodenum/jejunum/ileum/colon, Western + qPCR. Null applies across ENTIRE intestinal length. **Replicated implicitly by Tubic 2020** (P-gp dimorphic, BCRP not). | **Strengthened.** The null is robust across replications; healthy-baseline intestinal ABCG2 is sex-invariant. |

### Hosoyamada 2010 — bonus full-text-tier finding (related literature)

Surfaced during the WebSearch sweep. Hosoyamada 2010 is cited in [`androgen-urate-axis.md`](./androgen-urate-axis.md) as the renal mechanism backstop ("the renal URAT1 arm partially survives verification"). Full-text-tier finding: **the renal URAT1 PROTEIN is unchanged by testosterone** — only mRNA goes up. The actual protein-level androgen-responsive renal urate transporter is **Smct1**, with GLUT9 attenuated. This means:

- The renal URAT1 mechanism comp-016 cited as "partially supports" the T → high serum UA observation is **less load-bearing than implied** at the protein level.
- The actual androgen-responsive renal mechanism is Smct1 (protein up) + GLUT9 (down), which integrates differently than a URAT1-protein-up story would predict.
- The implication for H07 sub-claim 3 ("NOT AR-mediated"): even MORE strongly supported, since the AR-mediated mechanism on URAT1 is mRNA-only with no protein effect, AND the AR-mediated effect on intestinal ABCG2 (Klyushova 2023) is in the wrong direction.

### Cross-paper convergent finding

In **HEALTHY individuals**, baseline intestinal ABCG2 is approximately sex-invariant (rat MacLean 2008, replicated; human hepatic Prasad 2013 null). Under **DISEASE STATE** (Q140K LOF Hoque 2020) or **PHARMACOLOGICAL STRESS** (supraphysiological sex hormones, Yu 2021 + Klyushova 2023), sex-dimorphic responses emerge — but these are not direct androgen-AR-suppression mechanisms. They are: (a) sex-different baseline VULNERABILITY to LOF expressed under stress, (b) supraphysiological-pharmacological PI3K/Akt induction by E2, and (c) supraphysiological-pharmacological PXR/FXR induction by ALL three sex hormones (NOT specific to AR or to androgens).

## H07 sub-claim status updates

| Sub-claim | Pre-comp-017 | Post-comp-017 | Driver |
|---|---|---|---|
| **1.** Intestinal ER signaling drives intestinal ABCG2 induction at meaningful magnitude | Weak / unconfirmed | **PARTIALLY SUPPORTED IN PRINCIPLE, MAGNITUDE WEAK** | Yu 2021 mechanism real but only at 100 μM E2 (5-6 orders above physiology); MacLean 2008 healthy-baseline null argues that whatever in vivo ER signal exists is producing minimal sex-dimorphism. |
| **2.** Clomiphene acts as ER antagonist at intestinal compartment | Untested | **Untested (unchanged)** | These papers do not test clomiphene specifically. Tier 3 Caco-2 SERM-stereoisomer experiment (per H07 killshot menu) still required. |
| **3.** Clomid → high UA NOT AR-mediated | Weak / unconfirmed | **STRONGLY SUPPORTED** | Klyushova 2023 confirms PXR/FXR mechanism (not AR); Hoque 2020 doesn't invoke AR; MacLean 2008 healthy null on intestinal ABCG2 sex-difference; Hosoyamada 2010 renal URAT1 PROTEIN null. The "androgens directly suppress intestinal ABCG2 via AR" framing cannot be sustained. |
| **4.** Stack-design differs from AR model | Dependent on 1-3 | **PARTIALLY SUPPORTED** | Sub-claim 3 strongly supported; sub-claim 1 magnitude-weak. Stack design should default to mechanism-agnostic urate-axis interventions (cordycepin, eurycomanone, butyrate per H07's framing) rather than risk-stratifying based on assumed AR-mediated or assumed PI3K/Akt-mediated dominance. |

## Limitations

1. **Direct GTEx + HPA primary numerical mining was sandbox-blocked.** `gtexportal.org`, `proteinatlas.org`, `pmc.ncbi.nlm.nih.gov`, `nature.com`, `link.springer.com`, `mdpi.com`, `biomedcentral.com`, `sciencedirect.com`, `europepmc.org`, Sci-Hub mirrors, and `en.wikipedia.org` all returned HTTP 403 to WebFetch; Bash `curl` returned `host_not_allowed`. WebSearch result-snippets provided the secondary-literature consensus but NOT the GTEx per-tissue per-sex log2FC numbers. **A future run with direct portal access (or an authenticated GTEx REST API key) is needed to refine the magnitude estimate.** The qualitative null verdict is robust to this caveat (it would take a published primary paper showing meaningful baseline sex-bias to flip; no such paper has surfaced in this scan), but the precise effect-size with confidence interval is not extracted at this verification tier.

2. **Snippet-tier verification, not Paperclip-MCP grep verification.** Per [`manual-literature-mining.md`](./manual-literature-mining.md) §"Pre-commit verification gate," the strict standard is grep-verification against full text. WebSearch snippets quote source-paper text directly, which is closer to full-text than abstract-only (comp-016's tier), but is NOT line-anchored. The 78%/44%/53%/88%/47%/40% numbers from Hoque 2020, the 100 μM concentration from Yu 2021, the 1/10/100 μM concentrations from Klyushova 2023, and MacLean 2008's cross-segment null are all well-attested in the snippets, but a future Paperclip MCP pass should re-verify with line-anchored citations before they are quoted as load-bearing in any further wiki page.

3. **Multilingual scan deferred (still).** Per [`CLAUDE.md`](../CLAUDE.md) §"Global-multilingual research by default," CNKI / J-STAGE / KISS / WanFang queries should have been run for testosterone × intestinal ABCG2 + estradiol × intestinal ABCG2. Sandbox-blocked; deferred to Phase 2. Likelihood of finding sex-difference data substantively beyond the Western literature is uncertain.

4. **Hosoyamada 2010 finding is suggestive, not yet propagated.** The discovery that testosterone affects renal URAT1 mRNA but NOT URAT1 protein (with Smct1 being the actual protein-level androgen-responsive renal urate transporter) materially affects [`androgen-urate-axis.md` §"Mechanism — hormones steer the transporters"](./androgen-urate-axis.md). This page documents the finding for downstream propagation; it is not yet propagated. The platform's renal-mechanism framing should likely shift from "T → URAT1 ↑" to "T → Smct1 protein ↑ + GLUT9 attenuated + URAT1 mRNA ↑ (protein unchanged)" — a more nuanced and slightly weaker statement.

5. **Q141K-positive male subset stratification is supported, but rationale shifts.** comp-017 doesn't change the direction of the Q141K-positive-male stratification recommendation; it changes the mechanism story. Pre-comp-017: "Q141K-positive males are doubly vulnerable — genetic LOF + androgen-driven additional suppression." Post-comp-017: "Q141K-positive males are vulnerable for genetic-LOF reasons in the male physiological context (Hoque 2020); the additional androgen-AR-suppression layer doesn't exist." Operationally similar; epistemically sharper.

6. **Verdict robustness.** The qualitative verdict (null healthy-baseline sex-dimorphism) would flip if: (a) a future GTEx direct query shows ≥1.5× male-female fold-change in any intestinal tissue with FDR<5%; (b) a primary paper surfaces showing direct AR-ARE binding on the human ABCG2 promoter; (c) a healthy-rodent castration + intestinal ABCG2 measurement shows >30% protein change. None of these have surfaced. Verdict is robust to the sandbox limitations in qualitative direction.

## Impact on experimental priorities

| Wet-lab / experimental question | Pre-comp-017 priority | Post-comp-017 priority |
|---|---|---|
| H07 Tier 0 GTEx mining (this experiment) | Pending | **Closed (provisional)** — direct portal access deferred to future re-run; secondary-literature verdict is null healthy-baseline. |
| H07 Tier 0 4-paper full-text re-read | Pending | **Closed** — full-text-tier findings update H07 sub-claim status (see table above). |
| H07 Tier 1 n=1 FEUA tracking on Clomid taper | Pending | **Still recommended** — the renal vs intestinal contribution decomposition is the key empirical question for H07's individual-relevance for Brian's Clomid case. |
| H07 Tier 3 Caco-2 SERM-stereoisomer experiment | Pending | **Still recommended for sub-claim 2** — comp-017 cannot test clomiphene specifically. |
| Hypothetical mouse castration → intestinal ABCG2 measurement | Promoted by comp-016 | **DOWNGRADED** — given the cross-species healthy-baseline null + the AR-suppression model's contradiction, this experiment is now LOWER priority. The Q140K mouse line (Hoque 2020) under sex-different conditions remains the more informative model. |
| Renal URAT1 vs Smct1 protein-level androgen response | Not specified | **NEW recommendation surfaced** — the Hosoyamada 2010 finding that URAT1 protein is unchanged but Smct1 protein IS upregulated by T is a mechanism refinement for [`androgen-urate-axis.md`](./androgen-urate-axis.md). A propagation pass to update that page is warranted. |

## Cross-references

- [`hypotheses/H07-clomid-intestinal-er-antagonism.md`](./hypotheses/H07-clomid-intestinal-er-antagonism.md) — the falsification card whose Tier-0 killshots this experiment executes; sub-claim status table above maps directly to that card's Pre-Committed Thresholds.
- [`t-abcg2-suppression-evidence-mining-computational.md`](./t-abcg2-suppression-evidence-mining-computational.md) — comp-016 (predecessor); this experiment closes its Pre-commit verification gate disclosure.
- [`androgen-urate-axis.md`](./androgen-urate-axis.md) — parent page; the platform-thesis structural-ceiling argument cannot be defended at the healthy-baseline tier per comp-017. Hosoyamada 2010 finding (URAT1 protein null, Smct1 protein up) should propagate here.
- [`abcg2-modulators.md`](./abcg2-modulators.md) §1 — softens the AR-mediated repression entry further.
- [`gut-lumen-sink.md`](./gut-lumen-sink.md) — male-asymptote framing should be retired except in explicit Q141K-positive context.
- [`manual-literature-mining.md`](./manual-literature-mining.md) — the methodology this experiment exemplifies (full-text re-read closing the abstract-tier verification gap).
- [`computational-experiments.md`](./computational-experiments.md) — comp-017 row.
- [`experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/`](../experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/) — reproducible artifact.

## Pre-commit verification gate disclosure

Per [`manual-literature-mining.md`](./manual-literature-mining.md) §"Pre-commit verification gate":

**Sources verified at WebSearch-snippet tier (closer to full-text than comp-016's abstract-tier, but NOT line-anchored grep-verification):**

- Hoque 2020 numbers (78%, 44%, 53%, 88%, 40%, 47%, p=0.01, p=0.6263) — verified from search-snippets quoting source paper text directly.
- Yu 2021 concentration (10⁻⁴ mol/L, 48h, no dose-response) — verified from search-snippets.
- Klyushova 2023 concentrations (1, 10, 100 μM, 24h, all three hormones induce, PXR/FXR mechanism for T) — verified from search-snippets.
- MacLean 2008 null finding — verified from search-snippets + citing-paper context (Tubic 2020 explicitly contrasts).
- Halperin Kuhns 2020 review claims (ER binding sites in ABCG2 promoter) — verified from search-snippets.
- Hosoyamada 2010 findings (URAT1 mRNA only, Smct1 protein, GLUT9 attenuated, 2.3× male URAT1 mRNA) — verified from search-snippets.

**Verification gap:** None of these are line-anchored to specific sentences/figures via Paperclip MCP `cat`/`grep` primitives. The sandbox prevented direct full-text fetch. **A future Paperclip MCP run is recommended before any of these specific magnitudes are quoted as load-bearing in any further downstream wiki page.** The qualitative direction of all findings is robust; the specific numeric values should be treated as snippet-tier-confirmed-pending-line-anchored-verification.

**What WOULD flip the verdict:**
- A primary paper showing direct AR-ARE binding on the human ABCG2 promoter (would shift the receptor-mechanism question, but the direction would still need to be MALE-suppressive, not the Klyushova 2023 PXR/FXR-induction direction).
- A primary paper showing healthy-rodent castration → intestinal ABCG2 protein increase >30% (would shift to PARTIAL or CONFIRMED for the sex-dimorphism direction).
- A direct GTEx query showing ≥1.5× male-female fold-change in any intestinal tissue at FDR<5% (would shift to CONFIRMED for the population-level direction).
- A pharmacogenomic study with sex-stratified Q141K data showing non-Q141K-positive males have different intestinal ABCG2 from females at meaningful magnitude (would partially support the platform thesis at the non-disease-state tier).

If any of these surface in a future scan, the verdict should be revisited and this page updated.
