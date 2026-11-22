# Batch 238 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `4f48fb310543d50e79bee85665e6e5bc31aa1c48` | `70cbbc2f8a5c3164eb0d8bf2d73bb96796a40cc6` | Initial review snapshot: the signed candidate, on `origin/full-ru-238-words-77`. |
| `f664ac5c031aace064a508fa710fc8e06021a7bd` | `24d97cbff5ae31d8aeea528ea69e9810cc42d71a` | Fix 1 (final candidate). It covers correctness F1 and F2, consistency Q1, Q2, Q3, C1 (with two of its weaker cases) and T1, comprehensibility C238-1 to C238-9 (C238-2, C238-3 and C238-9 with adapted wording; C238-4 and C238-6 partially; C238-5 through F1), the seven conservative pairs the consistency reviewer listed, and the 見下ろす optional raised by all three reviewers. It adds nine exclusions (あらすじ→内容 and 筋, 要領→実 and 技術, 個体→身体, 要旨→圧縮, 見学→出席, 標本→代表 and サンプル→型), removes two RU-added ones (見出し→サイン and 署名), adds four RU-only links and removes none. Signed; on `origin/full-ru-238-words-77`. |

Fix 1 changed sixteen word files and regenerated `manifest.json` (`contentVersion` `63b555f09410c1b9`, 5,259 entries:
5,254 `files` + 3 images + 2 scenes; the candidate had `b74b9d64eb49d4e7`). The intake was not refreshed; it still records
the candidate's 33 payload hashes.
- `見かけ` (lines 4 and 12; correctness F1, also resolving comprehensibility C238-5): title and H1 «внешний облик (в
  отличие от сути)» instead of «видимость; внешний облик (в отличие от сути)», the reviewer's shorter remedy and one
  segment like EN :4 "outward appearance". The comprehensibility reviewer's extra segment «кажущийся вид» was not added.
- `改める` (lines 44–45 and 47; correctness F2): «Словарь отмечает и другие употребления — «делать как положено, соблюдая
  формальности», — кроме приведённых здесь примеров.» instead of «Словарь отмечает и другие, более книжные употребления,
  кроме приведённых здесь примеров.», removing the unsupported register claim and restoring EN :44's "further
  formal/proper-action uses"; the citation line now ends «значения 1–3; другие употребления — значение 4.» instead of
  «значения 1–3.» (JMdict 1200750 sense 4), a verified clarification beyond EN's "senses 1-3".
- `改める` (line 21; comprehensibility C238-1): «— Я хочу исправить свои плохие привычки.» instead of «— Я хочу
  избавиться от вредных привычек.», the reform sense of the title «исправлять (привычки)» and EN "correct my bad habits".
- `あらすじ` (new line 9; consistency Q1 and the conservative pair あらすじ–筋): `quiz_exclusions: [内容, 筋]` on a new
  line after `tags:` (あらすじ has no exclusions in EN).
- `あらすじ` (line 20, formerly 19; comprehensibility C238-4, partially adopted): «— Расскажите, пожалуйста, краткое
  содержание этого романа.» instead of «— Перескажите, пожалуйста, вкратце содержание этого романа.» «Расскажите» fixes
  the speech act of 教えてください; «краткое содержание», the card's own first title segment, is kept, and the reviewer's
  «сюжет», the title of 筋, was not used.
- `要領` (line 9; consistency Q2 and the conservative pair 要領–技術): 実 and 技術 appended to `quiz_exclusions`.
- `見出し` (lines 4, 9 and 12; consistency Q3): title and H1 «заголовок (статьи, раздела); заглавное слово (словарной
  статьи); указатель» instead of «заголовок (статьи, раздела); подпись (к фото); заглавное слово (словарной статьи);
  указатель», and the two RU-added guards サイン and 署名 removed, restoring the EN list [題, 題名, 項目, 索引, 説明]. The
  body (:16, «название или подпись», EN "title or caption") is unchanged; the reviewer's body rewording was not adopted.
- `サンプル` (line 32; consistency C1): `[見本](見本.md)（みほん）` and `[標本](標本.md)（ひょうほん）` instead of plain
  見本（みほん） and 標本（ひょうほん）; line 9 appends 型 (conservative pair).
- `個体` (lines 4 and 12; consistency T1): title and H1 «особь; отдельный организм; экземпляр» instead of «особь; отдельный
  организм», restoring EN's "specimen" and matching kanji/個:36 and the body.
