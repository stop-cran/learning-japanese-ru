# Batch 244 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `c21597475cf24f578b35cc6636257450f8a80902` | `ba7eb57a671e3585fadb94026d9d505021a0444a` | Initial review snapshot: the signed candidate, on `origin/full-ru-244-words-83`. |
| `149b7d7a4e39a451f5dc9acf61d932162fccc25a` | `cf7886d9e0b39a6cde7cb25034fdd65d929ba04e` | Fix 1. It covers the correctness UNVERIFIED そのうえ root claim and the correctness optional on 紫, consistency F1 to F5 and comprehensibility C1 to C6, C8 and C10 to C18 (C1, C4, C10 and C12 in reworded form; C3, C6, C16 and C17 partially). It retitles 純粋, adds eight exclusions and one reviewed RU-only link, and removes no exclusion or link. Signed. |
| `fd4ae41f73627dd265516bc898bd4ace41dcbd03` | `94ea84ff83170eea51081a066405390b8b3ee2fe` | Fix 2: correctness recheck R1, the construction note at そのうえ:48–49. Signed. |
| `c4ba4be0720d82ebf4916c840d8d6baf79497457` | `f57bb98c2fe6e3a770c506358e8ace15e586f2eb` | Fix 3: the correctness recheck optional, the qualified substitution note at 素質:50. Signed. |
| `85a96a258bf3ce7fbdfa6222f766088c90d18bb4` | `f6e6c9aa1719e22a4e9a24ccaaa8bf3de6ce587c` | Fix 4 (final candidate): comprehensibility C16, maintained at its recheck; retitles 書留 and removes fix 1's 書留→チェック exclusion. Signed; on `origin/full-ru-244-words-83`. |

Each fix regenerated `manifest.json`; every snapshot records 5,439 entries (5,434 `files` + 3 images + 2 scenes).
`contentVersion` is `3e1149c3d5d019ad` at the candidate, `c713de93e440c110` after fix 1, `70ba24d88bd0d212` after fix 2,
`e5d4af622b389276` after fix 3 and `4cde7d763e8ccfa1` after fix 4. The intake was not refreshed; it still records the
candidate's payload hashes. The commit messages read:
- fix 1: "Batch 244: apply review fixes / Correctness (そのうえ), consistency F1-F5 and comprehensibility C1-C6, C8,
  C10-C18 (C7, C9, C19 declined; see dispositions):", followed by a bulleted list of the changes;
- fix 2: "Batch 244: narrow the そのうえ construction note (correctness recheck R1)";
- fix 3: "Batch 244: qualify the 素質 substitution note (correctness recheck option)";
- fix 4: "Batch 244: render 書留 "written record" as «письменная запись» (comprehensibility recheck C16)".

Fix 1:
- `そのうえ` (lines 9, 42 and 48–49; the correctness UNVERIFIED claim, comprehensibility C17 partial and C18): 余計
  appended to `quiz_exclusions`; «Для физического положения [上](上.md) противопоставлено [下](下.md)（した）.» instead of
  «Для физического положения 上 противопоставлено…», a reviewed RU-only link (EN has plain text); «Чтобы отличить
  добавление от физического положения, смотрите на конструкцию: связка そのうえ вводит новый факт, а その上に при глаголе
  указывает место.» instead of «Как в русском «сверх того» и «сверху» связаны общим корнем, но значат разное, смотрите на
  конструкцию, чтобы отличить добавление от физического положения.» The title «сверх того; притом» is kept.
- `純粋` (lines 4, 12 and 19; comprehensibility C15 and C14): title and H1 «чистый (без примесей); неподдельный» instead
  of «чистый; неподдельный; без примесей»; «Я спросил из неподдельного любопытства.» instead of «…из искреннего
  любопытства.»
- `書留` (line 9; comprehensibility C16 partial): チェック appended to `quiz_exclusions`; the title «заказное
  отправление; письменная отметка» is kept.
