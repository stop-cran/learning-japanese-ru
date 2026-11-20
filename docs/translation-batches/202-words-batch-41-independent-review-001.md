# Batch 202 — independent review 001

## Snapshot and scope

- Reviewed snapshot: candidate tree `fdf29ba137faa929ab8a81876d0e252c83d1c416`, staged in a scratch worktree, not a commit.
  - Batches 197–201 had been reviewed and their fixes rechecked, but their signed commits could not yet be made because the
    signing key's passphrase cache had expired. Rather than wait, Batch 202 was authored on top of the reviewed Batch 201 tree
    `7d283bd2cd5bce2a235e4f6abb34a0611494321e`, at detached HEAD `5dd9a78` in a separate worktree.
  - The candidate differs from `7d283bd` by 44 paths: 30 new word cards, 13 navigation-only files (18 restored links) and
    `manifest.json`.
  - Reviewers were told to read the staged tree and not to rely on HEAD. No unsigned commit was made.
- After Batch 201 was published as `e80d113a1601af71925517822926defc29bbb8de`, branch `full-ru-202-words-41` was cut from that merge. Its parent commit
  `b5992255e25697b35c3c55f791a073857146a2a8` adds only the Batch 201 publication record. The final reviewed content tree was copied there and committed signed as
  `b75403d780edb7a2327a2b320955258acf5cb8f1`, together with the intake. `git diff 459ddef b75403d -- words kanji strokes articles manifest.json` is empty;
  see the recheck record for the revised tree `459ddef`.
- Published baseline recorded in the intake: `e80d113a1601af71925517822926defc29bbb8de` (Batch 201 merge).
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers.
  - Correctness read every new card and its EN original completely, inspected the link-only changes, and read 火, 火事, 火曜日,
    金曜, 河, 公演, 演技, 泊まる, たまに, 沈む, 下がる, 下げる and 不満 as comparisons.
  - Consistency read the 13 navigation-only diffs and covered `manifest.json`. Its first returned report read only 7 of the 30
    cards in full and checked the other 23 structurally. At the coordinator's request, the same reviewer session read the
    remaining 23 cards in full on the same tree and updated its report in place; the recorded report covers both passes.
  - Comprehensibility read all 30 cards and compared them with the RU cards behind the risk pairs (火事, 火曜日, 演技, 公演, 納得,
    費用, 港, 水泳, 泳ぎ方, 暖かい, きれい). It reviewed the 13 navigation restorations from their diffs.
  - The intake was generated after review from the same paths. Its payload hashes are checked by the final validation receipt.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time, including the consistency reviewer's second pass. Before each next review, the
  coordinator checked that the worktree's index tree was still `fdf29ba`, that the working tree equalled the index and that
  nothing was untracked. No fix was applied until all three reports were complete.
