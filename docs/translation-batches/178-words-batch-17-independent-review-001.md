# Batch 178 (`178-words-batch-17`) — independent review

## Snapshot
- Repo `learning-japanese-ru`, branch `full-ru-178-words-17`, candidate `43f30e7` (parent `dfc3227`). Working tree clean; nothing edited, staged or committed by the reviewer.
- EN source: `learning-japanese-en-frozen` (6af98cb).
- 44 files changed: 30 new `words/*.md`, the intake JSON (not read, as instructed), `manifest.json` (hash/contentVersion updates only), and 12 existing files (kanji 刊 副 匹 区 圧 差 幅 規; words 柳 梓 特徴 狂う). No generated or `__pycache__` files.
- Reviewer: Claude, read-only (kanji-accuracy-reviewer role), blind to the author report and prior reviews.

## Scope
- All 30 EN/RU article pairs read in full and compared sense by sense, note by note and example by example.
- Script check: every Japanese run in each EN article is present in the RU article (whitespace-normalised). 0 misses.
- `link_parity.py` on all changed files: no LOST links. Every link dropped relative to EN points to a page that does not exist in RU (for example kanji 準 幹 柳; words 床 新幹線 亥 丑 怪しい 効果 影響 印刷 発表 分ける 差別 共通 間違い 詩人). Two EXTRA links are valid RU targets: 基地:29 →基, 基盤; 素:31 →基本, 基礎.
- 12 navigation-only files: the word diff shows only link brackets added at the EN link positions. In 規.md, `[規準](../words/基準.md)` matches EN. 差.md:45 and 刊.md:20 are unlinked in EN as well.
- `word_title_screen.py` on the batch, then a manual check of the RU titles and `quiz_exclusions` in each semantic cluster (base/foundation, poetry, zodiac, strange, sameness, publishing, difference).
- A grep for leftover Latin text in learner-facing lines.
- Spot checks against JMdict through the jisho API (幹, 地盤) and Daijisen through weblio (地盤).

## Verdicts
- **Correctness: CLEAN.** Readings, types, senses, examples and translations are faithful to EN. F2 is a wording slip in a gloss, not a factual error.
- **Scoped coverage: CLEAN.** All EN senses, notes, examples, citations and exclusions are present. Link restorations are navigation-only and complete.
- **Comprehensibility: NEEDS FIX (minor).** F1 and F3 must be fixed; F2 should be.
- **Quiz safety: CLEAN.** The one residual pair (Q1) is EN-inherited and low-risk. It is listed for the author to decide on.

## Findings

**F1** — low — comprehensibility — `words/基地.md:33`
- Claim: «…не становится 基地 только потому, что по-английски обе можно назвать base.» The contrast is left in English. This breaks the methodology rule against English glosses in learner-facing text, and the argument means nothing to a Russian reader.
- Remedy: «…только потому, что по-русски обе можно назвать «базой» или «основой».» Either word works for both 台 and 基地 in Russian, so the warning still applies.
- Evidence: the line itself; `docs/translation-methodology.md` glossary section («Не оставляйте английские глоссы…»).
- Confidence: high.

**F2** — low — comprehensibility/correctness — `words/区別.md:21`
- Claim: «区別がつかない значит «не могу отличить». Подлежащее здесь — само различие, а не человек…». The gloss adds a first-person subject, and the very next sentence says there isn't one. A learner gets two conflicting messages.
- Remedy: gloss it impersonally, for example «различить невозможно; разницы не видно».
- Evidence: 区別.md:21–22. Daijisen 区別がつく is intransitive with 区別 as the subject.
- Confidence: medium-high.

**F3** — low — comprehensibility — `words/副作用.md:35`
- Claim: «Русское «побочный эффект» в переносном смысле говорят и о последствиях решений» is ungrammatical: «говорят» has no correct object or preposition.
- Remedy: «Выражение «побочный эффект» по-русски употребляют и в переносном смысле — о последствиях решений; эта карточка учит прежде всего лекарственному значению из примеров.»
- Evidence: the line itself.
- Confidence: high.

