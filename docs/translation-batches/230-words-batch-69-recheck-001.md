# Batch 230 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `5ec190a7c89f162bdb1673eca213fab94aab9624` | `6d3c31bd01596be9b29662885a4d2cae61c73bac` | Initial review snapshot: the signed candidate, pushed before review. |
| `93e2dea8fb11f1bc7e6ea5ed03273f3c61bfc2a7` | `2f77d725d22204f5842d8f7e15126e32662c870d` | Fix 1 (final candidate). It covers correctness C1, consistency F1, comprehensibility C1–C9 (C2, C4, C5, C6 and C8 with adapted wording) and the adopted optional items (録音:31, the three 長方形 links and the 鈴 link in 鐘). Signed and pushed before the rechecks. |

Fix 1 changed thirteen word files and regenerated `manifest.json` (`contentVersion` `01ce08b9df2397d3`, 5,019 entries; the
candidate had `cf8e1ff9dcb79ff6`). The intake was not refreshed; it still records the candidate's 31 payload hashes.
- `鈴` (lines 4, 12, 20, 22–23 and 39; correctness C1 and comprehensibility C4, merged, adapted wording):
  - title and H1 «колокольчик (часто округлый); бубенчик» instead of «бубенчик» (EN "bell (often globular)"). The
    correctness reviewer's «храмовый колокол» was not used, because the RU 鐘 card owns «колокол» and the temple bell, so
    it would blur the 鈴/鐘 contrast the cards teach; the comprehensibility reviewer's «колокольчик; бубенчик (типичный
    небольшой)» was replaced by EN's "(often globular)" qualifier, matching the body's own «часто округлый»;
  - line 20: «Когда я потряс колокольчик, раздался приятный звон.» instead of «Когда я потряс бубенчик, …»;
  - lines 22–23: «колокольчик звенит» and «звенеть колокольчиком» instead of «бубенчик звенит» and «звенеть бубенчиком»;
  - line 39: «鈴 называет и колокольчики в синтоистских святилищах, в том числе большие, а не только маленькие
    бубенчики.» instead of «鈴 называет и бубенцы в синтоистских святилищах, в том числе большие.» The cat-collar example
    keeps «бубенчик», as the comprehensibility reviewer advised.
- `鐘` (line 29; consistency F3): «[鈴](鈴.md)（すず）обычно называет маленький звенящий колокольчик или бубенчик» instead of
  «鈴（すず）обычно называет маленький звенящий бубенчик», adding an RU-only link and aligning the gloss with the new 鈴
  title.
- `長所` (line 9; consistency F1): `quiz_exclusions: [得意, 利益, 味噌, 武器]`, adding 武器 «оружие; сильная сторона», whose
  figurative sense names 長所's own «сильная сторона»; RU already guards 得意–武器 for the same segment.
- `四角`:
  - line 19 (comprehensibility C2, adapted wording): «Я нарезал этот хлеб четырёхугольниками.» instead of «Я нарезал этот
    хлеб прямоугольными кусками.», which excluded squares, against line 16. The instrumental shape is shape-neutral
    between square and rectangle; the reviewer's «в виде четырёхугольника» is singular for a sliced loaf;
  - line 27 (consistency F2): `[長方形](長方形.md)（ちょうほうけい）` instead of plain 長方形（ちょうほうけい）.
- `四角い` (line 35; consistency F2) and `正方形` (line 34; consistency F2): `[長方形](長方形.md)（ちょうほうけい）` instead of
  plain 長方形（ちょうほうけい）.
- `録音` (line 31; correctness optional item): «Сохраняйте все четыре моры (ритмические единицы): ろ・く・お・ん; не
  выбрасывайте く.» instead of «Сохраняйте все четыре слога-моры: ろ・く・お・ん; не выбрасывайте く.»
- `揃う` (lines 20 and 31; comprehensibility C1): «Все необходимые документы теперь в сборе.» instead of «Все необходимые
  документы собраны.», and «書類が揃う описывает, что все документы в сборе;» instead of «書類が揃う описывает, что документы
  собраны полностью;». The intransitive 揃う no longer reads as the passive of 揃える (EN "are now together").