- Full blind reports:
  - `202-words-batch-41-review-correctness-001.md`
  - `202-words-batch-41-review-consistency-001.md`
  - `202-words-batch-41-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's
  reports. The consistency reviewer ran its own title-overlap screen of the new titles against all RU word titles and treated its
  hits as leads.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (温度 only); scoped coverage **NEEDS FIX** (濠 only). The other 29 cards were CLEAN on both
facets.

- C1 (minor, high confidence), `温度.md:21`: «温度が下がる — что температура понижается сама» adds a spontaneous,
  no-external-cause implication absent from EN's "describes the temperature falling". The contrast is the temperature as
  subject versus object. Evidence: Digital Daijisen 下がる sense 3 (a degree becoming lower, with temperature examples) and
  Kuznetsov «сам» I.2 (the independent, no-intervention reading). Remedy (the reviewer's text): «温度を下げる описывает, что
  кто-то понижает температуру; 温度が下がる — что температура понижается, без указания причины.»
- C2 (minor, high confidence), `濠.md:33–35`: EN's note that its N2 source gives both "moat" and "canal", uses the spelling 堀,
  and maps to the stable 濠 article (JMdict 1522060, reading ほり) with the existing N3 level retained was dropped. This is a
  narrow source-note omission, not a missing Japanese sense or a changed level.

Optional (outside the facet): `満足.md:15` «Тем, чем человек доволен, отмечается に» is a grammatical slip; prefer «То, чем…».

Other checks:

- The reviewer inspected the Jisho/JMdict-based entries for all 30 headwords and for the added comparisons まじめ, 真剣, 人気,
  広がる and たま, the HTML 滅多に entry for its ateji note, the lexical Daijisen 堀 heading and the Kotobank 運河 entry.
- It checked the Russian adaptations against Kuznetsov entries on Gramota: «утонуть» (fatal drowning), «бухта» (small bay),
  «спряжение» (verbal conjugation) and «серьёзный» (person or attitude versus gravity). They support the adapted wording in
  溺れる, 湾, 活用 and 深刻.
- `tools\validate.py` reported 0 errors.

### Consistency and quiz safety

Verdict after both passes: consistency **NEEDS FIX** (温暖 only); quiz safety **CLEAN**; scoped cross-file integration **CLEAN**.

- The validator reported 0 errors. Front matter matches EN in all 30 cards apart from the localized titles and the added
  exclusions; every card has the four standard sections and one `Словарь:` line with JMdict entry and sense numbers identical
  to EN. All EN exclusions are kept.
- Every RU link target is also an EN link target (no Russian-only link), and every EN link absent from RU has no RU target file.
  The 13 navigation diffs change only link brackets and targets at EN link positions.
- `manifest.json` adds exactly 30 entries and removes none; all `kanji/` and `words/` hashes match. The `strokes/*.json` hashes
  could not be recomputed from the worktree's CRLF checkout bytes, but those entries are unchanged from the base manifest.
- Every exact whole-title or segment collision between a new card and an existing card has a direct exclusion on one side.
  Other candidate pairs in the dense clusters differ in part of speech or object, or carry a contrast the article teaches.

Finding:

- F1 (minor, high confidence), `温暖.md:16`: «Это na-прилагательное» uses Latin «na-», the only such occurrence among 2,713 RU
  word cards; 149 cards, including 清潔 and 深刻 in this batch, write «な-прилагательное». Remedy: «Это な-прилагательное, которое
  может работать и как существительное.»

Optional: `濠.md` omits EN's two source-note sentences; the reviewer judged them project-internal and nonblocking (the same
omission as correctness C2).

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (灰, 涙, 温暖); the other 27 cards and the navigation diffs **CLEAN**. Scoped coverage
**CLEAN**.

All three findings are minor and high-confidence:

- C1, `灰.md:15`: «Количество золы задаёт остальное предложение, а не форма самого слова» reads backwards («задаёт» makes the
  amount determine the sentence), so it does not teach that the sentence supplies the quantity. Remedy: «Сколько золы, показывает
  всё предложение, а не особая форма слова.»
- C2, `涙.md:18`: «Она плакала от радости» renders 涙を流しました with the Russian for 泣く, although the card glosses the
  construction as «проливать слёзы» and keeps 泣く distinct. EN: "She shed tears of joy." Remedy: «Она от радости пролила слёзы.»
- C3, `温暖.md:16`: «na-прилагательное» is unexplained Latin for an English-free learner (the same defect as consistency F1).
  Remedy: «Это な-прилагательное».

Optional:

- 体温:33 «Для словаря важно» is a calque of "for vocabulary purposes".
- 海外:19 «письмо другу за рубежом» can attach «за рубежом» to the sending.
- 流行:18 «популярна» sits next to the card's own 人気 «популярность» contrast; «сейчас в моде» would sharpen it.
- 消費:32 «обычные расходы семьи» uses the title word of 費用 without naming that card.
- 濠:19 uses 堀 before the spelling note.
- 泳ぎ explains manner but never names 泳ぎ方.

Outside the facet (not scored): new-card exclusions are not reciprocated on partner cards; 火災:18 renders 昨夜 as «вчера вечером»
where EN has "last night".

## Exclusion classification: author and consistency reviewer

The author added 16 direct, one-sided exclusion pairs beyond EN on 11 new cards. All 16 EN exclusion entries (11 lists) are
retained. The author report and the blind consistency reviewer classified the pairs independently. The differences are preserved
here rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `火災`→`火事` | required | required |
| `火曜`→`火曜日` | required | required |
| `溺れる`→`沈む` | required | required |
| `深刻`→`まじめ` | required | required |
| `滅多に`→`たまに` | precautionary | required-leaning (at least conservative) |
| `演奏`→`演技` | precautionary | conservative, bordering on unjustified; harmless |

Both classify the other ten pairs as precautionary/conservative: `深刻`→`真剣`, `滅多に`→`たま`, `演奏`→`公演`,
`温暖`→`ぽかぽか`, `体温`→`熱`, `温度`→`熱`, `流行`→`人気`/`広がる`/`回り` and `泳ぎ`→`泳ぐ`. Neither found an unjustified
pair, and no kept pair guards a contrast that a card teaches as an antonym.

Reconciliation, the coordinator's dispositions and the final verdicts are in `202-words-batch-41-recheck-001.md`.
