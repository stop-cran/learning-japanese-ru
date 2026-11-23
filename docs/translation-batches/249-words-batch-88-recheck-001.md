# Batch 249 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `a8e87dd42d8d6fb01c89b03aa12b995550acc585` | `82d39083172fc5e751eed8b92d9932a1a19aa623` | Initial review snapshot: the signed candidate, on `origin/full-ru-249-words-88`. |
| `07ad251170e95ef589e7ec5bd814eb4c99a2bd4d` | `ba1a26718455f095e125af69105081bca0a25032` | Fix 1 (final candidate). It covers consistency Q1 and Q2 and comprehensibility C1–C9, C11 and C12 (C1, C2, C8, C11 and C12 with modification), plus the comprehensibility optional note on 田植え:33; it declines C10 and the other optional notes. It retitles 発つ, rewrites example translations in 留まる and 住まい and prose in 応用, あてはめる, 申請, 役目, 申し訳ない, 発つ, 実用, 原産 and 田植え, adds two exclusions (略す→減らす and 申し訳ない→詫びる), removes four links together with their English-dependent sentences (応用→申し込む, あてはめる→申し込む, 申請→適用 and 役目→行事) and changes no navigation-only file. Signed; on `origin/full-ru-249-words-88`. |

The fix regenerated `manifest.json`; both snapshots record 5,589 entries (5,584 `files` + 3 images + 2 scenes).
`contentVersion` is `ff40e930d163cbc9` at the candidate and `0b5d06675bb7dbf0` after fix 1. The intake was not
refreshed; it still records the candidate's payload hashes. The commit message reads "Batch 249 fix 1: apply
blind-review dispositions", followed only by the co-author trailer.

Fix 1:
- `略す` (line 9; consistency Q1, verbatim): `quiz_exclusions` appends 減らす (`[省略, 省く, 縮める, 抜く, 削除, 詰める,
  略語, 除く, 削る, 飛ばす, 減らす]`).
- `申し訳ない` (lines 9 and 33; consistency Q2, verbatim, and comprehensibility C5): `quiz_exclusions` appends 詫びる; the
  sentence «Не переводите каждое употребление как чувство грусти или как сочувствие чужой беде.» is deleted and the next
  sentence gains its subject: «申し訳ない выражает извинение или извиняющийся ответ на доставленное беспокойство.» instead
  of «Это извинение или извиняющийся ответ на доставленное беспокойство.»
- `応用` (line 33; comprehensibility C1, with modification): «По-русски можно сказать и «применять мазь», но нанесение мази
  или краски — это [塗る](塗る.md)（ぬる）, а не 応用.» instead of «Наносить вещество на поверхность — это
  [塗る](塗る.md)（ぬる）, а подавать заявку — [申し込む](申し込む.md)（もうしこむ）. Эти действия не становятся значениями
  応用. Точно так же прикладная физика — название области, а не заявление о приёме на работу.» The link to 申し込む is
  removed with its sentence.
- `あてはめる` (line 33; comprehensibility C2, with modification): «По-русски можно сказать и «применять мазь», но нанесение
  мази или краски — это [塗る](塗る.md)（ぬる）, а не あてはめる.» instead of «Наносить краску — это [塗る](塗る.md)（ぬる）, а
  подавать заявку на курс — [申し込む](申し込む.md)（もうしこむ）. Это другие действия, а не употребления あてはめる.»; the
  rule-appropriateness sentence is kept. The link to 申し込む is removed with its sentence.
- `申請` (line 33; comprehensibility C3, verbatim): the sentence «Это не «применение» правила или метода, как в
  [適用](適用.md)（てきよう）.» is deleted, with its link.
- `役目` (line 41; comprehensibility C4, verbatim): the paragraph «役目 — это роль или назначение, а не мероприятие:
  мероприятие называет [行事](行事.md)（ぎょうじ）.» is deleted, with its link and the following blank line.
- `発つ` (lines 4, 12, 16 and 33; comprehensibility C6 and C7, verbatim): title and H1 «уезжать; отправляться в путь»
  instead of «уезжать; отбывать»; «発つ — уезжать, отправляться в путь.» instead of «発つ — уезжать, отбывать в путь.»; «…и
  建つ（たつ）— о том, что строение возводится.» instead of «…и 建つ — о том, что строение возводится.»
