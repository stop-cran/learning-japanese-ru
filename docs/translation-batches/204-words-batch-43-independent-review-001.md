# Batch 204 — independent review 001

## Snapshot and scope

- Reviewed snapshot: candidate tree `c4b6d94520f4755df78422eb4d06805db0b988a1`, staged in a scratch worktree, not a commit.
  - Batches 197–203 had been reviewed and their fixes rechecked, but their signed commits could not yet be made because the
    signing key's passphrase cache had expired. Rather than wait, Batch 204 was authored on top of the reviewed Batch 203 tree
    `20d023225e820a0a3b1eb7e965807dc7d5820fd3`, at detached HEAD `5dd9a78` in a separate worktree.
  - The candidate differs from `20d0232` by 47 paths: 30 new word cards, 16 navigation-only files (24 restored links) and
    `manifest.json`.
  - Reviewers were told to read the staged tree and not to rely on HEAD. No unsigned commit was made.
- After Batch 203 was published as `00821e86400b1fbec9ac611795469d98a77cbdce`, branch `full-ru-204-words-43` was cut from that merge. Its parent commit
  `3110d47a616fb5e6ed6cfd6df383e9a43533d2af` adds only the Batch 203 publication record. The final reviewed content tree was copied there and committed signed as
  `b0e6a9334e0ba31036280983f37ca21f339071d1`, together with the intake. `git diff d9a9765 b0e6a93 -- words kanji strokes articles manifest.json` is empty;
  see the recheck record for the revised tree `d9a9765`.
- Published baseline recorded in the intake: `00821e86400b1fbec9ac611795469d98a77cbdce` (Batch 203 merge).
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers against their EN originals.
  - Correctness also inspected every changed existing runtime passage. It read the RU cards 昼御飯, 昼, 正しい, 本当, 迎える, 喜ぶ,
    休む, 原因, 途端, 手段, 組む, 論じる, 食料品 and 松竹梅 in full as comparisons.
  - Consistency read the complete diffs of the 16 navigation-only files with `git diff -U0`. It scripted front-matter, heading,
    link-parity, broken-target and exclusion comparisons with EN, scanned every EN file that links to a new word, screened all
    2,773 RU titles for equal segments and checked the manifest hashes.
  - Comprehensibility read the existing RU 迎える, 喜ぶ, 考慮, 見当, 留守, 気分, 正しい, 昼, 昼御飯, 梅 and 松竹梅 for the stated
    contrasts and reviewed the navigation restorations from their diffs.
  - The intake was generated after review from the same paths. Its payload hashes are checked by the final validation receipt.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that the worktree's index tree was
  still `c4b6d94`, that the working tree equalled the index and that nothing was untracked or ignored. No fix was applied until all
  three reports were complete. The review prompts forbade running `tools/build_manifest.py`; the correctness and consistency
  reports state that no generator was run, and the tree checks after every review found no change.
