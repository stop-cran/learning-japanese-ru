# B232 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `56da736ec2499c2e67dc01cd65078098c31e2716` (tree `e27c0b79e91de862b493efe3dffbc9683aa33060`),
> the signed candidate pushed before review.
> Later reconciliation is in `232-words-batch-71-recheck-001.md`.

Snapshot: RU 56da736ec2499c2e67dc01cd65078098c31e2716 against c82c00484cd5861cb43127babaad3589315fa891. HEAD confirmed before and after review; git status --porcelain empty both times. Frozen EN HEAD confirmed as 6af98cb717755690a9ca793e5454a96ebd7a8f9f. No uncommitted content included.

Scope: Independent blind, read-only correctness and scoped-coverage review. Actual reviewer model is not independently verifiable; no nested reviewers used.

Full-read attestation: each of the following RU files AND its frozen EN original was read completely, including front matter, all examples/readings, explanations and citations:
words/部首.md; words/原料.md; words/成分.md; words/部品.md; words/郡.md; words/裏返す.md;
words/お帰り.md; words/返る.md; words/遡る.md; words/遠足.md; words/対策.md; words/方角.md;
words/方針.md; words/地帯.md; words/角度.md; words/方面.md; words/道順.md; words/過失.md;
words/過半数.md; words/余る.md; words/超過.md; words/過剰.md; words/遊園地.md; words/逸れる.md;
words/統一.md; words/連合.md; words/作製.md; words/作成.md; words/製作.md; words/造船.md.

Also read the six complete RU added-link targets 町, 村, 市, 帯, 残る and 足りる; the exact titles and complete meaning sections of 構成, コース, 針路, 角, 作る, 製造, 生産 and 余分; and the changed passages in kanji/余.md, kanji/帯.md and words/余分.md. Reviewed against the three assigned RU normative files. No author/reviewer reports, tracking records, translation-batch/draft directories or prohibited scratch checkouts read.

Checks: primary Jisho/JMdict lexical entries, readings, relevant senses and word classes inspected for all 30 cards; their 30 cited primary entry IDs independently matched to the Jisho pages' JMdict edit links. Relevant Daijisen and Seisenban entries inspected separately from adjacent aggregator content. Metadata comparison found no removed source fields/exclusions: six cards add exclusions. All EN links with existing RU targets remain linked; new cards have no missing relative Markdown targets. Main Japanese examples/readings are preserved; Japanese-run comparison differences were checked against the localized commentary. Read-only validator: 0 errors. Independently recomputed the 33 changed card files' normalized manifest hashes: no mismatches. No generator run.

Verdicts: correctness NEEDS FIX for words/角度.md and words/遊園地.md, CLEAN for the other 28 new cards; scoped coverage CLEAN for all 30. The two findings concern inaccurate restrictions, not a missing article or missing EN example. CLEAN is bounded, not exhaustive certification. Russian comprehensibility and comprehensive quiz safety are not assigned verdicts.

Findings:

