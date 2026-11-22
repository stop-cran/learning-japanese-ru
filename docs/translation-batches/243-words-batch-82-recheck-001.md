# Batch 243 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `73cef33b421a2937376b84f06ad0c9908bc93346` | `0dc620083dfbf22c3f2b5550ecb4b76d3ebcbe2e` | Initial review snapshot: the signed candidate, on `origin/full-ru-243-words-82`. |
| `6aa1bca90f5fbdbf7b03e90711e2f25a65472d9a` | `24724a91232245c46ae399ecf876a7c4309a875e` | Fix 1 (final candidate). It covers correctness C01 to C06, consistency F1 and F2 (with the optional 作成 guard) and comprehensibility C1, C2 and C4 to C10 (C8 and C9 as duplicates of correctness C02 and C01; correctness C01, C03 and C06 and comprehensibility C1 and C5 in reworded form). It retitles のろい, 絨毯, 美容, 緩い, 編集 and くれぐれも, adds three exclusions and two reviewed RU-only links, and removes no exclusion or link. Signed; on `origin/full-ru-243-words-82`. |

The fix regenerated `manifest.json`; both snapshots record 5,409 entries (5,404 `files` + 3 images + 2 scenes).
`contentVersion` is `1cd2bb5be75b134a` at the candidate and `c33e46e8ce6a3a3b` after fix 1. The intake was not
refreshed; it still records the candidate's payload hashes. The commit message reads "Batch 243: apply review fixes /
Correctness C01-C06, consistency F1-F2 and comprehensibility C1, C2, C4-C10 (C3 declined; see dispositions)", followed
by one line per change.

Fix 1:
- `編物` (line 20; correctness C01 reworded, comprehensibility C9): «— За неделю я закончил своё вязание.» instead of «— Я
  неделю довязывал своё вязанье.»
- `絵の具` (line 20; correctness C02, comprehensibility C8): «— Я использовал немного красной краски.» instead of «— Я взял
  немного красной краски.»
