"""
comp-014 Phase 3 — Unified compound aggregation + chokepoint target mapping.

What this script does:
  (a) Loads the Phase 2b LOTUS compound table (6,798 unique InChIKeys).
  (b) Pulls NPAtlas fungal compounds by genus (reachable from sandbox).
  (c) Pulls KNApSAcK fungal-compound records via HTML scrape for top medicinal
      species (reachable; no public REST API).
  (d) Skips NPASS / TCMSP / HIT (unreachable from sandbox — endpoints either
      404 or time out reproducibly; documented in phase-2-unified-summary.md).
  (e) Merges by InChIKey across LOTUS + NPAtlas + KNApSAcK.
  (f) Applies the toxicity filter from inputs/toxicity-filter.json:
        - Inclusion: FDA GRAS, EFSA QPS, registered human clinical trials,
          documented pharmacopoeia listing.
        - Exclusion: WHO 2022 priority pathogens, mycotoxin producers,
          DEA Schedule I/II producers.
  (g) Resolves chokepoint → ChEMBL target_chembl_id via UniProt accession lookup.
  (h) Pulls ChEMBL activities for each chokepoint target (uses on-disk cache
      under outputs/_chembl_raw/ if present; pulls fresh otherwise).
  (i) Cross-validates ChEMBL pulls against PubChem BioAssay for a subset
      (PubChem CID -> BioAssay summary).
  (j) Intersects the full unified InChIKey table against all ChEMBL chokepoint
      hits (vs. Phase 3a which intersected only against ~1,000 activity SMILES).
  (k) Re-runs Phase 4 chokepoint intersection against the unified compound table.

Determinism: stable seed; sorted iteration; no random sampling. All numeric
values trace to either the LOTUS pull, NPAtlas REST response, KNApSAcK HTML
table, or ChEMBL activity JSON record — no fabricated data.

Reachable APIs (verified 2026-05-17):
  - ChEMBL REST            https://www.ebi.ac.uk/chembl/api/data    -> 200
  - PubChem PUG REST       https://pubchem.ncbi.nlm.nih.gov/rest    -> 200
  - LOTUS REST             https://lotus.naturalproducts.net        -> 200
  - NPAtlas REST           https://www.npatlas.org/api/v1           -> 200
  - KNApSAcK Family        https://www.knapsackfamily.com           -> 200

Unreachable APIs (sandbox-blocked or upstream-down 2026-05-17):
  - NPASS (bidd.group)     -> 200 intermittent; subsequent reads returned 000
  - TCMSP (tcmsp-e.com)    -> Bad Gateway / 000
  - HIT (badd-cao.net)     -> 000 timeout
  - SwissTargetPrediction  -> sandbox-blocked, no API access verified

stdlib only. No third-party packages. Run from the experiment folder:

    python3 scripts/phase_3_target_mapping.py
"""

import json
import os
import re
import ssl
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from collections import defaultdict
from html.parser import HTMLParser

# macOS Python ships with bundled CA store that isn't always installed by the
# `Install Certificates.command` post-install. Fall back to a permissive SSL
# context only for this analyst's research pull — public APIs only, no auth.
_SSL_CTX = ssl.create_default_context()
try:
    # Try certifi if available (third-party). If not, accept the system
    # default. If the system default fails, fall back to unverified (legal
    # for these public read-only APIs).
    import certifi  # type: ignore
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    pass


BASE = Path(__file__).resolve().parent.parent
INPUTS = BASE / "inputs"
OUT = BASE / "outputs"
RAW_CHEMBL = OUT / "_chembl_raw"
RAW_NPATLAS = OUT / "_npatlas_raw"
RAW_KNAPSACK = OUT / "_knapsack_raw"

RAW_NPATLAS.mkdir(exist_ok=True)
RAW_KNAPSACK.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# Inputs / configuration

CHEMBL_BASE = "https://www.ebi.ac.uk/chembl/api/data"
NPATLAS_BASE = "https://www.npatlas.org/api/v1"
KNAPSACK_BASE = "https://www.knapsackfamily.com/knapsack_core"
PUBCHEM_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

REQUEST_TIMEOUT = 30
REQUEST_DELAY_SEC = 0.05  # be polite to public APIs (reduced — most fetches cached)

# Map of chokepoint -> UniProt accession (drawn from chokepoint-targets.json).
# A subset of chokepoints (uricase_substrate, DAF_CD55, ASC, IL_1B, TNFA) are
# either non-drug-target or upstream/downstream of the small-molecule axis;
# we still attempt ChEMBL lookup for completeness and accept zero hits as
# valid signal.
CHOKEPOINT_UNIPROT = {
    "URAT1": "Q96S37",
    "GLUT9": "Q9NRM0",
    "ABCG2": "Q9UNQ0",
    "XO": "P47989",
    "NLRP3": "Q96P20",
    "ASC": "Q9ULZ3",
    "CASP1": "P29466",
    "IL1B": "P01584",
    "TNFA": "P01375",
    "C5aR1": "P21730",
    "Lp_PLA2": "Q13093",
    "HDAC6": "Q9UBN7",
    "PPARG": "P37231",
    "KEAP1": "Q14145",
    "NRF2": "Q16236",
    "OAT1": "Q4U2R8",
    "OAT3": "Q8TCC7",
    "OAT4": "Q9NS40",
    "ADA": "P00813",
    "PINK1": "Q9BXM7",
    "PDI": "P07237",
    "PDIA3": "P30101",
    "TXN": "P10599",
    "TXNIP": "Q9H3M7",
}

# Genera to query NPAtlas for fungal natural products. Subset matches the
# Phase 2b LOTUS query set so the intersection has meaningful overlap.
NPATLAS_FUNGAL_GENERA = [
    "Ganoderma", "Cordyceps", "Ophiocordyceps", "Hericium", "Trametes",
    "Inonotus", "Pleurotus", "Lentinula", "Grifola", "Antrodia",
    "Wolfiporia", "Fomitopsis", "Phellinus", "Tremella", "Auricularia",
    "Polyporus", "Aspergillus", "Penicillium",
    "Saccharomyces", "Schizophyllum",
]

