# ムンドは監査済みHTML全文をコピー。他5サイトは従来どおり既存の<head>を保持します。
import os
import shutil
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
shutil.copyfile(os.path.join(ROOT,'src','mundo-audited','index.html'),os.path.join(ROOT,'index.html'))
print('deployed',os.path.join(ROOT,'index.html'))
PAIRS=[('all/index.html','gen/lol-codex.html'),('jax/index.html','jax-codex.html'),('cho/index.html','cho-codex.html'),('nasus/index.html','nasus-codex.html'),('items/index.html','items/item-codex.html')]
for dst,src in PAIRS:
    dst=os.path.join(ROOT,dst); src=os.path.join(ROOT,'src',src)
    o=open(dst,encoding='utf-8').read(); h=o[:o.index('<body>')+len('<body>\n')]
    open(dst,'w',encoding='utf-8').write(h+open(src,encoding='utf-8').read()+'\n</body></html>\n')
    print('deployed',dst)