C1; Minor; correctness; words/角度.md:4,12.
Claim/impact: «величина угла (в градусах)» presents degrees as part of the title's meaning restriction. The word also denotes angular magnitude expressed in radians or other angular units; the body's correct explanation at lines 38–39 does not remove the misleading title qualification.
Remedy: replace the title and H1 gloss with «величина угла; ракурс (точка обзора)». Existing exclusion with 角 can remain.
Evidence: Digital Daijisen, 角度 sense 1, explicitly lists «ラジアン・度・分(ふん)・秒» (https://www.weblio.jp/content/角度). The actually inspected Seisenban definition 1 likewise contrasts specialist radians with practical degrees/minutes/seconds (https://kotobank.jp/word/角度-460585). EN title is unrestricted «angle; viewpoint».
Confidence: high. Status: unresolved; no edits authorized.

C2; Minor; correctness; words/遊園地.md:31–32.
Claim/impact: «…там можно отдыхать или играть, но это не парк аттракционов» turns EN's possible distinction into a categorical exclusion. It teaches that a 公園 cannot be an amusement park.
Remedy: «[公園](公園.md)（こうえん）— общественный парк: там можно отдыхать или играть, но он не обязательно является парком аттракционов.»
Evidence: Digital Daijisen, 公園 sense 1, explicitly includes publicly provided «庭園や遊園地» (https://www.weblio.jp/content/公園). Frozen EN words/遊園地.md:32 says a public park «can be a place to relax or play without being an amusement park», not that the categories never overlap.
Confidence: high. Status: unresolved; no edits authorized. This does not itself recommend a quiz-exclusion change, which needs the separate quiz assessment.

Optional: None required. Several scrutinized points do NOT establish additional defects:

- The masculine first-person past forms are legitimate concrete Russian example translations, not claims that Japanese marks male speakers. Japanese omitted subjects permit contextual «я/мы/у нас» as in the EN examples. «Давал почитать» is a natural general-factual imperfective for the completed loan; «ко мне» fits 返ってきました with the speaker as lender. «Туда» supplies the destination implicit in explaining a route. Neither forces a universal grammatical mapping.
- 成分's example «состав продукта» is supported by JMdict's explicit composition gloss; it does not assert unrestricted interchangeability with 構成. «Угол» and «курс» in example translations likewise do not erase the cards' explicit semantic contrasts.
- The negative outcome in the overproduction example remains visible through «слишком много»; てしまう is not invariably an explicit statement of regret. Adding «к сожалению» everywhere would overtranslate. The completed digression translation is acceptable.
- «Запчасть» and «перерасход» are legitimate contextual narrower equivalents alongside broader first glosses, not assertions that every 部品 is a replacement or every 超過 is spending. Phrase-like Russian glosses in 方面, 道順 and 過半数 are explained by the noun labels and constructions.
- Removing the English-only compatible/frame gloss warnings is justified: those English glosses are not offered to RU learners. The other localized contrasts preserve the Japanese teaching distinctions; the plain pointer to the untranslated かえる article is not a broken link.

Supporting evidence for scrutinized adaptations: Kuznetsov via Gramota defines сырьё as extracted OR produced material for further processing (https://gramota.ru/poisk?query=сырьё&mode=slovari&dicts[]=42), комплектующие as technical-product components (same query pattern for комплектующие), перерасход as expenditure above a norm/plan (перерасход), and ракурс sense 3 as viewpoint (https://gramota.ru/poisk?query=ракурс&mode=slovari). Its запчасти entry explicitly gives singular запчасть and replacement parts. Wiktionary's actually inspected радикал I sense 3 equates it with иероглифический ключ (https://ru.wiktionary.org/wiki/радикал); оплошность sense 2 is a mistaken act/blunder; судостроение sense 1 is ship production/industry; верфь sense 1 covers building and repairing vessels; пособие sense 2 includes an instructional book (corresponding same-headword Wiktionary pages). Thus these terms need no invented corrections.

The actual Russian encyclopedia usage «Уезды Японии» identifies 郡 (https://dic.academic.ru/dic.nsf/ruwiki/1339818); used for terminology only, not its dated administrative history. Modern structure is corroborated by the Daijisen 郡 entry. Nipponica's inspected 遠足 section supports day trips, buses/trains and varied school groupings (https://kotobank.jp/word/遠足-170815); «выезд классом» is a concrete school-context rendering, not a claim that every outing is exactly one class. Russian clinical usage attests «тактика лечения» (https://cyberleninka.ru/article/n/k-voprosu-o-lechebnoy-taktike-i-strategii-pri-yazvennoy-bolezni-v-sovremennyh-usloviyah); it is an acceptable contextual 方針 translation.

Daijisen confirms 部品 as shortened 部分品, 成分's grammatical/vector extensions, 郡's historical こおり, 方角's thought/method extensions, 返る's 裾が返る, and 造船's タンカーを造船する. The latter is not contradicted by JMdict's intransitive tag. Jisho's complete 連合 page explicitly marks 聯合 «Rarely-used kanji form» and records RENGO; its 越える page places 超える particularly in the exceeding sense. The separate 反る/そる entry is 1480170. Daijisen 湯桶読み confirms native-first/on-second classification (https://www.weblio.jp/content/湯桶読み); 道順 explains it before naming it. The godan/ichidan/native/on terminology and examples retain the source's classifications. Digital Daijisen is the source's proper name, not untranslated explanatory prose.

Limits: No native-speaker, device, media, archive or learning-effectiveness testing. Not every supplementary comparison ID was independently re-fetched, nor was every suggested baseline comparison article read in full; the exact actual baseline scope is stated above. Some Gramota requests returned 429 and direct Python Wiktionary requests returned 403; relevant actual entries were subsequently read through the available web-fetch path or established usage sources. Jisho API output omits some spelling annotations, so 聯合 was checked on the complete page. The current Daijisen 遡る entry confirms upstream/past uses but does not print the exact 四月に遡って適用する string; the retroactive sense is independently supported by inspected JMdict sense 2, and the construction is retained from EN, not claimed as a newly attested verbatim quotation. The initial oversized shell outputs were not treated as full-read evidence; all 30 assigned pairs were subsequently returned completely in bounded two-pair reads. Only this report was intentionally written; repository HEAD, index and working tree remained unchanged.
