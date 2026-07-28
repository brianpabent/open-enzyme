# Intestinal ABCG2 sex-difference evidence audit

**Experiment:** comp-017  
**Original extraction:** 2026-05-07  
**Correction verification and artifact run:** 2026-07-27  
**Output schema:** 2  

## Verdict

**Direct healthy-human intestinal ABCG2 sex-stratification remains unresolved.**

The run extracted no sex-stratified GTEx intestinal distribution and no sex-stratified HPA intestinal protein values, so it did not test the preregistered 1.5-fold population threshold.

**Mechanistic Extrapolation:** The sources do not establish a large healthy-baseline human intestinal sex difference. Rat baseline, Q140K mouse disease-state, and pharmacological Caco-2 findings remain separate evidence contexts.

## Part A — direct healthy-human dataset question

- **Decision rule:** test a prespecified 1.5× population difference.
- **GTEx values extracted:** None
- **HPA sex-stratified protein:** NOT DIRECTLY EXTRACTED
- **Decision:** `DIRECT_HUMAN_BASELINE_UNRESOLVED`
- **Reason:** No healthy-human, sex-stratified intestinal ABCG2 values were extracted; the 1.5-fold population threshold was not tested.
- **Original access trace:** The 2026-05-07 run recorded failed direct GTEx Portal access attempts with HTTP 403/host_not_allowed. This is an operational explanation for the missing input, not evidence about ABCG2.

## Part B — four-paper mixed-tier evidence correction

| ID | Evidence | Source | Correction or scope gain |
|---|---|---|---|
| P01 | **Animal Model** | Hoque KM, Halperin Kuhns VL, et al. (2020) — Nature Communications | Primary-text verification confirms 78% jejunal versus 44% renal loss as the like-for-like Western-blot comparison. |
| P02 | **In Vitro** | Liu L, Zhao T, Shan L, Cao L, Zhu X, Xue Y (2021) — Nutrition & Metabolism | The primary text fixes the Caco-2 active condition at a nominal 100 µM and shows that the tested response was not dose-dependent. |
| P03 | **In Vitro** | Slepnev AA, Abalenikhina YV, Popova NM, Shchulkin AV, Yakusheva EN (2023) — Biochemistry (Moscow), Supplement Series A: Membrane and Cell Biology | The correct attribution is Slepnev et al., not Klyushova et al. |
| P04 | **Animal Model** | MacLean C, Moenning U, Reichel A, Fricker G (2008) — Drug Metabolism and Disposition | The verified abstract supports a qualitative healthy-rat null across the studied intestinal scan. |

### Source-specific extracts

#### P01 — Hoque KM, Halperin Kuhns VL, et al. (2020)

- **Title:** The ABCG2 Q141K hyperuricemia and gout associated variant illuminates the physiology of human urate excretion
- **PMID:** 32488095; **DOI:** 10.1038/s41467-020-16525-w
- **Evidence level:** **Animal Model**
- **Verification tier:** Primary full text verified through Europe PMC XML on 2026-07-27.
- **Method described:** Q140K mouse model; jejunal and renal Western blots, intestinal immunofluorescence, and intestinal-loop urate-flux measurements.

**Reported findings retained in the committed extract:**
- {"finding": "Q140K+/+ jejunal ABCG2 protein abundance was 78% lower than WT by Western blot.", "details": "WT n=8; Q140K+/+ n=6; p=0.0046."}
- {"finding": "The article's like-for-like Western-blot comparison was 78% jejunal reduction versus 44% renal reduction."}
- {"finding": "Male Q140K+/+ fractional excretion of urate was 47% lower.", "details": "n=12; p=0.01. Female mice showed no change; n=7; p=0.6263."}
- {"finding": "Modeled ABCG2-mediated jejunal urate flux was reduced 84.2% in Q140K+/+ mice.", "details": "WT n=17; Q140K+/+ n=10; p<0.0001."}

**Correction or scope gain:**
- Primary-text verification confirms 78% jejunal versus 44% renal loss as the like-for-like Western-blot comparison.
- The article HTML/XML, version-of-record PDF, supplementary-information PDF, and publisher source-data workbook contain no 53% or 88% intestinal reduction. The older 53%/88% sentence entered COMP-016 as an explicitly unverified search-summary claim and was then mislabeled as a verbatim snippet in the historical COMP-017 output; it is not a primary-source quotation.
- The primary article separately reports a 78% Western-blot reduction and a statistically significant reduction in jejunal immunofluorescence signal. These are distinct measurements and are not combined into a new percentage.

**Scope notes:**
- This is Q140K disease-state mouse evidence, not a healthy-human baseline estimate.
- The paper does not test clomiphene or establish direct androgen-receptor repression of intestinal ABCG2.

#### P02 — Liu L, Zhao T, Shan L, Cao L, Zhu X, Xue Y (2021)

- **Title:** Estradiol regulates intestinal ABCG2 to promote urate excretion via the PI3K/Akt pathway
- **PMID:** 34144706; **DOI:** 10.1186/s12986-021-00583-y
- **Evidence level:** **In Vitro**
- **Verification tier:** Primary full text verified through Europe PMC XML on 2026-07-27.
- **Method described:** Caco-2 concentration/time experiments with estradiol benzoate and LY294002. The paper also contains clinical and mouse work, but those claims are not rendered by this audit.