- `性質` (lines 47–48; comprehensibility C1 reworded): «его внутренние свойства. Имущество, которым владеют, — это
  [財産](財産.md), а не 性質.» instead of «…Русское «свойство» здесь не связано с «собственностью»: имущество, которым
  владеют, — это [財産](財産.md).»
- `素人` (lines 29–30; comprehensibility C2): «отмечает しろうと как особое чтение всего слова: запоминайте 素人 целиком,»
  instead of «…всего слова. На карточке используется категория приложения jukujikun для такого чтения: запоминайте 素人
  целиком,».
- `算盤` (lines 32–33; comprehensibility C3 partial): «Метка `jukujikun` (чтение, присвоенное всему слову) отмечает здесь
  эту стратегию заучивания целого слова; …» instead of «Категория приложения `jukujikun` отмечает здесь…».
- `素質` (lines 48–50; comprehensibility C4 reworded): «Русские слова «характер» и «качества» соответствуют разным
  японским словам: [人物](人物.md) и [カラー](カラー.md) тоже связаны с человеком или его особенностями, но не заменяют 素質 в
  предложении.» instead of «…соответствуют нескольким словарным статьям; исключения в викторине не делают [人物](人物.md)
  или [カラー](カラー.md) свободно взаимозаменяемыми с 素質 в предложении.»
- `素直` (lines 9, 20 and 34–35; consistency F2, comprehensibility C5 and C6 partial): おとなしい appended to
  `quiz_exclusions`; «У него покладистый характер, и он умеет прислушиваться к советам.» instead of «…и он охотно
  прислушивается к советам.»; «Чтение соединяет онное ス с исконным なお. Это смешанное чтение, а не два обычных онных
  чтения.» instead of the sentence on how «Эта коллекция относит смешанное чтение…».
- `系統` (line 41; comprehensibility C8): «Других значений, которые встречаются в учебных списках, но не подтверждаются
  проверенными словарными определениями, эта статья не учит.» deleted.
- `作者` (lines 38–39; comprehensibility C10 reworded): «Чем 作者 отличается от 作家 и как различаются окончания 者 и 家,
  объясняется в статье об окончаниях профессий и ролей.» instead of «Сравнение 作者 с 作家 и окончаний 者 и 家 см. в статье
  об окончаниях профессий и ролей.» The article mention stays unlinked because RU has no such article.
- `紺` (line 19; comprehensibility C11): «Эта униформа тёмно-синяя.» instead of «Эта форма тёмно-синяя.»
- `紫` (line 21; comprehensibility C12 reworded and the correctness optional): «…растение воробейник краснокорневой,
  которое обычно пишут» instead of «…растение воробейник (лат. Lithospermum erythrorhizon), которое обычно пишут»
  (Plantarium item 23077).
- `純情` (line 19; comprehensibility C13): «Пожалуйста, не подшучивайте над её невинностью.» instead of «Пожалуйста, не
  смейтесь над её невинностью.»
- Exclusion-only changes (line 9 each): 組み立てる +集める, 拾う (consistency F1; 集まる not added); 終点 +停留所 (F3);
  等分 +区分 (F4); 気配 +機嫌 (F5).

Fix 2:
- `そのうえ` (lines 48–49; correctness recheck R1): «Чтобы отличить добавление от физического положения, смотрите на
  конструкцию и контекст: связка そのうえ вводит новый факт, а в примере с коробкой その上に указывает место.» This is the
  reviewer's remedy plus «и контекст», which the dispositions say "restores EN's point that the construction and its
  context, not the shared phrase, decide the reading".

Fix 3:
- `素質` (line 50; correctness recheck optional): «не могут свободно заменять 素質» instead of «не заменяют 素質»,
  "restoring EN's qualified "not freely interchangeable" instead of a categorical rule".

Fix 4:
- `書留` (lines 4, 9, 12 and 21; comprehensibility C16): title and H1 «заказное отправление; письменная запись» instead of
  «заказное отправление; письменная отметка»; «значение письменной записи» instead of «значение письменной отметки»; fix 1's
  チェック exclusion removed, because it "guarded only the dropped «отмет» stem". The final list is
  `[郵便, 便, 記録, メモ, ノート, 書き取り, 速達]`.

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- The correctness reviewer's optional wording for そのうえ was not used "because it still leans on a Russian word pair";
  its 絞る «В рецепте:» label was declined ("the cooking context is clear").
