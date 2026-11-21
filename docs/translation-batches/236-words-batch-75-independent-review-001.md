# Batch 236 — independent review 001

## Snapshot and scope

- Reviewed commit: `122b0192996f8c54236941b802ee5b10a19d06fd` (tree `1fcb849e038d197467585c2ee4f298c482a359c5`), branch
  `full-ru-236-words-75`, parent `ad5fc9b`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 235 candidate `75b2616d78a93d0655a2e7494abb6c1f9585ad10`.
    Before copying, the coordinator's candidate script checked two things: that the six navigation files edited there
    (`kanji/争.md`, `kanji/圧.md`, `kanji/有.md`, `kanji/言.md`, `kanji/難.md` and `words/戦う.md`) were unchanged between
    `75b2616` and the candidate's parent `ad5fc9b`, and that none of the 30 new cards existed in the primary checkout. It
    also checked that the branch, HEAD and `origin/main` were the expected ones and that the tree was clean.
  - The script byte-compared the 36 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 36 batch paths plus `manifest.json`. Its byte scan of all
    36 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 36 committed
    blobs at `122b019` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from Batch 235; all eight restored links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made no content edits: no title edit, no exclusion
    append and no held link; the 36 lane files were copied unchanged. Its adjudication record states:
    - "Screens rerun by the coordinator with RU_ROOT = lane: `word_title_screen.py` over the 30 words reports 0
      unguarded exact segments (output `b236-lane-screen.txt`, 52 guarded OK lines); `validate.py` 0 errors; `navonly.py
      HEAD --only` over kanji/争, 圧, 有, 言, 難 and words/戦う reports 6 files, 8 links added, 0 problems.";
    - for `link_parity.py` over the 36 paths: "RU-only links 謙虚:32 → 謙遜, 胡椒:32 → 塩, 削除:33 → 追加, 詰まる:38 → 込む.
      Each target is mentioned as a substantive comparison in the frozen EN card (plain text there) and has an existing
      RU card; accepted under the B222 precedent.";
    - "kanji/言.md EXTRA 言葉 is pre-existing at 75b2616 (same output with RU_ROOT = primary), not a B236 change.";
    - "貝 LOST トップ, 頂上: the EN paragraph ("The quiz keeps this written form apart from トップ and 頂上, whose English
      labels contain bare 'top'…") is an English-label safeguard with no Russian counterpart (ばい «волчок» vs «верх;
      лидирующая позиция» / «вершина»). Dropped under the translation-boundary rule (drop English-dependent comparisons,
      keep the Japanese rule): the Japanese facts kept are the separate ばい noun, its usual katakana spelling, its
      spinning-top sense and that ばい is not a general reading of かい. Both EN exclusions and the footer JMdict IDs
      1085030/1430220 are retained (B228 footer rule). Accepted; hand to the reviewers as a deliberate drop to check.";
    - "Titles compared with EN one by one; no coordinator title edit.";
    - "RU-added exclusions accepted as reported: 14 pairs; required 話しかける→扱う («обращаться») and 縮む→座る («садиться»);
      conservative 論ずる→検討/考慮/取り上げる, 謎謎→不思議, 有難い→御礼/礼/ありがとう, 縮む→乗る, 詰まる→密, 言い出す→勧める,
      話し中→会話/話.";
    - "Unverified Russian usage to hand to the reviewers: register of «испрашивать» in the 請う title (bookish; matches
      the formal/literary register of 請う, but unconfirmed as learner-friendly) and whether «ракушка» adequately covers 貝
      in both the animal and the shell sense.";
    - "Pending checks done after the B235 publication (main c9c13e3, record ad5fc9b): none of the 36 B236 paths links to
      or mentions a B235 card changed by fix 930e9f3 (跳ねる, 貸し出し, 転がる, 賞品, 賞金, 交差, 足袋, 赤道) or quotes any
      of their replaced wording; `b236_cand.ps1` phase 1 on the published tree: the 6 nav files are identical between the
      lane base 75b2616 and the B235 publication record, the 36 lane files were copied byte-identically, validate 0
      errors, unit tests OK, budget OK, title screen 0 unguarded exact segments, navonly 6 files / 8 links / 0 problems,
      and link_parity reports the same RU-only links, the pre-existing 言→言葉 extra and the 貝 drop as above; manifest
      5,199 entries.";
    - "Process incident found after the B236 candidate (coordinator check while adjudicating B237): the session's EN
      worktree (C:\Users\romanko\repos\copilot-worktrees\learning-japanese\romanko-microsoft-super-spoon, EN commit
      8563b6fd) had all 30 B236 word files `words/<word>.md` rewritten at 6:31:12 PM, during the B236 author run, with LF
      line endings and content identical to the EN HEAD after CRLF/LF normalization (checked byte-wise for all 30). The
      coordinator restored them with `git checkout`; no RU file and no EN commit was affected."

    The committed manifest records 5,199 entries (5,194 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The consistency
    reviewer also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 6 files with 8 restored navigation links (the kanji cards 争, 圧, 有, 言 and 難 and the word card 戦う);
    - `manifest.json` (`contentVersion` `665aa4623102be73`, 5,199 entries);
    - the intake, whose note reads "B236 30-card adaptation with eight navigation-only link restorations in six existing
      files; candidate before blind review."
- Published baseline recorded in the intake: `c9c13e32aeeb31752bddc152d7e69e674f7a3a4e` (Batch 235 merge). Parent
  `ad5fc9b` adds only the Batch 235 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests (the authoring worktree run reported 124 tests);
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 6 files (8 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen: no unguarded exact title-segment overlap (52 `OK` lines for pairs already guarded by an exclusion and
    434 stem-only `!!` lines);
  - link parity: no EN link lost where the RU target exists, apart from the deliberate 貝 drop of トップ and 頂上; the only
    RU-only links added by the batch are 謙虚:32 → 謙遜, 胡椒:32 → 塩, 削除:33 → 追加 and 詰まる:38 → 込む; the kanji card
    言 keeps its pre-existing RU-only links to 言葉 (lines 33 and 42), present at the published baseline.
- Common sample: all three reviewers read all 30 new word cards in full. The correctness and comprehensibility reviewers
  read each card against its complete frozen EN original. The consistency reviewer compared the EN originals mechanically
  and by eye, read the six navigation-file diffs, and checked the intake and manifest.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file), all linked word-card meaning sections and
    linked kanji meaning excerpts (not a full review of those older cards), and compared metadata programmatically. Its
    report does not mention the navigation-file diffs.
  - Inspected the JMdict XML entry for every cited seven-digit JMdict ID, including search-only flags and separate
    homonyms; Jisho requests partly returned HTTP 429, so the direct JMdict XML covered every cited entry instead.
  - Japanese sources beyond JMdict: Digital Daijisen on Weblio (講師, 謙遜, 謎謎, 論ずる, 請う, 調節, 調整, 胡椒, 調味料,
    誓う, 縮小, 削る, 削除, 縮める, 縮れる and 縮む), Kotobank (貝), Seisenban (恐縮 definition 2 and 課税), Wiktionary and
    Kanjipedia (請う) and KANJIDIC2 (kanjiapi returned HTTP 403).
  - Russian sources: Kuznetsov on gramota.ru (испрашивать, ракушка, наладка, подстройка, свёртывать, курчавиться, опущение,
    скромничать, смирение, наставление, сморщиваться, благодарный, сокращение, перец and клясться) and the gufo.me entry
    for клясть; scoped meaning checks, not frequency claims.
  - Ran no generator and no validator.
- Consistency review scope:
  - Read all 30 RU cards in full and compared them mechanically and by eye with the frozen EN cards; read the six
    navigation diffs (争, 圧, 有, 言, 難 and 戦う); checked `manifest.json` and the intake JSON; ran the validator (0
    errors); screened the titles against all RU titles.
  - Checked that the intake's 36 paths equal the diff; it noted that 118 strokes manifest hashes differ from the working
    tree (unchanged by this commit, probably a line-ending artifact, pre-existing, out of scope).
  - Performed no dictionary re-verification ("JMdict not checked") and did not assess translation quality.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN; partial reads only of the near-synonym titles and the openings of 頼む, 感謝 and
    戦う; read the title, glossary and report-contract rules. "Kanji diffs and the intake JSON were not reviewed."
  - Used the JMdict IDs cited on the cards, plus JapanDict for 1264080 and Ozhegov/Ushakov for смирение and скромничать;
    the JMdict database was not re-opened entry by entry. It records no validator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; the correctness and comprehensibility reports say their model is not independently verifiable in the
  session, and the consistency report makes no statement about its model.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. The correctness
  report records HEAD verified as `122b019` with an empty `git status --porcelain`; the consistency report records
  `122b019` with a clean tree at start and end (it removed a Python bytecode cache directory under `tools/` that it had
  created by accident); the comprehensibility report records an empty `git status --porcelain` with HEAD matching the
  candidate and no uncommitted changes. No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No reviewer reported running a generator: the correctness report says that no generators or
  validators ran and that only its report was deliberately written; the consistency report records only the validator
  run; the comprehensibility report's initial section records no validator or generator run. No tracked repository file
  was changed.
- Full blind reports:
  - `236-words-batch-75-review-correctness-001.md`
  - `236-words-batch-75-review-consistency-001.md`
  - `236-words-batch-75-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The consistency brief made the intake record's path list the single exception, for its path check. The correctness
  report says "Excluded publication/draft records not read." The consistency report makes no statement about unread
  materials; it records checking the intake JSON. The comprehensibility report makes no statement about unread
  materials; it says the kanji diffs and the intake JSON were not reviewed.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for 誓う and 話し合い; scoped coverage **NEEDS FIX** for 請う (title); no other
actionable defect established in the 30-card scope. Russian comprehensibility and whole-pool quiz quality are outside
these verdicts.

- C236-01 (medium, correctness; high confidence), `誓う.md:41–42`: «Русское “клясться” в разговорной речи может означать
  и “браниться, проклинать”» transfers English "swear" polysemy to a different Russian lemma; Kuznetsov defines клясться
  as giving an oath or emphatically promising, while the curse/reproach meanings belong to клясть. This teaches an
  erroneous Russian/Japanese distinction. Remedy: remove the English-only contrast, or replace both sentences with
  «誓う означает давать клятву или обет, а не браниться». Evidence: Kuznetsov on gramota.ru (клясться); gufo.me
    (клясть); JMdict 1381210 sense 1.
- C236-02 (medium, scoped coverage; high confidence), `請う.md:4,12`: the title «просить, испрашивать (наставления,
  прощения)» drops the EN title's "invite" sense, which RU still teaches at lines 16, 29, 37 and 42, and the qualifier
  confines the title to two request objects while EN covers requests generally. Remedy: «просить, умолять; приглашать»
  in front matter and heading, retaining the formal construction explanation in the body. Evidence: frozen EN
  `words/請う.md:4,16,38–48`; JMdict 1592920 sense 1 ("to beg; to ask; to request; to invite").
- C236-03 (low, correctness; high confidence), `話し合い.md:19`: «Завтра мы всей семьёй всё обсудим» adds an all-inclusive
  object ("everything") absent from 明日、家族で話し合いをします and EN "We will have a family discussion tomorrow."; this
  is a translation-content addition, not an objection to rendering the noun with a Russian verb. Remedy: «Завтра мы
  обсудим это всей семьёй». Evidence: frozen EN `words/話し合い.md:19`; JMdict 1600910 sense 1.

What the reviewer confirmed:
- Programmatic comparison confirmed all original stable metadata; the changes are additive quiz exclusions only. All
  relative links resolve, and the four new comparison links (謙虚→謙遜, 胡椒→塩, 削除→追加 and 詰まる→込む) accurately
  describe their targets.
- Japanese bullet examples and kana lines match EN exactly after normalizing outer Markdown/layout punctuation; no
  Japanese tense, polarity or transitivity defect was established. 有難い's «Я благодарен» preserves an idiomatic gratitude
  utterance.
- 貝's removed トップ/頂上 link sentences serve only EN-label safeguards, and their omission is permitted by the supplied
  contract; the separate ばい senses, the restriction against treating ばい as the card's general reading, the exclusions
  and the bibliography remain. «ракушка» need not itself mean the animal, because the title separately covers a living
  mollusc and an empty shell.
- The Kuznetsov/Gramota entries for the flagged words (among them испрашивать, bookish) establish the flagged uses, not
  frequency or universal equivalence; no defect was established merely from uncommon vocabulary.

Optional: none. Limits: current dictionary entries are corroboration, not a byte-identical reproduction of the author's
frozen dictionary snapshot; Jisho returned HTTP 429 and kanjiapi HTTP 403 for some requests (direct JMdict XML and
KANJIDIC2 used instead); no full kanji-front-matter/radical, repository-wide quiz, app/native-speaker acceptance or
historical-etymology audit; no generators or validators ran; the sitting-state/onset wording in 縮める was considered
without an actionable defect.

### Consistency and quiz safety

Verdicts: consistency **NEEDS FIX** (F1 only); quiz safety **CLEAN**; navigation restorations, `manifest.json` and intake
**CLEAN**. Comprehensibility was not assigned to this review, and translation quality was not assessed.

- F1 (low-medium), `貝.md`: EN links トップ.md and 頂上.md in two sentences explaining why they are excluded
  (English-label safeguard); RU drops the sentences and links although both targets exist, and the exclusions [トップ,
  頂上] remain in front matter with no learner-visible reason. Remedy: add a short sentence linking both and saying they
  are kept apart only as a safeguard, or accept the omission since Russian labels do not collide.
- F2 (low, nonblocking): the 謎謎→不思議 guard is an unnecessary over-guard (noun vs na-adjective, titles already differ;
  不思議 already guards 謎).
- F3 (optional): the in-batch pair 話し合い–話し中 (both «разговор») is unguarded, inconsistent with the author's own
  話し中→会話/話 reasoning.

What the reviewer confirmed:
- Front matter equals EN except title and quiz_exclusions; all EN guards are kept in order; exactly 14 RU additions.
  Footers and headings match.
- All EN links are present where RU targets exist (apart from F1); the four RU-only links (謙虚→謙遜, 胡椒→塩, 削除→追加 and
  詰まる→込む) sit in substantive comparisons and are acceptable. Nonexistent kanji cards are plain text.
- Navigation diffs touch only link brackets and hrefs at EN positions. Manifest hashes of words and kanji and the intake
  candidate hashes match; the intake's 36 paths equal the diff.

Optional (nonblocking): long titles (論ずる 77, 恐縮 76 characters) are within the repository's existing range (パス 84);
there is no length rule. Limits: semantic judgments are title/body-based; JMdict not checked; 118 strokes hashes differ
between the working tree and the manifest (unchanged by this commit, probably a line-ending artifact, pre-existing, out
of scope); translation quality not assessed.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (twelve items in 講師, 有難い, 恐縮, 謙虚, 謙遜, 話し合い, 争う, 言い出す, 圧縮/
削除/縮める/削る, 請う/削る, 請う and 話し中); scoped coverage **CLEAN**.

- C1 (high; high confidence), `講師.md:21`: «преподаватель» is the quiz title of 教師 («преподаватель; педагог»), used here
  for 大学の講師, while lines 34 and 41 say 教師 is the broader job; the contrast is taught backwards. Remedy: «Она лектор в
  университете.» Evidence: 教師's title; EN "university lecturer"; JMdict 1282280, cited on the card.
- C2 (high; high confidence), `有難い.md:20`: lines 20–21 use the person frame that lines 23–24 reject; line 20 copies
  感謝.md:19, and line 21 adds «очень» (no とても) and «признателен», 感謝's title family; «желанный» never appears.
  Remedy: line 20 «Как кстати, что вы мне помогли.»; line 21 «Когда я занят, получить помощь — это то, что я ценю.»
  Evidence: lines 23–24; 感謝.md:19; EN "something I appreciate".
- C3 (medium; high confidence), `恐縮.md:4`: the qualifier «(от чужой любезности или похвалы)» drops 恐縮ですが, taught at
  lines 23 and 26, and line 22 «Я очень признателен…» is plain gratitude, not the obligation or awkwardness of JMdict
  1236740 senses 1–2. Remedy: title and H1 «неловкая признательность; смущение (от любезности, похвалы или беспокойства)»;
  line 22 «За ваше любезное письмо я вам признателен и мне неловко.» Evidence: JMdict 1236740; EN title "feeling obliged;
  apologetic gratitude".
- C4 (medium; high confidence), `謙虚.md:21`: «со смирением» contradicts line 40 (not agreeing with every claim); Ozhegov
  defines смирение as readiness to submit to another's will. Remedy: «Я скромно принимаю совет учителя.» Evidence:
  Ozhegov; line 40; EN "with humility".
- C5 (medium; high confidence), `謙遜.md:20`: «он скромничает» for 謙遜しています suggests excessive or ironic modesty
  (Ozhegov; Ushakov), while line 42 says it is not necessarily insincere; line 21 is acceptable. Remedy, line 20 only:
  «Даже когда его хвалят, он принижает свои заслуги.» Evidence: Ozhegov and Ushakov; line 42; EN "remains modest".
- C6 (medium; high confidence), `話し合い.md:19`: «всё обсудим» verbalises the noun 話し合いをします and adds «всё». Remedy:
  «Завтра мы всей семьёй проведём обсуждение.» Evidence: the Japanese example; EN "have a family discussion".
- C7 (medium; high confidence), `争う.md:19`: «борются» is the quiz verb of 戦う («сражаться; бороться»), while this title is
  «соперничать» and EN has "competing"; not a false sense, but the example teaches 戦う's answer. Remedy: «Две команды
  соперничают за победу в чемпионате.» Evidence: 戦う's title; EN; JMdict 1400620, cited on the card.
- C8 (medium; high confidence), `言い出す.md:19`: «заявил» for 急に…と言い出しました loses the onset in line 16. Remedy: «Он
  вдруг заговорил о том, что хочет домой.» Evidence: JMdict 1264080 senses 1–2; JapanDict 言い出す; EN "started saying".
- C9 (medium; high confidence), `圧縮.md:41`, `削除.md:38`, `縮める.md:44`, `削る.md:43`: «исходный список» is author-facing;
  the learner has no such list. Remedy: delete or rephrase each pointer while keeping the contrasts. Evidence: the
  matching EN sentences name "the source list" / "the legacy source".
- C10 (low; high confidence), `請う.md:42`, `削る.md:25`: «соответствие уровню N2» and «уровень N2 не присвоен» are
  authoring status, and N2 is unexplained Latin script. Remedy: rephrase both without the level status, keeping the extra
  senses. Evidence: the glossary; N5–N1 is a JLPT level, not an authoring flag.
- C11 (medium; medium-high confidence), `請う.md:20`: «Я попросил учителя о наставлении» copies 頼む.md:20's frame and uses
  the everyday verb, although line 47 says the construction is more formal than お願い. Remedy: «Я обратился к учителю за
  наставлением.»; in line 16, after «испрашивать», add «(книжное «официально просить»)». Evidence: 頼む.md:20; lines 16
  and 47; JMdict 1592920, cited on the card.
- C12 (medium; medium-high confidence), `話し中.md:4`: both segments are non-nominal for a tagged noun (predicative
  «занято» and the clause «идёт разговор»); not a quiz collision. Remedy: title and H1 «занятая линия; идущий разговор».
  Evidence: tags include noun.

Optional: 謎謎.md:38 «пазл» is not tied to line 33's «パズル — головоломка»; 調整.md:4 «наладка» is narrower than the
schedule example; 誓う.md:21 could drop «друг другу» (EN has no addressee); 論ずる.md:42 «サ変» is unexplained (gloss it or
drop the label). It did not uphold the lost トップ/頂上 links on 貝 (an English-label quiz safeguard; RU titles do not
collide), judged the extra links to 謙遜, 塩, 追加 and 込む helpful, and found no unguarded exact title-segment overlap
(stem hits are false leads). Limits: JMdict IDs are the cards' own citations, plus JapanDict and Ozhegov/Ushakov; other
comparison cards were checked by title; the kanji diffs and the intake JSON were not reviewed; quiz-exclusion symmetry
is outside these facets except where an example uses another card's title.

## Exclusion classification

All 151 EN exclusion entries (29 lists) are retained in EN order; 胡椒 has none in EN. Twenty-three of them lie inside
the batch. At the candidate, fourteen direct, one-sided entries were added on eight new cards, all appended to existing
lists; none targets a batch word.

| Entries | Consistency reviewer |
|---|---|
| 縮む→座る, 話しかける→扱う, 論ずる→検討, 論ずる→考慮, 言い出す→勧める (5) | Required |
| 論ずる→取り上げる, 有難い→御礼/礼/ありがとう, 縮む→乗る, 詰まる→密, 話し中→会話/話 (8) | Conservative/acceptable |
| 謎謎→不思議 (1) | Unnecessary over-guard (F2, low, nonblocking) |

The author and the coordinator classed 話しかける→扱う and 縮む→座る as required and the other twelve as conservative; the
coordinator accepted all fourteen as reported. The reviewer classed three of the coordinator's conservative entries
(論ずる→検討, 論ずる→考慮 and 言い出す→勧める) as required and 謎謎→不思議 as unnecessary (F2), judged declined stem-only
pairs defensible and judged quiz safety CLEAN; it also raised the unguarded in-batch pair 話し合い–話し中 as optional F3.
The correctness reviewer checked the RU-added exclusions only as additive metadata, and the comprehensibility reviewer
treated quiz-exclusion symmetry as outside its facets.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`236-words-batch-75-recheck-001.md`.
