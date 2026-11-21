# B237 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `be448e7c8309d0b9fe6296bd3bc75b2508312556` (tree `3fdba75c00a9a083e212398d0b36c726a2e6f7e7`),
> the signed candidate pushed before review.
> Later reconciliation is in `237-words-batch-76-recheck-001.md`.

Snapshot: RU candidate be448e7c8309d0b9fe6296bd3bc75b2508312556, parent f9bab892714c2957af508bb37f5e1d9cecd37dbe. HEAD matches; initial working tree clean. EN translation baseline: frozen 6af98cb. No repository files edited or generators run.

Scope: Correctness and scoped coverage only. Model identity not independently verifiable. Read the entire brief, including its long risk-point line in bounded portions, and the binding review/word-format provisions.

The following attestation is file-by-file: EVERY listed RU file and its same-path frozen EN original were read IN FULL, including front matter, all examples, formation explanations, comparisons, nuance sections and citations. The JMdict column records the primary numbered entry independently inspected in the actual dictionary, not merely the article's assertion.

| File | Paired reading | Primary JMdict entry |
| --- | --- | --- |
| words/おじゃまします.md | RU + EN full | 1002050 |
| words/ごめんください.md | RU + EN full | 1270690 |
| words/お待ちどおさま.md | RU + EN full | 1002360 |
| words/お待たせしました.md | RU + EN full | 2149640 |
| words/ごめん.md | RU + EN full | 1270670 |
| words/すまない.md | RU + EN full | 1610020 |
| words/詫びる.md | RU + EN full | 1606790 |
| words/評論.md | RU + EN full | 1490080 |
| words/診断.md | RU + EN full | 1365480 |
| words/診る.md | RU + EN full | 1365450 |
| words/訳す.md | RU + EN full | 1538350 |
| words/言葉遣い.md | RU + EN full | 1264560 |
| words/言付ける.md | RU + EN full | 1593330 |
| words/言い付ける.md | RU + EN full | 1264230 |
| words/解説.md | RU + EN full | 1199080 |
| words/応ずる.md | RU + EN full | 1609380 |
| words/回答.md | RU + EN full | 1199680 |
| words/解答.md | RU + EN full | 1199160 |
| words/溶ける.md | RU + EN full | 1546070 |
| words/解散.md | RU + EN full | 1199000 |
| words/占う.md | RU + EN full | 1389430 |
| words/観測.md | RU + EN full | 1214980 |
| words/アイデア.md | RU + EN full | 1014210 |
| words/アイディア.md | RU + EN full | 1014210 |
| words/観念.md | RU + EN full | 1215010 |
| words/親類.md | RU + EN full | 1365420 |
| words/親指.md | RU + EN full | 1365190 |
| words/覗く.md | RU + EN full | 1470840 |
| words/見送る.md | RU + EN full | 1259830 |
| words/慰める.md | RU + EN full | 1156890 |

Also inspected the changed runtime hunks in kanji/付.md, kanji/占.md, kanji/言.md, words/応じる.md, words/解ける.md, words/説明.md and words/集合.md: these introduce links without changing their teaching text. Checked all linked word titles/readings and read words/恐縮.md in full to verify the descriptions in ごめん and すまない. This is not a whole-card re-review of every pre-existing comparison target or kanji.

Verdicts:
- Correctness: CLEAN for all 30 paired cards and the ancillary link-only changes.
- Scoped coverage: CLEAN for all 30 paired cards and the ancillary link-only changes.
- Russian comprehensibility: UNVERIFIED — not an assigned facet; lexical meaning/register checks do not constitute a comprehensive readability review.

Findings: None. No actionable defect established.

Evidence and decisions:

