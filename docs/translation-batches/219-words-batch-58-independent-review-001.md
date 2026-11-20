# Batch 219 — independent review 001

## Snapshot and scope

- Reviewed commit: `f72537721d86b0d72485aecb4a758b10ef241a20` (tree `ea1be965b31c1cc36dc04bbe0cacaaacc3b3e6b5`), branch
  `full-ru-219-words-58`, parent `e2ff180`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 218 candidate `4cc28f4411ca8c4cc1d94c5a7cfc02e25752f746`.
    Before copying, the coordinator checked two things: that the 17 navigation files edited there were unchanged between
    `4cc28f4` and the candidate's parent `e2ff180`, and that none of the 30 new cards existed there. The Batch 218 fixes
    touched only 以来, 仲間, 任せる, 休憩, 会員, 住民, 何とか, 余分 and 例え; of these only 以来 is in this batch's path set,
    and it was not copied from the scratch worktree (see the held link below).
  - The coordinator byte-compared the 47 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 48 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - One held wrap was carried into this batch: Batch 218's 以来 had left its EN link to 今後 as plain text because 今後 is
    a Batch 219 word. The coordinator wrapped that mention at EN's position (以来 line 29) in the primary checkout, on top
    of the published, fixed 以来 card; it is the only change to that card.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 18 files with 23 restored navigation links (including the held 以来→今後 link);
    - `manifest.json` (`contentVersion` `bc7ef19587f3f1e0`, 4,689 entries);
    - the intake.
- Published baseline recorded in the intake: `fcc56087238d3cba6e5bb8230a4e6200bcf3604f` (Batch 218 merge). Parent
  `e2ff180` adds only the Batch 218 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK;
  - content budget: OK, 4,706 entries / 13.32 MB inflated;
  - navigation-only check: 18 files and 23 links, with no problem;
  - title screen: no unguarded exact title-segment overlap;
  - link parity: six RU-only links (主に→だけ, 予報→天気予報, 事務→事務所, 今にも→今に, 今回→最近 and 代理→本人), each to
    a target that EN mentions without a link.
- Common sample: all three reviewers read all 30 new word cards in full.
  - Correctness and comprehensibility read each card against its full EN original.
  - Consistency compared each card's front matter, link targets and exclusions with EN.
- Correctness review scope:
  - Read in full the existing RU 最近, 今に, 事務所, だけ, 本人, 天気予報 and 以来 (the six RU-only link targets and the
    held-link card); read only metadata, meaning and examples of これから, ほとんど, まず, もうすぐ, 一緒, 中学校, 乗る, 予想,
    予期, 代わり, 前 and 仕事; inspected the navigation-only diffs and the reading metadata of 以 and 際.
  - Read the JMdict-backed Jisho API records for all 30 headwords and the six RU-only link targets (だけ through 丈/だけ);
    Digital Daijisen on Kotobank for 今に, 今にも and 専業主婦.
  - Russian sources: Kuznetsov entries on Gramota (изменить, толчея, представительство, общественность, наперёд), the
    Universal Dictionary on Gramota (заместитель) and Russian Wiktionary (толчея, смета, канцелярский, искусственный,
    назад, хозяйка, того и гляди, прогнозирование). HTTP 429/403 failures were replaced by successful fetches, and a
    misdirected Kotobank page was discarded; neither was treated as evidence.
  - Ran `tools/validate.py` (0 errors). It ran no generator.
- Consistency review scope:
  - Read all 30 cards and all 18 navigation diffs in full.
  - Checked the manifest (`contentVersion` and the hashes of the changed and new files) and the intake path list
    (48 payload paths, equal to the content diff; no held paths; no learner content).
  - Confirmed that the absent link targets デート, 世の中 and the kanji cards 算 and 測 are absent.
  - Classified the RU-added exclusions from the RU titles and from JMdict senses read through Jisho. It ran
    `tools/validate.py` (0 errors) and used the title-screen and link-parity tools only as leads.
  - It reported, as an unconfirmed limit, that 110 `strokes/*.json` files did not match their manifest hashes in a
    working-tree check. The coordinator withdrew this by evidence, as in Batches 217 and 218: `tools/build_manifest.py`
    hashes the bytes after CRLF→LF normalisation, the stroke blobs are CRLF byte copies marked `-text`, and the batch
    touches no stroke file.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN; read 以来 in full; compared the RU titles and named contrasts of 前, これから,
    将来, 今度, もうすぐ, 今に, 代わり, 社会, 予想, 天然, 混雑 and 大勢; read the link-only diffs of the other 17 navigation
    files.
  - Read JMdict entries through the Jisho API (JMdictDB required a password) and dictionary entries from Ozhegov,
    Kuznetsov, Efremova and Ushakov on gufo.me and dic.academic.ru.
  - Used the link-parity check only as a lead: no EN link whose RU target exists was dropped. It did not run the content
    validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier.
