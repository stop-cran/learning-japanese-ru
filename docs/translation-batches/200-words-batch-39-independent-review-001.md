# Batch 200 — independent review 001

## Snapshot and scope

- Reviewed snapshot: candidate tree `117374d47cec40b00dcaae3eb8cff40bfba29c1e`, staged in a scratch worktree, not a commit.
  - Batches 197, 198 and 199 had been reviewed and their fixes rechecked, but their signed commits could not yet be made because
    the signing key's passphrase cache had expired. Rather than wait, Batch 200 was authored on top of the reviewed Batch 199 tree
    `841bc8c046cc7e4141696ceba1e213b6a98b2d7e`, at detached HEAD `5dd9a78` in a separate worktree.
  - The candidate differs from `841bc8c` by 50 paths: 30 new word cards, 19 navigation-only files (27 restored links) and
    `manifest.json`.
  - Reviewers were told to read the staged tree and not to rely on HEAD. No unsigned commit was made.
- After Batch 199 was published as `8dd8bc7d7593204957771fe82ac05391a2057a11`, branch `full-ru-200-words-39` was cut from that merge. Its parent commit
  `208d0eaa39477ae8822370e281e5f4b64c448ace` adds only the Batch 199 publication record. The final reviewed content tree was copied there and committed signed as
  `2eaed77d122d352a7c4685486e1125f3c01e4a5a`, together with the intake. `git diff 00107e1 2eaed77 -- words kanji strokes articles manifest.json` is empty;
  see the recheck record for the revised tree `00107e1`.
- Published baseline recorded in the intake: `8dd8bc7d7593204957771fe82ac05391a2057a11` (Batch 199 merge).
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness read every new card and its EN original completely, and inspected the changed passages in the 19
    navigation-only files.
  - Consistency read the 19 navigation-only diffs and covered `manifest.json`.
  - Comprehensibility read the new cards and the named comparison cards. It inspected the kanji and reciprocal link edits only to
    confirm that they add links, and gave them no separate verdict.
  - The intake was generated after review from the same paths. Its payload hashes are checked by the final validation receipt.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that the worktree's index tree
  was still `117374d`, that the working tree equalled the index and that nothing was untracked.
