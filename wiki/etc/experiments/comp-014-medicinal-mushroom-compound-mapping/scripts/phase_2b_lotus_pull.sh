#!/bin/bash
# Phase 2b: Pull fungal compounds from LOTUS REST API.
#
# Iterates a list of fungal genera and species, queries LOTUS search/simple,
# caches raw responses in outputs/_lotus_raw/. Run aggregate_lotus.py after
# to deduplicate and produce the canonical compound × species table.
#
# Notes:
# - LOTUS REST API endpoint is https://lotus.naturalproducts.net/api/search/simple
# - The response includes compound metadata (InChIKey, SMILES, MW, etc.)
#   but does NOT directly attach organism attribution per compound — we
#   attribute by the query name (recorded as [query-hint] in the aggregator).
# - 200 record limit per query may truncate very-rich genera (Ganoderma
#   lucidum returns 28MB suggesting many compounds per record).
# - LOTUS aggregates upstream sources (NPAtlas, Wikidata-fed, etc.).
#
# Usage:
#   bash scripts/phase_2b_lotus_pull.sh
#
# Output:
#   outputs/_lotus_raw/<query>.json  (gitignored — raw cache)
#   Then run: python3 scripts/phase_2b_aggregate_lotus.py
set -e

EXPDIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTDIR="$EXPDIR/outputs"
mkdir -p "$OUTDIR/_lotus_raw"

# Coverage: Phase 5 anchor species + broader genera that include many species.
# Add to this list to extend breadth — re-running is idempotent (cache check).
QUERIES=(
  "Ganoderma" "Cordyceps" "Ophiocordyceps" "Hericium" "Trametes" "Inonotus"
  "Grifola" "Lentinula" "Pleurotus" "Agaricus" "Antrodia" "Phellinus"
  "Wolfiporia" "Polyporus" "Tremella" "Auricularia" "Aspergillus oryzae"
  "Aspergillus terreus" "Aspergillus niger" "Aspergillus sojae"
  "Penicillium chrysogenum" "Penicillium roqueforti" "Penicillium camemberti"
  "Saccharomyces cerevisiae" "Schizophyllum commune" "Flammulina"
  "Hypsizygus" "Volvariella" "Coprinus" "Coprinopsis" "Ustilago" "Cyathus"
  "Boletus" "Suillus" "Lactarius" "Russula" "Termitomyces" "Hypholoma"
  "Phallus" "Geastrum" "Sparassis" "Hericium erinaceus" "Cordyceps militaris"
  "Cordyceps sinensis" "Trametes versicolor" "Inonotus obliquus"
  "Fomitopsis" "Piptoporus" "Polyporellus" "Ganoderma applanatum"
  "Ganoderma lucidum" "Ganoderma sinense" "Pleurotus ostreatus"
  "Pleurotus eryngii" "Cordyceps cicadae" "Yarrowia lipolytica"
)

for q in "${QUERIES[@]}"; do
  safe=$(echo "$q" | tr ' ' '_')
  outfile="$OUTDIR/_lotus_raw/${safe}.json"
  if [ -s "$outfile" ]; then
    echo "skip $q (cached)"
    continue
  fi
  curl -sS --max-time 60 -G \
    -H "User-Agent: OpenEnzymeResearchBot/1.0 (brian@headsupresults.com)" \
    -H "Accept: application/json" \
    --data-urlencode "query=$q" \
    --data-urlencode "limit=200" \
    "https://lotus.naturalproducts.net/api/search/simple" \
    -o "$outfile" 2>/dev/null
  size=$(wc -c < "$outfile" 2>/dev/null || echo 0)
  echo "  $q -> $size bytes"
  sleep 0.3  # be polite to LOTUS
done

echo ""
echo "Total files: $(ls "$OUTDIR/_lotus_raw" | wc -l)"
echo "Total bytes: $(du -sh "$OUTDIR/_lotus_raw" | cut -f1)"
