# Batch 216 — independent review 001

## Snapshot and scope

- Reviewed commit: `034ab7ea9034db0f24f7d8dfdad1f16af819e788` (tree `ca36d09f0ff3b18b6aa66d1ac4e8f2fbcf82f41c`), branch
  `full-ru-216-words-55`, parent `f5a6403`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 215 candidate `2ae93fbb0633b03857d1ae4bade78a29dccba880`.
    Before copying, the coordinator checked two things: that the 23 navigation files were unchanged between `2ae93fb` and
    the candidate's parent `f5a6403`, and that none of the 30 new cards existed there. The Batch 215 fix touched only
    共同, 化粧, 単に and 博士, none of which is in this batch's path set.
  - The coordinator byte-compared all 53 scratch content files with the primary checkout twice: after copying and again
    at commit time. Its byte scan found no BOM or CR, and every file ends with a newline, as `.gitattributes` requires.
  - No held wraps were carried into this batch.
  - The coordinator made no content change before the candidate.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 23 files with 37 restored navigation links;
    - `manifest.json` (`contentVersion` `b3cc2ebec3dd0f16`, 4,599 entries);
    - the intake.
- Published baseline recorded in the intake: `2721d15954814a731eaa60f6b47a671f58f82b28` (Batch 215 merge). Parent
  `f5a6403` adds only the Batch 215 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK;
  - content budget: OK, 4,616 entries / 13.05 MB;
  - navigation-only check: 23 files and 37 links, with no problem;
  - title screen: no unguarded exact title-segment overlap.
- Common sample: all three reviewers read all 30 new word cards in full.
  - Correctness and comprehensibility read each card against its full EN original.
  - Consistency compared each card's front matter, link targets and exclusions with EN.
- Correctness review scope:
  - Read in full the three binding RU instruction and format files.
  - Checked the title and exclusion fields of the comparison cards. It read 負ける, 譲る, 加える, 足す, 特に, 番, 別 and 機関
    in full.
  - Checked the link-only diffs of the existing cards.
  - Read the JMdict-backed Jisho API records for all 30 headwords, for what it reports as 21 comparison words of the
    RU-introduced guards, and for 検査 and 血液検査.
  - Mechanically confirmed all 63 bullet examples, with their full kana lines, verbatim against EN.
  - Japanese sources: Digital Daijisen 加わる on Weblio (senses 3–4: 暑さが加わる, 圧力が加わる) and Digital Daijisen 度 on
    Kotobank (ド sense 2 lists 制度).
  - Gramota entries (Kuznetsov, and Babenko where cited):
    - театр (senses 1 and 3), играть (2–4), драма (Babenko, 2);
    - очередь (1–2), анализ (3, the medical subsense), сыщик (2), жать (the second homonym);
    - уступить (4), делить (4, arithmetic), поезд (1), область (5), особый/особо, кончиться (2);
    - часть (2), польза, интерес (5), учредить (2);
    - рекомендовать, советовать, предлагать, действовать, добавлять, присоединяться, рвать and полицейский.
  - Russian Wiktionary: острота́ sense 1 (the sharpness of a blade). It did not use the separate entry остро́та (a joke)
    as evidence.
  - It ran no validator or generator and delegated nothing.
- Consistency review scope:
  - Read all 30 cards and all 23 navigation diffs in full. Programmatically, it stripped the link syntax from the old and
    new text of every navigation file and found them identical. It also compared the per-target link counts with EN.
  - Rebuilt the manifest in memory with `build_manifest.build_manifest` and found it identical to the committed file
    (`contentVersion` `b3cc2ebec3dd0f16`). It did not run the generator's writer.
  - Checked that the intake's 53 payload paths equal the 53 `words/` and `kanji/` paths in the content diff, and that
    every `candidateRawSha256` equals the manifest hash.
  - Ran `tools/validate.py` (0 errors), `tools/check_content_budget.py` (4,616 entries / 13.05 MB), `link_parity.py` and
    `word_title_screen.py`.
  - Confirmed that these targets are absent: `kanji/詞.md`, `kanji/損.md`, and the words 優れる, ドラマ, 出会い, 薦める,
    利く, 探偵, 体制, 行列 and 分かれる.
  - Importing `build_manifest` created an untracked `tools/__pycache__`. The reviewer deleted it itself and reported the
    tree clean again.
  - Classified every RU-added exclusion from the RU titles and JMdict senses, from its own knowledge of JMdict and the
    senses cited on the cards. It did not re-fetch the entries.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN.
  - Read the comparison cards 電車, 手伝い and 地方, and the title lines of the named near-synonyms.
  - Read JMdict entries on Jisho; JMdictDB itself required a password. Used Gramota and Kuznetsov for «электричка».
  - Ran `link_parity.py` on the 30 cards. It used the title-screen stem hits only as leads.
  - Did not review the kanji edits or the reciprocal edits to existing cards. It reports no validator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier.
