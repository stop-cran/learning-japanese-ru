# B242 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `8cada6dfbe469d4905e64c9ba8e8e2377f1d0b6f` (tree `06db481b65bf56830aa81d275089b6c4af319389`),
> the signed candidate pushed before review.
> Later reconciliation is in `242-words-batch-81-recheck-001.md`.

Snapshot: Candidate 8cada6dfbe469d4905e64c9ba8e8e2377f1d0b6f; parent f02299abd44b6fbc0c916ad5b6f9b6ed88273592. RU primary checkout C:\Users\romanko\repos\learning-japanese-ru. HEAD matched and git status --porcelain was empty initially and at the completion-stage recheck. No repository, branch, index or commit modified; only this report written.
Scope: Independent blind review: correctness and scoped coverage against frozen EN 6af98cb. Model identity not independently verifiable. Each following RU file AND its same-path EN original has now been read in full (including front matter, all sections, examples, readings and citations):

- words/押さえる.md — full RU + EN.
- words/敷く.md — full RU + EN.
- words/広げる.md — full RU + EN.
- words/膨らむ.md — full RU + EN.
- words/膨らます.md — full RU + EN.
- words/広々.md — full RU + EN.
- words/膨大.md — full RU + EN.
- words/おかけください.md — full RU + EN.
- words/腰掛ける.md — full RU + EN.
- words/腰掛け.md — full RU + EN.
- words/脱線.md — full RU + EN.
- words/学力.md — full RU + EN.
- words/学術.md — full RU + EN.
- words/実力.md — full RU + EN.
- words/生き生き.md — full RU + EN.
- words/活躍.md — full RU + EN.
- words/功績.md — full RU + EN.
- words/実績.md — full RU + EN.
- words/性能.md — full RU + EN.
- words/能率.md — full RU + EN.
- words/背負う.md — full RU + EN.
- words/育児.md — full RU + EN.
- words/肯定.md — full RU + EN.
- words/肘.md — full RU + EN.
- words/肌着.md — full RU + EN.
- words/職人.md — full RU + EN.
- words/耕す.md — full RU + EN.
- words/習字.md — full RU + EN.
- words/羨む.md — full RU + EN.
- words/羨ましい.md — full RU + EN.

Also inspected candidate navigation-only changes in kanji/児.md, kanji/生.md, words/広める.md, words/要領.md and words/風船.md. Forbidden batch records, scratch worktrees and other reviewers' material were not opened.
Verdicts:
- CORRECTNESS: NEEDS FIX (F1–F3). Per-article exceptions: the exact pinned “rare/search-only” labels for 布く/藉く in words/敷く.md:35 and 展げる in words/広げる.md:31–32 remain UNVERIFIED; see Limits. These exceptions are not asserted defects.
- SCOPED COVERAGE: CLEAN. All 30 pairs read completely; no missing EN teaching point, example, citation, original exclusion or existing-target link established. CLEAN is bounded to this translation scope, not exhaustive lexical or quiz certification.

Findings:

F1; P2; CORRECTNESS; words/耕す.md:43–44.
Claim: “Русское «возделывать» может употребляться и переносно, например о развитии способностей.” This transfers the English gloss “cultivate” and its talent-development polysemy to a Russian verb whose inspected standard dictionary senses are agricultural. It introduces an unsupported Russian-only lexical lesson; JMdict does not establish Russian usage.
Correct fact: the inspected Russian entries describe preparing/cultivating land and growing plants. “Культивировать”, not the chosen equivalent “возделывать”, has an explicitly recorded development/perfection sense. This is not a claim that creative literary metaphors with “возделывать” are impossible.
Remedy: replace lines 43–44 with “耕す относится к обработке сельскохозяйственной почвы. Для развития способностей или отношений выбирайте другое слово по контексту.” Retain the following distinction from the entire crop-production process.
Evidence actually inspected: Kuznetsov, ВОЗДЕЛАТЬ, senses 1–2 and imperfective возделывать, https://gramota.ru/poisk?query=возделать&mode=slovari ; КУЛЬТИВИРОВАТЬ, sense 3, https://gramota.ru/poisk?query=культивировать&mode=slovari ; Ozhegov/Shvedova, ВОЗДЕЛАТЬ, https://dic.academic.ru/dic.nsf/ogegova/26322 ; Japanese 耕す, sense 1, https://jisho.org/search/耕す .
Confidence: medium-high for the unsupported standard-usage adaptation; no exhaustive corpus claim.

F2; P2; CORRECTNESS; words/功績.md:44–45.
Claim: “功績 не имеет отношения к передаче денег.” The EN warning only excludes treating 功績 as a generic instruction to donate. RU instead categorically excludes any connection with giving money, misleading learners about recognition of meritorious donations.
Correct fact: 功績 names a valued achievement/contribution, not the act of transferring money itself; a donation can nevertheless be recognized for its merit.
Remedy: “Слово «вклад» может обозначать и денежное пожертвование, как [寄付](寄付.md)（きふ）. 功績 называет заслугу или ценимый результат, а не само действие передачи денег.”
Evidence actually inspected: 功績, JMdict 1275070, sense 1 (“achievement; meritorious deed; distinguished service; contribution”), https://jisho.org/search/功績 ; National Archives, Cabinet record dated 1920-01-23, 褒章条例ニ関スル内規ヲ定ム, https://www.digital.archives.go.jp/item/1686777 , document-content text “公益の為に為したる寄附にして其功績を認め得る” explicitly recognizes the merit of a public-interest donation. The historical example disproves the categorical exclusion; it is not evidence of current frequency.
Confidence: high.

