---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-016
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-016

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-016-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-016-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-016

## Bottom-line verdict

**Action required.** The qualitative verdict — **direct testosterone/androgen suppression of intestinal ABCG2 is weak/unconfirmed** — is directionally supported by the curated artifact and by already-updated downstream pages. However, the artifact-summary contract is not clean: primary-source verification remains unresolved for load-bearing numbers, the executable aggregation has hard-coded judgment and mislabeled output fields, the reproduction command/path is wrong from repo root, and some summaries still overstate or omit the later comp-017 physiological-concentration corrections.

## Implementation and constraint closure

**Question/model fit.**  
The experiment is a curated literature-mining aggregation, not an independent literature search or full-text verification. It can support the narrower claim: “given these 17 curated records, no included primary study directly shows T/DHT → lower intestinal ABCG2 in vivo.” It cannot by itself prove that no such study exists in the literature, because:

- the scan was abstract/WebSearch-summary level;
- WebFetch was 403-blocked;
- multilingual databases were not searched;
- no primary-source grep/full-text extraction is present in comp-016 itself.

**Implementation traced.**

- `inputs/studies.json` → `analyze.py` → `outputs/results.json` and `outputs/summary.md`.
- The executable uses:
  - `studies[]`
  - `direction_for_thesis`
  - `tissue_measured`
  - `evidence_tier`
  - `intervention`
  - `title`, `species`, `journal`, `year`, `key_finding`
  - `fetch_date`
  - `verdict_logic.claim_being_tested`
  - `verdict_logic.summary_judgment`
- Many heuristic “unused” leaves are genuinely documentation/provenance fields, not necessarily defects: `search_strategy`, `summary_counts`, magnitudes, caveats, platform relevance, authors, PMIDs, URLs, etc. They are stored for audit but not used by the script.

**Implementation concerns.**

1. **Hard-coded verdict component.**  
   `render_verdict()` sets `n_direct_supports_T_suppresses_intestinal = 0` by fiat rather than deriving it from structured input. This is acceptable only if the artifact is explicitly a manually curated evidence ledger, but it is not a robust executable classifier. If `studies.json` were updated with a directly supportive study, the script would still report zero unless the code changed.

2. **Load-bearing classification is a coarse heuristic.**  
   `is_load_bearing_for_intestinal_claim()` counts studies as load-bearing if they measure intestinal/Caco-2 tissue and the intervention string contains terms such as `testosterone`, `estradiol`, `q140k`, `q141k`, etc. This correctly selects S01/S03/S04 in the current file, but it is a string heuristic, not a biological proof of load-bearing status.

3. **Field-label mismatch in outputs.**  
   `direct_intestinal_sex_dimorphism_studies` is populated with all `load_bearing_intestinal_studies`, including **S04_Klyushova2023**, which is a Caco-2 testosterone-exposure study, not a sex-dimorphism study. The label should be changed or the contents filtered.

4. **Direct contradiction count excludes MacLean despite summary wording.**  
   `outputs/summary.md` says “Direct contradictory evidence (T → intestinal ABCG2 up; or no sex difference),” but the loop prints only `verdict.direct_contradicts_T_suppresses_intestinal_ABCG2`, which contains only S04. MacLean/S10 is classified as `CONTRADICTS` in `aggregation.by_direction`, and the rationale mentions it, but it is excluded from `direct_contradicts` because it lacks hormone/genotype intervention. That distinction may be defensible, but the heading and count should be clarified: S04 is the direct intestinal in vitro opposite-direction study; S10 is healthy-baseline sex-difference null evidence, not direct T-manipulation evidence.

5. **Stored manual summary counts are not reconciled with code output.**  
   `inputs/studies.json.summary_counts.by_direction_intestinal_specifically` lists neutral/no-difference and contradicting studies differently from `analyze.py`’s computed verdict fields. This is not fatal if `summary_counts` is documentation-only, but the artifact should mark it as non-executable or remove stale conflicts.

6. **Reproducibility path mismatch.**  
   README says:
   ```bash
   cd experiments/comp-016-t-abcg2-suppression-evidence-mining
   python3 analyze.py
   ```
   The actual tracked path is:
   ```bash
   cd wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining
   python3 analyze.py
   ```
   From repo root, the README command is not a valid reproduction path unless an untracked symlink exists.

