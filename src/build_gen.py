import json,sys; sys.path.insert(0,'.')
from links import links
CS=json.load(open('cs/cs_all.json')); TIPS=json.load(open('tips/tips.json')); BUY=json.load(open('buy.json')); SCALE=json.load(open("scale/scale.json")); DMG=json.load(open("dmg/dmg.json")); GW={k:{"lv":v["lv"],"why":v["why"]} for k,v in json.load(open("gw/gw.json")).items()}
C=json.load(open('gen/champs_v2.json'))
for c in C: c.update(links(c['id'])); c['cs']=CS[c['id']]['cs']; c['tip1']=TIPS.get(c['id'],''); c['gw']=GW.get(c['id']); c['buy']=BUY.get(c['id'],{}).get('gen',''); c['sc']=SCALE.get(c['id']); c['lg']=c['id'].lower(); c['dmg']=DMG.get(c['id'])
g=open('gen/template_all.html').read()
open('gen/lol-codex.html','w').write(g.replace('__DATA__', json.dumps(C, ensure_ascii=False).replace('</','<\\/')).replace('__IMG__', open('gen/img.json').read()))
print('built gen')
