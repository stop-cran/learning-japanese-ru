# B257 — scoped rechecks at the first signed learner fix

The initial blind reports for [correctness](257-words-batch-96-review-correctness-002.md), [Russian comprehensibility](257-words-batch-96-review-comprehensibility-001.md) and [consistency/quiz integration](257-words-batch-96-review-consistency-001.md), and the supplementary [GPT correctness report](257-words-batch-96-review-correctness-001.md), concern signed blind candidate `bd3cb7293fa63d0b8ad59692524d561e2df91678`, tree `8b50554614afa6e0e4d5f91895425ced03b43387`. Their routing and execution are recorded in the [routing note](257-words-batch-96-review-routing-blocker-001.md) and in execution records [001](257-words-batch-96-review-execution-001.json) and [002](257-words-batch-96-review-execution-002.json). The rechecks below concern signed learner fix 1 `26e81a9dd6966cd0b5344f64ef231183cdb51b79`, tree `5371092b856634110dcd8669bfc914c300487778`, with frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. Its sole parent `d8bda4bd4b0d64c98beca98485158b07c7c0d7fd` and that revision's sole parent `f16b4a6ce980e6df1bfda62640c558ee623f3cac` only add review records to the candidate. Excluding `docs/`, fix 1 changes 15 paths, +34/−34 lines, against its parent and the candidate alike: `manifest.json` (content version and 14 payload hashes) and the cards 下旬, 写る, 工夫, 日差し, 日帰り, 早口, 明け方, 映す, 昼寝, 曖昧, 曲げる, 更ける, 書道 and 月末. The other 16 new words, the existing 汗 correction and the five navigation files are byte-identical to the candidate. Every example keeps its Japanese sentence and reading; the Russian translations of examples differ in six cards: 下旬, 日差し, 明け方, 映す, 更ける and 書道. The final reviewed learner revision is fix 4 `fc7d195e010a02dc0bc163fb7da877bfdbade803`. The later records are [fix 1](257-words-batch-96-recheck-001.md), [fix 2](257-words-batch-96-recheck-002.md), [fix 3](257-words-batch-96-recheck-003.md), [fix 4](257-words-batch-96-recheck-004.md) and [execution 003](257-words-batch-96-review-execution-003.json). Full public reports follow; their hashes identify the original UTF-8 report bodies, not stdout wrappers or the full file. Each report also appeared in read-only tool output. The bodies are reproduced byte-for-byte and may contain the reviewers' own local paths to the exported review inputs.

**Order and reviewer identity.** “Original reviewer” means the instance that wrote the counted initial report for its facet. The original Claude correctness reviewer `2244d4c0-09a0-4712-8da3-0888a527f859` received its follow-up by `write_agent`; its final report and observed idle notification preceded the follow-up to the original Grok comprehensibility reviewer `fbadf36a-13f7-4a66-8047-ecc96e03dee5`. For such follow-ups the end time is the final report's `assistant.turn_end` followed by the observed idle notification, not a `subagent.completed` event. No consistency recheck ran on this fix: neither original GPT instance could be reached, as described in the [fix 3 record](257-words-batch-96-recheck-003.md). The consistency facet was rechecked on fix 3 and fix 4.

**Outcome.** The correctness reviewer marked finding F1 and observations O1–O4 resolved, judged the added 工夫–発想 and 工夫–仕方 exclusions warranted and the 昼寝–夢 exclusion harmless, raised no new finding and returned CLEAN for correctness, coverage and Russian comprehensibility. The comprehensibility reviewer marked its items 1–6 resolved, with kanji/方.md:36 withdrawn and kanji/明.md:58 resolved without edit. It raised one new Low finding: «исходный список слов», added to 工夫:34 and 月末, was unexplained editorial jargon. It cited 月末 line 38; its next recheck corrected this to line 37. Its Russian comprehensibility verdict NEEDS FIX led to fix 2. Its optional points on 日程, 昼寝 «сиеста» and the 発想 exclusion were not elevated and were not adopted. The evidence does not establish runtime distractor behavior, learner or device outcomes, frequency, publication or release readiness.

**Gates.** The four serial gates ran on the working tree before the signed commit, and the committed manifest has the gate's content version: content version `7fb678057780f1a7`, 5,829 manifest entries, validator 0 errors, 124 unit tests passed in 61.995 s, local ZIP 8,468,465 bytes; gate calls 2026-11-24T06:57:28.571Z–2026-11-24T07:00:15.596Z, signed commit at 2026-11-24T07:00:39Z.

