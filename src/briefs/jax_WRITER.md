# Task: write JAX-top matchup entries (Japanese) for a beginner aiming for Gold

The reader plays Jax top and wants, for each lane opponent: how Jax should play to win, a one-line memo of what to focus on, and VERY concrete sequences ("相手のQにEを合わせて、その後AA→Wでダメトレ" level of detail). Accuracy first: a wrong interaction (e.g. claiming Jax E dodges a spell that it does not) loses games. Patch 26.19 (Data Dragon 16.19), Sept 2026.

Base dir: <repo>/src/jax/

## Jax kit (verified on https://wiki.leagueoflegends.com/en-us/Jax on 2026-09-28 — trust this)
- P アサルトアタック (Relentless Assault): each basic attack gives a stack for 2.5s (refreshes, up to 8), each stack = bonus attack speed. → hitting minions before a fight pre-stacks attack speed.
- Q リープストライク (Leap Strike): CD 8/7.5/7/6.5/6, range 700. Dashes to the target UNIT — enemy OR ally, including minions and wards (official tip: can jump to allied units incl. wards → escape). If enemy in range on arrival: physical damage, and if target is a champion Jax auto-attacks them after the dash. Jax can cast any ability during the dash. Cannot target structures. Grounded disables it; knockdown interrupts.
- W パワーバッシュ (Empower): CD 7/6/5/4/3. Next basic attack or Leap Strike within 10s deals bonus magic damage. RESETS Jax's basic attack timer (= AA → W → immediate second attack). On a basic attack it gets +50 range and an uncancellable windup. Parries (e.g. Fiora W) and spell shields block it.
- E カウンターストライク (Counter Strike): CD 17/15/13/11/9, duration 2s, radius 375. While active: DODGES all incoming non-turret basic attacks (including ability-based attacks that apply on-hit — i.e. empowered basic attacks), and takes 25% reduced damage from champion AREA-OF-EFFECT abilities. It does NOT dodge non-AoE spells/skillshots and does NOT block turret shots. Recast manually after 1s, or auto at 2s: magic damage to nearby enemies (+20% per attack dodged, up to +100%) and STUN for 1s in 375 radius. Exceptions named on the wiki: Alpha Strike (Master Yi) and Piercing Darkness (Senna) — E dodges only their on-hit parts, not the ability itself.
- R ウェポングランドマスター (Grandmaster-at-Arms): CD 110/100/90. Passive: every 3rd consecutive hit (2 stacks then next attack) deals bonus magic damage; while active it triggers at 1 stack (every 2nd hit). Active: 0.25s cast (can move during it), damages nearby (375) enemies; if it hits a champion gains bonus armor and MR for 8s.
- Standard patterns from a top Jax guide (mobafire ThisIsPatrik 26.18, OK to use): hit minions first to stack P before engaging; level-1 vs melee: AA them in their wave, when minions aggro activate E and keep attacking; lvl6 combo: AA minions twice → Q onto enemy → AA → immediately W (R passive proc + W burst); splitpush: AA → W reset.
- Short trade template (derived from verified mechanics above; adapt per matchup): E → Q onto enemy (arrive with E active) → AA → W (reset) → recast E after ≥1s for the stun → walk out / Q back to a minion or ward.

## Inputs per champion
`in/<slug>.json`: Jax's win rate vs this opponent from OP.GG (Emerald+, 26.19) as [winrate, games] (null = not enough data), the opponent's skill descriptions and CDs (trusted, already fact-checked), a generic "how to play vs this champion" entry (trusted), and a Dr. Mundo–view counter text (REFERENCE ONLY — Mundo mechanics like "ムンドのQ" never apply to Jax). Also `hints_mobafire.md` has matchup tips from a Jax guide: treat as leads to VERIFY, not facts.

