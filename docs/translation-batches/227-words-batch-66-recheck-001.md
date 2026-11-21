# Batch 227 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `5cf2313776672567fd1454fffd027b253bb10278` | `b8e291d86716374cd700fba67aaccfa3900d3caf` | Initial review snapshot: the signed candidate, pushed before review. |
| `405231717ab9e83e4f7ee6e7427131a6b2556e4a` | `83de0eed31787b3dcc8910270d96b58735735d67` | Fix 1 (final candidate). It covers correctness C1–C3, consistency F1 and F2, comprehensibility C1–C6 (C2 and C4 partially accepted), the adopted optional items (集金 from correctness, five guard notes from consistency and 時間割 from comprehensibility), a conservative guard added with the 頂点 retitle and the intake refresh. Signed and pushed before the rechecks. |

Fix 1 changed 14 word files and regenerated `manifest.json` (`contentVersion` `c4cede57701bb442`, 4,929 entries; the
candidate had `e6f5556bb7dcb4ba`) and the intake:
- `飛び込む` (line 34; correctness C1, alternative wording): «[入る](入る.md)（はいる）значит «входить» в более широком смысле
  и не требует порыва или прыжка.» instead of «…в более широком смысле, без порыва или прыжка.», matching EN "without
  requiring a rush or leap" (Digital Daijisen 入る sense 1 and 飛び込む senses 1 and 3).
- `突っ込む` (line 43; correctness C2): deleted «Основные значения — «ринуться, врезаться во что-то» и «углубиться во
  что-то»; остальные употребления полезно узнавать при чтении.» The preceding sentence already separates the three
  constructions (JMdict 1456940 senses 1–6; Digital Daijisen 突っ込む).
- `区切る` (line 26; correctness C3, adapted to the deck wording adopted in Batch 226): «В этой коллекции такая смешанная
  форма с онным началом условно отнесена к канго: ク — онное чтение, а озвончённый элемент ぎる связан с исконным
  切る（きる）. Это современное объяснение чтения, а не сложение из одних онных чтений и не утверждение о том, как слово
  сложилось исторически.» instead of «Эту смешанную форму с онным началом относят к канго — словам китайского
  происхождения: …» (Digital Daijisen 漢語; frozen EN 区切る:27).
- `集金` (line 33; correctness optional item): «…не значит получать оплату по счетам или собирать взносы.» instead of
  «…не значит собирать счета или взносы.»
- `境界` (line 9; consistency F1): `quiz_exclusions: [境, 国境, 限界, かぎり, 制限, 限る, 線]`, guarding «разделительная
  линия» against 線 «линия; провод».
- `雑音` (line 9; consistency F2): `quiz_exclusions: [音, 物音, 騒音, 噂, 批判, じゃま]`, guarding «помехи (в сигнале)»
  against じゃま «помеха; вмешательство».
- `預かる`, `頭脳` and `突く` (line 9; consistency optional items): `預かる` `[世話, 面倒, 保存]` («хранение»), `頭脳` `[脳,
  頭, 知能, 知恵, 理解, 中心]` (the figurative «мозговой центр» and 中心 «центр; ядро; главная часть») and `突く` `[刺す,
  押す, 叩く, 打つ, 当たる, 突き当たる]` («тыкать» and «натыкаться»).
