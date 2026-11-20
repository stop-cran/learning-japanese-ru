# Batch 205 — independent recheck 001

## Snapshots

| Snapshot | Tree | Change |
|---|---|---|
| Staged candidate (scratch worktree) | `e26a8e9466a82a925d4a0c429efe08a701323ae3` | Initial review snapshot, on top of the reviewed Batch 204 tree `d9a9765`. |
| Staged revision (scratch worktree) | `84dc60f36a87e9d9830a88933c63105d0aad4bf4` | Review fixes; the snapshot read by the rechecks. |
| `18386f84bbdd74074d7667d508602bda5900e05b` | `4906ff8fb26006e31c174903c08c63aedeef5482` | Signed candidate on `full-ru-205-words-44`: the content of `84dc60f` plus the intake. |

The revision changes seven word files and regenerates `manifest.json`:
- `札`: lines 40-41, «Если в списке слов рядом с чтением さつ стоят такие переводы, они относятся к слову ふだ; чтению さつ
  соответствует значение «банкнота».», become lines 40-43: «Если словарь или список слов даёт при чтении さつ переводы «билет»
  или «бирка», это значения слова ふだ. Так было и в исходном списке слов, на котором основана эта карточка: там чтение さつ
  соединено с переводами слова ふだ. Карточка сохраняет это чтение и учит подтверждённому значению «банкнота»; что имел в виду
  составитель списка, остаётся неясным.» The correctness and comprehensibility reviewers had flagged the same sentence
  independently, so the rewrite merges their remedies rather than using either verbatim: the comprehensibility reviewer's
  learner-facing dictionary warning comes first, and EN's qualification that the correction does not establish the compiler's
  intent is kept in the wording already published in 無, 素 and 便.
- `有効`: the ticket example (line 17) is translated «Этот билет действителен по завтрашний день включительно.» instead of
  «Этот билет действителен до завтра.», making EN's "valid through tomorrow" explicit.
- `旧`: the school example (line 21) is translated «Это прежнее здание школы.» instead of «Это старое здание школы.», so the
  example keeps the 旧/古い distinction that the card's own note makes.
- Quiz exclusions only: `暮らす.md:9` reads `quiz_exclusions: [住む, 生きる, 生活]` instead of `[住む, 生きる]`;
  `暗記.md:9` adds `quiz_exclusions: [覚える]` after `tags:`; `書類.md:9` adds `quiz_exclusions: [紙]` after `tags:`;
  `服装.md:9` reads `quiz_exclusions: [衣服, 服, 格好]` instead of `[衣服, 服]`.
- Only these seven word hashes and `contentVersion` change in the manifest. No title, link, reading or Japanese example changes;
  the only front-matter changes are the four exclusion lines.

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
- a short description of each change made in response to the other reviewers, without their reports; for the shared 札
  sentence, the correctness and comprehensibility reviewers were each told in one sentence what the other had flagged;
- the revised snapshot;
- the actual word diff from `e26a8e9` to `84dc60f`.

The prompts took the changed-file count from the diff (seven word files plus the manifest), and all three reports agree.

Commit signing was still unavailable: the signing key's passphrase cache had expired. Both snapshots were therefore staged trees
in a scratch worktree, and reviewers were told to read those trees rather than HEAD. No unsigned commit was made. After Batch 204
was published, the reviewed content was committed signed as `18386f8`. `git diff 84dc60f 18386f8 -- words kanji strokes
articles manifest.json` is empty.

