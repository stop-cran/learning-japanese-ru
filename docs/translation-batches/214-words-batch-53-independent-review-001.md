# Batch 214 — independent review 001

## Snapshot and scope

- Reviewed commit: `a371c734a15f44e674e87a3a9ea0c9f147961d90` (tree `6712ca2c3fe82adc1a20a1e86be3a7a58861d70a`), branch
  `full-ru-214-words-53`, parent `0138d32`. The candidate was committed signed directly and pushed before review.
  - The content was authored in a scratch worktree on the Batch 213 candidate `3c8461447a0a88352701ecb3fc7183b5c545a07b`.
    Before copying, the coordinator checked that the 15 navigation files were unchanged between `3c84614` and the
    candidate's parent `0138d32`, and that none of the 30 new cards existed there; after copying, it byte-compared all 45
    scratch content files between the scratch worktree and the primary checkout. No held wraps were carried into this
    batch.
  - The coordinator made no content change before the candidate. The author had already retitled its own 地区 draft from
    «участок территории; зона» to «округ; выделенная зона», because «участок» collided with 土地, 所 and 担当.
  - The candidate differs from the published baseline by 30 new word cards, 15 files with 22 restored navigation links,
    `manifest.json` (`contentVersion` `d495e3ffa0bf3285`, 4,534 entries) and the intake.
- Published baseline recorded in the intake: `3febe87a2674a5c5793e5a29d5e7dd1614345f18` (Batch 213 merge). Parent `0138d32`
  adds only the Batch 213 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers. Correctness and comprehensibility read each
  card against its full EN original; consistency read each card against EN and compared front matter and links by script.
  - Correctness also read the three binding RU instruction and format files in full, the comparison cards 地域, 地方,
    お土産, 土曜日, 祝い, 科目, 道徳, 貿易, 店員, 熱中, 夢中 and 言う in full, the titles of the other suggested comparison
    cards, and the changed hunks of the five kanji and ten word files in the navigation diff. It inspected all 30
    headwords through the JMdict-backed Jisho API, keeping distinct readings and entries apart; Daijisen 地区 (Weblio) and
    国語 (Kotobank); and Gramota dictionary entries (including Kuznetsov and Babenko) for округ, район, горизонт,
    граница, гостинец, сувенир, коммерция, купец, иллюстрация, обносить, ловкий, добро, хороший, единственный,
    уникальный, дыхание, друг, окружающий, впитать, суммировать, держать, опровержение, напротив, вращать, вращаться,
    извергать, извергнуть and изрыгать, plus a dictionary search for периметр. Initial Gramota searches returned
    HTTP 429; the direct entries were then read. One wrong numeric Kotobank
    URL redirected to an unrelated entry and was discarded. It ran `tools/validate.py` (0 errors).
  - Consistency read all 30 cards and all 15 navigation diffs in full against EN, ran `link_parity.py` on the 30 cards
    (clean), checked the SHA-256 of all 45 changed kanji and word files against `manifest.json` (no mismatch; every
    manifest path exists) and checked that the intake path list equals the diff. It classified every RU-added exclusion
    from the RU titles and card senses; dictionary entries were not re-fetched. A broad RU-title stem screen was aborted
    as too slow, so remaining pair candidates came from `word_title_screen.py` leads and the comparison cards' headings.
  - Comprehensibility read the 30 cards in full against EN and read parts of 息, 環境, 周り, 回り, 境 and コーヒー, and the
    titles of the named near-synonyms, as contrast evidence only. It cited Jisho/JMdict entries for 味方, 回り, 周り and
    国境, entry 1404320 for the breath gloss in 呼吸, and a kousei.club usage note on 周り/回り. It ran no validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD was still `a371c73`
  and that `git status --porcelain --ignored` was empty. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator and named the report as the only file a
  reviewer writes. The correctness and comprehensibility reports state that no generator was run; the consistency report
  states it in its recheck section.
- Full blind reports:
  - `214-words-batch-53-review-correctness-001.md`
  - `214-words-batch-53-review-consistency-001.md`
  - `214-words-batch-53-review-comprehensibility-001.md`
- Initial reviewers were told not to read the author report or prompt, the coordinator's title-screen output or notes, the
  batch records, or one another's reports; the correctness report confirms that no author or reviewer report, batch
  record, translation draft or scratch worktree was read.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (地区); the other 29 cards **CLEAN**. Scoped coverage **CLEAN** for all 30 cards.

- C1 (minor; high confidence on the lexical scope, medium-high on the learning impact), `地区.md:4,12`: the title
  «округ; выделенная зона» makes both alternatives sound like specially constituted territorial units, while 地区 also
  names an ordinary local district; the body already translates its neighbourhood examples with «район». Evidence:
  Daijisen 地区 sense 1 «ある限られた範囲内の土地。地域。» against sense 2, an administratively designated area; JMdict/Jisho
  地区 sense 1 (district, area, zone, quarter, section, region); Kuznetsov «округ» (an administrative, political,
  military or economic subdivision of a state) and «район» sense 1 (including residential districts). Remedy:
  `title: район; выделенная зона` and the same H1 gloss, keeping the 地域/地方 exclusions and checking the new title
  against the live pool.

