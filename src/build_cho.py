import json,sys
sys.path.insert(0,'.')
from links import links
CS=json.load(open("cs/cs_all.json")); TIPS=json.load(open("tips/tips.json")); BUY=json.load(open("buy.json")); SCALE=json.load(open("scale/scale.json")); DMG=json.load(open("dmg/dmg.json")); GW={k:{"lv":v["lv"],"why":v["why"]} for k,v in json.load(open("gw/gw.json")).items()}; EN=json.load(open("en_names.json")); IDS={k.lower():k for k in EN}
d=json.load(open('data2.json')); meta=json.load(open('ddmeta.json'))
J=json.load(open('cho/cho_final.json')); WR=json.load(open('cho/wr.json'))
G={c['id']:c for c in json.load(open('gen/champs_v2.json'))}
def tier(w):
    if w is None: return 'nodata'
    return 'hard' if w<47 else 'even' if w<51 else 'fav' if w<54 else 'fav2'
champs=[]
src=[c for c in d['champs'] if c['slug']!='chogath']
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
    e.update(links(IDS.get(s,"MonkeyKing"))); e['cs']=CS[IDS.get(s,'MonkeyKing')]['cs']; e['tip1']=TIPS.get(IDS.get(s,'MonkeyKing'),''); e['gw']=GW.get(IDS.get(s,'MonkeyKing')); e['buy']=BUY.get(IDS.get(s,'MonkeyKing'),{}).get('mundo',''); e['sc']=SCALE.get(IDS.get(s,'MonkeyKing')); e['lg']=IDS.get(s,'MonkeyKing').lower(); e['dmg']=DMG.get(IDS.get(s,'MonkeyKing'))
    champs.append(e)
basics=[
 ["P（パッシブ）","ユニット（ミニオン・モンスター・チャンピオン）を倒すたびに、体力とマナが回復します。CSを取るほどレーンで粘れます。"],
 ["Q","指定した地点が約0.6秒後に破裂し、魔法ダメージと1秒の打ち上げ、その後1.5秒の60%スロウを与えます。射程950。遅れて出るので、動いている相手には当たりにくい技です。"],
 ["W","前方の扇形に叫び、魔法ダメージと沈黙（1.6〜2秒、スキルが使えなくなる妨害）を与えます。射程650。移動と通常攻撃は止められません。"],
 ["E","次の3回のAA（6秒以内）が強化され、射程+50と、前方へ直線に飛ぶトゲ（魔法ダメージ・相手の最大体力に応じた追加ダメージ・スロウ）が付きます。AAのタイマーをリセットします。"],
 ["R","対象1体に確定ダメージ（防御で減らないダメージ）を与えるとどめ技です。倒すとスタックが溜まり、最大体力・射程・体の大きさが増えます（ミニオンや中立モンスターからは6スタックまで）。射程175と短く、近づく必要があります。"],
 ["強み","打ち上げ（Q）と沈黙（W）の2つの妨害で、相手の攻めを止められます。Rの確定ダメージで、体力の減った相手を確実に倒せます。スタックが溜まるほど硬くなります。"],
 ["弱み","Qが遅れて出るため、動き回る相手には当たりにくいです。OP.GGの勝率では、グラガス・リヴェン・ブラッドミア・ジェイスなど、序盤から殴り合いや削りが強い相手を苦手にしています。"],
]
me={}
jj=json.load(open('dd/latest/data/ja_JP/champion/Chogath.json'))['data']['Chogath']
names=[jj['passive']['name']]+[s['name'] for s in jj['spells']]; cds=[None]+[s['cooldownBurn'].replace('/',' / ') for s in jj['spells']]
gs=[{"shape":"passive"},{"shape":"circle","range":950,"radius":125,"cast":0.627},{"shape":"cone","range":650,"angle":60,"cast":0.5},{"shape":"buff"},{"shape":"unit","range":175}]
for k,n,cd,g in zip('PQWER',names,cds,gs):
    me[k]={"name":n,"cd":cd or "なし（常時効果）","g":{**{"shape":None,"range":None,"width":None,"radius":None,"angle":None,"speed":None,"cast":None},**g}}
gloss=[x for x in d['gloss'] if x[0] not in ('重傷','最大HP割合ダメージ')]
gloss+= [["重傷","回復量を減らす効果です。回復の多い相手には「エクスキューショナー コーリング」などで付けます"],
 ["on-hit効果","通常攻撃が当たった時に発動する追加効果のことです。on-hit効果が乗るスキルは、ジャックスのEで回避できます"],
 ["スタン","移動も攻撃もスキルもできなくなる妨害です"]]
data={"champs":champs,"basics":basics,"gloss":gloss,"me":me,"meInfo":{"key4":"0031","slug":"chogath","name":"チョ＝ガス"}}
img=json.load(open('img.json')); gi=json.load(open('gen/img.json')); img['chogath']=gi['Chogath']; img.pop('jax',None) if False else None
img={k:v for k,v in img.items() if k in {c['slug'] for c in champs}|{'chogath'}}
t=open('template_cho.html').read()
open('cho-codex.html','w').write(t.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')).replace('__IMG__',json.dumps(img)))
print('built',len(champs))
