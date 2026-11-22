# B245 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `004903db88a34b30524ca68ffc5b8dfbc085bbfa` (tree `86483e2d7614ce9f762d411eb04dc4c869602984`),
> the signed candidate pushed before review.
> Later reconciliation is in `245-words-batch-84-recheck-001.md`.

Snapshot: RU primary checkout C:\Users\romanko\repos\learning-japanese-ru; branch full-ru-245-words-84; candidate/HEAD 004903db88a34b30524ca68ffc5b8dfbc085bbfa; parent e73ae1b17912f1796cb236e566f4224e242f361e. Initial and final git status --porcelain empty. Frozen EN source: C:\Users\romanko\repos\learning-japanese-en-frozen, supplied revision 6af98cb717755690a9ca793e5454a96ebd7a8f9f.

Scope: Independent blind, read-only correctness and scoped-coverage review. Model identity not verifiable. All lines of each following RU card AND its frozen EN original were read, including metadata, examples/readings, explanations, comparisons and citations:
- words/標識.md — full RU/EN pair.
- words/符号.md — full RU/EN pair.
- words/競馬.md — full RU/EN pair.
- words/童話.md — full RU/EN pair.
- words/立ち止まる.md — full RU/EN pair.
- words/窓口.md — full RU/EN pair.
- words/突き当たり.md — full RU/EN pair.
- words/架空.md — full RU/EN pair.
- words/空想.md — full RU/EN pair.
- words/空中.md — full RU/EN pair.
- words/空っぽ.md — full RU/EN pair.
- words/税関.md — full RU/EN pair.
- words/移転.md — full RU/EN pair.
- words/秤.md — full RU/EN pair.
- words/私鉄.md — full RU/EN pair.
- words/私立.md — full RU/EN pair.
- words/おやすみ.md — full RU/EN pair.
- words/祭日.md — full RU/EN pair.
- words/お参り.md — full RU/EN pair.
- words/敬う.md — full RU/EN pair.
- words/祭る.md — full RU/EN pair.
- words/神話.md — full RU/EN pair.
- words/神様.md — full RU/EN pair.
- words/祝日.md — full RU/EN pair.
- words/先祖.md — full RU/EN pair.
- words/祖先.md — full RU/EN pair.
- words/社説.md — full RU/EN pair.
- words/社会科学.md — full RU/EN pair.
- words/磁石.md — full RU/EN pair.
- words/確率.md — full RU/EN pair.

Also inspected the existing comparison-card titles and the changed lines in words/休日.md, words/突き当たる.md and words/編集.md, plus the manifest delta. No author/reviewer reports, title-screen results, batch/draft/tracking content or numbered scratch checkouts were consulted.