- Reviews ran serially, one reviewer at a time. Before each review the coordinator checked that HEAD was still `034ab7e`
  and that `git status --porcelain --ignored` was empty. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator. They named the report as the only
  file a reviewer writes. The correctness report states that no validator or generator was run.
- Full blind reports:
  - `216-words-batch-55-review-correctness-001.md`
  - `216-words-batch-55-review-consistency-001.md`
  - `216-words-batch-55-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch worktrees;
  - one another's reports.

  The correctness report confirms that it read no author, reviewer, batch, tracking or draft material or scratch
  worktree. The consistency report confirms that it read no batch record, ledger, progress, author report or reviewer
  report. The comprehensibility report does not restate the rules.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **CLEAN**; scoped coverage **CLEAN**, for all 30 cards. No findings.

What the reviewer confirmed:
- All 63 bullet examples and their kana lines match EN verbatim. It found no wrong polarity, argument role, event stage
  or obligatory-gender rule. Masculine first-person past forms in Russian are contextual renderings, not a claim that
  the speaker must be male.
- The fields word, reading, jlpt, type, kanji and tags match EN, and every EN exclusion is retained.
- Every EN external URL remains. No EN relative link whose RU target exists was dropped, and the 30 cards contain no
  broken relative link. Missing RU targets stay plain text.
- The EN-only "tutor/spouse" gloss warning in 助手, the "(ordinary)" source wording in 列車 and EN's computer-file
  contrast were omitted without losing a Japanese rule.

Cited evidence supporting the Russian adaptations:
- 勧める and 効く: the Jisho records keep the sense-local spelling restrictions and support the 効く/利く spelling
  tendency.
- 分: Jisho separates ぶ and ぶん and supports the three measurement scales.
- 加わる: Digital Daijisen senses 3 and 4 give 暑さが加わる and 圧力が加わる.
- 制度: Digital Daijisen 度, ド sense 2, lists 制度 under the "standard, model" sense.
- 劇場 and 劇: «театр» covers both the art and the building (senses 1 and 3). «играть» covers games and sport,
  instruments and stage acting (senses 2–4). Babenko's «драма» sense 2 is the broad stage-work category.
- 列: «очередь» senses 1–2 separate a queue from someone's turn.
- 分析: «анализ» sense 3 has the medical subsense. Jisho 血液検査 means "blood test". The card says «обычно», not that a
  scientific analysis of blood can never be 分析.
- 刑事: «сыщик» sense 2 (an investigator).
- 刈る: the second homonym «жать» means reaping cereal crops, not harvesting in general.
- 切れ: Wiktionary острота́ sense 1, «острота ножа».
- 利益: JMdict sense 2 groups benefit, advantage, good and interests. The card keeps «чьи-либо интересы» and
  人の利益を守る, so the short title «выгода; польза» does not drop a taught sense.
- 前者: «первый из двух названных» keeps the first-mentioned reference, not precedence in time.

Optional: none.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; scoped coverage (cross-file integration) **CLEAN**; quiz safety **NEEDS FIX** (F1).

- All 23 navigation diffs only wrap existing text in links. The 37 restored links match the EN positions and counts
  exactly. `kanji/劇.md` links 劇場 twice and 劇 once, and leaves the mentions EN leaves unlinked as plain text.
- The fields word, reading, jlpt, type, kanji and tags equal EN, and every EN exclusion is retained.
- Links equal EN except where the target is absent in RU, and except for four RU-only links. The reviewer judged all
  four justified under the RU rule to link existing cards at a substantive introduction or comparison
  (content-structure line 42): 到着→着く (the card compares 着く), 分→部分 (it compares 部分), 分ける→分かる (it warns
  about the verb endings) and 列→順番 (it separates «чей-то черёд» from a row).
- It found no unlinked mention of an existing card substantive enough to need a link. 裁判, 事件, 特急, 暖房 and 圧力
  appear only incidentally inside examples.

Findings:
- F1 (minor; medium-low confidence), `切れる.md:10`. 切れる's displayed sense «кончаться (о запасе)» (the card's
  電池が切れました and 期限が切れる) is a near-synonym of 終わる «заканчиваться; заканчивать». The batch already guards
  切る→終わる and 無くなる→終わる. A learner could defensibly pick 終わる.
  - Remedy: add 終わる to `quiz_exclusions`.
  - The reviewer noted that 終わる normally cannot take a stock as its subject and that EN has no such guard, so
    reasonable people could leave it.
- F2 (trivial; medium confidence), `劇.md:10`: the 劇→劇場 entry is an over-guard. The card itself teaches that 劇 is
  not the building, and 劇場's title says «театр (здание)». The reviewer classed the entry unjustified but harmless, and
  did not ask for a blocking change. Remedy, for a strict reading: remove 劇場.

Limits it recorded, all outside this batch's diff:
- `kanji/割.md` has RU-only links to 割れる and 割合; they predate the batch.
- `words/損.md` lacks EN's link to `../kanji/損.md` because that kanji card is absent.
- EN links in other kanji files point to the absent words 刺さる, 刺す, 刺身, 名刺, 演劇, 効力, 勇ましい and 姿勢; they
  stay plain text.

### Comprehensibility and scoped coverage

Verdicts:
- Comprehensibility: **NEEDS FIX** (分, 刈る, 到着, 前者, 助手); the other 25 cards are clean in this facet.
- Scoped coverage: **NEEDS FIX** (助手); the other 29 cards are clean in this facet.

1. Minor (high confidence), `分.md:4,12`: the quiz title starts with «бу», a Cyrillic transliteration of the reading ぶ.
   A beginner may not map it to ぶ, and the same title also covers the different reading ぶん. The heading and body
   already show ぶ and ぶん. Remedy: title and H1 «дробная единица; чья-либо часть». Evidence: JMdict 1502850 (ぶ) and
   1502860 (ぶん), as cited on the card.
2. Minor (high confidence that the contrast is absent), `助手.md:34–36`: the card never separates 助手 from 手伝い,
   whose title «помощь; помощник» shares the gloss «помощник». Remedy: a contrast sentence after the 助ける sentence.
   Evidence: JMdict 1344650 助手 (assistant; helper; assistant to a professor) and 1328170 手伝い (helper; assistant;
   help; assistance).
3. Minor (high confidence), `到着.md:21` and `前者.md:18`: both translations gloss 電車 as «электричка», which in
   ordinary Russian is a suburban or short-distance electric train. The existing 電車 card is titled «электропоезд» and
   says its contrast with 列車 is not suburban against long-distance. Remedy: «электропоезд», with «первый» agreeing in
   前者. Evidence: JMdict 1443530 電車 sense 1; Kuznetsov «электричка» (colloquial, typically suburban);
   `電車.md:16,34`.
4. Minor (high confidence), `刈る.md:36–37`: «не представляет стрижку именно как срезание коротко» is a calque of the EN
   sentence and does not show how 髪を切る differs from 刈る. Remedy: a sentence presenting 髪を切る as the ordinary
   «подстричь волосы». Evidence: JMdict 1209540 刈る sense 1 includes cutting hair, so the point is framing, not a ban.

Optional notes:
- 分野 already blocks 地方's geographic «область»; an explicit 地方 sentence would only make the false friend unmistakable.
- 前者's «два предложения» for 案 could be read as grammatical sentences; «два варианта» would be clearer.
- 割る's «вылейте его в миску» is freer than 入れる; «положите в миску» is closer.
- 別に does not contrast あまり, and 列車's hedge that 汽車 also names other trains is vaguer than 電車's. The reviewer
  judged both uses already taught.

The reviewer judged that none of these is an actionable defect. It treated the Weblio and Daijisen footers on 加わる
and 制度 as translated source citations parallel to EN, and the schematic N, A, B, X and Y and the term «い-прилагательное»
as consistent with existing RU cards. It did not turn the title-screen stem hits that the cards already qualify into
findings: очередь/順番, анализ/検査, драма, острота, жать, детектив and сила движения.

## Exclusion classification

All 13 EN exclusion entries (11 lists) are retained. At the candidate, 24 direct, one-sided entries were added on 15 new
cards. The author and the consistency reviewer classified them as follows:

| Entry | Author | Consistency reviewer |
|---|---|---|
| 勧める→推薦 | conservative | conservative (verb against noun) |
| 勧める→提案 | conservative | conservative |
| 効く→効果 | conservative | conservative (verb against noun; shared stem «эффект») |
| 劣る→負ける | required | required (shared «уступать»; 負ける "to be inferior to") |
| 劣る→譲る | conservative | conservative (shared string «уступать» only) |
| 加わる→加える | required | required (intransitive/transitive pair) |
| 加わる→足す | conservative | conservative |
| 劇→芝居 | required | required (both "play; drama") |
| 劇→公演 | conservative | conservative |
| 劇→劇場 | conservative | unjustified, harmless (F2) |
| 割る→分ける | required | required (division sense) |
| 制度→機関 | conservative | conservative |
| 到着→着く | conservative to required | required |
| 別れ→別れる | conservative | required (the 勝ち/勝つ precedent) |
| 別に→あまり | required | required |
| 別に→特に | conservative | conservative |
| 別に→別 | required | required |
| 列車→汽車 | conservative | conservative |
| 列→順番 | required | required (shared «очередь») |
| 列→番 | required | required (shared «очередь») |
| 刑事→警官 | conservative | conservative (hypernym) |
| 切れる→切る | conservative | required |
| 切れる→破る | conservative | conservative |
| 分析→検査 | required | required (検査's title includes «анализ») |

The author classes are taken from the author's per-row table. Its summary totals omitted 劇→芝居 and 分析→検査, which
its table marks required. The fix removed 劇→劇場 and added 切れる→終わる (F1). The correctness reviewer inspected the
JMdict records of the 21 guard comparison words it reports, without auditing quiz safety exhaustively. The comprehensibility reviewer did
not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`216-words-batch-55-recheck-001.md`.
