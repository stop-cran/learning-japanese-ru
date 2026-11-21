# Batch 231 — independent review 001

## Snapshot and scope

- Reviewed commit: `5af5353eab033af178249f39b48ac4200abf5c24` (tree `f0e6d8ef3d9983f842128471acff66dfe5a652bc`), branch
  `full-ru-231-words-70`, parent `2e53d62`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 230 candidate `5ec190a7c89f162bdb1673eca213fab94aab9624`.
    Before copying, the coordinator's candidate script checked two things: that the five navigation files edited there
    (`kanji/魚.md`, `words/魚.md`, `words/甘い.md`, `words/積む.md` and `words/能力.md`) were unchanged between `5ec190a`
    and the candidate's parent `2e53d62`, and that none of the 30 new cards existed in the primary checkout. The Batch 230
    fixes touched only 鈴, 鐘, 長所, 四角, 四角い, 正方形, 録音, 揃う, 揃える, 継続, 銅, 仕上がる and 長引く; none of them is
    in this batch's path set.
  - The script byte-compared the 35 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 36 batch paths plus `manifest.json`. Its byte scan of all
    36 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 36 committed
    blobs at `5af5353` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - One wrap was held from Batch 230 and applied by the coordinator: after the Batch 230 publication the script replaced
    the anchor «и 釜（かま）называют», which had to occur exactly once, with «и [釜](釜.md)（かま）называют» in the
    published `words/鉢.md`. The other six links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made no other content edits. Its adjudication record
    states:
    - "Content edit by the coordinator: only the held 鉢→釜 navigation link (`words/鉢.md`, «и [釜](釜.md)（かま）называют»),
      applied by `b231_cand.ps1` after Batch 230 publication. No other content edits; the 35 lane files were copied
      unchanged from `-b216` (detached at the B230 candidate `5ec190a`).";
    - "Lane check against the B230 fix: no B231 draft quotes or names a B230 title changed by fix 1 (鈴, 銅, 長引く).";
    - "`type` and `tags` of all 30 cards equal EN.";
    - "RU-added exclusions (3), each one-directional; the targets do not declare them back: 重体→状態, 重体→具合 (a new
      list; EN 重体 has none), 下品→いかがわしい. Checked titles: 状態 «состояние», 具合 «состояние; самочувствие»,
      いかがわしい «сомнительный; непристойный».";
    - "RU-only links (5), each at a substantive comparison (B214/B230 lesson): 金魚:26→鯉 (related-words list that links
      魚), 引力:34→重力, 重力:39→重い, 酸性:34→酸っぱい, 酢:32→酸っぱい. EN leaves them plain. Accepted.";
    - "Link parity also lists 甘い→おいしい: pre-existing RU-only link at 甘い:46 from batch029 (`50d4407`), unchanged by
      B231.";
    - "Author's limit: 鉢↔釜 reciprocal — resolved by the held link above."

    The committed manifest records 5,049 entries; the reviewers' `tools/validate.py` runs on the candidate reported 0
    errors.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 6 files with 7 restored navigation links (the kanji card 魚 and the word cards 魚, 甘い, 積む, 能力 and 鉢);
    - `manifest.json` (`contentVersion` `9f7fbab4482b1d53`, 5,049 entries);
    - the intake, whose note reads "B231 30-card adaptation with seven navigation-only link restorations in six existing
      files (the 鉢→釜 link applied by the coordinator after Batch 230 publication); candidate before blind review."
- Published baseline recorded in the intake: `80dbfc2715dd0eb1c7c12df952c76a868cd95a35` (Batch 230 merge). Parent
  `2e53d62` adds only the Batch 230 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on any failing check, passed:
  - `tools/validate.py`;
  - unit tests (the authoring worktree run reported 124 tests);
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 6 files;
  - title screen: no unguarded exact title-segment overlap (24 `OK` lines for pairs already guarded by an exclusion and
    190 stem-only `!!` lines);
  - link parity: no EN link lost where the RU target exists; the RU-only links are the five accepted above and the
    pre-existing 甘い→おいしい.
