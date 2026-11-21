# Batch 231 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `5af5353eab033af178249f39b48ac4200abf5c24` | `f0e6d8ef3d9983f842128471acff66dfe5a652bc` | Initial review snapshot: the signed candidate, on `origin/full-ru-231-words-70`. |
| `a1887ba643815eb87d79c7dcbe8382af149b73c2` | `2e168b05b3b843ddbc3b1a7bd0016d94aab7d26a` | Fix 1 (final candidate). It covers correctness C1, consistency F1, comprehensibility 1–8 (3, 5 and 8 with adapted wording) and the adopted optional items (correctness 下品:39–40, 酸っぱい:40–41 and 重たい's title; consistency 一致; comprehensibility 酢:28). Signed; on `origin/full-ru-231-words-70`. |

Fix 1 changed twelve word files and regenerated `manifest.json` (`contentVersion` `b6960b5c286625f2`, 5,049 entries; the
candidate had `9f7fbab4482b1d53`). The intake was not refreshed; it still records the candidate's 36 payload hashes.
- `酌む` (lines 4, 12, 16, 19, 20, 27, 33, 41 and 44; correctness C1) and `汲む` (line 34; correctness C1): «саке» instead
  of «сакэ» at every occurrence, including 酌む's title and H1 «наливать саке; выпивать вместе» and the model translations
  «Я налил гостю саке.» and «Мы с другом беседовали за саке.»; Japanese 酒/さけ and the Japanese examples are unchanged.
- `みじめ` (lines 4, 12 and 19; comprehensibility 2): title and H1 «жалкий; плачевный» instead of «жалкий и униженный;
  плачевный»; line 19: «Проиграв матч с большим отрывом, я почувствовал себя несчастным и жалким.» instead of «…
  я почувствовал себя жалким и униженным.»
- `重役` (comprehensibility 3, adapted wording):
  - lines 4 and 12: title and H1 «член руководства компании; важный пост» instead of «член правления (компании); важный
    пост». The reviewer's «руководитель компании» was not used, because it could be read as 社長 «глава компании»;
  - line 19: «На совещании присутствовал один из руководителей компании.» instead of «На совещании присутствовал член
    правления компании.»;
  - line 39: «Не каждый начальник отдела входит в высшее руководство компании,».
- `重量`:
  - line 18 (comprehensibility 4): «Вес этого багажа — десять килограммов.» instead of «Этот багаж весит десять
    килограммов.»;
  - lines 38–40 (comprehensibility 5, adapted wording): «Само 重量 значит только «вес» и не называет весовую категорию.
    Тяжёлую весовую категорию (например, у боксёров) называют отдельные слова 重量級（じゅうりょうきゅう）и
    ヘビー級（ヘビーきゅう）.», replacing the note that 重量 «не называет боксёра-тяжеловеса».
- `引力` (line 20; comprehensibility 6): «Сила притяжения Земли тянет предметы к себе.» instead of «Притяжение Земли
  притягивает предметы.»
- `重たい` (comprehensibility 7 and the correctness optional item): title and H1 «тяжёлый; гнетущий (об атмосфере)» instead
  of «увесистый; гнетущий (об атмосфере)» (lines 4 and 12); line 9 adds 苦しい «мучительный; тяжёлый»:
  `quiz_exclusions: [重い, 重大, 深刻, 暗い, じめじめ, 大変, 苦しい]`.
- `金魚` (line 16; comprehensibility 8, adapted wording): «金魚鉢（きんぎょばち）— «чаша для золотых рыбок»,» instead of
  «… «круглый аквариум для золотых рыбок»,». The reviewer's «стеклянная» was not used: Daijisen's ガラス製などの is not
  glass only, and «чаша» matches the RU 鉢 title «чаша; цветочный горшок».
- `下品` (lines 39–40; comprehensibility 1 and the correctness optional item): the two-line note on the source-list gloss
  «скупость» is deleted.
- `酸っぱい` (lines 40–41; correctness optional item): «酸っぱい описывает кислый вкус, а не химическое измерение
  кислотности, и не служит общим ярлыком для всего, что относят к 酸性.»
- `酢` (line 28; comprehensibility optional item): «Это отдельное слово читается кунным чтением, а не онным.» instead of
  «… по кун, а не по он.»
- `重なる` (line 9; consistency F1 with its optional extension): `quiz_exclusions: [積もる, 積む, 繰り返す, 被る, 合わせる,
  重ねる, 合う, 一致]`, adding 合う «подходить; совпадать», which shares «совпадать» with 重なる's «совпадать по времени»,
  and 一致 «совпадение; единодушие».

The comprehensibility reviewer's 下品:20 «пошло» and its other optional notes (コース's katakana note, 配る and 分ける, 都心's
last sentence, 釘 «крепёжный штырь», 金魚 collocations, and «сакэ», «набэ», «патинко» and «годан/итидан») were not
adopted; the dispositions gave the reasons (see the reconciliation table). EN 下品:20 reads "crude", which the reviewer
itself called a fair match for «грубо»; 配る already excludes 分ける in EN; the reviewer classed the other notes as
non-defects. The consistency reviewer had no optional notes beyond 一致.

