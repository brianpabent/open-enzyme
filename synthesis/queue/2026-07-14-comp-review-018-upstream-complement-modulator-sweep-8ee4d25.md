---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-018
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-018

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-018-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-018-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-018

## Bottom-line verdict

**Action required.** comp-018 is a useful literature-catalog artifact for upstream complement modulators, but the artifact-summary contract is not clean: README/outputs/index disagree on phase status, counts, tiering, and available files; the reproducible script only validates/rewrites a scope summary and does not reproduce the literature sweep; `outputs/summary.md` is referenced but not tracked; and several headline quantitative claims—especially rosmarinic-acid 5–10 µM and dietary-scale CP0 relevance—are stronger than the implemented artifact and provenance can support.

The biological verdict should remain **Phase 0 hypothesis-generating**: “documented anticomplement activity exists upstream of C5aR1” is supported as a literature-catalog conclusion; “dietary rosemary / luteolin / Houttuynia will modulate gout-relevant CP0 in vivo” is not resolved by this computation.

## Implementation and constraint closure

**Question/model fit.** The experiment asks which compounds have documented upstream complement activity and platform relevance. The implementation is a manually assembled literature database plus a minimal JSON/schema/count validator. That can answer “what did the search record catalog?” but not “which compounds operate at gout-relevant concentrations at MSU crystal sites.” The dominant hidden substitutions are:

- CH50/AP50 hemolysis or complement-depletion assays are treated as proxies for MSU-crystal complement inhibition.
- In vitro IC50/CH50 values are treated as candidates for physiological operating concentrations without a pharmacokinetic/mass-balance model in this comp.
- “FDA-GRAS source plant / dietary herb” is treated as evidence of access, not evidence of target-site exposure.
- “Upstream of C5a generation” is treated as CP0 relevance, but local joint, systemic plasma, gut mucosal, and gut-luminal complement are different compartments.

**Code/input/output trace.**

- `scripts/scope_validate.py` reads:
  - `inputs/targets.json`
  - `inputs/query-strategy.json`
  - `outputs/compounds.json`
- It validates only minimal required fields:
  - targets: `id`, `uniprot`, `node_class`, `msu_relevance`, `intervention_direction`
  - compounds: `name`, `compound_class`, `target_node`, `platform_relevance`
- It computes tier counts and ChEMBL coverage from the compound list, then writes `outputs/scope-summary.md`.
- It does **not**:
  - verify PMIDs, DOIs, IC50s, doses, species, assay format, ChEMBL records, or full-text line anchors;
  - reproduce the PubMed/Paperclip/ChEMBL sweep;
  - check consistency between `compounds.json.sweep_summary` and the actual `compounds` list;
  - check that `verification_status` exists per compound or per IC50;
  - validate unit conversions (`mM`→`µM`, `g/L`→`µg/mL`, etc.);
  - enforce retraction exclusion except as stored prose.

**Stored-but-unused / documentation-only findings.**

The heuristic “unused JSON leaf paths” are mostly documentation/provenance fields, not executable inputs. However, this is itself load-bearing: the validator does not consume `primary_sources`, `verification_gate_protocol`, `multilingual_sources_direct_read`, `fetch_date`, or source-translation metadata. Therefore the “verification gate” is a documented contract, not an implemented gate.

**Implementation defects / mismatches.**

- `README.md` references `outputs/summary.md`, but the tracked inventory and directory listing include only `outputs/compounds.json` and `outputs/scope-summary.md`.
- README says “32 compounds”; generated `scope-summary.md` says **33 compounds**.
- `compounds.json.sweep_summary.total_compounds_with_documented_activity` says **32**, while the actual list contains **33** entries.
- `compounds.json.sweep_summary.chembl_coverage.compounds_no_chembl` says **18**, but generated `scope-summary.md` computes **19 / 33**.
- `compounds.json.sweep_summary.tier_summary` says TIER_1 strong evidence = **6**, TIER_2 = **12**, TIER_3 = **14**, but generated tier counts are: TIER_1 = **1**, TIER_2 = **10**, TIER_3 = **12**, plus several out-of-scope/reference/repurposing categories.
- `scope_validate.py` truncates `msu_relevance` by first whitespace token, producing malformed summary rows such as `C5 | ... | the` and `MASP-2 | ... | narsoplimab-target;`.
- The README is Phase 1-stale: it says Phase 2 is queued, while the interpretive page and `phase-2/` artifacts say Phase 2 is complete.
- The README top-line remains rosmarinic-acid-forward; the current canonical wiki stub warns that Phase 1 was brief-contaminated and points to comp-020/Phase 2 for prioritization.