- `揃える` (line 30; comprehensibility C1): «書類が揃った значит «все документы в сборе»» instead of «書類が揃った значит
  «документы все собраны»». Line 31's agentive «кто-то собрал документы» stays.
- `継続` (line 22; comprehensibility C3): «Это состояние продолжается.» instead of «Это состояние сохраняется.», which is
  the territory of 維持 (EN "This state is continuing").
- `銅`:
  - lines 4 and 11 (comprehensibility C5, adapted wording): title and H1 «медь; бронзовая медаль (сокращённо)» instead of
    «медь; бронзовая медаль (сокращ.)», matching the published 中学 marker «(сокращённо)»; the reviewer's «(сокращение)»
    would repeat 略語's gloss word;
  - line 27 (comprehensibility C6, adapted wording): «Не каждое из этих чтений названия металла используется и для
    сокращения «бронзовая медаль».» instead of «Не все эти чтения названия металла переносят на себя сокращение
    «медаль».»
- `仕上がる` (line 19; comprehensibility C7): «По плану эта картина будет готова к завтрашнему дню.» instead of «Эта картина
  должна быть готова к завтрашнему дню.», dropping the obligation 予定です does not express and keeping the intransitive
  subject.
- `長引く`:
  - lines 4 and 12 (comprehensibility C8, adapted wording): title and H1 «затягиваться (по времени); долго тянуться»
    instead of «затягиваться (по времени); длиться дольше ожидаемого» (EN "drag on; be prolonged"). The second gloss
    restates line 16 and keeps EN's two-part title, so line 17's «Часто» is no longer contradicted;
  - line 22 (comprehensibility C9): «Моя простуда долго не проходит.» instead of «Моя простуда никак не проходит.»

The 撮る link at 録音:47 (part of consistency F3) and the comprehensibility optional notes (四角い's box shape, the 長男 and
長女 possessors, 鉄砲 «ружьё», and 整備 and 過程 phrasing) were not adopted; the dispositions gave the reasons (see the
reconciliation table). 録音:47 is an orthographic note on 録る against 撮る, not a comparison with 録音, and the reviewer
itself classed the optional notes as non-defects. The outside-facet title overlaps the comprehensibility reviewer listed
(継続/続き, 長引く/ずるずる/だらだら, 鉄砲/銃, 仕上がる/できる and 鉱物/鉱石) each already have a direct exclusion.

The coordinator's post-fix title screen of the three changed titles (鈴, 銅 and 長引く) is recorded in its dispositions.
鈴's only exact title segment shared with another card is «колокольчик», shared with ベル «звонок; колокольчик» and guarded by
鈴's EN exclusion of ベル; 長引く's «затягиваться» is shared with ずるずる and だらだら, both guarded by 長引く's EN exclusions;
銅 has no hit; other hits are stem-only. Fix 1 adds four RU-only links to cards in the batch at substantive comparisons:
四角→長方形, 四角い→長方形 and 正方形→長方形, where EN 四角:27, 四角い:35 and 正方形:34 name 長方形 in plain text at the
corresponding places, and 鐘→鈴, where EN 鐘:29 leaves 鈴 plain in the paragraph that links ベル. Link parity on the 31
batch paths reports only these four as extra and no EN link lost where the RU target exists. `tools/validate.py` reported
0 errors before the fix commit.

Net change from the candidate:
- titles and H1s of 鈴, 銅 and 長引く;
- example translations in 鈴 (three lines), 揃う, 四角, 継続, 仕上がる and 長引く;
- prose in 鈴 (line 39), 揃う (line 31), 揃える (line 30), 銅 (line 27), 録音 (line 31) and 鐘 (line 29);
- one exclusion (長所→武器) and four links (四角, 四角い and 正方形 to 長方形; 鐘 to 鈴).

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`5ec190a..93e2dea -- words` is thirteen word files, 24 lines added and 24 removed; with `manifest.json` the commit changes
14 files, 38 lines added and 38 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs; the
initial reports state that the model is not verifiable from inside the session.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. Each brief was sent only after the previous reviewer had replied. No recheck raised a new finding, so
there was no fix 2.

