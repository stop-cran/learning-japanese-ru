# Batch 239 — independent review 001

## Snapshot and scope

- Reviewed commit: `39b6bd13afc5eec5371ce27cd611ce1ff581f19a` (tree `d966f81d76a25657d6aad60cb77733f2f9631bfd`), branch
  `full-ru-239-words-78`, parent `3f56e1a`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 238 candidate `4f48fb310543d50e79bee85665e6e5bc31aa1c48`.
    Before copying, the coordinator's candidate script checked two things: that the nine navigation files edited there
    (`kanji/圧.md`, `kanji/局.md`, `kanji/薬.md`, `words/側.md`, `words/虫.md`, `words/蛇.md`, `words/蛍.md`, `words/蝶.md`
    and `words/被る.md`) were unchanged between `4f48fb3` and the candidate's parent `3f56e1a`, and that none of the 30 new
    cards existed in the primary checkout. It also checked that the branch, HEAD and `origin/main` were the expected ones
    and that the tree was clean.
  - The script byte-compared the 39 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 39 batch paths plus `manifest.json`. Its byte scan of all
    39 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 39 committed
    blobs at `39b6bd1` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from Batch 238; all thirteen restored links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made two content edits, to `words/思い付く.md` and
    `words/栓.md`; the other 37 lane files were copied unchanged. Its adjudication record states:
    - "Screens rerun by the coordinator with RU_ROOT = lane: `validate.py` 0 errors; `navonly.py HEAD --only kanji/圧.md
      kanji/局.md kanji/薬.md words/側.md words/虫.md words/蛇.md words/蛍.md words/蝶.md words/被る.md` reports 9 files,
      13 links added, 0 problems; the lane's changed-path set is exactly the 39 paths (30 new cards + 9 restoration files)
      plus manifest.json (5,289 entries after the coordinator edits).";
    - `link_parity.py` over the 39 paths: "checked 39", no LOST link; the EXTRA (RU-only) links are カバー → 表紙 (EN :35
      makes the same book-cover comparison in plain text), コック → 蛇口 (EN plain-text comparison) and 栓 → 渋滞 (in the
      RU-added traffic-jam sentence), and the pre-existing 局 → 郵便局 and 側 → 近く/隣, identical at the base `4f48fb3`
      (`b239-lane-parity.txt`);
    - `word_title_screen.py` over the 30 words: every exact-segment overlap is guarded;
    - edit 1, `words/思い付く.md:20` (example translation): «Мне не приходит хорошая идея.» → «Хорошая идея в голову не
      приходит.» The old wording lacks «в голову» and is not grammatical Russian; the new one keeps the idea as subject,
      matching the card's が remark (EN "I can't think of a good idea.");
    - edit 2, `words/栓.md:40`: the list of Russian renderings omitted «кран», which the title and example 2 use; it now
      reads «пробка», «затычка», «кран» или «вентиль»;
    - stem-only leads decided without a guard, among them 清書/表紙 «переп», 裂く «части», 衣食住 «одежд» and «жильё»,
      行列 «очере», 蘇る «восст»/«памят», 薬品 «средс» and 薄める «впеча»/«возде»;
    - "Titles compared with EN one by one (`b239_titles.py`): no coordinator title edit. Every EN `quiz_exclusions` entry
      is retained in EN order; RU additions are appended.";
    - RU-added exclusions: 12 pairs on 9 cards — required 行列→番 and 順番 («очередь»), 血液→血 («кровь»), 衣食住→服
      («одежда») and 栓→渋滞 («пробка»); conservative 清書→書き取り, 被せる→履く, 蛇口→水道, 蘇る→浮かぶ, 衣食住→衣服 and
      住宅, and 薬品→農薬;
    - author deviations accepted: 裂く's title without «разлучать»; 栓's RU-added sentence that 栓 is not a traffic «пробка»
      (→ 渋滞); the コック → 蛇口 link; and English-dependent remarks adapted or dropped in 清書 ("fair"), 儀式 («служба»),
      コック (spelling), 薬指 (finger numbering), 薬品 (plural title) and 衣食住 (word order);
    - left to the blind review: 被せる «надевать (на голову другому)», 思い付く's recall qualifier, 蓋 «крышка» alone,
      行事 «мероприятие» alone, 蓋:20's agentive translation and 儀式's «служба» paragraph;
    - unverified Russian usage handed to the reviewers: «служба», «вспарывать», «додумываться», «затычка», «химикаты» and
      «полутёмный»;
    - a dependency on Batch 238: 清書 (RU-added) and 複写 (EN) exclude 書き取り, so the coordinator was to confirm that its
      title still matched. The title «диктант; переписывание (текста, кандзи)» is identical at `4f48fb3`, `52d5c9c` and
      `8cc7216`, and Batch 238's fix `f664ac5` did not change `words/書き取り.md`;
    - missing kanji with EN links (plain text, no link): 清 複 裏 被 衣 角 血 液 缶 蚊 蛇 薄 麦; unavailable words left plain:
      下書き, 着せる, 液体, 気圧, 夜間, うどん.

    The committed manifest records 5,289 entries (5,284 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The correctness
    and consistency reviewers also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 9 files with 13 restored navigation links (the kanji cards 圧, 局 and 薬 and the word cards 側, 虫, 蛇, 蛍, 蝶 and
      被る);
    - `manifest.json` (`contentVersion` `05ed8b9a8d8bc80c`, 5,289 entries);
    - the intake, whose note reads "B239 30-card adaptation with thirteen navigation-only link restorations in nine
      existing files; candidate before blind review."
- Published baseline recorded in the intake: `52d5c9c93d2a9cd6847ce846bae0f1db2a245496` (Batch 238 merge, PR #122).
  Parent `3f56e1a` adds only the Batch 238 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 9 files (13 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b239-cand-screen.txt`): no unguarded exact title-segment overlap (28 `OK` lines for pairs already
    guarded by an exclusion and 115 stem-only `!!` lines). The exact shared segments are all guarded: 被せる–着る
    «надевать», 衣食住–服 «одежда», 行列–列, 番 and 順番 «очередь», 儀式–式 «церемония», 血液–血 «кровь», コック–栓
    «вентиль», 思い付く–思い出す «вспоминать» and 栓–渋滞 «пробка»;
  - link parity: no EN link lost where the RU target exists; the RU-only links at the candidate are カバー:43 → 表紙,
    コック:39 → 蛇口 and 栓:44 → 渋滞, plus the pre-existing 局 → 郵便局 and 側 → 近く/隣 on navigation files.
