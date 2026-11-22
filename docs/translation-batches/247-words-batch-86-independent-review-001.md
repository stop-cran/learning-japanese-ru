# Batch 247 — independent review 001

## Snapshot and scope

- Reviewed commit: `83b26408e9899c14813ea3226de3a04c72164abf` (tree `96d36fd6130dc64d3cb202f00e98df2330547687`), branch
  `full-ru-247-words-86`, parent `ac67a60`. The candidate was signed and pushed before review.
  - The content was authored in the scratch lane `learning-japanese-ru-b247`, whose local-only scratch commit `bca83ec`
    ("B247 lane drafts on B242-B246 scratch") sits on `4ef6fa4` ("B242 fixes 1-3 synced onto B246 lane scratch"), itself
    on the earlier lane scratch commits `b37a987` and `282ea33`. The coordinator's candidate script checked that the lane
    was clean at `bca83ec` with parent `4ef6fa4`, that the branch, HEAD~1 and `origin/main` were the expected published
    baseline, that the primary tree, including ignored files, was clean, that the three navigation files edited in the
    lane were unchanged between `4ef6fa4` and the published HEAD, and that none of the 30 new word files already
    existed.
  - The script copied 33 lane files (the 30 new cards and the navigation files `kanji/着.md`, `words/被せる.md` and
    `words/頭.md`), then applied two exact-once follow-up edits carried from Batch 245's fix 1 (`1dc38a8`, which
    retitled the published card 空っぽ from «совсем пустой; полый» to «пустой; полый»; recorded in
    `b245-downstream-followups.md` and applied by `b247_post.py`), because two B247 drafts quoted the old gloss:
    - `words/真っ白.md`: «（からっぽ）, «совсем пустой», » → «（からっぽ）, «пустой», »;
    - `words/真空.md`: «значит «совсем пустой, полый».» → «значит «пустой, полый».».

    It then regenerated the manifest, checked that the changed path set was exactly the 33 batch paths plus
    `manifest.json`, byte-compared the other 31 copies with the lane, and verified that the two edited files equal the
    lane copy plus that edit (a single changed line each). These two candidate files therefore intentionally differ from
    the lane blobs. Fix 1 did not touch either edited line (line 29 in both files; fix 1 changed 真空 lines 18 and 33
    only, and did not change 真っ白). No link was held from an earlier batch. The script's byte scan of the content paths
    prints any BOM, CR or missing final newline rather than stopping; for this record the 33 committed blobs at `83b2640`
    (and again at the final fix `9c5a6a4`) were checked: none has a BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - After authoring and before the candidate commit, the coordinator edited six lane cards: merged paragraph splits in
    着々, 真空, 真っ暗, 直線, 直後 and 直前, and one sentence in 直後; the other 24 new cards and the three navigation
    files were copied unchanged (apart from the two follow-up edits above). Its adjudication record (lane
    `learning-japanese-ru-b247`, base `4ef6fa4`, uncommitted) states:
    - "Scope: all 30 new cards read in full (Russian prose, examples, title/H1, links) against frozen EN 6af98cb;
      non-title metadata compared mechanically with EN (b247_cmp.py: all match except four cards carrying the five
      RU-added exclusions below). Link audit (rutools link_parity, 33 files): no lost or extra links; nine EN targets not
      yet published stay plain (kanji 庁 県 線 角; words 一斉 住まい 円周 曲線 水平). RU-only links: none. Nav edits: 3
      files / 5 links (kanji/着 38, 52; words/被せる 46; words/頭 33, 48); navonly 0 problems.";
    - the edits, each with its recorded reason:
      - 着々, 真空, 真っ暗, 直線, 直後 and 直前: "merged 7 RU-only blank-line paragraph splits (2+1+1+1+1+1) back into
        the EN paragraphs" ("the drafts split single EN paragraphs; the published corpus keeps EN paragraph structure;
        paragraph parity now matches EN for all 30");
      - 直後: «Это отдельно подтверждённое признание: …» → «Это значение подтверждено отдельным источником: …» ("calque of
        EN "separately sourced recognition"; «признание» does not read as dictionary recognition of a sense");
    - accepted as drafted: "Faithful as drafted: 着せる 倣う 真似る 真っ黒 真っ白 真っ青 しょうがない 正面 先頭 はじめに 真っ先
      官庁 県庁 看病 相撲 相互 直通 垂直 直角 以降 以後 たちまち 直径 目覚まし (plus the edited cards' unchanged prose).";
    - "RU-added exclusions (all conservative, direct pairs on new cards only): 直前→直に and 直前→直接 (shared
      «непосредствен-» from the RU wording; B219 precedent), たちまち→瞬間 («мгновение»; EN already guards 一瞬), 官庁→機関
      (shared «учреждение»), 直線→直通 (Russian «прямая линия» also names a direct phone line).";
    - "RU-side adaptations accepted: 真似る adds the Russian-government note (подражать + dative vs Japanese を); 倣う
      adapts the English "imitate + を" remark to «перенимать что-либо»; 真空 replaces English "empty" with русское
      «пустой»; はじめに rewords the English "introduction" ambiguity (no person-to-person introduction).";
    - "真っ暗 example 2 «всё впереди показалось беспросветным» follows EN "everything seemed hopeless".";
    - "Unverified Russian (not defects): подражать governance and «прямая линия» as a phone-line name were not
      re-fetched; both are standard usage.";
    - "Validation after edits (lane): manifest 5,529 files; validate 0 errors; 124 tests OK; budget OK (localZipBytes
      8,006,764); link parity clean (33 files); navonly 3 files / 5 links / 0 problems; diff --check clean; no
      BOM/CR/missing EOL; paragraph parity with EN for all 30."

    Fix 1 later changed several of these passages again (see the recheck record): the reworded 直後 sentence on line 32
    now reads «Это значение взято из Daijisen: в записи JMdict, указанной ниже, есть только значение «сразу после».»
    (comprehensibility F4); the 倣う adaptation on line 21 now reads «По-русски говорят «брать что-либо за образец» с
    винительным падежом, но при 倣う образец отмечается に, а не を.» (F10); the closing sentence of 真空's «пустой» note
    on line 33 now reads «Но это не значит, что любое русское «пустой» можно перевести как 真空.» (F1); and the
    はじめに sentence «Ни тот, ни другой не означает представления одного человека другому.» on line 21 is deleted (F11).
    Fix 1 also changed 看病, たちまち, 直前, 目覚まし, 先頭, しょうがない, 垂直 and 直通, which the coordinator had accepted
    as drafted, and 真空:18. The merged paragraphs stand.

    The committed manifest records 5,529 entries (5,524 `files`, 3 images and 2 scenes; `contentVersion`
    `6cfe11c9d4ba290e`); the coordinator's lane `validate.py` run and its phase-1 `tools/validate.py` run on the
    candidate content reported 0 errors. The correctness and consistency reviewers also ran the validator on the
    candidate (0 errors each).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards (two of them carrying the follow-up edits above);
    - 3 files with 5 restored navigation links (the kanji card 着 and the word cards 被せる and 頭);
    - `manifest.json` (`contentVersion` `6cfe11c9d4ba290e`, 5,529 entries);
    - the intake, whose note reads "B247 30-card adaptation with five navigation-only link restorations in three
      existing files, carrying two B245-fix follow-up edits; candidate before blind review."

    Against the published baseline the candidate changes 36 files (1,395 insertions, 9 deletions), including the
    parent's publication record; the candidate commit itself changes 35 files (1,315 insertions, 9 deletions).
