# B254 — scoped rechecks at the signed content fix

| Input | Revision |
|---|---|
| Frozen EN | `6af98cb717755690a9ca793e5454a96ebd7a8f9f` |
| Signed blind candidate / parent of fix | `559309ba0d24b9a8cd90fe1a59776a34a86a66e8` |
| Signed fix, all rechecks | `dfdfeebcc0c54972451bc3d028ccc918ccc99ab7`, tree `298406b7d69f86451b7951c9567523064462b2c2` |

The [independent-review record](254-words-batch-93-independent-review-001.md) separates initial reviewer findings, coordinator checks and the decision on each item. The fix changes the 30 new word files and their generated manifest, not the ten existing navigation files or the intake. Sixteen cards have a change beyond example-wrapper formatting; the other fourteen only restore the frozen EN wrapper. Of 61 example blocks, 59 needed a wrapper change. The two 冷める blocks were already exact; that card changed for a different reason. No Japanese sentence or kana string was rewritten.

### What each original reviewer rechecked

The same original reviewer IDs and model families were used in the same order; the full reports follow. Rechecks covered the changes, not a second blind read of the original corpus. The coordinator observed each final reply and idle notification before sending the next recheck. The timestamps below refer to the recheck message and the end of the final reply turn, not a new OS process or a second initial `subagent.completed` event.

| Facet | UTC on 2026-11-23 | Bounded result and actual scope |
|---|---|---|
| Correctness and source coverage | 21:50:15.982–21:55:20.850 | **CLEAN / CLEAN** for changed material. F01–F14 resolved, no new issue. All 30 word diffs, the example blocks, relevant sources and comparison passages; not a full reread of all bodies or a quiz-pool audit. The returned per-file diff sets contain all changed lines for all 30. |
| Consistency, quiz safety, integration | 21:55:45.067–22:00:36.101 | **CLEAN** for changed choices, EN retention and integration. C1 resolved; O1 implemented conservatively, O2/O3 accepted. All 30 candidate-to-fix diffs, all five changed titles, comparison entries and labels; validator and 124 tests reported. Of the zero-context diffs, 28 were directly matched by file headers; for 洒落 (lines 1–10, 11–13 of its diff) and 海水浴 (1–7, 8–18) consecutive bounded outputs supplied the rest. No link-debt scan rerun and no external quiz execution. |
| Russian comprehensibility and scoped coverage | 22:01:00.243–22:05:58.753 | **CLEAN / CLEAN** for changed learner text. C1 and C2 resolved, no new required change. All changed lines of all 30 word diffs were returned (注す split across outputs); no re-read of the ten unchanged navigation diffs, no independent quiz verdict. See body-read qualification below. |

The comprehension recheck describes eight additional fixed cards as full reads. The coordinator could match every nonempty line to returned outputs for **海水浴 and 泊める**. For **流域, 消極的, 消防署, 流行る, 活力 and 洒落** the execution record supports changed hunks and selected passages, not full post-fix files (for example, 流行る:30–32 and 活力:42–44 were absent). The [initial review record](254-words-batch-93-independent-review-001.md) documents the complete blind reads; the recheck verdict applies only to the returned changed material. The original report is preserved below. Its “three wrapped readings” refers to three files (寝間着, 洒落, 淡水); together they contain six wrapped examples.

Comprehension optionals adopted: the missed explanation (油断), scientific/prescriptive rule (法則), Western-style qualifier (洋品店), outing without a walk (おしゃれ), and the glossed causative (泊める). The report left «Налейте», the plural shops, «торговая точка» and «атэдзи» as nondefects. More precisely, Japanese 新しい店 does not mark the number of shops, but **the frozen EN translation does say “New shops”**. The reviewer noted the looser flu example, the shorter beach-visit caveat and the explicit N2 qualification; none was judged a remaining comprehension or coverage defect.

### Changed titles and evidence limits

| Word | Blind label → signed fix |
|---|---|
| 流行る | «быть в моде; свирепствовать (о болезни); иметь успех (о заведении)» → «быть в моде; широко распространяться (о болезни); иметь успех (о заведении)» |
| 活力 | «жизненная сила; жизнеспособность» → «жизненная сила; энергия» |
| 治す | «вылечить; лечить» → «вылечить; залечить (рану)» |
| 洋品店 | «магазин одежды и аксессуаров» → «магазин одежды и аксессуаров западного стиля» |
| 法則 | «закономерность; закон природы» → «закономерность; научный закон; правило» |

