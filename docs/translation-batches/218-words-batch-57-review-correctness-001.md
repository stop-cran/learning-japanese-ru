# B218 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `4cc28f4411ca8c4cc1d94c5a7cfc02e25752f746` (tree `b193110e748f6063dcdcc5a24c49e17bffecd066`),
> the signed candidate pushed before review.
> Later reconciliation is in `218-words-batch-57-recheck-001.md`.

Snapshot: RU signed candidate 4cc28f4411ca8c4cc1d94c5a7cfc02e25752f746, compared with parent 6591e0e020f045a152d2a15eb0a52795da704555. HEAD matched; working tree clean initially and after review. No uncommitted changes included. Frozen EN HEAD confirmed as 6af98cb717755690a9ca793e5454a96ebd7a8f9f.

Scope: Blind, read-only CORRECTNESS and SCOPED COVERAGE review. Reviewer model is not independently verifiable from the available execution context. No delegation. Each of the following RU files AND its frozen EN original was returned and read IN FULL:

- words/倒す.md
- words/修理.md
- words/修正.md
- words/信じる.md
- words/信用.md
- words/信頼.md
- words/保証.md
- words/価値.md
- words/例え.md
- words/作物.md
- words/作法.md
- words/作曲.md
- words/作品.md
- words/余分.md
- words/何時か.md
- words/何とか.md
- words/何でも.md
- words/何で.md
- words/体育.md
- words/住民.md
- words/住宅.md
- words/伝統.md
- words/会員.md
- words/休暇.md
- words/休憩.md
- words/企業.md
- words/任せる.md
- words/仲間.md
- words/仲.md
- words/以来.md

Binding instructions were read completely. Existing RU 勝つ, 直す, 礼儀, 曲, 自宅, 夏休み, 昼休み and 同僚 were read fully; other suggested comparisons at title/guard level only. Existing runtime integration changes were inspected as a bounded diff. No forbidden reports, batch/draft/tracking records or scratch checkout were read.

Verdicts: correctness CLEAN for all 30; scoped coverage NEEDS FIX for words/余分.md (F1), CLEAN for the other 29. Comprehensibility/quiz safety are outside scope. CLEAN is bounded, not exhaustive.

Findings:

F1; Minor; scoped coverage / exact Japanese-source preservation; words/余分.md:24.
The source's reading join よ + ぶん became ヨ + ブン. These have the same sound; RU correctly calls them on readings. This is NOT a linguistic reading error, but violates the assignment's explicit script-preservation requirement.
Remedy: replace the final sentence with exactly: «Онные чтения складываются как よ + ぶん.»
Evidence: frozen EN words/余分.md:29: “The on readings combine as よ + ぶん.”; RU line 24; assignment's script-preservation rule. [Jisho/JMdict 余分](https://jisho.org/search/余分), entry 1544520, confirms よぶん, noun / na-adjective, “extra; excess; surplus”. The defect concerns source preservation, not pronunciation.
Confidence: high. Status: unresolved.

Evidence and checks:

- All 30 full working-tree reads matched candidate Git blobs after newline normalization. All EN Japanese example sentences remain present, ignoring Markdown/translation wrappers; inline forms/explanations were also read manually.
- Source IDs, readings, levels, types, kanji lists, tags, exclusions and dictionary references are retained. Seven guards are added: 倒す–勝つ, 修正–直す, 作法–礼儀, 作品–曲, 住宅–自宅, 休暇–夏休み, 休憩–昼休み. All EN links with available RU targets survive; every new card has a manifest entry. Read-only `python -X utf8 -B tools\validate.py`: `0 error(s)`. No generator ran.
- Live Jisho/JMdict entries for ALL 30 were inspected for spelling/readings, senses, POS and restrictions, excluding Wikipedia objects: `https://jisho.org/api/v1/search/words?keyword=<headword>`.
- Particularly: [保証](https://jisho.org/search/保証) allows 保障 in the general assurance entry but restricts warranty to 保証; [作法](https://jisho.org/search/作法) restricts etiquette to さほう; [例え](https://jisho.org/search/例え) has spelling preferences (“esp.”), not absolute sense restrictions; [仲間](https://jisho.org/search/仲間) includes colleague and the group/category senses; [以来](https://jisho.org/search/以来) includes suffixal and standalone adverbial use. These distinctions survive translation.
- [大辞泉 勝つ](https://kotobank.jp/word/勝つ-464050), sense 1, shows competition with に; [大辞泉 直す](https://kotobank.jp/word/直す-587499), 1イ/2イ, distinguishes repair/correction with を examples. JMdict's intransitive 勝つ and transitive 直す/倒す support the added contrasts.
- [なんで, actual usage notes](https://en.wiktionary.org/wiki/なんで#Usage_notes) explicitly describes chiefly informal language compatible with polite endings; this supports the new «разг.» title qualifier without treating the polite example as contradictory. [大辞泉 何で](https://kotobank.jp/word/何で-590616) and JMdict were inspected separately.
- Every main example was checked for polarity, aspect/event stage, voice and roles. Russian masculine first-person forms / «мой друг» select possible contexts, not a claim that 私/友達 encodes male sex. 姉/彼女 remain female. «Коллегами» correctly translates 仕事の仲間, supported by its coworker sense; it does not equate every 仲間 with 同僚.

Russian evidence (actual entry bodies/senses):

- [Вверить](https://gramota.ru/meta/vverit), Kuznetsov: “отдать в чьё-либо распоряжение, поручить чьим-либо заботам; доверить”; [вверять](https://gramota.ru/poisk?query=вверять&mode=slovari) points to this entry. [Усмотрение](https://gramota.ru/meta/usmotrenie): conclusion/opinion/decision. Supports 任せる's title and discretion explanation.
- [Антракт](https://gramota.ru/poisk?query=антракт&mode=slovari), Kuznetsov sense 1: interval between acts/concert sections; conversational extension to a break in activity. The title corresponds to EN “intermission”, not a new musical-work sense.
- [Излишек](https://gramota.ru/meta/izlishek), Kuznetsov sense 1: what remains beyond the required amount; [лишний](https://gramota.ru/meta/lishniy), senses 1–3, includes extra/additional as well as unnecessary. Thus a useful spare onigiri is not contradicted by the RU example.
- [Творение](https://gramota.ru/meta/tvorenie), Kuznetsov sense 1: creative product, marked elevated; it does not require a famous professional. [Работа](https://gramota.ru/meta/rabota), senses 2/4/5/6, supports the employment/task/created-work distinction. The latter is a legitimate Russian adaptation, not a surviving English-only pun.
- [Товарищ](https://gramota.ru/meta/tovarishch), Kuznetsov senses 1–2: friend or person linked by occupation/activity; [компания](https://gramota.ru/meta/kompaniya), senses 1–2, distinguishes a social group from a business. [Взаимоотношения](https://gramota.ru/meta/vzaimootnosheniya): relations between people/things; the title's “между людьми” supplies 仲's narrower domain.
- [Креди́т](https://gramota.ru/poisk?query=кредит&mode=slovari&dicts[]=42), Kuznetsov senses 1–2: lending/deferred payment and commercial trust/creditworthiness. The separate accounting homonym кре́дит was NOT used as evidence. [Доверие](https://gramota.ru/meta/doverie) and [уверенность](https://gramota.ru/meta/uverennost), sense 1, support the trust/reliability wording without a feelings-versus-finance partition.
- [Кое-как](https://gramota.ru/meta/koe-kak), Kuznetsov sense 1: “с большим трудом, еле-еле”; sense 2 separately means carelessly/badly. In «кое-как успел вовремя», the first sense fits. No careless-action error established.
- [Пример](https://gramota.ru/meta/primer), Kuznetsov sense 1, supports an explanatory instance; [сравнение](https://gramota.ru/meta/sravnenie), sense 2, supports figurative comparison. [Сочинение](https://gramota.ru/meta/sochinenie), senses 1–3, supports the adapted 作曲/作文 comparison.
- [Культура](https://gramota.ru/meta/kultura), sense 7, supports cultivated plant varieties; the 作物 body separately retains agricultural produce. [Этикет](https://gramota.ru/meta/etiket) supports 作法. [Физкультура](https://gramota.ru/meta/fizkultura) and culture's physical-education subentry support 体育 without equating it to a building or one sport.
- [Житель](https://gramota.ru/meta/zhitel) denotes an inhabitant; [жильё](https://gramota.ru/meta/zhile), sense 2, and [жилой](https://gramota.ru/meta/zhiloy) concern dwelling/residential use. The 住宅 contrast is accurate, though its rejected gloss was not offered as a RU headword translation. [Член](https://gramota.ru/meta/chlen), sense 4, supports association/group membership. [Отпуск](https://gramota.ru/meta/otpusk), sense 2, covers release from duties for rest OR other purposes, not only a paid annual trip. [Перерыв](https://gramota.ru/meta/pereryv), sense 3, supports 休憩.
- [Впредь](https://gramota.ru/meta/vpred) means future time. The 以来 warning preserves the Japanese past-anchor rule; its quoted “dictionary translation” is an adaptation of EN “henceforth”, not a Russian gloss actually offered by this card.

Optional:

- Nonblocking: mark «творение» elevated; consider «стали хорошо ладить» alongside «подружились» in 仲. [仲良く](https://kotobank.jp/word/仲良く-588196) describes good/amicable terms; [подружиться](https://gramota.ru/meta/podruzhitsya) establishes friendship. The contextual example remains possible, not an established mistranslation.
- 以来:33 could state the past-anchor rule without warning against an unseen Russian “dictionary translation”. 住宅's resident/dwelling contrast remains useful through 住民; no need to restore the English-only source-list warning.
- Outside facets: navigation gaps observed at 住宅:29→住民, 自宅:32→住宅, 昼休み:31→休憩. Not a complete reciprocal-link audit.
- Outside facets: quiz leads 住民–人口 («население») and 仲間–友達 («друг») lack direct guards in displayed fields despite dictionary sense overlap. Refer to quiz reviewer for actual-pool adjudication; these are not counted as in-facet findings.

Limits: No native-speaker, app/device, archive or complete quiz-pool certification. Live dictionaries, not historical reconstructions. Initial Gramota HTTP 429s were resolved through successful actual entries above. Oversized first reads were not counted; all 30 pairs were subsequently returned completely in bounded reads. No consequential linguistic claim remains unresolved in scope. Only this report was intentionally written; no generators, repository edits, staging, commits, pushes or branch/checkout operations.

Summary: correctness CLEAN; scoped coverage NEEDS FIX. Findings by severity: Critical 0; Major 0; Minor 1. F1: restore source hiragana よ + ぶん in words/余分.md:24.
