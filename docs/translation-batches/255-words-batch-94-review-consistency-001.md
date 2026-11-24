> Original blind consistency report on `8f4707c36e5d79d004c808e633c03c2cfaa4ae11` (tree `02468341eec95db807578daf86fd723a98478e6e`).
> Completed runtime: `claude-opus-5.5`, agent `8231b23d-2231-45c6-8669-d7bc2814c2f7`. The report body below is unchanged apart from LF line endings (the saved original used CRLF).
> [Coordinator reconciliation](255-words-batch-94-independent-review-001.md) and [scoped rechecks](255-words-batch-94-recheck-001.md).

# B255 blind review — CONSISTENCY + QUIZ SAFETY (+ integration coverage)

Snapshot: 8f4707c36e5d79d004c808e633c03c2cfaa4ae11 (branch romanko-microsoft-russian-batch-255, parent 650d466). `git rev-parse HEAD` matched and `git status --porcelain` was empty at start and end; no uncommitted changes reviewed. EN reference: frozen 6af98cb717755690a9ca793e5454a96ebd7a8f9f (clean worktree / `git show`).

Scope: facets consistency, quiz safety and integration coverage only. Model: not verifiable from inside the session.
- Read in full, RU paired with EN, every line returned (sample dir): words/ 汁, 水素, 水筒, 水平, 水平線, 水分, 気圧, いってらっしゃい, 元気でね, おだいじに, 気を付ける, 公共, 公衆, 民間, 歌謡, 民謡, 毛皮, 比較的, 毎度, 殻, ステージ, 段階, いちいち, 残らず, 死体, 歯車, 歯磨き, 正門, 正味, 欧米 (30/30).
- Read in full: inputs/b255-navigation-diff.txt (kanji/圧, words/お帰り, 地平線, 垂直, 毛糸, 羊毛, 血圧, 西洋, 門 — 9/9); inputs/b255-mechanical-facts.md; intake part of the candidate diff (ruAddedQuizExclusions, unavailableSourceLinkTargets, ~L680-782).
- Rules read: RU content-structure, content-format-reference, translation-methodology; EN content-format exclusions, EN confusable-words.
- Checks run: `tools\validate.py` → "0 error(s)", exit 0, no __pycache__; link_parity.py (39 files); word_title_screen.py (220 stem leads reviewed by hand); own read-only sweeps: all RU titles, EN→RU link debt, RU exclusions naming batch words, related RU/EN front matter and footers, sample dictionary glosses.

Verdicts: correctness (consistency + quiz safety) NEEDS FIX — one minor missing pair (F1) and low-severity over-guarding (F2); format, links, navigation and manifest CLEAN. Coverage (integration) CLEAN. Russian comprehensibility: not assigned.

