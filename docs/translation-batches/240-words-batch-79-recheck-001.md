# Batch 240 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `d0d977cad025983c702361e0408d9c9be4b8b085` | `401f953909d959a255de1b8abeeb08406c7d4054` | Initial review snapshot: the signed candidate, on `origin/full-ru-240-words-79`. |
| `3544d75afb94d41fc2eccd74dd0df04a6a762b77` | `3a7d75eb739aa93018ba6b4d41ebf36fd181bedc` | Fix 1 (final candidate). It covers correctness C1 to C4 (C4 by deletion under comprehensibility C6), comprehensibility C1 to C17, C19 and C20 (C1, C3, C5, C6, C7, C8, C11, C12, C13, C15 and C17 as modified or partial dispositions), and consistency O2 through comprehensibility C17's title change. It adds one exclusion (若々しい→ぴんぴん), removes none, adds one link (蒸す:43 → べたべた) and removes none. Signed; on `origin/full-ru-240-words-79`. |

Fix 1 changed sixteen word files and regenerated `manifest.json` (`contentVersion` `efb73b59212c9d63`, 5,319 entries:
5,314 `files` + 3 images + 2 scenes; the candidate had `c8706e72790b4f7f`). The intake was not refreshed; it still records
the candidate's 34 payload hashes.
- `落第` (line 20; correctness C1): «— Я провалил экзамен и заново прошёл материал.» instead of «— Я провалил экзамен и
  заново выучил материал.»; perfective «выучить» asserted successful mastery, whereas もう一度勉強し直しました and EN
  "studied the material again" state only renewed study.
- `茂る` (lines 28–29; correctness C2): «滋る помечено как редко используемое написание, и в этих примерах ему подражать не
  нужно.» instead of «滋る помечено как устаревшее, и в этих примерах ему подражать не нужно.», matching JMdict 1533740's
  "rarely used kanji form". The stronger claim is inherited from EN 茂る:25, which is frozen and unchanged.
- `蒸す` (lines 41–43; correctness C3 and comprehensibility C2): the sentence «Эти пересечения требуют прямых исключений в
  тестах, хотя слова не взаимозаменяемы во всех конструкциях.» becomes «При этом слова не взаимозаменяемы во всех
  конструкциях.», and a new line 43 restores EN :48's link to the existing card べたべた: «[べたべた](べたべた.md) описывает
  липкость или привычку льнуть к кому-то, а не саму душную влажную погоду.» The six English-label guards are kept
  unexplained.
- `蒸す` (lines 4 and 12; comprehensibility C3, modified): title and H1 «готовить на пару; быть душно и влажно (о погоде)»
  instead of «готовить на пару, прогревать паром; быть душно и влажно (о погоде)»; the towel sense stays in the body. The
  remedy's «душно и влажно» without «быть» was not used.
