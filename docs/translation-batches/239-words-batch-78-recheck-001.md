# Batch 239 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `39b6bd13afc5eec5371ce27cd611ce1ff581f19a` | `d966f81d76a25657d6aad60cb77733f2f9631bfd` | Initial review snapshot: the signed candidate, on `origin/full-ru-239-words-78`. |
| `8cc72168280a85ef43c00e411f8e04064a802126` | `3f346f6b836c6d535ceed9bf7ba0dc0ac1958fe5` | Fix 1 (final candidate). It covers correctness C1 and C2, consistency Q1, comprehensibility C1 to C11 (C2, C3, C4, C7 and C11 partially; C7 merged with correctness C1), the correctness コック optional and the comprehensibility optionals 虹:20, 衣食住:19 and 薄める:21. It adds one exclusion (裂く→びりびり), removes none, and adds or removes no link. Signed; on `origin/full-ru-239-words-78`. |

Fix 1 changed fourteen word files and regenerated `manifest.json` (`contentVersion` `9e254682999b1030`, 5,289 entries:
5,284 `files` + 3 images + 2 scenes; the candidate had `05ed8b9a8d8bc80c`). The intake was not refreshed; it still records
the candidate's 39 payload hashes.
- `思い付く` (lines 4 and 12; correctness C1, merged with comprehensibility C7): title and H1 «придумывать; вспоминать»
  instead of «придумывать, додумываться; вспоминать (о мысли, пришедшей на ум)», a two-segment rendering of EN :4 "hit
  upon an idea; recall". The parenthesis narrowed the recall segment against Digital Daijisen sense 2 (急用を思い付く) and
  JMdict 1589330 sense 2; bare «додумываться» (comprehensibility C7) is gone. The body keeps «додуматься до идеи». The
  correctness remedy's «додумываться» and the comprehensibility remedy's «мысль приходит на ум» were not used.
- `被せる` (line 20; correctness C2): «— Я накрыл еду крышкой и оставил её накрытой.» instead of «— Я накрыл еду
  крышкой.», carrying ておく (EN "I left a lid over the food").
- `被せる` (line 30; comprehensibility C9): «каузатива — формы «заставить или позволить сделать» — от любого глагола на
  る.» instead of «каузатива от любого глагола на る.», with the inline gloss used at お待たせしました:25.
- `裂く` (line 9; consistency Q1): びりびり appended to `quiz_exclusions`, now `[破る, 割る, 切る, 離す, 分ける,
  びりびり]`.
- `裂く` (line 42; comprehensibility C11, partially adopted): «Общее для обоих написаний значение «разрезать, вспарывать»
  не отменяет этих ограничений.» instead of «Общее значение «вспарывать» не отменяет этих ограничений.», which had
  mistranslated EN "the shared cutting-open sense". The title is unchanged.
- `コック` (lines 44–47, formerly 44–48; comprehensibility C1 and the correctness optional): «Исходная строка объединяет
  значения двух записей.» is removed; «нидерландской записи kok» becomes «слову, пришедшему из нидерландского kok»; and
  «У отдельного семейства, пришедшего из английского, есть и другие значения; эта статья выбирает из источника только
  значения «повар» и «вентиль».» becomes «У слова-оборудования, пришедшего из английского, есть и другие значения; здесь
  учат только «повар» и «кран, вентиль».» The distinction between the two words and the warning against mixing them are
  kept; the コック:39 → 蛇口 link is unchanged.
- `蛇口` (line 27; comprehensibility C2, partially adopted): «В метаданных оно отнесено к `kango` по онному первому
  элементу, как принято в этом репозитории.» instead of «Это смешанное слово, начинающееся с онного чтения, отнесено к
  категории `kango` по правилам репозитория.», following the published 王様:24 pattern. Deleting the remark was declined.
- `蕎麦` (lines 30–31; comprehensibility C3, partially adopted): «В метаданных оно отнесено к `jukujikun` — так обозначают
  чтение, присвоенное всему слову целиком. Это не делает гречиху тем же растением, что пшеница.» instead of «Категория
  `jukujikun` здесь фиксирует именно такое чтение всего слова. Она не делает гречиху тем же растением, что пшеница.»
  (precedent 時計:25).
