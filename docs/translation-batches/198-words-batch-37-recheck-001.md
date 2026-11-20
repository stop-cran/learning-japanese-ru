# Batch 198 — independent recheck 001

## Snapshots

| Snapshot | Tree | Change |
|---|---|---|
| Staged candidate (scratch worktree) | `c82e94b30d2c72c36fb56406ba2aaaf1f54e0002` | Initial review snapshot, on top of the reviewed Batch 197 tree `ea3a478`. |
| Staged revision (scratch worktree) | `80c7336de2a89655b543c35641a339e44f5a0833` | Review fixes; the snapshot read by the rechecks. |
| `174d0cca377e42a87ca99e3bdd9d24274a1d9278` | `d352e7de35e8a1038e565b29160ce148b11ac0c5` | Signed candidate on `full-ru-198-words-37`: the content of `80c7336` plus the intake. |

The revision changes eight word files and regenerates `manifest.json`:
- `移動`: `quiz_exclusions` becomes `[移す, 移る, 動かす, 動く]`. 動かす answers F1. 動く «двигаться; работать» is a conservative
  coordinator extension: 移動 «перемещение; передвижение» shares the stem of «двигаться», 移動する is taught both transitively
  and intransitively, and the baseline already pairs 移す→動かす and 移る→動く.
- `穀物`: line 20 translates 米や麦などの穀物 as «зерновые, например рис и пшеницу или ячмень», keeping 麦 as one cover-term item.
  Lines 38–39 say that 穀物 names grain or grain crops in general, not a finished grain product or one particular crop.
- `積む`: line 20 translates 箱を三つ積みました as «Я сложил три коробки стопкой.».
- `積極的`: the warning against «положительный результат анализа или положительное число», which depended on English "positive",
  is removed. The talkative-personality boundary is unchanged.
- `神経`: lines 27–28 state the premise before rejecting the literal parse: «У 経 есть и значение «сутра», но 神経 нельзя понимать
  буквально как «писание бога».» RU `kanji/経.md` is titled «проходить; сутра» and teaches お経.
- `祭`: lines 39–40 replace the author-facing dictionary note with «В разговорной речи и в интернете у 祭 есть и другие значения;
  в обычных описаниях праздника это слово значит «фестиваль».».
- `空き`: line 21 asks «Завтра после обеда есть свободное окно?», keeping the kind of availability unspecified.
- `積もる`: line 19 translates 道に雪が積もっています as the state «На дороге лежит снег.».
- Only these eight word hashes and `contentVersion` change in the manifest. No link is added or removed.

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
- the actual diff from `c82e94b` to `80c7336`.

The prompts' summary line misstated the change as nine word files, repeating the Batch 196 slip. The diff itself,
which every reviewer read, changes eight word files plus the manifest, and all three reports describe eight. Later
recheck prompts take the count from the diff.

Commit signing was unavailable throughout the review: the signing key's passphrase cache had expired. Both snapshots were therefore
staged trees in a scratch worktree, and reviewers were told to read those trees rather than HEAD. No unsigned commit was made.
After Batch 197 was published, the reviewed content was committed signed as `174d0cc`. `git diff 80c7336 174d0cc -- words
kanji strokes articles manifest.json` is empty.

The worktree's index tree, working tree and untracked-file list were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `80c7336` | No original findings. The 穀物 optional is resolved: «как сырьё» is gone, and the note covers grain and grain crops without naming one product or crop. Regression check of every changed passage: «например» keeps the open や…など list and 麦 stays a cover term (the reviewer read JMdict 麦: wheat, barley, oats); «сложил три коробки стопкой» adds no extra event; «На дороге лежит снег» is a natural result state; «свободное окно» keeps the availability unspecified; 積極的 loses only the English-dependent warning. For 神経 it read the separate 経（きょう） "sutra" and お経 entries and found the premise true, with the compound's reading シン + ケイ unchanged. The reviewer matched all eight changed hashes to `manifest.json` and ran the validator (0 errors). Correctness and scoped coverage are **CLEAN**. |
| Consistency | tree `80c7336` | F1 is resolved: 移動 now guards 動かす, and the target exists. The 動く extension was judged justified as a conservative guard, not an over-guard: it shares the «двиг-» stem, 移動する is also intransitive, and 移る→動く is a baseline precedent. It does not guard a contrast taught as an antonym. The 祝い→お祭り, 祭→お祝い/祝い and 祝い→お土産 optionals stay optional and their retention is acceptable. The 動かす–動く optional is withdrawn. The reviewer found that the diff adds or removes no link and changes no other front matter, recomputed every manifest hash (0 stale) and ran the validator (0 errors). Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `80c7336` | C1–C5 are resolved. C4: the sutra premise is now stated and supported by the linked 経 and 神 kanji titles, so «писание бога» is no longer an unmotivated calque. C5: the note is now a learner-facing festival boundary. The 空き and 積もる optionals are resolved. The 礼儀–行儀 and 祝う–喜ぶ contrasts stay optional; they are not missing EN points. Regression check: the rewritten 穀物 note is readable without English "cereal" or "corn" and agrees with the example and the 米/麦 notes; 移動 changes only quiz metadata. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Consistency F1: no 移動–動かす guard | **Resolved** | `移動.md:9`. |
| Coordinator extension: 移動→動く | **Conservative guard, accepted on recheck** | `移動.md:9`. Not a finding; the consistency rechecker judged it justified and conservative. |
| Consistency optional: drop 祝い→お祭り | **Optional, declined** | The baseline お祭り card already guards お祝い, and 祝い shares «празднование» with お祝い. The reviewer accepted keeping it. |
| Consistency optional: drop 祭→お祝い/祝い and 祝い→お土産 | **Optional, declined** | Conservative guards; the reviewer required no action. |
| Consistency optional: 動かす–動く | **Withdrawn** | Not recommended by the reviewer; 動かす «приводить в движение» is distinct from 動く. |
| Correctness optional: 穀物 «как сырьё» | **Optional, adopted** | `穀物.md:38-39`. |
| Comprehensibility C1: three crops for 米や麦 | **Resolved** | `穀物.md:20`. |
| Comprehensibility C2: «одна на другую» for three boxes | **Resolved** | `積む.md:20`. |
| Comprehensibility C3: English "positive" warning in 積極的 | **Resolved** | `積極的.md:39-40`. |
| Comprehensibility C4: unmotivated «писание бога» | **Resolved, in modified form** | `神経.md:27-28`. The premise is stated instead of deleting EN's warning; the reviewer accepted it. |
| Comprehensibility C5: author-facing dictionary note in 祭 | **Resolved, in modified form** | `祭.md:39-40`. Rewritten as learner guidance instead of deleted, keeping EN's scope boundary. |
| Comprehensibility optional: 空き «свободное время» | **Optional, adopted** | `空き.md:21`. |
| Comprehensibility optional: 積もる «Дорогу засыпало снегом» | **Optional, adopted** | `積もる.md:19`. |
| Comprehensibility optional: 礼儀–行儀 and 祝う–喜ぶ one-line contrasts | **Optional, declined** | Not in EN; the distinctions are available on 行儀 and in 祝う's action-not-feeling wording. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** after fixes, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
