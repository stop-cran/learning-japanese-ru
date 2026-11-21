# B230 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5ec190a7c89f162bdb1673eca213fab94aab9624` (tree `6d3c31bd01596be9b29662885a4d2cae61c73bac`),
> the signed candidate pushed before review.
> Later reconciliation is in `230-words-batch-69-recheck-001.md`.

Snapshot: RU 5ec190a7c89f162bdb1673eca213fab94aab9624, C:\Users\romanko\repos\learning-japanese-ru; HEAD verified, status --porcelain empty; no uncommitted content. EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f. No repository modifications.

Scope: Independent blind correctness/scoped-coverage review; actual model unverifiable; no nested reviewers. Read all three binding RU references. Each listed card was read in FULL against its FULL frozen EN original:
- C:\Users\romanko\repos\learning-japanese-ru\words\長男.md:1-44
- C:\Users\romanko\repos\learning-japanese-ru\words\四角.md:1-34
- C:\Users\romanko\repos\learning-japanese-ru\words\四角い.md:1-38
- C:\Users\romanko\repos\learning-japanese-ru\words\正方形.md:1-44
- C:\Users\romanko\repos\learning-japanese-ru\words\長方形.md:1-46
- C:\Users\romanko\repos\learning-japanese-ru\words\長所.md:1-49
- C:\Users\romanko\repos\learning-japanese-ru\words\継続.md:1-45
- C:\Users\romanko\repos\learning-japanese-ru\words\長引く.md:1-52
- C:\Users\romanko\repos\learning-japanese-ru\words\長女.md:1-43
- C:\Users\romanko\repos\learning-japanese-ru\words\鑑賞.md:1-50
- C:\Users\romanko\repos\learning-japanese-ru\words\鐘.md:1-35
- C:\Users\romanko\repos\learning-japanese-ru\words\録音.md:1-51
- C:\Users\romanko\repos\learning-japanese-ru\words\錆.md:1-32
- C:\Users\romanko\repos\learning-japanese-ru\words\錆びる.md:1-33
- C:\Users\romanko\repos\learning-japanese-ru\words\銅.md:1-42
- C:\Users\romanko\repos\learning-japanese-ru\words\鉱物.md:1-47
- C:\Users\romanko\repos\learning-japanese-ru\words\丼.md:1-49
- C:\Users\romanko\repos\learning-japanese-ru\words\鉢.md:1-46
- C:\Users\romanko\repos\learning-japanese-ru\words\鉄砲.md:1-33
- C:\Users\romanko\repos\learning-japanese-ru\words\鉄橋.md:1-33
- C:\Users\romanko\repos\learning-japanese-ru\words\鈴.md:1-43
- C:\Users\romanko\repos\learning-japanese-ru\words\仕上がる.md:1-34
- C:\Users\romanko\repos\learning-japanese-ru\words\イコール.md:1-45
- C:\Users\romanko\repos\learning-japanese-ru\words\整備.md:1-46
- C:\Users\romanko\repos\learning-japanese-ru\words\揃える.md:1-48
- C:\Users\romanko\repos\learning-japanese-ru\words\揃う.md:1-50
- C:\Users\romanko\repos\learning-japanese-ru\words\釣り合う.md:1-35
- C:\Users\romanko\repos\learning-japanese-ru\words\針金.md:1-49
- C:\Users\romanko\repos\learning-japanese-ru\words\課程.md:1-35
- C:\Users\romanko\repos\learning-japanese-ru\words\過程.md:1-35
Also read existing RU words\ちゃわん.md, words\ベル.md and words\合う.md in full for conventions/comparisons; inspected the ベル link-only change and manifest diff. Did not read the prohibited drafts, author/reviewer reports, tracking file or RU batch records.

Verdicts: correctness NEEDS FIX (鈴 title only, C1 below); correctness CLEAN for the other 29 cards within this bounded review. Scoped coverage CLEAN for all 30: no missing EN teaching point, example, citation or required existing-target link established. Russian comprehensibility and comprehensive quiz safety were not assigned and receive no overall verdict.

Findings:
C1; Minor; correctness; C:\Users\romanko\repos\learning-japanese-ru\words\鈴.md:4,12 (compare :16,38-39). The unqualified title «бубенчик» narrows the source's “bell (often globular)” to the spherical/rattling subtype. This is a SHAPE restriction, not a claim that a large shrine bell cannot be a бубенец. The body correctly denies a universal shape/size rule, but the standalone learner title does not retain that breadth. Remedy: broaden title and H1 together, for example «колокольчик; бубенец; храмовый колокол», retaining the present shape/use explanation and direct guards with ベル and 鐘. If another shorter label is chosen, verify that it does not make the spherical construction compulsory.
Evidence: actual Digital Daijisen すず【鈴】 at https://www.weblio.jp/content/鈴, sense 1 defines the slit hollow sphere, explicitly including large shrine examples; sense 2 also records the hanging-bell shape with a suspended tongue (風鈴の類). Actual Kuznetsov entries at https://gramota.ru/poisk?query=бубенчики&mode=slovari and https://gramota.ru/poisk?query=бубенцы&mode=slovari define БУБЕНЧИКИ as =Бубенцы and БУБЕНЦЫ as hollow metal balls with metal pieces inside. Thus size alone is NOT grounds for rejection; the narrower construction is. Frozen EN title and :38-40 explicitly preserve the prototype/non-universal distinction. Confidence: high in the lexical distinction; medium-high in the learning impact, hence Minor.

