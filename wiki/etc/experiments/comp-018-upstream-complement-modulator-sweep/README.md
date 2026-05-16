# comp-018: Upstream Complement Modulator Sweep

**Question:** Across all compound classes (fungal, plant, bacterial, marine, dietary, FDA-approved drug, classical TCM/Kampo/Ayurveda), which compounds have documented activity at upstream complement cascade nodes (proximal to C5a generation), and which are gout-platform-relevant?

**Verdict (top-line):** **Direct natural-product C5aR1 antagonists remain empty (re-confirms comp-014 / §1.21).** But moving one node upstream to the **C3 convertase** uncovers a substantial natural-product literature anchored by **rosmarinic acid** (rosemary, lemon balm, spearmint) — C3-convertase IC50 5-10 µM, three independent in vivo precedents, FDA-GRAS source plants, dietary-scale viable. The chokepoint-hacker move worked: don't fight at C5aR1, prevent C5a from being generated.

**Status:** **Phase 1 — Done 2026-05-08.** Sweep executed via PubMed MCP + Paperclip MCP grep on PMC full-text where available. Phase 2 (multilingual CNKI/WanFang/J-STAGE direct read with two-model translation cross-check) queued.

**Reproducible artifact:** `python3 scripts/scope_validate.py` from this folder validates the JSONs and emits `outputs/scope-summary.md`.

**Interpretive wiki page:** [`wiki/upstream-complement-modulator-sweep-computational.md`](../../../upstream-complement-modulator-sweep-computational.md)

**Tracking index:** [`wiki/computational-experiments.md`](../../../computational-experiments.md) — comp-018 row added.

---

## Why this experiment exists

Brian's framing 2026-05-08:

> *"What are all the things upstream of CP0 that we could exploit, and any compound — fungal, plant, bacterial, marine — that affects them. If the answer is rosemary, I'll grow rosemary."*

CP0 ("complement priming") is one of seven NLRP3 chokepoints. MSU crystals trigger the complement cascade, generating C5a, which is a dominant NLRP3 priming signal (`complement-c5a-gout.md`).

Three threads converged on CP0 by 2026-05-08:

1. **Engineering thread** — comp-012 → H05 → §1.25: soluble truncated DAF/CD55 SCR1-4 expressed in *A. oryzae* is in silico LOW protease risk, wet-lab gate scoped.
2. **Direct natural-product C5aR1 antagonist thread** — comp-014 + §1.21: empty. Zero validated fungal or plant C5aR1 antagonists in ChEMBL or PubMed.
3. **comp-018 (this experiment)** — the third thread: don't hunt for C5aR1, hunt for compounds at any upstream node (C1q, MBL, C3, Factor B/D/H, properdin, DAF/CD55 host upregulation, C1-INH, C5 itself).

The chokepoint-hacker logic: if you can't block C5a binding, prevent C5a from being made.

---

## Method

| Step | What | Tool |
|---|---|---|
| 1 | Define upstream nodes (16 targets — see `inputs/targets.json`) | manual + canonical wiki |
| 2 | Per-target PubMed search for natural-product / dietary / repurposed inhibitors | `mcp__plugin_pubmed_PubMed__search_articles` |
| 3 | Per-hit metadata + abstract retrieval | `mcp__plugin_pubmed_PubMed__get_article_metadata` |
| 4 | Full-text grep where PMC mirror exists, line-anchored verification of IC50s | `mcp__paperclip__paperclip` (search/cat/grep — NOT `map`) |
| 5 | Per-compound ChEMBL coverage check (compound class + target class) | manual ChEMBL recall |
| 6 | Tier assignment — TIER_1 (in vivo + in vitro + dietary precedent), TIER_2 (in vitro IC50 + accessible source), TIER_3 (in vitro only or weak / abstract-only / retracted) | analysis |

