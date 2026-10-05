# 各ビルド結果を、公開用 index.html（<head> 部分は既存のものを保持）に差し込みます。
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIRS=[('index.html','mundo-codex.html'),('all/index.html','gen/lol-codex.html'),('jax/index.html','jax-codex.html'),('cho/index.html','cho-codex.html'),('items/index.html','items/item-codex.html')]
for dst,src in PAIRS:
    dst=os.path.join(ROOT,dst); src=os.path.join(ROOT,'src',src)
    o=open(dst,encoding='utf-8').read(); h=o[:o.index('<body>')+len('<body>\n')]
    open(dst,'w',encoding='utf-8').write(h+open(src,encoding='utf-8').read()+'\n</body></html>\n')
    print('deployed',dst)
