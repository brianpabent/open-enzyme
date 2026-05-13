# Experimental Log

The "experimental" record for this methodology paper is the **operational
record of the Open Enzyme wiki-sweep daemon** during its first ~3 weeks of
production use (2026-04-21 through 2026-05-13). Each catch below is a real
incident from the operational logs.

## 1. System Setup

* **Substrate corpus:** Open Enzyme research wiki — ~80 long-form Markdown
  pages on engineered food-grade fungal strains for therapeutic enzyme
  production, plus a Mermaid concept graph and a cross-reference network.
* **Trigger mechanism:** GitHub Actions workflow `wiki-sweep.yml` fires on
  every push that touches `wiki/*.md`.
* **Pass orchestration:** OpenRouter HTTP gateway routes successive passes
  to different vendors' frontier models. Three operational passes plus an
  episodic peer-review pass.
* **State persistence:** `logs/sweep-state.json` records the last successful
  sweep commit, pending paths, and recent failures. Atomic-write at Pass 3
  success.
* **Operational hardening:** Rebase-before-push to handle concurrent commits;
  retry-with-backoff on OpenRouter HTTP 5xx; `failed-sweep-<sha>.md` ledger
  uploaded as a workflow artifact so failure traces survive runner teardown.

## 2. Three Operational Passes (current model assignment)

| Pass | Role | Model | Vendor |
|---|---|---|---|
| 1 | Propagate | Claude Sonnet 4.6 | Anthropic |
| 2 | Synthesize | DeepSeek V4-Pro (primary), Gemini 2.5 Pro (fallback) | DeepSeek / Google |
| 3 | Review | GPT-5.5 (default since 2026-05-08; Claude Opus 4.7 alternate) | OpenAI / Anthropic |
| Peer-review (episodic) | Independent cross-vendor verification | DeepSeek V4-Pro | DeepSeek |

## 3. Cost and Latency Measurements

* **Pass 2 single sweep (Gemini 2.5 Pro, 2026-04-28):** $0.7288 OpenRouter
  cost; 62 lines of synthesis output.
* **DeepSeek V4-Pro peer-review pass (2026-04-25):** $0.2070 OpenRouter
  cost; 467,964 input tokens; 4,005 output tokens.
* **End-to-end three-pass sweep latency:** 9–12 minutes typical. Pass 2
  dominates (5–7 minutes for full-corpus read).
* **Monthly operational cost:** low tens of dollars during normal use.

## 4. Four Representative Catches

### Catch 1 — Within-vendor cascade (DAF SCR1-4 disulfide-count, 2026-05-06)

A Sonnet subagent authoring a computational analysis page for a complement
regulator protein (human DAF/CD55) asserted "3 conserved disulfide bonds
per SCR domain → 12 total for SCR1-4" in four separate places of prose
narrative. The number was hallucinated — the analysis pipeline (AlphaFold
pLDDT-based protease stability scoring) does not compute disulfides at all;
its Limitations section explicitly states "Disulfide bonds not modelled."

The error propagated overnight: Pass 1 of the next-morning sweep incorporated
the "12 disulfides" figure into the H05 hypothesis card. Downstream synthesis
used it as input to a chaperone-orthogonal stacking calculation, producing a
panic over a fabricated "17+12=29 disulfides" triple-cassette total.

The catch came from a combination of the next-day sweep and a manual
walkthrough verification against the canonical UniProt P08174 record, which
has exactly 8 DISULFID feature annotations across SCR1-4 (canonical sushi/
CCP fold, 2 disulfides per domain — well-established complement biology).

This catch motivated a pre-commit grep-verify gate: every load-bearing
quantitative claim in newly-authored content must be checked against its
primary source before the commit lands.

### Catch 2 — Upstream-of-subagent contamination (comp-018 framing bias, 2026-05-08)

A comp-018 subagent was launched to perform a literature scan of upstream
complement-cascade modulators. The brief composed for the subagent included
a contrived example from a casual user message: "if it's rosemary I'll grow
rosemary." The framing was meant to illustrate the kind of finding that
would be useful — a specific, growable, dietary modulator — but landed
verbatim in the subagent's instructions.

The subagent's output prioritized rosmarinic acid (a polyphenol abundant in
rosemary) as a Tier-1 finding. The subagent's report-back literally said
"Brian's literal 'if it's in rosemary I'll grow rosemary' framing landed
empirically" — the rhetorical-callback tell that signaled framing
contamination.

The catch came from comp-020, a verification rerun with the contaminated
framing stripped. The clean rerun found three tied tier-1 candidates instead
of one (rosmarinic acid, *Helicteres* benzofuran lignans, luteolin); the
original comp-018 had missed *Helicteres* lignans entirely despite their
4-20× greater potency on matched assay.