- `緩い` (lines 4, 12, 16–17, 41, 50–51 and 56; correctness C03 and C06, both reworded): title and H1 «нетугой, слабо
  затянутый; нестрогий; некрутой (о склоне)» instead of «слабо затянутый; нестрогий; некрутой (о склоне)»; the opening
  says «затянуто не туго, сидит свободно (например, обувь или одежда) или устроено не строго»; the 緩める comparison lists
  «нетугой», «свободно сидящий» или «нестрогий»; «Отдельное слово ぬるい в значениях «нестрогий» и «медлительный» тоже можно
  записать как 緩い; его значение «тепловатый» к ゆるい не относится.» instead of «Отдельное слово ぬるい «тепловатый» тоже
  можно записать как 緩い, но это не значит, что ゆるい означает «тепловатый».»; the usage line adds «написание 緩い для ぬるい —
  только во втором значении: [Digital Daijisen, ぬるい](https://www.weblio.jp/content/ぬるい).» «Свободный» stays out of the
  title because 暇's title uses it without a guard.
- `編集` (lines 4, 9 and 12; correctness C04, consistency F2 and its optional): title and H1 «редактирование; составление
  сборника; монтаж (фильма, видео)» instead of «редактирование; монтаж (фильма, видео)»; `quiz_exclusions: [編む, 修正,
  作成]` instead of `[編む]`.
- `くれぐれも` (lines 4 and 12; correctness C05): title and H1 «настоятельно; снова и снова» instead of «настоятельно;
  убедительно (о просьбе)».
- `繋がり` (line 9; consistency F1): 交際 appended to `quiz_exclusions`.
- `のろい` (lines 4, 12, 20–21 and 36; comprehensibility C1, example 2 reworded): title and H1 «вялый; туго соображающий»
  instead of «неповоротливый; туго соображающий»; «— Эта машина движется вяло.» and «— У него замедленная реакция.» instead
  of «— Эта машина неповоротлива.» and «— Он медленно реагирует.»; the 遅い contrast reads «вялость, а не просто позднее
  прибытие» without «неповоротливость».
- `傾く` (lines 43–44; comprehensibility C2): «В примере с компанией речь об упадке дел, а не об отказе: отказ передаёт
  [断る](断る.md)（ことわる）.» instead of ««Клониться к упадку» в примере с компанией значит «слабеть», а не «отклонять»
  приглашение: отказ передаёт [断る](断る.md)（ことわる）.»; the following «Не думайте…» sentence stays.
- `絨毯` (lines 4 and 11; comprehensibility C4): title and H1 «ковёр; коврик» instead of «ковёр; ковровая дорожка»; the
  runner stays in the body.
- `美容` (lines 4, 12 and 41–42; comprehensibility C5, landscape sentence reworded): title and H1 «уход за внешностью;
  наведение красоты» instead of «уход за внешностью; косметические процедуры»; «美容 не ограничивается красотой фигуры. И не
  всякий красивый пейзаж становится предметом косметических процедур.» becomes «Красивый пейзаж сам по себе не относится к
  美容.»
- `線路` (line 20; comprehensibility C6): «— Я живу рядом с железнодорожными путями.» instead of «— Я живу рядом с железной
  дорогой.»
- `なだらか` (lines 42–43; comprehensibility C7): «Не считайте, что каждый なだらかな путь безопасен или не требует усилий.»
  instead of «Не превращайте «лёгкий» из словарного толкования в утверждение, что каждый なだらかな путь безопасен или не
  требует усилий.»
- `繋がる` (line 40) and `繋ぐ` (line 35; comprehensibility C10): the plain 切れる and 繋がる become the reviewed RU-only links
  «[切れる](切れる.md)（きれる）, «обрываться, прерываться», противопоставляется установленной связи:» and «[繋がる](繋がる.md)
  （つながる）— непереходный глагол:». 繋ぐ is a navigation-only file: its EN-position 接続 link and the rest of line 35 are
  unchanged, and navigation totals become 10 files / 13 links (12 EN-position restorations and 1 reviewed RU-only link).
  No other navigation file changed after the candidate.

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Correctness C01, C03 and C06 were accepted with reworded remedies; the reviewer accepted each wording at recheck and
  maintained no disagreement (C03: «Нетугой» "is compatible with that meaning", Kuznetsov тугой sense 3; C06: "Daijisen
  ぬるい sense 2 covers both leniency and slow movement; I accept both glosses").
- The correctness optionals on 美容's figure warning and 傾く's contrast were fixed under comprehensibility C5 and C2;
  absent-kanji references stay plain text (repository convention) and reading terminology is unchanged. At recheck the
  reviewer judged the cautions resolved and the other two "remain optional, not blocking defects".
- Consistency's optional 下降→下げる guard was declined (noun «снижение; понижение» vs verb «опускать; снижать»; "a
  different part of speech in the quiz answer is not a defensible second answer, and EN does not pair them"), and its
  optional removal of 総理大臣→政府 was declined ("Harmless and conservative; «правительство» sits inside «глава
  правительства»"); the reviewer withdrew both at recheck.
- Comprehensibility C1 was accepted with example 2 reworded («У него замедленная реакция.» instead of the proposed
  «Реакция у него вялая.»), and C5 with the landscape sentence reworded; the reviewer did not maintain either point.
- Comprehensibility C3 (繋がり «связи» vs パイプ) was declined: "パイプ, 関係 and 付き合い are all in 繋がり's exclusions, so
  the quiz is guarded"; «узы» "is bookish and stronger than EN's neutral "relationship"". The recheck maintained it (see
  below), and it was withdrawn after a narrow follow-up; no second fix was made.
- The comprehensibility optionals (縫う «покрепче», 繋がり «нашего района», 絨毯 «Мы постелили», ぞくぞく:26's gloss of 続々
  «один за другим», 始終:45 «устаревшими») needed no change; ぞくぞく:26 is a navigation gloss and stays.

Post-fix screen: a saved rerun at `6aa1bca` against the RU primary over the seven words whose title or exclusions changed
(のろい, 絨毯, 美容, 緩い, 編集, くれぐれも and 繋がり; `b243-postfix-screen.txt`, 48 lines) finds two exact-segment hits,
both guarded: くれぐれも–再三 «снова и снова» and 繋がり–パイプ «связи». It also lists 7 further guarded stem leads (編集–作成
and 編む; くれぐれも–しきりに, 繰り返す and 要求; 繋がり–付き合い and 仲) and 39 unguarded stem-only leads. The consistency
recheck's whole-segment screen of the six retitled cards found only the guarded くれぐれも–再三 segment.

The new くれぐれも segment «снова и снова» equals 再三's first segment. 再三's EN `quiz_exclusions` contains くれぐれも, and a
declared pair "is excluded in both directions even if only one article declares it" (EN `docs/content-format.md`, lines
162–163), so the pair is guarded in both directions; no exclusion was added for it. The consistency recheck called it
"already guarded (pre-existing exclusion)"; the comprehensibility recheck's checked-not-filed note called "the missing
reverse exclusion a quiz note outside this facet".

Net change from the candidate:
- titles and H1s of のろい, 絨毯, 美容, 緩い, 編集 and くれぐれも;
- example translations in 編物, 絵の具, のろい (two) and 線路;
- prose in 緩い (opening, the 緩める comparison, the ぬるい passage and the usage line), のろい (the 遅い contrast), 傾く,
  美容 and なだらか;
- three exclusions added (繋がり→交際, 編集→修正 and 編集→作成), none removed;
- two reviewed RU-only links added (繋がる:40 → 切れる and 繋ぐ:35 → 繋がる); no link removed or retargeted.

No Japanese example sentence, sourced reading, kanji card or EN exclusion changed. The content diff
`73cef33..6aa1bca -- kanji words` is 14 word files, 35 lines added and 35 removed; with `manifest.json` the fix changes
15 files, 50 lines added and 50 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the initial reports state "Model identifier not independently verifiable.", "Model: not verifiable by me." and
"Model: not verifiable.", and the comprehensibility recheck repeats "Model not verifiable."

The rechecks ran serially, one reviewer at a time, in one round: correctness, then consistency, then comprehensibility,
each on the full diff `73cef33..6aa1bca` (14 word cards, of which words/繋ぐ.md is a navigation-only file, and
`manifest.json`). The comprehensibility reviewer then received one narrow follow-up on the same snapshot about its
maintained C3 only (brief `b243-recheck2-msg-comprehensibility.txt`). The briefs sent were one recheck brief per reviewer
and that follow-up. This ordering rests on the coordinator's session records; the recheck sections do not record times.

Each reviewer appended its recheck to its own report file under `## Recheck (6aa1bca)`; the comprehensibility reviewer
appended its follow-up answer under `### Recheck addendum (C3)`.

No recheck ran a generator. The correctness reviewer records "validator 0 errors; diff --check clean. No generator run.";
the consistency reviewer ran `tools/validate.py` (0 errors) with Python `-B` ("tools/__pycache__ not created"), found
that the "Committed manifest.json equals an in-memory `build_manifest(Path('.'))` regeneration (True)" and records "No
generator was run (build_manifest was called only as an in-memory function; nothing written)"; the comprehensibility
reviewer records "No generator was run." and "did not re-run validate or the title screen". The correctness section
records the snapshot `6aa1bca90f5fbdbf7b03e90711e2f25a65472d9a` with "HEAD verified, index/worktree clean"; the
consistency section records HEAD `6aa1bca90f5fbdbf7b03e90711e2f25a65472d9a` and a "working tree clean before and after";
the comprehensibility section records HEAD `6aa1bca90f5fbdbf7b03e90711e2f25a65472d9a`, parent `73cef33` and an empty
`git status --porcelain`. The recheck records include no separate coordinator status check after the rechecks; when
these records were drafted, a read-only check showed the RU checkout on `full-ru-243-words-82` at HEAD
`6aa1bca90f5fbdbf7b03e90711e2f25a65472d9a` with `git status --porcelain --ignored` printing nothing.

### Round 1 (`6aa1bca`)

| Facet | Scope and result |
|---|---|
| Correctness | Snapshot `6aa1bca`, "HEAD verified, index/worktree clean". "Read the entire supplied recheck/dispositions and all 14 changed cards in full". "C01 RESOLVED. 編物:20 now explicitly reports completion." "C02 RESOLVED. 絵の具:20 now says the paint was used." "C03 RESOLVED. … «Нетугой» is compatible with that meaning, not merely deficient fastening: Kuznetsov's тугой sense 3 means tightly fitting." "C04 RESOLVED. 編集 title/H1 restore compilation; added exclusions do not remove teaching content." "C05 RESOLVED. くれぐれも title/H1 restore repetition, with context qualifications retained." "C06 RESOLVED. 緩い:50–57 restricts the alternative spelling to non-temperature senses and cites the correct source." "Regressions: none established." (のろい: JMdict 2838553 and Kuznetsov вялый sense 2; 美容: JMdict 1486670; 絨毯, 線路, 傾く/なだらか and the new substantive links "retain their teaching points"; "Stable metadata and Japanese example/readings verified across all 14; new link/exclusion targets exist.") Optional: "美容/傾く cautions resolved; absent-kanji references and reading-term introductions remain optional". Correctness **CLEAN**; scoped coverage **CLEAN**; "Six findings resolved; zero new or outstanding actionable findings." Limits: "Earlier unverified search-only 絨氈, railway wording and terminology limits remain; unchanged claims and automatic quiz uniqueness are not newly certified." |
| Consistency | HEAD `6aa1bca`, tree clean before and after. F1 and F2 **resolved**, with "the optional 作成 guard … also **resolved**"; the optionals 下降 vs 下げる and 総理大臣→政府 "declined; **withdrawn**". "Optional RU-only links 編む→編集, 編物→縫う: remain acceptable. New 繋がる→切れる and 繋ぐ→繋がる: acceptable, both at substantive contrasts, targets exist, form `[word](word.md)（reading）`." "totals 10 files / 13 links are consistent." Whole-segment screen of the six changed titles: "the only shared segment is くれぐれも «снова и снова» = 再三, already guarded (pre-existing exclusion). No unguarded overlap." 15 changed files: "no BOM, no CR", H1 equal to the title, "all relative .md links resolve, `git diff --check` clean"; `validate.py` 0 errors; in-memory manifest equal; "Body-only edits … touch no front matter or links beyond those listed." Consistency **CLEAN**; quiz safety **CLEAN** ("0 open findings"); cross-file integration / nav **CLEAN**. Limits: "linguistic accuracy of the new Russian wording and the ぬるい/緩い Daijisen claim were not independently verified; title screen is whole-segment, not semantic beyond my manual reading." |
| Comprehensibility | HEAD `6aa1bca`, parent `73cef33`, porcelain empty; "Read the full content diff and the changed passages in the tree." C1 (not maintaining the example-2 point: «У него замедленная реакция.» "is natural for 彼は反応がのろいです and is not 遅い's «медленно» or «медленный»"), C2, C4, C5 ("I do not maintain a disagreement"), C6, C7, C8, C9 ("I do not maintain a disagreement") and C10 ("Both links are present") **resolved**. "C3 unresolved; medium; comprehensibility; words/繋がり.md:4. I maintain the point." "I withdraw «узы»"; proposed remedy: title and H1 «взаимосвязь; взаимоотношения». "Optional notes stay optional and are not escalated." Checked, not filed: "くれぐれも «снова и снова» copies 再三's lead segment, but EN titles share "repeatedly" and the full titles stay distinct; the missing reverse exclusion is a quiz note outside this facet." 編集 «составление сборника» "restores EN compilation"; 緩い «нетугой, слабо затянутый» "plus the clothes sentence covers loose fit without 暇's «свободный»". Comprehensibility **NEEDS FIX** (C3 unresolved); scoped coverage **CLEAN**. Limits: "did not re-run validate or the title screen. Model not verifiable." |

C3 follow-up (same snapshot `6aa1bca`; comprehensibility only). The coordinator kept the decline with new evidence: 仲's
title is «взаимоотношения (между людьми)», so the proposal would create an exact whole-segment duplicate with 仲;
繋がり:34 teaches 仲 as the personal-relationship contrast; 関係, 連絡, 付き合い and 交際 crowd the field and are all guarded.
The reviewer's `### Recheck addendum (C3)` reads: "C3 withdrawn. «взаимосвязь; взаимоотношения» would be 仲's whole
segment «взаимоотношения (между людьми)» and would contradict words/繋がり.md:34, which reserves личные отношения for 仲. No
other everyday gloss of EN "relationship" avoids a whole segment of 関係, 連絡, 付き合い, 交際 or パイプ without overstating
the sense («узы» already withdrawn). The current «связи (с людьми)» is a different whole segment from パイプ's «связи,
канал общения между людьми» and is the ordinary rendering already used in example 1. Quiz safety is unchanged.
Comprehensibility verdict on this snapshot: CLEAN." The reviewer's first recheck verdict was comprehensibility NEEDS FIX
(C3 maintained, medium); its final verdict after the addendum is CLEAN. No second fix was made.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C01: 編物:20 «довязывал» does not report completion (medium) | **Resolved** (reworded remedy) | `編物.md:20`; Digital Daijisen 仕上げる sense 1. |
| Correctness C02: 絵の具:20 «взял» instead of "used" (medium) | **Resolved** | `絵の具.md:20`; Digital Daijisen 使う sense 2. |
| Correctness C03: 緩い omits the loose-fit sense (medium; scoped coverage) | **Resolved** (reworded remedy) | `緩い.md:4,12,16–17,41`; Digital Daijisen ゆるい sense 1; Kuznetsov тугой sense 3. |
| Correctness C04: 編集 drops "compilation" (medium; scoped coverage) | **Resolved** | `編集.md:4,12`; JMdict 1603240 sense 1. |
| Correctness C05: くれぐれも drops "repeatedly" (medium; scoped coverage) | **Resolved** | `くれぐれも.md:4,12`; JMdict 1269140 sense 2. |
| Correctness C06: 緩い:50–51 attaches the 緩い spelling of ぬるい to «тепловатый» (medium) | **Resolved** (reworded remedy) | `緩い.md:50–51,56`; JMdict 1183300; Digital Daijisen ぬるい sense 2. |
| Correctness optionals: 美容 figure warning, 傾く contrast | **Resolved** under comprehensibility C5 and C2 | `美容.md:41–42`; `傾く.md:43–44`. |
| Correctness optionals: absent-kanji references, reading terminology | **Optional**; unchanged | Repository convention; "remain optional, not blocking defects". |
| Correctness limits: 絨毯's search-only 絨氈, 接続's «стыковка поездов», «онные чтения» | **UNVERIFIED**; not defects, unchanged | No contrary evidence found; JMdictDB required authentication. |
| Consistency F1: 繋がり lacks 交際 (low) | **Resolved** | `繋がり.md:9`. |
| Consistency F2: 編集 lacks 修正 (low), with the optional 作成 | **Resolved** | `編集.md:9`. |
| Consistency classification of the RU-added exclusions | **Recorded**; all nine kept | See the final exclusion set. |
| Consistency optional: 下降→下げる | **Withdrawn** at recheck | Noun vs verb; EN does not pair them. |
| Consistency optional: remove 総理大臣→政府 | **Withdrawn** at recheck | Harmless conservative guard. |
| Consistency optional: RU-only links 編む→編集, 編物→縫う | **No action**; acceptable at recheck | Substantive comparisons; targets exist. |
| Comprehensibility C1: のろい title and examples (medium) | **Resolved** (example 2 reworded) | `のろい.md:4,12,20–21,36`. |
| Comprehensibility C2: 傾く:43 English-only contrast (medium) | **Resolved** | `傾く.md:43–44`. |
| Comprehensibility C3: 繋がり «связи» vs パイプ (medium) | Declined; maintained at recheck; **withdrawn** after the follow-up | Guarded by パイプ, 関係 and 付き合い; the proposal duplicates 仲's whole segment; `繋がり.md:34`. |
| Comprehensibility C4: 絨毯 «ковровая дорожка» (medium) | **Resolved** | `絨毯.md:4,11`. |
| Comprehensibility C5: 美容 title and figure warning (medium) | **Resolved** (landscape sentence reworded) | `美容.md:4,12,41–42`. |
| Comprehensibility C6: 線路:20 uses 鉄道's title (low) | **Resolved** | `線路.md:20`. |
| Comprehensibility C7: なだらか:42 rejects an unshown gloss (low) | **Resolved** | `なだらか.md:42–43`. |
| Comprehensibility C8, C9: duplicates of correctness C02 and C01 (low) | **Resolved** | As correctness C02 and C01. |
| Comprehensibility C10: 切れる and 繋がる left plain (low) | **Resolved** | `繋がる.md:40`; `繋ぐ.md:35`. |
| Comprehensibility optionals | **Optional**; no change, non-blocking | As listed above. |

Cross-batch note: links to absent targets stay plain. Sixteen EN link occurrences in this batch's new cards, to 14
targets, are absent from RU: words 毛皮, 火口, 片寄る and 社説, and kanji 群, 毛, 缶, 詰, 接, 鈍, 編, 線, 総 and 臣. The other
written kanji without an RU kanji card, 斜, 毯, 絨, 統, 緩, 緯, 縛, 縫, 繋 and 羊, have none in EN either. There are four
reviewed RU-only links to existing cards, all at substantive comparisons where EN has plain text: 編む:34 → 編集 and
編物:34 → 縫う (present at the candidate, accepted by the coordinator under the B214 rule) and 繋がる:40 → 切れる and
繋ぐ:35 → 繋がる (added by fix 1). No link was held from an earlier batch, and none is held for a later one. The
coordinator's adjudication records that no B243 card links to a Batch 241 or Batch 242 word, and the title screen was
rerun on the published Batch 242 tree before the candidate commit.

## Final exclusion set

All 169 EN exclusion entries (28 lists; EN has none on 緯度 or 絨毯) are retained in EN order; 15 of them lie inside the
batch, and the other 154 target existing RU cards. Twelve direct, one-sided entries are added on nine new cards, all
appended at the end of their lists. Nine were present at the candidate (from the authoring lane as adjudicated by the
coordinator) and three were added by fix 1; no fix removed one.

- Candidate (9), all classed conservative by the coordinator: 群れ→混雑 (混雑 «давка; скопление людей»), 缶詰→滞在 (滞在
  «временное пребывание»), 繋がり→パイプ and 付き合い (パイプ «труба; трубка; связи, канал общения между людьми», 付き合い
  «общение; отношения с людьми»), 編物→製品 (製品 «изделие; продукция»), 総理大臣→政府 (政府 «правительство»),
  くれぐれも→要求 (要求 «требование; настойчивая просьба»), 始終→飽くまで (飽くまで «упорно, до конца; сугубо») and 絶えず→継続
  (継続 «продолжение (дела, состояния); непрерывность»).
- Fix 1 (3): 繋がり→交際 (交際 «социальные контакты; романтические отношения»; consistency F1), 編集→修正 (修正
  «исправление; правка»; F2) and 編集→作成 (作成 «составление (документа, плана); создание (файла, учётной записи)»; the
  consistency optional, needed once 編集 gained «составление сборника»), each judged resolved at the consistency recheck.

The consistency reviewer classed 群れ→混雑 and 繋がり→付き合い as required by parity, 繋がり→パイプ as required,
くれぐれも→要求 as "REQUIRED/CONSERVATIVE (real title overlap)", 缶詰→滞在, 編物→製品, 始終→飽くまで and 絶えず→継続 as
conservative, and 総理大臣→政府 as "UNJUSTIFIED (harmless, over-restrictive; no fix required; optional removal)"; the
coordinator kept it, and the reviewer withdrew the optional removal at recheck. くれぐれも–再三 shares the whole segment
«снова и снова» and is guarded in both directions by 再三's EN entry くれぐれも. 再三~また «снова и снова» / «снова; также»
and 総理大臣~大臣 stay unguarded, as in EN. Every RU addition is appended at the end of its list, and no EN entry is
removed or reordered. Android applies each declaration symmetrically, so no reverse declarations were added to baseline
cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (編物 C01, 絵の具 C02, 緩い C06); the 絨氈, «стыковка поездов» and «онные чтения»
  points remain UNVERIFIED and are not asserted defects.
- Scoped coverage: **CLEAN** after fix 1 (緩い C03, 編集 C04, くれぐれも C05); CLEAN throughout in the comprehensibility
  review.
- Comprehensibility: **CLEAN** after fix 1 and the C3 follow-up (のろい, 傾く, 絨毯, 美容, 線路, なだらか, 絵の具, 編物, and
  the 繋がる/繋ぐ links); the reworded dispositions stand as accepted, and C3 is withdrawn.
- Cross-file consistency: **CLEAN** throughout; the twelve restored navigation links in ten files and the four reviewed
  RU-only links stand.
- Quiz safety: **CLEAN** after fix 1 (繋がり→交際, 編集→修正 and 作成), including the six retitles. This covers the
  reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread the changed cards or passages and the lines needed to judge them; the unchanged cards rest on review
  001, in which all three reviewers read all 30 cards in full against EN.
- The correctness reviewer's search-only 絨氈, railway wording and terminology limits remain; unchanged claims and
  automatic quiz uniqueness were not newly certified. The consistency reviewer did not independently verify the
  linguistic accuracy of the new Russian wording or the ぬるい/緩い Daijisen claim, its initial dictionary evidence was
  from its own knowledge rather than fresh lookups, and its title screen is whole-segment. The comprehensibility reviewer
  did not rerun the validator or the title screen, and found JMdictDB password-gated. Necessity classes are judgements,
  not measurements.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fix, so its payload hashes describe the candidate `73cef33`, not `6aa1bca`.
- Frequency and preferred register (for example «туго соображающий», «вялый», «нетугой», «наведение красоты», «составление
  сборника» and «связи (с людьми)») were not certified. Online dictionaries were current observations, not pinned
  archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
