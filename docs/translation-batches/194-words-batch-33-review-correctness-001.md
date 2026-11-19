# B194 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `6947a60b9c7d3731fd7f76d426d5721db87c55ee` (tree `b3d62aa2c27ac5821b90274487ade692874be11f`),
> the signed candidate pushed before review.
> The final "Addendum" section is a post-blind follow-up requested by the coordinator on the same candidate,
> checking nine Russian lexical choices against Gramota entries; the blind report above it is unchanged.
> Later reconciliation is in `194-words-batch-33-recheck-001.md`.

Snapshot: RU 6947a60b9c7d3731fd7f76d426d5721db87c55ee, compared with afec4b7; HEAD matched the requested candidate and the working tree was clean before and after review. Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f; its working tree was also clean. No uncommitted repository changes included.

Scope: Blind, read-only correctness and scoped-coverage review. Read all 30 RU cards and all 30 frozen EN originals in full: 解決, 解ける, 解く, 観察, 観客, 観光, 親友, 覚悟, 覚める, 覚ます, 見解, 見舞い, 偉い, 上等, 見事, 覆う, 要素, 要点, すなわち, つまり, 要するに, 製品, 裸, 裏切る, 裁判, 害, 被害, 被る, 袖, 袋. Read the three binding RU instruction/format documents. Compared complete existing RU cards 答, 決定, 済む, 答える, 解釈, 理解, 起きる, お見舞い, 見物, 立派, 優秀 and 友人 for relevant conventions and distinctions. Inspected all changed passages in the four existing kanji cards, eight existing word cards and manifest. Actual reviewer model is not independently verifiable.

Verdicts: correctness CLEAN; scoped coverage CLEAN; no per-article exceptions.

Findings: none. No actionable correctness defect or omission within the assigned source-relative scope was established.

Review evidence:

- Compared every example translation and explanatory passage against EN, including tense, negation, affected participant, transitivity, particle roles, register qualifications and the boundaries of component-based memory aids. The が/を contrasts in 解ける/解く and 覚める/覚ます remain explicit; 目を覚ます is not misrepresented as necessarily waking another person. English-dependent observations in 覚める, 覚ます, 要点, 被る and 袋 were adapted without losing the Japanese rule.
- All 30 front matters retain the source word, reading, JLPT level, type, kanji and tags. Every original exclusion remains present; additions do not replace original exclusions. All cited seven-digit dictionary IDs match the respective EN originals.
- All EN teaching senses, examples, comparison labels and dictionary citations remain represented. Removed internal hyperlinks point only to targets absent from this RU snapshot; their visible words, readings and explanations remain. This is not a missing comparison or an instruction to import additional cards.
- Checked Japanese-body character projections across all 30 pairs and manually reconciled their differences: harmless repetition/reordering in translated prose or the restored visible label 服. Japanese sentences, readings and conjugated forms were retained. Surrounding parentheses, Markdown spacing and line wrapping are localized/reformatted, so this is not a claim of byte-identical Japanese-bearing lines.
- Queried and inspected the actual Jisho JMdict API entries for every assigned word on 2026-11-19, selecting exact spellings/readings rather than accepting the first search result or Wikipedia definitions. For kana headwords, inspected 即ち（すなわち）and 詰まり（つまり）. API endpoint used for each word: `https://jisho.org/api/v1/search/words?keyword=<URL-encoded word>`.

Particularly consequential dictionary confirmations:

