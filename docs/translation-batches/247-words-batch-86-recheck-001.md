# Batch 247 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `83b26408e9899c14813ea3226de3a04c72164abf` | `96d36fd6130dc64d3cb202f00e98df2330547687` | Initial review snapshot: the signed candidate, on `origin/full-ru-247-words-86`. |
| `9c5a6a4ddf1e8d5ba5d58d28bb75fa0bac50ff79` | `542f32957ba9896754688ed06adaabd93f62bbea` | Fix 1 (final candidate). It covers correctness C1 and S1 and comprehensibility F1–F5 and F7–F12 (F1, F2, F4, F5, F7, F10 and F12 with modification), plus the optional notes on 真空's «сосуд» and 直通's «номер прямой связи». It retitles たちまち, 直前, 先頭 and しょうがない, rewrites example translations and prose in 看病, たちまち, 真空, 直通, しょうがない, 直後, 直前, 目覚まし, 倣う, はじめに and 垂直, and changes no link, exclusion or navigation-only file. Signed; on `origin/full-ru-247-words-86`. |

The fix regenerated `manifest.json`; both snapshots record 5,529 entries (5,524 `files` + 3 images + 2 scenes).
`contentVersion` is `6cfe11c9d4ba290e` at the candidate and `07e0fa723a162974` after fix 1. The intake was not
refreshed; it still records the candidate's payload hashes. The commit message reads "Batch 247 fix 1: apply
blind-review dispositions", followed only by the co-author trailer.

Fix 1:
- `看病` (line 19; correctness C1, verbatim): «Я не пошёл на работу, чтобы ухаживать за больным отцом.» instead of «Я
  взял отгул для ухода за больным отцом.»
- `たちまち` (lines 4, 12 and 19; correctness S1): title and H1 «в мгновение ока; внезапно» instead of «в мгновение ока;
  моментально»; the example reads «Небо вдруг потемнело.» instead of «Небо моментально потемнело.»
- `真空` (lines 18 and 33; the consistency optional on «сосуд» and comprehensibility F1, with modification): «Мы создали
  вакуум внутри контейнера.» instead of «…внутри сосуда.»; «Daijisen фиксирует и переносное значение — пустоту или
  бездействие. Но это не значит, что любое русское «пустой» можно перевести как 真空.» instead of «Daijisen фиксирует и
  переносную пустоту или бездействие; эти расширения не превращают любое русское «пустой» в 真空.» The candidate-time
  follow-up edit on line 29 is untouched.
- `直前` (lines 4, 12 and 34; comprehensibility F3, and F2 with modification): title and H1 «непосредственно перед; прямо
  перед» instead of «непосредственно перед (по времени); прямо перед (в пространстве)»; «В исходном списке слов указано
  временное значение; пространственное приведено здесь дополнительно.» instead of «Исходный список закрепляет временное
  значение; пространственное — дополнительное учебное.»
- `直後` (line 32; comprehensibility F4, with modification): «Это значение взято из Daijisen: в записи JMdict, указанной
  ниже, есть только значение «сразу после».» instead of the coordinator's candidate wording «Это значение подтверждено
  отдельным источником: в основной закреплённой словарной записи есть только значение «сразу после».»
- `目覚まし` (line 16; comprehensibility F5, with modification): «目覚し (так слово записано в исходном списке слов) и
  目ざまし — записи того же слова めざまし.» instead of «目覚し — запись из исходного списка — и 目ざまし являются записями той
  же статьи めざまし.»
- `先頭` (lines 4 and 12; comprehensibility F7, with modification): title and H1 «начало ряда; передняя часть; место во
  главе» instead of «начало ряда (очереди); передняя позиция; место во главе».
- `しょうがない` (lines 4, 12 and 21; comprehensibility F9 and F8, verbatim): title and H1 «ничего не поделаешь;
  безнадёжный; невыносимо» instead of «…; до невозможности»; the example reads «Ну и безнадёжный же человек.» instead of
  «Ну и безнадёжный же ты человек.»
