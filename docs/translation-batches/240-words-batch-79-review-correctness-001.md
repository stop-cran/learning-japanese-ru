# B240 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `d0d977cad025983c702361e0408d9c9be4b8b085` (tree `401f953909d959a255de1b8abeeb08406c7d4054`),
> the signed candidate pushed before review.
> Later reconciliation is in `240-words-batch-79-recheck-001.md`.

Snapshot: d0d977cad025983c702361e0408d9c9be4b8b085 in C:\Users\romanko\repos\learning-japanese-ru. HEAD matched at start and finish; git status --porcelain was empty; working-tree and index diffs both exit 0. No uncommitted changes included. Reviewed against frozen EN checkout 6af98cb as specified.

Scope: Correctness (Japanese facts, Russian semantic accuracy, examples, cited claims) and scoped coverage. Actual model identity is not exposed/verifiable; no model name claimed.

Each following file was read IN FULL in RU and against its IN FULL frozen EN original, including front matter, every section, example/reading, comparison and footer:
- words/蒸発.md — full RU + EN
- words/気体.md — full RU + EN
- words/蒸す.md — full RU + EN
- words/蒸気.md — full RU + EN
- words/湿度.md — full RU + EN
- words/湿気.md — full RU + EN
- words/蒸し暑い.md — full RU + EN
- words/散らかる.md — full RU + EN
- words/散らかす.md — full RU + EN
- words/散る.md — full RU + EN
- words/散らす.md — full RU + EN
- words/撒く.md — full RU + EN
- words/蒔く.md — full RU + EN
- words/葬式.md — full RU + EN
- words/著す.md — full RU + EN
- words/落第.md — full RU + EN
- words/落とし物.md — full RU + EN
- words/下駄.md — full RU + EN
- words/草履.md — full RU + EN
- words/茂る.md — full RU + EN
- words/英文.md — full RU + EN
- words/英和.md — full RU + EN
- words/若々しい.md — full RU + EN
- words/教養.md — full RU + EN
- words/芸能.md — full RU + EN
- words/花火.md — full RU + EN
- words/花嫁.md — full RU + EN
- words/芯.md — full RU + EN
- words/艶.md — full RU + EN
- words/早速.md — full RU + EN

Also inspected the binding RU instructions/format reference, actual linked/excluded RU titles and relevant comparison cards (including 儀式, 式, べたべた, はらはら, 跳ねる, さわやか). Did not inspect author/reviewer reports, tracking/disposition records, forbidden session files or scratch worktrees. No delegation.

Verdicts:
- correctness: NEEDS FIX — C1, C2, C4. Japanese sentences and kana reading strings match EN; no reading/conjugation defect established. The two source-attribution findings are inherited from EN, not Japanese-text translation mutations.
- scoped coverage: NEEDS FIX — C3. No missing sample reads. No broken runtime links or other dropped links to existing RU cards established.
- Russian comprehensibility: UNVERIFIED — outside the two assigned facets; semantic Russian accuracy was reviewed under correctness, not native-reader comprehensibility.

Findings:

C1; moderate; correctness; words/落第.md:20
Claim: «Я провалил экзамен и заново выучил материал.» The second clause adds successful acquisition/mastery: «выучить» means to memorize/assimilate. Japanese もう一度勉強し直しました reports studying again, without establishing mastery or subsequent success. This changes the example's outcome.
Remedy: replace the Russian translation with «Я провалил экзамен и снова занимался, повторяя материал.»
Evidence: https://www.weblio.jp/content/勉強 — Digital Daijisen, sense 1, 学問や技芸などを学ぶこと; https://www.weblio.jp/content/し直す — Digital Daijisen, doing the same thing again; https://gramota.ru/poisk?query=выучить&mode=slovari — Kuznetsov, sense 1, «Уча, запомнить, усвоить». Frozen EN words/落第.md:21 explicitly says “studied the material again”.
Confidence: high.