At the signed fix the complete 30-word title screen against the RU pool returned 28 guarded lines and 213 unguarded stem-only leads. All three exact segment overlaps were already guarded: 活力—エネルギー, 活力—活気 («энергия») and 法則—決まり («правило»). This is not the reviewer's narrower seven-word screen; neither screen establishes that all Russian meanings are equivalent or that every theoretical overlap will be drawn.

Consistency optional O-A (流行る–広める) was not adopted: intransitive disease spread and causing something to spread are not the same answer. O-B (the existing 書店/八百屋 vs 商店 cases) was not extended from the conservative 洋品店 pair; no required new edge was established. O-C identified a genuine corpus-style difference, not a verified reader failure: the exact frozen example wrappers were retained and no global style policy was changed. The reviewer calls the fixed example convention half-width in brief; **two 冷める pairs retain the source's full-width parentheses**, and for the six split examples the exact prefix is newline and two spaces followed by `(`. The candidate-to-fix example-line change is in **29** cards, not all 30: 冷める's changed line is about feelings.

Four RU-only additions were classified as required for the actual visible labels (商店→店, ショップ→店, ショップ→売り場, 油断→のんき); two were accepted as conservative without established necessity (涼む→休む, 洋品店→商店). All 122 EN exclusions remain in source order. Neither the three screen matches nor those six additions certify option counts, tag/random fallback, voice, drawing, device rendering, ordinary RU activation or release.

The fix tree regenerated manifest `7b3d067ef940470a` (5,734 files, three images, two scene catalogs); the validator reported zero errors, 124 unit tests passed, and the post-generation local archive-budget estimate was 8,333,334 bytes (5,756 entries). These checks used the content-fix tree; final validation of the later committed records is a separate [receipt](254-words-batch-93-final-validation-001.json), not a public archive or release verification.

## Original recheck reports

The reports below are reproduced in run order, normalized to LF. Section headings, runtime metadata and hashes are not part of the reports. A hash denotes the original report file, not its stdout wrapper or the network return.

### correctness — `gpt-6.2-sol`

Agent `e068a9e0-56ea-4f50-a09c-e5f151de29cc`, input `dfdfeebcc0c54972451bc3d028ccc918ccc99ab7`, completed 2026-11-23T21:55:20.850Z; original report file SHA-256 `644332ec7ec74c732c5ef386e3d4ceba050806aabf04bb660d96962d1fa96219`.

