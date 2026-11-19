# Batch 194 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `6947a60b9c7d3731fd7f76d426d5721db87c55ee` | `b3d62aa2c27ac5821b90274487ade692874be11f` | Initial review snapshot: the signed candidate, pushed before review. |
| `330e6214634ad4e22e652a910c5e9c7ef65a548f` | `0b7e8c6f4f122140be31991fdef2fa18dbc4d673` | Final candidate. |

The final candidate makes these changes:
- `見事`: `quiz_exclusions` gains `凄い`.
- `解決`: `quiz_exclusions` gains `決める`.
- `被害`: the opening definition is «ущерб, повреждение или вред с точки зрения того, кто их понёс» instead of «…увиденные со стороны
  того, кто их понёс».
- `被る`: the provenance note now begins «Толкование «страдать» в исходном списке слов…» instead of quoting the English gloss «to suffer».
- `覚ます`: the title and H1 are «пробуждать; выводить из сна» instead of «будить; пробуждать», and the gloss is «пробуждать, выводить из сна».
- `見舞い`: the お-form «добавляет вежливую приставку お» (accepted optional item).
- `解く`: the nuance warning names «развязывать», the card's own physical gloss, instead of «расстёгивать» (accepted optional item).
- The manifest and intake are regenerated. `contentVersion` is `5fb1d9d0be555c9a`, and only the seven changed word hashes differ.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks used the same reviewer agents, model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

Rechecks ran serially.
Each reviewer received only:
- its own original findings;
- the coordinator's dispositions of them;
- the revised snapshot;
- the actual diff `6947a60..330e621`.

HEAD and the working tree were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | `330e621` | The original review had no findings. All seven revised cards and the corresponding frozen EN passages were read. «Пробуждать; выводить из сна» renders EN "awaken; bring out of sleep" and JMdict 1206060 sense 1 (transitive) and is supported by Babenko's verb dictionary on Gramota. 被害's lead keeps EN's sufferer-side perspective. «Толкование „страдать“» is a reader-facing rendering of EN's provenance statement, not a claim about the source list's literal wording. お as a polite prefix is supported by the JMdict/Jisho 御（お）prefix entry. «Развязывать» is JMdict 解く sense 1. No EN sense, note, link or exclusion was lost; the seven hashes match the manifest and the validator reports 0 errors. Correctness and scoped coverage are **CLEAN**. |
| Consistency | `330e621` | F1 and F2 resolved; the two guards are one-sided, with no reverse declarations on baseline cards, and both targets exist. The new 覚ます title has no exact title-segment collision; the 覚ます→起す guard remains justified because both words still denote waking. Only the incidental root «вывод-» overlaps 判断 «суждение; вывод», which is not a defensible substitute. Link parity is unchanged. The reviewer ran the validator (0 errors) and `build_manifest.py` (no change, `5fb1d9d0be555c9a`), re-ran its front-matter, heading, example and exclusion-retention scripts and matched all 42 intake candidate hashes. Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | `330e621` | C1–C3 resolved, and both optional items resolved. 被害 now reads as perspective rather than sight. 被る's revised sentence is Russian and ties «страдать» to the preceding contrast; keeping the note matches EN and published RU cards. The declined 起す sentence would be an RU-only link; its absence matches EN, and the card already says 目を覚ます need not mean waking another person. No regression. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Consistency F1: 見事 lacks 凄い | **Resolved** | `見事.md:9` is `[すばらしい, 立派, 偉い, 感心, 優秀, 上等, 凄い]`, the reviewer's exact remedy. All six EN entries are retained. |
| Consistency F2: 解決 lacks 決める | **Resolved as a conservative guard** | `解決.md:9` is `[答, 決定, 解く, 解ける, 決める]`. It follows the batch's 解く→決める for the shared Russian «решать». |
| Comprehensibility C1: 被害 «увиденные» can read as harm that was seen | **Resolved with a variant remedy** | `被害.md:16`: «…с точки зрения того, кто их понёс». The proposed «со стороны того…» was not used because it can be misread as the party that caused the harm. |
| Comprehensibility C2: 被る ends with an English gloss and source-list meta | **Partially accepted; resolved** | `被る.md:46–48` renders the gloss as «страдать». The note was kept rather than deleted: EN keeps it, and published RU cards (便, 変化, 後, 空, 素, 注ぐ) keep the same kind of source-list note. The reviewer accepted this on recheck. |
| Comprehensibility C3: 覚ます title copies 起す «будить»; no 起す comparison | **Title accepted; sentence and link declined; resolved** | `覚ます.md:4,12,16`: «пробуждать; выводить из сна». The comparison sentence with a [起す] link was declined because EN 覚ます has neither, and RU must not add RU-only links. The reviewer accepted the residual gap as matching EN. |
| Comprehensibility optional: say that お in お見舞い is the polite prefix | **Optional, accepted** | `見舞い.md:18`: «добавляет вежливую приставку お», matching 箸 and お見舞い. |
| Comprehensibility optional: 解く warns against «расстёгивать», which it never teaches | **Optional, accepted** | `解く.md:39`: «развязывать», the card's own physical gloss. |
| Consistency optional: guard 解決–決まる | **Optional, declined** | 決まる «решаться; быть решённым» is an intransitive verb, 解決's title is a noun and 決定 already guards «решение». The reviewer withdrew it on recheck. |
| Consistency optional: 親友–親しい | **Optional, unchanged** | Noun versus adjective, unguarded in EN; the reviewer recommended no action. |
| Consistency optional: 被る provenance sentence | **Handled under C2** | The reviewer confirmed nothing remains in its facet. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** after fixes, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
