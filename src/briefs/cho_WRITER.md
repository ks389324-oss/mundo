# Task: write CHO'GATH-top matchup entries (Japanese) for a beginner aiming for Gold

The reader plays Cho'Gath (チョ＝ガス) top and wants, for each lane opponent: how Cho'Gath should play to win, a one-line memo, and VERY concrete sequences ("相手のEが終わったらQ（ラプチャー）→ W（スクリーム）→ E強化AA" level of detail). Accuracy first. Patch 26.19 (Data Dragon 16.19), Oct 2026.

Base dir: <repo>/src/cho/

## Cho'Gath kit (verified on https://wiki.leagueoflegends.com/en-us/Cho%27Gath on 2026-10-05 — trust this)
- P 暴食 (Carnivore): whenever Cho'Gath KILLS a unit (minion/monster/champion), heals 18–52 (by level) and restores mana. → His lane sustain depends on last-hitting; denying CS hurts him.
- Q ラプチャー (Rupture): CD 6, range 950, radius 125. After a 0.627s DELAY the target area erupts: magic damage, KNOCK-UP 1s, then 60% slow 1.5s. It is a ground-targeted delayed area (dodgeable, not blocked by minions). Hard to hit on a moving target; best after the enemy is slowed/committed or on predictable movement (dash end points, a target walking up to last-hit, a target locked in a channel).
- W スクリーム (Feral Scream): CD 11/10.5/10/9.5/9, range 650, 60° cone. Magic damage and SILENCE 1.6–2s on champions (silence = no abilities; they can still move and basic attack).
- E ヴォーパルスパイク (Vorpal Spikes): CD 8/7/6/5/4. Empowers next 3 basic attacks within 6s: +50 range, each attack launches a spike line in front dealing magic damage (% target max HP, +per Feast stack) and a slow. RESETS the basic attack timer. Spikes hit multiple enemies in a line (wave clear + poke through minions).
- R 捕食 (Feast): CD 80/70/60, range 175 (+ grows with stacks). TRUE damage to one target (champion: 300/475/650 +50% AP +10% bonus HP). If it kills: permanent stack (bonus HP, range, size). It's an execute — use it as the finisher; it can also secure dragon/baron/herald (true damage to monsters is higher; don't state numbers you didn't verify).
- Typical trade: E → AA (spikes) ×3 with AA resets; Q when the enemy is committed/slowed; W silence when the enemy dashes in or starts an all-in (silence stops their follow-up skills, not their movement or AAs).
- Cho'Gath is a tanky/AP-flexible bruiser-tank; weak early vs hard all-in fighters, scales with R stacks.

## Inputs per champion
`in/<slug>.json`: Cho'Gath's win rate vs this opponent from OP.GG (Emerald+, 26.19) as [winrate, games] (null = no data), the opponent's skill descriptions and CDs (trusted), a generic guide entry (trusted), and Mundo/Jax-view texts (REFERENCE ONLY — never apply Mundo or Jax mechanics to Cho'Gath).

## Verification (mandatory)
For every Cho'Gath-vs-X interaction you state, check the opponent's wiki page (https://wiki.leagueoflegends.com/en-us/<Name> or Template:Data_<Name>/<Ability_Name>; WebFetch, verbatim + Notes): e.g. whether W's silence stops X's ability already in progress, whether Q's knock-up interrupts X's dash/channel, unstoppable states (e.g. Malphite R, Sion R, Illaoi R leap ignores displacement), spell shields, untargetable (Vladimir W pool — R can't target), Kayle R invulnerable, Tryndamere R can't die (R true damage can't kill), Yasuo windwall (doesn't block Q, which isn't a projectile — verify), Fiora W parry (parries Q? W? R? verify), Gwen W mist (can Cho target her inside?), Sion passive etc. Numbers only from input or wiki. If you can't verify, leave it out.

## Output
Write `out/<group>.json`: object keyed by slug. Each value:
{
 "stance": [{"s":"攻め|五分|守り","when":"短い条件"}],
 "memo": "一口メモ。この対面でこれだけ意識する、1〜2文。",
 "win": "チョ＝ガスの勝ち筋。2〜3文。",
 "combos": [ {"name":"…","when":"…","steps":["…"],"why":"…"} ],   // 2–3, steps 3–7, very concrete, name opponent skills
 "goal": ["…"],     // 2–3
 "plays": [["こうなったら","こうする（理由）","go|w|no"]],  // 4–6
 "core": "相手の主力 1〜2文（チョ＝ガス目線）",
 "plan": "『A → B → C、という流れです。』の文を必ず含め、その後に崩し方を1文。（→の前後は半角スペース）",
 "trap": "チョ＝ガスが知らないと倒される仕様と防ぎ方。1〜2文。",
 "go": "攻めて良い瞬間。1〜2文。",
 "skills": {"P":{"c":"この技へのチョ＝ガスでの対策 1〜2文"}, "Q":{...}, "W":{...}, "E":{...}, "R":{...}},
 "evidence": ["English notes of each interaction verified + URL"]
}

## Style
- 敬体（です・ます）, short sentences, plain words. Beginner reader.
- Explain jargon on first use in each entry in parentheses: AA（通常攻撃）, CD（再使用までの待ち時間）, トレード（短く殴り合うこと）, オールイン, ウェーブ, CS, ガンク, スキルショット, 重傷, 沈黙（スキルが使えなくなる妨害）, etc.
- Refer to Cho'Gath skills as "Q（ラプチャー：遅れて打ち上げる地面攻撃）" "W（スクリーム：扇状の沈黙）" "E（ヴォーパルスパイク：トゲ付き強化AA）" "R（捕食）" on first use, then just the key. Opponent skills by key + short description.
- Items only with official Japanese names from ../dd/latest/data/ja_JP/item.json. Keep item advice minimal.
- Honest stance: if the matchup is bad (low win rate), say to play safe and why.

Write incrementally. When done, reply ONLY: file path, number of champions written, and any claims you could not verify (which must not be in the file).