**Limits.** Packet diff coverage counts the diff files whose whole whitespace-normalized text appears contiguously in one successful tool result returned before the final report (“complete”), and those whose hunks, from the first `@@` line on, appear so (“all hunks”). Per-file counts exclude the combined diff file, which is reported separately. A contiguous return documents exposure, not comprehension. A lower count means that the record does not establish one complete contiguous read of that file, not that the reviewer did not examine the material in another way, for example through the exported cards. Exposure before a context compaction is not retention. Model identity comes from runtime assistant-response, tool-dispatch and usage records, not from the reports' self-descriptions or lifecycle labels. The exported trees exclude the seven B257 review records. Tool-call arguments and returned results, other than the final stdout echo, were searched for identifiers of the RU worktree, session state, batch records and the ledger, tracking and progress files; each hit is categorized. Hit categories: *own-docs-grep*: a search in the exported tree returned one-line excerpts of public review records of earlier batches (eight lines, all from batches before 257); the reviewer disclosed this in its report. No device, media, voice, drawing, activation or publication clearance is given.

## Correctness — original reviewer

- **Reviewer:** `2244d4c0-09a0-4712-8da3-0888a527f859`; 19 assistant responses, 21 tool dispatches and 19 usage records, all `claude-opus-5.5`.
- **Dispatch:** follow-up by `write_agent` at 2026-11-24T07:04:31.710Z (3,355 UTF-8 bytes, SHA-256 `4d3f6f956b052e9c94cd29c90ed6cd38685acc9d4a6c001ac01bccc8b2123088`), delivered at 2026-11-24T07:04:32.939Z with identical bytes; final report at 2026-11-24T07:16:33.815Z, its `assistant.turn_end` at 2026-11-24T07:16:33.816Z, idle notification observed at 2026-11-24T07:16:57.129Z; no other sub-agent's events occurred in that window.
- **Tools:** powershell 20, read_powershell 1; none failed.
- **Diff coverage:** candidate → fix 1: 15 per-file diffs, complete 1/15, all hunks 15/15; combined diff not returned complete.
- **Context compaction:** started 2026-11-24T07:08:51.031Z, completed 2026-11-24T07:10:13.828Z, removed 54 of 65 messages; 3 of 3 calls that supplied diff coverage returned before it started.
- **Identifier hits:** own-docs-grep 1.
- **Echo:** the final response equals the report body; a read-only stdout echo completed at 2026-11-24T07:16:10.827Z returned it exactly.

Verbatim report body: 8,203 UTF-8 bytes, SHA-256 `e775dc1f1c87f464dfe01d17c288a874eb2e15d3f043f361602e57f892950112`.

B257 correctness/source coverage — bounded recheck + final acceptance (Japanese-correctness facet)

Snapshot
- Fix 26e81a9dd6966cd0b5344f64ef231183cdb51b79 (tree 5371092b856634110dcd8669bfc914c300487778), learner descendant of my reviewed candidate bd3cb7293fa63d0b8ad59692524d561e2df91678. Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f (clean checkout, HEAD re-checked).
- recheck-fix1\index.json SHA-256 244eaeae…b21b and all-learner-changes.diff 5e404e78…7e5a (24036 B) re-hashed: match. All 15 per-file diff hashes/sizes and candidate/fix blob IDs (recomputed from both exports) match the index.
- Read-only: no file writes, no agents. Runtime-observed model identity: unavailable.

Scope (actual complete reads)
- All 14 words__*.md.diff in full (19 changed lines); manifest.json.diff in full (contentVersion 8280df1bcb5f9963→7fb678057780f1a7; only the 14 card SHA-256 values change); fix manifest hashes re-verified against the 14 fix cards: 14/14.
- My own difflib candidate→fix comparison of the 14 cards reproduces exactly these 19 lines.
- Byte comparison of both exports: 8381 files each, identical path sets, exactly 15 differ (manifest + 14 cards = index set). Byte-identical: the 16 other new cards (有料 月給 書籍 曲線 捩る 捻る 普及 映る 日陰 日課 日時 日程 日用品 光線 日当たり 日の出), the five navigation files (kanji/方.md, kanji/明.md, words/カーブ.md, words/写す.md, words/直線.md), words/汗.md and all other files.
- Fix context: 更ける l.1–42, 早口 l.1–41, 明け方 l.14–40, 下旬 l.12–17, 日帰り l.28–44; front matter/opening of 工夫 昼寝 発想 仕方 夢 日の出 夜明け.
- EN halves (packet = 6af98cb): 曲げる l.29–31; 工夫 l.9, 33–36; 月末 l.35–38; 写る l.38–46; 書道 l.14–23; 明け方 l.1–24; 下旬 l.13–21; 日差し l.18–21; 日帰り l.38–48; 早口 l.34–49; 映す l.17–19; 曖昧 l.15–19; 更ける l.18–22, 38–50; 昼寝 l.9.
- Sources: packet dictionary 工夫 (1278220 S1–S3), 月末 (sourceSurface げつまつ; readings げつまつ, つきずえ), 昼寝 (1426370 S1); frozen docs/n2-vocabulary-batch-sources/batch-22.json N2:434 (kana くふう, waller_definition "labourer,worker"; identityNote → こうふ 1278230); docs/content-format.md:144 and docs/confusable-words.md:312 (exclusion pairs apply symmetrically). ACA 025, Daijisen (明け方; 更ける s.2) and JMA evidence reused from my original review, not re-fetched.

