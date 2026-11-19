# B191 consistency and quiz-safety review (batch `191-words-batch-30`)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `20834c891a290fd011cbc3ce5b4940d5d1f5f5be`, a local unsigned commit whose tree
> `09404a2d88294118352e760242feb2a6ff59de3e` is identical to the signed candidate `3109d3d20ad14c3bd1453458a5e20133a3172b87`.
> Later reconciliation is in `191-words-batch-30-recheck-001.md`.

Snapshot: RU `20834c8` (branch full-ru-191-words-30, parent `45f316f`); working tree clean (`git status` empty before and after review). Frozen EN `6af98cb`. `python -X utf8 -B tools\validate.py` -> 0 errors. `tools\build_manifest.py` re-run on the tree rewrote `manifest.json` byte-identically (tree still clean), so the manifest is not stale (3849 files, contentVersion 0e9abce696a61ffe). No `tools\__pycache__` created. Committed blobs are LF.
Scope: all 30 new `words/*.md` cards (read in full against EN originals / front matter compared with EN), the 12 navigation-only files (`git diff 45f316f 20834c8`), `manifest.json`, `docs/translation-batches/191-words-batch-30-intake.json`. Facets: consistency, quiz safety, cross-file integration. Model: not verifiable from inside this session. Optional tools run: `link_parity.py` (42 files) and `word_title_screen.py` (lexical leads only; no pre-existing reports/ledgers/prompts were read).
Verdicts:
- Consistency: CLEAN (front matter keys word/reading/jlpt/type/kanji/tags identical to EN for all 30; titles Russian; no generated/unrelated files in the commit; 44 files = 30 cards + 12 nav + manifest + intake).
- Quiz safety: NEEDS FIX (two minor missing direct guards, F1-F2; every EN exclusion retained; no unjustified exclusions).
- Cross-file integration / scoped coverage: CLEAN (links, navigation, manifest, intake).
Findings:
- F1; Minor; quiz safety; words/越す.md:9 (`quiz_exclusions: [越える, 渡る, 引っ越す, 移る]`); 越す teaches (and its tags include `time`) passing a period (年を越す) and crossing a threshold (人数を超す), while the RU 過ぎる card (title «проходить; миновать») teaches time passing and passing a place/age threshold (三十歳を過ぎて). JMdict 越す (1175300) sense "to pass (time)/to pass over a point" overlaps 過ぎる sense 1/time. The sibling 越える already guards 過ぎる, but 越す does not, so «проходить; миновать» is a defensible answer for 越す «переваливать через». Remedy: `quiz_exclusions: [越える, 渡る, 過ぎる, 引っ越す, 移る]` (then regenerate manifest). Confidence: medium (real dictionary overlap; necessity depends on distractor selection).
- F2; Minor; quiz safety; words/貴重.md:11; 貴重 «ценный; драгоценный» vs 高価 «дорогостоящий; высокой цены». JMdict 高価 sense 1 includes "valuable/costly", 貴重 "precious; valuable"; RU 高価 already excludes 大切/大事 against exactly this "valuable" reading, and the 貴重 article warns against the «дорогой» (price) reading, so it is the one close title pair left unguarded among the value cluster. Remedy: `quiz_exclusions: [大切, 大事, 高価]`. Confidence: medium-low (a real overlap, necessity not established; fix is harmless).
Optional:
- 贈る (teaches «вручать награду») and 与える vs 渡す «передавать; вручать»: all sibling give-verbs (あげる, 上げる, くれる, くださる, 差し上げる) carry 渡す; neither new card does. Dictionary basis 渡す sense "to hand over", but no shared title word with 与える and only the body sense «вручать» with 贈る; necessity not established, so not raised as a finding.
- 恩 «благодеяние; долг благодарности» vs おかげ «помощь; благодаря»: loose overlap (stem «благо-»; おかげ sense "help/benefit"); not required.
- 貢献 body renders 貢献する as «приносить пользу» and 役に立つ «быть полезным» exists; titles differ («вклад»), so no guard needed.
- Several cards (越す, 販売, 貢献) keep EN's meta remarks on "the English source list / English sale / services"; this is faithful to EN (越す.md:40-42, 販売.md:41, 貢献.md:40), left to the comprehensibility reviewer.
Exclusions beyond the EN file (dictionary basis; necessity):
- 身体 +生物: JMdict 生物 "living thing; organism" vs 身体 «организм» (shared title word, and the card teaches the contrast). Required.
- 越す +引っ越す: 引っ越す "to move house" = 越す sense "to move house" taught in the body (東京に越した). Required. 越す +移る: 移る sense "to move (house)", «переезжать» vs body sense. Required.
- 与える +くれる, +くださる: JMdict "to give" family; titles «давать мне или нам»/«давать нам (уважительно)» vs «давать». Required (mirrors the あげる/くれる/くださる sibling lists).
- 贈る +あげる, +差し上げる: «давать; дарить» / «давать; дарить (скромно)» share «дарить»; 与える is EN. +上げる: 上げる sense "to give" («поднимать; давать»). あげる/差し上げる required; 上げる conservative (real basis, necessity unestablished).
- 責任 +担当: title stem «ответственность» shared («ответственность за участок работы»); the 担当 article contrasts it. Required.
- 係 +責任: «ответственный (за порученное дело)» vs «ответственность» (shared stem). Required.
- 働き +労働: 労働 «труд» = 働き «труд». Required. 働き +運転: 運転 sense "operation (of a machine)" vs 働き «функционирование». Conservative. 働き +動く: 動く sense "to work/function (machine)" vs 働き «функционирование». Conservative. (働く, 仕事, 機能 are EN.)
- 販売 +売る: 販売 is a する-noun, action sense "to sell" = 売る «продавать». Required.
- 負け +負ける: 負ける derives 負け; «проигрыш» vs «проигрывать», no する on 負け. Conservative.
- 貸し +貸す: 貸す "to lend", base of 貸し; «ссуда» vs «одалживать». Conservative.
- 恩 +御礼: 御礼 "thanks; gratitude" vs «долг благодарности» (shared word). Required.
- No unjustified entries.
Checks passed: all EN exclusions retained verbatim (身体, 越える, 越す, 起こる, 与える, 贈る, 質, 賢い, 貸し, 貴重, 係, 働き, 作業, 勤め, 役, 義務, 務め, 責任, 豪華); 賞/贅沢/資源/資本/貯金/機能/責める/貢献 have none in EN and none needed (no shared title segment with any RU title; screened against all 2383 RU word titles, including senses taught in bodies). Work/duty cluster: pairs 役-義務, 役-務め, 義務-務め, 勤め-務め, 勤め-役, 勤め-勤める/仕事/働く/作業, 作業-仕事/労働/働き/働く, 係-担当/責任/役, 責任-義務/務め all guarded on at least one side. Giving: 与える/贈る vs あげる/上げる/差し上げる/くれる/くださる guarded; 贈り物/プレゼント/お土産 are nouns with different titles. 起こる-起きる guarded; 起す is «будить». 利口/賢い guarded (EN); 質-性格 guarded (EN); 豪華-贅沢 guarded (EN); 負け-負ける, 販売-売る guarded. 貸し-恩 (EN).
Navigation-only files: each of the 12 changes only link brackets/hrefs at EN link positions (与える, 責任 x3 files, 役, 越える, 貴重, 質, 賢い x2, 係, 責任 in 担当); no prose change. `link_parity` over all 42 files: no EN link with an existing RU target is missing; sole EXTRA is `kanji/役.md` -> `words/役に立つ.md`, already present at the baseline (not changed by this commit). A full scan of kanji/words/articles/strokes for any other RU file whose EN counterpart links to a batch word but RU does not found 0 (no residual navigation debt). EN links to absent RU targets (役割, 叱る, 攻める, 賞金, 賞品, 協力, 寄付, 資金, 借り, 愚かな, 節約, 敗北, 勝ち) correctly remain plain text.
Intake JSON: 42 payloads; for each, `candidateRawSha256` equals the sha256 of the committed RU file and `sourceRawSha256` equals the EN `6af98cb` blob; baseline `6aff607`, sourceCommit `6af98cb`.
Limits: dictionary entries were checked from JMdict sense knowledge and the cited IDs in the cards, not re-fetched; necessity of guards depends on the app's distractor selection, which was not simulated. Linguistic accuracy and comprehensibility of the card prose are other reviewers' facets; I read all 30 cards but did not audit readings or translations except where they affected exclusions or links.
