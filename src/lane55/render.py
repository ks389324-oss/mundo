#!/usr/bin/env python3
"""ムンドTOP対面帳（全55体）を作る。入力: lane55/cards/<slug>.json（55体の照合済みカード）、high8.json、stats6.json。出力: src/mundo-codex.html（deploy.py が index.html に反映）"""
import json, os, html, sys
S = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(S)
REPO = SRC
D2L = json.load(open(f'{REPO}/data2.json'))['champs']
ORDER = [c['slug'] for c in D2L]
SIX = {'garen', 'darius', 'mordekaiser', 'aatrox', 'ornn', 'sett'}
IMG = json.load(open(f'{REPO}/img.json'))
D2 = {c['slug']: c for c in json.load(open(f'{REPO}/data2.json'))['champs']}
FINAL = os.environ.get('FINAL', '_r4')
STATS = json.load(open(f'{S}/stats6.json'))
SHOP = {}
PREV = {s: ORDER[i-1] for i, s in enumerate(ORDER)}
NEXT = {s: ORDER[(i+1) % len(ORDER)] for i, s in enumerate(ORDER)}
e = lambda s: html.escape(str(s)) if s is not None else ''

def load(slug):
    p = f'{S}/cards/{slug}.json'
    return (json.load(open(p)), True) if os.path.exists(p) else (None, False)

def isnew(c, path):
    return ' <span class="new">新規</span>' if path in set(c.get('new') or []) else ''

def ruler(c):
    pts = [{'v': 125, 'label': 'ムンドのAA', 'kind': 'mundo'}] + (c.get('ruler') or []) + [{'v': 1050, 'label': 'ムンドのQ', 'kind': 'mundo'}]
    mx = max(1050, max(p['v'] for p in pts))
    pts = sorted(pts, key=lambda p: p['v'])
    rows = ''.join(f'<div class="rr k-{e(p.get("kind","info"))}{" uc" if p.get("unconfirmed") else ""}"><span class="rl">{e(p["label"])}{"（未確定）" if p.get("unconfirmed") else ""}</span><span class="rb"><i style="width:{p["v"]/mx*100:.1f}%"></i></span><span class="num">{e(p["v"])}</span></div>' for p in pts)
    return f'<div class="rul" aria-label="距離の比較">{rows}</div>'

