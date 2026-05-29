import glob, re, os, collections

files = sorted(glob.glob("wiki/*.md"))
wikinames = {os.path.basename(f) for f in files}
TAG = re.compile(r'\(\s*source[s]?\s*:\s*([^)]+)\)', re.I)
MD  = re.compile(r'([a-z0-9][a-z0-9\-]*\.md)', re.I)

tot_corpus_tok = sum(os.path.getsize(f) for f in files)/4
page_prov_tok = collections.defaultdict(float)
page_tot_tok  = {}
cited_from     = collections.Counter()
cited_from_tok = collections.Counter()
long_block_tok = 0.0
short_tag_tok  = 0.0
tagged_paras   = 0

for f in files:
    base = os.path.basename(f)
    txt = open(f, encoding='utf-8', errors='ignore').read()
    txt = re.sub(r'```.*?```', '', txt, flags=re.S)
    page_tot_tok[base] = os.path.getsize(f)/4
    for p in re.split(r'\n\s*\n', txt):
        m = TAG.search(p)
        if not m:
            continue
        cites = set()
        for c in MD.findall(m.group(1)):
            cl = c.lower()
            if cl in wikinames and cl not in {base}:
                cites.add(cl)
        if not cites:
            continue
        tagged_paras += 1
        ptok = len(p)/4
        page_prov_tok[base] += ptok
        for c in cites:
            cited_from[c]+=1; cited_from_tok[c]+=ptok
        if len(p.strip()) >= 200:
            long_block_tok += ptok
        else:
            short_tag_tok += ptok

total_prov = sum(page_prov_tok.values())
print("=== CORPUS-WIDE CROSS-PAGE PROVENANCE ===")
print(f"corpus total:                ~{tot_corpus_tok/1000:.0f}K tokens")
print(f"paras tagged (Source: other-wiki-page.md): {tagged_paras}")
print(f"token volume in those paras: ~{total_prov/1000:.0f}K tokens  ({total_prov/tot_corpus_tok*100:.1f}% of corpus)")
print(f"  LONG blocks (>=200 chars, likely restated exposition): ~{long_block_tok/1000:.0f}K")
print(f"  SHORT tags  (<200 chars, likely single cited claims):  ~{short_tag_tok/1000:.0f}K")
print()
print("=== TOP 15 most-DERIVATIVE pages (highest % cross-page-sourced) ===")
rows=[(page_prov_tok[b]/page_tot_tok[b]*100, page_prov_tok[b], page_tot_tok[b], b) for b in page_prov_tok if page_tot_tok[b]>500]
for pct,pt,tt,b in sorted(rows, reverse=True)[:15]:
    print(f"  {pct:4.0f}%  {pt/1000:4.1f}K/{tt/1000:4.1f}K tok  {b}")
print()
print("=== TOP 12 canonical pages most-RESTATED-FROM (by attributed tokens) ===")
for c,t in cited_from_tok.most_common(12):
    print(f"  ~{t/1000:4.1f}K tok across {cited_from[c]:3d} paras  <-  {c}")
