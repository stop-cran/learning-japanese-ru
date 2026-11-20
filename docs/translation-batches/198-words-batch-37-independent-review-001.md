# Batch 198 — independent review 001

## Snapshot and scope

- Reviewed snapshot: candidate tree `c82e94b30d2c72c36fb56406ba2aaaf1f54e0002`, staged in a scratch worktree, not a commit.
  - Batch 197 had been reviewed and its fixes rechecked, but its signed commits could not yet be made because the signing key's
    passphrase cache had expired. Rather than wait, Batch 198 was authored on top of the reviewed Batch 197 tree
    `ea3a478bcb5583d6b7357820d35dcfb51adc76b7`, at detached HEAD `5dd9a78` in a separate worktree.
  - The candidate differs from `ea3a478` by 44 paths: 30 new word cards, 13 navigation-only files (15 restored links) and
    `manifest.json`.
  - Reviewers were told to read the staged tree and not to rely on HEAD. No unsigned commit was made.
- After Batch 197 was published as `6575e4cfc9a3fe7f1cbc2e87c1bd1fd129e618a0`, branch `full-ru-198-words-37` was cut from that merge. Its parent commit
  `df947ea5fa50ab3a5ab1a726dce8fa5ac698a5e6` adds only the Batch 197 publication record. The final reviewed content tree was copied there and committed signed as
  `174d0cca377e42a87ca99e3bdd9d24274a1d9278`, together with the intake. `git diff 80c7336 174d0cc -- words kanji strokes articles manifest.json` is empty;
  see the recheck record for the revised tree `80c7336`.
- Published baseline recorded in the intake: `6575e4cfc9a3fe7f1cbc2e87c1bd1fd129e618a0` (Batch 197 merge).
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness also read every baseline-card change: the 13 navigation-only files.
  - Consistency read the 13 navigation-only diffs line by line and covered `manifest.json`.
  - Comprehensibility read the new cards and the named comparison cards. It scanned the link-only edits but gave them no
    separate verdict.
  - The intake was generated after review from the same paths. Its payload hashes are checked by the final validation receipt.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that the worktree's index tree
  was still `c82e94b`, that the working tree equalled the index and that nothing was untracked.
- Full blind reports:
  - `198-words-batch-37-review-correctness-001.md`
  - `198-words-batch-37-review-consistency-001.md`
  - `198-words-batch-37-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's reports.
  The consistency reviewer ran its own title screen of the new titles against the RU word titles and treated its hits as leads.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN** and scoped coverage **CLEAN** for all 30 cards and the navigation-only changes. No findings.

- The reviewer compared every example and translation with frozen EN, including polarity, event stage, transitivity and
  participant roles. All 60 Japanese example sentences are present verbatim.
- It retrieved the Jisho/JMdict entries for all 30 headwords and the separate entries 神経を使う and 礼儀正しい. It confirmed, for
  example, that 積もる's taught sense is intransitive, that 移動 takes both transitive and intransitive する, that 移す's illness
  sense is usually written in kana, and that 種（たね） is a separate entry from しゅ.
- For 穀物 it read the 世界大百科事典 and 日本大百科全書 entries on kotobank. An earlier URL redirected to an unrelated entry and
  was rejected as evidence.
- Removed source links all point to cards absent from RU; their Japanese labels remain as plain text.
- It ran the validator (0 errors) and matched the LF-normalised SHA-256 of all 43 changed content files to `manifest.json`.
- Optional: `穀物.md:38` could stay closer to EN's non-exclusive wording instead of defining 穀物 as grain «как сырьё».

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (F1); scoped cross-file integration **CLEAN**.

- F1 (minor, medium confidence): `移動.md:6`. 移動 teaches the action sense (この机を窓のそばに移動しました, «передвинул стол»),
  and 動かす «сдвигать; приводить в движение» is taught with the near-identical 椅子を…動かしてください. Neither card guards the
  other, and EN has no pair, so «передвинуть/сдвинуть» is defensible for both. Remedy: add 動かす to 移動's `quiz_exclusions`.
- Front matter other than title and `quiz_exclusions` equals EN for all 30 cards. Every EN link is either present or points to a
  card absent from RU and left as plain text. No new card adds a Russian-only link.
- The 13 navigation files change only link brackets and hrefs. All 4,054 manifest entries match recomputed hashes, and nothing
  unrelated is in the diff. The validator reported 0 errors.
- Optional: drop 祝い→お祭り, which the reviewer judged unjustified but harmless. If the owner prefers fewer guards, 祭→お祝い/祝い
  and 祝い→お土産 could also go. 動かす–動く could be revisited only if a quiz shows ambiguity; it is not required now.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (穀物, 積む, 積極的, 神経, 祭); scoped coverage **CLEAN**; the other 25 cards **CLEAN**.

All five findings are minor, with high confidence:

- C1, `穀物.md:20`: the Japanese example lists two items, 米や麦, but the translation listed three crops.
- C2, `積む.md:20`: «одна на другую» is a two-item idiom used for three boxes.
- C3, `積極的.md:39-40`: the warning against «положительный результат анализа или положительное число» only makes sense through
  English "positive".
- C4, `神経.md:26-28`: «писание бога» is rejected without telling the learner why a scripture reading would arise.
- C5, `祭.md:39-40`: the note about «разговорные интернет-значения словарной статьи» is author-facing.

Optional: `空き.md:21` «свободное время» narrows an unspecified availability; `積もる.md:19` «На дороге лежит снег» would match the
remaining-layer note more tightly; one-line 礼儀–行儀 and 祝う–喜ぶ contrasts would help but are not missing from EN.

No finding established a missing requested card, an incorrect Japanese example or a missing necessary prerequisite.

## Exclusion classification: author and consistency reviewer

The author added 26 direct, one-sided exclusion pairs beyond EN on 15 new cards. All 16 EN exclusion entries (12 lists) are
retained. The author report and the blind consistency reviewer classified the pairs independently. The differences are preserved
here rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `祭`→`お祭り` | required | conservative |
| `積む`→`折る` | required | conservative |
| `種`→`話題` | conservative | required |
| `確認`→`調べる` | conservative | required |
| `祝い`→`お祭り` | conservative | unjustified, nonblocking |

Both classify `禁煙`→`禁止`, `移動`→`移す`, `祝う`→`お祝い`, `祝う`→`祝い`, `祝い`→`お祝い`, `祝い`→`プレゼント`, `祝い`→`贈り物`,
`確認`→`チェック` and `確認`→`テスト` as required, and `立ち上がる`→`上がる`, `空き`→`席`, `穀物`→`米`, `稼ぐ`→`働く`, `根`→`原因`,
`移動`→`移る`, `祭`→`お祝い`, `祭`→`祝い`, `祝い`→`お土産`, `祝い`→`記念`, `感謝`→`恩` and `礼`→`恩` as conservative. No kept pair
guards a contrast that a card teaches as an antonym. The `移動`→`動かす` guard (F1) and the `移動`→`動く` coordinator extension added
after review bring the RU-added total to 28; they are recorded in the recheck record.

Reconciliation, the coordinator's dispositions and the final verdicts are in `198-words-batch-37-recheck-001.md`.
