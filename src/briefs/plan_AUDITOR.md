# Task: audit 「この対面の方針」cards written by another agent

Base dir: /home/claude/mundo/src/. Read briefs/plan_BRIEF.md for schema and rules.
Input: plan/out<N>.json. Trusted: data2.json, trade/trade.json, danger/danger.json, plays.json, danger/ar.json. Wiki: https://wiki.leagueoflegends.com/en-us/<Name>.

For EVERY entry check:
1. No contradiction with trusted files (stance phases, trade ショート/ロング/避ける, danger skills and their 避け方, go/pun windows).
2. "pas": only claims the passive blocks a skill if that skill's CC is immobilizing (stun/root/airborne incl. pulls & knockbacks/fear/charm/taunt/suppression). Slow/silence/blind/grounded are NOT blocked. Verify CC type on the wiki if data2 doesn't state it. null is fine if nothing relevant.
3. Every mechanic/number is in trusted files or verified on the wiki (WebFetch). Remove anything unverifiable.
4. Advice is coherent as ONE plan a beginner can stick to; go/back cues are visible in game.
5. Japanese: polite, lengths per brief.

Fix directly. Write plan/aud<N>.json (same shape, no "_ev") plus "_log": {"<en>":"ok" or "what changed and why (English)"}.
Reply ONLY: path, ok count, changed list with one-line reason.