F3; P3; CORRECTNESS (evidence-contract defect); words/職人.md:45–47,49–50.
Claim: the new Russian-only note explains the disapproving figurative sense of “ремесленник”, but cites only JMdict and Japanese Daijisen. Neither cited entry supports a claim about the Russian word's connotations. The note itself is correct; this is missing claim-specific support, not a mistranslation.
Remedy: retain the note and add “Русское значение: [Викисловарь — ремесленник](https://ru.wiktionary.org/wiki/ремесленник), значение 2 (перен., неодобр.).” A reputable Russian explanatory-dictionary entry covering that sense can replace this reference.
Evidence actually inspected: https://ru.wiktionary.org/wiki/ремесленник , sense 1, craft livelihood; sense 2, “перен., неодобр.”, noncreative/routine work. The existing Japanese citation, https://www.weblio.jp/content/職人 , supports craft and extended specialist uses of 職人, not Russian lexical coloration. EN has no counterpart to RU lines 45–47.
Confidence: high; low learning impact, explicit task evidence requirement.

Checks supporting the verdicts:
- All Japanese example sentences and kana payloads match the EN originals. Example layout and outer reading parentheses are localized; this is not a claim of byte-identical whole Markdown.
- IDs/word identity, reading, type, kanji, tags and levels are preserved. Original exclusions are preserved. Additional RU guards: 活躍 → 役割/役; 能率 → 効果; 育児 → 育てる; 肯定 → 主張; 職人 → 名人; 習字 → 清書. No unsupported deletion established.
- All 30 N2 identities/readings were independently matched to the pinned vocabulary CSV: https://raw.githubusercontent.com/stephenmk/yomitan-jlpt-vocab/b062d4e38c4bdd0950ae1d4ec55f04b176182e03/original_data/n2.csv . 押さえる teaches source 押える/おさえる, entry 1589080; 肯定 uses 1281180, not homophone 校庭. This is a community study label, not an official exhaustive JLPT list.
- Exact Jisho/JMdict entries were inspected for all 30 words (senses/POS, readings and restrictions). Verified literary 敷く, transitive godan 膨らます, separate archaic 広々/こうこう, spelling-restricted 膨大/suru, kana-usual おかけください and しょう-restricted 背負う/conceit. API Wikipedia/place pseudo-senses were excluded.
- Actual spelling notes verified at https://jisho.org/word/膨らむ , https://jisho.org/word/膨大 and https://jisho.org/word/肘 : 脹らむ, 厖大/尨大, 肱/臂 are rare kanji forms. Daijisen's 押さえる meanings and contrast with 抑える were independently read at https://kotobank.jp/word/押える-452098 .
- Weblio/Kotobank sections independently checked the higher-risk Japanese meanings; KANJIDIC-based kango component on-readings were checked, without treating them as historical proof. Actual Russian entries checked the high-risk glossary choices, including coercive силовой, knowledge/skill-level подготовка and non-mandatory extended-sitting усаживаться. No further actionable lexical defect established.
- Link comparison found no RU-only word-card links, no missing RU target and no dropped EN link with an existing RU target. Plain pointers correctly replace links to untranslated 敷地/活力/児童/手首/工員/憎む/恨む and kanji 腰/線/績/肯/肌/耕. The five navigation patches only wrap existing text in valid links.
- Read-only validation: python -X utf8 -B tools/validate.py in RU primary checkout, exit 0, 0 error(s). No generators executed.

Optional (nonblocking; not findings):
- words/背負う.md:21: “Он несёт ответственность за обеспечение своей семьи” makes the livelihood sense explicit. Daijisen's 背負う sense 2 includes 一家の生活を背負って立つ, https://www.weblio.jp/content/背負う ; 生活 sense 3 is livelihood, https://www.weblio.jp/content/生活 . No aspect-only defect established: “взвалил на себя” can express a resulting burden.
- Inherited process commentary and awkward titles are comprehensibility/quiz polish, not findings here.

Limits:
- Exact frozen raw JMdict spelling annotations were not available. Current Jisho proves the relevant ordinary senses, but its API omits some rare/search-only flags; its 広げる page says 展げる is occasionally used for unfolding. That does not establish the pinned search-only annotation. Raw EDRDG archive access failed certificate validation; JMdictDB returned an authentication gate. Neither was bypassed. The two specific annotation checks above therefore remain UNVERIFIED, not CLEAN and not fabricated defects.
- Direct requests sometimes failed (403/429) or HTML extraction was incomplete; recovered actual entries were used, never failures as evidence of absent senses. Not every comparison/guard ID or Russian collocation was separately dictionary-verified. No exhaustive comparison-corpus or quiz fallback audit.
- No historical-phonetic or native-device audit; no new etymological defect established.
