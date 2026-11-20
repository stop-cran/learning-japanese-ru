# B217 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `4af7ea72f6c372d31a810a783ca4b8655dd4ba44` (tree `7d76a5cff85d39b882c357ad2718d0fd71662b5c`),
> the signed candidate pushed before review.
> Later reconciliation is in `217-words-batch-56-recheck-001.md`.

Snapshot: RU candidate 4af7ea72f6c372d31a810a783ca4b8655dd4ba44; baseline 28c75781d9cd9ca51498f2e6ec4bab5dd9805cc6; frozen EN checkout designated 6af98cb. HEAD matched the candidate and git status --porcelain was empty both before and after review. No uncommitted changes included. No repository files, index or HEAD modified; no generators run.

Scope: Independent blind READ-ONLY review of correctness and scoped coverage. Model identity/version not independently verifiable. Every following RU file was read IN FULL against its complete frozen EN original:
- words/刀.md
- words/出会い.md
- words/出.md
- words/処理.md
- words/凍る.md
- words/冗談.md
- words/冒険.md
- words/再び.md
- words/円.md
- words/具体.md
- words/共通.md
- words/共に.md
- words/公平.md
- words/全国.md
- words/全員.md
- words/全て.md
- words/全.md
- words/全体.md
- words/党.md
- words/免許.md
- words/克服.md
- words/先日.md
- words/優勝.md
- words/優れる.md
- words/僅か.md
- words/傷.md
- words/健康.md
- words/停留所.md
- words/借金.md
- words/候補.md

Also read the binding RU instructions/reference; existing ナイフ, 出身, 流れ, 一緒, このあいだ and 勝ち cards in full for conventions/context; all changed hunks in the five existing kanji cards and nineteen existing word cards (link-only integrations). No author/reviewer reports, tracking ledger, batch records or scratch worktrees read. Comprehensibility and whole-pool quiz safety are not assigned verdicts.

Verdicts: correctness NEEDS FIX (one minor localized definition defect in words/克服.md; other 29 cards CLEAN within the reviewed scope); scoped coverage CLEAN for all 30 cards.

Findings:

