# Batch 235 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `75b2616d78a93d0655a2e7494abb6c1f9585ad10` | `a46106ee98c575dabd9e73ed70b1185de4ccd995` | Initial review snapshot: the signed candidate, on `origin/full-ru-235-words-74`. |
| `930e9f3dae23476c5443f1526242151ebb9e1e61` | `e2b6a36b07ceb92245758847d25916dbdb9f7275` | Fix 1 (final candidate). It covers correctness C1 and comprehensibility C1–C6 (C2 with the correctness optional on the 転がる title; C2 and C6 with adapted wording; C3 partially adopted) and the comprehensibility optional on 赤道. It adds and removes no exclusion and no link. Signed; on `origin/full-ru-235-words-74`. |

Fix 1 changed eight word files and regenerated `manifest.json` (`contentVersion` `2f4b942fc5207406`, 5,169 entries:
5,164 `files` + 3 images + 2 scenes; the candidate had `bf9f720376eac7d4`). The intake was not refreshed; it still records
the candidate's 35 payload hashes.
- `跳ねる` (line 39; correctness C1): «…芝居が跳ねる（しばいがはねる）— «спектакль заканчивается».» instead of «…— «спектакль
  окончился».», the nonpast counterpart of EN :43 "the show ends"; the Japanese phrase, kana and the surrounding
  explanation are unchanged.
- `貸し出し` (line 21; comprehensibility C1): «— В этом магазине выдают велосипеды на время.» instead of «— В этом магазине
  можно взять велосипед на время.»: the lender's side, as EN :19 "This shop rents out bicycles" and the card's own note at
  :43 (библиотека выдаёт, читатель берёт).
- `転がる` (lines 4 and 12; comprehensibility C2 with the correctness optional on the title, adapted wording): title and H1
  «катиться; падать кувырком; валяться» instead of «катиться; лежать где попало (брошенным)», the counterpart of EN "roll;
  tumble; lie around". «валяться» covers both the person lying on the tatami (:20) and the pencil lying on the floor (:21),
  and «падать кувырком» restores EN "tumble" (body :16 «падение кувырком»). The proposed «ложиться» was not used: it shares
  the «ложит-» stem with 寝る «спать; ложиться спать» and 積もる «ложиться слоем» (both unguarded), and it drops EN "tumble".
- `賞品` (lines 4 and 12; comprehensibility C3, partially adopted): title and H1 «приз (вещью); кубок» instead of «приз
  (вещью); кубок, трофей». «трофей» is removed because its first Russian sense is war spoils; «кубок» stays as the
  counterpart of EN's second segment "trophy" (EN :4 "prize item; trophy"), already qualified at :23 «Приз не обязательно
  кубок», as EN :21 "The prize need not be a trophy".
- `賞金` (line 21; comprehensibility C4): «— На этом конкурсе предусмотрен денежный приз.» instead of «— На этом конкурсе
  вручают денежный приз.», matching the card's 賞金が出る gloss at :18 and EN :19 "This competition offers prize money".
- `交差` (lines 4 and 12; comprehensibility C5): title and H1 «скрещение (линий, дорог); пересечение (друг с другом)»
  instead of «скрещение (линий, дорог); пересекаться (друг с другом)»: both segments are nouns, as EN "crossing;
  intersection" and the する-noun use at :16–17.
- `足袋` (line 16; comprehensibility C6, adapted wording): «足袋 — таби, традиционные японские носки, у которых большой палец
  отделён от остальных.» instead of «足袋 — традиционные японские носки, у которых большой палец отделён от остальных.»,
  introducing the Russian name before the examples use it, as EN does in its title ("tabi; traditional split-toe socks").
  The proposed added sentence was not used, and the title is unchanged.
- `赤道` (line 39; comprehensibility optional): «Не путайте чтение せきどう с отдельным кадастровым термином 赤道 для дорог,
  который читается あかみち или あかどう.» instead of «Не путайте чтение せきどう с отдельным термином кадастра 赤道, который
  читается あかみち или あかどう.», restoring EN :40 "the separate cadastral-road term".

The correctness reviewer's optional 車庫 «автобусный парк» was not adopted, nor were the comprehensibility reviewer's
wording «катиться; ложиться; валяться (где попало)» for 転がる, its single-segment 賞品 title «приз (вещью)» or its added
sentence for 足袋; its optional notes on 貨物:40, 足る's «(+ に足る)» and 身分証明書 led to no action. The consistency
reviewer's optional notes led to no action. The dispositions gave the reasons (see the reconciliation table).