- Published baseline recorded in the intake: `3af630833603ef75954524faad0bf021486f58be` (Batch 246 merge, PR #130).
  Parent `ac67a60` ("Record B246 publication verification") adds only the Batch 246 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 3 files (5 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b247-cand-screen.txt`, 357 lines): 40 `OK` lines for pairs already guarded by an exclusion and 317
    `!!` lines. It has no exact-segment line; all lines are stem-only. It differs from the lane screen
    (`b247-screen.txt`, 357 lines) in one stem-only line: the 倣う~純粋 line (stem «приме») appears in both with
    different 純粋 titles (the published title after the Batch 244 fix `149b7d7` is «чистый (без примесей);
    неподдельный», against the lane's pre-publication «чистый; неподдельный; без примесей»). No exact-segment line
    differs;
  - link parity: "checked 33", no LOST and no EXTRA link. For this record link parity was verified again at `9c5a6a4`
    with the same result; fix 1 changed no link target.
- Common sample: all three reviewers read all 30 new word cards in full against frozen EN, with the coverage of the EN
  side stated per reviewer below. The consistency reviewer also read all three navigation diffs in full and checked the
  intake record (path list and payload hashes) and the manifest entries; the correctness reviewer read the existing RU
  card 被せる in full; the comprehensibility reviewer "glanced at" the link-only edits in the three navigation files.
- Correctness review scope:
  - "Model identity not verifiable."; "Each following words/<name>.md was read IN FULL in both RU and EN", followed by
    the 30 cards; "Existing RU 被せる and 始め read in full; 24 comparison-card titles checked."
  - "All 63 main Japanese examples and kana text match EN apart from layout/parenthesis wrappers."; "All 140 actual
    local Markdown links resolve."
  - It inspected the actual Jisho/JMdict entries for all 30 words, "Actual Daijisen articles checked for all 16 cited
    Weblio words; Kotobank checked for 以降/以後 and Bunpro for てしょうがない"; it matched every N2 label by JMdict ID
    against the pinned n2.csv (`b062d4e…`); it checked component readings via kanjiapi.dev; it checked the Russian
    terminology against ru.wiktionary (подражать, сосуд, прямая_линия sense 3, исконный) and ru.wikipedia (Кандзи), and
    «отгул» against Kuznetsov via gufo.me.
  - "Read-only validator: `python -X utf8 -B tools/validate.py` → 0 error(s). Runtime diff whitespace check passed."
- Consistency review scope:
  - "Read in full: all 30 new RU cards and the 3 navigation diffs (kanji/着.md, words/被せる.md, words/頭.md)."
  - "Compared against frozen EN: front matter, H2 structure, link sets, quiz_exclusions, footer URLs and JMdict entry
    numbers (programmatic, all 30). EN bodies read line by line for only 14 cards (倣う, 真空, 官庁, たちまち, 垂直, 真っ青,
    はじめに, 真似る, 真っ先, 相互, 先頭, 直前, 目覚まし, 着せる). The other 16 were checked structurally only."
  - "Manifest: after CRLF normalisation (as build_manifest does) all 5524 hashes match. The diff touches only the 33
    changed files plus contentVersion. I did not recompute contentVersion and did not run the generator."
  - "`python tools/validate.py`: 0 error(s). (It created an untracked `tools/__pycache__`; I deleted it, tree clean
    again.)"
  - "The title-screen tool output was only partly read (slow); I supplemented it with grep over RU titles."; "Not
    verified: Russian linguistic correctness beyond consistency; tag-vocabulary and byte-format (CRLF/BOM) scan was
    started but not completed. Validator passing covers schema and tags."
- Comprehensibility review scope:
  - "comprehensibility and scoped coverage of the 30 new word cards, each read in full and compared with the frozen EN
    original (EN teaching sections read in full; dictionary footers not re-audited)"; "Link-only edits in kanji/着.md,
    words/被せる.md and words/頭.md were glanced at, not scored as new articles. Model: not verifiable."
  - Its limits record "JMdict and Daijisen pages were not re-opened; sense citations are the cards' own. Title-screen
    stem hits were a lead only. Intake JSON, manifest and batch records were not reviewed. No generator was run." It
    records no validator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `be433256-1742-4246-aee4-5076708fb527`,
  `9d58e4e5-e42f-4d92-87bc-07ea8439d31b` and `37b3d1cf-58d2-428f-a100-7e473e5c8207`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model identity
  not verifiable.", the comprehensibility report "Model: not verifiable." and the consistency report makes no statement
  about its model.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "HEAD matches; status --porcelain empty."; the
  consistency report records "HEAD matches; working tree clean." and the self-deleted `tools/__pycache__` above; the
  comprehensibility report records "git status --porcelain empty; HEAD matches that commit. No uncommitted changes." No
  fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No generators, repository edits, staging or commits; only this
  report was written."; the consistency report says "I did not recompute contentVersion and did not run the
  generator."; the comprehensibility report says "No generator was run." No reviewer reported changing a tracked
  repository file.
- Full blind reports:
  - `247-words-batch-86-review-correctness-001.md`
  - `247-words-batch-86-review-consistency-001.md`
  - `247-words-batch-86-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch lane worktrees.

  As in earlier batches, the consistency brief made one exception: the intake record, "check only that its path list
  matches the candidate's content diff and that it adds no learner content". The consistency report records "Intake
  JSON (only permitted exception): its 33 payload paths equal the content diff exactly, all candidateRawSha256 values
  match the working-tree bytes, held is empty, and it carries no learner content." and "Did not read: scratch
  worktrees, author or reviewer reports, translation-batches/drafts/tracking other than the intake JSON." The correctness
  report states "No author/reviewer reports, forbidden scratch worktrees, or excluded batch/draft/tracking files were
  deliberately opened"; the comprehensibility report states only that the intake, manifest and batch records "were not
  reviewed".

## Initial verdicts and findings

### Correctness

Verdicts: "CORRECTNESS — NEEDS FIX (看病, C1); SCOPED COVERAGE — NEEDS FIX (たちまち, S1). No actionable defect
established for the other articles in either facet. These are low-impact, local findings, not a batch-wide rejection."

- C1 (low; correctness), `words/看病.md:19`: "«Я взял отгул» introduces a specific kind of leave into generic
  仕事を休みました / EN “I took time off work.” Kuznetsov defines this leave as day(s) granted for overtime; no such
  employment circumstance is stated here." Remedy: «Я не пошёл на работу, чтобы ухаживать за больным отцом.» Evidence:
  Digital Daijisen 休む sense 4 (欠席・欠勤する) via Weblio; Kuznetsov «отгул» sense 2 via gufo.me. Confidence: "high for
  the dictionary distinction; medium for learning impact, since colloquial «отгул» can be used loosely."
- S1 (low; scoped coverage), `words/たちまち.md:4,12`: "Both «в мгновение ока» and «моментально» express speed;
  neither independently retains EN title's “suddenly,” also explicitly taught at RU:16,29,33." Remedy: "Restore «в
  мгновение ока; внезапно» in title and H1." Evidence: JMdict 1288480, separate senses 1 (in an instant) and 2
  (suddenly); frozen EN `words/たちまち.md:4,16–17`. Confidence: high.

What the reviewer confirmed: "Full reads found no substantive Japanese text loss. No new card link lacks an EN
counterpart; no EN link to an existing RU card is dropped."; "Dropped EN targets confirmed absent: kanji 庁/県/角/線 and
words 住まい/水平/曲線/一斉/円周."; "Stable metadata matches EN except declared added exclusion-list entries: 官庁→機関;
直線→直通; たちまち→瞬間; 直前→直に/直接."; "No introduced reading/classification defect established."; "Boundary
inclusion in 以降/以後 is appropriately qualified; 直後's spatial sense is explicitly separately sourced. 直前's 出る
explanation and through-service/stopping distinction in 直通 are supported. Shared written 被せる does not merge the two
primary readings."; the Russian-only dative note on подражать, the container sense of «сосуд» and the
communication-line sense of «прямая линия» were checked against ru.wiktionary; "English-dependent contrasts retain their
Japanese teaching limits."

Optional: "Outside these facets, learner prose could replace references to an unseen “исходный список” in
words/直前.md:34 and words/目覚まし.md:16 with direct usage statements. Both references are inherited from EN, not lost
Japanese teaching rules." Limits: "This is a full bilingual scoped review, not native-speaker certification or an
exhaustive quiz/title-collision audit. Comparison cards other than 被せる and 始め were not all read in full. Gramota
searches returned 429; actual Russian alternatives above were used. Initial 真っ白 API 429 and kanjiapi 403 were resolved
using the full Jisho page and a browser User-Agent respectively; neither remains a verification blocker."

### Consistency and quiz safety

Verdicts: "Consistency: CLEAN"; "Quiz safety: CLEAN (no missing required guard; one over-guard, see Optional)";
"Integration / manifest: CLEAN". Findings: "None blocking or required."

What the reviewer confirmed: "Front matter (word, reading, jlpt, type, kanji, tags) identical to EN for all 30 cards.
Section order matches the RU convention."; "Links: all links match EN except targets with no RU file (words/住まい, 水平,
曲線, 一斉, 円周; kanji/庁, 県, 角, 線, 倣), which are rendered as natural plain text in 相撲, 垂直, 直線, たちまち, 直径. No
RU-only links." (EN 倣う has no link to kanji 倣, so that one entry in the reviewer's list does not correspond to an EN
link; the coordinator's link audit and the records' link parity list nine plain targets without it.); "Navigation:
着せる linked in kanji/着.md (L38, L52) and words/被せる.md L46; 先頭 linked in words/頭.md (L33, L48). Only
brackets/hrefs changed, path forms identical to EN. The plain mention at kanji/着.md:62 is a pre-existing RU-only
sentence; fine."; "quiz_exclusions: all EN entries kept, in order, plus exactly 5 RU additions. All targets exist; no
self-reference or duplicates. Exclusions are one-sided by contract, so no reverse declaration is needed."; "Unguarded
stem-only neighbours (看病 vs 育児/美容 «уход за…», 相撲 vs 戦い, 相互 vs 交流/仲, 直線 vs 境界/方針/系統, はじめに vs 開始,
直角 vs 隅/街角): none are defensible correct answers; no guard needed."; "Titles unique; footers/URLs match EN."

Optional:
1. "たちまち title drops EN's "suddenly" sense (JMdict sense 2); 突然/急に/急激 guards already cover it."
2. "真空:18 renders 容器 as «сосуд» while the 容器 card title is «контейнер; тара»."
3. "相互 title «взаимный; обоюдный» is adjectival though the word is a noun taking の; body clarifies."
4. "直前 («Исходный список закрепляет…») and 目覚まし («запись из исходного списка») contain author-process wording; EN
   has the same."
5. "直線→直通 could be dropped (see above); keeping it is harmless."

Limits: "Blind review; 16 of 30 EN bodies compared structurally only; title-screen output partly read; contentVersion
not recomputed; no linguistic verdict on Russian quality."

### Comprehensibility and scoped coverage

Verdicts: "Comprehensibility — NEEDS FIX (exceptions: the ten findings below; the other 20 cards in scope have no
established comprehensibility defect). Scoped coverage — CLEAN (no EN Japanese teaching point dropped; unclear wording
is scored under comprehensibility)." The report says "ten findings" but lists twelve (F1–F12) on ten cards.

