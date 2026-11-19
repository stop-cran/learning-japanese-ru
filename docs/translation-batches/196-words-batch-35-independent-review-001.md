# Batch 196 — independent review 001

## Snapshot and scope

- Reviewed commit: `dd399249fe65eeba0cef005a3655cc3bc1ab874f` (tree `2585cf658a0f2479ce3fae46abb0b9c5ba55ea23`), branch `full-ru-196-words-35`, parent `ccb75fd`.
  The candidate was committed signed directly and pushed before review.
- Published baseline recorded in the intake: `4a59438` (B195 merge). Parent `ccb75fd` adds only the B195 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness and consistency also inspected the 21 navigation-only files (33 restored links).
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
  - `196-words-batch-35-review-correctness-001.md`
  - `196-words-batch-35-review-consistency-001.md`
  - `196-words-batch-35-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's reports.
  The consistency reviewer ran its own pattern-based title screen (about 200 candidate titles plus the named dense clusters).

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN** for all 30 cards; scoped coverage **NEEDS FIX** for 綿 only (F1). No optional items.

- F1 (minor, high confidence): `綿.md:19` changed the frozen EN reading gloss このしゃつはめんでできています to このシャツは…
  The pronunciation is the same, so this is a source-preservation defect, not a linguistic error.
- The reviewer inspected the Jisho/JMdict entries for all 30 headwords, including the 羽 feather/wing, badminton and hanetsuki
  restrictions, the separate counter entry, 綿's めん/わた identities and 繋ぐ's telephone sense. It read the full 缶 page for
  the ateji note, the 罹る kana note, the 精選版 日本国語大辞典 能がない subsection and the デジタル大辞泉/日本国語大辞典 才能 entries.
- For the Russian-only adaptation «старый друг» it inspected Gramota's СТАРЫЙ entry, sense 2.1.
- It ran the validator (0 errors) and confirmed that the 21 removed internal-link instances point to cards absent from RU,
  with every visible Japanese label retained.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (F1); scoped cross-file integration **CLEAN**.

- F1 (minor, medium confidence): 老人 «пожилой человек» has no guard against おじいさん «дедушка; пожилой мужчина» or
  おばあさん «бабушка; пожилая женщина», so 老人 is a defensible answer for either. EN has the same gap; the RU titles make it
  more explicit.
- Optional: 考え vs 計画/案, 絶対 vs 決して, and 肌 vs 革 (no guard needed).
- The reviewer ran the validator (0 errors) and `build_manifest.py` (byte-identical), recomputed all 51 intake hashes,
  compared 42 EN links to the 30 words in RU-existing files (0 differences) and diffed the 33 navigation restorations
  (link markup only). It inspected Jisho entries for 支える and 肌; other exclusion bases came from the cards' own text.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (能力, 能, 皮, 羽, 綿, 考慮, 絶対, 老人); scoped coverage **NEEDS FIX**
(能力, 能, 綿, 考慮, 絶対, 老人); the other cards **CLEAN**.

- C1: 能力 described 才能 as «природную одарённость», and the 能 / 才能 talent contrast stayed circular.
- C2: lowercase «театр но» reads as the Russian conjunction «но».
- C3: 綿 excludes 木綿 but never contrasts it.
- C4: 考慮 never separates weighing a factor from 尊重's «учёт».
- C5: 絶対's «обязательно» collides with the excluded ぜひ without explanation.
- C6: 老人 does not contrast おじいさん or おばあさん.
- C7: 羽 kept author-facing notes about the source list, the compiler's intention and N3.
- C8: «ханэцуки» is a bare Cyrillic transliteration.
- C9: 皮 pointed at an unseen «исходный смешанный список значений».
- All nine were rated minor. Optional polish items (保存/維持, 結ぶ/繋ぐ, 繰り返す/復習, 給料, 考え/意思, 缶, 能く) are kept
  in the complete report rather than promoted to defects.

No finding established a missing requested card, an incorrect Japanese example or a necessary prerequisite omission.

### Evidence disagreement preserved: 才能 and innateness

The correctness reviewer cited デジタル大辞泉 and 日本国語大辞典 entries that gloss 才能 with 生まれつきの能力 as support for the
«природную одарённость» emphasis, while noting that this is not a rule that learned abilities cannot be talent.
The comprehensibility reviewer cited JMdict («talent, ability», no innate restriction) and the existing reviewed RU 才能 card,
which says the word itself does not settle how far the ability is innate. The coordinator resolved the wording by fidelity
to frozen EN ("talent or aptitude") and cross-card consistency, not by majority; see the recheck record.

## Exclusion classification: author and consistency reviewer

The author added 13 direct, one-sided exclusion pairs beyond EN on 9 new cards. All 20 EN exclusion entries are retained.
The author report and the blind consistency reviewer classified them independently. The differences are preserved here
rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `能力`→`知能` | conservative | required |
| `能`→`機能` | conservative | required |
| `考慮`→`尊重` | conservative | required |
| `考え`→`意見` | conservative | required |
| `考え`→`考える` | conservative (noun→verb precedent) | unjustified but harmless |

Both classify `育つ`→`伸びる` as required, and `育つ`→`成長`, `皮`→`革`, `肌`→`表`, `肌`→`面`, `職`→`勤め`, `考え`→`見解`
and `維持`→`支える` as conservative. The reviewer judged none of the 13 a defect, and none guards a contrast that a card teaches.
The author had considered and declined 老人→おじいさん/おばあさん. The two guards added after review in response to F1 bring the
RU-added total to 15 and are recorded in the recheck record.

Reconciliation, the coordinator's dispositions and the final verdicts are in `196-words-batch-35-recheck-001.md`.
