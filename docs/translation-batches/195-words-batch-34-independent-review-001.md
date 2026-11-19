# Batch 195 — independent review 001

## Snapshot and scope

- Reviewed commit: `4a2fd76f6380d7478317c486f1042215190a5934` (tree `02afdeec8bfbf21e076e959600ab7ed18980f642`), branch `full-ru-195-words-34`, parent `68c4917`.
  The candidate was committed signed directly and pushed before review.
- Published baseline recorded in the intake: `c79168c` (B194 merge). Parent `68c4917` adds only the B194 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness and consistency also inspected the ten navigation-only files.
  - Consistency additionally covered `manifest.json` and the intake.
  - Comprehensibility read the link-only edits as context, without separate verdicts.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD and the working tree were unchanged.
- Full blind reports:
  - `195-words-batch-34-review-correctness-001.md`
  - `195-words-batch-34-review-consistency-001.md`
  - `195-words-batch-34-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's reports.
  The consistency reviewer ran its own title-segment collision scan against all RU word titles.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN** for all 30 cards; scoped coverage **NEEDS FIX** for 衣服 only (C1). No optional items.

- C1 (minor, high confidence): `衣服.md:45–48` dropped EN's English-plural sentence together with its Japanese rule
  that the word needs no plural ending. The rest of the category/context explanation was retained.
- The reviewer fetched the Jisho/JMdict entries for all 30 headwords, including both ライター entries, both relevant 臭い readings,
  the 行き suffix note, 天然's colloquial sense, 腰's texture sense and 自動's grammatical abbreviation, and the comparison
  entries 喧嘩, 連れ, お菓子, 苦痛 and 横. It read the Digital Daijisen 作家, 著者 and 自動 entries on Kotobank.
- Russian-only adaptations were checked against Kuznetsov («спутник», «колено», «трава») and Ozhegov/Shvedova («язык», «покончить»).
  Gramota returned HTTP 429 and one mirror HTTP 403; the reviewer used the alternative entries above.
- The reviewer ran the validator (0 errors) and confirmed that all 24 removed relative-link destinations are absent from the RU snapshot.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (F1); scoped cross-file integration **CLEAN**.

- F1 (minor, medium confidence): the RU title of 虫歯 «кариес; кариозный зуб» adds the "decayed tooth" sense,
  so «зуб; зубы» (歯) becomes a defensible answer. EN «tooth decay; cavity» has no such overlap.
- Optional: 舌→言語 (the parentheticals already disambiguate), 脇 vs 隣 (no guard needed) and the plain-text 作家 pointer
  to the untranslated article (acceptable until that article is translated).
- The reviewer ran the validator (0 errors), `build_manifest.py` (no change) and `link_parity.py` over the 40 paths, and
  recomputed the manifest and intake hashes for all 40 payloads. Its dictionary sense wording is self-declared as recalled
  rather than re-fetched.
- Its verdict parenthetical names `kanji/腰.md` as the only EN link without an RU target. That understates the unwrapped set:
  the author report lists eight absent kanji targets, fifteen absent word targets and the absent article. The coordinator checked
  that every one of these targets is absent in the RU tree, matching the correctness reviewer's count of 24 removed destinations.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (作家, 自慢); scoped coverage **NEEDS FIX** for 自慢, otherwise **CLEAN**.

- C1 (minor, high confidence): `作家.md:51` points the learner to an article on occupation and role endings that is absent from this
  edition. The rule itself is already summarised on the card, so the reviewer called it a dead pointer, not a missing definition.
- C2 (minor, high confidence for the collision): `自慢.md` shares the Russian «гордость» frame with the existing 誇り card but never
  separates the two words. The reviewer cautioned that any sharper rule would overclaim the dictionaries.
- Optional: the 衣服 example «Я переоделся из мокрой одежды» calques English "changed out of".

No finding established a missing requested card, an incorrect Japanese example or a necessary prerequisite omission.
Optional suggestions are kept in the complete reviewer reports rather than promoted to defects.

## Exclusion classification: author and consistency reviewer

The author added 14 direct, one-sided exclusion pairs beyond EN on 10 new cards. All 12 EN exclusion entries are retained.
The author report and the blind consistency reviewer classified them independently. The differences are preserved here
rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `表情`→`表現` | conservative | required (RU «выражение» collision) |
| `表情`→`現れ` | conservative | required (mild) |
| `衝突`→`喧嘩` | conservative | required (RU «конфликт» ≈ «ссора») |
| `行動`→`こと` | conservative | required |
| `衛星`→`月` | required/conservative | conservative |
| `衛星`→`友`, `連れ` | required/conservative | required (RU homonym «спутник») |
| `舌`→`言葉` | required/conservative | required |
| `脇`→`横` | required/conservative | required |

Both classify the remaining five pairs as conservative: `衣服`→`洋服`, `ライター`→`記者`, `菓子`→`ケーキ`, `飴`, and `苦しむ`→`苦痛`.
The reviewer judged none of the 14 unjustified, and none guards a contrast that a card teaches.
The author had considered and declined 虫歯→歯. The guard added after review in response to F1 brings the RU-added total to 15
and is recorded in the recheck record.

Reconciliation, the coordinator's dispositions and the final verdicts are in `195-words-batch-34-recheck-001.md`.
