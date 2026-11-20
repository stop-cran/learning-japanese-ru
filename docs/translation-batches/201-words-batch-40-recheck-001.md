# Batch 201 — independent recheck 001

## Snapshots

| Snapshot | Tree | Change |
|---|---|---|
| Staged candidate (scratch worktree) | `6e8f38856e4b35ab1e3322e0c66d6e16c5c39c43` | Initial review snapshot, on top of the reviewed Batch 200 tree `00107e1`. |
| Staged revision (scratch worktree) | `7d283bd2cd5bce2a235e4f6abb34a0611494321e` | Review fixes; the snapshot read by the rechecks. |
| `41cc79e263f0525a13687231644a622b209ad0e2` | `db5a31f22e39cecfdaba1810af7629012574c83b` | Signed candidate on `full-ru-201-words-40`: the content of `7d283bd` plus the intake. |

The revision changes eight word files and regenerates `manifest.json`:
- `現状`: line 9 adds 様子 to the exclusions, giving `[状態, 状況, 事態, 様子]`.
- `無`: line 9 adds ノー to the exclusions, giving `[無し, ノー]`.
- `無し`: line 31 no longer says that なし «говорит только об отсутствии». It now reads «Для отрицательного ответа есть,
  например, いいえ и いえ; в конструкциях Nなしで и Nなしの слово なし обозначает отсутствие N. Об отдельном оценочном
  употреблении なし — ниже.», using the correctness reviewer's text.
- `ノー`: line 33 adds a translation of EN's source note: the source row has no English gloss, so the interjection and prefix
  uses are dictionary-supported teaching choices, not a recovered account of the compiler's intent. The wording follows
  the reviewed `はあ.md:34`.
- `無`: line 40 adds a translation of EN's source note: the community list pairs ぶ with a mismatched «ничто» gloss, its
  intention is unresolved, and ぶ and む have separate source rows. The reviewed `便.md:44-47` and `素.md:35` keep similar notes.
- `燃える`: line 16 reads «непереходный глагол итидан», the glossary spelling, instead of «глагол группы ичидан».
- `犯罪`: line 25 reads «Несмотря на то, что состав напоминает о действии, изучаемое здесь слово — существительное.» instead of
  the «действенный» (effective) wording.
- `独身`: line 19 renders 独身の友人 as «с другом, не состоящим в браке» instead of the gendered «с неженатым другом».
- `現場`: line 16 replaces the calque «передний край практической работы» with «любое место, где непосредственно идёт
  практическая работа».
- Only these eight word hashes and `contentVersion` change in the manifest. Titles do not change; front matter changes only in
  the two exclusion lines; no link is added or removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer reread its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

Rechecks ran serially.
Each reviewer received only:
- its facet's original blind report;
- the coordinator's dispositions of its findings;
- the revised snapshot;
- the actual diff from `6e8f388` to `7d283bd`.

The prompts took the changed-file count from the diff (eight word files plus the manifest), and all three reports agree.

Commit signing was still unavailable: the signing key's passphrase cache had expired. Both snapshots were therefore staged trees
in a scratch worktree, and reviewers were told to read those trees rather than HEAD. No unsigned commit was made. After Batch 200
was published, the reviewed content was committed signed as `41cc79e`. `git diff 7d283bd 41cc79e -- words kanji strokes
articles manifest.json` is empty.

