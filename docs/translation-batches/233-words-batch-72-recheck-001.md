# Batch 233 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `5218a9afd4d733f79b5d88fc1f826c760dd93a8c` | `3aadf38b46b2d7b39f480ddaf01b9007deb5a244` | Initial review snapshot: the signed candidate, on `origin/full-ru-233-words-72`. |
| `1d78dd8417644049b0d391cf73eb660425bb93ea` | `3a6a09d083c39bc979773588560071ccf44d1d43` | Fix 1 (final candidate). It covers correctness F1 and the correctness optional, comprehensibility C1, C3–C8, C10 and C11 (C5, C8 and C11 with adapted wording; C1 and C6 partially adopted) and consistency O2 and O3. It adds and removes no exclusion. Signed; on `origin/full-ru-233-words-72`. |

Fix 1 changed twelve word files and regenerated `manifest.json` (`contentVersion` `24595e05bf341944`, 5,109 entries; the
candidate had `398922b5be16e31e`). The intake was not refreshed; it still records the candidate's 33 payload hashes.
- `成立` (lines 4 and 12; correctness F1): title and H1 «образование (организации); заключение (договора, сделки);
  состоятельность (довода)» instead of «заключение (договора, сделки); принятие (закона); образование (организации)». The
  glosses follow EN's order ("formation; conclusion; validity"); «принятие (закона)» leaves the short title, and the body
  still teaches enacting a law. The exclusion list is unchanged.
- `逆さ` (lines 4 and 12; comprehensibility C8, adapted wording): title and H1 «вверх ногами; задом наперёд» instead of
  «вверх ногами; наоборот». The reviewer's «в обратную сторону» was not used, because it implies motion and meets 逆
  «обратный»; the body already uses «задом наперёд».
- `通路` (lines 4 and 12; comprehensibility C11, adapted wording): title and H1 «проход (между рядами, сиденьями); проход
  или проезд» instead of «…; проход для людей», matching line 16 (people or vehicles). The reviewer's «путь для прохода»
  was not used, because it keeps the people-only reading.
- `出勤` (line 19; comprehensibility C3): «Завтра я приступаю к работе в девять.» instead of «Завтра я выхожу на работу к
  девяти.»
- `すれ違う` (line 20; comprehensibility C5, adapted wording): «В коридоре мы с учителем прошли мимо друг друга.» instead of
  «В коридоре я прошёл мимо учителя.» The reviewer's «разошёлся» was not used, because it is ambiguous in Russian (also
  "parted, separated").
- `通り掛かる` (lines 21 and 45; comprehensibility C4): «Когда я случайно проходил мимо магазина, я встретил друга.» instead
  of «Когда я проходил мимо магазина, …», and «человек, который случайно проходил мимо, …» instead of «… который просто
  проходил мимо, …».
- `効力` (lines 24–25 and 42; comprehensibility C6, partially adopted): «Когда речь о веществе или способе лечения, имеется
  в виду сила действия средства, а не юридическая сила.» instead of «… по-русски уместнее «действенность» или
  «эффективность», а не юридическая сила.», and «… а сила действия не означает успеха» instead of «… а действенность не
  означает успеха». Line 29 keeps «действенность», the published gloss of kanji/効 («эффективность; действенность»).
- `清い` (lines 16 and 20; comprehensibility C7): «чистый, незамутнённый» instead of «чистый, прозрачный», and «С гор
  стекает чистая, незамутнённая вода.» instead of «… чистая, прозрачная вода.»
- `送料` (lines 44–45; comprehensibility C1, partially adopted): «То, что викторина не предлагает рядом с 送料 общие слова о
  цене и расходах, / не означает, что эти денежные слова взаимозаменяемы в любом счёте или предложении.» instead of «Защита
  теста от общих слов о цене и расходах не утверждает, / что …». The sentence was reworded, not deleted, because EN keeps
  an equivalent quiz sentence and published 大事:40 keeps a parallel translated quiz remark.
- `さわやか` (lines 31 and 35–36; comprehensibility C10, consistency O2, correctness optional): a space after the すっきり,
  はきはき and ぺらぺら links.
