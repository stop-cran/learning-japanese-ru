# Batch 213 — independent review 001

## Snapshot and scope

- Reviewed commit: `3c8461447a0a88352701ecb3fc7183b5c545a07b` (tree `2e363e3eaf674dd400edb587315ee26cfe455597`), branch
  `full-ru-213-words-52`, parent `1269d26`. The candidate was committed signed directly and pushed before review.
  - The content was authored in a scratch worktree on the Batch 212 candidate `d5fd0d933b7590c71fceadde93af255a14c4e0c0`.
    Before copying, the coordinator checked that the 21 navigation files were unchanged between `d5fd0d9` and the
    candidate's parent `1269d26`, and that none of the 30 new cards existed there; after copying, it byte-compared all 51
    scratch content files between the scratch worktree and the primary checkout. No held wraps were carried into this
    batch.
  - Before the candidate, the coordinator retitled four author drafts (title and H1):

    | Card | Author title | Candidate title | Reason |
    |---|---|---|---|
    | 大部分 | «преобладающая часть; почти всё» | «большая часть; большинство» | «почти всё» overstated EN "greater part; most" (JMdict 1414850) |
    | 大半 | «бо́льшая половина; в основном» | «большинство; в основном» | «бо́льшая половина» narrowed EN "majority; most" |
    | 報告 | «сообщение о результатах; рапорт» | «отчёт; сообщение о результатах» | «рапорт» is a military or official report, narrower than EN "report" |
    | 外交 | «дипломатия; внешние сношения» | «дипломатия; отношения с другими странами» | «внешние сношения» is dated bureaucratic wording for EN "foreign relations" |

    The new exact segments are guarded: 大部分 and 大半 against たいてい (and 大半 against 大部分, an EN pair), and 報告
    against リポート and レポート.
  - The author had added combining stress marks (U+0301) in 大部分 and 大半; the coordinator removed them because the
    published corpus uses none. In the same pass it rephrased `大部分.md:25` to «大 определяет всё это существительное
    целиком: «большая часть», то есть больше, чем остальное.» (EN: "the large or greater portion").
  - The candidate differs from the published baseline by 30 new word cards, 21 files with 35 restored navigation links,
    `manifest.json` (`contentVersion` `2266857bdb63c3be`, 4,504 entries) and the intake.
- Published baseline recorded in the intake: `306307836e58012124f6f7856f0d87d465d47d47` (Batch 212 merge). Parent `1269d26`
  adds only the Batch 212 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers. Correctness and comprehensibility read each
  card against its full EN original; consistency compared front matter and links with EN by script.
  - Correctness also read the three binding RU instruction and format files, the comparison cards ほとんど, たいてい,
    莫大, 大小, 熱中, 下ろす, 瞬間, 次第, 州, リポート, 知らせる, 伝える and レポート in full, and every changed line of the
    eight kanji and thirteen word files in the navigation diff. It inspected the Jisho/JMdict entries for all 30
    headwords, for 夫妻 and for the RU-added guard targets, separating alternate readings and homonyms (大家 おおや,
    たいか; 地方 ちほう, じかた). Russian-side evidence came from Kuznetsov entries on Gramota (арендодатель, съезд,
    президент, министр, госпожа/господин, самозабвенный, заря, рубеж, гробница, полночь, округа, дипломатия, отчёт,
    исходить, область, провинция, стена, вечер, земля, снять), the Большой универсальный словарь entry for рубеж and
    ru.wiktionary округа and расстегнуть. Several Gramota requests returned HTTP 429; no conclusion was drawn from those
    failures. It also read Kotobank 塀 and 壁 and Kotobank 地方 (Digital Daijisen ちほう 1–2, じかた 3), ran
    `link_parity.py` on the 30 cards and `tools/validate.py` (0 errors).
  - Consistency read all 30 cards and all 21 navigation diffs in full, checked by script that removing link markup from
    each navigation file restores its parent text and that every added link also exists in EN with the same path form,
    checked `manifest.json` (recomputed in memory) and the intake's path list and hashes, compared the front matter, links
    and exclusions of every new card with EN by script, screened the new titles against every RU word title by exact
    segment and stem, ran `tools/validate.py` (0 errors) and classified every RU-added exclusion. Its JMdict senses for
    the exclusion pairs came from its own knowledge and were not re-fetched. It did not read EN bodies line by line.
  - Comprehensibility read the 30 cards in full against EN and read 熱中, 発表, 日中, レポート, ほとんど, 壁, 連絡 and
    奥さん in full and the titles of 妻, 婦人, 社長 and 戦争 as comparisons, not as a second verdict sample. It judged the
    navigation diffs as link wraps only and did not read the kanji files in full. It ran `link_parity.py` on the 30 cards,
    used `word_title_screen.py` only as a lead and checked the 地方, 大統領, 大部分 and ほとんど senses on Jisho; it did not
    re-fetch every cited dictionary entry, and its report records no `tools/validate.py` run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD was still `3c84614`
  and that `git status --porcelain --ignored` was empty. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator and named the report as the only file a
  reviewer writes. The correctness and consistency reports state that no generator was run and the repository was not
  modified; the comprehensibility report does not mention generators. The coordinator found the tree clean after each review.
