# Batch 205 — independent review 001

## Snapshot and scope

- Reviewed snapshot: candidate tree `e26a8e9466a82a925d4a0c429efe08a701323ae3`, staged in a scratch worktree, not a commit.
  - Batches 197–204 had been reviewed and their fixes rechecked, but their signed commits could not yet be made because the
    signing key's passphrase cache had expired. Rather than wait, Batch 205 was authored on top of the reviewed Batch 204 tree
    `d9a9765a5addaf58e31fefd85fb97eed1d242b99`, at detached HEAD `5dd9a78` in a separate worktree.
  - The candidate differs from `d9a9765` by 53 paths: 30 new word cards, 22 navigation-only files (26 restored links) and
    `manifest.json`.
  - Reviewers were told to read the staged tree and not to rely on HEAD. No unsigned commit was made.
- After Batch 204 was published as `56a952485c35b887a09d0828a05e8e06ca72226a`, branch `full-ru-205-words-44` was cut from that merge. Its parent commit
  `940cd4ae62bc1c7992c9d4a13009c9de79696b99` adds only the Batch 204 publication record. The final reviewed content tree was copied there and committed signed as
  `18386f84bbdd74074d7667d508602bda5900e05b`, together with the intake. `git diff 84dc60f 18386f8 -- words kanji strokes articles manifest.json` is empty;
  see the recheck record for the revised tree `84dc60f`.
- Published baseline recorded in the intake: `56a952485c35b887a09d0828a05e8e06ca72226a` (Batch 204 merge).
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers against their EN originals.
  - Correctness also read every changed passage in the 22 navigation-only files. It read the RU cards 生きる, 種, 盛り, それに,
    たいてい, 一昨日, あさって, 将来, 本当 and 住む in full as comparisons.
  - Consistency read the complete diffs of the 22 navigation-only files and compared each with its base after stripping link
    markup. It checked EN-versus-RU link parity for the new cards, scanned every RU file whose EN counterpart links to a batch
    word, screened all 2,803 RU word titles for equal segments and stems, and checked the manifest hashes.
  - Comprehensibility read the existing RU あさって, 将来, 自分, 自身, 服, 書物, 生活, 覚える, 経済, 途中, 最後, 時間 and 月曜日
    for the stated contrasts, and spot-checked the navigation restorations as link wraps.
  - The intake was generated after review from the same paths. Its payload hashes are checked by the final validation receipt.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that the worktree's index tree was
  still `e26a8e9`, that the working tree equalled the index and that nothing was untracked or ignored. No fix was applied until all
  three reports were complete.
- The review assignment allowed running validators on the working tree and named the report as the only file a reviewer writes.
  Unlike the Batch 204 launch messages, the correctness and consistency launch messages did not also name
  `tools/build_manifest.py`. The consistency reviewer ran it; its report states that this rewrote `manifest.json`
  byte-identically, and the coordinator's check after that review found the index tree still `e26a8e9`, the working tree equal
  to the index and nothing untracked or ignored. The comprehensibility launch message then forbade `tools/build_manifest.py` and
  any other generator. The correctness reviewer ran no generator or validator; the consistency reviewer also ran
  `tools/validate.py` (0 errors) and its own title screens; the comprehensibility reviewer used the shared title screen. All
  screen hits were treated as leads.
