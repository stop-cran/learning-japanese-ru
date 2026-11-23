> Original blind consistency review of `bbe4e485115525a1f4bd661960486449dbe4570b` (tree `a46d590fde1002c23b72346587efb6c17d0ea7c7`).
> Runtime identity verified by the coordinator: `claude-sonnet-5.5`, agent `99dd73a9-bf30-4991-870c-6ced97d29aca`.
> [Reconciliation at the signed fix](253-words-batch-92-recheck-001.md). The report below is unchanged apart from LF line endings.

# B253 consistency and quiz-safety review

## Snapshot
- Repository: `C:\Users\romanko\repos\learning-japanese-ru`, branch `full-ru-253-words-92`.
- HEAD was `bbe4e485115525a1f4bd661960486449dbe4570b` at the start and at the end. Parent: `7126ab8b`.
- The diff has 41 files: 30 new word cards, 9 navigation edits, `manifest.json`, and the intake JSON.
- `python tools/validate.py` printed `0 error(s)`.

## Scope
This was a blind, read-only review. I read these in full:
- all 30 new word cards;
- all 9 navigation diffs (kanji 乾, 劇, 帯; words 乾く, 泉, 濡らす, 熱帯, 芝居, 零点);
- the quiz rules in RU `copilot-instructions.md`;
- the whole brief.

I compared mechanically against the frozen EN repo:
- front matter;
- links;
- footer URLs;
- link targets;
- manifest hashes.

I read the intake JSON only for its path list and for learner content. I did not read any other reviewer's report, author report or prompt, or `docs/translation-batches` beyond that one intake file.

## Verdicts
- Consistency: **PASS** with minor, non-blocking notes (2 Low, 2 Info).
- Quiz safety: **PASS, with conservative guards noted.** No EN guard was dropped. No guard is a self-reference or duplicate. No unguarded pair that I found is a real confusion risk. Necessity of the RU-only guards is **UNVERIFIED**, not CLEAN.

## Mechanical results
- **Front matter:** word, reading, jlpt, type, kanji, tags and `quiz_exclusions` match EN for all 30 cards.
  - The only differences are the 14 RU-only guards listed below. Each is appended after the EN entries.
  - 漁師, 滝 and 温室 have no `quiz_exclusions` key in RU or EN. I judge that fine.
  - 混ぜる, 混じる and 混ざる have `type: wago` without a `wago` tag. EN is identical, so this is an EN-parity note, not an RU defect.
- **Links:**
  - No RU-only links.
  - The EN links missing in RU all point to absent targets: kanji 漁, 溶, 岩, 混, 湿, 蒸, 湯, 測, 量, 温, 泉, 清, 掃, plus 湧, 渇 and 滝, and the word 噴火. Plain text is the convention for absent targets.
  - All RU link targets exist.
  - Every EN file that links one of the 30 words either has a RU counterpart with the same link, or has no RU file.
- **Navigation edits:** each is a one-line change of link brackets and href only.
  - Kanji files use `../words/X.md`; word files use `X.md`.
  - The intended targets are correct: 乾→渇く, 劇→演劇, 帯→温帯, 乾く→渇く, 泉→温泉, 濡らす→湿る, 熱帯→温帯, 芝居→演劇, 零点→満点.
  - 熱帯 keeps its 暑い link, and 寒帯 stays plain.
- **Footers:** all JMdict, Weblio and Kotobank URLs equal EN.
  - The 満点 and 満員 Weblio URLs are percent-encoded, as in EN.
  - 渇く uses Kotobank, as in EN.
- **Manifest:** I did not regenerate it. I hashed all 39 changed word and kanji files with SHA-256 and compared them to `manifest.json`. 0 stale entries, and the 30 new entries are present.
- **Intake JSON:** the path set (39 words and kanji files) equals the content diff. It has no Cyrillic, so it adds no learner content.
- **Quiz exclusions:** the title screen shows only lexical-stem overlaps, with no exact comma-segment hits.

## RU-only guards (14): classification
I did not open JMdict. The "basis" below comes from the RU titles and general dictionary knowledge. Necessity is UNVERIFIED for every row. A guard is only harmful if it is unjustified, and I found none that is.