- Full blind reports:
  - `200-words-batch-39-review-correctness-001.md`
  - `200-words-batch-39-review-consistency-001.md`
  - `200-words-batch-39-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's reports.
  The consistency reviewer ran its own title-overlap screen of the new titles against all RU word titles and treated its hits as leads.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN**; scoped coverage **CLEAN** for all 30 cards. No findings.

Optional:

- O1, `命.md:46`: «JMdict также отмечает редкое написание 生命 для いのち» is a little stronger than the source. JMdict 命 sense 1
  says "sometimes written as 生命", and EN says "occasional use"; neither carries JMdict's explicit rare-form label. The reviewer
  suggested «иногда записывается как 生命» and did not establish a frequency error.
- O2, `生じる.md:23`: «Во втором недоразумение порождает выражение» is grammatically possible as object-first word order, but both
  neuter nouns have identical nominative and accusative forms, so the ordinary subject-first reading reverses the roles. The
  reviewer suggested «Во втором выражение порождает недоразумение» and placed it outside its own facets.

Withdrawn lead: `発表.md:18` attaches «на занятии» to the presentation, where EN's final "in class" more readily follows
"researched". Treating 授業で as necessarily embedded would be too strong, and the card describes a classroom presentation.

Other checks:

- The reviewer inspected the Jisho/JMdict entries for all 30 headwords, keeping apart 生（せい）and 生（なま）, 生地（きじ）and
  生地（せいち・しょうち）, 球（きゅう）and the shared 玉・球（たま）entry, and both senses of 生じる.
- It checked the Russian adaptations «жизнь» and «корыстный» against Gramota dictionary entries. They support the breadth of
  «жизнь» and a personal-benefit, not professional-mercenary, reading of «корыстный».
- By script, it compared source metadata and the Japanese token inventory of all 30 cards. All source identity, reading, level,
  type, kanji and tag fields remain, and every EN exclusion is kept. The only removed Japanese token is the redundant なま in 生's
  H1; its reading and examples remain in the body. Every relative link target exists.
- The reviewer did not run the validator and makes no structural-validation claim.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX**; scoped cross-file integration **CLEAN**.

- The validator reported 0 errors. `build_manifest` was recomputed in memory without writing, and its output equals
  `manifest.json` (4,114 entries).
- Front-matter keys and order match EN in all 30 cards, apart from the added `quiz_exclusions` lines.
- Every EN link whose RU target exists is present. The omitted EN-only links all point to absent cards: the words 報告, 信じる,
  すみません, ごめんなさい, 就職, ボール, カード, 人生, 地球 and 事情, and the kanji 訳, 防, 布, 瓶, 境, 玉, 象 and 況. The report calls
  them "14 omitted EN-only links", but its own list names 18 targets; a coordinator count finds 19 EN link occurrences in the 30
  cards (ボール is linked from both 玉 and 球). No Russian-only link was added.
- The 19 navigation-only files change only at link brackets and targets. A repository-wide check found no EN file that
  links to a new card while its RU counterpart leaves it unlinked.

Both findings are minor:

- F1 (medium confidence), `状況.md` front matter: the title «положение вещей; совокупность обстоятельств» overlaps the existing
  都合 «обстоятельства; удобство», and neither card guards the other. The overlap is introduced by the Russian titles; EN's titles
  are "situation; state of affairs" and "circumstances; availability". 場合→都合 is the precedent for the same overlap. Remedy:
  add 都合 to 状況's exclusions.
- F2 (high confidence that 銅貨 is unjustified, medium on 硬貨), `玉.md` front matter: `[硬貨, 銅貨]` goes beyond EN. 玉→硬貨 has
  a real but unestablished necessity, since 玉's title says «суффикс монет», not «монета». 玉→銅貨 is reached only by chaining
  玉~硬貨 and 硬貨~銅貨; the app does not apply exclusions transitively. Remedy: `[硬貨]`.

Optional:

- 生 «…сырой (о пище)» shares the word «сырой» with じとじと and じめじめ; the qualifier and the different sense make a guard
  unnecessary.
- 用いる/使用 vs 適用: a guard is not required.
- 発表 ends with «Лексика:», where most cards use «Словарь:».
- 画家.md and 申し訳.md have a doubled blank line before «Оттенки значения».

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (生じる, 生地, 命, 生, 現金); the other 25 cards **CLEAN**. Scoped coverage **CLEAN**
for all 30 cards.

All five findings are high-confidence:

- C1 (moderate), `生じる.md:23`: the same reversed roles as correctness O2, found independently. A learner who trusts the summary
  inverts が and を. Remedy: «Во втором выражение порождает недоразумение.»
- C2 (minor), `生地.md:33`: the «Оттенки значения» paragraph is an author note («Исходный список», «проверенную идентичность»,
  «замысел составителя»). It also carries the English gloss "birthplace", so a learner needs English to see the rejected gloss.
  Remedy: delete the paragraph; fabric and dough are already taught in «Значение».
- C3 (minor), `命.md:47`: «Общественный источник смешивает…» is adjudication, not a learner explanation. Remedy: state that
  «приказ, повеление» belongs to the reading めい, and that «судьба, рок» is an archaic sense of いのち.
- C4 (minor), `生.md:38`: the clause about the community source's rows is editorial. The learner rule is already in the preceding
  sentence. Remedy: delete the clause.
- C5 (minor), `現金.md:36`: «Не сводите второе значение к наёмникам… только потому, что … «корыстный»» introduces a false lead,
  because «корыстный» does not mean mercenary. EN's warning exists only because of the English gloss "mercenary". Remedy: end the
  paragraph at «Оба значения относятся к одной словарной записи.»

Optional:

- 発表's title «оглашение» is narrower than the kanji card's «объявление».
- 状況 and 事態 are near-paraphrases; their bodies separate them, but not with a minimal pair.
- 現金's «взялся помогать» is past tense for non-past 手伝う.

The reviewer judged none of these an actionable defect.

## Exclusion classification: author and consistency reviewer

The author added 17 direct, one-sided exclusion pairs beyond EN on 11 new cards. All 32 EN exclusion entries (16 lists) are
retained. The author report gave a total of 18 and listed 14 conservative pairs; its own list has 13 conservative and 4 required
pairs, 17 in all, matching the candidate tree. The author report and the blind consistency reviewer classified the pairs
independently. The differences are preserved here rather than resolved by vote. Classification does not change runtime
behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `画家`→`作家` | required | conservative |
| `玉`→`硬貨` | required | conservative |
| `男子`→`男の人` | conservative | required |
| `予防`→`防ぐ` | conservative | required |
| `瓶`→`缶` | conservative | required |
| `玉`→`銅貨` | conservative | unjustified |

Both classify `用いる`→`利用` and `事態`→`状況` as required, and `男子`→`おじさん`, `男子`→`おじいさん`, `申し訳`→`謝る`, `使用`→`用`,
`現金`→`お金`, `現金`→`金`, `現金`→`金銭`, `光景`→`景色` and `光景`→`眺め` as conservative. No kept pair guards a contrast that a card
teaches as an antonym.

Reconciliation, the coordinator's dispositions and the final verdicts are in `200-words-batch-39-recheck-001.md`.
