# B195 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `4a2fd76f6380d7478317c486f1042215190a5934` (tree `02afdeec8bfbf21e076e959600ab7ed18980f642`),
> the signed candidate pushed before review.
> Later reconciliation is in `195-words-batch-34-recheck-001.md`.

Snapshot: RU 4a2fd76f6380d7478317c486f1042215190a5934, branch full-ru-195-words-34; no uncommitted changes included. Initial and final HEAD/branch match; working tree was clean before and after the review. EN source HEAD confirmed as 6af98cb717755690a9ca793e5454a96ebd7a8f9f. Only this report was written.

Scope: BLIND, read-only correctness and scoped-coverage review of all thirty complete RU cards against their complete frozen EN originals:
表情, 衣服, 衝突, 衛星, 行儀, 行動, 行き, 虫歯, 作家, ライター, 著者, 菓子, 莫大, 苦しむ, 芸術, 芝生, 航空, 舞台, 舌, 臭い, 天然, 自然, 自殺, 自慢, 自動, 膝, 腰, 腐る, 脇, 才能.
Actual reviewer model is not independently verifiable.

Read RU binding instructions and format reference. Inspected runtime diff inventory and every changed passage in the seven reused word cards (尻, 袖, 詩人, 誇り, 轢く, 鉄道, 麒麟) and three kanji cards (才, 能, 舞); these changes only wrap existing text in links. For conventions and contrast checks, read complete baseline cards 表現, 顔, 笑顔, 様子, 服, 洋服, 上着, 着物, 喧嘩, 連れ, お菓子, 苦痛, 横, 言葉, 腕, 誇り, 行う, 動く, 運動, こと, 悩む, 苦しい, 草, 庭. Other suggested comparison cards were screened at title level only, not reported as full article reviews.

Verdicts:
- Correctness: CLEAN for all thirty cards within this scope; no actionable Japanese or Russian semantic defect established.
- Scoped coverage: NEEDS FIX for 衣服 only (C1); CLEAN for the other twenty-nine cards within this scope.
- Comprehensibility and comprehensive quiz/collection consistency are not assigned verdicts.

Findings:

C1; Minor; scoped coverage; words/衣服.md:45–48.
Claim and impact: The English-specific wording has been removed together with its underlying Japanese number rule. EN words/衣服.md:41–44 explicitly says that the plural translation does not require a Japanese plural ending. RU retains the category/context explanation but nowhere preserves that rule. This is a small standalone-card coverage omission, not an incorrect Japanese example.
Remedy: After line 47 add: «В этом употреблении 衣服 не требует специального окончания множественного числа.» The English comparison itself need not return.
Evidence: Direct comparison with frozen EN words/衣服.md:41–44; the existing RU words/服.md, first meaning paragraph, already explains that the Japanese noun does not distinguish singular and plural here. The exact Jisho/JMdict-backed 衣服 entry confirms the noun and reading, but is not claimed to be independent evidence for a general number rule: https://jisho.org/api/v1/search/words?keyword=%E8%A1%A3%E6%9C%8D .
Confidence: High for the omitted source rule; minor learning impact.

Evidence and checks:
- Read and compared every example translation and explanatory section. All 61 Japanese example sentence bullets retain their sentence bodies. Readings were compared in the complete paired reads; source ASCII reading delimiters have generally become RU full-width delimiters, a presentation normalization rather than a change to the Japanese sentence.
- In-memory comparison found no changes to source word/reading/JLPT/type/kanji/tags fields, no lost source quiz exclusion, and no lost external citation URL. Added exclusions were not treated as proof of quiz safety.
- All 24 removed relative-link destinations are absent from this RU snapshot; their explanatory text/labels remain in Russian, rather than being replaced with invented links. This includes the plain-text occupation/role-endings reference in 作家. No currently existing source-relative destination was silently dropped by this comparison.
- Ran `python -X utf8 -B tools\validate.py` directly in the RU candidate tree: exit 0, `0 error(s)`. Did not run the manifest generator or any writing validator.
- Independently fetched exact Jisho/JMdict-backed lexical entries for all thirty assigned words, including both separate ライター entries, both relevant 臭い readings, 行き's suffix-specific «usu. ゆき» note, 天然's colloquial abbreviation sense, 腰's texture sense, and 自動's grammatical abbreviation. Wikipedia definitions, place-name objects and unrelated readings were not used as lexical evidence. Three initial HTTP 429 responses (著者, 芸術, 自動) were subsequently resolved by spaced successful requests.
- Also inspected actual entries for 喧嘩, 連れ, お菓子, 苦痛 and 横 to check the added comparisons. For example, https://jisho.org/api/v1/search/words?keyword=%E6%A8%AA gives the separate «beside; aside; next to» sense, not an anatomical armpit sense; https://jisho.org/api/v1/search/words?keyword=%E8%A1%9D%E7%AA%81 gives both collision and quarrel/conflict senses.
- Inspected the actual Digital Daijisen 作家 entry, not merely the surrounding Kotobank aggregation: https://kotobank.jp/word/作家-510921 defines a creator of artistic works, especially a novelist. This supports retaining the ceramic-artist example rather than narrowing 作家 to literary authors. Inspected 著者 at https://kotobank.jp/word/著者-569443 and 自動 at https://kotobank.jp/word/自動-522031 as well.
- Checked Russian-only lexical adaptations against actual Russian entries: Kuznetsov «спутник» senses 1, 3 and 4 (travelling companion, natural satellite, artificial spacecraft), «колено» sense 2 and its «Сидеть на коленях у кого-л.» example, and «трава» senses 1–2 (plant versus vegetation cover). URLs: https://gufo.me/dict/kuznetsov/спутник ; https://gufo.me/dict/kuznetsov/колено ; https://gufo.me/dict/kuznetsov/трава . The simplified Gufo response omitted the main definitions; inspected their actual readable HTML definitions instead, not the related-dictionary snippets.
- Ozhegov/Shvedova's actual entries distinguish anatomical «язык» from the communication system and list «покончить с собой» without a criminal-register label: https://ozhegov.info/slovar/?q=язык ; https://ozhegov.info/slovar/?q=покончить . These support the RU 舌 adaptation and the factual 自殺 translation without treating a dictionary as proof of a universal editorial style preference.

Optional: None.

Limits: No author report, other reviewer report, RU batch records/drafts/tracking, or title-screen output was read. This is not a full baseline-corpus review, exhaustive quiz-pair audit, independent etymological reconstruction, corpus-frequency study, native-speaker certification or device test. Existing reviewed EN explanations were used as the translation baseline; dictionary recognition was not treated as proof of every example's frequency. Live Jisho exposes current lexical objects, not a byte-identical frozen JMdict dump or independently checked historical ent_seq assignments. Gramota returned HTTP 429 and the SPbU dictionary mirror HTTP 403; Russian checks used the actual alternative entries above. A direct Kotobank お菓子 URL returned 404; the successful exact JMdict-backed お菓子 entry and baseline RU card were used for that comparison. These access failures do not leave a consequential contrary claim unresolved.
