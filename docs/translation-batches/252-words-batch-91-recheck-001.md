# Batch 252 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `ac62348651051d98995df3cb458c512a93488d4f` | `3265cdbc606c1dda0bb1e974126e789e9c8398dc` | Initial review snapshot: the signed candidate, on `origin/full-ru-252-words-91`. |
| `2a3a0d5e755e970288c9f298f283ca9d45b44ef5` | `1efd15e8d7f65d00aca413f1987c03c558f488e0` | Fix 1 (final candidate). It covers correctness F1 (with modification), consistency F1 and O3 for 為替 (the latter via comprehensibility C2), and comprehensibility C7 (verbatim) and C1, C2, C3, C4 and C5 (with modification); it declines comprehensibility C6 and consistency O1, O2 and O3 for 無地 and 点々, and takes no action on consistency F2, the RU-added guard classification, the correctness reviewer's Russian lexical checks, the pre-existing notes or the comprehensibility optionals. It retitles 停車, 為替 and 一通り, rewrites three sentences (停車:34, 一通り:19's translation and 火傷:31), adds one RU-added exclusion and removes none, adds one RU-only link to an existing card (潰す:39 → 直す), removes or retargets no link and changes no navigation-only file. Signed; on `origin/full-ru-252-words-91`. |

The fix regenerated `manifest.json`; both snapshots record 5,679 entries (5,674 `files` + 3 images + 2 scenes).
`contentVersion` is `42a30cef229b3b48` at the candidate and `38acaadeab809846` after fix 1; the manifest differs only in
`contentVersion` and the five hashes of the changed cards. The consistency recheck gives the same count ("There are
5,674 file entries plus 3 images plus 2 scenes, which is 5,679. This agrees with the dispositions."). The intake was
not refreshed; it still records the candidate's payload hashes. The commit message reads "Batch 252: fix 1 after blind
review", followed by "Address blind correctness, consistency and comprehensibility findings on candidate ac623486:
repair 停車's broken 停止 predicate and use «остановка транспортного средства» (no parking «стоянка»), lead 為替 with
«денежный перевод; валютные операции» and guard 翻訳, soften 一通り's example and drop the title usage note, make 火傷's
no-card remark learner-facing, and link the existing 直す card from 潰す." and the co-author trailer.

Fix 1:
- `停車` (lines 4, 12 and 34; comprehensibility C1 and correctness F1, both with modification): title and H1
  «остановка транспортного средства» instead of «остановка транспорта; стоянка (в пути)»; line 34 «Так говорят и о
  механизме, который вовсе не является транспортным средством.» instead of «停止 может и механизм, который вовсе не
  транспортное средство.» It follows line 33 «[停止](停止.md)（ていси）— более широкая остановка или приостановление:» and
  adapts EN 停車:31 "a machine can 停止 without being a vehicle". «стоянка» no longer occurs anywhere in `words/停車.md`;
  the exclusions are unchanged.
- `為替` (lines 4, 9 and 12; comprehensibility C2, with modification, and consistency F1, verbatim): title and H1
  «денежный перевод; валютные операции» instead of «валютный обмен; денежный перевод»; exclusions `[両替, 交換, 換える,
  替える, 案, 通貨, 翻訳]` instead of `[両替, 交換, 換える, 替える, 案, 通貨]`.
- `一通り` (lines 4, 12 and 19; comprehensibility C4 and C3, both with modification): title and H1 «целиком, но бегло;
  полный набор; обыкновенный» instead of «целиком, но бегло; полный набор; обыкновенный (в отрицании)»; line 19's
  translation «— Я бегло прочитал всю инструкцию.» instead of «— Я прочитал инструкцию от начала до конца.», with the
  Japanese 説明書を一通り読みました。（せつめいしょをひととおりよみました。） unchanged (EN 一通り:20 "I read through the
  instructions.").
- `火傷` (line 31; comprehensibility C5, with modification): «Отдельной карточки для кандзи 傷 пока нет, но этот знак всё
  равно входит в написание 火傷.» instead of «Карточки для кандзи 傷 в коллекции пока нет; он всё равно входит в метаданные
  записанного слова.» It adapts EN 火傷:29 "傷 has no kanji card in the current collection; it still belongs in the
  written word's metadata."
- `潰す` (line 39; comprehensibility C7, verbatim): «[直す](直す.md)（なおす）— «чинить» — или 立て直す（たてなおす）—
  «восстанавливать, поправлять» — могут быть противоположностью в подходящем контексте.» instead of the same line with
  plain 直す. EN 潰す:41 has the plain text "直す (なおす), "repair," or 立て直す (たてなおす), "rebuild; restore," can
  contrast in appropriate contexts."; 立て直す stays plain because it has no RU card.

All five are new Batch 252 cards. No navigation-only file changed, so navigation stays at 9 files / 17 links, all
EN-position restorations. The coordinator's candidate edits stand: fix 1 did not touch 停止 or オイル. Fix 1 did change
two items the coordinator had kept: 停車's title, which contained «стоянка» (kept among the lexis "judged natural, not
dictionary-checked"), and 為替's exclusions, which gained 翻訳.

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Correctness F1 was accepted with modification: "The reviewer's «Остановиться может и механизм…» is grammatical but
  no longer refers to 停止, which the previous line introduces."
- Comprehensibility C1 was accepted with modification: "The reviewer's «краткая остановка (не парковка)» is not used.
  The card body (line 42) says that the word itself does not state how long the stop lasts, and a negated parenthesis
  is not a usable quiz gloss."; «стоянка» is dropped because "Russian traffic rules (ПДД РФ п. 1.2) define «остановка»
  as a halt of up to 5 minutes, or longer for boarding or loading. «стоянка» is longer than that, which is 駐車 and
  駐車場's parking sense."
- Comprehensibility C2 was accepted with modification: "The reviewer's «валютный расчёт» is not used because it is not
  an established Russian term."
- Comprehensibility C3 was accepted with modification: "The reviewer's «в общих чертах прочитал» would lose the "whole
  document" part."
- Comprehensibility C4 was accepted with modification: "«(в отрицании)» is dropped from the title and H1, but the
  first segment keeps its natural order «целиком, но бегло»."
- Comprehensibility C5 was accepted with modification: "Deleting the sentence is declined, consistent with C238-6, C2
  of B239 and B241. EN keeps it, and published RU cards carry the same kind of note, so a corpus-wide decision remains
  a follow-up."
- Comprehensibility C6 (オイル:28 Latin `oil`) was declined: "The «заимствование из английского X» pattern is used on
  dozens of published loanword cards (アイスクリーム, オフィス, カバー, カーブ, キャプテン and others). B223 C1 preserved
  it, and the reviewer rates the impact low."
- Consistency O1 (無沙汰) was declined: "EN's "neglecting to keep in touch" is also a verbal gloss inside a noun title,
  and the body explains the register."
- Consistency O2 (潜る) was declined: "«нырять» also covers jumping into water. That would bring 潜る closer to 飛び込む
  in a learner's memory, even though the guard keeps the quiz safe. The reviewer marks this as optional."
- Consistency O3 was covered by C2 for 為替 and declined for 無地 and 点々: "The 無地 body explains «однотонный», and
  点々's adverb plus plural noun mirrors EN "scattered here and there; dots"."
- Consistency F2 needed no action ("The pairs share a topic but no title segment, and EN has no guards for them."), nor
  did the RU-added guard classification ("Three guards are required and nineteen are conservative. None is
  unjustified, so all 22 stay."), the correctness reviewer's Russian lexical checks ("The reviewer found no
  contradiction on gramota.ru. «стоянка» is removed from 停車's title for a different reason, under C1."), the
  pre-existing notes ("They are outside the batch or inherited from EN, and are recorded for a later pass.") or the
  comprehensibility optionals (for example "災難 «злоключение» is accurate (Kuznetsov).").

Quiz-exclusion changes. Comparing each card's `quiz_exclusions` with frozen EN gives 22 RU-added pairs on 12 cards at
the candidate and 23 on 12 cards at the fix. Fix 1 removed none and added one:
- 為替→翻訳 (翻訳 «перевод»), consistency F1 (Medium, confidence medium); the dispositions: "翻訳's whole title is
  «перевод», and Russian «перевод» also names a money transfer. A 為替 question could therefore show 翻訳 as a second
  defensible answer." and "The title stays «денежный перевод» in its first segment under C2, so the guard is still
  required. 通訳 «устный перевод» and 訳す «переводить (на другой язык)» are qualified as translation and are left
  unguarded."

At recheck the consistency reviewer recorded "F1 (為替 ~ 翻訳 guard): RESOLVED." and "通訳 «устный перевод» and 訳す
«переводить (на другой язык)» may stay unguarded. They are qualified as spoken or linguistic translation, and their
segments are not «перевод» or «денежный перевод». I agree with the disposition."; it also wrote "The EN six come
first, in EN order", but frozen EN 為替 has five exclusions (両替, 交換, 換える, 替える and 案), and 通貨 is RU-added, as its
initial report's classification and the correctness recheck record. The correctness recheck found "EN guards remain the
exact ordered prefix [両替, 交換, 換える, 替える, 案]; existing RU 通貨 follows, then new 翻訳. 翻訳.md exists."; the
comprehensibility recheck: "為替's added 翻訳 guard matches the body's «перевод текста» warning and does not change the
teaching."

Post-fix screen: a saved rerun at the committed `2a3a0d5` over all 30 batch words (`b252-fix-screen.txt`, 312 lines)
has 40 `OK` lines for pairs already guarded by an exclusion and 272 `!!` lines. Its exact-segment lines are the same
four guarded `OK` lines as at the candidate (停止 ~ ストップ, 停止 ~ 停留所, 一通り ~ そっくり and オイル ~ 油), the 一通り
one showing the new title. Against the candidate screen (`b252-cand-screen.txt`, 321 lines: 42 `OK` and 279 `!!`) it
removes 69 lines and adds 60, all from the three retitles and the 翻訳 guard:
- 一通り: ten `!!` lines with the stem «отриц» removed (あんまり, どうしても, なにも, なんとも, 不, 別に, 否定, 滅多に, 短所 and
  論ずる); 8 `!!` and 5 `OK` lines reworded to the new title;
- 停車: six `!!` lines with the stem «средс» added (せっけん, 手段, 暮らし, 薬品, 農薬 and 道具); the `OK` 駐車場 «стоян» line
  removed (the guard stays); 15 `!!` and 6 `OK` lines (ストップ, 停留所, 止まる, 止める, 立ち止まる and 終点) and the `OK`
  停止 ~ 停車 line reworded to the new title;
- 為替: four `!!` «обмен» lines (交流, 取り替える, 議論 and 通信) and the `OK` 交換 and 換える lines removed; two `!!`
  «опера» lines added (作業 and 手術); 為替 ~ 翻訳 changed from `!!` to `OK`; 14 `!!` lines and the `OK` 両替 and 通貨
  lines reworded to the new title.

No pair outside these words changes. The dispositions record the post-fix screen of the changed titles
(`b252-fix-screen-changed.txt`) as "no unguarded exact-segment hit remains. The only exact segment hit is 一通り ~
そっくり «целиком», which is guarded. The stem-only hits are not competing answers", for example "停車 «транс-/средс-» ~
乗り物 «транспортное средство», 車, 交通, 発車 «отправление транспорта» and others. These are vehicle nouns or the
contrasted departure, not a stopping." and "為替 «опера-» ~ 手術 (surgery) and 作業 (work operation)." The consistency
recheck ran its own scripted exact-segment comparison of the three new titles "against all 4,213 RU word titles" and
found no exact-segment collision; it reported that "The post-fix screen paragraph in the dispositions matches my
independent comparison: the exact hit 一通り~そっくり is guarded, and the other overlaps are stem-only and
non-competing."

Net change from the candidate:
- titles and H1s of 停車, 為替 and 一通り;
- prose in 停車 (line 34), 一通り (line 19's translation) and 火傷 (line 31);
- exclusions: 翻訳 appended to 為替; none removed;
- one RU-only link added (潰す:39 → 直す); none removed or retargeted.

No Japanese example sentence, kana reading, kanji card, EN exclusion, non-title front-matter field other than
`quiz_exclusions`, or navigation file changed. None of the three old titles occurs anywhere in RU at the fix. The
content diff `ac62348..2a3a0d5 -- words` is 5 word files, 11 lines added and 11 removed; with `manifest.json`, 17 lines
added and 17 removed.

Fix 1 validation, as recorded in the dispositions: "`tools/validate.py`: 0 errors."; "Manifest rebuilt: 5,679 files,
version 38acaadeab809846."; "124 unit tests OK; content budget OK (exit 0); `git diff --check` clean." For this record
link parity was verified again over the 39 batch paths at `2a3a0d5`: "checked 39", no LOST link and EXTRA only the
three reviewed RU-only links words/地味 → words/派手, words/断水 → words/停電 and words/潰す → words/直す; the fix diff adds
exactly the 潰す → 直す link and removes or retargets none.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the correctness recheck says "Model identifier not independently verifiable.", the consistency recheck "Model not
verifiable." and the comprehensibility recheck "Model: not verifiable from this session." The dispositions label each
reviewer's model "per runtime status".

The rechecks ran serially, one reviewer at a time, in one round: comprehensibility, then correctness, then
consistency, each on the fix diff `ac62348..2a3a0d5` (5 word files and `manifest.json`). The initial reviews had run
correctness, then consistency, then comprehensibility. The recheck report files' write times are 16:27, 16:32 and 16:34
local time on 2026-11-23; the orderings otherwise rest on the coordinator's session records. There was no second fix
and no follow-up exchange.

Rechecks were returned as separate reports rather than appended to the initial review files: the full texts are in
`b252-recheck-correctness.md`, `b252-recheck-consistency.md` and `b252-recheck-comprehensibility.md` in the
coordinator's session folder, and their content is recorded in the round table below. The coordinator's record of how
the briefs were delivered: "The three recheck briefs are saved as
b252-recheck-msg-{comprehensibility,correctness,consistency}.txt, and each reviewer received only a pointer message
asking it to read its brief in full. The comprehensibility brief was saved at 15:24:30 UTC and pointed to at 15:24:47;
the consistency brief was saved at 15:25:32 and pointed to at 15:33:12, after the correctness recheck report
(15:32:13). The correctness brief was edited in the same parallel tool batch that sent its pointer (send started
15:28:55; file written 15:28:59): the edit only shortened the Task line to "Task: reconcile F1 as", removing the
parenthetical "(and, if you now disagree with it, your earlier acceptance of «стоянка (в пути)»)"; the saved file is
the edited text, which still asks whether dropping «стоянка (в пути)» is right, and the coordinator's records do not
establish whether the reviewer read the file before or after that edit." Each brief gave the reviewer its own original
report, the coordinator's dispositions for all three facets (not the other reviewers' reports) and the fix diff, and
repeated the read-only and no-generator rules ("do not run tools/build_manifest.py or any other generator
(tools/validate.py is allowed; remove any" Python bytecode cache "it leaves)", paraphrased here only in naming the
cache directory); the consistency brief added "including with --help" after "any other generator", following that
reviewer's accidental `--help` run of the generator during review 001 (see the independent review record).

No recheck reported running a generator. The correctness recheck records "Allowed read-only validation with python -X
utf8 -B tools/validate.py returned 0 error(s); no" bytecode cache "exists. No generator or repository write was
performed; original report preserved."; the consistency recheck records "`tools/validate.py` reports 0 errors.", that
no bytecode cache is left, and "I ran no generator."; the comprehensibility recheck records "Did not rerun the title
screen or validate.py", "No repo file written." and that no bytecode cache was created, and makes no statement about
generators. The correctness recheck records HEAD `2a3a0d5e755e970288c9f298f283ca9d45b44ef5` with parent
`ac62348651051d98995df3cb458c512a93488d4f`, "Primary RU checkout verified clean at start and immediately before
writing: git status --porcelain empty; index SHA-256 unchanged during recheck"; the consistency recheck records the
same HEAD with "`git status --porcelain` was empty at the start and at write."; the comprehensibility recheck records
the same HEAD and parent with "`git status --porcelain` empty at start and at write. Original report not rewritten."
The RU primary checkout was at HEAD `2a3a0d5e755e970288c9f298f283ca9d45b44ef5` and clean when these records were drafted.

### Round 1 (`2a3a0d5`)

| Facet | Scope and result |
|---|---|
| Comprehensibility | `2a3a0d5`, parent `ac62348`, porcelain empty at start and at write. "Scope: recheck of C1–C7 and the optional notes against dispositions and fix 1. Read in full on HEAD: words/停車.md, words/為替.md, words/一通り.md, words/火傷.md, words/潰す.md." Titles checked: 停留所, 駐車, 駐車場, 両替 and 直す; "オイル.md:28 reread (unchanged)." C1–C5 and C7 **resolved**, for example C1 "Declining «краткая остановка (не парковка)» is right: line 42 says the word does not state duration, and a negated parenthesis is not a quiz gloss."; C2 "«валютный расчёт» is not an established term; the modification is better."; C3 "«в общих чертах» would have dropped the whole-document part."; C4 "Bare «обыкновенный» is a gloss, not a rule."; C5 "Rewording instead of deletion is reasonable once the metadata wording is gone"; C7 "The link target exists." "C6 withdrawn. Latin `oil` remains at オイル.md:28. The decline is reasonable: impact was low, and the published «заимствование из английского X» pattern (and B223) is the house style. Not refiled." Each optional note "optional, unchanged". New text: "停車:34 «Так говорят и о механизме…» is grammatical and, after the colon on the 停止 gloss, refers to 停止, not to 停車. No regression." "Findings: none." Verdicts: "Comprehensibility: CLEAN. Scoped coverage: CLEAN. The five edits keep the EN points; no new learner-facing defect." Limits: "Did not reread the 25 unchanged batch cards. Did not rerun the title screen or validate.py; the disposition's post-fix screen was used only as a lead. Other reviewers' reports were not read." |
| Correctness | `2a3a0d5` against `ac62348`, porcelain empty at start and immediately before writing; frozen EN `6af98cb7`. "Read in full words/停車.md, words/為替.md, words/一通り.md, words/火傷.md and words/潰す.md, each against its full supplied frozen EN original (designated 6af98cb7). Read original correctness report, coordinator dispositions and complete word fix diff; also read words/直す.md and inspected manifest diff/change boundary." "F1 RESOLVED — words/停車.md:33–34 now forms a grammatical explanation: “Так говорят” refers to the immediately preceding 停止 and applies it to a non-vehicle mechanism, preserving EN:31." "The coordinator's wording is acceptable; my earlier alternative need not be adopted." HIGH confidence. "Prior “стоянка” lexical check retained, not withdrawn. Removing it from the title is sound disambiguation, not proof that its general-language train-stop sense was false. The cited road-rule distinction is technical, not a duration restriction on Japanese 停車." New text, per card: 停車 "matches EN “vehicle stopping; halt” and JMdict 1434960 sense 1"; 為替 "is an acceptable contextual title for JMdict 1157330 senses 1 (money order/draft) and 2 (exchange, e.g. foreign)"; 一通り "Dropping “(в отрицании)” is safe: sense 3 says “usu. in the negative”, not exclusively negative"; 火傷 "Both source facts remain"; 潰す "Added link resolves to words/直す.md". Evidence: JMdict_e freshly inspected, kotobank 為替 and the ПДД 1.2 text. Checks: "Japanese examples/readings are unchanged from the reviewed candidate, including the Japanese portion of 一通り:19. All five cards' runtime links resolve. Manifest diff changes only contentVersion and these five hashes". "Findings: None new or unresolved within the assigned facets. F1 resolved; no scoped-coverage regression established." Verdicts: "correctness CLEAN; scoped coverage CLEAN on HEAD, within this five-card regression scope plus the prior unchanged review scope." Limits: "CLEAN is bounded, not exhaustive correctness. This pass reread the five changed cards, not the other 25 unchanged cards or every declined observation in other facets."; "Frozen-source commit identity and commit signatures were not independently authenticated."; "full packaging/app quiz behavior was not recertified." |
| Consistency | HEAD `2a3a0d5` (parent `ac62348`), porcelain empty at start and at write; `tools/validate.py` 0 errors. "I read the fix diff (5 cards plus manifest) in full and the dispositions in full. I read the title/H1 lines of 停車, 為替 and 一通り and the 潰す and 火傷 changed lines. I ran my own scripted exact-segment comparison of the 3 new titles against all 4,213 RU word titles. I did not run `word_title_screen.py` or `link_parity.py`." F1 "RESOLVED"; 通訳 and 訳す "may stay unguarded"; F2 "WITHDRAWN as actionable; no change needed. The fix adds no new in-batch pair."; "Guard classification (3 required, 19 conservative, 0 unjustified): unchanged and still valid."; O1 "declined, and I agree"; O2 "declined, and I accept it. The guard covers 飛び込む anyway. OPTIONAL and closed."; "O3 for 為替: RESOLVED by C2."; "O3 for 無地/点々: declined, and I agree; the bodies carry the warnings. OPTIONAL and closed."; pre-existing notes "still OUT OF SCOPE. They are unchanged and not regressions." New text: no exact-segment collision for 停車, 為替 or 一通り; "停車:34 is now grammatical. «стоянка» is gone from the card (grep)."; "«(в отрицании)» and «валютный обмен» are gone from the cards (grep)."; "H1 matches the title in all three title-changed cards (grep)."; "潰す:39 → `直す.md` resolves, because the file exists. It is the third RU-only link in the batch, after 断水→停電 and 地味→派手."; "火傷:31 is rephrased. It still correctly says that no card for 傷 exists."; manifest "only `contentVersion` (42a30cef… → 38acaade…) and the 5 hashes for 一通り, 停車, 潰す, 火傷 and 為替 changed". "Findings: none. No new or unresolved actionable items." Verdicts: "Consistency CLEAN on HEAD. Quiz safety CLEAN on HEAD (no unresolved item)." Limits: "the screen agreement rests on my own script and on spot checks. I split segments on `;` and removed parentheticals, so comma-level matches such as 「целиком」 were judged by hand. Dictionary senses were not independently looked up. I ran no generator." |

No recheck raised a new finding or left an optional note open. There was no second fix.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 停車:34 «停止 может и механизм…» (LOW; correctness) | **Resolved** (with modification) | `停車.md:34`; correctness recheck "The coordinator's wording is acceptable; my earlier alternative need not be adopted."; comprehensibility recheck "refers to 停止, not to 停車"; JMdict 1434920 senses 1–2. |
| Correctness Russian lexical checks (стоянка, крапинка, однотонный, несметный, заурядный, злоключение, мутнеть, творить) | **Accepted**; no action | Correctness recheck "Prior “стоянка” lexical check retained, not withdrawn."; «стоянка» left 停車's title under C1 for a different reason. |
| Consistency F1: missing guard 為替 ~ 翻訳 (Medium) | **Resolved**; guard added | `為替.md:9`; consistency recheck "RESOLVED"; correctness recheck "翻訳.md exists." |
| Consistency F2: unguarded in-batch topic pairs (Low; no action required) | **Withdrawn**; no action | Consistency recheck "WITHDRAWN as actionable; no change needed." |
| Consistency guard classification (3 required, 19 conservative) | **Accepted**; no action | Consistency recheck "unchanged and still valid". |
| Consistency O1: 無沙汰 verb-phrase segment (OPTIONAL) | **Optional**; declined | Consistency recheck "declined, and I agree. The EN gloss is also verbal. It stays OPTIONAL and closed." |
| Consistency O2: 潜る «уходить под воду» (OPTIONAL) | **Optional**; declined | Consistency recheck "declined, and I accept it." |
| Consistency O3: 為替 «валютный обмен» (OPTIONAL) | **Resolved** (via C2) | Consistency recheck "O3 for 為替: RESOLVED by C2." |
| Consistency O3: 無地 «однотонный», 点々 adverb plus noun (OPTIONAL) | **Optional**; declined | Consistency recheck "declined, and I agree; the bodies carry the warnings. OPTIONAL and closed." |
| Consistency pre-existing notes: 火山:23 bracket, 各.md plain 各々/各自, 火傷 tag | **Accepted**; out of scope | Consistency recheck "still OUT OF SCOPE". |
| Comprehensibility C1: 停車 title «…; стоянка (в пути)» (medium) | **Resolved** (with modification) | `停車.md:4,12`; comprehensibility recheck "Declining «краткая остановка (не парковка)» is right"; JMdict 1434960 sense 1 and ПДД 1.2 per the correctness recheck. |
| Comprehensibility C2: 為替 «валютный обмен» (medium) | **Resolved** (with modification) | `為替.md:4,12`; comprehensibility recheck "the modification is better"; JMdict 1157330 senses 1–2. |
| Comprehensibility C3: 一通り:19 «от начала до конца» (medium) | **Resolved** (with modification) | `一通り.md:19`; comprehensibility recheck "keeps both "through" and "not exhaustive"". |
| Comprehensibility C4: 一通り «обыкновенный (в отрицании)» (low) | **Resolved** (with modification) | `一通り.md:4,12`; correctness recheck "sense 3 says “usu. in the negative”, not exclusively negative". |
| Comprehensibility C5: 火傷:31 editorial wording (low) | **Resolved** (with modification) | `火傷.md:31`; comprehensibility recheck "Rewording instead of deletion is reasonable"; correctness recheck "Both source facts remain". |
| Comprehensibility C6: オイル:28 Latin `oil` (low) | **Withdrawn**; decline stands | Comprehensibility recheck "C6 withdrawn." "Not refiled." |
| Comprehensibility C7: 潰す:39 plain 直す (low) | **Resolved**; RU-only link added | `潰す.md:39`; comprehensibility recheck "The link target exists."; JMdict 1599390 sense 1 per the correctness recheck. |
| Comprehensibility optionals: 災難, 潰す:30, 無地:41–42, 点々:41, 炭鉱:39, 為す, long 潰す/潜る titles, 灯台:20 | **Optional**; no change | Comprehensibility recheck "optional, unchanged" for each. |

Cross-batch note: links to absent targets stay plain. Eleven EN link occurrences in this batch's new cards, to 10
targets, are absent from RU: words 淡水 (from 断水), kanji 替 (from 為替), kanji 炭 and 鉱 (from 炭鉱), kanji 灰 (from 灰色),
kanji 灯 and 油 (from 灯油), kanji 灯 (from 灯台), words 乾かす and 湿る (from 濡らす) and kanji 濃 (from 濃度). The
coordinator's adjudication sentence names the same ten targets; the author report's listing of 直す as absent was
wrong, and fix 1 linked it. The 30 EN cards have no article link. The other written kanji without an RU kanji card (傷,
凡, 汰, 沙, 潜, 潰, 濁, 濡, 災, 為 and 無) have no EN kanji card either. No link is lost to an existing target. The new cards
have three reviewed RU-only links (断水:32 → 停電 and 地味:38 → 派手 at the candidate, 潰す:39 → 直す from fix 1); no
navigation file has an RU-only link. No link was held from an earlier batch, and none is held for a later one. The nine
navigation-only files with their 17 restored links (kanji/停.md to 停止, 停車 and 停電; kanji/各.md to 各地; words/下降.md
to 火口; words/派手.md to 地味; words/潰れる.md to 潰す; words/火山.md to 火口; words/無限.md to 無数; words/突く.md to 点く;
words/転々.md to 点々) are unchanged by fix 1. Every exclusion target resolves to a card published at the baseline or to
a batch card. The scratch lane copies of the five fixed cards used for later batches (B253–B262 lanes) still carry the
candidate text; the dispositions record that they "are resynced when the B253 candidate is built". That resync is
outside this batch.

## Final exclusion set

All 143 EN exclusion entries (25 lists; EN has none on 停電, 断水, 炭鉱, 灰色 or 灯台) are retained in EN order; 11 of
them lie inside the batch, and the other 132 target existing RU cards. Twenty-three direct, one-sided entries are added
on twelve new cards; each is appended at the end of its list:

- 停車→停留所, 駐車, 駐車場, 立ち止まる, 終点: `[ストップ, 止まる, 止める, 停留所, 駐車, 駐車場, 立ち止まる, 終点]`;
- 停止→止む, 停留所: `[ストップ, 止まる, 止める, 止す, 中止, 終了, 休業, 立ち止まる, 停車, 停電, 断水, しまう, 上がる, 壊れる,
  落ちる, 止む, 停留所]`;
- 無沙汰→久しぶり, 黙る: `[怠る, 不通, 久しぶり, 黙る]`;
- 地味→謙遜: `[おとなしい, あっさり, 謙虚, 謙遜]`;
- 各地→全国: `[あちこち, 方々, 全国]`;
- 一通り→おおざっぱ, そっくり, 完全, セット: `[ざっと, 大体, およそ, ほぼ, ほとんど, 一応, 一般, 普通, 普段, あたりまえ, 平均,
  たいてい, 全部, 全体, 全て, 全, 方法, おおよそ, チェック, 各地, おおざっぱ, そっくり, 完全, セット]`;
- 平凡→日常: `[普通, 一般, あたりまえ, 一通り, 地味, つまらない, 日常]`;
- 為替→通貨, 翻訳: `[両替, 交換, 換える, 替える, 案, 通貨, 翻訳]`;
- オイル→バター: `[油, 石油, 脂, バター]`;
- 潰す→殺す: `[潰れる, 砕く, 壊す, 崩す, 倒す, 割る, 無駄, ぺちゃんこ, 殺す]`;
- 潜る→水中: `[飛び込む, 沈む, 沈める, 隠れる, 隠す, 覆う, 通る, 避ける, 水中]`;
- 漢和→漢字, 日中: `[辞書, 辞典, 字引, 漢字, 日中]`.

Twenty-two were present at the candidate and accepted by the coordinator with the reasons quoted in the independent
review record (21 drafted guards kept and 停止→停留所 added at adjudication); fix 1 added 為替→翻訳 and removed none, as
described above. None targets a batch word. The consistency reviewer classed 停止→停留所, オイル→バター and 一通り→そっくり as
"Required" and the other nineteen candidate additions as "Conservative (real basis, necessity unestablished; keep)",
with "Unjustified: none."; at recheck the classification is "unchanged and still valid", and the added 為替→翻訳 is the
guard it had asked for under F1. No target card declares the reverse pair. Every RU addition is appended at the end of
its list, and no EN entry is removed or reordered. Android applies each declaration symmetrically (EN
`docs/content-format.md`, lines 162–165), so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (停車 F1); CLEAN at recheck for all five changed cards.
- Scoped coverage: **CLEAN** throughout; no coverage regression was established at recheck.
- Comprehensibility: **CLEAN** after fix 1 (停車, 為替, 一通り, 火傷 and 潰す); the modified dispositions of C1–C5 stand as
  accepted, and the declined C6 stands as withdrawn.
- Cross-file consistency: **CLEAN** after fix 1; the 17 restored navigation links in 9 files and the three reviewed
  RU-only links in new cards stand.
- Quiz safety: **CLEAN** after fix 1 (為替→翻訳); the twenty-three RU additions stand. This covers the reviewed batch and
  the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread the changed cards and the lines needed to judge them; the unchanged cards rest on review 001, in
  which all three reviewers read all 30 cards in full. The correctness recheck "reread the five changed cards, not the
  other 25 unchanged cards or every declined observation in other facets"; the comprehensibility recheck read the five
  changed cards in full and "Did not reread the 25 unchanged batch cards"; and the consistency recheck read the fix diff
  in full and the changed title/H1 and body lines.
- In review 001 the consistency reviewer took the dictionary basis "from the sense IDs cited in the footers" and
  triaged its title screen only in part; at recheck it did not run `word_title_screen.py` or `link_parity.py`, and its
  "EN six" description of 為替's list is inaccurate (EN has five). The comprehensibility recheck did not rerun the title
  screen or validate.py. Link parity at the fix was rerun for this record; the candidate link parity for this record ran
  on a since-deleted temporary export. Necessity classes are judgements, not measurements.
- Which version of the correctness recheck brief the reviewer read (before or after its Task line was shortened) is not
  established by the coordinator's records; both versions ask about dropping «стоянка (в пути)».
- The correctness recheck did not authenticate the frozen-source identity or commit signatures; no full-corpus synonym
  or runtime quiz audit was made.
- The serial order of the reviews and rechecks rests on the coordinator's session records and the report write times.
- The intake was not refreshed by the fix, so its payload hashes describe the candidate `ac62348`, not `2a3a0d5`.
- The C5 corpus-wide decision on no-card remarks is recorded as a follow-up outside this batch.
- Frequency and preferred register (for example «остановка транспортного средства», «валютные операции» and «бегло
  прочитал всю инструкцию») were not certified. Online dictionaries were current observations, not pinned archives.
  The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