- `透き通る` (line 42) and `澄む` (line 45) (consistency O3): the redundant `（はっきり）` after the `[はっきり](はっきり.md)` link
  removed.

The comprehensibility reviewer's C2 (通貨:42) and C9 (さわやか:21) were not adopted, nor were its wordings «разошёлся»
(すれ違う), «в обратную сторону» (逆さ) and «путь для прохода» (通路), its deletion of the 送料 sentence or its line-29 change
in 効力; its optional notes (通用's verbal title, 澄む's state reading, the 有効 and 知らせ overlaps, 紙幣 and 札, 成立 and 教育,
解放されて, 透き通る's lead and さわやか «в комнату») led to no action. The consistency reviewer's O1, O4 and O5 led to no
action; O3 was applied to this batch only. The dispositions gave the reasons (see the reconciliation table).

The coordinator's post-fix title screen of the three changed titles is recorded in its dispositions (8 `OK` lines for
guarded pairs, 51 stem-only `!!` lines, no unguarded exact overlap). The exact title segments that a changed title shares
with another card are all guarded: 成立's «образование» with 教育 «образование; обучение» by the RU exclusion 成立→教育, and
its «заключение» with 結論 «заключение; итоговый вывод» by EN. 成立→納得 no longer rests on an exact segment and stays as a
conservative guard for «состоятельность (довода)» near 納得 «убеждённость; принятие (доводов)». 逆さ has no exact hit, and
通路's «проезд» meets 通行 «движение; проезд» only as a stem; 通路 excludes 通行 in EN. Fix 1 adds no link and removes none:
the changed link lines (さわやか:31 and 35–36, 透き通る:42 and 澄む:45) change only spacing and the text after the link, and
their targets are unchanged. There were no RU-only links at the candidate, and there are none after fix 1.
`tools/validate.py` reported 0 errors, the unit tests (124) passed and `link_parity.py` on the 12 changed cards was clean
before the fix commit.

Net change from the candidate:
- titles and H1s of 成立, 逆さ and 通路;
- example translations in 出勤, すれ違う, 通り掛かる and 清い;
- prose in 通り掛かる (line 45), 効力 (lines 24–25 and 42), 清い (line 16) and 送料 (lines 44–45);
- formatting in さわやか, 透き通る and 澄む;
- no exclusion or link change.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`5218a9a..1d78dd8 -- words` is twelve word files, 22 lines added and 22 removed; with `manifest.json` the commit changes
13 files, 35 lines added and 35 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs; the
initial reports state that the model is not verifiable from inside the session.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. No recheck raised a new finding, so there was no fix 2.

Each reviewer appended its recheck to its own report file. Each brief included the full words diff `5218a9a..1d78dd8`, the
coordinator's evidence and rationale for the edits (the post-fix screen and the reasons for the declined items) and that
reviewer's original verdicts with their dispositions. The correctness section records that it read the complete recheck
message, the actual fix diff and all twelve revised cards in full; the consistency section records the reviewed paths as
the 12-card words diff plus `manifest.json`; the comprehensibility section reconciles each of its findings against the
cited passages. The recheck sections do not reproduce the briefs, so this record does not claim their further contents.

All three rechecks state that no generator was run. The correctness and consistency reviewers each ran
`tools/validate.py` (0 errors each); the comprehensibility reviewer did not re-run the validator. Each recheck section
records snapshot `1d78dd8` with a clean tree. After the three rechecks the coordinator confirmed, read-only, that the RU
checkout is on `full-ru-233-words-72` at HEAD `1d78dd8417644049b0d391cf73eb660425bb93ea` (`git rev-parse HEAD`) and that
`git status --porcelain --ignored` prints nothing, so no tracked, untracked or ignored file was left by the rechecks.

### Round 1 (`1d78dd8`)

