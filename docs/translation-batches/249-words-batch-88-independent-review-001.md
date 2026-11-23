# Batch 249 — independent review 001

## Snapshot and scope

- Reviewed commit: `a8e87dd42d8d6fb01c89b03aa12b995550acc585` (tree `82d39083172fc5e751eed8b92d9932a1a19aa623`), branch
  `full-ru-249-words-88`, parent `35ae8ce`. The candidate was signed and pushed before review; its message reads "Batch
  249 candidate: 30 Russian word articles", followed only by the co-author trailer.
  - The content was authored in the scratch lane `learning-japanese-ru-b249`, whose local-only scratch commit `acc9bcc`
    ("B249 lane drafts on B242-B248 scratch") sits on `2d85e8d` ("B248 lane drafts on B242-B247 scratch"), itself on
    `bca83ec` ("B247 lane drafts on B242-B246 scratch"), `4ef6fa4` ("B242 fixes 1-3 synced onto B246 lane scratch") and
    the earlier lane scratch commits `b37a987` and `282ea33`. The coordinator's candidate script checked that the lane
    was clean at `acc9bcc` with parent `2d85e8d`, that the branch was `full-ru-249-words-88`, that HEAD was the Batch 248
    publication record and that HEAD~1 and `origin/main` were the expected published baseline, that the primary tree,
    including ignored files, was clean, that the ten navigation files edited in the lane were unchanged between
    `2d85e8d` and the published HEAD, and that none of the 30 new word files already existed.
  - The script copied 40 lane files (the 30 new cards and the navigation files `kanji/厚.md`, `words/みっともない.md`,
    `words/ゴール.md`, `words/ストップ.md`, `words/成長.md`, `words/止まる.md`, `words/相撲.md`, `words/苗代.md`,
    `words/西暦.md` and `words/誕生日.md`); no follow-up edit from an earlier fix was applied. It then regenerated the
    manifest, checked that the changed path set was exactly the 40 batch paths plus `manifest.json` and byte-compared
    all 40 copies with the lane. No link was held from an earlier batch. The script's byte scan of the content paths
    prints any BOM, CR or missing final newline rather than stopping; for this record the 40 committed blobs at
    `a8e87dd` (and again at the final fix `07ad251`) were checked: none has a BOM or CR, and every file ends with a
    newline, as `.gitattributes` requires.
  - After authoring and before the candidate commit, the coordinator edited lane cards: it retitled 番地, 公務, 役目,
    あてはめる, 住まい, 発売, スタート, 畳む and 申し訳ない and reworded examples or prose in 公務, 役目, 畳む, 申し訳ない,
    用途, 応用, 原産, 生長, 厚かましい, 生意気 and 生存; the ten navigation files were copied unchanged. Its adjudication
    record (lane `learning-japanese-ru-b249`, base `2d85e8d`, uncommitted) states:
    - "Scope: all 30 new cards read in full (Russian prose, examples, title/H1, links, footers) against frozen EN 6af98cb
      (8 cards read directly, the other 22 via an aligned EN/RU paragraph dump, b249-adj-read.txt; paragraph parity with
      EN for all 30); non-title metadata compared mechanically with EN (b249_cmp.py: all match except the two RU-added
      exclusions below). Link audit (rutools link_parity, 40 files): no lost links; one RU-only link (畳む →
      [広げる](広げる.md), accepted below). EN targets not yet published stay plain (words 特売 建つ あてはまる 生産地;
      kanji 畳 略 訳 植 応 請). Nav edits: 10 files / 10 links (kanji/厚 37; words/みっともない 36, ゴール 33, ストップ 29,
      成長 42, 止まる 53, 相撲 32, 苗代 38, 西暦 34, 誕生日 28); glosses unchanged; navonly 10 files / 10 links, only the
      expected NON-CARD manifest.json note. Title screen: every whole-segment overlap is guarded or stem-only."

      That plain list mixes three kinds of item: the three absent EN word link targets 特売 (from 発売), 建つ (from 発つ)
      and あてはまる (from あてはめる); 生産地, which EN 産地:29 mentions only in plain text and RU names in prose
      («生産地（せいさんち）обозначает район производства.»); and the six written kanji without an RU kanji card (EN links
      畳, 略, 訳 and 植 among them; EN has no card for 応 or 請). A mechanical count of `.md` link targets in EN finds 7 EN
      link occurrences to 7 absent RU targets (発売→words/特売, 発つ→words/建つ, あてはめる→words/あてはまる, 畳む→kanji/畳,
      略す→kanji/略, 申し訳ない→kanji/訳, 田植え→kanji/植). The closing screen sentence covers whole segments only: the four
      住まい «место» lines are unguarded and are discussed below;
    - the edits, each with its recorded reason:
      - 番地: title/H1 «номер участка (в адресе); адрес в памяти (компьютера)» → «номер участка или дома (в адресе);
        адрес» ("the draft narrowed EN "address" to computer memory");
      - 公務: title/H1 → «официальные обязанности; государственные дела»; ex2 → «Я разделяю официальные обязанности и
        личную жизнь.»; synonyms «может входить в официальные обязанности» ("«служебные обязанности» is too generic for
        EN "official public duties"");
      - 役目: title/H1 «отведённая роль; предназначение» → «обязанность; роль; предназначение»; ex1 → «Моя роль — вести
        протокол совещания.» ("the title dropped EN "duty" (every EN title sense needs a segment, B243 lesson);
        «отведённая роль» was clunky");
      - あてはめる: title/H1 → «применять (правило к случаю); подставлять (в формулу); вписывать (в категорию)» ("the
        draft narrowed "fit into" to formula substitution");
      - 住まい: title/H1 «кров; место, где живут» → «жилище; место, где живут» (body unchanged) ("«кров» is bookish");
      - 発売: title/H1 «выход в продажу; поступление в продажу» → «выход в продажу» ("redundant second segment");
      - スタート: title/H1 «момент старта; отправная точка» → «старт; отправная точка» ("«момент старта» is awkward");
      - 畳む: title/H1 → «складывать (бельё, зонт, футон); закрывать своё дело»; meaning line «складывать,
        сворачивать…», «то, что складывают…»; ex1 → «Я сложил постиранное бельё и убрал его на полку.»; «сложить и
        убрать», «складыванию в компактную форму» ("«складывать» is the natural verb for laundry and umbrellas (折る is
        guarded)");
      - 申し訳ない: title/H1 «мне нет оправдания; непростительно» → «простите; непростительно»; ex1 → «Простите, что
        заставил вас ждать.» ("register: «мне нет оправдания» is too heavy for routine お待たせして申し訳ありません");
      - 用途: ex1 → «Расскажите, пожалуйста, для чего служит этот инструмент.» ("natural Russian; matches the card's
        «для чего служит X» pattern");
      - 応用: ex1 → «Я применяю полученные знания в работе.» ("redundant «на практике в работе»");
      - 原産: ex1 → «Это растение родом из Южной Америки.»; ex2 → «Я выясняю, где родина этого фрукта.» ("natural
        Russian («родом», «родина» for a plant's origin); faithful to EN");
      - 生長: ex1 → «Рассада хорошо растёт.»; ex2 → «Каждую неделю мы фиксируем рост растений.» ("natural Russian; ex2
        keeps the noun as object, as the following EN note requires");
      - 厚かましい: ex2 «Простите за беззастенчивую просьбу, но…» → «Простите за наглую просьбу, но…» ("idiomatic
        Russian for 厚かましいお願いですが");
      - 生意気: ex1 → «Простите, что позволил себе дерзкие слова.» ("the draft was calqued and awkward");
      - 生存: ex1 → «После аварии подтвердилось, что три человека живы.»; ex2 → «Эта рыба может выжить даже в холодной
        воде.» ("natural Russian, faithful to EN");
    - accepted as drafted: "Faithful as drafted: 略す 発つ 住居 留守番 留まる 申請 田植え 実用 当番 用語 産地 ずうずうしい
      生年月日 人命 (plus the edited cards' unchanged prose).";
    - "略す title kept: «опускать» would collide with unguarded 下げる/下ろす/降ろす and «сокращать» with 減らす.";
    - "申し訳ない alternatives «приношу извинения» / «прошу прощения» rejected: near-duplicates of unguarded 詫びる
      «приносить извинения; просить прощения».";
    - "RU-only link 畳む → [広げる](広げる.md): a substantive antonym comparison; target already in RU.";
    - "RU-added exclusions (direct pairs on new cards only): 住まい→住居 (required: «место, где живут» vs «место
      проживания»), 用途→応用 (conservative: shared «применение»).";
    - "English-dependent EN notes adapted: 人命 singular/plural "life" (now about Russian number); 応用 and あてはめる
      English "apply" polysemy (now a direct 塗る / 申し込む contrast).";
    - "Nav gloss «наглый; бесстыдный» in kanji/厚 left unchanged (navigation-only edit), although the card title is
      «наглый; беззастенчивый».";
    - "Validation after edits (lane): manifest 5,589 files (version 88d083ee4368de1b); validate 0 errors; 124 tests OK;
      budget OK (5,606 entries; localZipBytes 8,101,858); link parity: only the accepted RU-only 畳む→広げる link (40
      files); navonly 10 files / 10 links; diff --check clean; paragraph parity with EN for all 30."

    The lane `contentVersion` differs from the candidate's because the lane tree carries its own copies of earlier lane
    drafts; the entry count is the same.

    Fix 1 later rewrote the adapted 応用:33 and あてはめる:33 contrast (comprehensibility C1 and C2; see the recheck
    record): the 申し込む comparison and its link are gone, and the 塗る contrast is now framed in Russian terms. The
    coordinator's titles and other edits stand. Fix 1 also changed 略す, 発つ, 留まる, 申請, 田植え and 実用, which the
    coordinator had accepted as drafted, and passages the coordinator had left unchanged in 申し訳ない (line 33), 役目
    (line 41), 原産 (line 33) and 住まい (line 18).

    The committed manifest records 5,589 entries (5,584 `files`, 3 images and 2 scenes; `contentVersion`
    `ff40e930d163cbc9`); the coordinator's lane `validate.py` run and its phase-1 `tools/validate.py` run on the
    candidate content reported 0 errors. The correctness and consistency reviewers also ran the validator on the
    candidate (0 errors each).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 10 files with 10 restored navigation links (the kanji card 厚 and the word cards みっともない, ゴール, ストップ, 成長,
      止まる, 相撲, 苗代, 西暦 and 誕生日);
    - `manifest.json` (`contentVersion` `ff40e930d163cbc9`, 5,589 entries);
    - the intake, whose note reads "B249 30-card adaptation with ten navigation-only link restorations in ten existing
      files; candidate before blind review."

    Against the published baseline the candidate changes 43 files (1,464 insertions, 21 deletions), including the
    parent's publication record; the candidate commit itself changes 42 files (1,384 insertions, 21 deletions).
- Published baseline recorded in the intake: `0bb92c888c6d17d2e45306ac77c4c6ada0418708` (Batch 248 merge, PR #132).
  Parent `35ae8ce` ("Record B248 publication verification") adds only the Batch 248 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace, navigation-only or tracking-ledger check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 10 files (10 links added, no other change);
  - tracking-ledger pre-check (the 30 new word paths are exactly the batch paths not yet in the ledger).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b249-cand-screen.txt`, 588 lines): 65 `OK` lines for pairs already guarded by an exclusion and 523
    `!!` lines. It has 15 exact-segment lines. Eleven are `OK`, each guarded by the batch card's own EN entry:
    スタート–始め «старт», 畳む–折る «складывать», 住まい–宅 and 家 «жилище», 番地–住所 «адрес», 申し訳ない–お待ちどおさま and
    すみません «простите», and 役目–務め, 役, 役割 and 義務 («обязанность»/«роль»). Four are `!!`: 住まい–場, 場所, 所 and 陰
    «место», which the author report declined («место» is qualified by «где живут», and the leading «жилище» separates
    the whole titles). All other lines are stem-only. `b249-screen.txt` (588 lines, the lane screen) differs from the
    candidate screen in ten stem-only lines on each side, which show the published titles of おやすみ, 書留, 先頭, 純粋
    and 直前 (for example 書留 «заказное отправление; письменная запись» and 直前 «непосредственно перед; прямо перед»)
    instead of the lane's pre-publication copies («заказное отправление; письменная отметка», «непосредственно перед
    (по времени); прямо перед (в пространстве)»). No exact-segment line differs. `b249-title-screen.txt`,
    `b249-title-screen2.txt` and `b249-title-screen3.txt` are earlier screens with 住まい's pre-adjudication title «кров;
    место, где живут»; their only exact-segment lines are the four 住まい «место» lines;
  - link parity: "checked 40", no LOST link and one EXTRA, the RU-only link `words/畳む.md` → `words/広げる.md`. For this
    record link parity was verified again at `a8e87dd` with the same result. At `07ad251` it reports the same EXTRA and
    four LOST links that fix 1 removed by design (see the recheck record).
- Common sample: all three reviewers read all 30 new word cards in full, with the coverage of the EN side stated per
  reviewer below, and all three read the ten navigation diffs. The consistency reviewer also checked the intake paths
  and hashes and recomputed the manifest in memory; the correctness reviewer checked the current titles and readings of
  all linked word targets.
- Correctness review scope:
  - "Model identity is not independently verifiable. The complete RU body and front matter of EACH file below were read
    against its complete frozen EN original", followed by the 30 cards; "Also inspected the candidate's existing-card
    link-restoration diffs: kanji/厚.md; words/みっともない.md, ゴール.md, ストップ.md, 成長.md, 止まる.md, 相撲.md, 苗代.md,
    西暦.md, 誕生日.md. These were link-only changes, not new Japanese claims. Comparison checks included current
    titles/readings of all 99 linked word targets and complete reused bodies of 止まる, 成長, 広げる, 留守, 公務員 and 経つ."
  - "Inspected actual Jisho/JMdict forms, senses and parts of speech for all 30 words, then checked the cited primary
    entry numbers against the pages' actual JMdict edit links. The IDs match"; "Independently read the named Digital
    Daijisen sections, not merely other dictionaries on Weblio."; on/kun claims were checked "against actual
    https://kanjiapi.dev/v1/kanji/<character> responses" ("shell kanjiapi requests returned 403, but actual responses
    were obtained through web_fetch"); eight Russian words (бесстыжий, беззастенчивый, произрасти, присмотреть,
    отбывать, обременить, оборваться, исконный) were checked "against actual Gramota entries"; "All 30 jlpt: 2 labels and
    selected entry identities match the frozen docs/n2-vocabulary-sources.tsv rows"; "All 60 Japanese example sentences
    and their kana readings match EN verbatim."
  - "Ran the primary checkout's validator directly with python -X utf8 -B: exit 0, "0 error(s)". No generator, checkout,
    staging or repository edit was performed."
- Consistency review scope:
  - "Read in full: all 30 new RU word cards, and all 10 navigation-only diffs (`git diff -U0` against parent
    `35ae8ce`)."
  - "Verified programmatically against EN: front matter, link sets, heading counts, footer entries and sense numbers.
    An in-memory manifest recompute equals the committed `manifest.json`. The intake JSON holds 40 payload paths equal
    to the 40 content-diff files, and all candidate hashes match; it contains no learner content. Titles of all 4123 RU
    words were screened for semantic overlap with the 30 new titles."
  - "`python tools/validate.py`: 0 errors."
  - Incident: "the in-memory manifest check created `tools/__pycache__`. I deleted it, and the tree is clean."
  - Limits: "No independent dictionary access beyond the cards' own citations."; "The title screen is a lead generator,
    not a verdict. About 520 flagged rows were mostly stem-only noise."; "Semantic judgments on the Q1 and Q2 guards and
    the optional items are mine. They are not tested against learner quiz output."
- Comprehensibility review scope:
  - "Read in full, RU and EN:" followed by the 30 cards; "Compared related RU titles (販売, 始め, 出発, 住所, 家, 住宅, 残る,
    適用, 使用, 行事, and the brief's near-synonym set). Link parity on repo-relative paths: no dropped EN link whose RU
    target exists; only extra is 畳む→広げる, which matches 広げる's title. Title screen used as a lead, not a verdict.
    Model: not verifiable."
  - Its limits record "Dictionary checks used the cards' cited JMdict ids plus Jisho for 原産 (1261470: "place of
    origin; habitat") and 発つ/立つ (depart sense, oft. 発つ). Daijisen pages were not re-opened beyond the cards'
    citations. No claim about quiz runtime behaviour." It records no validator run and makes no statement about
    generators.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `3134ada8-413b-458f-8d02-46df480b28f7`,
  `400f769f-e41b-4eaf-9eb8-9693b3ace6f4` and `cebd0da4-142e-4c2f-88a4-ab3601a2ad9e`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model identity
  is not independently verifiable.", the consistency report "Model identity cannot be verified from inside the
  session." and the comprehensibility report "Model: not verifiable."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "Primary checkout HEAD matches; git status --porcelain
  is empty."; the consistency report records "`git status --porcelain` empty at start and at end."; the
  comprehensibility report records "HEAD matches; `git status --porcelain` empty (no uncommitted changes)". No fix was
  applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No generator, checkout, staging or repository edit was
  performed."; the consistency report recomputed the manifest only in memory and records the transient
  `tools/__pycache__` it created and deleted; the comprehensibility report makes no statement about generators. No
  reviewer reported changing a tracked repository file.
- Full blind reports:
  - `249-words-batch-88-review-correctness-001.md`
  - `249-words-batch-88-review-consistency-001.md`
  - `249-words-batch-88-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch lane worktrees.

  As in earlier batches, the consistency brief made one exception: the intake record, "check only that its path list
  matches the candidate's content diff and that it adds no learner content". The consistency report records "The
  intake JSON holds 40 payload paths equal to the 40 content-diff files, and all candidate hashes match; it contains no
  learner content." The correctness report states "No author/reviewer report, prohibited scratch checkout, RU batch
  record or tracking ledger was consulted."; the comprehensibility report states "Blind: intake, batch records and
  other reviews unread."; the consistency report makes no separate statement about the other sources.

## Initial verdicts and findings

### Correctness

Verdicts: "Correctness CLEAN; scoped coverage CLEAN, for all 30 listed articles. No per-article exception. CLEAN means
no actionable defect established, not proof of exhaustive correctness. Russian comprehensibility and quiz quality are
not separately scored."

Findings: "None." Optional: "None proposed within the assigned facets."

What the reviewer confirmed: "All 60 Japanese example sentences and their kana readings match EN verbatim. A separate
Japanese-token comparison found no lost lexical phrase except the template label 地域名 in 原産, correctly translated as
"название местности"."; "Non-title front matter is preserved, except the two deliberate added guards: 住まい → 住居 and
用途 → 応用. Both are defensible direct overlap protections."; "Every EN link to an existing RU target survives. The seven
absent-target links remain plain text: kanji/畳, 略, 訳, 植 and words/特売, 建つ, あてはまる. Their teaching content remains.
畳む's added 広げる link exists and its "раскладывать, разворачивать" gloss fits that card."; the JMdict IDs of all 30
words; Digital Daijisen confirmations for 住まい, 住居, 略す, 留まる, 申し訳ない, 生長/成長, 図々しい, 生意気 and the noun
cards; kanjiapi.dev readings ("These checks establish readings, not historical etymology."); "The omitted English-only
"on sale" ambiguity and English tense-ending warning do not remove the Japanese points"; "Rebuilt apply/application,
function, life and apology comparisons preserve the Japanese distinctions and their qualifications."; "No consequential
tense, polarity, transitivity, gender or subject error was established in the Russian examples."; and the eight Gramota
entries, including отбывать ("departure sense, separately from serving a sentence.")

Limits: "This is not an app/reader acceptance test, full-corpus synonym audit, native-speaker certification or
historical-etymology study. Existing neighboring articles were not all re-reviewed in full. Quiz candidate behavior and
Russian beginner readability remain outside the assigned verdicts. Initial Jisho rate limits were resolved with
throttled follow-up; shell kanjiapi requests returned 403, but actual responses were obtained through web_fetch. No
consequential source check remained blocked."

### Consistency and quiz safety

Verdicts: "Consistency, links, metadata, manifest, intake: **CLEAN**."; "Quiz safety: **NEEDS FIX** (Q1 and Q2, both
low-to-medium severity, moderate confidence)."

- Q1, `words/略す.md`: "略す «сокращённо называть (записывать); опускать подробности» can share "сокращать" with 減らす
  «уменьшать; сокращать». EN already guards 縮める, which has the same overlap." Remedy: append 減らす
  (`[省略, 省く, 縮める, 抜く, 削除, 詰める, 略語, 除く, 削る, 飛ばす, 減らす]`).
- Q2, `words/申し訳ない.md`: "申し訳ない «простите; непростительно» vs 詫びる «приносить извинения; просить прощения».
  詫びる already lists 申し訳, but the contract is symmetric and applies to direct pairs, so the pair must be declared on
  at least one side. The same relation is already guarded for 謝る." Remedy: append 詫びる.

What the reviewer confirmed: "Front matter matches EN for all 30 cards. The only differences are the two RU-introduced
guards: 住まい→`住居` and 用途→`応用`, both appended last. All EN exclusions are retained."; "Link sets match EN, except
for EN links whose RU target does not exist, which stay plain (correct by convention): 発売 (特売), 発つ (建つ), あてはめる
(あてはまる), and kanji 畳, 略, 訳, 植 (in 畳む, 略す, 申し訳ない, 田植え). I confirmed these RU files are absent."; "The 10
navigation files each change exactly one target link. Paths are correct. No RU-only links appear, and plain-mention
counts match EN. The only EN-only link is kanji/苗 in 苗代, which is pre-existing because RU `kanji/苗.md` is absent." (The
"No RU-only links" sentence concerns the navigation files; the report lists 畳む → 広げる separately under Optional.);
"No exact-title duplicates among the batch words."

Optional (nonblocking): "`畳む` links `広げる.md`, which EN leaves plain. The target card exists and its title fits the
gloss. This is an acceptable substantive antonym link."; "`止まる.md` line 53: «другое чтение [留まる] — とどまる» is
slightly ambiguous, since 留まる can be read とまる or とどまる. Suggested wording: «отдельная статья [留まる](留まる.md) учит
чтению とどまる — «оставаться; пребывать»»."; weak overlaps "judged not required": 役目 vs 用, 番地 vs 番, 発売 vs 刊行 and
発行, 留守番 vs 預かる and 預ける, 生長 vs 増加; "厚かましい has no `quiz_exclusions` key. This is fine because the
neighbouring words declare one-way guards and EN has no key either."; "In-batch pairs that share only a stem and no
sense need no guards".

Limits: the dictionary, screening and semantic-judgement limits quoted above.

### Comprehensibility and scoped coverage

Verdicts: "comprehensibility NEEDS FIX; scoped coverage NEEDS FIX (発つ only; other 29 articles CLEAN)".

All twelve findings are comprehensibility findings, and C7 also concerns scoped coverage; C1, C2, C3, C4, C6 and C8 are
medium severity and C5, C7, C9, C10, C11 and C12 low; confidence is high except for C12 (medium).
- C1 (medium), `words/応用.md:33`: "The sentence says прикладная физика is not a job application, and that painting or
  filing an application are not 応用. Russian «практическое применение» and «прикладной» do not mean those things, so
  the warning has no target and can invent a false link to приём на работу." Remedy: a replacement sentence about
  «прикладной» in 応用物理学.
- C2 (medium), `words/あてはめる.md:33`: "«Наносить краску» and «подавать заявку на курс» reject senses the Russian
  glosses never show." Remedy: delete the first two sentences; keep the rule-appropriateness sentence.
- C3 (medium), `words/申請.md:33`: "«Это не «применение» правила или метода, как в 適用» warns against a reading that
  «заявление; ходатайство» does not have." Remedy: delete only the 適用 sentence.
- C4 (medium), `words/役目.md:41`: "«не мероприятие» rejects a sense none of «обязанность; роль; предназначение» has."
  Remedy: delete the sentence.
- C5 (low), `words/申し訳ない.md:33`: "«чувство грусти» and «сочувствие чужой беде» are the English "I'm sorry" =
  sad/condolence warning". Remedy: delete the first sentence only.
- C6 (medium), `words/発つ.md:4`: "Quiz gloss «отбывать» without «в путь» is current Russian for serving a sentence or a
  posting, not for leaving on a trip." Remedy: title and H1 «уезжать; отправляться в путь»; line 16 «発つ — уезжать,
  отправляться в путь.»
- C7 (low; comprehensibility and scoped coverage), `words/発つ.md:33`: "The homophone note names 建つ with no reading."
  Remedy: «и 建つ（たつ） — о том, что строение возводится.»
- C8 (medium), `words/実用.md:29`: "«практическое применение» is the quiz title of 応用, so the contrast the titles try to
  draw (использование/практичность vs применение знаний) collapses in the paragraph that should keep them apart." Remedy: «…пригодность в реальном деле…».
- C9 (low), `words/原産.md:33`: "«Словарный перевод «место обитания» здесь нуждается в уточнении» points at a gloss the
  card never shows." Remedy: «Это исходное происхождение, а не место, где растение или животное находится сейчас.»
- C10 (low), `words/役目.md:27`: "«в этой коллекции» and «с тегом смешанного чтения» describe cataloguing the learner
  cannot see (`type`/`tags`)." Remedy: «Чтение соединяет онное やく и японское め. Это не два онных чтения; учите слово
  целиком.»
- C11 (low), `words/留まる.md:19`: "«Ущерб не вышел за пределы небольшого масштаба» is a calque." Remedy: «Ущерб не вышел
  за рамки небольшого.»
- C12 (low; confidence medium), `words/住まい.md:18`: "«Я ищу новое место, где жить» is missing a finite verb and reads
  like a place-word". Remedy: «Я ищу новое жилище.»

Optional: "words/畳む.md:4 «футон» is not glossed"; "words/生長.md:4 «произрастание» is bookish"; "words/田植え.md:33 «в
просмотренных словарных статьях» describes the author's check"; "words/あてはめる.md:4 is long but the three senses are
real."; "words/住居.md:18 «жилое помещение» is stiff and matches the formal noun; not a defect." Outside its facet:
"始め's quiz_exclusions omit スタート despite the shared segment «старт» (スタート lists 始め); 厚かましい has no
quiz_exclusions while ずうずうしい lists it." It also judged several passages to have a Russian target: "発売:21/:33 on
«скидке» is kept because the card itself introduces 特売. スタート:33, 人命:16/:29, 生意気:25/:33 and 役目:25 have a Russian
target." Limits: the dictionary and quiz-runtime limits quoted above.

## Exclusion classification

All 222 EN exclusion entries (29 lists; EN has none on 厚かましい) are retained in EN order. 15 of them lie inside the
batch, and the other 207 target existing RU cards. At the candidate, two direct, one-sided entries were added on two
new cards, each appended at the end of its list: 住まい→住居, which targets a batch word, and 用途→応用, which also
targets a batch word. Neither reverse side declares the pair (住居 lists no 住まい, and 応用 lists no 用途).

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 住まい→住居 (1) | "(required: «место, где живут» vs «место проживания»)" | "**required**. The titles «жилище; место, где живут» and «жилое помещение; место проживания» are near synonyms." |
| 用途→応用 (1) | "(conservative: shared «применение»)" | "**conservative but acceptable**. Both revolve around "применение"; 応用→用途 is not guarded, which is fine because the declaration is one-way." |

The coordinator and the consistency reviewer agree on both classes. The correctness reviewer found that "Both are
defensible direct overlap protections." and noted that "The frozen docs/content-format.md explicitly says a declaration
on either card protects both directions; reciprocal declarations are not required." The comprehensibility reviewer did
not classify them. The consistency reviewer's findings Q1 (略す→減らす) and Q2 (申し訳ない→詫びる) are not candidate
entries; fix 1 adopted both.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`249-words-batch-88-recheck-001.md`.
