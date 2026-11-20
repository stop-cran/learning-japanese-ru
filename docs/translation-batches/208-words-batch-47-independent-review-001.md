# Batch 208 — independent review 001

## Snapshot and scope

- Reviewed commit: `8963d85fc260aff6125e062366bcb09428c788ac` (tree `f0b363a16795dc636e1495eb6af34ee0f76fd3a4`), branch
  `full-ru-208-words-47`, parent `8266013`. The candidate was committed signed directly and pushed before review.
  - The content was authored in a scratch worktree on the B207 content tree `808eb9e7ae01c1a32fbce47a04312e96e1d82b05`.
    Before committing, the coordinator byte-compared all 44 content files between the scratch worktree and the primary
    checkout and checked that the 14 navigation files were unchanged between `808eb9e` and the published baseline.
  - Before the candidate, the coordinator made three content changes to the author's output:
    - `恐怖`: the reading join «キョウ + フ» became EN's hiragana «きょう + ふ».
    - `応じる`: the title and H1 «соглашаться (на просьбу); соответствовать» became «откликаться; соглашаться (на
      просьбу)», because «соответствовать» is not an EN title sense; に応じて stays taught in the body.
    - `思想`: the title and H1 «мировоззрение; идеология» became «мысль; идеология», for EN "thought; ideology", and
      the reading join «シ + ソウ» became «し + そう».
  - The candidate differs from the published baseline by 30 new word cards, 14 navigation-only files (18 restored links),
    `manifest.json` and the intake.
- Published baseline recorded in the intake: `7e34591050f565e11de978da42fe85c99bfa6262` (Batch 207 merge). Parent `8266013`
  adds only the Batch 207 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers against their EN originals.
  - Correctness also read the complete runtime diffs of the 14 navigation-only files, the RU 評価, 思う and 鬼 cards that the
    new comparisons cite and the binding RU instruction and reference files. It inspected the Jisho/JMdict entries for all
    30 written forms (recovering one HTTP 429 response for 恐ろしい with a later paced request), the Digital Daijisen entries
    堪える and 息, and the Russian-side entries behind the adaptations: Kuznetsov (gramota.ru) «пытаться», «конституция»,
    «ужасный», «клевета» and «сердце», Babenko «клевета», Gramota's noun-suffix rules page and Efremova's -ость entry. It
    ran `tools/validate.py` (0 errors).
  - Consistency read all 14 navigation diffs in full, checked every `manifest.json` entry (4,354, all hashes matching) and the
    intake's 44 paths and candidate hashes, ran `tools/validate.py` (0 errors), and classified every added exclusion.
  - Comprehensibility read the RU 鬼, 近代, 感心, 必ず, 急に and 記憶 cards for convention and contrast and checked link parity
    on the 30 new cards. It did not read the navigation files as prose, gave no verdict on them and did not
    run the validator. The JMdictDB page for 悪戯 (1151580) is password-gated, so it relied on the JapanDict rendering of that
    entry.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD was still `8963d85`
  and that `git status --porcelain` was empty. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator and named the report as the only file a
  reviewer writes. The correctness and consistency reports state that no generator was run; the initial comprehensibility
  report does not mention generators, and its rechecks state that none was run. The coordinator found the tree clean after
  each review.
