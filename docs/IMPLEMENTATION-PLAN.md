# EN/RU implementation: small checkpoints before broad translation

Latest owner direction (2026-11-04): proceed with continuous background authoring against
the same frozen EN `6af98cb...`. C6/C7 device and exact media-package approval remain
ordinary RU activation/release gates, not prerequisites to translating and publishing reviewed source batches.
Use one authoring lane, at most one reviewer at a time, convenient dependency-closed batches
and frequent signed commits, pulls/reconciliation and pushes without confirmation.
The [current full-scope plan](FULL-TRANSLATION-PLAN.md#subsequent-owner-authorization-sequential-background-authoring)
records this revised order; earlier blocked observations below remain historical.

The owner's explicit 2026-11-06 restart instruction supersedes only the temporary
046 pause, not the frozen target or evidence/release protections.

## Current qualified source milestone: batch120

Batch120 adds **five complete Russian frozen N3 lessons, 昔/景/昨/晩/晴, 310 file lines**, and five
RAW-identical Japanese KanjiVG assets. Twelve existing word bodies receive one NAV-only standalone-glyph
wrapper each (一昨年, 一昨日, 今晩, 昔, 昨夜, 昨日, 晩, 晩御飯, 景色, 晴れ, 晴れる, 毎晩), planned in the
signed intake; no navigation amendment. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Candidate `274f263c4c8ca42d2fc4f6dc3efcd3eb6fb5fd37` received **two sequential completed whole
independent reviews** (never concurrent). Each read 88 whole teaching bodies (44 EN/44 CURRENT RU: five
primary pairs, 25 context pairs, 14 linked-only pairs), 81 whole official TEXT units plus one header,
all 424 typed rows, 15 proposals, five L/five A rulings, five outside LIMITS and all 12 navigation diffs
in 69 complete windows with identical opening/closing gates and zero failures. The writer first misread
review A's unrelated short native final as a no-op and launched review B; a private erratum supersedes
that wrong record, and B is not used to outvote A.

- [Review A](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-independent-review-001.json) (6472-byte report, SHA256
  `1b4dff570ecacba4bdd12d3de6ffe85539bdb58136a9a5c2f6c2c9876718d765`): **C1 CLEAN, C2 NEEDS FIX, C3 CLEAN**; findings 120-F001..F004:
  昔→借 (シャク), 景→京 (ケイ), 昨→作 (サク), 晴→青 (セイ) share an on'yomi, unsafe as unqualified reading
  negatives; N009 昨→時 ordinary **U**.
- [Review B](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-independent-review-002.json) (6072-byte report, SHA256
  `355b036da3b715c5a7bc2fe474178e213629b9a657ccc724c9cfc62f447da71c`): **C1 CLEAN, C2 UNVERIFIED, C3 CLEAN**; no findings; the same four
  directions are introductory shape comparisons only, not reading negatives.

The signed [writer adjudication](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-review-finding-adjudication-001.json) resolved F001–F004 **without
runtime mutation**: the four lines are identical to frozen EN; the app's committed reading-quiz code
(kanji-cards-android `10d98d0`, `KanjiReadings.kt` `excludedKeys`) removes every target on/kun reading
and its voicing/long-vowel/small-っ variants from wrong options, and the meaning mode uses distinct
Russian titles. One later [focused review](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-focused-review-001.json) (one different reviewer;
2366-byte report) found **F001–F004 RESOLVED**, C1/C2 CLEAN, C3 N/A, the
adjudication record accurate and no new findings; it verified committed source only, not a device or
other app versions. Original verdicts stay immutable; the batch is not retrospectively whole-CLEAN.

Review A classified ten directions S-intro, N009 昨→時 U and the four shared-reading directions as accurate
introductory shape comparisons that are **REJECTED as reading negatives** (review B: all 15 S-intro, the same
four not reading negatives); all 15 stay retained introductory/source-core comparisons (canonical author mapping
Q) and all 15 ordinary uses stay **U** (metadata retention is not guard approval). All five L and five A rulings are SUPPORTED. Outside LIMITS
(昔 vs 去年/今/古; 景 vs 景色/色; 昨 vs 昨日/昨年/今/去; 晩 vs 夕/夜/今晩/毎晩/早; 晴 vs 晴天/天気/青) are
observations, not new guards. 昔話, 風景/夜景, 昨年 and 晴天 stay plain text (no runtime word).

The [qualified source record](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-reviewed-source.json) preserves 2334 baseline runtime RAWs/tracking rows
and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2356 runtime/1478 words/424
kanji/424 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged; kanji 80 N5/166 N4/**176
N3**/2 N2; **191 N3 remain**. Strict progress: **2356 reviewed-current/two excluded reviewed
blocked-media drafts/5920 pending of 8278**. Checkpoint authority null/Ready false. Prior 082–119 U
qualifications remain unchanged; the existing RU 昨日 without a 昔 link, RU 時 distractors differing from
EN, the RU 高 distractor 本 and the earlier open observations (RU 怖/青/耳/愛/強/院/留守/怒る/少) are
outside this batch and remain open. Protected 033 WORD空 stays excluded/runtime-absent/not media. No
device/media/default/package/release authority. Continue 121+ and **ALL remaining safe frozen
levels/families**, not finite completion.

## Previous qualified source milestone: batch119

Batch119 adds **three complete Russian frozen N3 lessons, 恐/情/感, 194 file lines**, and three
RAW-identical Japanese KanjiVG assets. No existing word body changes (zero navigation wrappers, no
navigation amendment). Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/119-fear-emotion-and-feeling-kanji-independent-review-001.json) (one reviewer) of
original candidate `2211457052dd721178b9b70a2e0f9cbe8833908e` read **32 whole teaching bodies, 17 EN/15
CURRENT RU** (three primary pairs, 11 context pairs 工/心/必/忘/忙/念/怖/思/性/息/青, the linked-only
existing pair words/怖い, and two EN-only comparison bodies words/恐れる and 感情), **72 whole official
TEXT units** (15 KANJIDIC2, one radical-evidence unit, 53 JMdict, three KanjiPedia) plus one provider
header, all 419 CURRENT typed rows, nine original directions, three L/three A rulings, three outside
LIMITS, four guidance files and three RU rubrics — **53 complete windows**, 56 successful commands,
zero failures, identical opening/closing gates, zero glyph pixels and zero web pages. The original
**8605-byte stdout report**, SHA256 `18f15b9586eba1f56d9f4c45b426acc7750d4320a1130a853d08d27f9c845bfc`, byte-identical to the
reviewer's native final, is published verbatim. Actual verdicts: **C1 NEEDS FIX**, **C2 UNVERIFIED**
for ordinary active-negative quiz deployment (CLEAN for the bounded dependency and introductory
comparison scope), **C3 CLEAN** — finding **119-F001** (moderate, C1): the 感 lesson presented the
sense «заражаться, заболевать» itself as an abbreviation of 感冒, while KanjiPedia meaning ② lists
染まる。かかる separately from the abbreviation use 「感冒」の略.

A signed [pre-mutation wording freeze](translation-batches/119-fear-emotion-and-feeling-kanji-review-finding-illness-sense-amendment-freeze-001.json)
(`9387855ce81ff58d18adce37f712ee46906acd50`) authorised replacing exactly that line with a separated sense (感染) and
abbreviation (感冒 «простуда», e.g. 流感) statement, with an author-record erratum; the
[corrected candidate](translation-batches/119-fear-emotion-and-feeling-kanji-corrected-candidate-001.json) `edb0e3227123a0a39d9d4e778ce016ec7f34c2b1` changes only
kanji/感.md (typed metadata identical for all 419 rows). One later
[focused review](translation-batches/119-fear-emotion-and-feeling-kanji-independent-review-focused-001.json) (one different reviewer, never concurrent;
21 windows, 24 commands, zero failures; 2234-byte report) found **119-F001 RESOLVED**, bounded
C1/C2/C3 CLEAN, the erratum accurate, and no new findings. It is not a second whole review; the original
verdicts stay immutable and the batch is not retrospectively whole-CLEAN. The reviewer's optional notes
(an alternative 恐 title, an explicit 情/感 overlap note, readings for illustration compounds) are
explicitly not defects, recorded and not applied.

All nine directions are **S-intro** (introductory/source-core only, canonical author mapping Q); N004
情→青 and N005 情→性 are **REJECTED as セイ reading-negatives** (shape comparison only); all nine
ordinary uses stay **U** (metadata retention is not guard approval). L001 恐 and L002 情 are
supported; L003 感 was partial (now resolved by F001); all three A rulings are SUPPORTED. Outside
LIMITS (恐 vs 怖/忙/強/心; 情 vs 感/愛/事/思/心; 感 vs 情/想/思/心 and the partial 成 contact) are
observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/119-fear-emotion-and-feeling-kanji-reviewed-source.json) preserves 2340 baseline runtime
RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2346 runtime/1478 words/419 kanji/419 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**171 N3**/2 N2; **196 N3 remain**. Strict progress: **2346
reviewed-current/two excluded reviewed blocked-media drafts/5930 pending of 8278; 5932 runtime
paths absent**. Version `661906a3eef21dda`; checkpoint authority null/Ready false. Prior
082–118 U qualifications remain unchanged; the existing unlinked 恐 mention in RU 怖.md, the unlinked
青白い in RU 青.md, the RU 耳.md unlinked 恥 mention, the RU 愛 metadata kun かな.しい, the RU 強
metadata kun こわ.い, the existing unlinked 完 mention in RU 院.md, the RU 留守 wording, the existing
RU 怒る «официальный или литературный» wording for いかる and the RU 少.md distractor 名 (frozen EN 小)
are outside this batch and remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 120+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch118

Batch118 adds **five complete Russian frozen N3 lessons, 忘/忙/念/怖/性, 306 file lines**,
and five RAW-identical Japanese KanjiVG assets. Eight whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (女性→性; 忘れる→忘; 忘れ物→忘; 忙しい→忙; 怖い→怖;
性格→性; 残念→念; 男性→性), planned in the signed intake; no whole-label wrapper and no navigation
amendment. All visible prose, Japanese metadata, quiz arrays, old links, line endings and frozen
levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/118-forget-busy-wish-fear-and-nature-kanji-independent-review-001.json) (one reviewer) of
candidate `b0a47569d86cf1abdd20410d7d89e6e31f6fb21d` read **65 whole teaching bodies, 33 EN/32
CURRENT RU** (five primary pairs, 16 context pairs including the eight NAV words, 11 linked-only
existing pairs 女/男/物/暇/女の人/女の子/覚える/気分/悲しい/男の人/男, and the EN-only comparison
body 恐), **86 whole official TEXT units** (17 KANJIDIC2, one radical-evidence unit, 63 JMdict, five
KanjiPedia) plus one provider header, all 416 CURRENT typed rows, 15 original directions, five
L/five A rulings, five outside LIMITS, eight exact NAV diffs, four guidance files and three RU
rubrics — **65 complete windows**, 69 successful commands including two stdout emissions (the first
a superseded format variant differing only in the 15 N-line prefixes, with identical dispositions;
the second equal to the native final), zero failed commands, identical opening/closing gates, zero
glyph pixels and zero web pages. The canonical **8128-byte stdout report**, SHA256
`25edf72eb048eec50dd1690f4be313e3a9aef41188e9c416d7812b2ec8284379` (the reviewer's native final plus one terminal LF), is published verbatim.
Actual verdicts: **C1 CLEAN**, **C2 UNVERIFIED** (all eight NAV-only wrappers and new links verified
and no shared answer found against current titles, but ordinary active quiz safety is not confirmed
without the actual prompt/render; no defect), **C3 CLEAN**; findings none. The optional note offers
stylistic title alternatives (忙 «занятость», 怖 «страшный; бояться», 性 «природа; пол») and states
they are not defects; no change.

All 15 directions are **S-intro** (introductory/source-core only, canonical author mapping Q). All
15 ordinary all-mode uses stay **U** (metadata retention is not guard approval). All five L and five
A rulings are supported; all eight NAV changes are NAV-ONLY; outside LIMITS (忘/忙 and 亡/ボウ, 失;
急 and 夢 ボウ; 念 vs 今/思/想/意; 怖 vs 強 こわ.い and 声; 性 vs 生 セイ・ショウ, 性質 and 男/女) are
observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/118-forget-busy-wish-fear-and-nature-kanji-reviewed-source.json) preserves 2322 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2340 runtime/1478 words/416 kanji/416 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**168 N3**/2 N2; **199 N3 remain**. Strict progress: **2340
reviewed-current/two excluded reviewed blocked-media drafts/5936 pending of 8278; 5938 runtime
paths absent**. Version `00404f2955d875b4`; checkpoint authority null/Ready false. Prior 082–117
U qualifications remain unchanged; the existing unlinked 恥 mention in RU 耳.md, the RU 愛 metadata
kun かな.しい, the RU 強 metadata kun こわ.い, the existing unlinked 完 mention in RU 院.md, the RU
留守 wording, the existing RU 怒る «официальный или литературный» wording for いかる and the RU 少.md
distractor 名 (frozen EN 小) are outside this batch and remain open observations. Protected 033
WORD空 stays excluded/runtime-absent/not media. No device/media/default/package/release authority.
Continue 119+ and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch117

Batch117 adds **four complete Russian frozen N3 lessons, 息/恥/想/悲, 255 file lines**,
and four RAW-identical Japanese KanjiVG assets. Three whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (恥ずかしい→恥; 息子→息; 悲しい→悲), planned in the signed
intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata,
quiz arrays, old links, LF line endings and frozen levels of those words remain unchanged. Frozen
EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/117-breath-shame-thought-and-sorrow-kanji-independent-review-001.json) (one reviewer) of
candidate `26cf950d982dcd6c4a3cad7a95c6de8c43992641` read **42 whole teaching bodies, 23 EN/19
CURRENT RU** (four primary pairs, 11 context pairs including the three NAV words, four linked-only
existing pairs 子/娘/子供/残念, and four EN-only comparison bodies 相/非/予想/息), **72 whole
official TEXT units** (17 KANJIDIC2, one radical-evidence unit, 50 JMdict, four KanjiPedia) plus
one provider header, all 411 CURRENT typed rows, 12 original directions, four L/four A rulings,
four outside LIMITS, three exact NAV diffs, four guidance files and three RU rubrics — **55
complete windows**, 58 successful commands plus one failed stdout delivery (terminal-LF assertion,
no report printed, not credited), zero reader failures, identical opening/closing gates, zero glyph
pixels and zero web pages. The original **5629-byte stdout report**, SHA256
`b43b6e7c40bdda175189d15a00ef9e5b8ee1a0f85b0eb6d548beaa531c7e246a` (the reviewer's native final plus one terminal LF), is published verbatim.
Actual verdicts: **C1 CLEAN**, **C2 CLEAN** (three NAV-only wrappers and links verified), **C3
CLEAN**; findings none; the optional note says no correction is warranted for omitting the
literary 息 そく «сын» sense.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); the
reviewer additionally found each bounded-safe as a negative against the current directed Russian
titles only (N012 悲→怒: related emotions, but «печаль» and «гнев; сердиться» are not
interchangeable answers). All 12 ordinary all-mode uses stay **U** (metadata retention is not guard
approval). All four L and four A rulings are SUPPORTED; all three NAV changes are NAV-ONLY; outside
LIMITS (息 vs 休 and breathing kanji 吸/呼/吹; 恥 vs 取 and チ homophones; 想 vs 思/考/意 and ソウ
homophones; 悲 vs 喜/愛/悪 and ヒ homophones) are observations, not new guards and not cleared for
future options.

The [qualified source record](translation-batches/117-breath-shame-thought-and-sorrow-kanji-reviewed-source.json) preserves 2319 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2330 runtime/1478 words/411 kanji/411 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**163 N3**/2 N2; **204 N3 remain**. Strict progress: **2330
reviewed-current/two excluded reviewed blocked-media drafts/5946 pending of 8278; 5948 runtime
paths absent**. Version `61339f58dd6b72be`; checkpoint authority null/Ready false. Prior 082–116
U qualifications remain unchanged; the existing unlinked 恥 mention in RU 耳.md, the RU 愛 metadata
kun かな.しい, the existing unlinked 完 mention in RU 院.md, the RU 留守 wording, the existing RU 怒る
«официальный или литературный» wording for いかる and the RU 少.md distractor 名 (frozen EN 小) are
outside this batch and remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue
118+ and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch116

Batch116 adds **four complete Russian frozen N3 lessons, 必/怒/愛/慣, 279 file lines**,
and four RAW-identical Japanese KanjiVG assets. Five whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (必ず→必; 必要→必; 怒る→怒; 慣れる→慣; 習慣→慣), planned in
the signed intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese
metadata, quiz arrays, old links, LF line endings and frozen levels of those words remain unchanged.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/116-necessity-anger-love-and-habit-kanji-independent-review-001.json) (one reviewer) of
candidate `76f9e08f0ae41e721c72a488462698bfcb310a74` read **47 whole teaching bodies, 24 EN/23
CURRENT RU** (four primary pairs, 16 context pairs including the five NAV words, three linked-only
existing pairs 多分/習う/習, and one EN-only comparison body words/愛), **65 whole official TEXT
units** (19 KANJIDIC2, one radical-evidence unit, 41 JMdict, four KanjiPedia) plus one provider
header, all 407 CURRENT typed rows, 12 original directions, four L/four A rulings, four outside
LIMITS, five exact NAV diffs, four guidance files and three RU rubrics — **57 complete windows**, 60
successful commands, zero failures, identical opening/closing gates, zero glyph pixels and zero web
pages. The original **4605-byte stdout report**, SHA256 `67e793d889496bb9511ff189c245cce63ead1d2bcbddec913f16b62a27b84ae3`
(the reviewer's native final plus one terminal LF), is published verbatim. Actual verdicts: **C1
CLEAN**, **C2 CLEAN** (bounded; five NAV-only wrappers and links verified), **C3 CLEAN**; findings
none; optional none.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); the
reviewer additionally found each bounded-safe as a negative against the current directed Russian
titles only (N005 怒→安: «спокойный» is a contrast, not an anger synonym). All 12 ordinary all-mode
uses stay **U** (metadata retention is not guard approval). All four L and four A rulings are
SUPPORTED; all five NAV changes are NAV-ONLY; outside LIMITS (必 vs 用/定 and 心-shape kanji; 怒 vs
思/悪/好 and ド; 愛 vs 好/受/親/意/間; 慣 vs 習/常 and the カン homophones) are observations, not new
guards and not cleared for future options.

The [qualified source record](translation-batches/116-necessity-anger-love-and-habit-kanji-reviewed-source.json) preserves 2309 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2322 runtime/1478 words/407 kanji/407 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**159 N3**/2 N2; **208 N3 remain**. Strict progress: **2322
reviewed-current/two excluded reviewed blocked-media drafts/5954 pending of 8278; 5956 runtime
paths absent**. Version `b7c806b406302b76`; checkpoint authority null/Ready false. Prior 082–115
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md, the RU 留守
wording, the existing RU 怒る «официальный или литературный» wording for いかる (the new 怒 lesson
says «книжное или литературное») and the RU 少.md distractor 名 (frozen EN 小) are outside this
batch and remain open observations. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 117+ and **ALL remaining safe frozen
levels/families**, not finite completion.

## Previous qualified source milestone: batch115

Batch115 adds **five complete Russian frozen N3 lessons, 政/敗/数/散/期, 358 file lines**,
and five RAW-identical Japanese KanjiVG assets. Four whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (失敗→敗; 政治→政; 散歩→散; 数学→数), planned in the
signed intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese
metadata, quiz arrays, old links, line endings and frozen levels of those words remain unchanged.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-independent-review-001.json) (one reviewer) of
original candidate `0a7f8e29da9314a477368484eeec5ce990b806ef` read **46 whole teaching bodies, 24 EN/22
CURRENT RU** (five primary pairs, 13 context pairs including the four NAV words, four linked-only
existing pairs 失/学/歩/歩く, and two EN-only comparison bodies: words/数 and 期間), **82 whole official
TEXT units** (20 KANJIDIC2, two radical-evidence units, 55 JMdict, five KanjiPedia) plus one provider
header, all 403 CURRENT typed rows, 15 original directions, five L/five A rulings, five outside LIMITS,
four exact NAV diffs, four guidance files and three RU rubrics — **58 complete windows**, 61 successful
commands, identical opening/closing gates, zero glyph pixels and zero web pages. One earlier stdout
delivery attempt failed its own size assertion before printing anything and is recorded, not credited.
The original **10796-byte stdout report**, SHA256 `61660ded5a5168d8852accab2b70e288b9a4d0d616f19c64a754855abb59abef`, byte-identical
to the reviewer's native final, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 NEEDS FIX**
(unrestricted quiz safety UNVERIFIED; all four NAV diffs and links verified), **C3 CLEAN** — finding
**115-F001** (low): the 数 lesson left 数学 unlinked in the スウ reading row and the common-words list
although words/数学.md exists, and the author lesson record L003 wrongly claimed it was linked.

A signed [pre-mutation link freeze](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-review-finding-word-link-amendment-freeze-001.json)
(`d7478e5a3f446b2ea19ca468bbb433171342ee6f`) authorised exactly two `[数学](../words/数学.md)` wrappers
and recorded the L003 author-record erratum; the [corrected candidate](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-corrected-candidate-001.json)
`b24d52d013aa100a75e564d33a716a2fa97c0bee` changes only those two lines (typed metadata identical for
all 403 rows). One later [focused review](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-independent-review-focused-001.json) (one different
reviewer, never concurrent; 22 windows, 25 commands, zero failures; 2090-byte report) found **115-F001
RESOLVED**, bounded C1/C2/C3 CLEAN, the L003 erratum accurate, and no new findings. It is not a second
whole review; the original verdicts stay immutable and the batch is not retrospectively whole-CLEAN.
The reviewer's optional density/ちらしずし gloss note is polish, recorded and not applied.

All 15 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); N001
政→正 is **REJECTED as a reading-negative** (both read セイ/ショウ; shape comparison only); all 15
ordinary uses stay **U** (metadata retention is not guard approval). The 数 L ruling was partial
(now resolved by F001); the other four L and all five A rulings are SUPPORTED; all four NAV changes
are NAV-ONLY; outside LIMITS (政 vs 制 plus 局/御 fallback scrutiny; 敗 vs 勝/失 and weak 売; 数 vs 計;
散 vs 集, 歩 and the サン homophones; 期 vs 時/間) are observations, not new guards and not cleared
for future options.

The [qualified source record](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-reviewed-source.json) preserves 2300 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2314 runtime/1478 words/403 kanji/403 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**155 N3**/2 N2; **212 N3 remain**. Strict progress: **2314
reviewed-current/two excluded reviewed blocked-media drafts/5962 pending of 8278; 5964 runtime
paths absent**. Version `2d936b9edafe0e5e`; checkpoint authority null/Ready false. Prior 082–114
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 116+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch114

Batch114 adds **four complete Russian frozen N3 lessons, 才/支/放/断, 283 file lines**,
and four RAW-identical Japanese KanjiVG assets. Two whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (支度→支; 放送→放), planned in the signed intake; no
whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz arrays,
old links, line endings and frozen levels of those words remain unchanged. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`. The signed semantic freeze `c6b0335` stated 2300
prospective runtime objects; the actual count is 2304 (the four lessons and four strokes were
omitted from that arithmetic). This bookkeeping erratum is recorded in the candidate record; the
freeze is not rewritten.

The [actual whole independent review](translation-batches/114-talent-support-release-and-cut-kanji-independent-review-001.json) (one reviewer) of
candidate `e1d097359f260a694f80214387f5be58a74bd566` read **52 whole teaching bodies, 28 EN/24
CURRENT RU** (four primary pairs, 15 context pairs, five linked-only existing pairs and four EN-only
word comparisons: 判断, 才能, 支払う, 放れる), **89 whole official TEXT units** (21 KANJIDIC2, four
Unicode key rows, 60 JMdict, four KanjiPedia) plus one provider header, all 398 CURRENT typed rows,
12 original directions, four L/four A rulings, four outside LIMITS, two exact NAV diffs, four guidance
files and three RU rubrics — **58 complete windows**, 61 successful commands, no failures, identical
opening/closing gates, zero glyph pixels and zero web pages. The original **5868-byte
stdout report**, SHA256 `4b0bbad34a9e4b07071c659c2c3ed830f1925880d150b9bbe54fc35d89ba1c9b`, equal to the reviewer's 5867-byte
native final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 CLEAN**
(content-level: NAV wrappers, links and the 12 directions for introductory/source-core comparison
only), **C3 CLEAN**; findings none; optional none.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 12
ordinary uses stay **U** (metadata retention is not guard approval; C2 CLEAN does not upgrade them).
N004 支→友 (a friend may help) and N007 放→方 (ホウ reading contact) are noted by the reviewer. All four
L rulings are SUPPORTED and all four A clarifications SOURCE-BOUNDED; both NAV changes are NAV-ONLY;
outside LIMITS (才 vs 歳/年 age and 力 ability; 支 vs 仕 forms and 助; 放 vs 発 and the 話 homophone;
断 vs 切/否/定/判 and 立/発 homophones) are observations, not new guards and not cleared for future
options.

The [qualified source record](translation-batches/114-talent-support-release-and-cut-kanji-reviewed-source.json) preserves 2294 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2304 runtime/1478 words/398 kanji/398 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**150 N3**/2 N2; **217 N3 remain**. Strict progress: **2304
reviewed-current/two excluded reviewed blocked-media drafts/5972 pending of 8278; 5974 runtime
paths absent**. Version `6f11296688f71eb7`; checkpoint authority null/Ready false. Prior 082–113
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 115+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch113

Batch113 adds **four complete Russian frozen N3 lessons, 成/戦/戻/所, 270 file lines**,
and four RAW-identical Japanese KanjiVG assets. Eight whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (戦争→戦; 戻る→戻; 事務所, 住所, 台所, 場所, 所, 近所→所),
planned in the signed intake; no whole-label wrapper and no navigation amendment. All visible prose,
Japanese metadata, quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN
remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/113-become-war-return-and-place-kanji-independent-review-001.json) (one reviewer) of
original candidate `66316abd112bc5621fb36ccc5ad2536dc3b79d09` read **48 whole teaching bodies, 25 EN/23
CURRENT RU** (four primary pairs, 16 context pairs including the eight NAV words, three linked-only
existing word pairs 本/試合/部屋, and two EN-only comparison bodies: the かえる article and 完成),
**68 whole official TEXT units** (17 KANJIDIC2, two radical-evidence units, 45 JMdict, four KanjiPedia)
plus one provider header, all 394 CURRENT typed rows, 12 original directions, four L/four A rulings,
four outside LIMITS, eight exact NAV diffs, four guidance files and three RU rubrics — **61 complete
windows**, 64 successful commands, zero failures, identical opening/closing gates, zero glyph pixels and
zero web pages. The original **5235-byte stdout report**, SHA256
`b1e1779bdc45910ce3e420c7ae4443a5d089a5558f06f5218e661cb82475cce8`, equal to the reviewer's 5234-byte
native final plus one terminal LF, is published verbatim. Actual verdicts: **C1 NEEDS FIX**, **C2
UNVERIFIED** (all eight NAV diffs and links verified; active-negative/runtime option safety not
established), **C3 NEEDS FIX** — finding **113-F001**: the 成 lesson title and H1 «становиться;
совершаться» misdirected learners away from the core senses of 成る/成す.

A signed [pre-mutation title freeze](translation-batches/113-become-war-return-and-place-kanji-review-finding-title-gloss-amendment-freeze-001.json)
(`aa6de027cb691315c81f80e1d5e6ca0e927abd56`) authorised exactly the title and H1; the
[corrected candidate](translation-batches/113-become-war-return-and-place-kanji-corrected-candidate-001.json) `9c0d08e89b144681713397b613a5f7bda7f47619`
now reads «становиться; добиваться результата» (the reviewer's «достигать результата» adapted to avoid
overlap with the title vocabulary of 達/到). One later [focused review](translation-batches/113-become-war-return-and-place-kanji-independent-review-focused-001.json)
(one different reviewer, never concurrent; 25 windows, 28 commands, zero failures, all 394 typed titles;
2830-byte report) found **113-F001 RESOLVED**, bounded C1/C2/C3 CLEAN, the adaptation sound, and no new
findings. It is not a second whole review; the original verdicts stay immutable and the batch is not
retrospectively whole-CLEAN. The reviewer's optional 戦 «состязание» completeness note is explicitly not
a defect and is recorded, not applied.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 12
ordinary uses stay **U** (metadata retention is not guard approval). The 成 L ruling was the partial
title finding (now resolved); the other three L and all four A rulings are SUPPORTED; all eight NAV
changes are NAV-ONLY; outside LIMITS (戻 vs 帰 (strong overlap); 所/場/席 «место»; 処 vs 所; 戦 vs 試
via 試合) are observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/113-become-war-return-and-place-kanji-reviewed-source.json) preserves 2280 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2296 runtime/1478 words/394 kanji/394 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**146 N3**/2 N2; **221 N3 remain**. Strict progress: **2296
reviewed-current/two excluded reviewed blocked-media drafts/5980 pending of 8278; 5982 runtime
paths absent**. Version `cda80c756030dd78`; checkpoint authority null/Ready false. Prior 082–112
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 114+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch112

Batch112 adds **five complete Russian frozen N3 lessons, 役/彼/徒/得/御, 291 file lines**,
and five RAW-identical Japanese KanjiVG assets. Nine whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (役に立つ→役; 彼/彼ら/彼女→彼; 御主人/御礼/昼御飯/晩御飯→御;
生徒→徒; 御礼/昼御飯/晩御飯 keep their CRLF line endings), planned in the signed intake; no whole-label
wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz arrays, old links and
frozen levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/112-role-he-pupil-gain-and-honorific-kanji-independent-review-001.json) (one reviewer) of
candidate `c0c741edfef9683315ccfc0389bb17ecd7202c40` read **44 whole teaching bodies, 23 EN/21
CURRENT RU** (five primary pairs, 16 context pairs and two EN-only word comparisons: 役, 得意),
**81 whole official TEXT units** (16 KANJIDIC2, one radical-evidence unit, 59 JMdict, five KanjiPedia)
plus one provider header, all 390 CURRENT typed rows, 15 original directions, five L/five A rulings,
five outside LIMITS, nine exact NAV diffs, four guidance files and three RU rubrics — **58 complete
windows**, 61 successful commands, identical opening/closing gates, zero glyph pixels and zero web pages.
**One command failed** (a mistyped `Set-Location` directory, exit 2, no helper output, not credited);
the reviewer reran that exact window (pool 336–373) successfully. The original **6724-byte stdout
report**, SHA256 `1f77ae0ae95d9caf7ecf5fb2cbef0b74b8f696dc6daec63f1f1e05bd47de8a20`, equal to the
reviewer's 6723-byte native final plus one terminal LF, is published verbatim. Actual verdicts:
**C1 CLEAN**, **C2 UNVERIFIED** (nine NAV-only wrappers and links verified; ordinary active-negative/runtime
guard safety not established), **C3 CLEAN**; findings none. The reviewer's optional wording polish
(«передвижение пешком» for 徒, «уважительный/вежливый префикс» for 御) is explicitly not a defect and is
recorded, not applied.

All 15 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 15
ordinary uses stay **U** (metadata retention is not guard approval); N012 得→特 (トク) and N015 御→後 (ご)
are noted reading contacts. All five L and all five A rulings are SUPPORTED; all nine NAV changes are
NAV-ONLY; outside LIMITS (役 vs 務; 彼 people/third-person neighbours; 徒 vs 歩 (strong overlap); 得 vs
受/利/取/読/失; 御 vs 小 reading, 飯/礼/主 partners, 制) are observations, not new guards and not cleared
for future options.

The [qualified source record](translation-batches/112-role-he-pupil-gain-and-honorific-kanji-reviewed-source.json) preserves 2269 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2288 runtime/1478 words/390 kanji/390 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**142 N3**/2 N2; **225 N3 remain**. Strict progress: **2288
reviewed-current/two excluded reviewed blocked-media drafts/5988 pending of 8278; 5990 runtime
paths absent**. Version `5580c593a1f5bf7b`; checkpoint authority null/Ready false. Prior 082–111
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 113+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch111

Batch111 adds **four complete Russian frozen N3 lessons, 式/引/当/形, 241 file lines**,
and four RAW-identical Japanese KanjiVG assets. Twelve whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (式→式; 字引, 引き出し, 引き出す, 引く, 引っ越す→引; お弁当, 本当,
相当, 適当→当; 人形, 形→形), planned in the signed intake; no whole-label wrapper and no navigation amendment.
All visible prose, Japanese metadata, quiz arrays, old links and frozen levels of those words remain
unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/111-ceremony-pull-hit-and-shape-kanji-independent-review-001.json) (one reviewer) of
original candidate `9a8b6927678fc31002c17a133ec00fa8a338cb54` read **60 whole teaching bodies, 31 EN/29
CURRENT RU** (four primary pairs, 25 context pairs including the twelve NAV words, and two EN-only
comparison bodies: 当たる, 形式), **83 whole official TEXT units** (23 KANJIDIC2, four radical-evidence
units, 52 JMdict, four KanjiPedia) plus one provider header, all 385 CURRENT typed rows, 12 original
directions, four L/four A rulings, four outside LIMITS, 12 exact NAV diffs, four guidance files and three
RU rubrics — **63 complete windows**, 66 successful commands, zero failures, identical opening/closing
gates, zero glyph pixels and zero web pages. The original **5914-byte stdout report**, SHA256
`26af0c0751ca8c33118b029f845a5d60139c2f21afd0e72d3031e606cee76c06`, equal to the reviewer's 5913-byte
native final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 UNVERIFIED**
(all 12 NAV diffs and links verified; ordinary active-negative/fallback quiz safety not established),
**C3 NEEDS FIX** — finding **111-F001**: the sense list «формулу или установленную форму, способ» in
«Значение и происхождение» of the 式 lesson was ambiguous.

A signed [pre-mutation wording freeze](translation-batches/111-ceremony-pull-hit-and-shape-kanji-review-finding-list-wording-amendment-freeze-001.json)
(`5b286f176f08274df8ffae6bd156b5f85eb76e25`) authorised exactly that one line; the
[corrected candidate](translation-batches/111-ceremony-pull-hit-and-shape-kanji-corrected-candidate-001.json) `38b94207f9b7b950a32dd2dd1515e85c370d2c2c`
now reads «式 может обозначать церемонию, формулу, а также установленную форму или способ.» (the reviewer's
wording, adopted verbatim). One later [focused review](translation-batches/111-ceremony-pull-hit-and-shape-kanji-independent-review-focused-001.json) (one
different reviewer, never concurrent; 21 windows, 24 commands, zero failures; 1706-byte report) found
**111-F001 RESOLVED**, bounded C1/C2/C3 CLEAN, the wording accurate, and no new findings. It is not a
second whole review; the original verdicts (including C2 UNVERIFIED) stay immutable and the batch is not
retrospectively whole-CLEAN.

Ten directions are **S-intro** (introductory/source-core only, canonical author mapping Q); **N006 引→写
and N012 形→新 are U** (withheld, retained only as frozen source metadata); all 12 ordinary uses stay
**U** (metadata retention is not guard approval). All four L rulings are SUPPORTED within introductory
scope and all four A rulings SUPPORTED_BOUNDED; all 12 NAV changes are NAV-ONLY; outside LIMITS (式 vs
形/方/会; 引 vs 取/出/持; 当 vs 正/本当/真 and the 中 reading; 形 vs 体 «форма») are observations, not new
guards and not cleared for future options.

The [qualified source record](translation-batches/111-ceremony-pull-hit-and-shape-kanji-reviewed-source.json) preserves 2258 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2278 runtime/1478 words/385 kanji/385 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**137 N3**/2 N2; **230 N3 remain**. Strict progress: **2278
reviewed-current/two excluded reviewed blocked-media drafts/5998 pending of 8278; 6000 runtime
paths absent**. Version `7e0ae657bf39c8a5`; checkpoint authority null/Ready false. Prior 082–110
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 112+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch110

Batch110 adds **four complete Russian frozen N3 lessons, 市/師/席/常, 242 file lines**,
and four RAW-identical Japanese KanjiVG assets. Six whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (市/市場/市民→市, 出席/席→席, 非常に→常; all six LF-only),
planned in the signed intake; no whole-label wrapper and no navigation amendment. All visible prose,
Japanese metadata, quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN
remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. The signed semantic freeze stated a prospective
runtime count of 2266 by author miscount; the actual candidate count 2270 (2262 + four lessons + four
stroke files) is recorded in the candidate record, and the freeze is not rewritten.

The [actual whole independent review](translation-batches/110-market-teacher-seat-and-usual-kanji-independent-review-001.json) (one reviewer) of
candidate `1cf02f67cd180038532ab18e1c2c0e742a3f6ca8` read **36 whole teaching bodies, 20 EN/16
CURRENT RU** (four primary pairs, 12 context pairs and four EN-only comparison bodies: the
occupation-and-role-endings article, 教師, 欠席, 非常口), **61 whole official TEXT units** (13 KANJIDIC2,
one radical-evidence unit, 43 JMdict, four KanjiPedia) plus one provider header, all 381 CURRENT typed
rows, 12 original directions, four L/four A rulings, four outside LIMITS, six exact NAV diffs, four
guidance files and three RU rubrics — **53 complete windows**, 56 successful commands, zero failures,
identical opening/closing gates, zero glyph pixels and zero web pages. The original **5190-byte stdout
report**, SHA256 `25b8eee9a548eaf085d89d1f6383ec804faad96ac950fe54638eb9a49f1f3f18`, equal to the
reviewer's 5189-byte native final plus one terminal LF, is published verbatim. Actual verdicts: **C1
CLEAN**, **C2 CLEAN** (the reviewer states this is content-level review, not runtime quiz acceptance;
NAV diffs and links verified), **C3 CLEAN**; findings none; optional none.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 12
ordinary uses stay **U** (metadata retention is not guard approval; C2 CLEAN does not upgrade them).
All four L and all four A rulings are SUPPORTED; all six NAV changes are NAV-ONLY; outside LIMITS
(市 vs 町/場; 師 vs 先/者/教; 席 vs 座 (strong title overlap)/場/出; 常 vs 毎/日) are observations, not new
guards and not cleared for future options.

The [qualified source record](translation-batches/110-market-teacher-seat-and-usual-kanji-reviewed-source.json) preserves 2256 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2270 runtime/1478 words/381 kanji/381 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**133 N3**/2 N2; **234 N3 remain**. Strict progress: **2270
reviewed-current/two excluded reviewed blocked-media drafts/6006 pending of 8278; 6008 runtime
paths absent**. Version `c97f5998cc1e84fd`; checkpoint authority null/Ready false. Prior 082–109
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 111+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch109

Batch109 adds **two complete Russian frozen N3 lessons, 座/庭, 116 file lines**,
and two RAW-identical Japanese KanjiVG assets. Three whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (座る→座, 庭→庭, 家庭→庭; CRLF line endings kept), planned in the
signed intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata,
quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/109-seat-and-garden-kanji-independent-review-001.json) (one reviewer) of
original candidate `a38f1c4c531ae9f73757091f6e143dc778ba851e` read **20 whole teaching bodies, 10 EN/10
CURRENT RU** (two primary pairs and eight context pairs, including the three NAV words), **29 whole
official TEXT units** (9 KANJIDIC2, one radical-evidence unit, 17 JMdict, two KanjiPedia) plus one
provider header, all 377 CURRENT typed rows, six original directions, two L/two A rulings, two outside
LIMITS, three exact NAV diffs, four guidance files and three RU rubrics — **44 complete windows**, 47
successful commands, zero failures, identical opening/closing gates, zero glyph pixels and zero web
pages. The original **4623-byte stdout report**, SHA256
`af92edca08ef2493236ef04a468fd9c87a1e430271932cf782dd9f699f7a670d`, equal to the reviewer's 4622-byte native
final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 UNVERIFIED** (NAV
diffs and links verified; ordinary active-negative quiz safety not checked), **C3 NEEDS FIX** — finding
**109-F001**: the Japanese classification label 会意形声 in «Значение и происхождение» of the 座 and 庭
lessons was not glossed in Russian.

A signed [pre-mutation term-gloss freeze](translation-batches/109-seat-and-garden-kanji-review-finding-term-gloss-amendment-freeze-001.json)
(`5a01830e8d0ddf43ea8529d477e5d4af544742a1`) authorised exactly one line in each lesson; the
[corrected candidate](translation-batches/109-seat-and-garden-kanji-corrected-candidate-001.json) `3c78c3f6fd5fe93e0ce4d03e0a43b2dd0756283c`
now reads «знак 会意形声 — части соединены по смыслу, и одна из них указывает ещё и на звучание», followed by
a «Здесь …» sentence with the unchanged component explanation. The reviewer's example gloss was adopted in
substance, not verbatim. One later [focused review](translation-batches/109-seat-and-garden-kanji-independent-review-focused-001.json) (one different
reviewer, never concurrent; 22 windows, 25 commands, zero failures; 2523-byte report) found **109-F001
RESOLVED**, bounded C1/C2/C3 CLEAN, the gloss accurate, and no new findings. It is not a second whole
review; the original verdicts (including C2 UNVERIFIED) stay immutable and the batch is not
retrospectively whole-CLEAN.

All six directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all six
ordinary uses stay **U** (metadata retention is not guard approval). Both L rulings are
SUPPORTED_WITHIN_INTRODUCTORY_SOURCE and both A rulings SOURCE_SUPPORTED_BOUNDED_CLARIFICATION; all three
NAV changes are NAV-ONLY; outside LIMITS (座 vs 場 «место»/居/立/席; 庭 vs 園 «сад»/家/公) are observations,
not new guards and not cleared for future options.

The [qualified source record](translation-batches/109-seat-and-garden-kanji-reviewed-source.json) preserves 2255 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2262 runtime/1478 words/377 kanji/377 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**129 N3**/2 N2; **238 N3 remain**. Strict progress: **2262
reviewed-current/two excluded reviewed blocked-media drafts/6014 pending of 8278; 6016 runtime
paths absent**. Version `55ad396f14ddcd39`; checkpoint authority null/Ready false. Prior 082–108
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 110+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch108

Batch108 adds **four complete Russian frozen N3 lessons, 差/平/幸/幾, 230 file lines**,
and four RAW-identical Japanese KanjiVG assets. Six whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (交差点/差し上げる/差す→差, 幸せ/幸福→幸, 幾つ→幾; CRLF kept in
交差点/差す/幸福/幾つ, LF-only kept in 差し上げる/幸せ), planned in the signed intake; no whole-label wrapper
and no navigation amendment. All visible prose, Japanese metadata, quiz arrays, old links and frozen
levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/108-difference-peace-fortune-and-how-many-kanji-independent-review-001.json) (one reviewer) of
candidate `42ba5e85bc1b35c47b21a43f377ff35079e069c4` read **45 whole teaching bodies, 24 EN/21
CURRENT RU** (four primary pairs, 17 context pairs and three EN-only comparison bodies 差/平和/平等),
**85 whole official TEXT units** (19 KANJIDIC2, three radical-evidence units, 59 JMdict, four
KanjiPedia) plus one provider header, all 375 CURRENT typed rows, 12 original directions, four L/four A
rulings, four outside LIMITS, six exact NAV diffs, four guidance files and three RU rubrics — **57
complete windows**, 61 commands: 60 successful plus one stdout delivery attempt that failed its own
11000-byte size assertion (11151 bytes, exit 1, not a report) before a successful shortened retry;
identical opening/closing gates, zero glyph pixels and zero web pages. The original **7101-byte stdout
report**, SHA256 `0f4d7d14afd930e561b4debfa9d79b81a89055528b92a9f409820f4495a81ee0`, equal to the
reviewer's 7100-byte native final plus one terminal LF, is published verbatim (its Snapshot line drops
the last hex digit of the candidate hash; both gates verified the full hash). Actual verdicts: **C1
CLEAN**, **C2 UNVERIFIED** (NAV diffs and links verified; ordinary active-negative quiz/fallback
behaviour not checked), **C3 CLEAN**; findings none confirmed; optional none.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 12
ordinary uses stay **U** (metadata retention is not guard approval); the reviewer notes the real サ
reading overlap for 差→左. All four L rulings are SUPPORTED and all four A rulings
SOURCE-SUPPORTED/BOUNDED; all six NAV changes are NAV-ONLY; outside LIMITS (差 vs 間 «промежуток»/別/他/
変/交; 平 vs 和/安/世 with the Russian «мир» homonym/公; 幸 vs 福/運 «удача»/喜/楽/好/不; 幾 vs 何/多/少) are
observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/108-difference-peace-fortune-and-how-many-kanji-reviewed-source.json) preserves 2244 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2258 runtime/1478 words/375 kanji/375 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**127 N3**/2 N2; **240 N3 remain**. Strict progress: **2258
reviewed-current/two excluded reviewed blocked-media drafts/6018 pending of 8278; 6020 runtime
paths absent**. Version `2dff1832b3fa8bda`; checkpoint authority null/Ready false. Prior 082–107
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 109+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch107

Batch107 adds **two complete Russian frozen N3 lessons, 局/居, 117 file lines**,
and two RAW-identical Japanese KanjiVG assets. One whole current word body receives a
**NAV-only standalone-glyph wrapper** (郵便局→局; its CRLF line endings are kept), planned in the signed
intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz
arrays, old links and frozen levels of that word remain unchanged. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/107-bureau-and-reside-kanji-independent-review-001.json) (one reviewer) of
candidate `5cb99596bc51a01516173816ea8385fb6b89c9e9` read **20 whole teaching bodies, 11 EN/9
CURRENT RU** (two primary pairs, five context pairs, two linked existing-word pairs いる/今 and two
EN-only comparison bodies 居間/薬局), **32 whole official TEXT units** (8 KANJIDIC2, one
radical-evidence unit, 21 JMdict, two KanjiPedia) plus one provider header, all 371 CURRENT typed rows,
six original directions, two L/two A rulings, two outside LIMITS, one exact NAV diff, four guidance files
and three RU rubrics — **44 complete windows**, 47 successful commands, zero failures, identical
opening/closing gates, zero glyph pixels and zero web pages. The original **3464-byte stdout report**,
SHA256 `365abcee9fd9fbb78dbedf4af0c81d2ae1dd5a74aef1ae7d144012a61a645061`, equal to the reviewer's
3463-byte native final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**,
**C2 CLEAN** (bounded; explicitly not a runtime quiz/fallback test), **C3 CLEAN**; findings none;
optional none.

All six directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all
six ordinary uses stay **U** (metadata retention is not guard approval). Both L rulings are
SUPPORTED_WITHIN_INTRODUCTORY_SOURCE and both A rulings SOURCE_SUPPORTED_BOUNDED_CLARIFICATION; the NAV
change is NAV-ONLY; outside LIMITS (局 vs 院/官/社/館/店; 居 vs 住/在/有/存/宅/家 and the 居間–今 homophone)
are observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/107-bureau-and-reside-kanji-reviewed-source.json) preserves 2245 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2250 runtime/1478 words/371 kanji/371 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**123 N3**/2 N2; **244 N3 remain**. Strict progress: **2250
reviewed-current/two excluded reviewed blocked-media drafts/6026 pending of 8278; 6028 runtime
paths absent**. Version `64c89d457b371b9a`; checkpoint authority null/Ready false. Prior 082–106
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 108+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch106

Batch106 adds **three complete Russian frozen N3 lessons, 寒/寝/察, 161 file lines**,
and three RAW-identical Japanese KanjiVG assets. Four whole current word bodies receive
**NAV-only standalone-glyph wrappers** (寒い→寒, 寝る→寝, 寝坊→寝, 警察→察; 寒い and 寝る keep their CRLF
line endings), planned in the signed intake; no whole-label wrapper and no navigation amendment. All visible
prose, Japanese metadata, quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN
remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/106-cold-sleep-and-inspect-kanji-independent-review-001.json) (one reviewer) of
original candidate `fae77012825f8e1768c75803052476e7784e7247` read **25 whole teaching bodies, 13 EN/12
CURRENT RU** (three primary pairs, nine context pairs and one EN-only comparison body), **47 whole
official TEXT units** (7 KANJIDIC2, one radical-evidence unit, 36 JMdict, three KanjiPedia) plus
one provider header, all 369 CURRENT typed rows, nine original directions, three L/three A rulings,
three outside LIMITS, four exact NAV diffs, four guidance files and three RU rubrics —
**47 complete windows**, 50 successful commands, zero failures, identical opening/closing gates, zero
glyph pixels and zero web pages. The original **4535-byte stdout report**, SHA256
`e3133ed7689332b8216564335c1f417f32f42bb67dc99990c8581cb661ea45c7`, equal to the reviewer's 4534-byte native
final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 CLEAN** (bounded
content review; four NAV-only wrappers; runtime fallback not exercised), **C3 NEEDS FIX** — finding
**106-F001**: the 寝 lesson note «[眠る] (ねむる) сосредоточено на самом сне» was an awkward, grammatically
mismatched Russian clause.

A signed [pre-mutation wording freeze](translation-batches/106-cold-sleep-and-inspect-kanji-review-finding-wording-amendment-freeze-001.json)
(`f897efa2ae2ee2ecf1ee79f1274fec000c5f1650`) authorised exactly one line in kanji/寝.md; the
[corrected candidate](translation-batches/106-cold-sleep-and-inspect-kanji-corrected-candidate-001.json) `dc08c1aaea097d07ac905048bc703507e4c24c51`
now reads «В слове [眠る] (ねむる) акцент на самом сне, а у 寝る есть ещё значение «лежать; ложиться»». The
reviewer's replacement gloss «лечь; отправиться спать» was deliberately not adopted (the existing gloss
follows the frozen EN lying-down sense and JMdict 1360010). One later
[focused review](translation-batches/106-cold-sleep-and-inspect-kanji-independent-review-focused-001.json) (one different reviewer, never
concurrent; 21 windows, 24 commands, zero failures; 3325-byte report) found **106-F001 RESOLVED**,
bounded C1/C2/C3 CLEAN, the kept gloss acceptable, and no new findings. It is not a second whole review;
the original verdicts stay immutable and the batch is not retrospectively whole-CLEAN.

All nine directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all
nine ordinary uses stay **U** (metadata retention is not guard approval). All three L and three A
rulings are SUPPORTED and bounded; all four NAV changes NAV-ONLY; outside LIMITS (寒 vs 冷/冬, 寝 vs
夢/休/起/夜, 察 vs 見/知/思/考/判) are observations, not new guards.

The [qualified source record](translation-batches/106-cold-sleep-and-inspect-kanji-reviewed-source.json) preserves 2236 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2246 runtime/1478 words/369 kanji/369 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**121 N3**/2 N2; **246 N3 remain**. Strict progress: **2246
reviewed-current/two excluded reviewed blocked-media drafts/6030 pending of 8278; 6032 runtime
paths absent**. Version `a994f0996c3cf112`; checkpoint authority null/Ready false. Prior 082–105
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 107+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch105

Batch105 adds **four complete Russian frozen N3 lessons, 官/富/定/寄, 222 file lines**,
and four RAW-identical Japanese KanjiVG assets. Three whole current word bodies receive
**NAV-only standalone-glyph wrappers** (予定→定, 寄る→寄, 警官→官; 警官 keeps its CRLF line endings),
planned in the signed intake; no whole-label wrapper and no navigation amendment. All visible prose,
Japanese metadata, quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN
remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/105-official-wealth-decide-and-approach-kanji-independent-review-001.json) (one reviewer) of
candidate `033cba3aa08fe18287a5312d5e684f0be9abf6ac` read **36 whole teaching bodies, 19 EN/17
CURRENT RU** (four primary pairs, thirteen context pairs and two EN-only comparison bodies), **84 whole
official TEXT units** (18 KANJIDIC2, one radical-evidence unit, 61 JMdict, four KanjiPedia) plus
one provider header, all 366 CURRENT typed rows, twelve original directions, four L/four A rulings,
four outside LIMITS, three exact NAV diffs, three guidance files and three RU rubrics —
**52 complete windows**, 55 successful commands, zero failures, identical opening/closing gates, zero
glyph pixels and zero web pages. It **never ran the two assigned windows of
docs/content-format-reference.md**, although its Scope line claims all guidance ranges; that claim
is recorded as inaccurate and the review is not treated as complete for that file. The original
**4910-byte stdout report**, SHA256 `b61242a94acdb293fc6febfc98f78fcc9f4950ded5c2aff17ea07a37c5544daa`, equal to the reviewer's
4909-byte native final plus one terminal LF, is published verbatim.

A separate, later [focused supplementary review](translation-batches/105-official-wealth-decide-and-approach-kanji-supplementary-review-001.json)
(one different reviewer, never concurrent) read the whole 108-line content-format reference and the four
complete EN/RU primary pairs: **F1 CLEAN** (format-reference compliance), findings none. Its two
snapshot gates failed because the writer's own untracked first-review record tripped the helper's
untracked-path check; the reviewer reported the snapshot as UNVERIFIED, the writer's diagnostic gate
passed with only that file held aside, and the writer's capture verified every credited window
against the bound candidate text.

Actual verdicts: **C1 CLEAN**, **C2 CLEAN** (bounded content review; runtime fallback was not
exercised), **C3 CLEAN**; findings none; optional none. All twelve directions are **S-intro**
(introductory/source-core only, canonical author mapping Q); all twelve ordinary uses stay **U**
(metadata retention is not guard approval). All four L rulings and all four A rulings are SUPPORTED
and bounded; all three NAV changes NAV-ONLY; outside LIMITS (官 vs 公/員/者, 富 vs 福/多/金,
定 vs 立 shared title token and 予, 寄 vs 近/通/送/付) are observations, not new guards.

The [qualified source record](translation-batches/105-official-wealth-decide-and-approach-kanji-reviewed-source.json) preserves 2229 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2240 runtime/1478 words/366 kanji/366 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**118 N3**/2 N2; **249 N3 remain**. Strict progress: **2240
reviewed-current/two excluded reviewed blocked-media drafts/6036 pending of 8278; 6038 runtime
paths absent**. Version `d5851d6a5b302efe`; checkpoint authority null/Ready false. Prior 082–104
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 106+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch104

Batch104 adds **four complete Russian frozen N3 lessons, 客/害/宿/容, 221 file lines**,
and four RAW-identical Japanese KanjiVG assets. Three whole current word bodies receive
**NAV-only standalone-glyph wrappers** (下宿→宿, 客→客, 宿題→宿), planned in the signed intake; no
whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz arrays,
old links and frozen levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/104-guest-harm-lodging-and-contents-kanji-independent-review-001.json) (one reviewer) of
candidate `82669fd69433962ff3b9c7070da8d2222e2667c9` read **28 whole teaching bodies, 15 EN/13
CURRENT RU** (four primary pairs, nine context pairs and two EN-only comparison bodies), **70 whole
official TEXT units** (14 KANJIDIC2, one radical-evidence unit, 51 JMdict, four KanjiPedia) plus
one provider header, all 362 CURRENT typed rows, twelve original directions, four L/four A rulings,
four outside LIMITS, three exact NAV diffs, the whole guidance files and three RU rubrics —
**51 complete windows**, 54 successful commands, zero failures, identical opening/closing gates, zero
glyph pixels and zero web pages. The original **6051-byte stdout report**, SHA256
`f33af8c4b9eb7c7dd686861107308fae0c3d9982bee281b66f141e7641348377`, equal to the reviewer's
6050-byte native final plus one terminal LF, is published verbatim.

Actual verdicts: **C1 CLEAN**, **C2 CLEAN**, **C3 CLEAN**; findings none. C2 explicitly does not
certify UI fallback selection or all possible quiz compositions. All twelve directions are **S-intro**
(introductory/source-core only, canonical author mapping Q); all twelve ordinary uses stay **U**
(metadata retention is not guard approval). All four L rulings SUPPORTED within the introductory source,
all four A rulings source-supported and bounded; all three NAV changes NAV-ONLY; outside LIMITS
(客 vs 旅/店, 害 vs 悪, 宿 vs 家/宅 and 館/旅, 容 vs 内/中) are observations, not new guards. The
reviewer's optional wording note (прилагательное типа な) was not adopted: な-прилагательное is the
established term across the current Russian corpus.

The [qualified source record](translation-batches/104-guest-harm-lodging-and-contents-kanji-reviewed-source.json) preserves 2221 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2232 runtime/1478 words/362 kanji/362 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**114 N3**/2 N2; **253 N3 remain**. Strict progress: **2232
reviewed-current/two excluded reviewed blocked-media drafts/6044 pending of 8278; 6046 runtime
paths absent**. Version `172b6f6cb7374ac0`; checkpoint authority null/Ready false. Prior 082–103
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 105+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch103

Batch103 adds **four complete Russian frozen N3 lessons, 宅/守/完/実, 217 file lines**,
and four RAW-identical Japanese KanjiVG assets. Five whole current word bodies receive
**NAV-only standalone-glyph wrappers** (お宅→宅, 実に→実, 実際→実, 現実→実, 留守→守); no whole-label
wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz arrays, old links
and frozen levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/103-residence-protect-complete-and-real-kanji-independent-review-001.json) (one reviewer) of
candidate `95b1839836a0264d670a53610c97903d2c4e2de4` read **37 whole teaching bodies, 20 EN/17
CURRENT RU** (four primary pairs, 13 context pairs and three EN-only comparison bodies), **84 whole
official TEXT units** (14 KANJIDIC2, one radical-evidence unit, 65 JMdict, four KanjiPedia) plus
one provider header, all 358 CURRENT typed rows, twelve original directions, four L/four A rulings,
four dictionary clarifications, four outside LIMITS, five exact NAV diffs, the whole guidance files and
three RU rubrics — **54 complete windows**, identical opening/closing gates, zero glyph pixels and zero
web pages. The first stdout delivery failed its own terminal-LF assertion (a delivery failure, not a
reading failure); the second succeeded. The original **5053-byte stdout report**, SHA256
`0cfb31c85450e1e3df5b67c1548bac6f7c5f9a2a7c60dadc130bedd71f6d271d`, equal to the reviewer's
5052-byte native final plus one terminal LF, is published verbatim.

Actual verdicts: **C1 CLEAN**; **C2 NEEDS FIX** — all five edits are navigation-only with correct
targets, but direction **103-N010 実→完 is REJECTED** (finding **103-F001**): 完 «завершённый;
полный» can fit 実's official みち.る/content-full sense, so a learner could be marked wrong for a
defensible answer; **C3 CLEAN**. The other eleven directions are **S-intro** (introductory/source-core
only, canonical author mapping Q); all eleven ordinary uses stay **U** (metadata retention is not
guard approval). All four L and all four A rulings SUPPORTED-bounded; all five NAV changes NAV-ONLY;
outside LIMITS (宅 vs 家/住, 守 vs 助, 完 vs 終, 実 vs 真/本) are observations, not new guards. The
reviewer's optional 守 wording polish was explicitly "not required" and was not adopted.

A signed [pre-mutation distractor-amendment freeze](translation-batches/103-residence-protect-complete-and-real-kanji-review-finding-distractor-amendment-freeze-001.json)
`668c25ec91d723fd3c99d95f70447b4f200a2e0d` authorized exactly one change: removing 完 from the
distractors of kanji/実.md (now 春, 失), keeping the prose shape comparison with 完 and adding no
new direction. The [corrected candidate](translation-batches/103-residence-protect-complete-and-real-kanji-corrected-candidate-001.json)
`e1f385b741a86b1093c0666f31fe937b9e1e9d00` changes only that line plus the manifest. One
[focused independent review](translation-batches/103-residence-protect-complete-and-real-kanji-independent-review-focused-001.json) read the EN, original RU and
corrected RU 実 bodies, whole JMdict 1320800/1320810/1211490/1211510 entries, KANJIDIC2 実/完/春/失,
KanjiPedia 実/完, the current typed rows, the exact amendment and continuity, and the guidance/rubric
windows (24 complete windows, 27 successful commands, zero failures/web pages); its 2329-byte
report, SHA256 `bb75e23a449e5476e77d1eaf605e20ccbe84f3a3bbac89230baf449bd8e7ad06`, rules **F001
RESOLVED** with C1/C2/C3 CLEAN within that bounded scope and no new findings (its transcription of
the freeze hash drops one digit; the exact commit is recorded above). It is not a second whole
review; the original verdicts stay immutable and the batch is not upgraded to whole CLEAN.

The [qualified source record](translation-batches/103-residence-protect-complete-and-real-kanji-reviewed-source.json) preserves 2211 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2224 runtime/1478 words/358 kanji/358 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**110 N3**/2 N2; **257 N3 remain**. Strict progress: **2224
reviewed-current/two excluded reviewed blocked-media drafts/6052 pending of 8278; 6054 runtime
paths absent**. Version `1412246181bad4e4`; checkpoint authority null/Ready false. Prior 082–102
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 104+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch102

Batch102 adds **four complete Russian frozen N3 lessons, 婚/婦/存/対, 224 file lines**,
and four RAW-identical Japanese KanjiVG assets. Six whole current word bodies receive
**NAV-only wrappers**: five standalone-glyph wrappers (反対→対, 婦人→婦, 対する→対, 看護婦→婦,
結婚→婚) and one whole-label wrapper, 存じ in words/ご存じ.md → kanji/存.md, authorized by the signed
[pre-mutation whole-label navigation amendment](translation-batches/102-marriage-woman-existence-and-opposition-kanji-pre-mutation-whole-label-navigation-amendment-001.json).
All visible prose, Japanese metadata, quiz arrays, old links and frozen levels remain unchanged;
no new guard or removed direction. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/102-marriage-woman-existence-and-opposition-kanji-independent-review-001.json) (one reviewer) of
candidate `c199d4ca7073a14c6d8a286ba5e0c6410f30f7ae` read **48 whole teaching bodies, 25 EN/23
CURRENT RU** (four primary pairs, 19 context pairs and two EN comparison bodies), **102 whole
official TEXT units** (22 KANJIDIC2, three radical-evidence units, 73 JMdict, four KanjiPedia) plus
one provider header, all 354 CURRENT typed rows, twelve original directions, four L/four A rulings,
four dictionary clarifications, four outside LIMITS, six exact NAV diffs, the whole guidance files and
three RU rubrics — **59 complete windows**, identical opening/closing gates, zero glyph pixels, zero
web pages, 62 successful commands and zero failures. The original **10286-byte stdout report**,
SHA256 `8a52d52d8576b1407fc2439069641dae84a1e79a561d91bb748c864f48a85b76`, byte-identical to the
reviewer's native final, is published verbatim.

Actual verdicts: **C1 CLEAN**; **C2 UNVERIFIED** — all six edits are navigation-only with
correct targets and the 存じ whole-label wrapper matches the amendment, but ordinary
active-negative quiz safety is not established for any direction; **C3 NEEDS FIX** with one
minor finding, **102-F001**: kanji/婦.md called 婦人 «потенциально чувствительное», an unexplained
calque that does not tell a learner whether offensiveness or emotional sensitivity is meant. All
twelve directions are **S-intro** (introductory/source-core only, canonical author mapping Q), none
withheld; all twelve ordinary uses are **U** (metadata retention is not guard approval). All four
L rulings SUPPORTED-intro; A001/A003/A004 SUPPORTED-bounded and **A002 PARTLY SUPPORTED**: the
author capture called JMdict 2857591 «literary», but its actual marker is «dated term» (sense not
taught). All six NAV changes NAV-ONLY; outside LIMITS (婚 vs 帰/妻/夫, 婦 vs 女/妻, 存 vs 在/有/知,
対 vs 反/向) are observations, not new guards.

A signed [pre-mutation register-amendment freeze](translation-batches/102-marriage-woman-existence-and-opposition-kanji-review-finding-register-amendment-freeze-001.json)
authorized exactly two lines of kanji/婦.md: «требующее осторожности из-за возможной
оскорбительности» for the 婦人 warning, and the reviewer's optional polish «один из членов
супружеской пары» in the 夫婦 explanation. The A002 characterization is corrected in that freeze and
this acceptance record only; the frozen author record is not rewritten. The
[corrected candidate](translation-batches/102-marriage-woman-existence-and-opposition-kanji-corrected-candidate-001.json) `db62612f84b8b8e9b0e4667d184ef71a3f6abc84`
changes only those two lines plus the manifest. One
[focused independent review](translation-batches/102-marriage-woman-existence-and-opposition-kanji-independent-review-focused-001.json) read the EN, original RU and
corrected RU 婦 bodies, whole JMdict 1496670/1583640/2857591 entries, the exact amendment and
continuity, and the guidance/rubric windows (21 complete windows, 24 successful commands, zero
failures/web pages); its 2027-byte report, SHA256
`5bfcc7c4884ad2f0e27b73a35d55a9a91f635d6b0ccb7cd9e687c90be2623b0d`, rules **F001 RESOLVED**, the
polish incorporated and the A002 correction accurate, with C1/C2/C3 CLEAN within that bounded scope
and no new findings. It is not a second whole review; the original verdicts stay immutable and the
batch is not upgraded to whole CLEAN.

The [qualified source record](translation-batches/102-marriage-woman-existence-and-opposition-kanji-reviewed-source.json) preserves 2202 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2216 runtime/1478 words/354 kanji/354 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**106 N3**/2 N2; **261 N3 remain**. Strict progress: **2216
reviewed-current/two excluded reviewed blocked-media drafts/6060 pending of 8278; 6062 runtime
paths absent**. Version `f0bef69f37056089`; checkpoint authority null/Ready false. Prior 082–101
U qualifications remain unchanged; the existing RU 天/夫 stroke wording and RU 時 metadata
differences outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 103+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch101

Batch101 adds **four complete Russian frozen N3 lessons, 夢/好/妻/娘, 222 file lines**,
and four RAW-identical Japanese KanjiVG assets. Six whole current word bodies receive
**NAV-only wrappers**: five standalone-glyph wrappers (夢→夢, 好き→好, 妻→妻, 娘→娘, 格好→好)
and one whole-label wrapper, 好き in words/大好き.md → kanji/好.md, authorized by the signed
[pre-mutation whole-label navigation amendment](translation-batches/101-dream-like-wife-and-daughter-kanji-pre-mutation-whole-label-navigation-amendment-001.json).
All visible prose, Japanese metadata, quiz arrays, old links and frozen levels remain unchanged;
no new guard or removed direction. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/101-dream-like-wife-and-daughter-kanji-independent-review-001.json) (one reviewer) of
candidate `b9d1be9f20d5d50c909b891ddeae9f03e74c3a81` read **44 whole teaching bodies, 22 EN/22
CURRENT RU** (four primary pairs and 18 context pairs), **100 whole official TEXT units** (19
KANJIDIC2, two radical-evidence units, 75 JMdict, four KanjiPedia) plus one provider header, all 350
CURRENT typed rows, twelve original directions, four L/four A rulings, four outside LIMITS,
six exact NAV diffs, four whole guidance files and three RU rubrics — **57 complete windows**,
identical opening/closing gates, zero glyph pixels, zero web pages; it did not read the optional
夫.md/良.md. One report emission failed (exit 1) only because the literal lacked its terminal LF;
the next emission succeeded. The original **5466-byte stdout report**, SHA256
`632dad84d074a3666e61ca257b0f1249ecd4af3cb314e3f8523ec7800f66d4de`, is published verbatim.

Actual verdicts: **C1 CLEAN**; **C2 UNVERIFIED** — all six edits are navigation-only with
correct targets and the 好き whole-label wrapper matches the amendment, but ordinary
active-negative quiz safety is not established for any direction; **C3 NEEDS FIX** with one
finding, **101-F001**: kanji/妻.md said 夫妻 is «несколько официальное», suggesting official
status rather than JMdict 1496520's "somewhat formal" register. Ten directions are **S-intro**
(introductory/source-core only, canonical author mapping Q); **N002 夢→夜 and N004 好→妹 are U**
(withheld, retained in frozen source metadata as ordinary negatives, not guard approval); all
twelve ordinary uses are **U**. All four L rulings SUPPORTED and four A clarifications
SOURCE-SUPPORTED, BOUNDED; all six NAV changes NAV-ONLY; outside LIMITS (evening/night,
favorable/good, spouse/female, child/female/component) are observations, not new guards.

A signed [pre-mutation register-amendment freeze](translation-batches/101-dream-like-wife-and-daughter-kanji-review-finding-register-amendment-freeze-001.json)
authorized exactly one word, официальное→формальное, in that line of kanji/妻.md **and in the
identical author-written line of kanji/夫.md, accepted in batch100** (same JMdict entry, same
defect). This is a disclosed cross-batch correction of accepted text; historical batch100
records are not rewritten. The [corrected candidate](translation-batches/101-dream-like-wife-and-daughter-kanji-corrected-candidate-001.json)
`b00ac8be8e4fb98be5d202cb7daf0f9ccefb7405` changes only those two lines plus the manifest. One
[focused independent review](translation-batches/101-dream-like-wife-and-daughter-kanji-independent-review-focused-001.json) read the six
EN/original/corrected 妻/夫 bodies, the whole JMdict 1496520 entry, the exact amendment diffs,
continuity and all guidance/rubric windows (22 complete windows, 25 successful commands, zero
failures/web pages); its 1963-byte report, SHA256
`a91756930e09b7ecdc70bd37806f8c990510a84e4f15e39de42582b6025669b0`, rules **F001 RESOLVED** in
both files with C1/C2/C3 CLEAN within that bounded scope and no new findings. It is not a second
whole review; the original verdicts stay immutable and the batch is not upgraded to whole CLEAN.

The [qualified source record](translation-batches/101-dream-like-wife-and-daughter-kanji-reviewed-source.json) preserves 2193 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2208 runtime/1478 words/350 kanji/350 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**102 N3**/2 N2; **265 N3 remain**. Strict progress: **2208
reviewed-current/two excluded reviewed blocked-media drafts/6068 pending of 8278; 6070 runtime
paths absent**. Version `036029d3a8e204ca`; checkpoint authority null/Ready false. Prior 082–100
U qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 102+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch100

Batch100 adds **four complete Russian frozen N3 lessons, 変/太/夫/失, 242 file lines**,
and four RAW-identical Japanese KanjiVG assets. Thirteen whole current word bodies receive
**NAV-only standalone-glyph wrappers** (丈夫→夫, 変→変, 変える→変, 変わる→変, 変化→変, 変更→変,
大丈夫→夫, 大変→変, 太い→太, 太る→太, 太陽→太, 夫→夫, 失敗→失), planned in the signed intake;
no navigation amendment was needed. All visible prose, Japanese metadata, quiz arrays, old links
and frozen levels remain unchanged; no new guard or removed direction. Optional links to
articles/kaeru-change-replace-and-return.md, articles/ayashii-and-related-words.md, kanji/妻.md
and words/夫婦.md stay unwrapped because those files are EN-only. The signed semantic freeze
recorded a prospective count of 2196 runtime objects in arithmetic error (actual 2192+4+4=2200);
the erratum is disclosed in the candidate record, not rewritten, and has no semantic effect.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/100-change-thick-husband-and-loss-kanji-independent-review-001.json) (one reviewer) read **56 whole
teaching bodies, 30 EN/26 CURRENT RU**: four primary pairs, 22 current context pairs and
four EN-only comparisons (the two articles, kanji/妻.md, words/夫婦.md), including all thirteen
changed words; **89 whole official TEXT units** (15 KANJIDIC, two Unicode, 68 JMdict, four
visible KanjiPedia) plus one provider header; all 346 CURRENT typed rows, twelve original
directions, four L/four A rulings, four outside LIMITS, thirteen exact NAV diffs, four whole
guidance files and three RU rubrics — **63 complete windows** (the two long comparisons by
complete line unions), 66 successful terminal commands, zero failures/truncations/waits,
identical opening/closing gates, zero glyph pixels, zero web pages. The original **6278-byte
stdout report**, SHA256 `36ab037cdd776352c6238f889b5158d7abcdba7f296ed50b11304315e131ea24`,
is published verbatim with its final LF; the child/task native final is the identical
6277-byte text without the terminal LF. Its Scope line says "5 EN-only comparisons"; the bound
units are four, read in five windows (wording note, report not rewritten). No projection or
second review.

Actual verdicts: **C1 CLEAN** (four new lessons within bounded official evidence),
**C2 UNVERIFIED** — all thirteen edits are glyph-only wrappers to the matching new cards, with
unchanged prose/metadata, but ordinary active-negative quiz safety is not established for any
direction — and **C3 CLEAN** (Russian comprehension of new lessons and wrapper readability; not
native certification). Findings: none; optional: none. All **twelve directions are S-intro**
(introductory/source-core comparison only, canonical author mapping Q) with ordinary safety
**U**; metadata retention is not guard approval. All four L rulings SUPPORTED-intro and four A
clarifications SUPPORTED-bounded; all thirteen NAV changes NAV-ONLY. Outside LIMITS record
adjacency concerns, not guards: 化/変 shared «изменение» (disambiguated by the second gloss),
大/太 size domain, 主/男/大 near 夫, 死/失 and 礼/失礼. The existing RU kanji/天.md describes
夫's top stroke differently from the new 夫 lesson; this outside observation remains open,
unresolved and not adjudicated in batch100.

The [qualified source record](translation-batches/100-change-thick-husband-and-loss-kanji-reviewed-source.json) preserves 2179 other baseline runtime RAWs/tracking
rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2200 runtime/
1478 words/346 kanji/346 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji 80 N5/166 N4/**98 N3**/2 N2; **269 N3 remain**. Strict progress: **2200 reviewed-current/
two excluded reviewed blocked-media drafts/6076 pending of 8278; 6078 runtime paths absent**.
Version `0311e367192bec83`; checkpoint authority null/Ready false. Prior 082–099 U
qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 101+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch099

Batch099 adds **four complete Russian frozen N3 lessons, 在/報/増/暗, 218 file lines**,
and four RAW-identical Japanese KanjiVG assets. Four whole current word bodies receive
**NAV-only standalone-glyph wrappers** (増える→増, 天気予報→報, 暗い→暗, 電報→報),
planned in the signed intake; no navigation amendment was needed. All visible prose, Japanese metadata, quiz arrays, old links
and frozen levels remain unchanged; no new guard or removed direction. The optional 存在 and
報告 links stay unwrapped because words/存在.md and words/報告.md are EN-only. A frozen
proposal key mislabelled "prior099" (meaning prior098) is disclosed in the candidate record,
not rewritten. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/099-existence-report-increase-and-dark-kanji-independent-review-001.json) (one reviewer) read **44 whole
teaching bodies, 23 EN/21 CURRENT RU**: four primary pairs, 17 current context pairs and
two EN-only comparisons (words/報告.md, words/存在.md), including all four changed words;
**89 whole official TEXT units** (21 KANJIDIC, two Unicode, 62 JMdict, four visible
KanjiPedia) plus one provider header; all 342 CURRENT typed rows, twelve original directions,
four L/four A rulings, four outside LIMITS, four exact NAV diffs, four whole guidance files and
three RU rubrics — **57 complete windows**, 60 successful terminal commands, zero failures/
truncations/waits, identical opening/closing gates, zero glyph pixels, zero web pages. The
original **6419-byte stdout report**, SHA256
`73b5975e595210095c2bbc70653870d01ba6c71c07a83b11ea693fbbd10f7394`, is published verbatim
with its final LF; the child/task native final is the identical 6418-byte text without the
terminal LF. No projection or second review.

Actual verdicts: **C1 CLEAN** (four new lessons within bounded official evidence),
**C2 UNVERIFIED** — all four edits are standalone link wrappers to valid targets, but ordinary
active-negative quiz safety is not established for any direction, and the reviewer left
words/暗い.md whole-file raw parity unverified because the helper compared different hash
domains — and **C3 CLEAN** (Russian comprehension of new lessons and wrapper readability; not
native certification). Findings: none confirmed; optional: none. The writer's post-review
mechanical reconciliation (recorded in the review artifact, not reviewer approval) shows the
暗い working copy is exactly the CRLF projection of the LF Git blobs before and after, whose
56 lines differ only by the one wrapper. All **twelve directions are S-intro**
(introductory/source-core comparison only, canonical author mapping Q) with **ordinary U**
stated by the reviewer; metadata retention is not guard approval. All four L rulings and four
A clarifications SUPPORTED within bounded scope; all four NAV changes NAV-ONLY. Outside LIMITS
record overlap concerns, not guards: 有/在 «существовать» (inherited from EN), 報/告/伝
«сообщ-» root (introduced by Russian titles), increase/add/many/layer and dark/colour/light/
night adjacency.

The [qualified source record](translation-batches/099-existence-report-increase-and-dark-kanji-reviewed-source.json) preserves 2180 other baseline runtime RAWs/tracking
rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2192 runtime/
1478 words/342 kanji/342 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji 80 N5/166 N4/**94 N3**/2 N2; **273 N3 remain**. Strict progress: **2192 reviewed-current/
two excluded reviewed blocked-media drafts/6084 pending of 8278; 6086 runtime paths absent**.
Version `22dd52644a6a5394`; checkpoint authority null/Ready false. Prior 082–098 U
qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 100+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch098

Batch098 adds **four complete Russian frozen N3 lessons, 回/因/困/園, 226 file lines**,
and four RAW-identical Japanese KanjiVG assets. Five whole current word bodies receive
**NAV-only standalone-glyph wrappers** (公園→園, 動物園→園, 原因→因, 回る→回, 困る→困),
planned in the signed intake; no navigation amendment was needed. All visible prose,
Japanese metadata, quiz arrays, old links and frozen levels remain unchanged; no new guard
or removed direction. The optional 公演 link in kanji/園.md stays unwrapped because
words/公演.md is EN-only. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/098-turns-cause-trouble-and-garden-kanji-independent-review-001.json) (one reviewer) read **23 whole
teaching bodies, 12 EN/11 CURRENT RU**: four primary pairs, seven current context pairs and
one EN-only comparison (words/公演.md), including all five changed words; **70 whole official
TEXT units** (nine KANJIDIC, one Unicode, 56 JMdict, four visible KanjiPedia) plus one
provider header; all 338 CURRENT typed rows, twelve original directions, four L/four A
rulings, four outside LIMITS, five exact NAV diffs, four whole guidance files and three RU
rubrics — **48 complete windows**, 51 successful terminal commands, zero failures/
truncations/waits, identical opening/closing gates, zero glyph pixels, zero web pages. The
original **5824-byte stdout report**, SHA256
`ffa466864fc28c41d6f34425b2c0aaf8531d0f073e82d2fa3f558efcb30759db`, is published verbatim
with its final LF; the child/task native final is the identical 5823-byte text without the
terminal LF. No projection or second review.

Actual verdicts: **C1 CLEAN** (four new lessons within bounded official evidence),
**C2 UNVERIFIED** — all five edits precisely NAV-only and links resolve, but ordinary
active-negative quiz safety is not established for any direction — and **C3 CLEAN**
(Russian comprehension of new lessons and wrapper readability; not native certification).
Findings: none confirmed. All **twelve directions are S-intro** (introductory/source-core
comparison only, canonical author mapping Q) with **ordinary U** stated by the reviewer;
metadata retention is not guard approval. All four L rulings and four A clarifications
SUPPORTED within bounded scope; all five NAV changes NAV-ONLY. Outside LIMITS record overlap
concerns, not guards: 回 vs current 度 on «раз» (inherited from EN), 因 vs current 由 on
«причина» (introduced by Russian titles), trouble/adversity/poverty and garden/place/facility
adjacency. One optional polish suggestion (briefly gloss «онное/кунное чтение» at first use)
was not applied in 098.

The [qualified source record](translation-batches/098-turns-cause-trouble-and-garden-kanji-reviewed-source.json) preserves 2171 other baseline runtime RAWs/tracking
rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2184 runtime/
1478 words/338 kanji/338 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji 80 N5/166 N4/**90 N3**/2 N2; **277 N3 remain**. Strict progress: **2184 reviewed-current/
two excluded reviewed blocked-media drafts/6092 pending of 8278; 6094 runtime paths absent**.
Version `01b440869053b33c`; checkpoint authority null/Ready false. Prior 082–097 U
qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 099+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch097

Batch097 adds **three complete Russian frozen N3 lessons, 合/君/命, 204 file lines**,
and three RAW-identical Japanese KanjiVG assets. Ten whole current word bodies receive
**NAV-only wrappers**: nine standalone-glyph wrappers (一生懸命→命, 具合→合, 割合→合,
合う→合, 合図→合, 君→君, 場合→合, 試合→合, 都合→合) and one whole-word label wrapper,
間に合う's existing label `合う` → `../kanji/合.md`, authorized before mutation by the
[signed whole-label navigation amendment](translation-batches/097-fitting-address-and-life-kanji-pre-mutation-whole-label-navigation-amendment-001.json). All visible prose, Japanese metadata,
quiz arrays, old links and frozen levels remain unchanged; no new guard or removed direction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/097-fitting-address-and-life-kanji-independent-review-001.json) (one reviewer, replacement writer after
the original author session was lost) read **47 whole teaching bodies, 24 EN/23 CURRENT RU**:
three primary pairs, 20 current context pairs and one EN-only comparison (words/命.md), including
all ten changed words; **85 whole official TEXT units** (15 KANJIDIC, one Unicode, 66 JMdict,
three visible KanjiPedia) plus one provider header; all 334 CURRENT typed rows, nine
original directions, three L/three A rulings, three outside LIMITS, the amendment, ten exact
NAV diffs, four whole guidance files and three RU rubrics — **57 complete windows**, 60
successful terminal commands, zero failures/truncations/waits, identical opening/closing
gates, zero glyph pixels, zero web pages. The original **9432-byte stdout/native-final
report**, SHA256 `ca4acd2bb193d4f20bd0bbca0a32eebc26b5fd555ff573b1940cf4a46f738f34`, is published verbatim with its final LF; no projection or second review.

Actual verdicts: **C1 CLEAN** (three new lessons within bounded official evidence),
**C2 CLEAN for bounded scope/navigation but UNVERIFIED for ordinary active-negative quiz
safety**, **C3 CLEAN** (Russian comprehension of new lessons and wrapper readability).
Findings: none confirmed. All **nine directions are S-intro** (introductory/source-core
comparison only, canonical author mapping Q) with **ordinary U** stated by the reviewer;
metadata retention is not guard approval. All three L rulings and three A clarifications
SUPPORTED within bounded scope; all ten NAV changes CLEAN as NAV-only. Outside LIMITS record
real unresolved overlap concerns, not guards: 合's meeting sense vs current 会, 君's
master/ruler senses vs current 主, 命 vs current 生 «жизнь». One optional polish suggestion
(full readings for two short phrases in kanji/合.md notes) was not applied in 097.

The [qualified source record](translation-batches/097-fitting-address-and-life-kanji-reviewed-source.json) preserves 2160 other baseline runtime RAWs/tracking
rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2176 runtime/
1478 words/334 kanji/334 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji 80 N5/166 N4/**86 N3**/2 N2; **281 N3 remain**. Strict progress: **2176 reviewed-current/
two excluded reviewed blocked-media drafts/6100 pending of 8278; 6102 runtime paths absent**.
Version `d6d621873d0b1741`; checkpoint authority null/Ready false. Prior 082–096 U
qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 098+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch096

Four complete Russian frozen N3 lessons,**号/向/和/商,289 file lines**,
four RAW-identical KanjiVG assets and seven whole current word bodies/seven
**NAV-only standalone-glyph wrappers**:信号→号,向かう→向,向く→向,向ける→向,
向こう→向,番号→号,記号→号. All visible prose,Japanese metadata,quiz arrays,
old links and frozen levels unchanged;no new guard or removed direction.

The [actual FIRST whole review](translation-batches/096-number-direction-harmony-and-commerce-kanji-independent-review-001.json)
read46 whole teaching bodies,**24 EN/22 CURRENT RU**:four primary pairs,
18 current context pairs,two EN-only comparisons,including all seven changed words.
It read138 whole official TEXT units:20 KANJIDIC/one Unicode/113 JMdict/four
KanjiPedia,plus one whole header;331 CURRENT typed rows,12 directions,four L/
four A,seven NAV diffs,four outside LIMITS,the complete format amendment in13
logical units,four whole guidance files and three correct RU rubrics.
**65 complete windows**;zero glyph pixels,not331 whole lessons/1478 fresh guards.

Original **10799-byte stdout/native-final report**,SHA256
`75d29c9267c9488cab0457025bfc3f69dc42005805cb14440bc9f88e9859c491`,
published verbatim with final LF;no projection or second review.
73 native commands/74 returns/69 terminal successes;68 helper invocations in
distinct native shells. One closing-gate30s wait recovered by one actual
`read_powershell(delay30)`/complete exit0;gate payloads match. All65 reading
windows complete;zero failed readings/truncations.
Four delivery-size assertions14165/12115/11342/11011 before one successful
10799-byte emission. First size is measured from the actual immutable literal;
the original report lists attempts2/3/4,not rewritten by the capture audit.
Author preparation mechanics/initial format failure,one N008-qualification
capture-regex failure and a successful diagnostic classification erratum are
preserved separately,not reviewer reading failures or additional reviews.

Actual **C1 SUPPORTED introductory/source-core/C2 SUPPORTED bounded coverage/
dependencies/C3 SUPPORTED22 whole RU**,not literal CLEAN/ordinary quiz approval.
No current consequential correctable teaching/NAV/format defect established.
**All12 actual S-intro comparisons ONLY;N008和→秋 explicitly “for meaning”**.
Canonical Q is an explicit author mapping,not original report rewriting.
**ALL12 ordinary active-negative/all-sense/reading/fallback safety U**;
retained metadata/titles/parser passes do not approve guards.
All4L supported-bounded/4A supported/7NAV accepted AS NAV-ONLY;4 outside LIMITS
are not guards/global pairs. 和/秋 shared nanoriあい does not approve runtime
readings or word synonymy. 商quotient/高amount numerical affinity is not claimed
synonymy or resolved by titles. Mnemonics,source community levels,exact-form
misses and broader modern necessity-frequency/global uniqueness stay bounded.
Current kanji lacks記/数/平/禾/合/対/進;words/components are not providers.

The [format-only amendment](translation-batches/096-number-direction-harmony-and-commerce-kanji-post-initial-mutation-format-only-amendment-001.json)
is explicitly **POST initial mutation**,not retroactive premutation/EOL/semantic review.
Initial manifest2170/`47a864f666bbaf1e` passed;validator failed four schema errors,
tests/budget NOT run. Signed70ab corrects exactly eight H2 labels to canonical
`Частые слова`/`Примечания`;all other teaching/Japanese/metadata/NAV/strokes unchanged.
Original9052 freeze/proposals001/bound helpers/initial authoring001/failed checks001
immutable. CURRENT four RU bodies match002,not original001 RAWs;no EOL amendment.
Fresh002 checks pass;CURRENT4RU/7wholechangedwords/331typed read in13 author returns,
not reviewer credits.

Qualified source checkpoint: **2170 runtime/1478 words/331 kanji/331 strokes**;
words671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji80 N5/166 N4/**83 N3**/2 N2;all166 N4 included,**284 N3 remain**.
Strict statuses2170 reviewed-current/two excluded reviewed blocked-media drafts/
6106 pending of8278;6108 runtime paths absent,no partial.
Version `4db327de9b972839`;checkpoint null/Ready false.
2155 other baseline RAWs/tracking rows preserved;all1478 word metadata/quiz arrays
unchanged. Accepted-main counts require signed normal integration;fresh final
checks/public archives/signatures/four protected refs/exact-main CI/owner issue
verification are separate receipts. Runtime2170 is not2178 exported bodies.
Prior082/091/093/094/095 qualifications remain unchanged;broader ordinary modern
necessity-frequency/global uniqueness UNVERIFIED.
Protected033 WORD空 excluded-C2U/runtime-absent/not media;KANJI空 does not resolve it.
No device/media/default/package/release approval;continue097+ **ALL remaining
safe frozen families**,not full-task completion.

## Previous qualified source milestone: batch095

Four complete Russian frozen N3 lessons,**否/告/喜/声,319 file lines**,
four RAW-identical KanjiVG assets and three current word bodies/three
**NAV-only standalone-glyph wrappers**:喜び→喜,喜ぶ→喜,声→声.
Visible prose,Japanese metadata,quiz arrays,old links and frozen levels unchanged;
no new guard or removed direction. Frozen EN remains unchanged.

The [actual whole review](translation-batches/095-negation-announcement-voice-and-rejoicing-kanji-independent-review-001.json)
read31 whole teaching bodies,**17 EN/14 RU**:four primary pairs,ten CURRENT
context pairs,three EN-only comparisons,including all three changed words.
It read99 whole official TEXT units:15 KANJIDIC/two Unicode/78 JMdict/four
KanjiPedia,plus one whole header;327 CURRENT typed rows,12 directions,
four L/four A,three NAV diffs/four outside LIMITS,four whole guidance files
and three correct RU rubrics. **51 complete successful reading windows**;
zero glyph pixels,not327 whole lessons or1478 fresh word-guard judgments.

The original **10776-byte stdout/native-final report**,SHA256
`9640c96d1a064310c7e225d512f2099f57234f5176a04e0dc3ef316cfe865044`,
is published verbatim,final LF included;no projection or second review.
58 terminal returns:56 successes/two reviewer delivery-size assertions12197/11307,
not failed readings.54 helper invocations had distinct successful reader shells;
one successful size-only measurement/one exact emission are separate.
Gate payloads match;no unread window,truncation or nonterminal wait.
One author-only capture-prefix failure and explicit correction of its premature
alias-root diagnosis are preserved separately:actual report-only scripts had
empty prefixes,no filesystem access. Strict AST stdout-only audit retained;
no source/report/reviewer mutation or new review.

Actual **C1 SUPPORT within assigned source teaching/C2 qualified SUPPORT for
bounded authoring-dependencies-introductory comparisons/C3 SUPPORT within14
CURRENT RU bodies**,not literal CLEAN verdicts or ordinary quiz clearance.
No necessary learner-text fix;no reviewer-specified severity is invented.
**Eleven actual SQ introductory/source-core directions;N012声→告 U**:
whole KanjiPedia声②/告① share an utterance domain,corroborated by
JMdict1380440/1380540/1285990. A voice-only title/disclosure does not resolve it.
Canonical Q is an explicit author schema mapping,not report rewriting.
**ALL12 ordinary active-negative safety U**;metadata retention is not approval.
L001–L003/all four A/three NAV supported;L004 qualified.
Four outside LIMITS are not new guards/global pairs.
Prior082/091 U,093's27 ordinary U and094呼/吹 overlap/all nine ordinary U unchanged.
Broader ordinary suitability,necessity-frequency/global future uniqueness UNVERIFIED.
One completed/idle one-shot reviewer,not running.

Four new Markdown LF attributes checked BEFORE RAW proposal binding;all seven
actual teaching RAWs match those pre-mutation proposals,no EOL amendment invented.
CURRENT four new RU/three changed whole words/327 typed rows were freshly read
in12 author returns;reviewer reading borrows none of those credits.
Qualified source checkpoint: **2162 runtime/1478 words/327 kanji/327 strokes**;
words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/166 N4/**79 N3**/2 N2;all166 frozen N4 included,**288 N3 remain**.
Strict statuses2162 reviewed-current/two excluded reviewed blocked-media drafts/
6114 pending of8278;6116 runtime paths absent,no partial.
Version `c2909e83de70da8b`;checkpoint null/Ready false.
2151 other baseline RAWs/tracking rows preserved;all1478 word metadata/quiz arrays unchanged.
Accepted-main counts require signed normal integration;fresh final serialized
checks/public archives/signatures/four protected refs/exact-main CI/owner issue
verification have separate receipts.
Protected033 WORD空 stays excluded/C2 U/runtime-absent/not media;KANJI空 does not resolve it.
No device/media/default/package/release approval;continue096+ and **ALL remaining
safe frozen families**,not full-task completion.

## Previous qualified source milestone: batch094

Three complete Russian frozen N3 lessons,**吸/吹/呼,206 file lines**,
three RAW-identical KanjiVG assets and three current word bodies/three
**NAV-only standalone-glyph wrappers**:吸う→吸,吹く→吹,呼ぶ→呼.
No visible prose,Japanese metadata,quiz array,old link or frozen level change;
no new guard or removed direction. Frozen EN remains unchanged.

The [actual whole review/path-only public projection](translation-batches/094-absorption-breathing-and-blowing-kanji-independent-review-001.json)
cover18 whole teaching bodies,**10 EN/8 RU**:three primary pairs,five CURRENT
context pairs,two EN-only comparisons,including all three changed words.
It read92 whole official TEXT units:seven KANJIDIC/one Unicode/81 JMdict/three
KanjiPedia,plus one whole header;323 CURRENT typed rows,nine directions,
three L/three A,three NAV diffs/three outside LIMITS,the whole EOL amendment,
four whole guidance files and three correct RU rubrics.
**54 complete successful reading windows**;zero glyph pixels.
323 metadata rows are not whole lessons or1478 fresh word-guard judgments.

The original **10985-byte stdout/native-final report**,SHA256
`bdb29b4f8b1c8d1f044fa3cc542d6392c64de35124783a80271b96f617da73f6`,
is privately immutable,final LF included. Publicly only one absolute checkout
root is replaced,with separate projection bytes/hash,not original-payload identity
or a second review.59 terminal returns:57 successes/two reviewer delivery-size
assertions12722/11684,not failed readings.56 successful reader shells contained
57 helper invocations:opening gate;ranges shared one semicolon-chained shell,
not two individually observed exit codes. Gate payloads are byte-identical.
No unread window,truncation or nonterminal wait;seven author-only mechanical
failures remain preserved separately from reviewer evidence.

Actual **C1 source CLEAN/C2 bounded coverage-dependencies supported,
introductory suitability QUALIFIED ONLY/C3 Russian CLEAN**.
No necessary learner-text fix;the medium C2 negative-clearance qualification stays.
**Seven introductory/source-core Q;N006吹→呼 and N008呼→吹 U**:
whole KanjiPedia吹①/呼③ share exhalation,confirmed by JMdict1370760/1266460.
Calling-first titles/disclosure do not erase it. **ALL9 ordinary active-negative
safety U**;metadata retention is not guard approval.
L001/L002/all three A/NAV supported;L003 qualified.
Three outside LIMITS are not new guards/global pairs.
Prior082姉→妹 U,091割→利 U and093's27 ordinary active-negative U remain unchanged.
Broader ordinary suitability,necessity-frequency/global future uniqueness UNVERIFIED.
One completed/idle one-shot reviewer,not running.

The [explicit EOL amendment](translation-batches/094-absorption-breathing-and-blowing-kanji-post-initial-mutation-eol-domain-amendment-001.json)
is **POST initial runtime mutation**,before candidate checks/review.
Original001 CRLF predictions,original read receipts/signed semantic freeze and
the failed author-only RAW probe remain immutable. Three actual new LF files
already followed `eol=lf`;three NAV working CRLF bytes unchanged.
002 changes predictive RAW domains only,not learner semantics or history.
Original eleven prospective returns are not fresh002 reads;only printed typed/
NAV exact identity and RU console-LF-normalized identity carry forward.
Actual CURRENT three new RU/three changed words/323 typed rows were later freshly
read in eleven author returns. Reviewer reading borrows none of those credits.

Qualified source checkpoint: **2154 runtime/1478 words/323 kanji/323 strokes**;
words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/166 N4/**75 N3**/2 N2;all166 frozen N4 included,**292 N3 remain**.
Strict statuses2154 reviewed-current/two excluded reviewed blocked-media drafts/
6122 pending of8278;6124 runtime paths absent,no partial.
Version `012875a68bf96891`;checkpoint null/Ready false.
2145 other baseline RAWs/tracking rows preserved;all1478 word metadata/quiz arrays unchanged.
Accepted-main counts require signed normal integration;fresh final serialized
checks/public archives/signatures/four protected refs/exact-main CI/owner issue
verification have separate receipts.
Protected033 WORD空 stays excluded/C2 U/runtime-absent/not media;KANJI空 does not resolve it.
No device/media/default/package/release approval;continue095+ and **ALL remaining
safe frozen families**,not full-task completion.

## Previous qualified source milestone: batch093

Nine complete Russian frozen N3 lessons,**化/単/危/原/参/反/収/取/受,557 file lines**,
nine RAW-identical KanjiVG assets and twelve current word bodies/twelve **NAV-only
wrappers around existing standalone explanatory glyphs**:
危ない→危,危険→危,原因→原,参る→参,反対→反,取り替える→取,取る→取,
受ける→受,受付→受,変化→化,文化→化,簡単→単.
No compound/stem split,visible semantic amendment,new word,Japanese source metadata
correction or removed direction. Frozen EN and historical originals remain unchanged.
The private001取 bibliography mistake2457950（夏げ）was corrected in002 to
2451270（取り/取とり）before signed semantic freeze/runtime/candidate/review.

The [actual whole review](translation-batches/093-transformation-simplicity-danger-origin-participation-and-hand-radical-kanji-independent-review-001.json)
read96 whole teaching bodies,**51 EN/45 RU**:nine primary pairs,36 CURRENT
context pairs and six EN-only comparisons,including all twelve changed words.
It read260 official TEXT units:32 KANJIDIC/six Unicode/213 JMdict/nine KanjiPedia,
plus one whole header;320 CURRENT typed metadata rows,all27 retained directions,
nine L rulings/nine A clarifications,twelve exact NAV diffs,nine outside observations,
the citation-correction summary,four whole guidance files and three correct RU rubrics.
94 successful reading windows bind actual whole payloads and line unions.
100 commands succeeded:97 helper commands,two stdout-only size measurements,one emission.
101 tool returns include **one initial nonterminal final-gate wait** with no
terminal/reading credit;one same-shell continuation returned the complete exit0 gate.
Initial/final gates are byte-identical;no failed reviewer command or assigned reading.
Zero glyph pixels;320 typed rows are not whole lessons or1478 fresh word guards.

The **10826-byte original stdout/native-final report**,SHA256
`dcdf8435a591670a19a287f4b31da9211e3f24a8497887c480edc1103be2be10`,
is published verbatim,final LF included;no projection or second whole review.
Actual **C1 source CLEAN/C2 source consistency-dependencies-citations-introductory
contrasts QUALIFIED ONLY/C3 Russian CLEAN** remain scoped.
No assigned-text fix was requested. Two author-only capture/probe failures are
preserved separately;the corrected colon parser reads the unchanged original report.

All27 original metadata directions remain,**not27 safe negatives**.
**23 introductory/source-core Q;N005単→早,N008危→急,N022取→聞,N025受→学 U**.
Ordinary active-negative safety is **U for ALL27**.
Actual simple/danger overlaps and accept/lesson-taking context questions persist;
different titles or disclosure do not resolve them.
L001/L004–L007 and A001/A003/A005–A007 are supported;four L/four A are qualified.
All twelve NAV changes are supported. Nine outside observations are limitations,
not new guards/global pairs. Prior091割→利 active-negative U and082姉→妹
unrestricted U persist. No reverse/transitive inference,frequency or etymology claim.
Broader ordinary suitability,modern necessity-frequency/global future uniqueness
stay **UNVERIFIED**. One completed/idle one-shot reviewer,not running.

Qualified source checkpoint: **2148 runtime objects/1478 words/320 kanji/320 strokes**;
words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/166 N4/**72 N3**/2 N2;all166 frozen N4 included,**295 N3 remain**.
Strict statuses2148 reviewed-current/two excluded reviewed blocked-media drafts/
6128 pending of8278;6130 runtime paths absent,no partial.
Version `5f24829dba357164`;checkpoint authority null/Ready false.
2118 other baseline runtime RAWs/tracking rows persist;all twelve word patches are NAV-only.
These become accepted-main counts only after signed normal integration.
Fresh final serialized checks/public archives/signatures/four protected refs/
exact-main CI/owner issue verification have separate receipts.
Protected033 WORD空 remains excluded/C2 UNVERIFIED/runtime-absent/not media;
accepted077 KANJI空 does not resolve it. No device/media/default/package/release approval.
Continue094+ and **ALL remaining safe frozen families**,not task completion.

## Previous qualified source milestone: batch092

Seven complete Russian frozen N3 lessons,**加/助/努/労/務/勝/勤,468 file lines**,
seven RAW-identical KanjiVG assets and four current word bodies/four **NAV-only
wrappers around existing standalone explanatory glyphs**:
事務所→務,公務員→務,勝つ→勝,勤める→勤. No compound/stem split,visible semantic
amendment,new word,source metadata correction or removed direction.
Frozen EN,intake,premutation freeze,proposals,candidate and actual report stay unchanged.

The [actual whole review](translation-batches/092-addition-help-effort-labor-duties-victory-and-diligence-kanji-independent-review-001.json)
read49 whole teaching bodies,**27 EN/22 RU**:seven primary pairs,15 CURRENT
context pairs and five EN-only comparisons,including all four changed words.
It read148 official TEXT units:17 KANJIDIC/one Unicode/123 JMdict/seven KanjiPedia,
plus one whole header;311 CURRENT typed metadata rows,all21 original/active directions,
seven L rulings/seven A clarifications,four exact NAV diffs,seven outside observations,
four whole guidance files and three correct CURRENT RU rubrics.
66 successful reading commands/tool returns/windows bind actual whole payloads
and line unions;75 terminal commands include72 successful and **three failed
report-size assertions before emission**,not failed readings.
No assigned-reading failure,truncation or nonterminal return;zero glyph pixels.
311 typed rows are not whole lessons or1478 fresh word guards.

The **10732-byte original stdout/native-final report**,SHA256
`537de58ae7aea58e157638724332546ce38b836a509b53f124bfb4597d5b62e6`,
is published verbatim,final LF included;no projection or second whole review.
Actual **C1 source CLEAN/C2 bounded SOURCE coverage COMPLETE,introductory
contrasts QUALIFIED,evidence consistency NEEDS FIX F1/C3 Russian CLEAN**
remain scoped. The [separate ID erratum](translation-batches/092-addition-help-effort-labor-duties-victory-and-diligence-kanji-source-evidence-id-erratum-001.json)
adopts the actual reviewer's exact mapping/remedy after author reading of all five
whole bound objects:1539080勝れる/優れる;1603910勝る/優る;1171010右 better-of-two;
1609560勝ち victory;2593990勝 victory/scenic spot/win counter,not右.
The historical freeze/helper/report and original NEEDS FIX verdict remain immutable.
This is not a learner defect,new independent verdict,learner edit or guard.

All **21 directions are introductory-core Q only**. L002/A002 are qualified:
助すけ «helper» is one sense,not exhaustive;1344370 also has colloquial «woman».
Other six L/A rulings and all four NAV changes are supported.
労 care/nursing overlaps help;動く operate/work constrains勤→動;右/服/野 retain
their additional attested senses. Seven outside observations are limitations,
not new guards. Prior091割→利 active-negative U and082姉→妹 unrestricted U persist.
No reverse/transitive inference,frequency or etymology claim.
Ordinary/all-sense/fallback suitability,modern necessity-frequency/global future
uniqueness stay **UNVERIFIED**. One completed/idle reviewer,not running;
the exact original-reviewer-requested ID correction is not a second review.

Qualified source checkpoint: **2130 runtime objects/1478 words/311 kanji/311 strokes**;
words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/166 N4/**63 N3**/2 N2;all166 frozen N4 included,**304 N3 remain**.
Strict statuses2130 reviewed-current/two excluded reviewed blocked-media drafts/
6146 pending of8278;6148 runtime paths absent,no partial.
Version `8577ac7d183281ca`;checkpoint authority null/Ready false.
2112 other baseline runtime RAWs/tracking rows persist;all four word patches are NAV-only.
These become accepted-main counts only after signed normal integration.
Fresh final serialized checks/public archives/signatures/four protected refs/
exact-main CI/owner issue verification have separate receipts.
Protected033 WORD空 remains excluded/C2 UNVERIFIED/runtime-absent/not media;
accepted077 KANJI空 does not resolve it. No device/media/default/package/release approval.
Continue093+ and **ALL remaining safe frozen families**,not task completion.

## Previous qualified source milestone: batch091

Eight complete Russian frozen N3 lessons,**列/初/判/利/到/制/刻/割,584 file lines**,
eight RAW-identical KanjiVG assets and eight current word bodies/eight **NAV-only
wrappers around existing standalone explanatory glyphs**. No compound/stem split,
visible semantic amendment,new word,source metadata correction or removed direction.
Frozen EN,intake,premutation freeze,proposals,candidate and actual report remain unchanged.

The [actual whole review](translation-batches/091-rows-beginnings-judgment-benefit-arrival-regulation-carving-and-division-kanji-independent-review-001.json)
read55 whole teaching bodies,**31 EN/24 RU**:eight primary pairs,16 CURRENT
context pairs and seven EN-only comparisons,including all eight changed words.
It read224 official TEXT units:15 KANJIDIC/one Unicode/200 JMdict/eight KanjiPedia,
plus one whole header;304 CURRENT typed metadata rows,all24 original/active directions,
eight L rulings/eight A clarifications,eight exact NAV diffs,eight outside observations,
four whole guidance files and three correct CURRENT RU rubrics.
73 successful reading commands/tool returns/windows bind actual whole payloads
and line unions;80 successful terminal commands,zero failed,truncated or nonterminal.
Zero glyph pixels;304 typed rows are not whole lessons or1478 fresh word guards.

The **10976-byte original stdout/native-final report**,SHA256
`ed2d2e11d5032c906131b34057baecaa6bd8e27e6a45bea21d574b78be70c000`,
is published verbatim,final LF included;no projection or second whole review.
Actual **C1 source CLEAN/C2 bounded SOURCE dependencies/suitability QUALIFIED/
C3 Russian CLEAN** remain scoped. L003/A003 are **supported with qualification**:
paper/book-size判 isはん/ばん,notバン-only;the actual learner body already correctly
states this. Seven other L/A rulings and all eight NAV changes are supported.
One completed/idle reviewer,not running;no learner-prose fix requested.

**23 introductory semantic Qs plus091-N023割→利 U for active-negative suitability**:
whole JMdict1606800 sense3 attests割り profit/gain,intersecting利1549460.
This is actual lexical counterevidence. Historical metadata retention is **not
guard approval or activation authority**;descriptive source teaching is separate.
091-N007判→半 sharesハン,not a reading-mode guard. 到/着/達,初/始,
刻/時/秋とき and利く/聞く tasting prevent universal separation.
Eight outside observations are limitations,not new guards. Modern-shape mnemonics
are not etymology;exact-form misses are not absence/register/frequency proof.
Ordinary/all-sense/fallback suitability,modern necessity-frequency/global future
uniqueness stay **UNVERIFIED**. Prior082姉→妹's original unrestricted U is unchanged.

Qualified source checkpoint: **2116 runtime objects/1478 words/304 kanji/304 strokes**;
words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/166 N4/**56 N3**/2 N2;all166 frozen N4 included,**311 N3 remain**.
Strict statuses2116 reviewed-current/two excluded reviewed blocked-media drafts/
6160 pending of8278;6162 runtime paths absent,no partial.
Version `945eac2c7dfe171f`;checkpoint authority null/Ready false.
2092 other baseline runtime RAWs/tracking rows persist;all eight word patches are NAV-only.
These become accepted-main counts only after signed normal integration.
Fresh final serialized checks/public archives/signatures/four protected refs/
exact-main CI/owner issue verification have separate receipts.
Protected033 WORD空 remains excluded/C2 UNVERIFIED/runtime-absent/not media;
accepted077 KANJI空 does not resolve it. No device/media/default/package/release approval.
Continue092+ and **ALL remaining safe frozen families**,not task completion.

## Previous qualified source milestone: batch090

Eight complete Russian frozen N3 lessons,**乗/亡/光/全/共/具/冷/処,639 file lines**,
eight RAW-identical KanjiVG assets and15 current word bodies/15 NAV-only wrappers:
**14 standalone glyphs plus one whole existing explanatory ます-stem乗り** in
乗り換える. That exact whole-label adaptation was frozen before mutation;no
compound/Markdown splitting,visible prose change,semantic amendment,new word,
source metadata correction or removed direction. Frozen EN,intake,freeze,
proposals,candidate and actual report remain unchanged.

The [actual whole review](translation-batches/090-riding-loss-light-wholeness-sharing-tools-cold-and-places-kanji-independent-review-001.json)
read89 whole teaching bodies,**46 EN/43 RU**:eight primary pairs,35 CURRENT
context pairs and three EN-only comparisons,including all15 current changed words.
It read315 official TEXT units:27 KANJIDIC/seven Unicode/273 JMdict/eight KanjiPedia,
plus one whole header;296 CURRENT typed metadata rows,24 original/active directions,
eight L rulings/eight A clarifications,15 exact NAV diffs,eight outside observations,
four whole guidance files and three correct CURRENT RU rubrics.
91 successful reading commands/tool returns/windows bind actual whole payloads
and line unions;zero failed,truncated or nonterminal reads.
96 terminal commands comprise94 successes and two report-size assertion failures
at11853/11255 bytes **before report stdout**,not reading failures or findings.
Zero glyph pixels;296 typed rows are not whole lessons or1478 fresh word guards.

The **10451-byte original stdout/native-final report**,SHA256
`201208577346bfe00548d15673c35f80a88badd174463e596bc6df2f449619d1`,
stays private/immutable. Its **10346-byte path-only public projection**,SHA256
`5d4719570f8ce01493fc60c6f40ad8790699b288a73ca9f27c66db2f786213f6`,
replaces machine roots only;these are distinct domains,not a second review.
Actual **C1 source CLEAN/C2 bounded dependencies-NAV and introductory contrasts
QUALIFIED/C3 Russian CLEAN** remain scoped;no significant consequential scoped fix
was requested. All eight L/A rulings/clarifications are accepted boundedly.
One completed/idle reviewer,not running;no focused or second whole review.

All24 Qs are **forward introductory-core contrasts ONLY**.
090-N013共→具 and090-N017具→共 are separate independent direct judgments,not
reciprocal inference;具する accompaniment/possession prevents blanket exclusion.
具/備える,全/共 collectivity and処/外 place/removal also limit exclusion.
All readings/classifications remain;処 is **ショ**,notショウ,and処る is independently
attested despite a JMdict exact-form miss. Mnemonics are not etymology;
exact-form misses are not absence/register/frequency proof.
Eight outside observations are limitations,not guards. Ordinary/all-sense/
reading-mode/fallback suitability,modern necessity-frequency/global current-future
uniqueness stay **UNVERIFIED**. Prior word guards and082姉→妹's unrestricted U persist.

Qualified source checkpoint: **2100 runtime objects/1478 words/296 kanji/296 strokes**;
words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/166 N4/**48 N3**/2 N2;all166 frozen N4 included,**319 N3 remain**.
Strict statuses2100 reviewed-current/two excluded reviewed blocked-media drafts/
6176 pending of8278;6178 runtime paths absent,no partial.
Version `eff88314bda21342`;checkpoint authority null/Ready false.
2069 other baseline runtime RAWs/tracking rows persist;all15 word patches are NAV-only.
These become accepted-main counts only after signed normal integration.
Fresh final serialized checks/public archives/signatures/four protected refs/
exact-main CI/owner issue verification have separate receipts.
Protected033 WORD空 remains excluded/C2 UNVERIFIED/runtime-absent/not media;
accepted077 KANJI空 does not resolve it. No device/media/default/package/release approval.
Continue091+ and **ALL remaining safe frozen families**,not task completion.

## Previous qualified source milestone: batch089

Seven complete Russian frozen N3 lessons,**余/便/係/信/備/働/優,513 file lines**,
seven RAW-identical KanjiVG assets and nine existing word bodies/nine NAV-only
wrappers. No new word,word semantic amendment,source metadata correction or
removed direction;frozen EN,intake,freeze,proposals,candidate/report stay unchanged.

The [actual whole review](translation-batches/089-surplus-convenience-connection-trust-preparation-work-and-kindness-kanji-independent-review-001.json)
read67 whole teaching bodies,**36 EN/31 RU**:seven primary pairs,24 CURRENT
context pairs and five EN-only comparisons,including all nine changed words.
It read238 official TEXT units:24 KANJIDIC/one Unicode/206 JMdict/seven KanjiPedia,
plus one whole header;288 CURRENT typed metadata rows,21 original/active
directions,seven L rulings/seven A clarifications,nine exact NAV diffs/wrappers,
seven outside observations,four whole guidance files and three correct CURRENT RU rubrics.
77 successful reading commands/tool returns/windows bind actual whole payloads
and line unions;no failed/truncated reads. All80 terminal commands succeeded.
82 actual tool returns include two nonterminal final-gate returns not credited as
terminal success;one terminal follow-up completed that gate.
Zero glyph pixels;288 metadata rows are not whole lessons or1478 fresh word guards.

One successful **10716-byte original stdout/native-final report**,SHA256
`4054652327a33d17e27f3d6ab9f1636f591ad76aedfd7caf062f6c9e4c417d44`,
requires no path projection/rewrite. Actual **C1 source PASS/C2 bounded
dependencies-NAV and introductory contrasts QUALIFIED/C3 Russian PASS** remain
scoped;no significant consequential source/Russian fix was requested.
All seven L/A rulings/clarifications are accepted boundedly.
One completed/idle reviewer,not running;no focused or second whole review.

All21 Qs are **forward introductory-core contrasts ONLY**.
089-N016働→動 explicitly retains function/work/movement and稼働/稼動 overlap,
not all-sense/fallback-safe wrong-answer approval. 係る work/result,便 stool/body
and信 credit/borrowing also forbid blanket disjointness.
Seven outside observations are not guards. Ordinary/all-sense/read-mode/fallback
suitability,modern necessity-frequency/global current-future uniqueness remain
UNVERIFIED. Existing word guards and082姉→妹's original unrestricted U stay unchanged.
系/憂 remain metadata/visible-shape components,not invented frozen EN lessons.

Qualified source checkpoint: **2084 runtime objects/1478 words/288 kanji/288 strokes**;
words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/166 N4/**40 N3**/2 N2;all166 frozen N4 included,**327 N3 remain**.
Strict statuses2084 reviewed-current/two excluded reviewed blocked-media drafts/
6192 pending of8278;6194 runtime paths absent,no partial.
Version `744d39ac52c0452b`;checkpoint authority null/Ready false.
2061 other baseline runtime RAWs/tracking rows persist;all nine word patches are NAV-only.
These become accepted-main counts only after signed normal integration.
Fresh final serialized checks/public archives/signatures/four protected refs/
exact-main CI/owner issue verification have separate receipts.
Protected033 WORD空 remains excluded/C2 UNVERIFIED/runtime-absent/not media;
accepted077 KANJI空 does not resolve it. No device/media/default/package/release approval.
Continue090+ and **ALL remaining safe frozen families**,not task completion.

## Previous qualified source milestone: batch088

Seven complete Russian frozen N3 kanji lessons,**倒/候/値/偶/偉/側/例,
497 corrected file lines**,seven RAW-identical KanjiVG assets and seven existing
word bodies/seven NAV-only wrappers. No new word,word semantic amendment,
source metadata correction or removed direction. Frozen EN remains unchanged.
Original493-line proposals,intake,freezes,candidates and actual reports are immutable.

The [actual whole review](translation-batches/088-examples-falling-weather-values-chance-and-sides-kanji-independent-review-001.json)
read56 whole teaching bodies,**33 EN/23 RU**:seven primary pairs,16 current context
pairs and10 EN-only comparisons,including all seven changed word bodies.
It read251 official TEXT units:22 KANJIDIC/one Unicode/221 JMdict/seven KanjiPedia,
plus one whole header;281 CURRENT whole metadata rows,21 historical/active directions,
seven L rulings/seven A additions,seven exact NAV diffs/wrappers,seven outside
observations,four whole guidance files and three correct CURRENT RU rubrics.
64 successful reader tool returns/72 windows bind whole actual payloads/line unions.
Two truncated bundles were not credited and were reread completely.
Zero glyph pixels;281 metadata rows are not whole lessons or1478 fresh word guards.

Original **C1 NEEDS FIX F1/C2 textual dependency-NAV PASS with21 qualified core Qs/
C3 QUALIFIED** remain unchanged. Two successful stdout deliveries are historical:
earlier10582 bytes with three bell path escapes/warning;reviewer-corrected10681 bytes,
SHA256 `a494aa0cada1a9a3a4028ea0ae9c50224d90ffa72a02e013b2e20c52652f4285`,
exactly match native final. This is one whole review,not two or failed pre-emission reports.
F1 concerns missing formal/literary labels for standalone あたい price/worth.
The exact four-line usage correction was frozen and signed before runtime mutation.

The [actual focused review](translation-batches/088-examples-falling-weather-values-chance-and-sides-kanji-independent-review-focused-002.json),
8755 bytes,SHA256 `9f35cb7311cb038f061dd0e2e4abbe46e84b02663b927ae535529c18809feed0`,
resolves **F1 only**,without blanket-formal mathematics/computing.
It read five whole teaching bodies,2 EN/3 RU,and eight official TEXT units,
six JMdict/one KANJIDIC/one KanjiPedia;25 credited windows,zero pixels.
One oversized guidance return received no credit;both windows were reread fully.
Bounded C1/C3 usage-gap resolution and C2 amendment continuity resolve the
F1-dependent L003/A003 qualification,not original report verdicts/whole-batch CLEAN.
Both one-shot reviewers are completed,not actually running.

All21 original Qs keep **original qualified forward introductory-core scope only**.
Five 値 endpoint hashes change without semantic expansion/qualifier weakening;
the focus is not five/21 fresh pair judgments or281 fresh semantic rows.
倒→側,候→使,偶→値 and側→内/右/左 retain actual overlap limits.
Seven outside observations are not guards. Ordinary/all-sense/read-mode/fallback
safety,modern necessity-frequency/global future uniqueness remain UNVERIFIED.
Prior word-guard support/scope/identity and082姉→妹's unrestricted U are unchanged.

Qualified source checkpoint: **2070 runtime objects/1478 words/281 kanji/281 strokes**;
words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/166 N4/**33 N3**/2 N2;all166 frozen N4 included,**334 N3 remain**.
Strict statuses2070 reviewed-current/two excluded reviewed blocked-media drafts/
6206 pending of8278;6208 runtime paths absent,no partial.
Version `c3357a2913cdfd26`;checkpoint authority null/Ready false.
2049 other baseline runtime RAWs/tracking rows persist;all seven word patches are NAV-only.
These become accepted-main counts only after signed normal integration.
Fresh final serialized checks/public archives/signatures/four protected refs/
exact-main CI/owner issue verification have separate receipts.
Protected033 WORD空 remains excluded/C2 UNVERIFIED/runtime-absent/not media;
accepted077 KANJI空 does not resolve it. No device/media/default/package/release approval.
Continue089+ and **ALL remaining safe frozen families**,not task completion.

## Previous qualified source milestone: batch087

The eighty-seventh full-target batch adds **seven complete Russian frozen N3 kanji
lessons,他/付/件/任/伝/似/位,473 file lines**,and seven RAW-identical KanjiVG assets.
Ten existing word bodies receive10 **navigation-only wrappers**;
no new word,word semantic amendment or source-directed metadata correction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`;
signed intake,premutation freeze,proposals and candidate remain immutable.

The [actual whole review](translation-batches/087-otherness-attachment-duties-and-position-kanji-independent-review-001.json)
read **56 whole teaching bodies**,30 EN/26 RU:seven primary EN/RU pairs,
19 current context pairs and four whole EN-only comparisons.
All10 changed word bodies are included,not additional bodies.
It read185 whole official TEXT units:16 KANJIDIC,one Unicode,161 ordered
JMdict and seven visible KanjiPedia entries;one whole provider header is additional.
Zero glyph pixel views;historical inline glyphs stay UNINSPECTED.
It read274 current whole typed metadata rows,21 historical/active directions,
seven lesson rulings/seven separate clarifications,10 exact NAV diffs/10 wrappers,
seven outside observations,four whole guidance files and three correct CURRENT RU rubrics.
70 actual successful reader commands/windows bind entire payloads/complete
line unions,not markers alone;metadata rows are not274 whole lessons or1478 fresh guards.

One actual whole review produced one successful **10792-byte stdout/native final**,
SHA256 `af4deffc7c9b21193220e3e5d6e78db073cdb45821bedacab35817bc5fab0dd2`.
Original public bytes are unchanged,no path projection needed.
Two earlier size assertions failed before report emission,not earlier delivered
reports/semantic reviews,and credit no reading.
The final gate's initial nonterminal return is not success;its actual successful
`read_powershell` completion is separately bound:76 tool returns,
75 terminal commands/73 successful,two size failures.
The one-shot reviewer is completed,not actually running.
The original report prints only the scope-binding SHA256,not separate serialized
pool/evidence hashes. Author extraction separately binds those artifacts and
actual gates/all274 returned rows,without fabricating verbatim reviewer hash claims.

Actual **C1 CLEAN within assigned SOURCE teaching;C2 dependency/NAV/source-invariant
coverage CLEAN,quiz conclusions QUALIFIED;C3 CLEAN within26 whole RU bodies**,
not native certification. Seven lesson rulings/seven clarifications are accepted boundedly;
no significant current source-text fix,M001 or source withdrawal is established.
All21 historical directions remain active,with qualified **Q forward introductory-core ONLY**.
件くだん's bovine yokai1255930/3 limits件→牛;任 work/task prevents blanket任→件.
付's giving/entrusting/appearance and位's actual location/位する1640530 remain,
not all-sense/social-only clearance.
Broader ordinary/all-sense/reading-mode/fallback suitability,modern necessity-frequency
and global current/future uniqueness stay UNVERIFIED,not whole C2 CLEAN.
Seven outside observations are not guards;prior word-guard scope/identity and
082姉→妹's unrestricted U remain unchanged.
手伝う is not newly split:the wrapper surrounds standalone explanatory伝 elsewhere.

Qualified source checkpoint: **2056 runtime objects/1478 words/274 kanji/274 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**166 N4**/26 N3/2 N2;all166 frozen N4 included,
**341 of367 frozen N3 kanji remain**.
Strict progress: **2056 reviewed-current,two excluded reviewed blocked-media
drafts,6220 pending of8278;6222 runtime paths absent**,no partial.
Version `b4655aee17d7316d`;checkpoint authority null/Ready false.
2032 other baseline RAWs/tracking rows persist;10 word patches are NAV-only.
These become accepted-main counts only after signed normal integration;
fresh final serialized checks/public archives/signatures/four protected refs/
exact-main CI/owner issue verification have separate receipts.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue088+ and **ALL remaining safe frozen levels/families**,not task completion.

The previous eighty-sixth full-target batch adds **six complete Russian frozen N3 kanji
lessons,与/予/争/両/互/交,369 file lines**,and six RAW-identical KanjiVG assets.
Eleven existing word bodies receive11 **navigation-only wrappers**;
no new word or existing-word semantic amendment is introduced.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`;
signed intake,premutation freeze,proposals and candidate remain immutable.

The [actual whole review](translation-batches/086-giving-preparation-and-interaction-kanji-independent-review-001.json)
read **65 whole teaching bodies**,35 EN/30 RU:six primary EN/RU pairs,
24 current context pairs and five whole EN-only comparisons,including all
201 lines of the English kaeru article,not a RU runtime provider.
All11 changed word bodies are included,not additional bodies.
It read181 whole official TEXT units:19 KANJIDIC,four Unicode,152 ordered
JMdict and six visible KanjiPedia entries;one whole provider header is additional.
Zero glyph pixel views;historical inline glyphs stay UNINSPECTED.
It read267 current whole typed metadata rows,18 historical directions/17 active,
one M001,six lesson rulings/six separate clarifications,11 exact NAV diffs/11 wrappers,
six outside observations,four whole guidance files and three correct CURRENT RU rubrics.
72 actual successful reader commands/windows bind entire payloads/complete
line unions,not markers alone;metadata rows are not267 whole lessons or1478 fresh guards.

One actual whole review produced one successful **9945-byte stdout/native final**,
SHA256 `1446cb87e29862de94d1205d09860df7deb259f5451f29720f48d6e6ff6147fa`.
Original public bytes are unchanged,no path projection needed.
Two earlier size assertions failed before report emission,not earlier delivered
reports/semantic reviews,and credit no reading.
The one-shot reviewer is completed,not actually running.
Actual **C1 CLEAN within assigned SOURCE authoring;C2 SOURCE dependency/NAV
coverage CLEAN,quiz conclusions QUALIFIED;C3 CLEAN within30 whole RU bodies**,
not native certification. Six lesson rulings/six clarifications are supported boundedly;
no significant current source-text fix was requested.
Only explicit **086-M001** is independently supported:
`予.distractors [子,手,与]`→`[子,手]`.
Whole KanjiPedia予(B)②giving/類与 and与①giving defeat an unrestricted
historical N006予→与 against offered«давать; предоставлять».
All18 historical directions persist in evidence;17 active directions have
qualified introductory-core Q judgments.
Retained N003与→予 is separately Q against actual offered«заранее»;
no reciprocal/replacement/transitive deletion or fallback exclusion follows.
Broader ordinary/all-sense/reading-mode/fallback suitability,modern necessity-frequency
and global current/future uniqueness stay UNVERIFIED,not whole C2 CLEAN.
Six outside observations are not guards;prior word-guard scope/identity and
082姉→妹's unrestricted U remain unchanged.

Qualified source checkpoint: **2042 runtime objects/1478 words/267 kanji/267 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**166 N4**/19 N3/2 N2;all166 frozen N4 included,
**348 of367 frozen N3 kanji remain**.
Strict progress: **2042 reviewed-current,two excluded reviewed blocked-media
drafts,6234 pending of8278;6236 runtime paths absent**,no partial.
Version `7a11fb6dc2ec2efd`;checkpoint authority null/Ready false.
2019 other baseline RAWs/tracking rows persist;11 word patches are NAV-only.
These become accepted-main counts only after signed normal integration;
fresh final serialized checks/public archives/signatures/four protected refs/
exact-main CI/owner issue verification have separate receipts.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue087+ and **ALL remaining safe frozen levels/families**,not task completion.

The previous eighty-fifth full-target batch adds **six complete Russian N4 kanji lessons,
別/勉/真/答/親/題,385 file lines**,and six RAW-identical KanjiVG assets.
Fifteen existing word bodies receive15 **navigation-only wrappers**;
no new word,word semantic amendment or source-directed metadata correction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`;
signed intake,premutation freeze,proposals and candidate remain immutable.

The [actual whole review](translation-batches/085-separation-effort-truth-answers-parents-and-topics-kanji-independent-review-001.json)
read **90 whole teaching bodies**,45 RU/45 EN:six primary and39 current context
EN/RU pairs. All15 changed word bodies are included,not additional bodies.
It read232 whole official TEXT units:35 KANJIDIC,six Unicode,182 ordered JMdict,
six visible KanjiPedia and three supplemental KanjiPedia lexical texts.
Original229-TEXT and supplemental three-text receipts remain separate;
one whole provider header is additional and zero glyph pixel views are claimed.
Historical inline glyphs stay UNINSPECTED.
The review read261 current whole typed metadata rows,18 original directions,
six lesson rulings,five clarifications,15 exact NAV diffs/15 wrappers,
six outside observations,four guidance files and three correct CURRENT RU-root rubrics.
88 actual successful reader commands/windows bind entire returned payloads and
complete guidance line unions,not markers alone.
261 typed rows are not261 whole lessons or1478 freshly judged word guards.

One actual whole review produced one successful **10858-byte stdout/native final**,
SHA256 `721a847c031ae711b725749417ff5d73191dab50b801d48d734af1131f0f5dc3`.
Original public payload is unchanged;no path projection is needed.
Two earlier size assertions failed before report emission,not earlier delivered
reports/semantic reviews;failed commands credit no reading.
The one-shot reviewer is completed,not actually running.
Actual verdicts are **C1 PASS within assigned source content,
C2 QUALIFIED SOURCE PASS,C3 PASS within45 whole Russian bodies**.
No substantive source fix or required optional polish was established.
All18 original directions are retained with actual independent
**Q introductory-core contrast ONLY**;all broader ordinary-runtime/fallback/
all-sense/modern necessity-frequency/global current-future judgments remain UNVERIFIED.
No blanket ordinary-quiz C2 CLEAN is inferred.
Six lesson rulings/five clarifications are accepted boundedly;勉→力 and題→質
are judged against actual offered titles,not unrestricted reverse safety.
真まこと「―の道」supportsまことの;親しむ「土に親しむ」supports
things/contact,not an invented exact本に親しむ quote.
Six outside observations are not guards;prior word-guard scope/identity and
082姉→妹's unrestricted U remain unchanged.

Qualified source checkpoint: **2030 runtime objects/1478 words/
261 kanji/261 strokes**. Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**166 N4**/13 N3/2 N2.
**All166 frozen N4 kanji are included under qualified SOURCE scope**,not full-task closure.
Strict progress: **2030 reviewed-current,two excluded reviewed blocked-media
drafts,6246 pending of8278;6248 runtime paths absent**,no partial.
Version `6101e469724d76b4`;checkpoint authority null/Ready false.
2003 other baseline RAWs/tracking rows persist;15 word patches are NAV-only.
These become accepted-main counts only after signed normal integration;
fresh final serialized checks/public archives/signatures/four protected refs/
exact-main CI/owner issue verification have separate receipts.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue086+ and **ALL remaining safe frozen levels/families**,not task completion.

The previous eighty-fourth full-target batch adds **eight complete Russian N4 kanji
lessons,世/以/使/場/早/注/洋/漢,509 file lines**,and eight RAW-identical KanjiVG assets.
Twenty-three existing word bodies receive23 **navigation-only wrappers**;
no new word,word semantic amendment or source-directed metadata correction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`;
signed intake,premutation freeze,proposals and original report remain immutable.

The [actual whole review](translation-batches/084-world-use-water-and-places-kanji-independent-review-001.json)
read **108 whole teaching bodies**,54 RU/54 EN:8 primary and46 current
context EN/RU pairs. All23 changed word bodies are included,not extra bodies.
It read223 whole official source-TEXT units
(34 KANJIDIC/5 Unicode/176 ordered JMdict/8 visible KanjiPedia),
one whole provider header,255 current typed kanji rows,24 original directions,
eight lesson rulings,23 exact NAV diffs/23 wrappers,eight outside observations,
seven clarifications,four guidance files and three correct CURRENT RU-root rubrics.
Zero dictionary-glyph pixel views are claimed;historical inline glyphs stay
UNINSPECTED. Metadata rows are not255 whole lessons or1478 fresh word judgments.

One actual whole review produced one successful **10967-byte stdout/native final**,
SHA256 `30743e9d0b85a227764908faa63346e285fee322726bd49d83330f2856da5f92`,
including its terminal LF and **89 actual successful reader commands/windows**.
Two earlier size assertions failed before report emission;not earlier reports,
not more semantic reviews,and no reading credit.
Original bytes stay private/immutable;the public **10894-byte path-only projection**,
SHA256 `6afb1d6b81432196ba5a22226d30e957811aefe688c4167196beb0f412cd5518`,
replaces machine roots only and has a distinct byte/hash domain.

All eight roots/all24 original arrays persist with **24 independently qualified
introductory-core Q contrasts**,not unrestricted ordinary-quiz negatives.
使→事 was judged forward using the actual offered «дело; событие»/selectedこと;
extraつかう/つかえる and historical史/吏/事 forms alone do not prove a defect.
All seven dictionary clarifications are supported,including explicit selected
inventory boundaries for洋/漢's empty kun arrays and nonabsolute spelling
preferences for早/注. No reverse/transitive correction or guard clique follows.

**C1: qualified CLEAN within new teaching/preservation,not fresh certification
of all inherited historical claims. C2: assigned source/dependencies/NAV
qualified CLEAN and24 bounded core contrasts;broader ordinary/all-sense/fallback
C2 UNVERIFIED,not whole C2 CLEAN. C3: qualified CLEAN within54 whole RU bodies,
not native certification.**
No consequential correction was established within assigned facets.
Modern necessity/frequency and global current/future uniqueness remain UNVERIFIED.
Eight overlap observations are not new guards;速/所 are not typed kanji providers.
Prior word-guard scope/identity and082姉→妹's unrestricted U remain unchanged.

Qualified source checkpoint: **2018 runtime objects/1478 words/
255 kanji/255 strokes**. Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**160 N4**/13 N3/2 N2,**six frozen N4 remain:別/勉/真/答/親/題**.
Strict progress: **2018 reviewed-current,two excluded reviewed blocked-media
drafts,6258 pending of8278;6260 runtime paths absent**,no partial.
Version `c8dce7e6734759dd`;checkpoint authority null/Ready false.
1979 other baseline RAWs/tracking rows persist;23 word patches are NAV-only.
These become accepted-main counts only after signed normal integration;
fresh final checks,public archives/signatures/four protected refs/exact-main CI
remain separate publication evidence,not native/pixel/media approval.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue085+ and ALL remaining safe frozen levels/families,not task completion.

The previous eighty-third full-target batch adds **seven complete Russian N4 kanji
lessons,教/有/着/考/者/飯/館,411 file lines**,and seven RAW-identical KanjiVG assets.
Twenty-two existing word bodies receive22 **navigation-only wrappers**;
no new word or existing-word semantic amendment.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`;
signed intake,premutation freeze,proposals and original reports remain immutable.

The [actual whole review](translation-batches/083-teaching-existence-clothing-and-meals-kanji-independent-review-001.json)
read **96 whole teaching bodies**,188 whole official source-TEXT units,
one whole provider header,247 current typed kanji rows,21 historical
directions,seven lesson rulings,22 exact NAV diffs/22 wrappers,eight outside
observations,one source correction,three clarifications,four guidance files
and three correct CURRENT RU-root rubrics.
The whole207-line occupation-endings article is included.
Zero dictionary-glyph pixel views are claimed;historical inline glyphs,
including教's phonetic glyph,stay UNINSPECTED.
Metadata rows are not247 whole lessons or1478 fresh word judgments.

One actual whole review produced an earlier10946-byte stdout,SHA256
`93e84c504c1ef8f90d1679ce12ef9157dcb1589c056f6d80c00b91914c3d73b5`,
with an incorrect85-command count,and an actual corrected
**10803-byte stdout/native final**,SHA256
`604b54d8dfc247f2a7700c26c91cefe2370e49b2c5f592a92a25eaefe902892c`.
The latter records **82 actual successful reader commands/windows** and compact
wording. Both original deliveries persist;this is not a second semantic review.

The [premutation source freeze](translation-batches/083-teaching-existence-clothing-and-meals-kanji-source-adjudication-and-semantic-freeze-001.json)
proposes only083-S001:
`考.distractors [者,教,古]`→`[教,古]`.
Actual current死んだ父/先考 and whole JMdict2414430/1387630 support
the independently supported conservative one-way removal of N010考→者;
this is not merely historical elder derivation.
All seven mandatory roots/21 historical directions persist;
**20 active Q judgments are qualified introductory-core contrasts,
one rejected historical R is already removed**.
No automatic reverse correction or fallback exclusion follows.
着→目's actual Go-count/ordinal extensions limit C2.
The reviewer also supports the three explicit dictionary clarifications.

**C1: CLEAN within new source-text teaching/preservation,not fresh certification
of all inherited historical claims. C2: source coverage/NAV wrappers CLEAN
and20 bounded core contrasts;broader ordinary/all-sense C2 UNVERIFIED,
not whole C2 CLEAN. C3: CLEAN within assigned Russian text.**
No significant current source-text defect was found.
Ordinary quiz/fallback suitability,modern necessity/frequency and global
current/future uniqueness remain UNVERIFIED.
Eight overlap observations are not new guards;prior word-guard scope/identity
and prior082姉→妹's unrestricted U remain unchanged.

Qualified source checkpoint: **2002 runtime objects/1478 words/
247 kanji/247 strokes**. Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**152 N4**/13 N3/2 N2,**14 actual frozen N4 kanji remain**.
Strict progress: **2002 reviewed-current,two excluded reviewed blocked-media
drafts,6274 pending of8278;6276 runtime paths absent**,no partial.
Version `944b6247fc33d54c`;checkpoint authority null/Ready false.
1966 other baseline RAWs/tracking rows persist;22 word patches are NAV-only.
These become accepted-main counts only after signed normal integration;
fresh final checks,public archives/signatures/four protected refs/exact-main CI
remain separate publication evidence,not native/pixel/media approval.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue084+ and ALL remaining safe frozen levels/families,not task completion.

The previous eighty-second full-target batch adds **four complete Russian N4 kanji
lessons,味/妹/姉/始,287 file lines**,and four RAW-identical KanjiVG assets.
Thirteen existing word bodies receive14 **navigation-only wrappers**;
no new word or existing-word semantic amendment.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`;
signed intake,freeze,proposals and original reports remain immutable.

The [actual whole review](translation-batches/082-taste-family-and-beginnings-kanji-independent-review-001.json)
read **53 whole teaching bodies**,76 whole official source-TEXT units,
one whole provider header,240 current typed kanji rows,12 individual
directions,four adjudications,13 exact NAV diffs/14 wrappers,five outside
observations,four guidance files and three correct CURRENT RU-root rubrics.
Zero dictionary-glyph pixel views are claimed;the missing始 historical
inline glyph stays UNINSPECTED. Metadata rows are not whole lessons.
The actual **10827-byte stdout/final report**,SHA256
`5b9f6aaf8c8cb93e33ec15ff03784fe9765a534e0b0424c225a56b8e82513ffd`,
records C1/C3 CLEAN within scope and F082-01/C2 NEEDS FIX.
Its exact private original remains immutable;the tracked path-only public
projection is explicitly a different hash/length domain.

The signed [single source amendment](translation-batches/082-taste-family-and-beginnings-kanji-single-source-correction-freeze-001.json)
removes only invalid082-N004妹→姉:
`妹.distractors [姉,味,始]`→`[味,始]`.
Whole JMdict2752050's archaic妹いも means one's sister without a younger
restriction;the bare-glyph prompt does not constrain modernいもうと.
All12 historical directions and four closure members persist;
no replacement/reverse/transitive edge or lesson-prose change.
**Original dispositions stay10 Q +one R +one U,not11 Q.**
N007姉→妹 remains U for unrestricted clearance,with its modern core contrast
supported;no reciprocal defect was proved or automatically inferred.

The [actual focused review](translation-batches/082-taste-family-and-beginnings-kanji-independent-review-002.json),
**10132 bytes**,SHA256
`2ae374b7c73e3dd3e8d9bf5d9debc1024b4d6d87f71ba60bdd27ecaf3a317bd4`,
resolves only F082-01 after five whole teaching bodies,seven official TEXT
units,one header,two current/two prior typed rows and exact amendment/diff.
Its240-row identity audit is not fresh240-row semantics or another whole
53-body review. Ten Q judgments carry only original qualified core-contrast
scope;N007's U is not Q. **C1/C3: no remaining confirmed defect within
combined assigned scopes. C2: bounded correction CLEAN;broader C2 UNVERIFIED,
not whole C2 CLEAN.** Ordinary quiz suitability,modern necessity/frequency,
fallback safety and global future uniqueness remain UNVERIFIED.
No1478 fresh word-guard approvals or new exclusions follow.
姉はは remains attested metadata,not invented ordinary mother-reading usage;
始's historicalなりたち is not automatically modern lexical sister meaning.

Qualified source checkpoint: **1988 runtime objects/1478 words/
240 kanji/240 strokes**. Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**145 N4**/13 N3/2 N2,**21 actual frozen N4 kanji remain**.
Strict progress: **1988 reviewed-current,two excluded reviewed blocked-media
drafts,6288 pending of8278;6290 runtime paths absent**,no partial.
Version `730ea51721ee7090`;checkpoint authority null/Ready false.
1967 other baseline RAWs/tracking rows persist;13 word patches are NAV-only.
These become accepted-main counts only after signed normal integration;
fresh final checks,public archives/signatures/four protected refs/exact-main CI
remain separate publication evidence,not native/pixel/media approval.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue083+ and ALL remaining safe frozen levels/families,not task completion.

The previous eighty-first full-target batch adds **17 complete Russian kanji lessons/
1083 file lines,all actual frozen N4**,and17 RAW-identical KanjiVG assets.
Existing53 word bodies receive54 **navigation-only wrappers**;
no new word or existing-word semantic amendment.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original signed intake,freeze,proposals,candidate and report remain immutable.

The [actual whole review](translation-batches/081-light-nature-and-daily-life-kanji-independent-review-001.json)
read **215 whole teaching bodies**,306 whole official source-TEXT units,
one whole provider header,one actual PNG,236 current typed kanji rows,
all51 directions,18 adjudications,53 exact NAV diffs/54 wrappers,
11 outside observations,four guidance files and three correct CURRENT RU-root rubrics.
The **10889-byte actual stdout/final report**,SHA256
`93209116b8637757799463a0bbf560e9bfb0f4ee27dab31b2f1c8852f0f5fa08`,
requested F081-01/C2 and F081-02/C3;do not rewrite that historical verdict.
The signed explicit source amendment removes only invalid active英→花
from英.distractors,`[茶,花,映]`→`[茶,映]`,preserving all17 closure and51 history.
曜 explicitly names月曜日 in the three-reading warning;correct nativeひ→び persists.

The [actual focused review](translation-batches/081-light-nature-and-daily-life-kanji-independent-review-002.json),
**8712 bytes**,SHA256
`2fba3db032c7e4153563a8c9e77483e05976bed07088cab44cbb74bf7358c730`,
resolves only the two exact changes and the first report's wrong prospective-pool
hash label. It read eight whole teaching bodies,nine whole official TEXT units,
one header and two current/two prior typed rows.
The236-row audit independently confirms actual original602983... candidate
payloads and corrected2d2c... pool identities,not236 fresh semantic judgments.
Original10889-byte report remains immutable.
No second whole215-body review or1478 fresh word approval is claimed.
The50 retained Q directions carry only original qualified core-contrast scope;
N038 remains rejected history,with no invented replacement/reverse/transitive edge.
**C1/C3: no remaining confirmed defect within combined assigned scopes.
C2: bounded correction resolved,NOT whole C2 CLEAN. Broader ordinary quiz/
fallback suitability,modern necessity/frequency and global future uniqueness UNVERIFIED.**
Other glyph pixels remain UNINSPECTED;prior word-guard scope/identity persists.

Qualified source checkpoint: **1980 runtime objects/1478 words/
236 kanji/236 strokes**. Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**141 N4**/13 N3/2 N2,**25 actual frozen N4 kanji remain**.
Strict progress: **1980 reviewed-current,two excluded reviewed blocked-media
drafts,6296 pending of8278;6298 runtime paths absent**,no partial.
Version `b1d5197e8fc7fe07`;checkpoint authority null/Ready false.
1893 other baseline RAWs/tracking rows persist;53 word patches are NAV-only.
These become accepted-main counts only after signed normal integration;
fresh final checks,public archives/signatures/four protected refs/exact-main CI
are separate publication evidence,not native/pixel/media approval.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue082+ and ALL remaining safe frozen levels/families,not task completion.

The previous eightieth full-target batch adds **17 complete Russian kanji lessons/
1089 file lines:16 actual N4 plus unchanged source-N3達**,and17 RAW-identical
Japanese KanjiVG assets. Existing51 words receive51 **navigation-only wrappers**,
with no semantic amendment:50 standalone glyph wrappers and the existing
Russian meaning «продавать» in売り場. Japanese text,readings,examples,
metadata,quiz arrays,visible prose and original links persist.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`;
original signed intake,premutation freeze and report persist.

The [actual whole review](translation-batches/080-movement-routes-and-transitions-kanji-independent-review-001.json)
read **199 complete teaching bodies**:17 primary EN/RU pairs,81 current
context EN/RU pairs and three whole EN-only comparisons.
Its **266 whole source-TEXT units** are46 KANJIDIC records,nine Unicode
radical rows,193 whole ordered JMdict objects,17 whole visible KanjiPedia
entry/alt-label projections and the entire selected平凡社「普及版 字通」発
section including credit,visible[72,103)of146.
This is not whole Kotobank HTML/page/pixels.
The review read219 current typed kanji rows,all51 individual directions,
15 adjudications,51 exact patches,eight outside-edge observations,
four guidance files and three correct CURRENT RU-root rubrics.
Entire successful payloads/complete oversized line unions are bound;
219 metadata rows are not219 whole lessons or1478 fresh word-pool judgments.
The **10722-byte detailed report is actual reviewer stdout**,SHA256
`44fb95605bea67fa0b34220542595857adf807b1f4aed41e90c0752e4f8e892f`;
native/task final is a different52-byte generic summary.
Three actual unchanged-snapshot gates and four noncredited in-memory
report-length attempts persist;no reading gap or second review is invented.

**C1/C3: no consequential defect established within assigned scope.
C2: qualified dependencies and individual lexical-core contrasts only,
NOT whole C2 CLEAN.** All51 directions retain their individual qualified scope,
not universal disjointness. Eight outside observations,including運/福 «удача»,
are limitations,not new exclusions/global pair approvals.
**Broader ordinary quiz/fallback suitability,modern necessity/frequency and
future global uniqueness remain UNVERIFIED.** Rare/character attestation and
the selected字通 section do not establish ordinary productive spelling,
frequency,dictionary-only status or universal replacement.
Old word guards retain prior identity/support/limits,not1478 fresh judgments;
no semantic repair or learner correction occurred.

Qualified source checkpoint: **1946 runtime objects/1478 words/
219 kanji/219 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**124 N4**/13 N3/2 N2,leaving **42 actual frozen N4 kanji**.
Strict progress: **1946 reviewed-current,two excluded reviewed blocked-media
drafts,6330 pending of8278;6332 runtime paths absent**,no partial.
Version `abf49588ec0b0583`;checkpoint authority null/Ready false.
1861 other baseline RAWs/tracking rows persist;51 word patches are NAV-only.
Counts become accepted-main only after signed normal integration;
fresh final checks,actual archives/signatures/four protected refs/exact-main CI
are separate publication evidence. Stroke/root-license identity is not native,
pixel or media approval. Protected033 **word**空 stays excluded/runtime-absent/
C2 UNVERIFIED,not media;accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue081+ and ALL remaining safe frozen levels/families,not task completion.

The seventy-ninth full-target batch adds **23 complete Russian kanji lessons/
1480 file lines:22 actual N4 plus unchanged source-N3供**,and23 RAW-identical
Japanese KanjiVG assets. Existing55 words receive56 navigation wrappers:
**53 navigation-only plus two explicit semantic amendments,子供 and旅行**.
Signed premutation authority withdraws unsupported stronger spelling-policy/
preference/frequency claims andこども家庭庁 narrative illustration in子供,
and unsupported long/lonely/poetic/literary rankings in旅行 consistently with旅.
Those claims are not disproved. Original lexical metadata,readings,grammatical
Japanese example sentences and existing links persist;not every Japanese
narrative fragment is unchanged. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`;historical intake/freeze persist.

The [actual whole review](translation-batches/079-people-work-and-feelings-kanji-independent-review-001.json)
read **226 complete teaching bodies**:23 primary EN/RU pairs,85 current
context EN/RU pairs,eight EN-only comparisons,two whole historical RU
子供/旅行 bodies. It read **351 whole official units**:52 KANJIDIC records,
nine Unicode rows,267 whole ordered JMdict entries and23 whole visible
KanjiPedia entry/actual-alt-label projections,not whole HTML/pixels.
It read202 current typed kanji rows,69 individual directed proposals,
14 adjudications,55 exact patches,four guidance files and three correct
RU-root rubrics. Entire successful payloads/complete oversized line unions
are bound,not markers alone;202 metadata rows are not202 whole lessons
or1478 fresh word-pool judgments. The **10984-byte detailed report is
actual reviewer stdout**,SHA256
`23b72d223836aa6e4ea029cf925374201c694ec2b0b8e286047f169e7d3a47b3`;
native/task final is a different52-byte generic summary.
No byte identity or second review is fabricated.

**C1/C3: no significant issue established within assigned scope.
C2: assigned dependencies,amendments and qualified core contrasts established,
NOT whole C2 CLEAN.** All69 directions retain only stated lexical-core scope.
For N005仕→土,the author «visible土component» wording is not adopted;
the whole EN/RU lessons already correctly identify士.
Its [append-only disposition](translation-batches/079-people-work-and-feelings-kanji-review-qualification-dispositions-001.json)
changes no learner bytes. 借/貸 roles,色/白 category/subtype,旅/行/道 travel
and貸/質 pawn-domain connections remain qualified,not universally disjoint.
Outside69 overlap flags are not new pair judgments/runtime exclusions.
**Broader ordinary quiz/fallback suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED.** Rare/historical attestations
are not ordinary productive-practice approval;old guards retain prior
identity/support/limits,not1478 fresh semantic judgments.

Qualified source checkpoint: **1912 runtime objects/1478 words/
202 kanji/202 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**108 N4**/12 N3/2 N2,leaving **58 actual frozen N4 kanji**.
Strict progress: **1912 reviewed-current,two excluded reviewed blocked-media
drafts,6364 pending of8278;6366 runtime paths absent**,no partial.
Version `ae145971f3403a2b`;checkpoint authority null/Ready false.
1811 other baseline RAWs/tracking rows persist;53 NAV-only and two semantic
updates are separate. Counts become accepted-main only after signed normal
integration;fresh final checks,actual archives/signatures/four protected
refs/exact-main CI are separate publication evidence.
Stroke/root-license identity is not pixel/native/media approval.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue080+ and ALL remaining safe frozen levels/families,not task completion.

The seventy-eighth full-target batch adds **16 complete Russian kanji lessons/
778 file lines,all actual frozen N4**,and16 RAW-identical Japanese KanjiVG
assets. Existing54 complete word bodies receive55 exact navigation wrappers;
Japanese/readings/examples/metadata/quiz arrays/original word links persist.
The牛肉 change preserves `[肉](肉.md)` and wraps only its adjacent existing
Russian meaning as `«[мясо](../kanji/肉.md)»`;the malformed private proposal
was rejected before learner mutation. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`;signed intake/freeze persist.

The [actual whole review](translation-batches/078-home-places-and-everyday-things-kanji-independent-review-001.json)
read **221 complete teaching bodies**:16 primary EN/RU pairs,91 current
context EN/RU pairs,seven EN-only comparisons. Its official source scope is
**331 whole units plus two exact postal heading sections**,not333 whole
webpages:53 KANJIDIC records,13 Unicode key rows,234 whole ordered JMdict
entries,16 primary KanjiPedia and15 supplementary semantic projections.
It read179 current typed kanji rows,48 original directions,12 adjudications,
54 exact navigation diffs,four complete guidance files and three correct
RU-root rubrics. Entire successful payloads/complete oversized line unions
are bound,not markers alone. Neither postal listing was whole-read;
179 metadata rows are not179 whole lessons or1478 fresh word-pool judgments.
The **10843-byte detailed report is actual reviewer stdout**,
SHA256 `cdbb41d50df13341845070321cda3ccc9a36c2aa8662cb3b390a0d9cd5bad29d`;
native/task final is a different52-byte generic summary.
No byte identity or second review is fabricated.

**C1/C3: no consequential defect found within assigned scope.
C2: qualified core-contrast/dependency pass,NOT whole C2 CLEAN.**
All48 directions retain only stated lexical-core scope;N025死→切 covers
death versus cutting,not every ending sense,andN028/N029物→本/車 do not
make books/vehicles universally wrong answers for a generic thing.
The other45 are still qualified,not universal disjointness.
No D/Q reclassification,new exclusion fields or reverse/transitive edges.
**Broader fallback quiz suitability,modern necessity/frequency and global
future uniqueness remain UNVERIFIED**,including元/本,家/内,台/私,
画/図/計,generic/specific objects and ending-related overlaps.
Rare/historical references do not establish ordinary productive practice;
frozen花の京 has no fresh phrase-specific attestation. Prior word guards
retain only their original identity/support/limitations.

Qualified source checkpoint: **1866 runtime objects/1478 words/
179 kanji/179 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**86 N4**/11 N3/2 N2,leaving **80 actual frozen N4 kanji**.
Strict progress: **1866 reviewed-current,two excluded reviewed blocked-media
drafts,6410 pending of8278;6412 runtime paths absent**,no partial.
Version `b29f4d5e03b8582f`;checkpoint authority null/Ready false.
The1780 other baseline RAWs/tracking rows persist;54 navigation updates
are separate. These become accepted-main counts only after signed normal
integration;fresh final serialized checks,actual archives/signatures/four
protected refs/exact-main CI are separate publication evidence.
Stroke/root-license identity is not pixel/native/media approval.
Protected033 **word**空 remains excluded/runtime-absent/C2 UNVERIFIED,
not media;accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue079+ and ALL remaining safe frozen levels/families,not task completion.

The seventy-seventh full-target batch adds **22 complete Russian kanji lessons/
1279 file lines,21 actual N4 plus unchanged source-N2短**,and22 RAW-identical
frozen Japanese KanjiVG assets. Existing53 word bodies receive only56
navigation wrappers;Japanese/examples/metadata/quiz arrays remain unchanged.
The frozen EN target remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`;
signed intake,adjudication/freeze and fragment-restoration amendment persist.
The [actual whole review](translation-batches/077-study-writing-and-inquiry-kanji-independent-review-001.json)
read **250 whole teaching bodies/295 whole official source units/
163 current typed kanji rows/66 individual explicit directions/15 adjudications/
53 exact navigation diffs/three whole correct RU-root rubrics**.
Teaching bodies comprise22 primary EN/RU pairs,99 current context EN/RU pairs
and eight EN-only comparisons. Source units comprise64 genuine RAW KANJIDIC
records,17 Unicode key rows,185 whole ordered JMdict objects,22 KanjiPedia
main/five lexical projections and two complete captured Kotobank returns.
All150 actual public tool returns are bound;only entire successful payloads
receive reading credit. Rows are not whole lessons and projections are not pixels.
The **9717-byte detailed report is actual successful reviewer stdout**;
the actual native/task final is a different52-byte generic summary.
**No stdout/native byte identity is invented**,and two failed report-size
print attempts receive no evidence credit.

**C1/C3: no confirmed consequential defect within assigned scope.
C2: qualified dependency/explicit-direction pass only,not blanket CLEAN.**
All66 directions retain only current-core scope;eight receive additional
narrow qualifications,58 retain core contrasts,none establish universal
semantic disjointness. No independent D/Q reclassification,new kanji
exclusion fields or reverse/transitive directions are invented.
**Ordinary fallback quiz safety,modern necessity/frequency and global future
uniqueness remain UNVERIFIED**,including known non-explicit空/天,図/計,
試/験,言/話/語 and文/字 overlaps.
図え/験あかし are adequate limited character-reading references,
not verified modern standalone lexical practice;no examples are fabricated.
Existing word guards retain prior identity/support/limitations,
not1478 fresh word-pool/guard judgments.

Qualified source checkpoint: **1834 runtime objects/1478 words/
163 kanji/163 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**70 N4**/11 N3/2 N2,leaving **96 actual frozen N4 kanji**.
Strict progress: **1834 reviewed-current,two excluded reviewed blocked-media
drafts,6442 pending of8278;6444 runtime paths absent**,no partial.
Version `757e4bc2daf819c8`;checkpoint authority null/Ready false.
The1737 other baseline RAWs/tracking rows persist;53 navigation updates
are recorded separately. Stroke byte identity/root licenses are not
rendered/native animation approval. These become accepted-main counts
only after normal signed integration;fresh final serialized checks,
actual public archives/signatures/four protected refs/exact-main CI remain
separate publication evidence. Protected033 **word**空 remains excluded,
runtime-absent/C2 UNVERIFIED,not media;new **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue078+ and ALL remaining safe frozen levels/families,not task completion.

The seventy-sixth full-target batch adds **20 complete Russian lessons/
1031 file lines,all actual N4**,against unchanged frozen EN.
The [actual whole review](translation-batches/076-remaining-n4-states-and-formal-nouns-independent-review-001.json)
read **366 whole teaching bodies/403 whole official ordered projections/
1478 fresh CURRENT caption-reading-type-tags-actual-level-quiz rows/three
whole correct RU-root rubrics**:20 primary EN/RU pairs,140 contextual
pairs,45 EN-only comparisons and one complete1708-line EN article.
No external pages were fetched/read. Its **10356-byte actual report**
has identical successful stdout/native payloads,with167 actual public
tool events/entire returned payloads bound separately. Rows are not
whole lessons or observed quiz runs.

**C1/C3: no consequential Japanese/content or Russian-comprehension defect
established in the20 new lessons within assigned evidence. C2:70 individual
qualified S judgments**,one original source guard plus69 additions.
The author's5D/65Q labels are not independent D/Q classifications.
Q004皆–全然 adopts only the reviewer's narrower complete-extent scope
in negative-evaluation contexts,not “not at all” or positive “very”;
the stronger author affirmative-only selection claim is withdrawn,
not the runtime guard.
The [append-only resolution](translation-batches/076-remaining-n4-states-and-formal-nouns-review-resolution-amendment-001.json)
preserves C2-1:Q061眠る–寝る incorrectly cited1529330(眠い).
The correct1360010(寝る) whole object/provider was already actually read
and independently supported by that original review;only the bound record
is corrected by append. The valid guard,learner bodies,signed original
freeze/report and all1770 baseline runtime RAWs/tracking/history persist.
No second whole/focused review or70 fresh judgments is claimed.
All70 carry only actual original qualified scope/current identity.
**Broader ordinary modern quiz suitability,necessity/frequency and global
future uniqueness remain UNVERIFIED for every pair;not blanket C2 CLEAN.**
Japanese IDs/readings/examples/levels/source guard/available navigation
remain intact;only unavailable optional navigation wrappers are unwrapped.
Alternate kana identities,register,animacy,participant roles and secondary
senses remain explicitly limited;no transitive pair closure.

Qualified source checkpoint: **1790 runtime objects /1478 words**,
671 N5/**636 N4**/97 N3/19 N2/55 unlabelled.
**All636 actual frozen N4 words now have complete reviewed source,
not full-target completion or ordinary RU activation.**
Strict progress: **1790 reviewed-current,two excluded reviewed blocked-media
drafts,6486 pending of8278;6488 runtime paths absent**,no partial.
Version `051fad4e7c9dcf2b`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration.
Fresh final serialized checks,actual public archives/signatures/four
protected refs/exact-main CI remain separate publication evidence.
Protected033空 remains the only pending N5 word,excluded/C2 UNVERIFIED,
not media. No assets/native/device/phone/IME/media/default/package/release
authority. Continue077+ and ALL remaining safe frozen levels/families;
not task completion. Earlier milestones retain their original scope.

The seventy-fifth full-target batch adds **20 complete Russian lessons/
1164 file lines,all actual N4**,without reclassification,against unchanged
frozen EN. The [actual original whole review](translation-batches/075-public-life-commerce-and-services-independent-review-001.json)
read **271 whole teaching bodies/299 whole official ordered projections/
1458 fresh current caption-reading-type-tags-level-quiz rows/three whole
correct RU-root rubrics**:20 primary EN/RU pairs,81 contextual pairs and69
EN-only comparisons. No articles/external pages were read.
Its **10933-byte stdout/native identity** and original verdicts remain
immutable: **C1 PASS within assigned teaching scope,C2 NOT CLEAN with
F1/F2,C3 requiring Russian agreement correction**.

Following a signed pre-mutation amendment,the
[actual focused review](translation-batches/075-public-life-commerce-and-services-independent-review-002.json)
read **11 whole teaching bodies/five whole official objects/five specific
corrected rows/three whole correct RU-root rubrics**,the original report,
bounded amendment and exact two-file diff.
Its **7808-byte stdout/native identity** resolves F1 with new Q038
失敗–落す under the conservative lexical policy:school/course failure
or contest loss only,canonical runtime落す/おとす,new owner only,
transitive participant/causal roles preserved. No unrestricted failure,
physical-dropping,general-exam or modern-necessity proof follows.
F2/Q030失敗–違う is resolved by withdrawing an unsupported author proposal,
not a source edge or proof of direct equivalence.
輸入's «нужен сказуемый»→«нужно сказуемое» fixes Russian neuter agreement,
not Japanese import direction. 消しゴム–ゴム has no CURRENT pair solely
becauseゴム is absent;standalone eraser abbreviation is attested and
material/item difference is not a universal negative.

**37 current protections =36 original individual S judgments carrying only
original qualified scope/current identity plus newly supported Q038.**
Original author3D/34K labels are not independent D/K classifications.
No36 fresh judgments,second whole review or1458 fresh focused rows are
claimed. The author freshly read all1458 corrected rows/two affected
whole RU lessons;18 other new lessons retain original whole-reading and
identity evidence. **Broader ordinary modern quiz suitability,necessity/
frequency and global future uniqueness remain UNVERIFIED for every pair,
including author-labelled D/Q038;not blanket C2 CLEAN/PASS.**
No new blocking C1/C3 issue was found within actual corrective scope.
All1750 accepted baseline RAWs/tracking/history remain unchanged.

Qualified source checkpoint: **1770 runtime objects /1458 words**,
671 N5/616 N4/97 N3/19 N2/55 unlabelled; **20 N4 remain**.
Strict progress: **1770 reviewed-current,two excluded reviewed blocked-media
drafts,6506 pending of8278;6508 runtime paths absent**,no partial.
Version `b54d436ba00b8218`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration.
Fresh final serialized checks,actual public archives/signatures/four
protected refs/exact-main CI remain separate publication evidence.
Protected033空 remains the only pending N5 word,excluded/C2 UNVERIFIED,
not media. No assets/native/device/phone/IME/media/default/package/release
authority. Continue076+ and ALL remaining safe frozen levels/families;
not task completion. Earlier milestones retain their original scope.

The seventy-fourth full-target batch adds **25 complete Russian lessons/
1475 file lines:20 actual N4 and five actual N3**,without reclassification,
against unchanged frozen EN.
The [actual whole review](translation-batches/074-actions-search-and-handling-independent-review-001.json)
read **381 whole teaching bodies/417 whole official ordered projections/
1438 fresh current caption-reading-quiz rows/three whole RU-root rubrics/
one whole named Digital Daijisen entry**:25 primary EN/RU pairs,
130 contextual pairs,70 EN-only words and one complete1708-line EN article.
Its **10828-byte stdout/native identity** is preserved. Rows are not whole
lessons;the named entry is not the whole Weblio page or frequency proof;
the contextual article is not fresh reading of all linked sources/PDFs.
**C1/C3 find no blocking correction in25 translated primaries within
assigned evidence**,not universal/native certification.
**C2 supports165 individual qualified protections,18D/147K**:
21 source3D/18K plus144 additional15D/129K;unsupported/withdrawn:none.
No additional missing direct pair was confirmed in the1438-row current
pool and actual evidence. Standalone alternate readings,secondary senses,
participant roles,transitivity,register and domains remain qualified.
**Broader ordinary modern quiz suitability,necessity/frequency and
global future uniqueness remain UNVERIFIED for all165,including D;
not blanket C2 CLEAN/PASS or unrestricted substitution.**
No substantive correction finding/amendment/focused report/second whole
is invented. All1725 accepted baseline RAWs/tracking/history persist.
打つうつ/ぶつ forms/senses,気付く actualN3/kango/mixed reading and full
こと attachment,見つかる finding-result and attested 見つける visual
familiarity remain distinct;attestation is not modern-frequency evidence.
Qualified source checkpoint: **1750 runtime objects /1438 words**,
671 N5/596 N4/97 N3/19 N2/55 unlabelled; **40 N4 remain**.
Strict progress: **1750 reviewed-current,two excluded reviewed blocked-media
drafts,6526 pending of8278;6528 runtime paths absent**,no partial.
Version `113a0f93170b0594`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration.
Fresh final serialized checks,actual public archives/signatures/four
protected refs/exact-main CI remain separate publication evidence.
Protected033空 remains the only pending N5 word,excluded/C2 UNVERIFIED,
not media. No assets/native/device/phone/IME/media/default/package/release
authority. Continue075+ and ALL remaining safe frozen levels/families,
not task completion. Earlier milestones below retain their original scope.

The seventy-third full-target batch adds **26 complete Russian lessons/
1493 file lines:20 actual N4,five actual N3 and one unlabelled顔**,
without reclassification or adding absent `jlpt`,against unchanged frozen EN.
The [actual original whole review](translation-batches/073-movement-direction-and-transfer-independent-review-001.json)
read **317 whole teaching bodies/383 whole official ordered projections/
1413 original fresh caption-reading-quiz rows/three whole RU-root rubrics/
923 instruction lines**:26 primary EN/RU pairs,91 contextual pairs,
81 EN-only words and two whole EN-only articles. No external page was
fetched/read. Its **10861-byte stdout/native identity** and bounded
C1/C3 findings remain immutable: no confirmed required factual correction
or consequential Russian-language defect in26 new lessons against assigned
evidence. **C2 originally had F1–F7 unresolved,not CLEAN**:
one P2 gap and six P3 qualified safeguard questions,not proven universal
modern necessity.
Original111 individual judgments are **68D/43K**:
14 retained source12D/2K plus97 additional56D/41K.
The source向かう–顔 withdrawal is independently supported only for
the original candidate/scope and unchanged identity;frozen EN/intake15
declarations remain immutable,14 retained. Three顔 objects/body were
not newly read in the later focus.

A signed pre-mutation amendment adds **24 protections RP098–RP121
on17 new owners**,with16 unchanged accepted providers.
The [actual focused review](translation-batches/073-movement-direction-and-transfer-independent-review-focused-002.json)
resolves only the exact F1–F7 questions as bounded lexical protection:
**66 whole bodies/33 EN/RU pairs,32 whole objects,33 fresh corrected
affected rows,three whole RU-root rubrics,923 instruction lines**,
the complete original report,three complete records and exact329-line diff.
Its **10994-byte stdout/native identity** is preserved;24 fresh judgments
are **12D/12K**. C1/C3 find no confirmed new substantive factual or
consequential Russian regression within focus,not a new whole certification.
The four whole provider pairs 一杯/落す/押す/もらう are newly included
in append-only binding004/focus,not original317-body bilingual reading.

The **135 current pairs:80D/55K** retain111 judgments carrying
**only original scope/identity**,not111 or135 fresh focused judgments.
All26 new teaching-body byte tails,9 whole new RAW files and1396/1413
rows are unchanged. Only24 inline exclusions on17 new-owner lists changed;
no baseline/provider/body/caption/Japanese/classification mutation.
This is not a second317-body/383-object review or1413 fresh corrected rows.
Banking verb/noun,secondary-sense,orientation/participant,illness and fax
limitations persist;D/K is not unrestricted substitution.
**Broader C2 ordinary quiz suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED,not blanket CLEAN/PASS.**
All1699 accepted baseline runtime RAWs/tracking/history persist.
Qualified source checkpoint: **1725 runtime objects /1413 words**,
671 N5/576 N4/92 N3/19 N2/55 unlabelled; **60 N4 remain**.
Strict progress: **1725 reviewed-current,two excluded reviewed blocked-media
drafts,6551 pending of8278;6553 runtime paths absent**,no partial.
Version `d57de202b04c40d6`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration.
Fresh final serialized checks,actual public archives/signatures/four
protected refs/exact-main CI remain separate publication evidence.
Protected033空 remains the only pending N5 word,excluded/C2 UNVERIFIED,
not media. No assets/native/device/phone/IME/media/default/package/release
authority. Continue074+ and ALL remaining safe frozen levels/families,
not task completion.

The seventy-second full-target batch adds **20 complete actual N4
Russian lessons /1053 file lines**,without reclassification,against
the unchanged frozen EN target.
The [actual original whole review](translation-batches/072-qualities-evaluation-and-manner-independent-review-001.json)
read **297 whole teaching bodies/355 whole official ordered projections/
1387 original fresh caption-reading-quiz rows/three whole RU-root rubrics/
three historical public external payloads**:20 primary EN/RU pairs,
98 contextual pairs,55 EN-only words,four EN-only articles and two
extra RU-only bodies,多い/事故.
Its10819-byte stdout/native identity and actual C1/C3 wording,
**“No consequential new lesson-level factual error established” /
“No consequential new Russian-language defect established”**,remain
bounded by the original scope. **C2 originally had unresolved consequential
medium072-F01/F02,not CLEAN.**
Original122 individual judgments:five sourceD plus117 additional89D/28K
= **94D/28K**,only bounded lexical protection.

A signed pre-mutation amendment adds **RP118 おかしい–違う /
RP119 凄い–多い** for the exact findings,and **RP120 しっかり–結構 /
RP121 変–事故** for two original K-level questions,not new findings.
The [actual focused review](translation-batches/072-qualities-evaluation-and-manner-independent-review-focused-002.json)
resolves only the exact F01/F02 missing-direct-protection findings:
**16 whole bodies/eight EN/RU pairs,eight whole objects,eight fresh
affected rows,three whole RU-root rubrics,923 instruction lines**,
the complete original report,amendment,applied record and exact diff.
Its9613-byte stdout/native identity is preserved.
New independent judgments are **RP118/119 D,RP120/121 K**.
C1/C3 establish no consequential new error or correction-induced
regression within that focus,not a new whole-batch certification.
RP120/121 retain explicit qualified-conservative lexical limitations;
their ordinary modern applicability/necessity/frequency is UNVERIFIED.

The **126 current pairs:96D/30K** include122 retained judgments carrying
**only original scope/identity**,not122 fresh focused judgments.
All20 new teaching-body RAWs,16 new whole-file RAWs and1383/1387 rows
are unchanged. Only four new-owner quiz-exclusion lists changed;
no baseline-provider/body/caption/Japanese/classification mutation.
This is not a second297-body review or1387 fresh corrected rows.
No automaticどんどん–すっと speed pair,positive/degree/manner clique
or withdrawn070 guard revival;なかなか1599420.4 is Nの,not unrestrictedな.
**Broader C2 ordinary quiz suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED,not blanket CLEAN/PASS.**
All1679 accepted baseline runtime RAWs/tracking/history persist.
Qualified source checkpoint: **1699 runtime objects /1387 words**,
671 N5/556 N4/87 N3/19 N2/54 unlabelled; **80 N4 remain**.
Strict progress: **1699 reviewed-current,two excluded reviewed blocked-media
drafts,6577 pending of8278;6579 runtime paths absent**,no partial.
Version `2aab0f69daec0c92`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration.
Final serialized checks,actual public archives/signatures/four protected
refs/exact-main CI remain separate publication evidence.
Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue073+ and ALL remaining safe frozen levels/families,not task completion.

The seventy-first full-target batch adds **30 complete Russian lessons/
1700 file lines:20 actual N4 and ten actual N3** recursive explicit
providers,without reclassification,against unchanged frozen EN.
The [actual original whole review](translation-batches/071-degree-extent-sufficiency-and-assessment-independent-review-001.json)
read **263 whole teaching bodies/389 whole official ordered projections/
1367 original fresh caption-reading-quiz rows/three whole RU-root rubrics**:
30 primary EN/RU pairs,83 contextual pairs,36 EN-only words and one
EN-only article. Its9351-byte stdout/native identity and actual
**C1 PASS,C2 REVISE071-F01,C3 REVISE071-F02 minor** remain immutable.
Original166 individual judgments:26 source12D/14K plus140 additional
39D/101K = **51D/115K**,only bounded lexical protection.

A signed pre-mutation amendment adds exactly **RP141 ずいぶん–実に**
and verified **足す（たす）** in two new owners.
The [actual focused review](translation-batches/071-degree-extent-sufficiency-and-assessment-independent-review-focused-002.json)
resolves onlyF01/F02: **seven whole bodies** (three EN/RU pairs and
EN-only足す),**four whole objects,three fresh affected rows,three whole
RU-root rubrics**,the original report,amendment,applied record and exact
diff. Its8165-byte stdout/native identity is preserved.
**C1 PASS,C2 PASS only for the exact amendment/direct lexical subscope,
C3 PASS** are bounded,not a second whole review or blanket C2.
RP141 is independently **D** with expectation/surprise/evaluation
restrictions,not universal interchangeability or an ordinary-frequency claim.
足す stays unlinked,EN-only and absent from runtime,not a new provider.

The **167 direct pairs:52D/115K** include166 retained judgments carrying
**only original scope/identity**,not166 fresh focused judgments.
Exactly29/30 bodies,28/30 new whole RAW files and1365/1367 rows are
unchanged;one quiz-metadata change onずいぶん and one RAW-only reading
change on足りる. The third fresh affected row is unchanged実に;
足す has no runtime row. This is not1367 freshly reread corrected rows.
Additionalずいぶん–悪い andなかなか/かなり–ちょっと questions
remain unadopted/unverified,not required corrections.
**Broader C2 ordinary quiz suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED.**
All1649 accepted baseline runtime RAWs/tracking/history persist.
Qualified source membership: **1679 runtime objects /1367 words**,
671 N5/536 N4/87 N3/19 N2/54 unlabelled; **100 N4 remain**.
Strict progress: **1679 reviewed-current,two excluded reviewed blocked-media
drafts,6597 pending of8278;6599 runtime paths absent**,no partial.
Version `2bc3b24fd9aba5a3`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/
signatures/four protected refs/exact-main CI remain separate evidence.
Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue072+ and ALL remaining safe frozen levels/families,not task completion.

The seventieth full-target batch adds **20 complete actual N4 connector/
response/degree lessons /1114 Russian file lines** against unchanged frozen EN.
The [actual original whole review](translation-batches/070-connectors-response-and-degree-independent-review-001.json)
read **225 whole teaching bodies/400 whole official ordered projections/
1337 original fresh caption-reading-quiz rows/three whole RU-root rubrics**:
20 primary EN/RU pairs,74 contextual pairs and37 frozen-only bodies.
All101 assigned windows returned;10979-byte stdout/native identity and
actual **C1/C3 CLEAN,C2 NEEDS_FIX 070-F01/F02** remain immutable.
Original74 individual judgments:three source direct guards plus71 additional
proposals,31 direct/38 qualified/one rejected/one unverified.

The exact pre-mutation amendment withdraws **Q68 全然–みんな (R)/
Q69 全然–もう (U)**,without declaring never-overlap or frequency.
The [actual focused review](translation-batches/070-connectors-response-and-degree-independent-review-focused-002.json)
resolves **onlyF01/F02 in the corrected focus**:18 whole bodies,nine whole
official objects,nine affected rows,three whole RU-root rubrics,the exact
diff,amendment and original report;all13 assigned windows returned.
Its10374-byte stdout/native identity and **C1/C2/C3 CLEAN** verdicts
are bounded,not a second whole review or blanket C2 CLEAN.
It individually supports **RP72 こう–そうして (D)** and
**RP73 そう–そうして/RP74 ああ–そうして/RP75 こう–それほど/
RP76 こう–そんなに (Q)**,with actual whole-word manner/degree,
viewpoint and construction restrictions,not automatic family closure.

The **77 direct pairs:35 direct/42 qualified** include72 retained judgments
carrying **only original scope/identity**,not72 fresh judgments.
All20 learner bodies remain RAW-identical;1333 pool rows are identical.
The nine fresh affected rows include four changed owners/five unchanged
providers;other1328 are outside fresh focus,retained by identity.
This is not1337 freshly reread corrected rows.
Four remaining additional questions stay unverified;全然–いい/良い remains
rejected phrase-component lifting. **Broader C2 ordinary quiz suitability,
modern necessity/frequency and global future uniqueness remain UNVERIFIED.**
All1629 baseline runtime RAWs/tracking/history and three source guards persist.
Qualified source membership: **1649 runtime objects /1337 words**,
671 N5/516 N4/77 N3/19 N2/54 unlabelled; **120 N4 remain**.
Strict progress: **1649 reviewed-current,two excluded reviewed blocked-media
drafts,6627 pending of8278;6629 runtime paths absent**,no partial.
Version `26fc062e779f8e9e`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/
signatures/four protected refs/exact-main CI remain separate evidence.
Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue071+ and ALL remaining safe frozen levels/families,not task completion.

The sixty-ninth full-target batch adds **20 complete actual N4 time-interval/
sequencing lessons /1044 Russian file lines** against unchanged frozen EN.
The [actual original whole review](translation-batches/069-time-intervals-and-sequencing-independent-review-001.json)
read **244 whole teaching bodies/233 whole official ordered projections/
1317 original fresh caption-reading-quiz rows/three whole RU-root rubrics**:
20 primary EN/RU pairs,93 contextual EN/RU pairs,10 frozen-only bodies and
four extra question-provider EN/RU pairs. All92 assigned windows returned.
The10947-byte stdout/native identity and actual **C1/C3 CLEAN,
C2 UNVERIFIED**,with no confirmed findings,are immutable.

The original83 individual judgments are one source direct guard plus82
additional proposals:20 direct/57 qualified/five unverified.
A pre-mutation amendment withdraws exactly five unapproved extras:
Q14 これから–今度,Q32 そろそろ–今度,Q33 そろそろ–近く,
Q34 そろそろ–近い,Q53 まず–たいてい. Insufficient evidence is
not proof that the pairs are unrelated;source 間–部屋 remains.
The [actual focused review](translation-batches/069-time-intervals-and-sequencing-independent-review-focused-002.json)
supports only those withdrawals/identity: **20 whole bodies** (18 assigned
plus additional whole EN/RU もうすぐ),**nine whole objects/nine affected
rows/three whole RU-root rubrics**,exact diff,amendment and original report.
All13 assigned windows and the extra complete pair returned;10963-byte
stdout/native identity persists. Its **C1/C3 CLEAN_BOUNDED,C2 UNVERIFIED**
remain separate;only withdrawal/identity subscope is **CLEAN_BOUNDED**.
No confirmed consequential missing direct guard or source-acceptance
blocker was established within the evidence read. Additional
これから–向こう/もうすぐ–早い/そろそろ–早い remain unverified,
not new approved guards or categorical non-overlap claims.

The **78 retained direct pairs:21 direct/57 qualified** carry only
original judgments/scope and identity,not78 fresh focused judgments.
All20 learner bodies remain RAW-identical;1314 of1317 rows are identical.
The nine fresh focused rows include three changed owners/six unchanged
providers;other1308 are retained by identity. This is not a second whole
review or1317 freshly reread corrected rows. **Broader C2 ordinary quiz
suitability,modern necessity/frequency and global future uniqueness
remain UNVERIFIED.** 一度's temporary sense is ひとたび-only;
calendar periods,manner/imminence and あいだ/ま are not flattened.
All1609 baseline runtime RAWs/tracking rows and historical evidence persist.
Qualified source membership: **1629 runtime objects /1317 words**,
671 N5/496 N4/77 N3/19 N2/54 unlabelled; **140 N4 remain**.
Strict progress: **1629 reviewed-current,two excluded reviewed blocked-media
drafts,6647 pending of8278;6649 runtime paths absent**,no partial.
Version `7380f7d1b0604a2a`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/
signatures/four protected refs/exact-main CI remain separate evidence.
Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue070+ and ALL remaining safe frozen levels/families,not task completion.

The sixty-eighth full-target batch adds **20 complete actual N4 people/
address/social-role lessons /1023 Russian file lines** against unchanged
frozen EN. The [actual original whole review](translation-batches/068-people-address-and-social-roles-independent-review-001.json)
read **198 whole teaching bodies/262 whole official ordered projections/
1297 original candidate caption-reading-quiz rows/three whole RU-root
rubrics**:20 primary EN/RU pairs,73 contextual EN/RU pairs and12
frozen-only bodies. All84 assigned windows returned completely.
The10880-byte stdout/native report and original **C1/C3 CLEAN_BOUNDED,
C2 NEEDS_FIX F1** are immutable.

F1's five missing direct protections were frozen before metadata changes:
お嬢さん–女,君–兄 and 彼–あそこ/そこ/向こう.
The [actual focused review](translation-batches/068-people-address-and-social-roles-independent-review-focused-002.json)
resolves **only F1**:16 whole teaching bodies/six whole official objects/
eight affected rows/three whole RU-root rubrics/exact diff/amendment/
original report,all12 assigned windows complete;9743-byte stdout/native
identity preserved. Its **C1/C2/C3 CLEAN_BOUNDED** verdicts are focused,
not a second whole review or blanket C2 CLEAN.

Original98 individual judgments(two direct/96 qualified) retain only
original scope/identity. Five new individual qualified judgments yield
**103 direct pairs:two direct/101 qualified**,not transitive closure.
All20 learner bodies are RAW-identical across the correction;1294 of1297
pool rows are identical. The eight fresh focused rows include three
changed owners and five unchanged providers; the other1289 are retained
by identity,not fresh semantic reading. **Broader C2 ordinary quiz
suitability,modern necessity/frequency and global future uniqueness
remain UNVERIFIED.** Standalone 女じょ daughter,letter-address 兄けい you
and rare written 彼あれ place retain exact reading/role/deictic limits,
without changing primary readings or claiming suffix/class equivalence.

All1589 baseline runtime RAWs/tracking rows and historical evidence persist.
Qualified source membership: **1609 runtime objects /1297 words**,
671 N5/476 N4/77 N3/19 N2/54 unlabelled; **160 N4 remain**.
Strict progress: **1609 reviewed-current,two excluded reviewed blocked-media
drafts,6667 pending of8278;6669 runtime paths absent**,no partial.
Version `b4cbcf44148ebcc6`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/signatures/
four protected refs/exact-main CI remain separate publication evidence.
Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority;
continue069+ and ALL remaining safe frozen levels/families,not task completion.

The sixty-seventh full-target batch adds **19 complete shapes/properties/
comparison lessons /993 Russian file lines**:16 actual N4 plus three
source-required actual N3 providers 型/式/種類, without relabelling.
The [actual independent review](translation-batches/067-shapes-properties-and-comparison-independent-review-001.json)
read **224 whole teaching bodies/233 whole official ordered projections/
1277 actual candidate caption-reading-quiz rows/three whole RU-root
rubrics**:19 primary EN/RU pairs,85 contextual EN/RU pairs and16
frozen-only bodies. All94 assigned windows and both semantic record
projections returned completely; the actual10960-byte stdout/native
report identity persists.

Actual **C1/C2/C3 CLEAN_BOUNDED** verdicts remain qualified to that
evidence. No consequential defect was reported.
**Broader C2 ordinary quiz suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED**, not relabelled CLEAN.
All111 pairs were individually assessed:nine preserved source guards
(7 direct/2 qualified) and102 additional proposals(10 direct/92 qualified).
Each same-ID reason/reading/sense/domain restriction persists, not
universal synonymy, transitive guards or ordinary necessity proof.
Predicted certainty excludes 硬い; physical コード uses2855837;
深い's far-from-home-plate guards remain baseball-only.
These do not resolve protected033空 or create geographic synonymy.
Separate 形/体/表 readings and ordinary 裏 lining/inside senses are kept.
No English line/thread/rope or wet-and-soft shortcut was adopted.
This is one whole review, not1277 whole-lesson/global recertification.

All1570 baseline runtime RAWs/tracking rows and historical evidence are
preserved. Qualified source membership: **1589 runtime objects /1277
words**,671 N5/456 N4/77 N3/19 N2/54 unlabelled; **180 N4 remain**.
Strict progress: **1589 reviewed-current,two excluded reviewed blocked-media
drafts,6687 pending of8278;6689 runtime paths absent**,no partial.
Version `f82172af12d5695b`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/signatures/
four protected refs/exact-main CI remain separate publication evidence.
Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority;
continue068+ and ALL remaining safe frozen levels/families,not task completion.

The sixty-sixth full-target batch adds **16 complete actual N4 leisure/
sports/toys/sound lessons /866 Russian file lines** against unchanged
frozen EN. The [actual independent review](translation-batches/066-leisure-sports-toys-and-sounds-independent-review-001.json)
read **113 whole teaching bodies/129 whole official projections/1258
actual candidate caption-reading-quiz rows/three whole RU-root rubrics**:
16 primary EN/RU pairs,33 contextual EN/RU pairs and15 frozen-only bodies.
All52 assigned windows returned completely; the actual10870-byte
stdout/native report identity is preserved.

**C1/C3 CLEAN; C2 UNVERIFIED**, with no confirmed repairable omission
within the evidence read. All29 direct proposals were independently
assessed individually:eight direct lexical/current-caption protections
and21 qualified conservative protections. Each actual reason/restriction
persists. No universal synonymy, transitive clique, bare unrestricted 音
fame sense or festival/calendar-holiday identity was adopted.
**Ordinary modern necessity/frequency, broader ordinary quiz suitability
and future global uniqueness remain UNVERIFIED.**
This is not blanket C2 CLEAN,1258 whole-lesson recertification,
or runtime/native/device/default/release approval.

All1554 baseline runtime RAWs/tracking rows and historical evidence are
preserved. Qualified source membership: **1570 runtime objects /1258
words**,671 N5/440 N4/74 N3/19 N2/54 unlabelled; **196 N4 remain**.
Strict progress: **1570 reviewed-current,two excluded reviewed blocked-media
drafts,6706 pending of8278;6708 runtime paths absent**,no partial.
Version `54c5285050e9254c`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/signatures/
four protected refs/exact-main CI remain separate publication evidence.
Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority;
continue067+ and ALL remaining safe frozen levels/families,not task completion.

The sixty-fifth full-target batch adds **22 complete actual N4 writing/
media/electronic-device lessons /1121 Russian file lines** against unchanged
frozen EN. The [actual original whole review](translation-batches/065-writing-media-and-electronic-devices-independent-review-001.json)
read180 assigned whole bodies plus two additional whole 場所 bodies:
**182 whole teaching bodies/209 whole official projections/1242 actual
caption-reading-quiz rows/three current RU-root rubrics**.
Original **C1/C3 CLEAN,C2 NEEDS_FIX F01** and30 individual additional-guard
judgments(two identical-variant direct/28 qualified),plus two assessed
source PC guards,remain immutable.

The [actual focused review](translation-batches/065-writing-media-and-electronic-devices-independent-review-002.json)
freshly read four whole bodies/four whole official objects/two current
full-metadata rows/three whole RU-root rubrics,the full original report,
signed pre-mutation freeze,identity proof and exact diff.
It resolves **F01/Q31字–場所** only as qualified direct lexical/actual-caption
protection: bareあざ/あざな village-section meanings can fit actual
«место; местоположение»,not a geographic meaning of bareじ,all-place
equivalence or transitive protection through所/土地.
All22 RU teaching-body bytes/1242 captions-readings-levels-types-tags and1532
accepted baseline RAWs are unchanged; only 字's exclusion header appends場所.
Original30+2 judgments carry only originalscope/identity,**not31 fresh
judgments,a second whole182-body review or1242 fresh corrected rows**.
Original10969-byte/focused9730-byte stdout/native identities persist.
**C2 qualified direct protection only;all31 additional ordinary modern
necessity/frequency,broader ordinary quiz suitability and global future
uniqueness stay UNVERIFIED.** There are33 direct pairs,not cliques.

Owner migration-complete/resume explicitly supersedes only the temporary
storage pause;historical evidence/target/verdicts remain unchanged.
Qualified source membership: **1554 runtime objects /1242 words**:
671 N5/424 N4/74 N3/19 N2/54 unlabelled; **212 N4 remain**.
Strict progress: **1554 reviewed-current,two excluded reviewed blocked-media
drafts,6722 pending of8278;6724 runtime paths absent**,no partial.
Version `35e05ae7058fb767`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/signatures/
four protected refs/exact-main CI remain separate publication evidence.
Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority;
continue066+ and ALL remaining safe frozen levels/families,not task completion.

The sixty-fourth full-target batch adds **26 complete places/institutions/
geography lessons /1487 Russian file lines**:22 actual N4 plus four required
actual N3 providers, without relabelling. The frozen EN target is unchanged.
The [actual original whole review](translation-batches/064-places-institutions-and-geography-independent-review-001.json)
read172 whole teaching bodies/169 whole official projections/1220 current
caption-reading-quiz rows/three current RU-root rubrics:26 EN/RU primary
pairs,52 EN/RU providers and16 source-only EN lessons, no article.
Actual **C1/C2/C3 NEEDS_FIX all coupledF1** and24 individually qualified
original retains remain immutable; no separate Japanese/prose defect.

The [actual focused review](translation-batches/064-places-institutions-and-geography-independent-review-002.json)
freshly read four whole bodies/three whole official objects/two current
full-metadata rows/three RU-root rubrics, the full original report, signed
freeze, exact diff and identity proof. It resolves **F1/Q25市民–人口**:
actual «население» can denote collective inhabitants, not only the headcount
explained inside 人口. This is directional caption polysemy, not numerical
equality, generic person inclusion or transitive protection.

All26 teaching-body bytes and1220 captions-readings-levels-types-tags remain
identical; only one header negative field changes. Original24 qualified
judgments/five source guards carry original scopes, not25 fresh judgments,
a second172-body review or1220 freshly reviewed corrected rows.
Original10931-byte/focused10009-byte stdout/native identities persist.
The original rubric hashes were correct; focused independent measurement
clarifies header-plus-file payload sizes versus working/Git RAW sizes,
without rewriting history or claiming another semantic review.
Focused CLEAN is limited to the exact correction; **broader C2 ordinary
quiz suitability and all25 ordinary modern necessity/frequency/global future
uniqueness stay UNVERIFIED**. Five source guards plus25 qualified additions
are30 direct protections, not cliques.

Qualified source membership: **1532 runtime objects /1220 words**:
671 N5/402 N4/74 N3/19 N2/54 unlabelled; **234 N4 remain**.
Strict progress: **1532 reviewed-current, two excluded reviewed blocked-media
drafts,6744 pending of8278;6746 runtime paths absent**, no partial.
Version `600e5cd458536a7c`; checkpoint authority null/Ready false.
All1506 baseline RAWs/tracking/history and excluded033空 are preserved.
Serialized final checks, signed main integration, actual public archives/
signatures/four protected refs and exact-main CI remain separate publication
evidence. No assets/native/device/phone/IME/media/default/package/release
authority; continue065+ and ALL remaining safe frozen levels/families.

The sixty-third full-target batch adds **20 complete actual N4 giving/
receiving/honorific lessons /1146 Russian file lines** against unchanged
frozen EN. The [actual original whole review](translation-batches/063-giving-receiving-and-honorifics-independent-review-001.json)
read199 complete teaching bodies/219 whole official projections/1194 actual
caption-reading-quiz rows/three current RU-root rubrics. The199 bodies
comprise20 EN/RU root pairs,64 EN/RU provider pairs,30 source-only EN lessons
and the whole1707-line EN formal-nouns article, not1194 whole lessons.
Actual **C1/C2/C3 CHANGES_REQUIRED all coupled to F1** and90 individually
qualified original retains remain immutable; no separate Japanese/prose
defect was confirmed.

The [actual focused review](translation-batches/063-giving-receiving-and-honorifics-independent-review-002.json)
freshly read eight whole bodies/four whole official entries/four current
metadata-caption rows/three RU-root rubrics, the full original report and
signed exact freeze. Q94あげる–やる resolves F1 across its three coupled
facets; distinctIDあげる is not protected through上げる.
Q95ご存じ–承知 independently resolves only the exact nominal-awareness
gap under1593570.1/1349480.1 and full bilingual teaching, not agreement,
forgiving, generic comprehension or ordinaryご存じする.
The original knowledge gap was UNVERIFIED, not a confirmed finding.

Original90 qualified judgments carry identity, not92 fresh judgments.
All20 learner bodies/1146 lines and1194 captions/readings/levels/types/tags
remain unchanged;1192 other whole-file/metadata identities are checked.
Only two header guard arrays changed, with four affected/provider rows
actually returned, **not1194 freshly reread amended rows or a second
whole199/201-body review**. Original10925-byte/focused10845-byte actual
stdout/native identities persist. Effective C1/C2/C3 CLEAN is restricted
to documented assigned scopes; **all92 ordinary modern necessity/frequency,
broader quiz suitability and global future uniqueness remain UNVERIFIED**.
Four otherやる interactions stay NEED_UNVERIFIED and unadopted,
not confirmed safe or missing guards. Q82/Q85/Q88 remain pre-review author
withdrawals, not reviewer resolutions; no gift-occasion clique.
Five source guards plus92 qualified additions are direct protections,
not transitive or unrestricted synonym equivalence.

Qualified membership: **1506 runtime objects /1194 words**:
671 N5/380 N4/70 N3/19 N2/54 unlabelled; **256 N4 remain**.
Strict progress: **1506 reviewed-current, two excluded reviewed blocked-media
drafts,6770 pending of8278;6772 absent runtime paths**, no partial.
Version `8165025f1f993ccb`; checkpoint authority null/Ready false.
All1486 baseline RAWs/tracking/history and protected excluded033空 remain.
Signed freezes preceded their respective changes.
Final serialized checks, signed main integration, actual public archives and
exact-main CI are separate publication proofs, not reviewer claims.
No asset/app/device/phone/IME/media/package/default/release approval.
**Continue064+ and the entire safe remaining frozen scope; full task not complete.**

Batch062 and earlier milestones below are historical.

The sixty-second full-target batch adds **25 complete changes/breaking/
continuation lessons /1327 Russian file lines** against unchanged frozen EN:
**23 actual N4 and two actual N3 words**, with no level relabeling.
The [actual original whole review](translation-batches/062-changes-breaking-and-continuation-independent-review-001.json)
read298 complete assigned teaching bodies,314 whole official objects,
all1174 actual caption/reading/quiz rows and three current RU-root rubrics.
The298 bodies are25 EN/RU root pairs,92 EN/RU provider pairs,62 source-only
EN lessons and two whole EN contextual articles, not1174 baseline bodies.
Actual **C1 PASS / C2 REVISE / C3 PASS** and64 individually qualified
retain judgments remain immutable.

The [actual focused review](translation-batches/062-changes-breaking-and-continuation-independent-review-002.json)
resolves exact062-R1 through directQ65止める–切る protection.
Its fresh scope is four complete teaching bodies,two whole official entries,
**two affected actual rows**,three currentRU rubrics and the full original
report/proposal/diff, with executed identity assertions.
Whole1310670.1/1384830.3/4 directly support switching off/termination;
not every stopped activity is cutting and not inference through消す/終わる.
Symmetric exclusion is not bidirectional lexical equivalence.
Original64 judgments/all25 bodies/all1174 captions-readings carry unchanged
identities, **not a second whole review,65 fresh semantic judgments or1174
freshly reread amended rows**.
Effective facets PASS only within their documented source scopes;
C2 is assigned text/dependencies/qualified lexical protection, not global
ordinary-quiz certification. **All65 ordinary modern necessity/frequency,
broader quiz suitability and global future uniqueness remain UNVERIFIED.**
Original10924-byte/focused8435-byte actual stdout/native identities persist.

Eight source guard declarations/seven unordered pairs plus65 additions:
72 unique direct pairs/73 declarations, without transitive cliques.
All25 complete bodies/Japanese examples/actual classifications remain.
Eleven original wrappers retained/30 unavailable destinations unwrapped;
supported self-contained explanations replace optional article navigation.
Transitivity is not intention; suffix-only uses do not freely transfer to
bare verbs; actual transitive終わる/latest最後 remain.
No new provider or asset; all1461 baseline RAWs/tracking/history preserved.

Qualified membership: **1486 runtime objects /1174 words**:
671 N5/360 N4/70 N3/19 N2/54 unlabelled; **276 N4 remain**.
Strict progress: **1486 reviewed-current, two excluded reviewed blocked-media
drafts,6790 pending of8278;6792 absent runtime paths**, no partial.
Version `a6c0541b79431b29`; checkpoint authority null/Ready false.
Signed original/resolution freezes preceded their respective changes;
original findings and exact focused resolution remain separate evidence.
Final serialized checks, signed main integration, actual public archives and
exact-main CI are separate publication proofs, not reviewer claims.
Protected excluded033空 remains C2UNVERIFIED and not media.
No asset/app/device/phone/IME/media/package/default/release approval.
**Continue063+ and the entire safe remaining frozen scope; full task not complete.**

Batch061 and earlier milestones below are historical.

The sixty-first full-target batch adds **22 complete actualN4 nature/landscape
lessons /1134 Russian file lines** against unchanged frozen EN.
The [actual original whole review](translation-batches/061-nature-and-landscapes-independent-review-001.json)
read228 assigned complete teaching bodies,271 entire official objects,
all1149 actual caption/reading/quiz rows, two complete saved native dictionary
payloads, three current RU-root rubrics and one additional fullRU有名 lesson.
The228 assigned bodies are22 EN/RU root pairs,71 EN/RU provider pairs and42
source-only EN lessons, not1149 baseline bodies.
Original C1/C3 **CLEAN**, C2 **NEEDS_REVISION** and all32 individually
qualified retain judgments remain immutable.

The [actual focused review](translation-batches/061-nature-and-landscapes-independent-review-002.json)
resolves exact061-R1 through directQ33世界–有名 protection.
Its fresh scope is four complete teaching bodies,two whole official objects,
1149 actual amended rows,three currentRU rubrics and the full original report,
with mechanical identity checks. World-famous世界 is a **の-modifying noun**
under1373860.3, not aな-adjective;有名1541620.1 is aな-adjective.
Conservative symmetric suppression is not bidirectional lexical equivalence.
Original32 judgments/all22 bodies carry unchanged identities,
**not a second whole review or33 freshly reread semantic judgments**.
Effective C2 CLEAN covers only assigned text/dependencies and individually
qualified lexical protections; original historical C2 remains NEEDS_REVISION.
**All33 ordinary modern necessity/frequency and global uniqueness UNVERIFIED.**
Original10666-byte and focused9344-byte actual stdout/native identities persist.

Actual景色 reading history retains kango/special-reading treatment without
productiveけ for景 or unrestricted historical気色 sense transfer.
Appearance/state/ceramic colour, alternate人間じんかん, mountain-forest山,
figurative林, glyph/dot/sumo星, specific花見 viewing, secondary光 and
Internet草 comparisons preserve their source/POS/reading/register limits.
No transitive category clique, paper-counter-to-leaf noun inference
or plant-branch-to-bank-branch substitution.
All22 complete bodies/Japanese examples/actualN4 classifications remain.
Nine original wrappers retained/26 unavailable destinations unwrapped;
no new provider or asset. All1439 baseline RAWs/tracking/history preserved.

Qualified membership: **1461 runtime objects /1149 words**:
671 N5/337 N4/68 N3/19 N2/54 unlabelled;299 N4 remain.
Strict progress: **1461 reviewed-current, two excluded reviewed blocked-media
drafts,6815 pending of8278;6817 absent runtime paths**, no partial.
Version `97896ffd55fe07c2`; checkpoint authority null/Ready false.
Signed original/resolution freezes preceded their respective changes;
original findings and exact focused resolution remain separate evidence.
Final serialized checks, signed main integration, actual public archives and
exact-main CI are separate publication proofs, not reviewer claims.
Protected excluded033空 remains C2UNVERIFIED and not media.
No asset/app/device/phone/IME/media/package/default/release approval.
**Continue062+ and the entire safe remaining frozen scope; full task not complete.**

Batch060 and earlier milestones below are historical.

The sixtieth full-target batch adds **24 complete N4 transport/journey
lessons /1428 Russian file lines** against the unchanged frozen EN.
The [actual single independent report](translation-batches/060-transport-and-journeys-independent-review-001.json)
read262 complete assigned teaching bodies,251 entire official objects,
all1127 actual caption/reading/quiz rows and both complete stored operator
payloads. The whole206-line occupation article is included in262;
pool rows are not1127 baseline teaching bodies.
C1/C3 are CLEAN within assigned correctness/Russian-prose scopes.
C2 is CLEAN only for assigned text/dependencies and qualified lexical/caption
protection; all36 direct proposals individually retain, no findings or repairs.
**Ordinary modern necessity/frequency for all36 and global uniqueness remain
UNVERIFIED**, not a blanket suitability or runtime acceptance certificate.
Actual successful stdout/native-final10932-byte payload identity is preserved.

The unavailable運転手 article promise becomes supported role/reading facts.
ガソリン withdraws the unsupported negative gas-frequency rule while retaining
the actual unlabelled gasoline sense1040060.6, not a replacement frequency claim.
特急 keeps genuine1454750 operator notes and two named operator examples,
not universal tariffs/speeds. The author's premature denial of those notes
was withdrawn append-only before freeze/writing, preserving the original.
Archaic通る/知る, dated汽車/電車, selected-caption普通/大丈夫,
progression運ぶ/行く, noun急/危険 and spelling-qualified船 restrictions
remain explicit; no transitive vehicle/container/circumstance clique.
Japanese route valency, recurrence, transfer particles,普通な,急ぐ forms,
train/port/ship/parking distinctions and all24 actualN4 metadata remain.
Eight available source wrappers retained/31 unavailable optional destinations
unwrapped without removing Japanese facts/readings.

Qualified source membership: **1439 runtime objects /1127 words**,
671 N5/315 N4/68 N3/19 N2/54 unlabelled;321 N4 remain.
Strict progress: **1439 reviewed-current, two excluded reviewed blocked-media
drafts,6837 pending of8278;6839 absent runtime paths**, no partial.
Version `d57b831a620f33e3`; checkpoint authority null/Ready false.
All1415 baseline RAWs/tracking/history and protected excluded033空 preserved.
The signed semantic freeze preceded learner writing.
Final serialized checks, signed main integration, actual public archives and
exact-main CI are separate publication evidence, not reviewer claims.
No new asset/app/device/phone/IME/media/package/default/release approval.
**Continue the entire remaining safe frozen scope; full task not complete.**

Batch059 and earlier milestones below are historical.

The fifty-ninth full-target batch adds **22 complete social-action/gathering
lessons /1221 Russian file lines** against the unchanged frozen EN:
**20 actual N4 roots plus required N3スピーチ/演説**, without relabeling.
The [actual original whole review](translation-batches/059-social-actions-and-gatherings-independent-review-001.json)
read191 assigned complete teaching bodies plus two additional質問 bodies,
189 whole official objects and all1103 actual caption/reading/quiz rows.
Its original C1 **NO_CONFIRMED_TEACHING_DEFECT; Q49 UNVERIFIED**,
C2 **CHANGES_REQUIRED**, C3 **CLEAN_WITHIN_READ_PROSE_SCOPE** remain immutable.
The [actual focused review](translation-batches/059-social-actions-and-gatherings-focused-review-001.json)
accepts exact F1 **Q52尋ねる–質問** and resolves F2 by removing unverified
**Q49勝つ–取る**. Withdrawal is not proof that取る never means winning.
Its fresh scope is eight complete teaching bodies,four existing entire objects
and1103 full current caption/reading/quiz rows, not a second whole review.
Limited C1/C2/C3 CLEAN resolves the assigned findings;
the original52 individually qualified judgments and22 body hashes carry forward.
Current53 directed fields equal those52 plusQ52; Q49's historical record remains.
Ordinary modern necessity/frequency/global uniqueness stay **UNVERIFIED**.

Apology, wishes, awareness/consent, restraint, caution/reprimand, asking/visiting,
guidance, care agency, celebration/sympathy, broadcasting, competition,
winning/losing and gathering agency remain fully taught.
Dated謝る/心配, nominal congratulations, reading-onlyたずねる, conditional
ご案内 knowledge and separate sumo/cards取る qualifications remain explicit.
試合 stays wago/ateji; no English-only win/acquisition or transitive clique.
One stored bounded native return supplies the complete first DigitalDaijisen
案内 entry/separateあない and only part of the second entry, not frequency.
Nine available source wrappers retained/26 unavailable optional wrappers unwrapped.
All22 bodies and1103 captions/readings are unchanged after exact metadata remedies.

Qualified source membership: **1415 runtime objects /1103 words**,
671 N5/291 N4/68 N3/19 N2/54 unlabelled.
Strict progress: **1415 reviewed-current, two excluded reviewed blocked-media
drafts,6861 pending of8278;6863 absent runtime paths**, no partial.
Version `674da6962ef93ad7`; checkpoint authority null/Ready false.
All1393 baseline RAWs/tracking/history and protected excluded033空 preserved.
Original and focused actual stdout/native-final payloads remain immutable.
Signed semantic/resolution freezes preceded their respective changes.
Final serialized checks, signed main integration, actual public archives and
exact-main CI are separate publication evidence, not reviewer claims.
No asset/app/device/phone/IME/media/package/default/release approval.
**Continue the entire remaining safe frozen scope; full task not complete.**

Batch058 and earlier milestones below are historical.

The fifty-eighth full-target batch adds **20 complete N4 memory/intention/
certainty lessons /1011 Russian file lines** against the unchanged frozen EN.
The [actual original whole review](translation-batches/058-memory-intentions-and-certainty-independent-review-001.json)
read126 complete teaching bodies,174 whole official objects and all1081
actual caption/reading/quiz rows, plus two stored bounded native returns.
Original **C1/C3 CLEAN and C2 NEEDS_REVISION remain immutable**.
The [actual focused review](translation-batches/058-memory-intentions-and-certainty-focused-review-001.json)
independently accepts the exact F1訳–説明 repair and BOTH F2 direct
やはり–また /やっぱり–また repairs.
Its fresh scope is10 whole teaching bodies,six entire objects and1081current
captions/readings; all20 body hashes carry forward unchanged.
The28 qualified direct guards retain four source fields and21 originally
supported proposals, plus three focused repairs. No second whole CLEAN
report, transitive closure or fresh25-pair semantic rereading is claimed.
Alternate/reading-only, archaic, consumption and tentative-memory limits
remain; ordinary modern necessity/frequency/global uniqueness stay **UNVERIFIED**.

Memory, intention/schedule, expectation/obligation, hypotheticalたら/ば,
grounds/explanation and decision valency remain fully taught.
The prewritingもし correction and later directもし–万一 source freeze
remain distinct historical phases; no after-review body repair.
Later parent source175 includes one additional説明-footer object;
the original actual174-object scope is not enlarged retroactively.
Nine wrappers retained/23 unavailable optional wrappers unwrapped;
unavailable article promises replaced by factual prose, not adopted providers.

Qualified source membership: **1393 runtime objects /1081 words**,
671 N5/271 N4/66 N3/19 N2/54 unlabelled.
Strict progress: **1393 reviewed-current, two excluded reviewed blocked-media
drafts,6883 pending of8278;6885 absent runtime paths**, no partial.
Version `8378ce96cf6756b8`; checkpoint authority null/Ready false.
All1373 baseline RAWs/tracking/history and protected excluded033空 preserved.
The original and focused stdout/native-final payloads are immutable.
Signed semantic/resolution freezes preceded their respective changes.
Final serialized checks, signed main integration, actual public archives and
exact-main CI are separate publication evidence, not reviewer claims.
No asset/app/device/phone/IME/media/package/default/release approval.
**Continue the entire remaining safe frozen scope; full task not complete.**

Batch057 and earlier milestones below are historical.

The fifty-seventh full-target batch adds **21 complete feelings/reactions/
attitudes lessons /1211 Russian file lines**:
**20 actual N4 roots plus required N3幸せ**, with original levels unchanged.
The [actual single independent report](translation-batches/057-feelings-reactions-and-attitudes-independent-review-001.json)
read138 complete teaching bodies,138 whole official objects and all1061
actual caption/reading/quiz rows. No consequential assigned C1/C3 defect
was found; C2 accepts the word-only dependencies and all **27 individually
qualified direct guards: nine source edges plus18 proposals**.
No findings or repairs; the original report and exact successful stdout/
native-final bytes remain immutable. Rows are not1061 whole baseline lessons.

Independently accepted exact adaptations omit only optionalびっくり
image/image_scene metadata andねっしん source-internal N3-list indirection.
Full teaching,熱心 identity and actualねっしん N4/kanaID/type:kango/kanji[]
remain; the image stays separately pending, without media authority.
Mixed気持ち on-first classification and nativeまじめ/ateji are preserved.
Reading protections are not sense equivalence; conservative bodily-feeling,
reverse bare熱い enthusiasm, outcome sadness/regret and earnest-diligence
guards retain their exact limits. No transitive clique or ordinary-frequency
certification; broader uniqueness/modern necessity remain **UNVERIFIED**.

Qualified source membership: **1373 runtime objects /1061 words**,
671 N5/251 N4/66 N3/19 N2/54 unlabelled.
Strict progress: **1373 reviewed-current, two excluded reviewed blocked-media
drafts,6903 pending of8278;6905 absent runtime paths**, no partial.
Version `00199a7e565a0693`; checkpoint authority null/Ready false.
All1352 baseline RAWs/tracking/history and protected excluded033空 preserved.
Fifteen wrappers retained/23 unavailable optional wrappers unwrapped;
signed semantic freeze preceded learner writing.
Final serialized checks, signed main integration, actual public archives and
exact-main CI are separate publication evidence, not report claims.
No new asset/app/device/phone/IME/media/package/default/release approval.
**Continue the entire remaining safe frozen scope; full task not complete.**

Batch056 and earlier milestones below are historical.

The fifty-sixth full-target batch adds **20 complete N4 health/recovery/safety
lessons /1157 Russian file lines** against unchanged frozen source.
The [actual single independent report](translation-batches/056-health-recovery-and-safety-independent-review-001.json)
read163 complete teaching bodies,168 whole official objects,
all1040 candidate captions/readings/quiz rows and two bounded native returns.
Two failed requests provided no definitions.
C1/C3 are CLEAN within assigned correctness/Russian-prose scopes.
Original **C2 NEEDS_REVISION F1/Q17** is immutable:
the [exact append-only resolution](translation-batches/056-health-recovery-and-safety-amended-authoring-001.json)
withdraws only unsupported安全–安心, retaining大丈夫 and all prose.
All20 actually reviewed teaching bodies and1040 captions/readings are identical.
**Seventeen individually qualified direct safeguards retained, Q17 withdrawn,
none unresolved**; not a new whole/focused CLEAN review or fresh rereading.
The signed resolution freeze preceded its sole header amendment.

Objective safety remains distinct from an unworried mind.
An English synonym list is not actual-caption equivalence evidence.
Mixed-reading歯医者/type:wago and具合/type:kango/actual tags are preserved.
看護婦 is explicitly obsolete/deprecated; modern看護師 is not restricted
by gender. Source-only治す staysN2; no absent provider is forced into runtime.
Medical roles, transitivity, change/result and ordinary spelling contrasts
are taught without denying dictionary overlap.
Rare standalone喉 fish and Kansai直す retain their exact restrictions.
The returned血 character/index material is not a standaloneち definition.
No transitive medical/body/method/positive-response clique, idiom-host stripping,
ordinary frequency claim or second CLEAN report.
Broader uniqueness and ordinary modern necessity/frequency remain **UNVERIFIED**.

Qualified source membership: **1352 runtime objects /1040 words**,
671 N5/231 N4/65 N3/19 N2/54 unlabelled.
Strict progress: **1352 reviewed-current, two excluded reviewed blocked-media
drafts,6924 pending,6926 absent runtime paths**, no partial.
Version `fc5bb42159c65874`; checkpoint authority null/Ready false.
All1332 baseline RAWs/tracking/history and protected excluded033空 preserved.
Five source wrappers retained/26 unavailable optional wrappers unwrapped.
Final serialized checks, signed main integration, actual public archives
and exact-main CI are separate publication evidence, not report claims.
No new asset/app/device/phone/IME/media/package/default/release approval.
Continue the entire remaining safe frozen scope.

Batch055 and earlier milestones below are historical.

The fifty-fifth full-target batch adds **20 complete N4 clothing/accessory/body
lessons /1035 current Russian file lines** against the unchanged frozen source.
The [actual single independent report](translation-batches/055-clothing-accessories-and-body-independent-review-001.json)
read168 complete teaching bodies,224 whole official objects, all1020 candidate
captions/readings and six stored bounded lexical returns.
C1/C3 are CLEAN within assigned correctness/Russian-prose scope.
Original **C2 NEEDS_REVISION** and both findings are immutable:
the [exact append-only resolution](translation-batches/055-clothing-accessories-and-body-amended-authoring-001.json)
implements original F1's directサンダル–靴 prescription and F2's Q11
ability-reference correction to1554820:2.
All20 reviewed teaching bodies and1020 captions/readings are identical;
only one header line was added.
The36 qualified safeguards comprise35 independently retained proposals plus
one independently prescribed addition, not a new whole/focused CLEAN review.
The exact resolution freeze preceded its metadata implementation.
No transitive footwear/person/clothing closure, English-gloss-only equivalence,
compound host stripping or invented historical origin is adopted.
Ordinary modern necessity/frequency and broader global uniqueness remain
**UNVERIFIED**, including archaic首/このかみ and classical美しい evidence.
木綿 material/tree/thread identities and格好 noun/adjective scopes stay distinct;
首's neck lesson does not falsely deny the independently recorded head sense.

Qualified source membership: **1332 runtime objects /1020 words**,
671 N5/211 N4/65 N3/19 N2/54 unlabelled.
Strict progress: **1332 reviewed-current, two excluded reviewed blocked-media
drafts,6944 pending,6946 absent runtime paths**, no partial.
Version `d2bb4ec8e78636e8`; checkpoint authority null/Ready false.
All1312 baseline RAWs/tracking rows and historical evidence are preserved.
Ten source wrappers retained/16 unavailable optional wrappers unwrapped;
no source-only provider forced into runtime.
Final serialized checks, signed main integration, actual public archives
and exact-main CI are separate publication evidence, not semantic report claims.
Protected excluded033空 remains the only N5 pending/C2 UNVERIFIED word,
not media. No new asset/app/device/phone/IME/media/package/default/release approval.
Continue the entire remaining safe frozen scope.

Batch054 and earlier milestones below are historical.

The fifty-fourth full-target batch adds **20 complete N4 meals/cooking/flavour
lessons /1024 Russian lines** against the unchanged frozen source.
The [actual single independent report](translation-batches/054-meals-cooking-and-flavours-independent-review-001.json)
actually read179 complete teaching bodies,196 whole official objects,
all1000 candidate captions/readings and nine stored bounded public returns.
C1/C3 are CLEAN in the assigned correctness/Russian-prose scope.
C2 is CLEAN for assigned dependencies and **35 individually retained conservative
direct guards**; no findings, withdrawals or unresolved guard IDs.
All20 reviewed bodies and metadata remain identical.
The genuine signed pre-writing freeze preceded all learner writing.
No second review, invented repair or fresh1000-baseline-body rereading is claimed.
Ordinary modern necessity/frequency and broader global uniqueness remain
**UNVERIFIED**, including rare米/metre and qualified grain/serving/proficiency/
heating/psychological caption interpretations.
Actual甘い/うまい spelling and separate味 adjective/み noun-counter/suffix
domains are not guessed from English or character glosses.
Payment senses retain their exact qualifications;焼ける potential modality
is not dropped. Generated examples/failed fetches are not lexical evidence,
and phonetic spelling does not prove historical origin.

Qualified source membership: **1312 runtime objects /1000 words**,
671 N5/191 N4/65 N3/19 N2/54 unlabelled; protected空 is the only remaining N5 word.
Strict progress: **1312 reviewed-current, two excluded reviewed runtime-blocked
media drafts,6964 pending,6966 absent runtime paths**, no partial.
Version `45b56afd82c797ad`; checkpoint authority null/Ready false.
All1292 baseline RAWs/tracking rows and historical evidence are preserved.
Nine source navigation wrappers retained/14 unavailable optional wrappers
unwrapped; no source-only provider forced into runtime.
Signed main integration/public archives/exact-main CI are separate actual
publication evidence, not linguistic-report claims.
Protected excluded033空 remains pending/C2 UNVERIFIED, separate from the
two media drafts. No new asset/app/device/phone/IME/media/default/release
approval. Continue the entire remaining safe frozen scope.

Batch053 and earlier milestones below are historical.

The fifty-third full-target batch adds **20 complete N4 housing/overnight/
household-routine lessons /1068 Russian lines** against the unchanged frozen source.
The [actual single independent report](translation-batches/053-housing-overnight-stays-and-household-routines-independent-review-001.json)
read201 assigned complete teaching bodies plus two consequential bath bodies,
208 assigned plus one additional complete official entry, and all980 actual
candidate captions/readings. C1/C3 found no actionable defect in the assigned
change scope; original **C2 CHANGES REQUIRED** and five findings are immutable.
The [exact metadata resolution](translation-batches/053-housing-overnight-stays-and-household-routines-finding-resolution-001.json)
withdraws Q7二階建て–ビル, Q20忘れ物–忘れる,
Q21忘れ物–無くす and Q35塵–少し; adds direct湯–お風呂;
and preserves **all20 complete teaching bodies**.
**45 individually qualified safeguards** comprise44 explicitly retained
proposals and one prescribed addition. No transitive bath/building/provider
closure, invented minimum-floor rule, 忘れ物する or obligatoryちり host.
Separate田舎/でんしゃ rural-house evidence retains its reading/domain limit,
not ordinary modern N4 necessity/frequency proof.
The original47-proposal freeze and Q48 supplement are unchanged; Q48 was
signed before that metadata, after initial body drafts, not before all writing.
No second review or fresh980-baseline-body rereading is invented.
Broader whole-pool uniqueness and ordinary modern necessity/frequency remain
**UNVERIFIED** outside the actual bounded judgment.

Membership: **1292 runtime objects /980 words**,
671 N5/171 N4/65 N3/19 N2/54 unlabelled; protected空 is the only remaining N5 word.
Strict progress: **1292 reviewed-current, two excluded reviewed runtime-blocked
media drafts,6984 pending,6986 absent runtime paths**, no partial.
Version `74cedfd0a5a1228e`; checkpoint authority null/Ready false.
All1272 baseline RAWs/tracking rows and historical evidence are preserved.
Final serialized checks, signed integration/public archives/exact-main CI
are recorded separately. Protected excluded033空 remains pending/C2 UNVERIFIED,
separate from the two media drafts. No new asset/app/device/phone/IME/media/
default-activation/release approval. Continue all safe frozen levels/families.

Batch052 and earlier milestones below are historical.

The fifty-second full-target batch adds **20 complete N4 household/tools/
daily-living lessons /1080 Russian lines** against the unchanged frozen source.
The [actual independent report](translation-batches/052-household-tools-and-daily-living-independent-review-001.json)
read20 primary/50 contextual complete EN/RU pairs and30 source-only comparisons,
plus the complete guitar pair (**172 bodies**),173 complete official entries
and all960 actual candidate captions/readings.
C1/C3 PASS apply within the20 lessons; original **C2 CHANGES REQUIRED** is immutable.
The [exact metadata repair](translation-batches/052-household-tools-and-daily-living-finding-resolution-001.json)
adopts 引き出し–荷物 and道具–ギター while preserving **all20 complete bodies**.
**31 individually qualified safeguards** comprise29 supported original proposals
and the two prescribed additions. Actual full named Russian «багаж» evidence,
not earlier literal-only/other-dictionary summaries, supports the knowledge-stock fit.
The guitar guard is direct «инструмент» caption protection, not a family clique.
大事–大丈夫 retains its Tochigi-dialect-only limit; ordinary N4 necessity/
frequency UNVERIFIED. Shared大事/大切 captions do not equate Japanese senses.
ガラス's card-reading warning permits separateグラス material usage.
The signed pre-bedding amendment preserves蒲団 rarity, not unsupported age.
No second review, transitive expansion or fresh940-baseline-body rereading is invented.
Broader whole-pool uniqueness, 暖房–ストーブ fit and ordinary modern necessity/
frequency remain **UNVERIFIED**; earlier historical limits are not cleared.

Membership: **1272 runtime objects /960 words**,
671 N5/151 N4/65 N3/19 N2/54 unlabelled; protected空 is the only remaining N5 word.
Strict progress: **1272 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7004 pending,7006 absent runtime paths**, no partial.
Version `57fedd851a2005e0`; checkpoint authority null/Ready false.
All1252 baseline RAWs/tracking rows and historical evidence are preserved.
Final serialized checks, signed integration/public archives/exact-main CI
are recorded separately. Protected excluded033空 remains pending/C2 UNVERIFIED,
separate from the two media drafts. No new asset/app/device/phone/IME/media/
default-activation/release approval. Continue all safe frozen levels/families.

Batch051 and earlier milestones below are historical.

The fifty-first full-target batch adds **21 complete N4 workplaces/roles/
arrangements lessons /1136 Russian lines** against the unchanged frozen source.
The [actual independent report](translation-batches/051-workplaces-roles-and-arrangements-independent-review-001.json)
read21 primary/35 contextual complete EN/RU pairs and14 source-only comparisons,
plus two additional pairs (**130 bodies**),126 complete official entries
and all940 actual metadata rows.
C1/C3 CLEAN apply within the21 lessons; original **C2 NEEDS FIX** is immutable.
The [exact bounded repair](translation-batches/051-workplaces-roles-and-arrangements-finding-resolution-001.json)
adopts five prescribed direct guards: 仕方–手/パーティー
and受付–手/道/パーティー, plus泳ぎ方（およぎかた）.
Twenty bodies are identical; all other仕方 teaching bytes are identical.
**43 qualified safeguards** comprise38 supported original proposals
and five prescribed additions. Optional Q32用事–約束 is deliberately
withdrawn for lack of independent caption-fit support, not independently
rejected or automatically disproved; its underlying fit remains UNVERIFIED.
Medium confidence for受付–道 and all original qualifications remain binding.
Shared exact-caption groups do not imply Japanese rank/preparation equivalence.
No second review, automatic clique, transitive expansion or fresh full-baseline
reading is invented. Broader caption-fit/uniqueness/ordinary modern necessity/
frequency remain **UNVERIFIED**.

Membership: **1252 runtime objects /940 words**,
671 N5/131 N4/65 N3/19 N2/54 unlabelled; protected空 is the only remaining N5 word.
Strict progress: **1252 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7024 pending,7026 absent runtime paths**, no partial.
Version `a38ee7bed6b39b87`; checkpoint authority null/Ready false.
All1231 baseline RAWs/tracking rows and historical evidence are preserved.
Final serialized checks, signed integration/public archives/exact-main CI
are recorded separately. Protected excluded033空 remains pending/C2 UNVERIFIED,
separate from the two media drafts. No new asset/app/device/phone/IME/media/
default-activation/release approval. Continue all safe frozen levels/families.

Batch050 and earlier milestones below are historical.

The fiftieth full-target batch adds **18 complete N4 communication/polite-speech
lessons /950 Russian lines** against the unchanged frozen source.
The [actual independent report](translation-batches/050-communication-and-polite-speech-independent-review-001.json)
read18 primary/34 contextual complete EN/RU pairs and18 source-only comparisons
(**122 bodies**),120 complete entries and all919 actual metadata rows.
C1/C3 CLEAN apply within the18 complete lessons; original **C2 NEEDS FIX**
remains immutable. F1/F2/F3 prescribe seven direct guards:
伝える–知らせる, 申し上げる–表現/伝える/知らせる/教える,
and相談–会議/話す. The
[exact metadata repair](translation-batches/050-communication-and-polite-speech-finding-resolution-001.json)
adopts them while preserving all18 teaching bodies by identity.
**44 individually qualified safeguards** comprise37 original proposals
and seven prescribed additions. No second review, automatic register clique,
transitive expansion or fresh full-baseline reading is invented.
POS/suru/register/rare-sense/alternate-reading/intonation limits remain binding;
the会議 addition retains medium confidence.
Broader caption-fit questions, whole-pool uniqueness and ordinary modern
necessity/frequency remain **UNVERIFIED**.

Membership: **1231 runtime objects /919 words**,
671 N5/110 N4/65 N3/19 N2/54 unlabelled; protected空 is the only remaining N5 word.
Strict progress: **1231 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7045 pending,7047 absent runtime paths**, no partial.
Version `f382ac4c68b299c5`; checkpoint authority null/Ready false.
All1213 baseline RAWs/tracking rows and historical evidence are preserved.
Final serialized checks, signed integration/public archives/exact-main CI
have separate evidence. Protected excluded033空 remains pending/C2 UNVERIFIED,
separate from the two media drafts. No new asset/app/device/phone/IME/media/
default-activation/release approval. Continue all safe frozen levels/families.

Batch049 and earlier milestones below are historical.

The forty-ninth full-target batch adds **13 complete N4 discipline/culture/
society lessons** against the unchanged frozen source.
The [actual independent report](translation-batches/049-disciplines-culture-and-society-independent-review-001.json)
read13 primary/22 contextual/three additional complete EN/RU pairs and ten
source-only comparisons (**86 bodies**),95 complete entries and all901 actual
metadata rows. C1 CLEAN/C3 ACCEPTABLE apply within the13 complete lessons;
original **C2 NEEDS_FIX** remains immutable. R049-N1/N2/N3 prescribe six direct
guards: 科学–地理/数学/歴史/経済, 歴史–話 and経済–お金.
The [exact metadata repair](translation-batches/049-disciplines-culture-and-society-finding-resolution-001.json)
adopts them while preserving all13 teaching bodies by identity.
**15 individually qualified safeguards** comprise nine original proposals
and six prescribed additions. No second review, automatic subject clique or
fresh full-baseline reading is invented. Broader caption-fit questions,
whole-pool uniqueness and ordinary modern necessity/frequency remain
**UNVERIFIED**; rare-sense/alternate-reading limitations stay binding.

Membership: **1213 runtime objects /901 words**,
671 N5/92 N4/65 N3/19 N2/54 unlabelled; protected空 is the only remaining N5 word.
Strict progress: **1213 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7063 pending,7065 absent runtime paths**, no partial.
Version `de2067e8bc992b38`; checkpoint authority null/Ready false.
All1200 baseline RAWs/tracking rows and historical evidence are preserved.
Final serialized checks, signed integration/public archives/exact-main CI
have separate evidence. Protected excluded033空 remains pending/C2 UNVERIFIED,
separate from the two media drafts. No new asset/app/device/phone/IME/media/
default-activation/release approval. Continue all safe frozen levels/families.

Batch048 and earlier milestones below are historical.

The forty-eighth full-target batch adds **16 complete N4 study/reference/school
lessons /800 Russian lines** against the unchanged frozen source.
The [actual independent report](translation-batches/048-study-reference-and-school-independent-review-001.json)
read16 primary/28 contextual complete EN/RU pairs and two source-only
comparisons (**90 bodies**),88 complete entries and all888 actual metadata rows.
C1/C3 are CLEAN within the16 lessons; original **C2 NEEDS REVISION** is immutable.
R048-N1/N2/N3 identify unsupported教育–練習,大学生–留学生 and校長–先生.
The [exact metadata repair](translation-batches/048-study-reference-and-school-finding-resolution-001.json)
withdraws those three proposals; all16 teaching bodies are identity-preserved.
**29 individually qualified safeguards** remain, not a second review or a
fresh full-baseline reading. Broader whole-pool uniqueness and ordinary modern
necessity/frequency remain **UNVERIFIED**. Dictionary exact-caption dedup
is verified; source-only/exploratory comparisons create no forced providers.

Membership: **1200 runtime objects /888 words**,
671 N5/79 N4/65 N3/19 N2/54 unlabelled; protected空 is the only remaining N5 word.
Strict progress: **1200 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7076 pending,7078 absent runtime paths**, no partial.
Version `070e2559a59b4564`; checkpoint authority null/Ready false.
All1184 baseline RAWs/tracking rows and historical evidence are preserved.
Final serialized checks, signed integration/public archives/exact-main CI
have separate evidence. Protected excluded033空 remains pending/C2 UNVERIFIED,
separate from the two media drafts. No new asset/app/device/phone/IME/media/
default-activation/release approval. Continue all safe frozen levels/families.

Batch047 and earlier milestones below are historical.

The forty-seventh full-target batch adds **12 complete safe N5 lessons**.
The [actual independent report](translation-batches/047-n5-safe-text-closure-independent-review-001.json)
read12 primary/25 contextual complete EN/RU pairs (**74 bodies**),
87 complete official entries and all872 actual metadata rows.
C1/C3 are CLEAN for the new lessons; original **C2 NEEDS FIX** stays immutable.
R047-1 independently prescribes directあの–あれ andあの–それ;
the [exact metadata repair](translation-batches/047-n5-safe-text-closure-finding-resolution-001.json)
adopts them while preserving all12 complete teaching bodies by identity.
No second review or fresh full-baseline body reread is invented.
**19 individually qualified safeguards** are retained.
Broader whole-pool semantic uniqueness and ordinary modern necessity/frequency
remain **UNVERIFIED**, not global C2 CLEAN.

Membership: **1184 runtime objects /872 words**,
671 N5/63 N4/65 N3/19 N2/54 unlabelled; **one of672 N5 words remains: 空**.
Strict progress: **1184 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7092 pending,7094 absent runtime paths**, no partial.
Version `1ba71a9ba5033842`; checkpoint authority null/Ready false.
All1172 baseline RAWs/tracking rows and historical evidence are preserved.
Final serialized checks, signed integration/public archives/exact-main CI have
separate evidence. Protected excluded033空 stays pending/C2 UNVERIFIED,
separate from the two media drafts. No new asset/app/device/phone/IME/media/
default-activation/release approval. Continue all safe frozen levels/families.

Batch046 and earlier milestones below are historical.

The forty-sixth full-target batch adds **16 complete N5 time/sequence/position
lessons**. The [actual whole report](translation-batches/046-time-sequence-positions-independent-review-001.json)
preserves C1/C3 CLEAN and original C2 NEEDS REVISION after62 assigned pairs
plus向こう,124 complete official entries and860 captions.
The [focused report](translation-batches/046-time-sequence-positions-independent-review-002.json)
reads nine pairs/11 entries/three localized RU rubrics, not a second whole
review. Identity carries forward16 bodies, not fresh whole-pool semantics.
046-R1 resolves先–向こう;046-R2 resolves by withdrawing four unsupported
proposals;046-R3 withdraws the incorrect historical-hash diagnosis and resolves
the actual EN/RU reader-domain bug. Original receipts/reports stay immutable.
One source pair plus54 qualified conservative guards are adopted;51 retain
original qualified support. New先–最近 and今–先 keep rare standalone先/さっき
limits. **Broader quiz suitability and ordinary modern necessity/frequency
remain UNVERIFIED**, not global CLEAN.

Membership: **1172 runtime objects /860 words**,
659 N5/63 N4/65 N3/19 N2/54 unlabelled; **13 of672 N5 words remain**.
Strict progress: **1172 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7104 pending,7106 absent runtime paths**, no partial.
Version `982dcba7f94b15a8`; checkpoint authority null/Ready false.
All1156 baseline RAWs/tracking rows and historical receipts remain unchanged.
Actual final checks/integration/public archives/exact-main CI have separate
evidence. Excluded033空 remains pending/C2 UNVERIFIED, separate from media.
No new assets/app/device/phone/IME/media/default-activation/release approval.
Continue047 and every safe remaining frozen level/family after046 integration.

Batch045 and earlier milestones below are historical.

The forty-fifth full-target batch adds **13 complete N5 body/health/safety
lessons** against the unchanged frozen source.
[Reviewed source045](translation-batches/045-body-health-safety-reviewed-source.json)
and [actual independent evidence](translation-batches/045-body-health-safety-independent-review.json)
record one whole46-pair/92-body/129-entry/844-caption review, including all648
new Russian lines and one complete named Russian primary entry.
C1/C3 are CLEAN for the new lessons; C2 adopted coverage/dependencies are
CLEAN and all20 qualified direct guards are supported. Broader semantic quiz
suitability and stronger modern necessity/frequency remain explicitly
UNVERIFIED, not relabelled CLEAN. Neither an obligatory extra guard nor universal
safety is established for the unadopted 死ぬ–終わる and 頭–精神/心 hypotheses.
No transitive body/people/adjective clique is endorsed.
Actual7681-byte UTF-8 stdout report, independently returned base64 and final
message content agree; these domains are not network-wire bytes.
The three-line stdout method clarification was independently assessed.

Membership: **1156 runtime objects /844 words**,
643 N5/63 N4/65 N3/19 N2/54 unlabelled; **29 of672 N5 words remain**.
Strict progress: **1156 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7120 pending,7122 absent runtime paths**, no partial.
Version `820f471d66840ea7`; checkpoint authority null/Ready false.
All1143 baseline RAWs/tracking rows and historical receipts remain unchanged.
Actual final validation/integration/public archives/exact-main CI have separate
evidence. No new assets or app/ordinary EN/device/media/default-activation/release
approval. Canonical life/occupation/safety mapping gaps are bounded to immutable
app5c000bd, live app UNVERIFIED and untouched.
Later genuine native findings may require affected-batch correction/review;
continue046 and every safe remaining frozen level/family.

Batch044 and earlier milestones below are historical.

The forty-fourth full-target batch adds **16 complete N5 arts/music/media
lessons** against the unchanged frozen source.
[Reviewed source044](translation-batches/044-arts-music-media-reviewed-source.json)
and [actual independent evidence](translation-batches/044-arts-music-media-independent-review.json)
preserve whole40-pair/59-entry/831-caption C1/C3 CLEAN, C2 NEEDS_FIX.
A focused eight-pair/eight-entry/three-Russian-primary-entry recheck resolves
four safeguards and the 組 citation erratum, and assesses three method lines.
Unique pair/official-entry evidence remains40/59, not48/67.
All16 learner bodies/831 captions and1127 baseline RAWs/tracking rows are preserved.
The current 組 reference is1397450:2; an explicit forward erratum preserves
immutable historical wrong citations rather than silently rewriting them.
**18 protections = four direct displayed-answer +14 limited decisions**;
stronger modern necessity/frequency of the14 remains UNVERIFIED/unasserted.
The actual focused return and exact-ID readback support review; its saved LF
transcript hash does not claim still-unverified native-public-event byte identity
or network-wire bytes. Successful reader evidence is separately captured.

Membership: **1143 runtime objects /831 words**,
630 N5/63 N4/65 N3/19 N2/54 unlabelled; **42 of672 N5 words remain**.
Strict progress: **1143 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7133 pending,7135 absent runtime paths**, no partial.
Version `2feceed6354d1b68`; checkpoint authority null/Ready false.
Actual final validation/integration/public archives/exact-main CI have separate
evidence. No new assets or app/ordinary EN/device/media/default-activation/release
approval. Canonical art/audio/equipment/office/sound mapping gaps are bounded
to immutable app5c000bd, live app UNVERIFIED.
Later genuine native findings may require affected-batch correction/review;
continue045 and every safe remaining frozen level/family.

Batch043 and earlier milestones below are historical.

The forty-third full-target batch adds **16 complete N5 food/tableware/object
lessons** against the unchanged frozen source.
[Reviewed source043](translation-batches/043-food-tableware-objects-reviewed-source.json)
and [actual independent evidence](translation-batches/043-food-tableware-objects-independent-review.json)
preserve whole40-pair/47-entry/815-caption C1/C3 CLEAN, C2 CHANGES REQUIRED.
The focused two-pair/two-entry recheck resolves direct ちゃわん–カップ and
supports two method lines; unique evidence remains40/47, not42/49.
All16 learner bodies/815 captions and1111 baseline RAWs/tracking rows are preserved.
The focused provenance-only finding remains verbatim; its stale requester premise
is adjudicated with the actual persisted public report event,12253 UTF-8 bytes
and exact hash—not claimed network-wire bytes or a new linguistic review.
[Provenance evidence](translation-batches/043-food-tableware-objects-provenance-adjudication-001.json)
also distinguishes delayed journal persistence from the earlier failed capture.
**Seven protections = four direct taught/caption +three limited decisions**;
stronger modern necessity/frequency of the three remains UNVERIFIED/unasserted.

Membership: **1127 runtime objects /815 words**,
614 N5/63 N4/65 N3/19 N2/54 unlabelled; **58 of672 N5 words remain**.
Strict progress: **1127 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7149 pending,7151 absent runtime paths**, no partial.
Version `5bd14414dcad4e99`; checkpoint authority null/Ready false.
Actual candidate/corrected checks passed; final validation/integration/public
archives/exact-main CI have separate evidence. No new assets or app/ordinary
EN/device/media/default-activation/release approval. Canonical dining/object/utensil
mapping gaps are bounded to immutable app5c000bd, live app UNVERIFIED.
Later genuine native findings may require affected-batch correction/review;
continue044 and every safe remaining frozen level/family.

Batch042 and earlier milestones below are historical.

The forty-second full-target batch adds **18 complete travel/movement/place
lessons:16 N5 roots and two required N4 providers**.
[Reviewed source042](translation-batches/042-travel-movement-places-reviewed-source.json)
and [actual independent evidence](translation-batches/042-travel-movement-places-independent-review.json)
preserve the whole62-pair/799-caption/123-complete-entry/51-proposal review:
original C1/C3 CLEAN, C2 NEEDS FIX, not retroactively CLEAN.
The focused17-pair/18-entry/all799-caption recheck resolves ten additions,
accepts four withdrawals and six new method lines. These pairs/entries are
subsets of the original62/123, not79/141 unique objects.
All18 learner bodies/titles and1093 baseline RAWs/tracking rows are preserved.
**57 direct protections = two source edges +17 direct taught/caption decisions
+38 limited dictionary/context decisions**; stronger modern necessity/frequency
of all38 remains UNVERIFIED/unasserted. Residual 差す–輝く and 国–外国 hypotheses
remain UNVERIFIED, without an established necessary extra guard in this boundary.

Membership: **1111 runtime objects /799 words**,
598 N5/63 N4/65 N3/19 N2/54 unlabelled; **74 of672 N5 words remain**.
Strict progress: **1111 reviewed-current, two excluded reviewed runtime-blocked
media drafts,7165 pending,7167 absent runtime paths**, no partial.
Version `4ee4c7df08855309`; checkpoint authority null/Ready false.
Actual candidate/corrected checks passed; final checks, signed integration,
public archives and exact-main CI have separate publication evidence.
No new assets or app/ordinary EN/device/media/default-activation/release approval.
The canonical `occupations` mapping gap is observed only at immutable app
`5c000bd`; concurrent live-app status remains UNVERIFIED.
Later genuine native findings can require affected-batch correction/review;
authoring of independent safe frozen content continues.

Batch041 and earlier milestones below are historical.

The forty-first full-target batch adds **25 complete core-action/making/existence
lessons: 18 N5 roots, four required N4 and three required N3 providers**.
[Reviewed source041](translation-batches/041-core-actions-making-existence-reviewed-source.json)
and [actual independent evidence](translation-batches/041-core-actions-making-existence-independent-review.json)
preserve the whole 69-pair/781-caption/80-object/67-proposal reading:
original C1/C3 CLEAN, C2 NEEDS FIX, not retroactively CLEAN.
The focused four-pair/four-object recheck resolves direct いる–要る and 上げる–貸す
guards and assesses six method lines. Cumulative unique bilingual evidence is
**69 pairs**, not 73. All 25 learner bodies and 781 titles remain unchanged.
**69 direct protections = nine source edges +17 direct taught/caption decisions
+43 limited conservative/contextual decisions**; stronger ordinary modern
necessity/frequency of all 43 remains UNVERIFIED and unasserted.
All 1068 accepted baseline RAWs/tracking rows are preserved.

Membership: **1093 runtime objects /781 words**,
582 N5/61 N4/65 N3/19 N2/54 unlabelled; **90 of672 N5 words remain**.
Fresh strict progress: **1093 reviewed-current, two excluded reviewed runtime-blocked
media drafts, 7183 pending, 7185 absent runtime paths**, no partial.
Version `e05eb558300d0602`; checkpoint authority null/Ready false.
Actual candidate/corrected checks passed; final checks, signed integration,
public archives and exact-main CI have separate publication evidence.
No new assets or app/ordinary EN/device/media/default-activation/release approval.
The six canonical-tag mapping gaps are bounded to immutable app `5c000bd`.
Later actual native findings can require affected-batch correction/review;
authoring of safe frozen content continues.

Batch040 and earlier milestones below are historical.

The fortieth full-target batch adds **25 complete connectives/frequency/degree
lessons: 22 N5 roots, one required N4 and two required N3 providers**.
[Reviewed source040](translation-batches/040-connectives-frequency-degree-reviewed-source.json)
and [actual independent evidence](translation-batches/040-connectives-frequency-degree-independent-review.json)
preserve the whole 47-pair/two-EN-only/756-caption/55-object/42-proposal review:
original C1/C2/C3 NEEDS FIX, not retroactively CLEAN. The focused seven-pair/
seven-object review resolves two missing よく guards and the まだ stage/time
explanation; また–本当 is withdrawn as unsupported. Two Russian phrases and five
method lines are independently accepted. Cumulative unique bilingual evidence
remains **47 pairs**, not 54. **43 direct protections =18 source-sense +25 limited
conservative/contextual decisions**; stronger ordinary modern necessity/frequency
of all 25 remains UNVERIFIED and unasserted.
All 1043 accepted baseline RAWs/tracking rows and 756 actual titles are preserved.

Membership: **1068 runtime objects /756 words**,
564 N5/57 N4/62 N3/19 N2/54 unlabelled; **108 of672 N5 words remain**.
Fresh strict progress: **1068 reviewed-current, two excluded reviewed runtime-blocked
media drafts, 7208 pending, 7210 absent runtime paths**, no partial.
Version `20947276cf78bbe5`; checkpoint authority null/Ready false.
Actual candidate/corrected checks passed; final checks, signed integration,
public archives and exact-main CI have separately recorded publication evidence.
No new assets or app/ordinary EN/device/media/default-activation/release approval.
Canonical concepts/conjunction/frequency/reality/sequence mapping follow-up is
confined to immutable app `5c000bd`. Later actual native findings can require
affected-batch correction/review; authoring of safe frozen content continues.

Batch039 and earlier milestones below are historical.

The thirty-ninth full-target batch adds **18 complete N5 question, address,
request and response lessons**.
[Reviewed source039](translation-batches/039-questions-address-responses-reviewed-source.json)
and [actual independent evidence](translation-batches/039-questions-address-responses-independent-review.json)
combine a whole 39-pair/731-caption/50-object review with narrow additional 嫌
evidence and a focused 11-pair/eight-object recheck of seven real corrections.
The original C1/C3 CLEAN, C2 NEEDS FIX report is preserved; all seven direct
metadata additions, one natural Russian apology and five method lines are
independently accepted. Cumulative unique bilingual evidence is 40 pairs,
not an additional full-corpus or repeated whole review.
**39 direct protections = 17 ordinary-sense +22 conservative/contextual decisions**;
ordinary modern necessity/frequency of the 22 remains UNVERIFIED and unasserted.
All 1025 accepted baseline RAWs/tracking rows and 731 actual captions are preserved.

Membership: **1043 runtime objects /731 words**,
542 N5/56 N4/60 N3/19 N2/54 unlabelled; **130 of672 N5 words remain**.
Fresh strict progress: **1043 reviewed-current, two excluded reviewed runtime-blocked
media drafts, 7233 pending, 7235 absent runtime paths**, no partial.
Version `cdf164e767e453ad`; checkpoint authority null/Ready false.
Actual candidate/corrected checks passed; final validation, integration, public
archives and exact-main CI remain separately evidenced publication operations.
No new assets or app/ordinary EN/device/media/default-activation/release approval.
Canonical `interjection`/`polite`/`request` mapping follow-up is confined to
immutable app `5c000bd`. Later actual native findings can require affected-batch
correction/review; authoring of safe frozen content continues.

Batch038 and earlier milestones below are historical.

The thirty-eighth full-target batch adds **18 complete quantity/measurement/comparison words:
16 N5 roots and two required N4 providers, 最も/最初**.
[Reviewed source038](translation-batches/038-quantities-measurements-reviewed-source.json)
and [actual independent evidence](translation-batches/038-quantities-measurements-independent-review.json)
preserve the initial 39-pair code-review reading whose 52-byte return supplied no
linguistic facet report. It is **NOT_REPORTED, not approval**. The subsequent actual
linguistic adjudication read all 18 new pairs and 12 support pairs, 713 compact captions,
68 complete candidate query-object rows and six selected dictionary ranges:
C1/C3 CLEAN, 21 direct necessities supported, three ordinary-necessity claims UNVERIFIED.
A narrow six-pair/five-range recheck independently accepts those three dictionary-grounded
guards **only as qualified conservative metadata** and four method lines.
Their ordinary contemporary necessity/frequency remains UNVERIFIED, not newly taught N5 usage.
The earlier report is not retroactively relabelled; **24 direct guards = 21 supported
necessities + three independently accepted conservative protections**.

All 1007 accepted baseline RAWs/tracking rows and all 18 full learner bodies/metadata
remain unchanged by the documentation-only qualification.
Membership: **1025 runtime objects /713 words**, word levels
524 N5/56 N4/60 N3/19 N2/54 unlabelled; **148 of 672 N5 words remain**.
Fresh strict progress: **1025 reviewed-current, two excluded reviewed runtime-blocked
media drafts, 7,251 pending, 7,253 absent runtime paths**, no partial.
Version `c3444eaf9a65b497`; checkpoint authority null/Ready false.
Candidate manifest/validator/124 tests/budget passed; final checks, signed main integration,
actual public archives and exact-main CI have separate receipts.
No new assets or app/ordinary EN/device/media/default-activation/release approval.
Canonical tag gaps are reported only at immutable app `5c000bd`.
Later actual native findings can require affected-batch correction/review;
continue every remaining safe frozen level/family without a speculative stop gate.

Batch 037 and earlier milestones below are historical.

The thirty-seventh full-target batch adds **16 complete N5 communication/learning words**.
[Reviewed source037](translation-batches/037-communication-learning-reviewed-source.json)
and [actual independent review](translation-batches/037-communication-learning-independent-review.json)
combine a whole review of 35 complete EN/RU pairs, 695 compact captions,
61 complete selected lexical objects and four selected dictionary ranges with a
focused recheck of five complete pairs, five fresh selected ranges and three guidance
lines/one link. The initial C2 NEEDS_FIX and both unverified guard rationales are preserved.
The recheck resolves the added 作文–書く guard, retains 覚える–勉強 using exact new
Japanese/Russian acquisition-sense evidence, and withdraws unestablished 覚える–習う:
**24 direct guards**, not a transitive clique. The Russian dictionary sense has no
usage example; no invented collocation is claimed as attested.

All 991 accepted baseline RAWs/tracking rows, all 16 learner bodies/695 captions
and the full excluded C2-unverified 空 remain unchanged by the metadata correction.
Membership: **1007 runtime objects**, including 695 words;
word levels 508 N5/54 N4/60 N3/19 N2/54 unlabelled; **164 of 672 N5 words remain**.
Fresh strict progress: **1007 reviewed-current, two excluded reviewed runtime-blocked
media drafts, 7,269 pending, 7,271 absent runtime paths**, no partial.
Version `78b9999fcefcb597`; checkpoint authority null/Ready false.
Corrected candidate: validator 0 errors, 124 tests OK in 30.812s and budget passed;
final checks, signed main integration, actual public archives and exact-main CI have
separate receipts. Canonical `memory`, `requests`, `study` IDs stay stable;
raw fallback is observed only at pinned app `5c000bd`, not a current-app/device claim.
No new assets or app/ordinary EN/device/media/default-activation/release approval.
Later real native findings can require affected-batch correction/re-review;
continue every remaining safe frozen level/family without a speculative stop gate.

Batch 036 and earlier milestones below are historical.

The thirty-sixth full-target batch adds **14 complete N5 state-change/operation words**.
[Reviewed source 036](translation-batches/036-state-changes-operations-reviewed-source.json)
and its [independent review](translation-batches/036-state-changes-operations-independent-review.json)
combine one actual whole review with one narrow consequential-resolution recheck.
The whole reviewer read 34 full EN/RU pairs, 679 compact captions, 55 complete selected
lexical objects and four selected dictionary ranges. It retained 24 direct safeguards,
but returned C2/C3 NEEDS_FIX and an unverified 開く–広い question—not blanket approval.
The focused reviewer read five full pairs, two complete opening objects, two fresh
dictionary ranges, both append-only errata and four new guidance lines.
It resolved the dictionary-sense wording and actual-caption misquotation, established
no additional 開く–広い guard, and independently retained two newly evidenced direct
opening/beginning/ending safeguards: **26 direct pairs total**, not a transitive clique.
Modern frequency of the euphemistic ending use remains unverified, not new N5 teaching.

All 977 baseline runtime RAWs/tracking rows and the full excluded C2-unverified 空
remain unchanged. Membership is **991 runtime objects** — 141 kanji/679 words/
141 strokes/2 articles/22 counter files/one grammar set/2 scene catalogs/3 images.
Fresh strict progress: **991 reviewed-current, two excluded reviewed runtime-blocked
media drafts, 7,285 pending, 7,287 absent runtime paths**, no partial.
Word levels: 492 N5/54 N4/60 N3/19 N2/54 unlabelled; **180 of 672 N5 words remain**.
Version `c7e6d0d7021e3248`; checkpoint authority null/Ready false.
Corrected candidate: validator 0 errors, 124 tests OK in 31.927s;
budget 999 files/1008 entries/2,810,316 retained/2,828,531 inflated/1,415,548 ZIP bytes.
Final checks, main integration, actual public archives and exact-main CI have separate receipts.
The canonical `attachment` tag stays stable; raw fallback is observed only at pinned
app `5c000bd`, not asserted for the concurrent current app or a device.
README, old ordering and current C6 links now separate reviewed source from ordinary activation;
historical receipts and five real native Word Type paths are preserved.
No new assets, app/ordinary EN edits, phone/IME/playback/new audio-package/C6/C7/default
activation/release/checkpoint authority. Later real findings may require affected-batch
correction/re-review; continue every remaining safe frozen level/family meanwhile.

Batch 035 and earlier milestones below are historical.

The thirty-fifth full-target batch adds **14 complete N5 daily-life/work/rest words**.
[Reviewed source 035](translation-batches/035-daily-life-work-rest-reviewed-source.json)
and its [independent review](translation-batches/035-daily-life-work-rest-independent-review.json)
combine one actual whole review with one narrow consequential-fix recheck.
The whole reviewer read 27 full EN/RU pairs, 665 compact captions, 34 complete
selected lexical rows and four selected dictionary ranges, retaining all 15 proposals.
Its C2 finding requires the direct 家庭–門 safeguard: exact-written 門（かど）
has a family sense. The focused changed-snapshot recheck resolves that one addition
after two full pairs, three complete selected objects and four new guidance lines.
C1/C3 and the other 15 decisions carry forward because all bodies/captions and
976 other runtime RAWs are unchanged; this is not a second whole review.

All 963 baseline runtime RAWs/tracking rows and the full excluded C2-unverified 空
remain unchanged. Membership is **977 runtime objects** — 141 kanji/665 words/
141 strokes/2 articles/22 counter files/one grammar set/2 scene catalogs/3 images.
Fresh strict progress: **977 reviewed-current, two excluded reviewed runtime-blocked
media drafts, 7,299 pending, 7,301 absent runtime paths**, no partial.
Word levels: 478 N5/54 N4/60 N3/19 N2/54 unlabelled; **194 of 672 N5 words remain**.
Version `b4d1c08e122a2bbb`; checkpoint authority null/Ready false.
Corrected candidate checks: validator 0 errors, 124 tests OK in 30.265s;
budget 985 files/994 entries/2,769,242 retained/2,785,924 inflated/1,394,984 ZIP bytes.
Final checks, main integration, archive and exact-main CI have separate receipts.
No new assets or canonical tags, app/ordinary EN edits, phone/IME/playback/new
audio-package/C6/C7/default activation/release/checkpoint authority.
Continue every remaining safe frozen level/family.

Batch 034 and earlier milestones below are historical.

The thirty-fourth full-target batch adds **12 complete N5 hygiene/household words**.
[Reviewed source 034](translation-batches/034-hygiene-household-reviewed-source.json)
and its [independent review](translation-batches/034-hygiene-household-independent-review.json)
bind one actual whole three-facet review: 12 primary/18 supporting full EN/RU pairs,
651 compact captions, 33 complete selected lexical rows and nine selected ranges
from eight pages. The complete 6,185-byte native report and successful reading
trace are preserved; C1/C2/C3 are CLEAN within this twelve-unit source boundary.
All seven direct guards are retained; no cleaning/category/transitive clique is added.
The age-spelling frequency of 歯 is still unverified, not taught as primary N5.

All 951 older runtime RAWs/tracking rows and the full excluded C2-unverified 空 draft
are unchanged. Membership is **963 runtime objects** — 141 kanji/651 words/
141 strokes/2 articles/22 counter files/one grammar set/2 scene catalogs/3 images.
Fresh strict progress: **963 reviewed-current, two excluded reviewed runtime-blocked
media drafts, 7,313 pending, 7,315 absent runtime paths**, no partial.
Word levels: 464 N5/54 N4/60 N3/19 N2/54 unlabelled; **208 of 672 N5 words remain**.
Version `8544136ac90cafb4`; checkpoint authority null/Ready false.
Candidate checks: validator 0 errors, 124 tests OK in 29.284s;
budget 971 files/980 entries/2,732,926 retained/2,749,608 inflated/1,376,093 ZIP bytes.
Final checks, source integration, archive and exact-main CI have separate receipts.
At exact old app pin `5c000bd` only, newly exposed `facilities` lacks an explicit
localized hint mapping; retain the ID and record app follow-up, not a current-app claim.
No new assets or phone/IME/playback/new audio-package/C6/C7/default activation/
release/checkpoint authority. Continue every remaining safe frozen level/family.

Batch 033 and earlier milestones below are historical.

The thirty-third full-target batch authors 19 complete N5 nature/outdoor texts.
[Reviewed source 033](translation-batches/033-nature-outdoor-activity-reviewed-source.json)
adopts **18 runtime words**; the complete, unchanged
[空 draft](translation-drafts/033-nature-outdoor-activity/words/空.md)
stays excluded and **C2 UNVERIFIED**, not accepted or removed from the frozen target.
Its remote-place sense does not yet establish or reject the exact Russian
далеко/вдали/далёкий caption overlaps. It remains one of the pending paths,
not a third reviewed runtime-blocked media draft. Safe independent authoring continues.

The actual whole reviewer read 19 primary/20 supporting pairs, 640 compact captions,
41 selected complete lexical rows and five selected sections. Its oversized full
native report was not opened from OS temp; visible C1/C3 CLEAN and C2 NEEDS FIX
labels and actual successful reading trace are preserved with that explicit limit.
The fully available focused report independently retains 17 original pairs,
requires four further direct safeguards and leaves two sky-caption claims unverified.
The changed-snapshot recheck returns no significant issues after eight full pairs,
eight semantic labels, three lexical rows, six new selected sections and mechanical
951-runtime/639-row checks. This supports the **18-unit runtime boundary only**,
not CLEAN for the excluded draft or a fresh whole-batch review.
All 19 original learner bodies, 639 remaining captions/readings and 933 baseline
RAWs remain unchanged through the correction. Runtime has **18 direct guards**.

Membership: **951 runtime objects** — 141 kanji/639 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images.
Fresh strict progress: **951 reviewed-current, two excluded reviewed runtime-blocked
media drafts, 7,325 pending, 7,327 absent runtime paths**, no partial.
The separate complete unverified 空 draft is inside pending, not additional membership.
Word levels: 452 N5/54 N4/60 N3/19 N2/54 unlabelled; **220 of 672 N5 words remain**.
Version `8a1515166740e2bd`; checkpoint authority null/Ready false.
Corrected checks: validator 0 errors, 124 tests OK in 31.551s;
budget 959 files/968 entries/2,704,908 retained/2,721,590 inflated/1,360,862 ZIP bytes.
Final checks, source integration, archive and exact-main CI have separate receipts.
At pinned app `5c000bd` only, `activity`, `animals`, `leisure`, `motion` also
lack explicit localized cases. Preserve IDs; app follow-up only, concurrent app untouched.
No new assets, paid media, phone/IME/playback/new audio-package/C6/C7/default
activation/release/checkpoint authority. Continue every remaining safe level/family.

Batch 032 and earlier milestones below are historical.

The thirty-second full-target source batch adds 27 complete travel, place and
transport word articles: 26 N5 roots and the mandatory N4 corner provider 隅.
[Batch 032 reviewed source](translation-batches/032-travel-places-transport-reviewed-source.json)
and its [cumulative independent record](translation-batches/032-travel-places-transport-independent-review.json)
preserve the actual initial 27-primary/21-supporting complete-pair, 621-caption
and 57 selected-object-row review. Initial C2 UNVERIFIED remains immutable.
The focused seven-pair/seven-label/six-repeated-object recheck, actual short
Japanese dictionary subsection and pinned app source resolve the bare 門／かど
question with three direct 家/家族/庭 additions. All 23 guards are direct;
the cumulative unique complete-pair count is 48, not all 50 available fingerprints.
All 933 learner bodies, 621 captions/readings and 906 baseline RAWs are unchanged
through the metadata correction. Active guidance preserves the observed
optional-reading boundary and per-sense spelling restriction.

Membership is 933 runtime objects: 141 kanji/621 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images. Fresh strict progress:
933 reviewed-current, no partial, two excluded reviewed runtime-blocked drafts,
7,343 pending and 7,345 absent runtime paths. Word levels are
434 N5/54 N4/60 N3/19 N2/54 unlabelled; 238 of 672 frozen N5 words remain.
Version `5d758becdc2891a3`; checkpoint authority null/Ready false.
Corrected-candidate serialized checks: validator 0 errors, 124 tests OK in 29.428s;
budget 941 files/950 entries/2,658,751 retained/2,675,433 inflated/1,336,507 ZIP bytes.
Final checks, source integration, desktop archive and exact-main CI have separate receipts.
Exact pinned app `5c000bd` lacks localized cases for new `buildings`, `entertainment`,
`shopping`, `swimming` and previous `comparison`, `distance`, `speed`; they fall
through as raw tags. Reported app follow-up only, not a concurrent-app modification
or current-dirty-tree inspection. No new assets, paid generation, phone/IME/playback/
new audio-package/C6/C7/activation/release/checkpoint authority follows.
Continue all remaining safe frozen levels and families, including excluded listening drafts.

Earlier accepted milestones below are historical.

The thirty-first full-target source batch adds 31 complete distance, speed,
position and direction word articles: 26 N5, three N4 and two N3.
[Batch 031 reviewed source](translation-batches/031-distance-speed-direction-reviewed-source.json)
and its [cumulative independent record](translation-batches/031-distance-speed-direction-independent-review.json)
preserve the actual initial 32-primary-pair/594-caption/63-object review and
39 supporting Russian bodies for C2, separately from the fresh seven-pair/
seven-label/seven-repeated-object recheck. Supporting English bodies were not
all read; this is not 71 fully reviewed bilingual pairs.
Three direct missing guards 横–近く and 向こう–ほか/他 are resolved; the author
withdraws insufficiently supported 速い–易しい metadata without declaring an
absolute spelling ban. The 67 remaining safeguards are direct assessments.
Initial C2 NEEDS FIX remains historical; the focused all-CLEAN return and
unchanged-body/title evidence support cumulative scoped textual acceptance.
The original sync reviewer could not resume; one fresh narrower reviewer ran afterward.
The exact one-phrase 川上/downstream correction is fully rereviewed and its
current tracking updated; the other 874 baseline runtime RAWs remain unchanged.
Historical receipts and unchanged tracking rows are preserved.

Membership is 906 runtime objects: 141 kanji/594 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images. Fresh strict progress:
906 reviewed-current, no partial, two excluded reviewed runtime-blocked drafts,
7,370 pending and 7,372 absent runtime paths. Word levels are
408 N5/53 N4/60 N3/19 N2/54 unlabelled; 264 of 672 frozen N5 words remain.
Version `36b8a5c1bbb4b3ed`; checkpoint authority null/Ready false.
Corrected-candidate serialized checks: validator 0 errors, 124 tests OK in 28.994s;
budget 914 files/923 entries/2,597,051 retained/2,613,733 inflated/1,303,376 ZIP bytes.
Final checks, source integration, desktop archive and exact-main CI have separate receipts.
The three new canonical word-tag IDs `comparison`, `distance`, `speed` have
app mappings UNVERIFIED, not established missing; the concurrent app stays untouched.
No new assets, paid generation, phone/IME/playback/new audio-package/C6/C7/
activation/release/checkpoint authority follows. Continue every remaining safe
frozen level and family, including honest excluded listening drafts.

The thirtieth full-target source batch adds 22 complete N5 skill, preference,
interest and practical-evaluation word articles.
[Batch 030 reviewed source](translation-batches/030-skill-interest-evaluation-reviewed-source.json)
and its [cumulative independent record](translation-batches/030-skill-interest-evaluation-independent-review.json)
preserve the actual initial 54-pair/563-answer-row review separately from the
fresh three-pair/three-row focused recheck. The initial reviewer read 39 required
selected lexical query objects plus two additional objects; the focused reviewer
read three repeated objects, not three new lexemes. All 49 original direct guards
were retained. Initial C2 findings remain immutable; the exact correction adds
only direct 大切–大きい/大きな guards, giving 51 cumulative safeguards.
The corrected return is C1/C2/C3 CLEAN within its focused scope, supporting
cumulative scoped textual acceptance across 54 unique complete pair paths.
All 853 accepted baseline runtime RAWs and earlier tracking rows are unchanged.
Two new active guidance lines address actual simplified-HTML loss of Japanese
span/ruby content; both were independently read.

Membership is 875 runtime objects: 141 kanji/563 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images. Fresh strict progress:
875 reviewed-current, no partial, two excluded reviewed runtime-blocked drafts,
7,401 pending and 7,403 absent runtime paths. Word levels are
382 N5/50 N4/58 N3/19 N2/54 unlabelled; 290 of 672 frozen N5 words remain.
Version `ef6742b6f5b62e67`; checkpoint authority null/Ready false.
Corrected-candidate serialized checks: validator 0 errors, 124 tests OK in 31.802s;
budget 883 files/892 entries/2,511,772 retained/2,528,454 inflated/1,259,693 ZIP bytes.
Final checks, source integration, desktop archive and exact-main CI have separate receipts.
The five newly adopted canonical word-tag IDs `ability`, `atmosphere`, `desire`,
`preference`, `preferences` have app mappings UNVERIFIED, not established missing;
the concurrent app stays untouched.
No new assets, paid generation, phone/IME/playback/new audio-package/C6/C7/
activation/release/checkpoint authority follows. Continue every remaining safe
frozen level and family, including honest excluded listening drafts.

The twenty-ninth full-target source batch adds 25 complete weather, taste and
condition word articles: 24 N5 and the actual N3 negative-answer provider 苦しい.
[Batch 029 reviewed source](translation-batches/029-weather-taste-condition-reviewed-source.json)
and its [cumulative independent record](translation-batches/029-weather-taste-condition-independent-review.json)
preserve the actual initial 43-pair/541-answer-row/35-lexical-object review and
the fresh focused three-pair/three-row/one-repeated-object recheck separately.
Together they support C1/C2/C3 CLEAN across 43 unique complete EN/RU pair paths,
not a fresh 43-pair or 541-semantic-row recheck. Initial C2/C3 findings remain
immutable. The corrections add a moderate conservative direct 寒い–弱い guard
and verified 下手（へた）comparison reading; all 21 original guards are retained.
No category/transitive clique or direct Japanese–Russian cold-joke attestation
is claimed. All 828 baseline runtime RAWs and earlier tracking rows are unchanged.
Seven new methodological lines were independently read across the two reviews:
four on kana-only/homonym selection and three on verified comparison readings.

Membership is 853 runtime objects: 141 kanji/541 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images. Fresh strict progress:
853 reviewed-current, no partial, two excluded reviewed runtime-blocked drafts,
7,423 pending and 7,425 absent runtime paths. Word levels are
360 N5/50 N4/58 N3/19 N2/54 unlabelled; 312 of 672 frozen N5 words remain.
Version `ccfb8fceb5c857bf`; checkpoint authority null/Ready false.
Actual final serialized checks: validator 0 errors, 124 tests OK in 44.704s;
budget 861 files/870 entries/2,447,460 retained/2,464,142 inflated/1,227,330 ZIP bytes.
Source integration, desktop archive and exact-main CI have separate actual receipts.
The five newly adopted canonical word-tag IDs `condition`, `difficulty`,
`evaluation`, `taste`, `temperature` have app mappings UNVERIFIED, not
established missing; the concurrent app stays untouched.
No new assets, paid generation, phone/IME/playback/new audio-package/C6/C7/
activation/release/checkpoint authority follows. Continue every remaining safe
frozen level and family, including honest excluded listening drafts.

The twenty-eighth full-target source batch adds 33 complete colour/shape/size and
related word articles: 27 N5 and six actual negative-answer providers. The frozen
source remains EN `6af98cb...`. [Batch 028 reviewed source](translation-batches/028-colour-shape-size-reviewed-source.json)
and its [cumulative independent record](translation-batches/028-colour-shape-size-independent-review.json)
distinguish the actual initial 59-pair/516-answer-row review from the focused
10-pair/19-row recheck; together they cover 61 unique complete EN/RU pairs.
Initial C2/C3 findings remain immutable. The focused reviewer returns C1/C2/C3
CLEAN for the corrections and supports cumulative scoped textual acceptance.
Exactly 41 previously accepted plus four newly adjudicated direct guards remain;
six questionable proposals were withdrawn and one rejected proposal removed,
not declared universally impossible. No category/transitive clique was added.
793 baseline runtime RAWs are unchanged; the other two changes are exactly
reversible navigation wrappers in 土地/輝く, with earlier adaptations preserved.

Membership is 828 runtime objects: 141 kanji/516 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images. Fresh strict progress:
828 reviewed-current, no partial, two excluded reviewed runtime-blocked drafts,
7,448 pending and 7,450 absent runtime paths. Exactly 336 of 672 frozen N5 words
are adopted; 336 N5 words and every other pending family remain in scope.
Version `01fc236dddbb5efe`; checkpoint authority null/Ready false.
Corrected-candidate serialized checks: validator 0 errors, 124 tests OK in 32.569s,
budget 836 files/845 entries/2,380,105 retained/2,396,787 inflated/1,192,811 ZIP bytes.
Final checks, source integration, desktop archive and exact-main CI are separate receipts.
The eight newly adopted word-tag IDs `behavior`, `character`, `cleaning`,
`description`, `dimension`, `length`, `property`, `shape` have app mappings
UNVERIFIED, not established missing. The concurrent app remains untouched.
No new assets, paid generation, phone/IME/playback/C6/C7/activation/release
authority follows. Continue every remaining safe frozen level and family.

The twenty-seventh full-target source batch adds 14 complete N5 numeral word
articles without changing any of the 781 baseline runtime RAW objects.
[Batch 027 reviewed source](translation-batches/027-numeral-words-reviewed-source.json)
and its [independent report](translation-batches/027-numeral-words-independent-review.json)
bind the actual signed candidate, all 39 complete EN/RU pairs, all 483 combined
word-title/metadata/guard rows and 14 complete selected lexical objects.
One read-only reviewer returned explicit C1/C2/C3 CLEAN within this scope, with
no required fixes; this is not 483 whole-body or whole-corpus/native acceptance.
The nine numeral/general-count exclusions are valid conservative direct pairs;
the ゼロ–零 pair is valid but defensively redundant where exact-title deduplication
already applies. No unit/date/category cliques or transitive guards were added.

Membership is 795 runtime objects: 141 kanji/483 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images. Fresh strict progress:
795 reviewed-current, no partial, two excluded reviewed runtime-blocked drafts,
7,481 pending and 7,483 absent runtime paths. The word pool includes 309 of 672
frozen N5 words; 363 N5 words and every other pending family remain in scope.
Version `d449a612af670113`; checkpoint authority null/Ready false.
Actual final serialized checks: validator 0 errors, 124 tests OK in 37.494s,
budget 803 files/812 entries/2,294,558 retained/2,311,240 inflated/1,148,688 ZIP bytes.
Source integration/public archive/exact-main CI are separately evidenced.
Canonical tag `quantity` is new to the adopted word pool; its app hint remains
UNVERIFIED, not an established missing mapping. The concurrent app was untouched.
No new assets, paid generation, phone/IME/playback/C6/C7/activation/release
authority follows. Continue the entire frozen corpus after this milestone.

The twenty-sixth full-target source batch adds29complete kanji and29RAW-identical
licensed frozen strokes. [Batch026 reviewed source](translation-batches/026-n5-kanji-closure-reviewed-source.json)
binds119affected paths:58new objects,60navigation-only old bodies and日's one-line
third-foil amendment;662other baseline RAW objects remain unchanged.

The whole-batch read-only reviewer actually read all108complete EN/RU pairs, all141kanji
answer rows,59scoped word rows,29complete XML records,15radical rows and13dictionary
main entries. Its actual returned overall verdict is “No significant issues found in
the reviewed changes.” It did not return separate facet grades. Actual public messages
and completed BEGIN/END/hash markers substantiate coverage; requests alone are not proof.
The synchronous reviewer could not receive follow-up. One subsequent narrowly scoped
read-only adjudication read ten complete pairs and returns explicit C1/C2/C3 CLEAN only
for the disputed claims/five foil changes/reverse校→学/日 amendment. It is not a second
108-pair review. Both actual scopes and the reporting limit remain explicit in the
[independent record](translation-batches/026-n5-kanji-closure-independent-review.json).

Five source foils change;82other directed source edges remain. The 多/高 alternatives
are conservative valid choices, not uniquely necessary replacements or universal
equivalences. Historical source-only reading/register/etymology claims remain UNVERIFIED
and are not asserted in RU. Canonical readings/IDs/tags/levels and substantive Japanese
examples remain. Optional absent navigation is plain text, never an English placeholder.

Membership781:141kanji/469words/141strokes/2articles/22counterfiles/onegrammarset/
2scenecatalogs/3images; kanji80N5/49N4/11N3/1N2. All80frozenN5kanji are now present,
not allN5words or all8278objects. Fresh strict progress:781reviewed-current, no partial,
two reviewed runtime-blocked drafts,7,495pending and7,497runtimepathsabsent.
Version `b99a20143288672b`; checkpointauthoritynull/Readyfalse.
Actual initial serial checks:0errors/124tests27.543s;789files/798entries/2264099retained/
2280781inflated/1131944localZIPbytes. Final checks and desktop archive/exact-main CI are
separate actual receipts. No new images/scenes/audio, device/IME/playback/newpackage/
C6/C7/ordinaryactivation/release/checkpoint authority follows. Existing app-tag gaps
remain unresolved; concurrent app untouched. Continue remainingN5words and every
safe frozen family, with frequent reviewed-source integration.

Earlier accepted milestones below are historical.

The twenty-fifth full-target source batch adds full重 and35complete word articles,
plus one RAW-identical licensed frozen重stroke.
[Batch025 reviewed source](translation-batches/025-heavy-support-vocabulary-reviewed-source.json)
binds48affected runtime paths:37new objects and13useful wrappers across11old bodies.
All675other baseline RAW objects remain unchanged. One bounded read-only reviewer
actually read all58complete RU/EN pairs, all469word/112kanji title/guard rows,
88queries/114complete matching-object occurrences, both complete重/気XML records
and the exact cited spelling, quantity, material and reading-classification evidence.
This is not581whole-body or full-corpus/native-human acceptance.

All three source facets pass, with an explicit historical qualification:
the ENclaim thatおも.なうis archaic/dictionary-only or specifically means
“to take seriously” remains UNVERIFIED. RU preserves the reading without that assertion.
All19original word edges and重's three foils remain;17individually reviewed Russian
direct pairs are added, not transitive cliques. Source IDs/levels/types/tags/readings
and all substantive examples remain. Named気dictionary systems, quantity clauses,
spelling-specific Notes, mental-life/material/group distinctions and actualtransitive終わる
are qualified rather than simplified into false universal rules.

Current membership723:112kanji/469words/112strokes/2articles/22counterfiles/
onegrammarset/2scenecatalogs/3images. Fresh strict8278-entry progress:723reviewed-current,
no partial, two reviewed runtime-blocked drafts,7,553pending and7,555runtimepathsabsent.
Kanji74N5/33N4/5N3 still leave 名・子・学・小・校・高 absent.
Actual serial checks:0errors/124tests29.720s; budget731files/740entries/
2118980retained/2135662inflated/1058981localZIPbytes; version `191af32fbe5095ba`.
The initial27author-side validation failures remain honest historical evidence;
all exact fixes retained Japanese teaching and did not weaken validators.
Public archive/exact-main CI follow separately. The
[actual app follow-up](translation-batches/025-heavy-support-vocabulary-app-tag-followup.json)
and earlier tag gaps remain unresolved; canonical IDs and the concurrent app are untouched.
No phone/IME/playback/newmedia/packageaudio/C6/C7/activation/release/checkpoint authority
follows. Continue the actual29-kanji support component, remainingN5 and every safe frozen family.

Earlier accepted milestones below are historical.

The twenty-fourth full-target source batch adds complete動・夜・広・度・病 cards,
four full word articles and five RAW-identical licensed frozen-source strokes.
[Batch024 accepted source](translation-batches/024-motion-night-space-reviewed-source.json)
binds26affected runtime paths:14new objects and thirteen meaningful link wrappers across
twelve old bodies. All660other baseline RAW objects remain unchanged. After a generic
synchronous diff-review response supplied no reading-scope evidence and could not be
resumed, one bounded read-only evidence review actually read32assigned complete RU/EN
pairs plus 入院/時,34unique pairs, and all434word/111kanji title/guard rows.
All three source-text facets are CLEAN; no findings or consequential unverified claims
remain within this bounded reading scope. This is not545whole-body or full-corpus review.

The15directed kanji edges retain fourteen source edges; only 動:行→男 changes, because
ordinary car/clock translations can overlap 行's «идти; ехать». Four individually
reviewed direct word guards are 広い–大きい and 今度–最近/近頃/このごろ, without
transitive cliques. Complete source readings, examples, levels and canonical IDs remain.
The 病 affix explanation distinguishes actual position, lexical spelling and dictionary
notation; 恋病's two attested readings do not establish universal 病み spelling.
Current membership686:111kanji/434words/111strokes/2articles/22counterfiles/
onegrammarset/2scenecatalogs/3images. Fresh strict8278-entry progress:686reviewed-current,
no partial, two reviewed runtime-blocked drafts,7,590pending and7,592runtimepathsabsent.
Kanji74N5/32N4/5N3 still leave 名・子・学・小・校・高 absent.
Actual final serial checks:0errors/124tests31.403s; budget694files/703entries/
2009904retained/2026586inflated/1005053localZIPbytes; version `dc1555f59e7dc259`.
Public desktop archive/exact-main CI follow separately. Actual app fallback for canonical
`i-adjective`, `health`, `place` remains unresolved; earlier023tag gaps also remain.
IDs retained and concurrent app untouched. No phone/IME/playback/media/packageaudio/
C6/C7/activation/release/checkpoint authority follows. Continue every safe frozen family.

The twenty-third full-target source batch adds full会・公・力・店・持・特・社・道・駅
cards,13complete word articles and nine RAW-identical licensed frozen-source strokes.
[Batch023 accepted source](translation-batches/023-n5-support-foundations-reviewed-source.json)
binds36affected paths:31new runtime objects and five exact wrappers across five old bodies;
all636other baseline RAW objects remain unchanged. Actual first independent review read
49assigned completeRU/ENpairs plus 左右/旅行,51unique pairs, and all430word/106kanji
title/guard rows. Its one cross-facet finding and four unsupported frequency/register
qualifiers were saved before a separate signed correction freeze. A fresh focused reviewer
read six complete pairs, confirmed the exact 力–左右 guard and four neutralizations,
and verified667unchanged runtime objects/46unchanged pair bodies. All three source-text
facets are CLEAN; this is not a second51-pair reading or57unique pairs.

All27directed kanji edges and four retained source word negative edges are reviewed.
The only kanji-edge change is 会:社→公. Four direct word guards are 書店–店、
水道–水、道–方、力–左右, without transitive cliques. The 力/強い voicing-component
correction, qualified histories and 公立/持てる distinctions retain exact evidence.
Unsupported rarity/register modifiers are neutralized, not declared false or common.
Current membership672:106kanji/430words/106strokes/2articles/22counterfiles/
onegrammarset/2scenecatalogs/3images. Fresh strict8278-entry progress:672reviewed-current,
no partial, two reviewed runtime-blocked drafts,7,604pending and7,606runtimepathsabsent.
Kanji74N5/27N4/5N3 still leave 名・子・学・小・校・高 absent.
Actual corrected serial checks:0errors/124tests33.568s; budget680files/689entries/
1969250retained/1985932inflated/984888localZIPbytes; version `2de6f16a7092c537`.
Public desktop archive/exact-main CI follow separately. Actual app fallback for canonical
`institutions`, `na-adjective`, `work` remains unresolved; IDs retained and concurrent app
untouched. No phone/IME/playback/media/packageaudio/C6/C7/activation/release/checkpoint
authority follows. Continue every safe family of the finite frozen target.

Earlier accepted milestones below are historical.

The twenty-second full-target source batch adds full友・古・右・天・左・新・気・犬・良・銀・長
cards,13complete word articles and11RAW-identical licensed frozen-source strokes.
[Batch022 accepted source](translation-batches/022-foundation-contrasts-kanji-reviewed-source.json)
binds46affected paths:35new runtime objects and14exact wrappers across11older bodies.
All595other baseline RAW objects remain unchanged. Actual independent review read47complete
RU/ENpairs and417word/97kanji title/guard rows—not514whole-body reviews. One finding,
unsafe長→良 because both have ordinary positive-quality meanings, was recorded before
a separate signed amendment and resolved by長→銀. A focused independent3-pair recheck
confirmed the fix and unchanged640other runtime objects; all three textual facets are CLEAN.
The synchronous initial reviewer could not receive follow-up messages, so a fresh narrow
recheck was necessary; there was never more than one active reviewer.

All33final directed kanji edges, six source word negative edges and three new direct guards
(子犬–犬、右手–手、左手–手) are reviewed; no transitive clique. Four source kanji edges
change in total. Named気reading-classification/history, qualified右岸うがん correction,
古/新/良reading grouping and register retain their exact evidence boundaries.
Current membership641:97kanji/417words/97strokes/2articles/22counterfiles/onegrammarset/
2scenecatalogs/3images. Strict8278-entry progress:641reviewed-current, no partial,
two reviewed runtime-blocked drafts,7,635pending and7,637runtimepathsabsent.
Kanji levels74N5/18N4/5N3 leave six frozenN5kanji:名・子・学・小・校・高.
Actual final serialized checks:0errors/124tests37.589s; budget649files/658entries,
1886838retained/1903520inflated/944262localZIPbytes; version `add35d1a4509626b`.
Public desktop archive/exact-main CI follow separately. No new canonical tag IDs;
concurrent app and frozen pilot refs remain untouched. No phone/IME/playback/newmedia/
packageaudio/C6/C7/activation/release/checkpoint authority. Continue every safe frozen family.

Earlier accepted milestones below are historical.

The twenty-first full-target source batch adds full万・国・語・母・父・毎・海 cards,
two complete word articles and seven RAW-identical licensed frozen-source strokes.
The separately frozen navigation amendment covers18old bodies with22exact wrappers;
all other old RAW bytes and572unaffected baseline runtime objects remain unchanged.
[Batch021 accepted source](translation-batches/021-everyday-foundations-kanji-reviewed-source.json)
binds all34affected paths and the actual independent whole45RU/EN-pair review:
27authored/amended bodies plus18complete contexts, all404word/86kanji title/guard rows,
three CLEAN textual facets and no required finding. The490title rows are not490body reviews.
All21new directed kanji edges were read. One source語→話 edge becomes語→口 because
ordinary speaking meanings overlap; no new word guard or transitive clique was required.
每historical-form wording, named-dictionary母rare-reading classification and語らうregister
retain their evidence boundaries; technical Japanese fields/classifications stay stable.

Current membership606:86kanji/404words/86strokes/2articles/22counterfiles/onegrammarset/
2scenecatalogs/3images. Strict8278-entry progress:606reviewed-current, no partial,
two reviewed runtime-blocked drafts,7,670pending and7,672runtimepathsabsent.
Kanji levels68N5/14N4/4N3 leave12frozenN5kanji absent; no invented syllabus coverage.
Actual final serialized checks:0errors/124tests43.963s; final budget614files/623entries,
1795849retained/1812531inflated/898650localZIPbytes; version `74520d18c4425b1b`.
Public desktop archive/exact-main CI follow separately from source acceptance.
New retained canonical `set-phrase` and `simplified-form` app rendering is UNVERIFIED,
not a proven defect; concurrent app untouched. Historical receipts remain immutable.
No native/phone/IME/playback/newmedia/packageaudio/C6/C7/activation/release/checkpoint authority.
Continue every remaining safe frozen family; this is not full-corpus or allN5 completion.

The twentieth full-target source batch adds complete motion/position cards for前・後・来・行,
six complete words and four RAW-identical licensed frozen-source strokes; nine older bodies
restore one source-linked wrapper each without altering their other RAW bytes.
[Batch020 accepted source](translation-batches/020-motion-position-reviewed-source.json)
binds all23affected paths and the actual independent whole31RU/EN-pair review
(19authored/amended bodies plus12complete contexts), all402word/79kanji title/guard rows
and three CLEAN textual facets. These title tables are not481complete-body reviews.
The single前→先 distractor replacement by前→月 and three individually supported
行く–出かける/出る/立つ guards preserve Japanese meanings without a movement clique.
後history is explicitly attributed;来glyph readings and銀行history retain their qualifiers.
All567unaffected baseline runtimeRAW objects and immutable historical receipts remain.

Current membership590:79kanji/402words/79strokes/2articles/22counterfiles/onegrammarset/
2scenecatalogs/3images. Strict8278-entry progress:590reviewed-current, no partial,
two reviewed runtime-blocked drafts,7,686pending and7,688runtimepathsabsent.
Kanji membership62N5/13N4/4N3 leaves18frozenN5kanji absent; no invented syllabus coverage.
Actual final serialized checks:0errors/124tests57.027s; final budget598files/607entries,
1754286retained/1770968inflated/877733localZIPbytes; version `b4730636d151b4ee`.
Public desktop archive/exact-main CI follow separately from source acceptance.
The new canonical `irregular` ID remains technical; current app rendering is UNVERIFIED.
No native/phone/IME/playback/newmedia/packageaudio/C6/C7/activation/release/checkpoint authority.
Continue the remaining safe frozen-target batches; this is not full-corpus or allN5 completion.

The nineteenth full-target source batch completes the frozen57-kanji foundation component:
42N5/11N4/4N3 kanji,57byte-identical licensed source strokes, and135previously accepted word
amendments restoring152required links. One inherited月teaching claim is separately corrected.
[Current batch019 source record](translation-batches/019-foundation-kanji-reviewed-source.json)
composes the actual whole57kanji review and three complete45word reviews with genuine focused
円/月/分/車–電車 corrections/rechecks—not a fresh192body or whole-corpus review.
All assigned learner-source facets are CLEAN through that exact lineage. Valid 車 and電車
meanings remain; their direct exclusion does not create a transitive自動車–電車pair.

Current membership576:75kanji/396words/75strokes/2articles/22counterfiles/onegrammarset/
2scenecatalogs/3images. Strict8278-entry progress:576reviewed-current, no partial,
two reviewed runtime-blocked drafts,7,700pending and7,702runtimepathsabsent.
All326unaffected baseline runtimeRAW objects remain unchanged;135words and月are intentionally
updated and re-reviewed. Historical receipts remain immutable; checkpointauthoritynull/Readyfalse.
Actual final serialized checks:0errors/124tests32.498s; final budget584files/593entries,
1711270retained/1727952inflated/857517localZIPbytes; version `ab961b443ea10352`.
The observed missing Unicode-license export is repaired by an exact1995byte frozen-license
root copy, preserving the historical docs copy and broad developer-directory exclusions.
Actual local single-root archive verification covers all576runtime hashes and57newstrokeRAWs.
Public desktop archive/exact-main CI are recorded separately after actual publication, not
inferred from these source/text checks. Canonical IDs remain; concurrent app untouched.
No native/phone/IME/grading/playback/newmedia/packageaudio/C6/C7/activation/release/checkpoint
authority follows. Continue subsequent safe batches through every remaining frozen family.

The eighteenth full-target source batch completed21 full human/sign/trace articles:
three remaining linked roots plus18 actual negative-reference dependencies,
preserving15N3/3N2/oneN4/oneN5/oneunlabelled classifications.
[Batch018](translation-batches/018-people-signs-traces-words-review.json) records actual whole
816EN/1027RU lines,21titles/84sections/all396actual title/hash records and six complete
unchanged Russian baseline bodies222lines. All55complete successful dictionary queries comprise
58entryoccurrences/104forms/161objects=144lexical+17Wiki; a separate complete人query supplies
eight lexical senses. NamedSeisenban兆候evidence is distinguished from the firstDaijisen block.
All24source references and13 individually justified direct Russian guards survive;
character/collective-human/mark/signal/expression overlaps are assessed directly, not transitively.
Actual whole three-facet review: all scoped source/text facets CLEAN; no required correction.
At that milestone membership462; strict8278-entry statuses462reviewed-current, no partial, two reviewed
runtime-blocked drafts and7,814pending, with7,816runtimepathsabsent.
All441earlier tracking records/non-record sections/runtimeRAWobjects unchanged;
checkpointauthoritynull/Readyfalse. Serialized checks:0errors/124tests49.038s;
budget469files478entries1413172retained/1427189inflated/710824localZIPbytes;
version `2896f5c9d706c5bd`. Twenty-one pinned-app unmapped IDs affect27occurrences;
current rendering UNVERIFIED, concurrent app untouched. All21new working textsCRLF;
RAW/LF/Git/public domains remain distinct. The format-reference intro now targets the committed
frozen6afcontract instead of later/dirtyEN, retaining earlier test reports as historical.
No assets/grammar/media or device/native/C6/C7/package/activation/release/checkpoint authority.
Continue the real57-new-kanji mandatory-distractor component and every remaining frozen family.

The seventeenth full-target source batch completed25 full place/period/name/reading-support
articles, preserving2N2/5N3/2N4/oneN5/15unlabelled classifications.
[Batch017](translation-batches/017-places-time-reading-words-review.json) records actual whole
794EN/913RU lines,25titles/100sections/all375actual labels/nine complete unchanged baseline
Russian bodies335lines. All66complete successful queries comprise66entryoccurrences/96forms/
106objects=92nonWikiNonPlace+twoPlace+12Wiki; seven exact failures are not positive evidence
or invalidity. Actual proper-name revisions and accepted六か月row are separately bound.
The genuine北海道FAQ—not a search-invented quote in the actual pamphlet—supports the qualified
replacement history. Two directly related active-guidance lines preserve exact-source discipline.
There are no source-header negative edges; two independently justified direct guards protect
見物–見るand読書–読むactual Russian overlaps, not transitive cliques or POS-only reasoning.
All three scoped source/text facets CLEAN after actual whole review; no required correction.
At that milestone membership441; strict8278-entry statuses441reviewed-current, no partial, two reviewed
runtime-blocked drafts and7,835pending, with7,837runtimepathsabsent.
All416earlier tracking records/non-record sections/runtimeRAWobjects unchanged;
checkpointauthoritynull/Readyfalse. Serialized checks:0errors/124tests27.955s;
budget448files457entries1352155retained/1366172inflated/680317localZIPbytes;
version `d0406f8891b9ecac`. Sixteen pinned-app unmapped IDs affect21occurrences; app rendering
UNVERIFIED and concurrent checkout untouched. All25new working textsCRLF; byte domains distinct.
No assets/grammar/media or device/native/C6/C7/package/activation/release/checkpoint authority.
Continue the remaining3linked roots/21closed words,57-new-kanji component, then all frozen families.

The sixteenth full-target source batch completed25 full everyday reading-word articles:
19roots plus six real source negative-reference dependencies, preserving24N5/oneN3.
[Batch016](translation-batches/016-everyday-reading-words-review.json) records actual whole
820EN/844RU-line reading,25titles/100sections/all350displayed meanings/nine complete unchanged
Russian baseline bodies310lines. All73complete dictionary query/entry occurrences comprise
126forms/289objects=270lexical+twoPlace+17Wiki; no unique-lexeme or blanket-adoption assertion.
Both complete textual Tokyo-pitch sections support雨HL/飴LH, not audio/native acceptance.
All eight source-directed edges and eight individually reviewed direct Russian guards survive;
足–お金is explicitly narrowly conservative, with colloquial/usuお〜witness, not ordinary bare
money usage. No transitive colour/food/bodypart/transport/movement clique is inferred.
The actual whole three-facet review found no consequential defect; all scoped facets CLEAN.
Hand/foot non-antonym, every-year dual readings, birth/knowledge/loan/colour/half distinctions
remain; two directly related guidance lines document the source-label discrepancy.
At that milestone membership416; strict8278-entry statuses416reviewed-current, no partial, two reviewed
runtime-blocked drafts and7,860pending, with7,862runtime paths absent. All391 earlier tracking
records/non-record sections and runtimeRAWobjects remain unchanged; checkpointauthoritynull/Readyfalse.
Serialized checks:0errors/124tests48.039s; budget423files432entries1294859retained/
1308876inflated/651417localZIPbytes; version `faa2fe07d4ce9f22`.
Eleven pinned-app unmapped IDs affect13occurrences; IDs stable, concurrent app untouched.
All25new working texts are CRLF; normalized/Git/public domains remain distinct.
No new assets/grammar/media or device/native/C6/C7/package/activation/release/checkpoint authority.
Continue safe required-word support for the57-new-kanji component, then all remaining frozen families.

The fifteenth full-target source batch completed37 full calendar/count word articles,
preserving23 N5/14 unlabelled source levels. [Batch015](translation-batches/015-calendar-count-words-review.json)
records whole1134EN/1138RU-line reading,37 titles/148 sections, all325 displayed meanings and
full日/人 source/RU pairs. Source zero negative edges and two justified direct Russian guards
remain; no generic/transitive number/person/day clique or fabricated missing month units.
All56 complete dictionary queries comprise57 entry occurrences/177forms/136sense objects,
including12Place/4Wiki objects, leaving120lexical occurrences; no blanket sense adoption.
One genuine minor finding required removal of an unsupported added一千円 spelling assertion.
False historical capture attributions are explicitly withdrawn by a superseding erratum;
immutable originals remain. An independent exact-delta/evidence recheck resolved B015-R1.
Other36 new words/all354 earlier runtime RAW objects are unchanged; final composite facets CLEAN.
At that milestone membership391; strict8278-entry statuses391reviewed-current, no partial, two reviewed
runtime-blocked drafts and7,885pending, with7,887runtime paths absent. All354 old tracking records/
non-record sections unchanged; checkpoint authority null/Ready false.
Final serialized checks:0errors/124tests32.014s; budget398files407entries1234441retained/
1248458inflated/620416localZIP bytes; version `95a8d5dc2948138c`.
Counter-specific sound changes, actual alternate readings, calendar/date/duration distinctions
and bounded currency claims survive. Eleven pinned-app unmapped IDs affect56occurrences;
canonical IDs remain stable and the concurrent app was not changed. No assets/grammar/media or
native/device/activation authority follows. Continue required-word support for the actual57-new-kanji
mandatory-distractor component, then every remaining level/source family.

The fourteenth full-target source batch completed38 full calendar/time word articles:
34 N5 roots plus four mandatory source negative-reference dependencies, preserving35 N5/two N4/
one N3 levels. [Batch014](translation-batches/014-calendar-time-words-review.json) records actual
whole1302EN/1271RU-line reading,38 titles/152 localized sections, all288 displayed meanings and seven
complete supporting baseline bodies. All15 source edges and six individually evidenced new Russian
guards survive; no meal/daypart transitive clique or indiscriminate sense adoption was added.
One genuine minor source-fidelity finding required夕方's comparison to include early evening.
The exact one-clause repair and two active guidance lines were independently rechecked; the other37
new files, all Japanese/technical data and all316 earlier runtime RAW objects are unchanged.
Initial NEEDS FIX evidence remains historical; the final composite three source/text facets are CLEAN.
At that milestone membership354; strict8278-entry statuses354reviewed-current, no partial, two reviewed
runtime-blocked drafts and7,922pending, with7,924runtime paths absent. All316 earlier tracking records/
non-record sections remain unchanged; checkpoint authority null/Ready false.
Final serialized checks:0errors/124tests32.911s; budget361files370entries1163599retained/
1177016inflated/581157localZIP bytes; version `636066eada6c6783`.
Actual dictionary counts are45entries/70forms/81returned sense objects, including17Wikipedia
pseudo-definitions, not81lexical+17. Seven pinned-app unmapped IDs affect21 occurrences/20 new
cards; canonical IDs remain stable and the concurrent app was not changed.
No new assets/grammar contexts/media or native/device/IME/activation/release authority follows.
Continue the next safe remaining N5 kanji/words/support batch and then all remaining source families.

The thirteenth full-target source batch completed eleven missing N5 schema2 number/time files:
122 complete expressions,255 Russian learner-text leaves,392 written-answer occurrences and149
reading-answer occurrences. [Batch013](translation-batches/013-n5-number-time-expressions-review.json)
records actual whole2064EN/2064RU-line reading and one genuine minor finding: `24 дней` required
`24 дня`. The exact cue-only correction and two-line active guidance lesson were independently
rechecked; all other254 leaves, all Japanese/technical/accepted data and all305 prior runtime
RAW fingerprints remain unchanged. The narrower check is not a second whole122-expression review.
At that milestone membership was316; strict8278-entry statuses were316reviewed-current, no partial, two reviewed
runtime-blocked drafts and7,960pending, with7,962runtime paths absent. All305 earlier tracking
records/non-record sections remain unchanged; checkpoint authority is null and Ready remains false.
Final serialized checks:0errors/124tests28.490s; budget323files332entries1077037retained/
1090454inflated/534880localZIP bytes; version `2d5ac8dd3491a7de`.
Calendar/timepoint/duration and canonical-versus-alternate-reading constraints survive in Russian.
No word-quiz/grammar/media/app changes or native/exhaustive/parser/device/activation approval follows.
The subsequently frozen calendar/time word scope was completed and reviewed as014 above.

The twelfth full-target source batch completed the full ten-file N5 schema1 counter component:
nine new files plus completion of the partial `tsu.json`,124forward cards/20reverse fixtures/
80live option contexts/191Russian text leaves. [Batch012](translation-batches/012-n5-counter-closure-review.json)
preserves the initial whole review and actual findings: six wrong `回` choices admitted action
frequency, and bare `お茶` admitted bottled `本`. Seven exact negative sites were prefrozen,
corrected and independently adjudicated; all prompts/accepted tiers/readings/IDs/Russian leaf
values stayed unchanged. Direct full-range evidence resolved the language/bounded-form policy,
not Android normalization or native/editor/exhaustive-grading acceptance.
The actual narrower adjudication read12complete current/source/initial records and four live
reverse nouns; a generic interim result was not counted as scoped evidence.
At that milestone membership was305; statuses were305reviewed-current, no partial, two reviewed runtime-blocked
drafts and7,971pending, with7,973runtime paths absent. All295other prior tracking records/runtime
blobs and non-record sections remain unchanged; old partial-tsu receipts remain historical.
Final serialized checks:0errors/124tests43.252s, budget312files321entries984818retained/
998235inflated/520508localZIP bytes; version `e82c69299a2d0bbe`.
No word-tag/app/media/frozen-ref/checkpoint authority changed. C6/C7 and historical automatic
grading/native/device bounds still gate activation/release, not independent text authoring.
The next proposed lane at that time was eleven missing N5 schema2 number/time files;
that scope was subsequently frozen, authored and reviewed as013 above.

The eleventh full-target source batch completed21 full N5 stationery/personal-object articles.
[Batch011](translation-batches/011-stationery-personal-objects-review.json) records actual
whole21-pair reading (699EN/848RUlines), all23 queries/24entries/57senses/36forms,
250 actual answer labels and four complete baseline EN/RU pairs. All three facets CLEAN,
no findings or optional polish. Three direct guards cover generic/specific pens and the
Russian periodical label, not a writing-tool/publication clique.
Membership became296; statuses were295 reviewed-current, one partial counter, two reviewed
runtime-blocked drafts and7,980 pending. All275 earlier tracking records are unchanged.
Pinned app-hint follow-up covers17 IDs/22occurrences/19cards, not all newly introduced.
No native/rendering/device/media/activation/checkpoint or frozen-ref approval is implied.
Continuous full-frozen-target authoring proceeds.

The tenth full-target source batch completed25 full home/furniture word articles:
24N5 plus the mandatory N4 会話 dependency. [Batch010](translation-batches/010-home-furniture-review.json)
records actual independent reading of all25 complete RU/EN pairs,32 complete dictionary
queries,229 actual answer labels and nine relevant complete baseline bodies; all three
facets CLEAN, no findings. Seven direct Russian ambiguity guards include the room/cuisine
polysemy of «кухня», without a housing/furniture/transitive clique. A stale provisional
sentence in the immutable freeze receipt is explicitly corrected, not rewritten.
Membership became275; statuses were274 reviewed-current, one partial counter, two reviewed
runtime-blocked drafts and8,001 pending. All250 earlier tracking records are unchanged.
Pinned app-hint follow-up covers17 IDs/29occurrences/24cards, not all newly introduced.
No native/rendering/device/media/activation/checkpoint or frozen-ref approval is implied.
Continuous authoring proceeds against the same frozen full target.

The ninth full-target source batch completed23 full N5 clothing/accessory word articles.
[Batch009](translation-batches/009-clothing-accessories-review.json) records whole23-pair reading,
all27 dictionary queries and204 actual answer labels, with four individually justified direct
exclusion pairs. A real low-severity provenance overstatement was corrected and independently
rechecked; all23 learner files and all prior runtime objects stayed unchanged through closure.
Membership became250; statuses were249 reviewed-current, one partial counter, two reviewed
runtime-blocked drafts and8,026 pending. Source authoring continued.
The exact pinned app-hint gaps additionally cover seven IDs/25occurrences in23 new cards;
canonical IDs and concurrent app remain untouched. No native option-pool, device/media,
activation, checkpoint or frozen pilot/controlled ref approval is implied.

The eighth full-target source batch completed27 full food/drink/meal word articles:
26N5 plus the mandatory N4 食事 dependency. [Batch008](translation-batches/008-food-drinks-review.json)
records whole27-pair reading, all27 complete dictionary queries and181 actual answer labels,
then genuine corrective recheck of the missing direct 昼/昼御飯 lunch guard and two exact
optional phrases. Existing baseline bodies and the other24 new cards are unchanged.
Membership became227; statuses were226 reviewed-current, one partial counter, two reviewed
runtime-blocked drafts and8,049 pending. Source authoring continued.
The pinned external app renderer still needs Russian mappings for six canonical hint IDs
(`food`, `drinks`, `animal`, `polite-prefix`, `suru-verb`, `meals`); some already affect baseline.
The exact affected scope is documented, IDs preserved, concurrent app untouched.
No ordinary activation, device/media authority, checkpoint or frozen pilot ref changed.

The seventh full-target source batch completed the full numbers/counters article:
all856 frozen source lines,67 citation occurrences and the prior77-line reviewed Russian
general-count lesson. [Batch007](translation-batches/007-numbers-counters-article-review.json)
records whole987-line RU/EN/baseline reading with all three facets CLEAN, no findings,
and adoption of the reviewer's exact optional duration wording.
Membership remained200; statuses were199 reviewed-current, one partial counter unit,
two reviewed runtime-blocked drafts and8,076 pending. Only the article changed;
no new counter, grammar exercise, vocabulary context, asset or release authority was adopted.

The sixth full-target source batch completed the previously partial listing/examples article:
all469 frozen English lines are translated, with the57-line prior reviewed Russian adaptation
retained as a bounded supplement. [Batch006](translation-batches/006-listing-examples-review.json)
records whole-body three-facet CLEAN review and the optional reviewer-proposed wording polish.
Runtime membership remained200; statuses became198 reviewed-current, two partial,
two reviewed runtime-blocked drafts and8,076 pending. No new grammar exercise, vocabulary
context, media permission, frozen pilot ref or release/device approval is introduced.

The fifth full-target source batch was independently accepted: 本,28 complete word articles
and one exact KanjiVG file. [Batch005](translation-batches/005-books-study-review.json)
records whole29-text RU/EN reading,31 complete dictionary objects and154 actual answer labels;
all three facets CLEAN, no findings. Runtime membership became200;8,076 frozen objects then remained
pending, three were partial and two reviewed drafts remained runtime-blocked. Continuous source
authoring proceeds; no release/device/media permissions or frozen pilot refs change.

The fourth full-target source batch was independently accepted: two kanji, 14 full word
articles and two exact KanjiVG files. [Batch 004](translation-batches/004-entry-exit-review.json)
records actual full reading of all16 RU/EN texts, source-based reading-table correction
and bounded grammar adaptation; all three facets CLEAN, no findings. Runtime membership
was170;8,106 frozen objects then remained pending, three partial and two reviewed drafts
runtime-blocked. Its exact source CI41867262069 has now succeeded; actual public archive
and170 runtime hashes were separately verified, without device/release acceptance.

The third full-target source batch was independently accepted: 19 complete kinship/relationship
word articles, actual full review and an exact six-pair correction recheck.
[Batch 003](translation-batches/003-kinship-relationships-review.json) preserves Japanese facts,
all original pairs, dictionary restrictions and review limits. Runtime membership then became 152;
8,124 frozen objects remain pending, three are partial and two reviewed drafts remain
runtime-blocked. Continue the next safe source batch; no release/media/device gate changed.

The second full-target source batch was independently accepted: three kanji, 23 full words,
three exact KanjiVG files and whole-article re-review of the restored 休日 navigation.
[Batch 002](translation-batches/002-people-family-review.json) records the actual independent
27-text three-facet reading, hashes and limits. Runtime membership then became 133;
8,143 frozen objects remain pending, three are partial and two reviewed drafts remain
runtime-blocked. Continuous source authoring continues; release/media/device gates remain.

The first full-target source batch was independently accepted: 23 complete demonstrative
word articles, exact direct answer-pair corrections and current hashes are recorded in
[batch 001](translation-batches/001-demonstratives-review.json). Runtime membership then became
104; 8,172 frozen objects remain pending, three are partial and two reviewed drafts remain
runtime-blocked. Continue authoring; this does not change any release/media/device gate.

Current full-scope execution (2026-11-04): the owner requested the remaining roadmap, not
another smaller pilot. [Full scope and dependency order](FULL-TRANSLATION-PLAN.md) freeze EN
`6af98cb...`: 8,278 runtime objects across14families; RU has81 present, including three partial
units. The independently reviewed plan retains C6/C7 gates. Contributor provenance/drift
tooling is implemented and independently accepted after correcting raw duplicate JSON loading;
124 tests and the actual zero-error validator pass. The reproducible manual report leaves
partial units, runtime-blocked drafts and the remaining corpus pending; no checkpoint/tag advanced.
Additional owned API29 testing earned 40 real reverse answers and passed five newly unlocked
Word Type questions with automatic focus/IME and committed source-bound history.
Delivery of the new signed `0293a7ba...` APK to the phone is verified, not phone
installation/acceptance. Counter second-day, exact audio authority/playback and owner-device/C7
remain blocked; broad translation has not been declared complete or silently enabled.
The historical pilot narrative below retains its original scope and earlier observations.

Current status: Pilot A's bounded C5 integration gate is accepted through Native15. The owner
subsequently authorized merging all three reviewed testing branches: app main `30b0719`,
RU main `98046a9`, EN main signed two-parent merge `5f460b8`. This is source publication,
not production/default activation. Official `ru-pilot-a` remains pinned at544dd15.
The next C6 cohort and its separately frozen necessary closure amendment are specified in
[Pilot B](PILOT-B.md): 81 runtime entries, complete structured lessons and bounded reused pictures;
both complete audio adaptations remain text drafts blocked for runtime by fresh-package authority.
Pilot B now has accepted independent content review, 109 tool tests, final public-archive readers,
and bounded actual grammar/counter/picture integration on the owned API-29 lab. That integration
also corrected retained-producer locale resolution in the app. The complete observation matrix,
exact APK/package identities, restored original lab state and remaining earned-history/native
boundaries are in [Pilot B](PILOT-B.md); counter suffix typing, Word Type targets beyond the five
actually unlocked and checked later, and listening are not silently counted green.
The [later five-target C6 record](https://github.com/stop-cran/learning-japanese-ru/issues/6#issuecomment-6633295530)
supersedes only the earlier unearned-Word-Type observation, not the remaining gates.
New work is published on `ru-pilot-b` / `ru-pilot-b-integration`
and fast-forwarded into the respective mains as source integration, not substituted into the frozen
official `ru-pilot-a` or the controlled native runtime commit.
C7 and broad translation remain separate. Earlier pending/failed dispositions below retain their dates.

Earlier status: C2 instructions independently reviewed and adopted, shared C1 Python checks passing,
app localization received bounded code acceptance, then native testing reopened two Settings defects;
pilot-A content is independently accepted after all eight corrections and
affected-content re-review. The real RU tooling suite passes 109 tests after the raw-export regression;
app/native/general-publication acceptance remains pending.
Retained Android correction regressions pass 85 tests with zero failures/errors/skips; the isolated
released reader also passes 2 actual current-main EN/RU archive cases. The next bounded correction
batch passes 40 retained tests with zero failures/errors/skips; the parent verified the release APK
signature/hash/size and unchanged original UX snapshots. Targeted reviews resolve duplicate manifest
declarations, candidate busy cleanup, the queued-sync overwrite and typed Drawing admission.
The second targeted review returned NEEDSFIX for two coupled gaps: obsolete branch authority blocks an
intentional default-source transition, and Practice recovery/stale-preview guidance remains English.
The author completed the two-fix batch; the parent verified 25 retained passing cases with zero
failures/errors/skips, final command exit statuses, APK hash/size and unchanged original UX snapshots.
That narrow review confirmed the original default-sync recovery and all four Practice notices, but
returned NEEDSFIX for one coupled marker defect: a same-branch English/System choice is saved only
in preferences, allowing startup to restore older language intent. A single-issue marker/recovery
correction is now implemented. The parent verified 12 retained passing cases with zero failures,
errors or skips, final raw build/command outcomes, APK signature/hash and original UX snapshots.
The one-issue followup returned bounded CLEAN: the latest-intent marker is resolved and no directly
coupled regression was established. Previously reported code-review findings are reconciled across the retained
review sequence; this is not whole-app/native certification.
The first bounded C5 batch passes four raw-recorded, non-skipped article/import/locale/Back executions
on API 29/35 at font scales 1.0/1.5. It uses debug instrumentation and an explicit pilot fixture source;
the frozen signed release separately passed four real Settings English/System/English flows on
the same API/font matrix, including normal force-stop/relaunch persistence. API 35 confirms explicit
`[en]` versus System `[]`; API 29 selected-state screenshots substitute only for its unavailable
platform locale probe. This is not instrumentation, pre-acknowledgement crash or whole-Settings layout acceptance:
API 29 at 1.5 shows an adjacent Intensive control width defect, with baseline/RU causality under triage.
C4's signed public candidate `544dd15f6a07e53042bdb488b9d7a04da9685313` is export/CI verified
only on `ru-pilot-a`. The next native batch completed four actual signed-release public imports,
automatic RU alignment, normal four-choice questions/feedback, Russian article rendering and restart
retention. It found two concrete Settings defects: longer RU labels expose squeezed horizontal
actions, and English checking status persists after accepted RU import. Native execution is paused
for bounded responsive-layout/status-lifecycle correction, targeted review and a new signed candidate.
Native HTTP bytes were not captured; nested article-link/Back was exercised in two configurations,
while the other two used embedded articles/Back to Kanji. This is not ordinary `main`/C7 activation.
The Settings correction passes 33 focused cases with zero failures/errors/skips, lint and signed build;
the responsive component change has bounded static acceptance. Direct parent review requires two
status followups: old-locale invalid-URL errors are not in the migration map, and same-source equality
can mask a returned acceptance failure, while older ordinary-sync activity can hide its rejection.
[Bounded correction review](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6612238696).
The status followup and parent-owned completion cleanup now pass 25 focused cases with zero
failures/errors/skips. Foreground/token ownership, failed-pending cleanup, source-bound terminal
provenance and coordinator process epochs are documented in app instructions.
New signed APK `8b96a453aebf35b051fc32e2cec4326bc4750ff1a22918e68c8dd7013f33525c`
is frozen for bounded native rerun; prior native evidence still belongs to the old APK.
The four-configuration rerun on that exact APK now passes the bounded Settings/public-import/
normal-restart/meaning/article gate. Complete raw records, installed identities and readable-control
screenshots are verified. Source-specific committed history, Kana continuity, offline/failure recovery
and the remaining pilot modes are the next C5 batches; broader acceptance remains open.
[Parent native4 disposition](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6614846692)
and [RU integration record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6614847702).
The follow-on trace confirms that fresh Drawing/Readings are normally locked by the two-day
meaning rule, but their generic RU content-unavailable explanation was a missing hint mapping.
Both producer-owned rule hints now use the existing exhaustive localized resource mapping;
the complete-sentence voice wrapper no longer appends a second full stop. Unlock/source policies
are unchanged. Five focused UI tests pass without failures/errors/skips, and lint/release build pass.
Signature and scoped diff checks pass; Detekt has only original ComposeUiTest81/345.
New signed APK `0556d572fe261cb6b40788e383551efc3ec397fbcca5452f98d25beb863d1664`
is frozen with the unchanged signer and eleven retained fingerprints/snapshots.
Affected native observations remain pending; old native evidence still belongs to its exact APK.
Both verified rendering invariants are recorded in app instructions.
[Verified notice checkpoint](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6615099466)
and [RU record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6615100470).
A 45-minute native source/history checkpoint is assigned on the new frozen candidate, at normal
font on API29/API35, with actual Next/Kana continuity, offline recovery and affected notices/footer.
Live EN main observed before assignment is `3d7e04f9dd9766407b9f27c3711adba620505e8b`;
it does not replace the frozen RU teaching source. No public EN forks were available in the lookup;
a same-canonical-source pilot branch must not be presented as a distinct custom fork.
The returned batch5 checkpoint is parent-verified: all668 inventoried hashes,716 raw command/status
records,161 PNG/XML/separate-stderr pairs, both installed identities/signatures and eleven frozen
fingerprints. Actual ADB records span33.96 minutes. API29 exercises real EN/RU source cycles,
normal Next commits, Kana continuity, both localized rule hints and offline failure/unedited retry.
Home counts establish aggregate allowance/queue continuity, not per-card SRS/history isolation.
API35 covers only retained RU source, corrected voice reason and actual version footer; its source/
quiz/Kana/offline scope remains open. Actual footer versions are EN`2793bdf7fa3bb180` and
RU`afe5c99e66524d95`, separate from native archive hashes, which were not captured.
[Parent batch5 disposition](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6616072446)
and [RU integration record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6616073312).
No new consequential finding was established; existing allowance-count guidance applies.
The next45-minute checkpoint is assigned to API35 lifecycle with the same frozen APK and preserved
lab data. Actual read-only progress exports are requested to distinguish review/history/state
records from capped Home counts; no learner or content/authority injection is allowed in that batch.
The returned API35 batch6 is now parent-verified:452 original hashes,479 complete raw command/status
records,103 PNG/XML/separate-stderr pairs, eleven frozen inputs and both installed identities/signatures.
Actual format6 progress exports retain EN梅/RU日/builtinけ records, add offline EN額, and retain
all4 actual history/SRS rows unchanged through restart and final RU reacceptance. This is source-bound
record persistence for exercised cards, not same-glyph isolation. Offline cached study succeeds;
same-source Save fails and unedited retry succeeds after Wi-Fi restoration. The tablet's unsupported
phone-service command is disclosed, not an app failure. Actual footer EN`ac3f4e4da89adf35` differs
from batch5; RU remains`afe5c99e66524d95`. No native archive hash or new consequential defect.
[Parent batch6 disposition](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6616998936)
and [RU integration record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6617000206).
The API35 pilot-mode batch7 returned a4-minute harness block: production adbd refuses root
despite exit0 and run-as refuses the non-debuggable release. Parent verified69 original hashes,
79 raw text/binary records,11 paired captures, unchanged signed inputs and4 actual prior progress
rows. No fixture, typing/IME/drawing or new study commit. Its RU Words screenshot exposes a separate
consequential presentation defect: localized Word-lock guidance re-enters the legacy reason adapter,
becomes generic content-unavailable advice, and its underlying direction argument is English-only.
[Parent batch7 finding](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6617308178)
and [RU integration record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6617308201).
Correct that WordModeRow presentation through its existing localizedReason override and localized
direction resources, preserve the original gate state, add focused regression/instruction evidence.
Production stays frozen while the next45-minute native8 checkpoint uses a fresh task-owned API29
Google APIs test AVD from the installed image; actual development access/schema/backups must be
verified before minimal disclosed learner prerequisites. Old lab/personal data, teaching/authority,
grading, time and four-choice gates stay untouched. Capture focus/visible IME before input helpers;
eligible mode/recognition evidence remains pending. Word-lock correction follows its return.
Native8 now has parent bounded acceptance:325 original hashes,329 recorded ADB channels/64 paired
captures, genuine userdebug lab access and actual30-table SQLite/WAL comparisons. Three prerequisite
states/six dated logs are isolated from four real Grade3 reading/drawing/WordReading responses.
WordType has actual preinput focus/visible Gboard, but shell Unicode key-event mapping fails;
successful validation/Next is still open. Private export matches actual persisted rows. Source
identity remains stable; only its post-UI acknowledgement token changes, not the fixture authority.
The screenshot also exposes raw English Word type/tag hints. Both Word presentation corrections
now pass7 focused UI cases (0 failures/errors/skips), lint/release/signature/diff; Detekt remains
only original ComposeUiTest81/345. Canonical IDs/gates/English display are preserved; all14 visible
pilot metadata labels are projected through localized resources. App instructions record the
mechanisms and separate shell Unicode failure from focus/keyboard capability.
[Parent batch8/static correction](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6618215472)
and [RU integration record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6618215462).
New signed candidate`15ab35ef4592e2f0e3e74fff1ccda6b79d57ca3731b36b30bf6fd85d42c4cb6b`
is51,540,218 bytes, unchanged signer, fourteen exact frozen inputs. Native9 is assigned with45-minute
limit: API35 corrected/enlarged Word-lock notices and retained history, plus API29 real WordType
validation/Next and localized metadata. A separately signed local input-only UiAutomation helper
may send text after actual focus/IME proof; it does not change the IME or grading. Its runtime
acceptance and this new APK's native acceptance remain pending; earlier results stay with0556.
Native9 now has parent bounded acceptance on that exact15ab APK: API35 corrected Word prerequisites
at1.0/1.5, source/restart persistence and exact four prior state/log rows plus five sessions;
API29 focused RU Type with localized noun/nature, one disclosed input-only helper invocation,
normal Check/feedback/Next and a real Grade3 own-mode record. Actual30-table SQLite/WAL comparison
retains prior7states/10logs/4sessions and adds only one WordType state/log/completed session;
authority/sync unchanged, final8states/11logs/5sessions match the genuine private export.
All175 original hashes/14 frozen files/26 PNG/XML/separate-CRLF-only-stderr pairs and installed
signatures are independently verified. Only244 of262 recognizable command labels are fully separated:
18 interleaved/damaged blocks and extra unassignable status markers are retained/excluded, while
critical upgrade/input/Check/Next/backup/cleanup evidence is complete. App instructions now require
atomic or per-device records, not total-status-count claims. Both full logcat capture phases have
no target crash/ANR; owned cleanup verified. API29 enlarged Type/Japanese keyboard capability remain
unproven; two Word defects are reconciled, not full C5/general publication.
[Parent batch9](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6618617092)
and [RU record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6618617104).
The next45-minute checkpoint is assigned to actual external Android app-language/System return
on API35 and one genuine Android backup/restore attempt on disposable API29, with pending-candidate
interruption only if time permits. No fake OS choice, root-copy substitute for platform backup,
data clear or new public test repository. Exact15ab code/APK stays frozen; the post-native9 guide
change is recorded separately. Per-device/atomic logs prevent repeat evidence corruption.
Semantic platform blocks and any remaining custom/corrupt/capture scope must be reported, not
silently converted to success. This assignment is not acceptance.
Native10 parent verified649 original hashes/433 atomic records/55 PNG/XML/empty-stderr pairs,
fourteen unchanged inputs/both installed APKs and exact owned cleanup. Exclude80 malformed empty
startup commands from353 valid records. Real API35 external English→System persists across restart,
real System RU→EN return retains the pilot and blocks mismatched fresh Kanji/Words; explicitRU/
Systemen-US restored. Actual4state/4log/5session rows matchNative9 exactly. Replacement confirmation
and distinct-fork behavior remain separate. [Parent10](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6619212791)
and [RU record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6619212824).
The backup disposition is corrected from producer summary: original service log shows confirmation
timed out before the allow tap, then invalid-token acknowledgement. Zero-byte output does not
establish platform backup inability; restore was not attempted. App instructions now record named
argument arrays/fail-fast usage errors and asynchronous timely device confirmation. A single
corrected bounded backup/restore attempt is needed; do not repeat the accepted external matrix.
Native11 is assigned15minutes to only the owned API29 lab: one asynchronous backup with timely
fresh confirmation, real archive proof, then asynchronous platform restore and actual progress/
source-language retention if backup succeeds. No root-copy substitute, data clear or external
matrix rerun. Same15ab APK/code; post-native10 guide is separately frozen. Return an honest
semantic block if timely acknowledgement still produces no archive. Result remains pending.
Native11 is now parent-verified within its backup/restore scope:196 original hashes,14 frozen
inputs,115 atomic records (112 numeric statuses;3 unknown launch-status records for2 actual
commands),13 PNG/XML pairs and the installed15ab APK/signature. Timely confirmations led to
actual Android backup/restore completion; the valid25,649,927-byte archive's SQLite/WAL copy
passes integrity checking and exactly matches the post-restore8state/11log/5session rows and
all exported settings retained fromNative9. Actual Russian app Home/Settings are verified;
the filename-labelled final Home is the launcher, not another app check.
[Parent11](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6619800477)
and [RU record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6619801292).
The native service clears data as part of normal restore; no manual data-clear/root-copy
recovery was substituted. Missing async host numeric exits remain unknown. The producer's
different expected-guide text is not accepted as a parent handoff mismatch: actual guide and
stored parent receipt agree. Private backup/export remain local.
Before restore, English UI changed but both default-source repair taps lost their confirmation;
no different selected source was restored. A focused parent cancellation/saved-state regression
reproduces the lost dialog at older-Android Activity recreation. The correction saves confirmation
and changed-default drafts before locale application, keeps explicit Keep/Use default behavior
and durable language intents, and aligns the fields after approved replacement. A bounded
affected signed-release checkpoint is still required; C5 and ordinary RU rollout remain open.
The correction's final8 focused UI cases pass without failures/errors/skips; lint/release,
signature and diff checks pass, with only the two original Detekt findings. New signed candidate
is51,540,218bytes, SHA`a7a9e6b349275fd95221f8cebd1b05f7ad55026118c55f2c49c3b1b7278ecc51`;
18 inputs are frozen, including the new cancellation regression and updated app instructions.
Native12 is assigned20minutes, only ownedAPI29: in-place upgrade, actual recreated confirmation/
Keep/reopened repair/approved default and aligned fields, changed built-in default drafts,
public pilot reacceptance/restart and exact prior progress preservation. No repeated backup,
external matrix, quiz responses or new fixtures. Actual result remains pending.
Native12 stopped safely before installation: its assigned5580 port belonged to an unrelatedAPI35
AVD, not the ownedAPI29 image. Parent verified28 original hashes,6 complete numeric command
records and the actual scoped identity. Initial ambiguous probe/pidof statuses remain unknown;
reconstructed before-fingerprint rows are not direct evidence. No app/native acceptance.
App instructions now require scoped AVD/API identity before app commands and direct hash rows.
Native12b retains the same signeda7a9 APK/17 code inputs with a separately updated method guide;
the same ownedAPI29 userdata is explicitly authorized on checked-free5582/5583, not another image
or a data reset. One20-minute affected execution remains pending; foreignAVDs stay untouched.
Native12b now has parent acceptance for the affected confirmation/default-field correction:
648 original hashes,18 direct before/after inputs,181 numeric records/179 successes and33
PNG/XML/binary-stdout/empty-diagnostic pairs verified. Actual Keep/reopened repair at1.5/default
fields and English sync work; explicit RU pilot acceptance and Russian force-stop/relaunch retain
all progress families exactly (8state/11log/5session) and the frozen pilot head.
[Parent12b](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6620512425)
and [RU record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6620513102).
The first Russian-labelled tap actually selected Spaced same day; a normal UI correction restored
Next day before further checks, without answers. Effective defaults returned, but explicitNextDay
and font1.0 values differ from prior unset preferences. Two cleanup syntax failures were corrected
with per-path absence checks. App guidance records current-hierarchy tap attribution and
raw/effective default comparisons. No target fatal/ANR; owned cleanup verified.
Separate Activity-instance event, EN-default restart, exact RU-main refusal cause and broader
distinct-source/corrupt/interrupted-source gates are not newly proven. No further native matrix
is assigned. C5 and source publication remain open; ordinaryRU/C7 stays disabled.
A prior native smoke without a preserved raw log is not counted as acceptance.
Refreshed current-main EN tooling and actual released-reader checks passed; green tests do not replace
remaining native gates, adjudication of new observations or general publication checks.
The [design](DESIGN.md) remains authoritative for language/source behavior. This plan changes delivery order,
not the agreed independent histories, Japanese target, Latin romaji or no-English-fallback policy.
[Independent review and reconciliation](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6599641819):
no blockers; clarified validated-candidate retention and C0 candidate versus C4 final cohort ownership.

The user has now explicitly authorized a temporary public source for the remaining controlled
C5 checks: [learning-japanese-ru-integration-test](https://github.com/stop-cran/learning-japanese-ru-integration-test).
Its six signed fixture references and actual public exports are verified; all51 reviewed runtime
bodies and12 raw stroke files match the official pilot. Only documented metadata/checksum faults
and a test-only README differ. One25-minute ownedAPI29 execution is assigned; custom-source
alignment, same-glyph isolation and rejected/interrupted-update outcomes remain pending parent
verification. Only test `main` may advance through the prepared corruption/recovery commits;
official EN/RU references and private learner data are outside that authorization.
[Controlled-source plan](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6625623307).

The separate EN compatibility refresh uses current-main baseline
`ab874b6136ad664f7ede1f7ee2adcc2a9f44d7d6`:368 Python tests,validator0,budget/vocabulary checks
and8266 runtime hashes pass, preserving incoming runtime membership/hashes exactly. The released
reader's2 actual cases and current reader's2 cases each pass without failures/errors/skips on the
new schema1 EN package and exact public RU pilot. This candidate remains uncommitted/unpublished;
the RU teaching baseline is unchanged.
[Exact compatibility record](https://github.com/stop-cran/learning-japanese/issues/61#issuecomment-6625623363).

Native13 has bounded parent acceptance:956 original hashes,18 direct input pairs,293 numeric records,
52 raw PNGs and60 actual XML reads verified. Genuine custom `口`/`川` answers add only2states/2logs/
1session; the official `川`/Quiz record and all prior8/11/5 records remain exact. The same-language
Russian choice retains the custom source; both invalid-metadata candidates get localized rejection,
and official RU is restored. Cross-language custom alignment, unfiltered27-word count, exact parser
cause and post-rejection custom-cache recount remain unproven. Unscoped task-file cleanup checking
failed and is not accepted; exact owned process/port shutdown is verified.
[Parent13](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6626137486)
and [RU record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6626137522).
The corrupt/interrupted cases were blocked by the harness's default GitHub account, not lack of the
owner credential: parent operation-local owner preflight proves push permission. A pinned-repository,
no-force, readback-checked ref helper fixes that prerequisite. App instructions capture the verified
authentication/cleanup mechanisms; app code/APK stays frozen. One narrower recovery checkpoint may
use that helper, without repeating study answers or the accepted custom-history case.

Native14 now has parent bounded acceptance for cross-language custom import and corrupt-update
recovery:666 original hashes,18 parent-before/producer-after inputs,205 numeric records,16 PNGs,
29 XML reads and5 integrity-checked30-table SQLite/WAL snapshots. English Settings aligns to RU
while retaining the custom URL/main. Same-source candidate Save rejects the corrupted testmain;
its entire DB/WAL/SHM archive stays byte-identical to baseline. Unedited retry accepts the repaired
head28b39c15 without cache/progress loss. All5 snapshots retain12kanji/27words; final genuine
export exactly retains Native13's10/13/6 and every other progress family, with no new answers.
Official RU/source/Russian relaunch and exact task-file/process/network cleanup are verified.
[Parent14](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6626796021)
and [RU record](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6626796016).
One Checking/force-stop attempt completed acceptance before the stop; pending-validation
interruption remains unverified. Its contradictory candidateAccepted:false summary flag is
rejected against the actual accepted_source row. Launch metadata names the ownedAVD and the
scoped SDK is29, but the AVD-name property was empty, not direct identity proof. App instructions
record both verified harness mechanisms. Native13's invalid-metadata rejections remain accepted;
they were not repeated here. No further native run is automatically assigned. C5 remains open
at the pending-validation interruption boundary; C6/C7 and ordinary rollout remain separate.

Native15 closes the precise remaining pending-validation boundary in one directly executed,
user-approved check. The actual scoped emulator-console name/API identify the ownedAPI29 AVD
before app operations; all17code inputs and installed signeda7a9 APK remain unchanged.
Temporary UID10146-only IPv4/IPv6 TCP443 drops show2packets/120bytes blocked. ActualChecking
and a fresh durable pending token precede force-stop by1.8491112seconds fromSave, before the
8second head-request timeout. Post-stop accepted_source remains official544dd15; the entire
pre/post DB/WAL/SHM archive is byte-identical. All5integrity-checked SQLite/WAL snapshots have
all30tables exactly equal, including both12kanji/27wordcaches and all10/13/6 progress rows.
Normal relaunch abandons the pending intent and retains officialRU/explicitRussian/actualHome.
Both complete firewall rule sets are restored byte-for-byte;13exact device XML files and owned
PID17856/ports5582–5583 are independently absent.481original file hashes are verified.
App guidance records the verified fault-control invariant. This accepts the bounded C5 gate,
not mid-body or post-commit/pre-ack death, C6/C7 or ordinary rollout. Initial console/CLI/SQLite
harness setup corrections occurred before the only Save and are not extra interruption attempts.
[Native15 acceptance](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6627649531).

## Ownership and sequence

The initial checkpoint sequence below is retained as historical pilot/release ordering.
Its old requirement to finish C6/C7 before broad **source authoring** is superseded by the
subsequent owner authorization at the top and in [FULL-TRANSLATION-PLAN.md](FULL-TRANSLATION-PLAN.md).
Reviewed source batches continue against frozen EN `6af98cb…`; ordinary/default activation
and applicable release acceptance remain gated. Actual later native findings may require
correction and independent re-review of affected batches, not a speculative stop to unrelated authoring.

| Checkpoint | Result | Work item |
| --- | --- | --- |
| C0 | Frozen source, scope and acceptance dossier | [RU #4](https://github.com/stop-cran/learning-japanese-ru/issues/4) |
| C1 | Language-aware transport/import contract tested before publication | [EN #61](https://github.com/stop-cran/learning-japanese/issues/61) |
| C2 | Complete reviewed RU instruction set, first usable revision | [RU #1](https://github.com/stop-cran/learning-japanese-ru/issues/1) |
| C3 | Russian app shell smoke-tested, then complete app localization and safe switching | [Android #28](https://github.com/stop-cran/kanji-cards-android/issues/28), [#127](https://github.com/stop-cran/kanji-cards-android/issues/127) |
| C4 | Reviewed, dependency-closed kanji/word pilot A | [RU #3](https://github.com/stop-cran/learning-japanese-ru/issues/3) |
| C5 | First real app/content integration and methodology correction gate | [RU #5](https://github.com/stop-cran/learning-japanese-ru/issues/5) |
| C6 | Small representative pilot B for structured content/media, second correction gate | [RU #6](https://github.com/stop-cran/learning-japanese-ru/issues/6), RU #3 and #5 |
| C7 | Release acceptance and scoped checkpoint; no longer a prerequisite for independent source authoring | [RU #7](https://github.com/stop-cran/learning-japanese-ru/issues/7), RU #3, [RU #2](https://github.com/stop-cran/learning-japanese-ru/issues/2), #5 |

C1 and C2 start in parallel, but C2's executable format instructions must agree with C1 before adoption.
C3's string inventory can start immediately; its source transition implementation needs C1's contract.
C4 requires adopted C1/C2 and a minimal provenance ledger, not scheduled drift automation.
C5 requires complete C3 and reviewed C4; C6 starts only after C5 findings affecting the next batch are reconciled.
C7 retains its applicable C6 acceptance requirements for ordinary activation/release.
The former broad-translation-last order is superseded for source authoring; optional automated
drift reports are not an authoring or study prerequisite. Current partial C6 evidence includes
[grammar/counter/picture observations](https://github.com/stop-cran/learning-japanese-ru/issues/6#issuecomment-6630812890)
and the later [five genuinely unlocked native Word Type paths](https://github.com/stop-cran/learning-japanese-ru/issues/6#issuecomment-6633295530).
Only the specifically recorded remaining gates are unpassed; these observations do not approve
new audio packages, phone/JapaneseIME testing, C7 or ordinary/default activation.

## C0: freeze a bounded experiment

Planning inspection: EN `e27e8aaa61f374fd79216de792f37fd4d2102907`, Android
`8118c2ea4e3c94bf089340360edb644ee0c0cf5c`, RU bootstrap `5713d2fe605a2b2b936b6241abc17b15b047cb8a`.
These are not translation-alignment checkpoints; execution must refresh the source/instruction inventory below.

- Record exact EN/app commits, fresh instruction-entry inventory, current release compatibility baseline,
  locale/source transition table and the exact learning behaviors each pilot must exercise.
- Record pilot-A candidate IDs and provisional support scope. C4 owns the final dependency-closed item inventory
  and freezes it before translation; pilot B is selected separately at C6 after first-gate corrections.
- Create one acceptance dossier with source/item inventories, dependencies, expected UI strings, actual app/content
  revisions, test commands/results, reviewer dispositions and known gaps. Evidence belongs in contributor docs,
  not learner runtime or a second authoritative app state.
- Initialize minimal RU provenance records: adopted scope, EN source hashes, RU reviewed hashes/revisions,
  intentional adaptations and pending/out-of-scope. Initially no translated item or completed checkpoint exists.
- Freeze each batch's upstream SHA while it is authored. Reconcile later upstream changes before checkpoint
  advancement rather than continuously moving the source during review.

Exit: concrete inventories/test cases exist; no open transport/state decision blocks C1.
This is planning evidence, not a translation tag or linguistic approval.

## C1: prove the contract with small fixtures

- Settle authored base/target language configuration, deterministic metadata hashing/versioning, language-neutral
  fields/headings and legacy adapters, repository-language stability, cache metadata and migration boundaries.
- Implement generator/validator/importer support together, keeping the currently released EN reader compatible
  with a freshly generated EN package. RU must fail safely on that old reader, retaining its accepted EN data.
- Use small synthetic fixtures across supported kanji/word/articles, counter v1/v2, grammar/curriculum,
  scenes and both listening transports. These are format tests, not reviewed Russian teaching packages.
- Cover absent legacy EN metadata, malformed/unsupported language/target, unexpected repository-language change,
  metadata-only version change, localized sections, corrupt hashes, missing dependencies and source isolation.
- Run focused existing Python/core/import/migration tests. Verify both old-reader/new-EN and old-reader/RU refusal
  with actual released parser behavior, not only static old-manifest fixtures.

Exit: compatibility matrix and exact transport are green and documented. Do not point an existing learner's
app at a draft RU package or raise the live EN schema just to exercise RU rejection.

## C2: complete instructions before teaching-content authoring

First usable instruction revision implemented and independently accepted at RU
`df6839f4292a52e3316cf040450de38b6adf9add`;
[review and reconciliation](https://github.com/stop-cran/learning-japanese-ru/issues/1#issuecomment-6602318753).
All identified source-rule omissions were restored. This instruction checkpoint permits pilot-A authoring,
not publication acceptance; the original C2 contract below remains the reference for future instruction updates.

- Freshly enumerate EN instructions, scoped authoring files, reviewer agents and normative references;
  compare with the planning inventory and document retain/adapt/replace/remove decisions.
- Implement the complete RU overall/authoring/reviewer guidance for all content families. Close inherited
  path-scoped gaps; use shared guidance rather than requiring one new file or reviewer for every namespace.
- Include a compact terminology/translation guide and worked adaptations: `待つ` without the English comparison
  but retaining awaited-person `を` and waiting-place `で`, plus a complete constrained grammar/task example.
  Samples remain explicitly non-runtime until separately admitted to a content pilot.
- Preserve verified Japanese facts/IDs, naturalness and evidence boundaries; review new Russian comparisons,
  translated answer labels, context-sensitive distractors and pre-/post-answer information.
- Independently review the entire resulting instruction set and samples, reconcile findings, check local references
  and format consistency. Recheck EN instruction changes before adoption.

Exit: a complete, independently reviewed first instruction revision is usable for C4.
It is not frozen forever: C5/C6 can refine it with real integration evidence before expansion.

## C3: translate the app and prove safe language/source transitions

First small testable slice: Russian Home/Settings/section labels, unavailable/download states, standard quiz
chrome and built-in Kana. Native smoke-test real locale contexts and enlarged Russian text before translating
every screen. Use isolated format fixtures; never put English lessons behind a Russian production selector.

Then finish all app-owned surfaces: question/answer/status/error text, mode/deck labels, drawing feedback,
articles/help/accessibility, notifications, listening/recovery/results, export UI, plurals and dates/numbers.
Russian meaning voice uses Russian on-device support or localized unavailability, never English/cloud fallback.
Latin romaji and stable stored enums/IDs are retained; no grading/FSRS change is part of localization.

Implement one source/locale transition owner, including explicit pending versus accepted states:

- New install versus existing EN upgrade; supported device language and System default changes.
- Same-language custom repo retention and confirmed mismatched custom replacement.
- A validated candidate repo aligns UI language without recursively replacing that repo with the UI language's default source.
- Offline matching cache versus localized retry; invalid source/language and failed imports retain accepted data.
- Rapid changes, navigation/cancel/draft edits, stale sync/validation completion, process restart and backup restoration.
- Android Settings changes are observed outside the in-app picker. If confirmation/finish-session is needed while
  backgrounded, persist the pending decision and disclose/resolve it on return; do not silently replace custom content.
- Ordinary active questions explicitly finish/leave; durable listening retains captured content and language.

Test native API 29 and 35, with actual enlarged system text (including dialogs), focused inputs and settled IME.
Test Russian plurals with representative 1/2/5/11/21 quantities, notifications using the app locale, and ambiguous
voice hypotheses/unavailable support. Fixture review states may expose gated modes only in a disposable DB.

Exit: complete app-owned EN/RU coverage and source-switch tests pass; signed candidate release builds.
The early smoke slice is not called complete app translation. Ordinary RU activation remains gated until C7.

## C4: small coherent pilot A, not the full N5 corpus

Target a manageable first batch, provisionally 8-12 kanji and 15-25 words, including `待`/`待つ` and the linked
examples needed by their retained readings. These are sizing targets, not permission to truncate dependencies.
C0 records candidates; C4 freezes final exact paths/IDs and support dependencies before writing. Adjust the batch
or choose simpler cards if closure grows too large.

- Include enough permitted candidates for real meaning/reading choice pools; verify actual expected option counts,
  not a passing quiz with only its correct answer. No gate/exclusion weakening to accommodate a tiny dataset.
- Include full linked article and reading-example support, verified unchanged stroke files and their notices.
  Required examples, assessment prerequisites and references must resolve.
- For optional navigation to untranslated broader material, explicitly retain unlinked Japanese text or omit the
  optional link with a reviewed ledger disposition; never leave dangling links or point silently into English.
  Do not remove teaching rules, claimed reading evidence or scored prerequisites just to shrink the batch.
- Translate all learner-visible fields and bodies. Check Russian label uniqueness/semantic ambiguity and mark
  intentional adaptations; unchanged Japanese provenance is reused without restarting every source investigation.
- Independently review content for correctness, bounded coverage and Russian comprehensibility; reconcile, validate
  and regenerate the exact runtime manifest. Initially publish on an explicitly named testing branch/revision.
  A later owner-authorized merge of reviewed sources into main is not C7 approval or ordinary RU activation.

Exit: reviewed pilot A archive is dependency-closed, format/budget checks pass, and source/RU hashes are recorded.
App-wide localization is broader than pilot teaching coverage; missing content families must be disclosed as unavailable.

## C5: integrate the actual app with pilot A and correct the method

Use the signed candidate APK and exact public candidate archive with its generated manifest. Exercise the real sync,
import, Home queues, quiz/typing/drawing/readings, feedback, linked article Back and progress persistence. Do not
substitute parser fixtures or authoring-only files for delivered lessons. Avoid changing personal learner data.

Check EN to RU to EN, source-specific history restoration, built-in Kana continuity, no English fallback, corrupted/
interrupted updates, offline after sync, unsupported/undeclared repo handling, custom alignment and Android Settings.
Compare visible Russian text, voice/IME behavior and actual selectable options with the approved pilot content.
Retain the exact APK/EN/RU revisions and raw non-skipped native results; record public archive hashes separately
from linguistic approval. Require the old EN reader regression to remain green against the integrated new EN tooling.

For each meaningful finding, identify app, schema/tool, translation, instruction or test-harness ownership. Reproduce
before changing behavior; retain unresolved evidence. Fix/re-review affected content/code, rerun the smallest affected
checks, and update corresponding instructions with a concise mechanism/invariant and a concrete finding reference.
Amend this plan/dependencies when a finding changes the next checkpoint. Do not turn one anecdote into a universal rule.

Exit: no unresolved consequential pilot-A issue; applicable guidance and plan corrections are persisted.
If none are found, say so: no mandatory finding count or instruction churn.

## C6: pilot B exercises structured and media boundaries

After C5, add a small dependency-closed representative set: one compact complete grammar group/set and companion
article/vocabulary/prerequisites; bounded counter v1/v2 examples; at least two permitted word-picture candidates;
one complete legacy listening passage and one existing supported Japanese task package with localized help/feedback.
Choose exact source objects and their true dependency closure before authoring; do not extract arbitrary JSON rows
or inherit package approvals. Synthetic C1 format fixtures are not actual-content acceptance.
The concrete B0–B4 plan, pre-authoring objects, negative-reference closure and scoped operation matrix are in
[PILOT-B.md](PILOT-B.md). Actual vocabulary review binds every translated context; canonical content tags also
need checking at their UI renderer. Existing validator/vocabulary tooling is retained rather than weakened.

Reuse unchanged verified Japanese audio/artwork only, with licenses and fresh package bindings/approval boundaries.
If suitable media or approval is absent, narrow the candidate with an explicit blocked/missing case instead of
generating paid media or claiming that family passed. New media needs separate authorization.

Run second real integration: grammar choice/type and answer-information placement; counter full phrase/readings;
scene descriptions/accessibility without answer leakage; listening playback, transcript/feedback and captured
encounter interruption, process recreation and source/language return. Use isolated review states where necessary.
Apply C5's finding -> correction -> guidance -> affected-regression loop again before expanding the collection.

Exit: all planned pilot-B families genuinely reviewed and integrated, or blocking cases openly recorded.
Unsupported/missing families cannot be counted green or silently replaced with EN content.

## C7: candidate acceptance, then scale the validated process

- Revalidate the integrated published tree, budgets, links, metadata, current EN reader compatibility, release build,
  source transitions, both native API matrices and independent changed-content/code review.
- Provide a version/commit-suffixed release APK in the phone's `Internal storage\Download` when owner testing is
  requested/authorized. Record exact installed APK/content and genuine phone feedback; do not infer it from emulator
  success. Delivering an APK is not installing or approving it.
- Keep owner-testing publication distinct from general release. Enable ordinary RU default/new-install selection
  only after the required compatible app, reviewed runtime stages and applicable release acceptance gates pass.
- Record immutable scoped RU/EN checkpoints only for the adopted, reconciled inventory. Whole-corpus parity remains
  pending; reuse correct earlier review records but re-review changed Russian text or teaching semantics.
- Choose subsequent translation work by coherent content family and review complexity, using refined instructions.
  Add scheduled drift-report/PR automation after a tested manual diff/checkpoint cycle; its availability never gates study.

## Methodological notes recorded now

The reconciled [instruction-plan review](https://github.com/stop-cran/learning-japanese-ru/issues/1#issuecomment-6599291063)
exposed the fixed-inventory and path-scope gaps; the [cross-repository review](https://github.com/stop-cran/learning-japanese-ru/issues/4#issuecomment-6599252027)
identified new-EN/old-reader acceptance ambiguity and the eager-versus-pending source switch change.
Those mechanisms are recorded in corresponding EN/RU/app instructions now.

During this localization work, persist verified reusable findings in the relevant repository's active instructions
in the same correction batch. Keep reproduction, evidence, scope and disposition in the work item; code/linguistic
errors must be fixed, not merely documented. Pending hypotheses stay explicit and do not become mandatory rules.
This is the user's requested methodology for this project, not an assertion that future integration has already passed.
