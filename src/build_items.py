import json
d=json.load(open('items/data.json'))
t=open('items/template_items.html').read()
open('items/item-codex.html','w').write(t.replace('__N__',str(len(d['items']))).replace('__DATA__',json.dumps(d,ensure_ascii=False).replace('</','<\\/')))
print('built items',len(d['items']))
