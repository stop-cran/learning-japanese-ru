# Batch 160 independent review 001

Reviewer: read-only `kanji-accuracy-reviewer` subagent (Claude, Anthropic), independent of authoring; report preserved as returned.

Snapshot: 256fd596756472f19a58479f21993b5bd04bd184 (RU working tree clean, equal to this commit). EN source 6af98cb.

Scope: All 13 RU kanji cards read in full and compared line by line with EN at 6af98cb; 13 stroke files; 8-word diff; intake JSON. Ran `tools/validate.py` (read-only): 0 errors, exit 0; tree still clean afterwards. Model: Claude (Anthropic).

Verdicts:
- **Strokes (13):** CLEAN. All 13 blob IDs match EN; working-file SHA-256 matches intake; `.gitattributes` `eol=lf -text`.
- **Words (8):** CLEAN. Word diff shows only the `[X](../kanji/X.md)` wrapper; every target exists.
- **Intake:** CLEAN (spot-checked hashes for 延, 承, 患 and all strokes). The "no other RU card lists any of the 13 as a distractor" claim holds: only 悩→快, inside the batch.
- **Links:** every EN word link whose target exists in RU is kept; the 25 targets missing in RU (延期, 伸びる, 規律, 回復, 恋, 担当, …) are plain text, acceptable.
- **Per card** (correctness / coverage / Russian):

| Card | Correctness | Coverage | Russian |
| --- | --- | --- | --- |
| 弱, 律, 復, 快, 技, 拝 | CLEAN | CLEAN | CLEAN |
| 延 | NEEDS FIX (F1) | CLEAN | CLEAN |
| 悩 | NEEDS FIX (F2) | NEEDS FIX (F2) | CLEAN |
| 承 | NEEDS FIX (F3) | CLEAN | CLEAN |
| 戸 | NEEDS FIX (F4) | CLEAN | CLEAN |
| 恋 | CLEAN | NEEDS FIX (F5) | NEEDS FIX (F5) |
| 担 | CLEAN | NEEDS FIX (F6) | NEEDS FIX (F6, F7) |
| 患 | CLEAN | CLEAN | NEEDS FIX (F8) |

- **Metadata:** strokes, grade, JLPT, on/kun with okurigana dots match kanjiapi (KANJIDIC) for all 13, except kanjiapi gives grade 5 for 承 while Jisho (current KANJIDIC2) shows grade 6, matching the 2020 MEXT revision; the card's `grade-6` is correct.

Findings:
1. **Minor; correctness; kanji/延.md:30.** 延べる glossed «…распространять…»; JMdict: "lay out; spread out; stretch; widen" and "postpone; extend". «Распространять» = disseminate, a meaning the verb lacks. Fix: `延べる のべる — расстилать; продлевать; откладывать`. Evidence: JMdict via Jisho API, 延べる senses 1–2. Confidence: high.
2. **Minor; correctness and coverage; kanji/悩.md:33 and :46.** Table gloss for sense 2 «тревожный; трудный»; the note then lists «тревожный» again as separate sense 3 ("anxious; uneasy"); contradiction, and the EN "sense 2" qualifier was dropped. Fix line 33: `悩ましい なやましい — мучительный; трудный (одно из значений)`; line 46: `У 悩ましい в JMdict есть также значения «соблазнительный; чарующий» и «беспокойный; встревоженный». «Мучительный; трудный» в таблице — второе значение статьи, а не полный перечень.` Evidence: JMdict via Jisho API, 悩ましい: 1 seductive/enchanting; 2 troubling/difficult/thorny; 3 anxious/uneasy. Confidence: high.
3. **Minor; correctness; kanji/承.md:46.** ウケる said to be used especially in colloquial «забавлять» ("amuse someone"); JMdict sense marked "esp. ウケる" is intransitive "to find funny; to be amused (by)" — direction reversed. Fix: replace «забавлять» with «находить смешным; забавляться». Evidence: JMdict via Jisho API, 受ける sense 7 [vi], colloquial, "esp. ウケる". Confidence: medium-high (EN "amusement use" is ambiguous).
4. **Minor; correctness; kanji/戸.md:48.** Comparison note glosses 戻 «возвращаться; отменять»; "cancel" is not a 戻 meaning (KANJIDIC re-/return/revert/resume/restore/go backwards) and contradicts the linked RU card title «возвращаться; возвращать». Fix: `Сравните с [戻](../kanji/戻.md) («возвращаться; возвращать»): …`. Confidence: high.
5. **Minor; coverage/adaptation; kanji/恋.md:43.** «В отдельной статье 恋 разбирается существительное こい», but `words/恋.md` does not exist in RU (true only in EN). Fix: `Как самостоятельное слово 恋 читается こい и является существительным.` keeping the rest. Evidence: `Test-Path words/恋.md` False. Confidence: high.
6. **Minor; coverage/adaptation; kanji/担.md:44.** «В статье о слове разбирается ответственность за порученную роль», but `words/担当.md` does not exist in RU. Fix: `Обычно оно означает ответственность за порученную роль или участок работы.` Confidence: high.
7. **Minor; Russian comprehensibility; kanji/担.md:42.** «его значение «нести на плече» не ограничивается переносным употреблением» is illogical; EN means the verb is not limited to the figurative sense. Fix: `担う имеет и переносное значение «нести ответственность», но не ограничивается им: буквально он означает «нести на плече».` Confidence: high.
8. **Minor; Russian comprehensibility; kanji/患.md:20.** «пациент …, а не человек, терпеливо ожидающий» carries over the English patient/patient pun; Russian «пациент» has no "терпеливый" sense. Fix: `患者（かんじゃ）— пациент, больной в медицинском смысле.` Confidence: high.