The coordinator's post-fix title screen of the three changed titles (`b235-postfix-screen.txt`; pool: the RU primary
word cards plus the Batch 236 lane drafts) found three exact shared segments, all guarded by EN lists on the new cards:
転がる's «катиться» with ころころ «катиться; то и дело меняться» and ごろごろ «громыхать; катиться; валяться без дела», and
交差's «пересечение» with 横断 «переход (через дорогу и т. п.); пересечение» (declared on 交差; 横断's own list does not
declare 交差). Everything else is stem-only: 転がる meets 倒れる «падать; рушиться», 落ちる «падать» and 転がす «катить
(что-либо); опрокидывать» (all guarded); 交差's «перес-» meets 横切る and 渡る (guarded) and からから, ぱさぱさ, 乗り換える,
数える, 止す and 送料 (unguarded prefix coincidences with unrelated words); 賞品 has no exact segment and no stem lead. Fix 1
adds no link and removes none, and changes no exclusion. The three RU-only links at the candidate, 資料:31 → 情報, 資料:32
→ 材料 and 貸間:33 → 下宿, are unchanged. The dispositions record `tools/validate.py` 0 errors and the unit tests (124) OK
in the post-fix state.

Net change from the candidate:
- titles and H1s of 転がる, 賞品 and 交差;
- example translations in 貸し出し and 賞金;
- prose in 跳ねる (line 39), 足袋 (line 16) and 赤道 (line 39);
- no exclusion or link change.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`75b2616..930e9f3 -- words` is eight word files, 11 lines added and 11 removed; with `manifest.json` the commit changes
9 files, 20 lines added and 20 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs; the
reports state that the model is not verifiable from inside the session.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. No recheck raised a new finding, so there was no fix 2.

Each reviewer appended its recheck to its own report file. The correctness section records that it inspected the actual
eight-card diff and reread all eight revised RU cards and their EN originals completely, considering the rationale as
evidence, not authority; the consistency section records the reviewed scope as the diff against `75b2616` (8 word cards
+ `manifest.json`) screened against all RU word titles; the comprehensibility section records that it read the eight
changed passages in the working tree and reconciles each of its findings. The recheck sections do not reproduce the
briefs, so this record does not claim their contents.

All three rechecks state that no generator was run. The consistency reviewer ran `tools/validate.py` (0 errors); the
correctness reviewer records no validator or unit-test run, and the comprehensibility reviewer did not run the validator.
The correctness section records snapshot `930e9f3` with a clean RU worktree, the consistency section `930e9f3` with a clean
tree, and the comprehensibility section `930e9f3` with an empty `git status --porcelain`. The recheck records include no
separate coordinator status check after the rechecks; when these records were drafted, a read-only check showed the RU
checkout on `full-ru-235-words-74` at HEAD `930e9f3dae23476c5443f1526242151ebb9e1e61` with `git status --porcelain --ignored`
printing nothing.

### Round 1 (`930e9f3`)