## Verification (mandatory)
For every Jax-vs-X interaction you state, check the opponent's wiki page (https://wiki.leagueoflegends.com/en-us/<Name>, or `Template:Data_<Name>/<Ability_Name>`; ask WebFetch for verbatim text + Notes):
- "Jax's E dodges X": only if X is a basic attack or an empowered basic attack / on-attack ability (wiki wording like "next basic attack", "empowers his next attack", "basic attacks"). If X is a spell (projectile, dash, area), E does NOT dodge it; if X is an AREA ability, E reduces its damage by 25% — say "軽減" not "回避".
- "E stun is blocked/negated by X" (e.g. whether Fiora's Riposte parries Jax's E stun / W; whether Poppy W stops Jax Q; spell shields), "Q is stopped by X" (e.g. Poppy's Steadfast Presence stops dashes → Jax Q), unstoppable/untargetable states (Fiora W? Vladimir W pool untargetable, Kayle R invulnerable, Yorick, Shen W blocks attacks for allies, Tryndamere R can't die, Kindred etc.), grounded effects.
- Any number you give (duration, CD) must be from input or wiki.
If you cannot verify, leave it out. Never invent numbers.

## Output
Write `out/<group>.json`: object keyed by slug. Each value:
{
 "stance": [{"s":"攻め|五分|守り","when":"短い条件（例：Lv1〜5）"}],   // 1–3 steps over the lane, first = early lane
 "memo": "一口メモ。この対面でこれだけ意識する、1〜2文。",
 "win": "ジャックスの勝ち筋。2〜3文。どの時間帯に、何を条件に勝つか。",
 "combos": [ {"name":"短い名前（例：Eで受けてからの短いトレード）","when":"使う瞬間（相手の何が無い時・何をした時）","steps":["E（カウンターストライク）を押す","…","…"],"why":"なぜ有効か1〜2文"} ],   // 2–3, steps 3–7 each, very concrete, name opponent skills
 "goal": ["狙い（短く）","…"],     // 2–3
 "plays": [["こうなったら（相手の行動・画面の合図）","こうする（ジャックスの行動と理由）","go|w|no"]],  // 4–6; go=打ち返す, w=避ける・受ける, no=付き合わない
 "core": "相手の主力（何が一番危険か）1〜2文。ジャックス目線、ムンドの話はしない。",
 "plan": "相手の狙い。『A → B → C、という流れです。』の文を必ず含め、その後に崩し方を1文。（→の前後は半角スペース）",
 "trap": "ジャックスが知らないと倒される仕様（分からん殺し）と防ぎ方。1〜2文。",
 "go": "攻めて良い瞬間。1〜2文。",
 "skills": {"P":{"c":"この技へのジャックスでの対策（Eで避けられる／軽減だけ／避けられない、を必ず明記）1〜2文"}, "Q":{...}, "W":{...}, "E":{...}, "R":{...}},
 "evidence": ["English notes of each interaction you verified + URL"]
}

## Style
- 敬体（です・ます）, short sentences, plain words. Beginner reader.
- Explain jargon on first use in each entry in parentheses: AA（通常攻撃）, CD（再使用までの待ち時間）, トレード（短く殴り合うこと）, オールイン（どちらかが倒れるまで戦うこと）, ウェーブ（ミニオンの群れ）, CS（ミニオンを倒してお金を得ること）, フリーズ, ガンク, スキルショット, 重傷, etc.
- Refer to Jax skills as "E（カウンターストライク）" on first use in an entry, then "E" is fine. Refer to opponent skills by key + short Japanese description (e.g. "ダリウスのW（次の通常攻撃が強化されるスロウ攻撃）").
- Items: only use official Japanese names from `<repo>/src/dd/latest/data/ja_JP/item.json` (grep it). Keep item advice minimal.
- Honest stance: if the matchup is bad for Jax (low win rate, ranged poke, etc.), say to play safe, which items/levels change it, and what not to do.

Write the file incrementally (after every 2–3 champions). When done, reply ONLY: file path, number of champions written, and any claims you could not verify (which must not be in the file).