1. Inspected the actual numbered entries, forms, sense lists, parts of speech and relevant usage flags in [JMdict_e](https://www.edrdg.org/pub/Nihongo/JMdict_e.gz), downloaded/decompressed/parsed only in memory. All primary entries in the table match the cards' selected readings and taught senses. Also inspected 邪魔 1323500:1–2 and 溶かす 1546040:1–2. In particular:
   - 1002360 marks お待ちどうさま with irregular-kana flag `ik`; the warning is justified.
   - 1264230:1–2 supports instruction and telling-on senses; 1593330:1–2 supports intermediary delivery and the separately acknowledged archaic pretext.
   - 1546070 includes 解ける among melting/dissolving spellings and labels money/time use colloquial.
   - 1470840 distinguishes transitive looking senses from intransitive partial appearance.
   - 1609380 identifies the ずる alternative; the shared 応じ- forms are not an unrelated-example defect.
   - The same 1014210 entry supplies both アイデア and アイディア.

2. Inspected the named monolingual sections, not unrelated aggregator entries:
   - [Digital Daijisen, 御免](https://www.weblio.jp/content/御免), definitions 1–5, supports authorization, discharge, rejection, apology and visiting/leave-taking; the short visiting example is actually present.
   - [Digital Daijisen, ごめんください](https://www.weblio.jp/content/ごめんください), definitions 1–2, supports arrival/leave-taking and apology. A title focused on the explicitly selected arrival use does not erase the additional uses retained in the body.
   - [御待遠様, Daijisen and Seisenban](https://kotobank.jp/word/御待遠様-454401) supports apologetic acknowledgment after keeping someone waiting, without establishing a universal politeness ranking.
   - [詫びる](https://www.weblio.jp/content/詫びる) and [謝る, usage comparison](https://www.weblio.jp/content/謝る) support the formal/written tendency, apology formula, and shared origin with 侘びる. The RU text does not license unrestricted spelling substitution.
   - [すまない](https://www.weblio.jp/content/すまない) supports apology, gratitude, requests and its connection to negated 済む.
   - [診る, broader みる entry](https://www.weblio.jp/content/診る), specifically definition 7, supports medical examination/pulse checking. [診断](https://www.weblio.jp/content/診断):1–2 supports diagnostic judgment and broader condition assessment.
   - [訳す](https://www.weblio.jp/content/訳す) supports the modern godan form. [言付ける](https://www.weblio.jp/content/言付ける) contains distinct いいつける and ことづける headings; the RU comparison preserves their distinction.
   - [応ずる, Seisenban](https://kotobank.jp/word/応ずる-449094) and [応じる, Daijisen](https://kotobank.jp/word/応じる-449078) support the conjugational relationship.
   - [評論](https://www.weblio.jp/content/評論), [言葉遣い](https://www.weblio.jp/content/言葉遣い), [回答](https://kotobank.jp/word/回答-458121), [解答](https://kotobank.jp/word/解答-458132), [観念, Seisenban](https://kotobank.jp/word/観念-49433), [親類](https://www.weblio.jp/content/親類) and [見送る](https://www.weblio.jp/content/見送る) support the consequential distinctions and additional senses.

3. Inspected actual Russian dictionary definitions on Gramota:
   - [уволить](https://gramota.ru/poisk?query=уволить&mode=slovari): Kuznetsov definition 3 and the universal dictionary's speech-formula definition explicitly support «нет уж, увольте» as rejecting something unwanted. A bookish shade is a style consideration, not evidence that the refusal sense is false.
   - [задумка](https://gramota.ru/poisk?query=задумка&mode=slovari): colloquial intention/design/plan supports the contextual idea gloss.
   - [доносить](https://gramota.ru/poisk?query=доносить&mode=slovari) and [ябедничать](https://gramota.ru/poisk?query=ябедничать&mode=slovari): the relevant reporting-on-someone senses, including Kuznetsov's teacher example, support the qualified misbehavior/telling-on use; the card does not claim every report is a denunciation.
   - [весть](https://gramota.ru/poisk?query=весть&mode=slovari), [гостинец](https://gramota.ru/poisk?query=гостинец&mode=slovari), [виноватый](https://gramota.ru/poisk?query=виноватый&mode=slovari), [подглядеть](https://gramota.ru/poisk?query=подглядеть&mode=slovari), [смирение](https://gramota.ru/poisk?query=смирение&mode=slovari), [критический](https://gramota.ru/poisk?query=критический&mode=slovari) and [прогноз](https://gramota.ru/poisk?query=прогноз&mode=slovari) support the senses used. In particular «виноват» is explicitly an apology interjection; «критический» can involve assessment of strengths/weaknesses or disapproval.

4. Example translations preserve the taught roles, polarity, event and tense. No defect established from Russian masculine past forms for unspecified speakers, context-supplied subjects, ordinary Russian present for these ている examples, or active Russian rendering of the explicitly explained Japanese passive. Contextual «Спасибо»/«Здравствуйте» in the visiting exchanges do not establish a new lexical gratitude/greeting sense. Nor does «Что ж» distort では in the transition after waiting.

5. Coverage: retained every EN-selected sense, example, citation and Japanese teaching restriction. Omitted English-specific “interpret/examine/snitch” comparisons do not remove the language-to-language restriction, medical limitation or telling-on disapproval: those remain elsewhere in RU. Japanese sentences and kana readings were also checked with a span-parity scan; its two missing word-token occurrences belong to the omitted English-dependent prose, not deleted examples/readings. Changes to surrounding heading/separator/parenthesis typography follow the RU presentation convention, not altered Japanese sentence content.

6. Metadata/link checks: word, reading, jlpt, type, kanji and tags match EN throughout. Every original exclusion is retained; six cards add exclusions, with no removed original pair. No broken RU Markdown target and no dropped EN link whose RU target exists were found. Missing-kanji/word targets are left as plain text, as required. All 30 N2 labels independently match their rows in the frozen EN docs/n2-vocabulary-sources.tsv under the published vocabulary-level policy; they were not inferred from kanji difficulty.

Optional: None in the assigned facets.

Limits: CLEAN means no established actionable defect, not an exhaustive proof. Russian comprehensibility, whole-corpus quiz candidate uniqueness, app/manifest behavior and publication acceptance are outside this review. No validator/generator, author artifacts, RU batch records, tracking files, other reviewer reports or forbidden scratch worktrees were read/run. Initial Jisho throttling and the ftp-host certificate failure were superseded by successful inspection of the canonical-host JMdict XML; neither is treated as evidence against a card.
