# Batch 203 — independent recheck 001

## Snapshots

| Snapshot | Tree | Change |
|---|---|---|
| Staged candidate (scratch worktree) | `d6e95d46124d66f60472825a8db483b5702688f7` | Initial review snapshot, on top of the reviewed Batch 202 tree `459ddef`. |
| Staged revision (scratch worktree) | `20d023225e820a0a3b1eb7e965807dc7d5820fd3` | Review fixes; the snapshot read by the rechecks. |
| `1f5e73c6f566d8364003e98a82bf4d8393f5c5aa` | `ecc37a822e6576480bef762223cccc3030c0a6f4` | Signed candidate on `full-ru-203-words-42`: the content of `20d0232` plus the intake. |

The revision changes five word files and regenerates `manifest.json`:
- `毛布`: line 32 reads «Учите глаголы укрывания вместе с частицами: в приведённых ситуациях используются 毛布をかける и
  毛布をかぶる.» instead of the categorical «…одеяло не надевают глаголом для одежды вроде 着る（きる）.», using the correctness
  reviewer's text.
- `波`: line 32 adds «Жест «помахать рукой» передаётся выражением 手を振る（てをふる）, а не словом 波.», restoring EN's Japanese
  contrast (EN `波.md:32`) without its English pun.
- `正確`: line 9 reads `quiz_exclusions: [ちょうど, 正しい]` instead of `[ちょうど]`.
- `気味`: line 34 opens with the learner rule (the noun 気味 is read きみ and names the sensation, as in 気味が悪い; the suffix 〜気味
  is read ぎみ and expresses a tendency or slight degree, as in 疲れ気味, a separate dictionary entry) and then explains in plain
  words that the N3 list the card is based on gives きみ with a gloss closer to the suffix. It replaces the author-note wording
  «В исходном списке слов…».
- Optional rewording adopted: `死亡`: line 26 ends «…не стоит просто подставлять вместо него само 死亡.» instead of the jargon
  «…китайское сложение.».
- Only these five word hashes and `contentVersion` change in the manifest. No title, link or reading changes; the only front-matter
  change is the 正確 exclusion.

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
- the actual diff from `d6e95d4` to `20d0232`.

The prompts took the changed-file count from the diff (five word files plus the manifest), and all three reports agree.

Commit signing was still unavailable: the signing key's passphrase cache had expired. Both snapshots were therefore staged trees
in a scratch worktree, and reviewers were told to read those trees rather than HEAD. No unsigned commit was made. After Batch 202
was published, the reviewed content was committed signed as `1f5e73c`. `git diff 20d0232 1f5e73c -- words kanji strokes
articles manifest.json` is empty.

The worktree's index tree, working tree and untracked-file list were unchanged after every recheck.