Quiz directions: all 39 safe; no distractor title (read from current RU cards) is also a correct answer for its prompt.

| Prompt (RU title) | Distractors (RU titles) | Verdict |
| --- | --- | --- |
| 延 «продлевать; откладывать» | 建 «строить», 庭 «сад; двор», 近 «близкий» | safe |
| 弱 «слабый; хрупкий» | 強 «сильный» (antonym), 弟 «младший брат», 引 «тянуть; вытягивать» | safe |
| 律 «закон; ритм» | 待 «ждать», 建 «строить», 洋 «океан; западный стиль» | safe |
| 復 «восстанавливать; повторять» | 待 «ждать», 得 «получать; приобретать», 彼 «он» | safe |
| 快 «приятный; комфортный» | 決 «решать; определять», 怖 «страшный», 忙 «занятой» | safe |
| 恋 «романтическая любовь; тоска» | 変 «изменение; странный», 忘 «забывать», 急 «срочность; внезапность» | safe |
| 患 «недуг; страдать от болезни» | 中 «середина; внутри», 思 «думать; чувствовать», 息 «дыхание» | safe (中's "be affected" sense not in its title) |
| 悩 «беспокоиться; мучиться» | 怖 «страшный», 忙 «занятой», 快 «приятный; комфортный» | safe |
| 戸 «дверь; счётное слово для домов» | 石 «камень», 戻 «возвращаться; возвращать», 店 «магазин» | safe |
| 承 «принимать; соглашаться» | 水 «вода», 手 «рука», 了 «завершение; улаженность» | safe (了's "understand/consent" sense not in its title) |
| 技 «навык; мастерство» | 支 «поддержка; ответвление», 持 «держать; иметь», 抜 «вытаскивать; вынимать» | safe |
| 担 «нести на плечах; брать на себя» | 指 «палец; указывать», 押 «толкать; нажимать», 招 «приглашать; подзывать» | safe |
| 拝 «поклоняться; кланяться с почтением» | 持 «держать; иметь», 指 «палец; указывать», 押 «толкать; нажимать» | safe |

- **Changed titles:** «недуг; страдать от болезни», «принимать; соглашаться», «навык; мастерство» are unique among RU kanji titles. Nearest neighbours 病 «болезнь», 痛 «боль; болеть», 苦 «горечь; страдание», 受 «получать; подвергаться», 喫 «употреблять; принимать внутрь», 術 «техника; способ» are in no distractor relation with the changed cards in either direction. KANJIDIC supports each change: disease (患), acquiesce (承), skill/art/craft (技).
- **Kept EN overlaps:** 律/法 «закон» and 復/再 are not distractors of each other in either direction; harmless today.

Optional:
- 恋 (lines 31, 37): 恋しい glossed as the noun phrase «тот, по кому тоскуют»; consider «(такой,) по которому тоскуют; которого не хватает».
- 拝:45: «скромно увидеть» could be misread as "catch a modest glimpse"; consider «видеть (скромная форма; о высоком лице или вещи)».
- 拝 (拝見 note): add «или его стороны» to keep EN's "own side".
- 延 table: EN label "prefix" dropped; consider «(приставка перед счётным словом или единицей)».
- Dropped secondary glosses: 弱い «хрупкий», 弱視 «нарушенное зрение», 回復 «выздоровление»; mostly covered, optional.
- 戸 note: EN hedge "ordinary" dropped, making «не к отдельным дверным полотнам» categorical.
- JLPT label: this batch uses «общественный учебный список», 92 existing N2 RU cards use «список сообщества»; consider consistency.
- 患 title «недуг»: no example shows the noun sense (EN has none either); 疾患 would be an addition beyond EN.

Limits:
- JMdict checked through the Jisho API (EDRDG JMdictDB web requires a password).
- KANJIDIC checked through kanjiapi; its 承 grade is stale, cross-checked with Jisho.
- Radical 64 for 承 confirmed on Jisho only; the other 12 match EN and standard Kangxi but were not fetched individually.
- Not re-opened: the jōyō PDF claim for 承 (ショウ, うけたまわる only) and the alternative 7-stroke count for 延; both inherited from EN.
- 恋う UNVERIFIED: Jisho's JMdict copy lists only "to love"; the card's "love; miss" comes from EN, not the RU translation.
- No native-speaker or app runtime check.