Optional: Outside the assigned facets, a small comprehensibility improvement at C:\Users\romanko\repos\learning-japanese-ru\words\録音.md:31: «Сохраняйте все четыре моры (ритмические единицы): ろ・く・お・ん; не выбрасывайте く». This avoids an unexplained «слога-моры». Do not present this as a proven wrong count or as proof that no syllabic analysis of morae exists: Daijisen モーラ【mora】 (https://www.weblio.jp/content/モーラ) distinguishes phonetic syllables from morae, while Rybin's actual 2009 article discusses a deep phonological syllable/mora analysis (https://cyberleninka.ru/article/n/sootnoshenie-slog-mora-i-problema-slogodeleniya-v-sovremennom-yaponskom-yazyke). Four morae and the supplied segmentation are correct.

Evidence and dispositions:
- Inspected actual Jisho/JMdict forms, senses, restrictions and POS for all 30 headwords; イコール matched on reading. Independently checked all 30 word pages' “Edit in JMdict” IDs against the cards: all agree. Excluded Wikipedia blocks and the 長所 place-name homonym. Initially failed API requests were subsequently successful.
- Inspected full-page rare-form Notes for 錆 (銹/鏽), 鉱物 (礦物), 鉄砲 (鉄炮), and the forms/restrictions for 銅. Rare labels match; 銅 sense 2 is restricted to どう and marked abbreviation. No invented archaic restriction occurs in RU. Checked 仕上る and つり合う/釣合う in the actual forms. 錆びる is ichidan/intransitive; 長引く, 揃う, 仕上がる and 釣り合う have the stated godan classes; 継続 permits both transitivities.
- Read actual body-level Daijisen headings for 四角/しかく, 四角い, 長方形, 鑑賞, 鉢/はち, 鉄橋, 鉄砲 and 鈴/すず. 四角's な/の attachment, 四角い's noun-plus-adjective formation, the inclusive rectangle definition, artistic appreciation, Sanskrit pātra via 鉢多羅, specialized firearm senses and the separate 鉄灸 reference are supported. 鑑賞's そのよさを味わう supports the Russian enjoyment wording; it does not require favorable reviewing. The kango remarks identify collection classification rather than deriving ultimate etymology or metal composition from the tag.
- Read actual Russian definitions: Wiktionary темпура includes instrumental темпурой; благоустройство includes providing necessary conditions/equipment; техобслуживание covers servicing machines; уравновешиваться and соразмерный support equilibrium/proportion. Gramota's actual Бабенко череп entry explicitly gives «черепная коробка» as a synonym; Kuznetsov достоинство supports a positive quality, not necessarily moral goodness. Wiktionary горшок explicitly covers cooking and growing flowers; курс has a separate route/direction sense. These support the adapted distinctions without categorical substitution bans. The actual Russian Hokkaido University page uses «магистерской программы» and «докторской программы»: https://www.let.hokudai.ac.jp/en/ru. No equivalence to a Russian doctoral degree is asserted by the card.
- For патра, read the actual Russian Princeton-dictionary-derived entry naming pātra and 鉢: https://www.dharmata.ru/index.php/Патра. For донбури, observed the spelling and bowl/dish use in actual Russian running text at https://www.syl.ru/post/home-and-family/182206; this is usage evidence, not normative dictionary registration. The card supplies an independent Russian description, so learners do not depend on recognizing the loanword. Звоночек is documented as a diminutive of звонок in the actual Wiktionary entry. Итидан/годан spellings occur in the actual Russian teaching text https://kellenok.github.io/cure-script/ru/5-verb-groups-and-the-%E3%81%A6-form.html; grammatical class verification itself rests on JMdict, not that page's broader claims. Канго/онное чтение and Дайдзисэн are transparent transcriptions of the corresponding Japanese terms/source name, not new etymological evidence.
- Reviewed all translations for tense/aspect, polarity, roles and event/result distinctions. Contextually supplied pronouns, masculine pasts, number choices and result-state translations do not teach Japanese gender/possessor rules. «Расследование», «никак не проходит», «должна быть готова», «бронзу», «в сборе» and the chair example are defensible here; non-literal wording alone is not a defect.
- Paired full reads retain the EN senses and teaching rules, including the English-dependent adaptations. Machine cross-check: all original metadata fields except translated titles agree; original exclusions are retained, with the three disclosed RU additions for 丼/鉢/過程. No EN link whose RU target exists is dropped. All full Japanese sentence strings found in EN are retained unchanged; readings and other Japanese material were additionally checked in the paired reads. Parenthesis layout is localized without changing the kana. Untranslated-target pointers remain permissible plain text, not broken links. 整 really has no RU kanji card.
- Read-only validation: python -X utf8 -B C:\Users\romanko\repos\learning-japanese-ru\tools\validate.py returned exit 0, «0 error(s)». No manifest generator run. Structural success is not linguistic certification.

Limits: Complete paired review of these 30 cards, not the entire comparison pool, a corpus study or native-speaker/device certification. Some initial returns failed or truncated; only successful actual entries and bounded returned passages support the conclusions. No normative-dictionary registration established for донбури/патра; separately identified usage/history evidence supports those adaptations. Syllable/mora terminology is optional because analyses differ. Only C1 is a required correction.
