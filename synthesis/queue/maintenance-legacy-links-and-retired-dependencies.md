---
type: maintenance
priority: after-current-comp-walk
source: user-request-and-comp-014-retirement-audit
---

# Historical links and retired-COMP dependencies

This item belongs at the end of the current COMP-review walk.

## Required actions

1. Re-run the historical-repository link scan. The earlier scan found 61 old
   broken links in untouched legacy logs, specs, and posts; use the new count
   rather than assuming it is still 61. Repair resolvable references without
   rewriting historical scientific conclusions.
2. Correct COMP-016's lifecycle-bound references to invalidated COMP-014:
   COMP-014 cannot support a fungal-ABCG2 frequency claim or serve as
   provenance for the DAE lead. Follow the COMP lifecycle rather than editing
   the artifact outside review.
3. Handle COMP-020's COMP-014 dependency inside the existing
   `comp-review-020.md` action; do not create a second scientific conclusion
   from the retired artifact.
4. Verify that no synthesis-eligible current artifact still treats a retired
   COMP-014 row, count, no-hit, or rank as evidence.

Delete this file when the repairs and checks are complete. Git is the archive.
