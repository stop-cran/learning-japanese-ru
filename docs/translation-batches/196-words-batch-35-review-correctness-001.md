# B196 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `dd399249fe65eeba0cef005a3655cc3bc1ab874f` (tree `2585cf658a0f2479ce3fae46abb0b9c5ba55ea23`),
> the signed candidate pushed before review.
> Later reconciliation is in `196-words-batch-35-recheck-001.md`.

Snapshot: RU dd399249fe65eeba0cef005a3655cc3bc1ab874f, compared with ccb75fd; working tree clean at intake and after validation, HEAD unchanged. Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f.

Scope: Blind, read-only correctness and scoped coverage. Read all 30 complete RU cards against their complete frozen EN originals: 能力, 能, 胃, 育つ, 肩, 皮, 肌, 職業, 職, 考慮, 考え, 老人, 老い, 翼, 羽, 美人, 罹る, 罰する, 罪, 缶, 繰り返す, 結ぶ, 繋ぐ, 綿, 保存, 維持, 絶滅, 絶対, 絵画, 給料. Read the three binding instruction/reference files. Fully read existing 才能, おなか, 革, 木綿, 必ず and きっと for conventions/comparisons; inspected the other suggested comparison titles, not their complete bodies. Inspected all 21 modified baseline word/kanji files' changes: each is link markup only, with unchanged visible prose. Checked new-card metadata, Japanese lexical runs, citation URLs, retained link labels and local targets. No author/reviewer reports or forbidden batch/tracking records read. Actual model identifier not independently verifiable.

Verdicts: correctness CLEAN for all 30 cards; scoped coverage NEEDS FIX for 綿 only (F1, minor source-preservation defect), CLEAN for the other 29. No incorrect Japanese pronunciation or Russian meaning established.

Findings:

F1; Minor; scoped coverage / exact Japanese-source preservation; words/綿.md:19.
Claim and impact: The reading of the first example changes frozen EN このしゃつはめんでできています。 to このシャツはめんでできています。. Both convey the same pronunciation, so this is not a linguistic error or a misleading translation. It nevertheless changes the Japanese reading sample contrary to the assignment's explicit verbatim/kana-preservation requirement; the difference is not Russian localization.
Remedy: Replace the complete line with:
- このシャツは綿でできています。（このしゃつはめんでできています。）— Эта рубашка из хлопка.
Evidence: Frozen EN words/綿.md:18 at 6af98cb versus RU words/綿.md:19 at dd39924. The exact Japanese-run comparison independently isolates this kana-script replacement; no other existing Japanese lexical run was replaced or deleted. Jisho/JMdict's separate 綿 entries confirm めん “cotton” and わた “cotton plant / batting, wadding, padding” (1533330 sense 1; 1533340 senses 1–2), but the finding concerns source fidelity, not those valid meanings: https://jisho.org/api/v1/search/words?keyword=%E7%B6%BF .
Confidence: High. Status: unresolved at the reviewed snapshot.

Evidence and positive checks:
- Inspected actual Jisho/JMdict API entries for every one of the 30 Japanese spellings, selecting the matching reading and excluding Wikipedia senses. All selected learner senses and relevant transitivity/class/reading restrictions fit the RU explanations. In particular, 羽 entry 1171680 distinguishes feather/wing, badminton はね, and hanetsuki 羽根; counter entry 1607310 is separate. 綿 retains its distinct めん/わた identities; 罪 retains culpability as well as crime/sin; 繋ぐ retains telephone transfer; 絶対 retains adverbial use versus の attachment.
- The actual full 缶 page, including Notes, marks 缶 as ateji and lists Dutch kan / English can plus the abbreviated canned-food sense: https://jisho.org/word/%E7%BC%B6 . The actual 罹る entry explicitly marks the disease sense as usually kana-written, without asserting rarity: https://jisho.org/word/%E7%BD%B9%E3%82%8B .
- Inspected the named 精選版 日本国語大辞典 subsection, not merely the first aggregator block, for 能がない: lack of ability/talent, resourcefulness or sufficient thought supports the qualified disparagement warning. https://kotobank.jp/word/%E8%83%BD%E3%81%8C%E3%81%AA%E3%81%84-596150 .
- Corroborated 能力's Russian “природную одарённость” description of 才能 with the actual デジタル大辞泉 and 精選版 日本国語大辞典 entries, which explicitly give 生まれつきの能力. This supports that emphasis, not a universal rule that learned abilities cannot be talent. https://kotobank.jp/word/%E6%89%8D%E8%83%BD-508270 .
- The Russian adaptation “старый друг” preserves the EN old-friend distinction. Gramota's actual СТАРЫЙ entry, sense 2.1, gives longstanding relations and explicitly lists друг: https://gramota.ru/poisk?query=%D1%81%D1%82%D0%B0%D1%80%D1%8B%D0%B9&mode=slovari .
- All EN front-matter fields other than localized title / expanded quiz_exclusions match; no original exclusion guard was lost. All source citation URLs are retained. The 21 removed internal-link instances point to cards absent from RU; every visible Japanese label remains, with readings supplied where needed. No broken local link was found in the 30 new cards. These bounded unlinkings are not omitted teaching content.
- Every EN learner sense, note and example remains represented in Russian. Readings, grammatical contrasts, tense/polarity, roles, register qualifications and example translations show no additional actionable defect. Conventional RU heading/parenthesis typography is distinguished from the kana-content replacement in F1.
- Ran `python -X utf8 -B tools\validate.py` on the existing candidate tree: exit 0, 0 errors. No generator was run and no repository file was written.

Optional: None.

Limits: CLEAN is bounded to the assigned facets, not exhaustive linguistic certification. No comprehensive quiz-safety/whole-pool audit or comprehensibility verdict; most comparison cards were title-screened only. Live dictionary entries were inspected, not independently hash-matched historical JMdict releases; API responses omit some spelling-local notes, so the consequential 缶 ateji claim was checked on the full page. Native-speaker, corpus-frequency, app/device/media and publication checks were not performed. Structural validation does not establish semantic correctness. The earlier oversized combined diff output was not treated as a completed read: all 30 pairs were subsequently returned in full in bounded reads, and all modified baseline changes were separately checked. Only this report was written.
