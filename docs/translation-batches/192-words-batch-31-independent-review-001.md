# Batch 192 — independent review 001

## Snapshot and scope

- Reviewed commit: `dc2c32f8ce8a1308980a4e2b9b85c21cb758b73b` (tree `694386eaa3f4a96a292adaa19ae9e771c2e736bb`), branch `full-ru-192-words-31`, parent `4d79f1f`.
  The candidate was committed signed directly and pushed before review.
- Published baseline recorded in the intake: `22c9038` (B191 merge). Parent `4d79f1f` adds only the B191 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness and consistency also inspected the thirteen navigation-only files.
  - Consistency additionally covered `manifest.json` and the intake.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD and the working tree were unchanged.
- Full blind reports:
  - `192-words-batch-31-review-correctness-001.md`
  - `192-words-batch-31-review-consistency-001.md`
  - `192-words-batch-31-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the title-screen output or one another's reports.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (`譲る` only); scoped coverage **CLEAN**.

- C192-01 (minor, high confidence in the overlapping senses): `譲る.md:44–45` added a Russian-only contrast presenting 負ける as defeat
  and 譲る as voluntary concession. 負ける also means to yield or give in and to reduce a price
  (JMdict senses 1, 2 and 5; 精選版 日本国語大辞典), so the contrast drew a false lexical boundary.
- All 30 headwords were read from Jisho/JMdict. The reviewer also inspected Kotobank entries for 負ける, 譲る and 谷,
  and Gramota (Krysin) for «спикер».

### Consistency and quiz safety

Verdict: consistency **NEEDS FIX** (C1 only); quiz safety **NEEDS FIX**; scoped cross-file coverage **CLEAN**.

- Q1 (moderate, high confidence): 招く and 誘う lacked direct guards against 呼ぶ, whose RU body teaches «приглашать»;
  the existing 招待→呼ぶ guard covers the same sense.
- Q2 (minor-moderate, medium-high confidence): 語る lacked 話す, whose RU body teaches «рассказывать».
- Q3 (minor-moderate, medium confidence): 議論 lacked 話し合う (the «обсуждение» overlap already guarded via 相談), and optionally 論じる.
- Q4 (minor, medium-low confidence each): noun/verb or generic-stem pairs with existing precedents —
  読み→読む, 調査→調べる, 説→説明, 語学→勉強.
- C1 (minor, medium confidence): `講演.md:37–38` and `招く.md:32–33` added learner-facing Russian-only sentences
  stating test behaviour («в тестах … не ставится рядом»), which can go stale when exclusions change.
- Optional: 議論's `../words/相談.md` href form differs from sibling cards.
- The reviewer independently ran the validator, link parity and all 43 intake payload hashes. It did not re-fetch JMdict pages,
  so the dictionary sense wording in its report is self-declared UNVERIFIED; quiz necessity was judged from RU titles and bodies.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (`読み` only); scoped coverage **CLEAN**.

- C1 (minor, high confidence): `読み.md:44–46` tied the pronunciation-versus-definition point to 読書, implying 読書 means
  «полное толкование знака»; its genitive gloss «чтения книг» also disagreed with the 読書 title.
- Optional items:
  - 調査:21 «обследование жизни студентов» is stiffer than «опрос»;
  - 講演:36–38 did not give the 演説 distinction;
  - 調子 title «состояние (форма)» could be read as shape;
  - 語 and 単語 reuse a similar example.
- The reviewer read the 読み, 読書 and 調査 dictionary entries and found no leftover learner-facing English gloss.

No finding established a missing requested card, a lost EN teaching point or a necessary prerequisite omission.
Optional suggestions are kept in the complete reviewer reports rather than promoted to defects.

## Exclusion classification: author and consistency reviewer

The author added 7 direct, one-sided exclusion pairs beyond EN. The author report and the blind consistency reviewer classified them independently.
The differences are preserved here rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `譲る`→`負ける` | conservative | required (shared title word «уступать») |
| `議論`→`相談` | conservative | required (shared «обсуждение» meaning) |
| `話し合う`→`相談` | conservative | required (same «обсуждение» stem) |
| `講演`→`スピーチ` | conservative | required (講演 body uses the スピーチ title wording) |
| `誘う`→`招待` | conservative | required-leaning (same «приглашать/приглашение» stem) |

Both classify the remaining 2 pairs the same way:
- required: `招く`→`招待`;
- conservative: `語る`→`話`.

The author counts 1 required and 6 conservative; the reviewer counts 5 required, 1 required-leaning and 1 conservative.
The reviewer judged no added entry unjustified.
The nine guards added after review are recorded in the recheck record.

Reconciliation, the coordinator's dispositions and the final verdicts are in `192-words-batch-31-recheck-001.md`.