- `カバー` (line 40; comprehensibility C4, partially adopted): «Это заимствование не переняло всех значений исходного
  английского слова.» instead of «Не переносите на это заимствование все значения английского cover.» Line 28's origin
  word «cover» is unchanged.
- `血圧` (lines 17, 19 and 20; comprehensibility C5): «измерять кровяное давление», «кровяное давление высокое», «Каждое
  утро я измеряю кровяное давление.» and «Врач сказал мне, что у меня высокое кровяное давление.» instead of the bare
  «давление», which is 圧力's whole title.
- `蓋` (line 20; comprehensibility C6): «— Крышка бутылки не открывается.» instead of «— Не могу открыть крышку бутылки.»,
  keeping the lid as the subject of intransitive 開きません.
- `複写` (lines 4 and 12; comprehensibility C8): title and H1 «копирование; воспроизведение» instead of «копирование;
  дубликат» (JMdict 1501390); the «копия» segment of コピー is still avoided.
- `街角` (line 18; comprehensibility C10): «…поверните направо на следующем углу улицы.» instead of «…на следующем
  углу.», as EN "street corner", away from 角's title «угол».
- `虹` (line 20; comprehensibility optional): «— В небе перекинулась большая радуга.» instead of «— На небе раскинулась
  большая радуга.»
- `衣食住` (line 19; comprehensibility optional): «…людям, которым трудно обеспечить себя одеждой, едой и жильём.»
  instead of «…людям, которым не хватает самого необходимого: одежды, еды и жилья.»
- `薄める` (line 21; comprehensibility optional): «Я добавил белой краски и сделал цвет светлее.» instead of «Я добавил
  белил и сделал цвет светлее.»

Comprehensibility C2 was partially adopted: deleting 蛇口:27's metadata remark was declined, for consistency with Batch
238's C238-6, because EN keeps it and published RU cards carry the same note (王様:24, 景色:38, 見本:27). C3 and C4 were
partially adopted in the same way: the 蕎麦 term is explained instead of deleted, and the カバー warning is kept but no
longer needs English polysemy. C7's «мысль приходит на ум» was declined because it would drop the recall sense that
correctness C1 established from Daijisen sense 2 and JMdict sense 2 and that EN :4 "recall" carries. C11's title change to
«раздирать на части; разрывать» was declined: «вспарывать» renders JMdict 1207730 sense 2 "to cut open (esp. the
abdomen)", which EN :4 "split open" and :16 "cut it open" carry, and the proposal would repeat the first segment and drop
that sense. The consistency optional on 蓋:24 and 蝋燭:29 ("no kanji card yet") was declined: both mirror EN and are true
at this snapshot, and a corpus-wide refresh of such statements is a later navigation task. The comprehensibility
optionals on 衣食住:17, 薬品:40–41 and 蕎麦:47 were declined: 衣食住:17 maps the title order to the kanji order for the
learner; 薬品:40–41 explains the plural title the learner sees, as EN :39 does for the English gloss; and 蕎麦:47 mirrors
EN :47, and published RU keeps such scope notes (削る:25, 見学:25). 表紙 needed no change. Whether metadata remarks like
蛇口:27 should be dropped corpus-wide is recorded in the dispositions as a follow-up, not a one-card change. The
dispositions gave the reasons (see the reconciliation table).