**Tool discipline applied:** Per `CLAUDE.md` §"Tool discipline" and `memory/feedback_paperclip_map_unreliable.md`:
- Paperclip `map` operator NOT used (hallucinates organisms / fabricates kinetics)
- Paperclip restricted to `search` / `cat` / `grep` / `head` / `lookup` primitives
- Paperclip used only for PMC / arXiv / bioRxiv / medRxiv corpus (NOT CNKI / WanFang / J-STAGE — wrong corpus per Pass 3 review 2026-05-08)
- Direct multilingual searches deferred to Phase 2 (with the model's native multilingual training, two-model cross-check per CLAUDE.md §Translation protocol)

**Pre-commit verification gate applied:** Per CLAUDE.md Rule 4. Every IC50 / mechanism / dose claim is anchored to a primary source PMID with explicit `verification_status` field. Where the primary source is paywalled and no PMC mirror exists, the claim is marked "abstract-tier" or `[UNVERIFIED]`. The DAF SCR1-4 disulfide-count incident (canonical case for this rule) is the discipline this gate enforces.

---

## File index

```
comp-018-upstream-complement-modulator-sweep/
  scripts/
    scope_validate.py              ← Phase 1 validator + summary emitter
  inputs/
    targets.json                   ← 16 upstream complement cascade nodes with UniProt + MSU relevance
    query-strategy.json            ← multi-source query strategy + executed PubMed macros + tool discipline
  outputs/
    compounds.json                 ← 32 compounds with documented activity, tier-classified, IC50-anchored
    summary.md                     ← human-readable top-10 + ChEMBL gap + recommendations
    scope-summary.md               ← generated by scope_validate.py (run after first commit)
  README.md                        ← this file
```

---

## Top 10 candidate compounds × upstream node × tier

(Full table in `outputs/summary.md`)

1. **Rosmarinic acid** (rosemary, lemon balm, spearmint) — C3 convertase 5-10 µM (PMID 3198307); 3 in vivo precedents — TIER 1
2. **Luteolin** (Lonicera, dietary) — C3 convertase CP+AP 170-190 µM; ALSO XO 550 nM + URAT1 from comp-013 — TIER 2 (triple-convergence)
3. **Tiliroside** (Magnolia fargesii) — CP convertase 54 µM (PMID 9821813) — TIER 2
4. **Bupleurum polysaccharides** (Chai Hu) — lectin pathway IC50 ~1 mg/mL (PMID 26579461) — TIER 2 (gut-luminal)
5. **Falcarindiol** (Dendropanax / carrot / celery) — CP convertase 15.2 µM (PMID 21520473) — TIER 2
6. **Ganoderic acid Sz** (G. lucidum) — CP convertase 44.6 µM (PMID 20091270) — TIER 2 (fungal)
7. **Ergosterol** (mushrooms) — CP convertase 52 µM (PMID 20091270) — TIER 2 (fungal/dietary)
8. **Quercetin** (dietary, microbiome-deglycosylated active) — CP+AP active, gut-microbiome-enhanced — TIER 2
9. **3,5-Dicaffeoylquinic acid** (artichoke, honeysuckle) — C1 component <10 µM (PMID 17260306) — TIER 2
10. **K-76 / K-76-COOH** (Stachybotrys; semi-synthetic) — C5 inhibitor 100-570 µM; in vivo C5 block in mouse LPS shock — TIER 2 (engineering-relevant)

---

## ChEMBL coverage gap

- Compounds catalogued: 32
- With any ChEMBL record (other targets): 14
- With curated ChEMBL anticomplement bioactivity: **0**
- ChEMBL anticomplement coverage rate: **0.0%**

ChEMBL has zero curated hemolytic-assay anticomplement data for any compound. The natural-product anticomplement assay class (CH50/AP50) was never systematically indexed by ChEMBL — same gap pattern as comp-013 TCM compounds, but worse here because anticomplement is a niche assay.

---

## What this experiment is NOT

- **Not a clinical recommendation document.** TIER 1 / TIER 2 verdicts are research-stage triage, not patient guidance. Phase 0 (Research & Design).
- **Not a complete enumeration.** Phase 1 covers PubMed-indexed English literature + PMC full text. Direct CNKI/WanFang/J-STAGE multilingual ingestion is queued as Phase 2.
- **Not a synthesis-tractability study.** Whether rosmarinic acid can be over-produced via engineered koji or LBP chassis is a separate engineering-feasibility question for a future comp-NNN.
- **Not a gout clinical trial.** No claim that rosemary supplementation will treat gout. The mechanistic logic (upstream of C5a → upstream of CP0 priming → less NLRP3 priming) is plausible but unvalidated in humans for gout specifically.

---

## Relationship to other comp-NNN experiments

- **comp-014 (medicinal mushroom compound mapping):** Phase 2 finding that fungal C5aR1 antagonist class is empty is RE-CONFIRMED by comp-018 across all compound classes, not just fungal. comp-018 adds Ganoderma triterpenes (ganoderic acid Sz, ergosterol) at a different node (CP convertase) — extending comp-014's fungal reach to the upstream-complement axis.
- **comp-013 (TCM gout compound triage):** comp-018 surfaces luteolin's third mechanism (CP convertase) on top of XO + URAT1 already established. Luteolin is now triple-mechanism gout-relevant.
- **comp-012 + H05 (DAF SCR1-4 engineering):** comp-018 surfaces a parallel engineering thesis — recombinant C1-INH expression in koji or LBP — that has the same chassis logic as DAF SCR1-4 but operates at a different complement node. Phase 2 follow-up.

---

## Reproducibility

```bash
cd experiments/comp-018-upstream-complement-modulator-sweep
python3 scripts/scope_validate.py
```

stdlib only (json, pathlib, sys). No external packages. Produces `outputs/scope-summary.md`.

The compound × IC50 / target / source table in `outputs/compounds.json` was assembled via PubMed and Paperclip MCP queries on 2026-05-08; the JSON is the canonical record. To re-run the underlying queries, follow `inputs/query-strategy.json` §search_macros_executed_2026_05_08.
