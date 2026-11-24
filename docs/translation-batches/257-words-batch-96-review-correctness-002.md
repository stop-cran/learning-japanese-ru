# B257 RU (word batch 96) — Japanese correctness / source-coverage facet, original read-only review

## Snapshot
- RU candidate bd3cb7293fa63d0b8ad59692524d561e2df91678, tree 8b50554614afa6e0e4d5f91895425ced03b43387, parent 8ddfa6793f162d6e896a91417d81b77c511df39e; RU read only from E (candidate-bd3cb729 raw-blob export). Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f; checkout HEAD verified, clean.
- Inventory SHA256 d6a27d79…1078d verified; 104/104 packet files re-hashed, 0 mismatches.
- No file written or edited, no agent launched, no other RU checkout or .copilot path read; no uncommitted files involved. Runtime-observed model identity: unavailable.

## Scope (actual reads)
- All 31 paired P\*.md read completely, RU and EN blocks (each ≤7202 B, none truncated): 有料 月給 下旬 月末 書道 書籍 更ける 曲線 捩る 工夫 捻る 曲げる 曖昧 普及 昼寝 映す 写る 映る 明け方 早口 日陰 日課 日時 日程 日用品 光線 日差し 日当たり 日帰り 日の出 汗. After a context compaction I re-extracted all 63 bulleted examples RU/EN side by side, re-read 日程 and 明け方 in full and the decisive lines of 曲げる 写る 映る 工夫 日時 日陰 日当たり 日差し 光線 書籍 捩る 普及 書道.
- P\corrections\汗.md.diff; all 5 P\navigation diffs (6 link insertions).
- All 31 P\dictionary and 31 P\facts packets; the 3 P\supplemental locator files, every pointer resolved with git show 6af98cb (18 Weblio/ACA locators; all 17 cited-JMdict comparison families). P\word-metadata-pool.json: one targeted query (dawn/sunrise titles). P\current-title-screen.txt: not relied on.
- Fresh in-memory fetches, nothing saved: ACA 2014 report PDF (924697 B, SHA256 57ad033d…c0d3fb = frozen hash; entry 025 + footnote, PDF p.12 / printed p.8); Weblio Daijisen 有料, 日程, 日時, 明け方; JMA 予報用語「時に関する用語」; Jisho API 汗する.
- E: words/曲る.md (plus frozen EN words/曲る.md); existence of every link target in the 30 new cards and the 6 navigation links.
- Every JMdict entry/sense citation in the 31 cards matches EN and the packets.

## Verdicts (this facet)
- Correctness: no material Japanese factual error found within the boundary. Readings, godan/ichidan class, transitivity, sense/spelling restrictions (日陰 S2 only 日影/日かげ; 日当たり S2 only 日当たり/日当り; 曲げる 枉げる [rK]), search-only forms (陽射, 昼寐), variant readings/spellings (つきずえ, しょじゃく, はやぐち, 速口, 日蔭, 日当り/陽当り), 有料 toll-road abbreviation, 普及 vt/vi, homograph 工夫 こうふ, 日時 S2 (Daijisen 「ある長さの日数と時間」), 日程 «намеченные даты» (Daijisen 「また、日どり」) and the ACA 写/映 statements match sources. One Low new-translation wording defect changes a spelling-status statement (F1).
- Coverage: substantially complete; every EN example, gloss, comparison and limitation has a RU counterpart except source-list provenance clauses (O1). English-only notes are adapted soundly (光線: EN beam=桁 / light=軽い note replaced by notes on the examples; 日程: "agenda" caution re-targeted to «повестка дня»).
- Russian comprehensibility, as it bears on facts: adequate. Numbers, polarity, tense and roles are preserved in all 63 examples (e.g. 月給 «двести пятьдесят тысяч иен», 下旬 «с двадцать первого числа до конца месяца», 写る «получилось нечётким», 早口 «не смог разобрать»).
- 汗 correction (RU l.32): accurate improvement. AFTER «В первом примере человек вспотел — 汗をかく, а во втором вытер пот — 汗を拭く» matches 暑くて、たくさん汗をかきました / タオルで汗を拭きました; BEFORE and EN said the examples use 汗をかく — an inherited inaccuracy, now fixed. 汗する exists in JMdict (Jisho: あせする, vs, vi).
- Navigation: the 6 links (明け方 ×2, 曲線 ×2, 写る, 映す) target the new RU cards; gloss text unchanged.
- Layout: the 30 new cards keep EN's sentence/reading layout (`- 文。 (よみ。) — перевод`; 書籍/捩る wrap to a second line as in EN); inline readings use RU （）. 汗 keeps its pre-existing RU layout `文。（よみ。）— …`, untouched by the diff.