- [解決](https://jisho.org/search/解決): sense 1, settlement/solution/resolution, both transitive and intransitive suru-verb. [解ける](https://jisho.org/search/解ける): とける entry, senses 1–4, solution, untying, lifted restrictions and eased tension; distinguished the separate ほどける entry. [解く](https://jisho.org/search/解く): とく entry, senses 1, 3 and 4, untying, solving and dispelling misunderstandings.
- [観察](https://jisho.org/search/観察), sense 1: observation, transitive suru-verb; [観客](https://jisho.org/search/観客), sense 1: spectator/audience with かんきゃく recorded; [観光](https://jisho.org/search/観光), sense 1: sightseeing/tourism, transitive suru-verb; [親友](https://jisho.org/search/親友), sense 1: close friend.
- [覚悟](https://jisho.org/search/覚悟), senses 1–3: mental preparedness, determination and resignation; [覚める](https://jisho.org/search/覚める), senses 1–2: waking and recovery from intoxication/anaesthesia; [覚ます](https://jisho.org/search/覚ます), sense 1: transitive awakening. The cards preserve their distinct constructions.
- [見解](https://jisho.org/search/見解), sense 1: opinion/point of view; [見舞い](https://jisho.org/search/見舞い), senses 1–2: illness/misfortune visit or inquiry, sympathy, and corresponding letter/gift.
- [偉い](https://jisho.org/search/偉い), senses 1–2: admirable and high-ranking, with usually-kana qualifications attached to later senses; [上等](https://jisho.org/search/上等), senses 1–2: superior quality with な/の modification and the “just fine/bring it on” exclamation; [見事](https://jisho.org/search/見事), senses 1–3: praise, completeness (usually 見事に), and the archaic noun “something worth seeing.”
- [覆う](https://jisho.org/search/覆う), sense 1: transitive covering/hiding; [要素](https://jisho.org/search/要素), senses 1–2: constituent/factor and computing element/member; [要点](https://jisho.org/search/要点), sense 1: gist/main point.
- [すなわち](https://jisho.org/search/すなわち), restatement sense and usually-kana marking; [つまり](https://jisho.org/search/つまり), senses 1–2: restatement and summary, distinct from later noun senses; [要するに](https://jisho.org/search/要するに), sense 1: summary expression/adverb. No unsupported rigid register hierarchy was introduced.
- [製品](https://jisho.org/search/製品), manufactured/finished goods; [裸](https://jisho.org/search/裸), senses 1–2 and noun/no modification; [裏切る](https://jisho.org/search/裏切る), senses 1–2, betrayal and disappointment; [裁判](https://jisho.org/search/裁判), sense 1, trial/judgment and transitive suru-verb.
- [害](https://jisho.org/search/害) and [被害](https://jisho.org/search/被害), sense 1 in each: harm versus suffering damage, both nouns. [被る](https://jisho.org/search/被る): separate かぶる and こうむる entries; inspected かぶる senses 1 and 3, including usually-kana tags, and こうむる sense 1. [袖](https://jisho.org/search/袖), sense 1: clothing sleeve; [袋](https://jisho.org/search/袋), ふくろ sense 1: bag/sack/pouch, not the separate たい counter.
- Read-only validation: `python -X utf8 -B tools\validate.py` returned exit 0, `0 error(s)`. Independently compared LF-normalized SHA-256 hashes of all 42 changed word/kanji files with manifest entries: zero mismatches. Neither command regenerated content or manifest.

Optional: none.

Limits: CLEAN is bounded to the assigned correctness/source-relative coverage review, not exhaustive linguistic certification. Baseline comparisons were the complete cards and changed passages identified above, not a full reread of every suggested related card. This is not a separate comprehensibility or corpus-wide quiz-safety verdict. Dictionary checking used live Jisho JMdict entry/sense data, not an independent historical/etymological or frequency investigation; the reviewed cards appropriately qualify those boundaries. No author report, author prompt, title-screen output, other reviewer report, RU batch/draft records or translation tracking was read. No repository file was edited, staged, committed, pushed or checked out; only this report was written.

Finding counts: critical 0; major 0; minor 0.

## Addendum: Russian lexical check (post-blind follow-up)

Snapshot: Same candidate 6947a60; earlier blind report preserved.
Scope: Nine choices; actual Gramota entries inspected 2026-11-19. BTS = Kuznetsov's Bolshoy tolkovyy slovar; BUS = Morkovkin et al.'s Bolshoy universalnyy slovar.
Verdicts: correctness CLEAN; scoped coverage CLEAN for all nine checks.

Per-item verdicts and evidence:

- 観客: CLEAN. BUS [зритель](https://gramota.ru/poisk?query=зритель&mode=slovari&dicts[]=48), 1.1 includes performances and sports; BTS [публика](https://gramota.ru/meta/publika), 1 covers attending visitors, spectators or listeners. Fits the individual/collective spectator sense, not every Russian use.
- 袖: CLEAN. BTS [рукав](https://gramota.ru/poisk?query=рукав&mode=slovari&dicts[]=42), 1 is the garment part covering an arm or part of it. Exact clothing sense, not a river branch or hose.
- 袋: CLEAN. BTS [пакет](https://gramota.ru/meta/paket), 1's container subsense, and [мешок](https://gramota.ru/meta/meshok), 1 support packaging/storage containers. Babenko's noun dictionary on the first page explicitly includes paper/polyethylene bags. Fits the card's container meaning, without restricting 袋 to one material.
- 裸: CLEAN. BTS [голый](https://gramota.ru/meta/golyy), 1 and 3 cover unclothed and uncovered; [неприкрытый](https://gramota.ru/meta/neprikrytyy), 2 means lacking a covering. Fits naked/bare; unrelated Russian senses do not transfer automatically.
- 裏切る: CLEAN. BTS [предать](https://gramota.ru/meta/predat), 1 includes violating loyalty and records imperfective предавать; [подвести](https://gramota.ru/meta/podvesti), 8 includes disappointing hopes/expectations, including nonhuman causes, and records подводить. Fits betrayal/letting down, not literal leading.
- 解決: CLEAN. BTS [урегулировать](https://gramota.ru/meta/uregulirovat) defines settling issues and lists derived урегулирование with issue/relationship examples. Fits resolution/settlement, not merely choosing an option.
- 偉い: CLEAN. BTS [высокопоставленный](https://gramota.ru/poisk?query=высокопоставленный&mode=slovari), sole definition: holding high social or official position. Fits the explicitly taught rank sense, not every praise use.
- 要素: CLEAN. BTS [составляющая](https://gramota.ru/poisk?query=составляющая&mode=slovari&dicts[]=42), sole definition: something forming part of a whole; its example concerns a component of success. Fits constituent/factor, including abstract constituents.
- 製品: CLEAN. BTS [изделие](https://gramota.ru/meta/izdelie) means a manufactured/made thing; [продукция](https://gramota.ru/poisk?query=продукция&mode=slovari), main definition and production subsense, means output/products of production. Fits an item or collective manufactured output; not a foodstuffs-only gloss.

Findings: none; critical 0, major 0, minor 0.
Optional: none.
Limits: Taught senses only, not universal synonymy or a quiz audit. Initial 429/404 failures were superseded by successful entry reads above. No other FILES documents read; only this addendum appended.