Process note: in both review 001 and this recheck, the consistency reviewer ran `tools/build_manifest.py`, which rewrites
`manifest.json` in place. The review 001 prompt asked it to confirm that no hash was stale; the recheck prompt forbade
regeneration. Both runs reproduced the existing bytes. After each run, the coordinator confirmed that `git write-tree` still printed
the reviewed tree, `git diff --quiet` exited 0, and no untracked or ignored file existed. The reviewed content was therefore not
altered.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `20d0232` | C1 and C2 are resolved. `毛布.md:32` uses the reviewer's proposed contextual wording: it no longer prohibits 着る and reinforces 毛布をかける and 毛布をかぶる, already taught at line 15 (EN `毛布.md:16–18`); «в приведённых ситуациях» is contextual guidance, not an unrestricted claim. `波.md:32` restores 手を振る（てをふる）and its contrast with 波, matching EN `波.md:32` in Japanese and the JMdict-backed entry inspected in review 001. Regression check of every changed passage: 正確's added pair agrees with 正確:16,29 and 正しい:16 (accurate/error-free versus correct/right) and introduces no source-fidelity defect; 気味:34 keeps きみ as the sensation noun and ぎみ as the tendency suffix, restates EN:16–22 and preserves EN:34's source-list discrepancy, separate dictionary treatment and bounded N3 assignment; EN's explicit remark that the compiler's intent is uncertain remains unstated, as before the revision, which the reviewer judged not consequential because the card asserts no intent; 死亡:26 «само 死亡» keeps EN:30–32's warning against mechanical substitution for 亡くなる without becoming an absolute ban. The reviewer recomputed the five LF-normalized hashes, which match the manifest; only those hashes and `contentVersion` changed. Correctness and scoped coverage are **CLEAN**. |
| Consistency | tree `20d0232` | F1 is resolved: `正確.md:9` reads `quiz_exclusions: [ちょうど, 正しい]`, well-formed, with both targets existing and the EN-inherited entry first. The optional 残す–残る guard is withdrawn: the titles «оставлять; приберегать» and «оставаться» share no title or segment, EN leaves the pair unguarded, and the 汚す/開ける precedent cited in review 001 is inherited from EN rather than an RU requirement. The 泥–土, 沖–海 and 正直–まじめ observations stay no-action, and the exclusion classifications stand. Regression check: the 毛布, 波, 気味 and 死亡 edits are body-only, with titles, links and other front matter identical to `d6e95d4`; 手を振る and 〜気味/疲れ気味/気味が悪い are plain text, as in EN, so link parity holds; terminology, «» quoting and the «список слов уровня N3» wording match the cards' existing text; «само 死亡» parallels EN's "substituting compounds". The reviewer ran the validator (0 errors), and regeneration reproduced the manifest (see the process note). Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `20d0232` | C1 is resolved: `気味.md:34` teaches きみ versus ぎみ first, with 気味が悪い and 疲れ気味, and then names the N3 list in plain words; «исходный список» is gone, and the learner is told to study the noun and treat the suffix as a reading comparison, not a second N3 item. The adopted optional 死亡 item is resolved: «само 死亡» makes the antecedent plain. The declined optional かわいそう and 気に入る items stay optional: かわいそう:19 «несправедливо» is the contextual translation that the note at line 21 explicitly qualifies as no separate dictionary sense, and 気に入る:19 «очень» renders EN "really" next to line 21's note on 気に入っている as a lasting preference. Regression check: 波:32 is natural for a learner who reads no English and restores the Japanese expression; 毛布:32 names constructions already taught with particles, so removing the 着る warning leaves nothing unexplained; 死亡:26 is clearer, not narrower; 正確's exclusion is not learner-visible prose. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 毛布 turns EN's caution into a ban on 着る | **Resolved** | `毛布.md:32`, the reviewer's text. |
| Correctness C2: 波 drops EN's 手を振る contrast | **Resolved** | `波.md:32`. |
| Consistency F1: 正確 and 正しい lack a direct guard | **Resolved** | `正確.md:9`. |
| Consistency optional: 残す–残る guard | **Withdrawn** | No title or segment overlap; EN leaves the pair unguarded; the cited precedents are EN-inherited. The reviewer withdrew the item on recheck. |
| Consistency observations: 泥–土, 沖–海, 正直–まじめ | **Optional, no action** | Assessed in review 001 as needing no guard; confirmed on recheck. |
| Comprehensibility C1: 気味 reads as an author note | **Resolved** | `気味.md:34`, rule first, the reviewer's noun/suffix wording. |
| Comprehensibility optional: 死亡 «китайское сложение» jargon | **Optional, adopted** | `死亡.md:26`. |
| Comprehensibility optional: かわいそう «несправедливо» | **Optional, declined** | `かわいそう.md:19` renders EN's own contextual translation, and line 21 states that «несправедливо» is not a separate dictionary sense; the reviewer accepted the decline. |
| Comprehensibility optional: 気に入る «очень» | **Optional, declined** | `気に入る.md:19` renders EN "really", and line 21 explains 気に入っている as a lasting preference; the reviewer accepted the decline. |
| Hand-wave contrast: comprehensibility limits listed the dropped «wave» trap as correctly dropped; correctness C2 flagged the lost 手を振る | **Preserved disagreement, resolved by fix** | Both positions are compatible with the fix: the English pun stays dropped, and the Japanese expression and rule are restored. 波 is the only English-only trap in this batch for which EN supplies a Japanese alternative. Neither reviewer saw the other's report. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN** after fixes.
- Scoped coverage: **CLEAN** after fixes.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN** after fixes.
- Quiz safety: **CLEAN**, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive
  groups.

Limits: the rechecks did not refetch dictionary entries; unchanged lexical facts rest on the dictionary inspection in review
001. Unchanged cards were not reread in the rechecks. JMdict 1222640 sense 2 (a tendency sense listed under きみ) was not
re-examined beyond review 001. No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