- Consistency's optional EN-inherited format points (算数 tags and URL, 紫 `colors`, kana spacing in 作者 and 算数) were
  declined ("byte-faithful to EN metadata or EN example formatting"); 算数:18 was declined under comprehensibility C9; the
  guards 筆者/私 and 第一/主要 were declined ("The word title screen finds no shared segment or stem"; "第一 already guards
  重要, 大事, 大切"). The reviewer accepted these declines at recheck.
- Comprehensibility C3 was adopted partially: the reviewer "assumed learners never see the `type` label, but the quiz hint
  shows it (kanji-cards-android `WordQuizScreen.kt:150` filters only wago/kango/gairaigo), and EN keeps the sentence", so
  the sentence now explains the label. C6 was adopted partially: the proposed «внимательно слушает» "would turn よく聞く
  into attentiveness while listening". The reviewer did not maintain either point.
- C7 (系統 «система; линия происхождения») was declined: bare «система» "would be an exact segment of guarded 機関" and
  «линия происхождения» "adds unguarded stem overlaps (出身, 原産, 産地 «происхожд-»)". C9 (算数:18 «по арифметике») was
  declined: "EN has the same pairing" and «по арифметике» "would sound dated". C19 (筆記 «ведение записей») was declined:
  it "suggests record-keeping". The reviewer accepted all three declines.
- C16 and C17 were first adopted as guards with the titles kept (書留→チェック; そのうえ→余計). The reviewer did not maintain
  C17 but maintained C16 at low severity; fix 4 then changed the 書留 title and removed チェック.
- C12 was accepted without the dye parenthetical, since "line 28 already explains the root dye"; the reviewer did not
  maintain that part. The comprehensibility optionals (第一, 粒, pronoun supply, «электропоезда», dropped English-only
  warnings) needed no change.

Post-fix screens: a saved rerun at `149b7d7` over 純粋 (`b244-postfix-screen.txt`, 21 lines) finds three exact-segment
hits for «чистый», with きれい, 清い and 清潔, all guarded by 純粋's EN exclusions, and 18 stem-only lines; the dispositions
record that the screen on 純粋, そのうえ and 書留 found "no unguarded whole-segment overlap (stem-only hits only, all
pre-existing apart from the newly guarded ones)". A saved rerun at `85a96a2` over 書留 (`b244-fix4-screen.txt`, 29 lines)
finds no exact-segment hit: 4 guarded stem leads (メモ, 筆記 and 記録 on «запис», 速達 on «отпра») and 25 unguarded
stem-only leads. The consistency addendum calls «запись» with 記録 "the only whole-segment overlap" and notes that it "is
guarded by the EN exclusion 記録".

筆記's EN `quiz_exclusions` contains 書留, and a declared pair "is excluded in both directions even if only one article
declares it" (EN `docs/content-format.md`, lines 162–163; Android `Words.kt:177–180`), so 書留–筆記 is guarded in both
directions without a new entry; the consistency addendum: "筆記 «записывание» declares 書留 in its own exclusions, and the
pair is symmetric."

Net change from the candidate:
- titles and H1s of 純粋 and 書留;
- example translations in 純粋, 純情, 紺 and 素直;
- prose in そのうえ, 作者, 性質, 書留, 算盤, 素人, 素直, 素質 and 紫, and the deleted 系統:41 sentence;
- seven exclusions added (組み立てる→集める and 拾う, 素直→おとなしい, 終点→停留所, 等分→区分, 気配→機嫌 and そのうえ→余計);
  fix 1's 書留→チェック was added and then removed by fix 4;
- one reviewed RU-only link added (そのうえ:42 → 上); no link removed or retargeted.

