import json,sys
sys.path.insert(0,'.')
from links import links
CS=json.load(open("cs/cs_all.json")); TIPS=json.load(open("tips/tips.json")); BUY=json.load(open("buy.json")); SCALE=json.load(open("scale/scale.json")); DMG=json.load(open("dmg/dmg.json")); GW={k:{"lv":v["lv"],"why":v["why"]} for k,v in json.load(open("gw/gw.json")).items()}; EN=json.load(open("en_names.json")); IDS={k.lower():k for k in EN}
d=json.load(open('data2.json')); meta=json.load(open('ddmeta.json'))
J=json.load(open('nasus/nasus_final.json')); WR=json.load(open('nasus/wr.json'))
G={c['id']:c for c in json.load(open('gen/champs_v2.json'))}
def tier(w):
    if w is None: return 'nodata'
    return 'hard' if w<47 else 'even' if w<51 else 'fav' if w<54 else 'fav2'
champs=[]
src=[c for c in d['champs'] if c['slug']!='nasus']
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
    e.update(links(IDS.get(s,"MonkeyKing"))); e['cs']=CS[IDS.get(s,'MonkeyKing')]['cs']; e['tip1']=TIPS.get(IDS.get(s,'MonkeyKing'),''); e['gw']=GW.get(IDS.get(s,'MonkeyKing')); e['buy']=BUY.get(IDS.get(s,'MonkeyKing'),{}).get('jax',''); e['sc']=SCALE.get(IDS.get(s,'MonkeyKing')); e['lg']=IDS.get(s,'MonkeyKing').lower(); e['dmg']=DMG.get(IDS.get(s,'MonkeyKing'))
    champs.append(e)
basics=[
 ["P（パッシブ）","ライフスティール（通常攻撃のダメージの一部で体力を回復）が付きます（レベルで10〜20%）。"],
 ["Q","次の通常攻撃（10秒以内）を強化し、射程+50と追加の物理ダメージを与えます。攻撃のタイマーもリセットします。この強化攻撃でとどめを刺すと、Qのダメージが永久に増えます（通常4、チャンピオン・大型ミニオン・大型モンスターは10）。"],
 ["W","相手チャンピオン1体に5秒間、時間とともに強くなるスロウ（最大47〜95%）と攻撃速度の低下を与えます。射程700。"],
 ["E","指定した範囲（半径400）に5秒間の炎を出し、魔法ダメージを与え続け、範囲内の敵の物理防御を30〜50%下げます。射程650。"],
 ["R","15秒間、体力・物理防御・魔法防御が増えて体が大きくなり、周りの敵に最大体力に応じた魔法ダメージを与え続けます。R中はQの待ち時間が半分になります。"],
 ["強み","時間とともにQのスタックが溜まり、終盤ほど強くなります。Wは近接・通常攻撃型の相手を大きく弱らせます。"],
 ["弱み","序盤はダメージが低く、遠くから削ってくる相手に弱いです。OP.GGの勝率では、ブラッドミア・アカリ・ヴェイン・トリンダメアなどを苦手にしています。"],
]
me={}
jj=json.load(open('dd/latest/data/ja_JP/champion/Nasus.json'))['data']['Nasus']
names=[jj['passive']['name']]+[s['name'] for s in jj['spells']]; cds=[None]+[s['cooldownBurn'].replace('/',' / ') for s in jj['spells']]
gs=[{"shape":"passive"},{"shape":"buff"},{"shape":"unit","range":700},{"shape":"circle","range":650,"radius":400},{"shape":"self","radius":400}]
for k,n,cd,g in zip('PQWER',names,cds,gs):
    me[k]={"name":n,"cd":cd or "なし（常時効果）","g":{**{"shape":None,"range":None,"width":None,"radius":None,"angle":None,"speed":None,"cast":None},**g}}
gloss=[x for x in d['gloss'] if x[0] not in ('重傷','最大HP割合ダメージ')]
gloss+= [["重傷","回復量を減らす効果です。回復の多い相手には「エクスキューショナー コーリング」などで付けます"],
 ["on-hit効果","通常攻撃が当たった時に発動する追加効果のことです。on-hit効果が乗るスキルは、ジャックスのEで回避できます"],
 ["スタン","移動も攻撃もスキルもできなくなる妨害です"]]
data={"champs":champs,"basics":basics,"gloss":gloss,"me":me,"meInfo":{"key4":"0075","slug":"nasus","name":"ナサス"}}
img=json.load(open('img.json')); gi=json.load(open('gen/img.json')); img['nasus']=gi['Nasus']; img.pop('jax',None) if False else None
img={k:v for k,v in img.items() if k in {c['slug'] for c in champs}|{'nasus'}}
t=open('template_nasus.html').read()
open('nasus-codex.html','w').write(t.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')).replace('__IMG__',json.dumps(img)))
print('built',len(champs))