## Findings
1. Low — words/曲げる.md RU l.30, new translation drift.
   Claim: «Карточка этого слова сохраняет устойчивую запись 曲る.»
   EN l.30: "The linked article retains its stable written ID 曲る." Dropping "ID" turns a note about the article identifier into a spelling claim (曲る as the established form).
   Consequence: contradicts the linked card — E words/曲る.md: «曲る — словарное написание 曲がる. В обычном письме используется более полное 曲がる»; frozen EN 曲る.md calls 曲がる "the ordinary spelling"; the same line itself writes 針金が曲がった.
   Correction: «Ссылка ведёт на карточку с идентификатором 曲る; обычное написание — 曲がる.» (or delete the sentence).
   Evidence: the two 曲る.md files above. Confidence: medium-high.

## Optional
- O1 Coverage, provenance only: 工夫 RU l.34 omits EN l.35 "The source list mixes the worker gloss with the くふう reading; the reading-specific dictionary entry resolves the mismatch" (the archived 工夫 locator confirms the mismatch); 月末 RU l.37 omits "the source list's" before げつまつ. No Japanese fact lost; restore only if RU keeps source-list caveats.
- O2 写る RU l.40 «…допустимо 映る — и при воспроизведении записи, и во время прямой трансляции». The ACA 025 footnote allows 「ビデオに映る姿」 for playback and 「防犯ビデオや胃カメラなど，撮影と同時に画像を再生する場合も…「ビデオに映る」と書くこともできる」. «прямая трансляция» (broadcast) falls under that principle but is less exact than EN "simultaneous live display" and RU 映る l.42 «изображение с камеры в реальном времени». Possible: «…и когда изображение с камеры показывается одновременно со съёмкой (камера наблюдения, гастроскоп)». Confidence medium.
- O3 書道 RU l.19: 書道を習っています → «занимаюсь каллиграфией» drops 習う (EN "take calligraphy lessons"); «хожу на занятия каллиграфией» keeps it.
- O4 明け方 (no error): RU frames the word as pre-dawn — title «предрассветное время», l.19 «под утро, перед рассветом», l.22 «небо перед рассветом» — vs EN "dawn; daybreak / around dawn / at dawn". Supported by Daijisen 「夜の明けようとするころ…[補説]気象庁の天気予報等では、午前3時頃から午前6時頃までをさす」, JMA (明け方 3–6時; 夜明け前 → 明け方) and JMdict "usu. 3:00–6:00 a.m."; l.16 «время около рассвета» keeps the broader sense. Pool check: 夜明け «рассвет; утренняя заря» is excluded, 日の出 «восход солнца…» stays distinct. Existing kanji glosses (方 «рассвет», 明 «время около рассвета») differ from the new title — consistency facet.

## Limits
- Live Daijisen checked only for 有料, 日程, 日時, 明け方; other Weblio/Daijisen claims rest on archived frozen locator records.
- JMdict records outside the packets (2463120 汗する, 1239730 曲る) not checked against the pinned version.
- No native-speaker or corpus/frequency evidence; naturalness of inherited examples (e.g. 地域にスポーツを普及しています, 日時を費やす) rests on JMdict vt/vi and Daijisen sense 2 「―がかかる」, not usage counts.
- Quiz exclusions/distractors, title-screen collisions and unlinked targets (籍 線 普 課 汗 ねじ 日の入り have no RU card in E) belong to other facets.
- Not device/media/voice/activation clearance. Stopping here; resumable for a bounded recheck.