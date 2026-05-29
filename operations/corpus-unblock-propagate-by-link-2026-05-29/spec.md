# Spec — Sweep Corpus Unblock (dedup + archive) + Pass-1 Propagate-by-Link

**Date:** 2026-05-29
**Branch:** `corpus-unblock-propagate-by-link`
**Author:** Brian + Claude (Opus 4.8)
**Status:** DRAFT — for independent-model review before implementation
**Reviewers:** (1) external model reviews *this spec* before work begins; (2) independent model reviews *the implemented work* before merge.

---

## 0. TL;DR

The `wiki-sweep` daemon has failed on every run since 2026-05-22 because the Pass 2 (Synthesize) prompt outgrew every model's context window. Root cause is twofold and coupled: (a) the prose corpus crossed ~1.0M tokens *now*, and (b) it keeps self-inflating because Pass 1 (Propagate) copies exposition into related pages instead of linking to a canonical page.

This spec covers two workstreams to be done together on one branch:

- **Workstream A — Corpus unblock (immediate):** deduplicate cross-page restatement and archive the append-heavy `validation-experiments.md`, bringing the Pass 2 prompt back under existing model caps without changing model routing or building sharded synthesis.
- **Workstream B — Propagate-by-link (durable):** change Pass 1's propagation discipline so new findings are written *once* on a canonical page and *linked* from related pages, instead of copied. This stops the corpus self-inflating at the source.

Sharded synthesis (the larger rebuild) is explicitly **out of scope** and demoted to a fallback only if B proves insufficient.

---

## 1. Problem statement & diagnostic evidence

### 1.1 The failure
- `wiki-sweep.yml` (GitHub Actions) runs three passes: Gate → Pass 1 Propagate → Pass 2 Synthesize → Pass 3 Review. Pass 3 advances a cursor in `logs/sweep-state.json` and emits items into `synthesis/queue/`.
- **Last successful sweep:** commit `e587aa1`, 2026-05-21 16:46Z (registry `last_successful_sweep`).
- **Three consecutive failures since:** run `26314082579` (2026-05-22, push), `26334305149` (2026-05-23, dispatch), `26362921474` (2026-05-24, dispatch). Nothing has run since 2026-05-24.
- In each, **Gate ✓ → Pass 1 ✓ → Pass 2 ✗** (exit 1 after ~21 min) → Pass 3 never runs.
- Because Pass 1 still commits its propagation (e.g. `4c3c416 sweep-1-propagate … [skip-wiki-sweep]` at main HEAD) but Pass 2/3 never complete, the queue stays empty and the cursor never advances — **"inbox zero" is a false negative, not a clean state.**

### 1.2 Root cause (verbatim from the failed Pass 2 log, run 26362921474)
```
WARNING: estimate 955,927 tokens approaches primary deepseek/deepseek-v4-pro's
1,000,000 cap. Likely fallback to google/gemini-2.5-pro.
...
curl: (22) error 400: "This endpoint's maximum context length is 1048576 tokens.
However, you requested about 1049444 tokens (1017199 of text input, 245 of tool
input, 32000 in the output)."
```
The whole-corpus synthesis prompt is ~1.017M tokens of text input. It overshoots DeepSeek V4-Pro (1.000M primary) **and** the Gemini 2.5 Pro fallback (1.048M) — the multi-model fallback cannot rescue a prompt no configured model can hold.

### 1.3 The corpus
- `build_corpus()` (`scripts/synthesize.py`) globs `wiki/*.md` + `wiki/hypotheses/*.md`, minus an `EXCLUDE` list. **`wiki/etc/**` is NOT in the corpus** (the glob is `wiki/*.md`, not `wiki/**/*.md`) — this is why moving content into `wiki/etc/` removes it from the Pass 2 prompt.
- Top-level `wiki/*.md`: **111 files, ~911K tokens** (3,643,636 chars). Plus `wiki/hypotheses/*.md` (H-cards) and minus EXCLUDE.
- Largest single page: `validation-experiments.md` at **~65K tokens (7% of corpus in one file)**, grown by sweep-driven accretion (its `### 3.X` self-experiment sections run 3.1→3.11; 31 of its last 40 commits are sweep/walkthrough-tagged).
- Growth rate: ~611K tokens (2026-05-05, per `synthesize.py` comment) → ~911K (2026-05-24) ≈ **~100K tokens/week** during a heavy content-push period (steady-state likely lower, but the trend is the point).