All twelve findings are comprehensibility findings with high confidence; F1–F4, F6–F8 and F10 are medium severity, and
F5, F9, F11 and F12 low.
- F1 (medium), `words/真空.md:33`: «эти расширения не превращают любое русское «пустой» в 真空» "is an ungrammatical
  calque of EN "those extensions do not turn every use of English empty into 真空"". Remedy: a two-sentence rewrite of
  the Daijisen remark.
- F2 (medium), `words/直前.md:34`: «Исходный список закрепляет временное значение; пространственное — дополнительное
  учебное» "names a source list the learner cannot see". Remedy: delete it and state the main and spatial senses
  directly.
- F3 (medium), `words/直前.md:4`: the title «непосредственно перед (по времени); прямо перед (в пространстве)» "is a
  definition, not a quiz answer (H1 line 10 repeats it)". Remedy: title and H1 «непосредственно перед; прямо перед».
- F4 (medium), `words/直後.md:32`: «в основной закреплённой словарной записи есть только значение «сразу после»» "is
  editor metadata"; "after teaching «прямо позади», the sentence makes that sense look unofficial". Remedy: «Это
  отдельное пространственное употребление; обычное значение — «сразу после».»
- F5 (low), `words/目覚まし.md:16`: «запись из исходного списка» "points at an invisible list". Remedy: «Записи 目覚し и
  目ざまし — то же слово めざまし.»