**Constraint closure.**

This comp is not a kinetic or mass-balance model, so reaction-substrate/cofactor closure in the enzymology sense is mostly not applicable. The relevant “constraint” layer is biological operating regime:

- **Physiological concentration vs. experimental concentration:** Later comp-017 corrections are load-bearing. Yu 2021’s Caco-2 estradiol benzoate condition is described as strong-pharmacological (~100 µM, far above physiological serum E2), and Klyushova 2023 uses 1/10/100 µM hormones, also supraphysiological for free testosterone. comp-016’s outputs/summary and computational-experiments row do not fully carry this nuance, although `wiki-archive.md` does via a correction note.
- **Compartment:** The comp correctly distinguishes renal/systemic urate endpoints from intestinal ABCG2 measurements. Sakamoto/Yahyaoui/KNIGHT/ENIGI support androgen/sex-hormone effects on serum urate or FEUA, but not intestinal ABCG2.
- **Localization/access:** Caco-2 is an intestinal epithelial model but not normal differentiated small-intestinal epithelium in vivo; the artifact flags this caveat for Klyushova.
- **Time/exposure:** Klyushova’s 24h supraphysiological exposure and Yu’s pharmacological E2/OVX replacement design are not equivalent to chronic physiological male/female baseline. This should be consistently propagated.
- **Safety/off-target framing:** The artifact appropriately does not convert androgen/ADT/SERM observations into clinical advice. It does, however, make platform-design recommendations that depend on mechanism; those should remain Phase 0 and verification-gated.
- **Sensitivity/uncertainty:** The dominant uncertainty is not a numerical parameter range in the script. It is literature coverage and primary-source verification. The artifact acknowledges this, but the executable does not quantify uncertainty or search completeness.

## Summary-fidelity audit

**README vs code/output.**

- Top-line README verdict matches `outputs/results.json`: **WEAK / UNCONFIRMED**.
- README’s “3 studies load-bearing” matches the script output: S01, S03, S04.
- README appropriately discloses abstract/WebSearch-summary verification, but it still foregrounds quantitative numbers such as Hoque 88% and Sakamoto −0.66 mg/dL that are not primary-source verified in comp-016.
- README reproduction command path is wrong from repo root.

**`outputs/summary.md` vs `results.json`.**

- Broad verdict is consistent.
- Internal mismatch: summary text says direct contradictory evidence includes “T up; or no sex difference,” but the generated direct-contradiction list includes only S04. S10 appears elsewhere in aggregate counts and rationale.
- The output summary has not been regenerated/incorporated after the comp-017 correction note. It still presents Hoque 88% without the 78% Western-only nuance and does not carry Yu/Klyushova supraphysiological-concentration caveats in the key “reframing” section.

**Interpretive page / `wiki-archive.md`.**

- The archive is materially stronger than the generated output because it includes a post-comp-017 correction note:
  - Hoque 88% is combined Western + apical IHC; Western-jejunum-only is 78%.
  - Yu 2021 operates at strong-pharmacological E2 tier; physiological magnitude unestablished.
  - Klyushova hormone concentrations are supraphysiological and xenobiotic-sensor-like.
  - Healthy-baseline sex dimorphism is near-null.
- This correction note is crucial and should be reflected in the generated output summary, README top-line caveats, and index row.

**`wiki/computational-experiments.md`.**

- The comp-016 row is broadly consistent with the original artifact, but it remains “abstract-tier” and omits key comp-017 physiological-concentration corrections.
- The comp-017 row later corrects these points, so the corpus is partially reconciled, but the comp-016 row itself is still stronger than the corrected read warrants.

**Downstream pages inspected.**