The worktree's index tree, working tree and untracked-file list were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `7d283bd` | C1 and C2 are resolved. `無し.md:31` attributes absence to Nなしで and Nなしの rather than to every use of なし, and the evaluative use remains at line 35, consistent with EN and JMdict 1529560 senses 1–2. `ノー.md:33` and `無.md:40` restore EN's qualifications (EN `ノー.md:33`, `無.md:37`) without reconstructing the compiler's intent, and 無 still separates bound-prefix ぶ from noun/prefix む. Regression check: the 独身 translation renders the past trip, the companion and the unmarried status of 独身の友人と旅行に行きました; the 現場 wording keeps EN's on-site sense without a military or frontier reading; the 犯罪 sentence matches EN's "action-like composition"; the 燃える change is transcription only; the two exclusion lists only append entries. The reviewer ran the validator (0 errors) and saw only the eight word hashes and `contentVersion` change in the manifest. Correctness and scoped coverage are **CLEAN**. |
| Consistency | tree `7d283bd` | F1 and F2 are resolved: 現状 excludes 様子, as its sibling situation cards do, and 無 excludes ノー. F3 is withdrawn as a defect and the 無し→いいえ/いえ/否 guards are reclassified as conservative: JMdict 無し has no "no" sense, but Russian «нет» is also the ordinary predicate of absence, so a learner could defend those distractors, and the reworded `無し.md:31` now says so. The optional 父親–親 guard stays unadded. Regression check: only the two declared exclusion lines changed; no title or link changed, so EN link parity is unchanged; the reworded passages create no new title collision. The reviewer ran the validator (0 errors) and `build_manifest.py --check` (exit 0). Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `7d283bd` | F1 and F2 are resolved: `燃える.md:16` now reads «итидан», and `犯罪.md:25` says the composition suggests an action while the word is a noun. The adopted optional rewordings are resolved: `現場.md:16` replaces the «передний край» calque with «любое место, где непосредственно идёт практическая работа», which still fits the accident and construction examples, and `独身.md:19` renders the friend as «не состоящим в браке», matching the card's own gloss and EN "unmarried friend". The declined optional items stay optional: 否's «другая грамматика» is understandable from «неприятный» and the guest-correction note; 率's «коэффициент» is defined in the body. Regression check: every changed passage was read in context against the frozen EN lines and the cited precedents (`はあ.md:34`, `便.md`, `素.md`); the reworded 無し, ノー and 無 passages state the learner rule before any provenance note, and the two exclusion lines and manifest hashes do not affect comprehension. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 無し «только об отсутствии» contradicts the evaluative use | **Resolved** | `無し.md:31`, the reviewer's text. |
| Correctness C2: ノー and 無 drop EN source-provenance qualifications | **Resolved** | `ノー.md:33`, `無.md:40`. |
| Consistency F1: 現状 lacks a guard against 様子 | **Resolved** | `現状.md:9`. Direct, one-sided pair; 状態, 状況 and 事態 already guard 様子. |
| Consistency F2: 無 lacks a guard against ノー | **Resolved** | `無.md:9`. Both titles teach the prefix «без». |
| Consistency F3: 無し→いいえ/いえ/否 unjustified | **Withdrawn** | The reviewer accepted the conservative classification on recheck; the guards are kept. |
| Consistency optional: 父親 vs 親 | **Optional, declined** | 父親's title is explicit about «отец»; the reviewer judged no guard required. |
| Comprehensibility F1: 燃える «ичидан» | **Resolved** | `燃える.md:16` «итидан». |
| Comprehensibility F2: 犯罪 «действенный» | **Resolved** | `犯罪.md:25`, the reviewer's text. |
| Comprehensibility optional: 独身 gendered «неженатым другом» | **Optional, adopted** | `独身.md:19`. |
| Comprehensibility optional: 現場 «передний край» calque | **Optional, adopted** | `現場.md:16`. |
| Comprehensibility optional: an いやな example on 否 | **Optional, declined** | The reviewer judged the passage understandable; it would be a Russian-only Japanese example outside EN. |
| Comprehensibility optional: 率 «коэффициент» | **Optional, declined** | The title avoids 割合 «доля; соотношение», and the body defines it. |
| Comprehensibility optional: ノー «английского no»; 現場 «дзюбакоёми» | **Optional, unchanged** | The reviewer judged the ノー line an etymology note not needed to understand «нет», and «дзюбакоёми» consistent with existing cards such as `円高.md`. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN** after fixes.
- Scoped coverage: **CLEAN** after fixes.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** after fixes, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

Limits: the rechecks did not refetch dictionary entries; unchanged lexical facts rest on the dictionary inspection in review
001. Unchanged cards were not reread in the rechecks. No native-speaker, learner, app-import, device, media, activation or
release acceptance is claimed.
