"""
Dogfood the lit-scan skill's local_curl_fetch against East Asian academic hosts.

Targets:
  - CNKI (kns.cnki.net) search
  - WanFang (wanfangdata.com.cn)
  - CQVIP (cqvip.com)
  - Baidu Scholar (xueshu.baidu.com)
  - ChinaXiv

Queries center on: 鱼腥草多糖 (HC polysaccharide) structure / anti- vs pro-inflammatory /
capsule composition / gout-uric-acid (to check if any MSU/gout data exists in zh corpus).

Reports HTTP status + bytes per host so we can honestly say what reached vs bot-walled.
"""
import sys
import urllib.parse
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "wiki/etc/experiments/lib"))

from agentic_lit_synthesis import local_curl_fetch, host_allowed_for_local_curl  # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE / "sources"

# (label, url) — search endpoints. Use each host's public search URL form.
def q(s):
    return urllib.parse.quote(s)

targets = [
    # Baidu Scholar (xueshu.baidu.com) — general zh academic search
    ("baidu_hcp_structure_antiinflam", f"https://xueshu.baidu.com/s?wd={q('鱼腥草多糖 结构 抗炎')}"),
    ("baidu_hcp_proinflam", f"https://xueshu.baidu.com/s?wd={q('鱼腥草多糖 促炎 免疫刺激')}"),
    ("baidu_hcp_capsule_composition", f"https://xueshu.baidu.com/s?wd={q('鱼腥草 胶囊 多糖 成分 含量')}"),
    ("baidu_hcp_gout_uricacid", f"https://xueshu.baidu.com/s?wd={q('鱼腥草 痛风 尿酸')}"),
    ("baidu_hcp_msu_nlrp3", f"https://xueshu.baidu.com/s?wd={q('鱼腥草 尿酸钠 NLRP3 白细胞介素1')}"),
    ("baidu_hcp2_homogalacturonan", f"https://xueshu.baidu.com/s?wd={q('鱼腥草多糖 半乳糖醛酸 TLR4 PBMC')}"),
    # CNKI search (kns.cnki.net) — public search entry
    ("cnki_hcp_structure", f"https://kns.cnki.net/kns8s/defaultresult/index?kw={q('鱼腥草多糖 结构 抗炎')}"),
    ("cnki_hcp_gout", f"https://kns.cnki.net/kns8s/defaultresult/index?kw={q('鱼腥草 痛风 尿酸')}"),
    # WanFang
    ("wanfang_hcp_structure", f"https://s.wanfangdata.com.cn/paper?q={q('鱼腥草多糖 结构 抗炎')}"),
    ("wanfang_hcp_gout", f"https://s.wanfangdata.com.cn/paper?q={q('鱼腥草 痛风 尿酸')}"),
    # CQVIP
    ("cqvip_hcp_structure", f"https://www.cqvip.com/search?k={q('鱼腥草多糖 结构 抗炎')}"),
    # ChinaXiv
    ("chinaxiv_hcp", f"https://www.chinaxiv.org/search.htm?q={q('鱼腥草多糖')}"),
]

for label, url in targets:
    host = urllib.parse.urlparse(url).hostname
    allowed = host_allowed_for_local_curl(host)
    if not allowed:
        print(f"[SKIP] {label}: host {host} not in allowlist")
        continue
    try:
        prov = local_curl_fetch(url, OUT, timeout_seconds=60)
        body = Path(prov["body_path"])
        size = body.stat().st_size if body.exists() else 0
        print(f"[OK]   {label}: rc={prov['returncode']} status='{prov['stdout']}' bytes={size} host={host}")
    except Exception as e:
        print(f"[FAIL] {label}: {type(e).__name__}: {str(e)[:180]} host={host}")
