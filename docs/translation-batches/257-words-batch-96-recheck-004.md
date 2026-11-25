# B257 — scoped rechecks at the fourth signed learner fix

These final rechecks concern signed learner fix 4 `fc7d195e010a02dc0bc163fb7da877bfdbade803`, tree `4691d166cddf3d033b850c2f7264203a7e4b65c4`, with frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. Its sole parent is fix 3 `41e708c1434b97b6b58c5239caf0e59939f2e5d4`. Excluding `docs/`, fix 4 changes 2 paths, +3/−3 lines against fix 3: `manifest.json` (content version `5848709124a36a60` → `edfb911307b5669f` and the 明け方 payload hash) and line 9 of `words/明け方.md`, from `quiz_exclusions: [夜明け]` to `quiz_exclusions: [夜明け, 朝]`. Against blind candidate `bd3cb7293fa63d0b8ad59692524d561e2df91678` it changes 15 paths, +35/−35 lines: `manifest.json` and the cards 下旬, 写る, 工夫, 日差し, 日帰り, 早口, 明け方, 映す, 昼寝, 曖昧, 曲げる, 更ける, 書道 and 月末. Every example keeps its Japanese sentence and reading; the Russian translations of examples differ in six cards: 下旬, 日差し, 明け方, 映す, 更ける and 書道. The other 16 new words, the existing 汗 correction and the five navigation files are byte-identical to the candidate. The records are [fix 1](257-words-batch-96-recheck-001.md), [fix 2](257-words-batch-96-recheck-002.md), [fix 3](257-words-batch-96-recheck-003.md), [fix 4](257-words-batch-96-recheck-004.md) and [execution 003](257-words-batch-96-review-execution-003.json). Full public reports follow; their hashes identify the original UTF-8 report bodies, not stdout wrappers or the full file. Each report also appeared in read-only tool output. The bodies are reproduced byte-for-byte and may contain the reviewers' own local paths to the exported review inputs.

**Order and reviewer identity.** The GPT replacement consistency reviewer `881b23c8-2333-4ddd-90a9-c2b9a769f74f`, which raised finding 3, rechecked fix 4 first; this was its second recheck and again a replacement recheck, not an original-agent recheck. The original Claude correctness reviewer `2244d4c0-09a0-4712-8da3-0888a527f859` and the original Grok comprehensibility reviewer `fbadf36a-13f7-4a66-8047-ecc96e03dee5` followed, each after the previous reviewer's final report and observed idle notification. Each of these two original reviewers received, as a temporary input, a byte-identical copy of its own original report, removed after its recheck. Apart from these copies and the original consistency brief and report given to the replacements on fix 3, the dispatch messages supplied no other reviewer's report and no author rationale; they described fix 4 only by its changed paths and line counts.

