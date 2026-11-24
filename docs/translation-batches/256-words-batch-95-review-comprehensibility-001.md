> Original blind return on `599b9e5b657468ea8c26bd651fe5cc9a4493ce64`, tree `7e2bfc4cc9e0807265347f39c79863b1fab22498`.
> Russian comprehensibility and scoped coverage. First dispatch and report-producing response: `grok-4.7`; reviewer `3749ffd7-8b4a-4efc-8740-346de4c8f21e`.
> [Reconciliation](256-words-batch-95-independent-review-001.md) and [scoped rechecks](256-words-batch-95-recheck-001.md). Original report body follows.

# B256 Russian comprehensibility and scoped EN-to-RU coverage

Snapshot: candidate 599b9e5b657468ea8c26bd651fe5cc9a4493ce64 (tree 7e2bfc4cc9e0807265347f39c79863b1fab22498), parent b604235935e67b74fa98cf9bfabb9d979554473f. EN frozen 6af98cb717755690a9ca793e5454a96ebd7a8f9f. Blind packet only. Runtime model id: not supplied in this prompt.

## Scope

Read in full, both RU and EN, every numbered line of these pair dumps (RU line counts): 次ぐ 53, 欠伸 43, 欄 45, 櫛 34, 機関車 35, 構造 49, 楕円 48, 山林 34, 森林 48, 桁 44, 校舎 44, キャンパス 38, 校庭 48, 枯れる 49, さすが 50, 果たして 47 (EN 45), ナンバー 45 (EN 46), 枚数 37, 枕 37, 東西 43, 東洋 50, 来日 46, 杉 33, 本部 35, 本来 38, 末っ子 33, 未満 47, 望遠鏡 40, 朗らか 37, 有無 43.

Navigation diffs, full hunks: articles/numbers-and-counters.md changed line 305; kanji/伸.md:43; kanji/欠.md:64; words/柳.md:29; words/桐.md:32; words/生える.md:38; words/茂る.md:36.

current-title-screen.txt: view lines 1–40; first whole-file view truncated at 59.1 KB; recovered by parsing all 334 lines. facts read in full: 未満, 東西, 本来, 構造. Partial: 森林 and 山林 (through related titles), 校舎 (through 学校 title), 朗らか (exclusions only). Dictionary JSON and frozen-sources packet not read. No other session-state files. No file edits.

## Verdicts

- Russian comprehensibility: NEEDS FIX
- Scoped EN-to-RU coverage: NEEDS FIX
- Assigned navigation diffs: CLEAN
- Answer-label distinguishability (checked neighbors): CLEAN
- Family consistency inside this set (山林/森林/杉; 校舎/校庭/キャンパス; 東西/東洋; 桁/枚数/ナンバー/未満): CLEAN

## Findings

1. Severity: medium. Facet: comprehensibility. File: words/さすが.md:45.
Exact text: «в английском все три значения передаются словом still, но по-японски это разные слова.»
Hinders: the three-way contrast with まだ and じっと is pinned to the English word still. A learner who does not know English cannot use that bridge; the foreign word sits in the nuance paragraph.
Replacement: «Это уступительное «всё же», а не «всё ещё, до сих пор», как まだ, и не неподвижность, как じっと. По-японски это разные слова.»
Source: EN line 45, localized everywhere else in this card. Confidence: high.

2. Severity: medium. Facet: comprehensibility and coverage. File: words/本来.md:18.
Exact text: «Изначально цель была не в этом.»
Japanese: これは本来の目的ではありません。 EN line 18: «This is not the original purpose.»
Hinders: the example turns attributive 本来の into a past-time adverb. The same card (lines 16 and 36) says 本来 is not just an earlier event. A phone reader can learn the parse the note warns against.
Replacement: «Это не изначальная цель.»
Source: paired EN line 18 and the Japanese example. Confidence: high.

3. Severity: low. Facet: comprehensibility. File: words/構造.md:44.
Exact text: «Английский перевод pattern в словаре относится к схеме расположения частей»
Hinders: pattern is unexplained English. The useful ban on calling 構造 a decorative узор is in the next clause and remains readable; the first clause does not.
Replacement: «Словарный смысл «схема расположения частей» не повод называть 構造 любой декоративный рисунок или узор.»
Source: EN lines 44–45; nearby excluded labels 模様 «узор; обстановка», 柄 «рукоятка; узор» (facts/構造.json). Confidence: high.

4. Severity: low. Facet: comprehensibility. File: words/東洋.md:43.
Exact text: «Старый английский перевод the Orient в словаре тоже указывает на это региональное понятие.»
Hinders: the sentence’s only new pointer is the English name the Orient. Lines 44–46 already say, in Russian, that this is not one country and not a fixed border.
Replacement: delete the sentence, or «В словаре это то же региональное понятие, уже описанное выше.»
Source: EN line 43. Confidence: high.

## Optional

- words/校舎.md:39–40 is grammatical but elliptical («Различить, входят ли в здание…»). Clearer: «Окружающие слова о месте помогают отличить вход в здание от пребывания где-то на территории школы.» Low impact; the contrast with 校庭 is already clear.
- EN links dropped while the gloss remains: 構造.md 造 and 工事; 山林.md 林; 森林.md 森 and 林; 枯れる.md 枯; 杉.md 杉; 次ぐ.md ついで. Navigation cost, not a missing sense.
- words/朗らか.md:19 «открыто засмеялись» adds a shade EN does not have. «Дети жизнерадостно засмеялись.»
- words/枕.md:16,19 «ракуго» is unexplained; the зачин sense does not depend on it.
- words/杉.md:16 Latin *Cryptomeria japonica* is neither Russian nor Japanese; the Russian names already carry the meaning.
- words/さすが.md:41 «даже мне» follows EN «even I»; the Japanese clause does not name the speaker. Not a separate RU defect.

Checked and not treated as collisions (shared word is not enough): 未満 «меньше (не включая границу)» vs 以下 «не больше; нижеследующее» vs 以上 «не меньше; вышеизложенное»; 森林 «лесной массив» vs 山林 «лесистые горы; лесные угодья» vs 林 «лес; роща»; 校舎 «здание школы» vs 学校 «школа»; 東西 «восток и запад» vs 東 «восток» / 東洋 «страны Востока; восточный мир»; 構造 «внутреннее устройство; конструкция» vs 装置 «устройство; аппарат». 本部 «головной офис» only mechanically overlaps «голова»; the labels are not interchangeable.

Assigned nav lines only wrap an existing gloss with a link to the new card. Glosses match: 桁 «три цифры, или три разряда»; 欠伸 «зевок»; 杉 «криптомерия (японский кедр)»; 枯れる «засыхать; увядать». No new learner-facing defect in those hunks. Old prose outside the changed lines was not reviewed.

## Limits

Not a native-speaker certification and not a learning-outcome claim. Japanese dictionary claims were not re-audited against external sources; no separate Japanese fact finding. Title-screen !! marks were used only as a label inventory, not as semantic verdicts. Unread: remaining facts/dictionary JSON, frozen-sources packet, worktree copies, author notes.