No Japanese example sentence, sourced reading, kanji card, navigation file or EN exclusion changed. The content diff
`c215974..85a96a2 -- words` is 17 word files, 31 lines added and 33 removed; with `manifest.json` the fixes change 18
files, 49 lines added and 51 removed. Fix 1 alone changes 17 word files (29 added, 31 removed); fixes 2, 3 and 4 each
change one word file and `manifest.json`.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the initial reports state "Model identity not verifiable." and "Model: not verifiable.", the consistency report makes
no statement about its model, and the comprehensibility recheck and addendum repeat "Model name not verifiable."

The rechecks ran serially, one reviewer at a time, in three rounds. In round 1 the correctness reviewer rechecked fix 1
(diff `c215974..149b7d7`: 17 word cards and `manifest.json`) and raised R1. After fixes 2 and 3, round 2 ran consistency
and then comprehensibility, each on the cumulative diff `c215974..c4ba4be`; comprehensibility maintained C16. After fix 4,
round 3 ran addenda on `85a96a2`: correctness on fixes 2 to 4, then consistency and comprehensibility on fix 4. The briefs
sent were `b244-recheck-msg-correctness.txt` (round 1), `b244-recheck-msg-consistency.txt` and
`b244-recheck-msg-comprehensibility.txt` (round 2), and `b244-recheck2-msg-correctness.txt`,
`b244-recheck3-msg-consistency.txt` and `b244-recheck3-msg-comprehensibility.txt` (round 3). This ordering rests on the
coordinator's session records; the recheck sections do not record times. No round-3 addendum raised a new finding, so
there was no fifth fix.

Each reviewer appended its recheck to its own report file: correctness under `## Recheck (149b7d7)` and
`### Recheck addendum (R1)`, consistency under `## Recheck (c4ba4be)` and `### Recheck addendum (fix 4)`, and
comprehensibility under `## Recheck (c4ba4be)` and `### Recheck addendum (C16)`.

No recheck ran a generator. The correctness reviewer records "No generator run; read-only validator 0 errors, diff --check
clean." at `149b7d7` and again at `85a96a2`; the consistency reviewer ran `tools/validate.py` at `c4ba4be` (0 errors) and
records "I ran no generator and wrote nothing to any repository", and at `85a96a2` "No generator was run and nothing was
written to any repository" (validator not rerun); the comprehensibility reviewer records "No generator was run." and
"validate.py not run." at `c4ba4be` and "No generator was run." at `85a96a2`. The correctness sections record HEAD
`149b7d7a4e39a451f5dc9acf61d932162fccc25a` and HEAD `85a96a258bf3ce7fbdfa6222f766088c90d18bb4`, each with "initial/final
status empty"; the consistency sections record HEAD `c4ba4be0720d82ebf4916c840d8d6baf79497457` with "the working tree was
clean at the start" and HEAD `85a96a258bf3ce7fbdfa6222f766088c90d18bb4` with "the working tree was clean"; the
comprehensibility sections record HEAD `c4ba4be0720d82ebf4916c840d8d6baf79497457` and HEAD
`85a96a258bf3ce7fbdfa6222f766088c90d18bb4`, each with "status empty". The recheck records include no separate coordinator
status check after the rechecks; when these records were drafted, a read-only check showed the RU checkout on
`full-ru-244-words-83` at HEAD `85a96a258bf3ce7fbdfa6222f766088c90d18bb4` with `git status --porcelain --ignored` printing
nothing.

### Round 1 (`149b7d7`)