- Reviews ran serially, one reviewer at a time. Each report records the snapshot `f725377` with an empty
  `git status --porcelain`. No fix was applied until all three reports were complete, and the coordinator confirmed
  afterwards that HEAD was still `f725377` and that `git status --porcelain --ignored` was empty.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `219-words-batch-58-review-correctness-001.md`
  - `219-words-batch-58-review-consistency-001.md`
  - `219-words-batch-58-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`, except
    that the consistency reviewer checked only the intake's path list;
  - the scratch worktrees;
  - one another's reports.

  The correctness report confirms that it read no author, reviewer or batch record or other session file. The
  comprehensibility and consistency reports do not restate the rules.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** (C1–C3, all minor; the other 27 cards are clean in this facet). Scoped coverage
**CLEAN** for all 30 cards and the reviewed navigation changes.

- C1 (minor; high confidence), `主義.md:19`: 彼は自分の主義を変えませんでした ("He did not change his principles") became
  «Он не изменил своим принципам». With the dative, изменить means betraying or abandoning one's principles, which
  imports a loyalty judgment and changes the lesson on 変える. Remedy: «Он не изменил свои принципы.» Evidence: JMdict
  変える sense 1 "to change; to alter; to transform"; Kuznetsov «изменить» 1 («Сделать иным; переменить») against
  «изменить» 2, sense 3 («Нарушить верность чему-л.», with the example «И. своим принципам»).
- C2 (minor; high confidence), `今にも.md:29`: the RU-only 今に comparison ended «оно не описывает того, что уже вот-вот
  произойдёт», a categorical ban that Digital Daijisen 今に 1 contradicts (a near-future inference, with the example
  この空では今に雨が降る). The difference is one of emphasis. Remedy: «…оно само по себе не подчёркивает непосредственную
  близость события так, как 今にも.» Evidence: Daijisen 今に and 今にも; JMdict 今に "before long".
- C3 (minor; high confidence on scope and register), `人込み.md:4,12,16`: the unqualified title gloss «толчея» is
  colloquial and names jostling or a crush, not merely a dense crowd. Remedy: the title gloss «толпа людей», or
  «толчея» only as a qualified contextual translation. Evidence: JMdict 人込み sense 1 "crowd of people"; Kuznetsov
  «толчея» 1, sense 1 «Разг. Давка, толкотня»; Russian Wiktionary «толчея».

What the reviewer confirmed:
- All source metadata, EN exclusions, Japanese examples, citations and teaching rules survive; no EN link to an existing
  RU target was dropped, missing targets stay plain text, and the restored 以来→今後 link is accurate. English-only
  remarks were appropriately omitted.
- The six RU-only comparisons keep their teaching point (subject to C2).
- 代表 «представительство» is attested in the activity sense (Kuznetsov sense 2), and 代理 «заместитель» has the
  general substitute sense, so neither title alone establishes an office or job restriction. 予算 «смета», 事務
  «канцелярская работа» and 交際's general and dating senses are supported.
- 世間's news example permits «внимание общественности», and the card retains everyday social judgment; «общественность»
  is narrower, but no lost taught sense was established.
- The «искусственный» note (Wiktionary sense 3, «деланый, неискренний»), the temporal «назад» note in 以前, «хозяйка
  дома» in 主婦 and 専業主婦 (Daijisen) are accurate; 中学 keeps the lower-secondary stage and abbreviation; 仏's uses,
  乗客's readings, 乗せる's class and its 載せる-only publication restriction, and the katakana ゴ in 互い are preserved.

Optional: «того и гляди» is colloquial but semantically supports imminence; «предварительная оценка» is more neutral than
«оценка наперёд» (Kuznetsov «наперёд»: «Нар.-разг.»); «прогнозирование» names the process, while the companion
«оценка» keeps the result; 主婦:17 could say «не занималась оплачиваемой работой» instead of «не работала вне дома».

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; scoped coverage (link, manifest and intake integration) **CLEAN**; quiz safety
**CLEAN**. No findings.

