# Batch 250 — independent review 001

## Snapshot and scope

- Reviewed commit: `4a5e70f1dff84c8e692a1d3c7f9c7c7bd01ce45c` (tree `bd733755f1232bb0d1e2ece9ccb4a0a15b5eeba6`), branch
  `full-ru-250-words-89`, parent `9f5e709`. The candidate was signed and pushed before review; its message reads "Batch
  250 candidate: 30 Russian word articles", followed only by the co-author trailer.
  - The content was authored in the scratch lane `learning-japanese-ru-b250`, whose local-only scratch commit `819ee18`
    ("B250 lane drafts on B243-fix/B249 scratch") sits on `c123f7f` ("B243 blind-review fix 6aa1bca synced onto B249
    lane scratch"), itself on `acc9bcc` ("B249 lane drafts on B242-B248 scratch") and the earlier lane scratch commits
    `2d85e8d`, `bca83ec`, `4ef6fa4` and `b37a987`. The coordinator's candidate script checked that the lane was clean at
    `819ee18` with parent `c123f7f`, that the branch was `full-ru-250-words-89`, that HEAD was the Batch 249 publication
    record and that HEAD~1 and `origin/main` were the expected published baseline, that the primary tree, including
    ignored files, was clean, that the fifteen navigation files edited in the lane were unchanged between `c123f7f` and
    the published HEAD, and that none of the 30 new word files already existed.
  - The script copied 45 lane files (the 30 new cards and the navigation files `kanji/卒.md`, `kanji/危.md`,
    `kanji/定.md`, `kanji/規.md`, `words/いかがわしい.md`, `words/バイオリン.md`, `words/ピアノ.md`, `words/奇しい.md`,
    `words/女王.md`, `words/妖しい.md`, `words/学会.md`, `words/挿す.md`, `words/疑わしい.md`, `words/発売.md` and
    `words/課程.md`); no follow-up edit from an earlier fix was applied. It then regenerated the manifest, checked that
    the changed path set was exactly the 45 batch paths plus `manifest.json` and byte-compared all 45 copies with the
    lane. No link was held from an earlier batch. The script's byte scan of the content paths prints any BOM, CR or
    missing final newline rather than stopping; for this record the 45 committed blobs at `4a5e70f` (and again at the
    fix `9e339f5`) were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - After authoring and before the candidate commit, the coordinator edited lane cards: it retitled 瓦, 倉庫, 独り言,
    生ずる and 物語る, reworded example 1 of 生ずる and 物語る, and rewrote the オルガン homograph paragraph; it also
    dropped one drafted RU-added exclusion (王女→王子). The fifteen navigation files were copied unchanged. Its
    adjudication record (lane `learning-japanese-ru-b250`, base `c123f7f`) states:
    - "Scope: all 30 B250 word cards (`b250-words.txt`) read against frozen EN `6af98cb7` in `b250-adj-read.txt`, plus
      the 15 navigation files (21 links) in lane `learning-japanese-ru-b250` on base `c123f7f`. Edits applied with
      `b250_coord.py` (exact-once replacements)."
    - the edits, each with its recorded reason:
      - 瓦: "title/H1 «черепица; черепичная плитка» → «черепица»" ("redundant second segment");
      - 倉庫: "title/H1 «склад; складское помещение» → «склад»" ("redundant second segment («хранилище» would collide
        with 金庫)");
      - 独り言: "title/H1 «…; монолог наедине с собой» → «разговор с самим собой; монолог»" ("JMdict "soliloquy;
        monologue"; redundant qualifier");
      - 生ずる: "title/H1 «зарождаться; влечь за собой; приводить к чему-либо» → «возникать; порождать; вызывать»; ex1
        «зарождаются проблемы» → «возникают проблемы»" ("EN "arise; produce; cause" (same as 生じる); «зарождаются
        проблемы» unidiomatic; 生じる/起こる already excluded");
      - 物語る: "title/H1 «поведать; …» → «рассказывать; свидетельствовать (о чём-либо)»; ex1 «поведал» → «рассказал»"
        ("imperfective-infinitive title convention; «поведать» bookish/perfective; 語る/話す already excluded");
      - オルガン: "distinctive paragraph: Russian «орга́н» is only a homograph of «о́рган» (body part, government body),
        different stress" ("draft claimed the same word "also means" these");
      - 王女: "`quiz_exclusions` drop RU-added 王子" ("no shared segment or meaning overlap (принцесса vs принц is a
        valid distractor); EN excludes only 女王");
    - accepted as drafted: "Unchanged cards judged faithful: 生る 生け花 生える 甘やかす 瓶詰 楽器 琴 学部 学科 理科 現に
      率直 献立 特色 特長 指定 特定 特売 怪しい 危うい 物騒 物置 定規 (plus the edited cards' unchanged prose), including
      restructured-but-complete 琴 率直 献立 指定 怪しい (paragraphs merged; content complete).";
    - "特定 title «конкретный; выявление (причины, лица)» kept: EN "specifying" is taught in the body; adding
      «указание» would create a new overlap with 示す.";
    - "RU-added exclusions kept (direct pairs on new cards only): 生る→実, 収穫 («плод(ы)»); 瓶詰→缶詰 («банка» =
      jar/can); 楽器→器具 («инструмент»); 学科→学問 («дисциплина»); 特色→癖 («особенность»); 特長→武器 (required:
      «сильная сторона/черта»), 長短, 節 (conservative); 指定→示す, 定期; 特定→具体; 特売→発売 (conservative); 危うい→重体
      («угроз-»); 物置→押し入れ (conservative, storage space), 貯蔵 («хранени-»); 独り言→会話, 話 (conservative: shared
      «разговор»).";
    - "English-specific EN notes adapted: 生える "cut teeth"; 物語る English "tell"; オルガン English "organ" (now
      Russian homograph).";
    - "Kanji/article links dropped where the target is absent in RU (甘やかす, 瓶詰, 怪しい); 怪しい's article mention is
      plain.";
    - "指定席 gloss «место, указанное в билете» acceptable.";
    - "Validation after edits (lane): manifest 5,619 files (version dd58847bc3fbf858); validate 0 errors; 124 tests OK;
      budget OK (5,636 entries; localZipBytes 8,148,460); link parity over 45 files: no LOST; EXTRA only pre-existing
      RU-only links in already-published nav files (kanji/危 → 急, 危ない; バイオリン → 弾く; 学会 → 社会), present at
      `c123f7f`; navonly 15 files / 21 links / 0 problems; diff --check clean; no BOM/CR/missing EOL (46 paths)."

      The plain-link sentence names only the cards 甘やかす, 瓶詰 and 怪しい. A mechanical count of `.md` link targets in
      EN finds 7 EN link occurrences to 7 absent RU targets in the new cards: two word cards (生える→words/枯れる,
      学科→words/学級) and five kanji cards (甘やかす→kanji/甘, 瓶詰→kanji/瓶 and kanji/詰, 怪しい→kanji/怪,
      倉庫→kanji/庫). That count does not match `../articles/` hrefs; separately, 怪しい's EN link to the article
      `ayashii-and-related-words.md` (EN 怪しい:46), which is absent in RU, is plain text at RU 怪しい:47–48. 瓶詰 keeps
      its EN links to the existing word cards 詰める, 缶詰, 瓶 and 保存. All seven absent targets and the article link stay
      plain at the candidate and at the fix.

    The lane `contentVersion` differs from the candidate's because the lane tree carries its own copies of earlier lane
    drafts; the entry count is the same.

    Fix 1 later changed two coordinator-edited cards again: 独り言 (title «разговор с самим собой; монолог» → «разговор с
    самим собой», line 17 rewritten) and 生ずる (title «возникать; порождать; вызывать» → «возникать; порождать», line 16
    rewritten); 生ずる's example 1 «В плане иногда возникают проблемы.» is unchanged. It also modified the kept 特定 title
    (the parenthetical «(причины, лица)» removed; final «конкретный; выявление»), and changed 瓶詰, 怪しい, 物騒, 危うい,
    献立 and 学部, which the coordinator had accepted as drafted (see the recheck record). The coordinator's other edits
    and its exclusion decisions stand.

    The committed manifest records 5,619 entries (5,614 `files`, 3 images and 2 scenes; `contentVersion`
    `bddfd3e4d9e4aa9d`); the coordinator's lane `validate.py` run and its phase-1 `tools/validate.py` run on the
    candidate content reported 0 errors. The consistency reviewer also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 15 files with 21 restored navigation links (the kanji cards 卒, 危, 定 and 規 and the word cards いかがわしい,
      バイオリン, ピアノ, 奇しい, 女王, 妖しい, 学会, 挿す, 疑わしい, 発売 and 課程);
    - `manifest.json` (`contentVersion` `bddfd3e4d9e4aa9d`, 5,619 entries);
    - the intake, whose note reads "B250 30-card adaptation with twenty-one navigation-only link restorations in
      fifteen existing files; candidate before blind review."

    Against the published baseline the candidate changes 48 files (1,801 insertions, 37 deletions), including the
    parent's publication record; the candidate commit itself changes 47 files (1,721 insertions, 37 deletions).