F1; Minor; correctness; words/克服.md:15.
Claim: «克服 — преодоление трудности, способность взять её под контроль» introduces ability as a definition of 克服. The EN original says “overcoming or bringing a difficulty under control”, not ability; JMdict likewise gives the action, not a capacity. A learner could incorrectly name a mere capability 克服. The remaining explanation and examples correctly describe overcoming, so the defect is localized and minor.
Remedy: replace the first sentence with «克服 — преодоление трудности, взятие её под контроль.» Preserve the following を and たい guidance.
Evidence: actual [Jisho/JMdict 克服 entry](https://jisho.org/search/克服), lexical sense 1: overcoming/surmounting/bringing under control, noun + transitive する; inspected through its [API response](https://jisho.org/api/v1/search/words?keyword=克服). [Кузнецов, «способность», sense 1](https://gramota.ru/poisk?query=способность&mode=slovari&dicts[]=42) explicitly defines possibility/ability to perform an action, rather than the action being performed. EN words/克服.md:15 supplies the exact source contrast.
Confidence: high.

Optional: none.

Evidence and completed checks:

- Inspected actual Jisho/JMdict entries for all 30 headwords through https://jisho.org/api/v1/search/words?keyword=<headword>, excluding Wikipedia objects as evidence. Also inspected 皆, この間, 勝ち and 運転免許. Confirmed 刀's reading restrictions, 円/丸 and slang-money distinction, 出会い/出合い spelling, parts of speech/transitivity, kana-use notes, and 停留所's readings. The added RU guards have direct lexical overlap; this is not a full quiz audit.
- Compared all 60 primary Japanese examples and their kana lines, plus the inline constructions, manually against EN. A separate exact-substring check also covered 59 primary sentence/kana pairs; 冗談's quoted dialogue was checked manually because its closing quotation mark falls outside that check's pattern. The reading-join passages retain EN katakana and identify on readings appropriately; no new RU-only Japanese sentence without its required reading line was found.
- No consequential tense, polarity, voice, transitivity or end-state mismatch established in the example translations. Russian masculine first-person past forms such as «я переехал» are contextual renderings, not an asserted Japanese masculine feature; explicitly female 彼女 remains female. The たい goal in 克服 and ongoing repayment in 借金 remain distinct from achieved completion. 運転免許 is naturally translated «водительские права».
- Metadata retains EN values except translated titles and added RU guards. Link checks found no missing target or dropped live EN link. Untranslated targets remain plain text. EN teaching senses, necessary rules, examples and citations remain represented; omitted English-dependent commentary removes no Japanese teaching point.
- `python -X utf8 -B tools\validate.py` on the primary RU checkout: **0 error(s)**. No manifest builder or other generator invoked. Final `git diff --quiet`, `git diff --cached --quiet` and empty status confirmed the reviewed tree/index stayed unchanged.

Russian lexical evidence inspected (definitions, not search summaries):

Unless specified otherwise, these are actual Кузнецов БТС entries on Gramota: `https://gramota.ru/poisk?query=<lemma>&mode=slovari&dicts[]=42`. Listed senses were inspected, not inferred from snippets.

- [«катана», Wiktionary, sense 1](https://ru.wiktionary.org/wiki/катана): traditional Japanese sword; Gramota had no exact lexical entry, so its fuzzy results were not used as evidence.
- «выходец» 1–2: person from another country/region or originating in a social stratum; «вытекание» cross-reference followed to «вытечь»: flowing out in a stream/drops. These support the qualified 出 title; the graduate meaning is independently supported by JMdict 出 sense 4.
- «встреча» 1 and «знакомство» 1, 4: meeting and becoming acquainted/knowledge of something; match 出会い's person/thing scope.
- «обработка»: handling data/information and other objects; «улаживание» cross-reference supplemented by [«уладить», Wiktionary 1–2](https://ru.wiktionary.org/wiki/уладить): bringing a matter/formalities to a desired result, settling disagreements.
- «покрыться» 2 and its imperfective покрываться: becoming covered on the surface; «лёд» 1: frozen water. Supports the frozen-over, not necessarily frozen-through reading.
- «вновь»: once more/again; «повторный» and its adverb повторно: recurring/second occurrence. The card explicitly retains the caveat against inferring an exact total occurrence count.
- «иена»: Japan's currency unit; «круг» 1: area bounded by a circumference or the circumference itself. «Круг (геометрический)» is therefore not rejected merely for the school distinction between circle and disk.
- «воплощение» 2: form of expression of an idea; «конкретный» and derived конкретность: materially definite/nonabstract. Supports 具体 without making bare 具体 an adjective.
- «общий» 3–4: jointly belonging/shared, similar or coinciding; 8 and 10: general/non-detailed. Supports both 共通's title and the Russian-only contrast in its final section.
- «сообща»: jointly/by common effort; «сообща с» also means together with. JMdict 共に's separate “both” sense prevents reducing both-parents-are-doctors to working jointly.
- «общенациональный»: covering/concerning the whole nation. The 全国 card qualifies this as a possible attributive rendering rather than claiming that 全国 is itself an adjective.
- «весь» 1, 3: whole/full extent and each item/person without omission; «целый» 2, 4 and its «в целом» construction: full entirety, integrated whole, overall. Supports the all/whole family while the cards retain context-limited scope and partial negation.
- «партия» 1, 4, 6: political organization, batch of goods, complete game. The localized contrast does not equate 党 with a goods batch/game, and the separate liking suffix remains explained.
- «лицензия» 1–3: official authorization for specified activities, sometimes its document. The card separately gives the driving-context rendering and does not call ordinary Russian driving papers a “водительская лицензия”.
- [«преодолеть», Wiktionary 2](https://ru.wiktionary.org/wiki/преодолеть): cope with/master something; not merely have the capacity to do so (F1).
- [«на днях», Большой универсальный словарь, senses 1.0–1.1](https://gramota.ru/poisk?query=на%20днях&mode=slovari): near future with present/future predicates versus recent past with past predicates. 先日 is correctly restricted to the latter.
- «чемпионат»: competition for primacy; JMdict 優勝 sense 1 gives overall victory/winning the title, supporting the first-place qualification, not merely winning one round.
- «превосходить» cross-reference followed to [«превзойти», Wiktionary 1](https://ru.wiktionary.org/wiki/превзойти): superiority in a respect; «выделяться» links to выделиться. The Japanese source separately confirms excellence, with field に and comparison より preserved.
- «незначительный» 1: small in amount/size/degree; [«лишь», Wiktionary 1](https://ru.wiktionary.org/wiki/лишь): restrictive “only”. Supports わずか's two displayed uses without requiring a negative predicate.
- «остановка» 1–2: action of stopping versus designated passenger boarding/alighting place. The card explicitly teaches the place, and the next-stop translation retains the intended future event through normal Russian present-for-scheduled/imminent-future usage.
- «заём»: receiving/taking money or valuables on repayment terms; «кандидат» 1: someone considered for selection; «вариант» 1 (including a route choice), 2: variant/possibility. Supports borrower-side 借金 and non-person 候補 without asserting an election or completed final selection.

Limits: All 30 new articles read fully; existing whole-card comparisons limited to the six named cards, other integrations to changed hunks. No full quiz-pool, native-speaker, frequency, app/device or publication acceptance claimed. Gramota HTTP 429 and urllib/Wiktionary HTTP 403 failures were supplemented by successful web_fetch entries or inspected cross-referenced lemmas, not treated as evidence. Lexical recognition does not prove universal interchangeability. No consequential unresolved claim remains beyond F1.
