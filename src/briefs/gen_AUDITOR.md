# Independent audit: generic "how to play against X" guide (Japanese)

Another writer drafted these entries. You did NOT write them. Your job is to find and fix factual errors before a beginner relies on them to climb ranked. Be skeptical: assume there are mistakes. Patch 26.19 (Sept 2026).

## Files (directory <repo>/src/gen/)
- Draft entries: `all_draft.json` (object keyed by champion id). Check only your assigned ids.
- Official Riot data per champion: `in/<id>.json` (official Japanese names/descriptions, cooldowns, ranges). Note: official "enemytips" are sometimes outdated, and KSante's official tips are wrongly Lee Sin's.

## How to check
For each assigned champion, fetch the wiki page https://wiki.leagueoflegends.com/en-us/<Name> (spaces→_, apostrophe→%27; Nunu → Nunu_%26_Willump; Renata → Renata_Glasc; MonkeyKing → Wukong) with WebFetch, asking for VERBATIM ability descriptions and "Notes/General Details" for all of P, Q, W, E, R. If truncated, use `Template:Data_<Name>/<Ability_Name>` pages. Then check every mechanical claim in the draft:
- skills.*.what / tip / cc: is the effect right? Is the listed CC exactly what the ability applies (type correct: stun vs knock up vs root vs slow, etc.)? Any CC missing from "cc" that the ability applies to enemies?
- "minions block it" / "goes through minions" / "can be dodged" / recasts / windup cues / conditions: must match the wiki's wording ("first enemy hit" = blocked by minions; "enemies hit"/"all enemies in a line" = passes through).
- plan, trap, aim, vs, strengths, weaknesses, spike: flag only if factually wrong or clearly bad advice given the mechanics (e.g. telling the reader to attack during an invulnerability window).
- lanes: flag only if clearly wrong for current solo queue.
Never correct from memory alone. If the wiki doesn't settle it, mark "unsupported" and propose removing the claim.

Known points to double-check if in your group: Jax Q (can it target allies/wards?), Milio Q (blocked by minions?), Zac Q, Galio R (knock up vs knock back), Camille E (stun), Janna Q, Elise E, Caitlyn E, Viego W, Karma Q, Draven E, Tahm Kench W, Renata R, Yasuo R, Lulu W, Kassadin E, Gwen R.

## Output
Write `audit/<groupname>.json` as a JSON array. For each issue:
{"id":"Jax","field":"skills.Q.tip" (or skills.Q.what / skills.Q.cc / plan / trap / aim[1] / vs[0] / strengths[2] / weaknesses[0] / spike / summary / lanes),
 "severity":"wrong|misleading|unsupported|bad_advice",
 "old":"current text",
 "new": replacement (string in the same polite Japanese style and similar length; for cc give a JSON array; for lanes a JSON array; to delete a list item give ""),
 "evidence":"verbatim wiki quote + URL"}
For champions with no issues add {"id":"<id>","field":"none","severity":"ok","old":"","new":"","evidence":"checked P,Q,W,E,R"}.

Reply ONLY with: file path, champions checked, issue counts by severity, and the 3 most important issues (one line each).