Snapshot: RU HEAD `dfdfeebcc0c54972451bc3d028ccc918ccc99ab7`, tree `298406b7d69f86451b7951c9567523064462b2c2`, parent `559309ba0d24b9a8cd90fe1a59776a34a86a66e8`. `git status --porcelain` пуст. EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`, только Git-объекты.

Scope: correctness и scoped coverage на fix. Проверены собственный замороженный отчёт и dispositions, все изменённые строки с контекстом в `parent..fix -- words` и нужные участки карточек и источников. Прочитаны диффы всех 30 `words/<имя>.md`:
- 淡水, 冷める, 涼む, 液体, 消防署, くたびれる, 消耗, 消毒, 消極的, 消化;
- 海洋, 海水浴, 寝間着, 浴衣, 流行る, 流域, 活字, 活力, 洗剤, おしゃれ;
- 洒落, 商店, ショップ, 洋品店, 注す, 原理, 法則, 泊める, 治す, 油断.

Для всех 30 сопоставлены японские предложение и кана со скобками, поля `word`, `reading`, `jlpt`, `type`, `kanji`, `tags`, исходные EN `quiz_exclusions` и относительные ссылки. Поля совпали; все EN-исключения сохранены; ссылки не изменились относительно родителя, доступные в RU цели EN-ссылок сохранены. Десять навигационных файлов не менялись в fix. Модель не верифицируется.

Verdicts: Первоначальный снимок: correctness **NEEDS FIX**, coverage **NEEDS FIX** (замороженные вердикты); 10 навигационных диффов **CLEAN**. Fix: correctness **CLEAN**, scoped coverage **CLEAN** для изменённого материала, Russian comprehensibility **not assigned**. Все 14 исходных находок **resolved** (9 Medium, 5 Low); новых дефектов в проверенной границе не установлено.

Findings: Строки указаны в fix; уверенность в статусах высокая. Daijisen — 小学館『デジタル大辞泉』.

- **F01 — resolved · `words/冷める.md:21`.** Вместо общего «охладеть» — восторг проходит, привязанность слабеет, гнев утихает. [Daijisen 冷める](https://www.weblio.jp/content/冷める) ②, JMdict 1556750 §2.
- **F02 — resolved · `words/消極的.md:20–21`.** Передано нежелание действовать, а 多く относится к прозвучавшим мнениям, не к говорящим или манере речи. [Daijisen 消極的](https://www.weblio.jp/content/消極的), пример ответа на предложение; JMdict 1350220 §1.
- **F03 — resolved · `words/流行る.md:4,12,17,21`.** Передана распространённость гриппа, не тяжесть болезни; мода и успех заведения сохранены. [Daijisen 流行る](https://www.weblio.jp/content/流行る) ①–③, JMdict 1552310 §§1–3.
- **F04 — resolved · `words/流域.md:25,35–36`.** Вода стекает с территории в реку, не наоборот. Частотное «обычно» удалено; осталось подтверждённое замечание о многозначности. [Daijisen 流域](https://www.weblio.jp/content/流域), [Кузнецов, «бассейн»](https://gramota.ru/meta/basseyn) ①–②.
- **F05 — resolved · `words/活字.md:19–20`.** Текст набирают из литер, а не набирают сам шрифт. Пример о мелком шрифте сохранён. JMdict 1208300 §§1–2; [Nipponica, 平石文雄・山本隆太郎](https://kotobank.jp/word/活字-45209), определение набора из литер.
- **F06 — resolved · `words/活力.md:4,9,12,16`.** Энергия для активного действия, не жизнеспособность; прямое исключение エネルギー сохранено. [Daijisen 活力](https://www.weblio.jp/content/活力), JMdict 1208480 §1.
- **F07 — resolved · `words/治す.md:4,12,16–17,44–45`.** «Вылечить; залечить (рану)». В данных примерах 治しました сообщает результат, а 治すために — цель; переходность и を сохранены. [Daijisen なおす](https://www.weblio.jp/content/治す) 1㋒ и 用法, JMdict 2856318 §1.
- **F08 — resolved · `words/海水浴.md:16–21,30–38`.** Купание и поездка купаться разведены: движение у に行く, не у существительного. Не всякая поездка на пляж — 海水浴, но жёсткий запрет снят. [Daijisen 海水浴](https://www.weblio.jp/content/海水浴), JMdict 1201520 §1.
- **F09 — resolved · `words/消防署.md:16–17,28`.** «Местное подразделение» не превращает муниципальный орган в государственное ведомство; учреждение и здание не смешаны. [Daijisen 消防署](https://www.weblio.jp/content/消防署), муниципалитеты и специальные районы; JMdict 1350370 §1.
- **F10 — resolved · `words/洋品店.md:4,12`.** В лейбле и заголовке восстановлен западный стиль, не страна производства. [Daijisen 洋品店](https://www.weblio.jp/content/洋品店) → [洋品](https://www.weblio.jp/content/洋品) ①; EN `batch-88.json` 1794470 §1 и `reviewEvidence/comparisonEntryFamilies/1662200` §1.
- **F11 — resolved · `words/法則.md:4,9,12,16–21`.** Заголовок охватывает научный закон и правило; текст различает оба значения. Исключения 規則, 規律 и 決まり сохранены. [Daijisen 法則](https://www.weblio.jp/content/法則) ①–②, JMdict 1517380 §1.
- **F12 — resolved · `words/洒落.md:55`.** Стиль — дополнительный смысл без самостоятельно установленного N2. EN `words/洒落.md:41`, индекс N2:719 и JMdict 1568640: выбран §1, §2 дополнительный.
- **F13 — resolved · 30 карточек из Scope.** Буквальный паритет с EN для 61/61 пар, включая предложение, кану, пунктуацию, внешние скобки и разделитель между предложением и каной. Исправлено 59/61 оболочек в 29 карточках; две пары 冷める не менялись. Восстановлены шесть переносов с двумя пробелами: 淡水:19–22, 寝間着:20–23, 洒落:20–23. Внешний Markdown и разделитель перед переводом не входят в сравнение.
- **F14 — resolved · `words/おしゃれ.md:20`.** «Сегодня перед выходом я наряжусь»: выход подразумевается, назначение не добавлено. [Daijisen 出掛ける](https://www.weblio.jp/content/出掛ける) ①, пример выхода нарядившись.

Проверка остальных изменений:
- `words/泊める.md:44–46`: 泊まる (годан) → 泊まらせる (позволить или велеть остаться на ночь по контексту), не самостоятельное переходное 泊める. [Daijisen 泊まる](https://www.weblio.jp/content/泊まる) ①, [泊める](https://www.weblio.jp/content/泊める) ① и EN `grammar/causative-perspective.json`. Удалённая RU-пара 泊める–泊まる отсутствовала в EN: «дать ночлег» и «ночевать» различаются ролями в обоих направлениях.
- `words/油断.md:19–20`: «пропустил» передаёт, что объяснение не услышал. [Daijisen 聞き逃す](https://www.weblio.jp/content/聞き逃す) ①. Причина во втором примере и отрицание в первом сохранены.
- `words/ショップ.md:4,9`, `words/洋品店.md:4,9`: добавленные цели 売り場 и 商店 существуют. Для «торговой точки» возможен ответ «место продажи»; магазин западной одежды может быть «розничным магазином». Это прямое пересечение RU-ответов, не взаимозаменяемость японских слов. Сверены фактические RU `words/売り場.md:4`, `words/商店.md:4` и статьи [売り場](https://www.weblio.jp/content/売り場), [ショップ](https://www.weblio.jp/content/ショップ), [商店](https://www.weblio.jp/content/商店).

Optional: нет.

Limits: Это перепроверка изменений, не повторное полное прочтение 30 двуязычных пар и 10 навигационных диффов. Глобальный квиз-пул и UI не проверялись. `manifest.json` есть в stat, не проверялся в языковых фасетах; валидатор и генераторы не запускались. Заголовок подписи присутствует, криптографическая проверка не выполнялась.

### consistency — `claude-opus-5.5`

Agent `d6fa97fa-35a2-416f-8e84-0f260d96c459`, input `dfdfeebcc0c54972451bc3d028ccc918ccc99ab7`, completed 2026-11-23T22:00:36.101Z; original report file SHA-256 `c4cb9289e7090cc3002618fd151f7daa781ec1a34ba624fea80197f2f708246a`.

# B254 recheck: consistency, quiz safety and integration (read-only)

## Snapshot
- Fix dfdfeebcc0c54972451bc3d028ccc918ccc99ab7: parent 559309ba (my blind candidate); signature status `G`.
- HEAD = fix. `git status --porcelain --ignored` was empty before and after.
- Frozen EN 6af98cb7.
- Diff 559309ba..dfdfeeb touches 31 files: 30 words/*.md and manifest.json.
- No kanji, grammar, articles, counters or docs changes. The 10 navigation files and the intake file are byte-identical to the candidate.
- My original report is unchanged.

## Scope actually read or run
- Inputs: my original report and the dispositions file.
- **Full -U0 diff of all 30 changed words, every hunk read:**
  - Example-line hunks in all 30.
  - Title, H1 and body changes in 流行る, 活力, 治す, 洋品店, 法則.
  - Body sentences in 冷める, 流域, 海水浴, 消防署, 泊める, 治す, 洒落.
  - Exclusion changes in ショップ, 洋品店, 泊める.
- **Frozen JMdict packets:**
  - batch-68 reviewEvidence/comparisonEntryFamilies/1588550 (売り場).
  - batch-66 entryFamilies and comparisonEntryFamilies/1600560 (のんき).
  - From the original review: the 油断, 涼む, 泊める, 商店 and ショップ JSON.
- **Script over all 30 cards, RU vs frozen EN `git show`:**
  - Front-matter keys and order, and word/reading/jlpt/type/kanji/tags.
  - Ordered EN exclusions as a prefix of the RU list; RU extras.
  - Exclusion targets exist; no self-exclusion.
  - Headings, and H1 equal to the title.
  - Result: no differences.
- **Title collisions:**
  - Full RU title corpus scanned with meaning regexes for the 5 new titles, marking guards in both directions.
  - `word_title_screen.py` on 流行る, 活力, 治す, 洋品店, 法則, ショップ, 泊める: 3 exact-segment lines (all guarded) and 90 stem-only lines, all read.
- **Manifest:** sha256 of each of the 30 changed files is present in manifest.json (0 unmatched).
- **Commands:**
  - `tools\validate.py` → 0 error(s), exit 0.
  - `unittest discover tools` → 124 tests OK.
  - Both run with -B and PYTHONDONTWRITEBYTECODE; no bytecode left.
- **Example delimiters:**
  - Fixed RU uses ASCII " (" + newline in 淡水, 寝間着 and 洒落, matching EN's two-line layout (2 lines each).
  - Corpus count: 245 RU word files are half-width-only (including B254); about 3451 use full-width （ ）.
  - Batch 253: 0 of 30 files are half-width.
  - No tool in tools/ parses example parentheses.
- **Not re-run:** link_parity and the link-debt scan, because no link text changed in the diff (verified by reading every hunk).

## Verdicts (bounded)
- Correctness / quiz safety: CLEAN. No remaining required guard among the changed titles and choices.
- Coverage / EN preservation: CLEAN.
  - All 122 EN exclusions are kept in EN order on all 30 cards.
  - There are exactly 6 RU additions.
  - Wrappers are unchanged.
- Integration / format: CLEAN.
  - Validator and 124 tests pass, and the manifest hashes match.
  - The delimiter style is an optional consistency note, not a defect.
- Russian comprehensibility: not assigned.

## Disposition status
**C1 (ショップ <-> 売り場): RESOLVED.**
- ショップ.md:9 now reads `quiz_exclusions: [商店, 店, 売り場]`.
- **Evidence correction.** My original "point of sale" gloss is wrong for the frozen packet. 1588550 sense 1 is "selling area; counter; section; department; sales floor", and sense 2 is "good time to sell".
- **Basis.** The guard rests on Russian-label overlap, not lexical identity. The unqualified «торговая точка» can be heard as a place where goods are sold, which is 売り場's RU title «место продажи; торговый отдел». In the RU-title → JP direction, 売り場 is a contextual alternative answer.
- **Classification.** Justified (required by the RU titles as written). It is not an assertion that shop = department.

**O1 (洋品店 → 商店): IMPLEMENTED; conservative.**
- 洋品店.md:9 now reads `[店, ショップ, 商店]`.
- **Support.** The broad 商店 title «торговое заведение; розничный магазин» (1347180 "shop; store; firm") genuinely covers a 洋品店 (1794470; 洋品 1662200 §1). The guard is supported directly, not inferred transitively from 店.
- **Necessity.** Not established, because the specific title is distinct. Acceptable.

**O2 (泊める → 泊まる removed): ACCEPTED; not required.**
- «приютить на ночь; дать ночлег» vs «ночевать; останавливаться на ночлег» share only the stem ночлег-. The roles differ (giver vs stayer); see 1474860 vs 1474850 §1.
- 宿 and 宿泊 still guard 泊まる for their own reasons.
- No EN exclusion was removed (verified).

**O3 (placement on ショップ): ACCEPTED.** The fix stays inside the batch; 売り場 is untouched.

**Retained RU additions.**

| Addition | Classification | Basis |
|---|---|---|
| 商店 → 店 | required | hypernym «магазин» |
| ショップ → 店 | required | hypernym «магазин» |
| 油断 → のんき | required, real semantic support | 1600560 sense 1 includes "careless; thoughtless" next to "carefree", matching 油断 1538690 "carelessness". The stem alone would not have established it. |
| 涼む → 休む | conservative | Driven by the RU title «отдыхать в прохладе»; 1554380 has no rest sense. Not a lexical equation. |

## New titles: affected comparisons
**活力 «жизненная сила; энергия»**
- Exact segment энергия with エネルギー «энергия» and 活気 «оживление; энергия»: both guarded on 活力 (EN-inherited).
- 元気, 体力, 力, 勢い, ぴんぴん, きびきび: guarded.
- 人生, 明るい, 陽気, ごしごし: stem-only, no shared meaning.

**法則 «закономерность; научный закон; правило»**
- Exact segment правило with 決まり: guarded.
- 規則 «правила», 規律, 法 «закон; метод», 法律, 原理, 主義: guarded.
- 作法 «правила этикета» and 礼儀 «правила вежливости» are qualified etiquette rules and are not answers for 法則.
- 違反, 改正, 適用 and similar differ in part of speech or event.

**流行る «быть в моде; широко распространяться (о болезни); иметь успех (о заведении)»**
- 広がる «распространяться», 流行, 人気, 栄える, 盛ん: guarded.
- 成功 «успех» (noun) vs «иметь успех (о заведении)»: qualified; unchanged from the candidate.
- 広める «распространять; расширять»: see O-A below.

**治す «вылечить; залечить (рану)»**
- 治る «выздоравливать; заживать», 回復, 直す: guarded.
- 傷 «рана» is a noun, not an answer.
- No RU 治療 or 手当て title collides.

**洋品店 «магазин одежды и аксессуаров западного стиля»**
- 店, ショップ, 商店: guarded.
- 洋服 «одежда западного стиля» is the garment, not the shop. The qualifier makes the shop/garment distinction explicit.
- 書店, 八百屋, 店員 are distinct.

**ショップ «торговая точка»**
- 市場 «рынок; торговая площадка» is a marketplace, not an outlet. The other hits are only on точка/торго- (点, 見解, 商売, …). Not required.

## Findings
None blocking. No required guard is missing, and no new collision or format defect was introduced by the fix.

## Optional (non-blocking)
- **O-A.** 流行る's new wording «широко распространяться» moves closer to 広める «распространять; расширять». 広める already excludes the noun 流行, but not 流行る.
  - The voice (-ся vs transitive) and «(о болезни)» keep the two distinct, so a guard isn't required. EN has none.
  - A conservative pair would be 広める.md:9 + `流行る`. That file is outside the batch.
- **O-B.** Siblings outside the batch, 書店 «книжный магазин» and 八百屋, do not guard 商店, unlike the new 洋品店 → 商店. The same holds in EN. Not required, because each specific title is distinct.
- **O-C.** Delimiter style. B254 now uses ASCII " (" like EN; batch 253 and about 3451 RU files use full-width （）.
  - The validator, tests and tools/ are indifferent to this, so it is not a defect.
  - Whether an external app reader prefers one form was not verified.
  - A corpus-wide style decision could be recorded later.

## Limits
- Russian naturalness of the reworded bodies (冷める, 流域, 海水浴, 消防署, 泊める, 治す, 活字, 消極的, 油断, おしゃれ) was read for consistency only, not judged.
- Dictionary evidence is limited to the frozen packets cited.
- Quiz runtime direction and option-count behaviour were inferred, not executed. The external app parser is not in this repo.
- link_parity and the link-debt scan were not re-run; that is justified because no link text changed.

### comprehensibility — `grok-4.7`

Agent `a4fb99dc-af7c-4824-b3fc-bb51193fa085`, input `dfdfeebcc0c54972451bc3d028ccc918ccc99ab7`, completed 2026-11-23T22:05:58.753Z; original report file SHA-256 `ec2de08403114ec32e06c7b3ea963417ebc1faba3afd4792cc09ae92cde8ebfd`.

Snapshot: fix dfdfeebcc0c54972451bc3d028ccc918ccc99ab7; parent 559309ba0d24b9a8cd90fe1a59776a34a86a66e8; frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f; uncommitted changes: none. Model: not verifiable in this session. Original report preserved.

Scope: Russian comprehensibility and scoped coverage only, recheck of the signed fix. Read in full: the parent-to-fix diff of all 30 `words/*.md` cards, and the current cards `words/流域.md`, `words/消極的.md`, `words/海水浴.md`, `words/消防署.md`, `words/流行る.md`, `words/活力.md`, `words/泊める.md`, `words/洒落.md`. Compared frozen EN `words/海水浴.md`, `words/消防署.md`, `words/流行る.md`. Opened `words/エネルギー.md` titles for the new 活力 label. Sampled `manifest.json` hunks (contentVersion and word hashes only). Confirmed no diff for kanji/則.md, kanji/商.md, kanji/域.md, kanji/巻.md, words/せっけん.md, words/断水.md, words/気体.md, words/活躍.md, words/焦点.md, words/血液.md; those files were not re-read. Prior dictionary evidence for 流域 and 消極的 was reused, not re-fetched.

Verdicts: correctness not assigned; coverage CLEAN; Russian comprehensibility CLEAN. CLEAN means no confirmed fixable defect in this recheck, not a proficiency or quiz-safety claim.

Finding status:
- C1 resolved. `words/流域.md:25` is now «Вместе они обозначают территорию, с которой вода стекает в реку.» That matches the opening (lines 15–16) and Daijisen «河川に流れ込む降水の降り集まる地域». The «обычно» claim about bare «бассейн» is gone; lines 35–36 say the Russian word has other senses, for example a swimming pool, and here it means a river basin. No reversed reading remains.
- C2 resolved. `words/消極的.md:21` is «Во многих мнениях, прозвучавших на совещании, чувствовалось нежелание действовать.» 意見 stays the locus; «сдержанно» is gone. Line 35 still glosses 遠慮 as «сдержанность из уважения к другим». «Нежелание действовать» matches the card's own definition and 精選版日本国語大辞典 進んで行為をしようとはしないさま. «чувствовалось» is a mild hedge, not a return of the speaker-manner reading. The first example, «без особого энтузиазма», also avoids the grammatical-passive reading the card still disclaims.

Optional status:
- 油断.md:20 resolved: «пропустил», not «прослушал». Context still selects a miss, not listen-through.
- 法則.md:4 resolved: title «закономерность; научный закон; правило» no longer forces a nature-only split. Body still teaches both a scientific law and a rule to follow.
- 洋品店.md:4 resolved: title restores «западного стиля». Example glosses stay shorter; the definition still has the qualifier.
- おしゃれ.md:20 resolved: «Сегодня перед выходом я наряжусь» drops the unexpressed stroll.
- 泊める.md:44–46 resolved in learner text: «каузативная форма» plus 泊まらせる, glossed «позволить или велеть». Not the imperative reading. The 泊まる contrast remains in the body.
- 液体.md:18 «Налейте» kept for liquid into a bottle. Still not a defect.
- 活力.md:20 plural «магазины» kept; Japanese and frozen EN do not fix the number. Not a defect. The new title «жизненная сила; энергия» shares a word with エネルギー «энергия»; the 活力 article still separates life force from joules. Reverse quiz pairing was not audited.
- ショップ title «торговая точка» kept. Still stiff, still clear. Not a defect.
- Bare «атэдзи» in くたびれる and 洒落 unchanged and still followed by the practical consequence. Not a defect.
- Residual, not a defect: `words/海水浴.md:36` «Не всякую поездку на пляж называют 海水浴» no longer states EN's condition (nobody bathes or swims). The opening still defines the word as sea bathing, including a short dip, so the article's question remains answered.
- Residual, not a defect: `words/流行る.md:21` «многие болеют гриппом» is looser than EN "prevalent", but the title and definition keep «широко распространяться».
- `words/洒落.md:55` «отдельный уровень N2 … не установлен» is meta. The style sense is still taught just above it.
- `words/消防署.md:16–17` «аварийно-спасательные работы» is a fair Russian rendering of EN "related emergency work", not a new false sense.

Other changes: reading separators and three wrapped readings (寝間着, 洒落, 淡水) stay paired with the sentence. 冷める now explains weakening feelings without relying on figurative «охладеть» alone. 治す title «вылечить; залечить (рану)» and the purpose-versus-result note are clearer against 直す. 活字 «набрали текст из литер» matches setting type better than "набрали шрифт". Quiz-metadata edits (ショップ adds 売り場; 洋品店 adds 商店; 泊める drops 泊まる) are outside these facets; the learner contrast for 泊まる is still on the card.

Limits: Correctness was not reassigned. Navigation lines were verified unchanged, not reread. Manifest hashes were sampled, not opened line by line. Quiz necessity and cross-card option safety were not judged. No claim of learning outcomes.