C2; low; correctness; words/茂る.md:28
Claim: «滋る помечено как устаревшее». The currently cited JMdict entry marks this spelling as rare, not obsolete. Rarity and obsolescence are different annotations; the card teaches an unsupported stronger restriction.
Remedy: «滋る помечено как редкое написание; в этих примерах используйте 茂る.»
Evidence: https://www.edrdg.org/pub/Nihongo/JMdict_e.gz — actual entry 1533740, k_ele/keb 滋る, ke_inf “rarely used kanji form”, not an obsolescence annotation.
Confidence: high for the current source discrepancy. EN words/茂る.md:25 contains the same stronger claim; no historical capture was inspected.

C3; low; scoped coverage; words/蒸す.md:42
Omission: frozen EN words/蒸す.md:48 links べたべた, whose RU card exists. Removing the English-only “sticky/close” discussion also removes this existing-target comparison/link. The English framing can be omitted, but the explicit link-retention contract is not satisfied.
Remedy: insert a brief Russian comparison after this paragraph: «[べたべた](べたべた.md) описывает липкость поверхности или тесное льнущее поведение, а не само по себе жаркую влажную погоду.» No need to restore English labels or American Heritage citations.
Evidence: frozen EN words/蒸す.md:46–50; existing RU words/べたべた.md:16–20 and its cited JMdict entry 1011440. Full link-set comparison across all 30 cards found this sole dropped link to an existing RU target; https://jisho.org/search/べたべた supplies the corresponding lexical senses.
Confidence: high.

C4; low; correctness; words/艶.md:45
Claim: «Среди английских переводов в словаре есть “glaze” (глазурь)». The only dictionary cited by this word card is JMdict, but its actual entry 1177680 has gloss/luster/shine/sheen/polish, not “glaze”. “Glaze” is a KANJIDIC2 character gloss for 艶. The sound distinction between surface quality and coating is retained, but the asserted source fact conflates character and word dictionaries.
Remedy: replace this sentence with «Блеск поверхности не означает ни материал глазури, ни само покрытие керамики глазурью.» Keep the following distinction sentence.
Evidence: https://www.edrdg.org/pub/Nihongo/JMdict_e.gz — entry 1177680, sense 1; https://jisho.org/api/v1/search/words?keyword=艶 — つや entry, sense 1; https://www.edrdg.org/kanjidic/kanjidic2.xml.gz — character 艶 includes “glaze”.
Confidence: high for the current dictionaries. Frozen EN words/艶.md:45 contains the same source-gloss framing; no historical capture was inspected.

Optional: Nonblocking, outside assigned comprehensibility facets: explain годан/итидан/окуригана/дзюкудзикун at first use; consider «посыпаю салат рубленым зелёным луком» instead of «раскидываю … поверх салата» (散らす:21), and «салютные заряды» rather than «салютные залпы» (花火:25). These are not counted as established correctness findings.

Limits:
- Actual JMdict XML entries (all 29 explicitly cited main word IDs) and Jisho lexical entries for all 30 sample words were inspected. Current KANJIDIC2 (header 2026-11-22) verified the component-reading labels; kanjiapi succeeded through web_fetch after direct Python requests returned 403. These are current dictionaries, not reconstructed historical source captures. Exact October KANJIDIC2 snapshot provenance was not authenticated; no historical etymology is inferred from readings.
- No independently established defect from ordinary illustrative pronoun/gender choices, omitted overt «один» in «купил … словарь», result-state «разрослась», or timely «быстрый ответ». Dictionary entries support the relevant senses; grammatical localization need not mirror Japanese syntax mechanically.
- English-dependent-only passages/citations in 気体, 蒸す, 蒸し暑い, 下駄 and 茂る need not be restored merely for literal English parity. C3 concerns the separately required existing-target link.
- Russian dictionaries were actually consulted for the flagged semantic distinction and several title terms (моложавый, новобрачный, глянец, фитиль, сердцевина, раскидывать, пар, дзори, прогревать, погоня). Some Gramota queries were rate-limited; available Wiktionary entries were used where appropriate. This is not dictionary authentication of every Russian collocation or a native-speaker readability claim.
- The official 著す spelling PDF was decoded and its entry 015 on printed p. 6 inspected. Source wording matches the card. Unchanged sample sentences/readings were checked manually and by string comparison; ASCII/full-width surrounding delimiters were treated as formatting localization.
- No validator, generator, staging, commit, push, checkout, branch switch or repository edit was performed. The only authored file is this report.