- Published baseline recorded in the intake: `ed6aa52956367226e86fb3ef125c0d5eb612c766` (Batch 249 merge, PR #133).
  Parent `9f5e709` ("Record B249 publication verification") adds only the Batch 249 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace, navigation-only or tracking-ledger check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 15 files (21 links added, no other change);
  - tracking-ledger pre-check (the 30 new word paths are exactly the batch paths not yet in the ledger).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b250-cand-screen.txt`, 321 lines): 43 `OK` lines for pairs already guarded by an exclusion and 278
    `!!` lines. It has 3 exact-segment lines. Two are `OK`, each guarded by the batch card's own EN entry: 生ずる–生じる
    («возникать», «порождать») and 物語る–語る («рассказывать»). One is `!!`: line 12, 生ずる–呼ぶ «вызывать» (consistency
    F4 and comprehensibility C1 below). All other lines are stem-only. `b250-screen.txt` (321 lines, the lane screen)
    differs from the candidate screen in one stem-only line on each side, 率直 ~ 直前: the candidate screen shows the
    published 直前 title «непосредственно перед; прямо перед», the lane screen the lane's pre-publication copy
    («непосредственно перед (по времени); прямо перед (в пространстве)»). No exact-segment line differs; its line 12 is the same 生ずる–呼ぶ line, which the dispositions
    cite as "the candidate screen (`b250-screen.txt:12`)". `b250-screen-out.txt` (336 lines) is the author's earlier
    lane screen, with no exact-segment line;
  - link parity: "checked 45", no LOST link and four EXTRA links, all RU-only links in navigation files that predate
    this batch: kanji/危 → kanji/急 and → words/危ない, words/バイオリン → words/弾く and words/学会 → words/社会. Each set
    is identical at the published baseline `ed6aa52` and at the fix `9e339f5`, and EN has none of them. For this record
    link parity was verified again at the fix with the same result.
- Common sample: all three reviewers read all 30 new word cards in full against EN, and all three read the fifteen
  navigation diffs. The consistency reviewer also checked the intake path list and recomputed the manifest in memory.
- Correctness review scope:
  - "Model identity not independently verifiable. No other agents used. Each following RU words/<name>.md and its
    frozen EN counterpart was read IN FULL", followed by the 30 cards; "Restored links in the four changed kanji cards
    and eleven existing word cards were reviewed as bounded diffs, not as full-card audits."
  - "Inspected the exact primary JMdict entry IDs/senses for all 30 new cards, plus relevant comparison entries;
    inspected cited Japanese usage entries and additional Daijisen/Kotobank definitions. Checked Russian lexical claims
    against actual Gramota and supplementary Wiktionary entries. Checked component readings in primary KANJIDIC2 and all
    30 vocabulary-level mappings against the EN N2 source index/policy."
  - "No validator, generator, build, app test, or native-speaker acceptance check run. kanjiapi requests returned HTTP
    403; component readings were instead checked in https://www.edrdg.org/kanjidic/kanjidic2.xml.gz ."
- Consistency review scope:
  - "Read in full: all 30 new RU cards, each against its frozen EN original. Read all 15 navigation-only diffs."
  - "Scripted checks: front matter against EN, link sets, footers and JMdict numbers, headings, and the intake path
    list."; "Quiz safety: classified the 18 RU-introduced exclusions and read their target cards' titles and
    exclusions."
  - "`python tools/validate.py`: 0 errors."; "Manifest: `build_manifest(Path('.'))` run in memory equals
    `manifest.json` (contentVersion `bddfd3e4d9e4aa9d`). Current."
  - Incident: the in-memory manifest check briefly created a Python bytecode cache under `tools`, which the reviewer
    deleted.
  - Limits: no exhaustive title-segment screen ("I only began reading the latter's noisy output"); "Line-by-line
    EN-position parity for the other unlinked mentions in the 15 navigation files was not completed. The diffs
    themselves are link-only."; "Model: not verifiable."; "Dictionary bases rest on my own JMdict knowledge, not a live
    lookup."
- Comprehensibility review scope:
  - "All 30 new cards were read in full against their EN originals", followed by the 30 cards; "Neighbour titles used
    for collisions were read", followed by the neighbours and the fifteen link-only diffs ("Those diffs add links only;
    no new learner prose."); "Link parity on the 30 new cards: checked 30, no LOST/EXTRA. Model: not verifiable."
  - Its limits record "Title-screen overlap was used only as a lead; collisions above were checked against the actual
    titles." It records no validator run and makes no statement about generators.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `b2604ac1-e205-43d8-80a9-eafea952ad11`,
  `64762cac-b502-46d6-9a39-cc98a7944d0d` and `18d54d94-3ffd-476e-be6f-95bbb05d6b88`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model identity
  not independently verifiable.", and the consistency and comprehensibility reports "Model: not verifiable."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "Initial and final git status --porcelain empty";
  the consistency report records "Working tree was clean at start and at end."; the comprehensibility report records
  "`git status --porcelain` empty. No uncommitted changes." No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No validator, generator, build, app test, or native-speaker
  acceptance check run." and "Only this report was written."; the consistency report recomputed the manifest only in
  memory, records the transient Python bytecode cache it created and deleted, and says "no generators were run"; the
  comprehensibility report makes no statement about generators. No reviewer reported changing a tracked repository
  file.
- Full blind reports:
  - `250-words-batch-89-review-correctness-001.md`
  - `250-words-batch-89-review-consistency-001.md`
  - `250-words-batch-89-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch lane worktrees.

  As in earlier batches, the consistency brief made one exception: the intake record, "check only that its path list
  matches the candidate's content diff and that it adds no learner content". The consistency report records that the
  intake "has 45 payload paths. Together with the intake file itself and `manifest.json`, that equals the 47 changed
  paths exactly. `held` is empty, and it has no learner content.", and states "I did not read the BLIND-excluded
  material (other FILES content, translation-batches, translation-drafts, tracking, or scratch worktrees), apart from
  the permitted intake path list." The correctness and comprehensibility reports make no separate statement about these
  sources.

## Initial verdicts and findings

### Correctness

Verdicts: "CORRECTNESS NEEDS FIX (F02); SCOPED COVERAGE NEEDS FIX (F01). Counts: Critical/P0 0; High/P1 0;
Medium/P2 1; Low/P3 1."

- F01 (Low, P3; scoped coverage), `words/怪しい.md:20–21`: "Both kana readings remove source-internal spaces, contrary
  to the explicit verbatim-Japanese requirement. Pronunciation is unchanged, but the frozen reading presentation is not
  retained." Remedy: restore only the kana strings to 「あの はなしは すこし あやしいです。」 and 「かれが くるかどうか
  あやしいです。」. Confidence: high.
- F02 (Medium, P2; correctness), `words/瓶詰.md:4,12,16,38`: "Defining the general packaging action as «розлив»
  restricts it to pouring liquid. 瓶詰 means filling/packing bottles or jars, including non-liquid contents; the EN
  explanation explicitly says "putting something into bottles or jars," without a pouring restriction." Remedy: title
  and H1 «упаковка в бутылки или банки; в бутылках или банках», line 16 «瓶詰 означает упаковку в бутылки или банки, а
  瓶詰する — помещать что-либо» and line 38 «Такая упаковка»; "The jam example can remain: jam can be poured." Evidence:
  Digital Daijisen via Weblio, the Russian Orthographic Dictionary via Gramota and JMdict entry 1491130. Confidence:
  high.

Optional: "None."

What the reviewer confirmed: "All shared front-matter metadata and original exclusions retained; every new exclusion
names an existing RU card. All EN links with existing RU targets retained; no RU-only links or broken links in the 30
cards. All 60 Japanese example sentence bodies retained; the two kana-spacing exceptions are F01."

Limits: "No validator, generator, build, app test, or native-speaker acceptance check run."; kanjiapi returned HTTP
403, and KANJIDIC2 was used instead; "Jisho/Gramota throttled some requests; primary JMdict and other actual dictionary
entries supplied fallback evidence where needed."; "Existing comparison cards were inspected only as needed for this
batch, not certified in full; no exhaustive corpus/quiz audit. Missing RU targets intentionally left unlinked are not
defects. No other actionable defect established in these two facets; this is not a claim of exhaustive correctness."

### Consistency and quiz safety

Verdicts: "CONSISTENCY: PASS. No High or Medium findings."; "QUIZ SAFETY: PASS. No missing required guard was found.
One optional addition and some conservative guards are noted below."

- F1 (Low; quiz), `words/特長.md`: "The RU-added `長短` guard is not needed. 長短 means «длина; достоинства и
  недостатки», and 特長 means a strong point." Remedy: "Optional: drop `長短`. Harmless if kept." Confidence: medium.
- F2 (Low; quiz), `words/特長.md` (`節`, `武器`): "`武器` is justified (title «сильная сторона»). `節` is conservative:
  its title «примечательная черта» is close to 特長." Remedy: "None needed." Confidence: medium.
- F3 (Low; quiz), `words/楽器.md` (`器具`): "Conservative. Both titles contain «инструмент», but 楽器 is the musical
  instrument and 器具 is a tool or apparatus. The guard is harmless and arguably helpful." Remedy: "None." Confidence:
  medium.
- F4 (Optional; quiz), `words/生ずる.md` and `words/呼ぶ.md`: "Both titles contain the segment «вызывать» (生ずる
  «возникать; порождать; вызывать», 呼ぶ «звать; вызывать»). Senses differ: 呼ぶ is "summon", 生ずる is "cause"."
  Remedy: "Optional guard `呼ぶ` on 生ずる." Confidence: low.