### 1.4 The self-inflation mechanism (why pruning bounced back)
A corpus-wide provenance scan (paragraphs carrying `(Source: <other-wiki-page>.md)` tags) found:
- **~50K tokens (5.4% of corpus) are cross-page-sourced**, of which **~47K are long blocks (≥200 chars) — substantive restated exposition**, not one-line citations.
- Paragraph counts attribute 76 paras to `nlrp3-exploit-map.md`, 65 to `engineered-yeast-uricase-proposal.md`, 60 to `gout-deep-dive.md`, etc. These counts are the fingerprint of **Pass 1 propagating findings by copying exposition** (with a `(source:)` tag) into related pages.
- **Conclusion:** Pass 1's propagate-by-copy behavior is simultaneously the corpus-growth driver and the redundancy source. Dedup alone is fighting the daemon's own behavior; without B, the restatement regrows.

### 1.5 Verification of the two earlier conclusions
- Verbatim duplication is negligible (~0.3%) — the redundancy is *condensed/paraphrased* restatement, openly provenance-tagged, which exact-match scanning misses but the `(Source:)` scan catches.
- TF-IDF overlap pairs are mostly legitimately-related pages; only a handful of large pairs are genuine restatement (see §3.1).

---

## 2. Goals / Non-goals

### Goals
1. **Unblock the daemon under existing model routing** (DeepSeek V4-Pro primary, Gemini 2.5 Pro fallback) — Pass 2 prompt back under ~950K tokens with headroom.
2. **Stop the corpus self-inflating** — Pass 1 propagates by link, not by copying exposition.
3. **Preserve all canonical content and evidence integrity** — no information loss, no evidence-tag loss, no broken links.
4. Fix two cross-page contradictions found in the audit while editing adjacent text (§3.4).

### Non-goals (explicitly out of scope)
- **Sharded / hierarchical synthesis** — deferred; only revisited if B proves insufficient against future growth.
- **Model-routing changes** (e.g., routing Pass 2 to a 2M-context model) — not needed if A succeeds; avoided because routing has a documented mistake history (`synthesize.py` comments).
- **Touching `wiki/etc/**`, `reference/*`, `*.html`** content.
- **Re-architecting Pass 2 or Pass 3.**

---

## 3. Workstream A — Corpus unblock (dedup + archive)

### Guiding principle — canonical ownership
For any concept, **one page owns the exposition** (the primary-research doc or the designated concept page). Other pages get **a one-line recap + a markdown link**, never a copied exposition block. Explicitly *legitimate* and **kept**:
- Brief recap-with-a-link (1–3 sentences) that orients the reader before linking.
- Intentionally consolidated safety boilerplate (the `supplements-stack.md` standardized drug-interaction / dose-risk blocks restated on individual compound pages) — this is a deliberate pattern, leave it.
- A compact reference table that defines vocabulary the rest of the corpus cites (e.g., the CP0–CP6b chokepoint table).

### A1. The five audited pairs (agent-reviewed; exact trims)