- `wiki/androgen-urate-axis.md`: already heavily reconciled. It explicitly reframes from active androgen suppression to absent estradiol-positive signaling, flags verification pending, and notes near-null healthy-baseline magnitude.
- `wiki/abcg2-modulators.md`: already heavily reconciled and includes comp-017 corrections, including Yu/Klyushova supraphysiological nuance.
- `wiki/gut-lumen-sink.md`: mostly reconciled by later comp-044 reset; it no longer appears to rely strongly on the old structural-ceiling claim.
- `wiki/cross-validation.md`: contains the comp-016 reframe, but still quotes Hoque 88% and Yu 2021 without the full comp-017 concentration caveat in the Claim 1 section.
- `wiki/koji-endgame-strain.md`: includes a comp-016 footnote softening “structural ceiling” to “modest dose-response shift,” but still uses Hoque 88% as the headline and only lightly carries comp-017’s concentration/magnitude corrections.
- `wiki/hypotheses/H07-clomid-intestinal-er-antagonism.md`: already well reconciled; it explicitly incorporates comp-017 status updates and caveats.
- `wiki/validation-experiments.md`: dashboard still names §1.14 as “DHT + TNFα additive ABCG2 suppression...” This can be retained as a falsification experiment only if rewritten as a test of null/opposite DHT effect rather than assuming additive androgen suppression.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 17 curated studies | `inputs/studies.json`; `outputs/results.json` `n_studies_total` | Counted directly from `studies[]` | Artifact-internal only; no independent search reproduction | Internally reproducible, literature completeness unresolved |
| Zero primary studies directly show T/DHT suppresses intestinal ABCG2 in vivo | README; `verdict_logic`; hard-coded in `render_verdict()` | Hard-coded as `n_direct_supports_T_suppresses_intestinal = 0` | Based on abstract/WebSearch-summary scan; not exhaustive/full-text | Qualitatively plausible but not executable-proof; primary-source/search verification required |
| 3 load-bearing intestinal studies: S01/S03/S04 | `analyze.py`; `results.json` | Derived by tissue/intervention string heuristic | Artifact-internal classification | Reproducible for current JSON; heuristic should be documented |
| S04 Klyushova contradicts: testosterone increases ABCG2 in Caco-2 | `studies.json` S04; `results.json`; summary | Classified as `CONTRADICTS`; direct contradiction list | Abstract/WebSearch-summary in comp-016; comp-017 later full-text-read caveat | Direction likely supported; physiological relevance limited by supraphysiological concentrations |
| Klyushova concentrations 1/10/100 µM | `studies.json` S04 caveats; `wiki-archive.md` correction note | Not used numerically | Citation string / secondary extraction; comp-017 claims full-text re-read | Must be propagated wherever Klyushova is used as “T induces” evidence |
| S01 Hoque 88% intestinal ABCG2 protein loss; 53% heterozygote; 44% kidney | README; `studies.json`; output summary; wiki archive correction | Not used numerically except text | comp-016 says search-summary verified; comp-017 says 88% combined, 78% Western-only | Use 78%/88% distinction; do not quote 88% alone as Western-only or primary-verified by comp-016 |
| Female Q140K protected / no hyperuricemia | README; S01; wiki archive | Textual rationale | Search-summary in comp-016; comp-017 partial verification noted | Supported directionally; exact phenotype details require primary line verification if load-bearing |
| S03 Yu 2021 estradiol upregulates intestinal ABCG2 via PI3K/Akt | README; `studies.json`; output summary | Classified `SUPPORTS_ASYMMETRIC`; selected load-bearing | comp-016 abstract-tier; comp-017 notes pharmacological concentration | Mechanism exists at strong-pharmacological tier; physiological sex-dimorphism magnitude unestablished |
| MacLean 2008 no healthy rat intestinal ABCG2 sex difference | S10 in `studies.json`; output rationale | Classified `CONTRADICTS` in aggregate but excluded from direct contradiction list | Abstract-tier in comp-016; comp-017 says null strengthened | Important negative-baseline evidence; output headings/counts need clarification |
| Sakamoto 2018 ADT −0.66 mg/dL serum urate | README; S02; output summary | Classified `SUPPORTS_STRONG`, not load-bearing intestinal | comp-016 says abstract/search-summary verified | Useful systemic/renal-supporting number; should not be cited as intestinal ABCG2 evidence |
| No direct AR-ARE on ABCG2 promoter | README; output mechanism summary | Textual only | No executable source check; based on scan | Plausible but unresolved; should remain “not identified in this scan,” not absolute |
| Jeong 2015 androgen withdrawal → CREB/CRTC2 → BCRP in LNCaP | S07; output mechanism summary | Classified `SUPPORTS_MECHANISTIC`, not load-bearing intestinal | Abstract/WebSearch-summary | Mechanistic extrapolation only; cancer-line context must stay explicit |
| Verdict `WEAK_UNCONFIRMED` | `analyze.py`; `results.json`; output summary | Derived partly from hard-coded zero-support logic plus contradiction count | Artifact-internal judgment | Qualitative verdict acceptable; quantitative/executable derivation not fully closed |
| Reproduction command | README | User-facing reproducibility contract | Path in README omits `wiki/etc/` | Change required |

