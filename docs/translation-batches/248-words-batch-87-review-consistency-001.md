# B248 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `14cc61a3526acddf05f23db55318f168a6d55b44` (tree `6813010a904c7b243be5fd05a86333b6e79affa8`),
> the signed candidate pushed before review.
> Later reconciliation is in `248-words-batch-87-recheck-001.md`.

Snapshot: RU branch full-ru-248-words-87, HEAD = 14cc61a3526acddf05f23db55318f168a6d55b44 (as specified); `git status --porcelain` empty. Nothing edited, staged or generated.

Scope: facets CONSISTENCY and QUIZ SAFETY plus cross-file integration. Model not verifiable.
- Read in full (front matter and body): all 30 new cards (派手 目立つ 中身 目次 狙う 狙い 目指す あたりまえ 標準 思い込む 仮定 推定 目安 目上 盛る 盗難 盆地 盆 皮膚 案外 思いがけない 皮肉 的確 百科事典 白髪 登場 発電 発揮 発想 発射).
- Read in full: the diffs of kanji/外.md, words/目下.md, words/課程.md, words/過程.md.
- Also read: the manifest diff and the intake paths.
- EN comparison was programmatic (front matter minus title; set of .md link targets). It was not a line-by-line prose read.
- `tools/validate.py`: 0 errors.
- `build_manifest.build_manifest()` called in memory (no write) equals the committed manifest.json, so there is no stale hash.
- The intake path list (34) equals the content diff (34). It holds only hashes and notes, with `held: []` and no learner content.
- The diff contains no generated or unrelated files. Blobs are LF.

Verdicts
- Consistency: CLEAN.
- Quiz safety: CLEAN. No missing required guard. Two optional leads (O1, O2).
- Navigation-only restorations (外, 目下, 課程, 過程): CLEAN.
- Manifest/intake integration: CLEAN.

Findings: none.

Evidence

1. Consistency
- Front matter equals EN for all fields except the translated title.
- The only `quiz_exclusions` differences are the 6 RU-appended entries on 5 cards (中身, 推定, 目安, 案外, 発揮); every EN entry is retained.
- 盆地 and 百科事典 have no `quiz_exclusions` in RU or EN.
- All relative .md links in the 30 cards resolve.
- EN links left as plain text have no RU file: 地味, 平野, 仮説, 上司, 予想どおり, 退場, トレー, 撃つ, 部下, kanji 準/皮/膚. This follows the repository convention.
- No dropped EN link has an existing RU target.
- One RU-only link: 狙う:29 → 目指す (in-batch sibling, a real synonym comparison). It is useful and harmless.
- Nav files each change one line, link wrap only, at the EN link position, and the path forms match EN:
  - 外:41 `[案外](../words/案外.md)`
  - 目下:33 `[目上](目上.md)`
  - 課程:33 `[仮定](仮定.md)`
  - 過程:33 `[仮定](仮定.md)`
  - Surrounding prose, the pre-existing «курс» remarks and the 過程:9 exclusion are untouched.
  - The old glosses are compatible with the new titles, so no change is needed.
- Inherited from EN, not a batch defect: 的確 and 盆地 have no `kango` tag although their type is kango. The validator passes.