- Common sample: all three reviewers read all 30 new word cards in full against their full EN originals, and the six
  navigation-file diffs. The consistency reviewer also compared front matter and links with EN by script.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file), the existing RU cards 課程, 方向, 重い, 鯉, 魚,
    ピン, 鍋, 強調 and 発音 in full for comparisons, and all six navigation diffs; other comparison titles were checked
    without treating those cards as fully reviewed.
  - Inspected the actual Jisho/JMdict entries and Japanese dictionary sections, including the reading and spelling flags
    for 重役 (obsolete おもやく against じゅうやく), 醜い (rare 見憎い) and 酢 (rare 醋/酸 read す); compared mechanically
    that all 30 files keep their EN seven-digit citation identifiers and external source URLs.
  - Japanese sources beyond Jisho: Digital Daijisen on Weblio for 針路, 重役, 重点, 重体, 給与 and 酌む; the World
    Encyclopedia and Nipponica sections for 釜 on Kotobank.
  - Russian sources: Gramota's Russian Orthographic Dictionary search for саке and Gramota's spravka answer 309247; Gramota's
    Kuznetsov entry for увесистый (optional item).
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 cards in full against EN (front matter and body) and the complete `-U0` diffs of all six navigation files
    with the EN counterpart lines; read the front matter of 合う, 一致, 状態, 具合 and いかがわしい.
  - Checked that the intake's 36 payload paths equal the 36 content paths of the diff and that every
    `candidateRawSha256` matches; checked the manifest; enumerated every EN file that links one of the 30 new words and
    compared it with RU.
  - Ran `tools/validate.py` (0 errors) and a title screen against all RU word titles (126 candidate pairs not already
    guarded, no exact whole-word segment overlap among them). It did not re-fetch dictionary pages.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN and the six navigation diffs. Title-screen overlaps were used as leads only.
  - Opened JMdict entries for its findings (1186230, 1303280, 1336770, 1336900 and 1335780) and Digital Daijisen for 重役,
    みじめ and 金魚鉢, not every footer. It ran its own `word_title_screen.py` run as a lead and a link-parity check (no EN
    link whose RU target exists was dropped); it ran no validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. Each report records
  the snapshot `5af5353` with an empty `git status --porcelain`. No fix was applied until all three reports were
  complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The consistency reviewer disclosed one deviation: it ran `python tools/build_manifest.py --help`
  once, which executed the generator (printing 5049 files and version `9f7fbab4482b1d53`); `git status` afterwards showed
  no tracked file modified, and it deleted the untracked `tools/__pycache__` its run created. HEAD and the index never
  changed. No tracked repository file was changed.
