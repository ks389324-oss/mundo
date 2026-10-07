# Task: write NASUS-top matchup entries (Japanese) for a beginner aiming for Gold

The reader plays Nasus (ナサス) top and wants, for each lane opponent: how Nasus should play to win, a one-line memo, and VERY concrete sequences ("相手のEが終わったらW（ウィザー）→ AA → Q（サイフォンストライク）でリセット" level of detail). Accuracy first. Patch 26.19 (Data Dragon 16.19), Oct 2026.

Base dir: <repo>/src/nasus/

## Nasus kit (verified on https://wiki.leagueoflegends.com/en-us/Nasus on 2026-10-07 — trust this)
- P ソウルイーター (Soul Eater): 10/15/20% life steal (by level).
- Q サイフォンストライク (Siphoning Strike): CD 7.5/6.5/5.5/4.5/3.5. Empowers next basic attack within 10s: +50 range, bonus physical damage (30/50/70/90/110 + 100% of stacks). RESETS the basic attack timer. If the empowered attack KILLS the target: +4 permanent stacks (+10 if champion, large minion or large monster). → Nasus's core plan is last-hitting minions with Q to stack; his early damage is low before stacks/levels.
- W ウィザー (Wither): CD 15/14/13/12/11, range 700, 5s. Slows a champion; slow grows each second up to 47/59/71/83/95%; also cripples attack speed (35.25→71.25% max). Strongest tool vs melee/AA champions and for sticking to a target.
- E スピリットファイア (Spirit Fire): CD 12, range 650, radius 400, 5s zone. Magic damage on cast then per second; enemies inside lose 30–50% armor. Used for poke and wave clear.
- R アヌビスの怒り (Fury of the Sands): CD 120/100/80, 15s. +300/450/600 health, +40/55/70 armor & MR, bigger, +50 attack range, area magic damage (% max HP) every 0.5s, and HALVES Q's cooldown while active.
- General: weak early (low damage before stacks), strong late; vs ranged/poke he loses lane and must farm under tower with Q. Short trade: W (slow) → AA → Q (reset) → E zone; all-in after 6 with R.

## Inputs per champion
`in/<slug>.json`: Nasus's win rate vs this opponent from OP.GG (Emerald+, 26.19) as [winrate, games] (null = no data), the opponent's skill descriptions and CDs (trusted), a generic guide entry (trusted), and Mundo/Jax-view texts (REFERENCE ONLY — never apply Mundo or Jax mechanics to Nasus).

## Verification (mandatory)
For every Nasus-vs-X interaction you state, check the opponent's wiki page (https://wiki.leagueoflegends.com/en-us/<Name> or Template:Data_<Name>/<Ability_Name>; WebFetch, verbatim + Notes): e.g. whether X's dash/blink escapes W's slow, whether Q (empowered attack) is dodged/blocked (Jax E dodges it, Fiora W parries, Shen W blocks, blinds make it miss — and then no stacks), whether X's damage is reduced by armor (E's armor shred matters only vs physical damage), Teemo blind, Gwen W mist, Vladimir W pool, Tryndamere R, Kayle R. Numbers only from input or wiki. If you can't verify, leave it out.

## Output
Write `out/<group>.json`: object keyed by slug. Each value:
{
 "stance": [{"s":"攻め|五分|守り","when":"短い条件"}],
 "memo": "一口メモ。この対面でこれだけ意識する、1〜2文。",
 "win": "ナサスの勝ち筋。2〜3文。",
 "combos": [ {"name":"…","when":"…","steps":["…"],"why":"…"} ],   // 2–3, steps 3–7, very concrete, name opponent skills
 "goal": ["…"],     // 2–3
 "plays": [["こうなったら","こうする（理由）","go|w|no"]],  // 4–6
 "core": "相手の主力 1〜2文（ナサス目線）",
 "plan": "『A → B → C、という流れです。』の文を必ず含め、その後に崩し方を1文。（→の前後は半角スペース）",
 "trap": "ナサスが知らないと倒される仕様と防ぎ方。1〜2文。",
 "go": "攻めて良い瞬間。1〜2文。",
 "skills": {"P":{"c":"この技へのナサスでの対策 1〜2文"}, "Q":{...}, "W":{...}, "E":{...}, "R":{...}},
 "evidence": ["English notes of each interaction verified + URL"]
}

## Style
- 敬体（です・ます）, short sentences, plain words. Beginner reader.
- Explain jargon on first use in each entry in parentheses: AA（通常攻撃）, CD（再使用までの待ち時間）, トレード（短く殴り合うこと）, オールイン, ウェーブ, CS, ガンク, スキルショット, 重傷, 沈黙（スキルが使えなくなる妨害）, etc.
- Refer to Nasus skills as "Q（サイフォンストライク：スタックが溜まる強化AA）" "W（ウィザー：強力なスロウ）" "E（スピリットファイア：物理防御を下げる炎の範囲）" "R（アヌビスの怒り）" on first use, then just the key. Opponent skills by key + short description.
- Items only with official Japanese names from ../dd/latest/data/ja_JP/item.json. Keep item advice minimal.
- Honest stance: if the matchup is bad (low win rate), say to play safe and why.

Write incrementally. When done, reply ONLY: file path, number of champions written, and any claims you could not verify (which must not be in the file).
