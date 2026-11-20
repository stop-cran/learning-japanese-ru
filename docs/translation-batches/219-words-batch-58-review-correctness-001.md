# B219 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `f72537721d86b0d72485aecb4a758b10ef241a20` (tree `ea1be965b31c1cc36dc04bbe0cacaaacc3b3e6b5`),
> the signed candidate pushed before review.
> Later reconciliation is in `219-words-batch-58-recheck-001.md`.

Snapshot: RU f72537721d86b0d72485aecb4a758b10ef241a20, against parent e2ff1803b9f9db1fcb7084b1130bbe9e4b15e8f3; HEAD matched and git status --porcelain was empty. No uncommitted changes included. Translation comparison: local frozen EN 6af98cb.

Scope: BLIND, read-only correctness and scoped coverage; model ID not independently verifiable; no delegation. Each item below attests COMPLETE RU and frozen EN reading, including metadata, examples/readings, explanations and sources:
- words/以前.md — full RU + EN.
- words/代表.md — full RU + EN.
- words/代理.md — full RU + EN.
- words/付き合い.md — full RU + EN.
- words/仏.md — full RU + EN.
- words/今後.md — full RU + EN.
- words/今回.md — full RU + EN.
- words/今にも.md — full RU + EN.
- words/人込み.md — full RU + EN.
- words/人種.md — full RU + EN.
- words/人生.md — full RU + EN.
- words/人工.md — full RU + EN.
- words/交際.md — full RU + EN.
- words/互い.md — full RU + EN.
- words/事実.md — full RU + EN.
- words/事務.md — full RU + EN.
- words/予算.md — full RU + EN.
- words/予測.md — full RU + EN.
- words/予報.md — full RU + EN.
- words/乗客.md — full RU + EN.
- words/乗せる.md — full RU + EN.
- words/主要.md — full RU + EN.
- words/主義.md — full RU + EN.
- words/主張.md — full RU + EN.
- words/主婦.md — full RU + EN.
- words/主に.md — full RU + EN.
- words/中止.md — full RU + EN.
- words/中学.md — full RU + EN.
- words/丘.md — full RU + EN.
- words/世間.md — full RU + EN.

Also read in full: RU 最近, 今に, 事務所, だけ, 本人, 天気予報, 以来. Sampled metadata/meaning/examples only: これから, ほとんど, まず, もうすぐ, 一緒, 中学校, 乗る, 予想, 予期, 代わり, 前, 仕事. Inspected navigation-only diffs for all three changed kanji and 15 existing changed words, and 以/際 reading metadata. No author/reviewer/batch records or other session files were read.

Verdicts: correctness NEEDS FIX (minor localized exceptions: 主義, 今にも, 人込み); scoped coverage CLEAN for all 30 cards and the reviewed ancillary changes. Correctness CLEAN for the other 27 new cards within this bounded review. Comprehensibility and comprehensive quiz-safety review are not assigned and receive no verdict.

Findings:

C1; Minor; correctness; words/主義.md:19.
The Japanese 彼は自分の主義を変えませんでした and EN “He did not change his principles” describe not changing one's principles. RU “Он не изменил своим принципам” instead uses изменить + dative: not betraying/abandoning one's principles. This is a natural Russian expression, but it imports a loyalty judgment and changes the lexical/argument-structure lesson for 変える. A person can revise a principle without “betraying” it.
Remedy: “Он не изменил свои принципы.”
Evidence: actual JMdict/Jisho 変える entry, sense 1 “to change; to alter; to transform,” https://jisho.org/api/v1/search/words?keyword=変える; Kuznetsov, ИЗМЕНИТЬ 1 “кого-что. Сделать иным; переменить” versus ИЗМЕНИТЬ 2, sense 3 “кому-чему ... Нарушить верность чему-л.” with the exact example “И. своим принципам”, https://gramota.ru/poisk?query=изменить&mode=slovari&dicts[]=42.
Confidence: high; localized impact, not a reversed overall interpretation.

C2; Minor; correctness; words/今にも.md:29.
The RU-only comparison ends “оно [今に] не описывает того, что уже вот-вот произойдёт.” This turns a useful difference in emphasis into a categorical ban on describing a sufficiently near event with 今に. The dictionary allows a near-future inference from the present sky, including rain; the distinction is that 今にも specifically foregrounds apparent immediacy, whereas 今に need not. The rest of the 今にも explanation and its past-impression example are accurate.
Remedy: replace the final clause with “оно само по себе не подчёркивает непосредственную близость события так, как 今にも.”
Evidence: Digital Daijisen 今に, sense 1 “近い将来に関する推量または決意” and actual example この空では今に雨が降る, https://kotobank.jp/word/今に-435873; 今にも “目前に何かが起こりそうなさま。すぐにも。今まさに”, https://kotobank.jp/word/今にも-435878. JMdict 今に likewise gives “before long”, not a prohibition on an imminent referent.
Confidence: high; no claim of free substitution.