- Common sample: all three reviewers read all 30 new word cards in full against their complete frozen EN originals. The
  consistency reviewer also read the nine navigation-file diffs in full and checked the intake path list and hashes and
  the manifest; the correctness reviewer checked the candidate's backlink changes, and the comprehensibility reviewer read
  the navigation changes as link-only diffs.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file); also checked the candidate's backlink changes,
    metadata, relative-link parity, selected baseline comparisons and manifest validation.
  - Read the full current JMdict entries for all 30 main words, additional cited entries and relevant comparisons;
    checked component readings in kanjidic2 (www.edrdg.org) after kanjiapi requests failed; Jisho rate limiting "was
    superseded by full JMdict retrieval". It also inspected Digital Daijisen 思い付く (Kotobank) and 置く (Weblio).
  - Russian glosses inspected where consequential: вспарывать, додумываться, химикат, сумрачный, полутёмный, дубликат,
    восполнять, служба and чёрный ход; scoped meaning checks, not frequency claims.
  - Checked that all 64 bulleted Japanese example sentences and their kana readings match EN, and that all 30 N2 labels
    match the pinned community vocabulary CSV (stephenmk/yomitan-jlpt-vocab, `original_data/n2.csv`).
  - "Only this designated report was written; no generators, commits, pushes or checkout changes."
- Consistency review scope:
  - Read all 30 RU cards in full against their EN originals (front matter, body, footer) and all nine navigation diffs in
    full (13 link occurrences); checked EN guard retention programmatically for all 30; ran the validator (0 errors).
  - Checked that the intake's 39 payload paths equal the candidate's content diff (30 new + 9 navigation files), that
    every `candidateRawSha256` matches the working-tree bytes and that the intake adds no learner content.
  - Scanned all RU titles for unguarded overlaps; dictionary senses were cited from general knowledge and the cards'
    entry numbers: "I did not independently verify the JMdict/Daijisen entry numbers or senses against the live
    dictionary".
