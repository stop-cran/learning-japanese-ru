# Batch 246 — independent review 001

## Snapshot and scope

- Reviewed commit: `008ef28b7b8bb7986f863bea017c0e0e8165a058` (tree `75d0f14a1b55fc23d71f03565846f577eae947fd`), branch
  `full-ru-246-words-85`, parent `f6422c4`. The candidate was signed and pushed before review.
  - The content was authored in the scratch lane `learning-japanese-ru-b246`, whose commit `b37a987` sits on `282ea33`
    ("B245 lane drafts on B242-B244 scratch"). The coordinator's candidate script checked that the lane was clean at
    `b37a987` with parent `282ea33`, that the branch, HEAD~1 and `origin/main` were the expected published baseline, that
    the primary tree, including ignored files, was clean, that the nine navigation files edited in the lane were unchanged
    between `282ea33` and the published HEAD, and that none of the 30 new word files already existed.
  - The script copied 39 lane files (the 30 new cards and the navigation files `kanji/包.md`, `kanji/印.md`,
    `kanji/巻.md`, `kanji/短.md`, `words/撒く.md`, `words/矛.md`, `words/蒔く.md`, `words/転がす.md` and
    `words/長所.md`), regenerated the manifest, checked that the changed path set was exactly the 39 batch paths plus
    `manifest.json`, and byte-compared the copies with the lane. No link was held from an earlier batch. Its byte scan of
    the content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 39 committed
    blobs at `008ef28` (and again at the final fix `c1767c6`) were checked: none has a BOM or CR, and every file ends
    with a newline, as `.gitattributes` requires.
  - After authoring and before the candidate commit, the coordinator edited fourteen lane cards: paragraph breaks in
    twelve, one appended citation line in 碗 and one sentence each in 包装 and 対立; the other 16 new cards and the nine
    navigation files were copied unchanged. Its adjudication record (lane `learning-japanese-ru-b246`, base `282ea33`,
    uncommitted) states:
    - "Scope: all 30 new cards read in full against frozen EN 6af98cb (Russian prose, examples, title/H1, links);
      non-title metadata compared mechanically with EN (b246_cmp.py: all match except one RU-added exclusion 破く→破る,
      required: EN gives both cards the identical title "tear; rip", which the app deduplicates, while the distinct RU
      titles «порвать; разорвать» / «рвать; разрывать» are aspect partners a learner could not reject). Link audit:
      three RU-only links 湯飲み:34→ちゃわん, 短所:37→長所 and 知り合い:34→知人, each at a substantive comparison in the
      body (B214 precedent; RU content-structure rule permits links at substantive comparisons) — accepted, flagged for
      consistency review. Eight EN targets not yet published stay plain (kanji 湯 片 装 編 矛; words 名所 対照 潰す). Nav
      edits: 9 files / 21 links (kanji 包 印 巻 短; words 撒く 矛 蒔く 転がす 長所).";
    - the edits, each with its recorded reason:
      - 巻く, 椀, 碗, 崩れる, 崩す, 砕く, 砕ける, 潰れる, 破く, 破れる, 矢印 and 矛盾: "restored 21 blank-line paragraph
        breaks (2+1+1+2+2+2+2+1+1+3+3+1)" ("the drafts merged EN paragraphs; the published corpus keeps EN paragraph
        structure (3,406 of 3,913 RU cards); paragraph parity now matches EN for all 30");
      - 碗: appended «Счётное слово для порций: [Digital Daijisen через Weblio: 杯](https://www.weblio.jp/content/杯),
        именно заголовок はい как счётного слова.» ("the EN 杯 Weblio citation line was lost in drafting");
      - 包装: «Эти сравнения не делают 包装 каждый свёрток или каждое заполнение ёмкости.» → «Из этих сравнений не
        следует, что любой свёрток или любое заполнение ёмкости — это 包装.» ("ungrammatical calque of EN "do not make
        every parcel … 包装"");
      - 対立: «…— это скорее сравнение со стороны предметов, которые не борются…» → «…может означать взгляд
        наблюдателя, который сравнивает предметы, не борющиеся и не сопротивляющиеся друг другу.» ("EN "an observer's
        comparison of things that are not fighting"; «со стороны предметов» read as the objects doing the comparing");
    - accepted as drafted: "Faithful as drafted: 湯飲み 入れ物 くるむ 容器 碁 破片 千切る 研修 短編 短期 短所 知人 知り合い 目印
      矢印 矛盾 瞳 睨む (plus the edited cards' unchanged prose)."; "破く title «порвать; разорвать» (perfective) against
      破れる «порваться; протереться; сорваться (о переговорах)» keeps the transitive/intransitive contrast; 破く→破る
      exclusion recorded as RU-added."; "潰れる «быть раздавленным» kept, with the RU nuance note that it is an ordinary
      intransitive verb, not the passive of 潰す (RU-specific clarification of a passive-looking Russian gloss)."; "知人
      and 知り合い share the identical title «знакомый», as in EN; the app's exact-title deduplication protects the pair,
      so no exclusion is added (EN has none).";
    - "Dropped English-only notes accepted: 入れ物 English "case", 碁 English verb "go", 瞳 English "pupil" = student.";
    - "Unverified Russian register (not defects): «вместилище» (入れ物) as bookish; «минус» (短所) as colloquial.";
    - "Draft-dependent exclusions point at unpublished drafts and must land after them: 崩れる/砕ける→下降 (B243),
      目印→気配 (B244), 目印/矢印→標識/符号 (B245). 研修→稽古 targets the published B241 card." All of these targets
      exist at the published baseline;
    - "Validation after edits (lane, scratch b37a987): manifest 5,499 files; validate 0 errors; 124 tests OK; budget OK;
      link parity: only the three RU-only links above (plus two pre-existing kanji/短 extras already in HEAD); navonly 9
      files / 21 links / 0 problems; diff --check clean; no BOM/CR/missing EOL; paragraph parity with EN for all 30."

    Fix 1 later changed two of these cards (see the recheck record): 破く's title, H1 and line 16 (the accepted 破く
    title above is the candidate title, which fix 1 replaced; the restored paragraph breaks are intact), and 破片's title,
    H1 and lines 16–17, which the coordinator had accepted as drafted. The 碗 citation line and the 包装 and 対立
    sentences above stand as edited.

    The committed manifest records 5,499 entries (5,494 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The
    correctness and consistency reviewers also ran the validator on the candidate (0 errors each).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 9 files with 21 restored navigation links (the kanji cards 包, 印, 巻 and 短 and the word cards 撒く, 矛, 蒔く,
      転がす and 長所);
    - `manifest.json` (`contentVersion` `cc9db27bbbea5cc7`, 5,499 entries);
    - the intake, whose note reads "B246 30-card adaptation with 21 navigation-only link restorations in nine existing
      files; candidate before blind review."

    Against the published baseline the candidate changes 42 files (1,820 insertions, 29 deletions), including the
    parent's publication record; the candidate commit itself changes 41 files (1,740 insertions, 29 deletions).
- Published baseline recorded in the intake: `1608f454b9fb2e4bd67726867c1ce268b7280c5b` (Batch 245 merge, PR #129).
  Parent `f6422c4` adds only the Batch 245 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 9 files (21 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b246-cand-screen.txt`, 223 lines): 36 `OK` lines for pairs already guarded by an exclusion and 187
    `!!` lines. Its exact-segment lines are 椀~ボール «миска», 椀~碗 «миска» and «счётное слово для порций в мисках» and
    碗~ボール «миска», all `OK`, and the unguarded `!!` line 知り合い~知人 «знакомый»; the other lines are stem-only. It
    differs from the lane screen (`b246-screen.txt`, 224 lines) in three stem-only lines: the 短編~編集 line appears in both
    with different 編集 titles (the published title after the Batch 243 fix `6aa1bca` adds «составление сборника» to the
    lane's pre-publication copy), and the lane-only 短所~符号 line (stem «минус») disappears because Batch 245's fix 1
    changed 符号's title to «условное обозначение; код; знак числа». No exact-segment line differs;
  - link parity: no LOST link, and EXTRA only the three RU-only links named in the adjudication plus the kanji/短 links to
    kanji/知 and words/短い, which already exist at the published baseline. For this record link parity was verified
    again at `c1767c6` with the same result; fix 1 changed no link target.
- Common sample: all three reviewers read all 30 new word cards in full against their complete frozen EN originals. The
  consistency reviewer also read all nine navigation diffs in full and checked the intake record (path list and payload
  hashes) and the manifest entries; the correctness reviewer "reviewed every changed runtime hunk" in the nine
  navigation files and read 転がす completely; the comprehensibility reviewer checked the "batch link edits" in the nine
  files "for learner-facing wording".
- Correctness review scope:
  - "Model identity not independently verifiable."; "Each following RU file AND its frozen EN original was read
    completely, including front matter, every section, example, comparison and footer", followed by the 30 cards.
  - "higher-risk existing comparison cards ちゃわん, ケース, 稽古, 仲間, 長所, 目標, 標識, 陽気 and 入れる were read
    completely."
  - It inspected the official JMdict XML ("not search summaries"); "kanjiapi.dev requests returned HTTP 403", so it
    verified component readings against the official KANJIDIC2 XML; it checked all 30 N2 labels against the policy's
    pinned n2.csv; Digital Daijisen blocks via Weblio; the Russian JMdict entry for 紹介 at JapanDict; Gramota
    (Kuznetsov, Babenko) for «вместилище» and «минус».
  - "Automated comparison verified all 60 Japanese example sentences AND all 60 complete kana readings identical to EN."
  - "Read-only validator: `python -X utf8 -B C:\Users\romanko\repos\learning-japanese-ru\tools\validate.py` completed
    with `0 error(s)`. No generator was run."
- Consistency review scope:
  - "Read in full: all 30 new RU cards; all 9 navigation diffs (`git diff -U0`, 21 link changes: 包 3, 印 4, 巻 2, 短 6,
    撒く 1, 矛 2, 蒔く 1, 転がす 1, 長所 1); the manifest diff (hunks) and the intake JSON (paths and hashes only); the EN
    counterparts for front matter, links, footers and the English-dependent remarks (入れ物, 碁, 瞳, 巻く, 潰れる, 知人,
    睨む, 短所, 対立, 短編, 容器, 矢印) plus structured EN-vs-RU comparison of all 30. Title-screen tool run read-only
    (RU_ROOT). Not run: generators."
  - "`python tools/validate.py` = 0 errors."
  - Its limits record "Model identity not stated. App-side title dedupe unverified. Pre-existing prose glosses in older
    navigation cards were not audited beyond the changed links. Linguistic correctness is another reviewer's facet."
- Comprehensibility review scope:
  - "comprehensibility and scoped coverage, assessed separately. All 30 new cards read in full against the frozen EN
    originals", plus "Comparison titles and cited passages of related RU cards (including `欠点`, `長所`, `破る`, `ケース`,
    `疑う`)". "Model: not verifiable from this session."
  - Its limits record "JMdictDB rejected an unauthenticated fetch; JMdict senses are cited from the Jisho API, Daijisen
    from Weblio, «щепка» from Ozhegov. Related cards were not all read in full." It cites a `word_title_screen.py` result
    for 知人/知り合い and records no validator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `7a8ff5bc-98d4-4126-9342-ec8c08bba2da`,
  `76383fa6-9ebe-4100-833c-714bca4bed39` and `30aafaab-95d5-4635-a558-9d109528d4b5`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model identity
  not independently verifiable.", the consistency report "Model identity not stated." and the comprehensibility report
  "Model: not verifiable from this session."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "Initial and final git status --porcelain empty; final
  worktree and index diffs empty."; the consistency report records "`git status --porcelain` empty"; the
  comprehensibility report records "`git status --porcelain` is not empty: untracked `tools/__pycache__/` only. No other
  uncommitted content." and, in its limits, "`tools/__pycache__/` was not inspected or deleted." Its cause was not
  established; the coordinator removed it before fix 1. No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No generator, checkout, staging or repository edit performed."; the
  consistency report says "Not run: generators."; the comprehensibility report says "No generators were run." No reviewer
  reported changing a tracked repository file.
- Full blind reports:
  - `246-words-batch-85-review-correctness-001.md`
  - `246-words-batch-85-review-consistency-001.md`
  - `246-words-batch-85-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  As in earlier batches, the consistency brief made one exception: the intake record, "check only that its path list
  matches the candidate's content diff and that it adds no learner content". The consistency report records "Intake
  JSON: 39 payload paths exactly equal the diff's kanji/word paths; candidate hashes equal the manifest; no learner
  content." The correctness report states "No other batch report, author output, tracking ledger or prohibited scratch
  checkout read."; the comprehensibility report makes no statement about these sources.

## Initial verdicts and findings

### Correctness

Verdicts: "correctness CLEAN; scoped coverage CLEAN, for all 30 articles and the changed navigation hunks. No per-article
exception. CLEAN means no actionable defect established in these assigned facets, not exhaustive certification of the
corpus or client." Findings: "None in the assigned facets."

- Q1 (outside the assigned facets; "medium learning impact; QUIZ"; confidence high), `words/湯飲み.md:9` and
  `words/ちゃわん.md:9`: "There is no direct 湯飲み–ちゃわん exclusion: both lists currently contain only カップ. “Чайная
  чашка” is a defensible answer for ちゃわん: JMdict 1597530 sense 1 includes “tea cup”, and that RU card explicitly
  teaches its tea-vessel use. Different titles (“чайная чашка” versus “миска для риса”) evade exact-title deduplication;
  the shared カップ exclusion is not transitive." Remedy: "on 湯飲み: `quiz_exclusions: [カップ, ちゃわん]`". "This is not
  a mistranslation or an EN-coverage omission."

What the reviewer confirmed: all 30 principal JMdict entries and cited sense numbers in the XML; component readings in
KANJIDIC2; exact rows for all 30 N2 labels in the pinned n2.csv; "Daijisen 矢印 sense 2 is the
archer's identifying mark, NOT romantic interest; the card correctly attributes the romantic sense to JMdict"; "睨む's
suspicious-watch sense is supported by JMdict sense 4 and Daijisen sense 4; translating the passive with active police
verbs preserves participant roles"; "潰れる's Russian passive-looking gloss is compatible with its explicit Japanese
intransitive explanation"; 知人's «по рекомендации знакомого» is "not a demonstrated mistranslation"; "“Вместилище” is
therefore checked, not assumed incorrect", and Kuznetsov sense 4 "confirms colloquial “недостаток”" for «минус";
"Every EN sense, non-English-specific rule, example and citation remains represented"; "Front matter is unchanged except
translated titles and the added direct 破く–破る exclusion; no EN guard was removed. Exact-equal 知人/知り合い titles are
already deduplicated under the documented client contract."; "Exactly three additional card links occur: 湯飲み→ちゃわん,
短所→長所, 知り合い→知人; their claims fit the target meanings, even when the comparison gloss is not an exact quotation
of the target title."; "Exactly eight EN card links are left plain: kanji 湯/装/片/編/矛 and words 潰す/名所/対照."; "All
navigation additions point to the correct new identity, including 包む（くるむ）→words/くるむ.md."

Optional: "consider defining годан/итидан/окуригана and онное/кунное at first use; trim contributor-oriented
collection/metadata sentences; optionally align 破く/破れる titles with the predominantly imperfective Russian title
style."; "“Минус” could be marked “разг.” if a Russian-register annotation is desired." Limits: "No native-speaker/
proficiency or client-runtime acceptance claimed. Quiz checks were limited to obvious local risks, not a corpus-wide
title-collision audit"; existing comparison cards "not comprehensively re-reviewed as new publications"; "Live
dictionaries are today's entries, not recovered historical captures."

### Consistency and quiz safety

Verdicts: "Coverage / links / navigation: CLEAN"; "Duplicates and conflicts: CLEAN (one optional note, O1)";
"Distractors / quiz_exclusions: CLEAN"; "Tags and metadata: CLEAN"; "Manifest / generated files: CLEAN (strokes
untouched; no kanji card added, so none required)"; "Formatting / footers: CLEAN"; "Unverified: whether the app dedupes
quiz options by title (code not available)." Findings: "No blocking, major or minor defects."

- O1 (optional, low; quiz safety; confidence medium), `words/知人.md:9`, `words/知り合い.md:9`: "both have the title
  «знакомый» and neither excludes the other (EN parity; the repo has many identical-title unguarded pairs, e.g.
  友人/友達, 辞書/辞典). Not a defect. Conservative remedy: append `知り合い` to 知人's `quiz_exclusions` after the EN
  entries."
- O2 (info; navigation): "EN-only links with no RU target stay plain, correctly … RU-only links 湯飲み→ちゃわん, 短所→長所,
  知り合い→知人 all resolve. Nothing to fix."

What the reviewer confirmed: "Front matter matches EN for all 30 (word, reading, jlpt, type, kanji, tags) except the
added 破く guard."; "All EN exclusions are retained in all 30 cards. 碁 needs no extra guard (no 囲碁/将棋 card; ご
homophones are not title-confusable). 椀/碗/ボール are mutually guarded."; "the only unguarded exact title match is
知人/知り合い (O1); the stem-only rows were noise or EN parity"; "Cross-batch links: 目印→標識 …, 研修→稽古 …, 知り合い→仲間
… resolve and fit the glosses."; "Manifest: all 39 kanji/word entries in the diff match the SHA-256 of the committed
files (CRLF-normalised); 5494 manifest files equal 5494 on disk; the diff touches only contentVersion and these
entries."; "English-dependent remarks (碁 "go", 瞳 "pupil", 潰れる "be crushed", 入れ物 "case") are rebuilt for Russian or
dropped naturally; no RU wording defects seen."

### Comprehensibility and scoped coverage

Verdicts: "Comprehensibility: NEEDS FIX (`短所`, `破く`, `破片`, `睨む`; the other 26 new cards have no actionable
comprehensibility defect). Scoped coverage: NEEDS FIX (`短編` only; the other 29 new cards do not lose a
Russian-relevant EN teaching point)."

All five findings are medium severity and high confidence.
- C1 (comprehensibility), `words/短所.md:16` and `:20` (also `:18`, `:23–24`, `:34`; `words/長所.md:31`): "the
  definition and the first example answer with 欠点's quiz title «недостаток; слабая сторона». A learner cannot tell the
  two words apart from the example, and the comparison at line 34 never shows 欠点's actual title. The batch's new link
  on `長所` repeats the same stolen gloss." Remedy: make the body use the title («отрицательная сторона», «минус»), gloss
  欠点 with its own title at line 34, and replace the 長所:31 gloss with «отрицательная сторона; минус».
- C2 (comprehensibility), `words/破く.md:4` and `:16`: "the citation-form title and the opening gloss are perfective
  («порвать; разорвать»), while the paired card `破る` is imperfective «рвать; разрывать» … a learner will treat 破く as
  the completed form of 破る." Remedy: title and H1 «рвать; разрывать (бумагу, ткань)» and the matching line 16.
- C3 (comprehensibility), `words/破片.md:4` and `:16`: "«щепка» is an equal quiz gloss, but in ordinary Russian it is a
  thin piece split along the grain of wood … A learner can leave thinking 破片 means wood chips". Remedy: title
  «осколок; обломок» and a definition naming glass and ceramics.
- C4 (comprehensibility), `words/睨む.md:22`: "«подозревает» is 疑う's quiz word (`сомневаться; подозревать`) rather than
  this sentence's watch sense", and the active translation does not match the passive note. Remedy: «Он у полиции под
  подозрительным наблюдением.»
- C5 (scoped coverage), `words/短編.md:19` and `:22`: "The Russian example drops the shortness (`один рассказ`)", and
  «рассказ, новелла» replaces EN's "explicitly means a short story". Remedy: «Перед сном я прочитал один короткий
  рассказ.» and «короткий рассказ» for 短編小説.

Optional: "nonblocking": 潰れる's title could lead with «сминаться; раздавливаться; разоряться»; a shorter 椀/碗 counter
gloss «счёт мисок»; "`矢印.md:28` "двух знаков в метаданных" and `くるむ.md:31` "не меняет карточку つつむ" are
understandable leftovers of the EN wording and do not teach a wrong meaning"; "`入れ物` «вместилище» and `対立`
«конфронтация» are bookish, but each card also gives a plain gloss and examples"; outside its facets, 知人 and 知り合い
"do not exclude each other … that is a quiz-pair gap, not a reason to invent a register label the dictionaries do not
give." Limits: the dictionary access limits quoted above; "Related cards were not all read in full."; "No generators
were run."

## Exclusion classification

All 212 EN exclusion entries (29 lists; EN has none on 碁) are retained in EN order. 31 of them lie inside the batch,
and the other 181 target existing RU cards. At the candidate, one direct, one-sided entry was added on one new card,
appended at the end of its list; it does not target a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 破く→破る (1) | Accepted as "required: EN gives both cards the identical title "tear; rip", which the app deduplicates, while the distinct RU titles «порвать; разорвать» / «рвать; разрывать» are aspect partners a learner could not reject" | "JMdict 破く (1983750) and 破る both gloss "tear"; the RU titles 破く «порвать; разорвать» and 破る «рвать; разрывать» are an aspect pair, so either is a defensible answer. 破れる already excludes 破る in EN and RU; 破る is an earlier-batch card and cannot declare 破く itself. Classification: required." |

The coordinator added no exclusion for the identical 知人/知り合い titles, relying on the app's exact-title
deduplication; the consistency reviewer raised that pair only as the optional O1 and listed the app behaviour as
unverified. The correctness reviewer confirmed the added 破く–破る exclusion and raised the outside-facet Q1
(湯飲み→ちゃわん), and the comprehensibility reviewer's 破く finding C2 concerned the aspect of the title rather than an
unguarded overlap.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`246-words-batch-85-recheck-001.md`.
