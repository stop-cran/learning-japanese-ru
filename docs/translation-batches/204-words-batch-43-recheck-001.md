# Batch 204 — independent recheck 001

## Snapshots

| Snapshot | Tree | Change |
|---|---|---|
| Staged candidate (scratch worktree) | `c4b6d94520f4755df78422eb4d06805db0b988a1` | Initial review snapshot, on top of the reviewed Batch 203 tree `20d0232`. |
| Staged revision (scratch worktree) | `d9a9765a5addaf58e31fefd85fb97eed1d242b99` | Review fixes; the snapshot read by the rechecks. |
| `b0e6a9334e0ba31036280983f37ca21f339071d1` | `357d090d8fa6c2b2fbc3b3418565d994b0359675` | Signed candidate on `full-ru-204-words-43`: the content of `d9a9765` plus the intake. |

The revision changes ten word files and regenerates `manifest.json`:
- `次第`: line 31 reads «…оно подчёркивает момент, когда вслед за одним событием сразу происходит другое, часто неожиданное.»
  instead of «…оно связывает уже случившееся событие с тем, что произошло в тот же миг, часто неожиданно.», using the
  correctness reviewer's text. The dictionary line (37) ends «; для сравнения запись 1610870（途端）.», and line 39 adds
  «Конструкция 途端: [Bunpro, たとたんに](https://bunpro.jp/grammar_points/%E3%81%9F%E3%81%A8%E3%81%9F%E3%82%93%E3%81%AB).»,
  the same external URL that the RU 途端 card cites.
- `お昼`: line 9 reads `quiz_exclusions: [昼食, 昼御飯, 昼, 昼間]` instead of `[昼食, 昼御飯, 昼]`.
- `プラス`: line 9 adds `quiz_exclusions: [足す]` after `tags:`.
- `歓迎`: the verb gloss (line 16) is «радушно принимать кого-то или что-то; благосклонно относиться к чему-то» instead of
  «радушно принимать, приветствовать кого-то или что-то»; the people example (line 18) is translated «Мы все радушно приняли
  нового учителя.» instead of «Мы все тепло встретили нового учителя.»; and line 29 adds, after «…но это разные действия.»,
  «迎える（むかえる）«встречать; приветствовать» описывает встречу прибывающего человека, например на вокзале; 歓迎 подчёркивает
  радушие приёма или благосклонное отношение, а не сам факт встречи.» The sentence is plain text, because EN does not link
  迎える here and RU-only internal links would break link parity.
- Optional comparison-entry citations adopted on the dictionary lines of `事情` (1261190 原因), `様` (1328110 手段), `構成`
  («Для сравнения: записи 1279790（構造）и 1397590（組む）.» instead of «Для сравнения: запись 1279790.»), `検討`
  (1561620 論じる), `栄養` (1358680 食料品) and `松` (1349920 松竹梅). Each ID matches the compared card's own dictionary line;
  構造 has no RU card and matches the frozen EN 構造 card.
- Only these ten word hashes and `contentVersion` change in the manifest. No title, link target, reading or Japanese example
  changes; the only front-matter changes are the お昼 and プラス exclusions.

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
- the coordinator's dispositions of its findings and optional items;
- a one-line description of each change made in response to the other reviewers, without their reports;
- the revised snapshot;
- the actual diff from `c4b6d94` to `d9a9765`.

The prompts took the changed-file count from the diff (ten word files plus the manifest), and all three reports agree.

Commit signing was still unavailable: the signing key's passphrase cache had expired. Both snapshots were therefore staged trees
in a scratch worktree, and reviewers were told to read those trees rather than HEAD. No unsigned commit was made. After Batch 203
was published, the reviewed content was committed signed as `b0e6a93`. `git diff d9a9765 b0e6a93 -- words kanji strokes
articles manifest.json` is empty.

The recheck prompts forbade running `tools/build_manifest.py` or any other writing tool; all three reports state that no generator
was run. After every recheck the coordinator confirmed that `git write-tree` still printed `d9a9765…`, `git diff --quiet` exited 0,
and no untracked or ignored file existed.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `d9a9765` | C204-1 is resolved: `次第.md:31` uses the reviewer's replacement exactly; the past-only wording is gone, while the た-form attachment, the ます-stem + 次第 contrast and the original examples remain. The reviewer freshly inspected Bunpro's たとたんに page (Structure/About/Examples: Verb[た] + とたん(に), an immediate, possibly unexpected development, with the nonpast traffic-light warning) and confirmed that RU 途端's dictionary line carries 1610870 and the same construction URL. The optional comparison IDs are adopted as an editorial improvement; each matches the compared card's own dictionary line, and no existing citation or sense range was removed. Regression check of every changed passage: 歓迎's new gloss keeps both welcoming a person and favourable reception of something, the new translation keeps agent, object, completed action and positive reception, and the 迎える sentence describes the arrival/meeting use without claiming that the words never overlap (Jisho 歓迎 "welcome; (warm) reception"; Jisho 迎える sense 1 "go out to meet; receive; welcome; greet"; Digital Daijisen 歓迎 on Weblio 喜んでむかえること／喜んで受け入れること, with 建設的な批判は歓迎する); the お昼, プラス and citation edits introduce no teaching-rule change. The reviewer ran the validator (0 errors) and confirmed that the ten LF-normalized hashes match the manifest. Correctness and scoped coverage are **CLEAN**. |
| Consistency | tree `d9a9765` | F1 is resolved: `お昼.md:9` adds 昼間, which exists, and keeps EN's 昼食, 昼御飯 and 昼. F2 is resolved as the proposed conservative guard: `プラス.md:9` `quiz_exclusions: [足す]` is a valid single-line key, and 足す exists. The declined 正–本当, 来–次 and 横断–越える guards are accepted: no title segment is shared, EN declares none, and the reviewer had rated them low risk. The 梅-terminology item is withdrawn: 松 and 桜 pair «японская слива» with the 梅 card's title term «японский абрикос», the 梅 card itself names «японские сливы» as a culinary name, and 竹/桃 use «слива умэ». The forward obligation (EN exclusions on untranslated cards that target batch words) stays informational. Regression check: the Bunpro URL is byte-identical to RU 途端's, so there is no RU-only relative link; «Конструкция 途端:» names the construction, a minor and acceptable variant of 途端's «Конструкция:»; every cited ID matches the cited card, each compared word is already an exclusion target, and «для сравнения запись N（word）» is uniform; 歓迎's exclusions are unchanged and its 迎える mention is unlinked plain text matching the 迎える card's title; no title changed. Only the ten changed entries and `contentVersion` differ in the manifest, and their hashes match; the validator reports 0 errors. Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `d9a9765` | C1 is resolved: 歓迎's gloss, people example and station contrast now separate it from 迎える without a link; the reading and the other card's title are inline, and «приветствовать» remains only as 迎える's quoted title. The declined optional items are accepted: 松 shows まつ and explains the ranking with 松・竹・梅 readings, and the published 松竹梅 card uses «мацу»; the 横断, 検討, 欠席, 栄養, 構成, 機嫌 and 事情 notes were not established defects, and each distinction is already in the card's paired gloss or an existing comparison card. Regression check: 次第's 途端 sentence is unambiguous and keeps the attachment contrast with 分かり次第、連絡します; the Bunpro line names the Japanese construction and matches 途端's source link, so it is not teaching-body noise; each new citation names a word the card body already explains; the お昼 and プラス changes are not learner prose. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C204-1: 次第 presents actual past occurrence as the rule of た-форма + 途端に | **Resolved** | `次第.md:31`, the reviewer's text; source lines 37 and 39. |
| Correctness optional: comparison-entry IDs for Russian-only lexical comparisons | **Optional, adopted** | Dictionary lines of 事情, 様, 構成, 検討, 栄養, 松 and 次第; each ID matches the compared card's own line. |
| Correctness optional: Russian-dictionary citations | **Optional, unchanged** | No semantic defect established; the reviewer inferred no publication blocker. |
| Consistency F1: お昼 and 昼間 lack a direct guard | **Resolved** | `お昼.md:9`. |
| Consistency F2: プラス and 足す lack a direct guard | **Resolved** (conservative) | `プラス.md:9`. |
| Consistency optional: 正–本当, 来–次, 横断–越える guards | **Optional, declined** | No shared title or segment; EN declares none; rated low risk. The reviewer accepted the decline. |
| Consistency optional: 梅 called «японская слива» in 松 and 桜 | **Withdrawn** | Both cards also give «японский абрикос»; the RU 梅 card's own note allows «японские сливы». The reviewer withdrew the item on recheck. |
| Comprehensibility C1: 歓迎's gloss and people example reuse 迎える's Russian | **Resolved** | `歓迎.md:16,18,29`. |
| Comprehensibility optional: 松 «Мацу»; notes on 横断, 検討, 欠席, 栄養, 構成, 機嫌, 事情 | **Optional, declined** | Not established as defects; the reviewer agreed on recheck. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN** after fixes.
- Scoped coverage: **CLEAN** throughout.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after fixes, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

Limits: the rechecks reread only the changed passages; unchanged cards rest on review 001's full reading. Apart from the
correctness reviewer's fresh Bunpro, Jisho and Weblio inspection, dictionary entries were not refetched; the new comparison IDs
were cross-checked against the existing RU cards and the frozen EN 構造 card, not re-derived from a raw JMdict archive. No
native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
