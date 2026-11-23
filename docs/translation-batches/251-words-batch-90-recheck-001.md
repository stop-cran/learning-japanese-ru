# Batch 251 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `8bb7b574df56eb149c7b7c22a70aae4cde4bbee6` | `af91f2d01fc3555bf1190ac60079f79715e80cb7` | Initial review snapshot: the signed candidate, on `origin/full-ru-251-words-90`. |
| `e290cd22b5454c58fbae4cc2e40ba53ec135e803` | `68e266498dacebc77b2621598b848238de1c3e2e` | Fix 1 (final candidate). It covers correctness F1 and the correctness optional notes on 射す:39, あぶる:41 and 照る (the last three via comprehensibility C1, C2 and C5), consistency items 1–4, 8 and 10 (item 11 via C5), and comprehensibility C1, C4, C5 and C11 (verbatim) and C2, C3, C6, C7, C8 and C10 (with modification); it declines the correctness optional on 照らす «озарять», consistency item 7 and comprehensibility C9, takes no action on consistency items 5, 6, 9, 12 and 13 or on the comprehensibility optionals. It retitles 焚く, 加熱, 煎る, 片寄る and 照る, rewrites prose in 焚く, 焦がす, 燃やす, 射す, あぶる, 煙突 and 照らす, deletes one English-dependent sentence in 射す, removes four RU-added exclusions and adds two, and adds, removes or retargets no link and changes no navigation-only file. Signed; on `origin/full-ru-251-words-90`. |

The fix regenerated `manifest.json`; both snapshots record 5,649 entries (5,644 `files` + 3 images + 2 scenes).
`contentVersion` is `703a555ae1987ab0` at the candidate and `5cf3a145293b1c8c` after fix 1; the manifest differs only in
`contentVersion` and the fourteen hashes of the changed cards. The consistency recheck gives the same count ("Counts:
5,644 files, 3 images, 2 scenes, so 5,649 entries."). The intake was not refreshed; it still records the candidate's
payload hashes. The commit message reads "Batch 251: fix 1 after blind review", followed by "Address blind
correctness, consistency and comprehensibility findings on candidate 8bb7b574: correct 焚く (no «растапливать» for a
bath), Russian-specific transitivity notes for 焦がす/燃やす, ordinary quiz titles for 加熱, 煎る, 片寄る, 照る, remove
English-only and source-list remarks, state 煙突's slang sense, and drop RU-added antonym guards (片道, 片寄る, 休業,
暖まる)." and the co-author trailer.

Fix 1:
- `焚く` (lines 4, 12, 17 and 31–32; correctness F1, verbatim, and comprehensibility C8, with modification): title and
  H1 «жечь топливо; разводить и поддерживать огонь» instead of «жечь (топливо); растапливать (печь, ванну)»; line 17
  «топливо или благовония, топить печь или котёл, нагревать воду для ванны.»; lines 31–32 «[焼く](焼く.md) читается やく.
  В словарной статье 焼く есть устаревшее написание 焚く（やく）, но это не значит, что современные 焚く（たく）и 焼く
  свободно обмениваются чтениями.» Line 24's «нагреть ванну» "is already correct and stays".