| Facet | Scope and result |
|---|---|
| Correctness | "Snapshot: HEAD 149b7d7a4e39a451f5dc9acf61d932162fccc25a; initial/final status empty." "All 17 changed cards read fully; every changed passage checked against the candidate, relevant frozen EN and dictionary evidence; words/上.md read fully." "Old UNVERIFIED root claim RESOLVED by removal, but its replacement has R1 below." "Interim 絞る C1 remains WITHDRAWN; recipe label remains OPTIONAL, not required." "紫 species-name suggestion RESOLVED (prior inspected Plantarium item 23077)." "性質, 素人, 素直 and 系統 machinery suggestions RESOLVED; 算盤 PARTIALLY RESOLVED (explained label is factually acceptable, annotation remains optional polish)." "素質 wording improved; optionally restore “not freely interchangeable” rather than the categorical “не заменяют”." 純粋 (JMdict 1341930), 紺 (Daijisen 制服, sense 1), 純情 (Daijisen からかう sense 1), 素直 and the rewritten 性質/素人/算盤/作者 passages accepted; "上 link is appropriate and the explicitly authorized EN-link exception. New guards all exist; Japanese example strings unchanged". R1 (medium, high confidence), `そのうえ.md:49`: "“その上に при глаголе указывает место” overgeneralizes: その上に can also add a fact with a verbal predicate" (Saito example 彼に払うべき金を払ったその上に礼をした; 実用日本語表現辞典 その上に "additional"). Correctness **NEEDS FIX** (R1); scoped coverage **CLEAN**. Limits: "Prior botanical evidence reused after refresh returned 504. APK/automatic quiz pools not audited." |

### Round 2 (`c4ba4be`)

| Facet | Scope and result |
|---|---|
| Consistency | "HEAD is c4ba4be0720d82ebf4916c840d8d6baf79497457 and the working tree was clean at the start. `tools/validate.py` reports 0 errors." F1 ("集まる was not added, which I had listed as optional"), F2, F3, F4 and F5 **resolved**; the RU-added guards 作者→著者, 性質→性能 and 書留→速達 "kept, which I accepted"; 素質 «исключения в викторине» **resolved**; "算数:18, the EN-inherited format points, and the 筆者/私 and 第一/主要 guards: **withdrawn / optional, declined with a stated rationale**. I accept that." Regression checks: fixes 2 and 3 touch only `manifest.json`, そのうえ and 素質, with "No title, exclusion, link or navigation file changes in them"; 純粋's title equals its H1, and the exact segment «чистый» appears only on きれい, 清潔 and 清い, "All three are in 純粋's exclusions"; "書留→チェック: sound"; "そのうえ→余計: sound"; the そのうえ→上 link "is a reviewed RU-only link on a new batch card, not a navigation file, so navigation stays at 4 files and 4 links"; "No orphaned references"; "manifest.json changed only in hashes and contentVersion". Consistency, format, links and navigation **CLEAN**; quiz safety **CLEAN** ("F1–F5 resolved, no new ambiguity"). Limits: "the manifest hashes were not recomputed independently. A scripted whole-tree pass hung and was abandoned."; strokes CRLF hashing and the two scenes outside the manifest remain out of scope. |
| Comprehensibility | "HEAD c4ba4be0720d82ebf4916c840d8d6baf79497457; status empty. Judged the 17-card words diff on the files." C1, C2, C4 ("Fix 3 «не могут свободно заменять» is the qualified contrast, not a regression"), C5, C8, C10, C11, C13, C14, C15 ("«чистый» still pairs only with excluded きれい, 清い, and 清潔") and C18 **resolved**; C3 "partially resolved; I do not maintain a further change"; C6 resolved ("I do not maintain «внимательно»"); C12 resolved ("I do not maintain the dye parenthetical"); C17 resolved ("I do not maintain a title change. 余計 is now excluded"); C7, C9 and C19 "decline accepted; I do not maintain". "C16 partially resolved; I maintain the gloss, now low. The チェック exclusion fixes the stem collision. «письменная отметка» still reads as a mark or grade, not EN "written record"." "そのうえ:48–49 (fix 2): no regression." Comprehensibility **NEEDS FIX** (C16 unresolved, low); scoped coverage **CLEAN**. Limits: "quiz-hint source not in this checkout; title screen not re-run; 出身 stem checked. Model name not verifiable." |

### Round 3 (`85a96a2`)

