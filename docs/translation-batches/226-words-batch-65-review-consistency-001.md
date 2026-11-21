# B226 (226-words-batch-65) — CONSISTENCY / QUIZ SAFETY review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `bebdf808fd419165e2b6098bd25d815f7c41c235` (tree `acea83488c876c2f725c512d68e7db0c9584fba9`),
> the signed candidate pushed before review.
> Later reconciliation is in `226-words-batch-65-recheck-001.md`.

Snapshot: RU `bebdf808fd419165e2b6098bd25d815f7c41c235` (branch `full-ru-226-words-65`); `git rev-parse HEAD` matched and
`git status --porcelain --ignored` was empty before and after review (no uncommitted changes). Diff base `b61f341f…`.
Frozen EN `6af98cb`.

Scope: Read in full against their EN originals all 30 new cards (`words/` 一流 高級 高度 高等 高層 挙げる 拡充 拡張 片付く 固まる
強化 激増 増大 高める おどかす 驚かす 騒がしい 騒々しい 馴れる 香水 養分 餅 飾り 飽くまで 飢饉 飢える 食塩 挿す 裁縫 刺す) and the
complete diffs of the five navigation files (`kanji/刺.md`, `kanji/固.md`, `kanji/塩.md`, `words/アクセサリー.md`,
`words/片付ける.md`). Checked `manifest.json` diff, the intake record (path list/hashes only), `tools/validate.py` (0 errors),
and read-only scripted comparisons of front matter, headings and link multisets with EN. Ran only the optional
`word_title_screen.py` (read-only); did not run any generator. Did not read author reports, batch records or drafts.
Model: not verifiable from inside the session.

Verdicts:
- Consistency (format, terminology, links, navigation, manifest): CLEAN
- Quiz safety (EN guards retained, RU additions classified, no missing required guard established): CLEAN
- Scoped coverage of cross-file integration: CLEAN
- No per-article exceptions.

Findings: none (no actionable defect established).

## Evidence summary

1. Front matter: for all 30 cards `word, reading, jlpt, type, kanji, tags` equal EN. `quiz_exclusions` equal EN except the four
   RU-introduced additions below; 高める drops nothing (EN list ⊂ RU list + 上がる). おどかす and 餅 have no key (as EN). 4 `##`
   headings per card, identical to EN and to published RU cards (Значение / Как сочетаются кандзи / Синонимы и антонимы /
   Оттенки значения). H1 `# word（reading）— title` form consistent; no CRLF, all end with newline.
2. Links (multiset compared with EN): identical except
   - EN-only targets with no RU file (confirmed absent: `kanji/層`, `kanji/片`, `kanji/香`, `words/揚げる`, `words/増減`,
     `words/生け花`, `words/刺さる`) → plain text per convention, correct;
   - RU-only: `強化 → 固まる.md` (see below). Every RU link target exists.
   - 一/流, 高, 度, 等, 付, 固, 強/化, 増, 大, 水, 分, 食/塩, 刺 kanji links match EN; 充 層 張 拡 挙 挿 激 片 級 縫 裁 飢 飽 飾 餅 養 饉 香 馴 騒 驚 have no
     RU kanji file and no link.
3. 強化→固まる (RU-only link): sits in the Russian restatement of EN's English-dependent "solidify" remark; the card
   compares 固まる/固める with 強化 substantively, and 固まる now exists in this batch. Matches content-structure line 42
   ("ссылки на имеющиеся карточки ставьте при содержательном вводе/сравнении"). Acceptable, not a defect. (固める has no card → plain.)
4. Navigation restorations: diffs touch only the 8 link occurrences (刺: 刺す at lines 20, 31, 40; 固: 固まる line 32; 塩: 食塩 lines 28, 34;
   アクセサリー: 飾り line 35→ `[飾り](飾り.md)` at line 35; 片付ける: 片付く line 50). Positions/path forms equal EN
   (`../words/X.md` in kanji, `X.md` in words). Plain mentions left plain match EN    (EN links 刺さる at kanji/刺 lines 20, 32, 41 to a target that has no RU file → plain in RU, as are the line-47 mention and 塩 line 20 食塩, which EN also leaves plain). No other bytes changed.
5. Manifest: all 4,776 non-stroke manifest hashes (kanji/words/articles) equal sha256 of the committed blobs; every tracked
   content `.md` is listed; 35 changed entries + contentVersion changed only. Intake record: 35 payload paths = exactly the 30 new cards + 5
   nav files in the diff; `candidateRawSha256` equals the manifest hash for each; no learner content.
