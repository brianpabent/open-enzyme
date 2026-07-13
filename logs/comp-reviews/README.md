# Independent comp reviews

One immutable review log per changed `comp-NNN` artifact, written by
`.github/workflows/comp-review.yml` through `scripts/comp-review.py`.

The normal wiki sweep reads the short interpretive pages under `wiki/` but
does not inline `wiki/etc/experiments/`. These logs are the audit trail for
the complementary artifact-level review of code, inputs, outputs, summary
fidelity, constraint closure, and affected wiki pages.

Clean reviews write only a log. Reviews requiring action also emit one
`type: comp-review` item to `synthesis/queue/` for the normal walkthrough and
closure flow.

Filename:

```text
YYYY-MM-DD-comp-NNN-<trigger-sha7>.md
```
