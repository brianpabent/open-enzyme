import glob, re, os, math, collections

files = sorted(glob.glob("wiki/*.md"))
STOP = set("the a an and or of to in for on with is are be as by at from this that it its their which we our you your they them than then so if not no can may will would could should into over under up down out about more most less also such each per via vs etc into within across between both either neither only just but how what when where who whom whose all any some many few one two three".split())
def toks(f):
    t = open(f, encoding='utf-8', errors='ignore').read().lower()
    t = re.sub(r'```.*?```', ' ', t, flags=re.S)
    t = re.sub(r'http\S+', ' ', t)
    return [w for w in re.findall(r'[a-z][a-z0-9\-]{2,}', t) if w not in STOP]

docs = {f: collections.Counter(toks(f)) for f in files}
N = len(docs)
df = collections.Counter()
for c in docs.values():
    for w in c: df[w]+=1
idf = {w: math.log(N/(1+d)) for w,d in df.items()}
def vec(c):
    v = {w: (1+math.log(n))*idf[w] for w,n in c.items()}
    norm = math.sqrt(sum(x*x for x in v.values())) or 1
    return {w:x/norm for w,x in v.items()}, norm
vecs = {f: vec(c)[0] for f,c in docs.items()}
def cos(a,b):
    if len(a)>len(b): a,b=b,a
    return sum(x*b.get(w,0) for w,x in a.items())

pairs=[]
fl=list(files)
for i in range(len(fl)):
    for j in range(i+1,len(fl)):
        s=cos(vecs[fl[i]],vecs[fl[j]])
        pairs.append((s,fl[i],fl[j]))
pairs.sort(reverse=True)
print("=== TOP 22 MOST TEXTUALLY-OVERLAPPING PAGE PAIRS (TF-IDF cosine) ===")
for s,a,b in pairs[:22]:
    print(f"  {s:.2f}  {os.path.basename(a):42s} ~ {os.path.basename(b)}")

print("\n=== pages whose closest neighbor is very high (potential echoes) ===")
best=collections.defaultdict(float); bestp={}
for s,a,b in pairs:
    if s>best[a]: best[a]=s; bestp[a]=b
    if s>best[b]: best[b]=s; bestp[b]=a
for f in sorted(best, key=lambda x:-best[x])[:14]:
    kt=os.path.getsize(f)/4/1000
    print(f"  {best[f]:.2f}  {os.path.basename(f):42s} (~{kt:.0f}K tok)  ↔ {os.path.basename(bestp[f])}")
