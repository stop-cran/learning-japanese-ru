# Batch 232 — independent review 001

## Snapshot and scope

- Reviewed commit: `56da736ec2499c2e67dc01cd65078098c31e2716` (tree `e27c0b79e91de862b493efe3dffbc9683aa33060`), branch
  `full-ru-232-words-71`, parent `c82c004`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 231 candidate `5af5353eab033af178249f39b48ac4200abf5c24`.
    Before copying, the coordinator's candidate script checked two things: that the three navigation files edited there
    (`kanji/余.md`, `kanji/帯.md` and `words/余分.md`) were unchanged between `5af5353` and the candidate's parent
    `c82c004`, and that none of the 30 new cards existed in the primary checkout. None of the twelve word cards changed by
        the Batch 231 fix is in this batch's path set.
  - The script byte-compared the 33 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 33 batch paths plus `manifest.json`. Its byte scan of all
    33 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 33 committed
    blobs at `56da736` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from Batch 231; all six restored links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator's only content edits were three `quiz_exclusions`
    appends made in the authoring worktree before the copy. Its adjudication record states:
    - "Content edits by the coordinator: three `quiz_exclusions` appends only, made in `-b216` before the copy after the
      title screen found three unguarded exact title-segment overlaps (方針→線 «линия», 方面→球 «сфера», 作成→建設
      «создание»; see RU-added exclusions below). Otherwise the 33 lane files are copied unchanged from `-b216` (detached
      at the B231 candidate `5af5353`); no held links this batch.";
    - "`type`, `tags`, `level`, `kanji`, `id` and `reading` of all 30 cards equal EN; every EN exclusion is retained in EN
      order.";
    - "Classification: 裏返す:28/43, 遡る:25, 道順:23, 過失:25, 余る:26 and 造船:30–31 mention native/on readings, each
      mirroring an EN body sentence at the same place; no added kango/wago body sentence (B229 lesson honoured).";
    - "RU-added exclusions (7), each one-directional; the targets do not declare them back. From the lane (4): 製作→作製
      (titles share «изготовление»), 余る→残る (残る «оставаться» is a prefix of «оставаться лишним»), 角度→角 (角 «угол»),
      余る→余分 (余分 «излишек; лишний»). Added by the coordinator after the title screen (3), each an exact Russian title
      segment shared with an existing card: 方針→線 (方針 «курс действий; линия (организации, руководства)» ~ 線 «линия;
      провод»; EN "policy; course of action"), 方面→球 (方面 «…; сфера, область (деятельности)» ~ 球 «сфера; мяч», a
      Russian homonym — field vs. geometric sphere; EN "direction; area; field"), 作成→建設 (作成 «составление (документа,
      плана); создание (файла, учётной записи)» ~ 建設 «строительство; создание»; EN "drawing up; document creation").
      Each is conservative: the RU titles are faithful, and the shared bare segment could make the other card's title
      look answerable; appended at the end of the existing list, EN entries and order unchanged. Final screen: 0
      unguarded exact.";
    - "RU-only links (6), each at a substantive comparison that EN makes in plain text (B214/B230 lesson): 郡:18→町, 村,
      市 (EN "towns and villages … a city is not a subdivision of a 郡"); 地帯:40→帯 (replaces EN's English "belt" remark
      with a contrast to standalone 帯); 余る:33→残る and 余る:34→足りる (EN synonym/antonym section). Accepted.";
    - "Navigation: 6 restored links in 3 files, markup only, at EN-linked positions (EN `kanji/余.md` 3, `kanji/帯.md` 2,
      `words/余分.md` 1).";
    - "Lane check after the B231 fix (a1887ba): done. A scan of the 33 lane files for the twelve fix-1 words and their
      old wordings finds only 超過:21 (the Japanese example 重量超過で追加料金がかかりました。, no link and no quoted B231
      title); no B232 draft quotes a B231 title or passage changed by fix 1, so no B232 edit is needed."

    The committed manifest records 5,079 entries (5,074 `files`, 3 images and 2 scenes); the correctness and consistency
    reviewers' `tools/validate.py` runs on the candidate reported 0 errors.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 3 files with 6 restored navigation links (the kanji cards 余 and 帯 and the word card 余分);
    - `manifest.json` (`contentVersion` `963e050e25bb648e`, 5,079 entries);
    - the intake, whose note reads "B232 30-card adaptation with six navigation-only link restorations in three existing
      files; candidate before blind review."
