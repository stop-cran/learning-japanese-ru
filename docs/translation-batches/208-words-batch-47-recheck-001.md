# Batch 208 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `8963d85fc260aff6125e062366bcb09428c788ac` | `f0b363a16795dc636e1495eb6af34ee0f76fd3a4` | Initial review snapshot: the signed candidate, pushed before review. |
| `e5739f49a72bb9cb9b4093beb5298ef293fb6761` | `e8b26f264afa42281f156df781bdc277a800d939` | Fix 1: the five initial review fixes plus the intake refresh, committed signed and pushed before the first rechecks. |
| `45196f4826831e745ce46ce92b0b0157a9f19797` | `bc4e715ccb2f8ca1b53ce241f949ad2b589c713c` | Fix 2: two recheck fixes plus the intake refresh, committed signed and pushed before the second rechecks. |
| `c283b5f5ca98fa3bd15cf6f8ba2caade51631a81` | `1ba3199f45a39a733348f8aabb2fc4574a311213` | Fix 3 (final candidate): one coordinator-initiated fix plus the intake refresh, committed signed and pushed before the third rechecks. |

Fix 1 changed five word files and regenerated `manifest.json` (`contentVersion` `83e18ead74d47992`) and the intake:
- `必死` (line 21): 彼女は必死に笑いをこらえました is rendered «Она изо всех сил сдерживала смех.» instead of «Она отчаянно
  пыталась сдержать смех.» (correctness C1).
- `息` (after the 息が合う example): EN's boundary sentence is restored as «Этот оборот не делает 息 общим словом для тона голоса
  или музыкального тона.» (scoped coverage C2).
- `思想` (line 19): 近代の思想 is rendered «Я изучаю в университете мысль эпохи модернизации.» instead of «…мысль Нового
  времени.», matching the published 近代 card (comprehensibility P1).
- `急激` (line 42): the sentence ends «急激 оценивает масштаб и крутизну изменения.» without «а не политические взгляды»
  (comprehensibility P2).
- `悪戯` (line 22): 機械にいたずらする is glossed «баловаться с машиной, копаться в механизме» instead of «…, портить механизм»
  (comprehensibility P3).

Fix 2 changed two word files and regenerated `manifest.json` (`contentVersion` `32414df9db914fc3`) and the intake:
- `必死` (line 21): the example now reads «Она отчаянно сдерживала смех.» (comprehensibility P4, below).
- `息`: the restored sentence is deleted again (comprehensibility P5, below); the file is byte-identical to the candidate.

Fix 3 changed one word file and regenerated `manifest.json` (`contentVersion` `8319135071478801`) and the intake:
- `成績` (lines 37-40): the RU-only 評価 contrast quotes EN `評価.md:18` 先生は学生の発表を評価しました, and now gives EN's kana
  reading （せんせいはがくせいのはっぴょうをひょうかしました） in the card's inline style (comprehensibility optional note, below).

Net change from the candidate: four learner lines in 必死, 思想, 急激 and 悪戯, and one added kana reading in 成績. No title,
Japanese example, internal link or quiz exclusion changed in any fix, and no existing reading changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer reread its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

All three rounds ran serially. Each reviewer appended to its own report file, which stayed in its session context, and each
recheck message gave it only:
- the revised snapshot, its parent and the read-only rules;
- the actual content diff (`git diff 8963d85 e5739f4 -- words`, `git diff e5739f4 45196f4 -- words`, then
  `git diff 45196f4 c283b5f -- words`);
- a summary of its own findings and optional notes, with the coordinator's disposition of each;
- for edits prompted by other reviewers, the change and the coordinator's evidence (for example Digital Daijisen 堪える
  sense 2 for C1, and the EN source-row evidence for 息 in round 2), without those reviewers' reports.

The shared opening of the round-1 messages said that three of the five edits came from another facet reviewer's findings.
That count was right only for the correctness reviewer: all five came from other reviewers for consistency, and two for
comprehensibility. Each message showed the full diff and described every change, so the scope of the rechecks was unaffected.

The coordinator's first disposition of the comprehensibility reviewer's optional 発表 note, repeated in that reviewer's
round-1 message, gave a false basis: "EN gives none". EN 成績 has no such sentence; the RU card's 評価 contrast is RU-only and
quotes EN `評価.md:18`, which gives the reading. The coordinator found this while drafting these records, adopted the note
in fix 3 and disclosed the false basis in the round-3 message to that reviewer.

