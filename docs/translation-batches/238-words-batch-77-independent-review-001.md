# Batch 238 — independent review 001

## Snapshot and scope

- Reviewed commit: `4f48fb310543d50e79bee85665e6e5bc31aa1c48` (tree `70cbbc2f8a5c3164eb0d8bf2d73bb96796a40cc6`), branch
  `full-ru-238-words-77`, parent `fd677f7`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 237 candidate `be448e7c8309d0b9fe6296bd3bc75b2508312556`.
    Before copying, the coordinator's candidate script checked two things: that the three navigation files edited there
    (`kanji/個.md`, `words/書く.md` and `words/責める.md`) were unchanged between `be448e7` and the candidate's parent
    `fd677f7`, and that none of the 30 new cards existed in the primary checkout. It also checked that the branch, HEAD
    and `origin/main` were the expected ones and that the tree was clean.
  - The script byte-compared the 33 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 33 batch paths plus `manifest.json`. Its byte scan of all
    33 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 33 committed
    blobs at `4f48fb3` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from Batch 237; all three restored links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made one content edit, to `words/看板.md`; the
    other 32 lane files were copied unchanged. Its adjudication record states:
    - "Screens rerun by the coordinator with RU_ROOT = lane: `validate.py` 0 errors; `navonly.py HEAD --only kanji/個.md
      words/書く.md words/責める.md` reports 3 files, 3 links added, 0 problems; the lane's changed-path set is exactly
      the 33 paths (30 new cards + 3 restoration files) plus manifest.json (5,259 entries).";
    - "`link_parity.py` over the 33 paths: "checked 33", no LOST or unexplained EXTRA links (`b238-lane-parity.txt`).";
    - "`word_title_screen.py` over the 30 words (`b238-lane-screen.txt`): no unguarded exact-segment overlap.";
    - edit 1, `words/看板.md` (title, H1 and exclusions): «вывеска; доброе имя, гордость (заведения, фирмы)» →
      «вывеска; репутация (заведения, фирмы)». EN has "signboard; shop's reputation" and JMdict 1213990 sense 3;
      «доброе имя» contradicted the card's closing line «Ни одно из этих значений не гарантирует, что у заведения
      хорошая репутация», and the body nowhere supports «гордость». The RU-added 誇り exclusion was removed, putting the
      list back at EN parity; «репутация» ~ 評判 is guarded by the EN pair, and the other leads are qualifier-only stems
      (заведения/фирмы ~ サービス, 支店, 酒場). The record notes a rescreen (`b238-kanban-screen.txt`), a rebuilt manifest
      and `validate.py` 0 errors after the edit;
    - stem-only and different-sense leads decided without a guard: 見学 ~ 伺う/通う/お見舞い «посещ» (the purposes
      differ; 訪問 and 訪ねる are guarded by EN pairs); 看板 ~ 自慢 (moot after the title fix); 改める ~ 改正 (guarded
      by the EN pair on 改正); 見直す ~ 改める/改正/調べる (EN pairs); 複数 (no shared segment; EN declares no
      exclusions); 索引 «предметный указатель (в книге)» ~ 見出し «указатель» (guarded by the EN pair on 見出し);
      書き取り ~ 写す «переписыв» (guarded); and 西暦 ~ 西洋, 襖 ~ 雨戸, 見かけ ~ 見える/違う, 要領 ~ 技術/説明,
      要旨 ~ 考え/論文, 見出し ~ 記事/単語/言葉 and 見舞う ~ 診る (different senses; the author's declines accepted);
    - "Titles compared with EN one by one (`b238_titles.py`); one coordinator title edit (看板, above). Every EN
      `quiz_exclusions` entry is retained in EN order; metadata other than title/exclusions matches EN for all 30
      cards.";
    - "RU-added exclusions after edit 1: 4 pairs, all required for exact segments: 改める→調べる («проверять»),
      見出し→サイン and 見出し→署名 («подпись»), 要旨→実 («суть»).";
    - "Author deviations accepted: 見慣れる avoids «примелькаться»; 索引 drops «индекс». Eight English-dependent remarks
      dropped or adapted (ぶつける, なぐる, 実例, 見下ろす, 索引, あらすじ, 襖, 西暦). 見本 keeps EN's
      metadata-convention sentence («В метаданных по принятому в проекте правилу такие слова отмечены как исконные»),
      checked against EN.";
    - unverified Russian usage handed to the reviewers: 看板's adapted サイン remark («не переводите им вывеску»), which
      replaces an English-"sign" comment, and 見出し «подпись (к фото)» for the caption sense (JMdict sense 1 lists
      caption);
    - a dependency on Batch 237: 見舞う excludes and links 慰める, and 見学 excludes 観測, so the coordinator was to confirm
      that those titles still matched and to rerun the screen on the published Batch 237 tree. The candidate screen ran
      on that tree, and the titles are identical at `be448e7`, `fd677f7` and `f664ac5`: 慰める «утешать (в горе,
      неудаче); успокаивать (душу, сердце)» and 観測 «наблюдения и измерения (погоды, небесных тел); прогнозная оценка
      (развития событий)»;
    - "Missing kanji (plain text, no link): 改 攻 旨 暦 板 概 標 看 索 複 襖 覧 造 領. Unavailable words left plain:
      ぶつかる, 改めて, 能率, 生年月日, 単数."

    The committed manifest records 5,259 entries (5,254 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The consistency
    reviewer also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 3 files with 3 restored navigation links (the kanji card 個 and the word cards 書く and 責める);
    - `manifest.json` (`contentVersion` `b74b9d64eb49d4e7`, 5,259 entries);
    - the intake, whose note reads "B238 30-card adaptation with three navigation-only link restorations in three
      existing files; candidate before blind review."
- Published baseline recorded in the intake: `a0af1d45b7f0152bfb00b849a6559b94f4870019` (Batch 237 merge, PR #121).
  Parent `fd677f7` adds only the Batch 237 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 3 files (3 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b238-cand-screen.txt`): no unguarded exact title-segment overlap (62 `OK` lines for pairs already
    guarded by an exclusion and 588 stem-only `!!` lines). The exact shared segments are all guarded: ぶつける–打つ
    «ударять», 見舞う–訪ねる «навещать», 改める–直す «исправлять», 改める–確かめる and 改める–調べる «проверять»,
    改める–見直す «пересматривать», 見本–型 «образец», 見出し–サイン and 見出し–署名 «подпись», 見出し–題名 «заголовок»,
    看板–評判 «репутация», おおよそ–およそ, くらい and 程度 «примерно», おおよそ–大体 «в целом», and 要旨–内容 and
    要旨–実 «суть»;
  - link parity: no EN link lost where the RU target exists and no RU-only link at the candidate.