Each reviewer appended its recheck to its own report file, which stayed in its session context. Each brief included the
full words diff `5ec190a..93e2dea` and the coordinator's evidence and rationale for the edits. The correctness section
records that it read the complete recheck instructions, the supplied diff and rationale, and independently read the
actual 13-card fix diff against `5ec190a`; the consistency section records the diff as 13 word cards plus `manifest.json`
with the batch path set unchanged; the comprehensibility section records that it reread the changed passages. The recheck
sections do not reproduce the briefs, so this record does not claim their further contents.

The correctness and comprehensibility rechecks state that no generator ran, and the consistency recheck states that no
generator or `build_manifest.py` was run. The correctness and consistency reviewers each ran `tools/validate.py` (0 errors
each); the comprehensibility reviewer ran no validator. Each recheck section records snapshot `93e2dea` with a clean tree.
After the last recheck the coordinator confirmed that HEAD was `93e2dea` and that `git status --porcelain --ignored` was
empty.

### Round 1 (`93e2dea`)

| Facet | Scope and result |
|---|---|
| Correctness | Bounded recheck of all 13 changed cards against `5ec190a` and the relevant frozen EN and current RU context, plus its original C1 and optional item; it did not re-read the unchanged passages in full. C1 is **resolved**: 鈴's title includes the broader колокольчик, keeps "often rounded" as a tendency and permits large shrine examples, so a spherical rattling construction is no longer compulsory; the cat example appropriately keeps бубенчик, and the reviewer's «храмовый колокол» was an example, not a required label. The 録音:31 optional item is **resolved** (adopted verbatim; segmentation and reading unchanged). No regression: 揃う/揃える's «в сборе» keeps the completed availability without adding an agent; 四角's four-cornered pieces do not assert equal sides; the 長方形 links change no reading or claim; 継続 keeps ongoing aspect and intransitivity; 銅 keeps the bronze-medal sense and its どう restriction; 仕上がる keeps 予定, the deadline and the finished-result subject without obligation; 長引く keeps prolonged duration, with "longer than expected" still qualified as frequent; 鈴/鐘 keep the shape/use contrast and size qualification; the 長所 exclusion keeps all original metadata. Validator 0 errors. Correctness and scoped coverage are **CLEAN**, carrying forward the original full 30-card review, with no new finding. |
| Consistency | Snapshot `93e2dea` with a clean tree; the diff is 13 word cards plus `manifest.json`, with the batch path set unchanged. F1 is **resolved**: 長所 excludes 武器, with the EN entries kept in EN order. F2 is **resolved**: 長方形 is linked at 四角:27, 四角い:35 and 正方形:34 at substantive comparisons, and the links resolve. F3 is **resolved** for 鈴 at 鐘:29: the link resolves, and «колокольчик или бубенчик» agrees with the new 鈴 title and ベル:40; the declined 撮る link at 録音:47 is accepted as optional (an orthographic note, not a comparison). Title equals H1 for 鈴, 銅 and 長引く (script-confirmed). Exact-segment title screen across the full RU word pool for the three new titles: only 鈴–ベル «колокольчик» and 長引く–ずるずる and だらだら «затягиваться», all directly guarded; 銅 has none. The other edits are example or prose only, with no link or exclusion change and no new collision; no EN guard was lost. Every changed `words/` manifest entry matches its SHA-256. Validator 0 errors. Consistency, quiz safety and cross-file integration are **CLEAN**, with no new finding. |
| Comprehensibility | Snapshot `93e2dea` with a clean tree; reread the changed passages, not all 30 cards. C1 is **resolved**: 揃う reads «в сборе» while the transitive «Я собрал» / «кто-то собрал» stay, so the pair is no longer active and passive of one verb. C3, C7 and C9 are **resolved** as proposed. C2, C4, C5, C6 and C8 are **resolved** by the adapted wordings, which the reviewer no longer maintained in its proposed forms: «четырёхугольниками» is shape-neutral and natural for a sliced loaf; 鈴's «колокольчик (часто округлый); бубенчик» keeps EN's shape qualifier rather than a size rule, and avoiding «колокол» preserves 鐘, while 鐘:29's qualified «обычно … колокольчик или бубенчик» does not restore the overclaim; «(сокращённо)» is transparent; 銅:27 is readable and names «бронзовая медаль»; «долго тянуться» restates line 16 without making line 17's «Часто» definitional. The optional notes stay optional and are not pressed. No regression in the adopted 録音 optional item or in the correctness and consistency changes of fix 1. Comprehensibility and scoped coverage are **CLEAN**, with no new finding. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 鈴's title «бубенчик» narrows EN "bell (often globular)" (minor) | **Resolved** (adapted wording, merged with comprehensibility C4) | `鈴.md:4,12,20,22–23,39`; Digital Daijisen すず senses 1–2; Kuznetsov БУБЕНЦЫ; frozen EN 鈴 title and :38–40. |
| Correctness optional: 録音:31 «слога-моры» | **Optional, adopted**; resolved at recheck | `録音.md:31`; Digital Daijisen モーラ; Rybin 2009. |
| Consistency F1: 長所 «достоинство; преимущество» and 武器 «оружие; сильная сторона» (minor, quiz safety) | **Resolved** | `長所.md:9`; 武器's title; RU guards 得意–武器 for the same segment. |
| Consistency optional F2: link 長方形 in 四角:27, 四角い:35 and 正方形:34 | **Optional, adopted**; resolved at recheck | `四角.md:27`, `四角い.md:35`, `正方形.md:34`; `長方形.md` is in the batch; recorded as RU-only links. |
| Consistency optional F3: link 鈴 in 鐘:29 | **Optional, adopted**; resolved at recheck | `鐘.md:29`; `鈴.md` is in the batch; recorded as an RU-only link. |
| Consistency optional F3: link 撮る in 録音:47 | **Optional, not adopted**; accepted at recheck | 録音:47 is an orthographic note (録る against 撮る), not a comparison with 録音. |
| Consistency optional: 長女–お嬢さん and 長所–プラス | **No action** | Weak hyponym or gloss overlaps; the reviewer judged them not required. |
| Comprehensibility C1: 揃う rendered as the passive of 揃える (moderate, also coverage) | **Resolved** | `揃う.md:20,31`; `揃える.md:30`; JMdict 1406110 senses 1–2; EN "are now together". |
| Comprehensibility C2: 四角:19 «прямоугольными кусками» (minor) | **Resolved** (adapted wording) | `四角.md:19`; `四角.md:16`; JMdict 1307090 sense 1. |
| Comprehensibility C3: 継続:22 «сохраняется» (minor) | **Resolved** | `継続.md:22`; EN "This state is continuing"; 維持 contrast at line 36. |
| Comprehensibility C4: 鈴 equated with «бубенчик» (moderate) | **Resolved** (adapted wording, merged with correctness C1) | `鈴.md:4,12,20,22–23,39`; JMdict 1557580; Digital Daijisen 鈴 sense 1. |
| Comprehensibility C5: 銅 «(сокращ.)» (minor) | **Resolved** (adapted wording) | `銅.md:4,11`; JMdict 1582390 sense 2; the published 中学 marker «(сокращённо)». |
| Comprehensibility C6: 銅:27 «переносят на себя» (minor) | **Resolved** (adapted wording) | `銅.md:27`; JMdict restriction of sense 2 to どう. |
| Comprehensibility C7: 仕上がる:19 «должна быть готова» (minor) | **Resolved** | `仕上がる.md:19`; 予定です; JMdict 1305130. |
| Comprehensibility C8: 長引く title «длиться дольше ожидаемого» (minor) | **Resolved** (adapted wording) | `長引く.md:4,12`; `長引く.md:16–17`; Digital Daijisen 長引く; EN "drag on; be prolonged". |
| Comprehensibility C9: 長引く:22 «никак» (minor) | **Resolved** | `長引く.md:22`; 風邪が長引いています has no intensifier. |
| Comprehensibility optional: 四角い box shape, 長男/長女 possessors, 鉄砲 «ружьё», 整備 and 過程 phrasing | **Optional, not adopted**; kept optional at recheck | The reviewer classed them as non-defects. |
| Comprehensibility outside-facet notes: 継続/続き, 長引く/ずるずる/だらだら, 鉄砲/銃, 仕上がる/できる, 鉱物/鉱石 | **No action** | Every pair already has a direct exclusion. |
| Consistency limit: its raw-byte hash check flagged `strokes/*.json` manifest entries (it reported 114, and counted 5,014 entries) | **Not a defect**; pre-existing and outside the batch | `tools/build_manifest.py` hashes text files after CRLF→LF normalization (`sha256` at line 19). The stroke files are CRLF byte copies of EN blobs, committed and checked out unchanged under `.gitattributes` (`strokes/*.json -text`), as established in Batch 226; 118 of the 718 committed stroke blobs at `93e2dea` contain CR bytes; the coordinator re-hashed all 718 entries at `93e2dea` with the generator's normalization, and all match. The manifest's 5,019 entries are its 5,014 `files` plus 3 images and 2 scenes. Fix 1 touches no `strokes/` file. |
| Exclusion classification: the three RU-added candidate guards | **Agreed**; all kept | 丼→料理 and 過程→途中 conservative with a real basis; 鉢→植木 a topic neighbour, harmless. |

