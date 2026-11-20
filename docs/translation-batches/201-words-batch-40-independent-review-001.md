# Batch 201 — independent review 001

## Snapshot and scope

- Reviewed snapshot: candidate tree `6e8f38856e4b35ab1e3322e0c66d6e16c5c39c43`, staged in a scratch worktree, not a commit.
  - Batches 197, 198, 199 and 200 had been reviewed and their fixes rechecked, but their signed commits could not yet be made
    because the signing key's passphrase cache had expired. Rather than wait, Batch 201 was authored on top of the reviewed
    Batch 200 tree `00107e197ba7aa3968b2b9db9069694484bf4edd`, at detached HEAD `5dd9a78` in a separate worktree.
  - The candidate differs from `00107e1` by 45 paths: 30 new word cards, 14 navigation-only files (21 restored links) and
    `manifest.json`.
  - Reviewers were told to read the staged tree and not to rely on HEAD. No unsigned commit was made.
- After Batch 200 was published as `3b1635c4b63daa621c52177491c09ce535302479`, branch `full-ru-201-words-40` was cut from that merge. Its parent commit
  `a1091bc4e6516db2417e48ea265d120c631b95f5` adds only the Batch 200 publication record. The final reviewed content tree was copied there and committed signed as
  `41cc79e263f0525a13687231644a622b209ad0e2`, together with the intake. `git diff 7d283bd 41cc79e -- words kanji strokes articles manifest.json` is empty;
  see the recheck record for the revised tree `7d283bd`.
- Published baseline recorded in the intake: `3b1635c4b63daa621c52177491c09ce535302479` (Batch 200 merge).
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness read every new card and its EN original completely, and inspected the changed passages in the 14
    navigation-only files.
  - Consistency read the 14 navigation-only diffs and covered `manifest.json`.
  - Comprehensibility read the new cards and the named comparison cards. It treated the kanji and reciprocal link edits as link
    insertions and gave them no separate verdict.
  - The intake was generated after review from the same paths. Its payload hashes are checked by the final validation receipt.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that the worktree's index tree
  was still `6e8f388`, that the working tree equalled the index and that nothing was untracked.
