# Spec — Sweep Corpus Unblock (dedup + archive) + Pass-1 Propagate-by-Link

**Date:** 2026-05-29
**Branch:** `corpus-unblock-propagate-by-link`
**Author:** Brian + Claude (Opus 4.8)
**Status:** DRAFT v2 — Codex spec-review incorporated (see §10); pending Brian alignment on Open Questions §7 before implementation
**Reviewers:** (1) external model reviews *this spec* before work begins ✓ Codex round 1 done; (2) independent model reviews *the implemented work* before merge.

---

## 0. TL;DR

The `wiki-sweep` daemon has failed on every run since 2026-05-22 because the Pass 2 (Synthesize) prompt outgrew every model's context window. Root cause is twofold and coupled: (a) the prose corpus crossed ~1.0M tokens *now*, and (b) it keeps self-inflating because Pass 1 (Propagate) copies exposition into related pages instead of linking to a canonical page.

This spec covers three workstreams to be done together on one branch:

- **Workstream A — Corpus unblock (immediate):** deduplicate cross-page restatement and archive the append-heavy `validation-experiments.md`, bringing the Pass 2 prompt back under existing model caps without changing model routing or building sharded synthesis.
- **Workstream B — Propagate-by-link (durable):** change Pass 1's propagation discipline so new findings are written *once* on a canonical page and *linked* from related pages, instead of copied. This stops the corpus self-inflating at the source.
- **Workstream C — Daemon-guard hardening (added in Codex review):** small `synthesize.py` fixes so an overflow fails loudly/pre-flight (no 4× retry on a context-length 400) and the cap guard can't be defeated by a stale constant. (§4b)

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