The coordinator's post-fix title screen of the changed titles is recorded in its dispositions (5 `OK` lines for guarded
pairs, 16 stem-only `!!` lines). みじめ's only exact title segment shared with another card is «жалкий», shared with 哀れ
«жалость; жалкий» and guarded by みじめ's EN exclusion of 哀れ; 重たい's «тяжёлый» is shared with 重い «тяжёлый», guarded by
重たい's EN exclusion of 重い, and with 苦しい «мучительный; тяжёлый», guarded by the new RU exclusion; 酌む and 重役 have
no exact hit; other hits are stem-only. Fix 1 adds no link and removes none: the only changed link line is 酌む's, where
«сакэ» became «саке» in the text and the target is unchanged. The five RU-only links of the candidate (金魚→鯉, 引力→重力,
重力→重い, 酸性→酸っぱい and 酢→酸っぱい) stand unchanged. `tools/validate.py` reported 0 errors and the unit tests (124)
passed before the fix commit.

Net change from the candidate:
- titles and H1s of 酌む, みじめ, 重役 and 重たい;
- example translations in 酌む (two lines), みじめ, 重役, 重量 and 引力;
- prose in 酌む and 汲む («саке»), 重役 (line 39), 重量 (lines 38–40), 金魚 (line 16), 酢 (line 28) and 酸っぱい
  (lines 40–41), and 下品's two-line note removed;
- three exclusions (重なる→合う, 重なる→一致 and 重たい→苦しい) and no link change.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`5af5353..a1887ba -- words` is twelve word files, 29 lines added and 31 removed; with `manifest.json` the commit changes
13 files, 42 lines added and 44 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs; the
initial reports state that the model is not verifiable from inside the session.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. Each brief was sent only after the previous reviewer had replied. No recheck raised a new finding, so
there was no fix 2.

Each reviewer appended its recheck to its own report file, which stayed in its session context. Each brief included the
full words diff `5af5353..a1887ba` and the coordinator's evidence and rationale for the edits. The correctness section
records that it read the full recheck brief and the actual 5af5353..a1887ba word diff, checked every changed passage in
all 12 cards and reread the five EN originals with rewritten translations; the consistency section records the changed
paths as 12 cards plus `manifest.json`; the comprehensibility section records that it read the twelve-card diff and the
changed passages. The recheck sections do not reproduce the briefs, so this record does not claim their further contents.

The correctness and comprehensibility rechecks state that no generator ran, and the consistency recheck states that no
generator or `build_manifest.py` was run. The correctness and consistency reviewers each ran `tools/validate.py` (0 errors
each); the comprehensibility reviewer did not re-run the validator. Each recheck section records snapshot `a1887ba` with a
clean tree. After the three rechecks the coordinator confirmed, read-only, that the RU checkout is on
`full-ru-231-words-70` at HEAD `a1887ba643815eb87d79c7dcbe8382af149b73c2` (`git rev-parse HEAD`) and that
`git status --porcelain --ignored` prints nothing, so no tracked, untracked or ignored file was left by the rechecks.

### Round 1 (`a1887ba`)

