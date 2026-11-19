# B188 Russian word-card batch: consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `c721e1cb63f33938081927e236dc7f9674f073b6`. Later reconciliation in
> `188-words-batch-27-recheck-001.md` corrects this report's symmetry assumption: one-sided declarations are sufficient.

**Verdict: facet NEEDS-CHANGES; scoped coverage NEEDS-CHANGES.**
Nothing is blocking structurally: the validator, the manifest and every intake hash are clean. The blockers are quiz-safety gaps in the exclusion pool and one title/heading mismatch. Together with the missing progress/tracking update for batch 27, these should be fixed before publication.

## Snapshot and scope

- **RU:** `C:\Users\romanko\repos\learning-japanese-ru`, branch `full-ru-188-words-27`, HEAD `c721e1cb63f33938081927e236dc7f9674f073b6` (verified).
- **EN frozen:** `C:\Users\romanko\repos\learning-japanese-en-frozen`, `6af98cb717755690a9ca793e5454a96ebd7a8f9f` (verified).
- **Commit:** a single commit changing 41 files, with parent `ef4553a`.
- **Read in full:**
  - all 30 new `words/*.md` cards;
  - the 3 touched kanji cards: `刻`, `路`, `遅`;
  - the 5 touched word cards: `回復`, `幸せ`, `現在`, `町`, `高速`;
  - `articles/numbers-and-counters.md` (diff);
  - `manifest.json` (rebuilt and compared);
  - `docs/translation-batches/188-words-batch-27-intake.json`;
  - the format and instruction excerpts on quiz exclusions, batches and links;
  - the EN `docs/confusable-words.md` (only CW086 is relevant, and `勧める` has no card).
- **Not consulted:** the title-screen output, the author report and prompt, and other reviews. The title and collision checks below come from my own scan of all 2,293 RU word cards.
- **Reviewer model:** execution metadata does not expose it, so I am not stating one.
- **Correctness of Japanese and comprehensibility of Russian:** UNVERIFIED. I looked at Russian only where it changes how a quiz answer reads.

## Checks that passed

- `python tools/validate.py` reports 0 errors.
- `python tools/build_manifest.py` produced no manifest change. My validate run left a `tools/__pycache__` folder, which I removed; the tree is clean again.
- All 39 payload entries in the intake match the candidate files (raw SHA-256) and the frozen EN files (raw SHA-256).
- The 30 cards match EN in `word`, `reading`, `jlpt`, `type`, `kanji`, `tags` and the section count (4 each).
- Compared with EN, the RU cards add `quiz_exclusions` pairs on 9 cards and drop 15 links:
  - **Added pairs** (`遂に`, `前進`, `進学`, `週間`, `速度`, `通行`, `通過`, `通学`, `通り過ぎる`): every target exists. This is a positive.
  - **Dropped links** (`礼儀`, `以前`, `未来`, `経つ`, `暮らす`, `不幸`, `欠席`, `就職`, `勧める`, `仲間`, `成功`, `優勝`, `../kanji/改`): all of these cards are absent in RU, so plain text is correct.
- Every other new link resolves, including the 8 added to existing cards and the article link to `週間`.
- Headings, facts and section order are consistent across the 30 cards, except for the `進める` mismatch below. The RU full-width `（）—` heading format is used throughout.
- Titles:
  - Exact duplicate: `運` and `幸運` ("удача; везение"), mitigated by `幸運`→`運`.
  - Second exact duplicate: `遂に` and `とうとう` ("наконец; в итоге"), mitigated by `遂に`→`とうとう`.
  - There are no duplicate kanji-card titles; no kanji cards were added.
- The three touched kanji cards (`刻`, `路`, `遅`) previously had no linked word, so linking them is justified coverage.

## Findings

I assumed `quiz_exclusions` pairs are symmetric, as `docs/content-format-reference.md:98` says. The validator allows one-sided declarations (`test_validate.py:535`), and I could not confirm how the app enforces them.

### Medium