- Common sample: all three reviewers read all 30 new word cards in full. The correctness and comprehensibility reviewers
  read each card against its complete frozen EN original. The consistency reviewer read the EN originals of nine cards
  (two of them partly) and compared the others mechanically, read the three navigation-file diffs, and checked the intake
  path list and the manifest.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file); checked all relative links against the primary
    RU tree and the linked baseline titles and meaning paragraphs, reading サイン and 慰める in full ("The
    sympathetic-visiting description of 慰める matches its current card.").
  - Inspected all 30 full JMdict entries in the live publisher archive (www.edrdg.org), including IDs, sense numbering,
    word class and rare/search-only spelling annotations; an initial ftp-host certificate failure and Jisho rate limits
    were overcome through that hostname. It also inspected the relevant named Daijisen and Kotobank definitions, among
    them Digital Daijisen 改める sense 3 and the ふすま heading.
  - Russian sources: Kuznetsov on gramota.ru (видимость senses 1–2, подпись sense 3, особь, сноровка, муляж, сорвать
    sense 7 and швырять sense 1), Wiktionary (пробник sense 1) and readmejapan for the established Russian «фусума»;
    scoped meaning checks, not frequency claims.
  - Checked that every Japanese example and kana payload matches EN and that all 30 N2 labels have frozen EN source-index
    rows.
  - "No generators, repository edits, staging, commits or pushes performed."
- Consistency review scope:
  - Read all 30 RU cards and the three navigation diffs in full; read the EN originals of 見出し, 個体, 見学, 看板, あらすじ,
    御覧, 西暦 and, partly, 見下ろす and 見舞う in prose, and compared the front matter, kanji, tags, type, jlpt, reading,
    exclusion lists and order, link sets, footer URLs and section counts of all 30 with EN mechanically; checked every EN
    link in every EN file that targets one of the 30 words against its RU counterpart; ran the validator (0 errors).
  - Compared `manifest.json` with an in-memory `build_manifest()` result (no write): equal. The validator run left an
    untracked `tools/__pycache__/`, which the reviewer removed; the status was clean afterwards.
  - Checked that the intake's 33 payload paths equal the 33 content paths of the diff and that every
    `candidateRawSha256` matches the committed file.
  - Screened every batch title against all 3,793 RU word titles with its own scripts (exact segment, whole word, stem and
    keyword neighbourhood), not the coordinator's tool or output. Dictionary senses were cited from the cards' entry
    numbers and its own knowledge, not re-fetched.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN and the titles of peer cards used for collision checks; read the three
    navigation diffs as diffs only ("link text only"), outside its verdicts.
  - Ran `link_parity.py` on the 30 paths ("checked 30", no dropped-link hits) and used `word_title_screen.py` only as a
    lead. Dictionary checks used Jisho API renderings of JMdict and the entry IDs printed on the cards; "JMdictDB login
    page was not used". It records no validator or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; the correctness report says "Model identity not independently verifiable",   the consistency report "I cannot
    name my model.", and the comprehensibility report "Model: not
  verifiable from this runtime".
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. The correctness
  report records HEAD matching `4f48fb3` with an empty `git status --porcelain`; the consistency report records
  `4f48fb3` with an empty status at the start and a clean status after removing the bytecode cache the validator had
  created; the comprehensibility report records an empty `git status --porcelain` at the start and at report time, with
  parent `fd677f7`. No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No reviewer reported running a generator script: the correctness report says "No generators,
  repository edits, staging, commits or pushes performed."; the consistency report says "No generator was run that writes
  files" and records the validator run and the in-memory manifest comparison, which called `build_manifest()` without
  writing a file; the comprehensibility report records only the read-only `link_parity.py` and `word_title_screen.py`
  runs. No tracked repository file was changed.
- Full blind reports:
  - `238-words-batch-77-review-correctness-001.md`
  - `238-words-batch-77-review-consistency-001.md`
  - `238-words-batch-77-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the `-b198` and `-b216` scratch worktrees;
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  As in Batch 236, the consistency brief made one exception: the intake record, for its path check. The consistency
  report records that check and that it did not use the coordinator's screen tool or output. The correctness and
  comprehensibility reports make no statement about unread materials beyond their stated scope; the comprehensibility
  reviewer ran `word_title_screen.py` itself as a lead rather than reading the coordinator's output.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** (F1 and F2); scoped coverage **NEEDS FIX** (F2); Russian comprehensibility
**UNVERIFIED** (not an assigned facet). "No other actionable defect established in the assigned 30 articles."

- F1 (P2, medium; high confidence), `見かけ.md:4` (also :12): the independent title segment «видимость» supplies the
  ordinary visibility/seeing-distance sense, which 見かけ does not have, and its secondary Russian sense suggests deceptive
  appearance; the qualifier after «внешний облик» does not qualify the first answer segment. Evidence: JMdict 1604420
  senses 1–2 ("outward appearance"; attributive "apparent"); Kuznetsov «видимость» senses 1–2. Remedy: «внешний вид;
  внешний облик (в отличие от сути)», or simply «внешний облик (в отличие от сути)».
- F2 (P3, low; high confidence), `改める.md:44`: «Другие, более книжные употребления» turns EN's "further
  formal/proper-action uses" into an unsupported register statement and never says what those uses mean. Evidence: frozen
  EN `words/改める.md:44`; JMdict 1200750 sense 4 "to do properly; to do formally", with no bookish tag; Digital Daijisen
  改める sense 3 服装や態度をきちんとする. Remedy: «Словарь отмечает и значение „делать как положено, соблюдать
  формальности“, помимо приведённых здесь примеров.», citing JMdict sense 4.

What the reviewer confirmed:
- All 30 full JMdict entries support the cards' readings and taught senses; every Japanese example and kana payload
  matches EN, with ASCII reading parentheses consistently made full-width.
- All original front-matter facts and guards are retained; added guards occur only in 改める, 見出し and 要旨. All 30 N2
  labels have frozen EN source-index rows.
- No broken or wrongly dropped existing-target link; removed EN links have no RU target.
- Omitting the English-only "nail on", "illustration/drawing" and "argument/quarrel" contrasts is not a coverage defect,
  since RU never offers those English glosses and keeps their Japanese teaching points.
- Kuznetsov supports «подпись» (sense 3) for a caption, «особь», «сноровка», «муляж» and «сорвать» (sense 7); Wiktionary
  supports «пробник»; the Russian «фусума» was checked against its Daijisen ふすま heading.

Optional: 見下ろす.md:39–40 could state the Japanese distinction directly instead of keeping the room/error juxtaposition
from English "overlook" (suggested «見下ろす описывает взгляд сверху вниз, а не случайный пропуск ошибки.»); in
ぶつける.md:4/:21, «бросать»/«Я бросил мяч в стену» would be more neutral than «швырять»/«швырнул», "not a separate
established correctness defect" (JMdict 2742080:2 "fling; hurl"; Kuznetsov «швырять» sense 1). Limits: a content review,
not native-speaker, corpus-frequency, app, quiz-pool or learning-effectiveness validation; the JMdict entries are current
dictionary evidence, not a frozen capture; no finding rests on default masculine past forms, supplied pronouns or natural
active renderings of Japanese passives.

### Consistency and quiz safety

Verdicts: consistency **NEEDS FIX** (C1, low); quiz safety **NEEDS FIX** (Q1, Q2); cross-file integration **CLEAN**.

- Q1 (medium; medium-high confidence), `あらすじ.md:8` (no `quiz_exclusions` line; insert after `tags:`): あらすじ
  «краткое содержание (фильма, книги, плана); краткий пересказ» contains the whole of 内容's first segment «содержание»
  (内容 «содержание; суть»), and neither side declares the pair; 要旨 and 要領 already guard 内容. Remedy:
  `quiz_exclusions: [内容]`. Classification: "RU-introduced, required (title-induced exact-word overlap)".
- Q2 (low-medium; medium confidence), `要領.md:9`: 要領 «суть дела (в объяснении); …» and 実 «плод; суть» share «суть»
  and are unguarded, while 要旨→実 is guarded for the same word. Remedy: append 実.
- Q3 (low; medium-low confidence), `見出し.md:4,12`: the title segment «подпись (к фото)» (EN title "heading; headline;
  index") is narrower than the body, never exemplified, readable as "signature", and the only reason for the guards
  見出し→サイン/署名. Remedy (optional): title and H1 «заголовок (статьи, раздела); заглавное слово (словарной статьи);
  указатель», and body «подпись» → «подпись-заголовок (например, к фото)»; "if the title stays, keep the two guards".
- C1 (low; medium confidence), `サンプル.md:32–33`: 見本 and 標本 are compared with definitions but left plain although
  both cards exist in this batch, against the RU content-structure rule (`.github/instructions/content-structure.instructions.md:42`);
  "a rule-based, not an EN-parity, finding". Remedy: link both. Weaker cases: 個体.md:36 種 and 集団 and おおよそ.md:35
  正確; 改正.md:21 法律 needs no link.
- T1 (low; medium-low confidence), `個体.md:4` (and the H1): EN "individual organism; specimen" loses "specimen" in
  «особь; отдельный организм», although the body and kanji/個.md:36 use «экземпляр». Remedy (optional): «особь; отдельный
  организм; экземпляр».

The report cites line 9 as the H1 for T1; in the committed card the H1 is on line 12.

What the reviewer confirmed:
- Each navigation diff only wraps existing plain text, with EN's path forms and EN-position parity (個 line 36, 書く line
  22, 責める line 35); the glosses beside the new links are not misleading, and no other plain mention of the three
  targets that EN links remains.
- All EN guards are present on all 30 cards in EN order, with RU additions appended; 看板's list equals EN's (15 entries).
  索引, あらすじ and 複数 have no list in EN or RU. The whole-segment overlaps ぶつける–打つ, 見舞う–訪ねる, 改める–直す,
  改める–確かめる, 見直す–改める, 見本–型, 見出し–題名, 看板–評判, おおよそ–およそ/くらい/程度/大体 and 要旨–内容 are
  guarded; its own screen found no further unguarded exact-segment overlap except Q1 and Q2.
- It agreed with the declined pairs listed in its brief, including the unguarded in-batch pairs.
- The dependent Batch 237 pairs fit: 見舞う→慰める and its body fit 慰める «утешать (в горе, неудаче); успокаивать (душу,
  сердце)», and 見学→観測 fits 観測 «наблюдения и измерения (погоды, небесных тел); прогнозная оценка (развития событий)».
- Front matter other than the title and RU-added exclusions equals EN on all 30 cards; every relative link resolves;
  footers name the same dictionaries as EN; section order equals EN; the plain-text pointers to absent targets read
  naturally; the manifest equals the in-memory rebuild; the intake paths and hashes match.

Optional: 見下ろす.md:39–41 calques EN's "overlook" ambiguity; 見学.md:4's title is weighted towards the secondary
«присутствие без участия» sense (suggested «ознакомительное посещение (завода, музея); наблюдение со стороны»). It also
listed seven optional conservative pairs: 個体–身体, 要領–技術, 要旨–圧縮, 見学–出席, 標本–代表, サンプル–型 and
あらすじ–筋. Limits: no live dictionary consultation; 17 EN cards compared mechanically, not read in prose; its own
screen scripts, so near-synonyms without a shared Russian word could be missed; pre-existing differences from EN in
published files were not assessed.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (改める, 見慣れる, 御覧, あらすじ, 見かけ, 見本, 見下ろす, 複数 and 見学; no
actionable defect in the other 21 cards); scoped coverage **CLEAN** for all 30.

- C238-1 (medium; high confidence), `改める.md:16`: «Я хочу избавиться от вредных привычек.» states removal, not the
  reform sense of the title and EN "correct my bad habits". Remedy: «Я хочу исправить вредные привычки.»
- C238-2 (medium; high confidence), `見慣れる.md:16`: «Это привычный, хорошо знакомый пейзаж.» adds knowing, which the card
  contrasts with 知る and 親しい. Remedy: «Это привычный на вид пейзаж.»
- C238-3 (medium; high confidence), `御覧.md:4` (also :11): the title does not cover the usually-kana "look" sense taught
  by «Смотри, радуга!», and its honorific qualifier fights the familiar ～てごらん nuance. Remedy: «посмотри (уважительно
  или по-простому); попробуй (сделать)».
- C238-4 (medium; high confidence), `あらすじ.md:16`: «Перескажите, пожалуйста, вкратце содержание этого романа.» is a
  retelling command, and «содержание» is 内容's title word. Remedy: «Расскажите, пожалуйста, кратко сюжет этого романа.»
- C238-5 (medium; high confidence), `見かけ.md:4`: the unqualified first gloss «видимость» first means visibility.
  Remedy: «внешний облик (в отличие от сути); кажущийся вид».
- C238-6 (low; high confidence), `見本.md:26`: the metadata/project-rule sentence is author-facing. Remedy: delete it.
- C238-7 (low; high confidence), `見下ろす.md:37`: «не обычный глагол для того, чтобы случайно не заметить ошибку»
  rejects a meaning that only English "overlook" suggests. Remedy: drop that clause and keep the contempt sentence.
- C238-8 (low; high confidence), `複数.md:39`: «как в английском» makes the warning depend on English morphology. Remedy:
  end the sentence at «окончания множественного числа».
- C238-9 (low; medium confidence), `見学.md:25`: bare «для N2» is an unexplained abbreviation in learner prose. Remedy:
  «и на этом уровне это не отдельное задание».

Its line numbers point at the paragraph rather than the example or passage line; the dispositions located the passages
by content (改める:21, 見慣れる:19, あらすじ:19, 見本:27, 見下ろす:39–41).

Optional: 見舞う.md:28's active «На город обрушился сильный дождь» is natural; 見かけ.md:17 «чем кажется» is ordinary;
サンプル.md:27's Latin "sample" matches accepted gairaigo wording; ぶつける.md:18 «швырнул» is a little stronger than EN
"threw against"; 書き取り.md:18 matches EN. It noted that the dropped "nail on", "illustration" and "argument" remarks
have no Russian polysemy to teach, that the rebuilt remarks in なぐる, 索引, 看板, 襖 and 西暦 are understandable without
English, and that «фусума» is glossed like «сёдзи». Outside its facets: 索引.md has no quiz_exclusions while 見出し's
title includes «указатель», and the real title-screen overlaps are already guarded. Limits: Jisho API renderings of
JMdict rather than JMdictDB; peer cards not read in full; no claim about quiz runtime behaviour.

## Exclusion classification

All 229 EN exclusion entries (27 lists) are retained in EN order; 索引, あらすじ and 複数 have none in EN. Thirty-three of
them lie inside the batch, and the other 196 target existing RU cards. At the candidate, four direct, one-sided entries
were added on three new cards, all appended at the end of their lists; none targets a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 改める→調べる (1) | Required (exact segment «проверять») | Required |
| 見出し→サイン, 見出し→署名 (2) | Required (exact segment «подпись») | Conservative while the title keeps «подпись (к фото)»; see Q3 |
| 要旨→実 (1) | Required (exact segment «суть») | Conservative; "keep it if Q2 is applied" |

The authoring lane had also added 看板→誇り, which the coordinator removed with the 看板 retitle before the candidate.
The consistency reviewer found "No over-guard of an antonym/contrast", raised the missing guards Q1 and Q2 above and
listed seven optional conservative pairs. The correctness reviewer checked the RU-added exclusions only as additive
metadata, and the comprehensibility reviewer treated 索引's lack of exclusions as a quiz matter outside its facets.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`238-words-batch-77-recheck-001.md`.
