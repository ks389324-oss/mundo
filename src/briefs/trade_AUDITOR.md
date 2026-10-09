# Task: audit trade recommendations (ショート/ロング/避ける) written by another agent

Base dir: /home/claude/mundo/src/. Read briefs/trade_BRIEF.md for definitions and rules.
Input: trade/out<N>.json. Trusted: data2.json champs[] (by "en"). Wiki: https://wiki.leagueoflegends.com/en-us/<Name>.
For EVERY entry check: (1) consistent with data2 stance/win/trap/go/pun; (2) every mechanic in "why" is true per data2 or the wiki (WebFetch to check anything not in data2 — don't trust memory); (3) the ショート/ロング logic follows the decision rule; (4) Japanese is polite, ≤60字, skill names match data2.
Fix problems directly. Write trade/aud<N>.json with the same shape (without "_ev"), plus "_log": {"<en>":"ok" or "what you changed and why (English)"}.
Reply ONLY: path, ok count, changed list with one-line reason.

Extra caution: writers flagged several ロング entries as their own inference (e.g. Zed Lv6+, Malphite, Vladimir, Gangplank, Riven, K'Sante, Jayce, Pantheon, Renekton, Mordekaiser R中) and Olaf/Garen/Gragas as judgment calls. For each ロング, require clear support from data2 (stance 攻め/五分 + text that says long fights or sustain favour Mundo, or that the enemy's damage is front-loaded / on cooldown) or the wiki. If support is weak, prefer ショート and say why. Do not invent mechanics.