- `倣う` (line 21; comprehensibility F10, rewritten rather than deleted): «По-русски говорят «брать что-либо за образец» с
  винительным падежом, но при 倣う образец отмечается に, а не を.» instead of «Русское «перенимать что-либо» с прямым
  дополнением не означает, что здесь нужно механически ставить を.»
- `はじめに` (line 21; comprehensibility F11, verbatim): the second sentence «Ни тот, ни другой не означает представления
  одного человека другому.» is deleted; the line now reads «Первый пример упорядочивает действия, второй называет часть
  книги.»
- `垂直` (line 33; comprehensibility F12, with modification): «Не переводите каждое 垂直 словом «вертикальный»: две
  наклонные линии тоже могут быть перпендикулярны друг другу.» instead of «Не переводите каждое 垂直 как «стоящий прямо
  на странице». Две наклонные линии могут быть перпендикулярны друг другу.»
- `直通` (line 19; comprehensibility optional, verbatim): «Это прямой номер ответственного сотрудника.» instead of «Это
  номер прямой связи с ответственным сотрудником.»

All twelve are new Batch 247 cards. No navigation-only file changed, so navigation stays at 3 files / 5 links, all
EN-position restorations. 真っ白, the other card carrying a candidate-time follow-up edit, is unchanged.

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Comprehensibility F1 was accepted with modification: "The opening sentence is kept."
- Comprehensibility F2 and F5 were accepted with modification: "The source-list reference is a deck convention (49
  occurrences in published RU words/kanji; 82 "source list" mentions in EN), so it is kept but made readable". The same
  change answers the correctness optional and consistency optional 4 on this wording; at recheck the correctness reviewer
  recorded both notes "PARTIALLY RESOLVED, still OPTIONAL/outside facets" and the consistency reviewer recorded 4
  "RESOLVED".
- Comprehensibility F4 was accepted with modification: "The source qualification is kept (EN "separately sourced
  recognition") but names the sources instead of "the pinned principal entry"."
- Comprehensibility F7 was accepted with modification: the new title "keeps all three EN senses ("head of a line; front;
  lead") in shorter form; «передняя часть» matches the 頭 kanji and word cards' gloss of 先頭." The dispositions also
  record: "The reviewer's claim of an unexcluded «передняя» overlap with 正面 is incorrect: 先頭 already excludes 正面 and
  前, and 正面 «передняя сторона; фасад» shares no exact segment." At recheck the comprehensibility reviewer recorded
  "«передняя часть» is not 正面's «передняя сторона», and 先頭 excludes 正面."
- Comprehensibility F10 was accepted with modification (rewrite, not delete): "The EN warning ("English 'imitate
  something' does not justify mechanically using を") is an L1-interference rule that applies to Russian too, because the
  card's own title «брать за образец» takes an accusative object; the rewrite states the rule plainly."
- Comprehensibility F12 was accepted with modification: "The following sentence on local horizontal is kept."
- Comprehensibility F6 (真っ白 title) was declined: "«незаполненный» renders JMdict/EN "blank"; line 16 explains blank
  paper and a blank mind, and the line 19 example teaches the mind sense. The suggested «ни записи, ни мысли» is not a
  gloss". At recheck the reviewer withdrew F6: "The declined title was not a gloss."
- Consistency optional 3 (相互 adjectival title) was declined: "«взаимный; обоюдный» follows EN "mutual; reciprocal";
  the body teaches 相互の and 相互に." Consistency optional 5 (直線→直通 over-guard) was kept: "Harmless; it also guards
  the 直通–直線 pair raised by the comprehensibility reviewer."