| Facet | Scope and result |
|---|---|
| Correctness | Bounded recheck of every changed passage in all 12 changed cards against `5af5353` and the relevant frozen EN, rereading the five EN originals with rewritten translations; it did not re-read the unchanged passages in full. C1 is **resolved**: every occurrence in 汲む and 酌む now reads «саке», no «сакэ» remains in either file, and the Japanese is untouched. The three optional items are **resolved**: 下品's deletion is accepted, because the English "meanness" ambiguity is absent in RU and the remaining distinctions preserve the Japanese lesson; 酸っぱい's adapted wording keeps taste against the chemical property without the dictionary-gloss framing; 重たい's neutral «тяжёлый» keeps the physical sense. No regression and no objection to the adapted wordings: みじめ «жалкий; плачевный» and «несчастным и жалким» fit the miserable/pitiable sense without making humiliation obligatory (Jisho's entry also includes unhappy); 重役's wording keeps the executive and important-role senses without restricting membership to a board or to 社長; 重量's noun-subject translation keeps the ten-kilogram assertion, and the weight/weight-class wording keeps the lexical distinction; 引力's revised translation keeps agency, present tense and the physical meaning; 金魚's «чаша для золотых рыбок» matches Jisho's 金魚鉢 "goldfish bowl" without unsupported shape or material restrictions; 酢's kun/on terminology changes no reading claim; the added exclusions remove no metadata or lesson. Validator 0 errors. Correctness and scoped coverage are **CLEAN**, carrying forward the original full 30-card review, with no new finding. |
| Consistency | Snapshot `a1887ba` with a clean tree; the changed paths are 12 cards plus `manifest.json`. F1 is **resolved**: 重なる's `quiz_exclusions` is `[積もる, 積む, 繰り返す, 被る, 合わせる, 重ねる, 合う, 一致]`, with all EN entries kept; the optional 一致 is **resolved** (adopted, harmless). Its classifications of the candidate guards (下品→いかがわしい required; 重体→状態/具合 conservative, nonblocking) stand. Title equals H1 on all 12 changed cards. Title screen of the four new titles across the RU word pool: the only exact-segment overlaps are みじめ–哀れ «жалкий» (EN guard), 重たい–重い «тяжёлый» (EN guard) and 重たい–苦しい «тяжёлый» (new RU guard); 重たい→苦しい is justified, because 苦しい «мучительный; тяжёлый» can be read as «тяжёлый» for 重たい. The stem-only lead 重役–指導 «руководство» is not a defensible answer swap, and 重役 shares no segment with 社長 or 部長. All EN exclusions are retained in the 12 cards; the RU-added exclusions total six. Link integrity: the only changed link line is 酌む's, with the target unchanged; no broken target; deleting the 下品 note left nothing orphaned. The 12 changed files' SHA-256 equal the committed manifest hashes; it counted 5,044 manifest entries. Validator 0 errors. Consistency, quiz safety and cross-file integration are **CLEAN**, with no new finding. |
| Comprehensibility | Snapshot `a1887ba` with an empty `git status --porcelain`; read the twelve-card diff and the changed passages, not all 30 cards. Findings 1, 2, 4, 6 and 7 are **resolved** as proposed (the 苦しい exclusion is outside its facets). Findings 3, 5 and 8 are **resolved** by the adapted wordings, which the reviewer accepted and no longer maintained in its proposed forms: «член руководства компании» covers Daijisen's officer cover-term without the board-only gloss and avoids equating 重役 with 社長 «глава компании»; the 重量 note drops the unseen person-gloss, with boxers only as an example of a weight class; «чаша» matches 鉢 and drops roundness and аквариум, and it does not maintain «стеклянная», because Daijisen reads ガラス製などの, not glass only. The adopted 酢:28 optional is **resolved**; the declined 下品:20 «пошло» stays optional («the decline is right», EN "crude"); the other optional notes stay optional. No regression: «саке» is the Lopatin spelling and is consistent within 酌む and 汲む; the 酸っぱい rewrite keeps the taste-versus-酸性 contrast; 重なる's new exclusions change no learner prose; the unchanged みじめに負ける «унизительное поражение» was not reopened. Comprehensibility and scoped coverage are **CLEAN**, with no new finding. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: «сакэ» instead of the standard «саке» in 酌む and 汲む:34 (minor) | **Resolved** | `酌む.md:4,12,16,19,20,27,33,41,44`; `汲む.md:34`; Gramota's Russian Orthographic Dictionary «саке́, нескл., ж. и с.»; Gramota spravka 309247. |
| Correctness optional: 下品:39–40 source-list framing | **Optional, adopted** (with comprehensibility 1); resolved at recheck | `下品.md:39–40` deleted; JMdict 1186230 sense 1. |
| Correctness optional: 酸っぱい:40–41 dictionary-gloss framing | **Optional, adopted** (adapted wording); resolved at recheck | `酸っぱい.md:40–41`. |
| Correctness optional: 重たい's «увесистый» | **Optional, adopted** (with comprehensibility 7); resolved at recheck | `重たい.md:4,12`; Gramota's Kuznetsov entry увесистый; JMdict 1335780. |
| Consistency F1: 重なる «совпадать по времени» and 合う «подходить; совпадать» (minor, quiz safety) | **Resolved** | `重なる.md:9`; 合う's title; JMdict 合う "to match; to coincide"; the card's own 会議が試験と重なりました. |
| Consistency optional: 一致 in 重なる's list | **Optional, adopted**; resolved at recheck | `重なる.md:9`; 一致 «совпадение; единодушие»; RU already guards 一致–合う. |
| Comprehensibility 1: 下品:39–40 explains an unseen source-list gloss (minor) | **Resolved** | `下品.md:39–40` deleted; JMdict 1186230 sense 1. |
| Comprehensibility 2: みじめ «жалкий и униженный» requires humiliation (minor, also coverage) | **Resolved** | `みじめ.md:4,12,19`; JMdict 1303280; Digital Daijisen みじめ. |
| Comprehensibility 3: 重役 «член правления» narrows 会社の重役 to the board (minor, also coverage) | **Resolved** (adapted wording) | `重役.md:4,12,19,39`; Digital Daijisen 重役 sense 2 (取締役・監査役など役員の総称); JMdict 1336770 sense 1. |
| Comprehensibility 4: 重量:18 translates the noun with «весит» (minor) | **Resolved** | `重量.md:18`; JMdict 1336900. |
| Comprehensibility 5: 重量:38 rejects an unseen person-gloss (minor) | **Resolved** (adapted wording) | `重量.md:38–40`. |
| Comprehensibility 6: 引力:20 tautology (minor) | **Resolved** | `引力.md:20`; 引力 (noun) against 引きつけます. |
| Comprehensibility 7: 重たい's unexplained «увесистый» (minor) | **Resolved** | `重たい.md:4,12`; JMdict 1335780 "heavy; weighty"; the existing 重い exclusion kept and 苦しい added. |
| Comprehensibility 8: 金魚:16 «круглый аквариум» (minor) | **Resolved** (adapted wording) | `金魚.md:16`; Digital Daijisen 金魚鉢 (ガラス製などの鉢形の容器); Jisho 金魚鉢 "goldfish bowl". |
| Comprehensibility optional: 酢:28 «по кун / по он» | **Optional, adopted**; resolved at recheck | `酢.md:28`. |
| Comprehensibility optional: 下品:20 «пошло» | **Optional, not adopted**; accepted at recheck | EN 下品:20 "crude"; the reviewer called «грубо» a fair rendering. |
| Comprehensibility optional: コース's katakana note, 配る and 分ける, 都心's last sentence, 釘 «крепёжный штырь», 金魚 collocations, and «сакэ», «набэ», «патинко» and «годан/итидан» | **Optional, not adopted**; kept optional at recheck | The reviewer classed them as non-defects; 配る already excludes 分ける in EN. |
| Exclusion classification: the three RU-added candidate guards | **Agreed**; all kept | 下品→いかがわしい required; 重体→状態 and 重体→具合 conservative, nonblocking (keeping or dropping them is an editorial choice). |
| Consistency limit: its naive SHA-256 check of `strokes/*.json` against the manifest disagreed and was not pursued | **Not a defect**; pre-existing and outside the batch | `tools/build_manifest.py` hashes text files after CRLF→LF normalization. The stroke files are CRLF byte copies of EN blobs, committed and checked out unchanged under `.gitattributes` (`strokes/*.json -text`), as established in Batch 226; 118 of the 718 committed stroke blobs at `a1887ba` contain CR bytes, and re-hashing all 718 entries at `a1887ba` with the generator's normalization matches the manifest. Fix 1 touches no `strokes/` file. |
| Consistency recheck: «the manifest has 5,044 entries», not compared with 5,049 | **Not a discrepancy** | `manifest.json` at `a1887ba` (read with `git show`) has the keys `baseLanguage`, `contentVersion` (`b6960b5c286625f2`), `files` (5,044 entries), `images` (3), `scenes` (2), `schemaVersion` (2) and `targetLanguage`; the generator's 5,049 is the 5,044 `files` plus 3 images and 2 scenes. The candidate `5af5353` has the same split. |
| Consistency process deviation: `python tools/build_manifest.py --help` executed the generator once | **Noted; no action** | It printed 5049 files and version `9f7fbab4482b1d53`; no tracked file changed, and the reviewer deleted the untracked `tools/__pycache__`. |
| «сакэ» in published cards outside the batch (words 酒, 舟 and 猪; kanji 酒, 杯 and 冷) | **Out of scope**; recorded as a follow-up | Not changed by this batch; separate normalisation to «саке». The comprehensibility recheck called it a deferred normalisation, not a defect here; the consistency recheck did not assess it. |

