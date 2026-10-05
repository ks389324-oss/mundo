# Task: rewrite champion entries so a true BEGINNER can understand the champion (Japanese)

The reader is a League of Legends beginner (aiming for Gold). They told us the current entries are unreadable: terse notes like "HPを高く保ち、半分を切らないようにしましょう（位置がばれて狙われます）" leave them asking "what does that mean?". Your job is to rewrite each entry so that, after reading it once, a beginner understands (1) what this champion does and why it is dangerous, (2) what they will SEE on screen, and (3) exactly what to do, and why.

Accuracy still comes first. The current text in `gen/champs.json` has already been fact-checked twice. Keep its facts. When you add an explanation of a mechanic that is not already in the entry (e.g. "the trail is visible from far away", "healing back above half removes it"), verify it on the wiki first: https://wiki.leagueoflegends.com/en-us/<Name> or `Template:Data_<Name>/<Ability_Name>` (WebFetch; ask for verbatim text + Notes). Never add numbers or mechanics from memory. `gen/out/g??.json` has the original writer's wiki evidence notes (field "evidence") which you may use.

## Style rules (very important)
- Polite Japanese (です・ます). Short sentences. Plain words.
- Every mechanic must be followed by what it MEANS for the reader in practice ("つまり…", "実戦では…").
- Every piece of advice must include WHY.
- Use on-screen cues a beginner can recognize: 「地面に赤い円が出たら」「体が光ったら」「武器を振りかぶったら」「体力バーの下のゲージが満タンになったら」. Only describe cues that are real (verify if unsure; otherwise describe the effect instead).
- Explain jargon the first time it appears in each entry, in parentheses: ガンク（敵ジャングラーの奇襲）, CD（スキルの再使用までの待ち時間）, スキルショット（方向を指定して撃つ技。横に動けば避けられる）, 重傷（回復量を減らす効果。「処刑人の招待状」などで付けられる）, トレード（短く殴り合うこと）, オールイン（どちらかが倒れるまで戦うこと）, AA（通常攻撃）, ウェーブ（ミニオンの群れ）, CS（ミニオンを倒してお金を得ること）, etc.
- Do not assume the reader's champion. Advice must work for anyone (ranged or melee); when advice differs, say so ("近接キャラなら…、遠距離キャラなら…").
- No Dr. Mundo–specific content.

## Model example (Warwick W, before → after)
Before: what「HPが半分未満の敵チャンピオンの位置が分かり、そこへ向かう時に加速します。」 tip「HPを高く保ちましょう。」
After:
 what「敵チャンピオンのHPが半分を切ると、かなり離れていてもワーウィックにはその相手への道筋（血の跡）が見え、それを追う間は足が速くなります。HPが半分未満の相手には攻撃速度も上がります。発動すると、一番近い敵1人をHPに関係なく8秒間この状態にできます。」
 means「つまり、あなたのHPが半分を切った瞬間から、ワーウィックは遠くからでも狙って走ってこられます。ワーウィックはジャングルで使われることが多いので、レーンで削られた直後にガンク（敵ジャングラーの奇襲）が来やすくなります。」
 tip「HPが半分を切ったら、帰還するかタワーの近くまで下がります。回復して半分以上に戻れば追跡は消えます。」

## Output schema
Write `gen/rw/<groupname>.json`: an object keyed by champion id. Each value:
{
 "key": "これだけ覚える。この相手で一番大事なこと1〜2文（理由つき）",
 "summary": "どんなキャラか。2〜4文。役割・戦い方・何が怖いか",
 "strengths": [{"t":"見出し（10〜20字）","d":"説明と、あなたにとっての意味（1〜3文）"}],   // 2–3
 "weaknesses": [{"t":"見出し","d":"説明と、どう突くか（1〜3文）"}],                      // 2–3
 "spike": "強い時間帯（序盤／中盤／終盤）と理由、その時間帯にどうするか（2〜3文）",
 "plan": "相手のよくある流れ。『A → B → C、という流れです。』の文を必ず含め、その後に崩し方を1文",
 "vs": [{"do":"こうする（行動を1文）","why":"理由（1〜2文）"}],                            // 3–5
 "aim": [{"when":"この瞬間","do":"こうする（理由も）"}],                                   // 1–3
 "trap": "知らないと倒される仕様：何が起きるか＋どう防ぐか（2〜3文）",
 "skills": {
   "P": {"what":"どういう技か。画面で何が見えるか（1〜3文）", "means":"つまり、あなたにとって何が怖い／何が起きるか（1〜2文）", "tip":"対応：具体的な行動と理由（1〜2文）", "cc":[copy from current entry]},
   "Q": {...}, "W": {...}, "E": {...}, "R": {...}
 },
 "evidence": ["English notes of any NEW facts you verified + URL"]
}
Keep "cc" exactly as in the current entry unless you verified it is wrong (then note it in evidence). Do not output lanes/type (they are kept as-is).

Write the file incrementally (after every few champions) so work is not lost. When done, reply ONLY: file path, number of champions written, and any new claims you could not verify (these must not be in the file).
