---
type: priority-action
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 1
global_index: 10
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# Add the Ginkgo $39 cell-free pre-gate as an optional pre-screen in `validation-experiments.md` §1.1 (Uricase gene performance comparison).

1. **Add the Ginkgo $39 cell-free pre-gate as an optional pre-screen in `validation-experiments.md` §1.1 (Uricase gene performance comparison).** The experiment queue currently lists the full gene-synthesis + transformation pipeline at $2,000–3,000. A one-sentence addition noting that a $39 cell-free run can serve as a fail-fast pre-gate (for uricase variants specifically) would save $2,000+ on any variant that fails at the translation/folding step. The Ginkgo page already makes the case; the validation-experiments page should operationalize it.

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` This priority action is stale: `validation-experiments.md` §1.1 already operationalizes the Ginkgo pre-gate as a named option, including the $39/protein price, ~5–10 day turnaround, lead-variant target, and negative/positive decision consequences. The actionable item should be changed from "add this to §1.1" to "execute the already-queued §1.1 pre-gate and clarify whether Ginkgo bundles uricase activity readout or only expression/solubility."

---

## ✓ Already actioned 2026-05-15 (closure note — doubly stale)

Pure closure. No new wiki work. Two reasons this priority action is closed:

1. **Pass 3 was right** that `validation-experiments.md` §1.1 already had the Ginkgo cell-free pre-gate as a named option (line 102). The "add this to §1.1" framing was stale at sweep time.
2. **And it's now further stale** per Items 8 + 9 (this same walk): the 2026-05-13 priority-stack decision to skip the $39 cell-free path lifted the pre-gate option from "recommended" to "deferred." Pass 3's suggested re-framing ("execute the already-queued §1.1 pre-gate") is also no longer the right move — we explicitly decided to *not* execute it for now.

Canonical state:
- `wiki/ginkgo-cloud-lab-evaluation.md` TL;DR — "Decision (2026-05-13): skip the $39 cell-free for now" + computational-corpus rationale
- `wiki/validation-experiments.md` §1.1 line 102 — pre-gate option marked "(deferred 2026-05-13)" with revisit trigger
- The now-prioritized comp-NNN on the compounding-pharmacy / repurposing track is **comp-027** (disulfiram dose modeling), queued in Planned Analyses; that's gated on different work (off-label dose modeling), not Ginkgo cell-free.

Closing. No further wiki touch needed.
