# B190 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `0462ca5d05879b79e3fc4c28893b707b1c7af588`.
> Later reconciliation is in `190-words-batch-29-recheck-001.md`.

Snapshot: RU 0462ca5d05879b79e3fc4c28893b707b1c7af588, branch full-ru-190-words-29; clean worktree confirmed before and after review. Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f. No uncommitted content included.

Scope: Independent blind, read-only correctness and scoped-coverage review. All 30 new cards read in full against their frozen EN originals: 通り, 通す, 通じる, 瞬間, 途端, 逆らう, 逆, 追う, 追い付く, 迷惑, 迷子, 述べる, 現代, 近代, 迎え, 辺り, 農民, 農業, 農家, 辞める, 轢く, 丸, 輪, 転ぶ, 軒, 軍隊, 軍, 身長, 自身, 身. All 40 suggested existing RU comparison cards read in full. Inspected runtime diffs against 5bfe405, including the eight baseline edits: kanji/丸.md, kanji/追.md and words/止める.md, 現在.md, 背.md, 見送り.md, 面倒.md, 順.md. These baseline edits add navigation links. Actual model identifier/override is not independently verifiable in this runtime.

Verdicts:
- Correctness: NEEDS FIX (F1; F2's missing claim-matched evidence). The Russian historical-periodization addition in 近代 remains UNVERIFIED, not established false. 輪's frequency qualifier is likewise unsupported by the inspected dictionary. Other reviewed passages have no established actionable correctness defect.
- Scoped coverage: NEEDS FIX for 通じる only (F1's dropped qualification); CLEAN for the other 29 new cards and inspected baseline edits. All original front-matter identity/readings/levels/types/tags/kanji/exclusions are retained; added exclusions do not remove original ones. Japanese example/kana sequences are retained. Removed Markdown links target cards unavailable in RU, with visible labels/readings retained; these are not coverage defects. No other omitted EN sense, note, example, citation or required rule established.

Findings:

F1; Minor; correctness and scoped coverage; words/通じる.md:36–37.
Claim/impact: “Он не заменяет 通じる в значениях, связанных с общением” makes the comparison categorical. EN says “It is not a replacement for every communication use of 通じる.” Losing “every” overstates the separation and conceals 通る's own communication-related senses.
Exact remedy: Replace line 37 with “Однако 通る нельзя автоматически подставлять вместо 通じる во всех конструкциях, связанных с общением.”
Evidence: Frozen EN words/通じる.md, corresponding comparison paragraph. Actual [Jisho/JMdict 通る](https://jisho.org/word/通る), entry 1433030: sense 7 relayed/conveyed, sense 10 comprehensible/make sense, sense 11 get one's point across/be understood. These establish overlap, not unrestricted interchangeability. Actual [Digital Daijisen 通る](https://www.weblio.jp/content/通る), 4㋑, also documents intelligible content with 理屈が通っている; its sense 5 has a classical quotation and is not being presented as modern colloquial substitution evidence.
Confidence: High about the missing source qualification and excessive categorical wording. No claim that all constructions permit substitution.

F2; Minor; correctness/evidence support; words/近代.md:33–35, 農民.md:34–36, 丸.md:20,34, 輪.md:31,37, 軍隊.md:32–34, 軍.md:33–35, 身長.md:33–35, 自身.md:33–35.
Claim/impact: These Russian-only lexical/historical explanations cite only JMdict Japanese headword entries. Those citations support the Japanese meanings, not the added assertions about Russian usage. This fails the assignment's explicit requirement that Russian-only claims be supported by the dictionary cited. It is principally a traceability gap, not eight demonstrated mistranslations.
Remedy: Add claim-matched Russian dictionary citations for the lexical additions, keeping the JMdict citations for Japanese. For 輪, replace “Русское «кольцо» часто понимают как украшение” with “Русское «кольцо» может обозначать украшение”: a dictionary establishes that sense, not its frequency of interpretation. For 近代, inspect and cite an accessible reputable Russian historical-periodization source; if unavailable, remove the unsupported dating assertion and retain a narrower caution such as “Не приравнивайте русское название исторического периода к 近代 без проверки принятой периодизации.” Do not remove the independently supported Japanese Meiji–WWII explanation.
Actual inspected evidence:
- [Kuznetsov, крестьянин](https://gramota.ru/poisk?query=крестьянин&mode=slovari): farming/rural-person sense and separate pre-1917 estate sense support the qualified lexical contrast. They do not prove a general frequency claim.
- [Kuznetsov, месяц](https://gramota.ru/meta/mesyats): time-unit sense and conversational moon sense support 丸's Russian ambiguity note.
- [Kuznetsov, кольцо](https://gramota.ru/poisk?query=кольцо&mode=slovari&dicts%5B%5D=42): sense 1 hoop-shaped object and sense 2 finger jewelry support polysemy, not “часто”.
- [Kuznetsov, армия](https://gramota.ru/poisk?query=армия&mode=slovari): senses 1–2 distinguish all armed forces from land forces, supporting both military-card additions.
- [Kuznetsov, рост](https://gramota.ru/poisk?query=рост&mode=slovari&dicts%5B%5D=42): senses 1–2 distinguish growth/development from stature, supporting 身長.
- [Kuznetsov, сам](https://gramota.ru/poisk?query=сам&mode=slovari&dicts%5B%5D=42): I.1–2 distinguish personal participation from independent action, supporting 自身's qualified contrast.
- Actual JMdict 近代 entry 1242420, senses 1–2, supports the Japanese recent/modern-era meanings and Meiji Restoration–WWII period, not the Russian “Новое время” dating assertion. Attempts to inspect the relevant Russian encyclopedia entry failed or yielded only other-entry summaries; search snippets are not verification.
Confidence: High for citation mismatch, confirmed lexical senses and the frequency-evidence boundary; no independent substantive verdict on the Russian historical dating claim.

Optional: None beyond the remedies above. No broader synonym expansion requested.

Limits: Lexical Jisho/JMdict entries inspected for all 30 headwords, separating alternate readings/senses. Additional actual entries inspected include Digital Daijisen 通り, 通す, 通ずる, 逆らう, 迷惑, 通る and 一軒; Kotobank 軒 (including the separate counter/eaves entries and voiced-counter note); full Jisho 述べる spelling notes; Bunpro たとたんに; and the Russian dictionary entries cited above. This is a bounded editorial review, not exhaustive corpus, frequency or native-speaker certification. The Russian historical assertion and 輪's “часто” remain unverified as specified in F2. Some initial grouped reads exceeded output limits; affected card reads were repeated in smaller, untruncated groups before being counted as full reads. No author report/prompt, other reviewer report, title-screen output or excluded translation records were read. No quiz-pool/manifest integration audit or comprehensibility-facet verdict is claimed. No repository files changed and no generators or publication operations run.
