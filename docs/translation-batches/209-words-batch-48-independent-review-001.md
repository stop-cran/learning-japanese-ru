# Batch 209 — independent review 001

## Snapshot and scope

- Reviewed commit: `5f015601f1ff714f7c63b0edfa85215c8f99f071` (tree `b7775854199e6bd437d9ef17989cc2a7a45ae79a`), branch
  `full-ru-209-words-48`, parent `c834ac2`. The candidate was committed signed directly and pushed before review.
  - The content was authored in a scratch worktree on the Batch 208 candidate `8963d85fc260aff6125e062366bcb09428c788ac`.
    Before copying, the coordinator checked that the 20 navigation files were unchanged between `8963d85` and the published
    Batch 208 tree and that none of the 30 new cards existed there; before committing, it byte-compared all 50 content files
    between the scratch worktree and the primary checkout.
  - Before the candidate, the coordinator made one content change to the author's output: `得意`'s title and H1 «конёк;
    хорошо удающееся дело» became «сильная сторона; хорошо удающееся дело», for EN "one's strong point". The figurative
    «конёк» (ru.wiktionary senses «любимая тема», «любимый предмет приложения усилий») implies fondness, whereas the card,
    following EN, states that 得意 asserts ability without asserting enjoyment. The body mentions at lines 16, 25 and 33 were
    aligned, and the new exact segment «сильная сторона», shared with the published 武器 «оружие; сильная сторона», was
    guarded by adding 得意→武器.
  - The candidate differs from the published baseline by 30 new word cards, 20 navigation-only files (27 restored links),
    `manifest.json` and the intake.
- Published baseline recorded in the intake: `77a567dc73329b88f95a6e305ee6618bb5db5255` (Batch 208 merge). Parent `c834ac2`
  adds only the Batch 208 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers against their EN originals.
  - Correctness inspected every changed line of the 20 navigation-only files (changed-passage review, not a full re-review
    of those files), read in full the RU 武器, 有効, 左右, 毒, 性, 苦手, 自慢, お弁当 and 陰 cards for the actual comparison
    senses and labels, and read the three binding RU instruction and format documents. It queried the Jisho/JMdict entries
    for all 30 written forms and for 武器, 有効, 左右, 毒, 性 and the prefix 御, and the Digital Daijisen entry ごうとう (強盗).
    Russian-side evidence came from the entry bodies Kuznetsov «сторона», «второй», «малолетний», «следовать», «попасть»,
    «тень» and «грабеж» and Ozhegov «пол» and «реклама» (Gramota requests were rate-limited). It ran `tools/validate.py`
    (0 errors).
  - Consistency read all 20 navigation diffs in full, checked the manifest hashes of the 50 changed Markdown files and the
    intake's top-level structure, ran `tools/validate.py` (0 errors), and classified every added exclusion. It worked from
    the prompt's contract without reading the RU instruction files, and its JMdict senses for the exclusion pairs came from
    its own knowledge rather than fetched entries.
  - Comprehensibility opened the RU 気持ち, 陰, 性, 役, 若い, 小さい and 小さな cards for convention and checked link parity on
    the 30 new cards. Its evidence included JMdict 1454510 with a Jisho example for 得意, the Gramota Большой толковый словарь
    result and Russian Wiktionary for «малолетний». It did not read the navigation files as prose, gave no verdict on them
    and does not report running the validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD was still `5f01560`
  and that `git status --porcelain` was empty. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator and named the report as the only file a
  reviewer writes. The initial correctness report states that no generator was run; the initial consistency and
  comprehensibility reports do not mention generators, and their rechecks state that none was run. The coordinator found the
  tree clean after each review.