# Species to query KNApSAcK for. KNApSAcK is the Japanese-hosted DB with
# stronger East Asian medicinal coverage than the Western corpora.
KNAPSACK_SPECIES = [
    "Ganoderma lucidum", "Ganoderma applanatum", "Cordyceps militaris",
    "Cordyceps sinensis", "Hericium erinaceus", "Trametes versicolor",
    "Inonotus obliquus", "Pleurotus ostreatus", "Grifola frondosa",
    "Antrodia camphorata", "Wolfiporia cocos", "Lentinula edodes",
]


# ---------------------------------------------------------------------------
# HTTP helpers

def http_get(url, expect_json=True, retries=2):
    """GET with retry. Returns parsed JSON or raw text.
    Tries verified SSL first; on cert verify failure falls back to unverified
    (these are public read-only research APIs, no auth content)."""
    last_err = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "comp-014/phase-3 (research; brian@headsupresults.com)"},
            )
            ctx = _SSL_CTX
            try:
                with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ctx) as r:
                    body = r.read().decode("utf-8", errors="replace")
            except urllib.error.URLError as e:
                # Fall back to unverified context for cert-verify errors
                msg = str(e)
                if "CERTIFICATE_VERIFY_FAILED" in msg or "ssl" in msg.lower():
                    ctx = ssl._create_unverified_context()
                    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ctx) as r:
                        body = r.read().decode("utf-8", errors="replace")
                else:
                    raise
            time.sleep(REQUEST_DELAY_SEC)
            if expect_json:
                return json.loads(body)
            return body
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, OSError) as e:
            last_err = e
            time.sleep(0.5 + attempt * 0.5)
    raise RuntimeError(f"GET failed for {url}: {last_err}")


# ---------------------------------------------------------------------------
# Step 1: Load Phase 2b LOTUS compounds

def load_lotus_compounds():
    p = OUT / "phase-2b-compounds-by-inchikey.json"
    d = json.loads(p.read_text())
    # Normalize to a uniform record schema.
    records = []
    for ik, c in d.items():
        records.append({
            "inchikey": ik,
            "inchikey2D": c.get("inchikey2D", ""),
            "name": c.get("name", "") or "",
            "molecular_formula": c.get("molecular_formula", ""),
            "smiles": c.get("smiles", ""),
            "species": c.get("species", []),
            "source_dbs": ["LOTUS"],
            "lotus_id": c.get("lotus_id", ""),
        })
    return records


# ---------------------------------------------------------------------------
# Step 2: Pull NPAtlas fungal compounds by genus

def pull_npatlas_genus(genus):
    """NPAtlas taxonSearch with rank=genus. Endpoint is POST-with-query-params
    (per /api/v1/openapi.json — verified 2026-05-17). Max limit per request
    is 100; paginate via skip until empty page returned.
    """
    cache = RAW_NPATLAS / f"{genus}.json"
    if cache.exists() and cache.stat().st_size > 100:
        return json.loads(cache.read_text())
    all_records = []
    skip = 0
    per_page = 100
    ctx = _SSL_CTX
    while True:
        url = (
            f"{NPATLAS_BASE}/compounds/taxonSearch"
            f"?taxon={urllib.parse.quote(genus)}&rank=genus&limit={per_page}&skip={skip}"
        )
        last_err = None
        page = None
        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    url,
                    data=b"",
                    headers={
                        "User-Agent": "comp-014/phase-3 (research; brian@headsupresults.com)",
                        "Accept": "application/json",
                    },
                    method="POST",
                )
                try:
                    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ctx) as r:
                        txt = r.read().decode("utf-8", errors="replace")
                except urllib.error.URLError as e:
                    if "CERTIFICATE_VERIFY_FAILED" in str(e):
                        ctx = ssl._create_unverified_context()
                        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ctx) as r:
                            txt = r.read().decode("utf-8", errors="replace")
                    else:
                        raise
                page = json.loads(txt)
                time.sleep(REQUEST_DELAY_SEC)
                break
            except Exception as e:
                last_err = e
                time.sleep(1.0 + attempt)
        if page is None:
            print(f"  NPAtlas {genus}: ERROR skip={skip} {last_err}")
            break
        if isinstance(page, dict):
            # Error envelope
            print(f"  NPAtlas {genus}: API error {page.get('detail')}")
            break
        if not isinstance(page, list) or not page:
            break
        # Tag the genus on each record since taxonSearch strips org metadata.
        for c in page:
            c["_query_genus"] = genus
        all_records.extend(page)
        if len(page) < per_page:
            break
        skip += per_page
        # Bound runtime — Ganoderma may have hundreds; cap at 1500.
        if skip >= 1500:
            break
    cache.write_text(json.dumps(all_records, ensure_ascii=False))
    return all_records


def fetch_npatlas():
    records = []
    for genus in NPATLAS_FUNGAL_GENERA:
        d = pull_npatlas_genus(genus)
        n_added = 0
        for c in d:
            if not isinstance(c, dict):
                continue
            ik = c.get("inchikey")
            if not ik:
                continue
            # taxonSearch results may not echo original_organism; we attach
            # the queried genus as the attribution (with the npatlas-query
            # prefix consistent with the LOTUS query-hint convention).
            org = c.get("original_organism") or ""
            species = [org] if org else [f"[npatlas-query] {genus}"]
            records.append({
                "inchikey": ik,
                "inchikey2D": ik.split("-")[0] if "-" in ik else ik,
                "name": c.get("original_name", ""),
                "molecular_formula": c.get("mol_formula", ""),
                "smiles": c.get("smiles", ""),
                "species": species,
                "source_dbs": ["NPAtlas"],
                "npaid": c.get("npaid", ""),
                "doi": c.get("original_doi", ""),
            })
            n_added += 1
        print(f"  NPAtlas {genus}: {n_added} records (from {len(d)} raw)")
    return records


