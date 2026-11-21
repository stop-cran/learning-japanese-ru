# Batch 235 — independent review 001

## Snapshot and scope

- Reviewed commit: `75b2616d78a93d0655a2e7494abb6c1f9585ad10` (tree `a46106ee98c575dabd9e73ed70b1185de4ccd995`), branch
  `full-ru-235-words-74`, parent `b8314fd`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 234 candidate `1e7c04d20795a3f0efac996855d00f233ebe566b`.
    Before copying, the coordinator's candidate script checked two things: that the five navigation files edited there
    (`kanji/資.md`, `words/原料.md`, `words/書類.md`, `words/材料.md` and `words/貸す.md`) were unchanged between
    `1e7c04d` and the candidate's parent `b8314fd`, and that none of the 30 new cards existed in the primary checkout. It
    also checked that the branch, HEAD and `origin/main` were the expected ones and that the tree was clean.
  - The script byte-compared the 35 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 35 batch paths plus `manifest.json`. Its byte scan of all
    35 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 35 committed
    blobs at `75b2616` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from Batch 234; all six restored links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made no content edits: no title edit, no exclusion
    append and no held link; the 35 lane files were copied unchanged. Its adjudication record states:
    - "Screens rerun by the coordinator with RU_ROOT = lane: `word_title_screen.py` over the 30 words reports 0
      unguarded exact segments (output `b235-lane-screen.txt`); `link_parity.py` over the 35 paths reports only the
      three intended RU-only links 資料:31 → 情報, 資料:32 → 材料 (information/material contrast with existing RU cards)
      and 貸間:33 → 下宿 (paired with the required 貸間→下宿 guard); `navonly.py HEAD --only` over kanji/資, words/原料,
      書類, 材料 and 貸す reports 5 files, 6 links added, 0 problems; `validate.py` 0 errors.";
    - "Titles compared with EN one by one; no coordinator title edit. Deviations from the topic leads (転がす without
      «(нечаянно)», 転々 rephrased adverbially, 身分 «материальное положение», 足袋 without «таби», 足る without «(книжн.)»,
      家屋 without «жилое», 溜まる/貯蔵 qualifiers following EN's actual lists) are accepted as reported.";
    - "RU-added exclusions accepted as reported: 5 pairs on 4 cards; 資料→材料 and 貸間→下宿 required, 資料→参考, 賞品→賞金
      and 貸し出し→支給 conservative. Close stem hits checked in the compact screen: 賞品/賞金, 蓄える/貯金, 溜める/蓄える,
      貯蔵/保存, 足る/十分, 身分/地位/立場, 起床/起きる are guarded; 起床/立つ/立ち上がる, 貸し出し/発行, 貸家/貸間, 貨物/輸送,
      蓄える・貯蔵/余裕, 身分/性格/証明 are different senses or parts of speech (no guard).";
    - "Navigation restorations: wording of the restored passages (資 «материалы; документы; данные», 原料/書類/材料
      «справочные сведения/материалы», 貸す «выдача во временное пользование») is compatible with the new titles; brackets
      only.";
    - "Unverified Russian usage to hand to the reviewers: «депо» for buses (Kuznetsov names rail/tram rolling stock only;
      «автобусный парк» may be preferred), «таби» (no Russian dictionary entry; example glosses only), «скрещение»,
      «внаём» (Kuznetsov entry found by the author).";
    - "Process incident (author): a relative-path PowerShell write resolved against the session's EN worktree and rewrote
      `words/資料.md` there with identical content (no diff). The coordinator also found an older, unrelated stray
      EN-worktree edit (`words/能力.md`, RU-only 知能 guard, dated to B196 authoring on 2026-11-19 20:35) and reverted it;
      the EN worktree is clean. Neither touched the RU primary checkout or any committed RU content.";
    - "Lane check after the B234 fix (verified by the coordinator against the candidate 75b2616): none of the 35 B235
      paths links to or quotes a B234 card changed by fix b850104 (近々, 補う, 退く, 農薬, 催促, 接する, 交通機関) or their
      old wording («в ближайшие дни», «торопить (с ответом)», «вести себя (с людьми)», «средства сообщения», «выплату
      возмещения», «регуляторы роста»); no B235 path is a B234 path. B235 titles are screened against the fixed B234
      titles at candidate time.";
    - "Candidate screen on the published B234 tree (main 1647191; b235-cand-screen.txt): 0 unguarded exact segments; the
      5 exact shared segments are guarded (転がる–ころころ and 転がる–ごろごろ «катиться», 転がす–倒す «опрокидывать», 足る–足りる
      and 足る–間に合う «быть достаточным»). Against the fixed B234 titles, only qualifier stem hits remain: 車輪, 車掌, 車庫
      and 貨物 share «поезд»/«автоб» with 交通機関's «(поезда, автобусы и т. п.)», and 交差 shares «дорог» with 退く «отойти
      с дороги» (different heads and senses; no guard). No change from the lane adjudication."

    The committed manifest records 5,169 entries (5,164 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. No reviewer ran
    the validator on the candidate.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 5 files with 6 restored navigation links (the kanji card 資 and the word cards 原料, 書類, 材料 and 貸す);
    - `manifest.json` (`contentVersion` `bf9f720376eac7d4`, 5,169 entries);
    - the intake, whose note reads "B235 30-card adaptation with six navigation-only link restorations in five existing
      files; candidate before blind review."
- Published baseline recorded in the intake: `1647191af5ef2fed02a2f6db5720b4b9d22fcbd3` (Batch 234 merge). Parent
  `b8314fd` adds only the Batch 234 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests (the authoring worktree run reported 124 tests);
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 5 files (6 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen: no unguarded exact title-segment overlap (31 `OK` lines for pairs already guarded by an exclusion and
    414 stem-only `!!` lines);
  - link parity: no EN link lost where the RU target exists; the only RU-only links are 資料:31 → 情報, 資料:32 → 材料 and
    貸間:33 → 下宿; for this record, no pre-existing RU-only link sits in a batch path.
- Common sample: all three reviewers read all 30 new word cards in full, and the five navigation-file diffs. The
  correctness and comprehensibility reviewers read each card against its complete frozen EN original. The consistency
  reviewer compared the EN originals by script, and checked the intake and manifest.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file), the link-only changes in kanji/資 and the word
    cards 原料, 書類, 材料 and 貸す (links activated without prose changes), relevant linked baseline passages, retained
    citations, Japanese example and reading text, and available-target link parity.
  - Retrieved the matching Jisho/JMdict entries for all 30 headwords and confirmed all 30 primary IDs from the actual
    pages' "Edit in JMdict" links, inspecting rare-spelling flags directly; a separate read-only extraction matched all 62
    primary Japanese example/reading pairs exactly, and the current normalized-byte hashes match the manifest for all 30
    cards.
  - Japanese sources beyond JMdict: Digital Daijisen on Weblio (cited: 輸血, 転がる, 転がす, 車掌, 車庫, 氏名, 踏切, 跳ねる,
    足る, 溜まる and 溜める).
  - Russian sources: Kuznetsov and Krysin on gramota.ru (кондуктор, депо, приз, внаём and запасти) and Russian Wiktionary
    (депо, скрещение, таби and постройка); scoped meaning checks, not frequency claims.
  - Ran no generator and no validator.
- Consistency review scope:
  - Read all 30 RU cards and all five navigation diffs in full; compared the EN originals by script.
  - Checked the intake's path list against the 35 content paths in the diff, and the manifest; it noted that 118 strokes
    manifest hashes differ from the raw sha256 (pre-existing, unchanged files).
  - Performed no dictionary re-verification. Its report records no validator or generator run.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN; read the link edits in kanji/資 and the word cards 原料, 書類, 材料 and 貸す from
    the diff, not as full articles; compared the titles of the named near-synonym cards where they exist.
  - Cited Digital Daijisen on Weblio (転がる, 賞金), Jisho/JMdict (賞品) and Russian Wiktionary (трофей, таби). It records no
    validator or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. The correctness
  report records the snapshot `75b2616` with HEAD verified and an empty `git status --porcelain` at start and completion;
  the consistency report records `75b2616` with a clean tree; the comprehensibility report records an empty
  `git status --porcelain` with HEAD matching the candidate. No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No reviewer reported running a generator: the correctness report says no repository edits or
  generators and lists no generator or validator run among its limits; the consistency report records no generator run;
  the comprehensibility report records no validator or generator run. No tracked repository file was changed.
- Full blind reports:
  - `235-words-batch-74-review-correctness-001.md`
  - `235-words-batch-74-review-consistency-001.md`
  - `235-words-batch-74-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The consistency brief made the intake record's path list the single exception, for its path check. The correctness
  report says that no forbidden reports or records were read. The consistency report makes no statement about unread
  materials; it records checking the intake path list. The comprehensibility report says that no other reviewer report,
  author report or batch record was read.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for 跳ねる, **CLEAN** for the other 29 new cards; scoped coverage **CLEAN** for all
30. Comprehensibility and quiz safety were not assigned or certified.

- C1 (minor, correctness; high confidence), `跳ねる.md:39`: `芝居が跳ねる（しばいがはねる）— «спектакль окончился»`
  translates the unmarked nonpast as a completed past; EN has "the show ends". The sense is right, but the tense mismatch
  teaches the wrong correspondence. Remedy: replace only «спектакль окончился» with «спектакль заканчивается», retaining
  the Japanese phrase, kana and surrounding explanation. Evidence: Jisho/JMdict 跳ねる, entry 1429620, sense 4 ("to come to
  an end; to close (for the day)"); Digital Daijisen は・ねる sense 4 `芝居などで、その日の興行が終わる`.

What the reviewer confirmed:
- The other 29 cards are CLEAN within this scope; no actionable loss of selected teaching points, prerequisites,
  distinctions or available source links was established.
- Source identities, readings, JLPT, type, kanji, tags and existing exclusions are retained; the added exclusions
  (賞品→賞金, 資料→材料/参考, 貸間→下宿, 貸し出し→支給) were checked for presence, not adjudicated for the quiz.
- No dropped links with existing RU targets, no dropped external citations and no broken links in these cards; the added
  word links are 資料→情報/材料 and 貸間→下宿, and unavailable RU targets remain plain text.
- It noted that the 貸し出し bicycle translation adopts the borrower's viewpoint, while the explanation still identifies
  the lender; no reversed lexical meaning was established.

Optional: 転がる's title could mention tumbling or lying down (the body preserves these senses; nonblocking polish);
車庫 «автобусный парк» is an editorial alternative, not a proven mandatory replacement. Limits: no native-speaker
certification, device, reader or archive test, full quiz review, or generator/validator run; frequency, exact modern
bus-depot usage and preferred register are not certified; no fresh KANJIDIC2 or historical-etymology audit; throttling
was overcome with paced retrieval, and failed or truncated outputs were not treated as evidence.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **CLEAN**; scoped integration **CLEAN**. Findings: none actionable.
Comprehensibility was not assigned to this review.

What the reviewer confirmed:
- The intake path list equals the 35 content paths in the diff.
- All 30 new RU cards and the five navigation diffs were read in full; the EN comparison was done by script.

Optional (nonblocking): the RU-added guards 資料→材料 and 貸間→下宿 are required, and 資料→参考, 賞品→賞金 and 貸し出し→支給
are conservative ("発行 shares «выдача» but is unguarded, minor inconsistency"); the unguarded neighbours 資料–情報/原料,
身分–現状 and 載る–刊行 are optional; 足る glosses 間に合う «годиться; хватать» against its title «успевать; быть
достаточным». Limits: 118 strokes manifest hashes differ from the raw sha256 (pre-existing, unchanged files); EN bodies
were compared by script; no dictionary re-verification.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (six minor items in 貸し出し, 転がる, 賞品, 賞金, 交差 and 足袋); no actionable
defect in the other 24 cards and the link-only edits; scoped coverage **CLEAN**.

- C1 (minor; high confidence), `貸し出し.md:21` (contradicts :43): the shop's 貸し出しをしています is translated from the
  borrower's side («можно взять»), while the card's own note says the lender issues and the reader borrows. Remedy: «— В
  этом магазине выдают велосипеды на время.» Evidence: EN "This shop rents out bicycles"; the note at line 43.
- C2 (minor; high confidence), `転がる.md:4` (and :12, :20): the title gloss «лежать где попало (брошенным)» covers only
  careless abandoned things, but the taught example is intentional lying down («Я улёгся на татами и читал книгу»).
  Remedy: title and H1 «катиться; ложиться; валяться (где попало)». Evidence: Digital Daijisen ころがる sense 3
  からだを横にする, with 畳の上に転がって新聞を読む; sense 4 is the separate careless-placement use.
- C3 (minor; high confidence), `賞品.md:4` (and :12, :23, :37): «кубок, трофей» is an unqualified second gloss narrower
  than «приз (вещью)», and «трофей» ordinarily means captured enemy property or a victory symbol. Remedy: title and H1
  «приз (вещью)», keeping «кубок или другой предмет» in the body. Evidence: JMdict via Jisho 賞品 "prize; trophy"; Russian
  Wiktionary «трофей» sense 1 military spoils, sense 2 symbol of victory.
- C4 (minor; high confidence that the example contradicts the card's gloss, medium that no speaker could hear «вручают»
  here), `賞金.md:21` (contradicts :18): 賞金が出ます is glossed on the card as «предусмотрен денежный приз», but the example
  says «вручают». Remedy: «— На этом конкурсе предусмотрен денежный приз.» Evidence: EN "This competition offers prize
  money"; Daijisen 賞金 «賞として与える金銭».
- C5 (minor; medium-high confidence), `交差.md:4` (and :12, :16): 交差 is a noun/する-verb, but the co-equal quiz gloss is
  the infinitive «пересекаться». Remedy: title and H1 «скрещение (линий, дорог); пересечение (друг с другом)». Evidence:
  front matter `tags: [kango, noun, suru]`; EN title "crossing; intersection".
- C6 (minor; medium-high confidence), `足袋.md:19–20`: «таби» appears only in the translations and is never introduced
  as a Russian word. Remedy: after line 16 add «В русских описаниях их называют «таби».» Evidence: Russian Wiktionary
  marks «таби» этногр.

Optional: delete `Карточка сохраняет исходное чтение かもつ.` in 貨物:40 («исходное» is author-facing); 足る's title
`(+ に足る)` is formula notation in a quiz title; 赤道 «термином кадастра» is opaque; 身分証明書 in 身分 has no kana reading.
None was scored. Limits: quiz metadata was not a facet; 貯蔵's added place particle で was not verified and is outside
these facets; checked and not treated as defects: 載る's passive «быть опубликованным», the adverbial 転々 title, the
qualified «депо», «подъём», «постройка», «внаём», «материалы» and «скрещение (линий, дорог)», 貸間's 下宿 line and the
parallel 蓄える/溜める frames; it noted that the English-only musical-conductor warning on 車掌 is correctly absent; model
identity not verifiable.

## Exclusion classification

All 137 EN exclusion entries (26 lists) are retained in EN order; 輸血, 車掌, 赤道 and 資料 have none in EN. Twelve of them
lie inside the batch. At the candidate, five direct, one-sided entries were added on four new cards: three appended to
three existing lists and one new list on 資料 (two entries); only 賞品→賞金 targets a batch word.

| Entries | Consistency reviewer |
|---|---|
| 資料→材料, 貸間→下宿 (2) | Required |
| 資料→参考, 賞品→賞金, 貸し出し→支給 (3) | Conservative ("発行 shares «выдача» but is unguarded, minor inconsistency") |

The author and the coordinator classed 資料→材料 and 貸間→下宿 as required and 資料→参考, 賞品→賞金 and 貸し出し→支給 as
conservative; the coordinator accepted all five as reported. The reviewer gave the same classes, adding the 発行 note, and
judged quiz safety CLEAN; all five entries are kept. The correctness reviewer checked the
added exclusions for presence only, and the comprehensibility reviewer did not audit the exclusion lists.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`235-words-batch-74-recheck-001.md`.