| Facet | Scope and result |
|---|---|
| Correctness | "Snapshot: HEAD 85a96a258bf3ce7fbdfa6222f766088c90d18bb4; initial/final status empty." "All three cards read fully; changed passages checked against frozen EN and actual JMdict." "R1 RESOLVED: そのうえ:48–49 now limits the spatial reading to the box example … it no longer claims every その上に with a verb is spatial." "Optional 素質:50 RESOLVED: “не могут свободно заменять” restores EN's qualified “freely interchangeable”." 書留's title and record sentence "retain both EN senses" (JMdict 1589960 sense 2); "Removing チェック establishes no correctness problem". Correctness **CLEAN**; scoped coverage **CLEAN**. "No new regression or outstanding finding established." Limits: "No exhaustive APK/automatic quiz-pool audit; remaining annotation polish stays optional." |
| Consistency | "HEAD is 85a96a258bf3ce7fbdfa6222f766088c90d18bb4 and the working tree was clean. The diff from c4ba4be touches only `words/書留.md` and `manifest.json`." Title equals H1; "The manifest changed only in `contentVersion` and the 書留 hash." The «запись» overlap with 記録 is guarded; 筆記's pair is symmetric; メモ is guarded; other «запис» hits are parenthetical or different senses; "Nothing new turned up in the pool or in the b245–b251 lane titles."; "Removing チェック is safe." Consistency, format, links and navigation **CLEAN**; quiz safety **CLEAN**. Limits: "I did not independently recompute the manifest hash. I did not run `tools/validate.py` again on this HEAD. I screened the lanes by title grep only." |
| Comprehensibility | "HEAD 85a96a258bf3ce7fbdfa6222f766088c90d18bb4; status empty. Read words/書留.md only." "C16 resolved. Title, H1, and the meaning sentence now say «письменная запись», which renders EN "written record" and no longer reads as a mark or grade. «письменная» blocks an audio-recording reading." "Dropping チェック is right: that guard only covered the removed «отмет» stem." "No comprehension regression." Comprehensibility **CLEAN**; scoped coverage **CLEAN**. Limits: "title screen not re-run. Model name not verifiable." |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness UNVERIFIED: そのうえ:48 «связаны общим корнем» | **Resolved** by removal (fix 1); the replacement raised R1 | `そのうえ.md:48–49`; Tikhonov segmentations via ru.wiktionary. |
| Correctness R1: そのうえ:49 «その上に при глаголе указывает место» overgeneralizes (medium) | **Resolved** (fix 2; reviewer remedy plus «и контекст») | `そのうえ.md:48–49`; Saito example via weblio; 実用日本語表現辞典 その上に. |
| Correctness interim C1: 絞る:19 imperative | **Withdrawn** by the reviewer | Procedural ます may be rendered as a Russian imperative. |
| Correctness optional: 絞る «В рецепте:» label | **Optional**; declined | "the cooking context is clear". |
| Correctness optional: 紫 species name | **Resolved** under comprehensibility C12 | `紫.md:21`; Plantarium item 23077. |
| Correctness optional: 性質, 素質, 素直, 素人, 算盤 and 系統 machinery wording | **Resolved** under comprehensibility C1 to C5 and C8; 算盤 **partially resolved**, annotation optional | As those findings. |
| Correctness optional: そのうえ alternative wording | **Optional**; not used | "still leans on a Russian word pair". |
| Correctness recheck optional: 素質 "not freely interchangeable" | **Resolved** (fix 3) | `素質.md:50`. |
| Consistency F1: 組み立てる lacks 集める, 拾う (required) | **Resolved** | `組み立てる.md:9`. |
| Consistency F2: 素直 lacks おとなしい (conservative) | **Resolved** | `素直.md:9`. |
| Consistency F3: 終点 lacks 停留所 (conservative) | **Resolved** | `終点.md:9`. |
| Consistency F4: 等分 lacks 区分 (conservative, low) | **Resolved** | `等分.md:9`. |
| Consistency F5: 気配 lacks 機嫌 (conservative, low) | **Resolved** | `気配.md:9`. |
| Consistency classification of the RU-added exclusions | **Recorded**; all three kept | See the final exclusion set. |
| Consistency optionals: EN-inherited format points, 算数:18, guards 筆者/私 and 第一/主要 | **Withdrawn / optional**, declines accepted at recheck | Byte-faithful to EN; no shared segment or stem; 第一 already guards 重要, 大事, 大切. |
| Consistency optional: 素質 «исключения в викторине» | **Resolved** under comprehensibility C4 | `素質.md:48–50`. |
| Consistency limits: strokes CRLF hashes, two scenes outside the manifest | Outside the batch; unchanged | Pre-existing; not batch content. |
| Comprehensibility C1: 性質:48 «собственность» aside (medium) | **Resolved** (reworded remedy) | `性質.md:47–48`. |
| Comprehensibility C2: 素人:30 app-category clause (medium) | **Resolved** | `素人.md:29–30`. |
| Comprehensibility C3: 算盤:32 invisible label (medium) | **Partially resolved**; not maintained | `算盤.md:32–33`; the quiz hint shows the label (`WordQuizScreen.kt:150`). |
| Comprehensibility C4: 素質:49 quiz-metadata wording (medium) | **Resolved** (reworded; qualified by fix 3) | `素質.md:48–50`. |
| Comprehensibility C5: 素直:34 collection clause (medium) | **Resolved** | `素直.md:34–35`. |
| Comprehensibility C6: 素直:20 «охотно» (medium) | **Partially resolved**; not maintained | `素直.md:20`. |
| Comprehensibility C7: 系統 «родословная линия» (medium) | Declined; decline **accepted** | Exact segment of guarded 機関; 出身, 原産, 産地 stems. |
| Comprehensibility C8: 系統:41 study-list sentence (low) | **Resolved** | `系統.md:41` deleted. |
| Comprehensibility C9: 算数:18 «по математике» (medium) | Declined; decline **accepted** | EN has the same pairing. |
| Comprehensibility C10: 作者:38 does not parse (medium) | **Resolved** (reworded remedy) | `作者.md:38–39`. |
| Comprehensibility C11: 紺:19 «форма» (medium) | **Resolved** | `紺.md:19`. |
| Comprehensibility C12: 紫:21 genus and Latin name (medium) | **Resolved** (without the dye parenthetical) | `紫.md:21`; Plantarium item 23077. |
| Comprehensibility C13: 純情:19 «не смейтесь» (medium) | **Resolved** | `純情.md:19`. |
| Comprehensibility C14: 純粋:19 «искреннего» (medium) | **Resolved** | `純粋.md:19`. |
| Comprehensibility C15: 純粋 title leads with «чистый» (medium) | **Resolved** | `純粋.md:4,12`; the «чистый» pairs with きれい, 清い and 清潔 are guarded. |
| Comprehensibility C16: 書留 «письменная отметка» (medium) | Partially resolved by fix 1 (guard); maintained at low; **resolved** by fix 4 | `書留.md:4,9,12,21`; JMdict 1589960 sense 2. |
| Comprehensibility C17: そのうえ «сверх» shared with 余計 (medium) | **Resolved** by the guard; title change not maintained | `そのうえ.md:9`. |
| Comprehensibility C18: そのうえ:42 上 left plain (low) | **Resolved** | `そのうえ.md:42`; reviewed RU-only link. |
| Comprehensibility C19: 筆記 «конспектирование» (low) | Declined; decline **accepted** | «ведение записей» would suggest record-keeping. |
| Comprehensibility optionals | **Optional**; no change, non-blocking | As listed in review 001. |

