---
type: open-question
sweep_date: 2026-05-30
sweep_sha: 0317c56
section_index: 9
global_index: 16
pass3_verdict: unknown
overlap_tag: RESTATEMENT
---

# What is the therapeutic dose range for each load-bearing compound in the medicinal-mushroom-complement track (cordycepin, GLPP, ergothioneine, eritadenine, erinacines, PSK, inotodiol, astilbin)?

9. **What is the therapeutic dose range for each load-bearing compound in the medicinal-mushroom-complement track (cordycepin, GLPP, ergothioneine, eritadenine, erinacines, PSK, inotodiol, astilbin)?** (Gates all Phase 7 follow-ups.) (source: medicinal-mushroom-complement-track.md §"Phase 7 follow-ups" #7)

> **Claude review — Confirmed.** `[OVERLAP: RESTATEMENT]` `medicinal-mushroom-complement-track.md` Phase 7 follow-up #7 explicitly asks for therapeutic dose grounding across cordycepin, GLPP, ergothioneine, eritadenine, erinacines, PSK, inotodiol, astilbin, and related compounds. This is necessary because the page’s Real Mushrooms example shows that product-content claims can undershoot mechanism-relevant cordycepin doses by 25–150×.

---

## ✓ Actioned 2026-06-01 (do the work — background dose-range scan spawned)

RESTATEMENT of [`medicinal-mushroom-complement-track.md` Phase 7 follow-up #7](../../wiki/medicinal-mushroom-complement-track.md). Rather than fast-close, Brian chose to do the work: spawned a **background multilingual subagent** (Opus) to scan the therapeutic dose range + product-delivery gap for all 8 load-bearing compounds (cordycepin, GLPP, ergothioneine, eritadenine, erinacines, PSK, inotodiol, astilbin), querying Chinese/Japanese sources with traditional-name framing (虫草素, 灵芝, 麦角硫因, 香菇, 猴头菇, 云芝/クレスチン, 桦褐孔菌, 落新妇苷/土茯苓) and two-model translation cross-check on dose numbers. The canonical frame: the cordycepin 25–150× product-undershoot — does any compound share that gap?

**Subagent reports only (no file edits).** Its dose-range table + product-gap analysis will be reviewed with Brian and landed into `medicinal-mushroom-complement-track.md` at **Item 24** (auto-appended review step, processed after Item 22 in normal walkthrough order — subagent completion is information, not authorization to jump ahead). The disposition of THIS item (do the work via background scan) is decided + initiated; the content landing is tracked at Item 24.
