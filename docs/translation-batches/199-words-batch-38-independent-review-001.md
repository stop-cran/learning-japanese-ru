# Batch 199 — independent review 001

## Snapshot and scope

- Reviewed snapshot: candidate tree `b99047ab07da1b5364690335e4fede1db79dca76`, staged in a scratch worktree, not a commit.
  - Batches 197 and 198 had been reviewed and their fixes rechecked, but their signed commits could not yet be made because the
    signing key's passphrase cache had expired. Rather than wait, Batch 199 was authored on top of the reviewed Batch 198 tree
    `80c7336de2a89655b543c35641a339e44f5a0833`, at detached HEAD `5dd9a78` in a separate worktree.
  - The candidate differs from `80c7336` by 44 paths: 30 new word cards, 13 navigation-only files (16 restored links) and
    `manifest.json`.
  - Reviewers were told to read the staged tree and not to rely on HEAD. No unsigned commit was made.
- After Batch 198 was published as `c3f3102bba7a2ad57f2f68761bd71ee9b696913d`, branch `full-ru-199-words-38` was cut from that merge. Its parent commit
  `d6662222c08eea45e5507167bb146fe352d002d4` adds only the Batch 198 publication record. The final reviewed content tree was copied there and committed signed as
  `4ff5f6a3d68716fff63534d4ee93322ec59ca182`, together with the intake. `git diff 841bc8c 4ff5f6a -- words kanji strokes articles manifest.json` is empty;
  see the recheck record for the revised tree `841bc8c`.
- Published baseline recorded in the intake: `c3f3102bba7a2ad57f2f68761bd71ee9b696913d` (Batch 198 merge).
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness read every new card and its EN original completely, and inspected the changed comparison passages in the
    13 navigation-only files.
  - Consistency read the 13 navigation-only diffs line by line and covered `manifest.json`.
  - Comprehensibility read the new cards, the link-only edits and the named comparison cards. It gave the link-only edits no
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
  was still `b99047a`, that the working tree equalled the index and that nothing was untracked.
