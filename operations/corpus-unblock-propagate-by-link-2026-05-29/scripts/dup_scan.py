import glob, re, os, collections

files = sorted(glob.glob("wiki/*.md"))
def norm(s):
    s = s.strip().lower()
    s = re.sub(r'\s+', ' ', s)
    return s

# ---------- paragraph-level exact/normalized duplication ----------
para_locs = collections.defaultdict(set)   # normed para -> set(files)
para_raw  = {}
for f in files:
    txt = open(f, encoding='utf-8', errors='ignore').read()
    # strip code fences to avoid mermaid/script noise
    txt = re.sub(r'```.*?```', '', txt, flags=re.S)
    for p in re.split(r'\n\s*\n', txt):
        n = norm(p)
        if len(n) < 160:        # ignore short bits (headers, list items, one-liners)
            continue
        if n.count(' ') < 20:   # at least ~20 words
            continue
        para_locs[n].add(f)
        para_raw[n] = p.strip()

dup = {n:fs for n,fs in para_locs.items() if len(fs) >= 2}
dup_tok = sum(len(n)/4 * (len(fs)-1) for n,fs in dup.items())  # redundant copies beyond the first
tot_tok = sum(os.path.getsize(f) for f in files)/4
print(f"=== PARAGRAPH-LEVEL (normalized exact) ===")
print(f"distinct paragraphs duplicated across >=2 files: {len(dup)}")
print(f"redundant token volume (copies beyond first): ~{dup_tok/1000:.0f}K tokens  ({dup_tok/tot_tok*100:.1f}% of corpus)")
print()
print("--- top 12 repeated paragraphs by (length x extra-copies) ---")
ranked = sorted(dup.items(), key=lambda kv: len(kv[0])*(len(kv[1])-1), reverse=True)[:12]
for n,fs in ranked:
    print(f"\n[{len(fs)} files, ~{len(n)/4:.0f} tok each] {sorted(os.path.basename(x) for x in fs)}")
    print("   “" + para_raw[n][:200].replace('\n',' ') + "…”")
