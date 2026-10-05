# Independent audit: Cho'Gath-top matchup entries (Japanese)

Another writer produced these entries. You did NOT write them. A beginner will rely on them to climb, so find and fix errors. Be skeptical. Patch 26.19.

Base dir: <repo>/src/cho/
- Brief given to writers (includes the verified Cho'Gath kit): `WRITER.md` — read it first.
- Entries: `out/g0.json` … `out/g4.json` (objects keyed by slug). Audit only your assigned slugs.
- Opponent trusted data: `in/<slug>.json`.

Cho'Gath kit facts are in WRITER.md (verified). Key risks to check: Q (ラプチャー) has a 0.627s delay — advice must not assume it hits a dashing/moving target reliably; W silence does NOT stop movement, basic attacks, or abilities explicitly castable while silenced, and may not cancel channels already in progress; R is single-target true damage execute — cannot target untargetable/zombie states, cannot kill through Tryndamere R, Kayle R invulnerability, Zilean-like revives; E resets AA and spikes hit in a line; P heals only on kills.

## Check for each assigned slug
1. Every "Eで避けられる／回避／防げる" and "軽減" claim, every stun/dash/parry/untargetable interaction, every number and duration → verify on the opponent's wiki page (https://wiki.leagueoflegends.com/en-us/<Name> or Template:Data_<Name>/<Ability_Name>; WebFetch asking for verbatim text + notes). Also any claim about Cho'Gath's own kit vs WRITER.md.
2. Combos: are the step sequences mechanically possible (e.g. Q delay 0.627s; E is 3 empowered AAs within 6s; R range 175 melee), and is the advice sound (not attacking into invulnerability/parry, not attacking into Fiora W parry, etc.)?
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
