# B222 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `d0d6d08431a1e7dd81d6eaa151a8c841c37c297e` (tree `c6b8f7f32697ac0e681e2544e3deb8f92208352a`),
> the signed candidate pushed before review.
> Later reconciliation is in `222-words-batch-61-recheck-001.md`.

Snapshot: RU d0d6d08431a1e7dd81d6eaa151a8c841c37c297e, compared with parent 908d7c0c82c9c0dac69488119c6d9cd3c6c1a9cd; HEAD confirmed before and after review, git status --porcelain empty both times. Frozen EN HEAD independently confirmed as 6af98cb717755690a9ca793e5454a96ebd7a8f9f. No repository edits, index changes, generators, commits or publication.

Scope: Independent BLIND read-only CORRECTNESS and SCOPED COVERAGE review. Actual model identifier not verifiable. Binding RU instructions and format reference read. No author reports/prompts, title-screen output, other reviews, batch/draft directories or translation-tracking read.

Full-reading attestation: EVERY following RU file was read IN FULL against its complete frozen EN original (each filename below is under words/):
カード.md; トランプ.md; トラック.md; デート.md; デモ.md; テント.md; チーム.md; チーズ.md; チャンス.md; ダンス.md; ダイヤ.md; タオル.md; タイプライター.md; ソファー.md; センター.md; セット.md; スープ.md; スター.md; スタンド.md; スタイル.md; スケート.md; スキー.md; スイッチ.md; ジーンズ.md; ジュース.md; ジェット機.md; サービス.md; ゲーム.md; グループ.md; グランド.md.
Also read RU 望み, 地図, 踊り, 台, いす, ガソリンスタンド, 履く and ベンチ in full; inspected all seven baseline navigation-only diffs and the suggested comparator titles. This is not a full-body review of every suggested comparator or a whole-pool quiz audit.

Verdicts: correctness NEEDS FIX (カード; title-scope defects in ダイヤ, スター, スタンド); scoped coverage NEEDS FIX (those titles and ソファー navigation). Other new cards: CLEAN in these bounded facets; no verdict on independent comprehensibility/quiz-safety facets. CLEAN means no established actionable defect, not exhaustive correctness.

Findings:

C1; Minor; correctness; words/カード.md:35.
Claim/impact: «словом „карточка“ называют также скребок для теста» transfers a JAPANESE dictionary sense to the Russian noun. EN describes the card entry, not a Russian baking-tool name. This teaches the wrong lexical identity.
Remedy: «В некоторых японских текстах о выпечке カード называют также скребок для теста; это значение не доказывает, что „сгусток“ входит в ту же словарную запись».
Evidence: actual entries at https://jisho.org/search/カード: JMdict 1036400 sense 7 “dough scraper; spatula”; separate 2848325 “curd”. Compare frozen EN カード:32. Russian «карточка» entry https://gramota.ru/meta/kartochka contains information/document/photo senses, not a dough-scraper sense. The positive Japanese evidence, not mere Russian dictionary silence, establishes the mistranslated referent.
Confidence: high.

C2; Minor; correctness; words/カード.md:31.
Claim/impact: «„картой“ カード бывает только как платёжная или игральная карта» makes an exhaustive Russian/Japanese boundary that the information-card sense does not support. The geographical contrast is sound; «только» is not. Non-payment information/identification cards are not thereby excluded from Russian «карта».
Remedy: «Географическая карта по-японски — [地図](地図.md)（ちず）, а не カード. В контексте оплаты или карточной игры カード переводится как „карта“; в других контекстах перевод выбирают по виду карточки».
Evidence: actual JMdict 1036400 senses 1–4 at https://jisho.org/search/カード; Russian «карта» sense 3 (information form) at https://gramota.ru/meta/karta and identification/payment sense 3 at https://ru.wiktionary.org/wiki/карта (actual wikitext inspected). These entries do not support the stated exhaustive restriction.
Confidence: high.

C3; Minor; correctness/scoped coverage; words/ダイヤ.md:4,12,16,36; words/スター.md:4,12,16,33; words/スタンド.md:4,12,17.
Claim/impact: three short labels narrow a broad source headword despite retaining the broader sense in the body:
- ダイヤ: «бриллиант» requires a cut/polished diamond; EN “diamond” and RU line 16 also include «алмаз». Use «алмаз; бриллиант; график движения поездов», and describe entry 1076860 as «алмаз; бриллиант», not only «бриллиант». The ring example itself is correctly translated.
- スター: «звезда (кино, спорта и т. п.)» plus «знаменитость» restricts both equivalents to people, losing the source title's general “star” coverage although symbol/celestial senses are explicitly taught. Use «звезда; знаменитость»; retain the useful contextual explanation in the body.
- スタンド: «настольная лампа» excludes the floor lamp expressly retained in RU line 17 and EN. Use «трибуна; подставка, стойка; настольная или напольная лампа».
Evidence: JMdict 1076860 at https://jisho.org/search/ダイヤ; Japanese ダイヤ = ダイヤモンド① at https://kotobank.jp/word/だいや-2058663 and the unrestricted mineral definition at https://kotobank.jp/word/だいやもんど-3158516; Russian «бриллиант» sense 1 at https://gramota.ru/meta/brilliant explicitly requires cutting/polishing. JMdict 1069210 senses 1–3 at https://jisho.org/search/スター and Russian «звезда» senses 1,3,4 at https://gramota.ru/meta/zvezda. JMdict 1069930 sense 4 at https://jisho.org/search/スタンド explicitly lists desk/floor/standard lamps; Russian «лампа» sense 1 at https://gramota.ru/meta/lampa is not restricted to desk lamps.
Confidence: high on the lexical restrictions; medium-high on their short-label learning impact. These are scope losses, not a demand to list every dictionary sense. Re-screen actual quiz labels if titles change.

