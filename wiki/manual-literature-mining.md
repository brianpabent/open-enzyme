---
title: "Manual Literature Mining Protocol — Paperclip MCP Discipline"
date: 2026-05-05
tags:
  - methodology
  - literature-mining
  - paperclip
  - verification-discipline
  - epistemic-rigor
  - global-multilingual
related:
  - paperclip-deep-dive.md
  - bio-ai-tools.md
  - open-source-platform.md
  - chembl-cross-check.md
  - CLAUDE.md
sources:
  - "feedback memory `feedback_paperclip_map_unreliable.md` — documented hallucination of organisms and fabricated kinetic numbers by the `map` operator (2026-05-05)"
  - "paperclip-deep-dive.md — full Paperclip MCP capability + limitation audit"
status: published
---

# Manual Literature Mining Protocol — Paperclip MCP Discipline

A small but load-bearing methodology page. Codifies the verification discipline for using Paperclip MCP (the full-text PubMed / bioRxiv / medRxiv / arXiv corpus) safely in this project — surfaced 2026-05-05 by the wiki sweep daemon (Pass 2 Connection #3 + Priority Action #1). The motivation: Paperclip's index of ~11M full-text papers is genuinely valuable for deep-dive questions, but the `map` operator (the convenience-aggregation primitive) hallucinates — wrong organisms, fabricated kinetic numbers, made-up author affiliations — making automated unverified use unsafe. This page defines the safe-use workflow.

## Why this protocol exists

Specific failure mode documented 2026-05-05: a Paperclip `map` query against a multi-paper question returned organism names not present in the source papers AND specific kinetic numbers (Km, IC50) that did not appear in any of the cited sources when grep-verified. The `map` primitive appears to do model-side aggregation of partial extracts, which the underlying model fills in plausibly but not faithfully. (Memory record: `feedback_paperclip_map_unreliable.md`, decided 2026-05-05.)

`search`, `cat`, `head`, `grep`, `scan` primitives DON'T exhibit this failure mode — they return raw paper content, line-anchored, verifiable. The protocol below confines automated use to those safe primitives and requires explicit verification before any quantitative claim derived from Paperclip enters the wiki.

## The five-rule discipline

### 1. Use safe primitives only

**Allowed:** `search`, `cat`, `head`, `grep`, `scan`.
**Forbidden in any automated workflow:** `map`, `reduce`, or any aggregation primitive that produces synthesized output rather than raw paper content.

If a finding requires aggregation across multiple papers (e.g., "summarize the IC50 range for compound X across all NLRP3-relevant studies"), do the aggregation in two stages: (1) `search` + `grep` to surface the specific lines containing IC50 values; (2) human-verify each value against `cat` of the source paper; (3) the synthesis happens in the wiki page, not in Paperclip's primitive call.

### 2. Anchor identity to `meta.json`

Every paper Paperclip returns has a `/papers/<id>/meta.json` file with: title, authors, journal, year, PMID, doi. **Cite from `meta.json`, not from inferred metadata in the paper body.** A common failure mode is misattributing a paper based on a title-like string in the body that turns out to be a citation TO another paper, not the paper's own title.

Workflow: `cat /papers/<id>/meta.json | jq .title` (or read directly) before quoting a paper.

### 3. Grep-verify all numbers before they enter the wiki

For any quantitative claim sourced from Paperclip — IC50, Km, dose, sample size, percent change, p-value, cohort n — `grep` for the specific number in the source paper's `content.lines` file BEFORE writing the number into the wiki. The verification step takes ~30 seconds and catches the `map`-class hallucination directly.

```bash
# Example: verify a claimed IC50
grep -i "IC50" /papers/<id>/content.lines
grep "5\.18\|5.18 μM" /papers/<id>/content.lines
```

If the number doesn't appear in the source, it didn't come from the source. Do not propagate.

### 4. Never propagate `map`/`reduce` summaries

If you find yourself looking at output from Paperclip's `map` or `reduce` primitives (e.g., from a prior session, from a logged subagent task, from the daemon's intermediate state) — **treat that output as un-validated and re-derive from the safe primitives.** A `map` summary that LOOKS reasonable cannot be assumed reasonable.

This applies even when the `map` output is convenient. Convenience is the failure-mode signal — `map` is fast precisely because it skips verification.