- Full blind reports:
  - `213-words-batch-52-review-correctness-001.md`
  - `213-words-batch-52-review-consistency-001.md`
  - `213-words-batch-52-review-comprehensibility-001.md`
- Initial reviewers were told not to read the author report or prompt, the coordinator's title-screen output or notes, the
  batch records, or one another's reports; the correctness report confirms that no batch records, scratch worktree, author
  material or other report was read.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN**; scoped coverage **CLEAN**. No findings; one optional note.

The reviewer checked every example translation against its Japanese, including completed versus ongoing states,
transitivity, passive appointment and election, recipient に, を境に, を通じて and the reported-information construction
によると. It found no missing Japanese lexical token and no difference in word, reading, jlpt, type, kanji or tags in any of
the 30 pairs; all EN exclusions are retained. It confirmed that 夫妻 carries the own-family restriction, that 大家 has
separate おおや and たいか entries, that the gender-neutral landlord explanation is preserved, that the poetic marker in
夕べ applies to the simple evening noun, and that «полночь» is cautioned against only as exactly 00:00. It treated
masculine Russian past forms as contextual renderings and read 塀 «забор; ограда» together with the body's
enclosing-wall and material qualification.

- Optional O1 (nonblocking precision), `地方.md:35`: qualify the closing sentence as «При чтении ちほう слово не означает
  „побережье“», since EN says "This reading" and Digital Daijisen (Kotobank 地方) and Jisho give the coast/shore sense to
  じかた.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (one added guard); cross-file integration **CLEAN**.

- F1 (minor, medium confidence), `大.md:7`: 大's title «большой размер; огромный (как приставка)» introduces «огромный»,
  and 巨大 «громадный; гигантский» (JMdict "huge; gigantic; enormous") is a defensible answer for it with no guard on
  either side, although the batch guards 莫大 for the same overlap. Remedy: `quiz_exclusions: [大きい, 大きな, 莫大, 巨大,
  大小]`.
- The front matter and links of every new card were compared with EN by script; all EN exclusions are retained, and the
  RU-added ones are classified below. The EN links missing in RU are exactly those whose RU targets do not exist (kanji
  臣, 領 and 境, word 代表), each left as plain text; there is no Russian-only link.
- The 21 navigation files contain exactly 35 added links (告, 報, 夫, 婦 and 球 three each; 城, 域, 塔 and 首相 two each; the
  other twelve files one each). Removing their markup restores the parent text of every file, and 発表 keeps EN's
  `../words/` path form. The manifest recomputed in memory equals the committed file, and the 51 intake paths equal the
  content diff with matching candidate hashes.
- Every exact title segment shared between a new card and an existing RU card is guarded (большинство, большая часть,
  огромный, снимать, вечер, отчёт, провинция; «основываться на» in よる and 基づく is covered by the EN pair 基づく→よる).
  Pairs checked and judged not to need a guard include 夫人/婦人, 大臣/首相, 大会 against 会議, 試合 and 競技, 夜中/夜, 夜明け/朝,
  外す/脱ぐ, 地方/田舎, 頼る/よる, 大戦/戦い and 大家 against 借りる and 貸す.
