# Batch 245 — independent review 001

## Snapshot and scope

- Reviewed commit: `004903db88a34b30524ca68ffc5b8dfbc085bbfa` (tree `86483e2d7614ce9f762d411eb04dc4c869602984`), branch
  `full-ru-245-words-84`, parent `e73ae1b`. The candidate was signed and pushed before review.
  - The content was authored in the scratch lane `learning-japanese-ru-b245`, whose commit
    `282ea33` ("B245 lane drafts on B242-B244 scratch") sits on `da27b0c`, the Batch 242 to Batch 244 lane drafts on the
    Batch 241 fix `9cf1600` (drafts `7e656bc`, `556daa9` and `fe1dfd3`). The coordinator's candidate script checked that
    the lane was clean at `282ea33` with parent `da27b0c`, that the branch, HEAD~1 and `origin/main` were the expected
    published baseline, that the primary tree, including ignored files, was clean, and that the two navigation files
    edited in the lane were unchanged between `da27b0c` and the lane HEAD.
  - The script copied 32 lane files (the 30 new cards and the navigation files `words/休日.md` and `words/突き当たる.md`),
    then applied one link held from Batch 243 (below), checked that the changed path set was exactly the 33 batch paths
    plus `manifest.json`, and byte-compared the copies with the lane. Its byte scan of the content paths prints any BOM,
    CR or missing final newline rather than stopping; for this record the 33 committed blobs at `004903d` (and again at
    the final fix `1dc38a8`) were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - Held link: `words/編集.md:33` `[社説](社説.md)`. 編集 is a Batch 243 card, and Batch 243's reviewed record left
    編集→社説 plain because 社説 did not exist yet. The candidate script's helper asserted that 社説 occurs once in the
    published file and wrapped «社説（しゃせつ）— редакционная» at that position, a one-line change (EN line 34).
  - After authoring and before the candidate commit, the coordinator made four content edits, to `words/架空.md`,
    `words/祭る.md`, `words/標識.md` and `words/空っぽ.md`; the other 28 lane files were copied unchanged. Its adjudication
    record states:
    - "Scope: all 30 new cards read in full against frozen EN 6af98cb (Russian prose, examples, title/H1, links);
      non-title metadata compared mechanically with EN (b245_cmp.py: all match except two RU-added exclusions 社説→論文
      and 社会科学→自然科学, accepted on the B224 precedent: the bodies contrast exactly these words and the RU titles
      share «статья»/«науки» stems). Link audit: one LOST link 税関→習慣 (the EN "customs/habits" English-homonym note
      was dropped because Russian «таможня» has no "habits" sense — accepted) and one RU-only link 祭日→祝日 (body
      compares the two directly; the RU content-structure rule permits links at substantive comparisons — accepted,
      flagged for consistency review). Nav edits 休日:26 [お休み](おやすみ.md) (mirrors EN line 27) and 突き当たる:30
      [突き当たり](突き当たり.md) accepted. Held for the candidate: 編集.md RU:33 `[社説](社説.md)` (編集 is a B243
      card).";
    - the edits, each with its recorded reason:
      - 架空: "title/H1 «вымышленный; подвесной (натянутый в воздухе)» → «вымышленный; подвесной (о проводах,
        канатах)»" ("the parenthetical read as a definition; the domain gloss is the usual Russian dictionary form for
        overhead lines/cableways; screen: stem-only hits");
      - 祭る: "title/H1 «обожествлять; поклоняться (божеству)» → «помещать в святилище; поклоняться (божеству)»" ("EN
        "enshrine"; «обожествлять» = "deify", which misfits 海の神を祭る (the god is already a god); screen: «поклон»
        stem hit お参り is a direct exclusion, the rest stem noise");
      - 標識: "«…а не история происхождения знаков.» → «…а не история происхождения этих кандзи.»" ("EN "the
        characters"; «знаков» was ambiguous with the card's own "signs" sense");
      - 空っぽ: "«О свободном времени для записи обычно говорят 空き, а не как о сосуде без содержимого.» → «Свободное
        время для записи обычно называют 空き, а не описывают как ёмкость без содержимого.»" ("broken construction
        («говорят … как о»)");
    - accepted as drafted: "Faithful as drafted: 符号 競馬 童話 立ち止まる 突き当たり 空想 空中 移転 秤 私鉄 私立 祝日 お参り
      敬う 神話 神様 先祖 祖先 社説 社会科学 磁石 確率 窓口 税関 祭日."; "おやすみ «выходной день (вежливо); отход ко сну
      (уважительно); спокойной ночи» kept: EN "rest" is rendered through the respectful sleep sense (お休みになる
      example); EN exclusions guard 休み 休日 休暇 休憩 欠席 休む 寝る 眠る 睡眠. Posed to blind review as a title-fit
      question, not a known defect."; "窓口 example «в окошке обслуживания» kept (natural for a counter window).";
    - "Dropped English-only notes accepted: 移転 "demise", 社説 English "leader", 磁石 English "compass" = drawing
      instrument (Russian «компас» never names the drawing tool, «циркуль»), 社会科学 English singular/plural note
      replaced by the corresponding Russian plural note.";
    - "神様 «Бог»/«бог» capitalisation note, 秤 «весы» plural-only usage and 標識 «знак» senses are standard Russian
      usage; gramota.ru verification was rate-limited (HTTP 429) — recorded as unverified, not a defect.";
    - "Kanji links to 符 競 童 税 移 鉄 祭 敬 祝 and word links to 国立/子孫 stay plain because those cards are not
      published yet (restore with their batches).";
    - "Validation after edits (lane): manifest 5,469 files; validate 0 errors; 124 tests OK; budget OK; link parity:
      only the two links above; navonly 2 files / 2 links / 0 problems; diff --check clean; no BOM/CR/missing EOL.
      Title screen 架空/祭る: 0 unguarded exact-segment hits."

    The lane navigation-only count is two files because the 編集 link was held for the candidate script. Fix 1 later
    changed other lines of three of these cards (see the recheck record): 祭る's meaning line and examples (its title is
    unchanged), 空っぽ:33 (the preceding bottle sentence was deleted, so the paragraph now starts with the coordinator's
    sentence), and 標識:45 and 架空:35, which are different lines from the coordinator's edits. The 架空 and 祭る titles
    and the 標識 and 空っぽ sentences above stand as edited.

    The committed manifest records 5,469 entries (5,464 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The
    consistency reviewer also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 3 files with 3 restored navigation links (the word cards 休日, 突き当たる and 編集);
    - `manifest.json` (`contentVersion` `28eee95d59bb55f0`, 5,469 entries);
    - the intake, whose note reads "B245 30-card adaptation with three navigation-only link restorations in three
      existing files; candidate before blind review."

    Against the published baseline the candidate changes 36 files (1,560 insertions, 7 deletions), including the
    parent's publication record; the candidate commit itself changes 35 files (1,480 insertions, 7 deletions).
- Published baseline recorded in the intake: `8e25ff3c9e80dfbb1120677d04bfb6eaa0699ff1` (Batch 244 merge, PR #128).
  Parent `e73ae1b` adds only the Batch 244 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 3 files (3 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b245-cand-screen.txt`, 312 lines): 31 `OK` lines for pairs already guarded by an exclusion and 281
    `!!` lines, all stem-only; it has no exact-segment line. It differs from the lane screen (`b245-screen.txt`, 312
    lines) in three stem-only lines, 空中~広々 «прост», 神様~職人 «масте» and 社説~編集 «редак», where the published titles
    of 広々 and 職人 (Batch 242 fix `872649e`) and 編集 (Batch 243 fix `6aa1bca`) differ from the lane's pre-publication
    copies. No exact-segment line differs;
  - link parity: LOST 税関→習慣 and EXTRA 祭日→祝日, the two links named in the adjudication (the saved lane run over the
    33 paths, `b245-lane-parity.txt`, also lists 編集→社説 as LOST, because the lane did not yet carry the held link).
    For this record link parity was verified again at `1dc38a8`: LOST only 税関→習慣, and EXTRA only 祭日→祝日 and the
    reviewed RU-only link added by fix 1 (`words/祭る.md` → 敬う).
- Common sample: all three reviewers read all 30 new word cards in full against their complete frozen EN originals. The
  consistency reviewer also read all three navigation diffs in full and checked the intake record (path list and payload
  hashes) and the manifest entries; the correctness reviewer "inspected the existing comparison-card titles and the
  changed lines in words/休日.md, words/突き当たる.md and words/編集.md, plus the manifest delta"; the comprehensibility
  reviewer read "the small diffs in words/休日.md, words/突き当たる.md and words/編集.md, and comparison titles (and,
  where the contrast depended on it, bodies)" of the cards named in its scope.
- Correctness review scope:
  - "Model identity not verifiable. All lines of each following RU card AND its frozen EN original were read, including
    metadata, examples/readings, explanations, comparisons and citations", followed by the 30 cards, each a "full RU/EN
    pair".
  - "Inspected all 30 primary cited JMdict entries in the official XML; relevant component readings in official
    KANJIDIC2. Checked consequential usage against actual Daijisen/Seisenban entries, not search snippets."; Russian
    entries on gramota.ru (Kuznetsov) and ru.wiktionary, and Lopatin §180 for Бог/бог.
  - "A read-only comparison confirms identical Japanese sentence and kana-reading contents for all 61 examples."
  - Its limits record "No validator, generator, app or media test was run." and that "Some Jisho/kanji API/Gramota
    requests were throttled or failed; direct official dictionary XML and actual alternative entries supplied the
    consequential evidence."
- Consistency review scope:
  - "all 30 new cards … were read in full (front matter and body). Each was compared with its frozen EN counterpart on
    front matter and link sets; I did not re-read the EN prose line by line. All three navigation diffs (休日, 突き当たる,
    編集) were read in full. I also checked manifest.json, the intake record (paths only), the validator, and a title
    screen of the 30 new titles (run by me) against all RU titles."
  - "validate.py: 0 errors."
  - Its limits record that "Dictionary senses were taken from the cards' own cited JMdict/Daijisen references and my own
    knowledge. I did not re-open the dictionaries.", and that the reverse direction of exclusions "was not required and
    was not checked".
- Comprehensibility review scope:
  - "comprehensibility for an English-free Russian-speaking beginner, and scoped coverage, reviewed separately. Read in
    full, each against its EN original", followed by the 30 cards, plus the comparison titles of "印, 記号, 看板, 合図,
    コード, 気配, 物語, 話, 止まる, 空, からから, 空き, 公立, 休み, 休日, 尊敬, 神, 名人, チャンス".
  - "Ran word_title_screen.py and link_parity.py from the session rutools against this checkout." Its limits record
    that the "title-screen output captured in this session was truncated, so it was a lead only" and that "Jisho
    extracts were opened for JMdict 1295250 (祭る), 1322890 (社説) and 1245380 (空っぽ); other dictionary tags were not
    re-opened". It records no validator or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `ccea6a85-9e5b-4059-8080-f134202419a5`,
  `5b2d689f-b835-48ae-886d-05a5431807da` and `62740252-3a6c-454f-acc7-e81f826a8a47`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model identity
  not verifiable.", the consistency report "Model: not verifiable." and the comprehensibility report "Model: not
  verifiable from the session."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "Initial and final git status --porcelain empty."; the
  consistency report records that `git status --porcelain` "was empty before review" and "is empty again" after it
  deleted the `tools/__pycache__/` its validator run created; the comprehensibility report records that `git status
  --porcelain` "was empty both before and after the review". No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No validator, generator, app or media test was run. No repository
  files, index or HEAD were changed; only this report was written."; the consistency report says "No tracked file was
  touched. I did not run build_manifest.py."; the comprehensibility report says "No repo file was edited." No reviewer
  reported changing a tracked repository file.
- Full blind reports:
  - `245-words-batch-84-review-correctness-001.md`
  - `245-words-batch-84-review-consistency-001.md`
  - `245-words-batch-84-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  As in earlier batches, the consistency brief made one exception: the intake record, "check only that its path list
  matches the candidate's content diff and that it adds no learner content". The consistency report records "its 33
  payload paths equal the 33 words/ files in the content diff (30 new + 3 restored). `candidateRawSha256` equals the
  manifest for each. It has no learner content." The correctness report states "No author/reviewer reports,
  title-screen results, batch/draft/tracking content or numbered scratch checkouts were consulted."; the
  comprehensibility report states "Did not read author reports, FILES review drafts, docs/translation-batches,
  docs/translation-drafts, or translation-tracking.json, and did not read the scratch worktrees."

## Initial verdicts and findings

### Correctness

Verdicts: "correctness NEEDS FIX; scoped coverage NEEDS FIX. Both exceptions concern words/おやすみ.md, F01 below. For
the remaining 29 full pairs and the inspected reused-card changes, no actionable defect was established in either
assigned facet."

- F01 (low; correctness and scoped coverage; confidence high), `words/おやすみ.md:4` (repeated at :12): "the respectful
  noun sense is titled "отход ко сну (уважительно)"". "JMdict 1612680 sense 2 is "sleep; rest", marked sonkeigo. It is
  not restricted to the transition into bed/sleep. EN :4 explicitly includes "rest", and RU :17 itself retains sleep OR
  rest." Remedy: "выходной день (вежливо); сон или отдых (уважительно); спокойной ночи" in the title and H1. Evidence
  also cites Daijisen 御休み sense 2.

What the reviewer confirmed: "word/reading/jlpt/type/kanji/tags match EN throughout. Original quiz exclusions are
retained; 社説 adds 論文 and 社会科学 adds 自然科学."; "Existing-target internal links are retained except the 習慣 link
attached solely to the removed English "customs" contrast. The only additional internal link within the 30 pairs is 祭日
→ 祝日; its comparison is supported by Daijisen 祭日 sense 2."; "The dropped counter/customs/demise/drawing-compass
passages depend on English polysemy. … restoring the disconnected 習慣 link is not required."; Russian «знак»,
«опознавательный», «окошко», «подвесной», «грёза», «полый», «весы», «родоначальник», «приостанавливаться» and
«передовица» checked in actual entries ("None establishes another incorrect gloss"); "Бог/бог adaptation agrees with
Lopatin §180"; the dictionary restrictions support がくう versus かくう, obsolete たちとまる, わたくしりつ/いちりつ, じせき,
祀る and 量る.

Optional: "Outside the assigned facets, 祭る:20–21 could make the dedicated/enshrined-deity meaning clearer, especially by
rendering the first example "Это святилище посвящено богу моря." Existing "почитают/почитаем" is defensible religious
wording, not an established factual defect". Limits: "a review of the specified 30 pairs, not an exhaustive baseline,
application/quiz-pool, native-speaker or learning-effectiveness audit"; JLPT metadata checked for retention only;
throttled Jisho/kanji API/Gramota requests; no validator, generator, app or media test.

### Consistency and quiz safety

Verdicts: "Consistency (format, links, metadata, manifest, navigation files): CLEAN."; "Quiz safety: NEEDS FIX, minor.
One RU-precedent guard is missing (F1, Low)."; "Scoped coverage / cross-file integration: CLEAN."

- F1 (low; confidence medium), `words/童話.md:8`: "童話 «сказка; история для детей» and 歴史 «история» share the Russian
  word «история»." "RU precedent: words/歴史.md already carries the RU-introduced guard `[話]` for the same «история»
  polysemy". Remedy: `quiz_exclusions: [話, 物語, 歴史]`.

What the reviewer confirmed: "Front matter: word/reading/jlpt/type/kanji/tags equal EN on all 30."; "Every RU link
target exists. Dropped EN links are all absent targets", apart from 習慣, where "the EN sentence "customs ≠ habits" is
not carried into the RU 税関. The RU text has no mention to link."; "Only RU-added link: 祭日 → 祝日.md. It exists, is a
mutual pair (祝日 lists 祭日), and is useful navigation. It is acceptable."; "Manifest: sha256 of all 33 changed words/
files equals the manifest entries."; "No generated or unrelated files in the diff: only 35 paths (33 words, manifest,
intake)."; "Navigation restorations are byte-identical to the parent except for the link brackets", at the EN positions
and in the EN path form, each file with "exactly one occurrence"; "The title screen had 0 exact-segment overlaps".

Optional (non-blocking): F2, 社説→評論 («критическая статья»; "If you want to keep the 論文 guard, apply the same
standard"); 上京/移転 and 祭日/祭 "Judged not required"; no exclusion needed on 税関, 秤, 私立 or 磁石; "税関: the RU text
drops the EN sentence about 習慣 (not applicable in Russian: «customs» ≠ «обычаи»), so there is no link to restore.
Fine."; tag vocabulary "identical to EN, so it is parity, not a defect". Limits: EN prose not compared line by line;
dictionary senses from the cards' references and the reviewer's knowledge; reverse direction not checked;
"Pre-existing differences from EN in the three navigation files are outside this batch."

### Comprehensibility and scoped coverage

Verdicts: "Comprehensibility: NEEDS FIX. Clean on this facet: 競馬, 童話, 窓口, 突き当たり, 空中, 税関, 私鉄, 私立, 祭日,
お参り, 神話, 神様, 祝日, 社説, 社会科学. Scoped coverage: NEEDS FIX. Exceptions: 祭る and 秤."

C245-01 is high severity, C245-02 to C245-09 medium and C245-10 to C245-15 low; C245-10, C245-13 and C245-14 are rated
medium confidence and the others high.
- C245-01 (high; comprehensibility and scoped coverage), `祭る.md:20-21` (and the definition at line 15): both examples
  render 祭る as «почитают/почитаем», "the quiz title of 敬う («уважать; почитать»)"; "A learner cannot tell 祭る from
  敬う", and «Мы» adds a speaker. Remedy: «Это святилище посвящено богу моря.» and «На домашнем алтаре помещено божество
  для поклонения.», with a shrine-first meaning line naming 敬う.
- C245-02 (medium; comprehensibility and scoped coverage), `秤.md:34`: «…но 秤 от этого не становятся.» "makes 秤 the
  subject". Remedy: «…но от этого не становятся 秤.»
- C245-03, `おやすみ.md:4`: the three-part title is "too long to read as one quiz option". Remedy: «выходной (вежливо);
  спокойной ночи».
- C245-04, `おやすみ.md:30`: «в его метаданных нет кандзи» "names card metadata the learner cannot see".
- C245-05, `符号.md:4`: "a three-part definition, not one quiz answer". Remedy: «кодовое обозначение; знак числа»; "Do
  not use bare «код»: コード’s title is «код; провод; музыкальный аккорд»."
- C245-06, `空っぽ.md:4` and line 18: «совсем» "is an intensifier the Japanese sentence and the dictionary gloss do not
  have". Remedy: «пустой (без содержимого)» and «Коробка внутри была пустой.»
- C245-07, `空っぽ.md:33`: the bottle sentence "warns against a confusion only the English «vacant/available» invited".
  Remedy: delete it.
- C245-08, `祖先.md:4` and `先祖.md:4`: "the titles invent a split the bodies deny". Remedy: 先祖 «предки рода;
  родоначальник», 祖先 «предок; предшествующие поколения».
- C245-09, `敬う.md:4`: "infinitive «почитать» is also «to read for a while»". Remedy: «уважать; чтить».
- C245-10 (low), `標識.md:45`: «показатель, маркер» "is easy to misread". Remedy: «языковой показатель» (например,
  признак грамматической роли).
- C245-11 (low), `架空.md:35`: «Просмотренная словарная статья» "describes an editorial check the learner did not see".
- C245-12 (low), `磁石.md:40`: «а не отдельно приведённое название пьесы» "refers to a dictionary-page heading".
- C245-13 (low), `立ち止まる.md:4`: «приостанавливаться» "is an unnatural imperfective for a person who stops walking".
  Remedy: «останавливаться на ходу; делать паузу».
- C245-14 (low), `空想.md:4`: «грёзы» "is bookish"; «воображаемая картина» "is a definitional third segment". Remedy:
  «фантазия; мечтание».
- C245-15 (low), `移転.md:20`, `確率.md:19`, `祖先.md:21`: «Мы перевели», «Мы рассчитали» and «Мы бережём» "add a
  first-person plural subject the Japanese does not state".

Optional: 祝日's two title segments; 祭日.md:25 «Второй кандзи — главный»; 社説 «передовица»; 童話's «сказку»; 私立's
long title; 窓口; 私鉄; "税関 lost the EN link to existing words/習慣.md (link_parity); that sentence is an English homonym
warning («customs» ≠ habits) and was correctly not copied — outside these facets, not a Russian coverage gap."; "祭日
gained a link to 祝日.md that EN left unlinked; that is helpful, not a defect."; "No quiz-exclusion regression versus EN
on 税関, 秤, 私立 or 磁石." Limits: the truncated title-screen output; only three Jisho extracts opened; no author
reports, batch records or scratch worktrees read.

## Exclusion classification

All 93 EN exclusion entries (26 lists; EN has none on 税関, 秤, 私立 or 磁石) are retained in EN order. Nine of them lie
inside the batch, and the other 84 target existing RU cards. At the candidate, two direct, one-sided entries were added
on two new cards, both appended at the end of their lists; neither targets a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 社説→論文 (1) | Accepted ("on the B224 precedent") | "conservative: it exists only because of the title overlap «статья». Necessity in an ordinary quiz is not established. It is harmless and may stay." |
| 社会科学→自然科学 (1) | Accepted ("on the B224 precedent") | "unjustified (guards a contrast the article itself teaches; shared «науки» only). It is harmless … Optional: remove it, or keep it as conservative. Not required either way." |

The coordinator accepted both because "the bodies contrast exactly these words and the RU titles share «статья»/«науки»
stems"; the consistency reviewer raised one missing guard (F1, 童話→歴史) and the optional F2 (社説→評論). The correctness
reviewer raised no exclusion finding ("Original quiz exclusions are retained; 社説 adds 論文 and 社会科学 adds 自然科学"),
and the comprehensibility reviewer's title findings C245-03, C245-05 and C245-09 concerned readability rather than
unguarded overlaps; it noted that コード is already excluded from 符号.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`245-words-batch-84-recheck-001.md`.
