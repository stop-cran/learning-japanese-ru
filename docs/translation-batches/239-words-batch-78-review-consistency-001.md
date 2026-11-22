# B239 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `39b6bd13afc5eec5371ce27cd611ce1ff581f19a` (tree `d966f81d76a25657d6aad60cb77733f2f9631bfd`),
> the signed candidate pushed before review.
> Later reconciliation is in `239-words-batch-78-recheck-001.md`.

Snapshot: RU `git rev-parse HEAD` = 39b6bd13afc5eec5371ce27cd611ce1ff581f19a (matches); `git status --porcelain` empty at start and at end. A run of `python tools/validate.py` created an untracked `tools/__pycache__/` and one of my commands (`build_manifest.py --help`) ran the generator, which rewrote manifest.json; I removed `tools/__pycache__/` and `git status` is clean again, so manifest.json was byte-identical (see Verdicts). I did not edit, stage, commit or switch anything.

Scope: Read in full against their EN originals (front matter, body, footer): all 30 new cards (清書 複写 裏口 裂く 被せる カバー 表紙 衣食住 街角 行列 儀式 行事 血液 血圧 蝋燭 コック 蛇口 蚊 虹 思い付く 蘇る 薬缶 薬指 薬局 薬品 薄暗い 薄める 蕎麦 栓 蓋). Read all nine navigation diffs in full (kanji/圧, 局, 薬; words/側, 虫, 蛇, 蛍, 蝶, 被る; 13 link occurrences). Manifest and intake JSON checked mechanically (hashes, path list). Facets: consistency, quiz safety, cross-file integration. Model: not verifiable from inside the session.

Verdicts:
- Consistency: CLEAN (validate.py 0 errors; no defect established).
- Quiz safety: NEEDS FIX (one low-severity missing guard, Q1; all EN guards retained; all 12 RU additions justified or conservative, none unnecessary).
- Cross-file integration (links, nav files, manifest, intake): CLEAN.

Findings:
- Q1; low; quiz safety; words/裂く.md:9: `quiz_exclusions` lacks びりびり. The existing RU card びりびり has the title «рвать в клочья; дребезжать; покалывание (током)» and its list guards 破る. 裂く has the title «раздирать на части; вспарывать» and the body «раздирать, разрывать». «Рвать в клочья» is a defensible correct answer for 裂く, so an ordinary quiz could present it as a wrong option. 裂く guards 破る, which is the same family, but not this card. Remedy: line 9 `quiz_exclusions: [破る, 割る, 切る, 離す, 分ける, びりびり]` (RU addition appended after the EN list). Basis: JMdict 1207730 sense 1 (裂く: tear, rend) against the onomatopoeic びりびり sense 'tearing noisily'. Necessity: conservative-to-required; confidence medium. Cheaper alternative if the author rejects it: leave as is. Not blocking learning content.

Classification of the 12 RU-introduced guards (each one-sided; all fit the one-direction contract):
- 清書→書き取り (words/清書.md:9): REQUIRED. 書き取り carries «переписывание (текста, кандзи)» and 清書 «переписывание начисто», so the whole word «переписывание» is shared and a learner could defend either. Basis: JMdict 書き取り (dictation; transcription/copying out) and 清書 1378240 sense 1.
- 被せる→履く (words/被せる.md:9): conservative. 履く «надевать обувь или одежду ниже пояса» shares «надевать» only as a prefix of a qualifier; 被る already guards 履く and 着る. Real basis, necessity unestablished; harmless.
- 衣食住→服 (words/衣食住.md:9): REQUIRED (the title lists «одежда» as its first element, the same segment as 服 «одежда»).
- 衣食住→衣服: conservative (衣服 «одежда в целом»; 衣食住 «одежда, еда и жильё»; EN links the two). Real basis; necessity not established.
- 衣食住→住宅: conservative (the «жильё» element is shared). Fine.
- 行列→番 and 行列→順番 (words/行列.md:9): REQUIRED (exact «очередь» shared; 番 «номер (по порядку); очередь», 順番 «очередь; порядок»).
- 血液→血 (words/血液.md:9): REQUIRED (exact «кровь»).
- 蛇口→水道 (words/蛇口.md:9): conservative. 水道 «водопровод; водопроводная вода» shares only the stem «водопровод»; titles already separate the device and the system. The body line explicitly teaches the contrast, but real confusion is unlikely; keep, no action.
- 蘇る→浮かぶ (words/蘇る.md:9): REQUIRED (not merely conservative): 蘇る «всплывать в памяти» and 浮かぶ «всплывать; приходить в голову» share the stem «всплыва». The memory sense of 蘇る (記憶が蘇る) and 浮かぶ (記憶が浮かぶ) are a defensible overlap.
- 薬品→農薬 (words/薬品.md:9): conservative (農薬 «пестициды…» are agricultural chemicals and 薬品 includes «химикаты»). Real basis; necessity unestablished.
- 栓→渋滞 (words/栓.md:9): REQUIRED (exact «пробка»; the body line 44 teaches the traffic sense, and the link is apt).
Over-guarding: none to remove. The author's "conservative" label for 清書→書き取り and 蘇る→浮かぶ underrates them; they are required.

