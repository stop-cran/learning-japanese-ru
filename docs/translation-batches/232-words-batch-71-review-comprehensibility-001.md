# B232 comprehensibility and scoped-coverage review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `grok-4.7`
> (Grok family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `56da736ec2499c2e67dc01cd65078098c31e2716` (tree `e27c0b79e91de862b493efe3dffbc9683aa33060`),
> the signed candidate pushed before review.
> Later reconciliation is in `232-words-batch-71-recheck-001.md`.

Snapshot: `56da736ec2499c2e67dc01cd65078098c31e2716` (branch `full-ru-232-words-71`). `git rev-parse HEAD` matches. `git status --porcelain` is empty. No uncommitted changes. Parent `c82c004`. Frozen EN source `6af98cb`.
Scope: comprehensibility and scoped coverage only. All 30 new cards read in full: `words/部首.md`, `原料.md`, `成分.md`, `部品.md`, `郡.md`, `裏返す.md`, `お帰り.md`, `返る.md`, `遡る.md`, `遠足.md`, `対策.md`, `方角.md`, `方針.md`, `地帯.md`, `角度.md`, `方面.md`, `道順.md`, `過失.md`, `過半数.md`, `余る.md`, `超過.md`, `過剰.md`, `遊園地.md`, `逸れる.md`, `統一.md`, `連合.md`, `作製.md`, `作成.md`, `製作.md`, `造船.md`. EN originals compared for titles, examples and the named contrasts. Link-only diffs in `kanji/余.md`, `kanji/帯.md` and `words/余分.md` only add links to the new cards. Model: not verifiable from this assignment.
Verdicts: Comprehensibility NEEDS FIX. Scoped coverage NEEDS FIX for `words/成分.md` only; the other 29 articles are CLEAN within these facets.
Findings:

C1. Minor; comprehensibility; `words/角度.md:4,12,37-38`. Title and H1 `величина угла (в градусах)` restrict the measure to degrees. The card's own note says degrees are only one unit, and Digital Daijisen sense 1 is the size of the angle, with units radian, degree, minute and second (https://kotobank.jp/word/角度-460585). A learner can reject a radian answer. Remedy: in the title and the H1, replace the first gloss with `величина угла` (drop `(в градусах)`). Evidence: Daijisen sense 1 and lines 37-38. Confidence: high.

C2. Minor; comprehensibility; `words/方面.md:4,12`. The lead gloss `в сторону (какого-либо места)` is a prepositional phrase, not a noun answer. The comma then exposes bare `сфера`, which is the lead title of `words/球.md` (`сфера; мяч`). EN title is "direction; area; field". Remedy, title and H1: `направление (к месту); область деятельности`. The parenthetical keeps the distinction from `words/方向.md` (`направление; курс`); do not use bare `сфера`. Evidence: title rule (short gloss usable as an answer, not a phrase); title screen segment match `сфера` against `球`; `球` is already in `quiz_exclusions`. Confidence: high.

C3. Minor; comprehensibility; `words/道順.md:4,12`. Lead gloss `как пройти (куда-либо)` is a clause. EN title is "route; directions". The second gloss `маршрут (по улицам)` is already a usable noun and is qualified against `words/コース.md`. Remedy, title and H1: `маршрут (по улицам); объяснение пути`. Evidence: content-structure title rule; EN title. Confidence: high.

C4. Minor; comprehensibility; `words/遡る.md:4,12`. Parenthetical `вести отсчёт назад` reads as counting backwards, not as tracing history. The body and the Edo example already teach the past sense (`восходит к эпохе Эдо`). EN title is "go upstream; trace back". Remedy, title and H1: `подниматься вверх по течению; восходить к прошлому`. Evidence: the parenthetical versus line 20 and EN "dates back". Confidence: high.

C5. Minor; comprehensibility; `words/作製.md:20`. `Мы готовим чертёж новой детали` uses `words/作る.md`'s second title gloss `готовить` and blurs `準備` for progressive `作製しています`. EN: "We are producing a design drawing for the new part." Remedy: `Мы изготавливаем чертёж новой детали.` Evidence: `作る` title `делать; готовить`; EN example. Confidence: high.

C6. Minor; comprehensibility; `words/原料.md:20`. `Эту бумагу делают из древесины` drops the role the card has just taught (`Nを原料にする`). EN: "This paper uses wood as its raw material." Remedy: `Для этой бумаги сырьём служит древесина.` Evidence: lines 17-18 and the EN example. Confidence: high.

C7. Minor; comprehensibility and scoped coverage; `words/成分.md:20,31-36`. `Я изучил состав продукта` uses the lead title of `words/構成.md` (`состав; компоновка (частей целого)`). The synonym section contrasts `材料`, `原料`, `要素` and `部分`, but never `構成`, although `構成` is in `quiz_exclusions` and this pair is a named risk. Digital Daijisen sense 1 is the elements or pure substances that make up a compound or mixture, not the composition of the whole (https://www.weblio.jp/content/成分). Remedy: translate the example as `Я изучил компоненты продукта.` Add after the `部分` sentence: `[構成](構成.md)（こうせい）— состав или компоновка целого, а не один компонент.` Evidence: `構成` title and reading `こうせい`; Daijisen sense 1; EN "composition" is not another EN card's quiz label, so this collision is created in Russian. Confidence: high.

C8. Minor; comprehensibility; `words/部品.md:4,12,39`. Unqualified second gloss `запчасть` means a spare part (Wiktionary: colloquial shortening of запасная часть). Digital Daijisen defines `部品` as short for `部分品`, a component of a machine or appliance (https://www.weblio.jp/content/部分品). Line 39 already says replacement is only one convenient scene. EN title is "parts; components; accessories", not spares. Remedy, title and H1: `деталь (механизма, устройства); комплектующая`. Evidence: Daijisen `部分品`; line 39. Confidence: high.

C9. Minor; comprehensibility; `words/超過.md:4,12`. `перерасход` is extra spending or an overspent sum (Ozhegov: перерасходованная сумма; Ushakov sense 1 is financial). Jisho/JMdict 1429410 is exceeding a limit or estimate. The card's examples are a time limit and excess weight, not expenditure. Remedy, title and H1: `превышение (лимита, нормы)`. Evidence: https://jisho.org/word/超過; Ozhegov via https://gufo.me/dict/ozhegov/перерасход. Confidence: high.

C10. Minor; comprehensibility; `words/超過.md:49`. `Метка N2 взята из закреплённого списка слов сообщества.` is an author-facing provenance note, and Latin `N2` is not a dictionary name or a source footer about the word. It does not teach `超過`. Remedy: delete the sentence. Evidence: line 49 follows the dictionary citation but states list provenance, not usage. Confidence: high.

C11. Minor; comprehensibility; `words/過剰.md:19`. `вредно для здоровья` is a stronger end state than `体によくありません`. EN: "is not good for your health." Remedy: `Чрезмерное беспокойство нехорошо для здоровья.` Evidence: the Japanese and the EN example. Confidence: high.

C12. Minor; comprehensibility; `words/逸れる.md:16,18`. `пролетать мимо цели` and `Мяч пролетел мимо мишени` add flight. The Japanese `ボールが的からそれました` and EN "The ball went wide of the target" do not. Remedy: in line 16, `проходить мимо цели`; in line 18, `Мяч прошёл мимо мишени.` Evidence: EN example; no manner of motion in the Japanese. Confidence: high.

Optional:
- `角度`: Ozhegov sense 3 of `ракурс` is a bookish "точка зрения", so the parenthetical is not a false sense. Prefer `точка зрения` anyway, because senses 1-2 are foreshortening or a camera angle, and the card's own example says `под другим углом`.
- `過失`: lead `оплошность` is milder than the accident example. The second gloss `вина по небрежности` already carries the legal sense. Reorder only if a quiz label must lead with negligence.
- `方角`: lead `сторона света` is narrower than JMdict sense 1 (direction). Line 16 states the broader sense, and the parenthetical on `направление` separates it from `方向`. Not a false gloss.
- `遠足`: title `на один день` is the prototype; the body says `обычно`. No change required.
- `道順.md:19`: `туда` adds a destination the Japanese does not name. Low learning impact.
- `原料.md:21`: `видов сырья` is slightly fuller than "one of the ingredients". Acceptable.
- `方針.md:19`: `о новом курсе` drops `действий` and shares `курс` with `方向`. The company-announcement context keeps it a policy. No change required.
- `過半数.md:9`: `большинство` is the quiz gloss of `大半`/`大部分`, but the same sentence immediately restricts it to more than half, and the examples do not use it. Title `больше половины` correctly avoids that gloss.
- `作製.md:19`: `сделали` is ordinary Russian for the completed model and matches EN "made". Do not force `изготовили` unless the `готовим` fix is being applied and the pair should match.
- `逸れる` is the only added-manner case promoted; no other added adverb rose to a finding.

Limits: No native-speaker check. JMdict senses are from the Jisho pages the cards cite; the JMdictDB edit form was not used. Quiz-exclusion symmetry was not assessed (outside these facets): `words/作製.md` does not list `製作`, while `words/製作.md` lists `作製`; `words/余る.md` contrasts `足りる` without listing it. Title-screen stem hits on `слова` were discarded; only segment matches were used as leads. `link_parity.py` found no dropped EN link whose RU target exists. Extra links in `郡`, `地帯` and `余る` teach named contrasts. Unlinked `資料`, `いってらっしゃい`, `娯楽`, `制作`, `観点`, `半数`, `逸らす`, `はぐれる` and the かえる article pointer have no RU target; the wording matches the allowed plain-text pattern. `годан`, `итидан`, `ютоёми`, `окуригана` and `Рэнго` are explained or established. Not claimed: validators, generators, or a full reread of every EN synonym paragraph beyond titles, examples and the contrasts named above.
