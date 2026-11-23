# Batch 249 (249-words-batch-88) — consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `a8e87dd42d8d6fb01c89b03aa12b995550acc585` (tree `82d39083172fc5e751eed8b92d9932a1a19aa623`),
> the signed candidate pushed before review.
> Later reconciliation is in `249-words-batch-88-recheck-001.md`.

## Snapshot
- RU repo `C:\Users\romanko\repos\learning-japanese-ru`, HEAD `a8e87dd42d8d6fb01c89b03aa12b995550acc585` (matches the brief); `git status --porcelain` empty at start and at end.
- Frozen EN: `learning-japanese-en-frozen` (`6af98cb`).
- `python tools/validate.py`: 0 errors.
- Model identity cannot be verified from inside the session.

## Scope
Read in full: all 30 new RU word cards, and all 10 navigation-only diffs (`git diff -U0` against parent `35ae8ce`). Verified programmatically against EN: front matter, link sets, heading counts, footer entries and sense numbers. An in-memory manifest recompute equals the committed `manifest.json`. The intake JSON holds 40 payload paths equal to the 40 content-diff files, and all candidate hashes match; it contains no learner content. Titles of all 4123 RU words were screened for semantic overlap with the 30 new titles.
Incident: the in-memory manifest check created `tools/__pycache__`. I deleted it, and the tree is clean.

## Verdicts
- Consistency, links, metadata, manifest, intake: **CLEAN**.
- Quiz safety: **NEEDS FIX** (Q1 and Q2, both low-to-medium severity, moderate confidence).

## Findings

### Consistency (clean)
- Front matter matches EN for all 30 cards. The only differences are the two RU-introduced guards: 住まい→`住居` and 用途→`応用`, both appended last. All EN exclusions are retained.
- Link sets match EN, except for EN links whose RU target does not exist, which stay plain (correct by convention): 発売 (特売), 発つ (建つ), あてはめる (あてはまる), and kanji 畳, 略, 訳, 植 (in 畳む, 略す, 申し訳ない, 田植え). I confirmed these RU files are absent.
- The 10 navigation files each change exactly one target link. Paths are correct. No RU-only links appear, and plain-mention counts match EN. The only EN-only link is kanji/苗 in 苗代, which is pre-existing because RU `kanji/苗.md` is absent.
- No exact-title duplicates among the batch words.

### Q1 — 略す lacks a guard against 減らす (NEEDS FIX)
略す «сокращённо называть (записывать); опускать подробности» can share "сокращать" with 減らす «уменьшать; сокращать». EN already guards 縮める, which has the same overlap.
Remedy in `words/略す.md`: set
`quiz_exclusions: [省略, 省く, 縮める, 抜く, 削除, 詰める, 略語, 除く, 削る, 飛ばす, 減らす]`

### Q2 — 申し訳ない lacks a guard against 詫びる (NEEDS FIX)
申し訳ない «простите; непростительно» vs 詫びる «приносить извинения; просить прощения». 詫びる already lists 申し訳, but the contract is symmetric and applies to direct pairs, so the pair must be declared on at least one side. The same relation is already guarded for 謝る.
Remedy in `words/申し訳ない.md`: append `, 詫びる` to `quiz_exclusions`.

### Classification of the RU-introduced guards
- 住まい→住居: **required**. The titles «жилище; место, где живут» and «жилое помещение; место проживания» are near synonyms.
- 用途→応用: **conservative but acceptable**. Both revolve around "применение"; 応用→用途 is not guarded, which is fine because the declaration is one-way.

## Optional (nonblocking)
- `畳む` links `広げる.md`, which EN leaves plain. The target card exists and its title fits the gloss. This is an acceptable substantive antonym link.
- `止まる.md` line 53: «другое чтение [留まる] — とどまる» is slightly ambiguous, since 留まる can be read とまる or とどまる. Suggested wording: «отдельная статья [留まる](留まる.md) учит чтению とどまる — «оставаться; пребывать»».
- Weak overlaps, judged not required:
  - 役目 vs 用 (the 用途 side already guards 用).
  - 番地 vs 番 (番号 is guarded, 番 is not).
  - 発売 vs 刊行 and 発行.
  - 留守番 vs 預かる and 預ける.
  - 生長 vs 増加 (増加 already guards 成長).
- 厚かましい has no `quiz_exclusions` key. This is fine because the neighbouring words declare one-way guards and EN has no key either.
- In-batch pairs that share only a stem and no sense need no guards: 住居–産地, 留まる–発売, あてはめる–用途, 用途–用語, 生年月日–生存, and so on.

## Limits
- No independent dictionary access beyond the cards' own citations.
- The title screen is a lead generator, not a verdict. About 520 flagged rows were mostly stem-only noise.
- Semantic judgments on the Q1 and Q2 guards and the optional items are mine. They are not tested against learner quiz output.