## Affected wiki pages

- `wiki/t-abcg2-suppression-evidence-mining-computational.md` — already mostly consistent / change required — stub points to archive correctly, but the archived artifact’s generated output and README need comp-017 correction propagation.
- `wiki/computational-experiments.md` — change required — comp-016 row should include the comp-017 caveat that Yu/Klyushova are supraphysiological and healthy-baseline sex dimorphism is near-null; avoid quoting Hoque 88% without the 78%/88% distinction.
- `wiki/androgen-urate-axis.md` — already consistent — inspected section already reframes mechanism, flags verification, and notes near-null healthy-baseline magnitude.
- `wiki/abcg2-modulators.md` — already consistent — inspected section includes comp-016/017 corrections and appropriate physiological-tier caveats.
- `wiki/gut-lumen-sink.md` — already mostly consistent — later comp-044 reset reduces dependence on comp-016’s structural-ceiling issue; no immediate comp-016-specific correction found.
- `wiki/cross-validation.md` — change required — Claim 1 section should import comp-017 nuances rather than leaving Hoque 88% and Yu PI3K/Akt as unqualified support for a male asymptote shift.
- `wiki/koji-endgame-strain.md` — change required — footnote is directionally updated but should avoid Hoque 88% as the sole headline and should carry the healthy-baseline near-null / pharmacological-tier caveats more clearly.
- `wiki/validation-experiments.md` — change required — §1.14 title/framing still assumes “DHT + TNFα additive ABCG2 suppression.” Reframe as a falsification assay testing DHT/T effects on ABCG2, including null/opposite-direction outcomes, not as an assumed additive suppression mechanism.
- `wiki/hypotheses/H07-clomid-intestinal-er-antagonism.md` — already consistent — explicitly incorporates comp-017 status updates and keeps the positive ER-antagonism mechanism open.
- `wiki/open-questions.md` — already partly consistent — includes reopened genotype/gut-sink questions and H07 links; no comp-016-specific correction required from inspected bundle.
- `wiki/androgen-natural-modulation.md` — unresolved — bundle omitted and tool budget prevented inspection; comp-016 output explicitly flags it for follow-up and it may still contain older androgen/ABCG2 or Clomid-UA framing.
- `wiki/prps-purine-biosynthesis-chokepoint.md` — already consistent / unaffected — references comp-015 rather than comp-016; no load-bearing comp-016 claim found in provided content.

## New connections or implications

1. **The strongest surviving platform implication is not “male structural ceiling”; it is “disease/genotype stress reveals transporter vulnerability.”**  
   Comp-016 plus comp-017 shifts the biologically grounded story from sex-hormone baseline suppression to Q141K/disease-state vulnerability plus pharmacological induction possibilities.

2. **The best wet-lab design should treat DHT/T as an unknown-direction factor.**  
   Because Klyushova points opposite and MacLean is null at baseline, validation §1.14 should not be framed as confirming DHT suppression. It should include DHT/T arms precisely to test suppression vs null vs induction.

3. **Renal/systemic androgen effects remain real but should be decoupled from intestinal ABCG2.**  
   Sakamoto, Yahyaoui, and Hosoyamada-type evidence supports a hormone–urate axis, but mostly renal/systemic. This decoupling matters for interpreting Clomid/TRT observations and for avoiding false attribution of serum-UA changes to intestinal ABCG2.

