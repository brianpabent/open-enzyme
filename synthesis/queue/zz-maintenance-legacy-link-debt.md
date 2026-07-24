---
type: maintenance
scope: legacy-link-debt
priority: last
observed_count: 61
---

# Clear legacy broken-link debt

## Why action remains open

The full repository link audit reports 61 broken relative links in untouched legacy logs, specifications, operations pages, paper notes, and posts. The maintenance batch that exposed them did not introduce them, and all surfaces changed in that batch are link-clean.

## Required action

Review the affected files as a separate final maintenance pass:

1. Repair links when a current canonical target exists.
2. Delete obsolete narrative artifacts when they have no unique current value; Git is the archive.
3. Convert intentional examples or non-link bracketed prose so the checker does not misread them.
4. Do not recreate deleted queue or synthesis-history files merely to satisfy a link.

Verification criterion: `python3 scripts/check-links.py` reports zero broken relative links across the full repository. Delete this queue file in the same commit.
