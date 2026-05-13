# Submission Guidelines — bioRxiv preprint + Patterns (Cell Press)

This paper is targeted for bioRxiv preprint posting followed by submission
to *Patterns* (Cell Press). Guidelines below reflect both targets.

## Submission deadline

This is a continuous-rolling submission, not a fixed venue deadline. For
the Literature Review Agent's `cutoff_date` derivation: target **research
cutoff date = 2026-05-01** (one month before manuscript completion target
of 2026-06-01). Papers published after 2026-05-01 may be cited only as
concurrent work, never as prior baselines.

## Page limit

*Patterns* main manuscript: typically 6,000–8,000 words excluding references
and figures. Target ~7,500 words for this paper.

## Mandatory sections

The submission contains, in this order:

1. Abstract (single paragraph, ~250 words)
2. Introduction
3. Related Work
4. Architecture (the system being described)
5. Heterogeneity-guard rationale
6. Case studies
7. Operational data
8. Limitations and failure modes
9. Discussion
10. Conclusion
11. Methods Appendix (cross-vendor production process used for the paper)
12. References

## Formatting rules

- Single-column, 11pt font
- Standard `\documentclass{article}` template
- Citations via natbib; use `\cite{...}` commands
- Figures saved at 300 DPI minimum
- Tables use the booktabs package
- Author byline: single author "Brian Abent" with affiliation "Open Enzyme"

## Topic scope

The paper is methodology — multi-agent AI architecture, scientific
literature synthesis, and the cross-vendor heterogeneity guard against
epistemic homogenization in AI-assisted research workflows.

## Review criteria

Reviewers will assess: novelty of the cross-vendor framing relative to
existing multi-agent literature, rigor of the case studies, operational
data substantiating the claims, honesty about limitations and failure
modes, and reproducibility (code and logs are openly published in the
Open Enzyme GitHub repository).

## What makes this paper unusual

The manuscript is drafted using the methodology it describes — cross-vendor
review applied at section boundaries during drafting, with catches logged
in a revisions appendix that becomes Appendix B of the final paper. This
reflexive structure is a load-bearing argument in the paper itself.
