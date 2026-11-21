# B223 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `13805217f9159dadc5849e7e0060bfbc1d2ffc4a` (tree `4ad1f061cda9d497acf9fc7d5c8b5856d91b254b`),
> the signed candidate pushed before review.
> Later reconciliation is in `223-words-batch-62-recheck-001.md`.

Snapshot: RU 13805217f9159dadc5849e7e0060bfbc1d2ffc4a, parent 8a759e5a7131ef4d06581fae6ac0d8471ba50e2c; frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f. HEAD verified before/after; git status --porcelain empty both times. Repository/index unchanged; only this report written.

Scope: BLIND read-only CORRECTNESS and SCOPED COVERAGE. Actual model not independently verifiable. Each following RU file AND complete frozen EN original read in full (metadata, sections, examples, readings, citations):
words/アイスクリーム.md; words/クリーム.md; words/クリスマス.md;
words/クラシック.md; words/キャンプ.md; words/キャプテン.md;
words/オーバー.md; words/エネルギー.md; words/ウイスキー.md;
words/インク.md; words/アルバム.md; words/アウト.md;
words/アイロン.md; words/わざと.md; words/やや.md;
words/だけど.md; words/ところが.md; words/なぜなら.md;
words/だって.md; words/だが.md; words/もっとも.md;
words/もしも.md; words/まるで.md; words/まさに.md;
words/まさか.md; words/まあ.md; words/きちんと.md;
words/そっくり.md; words/くっつく.md; words/くっつける.md.

Also read the three binding RU instruction/reference files, the complete RU comparison targets あ, ああ, 活気, ちょうど, もうすぐ, 結婚 and テント, and the changed passages in ざっと, ふと, ワイン, 万一, 思わず and 流れる. Other suggested comparison cards were not read in full; no whole-pool quiz-safety verdict is made. Prohibited author/reviewer/batch/tracking material and scratch worktrees were not consulted.

Verdicts:
- Correctness: NEEDS FIX (C2; title qualifier in C3a). キャンプ's unqualified Russian activity equivalence remains UNVERIFIED (U1). Other assigned cards: CLEAN within the examined correctness scope.
- Scoped coverage: NEEDS FIX (C1 and C3). For キャンプ, the Japanese activity/place coverage is present, but equivalence of the Russian activity label is UNVERIFIED (U1). Other assigned cards: CLEAN within the examined coverage scope.
- Russian comprehensibility and whole-pool quiz safety are outside the assigned facets, not certified.

Findings:

C1; Minor; scoped coverage; words/アイロン.md:17–19.
EN's シャツにアイロンをかけました。 is replaced by シャツにアイロンをかける: the construction survives, but the required verbatim example and its past/completed translation do not. Moving an unchanged example into prose would be acceptable.
Remedy: restore “- シャツにアイロンをかけました。（シャツにアイロンをかけました。）— Я погладил рубашку.” before the remaining bullet, then remove the redundant dictionary-form illustration if desired.
Evidence: frozen EN words/アイロン.md:20; RU:19; https://jisho.org/word/アイロン (JMdict 1014590 sense 1). The RU phrase is grammatical, but not source-identical.
Confidence: high.

C2; Minor; correctness; words/アイスクリーム.md:28.
“само по себе это слово не называет замороженный десерт” presents a categorical lexical exclusion for クリーム. The new comparison card itself correctly explains that クリーム also abbreviates アイスクリーム. The unqualified exclusion can teach the learner to reject a recorded meaning. This defect is inherited from EN; inheritance does not reconcile the contradiction.
Remedy: replace the final sentence with “[クリーム](クリーム.md) обычно означает сливки или крем; словарь отмечает и сокращённое значение «мороженое», но без помогающего контекста полное アイスクリーム яснее.”
Evidence: actual JMdict 1044480 sense 2 is “ice cream”, tagged Abbreviation, see-also アイスクリーム: https://jisho.org/word/クリーム and https://jisho.org/api/v1/search/words?keyword=クリーム. Compare RU words/クリーム.md:33. This evidence supports recognition, not a frequency ranking.
Confidence: high.

C3; Minor; scoped coverage (and correctness for the restrictive qualifier in a); words/もっとも.md:4,12; words/まるで.md:4,12; words/だって.md:4,12.
Three short titles prune source-title scope although the bodies retain most of the teaching:
a. “разумный (о доводе)” restricts もっとも below its own もっともな質問 and もっともな意見 examples. A question is not necessarily a довод. Use “разумный; обоснованный; впрочем”, or another qualification that does not restrict it to arguments.
b. “словно; совсем не” omits EN title's affirmative “completely”. RU:21 still teaches the positive predicate 違う, but its Russian “не так” rendering further hides that grammatical point. Use “словно; совершенно; совсем не”; “Совершенно отличается от того, что было раньше” is an available rendering at line 21.
c. “потому что (оправдываясь); даже; тоже” omits EN title's independent adversative “but”, which RU:19 correctly uses as “Но”. Use “потому что (оправдываясь); но; даже; тоже”.
Evidence: frozen EN front-matter titles, line 4 in each file; actual JMdict 1535810 sense 2 (“reasonable, natural, just”), 1216280 sense 3 (“really, completely, entirely…”), and 2643970 sense 2 (“but”): https://jisho.org/word/尤も ; https://jisho.org/word/丸で ; https://jisho.org/word/だって .
For a, Kuznetsov разумный sense 3 is “Основанный на разуме, оправдываемый здравым смыслом”; довод is specifically an argument advanced in proof: https://gramota.ru/poisk?query=разумный&mode=slovari and https://gramota.ru/poisk?query=довод&mode=slovari .
Confidence: high for omissions; medium-high for “о доводе”.