2. Quiz safety
- All guard targets exist and their titles match the task text.
- There are no self-guards and no duplicates.
- Neither the previous published batch nor 倣う is referenced.
- RU-introduced guards. Each is declared on one side only. Reverse sides do not declare the pair: 内容 has no `quiz_exclusions`; 観測 lists 予想 予測 意見 考え 見解 説 見当 見る 予報 占う 読み; ところが lists しかし でも だけど; 現れ lists 表現 言葉.
  - 中身→内容: REQUIRED. JMdict 中身 «contents; substance» overlaps 内容. The titles «содержимое; наполнение» and «содержание; суть» overlap, and the article says so. This is the only declaration of the pair.
  - 推定→観測: CONSERVATIVE. Basis: 観測 sense «forecast/outlook». Titles «косвенная оценка» and «прогнозная оценка (…)» share «оценка». 観測 already guards its own cluster. Real basis, necessity not established, harmless.
  - 推定→読み: CONSERVATIVE. Basis: 読み «guess; estimate». «оценка ситуации» vs «косвенная оценка». 予測 and 評価 already guard 読み, so it is consistent.
  - 目安→観測: CONSERVATIVE. Same 観測 basis. «приблизительная оценка» vs «прогнозная оценка».
  - 案外→ところが: REQUIRED by title collision. 案外 «вопреки ожиданиям» vs ところが «однако (вопреки ожиданию)». The dictionary senses differ (adverb vs conjunction), but the titles collide.
  - 発揮→現れ: REQUIRED by title collision. «проявление в деле» vs «проявление; выражение». 現れ had no guard for 発揮.
  - None is unjustified.
- 目上/目下: link only, no guard. The antonym titles «вышестоящий»/«нижестоящий» cannot be correct answers for each other. A guard would be unjustified.
- 盆地, 百科事典, 発電 and 発射 need no guard.
  - 盆地 vs 盆 are unrelated senses.
  - 百科事典 «энциклопедия» differs from 辞典/辞書 «словарь».
  - 発電 vs 生産/電力/電気/電報 are distinct.
  - 発射 vs 発車/打つ/投げる are distinct (but see O1).
- Stem-only screen neighbours (the 26 guarded and 258 unguarded rows; unguarded rows examined include 派手–効果/有効, 目立つ–瞳/投げる, 中身–含む/満ちる/半ば, 目指す–急速/態度, あたりまえ–大丈夫/平気/習慣/決まり, 標準–物価/級, 思い込む–信頼/固い, 仮定–結果/原料, 推定–評価/可/間接, 目安–およそ/大体/約/目印/倣う/純粋, 案外–予期/期待/やはり/変, 登場–誕生/外出/おやすみ, 発電–電流/能率/電子, 発揮–能力/知能/発達, 発想–型/代表/倣う, 発射–ラケット). Each shares a stem but not a sense, so none is a defensible correct answer and no guard is needed. The one segment hit, 狙い–考え «замысел», is guarded.
- Titles discriminate the in-batch groups.
  - 狙う / 狙い / 目指す differ by POS and sense and are mutually guarded.
  - 派手 / 目立つ differ by POS and are guarded.
  - Likewise 仮定/推定/思い込む, 標準/目安/あたりまえ, 案外/思いがけない/皮肉, 盆/盆地, 発揮/発想/発射/発電.
  - 中身 «наполнение» alone is thin for «суть», but the 内容 guard and the body cover it.
  - 皮膚 «кожный покров» is deliberately formal to avoid colliding with 肌 «кожа»; 肌 and 皮 are guarded.
  - 発揮 as a noun title fits its する use.

Optional (non-blocking, low confidence)
- O1: 発射 «пуск (ракеты, снаряда)» vs 飛ばす «запускать (в воздух)» (飛ばす guards 省く, 投げる). JMdict 飛ばす has a «launch» sense, so it is a possible near-answer. POS differs, EN does not guard it, and I did not verify the sense. If wanted: add `quiz_exclusions: [飛ばす]` to 発射 (currently none).
- O2: 登場 vs 誕生 «появление на свет; возникновение» share the stem «появление», but the senses are birth vs entrance. Not exact, and EN does not guard it. If wanted: add 誕生 to 登場's list. A guard for 目安 vs 目印 is not recommended.

Limits
- Dictionary senses are cited from memory of JMdict/Daijisen and the cards' own notes, and were not re-fetched.
- Semantic neighbour screening used the lexical title screen plus a keyword scan of RU titles, not a human pass over all RU titles.
- BLIND honoured: no author report, batch record, ledger or scratch worktree was read.
- Translation accuracy was not reviewed line by line; other facets cover it.
