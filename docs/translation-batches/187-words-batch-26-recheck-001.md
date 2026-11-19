# Batch 187 — independent recheck 001

## Snapshots and reviewers

- Initial review: `1597f0853220fbaeb521bab731c807b81e62373e`.
- First fix recheck: `331d9e89d22d33492a460f74d4f12a5ea361a2fd`.
- Final quiz-guard recheck: `67ca03cbe945bec9fadb315345c71a54707b2483`.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Rechecks used the same assigned model variants and facets as review 001: `gpt-6.1-sol` correctness, `claude-sonnet-5.5` consistency/quiz safety, `grok-4.7` comprehensibility. The final bounded pair review was assigned `claude-sonnet-5.5` and assessed exact excerpts from the final tree. Model assignments are recorded from the task-runner settings/runtime listing; reviewer prose did not expose separate provider serving IDs.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| `集中` particle roles | **Resolved** | The card now says を marks what is concentrated (attention) and に marks the point of focus. Correctness recheck verified this against the transitive example and dictionary use. |
| `際` past-form timing claim | **Resolved** | The card now qualifies that た alone does not mean the event preceded speech time and gives a future-context 来た際 example with a teaching-source link. |
| `関する` translation «вопрос по этому вопросу» | **Resolved** | Revised to «У меня есть вопрос по этой проблеме». |
| `鍋` cookware/food distinction | **Resolved** | The article distinguishes a pot/saucepan from フライパン and keeps 鍋料理 as the food sense. |
| `度`–`機会` | **Resolved** | Added the direct pair to `度` exclusions. |
| `始まり`–`出発` and `開始`–`出発` | **Resolved** | Added direct exclusions to both new cards. |
| `回`/`度` against `一度`, `もう一度`, `今度` | **Resolved** | `回` excludes `一度` and `もう一度`; `度` excludes all three. The final pair review judged `回`–`今度` not directly ambiguous because a repetition counter differs from the deictic «этот/следующий раз» expression. |

### Additional review suggestions adjudicated

- Suggestions to add reverse exclusions for `誤り`–`間違い`, `集まり`–`会合`, `失敗`–`誤り`/`間違い`, `関心`–`興味`, `関連`–`関係`, `集団`–`団体`, `対する`–`関する`, `かぎり`–`限界`, and `始め`–`開始` were **withdrawn as redundant**. The current cards already declare these exact direct pairs on one side. The Android quiz implementation checks both directions (`Words.kt:178,200`), so the pairs cannot appear together; these are not transitive exclusions.
- Suggested reciprocal links from baseline kanji pages were **optional and declined**: the corresponding EN mentions are plain text, and content guidance does not require a return link for every mention.
- `長期`–`時期`/`時代` and `関連`–`関する` remain **optional and declined**. The first shares a broad period gloss but distinguishes long duration from event timing/era; the second distinguishes a relation noun from a verb about a topic. Shared vocabulary/semantic field alone did not establish a direct answer collision.
- A final excerpt-only review questioned bracketed `[度]` and `[もう一度]`; the actual final card contains valid relative Markdown links, so this note does not apply.

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** for the reviewed batch and directly adjudicated pairs. Exclusions are direct pairs, not transitive groups; Android applies each declaration symmetrically.

The three primary rechecks covered the full 30-card common sample. The final `回`/`度` pair review was limited to the five named pairs and the exact card excerpts. It did not re-audit the complete Russian word pool or execute the quiz UI.

## Final validation

On the final candidate tree `67ca03cbe945bec9fadb315345c71a54707b2483`:

- `tools/build_manifest.py`: 3,729 files; content version `817df18244d528ab`.
- `tools/validate.py`: 0 errors.
- `python -X utf8 -B -m unittest discover -s tools -p 'test_*.py'`: 124 tests passed.
- `tools/check_content_budget.py`: 3,737 archive files; 10,448,115 inflated bytes.
- 30-card source checker: 0 bad; 59 example sentence/reading pairs checked with no missing Japanese sentence or kana reading.
- Frozen Japanese sentence scan: 124 strings, 0 missing.
- Link parity: all 47 changed Markdown files checked.
- Intake hashes were refreshed for all 47 payloads; the candidate tree was signed and committed unchanged as `9a98b6d8ad1e87b737f10235148b10737083f3cb`.

The navigation-only helper was initially verified during authoring and independently inspected in review. Its later broad rerun was not applicable to a base containing newly added cards; it attempted to `git show` a new card from the pre-batch base. The 17 navigation files were unchanged by the fix rounds, and link parity passed on the final 47-file payload.

## Limits

No native-speaker, device, learner, voice, drawing, runtime import, activation or ordinary-release acceptance is claimed. The exact model variants above are the assigned models recorded by the task runner; no additional serving-build identifiers were available.
