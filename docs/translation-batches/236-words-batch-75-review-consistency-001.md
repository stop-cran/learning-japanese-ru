# B236 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `122b0192996f8c54236941b802ee5b10a19d06fd` (tree `1fcb849e038d197467585c2ee4f298c482a359c5`),
> the signed candidate pushed before review.
> Later reconciliation is in `236-words-batch-75-recheck-001.md`.

## Snapshot
122b0192996f8c54236941b802ee5b10a19d06fd; tree clean at start and end (a `tools/__pycache__` I created by accident was removed).

## Scope
All 30 new RU cards read in full and compared mechanically and by eye with the frozen EN cards; the 6 navigation diffs (争, 圧, 有, 言, 難, 戦う); manifest.json; intake JSON; validator (0 errors); title screen against all RU titles.

## Verdicts
- Consistency: NEEDS FIX (one low-to-medium finding F1; everything else clean).
- Quiz safety: CLEAN (no missing required guard; two optional notes).
- Navigation restorations: CLEAN. manifest.json / intake: CLEAN.

## Findings
- F1 (low-medium) 貝.md: EN links トップ.md and 頂上.md in two sentences explaining why they are excluded (English-label safeguard). RU drops the sentences and links although both targets exist; the exclusions [トップ, 頂上] remain in front matter with no learner-visible reason. Fix: add a short sentence linking both and saying they are kept apart only as a safeguard («верх», «вершина» are unrelated to 貝), or accept the omission since Russian labels do not collide.
- F2 (low, nonblocking) 謎謎→不思議 guard is an unnecessary over-guard (noun vs na-adjective, titles already differ; 不思議 already guards 謎).
- F3 (optional) In-batch pair 話し合い–話し中 (both «разговор») is unguarded, inconsistent with the author's own 話し中→会話/話 reasoning.

Verified clean: front matter equals EN except title and quiz_exclusions; all EN guards kept in order; exactly 14 RU additions. Footers and headings match. All EN links present where RU targets exist (apart from F1); 4 RU-only links (謙虚→謙遜, 胡椒→塩, 削除→追加, 詰まる→込む) sit in substantive comparisons and are acceptable. Nonexistent kanji cards are plain text. Navigation diffs touch only link brackets/hrefs at EN positions. Manifest hashes of words/kanji and intake candidate hashes match; intake's 36 paths equal the diff.

14 RU guards: required: 縮む→座る, 話しかける→扱う, 論ずる→検討, 論ずる→考慮, 言い出す→勧める. Conservative/acceptable: 論ずる→取り上げる, 有難い→御礼/礼/ありがとう, 縮む→乗る, 詰まる→密, 話し中→会話/話. Unnecessary: 謎謎→不思議 (F2). Declined stem-only pairs judged defensible.

## Optional
Long titles (論ずる 77, 恐縮 76 chars) are within the repo's existing range (パス 84); no length rule.

## Limits
Semantic judgments are title/body-based; JMdict not checked. 118 strokes/*.json hashes differ from the working tree vs manifest (unchanged by this commit; probably a line-ending artifact, pre-existing, out of scope). Translation quality was not assessed.
