# Task: real damage composition (physical / magic / true) per champion from LoLalytics

Base dir: /home/claude/mundo/src/
For each champion id in dmg/ids<N>.json (Riot ids, e.g. "DrMundo", "MonkeyKing"):
- LoLalytics slug = id lowercased, except MonkeyKing → wukong.
- WebFetch https://lolalytics.com/lol/<slug>/build/ and ask for the verbatim "Physical Damage", "Magic Damage", "True Damage" numbers shown (these are average damage dealt to champions per game, from real games), plus the lane, patch and rank the page shows.
- If a fetch fails or numbers are missing, retry once. If still missing, record null.
- Sanity check: if the result looks implausible (e.g. total < 3000, or all three zero), refetch once.

Output dmg/out<N>.json: object keyed by id: {"phys": int, "magic": int, "true": int, "lane": "...", "patch": "...", "rank": "...", "url": "..."} (numbers as integers without commas; null fields if unavailable).
Write incrementally. Reply ONLY: path, count, ids with null data.
