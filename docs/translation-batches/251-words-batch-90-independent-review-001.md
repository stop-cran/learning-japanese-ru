# Batch 251 — independent review 001

## Snapshot and scope

- Reviewed commit: `8bb7b574df56eb149c7b7c22a70aae4cde4bbee6` (tree `af91f2d01fc3555bf1190ac60079f79715e80cb7`), branch
  `full-ru-251-words-90`, parent `9b8a497`. The candidate was signed and pushed before review; its message reads "Batch
  251 candidate: 30 Russian word articles", followed only by the co-author trailer.
  - The content was authored in the scratch lane `learning-japanese-ru-b251`, whose local-only scratch commit `95302bb`
    ("B251 lane drafts on B250 scratch (local scratch base for B252 lane; not for publication)") sits on `819ee18`
    ("B250 lane drafts on B243-fix/B249 scratch (local scratch base for B251 lane; not for publication)"), itself on
    `c123f7f` ("B243 blind-review fix 6aa1bca synced onto B249 lane scratch"), `acc9bcc` ("B249 lane drafts on
    B242-B248 scratch") and the earlier lane scratch commits `2d85e8d`, `bca83ec`, `4ef6fa4` and `b37a987`. The
    coordinator's candidate script checked that the lane was clean at `95302bb` with parent `819ee18`, that HEAD was the
    Batch 250 publication record with the published baseline as its parent and as `origin/main`, that the primary tree,
    including ignored files, was clean, that the four navigation files edited in the lane were unchanged between
    `819ee18` and the published HEAD, and that none of the 30 new word files already existed.
  - The script copied 34 lane files (the 30 new cards and the navigation files `words/傾く.md`, `words/光る.md`,
    `words/往復.md` and `words/炊く.md`); no follow-up edit from an earlier fix was applied. It then regenerated the
    manifest, checked that the changed path set was exactly the 34 batch paths plus `manifest.json` and byte-compared all
    34 copies with the lane. No link was held from an earlier batch. For this record the 34 committed blobs at `8bb7b57`
    (and again at the fix `e290cd2`) were checked: none has a BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - After authoring and before the candidate commit, the coordinator edited three lane cards: it retitled 熱する,
    reworded one 怠る example and rewrote 暖まる's distinctive paragraph. The four navigation files were copied
    unchanged. Its adjudication record (lane `learning-japanese-ru-b251`, base `819ee18`) states:
    - "Scope: all 30 B251 word cards read against frozen EN `6af98cb7` in `b251-adj-read.txt`, plus the 4 navigation
      files (4 links: 傾く 光る 往復 炊く) in lane `learning-japanese-ru-b251` on base `819ee18` (B250 scratch). Edits
      applied with `b251_coord.py` (exact-once replacements, CR-free, paragraph count unchanged)."
    - the edits, each with its recorded reason:
      - 熱する: "title/H1 «раскалять; накаляться (о споре, чувствах)» → «нагревать; накаляться (о споре, чувствах)»"
        ("EN "heat"; «раскалять» narrows to red-hot. «нагрев-» elsewhere only in 沸かす/沸く, both already excluded by
        熱する. Example «Я хорошо раскаляю сковороду» kept (natural for a frying pan)");
      - 怠る: "ex «Нельзя упускать из виду проверку безопасности» → «Нельзя пренебрегать проверкой безопасности»" ("EN
        "neglect"; «упускать из виду» = overlook");
      - 暖まる: "distinctive paragraph: replaced the claim that Russian «я согрелся» "sounds reflexive" in contrast to
        Japanese" ("false contrast: Russian «согреться» is also an intransitive change of state; now framed as a
        parallel plus the が/を point");
    - accepted as drafted: "Remaining cards judged faithful (爪 … 休業 in the adjudication read), titles matching the
      prompt's theme-guard leads.";
    - "照る «лить свет (о солнце, луне); быть солнечным (о погоде)» kept: «светить» avoided by title policy; «лить свет»
      attested literary Russian.";
    - "加熱 «подогрев; тепловая обработка», 怠る and 煎る titles kept (煎る 3 segments / 70 chars, within corpus norms:
      28 of 4,183 word titles are ≥70 chars, max 89).";
    - "射す English-gloss note ("strike") kept, following the あぶる precedent; open to reviewer comment.";
    - "RU-added conservative exclusions kept (prompt theme-guard leads, e.g. 晴れ, 暖房, 注目, いつまでも, 営業, 管).";
    - "EN-only links dropped where the target is absent in RU (温, 燃, 冷ます, 商店, 無数, 照).";
    - "Validation after edits (lane): manifest 5,649 files (version 02b295c1b61b0191); validate 0 errors; 124 tests OK;
      budget OK (5,666 entries; localZipBytes 8,194,426); link parity over 34 files: no LOST; EXTRA only the
      pre-existing 光る → 輝く (present at `819ee18`); navonly 4 files / 4 links / 0 problems; diff --check clean; no
      BOM/CR/missing EOL (35 paths)."

      The plain-link sentence names six targets. A mechanical count of `.md` link targets in EN finds 13 EN link
      occurrences to 9 absent RU targets in the new cards: kanji 畜 (from 牧畜), kanji 片 (from 片道, 片寄る and 片仮名),
      words/仮名 (from 片仮名), kanji 温 (from 暖める and 暖まる), kanji 燃 (from 燃やす), words/冷ます (from 熱する), kanji 照
      (from 照らす and 照る), words/商店 (from 焦点) and words/無数 (from 無限). The coordinator's sentence therefore omits
      畜, 片 and 仮名. The 30 EN cards have no `../articles/` link. All nine absent targets stay plain at the candidate and
      at the fix.

    The lane `contentVersion` differs from the candidate's because the lane tree carries its own copies of earlier lane
    drafts; the entry count is the same.

    Fix 1 later changed several items the coordinator had kept: the 照る, 加熱 and 煎る titles (now «светить (о солнце,
    луне); быть солнечным (о погоде)», «нагревание; подведение тепла» and «обжаривать без масла; подсушивать на огне»),
    the 射す "strike" sentence (deleted) and the RU-added guards 暖まる→暖房 and 休業→営業 (removed); see the recheck
    record. Fix 1 did not touch 熱する or 怠る and changed 暖まる only in its `quiz_exclusions`, so the coordinator's
    three edits stand.

    The committed manifest records 5,649 entries (5,644 `files`, 3 images and 2 scenes; `contentVersion`
    `703a555ae1987ab0`); the coordinator's lane `validate.py` run and its phase-1 `tools/validate.py` run on the
    candidate content reported 0 errors. The consistency reviewer also ran the validator on the candidate (0 errors), as
    did the correctness reviewer.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 4 files with 4 restored navigation links (the word cards 傾く, 光る, 往復 and 炊く);
    - `manifest.json` (`contentVersion` `703a555ae1987ab0`, 5,649 entries);
    - the intake, whose note reads "B251 30-card adaptation with four navigation-only link restorations in four existing
      files; candidate before blind review."

    Against the published baseline the candidate changes 37 files (1,626 insertions, 9 deletions), including the
    parent's publication record; the candidate commit itself changes 36 files (1,546 insertions, 9 deletions).
- Published baseline recorded in the intake: `48530035e93103d313a4c3f418e68526927a4d58` (Batch 250 merge, PR #134).
  Parent `9b8a497` ("Record B250 publication verification") adds only the Batch 250 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace, navigation-only or tracking-ledger check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 4 files (4 links added, no other change);
  - tracking-ledger pre-check (the 30 new word paths are exactly the batch paths not yet in the ledger).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b251-cand-screen.txt`, 313 lines): 26 `OK` lines for pairs already guarded by an exclusion and 287
    `!!` lines. It has no exact-segment line; every line is stem-only. `b251-screen.txt` (316 lines, the lane screen)
    contains every candidate-screen line and three more stem-only `!!` lines, 怠る ~ 発想, 休業 ~ 直前 and 休業 ~ 立ち止まる,
    which show the lane's own copies of those neighbour titles; no exact-segment line differs. `b251-screen-out.txt`
    (317 lines: 22 `OK` and 295 `!!`) is the author's earlier lane screen, with no exact-segment line; besides the same
    three lines it shows 熱する's pre-adjudication «раскалять» title (three «раска» lines instead of the `OK` 沸かす and
    沸く «нагре» lines, and 13 reworded lines) and has 片道 ~ 切符 and 煙突 ~ パイプ as `!!` rather than `OK`;
  - link parity: "checked 34", no LOST link and one EXTRA link, the RU-only words/光る → words/輝く (line 32) in a
    navigation file, which predates this batch. It is identical at the published baseline `4853003` and at the fix
    `e290cd2`, and EN has no such link (EN 光る:28 leaves 輝く plain). For this record link parity was verified again at
    the fix with the same result.
- Common sample: all three reviewers read all 30 new word cards in full against EN, and all three read the four
  navigation diffs. The consistency reviewer also checked the intake path list and the manifest hashes.
- Correctness review scope:
  - "Blind correctness and scoped-coverage review of all 30 new word cards. Each path below was read IN FULL in BOTH RU
    and EN, including front matter, every example/read­ing, all sections and footers", followed by the 30 cards; "Also
    reviewed the complete four one-line backlink diffs in words/往復.md, words/傾く.md, words/炊く.md and words/光る.md,
    and actual current titles of all linked/excluded comparison cards. Those existing cards were not each re-reviewed
    in full."
  - "Inspected all primary entries through Jisho's word API and all cited JMdict entry IDs, senses and form
    qualifications in canonical XML."; "Inspected cited Daijisen/Kotobank definitions for the nontrivial spelling,
    light/comparison, roasting, origin and historical claims."; it read the Agency for Cultural Affairs council report
    PDF (文化審議会国語分科会, 21 February 2014), checked component readings at kanjiapi.dev ("these were not used to
    invent etymologies"), matched every primary N2 spelling, reading and entry identity against the policy-pinned N2
    vocabulary CSV, and checked Russian lexical claims in Kuznetsov's dictionary via Gramota ("Thus these are not left
    “unchecked in a Russian dictionary.”").
  - "Read-only validator: python -X utf8 -B tools/validate.py, primary RU checkout, completed exit 0: “0 error(s)”."
    It records "No repository edits, index changes, generators, branch switches or checkouts." and "No subagents
    used."
- Consistency review scope:
  - "All 30 cards and the 4 navigation diffs (傾く, 光る, 往復, 炊く) read in full."; "Automated EN-vs-RU comparison of
    front matter, links and line counts."; "Manifest hashes and intake JSON (`docs/translation-batches/251-words-batch-90-intake.json`)
    checked."; "Footers compared with EN by URL, JMdict entry number and sense number."; "Quiz exclusions analysed,
    including the 16 RU-introduced guards on 13 cards."
  - "No generator run (no `build_manifest.py`), no edits, no branch changes."; it also ran `word_title_screen.py` from
    the coordinator's tools folder "with `RU_ROOT` set (output to temp, not the repo)".
  - Incident: its `tools/validate.py` run created a Python bytecode cache under `tools`, which the reviewer removed; it
    used `python -B` afterwards.
  - It noted that 118 `strokes/*` hashes "differ only through CRLF checkout (they match after LF normalisation). This is
    an environment artifact."
  - Limits: "Dictionary senses were not re-verified beyond the JMdict numbers cited in the cards."; "Body glosses for
    無限 (34-35) and 休業 (29) looked fine but I did not judge them against the target titles in detail."; for four cards
    with fewer lines than EN it did not re-read EN ("I did not re-read EN for 焚く, 煙突, 物凄い, 煎る.").
- Comprehensibility review scope:
  - "All 30 new cards read in full against EN frozen 6af98cb", followed by the 30 cards; "Risk-pair titles checked",
    followed by the neighbours; "Link-only diffs in 傾く 光る 往復 炊く inspected. word_title_screen.py and link_parity.py
    run."
  - Its limits record "rare/archaic tags (烘る, 熬る, 烟突, 烟い/けぶい, 焚く-under-焼く) not re-read in raw JMdict XML; no
    contrary tag established, so no correctness finding. Title screen returned empty seg= hits only (stem noise such as
    живот/животноводство), not identical quiz answers. link_parity.py printed only "checked 30"." It records no
    validator run and makes no statement about generators.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `7c0a1f14-24a4-4553-94de-9dc3b937f8b6`,
  `75de4ab3-209d-4fb2-bc5f-35b2f9d68bfc` and `f119632e-0187-4bde-b793-1e506a568e08`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Actual deployed
  model identifier is not exposed to this reviewer and cannot be verified.", the consistency report "Model identity: I
  cannot verify the model I ran as from inside the session." and the comprehensibility report "Model: not verifiable
  from the session."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. The report files'
  write times are 12:04, 12:13 and 12:28 on 2026-11-23; the ordering otherwise rests on the coordinator's session
  records (each reviewer launched after the previous one finished). The correctness report records "HEAD matches; git
  status --porcelain empty before and after review."; the consistency report records "Working tree clean."; the
  comprehensibility report records "HEAD matches; status --porcelain empty." No fix was applied until all three reports
  were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator ("do NOT run `tools/build_manifest.py`
  or any other generator") and stated "The only file you write is your report." The correctness report says "No
  repository edits, index changes, generators, branch switches or checkouts."; the consistency report says "No generator
  run (no `build_manifest.py`), no edits, no branch changes." and records the transient Python bytecode cache it created
  and removed; the comprehensibility report makes no statement about generators. No reviewer reported changing a
  tracked repository file.
- Full blind reports:
  - `251-words-batch-90-review-correctness-001.md`
  - `251-words-batch-90-review-consistency-001.md`
  - `251-words-batch-90-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch lane worktrees.

  As in earlier batches, the consistency brief made one exception: the intake record, "check only that its path list
  matches the candidate's content diff and that it adds no learner content". The consistency report records "Intake
  JSON: 34 payload paths equal the content diff (30 cards + 4 nav files). `candidateRawSha256` values match the
  manifest.", and states "Blind review: I did not read other review reports or the scratch worktrees." The correctness
  report states "No author/reviewer reports, other FILES-directory files, prohibited RU tracking/batch/draft contents or
  scratch worktrees read."; the comprehensibility report records "Author reports, translation-batches, and scratch
  worktrees not read." The consistency and comprehensibility reviewers ran the title screen themselves rather than
  reading the coordinator's output.

## Initial verdicts and findings

### Correctness

Verdicts: "correctness NEEDS FIX (F1, 焚く); scoped coverage CLEAN across all 30 paired articles and four backlink diffs.
CLEAN means no actionable coverage defect established, not exhaustive correctness."

- F1 (MEDIUM; correctness), `words/焚く.md:4` (repeated :12, :17): "Wrong claim: «растапливать (печь, ванну)» applies
  the Russian verb to a bathtub; :17 likewise coordinates «растапливать и нагревать ванну, печь или котёл»." "Correct
  fact / impact: 風呂を焚く concerns heating bathwater with a fire. Russian «растапливать» means starting a fire in a
  stove/furnace, or melting a substance, not the ordinary action of heating bathwater." Remedy: "replace title and H1
  gloss with «жечь топливо; разводить и поддерживать огонь». Replace :17 with «топливо или благовония, топить печь или
  котёл, нагревать воду для ванны.»" Evidence: JMdict 1596840 sense 2, Digital Daijisen 焚く sense 2 via Weblio, and
  Kuznetsov РАСТОПИТЬ¹/² and ВАННА via Gramota. Confidence: HIGH.

Optional (marked "outside assigned facets; nonblocking comprehensibility"): "射す:39 still explains the English legacy
gloss strike; あぶる:41 refers to an unseen source-list gloss."; "照る:4 «лить свет» is marked bookish by Kuznetsov лить
(4), while the examples already use everyday «светить». 照らす:4 «озарять» is elevated in Kuznetsov озарить; its ordinary
synonym «освещать» is already present. Register simplification is optional here, not a second correctness finding."

What the reviewer confirmed: "All 30 preserve EN word/reading/level/type/kanji/tags. Original exclusions retained;
additions examined as direct guards, not inferred transitive groups. Every referenced internal target exists. No extra
RU link/source URL and no dropped EN link whose RU target exists. The 13 missing-target EN links are appropriately plain
text in RU"; "All Japanese example sentences AND kana readings compared mechanically: identical contents, including
punctuation, katakana and reading choices."

Limits: "No deployed-app, device, generator, archive/publication or corpus-frequency testing; no exhaustive whole-pool
quiz certification (outside these facets). Dictionary meaning does not prove contemporary frequency."; "Exact model ID
and signature cryptographic validity remain unverifiable in this review."

### Consistency and quiz safety

Verdicts: "Consistency with EN: CLEAN (optional notes only)."; "Quiz safety: CLEAN. No missing required guard found.
Several RU-added guards are over-guarding, non-blocking."; "Navigation diffs: CLEAN."; "Manifest and intake: CLEAN.";
"Validator: 0 errors."

The report heads its findings "all low or optional; none blocking":
- Items 1–3 (LOW): 片道→往復 ("antonym/contrast taught in the article, titles share no wording. Unnecessary.
  Harmless."), 片寄る→公平 ("unnecessary. Opposite concept, no shared wording. Harmless.") and 休業→営業 ("unnecessary.
  Opposite concept. Harmless.").
- Item 4 (LOW): 暖まる→暖房 "inconsistent. 暖める has no 暖房 guard, so either drop it or add it to 暖める."
- Item 5 (INFO): "conservative but with a real basis, not required": 物差し→単位, 物凄い→莫大, 牧畜→家畜, 牧場→牧畜, 牧場→農家
  and 焚く→炊く.
- Item 6: "Required guards, present and correct": 照る→晴れ, 煙突→管 and パイプ, 焦点→注目, 無限→いつまでも and 片道→切符.
- Item 7 (OPTIONAL): "片寄る and 片道 share the RU phrase «в одну сторону» (the EN titles share nothing). The head words
  differ, so risk is low. A one-way guard could be added."
- Item 8 (OPTIONAL): "照る→快晴 is unguarded, which is inconsistent with the 晴れ guard."
- Item 9: unguarded pairs "judged not defensible confusions".
- Item 10 (LOW): 照らす:45's 参考 gloss «справка, ориентир» "drifts from the 参考 title"; suggested «справка, обращение к
  источнику».
- Item 11 (OPTIONAL): 照る's title «лить свет» "is stilted".
- Items 12 and 13 (INFO): the bunka.go.jp footer label is "consistent with earlier published cards 粗い, 荒い and 始め. Not
  an error."; 照る's tags lack `wago` although `type: wago`, "Identical to EN, so a pre-existing parity item, not a batch
  defect."

What the reviewer confirmed: "Front matter: every key identical to EN except `title` (Russian). Tags, `jlpt` and `type`
identical in all 30."; "Links: no RU-only and no broken links. EN links missing in RU point to targets absent in RU
(kanji 畜 片 燃 照 温; words 仮名 冷ます 商店 無数)."; each navigation diff "changes one line, only by link brackets, with no
line-count change. Positions and `X.md` path form match EN."; "Footers: URLs and JMdict entry/sense numbers identical to
EN in all 30 cards."; "Title screen: no exact title or segment duplicates."

Limits: the dictionary, body-gloss and strokes-hash limits quoted above, and "Blind review: I did not read other review
reports or the scratch worktrees."

### Comprehensibility and scoped coverage

Verdicts: "comprehensibility NEEDS FIX (片寄る 焦がす あぶる 加熱 焚く 燃やす 射す 照る 煙突 煎る; other 20 cards no actionable
defect). scoped coverage NEEDS FIX (加熱 焚く 焦がす 燃やす 射す; elsewhere the EN point remains in the Russian card)."

All eleven findings are medium severity; confidence is high except for C11 (medium) and C8 ("high on opacity, not on
the tag").
- C1, `words/射す.md:39`: "«старая английская глосса strike» is unusable without English and points at a source gloss
  the learner cannot see." Remedy: "delete line 39, or «Глагол не значит «ударять»: свет доходит до места, а не бьёт по
  нему.»"
- C2, `words/あぶる.md:41`: "«исходный список слов даёт такую глоссу» cites a list the learner cannot see and rejects
  «опаливать», which is not the quiz title". Remedy: «Не всякое あぶる значит «опаливать»: согревание рук и лёгкое
  обжаривание нори — обычные случаи.»
- C3 (comprehensibility and coverage), `words/焦がす.md:45`: "«одно русское «сжечь» не подсказывает конструкцию» copies
  English "burn". «Сжечь» is transitive and does select を; «подгореть» selects が."
- C4 (comprehensibility and coverage), `words/加熱.md:4`: "«подогрев; тепловая обработка» narrows JMdict "heating;
  application of heat"." Remedy: title and H1 «нагревание; подведение тепла».
- C5, `words/照る.md:4`: "Title «лить свет» is not what line 18 «Светит солнце» and line 19 «Ярко светила луна» say".
  Remedy: title and H1 «светить (о солнце, луне); быть солнечным (о погоде)».
- C6, `words/煎る.md:4`: the title "is a three-clause definition, not a quiz answer." Remedy: title and H1 «обжаривать
  всухую; подсушивать на огне».
- C7, `words/煙突.md:43`: "«В изученной словарной статье есть жаргонное значение, связанное с таксометром» is reviewer
  voice and never says what the slang means."
- C8, `words/焚く.md:31`: "«устаревшая запись написания в этой отдельной словарной семье» describes a dictionary entry. A
  beginner cannot tell which spelling or what to do."
- C9 (coverage), `words/焚く.md:4`: the title "does not cover line 17 «благовония» or line 21 «зажигаю благовонные
  палочки»." Remedy: title and H1 «жечь (огонь, благовония); растапливать (печь, ванну)».
- C10 (comprehensibility and coverage), `words/燃やす.md:21`: "«горят боевым духом» is not ordinary"; "Line 43 says
  «гореть» or «жечь» does not pick the particle; «жечь» does select を and «гореть» selects が." Remedy: «Спортсмены
  разжигают в себе боевой дух.» and rewritten lines 43 and 45.
- C11, `words/片寄る.md:4`: "«Крениться» is a physical list. Examples do not use it". Remedy: title and H1 «смещаться в
  одну сторону; быть предвзятым».

Optional: 物凄い «неимоверный; чудовищный» "is bookish for a spoken intensifier"; 物差し «мерило» "is bookish but explained";
"爪:30 «в коллекции» is low-impact meta"; "煙い:15 «держать глаза открытыми» is a calque, saved by «Так дымно»"; "照らす
«озарять» is literary"; 怠る and 無限 notes judged clear. Limits: the raw-JMdict, title-screen and link-parity limits
quoted above; "Author reports, translation-batches, and scratch worktrees not read."

## Exclusion classification

All 123 EN exclusion entries (25 lists; EN has none on 片道, 片仮名, 煙突, 煙い or 煉瓦) are retained in EN order. 21 of
them lie inside the batch, and the other 102 target existing RU cards. At the candidate, 16 direct, one-sided entries
were added on 13 new cards, each appended at the end of its list; none targets a batch word. Fix 1 removed four of them
and added two others (see the recheck record).

| Entries | Author (kept by the coordinator) | Consistency reviewer |
|---|---|---|
| 物差し→単位 (1) | "conservative" | item 5: "shared stem «мер»." |
| 物凄い→莫大 (1) | "conservative" | item 5: "JMdict sense 2 "tremendous" vs "enormous"." |
| 牧畜→家畜 (1) | "required: «скот/животные» overlaps the livestock title" | item 5: "stem «скот»." |
| 牧場→牧畜 (1) | "required: shared «животновод-» segment" | item 5: "shared stem «животновод»." |
| 牧場→農家 (1) | "conservative: «ферма/фермер»" | item 5: "«ферма»/«фермер»." |
| 片道→往復 (1) | "required: ticket antonym in the same frame" | item 1 (LOW): "Unnecessary. Harmless." |
| 片道→切符 (1) | "conservative: shared «билет»" | item 6: "parity with the EN 往復→切符 guard." |
| 片寄る→公平 (1) | "conservative: antonym of «предвзятый»" | item 2 (LOW): "unnecessary." |
| 焚く→炊く (1) | "required: homophone たく with an overlapping «растапливать/разводить» gloss" | item 5: "homophone たく, but the titles are clearly different." |
| 暖まる→暖房 (1) | "conservative" | item 4 (LOW): "inconsistent." |
| 照る→晴れ (1) | "conservative: «солнечная/ясная погода»" | item 6: "parity with the EN 晴れる guard." |
| 煙突→管, パイプ (2) | 管 "conservative: «труба»"; パイプ "conservative: «труба; трубка», sibling consistency with 管" | item 6: "both titles contain «труба»." |
| 焦点→注目 (1) | "conservative: «внимание»" | item 6: "«пристальное внимание» vs «центр внимания»." |
| 無限→いつまでも (1) | "conservative: «бесконечно»" | item 6: "parity with the 永久/永遠 guards." |
| 休業→営業 (1) | "conservative: open-for-business antonym" | item 3 (LOW): "unnecessary. Opposite concept." |

The author and the consistency reviewer differ on 牧畜→家畜, 牧場→牧畜 and 焚く→炊く (author required, reviewer
conservative), on 片道→切符, 照る→晴れ, 煙突→管 and パイプ, 焦点→注目 and 無限→いつまでも (author conservative, reviewer
required), and on 片道→往復 (author required, reviewer unnecessary). The reviewer found no missing required guard and
called the four entries of items 1–4 over-guarding or inconsistent but harmless. The correctness reviewer examined the
additions "as direct guards, not inferred transitive groups" and found every referenced target existing; the
comprehensibility reviewer did not classify them. The author had also declined 照る→快晴 ("verb title against a noun
title, and 晴れ is already guarded"), which the consistency reviewer raised as optional item 8.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`251-words-batch-90-recheck-001.md`.
