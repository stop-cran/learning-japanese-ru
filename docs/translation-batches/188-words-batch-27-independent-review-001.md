# Batch 188 — independent review 001

## Snapshot and scope

- RU candidate commit: `c721e1cb63f33938081927e236dc7f9674f073b6` (tree `b355d4c7005159e48aa02d1ed71aec0b60529078`), branch `full-ru-188-words-27`, parent `ef4553a`.
- Published baseline recorded in the intake: `6722867` (B187 merge); parent `ef4553a` adds only the B187 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards. Consistency additionally covered the nine navigation-only files, `manifest.json` and the intake.
- Reviewers were assigned three distinct model families: correctness — `gpt-6.1-sol`; consistency/quiz safety — `claude-sonnet-5.5`; comprehensibility — `grok-4.7`. The runtime agent listing exposed these assigned model variants; reviewer prose did not expose a lower-level serving identifier.
- Full blind reports: `188-words-batch-27-review-correctness-001.md`, `188-words-batch-27-review-consistency-001.md` and `188-words-batch-27-review-comprehensibility-001.md`.
- Initial reviewers did not read the author report, the author prompt, the title-screen output or one another's reports.
- Before review, the coordinator replaced English comparison terms in five cards (`違いない`, `連想`, `連れ`, `速度`, `通行`) with Russian wording. That correction is included in the reviewed commit.

## Initial verdicts and findings

| Reviewer facet | Verdict | Findings |
|---|---|---|
| Correctness and scoped coverage | Correctness **NEEDS FIX**; coverage **CLEAN**; comprehensibility **UNVERIFIED** | F1 (minor, high confidence): `週間.md:40–41` glossed 毎週 as «раз в неделю», although it means every week. |
| Consistency and quiz safety | Facet **NEEDS-CHANGES**; coverage **NEEDS-CHANGES** | Medium: M1 luck-group guards, M2 `違いない`–`確か`, M3 `遅刻`–`遅れる`, M4 `連想` vs «связь» words, M5 `連続`–`次々`/`連休`, M6 `伸びる` and `進歩`–`発展`, M7 `進める` title/H1 mismatch, M8 missing progress/tracking records. Low: L1 weaker label overlaps, L2 seven cards without a word-type tag (inherited from EN), L3 five kanji without RU cards. The report assumed that exclusions must be declared on both sides. |
| Comprehensibility and scoped coverage | Comprehensibility **NEEDS FIX**; coverage **NEEDS FIX** | 1: identical `運`/`幸運` glosses; 2: `進める` H1 «продолжать дело»; 3: circular ban in `進める.md:42–43`; 4: «проверки» overlap between `通過` and `合格` (coverage); 5 (low): English «way» in `道路.md:38`. |

No finding established a missing requested card or a necessary prerequisite omission.
Optional suggestions and unverified facets are kept in the complete reviewer reports rather than promoted to defects.
Reconciliation, the later quiz-pair findings and the final verdicts are in `188-words-batch-27-recheck-001.md`.