EN guard retention (checked programmatically for all 30): every EN `quiz_exclusions` list is a prefix of the RU list in EN order (diffs show only the appended RU additions on 清書, 被せる, 行列, 蛇口, 蘇る, 薬品, 栓; 衣食住 and 血液 have lists made only of RU additions; 蝋燭, コック, 虹, 薬局, 蕎麦 have none in EN or RU). None dropped. Title-screen check: the exact whole-segment overlaps (надевать, одежда, очередь ×3, церемония, кровь, вентиль, вспоминать, пробка) are all guarded on at least one side. A scan of all RU titles (including 蛇口/コック/栓, 非常口, 南口/西口, 見送る, 実施, スケジュール, 紅茶, ペンキ) found no other defensible pair left unguarded except Q1. In-batch pairs without any guard (清書–表紙, 被せる–蓋, 被せる–表紙, 裏口–街角, 行列–行事, 行列–儀式, 血液–血圧, 薬缶–薬局, 薬局–薬品, 薬指–薬品, 薄暗い–薄める, コック–薬缶) are separated by their titles; no guard needed. One-way in-batch declarations (複写→清書, カバー→被せる, 表紙→カバー, 行事→儀式, 蛇口→コック, 蘇る→思い付く, 栓→蛇口, 栓→コック, 蓋→カバー, 蓋→栓) suffice under the direct-pair, symmetric-application contract; コック and カバー are covered from the other side. The declined stem-only pairs listed in the prompt are different senses or parts of speech; I agree with leaving them unguarded.

Titles: all fit their senses; none needs a change. 裏口 «чёрный ход» is neutral and the body (line 38) denies secrecy; 裂く second sense (仲を裂く) is covered in the body (line 22) although EN's title has no segment for it either; 被せる «накрывать; надевать (на голову другому)» covers the body's uses and the 被る.md sentence (line 36) on covering someone or something else; カバー «восполнение» fits カバーする; 表紙 «переплёт» is acceptable for EN 'binding'; 栓 «пробка» is protected by the 渋滞 guard and body line 44. Titles of the in-batch groups (被せる/カバー/表紙/蓋, 清書/複写, コック/蛇口/栓, 行列/儀式/行事, 血液/血圧, 薬缶/薬指/薬局/薬品, 薄暗い/薄める) let a learner tell them apart.

Consistency evidence (nothing to fix):
- Front matter: every field except `quiz_exclusions` and `title` is identical to EN for all 30 cards; all use the scalar/inline-list subset; headings follow `# 字（かな）— title` and the four RU section names in order; LF endings (eol=lf).
- Links: every EN card link either resolves to an existing RU file or is absent from RU only when the target is absent (下書き, 着せる, 液体, 気圧, 夜間, うどん confirmed absent and rendered as plain text; the glosses «черновик, предварительный набросок» and «атмосферное давление» read naturally and drop nothing). All kanji links match EN where the RU kanji file exists (書, 写, 口, 割, 表, 紙, 食, 住, 行, 列, 式, 事, 圧, 思, 付, 薬, 指, 局, 品, 暗); all other kanji files are absent in RU, as in the prompt. No link points to a missing RU file. The three RU-only links are apt: カバー→表紙 (line 43, the same comparison EN makes in plain text), コック→蛇口 (line 39), 栓→渋滞 (line 44, a Russian-only sentence on the traffic sense). Every other card link has an EN counterpart. Unlinked mentions with existing RU cards (帽子, 足りる, 沸かす, 閉める, 抜く, 開ける) occur only in examples or collocations, as in EN; no link needed.
- Footers: URLs and JMdict entry IDs are set-identical to EN in all 30 cards (Weblio/Kotobank links where EN has them).
- Nine navigation files: diffs touch only the 13 link brackets/hrefs at EN positions (圧:45; 局:22,33,39; 薬:22,33,37; 側:41; 虫:36; 蛇:28; 蛍:37; 蝶:39; 被る:36) with the EN path forms; no prose changed; the later 局 pronunciation mention (RU line 45) and 薬品 in 薬.md stay plain, as in EN. The pre-existing 局 → 郵便局 link is untouched. The glosses beside the new titles do not mislead: «кровяное давление», «аптека», «комар», «водопроводный кран», «гречневая лапша соба» (the 蕎麦 title also names гречиха; the 側 sentence is about the food, so no conflict); the 被る sentence is covered by the 被せる title «накрывать».
- Manifest/intake: `build_manifest.py` output equals the committed manifest.json (git status clean after run, version 05ed8b9a8d8bc80c); no stale hash; the intake JSON has 39 payloads, its path set equals the candidate's content diff (30 new + 9 nav), every candidateRawSha256 matches the working-tree bytes, and it adds no learner content.

Optional:
- 蓋.md:24 («Карточки иероглифа 蓋 пока нет») and 蝋燭.md:29 are statements that will go stale when those kanji cards arrive; they mirror EN (蓋.md:23, 蝋燭.md:29), so leave until the kanji translation batches revisit them.

Limits:
- I did not independently verify the JMdict/Daijisen entry numbers or senses against the live dictionary; I only checked parity of URLs and IDs with EN and the plausibility of senses from the card text. Dictionary evidence for Q1 is from general knowledge of 裂く and the RU card text of びりびり (confidence medium).
- Pre-existing RU-only links outside this batch (e.g. 局→郵便局, 側→近く/隣) were not evaluated.
- Linguistic correctness of Russian prose beyond consistency and quiz safety belongs to other facets.
