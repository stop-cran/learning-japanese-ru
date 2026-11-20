# B215 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `2ae93fbb0633b03857d1ae4bade78a29dccba880` (tree `f3c26c5c643abd893a8e005cbc9d79d84a255f74`),
> the signed candidate pushed before review.
> Later reconciliation is in `215-words-batch-54-recheck-001.md`.

Snapshot: RU 2ae93fbb0633b03857d1ae4bade78a29dccba880, compared with parent 1a4cb33b654537125e535a6074dd7e7f14808b6d. HEAD matched and git status --porcelain was empty at both opening and closing checks; no uncommitted content included. EN source: supplied frozen checkout 6af98cb.

Scope: BLIND, read-only correctness and scoped coverage. Actual model identity is not independently verifiable. Each following RU file was read IN FULL against its complete frozen EN original:
words/名人.md; words/同時.md; words/同僚.md; words/合わせる.md; words/叱る.md; words/可能.md; words/可.md; words/取れる.md; words/取り上げる.md; words/収穫.md;
words/収入.md; words/双子.md; words/友情.md; words/及ぼす.md; words/参考.md; words/参加.md; words/原.md; words/印刷.md; words/占める.md; words/博物館.md;
words/博士.md; words/単位.md; words/単に.md; words/単なる.md; words/共同.md; words/協力.md; words/医療.md; words/医師.md; words/化粧.md; words/化学.md.
Also fully read the three binding RU instruction/format files and existing RU words/上手.md, 合う.md, 怒る.md, 注意.md, 野.md, 美術館.md, 医者.md, 科学.md. Inspected all 31 baseline runtime files' link-only changed hunks, not their complete articles. No author/reviewer material, batch records, tracking or drafts read. No delegation.

Verdicts:
- Correctness: UNVERIFIED for the batch solely because the explicitly requested exact Russian dictionary verification for «зачётная единица» could not be completed (L1 below). The remaining 29 cards are CLEAN within this review; no incorrect Japanese construction, reading or Russian example translation was established.
- Scoped coverage: NEEDS FIX for words/化粧.md only (F1, minor). CLEAN for the other 29 cards. All 30 received complete paired reads; no unread-file exception.
- Comprehensibility and exhaustive quiz-pool safety: outside the assigned facets; no verdict.

Findings:
F1; Minor; scoped coverage; words/化粧.md:28–29.
Claim/impact: EN explicitly identifies け + しょう as ON readings (“The on readings here are…”); RU retains the hiragana and pronunciation warning but drops the on-reading classification (“Чтения здесь…”). This is a small, specific source-note omission, not an incorrect reading. In the contrast with 化's か, the source teaches that the alternative is still an on reading.
Remedy: replace «Чтения здесь — け + しょう» with «Онные чтения здесь — け + しょう»; preserve the hiragana and the remainder unchanged.
Evidence: the fully read frozen EN words/化粧.md, “How the kanji combine”; actual Digital Daijisen kanji entry 化, https://kotobank.jp/word/化-58505, labels カ（漢）and ケ（呉）under ［音］ and gives 化粧 under ケ.
Confidence: high; limited impact.

