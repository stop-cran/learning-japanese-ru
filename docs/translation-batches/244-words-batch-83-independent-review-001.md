# Batch 244 — independent review 001

## Snapshot and scope

- Reviewed commit: `c21597475cf24f578b35cc6636257450f8a80902` (tree `ba7eb57a671e3585fadb94026d9d505021a0444a`), branch
  `full-ru-244-words-83`, parent `7e2b446`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the commit `556daa95a6abb058dbe62e1af26fe523a834d14b`, which holds
    the Batch 243 lane drafts on `eec3d2d` (the Batch 241 and Batch 242 drafts on the Batch 240 fix `3544d75`); the
    scratch commit is `fe1dfd3db9640d26783ce70b4b997d77436bf10d`. Before copying, the coordinator's candidate script
    checked that the four navigation files edited there were unchanged between `556daa9` and the candidate's parent
    `7e2b446`, and that none of the 30 new cards existed in the primary checkout. It also checked that the branch, HEAD
    and `origin/main` were the expected ones and that the tree, including ignored files, was clean.
  - The script byte-compared the 34 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 34 batch paths plus `manifest.json`. Its byte scan of all
    34 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 34 committed
    blobs at `c215974` (and again at the final fix `85a96a2`) were checked: none has a BOM or CR, and every file ends
    with a newline, as `.gitattributes` requires.
  - No link was held from an earlier batch; all four navigation files were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made ten content edits, to `words/純粋.md`,
    `words/紫.md`, `words/経度.md`, `words/水滴.md`, `words/算数.md`, `words/執筆.md`, `words/作者.md`, `words/そのうえ.md`,
    `words/第一.md` and `words/気配.md`; the other 24 lane files were copied unchanged. Its adjudication record states:
    - "Scope: all 30 new cards read in full against frozen EN 6af98cb (Russian prose, examples, title/H1, links);
      non-title metadata compared mechanically with EN (all match; EN exclusion order kept; three RU-added exclusions
      性質→性能, 書留→速達, 作者→著者 accepted). Link audit: no EN link whose target exists in the lane is missing, and no
      RU-only links. Nav edits 作家:36, 性:35, 性格:32, 重点:29 accepted.";
    - the edits, each with its recorded reason:
      - 純粋: "title/H1 «беспримесный; неподдельный; без примесей» → «чистый; неподдельный; без примесей»" ("«беспримесный»
        duplicated «без примесей» and is rare; «чистый» = EN "pure"; exact-segment hits きれい/清潔/清い are all direct
        exclusions of 純粋");
      - 紫: "«воробейник краснокорневой» → «воробейник (лат. Lithospermum erythrorhizon)»" ("genus name Воробейник =
        Lithospermum verified (ru.wikipedia genus list); the species vernacular was not verifiable");
      - 経度: "«Долгота этой точки — сто сорок градусов восточной долготы.» → «Эта точка находится на ста сорока
        градусах восточной долготы.»" ("avoids repeating «долгота»; matches EN rendering");
      - 水滴: "restored the number note (Japanese noun has no obligatory number ending, unlike Russian; «капля»/«капли»
        from context)" ("EN note dropped though it applies equally to Russian; the two examples use капли/капля");
      - 算数: "«по начальной математике» → «по математике» (example)" ("natural name of the school subject; the title
        keeps the sense distinction");
      - 執筆: "«работа над ним как автора» → «то есть авторская работа над ним»" ("grammar polish");
      - 作者: "examples → «Кто автор этого романа?», «Мы не знаем, кто написал эту картину.»" ("natural translations
        (title remains «создатель произведения»)");
      - そのうえ: "«Притом ещё и ветер усилился.» → «Вдобавок ещё и ветер усилился.»" ("«притом» is unnatural for an
        added event");
      - 第一: "«Первая по счёту причина» → «Первая причина»" ("natural translation");
      - 気配: "«В комнате не чувствуется ничьего присутствия.»; «Я чувствую, что собирается дождь.»" ("natural
        renderings of "no sign of anyone", "sense signs of rain"");
    - accepted as drafted: "純情/純粋 were re-authored after the agent's EN-overwrite incident; both re-read in full against
      EN: faithful."; "素直 «покладистый; искренний» kept: «послушный» would exactly collide with 利口 (guarded, but
      «покладистый» also covers the receptive sense in the first example)."; "おめでたい «радостный (о событии);
      простоватый» kept (простоватый = naive/simple-minded; standard word)."; "系統 «взаимосвязанная система; родословная
      линия», 気配 «смутный признак; намёк; настроение рынка» kept (avoid exact «система»/«признак» collisions; exclusions
      mirror EN).";
    - "素人 jukujikun phrasing matches published 時計; unlinked article mention in 作者 follows published 作家/武士.";
    - "Dropped English-only notes (そのほか "otherwise", 系統 raw-list gloss generalized) are appropriate.";
    - "Kanji links to 純/滴/粒/算/筆 omitted because RU kanji cards are not published yet (restore with kanji).";
    - "Lane copies of B241 cards still carry candidate titles (e.g. 余計); refresh on rebase after B241 publishes.";
    - "Validation after edits (lane): manifest 5,439 files; validate 0 errors; 124 tests OK; budget OK.";
    - "Title screen 純粋: 3 exact «чистый» hits, all guarded; stem hits «приме» (пример) are false positives."

    Two of these edits were changed again by fix 1 (see the recheck record): 純粋's title and H1 now read «чистый (без
    примесей); неподдельный» (comprehensibility C15), and 紫:21 now names «воробейник краснокорневой» without the Latin
    binomial (comprehensibility C12 and the correctness optional; Plantarium item 23077).

    The committed manifest records 5,439 entries (5,434 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The
    correctness and consistency reviewers also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 4 files with 4 restored navigation links (the word cards 作家, 性, 性格 and 重点);
    - `manifest.json` (`contentVersion` `3e1149c3d5d019ad`, 5,439 entries);
    - the intake, whose note reads "B244 30-card adaptation with four navigation-only link restorations in four existing
      files; candidate before blind review."

    Against the published baseline the candidate changes 37 files (1,659 insertions, 9 deletions), including the
    parent's publication record; the candidate commit itself changes 36 files (1,579 insertions, 9 deletions).
- Published baseline recorded in the intake: `0f2c03c681ff90e2fac796417f986ecdf0ee898e` (Batch 243 merge, PR #127).
  Parent `7e2b446` adds only the Batch 243 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 4 files (4 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b244-cand-screen.txt`, 303 lines): 28 `OK` lines for pairs already guarded by an exclusion and 275
    `!!` lines, all stem-only; the only exact-segment lines, 純粋 «чистый» with きれい, 清い and 清潔, are `OK` lines. It
    differs from the lane screen (`b244-screen.txt`, 302 lines) in three stem-only lines: an added 純粋~実力 «приме» line,
    and おめでたい~広々 and そのうえ~余計, where the published titles of 広々 (Batch 242 fix `872649e`) and 余計 (Batch 241
    fix `9cf1600`) differ from the lane's pre-publication copies. No exact-segment line differs;
  - link parity: no LOST and no EXTRA link (the saved lane run over the same 34 paths, `b244-lane-parity.txt`, prints
    only "checked 34"). For this record link parity was verified again at `85a96a2`: no LOST link,
    and EXTRA only for the reviewed RU-only link added by fix 1 (`words/そのうえ.md` → 上).
- Common sample: all three reviewers read all 30 new word cards in full against their complete frozen EN originals. The
  consistency reviewer also read all four navigation diffs in full and checked the intake record (path list and payload
  hashes); the comprehensibility reviewer read the "Commit-only link edits in words/作家.md, words/性.md, words/性格.md,
  words/重点.md … via diff, not as full-card reviews", and the comparison titles needed for quiz collisions.
- Correctness review scope:
  - "Model identity not verifiable. Read in full, file by file, BOTH RU words/<word>.md and its EN original", followed by
    the 30 cards ("30/30 complete pairs"); "also read 緯度, 実力, 性能, 速達 and 著者 fully."
  - Inspected actual JMdict XML entries ("not search snippets"), KANJIDIC2, Digital Daijisen via Weblio ("Checked
    Daijisen sections, not Weblio-generated introductory summaries"), Kotobank, Kanjipedia, Japan Post, Gramota,
    Russian Wiktionary, Plantarium and Ushakov via gufo.me.
  - "Read-only validator: python -X utf8 -B tools/validate.py in primary RU checkout, exit 0, “0 error(s)”. No generators
    run."
- Consistency review scope:
  - "Read all 30 new cards in full. Read all 4 navigation diffs (作家, 性, 性格, 重点) in full. Read the intake JSON and
    the manifest diff. Compared each card to the frozen EN source with scripts: front matter, exclusion prefix, links
    and structure."
  - "`python tools/validate.py`: 0 errors."
  - Its limits record that it "did not run build_manifest.py, link_parity.py or word_title_screen.py", "did not fully
    recompute manifest hashes" (118 `strokes/*.json` disk-hash mismatches, "probably CRLF checkout normalisation"; "A
    committed-blob check timed out, so this is unresolved"), and "did not judge the accuracy of the Russian titles in
    depth."
- Comprehensibility review scope:
  - "comprehensibility (primary) and scoped coverage, assessed separately. All 30 new cards read in full against their
    EN originals", followed by the 30 cards, plus the comparison titles of "青, 青い, 速達, 著者, 兆候, きれい, 清い, 清潔,
    数学, 停留所, 余計, 緯度, 電車, and others named in the risk list".
  - "`word_title_screen.py` and `link_parity.py` run as leads only (link parity: no lost EN link whose RU target
    exists)." Its limits record that "JMdictDB was password-gated; senses are from the public jisho.org JMdict display
    and from the cards’ own cited entry numbers" and that "Title-screen 5-character stems were not treated as verdicts".
    It records no validator or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `72218650-29d7-4ad3-875b-26bbaaaaf7af`,
  `f3294f9e-bb30-4a0f-a0a4-3107c7c7c54a` and `984b518d-553c-4ff3-93d6-05f78b2e55ed`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model identity
  not verifiable.", the comprehensibility report "Model: not verifiable." and "Model name not verifiable.", and the
  consistency report makes no statement about its model.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "Initial and final git status --porcelain empty; final
  HEAD unchanged; cached diff exit 0."; the consistency report records commit `c215974` and a "clean working tree"; the
  comprehensibility report records "uncommitted changes: none (`git status --porcelain` empty; HEAD matches the signed
  candidate)". No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No generators run." and "Only this report was written. No runtime
  files, Git state, generated files, author evidence or batch bookkeeping modified."; the consistency report says "I did
  not run build_manifest.py, link_parity.py or word_title_screen.py, because the instructions forbid generators or
  writing files, or I did not get to them." and "No `__pycache__` was created.";   the comprehensibility report makes
    no statement about file changes. No reviewer reported changing a tracked repository file.
- Full blind reports:
  - `244-words-batch-83-review-correctness-001.md`
  - `244-words-batch-83-review-consistency-001.md`
  - `244-words-batch-83-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  As in earlier batches, the consistency brief made one exception: the intake record, "check only that its path list
  matches the candidate's content diff and that it adds no learner content". The consistency report records "The intake
  path list equals the words diff (34 paths)." and "Every candidateRawSha256 matches the file on disk." The correctness
  report states "Non-runtime batch records, author/reviewer evidence and scratch checkouts were not consulted."; the
  comprehensibility report makes no separate statement.

## Initial verdicts and findings

### Correctness

Verdicts: "correctness UNVERIFIED solely for the Russian “common root” assertion in words/そのうえ.md:48 (see Limits); no
actionable correctness defect established in the other 29 cards. Scoped coverage CLEAN for all 30. CLEAN means no
actionable defect established, not exhaustive proof."

- Findings: "None established." An interim C1 on 絞る:19 was "WITHDRAWN: ます is morphologically polite nonpast, but
  recipe/procedural narration can legitimately translate as a Russian imperative."
- UNVERIFIED claim, `words/そのうえ.md:48`: «связаны общим корнем» "is NOT fully verified as written". Russian Wiktionary
  gives the root -сверх- for «сверх» and с- + -верх- + -у for «сверху» (Tikhonov), and Tikhonov's own entry is
  unsegmented; "These analyses do not establish the stated common modern root, but do not disprove historical
  relationship either. … therefore UNVERIFIED for this assertion rather than an invented definite defect."

What the reviewer confirmed: "No changed main Japanese example or kana-reading string found."; "Front matter matches EN
except three RU-added protective exclusions: 性質→性能, 書留→速達, 作者→著者. Targets exist; additions do not remove EN
metadata or introduce a false teaching rule."; "No broken RU card links or new card links lacking EN counterparts.
Removed EN links all have absent RU targets: 純, 滴, 粒, 算, 筆; 掃く, ブラシ; occupation-and-role-endings."; dictionary
support for «покладистый», «чистосердечие», «зерно», «крахмал», «простоватый», «взаимосвязанный», «пишущий эти строки»
and, through Ushakov's «настроение» sense 3, «настроение рынка»; "Registered-post service … not equated with express
delivery."

Optional: 絞る:19 «В рецепте:» label ("not a mandatory fix"); 紫:21 «воробейник краснокорневой (Lithospermum
erythrorhizon)» as "more precise than the genus name alone"; 性質:47–48's «собственность» warning "has little Russian
lexical motivation", and 素質:49, 素直:34–36, 素人:30, 算盤:32–37 and 系統:41 "expose collection/category/source
machinery; comprehensibility polish, outside these verdicts"; そのうえ:48–49 «В русском «сверх того» выражает добавление,
а «сверху» — положение. Так же различайте связующее и буквальное употребления そのうえ.» Limits: the root claim above;
"Jisho was partly rate-limited and kanjiapi returned 403; actual JMdict/KANJIDIC2 supplied replacement evidence."; "No
APK execution or exhaustive automatic quiz-pool audit".

### Consistency and quiz safety

Verdicts: "Consistency, format, links, navigation: CLEAN."; "Intake JSON and manifest: CLEAN on the checks I ran.";
"Quiz safety: NEEDS FIX. One required finding (F1) and four conservative ones (F2–F5). Three RU-added guards need no
change." The report gives no separate scoped-coverage verdict.

- F1 (required), `words/組み立てる.md:9`: "The RU title «собирать из деталей…» makes bare «собирать» a defensible answer.";
  集める «собирать; коллекционировать» and 拾う «подбирать; собирать» also contain it; "Neither side has a guard." Remedy:
  append `集める, 拾う`; "集まる is optional."
- F2 (conservative), `words/素直.md:9`: "«покладистый» plus the obedience teaching in the body overlaps おとなしい
  «послушный»." Remedy: add おとなしい.
- F3 (conservative), `words/終点.md:9`: "Both titles share «остановка»." Remedy: add 停留所.
- F4 (conservative, low), `words/等分.md:9`: "Both titles share «деление»." Remedy: add 区分.
- F5 (conservative, low), `words/気配.md:9`: "«настроение (рынка)» overlaps 機嫌 «настроение»." Remedy: add 機嫌.

What the reviewer confirmed: "Front matter matches EN apart from title and exclusions."; "Every EN exclusion is kept as
an ordered prefix."; "All links resolve."; "The only links not added are to targets absent from RU: kanji 純/滴/粒/算/筆,
掃く, ブラシ, and the occupation article."; "The four navigation changes are one-line link-only edits at the EN
positions."; "The manifest diff only adds the 30 entries, updates 4 hashes and changes contentVersion."; "No guard
needed: 経度, 紫, 素人, 水滴, 箒, 執筆."

Optional ("EN-inherited, not batch defects"): 算数 tags lack `kango`; 紫 tag `colors`; kana spacing and comparison-line
parentheses in 作者 and 算数; 算数's percent-encoded footer URL; 算数:18 «домашнее задание по математике» "mildly in
tension with the card's own warning"; "筆者 vs 私 and 第一 vs 主要: an optional guard at most."; 素質's learner prose
mentioning «исключения в викторине». Limits: the generator and screen scripts not run; manifest hashes not fully
recomputed (strokes CRLF, unresolved); "Two `scenes/*.json` files (きらきら, にこにこ) are not in the manifest."; "Footer
URLs and sense numbers were not diffed character by character against EN."; Russian title accuracy not judged in depth.

### Comprehensibility and scoped coverage

Verdicts: "Comprehensibility NEEDS FIX (exceptions with no finding: 絞る, 経度, 組み立てる, 終点, おめでたい, 糊, 水滴, 粒,
箒, 等分, 執筆, 筆者, そのほか, 第一, 気配). Scoped coverage CLEAN (no missing prerequisite or EN teaching point required to
answer the article; phrasing defects are under comprehensibility)."

Each finding is rated high confidence; C8, C18 and C19 are low severity and the others medium.
- C1, `性質.md:48`: «Русское «свойство» здесь не связано с «собственностью»» "warns against a confusion that exists only
  for English "property"". Remedy: «Имущество, которым владеют, — это [財産](財産.md), а не 性質.»
- C2, `素人.md:30`: «категория приложения jukujikun» "is Latin-script jargon and points at an app label the learner cannot
  see". Remedy: delete the clause and start at «запоминайте 素人 целиком».
- C3, `算盤.md:32`: «Категория приложения `jukujikun`» "is the same invisible Latin label". Remedy: «Это способ запомнить
  слово целиком, а не утверждение об историческом происхождении слова.»
- C4, `素質.md:49`: «исключения в викторине не делают…» "refers to quiz metadata the reader cannot see". Remedy: «[人物]
  (人物.md) и [カラー](カラー.md) тоже связаны с человеком или свойствами, но не заменяют 素質 в предложении.»
- C5, `素直.md:34`: «Эта коллекция относит смешанное чтение… к группе слов» "refers to the app’s classification". Remedy:
  «Чтение соединяет онное ス с исконным なお. Это смешанное чтение, а не два обычных онных чтения.»
- C6, `素直.md:20`: «охотно прислушивается» "adds willingness". Remedy: «…и он внимательно слушает советы.»
- C7, `系統.md:4`: «родословная линия» "narrows lineage to a family pedigree". Remedy: «система; линия происхождения».
- C8 (low), `系統.md:41`: the study-list sentence "points at study-list material the learner cannot see". Remedy:
  delete it.
- C9, `算数.md:18`: «по математике» "uses the quiz title of 数学". Remedy: «…по арифметике.»
- C10, `作者.md:38`: «Сравнение 作者 с 作家 и окончаний 者 и 家 см.…» "does not parse". Remedy: «Чем 作者 отличается от 作家
  и как различаются окончания 者 и 家, объясняется в статье об окончаниях профессий и ролей.»
- C11, `紺.md:19`: «Эта форма тёмно-синяя» leaves «форма» open to "shape". Remedy: «Эта униформа тёмно-синяя.»
- C12, `紫.md:21`: «воробейник» and «Lithospermum erythrorhizon» are not usable by a beginner. Remedy: describe the dye
  plant and its white flowers without the Latin name.
- C13, `純情.md:19`: «не смейтесь над» renders からかう as laughing. Remedy: «Пожалуйста, не подшучивайте над её
  невинностью.»
- C14, `純粋.md:19`: «из искреннего любопытства» "uses 素直’s title word". Remedy: «Я спросил из неподдельного
  любопытства.»
- C15, `純粋.md:4`: the lead «чистый» is also on きれい and 清潔; "Quiz exclusions guard the pair, so this is not an
  unguarded quiz collision, but the studied answer still starts with the word the article says is the wrong shortcut."
  Remedy: «чистый (без примесей); неподдельный».
- C16, `書留.md:4`: «письменная отметка» "reads as a mark or grade (it also stem-collides with チェック «отметка»)".
  Remedy: «заказное отправление; запись для памяти» and the matching line-21 change.
- C17, `そのうえ.md:4`: "Title word «сверх» is also the lead of 余計"; "The pair is not in quiz_exclusions". Remedy:
  «притом; вдобавок».
- C18 (low), `そのうえ.md:42`: 上 is left plain while 下 is linked. Remedy: «[上](上.md)».
- C19 (low), `筆記.md:4`: «конспектирование» "is narrower than the sense the body teaches". Remedy: «записывание; ведение
  записей».

Optional: 第一:23 «Да и вообще»; 粒 «лежит»; supplied participants in 絞る, おめでたい, 第一 and そのうえ; «электропоезда»
("matches the published 電車 title"); "Dropped English-only warnings in 絞る (press/train), 紺 (navy/deep blue labels), and
そのほか (otherwise) are not losses". "RU-added quiz exclusions 性能, 速達, 著者 are outside these facets." Limits: JMdictDB
password-gated; "Daijisen white-flower wording was not re-opened."; "The four link-only edits were not read as full
articles."

## Exclusion classification

All 174 EN exclusion entries (25 lists; EN has none on 経度, 紫, 素人, 水滴 or 箒) are retained in EN order. Nine of them
lie inside the batch, and the other 165 target existing RU cards. At the candidate, three direct, one-sided entries
were added on three new cards, all appended at the end of their lists; none targets a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 性質→性能 (1) | Accepted | "conservative. The basis is weak (nature vs performance) but harmless." |
| 書留→速達 (1) | Accepted | "conservative, bordering on unjustified. The only basis is the shared noun «отправление». Harmless; keep or drop at the author's discretion." |
| 作者→著者 (1) | Accepted | "justified. The 作者 example translates 作者 as «автор», and the 著者 title is «автор (книги, труда)»." |

The coordinator accepted all three without classifying them ("three RU-added exclusions 性質→性能, 書留→速達, 作者→著者
accepted"); the consistency reviewer headed them "RU-added guards (keep; no action)" and raised five missing guards
(F1 required, F2 to F5 conservative). The correctness reviewer raised no exclusion finding ("additions do not remove EN
metadata or introduce a false teaching rule"), and the comprehensibility reviewer's C15, C16 and C17 concerned titles:
C15's «чистый» overlaps are already guarded, while C16's チェック «отмет» and C17's 余計 «сверх» stems were unguarded.

Reconciliation, the coordinator's dispositions, the four fixes and the final verdicts are in
`244-words-batch-83-recheck-001.md`.