- The comprehensibility optionals were declined or needed no action: the たちまち link to 徐々に ("EN leaves 徐々に
  unlinked; kept for link parity."); 相互:18 «на взаимной основе», the 着せる title and a 正面:33 まとも lead-in ("Correct
  Russian and faithful to EN; no learning defect shown."); the missing exclusions ("以後 already excludes 以降 and Android
  applies exclusions in both directions; 直線→直通 guards 直通–直線; 相撲 and 直径 have no exclusions in EN and no
  overlapping titles were shown."). The 看病 «отгул» optional was handled with C1.

Post-fix screen: a saved rerun at the committed `9c5a6a4` over all 30 batch words (`b247-postfix-screen.txt`, 311 lines)
has 42 `OK` lines for pairs already guarded by an exclusion and 269 `!!` lines. Its only exact-segment lines are
たちまち–急に and たちまち–突然 («внезапно»), both `OK` because たちまち's own list excludes 急に and 突然. Against the
candidate screen (357 lines) it removes 113 lines and adds 67, all on the four retitled words: 先頭 51 removed and 52
added, 直前 46 and 8, たちまち 10 and 5, しょうがない 6 and 2. The dispositions record for 直前 and 先頭 "Title screen: no
exact-segment overlap.", and for しょうがない that "たまらない «невыносимый; неотразимый» shares a stem but no exact
segment and is already excluded."

Net change from the candidate:
- titles and H1s of たちまち, 直前, 先頭 and しょうがない;
- example translations in 看病, たちまち, 真空, しょうがない and 直通;
- prose in 真空 (line 33), 直前 (line 34), 直後 (line 32), 目覚まし (line 16), 倣う (line 21), はじめに (line 21) and 垂直
  (line 33);
- no exclusion added or removed;
- no link added, removed or retargeted.

No Japanese example sentence, sourced reading, kanji card, EN exclusion or link target changed; the only new Japanese
characters are the 倣う and に mentions in 倣う:21. The content diff `83b2640..9c5a6a4 -- words` is 12 word files, 20
lines added and 20 removed; with `manifest.json` the fix changes 13 files, 33 lines added and 33 removed.

Fix 1 validation, as recorded in the dispositions: "`tools/validate.py` 0 errors; manifest rebuilt (5,529 files incl. 3
images and 2 scene catalogs); 124 unit tests OK; content budget OK; `git diff --check` clean; link parity unchanged from
the candidate (33 paths, no LOST or EXTRA link); title screen: the only exact-segment hits on retitled words are
たちまち–急に and たちまち–突然 («внезапно»), both excluded. Other matches are stem-only and topical." For this record link
parity was verified again over the 33 batch paths at `9c5a6a4` ("checked 33", no LOST and no EXTRA link), and the link
targets in the fix diff were compared: fix 1 adds, removes and retargets none.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the recheck reports make no statement about model identity, and in review 001 the correctness report said "Model
identity not verifiable." and the comprehensibility report "Model: not verifiable."; the dispositions label each
reviewer's model "per runtime status".

The rechecks ran serially, one reviewer at a time, in one round: comprehensibility, then correctness, then consistency,
each on the fix diff `83b2640..9c5a6a4` (12 word files and `manifest.json`). The initial reviews had run correctness,
then consistency, then comprehensibility. These orderings rest on the coordinator's session records; the recheck reports
do not record times. There was no second fix and no follow-up exchange.

Rechecks were returned as separate reports rather than appended to the initial review files: the full texts are in
`b247-recheck-correctness.md`, `b247-recheck-consistency.md` and `b247-recheck-comprehensibility.md` in the
coordinator's session folder, and their content is recorded in the round table below. The recheck briefs were sent
through the agent-messaging channel and were not saved as files; each recheck's scope is described here from its own
Snapshot and Scope lines.

No recheck ran a generator. The correctness reviewer records "No repository edits, staging, commits or generators." and
"Only this new report was written."; the consistency reviewer records "No generators run; validate.py not re-run by me
this round."; the comprehensibility recheck makes no statement about generators or the validator. The correctness
recheck records `9c5a6a4ddf1e8d5ba5d58d28bb75fa0bac50ff79` against `83b26408e9899c14813ea3226de3a04c72164abf` with
"HEAD matches and `git status --porcelain` is empty before and after review."; the consistency recheck records HEAD
`9c5a6a4ddf1e8d5ba5d58d28bb75fa0bac50ff79` with "`git status --porcelain` empty before and after"; the
comprehensibility recheck records `9c5a6a4ddf1e8d5ba5d58d28bb75fa0bac50ff79` with "git status --porcelain empty before
and after this report." The untracked `tools/__pycache__/` that the initial consistency review's validator run created
had been deleted by that reviewer before its report was finished. When these records were drafted, a read-only check
showed the RU checkout at HEAD `9c5a6a4ddf1e8d5ba5d58d28bb75fa0bac50ff79` with `git status --porcelain --ignored`
printing nothing.