| Facet | Scope and result |
|---|---|
| Correctness | Snapshot `930e9f3`, parent `75b2616`, clean RU worktree verified. Inspected the actual eight-card diff and reread all eight revised RU cards and their EN originals completely. C1 is **resolved**: 跳ねる:39 has the exact requested nonpast gloss, with the Japanese, kana and surrounding qualifications unchanged; the original JMdict/Daijisen evidence still applies. The optional 転がる title is **resolved as optional polish**: «катиться; падать кувырком; валяться» restores roll/tumble/lie-around coverage, «валяться» accommodates persons and objects without imposing "abandoned", and it is at least as accurate as the former title. The optional 車庫 remains optional. Every other rewrite was judged at least as accurate in its context: 貸し出し:21 (the lender's side; neither payment nor permanent transfer asserted), 賞金:21 (matches :18 and EN "offers prize money"), 交差:4/12 (nominal «пересечение»; :16–18 still teach the する construction), 賞品:4/12 (removing «трофей» avoids its spoils sense; «кубок» is qualified at :16/:23), 足袋:16 (Russian «таби» names the already-defined socks) and 赤道:39 (the road qualifier restores the EN distinction). Japanese text retained and current normalized manifest hashes verified for all eight changed cards. No generator, validator or unit tests were run; prior dictionary evidence was reused. Correctness **CLEAN** and scoped coverage **CLEAN**; unchanged cards retain their initial bounded CLEAN assessments. |
| Consistency | Snapshot `930e9f3`, clean tree; diff against `75b2616` = 8 word cards + `manifest.json`. Validator 0 errors; no generator. Titles and H1s match on 転がる, 賞品 and 交差; 跳ねる, 貸し出し, 賞金, 足袋 and 赤道 are body-only edits with titles unchanged and no link added or removed. Exact-segment screen over all RU word titles: 転がる «катиться» is shared with ころころ, ごろごろ and 転がす (the first two in its exclusions; 転がす declares 転がる); «валяться» is shared only with ごろごろ (guarded); 賞品 «кубок» has no overlap; 交差 «пересечение» is shared only with 横断 ("guarded both ways"). No new unguarded ambiguity. Exclusion lists on these cards match the brief; no orphaned reference or broken link in the changed lines. Manifest: 5164 file entries; every non-strokes entry equals the raw sha256 of its file; no content file unlisted or missing (it read the brief's 5,169 as likely counting header keys; the 5,169 entries are 5,164 `files` + 3 images + 2 scenes). The 発行/貸し出し note stays optional (accepted), the unguarded 資料–情報/原料, 身分–現状 and 載る–刊行 stay optional, the 足る:36 note is **withdrawn**, and the strokes-hash limit is "resolved as explained", without independent re-derivation. Consistency, quiz safety and scoped integration are **CLEAN**, with no finding. |
| Comprehensibility | Snapshot `930e9f3`, parent `75b2616`, empty `git status --porcelain`; read the eight changed passages in the working tree, not all 30 cards. C1 is **resolved**: «выдают велосипеды на время» is the lender's side and matches :43. C2 is **resolved (adapted)**: the title no longer excludes the tatami example, «валяться» covers the person and the pencil, and «падать кувырком» matches the body gloss and EN "tumble"; the reviewer does not maintain «ложиться». C3 is **partially resolved; residual accepted, not unresolved**: «трофей» is gone, and «кубок» remains as the EN "trophy" segment, qualified at :16 and :23; the reviewer does not maintain deleting «кубок». C4 is **resolved**: matches the gloss at :18. C5 is **resolved**: both segments are nouns, and the body still requires する. C6 is **resolved (adapted)**: «таби» is defined before the examples use it; a separate sentence is unnecessary. The 赤道 optional is **resolved**. 貨物:40 and 足る «(+ に足る)» stay optional; the 身分証明書 note is **withdrawn** (its reading is already at 身分:40). No regression (跳ねる:39 checked). Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 跳ねる:39 «спектакль окончился» renders the unmarked nonpast as a past (minor) | **Resolved** | `跳ねる.md:39`; EN :43 "the show ends"; JMdict 1429620 sense 4; Digital Daijisen は・ねる sense 4. |
| Correctness optional: 転がる's title could mention tumbling or lying down | **Resolved** as optional polish (adopted through comprehensibility C2) | `転がる.md:4,12`; EN "roll; tumble; lie around". |
| Correctness optional: 車庫 «автобусный парк» | **Optional, not adopted**; kept optional at recheck | The reviewer classed it as nonblocking, and «депо» was not shown to exclude bus use. |
| Consistency classification of the five RU-added exclusions | **Agreed** that all stay; no action at recheck | The reviewer's classes match the author's and the coordinator's (see the final exclusion set below). |
| Consistency optional: 発行 shares «выдача» with 貸し出し but is unguarded | **Optional, not adopted**; accepted at recheck | No shared exact segment; the objects differ (documents vs items lent for temporary use); 発行 is a published card outside this batch. |
| Consistency optional: unguarded 資料–情報/原料, 身分–現状 and 載る–刊行 | **Optional, not adopted**; kept optional at recheck | The titles separate the senses. |
| Consistency optional: 足る:36 glosses 間に合う «годиться; хватать» against its title | **Withdrawn** at recheck | A contextual body gloss of the sufficiency sense, following EN :38 "serve the purpose; suffice"; 間に合う's title is unchanged. |
| Consistency limit: 118 strokes manifest hashes differ from the raw sha256 | **Not a defect**; explanation accepted at recheck without re-derivation | `tools/build_manifest.py:19` hashes text files after CRLF→LF normalization; exactly the 118 stroke files that contain CRLF (byte copies of EN) differ from their raw sha256; no strokes file changed in this batch. |
| Comprehensibility C1: 貸し出し:21 translates from the borrower's side (minor) | **Resolved** | `貸し出し.md:21`; EN :19 "This shop rents out bicycles"; the card's note at :43. |
| Comprehensibility C2: 転がる's title «лежать где попало (брошенным)» excludes the lying-down example (minor) | **Resolved** (adapted wording); «ложиться» not maintained at recheck | `転がる.md:4,12`; Digital Daijisen ころがる sense 3; EN "roll; tumble; lie around"; «ложиться» shares the «ложит-» stem with 寝る and 積もる (both unguarded). |
| Comprehensibility C3: 賞品 «кубок, трофей» (minor) | **Partially resolved**; residual «кубок» accepted at recheck | `賞品.md:4,12`; Russian Wiktionary «трофей» sense 1 war spoils; EN "prize item; trophy"; :23 «Приз не обязательно кубок» (EN :21). |
| Comprehensibility C4: 賞金:21 «вручают» contradicts the gloss at :18 (minor) | **Resolved** | `賞金.md:21`; EN :19 "This competition offers prize money". |
| Comprehensibility C5: 交差's infinitive «пересекаться» on a する-noun (minor) | **Resolved** | `交差.md:4,12`; EN "crossing; intersection"; tags `[kango, noun, suru]`. |
| Comprehensibility C6: 足袋 never introduces «таби» (minor) | **Resolved** (adapted wording: in line 16 rather than an added sentence) | `足袋.md:16`; EN title "tabi; traditional split-toe socks". |
| Comprehensibility optional: 赤道 «термином кадастра» is opaque | **Resolved** (adopted) | `赤道.md:39`; EN :40 "the separate cadastral-road term". |
| Comprehensibility optionals: 貨物:40 «Карточка сохраняет исходное чтение かもつ» and 足る's «(+ に足る)» | **Optional, not adopted**; kept optional at recheck | 貨物: EN parity (EN :33 "This card keeps the source reading かもつ"); 足る: it marks the construction of the «заслуживать» sense, which the body explains. |
| Comprehensibility optional: 身分証明書 lacks a kana reading | **Withdrawn** at recheck | The reading is already at `身分.md:40` (みぶんしょうめいしょ). |

Cross-batch note: links to absent targets stay plain. Seventeen EN link targets in this batch's new cards (18 occurrences)
are absent from RU: the words 巻く (from 転がす), 点々 (from 転々), 姓 (from 氏名), 草履 and 下駄 (from 足袋) and 緯度 (from
赤道), and the kanji cards 輸 and 血 (from 輸血), 輪 (from 車輪), 庫 (from 車庫), 氏 (from 氏名), 袋 (from 足袋), 床 (from
起床), 賞 (from 賞金 and 賞品), 貯 and 蔵 (from 貯蔵) and 貨 (from 貨物). The other written kanji without an RU kanji card,
載, 掌, 身, 蹴, 踏, 跳 and 蓄, have none in EN either. No links were held from Batch 234, and none is held from this batch.

## Final exclusion set

All 137 EN exclusion entries (26 lists; 輸血, 車掌, 赤道 and 資料 have none in EN) are retained in EN order; 12 of them lie
inside the batch, and the other 125 target existing RU cards. Five direct, one-sided entries are added on four new cards
(three appended to three existing lists and one new list of two on 資料), all from the authoring lane and all at the
candidate; the coordinator added none, and fix 1 added and removed none. The author and the coordinator classed 資料→材料
and 貸間→下宿 as required and 資料→参考, 賞品→賞金 and 貸し出し→支給 as conservative; the coordinator accepted them as
reported. The consistency reviewer classed them as follows:

- Required (2): 資料→材料 and 貸間→下宿.
- Conservative (3): 資料→参考, 賞品→賞金 and 貸し出し→支給; it added that 発行 shares «выдача» but is unguarded (a minor
  inconsistency, optional; accepted at recheck).

Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added; the targets do not declare these pairs back. 貸し出し→発行 is not
guarded (consistency optional, above). 横断's own list does not declare 交差; the pair is guarded by 交差's EN list.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (跳ねる, C1).
- Scoped coverage: **CLEAN** throughout.
- Comprehensibility: **CLEAN** after fix 1 (貸し出し, 転がる, 賞品, 賞金, 交差, 足袋 and 赤道); C3's residual «кубок» was
  accepted, and the remaining optional notes stay optional.
- Cross-file consistency: **CLEAN** throughout; the three RU-only links (資料:31 → 情報, 資料:32 → 材料 and 貸間:33 → 下宿)
  and the six restored navigation links of the candidate stand.
- Quiz safety: **CLEAN** throughout, including the 転がる, 賞品 and 交差 retitles. This covers the reviewed batch and the
  directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them; the comprehensibility recheck did not
  re-read the other cards or re-fetch dictionary pages, and it did not re-audit the quiz-stem inventory behind the unused
  «ложиться». The unchanged cards rest on review 001, in which all three reviewers read all 30 cards in full (the
  consistency reviewer compared the EN originals by script).
- The correctness recheck was a bounded bilingual recheck using previously verified dictionary evidence, not a fresh
  full-batch or quiz audit; it ran no validator or unit tests, and its original evidence and model limitations remain. The
  consistency reviewer performed no dictionary re-verification, did not read the Batch 236 drafts (its pool screen covers
  committed RU titles only), and its necessity classes are judgements, not measurements. The comprehensibility recheck did
  not run `validate.py`.
- Frequency, exact modern bus-depot usage («депо») and preferred register were not certified; Russian dictionary evidence
  for «таби» is limited to Wiktionary (этногр.).
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `75b2616`, not `930e9f3`.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
