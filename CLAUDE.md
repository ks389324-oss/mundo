# LoL対面攻略サイト（ks389324-oss/mundo）— 更新手順

GitHub Pages で公開しているLoL攻略ページ群です。どのClaudeのセッションからでも、このリポジトリを開けば更新できるように、元データとビルド手順をすべて `src/` に置いています。

## 公開ページ
| ページ | URL | 公開ファイル | 元データ |
|---|---|---|---|
| ムンドTOP対面帳（55体） | https://ks389324-oss.github.io/mundo/ | `index.html` | `src/data2.json`, `src/plays.json` |
| ジャックスTOP対面帳（55体） | /mundo/jax/ | `jax/index.html` | `src/jax/jax_final.json`, `src/jax/wr.json` |
| チョ＝ガスTOP対面帳（55体） | /mundo/cho/ | `cho/index.html` | `src/cho/cho_final.json`, `src/cho/wr.json` |
| ナサスTOP対面帳（55体） | /mundo/nasus/ | `nasus/index.html` | `src/nasus/nasus_final.json`, `src/nasus/wr.json` |
| LoL対面図鑑（汎用・全173体） | /mundo/all/ | `all/index.html` | `src/gen/champs_v2.json` |
| LoLアイテム図鑑 | /mundo/items/ | `items/index.html` | `src/items/data.json` |

全ページ共通の追加データ:
- `src/cs/cs_all.json`：CSで近づく時の注意
- `src/tips/tips.json`：ひとこと
- `src/gw/gw.json`：重傷が必要なキャラ
- `src/buy.json`：対策アイテム
- `src/scale/scale.json`：強い時間帯の目安（序盤・中盤・終盤の3段階。`src/gen/champs_v2.json` の解説から作図し、別担当が照合済み。実データではないため、図に「解説から作図」と明記し、League of Graphs の実データへのリンクを併記）
- `src/dmg/dmg.json`：AD／AP／混合の表示（LoLalytics の実戦ダメージ構成。物理÷(物理＋魔法)が70%以上でAD、30%以下でAP、それ以外は混合。取得手順は `src/briefs/dmg_BRIEF.md`）
- `src/trade/trade.json`：ショート／ロング／避けるのトレード推奨（ムンド版のみ。`data2.json` の照合済み記述を基に執筆し、別担当が照合。手順は `src/briefs/trade_BRIEF.md` → `trade_AUDITOR.md`）
- `src/danger/danger.json`：警戒スキル（1〜2個）・避け方・避けた後のショート／ロング／下がる、立ち位置の一言（ムンド版のみ。手順は `src/briefs/danger_BRIEF.md` → `danger_AUDITOR.md`）。`src/danger/ar.json` は通常攻撃の射程（Data Dragon）で、射程比較の図に使います
- `src/links.py`：外部リンクのURL規則

## 更新のしかた
1. `src/` の JSON（内容）またはテンプレート（見た目。`src/template*.html`, `src/gen/template_all.html`, `src/items/template_items.html`）を編集します。
2. `cd src && sh build_all.sh` を実行します。5ページを作り直し、公開用の `index.html` に反映します（`<head>` 部分は既存のものを残します）。
3. コミットして `git push origin HEAD:main` します。1〜数分で GitHub Pages に反映されます。

画面の確認は Playwright（Chromium）でPC幅（1920×920）とスマホ幅（390×700）の両方を見ます。PCは「最初の画面（.fv）」が920px以内に収まること、スマホは横にはみ出さないことを確かめます。

## 内容を書く時のルール（利用者の強い要望）
- **間違ったことは書かない。** スキルの仕様・数値・相互作用は、必ず公式Wiki（https://wiki.leagueoflegends.com/en-us/ ）で確認してから書きます。確認できないことは書きません。
- **書いた担当と別の担当が照合します。** 新しい対面帳や大きな追加では、執筆とは別の照合を必ず行います。手順書の雛形は `src/briefs/` にあります（`*_WRITER.md` → `*_AUDITOR.md`）。
- 利用者がYouTube動画や他のAIの文章を持ってきた場合は、1つずつWikiで照合し、古い・誤っている部分を直してから入れます（`src/briefs/vid_BRIEF.md`）。
- 文章は初心者向けで、です・ます調にします。専門用語には初出で（ ）の説明を付けます。
- アイテム名・スキル名はRiot公式の日本語名を使います（`src/dd/latest/data/ja_JP/item.json`、Data Dragon）。
- 勝率は出典とパッチを明記します。ムンド版はLoLalytics、ジャックス版・チョ＝ガス版・ナサス版はOP.GG（エメラルド以上）です。

## 新しいキャラの対面帳を足す場合
チョ＝ガス版がその見本です。次のファイルを複製して作ります。
- `src/build_cho.py`
- `src/template_cho.html`
- `src/briefs/cho_WRITER.md` と `src/briefs/cho_AUDITOR.md`

作ったら次の3つも更新します。
- `src/deploy.py` と `src/build_all.sh`（新しいページを追加）
- 各ページの上部の相互リンクボタン
- `README.md`

## Data Dragon（公式アイコン・データ）
アイコンは `src/img.json` と `src/gen/img.json` に埋め込み済みです。新しいアイコンや最新データが必要な時は、`https://github.com/InFinity54/LoL_DDragon` を sparse clone して `latest/` 以下を使います。
