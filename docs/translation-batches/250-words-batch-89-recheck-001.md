# Batch 250 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `4a5e70f1dff84c8e692a1d3c7f9c7c7bd01ce45c` | `bd733755f1232bb0d1e2ece9ccb4a0a15b5eeba6` | Initial review snapshot: the signed candidate, on `origin/full-ru-250-words-89`. |
| `9e339f53811e17e54bcdf70d695fff995fe3415a` | `684da564851c30c1e770c17b32332a5a3ec6ee68` | Fix 1 (final candidate). It covers correctness F01 and F02 (F02 with modification, merged with comprehensibility C2) and comprehensibility C1–C7 (C3 and C4 with modification), plus the comprehensibility optional note on 学部:37; it declines consistency F1 and F5, the consistency optional polish notes and the comprehensibility `kango` optionals, takes no action on F2 and F3, and resolves F4 through C1. It retitles 瓶詰, 生ずる, 独り言, 特定 and 物騒, rewrites prose in 瓶詰, 生ずる, 独り言, 危うい and 献立, deletes one sentence in 学部, restores EN's kana spacing in 怪しい, adds, removes or retargets no exclusion or link and changes no navigation-only file. Signed; on `origin/full-ru-250-words-89`. |

The fix regenerated `manifest.json`; both snapshots record 5,619 entries (5,614 `files` + 3 images + 2 scenes).
`contentVersion` is `bddfd3e4d9e4aa9d` at the candidate and `14b5ac2292329014` after fix 1; the manifest differs only in
`contentVersion` and the nine hashes of the changed cards. The consistency recheck gives the count as "unchanged at
5,623 entries"; the committed manifest has 5,619 entries at both commits, and the reviewer's tally method is not
recorded. The intake was not refreshed; it still records the candidate's payload hashes. The commit message reads
"Batch 250 fix 1: apply blind-review dispositions", followed only by the co-author trailer.

Fix 1:
- `怪しい` (lines 20–21; correctness F01, verbatim): the kana readings become 「あの はなしは すこし あやしいです。」 and
  「かれが くるかどうか あやしいです。」, with EN's internal spaces (EN 怪しい:19–20). Sentences and translations are
  unchanged.
- `瓶詰` (lines 4, 12, 16, 20 and 38; correctness F02 with modification, merged with comprehensibility C2): title and H1
  «фасовка в бутылки и банки; в бутылках или банках»; line 16 «瓶詰 означает фасовку в бутылки или банки…»; line 20
  «Я разложил джем по банкам.»; line 38 «Фасовка может быть частью…». The old title is «розлив по бутылкам и банкам; в
  бутылках или банках».
- `生ずる` (lines 4, 12 and 16; comprehensibility C1, verbatim): title and H1 «возникать; порождать» instead of
  «возникать; порождать; вызывать»; line 16 «生ずる означает порождать что-либо либо возникать, зарождаться.» instead of
  «生ずる означает порождать или вызывать что-либо либо возникать, зарождаться.» Example 1 («В плане иногда возникают
  проблемы.») and example 2 are unchanged.
- `独り言` (lines 4, 12 and 17; comprehensibility C3, with modification): title and H1 «разговор с самим собой» instead of
  «разговор с самим собой; монолог»; line 17 «Так можно назвать и монолог, если это речь, обращённая к самому себе, а не
  к слушателям.» instead of «Слово соответствует также монологу.»
- `特定` (lines 4 and 12; comprehensibility C4, with modification): title and H1 «конкретный; выявление» instead of
  «конкретный; выявление (причины, лица)».
- `物騒` (lines 4 and 12; comprehensibility C5, verbatim): title and H1 «небезопасный; угрожающий» instead of
  «небезопасный; неблагополучный (об обстановке); угрожающий (о словах)».
