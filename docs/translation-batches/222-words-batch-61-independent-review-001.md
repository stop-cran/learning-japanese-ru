# Batch 222 — independent review 001

## Snapshot and scope

- Reviewed commit: `d0d6d08431a1e7dd81d6eaa151a8c841c37c297e` (tree `c6b8f7f32697ac0e681e2544e3deb8f92208352a`), branch
  `full-ru-222-words-61`, parent `908d7c0`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 221 candidate `f888c34e8eb7c8d29c76c0433dbb3b0035ee8e3b`.
    Before copying, the coordinator checked two things: that the 6 navigation files edited there were unchanged between
    `f888c34` and the candidate's parent `908d7c0`, and that none of the 30 new cards existed there. The Batch 221 fixes
    touched only ドライブ, バン, ボール, パイプ, ド, ママ, ビデオ and トンネル; none of them is in this batch's path set.
  - The coordinator byte-compared the 36 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 37 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - One held wrap was carried into this batch: Batch 221's ベンチ had left its EN link to ソファー as plain text because
    ソファー is a Batch 222 word. The coordinator wrapped that mention at EN's position (ベンチ line 28) in the primary
    checkout, on top of the published ベンチ card; it is the only change to that card.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 7 files with 7 restored navigation links (including the held ベンチ→ソファー link);
    - `manifest.json` (`contentVersion` `57a4e697f7978cab`, 4,779 entries);
    - the intake.
- Published baseline recorded in the intake: `e50971240cfdcf5e45000db53892cdc31824f244` (Batch 221 merge). Parent
  `908d7c0` adds only the Batch 221 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK;
  - content budget: OK, 4,796 entries;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 7 files and 7 links, with no problem;
  - title screen: no unguarded exact title-segment overlap;
  - link parity: no EN link lost where the RU target exists, and seven RU-only links (カード→地図, チャンス→望み,
    ダンス→踊り, ソファー→いす with link text 椅子, スタンド→ガソリンスタンド, スタンド→台 and ジーンズ→履く). EN mentions five of
    these targets unlinked in a substantive comparison; 地図 and 望み are RU-added comparisons (the Russian homograph
    «карта» and the shared «шанс»).
- Common sample: all three reviewers read all 30 new word cards in full, each against its full EN original. The
  consistency reviewer compared them by script and by eye.
- Correctness review scope:
  - Read in full the existing RU 望み, 地図, 踊り, 台, いす, ガソリンスタンド and 履く (the RU-only link targets) and ベンチ
    (the held-link card); inspected all seven navigation diffs and the suggested comparator titles; read the binding
    instructions and the format reference.
  - Read the JMdict entries on Jisho for the headwords, including 1036400 and 2848325 (カード), 1076860 (ダイヤ), 1069210
    (スター), 1069930 (スタンド), 1519620 (望み), 1078040 (チャンス) and 2843595 (ジュース, deuce).
  - Japanese sources: Kotobank entries for ダイヤ, ダイヤモンド, センター and ショッピングセンター.
  - Russian sources: Gramota entries (карточка, открытка, карта, демонстрация, команда, шанс, надежда, танец, диван,
    центр, набор, установка, настройка, звезда, трибуна, стиль, фигура, выключатель, переключатель, группа, бонус,
    бриллиант, лампа, шатёр, свежий), Russian Wiktionary (карта, сгусток, деним), Kuznetsov «гранд-» on gufo.me and
    specialist usage pages for tennis «ровно» (tennis-hub), cheesemaking «сгусток» (zefbio), speed skating (megabook),
    «за счёт заведения» (kartaslov) and «центральный полевой игрок» (ScanDict, weak evidence).
  - Ran `tools/validate.py` (0 errors); ran no generator. An initial oversized read returned only a preview and was not
    counted; every card was then read completely in three-card RU/EN batches.
