# Batch 194 — independent review 001

## Snapshot and scope

- Reviewed commit: `6947a60b9c7d3731fd7f76d426d5721db87c55ee` (tree `b3d62aa2c27ac5821b90274487ade692874be11f`), branch `full-ru-194-words-33`, parent `afec4b7`.
  The candidate was committed signed directly and pushed before review.
- Published baseline recorded in the intake: `93d7bf3` (B193 merge). Parent `afec4b7` adds only the B193 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards.
  - Correctness and consistency also inspected the twelve navigation-only files.
  - Consistency additionally covered `manifest.json` and the intake.
  - Comprehensibility read the link-only edits as context, without separate verdicts.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD and the working tree were unchanged.
- Full blind reports:
  - `194-words-batch-33-review-correctness-001.md`
  - `194-words-batch-33-review-consistency-001.md`
  - `194-words-batch-33-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or one another's reports.
  The consistency reviewer re-ran `word_title_screen.py` itself as a lead.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN**; scoped coverage **CLEAN** across all 30 cards. No findings and no optional items.

- All 30 headwords were read from the Jisho/JMdict API, checking spelling, reading, sense, part of speech, restrictions and notes.
  The reviewer confirmed, among others, the が/を contrasts in 解ける/解く and 覚める/覚ます, that 目を覚ます is not presented as
  necessarily waking another person, the separate かぶる and こうむる entries for 被る, and that 袋 is ふくろ rather than the
  separate たい counter.
- Every removed EN link was checked against its RU-relative target; all such targets are absent from the bounded RU tree.
- The reviewer ran the validator (0 errors) and compared all 42 changed file hashes with the manifest (0 mismatches).
- After the blind report, the coordinator asked the same reviewer to check nine Russian lexical choices against actual Gramota
  entries (Kuznetsov's BTS and the BUS): зритель/публика (観客), рукав (袖), пакет/мешок (袋), голый/неприкрытый (裸),
  предать/подвести (裏切る), урегулировать (解決), высокопоставленный (偉い), составляющая (要素) and изделие/продукция (製品).
  All nine were **CLEAN**. The addendum is appended to the correctness report and is not a blind finding.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (F1, F2); scoped cross-file integration **CLEAN**.

- F1 (minor, medium confidence): 見事 «замечательный; восхитительный» lacked a guard against 凄い «потрясающий; невероятный»,
  although both cards already guard the same praise neighbours.
- F2 (minor, low-to-medium confidence): 解決 teaches 解決する as «решать что-либо», the same Russian verb as the title of
  決める «решать; определять»; the batch already guards 解く→決める and 解ける→決まる for that overlap.
- Optional: 解決→決まる (low confidence); 親友–親しい needs no action; the English «to suffer» provenance sentence in 被る
  belongs to the comprehensibility facet.
- The reviewer ran the validator (0 errors), `build_manifest.py` (no change) and the content budget check, compared front matter,
  headings and example counts with EN, checked EN link parity over all changed files and the reverse links to the 30 new targets,
  ran its own exact title-segment collision scan and recomputed all 42 intake payload hashes.
  Its dictionary sense wording is self-declared as recalled rather than re-fetched.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (被害, 被る, 覚ます); scoped coverage **NEEDS FIX** for 覚ます, otherwise **CLEAN**.

- C1 (minor, high confidence): `被害.md:16` defined the word as harm «увиденные со стороны того, кто их понёс».
  «Увиденные» can be read as harm that was seen or witnessed rather than suffered.
- C2 (minor, high confidence): `被る.md:46–48` ended with the English gloss «to suffer» and a remark about the source-list
  compiler, which an English-free beginner cannot use.
- C3 (minor, high confidence): the 覚ます title «будить; пробуждать» began with the entire title of the existing 起す «будить»,
  while EN keeps the titles apart; the card never named 起す or showed waking another person.
- Optional items: say that お in お見舞い is the polite prefix; 解く:39 warned against «расстёгивать», a gloss the card never teaches.
- The reviewer read the JMdict entry 1484350 (被害) for C1; other dictionary lines were checked against the frozen EN text.

No finding established a missing requested card, a lost EN teaching point or a necessary prerequisite omission.
Optional suggestions are kept in the complete reviewer reports rather than promoted to defects.

## Exclusion classification: author and consistency reviewer

The author added 25 direct, one-sided exclusion pairs beyond EN on 13 new cards. All 20 EN exclusion entries across 13 lists are
retained; the author report's count of "12 EN pairs" understates them, and a coordinator recount of the source front matter gives 20.
The author report and the blind consistency reviewer classified them independently. The differences are preserved here
rather than resolved by vote. Classification does not change runtime behaviour, because every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `解決`→`解く` | conservative | required (sense-sharing family) |
| `解決`→`解ける` | conservative | required (sense-sharing family) |
| `解ける`→`解く` | conservative | required (intransitive/transitive pair) |
| `解く`→`決める` | required | conservative (shared Russian «решать» only) |
| `偉い`→`偉大` | conservative | required-leaning (EN 偉い body names 偉大) |
| `上等`→`すばらしい` | required | conservative (real basis) |
| `被る`→`履く` | conservative | required (shared «надевать») |
| `要点`→`中心` | required | conservative |
| `観察`→`見物` | required | not classified in the table; noted as guarded |

Both classify the remaining 16 pairs the same way:
- required: `解決`→`決定`, `親友`→`友人`, `友達`, `友`, `覚ます`→`起す`, `見舞い`→`訪問`, `偉い`→`立派`, `感心`,
  `被る`→`着る`;
- conservative: `解ける`→`決まる`, `見舞い`→`訪ねる`, `伺う`, `偉い`→`優秀`, `大した`, `要素`→`部分`, `製品`→`品物`.
  The reviewer places 偉い→優秀 and 偉い→大した at the weak end of conservative but recommends no removal.

The author counts 13 required and 12 conservative; the reviewer counts 13 required, 1 required-leaning, 10 conservative
and 1 unclassified. The reviewer judged no added entry to block a distinction the cards teach.
The two guards added after review (見事→凄い, 解決→決める) bring the RU-added total to 27 and are recorded in the recheck record.

Reconciliation, the coordinator's dispositions and the final verdicts are in `194-words-batch-33-recheck-001.md`.
