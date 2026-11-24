> Original blind return on `599b9e5b657468ea8c26bd651fe5cc9a4493ce64`, tree `7e2bfc4cc9e0807265347f39c79863b1fab22498`.
> Correctness and EN-to-RU coverage. First dispatch and report-producing response: `claude-opus-5.5`; reviewer `6ea4c257-32b0-4378-b463-653132a6d129`.
> [Reconciliation](256-words-batch-95-independent-review-001.md) and [scoped rechecks](256-words-batch-95-recheck-001.md). Original report body follows.

# B256 (256-words-batch-95) — blind correctness + EN→RU coverage review

## Snapshot
- RU candidate 599b9e5b657468ea8c26bd651fe5cc9a4493ce64 (tree 7e2bfc4cc9e0807265347f39c79863b1fab22498, parent b604235935e67b74fa98cf9bfabb9d979554473f), signature status G; `git status --porcelain --untracked-files=all` empty → no uncommitted or untracked files. Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f, clean.
- Runtime model/ID metadata: not available to me; not guessed.

## Scope
- Parent→candidate: 39 paths = 30 new words/*.md + 7 nav files (+1/−1 each) + manifest.json (generated, not reviewed) + intake JSON (not read, per instruction).
- Read in full: all 30 b256-blind/*.md pairs (RU+EN, every numbered line); all 30 dictionary/*.json and facts/*.json; all 7 navigation/*.diff; current-title-screen.txt L1–334 (L1–141 in earlier chunks, then 142–205, 206–270, 271–334). No truncated or failed reads observed.
- Immutable blob reads: candidate docs/content-format-reference.md; EN docs/content-format.md (≈L126–176, quiz authoring); RU/EN front matter of related words; RU/EN counterpart lines of the 7 nav files; RU/EN "source spelling" usages; final re-check of every cited line (山林, 本来, 有無, 朗らか, さすが, 果たして, 次ぐ, 欠伸, 桁, 構造, 枚数, 枕, 東西) and titles of 楽しい, 愉快, 以内, 以下, 未満, はじめに.
- Scripted checks: pair files = git blobs (SHA-256, every line, LF end); front matter RU=EN except title + 4 added RU exclusions (次ぐ+占める, 果たして+実は, 枚数+枚, 朗らか+さわやか); word/reading/jlpt 2/type/kanji/tags preserved; all RU relative links resolve; links dropped vs EN point only to targets absent in RU; inbound-link parity: every EN link to the 30 words from a file that exists in RU is present at candidate (EN-only sources all absent in RU: ついで, ブラシ, 体系, 光線, しぼむ, 南北, 元々, kanji 造/林/森/枯/枚/杉).
- Japanese example sentences + readings: identical to EN in all 30 cards (scripted for the two-part layout; other layouts compared manually).
- Not used: the optional source-only packet; web.

## Verdicts
- Correctness (readings, forms, JLPT metadata, senses, kanji notes): NEEDS FIX (minor) — F2, F3, F5; otherwise consistent with the packets.
- Coverage (EN→RU meaning): NEEDS FIX (minor) — F1, F2, F3.
- Distractors/quiz_exclusions: NEEDS FIX (minor) — F4; no defect found in the 4 added RU exclusions.
- Navigation (7 diffs): CLEAN — each links the existing mention exactly where EN links (桁, 欠伸 ×2, 杉 ×2, 枯れる ×2); targets exist; glosses match the new titles.
- Russian wording (only where meaning is affected; no native-speaker claim): NEEDS FIX for F1/F3; rest Optional.

## Findings
**F1 — minor · coverage (direction reversed) · words/山林.md:31**
Claim: «Пусть перевод подсказывает пейзаж или контекст землепользования.» EN:31 "Let the landscape or land-use context guide the translation." RU makes the translation indicate the context, the reverse of the advice.
Fix: «Выбирайте перевод по контексту: пейзаж или землепользование.»
Source: EN words/山林.md:31. Confidence: high.

**F2 — minor · correctness/coverage (example) · words/本来.md:18**
Claim: これは本来の目的ではありません。 — «Изначально цель была не в этом.» EN "This is not the original purpose." RU turns adnominal 本来の目的 + present です into a past-time adverb + past tense, so it can read as "the goal has since changed" rather than "this is not the intended purpose"; it also hides the 本来の + noun pattern and conflicts with the card's own L16 («Слово не ограничивается событием, произошедшим раньше по времени») and L32 (本来の目的 = «задуманной или изначальной цели»).
Fix: «Это не изначальная (истинная) цель.»
Source: EN:18; JMdict 1523270 s1. Confidence: medium.

**F3 — minor · coverage (participant role) + idiom · words/有無.md:21**
Claim: 有無を言わせずに仕事を押し付けました。 — «Мне навязали работу, не спросив ни согласия, ни отказа.» The Japanese is active 押し付けました with no stated recipient; EN "They imposed the work without allowing any objection." RU adds the speaker as recipient (Japanese would normally mark that, e.g. 私に or passive 押し付けられました), which can mislead about voice; «спросив … отказа» is not idiomatic.
Fix: «Работу навязали, не дав ни согласиться, ни отказаться.» (matches L23)
Source: EN:21; JMdict 1541610 s2 "consent or refusal". Confidence: medium.

**F4 — minor · distractor · words/朗らか.md:9**
Claim: quiz_exclusions omit 楽しい. RU titles share the lead word: 朗らか «весёлый и открытый; ясный (о небе, дне)» vs 楽しい «весёлый; приятный» (screen L306 "!!"); the card's L16 also uses «весёлый … приятный звук» (JMdict 1560710 s1 cheerful; merry; melodious). A learner could reasonably accept «весёлый; приятный» for 朗らか and pick 朗らか for that prompt. The parallel 愉快 «весёлый; забавный» is already excluded in L9 (also in EN). RU-specific: EN titles ("cheerful; bright and clear" / "enjoyable, fun") share no head word.
Fix: add 楽しい to 朗らか quiz_exclusions (pairwise, symmetric).
Source: candidate words/朗らか.md:4,9,16; words/楽しい.md:4. Confidence: medium-high.

**F5 — minor · correctness (implied etymology) · words/さすが.md:27**
Claim: «流石 — исходное написание с цельным нерегулярным чтением さすが. Обычно пишут каной.» EN "source spelling" means the spelling in the source list (packet sourceSurface 流石, N2 row); Russian «исходное» naturally reads "original", implying 流石 is the word's original form. JMdict 1552390 tags the reading gikun/jukujikun, lists 遉/有繋 as rare kanji forms, all senses kana-usual; 2140120 marks 流石に as ateji; the card's L50 cites native-word origin. The same calque is in words/屑.md:25 (out of scope).
Fix: «流石 — словарное написание кандзи с цельным нерегулярным чтением さすが…»
Source: EN:27; dictionary/さすが.json. Confidence: medium.

## Optional
- 次ぐ:48–49 «не определяет его место по любому показателю» can read "by no measure"; EN "every measure" → «не означает, что он занимает то же место по всем показателям».
- 欠伸:27 «ключ со значением «зевать»» — EN names the radical ("yawning radical") → «ключ, который называют «зевота» (あくび)».
- 山林 title (L4/L12) and L19 «лесистые горы» foreground mountains, while L31 warns against that (JMdict 1303230 s1 mountain forest; forest land) → «горный лес; лесные угодья».
- 桁:20–21 «шесть разрядов», «число из трёх разрядов» → «шестизначный», «трёхзначное число»; L39 «Словарный перевод «столбец, колонна»» renders the English gloss "column" — say so.
- 構造:44 is categorical («относится») where EN says "can concern".
- さすが:20 «Даже такой учитель растерялся» — «такой» lacks an antecedent → «Даже учитель, уж на что знающий, …» (sense 3 さすがの…も).
- 枚数:18 «количество листов копий» is clunky; L23 «считаемых на 枚» → «которые считают счётным словом 枚».
- 枕:29 cites はじめに as «введение; для начала», unlike its title «для начала; вступление (в книге)».
- 東西 title «восток и запад» drops EN's "East and West" cultural sense (body L16 covers it) → add «Восток и Запад».
- 本来:19/36 «Как положено, …» is weak for counterfactual 本来なら → «По идее / По-хорошему, …».
- 朗らか:19 «весело и открыто засмеялись» — «открыто» reads "openly" → «весело засмеялись».
- 未満: 以下 «не больше; нижеследующее» is excluded, but 以内 «в пределах; не более» (same inclusive-limit wording; no shared stem, so not screened) is not; consider for parity. Low confidence.
- 果たして vs 実に «действительно; очень»: card L24 already contrasts «действительно, очень»; no change needed.

## Limits
- JMdict IDs outside the packets not verified: 1042130, 1413240, 1279820 (キャンパス), 2639500 (来日), 1406150/1588410 (有無), 森林 comparison IDs. Daijisen/Weblio/Kotobank links not fetched; F5's history point rests on JMdict tags and the card, not on the cited dictionary text.
- Glosses do not verify Russian; no frequency/naturalness claims beyond those stated; no native-speaker, learner, device or release claims.
- Title screen is mechanical; only "!!" pairs with semantic overlap were judged. Pairs without shared stems were checked only for listed related words and spot lookups.
- manifest.json, the intake JSON and the source-only packet were not reviewed.