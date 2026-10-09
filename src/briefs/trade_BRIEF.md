# Task: ショートトレード／ロングトレード推奨（ムンドTOP対面帳）

Base dir: /home/claude/mundo/src/
User = LoL beginner playing Dr. Mundo TOP, insists "絶対に間違ったことを書かない". Patch 26.19 (Sept 2026).

Definitions (show these meanings, not other ones):
- ショート＝スキル1〜2個と通常攻撃数発を当ててすぐ下がる短い殴り合い。
- ロング＝回復・体力を活かして数秒以上殴り合い続ける。
- 避ける＝その時間帯はトレード自体をせず、CSとQ（ミニオンの後ろから）だけ。
Decision rule: 「戦いが長引くほどどちらが得をするか」。相手の火力が殴り合い中に増える（スタック、ゲージ、回復、DPS型の通常攻撃）→ ショート。相手の火力が最初に集中していて耐えればムンドの持久力が上回る／相手の主要スキルがCD中 → ロング。

Sources:
1. TRUSTED (already fact-checked): data2.json → champs[] (find by "en"). Use stance, core, plan, trap, go, win, pun, skills. Your entry MUST be consistent with these (e.g. if stance says 守り 序盤 and win says 短いトレードだけ → 序盤 ショート or 避ける).
2. Any mechanic you cite that is not stated in data2.json must be verified on https://wiki.leagueoflegends.com/en-us/<Name> (or Template:Data_<Name>/<Ability>) with WebFetch. Dr. Mundo's own kit too (https://wiki.leagueoflegends.com/en-us/Dr._Mundo). If you cannot verify, do not write it.
3. No memory-based numbers. Avoid absolute words (絶対, 必ず) unless the data says so.

For each id in trade/ids<N>.json output 1〜3 phases, ideally aligned to that champ's stance phases:
{"<en>": [{"t":"ショート|ロング|避ける","when":"序盤 / Lv6以降 / コア1個以降 など（≤14字）","why":"です・ます調、日本語25〜60字。何が長引くと誰が得か。スキル名はdata2.jsonの表記に合わせる"}], ...}
Also output "_ev": {"<en>":"English: which data2 fields + wiki URLs you used"}.

Write trade/out<N>.json. Reply ONLY: path, count, and any champ where you were unsure (one line each).