| Facet | Scope and result |
|---|---|
| Correctness | Snapshot `1d78dd8`, parent exactly `5218a9a`, clean tree at start and end. Read the complete recheck message, the actual fix diff and all twelve revised cards in full; compared changed meanings with frozen EN and prior source evidence, and freshly checked the exact JMdict-backed API entries for 逆さ, 通路, 出勤, 通り掛かる, 清い and 効力. F1 is **resolved**: 成立:4,12 now retain formation, agreement-conclusion and argument-validity; removing law enactment from the short title is acceptable, because it remains explicit at :23–24 and :43 and is not a lost core branch. The optional さわやか spacing is **resolved**. No regression: 逆さ's back-to-front is an attested orientation, not a new motion claim, and the body keeps reversed order; 通路's «проезд» restores EN's and the dictionary's vehicle-compatible scope without changing the aisle examples; 出勤's «приступаю к работе в девять» is acceptable as reporting for duty at nine and removes the "by nine" and home-departure ambiguities (not a universal synonym); すれ違う now makes reciprocal passing explicit without changing tense or roles; 通り掛かる's «случайно» makes "happen to pass by" explicit while :43–44 still exclude an accidental whole journey; 効力's «сила действия» preserves efficacy/potency against legal force; 清い's «незамутнённый» preserves clear water; 送料:44–45 retains the warning against unrestricted interchangeability; 澄む:45 and 透き通る:42 remove only redundant kana readings. Validator 0 errors. Correctness **CLEAN** and scoped coverage **CLEAN** across the original 30-card scope, carrying forward the unchanged-card review; no new actionable defect. |
| Consistency | Snapshot `1d78dd8` with a clean tree before and after; reviewed the 12-card words diff plus `manifest.json`. Title equals H1 for 成立, 逆さ and 通路 (scripted exact comparison). New segments: 成立's «состоятельность (довода)» shares only a stem with お金持ち, 金持ち and 破産 («несостоятельность»), different in sense, so no guard is needed; 逆さ's «задом наперёд» meets no other title; 通路's «проход или проезд» meets 通行 «движение; проезд», which 通路 excludes in EN, and 通過 is RU-guarded. The other edits change body or translation text only; no link target changed and no link was orphaned; 送料 no longer uses «Защита теста». The manifest hashes of all 12 changed cards match the tree, and the batch path set is unchanged. O1 stays optional (EN also leaves 透明 plain); O2 is **resolved**; O3 is **resolved** in 澄む and 透き通る, with the same pattern in four published cards out of scope and unchecked; O4 is resolved with no action (the set is unchanged at 10, all EN exclusions are kept, 成立→教育 stays justified and 成立 has no unguarded exact overlap); O5 stays optional. Validator 0 errors. Consistency, quiz safety and scoped integration are **CLEAN**, with no open findings. |
| Comprehensibility | Snapshot `1d78dd8`, parent `5218a9a`, empty `git status --porcelain`; re-read the 12 changed cards' cited passages, the head of kanji/効, the 効果 and 通行 titles and 大事:40, not all 30 cards. C1 is **resolved**: «Защита теста» is gone, the new sentence is ordinary Russian, and the reviewer does not maintain deletion. C2 is **withdrawn**: «ответами в викторине» translates the EN sentence and matches published 大事:40. C3, C4, C7 and C10 are **resolved** as proposed. C5 is **resolved** in the adapted wording; the reviewer does not maintain «разошёлся», which would blur the card's second sense «разминуться». C6 is **resolved**: lines 24–25 and 42 now say «сила действия», and line 29 «действенность» matches published kanji/効, so the reviewer does not maintain changing it. C8 is **resolved**: «задом наперёд» drops bare «наоборот», and the reviewer does not maintain «в обратную сторону», which would imply motion. C9 is **withdrawn**: an isolated example needs a subject, EN has "He", and the voice-quality point is unchanged. C11 is **resolved**: «проход или проезд» matches line 16, «путь для прохода» stays people-only, and the «проезд» overlap with 通行 is no regression because lines 40–41 still say 通行 is the movement, not the place. No regression in the 成立 title (EN order, law enactment still at lines 24–25 and 43, the 教育 overlap qualified and excluded) or in the 透き通る and 澄む edits. The optional notes stay optional. Comprehensibility and scoped coverage are **CLEAN**, with no new finding. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 成立's title and H1 drop argument validity (minor, scoped coverage) | **Resolved** | `成立.md:4,12`; JMdict 1375880 sense 3 "being valid (of a theory, argument, etc.)"; EN "formation; conclusion; validity"; the body keeps law enactment (:23–24, :43). |
| Correctness optional: missing spaces after the comparison links in さわやか:30–36 | **Resolved** (with consistency O2 and comprehensibility C10) | `さわやか.md:31,35–36`. |
| Consistency optional O1: 透明 compared but unlinked in 透き通る | **Optional, not adopted**; kept optional at recheck | EN also leaves it unlinked, and the RU rules do not require new links beyond EN parity; the reviewer did not find it a defect. |
| Consistency optional O2: さわやか spacing after the すっきり and はきはき links | **Resolved** (duplicate of comprehensibility C10) | `さわやか.md:31,35–36`. |
| Consistency optional O3: redundant `（はっきり）` after the はっきり link in 澄む and 透き通る | **Resolved** for this batch | `澄む.md:45`, `透き通る.md:42`; EN has no such reading. The same pattern in the published cards トランプ, 宝石, 実は and 寧ろ is out of scope and recorded for the Issue #7 follow-up list. |
| Consistency O4: classification of the ten RU-added exclusions | **Agreed**; all kept; no action at recheck | See the final exclusion set below. |
| Consistency optional O5: the declined pairs 通り掛かる–たまたま/偶然/出会う, 妥当–申し訳/よろしい, 透明–見える, 通勤–通学, 解放–空く, 送料–配達 and 通帳–貯金 | **Optional, not adopted**; kept optional at recheck | The reviewer judged their titles visibly different and acceptable unguarded. |
| Comprehensibility C1: 送料:44–45 «Защита теста…» is app-test meta (minor) | **Resolved** (partial adoption: reworded, not deleted) | `送料.md:44–45`; EN keeps an equivalent quiz sentence; published 大事:40; the reviewer does not maintain deletion. |
| Comprehensibility C2: 通貨:42 «ответами в викторине» (minor) | **Withdrawn** at recheck (declined) | EN line 45 says the labels are not "mutually exclusive quiz answers"; published 大事:40 keeps a parallel remark. |
| Comprehensibility C3: 出勤:19 «выхожу на работу к девяти» (minor) | **Resolved** | `出勤.md:19`; 九時に marks the time of the action; the card's note concerns starting work. |
| Comprehensibility C4: 通り掛かる:21 and :45 drop the chance element (minor) | **Resolved** | `通り掛かる.md:21,45`; JMdict sense 1 "to happen to pass by"; EN "happened to". |
| Comprehensibility C5: すれ違う:20 shows one person passing (minor) | **Resolved** (adapted wording); «разошёлся» not maintained at recheck | `すれ違う.md:20`; Jisho すれ違う sense 1 "to pass (by) each other". |
| Comprehensibility C6: 効力:24–25, 29 and 42 point to 効果's glosses (minor) | **Resolved** (partial adoption); keeping line 29 accepted at recheck | `効力.md:24–25,42`; line 29 «действенность» is the published gloss of kanji/効 («эффективность; действенность»). |
| Comprehensibility C7: 清い:16 and :20 «прозрачный» is 透明's lead gloss (minor) | **Resolved** | `清い.md:16,20`; 透明 «прозрачный; видимый насквозь». |
| Comprehensibility C8: 逆さ bare «наоборот» (minor; medium confidence) | **Resolved** (adapted wording); «в обратную сторону» not maintained at recheck | `逆さ.md:4,12`; Jisho 逆さ sense 1 "inverted; upside down; reversed; back to front"; the body already uses «задом наперёд». |
| Comprehensibility C9: さわやか:21 «Он» adds a subject (minor; medium confidence) | **Withdrawn** at recheck (declined) | EN "He"; a subjectless Russian past-tense sentence reads as a fragment in an isolated example; the voice-quality point is unchanged. |
| Comprehensibility C10: さわやか:31 and 35–36 missing spaces (minor) | **Resolved** | `さわやか.md:31,35–36`. |
| Comprehensibility C11: 通路 «проход для людей» reads as pedestrian-only (minor) | **Resolved** (adapted wording); «путь для прохода» not maintained at recheck | `通路.md:4,12`; line 16 (people or vehicles); JMdict 1433600 sense 1; EN "passageway". |
| Comprehensibility optionals: 通用's verbal title, 澄む's state reading, the 有効 and 知らせ overlaps, 紙幣 and 札, 成立 and 教育, 解放されて, 透き通る's lead and さわやか «в комнату» | **Optional, not adopted**; kept optional at recheck | The reviewer classed them as acceptable. |
| Consistency initial limit: 118 `strokes/*.json` entries hash differently from the Windows working tree | **Not a defect**; pre-existing and outside the batch | `tools/build_manifest.py` hashes text files after CRLF→LF normalisation, and the 118 CRLF files are the stroke JSON byte copies committed under `.gitattributes` (`strokes/*.json -text`), as established at Batch 232. A read-only rehash of the 1d78dd8 blobs for these records matched all 5,104 `files` entries after
normalisation; exactly 118 blobs contain CRLF, all `strokes/*.json`. The reviewer attributed the difference to line endings and did not re-run the check at recheck; fix 1 touches no `strokes/` file. |

