# Review: batch 174 (`174-words-batch-13`)

## Snapshot
- RU repo `learning-japanese-ru`, branch `full-ru-174-words-13`, candidate `3ed3f15` (parent `ef82227`); working tree clean.
- EN frozen repo `learning-japanese-en-frozen` @ `6af98cb`.
- Reviewer: blind, read-only; author report/rationale and prior batch reviews not read.

## Scope
- 30 new word articles: 額 総額 中心 中央 半ば 竹 酒 笹 稲穂 研究員 研究者 富 財産 武器 矛 内容 実 果実 ピンク 桃 白桃 いかがわしい 疑わしい 略語 畝 畔 獣医 場 地 陸.
- Navigation-only edits in 7 existing files (kanji 容/富/酒, words こと/形式/獣/酔う), plus `manifest.json` and the intake JSON.
- 39 files changed. No generated files, `__pycache__` or `.pyc` were committed.

## Verdicts
| Facet | Verdict |
|---|---|
| Correctness | NEEDS FIX (minor: F3, F4) |
| Scoped coverage | CLEAN |
| Comprehensibility | NEEDS FIX (minor: F3 only) |
| Quiz safety | NEEDS FIX (F1 medium, F2 medium/low confidence) |

Coverage evidence:
- All 30 EN/RU pairs were read in full. Japanese examples and readings are kept verbatim, and every EN sense, note, example and citation is covered. English-only notes were replaced with sensible RU notes: 稲穂 "ear", 武器 "ordinance", 獣医 "vet", the 桃 colour note and the 額 «сумма» note.
- `link_parity.py`: checked 37, with no LOST or EXTRA links. EN links to targets absent in RU were dropped correctly.
- Inbound navigation debt: no RU file still lacks an EN link to any of the 30 new words.
- Nav-only edits change no text; brackets were added only at EN link positions (13 insertions, 13 deletions).

## Findings

### F1: quiz safety, `words/場.md:9` (Minor, confidence medium)
- **Wrong claim:** `quiz_exclusions: [場所, 所, 会場, 模様]` has no pair with 席.
- **Why it matters:** 場 is titled «место; обстановка». Baseline RU 席 «место для сидения» already excludes 場所, 所 and 会場 because they share «место», so the established precedent is that these labels collide.
- **Evidence:** JMdict 席 sense 2 is "location (of a gathering, etc.); place", which overlaps 場 (https://jisho.org/word/席).
- **Remedy:** `quiz_exclusions: [場所, 所, 会場, 模様, 席]`. Add the reciprocal 場 to `words/席.md` if the batch rules allow touching it; otherwise one side is enough.

### F2: quiz safety, `words/中央.md:9` (Minor, confidence medium/low)
- **Wrong claim:** `[真ん中, 中心, 中]` has no pair with 途中 or 間.
- **Why it matters:** 中央 is titled «центр; середина». Baseline 途中 «по пути; в процессе» excludes 真ん中 and 中, and 間 «промежуток; между» excludes 真ん中, 中 and 途中. 真ん中 «самая середина; центр» has essentially the same label as 中央, so the same collision applies directly, not just transitively.
- **Evidence:** JMdict 途中 includes "halfway; midway; in the middle of" (https://jisho.org/word/途中). JMdict 間 includes "space (between); interval" (https://jisho.org/word/間).
- **Remedy:** `quiz_exclusions: [真ん中, 中心, 中, 途中, 間]`.
- **Caveat:** batch 069 itself marked the 間–真ん中 guard as UNVERIFIED, which is why confidence is low. Consider the same check for 半ば–間 (半ば already excludes 途中).

### F3: correctness and comprehension, `words/実.md:22` (Minor, confidence high)
- **Wrong claim:** «…обсуждение было по существу, а не о настоящих плодах» suggests the discussion could have been about fruit.
- **Correct reading:** the EN says the discussion had real substance, and that 実 is used figuratively here, not to mean literal fruit.
- **Remedy:** «Второй пример значит, что в обсуждении было ценное содержание; 実 здесь не означает настоящие плоды.»

### F4: correctness, `words/地.md:23` (Minor, confidence medium)
- **Wrong claim:** «に отмечает направление».
- **Correct fact:** the EN says "destination". In standard teaching, direction is へ; に marks the arrival point (endpoint) of the motion.
- **Remedy:** «В первом примере に отмечает конечную точку движения (куда опустилась птица); во втором で — место, где произошло событие.»

## Optional
- `words/財産.md:39`: «財産 — только имущество» conflicts with the title «достояние; богатство» and the figurative example. Suggest «財産 — это имущество, богатство, а не положение дел».
- `words/畝.md:46`: English "furrow" appears in learner text and could be rephrased in Russian only. Similarly, English "field"/"earth" in `words/場.md:39-40` and `words/地.md:39` could be dropped; the Russian explanation is true without them.
- `words/中心.md:4`: «средоточие» is bookish for beginners (Ožegov: «место, где сосредоточено что-н.; центр»). «главное» may be clearer.
- 地 «местность» vs 田舎 «сельская местность» is a weak overlap; adding a guard is optional.

Checked as OK:
- 酒/お酒 (same title, guarded on the 酒 side), 額 and 総額 vs 金額/合計/代金, and 竹/笹 («саза» is genus *Sasa*: https://ru.wikipedia.org/wiki/Саза).
- 研究者–研究員, 財産–富, 矛–武器, 武器–道具 (conservative but justified), 実–本当/実際 (justified by the shared じつ reading), 果実–実/果物, and 疑わしい–いかがわしい.
- 畔–畝/道, 獣医–医者 (justified via «ветеринарный врач»), and 地/陸–土. No guard is unjustified.
- Title-screen hits judged not to be collisions: 場~ここ/そこ/売り場/跡/隅, 稲穂/畔~田, 白桃~白, 笹~細かい.
- Unlinked references such as «см. в статье о 怪しい…» follow the RU convention for untranslated articles.

## Limits
- Dictionary claims rely on JMdict via the jisho.org API (the 席 entry was fetched live) and on known Ožegov definitions. Other entries were not fetched in this run.
- F2 rests on a guard precedent that batch 069 itself marked UNVERIFIED.
- `manifest.json` and the intake JSON were checked only for presence, not semantically. The repo validator was not run.