- F6 (medium), `words/真っ白.md:4`: the title «белоснежный; незаполненный» "does not show the blank-mind sense the card
  teaches". Remedy: title and H1 «белоснежный; ни записи, ни мысли».
- F7 (medium), `words/先頭.md:4`: the title «начало ряда (очереди); передняя позиция; место во главе» "is too long for a
  quiz option. «Передняя» repeats 正面's «передняя сторона», and 正面 does not exclude 先頭, so both can look right.
  «Очереди» also echoes 真っ先's «в первую очередь», a different sense." Remedy: title and H1 «начало ряда; во главе».
- F8 (medium), `words/しょうがない.md:20` (the example is on line 21): «Ну и безнадёжный же ты человек» "adds «ты».
  しょうがない人だね does not name the addressee". Remedy: «Ну и безнадёжный же человек.»
- F9 (low), `words/しょうがない.md:4`: «до невозможности» "is not a usable quiz answer without a host word". Remedy:
  title and H1 «ничего не поделаешь; безнадёжный; невыносимо».
- F10 (medium), `words/倣う.md:21`: «Русское «перенимать что-либо» с прямым дополнением не означает, что здесь нужно
  механически ставить を» "rejects a gloss the card never gives". Remedy: delete the sentence.
- F11 (low), `words/はじめに.md:21`: «Ни тот, ни другой не означает представления одного человека другому» "warns
  against a mix-up that Russian «для начала» and «вступление (в книге)» do not invite". Remedy: delete the sentence.
