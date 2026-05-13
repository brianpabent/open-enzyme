# papers/

Paper drafts produced by Open Enzyme, with primary-source links into the wiki and operational logs that justify each claim.

Each paper lives in its own subdirectory:

- `cross-vendor-heterogeneity-guard/` — Paper #1. Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted scientific literature synthesis. Methodology paper; uses Open Enzyme's own sweep daemon as the case study.

## Drafting conventions

- **Single author (Brian Abent), with explicit AI-tools disclosure** in the methods section per current journal norms.
- **Voice: academic-formal, plain prose around precise terms.** Every load-bearing technical term gets a parenthetical gloss on first use. The running glossary in each paper's `glossary.md` is the authoritative term list.
- **Quality gate:** if Brian cannot explain a sentence back to me in his own words, the sentence is wrong and gets rewritten. Ghost-written PhD jargon is a failure mode.
- **Citations from wiki primary sources** wherever possible. Wiki citations link via relative paths; external citations follow venue conventions.

## Workflow

1. Draft sections in `draft.md`. Outline lives at `outline.md`. Term glossary at `glossary.md`.
2. After each substantive section lands, run an independent-vendor review pass (Gemini or DeepSeek) and log catches in `revisions.md`.
3. When the manuscript reaches preprint quality: post to bioRxiv first (zero gating, citable artifact), then submit to target venue.
4. The drafting process for Paper #1 specifically eats its own dog food — multi-vendor review at section boundaries, logged in `revisions.md`, summarized in the paper's own methods appendix.