| # | Trim target page | Canonical owner | What to trim → replace with | Est. savings | Hard constraint |
|---|---|---|---|---|---|
| 1 | `nlrp3-inflammasome.md` | `nlrp3-exploit-map.md` | The full 7-chokepoint exploit catalog (CP0→CP6b "The Step / Why / Exploits"), "Multi-Chokepoint Compounds", "SIBO–Gout–Lynn", koji-production sections → compact CP0–CP6b table + link lines | ~6.5–7.5K | **Keep a compact CP0–CP6b table** (vocabulary 10+ pages cite). **Do NOT delete** the anakinra acute-flare protocol / inhaled-mRNA-IL-1RA detail until confirmed canonical in `chassis-pending-interventions.md §4` / `gout-action-guide.md`. |
| 2 | `saccharomyces-cerevisiae.md` (the *derivative* page) | `engineered-yeast-uricase-proposal.md` | Delivery-formats a–e, dosing mathematics, gene-construct/source-gene table, product regulatory framing → link to proposal §§3–6 | ~3.5–4K | **Keep** the 13%-of-protein expression figure on the chassis page (Rasburicase Precedent block); keep generic organism biology (GRAS, transformation toolkit, A.oryzae comparison). Proposal page untouched. |
| 3 | `peptide-gout-addendum.md` | `bpc-157.md`, `kpv-peptide.md` | Deep per-peptide mechanism/dosing/safety expositions → gloss + link | ~2.2–2.8K | **Keep** the synthesis layer (stacking tiers, flare-phase timing table, "Honest Assessment", gut–urate axis). Preserve `[Mostly Preclinical]` / `[Preclinical + Mechanistic]` inline tags in the gloss. |
| 4 | `gout-deep-dive.md` ↔ `gout-pathophysiology.md` (bidirectional) | mechanism → `gout-pathophysiology.md`; treatment/pipeline/GWAS → `gout-deep-dive.md` | Trim deep-dive §1 cascade → link to pathophysiology; trim pathophysiology's treatment/pipeline/GWAS copies → link to deep-dive | ~2.5–3K | Keep heading stubs so TOC anchors resolve; keep deep-dive "two ways to solve gout" hook (1 sentence). Update now-circular `(Source:)` self-citations. |
| 5 | `blood-barrier.md` (framing layer) | `blood-barrier-exploits.md` | "Barrier's Multiple Defenses" + the "14 Theoretical Routes" re-list → recap + link | ~0.65–0.7K | Keep the page's distinct framing (lumen-sink rationale, oral tolerance, delivery formats). |

**A1 subtotal: ~15.5–18K tokens.**

### A2. Next-tier derivative pages (require per-page audit before trim)
The provenance scan flags these as heavily cross-page-sourced. Each needs the same agent-style link-vs-restate read **before** trimming (do not blind-trim):

| Page | % sourced | Likely canonical owner(s) to link to |
|---|---|---|
| `uricase.md` | 59% | `engineered-yeast-uricase-proposal.md`, `crispr-uricase.md`, `gout-pathophysiology.md` |
| `carnosine.md` | 42% | `koji-endgame-strain.md`, `nlrp3-exploit-map.md` |
| `gut-lumen-sink.md` | 41% | `gout-pathophysiology.md`, `abcg2-modulators.md` |
| `bhb-ketones.md` | 36% | `nlrp3-exploit-map.md`, `supplements-stack.md` |
| `aspergillus-oryzae.md` | 34% | `engineered-koji-protocol.md`, `koji-home-fermentation.md` |
| `disulfiram.md`, `oridonin.md`, `digestive-enzymes.md`, `sibo.md` | 22–30% | per-page |

**A2 estimated additional recovery: ~12–15K tokens** (realistic, keeping legitimate recaps). Combined A1+A2 realistic recovery: **~28–33K tokens.**

### A3. `validation-experiments.md` archive-split
- Create `wiki/etc/validation-experiments-archive.md` (in `wiki/etc/` → auto-excluded from corpus).
- **Move:** closed / frozen / superseded validation sections — specifically the `### 3.X` self-experiment protocol blocks that are designed but not active, and any frozen `### 1.X` computational-validation sections whose comp-NNN is closed.
- **Keep on `validation-experiments.md`:** active/in-flight experiments + a one-line link to the archive for the rest.
- **Decision needed (see §7 Open Questions):** do all `### 3.X` self-experiment sections move, or only closed ones? Proposed default: move closed/not-yet-active; keep active.
- **Estimated recovery: ~40–50K tokens** (the page is ~65K; target retaining ~15–25K of active content).

### A4. Contradictions to fix in-flight (grep-verify against primary source)
1. **Dapansutrile trial phase:** `peptide-gout-addendum.md` says "Phase II" for gout; `kpv-peptide.md` says "Phase 3." Verify against primary source, harmonize.
2. **`index.md` swapped descriptions:** the one-liners for `blood-barrier.md` (line ~86) and `blood-barrier-exploits.md` (line ~197) are swapped relative to actual content. Fix descriptions.

### A5. Token-math acceptance target
- Current Pass 2 text input: ~1,017K.
- A (dedup ~28–33K) + A3 (archive ~40–50K) = **~68–83K reduction** → Pass 2 text input **~934–949K**.
- Under DeepSeek primary (1.000M) with ~50–66K headroom AND Gemini fallback (1.048M) with ~100K headroom. **Daemon unblocks under existing routing.**

