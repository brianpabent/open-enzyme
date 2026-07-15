---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-038
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-038

Canonical review log: [`logs/comp-reviews/2026-07-15-comp-038-eeab5b5.md`](../../logs/comp-reviews/2026-07-15-comp-038-eeab5b5.md)

ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-038

## Reviewed snapshot
Independent reviewer: OpenAI API reviewer. Reviewed daemon snapshot `eeab5b53054b93544c428a476dad06a8f8fe2621` as supplied in the artifact bundle and by read-only repository tools where available. The inspected substantive files matched the supplied paths/content for the experiment outputs and explicit wiki pages, but repository fixed-string search failed because `rg` was unavailable, and the validation page / some affected pages could not be fully searched after tool-result budget exhaustion.

## Bottom-line verdict
**Action required.** The original 2026-05-20 YELLOW assay-landscape conclusion is broadly plausible and internally consistent for an abstract-level desk audit. The new 2026-07-14 `outputs/summary.md` full-text-verification addendum, however, is not backed by a reproducible verification artifact, source excerpts, updated `results.json`, or updated provenance. It also conflicts with stale or contradictory downstream wiki text, especially the interpretive page’s older “electrochemical FAILS” section.

## Implementation and constraint closure
The implemented experiment is a literature-synthesis runner, not a physical assay model. `analyze.py` can:

- read `inputs/query-strategy.json` and `inputs/model-config.json`;
- fetch PubMed title/abstract metadata into `outputs/pubmed-snapshot.json`;
- write a Codex packet;
- optionally call OpenRouter roles;
- write `outputs/results.json` and a generated summary for the original first pass.

For the original 2026-05-20 run, the code/output closure is mostly coherent: the query plan was broad enough to find HPLC-UV, electrochemical fecal SCFA profiling, breath proxy literature, false-positive BHB / GHB / generic FFA entries, and ELISA-vendor ambiguity. The run honestly states no OpenRouter calls and that the N=5 trajectories were performed in one Codex session.

For the **2026-07-14 addendum**, implementation closure fails:

- No code path in `analyze.py` performs full-text retrieval, PDF parsing, DOI retrieval, extraction tables, or primary-source quote capture.
- `outputs/results.json` still says “full text has not yet been extracted for key candidates” and recommends a future full-text/protocol verification pass.
- `inputs/provenance.md` is still frozen to the 2026-05-20 abstract-level PubMed snapshot and does not record a 2026-07-14 full-text verification source list, commands, extracted fields, or reviewer.
- `outputs/pubmed-snapshot.json` contains abstracts, not full text. The added HPLC and electrochemical details are partly present in PubMed abstracts; this does not establish full-text verification.
- The addendum says verification was “against primary sources (PubMed).” PubMed abstracts are not the same thing as publisher/PMC full text, and the artifact does not include full-text excerpts or PDFs.

Constraint closure by assay:

- **HPLC-UV / De Baere 2013:** The abstract supports culture-supernatant matrix, liquid-liquid diethyl-ether extraction, acidification to pH < 2, UV 210 nm, 0.5–50 mM calibration, r 0.9951–0.9993, LOD 0.13–0.33 mM, LOQ 0.5–1.0 mM. This fits high-mM culture supernatants but does **not** cover the whole configured “100 µM to 50 mM” culture range at the low end. It is Tier 2-lab / community-biolab at best, not home-tier, and requires HPLC access plus solvent handling.
- **Electrochemical + ANN / Gu 2026:** The PubMed abstract in the artifact supports fecal matrix, gold-chip voltammetry, esterification/dissociation pretreatment, ANN decoupling, GC-MS comparison in n=30 independent fecal test cohort, and butyric-acid MAE/RMSE 0.029/0.034 mM. This makes it a plausible stool-track candidate. Remaining constraints are hardware availability, ANN/model reproducibility, source-cohort external validity, sample pretreatment complexity, and independent validation.
- **Breath H₂/CH₄:** The artifact supports rejection as a butyrate-specific quantification assay. Breath gases are fermentation/transit proxies, not butyrate concentration measurements.
- **Generic FFA kits:** The artifact cites Abcam ab65341 protocol exclusion of acetic, propionic, and butyric acid. The protocol itself is not included, so the claim is not independently primary-source verified within the artifact, but the conclusion is plausible and appropriately conservative.
- **SCFA/butyrate ELISA kits:** The RED-provisional treatment is appropriate. No PubMed/GC-MS validation surfaced in the supplied snapshot; specificity for an 88-Da analyte remains unclosed.
- **Serum butyrate:** The query scope included serum, but no viable serum Tier 2 assay emerged; summaries should keep the result matrix-specific.