C4; Minor; scoped coverage/navigation; words/ソファー.md:28.
Claim/impact: ベンチ is an explicit substantive furniture comparison but remains unlinked even though words/ベンチ.md exists in this snapshot. The restored ベンチ→ソファー link works and its comparison is accurate; it does not supply the missing opposite navigation.
Remedy: replace «ベンチ — скамья» with «[ベンチ](ベンチ.md) — скамья».
Evidence: both complete runtime cards inspected, including ベンチ:28; binding RU content-structure instructions require links when substantively introducing/comparing an available card. This is not an allegedly dropped EN link: the frozen EN mention was also plain text.
Confidence: high.

Evidence checks without findings:
- All source front-matter fields except translated title/additive exclusions match; no original exclusion lost. All EN local links whose RU target exists are retained. The non-linked untranslated targets are not defects. Full paired reads found the main Japanese examples/readings retained, including スタイル's hiragana reading lines and グランド's all-kana example without an added reading line. English-only contrasts were assessed as adaptations, not mechanically required.
- 望みがある versus チャンス is a defensible contextual distinction, not an asserted substitution ban: actual 望み entry 1519620 senses 1–2 and チャンス 1078040 sense 1 at https://jisho.org/search/望み and https://jisho.org/search/チャンス; Russian «надежда» and «шанс» entries https://gramota.ru/meta/nadezhda and https://gramota.ru/meta/shans. The seven added RU links preserve the described Japanese senses; no new malformed Japanese sentence established.
- Actual Gramota entries inspected for the Russian-only title vocabulary: карточка/открытка, демонстрация, команда, шанс, танец, диван, центр, набор/установка/настройка, звезда, трибуна, стиль/фигура, выключатель/переключатель, группа, бонус. Subject to C1–C3, no wrong equivalent established. «Бонус» includes additional reward/seller's discount: https://gramota.ru/meta/bonus.
- Specialist evidence inspected: «сырный сгусток» matches https://ru.wiktionary.org/wiki/сгусток and exact cheesemaking usage at https://zefbio.ru/chto-takoe-sychuzhnyj-ferment-i-ego-rol-v-syrode-13000; tennis «ровно» = deuce (40:40) at https://tennis-hub.ru/blog/tennisnyj-slovar.html, consistent with JMdict 2843595 and ジュース. «Деним» = jeans fabric at https://ru.wiktionary.org/wiki/деним; «шатёр» = large tent at https://gramota.ru/meta/shater; Speed Skating at https://megabook.ru/article/Скоростной+бег+на+коньках.
- センター: JMdict and https://kotobank.jp/word/せんたー-3213339; commercial facility supported by https://kotobank.jp/word/しよつぴんぐせんたー-3154712 and Russian «центр» sense 4. «Центральный полевой игрок» occurs at https://scandict.com/ru/dictionary/centre-field-k5ZjN; weak evidence for standardized terminology, not evidence of error.
- Restaurant usage: https://kartaslov.ru/предложения-со-словосочетанием/за+счёт+заведения; compound «гранд-»: Kuznetsov https://gufo.me/dict/kuznetsov/гранд_e31. «Свежее полотенце»: https://gramota.ru/meta/svezhiy sense 3 (clean/unused linen); EN itself uses “fresh”.
- Read-only structural validation: python -X utf8 -B tools\\validate.py, in the primary RU checkout: exit 0, 0 errors. No generator run.

Optional (nonblocking, not further established defects): prefer «поздравительную открытку»; soften スープ:20 to «по-русски обычно говорят „есть суп“»; in センター's title keep general «центр» and qualify the player «(в бейсболе)»; clarify ジュース:23's tennis term as «40:40 и последующие равенства в гейме».

Limits: No native/frequency certification, fresh full JMdict reconstruction of unchanged EN facts, or full quiz/manifest/publication audit. Failed 429/404 requests are not evidence; actual successful entries support the conclusions. Some specialist phrases have usage rather than normative-headword evidence (especially ScanDict). The initial oversized read returned only a preview and was not counted: all cards were subsequently returned completely in three-card RU/EN batches. Only this report was written.