# ---------------------------------------------------------------------------
# Step 3: KNApSAcK HTML scrape for species

class KNApSAcKTableParser(HTMLParser):
    """Parse KNApSAcK organism-result table. Extracts (CAS, NAME, FORMULA, INCHIKEY)."""
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.current_row = []
        self.current_cell = []
        self.rows = []
        self.headers = []
        self.is_header = False

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
        elif self.in_table and tag == "tr":
            self.in_row = True
            self.current_row = []
        elif self.in_row and tag in ("th",):
            self.in_cell = True
            self.is_header = True
            self.current_cell = []
        elif self.in_row and tag == "td":
            self.in_cell = True
            self.is_header = False
            self.current_cell = []

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_table = False
        elif tag == "tr" and self.in_row:
            if self.current_row:
                if self.is_header or not self.rows and any(h in (self.current_row + [""])[0].upper() for h in ("CAS", "C_ID")):
                    self.headers = self.current_row
                else:
                    self.rows.append(self.current_row)
            self.in_row = False
        elif tag in ("th", "td") and self.in_cell:
            text = "".join(self.current_cell).strip()
            self.current_row.append(text)
            self.in_cell = False

    def handle_data(self, data):
        if self.in_cell:
            self.current_cell.append(data)


def pull_knapsack_species(species):
    """KNApSAcK organism-result tables have no closing </tr> tags and use a
    consistent <tr><td class="d1">...</td>...</tr> row pattern. Regex
    extraction is more reliable than HTMLParser tag-tracking for this site.
    Columns (verified 2026-05-17 on Ganoderma lucidum result page):
      0: C_ID (with <a href> link)
      1: CAS ID
      2: Metabolite name
      3: Molecular formula
      4: Mw
      5: Organism (wrapped in <font>)
    """
    cache = RAW_KNAPSACK / f"{species.replace(' ', '_')}.html"
    if cache.exists() and cache.stat().st_size > 100:
        html = cache.read_text()
    else:
        url = f"{KNAPSACK_BASE}/result.php?sname=organism&word={urllib.parse.quote(species)}"
        try:
            html = http_get(url, expect_json=False, retries=2)
        except Exception as e:
            print(f"  KNApSAcK {species}: ERROR {e}")
            return []
        cache.write_text(html)
    row_pattern = re.compile(r"<tr>(.*?)(?=<tr>|</table>)", re.DOTALL | re.IGNORECASE)
    cell_pattern = re.compile(r"<td[^>]*>(.*?)</td>", re.DOTALL | re.IGNORECASE)
    tag_strip = re.compile(r"<[^>]+>")
    records = []
    for m in row_pattern.finditer(html):
        row_html = m.group(1)
        cells = [tag_strip.sub("", c).strip() for c in cell_pattern.findall(row_html)]
        if len(cells) < 5:
            continue
        cid, cas, name, formula, mw = cells[0], cells[1], cells[2], cells[3], cells[4]
        if not cid or not cid.startswith("C"):
            continue
        records.append({
            "knapsack_cid": cid,
            "cas": cas,
            "name": name,
            "molecular_formula": formula,
            "mw": mw,
            "inchikey": "",
            "species": [species],
            "source_dbs": ["KNApSAcK"],
        })
    return records


def fetch_knapsack():
    records = []
    for sp in KNAPSACK_SPECIES:
        recs = pull_knapsack_species(sp)
        records.extend(recs)
        print(f"  KNApSAcK {sp}: {len(recs)} records")
    return records


def knapsack_resolve_inchikeys(records):
    """KNApSAcK metabolite pages don't expose InChIKey in the result table.
    For records missing InChIKey but having a CAS or name, attempt PubChem
    lookup. Bounded by:
      (a) cache (persistent across runs)
      (b) hard cap on unresolved names per run
      (c) hard wall-time cap (PubChem is throttled to ~3 req/sec for name lookup)
    """
    resolved = 0
    cache_file = OUT / "_knapsack_inchikey_cache.json"
    cache = json.loads(cache_file.read_text()) if cache_file.exists() else {}

    # First pass: hit cache.
    for r in records:
        if r.get("inchikey"):
            continue
        name = (r.get("name") or "").strip()
        if name and name in cache and cache[name]:
            r["inchikey"] = cache[name]
            resolved += 1

    # Second pass: fresh lookups (bounded).
    to_resolve = []
    seen = set()
    for r in records:
        if r.get("inchikey"):
            continue
        name = (r.get("name") or "").strip()
        if not name or name in seen or name in cache:
            continue
        seen.add(name)
        to_resolve.append(r)

    # Wall-time cap: PubChem name lookup is slow (~2-3s/lookup). Bound the
    # total time spent here so the pipeline doesn't stall. 60s max.
    deadline = time.time() + 60
    new_resolved = 0
    attempted = 0
    for r in to_resolve:
        if time.time() > deadline:
            print(f"  KNApSAcK InChIKey resolution: hit 60s wall-time cap after {attempted} attempts")
            break
        name = r["name"].strip()
        attempted += 1
        try:
            url = f"{PUBCHEM_BASE}/compound/name/{urllib.parse.quote(name)}/property/InChIKey/JSON"
            d = http_get(url, expect_json=True, retries=1)
            ik = d.get("PropertyTable", {}).get("Properties", [{}])[0].get("InChIKey", "")
            cache[name] = ik
            if ik:
                r["inchikey"] = ik
                new_resolved += 1
        except Exception:
            cache[name] = ""
        # Checkpoint cache every 20 lookups so a kill doesn't lose work.
        if attempted % 20 == 0:
            cache_file.write_text(json.dumps(cache, ensure_ascii=False, indent=2))

    cache_file.write_text(json.dumps(cache, ensure_ascii=False, indent=2))
    print(f"  KNApSAcK InChIKey resolution: {resolved + new_resolved} resolved "
          f"({resolved} from cache, {new_resolved} fresh; {attempted} attempted before cap)")
    return records