- F12 (low), `words/垂直.md:33`: «Не переводите каждое 垂直 как «стоящий прямо на странице»» "rejects a gloss the card
  never shows". Remedy: «Не каждое 垂直 значит «вертикальный». Две наклонные линии могут быть перпендикулярны друг другу.»

Optional (nonblocking): link 徐々に in たちまち; 看病:18 «взял отгул» "is narrower than 仕事を休みました / EN "took time
off" — outside this facet, correctness"; 真空:16 «сосуда» («ёмкости» would avoid the blood-vessel reading); 相互:18 «на
взаимной основе» "is stiff"; 直通:18 «номер прямой связи» "is clearer as «прямой номер»"; the 着せる title "repeats one
sense"; outside its facet, the quiz-exclusion notes that 以降 does not exclude 以後, 直通 does not exclude 直線, and 相撲
and 直径 have none; a lead-in for 正面:33 on まとも. The report's line numbers for these optionals are one or two lines
earlier than the candidate lines (看病:19, 真空:18, 直通:19). Limits: the dictionary and record limits quoted above.

## Exclusion classification

All 156 EN exclusion entries (28 lists; EN has none on 相撲 or 直径) are retained in EN order. 12 of them lie inside the
batch, and the other 144 target existing RU cards. At the candidate, five direct, one-sided entries were added on four
new cards, each appended at the end of its list; only 直線→直通 targets a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 官庁→機関 (1) | "(shared «учреждение»)" | "warranted. Both titles share «учреждение»; JMdict 機関 sense 1 is institution/agency." |
| たちまち→瞬間 (1) | "(«мгновение»; EN already guards 一瞬)" | "warranted, conservative. Both carry «мгновение»." |
| 直前→直に, 直前→直接 (2) | "(shared «непосредствен-» from the RU wording; B219 precedent)" | "conservative. Shared «непосредственно» makes a defensible overlap." |
| 直線→直通 (1) | "(Russian «прямая линия» also names a direct phone line)" | "weakest; only shared word is «прямая», nouns differ (линия vs связь). Harmless over-guarding." |

The coordinator recorded all five as "all conservative, direct pairs on new cards only". The correctness reviewer
listed the same five as "declared added exclusion-list entries" without a classification, and the comprehensibility
reviewer's outside-facet notes asked for 以降–以後 and 直通–直線 guards and noted that 相撲 and 直径 have none.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`247-words-batch-86-recheck-001.md`.