6. Title screen: no new title exactly equals or duplicates an existing whole title/segment unguarded; only exact-segment overlap is
   刺す «колоть» vs ちくちく «колоть; покалывать» — the EN guard 刺す→ちくちく is retained (so the titles share a segment but are
   excluded). In-batch pairs stay visibly distinct (高級/高度/高等; 拡充 «наращивание (служб, оснащения)» vs 拡張 «расширение масштаба;
   расширение функций»; おどかす «запугивать; пугать» vs 驚かす «удивлять; поражать»; 騒がしい «шумливый…» vs 騒々しい «галдящий…»;
   飢饉 «голод (бедствие)» vs 飢える «голодать»).

## RU-introduced `quiz_exclusions` (dictionary basis; necessity classification)

| Entry | Basis | Class |
| --- | --- | --- |
| 激増 → 急激 | JMdict 激増 sense 1 "sudden increase" vs 急激 "sudden, abrupt, radical"; RU titles share «резк-» («резкий рост» / «резкий (о переменах)»); EN links 急激 in the card without a guard | **conservative** (real basis, necessity unestablished; harmless, keep) |
| 驚かす → 驚く | JMdict 驚かす 1 "to surprise; frighten" vs 驚く 1 "to be surprised"; transitive/intransitive pair, titles «удивлять» / «удивляться» differ only by voice | **conservative** (keep) |
| 飢饉 → 飢える | JMdict 飢饉 1–2 "famine; scarcity" vs 飢える 1–2 "to starve; hunger for"; titles «голод (бедствие)» / «голодать» share stem; EN links but does not guard. One-way declaration suffices (app applies pairs symmetrically; no reverse needed) | **conservative** (keep) |
| 高める → 上がる | JMdict 高める 1 "to raise; enhance" vs 上がる 1 "to rise"; titles «повышать (уровень)» / «подниматься; повышаться» share «повыш-»; intransitive counterpart of 上げる, which is already EN-guarded | **conservative** (keep) |

None is unjustified: no guard targets a contrast the article itself relies on as the *answer*; each pair is a near-synonymous/voice
or stem-sharing neighbour. No over-guarding of pairs where titles already separate the cards was found.

## Declined pairs (author's choice) — judged

Acceptable to leave unguarded (no defensible correct-answer reading from the displayed titles): 一流–アナウンサー, 高級–クラス, 高度–水準,
高層–大気 (title says «верхние слои атмосферы», 大気 «атмосфера» is not a defensible answer for 高層), 挙げる–行う, 挙げる–動かす («приводить (пример)» vs «приводить в
движение» are distinct senses), 拡充/強化–円高, 激増–急に (adverb vs noun; optionally revisit with 急激 consistency, nonblocking),
片付く–処理/治める, 驚かす–びっくり (verb «удивлять» vs noun «удивление»; nonblocking), 驚かす–意外, 騒がしい–激しい/荒い, 飽くまで–通す,
飢饉–ぺこぺこ, 挿す–乗せる («сажать» is a different sense). The long list of stem hits (一日, 優勝, 高速, 黒板, 物価, 級, 段, 順番, 片付ける, 雰囲気, 上着, アパート, 例, 典型,
設備, 消防, 機能, 障害, 程度, 量, 年齢, 水準, 熱, 努力, 来る, こりこり, ずいぶん, 負け, 一時, 混乱, 心配, 模様, 汚れる, 物質, ぺちゃんこ, 火災, 立つ, etc.) are incidental
shared morphemes; none is a defensible answer for the batch word. Retained EN guards 高級→上等/偉い/高い/高価, 高等→上等/高い/高級, 高層→ビル, 拡張→拡大/発展, 増大→拡張,
高める→増す, 片付く→片付ける, 養分→栄養, 飾り→アクセサリー/飾る, 飢饉→不足, 飢える→ぺこぺこ, 挿す→植える, 刺す→ちくちく: all present. 飢饉 declares 飢える
but not vice-versa (as in EN) — sufficient under the direct-pair/symmetric contract.

## Optional

- Pair to recheck once both batches are final: 激増 «резкий рост» vs the still-unpublished previous-batch draft on the stem «резк-» (not read; out of scope).
- 刺す, "Оттенки значения": «Это не просто ещё один способ сказать, что её кусает насекомое.» reads awkwardly after the 雑巾 example; a comprehensibility
  reviewer may wish to look at it (not a consistency defect).

## Limits

- Manifest check: 118 `strokes/*.json` entries do not equal the sha256 of the committed bytes (also true of the unchanged published tree; strokes are untouched
  by this candidate, presumably hashed canonically) — pre-existing and out of this batch; I did not run `build_manifest.py` (generator forbidden) so I could not
  confirm the generator's own staleness check, only that all kanji/words/articles hashes match and `validate.py` reports 0 errors.
- Dictionary senses cited above come from the cards' own source citations and general JMdict knowledge, not fresh lookups; necessity classes concern ordinary quiz
  behaviour and are judgements, not measurements. 増大 body lines ~560 and some prose were read but linguistic correctness and comprehensibility are other facets.