Findings:
- F1; minor; quiz safety + consistency; words/ステージ.md:9 (title L4, body L16, example L20). Defect: the title «эстрада; выступление на сцене» and the body (L16 «само выступление на сцене, шоу»; L20 彼らのステージ → «их выступление») teach the performance sense. RU 演説 «публичная речь; выступление» (L9 [話]) has the independent gloss «выступление», a defensible answer for ステージ in that sense. スピーチ «выступление перед слушателями» (L9 [演説, 話]) also describes a stage performance. No direct pair exists on either side. The overlap is introduced by the Russian labels: EN "stage; performance" vs "speech; public address" / "speech; short address" do not overlap. Corpus precedent: RU 公演 «выступление артистов; спектакль» L8 adds [芝居, 演説, スピーチ] beyond EN for the same «выступление» overlap. Impact: a quiz can mark a defensible choice wrong. Remedy: L9 → `quiz_exclusions: [舞台, 公演, 演技, 演奏, 芝居, 水準, 演説, スピーチ]` (演説 required; スピーチ conservative). Evidence: JMdict 1070320 s2 "performance; show" (sample dictionary capture); RU 演説 / スピーチ / 公演 front matter. Confidence: medium (演説), low–medium (スピーチ).
- F2; low; quiz safety (over-guarding) + consistency; words/水平線.md:9, words/歯車.md:9, words/欧米.md:9. Three RU-added pairs guard contrasts the article itself teaches, and the other label is not a defensible answer:
  - 水平線–地平線: L31 teaches land vs water horizon, and both labels carry those qualifiers. EN ("water horizon; horizontal line") has no pair. JMdict 1372060 s1 "horizon (related to bodies of water)" vs 1421440 s1.
  - 歯車–車輪: L33 says «колесо транспортного средства, а не обязательно шестерня», and the 車輪 label «колесо (поезда, автомобиля, велосипеда)» excludes a gear. JMdict 1313350 s1 "gear; cogwheel" vs 1323280 s1 "wheel".
  - 欧米–欧州/ヨーロッパ: L36 says they «называют Европу, а не обе части 欧米»; «Европа» is only part of the connected label «Европа и Америка» (instruction rule on connected labels). JMdict 1609390 "Europe and the United States; Europe and America; the West" vs 1181190 / 1137570 s1 "Europe". The rationale is also inconsistent: アメリカ «Америка; США», equally contained in the label, is not guarded.
  - Impact: no wrong key; the pairs remove taught distractors and leave an uneven rationale.
  - Remedy: 水平線 L9 → `quiz_exclusions: [線, 水平, 横]`; 歯車: delete L9 (EN has no exclusions); 欧米 L9 → `quiz_exclusions: [西洋]`. If the author keeps the Europe pairs as deliberate conservatism, make it consistent instead: `quiz_exclusions: [西洋, 欧州, ヨーロッパ, アメリカ]`.
  - Confidence: medium (this applies the brief's taught-contrast criterion; harmless either way).

RU-added exclusions (12; basis → classification). All EN exclusions are retained in all 30 cards.
1. 水平線+地平線: both JMdict "horizon" (1372060 s1 / 1421440 s1) → unjustified (F2).
2. 水平線+横: 横 1180570 horizontal sense vs «горизонтальная линия» (footer cites Daijisen for the geometric sense) → conservative (mirrors EN 水平–横).
3. いってらっしゃい+さようなら: 2088750 s1 "have a good day; take care; see you" vs 1291050 "goodbye"; the Russian «счастливо» is itself a farewell answer for さようなら → required (translation-introduced; medium).
4. 元気でね+さようなら: 2847540 s1 "take care"; «всего хорошего» is a standard rendering of さようなら → required.
5. 元気でね+元気: 1260720 "healthy; energetic"; containment explained at L26; not a defensible answer → conservative.
6. 公衆+観客: 1273900 s1 "the public" vs 1214810 s1 "audience; spectator"; the bare «публика» in the 観客 label is a defensible answer for 公衆 → required (translation-introduced).
7. 民間+私立: 1528630 s1 "private; non-governmental" vs 1311420 "private (establishment)"; L34 teaches the difference → conservative.
8. 比較的+比較: 1483600 s1 "comparatively" vs 1483560 s1 "comparison"; adverb vs noun, derivation explained at L28 → conservative (form-based).
9. 歯車+車輪 → unjustified (F2).
10. 正味+中身: 1377980 s4 "actual content; useful part" (body L36 «настоящее содержание») vs 1599430 s1–3 "contents"; parallels the EN 内容 guard (EN 中身 and 内容 share the title "contents; substance") → required (body-taught sense).
11–12. 欧米+欧州, 欧米+ヨーロッパ → unjustified (F2).

Missing-pair screen (no further required pair found):
- Pairs already guarded: 汁–ジュース/スープ, 水分–湿気, 気圧–圧力/大気/空気, 水筒–瓶, 段階–段/一段/ステージ, 残らず–全て, 毛皮/殻–皮, 正門–門, 死体–体.
- Pairs judged distinct as whole labels: 気圧–血圧, 水平線–直線, 段階–通過/過程/至る, 公共–公園, 民間–個人/国民/私鉄, 毎度–度/感謝/いらっしゃい, いちいち–次々/順番, おだいじに–治る/回復 (wish formula vs verb/noun), 正味–量 (EN parity), 毛皮–革, 比較的–割合/対する/関する.

Consistency:
- All 30 cards keep EN field order. Only the title changes, plus appended exclusions where listed.
- H1 follows `# 語（よみ）— title`; kana-only H1s match EN (いちいち, いってらっしゃい; ステージ keeps （ステージ） as EN does).
- All cards use the standard Russian H2s and JMdict footer lines.
- Readings are in kana; no transcription or terminology conflict with neighbouring RU cards noticed.
- Links: every EN link resolves to an existing RU target or is left as plain text where RU lacks it (kanji 筒 線 欧 門 磨 階 比 毛 皮 革 血; word 公式). No link points to a missing file.
- link_parity: no lost links. One extra link, ステージ→段階, is a valid RU-only link into the batch. 毛糸→毛 and 門→ドア/入口 are pre-existing extras on unchanged lines.
- Commit: 41 files (30 cards, 9 navigation files, manifest, intake); nothing unrelated.

Integration:
- The 9 navigation files change only link brackets/hrefs at EN-parity positions, with the same line count and no prose change.
- 32 EN content files link the batch words. Every RU counterpart that exists (17) now links them. The other 15 have no RU file yet (kanji 欧 比 毛 皮 磨 筒 線 門 階; words いってまいります, レベル, 一斉, 割と, 割合に, 各々), so there is no current link debt.
- No existing non-batch RU card names a batch word in `quiz_exclusions`. The pairs inside the batch (民謡→歌謡, 民間/公衆→公共…, 残らず→いちいち, the farewell cluster) are consistent.

Optional:
- 欧米–西 «запад»: RU 西洋 «западный мир» guards 西, while 欧米 («западные страны»; JMdict "the West") does not. The 西 body (L40-42) itself separates the geographic «запад» from the cultural «Запад». I judge «запад» not a defensible answer for 欧米, so no pair is required; adding 西 would only give parity with 西洋.
- 元気でね–健康 «здоровье; здоровый»: same «здоров» containment as the 元気 pair; not a defensible answer. Add it only if the 元気 pair is kept on that rationale.
- いってらっしゃい «счастливо» vs 幸せ «счастливый»: different words, and the parenthetical disambiguates.
- 歌謡–作品 and 歯磨き–クリーニング: hypernyms, no pair needed.
- Future: EN 割と / 割合に link 比較的; check pairs when those RU cards appear.
- Outside my facets: 水筒 L36 «Во 水筒 наливают» is awkward; 水平線 «горизонтальная линия» rests on Daijisen, not the JMdict capture.

Limits:
- No web or JMdict re-fetch. Batch-side senses come from the sample dictionary captures; other-side senses come from RU footers and titles.
- The title screen is heuristic, and the stem leads were judged by hand, so non-lexical confusions may be missed. No app quiz was run, and necessity labels are reviewer judgment.
- The intake gives no per-guard rationale.
- The manifest and the non-intake parts of the candidate diff were not reread line by line; manifest consistency rests on validate.py.
- Protocol disclosure: I briefly wrote the title-screen output to reports\b255-review-consistency.screen.txt (FILES, not a repository), then deleted it and confirmed it was gone. The harness auto-saved one oversized tool output under %LOCALAPPDATA%\Temp (not my write). No repository writes; HEAD and index unchanged.