4. **The artifact demonstrates a useful “claim-splitting” pattern.**  
   “ABCG2 is sex-dimorphic in a urate-relevant way” and “androgens directly suppress intestinal ABCG2” are separate claims with different evidence. Downstream pages that combine them should be split similarly.

## Required actions

1. **Fix the reproducibility command in `README.md`.**  
   Owner surface: comp-016 README. Verification criterion: from repo root, the documented command uses `cd wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining && python3 analyze.py`.

2. **Regenerate or manually update `outputs/summary.md` to include comp-017 corrections.**  
   Owner surface: comp-016 generated outputs or a clearly labeled post-hoc correction block. Verification criterion: summary distinguishes Hoque 78% Western-only vs 88% combined, states Yu/Klyushova pharmacological/supraphysiological concentration caveats, and avoids presenting physiological sex-dimorphism magnitude as established.

3. **Repair output field labels and contradiction wording.**  
   Owner surface: `analyze.py` and `outputs/results.json`/`summary.md`. Verification criterion: `direct_intestinal_sex_dimorphism_studies` does not include non-sex-dimorphism studies such as S04 unless renamed; S04 direct opposite-direction evidence and S10 healthy-baseline null evidence are reported in distinct categories.

4. **Make verdict derivation either fully data-driven or explicitly manual.**  
   Owner surface: `analyze.py`/README. Verification criterion: either direct-support count is computed from structured per-study fields, or README states that `analyze.py` aggregates a manually curated evidence ledger and that “zero direct support” is a curator judgment embedded in code.

5. **Complete or clearly schedule primary-source verification for load-bearing numbers.**  
   Owner surface: comp-016 provenance and downstream pages. Verification criterion: Hoque, Yu, Klyushova, MacLean, Sakamoto claims have line-anchored primary-source/Paperclip verification or remain labeled summary-tier everywhere they are quoted.

6. **Update `wiki/computational-experiments.md` comp-016 row.**  
   Owner surface: computational-experiments index. Verification criterion: comp-016 row includes abstract-tier status plus comp-017 concentration/magnitude correction summary.

7. **Update `wiki/cross-validation.md` and `wiki/koji-endgame-strain.md` comp-016-dependent wording.**  
   Owner surface: those pages’ sex-dimorphic ABCG2 / structural-ceiling passages. Verification criterion: no unqualified “88%” or Yu physiological implication; healthy-baseline near-null and pharmacological-tier caveats are visible.

8. **Reframe `validation-experiments.md` §1.14.**  
   Owner surface: validation §1.14 title/protocol. Verification criterion: DHT/T is described as an unknown-direction test factor, with pre-specified interpretation for suppression, null, or induction.

9. **Inspect `wiki/androgen-natural-modulation.md` for stale comp-016 implications.**  
   Owner surface: omitted downstream page. Verification criterion: no remaining direct intestinal androgen-suppression or Clomid-UA mechanism claim is stronger than comp-016/017 support.

## Review limits

- I did not execute `analyze.py`; reproducibility was assessed by code and committed-output inspection only.
- Repository fixed-string search failed because the tool backend lacked `rg`; affected-page discovery relied on provided bundle plus targeted file reads.
- Tool-result budget was exhausted while reading `validation-experiments.md`, so the full §1.14 protocol body and omitted pages could not be inspected.
- Primary papers were not independently opened or line-grep-verified in this review. Provenance judgments therefore distinguish artifact-internal citation strings, WebSearch-summary extraction, and later comp-017 correction notes rather than claiming new primary-source verification.
- No medical or clinical recommendation is made; this is Phase 0 computational/literature-method review only.

---
## ✓ Actioned 2026-07-14
**Disposition: caveat/downgrade** (relabel/hygiene tier). Added a ⚠️ caveat banner to the interpretive page (or artifact README for comp-015) capturing the audit's headline finding — the qualitative direction holds, but the quantitative/verdict framing overstated what the model resolves. Deeper artifact fixes (reproducibility defects, provenance-tier labeling, code/summary mismatches, any recompute) remain in the Required-actions above as residuals for a focused follow-up.
