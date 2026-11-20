# B197 consistency and quiz-safety review (batch `197-words-batch-36`)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5dd9a78f4e6d2f806be09953326bf77cb8e77c47` (tree `aa153ae4edbd312c5336da1a9ad2a142f9433e60`),
> the signed candidate pushed before review.
> Later reconciliation is in `197-words-batch-36-recheck-001.md`.

Snapshot: RU `full-ru-197-words-36` at 5dd9a78 (HEAD confirmed, parent 59b6e51); working tree clean before and after my checks. Frozen EN 6af98cb.
Scope: facets CONSISTENCY, QUIZ SAFETY and scoped cross-file integration only (no correctness/comprehensibility verdict). Read in full: the 30 new `words/*.md` cards against their EN originals' front matter and (for links/exclusions) bodies; diffs of the 11 navigation-only files; manifest; `docs/translation-batches/197-words-batch-36-intake.json`. Own tools: `tools/validate.py` (0 errors), `tools/build_manifest.py` (regeneration produced no diff, so the committed manifest is not stale), `link_parity.py` (41 changed files: no LOST/EXTRA; a whole-tree run shows only pre-existing LOST/EXTRA unrelated to batch words), an own overlap screen of every new title (word-stem and exact-segment) against all 2,563 RU word titles. Model: not verifiable from my runtime.
Verdicts:
- Consistency: CLEAN. Front matter (all fields except title/quiz_exclusions) is identical to EN for all 30 cards; commit contains exactly 43 files (30 cards, 11 restorations, manifest, intake), no stray files; all 41 intake payload hashes recompute (candidate, EN source raw and normalized) and the source commit matches.
- Quiz safety: CLEAN. All EN exclusions are retained; no missing required guard found; every exclusion target exists as a card; no new title equals another card's whole title or a title segment.
- Scoped coverage (cross-file integration): CLEAN. The 16 restored links sit at EN link positions; hrefs resolve to existing RU cards (kanji/ pages use ../words/, word pages use bare names); only link brackets/hrefs changed (diff -U0 confirms no prose change). No new Russian-only link.
Findings: none (0 Critical / 0 Major / 0 Minor).

Basis and necessity of every exclusion beyond the EN file (dictionary basis is the JMdict sense as cited in the card/EN source; I did not re-fetch entries, see Limits):
- 結論→判断: 判断 title «суждение; вывод» shares «вывод» with 結論 «итоговый вывод»; JMdict 判断 includes a "conclusion/decision" sense. REQUIRED (Russian title overlap).
- 今に→もうすぐ: 今に sense «before long; soon» = もうすぐ «скоро». REQUIRED.
- 今に→いずれ: いずれ «рано или поздно» also points at an indefinite future; titles differ in nuance. CONSERVATIVE (real basis, necessity unestablished).
- いずれ→どの, どっち: いずれ pronoun sense «which (of several/two)»; どの is prenominal «which», どっち is the colloquial どちら (EN already guards どれ/どちら). CONSERVATIVE.
- 結局→末: 末 title «конец; в итоге», 結局 «в конечном счёте». REQUIRED (title overlap; no EN guard exists).
- 経由→通過: 経由 «via» vs 通過 «проход через»; titles share «через». CONSERVATIVE (body teaches the contrast; necessity in an ordinary quiz not established).
- 営業→売る: 営業 «продажи» vs 売る «продавать» (stem overlap, different part of speech). CONSERVATIVE.
- 態度→行儀: 態度 «манера держаться» vs 行儀 «манеры; поведение». REQUIRED.
- 位置→所, 場: 所 «место; участок», 場 «место; обстановка»; analogous to the EN-guarded 場所 but weaker. CONSERVATIVE.
- 立場→見解: 立場 «угол зрения» vs 見解 «точка зрения; позиция». REQUIRED.
- 位→くらい: same spelling/reading (JMdict lists 位 as a writing of くらい/ぐらい); the card itself teaches the homograph. CONSERVATIVE.
- 級→水準: both titles lead with «уровень». REQUIRED.
- 納得→承知: 承知 «согласие» vs 納得 «принятие (доводов)»; JMdict senses both include consent/agreement. REQUIRED.
- 精々→以下: «самое большее» vs «не больше». REQUIRED.
- 範囲→額: shared «рамки/рамка» (額 title «рамка; сумма»). CONSERVATIVE (the figurative/picture-frame senses are different words; harmless).
- 節約→省く: 省く «экономить (силы)» vs 節約 «экономия». REQUIRED (title overlap).
- 節→曲: 曲 «мелодия» vs 節 «напев». REQUIRED.
- 節→特徴: both titles end in «черта». REQUIRED.
- 節→点: 点 «аспект»; the card itself notes 点 as «пункт в рассуждении». CONSERVATIVE.
- 答案→答: 答 «ответ; решение». REQUIRED.
- 筆→手: 手 title «рука; кисть» vs 筆 «кисть для письма». REQUIRED.
No exclusion is UNJUSTIFIED (none guards a mere topical relation or an antonym that the article uses as its contrast).

Optional (nonblocking, none required):
- O1 組合 vs 団体 (and 組織): 団体 «группа; организация» is a plausible loose answer for «объединение»; the EN-style pair is only 組合→会 (団体 is already declared on 会). Low confidence it matters; add `団体` only if the owner wants a conservative guard.
- O2 節約 vs 貯金: Russian «экономия» vs «сбережения» are near in Russian, though 貯金's title adds «откладывание денег»; no EN guard. Not established as necessary; conservative `貯金` could be added to 節約 if desired.
- O3 今に «в скором будущем» vs 先 «…в будущем»: weak overlap; not recommended.
- O4 The RU cards add comparison sentences not present in EN (e.g. 通過 in 経由, 承知 in 納得, 所/場 in 位置, 以下 in 精々, 額 in 範囲, 省く in 節約, 曲/特徴 in 節, 手 in 筆) to support the extra guards. They are unlinked, so link parity holds. Their linguistic accuracy is a correctness-facet question I did not assess.

Limits:
- I did not re-fetch JMdict entries; "dictionary basis" above rests on the senses cited in the cards and the existing RU titles, so entry-level confirmation of each sense is UNVERIFIED by me.
- Title screening is by Russian stem/segment overlap plus manual judgment against ~100 named comparison cards; synonymy without shared vocabulary (e.g. 結果 vs 合計 «итог», 結論 vs 結果, 範囲 vs 限界) was judged by reading and not found defensible, but is a judgment call.
- Did not read author reports, other reviewers' reports, title-screen outputs, or RU translation-batches records other than the intake JSON that is in scope; no other facet (correctness, comprehensibility) is assessed.
