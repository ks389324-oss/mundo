import json, urllib.parse
EN=json.load(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'en_names.json')))
FIX={"Dr. Mundo":"Dr.Mundo","Nunu & Willump":"Nunu Willump"}
def links(ddid):
    n=EN[ddid]; n=FIX.get(n,n)
    return {"lz":"wukong" if ddid=="MonkeyKing" else ddid.lower(), "op":ddid.lower(),
            "wk":urllib.parse.quote_plus("Champion/"+n, safe="")}
