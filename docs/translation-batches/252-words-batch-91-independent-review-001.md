# Batch 252 — independent review 001

## Snapshot and scope

- Reviewed commit: `ac62348651051d98995df3cb458c512a93488d4f` (tree `3265cdbc606c1dda0bb1e974126e789e9c8398dc`), branch
  `full-ru-252-words-91`, parent `0b335c8`. The candidate was signed and pushed before review; its message reads "Batch
  252 candidate: 30 Russian word articles", followed only by the co-author trailer.
  - The content was authored in the scratch lane `learning-japanese-ru-b252`, whose local-only scratch commit `e21a513`
    ("B252 lane drafts on B251 scratch (local scratch base for B253 lane; not for publication)") sits on `1bf398a`
    ("B244 blind-review fixes 149b7d7, fd4ae41, c4ba4be and 85a96a2 synced onto B251 lane scratch (local scratch base
    for B252 authoring; not for publication)"), itself on `95302bb` ("B251 lane drafts on B250 scratch (local scratch
    base for B252 lane; not for publication)"), `819ee18` ("B250 lane drafts on B243-fix/B249 scratch (local scratch base
    for B251 lane; not for publication)") and the earlier lane scratch commits. The coordinator's candidate script
    checked that the lane was clean at `e21a513` with parent `1bf398a`, that HEAD was the Batch 251 publication record
    with the published baseline as its parent and as `origin/main`, that the primary tree, including ignored files, was
    clean, that of the nine navigation files edited in the lane only `words/派手.md` had changed between `1bf398a` and
    the published HEAD, and that none of the 30 new word files already existed.
  - The script copied 39 lane files (the 30 new cards and the navigation files `kanji/停.md`, `kanji/各.md`,
    `words/下降.md`, `words/派手.md`, `words/潰れる.md`, `words/火山.md`, `words/無限.md`, `words/突く.md` and
    `words/転々.md`). 38 were copied byte-identically; `words/派手.md` was three-way merged with `git merge-file` (base:
    the scratch base `1bf398a`'s copy; ours: the lane's copy, which links 地味 on line 27; theirs: published main's copy,
    which carries line 31 as reworded by the published Batch 248 fix `c43dd9f`, "Batch 248 fix 1: apply blind-review
    dispositions"). The script then regenerated the manifest, checked that the changed path set was exactly the 39
    batch paths plus `manifest.json`, byte-compared every copy with the lane (`words/派手.md` with the saved merged file)
    and asserted that the published-main-to-merged diff of `words/派手.md` equals the scratch-base-to-lane diff. At the
    candidate `words/派手.md` therefore changes only line 27 (the plain 地味 becomes [地味](地味.md)). No follow-up edit
    from an earlier fix was applied, and no link was held from an earlier batch. For this record the 39 committed
    blobs at `ac62348` (and again at the fix `2a3a0d5`) were checked: none has a BOM or CR, and every file ends with a
    newline, as `.gitattributes` requires.
  - After authoring and before the candidate commit, the coordinator edited two lane cards: it retitled 停止, reworded
    one 停止 example and added the guard 停止→停留所, and it retitled オイル and restored its source word. The nine
    navigation files were not edited at adjudication. Its adjudication record (lane `learning-japanese-ru-b252`, base
    `1bf398a`) states:
    - "Scope: all 30 B252 word cards read against frozen EN `6af98cb7` in `b252-adj-read.txt` (plus `b252-cmp.txt`
      metadata/link diffs), and the 9 navigation files (17 added links per `navonly`; the author report's "14"
      undercounted repeated links in kanji/停.md and kanji/各.md) in lane `learning-japanese-ru-b252` on base `1bf398a`
      (B251 scratch). Edits applied with `b252_coord.py` (exact-once replacements, CR-free, paragraph count unchanged;
      dropped guards asserted RU-added and EN prefix preserved), then one manual guard addition (停止 → 停留所)."
    - the edits, each with its recorded reason:
      - 停止: "title/H1 «приостановление; прекращение работы» → «остановка (механизма, процесса); приостановление»"
        ("EN "stoppage; suspension"; «прекращение работы» could read as a person stopping/quitting work (the author had
        to guard 失業)");
      - 停止: "ex «Механизм внезапно прекратил работу.» → «Механизм внезапно остановился.»" ("EN "The machine suddenly
        stopped"");
      - 停止: "+ guard 停留所" ("the new title's bare segment «остановка» equals 停留所's «остановка (автобуса, трамвая)»
        after parenthetical stripping (title screen)");
      - オイル: "title/H1 «масло для жарки; моторное масло» → «масло; смазочное масло»" ("EN "oil; lubricant"; the draft
        title narrowed to two products while the body says the word is not restricted (olive, massage oil,
        kerosene)");
      - オイル: "«Это заимствование, записанное катаканой» → «Это заимствование из английского oil, записанное
        катаканой»" ("restores EN's source word");
    - RU-only links (accepted): "断水 → [停電](停電.md): substantive "not a power outage" comparison present in EN as
      plain text; target in this batch." and "地味 → [派手](派手.md): the dictionary antonym discussed in the card;
      target is the published-before-B252 B248 draft.", with "Precedent: B241 一段→段, B245 祭日→祝日, B248 狙う→目指す,
      B249 畳む→広げる.";
    - guard pruning: "Criterion: keep where titles share a lexeme or are near-synonyms with overlapping sense; drop
      antonyms, topical-only pairs, homophones/shared-component pairs and pairs the titles already disambiguate."; "Dropped
      (26; 21 drafted guards kept, 22 RU-added in total with 停止 → 停留所): 停止 故障 失業; 不通 交通 連絡; 無沙汰 便り; 無数
      様々; 地味 派手 (antonym); 各地 地方; 一通り 一度; 無地 模様 柄; 為す 善; 点く 消える; 点々 転々 徐々に; 炭鉱 石炭 (also
      removes the RU-only quiz_exclusions key); 災難 被害; 灯油 油 ガソリン; 火口 火山; 火傷 熱い; 濡らす 乾く; 濃度 割合; 濁る
      澄む; 潰す 暇; 漢和 英和."; "No reverse redundancy: no kept target already lists the new word.";
    - accepted as drafted: "EN-only links left plain where the target is absent in RU: kanji 替 炭 鉱 灰 灯 油 濃; words
      淡水 乾かす 湿る."; "English-only notes legitimately adapted/omitted: 灰色 gray/grey spelling note (12 vs 13
      paragraphs); 灯油 "paraffin" sentence; 為替 "draft" note adapted to «перевод» / «платёжный документ»."; "Russian
      lexis judged natural, not dictionary-checked: «стоянка», «творить», «злоключение», «крапинки», «однотонный»,
      «несметный», «заурядный», «мутнеть» (open to reviewer comment).";
    - "Validation after edits (lane): manifest 5,679 files (version c7fde884a8a82b79); validate 0 errors; unittest OK;
      budget OK (5,696 entries; localZipBytes 8,241,688); link parity over 39 files: no LOST, EXTRA only 地味 → 派手 and
      断水 → 停電; navonly 9 files / 17 links / 0 problems; title screen 0 unguarded exact overlaps; diff --check clean;
      no BOM/CR/missing EOL (40 paths)."

      The plain-link sentence names ten targets. A mechanical count of `.md` link targets in EN finds 11 EN link
      occurrences to the same 10 absent RU targets in the new cards: words/淡水 (from 断水), kanji 替 (from 為替), kanji 炭
      and 鉱 (from 炭鉱), kanji 灰 (from 灰色), kanji 灯 and 油 (from 灯油), kanji 灯 (from 灯台), words/乾かす and words/湿る
      (from 濡らす) and kanji 濃 (from 濃度). The 30 EN cards have no `../articles/` link. All ten absent targets stay
      plain at the candidate and at the fix. The author report also listed 直す as an absent target, although
      `words/直す.md` exists; the comprehensibility reviewer raised the plain 直す as C7, and fix 1 linked it.

    The lane `contentVersion` differs from the candidate's because the lane tree carries its own copies of earlier lane
    drafts; the entry count is the same.

    Fix 1 later changed two items the coordinator had kept: 停車's title, which contained «стоянка» (now «остановка
    транспортного средства»; «стоянка» no longer occurs anywhere in `words/停車.md`), and 為替's exclusions, which gained
    翻訳; see the recheck record. Fix 1 did not touch 停止 or オイル, so the coordinator's edits stand.

    The committed manifest records 5,679 entries (5,674 `files`, 3 images and 2 scenes; `contentVersion`
    `42a30cef229b3b48`); the coordinator's lane `validate.py` run and its phase-1 `tools/validate.py` run on the
    candidate content reported 0 errors. The consistency reviewer also ran the validator on the candidate (0 errors), as
    did the correctness reviewer.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 9 files with 17 restored navigation links (the kanji cards 停 and 各 and the word cards 下降, 派手, 潰れる, 火山, 無限,
      突く and 転々);
    - `manifest.json` (`contentVersion` `42a30cef229b3b48`, 5,679 entries);
    - the intake, whose note reads "B252 30-card adaptation with seventeen navigation-only link restorations in nine
      existing files; candidate before blind review."

    Against the published baseline the candidate changes 42 files (1,758 insertions, 24 deletions), including the
    parent's publication record; the candidate commit itself changes 41 files (1,678 insertions, 24 deletions).
- Published baseline recorded in the intake: `60c7b3cabd633a854c9357dcaf2d6b559a8ee026` (Batch 251 merge, PR #135).
  Parent `0b335c8` ("Record B251 publication verification") adds only the Batch 251 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace, navigation-only or tracking-ledger check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 9 files (17 links added, no other change);
  - tracking-ledger pre-check (the 30 new word paths are exactly the batch paths not yet in the ledger).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b252-cand-screen.txt`, 321 lines): 42 `OK` lines for pairs already guarded by an exclusion and 279
    `!!` lines. It has four exact-segment lines, all `OK` (guarded): 停止 ~ ストップ, 停止 ~ 停留所, 一通り ~ そっくり and
    オイル ~ 油; every other line is stem-only. `b252-screen.txt` and `b252-screen-final.txt` (323 lines each: 42 `OK`
    and 281 `!!`), the lane screens, have identical lines. Against the candidate screen they show the `OK` lines 停車 ~
    立ち止まる and 停止 ~ 立ち止まる with the lane's own 立ち止まる title «останавливаться на ходу; приостанавливаться»
    instead of published «останавливаться на ходу; делать паузу» (the 停止 line also with the stem «приос»), and two
    more stem-only `!!` lines, 濃度 ~ 発想 and 漢和 ~ 物騒, which show the lane's own copies of those neighbour titles;
    no exact-segment line differs;
  - link parity: "checked 39", no LOST link and two EXTRA links, the reviewed RU-only words/地味 → words/派手 and
    words/断水 → words/停電 in new cards. No navigation file has an RU-only link. For this record link parity was run
    on a temporary export of the candidate tree outside every repository (since deleted), with the same result, and
    again at the fix `2a3a0d5`, where it adds only the fix-added words/潰す → words/直す.
- Common sample: all three reviewers read all 30 new word cards in full against EN, and all three read the nine
  navigation diffs. The consistency reviewer also checked the intake path list and hashes.
- Correctness review scope:
  - "File-by-file full paired reading completed for:" the 30 cards; "Also inspected the restored-link runtime diffs in
    kanji/停.md, kanji/各.md, words/下降.md, words/派手.md, words/潰れる.md, words/火山.md, words/無限.md, words/突く.md and
    words/転々.md. Checked current titles/readings of comparison and exclusion targets; sampled existing RU conventions
    rather than claiming full review of every old card."
  - "Inspected actual JMdict XML entries for every cited entry ID, including spelling/reading and sense restrictions;
    consulted actual Daijisen/Weblio/Kotobank entries for consequential usage claims."; "Japanese Wiktionary's actual
    オイル etymology confirms the English borrowing."; it checked Russian dictionary entries on gramota.ru for стоянка,
    крапинка, однотонный, несметный, заурядный, злоключение, мутнеть and творить ("No lexical contradiction was
    established for those titles."), matched "All 30 N2 labels" against "the policy's pinned vocabulary CSV" and used
    KANJIDIC2 as a fallback ("Jisho rate limits and kanjiapi HTTP 403 responses were not treated as evidence.").
  - "Read-only validation completed: python -X utf8 -B C:\Users\romanko\repos\learning-japanese-ru\tools\validate.py —
    0 error(s). No generator was run." It records "No repository files edited, staged, committed, checked out, reset or
    pushed." and "No other agents used."
- Consistency review scope:
  - "Read in full: the 30 new word cards and the diffs of the 9 navigation-only files"; "I compared them against frozen
    EN and read the intake JSON for path parity, hashes and absence of learner content only."; "I ran my own title
    screen, but it was only partly triaged (see Limits)."
  - "`python tools/validate.py` reports 0 errors." The report also states that no Python bytecode cache was created.
  - Incident: "I accidentally ran `python tools/build_manifest.py --help`. It executed the generator and printed
    `manifest.json: 5679 files, version 42a30cef229b3b48`. `git status` stayed empty afterwards, so the manifest is
    byte-identical and current. No diff resulted."
  - Limits: "The title screen was only partly triaged." with spot checks and targeted lookups of 翻訳, 射す, 英和, 澄む,
    被害, 乾く, 割合, 久しぶり, 日常 and 通貨, "not exhaustively"; "Dictionary basis was taken from the sense IDs cited in
    the footers, which equal EN. I did not look up JMdict independently."; "Dictionary senses were not independently
    looked up."
- Comprehensibility review scope:
  - "Read in full, each against its EN original in `learning-japanese-en-frozen` at 6af98cb:" the 30 cards; "No file in
    that list was skipped or skimmed."; "Related RU titles checked for collisions: 駐車, 駐車場, 停留所, 油, バター, 派手,
    両替, 行う, 無限, 普通, 直す, 全国, 集中, 付く, 転々, 不幸, 辞書, ストップ."; the link-only hunks in the nine navigation
    files "were read as diffs only, not as new articles"; "Tools: `word_title_screen.py` (lead only) and
    `link_parity.py` (no LOST links; EXTRA 断水→停電 and 地味→派手 are added navigation, not defects)."
  - Its limits record "Not re-audited: dictionary tags for ちょうじ, むぐる and ほくち beyond the cards' own wording (no
    outright mis-label seen); intake JSON and translation-batch docs were not read." and that no Python bytecode cache
    was left in the RU tree. It records no validator run and makes no statement about generators.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `aff7f05e-f9a8-4035-9d23-e2cd4a818406`,
  `4f39d43f-2fa7-4ff3-829c-b5c1165aeeaa` and `0e460b5a-1457-4239-9502-013d484eb544`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model
  identifier not independently verifiable.", the consistency report "Model identity is not verifiable." and the
  comprehensibility report "Model: not verifiable from this session."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. The report files'
  write times are 15:53, 15:59 and 16:17 on 2026-11-23; the ordering otherwise rests on the coordinator's session
  records (each reviewer launched after the previous one finished). The correctness report records "Initial and final
  HEAD match the assigned candidate; git status --porcelain is empty."; the consistency report records "HEAD matches.
  `git status --porcelain` is empty before and after."; the comprehensibility report records "uncommitted changes: none
  (`git rev-parse HEAD` matches; `git status --porcelain` empty)". No fix was applied until all three reports were
  complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator ("do NOT run `tools/build_manifest.py`
  or any other generator") and stated "The only file you write is your report." The correctness report says "No
  generator was run."; the consistency report records its accidental `--help` run of the generator, which left `git
  status` empty; the comprehensibility report makes no statement about generators. No reviewer reported changing a
  tracked repository file.
- Full blind reports:
  - `252-words-batch-91-review-correctness-001.md`
  - `252-words-batch-91-review-consistency-001.md`
  - `252-words-batch-91-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch lane worktrees.

  As in earlier batches, the consistency brief made one exception: the intake record, "check only that its path list
  matches the candidate's content diff and that it adds no learner content". The consistency report records "Intake
  JSON: PASS. The 39 payload paths equal 30 cards plus 9 nav files. The hashes match, `held` is empty, and there is no
  learner content.", and states "I did not read the author reports, the title-screen output, the reviewer reports or
  the translation-batches, translation-drafts and tracking files (apart from the intake JSON)." The correctness report
  states "Blindness restrictions were maintained: no author/other-reviewer reports, title-screen output, prohibited
  batch/draft/tracking documents or scratch worktrees were read. Only this designated report was written."; the
  comprehensibility report records "intake JSON and translation-batch docs were not read." The consistency and
  comprehensibility reviewers ran the title screen themselves rather than reading the coordinator's output.

## Initial verdicts and findings

### Correctness

Verdicts: "correctness NEEDS FIX (停車, F1; no further actionable defect established in the other 29 cards); scoped
coverage CLEAN. Russian comprehensibility and quiz quality were not separately assigned or certified."

- F1 (LOW; correctness — damaged translation/argument structure), `words/停車.md:34`: "Claim: “停止 может и механизм,
  который вовсе не транспортное средство.”" "The EN point is that a non-vehicle machine can stop, illustrating the
  broader scope of 停止. Here the Japanese noun is left in the Russian infinitive/predicate position after “может”; the
  stopping action has no Russian verbal realization." "The preceding line allows the intended point to be recovered,
  limiting the learning impact." Remedy: "replace line 34 with “Остановиться может и механизм, который вовсе не является
  транспортным средством.”" Evidence: frozen EN `words/停車.md:31` ("a machine can 停止 without being a vehicle.") and
  JMdict 1434920 senses 1–2. Confidence: HIGH.

"Optional: None. Stylistic alternatives and unnecessary-but-harmless quiz exclusions are not elevated to defects."

What the reviewer confirmed: "All 30 main Japanese example sentences/readings and the non-title/non-exclusion metadata
match EN. All EN exclusions and external source URLs are retained; all runtime links resolve, and no EN link with an
existing RU target was dropped. Full semantic comparison found no omitted Japanese teaching rule. Removal of
English-only gray/grey, paraffin and geographic “plain” contrasts is not a coverage loss in Russian."

Limits: "CLEAN means no actionable defect established within the assigned boundary, not exhaustive correctness. The
frozen EN directory was used as supplied; its commit label was not independently authenticated. Repository signature
cryptography was not independently audited."; "Structural success is not semantic proof. App quiz execution and
exhaustive review of unchanged older cards/kanji metadata were outside scope."

### Consistency and quiz safety

Verdicts:
- "Structure and front matter vs EN: PASS. All 30 cards are identical to EN apart from the translated `title`."
- "Nav restorations: PASS. 17 link occurrences, byte-identical apart from the link brackets and hrefs. Line numbers
  match EN."
- "Links: PASS. Nothing is broken. The dropped EN links all point to cards that are absent in RU. The RU-only links
  断水→停電 and 地味→派手 are justified."
- "Footers and source URLs, entry IDs and sense numbers: PASS. They equal EN. No RU-only source was added."
- "EN quiz_exclusions retained: PASS. All are present, in EN order, with the RU additions appended."
- "RU-added guards: PASS with notes. 22 guards were added; none is unjustified. See the classification below."
- "Missing guards: one finding (F1)."
- "Manifest: PASS. It is current (see Limits)."
- "Intake JSON: PASS. The 39 payload paths equal 30 cards plus 9 nav files. The hashes match, `held` is empty, and
  there is no learner content."
- "Titles: PASS with optional polish (O1–O3)."

Findings:
- F1 (Medium, confidence medium), missing guard 為替 ~ 翻訳: "The 為替 title segment «денежный перевод» (line 12) shares
  the bare word «перевод» with `words/翻訳.md`, whose title is «перевод». EN has no such overlap. It is RU-introduced
  homonymy that makes a learner-visible wrong answer ambiguous." Remedy: "change line 9 to `quiz_exclusions: [両替, 交換,
  換える, 替える, 案, 通貨, 翻訳]`. Alternatively, drop the bare «перевод» from the title. The body already says
  «Перевод — денежный, а не текста» (為替:43)."
- F2 (Low, confidence medium; no action required), unguarded in-batch pairs: "These pairs share only a topic, with no
  shared title segment: 停電~断水, 停車~停電/断水/不通, 無数~無地, 点く~点々, 灯油~灯台, 灯台~オイル, 火口~火傷 and 濁る~濃度. EN
  has no guards for them either, so I judge guards unnecessary." "If a guard is wanted anywhere, 断水→停電 is the only
  candidate."

Optional:
- O1: "the 無沙汰 title segment «давно не давать о себе знать» is a verb phrase inside a noun title. The ご register is
  already signalled in the body."
- O2: "the 潜る title «уходить под воду» is stilted. «нырять» would be natural, and its closest card 飛び込む is guarded."
- O3: "the 為替 «валютный обмен» is narrower than the EN «financial exchange». The 無地 «однотонный» could imply a single
  colour, though the body clarifies it. 点々 mixes an adverb and a plural noun."
- Pre-existing, outside the batch: "`words/火山.md:23` has a mismatched bracket «（かこう, кратер)». `kanji/各.md` keeps
  各々 and 各自 plain because the targets are absent. The 火傷 tag `suru` vs the vocabulary `suru-verb` is inherited from
  EN."

Limits: the generator incident, title-screen triage and dictionary limits quoted above, and "Other model-reviewer
outputs were not consulted, by design."

### Comprehensibility and scoped coverage

Verdicts: "Comprehensibility: NEEDS FIX (停車, 為替, 一通り, 火傷, オイル, 潰す). The other 24 new cards have no established
comprehensibility defect. Scoped coverage: CLEAN. EN teaching points are still in the article bodies; English-only
traps (gray/grey, paraffin vs wax, draft, little by little, dip, modest, all parts, plain, oil/grease, smash) are
rebuilt or correctly dropped for Russian."

C1–C3 are medium and C4–C7 low; confidence is high for C1, C2, C3 and C5 and medium for C4, C6 and C7.
- C1, `words/停車.md:4` (repeat at line 12): "The quiz title «остановка транспорта; стоянка (в пути)» teaches the wrong
  Russian pair." Remedy: "set both the `title` and the H1 to `остановка транспортного средства; краткая остановка (не
  парковка)`. The kanji card already glosses this word as «остановка транспортного средства»." Evidence: Digital
  Daijisen 停車 sense 2 ("capped at 5 minutes in the Road Traffic Act") and JMdict.
- C2, `words/為替.md:4` (repeat at line 12): "«валютный обмен» is narrower than the settlement sense the body opens
  with and than EN "financial exchange", and it is not distinguishable from 両替 «обмен валюты; размен купюр»." Remedy:
  "`денежный перевод; валютный расчёт` in both `title` and the H1."
- C3, `words/一通り.md:19`: "«Я прочитал инструкцию от начала до конца» states a stronger, cover-to-cover reading than
  一通り and contradicts the next sentence (line 22), which says this example does not promise exhaustive study."
  Remedy: "`— Я в общих чертах прочитал инструкцию.`"
- C4, `words/一通り.md:4` (repeat at line 12): "«обыкновенный (в отрицании)» is a usage rule, not a gloss a learner can
  choose as one answer, and the three-part title reads as a definition." Remedy: "`бегло целиком; полный набор;
  обыкновенный`."
- C5, `words/火傷.md:31`: "«в коллекции» and «метаданные записанного слова» refer to the card set and to editorial
  metadata a beginner cannot see, and «он» has no clear learner-facing referent." Remedy: "delete the sentence."
- C6, `words/オイル.md:28`: "Latin `oil` is an unexplained English word in learner prose." Remedy: "`Это слово записано
  катаканой, без кандзи, которые можно было бы разобрать.`"; "Other gairaigo cards (バター, セット, チェック, ストーブ)
  also name the English source; that does not make this instance readable, but it keeps the impact low."
- C7, `words/潰す.md:39`: "直す is an existing RU card (`title: чинить; исправлять`) used as the practical opposite and
  left as plain text, so the contrast cannot be opened. 立て直す has no RU file and should stay plain." Remedy: "`[直す](直す.md)（なおす）— «чинить» — или 立て直す（たてなおす）— «восстанавливать, поправлять» — могут быть
  противоположностью в подходящем контексте.`"

Optional: 災難 «злоключение» "is accurate (Кузнецов: «Несчастный случай; беда, горестное приключение») but less
everyday than the first gloss «беда»; not a wrong answer."; "潰す:30 «в коллекции» is the same meta habit as C5, but a
learner can parse it"; "無地:41–42 warns about «простой», a gloss the card never offers."; "点々:41 «постепенное
улучшение» is narrower than the rebuilt "little by little" warning, but the 徐々に pointer holds."; "炭鉱:39
«используемой версии словаря» is slightly editorial"; 為す «творить» "can suggest creation", but the examples are
natural; "潰す and 潜る titles are long; each segment is a real gloss"; "灯台:20 plain 目印 reads naturally as a
collocation, not a missed contrast". Limits: "Title-screen overlaps of «остановка» (停止/停留所/ストップ), «масло»
(オイル/油) and «целиком» (一通り/そっくり) were leads only"; the dictionary-tag and intake limits quoted above.

## Exclusion classification

All 143 EN exclusion entries (25 lists; EN has none on 停電, 断水, 炭鉱, 灰色 or 灯台) are retained in EN order. 11 of
them lie inside the batch, and the other 132 target existing RU cards. At the candidate, 22 direct, one-sided entries
were added on 12 new cards, each appended at the end of its list; none targets a batch word. Fix 1 added one more,
為替→翻訳, and removed none (see the recheck record).

| Entries | Coordinator (kept under its criterion) | Consistency reviewer |
|---|---|---|
| 停車→停留所, 駐車, 駐車場, 立ち止まる, 終点 (5) | kept: "shared «остановка»/«стоянка»" | "Conservative (real basis, necessity unestablished; keep)" |
| 停止→止む (1) | kept | "Conservative" |
| 停止→停留所 (1) | added at adjudication: "the new title's bare segment «остановка» equals 停留所's «остановка (автобуса, трамвая)» after parenthetical stripping (title screen)" | "Required": "bare «остановка»" |
| 無沙汰→久しぶり, 黙る (2) | kept | "Conservative" |
| 地味→謙遜 (1) | kept | "Conservative" |
| 各地→全国 (1) | kept | "Conservative" |
| 一通り→おおざっぱ, 完全, セット (3) | kept | "Conservative" |
| 一通り→そっくり (1) | kept | "Required": "segment «целиком»" |
| 平凡→日常 (1) | kept: "marginal: «обыденность» ≈ «заурядный»" | "Conservative" |
| 為替→通貨 (1) | kept | "Conservative" |
| オイル→バター (1) | kept | "Required": "«масло»; the オイル/油 pair is already guarded" |
| 潰す→殺す (1) | kept: "«убивать время»/«убивать»" | "Conservative": "«убивать время»" |
| 潜る→水中 (1) | kept | "Conservative" |
| 漢和→漢字, 日中 (2) | kept | "Conservative" |

The coordinator's record gives a note only for the entries quoted in the table; it lists the others as kept under its
criterion. The consistency reviewer classed three entries as required and nineteen as conservative, with
"Unjustified: none. The extra guards cost only a little distractor variety."; it took the dictionary basis "from the
sense IDs cited in the footers" and "did not look up JMdict independently". It raised one missing guard, 為替 ~ 翻訳
(F1), and judged the unguarded in-batch topic pairs of F2 not to need guards. The correctness reviewer did not elevate
"unnecessary-but-harmless quiz exclusions" to defects; the comprehensibility reviewer did not classify the entries.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`252-words-batch-91-recheck-001.md`.