- `個体` (line 36; C1 weaker case): `[集団](集団.md)（しゅうだん）` instead of plain 集団（しゅうだん）; 種（しゅ） stays
  plain (RU words/種.md is たね «семя»). Line 9 appends 身体 (conservative pair).
- `おおよそ` (line 35; C1 weaker case): `[正確](正確.md)に（せいかくに）` instead of plain 正確に（せいかくに）.
- `御覧` (lines 4 and 12; comprehensibility C238-3, adapted wording): title and H1 «взгляд (уважительно о чужом); посмотри;
  попробуй (сделать)» instead of «взгляд (уважительно о чужом); попробуй (сделать)», covering the bare-ごらん "look!" use
  taught by «Смотри, радуга!» (EN "a look; try it"). The honorific qualifier stays on «взгляд» only; the reviewer's
  «посмотри (уважительно или по-простому)» was not used.
- `見慣れる` (line 19; comprehensibility C238-2, adapted wording): «— Это привычный глазу пейзаж.» instead of «— Это
  привычный, хорошо знакомый пейзаж.», dropping the knowing sense that the card's 知る/親しい contrasts exclude (EN
  "familiar scenery"). The reviewer's «привычный на вид» was not used.
- `見本` (line 27; comprehensibility C238-6, partially adopted): «В метаданных оно отнесено к `wago` по исконному первому
  элементу, как принято в этом репозитории.» instead of «В метаданных по принятому в проекте правилу такие слова
  отмечены как исконные.», following the published 王様:24 pattern. Deleting the remark, as proposed, was declined: EN
  keeps it and published RU cards carry the same kind of note (王様:24, 景色:38, 気付く:50).
- `見下ろす` (lines 39–40, formerly 39–41; comprehensibility C238-7 and the matching correctness and consistency
  optionals): the sentence «Комната может «смотреть» на море сверху, но 見下ろす — не обычный глагол для того, чтобы
  случайно не заметить ошибку.» is removed and the following caution now begins «Не настаивайте…» instead of «И наоборот,
  не настаивайте…». The room-and-sea view remains taught at :16/:19.
- `複数` (line 39; comprehensibility C238-8): the sentence ends «окончания множественного числа.» instead of «…
  множественного числа, как в английском.» The English-noun example at :20 is unchanged.
- `見学` (line 25; comprehensibility C238-9, adapted wording): «Это не обязательно значит уйти с урока; отдельно уровню N2
  это употребление не присвоено.» instead of «Это не обязательно значит уйти с урока, и для N2 это не отдельное задание.»,
  following published 削る:25 (EN "is not a separate N2 assignment"); line 9 appends 出席 (conservative pair).
- `標本` (line 9; conservative pair) appends 代表, and `要旨` (line 9; conservative pair) appends 圧縮 after the existing
  RU-added 実.

The correctness reviewer's other optional, ぶつける «швырять»/«швырнул» (also a comprehensibility optional), was not
adopted: JMdict 2742080 sense 2 includes "fling; hurl", and «швырять» keeps the hitting-throw distinct from 投げる
«бросать» (excluded). Nor were the consistency reviewer's 見学:4 title-proportion optional (the qualifier names the
PE-observation use taught at :23–25, and 出席 is now excluded), its body rewording for Q3, or the 個体 → 種 link (RU
words/種.md is the different word たね «семя»). The comprehensibility optionals on 見舞う:28, 見かけ:17, サンプル:27 and
書き取り:18 raised no defect and had no action; 索引's lack of exclusions needed none, as the 見出し–索引 pair is declared on
the 見出し side and exclusions are symmetric pair declarations. Whether metadata remarks like 見本:27 should be dropped
corpus-wide is recorded in the dispositions as a follow-up, not a one-card change. The dispositions gave the reasons (see
the reconciliation table).