def shop_html(sh):
    if not sh:
        return '<div class="shop"><p class="mute">ルーン・買い物：統計の取得待ち</p></div>'
    r = sh.get('runes', {})
    changed = r.get('status') == '変更'
    rows = [f'<div class="srow{" alert" if changed else ""}"><span class="sk2">ルーン</span><span>{"<b>変更：</b>" if changed else ""}{e(r.get("short") or r.get("text"))}</span></div>']
    det = []
    if r.get('considered') is not None or r.get('reason'):
        cons = ''.join(f'<li>{e(x.get("slot"))}：{e(x.get("from"))} → {e(x.get("to"))}　{e(x.get("idea"))}<br><span class="mute">判定：{e(x.get("verdict"))}</span></li>' for x in r.get('considered') or [])
        det.append(f'<li><b>ルーン</b>：{e(r.get("base"))}<br>{e(r.get("reason"))}<ul class="sub2">{cons}</ul></li>')
    else:
        det.append(f'<li><b>ルーン</b>：{e(r.get("text"))}</li>')
    fb = sh.get('first_back')
    if fb:
        if fb.get('tiers'):
            tr = ''.join(f'<li><b class="g">{e(x.get("gold"))}</b> {e(x.get("buy"))}<span class="bs">{e(x.get("basis"))}</span></li>' for x in fb['tiers'])
            rows.append(f'<div class="srow"><span class="sk2">初回帰還</span><ul class="tiers">{tr}</ul></div>')
            det.append('<li><b>初回帰還</b>：' + ''.join(f'{e(x.get("gold"))}：{e(x.get("buy"))}（{e(x.get("why"))}／根拠：{e(x.get("basis"))}）<br>' for x in fb['tiers']) + f'<span class="mute">{e(fb.get("note"))}</span></li>')
        else:
            rows.append(f'<div class="srow"><span class="sk2">初回帰還</span><span>{e(fb.get("short") or fb.get("text"))}</span></div>')
            det.append(f'<li><b>初回帰還</b>：{e(fb.get("text"))}</li>')
    b = sh.get('boots')
    if b:
        rows.append(f'<div class="srow"><span class="sk2">ブーツ</span><span>{e(b.get("short") or b.get("text"))}</span></div>')
        if b.get('base'):
            sw = ''.join(f'<li>{e(x.get("when"))} → <b>{e(x.get("to"))}</b>　<span class="mute">{e(x.get("why"))}</span></li>' for x in b.get('switch') or [])
            det.append(f'<li><b>ブーツ</b>：{e(b["base"].get("name"))}（{e(b["base"].get("why"))}）<ul class="sub2">{sw}</ul><span class="mute">{e(b.get("note"))}</span></li>')
        else:
            det.append(f'<li><b>ブーツ</b>：{e(b.get("text"))}</li>')
    c1 = sh.get('core1')
    if c1:
        rows.append(f'<div class="srow"><span class="sk2">1つ目</span><span>{e(c1.get("short") or c1.get("text"))}</span></div>')
        det.append(f'<li><b>1つ目</b>：{e(c1.get("text"))}</li>')
    basis = '統計の集計パッチは26.20（16.20）です。最新パッチ26.21の統計ではありません。' + (sh.get('basis') or '')
    return '<div class="shop">' + ''.join(rows) + f'<details class="sdet"><summary>買い物の根拠</summary><ul>{"".join(det)}</ul><p class="sb">{e(basis)}</p></details></div>'

def items(c, key, lab_if='if'):
    blk = c.get(key) or {}
    lis = []
    for i, it in enumerate(blk.get('items') or []):
        lis.append(f'<li><span class="if">{e(it.get(lab_if))}</span><span class="do">→ {e(it.get("do"))}{isnew(c, f"{key}.items[{i}]")}</span></li>')
    return '<ul class="act2">' + ''.join(lis) + '</ul>'

