---
type: connection
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 3
global_index: 3
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# The 7.5× Km misreport in `paperclip-deep-dive.md` — caught by a cross-vendor review nine days after it entered the corpus — is a live-fire demonstration that the multi-model sweep daemon catches errors that a single-vendor pipeline would miss, and it strengthens the case for the pre-commit grep-verify gate.

3. **The 7.5× Km misreport in `paperclip-deep-dive.md` — caught by a cross-vendor review nine days after it entered the corpus — is a live-fire demonstration that the multi-model sweep daemon catches errors that a single-vendor pipeline would miss, and it strengthens the case for the pre-commit grep-verify gate.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `wiki/paperclip-deep-dive.md`, `wiki/manual-literature-mining.md`, `wiki/open-source-platform.md`
   - *Page-pair linkage:* `paperclip-deep-dive.md` already cross-references `manual-literature-mining.md` (the pre-commit verification gate) and `open-source-platform.md` (multi-model synthesis). But the specific narrative — an error propagating from a wiki page into an external paper draft, then being caught by a cross-vendor Pass 4 review — is not yet documented as a **case study for the architecture’s value**.
   - *Why It Matters:* The DAF SCR1-4 disulfide-count incident (2026-05-06) was the canonical case for the pre-commit grep-verify gate. The Paperclip Km incident (2026-05-13) is the canonical case for the **cross-vendor review catching errors that escape single-model generation**. The error survived nine days in the corpus, propagated into a paper draft, and was caught by DeepSeek V4-Pro reviewing the draft — exactly the heterogeneity-guard pattern the architecture was designed for. Documenting this as a named case study (alongside the DAF incident) in `open-source-platform.md` §“Multi-model synthesis” gives the architecture a concrete, grep-verifiable success story. It also reinforces the discipline that *every* load-bearing number must pass the grep-verify gate before shipping — the Paperclip error would have been caught at write-time if the gate had been applied.
   - *Suggested Action:* Add a “Case study: Paperclip Km error (2026-05-13)” paragraph to `open-source-platform.md` §“Multi-model synthesis as guard against epistemic homogenization,” directly after the existing DAF SCR1-4 incident reference. Cross-link to `paperclip-deep-dive.md` and `manual-literature-mining.md`.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` This is a useful case-study framing. `paperclip-deep-dive.md` documents the corrected Najjari/Paperclip Km factor as 7.5× rather than 7,500×, says the error propagated into the cross-vendor heterogeneity-guard paper draft, and states that DeepSeek V4-Pro caught it on 2026-05-13; `manual-literature-mining.md` independently codifies the pre-commit grep-verify gate and names the DAF SCR1-4 incident as the prior canonical example. `open-source-platform.md` already mentions the Paperclip correction in the Paperclip subsection, but not as a named multi-model architecture case study alongside the DAF incident, so the suggested placement is additive.
