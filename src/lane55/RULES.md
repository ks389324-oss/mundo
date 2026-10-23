# ムンドTOP対面帳 — fixed completion criteria (FINAL). Do not add new requirements beyond this file.

Goal: an Iron–Bronze Dr. Mundo TOP player decides 立ち位置・CS・トレード・ルーン・買い物 in 30 seconds before laning. 55 matchups.
Live patch 26.20 (Data Dragon 16.20). Today 2026-10-20. (26.21 goes live 2026-10-21 — preview, unconfirmed: Darius Q CD 9–5→9–4, Sion HP/R, Wukong armor, Yone Q ratio, Varus Q/W, Zaahen bugfix. Mention only in "patch" for those six; never base advice on those numbers.)

Paths:
- Scratch: /tmp/claude-0/-home-claude/4ffab90c-5818-53c9-94b9-dc62450e754a/scratchpad/
- Repo (READ ONLY, never edit, never git push): /home/claude/ks389324-oss/mundo/src/
- Facts (wiki-verified): scratchpad/six/facts.json (runes, boots, minion gold/XP, item prices items_ja), scratchpad/six/mundo.json (Mundo kit).
- Template example (final, audited): scratchpad/six/sett_r4.json — copy its structure exactly.
- Earlier audit findings per matchup: inside scratchpad/all55/<slug>_in.json ("audit"); existing site content: same file ("existing").
- Critical findings already re-audited (use their final "after" texts and facts/judgements for Sylas, Anivia, Quinn, Yorick, Vayne, Zed, Sett, Jax): scratchpad/audit/high_v4.json.

## Card schema (same as six/sett_r4.json)
en, jp, sum{stand,go,cs,back,hit}, ruler[{v,label,kind,unconfirmed?}], stand{base,watch[{k,range?,why}],step_in,hold_back,positions{normal,lasthit,danger},passive_vs{blocks,not}}, go{items[{if,do}],except}, back{items[{if,do}],stop_chase}, cs{aa,e,q,skip,cost}, trade{start,hit,exit,long,no_trade[],realm?}, skills{P,Q,W,E,R}, patch, shop{runes,first_back,boots,core1,basis}, new[], changed[{path,before,after,why,src}], src[], unconfirmed[ "日本語で1行ずつ" ], major[{path,before,after,why}]  (major = only dangerous errors fixed: wrong spec, or advice that gets Mundo killed / wastes his main tool).

## Content rules
1. Positions: the AA-CS position is the goal. normal / lasthit / danger are distinct. Never "stand outside the enemy's max range" as the permanent position. lasthit says which enemy-skill state allows entering, from which side, and returning (seconds as 目安).
2. CS stepping (go) ≠ trading (trade.start) — trade is stricter. trade.no_trade lists 2〜4 "may CS but must not trade" cases.
3. Passive blocks ONE immobilizing effect (stun, root, airborne incl. pulls/knockbacks/knock-ups, fear, charm, taunt, suppression, sleep); not damage, slows, silence, follow-up, a second CC. Mundo W stores 80〜95% of damage taken in the first 0.75s and heals on recast; it reduces nothing. Never a standalone reason to step up or fight. passive_vs lists this opponent's blockable CC and what is not blocked.
4. Every threshold (HP半分, ミニオン3体, …) is 目安 and never permission on the other side.
5. CS cost: melee 20G, caster 14G, cannon 50G+; XP within 1500 even without the last hit. Conditions must allow AA last hits several times per wave in early lane; exceptions only where a real death/kill threat exists.
6. Numbers: only wiki-verified (WebFetch https://wiki.leagueoflegends.com/en-us/<Name>; K'Sante → K%27Sante, Cho'Gath → Cho%27Gath, Tahm Kench → Tahm_Kench, Wukong → Wukong) or already-verified values in the input files. Computed values say （計算の目安） with what they are computed from. Unlabelled double values on the wiki ("700 • 900") are unconfirmed → no assertion, flag in ruler and list in unconfirmed. If unknown, omit the number and describe the action. NEVER invent a distance.
7. Style: です・ます調, beginner-friendly, 専門用語は初出で（ ）, sum lines ≤42字, no 絶対/必ず/最適/推奨（統計で裏付けのない物）.

## Runes and shopping (fixed)
- Base page for ALL matchups: 不死者の握撃／打ちこわし・息継ぎ・超成長／天啓：魔法の靴・疾駆. shop.runes = {"status":"基本","short":"基本のまま","base":"不死者の握撃／打ちこわし・息継ぎ・超成長／天啓：魔法の靴・疾駆","considered":[≤2 realistic candidates using facts.json effects, verdict 基本維持],"reason":"対面別の個別ルーン統計が無いため基本ページを使います（LoLalytics・OP.GG・League of Graphsはページ単位まで）"}.
- Exception (early-boots matchups, judgement — no matchup rune stats): Teemo, Quinn, Vayne, Kennen, Varus, Jayce. For these: status "変更", short "魔法の靴→ビスケットデリバリー（ブーツを早く買うため）", text explains: 魔法の靴 forbids buying boots before its free boots (12 min, −45s per takedown, facts.json), and these ranged opponents kite/poke so early boots help; basis 判断（統計なし）. Biscuit effect from facts.json.
- With 魔法の靴 (all other matchups): first_back tiers must NOT contain ブーツ or any boots. shop.boots = {"short":"魔法の靴で無料（約12分）→ 強化","base":{"name":"魔法の靴の無料ブーツ","why":"12分（キル・アシスト1回ごとに45秒短縮）で入手、それまでブーツは買えません。その後スイフトネス ブーツ等へ強化（強化費用は未確認なら書かない）"},"switch":[conditions for スイフトネス／プレート スチールキャップ／マーキュリー ブーツ with facts.json effects and OP.GG matchup counts as reference],"note":"勝率の差は採用状況の違いも含むため、最適とは断定しません"}.
- Exception matchups: early boots allowed in tiers; boots section as before (base by counts/purchase order).
- first_back.tiers: 4 tiers 〜399G／400〜799G／800〜1099G／1100G〜, buy/why/basis(統計|動画研究|スキル仕様|未検証). Prices from facts.json items_ja. Refillable potion (詰め替えポーション) on first back ONLY for Aatrox, Ambessa, Darius, Fiora, Jax, Sett, Warwick, basis "動画研究" (the user's own study of top-player videos, patch 26.18 — not statistics). note: "購入順は統計で確認できないため、推奨ではなく候補です".
- core1: from LoLalytics (games, wr) — say データ不足 if <50 games or missing.
- Stats: WebFetch https://lolalytics.com/ja/lol/drmundo/vs/<lolalytics slug>/build/ (patch, wr, games, start items, core build order) and https://op.gg/ja/lol/champions/drmundo/items/top?target_champion=<slug> (boots counts). Slugs: ksante, tahmkench, chogath, wukong, etc. Copy numbers verbatim; never from memory; missing → データ不足. basis line: "統計：LoLalytics・OP.GG パッチ26.20（16.20）エメラルド以上。…".