- `加熱` (lines 4 and 12; comprehensibility C4, verbatim): title and H1 «нагревание; подведение тепла» instead of
  «подогрев; тепловая обработка» ("EN "heating; applying heat", JMdict 1190470. The body already used this wording at
  line 16.").
- `煎る` (lines 4 and 12; comprehensibility C6, with modification): title and H1 «обжаривать без масла; подсушивать на
  огне» instead of «обжаривать без масла; подсушивать на огне; поджаривать (зёрна, семена)».
- `片寄る` (lines 4, 9 and 12; comprehensibility C11, verbatim, and consistency item 2): title and H1 «смещаться в одну
  сторону; быть предвзятым» instead of «крениться в одну сторону; быть однобоким, предвзятым»; exclusions `[傾く, ずれる]`
  instead of `[傾く, 公平]`.
- `照る` (lines 4, 9 and 12; comprehensibility C5, verbatim, also consistency items 8 and 11 and the correctness
  optional): title and H1 «светить (о солнце, луне); быть солнечным (о погоде)» instead of «лить свет (о солнце, луне);
  быть солнечным (о погоде)»; 快晴 appended to the exclusions.
- `射す` (old lines 39–40; comprehensibility C1 and the correctness optional): the sentence «Старая английская глосса
  strike («ударять») может означать, что свет достигает поверхности; она не придаёт глаголу общего значения удара.» is
  deleted. It adapted EN 射す:39 "The legacy gloss "strike" can refer to light reaching a surface; it does not give this
  verb a general hitting sense."; it carried no link. The next line «射す — и не общий глагол для стрельбы из оружия.»
  becomes «射す — не общий глагол для стрельбы из оружия.» (now line 39).
- `あぶる` (line 41; comprehensibility C2, with modification): «Не переводите каждое あぶる словом «опаливать»: так
  передаётся лишь часть употреблений.» instead of «Не переводите каждое употребление словом «опаливать» только потому,
  что исходный список слов даёт такую глоссу.»
- `焦がす` (lines 45–46; comprehensibility C3, with modification): «Объект с を не делает глагол 焦げる. Русские
  «подпалить» и «подгореть» тоже различают переходность, но одно «сжечь» не выбирает между 焦がす, 焼く и 燃やす（もやす）.»
  instead of «Объект с を не делает глагол 焦げる, а одно русское «сжечь» не подсказывает, какая японская конструкция
  подходит.»
- `燃やす` (lines 21, 43 and 45; comprehensibility C10, with modification): line 21 «Спортсмены полны боевого духа.»;
  line 43 «Русские «сжигать» и «гореть» тоже различают переходность, но одно «жечь» не выбирает между 燃やす, 焼く и
  焦がす.»; line 45 ends «…даже если по-русски это передают как «полны боевого духа».»
- `煙突` (line 44; comprehensibility C7, with modification): the sentence now reads «В изученной словарной статье есть и
  отдельное жаргонное значение: везти пассажира такси, не включив счётчик; это не строительное значение этой
  карточки.» instead of «…есть и отдельное жаргонное значение, связанное с таксометром; это не строительное значение
  этой карточки.» ("The wording follows JMdict 1177320 sense 2 (Slang), which was verified on jisho.")
- `照らす` (line 45; consistency item 10): the 参考 gloss becomes «справка, обращение к источнику» instead of «справка,
  ориентир» ("EN "reference/consultation"; «ориентир» belongs to 目安").
- `片道`, `休業` and `暖まる` (line 9; consistency items 1, 3 and 4): the RU-added exclusions 往復, 営業 and 暖房 are
  removed, leaving `[切符]`, the nine EN entries and `[暖める, あぶる]` respectively.

All fourteen are new Batch 251 cards. No navigation-only file changed, so navigation stays at 4 files / 4 links, all
EN-position restorations. The coordinator's candidate edits stand: fix 1 did not touch 熱する or 怠る, and changed 暖まる
only in its `quiz_exclusions`, so its rewritten distinctive paragraph is unchanged. Fix 1 did change several items the
coordinator had kept: the 照る, 加熱 and 煎る titles, the 射す "strike" note (deleted) and the RU-added guards 暖まる→暖房
and 休業→営業 (removed).

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Correctness F1 was accepted with the reviewer's remedy for the title and line 17; "Line 24's «нагреть ванну» is
  already correct and stays."
- Comprehensibility C1: "The suggested «свет не бьёт» is not used, because «свет бьёт в окно» is idiomatic Russian."
- Comprehensibility C2 was accepted with modification: "Line 42 already names the nori and warming-hands uses, so the
  suggested list is not repeated."
- Comprehensibility C3 was accepted with modification: "This uses the pair already shown at lines 43–44."
- Comprehensibility C6 was accepted with modification: "The reviewed «без масла» is kept rather than «всухую», and the
  body (line 16) keeps «поджаривать (зёрна, семена)»."
- Comprehensibility C7 was accepted with modification: "The wording follows JMdict 1177320 sense 2 (Slang), which was
  verified on jisho."
- Comprehensibility C8 was accepted with modification: "The reviewer had not checked the tag. JMdict 1350600 (焼く)
  marks 焚く as "Out-dated kanji or kanji usage", verified on jisho."
- Comprehensibility C10 was accepted with modification: "The reviewer's «разжигают в себе» is not used: a transitive
  Russian rendering would erase EN's point that the emotional construction keeps を even when the translation sounds
  intransitive."
- Comprehensibility C11 was accepted: "«клониться или смещаться» stays in body line 16. The new title shares the head
  verb «смещаться» with published ずれる «смещаться (с места); …», so the fix adds the direct guard 片寄る→ずれる."
- Comprehensibility C9 (an incense title for 焚く) was declined: "EN's title lacks incense, and the body teaches it
  (lines 17, 21). The suggested title also retained the «растапливать (…ванну)» error fixed under F1."
- The correctness optional on 照らす «озарять» was declined: "The everyday «освещать» comes first, and the title mirrors
  EN "illuminate; shine on". The reviewer marks this as optional register polish."
- Consistency item 7 (片寄る ~ 片道 «в одну сторону») was declined: "A verb and a noun ("one-way") are not a defensible
  confusion, and the reviewer rates the risk low."
- Consistency items 5 and 6 needed no action ("The reviewer marks these guards as conservative or required."), nor did
  item 9 or items 12 and 13 ("Both are consistent with published cards and EN parity."); item 11 was covered by C5.
- The comprehensibility optional notes needed no change ("The reviewer marks them clear or low-impact.").

Quiz-exclusion changes. Comparing each card's `quiz_exclusions` with frozen EN gives 16 RU-added pairs on 13 cards at
the candidate and 14 on 11 cards at the fix. Fix 1 removed four:
- 片道→往復 (往復 «туда и обратно; билет туда и обратно»), 片寄る→公平 (公平 «справедливый; беспристрастный») and
  休業→営業 (営業 «коммерческая деятельность; продажи»), consistency items 1–3 (LOW, "unnecessary"); the dispositions:
  "These are RU-added guards on antonyms or contrasts with no shared title wording. EN shows the same relationships
  without a guard. A guard would hide a pair the articles teach as a contrast.";
- 暖まる→暖房 (暖房 «отопление; обогрев помещения»), consistency item 4 (LOW, "inconsistent"); the dispositions:
  "暖める carries no 暖房 guard, and 暖房 is a noun. The guard is dropped rather than copied to 暖める, so 暖まる's exclusions
  are [暖める, あぶる]."

It added two:
- 照る→快晴 (快晴 «безоблачная погода; ясное небо»), consistency OPTIONAL item 8; the dispositions: "照る's new title
  «…быть солнечным (о погоде)» shares the «погод-» stem with 快晴. This matches the existing 晴れ guard." The author had
  declined it at drafting ("verb title against a noun title, and 晴れ is already guarded");
- 片寄る→ずれる (ずれる «смещаться (с места); не совпадать (по времени, сути)»), comprehensibility C11; the new title
  shares the head verb «смещаться» with published ずれる.

At recheck the consistency reviewer classed items 1–4 and 8 as "RESOLVED" (for example item 1: "片道 now has `[切符]`
only, and EN has none."; item 8: "It is justified and direct."), item 7 as "OPTIONAL, decline accepted. Verb vs noun,
with different head words «смещаться» vs «путь/билет». The pair is not a defensible confusion.", and on the
unguarded 逸れる: "逸れる left unguarded: agreed. «отклоняться в сторону (от пути, цели)» is qualified as leaving a route
or topic, and the head verb differs from «смещаться». 片寄る→ずれる is the right direct guard, since ずれる shares the head
verb «смещаться» exactly." The dispositions' reason for leaving 逸れる unguarded: "逸れる «отклоняться в сторону (от
пути, цели); уходить от темы» is qualified as leaving a path or topic, not as being lopsided or biased, so it is left
unguarded." The comprehensibility recheck judged C11's "Guard vs ずれる «смещаться (с места)» is justified." and noted
that 片道, 休業 and 暖まる "change only exclusions; bodies still teach 往復, 営業 and 暖房, and the titles do not collide";
the correctness recheck found "added ずれる exists and has a directly overlapping title", 照る's "All six EN exclusions
remain in order, followed by 晴れ and 快晴; new target exists", and for 片道, 休業 and 暖まる that only the RU-added entry
was removed and the body is unchanged.

Post-fix screen: a saved rerun at the committed `e290cd2` over all 30 batch words (`b251-fix-screen.txt`, 325 lines)
has 29 `OK` lines for pairs already guarded by an exclusion and 296 `!!` lines. It has no exact-segment line. Against
the candidate screen (313 lines) it removes 7 lines and adds 19, all from the title and exclusion changes:
- 加熱: 4 removed (処理, 工業, 温い and the `OK` 暖める line) and 5 added (受ける, 架空 and 沸く `!!`; 沸かす and 熱する `OK`);
- 煎る: 3 removed (かりかり, ちょこちょこ, 蒔く), none added;
- 焚く: 11 added `!!` stem-only lines («подде-», «разво-» and «огонь»: 地盤, 広げる, 援助, 支える, 有難い, 本物, 火, 維持, 賛成,
  離婚, 飼う); the candidate title had no screen line;
- 照る: 2 added (光る `OK`, 明かり `!!`);
- 片寄る: 1 added (ずれる `OK`).

Two existing lines changed status: 片道 ~ 往復 «билет» from `OK` to `!!` (the removed guard) and 照る ~ 快晴 from `!!` to
`OK` (the added guard). Other lines of the retitled cards are reworded only (片寄る 36, 照る 16, あぶる ~ 煎る 1 and
片道 ~ 片寄る 1). 公平, 営業 and 暖房 did not appear in either screen. The dispositions record the remaining hits of the
changed titles as stem-only ("片寄る «сторо-» ~ side and direction titles (あちら, 一方, 片道, 逸れる and others);
«предв-» ~ preview titles (予約, 予期 and others)"; "加熱 «подве-» ~ 受ける, 架空; «нагре-» ~ 沸く «кипеть; нагреваться»
(an intransitive boiling verb)"; "焚く «подде-/разво-» ~ support and breeding titles; «огонь» ~ the noun 火 «огонь;
пламя»"; "照る «погод-/солнц-/свети-» ~ weather nouns, 太陽, 日, 日光, 昇る and 明かり"), "none a competing answer". The
consistency recheck re-ran the screen and reported "296 `!!` stem-only rows and 29 OK rows, with no unguarded exact
segment", matching the saved file; it also stated "The four dropped pairs no longer appear at all." and that 片道's
title "shares no wording with 往復". The saved screen still has the stem-only line `!! 片道 «путь в одну сторону; билет
в один конец» ~ 往復 «туда и обратно; билет туда и обратно» seg=[] stem=['билет']`; the shared word is «билет», a
stem-only, not an exact-segment, hit. The 往復 card is the batch's navigation target in the opposite direction
(往復:35 → 片道).

Net change from the candidate:
- titles and H1s of 焚く, 加熱, 煎る, 片寄る and 照る;
- prose in 焚く (lines 17 and 31–32), 焦がす (lines 45–46), 燃やす (lines 21, 43 and 45), 射す (line 40, now 39), あぶる
  (line 41), 煙突 (line 44) and 照らす (line 45);
- one sentence deleted in 射す (old line 39);
- exclusions: 往復, 公平, 営業 and 暖房 removed from 片道, 片寄る, 休業 and 暖まる; 快晴 and ずれる appended to 照る and 片寄る;
- no link added, removed or retargeted.

No Japanese example sentence, kana reading, kanji card, EN exclusion, non-title front-matter field other than
`quiz_exclusions`, or navigation file changed. None of the five old titles occurs anywhere in RU at the fix. The
content diff `8bb7b57..e290cd2 -- words` is 14 word files, 27 lines added and 28 removed (射す loses its deleted
sentence); with `manifest.json`, 42 lines added and 43 removed.

Fix 1 validation, as recorded in the dispositions: "`tools/validate.py` 0 errors; manifest rebuilt (5,649 files,
contentVersion 5cf3a145293b1c8c); 124 unit tests OK; content budget OK; `git diff --check` clean." For this record link
parity was verified again over the 34 batch paths at `e290cd2`: "checked 34", no LOST link and EXTRA only the
pre-existing RU-only navigation-file link words/光る → words/輝く (line 32), as at the candidate; the fix diff adds,
removes or retargets no link.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the correctness recheck says "Model ID unavailable; dispositions label original run gpt-6.1-sol, not
independently verified.", the consistency recheck "Model: not verifiable from inside the session." and the
comprehensibility recheck "Model: not verifiable from the session." The dispositions label each reviewer's model "per
runtime status".

The rechecks ran serially, one reviewer at a time, in one round: comprehensibility, then correctness, then consistency,
each on the fix diff `8bb7b57..e290cd2` (14 word files and `manifest.json`). The initial reviews had run correctness,
then consistency, then comprehensibility. These orderings rest on the coordinator's session records; the recheck reports
do not record times. There was no second fix and no follow-up exchange.

Rechecks were returned as separate reports rather than appended to the initial review files: the full texts are in
`b251-recheck-correctness.md`, `b251-recheck-consistency.md` and `b251-recheck-comprehensibility.md` in the
coordinator's session folder, and their content is recorded in the round table below. The recheck briefs are saved in
the same folder as `b251-recheck-msg-comprehensibility.txt`, `b251-recheck-msg-correctness.txt` and
`b251-recheck-msg-consistency.txt`; the comprehensibility brief was sent inline and saved afterwards, the correctness
brief was saved at the same time, and both were checked against the agent history; the consistency brief was saved
before it was sent. Each brief gave the reviewer its own original report, the coordinator's dispositions for all three
facets (not the other reviewers' reports) and the fix diff, and repeated the read-only and no-generator rules ("do not
run tools/build_manifest.py or any other generator (tools/validate.py is allowed; remove any" Python bytecode cache "it
leaves)", paraphrased here only in naming the cache directory).

No recheck reported running a generator. The correctness recheck records "No repository changes or generators." and
"python -X utf8 -B tools/validate.py: exit 0, 0 errors; no" bytecode cache "created. git diff --check clean."; the
consistency recheck records "`tools/validate.py` gives 0 errors. I removed no" bytecode cache "because I used `python
-B`. Nothing was written inside the repository."; the comprehensibility recheck records "title screen and validate.py
not re-run" and makes no statement about generators. The correctness recheck records
`e290cd22b5454c58fbae4cc2e40ba53ec135e803` with parent `8bb7b574df56eb149c7b7c22a70aae4cde4bbee6`, "both verified. git
status --porcelain empty at start and immediately before writing."; the consistency recheck records the same HEAD and
parent with "`git status --porcelain` was empty at start and at write."; the comprehensibility recheck records the same
HEAD and parent with "status --porcelain empty at start and at write. Original report not rewritten." The RU primary
checkout was at HEAD `e290cd22b5454c58fbae4cc2e40ba53ec135e803` and clean when these records were drafted.

### Round 1 (`e290cd2`)

| Facet | Scope and result |
|---|---|
| Comprehensibility | `e290cd2`, parent `8bb7b57`, porcelain empty at start and at the write. "Scope: comprehensibility and scoped coverage on HEAD. Read in full: 焚く 焦がす 燃やす 加熱 煎る 片寄る 照る 照らす 射す あぶる 煙突 片道 休業 暖まる, plus the fix diff and dispositions. Title spot-check: ずれる 快晴 往復 営業 暖房." C1–C8, C10 and C11 **resolved**, for example C1 "射す:39 English "strike" is gone. … Skipping «свет не бьёт» is right: «свет бьёт в окно» is idiomatic."; C3 "teach a contrast Russian has: «подпалить» takes を, «подгореть» takes が. … The false particle claim is gone."; C6 "Keeping «без масла» is clearer than «всухую»"; C7 "now state the slang: carry a taxi passenger without the meter. Usable. "В изученной словарной статье" is mild meta, not a remaining defect."; C8 "A beginner can use that."; C10 "Not using «разжигают» as the translation is right: it would hide that point."; C11 "Guard vs ずれる «смещаться (с места)» is justified." "C9 withdrawn. Decline is reasonable. EN's title has no incense, and the suggested title kept the wrong «растапливать ванну». … The quiz title need not list every example." "Optional unchanged, still not actionable", including "照らす «озарять» after «освещать» (decline reasonable)"; "参考 gloss is now «справка, обращение к источнику», which is clearer than «ориентир»." New text: "no comprehension regression. 焚く's new title does not name bath, stove or incense, but line 17, in the opening paragraph, does, so a beginner still learns those uses." "Findings: none." Verdicts: "comprehensibility CLEAN. scoped coverage CLEAN." Limits: "raw JMdict XML not re-read; title screen and validate.py not re-run (dispositions already report validate 0 errors and no unguarded exact-segment hit). Other reviewers' original reports not read. Author reports, batches and scratch worktrees not read." |
| Correctness | `e290cd2` against `8bb7b57`, porcelain empty at start and immediately before writing; frozen EN `6af98cb7`. "Read IN FULL these 14 RU cards AND frozen EN counterparts"; "Read original report, dispositions and full words fix diff. No other reviewers' reports or scratch worktrees read." "F1, 焚く:4,12,17 — RESOLVED. Title/H1 and line 17 implement the requested remedy exactly."; optional 射す "RESOLVED. … No Japanese rule lost."; optional あぶる:41 "RESOLVED"; optional 照る «лить свет» "RESOLVED"; optional 照らす «озарять» "OPTIONAL, not an unresolved defect. Decline accepted". New text, per card: 焚く:31–32 "Canonical JMdict 1350600 explicitly lists 焚く with the out-dated-kanji qualification and reading やく. Separate 1596840 is 焚く/たく."; 焦がす:45–46 "«подпалить» is transitive, «подгореть» intransitive; Russian comparison is true."; 燃やす:21, 43, 45 "«сжигать» transitive versus «гореть» intransitive is true. «Спортсмены полны боевого духа» faithfully renders EN"; 加熱 "accurately covers EN heating/application of heat"; 煎る "no-oil roasting and heat-drying cover the intended roast/parch/toast ingredient senses"; 片寄る "moving to one side/bias are supported"; 照る "sun/moon shining and sunny weather supported by Daijisen senses 1–2"; 照らす:45 «справка, обращение к источнику» "fits reference/consultation in context, not 目安's benchmark sense"; 射す:39–40 "deletion removes the English-gloss wrapper, not required Japanese instruction"; 煙突:43–45 "exactly matches JMdict 1177320 sense 2, labelled slang"; 片道, 休業 and 暖まる: only the RU-added entry removed, body unchanged. Evidence: "Re-fetched https://www.edrdg.org/pub/Nihongo/JMdict_e.gz ; inspected complete entries" (13 listed), weblio (Daijisen 照る 1–2), kotobank (煎る), jisho (参考) and ru.wiktionary for the four Russian verbs; "Gramota requests rate-limited/inconclusive." Checks: "Japanese example sentences and kana readings match EN mechanically. Links unchanged versus candidate; title/H1 aligned. All five modified exclusion lists preserve every EN exclusion in EN order. Manifest delta limited to contentVersion and the 14 card hashes." "Findings: None. F1 closed." Verdicts: "HEAD correctness CLEAN; scoped coverage CLEAN." Limits: "Changed-text/EN-preservation recheck, not whole-batch or whole-pool quiz recertification. No app tests, generators or signature cryptographic verification; model ID unverified." |
| Consistency | HEAD `e290cd2` (parent `8bb7b57`), porcelain empty at start and at write; `tools/validate.py` 0 errors, run with `python -B`. "I read the full `git diff -U0 8bb7b574 e290cd22 -- words` (14 cards) and the `manifest.json` diff. The cards were checked at the changed lines plus front matter and H1, not re-read end to end. I compared the exclusions of the five changed-exclusion cards with EN. I ran an exact-segment and stem scan of the five new titles against every RU word title in the corpus. I ran `word_title_screen.py` on the 30 batch words, with `RU_ROOT` set and output written to temp." Items 1–4 "RESOLVED"; 5 "unchanged, no action (agreed)"; 6 "unchanged and still present"; 7 "OPTIONAL, decline accepted"; 8 "RESOLVED. … It is justified and direct."; 9 "no action"; 10 "RESOLVED"; 11 "RESOLVED via C5"; 12 "INFO, unchanged, withdrawn as an issue"; 13 "INFO, unchanged, EN parity"; "逸れる left unguarded: agreed." New text: RU additions appended after EN lists, "All five are direct pairs, declared on one side."; "H1 equals the title on 焚く, 加熱, 煎る, 片寄る and 照る."; "Exact segments after parenthetical stripping: no collision for any of the 5 new titles against the corpus."; 沸く "is intransitive boiling, not a competing answer (low)"; ぐつぐつ "shares only «на огне», a mimetic simmering word, low"; 日光 "is a noun, so I rate it low"; body edits "add no links and no title or exclusion change"; manifest "only `contentVersion` and 14 hashes changed"; post-fix screen "296 `!!` stem-only rows and 29 OK rows, with no unguarded exact segment" (see the post-fix screen paragraph above on its "four dropped pairs" statement). "Findings: none." Verdicts: "consistency CLEAN. Quiz safety CLEAN. No new actionable finding." Limits: "I did not re-read untouched cards of the batch, the 4 navigation files, or the EN texts for the 焚く/煙突/物凄い/煎る line counts from my first review. I did not re-verify JMdict or jisho claims in C7 or C8. Model identity is unverifiable." |

No recheck raised a new finding or left an optional note open. The consistency reviewer's low ratings of 沸く, ぐつぐつ and
日光 were not raised as findings; the comprehensibility reviewer's "mild meta" remark on 煙突's «В изученной словарной
статье» was judged "not a remaining defect". There was no second fix.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 焚く «растапливать (печь, ванну)» (MEDIUM; correctness) | **Resolved** | `焚く.md:4,12,17`; correctness recheck "Title/H1 and line 17 implement the requested remedy exactly."; JMdict 1596840, Kuznetsov РАСТОПИТЬ. |
| Correctness optional: 射す:39 English gloss "strike" | **Resolved** (via C1) | Sentence deleted; correctness recheck "No Japanese rule lost." |
| Correctness optional: あぶる:41 source-list reference | **Resolved** (via C2) | `あぶる.md:41`; correctness recheck "RESOLVED". |
| Correctness optional: 照る «лить свет» | **Resolved** (via C5) | `照る.md:4,12`; Daijisen 照る 1–2 per the correctness recheck. |
| Correctness optional: 照らす «озарять» | **Optional**; declined | Correctness recheck "OPTIONAL, not an unresolved defect. Decline accepted"; comprehensibility recheck "decline reasonable". |
| Consistency 1: 片道→往復 unnecessary (LOW) | **Resolved**; guard removed | `片道.md:9`; consistency recheck "RESOLVED". |
| Consistency 2: 片寄る→公平 unnecessary (LOW) | **Resolved**; guard removed | `片寄る.md:9`; consistency recheck "the screen shows no 公平 hit". |
| Consistency 3: 休業→営業 unnecessary (LOW) | **Resolved**; guard removed | `休業.md:9`; consistency recheck "休業 is now exactly the EN list". |
| Consistency 4: 暖まる→暖房 inconsistent (LOW) | **Resolved**; guard removed | `暖まる.md:9`; consistency recheck "exactly EN". |
| Consistency 5: conservative guards (INFO) | **Accepted**; no action | Consistency recheck "unchanged, no action (agreed)". |
| Consistency 6: required guards | **Accepted**; no action | Consistency recheck "unchanged and still present". |
| Consistency 7: 片寄る ~ 片道 «в одну сторону» (OPTIONAL) | **Optional**; declined | Consistency recheck "OPTIONAL, decline accepted". |
| Consistency 8: 照る→快晴 unguarded (OPTIONAL) | **Resolved**; guard added | `照る.md:9`; consistency recheck "justified and direct". |
| Consistency 9: unguarded non-confusions | **Accepted**; no action | Consistency recheck "no action". |
| Consistency 10: 照らす:45 参考 gloss (LOW) | **Resolved** | `照らす.md:45`; correctness recheck "fits reference/consultation in context"; comprehensibility recheck "clearer than «ориентир»". |
| Consistency 11: 照る title «лить свет» (OPTIONAL) | **Resolved** (via C5) | Consistency recheck "RESOLVED via C5". |
| Consistency 12: bunka.go.jp attribution (INFO) | **Withdrawn**; no action | Consistency recheck "INFO, unchanged, withdrawn as an issue". |
| Consistency 13: 照る lacks `wago` tag (INFO) | **Accepted**; no action (EN parity) | Consistency recheck "INFO, unchanged, EN parity". |
| Comprehensibility C1: 射す:39 English "strike" (medium) | **Resolved** | Sentence deleted; `射す.md:39`; comprehensibility recheck "resolved". |
| Comprehensibility C2: あぶる:41 unseen list (medium) | **Resolved** (with modification) | `あぶる.md:41`; comprehensibility recheck "Clear without English." |
| Comprehensibility C3: 焦がす:45 «сжечь» (medium) | **Resolved** (with modification) | `焦がす.md:45–46`; correctness recheck "Russian comparison is true." |
| Comprehensibility C4: 加熱 title (medium) | **Resolved** | `加熱.md:4,12`; JMdict 1190470. |
| Comprehensibility C5: 照る title (medium) | **Resolved** | `照る.md:4,12`. |
| Comprehensibility C6: 煎る three-clause title (medium) | **Resolved** (with modification) | `煎る.md:4,12`; comprehensibility recheck "Keeping «без масла» is clearer than «всухую»". |
| Comprehensibility C7: 煙突:43 slang unexplained (medium) | **Resolved** (with modification) | `煙突.md:44`; JMdict 1177320 sense 2 per the correctness recheck; "mild meta, not a remaining defect". |
| Comprehensibility C8: 焚く:31 opaque spelling note (medium) | **Resolved** (with modification) | `焚く.md:31–32`; JMdict 1350600 vs 1596840 per the correctness recheck. |
| Comprehensibility C9: 焚く title without incense (medium; coverage) | **Withdrawn**; decline stands | Comprehensibility recheck "C9 withdrawn. Decline is reasonable."; lines 17, 21 and 24 teach the uses. |
| Comprehensibility C10: 燃やす:21, 43, 45 (medium) | **Resolved** (with modification) | `燃やす.md:21,43,45`; correctness recheck "«сжигать» transitive versus «гореть» intransitive is true." |
| Comprehensibility C11: 片寄る «крениться» (medium) | **Resolved**; ずれる guard added | `片寄る.md:4,9,12`; comprehensibility recheck "Guard vs ずれる … is justified." |
| Comprehensibility optionals: 物凄い, 物差し, 爪:30, 煙い:15, 照らす, 怠る, 無限 | **Optional**; no change | Comprehensibility recheck "Optional unchanged, still not actionable". |

Cross-batch note: links to absent targets stay plain. Thirteen EN link occurrences in this batch's new cards, to 9
targets, are absent from RU: kanji 畜 (from 牧畜), kanji 片 (from 片道, 片寄る and 片仮名), words 仮名 (from 片仮名), kanji 温
(from 暖める and 暖まる), kanji 燃 (from 燃やす), words 冷ます (from 熱する), kanji 照 (from 照らす and 照る), words 商店 (from
焦点) and words 無数 (from 無限). The coordinator's adjudication sentence names only 温, 燃, 冷ます, 商店, 無数 and 照. The 30
EN cards have no article link. The other written kanji without an RU kanji card (仮, 凄, 射, 怠, 暖, 焚, 無, 焦, 煉, 煎, 熟,
爪, 牧 and 瓦) have no EN kanji card either. No link is lost to an existing target, and the new cards have no RU-only
link. The RU-only link words/光る → words/輝く (line 32) in a navigation file predates this batch and is unchanged. No
link was held from an earlier batch, and none is held for a later one. The four navigation-only restorations (words/傾く.md
line 36 to 片寄る; words/光る.md line 33 to 照らす; words/往復.md line 35 to 片道; words/炊く.md line 38 to 焚く) are
unchanged by fix 1. Every exclusion target resolves to a card published at the baseline or to a batch card. The
scratch lane copies of the fourteen fixed cards used for later batches (B252–B261 lanes) still carry the candidate
text; the dispositions record that they "are resynced when the B252 candidate is built". That resync is outside this
batch.

## Final exclusion set

All 123 EN exclusion entries (25 lists; EN has none on 片道, 片仮名, 煙突, 煙い or 煉瓦) are retained in EN order; 21 of
them lie inside the batch, and the other 102 target existing RU cards. Fourteen direct, one-sided entries are added on
eleven new cards; each is appended at the end of its list:

- 物差し→単位: `[定規, 基準, 標準, 目安, 水準, 計る, 単位]`;
- 物凄い→莫大: `[凄い, 恐ろしい, 怖い, ひどい, 甚だしい, 大した, 大変, 非常, 非常に, とても, 実に, なんとも, ド, 極, 大いに, どうも,
  ずいぶん, だいぶ, かなり, 相当, なかなか, 大層, うんと, めちゃくちゃ, すばらしい, とんでもない, 激しい, きつい, 莫大]`;
- 牧畜→家畜: `[農業, 飼う, 育てる, 家畜]`;
- 牧場→牧畜, 農家: `[原, 野, 牧畜, 農家]`;
- 片道→切符: `[切符]`;
- 片寄る→ずれる: `[傾く, ずれる]`;
- 焚く→炊く: `[焼く, 焼ける, 焦がす, 焦げる, 燃える, 沸かす, 加熱, 暖める, 炊く]`;
- 照る→晴れ, 快晴: `[光る, 輝く, 射す, 差す, 照らす, 晴れる, 晴れ, 快晴]`;
- 煙突→管, パイプ: `[管, パイプ]`;
- 焦点→注目: `[中心, 要点, 重点, 集中, 点, 注目]`;
- 無限→いつまでも: `[永久, 永遠, いつまでも]`.

Twelve were present at the candidate and accepted by the coordinator with the reasons quoted in the independent review
record; fix 1 removed 片道→往復, 片寄る→公平, 休業→営業 and 暖まる→暖房 and added 照る→快晴 and 片寄る→ずれる, as described
above. None targets a batch word. The consistency reviewer classed 物差し→単位, 物凄い→莫大, 牧畜→家畜, 牧場→牧畜, 牧場→農家
and 焚く→炊く as "conservative but with a real basis, not required" and 照る→晴れ, 煙突→管 and パイプ, 焦点→注目,
無限→いつまでも and 片道→切符 as "Required guards, present and correct"; the author's classes differ for nine of them (see
the independent review record), and the dispositions took no action on items 5 and 6. At recheck the consistency
reviewer called the two added guards "justified and direct" (照る→快晴) and "the right direct guard" (片寄る→ずれる). No
target card declares the reverse pair. Every RU addition is appended at the end of its list, and no EN entry is removed
or reordered. Android applies each declaration symmetrically (EN `docs/content-format.md`, lines 162–165), so no
reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (焚く F1); CLEAN at recheck for all fourteen changed cards.
- Scoped coverage: **CLEAN** after fix 1 (加熱, 焚く, 焦がす, 燃やす and 射す); the declined C9 stands as withdrawn.
- Comprehensibility: **CLEAN** after fix 1 (片寄る, 焦がす, あぶる, 加熱, 焚く, 燃やす, 射す, 照る, 煙突 and 煎る); the
  modified dispositions of C2, C3, C6, C7, C8 and C10 stand as accepted.
- Cross-file consistency: **CLEAN** throughout; the 4 restored navigation links in 4 files and the pre-existing RU-only
  navigation-file link stand.
- Quiz safety: **CLEAN** throughout; fix 1 removed four RU-added guards and added two (照る→快晴, 片寄る→ずれる), and the
  fourteen RU additions stand. This covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct
  pairs, not transitive groups.

## Limits

- The rechecks reread the changed cards and the lines needed to judge them; the unchanged cards rest on review 001, in
  which all three reviewers read all 30 cards in full. The correctness recheck states "Changed-text/EN-preservation
  recheck, not whole-batch or whole-pool quiz recertification"; the comprehensibility recheck read the fourteen changed
  cards in full; and the consistency recheck checked them "at the changed lines plus front matter and H1, not re-read
  end to end" and "did not re-read untouched cards of the batch, the 4 navigation files".
- In review 001 the consistency reviewer did not re-verify dictionary senses "beyond the JMdict numbers cited in the
  cards" and did not judge the 無限 and 休業 body glosses "against the target titles in detail". At recheck it did not
  re-verify the JMdict or jisho claims in C7 or C8, and its statement that the four dropped pairs "no longer appear at
  all" does not match the saved post-fix screen's stem-only 片道 ~ 往復 «билет» line. The comprehensibility recheck did
  not re-read raw JMdict XML or re-run the title screen and validate.py. Link parity at the fix was rerun for this
  record. Necessity classes are judgements, not measurements.
- Gramota requests at recheck were "rate-limited/inconclusive"; the Russian transitivity claims rest on ru.wiktionary
  and the original report's Kuznetsov evidence.
- The correctness recheck did not verify signatures cryptographically; no full-corpus synonym or runtime quiz audit was
  made.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fix, so its payload hashes describe the candidate `8bb7b57`, not `e290cd2`.
- Frequency and preferred register (for example «нагревание», «смещаться в одну сторону» and «полны боевого духа») were
  not certified. Online dictionaries were current observations, not pinned archives. The app's quiz selection was not
  inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