**Finding 3 and fix 4.** The author adjudicated finding 3 as supported. Digital Daijisen on Weblio defines [明け方](https://www.weblio.jp/content/明け方) as 「夜の明けようとするころ。夜明け方。黎明(れいめい)。払暁(ふつぎょう)。⇔暮れ方。」 and [朝](https://www.weblio.jp/content/朝) as 「夜が明けて間もない時。また、夜明けから正午ごろまでの間。」: first the time shortly after daybreak, then, more broadly, the period from dawn to about noon. The author read both entries at 2026-11-24 20:10 UTC and again at 20:41 UTC. The narrow first part of the 朝 definition adjoins the period that 明け方 names, and the Russian title «время около рассвета» can extend to both sides of dawn, so a bare 朝 question could offer «утро» and «время около рассвета» as two defensible answers. Fix 4 adds only the direct guard, on the changed card; 朝 is unchanged because a declared exclusion applies in both directions. The exclusion declarations in the 30 new words go from 128 to 129. Across all 4,363 word headers the direct declared pairs go from 11,980 to 11,981, adding only 明け方–朝 and removing none; no transitive closure is applied, and 午前–明け方, 夜明け–午前, 夜明け–朝 and 朝ごはん–明け方 remain undeclared. In fix 3 the four cards 朝, 明け方, 有料 and 曲線 had no declared pair among them; in fix 4 they have exactly 明け方–朝. This is a metadata admissibility check, not observed client sampling. The Japan Meteorological Agency's [time terms](https://www.jma.go.jp/jma/kishou/know/yougo_hp/toki.html), fetched later by the correctness reviewer and re-read by the author, give 明け方 as 「午前３時頃から午前６時頃まで。」 and 朝 as 「午前６時頃から午前９時頃まで。」, adjacent periods; this is later confirmation, not the basis of the fix.

**Outcome.** The GPT replacement marked its new finding 3 resolved and kept its previous items 1–3 resolved and items 4–5 optional. It re-tested the four-card witness, found exactly one forbidden pair, 朝–明け方, and wrote: “The previously verified narrow 朝 sense supports this particular pair; it does not justify extending a time-word clique.” It raised no new finding and gave final facet acceptance of exact fix 4: CLEAN for correctness, coverage and Russian comprehensibility. The correctness reviewer checked both senses against Daijisen, JMdict and the JMA terms and judged the exclusion warranted, with no mirror entry needed on 朝. It confirmed that the other changed cards are byte-identical between fix 3 and fix 4 and that the fix 4 manifest builder reproduces `manifest.json` byte-for-byte (522,729 bytes). It also found that the 118 `strokes/*.json` raw-hash differences all match after the tool's CRLF → LF normalization, which closed the limit from its fix 3 recheck. It raised no new finding and returned CLEAN on all three verdicts. The comprehensibility reviewer found that the only learner-file change is the exclusion line, that «утро» and «время около рассвета» stay distinguishable, and that excluding 朝 is a conservative near-neighbor choice, not a learner-text defect; it raised no new finding and returned CLEAN on all three verdicts. All three counted facets therefore returned CLEAN on all three verdicts for exact fix 4, from three distinct actual families. The evidence does not establish runtime distractor behavior, learner or device outcomes, frequency, publication or release readiness.

**Optional points.** The following optional remarks were not adopted: a direct 午前–明け方 guard, which the correctness reviewer called a consistency-facet choice (confidence medium) and which the GPT replacement had advised against inferring; a direct 明け方–日の出 guard, which the correctness reviewer found not required and the supplementary Claude consistency report called defensible but not required by the sources; keeping 夜 visible at 更ける:20; the twelve absent optional kanji articles 及, 捩, 捻, 旬, 昧, 普, 曖, 汗, 籍, 線, 課 and 陰 and links for the plain-text ねじ and 日の入り references; 工夫–様 and 工夫–方 guards, which the supplementary report did not confirm; the full 明け方 title instead of «рассвет» at kanji/方.md:36, which the supplementary report called not needed and the comprehensibility reviewer had withdrawn at fix 1; the correctness reviewer's suggestion to mention again at 工夫:34, for literal parity with EN, the word list on which the card is based, a clause of the kind removed after the comprehensibility findings on fix 1 and fix 2; rewording «указан перевод» at 工夫:34, which the comprehensibility reviewer called slightly bureaucratic; deleting the 月末:37 clause «как в списке слов, на котором она основана»; and the comprehensibility reviewer's original remarks on the «повестка дня» caveat at 日程:40 and on «сиеста» in the 昼寝 title, which it kept optional and did not elevate. The inherited 光線–桁 exclusion stays: the original consistency reviewer noted that the Russian titles no longer share the English “beam” ambiguity but called the exclusion a conservative overrestriction, not grounds to remove a source guard or weaken the pool, and the GPT replacement kept it optional. The comprehensibility reviewer's notes that the 工夫–発想 and 明け方–朝 exclusions are not required by shared Russian title wording leave both in place: the correctness reviewer judged both warranted on dictionary senses, and both consistency replacements supported 工夫–発想, which the supplementary GPT correctness report had raised. None of these remarks was raised as a confirmed defect.

**Counted facets.** Correctness: the original Claude reviewer `2244d4c0-09a0-4712-8da3-0888a527f859` ([initial report](257-words-batch-96-review-correctness-002.md); rechecks of fix 1, fix 3 and fix 4). Russian comprehensibility: the original Grok reviewer `fbadf36a-13f7-4a66-8047-ecc96e03dee5` ([initial report](257-words-batch-96-review-comprehensibility-001.md); rechecks of fix 1, fix 2, fix 3 and fix 4). Consistency/quiz integration: the original GPT reviewer `506797e8-0707-4fcc-91c2-fcccd4d3717f` ([initial report](257-words-batch-96-review-consistency-001.md)), later unreachable, and the GPT replacement `881b23c8-2333-4ddd-90a9-c2b9a769f74f` (rechecks of fix 3 and fix 4). The three actual families are Claude (`claude-opus-5.5`), Grok (`grok-4.7`) and GPT (`gpt-6-astra`). Supplementary and not counted: the GPT correctness report of `11bc0117-0bc5-40ef-9e3c-ba8effd1ae26` under a Claude lifecycle label ([report](257-words-batch-96-review-correctness-001.md)) and the fix 3 recheck by the Claude consistency replacement `6ec8511a-6d52-45e4-9f9c-6ee6571b2249`, a repeat of the correctness family.

**Gates.** The four serial gates ran on the working tree before the signed commit, and the committed manifest has the gate's content version: content version `edfb911307b5669f`, 5,829 manifest entries, validator 0 errors, 124 unit tests passed in 51.825 s, local ZIP 8,468,430 bytes; gate calls 2026-11-24T21:44:40.399Z–2026-11-24T21:49:59.427Z, signed commit at 2026-11-24T21:50:15Z.

**Limits.** Packet diff coverage counts the diff files whose whole whitespace-normalized text appears contiguously in one successful tool result returned before the final report (“complete”), and those whose hunks, from the first `@@` line on, appear so (“all hunks”). Per-file counts exclude the combined diff file, which is reported separately. A contiguous return documents exposure, not comprehension. A lower count means that the record does not establish one complete contiguous read of that file, not that the reviewer did not examine the material in another way, for example through the exported cards. Exposure before a context compaction is not retention. Model identity comes from runtime assistant-response, tool-dispatch and usage records, not from the reports' self-descriptions or lifecycle labels. The exported trees exclude the seven B257 review records. Tool-call arguments and returned results, other than the final stdout echo, were searched for identifiers of the RU worktree, session state, batch records and the ledger, tracking and progress files; each hit is categorized. Hit categories: *supplied-input*: a deliberately supplied input contained a matched term (the original consistency brief or report, or the reviewer's own original report). No device, media, voice, drawing, activation or publication clearance is given.