- Published baseline recorded in the intake: `5dfe16c671ca962fb6f24882309b0f4e66c20756` (Batch 231 merge). Parent
  `c82c004` adds only the Batch 231 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on any failing check, passed:
  - `tools/validate.py`;
  - unit tests (the authoring worktree run reported 124 tests);
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 3 files (6 links added, no other change);
  - title screen: no unguarded exact title-segment overlap (47 `OK` lines for pairs already guarded by an exclusion and
    432 stem-only `!!` lines);
  - link parity: no EN link lost where the RU target exists; the RU-only links are the six accepted above, and no
    pre-existing RU-only link sits in a batch path.
- Common sample: all three reviewers read all 30 new word cards in full against EN, and the three navigation-file diffs.
  The consistency reviewer also compared front matter, links and exclusions with EN by script.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file), the six complete RU targets of the added links
    (町, 村, 市, 帯, 残る and 足りる), the exact titles and complete meaning sections of 構成, コース, 針路, 角, 作る, 製造,
    生産 and 余分, and the changed passages of the three navigation files.
  - Inspected the primary Jisho/JMdict entries, readings, senses and word classes for all 30 cards and matched their 30
    cited primary entry IDs to the Jisho pages' JMdict edit links; inspected Daijisen and Seisenban entries separately
    from adjacent aggregator content.
  - Japanese sources beyond Jisho: Digital Daijisen on Weblio for 角度, 公園 and 湯桶読み, and Daijisen entries for 部品
    (部分品), 成分, 郡, 方角, 返る, 造船 and 遡る; the Seisenban 角度 definition and the Nipponica 遠足 section on Kotobank;
    the complete Jisho pages for 連合 (rare 聯合, RENGO) and 越える, and the separate 反る entry 1480170.
  - Russian sources: Gramota's Kuznetsov entries for сырьё, комплектующие, перерасход, ракурс and запчасти; Russian
    Wiktionary for радикал, оплошность, судостроение, верфь and пособие; the academic.ru article «Уезды Японии»
    (terminology only); a CyberLeninka article attesting «тактика лечения».
  - Ran `tools/validate.py` (0 errors) and recomputed the normalized manifest hashes of the 33 changed files (no
    mismatch); ran no generator.
- Consistency review scope:
  - Read all 30 cards in full (front matter and body) and the full diffs of the three navigation files.
  - Programmatic checks against frozen EN: front matter (all keys but `title`), the link multiset per card, link-target
    existence, exclusion lists (order and additions), `link_parity.py` and `tools/validate.py` (0 errors); the SHA-256 of
    every `manifest.json` `files` entry (5,074 entries, 0 stale or missing); the intake's 33 payload paths against the 33
    content files of the diff (all candidate hashes match, no learner content).
  - Screened every batch title against all 3,613 RU word titles (its own segment and whole-word script plus
    `word_title_screen.py` segment hits) and grepped RU titles by keyword. It performed no dictionary lookups.
- Comprehensibility review scope:
  - Read all 30 cards in full; compared EN titles, examples and the named contrasts, and the three link-only navigation
    diffs.
  - Took JMdict senses from the Jisho pages the cards cite; opened Digital Daijisen for 角度, 成分 and 部分品, Jisho 超過
    (JMdict 1429410) and Ozhegov's перерасход on gufo.me for its findings. It used title-screen segment matches as leads
    only and reports a link-parity check     (no EN link whose RU target exists was dropped) and claims no validator
        or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. Each report records
  the snapshot `56da736` with an empty `git status --porcelain`. No fix was applied until all three reports were
  complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No reviewer reported running a generator: the correctness report says no generator was run and
  that repository HEAD, index and working tree remained unchanged; the comprehensibility report claims no validator or
  generator run. No tracked repository file was changed.
