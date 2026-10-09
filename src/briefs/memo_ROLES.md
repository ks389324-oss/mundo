# Roles for memo_BRIEF.md (read memo_BRIEF.md first)

## WRITER (N): ids in danger/ids<N>.json → write memo/w<N>.json
Rewrite each champ's plan + sk into the new schema, starting from danger/danger.json and plan/plan.json (both already audited — keep their facts, make them concrete and executable). Add react/hit. Use react_calc.json; verify windups not in data2 on the wiki. Add "_ev": {"<en>": "English: sources, wiki URLs, uncertainty"}.
Reply ONLY: path, count, unsure champs (one line each).

## BEGINNER (N): input memo/w<N>.json → write memo/b<N>.json
You are a Mundo beginner reading each card at champ select. For EVERY line ask: "これだけ読んで、何を・どこで・いつすればいいか分かる？" Typical questions: 避けてってどっちに？ どのくらい離れる？ 合図は画面で何が見える？ 当たったらどうする？ なぜその位置？ 入るって何をする？
Rewrite vague lines to be concrete, using ONLY facts already in the card or in trusted files (data2/trade/plays/ar/react_calc). Do NOT invent mechanics. If a concrete answer needs a fact you can't find there, keep the line as is and list it in "_need": {"<en>": ["question for the auditor (Japanese)"]}. Also "_q": {"<en>": ["questions you had (Japanese, short)"]}.
Reply ONLY: path, count, how many lines rewritten, champs with _need.

## AUDITOR (N): input memo/b<N>.json → write memo/a<N>.json
Fact-check every line against trusted files and the wiki (WebFetch anything not in trusted files; don't trust memory). Check react classification against react_calc.json + wiki windups, dodge directions vs skill shape, passive claims, consistency with trade/stance. Answer every "_need" item (add the verified fact to the card, or drop the request if unverifiable). Keep the beginner's concreteness — don't make lines vague again. Output same schema without _ev/_q/_need, plus "_log": {"<en>": "ok" or changes (English)}.
Reply ONLY: path, ok count, changed list one line each.