**Constraint closure.**

- **Reaction substrates/cosubstrates/products.** The target list covers C1q/C1r/C1s, MBL/MASP-2, C3 convertases, Factor B/D/H, properdin, DAF/CD55, CD59, C5 convertase, C5, C5aR1, and C1-INH. This is reasonable pathway coverage, but the compound table often records pathway-level hemolysis endpoints rather than direct molecular targets. For many entries, “target node” is inferred from CH50/AP50 or depletion-rescue context, not direct binding kinetics.
- **Operating concentration vs Km/Kd/IC50/CH50.** Not closed in comp-018. Rosmarinic acid has unresolved 5–10 µM vs 34 µM vs 137–182 µM assay spread; luteolin is ~170–190 µM; Houttuynia polysaccharides are mass-action µg/mL to mg/mL; Bupleurum is ~1 mg/mL. Whether these are achieved at gout-relevant complement sites is unmodeled here. Later comp-029 explicitly reframed rosmarinic acid as gut-luminal-transient rather than systemic.
- **Finite mass balance/replenishment/time.** Complement proteins are continuously replenished in serum/tissue. comp-018 does not model complement pool size, local production, clearance, residence time, post-meal exposure, or sustained inhibition. “Dietary-scale viable” is therefore not closed.
- **Localization/transport/access.** The gout CP0 site is MSU crystals in joints and tissue macrophage compartments. Many candidate exposures are gut-luminal or dietary; systemic free plasma levels may be far lower. Houttuynia/Bupleurum polysaccharides are plausibly luminal rather than systemic. DAF/C1-INH engineering threads have separate localization questions.
- **Coproducts/local peaks/redox/off-targets/safety.** The artifact flags some risks—Stachybotrys/K-76 toxicity, retracted sorgoleone paper, Houttuynia pro-inflammatory fraction in later pages, heparin anticoagulation via phase-2/comp-020 context—but no integrated safety model exists. Complement inhibition itself carries infection and immune-handling concerns; this is not quantified.
- **Sensitivity ranges.** No implemented sensitivity analysis in comp-018. Dominant uncertainties are assay-format spread, dietary PK, compartment access, species/serum source in hemolytic assays, polysaccharide structural fraction, and single-lab replication risk. The artifact mostly lists these as caveats rather than exploring them computationally.

## Summary-fidelity audit

**README vs artifact.**

- README is materially stale and over-specific:
  - says Phase 1 done and Phase 2 queued, while Phase 2 files exist and the interpretive wiki says Phase 2 complete;
  - says `outputs/summary.md` exists, but it is absent;
  - says compounds catalogued = 32, while generated summary says 33;
  - keeps rosmarinic acid as singular top-line “TIER 1” despite later comp-020/Phase 2 reframing to a multi-candidate tier.
- README’s command path says:
  - `cd experiments/comp-018-upstream-complement-modulator-sweep`
  - but repository path is `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep`.
  This is a reproducibility-contract mismatch unless run from a different undocumented root.

**`outputs/scope-summary.md` vs code/JSON.**

- `scope-summary.md` is plausibly generated by `scope_validate.py`, but its malformed MSU relevance values show the generator is low-fidelity for human interpretation.
- It correctly reflects the actual compound count as 33, exposing inconsistency with README and `compounds.json.sweep_summary`.

**Interpretive wiki page.**

- `wiki/upstream-complement-modulator-sweep-computational.md` is substantially more reconciled than README:
  - includes the Phase 1 contamination warning;
  - points to comp-020 as canonical for prioritization;
  - adds Phase 2 Houttuynia, Helicteres replication, and C1-INH engineering updates;
  - states Phase 2 complete.
- However, because the page is a compact stub and the archived Phase 1 narrative is still present, the artifact must clearly mark README/Phase 1 ranking as noncanonical for prioritization.

**`wiki/computational-experiments.md`.**

- Mostly reconciled with Phase 2:
  - comp-018 row says Phase 1 + Phase 2 complete;
  - mentions Houttuynia, Helicteres replication inconclusive, C1-INH anchors, and translation cross-check pending.
