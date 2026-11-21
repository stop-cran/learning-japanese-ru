# B235 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `75b2616d78a93d0655a2e7494abb6c1f9585ad10` (tree `a46106ee98c575dabd9e73ed70b1185de4ccd995`),
> the signed candidate pushed before review.
> Later reconciliation is in `235-words-batch-74-recheck-001.md`.

Snapshot: RU candidate 75b2616d78a93d0655a2e7494abb6c1f9585ad10; HEAD verified at start and completion, with empty git status --porcelain both times. Frozen EN source 6af98cb717755690a9ca793e5454a96ebd7a8f9f. No uncommitted repository changes included.

Scope: blind, read-only correctness/scoped coverage of all 30 batch-235 cards versus frozen EN. Model not independently verifiable. No forbidden reports/records read, repository edits or generators.

Full-reading attestation: every listed file read completely in BOTH RU and EN, including metadata, examples/kana, explanations, comparisons and citations.

| File | RU | EN |
|---|---|---|
| words\輸血.md | Full | Full |
| words\載る.md | Full | Full |
| words\転がる.md | Full | Full |
| words\転がす.md | Full | Full |
| words\転々.md | Full | Full |
| words\車輪.md | Full | Full |
| words\車掌.md | Full | Full |
| words\車庫.md | Full | Full |
| words\氏名.md | Full | Full |
| words\身分.md | Full | Full |
| words\蹴る.md | Full | Full |
| words\交差.md | Full | Full |
| words\踏切.md | Full | Full |
| words\跳ねる.md | Full | Full |
| words\足袋.md | Full | Full |
| words\足る.md | Full | Full |
| words\起床.md | Full | Full |
| words\赤道.md | Full | Full |
| words\賞金.md | Full | Full |
| words\賞品.md | Full | Full |
| words\資料.md | Full | Full |
| words\貸間.md | Full | Full |
| words\家屋.md | Full | Full |
| words\貸家.md | Full | Full |
| words\貸し出し.md | Full | Full |
| words\蓄える.md | Full | Full |
| words\溜まる.md | Full | Full |
| words\溜める.md | Full | Full |
| words\貯蔵.md | Full | Full |
| words\貨物.md | Full | Full |

Relevant linked baseline passages were checked, not the whole baseline. Changes in kanji\資.md and words\原料.md, 書類.md, 材料.md, 貸す.md activate links without changing prose.

Verdicts:
- Correctness: NEEDS FIX for words\跳ねる.md (C1); the other 29 cards are CLEAN.
- Scoped coverage: CLEAN for all 30. No actionable loss of selected teaching points, prerequisites, distinctions or available source links established.
- Comprehensibility and quiz safety: not assigned, not certified. CLEAN denotes absence of an established actionable defect in scope, not exhaustive correctness.

Findings:

### C1 — Past Russian gloss for an unmarked nonpast expression

