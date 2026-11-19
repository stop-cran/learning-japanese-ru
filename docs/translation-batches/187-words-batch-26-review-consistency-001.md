# Batch 187 (words-batch-26) — consistency and quiz-safety review

Reviewer: Claude family (requested `claude-sonnet-5.5`); the exact running model is not exposed to me, so I do not claim it.
Blind: I did not read the author report, author prompt or other reviewers' reports.

## Snapshot
- RU repo `C:\Users\romanko\repos\learning-japanese-ru`, branch `full-ru-187-words-26`, HEAD `cc6b8f1` (full `cc6b8f13ebceb4be3a1b13194f53efa9e27e0bc9`).
- `git write-tree` = `1597f0853220fbaeb521bab731c807b81e62373e`, matching the request. I re-ran it at the end and it is unchanged. I did not edit any file, the index, the branch or refs.
- Working tree equals the index. The only untracked item is `tools/__pycache__/`, which is Python bytecode. I most likely created it by running `tools/validate.py` and `tools/test_validate.py`; I could not tell whether it existed before. It does not affect the tree.
- EN frozen source `C:\Users\romanko\repos\learning-japanese-en-frozen`, HEAD `6af98cb717755690a9ca793e5454a96ebd7a8f9f`, clean.

## Scope
- Reviewed all 30 new `words/*.md` cards: 離す 雇う 集団 集中 会 会合 集まり 隠れる 隠す 障害 回 度 際 陰 限界 守る 防ぐ 関連 関心 関する 誤り 間違い 始まり 開始 閉じる 長期 鎖 鍋 鋭い 鋏.
- Reviewed all 17 navigation-only modified files: kanji 団, 守; words ぼんやり 仕舞い 利口 団体 対する 感心 永久 破る 約束 紐 組織 表す 達する 違い 離れる.
- Reviewed `manifest.json` and `docs/translation-batches/187-words-batch-26-intake.json`.
- Changed-file scope is exact: 49 files, comprising 30 A cards, 1 A intake, 17 M navigation files and 1 M manifest. There is nothing else. That includes no change to `translation-tracking.json`, `translation-progress.json` or the plans. In the batch-186 history those were recorded in later commits (`0227a4a`), so I treat their absence as normal for a candidate snapshot; I did not verify them.
- Method: scripted checks against the staged blobs and the EN frozen files. I compared front matter, link lists, exclusions, manifest and intake hashes. I also ran a Russian title-overlap scan against all RU word cards.

## Verdicts
| Facet | Verdict |
|---|---|
| Consistency | **PASS**, with no blocking or must-fix defect. |
| Quiz safety | **PASS with two Low-Medium advisory items.** No missing EN exclusion, no missing target, no duplicate or self exclusion, no duplicate title. See Findings F1 and F2. |
| Scoped coverage | **PASS.** The 30 requested cards exist and are identical to the EN counterparts in identity. |
| Correctness and comprehensibility | **UNVERIFIED.** This is not my assigned facet, and I made no linguistic verdict. I only observed that headings match `# 字（reading）— title`, that every card has the 4 required H2 sections in RU order, and that there is no stray English prose in the 30 cards. |
| Strokes, grammar and other facets | **UNVERIFIED** (out of scope). |

### Evidence behind the verdicts
- `python tools/validate.py` reports 0 errors; the manifest line shows 3729 files and version `157cf612e0e30e3d`. `python tools/test_validate.py` ran 83 tests, OK. The validator is not a linguistic verdict.
- **Identity.** For all 30 cards I compared every front-matter field except `title` and `quiz_exclusions` with the EN card: `word`, `reading`, `jlpt`, `type`, `kanji` and `tags`. There are no differences. The `title` differs only in language. No duplicate word title exists among the 30 or against any existing RU word title.
- **Files** are LF, have no BOM, and end with a newline.
- **Manifest.**
  - I regenerated it in-process with `build_manifest.build_manifest()` and it equals the staged `manifest.json` exactly, including `contentVersion` `157cf612e0e30e3d` and `schemaVersion` 2.
  - Versus base `cc6b8f1`: 30 files added, 17 changed, 0 removed. The 17 changed are exactly the navigation files above.
  - No other namespace changed.
- **Intake.**
  - `sourceCommit` is `6af98cb…`. `baseline` is `acef994…`, which is an ancestor of HEAD; it is the merge of the batch-186 PR #70, and the batch-186 intake used its own predecessor in the same way.
  - There are 47 payloads: 30 new cards, 15 navigation words and 2 kanji. `held` and `notes` are empty. The paths are unique and are exactly the set of changed content files.
  - For all 47 payloads, `candidateRawSha256` equals the SHA-256 of the staged blob. `sourceRawSha256` equals the hash of both the EN file on disk and the blob at `6af98cb`. `sourceSha256` equals `sourceRawSha256`. There are 0 mismatches.