- `突く` (lines 4 and 12; comprehensibility C1, the reviewer's wording): title and H1 «тыкать; ткнуть; делать выпад»
  instead of «тыкать; ткнуть; пихать». «пихать» also means stuffing something in (Ozhegov пихать 2; Gramota) and is
  unused in the body; «колоть» and «толкать», the titles of 刺す and 押す, were avoided (JMdict 1456890 senses 1–3).
- `コレクション` (lines 25 and 33; comprehensibility C2, partially accepted): «Это заимствование из английского,
  записанное катаканой; иероглифического сочетания здесь нет. Запоминайте написание コレクション целиком.» instead of «Это
  катаканное слово заимствовано из английского **collection**. Иероглифического сочетания здесь нет. Запоминайте японское
  написание コレクション, а не восстанавливайте его по английским буквам.», and «В Digital Daijisen есть отдельная статья
  コレクション со значением «исправление ошибки». Это другое заимствование, которое совпало с этим словом по написанию, а
  **не** ещё одно значение в цитируемой статье JMdict о коллекции.» instead of «…отдельная статья コレクション от
  английского *correction* — «исправление ошибки». Это отдельное заимствование, а **не** ещё одно значение…». Naming the
  source language follows the published RU gairaigo cards, and the footer keeps the Daijisen headings collection and
  correction as provenance (JMdict 1051540).
- `頼もしい` (line 18; comprehensibility C3, alternative wording): «— Она друг, на которого можно положиться: помогает
  мне, когда я в беде.» instead of «— Она надёжный друг, который помогает мне, когда я в беде.», whose «надёжный» is the
  title word of 確実 «несомненный; надёжный» and 堅い «твёрдый; надёжный» (JMdict 1548380).
- `頼もしい` (line 34; comprehensibility C4, partially accepted, keeping the spelling fact as EN does): «Пишите 頼もしい.
  Написание 頼母しい словарь сохраняет лишь для поиска, а не как обычную запись, поэтому учить его как равноправный
  вариант не нужно.» instead of «Пишите 頼もしい; написание 頼母しい словарь отмечает как встречающееся только при поиске,
  и его не нужно учить как равноправный вариант.»
- `頼もしい` (line 9; consistency optional items): `quiz_exclusions: [確か, 確実, しっかり, 信頼, 堅い]`.
- `頂点` (lines 4, 9 and 12; comprehensibility C5, the reviewer's wording): title and H1 «пик; высшая точка; вершина
  (угла)» instead of «пик; апогей; вершина (угла)» (Gramota апогей; JMdict 1430240). New conservative guard 頂点→最高
  («высшая точка» and 最高 «наивысший; наилучший»): `quiz_exclusions: [頂上, トップ, 上, 盛り, 山, 頭, 先端, 先, 端, 末,
  点, 最高]`.
- `響き` (line 18; comprehensibility C6): «— В этом зале звук хорошо резонирует.» instead of «— В этом зале хорошая
  акустика: звук отлично резонирует.», matching いい and EN "resonates well".
- `時間割` (line 18; comprehensibility optional item): «Я проверил расписание уроков на завтра.» instead of «Я посмотрел
  расписание уроков на завтра.», for 確認しました (EN "I checked").
- The intake note now names the fixed cards, and the 14 candidate hashes were refreshed.

Correctness's optional fuller titles for 時間割 and 響き, consistency's optional 突っ込む–挿す guard, and comprehensibility's
optional title notes (区切る, 突っ込む, 区域, 頭脳 and 順序) and 雑音:19 rewording were not adopted; the dispositions gave the
reasons, which the recheck briefs put to the reviewers (see the reconciliation table).

Titles changed on two cards, so the coordinator re-ran its title screen: no unguarded exact title-segment overlap; the
remaining stem-only hits are generic «делать», the homonymous «выпадать» of 抜ける and 降る, «точка зрения» of 見解 and the
pre-existing «вершин-» of 極める. No link changed, so link parity was unchanged from the candidate: no EN link lost where
the RU target exists, and the same single RU-only link. `tools/validate.py` reported 0 errors.

Net change from the candidate:
- titles and H1s of 突く and 頂点;
- one contrast in 飛び込む and a deleted sentence in 突っ込む;
- note wording in 区切る, コレクション, 頼もしい and 集金;
- example translations in 頼もしい, 響き and 時間割;
- eight added exclusion entries on seven cards (突く→突き当たる, 境界→線, 雑音→じゃま, 頂点→最高, 預かる→保存, 頭脳→中心,
  頼もしい→信頼 and 堅い).

No Japanese example sentence was altered, and no sourced reading, EN exclusion or link changed. The content diff is 14
word files, 20 lines added and 21 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, one reviewer at a time, all on fix 1, in this order: correctness, consistency, comprehensibility;
each brief was sent only after the previous reviewer had replied. No recheck raised a new
finding, so no second fix was needed.

Each reviewer appended to its own report file, which stayed in its session context. Each recheck brief gave the reviewer:
- the fix commit, the reviewed candidate as the base, and the read-only rules;
- the actual content diff `5cf2313..4052317 -- words`;
- the coordinator's evidence for every change and the declined items, stated without the other reviewers' reports;
- the reviewer's original verdicts and the disposition of each of its own findings and optional items. The
  comprehensibility brief asked whether the reviewer maintained its points against the partial acceptance of C2 and C4
  and the declined 雑音:19 item, stating that an unresolved disagreement would be recorded as such.

The three briefs, `b227-recheck-msg-{correctness,consistency,comprehensibility}.txt`, were delivered as session files that
the reviewers were told to read in full.

All recheck messages forbade running `tools/build_manifest.py` or any other generator. Every recheck section states that
none was run. The correctness and consistency reviewers each ran `tools/validate.py` (0 errors each); the
comprehensibility reviewer did not run it. Each recheck section records HEAD `4052317` with a clean tree (the
correctness reviewer before and after its checks).

### Round 1 (`4052317`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer compared the actual word diff against `5cf2313`, checked every changed passage in all 14 cards, including titles and exclusions, and reread the complete revised 突く, 頂点 and コレクション with the corresponding EN. C1–C3 are **resolved**: 飛び込む says 入る does not require the manner rather than excluding it; 突っ込む's unsupported hierarchy is deleted while the constructions and evidence remain; 区切る's grouping is conditional and collection-local, with the Chinese-origin definition removed and the historical disclaimer kept. The 集金 optional item is **resolved**; the 時間割 and 響き title items remain **optional**, declined without a blocking omission. No regression: 突く's «делать выпад» fits the physical thrust kept in the body (fresh evidence: Russian Wiktionary выпад sense 2, «колющий удар»; Weblio 突く sense 1); 頂点's «высшая точка» keeps the summit and apex reading; コレクション still distinguishes the two borrowings; 頼もしい keeps dependability and help, and its spelling note explains the search-only status accurately; 響き and 時間割 keep their senses. All 14 cards keep their Japanese example and reading prefixes, other metadata and every previous exclusion; the added targets exist. Validator 0 errors. Correctness and scoped coverage are **CLEAN**. |
| Consistency | Snapshot `4052317` with a clean tree; the commit changes the 14 word cards, `manifest.json` and the intake. F1 and F2 are **resolved**, and the adopted guard notes are **resolved**; the reviewer agreed with declining 突っ込む–挿す (its item withdrawn). The eight new entries are well-formed one-way entries, every target exists and none is duplicated in reverse; the RU-added total of 9 is accurate. H1 equals the title on 突く and 頂点, and across the full RU word pool each new title segment occurs only on its own card, so there is no exact overlap; 突く→突き当たる covers the «натыкаться» stem. No link target changed; navigation stays 5 files and 12 links, and the only RU-only link is still 突っ込む→引き出す. The manifest hashes match the working tree for the 14 changed cards, and the intake's 35 payload hashes match the files. Validator 0 errors. Consistency, quiz safety and scoped coverage are **CLEAN**. |
| Comprehensibility | Snapshot `4052317` with a clean tree. C1, C3, C5 and C6 are **resolved**: «пихать» and «апогей» are gone, the new titles match the senses taught in the bodies, «Она друг, на которого можно положиться…» avoids «надёжный» (slightly marked, not a defect), and «хорошо резонирует» matches いい. C2 is **resolved**; the reviewer did not maintain the partial-acceptance remainder: «заимствование из английского» names the source language without requiring the English gloss, and the footer headings are provenance outside the original finding. C4 is **partially resolved** and no longer actionable: the note still says «для поиска», but it now explains that 頼母しい is not an ordinary spelling to learn; the remaining wording is optional polish, and EN keeps the same warning. The 時間割 optional item is **resolved** by adoption; 雑音:19 is not maintained, and the declined title-mark notes remain **optional**, not elevated. No regression: 区切る's collection-local wording matches the published 騒々しい deck wording, 突っ込む keeps the three-construction contrast, and 飛び込む and 集金 are clearer without misleading narrowing. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 飛び込む excludes a rush or leap from 入る (minor, also coverage) | **Resolved** (alternative wording) | `飛び込む.md:34`; frozen EN "without requiring a rush or leap"; Digital Daijisen 入る sense 1 and 飛び込む senses 1 and 3. |
| Correctness C2: 突っ込む ranks senses without support (minor) | **Resolved** | `突っ込む.md:43` deleted; JMdict 1456940 senses 1–6; Digital Daijisen 突っ込む. |
| Correctness C3: 区切る defines канго by Chinese origin (minor, also coverage) | **Resolved** (adapted wording) | `区切る.md:26`; Digital Daijisen 漢語; frozen EN 区切る:27; the Batch 226 deck wording on 騒々しい. |
| Correctness optional: 集金 «собирать счета или взносы» | **Optional, adopted**; resolved at recheck | `集金.md:33`. |
| Correctness optional: fuller titles for 時間割 and 響き | **Optional, not adopted**; kept optional at recheck | The bodies keep the broader timetable and impression senses; 響き already excludes 印象, 感じ and 感想. |
| Consistency F1: 境界 «разделительная линия» and 線 «линия; провод» (minor, conservative) | **Resolved** | `境界.md:9`; `words/線.md` exists. |
| Consistency F2: 雑音 «помехи (в сигнале)» and じゃま «помеха; вмешательство» (minor, conservative) | **Resolved** | `雑音.md:9`; `words/じゃま.md` exists. |
| Consistency optional: 預かる–保存, 頼もしい–信頼 and 堅い, 頭脳–中心, 突く–突き当たる | **Optional, adopted**; resolved at recheck | `預かる.md:9`, `頼もしい.md:9`, `頭脳.md:9`, `突く.md:9`. |
| Consistency optional: 突っ込む–挿す | **Optional, not adopted**; withdrawn by the reviewer at recheck | «засовывать» and «вставлять» share no title segment or stem; the overlap mirrors EN "thrust into" and "insert", which EN did not guard. |
| Comprehensibility C1: 突く «пихать» (moderate) | **Resolved** | `突く.md:4,12`; Ozhegov and Gramota пихать; JMdict 1456890; guard 突く→突き当たる. |
| Comprehensibility C2: English words in コレクション's learner text (minor) | **Resolved** (partially accepted; the remainder not maintained at recheck) | `コレクション.md:25,33`; JMdict 1051540; the source language is still named, as on the published RU gairaigo cards, and the footer keeps the Daijisen headings as provenance. |
| Comprehensibility C3: 頼もしい «надёжный друг» (moderate) | **Resolved** (alternative wording) | `頼もしい.md:18`; JMdict 1548380; guards 頼もしい→信頼 and 堅い. |
| Comprehensibility C4: 頼もしい search-only jargon (minor) | **Partially resolved**; not maintained as actionable | `頼もしい.md:34`; the reviewer treats the remaining «для поиска» wording as optional polish; EN keeps the same warning. |
| Comprehensibility C5: 頂点 «апогей» (minor) | **Resolved** | `頂点.md:4,12`; Gramota апогей; JMdict 1430240; guard 頂点→最高. |
| Comprehensibility C6: 響き «отлично резонирует» (minor) | **Resolved** | `響き.md:18`; frozen EN "Sound resonates well". |
| Comprehensibility optional: 時間割 «Я посмотрел» | **Optional, adopted**; resolved at recheck | `時間割.md:18`; 確認しました, EN "I checked". |
| Comprehensibility optional: 雑音:19 rewording | **Optional, not adopted**; not maintained at recheck | The line pairs «пересуды» with «критику», as EN pairs "chatter" with "criticism"; 批判 is already excluded, and the figurative sense is framed in the opening and nuance section. |
| Comprehensibility optional: 区切る «размечать», 突っ込む «(перен.)», 区域 «территория», 頭脳 «мозговой центр», 順序 | **Optional, not adopted**; kept optional at recheck | The bodies qualify these glosses. |
| Consistency limit: raw-byte hash mismatch on 118 `strokes/*.json` manifest entries | **Withdrawn** as a defect; pre-existing and outside the batch | `tools/build_manifest.py` hashes text files after CRLF→LF normalization; the 118 files are CRLF byte copies of EN blobs kept by `.gitattributes` (`strokes/*.json -text`), as established in Batch 226. The batch touches no `strokes/` file. The reviewer did not recheck them at recheck. |
| Exclusion classification: 順序→決まり | **Classifications differ; the entry is kept either way** | The author added it as conservative; the consistency reviewer classed it as required (shared «порядок»; 決まり already excludes 順 and 順番). This record counts it as required. The fix entries are conservative, as the dispositions have them; the reviewer confirmed them and the total of 9 at recheck. |

Cross-batch note: links to absent targets stay plain. Ten EN link targets in this batch's new cards (12 occurrences) are
absent from RU: the kanji cards 境 (from 境界), 脳 (from 頭脳), 領 (from 領収 and 領事), 預 (from 預かる) and 順 (from 順序
and 順々), and the word cards 点く (from 突く), 突き当たり (from 突き当たる), 膨らます and 膨らむ (from 風船) and 乾燥 (from
感想). EN has kanji cards for 境, 脳, 順, 預 and 領; the other 8 written kanji without an RU kanji card have none in EN
either. No links were held from Batch 226.

## Final exclusion set

All 169 EN exclusion entries (27 lists) are retained in EN order. Nine direct, one-sided entries are added on eight new
cards (no new list):

- Required (1): 順序→決まり.
- Conservative (8): 境界→線, 雑音→じゃま, 突く→突き当たる, 頼もしい→信頼 and 堅い, 預かる→保存, 頭脳→中心 and 頂点→最高,
  all added in fix 1.

Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the fix (飛び込む, 突っ込む, 区切る); the 集金 optional item adopted, and the 時間割 and 響き
  titles remain optional.
- Scoped coverage: **CLEAN** after the fix (飛び込む, 区切る).
- Comprehensibility: **CLEAN** after the fix (突く, コレクション, 頼もしい, 頂点, 響き); C4's remaining «для поиска» wording and
  the declined title notes remain optional.
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN**, including the eight fix-1 entries. This covers the reviewed batch and the directly adjudicated
  pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them, except that the correctness reviewer
  reread the complete revised 突く, 頂点 and コレクション. The unchanged cards rest on review 001, in which the correctness
  and comprehensibility reviewers read all 30 cards in full against EN and the consistency reviewer read all 30 cards in
  full and compared them with EN by script.
- The comprehensibility reviewer did not re-fetch dictionaries, run the validator or re-audit quiz exclusions at recheck.
  The consistency reviewer's recheck manifest comparison covered the 14 changed cards and the 35 intake hashes; it did not
  recheck the 118 `strokes/` hashes, and its full-pool title screen was its own exact-segment match on titles split at
  «;», not the repository script.
- The consistency reviewer did not independently recheck dictionary entries or JMdict ids, and its `check_content_budget`
  run at the candidate timed out; the coordinator's candidate script ran the budget check (OK). Its necessity classes are
  judgements, not measurements.
- Some of the comprehensibility reviewer's Russian citations (пихать, апогей) came from search extracts, and it did not
  reopen Daijisen's separate correction headword; C2 did not depend on it. Its initial report cites 頼もしい:16 and :33 and
  響き:16 for passages at lines 18, 34 and 18.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