### Round 1 (`9c5a6a4`)

| Facet | Scope and result |
|---|---|
| Comprehensibility | `9c5a6a4`, porcelain empty before and after; "Prior review was 83b26408." "recheck of F1–F12 and optional notes against the fix-1 diff and the changed passages in context. Facets: comprehensibility, scoped coverage." F1–F5 and F7–F12 **resolved**, for example F1 "now names a figurative sense and says not every «пустой» is 真空. The target is clear."; F2 "The list name remains, but it no longer hides whether «прямо перед» is real."; F4 "The spatial sense is secondary, not unofficial."; F7 "«очереди» is gone. «передняя часть» is not 正面's «передняя сторона», and 先頭 excludes 正面. Body lines 16–18 still match."; F9 "Line 20 keeps the idiom «до невозможности»; line 23 still shows the construction. たまらない stays excluded."; F10 "uses the card's own «брать за образец» and states に, not を. «перенимать» is gone."; F11 "The English-only warning is deleted. Line 15 and the 紹介 contrast remain." F6 **withdrawn**: "words/真っ白.md:4 unchanged. Line 16 already glosses «незаполненный» as blank paper or a mind with no thought; line 18 teaches the mind use. The declined title was not a gloss." Optional: "看病:18 resolved («Я не пошёл на работу…»). 真空:16 resolved («контейнера»). 直通:18 resolved («прямой номер»)." (the changed lines are 看病:19, 真空:18 and 直通:19); "徐々に link declined — still plain text at たちまち:29; no defect (EN parity). 相互:18, 着せる title, 正面:33 declined; no defect. Exclusion notes withdrawn: the guarded pairs are already excluded, including both ways for 以降/以後." "New findings: none. Retitles checked against body and examples … No lost teaching point and no new unclear remark." Verdicts: "comprehensibility CLEAN; scoped coverage CLEAN." Limits: "dictionaries not re-opened; title screen not re-run. Manifest excluded from the diff." |
| Correctness | `9c5a6a4` against `83b2640`, porcelain empty before and after. "Read all twelve revised words/<name>.md files in full"; "Checked every changed passage in context against Japanese and actual dictionary entries. This is a delta recheck, carrying forward the full original 30-card bilingual review, not a new full-batch audit." "C1 — RESOLVED" (Daijisen 休む sense 4 欠席・欠勤する; "看病 remains patient care"); "S1 — RESOLVED" ("JMdict senses 1 and 2 support both title segments."). Source-list notes on 直前:34 and 目覚まし:16 "PARTIALLY RESOLVED, still OPTIONAL/outside facets". Regression checks of every changed passage, including the four retitles, 真空:18 ("faithful to 容器") and :33 ("retains Daijisen sense 2, not an invented JMdict figurative sense"), 直後:32 ("accurately names its sources"), 倣う:21 ("corroborated by Daijisen 前例に倣う and JMdict's intransitive godan classification. It does not ban を elsewhere in a sentence."), 垂直:33, はじめに:21 ("only removes an English-dependent “introduction” warning"), しょうがない:21, 直通:19 and 看病:19. "all 26 Japanese example/kana prefixes unchanged"; "all 84 literal Markdown links/citations unchanged"; "Runtime `git diff --check` passed." Reopened: the Jisho/JMdict API for all twelve words, Digital Daijisen via weblio.jp for 真空, 直後, 直前, 垂直, 直通, 休む and 倣う, and the pinned n2.csv IDs 1431330 and 1535340; "No network requests failed." Verdicts: "Correctness: CLEAN. Scoped coverage: CLEAN." "CLEAN does not certify exhaustive/native correctness." New findings: "None." Limits: "No fresh kanjiapi, Bunpro, Russian dictionary or native-speaker check; their unchanged claims retain the original review's evidence. Manifest, unrelated cards, exhaustive title collisions and comprehension beyond the optional notes were not re-audited." |
| Consistency | HEAD `9c5a6a4`, porcelain empty before and after. "Diff 83b2640..9c5a6a4 (manifest excluded): 12 word cards, 20 lines changed, nothing else." "Read the full fix diff (-U0). Programmatic checks over all RU word titles (exact titles, «;»-segments, shared stems), H1 vs title, front matter and link lists of the 12 cards in both commits, grep of the whole repo for old titles/sentences, manifest hashes (CRLF-normalised, all 5524 recomputed)." Optional notes: 1 "RESOLVED"; 2 "RESOLVED"; 3 "UNRESOLVED, left as optional polish (not in the fix; body explains). Acceptable."; 4 "RESOLVED"; 5 "OPTIONAL, unchanged (harmless)." Retitles: たちまち «внезапно» "shared with 急に and 突然 (both guarded, declared from たちまち)", びっくり stem-only and "not a defensible answer"; 直前 and 先頭 "no exact segment shared with any title"; しょうがない «невыносимо» "appears only in たまらない «невыносимый» (stem), guarded." "H1 = title on all 12 changed cards"; "repo-wide grep finds none outside the changed cards. kanji/頭.md (L20, L32, L40) and words/頭.md (L33, L48) quote 先頭 as «передняя часть; начало ряда» / «передней части очереди или группы»: still consistent with the new title."; "quiz_exclusions unchanged."; manifest: "only contentVersion and exactly the 12 changed entries differ from the candidate; no added or removed keys; all 5524 hashes match the working tree after CRLF normalisation." Verdicts: "Consistency: CLEAN"; "Quiz safety: CLEAN (one optional note)"; "Integration / manifest: CLEAN". New findings: "None required. Optional: the unguarded pair 直前/先頭 («прямо перед» vs «передняя часть») could be guarded if the team wants maximal strictness." Limits: "Russian quality not judged; validate.py not re-run by me; quiz-overlap scan is heuristic (segments and 5-letter stems)." |

