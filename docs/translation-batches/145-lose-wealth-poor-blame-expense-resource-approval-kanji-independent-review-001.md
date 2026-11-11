# Batch 145 independent review

**Candidate:** `6cb20cdce4e657d51632dbd74665473a6de4e853`

**Parent:** `0997550`

**Frozen English source:** `6af98cb717755690a9ca793e5454a96ebd7a8f9f`

## Scope and result

The read-only review covered the seven new lessons (`負`, `財`, `貧`, `責`, `費`, `資`, `賛`), their stroke assets, the two authorized reciprocal word-link edits, and the generated manifest delta. The reviewer confirmed that lesson metadata, readings, distractors, and cited JMdict IDs match the frozen source; all seven stroke files are byte-identical; the manifest contains exactly 14 registrations and two word-page hash updates; and both word edits are navigation-only. Lesson links resolve, and unavailable optional word targets remain plain Japanese text.

The initial report raised one MEDIUM finding at `kanji/費.md:5`, alleging that `grade-5` should be `grade-4`. In a focused follow-up, the reviewer withdrew the finding after checking the Ministry of Education, Culture, Sports, Science and Technology (MEXT) document *音訓の小・中・高等学校段階別割り振り表（平成29年3月）*. The official table lists `費5 ヒ`, assigning the reading ヒ to elementary grade 5. A local text extraction of the official PDF independently returned the same row. The candidate's `grade-5` classification is supported; no file change is warranted.

**Final review result: no actionable findings.** The review made no file or Git changes.

## Limits

All 21 direct negative/fallback distractor directions remain **UNVERIFIED**; no transitive closure or quiz-safety claim is made. The review does not certify native-speaker frequency or naturalness, independent JMdict record accuracy, runtime/device/media behavior, activation, or release readiness.

Primary classification evidence: [MEXT, 音訓の小・中・高等学校段階別割り振り表（平成29年3月）](https://www.mext.go.jp/a_menu/shotou/new-cs/__icsFiles/afieldfile/2017/05/15/1385768.pdf) (`費5 ヒ`).
