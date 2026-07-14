# Sulforaphane lit scan — synthesis (2026-07-14)

Three-track scan (Western clinical / Western mechanistic / East Asian multilingual) against the corpus baseline (newest prior citation: Wang 2022, PMID 36371056). Full track outputs: `trackA-`, `trackB-`, `trackC-*.md`. This is a synthesis for review; **no `wiki/` files were touched.**

## The one-line verdict

The scan **does not strengthen** sulforaphane's gout case — it **sharpens and partly weakens** it. There is still zero human urate/gout data; two new human RCTs complicate the systemic-anti-inflammatory assumption; and the mechanistic refresh turns up a *contradictory* ABCG2 signal plus an unsupported internal claim (Q141K rescue). The genuinely valuable new material is (a) formulation/bioavailability quantification, (b) a metabolite-pool reframing of the priming mechanism, and (c) a Chinese renal-protection angle absent from Western literature.

## Cross-track confirmations (independent tracks, same finding)

1. **Human urate/gout evidence = ZERO, triangulated.** Track A: 0 ClinicalTrials.gov trials with a gout/HUA/uric-acid endpoint (of 116 SFN trials total); PubMed direct = Wang 2022 only. Track C: CiNii 0 hits every SFN×urate combination; CQVIP surfaced no human urate trial. Not a retrieval gap — a real absence.
2. **SFN-metabolite priming reframing** independently surfaced by Track A (Andrade/Pagliarani 2026, PMID 41572056) and Track B (same paper). Parent SFN + its GSH/Cys/NAC conjugates all suppress TLR4/NLRP3/NF-κB/IL-1β, but **only parent SFN drives Nrf2 nuclear translocation** → a large share of priming suppression runs through TLR4/NF-κB and the longer-lived metabolite pool, not Nrf2. Genuine post-2022 refinement.

## Genuinely new since 2022

| Finding | Source | Evidence | Why it matters |
|---|---|---|---|
| Human: oral GR→SFN lowers IL-1β/TNF-α gene expression **in skin, NULL in blood/PBMC** | Chien 2025, *Metabolites*, PMID 40559384, n=18 RCT | Clinical Trial | First human in-vivo IL-1β suppression — but the blood-compartment null is exactly the compartment gout needs. |
| Human: broccoli-sprout SFN gave a **mild PRO-inflammatory (hormetic)** shift under caloric load (CCL-2 ↑, p=0.017) | van Steenwijk 2023, *Front Nutr*, NCT05146804, n=12 RCT | Clinical Trial | Directionally contradicts naive "SFN suppresses systemic inflammation." Human effect may be biphasic. |
| Human: mustard myrosinase **doubles SFN bioavailability** (39.8% vs 18.6%) | Mastaloudis 2026, *Sci Rep*, n=16 RCT | Clinical Trial | Human validation + quantification of the corpus's "add myrosinase" hack. Even optimized, only ~40% bioavailable. |
| Formulation: whey-protein microencapsulation → bioavailability **54% vs 16%** dried broccoli | Ali Redha 2025, *Food Funct*, PMID 39431890 | In Vitro (INFOGEST+Caco-2) | Strongest new delivery lever; ~3.4× over dried broccoli. |
| Youngest (2-day) sprouts carry the **most** SFN; degrades during GI digestion | de Vasconcelos Lopes 2025, PMID 40327164 | In Vitro | Corrects "older/greener sprout = more SFN" intuition. |
| **NQO1\*2** carriers under-excrete SFN — human responder-stratification variant | van Steenwijk 2023, PMID 37485383 | Clinical Trial | A pharmacogenetic responder axis analogous to ABCG2-Q141K. |
| **Chinese/unique:** SFN protects human renal tubular cells (HK-2) from urate-induced apoptosis via ER-stress IRE-1/JNK inhibition (10/20/40 μM) | CN, DOI 10.3760/cma.j.cn431460-20190505-00032 | In Vitro | A **kidney-protection / UPR** angle absent from the macrophage/NLRP3-centric Western literature. Two-model agreement. |
| **Pending human readout:** SFN 4 g/day × 2 mo in CKD, measuring PBMC NLRP3/IL-1β/IL-18/hs-CRP | NCT04608903, results overdue/unposted | (pending) | First human inflammasome-output readout on SFN. Highest-value watch item. |

## Corpus-claim verification (Track B)