Cross-batch note: links to absent targets stay plain. Five EN link targets in this batch's new cards (5 occurrences) are
absent from RU: the kanji cards 針 (from 針路), 量 (from 重量) and 郵 (from 郵送); and the word cards 終点 (from 重点) and
厚かましい (from みっともない). EN has kanji cards for all three of those kanji; the other written kanji without an RU kanji
card, 釜, 釘, 醜, 酸, 酢, 汲 and 酌, have none in EN either. The 鉢→釜 link held from Batch 230 is applied in this batch;
no links are held from Batch 231.

## Final exclusion set

All 130 EN exclusion entries (25 lists; 金魚, 重量, 重体, 酸性 and 酢 have none) are retained in EN order. Six direct,
one-sided entries are added on four new cards (one new list, 重体):

- Required (1): 下品→いかがわしい, added at the candidate.
- Conservative, nonblocking (2): 重体→状態 and 重体→具合, added at the candidate.
- Added by fix 1 (3): 重なる→合う and 重なる→一致 (consistency F1 and its optional extension), and 重たい→苦しい, after
  重たい's retitle to «тяжёлый; гнетущий (об атмосфере)».

Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added; the targets do not declare these pairs back.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (汲む and 酌む); the three optional items were adopted.
- Scoped coverage: **CLEAN** after fix 1 (みじめ and 重役).
- Comprehensibility: **CLEAN** after fix 1 (下品, みじめ, 重役, 重量, 引力, 重たい and 金魚); the 酢 optional item was
  adopted, and the other optional notes remain optional.
- Cross-file consistency: **CLEAN** throughout; the five RU-only links of the candidate stand.
- Quiz safety: **CLEAN** after fix 1 (重なる→合う and 一致), including the 酌む, みじめ, 重役 and 重たい retitles and
  重たい→苦しい. This covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them; the comprehensibility recheck did not
  re-read all 30 cards. The unchanged cards rest on review 001, in which all three reviewers read all 30 cards in full
  against EN.
- The correctness recheck was a bounded diff recheck; it cites fresh Jisho entries but no other fresh dictionary fetch, and
  its original evidence and model limitations remain. The consistency reviewer took the senses of 苦しい and 合う from the
  cards' own citations and did not re-fetch dictionaries; its necessity classes are judgements, not measurements. The
  comprehensibility recheck states that `validate.py` was not re-run, that quiz safety remained unassigned to it, and that
  it was not a fresh full-batch reread.
- Some of the correctness reviewer's initial live requests returned HTTP 429, and the archived JMdict ID/sense-version
  mapping was not reconstructed for every footer; only successfully inspected entries support its conclusions.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `5af5353`, not `a1887ba`.
- The «сакэ» spelling in existing cards outside the batch was not assessed by the reviewers and is left for a separate
  normalisation.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
