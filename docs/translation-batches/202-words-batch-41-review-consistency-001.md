# B202 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `fdf29ba137faa929ab8a81876d0e252c83d1c416`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 201 tree `7d283bd` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `202-words-batch-41-recheck-001.md`.
> Two passes: the first returned report read 7 of the 30 cards in full. At the coordinator's request, the same
> reviewer session then read the other 23 cards in full on the same tree and updated this report in place.

Snapshot: candidate tree fdf29ba137faa929ab8a81876d0e252c83d1c416 (base 7d283bd) in C:\Users\romanko\repos\learning-japanese-ru-b198. Confirmed: `git diff-index --cached --quiet` exit 0, `git diff --quiet` exit 0, no untracked files. Diff = 44 files (30 new words, 13 navigation files, manifest.json), nothing else.
Scope: all 30 new word cards. Full RU body read, 7 in pass 1 (演奏, 溺れる, 火曜, 深刻, 流行, 灰, 消防) and the remaining 23 in pass 2 (炎 火災 運河 濠 滞在 滅多に 満足 湾 温暖 気温 体温 温度 減る 減らす 清潔 涙 消費 海外 流れる 流れ 活用 活動 泳ぎ), each checked against EN front matter, links and dictionary line (and EN body for 濠). Pass 2 checked: terminology/notation against RU repo usage (な-прилагательное, итидан/годан, する-глагол, атэдзи, Онные чтения), titles/readings cited for linked cards against those cards, section headings, one `Словарь:` line with JMdict entry/sense numbers identical to EN, plain-label handling. Also 13 navigation-only diffs (-U0), manifest and quiz screen. Facets: consistency, quiz safety, cross-file integration. Model: not verifiable from inside this session.
Verdicts:
- Consistency: NEEDS FIX (one minor notation finding F1 in 温暖; all other cards CLEAN)
- Quiz safety: CLEAN (no missing required guard; extra exclusions classified below)
- Scoped cross-file integration: CLEAN
Findings:
F1; minor; consistency; words/温暖.md:16; "Это na-прилагательное" uses Latin "na-" in running Russian text, the only occurrence among the 2713 RU word cards (149 other cards use "な-прилагательное", including 深刻 and 清潔 in this batch); impact: inconsistent terminology, trivial learner impact. The EN source says "na-adjective", so this was a literal carry-over. Remedy: replace `Это na-прилагательное, которое может работать и как существительное.` with `Это な-прилагательное, которое может работать и как существительное.` (front-matter tag `na-adjective` is correct and unchanged). Evidence: grep of words/*.md (1 hit vs 149). Confidence: high.
Evidence summary:
1. Format: all 30 cards have front matter fields matching EN (word, reading, jlpt, type, kanji, tags); the only differences are Russian titles and added quiz_exclusions. H1 equals `（reading）— title`; all use the 4 standard sections; each has one `Словарь:` line. `tools/validate.py` reports 0 errors.
2. Links: for each of the 30 new cards and 13 touched files, the multiset of link targets in RU is a subset of EN's (no Russian-only link). Every EN link missing in RU has no RU target file (checked: kanji/灰 河 湾 温 減 清 涙 防 管, words/木曜 宿泊 汗 インク 不足 夜中 俳優 do not exist). No restored link is broken. The 13 navigation diffs change only bracket/href at EN link positions (流, 満, 不平, 不満, 傾向, 増す, 日中, 流す, 演技, 管, 納得, 絶滅, 行動); no prose change.
3. Manifest: all 4174 entries hash-match worktree bytes for kanji/words (the 118 `strokes/*.json` "mismatches" are CRLF autocrlf checkout artefacts in this worktree; those entries are unchanged from base). Added exactly 30 entries, removed 0, no unlisted runtime file. contentVersion changed. No generated/unrelated files.
4. Title screen: exact whole-title or segment collisions with other RU cards occur only for 炎/火, 火曜/火曜日, 溺れる/沈む, 温暖/暖かい, 清潔/きれい, 深刻/大変·重大·まじめ, 泳ぎ/水泳 and 火災/火事 (after stripping parentheticals); every one has a direct exclusion on one side (EN-inherited or RU-added). Exclusions are symmetric-by-app, so no reverse declarations are required. All EN exclusions are retained (炎, 濠, 清潔, 温暖, 温度, 減らす, 深刻, 海外, 流れ, 活用, 泳ぎ).
5. Other candidate pairs in the dense clusters (灰/灰皿·煙, 運河/川·河, 湾/海·港·海岸·湖·池, 滞在/泊まる·下宿·過ごす·渋滞, 満足/不満·不平·納得·うれしい·十分, 減る·減らす/増える·増す·少ない·下がる·下げる·絶滅·節約, 涙/泣く·流す, 消費/費用·使う·節約, 流れる·流れ/流す·管, 活用/用·適用, 活動/行動·運動·働き, 消防/火事·消す·消える, 気温/体温·熱) have different POS, different object, or a contrast the article teaches; no title would be a defensible answer for the other. Not required.

Added exclusions beyond EN (basis / necessity):
- 火災→火事: JMdict 火災 (fire, conflagration) and 火事 (fire, e.g. building fire) are the same event in ordinary use; bare «пожар» segment equals 火事's whole title. REQUIRED.
- 火曜→火曜日: identical title «вторник»; precedent 金曜→金曜日. REQUIRED.
- 溺れる→沈む: both «тонуть»; 沈む's title segment equals. REQUIRED.
- 深刻→まじめ: shared segment «серьёзный» (まじめ: serious, earnest). REQUIRED (EN pairs 重大/大変 retained).
- 深刻→真剣: 真剣 sense "serious (about)", 深刻 sense 2 "serious (expression/thought)". Real overlap, necessity not established because titles differ («серьёзно настроенный»; 真剣 already guards まじめ/重大/大変 itself). CONSERVATIVE.
- 滅多に→たまに: たまに «изредка» vs «редко»; JMdict たまに "occasionally; once in a while; rarely". Defensible answer in a Russian quiz. REQUIRED-leaning (at least conservative).
- 滅多に→たま: たま (rare, infrequent, 1 sense in the existing card) vs «редко»; adjectival «редкий» vs adverb. CONSERVATIVE.
- 演奏→公演: JMdict 公演 covers public performance of plays, music, dance; 演奏 is music performance; a concert could be called either. CONSERVATIVE.
- 演奏→演技: 演技 "performance (acting, a routine)" vs 演奏 "musical performance". Titles share "исполнение" only; the article itself teaches the distinction. CONSERVATIVE bordering on UNJUSTIFIED; harmless.
- 温暖→ぽかぽか: ぽかぽか «приятно тёплый» vs «тёплый (о климате)»; ぽかぽか already guards 暖かい/温い. Real but weak basis. CONSERVATIVE.
- 体温→熱: JMdict 熱 includes "temperature; fever; body temperature" sense in common usage (e.g. 熱を測る). CONSERVATIVE.
- 温度→熱: 熱 "heat; temperature (of a thing)". CONSERVATIVE.
- 流行→人気: JMdict 流行 includes "popularity; vogue" in the fashion sense; 人気 «популярность». CONSERVATIVE (article teaches the distinction, but a quiz could treat «мода»/«популярность» as near).
- 流行→広がる: noun «массовое распространение» vs verb «распространяться». Different POS; CONSERVATIVE.
- 流行→回り: 回り carries the «распространение» sense in its title (JMdict 回り, spreading). CONSERVATIVE.
- 泳ぎ→泳ぐ: 泳ぎ is the nominalised form of 泳ぐ; parallel to retained EN pairs 流れ→流れる and 減らす→減る. CONSERVATIVE.
None classified UNJUSTIFIED as a mere antonym/contrast or topical relation; none is harmful (extra exclusions only reduce distractor pool).
Optional: 濠.md omits two EN sentences that are project-internal source notes ("The N2 source gives both 'moat' and 'canal'" and the sentence on 堀/濠 sharing entry 1522060 with the retained N3 level). Their omission loses no learner-facing rule (the 堀-spelling, 壕/濠 and canal-sense statements are kept), so this is nonblocking; leave as is unless the batch rule requires verbatim parity of source notes.
Pass-2 checks with no defect: reading/title citations of linked cards match (e.g. 火 ひ, 火事 かじ, 煙 けむり, 川 かわ, 河 かわ, 池 いけ, 泊まる とまる, 不満 ふまん, 増える ふえる, 外国 がいこく, 国内 こくない, 水泳 すいえい, 泳ぐ およぐ, 流す ながす, 浮く うく); plain-label cases (宿泊, 湾 入り江, 汗, 木曜, 寒冷, 不潔, 浪費, 消火, 増やす, 減少) are all absent as RU targets and plain in EN; I did not verify reading-of-plain-label accuracy beyond the card prose; dictionary entry/sense numbers identical to EN for all 30 cards.
Limits: Linguistic correctness is outside this facet and was not independently verified in pass 2 beyond noticing no inconsistency with EN. No online dictionary re-fetch was done in this review; dictionary senses are cited from the card text/JMdict knowledge and the existing RU cards' titles, so the CONSERVATIVE/REQUIRED grades for the added exclusions rest on that and on RU title strings, not on a quiz simulation. All 30 card bodies were read in full (pass 1 and pass 2), but only against consistency criteria, not as a correctness review. `strokes/*.json` hashes could not be verified from CRLF worktree bytes (unchanged from base). No app (Words.kt) run was performed.