- Still has an opening verdict sentence emphasizing rosmarinic acid TIER 1 and “5–10 µM” before later caveats. This should be softened or reordered so the row’s first verdict reflects current canonical status: multi-candidate, assay-spread-limited, Phase 1 brief-contaminated.

**Validation and hypothesis surfaces.**

- `validation-experiments.md` includes DAF SCR1-4 §1.25 and broader CP0 follow-up references, but the bundle was truncated before any full Houttuynia §1.30 section. I cannot verify that Houttuynia/Helicteres wet-lab gates are fully reconciled.
- `H05-daf-scr14-cp0-thesis.md` acknowledges comp-018 and C1-INH as a future sister hypothesis if a future comp passes. Since comp-037 now exists with a MODERATE C1-INH verdict, H05’s C1-INH wording is stale.

**Other corpus pages inspected.**

- `complement-c5a-gout.md` is highly reconciled: it includes assay-spread caveats, Phase 2 Houttuynia, comp-029 rosmarinic-acid gut-luminal reframe, and comp-039 CFH classification.
- `modality-chokepoint-matrix.md` is reconciled and includes native-compound dietary complement modulators plus Houttuynia caveats.
- `supplements-stack.md` includes Houttuynia with strong structure-dependent and PK caveats.
- `gout-action-guide.md` includes CFH and upstream CP0 candidates with cautionary language; it does not appear to over-recommend rosmarinic acid as a clinical action.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 16 upstream complement targets defined | `inputs/targets.json`; `scope-summary.md` | Counted and listed by `scope_validate.py` | Internal artifact only; pathway biology cited in prose | Structurally plausible, but validator does not verify UniProt/pathway correctness |
| 32 vs 33 compounds catalogued | README; `compounds.json.sweep_summary`; actual `compounds` array; `scope-summary.md` | Validator counts actual list = 33 | Internal artifact inconsistency | **Action required** — reconcile counts everywhere |
| ChEMBL anticomplement coverage 0% | README; `compounds.json`; `scope-summary.md` | Computed from `chembl_anticomplement_data` strings | ChEMBL checks are documented but not directly verifiable from artifact | Plausible but not independently verified; count denominator inconsistent |
| Rosmarinic acid C3 convertase 5–10 µM | README; `compounds.json`; archived wiki | Stored as IC50 datum; not computationally derived | Explicitly abstract-tier; primary paper paywalled/not PMC; later pages note 20–30×/44× spread | **Do not use as sole load-bearing number**; full-text/matched-assay verification required |
| Rosmarinic acid “dietary-scale viable” | README; `compounds.json.platform_relevance`; archived wiki | Stored conclusion only | Inferred from GRAS sources and dosing plausibility; comp-029 later reframes to gut-luminal transient | Overstated in README; should be caveated as compartment/PK-unresolved |
| Luteolin CH50 190 µM / AP50 170 µM and triple-mechanism | `compounds.json`; README; comp-018 wiki; comp-039 | Stored conclusion only | Abstract/full-text status mixed; XO/URAT1 evidence comes from comp-013, not reproduced here | Plausible corpus connection, but systemic complement relevance unclosed |
| Bupleurum polysaccharides lectin pathway ~1 mg/mL | `compounds.json`; README; Phase 2 files | Stored conclusion only | Claimed Paperclip/PMC anchored for Wu 2015 | Gut-luminal plausible; systemic/joint relevance not established |
| Houttuynia cordata polysaccharide CH50 79–318 µg/mL | Phase 2 markdown; interpretive page; supplements/complement pages | Not present in Phase 1 `compounds.json`; not used by validator | Mix of English abstracts/full text; some source-language single-model flagged | Important Phase 2 addition; machine-readable Phase 1 output not updated to include it |
| Helicteres compound 5 CH50 9 µM | Phase 2 JSON; interpretive page; comp-020 | Not in Phase 1 `compounds.json`; not used by validator | Primary paper PMC full text claimed; no independent replication | Replication-first; should not be used as confirmed winner |
| C1-INH Pichia 30–180 mg/L active production | Phase 2 C1-INH literature markdown; comp index | Not in Phase 1 validator | Abstract-tier Bos 2003; full text not retrieved | Useful engineering lead, but full-text verification required before wet-lab gating |
| N-deglycosylated C1-INH retains protease-inhibitor function | Phase 2 C1-INH markdown; comp-037 row | Not in comp-018 code | Liu 2004 PMC available; artifact says not fully grep-verified in Phase 2 | Likely strong but should be line-verified if load-bearing |
| “Every IC50 / mechanism / dose grep-verified before commit” | README and `query-strategy.json.verification_gate_protocol` | Not implemented | Contradicted by explicit abstract-tier claims | Treat as aspiration/documented protocol, not enforced fact |
| `python3 scripts/scope_validate.py` reproducibility | README; script | Recomputes `scope-summary.md` only | Inspectable deterministic stdlib script | Plausible for summary reproduction; not for literature sweep reproduction |
| Phase 2 translation cross-check | Phase 2 files | Not implemented in script | Several Chinese/Japanese sources flagged single-model; DeepSeek cross-check pending | Required before wet-lab gates depend on flagged source-language details |