- F5 (Optional; consistency), `words/献立.md:32–34`: "The RU body adds a sentence saying the card is marked `kango` "по
  онному первому элементу, как принято в этом репозитории". EN:27 only says it is a mixed on-first reading, not
  ケンリツ. This is a meta-remark with no EN counterpart. It is not wrong, but it is extra." Remedy: "Optional: trim to
  match EN." Confidence: medium.

What the reviewer confirmed: the intake path list (quoted above); "the diffs are link-bracket and href wraps only, with
no prose change. The hrefs use the correct form (`../words/X.md` in kanji files, `X.md` in word files). All targets
exist."; "none of the 30 new cards has a broken or RU-only link. The links dropped relative to EN all had absent RU
targets and stay plain text, per convention", listing 生える → 枯れる, 学科 → 学級, 甘やかす → kanji/甘, 瓶詰 → kanji/瓶
and kanji/詰, 怪しい → kanji/怪 and `ayashii-and-related-words.md`, and 倉庫 → kanji/庫; "Front matter: identical to
EN apart from the exclusions listed below. No dropped EN guard. Footers and JMdict numbers are identical to EN in all
30 cards."; headings in the form `# 字（reading）— title`; and the titles of the 30 new cards unique among the RU word
titles screened. Its duplicates note adds "生じる and 生ずる share the title «возникать; порождать», but this pair
pre-dates the batch."; recorded here as observed, 生ずる is a new card in this batch, its candidate title was
«возникать; порождать; вызывать», and the pair is guarded by 生ずる's EN entry 生じる.

