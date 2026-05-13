# Submission checklist

Path from "current draft state" to "bioRxiv preprint live + manuscript submitted to *Patterns*." Step order matters where dependencies are noted; otherwise can be parallelized.

---

## Pre-submission content work

### Drafting completion

- [ ] **§2 Related work** drafted by PaperOrchestra per `paperorchestra-handoff.md` brief
- [ ] §2 cross-vendor reviewed by Claude + DeepSeek per `review-prompts.md` Prompt 3
- [ ] §2 catches applied to draft, logged in `revisions.md`
- [ ] **Abstract** drafted last, ~250 words, summarizes problem + contribution + demonstration + reflexive note
- [ ] Cross-vendor review of abstract by DeepSeek (single pass; abstract is short enough that one independent review is sufficient)

### Cross-vendor review passes on existing sections

- [ ] **Gemini 2.5 Pro review** of §3 + §6 + §7 per `review-prompts.md` Prompt 2
- [ ] **DeepSeek V4-Pro review** of §4 + §5 per `review-prompts.md` Prompt 1
- [ ] Review catches applied; `revisions.md` updated; Appendix A vendor-attribution table filled in

### Author-side review

- [ ] Brian's glossary-check pass — every term in `draft.md` either in `glossary.md` with an understandable gloss, or rewritten
- [ ] Brian's "explain this sentence back in your own words" pass on §4 and §5 specifically (the conceptual spine and concrete demonstrations)
- [ ] Brian's confirmation of the three open questions in `revisions.md` Session 1 (author byline format, vendor naming, reflexive-Methods-Appendix entry)

---

## Figures and tables

- [ ] **Figure 1: Architecture diagram.** Three operational passes (Sonnet → DeepSeek/Gemini → Opus/GPT-5.5) with the inter-pass artifact handoffs (`propagated_files`, `cited_files`). Episodic peer-review pattern shown as a separate dashed-line component. Vendor colors distinguish the cross-vendor pattern visually. PaperOrchestra can generate this from §3 text.
- [ ] **Figure 2: Catches by failure class.** Four bar segments representing the four case-study classes (§5.1 within-vendor cascade, §5.2 upstream contamination, §5.3 external-tool unreliability, §5.4 cross-vendor methodological). Could be a single bar with the catches color-coded, or a horizontal bar chart. Honest framing: N=1 per class; this is qualitative.
- [ ] **Table 1: Per-pass model assignment + cost + latency.** From §6 operational data. Pass / Model / Vendor / Typical cost / Typical latency / Token budget.
- [ ] **Table 2: Cross-vendor production process attribution.** From Appendix A. Section / Primary drafter / Independent reviewer / Catches logged.

---

## Code and data preparation

- [ ] **Snapshot the Open Enzyme repo** at the submission-time commit. Cite the commit SHA in Appendix C.
- [ ] **Zenodo DOI** for the snapshot. Generate via Zenodo's GitHub integration on the snapshot commit; cite the DOI in Appendix C and in the bibliography.
- [ ] **Sample synthesis log** for supplementary materials — pick one representative `logs/v4-synthesis-*.md` log that shows the synthesis discipline cleanly. Anonymize if needed.
- [ ] **Sample peer-review log** for supplementary materials — `logs/v4-peer-review-2026-04-25-deepseek.md` is the seminal case-study artifact; include it verbatim as supplementary material with a brief framing note.
- [ ] **GitHub Actions workflow file** — `.github/workflows/wiki-sweep.yml` — included as supplementary material so reviewers can verify the architectural claims in §3.

---

## Pre-submission integrity passes

- [ ] **Primary-source verification pass** — re-grep every load-bearing quantitative or identity claim in the final manuscript against its named primary source. Same discipline as the comp-NNN wiki authoring protocol.
- [ ] **Citation completeness check** — every numbered reference [N] in the body has a matching entry in References; every reference in References is cited at least once.
- [ ] **Glossary completeness check** — every precise term in `glossary.md` is used somewhere in the manuscript; every precise term in the manuscript that's not common knowledge is in the glossary.
- [ ] **Reflexive narrative preserved** — Methods Appendix entry on the Catch 1 PaperOrchestra confabulation is intact. This is load-bearing for the paper's argument.

---

## Submission to bioRxiv

- [ ] Convert final draft to PDF (PaperOrchestra produces LaTeX; render to PDF).
- [ ] Prepare bioRxiv-compatible figure files (PNG or PDF, sufficient resolution).
- [ ] bioRxiv submission portal: select category "Synthetic Biology" or "Bioinformatics" depending on framing — recommend "Bioinformatics" given the AI-methods focus.
- [ ] Cross-post to arXiv cs.AI on the same day for the ML audience.
- [ ] Update `paper-1-status.md` (or equivalent tracking doc) with the bioRxiv DOI once live.
- [ ] Update Open Enzyme `index.md` with a link to the preprint.

---

## Submission to *Patterns* (Cell Press)

After the bioRxiv preprint lands and any community feedback has been digested:

- [ ] Read *Patterns* author guidelines; format manuscript and references per their style.
- [ ] Prepare cover letter — emphasize the cross-vendor pattern's novelty relative to existing multi-agent literature, the operational deployment as evidence the pattern works, and the reflexive Methods Appendix.
- [ ] Identify suggested reviewers and any conflicts to flag.
- [ ] Submit via the Cell Press portal.
- [ ] Response loop on reviewer comments — apply the same cross-vendor review discipline to any substantive rewrites required by peer review.

---

## Backup venues if *Patterns* rejects

- [ ] *Nature Computational Science* — stretch target; higher bar but the cross-vendor framing fits.
- [ ] *PLOS Computational Biology* — open-access fallback; high publication rate; aligned with the open-source ethos of the Open Enzyme project.
- [ ] *Bioinformatics* (OUP) — narrower fit (more bench-bio tools than AI methodology), but plausible.

---

## What "done" looks like

1. bioRxiv preprint live at a citable DOI, with code/logs in Zenodo at a citable DOI.
2. arXiv cs.AI mirror live.
3. Manuscript under peer review at *Patterns* or successor venue.
4. Updated Open Enzyme `index.md` and `paper-1-status.md` reflect the published state.
5. Outreach material (grad-student / CC wet-lab path; potential collaborators) updated with the citable preprint as the credibility artifact.
