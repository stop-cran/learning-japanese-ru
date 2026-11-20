# B203 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `d6e95d46124d66f60472825a8db483b5702688f7`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 202 tree `459ddef` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `203-words-batch-42-recheck-001.md`.

Snapshot: RU candidate tree `d6e95d46124d66f60472825a8db483b5702688f7`, base `459ddef`, detached HEAD `5dd9a78`, in `C:\Users\romanko\repos\learning-japanese-ru-b198`. The staged candidate is intentionally uncommitted relative to HEAD. Initial checks: `diff-index --cached --quiet <candidate>` exit 0; `diff --quiet` exit 0; untracked-file listing empty. EN source: frozen `6af98cb`, `C:\Users\romanko\repos\learning-japanese-en-frozen`.

Scope: Independent blind, read-only review of CORRECTNESS and SCOPED COVERAGE. Actual model identity is not independently verifiable. No other reviewers, author prompts/reports, batch records, translation drafts or tracking files were read.

The following files were EACH read IN FULL in both candidate RU and frozen EN, including front matter, every example, all body sections and citations:

1. `words/注目.md`
2. `words/注.md`
3. `words/泥.md`
4. `words/波.md`
5. `words/泡.md`
6. `words/泉.md`
7. `words/沖.md`
8. `words/意志.md`
9. `words/決心.md`
10. `words/汚染.md`
11. `words/汗.md`
12. `words/氷.md`
13. `words/気味.md`
14. `words/気候.md`
15. `words/かわいそう.md`
16. `words/哀れ.md`
17. `words/気の毒.md`
18. `words/好む.md`
19. `words/気に入る.md`
20. `words/氏.md`
21. `words/毛布.md`
22. `words/比較.md`
23. `words/毒.md`
24. `words/母親.md`
25. `words/殺す.md`
26. `words/残す.md`
27. `words/死亡.md`
28. `words/歩道.md`
29. `words/正確.md`
30. `words/正直.md`

Also read the three binding instruction/reference files in full; existing RU 注意, 意思, 汚す, 残念, 好き, 布団, 正しい and お母さん in full; and the complete changed integration hunks for kanji 亡/殺 and the eleven existing-word link updates. Other suggested comparison cards were not read in full; no whole-card verdict is issued for them. The 30 new cards, not the entire existing corpus, are the verdict scope.

Verdicts:
- Correctness: **NEEDS FIX** for `words/毛布.md` only (C1). **CLEAN** for the other 29 reviewed new cards.
- Scoped coverage: **NEEDS FIX** for `words/波.md` only (C2). **CLEAN** for the other 29 reviewed new cards.
- Russian comprehensibility and quiz safety: outside the assigned facets; no independent verdict.

Findings:

**C1; Minor; correctness; `words/毛布.md:32`; unresolved.**
The added Russian instruction says categorically: «одеяло не надевают глаголом для одежды вроде 着る». EN instead warns against translating *every* “put on” with a clothing verb: it does not prohibit 着る for every blanket use. The Russian turns a sensible example-specific collocation lesson into an unrestricted exclusion. Contemporary JMdict even records 着る毛布（きるもうふ）, “wearable blanket”; the prohibition is therefore broader than the evidence supports. A beginner should learn かける/かぶる here without being taught that 着る is impossible for the object in other uses.
Remedy: replace the final sentence with «Учите глаголы укрывания вместе с частицами: в приведённых ситуациях используются 毛布をかける и 毛布をかぶる.» No explanation of wearable blankets or dialects needs to be added.
Evidence: frozen EN `words/毛布.md:44–47`; actual JMdict-backed Jisho entries inspected through `https://jisho.org/api/v1/search/words?keyword=着る` (results 着る and 着る毛布; latter reading きるもうふ, noun, “wearable blanket”). Digital Daijisen [着る](https://www.weblio.jp/content/着る), sense 1, covers things worn around the body; its supplement also explicitly records earlier use with 布団. The historical note alone is not being used to assert unrestricted modern idiomaticity.
Confidence: high on the overbroad wording; this is a localized qualification defect, not an error in the two model examples.

**C2; Minor; scoped coverage; `words/波.md:30–32`; unresolved.**
The entire source Japanese gesture contrast 手を振る（てをふる）has disappeared. EN `words/波.md:32` explicitly distinguishes the noun 波 from waving one's hand and supplies that Japanese expression and reading. Removing the English-dependent wording is appropriate, but the assignment expressly requires retaining source examples and the Japanese teaching rule. The current replacement retains only the physical/figurative distinction and the height/time qualification. This is a source-coverage omission, not a claim that the surviving Russian is linguistically wrong or that Russian has the same polysemy as English.
Remedy: append «Жест „помахать рукой“ передают выражением 手を振る（てをふる）, а не существительным 波.» This preserves the source teaching point without requiring English.
Evidence: full frozen EN/RU comparison; an additional Japanese-string check found 手を振る and てをふる to be the only source Japanese runs longer than two characters absent from all corresponding RU text. Actual [JMdict-backed Jisho search for 手を振る](https://jisho.org/api/v1/search/words?keyword=手を振る) returned exact spelling 手を振る, reading てをふる, expression/godan-る, “to wave one's hand”.
Confidence: high that this source expression/rule was omitted; severity remains minor because the principal meanings and both main examples are intact.

Optional: None. C2 is tied to this assignment's explicit source-example retention requirement, not a general demand to expand a Russian beginner card with English polysemy.

Evidence and checks:
- All 59 main Japanese example sentences were independently checked for exact sentence-string retention: no mismatch. Their kana readings were also read in the paired full texts. Surrounding EN ASCII parentheses/spaces are systematically localized to RU full-width parentheses; this is typographic normalization, not literal whole-line byte identity.
- All source metadata other than localized titles and permitted additional exclusions matched in a field comparison. Source exclusions were retained. All source external citation targets remain. Nineteen source internal-link occurrences are plain text in RU because the corresponding optional target files do not exist there; their visible Japanese labels remain. No unavailable-target link is demanded.
- Inspected actual Jisho/JMdict lexical forms, parts of speech and senses for 注目, 注, 泥, 波, 泡, 泉, 沖, 意志, 決心, 汚染, 汗, 氷, 気候, 哀れ, 気の毒, 好む, 気に入る, 氏 (し and うじ separately), 毛布, 比較, 母親, 殺す, 残す and 正直. Later successful exact searches verified 気味 (noun きみ versus suffix ぎみ) and かわいそう. API URLs use `https://jisho.org/api/v1/search/words?keyword=<exact spelling>`; Wikipedia-definition objects were excluded from evidence.
- Some initial API requests returned HTTP 429. Actual Digital Daijisen entries were inspected instead for [毒](https://www.weblio.jp/content/毒) (ordinary noun senses 1–2, including 夜ふかしはからだに毒), [死亡](https://www.weblio.jp/content/死亡) (しぼう, 人が死ぬこと), [歩道](https://www.weblio.jp/content/歩道) (ほどう, pedestrian way distinguished from 車道), and [正確](https://www.weblio.jp/content/正確) (せいかく, factually correct/no error; derived 正確さ).
- Additional localized explanations were checked against actual Digital Daijisen entries [注意](https://www.weblio.jp/content/注意), senses 1–3; [汚す](https://www.weblio.jp/content/汚す), specifically よごす senses 1–2, not just けがす; [残念](https://www.weblio.jp/content/残念), senses 1–2; and [汗だく](https://www.weblio.jp/content/汗だく), あせだく, 汗びっしょり. The 可哀想 entry also explicitly identifies 可哀想/可哀相 as ateji.
- The new Russian «грязь» contrast was confirmed in [Gramota/Kuznetsov, грязь](https://gramota.ru/poisk?query=грязь&mode=slovari&dicts[]=42), senses 1–2: wet earth versus dust/rubbish/uncleanliness. The «воля» contrast was confirmed in [Gramota, воля](https://gramota.ru/poisk?query=воля&mode=slovari), Kuznetsov senses 1–2 versus 5 (freedom). These are independent verification sources, not claims that the cards themselves cite those Russian dictionaries.
- For 氏, inspected the cited [Digital Daijisen entry](https://www.weblio.jp/content/氏), specifically し suffix senses 1–2 and 藤原氏; and [精選版 日本国語大辞典](https://kotobank.jp/word/氏-34455), specifically うじ [1] senses 2–3 and the attested 氏をつがぬ. This was the named dictionary section, not the unrelated encyclopedia material on the aggregate page.
- `python -X utf8 -B tools\validate.py` on the candidate worktree completed with `0 error(s)`, exit 0. No manifest generator was run because this review is read-only.

Limits: This is not a full-corpus semantic/quiz audit, native-speaker certification, frequency study, etymological re-audit, archive/media/device acceptance or independent JLPT reassignment. Live dictionary responses are not frozen-source version receipts and the Jisho API does not expose every written-form rarity flag; unchanged EN source qualifications are not represented as newly established frequency evidence. An initially oversized diff and two oversized paired-read outputs were not counted as complete reads; all 30 card pairs were subsequently returned in bounded, readable full outputs.

Final integrity: candidate/index comparison exit 0; working-tree diff exit 0; untracked listing empty; HEAD remains `5dd9a78`. Only this report was intentionally written. No repository file, index or HEAD was changed.
