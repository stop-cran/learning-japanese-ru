# Batch 233 — independent review 001

## Snapshot and scope

- Reviewed commit: `5218a9afd4d733f79b5d88fc1f826c760dd93a8c` (tree `3aadf38b46b2d7b39f480ddaf01b9007deb5a244`), branch
  `full-ru-233-words-72`, parent `fad19b9`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 232 candidate `56da736ec2499c2e67dc01cd65078098c31e2716`.
    Before copying, the coordinator's candidate script checked two things: that the three navigation files edited there
    (`articles/numbers-and-counters.md`, `kanji/効.md` and `words/開放.md`) were unchanged between `56da736` and the
    candidate's parent `fad19b9`, and that none of the 30 new cards existed in the primary checkout. None of the eleven
    word cards changed by the Batch 232 fix is in this batch's path set.
  - The script byte-compared the 33 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 33 batch paths plus `manifest.json`. Its byte scan of all
    33 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 33 committed
    blobs at `5218a9a` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from Batch 232; all three restored links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator's only content edits were three `quiz_exclusions`
    appends made in the authoring worktree before the copy. Its adjudication record states:
    - "Content edits by the coordinator: three `quiz_exclusions` appends only, made in `-b216` before the copy, after the
      title screen found three unguarded exact title-segment overlaps that the author had declined as told apart by
      parenthetical qualifiers (成立→教育 «образование», 成立→納得 «принятие», 通用→過ぎる «проходить»; see RU-added
      exclusions below). This applies the B232 coordinator lesson: the screen strips parentheticals, and a qualified
      segment can still make the other card's bare segment look answerable. Otherwise the 33 lane files are copied
      unchanged from `-b216` (detached at the B232 candidate `56da736`); no held links this batch.";
    - "`type`, `tags`, `level`, `kanji`, `id` and `reading` of all 30 cards equal EN; every EN exclusion is retained in
      EN order (checked field by field against frozen EN).";
    - "Classification: RU renders EN's katakana reading sentences ("The readings are X + Y" / "Read X + Y" / "…: X + Y")
      as «Онные чтения — X + Y» in 速達, 時速, 速力, 通路, 紙幣, 通貨, 通訳, 通知, 効力, 成立, 妥当, 回転, 通用, 通帳, 通勤,
      送料, 透明 and 解放; the katakana already marks on readings, and 27 published RU cards use the same wording for EN's
      unlabelled form (37 use plain «Чтения —»). Native-reading mentions (通知:33, 回転:32, すれ違う:29, 通り掛かる:31,
      這う:32, さわやか:26–27, 清い, 透き通る:28, 澄む:29, 逆さま:26, 逆さ:27) each mirror an EN body sentence; no added
      kango/wago body sentence (B229 lesson honoured).";
    - "RU-added exclusions (10), each one-directional; the targets do not declare them back. From the lane (7, all
      judged conservative by the author): 速達→郵送 (postal sending), 時速→高速 and 速力→高速 (stem «скорост-», speed
      neighbours), 通路→通過 (shared noun «проход»), 出勤→就職 («выход на работу» can be read as starting a job), 通用→納得
      («быть принятым … (о доводах)» vs «принятие (доводов)»), 成立→契約 (the body teaches 契約が成立する). Kept: each is
      harmless and the 通用/成立 ones now share 納得 with the coordinator guard. Added by the coordinator after the title
      screen (3), each an exact Russian title segment once parentheticals are stripped: 成立→教育 (成立 «…; образование
      (организации)» ~ 教育 «образование; обучение»; EN "formation; conclusion; validity" vs "education"), 成立→納得 (成立
      «…; принятие (закона)» ~ 納得 «убеждённость; принятие (доводов)»; EN "acceptance; being convinced"), 通用→過ぎる
      (通用 «…; проходить (о доводах, отговорках)» ~ 過ぎる «проходить; миновать»; EN "be accepted; be valid" vs "pass;
      go beyond"). Appended at the end of the existing list; EN entries and order unchanged. Final lane screen: 0
      unguarded exact, 52 guarded.";
    - "RU-only links: none (link parity clean over the 30 cards and 3 navigation files).";
    - "Navigation: 3 restored links in 3 files, markup only, at EN-linked positions (EN `kanji/効.md` → 効力,
      `words/開放.md` → 解放, `articles/numbers-and-counters.md` → 時速; the second plain 時速 mention in the article stays
      plain as in EN).";
    - "Footers of 成立 and すれ違う put the Daijisen link inside the «Словарь» line, mirroring EN's footer shape; no
      normalisation.";
    - "Lane check after the B232 fix: none of the 34 changed lane paths quotes a B232 passage or title changed by fix
      97a39cf (方面, 道順, 遡る, 部品, 超過, 角度, 作製, 原料, 過剰, 逸れる, 遊園地, or their old wording); B233 titles are
      screened against the fixed B232 titles at candidate time.";
    - "Unverified Russian words for the correctness reviewer: «сберегательная книжка», «скорость хода», «циркуляция»,
      «разминуться», «высвобождение (памяти)», «стоимость пересылки»."

    The committed manifest records 5,109 entries (5,104 `files`, 3 images and 2 scenes); the correctness and consistency reviewers'
    `tools/validate.py` runs on the candidate reported 0 errors.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 3 files with 3 restored navigation links (the kanji card 効, the word card 開放 and the article
      numbers-and-counters);
    - `manifest.json` (`contentVersion` `398922b5be16e31e`, 5,109 entries);
    - the intake, whose note reads "B233 30-card adaptation with three navigation-only link restorations in three
      existing files; candidate before blind review."