Item statuses
- F1 resolved — words/曲げる.md:30 now ends «Ссылка ведёт на карточку 曲る; обычное написание — 曲がる.» = EN l.30 (linked article keeps stable ID 曲る); agrees with words/曲る.md (usual 曲がる). The false spelling claim is gone.
- O1 resolved — words/工夫.md:34 adds «Исходный список слов смешивает толкование «рабочий» с чтением くふう; словарная статья для этого чтения устраняет несоответствие.» = EN l.35, confirmed by N2:434. words/月末.md:37 «…основное чтение этой карточки — げつまつ, как в исходном списке слов.» = EN l.37; sourceSurface げつまつ.
- O2 resolved — words/写る.md:40 «…и при воспроизведении записи, и когда изображение с камеры показывается в реальном времени, одновременно со съёмкой.» = EN l.42 ("simultaneous live display"), ACA 025 (撮影と同時に画像を再生する場合). The «прямая трансляция» narrowing is gone.
- O3 resolved — words/書道.md:19 «Каждую субботу я хожу на занятия каллиграфией.» renders 習っています (EN l.20 "I take calligraphy lessons").
- O4 resolved (was optional, not an error) — words/明け方.md:4 and :12 «время около рассвета», :19 «Дождь прекратился под утро, около рассвета.», :22 «небо на рассвете» match EN l.4/11/18/21 and RU l.16; consistent with JMdict 1532300 and Daijisen/JMA (no fixed hour).

Regression check of the other changed lines (Japanese/reading halves of all six changed example lines are unchanged)
- 下旬:19 «Я переезжаю в последней декаде апреля.» — 四月下旬 = 21–30 April; matches l.12/16/17 and EN l.19 "late April". OK.
- 日差し:19 «Сегодня сильный солнечный свет.» = EN l.19 "The sunlight is strong today." OK.
- 映す:19 «Я отразил своё лицо в зеркале.» = EN l.19 literally; keeps transitive 映す with the speaker as agent. OK.
- 曖昧:17 «расплывчатый, неопределённый ответ» = EN l.17 "a vague answer"; the extra «уклончивый» is gone. OK.
- 更ける:20 «Пока мы разговаривали, стало совсем поздно.» — 夜が更けました, EN l.21 "the night grew late"; night is fixed by title «(о ночи)», l.16, l.18; unchanged l.21 uses the same rendering. OK.
- 更ける:38 秋が更ける «осень становится всё глубже» — Daijisen s.2 季節が深まる; EN l.44–45 "autumn advances". OK.
- 日帰り:41 «Даже если дорога занимает всего час, … туда и обратно собираются съездить в пределах одного дня.» = EN l.44–45; same-day return per l.29, JMdict 1463920. OK.
- 早口:37 «Само существительное описывает только скорость речи.» keeps the EN l.45 core. The dropped EN l.43–44 negation (persuasive/dishonest/fluent) is tied to English "fast talker" (that sentence was already omitted in the candidate); «только» keeps the Japanese restriction; the RU card nowhere uses «беглый/бегло». Acceptable localization; no Japanese fact lost.
- Exclusions (no duplicate/self IDs; words/発想.md, 仕方.md, 夢.md exist; a declared pair acts in both directions):
  - 工夫+発想 warranted: 1278220 S2 "device; design; idea; plan" vs 発想 «идея; подход (к задаче)».
  - 工夫+仕方 warranted: S1 "devising (a way)", S2 "device" vs 仕方 «способ; приём»; the RU 工夫 title contains «способа» (方法, 手段 already excluded).
  - 昼寝+夢: Japanese senses do not overlap (1426370 nap vs dream/ambition); justified only by RU «сон» in both titles («дневной сон; сиеста» / «сон; мечта»). Harmless: it only removes a distractor.

