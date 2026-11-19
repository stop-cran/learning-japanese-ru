# Batch 189 — independent review 001

## Snapshot and scope

- RU candidate commit: `9251965ace4abea93cac73e84a2d32d76243abc5` (tree `6a7e3aff3e6da31527e2480e035cd9276878cde6`), branch `full-ru-189-words-28`, parent `6bd7b05`.
- Published baseline recorded in the intake: `a65f37f` (B188 merge); parent `6bd7b05` adds only the B188 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards. Consistency additionally covered the eight navigation-only files, `manifest.json` and the intake.
- Reviewers were assigned three distinct model families: correctness — `gpt-6.1-sol`; consistency/quiz safety — `claude-sonnet-5.5`; comprehensibility — `grok-4.7`. The runtime agent listing exposed these assigned model variants; reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time.
- Full blind reports: `189-words-batch-28-review-correctness-001.md`, `189-words-batch-28-review-consistency-001.md` and `189-words-batch-28-review-comprehensibility-001.md`.
- Initial reviewers did not read the author report, the author prompt, the title-screen output or one another's reports.

## Initial verdicts and findings

| Reviewer facet | Verdict | Findings |
|---|---|---|
| Correctness and scoped coverage | Correctness **NEEDS FIX** (`避ける` only); coverage **CLEAN** | C1 (minor, high confidence): `避ける.md:38–41` said the physical-contact sense is «закреплено за よける». JMdict's sense-local restrictions support that split within the entry, but デジタル大辞泉 gives さける sense 3 «よける» and a usage note on overlap for physical hazards. The wording was inherited from frozen EN `避ける.md:32`. Q1 (outside the facet): `鉄`–`鉄道` has no direct exclusion although JMdict 鉄 sense 4 is "railway" (Abbreviation). |
| Consistency and quiz safety | Consistency **CLEAN**; quiz safety **NEEDS FIX**; coverage **CLEAN** | F1 (minor, medium confidence): `鉄` and `銀` lacked `quiz_exclusions: [金属]`, although both bodies call the word a metal; the RU generic-label rule (`content-structure.instructions.md:160-161`, 車/電車) and the EN 金→金属 precedent apply. This is an inherited EN gap. Every one of the 23 RU-added exclusions had a stated basis; none was judged unjustified. |
| Comprehensibility and scoped coverage | Comprehensibility **NEEDS FIX** (`都市` only); coverage **NEEDS FIX** (`都市` only) | F1 (moderate, high confidence): `都市.md:3,7,11` glossed 都市 as «городской центр», which in Russian means the centre of a city (downtown); JMdict 1444990 sense 1 is "town; city; municipal; urban". The gloss also shared «центр» with 中央, 中心 and 真ん中. |

No finding established a missing requested card or a necessary prerequisite omission.
Optional suggestions are kept in the complete reviewer reports rather than promoted to defects.

## Exclusion classification: author and consistency reviewer

The author report and the blind consistency reviewer classified the 23 RU-added exclusion pairs independently. Both kept every pair;
the differences concern only whether a pair is required or conservative and are preserved here rather than resolved by vote.
Classification does not change runtime behaviour: every listed pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `銃`→`武器` | conservative | required (hypernym label; EN 矛–武器 precedent) |
| `重大`→`まじめ` | conservative | required (identical label word «серьёзный») |
| `適切`→`合う` | conservative | required |
| `金融`→`金銭` | required | conservative (borderline required) |
| `金融`→`お金`, `金融`→`金` | required | conservative |
| `金`→`経済`, `金銭`→`経済` | required | conservative |

The remaining 15 pairs are classified the same way by both:
- required: `金曜`→`金曜日`; `金融`→`経済`; `数`/`量`→`多少`; `野`→`畑`; `重大`→`大変`/`大した`; `便`/`郵便`→`郵便局`; `選択`→`選ぶ`; `適用`→`用`; `適切`→`適する`;
- conservative: `重大`→`相当`; `都市`→`町`; `適切`→`いい`.

Coordinator correction to the author report: its heading "Additional conservative guards (7)" lists six pairs.
The author's counts are 17 required and 6 conservative, 23 in total, which matches the reviewer's table.

Reconciliation, the coordinator's adjudication of Q1 and the final verdicts are in `189-words-batch-28-recheck-001.md`.
