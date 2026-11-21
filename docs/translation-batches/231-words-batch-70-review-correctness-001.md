# B231 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5af5353eab033af178249f39b48ac4200abf5c24` (tree `f0e6d8ef3d9983f842128471acff66dfe5a652bc`),
> the signed candidate pushed before review.
> Later reconciliation is in `231-words-batch-70-recheck-001.md`.

Snapshot: RU candidate 5af5353eab033af178249f39b48ac4200abf5c24, compared with parent 2e53d62d1a5408b4beefd4507edcbd4d7d76e04f; frozen EN source 6af98cb. Initial and final RU HEAD match the candidate; git status --porcelain is empty at both checks. No uncommitted changes included. Read-only review; only this report written.

Scope: Independent blind review of correctness and scoped coverage. Actual model identity/family is not independently verifiable in this reviewer context; no model-specific claim is made. Each entry below means the COMPLETE RU file and COMPLETE corresponding frozen EN file were read, not sampled. Paths are words/<entry>.md in their respective repositories.

| File | Full RU + EN read | Correctness | Scoped coverage |
|---|---|---|---|
| コース.md | Yes | CLEAN | CLEAN |
| 針路.md | Yes | CLEAN | CLEAN |
| 釜.md | Yes | CLEAN | CLEAN |
| 釘.md | Yes | CLEAN | CLEAN |
| 金魚.md | Yes | CLEAN | CLEAN |
| 重量.md | Yes | CLEAN | CLEAN |
| アクセント.md | Yes | CLEAN | CLEAN |
| 重点.md | Yes | CLEAN | CLEAN |
| 重役.md | Yes | CLEAN | CLEAN |
| 引力.md | Yes | CLEAN | CLEAN |
| 重力.md | Yes | CLEAN | CLEAN |
| 重体.md | Yes | CLEAN | CLEAN |
| 重なる.md | Yes | CLEAN | CLEAN |
| 重ねる.md | Yes | CLEAN | CLEAN |
| 重たい.md | Yes | CLEAN | CLEAN |
| 下品.md | Yes | CLEAN | CLEAN |
| だらしない.md | Yes | CLEAN | CLEAN |
| みじめ.md | Yes | CLEAN | CLEAN |
| みっともない.md | Yes | CLEAN | CLEAN |
| 醜い.md | Yes | CLEAN | CLEAN |
| 酸性.md | Yes | CLEAN | CLEAN |
| 酸っぱい.md | Yes | CLEAN | CLEAN |
| 酢.md | Yes | CLEAN | CLEAN |
| 酒場.md | Yes | CLEAN | CLEAN |
| 給与.md | Yes | CLEAN | CLEAN |
| 配る.md | Yes | CLEAN | CLEAN |
| 汲む.md | Yes | NEEDS FIX (C1) | CLEAN |
| 酌む.md | Yes | NEEDS FIX (C1) | CLEAN |
| 都心.md | Yes | CLEAN | CLEAN |
| 郵送.md | Yes | CLEAN | CLEAN |

Also read complete existing RU comparisons 課程, 方向, 重い, 鯉, 魚, ピン, 鍋, 強調 and 発音; checked selected other comparison titles without treating those cards as fully reviewed. Read all six existing-card runtime diffs: kanji/魚.md and words/魚.md, 甘い.md, 積む.md, 能力.md, 鉢.md. Their added links retain the displayed teaching meanings. Author/reviewer reports, title-screen output, translation-batch/draft records and translation tracking were not consulted.

Verdicts: Correctness NEEDS FIX, limited to minor Russian spelling C1 in 汲む and 酌む; the other 28 new cards CLEAN. Scoped coverage CLEAN for all 30. No substantive Japanese meaning, attachment, transitivity, polarity or tense defect established. CLEAN is bounded absence of an established actionable defect, not exhaustive linguistic certification.

Findings:

C1; Minor; correctness (Russian orthography); words/酌む.md:4,12,16,19-20,27,33,41,44 and words/汲む.md:34.
- Claim/impact: the established Russian borrowing is repeatedly printed «сакэ», including the 酌む title and model translations. Standard Russian spelling is «саке». This teaches a nonstandard spelling of the Russian gloss; it does not change the Japanese sense, reading or the 汲む/酌む distinction.
- Exact remedy: replace Russian «сакэ» with «саке» at those occurrences, including the front-matter title and heading; leave Japanese 酒/さけ and the Japanese examples unchanged.
- Evidence: the actual Russian Orthographic Dictionary entry on Gramota, https://gramota.ru/poisk?query=саке&mode=slovari, records «саке́, нескл., ж. и с.». The directly inspected answer https://gramota.ru/spravka/vopros/309247 explicitly lists «саке» among foreign common nouns ending in е after consonants. Its separate discussion of Japanese proper-name transcription does not exempt this common noun.
- Confidence: high. Severity remains minor because the intended drink and Japanese lesson are clear.

Preservation/evidence checks supporting the verdicts:
- No EN sense, example, consequential qualification or Japanese teaching distinction was found missing. Source-only English comparisons need not be reproduced literally: preserving the Japanese distinction, not translating English ambiguity into an artificial Russian rule, is the criterion.
- Stable metadata retained. Changes to exclusions are additions (重体: 状態/具合; 下品: いかがわしい), not lost baseline guards. No missing relative target or dropped EN link whose RU target exists was detected. Plain-text pointers to unavailable RU targets are permitted. All 30 files retain their EN seven-digit citation identifiers and external source URLs; this was also compared mechanically.
- Actual Jisho/JMdict entries and Japanese dictionary sections were inspected, not merely search snippets. Reading/spelling flags checked include 重役's obsolete おもやく versus executive じゅうやく, rare 見憎い for 醜い, and rare 醋/酸 read す for 酢. An alternate reading or rare spelling is not itself an error.
- Examples of consequential source checks: https://www.weblio.jp/content/針路 (Daijisen: navigational course and intended direction); https://www.weblio.jp/content/重役 (separate readings/senses); https://www.weblio.jp/content/重点 (important point and iteration mark); https://www.weblio.jp/content/重体 (life-endangering illness/injury); https://www.weblio.jp/content/給与 (money/goods supplied, including 制服を給与する); https://www.weblio.jp/content/酌む (combined entry and spelling note for serving alcohol). For 釜, the actual World Encyclopedia/Nipponica sections at https://kotobank.jp/word/釜-46502 support ceramic/metal vessels; the unrelated opening character-dictionary block was not substituted for the lexical evidence.
- The broader コース meal/service uses are supported by the actual Jisho/JMdict family; Daijisen alone was not treated as proving every sense. The extra katakana/no-kanji section is accurate and harmless. Russian past-tense masculine forms and contextually supplied pronouns do not assert that Japanese grammar encodes those features.
- Read-only validation: python -X utf8 -B tools/validate.py completed successfully: 0 error(s). No manifest builder or other generator was run.

Optional:
- Outside assigned facets: wording polish in words/下品.md:39-40 and words/酸っぱい.md:40-41. These retain source-list/dictionary-gloss framing that a Russian learner does not need. For 下品, simply «Не используйте 下品 как общее слово для скупости» retains the Japanese point. For 酸っぱい, «Здесь речь о кислом вкусе, а не об измерении кислотности» avoids treating English “acid” as a Russian dictionary gloss. The existing Japanese contrasts remain correct; these are not additional correctness findings.
- Nonblocking title precision in words/重たい.md:4,12: consider «тяжёлый; гнетущий (об атмосфере)» instead of «увесистый; гнетущий (об атмосфере)». Gramota's Kuznetsov entry for «увесистый» emphasizes considerable weight, whereas 重たい is the ordinary heavy/weighty adjective. The body already gives neutral «тяжёлый» and rejects an absolute objective/subjective split with 重い, so no categorical mistranslation is established.

Limits: This is not a full quiz-pool, native-speaker, device or whole-corpus review; comprehensibility/quiz safety were not assigned facets. All 30 pairs were fully read, but the much larger suggested comparison list was not fully read. Live lexical families and relevant flags were checked; the exact archived JMdict numeric ID/sense-version mapping was not independently reconstructed for every footer (retention was verified). Some live requests returned HTTP 429; actual alternate entries were used where possible, and a later Gramota repeat was rate-limited after its entry had already been inspected. No author evidence packet or other review was used to fill gaps. No consequential unresolved Japanese claim remains identified within this bounded review.
