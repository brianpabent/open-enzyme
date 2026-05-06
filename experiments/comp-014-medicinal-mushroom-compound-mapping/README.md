# comp-014: Medicinal Mushroom Compound × Chokepoint Mapping

**Question:** Across all known characterized fungal natural products — aggregated from sources that span the global research corpus, not just Western pharma — which compounds map onto Open Enzyme's existing chokepoints (uricase substrate, URAT1, ABCG2, NLRP3 axis, complement CP0, Lp-PLA2, HDAC6, redox/disulfide chemistry), and which fungal species are the highest-leverage producers?

**Status:** **Phase 1 — Scoped, execution pending.** This commit registers the experiment scope (candidate species, chokepoint targets, multi-database aggregation plan, multilingual literature plan). It does NOT yet contain pulled compound data, target mappings, or per-compound triage verdicts. Phase 2+ executes after Brian's review.

**Reproducible artifact:** `python3 scripts/scope_validate.py` from this folder validates the input JSONs and emits `outputs/scope-summary.md`.

**Interpretive wiki page:** [`wiki/medicinal-mushroom-compound-mapping-computational.md`](../../wiki/medicinal-mushroom-compound-mapping-computational.md)

---

## Why this experiment exists

Brian's framing (2026-05-06):

> *"There are so many different types of fungus out there, and they have different compounds. Those compounds have different medicinal benefits depending on how they are ingested. I'm just really curious: is there a way to pull in all of the known compounds from as many species as possible and then map that to our chokepoints? Because I suspect there are some compounds in mushrooms that could be beneficial to this project in one way or another, whether that's directly in the body or, who knows, something else like helping disulfides or some shit."*

The path-dependent failure mode this experiment guards against (per `Open Enzyme/CLAUDE.md` global-multilingual-research rule and umbrella `CLAUDE.md` Curiosity & First-Principles Framing): defaulting to ChEMBL-only (Western pharma slice) and missing the substantial East-Asian-clinical-experience evidence base for medicinal fungi. comp-013 surfaced this as a *named gap* for TCM phytochemicals; the same gap applies — and is likely larger — for medicinal mushrooms, because mycotherapy is a deeper traditional-medicine vertical in Chinese and Japanese practice than most TCM herbs.

The "redox/disulfide chemistry" angle in Brian's framing is non-trivial. It points at a chokepoint Open Enzyme has not formally mapped on the patient side. The DAF SCR1-4 disulfide-count incident (`Open Enzyme/CLAUDE.md` §Pre-commit verification gate) shows disulfide chemistry is already load-bearing on the engineering side. Whether to elevate this to a formal patient-side chokepoint is a Phase 5 decision, gated on what the breadth pass surfaces.

---

## Multi-phase execution plan

| Phase | What it does | Status |
|---|---|---|
| **Phase 1** | Scope: chokepoint targets, anchor species (sanity-check), toxicity filter, data-source inventory, multilingual literature plan. | **Done.** |
| **Phase 2** | Breadth aggregation, **species-agnostic with toxicity filter**. Pull every fungal compound from LOTUS + NPAtlas + KNApSAcK + NPASS + TCMSP + COCONUT. Apply toxicity-filter.json (FDA GRAS / EFSA QPS inclusion; WHO Pathogens 2022 + mycotoxin producers + Schedule I/II exclusion). Expected: 500-2000 unique species after filter. Output: unified fungal compound × species table. | **Starting now.** |
| **Phase 3** | Target mapping: ChEMBL + HIT + PubChem BioAssay (empirical) → SwissTargetPrediction (orphans). Output: compound × target table flagged empirical/predicted. | Concurrent with Phase 2 where possible. |
| **Phase 4** | Chokepoint intersection: join compound × target × Open Enzyme chokepoints. Output: ranked candidate compound × chokepoint pairs. | After Phases 2-3. |
| **Phase 5** | Multilingual literature ingestion **for every chokepoint-hit species, parallel via subagents**. CNKI + Wanfang + J-STAGE + KISS with two-model cross-check (Claude + DeepSeek for Chinese — DeepSeek as Model B per CLAUDE.md §Translation protocol). NOT capped at top-3-5 — that gating was the exact path-dependent narrowing the umbrella CLAUDE.md flags. Decide: redox/disulfide chokepoint ADMIT / PRELIMINARY / REJECT. | After Phase 4. |
| **Phase 6** | Per-compound triage: comp-013-style IC50 occupancy + composite scoring on top candidates. Verdicts: GUT-LUMINAL VIABLE / SYSTEMIC VIABLE / MECHANISM UNCLEAR / NON-VIABLE. Subset gets shio-koji protease stability comp-NNN follow-ups. | After Phase 5. |

