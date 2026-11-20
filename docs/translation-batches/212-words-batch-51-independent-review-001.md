# Batch 212 — independent review 001

## Snapshot and scope

- Reviewed commit: `d5fd0d933b7590c71fceadde93af255a14c4e0c0` (tree `e25b42695c1de0f449a934e1fd3152047e1f92a3`), branch
  `full-ru-212-words-51`, parent `b16939d`. The candidate was committed signed directly and pushed before review.
  - The content was authored in a scratch worktree on the Batch 211 candidate `53d6950b1b8c0d254414e1f2ba4d967b2ca3b43a`.
    Before copying, the coordinator checked that the 19 navigation files and the Batch 211 cards `完成.md` and `専攻.md`
    were unchanged between `53d6950` and the candidate's parent `b16939d`, and that none of the 30 new cards existed
    there; after copying, it byte-compared all 49 scratch content files between the scratch worktree and the primary
    checkout.
  - Before the candidate, the coordinator changed one author title: 完了 «завершённость; полное выполнение» became
    «завершение (задачи, процесса)» (title and H1). 完了 names the finishing of a task or process (EN "completion"); RU
    line 16 already said «завершение задачи или процесса», and the published `kanji/了.md:20,28,32` and `kanji/完.md:40`
    gloss it «завершение»; «завершённость» names a state, as in the Batch 211 完成 decision. The new segment «завершение»
    is shared with 完成 «завершение (изделия, произведения); законченный вид» and 仕舞い «конец; завершение»; both pairs
    were already in the author's 完了 exclusions.
  - The coordinator also restored the three links held for this batch in Batch 211 cards, at their EN-linked positions
    and with EN's href forms: `完成.md:27` (to 完了), `完成.md:31` (to 完全) and `専攻.md:28` (to 学ぶ). No surrounding text
    changed.
  - The candidate differs from the published baseline by 30 new word cards, 21 files with 31 restored navigation links
    (the author's 19 navigation-only files with 28 links, plus the three coordinator wraps), `manifest.json`
    (`contentVersion` `19f9fe8ee9495dee`, 4,474 entries) and the intake.
- Published baseline recorded in the intake: `8ded5ffbb279703cbbc1a00adc5b310d923d7eb3` (Batch 211 merge). Parent `b16939d`
  adds only the Batch 211 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers, and the restored learner lines
  `完成.md:27,31` and `専攻.md:28`. Correctness and comprehensibility read each card against its full EN original;
  consistency compared front matter and links with EN by script.
  - Correctness also read every changed line in the 21 navigation files, the three binding RU instruction and format
    files, and the comparison cards 研究者, お宅, 奇しい, ある and いる in full; other comparison cards were compared by title
    and reading only. It inspected the Jisho/JMdict entries for all 30 headwords and for 研究者, the full jisho.org
    entries for 女王 (including the irregular じょうおう note) and お宅 (1002400), Weblio/Digital Daijisen 宅 senses 1–3 and
    Kotobank 宇宙 (Daijisen 補説 and Nihon Kokugo Daijiten). Russian-side evidence came mainly from Kuznetsov entries on
    Gramota («совершенный», «безупречный», «четверть», «семестр», «наружность», «сторониться», «чудной», «диковинный»,
    «странноватый», «эрудиция», «наличие», «безработица», «утратить», «пристрастие», «непостижимый», «загадочный»,
    «жилище», «внук», «невестка», «учёный», «дисциплина», «комиссия», «ссуда», «стипендия», «отобрать», «лишить» and
    «помолвка») and from ru.wiktionary «учёность», «освоить», «внучка», «триместр» and «помолвка». Several Gramota requests
    returned HTTP 429; no conclusion was drawn from those failures. It ran `tools/validate.py` (0 errors).
  - Consistency read all 30 cards and all 21 navigation diffs in full, checked `manifest.json` and the intake's path list
    and hashes by script, compared the front matter and links of every new card with EN by script, screened the new titles
    against every RU word title by exact segment and 5-character stem, read the titles and exclusions of the comparison
    words named in its prompt, ran `tools/validate.py` (0 errors) and classified every RU-added exclusion. Its JMdict
    senses for the exclusion pairs came from its own knowledge; only 世界 was fetched online. It did not read EN bodies
    line by line.
  - Comprehensibility read the 30 cards in full against EN and judged the three restored learner lines; it did not
    review the other restored navigation links beyond the 全く→完全 line it used to check that contrast. It ran the
    link-parity tool on the 30 cards and checked the 完全 and 学習 senses on jisho.org; it did not re-fetch every cited
    dictionary entry, and its report records no `tools/validate.py` run. It mentions title-screen stem hits only as leads.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD was still `d5fd0d9`
  and that `git status --porcelain` was empty. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator and named the report as the only file a
  reviewer writes. The correctness report states that no generator was run; the consistency and comprehensibility reports
  do not mention generators, and both their rechecks state that none was run. The coordinator found the tree clean after
  each review.
- Full blind reports:
  - `212-words-batch-51-review-correctness-001.md`
  - `212-words-batch-51-review-consistency-001.md`
  - `212-words-batch-51-review-comprehensibility-001.md`
- Initial reviewers were told not to read the author report or prompt, the coordinator's title-screen output or notes, the
  batch records, or one another's reports; the correctness and consistency reports confirm this, the consistency reviewer
  noting the intake record as its only batch-record read.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN**; scoped coverage **CLEAN**. No findings and no optional notes.

The reviewer found all 60 principal Japanese examples and their kana readings identical to EN, and read each translation
for polarity, participants, tense and aspect. It checked that 孫 and 俳優 do not mark gender in Japanese, that the 婚約
example invents no partner's sex, and that masculine Russian past forms are contextual renderings. Front matter outside
the titles matches EN and every EN exclusion is retained. It found no dropped EN link to an existing RU target; the
unlinked mentions of kanji 委 and 奇 and of the words 会員 and 王女 are correct because those RU cards do not exist. All 31
restored links occur with the same label and target in EN, and removing their markup restores each previous RU file
exactly. On titles, it noted that «совершенный» (Kuznetsov sense 2) can also mean complete or absolute, so 完全's label was
not restricted to praise; that «пристрастие» sense 1 means liking or inclination; and that RU explains 婚約 as a commitment
to marry without implying a ceremony, so «помолвка» is not a translation error.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (one added guard); cross-file integration **CLEAN**.

- F1 (minor, medium confidence), `完全.md:9`: no direct guard against 全然 «совсем не; совершенно», although the titles
  share «совершенн-» (the overlap that justified the RU-added 完全→全く) and the card teaches 完全に as «полностью»; JMdict
  全然 also has the affirmative "wholly; entirely; completely" use. Remedy: `quiz_exclusions: [全く, 全然]`.
- The front matter and links of every new card were compared with EN by script; all EN exclusions are retained, and the
  RU-added ones are classified below. The EN links missing in RU are exactly the four whose RU targets do not exist (kanji 委 and 奇, words 会員 and
  王女), each left as plain text. A repository-wide link-count scan found no dropped EN link and no Russian-only link.
- The 21 navigation files contain exactly 31 single-line changes that only add link markup. The 51 changed manifest
  entries equal the diff's Markdown files and every Markdown hash matches; the 51 intake paths equal the diff and their
  candidate hashes match.
- No new title equals another card's whole title or segment without a guard. Pairs checked and judged not to need a guard
  include 存在/いる, 委員/議員, 奪う against 盗む, 取る and 与える, 失う against 無くす, 得る and 奪う, 契約/予約, 学期/期間, 奥
  against 中 and 内側, 女王 against 王 and 王様, 俳優 against 歌手, 選手, 演技 and 観客, and 失業 against 仕事, 就職 and 率.
- Optional: a guard 宇宙→世界 (JMdict 世界 sense 1 includes "the universe"; «мир» can mean «вселенная»; low–medium
  confidence); 完了 against 済ませる and 終わり judged not required.
- Limits: two existing cards outside the batch, 向かう (EN 顔) and 汚す (EN 土), lack an EN exclusion in RU; the raw
  SHA-256 of 118 `strokes/*.json` files differs from the manifest, which the reviewer attributed to CRLF/LF normalization;
  and the RU instructions define no Cyrillic-transcription rule, so the cards follow the existing kana-reading convention.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (完全, 学習); scoped coverage **CLEAN**. The other 28 cards and the three restored
lines are clean. K1 and K2 are the report's F1 and F2; the consistency F1 keeps its report label.

- K1 (minor, high confidence), `完全.md:4,12,16,19`: the title «совершенный; безупречный» keeps only the quality sense,
  while line 16 teaches полнота, the first example glosses 完全な as «полное» and the linked `完成.md:31` calls the word
  «полный; совершенный»; a meaning quiz therefore misses the completeness sense the card treats as primary. Evidence:
  JMdict 1211510 "perfect; complete". Remedy proposed: title and H1 «цельный; совершенный», not bare «полный» (一杯's
  title starts with it); in the example, drop «проблемы», which is not in 解決.
- K2 (minor; high confidence on «учебный процесс», medium on «освоение»), `学習.md:4,12`: «освоение знаний; учебный
  процесс» is not JMdict 1206820 "learning; study". «Учебный процесс» is a school's organized instruction, not individual
  study as in lines 19–20, and «освоение» can read as mastery, which line 40 denies. Remedy: «учёба; процесс изучения».

Optional notes: «учебный период» in the 学期 examples (lines 20–21); «Из неприязни к толпе…» for 嫌う:20; a simpler
learned-person sentence in 学者:17–18; a less strong lead than «пристрастие» for 好み; and «в глубину ящика» instead of «в
самую глубину» in 奥:19. The reviewer found no Cyrillic reading, no English gloss a learner must know and no app-quiz
sentence in learner text.

## Exclusion classification

All 32 EN exclusion entries (15 lists) are retained. At the candidate, 13 direct, one-sided entries were added on nine new
cards. The author called one of them required and twelve conservative; the consistency reviewer classified all 13 and
found none unjustified:

| Entry | Author | Consistency reviewer |
|---|---|---|
| 完全→全く | conservative | required (完全に ≈ 全く; shared «совершенн-») |
| 完了→完成 | conservative | required (shared «завершение») |
| 完了→仕舞い | conservative | required (shared «завершение») |
| 完了→終わる | conservative | conservative |
| 完了→終える | conservative | conservative |
| 完了→済む | conservative | conservative |
| 宅→お宅 | conservative | required (shared «дом») |
| 学者→研究者 | conservative | required |
| 存在→ある | required | required (shared «существ-») |
| 嫌う→避ける | conservative | required (嫌う sense 2 "to shun; to avoid") |
| 不思議→謎 | conservative | required (不思議 as noun "mystery") |
| 妙→奇しい | conservative | conservative |
| 好み→好む | conservative | conservative |

The 完了→完成 and 完了→仕舞い entries became exact-segment pairs with the coordinator's 完了 retitle. The correctness reviewer
considered the added guards as direct semantic comparisons without auditing them exhaustively; the comprehensibility
reviewer did not score them.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`212-words-batch-51-recheck-001.md`.
