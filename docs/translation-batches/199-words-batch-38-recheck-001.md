# Batch 199 — independent recheck 001

## Snapshots

| Snapshot | Tree | Change |
|---|---|---|
| Staged candidate (scratch worktree) | `b99047ab07da1b5364690335e4fede1db79dca76` | Initial review snapshot, on top of the reviewed Batch 198 tree `80c7336`. |
| Staged revision (scratch worktree) | `841bc8c046cc7e4141696ceba1e213b6a98b2d7e` | Review fixes; the snapshot read by the rechecks. |
| `4ff5f6a3d68716fff63534d4ee93322ec59ca182` | `cad97d1763da0789142085e46c5a943d2a1f4ca0` | Signed candidate on `full-ru-199-words-38`: the content of `841bc8c` plus the intake. |

The revision changes six word files and regenerates `manifest.json`:
- `盛り`: line 19 translates 桜は盛りを過ぎました as «Пик цветения сакуры уже прошёл.» (past the peak, as EN's "past their
  peak"), replacing «Сакура уже отцвела», which claimed that flowering had ended.
- `真似`: lines 37–39 describe the Russian-added 写す/コピー contrast as a tendency: they are usually «копировать», and their
  meanings can overlap with 真似. The restriction to texts, files and images is removed.
- `指導`: lines 39–40 describe 教育 as a broader concept of education, training and upbringing that can also apply to training
  particular people, instead of «вся система обучения и воспитания».
- `ゴール`: line 27 reads «Это заимствование из английского goal, записанное катаканой.» The gloss-equivalence wording
  «соответствует английскому goal» is removed; the English source word is kept, as in the reviewed アナウンサー, カーブ and
  オフィス cards.
- `知識`: line 19 translates 日本の歴史についての知識を増やしたいです as «Я хочу пополнить свои знания об истории Японии.»,
  keeping the noun that the card's note at lines 42–44 analyses.
- `直に`: the inline «словарная запись 1430700» at line 40 is removed; the footer still cites entry 1430700, senses 1–2.
- Only these six word hashes and `contentVersion` change in the manifest. No front matter changes and no link is added or removed.

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
- the actual diff from `b99047a` to `841bc8c`.

The prompts took the changed-file count from the diff (six word files plus the manifest), and all three reports agree.

Commit signing was unavailable throughout the review: the signing key's passphrase cache had expired. Both snapshots were therefore
staged trees in a scratch worktree, and reviewers were told to read those trees rather than HEAD. No unsigned commit was made.
After Batch 198 was published, the reviewed content was committed signed as `4ff5f6a`. `git diff 841bc8c 4ff5f6a -- words
kanji strokes articles manifest.json` is empty.

The worktree's index tree, working tree and untracked-file list were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `841bc8c` | C1–C3 are resolved. C1: «Пик цветения сакуры уже прошёл» keeps 盛りを過ぎる as past the peak (Digital Daijisen さかり sense 1). C2: the 写す/コピー wording now allows overlap and drops the artificial object restriction (JMdict 写す senses 1/3, コピー senses 1/2). C3: 教育 may concern individuals (Digital Daijisen 教育 sense 1 and its 新入社員を教育する example). Regression check of every changed passage: the reviewer independently inspected Digital Daijisen's ゴール【goal】 entry on weblio and found the donor-word wording accurate; 知識 keeps the desire, the noun and the topic; removing 直に's inline entry number removes no reading or sense. It confirmed identical front matter, link targets and Japanese example sentences in all six cards and matched the six changed hashes to the files. Correctness and scoped coverage are **CLEAN**. |
| Consistency | tree `841bc8c` | No original findings. The optional items stay unchanged: 登山→登る is retained as conservative; no stem-level guard is needed for 直に/自身, 相手/向こう, 真剣/集中 or 情報/通信; 指導→管理 is still not established as necessary. The revised 真似 and 指導 passages still support their declared guards. The reviewer found front matter and link targets byte-identical in the six cards, rebuilt the manifest in memory (equal to `manifest.json`) and ran the validator (0 errors). Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `841bc8c` | C1–C3 are resolved. C1: the gloss-equivalence wording is gone; the remaining "goal" is an etymon, as in `カーブ.md:27`, and the Russian senses are already in the meaning section. C2: the translation matches the card's note. C3: the example now teaches past the peak. The 直に entry-number optional is resolved; «расспросил», «занимается с» and the 眺める title stay optional and were not promoted. Regression check: 真似 and 指導 remain readable without English. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 盛り «Сакура уже отцвела» | **Resolved** | `盛り.md:19`. Also comprehensibility C3. |
| Correctness C2: 写す/コピー confined to texts, files and images | **Resolved** | `真似.md:37-39`. |
| Correctness C3: 教育 as «вся система» only | **Resolved** | `指導.md:39-40`. |
| Comprehensibility C1: «соответствует английскому goal» | **Resolved, in modified form** | `ゴール.md:27`. The English source word is kept as an etymon rather than deleted, following the reviewed loanword cards; the reviewer accepted it. |
| Comprehensibility C2: 知識 «больше узнать» | **Resolved** | `知識.md:19`. |
| Comprehensibility C3: 盛り «отцвела» | **Resolved** | Same fix as correctness C1. |
| Comprehensibility optional: inline entry number in 直に | **Optional, adopted** | `直に.md:40`; the footer keeps the citation. |
| Comprehensibility optional: 直に «выслушал» for «расспросил» | **Optional, declined** | 作家に話を聞く is interview-like here and «лично» carries じかに; the reviewer did not promote it. |
| Comprehensibility optional: 指導 «наставляет» / «занимается с» | **Optional, declined** | The meaning section already defines 指導する as «руководить, наставлять»; EN has "training". |
| Comprehensibility optional: 眺める title without «подолгу» | **Optional, declined** | The title renders EN's "gaze at"; the body marks duration as a tendency. |
| Consistency optional: drop 登山→登る | **Optional, declined** | The weakest conservative guard but harmless; the reviewer accepted retention. |
| Consistency optional: add 指導→管理 | **Optional, declined** | Necessity not established. |
| Consistency optional: stem-level guards 直に/自身, 相手/向こう, 真剣/集中, 情報/通信 | **Optional, declined** | The reviewer judged them unnecessary. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN** after fixes.
- Scoped coverage: **CLEAN** after fixes.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN**, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

Limits: the correctness reviewer could not confirm JMdict entry 1054230's raw source-language field because the Jisho API
returned an empty `source` array; the donor word was verified in Digital Daijisen instead. Unchanged cards were not reread in the
rechecks. No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
