# Batch 192 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `dc2c32f8ce8a1308980a4e2b9b85c21cb758b73b` | `694386eaa3f4a96a292adaa19ae9e771c2e736bb` | Initial review snapshot: the signed candidate, pushed before review. |
| `a4c76160fdeff68a846b0ae051cd9fc8f514ed2a` | `67999270d817bf75954296af71b60a4f841013ac` | Final candidate. |

The final candidate makes these changes:
- `譲る`: the categorical 負ける contrast is replaced by a qualified one limited to the seat example. It names 負ける's «проигрывать», «уступать, поддаваться» and «снижать цену» senses.
- `読み`: the closing 読書 note now says only that 読書（どくしょ）«чтение книг» names the activity and lacks the pronunciation and situation-assessment senses. 読む is guarded.
- `講演` and `招く`: the Russian-only sentences describing test behaviour are removed. 講演 keeps a qualified スピーチ/演説 comparison, and 招く guards 呼ぶ.
- `誘う`: 呼ぶ is guarded.
- `語る`: 話す is guarded.
- `議論`: 話し合う and 論じる are guarded.
- `説`: 説明 is guarded.
- `調査`: a new `quiz_exclusions: [調べる]` field.
- `語学`: a new `quiz_exclusions: [勉強]` field.
- The manifest and intake are regenerated. `contentVersion` is `48c2b7adc31bcbde`, and only the ten changed word hashes differ.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks used the same assigned model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

Rechecks ran serially.
Each reviewer received only:
- its own original findings;
- the coordinator's dispositions of them;
- the revised snapshot;
- the actual diff `dc2c32f..a4c7616`.

HEAD and the working tree were unchanged after every recheck.
The consistency reviewer's validator run left an untracked `tools/__pycache__`. The reviewer removed it, and the coordinator confirmed it was absent.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | `a4c7616` | C192-01 resolved. All ten changed cards were read completely. The partner overlaps for the nine new guards were checked against freshly read Jisho/JMdict entries for 呼ぶ, 話す, 読む, 調べる, 説明 and 勉強, and against 精選版 日本国語大辞典 entries for 読書 and 演説. No changed passage lost an EN teaching point, and there was no regression. Correctness and scoped coverage are **CLEAN**. |
| Consistency | `a4c7616` | Q1–Q4 and C1 resolved. The optional 議論 href item was withdrawn. The nine new guards are one-sided, with no reverse declarations on baseline cards. 読書 stays unlinked in 読み, as in EN. `contentVersion` is `48c2b7adc31bcbde`, exactly the ten changed word hashes are updated, and the validator reports 0 errors. The reviewer could not locate the coordinator's link-parity helper in the repository, so it checked link parity from the diff. The coordinator's run after the fixes reported only the pre-existing `kanji/単.md` extra link to 簡単. Consistency, quiz safety and scoped coverage are **CLEAN**. |
| Comprehensibility | `a4c7616` | C1 resolved. 読み's 読書 sentence now stands apart from the pronunciation point, has the nominative gloss «чтение книг», and stays unlinked for EN link parity. The 調査, 調子 and 語/単語 optional items remain optional and unchanged. The 講演 item is partly addressed, and the fuller contrast remains on 演説. The changed prose in 読み, 講演, 譲る and 招く has no regression; the 譲る hedge was checked against the JMdict 負ける entry. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C192-01: categorical 譲る/負ける contrast | **Resolved** | `譲る.md:44–46`: «В примере с местом 譲る означает уступить его другому, а не проиграть состязание. У 負ける（まける）есть значения «проигрывать», «уступать, поддаваться» и «снижать цену», поэтому это не абсолютное противопоставление.» The 負ける guard is kept. |
| Consistency Q1: 招く and 誘う lack 呼ぶ | **Resolved** | `招く.md:9` is `[招待, 呼ぶ]`. `誘う.md:9` is `[招く, 招待, 呼ぶ]`. |
| Consistency Q2: 語る lacks 話す | **Resolved** | `語る.md:9` is `[話, 話す]`. |
| Consistency Q3: 議論 lacks 話し合う and, optionally, 論じる | **Resolved** | `議論.md:9` is `[論争, 相談, 話し合う, 論じる]`. 論じる was accepted because its own body says 議論する overlaps in meaning. |
| Consistency Q4: 読み→読む, 調査→調べる, 説→説明, 語学→勉強 | **Resolved** | `読み.md:9` is `[読書, 予想, 読む]`. `説.md:9` is `[意見, 説明]`. 調査 and 語学 gain `[調べる]` and `[勉強]`. Each follows an existing precedent: 読書→読む, 研究→調べる and 研究→勉強. |
| Consistency C1: Russian-only test-behaviour sentences in 講演 and 招く | **Resolved; claim partly withdrawn** | Both clauses are removed, and the linguistic distinctions remain. 講演 now ends «…тоже называют выступления перед публикой, но не обязательно лекцию или доклад.» The finding's claim that no other card mentions quiz guards was partly withdrawn. EN-derived cards such as 椋, 笹, 脳, 荒れる, 菊 and 貝 discuss guards. The fix rests on the hard-coded, Russian-only nature of the removed sentences. |
| Comprehensibility C1: 読み–読書 contrast and genitive «чтения книг» | **Resolved with modification** | `読み.md:46–47`: «Отдельно от этого: 読書（どくしょ）, «чтение книг», называет только само занятие чтением; значений «произношение знака» и «оценка ситуации» у него нет.» The suggested link to 読書 was not adopted because EN 読み has no such link. |
| Consistency optional: 議論 `../words/相談.md` href form | **Withdrawn** | Frozen EN uses the same href. |
| Comprehensibility optional: «опрос» for 調査's survey example | **Optional, declined** | «обследование» matches the title and the Jardic entry. «опрос» remains in the meaning line. |
| Comprehensibility optional: 講演 lacks a 演説 distinction | **Optional, partly addressed** | The C1 fix leaves a qualified clause: 演説 and スピーチ name public speeches, but not necessarily a lecture or report. |
| Comprehensibility optional: 調子 «(форма)» may be read as shape | **Optional, declined** | Jardic gives «[спортивная] форма». The body explains 調子がいい/悪い as good or poor form. |
| Comprehensibility optional: 語 and 単語 share an example | **Optional, declined** | Both sentences are in frozen EN (`語.md:18` and `単語.md:19`). |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
