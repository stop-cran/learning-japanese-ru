# B214 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `a371c734a15f44e674e87a3a9ea0c9f147961d90` (tree `6712ca2c3fe82adc1a20a1e86be3a7a58861d70a`),
> the signed candidate pushed before review.
> Later reconciliation is in `214-words-batch-53-recheck-001.md`.

Snapshot: RU a371c734a15f44e674e87a3a9ea0c9f147961d90, branch full-ru-214-words-53; HEAD verified twice and working tree clean at both checks. No uncommitted runtime changes included. Comparison baseline 0138d32829d6334f2cf142b8c415123e10c910c6; EN originals read from the designated frozen 6af98cb checkout.

Scope: Independent blind, read-only CORRECTNESS and SCOPED COVERAGE review. Actual model identifier is not independently verifiable. Full paired reads, including front matter, every example/reading/translation, all four sections and citations, completed for EACH of these files in RU and EN:

- words/地平線.md — full RU + EN
- words/地区.md — full RU + EN
- words/地下.md — full RU + EN
- words/土産.md — full RU + EN
- words/土曜.md — full RU + EN
- words/国語.md — full RU + EN
- words/国民.md — full RU + EN
- words/国家.md — full RU + EN
- words/国境.md — full RU + EN
- words/国会.md — full RU + EN
- words/図.md — full RU + EN
- words/囲む.md — full RU + EN
- words/回す.md — full RU + EN
- words/器用.md — full RU + EN
- words/善.md — full RU + EN
- words/商売.md — full RU + EN
- words/商品.md — full RU + EN
- words/商人.md — full RU + EN
- words/唯一.md — full RU + EN
- words/哲学.md — full RU + EN
- words/品.md — full RU + EN
- words/呼吸.md — full RU + EN
- words/味方.md — full RU + EN
- words/周囲.md — full RU + EN
- words/吸収.md — full RU + EN
- words/加える.md — full RU + EN
- words/含む.md — full RU + EN
- words/否定.md — full RU + EN
- words/向かい.md — full RU + EN
- words/吐く.md — full RU + EN

Also read the three binding RU instruction/format files in full; inspected changed runtime hunks in the five kanji and ten existing word cards. Full baseline comparison reads: 地域, 地方, お土産, 土曜日, 祝い, 科目, 道徳, 貿易, 店員, 熱中, 夢中, 言う. Other suggested existing comparison cards: actual current titles inspected, not represented as full reads.

Verdicts:
- Correctness: NEEDS FIX for 地区 (C1); CLEAN for the other 29 cards within this reviewed scope.
- Scoped coverage: CLEAN for all 30 cards. The basic district sense is present in the body; C1 concerns the accuracy of the separately displayed title, not a missing body explanation.

Findings:

C1; Minor; correctness; words/地区.md:4,12 (compare :16–19,33).
Claim/impact: “округ; выделенная зона” makes both title alternatives sound like specially constituted territorial units, while 地区 also denotes an ordinary local district/area without that status. The article itself correctly translates its neighbourhood examples with “район” and warns against assuming legal status. A learner seeing only the heading/meaning answer gets a narrower equivalence than those examples teach.
Remedy: replace the title with `title: район; выделенная зона` and the H1 gloss with `# 地区（ちく）— район; выделенная зона`. Retain the existing body qualification and direct 地域/地方 exclusions; check the revised displayed title against the live pool rather than preserving an inaccurate synonym to distinguish answers.
Evidence: Daijisen, 地区, sense 1 “ある限られた範囲内の土地。地域。” versus sense 2, an administratively designated area for a purpose, inspected at https://www.weblio.jp/content/地区 . JMdict/Jisho 地区, lexical sense 1, includes district/area/zone/quarter/section/region: https://jisho.org/api/v1/search/words?keyword=地区 . Kuznetsov, округ, defines an administrative, political, military or economic subdivision of state territory, https://gramota.ru/meta/okrug ; Kuznetsov, район, sense 1 covers places distinguished by geographic/economic/social features, including residential districts, https://gramota.ru/meta/rayon . Thus округ is possible in appropriate contexts, not a sufficient replacement for the ordinary district gloss here.
Confidence: high on the lexical scope difference; medium-high on the learning impact, bounded to this title.