- Full blind reports:
  - `232-words-batch-71-review-correctness-001.md`
  - `232-words-batch-71-review-consistency-001.md`
  - `232-words-batch-71-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The consistency brief made the intake record the single exception, for its path and hash check. The correctness report
  says that no author/reviewer reports, tracking records, translation-batch/draft directories or prohibited scratch
  checkouts were read. The consistency report says that it did not read author reports, batch records, drafts or
  tracking; it checked the intake record's payload paths and hashes. The comprehensibility report describes its own
  reads and does not state what it left unread.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for 角度 and 遊園地, **CLEAN** for the other 28 new cards; scoped coverage **CLEAN**
for all 30. The two findings concern inaccurate restrictions, not a missing article or EN example. Russian
comprehensibility and comprehensive quiz safety were not assigned.

- C1 (minor, correctness; high confidence), `角度.md:4,12`: the title and H1 «величина угла (в градусах); ракурс (точка
  обзора)» present degrees as part of the meaning, whereas the word also denotes angular magnitude in radians or other
  units; the body's correct note does not remove the misleading qualification. Remedy: «величина угла; ракурс (точка
  обзора)»; the exclusion of 角 can remain. Evidence: Digital Daijisen 角度 sense 1 (ラジアン・度・分・秒); the Seisenban
  definition 1 on Kotobank (`角度-460585`); EN "angle; viewpoint" is unrestricted.
- C2 (minor, correctness; high confidence), `遊園地.md:31–32`: «…там можно отдыхать или играть, но это не парк
  аттракционов» turns EN's possible distinction into a categorical exclusion, teaching that a 公園 cannot be an
  amusement park. Remedy: «[公園](公園.md)（こうえん）— общественный парк: там можно отдыхать или играть, но он не
  обязательно является парком аттракционов.» Evidence: Digital Daijisen 公園 sense 1 includes publicly provided 庭園や遊園地;
  EN 遊園地:32 says a park "can be a place to relax or play without being an amusement park". It does not itself recommend
  a quiz-exclusion change.

What the reviewer confirmed:
- No removed source field or exclusion (six cards add exclusions); every EN link whose RU target exists remains linked;
  the new cards have no missing relative target; the main Japanese examples and readings are preserved.
- Masculine first-person past forms and contextual «я/мы/у нас» are legitimate concrete translations, not claims that
  Japanese marks the speaker; «давал почитать», «ко мне» and «туда» fit their examples.
- 成分's «состав продукта» is supported by JMdict's composition gloss; «запчасть» and «перерасход» are legitimate narrower
  contextual equivalents beside broader first glosses; the phrase-like glosses in 方面, 道順 and 過半数 are explained by the
  noun labels and constructions.
- Removing the English-only compatible/frame warnings is justified, and the plain pointer to the untranslated かえる
  article is not a broken link.
- Russian terms are attested: сырьё, комплектующие, перерасход, ракурс (sense 3, viewpoint) and запчасти (Kuznetsov);
  радикал as иероглифический ключ, оплошность, судостроение, верфь and пособие (Wiktionary); «Уезды Японии» for 郡; «тактика
  лечения» as a contextual 方針 rendering.
- Daijisen confirms 部品 as shortened 部分品, 成分's extensions, 郡's historical こおり, 方角's extensions, 返る's 裾が返る,
  造船's タンカーを造船する and native-first/on-second 湯桶読み; Nipponica supports 遠足 as day trips by bus or train with
  varied school groupings, so «выезд классом» is a concrete school-context rendering; Jisho marks 聯合 as rarely used.

Optional: none required. Limits: no native-speaker, device, media, archive or learning-effectiveness testing; not every
supplementary comparison ID was re-fetched, nor every suggested comparison article read in full; some Gramota requests
returned HTTP 429 and direct Wiktionary requests 403, after which the entries were read through another fetch path; the
current Daijisen 遡る entry does not print the string 四月に遡って適用する, whose retroactive sense rests on JMdict sense
2; oversized initial outputs were not treated as full reads, and all 30 pairs were reread in bounded two-pair reads.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **CLEAN**; scoped coverage of cross-file integration **CLEAN**. Findings: none
actionable. Russian prose accuracy was not line-reviewed in this facet.

What the reviewer confirmed:
- For all 27 cards with EN `quiz_exclusions`, the RU list equals the EN list in EN order, with additions only at the end
  (方針 +線, 角度 +角, 方面 +球, 作成 +建設, 製作 +作製; 余る a new key with 残る and 余分); 部首 and 遊園地 have no key, as
  in EN. Front matter differs from EN only in `title` and these additions.
- No RU link is lost where the RU target exists. Links removed because the target is absent (text kept plain): 資料,
  kanji 裏, いってらっしゃい, the article kaeru-change-replace-and-return, kanji 角 (from 方角 and 角度), kanji 針, kanji 順,
  kanji 超, 娯楽, 制作 and kanji 造. Links added, all resolving: 郡→市/町/村, 地帯→帯, 余る→残る/足りる.
- The navigation files are byte-identical apart from link brackets and hrefs, at the EN positions and in EN's path forms:
  余 lines 21, 37 and 50 (prose, あま.る row, word list); 帯 lines 28 and 39 (タイ row, word list; 包帯 correctly plain,
  with no RU card); 余分 line 28 (`余る.md`).
- Manifest hashes match every entry; the commit holds 35 files (30 cards, 3 navigation files, manifest and intake).
- Declined pairs judged from titles, for example 原料–部品, 方角–角度, 過半数–半分 and 統一–会/組合 (shared «объединение»,
  separated by qualifiers, EN also unguarded), need no guard.

Optional: O1 (very low): 部首 «ключ иероглифа (для поиска в словаре); радикал» and 鍵 «ключ» share «ключ»; the qualifier
makes 部首 unambiguous, and EN has no guard; `quiz_exclusions: [鍵]` on 部首 would be a content decision, not required.
O2 (very low): 方面 «в сторону (какого-либо места)» partially overlaps あちら «вон там; в ту сторону» (and そちら «туда; ваша сторона»); no guard needed. O3
(cosmetic): `お帰り.md:28` mentions 帰る plain, as EN does. O4 (outside the batch): `kanji/余.md:21` keeps its pre-existing
bare gloss «оставаться; быть в избытке», closer to 残る; prose edits are outside the navigation-only scope. Limits: no
dictionary lookups (sense statements rest on the cards' citations and general knowledge, so necessity classes are
judgements); Russian prose was not line-reviewed; the stem screen was heuristic (about 431 stem pairs not all inspected);
EN cards that exclude batch words (余計, 制作, 脱線) have no RU file.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (twelve minor items); scoped coverage **NEEDS FIX** for 成分 only, **CLEAN** for
the other 29.

- C1 (minor; high confidence), `角度.md:4,12,37-38`: «величина угла (в градусах)» restricts the measure to degrees, while
  the card's own note says degrees are one unit (Daijisen sense 1). Remedy: drop «(в градусах)».
- C2 (minor; high confidence), `方面.md:4,12`: the lead gloss «в сторону (какого-либо места)» is a prepositional phrase,
  not a noun answer, and bare «сфера» is 球's lead title. Remedy: «направление (к месту); область деятельности».
- C3 (minor; high confidence), `道順.md:4,12`: the lead gloss «как пройти (куда-либо)» is a clause. Remedy: «маршрут (по
  улицам); объяснение пути».
- C4 (minor; high confidence), `遡る.md:4,12`: «(вести отсчёт назад)» reads as counting backwards. Remedy: «подниматься
  вверх по течению; восходить к прошлому».
- C5 (minor; high confidence), `作製.md:20`: «Мы готовим чертёж новой детали.» uses 作る's gloss «готовить». Remedy: «Мы
  изготавливаем чертёж новой детали.»
- C6 (minor; high confidence), `原料.md:20`: «Эту бумагу делают из древесины.» drops the raw-material role just taught.
  Remedy: «Для этой бумаги сырьём служит древесина.»
- C7 (minor, also coverage; high confidence), `成分.md:20,31-36`: «Я изучил состав продукта» uses 構成's lead title
  «состав», and the synonym section never contrasts 構成. Remedy: «Я изучил компоненты продукта.» plus a 構成 contrast
  sentence. Evidence: Digital Daijisen 成分 sense 1.
- C8 (minor; high confidence), `部品.md:4,12,39`: «запчасть» means a spare part, whereas Daijisen 部分品 is a component.
  Remedy: «деталь (механизма, устройства); комплектующая».
- C9 (minor; high confidence), `超過.md:4,12`: «перерасход» is overspending, while JMdict 1429410 and the examples are
  about exceeding a limit. Remedy: «превышение (лимита, нормы)». Evidence: Jisho 超過; Ozhegov via gufo.me.
- C10 (minor; high confidence), `超過.md:49` (the line is 48): «Метка N2 взята из закреплённого списка слов сообщества.»
  is an author-facing provenance note. Remedy: delete it.
- C11 (minor; high confidence), `過剰.md:19`: «вредно для здоровья» is stronger than 体によくありません. Remedy:
  «Чрезмерное беспокойство нехорошо для здоровья.»
- C12 (minor; high confidence), `逸れる.md:16,18` (the ball example is on line 19): «пролетать мимо цели» and «Мяч
  пролетел мимо мишени» add flight, which neither the Japanese nor EN "went wide of the target" has. Remedy: «проходить
  мимо цели» and «Мяч прошёл мимо мишени.»

Optional: 角度 «точка зрения» instead of «ракурс» (Ozhegov sense 3 makes «ракурс» not a false sense); 過失's order of
«оплошность» and «вина по небрежности»; 方角's narrower lead; 遠足's «на один день»; 道順:19 «туда»; 原料:21; 方針:19;
過半数:9; 作製:19 «сделали»; 逸れる is the only added-manner case promoted. Limits: no native-speaker check; JMdict senses
from the Jisho pages the cards cite; quiz-exclusion symmetry not assessed (作製 does not list 製作; 余る does not list 足りる);
unlinked 資料, いってらっしゃい, 娯楽, 制作, 観点, 半数, 逸らす, はぐれる and the かえる article pointer have no RU target; no
validator, generator or full reread of every EN synonym paragraph claimed.

## Exclusion classification

All 177 EN exclusion entries (27 lists) are retained in EN order; 部首, 余る and 遊園地 have none. Twenty-three of them lie
inside the batch. At the candidate, seven direct, one-sided entries were added on six new cards; one of them (余る) is a
new list, and none targets a batch word except 製作→作製.

| Entries | Consistency reviewer |
|---|---|
| 製作→作製, 余る→残る (2) | REQUIRED: 製作 and 作製 share «изготовление»; 残る «оставаться» is the whole prefix of 余る «оставаться лишним…», so either answer is defensible; keep |
| 余る→余分, 角度→角, 方針→線, 方面→球, 作成→建設 (5) | CONSERVATIVE: real shared-gloss basis («лишний», «угол», «линия», «сфера», «создание»), necessity unestablished; harmless, keep |

余る→余分 rests on «лишним» against 余分 «излишек; лишний», with different parts of speech; 角度 «величина угла» against
角 «угол»; 方針 «линия (организации, руководства)» against 線 «линия; провод», 方面 «сфера, область (деятельности)» against
球 «сфера; мяч», and 作成 «создание (файла, учётной записи)» against 建設 «строительство; создание» are Russian homonymy or
qualified senses. All seven entries are kept. The correctness reviewer noted that six cards add exclusions without
removing any, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`232-words-batch-71-recheck-001.md`.
