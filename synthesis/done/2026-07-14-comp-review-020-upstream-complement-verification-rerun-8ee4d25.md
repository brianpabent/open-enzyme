---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-020
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-020

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-020-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-020-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-020

## Bottom-line verdict

Action required. The experiment is a useful Phase 0 literature-mining artifact, but the artifact-summary contract is not clean: several load-bearing quantitative claims are not primary-source verified in the committed artifact, one heparin molar conversion is wrong by 1000× in `outputs/per-node-findings.md`, “within ~20%” tier wording is repeatedly mathematically inconsistent, and the reproducibility path is an audit trail of external searches rather than a deterministic rerun.

The biological conclusion should be softened to: **comp-020 surfaces candidate upstream-complement modulators and assay-format caveats; it does not exhaustively resolve “all known upstream complement compounds,” does not establish physiological/dietary achievability, and does not independently verify the rosmarinic-acid primary-paper numbers.**

## Implementation and constraint closure

This is not executable computation; it is a manual / agentic literature-mining sweep. There are no scripts. Inputs are target-node/query-scope documents, and outputs are markdown tables plus a search log. Implementation closure therefore means tracing whether the stated query scope, search log, provenance table, per-node tables, README, and wiki summary are mutually consistent.

Key findings:

- **No deterministic implementation.** The README says there are “no scripts to run”; reproduction means re-querying Paperclip MCP and WebSearch. That is plausible as a literature-audit trail but not a deterministic computational experiment.
- **Stored inputs are documentation-only.** `target-nodes.json` and `query-strategy.md` define scope, but nothing enforces use. This is acceptable for a literature-mining experiment, but the “all known upstream complement nodes / all compound classes” framing is stronger than what 28 Paperclip queries + 2 WebSearch queries can close.
- **Primary-source closure is incomplete.** `inputs/provenance.md` explicitly says rosmarinic-acid values were obtained from WebSearch snippets and are `[PRIMARY-PAPER-CONFIRMATION-PENDING]`. But the README and wiki archive also say every load-bearing IC50/CH50/AP50/Ki value was grep-verified against primary full text. That is false for the rosmarinic-acid values, which are central to the narrative.
- **Internal quantitative error.** `outputs/per-node-findings.md` section I says heparin reference is “~2600 μM (38.5 μg/mL ÷ ~15 kDa MW).” Correct arithmetic is ~2.6 μM:
  - 38.5 μg/mL = 38.5 mg/L = 0.0385 g/L
  - 0.0385 g/L ÷ 15,000 g/mol = 2.57e-6 M = 2.6 μM  
  Earlier artifact text gives the correct 2.6 μM, so this is an internal contradiction.
- **Tiering math is inconsistent.**
  - C1q section calls Helicteres compounds 5 and 4 “top-tier within ~20%” in places, but 9 μM vs 40 μM is ~4.4× apart, not within 20%.
  - Marine sulfated polysaccharide tiering sometimes groups ANW/SC (~1 μg/mL) with SJW-3 (3.11 μg/mL) under “within ~20%” / no-headline language, but that is ~3× weaker.
  - Cross-class wording says rosmarinic acid, luteolin, and Helicteres “rank within ~20% of each other on no single common metric,” which is not a meaningful quantitative statement.
- **Question/model fit is partial.** The stated question asks for compounds with documented direct modulator activity at IC50/EC50 ≤100 μM-equivalent in matched-format assays. The artifact also includes:
  - compounds >100 μM, e.g. luteolin CH50 190 μM, quercetin/rutin/hyperoside/apigenin in the hundreds of μM to mM range;
  - polysaccharides reported in μg/mL or mg/mL without molar equivalence because MW/heterogeneity is unresolved;
  - broad hemolytic pathway assays that do not necessarily establish direct node binding;
  - animal-expression effects such as ginsenoside C1q reduction, not matched direct complement-modulator IC50 evidence.
- **Physiological constraint closure is limited.** The artifact does a good job naming assay-format heterogeneity but does not close:
  - achievable free concentration at the relevant compartment;
  - systemic vs gut-luminal vs synovial exposure;
  - serum protein binding and local residence time;
  - MSU-crystal-surface access;
  - finite complement-protein substrate pool and replenishment;
  - anticoagulation / coagulation risk for heparin/fucoidan-like sulfated polysaccharides;
  - off-target immune activation by complement-fixating polysaccharides.
- **Sensitivity coverage is mostly “convenient literature spread,” not formal sensitivity analysis.** Dominant uncertainties are assay format, compound purity/standardization, source-language coverage, and physiological concentration; these are flagged but not quantified in comp-020.

