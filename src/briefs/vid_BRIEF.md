# Task: integrate a YouTube matchup video (auto-transcribed Japanese, noisy) into our champion guides — fact-checked

Base dir: <repo>/src/
The user (LoL beginner aiming for Gold; "never teach me anything wrong") shared videos about how to play against a champion. Videos may be from older patches: the base ideas are probably sound, but item effects / numbers may have changed. Current patch 26.19 (Sept 2026).

Transcripts are auto-generated: champion/skill names are garbled (e.g. "9" = Q, "93" = Q3, "米/4ネ/夜根" = ヨネ, "イ追い/イオい" = イラオイ, "8ロックス" = エイトロックス, "バルス" = ヴァルス, "より/オリック" = ヨリック, "眼/眼光" = gank, "王険" = ルインドキング ブレード, "近剣" = エクスキューショナー コーリング).

## Inputs
- Your transcript(s): vid/<file> (given in your task).
- Current entries (already fact-checked; keep their facts unless the wiki shows they are wrong):
  - Mundo app: data2.json → champs[] with slug (fields win, go, trap, core, plan, stance, skills{P..R}{d,c,cd}); plays.json → [slug]{goal[], plays[[situation, action, tag(go|w|no)]]}
  - Jax app: jax/jax_final.json → [slug] {stance, memo, win, combos, goal, plays, core, plan, trap, go, skills{X:{c}}}
  - Generic app: gen/champs_v2.json → array, find by id (fields key, summary, strengths, weaknesses, spike, plan, vs[{do,why}], aim[{when,do}], trap, skills{X:{n,cd,what,means,tip,cc}})
  - tips/tips.json → {id: one-line "ひとこと"}
  - buy.json → {id: {mundo, jax, gen}} counter-item lines (see the Yone entry as the model).
- Model of what was done for Yone (for style): compare data2.pre_yone.json vs data2.json, plays.pre_yone.json vs plays.json, gen/champs_v2.pre_yone.json vs gen/champs_v2.json, buy.json["Yone"].
- Official Japanese item names: dd/latest/data/ja_JP/item.json. Official skill names: dd/latest/data/ja_JP/champion/<Id>.json.

## Steps
1. Extract every concrete claim from the video about playing against the champion: mechanics, timings, cooldowns, power spikes, what to dodge/how, minion blocking, trading windows, wave management, item/boot/rune advice, counter picks, teamfight advice.
2. Verify each mechanical/item claim on https://wiki.leagueoflegends.com/en-us/<Name> (champion) and item pages (WebFetch; ask for verbatim current text + notes + recent patch history). Classify: verified / outdated(changed) / wrong / opinion (strategy that can't be verified — usable if sensible and labelled as advice, never as fact).
3. Decide what improves our entries. Add only what is new or sharper than what we have; fix anything in our current entries the wiki shows is wrong. Keep everything beginner-friendly, polite Japanese (です・ます), explain jargon in parentheses the first time in a field. Mundo app: from Dr. Mundo's view (Mundo is a tank; his kit: Q bonesaw skillshot blocked by minions, W stores damage and heals if recast hits a champion, E empowered AA/AA reset, R heal; passive blocks one immobilizing CC). Jax app: Jax's view (E dodges basic attacks and on-hit abilities, 25% less AoE damage; Q jumps to any unit; W AA reset). Generic: any champion.
4. Counter-item box ("buy"): only items whose CURRENT effect you verified. Mundo = tank build; Jax = fighter (own core first unless the item is crucial); gen = by role.

## Output: vid/out_<id>.json
{
 "id": "<Riot id e.g. Aatrox>", "slug": "<mundo/jax slug e.g. aatrox>",
 "mundo": {"set": {"win": "...", "go": "...", "skills.Q.c": "...", ...}, "plays": [[...],...] or null (full replacement list, 4–7 items), "goal": [...] or null},
 "jax": {"set": {"memo": "...", "skills.E.c": "...", ...}, "plays_add": [[...]]},
 "gen": {"set": {"key": "...", "trap": "...", "spike": "...", "skills.W.tip": "...", ...}, "vs": [...] or null (full replacement list, 3–6), "aim": [...] or null},
 "tip": "new ひとこと (≤ 80 chars) or null",
 "buy": {"mundo": "...", "jax": "...", "gen": "..."} or null,
 "report": [{"claim":"video claim (Japanese, short)","status":"verified|outdated|wrong|opinion","note":"Japanese, one line: what's actually true now","evidence":"URL + verbatim quote"}]
}
Only include fields you change. Do not touch combos. Keep each text field under ~160 Japanese characters.
Reply ONLY: output path, number of claims by status, and the 3 most important corrections (one line each).
