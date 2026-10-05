# Task: write a GENERIC "how to play against this champion" guide entry (Japanese)

Audience: a League of Legends beginner (aiming for Gold) who wants to understand each champion as an OPPONENT, regardless of which champion they themselves play. Accuracy is the top priority: a wrong mechanic can lose them games. Patch 26.19 (Sept 2026).

## Inputs
For each champion id assigned to you, read `gen/in/<id>.json` (in this directory's parent: <repo>/src/gen/in/). It contains Riot's OFFICIAL Japanese skill names and short descriptions, cooldowns, ranges, and official enemy tips. Some entries also contain `verified_reference_from_earlier_audit` — already fact-checked Japanese notes you may reuse (ignore Dr. Mundo–specific advice).

## Verify
Official descriptions are brief. For every mechanic you state beyond them (what CC it applies, whether minions block it, whether it can be dodged/cancelled, windup cues, recasts, conditions), check the wiki: https://wiki.leagueoflegends.com/en-us/<Name> (spaces→_, apostrophe→%27; Wukong page is "Wukong"; Nunu is "Nunu_%26_Willump"; Renata is "Renata_Glasc"). With WebFetch, ask for VERBATIM ability descriptions plus "Notes/General Details" for the abilities you need. If truncated, use `https://wiki.leagueoflegends.com/en-us/Template:Data_<Name>/<Ability_Name>`. If you cannot verify a claim, leave it out. Never invent numbers; only use numbers that appear in the input or on the wiki. Plan about 1–2 fetches per champion; be efficient but do not skip verification of CC types and "blocked by minions" claims.

CC vocabulary (Japanese): スタン, スネア（移動不能）, ノックアップ, ノックバック, 引き寄せ, 恐怖, 挑発, 魅了, 睡眠, サプレッション, スロウ, サイレンス, 盲目, グラウンド（移動スキル封じ）, 変身（ポリモーフ）.

## Output
Write `gen/out/<groupname>.json` (group name given in your task): a JSON object keyed by champion id. Each value:
{
 "lanes": ["TOP"|"JG"|"MID"|"ADC"|"SUP", ...]   // 1–2 most common positions in current solo queue, most common first
 "type": "e.g. 近接ファイター / 遠距離メイジ / 暗殺者 / タンク / マークスマン / エンチャンター",
 "summary": "どんなキャラか。1〜2文。",
 "strengths": ["強み（短い一文）", "…"],      // 2–3
 "weaknesses": ["弱み（短い一文）", "…"],     // 2–3, only ones that are real and exploitable
 "spike": "強い時間帯：序盤／中盤／終盤のどこが強いか、1文。",
 "plan": "相手の典型的な狙い（コンボ）を『A → B → C、という流れです。』の形で。",
 "vs": ["基本の対応方針（こう対応する）", "…"],   // 3–4 concrete, actionable bullets that work for ANY champion you play (positioning, what to dodge, when to disengage, what to buy e.g. 重傷/魔法防御 only if clearly relevant)
 "aim": ["狙いたい瞬間（例：〇〇を外した直後）", "…"], // 1–3
 "trap": "知らないと倒される仕様（分からん殺し）。1〜2文。",
 "skills": {
   "P": {"what": "どういう技か（見た目・効果）1〜2文", "tip": "対応：こうしたい／ここに注意 1〜2文", "cc": ["スタン", ...]},
   "Q": {...}, "W": {...}, "E": {...}, "R": {...}
 },
 "evidence": ["short English notes of what you verified on the wiki + URL (not shown to users)"]
}
Style: formal polite Japanese (です・ます), plain words, short sentences, beginner friendly. Explain jargon briefly if needed. Use the official Japanese skill names only if helpful (the app already shows them). Keep each field concise. No Dr. Mundo-specific content. For "cc", list only CC that the ability actually applies to enemies ([] if none).

Write the file incrementally if helpful (e.g. after each few champions) so work is not lost. When done, reply ONLY: file path, number of champions written, and any champion/ability you could not verify.