The coordinator's post-fix title screen of the four changed titles (`b238-postfix-screen.txt`; pool: the RU word titles)
prints ten `OK` lines for guarded pairs and 81 stem-only `!!` lines. Its one exact shared segment is 見出し–題名
«заголовок» (題名 «название (произведения); заголовок»), guarded by the EN pair; 見かけ «внешний облик» meets 様子
«положение дел; облик» and, by the «внешн» stem only, 格好 and 表面, all guarded by EN pairs; 個体 meets 個人, 生物 and
身体 by stems only, all guarded; 御覧 meets ごらんになる by the «уважи» stem, guarded. The dispositions summarise this as
"no exact-segment overlap with any RU word title" with the remaining unguarded leads "qualifier/stopword stems (уважи-,
сдела-, отдел-, орган-, слово-, стать-, отлич-)", and state that «посмотри» and «экземпляр» occur in no other RU title.
The consistency recheck, by its own script over all RU word titles, found that "the four new titles have no exact-segment
overlap with any other RU title that lacks a guard on either side". The dispositions also record a corpus grep of the RU
primary checkout for the removed wording with no remaining quote, the only hits being the Batch 239 lane's copies of the
candidate files, and no Batch 239 draft referencing the changed cards. They record `tools/validate.py` 0 errors, the unit
tests (124) OK, the content budget OK and a 5,259-entry manifest in the post-fix state.

Net change from the candidate:
- titles and H1s of 見かけ, 見出し, 個体 and 御覧;
- example translations in 改める, あらすじ and 見慣れる;
- prose in 改める (lines 44–45 and the citation at 47), 見本 (line 27), 見下ろす (lines 39–40), 複数 (line 39) and 見学
  (line 25);
- nine appended exclusions on eight cards (あらすじ on a new line) and two RU-added exclusions removed from 見出し;
- four RU-only links (サンプル:32 → 見本 and 標本, 個体:36 → 集団 and おおよそ:35 → 正確); no link removed.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`4f48fb3..f664ac5 -- words` is sixteen word files, 30 lines added and 29 removed; with `manifest.json` the commit changes
17 files, 47 lines added and 46 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs;
the correctness report states that the model identity is not independently verifiable, the consistency report that it
cannot name its model, and the comprehensibility report, initially and at recheck, that the model name is not verifiable.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. Each recheck covered the full diff `4f48fb3..f664ac5`. No recheck raised a new finding, so there was
no fix 2.

Each reviewer appended its recheck to its own report file. The correctness section records that the live 16-card diff
exactly matches the supplied diff and that all changed passages were checked against frozen EN and its earlier full
review; the consistency section records scripted regression checks of titles, exclusions, links and removed wording on
all 16 changed cards against the working tree at `f664ac5`; the comprehensibility section records that it read the
changed passages and reconciles each of its findings. Each recheck brief told the reviewer to read it in full; the recheck
sections do not reproduce the briefs or state that they were read in full, so this record does not claim their contents.

All three rechecks state that no generator was run. The consistency reviewer ran `python -B tools/validate.py` (0 errors,
no `__pycache__` left) and compared `manifest.json` with an in-memory `build_manifest()` result (equal); the correctness
reviewer states that no generator or validator was run and no repository was written, and the comprehensibility reviewer
records no validator run. The correctness section records snapshot `f664ac5` with HEAD verified and a clean tree, the
consistency section `f664ac5` with an empty `git status --porcelain` before and after, and the comprehensibility section
`f664ac5` with an empty porcelain status. The recheck records include no separate coordinator status check after the
rechecks; when these records were drafted, a read-only check showed the RU checkout on `full-ru-238-words-77` at HEAD
`f664ac5c031aace064a508fa710fc8e06021a7bd` with `git status --porcelain --ignored` printing nothing.

### Round 1 (`f664ac5`)