Optional: "現に: the title does not signal the register of the word. EN does not either. Polish only."; "特定: the
title's «выявление» covers the 特定する sense only indirectly. The body teaches it clearly. Polish only."

Limits: the title-screen, other-mention-parity and dictionary limits quoted above.

### Comprehensibility and scoped coverage

Verdicts: "Comprehensibility NEEDS FIX. Scoped coverage CLEAN. No per-article coverage exception: every EN teaching
point checked is still in the Russian body, including 特定's specifying sense (scored under comprehensibility because
the title drops it)."

All seven findings are comprehensibility findings; C1–C4 are medium severity and C5–C7 low; confidence is high except
for C5 (medium).
- C1 (medium), `words/生ずる.md:4` (lines 12 and 16): "The quiz gloss «вызывать» is the same word as `words/呼ぶ.md`
  title «звать; вызывать», and neither card excludes the other." Remedy: title and H1 «возникать; порождать»; line 16
  «生ずる означает порождать что-либо либо возникать, зарождаться.»; "Do not keep «вызывать» and add a quiz exclusion:
  the exclusion would hide the pair, not tell the senses apart."
- C2 (medium), `words/瓶詰.md:4` (lines 12, 16, 20 and 38): "«Розлив по бутылкам и банкам; в бутылках или банках» is
  too long for one phone quiz answer, and «розлив» is industrial pouring of liquid." Remedy: title and H1 «фасовка в
  бутылки и банки; в бутылке или банке», line 16 «瓶詰 означает фасовку в бутылки или банки, а 瓶詰する — помещать
  что-либо», line 20 «Я разложил джем по банкам.» and line 38 «Фасовка может быть частью».