The recheck prompts forbade running `tools/build_manifest.py` or any other generator; all three reports state that none was run.
After every recheck the coordinator confirmed that `git write-tree` still printed `84dc60f…`, that the working tree equalled the
index, and that no untracked or ignored file existed.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `84dc60f` | C1 is resolved: `札.md:40-43` names the list as the source list underlying the card, states the reading/gloss mismatch and the retained banknote identity, and ends with «что имел в виду составитель списка, остаётся неясным», preserving EN's qualification without claiming the compiler's intent. The reviewer checked the qualification against the frozen EN card itself. The optional 有効 clarification is adopted and accurately retains "valid through tomorrow"; the 明後日 register note stays optional. Regression check: the reviewer read all seven revised cards in full and the RU 覚える, 生活, 紙 and 格好 cards. 旧's «прежнее» conveys the former-building relation without an age or condition claim, and the four added exclusions remove no teaching content and assert no unrestricted synonymy. It freshly inspected the Jisho API entries for 覚える (sense 1 memorize, learn by heart), 生活 (sense 1 life, living; intransitive する-verb), 紙 (paper) and 格好 (shape, form; appearance, style). Japanese example-and-reading prefixes are identical in all seven cards, and their LF-normalized hashes match the manifest. Correctness and scoped coverage are **CLEAN**. |
| Consistency | tree `84dc60f` | F1 and F2 are resolved: 暮らす→生活 and 暗記→覚える close the gaps, and both targets exist. The optional 書類→紙 and 服装→格好 guards are adopted as conservative guards and resolved; their targets exist. The 書斎/研究室, 元/基/素, 時刻/何時 and 暮らす/過ごす items are withdrawn as unnecessary. Regression check: the new exclusion lines follow `tags`, as elsewhere; the guards are direct and one-sided, the app applies them symmetrically, all EN exclusions are retained, and no other exclusion changed. The diff adds or removes no link, so EN link parity is unchanged; the reviewer agreed that 替える's plain-text pointer stays, because EN links that article at that position and the article is absent in RU. The 札 sentence has no links or quiz impact. The reviewer recomputed the seven hashes, found that only they and `contentVersion` differ in the manifest, and ran the validator (0 errors). Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `84dc60f` | C1 is resolved: the 札 rewrite opens with the learner-facing warning, then identifies the source list and keeps the banknote teaching and the qualification in the pattern of the published 無, 素 and 便 cards, so it no longer reads as though the app showed the wrong gloss. C2 is withdrawn: the card already states the を/に contrast and the 換える/代える/変える tendencies, no rule depends on the absent article, and the same unlinked pointer is published in 戻る and similar pointers in 作家, 政治家, 武士, 研究員, いかがわしい and 疑わしい. The optional 旧 change is resolved and matches the following contrast with the building that replaced it. The other optional items stay optional. Regression check: 有効's inclusive wording was judged against Japanese 明日まで and EN "through tomorrow", without a fresh dictionary fetch; the four exclusion-only edits contain no learner text. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 札 drops EN's qualification that the correction does not establish the compiler's intent | **Resolved** | `札.md:40-43`; frozen EN 札. |
| Correctness optional: 有効 «включительно» | **Optional, adopted** | `有効.md:17`. |
| Correctness optional: 明後日 register note | **Optional, unchanged** | Not in EN; the RU あさって card gives the contrast. |
| Consistency F1: 暮らす and 生活 lack a direct guard | **Resolved** | `暮らす.md:9`. |
| Consistency F2: 暗記 and 覚える lack a direct guard | **Resolved** | `暗記.md:9`. |
| Consistency optional: 書類–紙 and 服装–格好 guards | **Optional, adopted** (conservative) | `書類.md:9`, `服装.md:9`. |
| Consistency optional: 書斎/研究室, 元/基/素, 時刻/何時, 暮らす/過ごす | **Withdrawn** | The reviewer had judged no guard necessary and confirmed this on recheck. |
| Comprehensibility C1: 札's unexplained word-list sentence | **Resolved** | `札.md:40-43`. |
| Comprehensibility C2: 替える points to the absent かえる article | **Withdrawn** | Plain-text pointers to untranslated articles stay so the link can be restored at EN's position (`戻る.md:64-65`; Batch 195 declined the same request for 作家); the reviewer withdrew C2 on recheck. |
| Comprehensibility optional: 旧 «прежнее» | **Optional, adopted** | `旧.md:21`. |
| Comprehensibility optional: 更に, 景気, 明後日, 本人/自身, 書類/書物 | **Optional, unchanged** | Not established as defects; the reviewer agreed on recheck. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN** throughout.
- Scoped coverage: **CLEAN** after fixes (札).
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after fixes, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

Limits: the rechecks reread only the changed passages; unchanged cards rest on review 001's full reading. Apart from the
correctness reviewer's fresh Jisho API inspection of 覚える, 生活, 紙 and 格好, dictionary entries were not refetched; the
consistency reviewer's dictionary bases for the new guards are from its own knowledge of JMdict senses and the taught card
senses. No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.