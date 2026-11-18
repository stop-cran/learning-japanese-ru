Snapshot: `2686ee879b1f0d075cd5759341efd87a7724f697` on branch `full-ru-162-words-02`, working tree clean, no uncommitted changes. Baseline is `84ce6e9`. The EN source is frozen at `6af98cb`. Commit `4e48df4` was not reviewed (out of scope).

Scope:
- **Files read:**
  - All 30 new `words/*.md` cards, in full with line numbers, each beside its frozen EN counterpart.
  - The 8 edited files, compared with a word-diff against the baseline and checked against the EN link lines.
  - `docs/translation-batches/162-words-batch-02-intake.json`.
  - The rules: `.github/copilot-instructions.md` L1–70 and L158–401, and `docs/content-format-reference.md` L44–110. There is no `docs/content-format.md` in RU.
  - The author report, used as context only.
- **Role:** independent read-only reviewer. Model: Claude (Anthropic); the exact version is not visible to me.
- **Mechanical checks:**
  - `word_title_screen.py` on the 30 words. I judged each `!!` line by hand.
  - `link_parity.py` on the 38 scoped files: no LOST or EXTRA links. Across the whole tree, no LOST link points to any of the 30 new words.
  - EN↔RU `quiz_exclusions` parity script. No EN exclusion was dropped. The RU extras match the author report plus the coordinator's 決まり→順/順番, 機械→車/自動車, 皿→一杯 and 恋→小説. No unguarded reverse EN pair was found.
  - A grep of the RU title pool for synonym stems.
  - JMdict senses through the jisho API for 決まり, 約束, 続き, 皿, 苦手, 弱い, 法, 規則 and 習慣.
  - The intake path set equals the 38-file diff. All candidate and source SHA-256 hashes were recomputed and match.
  - Nothing was written to the repo.

Verdicts:
- **Correctness:** NEEDS FIX for 続き (F1). CLEAN for the other 29 words.
- **Scoped coverage:** CLEAN for all 30. English-only remarks are re-expressed in Russian:
  - 芝居 and 競技: «драма»/«игра»
  - 法: «закон»
  - 感心: «Молодец!»
  - 恋: «любить» for hobbies and food
  - 続き: the "rest ≠ relaxation" note was dropped, which is acceptable because it teaches no Japanese rule.
- **Comprehensibility:** CLEAN for all 30. The polish items are under Optional.
- **Quiz safety:** NEEDS FIX for 皿 (F2), 苦手 (F3), 方法 (F4), and 決まり and 法 (F5). CLEAN for the other 25.
- **The 8 edited files** (`kanji/担 承 技 恋 愛 法`, `words/式 許可`): CLEAN on every facet. Only link brackets changed, each wrap sits at an EN link position, and the paths are correct (`../words/X.md` from kanji, `X.md` from words).
- **Intake JSON:** CLEAN. It has the same keys as the batch-161 record. It has 38 payloads, no duplicates, `held` is empty, and the notes are accurate.

Findings:

F1
- **Severity:** Minor. **Facet:** correctness.
- **Where:** `words/続き.md:41`
- **Claim and impact:** «続き называет то, что осталось, а не новое отдельное произведение» flatly denies the next-installment/sequel sense. That contradicts JMdict 1894690 sense 1 ("continuation; rest…; next installment; sequel"), the card's own L18, and EN L32 ("'sequel' is just one possible translation"). A learner would be taught a false restriction, for example for 映画の続き.
- **Remedy:** soften the line, e.g. «続き не обязательно означает новое отдельное произведение: …».
- **Evidence:** jisho/JMdict 1894690; EN `words/続き.md:15,32`.
- **Confidence:** high.

F2
- **Severity:** Minor. **Facet:** quiz safety.
- **Where:** `words/皿.md:9`
- **Claim and impact:** 皿 «тарелка; порция» has no exclusion against 料理 «готовка; кухня; блюдо».
  - JMdict 皿 sense 1 is "plate; dish; platter" and sense 2 is "serving; helping; course". Russian «блюдо» covers both the vessel and the course, so 料理's title is a defensible answer to a 皿 prompt.
  - The card itself glosses 皿 as «тарелка, блюдо (посуда)» (L16) and discusses the «блюдо» ambiguity against 料理 (L36–38).
- **Precedent:** RU お皿 already excludes 料理 (batch-043 adjudication: «блюдо» as serving vessel vs prepared food).
- **Remedy:** add 料理 to 皿 `quiz_exclusions`.
- **Evidence:** jisho/JMdict 皿; `words/お皿.md:9`; `words/料理.md` title.
- **Confidence:** medium-high.