Verification notes (not additional findings):
- All 30 exact Japanese headwords/readings and their lexical senses were inspected through the live JMdict-backed Jisho API (`https://jisho.org/api/v1/search/words?keyword=<word>`). Distinct readings/entries were kept separate; Wikipedia/name objects were not used as lexical evidence. Japanese-run comparison supplemented, not replaced, full editorial paired reads. Reading-join scripts match EN. The one decreased 商人 occurrence is replaced by a Russian pronoun, not a lost rule.
- Front matter retains EN word, reading, jlpt, type, kanji, tags and every original exclusion. Additional guards are explicit additions, not removed source constraints. Existing-target EN links are retained; omitted links point to unavailable RU targets, in accordance with the convention. All source examples, sense explanations and citations are represented. The removed English source-gloss warning in 吸収 does not remove its Japanese intake rule.
- 地平線's land qualifier is preserved. Kuznetsov горизонт, sense 1, covers both land and water: https://gramota.ru/meta/gorizont . 国境's broader Russian граница comparison is supported by sense 1, which explicitly includes countries, regions and plots: https://gramota.ru/meta/granitsa .
- 土産: Kuznetsov гостинец explicitly marks the gift sense conversational and includes gifts brought/sent, especially sweets, https://gramota.ru/meta/gostinets . Сувенир includes both a gift and an object retained as a memory of visiting a place, https://gramota.ru/meta/suvenir . The card preserves both travel and visiting-gift situations; it does not claim that all souvenirs are self-kept or all 土産 edible.
- 国語: Daijisen senses 1–3 explicitly cover national common/official language, Japanese and the school subject, https://kotobank.jp/word/国語-63744 . “Государственный (национальный)” is therefore not rejected merely because the EN gloss says national. No claim about a particular country's statutory language designation is added. 国家 and 国会 retain the political-entity and foreign-national-legislature explanations; their titles do not restrict the latter to Japan alone.
- Russian lexical adaptations checked against actual explanatory entries, not search summaries: коммерция https://gramota.ru/meta/kommertsiya ; купец https://gramota.ru/meta/kupets ; иллюстрация https://gramota.ru/meta/illyustratsiya ; обносить sense 2 https://gramota.ru/meta/obnosit ; ловкий senses 1–2 https://gramota.ru/meta/lovkiy ; добро/хороший https://gramota.ru/meta/dobro and https://gramota.ru/meta/khoroshiy ; единственный/уникальный https://gramota.ru/meta/edinstvennyy and https://gramota.ru/meta/unikalnyy . Kuznetsov купец sense 1 is not marked historical, while sense 2 concerns the pre-1917 estate; the card does not equate 商人 with membership of that estate.
- 呼吸's cycle gloss: https://gramota.ru/meta/dykhanie . 味方's supporter reading of “друг”: Babenko senses 2/4, https://gramota.ru/meta/drug . 周囲's area/length contrast and social surroundings: https://gramota.ru/poisk?query=периметр&mode=slovari and https://gramota.ru/meta/okruzhayushchiy . 吸収's literal/figurative intake: впитать senses 1–2, https://gramota.ru/meta/vpitat . 加える's adapted arithmetic/summary warning: суммировать senses 1–2, https://gramota.ru/meta/summirovat . 含む's holding interpretation: держать sense 1, https://gramota.ru/meta/derzhat . 否定's “опровержение” is licensed as denial in a public text, not necessarily a successful logical proof: Babenko https://gramota.ru/meta/oproverzhenie . 向かい's Russian contrast: напротив senses 1–4, https://gramota.ru/meta/naprotiv .
- 回す's localized rotating/rotating-itself contrast is specifically bounded to the wheel example and supported by https://gramota.ru/meta/vrashchat and https://gramota.ru/meta/vrashchatsya ; it is not presented as a universal Russian–Japanese transitivity rule. 吐く's emission and abusive-speech glosses have dictionary support: https://gramota.ru/meta/izvergat , https://gramota.ru/meta/izvergnut , https://gramota.ru/meta/izrygat . The separate はく homophones are not merged into 吐く.
- Russian example tense, polarity, transitivity, role and event stage were checked individually. Gendered Russian renderings are contextual choices, not taught as gender encoded by 私/友人/さん. No additional Japanese sentence requiring a new reading line was introduced.
- Read-only validation: `python -X utf8 -B tools\validate.py` in the RU primary checkout returned `0 error(s)`, exit 0. No generator was run.

Optional: Outside the assigned facets, 吐く's title would be easier to understand with an explicit ordinary vomiting gloss such as “рвать (о рвоте)” rather than “извергать рвоту”. This is a comprehensibility suggestion, not a second established correctness defect or a claim that the exact current collocation was corpus-verified. A brief conversational-register note for Russian “гостинец” would also be reasonable but is nonblocking.

Limits: No author/reviewer reports, intake/batch records, translation tracking/drafts or scratch worktree were read. This is not a full consistency/quiz-safety audit, frequency study, native-speaker certification or app/device test. Existing comparison cards not listed as full baseline reads were inspected only as stated. Jisho is a live dictionary view, not a revalidation of the entire frozen JMdict release or every numeric entry ID; retained EN provenance is not recertified. Initial Gramota search requests returned 429; actual direct entries were subsequently read. One wrong numeric Kotobank URL redirected to an unrelated entry and was discarded before the correct 国語 entry was located and inspected. No consequential unresolved linguistic claim remains beyond C1. Only this report was intentionally written; HEAD and index were not changed.