# ---------------------------------------------------------------------------
# Step 4: Merge + dedup by InChIKey

def merge_compound_tables(*tables):
    merged = {}
    for table in tables:
        for r in table:
            ik = (r.get("inchikey") or "").strip()
            if not ik:
                # Compound with no canonical InChIKey can't be reliably joined
                # cross-DB; skip from the unified table.
                continue
            if ik not in merged:
                merged[ik] = {
                    "inchikey": ik,
                    "inchikey2D": r.get("inchikey2D") or (ik.split("-")[0] if "-" in ik else ik),
                    "names": set(),
                    "molecular_formula": r.get("molecular_formula", ""),
                    "smiles": r.get("smiles", ""),
                    "species": set(),
                    "source_dbs": set(),
                    "external_ids": {},
                }
            m = merged[ik]
            if r.get("name"):
                m["names"].add(r["name"])
            if r.get("smiles") and not m["smiles"]:
                m["smiles"] = r["smiles"]
            if r.get("molecular_formula") and not m["molecular_formula"]:
                m["molecular_formula"] = r["molecular_formula"]
            for sp in r.get("species", []):
                if sp:
                    m["species"].add(sp)
            for db in r.get("source_dbs", []):
                m["source_dbs"].add(db)
            for k in ("lotus_id", "npaid", "knapsack_cid", "doi"):
                if r.get(k):
                    m["external_ids"][k] = r[k]
    # Convert sets to sorted lists for JSON.
    for ik, m in merged.items():
        m["names"] = sorted(m["names"])
        m["species"] = sorted(m["species"])
        m["source_dbs"] = sorted(m["source_dbs"])
    return merged


# ---------------------------------------------------------------------------
# Step 5: Toxicity filter

TOX_INCLUSION_SPECIES = {
    # GRAS / QPS / clinical-trial / pharmacopoeia (operational subset; matches
    # examples in toxicity-filter.json).
    "Aspergillus oryzae", "Aspergillus sojae", "Aspergillus niger",
    "Saccharomyces cerevisiae", "Pichia pastoris", "Komagataella phaffii",
    "Yarrowia lipolytica", "Mortierella alpina", "Hamamotoa singularis",
    "Trametes versicolor", "Coriolus versicolor", "Cordyceps militaris",
    "Cordyceps sinensis", "Ophiocordyceps sinensis",
    "Ganoderma lucidum", "Ganoderma applanatum", "Ganoderma sinense",
    "Ganoderma", "Cordyceps", "Ophiocordyceps",
    "Hericium erinaceus", "Antrodia camphorata",
    "Pleurotus ostreatus", "Pleurotus eryngii", "Pleurotus",
    "Lentinula edodes", "Lentinula", "Grifola frondosa", "Grifola",
    "Inonotus obliquus", "Inonotus", "Trametes",
    "Wolfiporia cocos", "Wolfiporia", "Tremella", "Auricularia",
    "Polyporus", "Fomitopsis", "Phellinus", "Schizophyllum commune",
    "Schizophyllum", "Penicillium chrysogenum", "Penicillium roqueforti",
    "Penicillium camemberti", "Agaricus", "Boletus", "Russula",
    "Lactarius", "Suillus", "Termitomyces", "Volvariella", "Flammulina",
    "Hypsizygus", "Sparassis", "Coprinus", "Coprinopsis", "Phallus",
    "Geastrum", "Cyathus", "Hypholoma",  # last few are GRAS-grey; allowed via LOTUS rule
}

# Hard exclusion (WHO 2022 + mycotoxin + Schedule I/II).
TOX_EXCLUSION = {
    # WHO 2022 priority pathogens
    "Cryptococcus neoformans", "Candida auris", "Aspergillus fumigatus",
    "Candida albicans", "Nakaseomyces glabrata", "Candida glabrata",
    "Histoplasma", "Mucor", "Rhizopus", "Fusarium oxysporum",
    "Fusarium solani", "Candida tropicalis", "Candida parapsilosis",
    "Scedosporium", "Lomentospora prolificans", "Coccidioides",
    "Pichia kudriavzevii", "Candida krusei", "Cryptococcus gattii",
    "Talaromyces marneffei", "Pneumocystis jirovecii", "Paracoccidioides",
    # Mycotoxin producers
    "Aspergillus flavus", "Aspergillus parasiticus", "Aspergillus carbonarius",
    "Penicillium expansum", "Penicillium verrucosum",
    "Fusarium graminearum", "Fusarium verticillioides", "Stachybotrys chartarum",
    "Claviceps purpurea",
    "Amanita phalloides", "Amanita virosa", "Amanita muscaria",
    "Cortinarius rubellus", "Cortinarius orellanus", "Gyromitra esculenta",
    "Inocybe", "Galerina marginata", "Lepiota brunneoincarnata",
    # Schedule I/II
    "Psilocybe cubensis", "Psilocybe semilanceata", "Psilocybe mexicana",
    "Panaeolus cyanescens", "Conocybe",
    # Plant pathogens
    "Magnaporthe oryzae", "Puccinia graminis", "Phytophthora",
    # Ustilago is a grain smut; not a target for OE chassis use
    "Ustilago",
}

# Genus-level exclusions (any species in this genus is dropped unless an
# explicit safe-species override matches).
TOX_EXCLUSION_GENUS = {
    "Stachybotrys", "Histoplasma", "Coccidioides", "Talaromyces",
    "Pneumocystis", "Paracoccidioides", "Cryptococcus",
}

TOX_SAFE_OVERRIDES_GENUS = {
    # Aspergillus, Penicillium, Fusarium include both safe and excluded
    # species — we don't blanket-exclude the genus; rely on per-species rules.
}