F3
- **Severity:** Minor. **Facet:** quiz safety.
- **Where:** `words/苦手.md:4,9`
- **Claim and impact:** 苦手 «не силён (в чём-то); не по душе» has no exclusion against 弱い «слабый». «не силён» means «слаб (в чём-то)».
  - JMdict 苦手 sense 1 is "poor (at); weak (in)", and JMdict 弱い includes "unskilled" (数学に弱い).
  - Each title is therefore a defensible answer to the other word's prompt.
- **Precedent:** RU 下手 «неумелый» excludes 弱い. This guard was added in RU; EN 下手 has no exclusions.
- **Remedy:** add 弱い to 苦手.
- **Evidence:** jisho/JMdict 苦手 and 弱い; `words/下手.md:9`.
- **Confidence:** medium-high.

F4
- **Severity:** Minor. **Facet:** quiz safety.
- **Where:** `words/方法.md:9`
- **Claim and impact:** 方法 «способ; метод» has no exclusion against 泳ぎ方 «способ плавания».
  - The RU guards on 泳ぎ方 were added in batch 066: P09 泳ぎ方–仕方 «способ; приём» ("swimming method falls within способ; приём") and P08 泳ぎ方–方 ("standalone method").
  - The same reasoning applies directly to «способ; метод».
- **Remedy:** add 泳ぎ方 to 方法. Then judge 法 «закон; метод» the same way (the P08 logic). 手段 «способ достижения» is a weaker case.
- **Evidence:** `words/泳ぎ方.md:9` [方, 仕方, 技術, 手, 道, 道具]; `docs/translation-batches/066-leisure-sports-toys-and-sounds-independent-review-001.json:12` (P08/P09).
- **Confidence:** medium.

F5
- **Severity:** Minor. **Facet:** quiz safety.
- **Where:** `words/決まり.md:9`, `words/法.md:9`
- **Claim and impact:** the rules/law guards set in batch 075 (Q024 規則–法律, Q025 規則–約束) are not mirrored here.
  - **(a) 決まり vs 約束.** 決まり «правило; установленный порядок» has no exclusion against 約束 «обещание; договорённость». JMdict 決まり sense 2 is "agreement; arrangement", and 約束 sense 3 is "convention; rule". The card itself says 決まり «может описывать бытовую договорённость» (L35), so each title is a defensible answer for the other. Confidence: medium-high.
  - **(b) 法 vs 規則.** 法 «закон; метод» has no exclusion against 規則 «правила». This is the same relation as the guarded 規則–法律 «закон; законодательство» pair (Q024). Confidence: medium.
- **Remedy:** add 約束 to 決まり, and add 規則 to 法. Both gaps are inherited from EN, which guards neither pair, but the RU precedent makes these pairs direct.
- **Evidence:** jisho/JMdict 決まり, 約束, 法 and 規則; `words/規則.md:9` [法律, 約束]; `docs/translation-batches/075-public-life-commerce-and-services-independent-review.json:497,515`.

Optional:
- `words/続き.md:17`: «остальное из N» is unnatural. Suggest «остальная часть N».
- 続き «…; оставшаяся часть» and ほか «другой; остальное» are near-synonymous glosses in Russian. EN shares the same overlap ("the rest") without a guard. The meanings do differ (the remaining continuation vs others besides X). A guard would be cheap.
- 苦手 vs 欠点 «недостаток; слабая сторона»: in noun use (数学は苦手だ) 苦手 can read as «слабая сторона». Low risk.
- 決まり vs 習慣 «привычка; обычай» (JMdict 決まり sense 3 is "habit; custom"), and 決まり vs 法律 (Q024 logic). Low risk; the card teaches the rule and decision senses and contrasts 決まり with закон at L40.
- `words/見送り.md:20`: «Покупку новой машины отложили» reads in Russian as a car (新しい機械). Suggest «нового оборудования/станка».
- `words/演技.md:17`: «произвольная программа гимнаста» narrows EN "a gymnast's routine". Suggest «программа (выступление) гимнаста».
- `words/恋.md:26`: «влюбление» is a nonstandard noun. Suggest «…и не требует, чтобы человек влюблялся именно в этот момент».
- 感心 «…похвальный» and ほめる «хвалить» share a stem, but they differ in meaning and part of speech. No guard is needed unless the screen policy requires one.

Limits:
- I claim no native-speaker authority. Russian naturalness reflects my own judgement.
- I checked JMdict senses only for the words listed in Scope (jisho API). Other sense claims were checked against EN and general knowledge.
- The repo validator, `build_manifest.py` and the app were not run, as instructed. `manifest.json` is out of scope.
- Quiz risk was judged from the current RU titles plus the recorded precedent rationale. These pairs are direct and non-transitive, and each needs its own owner decision.
- `!!` lines from the title screen that I did not list were judged false positives: сторона, часть, провод, номер, использ-, средство, участок/ответ, признак, любование, and порядок (now guarded).