## Consistency — replacement reviewer (second recheck)

- **Reviewer:** `881b23c8-2333-4ddd-90a9-c2b9a769f74f`; 21 assistant responses, 14 tool dispatches and 8 usage records, all `gpt-6-astra`.
- **Dispatch:** follow-up by `write_agent` at 2026-11-24T22:03:15.083Z (4,692 UTF-8 bytes, SHA-256 `e105b874d208f2f0e021d6eb86138983142cc8cfcd89b4c79dbbd73ad6c07a6d`), delivered at 2026-11-24T22:03:16.569Z with identical bytes; final report at 2026-11-24T22:14:12.610Z, its `assistant.turn_end` at 2026-11-24T22:14:12.611Z, idle notification observed at 2026-11-24T22:14:46.216Z; no other sub-agent's events occurred in that window.
- **Tools:** powershell 9, read_powershell 1, update_todo 4; none failed.
- **Diff coverage:** candidate → fix 4: 15 per-file diffs, complete 0/15, all hunks 0/15; combined diff not returned complete; fix 3 → fix 4: 2 per-file diffs, complete 2/2, all hunks 2/2; combined diff not returned complete.
- **Context compaction:** none.
- **Identifier hits:** none.
- **Echo:** the final response equals the report body; a read-only stdout echo completed at 2026-11-24T22:13:26.299Z returned it exactly.

Verbatim report body: 8,351 UTF-8 bytes, SHA-256 `8e86eb98932c8b9207860d1b3c0a2254d20e1cd395347ab377da7c9569c0b0b5`.

# B257 / word batch 96 — fix4 consistency recheck

## Snapshot

Bounded READ-ONLY second recheck of my replacement consistency/quiz-integration review.

- **Fix4:** `fc7d195e010a02dc0bc163fb7da877bfdbade803`, tree `4691d166cddf3d033b850c2f7264203a7e4b65c4`.
- **Supplied sole parent:** fix3 `41e708c1434b97b6b58c5239caf0e59939f2e5d4`.
- **Frozen EN:** `6af98cb717755690a9ca793e5454a96ebd7a8f9f`, unchanged.
- **Root:** `R = C:\Users\romanko\repos\b257-blind-review-inputs`. Current content citations below refer to `R\fix4-fc7d195e` only.
- **Runtime model identity:** unavailable.

Supplied index, combined delta/cumulative diff, pool, screen and summary SHA-256 hashes matched. Indexed individual diff hashes and candidate/fix3/fix4 blob bindings were checked where applicable.

## Scope

Acceptance covers the full B257 facet: **30 new words, the existing 汗 correction, and five navigation files**. **Unchanged material relies on the original reviewer's complete read and source checks plus my previous fix3 replacement recheck. I did not repeat the complete 31-card review.**

New complete reads:

- `recheck-fix4/delta-fix3/words__明け方.md.diff:1–11`.
- `recheck-fix4/delta-fix3/manifest.json.diff:1–18`.
- `fix4-fc7d195e/words/明け方.md:1–40`.
- `quiz-inputs-fix4/summary.json:1–68`.

Additional targeted reads: `words/朝.md:1–16`, current status/navigation lines cited below, and current witness metadata. The index, both quiz pools and all 31 fix4 fact packets were parsed and compared mechanically; that is not a new semantic reading of every card. Cumulative diff hashes were verified without rereading the cumulative card diffs. No dictionary source was newly fetched; the direct pair's semantic basis remains my previously checked Daijisen evidence for 朝's narrow daybreak-period sense.