### 5. Cite line-anchored, with the project's citation format

Paperclip provides line-anchored URLs of the form `https://citations.gxl.ai/papers/<doc_id>#L<n>`. **Always cite at the line-anchor level**, never just at the paper level. This makes verification trivial for a future reader (or for the sweep daemon's Pass 3 reviewer) and forces the citation to point at a specific claim, not a generalized invocation of "the paper."

Citation discipline (from existing wiki convention):
- Inline: `[1]`, `[2]`
- References block at end of page:
  ```
  --------
  REFERENCES
  [1] Authors. "Title." *Journal* vol, pages (year). doi:XX
      https://citations.gxl.ai/papers/<doc_id>#L<n>
  ```
- Never expose Paperclip's internal `doc_id` in prose (only in the URL).

## Pre-commit verification gate (the rule that catches errors BEFORE the sweep, not after)

Rule 3 above ("grep-verify all numbers before they enter the wiki") covers Paperclip-sourced numbers specifically. This section generalizes the same discipline to **every load-bearing quantitative claim** in newly-authored wiki content — disulfide counts, residue counts, sequence lengths, IC50s, Kms, dose-response numbers, cohort sizes, percent changes, kinetic constants, evidence-tier counts. Whether the source is Paperclip, UniProt, ChEMBL, ClinicalTrials.gov, a PMC paper, or a database API response, the verification gate is the same.

**The rule:**

> Before any commit lands a wiki page (especially `wiki/<comp-NNN>-*.md` interpretive pages and `wiki/hypotheses/H<NN>-*.md` cards) that introduces a load-bearing quantitative claim, **the author must grep-verify the claim against its primary source and add a line-anchored citation inline.** A claim that cannot be grep-verified is not committed; it is either re-derived, replaced with a bounded "TBD pending source verification" marker, or dropped.

**Why this gate exists:**

The wiki sweep daemon (Pass 1 propagate → Pass 2 synthesize → Pass 3 review → Pass 4 DeepSeek peer-review) is *good* at catching cross-page inconsistencies — exactly the failure mode that surfaced the DAF SCR1-4 disulfide-count error on 2026-05-06 (Sweep A Connection 2). But that means the discipline currently catches errors ~12–24 hours *after* they ship into the corpus, by which time:

- The wrong number has propagated to multiple pages (DAF SCR1-4: comp-012 → H05 stub).
- The wrong number has been ingested into the synthesizer's context for downstream reasoning (the chaperone-orthogonal triple-cassette synergy panic — predicting 17+12=29 disulfides, 1.8× Huynh — was based on a fabricated coefficient).
- A peer-review pass and a hand-walkthrough are required to find and fix the propagation, instead of catching it at the source.

The sweep is a backstop, not a substitute. The pre-commit verification gate is the right moment to catch hallucinated numbers — at the moment they would enter the corpus, not after they've been laundered through the substrate.

**Operational pattern:**

When authoring new wiki content (especially comp-NNN interpretive pages, H-card stubs, scope pages, or any page making mechanistic / kinetic / structural claims), follow this micro-protocol per quantitative claim:

1. **Identify the load-bearing numbers in the draft.** Anything that downstream reasoning will depend on (cassette counts, disulfide counts, kinetic constants, evidence-tier verdicts, cohort sizes, percent-change magnitudes). Numbers used for color or rough order-of-magnitude framing are lower-stakes; load-bearing numbers feed into matrices, decision criteria, threshold gates, or other pages' calculations.

2. **For each load-bearing number, name the primary source.** UniProt accession + feature line, PMID + page/section, ChEMBL ID, NCT trial ID, etc. If you cannot name the primary source, the number is suspect — either find it or drop it.

3. **Grep-verify the number against the primary source.** For UniProt: `curl -s "https://rest.uniprot.org/uniprotkb/<ACC>.txt" | grep "<feature>"`. For PMC: `grep -i "<number>" /papers/<id>/content.lines`. For ChEMBL: pull the bioactivity record and check the value field. The verification should produce the number directly from the source, not be inferred from a summary.

4. **Cite line-anchored inline.** Per Rule 5 above for Paperclip; for UniProt: `(per UniProt P08174 DISULFID feature: Cys36-Cys81)` is line-anchored enough. For PMC: `(PMID 12345678 Table 2)` or `(PMID 12345678 §Results para 3)`. The citation must let a future reader (or the sweep's Pass 3 reviewer) re-verify in <30 seconds.

5. **If the number cannot be verified, do not ship it.** Options: re-derive from a different source, drop the claim and note the gap, or write a placeholder like `[TBD: pending UniProt verification]` and keep it out of the load-bearing path until verified.

**What counts as load-bearing — heuristics:**

- Any number that appears in a downstream comparison, table, matrix, decision criterion, or quantitative threshold ("if synergy <0.7, then..." / "29 vs. 25 total disulfides").
- Any number that, if wrong, would change the evidence-tier verdict, the experimental design, or the platform decision.
- Any number that other wiki pages will cite or reuse.
- Any number that the sweep daemon's Pass 2 synthesizer might pull into a cross-doc connection (which, in practice, is *almost any quantitative claim* — the synthesizer reads everything).

**What counts as low-stakes — exempt from the gate:**

- Order-of-magnitude framing where precision doesn't matter ("on the order of millions of dollars," "weeks not months").
- Numbers used purely for color in narrative prose, where the surrounding text would still be correct if the number were ±20% off.
- Numbers explicitly tagged as estimates or projections (with the tag making the uncertainty visible).

**The DAF SCR1-4 incident (2026-05-06) — provenance for this rule:**

The 2026-05-05 Sonnet subagent that authored `wiki/daf-cd55-scr14-truncated-computational.md` (comp-012) asserted "3 conserved disulfide bonds per SCR domain → 12 total" in 4 places of prose narrative. The comp-012 pipeline (AlphaFold pLDDT-based protease stability) does not actually count disulfides; comp-012's own Limitations section explicitly says "Disulfide bonds not modelled." The "12" was hallucinated at write-time. The error then propagated into `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` (the CP0-closure thesis stub) without independent verification.

The 2026-05-05 sweep daemon caught the inconsistency the next day (Sweep A Connection 2: chaperone framework had "8 (4 SCRs × 2 disulfides each)," comp-012 + H05 had "12") and surfaced it as a Priority Action. Verification against UniProt P08174 during the 2026-05-06 walkthrough confirmed 8 DISULFID feature annotations across SCR1-4 (the canonical sushi/CCP fold: Cys1-Cys3 + Cys2-Cys4 motif, 2 per domain).

If the pre-commit verification gate had been in place when comp-012 was authored, the number would have been grep-verified against UniProt at write-time and the wrong claim would never have shipped. The sweep would still have run, but it wouldn't have needed to find this class of error — only genuine cross-doc synthesis findings.

This rule generalizes: **the sweep daemon should be catching novel cross-doc connections, not catching fabricated coefficients.** Numerical hygiene is upstream of synthesis.

---

## Killshot tiering — pick the lowest-cost experiment that resolves the question

Sister discipline to the pre-commit verification gate: **before declaring an experiment as the "killshot" for an open hypothesis, walk a cost ladder and pick the lowest-tier option that resolves the question above noise floor for the platform's purposes.** The default "killshot" definition in institutional research is grant-tier ($50K–$500K mouse / cell-line / cohort study). For an open-source citizen-science project run by a CTO not a pharma lab, that default is wrong — both literally too expensive AND epistemically over-specified relative to the decision the experiment is supposed to inform.

**The OE killshot tier menu:**

| Tier | Cost | Time | Source / route | Examples |
|---|---|---|---|---|
| **Tier 0** | $0 | hours-days | Public dataset mining; full-text re-read of papers comp-NNN got at abstract-level; published-data synthesis | GTEx + Human Protein Atlas sex-stratified expression mining; GWAS catalog lookup; UniProt feature-annotation queries; full-text retrieval via Sci-Hub / Anna's Archive of papers cited only at abstract-tier; Mendelian randomization via published MR-Base summary statistics |
| **Tier 1** | $200–500 | days-weeks | Leverages existing self-experiment infrastructure | n=1 LabCorp / Quest panels (FEUA, hs-CRP, hormone panels); 16S microbiome OTU mining if the panel is already running; spot urinary biomarker measurements; serum-panel snapshots with pre-committed protocol |
| **Tier 2** | $0–500 | weeks | Crowdsourced / community-leveraged | Recruiting men's-health forum cohorts to share LabCorp panels; Twitter/Reddit-based n>>1 cohort assembly; community-sourced patient-reported outcomes; OSF-style collaborative protocols on existing self-experimenter populations |
| **Tier 3** | $2–5K | 4–12 weeks | Friendly bench (community college, undergrad thesis, sympathetic small lab) | Caco-2 / HEK293 / HepG2 cell-culture work with consumables-only budget; small-scale Western blot / qPCR / ELISA assay; tissue-culture collaboration where the academic partner has the equipment and the OE side funds reagents |
| **Tier 4** | $5–15K (academic collaborator) / $30–60K (institutional) | 8 weeks–3 months | Academic-collaboration animal study / formal cell-line work / contracted assay | Mouse castration + replacement studies via academic IACUC-protocol-leveraged route; published-with co-authorship arrangement; CRO-tier work (the institutional baseline) is the last resort |

**The discipline:** before promoting an experiment to "killshot" status, walk the ladder Tier 0 → Tier 4 and ask at each tier *"could I resolve this question above noise floor without spending more?"* Default to the lowest tier that answers yes. The mouse experiment is rarely the right first move for an OE-tier question; it is sometimes the right last move.

**Why this matters specifically for OE:**

1. **Budget reality.** OE is a CTO + AI-substrate research operation, not pharma. A daemon sweep costs ~$0.65; freaking out over a $50 sweep cost is the appropriate calibration. Proposing $30K+ experiments without walking the upstream cost ladder is a category error.
2. **Tier 0 + Tier 1 frequently resolve the question.** comp-016's verdict (T → intestinal ABCG2 suppression WEAK / UNCONFIRMED) was reached entirely from public-literature scanning — the question was already answered by Klyushova 2023, MacLean 2008, Hoque 2020, Yu 2021. **The institutional-default mouse experiment was unnecessary; the answer existed.** Tier 0 caught what Tier 4 would have only confirmed.
3. **Existing self-experiment infrastructure makes Tier 1 nearly free.** OE has running n=1 self-experiment protocols ([`self-experiment-protocol.md`](./self-experiment-protocol.md)) with established lab-panel workflows. Adding a new measurement to that workflow costs $50–100 per data point, not $30K.
4. **Crowdsourced cohorts produce real n>>1 evidence at $0 marginal cost.** The men's-health, gout, and microbiome communities on Twitter / Reddit / Hone routinely share lab panels publicly. Treating that as a usable data source (with appropriate methodological caveats) is the open-source-platform thesis applied to evidence gathering.
5. **The "killshot" framing should be: cheapest experiment that resolves the question, not biggest experiment that proves the answer beyond doubt.** Falsification-card discipline (per [`linter-design.md`](./linter-design.md)) is about *attempting* to falsify, not about overwhelming the question with budget. A $300 experiment that crosses a pre-committed threshold kills (or saves) a hypothesis as decisively as a $30K one.

**Worked example — H07 Clomid intestinal-ER-antagonism thesis** ([`hypotheses/H07-clomid-intestinal-er-antagonism.md`](./hypotheses/H07-clomid-intestinal-er-antagonism.md)):

- **Tier 0:** GTEx + HPA sex-stratified intestinal ABCG2 mining ($0); full-text re-read of the 4 anchor papers Klyushova 2023, MacLean 2008, Hoque 2020, Yu 2021 ($0). Estimated to resolve sub-claim 1 (does the PI3K/Akt → ABCG2 mechanism replicate in vivo?) and partially sub-claim 3 (is the renal arm enough?).
- **Tier 1:** n=1 FEUA tracking on Clomid dose changes (~$300). Resolves sub-claim 3 for one individual definitively.
- **Tier 2:** Crowdsourced clomiphene-vs-enclomiphene-vs-TRT cohort labs sharing ($0 in materials, weeks of community work). Resolves sub-claim 4 (the enclomiphene UA-direction question).
- **Tier 3:** Caco-2 + SERM treatment ($2–5K). Resolves sub-claim 2 (intestinal ER tissue-specificity under clomiphene).
- **Tier 4:** Mouse castration + T/E2 replacement + intestinal ABCG2 measurement ($5–15K via academic collaborator). Reserved as last resort.

The Tier 0 + Tier 1 combination probably closes the H07 thesis at >80% confidence for ~$300 + a week of analysis. Tier 4 is the institutional default; for OE it's the last resort, not the first move.

**This discipline composes with the pre-commit verification gate.** Both are "walk the checklist before shipping." The verification gate catches numerical hallucinations; the killshot tiering catches budget over-specification. Different failure modes; same shape of fix (named protocol, applied at the right moment in the workflow).

For falsification-card stub authoring (per [`hypotheses/README.md`](./hypotheses/README.md)), the killshot menu in the stub should be tier-explicit: each killshot listed with its cost tier, so the stub-to-full-card promotion can pick the right starting tier rather than defaulting to institutional.

---

## Specific OE questions worth Paperclip search-and-verify time

These are questions whose primary-literature grounding would meaningfully advance the platform but require non-trivial scanning. Listed here so they're discoverable as a queue (anyone reading this page can pick one up):

1. **Does *Candida utilis* uricase have published KEX2-site / cassette-compatibility data?** — supports comp-011 (the *C. utilis* uricase compatibility analysis). Search: `Candida utilis uricase Aspergillus` + grep KEX2, signal peptide, secretion.
2. ***Aspergillus oryzae* heterologous expression precedents** beyond what comp-010 + Killshot #1 already surfaced — particularly any solid-state-format dual-protein work. Search: `Aspergillus oryzae solid-state heterologous protein` + grep dual cassette, multi-cassette, two genes.
3. **ABCG2-probiotic intersections** — does any published probiotic strain (engineered or natural) modulate intestinal ABCG2 expression in vivo? Informs the LBP track's butyrate-via-*F. prausnitzii* thesis. Search: `ABCG2 probiotic` + grep intestinal expression, fold-change.
4. **GRAS-host complement-regulator expression** — has anyone published heterologous expression of soluble complement regulators (sCR1, Factor H, DAF/CD55) in any GRAS organism? Informs comp-006 / comp-012 platform implications. Search: `complement regulator heterologous expression yeast Aspergillus` + grep specific protein names.
5. **Si Miao San and related TCM gout formulas** — modern Chinese clinical evidence. Per the global-multilingual default ([CLAUDE.md](../CLAUDE.md) §"Global-multilingual research by default"), search Chinese-language sources directly via CNKI / WanFang / ChiCTR, not just PubMed-indexed translations. Informs the TCM × rigor track ([tcm-modern-rigor-intersection.md](./tcm-modern-rigor-intersection.md)) Phase 2 P2-1.
6. **NSlD-ΔP10 strain availability outside the Maruyama lab** — verify the `operations/ward-1995-lab-access.md` finding that the strain isn't in any public repository by direct catalog query at JCM, NBRC, CGMCC, CBS-KNAW, ATCC, FGSC.

## When Paperclip is the wrong tool

- **For ChEMBL bioactivity data** — use the ChEMBL MCP directly. Paperclip's index is paper-level; ChEMBL is target-and-compound-level with curated quantitative bioactivity. See [`chembl-cross-check.md`](./chembl-cross-check.md) for the cross-check discipline.
- **For patents** — Paperclip indexes academic literature, not patent literature. Use Google Patents, Espacenet, Lens.org, JPlatPat, CNIPA directly via WebFetch.
- **For non-English-language clinical trial registries** — ChiCTR (Chinese), JPRN (Japanese), KISS (Korean) registries are not in Paperclip's index. Direct WebFetch of those registries is the right tool.
- **For real-time updates** — Paperclip's index has an indexing lag. For the very most recent findings (within the last 1–4 weeks), the journal websites or PubMed direct may have content Paperclip doesn't yet have.

## Cross-references

- [`paperclip-deep-dive.md`](./paperclip-deep-dive.md) — full Paperclip MCP capability + limitation audit (the upstream documentation this page operationalizes for OE)
- [`bio-ai-tools.md`](./bio-ai-tools.md) — broader AI-tool landscape for biology research
- [`chembl-cross-check.md`](./chembl-cross-check.md) — sister discipline for ChEMBL bioactivity verification
- [`open-source-platform.md`](./open-source-platform.md) §"Multi-model synthesis as guard against epistemic homogenization" — the broader epistemic-rigor framework this protocol fits within
- [`CLAUDE.md`](../CLAUDE.md) §"Global-multilingual research by default" + §"Translation protocol" — the multilingual + cross-vendor disciplines that combine with this protocol for non-English Paperclip-adjacent work