---

## 4. Workstream B — Pass-1 propagate-by-link (durable fix)

### B1. Current behavior (`scripts/sweep-prompt-1-propagate.md`, step 3)
Pass 1 has a dedup guard that prevents re-copying the *same* content across sweeps, but for **genuinely new** findings its default action is **"insert a fresh subsection"** with `(source: <trigger>)`, and it instructs "don't append 'see also' footnotes" + "err toward more updates." Net effect: new findings are *copied as exposition* into every related page → the 47K restatement, growing each sweep.

### B2. Target behavior
Change the propagation discipline so that, when propagating a finding to a page that is **not** the finding's canonical home:
1. **Identify the canonical page** for the finding (the trigger file, or the established concept/primary-research page for that mechanism).
2. **Write the full exposition once**, on the canonical page only.
3. **On each related page, insert a one-line pointer + link**, carrying only the *minimal delta* needed for local context (e.g., "X also modulates CP2 — see [canonical page](./x.md) for mechanism and evidence"), with the evidence tag on the claim but **not** a copied mechanism block.
4. **Reserve full copies** for the genuinely-justified cases: a load-bearing number the local page's own reasoning depends on, or content with no other canonical home.

### B3. Implementation
- **Primary change:** rewrite step 3 of `scripts/sweep-prompt-1-propagate.md` to encode B2 — replace "insert a fresh subsection" default with "link to canonical + minimal delta" default; add an explicit canonical-ownership determination step; redefine when a full copy is permitted; keep the existing cross-sweep dedup guard.
- **Fix stale path:** the prompt references `wiki/GRAPH.md`; correct to `wiki/etc/GRAPH.md` (post-reorg). Verify the `lint-mermaid.py` invocation path too.
- **Optional guardrail (decision needed, §7):** add a check in `scripts/sweep-1-propagate.py` (or a post-pass lint) that flags when a propagation commit adds more than N lines (proposed N≈8) of new prose to a *non-canonical* page, as a soft signal of copy-instead-of-link. Could be advisory (log) or blocking.
- **No change** to Pass 2 / Pass 3 / model routing.

### B4. Acceptance
- A representative test propagation (re-run Pass 1 locally against a sample trigger file, or dry-run) adds links + minimal deltas, not copied exposition blocks.
- Re-running the `(Source:)` provenance scan after a few real sweeps shows the long-block restatement volume **flat or shrinking**, not growing.

---

## 5. Execution plan

1. **Single branch:** `corpus-unblock-propagate-by-link` (already created).
2. **Order of work:**
   - **B first** (rewrite Pass-1 prompt) — so the dedup in A demonstrates the target end-state and we don't immediately re-pollute.
   - **A2 per-page audits** (subagent reads) → then A1+A2 trims, A3 archive, A4 contradiction fixes.
   - Re-run the token-count + provenance scans locally to confirm §4.5 target met **before** any push.