**M1. Quiz safety: `運` and `幸運` have no exclusion with `幸せ` or `幸福`.**
- **Files:** `words/運.md:4,9`, `words/幸運.md:4,9`, `words/幸い.md:4,9`, `words/幸せ.md:4,9,16`, `words/幸福.md:4,9`.
- **Claim:** `幸せ.md:16` itself glosses 幸せ as «счастье; удача», but `幸せ` is excluded only against `幸福` and `喜び`.
  - `運` («удача; везение») and `幸運` («удача; везение») are therefore valid-looking answers or foils for `幸せ`.
  - `幸い` («удача; к счастью») excludes `幸運` and `幸せ` but not `幸福`.
  - `幸福` («счастье; благополучие») overlaps with `幸い`, whose dictionary sense also includes happiness.
- **Learner impact:** a learner can be marked wrong for a defensible choice.
- **Remedy:** add the direct pairs `運`–`幸せ`, `幸運`–`幸せ` and `幸い`–`幸福`. Do not add transitive pairs.
- **Confidence:** high for `幸せ` (the card's own text), medium for `幸福`.

**M2. Quiz safety: `違いない` has no exclusion with `確か`.**
- **Files:** `words/違いない.md:4,9`, `words/確か.md:4,9`.
- **Claim:** `確か` («достоверный; кажется») is a "certain" word, and the `違いない` card compares it at lines 36–38. `違いない` («несомненно; наверняка») excludes only `きっと`.
- **Remedy:** add `違いない`–`確か`.
- **Confidence:** medium.

**M3. Quiz safety: `遅刻` has no exclusion with `遅れる`.**
- **Files:** `words/遅刻.md:4,9`, `words/遅れる.md:4,9`.
- **Claim:** «опоздание» and «опаздывать; задерживаться» are the same concept in different parts of speech. `遅れる` excludes only `遅い` and `押す`.
- **Learner impact:** a noun versus verb difference is a weak basis for a wrong answer.
- **Remedy:** add `遅刻`–`遅れる`.
- **Confidence:** high.

**M4. Quiz safety: `連想` has no exclusion with `関連`, `関係` or `連絡`.**
- **Files:** `words/連想.md:4,9`; `関連` (`:4`: «связь; отношение к теме») and `関係` (`:4`: «связь; отношения») at `:9`.
- **Claim:** the new title «ассоциация; ассоциативная связь» contains the generic word «связь». Nearby `связь` labels exist on `連絡`, `関係` and `関連`; `連絡` is already excluded against `関連`.
- **Remedy:** add direct pairs, or retitle `連想` to «ассоциация» (the retitle needs its own review).
- **Confidence:** medium.

**M5. Quiz safety: `連続` has no exclusion with `次々` or `連休`.**
- **Files:** `words/連続.md:4,9` (body lines 16, 19, 20, 41–43 use «подряд»), `words/次々.md:4,9`, `words/連休.md:4,8`.
- **Claim:** the body teaches 連続 as «подряд», which is the whole `次々` title («один за другим; подряд») and part of `連休`'s («несколько выходных подряд»). The `連続` title («череда; последовательность») hides that sense. The repository guidance (the 力–左右 example) says to check meanings that sit in the body but not the title.
- **Remedy:** add `連続`–`次々` and `連続`–`連休`.
- **Confidence:** medium.

**M6. Quiz safety: `進歩`, `上達` and `改善` overlap with `伸びる` and the «развитие» family.**
- **Files:** `words/進歩.md:4,9`, `words/上達.md:4,9`, `words/改善.md:4`; `伸びる.md:4,9,17,44` («…улучшаться»; exclusions `[成長, 増える]`); `発展.md:4`, `成長`, `発達`.
- **Claim:** `伸びる` has an explicit «улучшаться» sense in its title and body. It is not excluded against `改善`, `進歩` or `上達`. `進歩.md:42` also frames the word as «развитие», but `進歩` has no pair with `発展`, `発達` or `成長`.
- **Remedy:** add `伸びる`–`改善`, `伸びる`–`進歩`, `伸びる`–`上達`, and at least `進歩`–`発展`.
- **Confidence:** high for `伸びる`, medium for the rest.

**M7. Reader-visible inconsistency: the title and heading of `進める` differ.**
- **File:** `words/進める.md:4` has `title: продвигать; вести дело вперёд`; `:12` has `# 進める（すすめる）— продвигать; продолжать дело`.
- **Claim:** all 29 other cards have an H1 that matches the title exactly, and the validator does not catch this one. The H1 «продолжать дело» also drifts toward `続ける` («продолжать»), which the card contrasts at lines 33–34.
- **Learner impact:** the quiz answer and the card heading differ.
- **Remedy:** make the H1 match the title, or change both together.
- **Confidence:** high.

**M8. Batch-integration gap: no progress or tracking record for batch 27.**
- **Files:** `docs/translation-progress.json` and `docs/translation-tracking.json` contain 0 references to `188-words-batch-27`. For example, `words/通り過ぎる.md` is still `"status":"pending","adopted":false` in the progress file.
- **Claim:** B187's batch commit (`6722867`) updated both files with 282 references each, so this one is still outstanding. It may be a planned post-review step; if so, it must still land before publication.
- **Remedy:** run the progress and tracking update for B188. The intake also records `baseline 6722867` while the parent is `ef4553a`; that parent only adds a docs-only verification file, so it is informational.
- **Confidence:** high that it is missing; medium on whether it is required before publication.

### Low

**L1. Quiz safety: weaker overlaps between labels.** Each of these is a possible direct pair, or a note that the overlap is accepted:
- `合格.md:4` and `試験.md:4`: both contain «экзамен».
- `通信.md:4` and `放送.md:5`: «передача информации» against «передача».
- `通行.md:4` and `前進.md:4`: «движение; проезд» against «движение вперёд».
- `前進.md:4` and `進める.md:4`: both contain «вперёд».
- `過去.md:4` and `昔.md:5`: «прошлое» against «давние времена»; the card contrasts them at lines 32–34.
- `週間.md:4,10` and `時期.md:4`, `時代`: the generic «период»; `期間` is already excluded.
- `道路.md:4` and `通学.md:4`, `坂.md:4`: «дорога» against «регулярная дорога в школу» / «наклонная дорога».
- `過ごす.md:4` and `行う`: «проводить» against «проводить время».

**L2. Tags: seven cards omit the word-type tag that about 90% of the corpus carries.**
- **Files:** `違いない` (wago), `遂に` (wago), `友` (wago), `運` (kango), `進歩` (kango), `週` (kango), `連想` (kango). The corpus count is 750 of 824 kango and 1,225 of 1,315 wago cards. All seven match the frozen EN source, so this is inherited. I did not find a validator rule against it; the format reference had no tag rule I could cite.

**L3. Coverage gaps: five kanji have no RU card.**
- `徳`, `遂`, `改`, `善`, `逮` are listed in the `kanji:` fields of the new words, so the metadata is correct. `改` exists in the frozen EN source but not in RU; the other four have no card in either repository.
- The `改善` and `逮捕` bodies therefore have plain text where EN links `改`. No stroke files exist for these kanji.

### Optional navigation

- `週.md:34` compares 週間 without linking it, although `週間` is now an article and links back to `週`.
- 15 kanji cards (`去`, `過`, `進`, `週`, `間`, `連`, `続`, `達`, `速`, `格`, `通`, `信`, `道`, `止`, `終`) list new words as plain text. These cards already have at least one linked word, so this is not required.
- When the cards for `勧める`, `仲間`, `以前`, `未来`, `礼儀`, `不幸`, `欠席`, `就職`, `成功`, `優勝`, `経つ` and `暮らす` arrive, restore the links dropped from EN. The `勧める`/`進める` homophone pair (CW086) will also need a direct quiz-exclusion pair.

## Limits

- I did not run the app, so exclusion symmetry and option generation are inferred from the docs and the validator tests.
- Quiz-pool overlaps come from title and token matching plus judgement. A pair I did not flag is not proven safe.
- Japanese accuracy, Russian comprehensibility and JMdict sense correctness are UNVERIFIED, apart from the quiz-meaning points above.
