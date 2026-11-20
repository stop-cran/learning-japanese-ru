# Batch 207 — independent review 001

## Snapshot and scope

- Reviewed commit: `ec1539c9b30591d1c207da84d96fa008d29c8e80` (tree `612e941814aefda3a8cbcf6072c15b22ba72bae2`), branch
  `full-ru-207-words-46`, parent `22823d6`. The candidate was committed signed directly and pushed before review.
  - The content was authored in a scratch worktree as tree `808eb9e7ae01c1a32fbce47a04312e96e1d82b05`;
    `git diff 808eb9e ec1539c -- words kanji strokes articles manifest.json` is empty.
  - The candidate differs from the published baseline by 30 new word cards, 10 navigation-only files (16 restored links),
    `manifest.json` and the intake. The coordinator made no content change to the author's output before the candidate.
- Published baseline recorded in the intake: `90172013dae7dbf17b39cee17a6ecdf3700e18d8` (Batch 206 merge). Parent `22823d6` adds
  only the Batch 206 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers against their EN originals.
  - Correctness also read the changed navigation hunks in all 10 navigation-only files and the binding RU instruction and
    reference files. It inspected the Jisho/JMdict entries for all 30 written forms (recovering nine HTTP 429 responses with paced
    requests), the Digital Daijisen 提出 entry, and the Kuznetsov (gramota.ru) entries «сдача», «разменять», «представить»,
    «критика» and «операция» behind the Russian-side contrasts. It ran `tools/validate.py` (0 errors).
  - Consistency read all 10 navigation diffs in full, checked every changed manifest hash and the intake's paths and hashes, ran
    `tools/validate.py` (0 errors), and screened every new title and exclusion against all RU word titles with its own
    segment-overlap script.
  - Comprehensibility ran the shared `link_parity.py` on the 30 new cards and the 10 navigation files. It did not reread the
    navigation files as prose and gave no verdict on them.
  - The intake records the same 40 content paths; its payload hashes are checked by the final validation receipt.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD was still `ec1539c` and
  that `git status --porcelain` was empty. The consistency reviewer's validator run left an untracked `tools/__pycache__/`, which
  that reviewer reported; the coordinator removed it and re-verified HEAD and a clean status before the next review. No fix was
  applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator and named the report as the only file a
  reviewer writes. All three reports state that no generator was run.