## Summary-fidelity audit

- **README vs provenance mismatch:** README says primary-paper text grep-verified for load-bearing numbers; provenance says rosmarinic-acid numbers were not full-text grep-verified and are pending. This needs correction in README and wiki summary.
- **Wiki archive vs provenance mismatch:** The wiki archive’s methodology section states every load-bearing IC50/CH50/AP50/Ki was grep-verified before being written. That is not true for rosmarinic acid.
- **`outputs/per-node-findings.md` mismatch:** The rosmarinic-acid table gives the 34 / 160 / 180 / 1500 μM values without an inline “primary full text pending” flag. The caveat exists in provenance but not where the values are used.
- **`computational-experiments.md` mostly captures the intended softened verdict**, but the phrase “Three independent scans now agree” on ChEMBL structural bias should be softened because comp-013/014/020 use overlapping ChEMBL-gap methodology; repetition is not independent evidence.
- **`upstream-complement-assay-format-mapping-computational.md` is already a reconciliation surface** for the RA assay-format spread and correctly labels Sahu/RA as “WebSearch-snippet-tier.” This page is more faithful than comp-020 itself.
- **`upstream-complement-modulator-sweep-computational.md` is already partially reconciled**: it warns comp-018 was framing-contaminated and points to comp-020. However, its comp-018 entry still contains older RA 5–10 μM language that should remain explicitly assay-format bounded.
- **H05 hypothesis card has stale RA wording.** It says dietary rosmarinic acid is “TIER-1 C3 convertase inhibitor, IC50 5–10 μM” in a coordination note. That should be updated to comp-021/comp-020’s assay-format-bounded 34–180 μM gut-relevant range, with the 5–10 μM number labeled lower-bound/purified-assay/non-load-bearing.
- **Validation surfaces are not fully propagated.** comp-020 proposes RA + MSU surface assay, Helicteres replication, multilingual follow-up, and assay-format mapping. Some later pages handle these, but comp-020 itself should make clear which are already done by comp-021/comp-039 and which remain open.
- **Application surface caution:** `gout-action-guide.md` references upstream-CP0 candidates in genotype/prevention contexts. It should continue to label these as mechanistic predictions, not supplement recommendations; no immediate correction found beyond ensuring comp-020’s caveats are not lost if summarized there.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| comp-020 was independent of comp-018/019 and brief-scrubbed | README; `inputs/provenance.md`; `outputs/per-node-findings.md` | Supports verification-rerun framing | Self-attested only; no independent audit trail proving non-consultation | Accept as author statement, not independently verifiable |
| Target scope includes upstream complement nodes C1q/MBL-MASP/C3 tickover/convertases/factors/regulators/residual C5 axis | `inputs/target-nodes.json` | Defines query universe | Directly available in artifact | Accept as scope definition |
| “Across all known nodes/classes” was swept | README question; wiki archive | Supports breadth-scan conclusion | Search log has 28 Paperclip + 2 WebSearch queries; partial multilingual; no exhaustive database enumeration | Overstated; should be “targeted breadth scan” |
| Helicteres compound 5 CH50 0.009 mM / AP50 0.021 mM | `outputs/per-node-findings.md`; `inputs/provenance.md` | Top C1q/CP candidate | Claimed Paperclip grep-verified to PMC6273495; primary text not included in artifact | Plausible but externally unverified by this review |
| Helicteres compound 4 CH50 0.040 mM / AP50 0.105 mM | Same | Top C1q/CP candidate | Claimed Paperclip grep-verified to PMC6273495 | Plausible but externally unverified |
| Luteolin CH50 0.19 mM / AP50 0.17 mM | Same | Multi-mechanism candidate and tier comparison | Claimed Paperclip grep-verified to PMC7126446 | Plausible but >100 μM; should not be described as ≤100 μM-equivalent hit |
| Heparin CH50 38.5 μg/mL ≈ 2.6 μM assuming 15 kDa | README/wiki archive; `outputs/per-node-findings.md` | Reference potency comparison | Calculation directly checkable | Correct in some locations; contradicted by erroneous 2600 μM in section I |
| Heparin reference ~2600 μM | `outputs/per-node-findings.md` section I | Ranking table | Direct arithmetic error | Incorrect; must be corrected to ~2.6 μM |
| Heparin LP/CP/AP 2/39/76 μg/mL; hexasaccharide 4; octasaccharide 3 | `outputs/per-node-findings.md`; `inputs/provenance.md` | MASP-2 / LP tier | Claimed Paperclip grep-verified to PMC7212410 | Plausible but primary source not in artifact |
| Bupleurum BCPs LP 0.098 mg/mL, CH50 0.35 mg/mL, AP50 0.337 mg/mL | `outputs/per-node-findings.md`; provenance | Plant polysaccharide LP candidate | Claimed Paperclip grep-verified to PMC4629277 | Plausible; not μM-equivalent because polysaccharide MW heterogeneity |
| Marine ANW 0.98 μg/mL, SJW-3 3.11 μg/mL | `outputs/per-node-findings.md`; provenance | Marine sulfated-polysaccharide tier | Claimed Paperclip grep-verified to PMC4728500 | Plausible; tier grouping language inconsistent |
| Rosmarinic acid C3b covalent IC50 34 μM; CP 180 μM; AP 160 μM; direct C5 convertase 1500 μM | `outputs/per-node-findings.md`; README/wiki archive; provenance | Central RA mechanism and assay-format-spread claim | Provenance admits WebSearch-snippet only; primary full text not in Paperclip; confirmation pending | Load-bearing unresolved; must be primary-source verified or explicitly caveated inline |
| RA 44× assay-format spread | `outputs/per-node-findings.md`; wiki archive; computational index | Canonical assay-format warning | Depends on unverified RA primary-paper values | Plausible, later comp-021 reconciles, but comp-020 should mark source tier |
| “Top-tier within ~20%” for Helicteres 9/40 μM | README/wiki archive/per-node | No-headline tiering | Direct arithmetic check | Incorrect wording; use threshold/tier language, not within-20% |
| “Top-tier within ~20%” for marine ANW/SC/SJW-3 | Wiki/per-node | No-headline tiering | Direct arithmetic check | Inconsistent; ANW/SC tied, SJW-3 next tier |
| Natural-product Factor H upregulators empty | `outputs/per-node-findings.md`; wiki archive | Coverage-gap claim | Based on limited search log; no exhaustive direct database search | Reasonable negative finding only within surveyed corpus |
| CD55/CD59/CR1 natural-product upregulators empty | Same | Supports engineering-thread territory | Based on limited search log | Reasonable within surveyed corpus; not globally closed |
| Fungal upstream complement modulators empty | `outputs/per-node-findings.md`; wiki archive | Extends comp-014 | Search log shallow; K76 did not surface; comp-014 separate | Should be “no novel hit surfaced in this scan,” not definitive global zero |
| ChEMBL anti-complement coverage ~20% and “three independent scans agree” | `outputs/per-node-findings.md`; wiki archive; computational index | Methodological conclusion | PubChem/ChEMBL spot-check not directly committed as query outputs; “typical >70% kinase/GPCR” uncited | Needs source/output support and softer independence wording |
| Multilingual coverage partial | provenance; search log; wiki archive | Limits coverage | Directly stated | Clean and appropriately caveated |
| Reproducibility via `cd experiments/...` | README; wiki archive | Reproduction contract | Path differs from tracked `wiki/etc/experiments/...`; no scripts; external tools required | Plausible audit trail but command/path should be corrected |

