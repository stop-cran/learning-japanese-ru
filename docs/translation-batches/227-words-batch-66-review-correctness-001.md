# B227 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5cf2313776672567fd1454fffd027b253bb10278` (tree `b8e291d86716374cd700fba67aaccfa3900d3caf`),
> the signed candidate pushed before review.
> Later reconciliation is in `227-words-batch-66-recheck-001.md`.

Snapshot: RU 5cf2313776672567fd1454fffd027b253bb10278, compared with parent 0d431aa0a52bac3d31a6b62334c4613807e70867 and frozen EN 6af98cb. HEAD confirmed; initial and final git status --porcelain empty. No uncommitted content included.

Scope: Blind correctness/scoped-coverage review. Model not independently verifiable; no delegation.
Every following RU file AND its corresponding frozen EN original was read IN FULL:
words/突く.md; words/突き当たる.md; words/突っ込む.md; words/飛び込む.md; words/風船.md; words/風呂敷.md; words/顕微鏡.md; words/区切る.md; words/境界.md; words/区域.md; words/区分.md; words/項目.md; words/題名.md; words/頼もしい.md; words/頭脳.md; words/受け取り.md; words/コレクション.md; words/集金.md; words/領収.md; words/領事.md; words/預かる.md; words/順序.md; words/順々.md; words/頂点.md; words/雑音.md; words/感想.md; words/響き.md; words/伝わる.md; words/響く.md; words/時間割.md.
Also read RU cards 入る, 引き出す, 決まり, 印象, 脳, 預ける; link-only diffs in kanji/区.md, kanji/域.md, words/句読点.md, words/意見.md, words/預ける.md; and binding references. No prohibited reports/records read.

Verdicts:
- Correctness NEEDS FIX: 飛び込む (C1), 突っ込む (C2), 区切る (C3). Other 27 cards CLEAN within this scope.
- Scoped coverage NEEDS FIX: 飛び込む (C1), 区切る (C3), where source qualifications have weakened/disappeared. Other 28 cards CLEAN within this scope.
- Comprehensibility and full quiz/manifest integration: outside assigned facets.

Findings:

C1; Minor; correctness/scoped coverage; words/飛び込む.md:34.
Claim/impact: 入る is described as entering “без порыва или прыжка”. EN says “without requiring a rush or leap”: the broader verb does not specify those manners, rather than excluding them. The RU wording can teach a false incompatibility with hurried/jumping entry. This is a lost qualification, not an incorrect Japanese example.
Remedy: replace the sentence with “[入る](入る.md)（はいる）значит «входить» в более широком смысле: само слово не указывает, происходит ли вход с разбега или прыжком.”
Evidence: frozen EN words/飛び込む.md, corresponding contrast; Digital Daijisen https://www.weblio.jp/content/入る, actual はい・る【入る／這入る】 sense 1, moving from outside into a bounded space, without a manner restriction (not the separate いる heading). Compare https://www.weblio.jp/content/飛び込む, senses 1 and 3, entry with momentum/leap or hurried entry.
Confidence: high on the omitted qualification; medium-high on the misleading categorical reading.

C2; Minor; correctness; words/突っ込む.md:43.
Claim/impact: “Основные значения — «ринуться, врезаться во что-то» и «углубиться во что-то»; остальные употребления...” promotes a particular EN source-gloss selection into a general main-versus-other hierarchy. Physical insertion, introduced first in the title, explanation and pocket example, is thereby demoted without supporting evidence. The source annotation may be removed; it should not become an unsupported lexical ranking.
Remedy: delete this sentence. The preceding sentence already distinguishes the three constructions, and the following dictionary reference retains the evidence. Alternatively describe what this card teaches without ranking dictionary meanings.
Evidence: frozen EN closing note explicitly concerns “The selected N2 source gloss”, not general lexical primacy. Official JMdict English XML https://www.edrdg.org/pub/Nihongo/JMdict_e.gz, entry 1456940: sense 1 thrust/cram/stuff/shove into; sense 2 plunge/charge/rush/crash into; sense 3 delve/go into depth; senses 4–6 probing, meddling and retorting. These definitions supply no main/additional frequency hierarchy. Digital Daijisen https://www.weblio.jp/content/突っ込む also explicitly includes insertion, including a hand in a pocket.
Confidence: high.

