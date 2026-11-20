# B212 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `d5fd0d933b7590c71fceadde93af255a14c4e0c0` (tree `e25b42695c1de0f449a934e1fd3152047e1f92a3`),
> the signed candidate pushed before review.
> Later reconciliation is in `212-words-batch-51-recheck-001.md`.

Snapshot: d5fd0d933b7590c71fceadde93af255a14c4e0c0 (HEAD confirmed; `git status --porcelain` empty; nothing uncommitted). `tools/validate.py`: 0 errors. The tree stayed clean.

Scope: Consistency, quiz safety and cross-file integration of batch 212. Read in full: all 30 new cards (front matter and body) and all 21 navigation diffs (31 restored links). Checked by script/hash: `manifest.json`, and the intake record's path list and hashes only (no learner content). Compared front matter and links of every new card against frozen EN (6af98cb). Screened the 30 new titles (segments and 5-character stems) against all RU word titles, and read the titles and exclusions of every comparison word named in the task. Model: not verifiable.

Verdicts:
- Consistency: CLEAN.
- Quiz safety: NEEDS FIX (F1, minor, one added guard). Otherwise CLEAN.
- Cross-file integration (links, manifest, intake): CLEAN.

Findings:
- F1; Minor; quiz safety; `words/完全.md` line 9 (`quiz_exclusions: [全く]`).
  Claim: 完全 has no direct guard against 全然 «совсем не; совершенно». The titles overlap on «совершенн-», which is the same overlap that justified the RU-added 完全→全く guard, and the article teaches 完全に as «полностью». The pair is declared on neither side (全然 lists [決して, とても, 何, 大変, どうも, 結構, 最も, 全部]).
  Remedy: `quiz_exclusions: [全く, 全然]`.
  Evidence: JMdict 全然 "wholly; entirely; completely" (adverb, before an affirmative) vs 完全 "perfection; completeness".
  Confidence: medium. The impact is a possible ambiguous quiz answer only.

RU-introduced exclusions (beyond EN):
| Pair | Basis | Classification |
|---|---|---|
| 完全→全く | 完全に ≈ 全く "completely"; shared «совершенн-» | required |
| 完了→完成 | 完成 "completion; perfection"; shared «завершение» | required |
| 完了→仕舞い | 仕舞い "end; close; conclusion"; shared «завершение» | required |
| 完了→終わる | 完了する "to complete" vs 終わる "to end" | conservative |
| 完了→終える | 終える "to finish" vs 完了する | conservative |
| 完了→済む | 済む "to finish; to be completed" | conservative |
| 宅→お宅 | お宅 "your house"; both titles share «дом»; parity with EN 宅–家/自宅 | required |
| 学者→研究者 | 学者 "scholar; scientist" vs 研究者 "researcher; scholar" | required |
| 存在→ある | 存在する "to exist" vs ある "to exist; to be"; stem существ- | required |
| 嫌う→避ける | 嫌う sense 2 "to shun; to avoid" | required |
| 不思議→謎 | 不思議 as noun "mystery" | required |
| 妙→奇しい | 奇しい is a rare spelling of あやしい; title «странный; подозрительный» | conservative |
| 好み→好む | same word family; both titles contain «вкус» | conservative |

None is unjustified. All EN exclusions on batch words are retained.

Checked, no guard required: 存在/いる, 委員/議員 (different titles), 奪う vs 盗む/取る/与える, 失う vs 無くす/得る/奪う, 契約/予約, 学期/期間, 奥 vs 中/内側, 姿 vs 格好/形/様子/影 (EN pairs present), 嫁/妻 (EN pair present), 女王 vs 王/王様, 俳優 vs 歌手/選手/演技/観客, 失業 vs 仕事/就職/率. No new title equals another card's whole title or segment without a guard.

Links and integration:
- Four EN links stay plain text because their RU targets are absent (confirmed): `kanji/委.md`, `words/会員.md`, `kanji/奇.md`, `words/王女.md`.
- Repo-wide EN-vs-RU link-count scan for batch words: no dropped EN link and no Russian-only link.
- All 21 navigation files contain exactly 31 single-line changes that only add link brackets/hrefs, and are otherwise byte-identical. Per-file counts match the specification.
- Manifest: all `.md` hashes match raw bytes. The 51 changed entries equal the diff's md files. No card is missing from the manifest.
- Intake: 51 payload paths equal the diff's md paths and the candidate hashes match; it adds no learner content.

Optional:
- Guard 宇宙→世界: JMdict 世界 sense 1 includes "the universe", and Russian «мир» can mean «вселенная». EN accepted the pair, so this is not required (low–medium confidence).
- 完了 vs 済ませる «заканчивать (дело)» and vs 終わり «конец; окончание» are not required at the threshold used above.

Limits:
- Dictionary bases for the RU-introduced pairs come from JMdict knowledge. Only 世界 was fetched online.
- I did not read EN bodies line by line. Front matter and links were compared by script, and RU bodies were read in full.
- Outside the batch: the existing cards 向かう (顔) and 汚す (土) lack an EN exclusion in RU. This is pre-existing.
- The 118 `strokes/*.json` raw-hash mismatches are a CRLF/LF artifact. They are pre-existing and unrelated.
- No Cyrillic-transcription rule was found in the RU instructions; the cards follow the existing kana-reading convention.
- BLIND rule followed: I read no author reports, title-screen output, batch records or tracking files. The only exception was the intake record.
