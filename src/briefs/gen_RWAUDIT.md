# Independent audit of the beginner rewrite (facts + clarity)

You did NOT write these entries. A beginner (aiming for Gold) will rely on them. Check two things for each assigned champion:

A. FACTS. Files in <repo>/src/gen/:
 - `rw_all.json` = the rewritten entries (object keyed by id) — this is what you audit.
 - `champs.json` = the previous version, already fact-checked twice (array; find by id). Facts that appear there are trusted.
 - `in/<id>.json` = Riot official Japanese data.
 Any mechanic, number, cue or condition in the rewrite that is NOT in champs.json must be verified on the wiki (https://wiki.leagueoflegends.com/en-us/<Name> or Template:Data_<Name>/<Ability_Name>, via WebFetch asking for verbatim text + Notes). Also re-check anything that looks suspicious even if it was in champs.json. Flag: wrong, unsupported (can't find it → propose removal), bad_advice (e.g. attacking during invulnerability, "stand behind minions" for something that passes through), and contradictions between fields.

B. CLARITY for a beginner. Flag (severity "unclear") only real problems:
 - jargon not explained in parentheses on first use within the entry (ガンク, CD, スキルショット, 重傷, トレード, オールイン, AA, ウェーブ, CS, カイト, ピール, etc.),
 - advice without a reason, or a mechanic with no "what it means for you",
 - vague phrases a beginner can't act on ("気をつけましょう" alone, "うまく避けましょう"),
 - advice that assumes a specific champion or only works for melee/ranged without saying so.
 Provide a concrete rewritten replacement.

## Output
Write `rwaudit/<groupname>.json` as a JSON array of issues:
{"id":"Warwick","field":"key" | "summary" | "spike" | "plan" | "trap" | "strengths[1].d" | "weaknesses[0].t" | "vs[2].do" | "vs[2].why" | "aim[0].when" | "aim[0].do" | "skills.W.what" | "skills.W.means" | "skills.W.tip",
 "severity":"wrong|unsupported|bad_advice|unclear",
 "old":"current text",
 "new":"full replacement text for that field (polite Japanese です・ます, same length or a bit longer; \"\" to delete a whole list item — only for vs/aim/strengths/weaknesses items, give field like \"vs[2]\")",
 "evidence":"verbatim wiki quote + URL, or for 'unclear' a one-line reason"}
Champions with no issues: {"id":"<id>","field":"none","severity":"ok","old":"","new":"","evidence":"checked"}.

Reply ONLY: file path, champions checked, counts by severity, 3 most important issues (one line each).