Cross-batch note: links to absent targets stay plain. Four EN link targets in this batch's new cards (6 occurrences) are
absent from RU: the kanji cards 貨 (from 通貨), 訳 (from 通訳), 清 (from 清い and 澄む) and 逆 (from 逆さま and 逆さ). The other
written kanji without an RU kanji card, 幣, 妥, 循, 環, 帳, 這, 透 and 澄, have none in EN either. No links were held from
Batch 232, and none is held from this batch.

## Final exclusion set

All 165 EN exclusion entries (29 lists; 通帳 has none) are retained in EN order. Ten direct, one-sided entries are added on
seven new cards (no new list), all at the candidate; fix 1 added and removed none:

- Required or justified (5): 通路→通過, 成立→教育, 通用→過ぎる, 時速→高速 and 速力→高速 (成立→教育 and 通用→過ぎる added by
  the coordinator after its title screen, with 成立→納得 below).
- Conservative, harmless (4): 速達→郵送, 成立→契約, 成立→納得 and 通用→納得.
- Weakest (1): 出勤→就職, kept for the author's reason that «выход на работу» can be read as starting a job, near 就職
  «трудоустройство; поступление на работу».

Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added; the targets do not declare these pairs back.

## Final bounded verdicts

- Correctness: **CLEAN** throughout for all 30 cards.
- Scoped coverage: **CLEAN** after fix 1 (成立's title, F1).
- Comprehensibility: **CLEAN** after fix 1 (通路, 効力, 出勤, すれ違う, 通り掛かる, さわやか, 清い, 逆さ and 送料); C2 and C9 were
  withdrawn, and the optional notes remain optional.
- Cross-file consistency: **CLEAN** throughout; there are no RU-only links, and the three restored navigation links of the
  candidate stand.
- Quiz safety: **CLEAN** throughout, including the 成立, 逆さ and 通路 retitles. This covers the reviewed batch and the
  directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them; the comprehensibility recheck did not
  re-read the other 18 cards or re-query JMdict. The unchanged cards rest on review 001, in which all three reviewers read
  all 30 cards in full against EN.
- The correctness recheck was a bounded diff recheck with fresh JMdict-backed entries for six headwords only; it did not
  independently re-run the author-reported unit tests or title screen or perform comprehensive quiz adjudication, and its
  original evidence and model limitations remain. The consistency reviewer performed no dictionary lookups, its title
  screen relied on reading, targeted comparison and the author's screen plus a targeted grep of the new segments (not an
  exhaustive tool run), and its necessity classes are judgements, not measurements; it did not check the four published
  cards with the `（はっきり）` pattern or re-run the strokes line-ending check. The comprehensibility recheck did not re-run
  `validate.py`.
- The correctness reviewer's Gramota requests intermittently returned HTTP 429 and a Jisho `/word/逆さま` request failed;
  only successfully inspected entries support its conclusions. The comprehensibility reviewer could not open JMdictDB
  (password required) and relied on the Jisho API display of JMdict.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `5218a9a`, not `1d78dd8`.
- The `（はっきり）` pattern in four published cards is left for the Issue #7 follow-up list.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
