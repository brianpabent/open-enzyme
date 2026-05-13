# Paper #1, Cross-vendor heterogeneity guard

**Working title:** *Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted scientific literature synthesis.*

**Author:** Brian Abent (Open Enzyme · brian@headsupresults.com). Single author.

**Status (2026-05-13):** Solo-draftable work complete. Manuscript has Abstract, §1–§9, Methods Appendix, Appendix A (vendor attribution), Table 1, Figures 1–2, and an 11-citation S2-verified bibliography. Pending: cross-vendor external review passes (Brian fires the prompts in `review-prompts.md`), then bioRxiv preprint submission per `submission-checklist.md`.

## Where things live

| File / dir | What it is |
|---|---|
| **`draft.md`** | The manuscript. Read this first. |
| `outline.md` | Section-by-section scope, target venues, completion checklist |
| `glossary.md` | Plain-English glosses for every precise term in the manuscript. Brian's review-handle for "do I understand this sentence?" |
| `revisions.md` | Chronological catches log across all drafting sessions. Becomes Appendix B of the final paper. 8 catches landed so far. |
| `review-prompts.md` | Three ready-to-fire cross-vendor review prompts (DeepSeek on §4/§5, Gemini on §3/§6/§7, parallel review of §2). Copy-paste-and-fire at the model's chat interface. |
| `submission-checklist.md` | Step-by-step path from current draft state to bioRxiv preprint live + Patterns submission. |
| `paperorchestra-handoff.md` | Self-contained brief for handing the manuscript to PaperOrchestra. Now historical context, §2 has already been drafted via the Ar9av/PaperOrchestra Path B install. |
| **`figures/`** | Self-rendering matplotlib scripts for Figures 1 and 2, plus PDF/PNG outputs. See `figures/README.md` for rebuild commands. |
| **`paperorchestra-workspace/`** | The Ar9av/PaperOrchestra workspace used to draft §2. Inputs (idea, exp log, conference guidelines, template), outline.json, BibTeX (refs.bib), S2-verified citation pool, LaTeX section output, and the verification audit. See workspace's own `drafts/verification-audit.md` for the complete provenance trail on §2 citations. |

## How drafting proceeded

| Session | Date | What landed |
|---|---|---|
| 1 | 2026-05-13 | outline, glossary, §4 + §5 (four case-study vignettes) |
| 2 | 2026-05-13 | §3 + §6 + §7 + §8 + §9, Methods Appendix, Appendix A skeleton, PaperOrchestra handoff packet |
| 3 | 2026-05-13 | §1, cross-vendor review prompts, submission checklist |
| 4 | 2026-05-13 | §2 via Ar9av/PaperOrchestra Path B (11 citations, S2 verification gap during rate-limit) |
| 5 | 2026-05-13 | Abstract, Table 1, glossary additions, drafter self-verify (Catches 7 + 8 landed) |
| 5.5 | 2026-05-13 | S2 API key arrived same day, all 11 citations upgraded to S2-verified |
| 6 | 2026-05-13 | Figure 1 (architecture) and Figure 2 (catches-by-class) rendered, wired into draft, Appendix A populated, structure audit |

## What remains

**Solo work (no Brian needed):** essentially done. Any further polish should be informed by the cross-vendor review catches rather than further self-edits at this point.

**Brian-required, in order:**
1. Fire `review-prompts.md` Prompt 1 (DeepSeek on §4/§5)
2. Fire `review-prompts.md` Prompt 2 (Gemini on §3/§6/§7)
3. Fire `review-prompts.md` Prompt 3 (Claude + DeepSeek parallel on §2)
4. Land review catches into `revisions.md`, apply corrections to `draft.md`
5. Glossary check + "explain this sentence back" pass on §4/§5
6. Confirm decisions in `revisions.md` Session 1 (author byline, vendor naming, reflexive-narrative entry)
7. Zenodo snapshot + bioRxiv submission per `submission-checklist.md`

After bioRxiv: prepare *Patterns* (Cell Press) submission per the checklist.

## How to rebuild artifacts

```bash
# Figures
cd figures
python3 figure1_architecture.py
python3 figure2_catches.py

# §2 BibTeX (re-runs S2 verification with the key in ~/.config/abent/paperorchestra.env)
cd ../paperorchestra-workspace
source ~/.config/abent/paperorchestra.env
python3 run_verify.py
python3 build_bib.py
```

## Why this paper exists

Open Enzyme's `wiki/open-source-platform.md` introduces the cross-vendor heterogeneity-guard pattern operationally; this paper formalizes it as an explicit architectural commitment and presents it as a publishable methodology contribution. The strategic frame: a published methodology paper is the credibility artifact that converts cold grad-student / wet-lab outreach into warm collaborative conversations (see [`project_oe_methodology_paper`](memory entry) and [`project_oe_wet_lab_search`](memory entry)). The reflexive twist, the paper is drafted using its own methodology, with self-catches logged as Appendix B, is the central argument.