3. **Commit discipline:** eager commits, scoped per logical unit (B prompt change; each dedup cluster; archive-split; contradiction fixes). Hold all pushes per Open Enzyme push-batching rule.
4. **Push/merge gating:** **Do not merge to main until** the local corpus token count confirms Pass 2 will fit (< ~950K). Otherwise the post-merge daemon run fails a 4th time. The successful post-merge daemon run is the real-world acceptance test.
5. **PR flow:** feature branch → PR → independent-model review of the work → Brian merges. Not direct-to-main.
6. **`[skip-wiki-sweep]`** is NOT used on these commits — we *want* the daemon to run on merge to validate the unblock. (The Pass-1 prompt's own propagation commits keep their `[skip-wiki-sweep]` marker as before.)

---

## 6. Acceptance criteria (measurable)

- [ ] Pass 2 text-input estimate **< 950K tokens** (re-run `synthesize.py`'s estimator or the local char/4 proxy on `build_corpus()` output).
- [ ] **No evidence-level tag lost:** for every `(Clinical Trial)/(Animal Model)/(In Vitro)/(Mechanistic Extrapolation)` claim removed from a derivative page, grep-verify the same claim+tag exists on the canonical page (per CLAUDE.md pre-commit grep-verify gate).
- [ ] **No broken anchors:** grep inbound `#anchor` links to every trimmed heading; repoint or keep heading stubs.
- [ ] `wiki/etc/GRAPH.md` nodes/edges intact; `lint-mermaid.py` passes.
- [ ] `validation-experiments.md` retains active experiments + archive link; archive page renders and is corpus-excluded.
- [ ] Two contradictions (§3.4) resolved against primary source.
- [ ] Pass-1 prompt encodes propagate-by-link; stale `wiki/GRAPH.md` path fixed.
- [ ] **Real-world test:** post-merge `wiki-sweep` run completes Pass 1 → 2 → 3, advances the cursor, emits queue items.

---

## 7. Risks & open questions

### Risks
| Risk | Mitigation |
|---|---|
| Evidence-tag loss when trimming derivative pages | Per-claim grep-verify gate before each trim commit |
| Broken inbound anchor links | Grep `<page>.md#<heading>` before deleting headings; keep stubs |
| Over-trimming distinct content | Conservative; honor agents' explicit "keep" lists; per-page audit for A2 |
| `(Source:)` tags left pointing at trimmed stubs | Update or drop now-circular self-citations in the same commit |
| Push a still-too-big corpus → 4th daemon failure | Local token-count gate before merge (§5.4) |
| Pass-1 propagate-by-link under-propagates (misses needed local context) | B2 step 4 reserves full copies for load-bearing local numbers / no-canonical-home cases |
| Daemon re-trigger recursion on the propagation commits | Keep `[skip-wiki-sweep]` on Pass-1's own commits (unchanged) |

### Open questions for Brian / reviewer
1. **A3 scope:** move *all* `### 3.X` self-experiment sections to the archive, or only closed/not-yet-active ones? (Proposed: only closed/not-active.)
2. **B3 guardrail:** enforce propagate-by-link in code (blocking lint in `sweep-1-propagate.py`) or rely on the prompt brief alone? (Proposed: prompt brief now; advisory log-only lint; revisit blocking later.)
3. **A2 aggressiveness:** how hard to trim the next-tier derivative pages — to a strict 1-line-recap, or allow a short paragraph where it aids readability? (Proposed: short recap allowed, ≤3 sentences.)
4. **Canonical-owner ties:** for concepts with two plausible canonical homes (e.g., uricase exposition split across `uricase.md` / `engineered-yeast-uricase-proposal.md` / `crispr-uricase.md`), who owns what? Needs a one-time ownership map (could be a small table in this spec after A2 audits).

---

## 8. Independent-review checklist (for the post-implementation reviewer)

1. **Dedup sanity:** Did any unique content get deleted (not just relocated/linked)? Spot-check 5 random trimmed blocks against their claimed canonical home.
2. **Evidence integrity:** Sample 10 trimmed evidence-tagged claims; confirm each survives with its tag on the canonical page.
3. **Link integrity:** Do all new recap links resolve? Any dangling anchors?
4. **Propagate-by-link sanity:** Read the rewritten Pass-1 step 3. Would it still propagate genuinely-new findings adequately, or does it now *under*-propagate (lose needed local context)? Is the "when a full copy is justified" carve-out clear enough to be followed?
5. **Token math:** Re-derive the Pass 2 prompt estimate from the post-work corpus; confirm < 950K with headroom.
6. **No scope creep:** Confirm sharded synthesis and model-routing were not touched.
7. **Contradiction fixes:** Are the dapansutrile phase and index.md descriptions correct against primary source?

---

## 9. Appendix — measurement commands (reproducible)

```bash
# corpus token proxy (chars/4) for the actual Pass-2 input set
cat wiki/*.md wiki/hypotheses/*.md | wc -c | awk '{printf "%.0fK tokens\n",$1/4/1000}'

# per-page size ranking
for f in wiki/*.md; do printf "%s %s\n" "$(wc -c < "$f")" "$f"; done | sort -rn | head -25

# cross-page provenance density (restatement signature) — see operations script
python3 <provenance-scan>   # paras tagged (Source: other-wiki-page.md), long-block volume

# sweep state + recent runs
python3 scripts/sweep-state.py read
gh run list --workflow=wiki-sweep.yml --limit 8
```
