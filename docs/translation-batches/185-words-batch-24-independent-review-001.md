# Batch 185 (185-words-batch-24) — blind RU review

## Snapshot
- RU repo `learning-japanese-ru`, branch `full-ru-185-words-24`, candidate `60c84eb` (parent `68a8d1c`); clean worktree; no `__pycache__`/`.pyc` committed.
- EN source: frozen `learning-japanese-en-frozen` @ 6af98cb.
- Reviewer: independent, blind (author report, batch/draft docs and tracking JSON not read). Model: not disclosed to reviewer.

## Scope
- 30 new words: きょろきょろ 制限 限る かぎり かあかあ 飽きる うんざり うとうと 空 黙る 黒板 魅力 鬼 髪の毛 高速 高価 骨折 物音 騒音 騒ぎ 駐車 香り 首相 餌 飼う 飯 食糧 食料 食物 食欲.
- Link-only restorations in 10 existing words + kanji/空, kanji/限 (16 links); manifest hash/entry updates.
- Every new article read in full against EN. Scripted checks: front matter (non-title keys) identical to EN; every EN Japanese string ≥2 chars present in RU; EN `quiz_exclusions` all retained; all exclusion targets exist; `link_parity.py` — no lost links (only pre-existing extra kanji/空 links). All EN links dropped in new articles point to RU-absent targets (除く, 禁止, ぐっすり, 板, kanji 毛/骨/駐/香, 悪魔, 速度, 総理大臣, 大臣, 大統領, 議会, 食品, images).

## Verdicts
| Facet | Verdict |
|---|---|
| Correctness | CLEAN |
| Scoped coverage | CLEAN |
| Comprehensibility | CLEAN |
| Quiz safety | NEEDS FIX (F1, F2) |

Russian-only paragraphs checked against cited/standard sources: 飽きる (subject inversion with «надоесть») ✓; 鬼 («óни» transliteration vs pronoun) ✓; 高価 («дорогой» = "dear" not carried by 高価) ✓; 髪の毛 («волосы»/«волосок») ✓; 飯 («зарабатывать на хлеб») ✓; 飼う («держать») ✓; 空 lines 38–41, 55–56 — JMdict そら sense 3 "far-off place; distant place" and 旅の空 "away from home; while travelling" confirmed (https://jisho.org/search/空 , https://jisho.org/search/旅の空) ✓.

## Findings

### F1 — Minor — 高価 lacks guard vs 大切 / 大事 (confidence: medium)
- File: `words/高価.md` line 9, `quiz_exclusions: [高い]`.
- 大切 and 大事 both have title «важный; дорогой» and both already exclude 高い over the shared segment «дорогой». Prompt 高価 («дорогостоящий; высокой цены») with distractor «важный; дорогой» is defensible: «дорогой» in Russian primarily means "expensive" (Ожегов: дорогой 1 «имеющий высокую цену»). Same ambiguity the repo already guards for 高い.
- Evidence: https://jisho.org/search/高価 ("highly priced; expensive; valuable; costly"); https://gramota.ru/poisk?query=дорогой ; RU `words/大切.md`, `words/大事.md` exclusions.
- Fix: `quiz_exclusions: [高い, 大切, 大事]`

### F2 — Minor — 食物 lacks guard vs 食事 (confidence: medium)
- File: `words/食物.md` line 9, `quiz_exclusions: [食べ物, 食料, 食料品]`.
- Title «пища; еда»; Russian «еда» sense 1 is the act of eating (Ожегов: «еда — 1. Приём пищи. 2. Пища»), which is exactly 食事 «приём пищи; трапеза». Prompt 食事 with distractor «пища; еда» is arguable. The same batch already guards 飯 («…; еда (разг.)») → 食事 for this reason, so 食物 is inconsistent.
- Evidence: https://gramota.ru/poisk?query=еда ; RU `words/飯.md` line 9.
- Fix: `quiz_exclusions: [食べ物, 食料, 食料品, 食事]`

### F3 — Minor — 駐車 lacks guard vs 止める (confidence: medium-low)
- File: `words/駐車.md` line 9, `quiz_exclusions: [駐車場]`.
- JMdict 止める(とめる) sense 2 is "to park (e.g. a car)"; the 駐車 article itself (line 37) teaches 車を止める = «поставить машину». Prompt 止める («останавливать; прекращать») with distractor «парковка; парковаться» is weak but defensible for a learner who just read line 37.
- Evidence: https://jisho.org/search/止める
- Fix (conservative): `quiz_exclusions: [駐車場, 止める]`

## Guard basis (RU-added `quiz_exclusions`)
| Card → guard | Dictionary basis | Needed in ordinary quiz? |
|---|---|---|
| きょろきょろ → 見る | mimetic of looking; matches じろじろ/ちらちら precedent | yes (consistency) |
| かぎり → 制限 | 限り s1 "limit; bounds" | yes |
| かぎり → できるだけ | 限り s4 "as much as …"; title has «насколько» | yes |
| かぎり → 以内, 内 | 限り s2 "extent; scope" ≈ «в пределах» | conservative |
| 髪の毛 → 髪, 毛 | shared segments | yes (required) |
| 高速 → 速い | "high speed; rapid" | yes |
| 骨折 → 折る | する-action "break a bone" | yes |
| 騒ぎ → 混乱 | "disturbance/turmoil" overlap | yes |
| 騒ぎ → ばたばた | shared «суматоха» | yes (required) |
| 駐車 → 駐車場 | «парковка» also names the place (article says so) | yes (required) |
| 飼う → 持つ | «держать/иметь» животное | yes |
| 飯 → ご飯, 食べ物 | JMdict めし "cooked rice; meal" | yes |
| 飯 → 米 | rice, follows 米–ご飯 precedent | conservative |
| 飯 → 食物 | shared «еда» | yes (required) |
| 食糧 → 食料品, 食べ物, 食物 | JMdict "food; provisions" | yes |
| 食物 → 食料品 | "food" overlap | yes |
| 食欲 → もりもり | title contains «с аппетитом» | yes (required) |
| 空 → 天気, 気, 気分, 遠く, 遠い | JMdict そら s2 weather, s4 state of mind, s3 far-off place | conservative (article teaches only s3; s2/s4 not shown) |

No unjustified guard found. All EN exclusions retained.

## Optional (not defects)
- 空 vs からから: 空 also reads から "empty" (Jisho), and the prompt shows the spelling; からから «…; пустой; …». Card reading is そら, so low risk; adding からから to 空 is optional (low confidence).
- 骨折 guards 折る but not 折れる «ломаться; сгибаться»; «ломаться» fits the intransitive sense of 骨折する. Optional guard (low).
- 騒ぎ vs 騒音 «шум; грохот» / 音: depends on whether JMdict 騒ぎ includes a "noise/racket" sense; Jisho shows only "uproar; disturbance" — not established.
- かぎり «…; пока» vs 間 (unshown "while" sense) — weak, not established.

## Limits
- No native Russian speaker check; naturalness judged by reviewer.
- Jisho condenses JMdict senses; the full JMdictDB (edrdg) required a password and was not consulted.
- Quiz necessity is a reasoned judgement; distractor frequency in the live quiz was not measured.
- Ожегов citations via gramota.ru search, not page-verified in this session.