- Full blind reports:
  - `205-words-batch-44-review-correctness-001.md`
  - `205-words-batch-44-review-consistency-001.md`
  - `205-words-batch-44-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt or one another's reports.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN** for all 30 cards; scoped coverage **NEEDS FIX** (札 only). The other 29 cards were CLEAN on both
facets.

- C1 (minor, high confidence), `札.md:38-41`: the frozen EN card ends its source correction with "This correction does not
  establish what the historical compiler intended." RU ended the paragraph with a generic conditional, «Если в списке слов рядом с
  чтением さつ стоят такие переводы, они относятся к слову ふだ…», and omitted that qualification, so a reader loses the
  distinction between correcting a mixed reading/gloss pairing and establishing what the compiler meant. The banknote/ふだ
  distinction itself is correct. Evidence: the complete frozen EN 札 card; the Jisho API entries for 札, with a separate さつ
  banknote entry and a ふだ ticket/tag/card/talisman entry. Remedy (the reviewer's text): a three-sentence replacement ending «Это
  исправление не устанавливает, что имел в виду составитель исходного списка.»

Optional: 有効 «действителен по завтрашний день включительно», making EN's "through tomorrow" explicit (Gramota answer 250448
permits inclusive «до» with validity dates and recommends «включительно» for clarity); a register note on 明後日, whose absence is
inherited from EN and whose contrast the RU あさって card already gives.

Other checks:

- Main Japanese example sentences and kana strings match EN in all 30 cards. Front matter keeps every EN field and exclusion. No
  dropped source link has an existing RU target; labels of absent targets remain as plain text.
- The reviewer inspected the Jisho API entries for every headword. Among them: the 替える spellings carry "usu." tendencies, not
  restrictions; 暮らす is an intransitive godan verb; 明後日's figurative sense is restricted to あさって; 元 has separate
  "former" and "origin" identities; 最中 さいちゅう/さなか is separate from the もなか sweet. It also inspected 種, 盛り, 生きる,
  それに, たいてい and 一昨日 for the Russian-added comparisons, the full Jisho 普段 page (ateji note and the earlier 不断 spelling)
  and the 精選版 日本国語大辞典 みょうごにち heading on Kotobank.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (暮らす, 暗記); scoped cross-file integration **CLEAN**.

- Front matter and section structure match EN. Every EN link target is either linked in RU or absent from RU, and no RU file
  whose EN counterpart links to a batch word leaves that link unrestored. All 22 navigation files are identical to their base once
  link markup is stripped. `tools/validate.py` reports 0 errors.
- Every segment or stem hit from screening all 2,803 RU titles is guarded or judged not defensible.

Findings:

- F1 (minor, medium confidence), `暮らす.md:9`: the verb 暮らす «вести жизнь; жить (где, как, с кем)» had no direct pair with
  生活 «повседневная жизнь; быт», although the 生活 card teaches 生活する «жить; вести свою жизнь» and JMdict records 生活する
  "to live". The repository already guards 暮らし–生活 (EN) and 生きる→生活. Remedy: `quiz_exclusions: [住む, 生きる, 生活]`.
- F2 (minor, conservative-to-required, medium confidence), `暗記.md:9-10`: 暗記 «заучивание наизусть», taught as 暗記する
  «выучить наизусть», had no pair with 覚える «запоминать; помнить», whose JMdict sense 1 is "to remember; to memorize"; 記憶
  already guards 覚える. Remedy: `quiz_exclusions: [覚える]`.

Optional: conservative guards 書類–紙 (the stems of «бумаги» and «бумага») and 服装–格好 (the 格好 card teaches «как человек
одет»). The reviewer judged no guard necessary for 書斎/研究室, 元/基/素, 時刻/何時 or 暮らす/過ごす.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (札, 替える); the other 28 cards **CLEAN**. Scoped coverage **CLEAN** for all 30.

- C1 (minor, high confidence), `札.md:40-41`: «Если в списке слов рядом с чтением さつ стоят такие переводы…» is leftover
  source-note language. A beginner has no such list on the card and may think the app shows ticket or tag glosses for さつ.
  Evidence: the Jisho displays of JMdict 1298960 (さつ: banknote) and 1298970 (ふだ: ticket/token, label/tag, card, talisman).
  Remedy: delete the sentence, or replace it with «Если словарь при чтении さつ даёт переводы «билет» или «бирка», это значения
  другого слова, ふだ.»
- C2 (minor, high confidence), `替える.md:48`: «Сравнение 替える с 換える, 代える и 変える разбирается в отдельной статье о
  глаголах かえる» points to an article that is not in the RU tree. The card already states the を/に contrast and the
  換える/代える/変える tendencies, so this is a dead pointer, not a missing rule. Remedy: delete the sentence.

Optional: 旧 «Это прежнее здание школы» instead of «старое», which the card assigns to 古い; 更に «стал ещё сильнее» would match
the change of state more tightly than «пошёл ещё сильнее»; 景気's title «экономическая конъюнктура» is jargon, although the body
immediately pairs it with «дела идут хорошо»; 本人 does not name 自身, and 書類 does not name 書物. The reviewer established that
明後日 omitting あさって's register note is not a defect.

Correctness C1 and comprehensibility C1 were found independently and concern the same 札 sentence from different facets.

## Exclusion classification: author and consistency reviewer

The author added 11 direct, one-sided exclusion pairs beyond EN on 10 new cards, and review F1/F2 and two adopted optional items
added four more. All 18 EN exclusion entries (11 lists) are retained. The author report and the blind consistency reviewer
classified the pairs independently. The differences are preserved here rather than resolved by vote. Classification does not
change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `木曜`→`木曜日` | required | required |
| `月曜`→`月曜日` | required | required |
| `日曜`→`日曜日` | required | required |
| `明後日`→`あさって` | required | required |
| `最中`→`盛り` | conservative (segment-equal; could be argued required) | required |
| `暮らす`→`生きる` | conservative (segment-equal; could be argued required) | required |
| `元`→`種` | conservative (segment-equal; could be argued required) | required |
| `本物`→`本当` | conservative | conservative |
| `本人`→`自身` | conservative | conservative |
| `本人`→`自分` | conservative | conservative |
| `更に`→`それに` | conservative | conservative |
| `暮らす`→`生活` | stem-only overlap, declined | missing guard, finding F1 (medium confidence) |
| `暗記`→`覚える` | not considered | missing guard, finding F2 (conservative-to-required) |
| `書類`→`紙` | stem-only overlap, declined (plain-text contrast in the body) | optional conservative guard |
| `服装`→`格好` | not considered | optional conservative guard |

Neither found a kept pair unjustified. The last four pairs were added after review.

Reconciliation, the coordinator's dispositions and the final verdicts are in `205-words-batch-44-recheck-001.md`.