def champ(slug):
    c, audited = load(slug)
    d = D2[slug]
    if c is None:
        return f'<section class="champ" id="c-{slug}" hidden><p class="mute">{e(d["jp"])}：執筆中</p></section>'
    im = IMG[slug]
    L = STATS.get(slug, {}).get('lolalytics') or {'wr': d['wr'], 'games': d['games'], 'patch': '26.19'}
    st = ' → '.join(f'{s["s"]}（{s["when"]}）' for s in d['stance'])
    sm = c['sum']
    sumrows = ''.join(f'<div class="r {k}"><span class="tag">{lab}</span><span>{e(sm.get(k))}</span></div>'
                      for k, lab in (('stand', '立つ'), ('go', 'CSに出る'), ('cs', 'CS'), ('back', '下がる'), ('hit', '殴る')))
    s = c.get('stand') or {}
    watch = ''.join(f'<li><span class="when">{e(w.get("k"))}{(" " + str(w.get("range"))) if w.get("range") else ""}</span><span>{e(w.get("why"))}</span></li>' for w in s.get('watch') or [])
    P3 = s.get('positions') or {}
    pos3 = ('<div class="pos3">' + ''.join(f'<div class="p {k}"><div class="h">{lab}</div><p>{e(P3.get(k))}</p></div>' for k, lab in (('normal','普段の位置'),('lasthit','ラストヒットの瞬間'),('danger','危険な時'))) + '</div>') if P3 else ''
    PV = s.get('passive_vs') or {}
    pvs = (f'<div class="pvs"><div><b>パッシブで防げる</b>{e(PV.get("blocks"))}</div><div><b>防げない</b>{e(PV.get("not"))}</div></div>') if PV else ''
    cs = c.get('cs') or {}
    opts = ''.join(f'<div class="opt{" no" if k=="skip" else ""}"><div class="h"><span>{lab}</span>{sub}</div><p>{e(cs.get(k))}{isnew(c, "cs."+k)}</p></div>'
                   for k, lab, sub in (('aa', 'AA', 'で取る'), ('e', 'E', 'で取る'), ('q', 'Q', 'で取る'), ('skip', '捨てる', '')))
    t = c.get('trade') or {}
    sk = c.get('skills') or {}
    U = c.get('unconfirmed') or []
    unc = ('<details><summary>未確認の点（' + str(len(U)) + '件）</summary><div class="dbody"><ul class="ul2">' + ''.join(f'<li>{e(x)}</li>' for x in U) + '</ul></div></details>') if U else ''
    RM = t.get('realm') or {}
    realm = (f'<div class="realm"><div class="h">R（異空間）に入れられた時</div><p><b>勝てる時：</b>{e(RM.get("win"))}</p><p><b>負けている時：</b>{e(RM.get("lose"))}</p><p class="mute">{e(RM.get("note"))}</p></div>') if RM else ''
    nt = t.get('no_trade') or []
    notrade = ('<div class="nt"><div class="h">CSには出てよいが、殴らない時</div><ul>' + ''.join(f'<li>{e(x)}</li>' for x in nt) + '</ul></div>') if nt else ''
    skrows = ''.join(f'<div class="skr"><img src="{im[k]}" alt="{k}"><div><b>{k}</b> {e(sk.get(k))}</div></div>' for k in 'PQWER' if sk.get(k))
    ch = c.get('changed') or []
    lg = (c.get('_log3') or []) if isinstance(c.get('_log3'), list) else []
    lgrows = ''.join(f'<tr><td><code>{e(x.get("path"))}</code></td><td>{e(x.get("issue"))}</td><td>{e(x.get("fix"))}</td><td class="mute">{e(x.get("src"))}</td></tr>' for x in lg if isinstance(x, dict))
    chrows = ''.join(f'<tr><td><code>{e(x.get("path"))}</code></td><td>{e(x.get("before"))}</td><td>{e(x.get("after"))}</td><td>{e(x.get("why"))}<br><span class="mute">{e(x.get("src"))}</span></td></tr>' for x in ch)
    patch = f'<details class="patch"><summary>パッチの注意あり</summary><p>{e(c["patch"])}</p></details>' if c.get('patch') else ''
    badge = '' if audited else '<span class="chip warn">照合前</span>'
    return f'''<section class="champ" id="c-{slug}" aria-label="{e(d["jp"])}" hidden>
<header class="hero"><img src="{im["c"]}" alt=""><div><h1>{e(d["jp"])} {badge}</h1>
<div class="sub"><span class="chip">{e(st)}</span><span>ムンド勝率 <span class="num">{L["wr"]:.1f}%</span>・<span class="num">{L["games"]:,}</span>試合（LoLalytics・集計パッチ{"26.19" if L.get("patch")=="26.19" else "26.20"}。最新の26.21の統計ではありません）</span></div></div></header>
{patch}
<div class="fv"><div class="sum">{sumrows}</div>
{shop_html(c.get("shop") or SHOP.get(slug))}</div>
<p class="dhead">理由と細かい条件</p>
<div class="grid">
<section class="blk stand s3"><h2><span class="tag">① 立つ</span>普段の立ち位置</h2>{ruler(c)}
{pos3}<ul class="act"><li><span class="when">基本</span><span>{e(s.get("base"))}{isnew(c,"stand.base")}</span></li>
<li><span class="when">近づく</span><span>{e(s.get("step_in"))}{isnew(c,"stand.step_in")}</span></li>
<li><span class="when">近づかない</span><span>{e(s.get("hold_back"))}{isnew(c,"stand.hold_back")}</span></li></ul>
<p class="x"><b>警戒するスキル</b></p><ul class="act w">{watch}</ul>{pvs}</section>
<section class="blk go"><h2><span class="tag">② CSに出る</span>CSに前へ出ていい合図</h2>{items(c,"go")}<p class="x"><b>例外：</b>{e((c.get("go") or {}).get("except"))}</p></section>
<section class="blk back"><h2><span class="tag">③ 下がる</span>下がる合図</h2>{items(c,"back")}<p class="x"><b>追撃をやめる：</b>{e((c.get("back") or {}).get("stop_chase"))}</p></section>
<section class="blk cs"><h2><span class="tag">④ CS</span>この1体をどう取るか</h2><div class="opts">{opts}</div>{('<p class="x cost"><b>捨てるコスト：</b>' + e(cs.get("cost")) + '</p>') if cs.get("cost") else ''}</section>
<section class="blk trade s3"><h2><span class="tag">⑤ 殴る</span>1v1のトレード</h2><div class="steps">
<div class="step"><div class="h">仕掛ける</div>{e(t.get("start"))}</div><div class="step"><div class="h">当てる</div>{e(t.get("hit"))}</div><div class="step"><div class="h">離れる</div>{e(t.get("exit"))}</div></div>
{notrade}{realm}<div class="long"><div class="h">長く殴り合ってよい条件</div>{e(t.get("long"))}</div></section>
</div>
{unc}<details><summary>スキルとCD</summary><div class="dbody">{skrows}</div></details>
<details><summary>既存の攻略から変えた点（{len(ch)}件）</summary><div class="dbody"><div class="tw"><table><tr><th>場所</th><th>変更前</th><th>変更後</th><th>理由・根拠</th></tr>{chrows}</table></div></div></details>
<details><summary>別担当の照合で直した点（{len(lg)}件）</summary><div class="dbody"><div class="tw"><table><tr><th>場所</th><th>問題</th><th>修正</th><th>根拠</th></tr>{lgrows}</table></div></div></details>
<div class="navrow"><button type="button" class="nb" data-go="{PREV[slug]}">← {e(D2[PREV[slug]]['jp'])}</button><button type="button" class="nb" data-go="{NEXT[slug]}">{e(D2[NEXT[slug]]['jp'])} →</button></div>
</section>'''