The reviewer confirmed that every card keeps EN's word, reading, jlpt, type, kanji, tags and exclusions; that all source
examples, sense explanations and citations are represented; that example tense, polarity, transitivity, role and event
stage match the Japanese; and that the Russian adaptations it checked (for example 地平線's land qualifier, 国境's broader
«граница», 土産's travel and visiting gifts, 国語's three Daijisen senses, 商人 «купец» not tied to the pre-1917 estate,
回す's bounded wheel contrast and 吐く's separate はく homophones) are supported by the cited entries. 吸収's removed
English source-gloss warning removes no Japanese intake rule.

Optional, outside its facets: a simpler ordinary vomiting gloss for 吐く, such as «рвать (о рвоте)», and a short
conversational-register note for «гостинец» in 土産. Neither was presented as a correctness defect.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **CLEAN**; scoped coverage (links, manifest, intake) **CLEAN**. No findings.

- Link restorations match EN's hrefs; the plain-text targets (kanji 線 and 境; words 水平線, 住民, ただ, 仲間, 加わる and
  肯定) are absent in RU. Front matter, type and kanji fields and all EN exclusions are preserved.
- RU-added exclusions were classified as shown below; none was judged unjustified enough to remove.
- Optional: O1 吸収→吸う («впитывание» against «всасывать»; low) and O2 味方/相手 («союзник» against «партнёр»;
  borderline). Neither is required.
- Limit noted outside the diff: RU `kanji/地.md` has an extra 地図 link compared with EN and leaves 土地 unlinked; this
  predates the batch.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (図, 国語, 囲む, 品, 味方, 呼吸, 周囲, 国境); scoped coverage **NEEDS FIX** (周囲;
呼吸 for the 息 contrast). The other cards are clean on each facet. The numbers below are the report's labels.

1. Minor, high, `図.md:16,18,21`: the glosses «рисунок» and «рисунок 1» repeat 絵's title «рисунок; картина», so the
   first example equates 図 with the word the synonym line separates. Remedy: «схема, чертёж или другое наглядное
   изображение», «на следующую схему» and «схема 1».
2. Minor, high, `国語.md:18,19,21`: the examples translate 国語 as «японский язык», the title of 日本語, after warning not to
   swap them. Remedy: school-subject renderings and «учебник по этому предмету».
3. Minor, high, `囲む.md:19`: «собралась за столом» means "at the table", not "around it", so what テーブルを marks is
   lost. Remedy: «Семья собралась вокруг стола и поужинала.»
4. Minor, high, `品.md:32`: «Метаданные карточки…» addresses card metadata rather than the learner. Remedy: name the
   heading's main reading しな and say that not every 品 is read that way.
5. Minor, high, `味方.md:28`: the ateji sentence is ungrammatical and names JMdict in the teaching text. Evidence: Jisho
   1527070 marks the ateji reading. Remedy: «Словарь помечает 味方 как атэдзи — кандзи, подобранные ради звучания.»
6. Minor (high that «дух» is unsupported; medium on the need for a one-breath contrast), `呼吸.md:29`: «дыхание, дух»
   reuses 息's title word and adds «дух», which a beginner can read as "spirit"; JMdict 1404320 gives breath and
   breathing, concord and steam, not spirit. Remedy proposed: air of breathing, plus a 一息 one-breath sentence.
7. Moderate, high, `周囲.md:34`: the only near-synonym sentence says that 回り also denotes the space around, while the
   linked RU 回り card teaches rotation, a circuit or spreading and gives surroundings to 周り; 環境, which shares
   «окружение» in its title, is not mentioned. Evidence: Jisho 回り 2800530 and 周り 1604290; RU `回り.md:25,36–39`;
   `環境.md`. Remedy proposed: a three-way contrast with links to 周り, 回り and 環境.
8. Minor (high that the sentence is opaque; medium on the exact restriction), `国境.md:29`: «JMdict ограничивает это
   чтение записью 国境…» names neither the other reading nor spelling. Remedy: delete it, or name 国境【くにざかい】 and
   国界【くにざかい】 as Jisho shows.

Optional notes: a 商売 contrast with 営業 or 貿易; 含む contrasts 入れる but not 加える, as EN does, which the reviewer did not
require reopening; a smoother 哲学 的な line; and «респирация» in 呼吸 as unnecessary. Title-screen stem hits such as гостинец/гостиница, округ/округлый and
горизонт/горизонтали were judged false friends.

## Exclusion classification

All 28 EN exclusion entries (19 lists) are retained. At the candidate, seven direct, one-sided entries were added on seven
new cards. The consistency reviewer classified all seven and found none unjustified:

| Entry | Author | Consistency reviewer |
|---|---|---|
| 土曜→土曜日 | required | required (identical «суббота») |
| 土産→祝い | conservative | conservative or likely required (shared «подарок») |
| 商売→貿易 | required | likely required (shared «торговля») |
| 商人→店員 | conservative | conservative (Russian-only «торговец»/«продавец» closeness) |
| 国語→科目 | required | conservative |
| 善→道徳 | conservative | conservative, necessity unestablished |
| 吸収→夢中 | conservative | conservative, necessity unestablished (shared «поглощ-», different parts of speech) |

The three 地区 guards (町, 辺, 近所) were added in the fix for correctness C1 and classified in the consistency recheck.
The correctness reviewer read several guard targets in full as comparisons without auditing quiz safety exhaustively; the
comprehensibility reviewer did not score them.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fixes and the final verdicts are in
`214-words-batch-53-recheck-001.md`.