**Q1** — low (EN-inherited) — quiz safety — `words/幹.md:4` vs `words/中心.md:4`
- Claim: 幹 «ствол дерева; костяк» and 中心 «центр; ядро; главная часть» have no guard on either side. JMdict 幹 sense 2 is "backbone; base; foundation". Some JMdict editions also list "main part; core", so «главная часть» could pass as a correct answer to a 幹 prompt.
- EN has the same gap: EN 中心 excludes only 真ん中, and EN 幹 does not exclude 中心. The risk is low because the RU 幹 title points to «ствол».
- Remedy (optional): add 中心 to 幹's `quiz_exclusions`, or accept the pair as is.
- Evidence: https://jisho.org/api/v1/search/words?keyword=幹; EN `words/中心.md` frontmatter.
- Confidence: medium.

## Checked, no defect established
- All Japanese examples and readings are kept verbatim. Sound changes and special readings (基盤 きばん, 地盤 じばん, 俳句, 川柳 せんりゅう, 巳 み, 寅 とら, 卯 う, 奇しい くすしい, 妖しい あやしい) are unchanged from EN.
- Added guards are justified by JMdict overlaps:
  - 素–基, 基本; 基地–基; 地盤–土; 幹–骨
  - 詩–句, 歌
  - 同一–一緒, 等しい; 同様–一緒, 等しい, 似る, そんな; 匹敵–並ぶ
  - 発行/出版/刊行–出す
  - 差–幅, 別; 区別–別; 違い–違う, 異なる, 相違, 別; 異なる–別; 相違–別
- Key pairs are guarded:
  - 違い–相違, 差–違い
  - 出版–発行; 刊行 against both 出版 and 発行
  - 巳–蛇, 寅–虎, 卯–兎/東
  - 奇しい against 疑わしい, いかがわしい, 変, おかしい, 珍しい; 妖しい–奇しい
- Zodiac titles follow the «X (знак зодиака)» precedent set by 辰 and 酉.
- English-only contrasts are well re-expressed in Russian: 素:31, 基地:29, 幹:30, 詩:33, 俳句:31, 圧力:33, 出版:31, 区別:33, 異なる:33, 妖しい:34.
- Polivanov transcription (хайку, хокку, сэнрю, хайкай) and glossary terms (онное чтение, годан, окуригана) are consistent.
- The remaining Latin words (素:35 prime, 同一:33 similarity, 区別:33 discrimination) are glossed as source-term citations, which is acceptable.
- 地盤 senses (ground / foundation / power base and constituency) match JMdict and Daijisen.

## Optional polish (non-blocking)
- 台.md:32 «в пределах тридцати с чем-то градусов» → «тридцать с лишним градусов».
- 同一.md:18 «Эти два — один и тот же продукт» → «Эти две вещи — …».
- 寅.md:24, 卯.md:24 «шестидесятеричного значения» (reads as base-60 numerals) → «значения в шестидесятилетнем цикле».
- 地盤.md:21 «избирательный округ кандидата» → «опора кандидата в избирательном округе». This is closer to Daijisen sense 3 (足場・勢力範囲).
- 副作用.md:16 «меня клонило в сон» → «меня стало клонить в сон», to show the onset.
- 副作用.md:35: the note could add that Japanese 副作用 also has a figurative sense (Daijisen sense 2).
- 発行 «выдача документов» and 支給 «выдача (денег, вещей)» share «выдача». The objects differ, so the risk is low; a guard is optional.
- 然る «такой; подобного рода» is not guarded against 同様, unlike そんな. This is marginal.

## Limits
- The app quiz pool was not run. Quiz safety rests on a manual check of titles and exclusions, and guards are not assumed to be transitive.
- Dictionary checks were limited to spot checks (jisho API for 幹 and 地盤, weblio Daijisen for 地盤). Other JMdict senses were judged against the EN citations.
- The intake JSON rationale and the author report were not read (blind review).