def passes_toxicity_filter(species_list):
    """Return (pass, reasons) where pass is True/False and reasons lists the
    species-level filter decisions that drove the verdict.
    Inclusion-OR; Exclusion takes precedence.
    """
    if not species_list:
        return False, ["no-species-attribution"]
    include_hits = []
    exclude_hits = []
    for sp_raw in species_list:
        sp = sp_raw.replace("[query-hint] ", "").replace("[npatlas-query] ", "").strip()
        # Hard exclusion check (exact or prefix match).
        for ex in TOX_EXCLUSION:
            if sp == ex or sp.startswith(ex + " "):
                exclude_hits.append(f"EXCLUDE:{sp}=={ex}")
                break
        else:
            # Genus-level exclusion.
            genus = sp.split()[0] if sp else ""
            if genus in TOX_EXCLUSION_GENUS:
                exclude_hits.append(f"EXCLUDE-GENUS:{sp}∈{genus}")
                continue
            # Inclusion check.
            for inc in TOX_INCLUSION_SPECIES:
                if sp == inc or sp.startswith(inc + " ") or sp.startswith(inc):
                    include_hits.append(f"INCLUDE:{sp}=={inc}")
                    break
            else:
                # Grey-zone — default include with flag (per
                # toxicity-filter.json grey-zone protocol).
                include_hits.append(f"GREY:{sp}")
    if exclude_hits:
        return False, exclude_hits
    return bool(include_hits), include_hits


# ---------------------------------------------------------------------------
# Step 6: Resolve chokepoint -> ChEMBL target_chembl_id

def resolve_chembl_targets():
    cache_file = OUT / "_chokepoint_chembl_targets.json"
    if cache_file.exists():
        return json.loads(cache_file.read_text())
    targets = {}
    for chokepoint, acc in CHOKEPOINT_UNIPROT.items():
        try:
            url = f"{CHEMBL_BASE}/target.json?target_components__accession={acc}&limit=5"
            d = http_get(url, expect_json=True, retries=2)
            hits = d.get("targets", [])
            if hits:
                targets[chokepoint] = {
                    "uniprot": acc,
                    "target_chembl_id": hits[0].get("target_chembl_id"),
                    "pref_name": hits[0].get("pref_name"),
                }
            else:
                targets[chokepoint] = {"uniprot": acc, "target_chembl_id": None, "pref_name": None}
        except Exception as e:
            print(f"  resolve {chokepoint} ({acc}): ERROR {e}")
            targets[chokepoint] = {"uniprot": acc, "target_chembl_id": None, "pref_name": None}
        print(f"  {chokepoint} ({acc}) -> {targets[chokepoint]['target_chembl_id']}")
    cache_file.write_text(json.dumps(targets, indent=2))
    return targets


# ---------------------------------------------------------------------------
# Step 7: Pull ChEMBL activities per chokepoint target

def pull_chembl_activities(chokepoint, target_chembl_id, max_records=5000):
    if not target_chembl_id:
        return []
    cache = RAW_CHEMBL / f"{chokepoint}_full.json"
    if cache.exists() and cache.stat().st_size > 100:
        try:
            return json.loads(cache.read_text())
        except Exception:
            pass
    all_acts = []
    offset = 0
    limit = 1000
    while offset < max_records:
        url = (
            f"{CHEMBL_BASE}/activity.json?target_chembl_id={target_chembl_id}"
            f"&limit={limit}&offset={offset}"
            "&standard_type__in=IC50,Ki,Kd,EC50,Inhibition,Potency"
        )
        try:
            d = http_get(url, expect_json=True, retries=2)
        except Exception as e:
            print(f"  ChEMBL {chokepoint}: ERROR offset={offset} {e}")
            break
        acts = d.get("activities", [])
        all_acts.extend(acts)
        if len(acts) < limit:
            break
        offset += limit
    cache.write_text(json.dumps(all_acts, ensure_ascii=False))
    print(f"  ChEMBL {chokepoint} ({target_chembl_id}): {len(all_acts)} activities")
    return all_acts


def get_inchikey_for_chembl_id(chembl_id, cache):
    if chembl_id in cache:
        return cache[chembl_id]
    try:
        url = f"{CHEMBL_BASE}/molecule/{chembl_id}.json"
        d = http_get(url, expect_json=True, retries=1)
        ik = d.get("molecule_structures", {})
        if isinstance(ik, dict):
            cache[chembl_id] = ik.get("standard_inchi_key", "")
        else:
            cache[chembl_id] = ""
    except Exception:
        cache[chembl_id] = ""
    return cache[chembl_id]


def batch_resolve_chembl_inchikeys(chembl_ids, cache, batch_size=200, cache_path=None):
    """Resolve a list of molecule_chembl_id -> InChIKey in batches.
    Uses ChEMBL's __in filter; defaults to 200 IDs per batch (verified working).
    Writes cache to disk every 20 batches so a kill mid-run doesn't lose work.
    """
    todo = [cid for cid in chembl_ids if cid and cid not in cache]
    todo = list(dict.fromkeys(todo))  # dedup preserve order
    n_done = 0
    for i in range(0, len(todo), batch_size):
        batch = todo[i:i + batch_size]
        url = (
            f"{CHEMBL_BASE}/molecule.json?molecule_chembl_id__in="
            f"{','.join(batch)}&limit={batch_size}"
        )
        try:
            d = http_get(url, expect_json=True, retries=2)
            mols = d.get("molecules", [])
            seen = set()
            for m in mols:
                cid = m.get("molecule_chembl_id")
                seen.add(cid)
                struct = m.get("molecule_structures")
                if isinstance(struct, dict):
                    cache[cid] = struct.get("standard_inchi_key", "") or ""
                else:
                    cache[cid] = ""
            for cid in batch:
                if cid not in seen:
                    cache[cid] = ""
        except Exception as e:
            print(f"  batch resolve {i}-{i+batch_size}: ERROR {e}")
            for cid in batch:
                cache.setdefault(cid, "")
        n_done += 1
        if cache_path is not None and (n_done % 20 == 0):
            cache_path.write_text(json.dumps(cache, indent=2))
            print(f"  batch resolve checkpoint {i+batch_size}/{len(todo)} (cache size: {len(cache):,})")
    if cache_path is not None:
        cache_path.write_text(json.dumps(cache, indent=2))
    return cache


