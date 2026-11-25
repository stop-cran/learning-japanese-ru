# B257 — scoped recheck at the second signed learner fix

This recheck concerns signed learner fix 2 `6f44b5b76f54b0374d710262fe100464b1987787`, tree `1715e08eaf3c485fe210948193eebc0332bec95b`, with frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. Its sole parent is fix 1 `26e81a9dd6966cd0b5344f64ef231183cdb51b79`. Excluding `docs/`, fix 2 changes 3 paths, +5/−5 lines against fix 1: `manifest.json` (content version and two payload hashes), 工夫 line 34 and 月末 line 37. Against blind candidate `bd3cb7293fa63d0b8ad59692524d561e2df91678` it changes 15 paths, +34/−34 lines. No example line changed. The records are [fix 1](257-words-batch-96-recheck-001.md), [fix 2](257-words-batch-96-recheck-002.md), [fix 3](257-words-batch-96-recheck-003.md), [fix 4](257-words-batch-96-recheck-004.md) and [execution 003](257-words-batch-96-review-execution-003.json). The full public report follows; its hash identifies the original UTF-8 report body, not the stdout wrapper or the full file. The report also appeared in read-only tool output. The body is reproduced byte-for-byte and may contain the reviewer's own local paths to the exported review inputs.

**Order and reviewer identity.** Only the reviewer that raised the fix 1 finding, the original Grok comprehensibility reviewer `fbadf36a-13f7-4a66-8047-ecc96e03dee5`, received a follow-up on this fix. The original Claude correctness reviewer later covered fix 1 → fix 3, and the replacement consistency reviewers covered candidate → fix 3, in the [fix 3 record](257-words-batch-96-recheck-003.md).

**Outcome.** The reviewer marked the 月末:37 part of its finding resolved and the 工夫:34 part partially resolved: a new clause still said that the word list behind the card had glossed くふう as «рабочий». Its new Low finding asked to delete the sentence from «Так было и» to its end; its Russian comprehensibility verdict NEEDS FIX led to fix 3. It corrected its earlier 月末 citation from line 38 to line 37. Its optional remark that the remaining 月末:37 clause «как в списке слов, на котором она основана» could be deleted was not adopted; the reviewer stated that the clause no longer blocks. The evidence does not establish runtime distractor behavior, learner or device outcomes, frequency, publication or release readiness.

**Gates.** The four serial gates ran on the working tree before the signed commit, and the committed manifest has the gate's content version: content version `d8931b53b81287fe`, 5,829 manifest entries, validator 0 errors, 124 unit tests passed in 51.523 s, local ZIP 8,468,501 bytes; gate calls 2026-11-24T07:28:50.509Z–2026-11-24T07:30:36.481Z, signed commit at 2026-11-24T07:41:23Z.

**Limits.** Packet diff coverage counts the diff files whose whole whitespace-normalized text appears contiguously in one successful tool result returned before the final report (“complete”), and those whose hunks, from the first `@@` line on, appear so (“all hunks”). Per-file counts exclude the combined diff file, which is reported separately. A contiguous return documents exposure, not comprehension. A lower count means that the record does not establish one complete contiguous read of that file, not that the reviewer did not examine the material in another way, for example through the exported cards. Exposure before a context compaction is not retention. Model identity comes from runtime assistant-response, tool-dispatch and usage records, not from the reports' self-descriptions or lifecycle labels. The exported trees exclude the seven B257 review records. Tool-call arguments and returned results, other than the final stdout echo, were searched for identifiers of the RU worktree, session state, batch records and the ledger, tracking and progress files; each hit is categorized. No hit occurred in the rechecks of this record. No device, media, voice, drawing, activation or publication clearance is given.

## Russian comprehensibility — original reviewer

- **Reviewer:** `fbadf36a-13f7-4a66-8047-ecc96e03dee5`; 5 assistant responses, 12 tool dispatches and 5 usage records, all `grok-4.7`.
- **Dispatch:** follow-up by `write_agent` at 2026-11-24T07:43:20.397Z (3,526 UTF-8 bytes, SHA-256 `5caee4fc4cc33d5c3faa1729999d86444d3c2dbe990bd6af66cc54a91734f550`), delivered at 2026-11-24T07:43:21.575Z with identical bytes; final report at 2026-11-24T07:46:06.229Z, its `assistant.turn_end` at 2026-11-24T07:46:06.231Z, idle notification observed at 2026-11-24T07:46:12.741Z; no other sub-agent's events occurred in that window.
- **Tools:** grep 1, powershell 3, view 8; none failed.
- **Diff coverage:** candidate → fix 2: 15 per-file diffs, complete 2/15, all hunks 2/15; combined diff not returned complete; fix 1 → fix 2: 3 per-file diffs, complete 3/3, all hunks 3/3; combined diff not returned complete.
- **Context compaction:** none.
- **Identifier hits:** none.
- **Echo:** the final response equals the report body; a read-only stdout echo completed at 2026-11-24T07:45:55.179Z returned it exactly.