The recheck prompts forbade running `tools/build_manifest.py` or any other generator; all recheck sections state that none
was run. The correctness reviewer ran `tools/validate.py` in round 1 only; the consistency reviewer ran it in all three
rounds; the comprehensibility reviewer reported not running it in rounds 2 and 3 and did not mention it in round 1. After every recheck the coordinator confirmed that HEAD was unchanged and that
`git status --porcelain --ignored` was empty.

### Round 1 (`e5739f4`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer read the five changed passages with their diff context. C1 is resolved: 必死:21 states actual restraint. C2 is resolved: 息 restores the boundary sentence. Regression check: 思想's «эпохи модернизации» is a contextual rendering, checked against Digital Daijisen 近代 senses 1-2 (era boundaries vary by region); deleting 急激's political aside leaves the Japanese scale distinction intact; 悪戯's tampering no longer entails damage, consistent with JMdict sense 4. `tools/validate.py` reported 0 errors. Correctness and scoped coverage are **CLEAN**. |
| Consistency | The reviewer read the full diff, checked that no title, reading, link or exclusion line changed, and checked every manifest hash (4,354 entries; exactly the five edited entries changed) and the intake's 44 paths and candidate hashes. K1 and K2 stay optional and unchanged; the declined optional guards were withdrawn as requirements. Consistency, quiz safety and cross-file integration are **CLEAN**. |
| Comprehensibility | P1, P2 and P3 are resolved. The reviewer accepted removing «пыталась» but raised P4: «изо всех сил» is the title of 一生懸命, which 必死 excludes, and the gloss of its example at 一生懸命.md:23 («бежал изо всех сил»), so the new wording collapses the synonym contrast that 必死's synonym section draws; remedy «Она отчаянно сдерживала смех.» It also raised P5: the restored 息 sentence answers an English "tone" gloss that nothing in the Russian card raises, an English-dependent remark like P2; remedy: delete it. Both minor. Comprehensibility **NEEDS FIX**; scoped coverage **CLEAN**. The reviewer withdrew its out-of-facet link note (EN also leaves those mentions unlinked); the «óни» and 発表 notes stayed optional. |

The coordinator accepted P4. It accepted P5 on source evidence: frozen EN `docs/n3-vocabulary-sources.tsv:63` records the
source row 息 "breath,tone" with the note that the unqualified "tone" is not established by the supplied 息 entry, and EN
`words/息.md:45` was added in the same commit (`ea3ef0c`) as that adjudication. Current JMdict 1404320 lists breath;
concord/harmony/rapport (息が合う); steam. The coordinator therefore proposed to the correctness reviewer that C2 be
withdrawn, with that evidence.

### Round 2 (`45196f4`)

| Facet | Scope and result |
|---|---|
| Correctness | C1 remains resolved: «отчаянно сдерживала» still asserts restraint and keeps 必死's desperation. The reviewer independently checked `n3-vocabulary-sources.tsv:63` and commit `ea3ef0c` and **withdrew C2**: the EN sentence accompanied the rejection of the source row's unsupported "breath,tone" gloss, RU never teaches that gloss, and RU keeps breathing and rapport with the construction and its example. In its words, the original finding "over-applied retain-every-note to source-specific cleanup". The validator was not rerun. Correctness and scoped coverage are **CLEAN**. |
| Consistency | Only 必死 and 息 changed; 息 is byte-identical to the candidate. «отчаянно» matches 必死's title «отчаянный; неистовый» and removes the fix-1 overlap with 一生懸命's title. All manifest hashes match, exactly the 必死 and 息 entries changed against `e5739f4`, and the intake's 44 paths and candidate hashes match the content diff. `tools/validate.py` reported 0 errors. The reviewer took the EN source-row evidence from the coordinator's message without rereading it. Consistency, quiz safety and cross-file integration are **CLEAN**. |
| Comprehensibility | P1-P3 remain resolved. P4 is resolved with the proposed wording verbatim. P5 is resolved by the deletion; the 息が合う gloss still limits the extension to rapport, and no Japanese distinction raised by the Russian card is lost. Comprehensibility and scoped coverage are **CLEAN**. |