C3; Minor; correctness/scoped coverage; words/区切る.md:26.
Claim/impact: EN's explicitly app-local grouping (“The app groups this on-first mixed form under kango”) becomes “относят к канго — словам китайского происхождения”. This removes the framework qualification and adds a blanket origin definition. It invites the learner to infer Chinese origin for this mixed form, despite the sentence's own final disclaimer about historical formation. Kango also includes words coined in Japan; it is not simply a guarantee of Chinese provenance.
Remedy: replace the paragraph with “В приложении эта смешанная форма с онным началом условно отнесена к канго: ク — онное чтение, а озвончённый элемент ぎる связан с исконным 切る（きる）. Это современное объяснение чтения, а не сложение из одних онных чтений и не утверждение о том, как слово сложилось исторически.”
Evidence: frozen EN words/区切る.md:27; Digital Daijisen https://www.weblio.jp/content/漢語, かん‐ご【漢語】 sense 1, explicitly includes both vocabulary transmitted from China and words created in Japan. The same source https://www.weblio.jp/content/区切る has く‐ぎる【句切る／区切る】; the mixed reading and the source's app-specific grouping are distinct issues. No metadata reclassification is requested.
Confidence: high.

Optional:
- More explicit title coverage would help 時間割 (“расписание; расписание занятий”) and 響き (add “впечатление от звучания”). Their bodies retain the broader timetable and impression senses; no Japanese construction or example is lost there. Likewise 雑音's figurative sense remains explicit in the body and its second example, as in EN; I do not require every additional sense in every short title.
- 集金's “собирать счета или взносы” could be smoother as “получать оплату по счетам или собирать взносы”, avoiding a possible image of collecting paper bills. The surrounding payment explanation is already clear.

Evidence and retained-scope checks:
- Inspected actual Jisho entries for all 30 word families. Subsequently streamed the official JMdict English XML in memory: all 49 distinct numeric IDs cited in the cards' source footers were present, including comparison/document entries. Checked the relevant definitions and spelling annotations, rather than treating entry existence as proof of usage. In particular 句切る is rare; 頼母しい is search-only; bare 響 has irregular okurigana; 風船's aerostat sense is dated. These are not new recommended everyday spellings/senses.
- Inspected separate Daijisen コレクション【collection】 and 【correction】 entries at https://www.weblio.jp/content/コレクション: the latter defines 修正・訂正. The preceding English-expression dictionary was not used as verification. Also inspected Daijisen 頭脳, 領収, 時間割, 響き and 受取, distinguishing ひびき from どよめき and the timetable noun from the novel.
- Russian lexical checks used actual Kuznetsov/Gramota entries and, where unavailable, actual Wiktionary definitions/attestations. Examples: https://gramota.ru/poisk?query=расписка&mode=slovari documents a signed acknowledgment of receipt; https://gramota.ru/poisk?query=апогей&mode=slovari labels the figurative peak bookish; https://ru.wiktionary.org/wiki/мозговой_центр explicitly includes an individual specialist, not only a think tank; https://ru.wiktionary.org/wiki/фуросики gives the wrapping cloth with literary attestations. Thus neither the person metaphor nor the cloth term warrants a correction merely because one dictionary search lacks it.
- Also inspected definitions for вникать, размечать, разгородить, аэростат, графа, рубрика, поочерёдно, пересуды, пихать, помеха, порядок, квитанция, граница and предел. Kuznetsov supports порядок's orderly-state/rules versus sequence senses. The граница/предел contrast distinguishes senses, not permitted Russian words. The document/action contrast does not exclude electronic receipts.
- Warm-voice/warm-words usage is explicitly supported by Kuznetsov's тёплый, figurative sense 5, at https://gramota.ru/poisk?query=тёплый&mode=slovari. Russian acoustic “warm sound” is also attested in the introduction to https://ru.wikipedia.org/wiki/Ламповый_звук. This supports the ordinary metaphor, not a claim that the exact string “тёплое звучание” is a fixed idiom or a measured frequency claim.
- Japanese examples/readings and the constructions, polarity, argument roles and qualifications were compared throughout the full reads. Contextual Russian masculine past forms do not assert that Japanese grammatically marks the speaker male; 本 does not require singular; a dive need not be head-first. The くる viewpoint, する/non-する distinctions, mixed readings and godan/ichidan warnings remain explicit. No additional RU-only full Japanese sentence lacking its reading line was established.
- Front matter preserved except the added direct 順序→決まり exclusion; the latter's existing RU title “правило; установленный порядок” supports that conservative ambiguity guard. No dropped EN link whose RU target exists was found. The new 突っ込む→引き出す link retains the physical-only reverse-action qualification. Missing RU targets left as plain text were not counted as defects.
- Read-only validation: python -X utf8 -B tools\validate.py returned 0 error(s). No generator was run; repository HEAD, index and working tree remained unchanged.

Limits: Bounded editorial review, not native-speaker certification, historical reconstruction, corpus-frequency measurement or a full quiz audit. Dictionary recognition does not certify every invented example; no consequential example defect was established beyond C1–C3. Initial rate limits were resolved. Oversized outputs were not counted as full reads; bounded subsequent calls supplied every complete pair. Exact “тёплое звучание” frequency was not established; ordinary metaphor is narrower evidence. Only this report was written; no fixes made.