- Optional: further title overlaps that mirror EN, with no required action: 地球 «планета Земля» vs 地 «земля; местность»,
  地域 «округа» vs 近所 «окрестности», and 報告 «сообщение» vs 教える «…; сообщать».
- Limits: 38 pre-existing EN-link differences in older cards outside the diff (for example 入口/出口, 理解, 国内 and many
  kanji cards) were seen but not evaluated; none targets a word in this batch.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (地方, 大統領, 大部分); scoped coverage **NEEDS FIX** (大部分). The other 27 cards
are clean on both facets. C1–C3 are the report's labels.

- C1 (minor, high confidence), `地方.md:35`: the closing sentence «Это слово не значит «побережье»…» adjudicates an
  English word-list gloss that a Russian learner has no reason to attach to ちほう, and its denial is too absolute because
  JMdict gives "coast" to the separate reading じかた. Remedy: delete the sentence; keep the 都会 and 東北地方 sentences and
  add no じかた lesson.
- C2 (minor, high confidence), `大統領.md:32`: «похожее на «шеф!» или «молодчина!»» teaches the familiar vocative as
  praise; «молодчина!» means "well done", not a form of address. Evidence: JMdict 1414650 sense 2 "big man; boss; buddy;
  mate", familiar, used vocatively, especially of an actor. Remedy proposed: «…особенно к актёру: вроде «шеф!» или
  «дружище!», а не похвала вроде «молодец!».»
- C3 (minor; high confidence), `大部分.md:27–29`: the card contrasts 大半 and 全部 but not ほとんど, although the titles share
  «большая часть» and ほとんど's negative use is «почти не»; a learner could treat 大部分 as that word. Evidence: JMdict
  1414850 大部分 "most part; greater part; majority" only; JMdict ほとんど adverb "almost; nearly" and, with a negative,
  "hardly". Remedy proposed: a linked ほとんど sentence naming the title overlap and the «почти»/«почти не» uses.

Optional notes: the provenance sentence in `よる.md:26`; 夢中/熱中 without an explicit contrast; 基づく/よる sharing
«основываться»; 報告/レポート sharing «отчёт»; the weaker «после войны» gloss in 大戦, repaired by the next sentence; «Мой»
in 売れる, inherited from EN; the unnamed たいか/たいけ reading behind 大家's «не «богатая семья»»; and the bookish «округа»
in 地域's title. The reviewer marked all of them polish, not defects.

## Exclusion classification

All EN exclusion entries are retained. At the candidate, 14 direct, one-sided entries were added on nine new cards. The
author report announced "15 direct pairs" (5 required, 10 conservative) but listed 14 (5 required, 9 conservative); the
list, not the count, matches the files. The consistency reviewer classified all 14 and found none unjustified:

| Entry | Author | Consistency reviewer |
|---|---|---|
| 大部分→ほとんど | required | required (shared «большая часть») |
| 大部分→たいてい | conservative | required (shared «большинство») |
| 大半→ほとんど | required | required |
| 大半→たいてい | conservative | required (shared «большинство») |
| 大→莫大 | conservative | required (shared «огромный») |
| 大→大小 | conservative | required |
| 夢中→熱中 | required | required |
| 外す→下ろす | conservative | required (shared «снимать») |
| 境→瞬間 | conservative | conservative (shared word «момент» only) |
| 報告→リポート | conservative | required (shared «отчёт») |
| 報告→知らせる | conservative | conservative |
| 報告→伝える | conservative | conservative |
| よる→次第 | required | required |
| 地方→州 | required | required (shared «провинция») |

The 大部分→たいてい, 大半→たいてい and 報告→リポート entries became exact-segment pairs with the coordinator's retitles. The
correctness reviewer read the guard targets in full as comparisons without auditing quiz safety exhaustively; the
comprehensibility reviewer did not score them.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`213-words-batch-52-recheck-001.md`.