- `危うい` (line 22; comprehensibility C6, verbatim): «Если так пойдёт и дальше, будущее компании под угрозой.»
- `献立` (line 52; comprehensibility C7, verbatim): «Какой перевод выбрать, зависит от того, что планируют.»
- `学部` (line 37; comprehensibility optional): the sentence «Здесь «факультет» — организационная единица, а не весь
  преподавательский состав.» is deleted. It adapted EN 学部:31 ""Faculty" here is an organizational unit, not simply the
  university's teaching staff."; it carried no link. The next sentence, «Само 学部 не называет отдельного студента
  бакалавриата…», is kept.

All nine are new Batch 250 cards. No navigation-only file changed, so navigation stays at 15 files / 21 links, all
EN-position restorations. The coordinator's candidate edits stand, except that fix 1 retitled 独り言 and 生ずる again and
removed the parenthetical from the 特定 title the coordinator had kept; the titles of 瓦, 倉庫 and 物語る, the 生ずる
and 物語る example 1 edits and the オルガン paragraph are unchanged.

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Correctness F02 was accepted with modification and merged with C2: "F02's «упаковка» is not used: published 包装 owns
  the exact quiz segment «упаковка». No pool title contains «фасов»." The title is C2's wording "shortened from «розлив
  по бутылкам и банкам»"; it uses the plural «в бутылках или банках» rather than C2's «в бутылке или банке», and line 38
  uses «Фасовка» rather than F02's «Такая упаковка».
- Comprehensibility C3 was accepted with modification: "the unqualified «монолог» contradicted line 41; EN "soliloquy"
  is the same sense and «монолог (к себе)» reads awkwardly as a quiz answer"; line 17 keeps "EN's soliloquy point in the
  body".
- Comprehensibility C4 was accepted with modification: "The suggested «обозначение» is not used: in Russian titles it
  reads as a sign or notation (published 符号 «условное обозначение», 番号 «номер (для обозначения)»), and «указание»
  would repeat 指定's leading segment, which the reviewer also advised against."
- Comprehensibility C5 was accepted; "«неспокойный» is not added because it is 騒がしい's title segment."
- Consistency F1 was declined: "長短 «длина; достоинства и недостатки» and 特長 «сильная черта; отличительное
  достоинство» share the «достоин-» stem and the evaluative merit sense, so the conservative guard stays; it removes no
  needed distractor."
- Consistency F2 and F3 needed no action ("reviewer: conservative, no change needed").
- Consistency F4 was "RESOLVED BY C1, no guard added": "C1 removes «вызывать» from 生ずる's title, so the overlap
  disappears and no 呼ぶ exclusion is needed".
- Consistency F5 and the comprehensibility `kango` optionals (瓶詰:31, 献立:33) were declined: "Frozen EN 瓶詰:34 states
  the same app policy ("The app groups on-first mixed compounds under `kango`"), and published RU 派手, 王様, 蛇口 and 見本
  use the same sentence. It answers the visible `kango` tag on a mixed reading and is kept for consistency."
- The consistency optional polish notes on 現に's register and 特定's «выявление» were declined ("reviewer: not
  defects").

Post-fix screen: a saved rerun at the committed `9e339f5` over all 30 batch words (`b250-fix-screen.txt`, 294 lines)
has 42 `OK` lines for pairs already guarded by an exclusion and 252 `!!` lines. It has two exact-segment lines, both
`OK` and guarded by the batch card's own EN entry: 生ずる–生じる («возникать», «порождать»; the two titles are now
identical) and 物語る–語る («рассказывать»). The unguarded 生ずる–呼ぶ «вызывать» line of the candidate screen is gone.
Against the candidate screen (321 lines) it removes 51 lines and adds 24, all from the five retitles: 生ずる 5 removed
and 2 added, 瓶詰 3 and 3, 独り言 17 and 17, 特定 9 and 2, 物騒 16 removed, and one 怪しい–生ずる «вызыв» line removed.
The dispositions record the remaining hits of the changed titles as stem-only ("生ずる «возни-» ~ 誕生; 瓶詰 «банка» ~
支店/缶; 独り言 «разго-/собой» ~ ordinary speech and «с собой» titles; 特定 «конкр-» ~ 場面), none a competing answer"; the
consistency recheck found that paragraph matches its observation.