| Claim in corpus | Verdict | Action |
|---|---|---|
| Nrf2 EC50 ≈ 580 nM (J Med Chem 2019) | **CONFIRMED** — ChEMBL, 3 independent docs — but potent end of a ~30× assay range (580 nM translocation → 0.6–19 µM ARE-reporter) | Annotate as assay-specific, not "the" EC50. |
| Nrf2-independent inflammasome inhibition (Greaney 2015) | **CONFIRMED as prior; no new structural target** (no NEK7/GSDMD/cysteine resolution post-2022) | Keep; note metabolite reframing. |
| Food-grade HDAC inhibition | **CONFIRMED as a mechanism class** (Somers 2023, Sharma 2022, Fawad 2022 — active in intestinal epithelium) | Keep. |
| SFN → HDAC inhibition → **partial Q141K ABCG2 rescue "documented in vitro"** (gout-action-guide.md) | **UNVERIFIED — internal over-reach.** No SFN-specific Q141K paper. Corpus's own abcg2-modulators.md attributes Q141K rescue to vorinostat/romidepsin (Saranko 2013), not SFN. | **Downgrade** to Mechanistic Extrapolation; state SFN-specific Q141K rescue is untested. |
| Nrf2 → ABCG2 enterocyte induction (settled, platform-favorable) | **PARTIAL + CONTRADICTORY signal.** Ho 2023 (*Br J Pharmacol*, PMID 37476954): l-SFN is a **PXR antagonist** that can *lower* ABCG2 via the PXR arm — opposite direction. Net enterocyte direction unresolved. | **Flag** the ambiguity; stop presenting SFN→ABCG2 induction as settled. |
| Urate-synthesis drop implies **direct XO inhibition** | **UNVERIFIED — no evidence.** Wang 2022's effect is Nrf2-epigenetic, not direct XO. | Do not assert direct XO inhibition. |
| Wang 2022 = only SFN-hyperuricemia primary paper | **CONFIRMED still current** | No change. |

## Two findings that mirror the OE platform architecture

1. **Enzyme-activated in-situ delivery.** The Chinese HUA-rat study (Track C, DOI 10.26914/c.cnkihy.2022.033776 — the conference companion of Wang 2022) dosed **glucoraphanin + myrosinase**, i.e. precursor + activating enzyme for in-situ SFN generation in the gut — *not* preformed SFN. That is structurally the same idea as the koji/uricase gut-lumen enzyme-delivery thesis, and its mechanism was framed as **excretion-dominant**, aligning with the ABCG2/gut-sink axis. Worth noting as a precedent, not just a data point.
2. **Japanese white space is real.** 132 J-STAGE + 84 broccoli-sprout records, zero pointed at urate/gout (CiNii = 0 every combination). A large functional-food base that has never been aimed at hyperuricemia — genuine absence, and an open lane rather than a covered one.

## Recommended corpus edits (for Brian's go — none applied yet)

1. **`wiki/gout-action-guide.md`** (~line 131): rewrite the "HDAC inhibitor … partial Q141K rescue documented in vitro" sentence → SFN is a confirmed food-grade HDAC inhibitor; HDAC-class inhibitors (vorinostat/romidepsin) rescue Q141K trafficking in vitro; **SFN-specific Q141K rescue is untested (Mechanistic Extrapolation).**
2. **`wiki/abcg2-modulators.md`** + **`wiki/supplements-stack.md`**: add the ABCG2-direction ambiguity flag (Ho 2023 PXR-antagonist counter-signal). Stop presenting SFN→enterocyte-ABCG2 induction as settled/platform-favorable without the caveat.
3. **`wiki/supplements-stack.md`** / **`nlrp3-inhibitor-screen.md`**: annotate the 580 nM Nrf2 EC50 as assay-specific (nuclear-translocation; 0.6–19 µM across ARE reporters).
4. **New content**: the SFN-metabolite priming reframing (Pagliarani/Andrade 2026); the human-data-status reality (zero urate; Chien PBMC null + van Steenwijk hormesis complicate the systemic-anti-inflammatory story); the formulation/bioavailability numbers; NQO1\*2 responder axis; NCT04608903 as a watch item.
5. **Consider**: a dedicated `wiki/sulforaphane.md` dossier to centralize the currently-scattered (8-page) coverage — this scan is enough to seed it.

## Evidence-tier bottom line

SFN's **Tier 2** supplement ranking is unchanged and still correct — it rests on animal (Yang 2018, Wang 2022) + in-vitro (Greaney 2015) evidence. **Nothing promotable to a human urate/gout tier exists.** If anything, the new human inflammation data argues for *more* hedging on human-facing systemic-anti-inflammatory claims, not less.