- Full blind reports:
  - `207-words-batch-46-review-correctness-001.md`
  - `207-words-batch-46-review-consistency-001.md`
  - `207-words-batch-46-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's
  reports.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (提出 only); scoped coverage **NEEDS FIX** (verbatim reading joins in four cards only). No
other factual defect was established in the 30 cards.

- C1 (low, high confidence), `提出.md:15`: «то, что представляют или сдают» names the submitted item, whereas 提出 denotes the act
  of submitting. Evidence: frozen EN `提出.md:15` ("submitting or handing something in"); Jisho/JMdict 提出 sense 1; Digital
  Daijisen 提出 «書類・資料などを…差し出すこと». Remedy: «提出 — существительное со значением «подача, сдача чего-либо».», keeping the
  following 提出する sentence.
- C2 (low, source fidelity only, high confidence), `不利.md:29`, `握手.md:29`, `批評.md:27-28`, `批判.md:29`: the RU cards changed
  EN's hiragana reading joins to katakana despite the verbatim-Japanese requirement. The pronunciations are correct. Remedy:
  restore «ふ + り», «あく + しゅ», «ひ + ひょう» (and the following standalone «ひょう») and «ひ + はん».

Other checks: Japanese example text and kana match EN in all 30 cards; IDs, readings, levels, types, kanji, tags and EN exclusions
are preserved, and the only new exclusion edges, 交換–代わり and 扱う–操作, are supported by the RU target cards and dictionary
senses. All 30 article-level N3 labels match frozen EN `docs/n3-vocabulary-sources.tsv`; 抱く's source row is いだく, which the card
teaches. EN links to absent RU targets are kept as plain text. No optional items.

### Consistency and quiz safety

Verdict: consistency **CLEAN** (front matter, format, links, navigation, manifest, intake); quiz safety **NEEDS FIX** (F1-F3).

- Front matter matches EN field for field in all 30 cards apart from translated titles and the two added exclusions. There are no
  RU-only links; every RU link target exists; EN links omitted in RU all point to targets with no RU file. All 10 navigation diffs
  change only link markup at existing mention positions. `contentVersion` and exactly 40 file entries changed in the manifest, and
  every changed hash matches. The reviewer also noted 118 pre-existing `strokes/*.json` raw-byte mismatches caused by the
  `core.autocrlf=true` working tree; those files are untouched by the candidate.
- F1 (medium as reported, medium-high confidence), `交換.md` exclusions: 交換 «обмен; замена одного другим» and 両替 «обмен валюты;
  размен купюр» share «обмен» without a direct pair. Remedy: 交換 `[取り替える, 代わり, 両替]`.
- F2 (medium, medium confidence), `掴む.md` exclusions: 掴む «хватать рукой; схватывать (суть)» lacks pairs with 捕まえる «ловить;
  захватывать» (JMdict "to seize") and 理解 «понимание», which the 掴む card itself compares. Remedy: `[握る, 捕まえる, 理解]`;
  the reviewer called 捕まえる the stronger case.
- F3 (low-medium, medium confidence), `持ち上げる.md` exclusions: 立てる «ставить вертикально; поднимать» is near «приподнимать»,
  and 立てる already excludes 上げる. Remedy: `[上げる, 立てる]`.
- F4 (low, high confidence; internal citation accuracy, not quiz safety), `提出.md` «Синонимы и антонимы»: 出す is quoted as
  «вынимать; сдавать», which is not the RU 出す title «вынимать; выносить».

Optional: conservative guards 掲示→放送 («объявление») and 手術→作業 («операция», low risk); no guard needed for 戻す/置く, 我慢/遠慮,
the same-reading pairs 或/ある, 振る/降る and 指す/差す, 換える/変える, 抜ける/抜く, 握る/持つ, 提出/おつり, or 抜ける/降る (disjoint
qualifiers on «выпадать»).

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (指す, 手品, 抱く; no established defect in the other 27); scoped coverage **CLEAN**.

- C1 (medium, high confidence), `指す.md:4,12`: the title and H1 «указывать (пальцем); иметь в виду» teach a finger restriction
  that line 29 withdraws and a speaker-intention gloss the card never teaches. Evidence: the card's examples (map, clock hand,
  shogi) and JMdict 指す senses 1, 3, 4. Remedy: title and H1 «указывать на что-либо»; not «показывать; указывать», which is 示す's
  title.
- C2 (low, high confidence), `手品.md:41-42`: an English-dependent aside about the old dictionary gloss "juggling" follows a clear
  Russian contrast with жонглирование. Remedy: delete it and keep the Russian contrast.
- C3 (low, high confidence), `抱く.md:26`: «но в просмотренной записи он не помечен как сленг» is an author note about dictionary
  markup that a beginner cannot use. Remedy: end the sentence at «Это тоже переходный глагол годан.»

Optional: 不利's «одно и то же устройство» for EN "arrangement" could read as a gadget («один и тот же расклад» or «одни и те же
условия»); 持ち上げる's title leads with «приподнимать» while the body says «поднимать». Title-screen leads given without verdicts:
抜ける/降る («выпадать», different qualifiers) and 手術/作業 («операция», already limited to surgery).

## Exclusion classification: author, coordinator and consistency reviewer

All 19 EN exclusion entries (12 lists) are retained. The author added two direct, one-sided pairs beyond EN; four more were added
after review from the consistency reviewer's findings: six pairs on four cards. The author report, the blind consistency reviewer
and the coordinator's dispositions classify them independently; the differences are preserved rather than resolved by vote.
Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer | Coordinator disposition |
|---|---|---|---|
| `交換`→`代わり` | conservative | conservative | kept |
| `扱う`→`操作` | conservative | required | kept |
| `交換`→`両替` | not declared (EN-parity «обмен» overlap; 両替 currency-specific) | required-class (F1); on recheck accepted the coordinator's reassessment | added; conservative, because the EN titles share "exchange" equally without a guard |
| `掴む`→`捕まえる` | not considered | required (F2, the stronger case) | added; required-class |
| `掴む`→`理解` | not considered | F2 (verb/noun-sense collision) | added; conservative |
| `持ち上げる`→`立てる` | not considered | required (F3) | added; required-class |
| `掲示`→`放送`, `手術`→`作業` | not declared (different senses) | optional conservative | not added |
| `抜ける`–`降る` | declined (disjoint qualifiers) | no guard needed | not added |

Neither the author nor the reviewer found a kept pair unjustified. The correctness reviewer independently found the two
author-added pairs supported.

Reconciliation, the coordinator's dispositions and the final verdicts are in `207-words-batch-46-recheck-001.md`.
