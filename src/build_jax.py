import json,sys
sys.path.insert(0,'.')
from links import links
CS=json.load(open("cs/cs_all.json")); TIPS=json.load(open("tips/tips.json")); BUY=json.load(open("buy.json")); SCALE=json.load(open("scale/scale.json")); GW={k:{"lv":v["lv"],"why":v["why"]} for k,v in json.load(open("gw/gw.json")).items()}; EN=json.load(open("en_names.json")); IDS={k.lower():k for k in EN}
d=json.load(open('data2.json')); meta=json.load(open('ddmeta.json'))
J=json.load(open('jax/jax_final.json')); WR=json.load(open('jax/wr.json'))
G={c['id']:c for c in json.load(open('gen/champs_v2.json'))}
def tier(w):
    if w is None: return 'nodata'
    return 'hard' if w<47 else 'even' if w<51 else 'fav' if w<54 else 'fav2'
champs=[]
src=[c for c in d['champs'] if c['slug']!='jax']
mm=meta['drmundo']; gm=G['DrMundo']
src.append({"jp":"ドクター・ムンド","en":"Dr. Mundo","slug":"drmundo",
  "skills":{k:{"d":gm['skills'][k]['what'],"cd":d['mundo'][k]['cd'],"g":d['mundo'][k]['g']} for k in 'PQWER'}})
for c in src:
    s=c['slug']; j=J[s]; w=WR.get(s)
    e={k:c[k] for k in ['jp','en','slug']}
    e['wr']=w[0] if w else None; e['games']=w[1] if w else 0; e['few']=bool(w) and w[1]<150; e['tier']=tier(e['wr'])
    for k in ['stance','memo','win','combos','goal','plays','core','plan','trap','go']: e[k]=j[k]
    e['skills']={}
    for k in 'PQWER':
        sk={x:v for x,v in c['skills'][k].items() if x!='c'}
        sk['c']=j['skills'][k]['c']
        if 'alt' in sk and isinstance(sk['alt'],dict): sk['alt']={x:v for x,v in sk['alt'].items() if x!='c'}
        e['skills'][k]=sk
    m=meta[s]; e['key4']=m['key'].zfill(4); e['official']=m['name']; e['snames']=dict(zip("PQWER",[m["pname"]]+m["snames"]))
    e.update(links(IDS.get(s,"MonkeyKing"))); e['cs']=CS[IDS.get(s,'MonkeyKing')]['cs']; e['tip1']=TIPS.get(IDS.get(s,'MonkeyKing'),''); e['gw']=GW.get(IDS.get(s,'MonkeyKing')); e['buy']=BUY.get(IDS.get(s,'MonkeyKing'),{}).get('jax',''); e['sc']=SCALE.get(IDS.get(s,'MonkeyKing')); e['lg']=IDS.get(s,'MonkeyKing').lower()
    champs.append(e)
basics=[
 ["P（パッシブ）","通常攻撃（AA）を当てるたびにスタックが溜まり（最大8、2.5秒で切れ始めます）、1スタックごとに攻撃速度が上がります。戦う前にミニオンを殴って溜めておくと、最初から速い攻撃で戦えます。"],
 ["Q","敵・味方のユニット（ミニオン・ワードを含む）へ跳びます。敵なら到着時にダメージを与え、チャンピオンなら続けて自動でAAします。味方ミニオンやワードへ跳べば逃げにも使えます。跳んでいる間に他のスキルを使えます。移動スキル封じ（グラウンド）中は使えません。"],
 ["W","次のAAかQに魔法ダメージを上乗せします。AAのタイマーをリセットするので、「AA → すぐW」で素早く2発入ります。AAに使うと射程が少し伸び、途中で止まらなくなります。フィオラのW（受け流し）などのパリィや、スペルシールドには防がれます。"],
 ["E","2秒間、敵の通常攻撃（タワーの攻撃を除く）と、「通常攻撃扱い（on-hit効果が乗る）」のスキルを回避し、範囲スキルのダメージを25%減らします。範囲ではない普通のスキルや飛び道具は避けられません。1秒たつと再発動でき（2秒で自動発動）、周囲（375）の敵にダメージとスタン1秒を与えます。避けた攻撃の数だけダメージが増えます（最大2倍）。"],
 ["R","パッシブ：AAを3回当てるごとに追加魔法ダメージ（発動中は2回ごと）。発動：周囲にダメージを与え、チャンピオンに当たると8秒間、物理防御と魔法防御が上がります。発動の溜め中も移動できます。"],
 ["強み","通常攻撃に頼る相手は、Eで攻撃を空振りさせてから反撃できます。Qで味方ミニオンやワードに跳べるため、逃げ道も作れます。アイテムがそろうとタワーを素早く壊せます（Wの攻撃リセットを使う）。"],
 ["弱み","Eで避けられない遠距離スキルを多く持つ相手（例：クインやティーモのような遠距離の相手や、ブラッドミア・シンジドのような範囲・持続ダメージの相手）には、近づく前に削られます。OP.GGの勝率でもこれらは苦手側に入ります。"],
]
me={}
jj=json.load(open('dd/latest/data/ja_JP/champion/Jax.json'))['data']['Jax']
names=[jj['passive']['name']]+[s['name'] for s in jj['spells']]; cds=[None]+[s['cooldownBurn'].replace('/',' / ') for s in jj['spells']]
gs=[{"shape":"passive"},{"shape":"dash","range":700},{"shape":"buff"},{"shape":"self","radius":375},{"shape":"self","radius":375,"cast":0.25}]
for k,n,cd,g in zip('PQWER',names,cds,gs):
    me[k]={"name":n,"cd":cd or "なし（常時効果）","g":{**{"shape":None,"range":None,"width":None,"radius":None,"angle":None,"speed":None,"cast":None},**g}}
gloss=[x for x in d['gloss'] if x[0] not in ('重傷','最大HP割合ダメージ')]
gloss+= [["重傷","回復量を減らす効果です。回復の多い相手には「エクスキューショナー コーリング」などで付けます"],
 ["on-hit効果","通常攻撃が当たった時に発動する追加効果のことです。on-hit効果が乗るスキルは、ジャックスのEで回避できます"],
 ["スタン","移動も攻撃もスキルもできなくなる妨害です"]]
data={"champs":champs,"basics":basics,"gloss":gloss,"me":me,"meInfo":{"key4":"0024","slug":"jax","name":"ジャックス"}}
img=json.load(open('img.json')); gi=json.load(open('gen/img.json')); img['jax']=gi['Jax']; img.pop('jax',None) if False else None
img={k:v for k,v in img.items() if k in {c['slug'] for c in champs}|{'jax'}}
t=open('template_jax.html').read()
open('jax-codex.html','w').write(t.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')).replace('__IMG__',json.dumps(img)))
print('built',len(champs))