- Full blind reports:
  - `204-words-batch-43-review-correctness-001.md`
  - `204-words-batch-43-review-consistency-001.md`
  - `204-words-batch-43-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt or one another's reports. The consistency reviewer ran its
  own title screens, and the comprehensibility reviewer ran the shared title screen; both treated hits as leads.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (次第 only); scoped coverage **CLEAN**. The other 29 cards were CLEAN on both facets.

- C204-1 (minor, high confidence), `次第.md:31`: the Russian-added comparison said that た-форма + 途端に «связывает уже случившееся
  событие с тем, что произошло в тот же миг». Contrasted with 次第's following action, this presents actual past occurrence as
  the distinguishing rule. The た attachment marks the preceding event's completion relative to the next one; the whole situation
  need not have happened already. Evidence: the JMdict-backed Jisho entry 途端 ("just as; as soon as; at the moment that", no
  past-only restriction); Bunpro たとたんに, whose example 青になった途端に飛び出すのは危ないよ is a general warning; the existing RU
  `途端.md`. Remedy (the reviewer's text): «оно подчёркивает момент, когда вслед за одним событием сразу происходит другое, часто
  неожиданное», plus a construction source.

Optional: append the comparison-entry IDs for Russian-only lexical comparisons (原因 1261190, 手段 1328110, 組む 1397590, 論じる
1561620, 食料品 1358680, 松竹梅 1349920).

Other checks:

- Main Japanese example sentences and kana strings match EN in all 30 cards, and a whole-body Japanese-token comparison found no
  omitted source token. Front matter keeps every EN field and exclusion; fourteen cards add exclusions.
- All EN links are kept except five whose RU targets do not exist (`kanji/梅.md`, `kanji/栄.md`, `kanji/板.md`, `kanji/松.md`,
  `words/以来.md`); their labels and explanations remain.
- The reviewer inspected JMdict-backed Jisho entries for all 30 headwords and the comparison words, and Gramota entries for
  «мотор», «акция» and «питание», which support the Russian localization notes in エンジン, 株 and 栄養. `tools\validate.py`
  reported 0 errors.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (お昼, プラス); scoped cross-file integration **CLEAN**.

- Front matter other than titles and exclusions equals EN in all 30 cards, and section structure matches. Link parity is exact: no
  Russian-only links, and the only EN-only links point to absent RU targets. Every navigation hunk changes only link brackets and
  hrefs at EN link positions, and a full EN→RU scan found no unrestored link to a new word. Every non-stroke manifest entry hashes
  correctly.
- No new title equals another card's title or title segment without a guard.

Findings:

- F1 (minor, medium confidence), `お昼.md`: the card teaches that お昼 «может обозначать и дневное время», as EN does and as JMdict's
  "daytime" sense supports, while 昼間 is titled «дневное время». Only 昼 was guarded. Remedy: `quiz_exclusions: [昼食, 昼御飯, 昼,
  昼間]`.
- F2 (minor, low–medium confidence), `プラス.md`: the card teaches AにBをプラスする «прибавить B к A» and names 足す «прибавлять;
  добавлять» as the arithmetic comparison; neither card declares the pair. Remedy (conservative): `quiz_exclusions: [足す]`.

Optional: guards 正–本当, 来–次 and 横断–越える (all judged low risk); 松 and 桜 call 梅 «японская слива», while the RU 梅 card is
titled «умэ; японский абрикос». Future obligation, not a defect: EN exclusions on not-yet-translated cards (モーター, ランチ, 交差,
公式, 構造, 以来, 文脈, 踏切) target these words and must be carried when those cards are translated.

The reviewer noted that `strokes/*.json` manifest hashes did not match the checked-out bytes in untouched files, apparently
because of CRLF conversion on checkout, and left them out of scope. The diff changes no stroke file.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (歓迎 only); the other 29 cards **CLEAN**. Scoped coverage **CLEAN**.

- C1 (minor; high confidence for the overlap, medium–high that a reader is misled), `歓迎.md:16,18,29`: the people-example
  «тепло встретили» and the gloss «приветствовать» use the same Russian as 迎える «встречать; приветствовать», so a beginner can
  read 歓迎する as going to meet someone; only the opinions example was separated. Evidence: JMdict 1212960 sense 1 (welcome; warm
  reception) and 1253190 sense 1 (go out to meet; receive; welcome); the RU 迎える card. Remedy: gloss «радушно принимать кого-то
  или что-то; благосклонно относиться к чему-то», translation «Мы все радушно приняли нового учителя.», and a 迎える contrast after
  the 招待 sentence.

Optional: 松's «комплекс «Мацу»» transliteration; 横断 does not restate 横切る's verb class; 検討 does not name 考慮 or 見当; 欠席
does not name 留守; 栄養 «недоедать», 構成 «структуру», 機嫌 «перестала сердиться» and 事情 «отгул» are slightly narrower or broader
than their contexts. The reviewer established none of these as a defect. In its limits it found no unadapted English-dependent
remark: "formal", "plus", "regular customer", "reception/front desk", "humor/jokes", "stock", "organ", "composition/essay" and
"next" were replaced with Russian contrasts or dropped where Russian has no matching ambiguity.

## Exclusion classification: author and consistency reviewer

The author added 17 direct, one-sided exclusion pairs beyond EN on 14 new cards, and review F1/F2 added two more. All 28 EN
exclusion entries (14 lists) are retained. The author report and the blind consistency reviewer classified the pairs
independently. The differences are preserved here rather than resolved by vote. Classification does not change runtime behaviour,
because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `昼食`→`昼` | required | required |
| `事情`→`原因` | required | required |
| `次第`→`途端` | required | required |
| `機嫌`→`気持ち` | required | required |
| `検討`→`論じる` | required | required |
| `板`→`黒板` | required | required |
| `横断`→`渡る` | required | conservative, leaning required |
| `横断`→`横切る` | required | conservative, leaning required |
| `欠席`→`休む` | conservative | required |
| `構成`→`組む` | conservative | required |
| `正`→`正しい` | conservative | conservative, leaning required |
| `次第`→`流れ` | conservative | conservative, leaning required |
| `松`→`松竹梅` | conservative (could be argued required) | conservative, leaning required |
| `歓迎`→`受付` | conservative | conservative |
| `様`→`手段` | conservative | conservative |
| `検討`→`考える` | conservative | conservative |
| `栄養`→`食料品` | conservative | conservative |
| `お昼`→`昼間` | not considered | missing guard, finding F1 (medium confidence) |
| `プラス`→`足す` | not considered | missing guard, finding F2 (low–medium confidence) |

Neither found a kept pair unjustified, and no kept pair guards a contrast that a card teaches as an antonym (the reviewer checked
権利–義務 and 欠席–出席). The `お昼`→`昼間` and `プラス`→`足す` pairs were added after review.

Reconciliation, the coordinator's dispositions and the final verdicts are in `204-words-batch-43-recheck-001.md`.