- Severity: Minor.
- Facet: correctness.
- Location: words\跳ねる.md:39.
- Claim: `芝居が跳ねる（しばいがはねる）— «спектакль окончился»` translates unmarked nonpast as completed past. EN has “the show ends.” The sense is right, but the tense mismatch teaches the wrong correspondence.
- Exact remedy: replace only `«спектакль окончился»` with `«спектакль заканчивается»`. Retain the Japanese phrase, kana and surrounding explanation.
- Evidence: actual [Jisho/JMdict 跳ねる entry](https://jisho.org/word/跳ねる), entry 1429620, sense 4 (“to come to an end; to close (for the day)”); actual [Digital Daijisen は・ねる](https://www.weblio.jp/content/跳ねる), sense 4, defines the theatre use as `芝居などで、その日の興行が終わる`, with `芝居が一〇時に―・ねる`. RU line 39 and the EN comparison supply the concrete tense discrepancy. This is not an objection to translating result-state ～ています with a Russian resultative past elsewhere.
- Confidence: high.
- Status: unresolved; this reviewer made no content edits.

Evidence and coverage checks:

- Matching Jisho/JMdict forms and senses retrieved for all 30; actual pages' “Edit in JMdict” links confirm all 30 primary IDs. Rare-spelling flags were inspected directly. Search snippets, unrelated Wikipedia results and failed numerical URLs were not evidence.
- 輸血 preserves transfusion versus donation and blood sampling; actual JMdict contrasts 献血/採血 and [Daijisen 輸血](https://www.weblio.jp/content/輸血) support the blood/component distinction and noun/suru treatment.
- 載る retains intransitivity and publication/listing versus riding. 転がる/転がす preserve transitivity and secondary senses: [Daijisen 転がる](https://www.weblio.jp/content/転がる), senses 1–4, and [転がす](https://www.weblio.jp/content/転がす), senses 1–4. 転々 retains repeated changing/moving; 車輪 does not become a steering wheel.
- 車掌 remains a transport occupation, not a musical role. [Daijisen 車掌](https://www.weblio.jp/content/車掌) explicitly includes buses; [Kuznetsov/Krysin кондуктор](https://gramota.ru/poisk?query=кондуктор&mode=slovari) support transport senses. Removing an English-only “conductor” ambiguity does not remove the Japanese teaching point.
- 車庫 retains accommodation of vehicles rather than every parking place. [Daijisen 車庫](https://www.weblio.jp/content/車庫) includes buildings or places for trains and automobiles. [Kuznetsov депо](https://gramota.ru/poisk?query=депо&mode=slovari) gives railway and other specialized uses; [Russian Wiktionary депо](https://ru.wiktionary.org/wiki/депо), sense 1, describes rolling stock “обычно рельсового,” not an absolute rail-only restriction. A categorical claim that bus-related депо is impossible was therefore not established.
- 氏名 preserves しめい versus separate うじな: [Daijisen 氏名](https://www.weblio.jp/content/氏名) has separate headings. 身分 retains status/position and contextual overlap, without making kanji associations fixed semantic compartments.
- 蹴る remains godan/transitive and retains rejection as well as literal kicking. The actual [Jisho 蹴る page](https://jisho.org/word/蹴る), entry 1333400, marks 蹶る as rare. 交差 retains crossing/intersection and suru use; [Russian Wiktionary скрещение](https://ru.wiktionary.org/wiki/скрещение), sense 1, explicitly includes an intersection place and `У скрещения дорог`. That establishes recognition, not preferred frequency.
- 踏切 preserves the railway crossing and selected secondary uses, distinct from an ordinary crossroads. [Daijisen 踏切](https://www.weblio.jp/content/踏切) explicitly includes athletic takeoff/place, determination and the sumo boundary. 跳ねる preserves ichidan conjugation, splashing and the boundaries with 撥ねる/刎ねる; only C1 is defective.
- 足袋 preserves split-toe socks and the spelling qualification: actual [Jisho 足袋](https://jisho.org/word/足袋), entry 1404920, marks 単皮 rare. [Russian Wiktionary таби](https://ru.wiktionary.org/wiki/таби), sense 1, recognizes the split-toe garment. Footwear comparisons remain contextual rather than synonym equations.
- 足る remains godan, not ichidan, and preserves sufficiency versus worthiness; [Daijisen 足る](https://www.weblio.jp/content/足る) supports both. 足ってる is not thereby certified as preferred modern standard usage: the additional Weblio attestation inspected is dialectal. 起床 retains getting out of bed versus awakening; 赤道 retains the equator and qualifies unrelated readings rather than merging separate lexical entries.
- 賞金/賞品 preserve money versus an awarded item and do not promise mutually exclusive real-world labels. [Kuznetsov приз](https://gramota.ru/poisk?query=приз&mode=slovari&dicts[]=42) supports an award sense; the maritime homonym was not imported into the teaching gloss. 資料 retains information/reference materials versus raw ingredients, supporting its added links to 情報 and 材料.
- 貸間/貸家 retain room versus house let for payment and distinguish boarding/lodging from merely renting a room. [Kuznetsov внаём](https://gramota.ru/poisk?query=внаём&mode=slovari) supports temporary paid use with room/house examples. JMdict recognizes 貸家's qualified alternative forms/readings. 家屋 remains a residential building, not all possible structures; [Russian Wiktionary постройка](https://ru.wiktionary.org/wiki/постройка), sense 2, supports a constructed building/structure, with the card's residential qualification.
- 貸し出し preserves lending direction and temporary/institutional use. The bicycle-availability translation adopts the borrower's viewpoint, but the explanation still identifies the lender; no reversed lexical meaning established.
- 蓄える/溜まる/溜める retain active storage versus intransitive accumulation and the qualified money-spelling overlap. [Daijisen 溜まる](https://www.weblio.jp/content/溜まる) permits financial accumulation; [溜める](https://www.weblio.jp/content/溜める) explicitly includes unpaid rent. Russian resultative past translations of retained ～ています states are not mechanically wrong. [Kuznetsov запасти](https://gramota.ru/poisk?query=запасти&mode=slovari&dicts[]=42) includes `Запаса́ние` and `З. дров на зиму`, supporting the storage/preparation terminology.
- 貯蔵 retains noun/transitive suru use, storage and its selected contrasts; 貨物 retains cargo/goods, not baggage or freight charges. Unselected secondary dictionary senses do not create a scoped-coverage requirement.
- Source identities, readings, JLPT, type, kanji, tags and existing exclusions are retained. Added exclusions: 賞品→賞金, 資料→材料/参考, 貸間→下宿, 貸し出し→支給; presence checked, not full quiz adjudication.
- Read-only link checks found no dropped links with existing RU targets, no dropped external citations, and no broken links in these cards. Added word links are 資料→情報/材料 and 貸間→下宿. Unavailable RU targets appropriately remain plain text.
- Manual complete comparison covered Japanese text and kana throughout. A separate read-only extraction matched all 62 primary Japanese example/reading pairs exactly, allowing layout-parenthesis normalization. Current normalized-byte hashes match manifest entries for all 30 cards.

Optional:
- words\転がる.md: title could mention tumbling/lying down; the body preserves these senses. Nonblocking polish.
- 車庫: `автобусный парк` is an editorial alternative, not a proven mandatory replacement.

Limits:
- No native-speaker certification, device/reader or archive test, full quiz review, generator/validator run. Bounded custom checks do not replace those.
- Relevant baseline/secondary citations checked, not every comparison ID. Frequency, exact modern bus-depot usage and preferred register are not certified.
- No fresh KANJIDIC2 or historical-etymology audit. No consequential unresolved claim beyond C1 established in scope.
- Throttling was overcome with paced retrieval; failed/truncated outputs were not evidence. Necessary passages were reread in bounded chunks.
