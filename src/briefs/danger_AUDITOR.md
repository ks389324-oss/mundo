# Task: audit 警戒スキル entries written by another agent

Base dir: /home/claude/mundo/src/. Read briefs/danger_BRIEF.md for the schema and rules.
Input: danger/out<N>.json. Trusted: data2.json champs[] (by "en"), trade/trade.json, plays.json. Wiki: https://wiki.leagueoflegends.com/en-us/<Name>.

For EVERY entry check:
1. The chosen 1〜2 skills are really the most dangerous ones for Mundo (consistent with data2 core/trap/skills[*].c).
2. "dodge" is right: よける only if the skill is a skillshot / has a visible windup that can be walked out of; 受ける for point-and-click (unit-targeted) skills; 位置 for things handled by positioning.
3. Every mechanic in pos/how/then is true per data2 or the wiki — WebFetch anything not in data2; don't trust memory. Pay special attention to claims that Mundo's passive blocks a CC (wiki: it blocks immobilizing effects; check if the specific CC is one of those and not a displacement), minion-collision claims (does the skillshot really stop on the first minion?), and timing claims (windup, gauges).
4. "t" (ショート/ロング/下がる) does not contradict trade/trade.json and data2 stance/win/go. ロング needs clear support; otherwise ショート.
5. Japanese: polite, lengths per brief, beginner-friendly.

Fix problems directly. Write danger/aud<N>.json with the same shape (without "_ev"), plus "_log": {"<en>":"ok" or "what you changed and why (English)"}.
Reply ONLY: path, ok count, changed list with one-line reason.