### Round 3 (`c283b5f`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer inspected the 成績 diff and frozen EN `評価.md:18`. The added reading matches the sentence and the EN reading, with only EN's full stop omitted for inline presentation. No regression; C1 remains resolved and C2 withdrawn. The validator was not rerun for this kana-only change. Correctness and scoped coverage are **CLEAN**. |
| Consistency | Only 成績 changed, with no title, link or exclusion line changed; 評価 and 発表 stay plain, so link parity is unchanged. All 4,354 manifest hashes match, exactly the 成績 entry changed against `45196f4`, and the intake's 44 paths and candidate hashes match the content diff. `tools/validate.py` reported 0 errors. Consistency, quiz safety and cross-file integration are **CLEAN**. |
| Comprehensibility | The optional 発表 note is resolved; the reading matches EN `評価.md:18`, and omitting the full stop matches the cited inline style. Findings 1-5 stay resolved. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 必死 example asserts only an attempt | **Resolved** (final wording from P4) | `必死.md:21`; Digital Daijisen 堪える sense 2. |
| Correctness C2: 息 omits EN's "tone" boundary sentence | **Withdrawn** by the reviewer in round 2 | Frozen EN `docs/n3-vocabulary-sources.tsv:63`; EN commit `ea3ef0c`; JMdict 1404320. Restored in fix 1, removed in fix 2. |
| Correctness optional: cite the Russian dictionaries; rephrase 必死:41 | **Optional, not adopted** | Card footers cite JMdict, as in EN; the Russian sources are recorded in this review. 必死:41 lay outside the reviewer's facet, and the comprehensibility reviewer raised no issue with it. |
| Consistency K1: mixed-script «óни» in 鬼 and 悪魔 | **Optional, not adopted** | The device comes from the published, reviewed B185 card `鬼.md` with its explanatory line (`鬼.md:16`); B208 changed only one navigation link there. A possible later polish item. |
| Consistency K2: 急速→急に is weak | **Optional, kept** | Harmless conservative guard; both words describe abrupt or fast change and share 急. |
| Consistency optional guards 意外→[突然, びっくり], 応じる↔答える | **Optional, not adopted** | EN declares neither; the 意外/びっくり stem overlap is inherited from EN "surprising"/"be surprised" across parts of speech; 応じる shares no title segment with 答える, and 返事 already guards 答える. |
| Consistency: redundant symmetric pairs 感じる↔感じ, 急速↔急激 | **Optional, kept** | Harmless; each side documents its own guard. |
| Comprehensibility P1: 思想 «мысль Нового времени» | **Resolved** | `思想.md:19`; `近代.md:12,16,18,33`. |
| Comprehensibility P2: English-dependent «а не политические взгляды» in 急激 | **Resolved** | `急激.md:42`. |
| Comprehensibility P3: 悪戯 «портить механизм» asserts damage | **Resolved** | `悪戯.md:22`. |
| Comprehensibility P4 (round 1): «изо всех сил» is 一生懸命's title | **Resolved** | `必死.md:21`; `一生懸命.md:4,23`. |
| Comprehensibility P5 (round 1): restored 息 "tone" sentence is English-dependent | **Resolved** | `息.md` equals the candidate; see C2. |
| Comprehensibility optional: «óни» in 悪魔 | **Optional, not adopted** | It follows the published 鬼 card; see K1. |
| Comprehensibility optional: 発表 without a reading in 成績 | **Resolved** in fix 3 | `成績.md:37-38`; EN `評価.md:18`. First declined on a false basis; see the process notes. |
| Comprehensibility observation: 必死 «пыталась» matches EN "tried" | **Superseded** by C1 | The reviewer accepted removing «пыталась» in round 1 and contested only the replacement adverb (P4). |
| Comprehensibility out-of-facet note: kanji/恐.md and words/怖い.md leave 恐ろしい and 恐怖 plain | **Withdrawn** by the reviewer in round 1 | EN kanji/恐.md:21,32-33,38-39 and EN words/怖い.md:31 also leave them unlinked; RU keeps EN link parity. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN** after fixes (必死).
- Scoped coverage: **CLEAN**; the only scoped-coverage finding (息) was withdrawn on source evidence.
- Comprehensibility: **CLEAN** after fixes (思想, 急激, 悪戯, 必死, and the 成績 reading; the 息 sentence added in fix 1 was
  removed).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** throughout, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs,
  not transitive groups.

Limits: the rechecks reread only the changed passages and the cards needed to judge them; unchanged cards rest on review
001's full reading. In the rechecks only the correctness reviewer fetched dictionary pages (Digital Daijisen 近代 in round 1)
or reread the EN source-row history (round 2); in round 3 it inspected EN `評価.md:18`. The other reviewers relied on the
earlier evidence and the coordinator's cited sources. No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
