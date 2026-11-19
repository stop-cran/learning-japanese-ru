# Batch 187 — independent review 001

## Snapshot and scope

- RU staged tree: `1597f0853220fbaeb521bab731c807b81e62373e`.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards; consistency additionally covered the 17 navigation-only files, manifest and intake.
- Reviewers were assigned three distinct model families: correctness — `gpt-6.1-sol`; consistency/quiz safety — `claude-sonnet-5.5`; comprehensibility — `grok-4.7`. The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Full blind reports: `187-words-batch-26-review-correctness-001.md`, `187-words-batch-26-review-consistency-001.md`, and `187-words-batch-26-review-comprehensibility-001.md`.
- Initial reviewers did not read the author report or one another's reports.

## Initial verdicts and findings

| Reviewer facet | Verdict | Findings |
|---|---|---|
| Correctness and scoped coverage | Correctness **NEEDS FIX**; coverage **CLEAN** | `集中.md:26–27` reverses the roles of を and に in 注意を一点に集中する. `際.md:46–49` overstates 来た際 as necessarily completed before speaking. Both P2, high confidence. |
| Consistency and quiz safety | Consistency **PASS**; quiz safety **PASS with advisory items** | Recommended a direct `度`–`機会` exclusion; noted `始まり`/`開始`–`出発` as possible conservative guards. |
| Comprehensibility and scoped coverage | Comprehensibility **NEEDS FIX**; coverage **CLEAN** | Repeated the 集中 particle issue; flagged `関する.md:23` («вопрос по этому вопросу») and `鍋.md:16,37` conflating 鍋 with a frying pan. |

No finding established a missing requested card or a necessary prerequisite omission. Optional suggestions and unverified facets are retained in the complete reviewer reports rather than promoted to defects.
