# Batch 197 — independent review 001

## Snapshot and scope

- Reviewed commit: `5dd9a78f4e6d2f806be09953326bf77cb8e77c47` (tree `aa153ae4edbd312c5336da1a9ad2a142f9433e60`), branch `full-ru-197-words-36`, parent `59b6e51`.
  The candidate was committed signed directly and pushed before review.
- Published baseline recorded in the intake: `e007e0b` (B196 merge). Parent `59b6e51` adds only the B196 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness and consistency also inspected the 11 navigation-only files (16 restored links).
  - Consistency additionally covered `manifest.json` and the intake.
  - Comprehensibility read the new cards and the named comparison cards, without separate verdicts on the link-only edits.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD and the working tree were unchanged.
- Full blind reports:
  - `197-words-batch-36-review-correctness-001.md`
  - `197-words-batch-36-review-consistency-001.md`
  - `197-words-batch-36-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's reports.
  The consistency reviewer ran its own stem and exact-segment title screen of every new title against all 2,563 RU word titles.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN** for all 30 cards; scoped coverage **NEEDS FIX** for 結果 only (C197-2).

- C197-2 (minor, high confidence): `結果.md:28` changed the frozen EN reading note "The reading is ケッカ, with a small っ."
  to «Чтение — けっか…». The pronunciation is the same, so this is a source-preservation defect, not a linguistic error.
- Optional: `経由.md:36` «на полпути маршрута или дела» could read «в пути или в процессе дела», closer to EN "partway through a
  route or activity". The reviewer withdrew its provisional C197-1 as a defect: JMdict 途中 sense 2 lists "midway; halfway", and
  Russian «на полпути» can be figurative.
- Optional: `結局.md:41` could drop the comma in «В конце концов, он же ребёнок» (Russian punctuation polish).
- The reviewer inspected the Jisho/JMdict entries for all 30 headwords, including the separate 直（なお）, 位（い） and くらい
  entries, and entries for the added comparisons (判断, もうすぐ, どの, できるだけ, なるべく, 販売, 売る, 見解, 行儀, 承知, 額, 曲, けち,
  手, 会, 答, 途中). Where Jisho rate-limited 粉, 節約, 節, 答案 and 筆, it read the デジタル大辞泉 entries on kotobank and later
  obtained the Jisho entries with paced requests. It also read デジタル大辞泉 通過, 省く (sense 2, 手間を省く), 水準, 特徴 and 以下
  (inclusive numerical limit).
- For the Russian-only adaptation in 結局 it inspected the Большой универсальный словарь entry В КОНЦЕ КОНЦОВ¹ sense 2.0, which
  supports the decisive-argument use. The coordinator had checked the same entry before review because the author flagged the
  claim as unverified.
- It ran the validator (0 errors) and confirmed that removed source link targets are absent from RU, with every visible
  Japanese label retained.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **CLEAN**; scoped cross-file integration **CLEAN**. No findings.

- Front matter other than title and `quiz_exclusions` is identical to EN for all 30 cards. The commit contains exactly 43 files
  (30 cards, 11 restorations, manifest, intake). All 41 intake payload hashes recompute.
- All EN exclusions are retained, every exclusion target exists, and no new title equals another card's whole title or segment.
- The 16 restored links sit at EN link positions and resolve; `diff -U0` shows link markup only. No RU-only link was added.
- The reviewer ran the validator (0 errors), `build_manifest.py` (no diff) and the link-parity helper (no LOST/EXTRA in the
  41 changed files).
- Optional: O1 組合 vs 団体/組織 (low confidence); O2 節約 vs 貯金 «экономия»/«сбережения»; O3 今に vs 先 (not recommended);
  O4 the RU-added comparison sentences supporting extra guards are unlinked, and their linguistic accuracy belongs to the
  correctness facet.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (節約, 組合); scoped coverage **CLEAN**; the other cards **CLEAN**.

- Finding 1 (minor, high confidence): `節約.md:37` gives 手間を省く without a reading although 省く（はぶく） on the same line has one.
- Finding 2 (minor, high confidence): `組合.md:18` gives the bold pattern **組合の会員** without a reading, while the paired pattern
  **組合に入る** in the same sentence has one. EN has the same omission.
- Optional polish: 節 不思議な節 «что-то странное» (as in EN); the 結果 example translation «Разобравшись…» versus the card's
  «в результате проверки» gloss; 籠 «вылетела» adds flight to 出ました (EN "came out"); residual meta wording in 管; the
  titles «путь через» (経由) and «истекать (о времени)» (経つ); no prose contrast for 範囲 vs 幅 (EN has none; 幅 is excluded).
- The reviewer confirmed that 直 / 今に / やがて / いずれ, 結局 / 結果 / 結論, the six position and rank cards and the other named
  pairs are distinguished in prose.

No finding established a missing requested card, an incorrect Japanese example or a necessary prerequisite omission.

## Exclusion classification: author and consistency reviewer

The author added 23 direct, one-sided exclusion pairs beyond EN on the new cards. All 33 EN exclusion entries are retained.
The author report and the blind consistency reviewer classified them independently. The differences are preserved here
rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `今に`→`いずれ` | required | conservative |
| `いずれ`→`どの` | required | conservative |
| `いずれ`→`どっち` | required | conservative |
| `経由`→`通過` | required | conservative |
| `態度`→`行儀` | conservative | required |
| `級`→`水準` | conservative | required |
| `納得`→`承知` | conservative | required |
| `精々`→`以下` | conservative | required |
| `節約`→`省く` | conservative | required |
| `節`→`特徴` | conservative | required |
| `筆`→`手` | conservative | required |

Both classify `結論`→`判断`, `今に`→`もうすぐ`, `結局`→`末`, `立場`→`見解`, `節`→`曲` and `答案`→`答` as required, and
`営業`→`売る`, `位置`→`所`, `位置`→`場`, `位`→`くらい`, `範囲`→`額` and `節`→`点` as conservative. The reviewer judged none of the
23 unjustified, and none guards a contrast that a card teaches. The `節約`→`貯金` guard added after review in response to O2
brings the RU-added total to 24 and is recorded in the recheck record.

Reconciliation, the coordinator's dispositions and the final verdicts are in `197-words-batch-36-recheck-001.md`.