| Facet | Scope and result |
|---|---|
| Correctness | Snapshot `f664ac5`, HEAD verified, clean tree; the live 16-card diff exactly matches the supplied diff; all changed passages checked against frozen EN and the earlier full review. F1 is **resolved**: 見かけ:4/:12 removes the misleading standalone gloss, and the outward-appearance and apparent-size teaching remain. F2 is **resolved**: 改める:44–47 restores proper/formal action, removes the register claim and cites JMdict 1200750:4. The 見下ろす optional is **resolved** by removing the English-dependent room/error contrast, keeping the physical-view examples and the contempt caution (1259370:2). The ぶつける optional "remains optional, not adopted": "fling/hurl" supports the unchanged translation. Other changes: 御覧 now covers JMdict 1270760:1–3, with only the looking noun qualified as respectful; 個体 «экземпляр» is faithful (Kuznetsov, sense 2); 見出し keeps heading, headline, index and the headword sense (1259710:3), with caption still in the body; the translations in 改める:21, 見慣れる:19 and あらすじ:20 are at least as accurate as before ("adopting them does not establish defects in the old versions"); 見本:27 accurately describes its own wago front matter; 見学:25 and 複数 keep EN's notes. New links have existing targets; added exclusions remove no EN guard, and 見出し removes only RU-added guards; Japanese example and kana payloads are unchanged on all 16 cards. Evidence: live publisher JMdict entries 1200750, 1259370, 1259710, 1264980, 1270760, 1396970 and 1604650; Kuznetsov «экземпляр». No generator or validator was run. Correctness **CLEAN** and scoped coverage **CLEAN**; Russian comprehensibility **UNVERIFIED** (not assigned); no new actionable regression. |
| Consistency | Snapshot `f664ac5`, empty `git status --porcelain` before and after; read-only; only `python -B tools/validate.py` run (0 errors), no generator; manifest equal to an in-memory rebuild. Q1, Q2, Q3, C1 (with the 個体→集団 and おおよそ→正確 links) and T1 are **resolved**; あらすじ→筋 is "an RU-added extra, defensible", and 要領→技術 its own adopted optional. The declined 個体 → 種 link is **withdrawn** ("agreed"), the 見下ろす optional **resolved** and the 見学 title-proportion optional **withdrawn**. The adopted optional guards are all present and appended after the EN lists; "Remaining optional-not-adopted items: none that affect safety." Scripted regression checks on all 16 changed cards: title equal to H1 (four title changes); the EN list an exact prefix in EN order on every card, with RU additions only appended and 見出し carrying none; no unguarded exact-segment overlap for the four new titles (its own script over all RU word titles); no broken relative link and no orphan of the removed wording anywhere in the tree. Consistency **CLEAN**, quiz safety **CLEAN** and cross-file integration **CLEAN**. |
| Comprehensibility | Snapshot `f664ac5`, empty porcelain status; read the changed passages, not all 30 cards; the four new link targets exist. C238-1, C238-7 and C238-8 are **resolved**; C238-2, C238-3, C238-4, C238-5 and C238-9 are **resolved**, with the reviewer not maintaining its alternative wordings («привычный на вид», the qualifier on «посмотри», «сюжет», «кажущийся вид», a freer rewrite of 見学:25); C238-6 is **partially resolved, deletion not maintained** ("Residual «метаданные» and `wago` are corpus-wide, not a one-card disagreement"). The ぶつける «швырнул» optional is **withdrawn**; 見舞う, 見かけ:17, サンプル:27 and 書き取り are not reopened; the 索引 note stays outside these facets. No regression: 見かけ's single gloss is clear, 見出し keeps «название или подпись» in the body, 個体 «экземпляр» matches the body and EN "specimen", the 改める sense-4 gloss is plain Russian, and the new links have readings. Comprehensibility **CLEAN** and scoped coverage **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 見かけ's first title segment «видимость» means visibility or a deceptive semblance (P2, medium) | **Resolved** | `見かけ.md:4,12`; EN :4 "outward appearance"; JMdict 1604420 senses 1–2; Kuznetsov «видимость» senses 1–2. |
| Correctness F2: 改める:44 «более книжные» is an unsupported register claim and loses "formal/proper-action uses" (P3, low; also scoped coverage) | **Resolved** | `改める.md:44–45,47`; EN :44; JMdict 1200750 sense 4; Digital Daijisen 改める sense 3. |
| Correctness optional: 見下ろす:39–40 keeps the English "overlook" room/error juxtaposition | **Resolved** (adopted with comprehensibility C238-7) | `見下ろす.md:39–40`; JMdict 1259370 sense 2. |
| Correctness optional: ぶつける:4/:21 «швырять»/«швырнул» | **Not adopted**; remains optional at recheck | JMdict 2742080 sense 2 "fling; hurl"; Kuznetsov «швырять» sense 1; 投げる «бросать» is excluded. |
| Consistency Q1: あらすじ–内容 share «содержание», unguarded (medium) | **Resolved** | `あらすじ.md:9` `quiz_exclusions: [内容, 筋]`; 内容 «содержание; суть». |
| Consistency Q2: 要領–実 share «суть», unguarded (low-medium) | **Resolved** | `要領.md:9`; 実 «плод; суть»; matches the existing 要旨→実 guard. |
| Consistency Q3: 見出し's «подпись (к фото)» narrows the title and motivates the サイン/署名 guards (low, optional) | **Resolved** (title adopted; body rewording not adopted) | `見出し.md:4,9,12`; EN title "heading; headline; index"; body :16 «название или подпись» (EN "title or caption") unchanged; the EN list [題, 題名, 項目, 索引, 説明] restored. |
| Consistency C1: サンプル:32–33 leaves 見本 and 標本 plain although compared (low) | **Resolved**; weaker cases 個体→集団 and おおよそ→正確 adopted | `サンプル.md:32`, `個体.md:36`, `おおよそ.md:35`; RU `.github/instructions/content-structure.instructions.md:42`; precedent きちんと:29. |
| Consistency C1 weaker case: 個体:36 種 | **Withdrawn** at recheck; declined | RU words/種.md is たね «семя», a different reading and word. |
| Consistency T1: 個体's title loses EN "specimen" (low, optional) | **Resolved** | `個体.md:4,12`; EN "individual organism; specimen"; kanji/個:36; Kuznetsov «экземпляр» sense 2. |
| Consistency optional: seven conservative pairs (個体–身体, 要領–技術, 要旨–圧縮, 見学–出席, 標本–代表, サンプル–型, あらすじ–筋) | **Resolved** (adopted) | Displayed-label overlaps checked by the coordinator; all appended after the EN lists; あらすじ–筋 "defensible" at recheck. |
| Consistency optional: 見下ろす:39–41 calques "overlook" | **Resolved** (adopted with comprehensibility C238-7) | `見下ろす.md:39–40`. |
| Consistency optional: 見学:4 title weighted towards «присутствие без участия» | **Withdrawn** at recheck; declined | The qualifier names the PE-observation use taught at :23–25; 出席 is now excluded. |
| Comprehensibility C238-1: 改める:21 «избавиться от вредных привычек» states removal (medium) | **Resolved** | `改める.md:21`; EN "correct my bad habits". |
| Comprehensibility C238-2: 見慣れる:19 «хорошо знакомый» adds knowing (medium) | **Resolved** (adapted wording; alternative not maintained) | `見慣れる.md:19`; the card's 知る/親しい contrasts; EN "familiar scenery". |
| Comprehensibility C238-3: 御覧's title misses the "look!" use (medium) | **Resolved** (adapted wording; alternative not maintained) | `御覧.md:4,12`; EN "a look; try it"; JMdict 1270760 senses 1–3 (sense 3 hon.). |
| Comprehensibility C238-4: あらすじ:19 «Перескажите» and 内容's title word «содержание» (medium) | **Resolved** at recheck (partially adopted: «краткое содержание» kept; «сюжет» not maintained) | `あらすじ.md:20`; «сюжет» is 筋's title; あらすじ–内容 and あらすじ–筋 are now guarded. |
| Comprehensibility C238-5: 見かけ's first gloss «видимость» (medium) | **Resolved** through correctness F1; «кажущийся вид» not added and not maintained | `見かけ.md:4,12`; EN single gloss; :17 teaches the apparent-size use. |
| Comprehensibility C238-6: 見本:26 metadata sentence is author-facing (low) | **Partially resolved**; deletion declined and not maintained at recheck | `見本.md:27`; EN keeps the remark; 王様:24, 景色:38, 気付く:50; the corpus-wide question is a follow-up. |
| Comprehensibility C238-7: 見下ろす:37 rejects a meaning only English "overlook" suggests (low) | **Resolved** | `見下ろす.md:39–40`. |
| Comprehensibility C238-8: 複数:39 «как в английском» (low) | **Resolved** | `複数.md:39`. |
| Comprehensibility C238-9: 見学:25 bare «для N2» (low) | **Resolved** (adapted wording; freer rewrite not maintained) | `見学.md:25`; published 削る:25; EN "is not a separate N2 assignment". |
| Comprehensibility optional: ぶつける:18 «швырнул» | **Withdrawn** at recheck; declined | «швырять» is the title; «бросить» would blur the excluded 投げる. |
| Comprehensibility optionals: 見舞う:28, 見かけ:17, サンプル:27, 書き取り:18 | **No action**; not reopened at recheck | The reviewer raised no defect. |
| Comprehensibility note outside its facets: 索引 has no exclusions | **No action** | The 見出し–索引 pair is declared on the 見出し side (EN list); exclusions are symmetric pair declarations. |