**Why phase-gated rather than monolithic:** Phase 2 alone is on the order of 30-80K compound records; Phase 5 multilingual literature ingestion has nontrivial token cost (translation cross-check doubles inference per source paper). Brian decides which phases are worth running, in what order, after seeing the scope.

---

## Reproducibility (Phase 1 only)

```bash
cd experiments/comp-014-medicinal-mushroom-compound-mapping
python3 scripts/scope_validate.py
```

stdlib only (json, pathlib). No external packages. Produces `outputs/scope-summary.md`.

Phase 2+ will add per-phase scripts. Each will follow the same stdlib-only + reproducible-from-cold pattern as comp-013.

---

## File index

```
comp-014-medicinal-mushroom-compound-mapping/
  scripts/
    scope_validate.py              ← Phase 1 validation + summary emitter
  inputs/
    phase-5-anchor-species.json    ← 18 well-studied fungi for Phase 2 sanity-check + Phase 5 deep-dive seed
    toxicity-filter.json           ← inclusion (GRAS/QPS/pharmacopoeia/clinical-trial) + exclusion (WHO 2022/mycotoxin/Schedule I) lists
    chokepoint-targets.json        ← Open Enzyme chokepoints with UniProt + 1 proposed addition
    data-sources.json              ← multi-DB aggregation plan + multilingual literature corpora + DeepSeek-as-Model-B translation pairing
    provenance.md                  ← source-of-source notes for the input curation
  outputs/                         ← generated by scope_validate.py
    scope-summary.md               ← human-readable Phase 1 scope summary
  README.md                        ← this file
```

---

## What this experiment is NOT

- **Not a meal-planning tool.** Does not recommend supplements or recipes.
- **Not a clinical guidance document.** "GUT-LUMINAL VIABLE" verdicts (when Phase 6 runs) are research-stage triage, not patient recommendations.
- **Not a pharmacognosy textbook.** Out of scope: total-synthesis tractability, marine-fungal natural products (separate corpus), mycotoxin survey for food safety (separate concern from chokepoint mapping).
- **Not a koji-engineering proposal.** comp-014 is upstream of engineering decisions. If the breadth pass surfaces a fungal compound that maps strongly onto a chokepoint and the producer fungus is cultivable, that's evidence for considering a separate engineering-feasibility comp-NNN — not a deliverable of this experiment.

---

## Disagreement protocol

If you reproduce the Phase 1 scope and disagree with:

- **Candidate species selection** — file a GitHub issue against `comp-014-medicinal-mushroom-compound-mapping` proposing additions/removals with rationale.
- **Chokepoint inventory** — should map back to wiki canonical chokepoints; if a chokepoint is missing or one of the listed ones is non-canonical, raise as an issue and reference the canonical wiki page.
- **The proposed redox/disulfide chokepoint addition** — Phase 5 is the formal decision point; pre-Phase-5 disagreement is a useful prior to record but the rejection criteria are documented in `chokepoint-targets.json`.
- **Database coverage** — if a major fungal-compound or East-Asian-pharmacology database is missing from the source list, that is a Phase 1 scope bug — file an issue with the source URL and access notes.