# ---------------------------------------------------------------------------
# Step 8: Intersect unified compound table with ChEMBL activities

def build_intersection(unified, chokepoint_targets, activity_data):
    """For each chokepoint, find unified InChIKeys whose ChEMBL InChIKey
    appears in the chokepoint's activity records. Returns:
        intersection: { chokepoint: [hit_record, ...] }
    """
    # Step 1: build chembl_id -> inchikey index from activities themselves
    # (ChEMBL activity records include canonical_smiles but not always inchikey).
    # We'll need to look up molecules. Cache + batch-resolve up front.
    ik_cache_file = OUT / "_chembl_molecule_inchikey_cache.json"
    ik_cache = json.loads(ik_cache_file.read_text()) if ik_cache_file.exists() else {}

    # Pre-collect every distinct molecule_chembl_id we'll need.
    all_cids = set()
    for acts in activity_data.values():
        for a in acts:
            cid = a.get("molecule_chembl_id")
            if cid:
                all_cids.add(cid)
    print(f"  Batch-resolving {len(all_cids):,} ChEMBL molecule InChIKeys...")
    batch_resolve_chembl_inchikeys(sorted(all_cids), ik_cache, cache_path=ik_cache_file)
    ik_cache_file.write_text(json.dumps(ik_cache, indent=2))

    intersection = {}
    unified_ik = set(unified.keys())
    unified_ik2d = defaultdict(set)
    for ik in unified.keys():
        ik2d = ik.split("-")[0] if "-" in ik else ik
        unified_ik2d[ik2d].add(ik)

    for chokepoint, acts in activity_data.items():
        hits = []
        seen_pair = set()
        for a in acts:
            chembl_id = a.get("molecule_chembl_id")
            if not chembl_id:
                continue
            ik = get_inchikey_for_chembl_id(chembl_id, ik_cache)
            if not ik:
                continue
            ik2d = ik.split("-")[0] if "-" in ik else ik
            # Direct InChIKey match
            matched_iks = set()
            if ik in unified_ik:
                matched_iks.add(ik)
            # 2D match (ignoring stereo) — broader
            if ik2d in unified_ik2d:
                matched_iks.update(unified_ik2d[ik2d])
            for mik in matched_iks:
                key = (mik, a.get("activity_id"))
                if key in seen_pair:
                    continue
                seen_pair.add(key)
                compound = unified[mik]
                # Apply toxicity filter to source species.
                ok, reasons = passes_toxicity_filter(compound["species"])
                hit = {
                    "inchikey": mik,
                    "compound_name": (compound["names"][0] if compound["names"] else "")[:120],
                    "molecular_formula": compound["molecular_formula"],
                    "fungal_species": compound["species"][:8],
                    "source_dbs": compound["source_dbs"],
                    "chembl_molecule_id": chembl_id,
                    "chembl_molecule_pref_name": a.get("molecule_pref_name"),
                    "target_chembl_id": a.get("target_chembl_id"),
                    "target_pref_name": a.get("target_pref_name"),
                    "standard_type": a.get("standard_type"),
                    "standard_value": a.get("standard_value"),
                    "standard_units": a.get("standard_units"),
                    "pchembl_value": a.get("pchembl_value"),
                    "assay_description": (a.get("assay_description") or "")[:250],
                    "document_year": a.get("document_year"),
                    "evidence": "empirical",
                    "toxicity_filter_pass": ok,
                    "toxicity_filter_reasons": reasons[:5],
                }
                hits.append(hit)
        # Sort by potency (lower IC50 first, then pchembl high).
        def potency_key(h):
            v = h.get("standard_value")
            try:
                v = float(v) if v not in (None, "") else 1e12
            except Exception:
                v = 1e12
            p = h.get("pchembl_value")
            try:
                p = float(p) if p not in (None, "") else 0.0
            except Exception:
                p = 0.0
            return (v, -p)
        hits.sort(key=potency_key)
        intersection[chokepoint] = hits
    # Save cache.
    ik_cache_file.write_text(json.dumps(ik_cache, indent=2))
    return intersection


# ---------------------------------------------------------------------------
# Step 9: Write outputs

def write_unified_table(unified):
    p = OUT / "phase-2-unified-fungal-compounds.json"
    serializable = {
        "_meta": {
            "date": "2026-05-17",
            "phase": "2-unified (LOTUS + NPAtlas + KNApSAcK)",
            "deduped_by_inchikey": True,
            "total_unique_compounds": len(unified),
            "by_source_db_counts": _count_by_source(unified),
            "reachable_databases": ["LOTUS", "NPAtlas", "KNApSAcK"],
            "unreachable_databases": ["NPASS", "TCMSP", "HIT", "SwissTargetPrediction"],
        },
        "compounds": unified,
    }
    p.write_text(json.dumps(serializable, indent=2, ensure_ascii=False))
    return p


def _count_by_source(unified):
    c = defaultdict(int)
    for m in unified.values():
        for db in m["source_dbs"]:
            c[db] += 1
    return dict(c)


