# Batch 197 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `5dd9a78f4e6d2f806be09953326bf77cb8e77c47` | `aa153ae4edbd312c5336da1a9ad2a142f9433e60` | Initial review snapshot: the signed candidate, pushed before review. |
| `4d7eed03bf8a6596149dd821f99e916b7aec9e08` | `ea3a478bcb5583d6b7357820d35dcfb51adc76b7` | Final candidate: review fixes plus the intake refresh. |

The final candidate changes five word files:
- `結果`: line 28 restores the frozen EN reading note «Чтение — ケッカ, с маленьким っ.». Line 20 translates
  調べた結果、原因が分かりました as «Проверив, мы выяснили причину.», matching the card's «в результате проверки» gloss.
- `節約`: line 37 gives 手間（てま）を省く. `quiz_exclusions` becomes `[省く, 貯金]`: 貯金 «сбережения; откладывание денег» is a
  conservative guard, because «экономия» and «сбережения» are close in Russian. The body contrast is unchanged.
- `組合`: line 18 gives **組合の会員**（くみあいのかいいん）, parallel to **組合に入る**（くみあいにはいる）.
- `籠`: line 20 translates 鳥がかごから出ました as «Птица вышла из клетки.», as EN "came out", without adding flight.
- `経由`: line 36 says 途中 means the thing is «находится в пути или в процессе дела», closer to EN "partway through a route or
  activity" than «на полпути».
- The manifest and intake are regenerated. `contentVersion` is `dbb402e02c496af4`, and only the five changed word hashes differ.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks used the same model variants and facets as review 001, run as fresh agents rather than the original agent sessions:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

Rechecks ran serially.
Each reviewer received only:
- its facet's original blind report;
- the coordinator's dispositions of its findings;
- the revised snapshot;
- the actual diff from `5dd9a78` to the revised tree.

The commit-signing key's passphrase cache expired before the fixes could be committed. The revised snapshot was therefore
staged and handed to the reviewers as tree `ea3a478`, with the instruction to read that tree rather than HEAD. A first signing
attempt, started before the intake refresh, was cancelled; it created no commit. No unsigned commit was made. The final
candidate `4d7eed0` was committed signed after the rechecks and wraps exactly the reviewed tree `ea3a478`.

HEAD, the index and the working tree were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `ea3a478` | C197-2 resolved: `結果.md:28` restores frozen EN's ケッカ; it was never a phonological error. C197-1 stays withdrawn. The 経由 optional is resolved: the reviewer read frozen EN and the JMdict-backed 途中 entry (senses 1 "on the way; en route" and 2 "in the middle of; midway; halfway") and found «в пути или в процессе дела» faithful without implying an exact halfway point. The 結局 comma optional is declined; the original report's Большой универсальный словарь entry supports the decisive-argument use. Regression check of every changed passage: «Проверив» renders 調べた結果 with the resulting discovery kept in the surrounding prose; てま and くみあいのかいいん are correct; «вышла» matches 出ました; the 貯金 guard asserts no synonymy and leaves the savings contrast at lines 33–34 intact. Correctness and scoped coverage are **CLEAN**. |
| Consistency | tree `ea3a478` | No original findings. O2 is resolved: `節約` declares `[省く, 貯金]` and `words/貯金.md` exists. O1 and O3 are declined and remain optional; O4 was routed to correctness, which found no defect. The changes add readings and reword translations only; no link was added or changed, and only 節約's front matter changed. The reviewer recomputed the five changed SHA-256 hashes against `manifest.json` and ran the validator (0 errors). Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `ea3a478` | Findings 1 and 2 resolved: 手間（てま）を省く and **組合の会員**（くみあいのかいいん） are now readable. The 結果 and 籠 optionals are resolved. The 管, 節, 経由-title, 経つ-title, "soon"/position-cluster and 範囲–幅 optionals are withdrawn as unchanged and not required. Regression check: ケッカ is clear beside the title's けっか and matches EN and the katakana used for component readings elsewhere (節約: セツ + ヤク); «в пути или в процессе дела» keeps the contrast with a route named «через». No new defect. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C197-2: 結果 changed EN's ケッカ to けっか | **Resolved** | `結果.md:28`. A source-preservation fix; the pronunciation was never wrong. |
| Correctness C197-1 (provisional): «на полпути» in 経由 | **Withdrawn** | Withdrawn by the reviewer in the original report: JMdict 途中 sense 2 lists "midway; halfway", and «на полпути» can be figurative. |
| Correctness optional: 経由 «в пути или в процессе дела» | **Optional, adopted** | `経由.md:36`. Confirmed on recheck against frozen EN and JMdict 途中. |
| Correctness optional: drop the comma in 結局 «В конце концов, он же ребёнок» | **Optional, declined** | Russian punctuation choice, not a Japanese meaning defect; the reviewer requested no change. |
| Consistency O1: 組合 vs 団体/組織 | **Optional, declined** | Low confidence; 組合 already guards 会, and 団体 is declared on 会. |
| Consistency O2: 節約 vs 貯金 | **Optional, adopted as a guard** | `節約.md:9`. A conservative one-sided pair, applied symmetrically by the app. RU-added exclusions now total 24. |
| Consistency O3: 今に vs 先 | **Optional, declined** | The reviewer did not recommend it. |
| Consistency O4: accuracy of RU-added comparison sentences | **Routed to correctness** | The correctness review read every complete new card, including these sentences, and checked entries for compared words such as 通過, 承知, 以下, 額, 省く, 曲, 特徴 and 手; it found no defect; the sentences are plain text, so link parity holds. |
| Comprehensibility Finding 1: 手間を省く without a reading | **Resolved** | `節約.md:37`. |
| Comprehensibility Finding 2: **組合の会員** without a reading | **Resolved** | `組合.md:18`. EN has the same omission; RU adds the reading. |
| Comprehensibility optional: 結果 «Разобравшись» vs the «в результате проверки» gloss | **Resolved** | `結果.md:20`. |
| Comprehensibility optional: 籠 «вылетела» adds flight | **Resolved** | `籠.md:20`. |
| Comprehensibility optional: 管 residual meta wording | **Optional, unchanged** | It renders the frozen EN statement that the dictionary entry below supports くだ, and does not misstate the reading. |
| Comprehensibility optionals: 節 不思議な節, the 経由 and 経つ titles, the "soon" and position clusters, 範囲 vs 幅 | **Optional, unchanged** | EN parity; withdrawn on recheck as not required. 範囲 already guards 幅. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN** after fixes.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN**, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