Stored-but-unused heuristic findings: most flagged JSON leaves are documentation/config fields or only enter dynamically through `json.dumps(model_config)` / `json.dumps(query_strategy)` in prompts. `target_concentration_ranges` is not directly used in scoring logic except through prompt inclusion and separate hardcoded judge-prompt ranges. `run.final_green_requires_full_text_or_protocol_evidence` is a policy field but not mechanically enforced except through prompt text. This is acceptable for an LLM synthesis experiment if documented, but it reinforces that the addendum is not reproducibly generated.

## Summary-fidelity audit
Original `README.md`, `outputs/results.json`, and the pre-addendum portions of `outputs/summary.md` agree: comp-038 was a PubMed title/abstract + targeted vendor first pass, YELLOW, with full-text verification still required. The addendum breaks that contract unless supporting evidence is added.

Key mismatches:

1. **`outputs/summary.md` addendum vs `outputs/results.json`:** Addendum says full-text verification gap is closed; `results.json` says full-text extraction has not been done and recommends it as next step.
2. **`outputs/summary.md` addendum vs `inputs/provenance.md`:** Provenance remains frozen to 2026-05-20 and does not record the 2026-07-14 full-text verification.
3. **Interpretive page contradiction:** `wiki/tier-2-butyrate-assay-audit-computational.md` contains both:
   - a 2026-07-14 resolution saying Gu 2026 electrochemical-ANN is validated and the older “electrochemical FAILS” claim is retracted; and
   - a later “Full-text verification — completed 2026-06-01” table saying Electrochemical + ANN **FAILS** due to vendor-locked hardware / unreleased ANN / GC-MS prerequisite.
   These cannot both remain as authoritative.
4. **`wiki/computational-experiments.md`:** The comp-038 entry partially reflects HPLC full-text verification, but still frames electrochemical only as “promising but research-platform grade” and keeps “next gate: full-text/protocol verification + small paired validation,” which is stale if the addendum is accepted.
5. **Validation references:** Multiple pages now refer to `validation-experiments.md` §1.31 as the wet-lab gate. The supplied dashboard excerpt did not show §1.31, and I could not fully verify the anchor text due tool budget exhaustion. This anchor must be checked and reconciled.
6. **Downstream re-anchoring claim:** The addendum says downstream wiki pages “re-anchor to the primary sources directly.” Some pages do, but the interpretive page still includes contradictory historical text and some pages still cite comp-038 as if the artifact itself contained the full-text layer.