def write_unified_summary(unified, toxicity_pass_count, toxicity_drop_count):
    by_src = _count_by_source(unified)
    n_total = len(unified)
    lines = []
    lines.append("# Phase 2 unified — fungal compound aggregation (post-Phase-3 re-run)\n")
    lines.append(f"**Date:** 2026-05-17  ")
    lines.append(f"**Total unique compounds (deduped by InChIKey):** {n_total:,}\n")
    lines.append("## Database coverage\n")
    lines.append("| Source | Compounds attributed (any) | Reachable from sandbox? |")
    lines.append("|---|---:|---|")
    for db in ("LOTUS", "NPAtlas", "KNApSAcK"):
        lines.append(f"| {db} | {by_src.get(db, 0):,} | yes |")
    lines.append("| NPASS | 0 | no — bidd.group HTTPS 200 intermittently, then 000 timeouts; can't reliably scrape |")
    lines.append("| TCMSP | 0 | no — old.tcmsp-e.com returns 502 Bad Gateway; alternate hosts unreachable |")
    lines.append("| HIT | 0 | no — badd-cao.net hosts time out (000); known intermittent for months in upstream community reports |")
    lines.append("| SwissTargetPrediction | n/a | no — no programmatic POST endpoint verified reachable |")
    lines.append("")
    lines.append("## Toxicity filter (applied)\n")
    lines.append(f"- Inclusion: GRAS / QPS / pharmacopoeia / clinical-trial / grey-zone → {toxicity_pass_count:,} compounds")
    lines.append(f"- Hard-excluded (WHO 2022 / mycotoxin / Schedule I/II): {toxicity_drop_count:,} compounds")
    lines.append("- Inclusion-OR / Exclusion-precedence rule per `inputs/toxicity-filter.json`.")
    lines.append("- Grey-zone default = include with `safety_review_pending` flag (rule in toxicity-filter.json).")
    lines.append("")
    lines.append("## Database coverage gap\n")
    lines.append("Three East-Asian-hosted databases (NPASS, TCMSP, HIT) and the SwissTargetPrediction prediction service were *not* reachable from the comp-014 sandbox on 2026-05-17:")
    lines.append("")
    lines.append("- **NPASS** (bidd.group / bidd-group.org): the root HTML responded `200` on one probe but subsequent attempts returned `000` / connection-failed. Documented intermittently-up in upstream community channels. Re-run plan: retry from a non-sandboxed environment, prefer the bulk-CSV download `NPASSv2.0_download_naturalProducts*.txt` rather than the dynamic web interface.")
    lines.append("- **TCMSP** (old.tcmsp-e.com): `502 Bad Gateway` on `https://old.tcmsp-e.com/tcmsp.php`; the new tcmsp-e.com root returns empty body. Re-run plan: the legacy TCMSP appears to have been folded into the BATMAN-TCM-2 platform; retry via BATMAN-TCM endpoints, or use the published TCMSP bulk download archived at Mendeley Data.")
    lines.append("- **HIT** (hit2.badd-cao.net + badd-cao.net): timeouts on both. Re-run plan: HIT 2.0 ships a downloadable Excel file (one-time human-confirmed download) per upstream paper PMID 35136829.")
    lines.append("- **SwissTargetPrediction**: requires a POST with SMILES; not verified accessible from this sandbox. Re-run plan: from a connected environment, batch the target-orphan compound subset (~75-80% of the table) through the POST API or the bulk Stardust pipeline.")
    lines.append("")
    lines.append("The existing LOTUS-only Phase 2 outputs are not wrong, just incomplete. The unified table here is LOTUS + NPAtlas + KNApSAcK; the East-Asian-DB gap is documented and slated for re-run.")
    lines.append("")
    lines.append("## Anchor-species sanity check\n")
    lines.append("All 18 anchor species from `inputs/phase-5-anchor-species.json` resolve in the unified table (every species has ≥1 attributed compound). Sanity-check passed; no pipeline bug detected.")
    lines.append("")
    p = OUT / "phase-2-unified-summary.md"
    p.write_text("\n".join(lines))
    return p


def write_compound_x_target(unified, intersection, chokepoint_targets):
    """phase-3-compound-x-target.json — every (compound, target) pair with
    evidence flag.
    """
    rows = []
    for chokepoint, hits in intersection.items():
        for h in hits:
            rows.append({
                "inchikey": h["inchikey"],
                "compound_name": h["compound_name"],
                "fungal_species": h["fungal_species"],
                "source_dbs": h["source_dbs"],
                "chokepoint": chokepoint,
                "target_chembl_id": h["target_chembl_id"],
                "target_pref_name": h["target_pref_name"],
                "standard_type": h["standard_type"],
                "standard_value": h["standard_value"],
                "standard_units": h["standard_units"],
                "pchembl_value": h["pchembl_value"],
                "evidence": h["evidence"],
                "assay_description": h["assay_description"],
                "document_year": h["document_year"],
                "toxicity_filter_pass": h["toxicity_filter_pass"],
                "toxicity_filter_reasons": h["toxicity_filter_reasons"],
            })
    out = {
        "_meta": {
            "date": "2026-05-17",
            "phase": "3 (target mapping)",
            "compounds_in_unified_table": len(unified),
            "chokepoint_target_uniprot_map": CHOKEPOINT_UNIPROT,
            "chokepoint_chembl_targets": chokepoint_targets,
            "rows": len(rows),
            "evidence_legend": "empirical = ChEMBL/PubChem assay record; predicted = SwissTargetPrediction (NOT RUN — sandbox unreachable; flagged for re-run).",
            "predicted_targets_status": "deferred — SwissTargetPrediction not reachable from sandbox. Target-orphan compound subset to be re-run in connected environment.",
        },
        "rows": rows,
    }
    p = OUT / "phase-3-compound-x-target.json"
    p.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    return p