- C3 (medium), `words/独り言.md:4` (line 12; "line 17 contradicts line 41"): "Unqualified «монолог» in ordinary
  Russian is a speech by one person, often to listeners." Remedy: title and H1 «разговор с самим собой; монолог (к
  себе)»; line 17 «Так называют и монолог, если это речь к самому себе, а не к слушателям.»
- C4 (medium), `words/特定.md:4` (lines 12, 17, 20 and 44): the title "keeps only the adjective and narrows the verb to
  «выявление (причины, лица)»". Remedy: title and H1 «конкретный; выявление; обозначение». "The specifying sense is
  still in the body, so this is not a coverage loss."
- C5 (low; confidence medium), `words/物騒.md:4` (line 12): the title "reads as a definition, not a quiz option".
  Remedy: title and H1 «небезопасный; угрожающий».
- C6 (low), `words/危うい.md:22`: "«окажется под угрозой» states a future end state the Japanese does not." Remedy:
  «Если так пойдёт и дальше, будущее компании под угрозой.»
- C7 (low), `words/献立.md:52`: "The Russian sentence reverses it: the translation decides what is being planned, and
  a beginner has no clear target." Remedy: «Какой перевод выбрать, зависит от того, что планируют.»

Optional: the `words/瓶詰.md:31` and `words/献立.md:33` sentences saying the word "is classed as `kango` in the
metadata, as is the practice in this repository" ("house-style polish, not a batch-only teaching failure. Drop those
two sentences."); "`words/学部.md:37` warns that «факультет» is not the teaching staff — a contrast the Russian card
never offers and that only English "faculty" invites. Drop «а не весь преподавательский состав»". It also listed
passages judged not to be findings, among them 生る «плодоносить», 瓦 «черепица», オルガン's stress note, 理科
«естествознание», 特売 «распродажа», 倉庫 «склад», 物語る's rebuilt remark and 生える's dropped "cut teeth" ("Masculine
«я» is the project convention."). Limits: the 卒直 "rare" tag was not re-checked in a full JMdict dump; «Я разлил
джем» is possible for hot jam; title-screen overlap was a lead only; the 倉庫 «склад» ~ 畳む stem overlap is "a
quiz-mechanics note outside these facets"; unlinked pointers to missing RU files "match the repository convention and
are not defects."

## Exclusion classification

All 117 EN exclusion entries (23 lists; EN has none on 生る, 生け花, 甘やかす, 瓦, オルガン, 倉庫 or 定規) are retained in
EN order. 10 of them lie inside the batch, and the other 107 target existing RU cards. At the candidate, 18 direct,
one-sided entries were added on 12 new cards, each appended at the end of its list; none targets a batch word, and no
target card declares the reverse pair. Fix 1 added, removed or reordered none of them.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 生る→実, 収穫 (2) | "(«плод(ы)»)" | required: "the 生る body is about bearing fruit." |
| 瓶詰→缶詰 (1) | "(«банка» = jar/can)" | required: "both mean canning or bottling." |
| 楽器→器具 (1) | "(«инструмент»)" | F3: "Conservative. … The guard is harmless and arguably helpful." |
| 学科→学問 (1) | "(«дисциплина»)" | required: "学問 «научная дисциплина» versus 学科 «учебная дисциплина»." |
| 独り言→会話, 話 (2) | "(conservative: shared «разговор»)" | plausible or conservative: "独り言 begins with «разговор…»." |
| 特色→癖 (1) | "(«особенность»)" | required: "shared word «особенность»." |
| 特長→武器 (1) | "(required: «сильная сторона/черта»)" | required: "shared sense «сильная сторона»"; F2: "justified". |
| 特長→節 (1) | "(conservative)" | F2: "`節` is conservative: its title «примечательная черта» is close to 特長." |
| 特長→長短 (1) | "(conservative)" | F1: "The RU-added `長短` guard is not needed." ("Harmless if kept.") |
| 指定→示す, 定期 (2) | listed without a separate reason | plausible or conservative: "示す is the «указывать» overlap; 定期 shares the 定 kanji." |
| 特定→具体 (1) | listed without a separate reason | required: "the title meanings «конкретный» and «конкретность» overlap." |
| 特売→発売 (1) | "(conservative)" | required: "close sale terms." |
| 危うい→重体 (1) | "(«угроз-»)" | plausible or conservative: "they differ, but the neighbouring sense is close." |
| 物置→押し入れ, 貯蔵 (2) | "押し入れ (conservative, storage space), 貯蔵 («хранени-»)" | plausible or conservative: "storage vocabulary." |

The coordinator and the consistency reviewer differ on two entries: 特売→発売 (coordinator conservative, reviewer
required) and 特長→長短 (coordinator conservative, reviewer F1 "not needed"). The reviewer found no unjustified guard
("none that could mislead") and no missing required guard. The correctness reviewer found that "every new exclusion
names an existing RU card"; the comprehensibility reviewer did not classify them. The coordinator's drafted 王女→王子
was dropped before the candidate (reason quoted above) and was never reviewed. The consistency reviewer's optional F4
(呼ぶ on 生ずる) is not a candidate entry; fix 1 resolved it through comprehensibility C1 without a guard.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`250-words-batch-89-recheck-001.md`.