- Consistency review scope:
  - Read all 30 cards, all seven navigation diffs and the `manifest.json` diff in full, and compared front matter,
    headings, example counts, JMdict ids, link pairs and path forms with EN.
  - Checked the intake only for its path list, candidate hashes and the absence of learner content, as its prompt
    permitted.
  - Ran `tools/validate.py` (0 errors) and its own read-only stem screen of RU word titles plus the supplied cluster
    list; the report gives the screen's size as 252 titles. It wrote a scratch title list,
    `b222-consistency-scratch-titles.txt`, in the coordinator's session folder outside the repository.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN, the seven link-restore diffs, and the titles and contrast passages of about 70
    named comparison cards (among them 地図, 日付, 月日, 機会, 望み, 踊り, 宝石, 玉, 予定, 星, 有名, 台, ガソリンスタンド, 飲み物,
    命令, 受付, 電灯, 機械, 選手 and ベンチ).
  - Checked senses through the Jisho API and JapanDict; JMdictDB itself was password-gated. It did not report running the
    content validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; each report says its model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time. Each report records the snapshot `d0d6d08` with an empty
  `git status --porcelain`. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written; the consistency reviewer's scratch title list above is the only
  other file, and it is outside the repository.
- Full blind reports:
  - `222-words-batch-61-review-correctness-001.md`
  - `222-words-batch-61-review-consistency-001.md`
  - `222-words-batch-61-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`, except
    that the consistency reviewer checked only the intake's path list and hashes;
  - the scratch worktrees;
  - one another's reports.

  The correctness report confirms that it read no author report or prompt, title-screen output, other review, batch or
  draft directory or tracking file. The consistency report confirms that it read no batch record, author report,
  title-screen output or scratch worktree. The comprehensibility report does not restate the rules.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** (カード; the titles of ダイヤ, スター and スタンド); scoped coverage **NEEDS FIX**
