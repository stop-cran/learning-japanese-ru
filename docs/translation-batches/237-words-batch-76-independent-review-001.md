# Batch 237 — independent review 001

## Snapshot and scope

- Reviewed commit: `be448e7c8309d0b9fe6296bd3bc75b2508312556` (tree `3fdba75c00a9a083e212398d0b36c726a2e6f7e7`), branch
  `full-ru-237-words-76`, parent `f9bab89`. The candidate was signed and pushed before review.
  - The branch's first candidate push, `335c157` (signed, same tree and parent), carried the wrong commit message
    "Batch 236 candidate"; about 20 seconds later the coordinator replaced it on the branch with `be448e7`, whose
    message names Batch 237. No review read `335c157`.
  - The content was authored in a scratch worktree on the Batch 236 candidate `122b0192996f8c54236941b802ee5b10a19d06fd`.
    Before copying, the coordinator's candidate script checked two things: that the seven navigation files edited there
    (`kanji/付.md`, `kanji/占.md`, `kanji/言.md`, `words/応じる.md`, `words/解ける.md`, `words/説明.md` and `words/集合.md`)
    were unchanged between `122b019` and the candidate's parent `f9bab89`, and that none of the 30 new cards existed in the
    primary checkout. It also checked that the branch, HEAD and `origin/main` were the expected ones and that the tree was
    clean.
  - The script byte-compared the 37 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 37 batch paths plus `manifest.json`. Its byte scan of all
    37 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 37 committed
    blobs at `be448e7` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from Batch 236; all nine restored links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made no content edits: no title edit, no exclusion
    append and no held link; the 37 lane files were copied unchanged. Its adjudication record states:
    - "Screens rerun by the coordinator with RU_ROOT = lane: `validate.py` 0 errors; `navonly.py HEAD --only` over
      kanji/付, 占, 言 and words/応じる, 解ける, 説明, 集合 reports 7 files, 9 links added, 0 problems; the lane's
      changed-path set is exactly the 37 paths (30 new cards + 7 restoration files) plus manifest.json.";
    - for `word_title_screen.py` over the 30 words: "one unguarded exact-segment pair, アイデア ~ アイディア, whose whole
      titles are identical («идея; задумка»). EN gives both the identical title "idea" and declares no mutual exclusion;
      the two are spelling variants of one word and the quiz deduplicates identical titles. Accepted at EN parity; no
      guard added. Every other exact shared segment is guarded (お待ちどおさま/お待たせしました/すまない against すみません,
      ありがとう, どうも and each other; 応ずる–応じる, 応ずる–承る; 親類–親戚; 見送る–省く/飛ばす/送る).";
    - for `link_parity.py` over the 37 paths: "RU-only link 言付ける:35 → 言い付ける (reading/spelling comparison that the
      frozen EN card makes in plain text; the target is in this batch). Accepted under the B222 precedent."; "kanji/付.md
      EXTRA 付く and kanji/言.md EXTRA 言葉 are pre-existing at 122b019, not B237 changes."; "No LOST links. EN links left
      plain because the RU target is absent: kanji 訳 (訳す), kanji 溶 (溶ける), kanji 測 (観測), words/悔やむ (詫びる),
      words/敬語 (言葉遣い).";
    - "Titles compared with EN one by one; no coordinator title edit.";
    - "RU-added exclusions accepted as reported: 8 pairs; required 親類→親戚 («родственник», «родня»), 見送る→省く and
      見送る→飛ばす («пропускать»); conservative 解散→終了/閉会, 観測→読み, 回答→応対, 慰める→落ち着く (new
      `quiz_exclusions` line; EN has none).";
    - "Unverified Russian usage to hand to the reviewers: «нет уж, увольте» for the ～はごめんだ refusal sense of ごめん,
      «задумка» in the アイデア/アイディア titles, and «доносить» in the 言い付ける title (the body also uses «ябедничать»;
      whether «доносить» is too strong for a child telling a teacher).";
    - "Resolved before the candidate (title screen rerun on 8b5e2b3 = B236 fix 1 + the 30 lane cards; output
      `b237-prefix-screen.txt`, diffed against `b237-lane-screen.txt`): the only exact-segment hit is still アイデア ~
      アイディア (accepted above)." The changes from the Batch 236 fix are stem-only: 詫びる ~ 請う «проси» and 応ずる ~ 請う
      «пригл», each decided without a guard; 言付ける ~ 恐縮 «доста», a coincidental stem, no guard; すまない ~ 恐縮 «хлопо»,
      "already guarded by the EN pair". "No B237 path quotes the replaced 恐縮/請う titles or other removed wording."

    The committed manifest records 5,229 entries (5,224 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The consistency
    reviewer also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 7 files with 9 restored navigation links (the kanji cards 付, 占 and 言 and the word cards 応じる, 解ける, 説明 and
      集合);
    - `manifest.json` (`contentVersion` `40af8534a08ba712`, 5,229 entries);
    - the intake, whose note reads "B237 30-card adaptation with nine navigation-only link restorations in seven existing
      files; candidate before blind review."
- Published baseline recorded in the intake: `8e183ba1efe41ff7c3c37519b37e5b513ce65bba` (Batch 236 merge). Parent
  `f9bab89` adds only the Batch 236 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 7 files (9 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen: no unguarded exact title-segment overlap apart from the identical アイデア ~ アイディア titles accepted
    at EN parity (62 `OK` lines for pairs already guarded by an exclusion, 407 stem-only `!!` lines and the one exact
    アイデア ~ アイディア `!!` line);
  - link parity: no EN link lost where the RU target exists; the only RU-only link added by the batch is 言付ける:35 →
    言い付ける; the kanji cards 付 and 言 keep their pre-existing RU-only links to 付く (lines 22, 35 and 52) and 言葉
    (lines 33 and 42), present at the published baseline.
- Common sample: all three reviewers read all 30 new word cards in full. The correctness and comprehensibility reviewers
  read each card against its complete frozen EN original. The consistency reviewer compared the EN originals by script
  and by eye, read the seven navigation-file diffs, and checked the intake path list and the manifest.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file, with the primary JMdict entry inspected for
    each), inspected the changed hunks of the seven navigation files ("these introduce links without changing their
    teaching text"), checked all linked word titles and readings, and read `words/恐縮.md` in full to verify the
    descriptions in ごめん and すまない; not a whole-card re-review of every pre-existing comparison target or kanji.
  - Inspected the actual numbered JMdict_e entries, parsed in memory, for every primary entry, plus 邪魔 1323500:1–2 and
    溶かす 1546040:1–2; initial Jisho throttling and an FTP-host certificate failure were superseded by the canonical-host
    JMdict XML.
  - Japanese sources beyond JMdict: Digital Daijisen on Weblio (御免 definitions 1–5, ごめんください 1–2, 詫びる, 謝る,
    すまない, 診る (みる definition 7), 診断 1–2, 訳す, 言付ける, 評論, 言葉遣い, 親類 and 見送る) and Kotobank (御待遠様 from
    Daijisen and Seisenban, 応ずる from Seisenban, 応じる from Daijisen, 回答, 解答, and 観念 from Seisenban).
  - Russian sources: the dictionaries on gramota.ru (уволить, Kuznetsov definition 3 and the universal dictionary's
    speech-formula definition; задумка, доносить, ябедничать, весть, гостинец, виноватый, подглядеть, смирение, критический
    and прогноз); scoped meaning checks, not frequency claims.
  - A span-parity scan of Japanese sentences and kana readings; the N2 labels were checked against the frozen EN
    `docs/n2-vocabulary-sources.tsv`.
  - Ran no generator and no validator.
- Consistency review scope:
  - Read all 30 RU cards in full and all seven navigation diffs (`-U0`, every changed line seen); compared every new
    card's front matter (except the title), heading count and `.md` link set with the frozen EN card by script; checked
    that all RU runtime links resolve and EN-link parity in every EN file that links a new word; ran the validator (0
    errors).
  - Compared `manifest.json` with an in-memory `build_manifest()` result (no write): identical. Importing the module
    created a Python bytecode cache directory, which the reviewer deleted; the tree was clean again.
  - Checked that the intake's 37 payload paths equal the 30 cards and seven navigation files of the diff.
  - Did not read the coordinator's title-screen output; its semantic screening was its own title review and pair
    matrices. Dictionary senses were cited from memory, not re-fetched.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN; read the seven navigation diffs as diffs only ("link additions; gloss text
    unchanged"), outside its verdict. "Intake JSON, manifest, and `docs/translation-batches/` were not read."
  - Dictionary checks used the public Jisho API (JMdict) and a Daijisen snippet for 覗く, "not a full Kotobank capture of
    every cited entry". It records no validator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; the correctness report says "Model identity not independently verifiable", the consistency report "Model:
  not verifiable." and the comprehensibility report "Model: not verifiable from this session".
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. The correctness
  report records HEAD matching `be448e7` with an initially clean working tree; the consistency report records `be448e7`
  with an empty `git status --porcelain` after deleting the bytecode cache it had created; the comprehensibility report
  records an empty `git status --porcelain` with HEAD matching the candidate and no uncommitted changes. No fix was
  applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No reviewer reported running a generator script: the correctness report says "No repository
  files edited or generators run."; the consistency report records the validator run and the in-memory manifest
  comparison, which imported `tools/build_manifest.py` and called its function without writing a file; the
  comprehensibility report records no validator or generator run. No tracked repository file was changed.
- Full blind reports:
  - `237-words-batch-76-review-correctness-001.md`
  - `237-words-batch-76-review-consistency-001.md`
  - `237-words-batch-76-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  Unlike Batch 236, the Batch 237 briefs made no exception for the intake record; the consistency brief asked for a
  manifest-consistency check. The correctness report says that no "author artifacts, RU batch records, tracking files,
  other reviewer reports or forbidden scratch worktrees were read/run." The consistency report makes no statement about
  unread materials; it says it did not read the title-screen output, and it nonetheless records checking the intake
  record's path list against the diff. The comprehensibility report says the intake JSON, the manifest and
  `docs/translation-batches/` were not read.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **CLEAN** and scoped coverage **CLEAN** for all 30 paired cards and the ancillary link-only
changes; Russian comprehensibility **UNVERIFIED** (not an assigned facet). Findings: none.

What the reviewer confirmed:
- All primary JMdict entries match the cards' selected readings and taught senses. In particular, 1002360 marks
  お待ちどうさま with the irregular-kana flag `ik`, so the card's warning is justified; 1264230:1–2 supports the instruction
  and telling-on senses of 言い付ける; 1593330:1–2 supports intermediary delivery and the acknowledged archaic pretext of
  言付ける; 1546070 includes 解ける among the melting/dissolving spellings; 1470840 distinguishes the transitive looking
  senses of 覗く from intransitive partial appearance; 1609380 identifies the ずる alternative; and one entry, 1014210,
  supplies both アイデア and アイディア.
- The monolingual sections support the consequential distinctions and additional senses, among them the visiting and
  leave-taking uses of 御免 and ごめんください, the formal tendency of 詫びる, the apology/gratitude/request uses of すまない,
  medical examination for 診る and the conjugational relationship of 応ずる and 応じる.
- The Russian entries support «нет уж, увольте» as a refusal (Kuznetsov definition 3 and the universal dictionary), the
  colloquial «задумка», the reporting-on-someone senses of «доносить» and «ябедничать» (including Kuznetsov's teacher
  example) and «виноват» as an apology interjection; "A bookish shade is a style consideration, not evidence that the
  refusal sense is false."
- Example translations preserve the taught roles, polarity, event and tense. Every EN-selected sense, example, citation
  and Japanese teaching restriction is retained; the omitted English-specific "interpret/examine/snitch" comparisons do
  not remove the corresponding restrictions, which remain elsewhere in RU.
- Word, reading, jlpt, type, kanji and tags match EN throughout; every original exclusion is retained, and six cards
  add exclusions. No broken RU Markdown target and no dropped EN link whose RU target exists were found; all 30 N2
  labels match the frozen EN source list.

Optional: none in the assigned facets. Limits: CLEAN means no established actionable defect, not an exhaustive proof;
Russian comprehensibility, whole-corpus quiz candidate uniqueness, app/manifest behaviour and publication acceptance are
outside this review; no validator or generator ran.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **NEEDS FIX** (three low-severity missing guards); cross-file integration
**CLEAN**. Linguistic correctness was outside this facet beyond observed inconsistencies.

- Q1 (low; medium confidence), `すまない.md` quiz_exclusions and `悪い.md` (title «плохой; виноватый»): the new すまない
  title «извини, виноват; …» contains «виноват», and the 悪い card teaches 悪いね as «Извини за это»; neither side declares
  the pair. Remedy: append 悪い to すまない's list.
- Q2 (low; low-medium confidence), `おじゃまします.md` quiz_exclusions: «простите за беспокойство (входя к кому-либо)» and
  すまない «…прости за хлопоты» are both "sorry for the trouble" apologies; neither side declares the pair. Remedy: append
  すまない to おじゃまします's list (or the reverse).
- Q3 (low; low confidence), `言付ける.md` and `言い付ける.md` quiz_exclusions: 頼む «просить; поручать» shares «поручать»
  with 言付ける «…поручать доставку (вещи)» and overlaps 言い付ける «велеть (сделать что-либо)»; 依頼 «просьба;
  поручение» likewise. Remedy: append 頼む to both lists.

The report cites line 8 for these quiz_exclusions; in the committed cards the field is on line 9.

What the reviewer confirmed:
- Front matter equals EN for all 30 cards except the title and the RU-added exclusions; heading counts and section order
  equal EN; all EN exclusions are retained (慰める has none in EN).
- Link sets equal EN except where the RU target is absent (the word cards 悔やむ and 敬語 and the kanji cards 訳, 溶 and
  測, left as plain text) and the one RU-only link 言付ける → 言い付ける, "acceptable and helpful"; no broken link in any
  RU kanji, word or article file; no EN-link count mismatch.
- Each navigation diff changes only link brackets and hrefs at EN positions, with EN's path forms (9 occurrences in 7
  files), and the glosses beside the new titles do not mislead. `manifest.json` equals an in-memory rebuild; the intake's
  37 payload paths equal the 30 cards and 7 navigation files.
- アイデア and アイディア carry identical titles, which are deduplicated, and the pair is not declared, as in EN.

Optional: none. Limits: no title-screen output was read; dictionary senses were cited from memory; linguistic correctness
is outside this facet.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (おじゃまします, ごめん, 言い付ける, 親類 and 覗く; no actionable defect in the other
25 cards); scoped coverage **CLEAN** for all 30.

- C237-1 (medium; high confidence), `覗く.md:4` (also lines 12 and 26): the co-equal title gloss «подглядывать» means
  looking secretly, but the card's note at line 34 says «тайком» is not obligatory and the examples are a hole, a
  bookstore drop-in and a ticket sticking out. Evidence: JMdict 1470840 senses 1, 3 and 5; Daijisen sense 4 is the secret
  look. Remedy: title and heading «заглядывать (в отверстие, ненадолго); выглядывать (показываться частично)»; line 26
  «заглядывает ли кто-то».
- C237-2 (medium; high confidence), `言い付ける.md:21`: «Я рассказал учителю о проделке друга» is neutral narration for the
  tell-on example; JMdict 1264230 sense 2 is telling on someone. Remedy: «— Я наябедничал учителю о проделке друга.»
- C237-3 (medium; high confidence), `ごめん.md:4` (also lines 12, 16 and 19): the title segment «нет уж, увольте» can merge
  with the «освобождение от должности» sense taught at lines 27–30 and with «уволить» 'dismiss'. Remedy: title «прости
  (по-свойски); мне этого не надо (отказ)», with a reworded example and an added note.
- C237-4 (medium; high confidence), `親類.md:20`: «Неподалёку живёт наш родственник» adds «наш», absent from the Japanese
  and EN "A relative lives nearby." Remedy: «— Неподалёку живёт родственник.»
- C237-5 (medium; high confidence), `おじゃまします.md:4` (also lines 12 and 16): «я вхожу» reads as the ordinary first person
  of 入る rather than the formula said while entering. Remedy: title and heading «простите за беспокойство (входя к
  кому-либо)»; line 16 ««простите за беспокойство» — формула, которую говорят, входя.»

Optional: 言付ける.md:19 «Я передал через друга» can read as completed delivery; 観測.md:21 «прогноз» is 予報's headword;
応ずる.md:37 «サ変» is unexplained; 見送る.md:40 «в долгий ящик» is stronger than deferring; すまない.md:4 «виноват» is a
guilt-flavoured apology. It also noted, without raising them: 観念.md:21 «никакого» is idiomatic; the identical
アイデア/アイディア titles are correct for one lexeme; お待ちどおさま does not exclude お待たせしました, although the reverse
exclusion exists; the titles of 応ずる, 解散, 観測 and 見送る are long (82–85 characters) but within the existing range
(恐縮 88, パス 84); 慰める «утешал» does not overclaim; the unlinked 悔やむ, 敬語, 溶かす, 小指 and 励ます and the kanji 訳,
溶 and 測 read naturally; link parity shows no lost EN link; and the おじゃまします formation sentence needs no English
metadata label. Limits: the Jisho API and a Daijisen snippet for 覗く; no native-speaker or learning-effectiveness claim;
quiz metadata was not scored.

## Exclusion classification

All 171 EN exclusion entries (29 lists) are retained in EN order; 慰める has none in EN. Nineteen of them lie inside the
batch. At the candidate, eight direct, one-sided entries were added on six new cards, all appended at the end of their
lists (慰める's on a new `quiz_exclusions` line); none targets a batch word.

| Entries | Consistency reviewer |
|---|---|
| 回答→応対, 解散→終了, 観測→読み, 親類→親戚 (4) | Required (回答→応対 "required (title level)") |
| 解散→閉会 (1) | Conservative-to-required |
| 見送る→省く, 見送る→飛ばす (2) | Required at title level, conservative dictionary-wise |
| 慰める→落ち着く (1) | Conservative (real Russian-root overlap, necessity unestablished) |

The author and the coordinator classed 親類→親戚, 見送る→省く and 見送る→飛ばす as required and the other five as
conservative; the coordinator accepted all eight as reported. The reviewer found "No unjustified entries found; none
guards a contrast the article teaches." and raised the three missing guards Q1–Q3 above. The correctness reviewer
checked the RU-added exclusions only as additive metadata, and the comprehensibility reviewer treated the お待ちどおさま
declaration and the identical アイデア/アイディア titles as quiz matters outside its facets.

Reconciliation, the coordinator's dispositions, the fixes and the final verdicts are in
`237-words-batch-76-recheck-001.md`.