- `実用` (line 29; comprehensibility C8, with modification): «実用 выдвигает на первый план практическую пользу или
  пригодность…» instead of «…практическое применение или пригодность…».
- `原産` (line 33; comprehensibility C9, accepted with the reviewer's point reworded): «Речь об исходном происхождении, а не о месте, где растение
  или животное находится сейчас.» instead of «Словарный перевод «место обитания» здесь нуждается в уточнении: речь об
  исходном происхождении.»; the garden and hometown sentences are kept.
- `留まる` (line 19; comprehensibility C11, with modification): «Ущерб ограничился небольшими масштабами.» instead of «Ущерб
  не вышел за пределы небольшого масштаба.»
- `住まい` (line 18; comprehensibility C12, with modification): «Я ищу новое жильё.» instead of «Я ищу новое место, где
  жить.»
- `田植え` (line 33; comprehensibility optional): «В примерах это существительное употребляется с 手伝う и 始まる; не стройте
  отсюда урок спряжения с する.» instead of «В примерах существительное употребляется с 手伝う и 始まる; в просмотренных
  словарных статьях нет пометки о глаголе с する, поэтому урок спряжения здесь не обобщается.»

All twelve are new Batch 249 cards. No navigation-only file changed, so navigation stays at 10 files / 10 links, all
EN-position restorations. The coordinator's candidate edits stand, including the titles of 番地, 公務, 役目, あてはめる,
住まい, 発売, スタート, 畳む and 申し訳ない.

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Comprehensibility C1 was accepted with modification: "Russian does say «применять мазь», so the 塗る contrast is kept in
  Russian terms"; "The reviewer's replacement about «прикладной» is not used: line 21 already explains 応用物理学 «прикладная
  физика» without な."
- Comprehensibility C2 was accepted with modification: "Same treatment"; the rule-appropriateness sentence is kept.
- Comprehensibility C8 was accepted with modification: the wording "avoids 応用's quiz title «практическое применение» while
  keeping EN's "utility" point." The reviewer had proposed «…пригодность в реальном деле…».
- Comprehensibility C10 was declined: "The classification is learner-visible: the word quiz hint shows non-origin tags
  such as `mixed-reading` (kanji-cards-android `WordQuizScreen.kt:150`), and published RU 話し中:27 uses the same
  collection framing. EN parity (EN 役目:29)." At recheck the comprehensibility reviewer withdrew C10 with the
  qualification that the hint shows "the English slug `mixed-reading` (origin tags filtered), not the Russian phrase, so
  «learner-visible» is only partial."
- Comprehensibility C11 was accepted with modification: "the reviewer's «за рамки небольшого» is elliptical."
- Comprehensibility C12 was accepted with modification: "natural everyday noun; the reviewer's «жилище» is bookish."
- The other comprehensibility optionals were declined: "«футон» is an established Russian loanword explained by line 16;
  «произрастание» keeps the plant-growth focus distinct from 成長; the あてはめる senses are real; 住居 matches its formal
  register (reviewer: not defects)."
- The comprehensibility reviewer's outside-facet notes on 始め–スタート and 厚かましい–ずうずうしい needed no action: "Each
  pair is already declared on one side (スタート lists 始め; ずうずうしい lists 厚かましい); Android applies declarations in
  both directions."
- The consistency optional on 止まる:53 was declined: "止まる is a navigation-only restoration file; only link positions are
  wrapped and the wording is not changed in this batch. The sentence keeps EN's meaning (EN 止まる:41)." Its weak overlaps
  (役目–用, 番地–番, 発売–刊行/発行, 留守番–預かる/預ける, 生長–増加) were declined as "not required; no shared exact title
  segment or near-synonym answer".

Post-fix screen: a saved rerun at the committed `07ad251` over all 30 batch words (`b249-fix-screen.txt`, 597 lines) has
71 `OK` lines for pairs already guarded by an exclusion and 526 `!!` lines. Its 15 exact-segment lines are those of the
candidate screen: eleven `OK`, and the four unguarded 住まい–場, 場所, 所 and 陰 «место» lines, which the author report
declined and no blind reviewer raised. Against the candidate screen (588 lines) it removes 3 lines and adds 12, all
stem-only: the 略す–減らす «сокра» and 申し訳ない–詫びる «прост» lines change from `!!` to `OK`; 発つ's line with 送別
«уезжа» changes only in the 発つ title; and the new «отправ-» stem adds lines with スタート, 出かける, 出発 and 発車 (`OK`,
already guarded) and with 書留, 船便, 送る, 速達 and 郵送 (`!!`), plus the 送別 line. The dispositions record that these
«отправ-» lines are "sending/mail answers, not setting off"; the consistency recheck agreed ("I see no
plausible-correct-answer risk").

Net change from the candidate:
- title and H1 of 発つ;
- example translations in 留まる and 住まい;
- prose in 応用 (line 33), あてはめる (line 33), 申請 (line 33), 役目 (line 41, deleted), 申し訳ない (line 33), 発つ (lines 16 and
  33), 実用 (line 29), 原産 (line 33) and 田植え (line 33);
- two exclusions added (略す→減らす and 申し訳ない→詫びる), none removed;
- four links removed with their sentences (応用→申し込む, あてはめる→申し込む, 申請→適用 and 役目→行事); none added or
  retargeted.

No Japanese example sentence, sourced reading, kanji card, EN exclusion or navigation file changed. The content diff
`a8e87dd..07ad251 -- words` is 12 word files, 15 lines added and 17 removed (役目 loses its deleted paragraph and a blank
line); with `manifest.json` the fix changes 13 files, 28 lines added and 30 removed.

Fix 1 validation, as recorded in the dispositions: "`tools/validate.py` 0 errors; manifest rebuilt (5,589 files incl. 3
images and 2 scene catalogs); 124 unit tests OK; content budget OK; `git diff --check` clean. Link parity on the 40 batch
paths: LOST only the four by-design removals above (応用→申し込む, あてはめる→申し込む, 申請→適用, 役目→行事); EXTRA only the
reviewed RU-only 畳む→広げる link." For this record link parity was verified again over the 40 batch paths at `07ad251`
with the same result, and the link targets in the fix diff were compared: fix 1 removes exactly those four links and
adds or retargets none (the 塗る links in 応用 and あてはめる were present at the candidate).

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the correctness recheck says "Model not independently verifiable.", the consistency recheck "Model not verifiable
from inside the session." and the comprehensibility recheck "Model: not verifiable." The dispositions label each
reviewer's model "per runtime status".

The rechecks ran serially, one reviewer at a time, in one round: comprehensibility, then correctness, then consistency,
each on the fix diff `a8e87dd..07ad251` (12 word files and `manifest.json`). The initial reviews had run correctness,
then consistency, then comprehensibility. These orderings rest on the coordinator's session records; the recheck reports
do not record times. There was no second fix and no follow-up exchange.

Rechecks were returned as separate reports rather than appended to the initial review files: the full texts are in
`b249-recheck-correctness.md`, `b249-recheck-consistency.md` and `b249-recheck-comprehensibility.md` in the
coordinator's session folder, and their content is recorded in the round table below. The recheck briefs are saved in
the same folder as `b249-recheck-msg-comprehensibility.txt`, `b249-recheck-msg-correctness.txt` and
`b249-recheck-msg-consistency.txt`. Each brief gave the reviewer its own original report, the coordinator's dispositions
for all three facets (not the other reviewers' reports) and the fix diff, and repeated the read-only and no-generator
rules ("tools/validate.py is allowed; remove any tools/__pycache__ it leaves").

No recheck ran a generator. The correctness recheck records "No generator or repository write/action performed." and
"Read-only python -X utf8 -B tools/validate.py: exit 0, 0 errors. git diff --check clean; tools/__pycache__ absent.";
the consistency recheck records "`tools/validate.py` run with `-B`: 0 errors; no `tools/__pycache__` left." and verified
the manifest "by diff inspection only (no generator run)"; the comprehensibility recheck records "validate.py not
re-run" and makes no statement about generators. The correctness recheck records
`07ad251170e95ef589e7ec5bd814eb4c99a2bd4d` with parent `a8e87dd42d8d6fb01c89b03aa12b995550acc585` and "Primary checkout
git status --porcelain empty at start and immediately before report write."; the consistency recheck records the same
HEAD and parent with "`git status --porcelain` was empty at start and at write."; the comprehensibility recheck records
the same HEAD and parent with "`git status --porcelain` empty at start and at write." When these records were drafted, a
read-only check showed the RU checkout at HEAD `07ad251170e95ef589e7ec5bd814eb4c99a2bd4d` with `git status --porcelain
--ignored` printing nothing.

### Round 1 (`07ad251`)

| Facet | Scope and result |
|---|---|
| Comprehensibility | `07ad251`, parent `a8e87dd`, porcelain empty at start and at the write. "recheck of C1–C12, the 発つ coverage item and the optional notes against b249-dispositions.md and `git diff a8e87dd 07ad251 -- words`. Read in full:" the 12 changed cards; "For the C10 decline: words/話し中.md:1-40 and kanji-cards-android WordQuizScreen.kt:51 and :150." C1–C9, C11 and C12 **resolved**, for example C1 "Job-application and «прикладная физика» remarks are gone. The kept 塗る contrast is now grounded in Russian «применять». Agree with not restating line 21."; C7 "建つ（たつ） is on the card. Scoped coverage for 発つ is CLEAN; the other 29 stay CLEAN."; C8 "The body now says «практическую пользу или пригодность», not 応用's quiz title «практическое применение»."; C11 "«Ущерб ограничился небольшими масштабами.» is natural, keeps 小規模, and is better than the elliptical «за рамки небольшого»."; C12 "«Я ищу новое жильё.» is the everyday noun. Agree that «жилище» is bookish." C10 "withdrawn. Decline accepted." with the `mixed-reading` qualification quoted above ("Not reopened: the same line still says やく is on and め is kun, not two on readings, and «в этой коллекции» matches published 話し中:23-27."). "Optional 田植え resolved"; the declined optionals "optional; decline accepted. They were not defects." New text: the 塗る sentence "is grammatical on 応用:33 and あてはめる:33 … Not a regression."; 申し訳ない:33 "stands alone"; "«Отправляться в путь» is intransitive departure, not sending a thing … A stem overlap with mail titles is not an exact gloss collision." "Findings: none". Verdicts: "comprehensibility CLEAN; scoped coverage CLEAN". Limits: "Dictionaries not re-opened. validate.py not re-run (dispositions already report 0 errors). B250–B258 lane copies are not this HEAD. No claim about quiz runtime beyond the hint source read above." |
| Correctness | `07ad251` against `a8e87dd`, porcelain empty at start and before the write; frozen EN `6af98cb`, clean. "All 12 changed words/*.md cards read IN FULL against complete frozen EN originals"; "Also read original report, dispositions, complete RU 減らす/詫びる/塗る cards, localization/review policy, EN exclusion contract and word/manifest fix diffs." It had no original finding or optional note; its reconciliation lines classify its original limits, including "partially resolved — two new guards checked; no full-corpus synonym/runtime quiz audit." and "four intentional removals are acceptable below." New text: 略す:9 "減らす guard conservatively protects overlapping Russian shortening/reduction labels."; 申し訳ない:9,33 "the extra guard is defensible despite expression/verb differences. Removing the English "sorry = sad/sympathy" aside loses no Japanese construction."; 応用:33 and あてはめる:33 "塗る（ぬる） correctly describes coating with ointment/paint, not applying knowledge" (Digital Daijisen 塗る; JMdict 1444270), the removed comparisons "English-dependent"; 申請:33 and 役目:41 the deleted comparisons English-only, "行事 exclusion remains"; 発つ "title/H1/gloss "уезжать; отправляться в путь" cover EN "depart; set off"" (JMdict 2857436/1597040 sense 5) and "建つ（たつ） is correctly the intransitive building/erection homophone, JMdict 1597045"; 実用:29 (JMdict 1321480), 原産:33, 留まる:19, 住まい:18 and 田植え:33 faithful. "Findings: None. All 24 Japanese examples and kana readings remain unchanged; core metadata and every EN exclusion survive. Manifest changes are only contentVersion and the 12 matching committed-blob SHA-256 values; no path added/lost." Verdicts: "Correctness CLEAN; scoped coverage CLEAN on HEAD in this recheck scope. No regression established; unchanged batch cards retain the prior review." Limits: "Post-fix recheck, not another blind review or endorsement of all coordinator rationales. Other reviewers' original reports not read. No generator or repository write/action performed. CLEAN means no actionable defect established in scope, not exhaustive correctness." |
| Consistency | HEAD `07ad251` (parent `a8e87dd`), porcelain empty at start and at write. "dispositions file; the full fix diff (12 word cards plus manifest.json, read in full at -U1, with the changed lines in context); front-matter `quiz_exclusions` of all affected cards and of the cross-referenced cards (申し込む, 適用, 行事, 減らす, 詫びる, 塗る); existence of all link targets; EN 発つ front matter; a title screen of 発つ against the RU title list." Q1 "RESOLVED. `減らす` appended last, 11 unique entries, target exists, the original 10 retained, bracket format intact."; Q2 "RESOLVED. `詫びる` appended last, 18 unique entries, target exists, format intact."; 止まる:53 "DECLINE ACCEPTED"; weak overlaps "OPTIONAL, decline accepted."; "畳む→広げる RU-only link, 住まい→住居 and 用途→応用 guards: acceptable, no change." 発つ: "No exact-segment collision among RU titles."; "Exclusions are unchanged and identical to EN". "Intentional link removals, all four confirmed", each exclusion retained; "Removal turned plain text into no dangling link anywhere." Manifest: "the diff changes exactly `contentVersion` (ff40e930d163cbc9 → 0b5d06675bb7dbf0) plus 12 hash lines, one for each of the 12 changed cards. Nothing else differs. I did not recompute it, because that would call the generator module." Post-fix screen paragraph: "matches my observation." "Findings: none." Verdicts: "consistency CLEAN; quiz safety CLEAN (HEAD)." Limits: "the manifest hashes were verified by diff inspection only (no generator run). The title screen used my earlier pre-fix title list plus direct reads of the changed cards; no other card's title changed in this commit. No dictionary access beyond what the cards cite." |

No recheck raised a new finding or left an optional note open. The comprehensibility reviewer's qualification of the C10
decline reason is recorded above; it did not reopen C10. There was no second fix.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness: no finding and no optional note | — | Correctness recheck "None — no original findings or optional recommendations." |
| Consistency Q1: 略す–減らす «сокращать» (low-to-medium) | **Resolved** | `略す.md:9`; consistency recheck "RESOLVED"; correctness recheck "減らす guard conservatively protects overlapping Russian shortening/reduction labels." |
| Consistency Q2: 申し訳ない–詫びる (low-to-medium) | **Resolved** | `申し訳ない.md:9`; consistency recheck "RESOLVED"; correctness recheck "the extra guard is defensible". |
| Consistency optional: 止まる:53 wording around 留まる | **Optional**; declined (navigation-only file) | Consistency recheck "DECLINE ACCEPTED". |
| Consistency optional: weak overlaps 役目–用, 番地–番, 発売–刊行/発行, 留守番–預かる/預ける, 生長–増加 | **Optional**; declined, no defect | Consistency recheck "OPTIONAL, decline accepted." |
| Consistency notes: RU-only 畳む→広げる link; 住まい→住居 and 用途→応用 guards; 厚かましい without a key; stem-only in-batch pairs | **Accepted**; unchanged | Consistency recheck "acceptable, no change." |
| Comprehensibility C1: 応用:33 English "apply/application" remarks (medium) | **Resolved** (with modification) | `応用.md:33`; 申し込む link removed by design, exclusion retained; comprehensibility recheck "resolved"; correctness recheck Digital Daijisen 塗る, JMdict 1444270. |
| Comprehensibility C2: あてはめる:33 English-dependent contrasts (medium) | **Resolved** (with modification) | `あてはめる.md:33`; 申し込む link removed by design, exclusion retained; comprehensibility recheck "resolved". |
| Comprehensibility C3: 申請:33 «применение» / 適用 sentence (medium) | **Resolved** | `申請.md:33`; 適用 link removed by design, exclusion retained. |
| Comprehensibility C4: 役目:41 «не мероприятие» (medium) | **Resolved** | `役目.md:41` deleted; 行事 link removed by design, exclusion retained. |
| Comprehensibility C5: 申し訳ない:33 sadness/condolence sentence (low) | **Resolved** | `申し訳ない.md:33`; correctness recheck "loses no Japanese construction". |
| Comprehensibility C6: 発つ title «отбывать» (medium) | **Resolved** | `発つ.md:4,12,16`; JMdict 2857436/1597040 sense 5 per the correctness recheck; consistency recheck "No exact-segment collision among RU titles." |
| Comprehensibility C7: 発つ:33 建つ without a reading (low; scoped coverage) | **Resolved** | `発つ.md:33`; JMdict 1597045; comprehensibility recheck "Scoped coverage for 発つ is CLEAN". |
| Comprehensibility C8: 実用:29 repeats 応用's title (medium) | **Resolved** (with modification) | `実用.md:29`; JMdict 1321480. |
| Comprehensibility C9: 原産:33 unseen gloss «место обитания» (low) | **Resolved** | `原産.md:33`. |
| Comprehensibility C10: 役目:27 collection/tag framing (low) | **Withdrawn**; decline accepted | Comprehensibility recheck "withdrawn. Decline accepted.", with the partial-visibility qualification; EN 役目:29 parity; `WordQuizScreen.kt:150`. |
| Comprehensibility C11: 留まる:19 calque (low) | **Resolved** (with modification) | `留まる.md:19`. |
| Comprehensibility C12: 住まい:18 «место, где жить» (low, medium confidence) | **Resolved** (with modification) | `住まい.md:18`. |
| Comprehensibility optional: 田植え:33 author-facing check | **Resolved** | `田植え.md:33`; comprehensibility recheck "Optional 田植え resolved". |
| Comprehensibility optionals: 畳む «футон», 生長 «произрастание», あてはめる title length, 住居 «жилое помещение» | **Optional**; declined, no defect | Comprehensibility recheck "optional; decline accepted. They were not defects." |
| Comprehensibility outside-facet notes: 始め–スタート, 厚かましい–ずうずうしい | **Accepted**; no action | Each pair is declared on one side (スタート lists 始め; ずうずうしい lists 厚かましい). |
| Four EN links removed by fix 1 (応用→申し込む, あてはめる→申し込む, 申請→適用, 役目→行事) | **Accepted**; by design | Link parity reports them as LOST; the consistency recheck confirmed all four, each exclusion retained; correctness recheck "four intentional removals are acceptable". |

Cross-batch note: links to absent targets stay plain. Seven EN link occurrences in this batch's new cards, to 7 targets,
are absent from RU: words 特売 (from 発売), 建つ (from 発つ) and あてはまる (from あてはめる), and kanji 畳 (from 畳む), 略 (from
略す), 訳 (from 申し訳ない) and 植 (from 田植え). The other written kanji without an RU kanji card, 応 and 請, have none in EN
either. Four EN links to existing cards are deliberately not reproduced: fix 1 removed 応用→申し込む, あてはめる→申し込む,
申請→適用 and 役目→行事 together with their English-dependent sentences, so link parity reports them as LOST; their
exclusions are retained. The one RU-only link, 畳む:29 → 広げる, is to a card published before this batch and is
unchanged by fix 1. No link was held from an earlier batch, and none is held for a later one. The ten navigation-only
restorations (kanji/厚.md line 37 and words/みっともない.md line 36 to 厚かましい; words/ゴール.md line 33 and
words/ストップ.md line 29 to スタート; words/成長.md line 42 to 生長; words/止まる.md line 53 to 留まる; words/相撲.md line
32 to 住まい; words/苗代.md line 38 to 田植え; words/西暦.md line 34 and words/誕生日.md line 28 to 生年月日) are unchanged by
fix 1; the existing gloss «наглый; бесстыдный» in kanji/厚 differs from the final 厚かましい title «наглый;
беззастенчивый» but shares its first segment. Every exclusion target resolves to a card published at the baseline or
to a batch card. The scratch lane copies of 発つ used for later batches (B250–B258) still carried the candidate text when
fix 1 was made; the dispositions record that they "are resynced after this fix". That resync is outside this batch.

## Final exclusion set

All 222 EN exclusion entries (29 lists; EN has none on 厚かましい) are retained in EN order; 15 of them lie inside the
batch, and the other 207 target existing RU cards. Four direct, one-sided entries are added on four new cards; each is
appended at the end of its list:

- 住まい→住居: `[住宅, 住所, 家, 家屋, 宅, 自宅, お宅, ホーム, 貸家, 下宿, 宿, 住む, 家庭, 住居]`;
- 用途→応用: `[用, 目的, ため, 使用, 利用, 実用, 活用, 使う, 用いる, 役目, 機能, 働き, 応用]`;
- 略す→減らす: `[省略, 省く, 縮める, 抜く, 削除, 詰める, 略語, 除く, 削る, 飛ばす, 減らす]`;
- 申し訳ない→詫びる: `[すまない, すみません, ごめんなさい, ごめん, 申し訳, 謝る, 悪い, あいにく, 恐縮, お待ちどおさま,
  お待たせしました, ありがとう, どうも, 御礼, 礼, 感謝, 有難い, 詫びる]`.

The first two were present at the candidate and accepted by the coordinator ("住まい→住居 (required: «место, где живут» vs
«место проживания»), 用途→応用 (conservative: shared «применение»)"); the consistency reviewer classed 住まい→住居 as
"**required**" and 用途→応用 as "**conservative but acceptable**", and the correctness reviewer found both "defensible
direct overlap protections". Both target batch words. Fix 1 added 略す→減らす (Q1; 減らす «уменьшать; сокращать») and
申し訳ない→詫びる (Q2; 詫びる «приносить извинения; просить прощения (за проступок)»), which target cards published before
this batch; the consistency recheck resolved both. Every RU addition is appended at the end of its list, and no EN entry
is removed or reordered. Android applies each declaration symmetrically (EN `docs/content-format.md`, lines 162–165), so
no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** throughout; CLEAN at recheck for all 12 changed cards.
- Scoped coverage: **CLEAN** after fix 1 (発つ C7); CLEAN throughout in the correctness review and recheck.
- Comprehensibility: **CLEAN** after fix 1 (応用, あてはめる, 申請, 役目, 申し訳ない, 発つ, 実用, 原産, 留まる and 住まい); the
  modified dispositions of C1, C2, C8, C11 and C12 stand as accepted, and the C10 decline stands.
- Cross-file consistency: **CLEAN** throughout; the ten restored navigation links in ten files, the RU-only 畳む→広げる
  link and the four by-design link removals stand.
- Quiz safety: **CLEAN** after fix 1 (略す Q1, 申し訳ない Q2), including the 発つ retitle; the four RU additions stand. This
  covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread the changed cards and the lines needed to judge them; the unchanged cards rest on review 001, in
  which all three reviewers read all 30 cards in full. The correctness recheck states "unchanged batch cards retain the
  prior review."
- In review 001 the consistency reviewer compared EN front matter, link sets, headings and footers programmatically and
  had "No independent dictionary access beyond the cards' own citations."; the comprehensibility reviewer did not
  re-open dictionaries at recheck. The consistency recheck verified the manifest by diff inspection only and screened
  titles from "my earlier pre-fix title list plus direct reads of the changed cards"; link parity at the fix was rerun
  for this record. Necessity classes are judgements, not measurements.
- The correctness recheck is "not another blind review or endorsement of all coordinator rationales"; no full-corpus
  synonym or runtime quiz audit was made.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fix, so its payload hashes describe the candidate `a8e87dd`, not `07ad251`.
- Frequency and preferred register (for example «жильё», «отправляться в путь» and «футон») were not certified. Online
  dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected beyond the
  comprehensibility reviewer's reading of the hint source.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