U1; Minor, unresolved evidence qualification; correctness/scoped coverage UNVERIFIED; words/キャンプ.md:4,15,18,24,32.
The card equates the activity “отдых в таком лагере” with Russian кемпинг and repeatedly translates going camping as going to a кемпинг. Inspected Russian dictionaries define кемпинг more narrowly as an equipped camp for motor tourists, whereas Japanese キャンプ sense 1 includes both camp and camping. “лагерь на природе” preserves the place sense, but does not independently establish the Russian activity equation. This is not proof that contemporary broader usage is impossible.
Remedy: either supply inspectable established evidence for the broader activity use, or make the activity explicit: title “отдых в лагере на природе; лагерь на природе”; キャンプに行く “поехать отдыхать в лагерь на природе”; second example “Я собираюсь с друзьями отдыхать в лагере на природе.” Explain кемпинг only as a possible kind of site, not a required facility.
Evidence: https://jisho.org/word/キャンプ (JMdict 1042200 sense 1, noun/intransitive suru); Kuznetsov and Krysin entries at https://gramota.ru/poisk?query=кемпинг&mode=slovari ; https://ru.wiktionary.org/wiki/кемпинг (sense 1 also specifies motor-tourist facilities). Kuznetsov лагерь sense 2 supports the broader alternative: https://gramota.ru/poisk?query=лагерь&mode=slovari .
A broader RIA tourism usage appeared in search, but the actual fetch failed; summary alone is not verification.
Confidence: high concerning the inspected dictionary definitions; broader modern activity use remains unverified, not rejected.

Evidence and completed checks:
- Actual Jisho/JMdict sense families inspected for all 30; all 30 exact word pages independently fetched and cited IDs matched. 尤も was distinguished from 最も. Full spelling Notes verified for 態と, 稍/漸, 尤も, 若しも, 丸で and 真逆, including rare-form/ateji labels. まあ's female-language label is attached to exclamatory sense 4 only.
- All six RU-only links checked against actual articles/dictionary meanings: クリーム→アイスクリーム, エネルギー→活気, まさに→ちょうど/もうすぐ, まあ→あ, くっつける→結婚. No unsupported substitution ban established. あ is interjection 2394370, not 亜 (https://jisho.org/search/あ%20%23words). 活気 is liveliness, not physical/caloric energy; もうすぐ's proximity contrasts appropriately with immediate-stage まさに…としている. Matchmaking sense 3 of くっつける is colloquial.
- Actual Gramota/Kuznetsov entries inspected for food, captain, overcoat/limit, energy/reserve, sports, connective, degree and manner glosses, including the specifically requested lemmas; lookup URL: https://gramota.ru/poisk?query=<lemma>&mode=slovari .
- https://gramota.ru/meta/polno sense 2 gives conversational “Довольно, хватит, пора прекратить”, with “Полно сидеть, повесив нос!”: calming полно is attested, not automatically obsolete. Поскольку explicitly means “так как, потому что”; впрочем I introduces qualification. Вплотную means extremely close/touching; придвинуть includes “П. стол вплотную к окну”. Держаться sense 5 supports maintaining position; запас sense 2 supports an available reserve.
- Metadata comparison found source word/reading/JLPT/type/kanji/tags unchanged; original exclusions retained. Existing-target EN links retained; missing-target links became plain text. Restored テント→キャンプ remains coherent. Apart from C1, no changed Japanese example/reading or lost body teaching point established. オーバー retains おーばー. English-only contrast/pronunciation/community-source wording was not mechanically required.
- Read-only validator: python -X utf8 -B ...\learning-japanese-ru\tools\validate.py → “0 error(s)”, exit 0. No generator run.

Optional: Outside assigned facets: キャプテン:15 “Полезная обстановка для этого слова” is an awkward calque; “Типичный контекст — спортивная команда” would read more naturally. No separate correctness defect claimed.

Limits: U1 unresolved. No native-speaker, frequency or full quiz-pool certification. Initial Gramota 429s and oversized ancillary dictionary/diff outputs were followed by successful bounded reads. Complete card-pair outputs were returned. No author reports consulted. Validation is structural, not semantic.