No recheck raised a new finding. The consistency reviewer's one new optional note, an exclusion between 直前 and 先頭, was
not acted on, for the reviewer's own reason: "直前 is time-led and the spatial segment «прямо перед» is not a fair gloss of
先頭; optional low-risk note only." There was no second fix.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 看病:19 «взял отгул» narrows 仕事を休みました (low) | **Resolved** | `看病.md:19`; Daijisen 休む sense 4; correctness recheck "C1 — RESOLVED". |
| Correctness S1: たちまち title drops "suddenly" (low; scoped coverage) | **Resolved** | `たちまち.md:4,12,19`; JMdict 1288480 senses 1 and 2; correctness recheck "S1 — RESOLVED". |
| Correctness optional: «исходный список» in 直前:34 and 目覚まし:16 | **Partially resolved**; optional | `直前.md:34`, `目覚まし.md:16`; correctness recheck "PARTIALLY RESOLVED, still OPTIONAL/outside facets". |
| Consistency optional 1: たちまち lacks "suddenly" | **Resolved** (with S1) | Consistency recheck "RESOLVED". |
| Consistency optional 2: 真空:18 «сосуд» vs 容器 «контейнер; тара» | **Resolved** | `真空.md:18`; consistency recheck "RESOLVED". |
| Consistency optional 3: 相互 adjectival title | **Optional**; declined (EN parity) | Consistency recheck "UNRESOLVED, left as optional polish (not in the fix; body explains). Acceptable." |
| Consistency optional 4: author-process wording in 直前 and 目覚まし | **Resolved** (with F2/F5) | Consistency recheck "RESOLVED". |
| Consistency optional 5: 直線→直通 over-guard | **Optional**; kept | Consistency recheck "OPTIONAL, unchanged (harmless)." |
| Consistency recheck optional: unguarded 直前/先頭 | **Optional**; no action | The reviewer judged «прямо перед» "not a fair gloss of 先頭". |
| Comprehensibility F1: 真空:33 calque (medium) | **Resolved** (with modification) | `真空.md:33`; Daijisen sense 2 per the correctness recheck. |
| Comprehensibility F2: 直前:34 source-list reference (medium) | **Resolved** (with modification) | `直前.md:34`; comprehensibility recheck "F2 resolved". |
| Comprehensibility F3: 直前 title is a definition (medium) | **Resolved** | `直前.md:4,12`; line 16 temporal, line 33 spatial. |
| Comprehensibility F4: 直後:32 editor metadata (medium) | **Resolved** (with modification) | `直後.md:32`; Daijisen sense 2 物のすぐうしろ; JMdict "immediately following" only. |
| Comprehensibility F5: 目覚まし:16 invisible list (low) | **Resolved** (with modification) | `目覚まし.md:16`; n2.csv spelling 目覚し per the correctness recheck. |
| Comprehensibility F6: 真っ白 title lacks the blank-mind sense (medium) | **Withdrawn**; title unchanged | Comprehensibility recheck "The declined title was not a gloss." |
| Comprehensibility F7: 先頭 title length and «передняя» overlap (medium) | **Resolved** (with modification) | `先頭.md:4,12`; 先頭 excludes 正面 and 前; no exact segment shared. |
| Comprehensibility F8: しょうがない:21 adds «ты» (medium) | **Resolved** | `しょうがない.md:21`. |
| Comprehensibility F9: «до невозможности» in the title (low) | **Resolved** | `しょうがない.md:4,12`; たまらない excluded. |
| Comprehensibility F10: 倣う:21 rejects an ungiven gloss (medium) | **Resolved** (rewritten, not deleted) | `倣う.md:21`; Daijisen 前例に倣う; JMdict intransitive godan. |
| Comprehensibility F11: はじめに:21 English-only warning (low) | **Resolved** | `はじめに.md:21`; 紹介 contrast remains. |
| Comprehensibility F12: 垂直:33 rejects an ungiven gloss (low) | **Resolved** (with modification) | `垂直.md:33`; JMdict senses 1–2; Daijisen senses 2–3. |
| Comprehensibility optionals: 看病 «отгул», 真空 «сосуда», 直通 «номер прямой связи» | **Resolved** | `看病.md:19`, `真空.md:18`, `直通.md:19`; comprehensibility recheck "resolved". |
| Comprehensibility optionals: 徐々に link, 相互:18, 着せる title, 正面:33 lead-in | **Optional**; declined, no defect | Comprehensibility recheck "declined; no defect". |
| Comprehensibility outside-facet exclusion notes (以降/以後, 直通/直線, 相撲 and 直径) | **Withdrawn** | Comprehensibility recheck "the guarded pairs are already excluded, including both ways for 以降/以後." |
| Coordinator's unverified Russian (подражать governance, «прямая линия» as a phone line) | **UNVERIFIED** by the coordinator; not defects | The correctness review checked both against ru.wiktionary; no Russian dictionary was reopened at recheck. |
| Consistency reviewer's kanji/倣 entry among missing link targets | **Reviewer error**; no action | EN 倣う has no kanji/倣 link; link parity lists nine plain targets without it. |

