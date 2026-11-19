# B189 consistency and quiz-safety review (batch `189-words-batch-28`)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `9251965ace4abea93cac73e84a2d32d76243abc5`.
> Later reconciliation is in `189-words-batch-28-recheck-001.md`.

Snapshot: RU `full-ru-189-words-28` at `9251965ace4abea93cac73e84a2d32d76243abc5` (parent `6bd7b05`, published main `a65f37f`); `git status --short` clean at start and at end; frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`, clean. Committed content only; nothing was edited, staged or committed.

Scope: facets consistency, quiz safety and scoped coverage (cross-file integration) for
- the 30 new `words/*.md` RU cards against their frozen EN originals: 銅貨 銃 銀 鉄道 鉄 ピン 針 金属 金 金銭 金融 金曜 金庫 数 量 野 重視 重大 酸素 都市 便 郵便 部分 避ける 選択 選手 適用 適切 適度 違反;
- the eight navigation-only restorations (`kanji/数.md`, `kanji/適.md`, `words/市.md`, `words/番号.md`, `words/都会.md`, `words/防ぐ.md`, `words/首都.md`, `articles/numbers-and-counters.md`), compared with `6bd7b05`;
- `manifest.json` and `docs/translation-batches/189-words-batch-28-intake.json` (the only file read from that folder).
The commit has exactly 40 files: 30 new cards, 8 restorations, `manifest.json`, the intake JSON.
Reviewer/model: a single reviewer; the actual model family cannot be verified from inside the session, so no independence claim is made. Blind: no author report/prompt, title-screen output, other review, other `docs/translation-batches` file, `docs/translation-drafts` or `docs/translation-tracking.json` was read. Findings come from runtime files, frozen EN, the binding RU rules and my own evidence.

Verdicts:
- Consistency (front matter, headings, JMdict lines, links, terminology, nav-only files, manifest, intake): **CLEAN**. All 30 cards: `word`, `reading`, `jlpt`, `type`, `kanji`, `tags` equal EN; headings follow the RU reference (`## Значение` / `## Как сочетаются кандзи` / `## Синонимы и антонимы` / `## Оттенки значения`, then `Словарь: [JMdict]…`); no stray English learner-facing text; terminology matches `docs/translation-methodology.md` (онное/исконное чтение, глагол итидан, кандзи; no «иероглиф»). The nav-only files differ from `6bd7b05` only by link brackets/hrefs at EN link positions (text identical after stripping `[x](y)`→`x`; no CRLF drift). `link_parity.py` on all 30 cards: no lost or extra link. Manifest and intake verified below. No word-card Cyrillic-transcription convention exists in the RU rules, and EN cards contain no romaji, so nothing is owed.
- Quiz safety: **NEEDS FIX (one Minor finding, F1)**. All 14 EN exclusions declared by the batch cards are retained; every RU addition has a stated basis (table); no unjustified guard; one missing hyponym guard (鉄/銀 vs 金属).
- Scoped coverage (cross-file integration): **CLEAN**. Every EN link whose RU target exists is a live RU link; where the RU target is absent (e.g. `kanji/防.md`, `words/地方.md`, 11 targets in `numbers-and-counters`) the text is left plain, as required. Manifest and intake cover exactly the batch.

Findings:
- **F1 — Minor; quiz safety; `words/鉄.md:1-9` and `words/銀.md:1-9` (body evidence `鉄.md:15`, `銀.md:15`); confidence medium.**
  Claim and impact: 鉄 «железо» and 銀 «серебро» have no `quiz_exclusions`, so each can appear in the same question as 金属 «металл». Both card bodies state that the word *is* a metal (`鉄.md:15` «железо, металл и химический элемент Fe»; `銀.md:15` «серебро, металл»), and `金属.md:34` itself calls them «отдельные металлы». By the RU rule "проверяйте и родовое значение в лейбле" (`content-structure.instructions.md:160-161`, 車/電車), the generic label «металл» is a defensible answer for the prompt 鉄 or 銀, while the specific label is also true; the batch already treats the same hyponym relation as needing a guard for 銃–武器 (EN's 矛–武器 precedent) and 金–金属 (EN). Impact: a learner who answers 金属 for 鉄 (or 鉄 for the prompt «металл») is marked wrong by an unavoidable semantic ambiguity.
  Remedy: insert `quiz_exclusions: [金属]` as a new front-matter line between line 8 (`tags: …`) and the closing `---` in both `words/鉄.md` and `words/銀.md`; then rerun `python tools/validate.py` and `python tools/build_manifest.py` and commit the regenerated `manifest.json` (and the intake hashes for the two cards). No body text change is needed.
  Evidence: JMdict 鉄 (1437780) s1–3 (iron; the metal/element), 銀 (1595090) s1 (silver, the metal); JMdict 金属 (1243040) s1 "metal". Counter-evidence for the adjudicator: frozen EN `鉄.md` (title "iron"), `銀.md` ("silver") and `金属.md` ("metal") declare no such pair, so this is an inherited gap rather than a regression; the cost of the guard is one candidate fewer in a small set of questions.

Exclusions beyond the EN file (RU additions) — dictionary basis and necessity. Titles are the RU labels shown in the quiz. JMdict wording is from the entries the cards cite or their Jisho/JMdict rendering.

| Declared on → pair | Basis (JMdict entry/sense, RU label overlap) | Class |
|---|---|---|
| 金曜 → 金曜日 | 金曜 (1243310 s1) "Friday", see-also 金曜日 "Friday"; both labels «пятница» | required |
| 銃 → 武器 | 銃 (1337000 s1) "gun; firearm" is a kind of 武器 s1 "weapon; arms" (label «оружие; сильная сторона»); generic label inside 武器's title; EN precedent 矛–武器 | required |
| 数 → 多少 | 数 (1580820/1580825) "number; amount" vs 多少 s2 "amount; quantity; number" (label «немного; количество»): shared «количество» | required |
| 量 → 多少 | 量 (1554640 s1) "quantity; amount" vs the same 多少 s2: shared «количество» | required |
| 野 → 畑 | 野 (1537250 s1) "field; plain" vs 畑 "field; farm; vegetable garden" (label «поле; огород»): shared «поле» | required (moderate; the card teaches the cultivated/open contrast) |
| 都市 → 町 | 都市 (1444990 s1) "town; city" vs 町 "town; neighbourhood" (label «городок; район»); RU 市 and 都会 already guard 町 | conservative (real basis; labels «город» vs «городок» differ) |
| 便 → 郵便局, 郵便 → 郵便局 | 便 (1512360) / 郵便 (1605680) "mail; postal service" vs 郵便局 "post office" (label «почтовое отделение»); Russian «почта» names both the service and the office, so «почта» in 便/郵便 is a defensible answer for 郵便局 | required |
| 重大 → 大変 | 重大 (1336500) "serious; important; significant; grave" vs 大変 s3 "serious; grave" (label «трудный; серьёзный»): shared «серьёзный» | required |
| 重大 → まじめ | まじめ s1 "serious; earnest; sober; grave" (label «серьёзный; добросовестный»): identical gloss word «серьёзный»; not an antonym/contrast guard | required (identical label word) |
| 重大 → 大した | 大した "considerable; important; significant" (label «значительный; выдающийся») vs 重大 label «значимый»: two JMdict glosses shared | required |
| 重大 → 相当 | 相当 s4 "considerable; substantial" (label «соответствие; значительный») vs «значимый» | conservative (looser overlap) |
| 金融 → 経済 | 金融 (1243290 s1) "finance; financing" vs 経済 s2 "finance; (one's) finances" (label «экономика; финансы»): shared «финансы» | required |
| 金融 → 金銭 | 金銭 (1243020) "money; cash" (label «деньги; денежные дела») vs 金融 s2 "monetary; financial" | conservative (borderline required: «денежные дела» ≈ «финансы») |
| 金融 → お金, 金融 → 金 | «финансы» vs «деньги»; precedent: RU 経済 already guards お金 | conservative |
| 金 → 経済, 金銭 → 経済 | 金/金銭 «деньги…» vs 経済 s2 "finance"; same RU 経済–お金 precedent; EN 経済 (title "economy and economics") has none | conservative |
| 選択 → 選ぶ | 選択 (1392290, noun/する) "selection; choice" with the verb action sense "to choose" vs 選ぶ "to choose" (label «выбирать») | required (action sense of する-noun) |
| 適用 → 用 | 適用 (1437500) "application (of a rule or method)" vs 用 s2 "use; purpose" (label «применение; назначение; дело»): shared «применение» | required |
| 適切 → 適する | 適切 (1437430/1437450/1493960) "appropriate; suitable" vs 適する "to fit; to suit" (label «подходить…»): shared «подходящий/подходить» | required |
| 適切 → 合う | 合う "to fit; to suit; to match" (label «подходить; совпадать») | required |
| 適切 → いい | いい label «хороший; подходит» contains «подходит»; RU 適当 already guards いい | conservative |

No addition is unjustified: none guards an antonym or contrast the article itself teaches, and none rests on topical relation alone. Retained EN pairs (14, all present): 便→便り, 郵便→便, 都市→都会, 都市→市, 重大→重要, 量→数, 金→お金, 金→金属, 金銭→お金, 金銭→金, 針→ピン, 適切→適当, 適度→適切, 適度→適当.

Manifest (verified): the generator's own `build_manifest()` (read-only call, no write) returns a dict identical to the committed `manifest.json` (3784 files, 3 images, 2 scenes, `schemaVersion` 2, `contentVersion` `941f9b2d43612f41`), so no stale hash. The diff against `6bd7b05` is 30 added entries (the new words) + 8 changed entries (the restorations) + `contentVersion`; no deletions, no unrelated or generated files.
Intake (verified): `schemaVersion` 1, `batchId` `189-words-batch-28`, `sourceCommit` is the full frozen-EN `6af98cb7…`, `baseline` `a65f37f…` is the published main (ancestor of the candidate), `held` empty. 38 payloads = the 30 cards + 8 restorations, no duplicates, no omissions; every `candidateRawSha256` equals SHA-256 of the RU file at `9251965` and the manifest value; every `sourceRawSha256`/`sourceSha256` equals the frozen-EN bytes (raw and CRLF-normalised; EN `numbers-and-counters.md` is CRLF, RU is LF, and the normalised hash matches). The note "independent review pending" describes the pre-review state; the record is expected to change after review.

Optional (non-blocking; none is a defect):
- Future obligations, not this batch: EN pairs naming batch words are declared on cards with no RU card yet and must be carried when those cards are translated, e.g. ピストル/鉄砲→銃, 硬貨/通貨→銅貨, 線路/私鉄/新幹線/輸送→鉄道, 通貨/紙幣/小遣い→金/金銭, 平野/牧場/無地→野, 深刻/甚だしい/重たい→重大, 妥当/的確/手頃→適切/適度, 郵送/書留/船便→郵便/便, 分量/体積/容積→量, 偶数/回数/桁/点数→数, 重点→重視, 潜る/退ける→避ける.
- 金庫 «сейф; хранилище» vs 銀行 «банк»: the body (`金庫.md:41`) teaches 信用金庫 as an institution; the labels do not overlap, so no guard is needed unless the title is later widened.
- 違反 «нарушение (правил, закона)» vs 障害 «препятствие; нарушение функции»: the word «нарушение» is shared, but both labels are qualified and differ in meaning; not defensible, no guard.
- 数 «число; количество» vs the date cards (一日 «один день; первое число» etc.): the 数 body already warns that «число» can mean a date (`数.md:46-47`); labels are qualified ordinals, no guard.
- 重視 «придавать большое значение» vs 重大 «значимый»/かまう «уделять внимание»: different parts of speech/senses; no guard.
- 鉄道 «железная дорога» vs 道/道路/電車/駅, 針 vs 時計/糸, 避ける vs 防ぐ/逃げる (the 防ぐ card `防ぐ.md:36` teaches the 避ける contrast), 選手 vs スポーツ/競技, 酸素 vs 空気, 部分 vs 中心/ほとんど, 銀 vs 金: examined; no defensible overlap beyond what is already guarded.

Limits:
- Reviewer model not verifiable (see Scope); no independence claim.
- No local JMdict. Entry numbers come from the cards; sense wording is from Jisho's JMdict rendering for 金曜, 多少, 銃, 金融, 経済, 重大, 大変, 武器, 金銭, まじめ, 大した, 郵便局, 用, 相当 and 適する. The wording for 町, 合う, 選ぶ, 畑, 都市, 適切 and 鉄/銀 senses was not re-fetched; those classifications rest on the cards' own cited entries and the RU labels.
- Quiz defensibility is a judgment about the displayed RU labels, not an execution of the app's candidate builder; the app's own 4-option selection and the title screen (lexical overlap only) were not treated as verdicts.
- Accuracy of Russian prose, readings and example sentences is outside this facet (comprehension/accuracy reviewers own it); this review checked structure, EN parity, links, exclusions, manifest and intake only.
- Counts above are as of `9251965`; later edits invalidate them.