Cross-batch note: links to absent targets stay plain. Eleven EN link occurrences in this batch's new cards, to seven
targets, are absent from RU: words 掃く and ブラシ (from 箒), and kanji 純 (from 純粋 and 純情), 滴 (from 水滴), 粒 (from 粒),
算 (from 算盤 and 算数) and 筆 (from 執筆, 筆記 and 筆者); 作者's EN link to the occupation-and-role-endings article is an
unlinked mention because RU has no such article. The other written kanji without an RU kanji card, 執, 盤, 第, 箒, 粋, 糊,
系, 素, 紫, 紺, 絞 and 統, have none in EN either. There is one reviewed RU-only link, そのうえ:42 → 上 (added by fix 1). No
link was held from an earlier batch, and none is held for a later one. The consistency recheck noted that the b247–b251
lane drafts of 純粋 and 純情 "still carry the pre-fix titles. The next sync must bring the new 純粋 title with it."

## Final exclusion set

All 174 EN exclusion entries (25 lists; EN has none on 経度, 紫, 素人, 水滴 or 箒) are retained in EN order; 9 of them lie
inside the batch, and the other 165 target existing RU cards. Ten direct, one-sided entries are added on nine new cards,
all appended at the end of their lists. Three were present at the candidate and seven were added by fix 1; fix 1 also
added 書留→チェック, which fix 4 removed.

