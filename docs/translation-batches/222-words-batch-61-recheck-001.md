# Batch 222 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `d0d6d08431a1e7dd81d6eaa151a8c841c37c297e` | `c6b8f7f32697ac0e681e2544e3deb8f92208352a` | Initial review snapshot: the signed candidate, pushed before review. |
| `b00e465d28d109502d1da2da9162bde322686c3d` | `3f27ad192e83baff4921802e2ee03a01350c4a0d` | Fix 1. It covers the four correctness findings, the five consistency findings, the two comprehensibility findings, two adopted optional items and the intake refresh. Signed and pushed before the rechecks. |
| `a1fe63a01670430a32ed030c8c7fdea0107a1b1f` | `182b4c953c56b12344604f92ddc1f44f8f9a3141` | Fix 2 (final candidate). It covers the correctness recheck finding R1 on ジュース and refreshes the intake. Signed and pushed before the second correctness recheck and the other two rechecks. |

Fix 1 changed nine word files and regenerated `manifest.json` (`contentVersion` `9d11d6c2eb09196a`; the candidate had
`57a4e697f7978cab`) and the intake:
- `カード`:
  - Lines 4, 12 and 21 (comprehensibility 1, accepted in modified form): «молочный сгусток» instead of «сырный сгусток» in
    the title, the H1 and the body definition, and the example translation «Сыр делают из молочного сгустка» instead of
    «…из сгустка». «Молочный сгусток» is the cheesemaking term (for example Smykov et al., «Определение момента готовности
    молочного сгустка к разрезке»). The reviewer's «сгусток молока (для сыра)» was not adopted, to keep «сыр» out of the
    title next to チーズ «сыр».
  - Line 31 (correctness C2, accepted in modified form): «…, а не カード. В контексте оплаты или карточной игры カード
    переводят как «карта»; в других случаях перевод выбирают по виду карточки.» instead of «…, а не カード: «картой» カード
    бывает только как платёжная или игральная карта.» The 地図 contrast stays.
  - Line 35 (correctness C1, the reviewer's remedy): «В некоторых японских текстах о выпечке カード называют также скребок
    для теста; …» instead of «…словом «карточка» называют также скребок для теста; …». JMdict 1036400 sense 7.
- `ダイヤ` (correctness C3, the reviewer's remedy): title and H1 «алмаз; бриллиант; график движения поездов» instead of
  «бриллиант; …» (lines 4 and 12), and the source line «записи 1076860 (значение 1, алмаз; бриллиант)» (line 36). Gramota
  бриллиант sense 1 requires a cut stone, while EN has "diamond". 宝石 and 玉 stay guarded, and no other title contains
  «алмаз».
- `スター` (correctness C3, the reviewer's remedy): title and H1 «звезда; знаменитость» instead of «знаменитость; звезда
  (кино, спорта и т. п.)» (lines 4 and 12), after EN "star; celebrity"; the symbol and celestial senses stay in the body.
  The exact segment «звезда» equals 星's whole title, which was already guarded.
- `スタンド`:
  - Lines 4 and 12 (correctness C3, the reviewer's remedy): title and H1 «трибуна; подставка, стойка; настольная или
    напольная лампа» instead of «…; настольная лампа». The body and JMdict 1069930 sense 4 include the floor lamp.
  - Line 9 (consistency F3 and F4): `quiz_exclusions: [台, 電灯, 受付, ガソリンスタンド, 明かり]` instead of
    `[台, 電灯, 受付]`. The body teaches スタンド as short for ガソリンスタンド «автозаправочная станция», and 明かり «свет;
    светильник» names the lamp sense already guarded with 電灯 (明かり itself guards 電灯).
- `ソファー` (line 28; correctness C4 and consistency F5, merged): «[ベンチ](ベンチ.md) — скамья» instead of «ベンチ —
  скамья». It is a RU-only link to an existing card at a substantive comparison (EN's mention is plain), in the same form
  as the card's `[椅子](いす.md)`. RU-only links become eight.
- `トラック`:
  - Line 9 (consistency F1): `quiz_exclusions: [車, 自動車]` instead of `[車]`, following the バス and タクシー precedent.
  - Line 21 (comprehensibility optional item, adopted): トラックに乗る «ехать на грузовике» instead of «ехать в грузовике»,
    which covers riding in the bed as well as the cab.
- `デート` (line 9; consistency F2): `quiz_exclusions: [月日, 日付]` instead of `[月日]`. The body records the calendar-date
  sense (JMdict 1081430 sense 2), and 日付 «дата» is its plainest title. 日付 is a navigation-only file in this batch, so
  the guard is declared on デート.
- `スープ` (line 20; correctness optional item, adopted): «хотя по-русски обычно говорят «есть суп»» instead of «хотя
  по-русски суп едят, а не пьют».
- `ジュース` (comprehensibility 2, first remedy; superseded by fix 2):
  - Title and H1 «сок; сладкий безалкогольный напиток; равный счёт (в теннисе)» instead of «…; ровно (счёт в теннисе)»
    (lines 4 and 12).
  - Line 23: «…означает равный счёт, например в теннисе; по-русски такой счёт в теннисе объявляют словом «ровно».»
  - Line 25: the example «— В теннисном матче счёт стал равным.» instead of «…счёт стал «ровно».»
  - Line 9: `quiz_exclusions: [飲み物, 等しい]`, a conservative guard because the new standalone «равный» was the first
    segment of 等しい «равный; равнозначный».
- The intake note now names the fixed cards, and the nine candidate hashes were refreshed.

Fix 2 changed only `ジュース` and regenerated `manifest.json` (`contentVersion` `3337677af8597d56`, 4,779 entries) and the
intake (correctness R1, the reviewer's remedy, extended):
- Lines 4 and 12: title and H1 «сок; сладкий безалкогольный напиток; счёт «ровно» (в теннисе и др.)». «(в теннисе и др.)»
  follows EN "sports deuce".
- Line 23: «…— это счёт «ровно». Так называют не любой равный счёт: в теннисе, настольном теннисе, волейболе и некоторых
  других играх это равенство, при котором каждой стороне не хватает одного очка до победы в гейме или партии. Дальше
  побеждает тот, кто выиграет два очка подряд. В теннисе это 40:40 и каждое следующее равенство в том же гейме, а счёт
  15:15 так не называют.» Evidence: the デジタル大辞泉 and 精選版 日本国語大辞典 ジュース (deuce) entries on Kotobank, both of
  which name tennis, table tennis and volleyball; tennis-hub «Ровно (Deuce)» as 40:40.
- Line 25: the example «— В теннисном матче счёт стал «ровно» (40:40).»
- Lines 29 and 37: «спортивный счёт» instead of «теннисный счёт», matching the multi-sport scope.
- Line 9: `quiz_exclusions: [飲み物]`. Fix 1's 等しい guard was withdrawn because «равный» left the title.

Before each fix commit, the coordinator's word title screen ran on the changed titles (カード, ダイヤ, スター, スタンド and
ジュース):
- After fix 1, the only new exact segment was スター «звезда» = 星, already guarded. The new stems were ジュース «равный»
  ~ 等しい (guarded in fix 1) and 匹敵 «не уступать; быть равным», and スタンド «напольная» ~ 畳 «татами (напольный мат)»,
  半ば and 満ちる. These are stem neighbours with different referents, so no guard was added. カード «молочный» and ダイヤ
  «алмаз» had no overlaps; 牛乳 and ミルク share only «моло», not the «молоч» stem.
- After fix 2, ジュース's title added no overlap: fix 1's «равный» neighbours disappeared, and «ровно» does not reach 平ら
  «ровный». Every other overlap the screen listed was already present on the candidate.

Net change from the candidate:
- five retitles (カード, ダイヤ, スター, スタンド, ジュース);
- body wording in カード, ジュース, スープ, トラック and ダイヤ's source line;
- two example translations (カード, ジュース);
- four added exclusion entries on three cards (トラック, デート, スタンド);
- one added link (ソファー→ベンチ).

No Japanese example sentence, sourced reading or EN exclusion changed. Across both fixes the content diff is nine word files,
44 lines added and 44 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, one reviewer at a time, in this order:
1. Correctness round 1, on fix 1. Its finding R1 led to fix 2.
2. Correctness round 2, on fix 2, for R1 only.
3. Consistency, on fix 2.
4. Comprehensibility, on fix 2.

Each reviewer appended to its own report file, which stayed in its session context. Each recheck brief gave the reviewer:
- the fix commit or commits, the reviewed candidate as the base, and the read-only rules;
- the actual content diff: `d0d6d08..b00e465` for correctness round 1, `b00e465..a1fe63a` for round 2, and the cumulative
  `d0d6d08..a1fe63a` for consistency and comprehensibility;
- the coordinator's evidence for every change, the title-screen results and the declined items, stated without the other
  reviewers' reports. The consistency and comprehensibility briefs said in one sentence that fix 2 followed the
  correctness recheck, and why;
- the reviewer's original verdicts and the disposition of each of its own findings.

The three briefs longer than about 20 KB were delivered as session files that the reviewers were told to read in full; the
second correctness brief was sent inline.

All recheck messages forbade running `tools/build_manifest.py` or any other generator. Every recheck section states that
none was run. The correctness reviewer ran `tools/validate.py` in both rounds (0 errors each), and the consistency reviewer ran
it once (0 errors), then deleted the untracked `tools/__pycache__` its run had left. The comprehensibility reviewer reported
running no validator. The fix scripts checked `git status --porcelain` after each fix commit, and after the consistency
and comprehensibility rechecks the coordinator confirmed that HEAD was `a1fe63a` and that
`git status --porcelain --ignored` was empty.

### Round 1 (`b00e465`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer checked the actual nine-card diff against the original review and frozen EN; it did not re-review unchanged cards in full. C1 is resolved: the scraper is now a sense of Japanese カード, not of Russian «карточка». C2 is resolved: contextual examples replace the exhaustive Russian restriction. C3 is resolved for all three titles and the ダイヤ source description. C4 is resolved: the relative ベンチ link works. The separate curd entry remains accurate as coagulated milk used for cheese, not finished cheese (a cheesemaking text on milk coagulation). トラックに乗る «ехать на грузовике» is natural and specifies neither driver nor passenger, cab nor bed. The added exclusions remove no original entry. **R1** (minor; high confidence), `ジュース.md:4,12,23,25`: the new «равный счёт» and «счёт стал равным» replace the specific deuce with generic equality, which includes 15:15 and 30:30; mentioning the umpire's call in line 23 does not restrict the title or restore the example. Remedy: a noun phrase such as «счёт „ровно“ (в теннисе)», keep the technical state in the example, and distinguish it briefly from arbitrary equality. Evidence: the デジタル大辞泉 sports entry on Kotobank requires the particular late-game tie; tennis-hub defines «Ровно (Deuce)» as 40:40 in a game. The スープ optional item is resolved; the postcard and baseball-title items stay optional and declined. Correctness and scoped coverage remain **NEEDS FIX** (R1 only). |

### Round 2 (`a1fe63a`)

| Facet | Scope and result |
|---|---|
| Correctness | R1 only: the reviewer read the actual ジュース diff from `b00e465` and the full revised card. R1 is resolved: lines 4, 12, 23 and 25 keep deuce as the named score, exclude arbitrary equality (15:15) and identify 40:40 and later ties in the same tennis game; the «(40:40)» parenthesis explains the technical state rather than inventing a different event. The late-game tie and two-consecutive-point definition match the デジタル大辞泉 and 精選版 日本国語大辞典 sports entries, freshly inspected on Kotobank; both name tennis, table tennis and volleyball, which supports the multi-sport scope and the «спортивный счёт» wording on lines 29 and 37 without conflating the beverage entry. The withdrawn 等しい exclusion had been introduced only for the removed «равный» label; 飲み物 remains. The earlier optional numerical clarification is now adopted in the body and example. Correctness and scoped coverage are **CLEAN** within the combined review and recheck scope. |
| Consistency | F1 is resolved: `[車, 自動車]`, both targets exist, following the バス and タクシー precedent (conservative to required). F2 is resolved: `[月日, 日付]` (conservative). F3 is resolved: ガソリンスタンド exists and the body teaches that sense (required). F4 is resolved: 明かり names the same lamp sense as 電灯 (conservative). F5 is resolved: the ベンチ link resolves, and RU-only links are now eight. The optional 灯 pair and トラック→乗り物 are withdrawn as not needed. Regression checks: screened against all word titles, カード «молочный сгусток», ダイヤ «алмаз» and スタンド «напольная» introduce no new exact segment or stem clash (畳 is a stem neighbour only); スター «звезда» equals 星's whole title, already guarded by `[星, 有名]`; withdrawing 等しい is correct because «равный» is gone. ジュース «счёт «ровно»» shares the bare word «счёт» with 会計 and 勘定 (as the candidate's «счёт в теннисе» already did), but the sense qualifier differs and the pair is not a real confusion: **optional, no fix needed**. The スタンド, トラック and デート lists are well-formed and deduplicated, target existing word files and retain EN's entries. The text-only edits touch no link or front-matter key beyond those above. All nine changed and 37 intake `words/` payload hashes equal the raw file SHA-256 in both `manifest.json` and the intake. Consistency, quiz safety and scoped coverage of cross-file integration are **CLEAN**. |
| Comprehensibility | Item 1 is resolved: カード lines 4, 12 and 21 say «молочный сгусток», defined in the same sentence as the coagulated milk mass from which cheese is made, with the example «Сыр делают из молочного сгустка»; omitting «(для сыра)» from the title does not restore the cheese-clot reading. Item 2 is resolved: ジュース names a score, «счёт «ровно» (в теннисе и др.)», not the bare adverb; the body excludes an arbitrary level score, explains the win-by-two tie and pins tennis to 40:40 rather than 15:15, and the example adds «(40:40)». The reviewer judged that its own earlier «равный счёт» remedy would have included 15:15, so this wording is the right close; it checked the deuce sentences against the same Kotobank entries. The トラック optional item is resolved (adopted); the グランド comma title stays optional and declined. No regressions: カード:31 keeps the 地図 contrast without the unsupported "only" rule, and :35 attributes the scraper to Japanese カード; ダイヤ's «алмаз; бриллиант» matches the body and the ring example; スター's title matches the opening sentence, with the symbol and sky senses in the body; スタンド's lamp gloss now includes the floor lamp the body taught; スープ:20 is the qualified form of the same point; the ベンチ link reads as a bench, not a sofa. The reviewer did not score the exclusions. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: カード attributes the dough-scraper sense to Russian «карточка» (minor) | **Resolved** | `カード.md:35`; JMdict 1036400 sense 7. |
| Correctness C2: カード's exhaustive «только» restriction on «карта» (minor) | **Resolved** (modified wording) | `カード.md:31`; Gramota карта sense 3; Russian Wiktionary карта sense 3. |
| Correctness C3: the ダイヤ, スター and スタンド titles narrow the headword (minor) | **Resolved** | `ダイヤ.md:4,12,36`, `スター.md:4,12`, `スタンド.md:4,12`; Gramota бриллиант; EN titles; JMdict 1069930 sense 4. |
| Correctness C4: ソファー leaves the compared ベンチ unlinked (minor) | **Resolved** (jointly with consistency F5) | `ソファー.md:28`; `words/ベンチ.md` exists. |
| Correctness R1 (recheck of fix 1): ジュース «равный счёт» includes non-deuce ties (minor) | **Resolved** by fix 2 | `ジュース.md:4,12,23,25,29,37`; デジタル大辞泉 and 精選版 日本国語大辞典 on Kotobank; tennis-hub. |
| Correctness optional: スープ:20 «обычно говорят „есть суп“» | **Optional, adopted** | `スープ.md:20`. |
| Correctness optional: «поздравительную открытку» | **Optional, not adopted** | «Поздравительная карточка» is ordinary Russian, keeps the title word visible and matches line 29. Declined. |
| Correctness optional: センター «(в бейсболе)» on the player gloss | **Optional, not adopted** | The body and the example note give the baseball context; the title is already long. Declined. |
| Correctness optional: ジュース «40:40 и последующие равенства в гейме» | **Optional, adopted** (through R1) | In the body and the example, not the title (`ジュース.md:23,25`). |
| Consistency F1: トラック leaves 自動車 unguarded (minor) | **Resolved** | `トラック.md:9`; `words/バス.md` and `words/タクシー.md` precedent. |
| Consistency F2: デート leaves 日付 unguarded (minor) | **Resolved** | `デート.md:9`; JMdict 1081430 sense 2; 日付 «дата». |
| Consistency F3: スタンド leaves ガソリンスタンド unguarded (minor) | **Resolved** | `スタンド.md:9`; the card's own body. |
| Consistency F4: スタンド leaves 明かり unguarded (minor) | **Resolved** | `スタンド.md:9`; 明かり «свет; светильник» and its own 電灯 guard. |
| Consistency F5: ソファー's plain ベンチ mention (minor or optional) | **Resolved** (merged with correctness C4) | `ソファー.md:28`. |
| Consistency optional: スタンド→灯 and トラック→乗り物 | **Withdrawn** | 灯 «свет лампы; огонёк» does not name the object; the 飛行機 precedent does not guard 乗り物. The reviewer agreed in its recheck. |
| Consistency recheck optional: ジュース «счёт» shared with 会計 and 勘定 | **Optional, no change** | Different sense qualifiers; the candidate's title already shared the bare word. |
| Consistency limit: `strokes/*.json` manifest hashes differ from raw bytes | **Not a defect** | `tools/build_manifest.py:18-19` hashes text payloads after CRLF-to-LF normalisation, and the byte-copied EN stroke files contain CRLF; the batch does not touch them. |
| Comprehensibility 1: カード «сырный сгусток» reads as a cheese clot (minor) | **Resolved** (modified) | `カード.md:4,12,21`; Jisho's separate カード curd entry. «Молочный сгусток» instead of the reviewer's «сгусток молока (для сыра)». |
| Comprehensibility 2: ジュース «ровно» as a bare adverb (minor) | **Resolved** (by fix 1, then fix 2) | `ジュース.md:4,12,23,25`; the reviewer's recheck. Fix 1's «равный счёт» was superseded after R1. |
| Comprehensibility optional: トラック «ехать на грузовике» | **Optional, adopted** | `トラック.md:21`. |
| Comprehensibility optional: グランド's comma title | **Optional, not adopted** | The reviewer called it not a wrong gloss, and the body explains the compound use. Declined. |
| Exclusion classification | **Reviewer's classification adopted** | The author's and reviewer's candidate classifications differ only in strength (table in review 001): the reviewer rates eleven author-"conservative" entries on nine cards as required. For the fix entries the reviewer classed スタンド→ガソリンスタンド as required (the coordinator's disposition had said conservative), トラック→自動車 as conservative to required, and デート→日付 and スタンド→明かり as conservative. Fix 1's ジュース→等しい was withdrawn in fix 2. |

Cross-batch note: links to absent targets stay plain. Two EN link occurrences in this batch's new cards target absent RU
files: テント→キャンプ and サービス→ただ (line 28 of each card). キャンプ is a Batch 223 word, so its link from テント is held for
that batch; ただ is not in Batch 223. The ベンチ→ソファー link held by Batch 221 was restored in this batch.

## Final exclusion set

All 18 EN exclusion entries (13 lists) are retained. Twenty-five direct, one-sided entries are added on 18 new cards (eight of
them new lists):

- Required (18): チャンス→望み, ダンス→踊り, ジェット機→飛行機, ゲーム→遊び, グランド→大きい and グランド→大きな; the eleven
  entries the reviewer raised from the author's "conservative", namely カード→地図, トラック→車, チーム→命令, ダイヤ→宝石,
  ダイヤ→玉, ダイヤ→予定, スター→有名, スタンド→電灯, ジーンズ→ズボン, ジュース→飲み物 and グループ→クラス; and, added in fix 1,
  スタンド→ガソリンスタンド.
- Conservative to required (1): トラック→自動車, added in fix 1.
- Conservative (6): タイプライター→機械, センター→選手, スタンド→受付 and サービス→無料 (the reviewer's "leaning required"), and,
  added in fix 1, デート→日付 and スタンド→明かり.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the fixes (カード, ダイヤ, スター, スタンド; ジュース after fix 2).
- Scoped coverage: **CLEAN** after the fixes (the ダイヤ, スター and スタンド titles, ソファー's navigation and ジュース's deuce
  definition).

- Comprehensibility: **CLEAN** after the fixes (カード, ジュース).

- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after fix 1 (トラック, デート, スタンド). This covers the reviewed batch and the directly adjudicated
  pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the cards needed to judge them. The unchanged cards rest on review
  001's full reading.
- The consistency reviewer's stem screen reported 252 word titles, although the RU repository had 3,313 word cards at
  the candidate (3,283 before this batch); the coordinator's own title screens covered all word titles, and the consistency
  recheck screened the changed titles against all of them.
- No native certification was obtained for «молочный сгусток» or the tennis call «ровно»; ScanDict for the センター player
  sense is usage-only evidence.
- The comprehensibility reviewer could not open JMdictDB, which was password-gated, and relied on the Jisho API,
  JapanDict and Kotobank.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
