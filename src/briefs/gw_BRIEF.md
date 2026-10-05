# Task: which champions should you buy 重傷 (Grievous Wounds) against? (Japanese LoL beginner guide, patch 26.19)

Base dir: <repo>/src/
Inputs:
- gen/champs_v2.json: 173 champions (fact-checked guide). Field id, name, skills{P,Q,W,E,R}{n,what,means,tip}, vs, weaknesses, etc.
- dd/latest/data/ja_JP/champion/<id>.json: Riot official Japanese descriptions (passive.description, spells[].description / tooltip).

Goal: for each of the 173 champions decide whether healing (self-heal, lifesteal/omnivamp built into the kit, or healing allies) is a CORE part of how they win fights, such that an opponent should buy a Grievous Wounds item against them. Only flag champions where the healing is large and central (e.g. Aatrox, Vladimir, Dr. Mundo, Warwick, Soraka, Swain, Sylas, Olaf, Briar, Fiora, Illaoi, Yuumi, Sona — verify each, do not trust this example list). Do NOT flag champions whose healing is minor or only via items/runes, or who only APPLY grievous wounds (e.g. Singed, Varus). Expect roughly 20–40 champions.

Verify each flagged champion's healing mechanic on https://wiki.leagueoflegends.com/en-us/<Name> (WebFetch, ask for which abilities heal and how much) unless it is already explicit in the official Japanese descriptions or champs_v2.json. Use ~1 fetch per uncertain champion; be efficient.

Output gw/gw.json: object keyed by champion id ONLY for flagged champions:
{"lv":"必須級"|"推奨", "why":"何で回復するかを短く（日本語、35字以内、例：Q（ダーキンブレード）の命中とR中の回復量アップ）", "evidence":"English: source + URL"}
- 必須級 = healing is the champion's main way to win fights/sustain (without anti-heal they out-sustain you).
- 推奨 = significant healing that matters in longer fights.
Skill keys and Japanese skill names must match the official data.
Reply ONLY: file path, counts per level, and ids listed per level.
