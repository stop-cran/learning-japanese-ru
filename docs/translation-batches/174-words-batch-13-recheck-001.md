# Recheck 001: batch 174 (`174-words-batch-13`)

## Snapshot
- RU repo `learning-japanese-ru`, fix commit `6126c80` (parent `3ed3f15`); working tree clean.
- Diff `3ed3f15..6126c80` changes 7 files: `manifest.json` and words 中心, 地, 場, 実, 畝, 財産. That is 27 insertions and 28 deletions.
- Read-only recheck. Nothing in the repo was modified.

## Reconciliation
| Item | Status | Evidence |
|---|---|---|
| F1: 場–席 guard | **Resolved** | `words/場.md:9` is now `[場所, 所, 会場, 模様, 席]`. |
| F2: 中央–途中/間 (and 半ば–間) | **Withdrawn** | See note below. |
| F3: 実 example gloss | **Resolved** | `words/実.md:22-23` now reads «…в обсуждении было ценное содержание; 実 здесь не означает настоящие плоды.» |
| F4: 地, meaning of に | **Resolved** | `words/地.md:23` now reads «に отмечает конечную точку движения (куда опустилась птица)». |
| Opt: 財産 wording | **Resolved** | `words/財産.md:38-39` now reads «財産 — это имущество, богатство, а не положение дел». It no longer contradicts the title or the figurative example. |
| Opt: English glosses in 場/地/畝 | **Resolved** | "field", "earth" and "furrow" are removed. Each passage now argues from Russian only and still reads correctly. 畝 says «В толкованиях знака встречается и значение «борозда»…», which is true (JMdict 畝 includes "furrow"). |
| Opt: 中心 title | **Resolved** | Front matter `title` and the H1 both read «центр; ядро; главная часть», and they match exactly. |
| Opt: 地–田舎 guard | **Resolved** | `words/地.md:9` adds 田舎. This is justified: 地 «местность» and the 地 example «в этих местах» overlap 田舎 «сельская местность; родные места». It mirrors the baseline guard 田舎 → 土地 («местность»). |

**Why F2 is withdrawn:**
- 中央 «центр; середина» shares no displayed label segment with 途中 «по пути; в процессе» or with 間 «промежуток; между».
- The overlap exists only transitively, through 真ん中, which 中央 already excludes.
- I cannot show a direct label collision, so the owner's decision stands. The 半ば–間 suggestion is withdrawn on the same grounds.

## New «часть» overlaps from the 中心 retitle
None of these is a real quiz collision, so no guards are needed.

- **ほとんど «почти; большая часть»:** this is a quantity adverb, and «большая часть» means "most of". 中心 «главная часть» means the core or focus. They differ in meaning and word class, so a learner would not take one for the other's answer.
- **内側 «внутренняя сторона; внутренняя часть»:** this is a spatial inside versus an outside. 中心 is a centre or focal point. «внутренняя часть» describes an interior, not a centre or core, so the answer stays unambiguous. This is the closest of the three, but it is still not a collision.
- **続き «продолжение; оставшаяся часть»:** this means a continuation or remainder, which is unrelated to 中心.
- **Existing guard:** 中 «внутри; середина», the one card that genuinely overlaps 中心's "inside/middle" sense, is already excluded.

## Regression checks
- **Reflow:** in 地, 場 and 財産 the paragraphs were rewrapped with no lost or duplicated text. Japanese inline readings are intact (地球（ちきゅう）, 電場（でんば）, 畑 link, 実がなる（みがなる）). Prose lines are ≤100 characters.
- **Links:** the only link in the changed passages is the 畑 link, and it is kept. No other links were touched.
- **Manifest:** `manifest.json` hashes match the committed bytes of all six changed word files. `contentVersion` was bumped. No generated files or `__pycache__` were committed.
- **中心 body:** the body still says «организующего средоточия» in the kanji-composition section. This is acceptable there because it is explanatory prose, not the label. Optional only.

## Final verdicts
| Facet | Verdict |
|---|---|
| Correctness | CLEAN |
| Scoped coverage | CLEAN |
| Comprehensibility | CLEAN |
| Quiz safety | CLEAN |

## Optional
- 中心 body «организующего средоточия» could be simplified (e.g. «главной, организующей части»). This is not a defect.

## Limits
- Only the `3ed3f15..6126c80` diff and its directly related title and exclusion data were rechecked. Unchanged files were not re-reviewed beyond the first review.
- The repo validator was not run.