Verbatim report body: 5,235 UTF-8 bytes, SHA-256 `f0170fc56c61d6727df40b7f6cd5d9ab33f34a75a3845d42abc23a44b8175e80`.

B257 Russian-comprehensibility recheck 2

Snapshot: signed learner fix2 6f44b5b76f54b0374d710262fe100464b1987787 (tree 1715e08eaf3c485fe210948193eebc0332bec95b), sole parent fix1 26e81a9dd6966cd0b5344f64ef231183cdb51b79. Frozen EN unchanged: 6af98cb717755690a9ca793e5454a96ebd7a8f9f. Runtime model identity: unavailable.

Scope: Complete reads of delta words__工夫.md.diff, words__月末.md.diff, and manifest.json.diff; cumulative words__工夫.md.diff and words__月末.md.diff. Fix2 context: words/工夫.md:1-40, words/月末.md:30-45. PowerShell line count: 工夫 sentence is line 34; 月末 sentence is line 37 (the earlier :38 citation was wrong). Own SHA-256 compare fix-26e81a9d vs fix2-tree-1715e08e: 8381=8381 paths; 8378 paths outside the 3 delta files identical; 0 missing; all 3 delta paths differ. The 12 other cumulative word diffs are SHA-256-identical to the fix1 diffs, so items 1-6 and the Optional points did not change after fix1. Unchanged learner text relies on the original complete read and the fix1 recheck. Only the fix2 lines were newly checked. Japanese examples and readings did not change.

Item statuses:
Previous New finding 1, words/工夫.md:34 — partially resolved. Current line: «Не путайте くふう с отдельным словом 工夫（こうふ）— устаревшим и неделикатным названием чернорабочего. Это значение не относится к くふう из этой карточки. Если список слов даёт при чтении くふう перевод «рабочий», это значение слова こうふ. Так было и в списке слов, на котором основана эта карточка; её значения взяты из словарной статьи для くふう.» The opaque «исходный список слов / устраняет несоответствие» is gone, and the worker gloss is now explicitly assigned to こうふ. The following clause still cites an unseen list and says that list glossed くふう as «рабочий». See New finding 1.
Previous New finding 1, words/月末.md:37 — resolved. Current line: «Словарь также фиксирует чтение つきずえ; основное чтение этой карточки — げつまつ, как в списке слов, на котором она основана.» Ordinary Russian; reading agrees with the header, title «конец месяца», examples, and the next line «Не читайте это слово как げっまつ». The leftover clause is surplus, not a confirmed defect.
Items 1-6 and the Optional points stand. Their cards are byte-identical to fix1; cumulative diffs match the fix1 diffs. No delta change.

New findings:
1. Low. words/工夫.md:34. Claim: «Так было и в списке слов, на котором основана эта карточка; её значения взяты из словарной статьи для くふう.» Also stiff: «даёт при чтении くふう перевод «рабочий».» Consequence: after a clear warning that «рабочий» is こうふ, the card tells a learner who has no separate list that the list behind this card assigned «рабочий» to くふう and that the card's meanings come from another article. That reopens the distinction the first two sentences close and does not help use くふう. It does not contradict the title «изобретательность; придумывание способа» or the unchanged examples, but it adds an editorial conflict. Correction: delete from «Так было и» to the end of the sentence. If the disambiguation is kept, stop at «Если где-то чтение くふう переведено как «рабочий», это значение слова こうふ.» Evidence: fix2 line 34 in context; delta and cumulative diffs; title and examples unchanged. The source-list mix itself was not re-verified and is not a Japanese usage fact. Confidence: high.

Regression: 月末.md:37 agrees with the card's Japanese reading and Russian title. manifest.json changes only contentVersion. Quiz exclusions and titles on both cards are unchanged. No new title collision.

Final verdicts: full B257 scope. Unchanged material relies on the original complete read and the fix1 recheck; only the fix2 lines were newly checked. CLEAN means no confirmed fixable defect in that boundary.
- correctness: CLEAN
- coverage: CLEAN
- Russian comprehensibility: NEEDS FIX

Optional: 月末.md:37 «как в списке слов, на котором она основана» can be deleted, but it no longer blocks. 日程 and 昼寝 «сиеста» remain optional and unchanged. 発想 exclusion remains not required by title overlap and is not a learner-text defect.

Limits: No file writes. No other RU checkout, .copilot path, author rationale, or another reviewer's report. JMdict/Daijisen were not re-opened. The 31 packet pairs were not re-read. Byte identity is SHA-256 of the two raw exports. Device, media, and voice are out of scope. Runtime model identity: unavailable.
