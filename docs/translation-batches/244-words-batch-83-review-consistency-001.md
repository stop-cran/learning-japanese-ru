# Batch 244 (244-words-batch-83) — consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `c21597475cf24f578b35cc6636257450f8a80902` (tree `ba7eb57a671e3585fadb94026d9d505021a0444a`),
> the signed candidate pushed before review.
> Later reconciliation is in `244-words-batch-83-recheck-001.md`.

## Snapshot
Commit c21597475cf24f578b35cc6636257450f8a80902, clean working tree. `python tools/validate.py`: 0 errors. Diff against parent 7e2b446…: 36 files (30 new words, 4 navigation files, manifest.json, intake JSON). No stray files.

## Scope
Read all 30 new cards in full. Read all 4 navigation diffs (作家, 性, 性格, 重点) in full. Read the intake JSON and the manifest diff. Compared each card to the frozen EN source with scripts: front matter, exclusion prefix, links and structure.

## Verdicts
- Consistency, format, links, navigation: CLEAN.
  - Front matter matches EN apart from title and exclusions.
  - Every EN exclusion is kept as an ordered prefix.
  - All links resolve.
  - The only links not added are to targets absent from RU: kanji 純/滴/粒/算/筆, 掃く, ブラシ, and the occupation article.
  - The four navigation changes are one-line link-only edits at the EN positions.
- Intake JSON and manifest: CLEAN on the checks I ran.
  - The intake path list equals the words diff (34 paths).
  - Every candidateRawSha256 matches the file on disk.
  - The manifest diff only adds the 30 entries, updates 4 hashes and changes contentVersion.
- Quiz safety: NEEDS FIX. One required finding (F1) and four conservative ones (F2–F5). Three RU-added guards need no change.

## Findings
**F1 (required). 組み立てる vs 集める / 拾う** — `words/組み立てる.md` line 9.
- The RU title «собирать из деталей…» makes bare «собирать» a defensible answer.
- 集める «собирать; коллекционировать» and 拾う «подбирать; собирать» also contain it.
- Neither side has a guard.
- Remedy: append `集める, 拾う` to 組み立てる `quiz_exclusions`. 集まる is optional.

**F2 (conservative). 素直 vs おとなしい** — `words/素直.md` line 9.
- «покладистый» plus the obedience teaching in the body overlaps おとなしい «послушный».
- Remedy: add おとなしい.

**F3 (conservative). 終点 vs 停留所** — `words/終点.md` line 9.
- Both titles share «остановка».
- Remedy: add 停留所.

**F4 (conservative, low). 等分 vs 区分** — `words/等分.md` line 9.
- Both titles share «деление».
- Remedy: add 区分.

**F5 (conservative, low). 気配 vs 機嫌** — `words/気配.md` line 9.
- «настроение (рынка)» overlaps 機嫌 «настроение».
- 機嫌 already guards 気分, 気 and 気持ち.
- Remedy: add 機嫌.

### RU-added guards (keep; no action)
- 作者→著者: justified. The 作者 example translates 作者 as «автор», and the 著者 title is «автор (книги, труда)».
- 性質→性能: conservative. The basis is weak (nature vs performance) but harmless.
- 書留→速達: conservative, bordering on unjustified. The only basis is the shared noun «отправление». Harmless; keep or drop at the author's discretion.

### No guard needed
経度, 紫, 素人, 水滴, 箒, 執筆.

## Optional (EN-inherited, not batch defects)
- 算数: tags lack `kango` although the type is kango.
- 紫: tag `colors`, while the repo uses `color`.
- 作者 and 算数: kana examples have internal spaces, and comparison lines omit parentheses around readings.
- 算数: footer URL is percent-encoded, unlike the others.
- 算数: example 18 renders 算数の宿題 as «домашнее задание по математике». This is mildly in tension with the card's own warning about «математика».
- 筆者 vs 私 and 第一 vs 主要: an optional guard at most.
- 素質: learner prose mentions «исключения в викторине».

## Limits
- I did not run build_manifest.py, link_parity.py or word_title_screen.py, because the instructions forbid generators or writing files, or I did not get to them.
- I did not fully recompute manifest hashes. A disk-hash check showed 118 strokes/*.json mismatches. This is probably CRLF checkout normalisation, because the strokes files are not in the diff. A committed-blob check timed out, so this is unresolved.
- Two `scenes/*.json` files (きらきら, にこにこ) are not in the manifest. They are outside the batch, and I did not check whether this is intended.
- Footer URLs and sense numbers were not diffed character by character against EN.
- I did not judge the accuracy of the Russian titles in depth.
- No `__pycache__` was created.
