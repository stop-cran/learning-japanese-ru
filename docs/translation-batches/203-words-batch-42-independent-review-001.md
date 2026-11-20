# Batch 203 — independent review 001

## Snapshot and scope

- Reviewed snapshot: candidate tree `d6e95d46124d66f60472825a8db483b5702688f7`, staged in a scratch worktree, not a commit.
  - Batches 197–202 had been reviewed and their fixes rechecked, but their signed commits could not yet be made because the
    signing key's passphrase cache had expired. Rather than wait, Batch 203 was authored on top of the reviewed Batch 202 tree
    `459ddeffdbb0a737d9bcc2062726e49627199462`, at detached HEAD `5dd9a78` in a separate worktree.
  - The candidate differs from `459ddef` by 44 paths: 30 new word cards, 13 navigation-only files (17 restored links) and
    `manifest.json`.
  - Reviewers were told to read the staged tree and not to rely on HEAD. No unsigned commit was made.
- After Batch 202 was published as `bbf0b2c9259d8fd4f9baa0f83df85314ebd7332f`, branch `full-ru-203-words-42` was cut from that merge. Its parent commit
  `e2f7f8a9e873b59b180fc74db3e49a228fc4af79` adds only the Batch 202 publication record. The final reviewed content tree was copied there and committed signed as
  `1f5e73c6f566d8364003e98a82bf4d8393f5c5aa`, together with the intake. `git diff 20d0232 1f5e73c -- words kanji strokes articles manifest.json` is empty;
  see the recheck record for the revised tree `20d0232`.
- Published baseline recorded in the intake: `bbf0b2c9259d8fd4f9baa0f83df85314ebd7332f` (Batch 202 merge).
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers.
  - Correctness read every new card and its EN original completely and inspected the link-only changes. It also read the RU
    cards 注意, 意思, 汚す, 残念, 好き, 布団, 正しい and お母さん in full as comparisons.
  - Consistency read the complete diffs of the 13 navigation-only files and of `manifest.json` in a single pass.
  - Comprehensibility read all 30 cards against their EN originals and used 注意, 意思, 残り, 道路 and 海岸 as comparison leads. It
    reviewed the 13 navigation restorations from their diffs.
  - The intake was generated after review from the same paths. Its payload hashes are checked by the final validation receipt.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that the worktree's index tree was
  still `d6e95d4`, that the working tree equalled the index and that nothing was untracked. No fix was applied until all three
  reports were complete.