Verification:
- Inspected all 30 primary cited JMdict entries in the official XML; relevant component readings in official KANJIDIC2. Checked consequential usage against actual Daijisen/Seisenban entries, not search snippets. Sources: https://www.edrdg.org/pub/Nihongo/JMdict_e.gz and https://www.edrdg.org/kanjidic/kanjidic2.xml.gz.
- A read-only comparison confirms identical Japanese sentence and kana-reading contents for all 61 examples. EN multiline layout and ASCII reading delimiters versus RU single-line/full-width formatting were distinguished from changes to Japanese content.
- word/reading/jlpt/type/kanji/tags match EN throughout. Original quiz exclusions are retained; 社説 adds 論文 and 社会科学 adds 自然科学. Existing-target internal links are retained except the 習慣 link attached solely to the removed English "customs" contrast. The only additional internal link within the 30 pairs is 祭日 → 祝日; its comparison is supported by Daijisen 祭日 sense 2. Missing-RU targets remain plain mentions as required.
- The dropped counter/customs/demise/drawing-compass passages depend on English polysemy. RU still teaches the service/contact distinction, customs authority, legal transfer versus physical relocation, and magnet versus compass. No necessary Japanese rule was established as missing from those omissions; restoring the disconnected 習慣 link is not required.
- Russian "знак" senses were checked at https://gramota.ru/meta/znak (Kuznetsov senses 1, 5–7), and "опознавательный" at https://gramota.ru/meta/opoznavatelnyy. Mathematical positive/negative sign agrees with Daijisen 符号 sense 3: https://www.weblio.jp/content/符号.
- Required Russian lexical checks used actual entries: https://ru.wiktionary.org/wiki/окошко (sense 2); https://gramota.ru/meta/podvesnoy (senses 1–2); https://gramota.ru/meta/greza (sense 1); https://gramota.ru/meta/polyy (sense 1); https://ru.wiktionary.org/wiki/весы (plural-only morphology and instrument sense); https://gramota.ru/meta/rodonachalnik (sense 1); https://ru.wiktionary.org/wiki/приостанавливаться (sense 1); https://gramota.ru/meta/peredovitsa and https://gramota.ru/meta/peredovaya (editorial sense). None establishes another incorrect gloss.
- Бог/бог adaptation agrees with Lopatin §180 and its note: https://gramota.ru/biblioteka/spravochniki/pravila-russkoy-orfografii-i-punktuatsii/nazvaniya-svyazannye-s-religiey. "Исконный" was checked at https://gramota.ru/meta/iskonnyy; established Russian usage of "онные чтения" at https://lingust.ru/faq/japanese/1989-6 was kept separate from the authoritative KANJIDIC2 classification checks.
- The dictionary restrictions/variants support がくう versus かくう, obsolete たちとまる, わたくしりつ/いちりつ, じせき, 祀る and 量る. 秤 is not the particle ばかり; Daijisen also records voiced -ばかり in compound scale names, which does not contradict that comparison.
- Russian supplied pronouns/possessors, masculine agreement, aspect choices and impersonal translations of Japanese passives were assessed contextually. No false universal correspondence or additional factual assertion was established. Rebuilt remarks on number, "картина", "в воздухе", "весы" and "уважать" retain their Japanese teaching points.

Verdicts: correctness NEEDS FIX; scoped coverage NEEDS FIX. Both exceptions concern words/おやすみ.md, F01 below. For the remaining 29 full pairs and the inspected reused-card changes, no actionable defect was established in either assigned facet.

Findings:

F01; LOW; correctness + scoped coverage; words/おやすみ.md:4 (repeated :12).
Claim: the respectful noun sense is titled "отход ко сну (уважительно)".
Correct fact / impact: JMdict 1612680 sense 2 is "sleep; rest", marked sonkeigo. It is not restricted to the transition into bed/sleep. EN :4 explicitly includes "rest", and RU :17 itself retains sleep OR rest. The title therefore narrows a taught sense to bedtime and omits the source title's rest meaning; the answer label does not represent the broader respectful noun use. Low severity because the body and example remain informative, rather than teaching an incorrect conjugation.
Remedy: replace the title at :4 and matching H1 gloss at :12 with "выходной день (вежливо); сон или отдых (уважительно); спокойной ночи".
Evidence: actual official JMdict XML, entry 1612680, sense 2, https://www.edrdg.org/pub/Nihongo/JMdict_e.gz; frozen EN words/おやすみ.md:4,16; RU :17. Independently, Daijisen 御休み sense 2 refers to the respected person's sleeping, not only retiring: https://www.weblio.jp/content/お休み.
Confidence: HIGH.

Optional:
- Outside the assigned facets, 祭る:20–21 could make the dedicated/enshrined-deity meaning clearer, especially by rendering the first example "Это святилище посвящено богу моря." Existing "почитают/почитаем" is defensible religious wording, not an established factual defect; the definition already preserves enshrinement. Evidence: JMdict 1295250 senses 1–2; Daijisen 祭る sense 2, https://www.weblio.jp/content/祭る; Russian "почитать", https://gramota.ru/meta/pochitat.

Limits: This is a review of the specified 30 pairs, not an exhaustive baseline, application/quiz-pool, native-speaker or learning-effectiveness audit. JLPT metadata was checked for frozen-EN retention, not independently reassigned. Some Jisho/kanji API/Gramota requests were throttled or failed; direct official dictionary XML and actual alternative entries supplied the consequential evidence. No validator, generator, app or media test was run. No repository files, index or HEAD were changed; only this report was written. Findings count: critical 0; high 0; medium 0; low 1. Optional notes are not findings.