- Comprehensibility review scope:
  - Read all 30 cards in full in RU and against EN; sampled the titles or contrast sections of 圧力, 角, 機能, サービス,
    勤め, コピー, 書き取り, 血, 暗い, 薄い, 思い出す, 釜, 薬, 出来事 and 沈める; read the nine navigation changes as
    link-only diffs.
  - Ran `link_parity.py` on the 30 cards (no lost EN links; the extra RU links to 表紙, 蛇口 and 渋滞 "point at existing
    cards and are not defects") and used `word_title_screen.py` only as a lead. "JMdictDB itself asked for a password, so
    sense citations are JapanDict renderings of the stated JMdict ids plus the cards' own citations." It records no
    validator or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; the correctness report says "Actual model identity: not independently verifiable.", the consistency report
  "Model: not verifiable from inside the session.", and the comprehensibility report "Model: not verifiable from the
  session prompt."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. The correctness
  report records HEAD matching `39b6bd1` with an empty `git status --porcelain` and empty working-tree and cached diffs;
  the consistency report records `39b6bd1` with an empty status at the start and at the end; the comprehensibility report
  records `git rev-parse HEAD` printing `39b6bd1` and an empty `git status --porcelain`. No fix was applied until all
  three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "no generators, commits, pushes or checkout changes"; the
  comprehensibility report records only the read-only `link_parity.py` and `word_title_screen.py` runs. The consistency
  report records that "one of my commands (`build_manifest.py --help`) ran the generator, which rewrote manifest.json"
  and that its validator run created an untracked `tools/__pycache__/`, which it removed; `git status` was clean
  afterwards, so the regenerated manifest was byte-identical to the committed one. No tracked repository file was
  changed.
- Full blind reports:
  - `239-words-batch-78-review-correctness-001.md`
  - `239-words-batch-78-review-consistency-001.md`
  - `239-words-batch-78-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the `-b198` and `-b216` scratch worktrees;
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  As in Batch 238, the consistency brief made one exception: the intake record, for its path check. The consistency
  report records that check. The correctness report states "Blindness maintained: no other session-files prompt/report,
  forbidden RU tracking/draft/batch record, or scratch worktree was read."; the comprehensibility report makes no
  statement about unread materials beyond its stated scope, and its reviewer ran `word_title_screen.py` itself as a lead
  rather than reading the coordinator's output.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** (C1 and C2); scoped coverage **NEEDS FIX** (C2); Russian comprehensibility
**UNVERIFIED** (not an assigned facet). "No actionable correctness defect established in the other 28 assigned articles."

- C1 (medium; high confidence for the Japanese sense, medium-high for the title's misleading Russian restriction),
  `思い付く.md:4` (repeated at :12): «вспоминать (о мысли, пришедшей на ум)» restricts the recall gloss to remembering a
  previously occurring thought, whereas the Japanese sense also covers remembering something forgotten, such as an
  urgent errand. Evidence: Digital Daijisen おもい‐つ・く sense 2 "忘れていたことを思い出す", example "急用を―・く"
  (Kotobank); JMdict 1589330 sense 2 "to remember; to recall". Remedy: «придумывать, додумываться; вспоминать», keeping
  the body's distinction from 思い出す and the existing exclusion.
- C2 (medium; high confidence), `被せる.md:20`: 料理に蓋をかぶせておきました is translated only as «Я накрыл еду крышкой.»;
  ておく's leaving/maintaining the resulting state is lost, which frozen EN keeps ("I left a lid over the food"). Evidence:
  Digital Daijisen 置く auxiliary sense 12㋑ "その状態を続けさせる。そのままにする" (Weblio); JMdict 1484320 for the
  covering verb. Remedy: «Я накрыл еду крышкой и оставил её накрытой.»

What the reviewer confirmed:
- All 64 bulleted Japanese example sentences and their kana readings match EN as strings, with full-width Russian
  reading wrappers in place of EN's ASCII wrappers; examples were reviewed in context, not approved by string equality.
- Front matter's word, reading, level, type, kanji, tags and existing exclusions are preserved; added RU exclusions are
  conservative guards, not replacements of EN exclusions. All 30 N2 labels match the pinned community CSV.
- No broken RU relative link; every dropped EN card link has an absent RU target; added links and backlinks preserve
  appropriate comparisons. The read-only validator reported 0 errors.
- Consequential Japanese and Russian entries were inspected (裂く/割く, 蘇る, 被せる/着せる, コック, 蛇口, 清書, 行事,
  薬缶, 栓; вспарывать, додумываться, химикат, сумрачный, полутёмный, дубликат, восполнять, служба, чёрный ход); "No
  additional actionable defect established."

Optional: outside its facets, `コック.md:44` «Исходная строка объединяет значения двух записей» refers to an author-facing
source row; it suggested «Здесь рассматриваются два разных слова с одинаковым написанием.» The separation itself is
correct (JMdict 1050310 versus 2862559). Limits: current dictionaries rather than a historical capture; no
native-speaker, app/device, learning-effectiveness or whole-pool quiz acceptance; Russian comprehensibility unassessed as
a facet.

### Consistency and quiz safety

Verdicts: consistency **CLEAN** (validate.py 0 errors); quiz safety **NEEDS FIX** (Q1); cross-file integration **CLEAN**.

- Q1 (low; medium confidence), `裂く.md:9`: `quiz_exclusions` lacks びりびり. 裂く «раздирать на части; вспарывать» and
  びりびり «рвать в клочья; дребезжать; покалывание (током)» share the tearing sense, so «рвать в клочья» is a defensible
  answer for 裂く. Basis: JMdict 1207730 sense 1. Necessity: "conservative-to-required". Remedy: append びりびり after the
  EN list.

What the reviewer confirmed:
- Every EN `quiz_exclusions` list is a prefix of the RU list in EN order, checked programmatically for all 30; 衣食住 and
  血液 have lists made only of RU additions; 蝋燭, コック, 虹, 薬局 and 蕎麦 have none in EN or RU.
- The exact whole-segment overlaps (надевать, одежда, очередь ×3, церемония, кровь, вентиль, вспоминать, пробка) are all
  guarded on at least one side; a scan of all RU titles found no other defensible unguarded pair except Q1. The in-batch
  pairs without a guard (清書–表紙, 被せる–蓋, 被せる–表紙, 裏口–街角, 行列–行事, 行列–儀式, 血液–血圧, 薬缶–薬局,
  薬局–薬品, 薬指–薬品, 薄暗い–薄める, コック–薬缶) are separated by their titles; the ten one-way in-batch declarations
  suffice under the direct-pair, symmetric-application contract. It agreed with leaving the declined stem-only pairs
  unguarded.
- Titles fit their senses; none needs a change.
- Front matter other than the title and exclusions equals EN on all 30 cards; every EN link resolves to an existing RU
  file or is plain text only when the target is absent; all kanji links match EN where the RU kanji file exists; the
  three RU-only links are apt; footers are set-identical to EN.
- The nine navigation diffs touch only the 13 link brackets/hrefs at EN positions, with EN's path forms; the later 局
  pronunciation mention and 薬品 in 薬.md stay plain, as in EN; the pre-existing 局 → 郵便局 link is untouched; the
  glosses beside the new titles do not mislead.
- The manifest equals the committed one; the intake paths and hashes match.

Optional: `蓋.md:24` («Карточки иероглифа 蓋 пока нет») and `蝋燭.md:29` will go stale when those kanji cards arrive;
they mirror EN, so "leave until the kanji translation batches revisit them". Limits: no live dictionary check (Q1's
evidence is general knowledge of 裂く and the RU card text of びりびり); pre-existing RU-only links outside this batch
(局→郵便局, 側→近く/隣) not evaluated; Russian prose correctness beyond its facets belongs to the other reviewers.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX**; scoped coverage **CLEAN** ("every EN Japanese teaching point is still present
somewhere on the RU card"); correctness **UNVERIFIED** (not an assigned facet).

- C1 (medium; high confidence), `コック.md:44`: «Исходная строка объединяет значения двух записей» and line 48's «эта
  статья выбирает из источника только значения» are translator meta with no learner referent. Remedy: delete line 44 and
  replace lines 47–48 with «У этого написания есть и другие значения; здесь учат только «повар» и «кран, вентиль».»
- C2 (medium; high confidence), `蛇口.md:27`: «отнесено к категории `kango` по правилам репозитория» puts an unexplained
  metadata tag and an author rule in learner prose. Remedy: delete the sentence.
- C3 (medium; high confidence), `蕎麦.md:30`: «Категория `jukujikun`» is the same unexplained metadata term. Remedy:
  «Это чтение всего слова целиком, а не сумма частей. Гречиха от этого не становится пшеницей.»
- C4 (medium; high confidence), `カバー.md:40`: «Не переносите на это заимствование все значения английского cover»
  requires English polysemy. Remedy: delete line 40.
- C5 (medium; high confidence), `血圧.md:17`: the glosses and both examples translate 血圧 as «давление», 圧力's whole
  title, hiding the distinction the card claims. Remedy: «кровяное давление» throughout.
- C6 (medium; high confidence), `蓋.md:20`: «Не могу открыть крышку бутылки» adds a first-person agent and ability to
  intransitive 開きません. Remedy: «Крышка бутылки не открывается.»
- C7 (medium; high confidence), `思い付く.md:4`: the title is too long to scan as an option, bare «додумываться» often
  means speculating beyond what was said, and bare «вспоминать» is 思い出す's whole title. Remedy: «придумывать; мысль
  приходит на ум».
- C8 (low; high confidence), `複写.md:4`: «дубликат» is narrower than the examples and the dictionary (JMdict 1501390).
  Remedy: «копирование; воспроизведение».
- C9 (low; high confidence), `被せる.md:29`: «каузатива» is unexplained. Remedy: restate the warning without the term.
- C10 (low; high confidence), `街角.md:18`: «на следующем углу» drops «улицы» and shows 角's title «угол». Remedy: «…на
  следующем углу улицы.»
- C11 (low; high confidence), `裂く.md:4`: unqualified «вспарывать» is violent and narrow, and line 42 calls it the shared
  sense with 割く. Remedy: title «раздирать на части; разрывать»; name the cut-open sense «разрезать, вскрывать».

Optional: `虹.md:20` «раскинулась» (prefer «перекинулась»); `衣食住.md:17` (delete the remark on the Russian title
order); `衣食住.md:19` «не хватает самого необходимого» is stronger than 困る; `薬品.md:40–41` «в русском заголовке» is
card chrome; `蕎麦.md:47` (delete the JLPT-level note); `薄める.md:20` «белил» (prefer «белой краски»); 表紙's
«переплёт» is qualified in the body, "no change required". Checked and not filed: 儀式's «служба» paragraph, 行事's
contrast with 機能, 栓's road-«пробка» sentence, 清書's memory-aid point, コック's cook-vs-valve distinction, 血圧's active
«сказал», 思い付く's second example, «чёрный ход» and «Мы» in 衣食住 and 行事. Limits: readings, radicals and dictionary
sense splits not re-audited; JapanDict renderings of the stated JMdict ids; comparison cards not read in full.

## Exclusion classification

All 71 EN exclusion entries (23 lists) are retained in EN order; 衣食住, 血液, 蝋燭, コック, 虹, 薬局 and 蕎麦 have none in
EN. Ten of them lie inside the batch, and the other 61 target existing RU cards. At the candidate, twelve direct, one-sided
entries were added on nine new cards, all appended at the end of their lists (衣食住's and 血液's on new `quiz_exclusions`
lines); none targets a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 行列→番, 行列→順番 (2) | Required (exact segment «очередь») | Required |
| 血液→血 (1) | Required (exact segment «кровь») | Required |
| 衣食住→服 (1) | Required (exact segment «одежда») | Required |
| 栓→渋滞 (1) | Required (exact segment «пробка») | Required |
| 清書→書き取り (1) | Conservative | Required (whole word «переписывание» shared) |
| 蘇る→浮かぶ (1) | Conservative | Required (shared stem «всплыва», memory sense) |
| 被せる→履く (1) | Conservative | Conservative |
| 衣食住→衣服, 衣食住→住宅 (2) | Conservative | Conservative |
| 蛇口→水道 (1) | Conservative | Conservative |
| 薬品→農薬 (1) | Conservative | Conservative |

The consistency reviewer found "Over-guarding: none to remove", raised the missing guard Q1 above and recorded that the
author's "conservative" label for 清書→書き取り and 蘇る→浮かぶ "underrates them". The correctness reviewer checked the
RU-added exclusions only as additive guards, and the comprehensibility reviewer found the title-screen exact overlaps
already in `quiz_exclusions`.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`239-words-batch-78-recheck-001.md`.
