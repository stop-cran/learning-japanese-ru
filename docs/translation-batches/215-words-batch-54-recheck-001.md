# Batch 215 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `2ae93fbb0633b03857d1ae4bade78a29dccba880` | `f3c26c5c643abd893a8e005cbc9d79d84a255f74` | Initial review snapshot: the signed candidate, pushed before review. |
| `3f9f8ea4b71d0adbe6700f03ef13eec12f022c4c` | `4a59c9fb3c5ce509b0db508a26c885ea7dda9b3c` | Fix (final candidate). It covers the correctness finding, the two comprehensibility findings, the accepted consistency and comprehensibility optional notes and the intake refresh. It was signed and pushed before the rechecks. |

The fix changed four word files and regenerated `manifest.json` (`contentVersion` `9f8d5901ab1c2598`, 4,569 entries) and the
intake:
- `化粧` (line 28): «Онные чтения здесь — け + しょう» instead of «Чтения здесь — け + しょう» (correctness F1).
  - The hiragana and the instruction to learn け + しょう as a whole are unchanged.
  - Digital Daijisen 化 (Kotobank) lists ケ among its on readings and gives 化粧 under ケ. «Онное чтение / онные
    чтения» is the deck's established term (65 occurrences).
- `博士` (line 17): «(PhD)» is removed. The sentence now reads «…доктора — обладателя докторской степени — или
  используют слово как титул «доктор».» (comprehensibility 1).
- `単に` (lines 4, 12, 16): title and H1 «просто (не более того); всего лишь» instead of «просто (не более того);
  исключительно»; the meaning line «просто, всего лишь, только» instead of «просто, всего лишь, исключительно»
  (comprehensibility 2, modified).
  - EN gives two title glosses, "merely; simply", so «всего лишь» renders "merely".
  - «только» on the meaning line keeps JMdict's "only; solely" without the ambiguous «исключительно».
  - The reviewer had proposed a single-gloss title, «просто (не более того)».
- `単に` (line 9): `quiz_exclusions: [だけ, ばかり]` (the consistency optional note, adopted as two conservative guards).
  - JMdict 1417030 glosses 単に "simply; merely; only; solely". だけ «только; столько, сколько» and ばかり «одно лишь» are
    defensible answers for it, and the new title brings them closer.
  - The coordinator's title screen after the edit found the exact segment «всего лишь» only in 単なる. That pair is
    already excluded by 単なる→単に. The stem hits (прост, более, всего) are pre-existing or false friends, such as まず
    «прежде всего» and 以内 «не более».
- `共同` (lines 32–33): the readings of 協力 and 一緒 are now in full-width parentheses, `（きょうりょく）` and
  `（いっしょ）`, as elsewhere in the batch (the comprehensibility optional note).
- The intake note now names the fixed cards, and the four candidate hashes were refreshed.