- Full blind reports:
  - `208-words-batch-47-review-correctness-001.md`
  - `208-words-batch-47-review-consistency-001.md`
  - `208-words-batch-47-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or notes, or one
  another's reports.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (必死 only); scoped coverage **NEEDS FIX** (息 only). The other 29 cards were clean on each
facet within this scope.

- C1 (minor, high confidence), `必死.md:21`: «Она отчаянно пыталась сдержать смех» asserts only an attempt, whereas
  彼女は必死に笑いをこらえました reports actual restraint. The loose wording follows EN's "tried desperately". Evidence: Digital
  Daijisen 堪える sense 2 with the collocation 笑いをこらえる; JMdict 堪える sense 2; Kuznetsov «пытаться». Remedy: «Она изо всех
  сил сдерживала смех.», with the Japanese unchanged.
- C2 (minor, high confidence), `息.md:45-47`: RU dropped EN:45's boundary sentence "That construction does not make 息 a
  general noun for a vocal or musical 'tone.'" after the 息が合う example. Remedy: append «Этот оборот не делает 息 общим словом
  для тона голоса или музыкального тона». The reviewer withdrew this finding in its second recheck; see the recheck record.

Other checks: the original Japanese examples and reading-join scripts are retained; original metadata and exclusions are
preserved; no EN link whose RU target exists was dropped. The Russian-side adaptations (憲法 «конституция» as physique, 恐ろしい
and «ужасный», 悪口 and «клевета», 心臓 and «сердце», the 性/-ость analogy, 感動 without the English "impressed" remark) are
supported by the inspected entries; the -ость analogy is qualified, not a one-to-one rule. Optional: add the verified Russian
dictionary references to provenance records or learner citations; make the source-oriented wording at 必死:41 more
learner-facing (outside the reviewer's facet).

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **CLEAN** (optional notes only); cross-file integration (manifest, intake,
navigation) **CLEAN**.

- Front matter matches EN apart from translated titles and the added exclusions. EN links omitted in RU all point to
  targets with no RU file (績, 象, 臓, 感ずる, 間隔, 劇, 冗談, 性別, 性質, 従う, 応ずる). There are no broken RU links, and the EN and
  RU link sets to the 30 new words are identical across all non-doc files. The manifest changes exactly 44 entries plus
  `contentVersion`.
- K1 (minor/optional, medium confidence), `鬼.md` and `悪魔.md`: «óни» mixes a Latin ó with Cyrillic letters. It is an
  intentional device explained in the 鬼 card but used nowhere else and awkward for search and copy.
- K2 (optional), `急速.md` exclusions: 急速→急に is weak, because «стремительный» does not overlap «внезапно; резко». It is
  harmless.

Optional: guards 意外→[突然, びっくり] and 応じる↔答える would be harmless; neither is required.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (思想, 急激, 悪戯; the other 27 cards clean); scoped coverage **CLEAN** for all 30.

- P1 (minor, high confidence), `思想.md:19`: «мысль Нового времени» equates 近代 with Russian school-history «Новое время»
  without the qualification required by the published 近代 card (`近代.md:12,16,18,33`). Remedy: «Я изучаю в университете мысль
  эпохи модернизации.»
- P2 (minor; high confidence that it is English-dependent), `急激.md:42-43`: «а не политические взгляды» answers EN's remark
  about English "radical"; the RU title and body use «резкий», which has no political sense. Remedy: end the sentence at
  «изменения.»
- P3 (minor, high confidence), `悪戯.md:22`: «портить механизм» asserts damage, whereas 機械にいたずらする is tampering or fooling
  around with a machine. Remedy: «баловаться с машиной, копаться в механизме».

Optional: 悪魔:25 «óни» follows the published 鬼 card (polish only); 成績:37 leaves 発表 without a reading (the sentence is RU-only and quotes EN 評価.md:18, which gives the reading; adopted in fix 3); 必死:21
«пыталась» is weaker than completed こらえました but matches EN "tried". Out of facet: kanji/恐.md and words/怖い.md leave 恐ろしい
and 恐怖 plain although those RU files now exist.

## Exclusion classification: author and consistency reviewer

All 19 EN exclusion entries (11 lists) are retained. The author added 20 direct, one-sided entries on 15 new cards; no
exclusion changed after review. The author report and the blind consistency reviewer classified them independently; the
differences are preserved rather than resolved by vote. Classification does not change runtime behaviour, because every
pair is declared. They agree on 恐れる→びくびく, 急激→急に, 思い出→記憶 and 心臓→心/胸 as required, and on 成績→評価,
慎重→注意/用心, 感覚→気持ち, 感動→感心 and 意識→気付く as conservative. They differ on:

| Pair | Author | Consistency reviewer | Coordinator disposition |
|---|---|---|---|
| `感じる`↔`感じ` | required (noun/verb naming the same action) | conservative; redundant because declared on both sides | kept; each side documents its own guard |
| `急速`↔`急激` | required (near-synonymous; shared example frame) | conservative; redundant because declared on both sides | kept |
| `必ずしも`→`必ず` | required (title stem «обязательно») | conservative | kept |
| `悪魔`→`鬼` | conservative («демон» covers both) | required (shared segment «демон») | kept |
| `応じる`→`返事`, `承知` | conservative | required (shared «отклик», «соглас-») | kept |
| `急速`→`急に` | conservative (contrasted in the body) | weak but harmless (K2) | kept |

Neither found a kept pair harmful. The correctness reviewer confirmed that the added exclusions exist; it did not audit them
exhaustively.

Reconciliation, the coordinator's dispositions and the final verdicts are in `208-words-batch-47-recheck-001.md`.
