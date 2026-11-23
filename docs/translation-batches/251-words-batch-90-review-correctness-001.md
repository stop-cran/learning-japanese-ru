# B251 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `8bb7b574df56eb149c7b7c22a70aae4cde4bbee6` (tree `af91f2d01fc3555bf1190ac60079f79715e80cb7`),
> the signed candidate pushed before review.
> Later reconciliation is in `251-words-batch-90-recheck-001.md`.

Snapshot: RU candidate 8bb7b574df56eb149c7b7c22a70aae4cde4bbee6, parent 9b8a497e9d561e519351c2492fc4b5b186637b25. HEAD matches; git status --porcelain empty before and after review. PGP signature header present; cryptographic validity not independently checked. EN comparison: designated frozen checkout 6af98cb. No repository edits, index changes, generators, branch switches or checkouts.

Scope: Blind correctness and scoped-coverage review of all 30 new word cards. Each path below was read IN FULL in BOTH RU and EN, including front matter, every example/read­ing, all sections and footers:

| File | RU / EN |
|---|---|
| words/物差し.md | full / full |
| words/物凄い.md | full / full |
| words/牧畜.md | full / full |
| words/牧場.md | full / full |
| words/片道.md | full / full |
| words/片寄る.md | full / full |
| words/片仮名.md | full / full |
| words/父母.md | full / full |
| words/爪.md | full / full |
| words/焦がす.md | full / full |
| words/焦げる.md | full / full |
| words/あぶる.md | full / full |
| words/暖める.md | full / full |
| words/加熱.md | full / full |
| words/焚く.md | full / full |
| words/燃やす.md | full / full |
| words/暖まる.md | full / full |
| words/熱する.md | full / full |
| words/熟語.md | full / full |
| words/照らす.md | full / full |
| words/射す.md | full / full |
| words/照る.md | full / full |
| words/煙突.md | full / full |
| words/煙い.md | full / full |
| words/煎る.md | full / full |
| words/煉瓦.md | full / full |
| words/焦点.md | full / full |
| words/無限.md | full / full |
| words/怠る.md | full / full |
| words/休業.md | full / full |

Also reviewed the complete four one-line backlink diffs in words/往復.md, words/傾く.md, words/炊く.md and words/光る.md, and actual current titles of all linked/excluded comparison cards. Those existing cards were not each re-reviewed in full. Read the binding RU review/word-format rules and relevant EN JLPT policy. No author/reviewer reports, other FILES-directory files, prohibited RU tracking/batch/draft contents or scratch worktrees read. No subagents used. Actual deployed model identifier is not exposed to this reviewer and cannot be verified.

Verdicts: correctness NEEDS FIX (F1, 焚く); scoped coverage CLEAN across all 30 paired articles and four backlink diffs. CLEAN means no actionable coverage defect established, not exhaustive correctness.

Findings:

F1; MEDIUM; correctness; words/焚く.md:4 (repeated :12, :17); unresolved.
- Wrong claim: «растапливать (печь, ванну)» applies the Russian verb to a bathtub; :17 likewise coordinates «растапливать и нагревать ванну, печь или котёл».
- Correct fact / impact: 風呂を焚く concerns heating bathwater with a fire. Russian «растапливать» means starting a fire in a stove/furnace, or melting a substance, not the ordinary action of heating bathwater. The title teaches an incorrect Russian verb–object combination for a specifically explained sense; the correct clarification at :24–25 does not repair that label.
- Remedy: replace title and H1 gloss with «жечь топливо; разводить и поддерживать огонь». Replace :17 with «топливо или благовония, топить печь или котёл, нагревать воду для ванны.» This continues the preceding line's «жечь» and preserves the incense, stove/boiler and bath senses.
- Evidence actually inspected: JMdict 1596840, sense 2, “to heat (a bath); to light (a stove); to stoke (a boiler)” in https://www.edrdg.org/pub/Nihongo/JMdict_e.gz ; Digital Daijisen 焚く, sense 2, 火を燃やして湯をわかす, https://www.weblio.jp/content/焚く ; Kuznetsov РАСТОПИТЬ¹, «Развести огонь в чём-л. (в печи, плите и т.п.)», versus РАСТОПИТЬ², melting, https://gramota.ru/poisk?query=растопить&mode=slovari ; Kuznetsov ВАННА, sense 1, bathing vessel, https://gramota.ru/poisk?query=ванна&mode=slovari .
- Confidence: HIGH.