Cross-batch note: links to absent targets stay plain. Twelve EN link occurrences in this batch's new cards, to ten
targets, are absent from RU: ぶつける → ぶつかる, 改める → kanji 改 and 改めて, 改正 → kanji 改, 改造 → kanji 改 and 造,
看板 → kanji 板, 要領 → kanji 領 and 能率, 西暦 → 生年月日, and 複数 → kanji 複 and 単数. The other written kanji without an
RU kanji card, 攻, 旨, 暦, 概, 標, 看, 索, 襖 and 覧, have none in EN either. No links were held from Batch 237, and none is
held from this batch. Whether metadata remarks like 見本:27 («В метаданных…») should be dropped corpus-wide is on the
follow-up list recorded in the dispositions; this record does not claim that any issue comment was posted.

## Final exclusion set

All 229 EN exclusion entries (27 lists; 索引, あらすじ and 複数 have none in EN) are retained in EN order; 33 of them lie
inside the batch, and the other 196 target existing RU cards. Eleven direct, one-sided entries are added on eight new
cards, all appended at the end of their lists, あらすじ's on a new `quiz_exclusions` line: two from the candidate
(改める→調べる and 要旨→実, from the authoring lane as adjudicated by the coordinator) and nine from fix 1 (あらすじ→内容,
consistency Q1; 要領→実, Q2; and the seven conservative pairs 個体→身体, 要領→技術, 要旨→圧縮, 見学→出席, 標本→代表,
サンプル→型 and あらすじ→筋). The candidate's two other RU-added entries, 見出し→サイン and 見出し→署名, were removed by fix 1
with the «подпись (к фото)» title segment (Q3); the lane's 看板→誇り had already been removed by the coordinator before
the candidate. The coordinator classed the four candidate entries as required for exact segments. The consistency reviewer
classed them as follows:

- Required (1): 改める→調べる.
- Conservative (3): 見出し→サイン and 見出し→署名 while the title kept «подпись (к фото)» (removed by fix 1), and 要旨→実,
  to be kept if Q2 was applied (kept).

It raised あらすじ→内容 as required (Q1) and 要領→実 as a missing guard (Q2), and listed the seven fix-1 conservative pairs
as "conservative at most". At recheck it confirmed all nine as present and appended after the EN lists, judged あらすじ→筋
"defensible" and confirmed that 見出し's list is exactly EN's. Every RU addition is appended at the end of its list; the
only removals are 見出し's two RU-added guards, and no EN entry is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (見かけ F1 and 改める F2).
- Scoped coverage: **CLEAN** after fix 1 (改める F2); comprehensibility review scoped coverage **CLEAN** throughout.
- Comprehensibility: **CLEAN** after fix 1 (改める, 見慣れる, 御覧, あらすじ, 見かけ, 見本, 見下ろす, 複数 and 見学); C238-6
  stands as partially resolved, with the deletion not maintained and the corpus-wide question on the follow-up list.
- Cross-file consistency: **CLEAN** after fix 1 (C1 and T1); the four RU-only links (サンプル:32 → 見本 and 標本,
  個体:36 → 集団 and おおよそ:35 → 正確) and the three restored navigation links in three files stand.
- Quiz safety: **CLEAN** after fix 1 (Q1, Q2 and Q3), including the 見かけ, 見出し, 個体 and 御覧 retitles. This covers the
  reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed cards or passages and the lines needed to judge them; the comprehensibility
  recheck did not reread unchanged cards in full or retest quiz runtime. The unchanged cards rest on review 001, in which
  all three reviewers read all 30 cards in full (the consistency reviewer read nine EN originals in prose, two of them
  partly, and compared the others mechanically).
- The correctness recheck re-inspected live publisher JMdict entries and Kuznetsov «экземпляр»; it ran no validator or
  unit tests, and its original dictionary-version, whole-pool, app and native-acceptance limits remain. The consistency
  reviewer did not consult live dictionaries, cited dictionary bases from the cards' entry numbers and its own knowledge,
  did not rerun the unit tests or content budget, and its title screen is its own exact-segment script, not a semantic
  read of all 3,793 titles. Its necessity classes are judgements, not measurements.
- The comprehensibility review read the navigation files as diffs only and did not review the intake JSON.
- Whether metadata remarks like 見本:27 should be dropped corpus-wide is a follow-up, not decided by this batch.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `4f48fb3`, not `f664ac5`.
- Frequency and preferred register (for example «швырять», «привычный глазу», «краткое содержание») were not certified.
  Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