### Byte and integration checks

- Own full export comparison, repeated at completion: **8,381 matching paths; 8,379 byte-identical files; exactly two changed files**, `manifest.json` and `words/明け方.md`; **3 insertions/3 deletions**. All other 30 assigned word cards and all five navigation files are unchanged. No export files were added.
- Exact byte substitution proved that 明け方 changed only from `quiz_exclusions: [夜明け]` to `quiz_exclusions: [夜明け, 朝]` at line 9. Every other header field, title, reading, link, body line and line ending is unchanged.
- Comparing the complete pools yielded **exactly one added direct pair, 明け方–朝, and no removed pairs**. Every other exclusion list, every distractor and every title is unchanged. No transitive or clique expansion occurred. The 31 assigned cards now contain **129 exclusion declarations and zero curated distractors**.
- From the fix4 export, with `RU_ROOT` explicitly set there: `python -X utf8 -B tools\validate.py` returned **exit 0, 0 errors**. This is structural validation of the actual export, not semantic or client clearance.
- The entire manifest matched pure in-memory `build_manifest(root)`; its writing entry point was not called. Schema/languages remain **2, ru/ja**. The only changed manifest values are:
  - `manifest.json:3`: `contentVersion: edfb911307b5669f`.
  - `manifest.json:3731`, `words/明け方.md`: LF-normalized SHA-256 `1001011f642c8621085b6a16137406ac78f51d4d09cf7081f1fdf10015f3733b`.
- All **4,363 fix4 pool records** matched actual front matter, with unique IDs. All **31 fact packets**, their **167 related records / 139 unique targets**, reverse declarers, required related sets, unavailable-path lists and summary hashes/counts matched. All **142 relative links** resolved.
- Independent JSON-pointer comparison confirmed that, beyond the embedded commit field, the fact changes are only 明け方's own exclusion list and 日の出's related 明け方 record. The pool changes only at `/words/words~1明け方.md/quiz_exclusions/1`. These agree with the supplied summary.
- The **421-line screen is byte-identical to fix3**. Every displayed title and direct-pair flag still matches the pool. It contains no 明け方–朝 row, so its unchanged hash is expected; the heuristic does not establish semantic completeness.

## Item statuses

### My new finding 3 — resolved

Both endpoints exist. Exact current front-matter evidence:

- `words/明け方.md:3`: `reading: あけがた`
- `words/明け方.md:4`: `title: время около рассвета`
- `words/明け方.md:9`: `quiz_exclusions: [夜明け, 朝]`
- `words/朝.md:3`: `reading: あさ`
- `words/朝.md:5`: `title: утро`
- `words/朝.md:9`: `quiz_exclusions: [午前, 朝ごはん]`

The declaration on 明け方 supplies the requested direct guard. Under the declared symmetric-pair contract, 朝 does not need a duplicate declaration. The previously verified narrow 朝 sense supports this particular pair; it does not justify extending a time-word clique.

**Four-card witness re-tested:** `朝 / 明け方 / 有料 / 曲線`, with current labels «утро» / «время около рассвета» / «платный; требующий оплаты» / «кривая линия; кривая».

It now has **exactly one forbidden pair: 朝–明け方**, also blocked in reverse order. The other five pairwise combinations remain unblocked. Thus the formerly admissible ambiguous quartet is rejected under the metadata rules. This is not a claim of observed client sampling.

### Previous items 1–5 — all statuses still stand

| Previous item | Status | Current evidence |
|---|---|---|
| 1. 昼寝–夢 | **resolved** | `words/昼寝.md:9` still includes 夢. |
| 2. 工夫–仕方 | **resolved** | `words/工夫.md:9` still includes 仕方; the separately verified 発想 guard also remains. |
| 3. 明け方 wording/navigation | **resolved** | `words/明け方.md:4,12` retains «время около рассвета»; `kanji/明.md:58` agrees. The linked あけがた example under `## Чтения` remains at `kanji/方.md:29–36`. |
| 4. Missing optional articles/unavailable links | **optional** | The same optional paths remain absent; ねじ is plain text at `words/捩る.md:45`, and 日の入り（ひのいり）at `words/日の出.md:31`. No required link is dangling. |
| 5. Inherited 光線–桁 exclusion | **optional** | `words/光線.md:9` retains 桁; unchanged titles at `光線:4` and `桁:4` remain «луч света; пучок света» and «балка; количество разрядов». |

## New findings

**None.** The intended direct guard resolves my remaining finding, and no new fixable defect was confirmed within this recheck boundary.

## Final verdicts

For the **full B257 scope within the consistency/quiz-integration facet**, using the explicitly stated unchanged-material dependencies:

- **Correctness: CLEAN.** The remaining confirmed quiz-label ambiguity is now directly guarded.
- **Coverage: CLEAN.** Assigned scope, metadata integration and required dependencies are covered; optional omissions remain distinguished.
- **Russian comprehensibility: CLEAN within this facet.** No confirmed remaining label/consistency defect; this is not a separate general-prose or native-speaker certification.

**Final facet acceptance of exact fix4: CLEAN.** No confirmed fixable defect remains within this boundary.

## Optional

The absent optional kanji articles remain 及, 捩, 捻, 旬, 昧, 普, 曖, 汗, 籍, 線, 課, 陰. Optional ねじ / 日の入り references and the inherited 光線–桁 restriction remain non-blocking. No scope expansion or additional exclusions are requested.

## Limits

No agents, file-writing commands or manifest writer ran. No RU worktree/checkout, `.copilot` contents or RU GitHub repository was accessed; no other reviewer's report or author rationale was sought. Export bytes remained unchanged during the recheck. Commit signatures and sole-parent provenance are supplied facts, not independently verified Git history.

No unit/smoke suite, client playback, randomized option-count, level-filter, device/media/voice or activation test ran. Those runtime properties remain **UNVERIFIED**, outside this source-content acceptance. Parser success and the heuristic screen are not semantic proof. Unchanged semantic coverage remains dependent on the original complete review and my previous recheck, as stated above.

## Correctness — original reviewer

- **Reviewer:** `2244d4c0-09a0-4712-8da3-0888a527f859`; 26 assistant responses, 38 tool dispatches and 26 usage records, all `claude-opus-5.5`.
- **Dispatch:** follow-up by `write_agent` at 2026-11-24T22:20:02.615Z (4,769 UTF-8 bytes, SHA-256 `8f0f9aae731a61596ae130674b7d606e2634ce9162f0571e5f2d96698b39bcfb`), delivered at 2026-11-24T22:20:04.040Z with identical bytes; final report at 2026-11-24T22:34:42.589Z, its `assistant.turn_end` at 2026-11-24T22:34:42.592Z, idle notification observed at 2026-11-24T22:34:44.891Z; no other sub-agent's events occurred in that window.
- **Tools:** grep 4, powershell 26, view 5, web_fetch 3; none failed.
- **Diff coverage:** candidate → fix 4: 15 per-file diffs, complete 1/15, all hunks 1/15; combined diff not returned complete; fix 3 → fix 4: 2 per-file diffs, complete 2/2, all hunks 2/2; combined diff returned complete.
- **Context compaction:** started 2026-11-24T22:25:57.607Z, completed 2026-11-24T22:26:54.455Z, removed 46 of 61 messages; 2 of 2 calls that supplied diff coverage returned before it started.
- **Identifier hits:** supplied-input 1.
- **Supplied originals:** its own initial report (8,489 UTF-8 bytes) was returned in full in one tool result with three-digit line numbers added by the reviewer's own print command; the stricter contiguous test does not count it complete.
- **Echo:** the final response equals the report body; a read-only stdout echo completed at 2026-11-24T22:34:09.475Z returned it exactly.

Verbatim report body: 9,873 UTF-8 bytes, SHA-256 `82a62521ea05247067bfd6e795df28507e4621bd414cda4e598a4bec96f2e260`.

# B257 correctness/source-coverage — third bounded recheck (fix4)

## Snapshot
- Reviewed: signed fix4 fc7d195e010a02dc0bc163fb7da877bfdbade803 (tree 4691d166cddf3d033b850c2f7264203a7e4b65c4), sole parent fix3 41e708c1434b97b6b58c5239caf0e59939f2e5d4; original candidate bd3cb7293fa63d0b8ad59692524d561e2df91678. Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f (exact Git objects).
- Read-only: no edits or file writes, no agents. I opened no RU checkout, .copilot path, RU GitHub repo, other reviewer's report or author rationale. Runtime-observed model identity: unavailable.

## Scope (complete reads this recheck)
- Own original report: 8489 B, SHA-256 e9b9f464… verified; l.1–43 read.
- R\recheck-fix4\index.json (6925 B, 023a1294… verified): all 17 entries checked, i.e. diff SHA-256/sizes and the candidate/fix3/fix4 blob IDs re-hashed from the exports (明け方 c93ca2cf→7505372b, candidate c41ca40f; manifest 3e6ac4de→ecdde76e, candidate 6a7eb656).
- delta-fix3: words__明け方.md.diff (395 B), manifest.json.diff (944 B) and all-fix4-changes.diff (1339 B, d0a67edf… verified), all read completely.
- cumulative: all-learner-changes.diff (24043 B, 16cc5b89… verified). The cumulative 明け方 diff (1851 B) was read completely. The other 13 card diffs and the manifest diff were hash-verified only; those 13 cards are byte-identical fix3→fix4.
- fix4 files:
  - Read in full: words/明け方.md (2376 B), words/朝.md (33 lines), words/夜明け.md (37 lines), tools/build_manifest.py.
  - Current lines: 曲げる:30, 工夫:34, 月末:37, 写る:40, 書道:19.
  - Ranges: docs/content-format-reference.md l.88–108; validate.py quiz-list checks l.34, 173–174, 482–505.
  - Imports of all validator modules checked: no writes or subprocess calls.