- Full blind reports:
  - `203-words-batch-42-review-correctness-001.md`
  - `203-words-batch-42-review-consistency-001.md`
  - `203-words-batch-42-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt or one another's reports. The consistency reviewer ran its
  own title-overlap screen of the new titles against all RU word titles, and the comprehensibility reviewer ran the shared title
  screen; both treated hits as leads.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (毛布 only); scoped coverage **NEEDS FIX** (波 only). The other 29 cards were CLEAN on both
facets.

- C1 (minor, high confidence), `毛布.md:32`: «одеяло не надевают глаголом для одежды вроде 着る» turns EN's caution against
  translating every "put on" with a clothing verb into a categorical prohibition. JMdict also records 着る毛布（きるもうふ）,
  "wearable blanket". Evidence: frozen EN `毛布.md:44–47`; the JMdict-backed Jisho entries 着る and 着る毛布; Digital Daijisen
  着る, sense 1. Remedy (the reviewer's text): «Учите глаголы укрывания вместе с частицами: в приведённых ситуациях используются
  毛布をかける и 毛布をかぶる.»
- C2 (minor, high confidence), `波.md:30–32`: EN's contrast between the noun 波 and the gesture 手を振る（てをふる）was dropped
  together with the English-dependent "wave" wording. Removing the English wording is appropriate, but the Japanese expression and
  its rule are source teaching content. A string check found 手を振る/てをふる to be the only source Japanese run longer than two
  characters absent from the RU text. Evidence: the JMdict-backed Jisho entry 手を振る (てをふる, "to wave one's hand").

Other checks:

- All 59 main Japanese example sentences are retained exactly. Metadata other than localized titles and added exclusions match EN,
  and all EN exclusions and external citations are kept. Nineteen EN link occurrences stay plain because their RU targets do not
  exist.
- The reviewer inspected JMdict-backed Jisho entries for the headwords, Digital Daijisen 毒, 死亡, 歩道, 正確, 注意, 汚す, 残念,
  汗だく and 可哀想 (including its ateji note), the Digital Daijisen and Nihon Kokugo Daijiten 氏 entries, and Gramota/Kuznetsov
  «грязь» and «воля». These confirmed the author's two unverified notes on 泥 and 意志.
- `tools\validate.py` reported 0 errors.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (正確 only); scoped cross-file integration **CLEAN**.

- The validator reported 0 errors, and a regenerated manifest showed no difference. Front matter matches EN in all 30 cards apart
  from the localized titles and the added exclusions; every card has the four standard sections, and each H1 matches the
  `word（reading）— title` form. All EN exclusions are kept.
- Every RU link target is also an EN link target (no Russian-only link), and every EN link absent from RU has no RU target file.
  A reverse scan found that the 13 restored files are exactly the existing RU sources of EN links to the new words; every hunk
  changes only link brackets and targets.
- No new title equals an RU title or title segment. Only 母親/お母さん share «мать», and that pair is guarded in EN.

Finding:

- F1 (minor, medium confidence), `正確.md:9`: 正確 «точный; безошибочный» and 正しい «правильный; верный» are defensible
  answers for each other, and neither card declares the pair. The card itself lists 正しい as a partial synonym. Remedy: add
  正しい to `quiz_exclusions` and regenerate `manifest.json`.

Optional: 残す→残る as a transitive/intransitive guard; the reviewer judged 泥↔土, 沖↔海 and 正直↔まじめ not to need guards.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (気味 only); the other 29 cards and the navigation diffs **CLEAN**. Scoped coverage
**CLEAN**.

- C1 (minor, high confidence), `気味.md:34`: the «Оттенки значения» paragraph reads as an author note. «исходный список слов», the
  gloss and «не считается дополнительным словом уровня N3» refer to a list and a level assignment the learner never sees, instead of
  stating when to say きみ and when ぎみ. Remedy (the reviewer's text): open with the rule that the noun 気味 is read きみ and names
  the sensation (気味が悪い), while the suffix 〜気味 is read ぎみ and expresses a tendency or slight degree (疲れ気味).

Optional:

- `死亡.md:26`: «китайское сложение» is unexplained jargon; «само 死亡» would be plainer.
- `かわいそう.md:19`: «это будет несправедливо» is immediately qualified at line 21; «его жалко» would be closer.
- `気に入る.md:19`: «Мне очень нравится» adds a degree; «Мне нравится» is enough.

In its limits, the reviewer listed the English-only traps (posted «notice», season «spring», hand «wave», legal «will», Mr./Ms.) as
adapted or correctly dropped. That assessment of the hand wave differs from correctness C2; see the recheck record.

## Exclusion classification: author and consistency reviewer

The author added 8 direct, one-sided exclusion pairs beyond EN on 6 new cards, and review F1 added a ninth. All 17 EN exclusion
entries (11 lists) are retained. The author report and the blind consistency reviewer classified the pairs independently. The
differences are preserved here rather than resolved by vote. Classification does not change runtime behaviour, because every kept
pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `気に入る`→`好き` | required | required |
| `好む`→`好き` | conservative | required |
| `比較`→`比べる` | conservative | required |
| `気に入る`→`大好き` | required | conservative |
| `哀れ`→`残念` | required | conservative, leaning unjustified; harmless |
| `かわいそう`→`残念` | conservative | conservative |
| `正確`→`ちょうど` | conservative | conservative |
| `かわいそう`→`貧しい` | conservative | conservative, leaning unjustified; harmless |
| `正確`→`正しい` | considered and declined (glosses distinct; a linked contrast) | missing guard, finding F1 (medium confidence) |

Neither found a kept pair unjustified enough to remove, and no kept pair guards a contrast that a card teaches as an antonym. The
`正確`→`正しい` pair was added after review on F1.

Reconciliation, the coordinator's dispositions and the final verdicts are in `203-words-batch-42-recheck-001.md`.