Net change from the candidate:
- titles and H1s of 瓶詰, 生ずる, 独り言, 特定 and 物騒;
- prose in 瓶詰 (lines 16, 20 and 38), 生ずる (line 16), 独り言 (line 17), 危うい (line 22) and 献立 (line 52);
- one sentence deleted in 学部 (line 37);
- the kana spacing of two readings in 怪しい (lines 20–21);
- no exclusion or link added, removed or retargeted.

No Japanese example sentence, kanji card, EN exclusion, RU-added exclusion, non-title front-matter field or navigation
file changed. None of the five old titles occurs anywhere in RU at the fix. The content diff `4a5e70f..9e339f5 --
words` is 9 word files, 19 lines added and 20 removed (学部 loses its deleted sentence); with `manifest.json` the fix
changes 10 files, 29 lines added and 30 removed.

Fix 1 validation, as recorded in the dispositions: "`tools/validate.py` 0 errors; manifest rebuilt (5,619 files,
contentVersion 14b5ac2292329014); 124 unit tests OK; content budget OK; `git diff --check` clean." For this record link
parity was verified again over the 45 batch paths at `9e339f5`: "checked 45", no LOST link and EXTRA only the four
pre-existing RU-only navigation-file links (kanji/危 → 急 and 危ない, バイオリン → 弾く, 学会 → 社会), as at the
candidate; the fix diff adds, removes or retargets no link.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the correctness recheck says "Model identity not verifiable.", and the consistency and comprehensibility rechecks
"Model: not verifiable." The dispositions label each reviewer's model "per runtime status".

The rechecks ran serially, one reviewer at a time, in one round: comprehensibility, then correctness, then consistency,
each on the fix diff `4a5e70f..9e339f5` (9 word files and `manifest.json`). The initial reviews had run correctness,
then consistency, then comprehensibility. These orderings rest on the coordinator's session records; the recheck reports
do not record times. There was no second fix and no follow-up exchange.