New findings
- None.

Final verdicts (full B257 scope at fix 26e81a9d)
- Correctness: CLEAN.
- Coverage/preservation of frozen EN: CLEAN.
- Russian comprehensibility as it bears on facts: CLEAN.
- Boundary: unchanged material (16 other new cards, 汗 correction, five navigation diffs, unchanged lines of the 14 cards) relies on my original complete read of byte-identical content; only the 19 changed lines plus the context above were newly checked. CLEAN = no confirmed fixable defect within this boundary; not certification of the corpus, devices, media, voice or activation.

Optional
1. 更ける:20 could keep 夜 visible, e.g. «…наступила глубокая ночь».
2. Quiz facet: 明け方's broader «время около рассвета» vs unexcluded 日の出 «восход солнца; время восхода солнца». Japanese differ (dawn period vs sunrise); EN has the same unexcluded pair. No change required.

Limits
- No fresh web fetches and no quiz-engine run in this recheck; symmetry taken from frozen docs.
- A grep of the export's docs for an EN-adaptation rule incidentally printed eight one-line excerpts of earlier batches' review records (docs/translation-batches/, not B257). I did not open or use them; the 早口 judgement rests on the EN/RU text only.
- Not read: any RU worktree/checkout, .copilot paths, the RU GitHub repo, other reviewers' reports, author rationale.

## Russian comprehensibility — original reviewer

- **Reviewer:** `fbadf36a-13f7-4a66-8047-ecc96e03dee5`; 8 assistant responses, 41 tool dispatches and 8 usage records, all `grok-4.7`.
- **Dispatch:** follow-up by `write_agent` at 2026-11-24T07:19:56.135Z (3,620 UTF-8 bytes, SHA-256 `98f0f7ffcb7b41ac30d919f3a659ee464128c23fb44b062d5b133dd9dcf375a2`), delivered at 2026-11-24T07:19:57.666Z with identical bytes; final report at 2026-11-24T07:24:22.791Z, its `assistant.turn_end` at 2026-11-24T07:24:22.793Z, idle notification observed at 2026-11-24T07:24:27.821Z; no other sub-agent's events occurred in that window.
- **Tools:** grep 2, powershell 3, view 36; one `grep` call failed at 2026-11-24T07:21:06.461Z because of a nonexistent search path; no other call failed.
- **Diff coverage:** candidate → fix 1: 15 per-file diffs, complete 15/15, all hunks 15/15; combined diff not returned complete.
- **Context compaction:** started 2026-11-24T07:20:10.726Z, completed 2026-11-24T07:20:49.987Z, removed 98 of 117 messages; 0 of 15 calls that supplied diff coverage returned before it started.
- **Identifier hits:** none.
- **Echo:** the final response equals the report body; a read-only stdout echo completed at 2026-11-24T07:24:13.230Z returned it exactly.

Verbatim report body: 6,742 UTF-8 bytes, SHA-256 `f46297d721f131312630f3d695e6f6ed6087beb968431a911b3af62a46dadc19`.

B257 Russian-comprehensibility recheck

Snapshot: signed learner fix 26e81a9dd6966cd0b5344f64ef231183cdb51b79 (tree 5371092b856634110dcd8669bfc914c300487778), learner descendant of bd3cb7293fa63d0b8ad59692524d561e2df91678. Frozen EN unchanged: 6af98cb717755690a9ca793e5454a96ebd7a8f9f. Runtime model identity: unavailable.

Scope: Complete reads of all 14 word diffs (19 changed lines) and manifest.json.diff. Fix-card context: 工夫.md:1-45, 月末.md:1-45, 写る.md:1-50, 書道.md:1-40, 昼寝.md:1-30, 明け方.md:1-30, 更ける.md:16-40, 早口.md:32-40, 曲げる.md:26-32, 日程.md:35-45, kanji/方.md:30-42, kanji/明.md:52-64; titles of 発想.md, 仕方.md, 夢.md. Own SHA-256 compare: 8381=8381 paths; 8366 paths outside the 15 changed files identical; 0 missing; all 15 changed paths differ. Unchanged learner text (16 other new cards, five navigation files, 汗) was not re-read; it relies on the original complete read. Japanese example and reading halves in the diffs did not change.

