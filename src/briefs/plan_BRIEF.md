# Task: 「この対面の方針」カード（ムンドTOP対面帳）

Base dir: /home/claude/mundo/src/
User = LoL beginner, Dr. Mundo TOP. He plays best when he picks ONE plan per matchup and sticks to it: 立ち回り（方針）、立ち位置（距離）、入るタイミング、押し引き（いつ前に出る／いつ引く）. He reads this card at champ select. Short, concrete, things he can SEE in game. Patch 26.19. User insists「間違ったことを書かない」.

Example of the kind of thinking he wants (Sett): 「Eの射程（450）の端に立って空振りを誘い、外したらAA→E→AAで短く殴って下がる。パッシブがある時はEのスタンを防げるので少し強気にCSを取り、無い時はEの射程外＋ミニオンと自分でセトを挟まない。」

## Output per champion
```
"<en>": {
  "rule": "徹底する方針。1文、です・ます調、15〜35字（例：Eを空振りさせた時だけ短く殴ります）",
  "pos": "基本の立ち位置・距離。20〜50字。射程の数字を使うなら data2 の skills[*].g.range / danger/ar.json の値だけ",
  "pas": "ムンドのパッシブ（行動不能を1回防ぐ。CD 60〜15秒）がある時とない時で、立ち位置や強気度をどう変えるか。20〜55字。相手に、パッシブで防げる重要な行動不能スキルが無ければ null",
  "go": ["入るタイミング＝見える合図→やること。1〜2個、各15〜40字"],
  "back": ["引く・付き合わない判断＝見える合図→やること。1〜2個、各15〜40字"],
  "later": "Lv6やコア完成で方針が変わるなら、その一言（15〜40字）。変わらなければ null"
}
```
Also `"_ev": {"<en>":"English: fields used, wiki URLs, uncertainty"}`.

## Sources & rules
1. TRUSTED (already fact-checked): `data2.json` champs[] by "en" (skills, stance, core, plan, trap, go, win, pun), `trade/trade.json`, `danger/danger.json` (警戒スキル・避け方, audited), `plays.json` (by slug), `danger/ar.json` (attack ranges). Your card is a SUMMARY/plan built from these — it must not contradict any of them (stance phases, ショート/ロング, which skill to bait, etc.).
2. Mundo's passive (Wiki https://wiki.leagueoflegends.com/en-us/Dr._Mundo): blocks the next IMMOBILIZING effect (stun, root, airborne incl. knock-ups/knockbacks/pulls, fear, charm, taunt, suppression). Does NOT block slow, silence, blind, grounded, damage. Only claim it blocks a specific skill if that skill's CC is one of these (check the champ's wiki page if data2 doesn't say the CC type).
3. Anything not in the trusted files must be verified on the wiki with WebFetch, or left out. No memory-based numbers. Avoid 絶対/必ず.
4. Mundo kit: Q＝遠距離の骨ノコ（射程1050）、AA→E→AA が基本の短いトレード、W＝受けたダメージの一部を回復に変える、R＝大回復. 
5. です・ます調、初心者向け。専門用語は（ ）で一言説明。Skill keys as "E" "W".

Write `plan/out<N>.json` for ids in `danger/ids<N>.json`. Reply ONLY: path, count, champs you were unsure about (one line each).