def high_html():
    p = f'{S}/high8.json'
    if not os.path.exists(p):
        return '<p class="mute">重大8件：照合中</p>'
    H = json.load(open(p))
    out = []
    for h in H:
        ev = ''.join(f'<li>{e(x.get("quote"))} <a href="{e(x.get("url"))}" target="_blank" rel="noopener">Wiki ↗</a></li>' for x in h.get('evidence') or [])
        ed = ''.join(f'<div class="ba"><code>{e(x.get("loc"))}</code><p class="b4"><span>修正前</span>{e(x.get("before"))}</p><p class="af"><span>修正後</span>{e(x.get("after"))}</p></div>' for x in h.get('edits') or [])
        jd = f'<p class="mute">判断を含む部分：{e(h["judgement"])}</p>' if h.get('judgement') and not h.get('judgements') else ''
        fx = ''.join(f'<li>{e(x.get("text"))} <span class="mute">（{e(x.get("quote"))}）</span> <a href="{e(x.get("url"))}" target="_blank" rel="noopener">Wiki ↗</a></li>' for x in h.get('facts') or [])
        jg = ''.join(f'<li>{e(x.get("text"))}<br><span class="mute">理由：{e(x.get("why"))}</span></li>' for x in h.get('judgements') or [])
        if fx or jg:
            jd = f'<div class="fj"><div class="fct"><div class="h">スキル仕様で確定した事実</div><ul>{fx}</ul></div><div class="jdg"><div class="h">実戦上の判断（目安）</div><ul>{jg}</ul></div></div>'
            ev = ''
        c3 = ''.join(f'<div class="ba"><code>{e(x.get("loc"))}</code><p class="b4"><span>前の修正案</span>{e(x.get("before"))}</p><p class="af"><span>今回の修正案</span>{e(x.get("after"))}</p><p class="mute">{e(x.get("why"))}</p></div>' for x in h.get('changes_v3') or [])
        if c3: jd += f'<p class="x"><b>今回さらに直した点</b></p>{c3}'
        out.append(f'<details class="hi"><summary><b>{e(h.get("jp") or h.get("champ"))}</b><span class="chip">{e({"確定":"指摘どおり","一部修正":"修正案を調整","誤指摘":"誤指摘"}.get(h.get("verdict"),h.get("verdict")))}</span><span class="mute">{len(h.get("edits") or [])}か所</span></summary><div class="dbody"><p>{e(h.get("problem"))}</p>{ed}{('<p class="x"><b>根拠</b></p><ul class="evl">' + ev + '</ul>') if ev else ''}{jd}</div></details>')
    return ''.join(out)


