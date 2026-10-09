import json,sys
sys.path.insert(0,".")
from links import links
CS=json.load(open("cs/cs_all.json")); TIPS=json.load(open("tips/tips.json")); BUY=json.load(open("buy.json")); SCALE=json.load(open("scale/scale.json")); DMG=json.load(open("dmg/dmg.json")); GW={k:{"lv":v["lv"],"why":v["why"]} for k,v in json.load(open("gw/gw.json")).items()}; EN=json.load(open("en_names.json")); IDS={k.lower():k for k in EN}
TRADE=json.load(open("trade/trade.json")); DANGER=json.load(open("danger/danger.json")); AR=json.load(open("danger/ar.json"))
t=open("template.html").read()
d=json.load(open("data2.json")); p=json.load(open("plays.json")); meta=json.load(open("ddmeta.json"))
for c in d["champs"]:
    c.update(p[c["slug"]]); c.pop("pun",None)
    c.update(links(IDS.get(c["slug"],"MonkeyKing"))); c["cs"]=CS[IDS.get(c["slug"],"MonkeyKing")]["cs"]; c["tip1"]=TIPS.get(IDS.get(c["slug"],"MonkeyKing"),""); c["gw"]=GW.get(IDS.get(c["slug"],"MonkeyKing")); c["buy"]=BUY.get(IDS.get(c["slug"],"MonkeyKing"),{}).get("mundo",""); c["sc"]=SCALE.get(IDS.get(c["slug"],"MonkeyKing")); c["lg"]=IDS.get(c["slug"],"MonkeyKing").lower(); c["dmg"]=DMG.get(IDS.get(c["slug"],"MonkeyKing"));
    c["trade"]=TRADE[c["en"]]; c["danger"]=DANGER[c["en"]]; c["ar"]=AR[c["en"]]
    m=meta[c["slug"]]; c["key4"]=m["key"].zfill(4); c["official"]=m["name"]; c["snames"]=dict(zip("PQWER",[m["pname"]]+m["snames"]))
d["mundoAR"]=AR["_mundo"]; mm=meta["drmundo"]; d["mundoInfo"]={"key4":mm["key"].zfill(4)}
for k,n in zip("PQWER",[mm["pname"]]+mm["snames"]): d["mundo"][k]["name"]=n
dj=json.dumps(d,ensure_ascii=False).replace("</","<\\/")
open("mundo-codex.html","w").write(t.replace("__DATA__",dj).replace("__IMG__",open("img.json").read()))
print("built")
