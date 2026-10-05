# Task: beginner-friendly item guide entries (Japanese), fact-checked. Patch 26.19 (Data Dragon 16.19), Oct 2026.

Base dir: <repo>/src/items/
`items.json`: array of items {id, name, gold, cat, stats[], body (official Japanese effect text, cleaned), chips, plain}. Your ids are in ids<N>.json.
Note: Riot's Data Dragon text sometimes shows a scaling value as "0" (e.g. ブランブル ベスト "0の魔法ダメージ"). For those, look up the real value on https://wiki.leagueoflegends.com/en-us/<Item_Name_in_English> (WebFetch; ask for the current verbatim passive text). English names: see ../dd/latest/data/en_US/item.json if present, else infer and verify.

For each item write:
- "who": どんなチャンピオン・役割が買うか（1文、20〜40字。例「攻撃速度で戦うマークスマン向け」）。Base it on the stats/effect; don't name specific champions unless obvious and generic (avoid if unsure).
- "easy": 効果のやさしい説明（1〜2文、です・ます）。Official text says what it does; rephrase plainly and say what it means in a fight ("つまり…"). Only use numbers that appear in body/stats or that you verified on the wiki. Explain jargon in parentheses (スキルヘイスト＝スキルの待ち時間短縮, 脅威＝物理防御を無視する力, 行動妨害耐性, 負傷＝回復量を減らす効果, オンヒット, etc.).
- "body_fixed": only if body contains a "0" placeholder that is clearly a missing value: the body with the correct value(s) from the wiki (keep the official Japanese wording otherwise), else null.
- "cat_ok": true, or a corrected category from this list if clearly wrong: ブーツ, 対策素材, サポート, 物理：クリティカル, 物理：攻撃速度, 物理：暗殺・貫通, 物理：ファイター, 物理＋魔法, 魔法：メイジ, 魔法：体力付き, タンク：物理防御, タンク：魔法防御, タンク：体力・両防御.
- "evidence": English, URL(s) used (only needed for body_fixed or cat change).

Output `items/sum<N>.json`: object keyed by id. Write incrementally. Reply ONLY: path, count, ids with body_fixed, ids with cat changed.
