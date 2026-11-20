# B208 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `8963d85fc260aff6125e062366bcb09428c788ac` (tree `f0b363a16795dc636e1495eb6af34ee0f76fd3a4`),
> the signed candidate pushed before review.
> Later reconciliation is in `208-words-batch-47-recheck-001.md`.

Snapshot: RU 8963d85fc260aff6125e062366bcb09428c788ac (branch full-ru-208-words-47); `git status --porcelain` empty before and after; frozen EN 6af98cb. No uncommitted changes included.
Scope: consistency, quiz safety and cross-file integration. All 30 new word cards read in full against the frozen-EN originals; all 14 navigation-only diffs read (-U0 against 8266013); manifest.json and the intake record path list checked. Reviewer model not independently verifiable from inside the session (stated, not asserted). Blind to author reports, drafts, tracking, title-screen output and the scratch worktree. Nothing modified; build_manifest.py not run.
Verdicts:
- Consistency: CLEAN
- Quiz safety: CLEAN (optional notes only)
- Cross-file integration (manifest, intake, navigation): CLEAN
- Scoped coverage: not assigned (not reported)
- Comprehensibility: not assigned (not reported)
Findings:
1. Minor/optional; consistency/comprehensibility; words/鬼.md (several lines), words/悪魔.md (鬼 paragraph): "óни" is written with a Latin ó followed by Cyrillic letters (mixed script). It is an intentional device to avoid confusion with "они" and is explained in the card, but it is used by no other card, which makes the glyph awkward for search and copy. Remedy: consider «они (о́ни)» with a Cyrillic о and a combining accent, or «онi»-free plain «они (оти)»; or leave it. Evidence: grep of words/ finds acute-marked Latin letters only in 鬼, 悪魔 and 銀行 (pinyin). Confidence: medium; not a defect in teaching content.
2. Optional; quiz safety; words/急速.md `quiz_exclusions` 急に is the one added entry I class as weak: 急速 «стремительный» does not overlap 急に «внезапно; резко», and the article teaches that a change can be both sudden and rapid. Harmless (it only removes a distractor pairing). Keep or drop.
No defects found: front matter keys and values match EN except for the added quiz_exclusions and shortened titles; no EN links were dropped except to RU-absent targets (績, 象, 臓, 感ずる, 間隔, 劇, 冗談, 性別, 性質, 従う, 応ずる), which are plain text; no broken RU links; EN and RU link sets to the 30 new words are identical across all non-doc files; validate.py reports 0 errors.
Quiz-exclusion classification (beyond EN; all EN exclusions retained):
- Required (shared RU title segment): 恐れる→びくびく (бояться); 急激→急に (резк-); 思い出→記憶 (воспоминание); 応じる→返事, 承知 (отклик, соглас-); 心臓→心, 胸 (сердце); 悪魔→鬼 (демон).
- Conservative (close senses, disjoint titles): 成績→評価; 慎重→注意, 用心; 感覚→気持ち; 感動→感心; 意識→気付く; 必ずしも→必ず.
- Conservative and redundant duplicates (the pair is declared on both sides, which the app treats symmetrically): 感じる↔感じ; 急速↔急激.
- Unjustified/weak: 急速→急に (finding 2). Exclusions are direct pairs and none is transitive.
- No exclusion is stale, self-referential or dangling (validate.py).
Optional: 意外 has no exclusions (same as EN) but «неожиданный; удивительный» sits near 突然 «внезапно» and びっくり «удивление»; a guard 意外→[突然, びっくり] would be harmless. 応じる «откликаться; соглашаться» vs 答える is undeclared (返事 already declares 答える). Neither is required.
Integration checks:
- manifest.json: 4354 entries; every entry's file exists and its hash matches (LF-normalised or raw); no removed entries; exactly 44 entries changed or added against 8266013 (30 new words + 14 navigation files), none unrelated; contentVersion changed. Existing tracked kanji/words files appear unquoted-path-escaped only in git ls-files output (a quoting artifact of my script, not missing entries; the all-entries check found no mismatch).
- Intake record: the 44 payload paths equal the content diff exactly; candidate hashes match the files; held is empty; the record contains no learner content. Commit touches only the 44 content files, manifest.json and the intake JSON (46 files).
Limits: dictionary senses cited from JMdict knowledge, not re-fetched; no app-side quiz run; linguistic correctness not reviewed beyond consistency; the git ls-files "not in manifest" probe was inconclusive because of path quoting, so completeness of manifest coverage for pre-existing files rests on the per-entry hash check and the 44-entry diff only.
