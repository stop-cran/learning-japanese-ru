# B216 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `034ab7ea9034db0f24f7d8dfdad1f16af819e788` (tree `ca36d09f0ff3b18b6aa66d1ac4e8f2fbcf82f41c`),
> the signed candidate pushed before review.
> Later reconciliation is in `216-words-batch-55-recheck-001.md`.

Snapshot: RU 034ab7ea9034db0f24f7d8dfdad1f16af819e788, compared with parent f5a640351bde47476d96b060149ad76a1884e799. HEAD matched and git status --porcelain was empty at opening and closing; no uncommitted changes included. Frozen EN HEAD verified as 6af98cb717755690a9ca793e5454a96ebd7a8f9f.

Scope: Independent blind, read-only CORRECTNESS and SCOPED COVERAGE review. Actual reviewer model is not independently verifiable. Each of the following RU files was read IN FULL against its complete frozen EN original:

- words/勧める.md
- words/勢い.md
- words/勝ち.md
- words/勘.md
- words/動詞.md
- words/勇気.md
- words/効く.md
- words/助手.md
- words/劣る.md
- words/加わる.md
- words/劇場.md
- words/劇.md
- words/割る.md
- words/前者.md
- words/刺激.md
- words/制度.md
- words/到着.md
- words/利益.md
- words/別れ.md
- words/別に.md
- words/列車.md
- words/列.md
- words/刑事.md
- words/刈る.md
- words/切れる.md
- words/切れ.md
- words/分野.md
- words/分析.md
- words/分ける.md
- words/分.md

The three binding instruction/reference files were read. Existing comparison-card title/exclusion fields and the candidate's existing-card link diffs were checked; 負ける, 譲る, 加える, 足す, 特に, 番, 別 and 機関 were additionally read in full for relevant conventions and senses. This is not a full linguistic re-review of those baseline cards.

Verdicts: CORRECTNESS CLEAN; SCOPED COVERAGE CLEAN, for all 30 named new cards. No per-article exceptions. CLEAN means no actionable defect established in this bounded review.

Findings: None.

Evidence and checks:

- Read the actual Jisho/JMdict API entries, forms, parts of speech, sense restrictions and notes for all 30 headwords, separating distinct readings/entries and excluding Wikipedia senses. Also inspected the 21 RU-introduced guard comparators and 検査/血液検査. For example, [勧める](https://jisho.org/api/v1/search/words?keyword=勧める) retains the sense-local spelling restrictions; [効く](https://jisho.org/api/v1/search/words?keyword=効く) supports the 効く/利く spelling tendency; [分](https://jisho.org/api/v1/search/words?keyword=分) separates ぶ and ぶん and supports the three measurement scales. No new sense was inferred merely from a shared spelling.
- [Weblio / Digital Daijisen, 加わる](https://www.weblio.jp/content/%E5%8A%A0%E3%82%8F%E3%82%8B), sense 3, explicitly gives 暑さが加わる; sense 4 gives 圧力が加わる. [Digital Daijisen, 度](https://kotobank.jp/word/%E5%BA%A6-102903), ド sense 2, explicitly lists 制度 under the standard/model sense.
- Russian localization claims were checked in actual dictionary entries, not search summaries: Gramota's Kuznetsov [театр](https://gramota.ru/meta/teatr), senses 1 and 3, supports art/building; [играть](https://gramota.ru/meta/igrat), senses 2–4, supports games/sport, instruments and stage acting; Babenko [драма](https://gramota.ru/meta/drama), sense 2, supports the broad literary category distinguished from the narrower genre.
- Kuznetsov [очередь](https://gramota.ru/meta/ochered), senses 1–2, supports the queue/turn distinction; [анализ](https://gramota.ru/meta/analiz), sense 3's medical subsense, supports the Russian medical use. The inspected [血液検査](https://jisho.org/api/v1/search/words?keyword=血液検査) entry explicitly means blood test. The RU note says “обычно”, not that scientific analysis of blood can never be 分析.
- Kuznetsov [сыщик](https://gramota.ru/meta/syshchik), sense 2, and Babenko's corresponding entry support the investigator sense; [жать](https://gramota.ru/meta/zhat), second homonym, supports reaping cereal crops, not arbitrary harvesting. Wiktionary [острота](https://ru.wiktionary.org/wiki/острота), **острота́** sense 1, explicitly gives cutting/piercing ability and “острота ножа”; the separate **остро́та** entry concerns a joke and was not used as evidence for sharpness.
- Further Russian title/adaptation checks used actual Gramota entries and relevant senses for уступить (4), делить (arithmetic sense 4), поезд (1), область (5), особый/особо, кончиться (2), часть (2), польза, интерес (5), учредить (2), рекомендовать, советовать, предлагать, действовать, добавлять, присоединяться, рвать and полицейский. Cross-references from abbreviated entries were followed where needed.
- [利益](https://jisho.org/api/v1/search/words?keyword=利益), sense 2, groups benefit/advantage/good/interests together. Its RU body explicitly preserves “чьи-либо интересы” and 人の利益を守る. The short title's “выгода; польза” therefore does not remove a taught sense; adding “интересы” to the title is not required to repair an established coverage defect. 前者's “первый из двух названных” preserves the first-mentioned reference rather than temporal precedence.
- All 63 bullet-example Japanese sentences and their complete kana lines were mechanically confirmed verbatim, supplementing full manual reading of their Russian translations. No erroneous polarity, argument-role, event-stage or obligatory-gender rule was established. Masculine first-person Russian past-tense examples are contextual renderings, not claims that the gender-neutral Japanese speaker must be male.
- Source word/reading/JLPT/type/kanji/tags fields match; every source exclusion is retained. All source external URLs remain, no source relative link with an existing RU target was dropped, and the 30 cards contain no broken relative links. Missing RU targets are appropriately plain text. Reading-join/script explanations and all Japanese teaching points are retained. The omitted EN-only “tutor/spouse”, “(ordinary)” provenance wording and computer-file contrast do not remove a Japanese rule from these RU cards.

Optional: None.

Limits: No native-speaker certification, app/device test, complete quiz-pool audit, source-archive identity audit or fresh linguistic review of the entire baseline corpus is claimed. Dictionary evidence establishes the inspected meanings and restrictions, not corpus frequency. No validators or generators were run. Prohibited author/reviewer/batch/tracking/draft materials and scratch worktrees were not consulted; no nested reviewer was used. Only this report was written.
