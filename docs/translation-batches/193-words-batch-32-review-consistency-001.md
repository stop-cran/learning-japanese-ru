# B193 consistency and quiz-safety review (batch `193-words-batch-32`)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `8fd47e7ccd776202db66e8f088d806a7693c02ac` (tree `a970b95cf288742a0ad921983505596e806124c4`),
> the signed candidate pushed before review.
> Later reconciliation is in `193-words-batch-32-recheck-001.md`.

Snapshot: RU branch full-ru-193-words-32, HEAD 8fd47e7ccd77 (parent 58c84bc), working tree clean (confirmed before and after review; my tool runs left nothing). Frozen EN 6af98cb. `tools/validate.py`: 0 errors. `build_manifest.py` run left the tree clean (manifest already current, contentVersion 580b51f48701b3fc).
Scope: consistency + quiz safety + cross-file integration. All 30 new word cards (front matter and full RU bodies read; structure, JP-token set, headings and links compared with the frozen EN originals), the 12 navigation-only restorations (diff 58c84bc..8fd47e7 read in full), manifest.json, and the intake JSON (all 42 payload sha256 values re-computed: candidate and EN source both match; no unrelated files in the commit). Quiz screen: my own stem/exact-segment scan of every RU word title against the 30 new titles, plus the listed clusters' actual card front matter/bodies (読み, 話, 評判, 決定, お見舞い etc.). Model: not verifiable from inside the session.
Verdicts:
- Consistency: NEEDS FIX (one minor item F1; everything else CLEAN: front matter keys/values, EN-link parity over all 42 files = 0 lost/extra, no remaining unrestored EN links to the 30 new targets anywhere in RU words/kanji/articles, nav-only files change only at link positions, manifest/intake hashes consistent).
- Quiz safety: NEEDS FIX (minor F2, F3). All EN exclusions are retained (誕生, 認める, 詳しい, 話題, 試す, 試し, 評価, 検査, 診察, 設計, 訓練, 触れる, 解釈); no new title equals another title/segment without a guard (only 認める/気付く "замечать", already guarded both ways in the 認める list).
- Scoped coverage of cross-file integration: CLEAN (all new cards' reciprocal EN links restored; the 12 nav files link exactly the EN positions).
Findings:
- F1; Minor; consistency/comprehensibility; words/訓.md (example 1 translation, line ~14); the translation renders the reading as a Cyrillic respelling «яма», which is also an ordinary Russian word ("pit"). EN gives plain やま; every other RU card keeps readings in kana (copilot-instructions: Japanese examples/ romaji stay as learning material; no Cyrillic-transcription convention exists). Impact: a beginner may read "яма" as the pit, not the sound; inconsistent with the rest of the corpus. Remedy: `「山」の訓は「やま」です。（「山」のくんは「やま」です。）— Кунное чтение знака 山 — やま.` Evidence: kanji/山.md and other RU cards keep やま in kana; EN words/訓.md line 15. Confidence: high.
- F2; Minor; quiz safety; words/訪問.md front matter; 訪問 "визит; посещение" has no direct guard against お見舞い "посещение больного; выражение сочувствия". The article itself names 見舞い as the narrower visit, お見舞い already guards 訪ねる/伺う (same visit family), and the two Russian titles share the head word "посещение". Either side may declare it. Remedy: `quiz_exclusions: [訪ねる, 伺う, お見舞い]`. Evidence: JMdict 見舞い (お見舞い) sense "visit to someone ill/ in trouble" vs 訪問 "visit, call". Confidence: medium (conservative guard; no exact title collision).
- F3; Minor; quiz safety; words/判断.md front matter; 判断 "суждение; вывод" (body teaches "оценка, решение, суждение") lacks a guard against 読み "чтение; оценка ситуации" (RU 読み body: "суждение о том, что что-то значит или что произойдёт"). The batch already guards 評価→読み and EN guards 解釈→読み for the same overlap; 判断 is at least as close to "оценка ситуации" as 評価. Remedy: `quiz_exclusions: [読み]` on 判断 (or add 判断 to 読み). Confidence: medium-low (defensible but unestablished necessity; pair is a direct pair, no transitivity needed).
Extra quiz_exclusions beyond EN (dictionary basis; necessity classification). Dictionary entries are from my JMdict knowledge of the same entries the cards cite; I did not re-fetch them.
- 生まれ→生まれる: 生まれ noun is the stem of 生まれる (JMdict 1609350 vs 生まれる "to be born"); conservative.
- 誕生→生まれる: 生まれる "to be born" overlaps 誕生 (suru) "to be born; come into being"; article lists it as the native verb; conservative (EN guards only 誕生↔生まれ).
- 許す→許可: 許す s.1 "permit/allow" vs 許可 "permission"; required (article says it fits the permission sense). Retained EN-silent pair.
- 認める→承認: 承認 "approval; recognition" vs 認める "recognize; approve"; required (shared Russian "признание/признавать"). 認める→許可: body teaches "компания разрешила" (認める "permit"); required.
- 試し→試験: 試験 "exam; test; trial" vs 試し "trial, try"; conservative.
- 評価→読み: shared lexeme "оценка"; 読み s.3 "reading/assessment of a situation"; required (mirrors EN 解釈→読み).
- 検査→調査: 調査 "investigation/survey" vs 検査 "inspection/examination" (body gloss "обследование"); conservative. 検査→テスト: テスト "test/examination"; 検査 "check/test"; required-ish (body gloss "проверка", matches existing チェック/試験 guards).
- 診察→受付: 受付 "reception desk/accepting" vs 診察 "medical examination/consultation"; Japanese senses differ; basis is only Russian polysemy of "приём"; conservative (lean unjustified, harmless).
- 設計→案: 案 "plan/draft/proposal" vs 設計 s.1 "plan; design" (RU title "проект"); conservative.
- 訪問→訪ねる, 伺う: 訪ねる "to visit", 伺う "to visit (humble)" vs 訪問 "visit"; required (shared "посещать/посещение"; article names 訪ねる as the overlapping native verb).
- 記憶→覚える: 覚える "to memorize; to remember" vs 記憶 "memory; to memorize/remember"; conservative-to-required ("помнить" appears in 覚える title). 記憶→思い出す: 思い出す "recall"; article teaches it as a contrast; POS differs, so conservative (lean unjustified).
- 記念→記憶: shared "память" in the Russian titles; real dictionary senses differ (記念 "commemoration, keepsake"); conservative.
- 訓→読み: 読み s.2 "reading of a kanji", 訓 is a reading; required.
- 討つ→勝つ: 勝つ "to win; to overcome/defeat an enemy" vs 討つ s.1 "to attack/defeat"; required (body: "одолевать врага" vs "побеждать").
- 触れる→関する: 関する "касаться; относиться к" overlaps "затрагивать (тему)" and literal "касаться" (触る already guarded); required.
No unjustified exclusion that blocks a legitimate distinction the article teaches was found; no exclusion guards an antonym.
Optional:
- 判断 vs 決定 and 検査 vs 調べる remain unguarded: titles differ ("суждение; вывод" vs "решение"; "осмотр; анализ" vs "исследовать; проверять"), EN has no pair; nonblocking.
- 診察→受付 could be dropped as lexical-only; keeping it is harmless.
Limits: No dictionary pages were re-fetched; senses above are recalled JMdict senses, not freshly verified. This review does not assess Russian prose accuracy beyond quiz/format/consistency (other reviewers' facets). I did not read author reports, other reviewer reports, title-screen output, batch records other than the intake JSON, drafts or tracking.