**Request-growth dynamics (per Codex review #1).** Pass 2 is an *agentic* loop (`MAX_TOOL_ITERATIONS=20` in `synthesize.py`): it starts from the corpus and reads more files via tools as it runs. Run `26362921474` printed an *initial* estimate of `~955,927 tokens (121 files)`, then grew across four tool-use turns to the failing request: **1,017,199 text-input + 245 tool-input + 32,000 reserved output = ~1,049,444**, over the route's 1,048,576 cap. **Implication for the acceptance gate: budget the full request (initial corpus + agentic tool-read growth + output reservation), not just the initial corpus text.** See §4.5.

**Two daemon-guard bugs this exposed (verified in `synthesize.py`, → Workstream C):**
- `CONTEXT_WINDOW_TOKENS` records `google/gemini-2.5-pro: 2_000_000` (line 114), but the live OpenRouter route only granted 1,048,576. The stale constant defeated the pre-flight cap check (line 653), so the overflow wasn't caught before the call. (Codex review #3.)
- The context-length HTTP 400 was treated as a *transient* curl error and retried 4× (retry logic lines ~354–382) instead of hard-failing with a trim/route message. (Codex review #2.)

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
- **Model-routing changes** (e.g., routing Pass 2 to a 2M-context model) — not needed if A succeeds; avoided because routing has a documented mistake history (`synthesize.py` comments). *Note (Codex review #4):* `x-ai/grok-4.20` is currently listed on OpenRouter at a 2M context window and is a plausible **emergency** 2M route — but only after a real API probe through the daemon's OpenRouter path, and it must **not** substitute for Workstream B's durable fix. Kept out of scope here; logged as a fallback option.
- **Editing existing `wiki/etc/**` reference/methodology pages, `reference/*`, `*.html`.** *Clarification (Codex review #6):* the sole permitted `wiki/etc/` write is **creating** the new `wiki/etc/validation-experiments-archive.md` in A3. No existing `wiki/etc/` page is edited.
- **Re-architecting Pass 2 or Pass 3.** (Workstream C touches only Pass-2 *guard* logic — cap constants, 400-classification, pre-flight budget — not the synthesis design.)

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

### A5. Token-math acceptance target (full-request budget, per Codex #1)
The gate is **not** "initial corpus < cap" — it must budget the whole request: `initial corpus + agentic tool-read growth + reserved output`. From run `26362921474`: initial corpus est. ~956K → final text input 1,017K, i.e. **~61K of agentic growth**, plus **32K reserved output** + tool input.

- Current initial corpus: ~911K (`wiki/*.md` proxy) / ~956K (daemon's own est. incl. `wiki/hypotheses/*.md`).
- Reduction: A1+A2 dedup (~28–33K) + A3 archive (~40–50K) = **~68–83K** → **initial corpus ~873–888K (proxy) / ~873–888K daemon-est.**
- **Full-request projection:** ~885K corpus + ~61K agentic growth + 32K output ≈ **~978K**. That clears the **Gemini fallback (1.048M)** with ~70K headroom but is **uncomfortably close to DeepSeek primary (1.000M)** (~22K headroom).
- **Therefore the acceptance bar is: daemon-estimated initial corpus ≤ ~850K**, giving full-request ≈ ~943K and ~57K headroom under DeepSeek primary. If A1+A2+A3 land at the high end of the reduction range (~83K) we hit this; if they land low (~68K) we are ~873K and rely on the Gemini fallback. **The merge gate (§5.4) re-measures the real `build_corpus()` output + a +90K request-overhead allowance and blocks merge if the projected request exceeds 1.000M.** If we cannot get under DeepSeek's 1.0M, the daemon still succeeds via Gemini fallback (≤1.048M) — acceptable, but flag it so the primary isn't silently always-overflowing.

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
- **Primary change:** rewrite step 3 of `scripts/sweep-prompt-1-propagate.md` to encode B2 — replace "insert a fresh subsection" default with "link to canonical + minimal delta" default; add an explicit canonical-ownership determination step; redefine when a full copy is permitted; keep the existing cross-sweep dedup guard. Also soften the existing "don't append 'see also' footnotes" / "err toward more updates" lines, which currently push toward copy-over-link.
- **GRAPH handling — decision-gated (Open Q #5, per Codex review #5).** The Pass-1 prompt references `wiki/GRAPH.md` (stale; it's at `wiki/etc/GRAPH.md` post-reorg). Two options:
  - **(a) Keep + fix:** correct the path to `wiki/etc/GRAPH.md`, verify the `lint-mermaid.py` path, keep graph-maintenance instructions.
  - **(b) Retire (reviewer-recommended):** Brian reportedly never uses the graph and the rendered Mermaid is too small to read. Remove graph-update requirements from `scripts/sweep-prompt-1-propagate.md` **and** `CLAUDE.md`; demote/remove the public links in `index.md` / `README.md`; keep `wiki/etc/GRAPH.md` as an archived artifact (or delete). This also removes per-sweep graph-churn work.
  - **Default pending Brian's ruling: (b).** Either way `wiki/etc/GRAPH.md` is already corpus-excluded, so neither affects the token math.
- **Optional guardrail (Open Q #2):** add a check in `scripts/sweep-1-propagate.py` (or a post-pass lint) that flags when a propagation commit adds more than N lines (proposed N≈8) of new prose to a *non-canonical* page, as a soft signal of copy-instead-of-link. Advisory (log) by default; blocking later.
- **No change** to Pass 2 / Pass 3 synthesis design or model routing. (Pass-2 *guard* fixes live in Workstream C.)

### B4. Acceptance
- A representative test propagation (re-run Pass 1 locally against a sample trigger file, or dry-run) adds links + minimal deltas, not copied exposition blocks.
- Re-running the `(Source:)` provenance scan (`operations/.../scripts/provenance_scan.py`) after a few real sweeps shows the long-block restatement volume **flat or shrinking**, not growing.

---

## 4b. Workstream C — Daemon-guard hardening (from Codex review #1/#2/#3)

Small, contained fixes to `scripts/synthesize.py` so a context overflow fails loudly and the guard can't be defeated by a stale constant. Not a Pass-2 redesign.

### C1. Correct (or probe) the model-cap constants
`CONTEXT_WINDOW_TOKENS` records `google/gemini-2.5-pro` and `gemini-2.5-flash` at `2_000_000`, but the live OpenRouter route granted only `1,048,576`. Either hard-code the **actual route caps** (Gemini 2.5 Pro → `1_048_576`) or add a **live model-cap probe** that reads the route's advertised limit at runtime. Stale caps silently defeat the pre-flight check at line ~653.

### C2. Classify context-length 400 as non-transient
The retry loop (lines ~354–382) retried the context-length 400 four times. Detect `"maximum context length"` / `"requested about"` in a 400 body and **hard-fail immediately** with an actionable message ("Pass-2 prompt exceeds route cap by N tokens; trim corpus or change route"), no sleep-retry. Preserve genuine transient retry (curl transport errors, 429, 5xx).

### C3. Pre-flight full-request budget
Make the pre-flight gate (line ~653) compare `estimated_corpus + reserved_output (32K) + an agentic-growth allowance (~65K, tunable)` against the route cap — not just the corpus estimate — so the daemon refuses to start a doomed call and prints the shortfall.

### C4. Acceptance
- Unit/manual: feeding a corpus that exceeds the route cap causes an immediate, descriptive hard-fail (no 4× retry), and the pre-flight gate blocks before the API call.
- `CONTEXT_WINDOW_TOKENS` matches live route caps (or the probe returns them).

---

## 5. Execution plan

1. **Single branch:** `corpus-unblock-propagate-by-link` (already created).
2. **Order of work:**
   - **C first** (guard hardening) — so that if any later step still leaves the corpus too big, the daemon fails *loudly and pre-flight* instead of burning 21 min + 4 retries. Cheap insurance for the rest of the work.
   - **B next** (rewrite Pass-1 prompt) — so the dedup in A demonstrates the target end-state and we don't immediately re-pollute.
   - **A2 per-page audits** (subagent reads) → then A1+A2 trims, A3 archive, A4 contradiction fixes.
   - Re-run the token-count + provenance scans locally to confirm §4.5 / §A5 target met **before** any push.
3. **Commit discipline:** eager commits, scoped per logical unit (C guard fixes; B prompt change; each dedup cluster; archive-split; contradiction fixes). Hold all pushes per Open Enzyme push-batching rule.
4. **Push/merge gating:** **Do not merge to main until** the §A5 full-request projection (real `build_corpus()` size + ~90K request overhead) is **< 1.000M** (DeepSeek primary) — or, at minimum, < 1.048M (Gemini fallback) with the primary-overflow flagged. Otherwise the post-merge daemon run fails a 4th time. The successful post-merge daemon run is the real-world acceptance test.
5. **PR flow:** feature branch → PR → independent-model review of the work → Brian merges. Not direct-to-main.
6. **`[skip-wiki-sweep]`** is NOT used on these commits — we *want* the daemon to run on merge to validate the unblock. (The Pass-1 prompt's own propagation commits keep their `[skip-wiki-sweep]` marker as before.)

---

## 6. Acceptance criteria (measurable)

- [ ] **Full-request projection < 1.000M** (DeepSeek primary) — real `build_corpus()` size + 32K output + ~65K agentic-growth allowance; or, at minimum, < 1.048M (Gemini fallback) with primary-overflow flagged (§A5).
- [ ] **No evidence-level tag lost:** for every `(Clinical Trial)/(Animal Model)/(In Vitro)/(Mechanistic Extrapolation)` claim removed from a derivative page, grep-verify the same claim+tag exists on the canonical page (per CLAUDE.md pre-commit grep-verify gate).
- [ ] **No broken anchors:** grep inbound `#anchor` links to every trimmed heading; repoint or keep heading stubs.
- [ ] `validation-experiments.md` retains active experiments + archive link; archive page renders and is corpus-excluded.
- [ ] Two contradictions (§3.4) resolved against primary source.
- [ ] Pass-1 prompt encodes propagate-by-link; GRAPH handling resolved per Open Q #5 (path fixed *or* maintenance retired).
- [ ] **Workstream C:** `synthesize.py` hard-fails (no retry) on context-length 400; cap constants match live route (or probe added); pre-flight gate budgets full request.
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
5. **GRAPH retirement (Codex #5):** keep + fix the path (option a), or retire graph-maintenance entirely (option b — reviewer-recommended, Brian reportedly never uses it)? Affects `CLAUDE.md`, `sweep-prompt-1`, `index.md`, `README.md`. **Needs Brian's ruling.** (Proposed: b.)
6. **C1 approach:** hard-code corrected route caps, or add a live model-cap probe? (Proposed: hard-code now — simplest, no extra API call per run — and note the probe as a later robustness upgrade.)
7. **DeepSeek-primary headroom:** if the reductions land low (~68K) and full-request stays ~873K corpus → ~963K request (over DeepSeek's 1.0M but under Gemini's 1.048M), is "succeeds via Gemini fallback, primary always overflows" acceptable for now, or is getting under the DeepSeek primary a hard requirement? (Proposed: acceptable short-term with a flag; B should bend the growth curve regardless.)

---

## 8. Independent-review checklist (for the post-implementation reviewer)

1. **Dedup sanity:** Did any unique content get deleted (not just relocated/linked)? Spot-check 5 random trimmed blocks against their claimed canonical home.
2. **Evidence integrity:** Sample 10 trimmed evidence-tagged claims; confirm each survives with its tag on the canonical page.
3. **Link integrity:** Do all new recap links resolve? Any dangling anchors?
4. **Propagate-by-link sanity:** Read the rewritten Pass-1 step 3. Would it still propagate genuinely-new findings adequately, or does it now *under*-propagate (lose needed local context)? Is the "when a full copy is justified" carve-out clear enough to be followed?
5. **Token math:** Re-derive the Pass 2 prompt estimate from the post-work corpus; confirm < 950K with headroom.
6. **No scope creep:** Confirm sharded synthesis and Pass-2 *synthesis design* were not touched (Workstream C guard fixes are in scope; flag if it went further).
7. **Contradiction fixes:** Are the dapansutrile phase and index.md descriptions correct against primary source?
8. **Guard fixes (Workstream C):** Does `synthesize.py` now hard-fail (no retry) on a context-length 400? Do `CONTEXT_WINDOW_TOKENS` match the live route (or a probe)? Does the pre-flight gate budget the full request (corpus + output + agentic growth)?

---

## 9. Appendix — measurement commands (reproducible)

```bash
# corpus token proxy (chars/4) for the actual Pass-2 input set
cat wiki/*.md wiki/hypotheses/*.md | wc -c | awk '{printf "%.0fK tokens\n",$1/4/1000}'

# per-page size ranking
for f in wiki/*.md; do printf "%s %s\n" "$(wc -c < "$f")" "$f"; done | sort -rn | head -25

# cross-page provenance density (restatement signature) — committed, reproducible
python3 operations/corpus-unblock-propagate-by-link-2026-05-29/scripts/provenance_scan.py
# verbatim-duplication scan (paragraph-level)
python3 operations/corpus-unblock-propagate-by-link-2026-05-29/scripts/dup_scan.py
# TF-IDF page-pair overlap
python3 operations/corpus-unblock-propagate-by-link-2026-05-29/scripts/overlap_scan.py

# sweep state + recent runs (gh needs unsandboxed network in this env)
python3 scripts/sweep-state.py read
gh run list --workflow=wiki-sweep.yml --limit 8
```

The three scan scripts are committed under this operations folder so the §A5 token gate and the §B4 durable-acceptance test (long-block `(Source:)` volume flat/shrinking) are reproducible.

---

## 10. Review log

### 2026-05-29 — Codex independent spec review

**Reviewer:** Codex (GPT-5)

**Status:** Findings to incorporate before implementation.

1. **Pass-2 failure was request-growth, not just initial-corpus size.** Run `26362921474` started with `Corpus: 121 files, ~955,927 tokens (est.)`, then completed four tool-use turns before failing. The failed request was `1,017,199` text-input tokens + `245` tool-input tokens + `32,000` requested output tokens = `~1,049,444`, exceeding the endpoint's `1,048,576` request cap. Implementation implication: the acceptance gate should count input + output budget + tool/conversation growth headroom, not only initial corpus text.

2. **Context-length HTTP 400s should be classified non-transient.** The failed run retried the same invalid request four times after the context-length 400. `scripts/synthesize.py` should detect "maximum context length" / "requested about" 400 responses and hard-fail immediately with a trim/routing message, not sleep-and-retry.

3. **Model-cap table needs live-route verification.** DeepSeek V4-Pro remains the Pass-2 primary; Gemini is only fallback. However, the route used by the daemon exposed a `1,048,576` cap for `google/gemini-2.5-pro`, while `scripts/synthesize.py` still records Gemini Pro as `2_000_000`. Before implementation, update `CONTEXT_WINDOW_TOKENS` to match the actual OpenRouter/API route, or add a live model-cap probe so the guard does not rely on stale constants.

4. **Grok 4.20 may be a 2M-context emergency route.** OpenRouter currently lists `x-ai/grok-4.20` with a 2M context window, and Oracle's xAI Grok 4.20 docs also describe a 2M-token combined prompt+response budget. xAI's own model docs may differ by route/version. Treat Grok 4.20 as a model-routing investigation or emergency fallback only after a real API probe through the daemon's OpenRouter path; do not let it replace Workstream B's durable propagate-by-link fix.

5. **`wiki/etc/GRAPH.md` is not load-bearing and should probably stop being maintained.** Git history shows `wiki/GRAPH.md` was added in the initial commit (`2e0e3ee`, 2026-04-21), then repeatedly updated by sweep propagation, then moved to `wiki/etc/GRAPH.md` in `8653de9` (2026-05-15) as a synthesis-excluded reference page. Brian has never used it, and the rendered Mermaid graph is too small to read. Replace B3's "fix stale graph path" with "remove or demote graph-maintenance instructions" unless Brian explicitly wants to keep it. Candidate actions: remove graph-update requirements from `CLAUDE.md` and `scripts/sweep-prompt-1-propagate.md`; remove/demote public links in `index.md` / `README.md`; keep `wiki/etc/GRAPH.md` as archived artifact or delete it.

6. **A3 conflicts with the stated `wiki/etc/**` non-goal.** §2 says not to touch `wiki/etc/**`, while A3 requires creating `wiki/etc/validation-experiments-archive.md`. Clarify that the non-goal is "do not edit existing reference/methodology pages under `wiki/etc/` except for the new archive file explicitly created by A3."

7. **The provenance-scan gate is not reproducible yet.** §9 lists `python3 <provenance-scan>`, but no script is named or committed in this spec directory. Since the durable acceptance test depends on long-block `(Source:)` restatement volume staying flat/shrinking, either commit the scan script or replace the placeholder with the exact command used for the audit.

---

### 2026-05-29 — Disposition of Codex review (Claude, Opus 4.8)

All 7 findings verified and incorporated. Two code claims (#2, #3) were checked against `synthesize.py` and confirmed accurate (`CONTEXT_WINDOW_TOKENS["google/gemini-2.5-pro"] = 2_000_000` at line 114; transient-retry loop at lines ~354–382 caught the 400). Changes:

1. **Request-growth gate** → new "Request-growth dynamics" note in §1.2; §A5 rewritten to budget *initial corpus + ~65K agentic growth + 32K output* against the cap; acceptance bar tightened to **daemon-est. corpus ≤ ~850K** (full-request ≈943K, ~57K under DeepSeek primary). §6 + §5.4 updated to the full-request projection.
2. **Hard-fail on context-length 400** → **Workstream C2** (new §4b): detect `"maximum context length"`/`"requested about"` 400 → immediate descriptive hard-fail, preserve genuine transient retry.
3. **Stale model caps** → **Workstream C1**: correct `CONTEXT_WINDOW_TOKENS` to live route caps (Gemini 2.5 Pro → 1,048,576) or add a probe. Open Q #6 picks the approach.
4. **Grok 4.20 2M emergency route** → noted in §2 Non-goals as an out-of-scope emergency fallback, probe-gated, must not replace Workstream B.
5. **GRAPH retirement** → B3 rewritten as decision-gated (keep+fix vs retire); **Open Q #5** added, default = retire (reviewer-recommended). Removed the unconditional "GRAPH nodes intact" acceptance item.
6. **A3 vs `wiki/etc/` non-goal conflict** → §2 reworded: only permitted `wiki/etc/` write is *creating* the new archive file.
7. **Provenance scan reproducibility** → the three scan scripts (`provenance_scan.py`, `dup_scan.py`, `overlap_scan.py`) committed under `operations/.../scripts/`; §9 placeholders replaced with real paths.

New decisions surfaced for Brian: Open Q #5 (GRAPH retire — needs ruling), #6 (cap-fix vs probe), #7 (is Gemini-fallback-only acceptable if reductions land low). Scope grew by one workstream (C, daemon-guard hardening); still no sharding, no synthesis-design or routing changes.
