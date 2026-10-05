# Task: one-glance "CSを取りに近づく時の注意" per champion (Japanese)

Reader: LoL beginner. Before a match they glance at the top of a champion page. They want: "when I step up to last-hit (CS), don't approach while skill X is available". Must be SHORT (the page must not get long).

Source (TRUSTED, already fact-checked twice): <repo>/src/gen/champs_v2.json (array; fields key, summary, strengths, weaknesses, vs, aim, trap, plan, skills{P,Q,W,E,R}{n,cd,what,means,tip,cc}). Use ONLY facts stated there. Do not add mechanics, numbers or cues from memory. If the source does not support a CS-relevant warning, give a generic but true one based on the source (e.g. the enemy's main poke skill).

For each assigned champion id, pick the 1–2 skills that most punish a player who walks up to minions to last-hit IN LANE (poke, hooks/pulls, engages, stuns, burst trades). Prefer basic skills (Q/W/E/P) over R, except when R is the actual threat from Lv6 (then say "Lv6以降").

Output `cs/out<N>.json`: object keyed by champion id:
{"cs":[{"k":"Q","t":"〜30字程度。『〇〇があるうちは〜しない／〜する』の形。スキルは短い説明つき（例：Q（引き寄せのフック）が上がっている間は、ミニオンの横に出ない）","src":"which field(s) of the source support it, e.g. skills.Q.what + vs[1]"}]}
- 1 item normally, 2 at most. Each "t" ≤ 40 Japanese characters, です・ます not required (terse imperative-ish like 「〜しない」「〜の後に取る」 is fine, but no rude tone).
- Must be actionable: what to avoid AND, if the source supports it, when it is safe (e.g. 「外した後に取る」).
- Do not mention any specific player champion (no Mundo/Jax).
Write incrementally. Reply ONLY: file path and count.
