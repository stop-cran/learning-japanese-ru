# Batch 191 — independent review 001

## Snapshot and scope

- Reviewed commit: `20834c891a290fd011cbc3ce5b4940d5d1f5f5be` (tree `09404a2d88294118352e760242feb2a6ff59de3e`), branch `full-ru-191-words-30`, parent `45f316f`.
- Signing note: GPG signing timed out when the candidate was first committed, so the reviews ran on the local unsigned commit `20834c8`.
  Once signing recovered, the identical tree was committed signed as `3109d3d20ad14c3bd1453458a5e20133a3172b87` with the same parent, and the branch was reset to it.
  `20834c8` was never pushed. The equality of the two trees was checked with `git rev-parse` before the rechecks, and every recheck reviewer verified it again.
- Published baseline recorded in the intake: `6aff607` (B190 merge). Parent `45f316f` adds only the B190 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness and consistency also inspected the twelve navigation-only files.
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
  - `191-words-batch-30-review-correctness-001.md`
  - `191-words-batch-30-review-consistency-001.md`
  - `191-words-batch-30-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the title-screen output or one another's reports.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (`負け` only); scoped coverage **CLEAN**.

- C191-1 (minor, high confidence): `負け.md:34–35` added «но звучит книжнее» for 敗北, a comparative register claim that frozen EN does not make.
  The inspected JMdict, Jisho and Digital Daijisen entries confirm the meaning and the する construction, but not the comparison.
- All 30 lexical entries were read from Jisho/JMdict, and Digital Daijisen was inspected for 越す.

### Consistency and quiz safety

Verdict: consistency and integration **CLEAN**; quiz safety **NEEDS FIX**.

- F1 (minor, medium confidence): `越す` lacked a direct guard against 過ぎる «проходить; миновать».
  越す teaches passing time (年を越す), and its sibling 越える already guards 過ぎる.
- F2 (minor, medium-low confidence): `貴重` «ценный; драгоценный» lacked a guard against 高価 «дорогостоящий; высокой цены».
- Optional, not established as necessary: 渡す guards on 与える/贈る; 恩–おかげ.
  - The reviewer also left the English meta remarks in 越す/販売/貢献 to the comprehensibility facet.
- The reviewer independently checked the validator, link parity, manifest hashes and intake hashes.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (`越す`, `販売`, `貢献`, `負け`); coverage **NEEDS FIX** (`働き`).

- C1 (minor): `越す` told the learner to disregard an English "go over" gloss.
- C2 (minor): `販売` opened with the English word "sale".
- C3 (minor): `貢献` had an aside about English "services" and «заслуги».
- C4 (minor): `負け` rendered 今回は私の負けです with the past-tense «я проиграл», then said the example uses no past-tense verb.
- C5 (minor): `働き`'s title lead «труд» is the entire title of 労働, and the card did not contrast the two words.
- Optional items:
  - 資本:41 and 与える:17 wording;
  - a 賢い→利口 back-pointer;
  - 質 «характер вещи»;
  - 係 «ведение» → «поручение»;
  - 越す's honorific sense 6.

No finding established a missing requested card, a lost EN teaching point or a necessary prerequisite omission.
Optional suggestions are kept in the complete reviewer reports rather than promoted to defects.

## Exclusion classification: author and consistency reviewer

The author added 17 direct, one-sided exclusion pairs beyond EN. The author report and the blind consistency reviewer classified them independently.
The differences are preserved here rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `越す`→`移る` | conservative | required («переезжать» sense taught in the body) |
| `恩`→`御礼` | conservative | required (shared «благодарность» meaning) |
| `係`→`責任` | conservative | required (shared stem «ответствен-») |
| `貸し`→`貸す` | required | conservative |
| `働き`→`運転` | required | conservative |
| `負け`→`負ける` | required | conservative |

Both classify the remaining 11 pairs the same way:
- required: `身体`→`生物`; `越す`→`引っ越す`; `与える`→`くれる`/`くださる`; `贈る`→`あげる`/`差し上げる`; `働き`→`労働`; `責任`→`担当`; `販売`→`売る`;
- conservative: `贈る`→`上げる`; `働き`→`動く`.

Both count 12 required and 5 conservative, but the sets differ by the six pairs above.
The reviewer judged no added entry unjustified.
The two guards added after review, `越す`→`過ぎる` and `貴重`→`高価`, are recorded in the recheck record.

Reconciliation, the coordinator's dispositions and the final verdicts are in `191-words-batch-30-recheck-001.md`.
