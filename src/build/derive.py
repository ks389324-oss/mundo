# LoLalytics の対面別ページ（build/raw.json）から、対面画面の「データ上の買い方」欄を作ります。
# 使い方: src フォルダで  python3 build/derive.py  → build/build.json と build/icons.json
import json, base64, io, os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = json.load(open(os.path.join(HERE, 'raw.json')))
MIN = 50  # これ未満の試合数の項目は「データ不足」として扱う

BASE_START = 'ドラン ヘルム'
BASE_BOOTS = 'スイフトネス ブーツ'
BASE_FIRST = {'心の鋼', 'ワーモグ アーマー'}
BASE_4TH = 'タイタン ハイドラ'
NORMAL_3RD = {'タイタン ハイドラ', '心の鋼', 'ワーモグ アーマー'}
GW_ITEMS = {'ソーンメイル', 'モータル リマインダー'}  # 重傷を付けられる完成品（このデータに出てくるもの）


def slot_word(n):
    if n <= 3: return '早め（コア3個目まで）'
    if n == 4: return '中盤（4個目）'
    return '装備が揃う頃（5〜6個目）'


out = {}
for slug, r in RAW.items():
    tot = r['games']
    sh = lambda g: round(100 * g / tot) if tot else 0
    e = {'url': r['url'], 'patch': r['patch'], 'rank': r['rank'], 'games': tot}
    st = r['start']
    if st['games'] >= MIN:
        e['start'] = {'items': st['items'], 'games': st['games'], 'share': sh(st['games']),
                      'diff': BASE_START not in st['items']}
    else:
        e['start'] = None
    c = r['core']
    first, boots, third = (c + [None, None, None])[:3]
    e['first'] = ({'name': first['name'], 'games': first['games'], 'share': sh(first['games']),
                   'diff': first['name'] not in BASE_FIRST} if first and first['games'] >= MIN else None)
    # いつもと違うブーツは、この対面の1割以上で買われている時だけ「推奨」として出す
    e['boots'] = ({'name': boots['name'], 'games': boots['games'], 'share': sh(boots['games']),
                   'diff': boots['name'] != BASE_BOOTS}
                  if boots and boots['games'] >= MIN and (boots['name'] == BASE_BOOTS or sh(boots['games']) >= 10) else None)
    early = []
    if third and third['games'] >= MIN and third['name'] not in NORMAL_3RD and third['name'] not in GW_ITEMS:
        early.append({'slot': 3, 'name': third['name'], 'games': third['games']})
    top4 = max(r['item4'], key=lambda x: x['games']) if r['item4'] else None
    if top4 and top4['games'] >= MIN and top4['name'] != BASE_4TH and top4['name'] not in GW_ITEMS:
        early.append({'slot': 4, 'name': top4['name'], 'games': top4['games']})
    e['early'] = early
    # 重傷アイテム：どの枠で何試合買われているか
    slots = []
    if third and third['name'] in GW_ITEMS:
        slots.append((3, third['name'], third['games']))
    for n, k in ((4, 'item4'), (5, 'item5'), (6, 'item6')):
        for x in r[k]:
            if x['name'] in GW_ITEMS:
                slots.append((n, x['name'], x['games']))
    gtot = sum(g for _, _, g in slots)
    if slots and gtot >= 30:
        main = max(slots, key=lambda s: s[2])
        e['gwbuy'] = {'name': main[1], 'slot': main[0], 'when': slot_word(main[0]), 'games': gtot,
                      'slots': [{'slot': s, 'games': g} for s, n, g in slots if n == main[1]]}
    else:
        e['gwbuy'] = {'name': None, 'games': gtot}
    out[slug] = e

json.dump(out, open(os.path.join(HERE, 'build.json'), 'w'), ensure_ascii=False, indent=1)

# アイコン（items/data.json にある物はそこから、無い物は Data Dragon の画像から）
names = set()
for e in out.values():
    for k in ('start',):
        if e[k]: names |= set(e[k]['items'])
    for k in ('first', 'boots'):
        if e[k]: names.add(e[k]['name'])
    names |= {x['name'] for x in e['early']}
    if e['gwbuy']['name']: names.add(e['gwbuy']['name'])
names |= {BASE_START, BASE_BOOTS, BASE_4TH} | BASE_FIRST
idata = {x['name']: x['ic'] for x in json.load(open(os.path.join(HERE, '..', 'items', 'data.json')))['items']}
EXTRA = {'ドラン シールド': '1054.png', 'ドラン ヘルム': '1120.png', '体力ポーション': '2003.png'}
icons = {}
for n in sorted(names):
    if n in idata:
        icons[n] = idata[n]
    elif n in EXTRA:
        im = Image.open(os.path.join(HERE, 'img', EXTRA[n])).convert('RGB').resize((48, 48), Image.LANCZOS)
        b = io.BytesIO(); im.save(b, 'WEBP', quality=80)
        icons[n] = 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
    else:
        raise SystemExit('icon missing: ' + n)
json.dump(icons, open(os.path.join(HERE, 'icons.json'), 'w'), ensure_ascii=False)
print('derived', len(out), 'icons', len(icons))
