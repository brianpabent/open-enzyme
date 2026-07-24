---
title: "C. utilis Uricase Cassette Compatibility — Dual-Cassette Koji Multi-Payload Configuration (Computational, comp-011)"
date: 2026-05-05
tags:
  - computational
  - dual-cassette
  - uricase
  - candida-utilis
  - cyberlindnera-jadinii
  - lactoferrin
  - ward-1995
  - kex2
  - codon-usage
  - aspergillus-oryzae
  - cassette-design
  - endgame-strain
  - koji
  - alln-346
related:
  - cassette-compatibility-computational.md
  - uricase-variant-selection.md
  - computational-experiments.md
  - validation-experiments.md
  - koji-endgame-strain.md
  - hypotheses/H01-ward-dual-cassette.md
  - uricase-protease-stability-computational.md
  - lactoferrin-protease-stability-computational.md
  - lactoferrin.md
sources:
  - "Ward PP, Piddington CS, Cunningham GA, Zhou X, Wyatt RD, Conneely OM. Biotechnology (N Y) 1995;13(5):498-503 (PMID 9634791)"
  - "Huynh HH, Morita N, Sakamoto T, et al. Fungal Biol Biotechnol 2020;7:7 (PMC7257131)"
  - "Rockwell NC, Krysan DJ, Komiyama T, Fuller RS. Chem Rev 2002;102(12):4525-48 (PMID 12475198)"
  - "Brenner C, Fuller RS. Proc Natl Acad Sci 1992;89:922-6 (PMID 1371243)"
  - "US10815461B2 — Allena Pharmaceuticals ALLN-346 C. utilis uricase directed-evolution mutations"
  - "Sands BE et al. Nat Commun 2022 — SEL-212 / pegadricase phase 3 attribution (PMID 35022448)"
status: retired-invalid-model
---

# C. utilis Uricase Cassette Compatibility — Dual-Cassette Koji Multi-Payload Configuration (Computational, comp-011)

The engineering weakness is loss of correct processing, folding, or secretion when a *C. utilis* uricase sequence is adapted to the Ward-style *Aspergillus* cassette. COMP-011 does not establish whether the wild-type or mutation-proxy construct succeeds.

## Current evidence boundary

UniProt P78609 supplies the wild-type *C. utilis* uricase sequence. US10815461B2 supplies a set of disclosed mutations, but the exact clinical ALLN-346 parent sequence was not available in the retired artifact. Ward 1995 supplies an *Aspergillus* secretion precedent (**In Vitro**); it does not validate this construct.

The retired COMP-011 model inferred codon burden without a planned CDS, mixed wild-type P78609 with a synthetic seven-mutation proxy, mis-mapped glycosylation coordinates, transferred KEX2-family preferences, and turned native-unpaired cysteine annotations into categorical folding and secretion-risk claims. Its MODERATE verdict, codon burden, KEX2 certainty, folding/PDI, glycosylation, secretion-capacity, and exact-ALLN-346 interpretations are invalid. The [COMP-011 tombstone](./etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/) is non-runnable.

> **Research conjecture — mutation-dependent junction processing**{ .research-conjecture-label }
>
> **Grounded premises:** Wild-type P78609 (source: UniProt P78609) and the patent-disclosed mutation set (source: US10815461B2) are distinct sequence objects; the Ward secretion study provides an **In Vitro** processing precedent for a different payload (PMID 9634791). The clinical parent and the intended *A. oryzae* CDS remain unverified.
>
> **Novel leap:** One or more disclosed mutations might alter processing or folding in the Ward-style secretion context even if catalytic selection favored the variant elsewhere. No direct study has tested those mutations in the proposed construct.
>
> **Why it matters:** A construct-specific effect could distinguish a sequence problem from a platform problem and prevent an invalid generalization from one variant.
>
> **Discriminating observation:** Define and sequence-verify each construct, then compare wild-type P78609 and the exact mutation proxy for produced termini, intact abundance, folding/assembly, secretion compartment, and retained uricase activity under matched conditions.

The exact clinical ALLN-346 sequence must not be inferred from the patent mutation list. No result here selects a variant, cassette, carrier, tag, or chassis.