- Full blind reports:
  - `209-words-batch-48-review-correctness-001.md`
  - `209-words-batch-48-review-consistency-001.md`
  - `209-words-batch-48-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or notes, or one
  another's reports.

## Initial verdicts and findings

### Correctness

Verdict: correctness **CLEAN**; scoped coverage **CLEAN**, for all 30 new cards. No findings and no optional notes.

The reviewer compared every example and explanation bilingually, including argument marking, transitivity, polarity,
register and event stage. It confirmed that the 当てる/当たる contrast keeps the agent/contact distinction, that 従う and 影響
keep their に constructions, that 心理 keeps the person-state/discipline distinction, that 引用 and 広告 each keep act versus
material, and that 強盗 keeps offender versus offense. Original metadata and exclusions are preserved, all EN links whose RU
target exists are retained, and the 27 navigation changes add links without changing the displayed teaching text. The
Russian-side adaptations (得意's title «сильная сторона», 後者 «второй» restricted to two mentioned items, 幼い's title
«малолетний», 床/性 and the homonymy of «пол», 広告 «реклама», 従う «следовать», 当たる/当てる «попасть», 影 «тень», 強盗 and
«грабёж») are supported by the inspected entries. In its recheck the reviewer stated that this CLEAN verdict missed the three
localized fidelity issues later corrected; see the recheck record.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **CLEAN** (optional guards only); scoped coverage **CLEAN**.

- Front matter of all 30 cards equals EN apart from the translated titles and the added exclusions; all EN exclusions are
  retained. There are no RU-only or dangling links; EN links to absent RU targets (底, 完全, 従姉妹, 前者, 主張, 参考, kanji 床, 宣伝,
  齢) are plain text. After stripping link markup, each of the 20 navigation files equals its base text. All 50 changed
  Markdown files match their manifest hashes.
- The five RU-added exclusions were classified independently: 得意→武器 («сильная сторона»), 影響→左右 («влияние») and 床→性
  («пол») as required; 効果→有効 and 影響→毒 as conservative. None is unjustified.
- Optional (minor, medium or low confidence; EN guards none of them): 引退↔辞める and 徹底↔丁寧 (medium), 心理↔精神 and 得意↔自慢
  (low), and the weaker pairs 当時↔昔, 幼い↔若い, 従う↔守る, 役割↔担当, 従兄弟↔親戚, 強盗↔犯人, 年齢↔歳, 強力↔力 and 効果↔副作用.
- Limit: a raw sha256 of 118 `strokes/*.json` files did not match the manifest; the reviewer treated this as pre-existing or a
  method artifact. The manifest hashes text after CRLF→LF normalization, and those 118 blobs contain CRLF; the reviewer
  confirmed this in its recheck and withdrew the limit.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (得意 only; the other 29 cards clean); scoped coverage **CLEAN** for all 30.

- C1 (minor, high confidence), `得意.md:19`: «Лучше всего мне даётся математика» adds a superlative that 得意な科目は数学です does
  not have, so a learner may take 得意 to mean "the best" rather than "a strong subject". Evidence: no 一番 or 最も in the
  sentence; frozen EN "My strong subject is mathematics."; JMdict 1454510 sense 2 "one's strong point; one's forte". Remedy:
  «Предмет, который мне хорошо даётся, — математика.»

Optional notes:
- `幼い.md:4,11`: «малолетний» is not the natural word for either taught example (the body itself uses «маленьким» and
  «незрелый»); not raised as a finding, because the body teaches both senses naturally and a bare «маленький» would collide
  with 小さい.
- `役割.md:19` adds «насоса», which 血液を送る does not say.
- `引っ張る.md:18` «сильнее» is comparative where 強く is «сильно».
- `年齢.md:19` «записаться» is registration where 参加できます is participation.
- `従う.md:16`: the slash list «следовать за человеком / указаниям / правилам» mixes cases.
- `床.md:4` «пол (в помещении)» with its examples adequately separates floor from sex and from storey; not a defect.

The reviewer also confirmed that English-dependent EN remarks (得意 "prosperity", 強調 "stress", 強盗 "burglary", 弁当 "box
lunch", 床 "floor/storey", 広告 countability, 強力's community gloss) were adapted into Russian or dropped without losing the
Japanese rule, and that no English leftovers remain in learner prose.

## Exclusion classification

All 25 EN exclusion entries (16 lists) are retained. Five direct, one-sided entries were added on four new cards: 効果→有効,
影響→左右, 影響→毒 and 床→性 by the author, and 得意→武器 by the coordinator with the 得意 retitle. The author's report, the
coordinator's notes and the blind consistency reviewer classified them identically: 得意→武器, 影響→左右 and 床→性 required (exact
shared title segments), 効果→有効 and 影響→毒 conservative (shared stems). No exclusion changed after review. The correctness
reviewer inspected the Japanese side of each added pair and found the guards supported; it did not audit exclusions
exhaustively.

Reconciliation, the coordinator's dispositions and the final verdicts are in `209-words-batch-48-recheck-001.md`.