- Frozen EN:
  - words/明け方.md (full): no quiz_exclusions; title "dawn; daybreak"; l.32 says 朝 "covers a broader period".
  - words/朝.md: title "morning"; l.17–end read. words/午前.md: title "morning, a.m.".
  - docs/content-format.md:143–144; docs/confusable-words.md:40–81, 306–316.
  - JMdict 1428280 朝/あさ, batch-11.json:14102: S1 n/adv "morning", S2 "breakfast". Also 1428285 ちょう and 2857350 あした.
- packet\dictionary\明け方.json: JMdict 1532300 S1 n/adv "dawn; daybreak", info "usu. from 3:00 a.m. to 6:00 a.m.", xref 暮れ方, 未明.
- Live sources:
  - JMA 時に関する用語, https://www.jma.go.jp/jma/kishou/know/yougo_hp/toki.html. 明け方「午前３時頃から午前６時頃まで」, 備考「夜が明ける頃を指す用語であるが、予報用語としては上記の意味で用いる」. 夜明け「日の出の前の空が薄明るくなる頃」. 朝「午前６時頃から午前９時頃まで」.
  - Daijisen 朝 via https://www.weblio.jp/content/朝: 「夜が明けて間もない時。また、夜明けから正午ごろまでの間」; [補説] JMA 6–9時, →明け方.