- `艶` (line 45, now removed; comprehensibility C6, split, superseding correctness C4's replacement): the sentence «Среди
  английских переводов в словаре есть «glaze» (глазурь), но это не доказывает, что 艶 называет материал глазури или само
  покрытие керамики глазурью.» is deleted. Line 31 «Отдельной карточки кандзи 艶 в нынешней коллекции нет.» is unchanged.
- `湿気` (line 18; comprehensibility C1, modified): «Карточка учит оба чтения: しっけ и しっき.» instead of «Эта карточка
  охватывает оба чтения из исходного списка: しっけ и しっき.»; full deletion was declined so the two-reading coverage stays.
- `芸能` (lines 4 and 12; comprehensibility C5, modified): title and H1 «исполнительские искусства; освоенные искусства и
  навыки» instead of «исполнительские искусства; освоенное искусство (как достоинство человека)», removing «достоинство»,
  which overlapped 長所 «достоинство; преимущество». The remedy's «развитые умения» was not used.
- `芸能` (line 40, now removed; comprehensibility C4): «Не называйте 芸能 любую достигнутую цель только потому, что
  английский словарный перевод говорит «accomplishments» (достижения).» is deleted; line 22 already says abilities, not
  results.
- `著す` (lines 4, 12, 19 and 20; comprehensibility C7, modified, severity moderate rather than high): title and H1
  «писать (книгу, труд); издавать своё сочинение» instead of «быть автором (книги, труда); издавать своё сочинение»;
  examples «— Она написала книгу об истории Японии.» and «— Этот учёный написал много книг.» instead of «— Она стала
  автором книги об истории Японии.» and «— Этот учёный — автор многих книг.» The remedy's perfective title was not used;
  書く is already excluded.
- `教養` (line 21; comprehensibility C8, partial): «— Она — образованный, культурный человек.» instead of «— Она
  образованный, культурный человек.»; «культурный» is kept.
- `教養` (line 19; comprehensibility C9): «— Я хочу с помощью чтения углубить свою образованность.» instead of «— Я хочу
  расширить свой кругозор с помощью чтения.» (深める = deepen; EN "deepen").
- `若々しい` (lines 4, 9, 12 and 20; comprehensibility C10, modified): title and H1 «моложавый; полный молодости (о голосе,
  манерах)» instead of «моложавый; юношески свежий (о голосе, манерах)»; example «— Мама говорит голосом, полным молодости.»
  instead of «— Мама говорит юношески свежим голосом.»; ぴんぴん appended to `quiz_exclusions`, now `[若い, 幼い, さわやか,
  ぴんぴん]`, after the post-fix screen found «полный» meeting ぴんぴん «полный сил; бодрый». The remedy's title «молодой
  облик; моложавый» was not used.
- `散らす` (line 21; comprehensibility C11, partial): «— Я посыпаю салат рубленым зелёным луком.» instead of «— Я
  раскидываю рубленый зелёный лук поверх салата.» The title «раскидывать; рассеивать» is unchanged.
- `花火` (line 21; comprehensibility C12, modified): «Это не дзюкудзикун (особое чтение всего слова целиком): каждый кандзи
  сохраняет своё собственное исконное чтение.» instead of «Это не дзюкудзикун: каждый кандзи сохраняет своё собственное
  исконное чтение.» Line 20's «(рэндаку)» is unchanged.
- `花火` (lines 15, 25 and 30; comprehensibility C13, partial): 手持ち花火 is glossed «фейерверки, которые держат в руке»
  instead of «ручные бенгальские огни» (line 15, and line 30's «для фейерверков, которые держат в руке, — 遊ぶ» instead of
  «для ручных бенгальских огней — 遊ぶ»); 線香花火 is glossed «тонкий бенгальский огонь из бумажного жгутика с порохом»
  instead of «маленькие бенгальские огни» (Daijisen 線香花火 1 via Weblio). The title «фейерверк» is unchanged.
- `芯` (lines 4 and 12; comprehensibility C14): title and H1 «сердцевина; грифель; фитиль» instead of «сердцевина;
  фитиль».
- `早速` (line 21; comprehensibility C15, modified): «— Спасибо за скорый ответ.» instead of «— Спасибо за быстрый
  ответ.», away from 速い's title «быстрый». The remedy's «без промедления» was not used.
- `落とし物` (line 20; comprehensibility C16): «…обратился за помощью на полицейском посту.» instead of «…обратился за
  помощью в полицейскую будку.», matching 交番 «полицейский пост».
- `撒く` (lines 4, 12 and 18; comprehensibility C17, modified; also consistency O2): title and H1 «рассыпать,
  разбрызгивать; ускользать от кого-либо» instead of «рассыпать, разбрызгивать; уходить от погони» (EN "give someone the
  slip"); line 18's redundant « — уходить от погони» is removed. The remedy's «отделаться от преследователя» was not used.
- `草履` (line 21; comprehensibility C19): «— Я надела дзори и вышла в сад.» instead of «— Я надел дзори и вышел в сад.»,
  consistent with «выбрала» on line 20. The remedy's plural forms were not used.
- `茂る` (line 20; comprehensibility C20): «— Когда наступает лето, листва на деревьях густеет.» instead of «— Когда
  наступает лето, деревья покрываются густой листвой.», making the foliage (木の葉) the subject.

Corrected inherited EN claims: correctness C2 (茂る: 滋る described as obsolete, EN 茂る:25) and correctness C4 (艶:
"glaze" attributed to the card's dictionary, EN 艶:45) are inherited from the frozen EN source. The RU cards are corrected
(茂る:28 reworded; 艶:45 deleted); EN is frozen and not changed, and the dispositions record C2 as "a corrected inherited
claim".

Declined or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Comprehensibility C6's line 31 was declined: «Отдельной карточки кандзи 艶 в нынешней коллекции нет.» is "inherited,
  true, explains the missing link (cf. 句読点:32)".
- C8's replacement «Она — человек широкой образованности.» was declined: «культурный» is "correct Russian for 教養のある人".
- C11's title change was declined: «раскидывать; рассеивать» is "faithful to "scatter"; the deliberateness note covers the
  concern; a change would ripple to 撒く/散る and B242".
- C12's «рэндаку» part was declined: "already explained inline and established in 9 corpus files".
- C13's title change was declined; the title «фейерверк» follows EN "fireworks".
- C18 was declined: "The parallel with 嫁:19 is inherited from EN; the contrast is stated at 33–34 and 39, and the Japanese
  sentences differ (花嫁 vs お嫁さん)".
- C21 was declined: «окуригана» is an "Established corpus term (325 RU files) and used by EN"; the follow-up is RU glossary
  entries for окуригана, рэндаку and дзюкудзикун.
- Consistency O1 was optional and "partly covered by C3": "EN 蒸し暑い:43–51 has no べたべた link, so no link is owed there;
  the remaining guards protect English labels only and stay as EN requires".
- Consistency O2 was declined in the dispositions ("The title gives the sense (shaking off pursuers); «отрываться от
  погони» is equally intransitive, and the body example 追っ手をまく shows the transitive frame"), but comprehensibility
  C17's accepted title change "also addresses consistency O2", and the consistency recheck judged O2 resolved.
- Consistency O3 (気体→物質, 落とし物→物) was declined: "The «вещество» overlap is inherited from EN (気体 "gas; gaseous
  substance" / 物質 "substance; matter", unguarded in EN); 物 «вещь; предмет» is a hypernym, not the meaning of 落とし物,
  and the specific title is the unambiguous answer in both directions".
- The correctness optionals (first-use explanations of годан/итидан/окуригана/дзюкудзикун, 散らす:21 «посыпаю», 花火:25
  «заряды») were "Deferred to the comprehensibility reviewer's verdict".

The coordinator's post-fix title screen of the six changed titles (`b240-postfix-screen.txt`; pool: the RU word titles)
prints 13 `OK` lines for guarded pairs and 61 stem-only `!!` lines. Its one exact shared segment is 著す–書く «писать»,
guarded by the EN pair on 著す; 若々しい's «полны» hit on ぴんぴん is guarded by the fix-1 addition. The dispositions
summarise the 61 unguarded stem-only lines (蒸す «готов»/«погод»/«влажн», 芸能 «навык»/«искус»/«испол», 著す
«писат»/«сочин», 若々しい «голос»/«полны») as "all different meanings or parts of speech", with "no guard added beyond
若々しい→ぴんぴん"; for 芸能's «навык» stem meeting マスター, 上達 and 訓練 they give "different parts of speech/meanings
(verb "master", "improvement", "training"); no guard added". The consistency recheck found that «грифель», «ускользать» and
«исполнительские» occur only in their own cards and that 著す «писать» = 書く is already excluded. The dispositions also
record a corpus grep of the RU primary checkout (words, kanji, articles) for the removed wording with no remaining quote,
the only hits being unrelated («исходный список» in kanji reading-table notes and ケーキ:41 «глазурь», cake icing). They
record `tools/build_manifest.py` (5,319 files, version `efb73b59212c9d63`), `tools/validate.py` 0 errors, the unit tests
(124) OK and the content budget (exit 0; 5,336 entries, local ZIP 7,671,457 B) in the post-fix state.

Net change from the candidate:
- titles and H1s of 蒸す, 芸能, 著す, 若々しい, 芯 and 撒く;
- example translations in 落第, 著す (two), 教養 (two), 若々しい, 散らす, 早速, 落とし物, 草履 and 茂る;
- prose in 茂る (lines 28–29), 蒸す (lines 41–43), 湿気 (line 18), 撒く (line 18), 花火 (lines 15, 21, 25 and 30), and
  the deletions of 艶:45 and 芸能:40;
- one appended exclusion (若々しい→ぴんぴん); none removed;
- one link added (蒸す:43 → べたべた, restoring EN :48's link to an existing card); none removed.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`d0d977c..3544d75 -- words` is sixteen word files, 35 lines added and 36 removed; with `manifest.json` the commit changes
17 files, 52 lines added and 53 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs;
the correctness recheck states "Model not verifiable.", the consistency recheck "model not verifiable from inside the
session", and the comprehensibility recheck "model not verifiable".

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. Each recheck covered the full diff `d0d977c..3544d75` (16 word cards and `manifest.json`). No recheck
raised a new finding, so there was no fix 2.

Each reviewer appended its recheck to its own report file. The correctness section records its scope as "all 16 changed
cards reread in full against the supplied changes and frozen EN 6af98cb" and that the "Actual word diff matches supplied
diff."; the consistency section records checks of the changed set, titles, exclusions, manifest hashes and
removed wording; the comprehensibility section reconciles each of its findings against the changed passages and lists
regressions checked.

All three rechecks state that no generator was run. The correctness reviewer states "No generator, validator or
repository write performed."; the consistency reviewer ran `validate.py` (0 errors) and records "tools/__pycache__
removed; status still clean"; the comprehensibility reviewer ran neither a generator nor `tools/validate.py`. The
correctness section records the requested full HEAD verified, parent `d0d977c` and a clean status at start and end; the
consistency section records HEAD `3544d75afb94d41fc2eccd74dd0df04a6a762b77` with a clean status; and the comprehensibility
section records HEAD `3544d75afb94d41fc2eccd74dd0df04a6a762b77`, parent `d0d977c` and an empty porcelain status. The
recheck records include no separate coordinator status check after the rechecks; when these records were drafted, a
read-only check showed the RU checkout on `full-ru-240-words-79` at HEAD `3544d75afb94d41fc2eccd74dd0df04a6a762b77` with
`git status --porcelain --ignored` printing nothing.

### Round 1 (`3544d75`)

| Facet | Scope and result |
|---|---|
| Correctness | Requested full HEAD verified, parent `d0d977c`, clean status at start and end; "all 16 changed cards reread in full against the supplied changes and frozen EN 6af98cb"; "Changed manifest hashes match file bytes; no removed links." C1 is **resolved**: 落第:20 «прошёл материал» "reports renewed study, not successful mastery" (Russian «пройти», educational sense 10, ru.wiktionary). C2 is **resolved**: 茂る:28's "rare spelling now matches JMdict 1533740". C3 is **resolved**: 蒸す:43's "existing-target べたべた link/contrast restored accurately". C4 is **resolved by deletion**: 艶:44–45 "surface quality/coating distinction remains; no dictionary conflation or material sense is introduced". Other changes "are at least as accurate semantically as the previously acceptable wording": 蒸す, 芸能, 著す, 若々しい, 芯 and 撒く keep their senses, 花火 "now accurately defines handheld fireworks and the paper-twist/powder form of 線香花火", and 教養, 散らす, 早速, 落とし物, 草履 ("gender change is permissible"), 茂る and 湿気 keep theirs. Evidence: current JMdict entries; Daijisen via Weblio for 芸能 (1–2), 線香花火 (1) and 手持ち花火. Optionals: 散らす wording resolved; term explanations partially resolved ("花火 glosses jukujikun"; "godan/ichidan/okurigana remain optional"); 花火 "salvos" "remains optional, not a defect". Correctness **CLEAN** and scoped coverage **CLEAN**; "No regression established." |
| Consistency | HEAD `3544d75`, clean status; diff from `d0d977c` = 16 word cards + `manifest.json`; `validate.py` 0 errors; no generator; manifest SHA-256 of all 16 changed cards match. Titles of 蒸す, 芸能, 著す, 若々しい, 芯 and 撒く "each match their H1 exactly". 若々しい `quiz_exclusions` = `[若い, 幼い, さわやか, ぴんぴん]` ("EN order kept, RU additions appended"), "so «полный молодости» is guarded". «грифель», «ускользать» and «исполнительские» "occur only in their own cards"; 芸能 «навыки» vs マスター/上達/訓練 "stays unguarded (unchanged from earlier; low risk, optional)"; 著す «писать» = 書く "already excluded". No orphaned removed wording; 落とし物 «полицейский пост» matches 交番. O1 "partially resolved" ("optional, no defect"); O2 **resolved** ("new title «ускользать от кого-либо», redundant body phrase removed"); O3 "withdrawn/optional". Consistency **CLEAN**, quiz safety **CLEAN** and scoped cross-file integration **CLEAN**; "No findings." Limits: "dictionary senses from memory". |
| Comprehensibility | HEAD `3544d75`, empty porcelain status, parent `d0d977c`; no generator, no `tools/validate.py`. C1 to C17, C19 and C20 are **resolved**, accepting the modified or partial dispositions (for example "Do not maintain deletion" for C1, "Do not maintain perfective title or high severity" for C7, "Do not maintain a title change" for C11, "Do not maintain expanding the title" for C13, "Do not maintain the narrower title" for C17); C18 and C21 are **withdrawn** ("contrast is already at 花嫁:33–34, :39 and 嫁:28; Japanese sentences differ"; "corpus term; glossary follow-up is the right place"). "Regressions: none. 落第 «прошёл материал» is renewed study, not passing." Comprehensibility **CLEAN** and scoped coverage **CLEAN**. Limits: "dictionaries not re-fetched". |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 落第:20 «заново выучил материал» asserts mastery (moderate) | **Resolved** | `落第.md:20`; EN "studied the material again"; Kuznetsov «выучить»; ru.wiktionary «пройти» sense 10. |
| Correctness C2: 茂る:28 calls 滋る obsolete (low; inherited from EN 茂る:25) | **Resolved**; EN claim corrected in RU only | `茂る.md:28–29`; JMdict 1533740 "rarely used kanji form". |
| Correctness C3: 蒸す lost EN :48's link to the existing card べたべた (low; scoped coverage) | **Resolved** | `蒸す.md:43`; べたべた:16–20; JMdict 1011440. |
| Correctness C4: 艶:45 attributes "glaze" to the dictionary (low; inherited from EN 艶:45) | **Resolved** by deletion (with comprehensibility C6) | `艶.md:44–45`; JMdict 1177680 sense 1; "glaze" is a KANJIDIC2 character gloss. |
| Correctness optionals: годан/итидан/окуригана/дзюкудзикун, 散らす «посыпаю», 花火 «заряды» | **Optional**; 散らす resolved, дзюкудзикун glossed, the rest optional at recheck | `散らす.md:21`, `花火.md:21`; "remains optional, not a defect". |
| Consistency classification: 散る→はらはら required; 散る→跳ねる and 若々しい→さわやか conservative | **Recorded**; all three pairs present | `散る.md:9`, `若々しい.md:9`; "No over-guarding found." |
| Consistency O1: six English-label guards on 蒸す and 蒸し暑い without in-card rationale | **Optional**; partially resolved at recheck, no defect | `蒸す.md:43` (べたべた contrast and link); EN 蒸し暑い:43–51 has no べたべた link. |
| Consistency O2: 撒く «уходить от погони» reads intransitive | **Resolved** (declined as proposed, addressed by comprehensibility C17) | `撒く.md:4,12,18`; "new title «ускользать от кого-либо», redundant body phrase removed". |
| Consistency O3: extra guards 気体→物質, 落とし物→物 | **Optional**; declined, withdrawn/optional at recheck | Overlap inherited from EN and unguarded there; 物 is a hypernym. |
| Comprehensibility C1: 湿気:18 «из исходного списка» has no referent (medium) | **Resolved** at recheck (modified: reworded, deletion not maintained) | `湿気.md:18`. |
| Comprehensibility C2: 蒸す:42 quiz-metadata sentence (medium) | **Resolved** (modified: non-interchangeability kept) | `蒸す.md:41–42`. |
| Comprehensibility C3: 蒸す's title long and stiff (medium) | **Resolved** at recheck (modified: «быть» kept; length not maintained) | `蒸す.md:4,12`; EN "steam food; be hot and humid". |
| Comprehensibility C4: 芸能:40 English «accomplishments» warning (medium) | **Resolved** | `芸能.md` (line 40 deleted); line 22. |
| Comprehensibility C5: 芸能's «достоинство» segment (medium) | **Resolved** at recheck (modified: «освоенные искусства и навыки»; shorter gloss not maintained) | `芸能.md:4,12`; 長所 «достоинство; преимущество»; EN "cultivated accomplishments". |
| Comprehensibility C6: 艶:45 «glaze» and 艶:31 card-set remark (medium) | **Resolved** at recheck (split: line 45 deleted; line 31 kept and not maintained) | `艶.md:44–45`, `艶.md:31`; cf. 句読点:32. |
| Comprehensibility C7: 著す's title and examples teach a state, not past acts (high) | **Resolved** at recheck (modified: imperfective title; perfective title and high severity not maintained) | `著す.md:4,12,19,20`; 書く excluded; EN "wrote"/"authored". |
| Comprehensibility C8: 教養:21 «Она образованный, культурный человек» (medium) | **Resolved** at recheck (partial: dash added, «культурный» kept; not maintained) | `教養.md:21`. |
| Comprehensibility C9: 教養:19 «расширить» for 深める (medium) | **Resolved** | `教養.md:19`; EN "deepen". |
| Comprehensibility C10: 若々しい «юношески свежий» (medium) | **Resolved** (modified: «полный молодости», plus 若々しい→ぴんぴん) | `若々しい.md:4,9,12,20`; 新鮮 «свежий»; ぴんぴん «полный сил; бодрый». |
| Comprehensibility C11: 散らす:21 «раскидываю» for a garnish (medium) | **Resolved** at recheck (partial: example changed; title change declined and not maintained) | `散らす.md:21`; line 16's deliberateness note. |
| Comprehensibility C12: 花火 «дзюкудзикун» and «(рэндаку)» unexplained (medium) | **Resolved** at recheck (modified: дзюкудзикун glossed inline; рэндаку not maintained) | `花火.md:20–21`; «озвонченная форма» on line 20. |
| Comprehensibility C13: 花火 手持ち花火 and 線香花火 both «бенгальские огни» (medium) | **Resolved** at recheck (partial: glosses distinguished; title expansion not maintained) | `花火.md:15,25,30`; Daijisen 線香花火 1; EN "fireworks". |
| Comprehensibility C14: 芯's title omits the pencil-lead sense (medium) | **Resolved** | `芯.md:4,12`; JMdict 1595120. |
| Comprehensibility C15: 早速:21 «быстрый ответ» uses 速い's title (medium) | **Resolved** at recheck (modified: «скорый»; «без промедления» not maintained) | `早速.md:21`; 速い «быстрый»; EN "prompt reply". |
| Comprehensibility C16: 落とし物:20 «полицейскую будку» (medium) | **Resolved** | `落とし物.md:20`; 交番 «полицейский пост». |
| Comprehensibility C17: 撒く «уходить от погони» omits the unwanted companion (medium) | **Resolved** at recheck (modified: «ускользать от кого-либо»; narrower title not maintained) | `撒く.md:4,12,18`; JMdict 1303400 senses 1–3; EN "give someone the slip". |
| Comprehensibility C18: 花嫁:19 same Russian frame as 嫁:19 (medium) | **Withdrawn** at recheck; declined | Contrast at 花嫁:33–34, :39 and 嫁:28; the Japanese sentences differ. |
| Comprehensibility C19: 草履 first-person examples switch gender (low) | **Resolved** | `草履.md:20–21`; "Both examples feminine." |
| Comprehensibility C20: 茂る:20 translates 木の葉 as «деревья» (low) | **Resolved** | `茂る.md:20`; "Subject is foliage." |
| Comprehensibility C21: «окуригана» not glossed (low) | **Withdrawn** at recheck; declined | Established corpus term (325 RU files), used by EN; glossary entries are a follow-up. |

Cross-batch note: links to absent targets stay plain. Fourteen EN link occurrences in this batch's new cards, to nine
targets, are absent from RU: 蒸発 → kanji 蒸, 気体 → 液体, 蒸す → kanji 蒸, 蒸気 → kanji 蒸, 湿度 → kanji 湿, 湿気 → kanji 湿
and 乾燥, 蒸し暑い → kanji 蒸, 撒く → 巻く, 蒔く → 巻く, 著す → kanji 著, 茂る → 枯れる, 芸能 → kanji 芸 and 早速 → さっさと.
The other written kanji without an RU kanji card, 嫁, 履, 撒, 暑, 第, 艶, 芯, 茂, 葬, 蒔, 養 and 駄, have none in EN either.
There is no RU-only link in the new cards. At the candidate 蒸す lacked EN :48's link to the existing card べたべた; fix 1
restored it at 蒸す:43 (correctness C3). The pre-existing RU-only links on kanji/花 to 北, 花瓶 and 花見 are untouched by
this batch (the candidate's navigation changes are bracket-only, and fix 1 changed no navigation file). No links were held
from Batch 239, and none is held from this batch. 葬式 excludes and links the Batch 239 card 儀式, whose title «церемония;
обряд, ритуал» is identical at the Batch 239 candidate and at the published baseline. The Batch 241 and Batch 242 lane
copies of 蒸す, 芸能, 著す, 若々しい, 芯 and 撒く predate fix 1; the dispositions record that "B241 must be based on published
B240, and B242 adjudication must re-check quotes of these titles". RU glossary entries for окуригана, рэндаку and
дзюкудзикун are on the follow-up list recorded in the dispositions; this record does not claim that any issue comment was
posted.

## Final exclusion set

All 132 EN exclusion entries (28 lists; 湿度 and 花火 have none in EN) are retained in EN order; 20 of them lie inside the
batch, and the other 112 target existing RU cards. Four direct, one-sided entries are added on two new cards, all appended
at the end of their lists: three from the candidate (from the authoring lane as adjudicated by the coordinator) and one
from fix 1 (若々しい→ぴんぴん, comprehensibility C10, precautionary after the post-fix screen). None was removed. The
coordinator classed the candidate entries as follows:

- Required (1): 散る→はらはら (はらはら «замирать от тревоги; плавно опадать», sharing the stem «опада»).
- Conservative (2): 散る→跳ねる (跳ねる «подпрыгивать; разлетаться брызгами (о воде, масле)») and 若々しい→さわやか
  (さわやか «освежающий; ясный и приятный (о голосе, манере)»).

The consistency reviewer classed the candidate entries the same way and found "No over-guarding found". At recheck it
confirmed 若々しい's list `[若い, 幼い, さわやか, ぴんぴん]`, "so «полный молодости» is guarded". Every RU addition is
appended at the end of its list, and no EN entry is removed or reordered. Android applies each declaration symmetrically,
so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (落第 C1, 茂る C2 and 艶 C4; C2 and C4 correct claims inherited from EN).
- Scoped coverage: **CLEAN** after fix 1 (蒸す C3 in the correctness review; 花火 and 著す in the comprehensibility
  review).
- Comprehensibility: **CLEAN** after fix 1 (湿気, 蒸す, 芸能, 艶, 著す, 教養, 若々しい, 散らす, 花火, 芯, 早速, 落とし物, 撒く,
  草履 and 茂る); the modified and partial dispositions stand as accepted, and C18 and C21 are withdrawn.
- Cross-file consistency: **CLEAN** throughout; the restored 蒸す → べたべた link and the six restored navigation links in
  four files stand.
- Quiz safety: **CLEAN** throughout, including the six retitles and the 若々しい→ぴんぴん addition. This covers the reviewed
  batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread the changed cards or passages and the lines needed to judge them; the unchanged cards rest on review
  001, in which all three reviewers read all 30 cards in full against EN.
- The correctness recheck used current dictionaries, "not historical captures", and is a "focused fix recheck, not a new
  native-reader/quiz audit". The consistency reviewer cited dictionary senses from memory and did not rerun the unit tests
  or content budget. The comprehensibility reviewer did not re-fetch dictionaries. Necessity classes are judgements, not
  measurements.
- The comprehensibility review read the navigation files as link-only diffs, ran `word_title_screen.py` as a lead only and
  did not run `link_parity.py`.
- The Russian usage of «дзори» was recorded as unverified (no Lopatin entry; gramota.ru HTTP 429); other ordinary Russian
  wording was not dictionary-checked by the coordinator.
- 花火 has no `quiz_exclusions` and no dictionary footer, mirroring EN's older card format.
- RU glossary entries for окуригана, рэндаку and дзюкудзикун are a follow-up, not decided by this batch.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `d0d977c`, not `3544d75`.
- Frequency and preferred register (for example «дзори», «гэта», «полный молодости», «ускользать от кого-либо», «скорый
  ответ», «прошёл материал») were not certified. Online dictionaries were current observations, not pinned archives. The
  app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
