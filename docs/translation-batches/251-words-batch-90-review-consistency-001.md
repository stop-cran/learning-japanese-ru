# Batch 251 (251-words-batch-90) - consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `8bb7b574df56eb149c7b7c22a70aae4cde4bbee6` (tree `af91f2d01fc3555bf1190ac60079f79715e80cb7`),
> the signed candidate pushed before review.
> Later reconciliation is in `251-words-batch-90-recheck-001.md`.

## Snapshot
- Repo `learning-japanese-ru`, HEAD `8bb7b574df56eb149c7b7c22a70aae4cde4bbee6` (matches pinned candidate).
- Working tree clean. My `tools/validate.py` run created `tools/__pycache__/`; I removed it and used `python -B` afterwards.
- Compared against frozen EN source `learning-japanese-en-frozen`.
- No generator run (no `build_manifest.py`), no edits, no branch changes.
- I also ran `word_title_screen.py` from the external rutools dir with `RU_ROOT` set (output to temp, not the repo).

## Scope
- All 30 cards and the 4 navigation diffs (傾く, 光る, 往復, 炊く) read in full.
- Automated EN-vs-RU comparison of front matter, links and line counts.
- Manifest hashes and intake JSON (`docs/translation-batches/251-words-batch-90-intake.json`) checked.
- Footers compared with EN by URL, JMdict entry number and sense number.
- Quiz exclusions analysed, including the 16 RU-introduced guards on 13 cards.
- Model identity: I cannot verify the model I ran as from inside the session.

## Verdicts
- Consistency with EN: CLEAN (optional notes only).
- Quiz safety: CLEAN. No missing required guard found. Several RU-added guards are over-guarding, non-blocking.
- Navigation diffs: CLEAN.
- Manifest and intake: CLEAN.
- Validator: 0 errors.

## Verified facts
- Front matter: every key identical to EN except `title` (Russian). Tags, `jlpt` and `type` identical in all 30.
- EN `quiz_exclusions` all kept; RU additions appended after them in EN order.
- RU-added guards (16 on 13 cards), exactly as the brief lists:
  物差し→単位; 物凄い→莫大; 牧畜→家畜; 牧場→牧畜, 農家; 片道→往復, 切符; 片寄る→公平; 焚く→炊く; 暖まる→暖房; 照る→晴れ; 煙突→管, パイプ; 焦点→注目; 無限→いつまでも; 休業→営業.
- Links: no RU-only and no broken links. EN links missing in RU point to targets absent in RU (kanji 畜 片 燃 照 温; words 仮名 冷ます 商店 無数). Plain text is per convention and reads naturally.
- Navigation: 傾く:36 links 片寄る, 光る:33 links 照らす, 往復:35 links 片道, 炊く:38 links 焚く.
  Each diff changes one line, only by link brackets, with no line-count change.
  Positions and `X.md` path form match EN.
- Manifest: all `words/` hashes match file bytes; no missing or extra word entries.
  118 `strokes/*` hashes differ only through CRLF checkout (they match after LF normalisation). This is an environment artifact.
- Intake JSON: 34 payload paths equal the content diff (30 cards + 4 nav files). `candidateRawSha256` values match the manifest.
- Footers: URLs and JMdict entry/sense numbers identical to EN in all 30 cards.
- Line counts: RU is 2-4 lines shorter than EN for 爪, 焦げる, 焚く, 熱する, 熟語, 物凄い, 煙突, 煎る, 休業.
  I confirmed for 爪, 焦げる, 熱する, 休業, 熟語 that the dropped lines are English-only remarks, correctly adapted.
  I did not re-read EN for 焚く, 煙突, 物凄い, 煎る.
- Title screen: no exact title or segment duplicates. Title-stem hits are covered by the guards below or are not defensible confusions.

## Findings (all low or optional; none blocking)

### Quiz guards
1. LOW, 片道.md front matter, `quiz_exclusions` 往復: antonym/contrast taught in the article, titles share no wording. Unnecessary. Harmless.
2. LOW, 片寄る.md front matter, 公平: unnecessary. Opposite concept, no shared wording. Harmless.
3. LOW, 休業.md front matter, 営業: unnecessary. Opposite concept. Harmless.
4. LOW, 暖まる.md front matter, 暖房: inconsistent. 暖める has no 暖房 guard, so either drop it or add it to 暖める.
5. INFO, conservative but with a real basis, not required:
   - 物差し→単位: shared stem «мер».
   - 物凄い→莫大: JMdict sense 2 "tremendous" vs "enormous".
   - 牧畜→家畜: stem «скот».
   - 牧場→牧畜: shared stem «животновод». The pair is declared on one side only, which is enough under the symmetric rule.
   - 牧場→農家: «ферма»/«фермер».
   - 焚く→炊く: homophone たく, but the titles are clearly different.
6. Required guards, present and correct:
   - 照る→晴れ: parity with the EN 晴れる guard.
   - 煙突→管 and 煙突→パイプ: both titles contain «труба».
   - 焦点→注目: «пристальное внимание» vs «центр внимания».
   - 無限→いつまでも: parity with the 永久/永遠 guards.
   - 片道→切符: parity with the EN 往復→切符 guard.
7. OPTIONAL: 片寄る and 片道 share the RU phrase «в одну сторону» (the EN titles share nothing). The head words differ, so risk is low. A one-way guard could be added.
8. OPTIONAL: 照る→快晴 is unguarded, which is inconsistent with the 晴れ guard.
   焦がす/焦げる vs あぶる/煎る is borderline (あぶる covers "scorch", its body says «опаливать»). Parity with EN.
9. Unguarded pairs I judged not defensible confusions: 照る vs ざあざあ/だらだら («лить» is a different sense); 焦点 vs 手品 («фокус» is a homonym); 焦点 vs 中央/真ん中; 熱する vs 燃やす; 暖まる vs 沸く/ほかほか.

### Content wording
10. LOW, 照らす.md:45: the 参考 gloss «справка, ориентир» drifts from the 参考 title «справочный материал; обращение к источнику». EN says "reference/consultation"; «ориентир» is really 目安's sense. Suggest «справка, обращение к источнику».
11. OPTIONAL, 照る.md title: «лить свет» is stilted. «светить» is clearer but is near 光る «светиться», which is guarded.
12. INFO, bunka.go.jp `ijidokun_140221.pdf` footer label: EN says "Agency for Cultural Affairs"; RU says «Совет по делам культуры, доклад 2014 года». The URL path is `bunkashingikai` (Council), and 140221 = 2014-02-21. It is consistent with earlier published cards 粗い, 荒い and 始め. Not an error.
13. INFO, 照る.md tags lack `wago` although `type: wago`. Identical to EN, so a pre-existing parity item, not a batch defect.

## Optional
- Drop or justify findings 1-4 if the guards should stay minimal.
- Apply the one-way guard and 快晴 guard if full consistency is wanted.

## Limits
- Dictionary senses were not re-verified beyond the JMdict numbers cited in the cards.
- Body glosses for 無限 (34-35) and 休業 (29) looked fine but I did not judge them against the target titles in detail.
- 118 strokes hash mismatches are CRLF-only and were not treated as defects.
- Blind review: I did not read other review reports or the scratch worktrees.
