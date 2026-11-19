# Batch 193 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `8fd47e7ccd776202db66e8f088d806a7693c02ac` | `a970b95cf288742a0ad921983505596e806124c4` | Initial review snapshot: the signed candidate, pushed before review. |
| `82b1d3b8c80ef016f234730e66c12c31da156a1f` | `b60a80df84c05dae0ae8471e4371391230024e30` | Final candidate. |

The final candidate makes these changes:
- `訓`: the first example's translation ends «— Кунное чтение знака 山 — やま.», giving the reading in kana instead of the Cyrillic «яма».
- `記事`: the sentence comparing the word with the English letters a and the, and with 冠詞（かんし）«артикль», is deleted. The paragraph now ends «…что он сообщает свежие новости.»
- `試し`: the first example's translation is «Я на пробу воспользовался этим приложением, чтобы посмотреть, что оно собой представляет.» (accepted optional item).
- `訪問`: お見舞い is guarded.
- `判断`: a new `quiz_exclusions: [読み]` field.
- The manifest and intake are regenerated. `contentVersion` is `562e894c59511c4c`, and only the five changed word hashes differ.

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
- the actual diff `8fd47e7..82b1d3b`.

HEAD and the working tree were unchanged after every recheck.
The consistency reviewer's validator run left an untracked `tools/__pycache__`. The reviewer removed it, and the coordinator confirmed it was absent.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | `82b1d3b` | The original review had no findings. All five revised cards, the existing お見舞い and 読み cards and frozen EN 記事 and 試し were read in full. やま is the kun reading of 山. Removing 記事's English-dependent remark loses no Japanese distinction, because Russian «статья» does not carry the grammatical sense of English "article". The new 試し translation renders 試しにこのアプリを使ってみました without asserting a result. The two new guards reflect genuine overlaps: 訪問 includes visiting a sick person, and 読み teaches «оценка ситуации». No regression. Correctness and scoped coverage are **CLEAN**. |
| Consistency | `82b1d3b` | F1–F3 resolved. The two new guards are one-sided, with no reverse declarations on baseline cards. 記事's link multiset matches EN (6 and 6). The reviewer ran the validator (0 errors) and `build_manifest.py`, which reproduces the manifest exactly (`contentVersion` `562e894c59511c4c`), and spot-checked all five changed intake hashes against the manifest. Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | `82b1d3b` | C1 resolved; the 記事 paragraph is complete and grammatical. The 試し item is resolved: «на пробу» reinforces the definition, and the next sentence still explains に with ～てみる. 訓's やま matches the card's later contrast of кунное やま and онное サン. The 証明, 判断, 検査, 記念 and 触れる optional items remain optional and unchanged. No regression. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Consistency F1: 訓 renders the reading of 山 as Cyrillic «яма» | **Resolved** | `訓.md:19`: «— Кунное чтение знака 山 — やま.» This matches EN's plain kana. |
| Consistency F2: 訪問 lacks お見舞い | **Resolved** | `訪問.md:9` is `[訪ねる, 伺う, お見舞い]`. The existing お見舞い card already contrasts itself with general 訪問. |
| Consistency F3: 判断 lacks 読み | **Resolved as a conservative guard** | `判断.md:9` is `[読み]`. It follows the batch's 評価→読み and EN's 解釈→読み. |
| Comprehensibility C1: 記事 explains itself through English a and the | **Resolved** | `記事.md:38–39` ends «…что он сообщает свежие новости.» No teaching rule was removed. |
| Comprehensibility optional: stiff 試し:19 translation | **Optional, accepted** | `試し.md:19`: «Я на пробу воспользовался этим приложением, чтобы посмотреть, что оно собой представляет.» «посмотреть» keeps EN's "to see". |
| Comprehensibility optional: 証明:23 points at the こと/わけ topic absent from RU | **Optional, declined** | The sentence names a topic and is not a link. The same unlinked pointer form is used in `おかげ.md:52`, `かぎり.md:42` and `ほか.md:52`, and the attachment rules are complete in the paragraph. |
| Comprehensibility optional: name 評価 in 判断's opening | **Optional, declined** | Titles and examples already separate a conclusion from rating work, and 評判 contrasts 評価. |
| Comprehensibility optional: 検査 title «осмотр; анализ» narrower than its body | **Optional, declined** | The body lists проверка, досмотр and обследование, and 診察 already guards 検査. |
| Comprehensibility optional: 記念 «ознаменование»; 触れる voice terminology | **Optional, unchanged** | The examples make both senses plain. |
| Consistency optional: 判断–決定 and 検査–調べる unguarded | **Optional, unchanged** | Different titles and no EN pair. |
| Consistency optional: drop 診察→受付 | **Optional, kept** | A harmless conservative guard. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN** after fixes.
- Quiz safety: **CLEAN** for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