Limit L1 (単位 «зачётная единица») was not a content change. The coordinator kept the term and gave the reviewers
normative evidence:
- Order No. 245 of the Russian Ministry of Science and Higher Education, 6 April 2021
  (https://base.garant.ru/402618156/53f89421bbdaf741eb2d1ecc4ddb4c33/). Paragraph 15 measures the workload of an
  educational programme in зачётные единицы; paragraph 16 states that the institution sets the unit's size.
- The encyclopedia article «Зачётная единица трудоёмкости».

The recheck asked whether this evidence closes L1.

Net change from the candidate: one retitle with two added exclusions (単に), one wording fix (化粧), one English abbreviation
removed (博士) and reading-format parentheses (共同). No Japanese example, reading or EN exclusion changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, in the order correctness, consistency, comprehensibility. Each reviewer appended to its own report
file, which stayed in its session context. Each recheck message gave it:
- the fix commit, its parent and the read-only rules;
- the actual content diff from `2ae93fb` to `3f9f8ea` inline;
- the coordinator's evidence for every change, including the L1 normative evidence;
- the declined items from all three facets with their reasons, without the other reviewers' reports;
- the coordinator's disposition of each of its own findings and optional notes.

All rechecks reviewed the final candidate `3f9f8ea`; no second fix was needed. The recheck messages forbade running
`tools/build_manifest.py` or any other generator, and all three recheck sections state that none was run.

The correctness and consistency reviewers ran `tools/validate.py` (0 errors); the comprehensibility recheck does not report a
validator run. The consistency reviewer's validator run left an untracked `tools/__pycache__` directory of seven bytecode
files. The coordinator deleted it, changing no tracked file, before the next recheck. After every recheck the coordinator
confirmed that HEAD was unchanged and that `git status --porcelain --ignored` was empty, after that removal where it applied.

### Round 1 (`3f9f8ea`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer checked the complete four-card diff and read all four revised cards in full, with the relevant EN passages and the meanings of the guard targets. F1 is resolved: 化粧 restores «Онные чтения» and keeps the hiragana and the pronunciation warning. L1 is resolved substantively, keeping a qualified source-type limit: the reviewer read Order No. 245, paragraphs 15–16, which use зачётные единицы for programme workload and define the unit in hours. With the JMdict credit sense, this closes the linguistic uncertainty. It does not supply a dictionary headword or establish numerical equivalence with Japanese credits, and the card claims none. For 単に it inspected JMdict via the Jisho API, Digital Daijisen 単に on Kotobank (restriction to the named matter) and Kuznetsov «всего лишь» ("only this and nothing more"); removing «исключительно» loses no selected sense. JMdict's first senses of 丈 (だけ) and 許り (ばかり) justify the two conservative guards, which assert no syntactic interchangeability. 博士 keeps the degree-holder, colloquial, title and expert senses. 共同's parentheses attach きょうりょく and いっしょ correctly. Correctness and scoped coverage are **CLEAN**. |
| Consistency | The reviewer confirmed that the commit changes only the four word files, the manifest and the intake, and that all four manifest SHA-256 hashes match the file bytes. Scanning every RU word title, it found the exact segment «всего лишь» only in 単なる, which the required 単なる→単に pair covers. «просто» appears in no other title, and 簡単 and 単純 share only the stem «прост-», which part of speech and the card's own contrast separate. The だけ/ばかり guards resolve its optional note. It withdrew its other two optional notes (協力–援助/世話 and 化学–科学) after the decline. Its RU-added exclusion classes are final. 化粧, 博士 and 共同 show no consistency or link regression; 共同's links to 協力 and 一緒 are unchanged, and the （…） readings match the house style. It judged L1 closed by the normative act, noting only that no dictionary entry was found. `tools/validate.py` reported 0 errors. Consistency, scoped coverage and quiz safety are **CLEAN**, with no new findings. |
| Comprehensibility | The reviewer reread the four changed passages. Finding 1 is resolved: 博士 no longer contains «(PhD)», and the sentence still separates the colloquial doctorate use from «знаток». Finding 2 is resolved: «всего лишь» and «только» are minimizing, not the "exceptionally" sense in 名人, and the parenthetical still separates «просто» from «нетрудно». The shared «всего лишь» with 単なる is an excluded pair, not a new learner ambiguity. 共同's （…） readings match the house style. 化粧's «Онные чтения» keeps the practical point; «онные» is established course vocabulary. On L1 it read Order No. 245, paragraphs 15–16, and the encyclopedia article (Ruwiki returned 401, so it used Wikipedia). It judged that the missing bilingual dictionary headword is not a learner defect, so L1 is closed for its facets. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 化粧 drops EN's on-reading classification | **Resolved** | `化粧.md:28`; Digital Daijisen 化. Severity unchanged (minor). |
| Correctness L1: no exact Russian dictionary headword for 単位 «зачётная единица» | **Resolved** substantively, with a retained source-type limit | Order No. 245 (6 April 2021), paragraphs 15–16; Wikipedia «Зачётная единица трудоёмкости»; JMdict 単位 sense 3. All three rechecks accepted the normative evidence. The term is unchanged. No dictionary headword was found, and the card claims no numerical equivalence. |
| Consistency | **No findings** | Review 001 reported none; the recheck found no regression. |
| Consistency optional: 単に–だけ/ばかり | **Resolved** (adopted as conservative guards) | `単に.md:9`; JMdict 単に 1417030, 丈 and 許り first senses; the correctness and consistency rechecks. |
| Consistency optional: 協力–援助/世話; 化学–科学 | **Withdrawn** | 協力 shares no title segment or stem with «помощь», and its title avoids «содействие». «химия» and «наука» are not mutually defensible answers, and the 化学 card already contrasts the homophones. The reviewer withdrew both in its recheck. |
| Consistency limit: RU `kanji/参.md` has an extra link to 参る | **No action** | Pre-existing and outside this batch's diff. |
| Comprehensibility 1: 博士 keeps the English abbreviation «(PhD)» | **Resolved** | `博士.md:17`; Jisho/JMdict 博士 sense 2. |
| Comprehensibility 2: 単に title and gloss «исключительно» | **Resolved** (modified wording) | `単に.md:4,12,16`; JMdict 単に; Kuznetsov «всего лишь». The title keeps two glosses, following EN "merely; simply", instead of the proposed single gloss. |
| Comprehensibility optional: 共同 readings without parentheses | **Resolved** | `共同.md:32–33`. |
| Comprehensibility optional: 名人 «знатока» echoes 博士's «знаток» | **Optional, not adopted** | Label hygiene only: 博士 already excludes 名人, and 名人's examples say «мастер». |
| Comprehensibility optional: «словарь помечает» instead of "JMdict помечает" in 博士 | **Optional, not adopted** | The named, linked dictionary is more precise, and the same phrasing occurs in 35 places in 34 published cards. |
| Comprehensibility notes: 原 «ручью», 叱る's 𠮟る note, 博士's reading notes, 可能 «Можно ли» | **No action** | The reviewer itself judged them not to be defects. |
| Exclusion classification | **Reviewer differs from author on 3 entries** | The author called 博物館→美術館, 及ぼす→影響 and 単なる→単に conservative; the consistency reviewer rated them required. The reviewer's classification is recorded as final. |

Cross-batch note: links to absent targets stay plain. The next batch includes 加わる and 分ける and will restore the links to
them from 参加 and 合わせる; no other link is held.

## Final exclusion set

All 9 EN exclusion entries (8 lists) are retained. Seven direct, one-sided entries are added on six new cards:

- Required (4): 原→野, 博物館→美術館, 及ぼす→影響, 単なる→単に.
- Conservative (3): 叱る→注意, 単に→だけ, 単に→ばかり.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the L1 evidence; 化粧 is also fixed.
- Scoped coverage: **CLEAN** after the fix (化粧).
- Comprehensibility: **CLEAN** after the fixes (博士, 単に).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** throughout, including the two 単に guards added in the fix. This covers the reviewed batch and the
  directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the cards needed to judge them. The unchanged cards rest on review
  001's full reading.
- No exact Russian dictionary headword for «зачётная единица» was found. The term rests on the normative act and the
  encyclopedia article.
- The consistency reviewer did not re-fetch dictionaries, rerun `link_parity.py` or recompute `contentVersion`.
- The comprehensibility reviewer did not reopen Jisho in this pass, did not rerun the title screen and did not reread the
  other 26 cards.
- The collocation frequency of «плотный макияж» was not established.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
