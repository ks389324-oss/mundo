# Independent audit: Jax-top matchup entries (Japanese)

Another writer produced these entries. You did NOT write them. A beginner will rely on them to climb, so find and fix errors. Be skeptical. Patch 26.19.

Base dir: <repo>/src/jax/
- Brief given to writers (includes the verified Jax kit): `WRITER.md` — read it first.
- Entries: `out/g0.json` … `out/g4.json` (objects keyed by slug). Audit only your assigned slugs.
- Opponent trusted data: `in/<slug>.json`.

Jax Counter Strike (E) dodge rules, verbatim from https://wiki.leagueoflegends.com/en-us/Template:Data_Jax/Counter_Strike :
- "dodge all incoming non-turret basic attacks and take 25% reduced damage from all area of effect abilities sourced from champions."
- "Counter Strike will also dodge abilities that can trigger on-hit effects (Parrrley, Mystic Shot)"
- "There are exceptions of abilities that Counter Strike will not dodge but will dodge the damage from on-hit effects that they trigger (Alpha Strike, Piercing Darkness)."
So: an opponent ability is "dodged" only if it is a basic attack / empowered basic attack, or an ability that applies on-hit effects (check the opponent wiki wording "applies on-hit effects"/"on-hit"). Anything else is NOT dodged; if it is an area ability, damage is reduced 25% ("軽減"). When the attack is dodged, riders of that attack (stun/slow/silence from an empowered attack) do not apply unless the wiki says otherwise — flag claims either way that the wiki does not support.

## Check for each assigned slug
1. Every "Eで避けられる／回避／防げる" and "軽減" claim, every stun/dash/parry/untargetable interaction, every number and duration → verify on the opponent's wiki page (https://wiki.leagueoflegends.com/en-us/<Name> or Template:Data_<Name>/<Ability_Name>; WebFetch asking for verbatim text + notes). Also any claim about Jax's own kit vs WRITER.md.
2. Combos: are the step sequences mechanically possible (e.g. E recast needs ≥1s after cast; W resets AA; Q needs a target unit within 700; can't Q during grounded), and is the advice sound (not attacking into invulnerability/parry, not using E into Fiora W, etc.)?
3. Contradictions between fields (e.g. memo says "攻め" but stance says 守り; one field says dodged, another says not).
4. Beginner clarity: jargon not explained on first use in the entry; vague advice without concrete action. Only flag real problems.
5. Official Japanese item names (check dd/latest/data/ja_JP/item.json in the parent scratchpad dir).

## Output
Write `audit/<group>.json` as a JSON array of issues:
{"slug":"garen","field":"memo" | "win" | "go" | "trap" | "core" | "plan" | "stance" | "goal" | "combos[1].steps[3]" | "combos[0].why" | "plays[2]" | "skills.Q.c",
 "severity":"wrong|unsupported|bad_advice|unclear",
 "old":"current text (for plays[i] give the array)",
 "new": replacement (same type as old: string, or array for plays[i]/stance/goal/steps; polite Japanese です・ます; "" to delete a list item),
 "evidence":"verbatim wiki quote + URL, or one-line reason"}
Slugs with no issues: {"slug":"<slug>","field":"none","severity":"ok","old":"","new":"","evidence":"checked"}.

Reply ONLY: file path, slugs checked, counts by severity, 3 most important issues (one line each).