- Full blind reports:
  - `201-words-batch-40-review-correctness-001.md`
  - `201-words-batch-40-review-consistency-001.md`
  - `201-words-batch-40-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's reports.
  The consistency reviewer ran its own title-overlap screen of the new titles against all RU word titles and treated its hits as leads.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (無し only); scoped coverage **NEEDS FIX** (ノー and 無, strict source-note parity only). The
other cards were CLEAN on both facets.

- C1 (minor, high confidence), `無し.md:31`: the Russian-only contrast «なし говорит только об отсутствии» is an unrestricted claim
  contradicted by the card's own evaluative それはなしです («так не пойдёт»). A learner could reject the taught evaluative sense.
  JMdict 1529560 has sense 1 "without" and sense 2 "unacceptable; not alright". Remedy (the reviewer's text): «Для отрицательного
  ответа есть, например, いいえ и いえ; в конструкциях Nなしで и Nなしの слово なし обозначает отсутствие N. Об отдельном оценочном
  употреблении なし — ниже.»
- C2 (minor, high confidence about the omission), `ノー.md:33` and `無.md:40`: EN's source-provenance qualifications were dropped
  rather than translated. EN ノー says the source list gave no English gloss, so the interjection and prefix uses are
  dictionary-supported teaching choices. EN 無 says the community list paired ぶ with a mismatched "nothing" gloss, its intention is
  unresolved, and ぶ and む have separate source rows. The reviewer established no Japanese teaching error and said that, if
  provenance were exempt from runtime translation, C2 could be dispositioned optional.

Other checks:

- The reviewer read the live Jisho/JMdict entries for all 30 headwords, including the kana-only ノー detail page and the separate
  無【ぶ】 (2423740) and 無【む】 entries, and checked the added contrasts against the entries for 状態, 状況, 事態, 熱心, 焼ける, 霧,
  大丈夫, 歴史 and 布.
- It checked the Russian adaptations against Gramota entries: «холостой» (masculine short form), «материя» and «материал»,
  «история» (story and history senses) and «скоро»/«скорый» (speed senses). They support the adapted warnings in 独身, 物質, 物語
  and 寧ろ.
- It compared front matter and every example, including kana readings, tense, polarity and argument structure. All source fields,
  dictionary IDs and EN link labels remain; the 11 removed link wrappers point to absent RU targets, and the visible Japanese words
  and readings remain.
- `tools\validate.py` reported 0 errors.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX**; scoped cross-file integration **CLEAN**.

- The validator reported 0 errors and `build_manifest.py --check` exited 0 (4,149 files).
- Front matter matches EN in all 30 cards apart from the localized titles and the added exclusions. All EN exclusions are kept.
- `link_parity.py` on the 30 cards found no issues. An ad-hoc comparison of every EN kanji, word and article link to a new word
  found no RU discrepancy and no Russian-only link. The 14 restorations change only link brackets and targets at EN link positions.

Findings:

- F1 (minor, medium confidence), `現状.md:9`: no guard against 様子 «положение дел; облик». The 現状 body itself glosses the word
  «нынешнее положение дел», and the sibling situation cards 状態, 状況 and 事態 all guard 様子. Remedy: add 様子.
- F2 (minor, medium confidence), `無.md:9`: no guard against ノー. Both titles teach the prefix «без», and both bodies show prefix
  use (ノーネクタイ; 無作法, 無事). Remedy: add ノー on 無 (one side suffices).
- F3 (minor, optional cleanup), `無し.md:9`: the added guards 無し→いいえ, いえ, 否 are unjustified, because 無し has no "no" sense
  and its title is «без; отсутствие». Remedy: keep only EN's ノー, or keep the extras as harmless distractor-pool loss.

Optional: 父親 and 親 share «родитель», but 父親's title is explicit about «отец»; no guard is required.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (燃える, 犯罪); the other 28 cards **CLEAN**. Scoped coverage **CLEAN** for all 30 cards.

Both findings are minor and high-confidence:

- F1, `燃える.md:16`: «глагол группы ичидан» departs from the glossary term «глагол итидан» (`docs/translation-methodology.md`)
  used everywhere else, so a learner may take it for a different class. Remedy: «непереходный глагол итидан».
- F2, `犯罪.md:25`: «действенный» состав means "effective", not EN's "action-like". Remedy: «Несмотря на то, что состав
  напоминает о действии, изучаемое здесь слово — существительное.»

Optional:

- 現場:16 «передний край практической работы» is a stiff calque of EN "front line".
- 独身:19 renders gender-neutral 友人 as «неженатым другом» after the card says the word is not male-only.
- 否:29 would be clearer with one いやな example.
- 率's title «коэффициент» is more technical than the body's «доля» / «уровень».
- ノー:25 «английского no» and 現場:25 «дзюбакоёми» match existing cards and are not new defects.

## Exclusion classification: author and consistency reviewer

The author added 14 direct, one-sided exclusion pairs beyond EN on 9 new cards. All 19 EN exclusion entries (13 lists) are
retained. The author report and the blind consistency reviewer classified the pairs independently. The differences are preserved
here rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `物語`→`歴史` | required | conservative (near-required) |
| `物質`→`布` | conservative | required |
| `物事`→`こと` | conservative | required |
| `物事`→`物` | conservative | required |
| `燃える`→`焼ける` | conservative | required |
| `熱中`→`ねっしん` | conservative | required |
| `無事`→`大丈夫` | conservative | required |
| `無事`→`幸福` | conservative | required |
| `無`→`無し` | conservative | required |
| `無し`→`いいえ` | conservative | unjustified |
| `無し`→`いえ` | conservative | unjustified |
| `無し`→`否` | conservative | unjustified |

Both classify `物語`→`語る` and `否`→`嫌` as conservative. No kept pair guards a contrast that a card teaches as an antonym.

Reconciliation, the coordinator's dispositions and the final verdicts are in `201-words-batch-40-recheck-001.md`.