Item statuses:
1. words/日差し.md:19 — resolved. «Сегодня сильный солнечный свет.» The light is the subject; added heat is gone.
2. words/更ける.md:20 — resolved. «стало совсем поздно.» This no longer sounds like nightfall and agrees with :21 and :23. words/更ける.md:38 — resolved. «осень становится всё глубже.» Closer to seasonal deepening; not a new defect.
3. words/明け方.md:4 and :12 — resolved. Title and heading: «время около рассвета». words/明け方.md:19 — resolved. «под утро, около рассвета.» Related :22 now «небо на рассвете», no longer «перед». kanji/明.md:58 — resolved without edit. Already «время около рассвета»; now matches the card. kanji/方.md:36 — withdrawn. Unchanged «рассвет» is a short readings-table gloss. It no longer contradicts a «пред-» title, and this page does not pair it with 夜明け. Not a confirmed remaining defect.
4. words/映す.md:19 — resolved. «Я отразил своё лицо в зеркале.»
5. words/早口.md:37 — resolved. The fast-talker triad is gone: «Само существительное описывает только скорость речи.»
6. words/曲げる.md:30 — resolved. «Ссылка ведёт на карточку 曲る; обычное написание — 曲がる.»

Optional points:
- words/下旬.md:19 — resolved. «Я переезжаю в последней декаде апреля.» No longer overlaps 月末 «конец».
- words/日程.md:40 — optional. Unchanged: «не переносите на каждое 日程 значение «повестки дня»». Not elevated.
- words/曖昧.md:17 — resolved. «расплывчатый, неопределённый ответ»; «уклончивый» removed.
- words/日帰り.md:41 — resolved. «Даже если дорога занимает всего час, поездка не становится 日帰り автоматически…» A one-hour road is no longer read as excluded by duration alone.
- words/昼寝.md:4 and :12 — optional. Title still «дневной сон; сиеста». Not elevated. The new 夢 exclusion is separate.

New findings:
1. Low. words/工夫.md:34 and words/月末.md:38. Claim: «Исходный список слов смешивает толкование «рабочий» с чтением くふう; словарная статья для этого чтения устраняет несоответствие.» and «как в исходном списке слов». Consequence: «исходный список слов» is unexplained editorial jargon, a calque of EN "source list", for a learner who never sees that list. On 工夫 the added sentence can reopen the くふう/こうふ distinction the previous sentence just closed: the learner may think a course list assigns «рабочий» to くふう. On 月末 the aside does not change the reading げつまつ, but it cites an unseen authority. Correction: delete both additions. The two sentences before 工夫.md:34 already suffice. If a dictionary point is kept, use only «В словаре чтение くふう — изобретательность и способ; «рабочий» относится к отдельному слову こうふ.» Evidence: those fix lines, read in context; EN 工夫 "The source list mixes…" and EN 月末 "the source list's げつまつ" explain the calque, not that the Russian is learner-clear. The source-list mix itself was not re-verified and is not treated as a Japanese usage fact. Confidence: high.

Regression, not findings: words/写る.md:41 is clearer than «прямой трансляции» and matches EN "simultaneous live display"; examples unchanged. words/書道.md:19 «хожу на занятия каллиграфией» matches 習っています and EN "take lessons" and does not teach a false rule. Quiz exclusions: 仕方 «способ; приём» shares «способ» with 工夫 «придумывание способа» — warranted. 夢 «сон; мечта» shares «сон» with 昼寝 «дневной сон» — warranted. 発想 «идея; подход (к задаче)» shares no title token with 工夫; the exclusion is not required by title overlap, but it does not make labels less distinguishable and is not a learner-text defect. manifest.json changes only contentVersion. The only changed title is 明け方 «время около рассвета», distinct from 夜明け «рассвет» (kanji/明.md:58) and from 夕方. 下旬 and 月末 remain distinct.

Final verdicts: full B257 scope. Unchanged material relies on the original complete read; only the changed lines were newly checked. CLEAN means no confirmed fixable defect in that boundary.
- correctness: CLEAN
- coverage: CLEAN
- Russian comprehensibility: NEEDS FIX

Optional: 発想 exclusion is not required by Russian-title overlap. 日程 and 昼寝 «сиеста» stay optional and are not elevated. «осень становится всё глубже» is slightly figurative but is anchored by «углубление времени года» in the same sentence.

Limits: No file writes. No other RU checkout, .copilot path, author rationale, or another reviewer's report. JMdict/Daijisen were not re-opened for unchanged claims. The 31 packet pairs were not re-read. Byte identity is SHA-256 of the two raw exports, not a second Git checkout. Device, media, and voice are out of scope. Runtime model identity: unavailable.
