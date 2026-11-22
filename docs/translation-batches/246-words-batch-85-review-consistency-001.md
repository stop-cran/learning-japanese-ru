# B246 (246-words-batch-85) consistency / quiz-safety / integration review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `008ef28b7b8bb7986f863bea017c0e0e8165a058` (tree `75d0f14a1b55fc23d71f03565846f577eae947fd`),
> the signed candidate pushed before review.
> Later reconciliation is in `246-words-batch-85-recheck-001.md`.

## Snapshot
HEAD 008ef28b7b8bb7986f863bea017c0e0e8165a058 (matches); `git status --porcelain` empty; `python tools/validate.py` = 0 errors.
Diff vs baseline: 41 files = 30 new word cards, 9 existing navigation files (4 kanji, 5 words), manifest.json, intake JSON.

## Scope / read-in-full attestation
Read in full: all 30 new RU cards; all 9 navigation diffs (`git diff -U0`, 21 link changes: 包 3, 印 4, 巻 2, 短 6, 撒く 1, 矛 2, 蒔く 1, 転がす 1, 長所 1); the manifest diff (hunks) and the intake JSON (paths and hashes only); the EN counterparts for front matter, links, footers and the English-dependent remarks (入れ物, 碁, 瞳, 巻く, 潰れる, 知人, 睨む, 短所, 対立, 短編, 容器, 矢印) plus structured EN-vs-RU comparison of all 30. Title-screen tool run read-only (RU_ROOT). Not run: generators.

## Verdicts
- Coverage / links / navigation: CLEAN
- Duplicates and conflicts: CLEAN (one optional note, O1)
- Distractors / quiz_exclusions: CLEAN
- Tags and metadata: CLEAN
- Manifest / generated files: CLEAN (strokes untouched; no kanji card added, so none required)
- Formatting / footers: CLEAN
- Unverified: whether the app dedupes quiz options by title (code not available).

## Findings
No blocking, major or minor defects.

- O1 (optional, low; quiz safety; words/知人.md:9, words/知り合い.md:9): both have the title «знакомый» and neither excludes the other (EN parity; the repo has many identical-title unguarded pairs, e.g. 友人/友達, 辞書/辞典). Not a defect. Conservative remedy: append `知り合い` to 知人's `quiz_exclusions` after the EN entries. Confidence: medium.
- O2 (info; navigation): EN-only links with no RU target stay plain, correctly: 湯, 片, 装, 編, 矛盾→, 潰す, 名所, 対照, and others. RU-only links 湯飲み→ちゃわん, 短所→長所, 知り合い→知人 all resolve. Nothing to fix.

## quiz_exclusions beyond EN
Only one addition in the batch: words/破く.md adds `破る` (last).
- Basis: JMdict 破く (1983750) and 破る both gloss "tear"; the RU titles 破く «порвать; разорвать» and 破る «рвать; разрывать» are an aspect pair, so either is a defensible answer. 破れる already excludes 破る in EN and RU; 破る is an earlier-batch card and cannot declare 破く itself.
- Classification: required.
All EN exclusions are retained in all 30 cards. 碁 needs no extra guard (no 囲碁/将棋 card; ご homophones are not title-confusable). 椀/碗/ボール are mutually guarded. Pairs checked by the title screen (224 rows): the only unguarded exact title match is 知人/知り合い (O1); the stem-only rows were noise or EN parity.

## Integration checks
- Front matter matches EN for all 30 (word, reading, jlpt, type, kanji, tags) except the added 破く guard.
- Cross-batch links: 目印→標識 (title «опознавательный знак; указательный знак»), 研修→稽古 («отработка навыков; репетиция»), 知り合い→仲間 («товарищ; член группы») resolve and fit the glosses.
- Footers: source names and entry/sense numbers match EN; Weblio labels use a colon. Cosmetic differences in 崩す, 砕く, 破片, 矛盾, 椀, 碗 are not content errors.
- Manifest: all 39 kanji/word entries in the diff match the SHA-256 of the committed files (CRLF-normalised); 5494 manifest files equal 5494 on disk; the diff touches only contentVersion and these entries.
- Intake JSON: 39 payload paths exactly equal the diff's kanji/word paths; candidate hashes equal the manifest; no learner content.
- English-dependent remarks (碁 "go", 瞳 "pupil", 潰れる "be crushed", 入れ物 "case") are rebuilt for Russian or dropped naturally; no RU wording defects seen.

## Limits
Model identity not stated. App-side title dedupe unverified. Pre-existing prose glosses in older navigation cards were not audited beyond the changed links. Linguistic correctness is another reviewer's facet.