- Published baseline recorded in the intake: `05160ca1d07f96bc8c7baa2f1fa05509fdce6573` (Batch 232 merge). Parent
  `fad19b9` adds only the Batch 232 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests (the authoring worktree run reported 124 tests);
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 3 files (3 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen: no unguarded exact title-segment overlap (52 `OK` lines for pairs already guarded by an exclusion and
    374 stem-only `!!` lines);
  - link parity: no EN link lost where the RU target exists and no RU-only link; for this record, no pre-existing RU-only
    link sits in a batch path.
- Common sample: all three reviewers read all 30 new word cards in full against EN, and the three navigation-file diffs.
  The consistency reviewer also checked front matter, links and exclusions against EN, and the intake and manifest
  hashes.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file), the complete comparison cards お金, きれい,
    速度, 高速, 有効, 放す, 通る, 逆 and 反対, the binding RU instructions and reference, and the complete link-only diffs of
    the three navigation files.
  - Inspected the JMdict-backed Jisho API entries for every headword, selecting the exact spelling and reading, with all
    senses, word classes, restrictions and notes; the Jisho 逆さま search page, whose Notes mark 逆様 as a rarely used
    kanji form; and the Jisho kanji entries 幣, 妥, 帳 and 透.
  - Japanese sources beyond Jisho: Digital Daijisen on Weblio for 成立, 通用, 紙幣, 通貨, 通帳 and 透き通る.
  - Russian sources: Gramota's Kuznetsov entries for сберегательный, циркуляция, разминуться, купюра, валюта, оборот,
    высвободить, явка and пересылка; Russian Wiktionary несостоятельный; the Samoylov maritime-dictionary entry «Скорость
    хода корабля» on academic.ru; the Почта России «Посылка Стандарт» page for «Стоимость пересылки» (expressions, not
    frequency).
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 cards in full (front matter and body) against EN and the full diffs of the three navigation files.
  - Checked front matter and key order, the links of each card, link counts in existing RU files that point at the new
    cards, the exclusion lists (order and additions), the intake's 33 payload paths and hashes against the content diff,
    and the manifest hashes of the 33 changed files; ran `tools/validate.py` (0 errors).
  - Screened batch titles against RU word titles by reading and targeted comparison, not by an exhaustive tool run. It
    performed no dictionary lookups.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN; compared the titles of the named near-synonym cards; read the learner diffs of
    the three navigation files (link additions only).
  - Took JMdict senses from the Jisho API display and the cards' cited entry numbers, and used the in-repo 効果 card. It
    ran `link_parity.py` on the 30 paths (it printed only `checked 30`) and used title-screen segment matches as leads
    only; it records no validator or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. Each report records
  the snapshot `5218a9a` with a clean tree. No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No reviewer reported running a generator: the correctness report says no generator, commit,
  stage, push, branch switch or issue action was run and that the final HEAD and status still showed the exact candidate
  with an empty porcelain status; the consistency report says no generators were run (only `tools/validate.py`); the
  comprehensibility report records no validator or generator run, and its recheck says no generator was run. No tracked
  repository file was changed.