The coordinator's post-fix title screen of the two changed titles (`b239-postfix-screen.txt`; pool: the RU word titles)
prints three `OK` lines for guarded pairs and three stem-only `!!` lines. Its one exact shared segment is 思い付く–思い出す
«вспоминать» (思い出す «вспоминать»), guarded by the EN pair on 思い付く; 複写 meets コピー «копия; копировать» and 写す
«копировать; фотографировать» by the «копир» stem, both guarded by EN pairs; and 複写 meets 受け取る «получать; воспринимать
(как)», 感覚 «чувствительность; восприятие» and 鑑賞 «восприятие произведений искусства (просмотр, прослушивание)» by the
«воспр» stem only, unguarded. The dispositions summarise this as "the only exact-segment overlap is 思い付く «вспоминать» ~
思い出す, already guarded", with the unguarded «воспр» hits "a different word" («восприятие»). The consistency recheck found
that «вспоминать» occurs in no other title than 思い出す's, that no other RU title contains «воспроизвед», and that the
copy-family words コピー, 写す, 真似, 印刷, 書き取り and 清書 are in 複写's exclusions. The dispositions also record a corpus
grep of the RU primary checkout (words, kanji, articles) for the removed wording with no remaining quote, the only hits
being unrelated (カバー:28's origin word «cover», 鍵:29 «дубликат ключа» and the 写 reading table). They record
`tools/build_manifest.py` (5,289 files), `tools/validate.py` 0 errors, the unit tests (124) OK and the content budget
(exit 0; 5,306 entries, local ZIP 7,624,708 B) in the post-fix state.

After the rechecks the coordinator corrected two of its own summaries in the dispositions, without changing any
reviewer's verdict:
- it had first summarized correctness's initial scoped-coverage verdict as CLEAN; the original report says NEEDS FIX
  (C2), as the correctness reviewer pointed out in its recheck ("Record correction: initial scoped coverage was NEEDS FIX
  for C2, not CLEAN as summarized by the coordinator.");
- its post-fix section had first said "14 pairs" for the RU-added exclusions; the listed pairs are 13 on 10 cards (the
  candidate's 12 pairs on 9 cards plus 裂く→びりびり). The three recheck briefs carried that miscount; no recheck relied
  on it.

Net change from the candidate:
- titles and H1s of 思い付く and 複写;
- example translations in 被せる, 血圧 (two), 蓋, 街角, 虹, 衣食住 and 薄める;
- prose in 被せる (line 30), 裂く (line 42), コック (lines 44–47), 蛇口 (line 27), 蕎麦 (lines 30–31), カバー (line 40)
  and 血圧 (line 17);
- one appended exclusion (裂く→びりびり); none removed;
- no link added or removed.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`39b6bd1..8cc7216 -- words` is fourteen word files, 23 lines added and 24 removed; with `manifest.json` the commit changes
15 files, 38 lines added and 39 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs;
the correctness report states that the actual model identity is not independently verifiable, the consistency report that
the model is not verifiable from inside the session, and the comprehensibility report that the model is not verifiable
from the session prompt.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. Each recheck covered the full diff `39b6bd1..8cc7216`. No recheck raised a new finding, so there was
no fix 2.

Each reviewer appended its recheck to its own report file. The correctness section records that it read "the complete
recheck message, actual diff and all 14 changed cards in full"; the consistency section records scripted regression
checks of the changed set, front matter, titles, manifest hashes and removed wording; the comprehensibility section
records that it read every changed passage and reconciles each of its findings. Each recheck brief told the reviewer to
read it in full; only the correctness section states that it did so.

All three rechecks state that no generator was run. The correctness reviewer ran `python -X utf8 -B tools/validate.py` (0
errors, exit 0); the consistency reviewer ran `validate.py` (0 errors) and removed the `tools/__pycache__` it leaves; the
comprehensibility reviewer ran neither a generator nor `tools/validate.py`. The correctness section records HEAD
`8cc7216` with a clean tree before and after, the consistency section HEAD `8cc7216` with a clean tree before and after,
and the comprehensibility section HEAD `8cc7216` with an empty `git status --porcelain`. The recheck records include no
separate coordinator status check after the rechecks; when these records were drafted, a read-only check showed the RU
checkout on `full-ru-239-words-78` at HEAD `8cc72168280a85ef43c00e411f8e04064a802126` with
`git status --porcelain --ignored` printing nothing.

### Round 1 (`8cc7216`)

| Facet | Scope and result |
|---|---|
| Correctness | HEAD `8cc7216`, parent `39b6bd1`, clean tree before and after; read the complete recheck message, the actual diff and all 14 changed cards in full. C1 is **resolved**: 思い付く:4,12 covers JMdict 1589330 senses 1–2 and EN's idea/recall pair; "Omitting the redundant title synonym loses no distinct sense". C2 is **resolved**: 被せる:20 preserves leaving the food covered. The コック optional is **resolved**. Record correction: its initial scoped-coverage verdict was NEEDS FIX for C2, "not CLEAN as summarized by the coordinator". Regression review: 複写 matches JMdict 1501390; 蓋:20 keeps the lid as subject (JMdict 1586270 sense 1); 裂く:42 correctly identifies sense 2 as shared (JMdict 1207730); 蛇口:27 and 蕎麦:30 accurately describe their own metadata; カバー:40 adds no new lexical restriction; コック keeps both homographs (1037960, 1050310, 2862559); 血圧, 街角, 虹, 衣食住 and 薄める are "at least as accurate as wording I previously accepted, not retrospective proof that those originals were defective"; 被せる's causative gloss is correct (guidetojapanese.org causepass). Japanese body strings unchanged on all 14 cards; only the two titles and one exclusion list change metadata. Evidence: relevant full entries freshly checked in the publisher's JMdict_e archive. Validator 0 errors; no generator. Correctness **CLEAN** and scoped coverage **CLEAN**; Russian comprehensibility **UNVERIFIED** (not assigned); no regression. |
| Consistency | HEAD `8cc7216`, clean tree before and after; read-only; `validate.py` 0 errors, no generator. Q1 is **resolved** (`[破る, 割る, 切る, 離す, 分ける, びりびり]`, EN order kept; line 42 consistent with the title). The declined 蓋:24 / 蝋燭:29 optional "Stays optional, no action." The reclassification of 清書→書き取り and 蘇る→浮かぶ is "noted, no change to my analysis". Regression checks: changed set manifest.json + 14 word cards; front matter changed only in 裂く, 思い付く and 複写; title equal to H1 on all 14; manifest hashes match the 14 changed cards; 思い付く's «вспоминать» guarded against 思い出す, "No other title has this segment"; no other RU title contains «воспроизвед»; no orphaned old wording in words/ or kanji/; the 蛇口 and 蕎麦 notes consistent with 王様:24, 見本:27 and 時計:25. Consistency **CLEAN**, quiz safety **CLEAN** and cross-file integration **CLEAN**; no new findings. Limits: the wording-only edits (カバー, コック, 蓋, 薄める, 虹, 血圧, 街角, 衣食住, 被せる) checked for structure and links, not re-read in full for translation accuracy; strokes manifest hashes not re-verified. |
| Comprehensibility | HEAD `8cc7216`, empty porcelain status; read every changed passage; no generator, no `tools/validate.py`. C1, C5, C6, C8, C9 and C10 are **resolved**; C2, C3, C4, C7 and C11 are **resolved** with the partial acceptance accepted ("I do not maintain deletion" for C2, C3 and C4; "I do not maintain replacing «вспоминать»: that would hide recall" for C7; "I do not maintain the title change" for C11). The optionals 虹:20, 衣食住:19 and 薄める:21 are "resolved as applied"; 衣食住:17, 薬品:40–41 and 蕎麦:47 are **withdrawn**; 表紙 "still no finding". "Regressions: none. Shortened titles drop no Japanese point. No new title collision outside an existing exclusion." Comprehensibility **CLEAN** and scoped coverage **CLEAN**; correctness **UNVERIFIED** (not assigned). |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 思い付く's recall segment narrowed by «(о мысли, пришедшей на ум)» (medium) | **Resolved** (merged with comprehensibility C7) | `思い付く.md:4,12`; EN :4 "hit upon an idea; recall"; Digital Daijisen sense 2 (急用を思い付く); JMdict 1589330 sense 2. |
| Correctness C2: 被せる:20 loses ておく (medium; also scoped coverage) | **Resolved** | `被せる.md:20`; EN "I left a lid over the food"; Digital Daijisen 置く sense 12㋑. |
| Correctness optional: コック:44 author-facing source-row wording | **Resolved** (adopted with comprehensibility C1) | `コック.md:44–47`; JMdict 1050310 and 2862559. |
| Consistency Q1: 裂く–びりびり share the tearing sense, unguarded (low) | **Resolved** | `裂く.md:9`; びりびり «рвать в клочья; дребезжать; покалывание (током)»; JMdict 1207730 sense 1. |
| Consistency classification: 清書→書き取り and 蘇る→浮かぶ required, not conservative | **Recorded**; both pairs present | `清書.md:9`, `蘇る.md:9`; "noted, no change to my analysis" at recheck. |
| Consistency optional: 蓋:24 and 蝋燭:29 "no kanji card yet" will go stale | **Optional**; declined, no action at recheck | Both mirror EN and are true at this snapshot; a corpus-wide refresh is a later navigation task. |
| Comprehensibility C1: コック:44 translator meta (medium) | **Resolved** | `コック.md:44–47`. |
| Comprehensibility C2: 蛇口:27 unexplained `kango` and author rule (medium) | **Resolved** at recheck (partially adopted: reworded, deletion declined and not maintained) | `蛇口.md:27`; EN keeps the remark; 王様:24, 景色:38, 見本:27; the corpus-wide question is a follow-up. |
| Comprehensibility C3: 蕎麦:30 unexplained `jukujikun` (medium) | **Resolved** at recheck (partially adopted: term explained; deletion not maintained) | `蕎麦.md:30–31`; precedent 時計:25. |
| Comprehensibility C4: カバー:40 requires English polysemy (medium) | **Resolved** at recheck (partially adopted: warning kept, self-contained; deletion not maintained) | `カバー.md:40`; EN :35; line 28's origin word unchanged. |
| Comprehensibility C5: 血圧 examples show 圧力's title «давление» (medium) | **Resolved** | `血圧.md:17,19,20`; 圧力 «давление»; EN "blood pressure". |
| Comprehensibility C6: 蓋:20 adds an agent and ability (medium) | **Resolved** | `蓋.md:20`; intransitive 開きません (JMdict 1586270 sense 1). |
| Comprehensibility C7: 思い付く's title too long, bare «додумываться» (medium) | **Resolved** at recheck (merged with correctness C1; «мысль приходит на ум» declined and not maintained) | `思い付く.md:4,12`; JMdict 1589330 senses 1–2; EN "recall". |
| Comprehensibility C8: 複写 «дубликат» too narrow (low) | **Resolved** | `複写.md:4,12`; JMdict 1501390. |
| Comprehensibility C9: 被せる:29 unexplained «каузатива» (low) | **Resolved** | `被せる.md:30`; precedent お待たせしました:25. |
| Comprehensibility C10: 街角:18 drops «улицы» (low) | **Resolved** | `街角.md:18`; 角 «угол»; EN "street corner". |
| Comprehensibility C11: 裂く «вспарывать» narrow; line 42 (low) | **Resolved** at recheck (partially adopted: line 42 corrected; title change declined and not maintained) | `裂く.md:42`; JMdict 1207730 sense 2; EN :4 "split open", :16 "cut it open". |
| Comprehensibility optionals: 虹:20, 衣食住:19, 薄める:20 (located at :21) | **Resolved** (adopted) | `虹.md:20`, `衣食住.md:19`, `薄める.md:21`. |
| Comprehensibility optionals: 衣食住:17, 薬品:40–41, 蕎麦:47 | **Withdrawn** at recheck; declined | Title-order hook; plural-title note as EN :39; 蕎麦:47 mirrors EN :47 (削る:25, 見学:25). |
| Comprehensibility note: 表紙 «переплёт» | **No action** | "no change required"; "still no finding" at recheck. |

Cross-batch note: links to absent targets stay plain. Twenty-one EN link occurrences in this batch's new cards, to
nineteen targets, are absent from RU: 清書 → kanji 清 and 下書き, 複写 → kanji 複, 裏口 → kanji 裏, 被せる → kanji 被 and
着せる, 衣食住 → kanji 衣, 街角 → kanji 角, 血液 → kanji 血, kanji 液 and 液体, 血圧 → kanji 血 and 気圧, 蛇口 → kanji 蛇,
蚊 → kanji 蚊, 薬缶 → kanji 缶 and 夜間, 薄暗い → kanji 薄, 薄める → kanji 薄, and 蕎麦 → kanji 麦 and うどん. The other
written kanji without an RU kanji card, 儀, 栓, 燭, 蓋, 蕎, 蘇, 虹, 蝋, 街 and 裂, have none in EN either. Three RU-only
links, all present at the candidate and unchanged by fix 1, point to existing cards that the frozen EN cards name in plain
text or not at all: カバー:43 → 表紙, コック:39 → 蛇口 and 栓:44 → 渋滞. The pre-existing RU-only links 局 → 郵便局 and
側 → 近く/隣 on navigation files are untouched by this batch (the candidate's navigation changes are bracket-only, and fix
1 changed no navigation file). No links were held from Batch 238, and none is held from this batch. Whether metadata
remarks like 蛇口:27 («В метаданных…») should be dropped corpus-wide, and the corpus-wide refresh of "no kanji card yet"
statements as a later navigation task, are on the follow-up list recorded in the dispositions; this record does not claim
that any issue comment was posted.

## Final exclusion set

All 71 EN exclusion entries (23 lists; 衣食住, 血液, 蝋燭, コック, 虹, 薬局 and 蕎麦 have none in EN) are retained in EN
order; 10 of them lie inside the batch, and the other 61 target existing RU cards. Thirteen direct, one-sided entries are
added on ten new cards, all appended at the end of their lists, 衣食住's and 血液's on new `quiz_exclusions` lines: twelve
from the candidate (from the authoring lane as adjudicated by the coordinator) and one from fix 1 (裂く→びりびり,
consistency Q1). None was removed. The coordinator classed the candidate entries as follows:

- Required (5): 行列→番 and 行列→順番 («очередь»), 血液→血 («кровь»), 衣食住→服 («одежда») and 栓→渋滞 («пробка»).
- Conservative (7): 清書→書き取り, 被せる→履く, 蛇口→水道, 蘇る→浮かぶ, 衣食住→衣服, 衣食住→住宅 and 薬品→農薬.

The consistency reviewer classed 清書→書き取り and 蘇る→浮かぶ as required as well, the other conservative entries as
conservative, and 裂く→びりびり as "conservative-to-required"; it found no over-guard. At recheck it confirmed 裂く's list
and noted the reclassification without changing its analysis. Every RU addition is appended at the end of its list, and
no EN entry is removed or reordered. Android applies each declaration symmetrically, so no reverse declarations were
added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (思い付く C1 and 被せる C2).
- Scoped coverage: **CLEAN** after fix 1 (被せる C2); comprehensibility review scoped coverage **CLEAN** throughout.
- Comprehensibility: **CLEAN** after fix 1 (コック, 蛇口, 蕎麦, カバー, 血圧, 蓋, 思い付く, 複写, 被せる, 街角 and 裂く); C2,
  C3, C4, C7 and C11 stand as resolved with the partial dispositions accepted, and the corpus-wide question on metadata
  remarks is on the follow-up list.
- Cross-file consistency: **CLEAN** throughout; the three RU-only links (カバー:43 → 表紙, コック:39 → 蛇口 and 栓:44 →
  渋滞) and the thirteen restored navigation links in nine files stand.
- Quiz safety: **CLEAN** after fix 1 (Q1), including the 思い付く and 複写 retitles. This covers the reviewed batch and the
  directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed cards or passages and the lines needed to judge them; the comprehensibility
  recheck did not reread unchanged cards in full or re-audit the sense split behind «вспарывать», and the consistency
  recheck checked the nine wording-only edits for structure and links, not for translation accuracy. The unchanged cards
  rest on review 001, in which all three reviewers read all 30 cards in full against EN.
- The correctness recheck re-inspected the publisher's JMdict entries; its original dictionary-version, whole-pool, app
  and native-acceptance limits remain. The consistency reviewer did not consult live dictionaries and cited dictionary
  bases from the cards' entry numbers and its own knowledge; it did not rerun the unit tests or content budget or
  re-verify the strokes manifest hashes. Its necessity classes are judgements, not measurements.
- The comprehensibility review read the navigation files as link-only diffs, used JapanDict renderings of JMdict and did
  not review the intake JSON.
- Whether metadata remarks like 蛇口:27 should be dropped corpus-wide, and when "no kanji card yet" statements such as
  蓋:24 and 蝋燭:29 are refreshed, are follow-ups, not decided by this batch.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `39b6bd1`, not `8cc7216`.
- Frequency and preferred register (for example «служба», «вспарывать», «затычка», «химикаты», «полутёмный», «перекинулась»)
  were not certified. Online dictionaries were current observations, not pinned archives. The app's quiz selection was not
  inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
