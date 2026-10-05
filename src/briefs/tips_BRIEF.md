# Task: fact-check and correct user-supplied one-line matchup tips (Japanese)

The user (LoL beginner aiming for Gold; insists "don't teach me anything wrong") pasted one-line tips per TOP champion, probably from another AI. We will show them on each champion page. Many are right; some are wrong or outdated (e.g. Urgot "プレスアタック" is a rune, not Urgot's kit). Patch 26.19, Sept 2026.

Input: tips/in<N>.json (base dir <repo>/src/). Each {name,id,text}.
Trusted, already fact-checked data: gen/champs_v2.json (array; find by id; fields summary/strengths/weaknesses/vs/aim/trap/plan/skills{n,cd,what,means,tip,cc}). Official Japanese item names: dd/latest/data/ja_JP/item.json.

For each tip, check EVERY claim:
- against champs_v2.json first; if not covered there, verify on https://wiki.leagueoflegends.com/en-us/<Name> (or Template:Data_<Name>/<Ability_Name>, or the item page) with WebFetch asking for verbatim text + notes.
- Things to be especially careful about: skill keys/names, whether a skillshot is blocked by minions ("最初に当たった敵" = blocked; "passes through" = not), whether an item can cleanse/counter something (e.g. QSS vs Mordekaiser R, blind removal), CD claims ("長い"), level spikes, item names (must be official Japanese names; "バミシンダー" → official name), exaggerations presented as rules ("絶対", "必須", "全て") when the data doesn't support them.
Then write a corrected version:
- Keep the user's wording and intent where correct. Fix or remove wrong parts. Do not add new advice beyond what is needed to replace a wrong part (sourced from champs_v2.json).
- Polite Japanese (です・ます), ≤ 90 characters, beginner-friendly; explain jargon in parentheses on first use if unclear (e.g. 重傷（回復量を減らす効果）).

Output tips/out<N>.json: array of {"id","name","orig","fixed","verdict":"ok|fixed","changes":"日本語で、何をなぜ直したか1〜2文（okなら空）","evidence":"English: what you checked + URL"}.
Reply ONLY: file path, counts ok/fixed, and list of fixed ids with one-line reason each.
