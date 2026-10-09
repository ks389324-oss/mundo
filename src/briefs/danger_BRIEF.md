# Task: 警戒スキル・避け方・避けた後のトレード（ムンドTOP対面帳）

Base dir: /home/claude/mundo/src/
User = LoL beginner playing Dr. Mundo TOP. Opens this card at champ select / loading screen to know: どのスキルを警戒するか、どう避けるか（立ち位置・距離感）、避けたら（外させたら）ショートかロングか。スキル名だけではピンとこないため、ページ側でアイコン・動画・距離の図を自動で付ける。文章は短く。
Patch 26.19 (Sept–Oct 2026). User insists「絶対に間違ったことを書かない」.

## Output per champion
```
"<en>": {
  "pos": "立ち位置・距離感の一言。です・ます調 20〜45字（例：ミニオンの後ろに立ち、Qの届く距離から削ります）",
  "sk": [  // 警戒スキル 1〜2個（多くても2個）。最も重要なものを先に
    {"k":"P|Q|W|E|R",
     "dodge":"よける|位置|受ける",   // よける＝歩いて避けられる飛び道具・予備動作のある技 / 位置＝立ち位置（ミニオンの陰・横にずれる・距離を取る）で防ぐ / 受ける＝対象指定などで避けられない→W等で受けて耐える
     "how":"避け方・対処。です・ます調 20〜55字。予備動作・目印（ゲージ、構え、エフェクト）があれば書く",
     "t":"ショート|ロング|下がる",  // そのスキルを外させた・使わせた直後にムンドがすること。下がる＝打ち返さず距離を取る
     "then":"その後の具体的な行動。です・ます調 20〜55字（例：CD中にQ→AA→E→AAで殴って下がります）"}
  ]
}
```
Also output `"_ev": {"<en>": "English: data2 fields used + wiki URLs fetched + any uncertainty"}`.

## Sources & rules
1. TRUSTED (already fact-checked): `data2.json` → `champs[]` (find by "en"): skills[*].d / .c / .cd / .g, stance, core, plan, trap, go, win, pun. Also `trade/trade.json` (audited ショート/ロング/避ける by phase) and `plays.json` (by slug). Your entry MUST NOT contradict these. Example: if trade.json says the matchup is ショート in all phases, do not write ロング unless it is specifically about the window right after the key skill whiffed AND data2 supports it (e.g. go says that skill on CD is the time to fight). If unsure, use ショート.
2. Any mechanic not stated in data2.json must be verified with WebFetch on https://wiki.leagueoflegends.com/en-us/<Name> (or Template:Data_<Name>/<Ability name>). Dr. Mundo's own kit: https://wiki.leagueoflegends.com/en-us/Dr._Mundo — e.g. whether his passive (気ままな往診 / Goes Where He Pleases) blocks the specific CC: check the wiki's wording about what it blocks (immobilizing effects) vs. what it does not (e.g. displacements such as knock-ups/pulls/knockbacks, or other CC types). If you cannot verify, do not write it.
3. No memory-based numbers. Avoid absolute words (絶対, 必ず) unless data says so. No percentages/damage numbers unless verified.
4. Skill names: write them as data2 does ("E（引き寄せ）" style is NOT required — the page shows the official name and icon automatically; in how/then just say "E" "W" etc. or a short paraphrase).
5. Mundo terms: Q＝骨ノコ投げ（遠距離）, W＝シールド的にダメージを溜めて回復, E＝強化通常攻撃, AA＝通常攻撃. Basic short trade = AA→E→AA. Keep consistent with data2 "pun"/"go".
6. Japanese: 初心者向け、です・ます調。専門用語は（ ）で一言説明。
7. Prefer what a beginner can SEE: ゲージ、構え、エフェクト、相手の位置。

Style reference (the user's own draft — check every fact before using anything similar; it may contain errors):
- セト E：セトとミニオンの一直線上に立たず、真横か斜め後ろに立つ。W直後（闘魂が空）にショート。
- モルデカイザー E：手の予備動作を見て横に避ける。Eを外した直後にQ→AA→E→ショート。単体でQを受けない（ミニオンの近くで戦う）。

Write `danger/out<N>.json` for ids in `danger/ids<N>.json`. Reply ONLY: path, count, and champs you were unsure about (one line each).