- Front matter (word, reading, type, kanji, jlpt, tags) is identical to EN for all 30 cards, and every RU exclusion list
  is a superset of EN's.
- Body links equal EN except the six RU-only links, each introduced or compared substantively, with existing targets.
  EN-only links stay plain text because the RU targets do not exist: 交際→デート, 世間→世の中, 予算→kanji 算 and
  予測→kanji 測.
- All 18 navigation files are prose-identical to their parents once the links are stripped; path forms are correct, and
  link counts for every batch word match EN across all existing RU files. The held 以来→今後 link is the only change to
  that card.
- The manifest's changed and new hashes match, and the intake's 48 paths equal the content diff.
- No exact title-segment duplicate exists among the answer titles beyond 中学 against 中学校, which EN guards.
- It classified every RU-added exclusion (see below) and found no unjustified guard and no missing required guard.

Optional (weak; none established as a defect): 主に–たいてい, 以前–昔, 主要–中心, 世間–人 and 今後–未来.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (代表, 人込み and 世間; the other 27 cards are clean in this facet); scoped
coverage **NEEDS FIX** for 人込み only, **CLEAN** for the other 29 cards.

- F1 (moderate; high confidence), `代表.md:4,12,16`: the title and opening gloss «представительство» ordinarily name a
  representative office (Ozhegov: «учреждение, представляющее чьи-н. интересы») or legal acting for another, and
  `代わり.md:37-38` already uses «представительство» for 代理. JMdict 1412170 sense 1 is a representative or delegate and
  sense 2 is being typical of a category, not an office. A learner can memorise 代表 as a mission or as 代理. Remedy: the
  title «представитель; образец категории» and an opening sentence that excludes an office and acting for another.
- F2 (minor; high confidence), `人込み.md:4,12,29`: the title «толчея» is colloquial and dictionary-equated with «давка»,
  the gloss `混雑.md:20` uses for 混雑 («давка; скопление людей»); JMdict 1367680 sense 1 is only "crowd of people". The
  card never names 混雑 or 大勢, so the dense-crowd, congestion and many-people distinction is not shown. Remedy: the
  title «толпа» and a paragraph contrasting 大勢 and 混雑.
- F3 (minor; high confidence on the dictionary mismatch, medium that a careful reader is misled), `世間.md:4,12,16,18`:
  the lead gloss «общественность» is in the dictionaries the active part of society or public organisations
  (Kuznetsov; Efremova sense 2; Ushakov sense 2), not people in general, and line 18 renders 世間の注目 as «внимание
  общественности». 社会's card already glosses 世間 as «окружающие люди, общественная среда». Remedy: the title
  «окружающие люди; люди вообще», a note against substituting «общественность», and line 18 «Эта новость привлекла
  внимание людей.»

Optional: 代理 «заместитель» can be read as a permanent deputy post (line 33 already says the person need not keep the
place); 今にも:33 could tie the unshown gloss «в любую минуту» to «того и гляди». Checked and not findings: «смета»,
«того и гляди», «фактически», the dropped English-only notes and 人工's «искусственный» qualifier.

## Exclusion classification

All 20 EN exclusion entries (15 lists) are retained. At the candidate, 35 direct, one-sided entries were added on 17 new
cards:

| Entries | Author | Consistency reviewer |
|---|---|---|
| 以前→先, 今にも→もうすぐ | required | required |
| 以前→過去, 代表→典型, 代理→代わり, 付き合い→関係, 付き合い→仲, 人生→生命, 今回→度, 今回→場合, 人込み→混雑, 主張→見解, 主に→大半, 主に→大部分, 事務→仕事 | conservative | required |
| 以前→元, 以前→まず, 今後→将来, 今後→先, 今にも→今に, 人生→生, 人生→生活, 交際→関係, 交際→恋, 交際→仲, 交際→連絡, 予測→予期, 予測→読み, 予測→天気予報, 主要→要点, 主義→思想, 主張→要求, 主に→主要, 中止→止める, 中止→止む | conservative | conservative |

The reviewer also listed four EN entries (予報→予測, 予報→予想, 予報→天気予報 and 乗せる→置く) as conservative. The
author and reviewer differ only in how much necessity they established, not in whether an entry belongs; the records
adopt the reviewer's classification. The correctness reviewer checked the guard comparison words in JMdict without
auditing quiz safety, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`219-words-batch-58-recheck-001.md`.
