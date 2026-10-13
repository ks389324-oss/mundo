# Task: Dr. Mundo TOP vs <opponent> item data from LoLalytics (verbatim extraction)

Base dir: /home/claude/mundo/src/
Your opponent slugs are in build/ids<N>.json (LoLalytics slugs, e.g. "yone", "ksante", "wukong", "tahmkench").

For each slug:
- WebFetch https://lolalytics.com/ja/lol/drmundo/vs/<slug>/build/
  Prompt it to return VERBATIM (no summarising, no guessing): the patch and rank shown; the matchup "Win Rate" and "Games" near the title;
  the "Starting Items" item names with the win rate and games shown next to them; the "Summoner Spells" names with win rate and games;
  the "Core Build" list in order (each item's Japanese name exactly as written, with the % and game count shown under it, if any);
  and the "Item 4", "Item 5", "Item 6" option lists (each name with its % and game count).
- Copy names exactly as the Japanese page writes them (e.g. "ドラン シールド", "マーキュリー ブーツ", "ソーンメイル"). Do NOT translate or normalise.
- If a field is missing from the fetched text, record null. If the fetch fails or the core build is missing, retry once.
- Never fill a value from memory or from another champion.

Output build/out<N>.json: object keyed by slug:
{
 "url": "...", "patch": "16.20", "rank": "EMERALD+",
 "wr": 48.27, "games": 1622,
 "start": {"items": ["ドラン シールド", "体力ポーション"], "wr": 48.18, "games": 961},
 "spells": {"items": ["フラッシュ", "イグナイト"], "wr": 58.33, "games": 60},
 "core": [{"name": "ワーモグ アーマー", "wr": 49.47, "games": 661}, {"name": "スイフトネス ブーツ", "wr": 52.01, "games": 546}, {"name": "終わりなき絶望", "wr": 64.0, "games": 50}],
 "item4": [{"name": "...", "wr": 0.0, "games": 0}],
 "item5": [...], "item6": [...]
}
Numbers as numbers (no %, no commas). Write the file incrementally (after each slug).
Reply ONLY: path, count, slugs with any null field.
