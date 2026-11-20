# B217 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `4af7ea72f6c372d31a810a783ca4b8655dd4ba44` (tree `7d76a5cff85d39b882c357ad2718d0fd71662b5c`),
> the signed candidate pushed before review.
> Later reconciliation is in `217-words-batch-56-recheck-001.md`.

Snapshot: 4af7ea72f6c372d31a810a783ca4b8655dd4ba44, clean tree (HEAD and `git status --porcelain` verified).
Scope: all 30 new cards and all 24 navigation diffs read in full; manifest hashes, intake path list, `validate.py` (0 errors). Model not verifiable.
Verdicts:
- Consistency: CLEAN
- Quiz safety: NEEDS FIX (minor)
- Cross-file integration: CLEAN
Findings:
- Q1; Minor; quiz; words/共に.md:9; 共に's title «и тот и другой» overlaps 両方 «оба». JMdict 共に has the sense "both; alike". Remedy: `quiz_exclusions: [一緒, 両方]`. Confidence: medium.
- Q2; Minor, conservative; quiz; words/出会い.md:9; the title shares «встреча» with 会合 and «знакомство» with 紹介, and the card itself teaches «встречи и знакомства». The EN pair is also unguarded. Remedy: `quiz_exclusions: [出会う, 会合, 紹介]`. Confidence: low-medium.
- Q3; Minor, conservative; quiz; words/処理.md (no exclusions); «улаживание дел» is close to 解決 «урегулирование». Remedy: `quiz_exclusions: [解決]`. Confidence: low.
- Beyond-EN exclusions: 全て→皆 (JMdict 皆 "all; everyone; everything"; shared «всё») is REQUIRED. 先日→このあいだ (identical segment «на днях») is REQUIRED. 優勝→勝ち (JMdict 勝ち "win; victory") is REQUIRED/conservative.
- All EN exclusions are retained.
- RU-only links 円→丸, 先日→このあいだ and 借金→借りる are substantive mentions or comparisons, so they are acceptable under the RU link rule.
- The EN-only link to 候補→kanji/補 has no RU target, so plain text is correct. All other listed absent targets were confirmed absent.
Navigation: 29 links restored in 24 files, link brackets and hrefs only, in EN path form: 処×3; 停, 再, 凍 ×2 each; 党×1; one in each word file. いくら wraps «иен» at EN's "yen" link position, which corresponds. 別れ and 劣る changed only by the link.
Manifest: no stale hash among kanji, words and articles; all 30 new cards are present. The 118 strokes/*.json entries mismatch the working tree, but they are unchanged by the candidate (a CRLF checkout artifact, pre-existing, outside the batch).
Intake: 54 paths, equal to the content diff; no learner content.
Optional: guards for 共通–同じ, 全–皆, 冗談–悪戯 and 借金–貸し are conservative only.
Limits: dictionary-basis claims come from my recollection of JMdict senses, not live page fetches. The strokes hash mismatch was not investigated beyond the CRLF indication.