Cross-batch note: links to absent targets stay plain. Fourteen EN link targets in this batch's new cards (17 occurrences)
are absent from RU: the kanji cards 角 (from 四角 and 四角い), 賞 (from 鑑賞), 録 (from 録音), 銅 (from 銅), 鉱 (from 鉱物),
鉄 (from 鉄砲 and 鉄橋), 橋 (from 鉄橋), 針 (from 針金) and 課 (from 課程); and the word cards 三角 (from 四角), 短所 (from
長所), 釜 (from 鉢), 学科 (from 課程) and 仮定 (from 課程 and 過程). EN has kanji cards for all nine of those kanji; the
other written kanji without an RU kanji card, 継, 鑑, 鐘, 錆, 丼, 鉢, 砲, 鈴, 整, 揃 and 釣, have none in EN either. No links
were held from Batch 229.

## Final exclusion set

All 121 EN exclusion entries (28 lists; 錆 and 銅 have none) are retained in EN order. Four direct, one-sided entries are
added on four new cards (no new list):

- Conservative with a real basis (3): 丼→料理 and 過程→途中, added at the candidate; 長所→武器, added by fix 1
  (consistency F1).
- Topic only, harmless (1): 鉢→植木, added at the candidate.

Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added; the targets do not declare these pairs back.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (鈴); the 録音 optional item was adopted.
- Scoped coverage: **CLEAN** after fix 1 (揃える and 揃う).
- Comprehensibility: **CLEAN** after fix 1 (四角, 継続, 鈴, 揃える, 揃う, 銅, 仕上がる and 長引く); the optional notes remain
  optional.
