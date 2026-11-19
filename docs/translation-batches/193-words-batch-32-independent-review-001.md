# Batch 193 — independent review 001

## Snapshot and scope

- Reviewed commit: `8fd47e7ccd776202db66e8f088d806a7693c02ac` (tree `a970b95cf288742a0ad921983505596e806124c4`), branch `full-ru-193-words-32`, parent `58c84bc`.
  The candidate was committed signed directly and pushed before review.
- Published baseline recorded in the intake: `3a0c79f` (B192 merge). Parent `58c84bc` adds only the B192 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness and consistency also inspected the twelve navigation-only files.
  - Consistency additionally covered `manifest.json` and the intake.
  - Comprehensibility also read the learner-facing link glosses in the twelve navigation-only files.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD and the working tree were unchanged.
- Full blind reports:
  - `193-words-batch-32-review-correctness-001.md`
  - `193-words-batch-32-review-consistency-001.md`
  - `193-words-batch-32-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the title-screen output or one another's reports.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN**; scoped coverage **CLEAN** across all 30 cards. No findings and no optional items.

- All 30 headwords were read from the Jisho/JMdict API, checking spelling, reading, sense, part of speech, restrictions and notes.
  The reviewer confirmed, among others, that 詰める keeps its transitive/intransitive allowance, that 触れる keeps the
  ～に手を触れる restriction, and that 評価 keeps both neutral assessment and positive recognition.
- The Russian-specific comparisons in 話題 and 記入 were checked against Gramota entries (Kuznetsov: тема, записаться).
- Every removed EN link was checked against its RU-relative target; all such targets are absent from the bounded RU tree.

### Consistency and quiz safety

Verdict: consistency **NEEDS FIX** (F1 only); quiz safety **NEEDS FIX** (F2, F3); scoped cross-file integration **CLEAN**.

- F1 (minor, high confidence): the first 訓 example rendered the reading of 山 as Cyrillic «яма», which is also the ordinary
  Russian word for "pit"; EN gives plain やま and RU cards keep readings in kana.
- F2 (minor, medium confidence): 訪問 «визит; посещение» lacked a direct guard against お見舞い «посещение больного; выражение
  сочувствия»; the titles share «посещение», and お見舞い already guards 訪ねる and 伺う.
- F3 (minor, medium-low confidence): 判断 lacked a guard against 読み «чтение; оценка ситуации», although the batch guards
  評価→読み and EN guards 解釈→読み for the same overlap.
- Optional: 判断/決定 and 検査/調べる remain unguarded (different titles, no EN pair); 診察→受付 could be dropped as lexical-only.
- The reviewer ran the validator, recomputed all 42 intake payload hashes, checked EN link parity over all 42 files
  (0 lost, 0 extra) and found no remaining unrestored EN link to the 30 new targets. Its dictionary sense wording is
  self-declared as recalled rather than re-fetched.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (`記事` only); scoped coverage **CLEAN**.

- C1 (minor, high confidence): `記事.md:39–40` explained the word through the English letters a and the
  («как английские a и the»). An English-free beginner cannot use that contrast, and Russian «статья» does not mean the
  grammatical «артикль».
- Optional items:
  - 試し:19 «Я попробовал этим приложением воспользоваться, чтобы посмотреть, какое оно» is stiff;
  - 証明:23 points at the こと/わけ topic, which is not in the RU tree;
  - 判断 could name 評価 explicitly;
  - the 検査 title «осмотр; анализ» is narrower than its body;
  - 記念 «ознаменование» is bookish;
  - 触れる uses voice terminology.
- The reviewer read the JMdict 記事 entry (1223240); JMdictDB required a password for other entries, so those were
  checked against the frozen EN cards.

No finding established a missing requested card, a lost EN teaching point or a necessary prerequisite omission.
Optional suggestions are kept in the complete reviewer reports rather than promoted to defects.

## Exclusion classification: author and consistency reviewer

The author added 19 direct, one-sided exclusion pairs beyond EN on 15 new cards. The author report and the blind
consistency reviewer classified them independently. The differences are preserved here rather than resolved by vote.
Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `許す`→`許可` | conservative | required (permission sense) |
| `認める`→`許可` | conservative | required (body teaches «разрешила») |
| `評価`→`読み` | conservative | required (shared «оценка»; mirrors EN 解釈→読み) |
| `訪問`→`訪ねる` | conservative | required (shared «посещать/посещение») |
| `訪問`→`伺う` | conservative | required (shared «посещать/посещение») |
| `訓`→`読み` | conservative | required (読み's kanji-reading sense) |
| `討つ`→`勝つ` | conservative | required (overcome an enemy) |
| `触れる`→`関する` | conservative | required (shared «касаться») |
| `検査`→`テスト` | conservative | required-ish (shared «проверка») |
| `記憶`→`覚える` | conservative | conservative-to-required («помнить») |

Both classify the remaining 9 pairs the same way:
- required: `認める`→`承認`;
- conservative: `生まれ`→`生まれる`, `誕生`→`生まれる`, `試し`→`試験`, `検査`→`調査`, `診察`→`受付`, `設計`→`案`,
  `記憶`→`思い出す` and `記念`→`記憶`. The reviewer leans towards calling 診察→受付 and 記憶→思い出す unjustified but harmless.

The author counts 1 required and 18 conservative; the reviewer counts 9 required, 1 required-ish,
1 conservative-to-required and 8 conservative.
The reviewer judged no added entry to block a distinction the cards teach.
The two guards added after review are recorded in the recheck record.

Reconciliation, the coordinator's dispositions and the final verdicts are in `193-words-batch-32-recheck-001.md`.