The overall scientific conclusion should stay conservative: **YELLOW / candidate-selection improved, wet-lab spike/recovery and paired GC-MS still required.** The addendum’s “VERIFIED” labels are acceptable only if the primary-source extraction artifact is committed and the wording clearly distinguishes “source details verified” from “OE method validated.”

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/summary.md` | generated_output + trigger_update | Yes | Original YELLOW summary is coherent. New full-text addendum is unsupported by a reproducible verification artifact and conflicts with `results.json` / provenance. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/results.json` | generated_output | Yes | Supports the original abstract-level first pass only; still says full-text extraction is a future limitation. Needs update or separate addendum artifact. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/pubmed-snapshot.json` | generated_output | Yes, via supplied first chunk plus repository tail read | PubMed snapshot contains title/abstract metadata. It supports candidate discovery and some method details but not full-text verification. Tail includes PMID 42041444 abstract with GC-MS validation metrics. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/codex-synthesis-packet.md` | generated_output | Yes, via supplied first chunk plus repository tail read | Source packet is consistent with 2026-05-20 abstract-level synthesis; no full-text addendum support. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/.gitkeep` | generated_output / placeholder | No | Non-substantive placeholder omitted from bundle; not load-bearing, but not inspected. |
| `wiki/tier-2-butyrate-assay-audit-computational.md` | affected wiki page | Yes, supplied | Contains contradictory 2026-06-01 “electrochemical FAILS” section and 2026-07-14 retraction/resolution. Change required. |
| `wiki/computational-experiments.md` | affected wiki page | Yes, supplied comp-038 section | Partially updated; still stale on electrochemical verification and next-gate wording. Change required if addendum stands. |
| `wiki/validation-experiments.md` | affected wiki page | Partially | Supplied excerpts show §1.14 but not enough to verify §1.31 anchor. Must verify anchor and reconcile comp-038 references. |
| `wiki/genotype-informed-supplement-workflow.md` | affected wiki page | Yes, supplied | Still broadly consistent that butyrate input verification is a gap; may need nuance that electrochemical fecal SCFA is a genuine stool-track candidate, not failed, if addendum accepted. |
| `wiki/quantification-ladder.md` | affected wiki page | Yes, read by tool | Mostly consistent with 2026-07-14 framing; relies on primary-source verification not present in comp artifact. |
| `wiki/open-questions.md` | affected wiki page | Partially, relevant sections read | Mostly consistent with corrected 2026-07-14 electrochemical retraction, but contains wording that the committed artifact remains abstract-level. Needs reconciliation after artifact update. |
| `wiki/mechanical-flare-triggers.md` | affected wiki page | Yes, read by tool | Uses comp-038 only for the butyrate input-verification gap; no immediate change required unless the workflow claims are upgraded. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| PubMed snapshot = 27 queries / 74 records | `results.json`, `pubmed-snapshot.json`, `README.md` | Fetched by `analyze.py --prepare-codex`; summarized in outputs | Direct artifact available | Verified by inspection. |
| Five Codex synthesis trajectories, no OpenRouter calls | `results.json`, `summary.md`, `README.md`, `provenance.md` | Manual in-session synthesis from packet; not reproduced by code | Internal provenance only; no model transcript beyond `results.json` | Acceptable for this LLM literature-synthesis subtype if kept as YELLOW/provisional. |
| HPLC-UV candidate: 0.5–50 mM, r 0.9951–0.9993, LOQ 0.5–1.0 mM, UV 210 nm, pH<2, diethyl ether extraction | PubMed abstract in `pubmed-snapshot.json`; addendum in `summary.md` | Used to rank HPLC-UV as culture-supernatant Tier 2-lab candidate | Abstract supports these details; full text not included | Candidate plausible, but “full-text verified” not established by artifact. Also low-end 100 µM culture range is below LOQ. |
| HPLC-UV is underivatized | `summary.md` addendum; PubMed abstract describes direct UV after extraction/acidification | Supports “simpler than derivatized HPLC” framing | Abstract supports no derivatization, but primary full text absent | Supported at abstract level; full-text provenance missing. |
| HPLC-UV is suitable for culture supernatants, not stool/home | `results.json`, `summary.md`, wiki pages | Core verdict | PubMed abstract and matrix statement support culture; no stool data | Supported. |
| Electrochemical-ANN candidate: GC-MS-validated fecal n=30, butyric MAE/RMSE 0.029/0.034 mM | Tail of `pubmed-snapshot.json`; `summary.md` addendum | Used to upgrade/retract “electrochemical fails” | PubMed abstract supports metrics; full text not included | Promising stool candidate supported at abstract level; “full-text verified” and hardware/protocol claims need committed source extraction. |
| Electrochemical hardware = disposable three-electrode planar gold chip + DPV/CV + ANN + dual pretreatment | `summary.md` addendum; PubMed abstract | Supports remaining hardware/reproducibility gates | Abstract supports most; full text absent | Plausible; source extraction needed for load-bearing adoption claims. |
| Direct linear models fail in fecal matrices; ANN suppresses matrix effects | `summary.md` addendum; PubMed abstract | Supports ANN necessity and non-simple adoption | Abstract supports | Supported at abstract level. |
| Generic FFA kit Abcam ab65341 excludes acetic/propionic/butyric acids | `results.json`, `summary.md` | Rejects generic FFA kits | Citation string only; protocol not included | Plausible but not primary-source verified in artifact. |
| Breath H₂/CH₄ is fermentation proxy, not butyrate quantification | `results.json`, `summary.md`, PubMed snapshot breath records | Rejects breath Tier 2 butyrate assay | Abstract corpus supports broad proxy conclusion | Supported. |
| EBC SCFAs do not track serum SCFA increases | PMID 41082646 abstract in `pubmed-snapshot.json` | Rejects respiratory SCFA proxy | Abstract supports | Supported at abstract level. |
| SCFA/butyrate ELISA kits lack validation and remain RED-provisional | `results.json`, `summary.md` | Rejects kit spend | Absence finding from PubMed/vendor scan; vendor scan not machine-readable | Conservative and acceptable, but vendor evidence not fully reproducible. |
| “Full-text verification gap closed” | `summary.md` addendum | Upgrades evidence status and downstream wiki wording | No full-text artifacts, extraction table, source excerpts, or updated provenance | Unsupported as committed; action required. |
| `validation-experiments.md` §1.31 is the remaining wet-lab gate | `summary.md` addendum; interpretive page; quantification/open-questions pages | Routes next wet-lab step | Anchor not fully verified in supplied/read excerpts | Must verify and reconcile. |
| `target_concentration_ranges` in query strategy | `inputs/query-strategy.json`, packet prompt | Prompt context; not deterministic code scoring | Config documented | Acceptable for LLM synthesis; note HPLC LOQ does not cover 100 µM lower culture bound. |

## Affected wiki pages
- `wiki/tier-2-butyrate-assay-audit-computational.md` — **change required** — contains mutually inconsistent 2026-06-01 “Electrochemical + ANN FAILS” table and 2026-07-14 “electrochemical retracted as error / genuine stool candidate” resolution. Must collapse to one current interpretation and preserve the older error only as clearly superseded history.
- `wiki/computational-experiments.md` — **change required** — comp-038 entry partly reflects HPLC full-text verification but not the Gu 2026 metrics or the changed full-text-verification status; “next gate: full-text/protocol verification” is stale if the addendum is accepted.
- `wiki/validation-experiments.md` — **change required / verification required** — multiple pages point to §1.31 as the paired HPLC-UV/electrochemical-vs-GC-MS wet-lab gate; I could not fully verify the section/anchor. Ensure the section exists, is indexed, and has success criteria matching the corrected comp-038 interpretation.
- `wiki/quantification-ladder.md` — **already mostly consistent, but provenance caveat required** — correctly treats HPLC-UV as culture-supernatant candidate and electrochemical-ANN as stool candidate, but it asserts primary-source verification not currently documented in the comp artifact.
- `wiki/open-questions.md` — **change required after artifact update** — relevant section now says the butyrate corner is partially de-risked and electrochemical failure was wrong, but it also references primary-source verification outside the abstract-level comp artifact. Reconcile once the extraction artifact is committed.
- `wiki/genotype-informed-supplement-workflow.md` — **mostly consistent / minor update required** — still correctly says butyrate input verification is not workflow-ready. If the electrochemical stool-track candidate is retained, the page should distinguish “genuine stool research-platform candidate” from “ready user-facing input-verification assay.”
- `wiki/mechanical-flare-triggers.md` — **already consistent** — uses comp-038 only to support the butyrate input-verification attribution gap; no immediate content change unless the butyrate assay becomes operational.
- `wiki/purine-degrading-bacteria.md` — **not inspected; search required** — README names it as informed by comp-038, and butyrate/product-measurement claims could be affected.
- `wiki/quantification-ladder.md`, `wiki/genotype-informed-supplement-workflow.md`, `wiki/open-questions.md` — **separate “already reconciled vs still action” pass required** once repository search works; `grep_repo` failed because `rg` was missing.

## New connections or implications
The important cross-corpus implication is matrix-splitting:

- **Culture-supernatant SCFA quantification** and **stool SCFA profiling** should no longer be treated as one Tier 2 assay problem. HPLC-UV is a plausible community-biolab culture-supernatant track; electrochemical-ANN is a plausible stool research-platform track; neither is home/kitchen Tier 2.
- The electrochemical-ANN candidate, if the full-text extraction is confirmed, affects more than comp-038: it weakens broad “no stool Tier 2 surface exists” language and should be represented as “no workflow-ready surface yet; one research-platform candidate exists.”
- The HPLC-UV lower LOQ (0.5–1.0 mM) means it may miss low-output engineered-strain or early fermentation samples around 100 µM. The validation design should include low-end spike/recovery, not only mM standards.
- The original desk-audit methodology is adequate for candidate discovery but not for evidence upgrades. Future agentic-literature-synthesis comps need a separate “source-extraction artifact” format when a later primary-source verification pass changes downstream claims.

## Required actions
1. **Commit a 2026-07-14 verification artifact** under comp-038, e.g. `outputs/full-text-verification-2026-07-14.md` or JSON, containing for each source: DOI/PMID, access path, full-text/protocol availability, exact extracted method fields, quotes or bounded excerpts, page/section/table references where possible, and reviewer/date. Verification criterion: every “VERIFIED” claim in `outputs/summary.md` maps to a row in this artifact.
2. **Update `outputs/results.json` and `inputs/provenance.md`** or add an explicit second-run provenance file so the artifact no longer simultaneously says “full text not extracted” and “full-text gap closed.” Verification criterion: `results.json`/provenance accurately distinguish 2026-05-20 abstract-level run from 2026-07-14 manual/full-text addendum.
3. **Reconcile `wiki/tier-2-butyrate-assay-audit-computational.md`.** Remove or clearly supersede the 2026-06-01 table saying electrochemical-ANN FAILS. Verification criterion: the page has one current verdict for Gu 2026, with hardware/ANN/external-validation caveats but no contradiction.
4. **Update `wiki/computational-experiments.md` comp-038 entry.** Verification criterion: entry reflects HPLC full-text details, Gu 2026 butyric-acid MAE/RMSE if accepted, and states the next gate as paired spike/recovery + GC-MS / independent validation, not “full-text verification” if that is now closed.
5. **Verify and reconcile `validation-experiments.md` §1.31.** Verification criterion: the anchor exists, is linked from the dashboard if decision-relevant, and separately specifies culture-supernatant HPLC-UV vs GC-MS and stool electrochemical-ANN vs GC-MS criteria if both are retained.
6. **Run a corpus-wide affected-page search once repository search works.** Search by `42041444`, `electrochemical FAILS`, `HPLC-UV`, `butyrate assay`, `SCFA ELISA`, `De Baere`, `Gu et al.`, and `validation §1.31`. Verification criterion: no page still claims electrochemical stool SCFA profiling “fails / do not re-surface” unless clearly marked as superseded history.
7. **Tighten wording of “full-text verified.”** Verification criterion: all pages distinguish “primary-source method details verified” from “OE assay validated.” The latter remains untrue until spike/recovery and paired GC-MS are completed.

## Review limits
I did not execute `analyze.py`. Primary-source full texts for De Baere 2013, Gu 2026, Abcam ab65341, or vendor ELISA protocols were not available in the artifact and were not independently retrieved. Repository fixed-string search failed because the `grep_repo` tool backend could not find `rg`, so affected-page discovery relied on supplied explicit pages and direct reads. The `validation-experiments.md` section containing §1.31 was not fully inspected before tool-result budget exhaustion. The non-substantive `outputs/.gitkeep` placeholder was not inspected. No `reviews/` directory exists in the comp folder, so there were no prior comp-local review logs to defer/read.