Verification supporting verdicts:
- All 30 preserve EN word/reading/level/type/kanji/tags. Original exclusions retained; additions examined as direct guards, not inferred transitive groups. Every referenced internal target exists. No extra RU link/source URL and no dropped EN link whose RU target exists. The 13 missing-target EN links are appropriately plain text in RU; 爪 correctly retains the no-kanji-card remark.
- All Japanese example sentences AND kana readings compared mechanically: identical contents, including punctuation, katakana and reading choices. EN ASCII reading delimiters are localized to full-width parentheses, not changes to Japanese sentences. Full manual paired reading found no omitted Japanese teaching rule, sense, example or citation. English-only monarch/earthquake/nail/transitive-English explanations need not survive literally.
- Nested-quotation examples are intact and accurately translated: 片仮名:18 «Слово «кофе», コーヒー, пишется катаканой.»; 熟語:18 «Слово 学校 «школа» — сложное слово из двух кандзи.»; 休業:19 «У входа было написано: «Сегодня закрыто».»
- Inspected all primary entries through Jisho's word API and all cited JMdict entry IDs, senses and form qualifications in canonical XML. In particular: historical 父母 readings; rare 烘る/熬る/烟突; kana-only レンガ; 温/暖 shared temperature sense; obsolete illness sense of 怠る. Kotobank URL number 2022842 was treated as a Kotobank identifier, not a missing JMdict entry.
- Inspected cited Daijisen/Kotobank definitions for the nontrivial spelling, light/comparison, roasting, origin and historical claims. 照らす comparison is Seisenban sense 4, not Daijisen sense 4. 焦点's black-paper explanation is explicitly in Daijisen. The footer regroupings retain their actual source identities.
- Directly read the official PDF title and printed p.5 item 007: 文化審議会国語分科会, 21 February 2014; the RU council attribution/year and qualified 暖/温 guidance are supported: https://www.bunka.go.jp/seisaku/bunkashingikai/kokugo/hokoku/pdf/ijidokun_140221.pdf .
- Component on/kun readings checked at https://kanjiapi.dev/v1/kanji/<character>; these were not used to invent etymologies. Classification sentences have EN counterparts. Every primary N2 spelling/reading/entry identity matched the policy-pinned CSV, including kana あぶる and both 煎る/炒る rows: https://raw.githubusercontent.com/stephenmk/yomitan-jlpt-vocab/b062d4e38c4bdd0950ae1d4ec55f04b176182e03/original_data/n2.csv .
- Russian dictionary checks were performed in this review, not assumed from the brief: Kuznetsov/Gramota entries лить (sense 4), литься (2), накалиться (2), раскалить (1), мерило (2), неимоверный, крениться, однобокий (2), подпалить (2), обуглить (1), пригореть (1–2), озарить (1), подсушить (1), подогреть (1–2), исконный, растопить and ванна. Reproducible entry URLs: https://gramota.ru/poisk?query=<lemma>&mode=slovari . Thus these are not left “unchecked in a Russian dictionary.” «Онные чтения» is established Russian pedagogical terminology, also observed directly at https://konnichiwa.ru/4516/ .
- Contextual Russian perfectives, masculine speakers and supplied pronouns do not assert universal Japanese gender/aspect rules. No defect established in «Спор накалился», «раскаляю сковороду», figurative «мерилом», «горят боевым духом», or the retained transitivity/spelling explanations. Short titles are not required to enumerate every secondary sense.
- Read-only validator: python -X utf8 -B tools/validate.py, primary RU checkout, completed exit 0: “0 error(s)”.

Optional (outside assigned facets; nonblocking comprehensibility):
- 射す:39 still explains the English legacy gloss strike; あぶる:41 refers to an unseen source-list gloss. Direct Japanese-specific guidance without those editorial references would be more self-contained; no additional factual defect is asserted.
- 照る:4 «лить свет» is marked bookish by Kuznetsov лить (4), while the examples already use everyday «светить». 照らす:4 «озарять» is elevated in Kuznetsov озарить; its ordinary synonym «освещать» is already present. Register simplification is optional here, not a second correctness finding.

Limits: No deployed-app, device, generator, archive/publication or corpus-frequency testing; no exhaustive whole-pool quiz certification (outside these facets). Dictionary meaning does not prove contemporary frequency. No consequential unresolved correctness claim beyond F1 is being promoted to CLEAN. Exact model ID and signature cryptographic validity remain unverifiable in this review.