- **EN exclusions.** All EN `quiz_exclusions` of the 30 cards are retained in RU, with none lost. Every exclusion target exists as an RU word card, so none is missing. There are no self, duplicate or distractor-overlapping entries. These cards have no `quiz_distractors`. The app applies exclusions in both directions, so a one-sided declaration is sufficient. This holds for 度↔回 (度 declares it) and 会↔集まり (集まり declares it).
- **RU-only direct exclusions.** There are 11 cards with additions. All are justified by a visible RU title overlap and point at an existing card:
  | Card (line 9) | Added | Visible RU overlap |
  |---|---|---|
  | 度 | 場合, ケース | 場合 «случай; ситуация», ケース «футляр; случай» share «случай» |
  | 際 | 場合 | pairs with 時, 度, 場合 |
  | 限界 | かぎり | both «предел» |
  | 関連 | 連絡 | 連絡 «связь; контакт» |
  | 関する | 対する, 触る | «относиться к», «касаться» |
  | 間違い | 失敗 | «ошибка» |
  | 始まり | 始め | «начало» |
  | 開始 | 最初 | «начало» |
  | 閉じる | ぱくぱく | «закрывать…» |
  | 長期 | 期間 | «период; срок» |
  | 鍋 | 料理 | «блюдо» |
  | 鋭い | 辛い | «острый» (辛い is «острый (о вкусе)») |

  I did not infer any transitive exclusion.
- **Links.**
  - For all 47 files, the ordered list of relative `.md` targets is identical to EN, with the sole difference that EN targets absent from RU are unlinked in RU. All 19 such dropped links have a target that does not exist in RU (放す, 雇 kanji, グループ, 影, 防 kanji, 避ける, 誤解, 鋭 kanji, 鈍い, 賢い, the two onomatopoeia articles, 感動, 永 kanji, 結ぶ, 到着, 届く, 共通). Each is therefore correctly plain text, and the card's `kanji` list still names the missing kanji.
  - No link is added at a non-EN position.
  - All remaining relative links resolve. The kanji 団 diff versus EN consists of EN-only targets 団地 and 座布団, which are absent in RU. The kanji 守 links are identical to EN.
- **Reciprocity.** For each of the 30 new cards I computed the EN files that link to it. For each such source that exists in RU, RU links back. Examples: 離れる→離す; 団体→会; 組織→会合; 表す→隠す; 破る/約束/防ぐ/kanji 守→守る; 感心→関心; 永久→長期; 紐→鎖; 利口→鋭い; 達する→限界; 仕舞い→始まり; 違い→間違い; ぼんやり→集中; 対する→関する; kanji 団→集団. There are no missing and no extra incoming links.
- **Pre-existing, unchanged** (the navigation diffs touch only link lines):
  - The RU 17 carry RU-only exclusion expansions, for example 仕舞い and 離れる.
  - `対する.md` has `# 対する（たいする） — …` with a space before the dash, unlike the other cards. This is outside the batch's changes.

## Findings

### F1 — Medium-Low, quiz safety (RU-visible title), advisory
- File/line: `words/度.md:9` (`quiz_exclusions: [時, 回, 場合, ケース]`); title «случай; раз; градус».
- Evidence: the existing `words/機会.md` has title «возможность; удобный случай» and no exclusions. The existing cards that carry the same «случай» sense, namely 時 (`時.md`) and ケース, both already exclude 機会. 度 excludes 場合 and ケース for exactly this reason but not 機会.
- Impact: a JA→RU question for 機会 (or an RU→JA question for 度) can show «случай» in both choices, so a learner cannot tell them apart by the visible label. EN is not affected because the EN titles are "occasion; time; degree" and "opportunity; chance".
- Remedy: add 機会 to 度's `quiz_exclusions` and regenerate the manifest and intake hash. The alternative is to keep the exclusion list as is and accept the risk. Confidence: medium, since the quiz's candidate selection depends on tags and kanji scoring.

### F2 — Low, quiz safety (RU-visible title), advisory
Each pair below shares a visible Russian word. None has an EN counterpart collision. Confidence: low-medium.
- `words/集まり.md` «собрание; скопление» vs existing `混雑.md` «давка; скопление людей» (shared «скопление»): add 混雑 to 集まり's exclusions, or retitle.
- `words/始まり.md:9` and `words/開始.md:9` («начало…») vs existing `出発.md` «отправление; начало пути». The existing «начало» cards 初め, 始め and 最初 already exclude 出発, so by the same precedent 始まり and 開始 would too. EN titles ("beginning; start") have the same shape, so this follows EN.
- `words/回.md` «раз; счётное слово…» and `words/度.md` vs 一度 «один раз», もう一度 and 今度. Shared «раз»; the meanings are clearly different.
- `words/障害.md:9` «нарушение функции» vs existing `故障.md` «неисправность; поломка»: a partial semantic overlap. EN has the same pair without an exclusion.
- `words/鍋.md` «горячее блюдо набэ» vs existing お皿 «блюдо для подачи»: the word «блюдо» is used in different senses.
- `words/会.md` «встреча; объединение» vs existing `会議.md` «совещание; конференция»: EN excludes 会↔会合 only, and RU follows it.
- Remedy for all: optional; add pair exclusions only if the maintainers want RU stricter than EN. I did not treat shared words or topics as a collision by themselves.

No other finding. I found no defect in links, identity, reciprocity, exact scope, counts, manifest or intake.

## Optional
- Consider recording 機会↔度 (F1) while the cards are still in candidate state, because the hashes in the manifest and intake will need regenerating anyway.
- Remove or ignore `tools/__pycache__/` (untracked bytecode) before committing.

## Limits
- Not assessed: Russian linguistic accuracy, JMdict facts, readings or Japanese examples, pedagogy and comprehension, strokes, article and grammar content, and the translation-tracking and progress files. These were not requested or not in the staged tree.
- The quiz-overlap scan is lexical (shared whole Russian words of at least 4 letters) plus my own reading of the matching titles. It does not replicate the app's candidate selection, so F1 and F2 estimate risk and do not prove ambiguity in any particular quiz.
- Model identity: I cannot verify which model ran this review.