| Card → guard | Basis | Class |
|---|---|---|
| 演劇→公演 | 公演 «выступление артистов; спектакль» is a performance. 演劇 is the theatrical art. Both overlap in «спектакль/театр». | conservative |
| 演劇→芸術 | The titles share «искусство». | conservative |
| 演劇→芸能 | 芸能 «исполнительские искусства». It shares «искусство» with the 演劇 title. | conservative |
| 溶かす→溶け込む | A transitive/intransitive family. Both render with «раствор…». | conservative |
| 溶け込む→加わる | The «вливаться (в коллектив)» sense is close to joining a group. | conservative |
| 売り切れる→特売 | Both titles use «распрод…». | conservative |
| 売り切れ→特売 | Same as above. | conservative |
| 満員→あふれる | «переполнен…» vs overflow. | conservative |
| 満員→大勢 | «полный людей» vs «много людей». | conservative |
| 湯気→もくもく | Both titles use «клуб…». | conservative |
| 温帯→適度 | Both titles use «умеренный», but the senses differ (zone vs degree). Weakest basis. | conservative, see F2 |
| 付き合う→会う, お目に掛かる | Title «общаться; …» shares «встречаться» with 会う. | conservative |
| 深夜→徹夜 | Both are «ночь» words. 徹夜 is «бодрствование всю ночь». | conservative |

None is an antonym or a contrast the article teaches, so none is "unjustified" in the contract's sense.

## Findings

### F1 (Low) — 溶け込む title and example add «полностью»
- File: `words/溶け込む.md`, title and example 砂糖が水に溶け込みました.
- Claim: EN is "dissolve into; blend in". The RU title and the example render this with «полностью», which EN does not have.
- Impact: it is a minor over-translation. The title is also long for a quiz label.
- Remedy: drop «полностью» and use «растворяться (в жидкости); вливаться (в коллектив)».
- Evidence: comparison with EN. Confidence: medium.

### F2 (Low) — 温帯→適度 guard is weakly grounded
- File: `words/温帯.md`, `quiz_exclusions`.
- Claim: the only link is the shared stem «умеренный». The senses differ: 温帯 is a climate zone, 適度 is a moderate degree.
- Impact: it is harmless over-guarding. It does reduce the distractor pool slightly.
- Remedy: keep it, or remove `適度` if the pool matters. Necessity is UNVERIFIED.
- Confidence: low.

### F3 (Info) — 水蒸気 title «горячий пар» may blur the 湯気 distinction
- File: `words/水蒸気.md`, title. The card teaches the 湯気 distinction at around line 31.
- 湯気 is already guarded against 水蒸気, so no quiz defect.
- Remedy: optional. Consider «водяной пар; пар» for the second segment.

### F4 (Info) — Small wording deviations from EN
- `words/湧く.md` drops EN's note that neither 湧 nor 渇 has a kanji card but 湧 still belongs in the written-kanji metadata. The metadata is correct, so this is acceptable.
- `words/清掃.md`: the title «очистка; уборка территории» is narrower than EN "cleaning; cleanup". The body covers the broader sense, including refuse removal.

## Optional
- Unguarded in-batch pairs 水蒸気–温泉, 温泉–湯気, 混じる–満員, 深まる–湧く, 満点–満員, 湿る–湯気, 湿る–水蒸気, 温泉–温帯, 温泉–温室, 温帯–温室, 深夜–深まる: the senses are distinct. The overlap is only «горячий» or «пар». No guard is needed.
- External overlaps I screened and judged not worth a guard:
  - 満点 vs 結果 and 松;
  - 水蒸気 and 湯気 vs 湯 and ほかほか;
  - 測定 vs 確認, 調べる and チェック;
  - 清掃 vs 区域 and 雑巾;
  - 混合 and 混ぜる vs ボール;
  - 渇く vs 苦しむ and 貧しい;
  - 湿る vs 気分 and 機嫌;
  - 売り切れる vs 存在 and 現金.
- I did not review linguistic accuracy; that belongs to the correctness reviewer.

## Limits
- I did not consult JMdict or any live dictionary. Dictionary bases are from titles and general knowledge, so necessity is UNVERIFIED.
- Line-count differences from EN (演劇, 漁師, 滝, 溶岩, 溶かす, 溶く, 湧く, 温帯) were examined only at the footer-URL level. I did not enumerate every adaptation.
- `validate.py` created an untracked `tools/__pycache__/`. I removed it. At the end `git status --porcelain` was empty and HEAD was unchanged.
- I did not run `build_manifest.py` or any other generator.