Evidence and retained boundaries:
- All 59 primary Japanese example sentences passed verbatim comparison; readings and supplementary constructions were read manually. Inherited metadata, dictionary references and selected senses remain. No dropped EN link with an existing RU target was found. Unavailable targets appropriately remain unlinked. Added readings in 可能, 収穫, 及ぼす and 協力 are appropriate. No source-markup leak or unsupported gender restriction was established; masculine first-person translations can represent a contextual male speaker. 化粧 retains «сделал(а)».
- Actual Jisho/JMdict records were read for ALL 30 headwords: https://jisho.org/api/v1/search/words?keyword=<headword>. Checked forms, parts of speech, selected senses/restrictions/register, excluding names and Wikipedia blocks. These support 叱る's godan/passive, 取れる removal versus potential, 参考 constructions, 博士 はかせ versus はくし and 化学's ばけがく.
- 名人: Kuznetsov, «мастер», sense 2 and the actual phraseological entry «Мастер своего дела», https://gramota.ru/meta/master, support the skilled-person title; it does not lose the EN “expert” meaning in this card. Meijin's separate title use remains.
- 合わせる: Babenko «подгонять» and Kuznetsov «подогнать», sense 5, https://gramota.ru/meta/podgonyat and https://gramota.ru/meta/podognat, support adjusting to fit. AをBに合わせる, joined efforts and 顔を合わせる remain distinct.
- 叱る: Babenko «отчитывать», https://gramota.ru/meta/otchityvat, explicitly describes a strict remark/reprimand, with a mother-and-child example. Kuznetsov «выговор», sense 2, https://gramota.ru/meta/vygovor, is «упрёк, замечание, внушение», distinct from disciplinary sense 3. Thus the mother's «сделала выговор» does not wrongly require an official sanction. Jisho 注意 sense 4 (admonishment/reprimand/telling-off), together with the existing RU 注意 card, supports the added direct guard without equating every 注意 with 叱る.
- 可: actual JMdict sense 3 supplies Pass/Fair on a 優・良・可 scale. Kuznetsov «удовлетворительно», sense 2, https://gramota.ru/meta/udovletvoritelno, names the lowest positive grade; the card's explicit “like, not exact equivalent” qualification is appropriate. «Проходной», sense 2 and its passing-score example, https://gramota.ru/meta/prokhodnoy, supports the threshold wording, not any universal percentage.
- 取れる: Kuznetsov «сойти», sense 5, https://gramota.ru/meta/soyti, is to cease covering a surface/disappear; «сходить», https://gramota.ru/meta/skhodit, supplies the imperfective. The dirt-not-coming-off example retains negation, and 取れている remains a resulting state.
- 取り上げる: Kuznetsov «вынести», sense 4, https://gramota.ru/meta/vynesti, explicitly gives presenting a question for discussion. All five selected EN senses remain.
- 収穫: Kuznetsov «плод», sense 4, https://gramota.ru/meta/plod, explicitly includes «плод усилий» and the result of earlier activity. The nonmonetary productive-trip explanation remains.
- 参考: Digital Daijisen, https://kotobank.jp/word/参考-513340, explicitly covers both consulting others' opinions/materials and the materials used for that purpose. This supports «справочный материал», not merely the act. Kuznetsov «образец», sense 2 and «брать за образец», https://gramota.ru/meta/obrazets, and «справочный», senses 2–3, https://gramota.ru/meta/spravochnyy, support the RU wording. The card expressly denies compulsory exact copying/agreement.
- 原: Kuznetsov entries https://gramota.ru/meta/lug, https://gramota.ru/meta/ravnina, https://gramota.ru/meta/pustosh and https://gramota.ru/meta/stepstep_5189 distinguish grassy land, a broadly level area, uncultivated/abandoned/uninhabited ground, and dry-climate grassland. The card makes these contextual alternatives, not interchangeable ecosystems. Both «равнина» example translations fit the supplied Japanese; the second retains traversed-space を. JMdict 野's field/plain sense supports the RU guard.
- 博物館: Kuznetsov «музей», sense 1, https://gramota.ru/meta/muzey, explicitly includes art collections and «музей изобразительных искусств», supporting the Russian umbrella term and the 美術館 guard.
- 博士: Kuznetsov «доктор», senses 1–2, https://gramota.ru/meta/doktor, separates physician and degree/holder. The はかせ/はくし distinction remains.
- 双子: actual dictionary results https://gramota.ru/poisk?query=однояйцевой&mode=slovari give both «однояйцовый и однояйцевой» and the one-fertilized-egg definition; https://ru.wiktionary.org/wiki/однояйцовый agrees. «Однояйцевые» legitimately renders biological “identical”.
- 単に/単なる: Kuznetsov «просто», https://gramota.ru/meta/prosto, distinguishes ease, restrictive «всего лишь» and other functions. The teaching contrast is supported; it is not an exhaustive taxonomy of Russian просто. JMdict rentaishi classification supports «перед существительным» and the no-extra-な rule. Added 単なる–単に guard is conservative for overlapping bare Russian meanings, not a claim of identical Japanese syntax.
- 医療: Babenko «медицина», https://gramota.ru/meta/meditsina, expressly includes scientific knowledge and practical health-preserving activity; the localized contrast is sound.
- 医師: Kuznetsov «официальный», https://gramota.ru/meta/ofitsialnyy, includes language characteristic of official documents/business papers. The actual Nipponica 医師 entry, https://kotobank.jp/word/医師-431904, identifies the legally regulated professional name and contrasts colloquial 医者. Read as the stated register cue, not an exclusive-use prohibition, «официальный термин» is supported.
- 化粧: Kuznetsov «макияж», senses 1–2, https://gramota.ru/meta/makiyazh, and «плотный», https://gramota.ru/meta/plotnyy, support cosmetics application and density. «Плотный макияж» contextually renders heavy makeup; exact collocation frequency was not established.
- Added guards 及ぼす–影響 and 原–野 are supported by the actual JMdict influence/effect and open-field/plain senses respectively; 博物館–美術館 by the Russian museum umbrella above. This is not a full distractor-corpus audit.

Optional: None.

Limits:
L1; verification limitation, NOT an established mistranslation; words/単位.md:4,15,18,20,34. JMdict sense 3 and https://en.wiktionary.org/wiki/credit senses 14–15 confirm academic credits. The actual Russian encyclopedia entry https://ru.wikipedia.org/wiki/Зачётная_единица_трудоёмкости supports the term and workload/grade distinction. However, the requested exact Russian dictionary entry for «зачётная единица» was not located: Gramota returned no exact entry, Russian Wiktionary compound requests returned 404, and Russian «кредит» lacked that sense. An encyclopedia is not the requested dictionary evidence. Inspect an appropriate exact dictionary entry to close this limit; current evidence does not justify replacing the translation.
No native-speaker, device, publication, archive, historical or frequency certification. Oversized initial output was replaced by complete bounded three-pair reads. Failed dictionary requests (404/429/403) were not treated as evidence.

Read-only validation: python -X utf8 -B tools\validate.py: “0 error(s)”, exit 0. Example/link comparisons passed. No generators or Git writes. Only this report written.