**Reported findings retained in the committed extract:**
- {"finding": "Caco-2 cells were exposed to 10^-4, 10^-6, and 10^-8 mol/L estradiol benzoate for 24, 48, or 72 hours."}
- {"finding": "10^-4 mol/L (100 µM) estradiol benzoate significantly increased ABCG2 mRNA at 48 hours without a dose-dependent effect."}
- {"finding": "50 µM LY294002 partially blocked the 100 µM estradiol-benzoate effect on ABCG2 mRNA.", "details": "p<0.05."}

**Correction or scope gain:**
- The primary text fixes the Caco-2 active condition at a nominal 100 µM and shows that the tested response was not dose-dependent.
- That cell-culture condition supports a pharmacological in-vitro mechanism; it does not quantify physiological intestinal regulation.

**Scope notes:**
- The retained Caco-2 findings are In Vitro evidence. The paper's clinical and mouse evidence contexts are not rendered, and this record does not answer the healthy-human sex-stratified baseline question.
- No clomiphene exposure was tested.

#### P03 — Slepnev AA, Abalenikhina YV, Popova NM, Shchulkin AV, Yakusheva EN (2023)

- **Title:** Effect of Sex Hormones on the ABCG2 Transport Protein in Caco-2 Cells
- **PMID:** —; **DOI:** 10.1134/S1990747823050100
- **Evidence level:** **In Vitro**
- **Verification tier:** Official publisher-supplied English abstract and journal metadata verified on 2026-07-27; full numerical results were not extracted.
- **Method described:** Caco-2 cells; Western-blot ABCG2 measurement after 24-hour exposure to progesterone, estradiol, or testosterone at nominal 1, 10, or 100 µM; orphan-receptor inhibitor conditions.

**Reported findings retained in the committed extract:**
- {"finding": "All three hormones increased ABCG2 at all three nominal concentrations tested.", "details": "The minimum tested active concentration was 1 µM; fold changes were not extracted."}
- {"finding": "PXR and FXR inhibition reduced the testosterone-associated increase, but ABCG2 remained above control."}
- {"finding": "CAR and PXR inhibition reduced the estradiol-associated increase, while PXR and FXR inhibition prevented the progesterone-associated increase."}

**Correction or scope gain:**
- The correct attribution is Slepnev et al., not Klyushova et al.
- The publisher abstract supports nominal 1, 10, and 100 µM culture conditions and PXR/FXR involvement. It does not establish free-tissue exposure or justify a serum-total or serum-free testosterone multiplier.

**Scope notes:**
- This In Vitro result does not support direct androgen-receptor repression; androgen-receptor involvement was not itself excluded by the reported inhibitor design.
- It does not establish a physiological testosterone effect, clomiphene mechanism, or human intestinal urate-flux effect.

#### P04 — MacLean C, Moenning U, Reichel A, Fricker G (2008)

- **Title:** Closing the gaps: a full scan of the intestinal expression of P-glycoprotein, breast cancer resistance protein, and multidrug resistance-associated protein 2 in male and female rats
- **PMID:** 18378562; **DOI:** 10.1124/dmd.108.020859
- **Evidence level:** **Animal Model**
- **Verification tier:** Primary PubMed abstract verified on 2026-07-27; no effect-size estimate was available in the abstract.
- **Method described:** Male and female rats; qRT-PCR and Western blot across duodenum, jejunum, ileum, colon, and a complete 3-cm segmentation of the intestine.

**Reported findings retained in the committed extract:**
- {"finding": "The authors reported that no sex-specific differences were observed for the intestinal transporter-expression scan."}

**Correction or scope gain:**
- The verified abstract supports a qualitative healthy-rat null across the studied intestinal scan.
- It supplies neither a healthy-human estimate nor a quantified human population threshold test.

**Scope notes:**
- This is Animal Model evidence and cannot resolve healthy-human intestinal ABCG2 sex stratification.

## Evidence boundaries

### Healthy-human baseline intestinal ABCG2 sex difference

- **Status:** `UNRESOLVED`
- **Evidence level:** **Mechanistic Extrapolation**
- **Boundary:** No direct GTEx/HPA sex-stratified intestinal values were extracted and the 1.5-fold threshold was not tested.

### Healthy-rat baseline intestinal ABCG2 sex difference

- **Status:** `NO_DIFFERENCE_REPORTED`
- **Evidence level:** **Animal Model**
- **Boundary:** MacLean et al. 2008 reported no sex-specific difference in the rat intestinal transporter-expression scan. This does not estimate a healthy-human effect.

### Q140K disease-state sex interaction

- **Status:** `SUPPORTED_IN_MOUSE_MODEL`
- **Evidence level:** **Animal Model**
- **Boundary:** Hoque et al. 2020 reported sex-dependent urate phenotypes in Q140K mice. The verified like-for-like Western comparison is 78% jejunal versus 44% renal reduction; the prior 88% value is not retained.

### Direct androgen-receptor repression of intestinal ABCG2

- **Status:** `NOT_SUPPORTED_BY_THESE_SOURCES`
- **Evidence level:** **In Vitro**
- **Boundary:** Slepnev et al. 2023 reported increased Caco-2 ABCG2 after nominal 1, 10, and 100 µM testosterone and implicated PXR/FXR with inhibitor conditions. AR was not tested or excluded, and no serum-total or serum-free multiplier is emitted.

### Clomiphene, intervention selection, or uricase response

- **Status:** `OUT_OF_SCOPE`
- **Evidence level:** **Mechanistic Extrapolation**
- **Boundary:** COMP-017 did not test clomiphene, select an intervention, or estimate Q141K-conditioned response to a gut-lumen uricase.

## Reproduction boundary

This script deterministically validates and renders the committed inputs. It does not retrieve literature, reconstruct missing GTEx/HPA values, or upgrade any record beyond its stated verification tier.