## Affected wiki pages

- `wiki/upstream-complement-modulator-sweep-computational.md` — already mostly consistent — contains contamination warning, Phase 2 update, Houttuynia, Helicteres replication status, and C1-INH anchors. Keep as canonical over README.
- `wiki/computational-experiments.md` — change required — comp-018 row is Phase 2-aware but still opens with a rosmarinic-acid-forward 5–10 µM verdict; reorder/soften to reflect current canonical multi-candidate, assay-spread-limited status.
- `wiki/complement-c5a-gout.md` — already consistent — includes comp-018, comp-020, comp-029, Houttuynia, and comp-039 caveats; no immediate correction found.
- `wiki/modality-chokepoint-matrix.md` — already consistent — includes native-compound dietary complement modulators and Houttuynia structure-dependent caveat.
- `wiki/supplements-stack.md` — already consistent — includes Houttuynia with explicit “research-stage,” structure-dependent activity, consumer-product caveat, and dietary-PK caveat.
- `wiki/gout-action-guide.md` — already mostly consistent — mentions upstream-CP0 candidates as mechanistic predictions, not clinical proof. Avoid adding stronger dietary recommendations until PK and wet-lab gates close.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` — change required — C1-INH sister-thread wording says “future comp-NNN” even though comp-037 has landed; update to reference comp-037 and preserve its MODERATE/kinetic-competition limitations.
- `wiki/upstream-complement-verification-rerun-computational.md` — already consistent — includes Helicteres replication pointer and comp-018 Phase 2 context.
- `wiki/validation-experiments.md` — unresolved — bundle truncation prevented full inspection of Houttuynia/Helicteres/CP0 validation sections. If §1.30 or comp-040 references depend on comp-018 Phase 2 source-language numbers, they must include the translation/replication caveats.
- `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/README.md` — change required — stale Phase 1 status, wrong/missing output file, wrong path, inconsistent counts, over-promoted rosmarinic acid.
- `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/outputs/compounds.json` — change required — stale Phase 1 canonical machine-readable output inconsistent with Phase 2 and with its own counts.
- `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/outputs/scope-summary.md` — change required — malformed target relevance strings; count/tier output exposes inconsistencies but does not flag them.

## New connections or implications

- The strongest cross-corpus connection is not “rosemary wins”; it is that **upstream complement natural-product literature is a citation-network/query-framing problem**, not simply a language-translation problem. Phase 2’s Houttuynia finding shows species/traditional-name queries are load-bearing.
- comp-018 Phase 2 plus comp-039 creates a coherent **CFH-independent dietary-CP0 hypothesis**: rosmarinic acid, luteolin, Houttuynia, and Helicteres act upstream of Factor H, so CFH Y402H stratification becomes testable rather than just speculative. This is still a biobank/wet-lab hypothesis, not clinical evidence.
- The C1-INH thread has matured from a comp-018 “parallel engineering idea” to comp-037’s EcN/LBP protease-stability question. H05 and CP0 architecture pages should treat DAF and C1-INH as sibling but not interchangeable regulators: DAF is surface convertase decay; C1-INH is classical/lectin protease inhibition.
- Houttuynia adds a mechanistically distinct polysaccharide/mass-action CP0+CP1 candidate, but its structure-dependent pro-/anti-inflammatory polarity makes consumer-product substitution particularly risky.
- The artifact’s own failures—brief contamination, missing `summary.md`, abstract-tier anchors, and count inconsistencies—are a good example of why the comp-NNN verification-agent proposal in `computational-experiments.md` is needed.

## Required actions

1. **Fix comp-018 README.** Owner surface: `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/README.md`. Verification criterion: status says Phase 1 + Phase 2 complete; command path uses `wiki/etc/experiments/...`; `outputs/summary.md` reference is removed or the file is added; counts match generated outputs; rosmarinic-acid headline is caveated and defers prioritization to comp-020/Phase 2.
2. **Reconcile machine-readable counts and tiers.** Owner surface: `outputs/compounds.json` and `outputs/scope-summary.md`. Verification criterion: actual compound count, `sweep_summary.total_compounds_with_documented_activity`, ChEMBL denominators, tier summary, README, and computational index all agree or explicitly distinguish Phase 1 vs Phase 2 datasets.
3. **Decide Phase 2 machine-readable integration.** Owner surface: comp-018 `outputs/` and `phase-2/`. Verification criterion: either (a) create a Phase 2 `compounds-phase-2.json` / combined canonical JSON including Houttuynia and Helicteres with replication/translation flags, or (b) explicitly label `outputs/compounds.json` as Phase 1-only and noncanonical for Phase 2 prioritization.
4. **Strengthen validator or rename its promise.** Owner surface: `scripts/scope_validate.py`. Verification criterion: either add checks for internal count/tier/ChEMBL consistency and required `verification_status`, or rename the script/README language so it does not imply provenance or IC50 validation.
5. **Fix `scope-summary.md` target rendering.** Owner surface: `scope_validate.py`. Verification criterion: generated target rows do not produce nonsensical MSU relevance values such as `the` or `narsoplimab-target;`; if truncation is desired, use explicit controlled tags.
6. **Update `wiki/computational-experiments.md` comp-018 row.** Verification criterion: first verdict line reflects current canonical status: Phase 1 brief-contaminated, comp-020/Phase 2 multi-candidate ranking, rosmarinic-acid assay spread, Houttuynia addition, Helicteres replication-first.
7. **Update H05 C1-INH wording.** Owner surface: `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md`. Verification criterion: replace “future comp-NNN” phrasing with comp-037’s actual MODERATE/kinetic-competition-gated result and preserve route/glycosylation caveats.
8. **Full-text / primary-source verification before wet-lab gating.** Owner surfaces: comp-018 Phase 2, validation experiment designs, comp-037 inputs. Verification criterion: Englberger 1988 RA, Bos 2003 C1-INH, and flagged Chinese/Japanese Phase 2 sources have direct full-text or two-model source-language verification before their numbers are used as wet-lab thresholds.
9. **Replicate before prioritizing Helicteres.** Owner surface: validation/wet-lab queue. Verification criterion: independent CH50/AP50 assay with rosmarinic acid, luteolin, and Styrax egonol controls confirms or refutes Yin 2016’s 9 µM claim.
10. **Keep application surfaces conservative.** Owner surface: `gout-action-guide.md` / `supplements-stack.md`. Verification criterion: no clinical or consumer recommendation is strengthened from comp-018 alone; dietary CP0 candidates remain Phase 0, mechanism-grounded, PK-unresolved.

## Review limits

- I did not execute `scope_validate.py`; assessment is by source inspection only.
- I did not retrieve PubMed, ChEMBL, PMC, FDA labels, or paywalled primary sources directly. Provenance assessments are based on artifact text and available wiki surfaces, not independent primary-source verification.
- Repository search tool `grep_repo` failed because `rg` was unavailable; affected-page discovery was done by reading high-priority pages supplied in the bundle and several omitted pages via `read_file`.
- Tool-result budget was exhausted before inspecting every omitted page in full, including complete `validation-experiments.md`, `open-questions.md`, and the full `combined-cp0-systems-model-computational.md`.
- The bundle’s `validation-experiments.md` was truncated, so I could not verify all downstream wet-lab protocol propagation, especially Houttuynia/Helicteres sections.
- I did not compare `outputs/scope-summary.md` byte-for-byte against a fresh generated output.
- This review treats all clinical/dietary implications as Phase 0 research hypotheses only, not medical advice or clinical evidence.