- Own comparisons: all 8381 paths byte-compared fix3↔fix4 and candidate↔fix4. All fix4 words/*.md titles scanned for dawn/morning/night labels.
- Tools: run on the fix4 export only, with RU_ROOT=fix4 export, python -X utf8 -B and PYTHONDONTWRITEBYTECODE=1.
  - tools/validate.py → "0 error(s)", exit 0.
  - build_manifest.build_manifest(Path(fix4)) called in memory; main() was not called.
  - File count stayed 8381; no __pycache__ was created.
- Not read: R\quiz-inputs-fix4 (optional context).

## Item statuses (original report)
- Finding 1 (曲げる:30) — resolved; stands. Current: «Ссылка ведёт на карточку 曲る; обычное написание — 曲がる.»
- O1 (工夫:34, 月末:37) — resolved; stands.
  - 工夫:34 ends «Если где-то у 工夫 с чтением くふう указан перевод «рабочий», это значение слова こうふ.»
  - 月末:37: «Словарь также фиксирует чтение つきずえ; основное чтение этой карточки — げつまつ, как в списке слов, на котором она основана.»
- O2 (写る:40) — resolved; stands. Current: «…и когда изображение с камеры показывается в реальном времени, одновременно со съёмкой.»
- O3 (書道:19) — resolved; stands. Current: «Каждую субботу я хожу на занятия каллиграфией.»
- O4 (明け方, originally "no error") — resolved; stands. fix4 changes only l.9.
  - l.4 and l.12: «время около рассвета».
  - l.16: «明け方 — время около рассвета, когда ночь сменяется дневным светом.»
  - l.19: «Дождь прекратился под утро, около рассвета.»
  - l.22: «небо на рассвете».
  - l.9: `quiz_exclusions: [夜明け, 朝]`.
  - The title now equals the 明 kanji gloss noted in O4. 方 «рассвет» remains an acceptable near-synonym (consistency facet).
- 曲げる, 工夫, 月末, 写る, 書道 and every other changed card except 明け方 are byte-identical fix3→fix4. The statuses from my first recheck (fix1) and second recheck (fix3) therefore still stand, including the warranted 工夫 (発想, 仕方) and 昼寝 (夢) exclusions.

## Regression check of the fix4 change
- Scope: the card's l.9 only (`[夜明け]` → `[夜明け, 朝]`), plus the manifest contentVersion and 明け方 hash lines (3+/3−).
  - No Japanese text, reading, sense, title, example, link or other body line changed.
  - Frozen EN 明け方 has no quiz_exclusions, so no EN content is lost. This is an RU quiz-label adaptation.
- Target:
  - words/朝.md exists (word 朝, あさ, title «утро»). The value is not self and not repeated.
  - Neither card has quiz_distractors, and no card lists 明け方 or 朝 as a distractor.
  - The validator checks existence, self, repeats, distractor overlap and the list declaration; it reports 0 errors.
  - Pairs are symmetric (RU content-format-reference.md:96–98; EN confusable-words.md:312), so 朝.md needs no mirror entry.
- Senses:
  - 明け方 = 「夜の明けようとするころ」 (Daijisen); JMdict "dawn; daybreak", usu. 3–6 a.m.; JMA 3–6時.
  - 朝 = 「夜が明けて間もない時。また、夜明けから正午ごろまでの間」; JMdict "morning"; JMA 6–9時.
  - The two periods meet at daybreak and overlap in everyday use. The card itself renders 明け方に as «под утро» (l.19) and says 朝 covers a broader span (l.32 = EN l.32).
  - With the RU titles «время около рассвета» and «утро», a learner could defend either label for either word, so excluding the pair is warranted. The change only removes a quiz pair and makes no learner-facing claim.
  - Title scan: 日の出 «восход солнца; время восхода солнца», 今朝 «сегодня утром» and 毎朝 «каждое утро» stay distinct. For 午前, see Optional.
- Manifest:
  - Entry words/明け方.md = 1001011f642c8621085b6a16137406ac78f51d4d09cf7081f1fdf10015f3733b, the raw SHA-256 of the LF-only file.
  - An in-memory rebuild with the fix4 build_manifest reproduces manifest.json byte-for-byte (522729 B): contentVersion edfb911307b5669f (was 5848709124a36a60), schemaVersion 2, ru/ja, 5824 files, 3 images, 2 scenes.
  - The fix3→fix4 files map differs only in words/明け方.md.
  - The 118 strokes/*.json raw-hash differences all match after the tool's CRLF→LF normalization (0 residual). This closes that limit from my second recheck.
- Byte identity:
  - fix3 vs fix4: same 8381 paths; only manifest.json and words/明け方.md differ; 8379 identical.
  - Candidate vs fix4: exactly 15 differ (manifest + 14 cards), as in the index.

## New findings
None.

## Final verdicts (full B257 scope, fix4)
- Correctness: CLEAN.
- Coverage/preservation of frozen EN: CLEAN.
- Russian comprehensibility as it bears on Japanese facts: CLEAN.
- Boundary: unchanged material rests on my original complete read of the candidate (31 pairs, five navigation diffs, the 汗 correction, packets). It also rests on my first recheck (fix1: 14 cards, 19 lines) and my second recheck (fix3: 工夫:34, 月末:37, manifest).
- Newly checked here: 明け方 l.9 with its full card context, the 朝 and 夜明け endpoints, the manifest delta and full rebuild, the validator run, and byte identity of all other paths.
- CLEAN means no confirmed fixable defect within this boundary. It is not a certification of any card or of the corpus.

## Optional
- 午前 «утро; до полудня» remains an allowed distractor for 明け方. It shares «утро» with the newly excluded 朝, and 3–6 a.m. is literally «до полудня». But it names the a.m. span, not dawn, so the best answer stays clear in both directions.
- Corpus practice is mixed: 朝 excludes 午前 and 深夜 excludes 夜, but 夜中 and 夜 are unpaired. Adding 午前 would be a quiz/consistency-facet choice, not a fix for a Japanese-fact defect. Confidence: medium.

## Limits
- I did not verify signatures, commit lineage or tree IDs; I used only the exports and the index.
- Daijisen and JMA were fetched live and are not version-pinned. JMdict 朝 comes from frozen batch-11.json and 明け方 from the packet.
- I did not read R\quiz-inputs-fix4 or the title screen. Beyond the dawn/morning/night title scan, I did no full pool-collision sweep.
- No new incidental exposure in this recheck. My first recheck's disclosure stands: a docs grep printed 8 one-line excerpts of earlier batches' review records, which I did not open or use.
- No native-speaker or corpus evidence. This is not device/media/voice/activation clearance. Stopping after this recheck.

## Russian comprehensibility — original reviewer

- **Reviewer:** `fbadf36a-13f7-4a66-8047-ecc96e03dee5`; 6 assistant responses, 11 tool dispatches and 6 usage records, all `grok-4.7`.
- **Dispatch:** follow-up by `write_agent` at 2026-11-24T22:38:51.323Z (4,857 UTF-8 bytes, SHA-256 `f5f107f352adf50f77d4a87469bf0f6084561e60c2d5f7c4487106c3ef05f72d`), delivered at 2026-11-24T22:38:52.624Z with identical bytes; final report at 2026-11-24T22:42:46.193Z, its `assistant.turn_end` at 2026-11-24T22:42:46.197Z, idle notification observed at 2026-11-24T22:43:03.966Z; no other sub-agent's events occurred in that window.
- **Tools:** powershell 2, read_powershell 2, view 7; none failed.
- **Diff coverage:** candidate → fix 4: 15 per-file diffs, complete 0/15, all hunks 0/15; combined diff not returned complete; fix 3 → fix 4: 2 per-file diffs, complete 2/2, all hunks 2/2; combined diff not returned complete.
- **Context compaction:** none.
- **Identifier hits:** none.
- **Supplied originals:** its own initial report (6,745 UTF-8 bytes) returned complete in one tool result.
- **Echo:** the final response equals the report body; a read-only stdout echo completed at 2026-11-24T22:42:37.524Z returned it exactly.

Verbatim report body: 4,384 UTF-8 bytes, SHA-256 `06ee860e4b63308e8ff063055f4536ae550ed35552a104773c04a408688d048c`.

B257 Russian-comprehensibility recheck 4

Snapshot: signed learner fix4 fc7d195e010a02dc0bc163fb7da877bfdbade803 (tree 4691d166cddf3d033b850c2f7264203a7e4b65c4), sole parent fix3 41e708c1434b97b6b58c5239caf0e59939f2e5d4. Frozen EN unchanged: 6af98cb717755690a9ca793e5454a96ebd7a8f9f. Runtime model identity: unavailable.

Scope: Complete reads of delta-fix3\words__明け方.md.diff and manifest.json.diff (header plus the 明け方 hash line). Fix4 context: words/明け方.md:1-28, words/朝.md:1-16, words/工夫.md:32-36, words/月末.md:34-40. Own SHA-256 compare fix3-41e708c1 vs fix4-fc7d195e: 8381=8381 paths; 8379 paths outside the 2 delta files identical; 0 missing; both delta paths differ. PowerShell line hits on the other cited cards. Original report read in full (6745 bytes). Unchanged material relies on the original complete read and the fix1-fix3 rechecks. Newly checked: the fix4 quiz_exclusions line and the 朝 title. No Japanese example or reading changed.

Item statuses:
1. words/日差し.md:19 — resolved. «Сегодня сильный солнечный свет.»
2. words/更ける.md:20 — resolved. «стало совсем поздно.» words/更ける.md:38 — resolved. «осень становится всё глубже.»
3. words/明け方.md:4 and :12 — resolved. «время около рассвета». words/明け方.md:16 — «время около рассвета, когда ночь сменяется дневным светом.» words/明け方.md:19 — resolved. «Дождь прекратился под утро, около рассвета.» words/明け方.md:22 still «небо на рассвете». The fix4 edit does not change these lines; line 9 is only quiz_exclusions: [夜明け, 朝]. kanji/明.md:58 — resolved without edit; file byte-identical to the earlier read. kanji/方.md:36 — withdrawn; unchanged short «рассвет», not reopened.
4. words/映す.md:19 — resolved. «Я отразил своё лицо в зеркале.»
5. words/早口.md:37 — resolved. «Само существительное описывает только скорость речи.»
6. words/曲げる.md:30 — resolved. «Ссылка ведёт на карточку 曲る; обычное написание — 曲がる.»
Optional: words/下旬.md:19 — resolved («в последней декаде апреля»). words/日程.md:40 — optional (unchanged caveat). words/曖昧.md:17 — resolved («расплывчатый, неопределённый ответ»). words/日帰り.md:41 — resolved. words/昼寝.md:4 — optional («дневной сон; сиеста»).
Earlier findings still stand: words/工夫.md:34 — resolved («Если где-то у 工夫 с чтением くふう указан перевод «рабочий», это значение слова こうふ.»). words/月末.md:37 — resolved («как в списке слов, на котором она основана»). Both files are outside the fix4 delta.

New findings: none. The only learner-file change adds 朝 to quiz_exclusions. It does not alter title, heading, explanation, or example translation. words/朝.md exists; its title is «утро» (line 5 and heading line 12). Against 明け方 «время около рассвета» the labels share no token and stay distinguishable in a bare quiz. Excluding the broader N5 morning word is a conservative near-neighbor choice, not a learner-text defect. manifest.json changes only contentVersion and the 明け方 hash.

Final verdicts: full B257 scope. Unchanged material relies on the original complete read and the earlier rechecks; only the fix4 exclusion line and the 朝 title were newly checked. CLEAN means no confirmed fixable defect in that boundary.
- correctness: CLEAN
- coverage: CLEAN
- Russian comprehensibility: CLEAN

Optional: 朝 exclusion is not required by shared title wording. 月末 surplus clause, 日程, 昼寝 «сиеста», and the 発想 exclusion remain not elevated.

Limits: No file writes. No other RU checkout, .copilot path, author rationale, or another reviewer's report. JMdict/Daijisen were not re-opened. The 31 packet pairs were not re-read. Byte identity is SHA-256 of the two raw exports. Device, media, and voice are out of scope. Runtime model identity: unavailable.