- Cross-file consistency: **CLEAN** throughout; the four RU-only links from the optional notes F2 and F3 were adopted.
- Quiz safety: **CLEAN** after fix 1 (長所→武器), including the 鈴, 銅 and 長引く retitles. This covers the reviewed batch
  and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them; the comprehensibility recheck did not
  re-read all 30 cards. The unchanged cards rest on review 001, in which all three reviewers read all 30 cards in full
  against EN.
- The correctness recheck was a bounded diff recheck and records no fresh dictionary fetch; its original evidence and
  model limitations remain. The consistency reviewer did not re-fetch the dictionary senses for F1 and did not re-inspect
  the intake beyond the unchanged path set; its necessity classes are judgements, not measurements. The
  comprehensibility reviewer did not re-fetch dictionaries, run the validator or audit quiz exclusions at recheck.
- Some of the correctness reviewer's initial dictionary returns failed or were truncated; only successful entries support
  its conclusions. No normative-dictionary registration was established for донбури or патра; separate usage and history
  evidence supports those adaptations.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `5ec190a`, not `93e2dea`.
- The consistency reviewer's stroke count (114) and entry count (5,014) came from its own raw-byte script and were not
  reconciled by it; 118 of the 718 committed stroke blobs at `93e2dea` contain CR bytes, matching the working tree.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