def lists_html():
    out_m = []; out_u = []; nm = nu = 0
    for s in ORDER:
        c, _ = load(s); jp = e(D2[s]['jp'])
        m = c.get('major') or []; u = c.get('unconfirmed') or []
        nm += len(m); nu += len(u)
        if m:
            items = ''.join(f'<div class="ba"><code>{e(x.get("path"))}</code><p class="b4"><span>修正前</span>{e(x.get("before"))}</p><p class="af"><span>修正後</span>{e(x.get("after"))}</p><p class="mute">{e(x.get("why"))}</p></div>' for x in m)
            out_m.append(f'<details class="hi"><summary><b>{jp}</b><span class="mute">{len(m)}件</span></summary><div class="dbody">{items}</div></details>')
        if u:
            out_u.append(f'<details class="hi"><summary><b>{jp}</b><span class="mute">{len(u)}件</span></summary><div class="dbody"><ul class="ul2">' + ''.join(f'<li>{e(x)}</li>' for x in u) + '</ul></div></details>')
    return (f'<h2 class="lh">重大な修正（{nm}件）</h2><p class="lead">スキル仕様の誤り、またはムンドが倒される・主力スキルを無駄にする案内を直したものです。</p>' + ''.join(out_m) +
            f'<h2 class="lh">未確認の点（{nu}件）</h2><p class="lead">Wikiや統計で確定できなかった点です。数値は書かず、行動で説明しています。</p>' + ''.join(out_u))

TIER = {'hard': '苦手', 'even': '互角', 'fav': '有利', 'fav2': '大きく有利'}
tpl = open(f'{S}/template.html').read()
groups = ''
for t in ('hard', 'even', 'fav', 'fav2'):
    btns = ''.join(f'<button type="button" class="pk" data-go="{c["slug"]}" data-q="{e(c["jp"])} {e(c["en"]).lower()}"><img src="{IMG[c["slug"]]["c"]}" alt="">{e(c["jp"])}</button>' for c in D2L if c['tier'] == t)
    groups += f'<div class="pg"><p class="pgh">{TIER[t]}</p><div class="pgr">{btns}</div></div>'
body = ''.join(champ(s) for s in ORDER)
out = tpl.replace('__GROUPS__', groups).replace('__CHAMPS__', body).replace('__HIGH__', high_html()).replace('__FIRST__', ORDER[0]).replace('__LISTS__', lists_html()).replace('__HIGHLEAD__', '監査で「重大」とした8件です。修正前は2026年10月23日より前の旧版の文、修正後は別の担当がWikiで照合した文で、55体の本文に反映済みです（29か所すべてを本文と照合し、セトの2か所を追加で反映、ジャックスの1か所を訂正）。')
out = out.replace('<title>ムンドTOP対面帳</title>\n', '', 1)
open(f'{SRC}/mundo-codex.html', 'w').write(out)
st = [load(s) for s in ORDER]
print('ok', sum(1 for x in st if x[0]), 'loaded', sum(1 for x in st if x[1]), 'final')