(those titles and ソファー's navigation). The other new cards are **CLEAN** in both facets.

- C1 (minor; high confidence), `カード.md:35`: «словом „карточка“ называют также скребок для теста» transfers a Japanese
  dictionary sense to the Russian noun; EN describes the card entry, not a Russian baking-tool name. Remedy: attribute
  the scraper to Japanese カード in baking texts. Evidence: JMdict 1036400 sense 7 "dough scraper; spatula" and the
  separate curd entry 2848325; Gramota «карточка» has no such sense. The positive Japanese evidence, not Russian
  dictionary silence, establishes the misattribution.
- C2 (minor; high confidence), `カード.md:31`: «„картой“ カード бывает только как платёжная или игральная карта» makes an
  exhaustive boundary that Russian «карта» does not support (Gramota sense 3, an information form; Russian Wiktionary
  sense 3, identification and payment cards). The 地図 map contrast is sound; «только» is not. Remedy: keep the map
  contrast and choose the translation by context.
- C3 (minor; high confidence on the lexical restrictions, medium-high on their learning impact): three short labels
  narrow a broad source headword although the body keeps the broader sense:
  - `ダイヤ.md:4,12,16,36`: «бриллиант» requires a cut and polished stone (Gramota бриллиант sense 1), while EN "diamond"
    and RU line 16 include «алмаз». Remedy: «алмаз; бриллиант; график движения поездов», and «алмаз; бриллиант» in the
    source line for 1076860. The ring example is correctly translated.
  - `スター.md:4,12,16,33`: «знаменитость; звезда (кино, спорта и т. п.)» restricts both equivalents to people, although
    the symbol and celestial senses are taught. Remedy: «звезда; знаменитость».
  - `スタンド.md:4,12,17`: «настольная лампа» excludes the floor lamp kept in line 17 and EN (JMdict 1069930 sense 4).
    Remedy: «трибуна; подставка, стойка; настольная или напольная лампа».
- C4 (minor; high confidence), `ソファー.md:28`: ベンチ is a substantive furniture comparison but stays unlinked although
  `words/ベンチ.md` exists. The restored ベンチ→ソファー link does not supply the opposite navigation. EN's mention is also
  plain, so this is not a dropped EN link. Remedy: «[ベンチ](ベンチ.md) — скамья».

What the reviewer confirmed:
- Source front matter is preserved apart from the translated title and the added exclusions; no EN exclusion is lost.
  Every EN link whose RU target exists is retained; キャンプ and ただ stay plain text. The main Japanese examples and
  reading lines match EN, including スタイル's hiragana reading lines and グランド's all-kana example.
- 望みがある against チャンス is a defensible contextual distinction, not a substitution ban (JMdict 1519620 and 1078040;
  Gramota надежда and шанс). The added RU links preserve the described Japanese senses and add no malformed Japanese.
- Subject to C1–C3, no wrong Russian equivalent was established for the title vocabulary in the Gramota entries listed
  above. «Сырный сгусток» matches Russian Wiktionary сгусток and cheesemaking usage; tennis «ровно» is deuce (40:40);
  «деним» and «шатёр» are attested; «свежее полотенце» is supported by Gramota свежий sense 3. センター's commercial
  facility is supported by Kotobank ショッピングセンター and Gramota центр sense 4.

Optional: «поздравительную открытку» for the greeting card; soften スープ:20 to «по-русски обычно говорят „есть суп“»; keep
センター's general «центр» and qualify the player sense «(в бейсболе)»; clarify ジュース:23 as «40:40 и последующие равенства в
гейме». Limits: no native or frequency certification and no whole-pool quiz, manifest or publication audit; some
specialist phrases rest on usage rather than headword evidence (especially ScanDict); failed 429 and 404 requests were not
treated as evidence.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **NEEDS FIX** (F1–F4, minor); scoped coverage (cross-file integration)
**CLEAN**, with one minor consistency note (F5). All 21 RU-added guards are justified; none over-guards.

- F1 (minor; medium confidence), `トラック.md:9`: a truck is an automobile, so 自動車 «автомобиль» is a defensible answer
  for «грузовик», but only 車 is guarded. Precedent: バス and タクシー each guard both 車 and 自動車. Remedy:
  `quiz_exclusions: [車, 自動車]`.
- F2 (minor; medium confidence), `デート.md:9`: the body records the calendar-date sense (JMdict 1081430 sense 2), which
  EN guards with 月日, but 日付 «дата» is the plainest title for it and is unguarded. 日付 is a navigation-only file here,
  so the guard belongs on デート. Remedy: `[月日, 日付]`. EN has the same gap in English; this is a RU-side decision.
- F3 (minor; medium confidence), `スタンド.md:9`: the body teaches スタンド as short for ガソリンスタンド «автозаправочная
  станция», but the title omits it and ガソリンスタンド is unguarded. Remedy: add ガソリンスタンド.
- F4 (minor; medium-low confidence), `スタンド.md:9`: 明かり «свет; светильник» names the lamp sense already guarded with
  電灯, and 明かり itself guards 電灯. Remedy: add 明かり (with F3: `[台, 電灯, 受付, ガソリンスタンド, 明かり]`). 灯 «свет
  лампы; огонёк» is weaker and optional.
- F5 (minor or optional; medium-low confidence), `ソファー.md:28`: 椅子 is linked but the equally compared ベンチ is plain
  although its card exists. Remedy: link it, matching the sibling form. Not a learning defect.

What the reviewer confirmed:
- `word`, `reading`, `jlpt`, `type`, `kanji` and `tags` equal EN on every card; heading sets, the H1 reading form,
  example-bullet counts and JMdict ids equal EN. All EN exclusions on the 13 cards that have them are retained.
- Every card's link pairs equal EN's except the absent キャンプ and ただ (plain text) and the seven RU-only links, each of
  which it accepted at a substantive comparison. No link in the 30 cards or the seven navigation files is broken, and
  path forms match EN, including `../kanji/機.md`.
- An EN-to-RU scan over words, kanji and articles found every EN link to a batch word from an existing RU file now
  present once, with no prose change; each navigation diff is a single line with only link brackets added.
- The manifest diff contains only the 37 new hashes and `contentVersion`; the intake path list equals the content diff's
  37 paths, its candidate hashes match the files, and it adds no learner content.
- Screens with no defect included カード/切符/手紙, デート/約束, デモ/でも, テント/小屋, チーズ/バター/牛乳, タオル/ハンカチ,
  ソファー/いす/ベンチ/席, センター/中/半ば, セット/準備, スープ/食事, スケート/スキー/滑る, スイッチ/ボタン, ジェット機/便,
  ゲーム/演技/トランプ, チーム/団体/組/グループ and グランド/立派/偉大/莫大.

Optional: the 灯 pair for スタンド (F4) and トラック→乗り物 (not needed; the 飛行機 precedent does not guard 乗り物). Limits:
JMdict was not re-opened online; quiz necessity was judged from displayed RU titles and taught senses, not the app's
distractor sampler; the linguistic correctness of the RU-added prose in カード, チャンス, ダンス and ソファー is outside this
facet.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (カード and ジュース; the other 28 cards are clean in this facet); scoped coverage
**CLEAN**.

- 1 (minor; high confidence), `カード.md:3,11,15`: the title and body teach «сырный сгусток» for the separate food word,
  which a beginner can read as a cheese clot or curd cheese rather than the milk curd cheese is made from; the bare title
  is the quiz answer. Remedy: «сгусток молока (для сыра)» and matching body wording. Evidence: Jisho's separate カード
  entry, sense "curd"; JapanDict gives only «карточка» for 1036400. The reviewer did not claim «сгусток» is wrong.
- 2 (minor; high confidence), `ジュース.md:3,11,18`: «ровно (счёт в теннисе)» uses an ordinary adverb ("exactly",
  "evenly") as if it were a score name, and the example «счёт стал «ровно»» has the same problem. Remedy: «равный счёт (в
  теннисе)» and «счёт стал равным». Evidence: JapanDict «равный счёт (в теннисе)»; Jisho デュース/ジュース "deuce".

What the reviewer confirmed: no English leftover, Cyrillic reading, Latin-script learner word, quiz-behaviour sentence or
author note in the 30 cards. The EN teaching points it checked are present, including the curd identity, the two デモ
senses, スープを飲む as «есть суп», activity against equipment for スケート and スキー, and the separate グラウンド noun. The
restored ベンチ↔ソファー link is consistent (скамейка against диван). Title-screen stem hits such as картофель, работа,
спорт, катана and напиток are shared stems, not competing answers.

Optional: トラック:11 «ехать в грузовике» is slightly narrow, since a rider may be in the bed; «ехать на грузовике» covers
both. グランド's comma title «большой, гранд- (в составных названиях)» is awkward as one quiz string but not a wrong gloss.
Limits: senses were checked through the Jisho API and JapanDict, not the live JMdictDB page; no native-speaker check;
quiz-exclusion completeness was not assigned; comparison cards were read only as far as the named contrast.

## Exclusion classification

All 18 EN exclusion entries (13 lists) are retained. At the candidate, 21 direct, one-sided entries were added on 17 new
cards (eight of them new lists):

| Entries | Author | Consistency reviewer |
|---|---|---|
| チャンス→望み, ダンス→踊り, ジェット機→飛行機, ゲーム→遊び, グランド→大きい, グランド→大きな | required | required |
| カード→地図, トラック→車, チーム→命令, ダイヤ→宝石, ダイヤ→玉, ダイヤ→予定, スター→有名, スタンド→電灯, ジーンズ→ズボン, ジュース→飲み物, グループ→クラス | conservative | required |
| タイプライター→機械, センター→選手, スタンド→受付 | conservative | conservative |
| サービス→無料 | conservative | conservative, leaning required |

The reviewer judged all 21 justified and none an over-guard; the author's and reviewer's classifications differ only in
strength. The correctness reviewer identified the added exclusions without auditing quiz safety, and the
comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fixes and the final verdicts are in
`222-words-batch-61-recheck-001.md`.