This catch motivated a "subagent brief hygiene" discipline: scope and
method propagate from user direction into briefs; contrived examples and
motivational framings must be stripped.

### Catch 3 — External-tool reliability test (Paperclip MCP probe, 2026-05-05)

A candidate external tool (Paperclip MCP, exposing ~11M full-text scientific
papers via a unified query interface) was evaluated for integration into the
sweep daemon as a "literature delta" surface. Verification probe: 12 papers
from the uricase variant landscape (a domain with hand-curated ground truths
for organism identity, kinetic parameters, and experimental modality) were
queried via Paperclip's `map` synthesis primitive.

Three failure classes surfaced. (a) Wrong organism identity: papers on
*A. flavus* uricase were repeatedly attributed to *A. globiformis*.
(b) Fabricated kinetic parameters: for the Najjari 2022 PASylated uricase
paper, the true Km is 52.61 µM; Paperclip's `map` returned 0.007 mM — off by
approximately 7,500-fold. (c) Invented wet-lab data for purely computational
papers.

Decision: do not integrate. Wiring `map` into the sweep would inject a
structured external hallucination source into a corpus designed for rigor —
exactly the failure mode the heterogeneity guard is meant to prevent.

### Catch 4 — Cross-vendor catches methodological risk (DeepSeek Connection 7, 2026-04-25)

Prior to 2026-04-25, Open Enzyme sweep work was driven primarily by a single
Claude Opus 4.7 local session — both propagation and synthesis through the
same model, no formal multi-pass daemon. On 2026-04-25, DeepSeek V4-Pro was
run as an independent peer-review pass on that substrate.

DeepSeek's Connection 7 in that peer-review log observed: "The 'DeepSeek V4
Assessment' inadvertently highlights a risk of epistemic homogenization in
the sweep process. […] If a single model (even a frontier one) becomes the
sole source of synthesis, the project's knowledge graph could converge on
that model's blind spots and biases. […] The value of this corpus is that
it can be interrogated by multiple AI systems with different reasoning
architectures, creating a form of 'adversarial collaboration.'"

This was a routine peer-review finding among several Connections — not
flagged with special urgency. But it named a structural risk that the
Claude-driven session had not surfaced across previous edits, despite Claude
having authored both the synthesis content and the prior self-reviews. The
within-vendor pipeline could not see the within-vendor blind spot. A
different vendor named it on the first pass.

This catch was the seminal motivating observation for the cross-vendor
daemon architecture itself: the three operational passes deliberately
assigned across Anthropic / DeepSeek / Google / OpenAI vendors so that no
single vendor's prior could dominate the corpus's evolution.

## 5. Failure modes observed and architectural response

### Push-race failure (Run 25051936845, 2026-04-28)

Pass 1 propagated and pushed successfully. Pass 2 ran fully and produced a
synthesis log locally on the runner. The runner's push attempt was rejected
because a concurrent commit (from Pass 1 of a parallel sweep) had landed on
`main`. Pass 3 never ran. The synthesis artifact was lost when the runner
tore down.

**Architectural response:** rebase-before-push in every pass after Pass 1;
failure ledger uploaded as a workflow artifact so traces survive runner
teardown.

### API outage failure (Run 25049501442, 2026-04-28)

Pass 1's OpenRouter call returned HTTP 503 (transient upstream outage). The
shell wrapper exited non-zero on the first failed `curl`. No retry. The
sweep terminated.

**Architectural response:** retry-with-backoff (5s / 15s / 45s) wrapping
every OpenRouter call; HTTP 5xx and curl exit codes 6/7/22/28 treated as
retryable; HTTP 4xx treated as fatal.

### Inter-pass information loss

A third failure class — Pass 3 admitting it could not verify a Pass 2
citation because the cited file was outside the trigger set — motivated
explicit inter-pass artifact handoff. Pass 1 emits a `propagated_files`
list; Pass 2 receives both `trigger_files` and `propagated_files` plus
emits a `cited_files` manifest; Pass 3 receives the synthesis log plus
both file lists inlined as a "warm cache," with read-only tools for
on-demand fetches.

## 6. Distribution of Catches by Class

Across the 13-day operational window 2026-04-25 to 2026-05-08, the four
case studies above are representative of four distinct failure classes.
The first three (§5.1, §5.2, §5.3) each surfaced exactly one instance
during the window. The fourth (§5.4) is the seminal cross-vendor catch
that motivated the entire architecture.

The operational data does not yet support a quantitative false-positive
rate estimate — the production daemon has not flagged enough findings
during the window to compute one with confidence. A more rigorous false-
positive analysis is queued as future work once the operational record
extends to ~6 months.