- Full blind reports:
  - `233-words-batch-72-review-correctness-001.md`
  - `233-words-batch-72-review-consistency-001.md`
  - `233-words-batch-72-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The consistency brief made the intake record the single exception, for its path and hash check. The correctness report
  says that no author/reviewer reports or restricted batch/tracking/draft records were consulted. The consistency report
  says that no author reports, other reviewer reports, translation drafts, translation tracking or scratch worktrees
  were read; it checked the intake record's paths and hashes only. The comprehensibility report says that the intake,
  batch records and author reports were not read.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **CLEAN** for all 30 new cards; scoped coverage **NEEDS FIX** for 成立 only (title only), **CLEAN**
for the other 29. The 成立 body itself retains all three senses. Comprehensibility and comprehensive quiz-pair
adjudication were not assigned.

- F1 (minor, scoped coverage; high confidence), `成立.md:4,12` (compare :16–21): the title and H1 «заключение (договора,
  сделки); принятие (закона); образование (организации)» restrict the glosses to agreements, laws and organizations and
  drop the argument-validity meaning, one of the EN title's three core meanings ("formation; conclusion; validity"),
  which the RU opening definition teaches and the second main example shows. Remedy: append «; состоятельность (довода)»
  to the title and H1, or shorten the label while keeping formation, agreement-conclusion and argument-validity; no
  change to the Japanese example or its translation «Этот довод несостоятелен» is needed. Evidence: Jisho/JMdict 成立
  entry 1375880, sense 3 "being valid (of a theory, argument, etc.); holding; applying"; Russian Wiktionary
  несостоятельный, sense 4 (lacking substantiation, proof or persuasiveness). Impact minor, because the body and example
  already explain it.

What the reviewer confirmed:
- Main sense counts and parts of speech agree with the JMdict-backed entries, including 速達's transitive する, 妥当's
  additional intransitive する, 通用's three senses, 回転's mathematical and slalom uses and 澄む's phonetic use; the 逆さ
  entry confirms its abbreviation tag and 倒さ form, and the other entries confirm 擦れ違う, 清む and 爽やか.
- Digital Daijisen supports 通用 sense 2 (世界に通用する新技術), 紙幣 as しへい money apart from しべい, 通貨 including
  預金通貨 as well as 現金通貨, 通帳's つうちょう heading for deposits and credit transactions, and 透き通る sense 2 (clear,
  well-heard sound).
- Explicit «онные» accurately clarifies EN's unclassified readings; the components without EN cards (幣 ヘイ, 妥 ダ, 帳
  チョウ, 透 トウ) match the Jisho kanji entries; native-word passages have EN counterparts.
- Russian terms are attested: сберегательная книжка, циркуляция, разминуться (both senses), купюра, валюта, оборот (with
  «смена клиентов» disambiguating), высвободить (computing sense of 解放, no file-erasure claim), явка, пересылка,
  «скорость хода» and «стоимость пересылки».
- Every example translation matches the Japanese: masculine past forms and supplied subjects are example-speaker choices,
  «переводил» does not make ました present, «несостоятелен» keeps the negative judgement, «освободившись» keeps the freed
  speaker beside the explicit passive note, and «разминулись»/«упустил» keep the unwanted result; no tense, polarity or
  argument-role error remains.
- The English-dependent adaptations keep their Japanese distinctions; no identity, reading, type, JLPT, kanji or tag
  value, main Japanese sentence or kana reading is lost; no local link is broken and no EN link whose RU target exists is
  dropped; original exclusions remain and seven cards add RU exclusions. Unavailable targets and EN's unlinked 透明
  mention are not defects.

Optional: outside the assigned facets, add the missing spaces after the comparison links in `さわやか.md:30–36` (notably
`すっきり` followed immediately by «пересекаются»); rendering polish, not a Japanese correctness defect. Limits: bounded
translation review, not native-speaker certification, a whole-corpus audit, app/device acceptance or exhaustive quiz
review; only the nine named comparison cards were read completely; not every comparison entry number or Weblio footer was
re-resolved; Gramota intermittently returned HTTP 429, and a failed Jisho `/word/逆さま` request was replaced by the
successful search page; failed requests and search summaries were not treated as verification.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **CLEAN**; scoped coverage of cross-file integration **CLEAN**, with one
minor optional link item. Findings: none actionable. Russian prose accuracy and dictionary senses were not assigned to
this facet.

What the reviewer confirmed:
- Front matter (word, reading, jlpt, type, kanji, tags) and key order match EN for all 30 cards.
- RU links equal EN links, except for kanji links whose RU kanji files do not exist (貨, 訳, 清, 逆 and similar), which are plain text;
  no dead link target and no extra link.
- Link counts in existing RU files that point at the new cards match EN; EN files that link to the new cards but have no
  RU file yet (ラッシュアワー, 入社, 出張, 放れる, 濁る, 純情, 純粋, 訳す, 巡る) are out of scope.
- The three navigation diffs change only link brackets and hrefs and match EN.
- The intake's 33 payload paths equal the 33 content-diff paths and each candidate hash matches; it holds hashes and paths
  only. The 33 changed manifest hashes match the working tree.
- All EN exclusions are retained in EN order, every target exists and no pair is duplicated one-way.

Optional: O1 (minor; medium confidence): 透明 is compared substantively in 透き通る's synonym section but left unlinked;
EN also leaves it unlinked, and the reviewer did not find this to be a defect. O2 (cosmetic): missing spaces in
`[すっきり](すっきり.md)пересекаются` and `[はきはき](はきはき.md)— «…` in さわやか. O3 (cosmetic): `[はっきり](はっきり.md)（はっきり）`
in 澄む and 透き通る repeats a redundant reading that EN does not have. O4: the classification of the ten RU-added
exclusions (below). O5: the declined pairs 通り掛かる–たまたま/偶然/出会う, 妥当–申し訳/よろしい, 透明–見える, 通勤–通学,
解放–空く, 送料–配達 and 通帳–貯金 have visibly different titles and are acceptable unguarded. Limits: 118 `strokes/*.json`
entries hash differently from the Windows working tree, which the reviewer attributed to line endings, pre-existing and
unchanged by this diff, without confirming the manifest's normalisation; no dictionary or native-speaker re-verification;
the screen of all RU word titles was done by reading and targeted comparison, not an exhaustive tool run.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (eleven minor items in 通路, 通貨, 効力, 出勤, すれ違う, 通り掛かる, さわやか, 清い,
逆さ and 送料); **CLEAN** for the other 20 cards; scoped coverage **CLEAN** for all 30.

- C1 (minor; high confidence), `送料.md:44-45`: «Защита теста…» is app-test meta, not a Japanese distinction, and the
  sentences above already separate shipping charge, quoted price and free shipping. Remedy: delete lines 44–45.
- C2 (minor; high confidence), `通貨.md:42`: «ответами в викторине» talks about quiz behaviour. Remedy: «Эти различия не
  делают широкие названия денег взаимоисключающими.»
- C3 (minor; high confidence on «к», medium that the verb alone would be unacceptable), `出勤.md:19`: «к девяти» means by
  nine and «выхожу» reads as leaving home, against the card's note and 九時に. Remedy: «Завтра я приступаю к работе в
  девять.»
- C4 (minor; high confidence), `通り掛かる.md:21,45`: «проходил мимо» is 通り過ぎる's quiz title and drops the chance
  element. Remedy: add «случайно» in both places. Evidence: Jisho 通り掛かる sense 1 "to happen to pass by".
- C5 (minor; high confidence), `すれ違う.md:20`: «я прошёл мимо учителя» shows one person passing. Remedy: «В коридоре я
  разошёлся с учителем.»
- C6 (minor; high confidence), `効力.md:24-25,29,42`: the card points a substance or treatment to «действенность» or
  «эффективность», 効果's published glosses. Remedy: «сила действия средства» at 24–25, a line-29 rewording and «сила
  действия» at 42.
- C7 (minor; high confidence), `清い.md:16,20`: «прозрачный/прозрачная» is 透明's lead gloss. Remedy: «чистый,
  незамутнённый» and «чистая, незамутнённая вода».
- C8 (minor; medium confidence), `逆さ.md:4,12`: bare «наоборот» also means "on the contrary", near 反対 and 逆. Remedy:
  «вверх ногами; в обратную сторону».
- C9 (minor; medium confidence), `さわやか.md:21`: «Он» adds a male third person the Japanese lacks. Remedy:
  «Поздоровался ясным, приятным голосом.»
- C10 (minor; high confidence), `さわやか.md:31,35-36`: missing spaces glue the links to the next word. Remedy: add them.
- C11 (minor; high confidence), `通路.md:4,12`: «проход для людей» reads as a pedestrian passage, while line 16 says people
  or vehicles. Remedy: «проход (между рядами, сиденьями); путь для прохода».

Optional: 通用's verbal title matches EN; 澄む's change-of-state title sits beside state examples explained at lines 23–24;
the 有効 and 知らせ overlaps match dictionary senses; 紙幣 and 札 share «бумажные деньги», distinguished by the 千円札 note;
成立's «образование (организации)» is qualified against 教育; 解放されて as «Освободившись»; 透き通る's slightly broad lead;
さわやか «в комнату» / «подул». None was scored. Limits: JMdictDB asked for a password, so senses are from the Jisho API
display of JMdict, the cards' cited entry numbers and the in-repo 効果 card; no native-speaker check; quiz-exclusion diffs,
tags and manifest hashes were not scored; «годан», «окуригана» and «онные чтения» were treated as established corpus
terms; unlinked absent targets are not defects.

## Exclusion classification

All 165 EN exclusion entries (29 lists) are retained in EN order; 通帳 has none. Twenty-two of them lie inside the batch.
At the candidate, ten direct, one-sided entries were added on seven new cards, none of them a new list and none targeting
a batch word.

| Entries | Consistency reviewer |
|---|---|
| 通路→通過, 成立→教育, 通用→過ぎる, 時速→高速, 速力→高速 (5) | Required or justified: shared «проход», «образование», «проходить» and «скорость» |
| 速達→郵送, 成立→契約, 成立→納得, 通用→納得 (4) | Conservative, harmless |
| 出勤→就職 (1) | Weakest: the titles share no wording; harmless but arguably unnecessary |

The author judged all seven lane entries conservative; the coordinator added 成立→教育, 成立→納得 and 通用→過ぎる as exact
segments once parentheticals are stripped. The reviewer's classes differ in places from those reasons (for example, it
classed 成立→納得 as conservative and 時速→高速 and 速力→高速 as justified). All ten entries are kept; 出勤→就職 keeps the
author's reason that «выход на работу» can be read as starting a job, near 就職 «поступление на работу». The correctness
reviewer noted that seven cards add exclusions without removing any, and the comprehensibility reviewer did not score
the guards.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`233-words-batch-72-recheck-001.md`.
