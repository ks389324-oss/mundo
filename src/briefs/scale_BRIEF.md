# Task: rough "power curve" (序盤/中盤/終盤 strength) per champion, derived from our verified text

Base dir: <repo>/src/  (here: /home/claude/mundo/src/)
Source (TRUSTED, fact-checked): gen/champs_v2.json — for each champion read `spike` (強い時間帯), `summary`, `strengths`, `weaknesses`, `plan`, `key`. Use ONLY what these fields say. Do not use outside knowledge or memory; if the text does not say anything about a phase, give it 2 (普通).

For each id in your list, output:
{"e":1|2|3, "m":1|2|3, "l":1|2|3, "why":"日本語25〜45字。どの記述から判断したか（例：序盤は弱く、アイテムがそろう中盤から強い、と記載）", "src":"field names used, e.g. spike, weaknesses[0]"}
- e = 序盤（Lv1〜6前後, レーン戦の前半）, m = 中盤（コアアイテム1〜2個, Lv6〜11前後）, l = 終盤（アイテムがそろった後）.
- 3 = 強い時間帯として記載されている, 1 = 弱い時間帯として記載されている, 2 = 記載なし・普通.
- Be conservative and consistent: a phase gets 3 or 1 only when the text clearly supports it. "序盤から強い" → e=3; "終盤に強くなる/スケールする" → l=3; "序盤が弱い" → e=1; "後半は伸びにくい/落ちる" → l=1.

Output scale/out<N>.json (object keyed by id). Reply ONLY: path and count.