- Full blind reports:
  - `231-words-batch-70-review-correctness-001.md`
  - `231-words-batch-70-review-consistency-001.md`
  - `231-words-batch-70-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The consistency brief made the intake record the single exception, for its path and hash check. The correctness report
  says that author/reviewer reports, title-screen output, translation-batch/draft records and translation tracking were
  not consulted. The consistency report says that it did not read author reports, other reviewer reports, batch records,
  drafts or tracking; it read the intake record, whose payload paths and hashes it checked. The comprehensibility report
  says that it read no author report, batch record or other review.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for 汲む and 酌む (Russian spelling only), **CLEAN** for the other 28 new cards;
scoped coverage **CLEAN** for all 30. No substantive Japanese meaning, attachment, transitivity, polarity or tense defect
was established. Comprehensibility and quiz safety were not assigned.

- C1 (minor, correctness (Russian orthography); high confidence), `酌む.md:4,12,16,19-20,27,33,41,44` and `汲む.md:34`:
  the established Russian borrowing is repeatedly printed «сакэ», including 酌む's title and model translations, whereas
  the standard Russian spelling is «саке». This teaches a nonstandard spelling of the Russian gloss; it does not change
  the Japanese sense, reading or the 汲む/酌む distinction. Remedy: replace «сакэ» with «саке» at those occurrences,
  including the front-matter title and heading, and leave Japanese 酒/さけ and the Japanese examples unchanged. Evidence:
  the Russian Orthographic Dictionary entry on Gramota («саке́, нескл., ж. и с.») and Gramota's spravka answer 309247,
  which lists «саке» among foreign common nouns ending in е after consonants.

What the reviewer confirmed:
- No EN sense, example, consequential qualification or Japanese teaching distinction is missing; source-only English
  comparisons need not be reproduced literally.
- Stable metadata is retained; the exclusion changes are additions (重体: 状態/具合; 下品: いかがわしい), not lost baseline
  guards. No missing relative target or dropped EN link whose RU target exists was detected. All 30 files keep their EN
  seven-digit citation identifiers and external source URLs.
- Daijisen supports 針路 (navigational course and intended direction), 重役 (separate readings and senses), 重点 (important
  point and iteration mark), 重体 (life-endangering illness or injury), 給与 (money or goods supplied, including
  制服を給与する) and 酌む (serving alcohol); the World Encyclopedia and Nipponica sections for 釜 support ceramic and metal
  vessels. The broader コース meal and service uses are supported by the JMdict family; the extra katakana/no-kanji
  section is accurate and harmless.
- An alternate reading or rare spelling (おもやく, 見憎い, 醋/酸) is not itself an error. Russian past-tense masculine forms
  and contextually supplied pronouns do not assert that Japanese grammar encodes those features. The six navigation
  diffs keep the displayed teaching meanings.

Optional: outside its facets, wording polish in `下品.md:39-40` and `酸っぱい.md:40-41`, which keep source-list or
dictionary-gloss framing a Russian learner does not need (for 下品, «Не используйте 下品 как общее слово для скупости»;
for 酸っぱい, «Здесь речь о кислом вкусе, а не об измерении кислотности»); and a nonblocking title precision for
`重たい.md:4,12`, «тяжёлый; гнетущий (об атмосфере)» instead of «увесистый; гнетущий (об атмосфере)» (Gramota's Kuznetsov
entry for «увесистый» emphasizes considerable weight). Limits: not a full quiz-pool, native-speaker, device or
whole-corpus review; the larger suggested comparison list was not fully read; the archived JMdict numeric ID/sense-version
mapping was not reconstructed for every footer (retention was verified); some live requests returned HTTP 429, and a
later Gramota repeat was rate-limited after its entry had already been inspected.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **NEEDS FIX** (one minor finding); cross-file integration **CLEAN**.
Linguistic correctness and comprehensibility were not assessed beyond reading for consistency.

- F1 (minor, quiz safety; medium confidence), `重なる.md` `quiz_exclusions` (cited as line 10; the key is on line 9): the
  RU title «накладываться друг на друга; совпадать по времени» adds a «совпадать» sense that EN's "be piled up; overlap"
  lacks, so it shares the verb «совпадать» with 合う «подходить; совпадать» and is a near-lexical neighbour of 一致
  «совпадение; единодушие»; neither pair is declared on either side, while the repo already guards 一致–合う. Remedy:
  `quiz_exclusions: [積もる, 積む, 繰り返す, 被る, 合わせる, 重ねる, 合う]`, with 一致 optional (`…, 合う, 一致]`).
  Evidence: the RU titles; JMdict 合う "to match; to coincide"; the card's own 会議が試験と重なりました.

What the reviewer confirmed:
- All other EN exclusion lists are byte-identical in RU, so all EN exclusions are retained; front matter other than
  `title` and the two RU-extended lists equals EN. The title screen against all RU titles found no further
  defensible-answer gap; it judged 金魚↔魚, 金魚↔鯉, 重量↔終了/量, 重力↔重い, 酢↔酸っぱい/しょうゆ/塩, 酒場↔店
  (EN-guarded), 都心↔郊外/都市 (guarded), 郵送↔郵便局/切手/発送-type words, 重たい↔苦しい «тяжёлый», 重体↔病気/症状 and
  重役↔部長/課長/経営 adequately separated.
- The five RU-only links (金魚→鯉, 引力→重力, 重力→重い, 酸性→酸っぱい and 酢→酸っぱい) resolve, are navigation-only and
  are acceptable. (It cited the 金魚 link as `金魚.md:21`; the link is on line 26.)
- The seven navigation restorations each match the EN position and href form, and the `-U0` diffs show only bracket and
  href changes: kanji 魚 lines 37 and 45 (EN 28 and 36), word 魚:25 (EN 27), 甘い:36 (苦い stays plain, as in EN), 積む:32,
  能力:22 (the form 重ねて) and 鉢:37 (same sentence as 鍋, as in EN line 37).
- Every EN file that links one of the 30 new words and exists in RU links it; the dropped EN links inside the new cards
  (針路→kanji 針, 重量→kanji 量, 重点→終点, みっともない→厚かましい and 郵送→kanji 郵) have no RU target. All relative
  targets resolve.
- The intake lists 36 payload paths equal to the 36 content paths of the diff, every `candidateRawSha256` matches, `held`
  is empty, and it adds no learner content; the committed manifest equals a fresh generation (version
  `9f7fbab4482b1d53`); the commit holds 38 files (30 new cards, 6 navigation files, manifest and intake).

Optional: none. Limits: dictionary entries were not re-fetched; the senses cited come from the cards' own citations and
standard JMdict glosses; its own naive SHA-256 check of `strokes/*.json` against the manifest disagreed (likely line-ending
normalization in the generator, unrelated to this batch) and was not pursued; no app quiz was executed; "defensible
answer" is a judgement from titles and glosses.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** for 下品, みじめ, 重役, 重量, 引力, 重たい and 金魚 (the other 23 new cards CLEAN on
this facet); scoped coverage **NEEDS FIX** for みじめ and 重役, **CLEAN** for the other 28.

- 1 (minor; high confidence), `下品.md:39-40`: «В исходном списке слов… «скупость»» is an author note about a source-list
  gloss the RU card never shows, so a beginner may now connect 下品 with stinginess. Remedy: delete lines 39–40. Evidence:
  JMdict 1186230 sense 1.
- 2 (minor, also coverage; high confidence), `みじめ.md:4,12,19`: the title and first translation require humiliation
  («жалкий и униженный»), narrowing Daijisen and JMdict 1303280 (miserable, wretched, unhappy, sad, pitiable) and EN.
  Remedy: title «жалкий; плачевный»; example «Проиграв матч с большим отрывом, я почувствовал себя несчастным и жалким.»
- 3 (minor, also coverage; high confidence), `重役.md:4,19,39`: «член правления» and the first example narrow 会社の重役 to
  board membership, whereas the card's own Daijisen sense 2 is 取締役・監査役など役員の総称 and JMdict 1336770 sense 1 is
  director/executive/top management. Remedy: title «руководитель компании; важный пост»; example «На совещании
  присутствовал один из руководителей компании.»; line 39 «Не каждый начальник отдела — руководитель компании».
- 4 (minor; high confidence on the divergence, limited impact), `重量.md:18`: the noun 重量 is translated with the verb
  «весит». Remedy: «Вес этого багажа — десять килограммов.» Evidence: JMdict 1336900.
- 5 (minor; high confidence), `重量.md:38`: «не называет боксёра-тяжеловеса» rejects a person-gloss the RU card never
  shows. Remedy: «Весовую категорию называют не само 重量, а отдельные слова 重量級（じゅうりょうきゅう）и
  ヘビー級（ヘビーきゅう）.»
- 6 (minor; high confidence), `引力.md:20`: «Притяжение Земли притягивает предметы» is tautological and hides 引力 (noun)
  against 引きつけます. Remedy: «Сила притяжения Земли тянет предметы к себе.»
- 7 (minor; high confidence), `重たい.md:4,19,22`: the lead gloss «увесистый» is never explained, is narrower than JMdict
  1335780 "heavy; weighty", and the examples use «тяжёлый». Remedy: title «тяжёлый; гнетущий (об атмосфере)»; the quiz
  collision with 重い «тяжёлый» is outside these facets, and the existing exclusion should stay.
- 8 (minor; high confidence on the definition, limited impact), `金魚.md:16`: «круглый аквариум» adds a shape and
  substitutes a tank for a bowl; Daijisen 金魚鉢 is 金魚を飼うための、ガラス製などの鉢形の容器. Remedy: «стеклянная чаша
  для золотых рыбок».

Optional: コース:32–33, the katakana note EN lacks, can stay; 下品:20 «грубо» is a fair "crude", but «пошло» would keep the
contrast with 粗い/荒い clearer; 配る does not name 分ける, whose title already says «раздавать (по частям)»; 酢:28 «по кун
/ по он» is terse, and «кунным чтением, а не онным» would match the glossary; 都心's last sentence is slightly awkward, not
unclear; 釘 «крепёжный штырь» is technical but explained; 金魚 has only collocations, as EN does; «сакэ», «набэ», «патинко»
and «годан/итидан» are explained or already established. Limits: not a native-speaker or corpus-frequency certification;
quiz pairs and full Japanese correctness were not assigned; dictionary checks were opened for the findings, not for every
footer; title-screen stem hits were not treated as defects.

## Exclusion classification

All 130 EN exclusion entries (25 lists) are retained in EN order; 金魚, 重量, 重体, 酸性 and 酢 have none. Fourteen of
them lie inside the batch. At the candidate, three direct, one-sided entries were added on two new cards; one of them
(重体) is a new list, and none targets a batch word.

| Entries | Consistency reviewer |
|---|---|
| 下品→いかがわしい (1) | REQUIRED: a learner can defensibly answer «непристойный» with 下品 and «неприличный» with いかがわしい; keep |
| 重体→状態, 重体→具合 (2, new list) | CONSERVATIVE: real shared-gloss basis («состояние»), necessity unestablished; mildly over-guarding, nonblocking |

下品 «вульгарный; неприличный» and いかがわしい «сомнительный; непристойный» are near-synonymous in Russian although EN's
titles ("vulgar; indecent" against "dubious; disreputable") were separate. 重体 «критическое состояние (угроза жизни)»
shares only the generic «состояние» with 状態 «состояние» and 具合 «состояние; самочувствие»; the reviewer noted that 調子
and 心理 share the same token unguarded, which is right, so keeping or dropping the 重体 entries is an editorial choice and
dropping them would not create a gap. All three entries are kept. The correctness reviewer noted that the exclusion
changes are additions, not lost baseline guards, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`231-words-batch-70-recheck-001.md`.