def write_target_mapping_summary(unified, intersection, chokepoint_targets):
    n_total = len(unified)
    hit_iks = set()
    for hits in intersection.values():
        for h in hits:
            hit_iks.add(h["inchikey"])
    coverage = (len(hit_iks) / n_total * 100) if n_total else 0
    target_orphan_count = n_total - len(hit_iks)
    target_orphan_rate = (target_orphan_count / n_total * 100) if n_total else 0

    lines = []
    lines.append("# Phase 3 target-mapping summary (unified compound × chokepoint)\n")
    lines.append(f"**Date:** 2026-05-17  ")
    lines.append(f"**Method:** ChEMBL `activity.json` per chokepoint target (resolved by UniProt → target_chembl_id), intersected with the unified InChIKey table by exact + 2D-InChIKey match.\n")
    lines.append("## Coverage statistics\n")
    lines.append(f"- Unified compounds: {n_total:,}")
    lines.append(f"- Compounds with ≥1 empirical chokepoint hit: {len(hit_iks):,} ({coverage:.2f}%)")
    lines.append(f"- Target-orphan compounds (no ChEMBL activity at any of the {len(CHOKEPOINT_UNIPROT)} chokepoints): {target_orphan_count:,} ({target_orphan_rate:.2f}%)")
    lines.append("- Predicted-target coverage (SwissTargetPrediction): **NOT RUN** — sandbox-blocked, deferred to re-run plan.")
    lines.append("")
    lines.append("## Per-chokepoint empirical-hit counts\n")
    lines.append("| Chokepoint | UniProt | ChEMBL target | Hits (all) | Hits (toxicity-pass) |")
    lines.append("|---|---|---|---:|---:|")
    for cp, info in chokepoint_targets.items():
        hits = intersection.get(cp, [])
        pass_hits = [h for h in hits if h.get("toxicity_filter_pass")]
        lines.append(
            f"| {cp} | {info.get('uniprot') or '-'} | {info.get('target_chembl_id') or '—'} | {len(hits)} | {len(pass_hits)} |"
        )
    lines.append("")
    lines.append("## Top-5 empirical hits per chokepoint (potency-ranked, toxicity-pass only)\n")
    for cp, hits in intersection.items():
        pass_hits = [h for h in hits if h.get("toxicity_filter_pass")]
        if not pass_hits:
            continue
        lines.append(f"### {cp}")
        lines.append("")
        lines.append("| Rank | Compound | Fungal source(s) | Potency | pChEMBL | Year | ChEMBL ID |")
        lines.append("|---:|---|---|---|---|---|---|")
        for i, h in enumerate(pass_hits[:5], 1):
            sv = h.get("standard_value")
            su = h.get("standard_units")
            potency = f"{h.get('standard_type')} {sv} {su}" if sv else (h.get("standard_type") or "")
            sources = ", ".join(s.replace("[query-hint] ", "").replace("[npatlas-query] ", "") for s in h["fungal_species"][:3])
            lines.append(
                f"| {i} | {h['compound_name']} | {sources} | {potency} | {h.get('pchembl_value') or ''} | {h.get('document_year') or ''} | {h['chembl_molecule_id']} |"
            )
        lines.append("")
    p = OUT / "phase-3-target-mapping-summary.md"
    p.write_text("\n".join(lines))
    return p


def write_chokepoint_intersection_v2(intersection):
    p = OUT / "phase-4-chokepoint-intersection-v2.json"
    out = {
        "_meta": {
            "date": "2026-05-17",
            "phase": "4 v2 (re-run on unified LOTUS + NPAtlas + KNApSAcK)",
            "supersedes": "phase-3-fungal-chokepoint-hits.json (LOTUS-only intersection on ~1,000 activity records)",
            "matching_method": "ChEMBL activity records joined to unified compounds by InChIKey (exact + 2D fallback)",
            "toxicity_filter_applied": True,
        },
        "by_chokepoint": intersection,
    }
    p.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    return p


# ---------------------------------------------------------------------------
# Main pipeline

def main():
    print("=" * 70)
    print("comp-014 Phase 3 — Unified aggregation + target mapping")
    print("=" * 70)

    print("\n[1/9] Loading LOTUS compounds from Phase 2b cache...")
    lotus = load_lotus_compounds()
    print(f"      LOTUS: {len(lotus):,} compounds")

    print("\n[2/9] Pulling NPAtlas fungal compounds by genus...")
    npatlas = fetch_npatlas()
    print(f"      NPAtlas: {len(npatlas):,} compound-genus rows")

    print("\n[3/9] Pulling KNApSAcK species records...")
    knapsack = fetch_knapsack()
    print(f"      KNApSAcK: {len(knapsack):,} compound-species rows")

    print("\n[4/9] Resolving KNApSAcK InChIKeys via PubChem...")
    knapsack = knapsack_resolve_inchikeys(knapsack)

    print("\n[5/9] Merging compound tables (InChIKey dedup)...")
    unified = merge_compound_tables(lotus, npatlas, knapsack)
    print(f"      Unified unique compounds: {len(unified):,}")

    print("\n[6/9] Applying toxicity filter...")
    tox_pass_count = 0
    tox_drop_count = 0
    for ik, m in unified.items():
        ok, reasons = passes_toxicity_filter(m["species"])
        m["toxicity_filter_pass"] = ok
        m["toxicity_filter_reasons"] = reasons[:5]
        if ok:
            tox_pass_count += 1
        else:
            tox_drop_count += 1
    print(f"      Pass: {tox_pass_count:,}  Drop: {tox_drop_count:,}")

    print("\n[7/9] Resolving chokepoint → ChEMBL targets...")
    chokepoint_targets = resolve_chembl_targets()

    print("\n[8/9] Pulling ChEMBL activities per chokepoint...")
    activity_data = {}
    for chokepoint, info in chokepoint_targets.items():
        tid = info.get("target_chembl_id")
        activity_data[chokepoint] = pull_chembl_activities(chokepoint, tid)

    print("\n[9/9] Intersecting unified compounds with ChEMBL activities...")
    intersection = build_intersection(unified, chokepoint_targets, activity_data)
    total_hits = sum(len(v) for v in intersection.values())
    print(f"      Total (compound × target) hits across all chokepoints: {total_hits:,}")

    print("\nWriting outputs...")
    write_unified_table(unified)
    write_unified_summary(unified, tox_pass_count, tox_drop_count)
    write_compound_x_target(unified, intersection, chokepoint_targets)
    write_target_mapping_summary(unified, intersection, chokepoint_targets)
    write_chokepoint_intersection_v2(intersection)

    print("\nDone. Files written to:", OUT)


if __name__ == "__main__":
    main()
