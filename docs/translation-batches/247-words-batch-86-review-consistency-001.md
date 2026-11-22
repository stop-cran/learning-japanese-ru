# B247 (247-words-batch-86) blind review: consistency, quiz safety, integration

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `83b26408e9899c14813ea3226de3a04c72164abf` (tree `96d36fd6130dc64d3cb202f00e98df2330547687`),
> the signed candidate pushed before review.
> Later reconciliation is in `247-words-batch-86-recheck-001.md`.

## Snapshot
- RU candidate 83b26408e9899c14813ea3226de3a04c72164abf (parent ac67a60). HEAD matches; working tree clean.
- `python tools/validate.py`: 0 error(s). (It created an untracked `tools/__pycache__`; I deleted it, tree clean again.)
- Commit touches 35 files: intake JSON, manifest.json, kanji/着.md, words/被せる.md, words/頭.md, 30 new words/*.md.

## Scope
Read in full: all 30 new RU cards and the 3 navigation diffs (kanji/着.md, words/被せる.md, words/頭.md).
Compared against frozen EN: front matter, H2 structure, link sets, quiz_exclusions, footer URLs and JMdict entry numbers (programmatic, all 30). EN bodies read line by line for only 14 cards (倣う, 真空, 官庁, たちまち, 垂直, 真っ青, はじめに, 真似る, 真っ先, 相互, 先頭, 直前, 目覚まし, 着せる). The other 16 were checked structurally only.
Intake JSON (only permitted exception): its 33 payload paths equal the content diff exactly, all candidateRawSha256 values match the working-tree bytes, held is empty, and it carries no learner content.
Manifest: after CRLF normalisation (as build_manifest does) all 5524 hashes match. The diff touches only the 33 changed files plus contentVersion. I did not recompute contentVersion and did not run the generator.
Did not read: scratch worktrees, author or reviewer reports, translation-batches/drafts/tracking other than the intake JSON. The title-screen tool output was only partly read (slow); I supplemented it with grep over RU titles.
Not verified: Russian linguistic correctness beyond consistency; tag-vocabulary and byte-format (CRLF/BOM) scan was started but not completed. Validator passing covers schema and tags.

## Verdicts
- Consistency: CLEAN
- Quiz safety: CLEAN (no missing required guard; one over-guard, see Optional)
- Integration / manifest: CLEAN

## Findings
None blocking or required.

Evidence behind the verdicts:
- Front matter (word, reading, jlpt, type, kanji, tags) identical to EN for all 30 cards. Section order matches the RU convention.
- Links: all links match EN except targets with no RU file (words/住まい, 水平, 曲線, 一斉, 円周; kanji/庁, 県, 角, 線, 倣), which are rendered as natural plain text in 相撲, 垂直, 直線, たちまち, 直径. No RU-only links. No inbound link lost: EN inbound links come only from files absent in RU.
- Navigation: 着せる linked in kanji/着.md (L38, L52) and words/被せる.md L46; 先頭 linked in words/頭.md (L33, L48). Only brackets/hrefs changed, path forms identical to EN. The plain mention at kanji/着.md:62 is a pre-existing RU-only sentence; fine.
- quiz_exclusions: all EN entries kept, in order, plus exactly 5 RU additions. All targets exist; no self-reference or duplicates. Exclusions are one-sided by contract, so no reverse declaration is needed.
- RU additions classified:
  - 官庁→機関: warranted. Both titles share «учреждение»; JMdict 機関 sense 1 is institution/agency.
  - たちまち→瞬間: warranted, conservative. Both carry «мгновение».
  - 直前→直に, 直前→直接: conservative. Shared «непосредственно» makes a defensible overlap.
  - 直線→直通: weakest; only shared word is «прямая», nouns differ (линия vs связь). Harmless over-guarding.
- Unguarded stem-only neighbours (看病 vs 育児/美容 «уход за…», 相撲 vs 戦い, 相互 vs 交流/仲, 直線 vs 境界/方針/系統, はじめに vs 開始, 直角 vs 隅/街角): none are defensible correct answers; no guard needed.
- Titles unique; footers/URLs match EN.

## Optional
1. たちまち title drops EN's "suddenly" sense (JMdict sense 2); 突然/急に/急激 guards already cover it.
2. 真空:18 renders 容器 as «сосуд» while the 容器 card title is «контейнер; тара».
3. 相互 title «взаимный; обоюдный» is adjectival though the word is a noun taking の; body clarifies.
4. 直前 («Исходный список закрепляет…») and 目覚まし («запись из исходного списка») contain author-process wording; EN has the same.
5. 直線→直通 could be dropped (see above); keeping it is harmless.

## Limits
Blind review; 16 of 30 EN bodies compared structurally only; title-screen output partly read; contentVersion not recomputed; no linguistic verdict on Russian quality.