## Affected wiki pages

- `wiki/upstream-complement-verification-rerun-computational.md` — change required — archived comp-020 page inherits the unflagged RA-primary-source issue, the “every load-bearing value grep-verified” overclaim, and inconsistent tier wording.
- `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/outputs/per-node-findings.md` — change required — fix heparin 2600 μM → 2.6 μM; add inline RA primary-full-text-pending flag; correct within-20% tiering language.
- `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/README.md` — change required — reproducibility path and “primary-paper grep-verified” wording need correction.
- `wiki/computational-experiments.md` — change required — comp-020 entry should soften “three independent scans now agree” and avoid implying the ChEMBL gap estimate is independently quantified primary evidence.
- `wiki/upstream-complement-assay-format-mapping-computational.md` — already consistent — it explicitly treats RA as WebSearch-snippet-tier and reconciles RA assay-format spread; no action except ensuring comp-020 points to it as reconciliation.
- `wiki/upstream-complement-modulator-sweep-computational.md` — mostly already consistent / minor change required — contamination warning and comp-020 comparison are present, but older RA 5–10 μM language should remain explicitly non-load-bearing and assay-format bounded.
- `wiki/complement-c5a-gout.md` — mostly already consistent — it incorporates comp-020/021/029/039 caveats and frames dietary CP0 as mechanistic prediction; check any remaining RA 5–10 μM language for source-tier caveat.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` — change required — coordination note uses stale “rosmarinic acid IC50 5–10 μM” language; update to assay-format-bounded comp-021 framing.
- `wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md` — already mostly consistent — it treats RA mechanism as CFH-independent and labels prediction uncertainty; however, its “Sahu 1999 IC50 = 34 μM verified against PubMed-hosted abstract” is not full-text verification and should not be conflated with primary full-text verification.
- `wiki/gout-genetic-variants.md` — already mostly consistent — CFH row cites comp-039 and labels gout link speculative; no direct comp-020 correction needed beyond source-tier discipline.
- `wiki/gout-action-guide.md` — already mostly consistent with Phase 0 caveats — ensure upstream-CP0 candidates remain mechanistic prediction / research-stage, not dietary advice.
- `wiki/tcm-modern-rigor-intersection.md` — already consistent in broad query-framing discipline — no comp-020-specific correction required.

## New connections or implications

- **comp-021 partially repairs comp-020.** The later assay-format mapping page is a better canonical source for RA quantitative use than comp-020 itself because it explicitly collapses the gut-relevant RA range to 34–180 μM and labels Sahu as WebSearch-snippet-tier.
- **The most important comp-020 contribution is not a winner list; it is assay-format discipline.** The RA and heparin spreads show that “anti-complement IC50” is not portable without pathway, serum dilution, surface, and readout.
- **Helicteres needs two independent closures before promotion:** (1) independent assay replication, and (2) cross-format testing. Its potency is striking but single-anchor and not within-20%-tied with RA/luteolin on any common metric.
- **Sulfated-polysaccharide hits are mechanistically plausible but safety-dominated.** Heparin/fucoidan-like activity brings anticoagulation/coagulation/fibrosis handling into the decision tree; potency alone is insufficient.
- **ChEMBL undercoverage is real enough to justify primary-literature mining, but not independently quantified by comp-020.** Treat it as a repeated methodological warning, not as three independent measurements of the same bias.
- **CFH stratification work depends on comp-020’s source-tier cleanup.** comp-039 uses comp-020 candidates; if RA/Helicteres quantitative values are cited in genotype-stratified predictions, the provenance caveats must travel with them.

## Required actions

1. Correct `outputs/per-node-findings.md`: change heparin reference from ~2600 μM to ~2.6 μM and audit all μg/mL→μM conversions.
2. Add inline source-tier flags to every rosmarinic-acid value in README/wiki archive/per-node table: “PMID citation confirmed; primary full-text verification pending” unless/until primary full text is inspected.
3. Replace “every load-bearing value grep-verified” with accurate wording: “all PMC-accessible load-bearing values grep-verified; RA values pending primary full-text confirmation.”
4. Replace “within ~20%” language where arithmetic does not support it. Use “same qualitative tier,” “sub-50 μM,” “within ~3×,” or “distinct mechanistic classes not directly rankable,” as appropriate.
5. Soften scope from “all known upstream complement compounds/classes” to “targeted breadth scan across named upstream nodes and compound classes, with partial multilingual coverage.”
6. Verify the 1988/1991/1999 rosmarinic-acid primary papers directly, or mark all derived RA quantitative downstream uses as unresolved.
7. Commit or cite reproducible ChEMBL query outputs if retaining the ~20% coverage number; otherwise state it as a spot-check estimate.
8. Update `computational-experiments.md` and H05 to use comp-021’s assay-format-bounded RA framing instead of stale 5–10 μM headline language.
9. Preserve Phase 2 open gates as required, not optional polish: CNKI/WanFang/J-STAGE deep dive, Helicteres replication, RA + MSU-crystal C3b/C5a assay.
10. Fix the README reproduction path to the actual repo-relative folder under `wiki/etc/experiments/...`, and explicitly state that no deterministic script reproduction exists.

## Review limits

I did not execute code; there is no code to execute. I could not independently inspect Paperclip MCP line outputs or external primary papers from within the repository. Repository search tooling failed because `rg` was unavailable, so affected-page discovery relied on the provided bundle plus direct reads of key listed wiki pages before tool-result budget was exhausted. Primary-source verification for PMC/PubMed claims remains unresolved unless the source text is committed or re-read externally.

---
## ✓ Actioned 2026-07-14
**Disposition: caveat/downgrade** (relabel/hygiene tier). Added a ⚠️ caveat banner to the interpretive page (or artifact README for comp-015) capturing the audit's headline finding — the qualitative direction holds, but the quantitative/verdict framing overstated what the model resolves. Deeper artifact fixes (reproducibility defects, provenance-tier labeling, code/summary mismatches, any recompute) remain in the Required-actions above as residuals for a focused follow-up.