C3; Minor; correctness (gloss scope/register); words/人込み.md:4,12,16.
Unqualified “толчея” is stronger than “толпа”: it names jostling/crush, not merely people densely gathered. It is also colloquial. The EN title and Japanese entry teach the general crowd, while the RU body supplies no restriction for this added alternative. This risks making pushing/disorder part of the word's definition. The main gloss “толпа” and both example translations are sound.
Remedy: use “толпа людей” as title/H1 gloss. Alternatively retain “толчея” only as a contextual, colloquial translation, explicitly noting that 人込み itself does not require толкотня.
Evidence: JMdict 人込み/人ごみ/人混み, sense 1 “crowd of people”, https://jisho.org/api/v1/search/words?keyword=人込み; Kuznetsov ТОЛЧЕЯ 1, sense 1 “Разг. Давка, толкотня”, https://gramota.ru/poisk?query=толчея&mode=slovari&dicts[]=42; Wiktionary толчея I.1 explicitly describes people pushing each other, https://ru.wiktionary.org/wiki/толчея.
Confidence: high on Russian scope/register; impact minor because the broader correct gloss leads the title.

Evidence and coverage dispositions:
- Inspected actual lexical JMdict/Jisho entries for all 30 words and six added-link targets: forms, POS, restrictions and info, excluding Wikipedia blocks. だけ was verified through 丈/だけ after an exact-spelling selector missed it. Added comparisons preserve their teaching point, subject to C2.
- Source metadata and EN exclusions survive; only title localization and added guards differ. No EN link to an existing RU target was dropped; missing-target pointers correctly remain plain text. Citations, Japanese examples and teaching rules survive. English-only remarks are appropriately omitted; restored 以来→今後 is accurate.
- 代表 “представительство” is supported in the activity sense, not just an office: Kuznetsov sense 2 “Выполнение обязанностей представителя”, https://gramota.ru/poisk?query=представительство&mode=slovari. 代理 “заместитель” has the general substitute sense, not solely a permanent deputy post: Universal Dictionary 1.0, https://gramota.ru/poisk?query=заместитель&mode=slovari. Neither title by itself establishes an erroneous office/job restriction.
- 予算 “смета” matches a prospective cost estimate: Wiktionary sense 1, https://ru.wiktionary.org/wiki/смета. 事務 “канцелярская работа” matches clerical work: actual канцелярский entry, https://ru.wiktionary.org/wiki/канцелярский. 交際 retains both general association and dating, not merely isolated dates.
- 世間's news example permits “внимание общественности”; “люди в целом” and the body retain everyday social judgment. Общественность is narrower (“Часть общества, активно участвующая ...”): https://gramota.ru/poisk?query=общественность&mode=slovari. No lost taught sense established; no unrestricted equivalence claimed.
- Russian “искусственный” really has the transferred “деланый, неискренний” sense (Wiktionary sense 3), https://ru.wiktionary.org/wiki/искусственный. Temporal назад is attested separately as a postposed expression with “Десять лет (тому) назад”, https://ru.wiktionary.org/wiki/назад. 以前's advice is qualified against mechanical substitution, not a claim that no dictionary ever glosses 以前 as “ago”; JMdict actually does so.
- “Хозяйка дома” is explicitly limited to household management, consistent with хозяйка's domestic-skills sense, https://ru.wiktionary.org/wiki/хозяйка. 専業主婦 is correctly explained at line 20; actual Daijisen defines 職に就かないで、家事に専念する主婦, https://kotobank.jp/word/専業主婦-186707. 中学 retains the lower-secondary stage and abbreviation and follows the existing 中学校 terminology; this is not a claim of identical foreign grades.
- Verified 仏's uses/ホトケ note, 乗客's readings, 乗せる's class/載せる-only publication restriction and preserved ゴ in 互い. No annotation leakage. Masculine first-person Russian examples are contextual renderings, not male-only Japanese meanings.

Optional: Nonblocking Russian-register polish: “того и гляди” is colloquial but semantically supports imminence, https://ru.wiktionary.org/wiki/того_и_гляди. “Предварительная оценка” is more neutral than “оценка наперёд” (Kuznetsov: “Нар.-разг.”, sense 2 “Заранее”), https://gramota.ru/poisk?query=наперёд&mode=slovari. Прогнозирование denotes making a forecast; companion оценка retains the result sense, https://ru.wiktionary.org/wiki/прогнозирование. 主婦:17 could use “не занималась оплачиваемой работой” instead of conventional “не работала вне дома”; line 20 already gives the correct distinction.

Limits: No exhaustive corpus/frequency, native-speaker, quiz-option or app/device validation. Batch/progress records intentionally unread. HTTP 429/403 failures were replaced by working actual entries. An initial oversized card read was not credited: all 30 RU/EN pairs subsequently returned completely in bounded calls. A misdirected Kotobank URL returned 医伯 and was discarded; the correct 今に entry was located by search and fetched.

Validation: python -X utf8 -B tools\validate.py, run from the primary RU checkout, printed “0 error(s)” and exited 0. No generator, edit, staging, checkout, commit, push or posting occurred in any repository. Only this report was written.