Rechecks were returned as separate reports rather than appended to the initial review files: the full texts are in
`b250-recheck-correctness.md`, `b250-recheck-consistency.md` and `b250-recheck-comprehensibility.md` in the
coordinator's session folder, and their content is recorded in the round table below. The recheck briefs are saved in
the same folder as `b250-recheck-msg-comprehensibility.txt`, `b250-recheck-msg-correctness.txt` and
`b250-recheck-msg-consistency.txt`; the correctness and consistency briefs were sent inline and saved afterwards,
verbatim from the agent history. Each brief gave the reviewer its own original report, the coordinator's dispositions
for all three facets (not the other reviewers' reports) and the fix diff, and repeated the read-only and no-generator
rules ("do not run tools/build_manifest.py or any other generator (tools/validate.py is allowed; remove any
Python bytecode cache it leaves)", paraphrased here only in naming the cache directory).

No recheck reported running a generator. The consistency recheck records "`tools/validate.py` reports 0 errors. I
removed the" Python bytecode cache under `tools` "the validator left behind."; the correctness recheck records
"Coordinator validation/title-screen claims were not independently rerun." and "no validator, generator, build,
app/native-speaker acceptance or exhaustive quiz/comparison-card audit performed"; the comprehensibility recheck records
"No repo file written." and makes no statement about validators or generators. The correctness recheck records
`9e339f53811e17e54bcdf70d695fff995fe3415a` with parent `4a5e70f1dff84c8e692a1d3c7f9c7c7bd01ce45c` and "git status
--porcelain empty at start and report write."; the consistency recheck records the same HEAD and parent `4a5e70f` with
"`git status --porcelain` was empty at the start and at the time of writing."; the comprehensibility recheck records the
same HEAD and parent with "`git status --porcelain` empty at start and at write." The RU primary checkout was at HEAD
`9e339f53811e17e54bcdf70d695fff995fe3415a` and clean when these records were drafted.

### Round 1 (`9e339f5`)

| Facet | Scope and result |
|---|---|
| Comprehensibility | `9e339f5`, parent `4a5e70f`, porcelain empty at start and at the write. "Recheck of C1–C7 and the two optional notes against fix 1. Read in full:" the nine changed cards; "Front matter of `生じる`, `包装`, `符号`, `番号`, `騒がしい` checked for the cited collisions." C1–C7 **resolved**, for example C1 "«вызывать» is gone; title `возникать; порождать` matches the accepted remedy."; C2 "«розлив»/«разлил» replaced; plural «в бутылках или банках» is a sound tweak of the suggested singular."; C3 "I agree «монолог (к себе)» would be a poor quiz answer."; C4 "I agree «обозначение» would read as a sign"; C5 "«неспокойный» correctly avoided (`騒がしい`)". "Optional kango sentences withdrawn — decline stands: EN `瓶詰` states the same on-first `kango` policy, and the tag is on the card. Optional `学部` faculty sentence resolved — deleted." New text: "No regression." 生ずる "now shares `生じる`'s title, but line 17 still says it is the bookish variant, the card already excludes `生じる`, and the causing use remains"; 特定's specifying sense is still taught at line 16 and contrasted at line 44; 独り言 line 17 "is natural and agrees with line 41"; «Я разложил джем по банкам» "is ordinary Russian for that action"; 学部 "still makes sense"; 怪しい's spaced kana "is easier, not harder, to read". "Findings: none." Verdicts: "Comprehensibility CLEAN. Scoped coverage CLEAN." Limits: "The other 21 batch cards were not re-read"; "Post-fix title screen was not re-run here; neighbour titles above were read directly. `生じる`'s own body still says «вызывать»; that card was not in this diff and is no longer a shared quiz answer with `生ずる`." |
| Correctness | `9e339f5` against `4a5e70f`, porcelain empty at start and at the write; frozen EN `6af98cb7`. "Read IN FULL each RU words/<name>.md and frozen EN counterpart" for the nine changed cards; "Read original report, dispositions and complete word diff; no other reviewers' reports or agents used." "F01 RESOLVED. 怪しい:20–21 now reproduce both EN kana strings, including internal spaces, exactly."; "F02 RESOLVED WITH MODIFIED REMEDY. Accept «фасовка» instead of «упаковка»: it removes the liquid-only restriction. Gramota defines portioning/packing goods, not only liquids."; "Original Optional NONE"; the original dictionary-access limits "RESOLVED for changed claims" and the empirical/full-corpus limits "OPTIONAL/outside this recheck". New text, per card: 瓶詰 "F02 is fixed, not merely renamed." (JMdict 1491130, Daijisen via Weblio, Gramota фасовка/фасовать); 生ずる "«возникать; порождать» retains intransitive arise and transitive produce/cause" (JMdict 1378660, Gramota породить); 独り言 "accurate self-talk title; qualified «монолог» retains soliloquy" (JMdict 1455670, Daijisen); 特定 "no EN sense is lost from the card" (JMdict 1455210); 物騒 "No scope loss from the shorter title" (JMdict 1502640); 危うい:22 "faithfully matches EN's present jeopardy"; 献立:52 "translation choice now clearly depends on what is being planned, as EN says"; 学部 "deletion removes the English faculty/staff ambiguity only. … No Japanese rule is lost." (Gramota факультет, Kotobank 学部). "Findings: None new or unresolved. All severities: 0. Across all nine cards, non-title metadata and links are unchanged; all 18 Japanese example sentences and internal kana strings match EN. Independently checked the nine manifest SHA-256 values; manifest changes are only these hashes and contentVersion." Verdicts: "CORRECTNESS CLEAN; SCOPED COVERAGE CLEAN. No actionable defect established; not exhaustive certification." Limits: "Recheck bounded to fix passages and full-card context; prior review supplies unchanged material. Coordinator validation/title-screen claims were not independently rerun. No assertion about unrelated declined quiz/comprehensibility suggestions. Original report preserved unchanged; only this new report written." |
| Consistency | HEAD `9e339f5` (parent `4a5e70f`), porcelain empty at the start and at writing; `tools/validate.py` 0 errors, and the bytecode cache it left was removed. "I read the full fix diff for all 9 cards, and 独り言 and 瓶詰 in full. I read the changed regions of 怪しい, 生ずる, 特定, 物騒, 危うい, 献立 and 学部 in context, via grep and diff. I read the dispositions file. Scripted checks: exact-segment collisions after parenthetical stripping, and stem overlaps across all RU word titles. H1/title checks, and a field-level diff of `manifest.json` between 4a5e70f and HEAD." F1 "optional and declined. I accept the decline."; F2 and F3 "no action"; F4 "resolved by C1. … I confirmed that no title now shares the segment with 呼ぶ, and I agree that a guard is unnecessary."; F5 "declined, and I withdraw it."; 現に "declined as polish. I accept."; 特定 «выявление» "addressed in part. … The «выявление» segment is unique in the corpus. Resolved." New text: every changed H1 ends with its title; "only `title` changed. `quiz_exclusions` are unchanged."; 瓶詰 "only 瓶詰 owns «фасов»"; 生ずる's title "now equals 生じる's title exactly, and these are the only two cards with those segments", judged safe by the exclusion and the あさって/明後日 and やっぱり/やはり precedents; 独り言, 特定 and 物騒 segments unique, with 独り言 "Line 17 is long (cosmetic only)."; the 学部 deletion "leaves no dangling reference"; the manifest "differs from 4a5e70f only in `contentVersion` (`bddfd3e4d9e4aa9d` → `14b5ac2292329014`) and in the 9 hashes of the changed cards. The file count is unchanged at 5,623 entries." (see the manifest paragraph above); the dispositions' post-fix screen paragraph "matches". "Findings: none. No new or unresolved actionable items." Verdicts: "CONSISTENCY: CLEAN on HEAD. QUIZ SAFETY: CLEAN on HEAD." Limits: "The unique-segment screen covers the 3,600+ RU word titles with my own parser"; "I did not re-read all 30 batch cards beyond the changes. The decline of F1 is a judgement call on my side." |

No recheck raised a new finding or left an optional note open. The consistency reviewer's remark that 独り言 line 17 is
long was "cosmetic only" and was not raised as a finding; the comprehensibility reviewer's note that 生じる's body still
says «вызывать» concerns a card outside the diff and is recorded as a limit. There was no second fix.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F01: 怪しい:20–21 kana spacing (Low, P3; scoped coverage) | **Resolved** | `怪しい.md:20–21`; correctness recheck "F01 RESOLVED"; comprehensibility recheck "spaced kana matches EN". |
| Correctness F02: 瓶詰 «розлив» (Medium, P2) | **Resolved** (with modified remedy; merged with C2) | `瓶詰.md:4,12,16,20,38`; correctness recheck "RESOLVED WITH MODIFIED REMEDY"; JMdict 1491130, Gramota фасовка. |
| Consistency F1: 特長→長短 guard not needed (low) | **Optional**; declined, guard kept | Consistency recheck "optional and declined. I accept the decline." |
| Consistency F2: 特長→節 conservative, 特長→武器 justified (low) | **Accepted**; no action | Consistency recheck "no action. Closed as "conservative, kept"." |
| Consistency F3: 楽器→器具 conservative (low) | **Accepted**; no action | Consistency recheck "no action, as above." |
| Consistency F4: optional 呼ぶ guard on 生ずる (optional) | **Resolved** by C1; no guard added | `生ずる.md:4,12`; consistency recheck "resolved by C1". |
| Consistency F5: 献立:32–34 `kango` remark (optional) | **Withdrawn**; decline accepted | Consistency recheck "declined, and I withdraw it."; EN 瓶詰:34. |
| Consistency optional: 現に register | **Optional**; declined, no defect | Consistency recheck "declined as polish. I accept." |
| Consistency optional: 特定 «выявление» indirect | **Resolved** | `特定.md:4,12`; consistency recheck "addressed in part. … Resolved." |
| Comprehensibility C1: 生ずる «вызывать» = 呼ぶ's answer (medium) | **Resolved** | `生ずる.md:4,12,16`; comprehensibility recheck "resolved"; correctness recheck JMdict 1378660; consistency recheck segment check. |
| Comprehensibility C2: 瓶詰 «розлив», long title (medium) | **Resolved** (merged with F02) | `瓶詰.md:4,12,16,20,38`; comprehensibility recheck "a sound tweak". |
| Comprehensibility C3: 独り言 unqualified «монолог» (medium) | **Resolved** (with modification) | `独り言.md:4,12,17`; JMdict 1455670 per the correctness recheck. |
| Comprehensibility C4: 特定 «выявление (причины, лица)» (medium) | **Resolved** (with modification) | `特定.md:4,12`; specifying sense taught at line 16/17 and line 44; JMdict 1455210. |
| Comprehensibility C5: 物騒 definition-like title (low) | **Resolved** | `物騒.md:4,12`; JMdict 1502640. |
| Comprehensibility C6: 危うい:22 future shift (low) | **Resolved** | `危うい.md:22`. |
| Comprehensibility C7: 献立:52 reversed sentence (low) | **Resolved** | `献立.md:52`. |
| Comprehensibility optional: 瓶詰:31 and 献立:33 `kango` sentences | **Withdrawn**; decline stands | Comprehensibility recheck "withdrawn — decline stands"; EN 瓶詰:34. |
| Comprehensibility optional: 学部:37 English "faculty" contrast | **Resolved** | Sentence deleted; comprehensibility recheck "resolved — deleted"; correctness recheck "No Japanese rule is lost." |

Cross-batch note: links to absent targets stay plain. Seven EN link occurrences in this batch's new cards, to 7 targets,
are absent from RU: words 枯れる (from 生える) and 学級 (from 学科), and kanji 甘 (from 甘やかす), 瓶 and 詰 (from 瓶詰), 怪
(from 怪しい) and 庫 (from 倉庫). 怪しい's EN link to the article `ayashii-and-related-words.md` is also plain, because the
article does not exist in RU. The other written kanji without an RU kanji card (倉, 器, 独, 献, 率, 琴, 瓦 and 騒) have no
EN kanji card either. No link is lost to an existing target, and the new cards have no RU-only link. The four RU-only
links in the navigation files kanji/危, バイオリン and 学会 predate this batch and are unchanged. No link was held from an
earlier batch, and none is held for a later one. The fifteen navigation-only restorations (kanji/卒.md line 56 to 率直;
kanji/危.md lines 34 and 44 to 危うい; kanji/定.md lines 35 and 44 and kanji/規.md lines 20, 32 and 36 to 定規;
words/いかがわしい.md line 31, words/奇しい.md lines 15 and 29, words/妖しい.md lines 15 and 28 and words/疑わしい.md line 31
to 怪しい; words/バイオリン.md line 28 and words/ピアノ.md line 40 to 楽器; words/女王.md line 31 to 王女; words/学会.md line
33 and words/課程.md line 29 to 学科; words/挿す.md line 36 to 生け花; words/発売.md line 29 to 特売) are unchanged by fix
1. Every exclusion target resolves to a card published at the baseline or to a batch card. The scratch lane copies of the
nine fixed cards used for later batches (B251–B260 lanes) still carry the candidate text; the dispositions record that
they "are resynced when the B251 candidate is built". That resync is outside this batch.

## Final exclusion set

All 117 EN exclusion entries (23 lists; EN has none on 生る, 生け花, 甘やかす, 瓦, オルガン, 倉庫 or 定規) are retained in
EN order; 10 of them lie inside the batch, and the other 107 target existing RU cards. Eighteen direct, one-sided entries
are added on twelve new cards; each is appended at the end of its list:

- 生る→実, 収穫: `[実, 収穫]`;
- 瓶詰→缶詰: `[瓶, 詰める, 缶詰]`;
- 楽器→器具: `[道具, オルガン, ピアノ, バイオリン, ギター, 笛, 器具]`;
- 学科→学問: `[科目, 学部, 分野, 専攻, 教室, 課, 課程, 学問]`;
- 独り言→会話, 話: `[話す, 言う, 会話, 話]`;
- 特色→癖: `[特徴, 特長, 独特, 性質, 性格, 質, カラー, 素質, 長所, 得意, 味噌, 利益, 人物, 機能, 癖]`;
- 特長→節, 武器, 長短: `[特色, 特徴, 長所, 得意, 味噌, 利益, 機能, 節, 武器, 長短]`;
- 指定→示す, 定期: `[指す, 決める, 選ぶ, 選択, 決定, 示す, 定期]`;
- 特定→具体: `[指定, 指す, 決める, 決定, 特殊, 具体]`;
- 特売→発売: `[売る, 販売, 発売]`;
- 危うい→重体: `[危ない, 危険, 怪しい, 疑わしい, 重体]`;
- 物置→押し入れ, 貯蔵: `[倉庫, 小屋, 押し入れ, 貯蔵]`.

All eighteen were present at the candidate and accepted by the coordinator with the reasons quoted in the independent
review record; fix 1 added, removed or reordered none of them, and the drafted 王女→王子 was dropped before the candidate.
None targets a batch word; 発売 is a card published in Batch 249. The consistency reviewer classed 生る→実, 収穫,
瓶詰→缶詰, 学科→学問, 特定→具体, 特色→癖, 特長→武器 and 特売→発売 as required and the others as plausible or conservative,
with F1 calling 特長→長短 "not needed"; the dispositions kept it, and the consistency recheck accepted the decline. No
target card declares the reverse pair. Every RU addition is appended at the end of its list, and no EN entry is removed
or reordered. Android applies each declaration symmetrically (EN `docs/content-format.md`, lines 162–165), so no
reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (瓶詰 F02); CLEAN at recheck for all nine changed cards.
- Scoped coverage: **CLEAN** after fix 1 (怪しい F01); CLEAN throughout in the comprehensibility review and recheck.
- Comprehensibility: **CLEAN** after fix 1 (生ずる, 瓶詰, 独り言, 特定, 物騒, 危うい, 献立 and 学部); the modified
  dispositions of C3 and C4 stand as accepted, and the `kango` decline stands.
- Cross-file consistency: **CLEAN** throughout; the 21 restored navigation links in 15 files and the four pre-existing
  RU-only navigation-file links stand.
- Quiz safety: **CLEAN** throughout; the 生ずる–呼ぶ «вызывать» overlap is gone after fix 1 (C1, F4), and the eighteen RU
  additions stand. This covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

## Limits

- The rechecks reread the changed cards and the lines needed to judge them; the unchanged cards rest on review 001, in
  which all three reviewers read all 30 cards in full. The correctness recheck states "prior review supplies unchanged
  material."; the comprehensibility recheck "The other 21 batch cards were not re-read"; and the consistency recheck "I
  did not re-read all 30 batch cards beyond the changes."
- In review 001 the consistency reviewer's dictionary bases rested "on my own JMdict knowledge, not a live lookup", and
  its title-screen and other-mention parity checks were partial. At recheck its unique-segment screen used its own
  parser, and its manifest entry count (5,623) differs from the committed 5,619 for an unrecorded reason. The
  comprehensibility recheck did not re-run the title screen; the correctness recheck did not rerun the coordinator's
  validation or title screen. Link parity at the fix was rerun for this record. Necessity classes are judgements, not
  measurements.
- 生じる's own body still says «вызывать»; the card is outside this batch and no longer shares a quiz answer with 生ずる.
- The correctness recheck is "not exhaustive certification"; no full-corpus synonym or runtime quiz audit was made.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fix, so its payload hashes describe the candidate `4a5e70f`, not `9e339f5`.
- Frequency and preferred register (for example «фасовка», «небезопасный» and «разговор с самим собой») were not
  certified. Online dictionaries were current observations, not pinned archives. The app's quiz selection was not
  inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