- Candidate (3), accepted by the coordinator without classification: 性質→性能 (性能 «рабочие характеристики; технические
  возможности»), 書留→速達 (速達 «срочная доставка (почты); срочное почтовое отправление») and 作者→著者 (著者 «автор (книги,
  труда)»).
- Fix 1 (7): 組み立てる→集める and 拾う (集める «собирать; коллекционировать», 拾う «подбирать; собирать»; consistency F1),
  素直→おとなしい (おとなしい «тихий; смирный; послушный»; F2), 終点→停留所 (停留所 «остановка (автобуса, трамвая)»; F3),
  等分→区分 (区分 «деление; классификация»; F4), 気配→機嫌 (機嫌 «расположение духа; настроение»; F5) and そのうえ→余計 (余計
  «сверх необходимого; ненужный; ещё больше»; comprehensibility C17), each judged resolved or sound at the consistency
  recheck.
- Added by fix 1 and removed by fix 4: 書留→チェック (チェック «проверка; отметка»), whose only basis was the stem «отмет»
  that fix 4 dropped from 書留's title.

The consistency reviewer classed 作者→著者 as "justified", 性質→性能 as "conservative. The basis is weak (nature vs
performance) but harmless." and 書留→速達 as "conservative, bordering on unjustified … Harmless; keep or drop at the
author's discretion."; it raised F1 as required and F2 to F5 as conservative. 書留–記録 shares the stem «запис» and is
guarded by 書留's EN entry 記録; 書留–筆記 is guarded in both directions by 筆記's EN entry 書留. 筆者~私 and 第一~主要 stay
unguarded, as in EN. Every RU addition is appended at the end of its list, and no EN entry is removed or reordered.
Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fixes 1 and 2 (the そのうえ root claim removed and R1 resolved) and fix 3 (素質:50).
- Scoped coverage: **CLEAN** throughout in all three reviews.
- Comprehensibility: **CLEAN** after fixes 1 to 4 (性質, 素人, 算盤, 素質, 素直, 系統, 作者, 紺, 紫, 純情, 純粋, 書留 and
  そのうえ); the partial and declined dispositions (C3, C6, C7, C9, C19) stand as accepted, and C16 is resolved by fix 4.
- Cross-file consistency: **CLEAN** throughout; the four restored navigation links in four files and the reviewed RU-only
  そのうえ→上 link stand.
- Quiz safety: **CLEAN** after fix 1 (F1 to F5 and そのうえ→余計) and fix 4 (書留 retitled, チェック removed), including the
  two retitles. This covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

## Limits

- The rechecks reread the changed cards or passages and the lines needed to judge them; the unchanged cards rest on review
  001, in which all three reviewers read all 30 cards in full against EN.
- The correctness reviewer reused prior botanical evidence after a refresh returned 504 and did not audit the APK or the
  automatic quiz pools. The consistency reviewer did not independently recompute manifest hashes, abandoned a scripted
  whole-tree pass that hung, did not rerun `tools/validate.py` at `85a96a2`, and screened the later lanes by title grep
  only. The comprehensibility reviewer did not run the validator or the title screen, and the quiz-hint source behind the
  C3 disposition was not in its checkout. Necessity classes are judgements, not measurements.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fixes, so its payload hashes describe the candidate `c215974`, not `85a96a2`.
- Frequency and preferred register (for example «покладистый», «простоватый», «настроение рынка», «умеет
  прислушиваться», «письменная запись» and «воробейник краснокорневой») were not certified. Online dictionaries were
  current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