- Full blind reports:
  - `199-words-batch-38-review-correctness-001.md`
  - `199-words-batch-38-review-consistency-001.md`
  - `199-words-batch-38-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's reports.
  The consistency reviewer ran its own title-segment screen of the new titles against all RU word titles and treated its hits as leads.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (盛り, 真似, 指導); scoped coverage **CLEAN** for all 30 cards.

All three findings are minor:

- C1 (high confidence), `盛り.md:19`: 桜は盛りを過ぎました was translated «Сакура уже отцвела», which says flowering has ended.
  The Japanese, and EN's "past their peak", say only that the peak has passed. Remedy: «Пик цветения сакуры уже прошёл».
- C2 (high confidence for the overlap), `真似.md:37-38`: the Russian-added contrast confined 写す and コピー to copying text, files
  or images, and 真似 to imitating actions, voice or manner. JMdict 写す sense 3 is "to imitate; to model after", and コピー covers
  imitation and a song cover. Stated without a qualifier, the contrast teaches an artificial object-based boundary. The reviewer
  proposed qualified wording.
- C3 (high confidence), `指導.md:39-40`: the Russian-added contrast called 教育 «вся система обучения и воспитания». 教育 can also be
  the training of particular people (デジタル大辞泉: 新入社員を教育する), and the existing RU 教育 card teaches that use. The
  reviewer proposed a broader-concept wording.

Other checks:

- The reviewer inspected the Jisho/JMdict entries for all 30 headwords, keeping 直に（じかに）apart from 直に（じきに）and
  盛り（さかり）apart from 盛り（もり）. It also read the comparison entries for 堅い, 違いない, 調べる, 案内, 重大, 大変, 写す, コピー,
  教育 and 管理.
- Front matter other than the title and the appended exclusions matches EN, and no EN exclusion was removed. All 60 Japanese
  example sentences are present verbatim.
- Removed source links point to nine cards absent from RU. Their Japanese labels remain as plain text.
- It checked the Russian title words обозревать, преемство, несостоятельный, тотчас, безотлагательно and лично against Gramota
  dictionary entries and found no title defect. The じか reading-history line is supported by デジタル大辞泉's 「じき」の音変化.
- The reviewer did not run the validator and makes no structural-validation claim.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **CLEAN**; scoped cross-file integration **CLEAN**. No findings.

- The validator reported 0 errors. `build_manifest` was imported without writing, and its output equals `manifest.json` exactly.
- The changed-file list is exactly the 30 new cards, the 13 navigation files and the manifest.
- The reviewer's own link audit over all 43 files found no broken link and no Russian-only link. Every EN link is either restored or
  points to an absent card: the kanji 硬, 貨, 砂, 炭, 県, 接 and 銅, and the words 仲間, スタート, 到着, 意志 and 重ねる. A scan of all RU
  and EN cards found no EN link to a batch word left unrestored. `link_parity.py` passed for 43 files.
- No EN exclusion is lost on either side. No new title segment exactly equals another card's title segment without a direct guard.
- Optional: 登山→登る is the weakest extra guard, to keep or drop at the owner's discretion. The stem-level leads 直に/自身,
  相手/向こう, 真剣/集中 and 情報/通信 need no guard. 指導→管理 could be added conservatively, but its necessity is not established.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (ゴール, 知識, 盛り); scoped coverage **NEEDS FIX** only for 盛り; the other cards **CLEAN**.

All three findings are minor, with high confidence:

- C1, `ゴール.md:27`: «соответствует английскому goal» leaves an English word in learner text. The reviewer proposed
  «Это заимствование из английского, записанное катаканой.»
- C2, `知識.md:19`: the card's note says 増やす is the action and 知識 is what the learner wants to пополнить, but the translation
  «Я хочу больше узнать об истории Японии» turns the noun 知識 into the verb «узнать». Remedy: «Я хочу пополнить свои знания об
  истории Японии.»
- C3, `盛り.md:19`: the same «отцвела» issue as correctness C1, found independently.

Optional:

- `直に.md:38`: drop the inline «словарная запись 1430700», which the footer already cites.
- `直に.md:19`: «расспросил» is a little stronger than 話を聞く.
- `指導.md:21`: «наставляет» would match the card's gloss.
- `眺める.md:3`: the title «подолгу смотреть» states a duration that the body treats as a tendency.

The reviewer checked the flagged clusters and found them taught: 確実/確か, 確かめる/確認/調べる, 情報/知識/知らせ/案内, じかに/じきに,
ゴール/目標/目的/ため, 指導/コーチ/監督, さかり/もり, 登山/登る and 発車/出発.

## Exclusion classification: author and consistency reviewer

The author added 21 direct, one-sided exclusion pairs beyond EN on 14 new cards. All 23 EN exclusion entries (15 lists) are
retained. The author report and the blind consistency reviewer classified the pairs independently. The differences are preserved
here rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `真っ赤`→`赤い` | required | conservative-to-required |
| `県`→`都` | required | conservative |
| `指導`→`教育` | required | conservative |
| `真っ赤`→`赤` | conservative | conservative-to-required |
| `直接`→`まっすぐ` | conservative | required-leaning |
| `監督`→`管理` | conservative | required |

Both classify `確実`→`確か`, `確実`→`堅い`, `確かめる`→`調べる`, `情報`→`案内` and `目標`→`ため` as required, and `確実`→`違いない`,
`確実`→`きっと`, `知らせ`→`知らせる`, `真剣`→`重大`, `真剣`→`大変`, `真似`→`写す`, `真似`→`コピー`, `ゴール`→`ため`, `指導`→`教える` and
`登山`→`登る` as conservative. The reviewer called `登山`→`登る` the weakest of the set and classified none as unjustified. No kept
pair guards a contrast that a card teaches as an antonym.

Reconciliation, the coordinator's dispositions and the final verdicts are in `199-words-batch-38-recheck-001.md`.
