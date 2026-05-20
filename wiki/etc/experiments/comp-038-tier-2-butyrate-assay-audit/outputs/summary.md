# comp-038 — Tier 2 Butyrate Assay Audit

**Run timestamp:** 2026-05-20T15:09:12+00:00  
**Mode:** Codex synthesis from local source packet; no OpenRouter model calls.  
**Overall verdict:** **YELLOW**

## Verdict

A ready-to-adopt simple/home colorimetric or breath-based butyrate assay did **not** surface. Two plausible Tier 2 candidates did surface, but both need verification before wet-lab adoption:

1. **HPLC-UV SCFA + lactate assay for bacterial culture supernatants — YELLOW.** Best near-term OE candidate for engineered-strain / culture-supernatant work. PMID 23542733 reports an HPLC-UV method for four SCFAs plus lactate in in vitro fermentation supernatants, with mM-range calibration compatible with culture outputs. It still requires HPLC access and paired GC-MS validation on OE samples.
2. **Electrochemical fecal SCFA profiling with ANN deconvolution — YELLOW.** Best stool-specific Tier 2 direction. PMID 42041444 reports rapid fecal SCFA profiling with electrochemical fingerprints and ANN-based decoupling, but it is an emerging research platform, not an off-the-shelf validated assay.

Rejected for current OE Tier 2 butyrate quantification:

- **Breath hydrogen / methane — RED.** Useful as broad fermentation/transit/adherence proxy, not butyrate-specific quantification.
- **Generic free-fatty-acid colorimetric kits — RED.** Abcam ab65341 explicitly excludes acetic, propionic, and butyric acids.
- **BHB / 3-hydroxybutyrate assays — RED.** Wrong analyte: ketone body, not microbial butyrate.
- **Butyric-acid / SCFA ELISA kits — RED-provisional.** Vendor claims exist, but no PubMed/GC-MS validation surfaced; require specificity and spike-recovery before consideration.

## Five-Trajectory Synthesis

| Trajectory | Lens | Main conclusion |
|---|---|---|
| 1 | Commercial colorimetric / kits | No validated plug-and-play butyrate colorimetric kit surfaced; generic FFA kits are false friends. |
| 2 | Analytical chemistry / culture | HPLC-UV is plausible for culture supernatants, not stool/home. |
| 3 | Breath proxies | Breath H2/CH4 measures fermentation broadly, not butyrate. |
| 4 | Biosensor / point-of-care | Electrochemical fecal SCFA profiling is the most promising stool-specific future Tier 2 path. |
| 5 | OE matrix fit | Split the problem: culture-supernatant Tier 2 is easier than stool/serum Tier 2; GC-MS remains the anchor. |

## Ranked Candidates

| Rank | Candidate | Verdict | Why | Required before use |
|---|---|---|---|---|
| 1 | HPLC-UV SCFA + lactate assay for bacterial culture supernatants | **YELLOW** | Compatible with mM fermentation supernatants; method exists in PubMed snapshot. | Full text PMID 23542733; butyrate-specific recovery/precision; OE spike-recovery; paired GC-MS. |
| 2 | Electrochemical fecal SCFA profiling with ANN deconvolution | **YELLOW** | Best stool-specific Tier 2 direction; fecal SCFA-focused. | Full text PMID 42041444; butyrate-specific reference correlation; external fecal validation. |
| 3 | Butyric-acid / SCFA ELISA kits | **RED-provisional** | Vendor claims but no validation surfaced; specificity concern. | Protocol, cross-reactivity, spike recovery, GC-MS comparison. |
| 4 | Breath H2/CH4 | **RED** | Fermentation proxy, not butyrate-specific. | Direct breath-to-butyrate validation, if it exists. |
| 5 | Generic FFA colorimetric kits | **RED** | Representative protocol excludes SCFAs. | Reject unless SCFA-specific validation appears. |

## Decision for OE

Use **GC-MS as the Tier 3 anchor**. For the first Tier 2 validation experiment, prioritize one of two tracks:

- **Culture-supernatant track:** HPLC-UV vs GC-MS on sodium-butyrate standards + engineered-strain / fermentation supernatants.
- **Stool track:** electrochemical fecal SCFA platform vs GC-MS, only after full-text review confirms butyrate-specific performance.

Do **not** build around breath hydrogen or generic FFA kits for butyrate quantification.

## Limitations

- PubMed snapshot is title/abstract metadata, not full-text verification.
- Vendor and patent search was targeted, not exhaustive.
- Commercial ELISA claims remain unverified and should not drive spend.
- No non-English corpus pass was run; revisit only if the analytical-chemistry source base remains sparse after full-text review.
- The five trajectories were performed in-session by Codex to avoid OpenRouter spend, not by five independent paid model calls.

## Key Sources

- PMID 23542733 — HPLC-UV method for SCFAs + lactate in in vitro fermentation.
- PMID 42041444 — rapid electrochemical fecal SCFA profiling.
- PMID 41082646 — exhaled breath condensate SCFAs do not track induced serum SCFA increases.
- PMID 1486849 / 8049636 / 21712835 / 27276436 / 41952402 — breath H2/CH4 fermentation proxy literature.
- Abcam ab65341 protocol v17a — generic FFA kit explicitly not designed for acetic, propionic, or butyric acid.
