# B216 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `034ab7ea9034db0f24f7d8dfdad1f16af819e788` (tree `ca36d09f0ff3b18b6aa66d1ac4e8f2fbcf82f41c`),
> the signed candidate pushed before review.
> Later reconciliation is in `216-words-batch-55-recheck-001.md`.

Snapshot: RU `034ab7ea9034db0f24f7d8dfdad1f16af819e788` on `full-ru-216-words-55`; `git rev-parse HEAD` matched and `git status --porcelain` was empty before and after the review. No uncommitted changes. (I once created an untracked `tools/__pycache__` by importing `build_manifest`; I deleted it, and the tree is clean again.)

Scope: Facets CONSISTENCY and QUIZ SAFETY plus cross-file integration, for batch 216 (`216-words-batch-55`). Reviewer model: not verifiable from inside the session.
Files read IN FULL, each against its EN original/frozen front matter and link set (EN `6af98cb`):
- All 30 new cards (front matter and body): 勧める 勢い 勝ち 勘 動詞 勇気 効く 助手 劣る 加わる 劇場 劇 割る 前者 刺激 制度 到着 利益 別れ 別に 列車 列 刑事 刈る 切れる 切れ 分野 分析 分ける 分. I checked EN front matter, `quiz_exclusions` and link sets programmatically for all 30.
- All 23 navigation diffs, read in full. I checked each programmatically: stripping Markdown link syntax from the old and new text gives identical text, so only link brackets/hrefs changed. I also compared per-target link counts with EN.
- `manifest.json`: I rebuilt it in memory with `tools/build_manifest.build_manifest` and compared it to the committed file. They are identical (contentVersion `b3cc2ebec3dd0f16`). I did not run the generator's writer.
- Intake record: its 53 payload paths equal the 53 `words/`/`kanji/` paths in the content diff, and every `candidateRawSha256` equals the manifest hash. It adds no learner content.
- `python tools/validate.py` gives 0 errors. `tools/check_content_budget.py` gives 4,616 entries / 13.05 MB.
- Tools run: `link_parity.py` and `word_title_screen.py` (the segment-overlap rows were all on the guarded pairs listed below). Targets confirmed absent: `kanji/詞.md`, `kanji/損.md`, `words/優れる.md`, `ドラマ.md`, `出会い.md`, `薦める.md`, `利く.md`, `探偵.md`, `体制.md`, `行列.md`, `分かれる.md`.

Verdicts:
- Consistency: CLEAN. No manifest, front-matter, link, navigation or intake defect found. The restored 37 links match the EN positions and counts exactly. `kanji/劇.md` links 劇場×2 and 劇×1 and leaves 悲劇 and 劇場 unwrapped.
- Quiz safety: NEEDS FIX, one Minor finding with medium-low confidence (F1). Every EN exclusion is retained.
- Scoped coverage of cross-file integration: CLEAN. RU-only links are justified and the pre-existing items are listed under Limits.

Findings:
- F1; Minor; quiz safety; `words/切れる.md:10` (`quiz_exclusions`); one gap in the guard set.
  Claim and impact: 切れる has the displayed sense «кончаться (о запасе)» (JMdict 切れる, the sense "to run out; to be exhausted"; the card example 電池が切れました, 期限が切れる). 終わる has the title «заканчиваться; заканчивать». The Russian glosses are near-synonyms. The author already guards this pair elsewhere (切る→終わる, 無くなる→終わる), but 切れる does not. A learner shown «кончаться (о запасе)» could defensibly pick 終わる. The guard is minor because 終わる normally cannot take a stock as its subject.
  Remedy: change line 10 to `quiz_exclusions: [折れる, 無くなる, 切る, 破る, 終わる]`. Then regenerate the manifest and the intake path/hash record as usual.
  Evidence: RU titles 切れる «рваться; кончаться (о запасе); хорошо резать» and 終わる «заканчиваться; заканчивать»; the card's own 期限が切れる sense.
  Confidence: medium-low; reasonable people could leave it, because EN also has no such guard.
- F2; Trivial; quiz safety (over-guard); `words/劇.md:10`; the 劇場 entry. See the table row below. Remove 劇場 from `quiz_exclusions` if you want a strict reading: `quiz_exclusions: [芝居, 公演]`. Confidence: medium, and I am not asking for a blocking change. It is optional and harmless.

RU-introduced `quiz_exclusions` (entries beyond EN), with dictionary basis and classification:

| Card → entry | Dictionary basis (entry, sense) | Class |
|---|---|---|
| 勧める → 推薦 | 勧める senses 1–3 "recommend; advise" vs 推薦 "recommendation; recommending" (suru-noun) | conservative (the verb/noun parts of speech differ) |
| 勧める → 提案 | 勧める sense "to suggest/offer" vs 提案 "proposal; suggestion" | conservative |
| 劣る → 負ける | 負ける has the sense "to be inferior to" | required (displayed «уступать» is shared) |
| 劣る → 譲る | 譲る "to yield; to give way", not "inferior" | conservative (shared string «уступать» only) |
| 加わる → 加える | 加える/加わる transitive/intransitive pair, «добавляться» vs «добавлять» | required |
| 加わる → 足す | 足す "to add" | conservative (加える already guards 足す) |
| 効く → 効果 | 効果 "effect; efficacy"; the stem «эффект» is shared | conservative (a verb vs a noun) |
| 劇 → 芝居 | JMdict 劇 "drama; play" vs 芝居 "play; drama; stage show" | required |
| 劇 → 公演 | 公演 "public performance of a play" | conservative |
| 劇 → 劇場 | 劇場 "theatre building"; the card itself teaches that 劇 is not the building | unjustified (a contrast the article teaches; harmless) |
| 割る → 分ける | 割る sense "to divide (arithmetic)" vs 分ける "to divide; to split" | required (displayed «делить»/«разделять») |
| 制度 → 機関 | 機関 sense "organ; institution; system" vs title «учреждённая система» | conservative |
| 到着 → 着く | 到着する "to arrive" vs 着く "to arrive"; the suru action sense is taught | required (project precedent 勝ち/勝つ, 負け/負ける) |
| 別れ → 別れる | same-stem noun/verb pair (JMdict 別れ / 別れる) | required by the 勝ち/勝つ precedent |
| 別に → あまり | JMdict 別に "(not) particularly", with the negation sense; あまり "(not) very much" | required |
| 別に → 特に | 特に "particularly"; overlaps in 特に問題はない | conservative |
| 別に → 別 | 別 "another; separate" vs 別に "separately" | required (the same stem and display) |
| 列車 → 汽車 | 汽車 "(steam) train" vs 列車 "train" | conservative |
| 列 → 順番 | 順番 "order; turn"; title segment «очередь» is shared | required |
| 列 → 番 | 番 "one's turn"; segment «очередь» is shared | required |
| 刑事 → 警官 | 警官 "police officer" is the hypernym of 刑事 "(police) detective" | conservative |
| 切れる → 切る | 切る «резать» vs 切れる «хорошо резать» | required |
| 切れる → 破る | 破る "to tear" vs 切れる "to snap/tear" | conservative |
| 分析 → 検査 | RU 検査 title «осмотр; анализ» equals 分析 «анализ» | required |

No exclusion is a mere topical guard apart from the 劇場 entry, which is classed unjustified (F2). The titles «помощник» (助手/手伝い), «уступать» (劣る/負ける/譲る) and «очередь» (列/順番/番) are each guarded by a direct exclusion on at least one side. No missing required guard was found other than F1. All other dense-cluster pairs in the brief (勢い/力・元気・活気, 勇気/覚悟, 勘/予想・判断・感じ, 勝ち/勝つ・負け, 刺激/影響・感動・いらいら, 劇場/映画館・舞台・会場, 刈る/切る・髪, 分/部分・割合, 分野/畑・地方, 前者/後者, 利益/損害・得る, 動詞/使う, 列車/普通, 別れ/別) have distinct Russian titles, and the EN guards are retained.

RU-only links: all four are justified. The RU rule «ссылки на имеющиеся карточки ставьте при содержательном вводе/сравнении» (content-structure line 42) applies to each.
- 到着→着く: the card compares and explains 着く.
- 分→部分: the card compares 部分.
- 分ける→分かる: the card explains it as «понимать» and warns about the endings.
- 列→順番: the card uses it to separate «чей-то черёд» from the row.

No unlinked mention of an existing card is substantive enough to need a link. The mentions 裁判, 事件, 特急, 暖房 and 圧力 are incidental words inside examples.

Optional: none beyond F2.

Limits:
- I did not verify linguistic correctness or comprehensibility (other facets). The dictionary bases above come from my knowledge of JMdict and the cards' own cited senses; I did not re-fetch the entries.
- Pre-existing differences from EN outside this batch were not changed by this candidate and are not defects here: `kanji/割.md` has RU-only links to 割れる and 割合; `words/損.md` lacks EN's `../kanji/損.md` link because `kanji/損.md` is absent; EN links in other kanji files point to words with no RU file (刺さる, 刺す, 刺身, 名刺, 演劇, 効力, 勇ましい, 姿勢) and stay plain text.
- I did not read the batch records, ledger, progress or any author or reviewer reports, per the blind rules.
