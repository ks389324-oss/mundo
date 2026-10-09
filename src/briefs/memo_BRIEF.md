# Task: 「そのまま実行するだけで勝てるメモ」への書き直し（ムンドTOP対面帳）— 3 roles

Base dir: /home/claude/mundo/src/
User = LoL beginner, Dr. Mundo TOP. He wants each matchup card to be a memo he can EXECUTE without thinking: not「避けて」but HOW（どっちへ・どの距離で・いつ）; not「注意」but WHERE to stand and WHY; and honest about what can't be dodged.
His own examples of the tone he wants:
- 「マルファイトのQは対象指定で避け不可。だからそのダメージは貰う前提で、こちらはQの射程（625）の外からムンドのQで削る」
- 「セトのEは予備動作0.25秒で見てからは避けられない。先端（射程450）くらいの距離に立って誘い、撃たれる前に一歩下がって避ける。挟まれなければ当たってもスタンしない」
- 「モルデカイザーのEは自分に向けた直線（幅200）。避ける方向は横。前に出ても避けられない。射程700の端で誘って下がるのが確実」
Patch 26.19. User insists「間違ったことを書かない」.

## Files
- Current cards to rewrite: `danger/danger.json` (per champ: pos, sk[ {k,dodge,how,t,then} ]) and `plan/plan.json` (per champ: rule,pos,pas,go[],back[],later).
- TRUSTED facts: `data2.json` champs[] by "en" (skills[*].d/.c/.cd/.g incl. range/width/cast/speed, stance, core, plan, trap, go, win, pun), `trade/trade.json`, `plays.json` (by slug), `danger/ar.json` (attack ranges).
- `danger/react_calc.json`: computed time from cast start until the skill reaches max range (cast + range/speed) per danger skill, from data2 geometry. null = unit-targeted or not computable (then check the wiki for windup/cast time if you need it).

## Output schema (per champ) — write to the path your role says
```
"<en>": {
  "plan": {"rule","pos","pas","go":[...],"back":[...],"later"},   // same keys as plan.json
  "sk": [ {"k","dodge":"よける|位置|受ける",
           "react":"見て避けられる|読みで避ける|避けられない",
           "how":"どう避けるか：方向・距離・合図。です・ます調 25〜70字",
           "hit":"当たった時／貰う前提での対応。20〜55字（不要なら null）",
           "t":"ショート|ロング|下がる","then":"20〜55字"} ]
}
```
react rule of thumb (an estimate; say 目安 if you mention it): unit-targeted / point-and-click → 避けられない. Total time ≤0.35s → 読みで避ける (stand at max range and step back BEFORE it's cast, or stand where it doesn't matter). ≥0.5s with a visible windup → 見て避けられる. In between: judge by windup visibility/width; if unsure → 読みで避ける. Self-centred AoE with a long windup (e.g. a spin) → 見て避けられる by walking OUT of the radius (say how far).
Dodge direction: line/cone aimed at you → 横; only at the tip can you step back. Circle at a location → 外へ. Self AoE → 離れる（半径◯◯の外へ）.
Numbers: only from data2 g / ar.json / react_calc.json / wiki-verified. Mundo Q range 1050, Mundo AA 125.

## Rules for everyone
- Must not contradict trusted files (stance phases, trade ショート/ロング/避ける, go/pun windows).
- Mundo passive blocks the next IMMOBILIZING effect only (stun, root, airborne incl. pulls/knockbacks, fear, charm, taunt, suppression); one per cooldown (60〜15秒). Not slow/silence/blind/grounded/damage.
- Every mechanic not in trusted files → verify via WebFetch on https://wiki.leagueoflegends.com/en-us/<Name> or leave out. No 絶対/必ず.
- です・ます調、初心者向け、専門用語は（ ）で一言。Keep it short; every line must be an action.
