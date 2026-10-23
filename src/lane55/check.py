#!/usr/bin/env python3
"""全55体の機械検査（スキーマ・文字数・ルーンと買い物の整合・詰め替え規則・禁止語）"""
import json, os, sys
S = '/home/claude/mundo/src'
REPO = S
SIX = {'garen', 'darius', 'mordekaiser', 'aatrox', 'ornn', 'sett'}
EXC = {'teemo', 'quinn', 'vayne', 'kennen', 'varus', 'jayce'}
REFILL = {'aatrox', 'ambessa', 'darius', 'fiora', 'jax', 'sett', 'warwick'}
BOOTS = ['ブーツ', 'スチールキャップ', 'マーキュリー']
order = [c['slug'] for c in json.load(open(f'{REPO}/data2.json'))['champs']]

def path(s):
    return f'{S}/lane55/cards/{s}.json'

def texts(o, skip=('changed', '_log', '_log2', '_log3', '_logF', '_rev', '_rev3', 'src', 'new', 'major', 'unconfirmed', '_reflect')):
    if isinstance(o, dict):
        for k, v in o.items():
            if k not in skip:
                yield from texts(v, skip)
    elif isinstance(o, list):
        for v in o:
            yield from texts(v, skip)
    elif isinstance(o, str):
        yield o

problems = {}
missing = []
for s in order:
    p = path(s)
    if not os.path.exists(p):
        missing.append(s); continue
    c = json.load(open(p)); P = []
    for k in ('sum', 'stand', 'go', 'back', 'cs', 'trade', 'skills', 'shop', 'unconfirmed', 'major'):
        if k not in c: P.append(f'欠落:{k}')
    for k in ('stand', 'go', 'cs', 'back', 'hit'):
        v = (c.get('sum') or {}).get(k) or ''
        if not v: P.append(f'sum.{k}空')
        elif len(v) > 42: P.append(f'sum.{k}={len(v)}字')
    pos = (c.get('stand') or {}).get('positions') or {}
    if set(pos) < {'normal', 'lasthit', 'danger'}: P.append('positions不足')
    if not (c.get('stand') or {}).get('passive_vs'): P.append('passive_vs無し')
    nt = (c.get('trade') or {}).get('no_trade') or []
    if not 2 <= len(nt) <= 4: P.append(f'no_trade={len(nt)}')
    if not (c.get('cs') or {}).get('cost'): P.append('cs.cost無し')
    sh = c.get('shop') or {}
    r = sh.get('runes') or {}
    base = r.get('base') or ''
    tiers = (sh.get('first_back') or {}).get('tiers') or []
    if len(tiers) != 4: P.append(f'tiers={len(tiers)}')
    tiertxt = ' '.join((t.get('buy') or '') for t in tiers)
    if s in EXC:
        if 'ビスケット' not in json.dumps(r, ensure_ascii=False): P.append('例外なのにビスケット無し')
    else:
        if '魔法の靴' not in base: P.append('基本ルーンに魔法の靴無し')
        if any(b in tiertxt for b in BOOTS): P.append('魔法の靴なのに初回帰還にブーツ')
    refill = '詰め替え' in tiertxt
    if refill and s not in REFILL: P.append('詰め替えが対象外')
    if s in REFILL and not refill: P.append('詰め替え無し（対象）')
    allt = ' '.join(texts(c))
    for w in ('絶対', '必ず'):
        if w in allt: P.append(f'禁止語:{w}')
    for w in ('最適です', '推奨します', 'が最適', 'を推奨'):
        if w in allt: P.append(f'禁止語:{w}')
    if s == 'ornn' and '約360' in allt: P.append('オーンE未確定値')
    if s == 'mordekaiser' and ('700の端' in allt or '700より少し外' in allt): P.append('モルデE未確定値')
    if P: problems[s] = P
print('missing', missing)
print('problems', len(problems))
for s, P in problems.items(): print(' ', s, P)