Cross-batch note: links to absent targets stay plain. Ten EN link occurrences in this batch's new cards, to 9 targets,
are absent from RU: kanji 庁 (from 官庁 and 県庁), 県 (from 県庁), 角 (from 直角) and 線 (from 直線), and words 住まい
(from 相撲), 水平 (from 垂直), 曲線 (from 直線), 一斉 (from たちまち) and 円周 (from 直径). The other written kanji without
an RU kanji card, 倣, 垂, 径, 撲 and 看, have none in EN either. No EN link to an existing card is dropped, and there is no
RU-only link. No link was held from an earlier batch, and none is held for a later one. The five navigation-only
restorations (kanji/着.md lines 38 and 52 and words/被せる.md line 46 to 着せる; words/頭.md lines 33 and 48 to 先頭) are
unchanged by fix 1; kanji/着.md lines 62–63 keep a pre-existing plain mention of 着せる with no EN link counterpart, and
kanji/頭.md (lines 20, 32 and 40) and words/頭.md:33 quote 先頭 as «передняя часть; начало ряда», consistent with the new
title. The published 事情:18 also uses «отгул», outside this batch's scope. Every exclusion target resolves to a card
published at the baseline or to a batch card.

## Final exclusion set

All 156 EN exclusion entries (28 lists; EN has none on 相撲 or 直径) are retained in EN order; 12 of them lie inside the
batch, and the other 144 target existing RU cards. Five direct, one-sided entries are added on four new cards, all
present at the candidate and accepted by the coordinator as "all conservative, direct pairs on new cards only"; fix 1
added or removed none. Each is appended at the end of its list:

- 官庁→機関: `[庁, 局, 事務所, オフィス, 政府, 機関]`;
- 直線→直通 (the only one targeting a batch word): `[線, まっすぐ, 直通]`;
- たちまち→瞬間: `[すぐに, 直ちに, 早速, 急, 急に, 急激, 突然, いきなり, すっと, 一瞬, 一度に, さっさと, 瞬間]`;
- 直前→直に and 直前→直接: `[前, 先, 以前, 直に, 直接]`.

The consistency reviewer classed 官庁→機関 as "warranted", たちまち→瞬間 as "warranted, conservative", 直前→直に/直接 as
"conservative" and 直線→直通 as "weakest … Harmless over-guarding", and kept the last as optional at recheck ("OPTIONAL,
unchanged (harmless)"). The guarded exact-segment pairs in the post-fix screen, たちまち–急に and たちまち–突然, are covered
by EN entries in たちまち's own list. 直前 and 先頭 remain unguarded against each other (consistency recheck optional, no
action). Every RU addition is appended at the end of its list, and no EN entry is removed or reordered. Android applies
each declaration symmetrically (EN `docs/content-format.md`, lines 162–165), so no reverse declarations were added to
baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (看病 C1); CLEAN at recheck.
- Scoped coverage: **CLEAN** after fix 1 in the correctness recheck (たちまち S1); CLEAN throughout in the
  comprehensibility review and recheck.
- Comprehensibility: **CLEAN** after fix 1 (真空, 直前, 直後, 目覚まし, 先頭, しょうがない, 倣う, はじめに and 垂直); the
  modified dispositions of F1, F2, F4, F5, F7, F10 and F12 stand as accepted, and F6 was withdrawn.
- Cross-file consistency: **CLEAN** throughout; the five restored navigation links in three files stand.
- Quiz safety: **CLEAN** throughout, including the four retitles; the five RU additions stand and 直前/先頭 remain
  unguarded as an optional note. This covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct
  pairs, not transitive groups.

## Limits

- The rechecks reread the changed cards or passages and the lines needed to judge them; the unchanged cards rest on review
  001, in which all three reviewers read all 30 cards in full against EN. The correctness recheck was "a delta recheck,
  carrying forward the full original 30-card bilingual review, not a new full-batch audit".
- In review 001 the consistency reviewer read only 14 EN bodies line by line ("The other 16 were checked structurally
  only."), read the title-screen output only in part and did not complete its tag-vocabulary and byte-format scan; the
  comprehensibility reviewer did not reopen JMdict or Daijisen, at review or at recheck. The correctness reviewer's
  Gramota searches returned 429, and its recheck made no fresh kanjiapi, Bunpro or Russian-dictionary check. Necessity
  classes are judgements, not measurements.
- The untracked `tools/__pycache__/` created by the initial consistency reviewer's validator run was deleted by that
  reviewer; the tree was clean at every later check.
- The comprehensibility review's verdict says "ten findings" but lists twelve, and some of its line citations (F8 and
  three optionals) are one or two lines earlier than the candidate's lines; the records use the actual lines.
- The recheck briefs were not saved as files; each recheck's scope is taken from its own report.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fix, so its payload hashes describe the candidate `83b2640`, not `9c5a6a4`.
- Frequency and preferred register (for example подражать governance, «прямая линия» as a phone-line name, «прямой
  номер», «невыносимо» and «внезапно») were not certified. Online dictionaries were current observations, not pinned
  archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
