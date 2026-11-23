# Batch 253 — independent recheck 001

## Snapshots

| Stage | Signed commit | Tree | Parent |
|---|---|---|---|
| Blind candidate | `bbe4e485115525a1f4bd661960486449dbe4570b` | `a46d590fde1002c23b72346587efb6c17d0ea7c7` | `7126ab8be4bf9ea8358b57a02e673fef007278f4` |
| Fix 1 / reviewed content | `c972b6793d49df2da0e4b62ba2636114e53a0f62` | `f8fd357abbd293ba268e17ef378117682e04fd92` | `bbe4e485115525a1f4bd661960486449dbe4570b` |

Original content branch `full-ru-253-words-92`; published baseline `6efe3ec4f81c0fb39b6478cbfd15d46199db1fc7`; frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. No later integration commit is a reviewed-content snapshot in this record.

The original reviewers each rechecked the single candidate-to-fix diff **once**, serially and in the same order as the blind reviews: correctness (`gpt-6.1-sol`, `f8dfbe0c-bd07-49ff-b12d-6bb92e7a61e5`), consistency (`claude-sonnet-5.5`, `99dd73a9-bf30-4991-870c-6ced97d29aca`), comprehensibility (`grok-4.7`, `20c8cfac-fabd-488d-9861-f1b1f56f9bfd`). All completed normally before restart, including the original comprehensibility reviewer. No replacement, second fix, second round or addendum. Each recheck is a separate report, not a silently rewritten blind review.

**Brief delivery:** The coordinator's 2026-11-23 UTC session events record three complete inline sends, not messages pointing to files. `b253-recheck-msg-correctness.txt` was saved at 19:04:29Z **before** the 19:04:53Z send. `b253-recheck-msg-consistency.txt` and `b253-recheck-msg-comprehensibility.txt` were extracted verbatim **after** the 19:10:22Z and 19:15:10Z sends, respectively. The times of these copies are not evidence of file-pointer delivery or the order of review completion. The runtime model identities were verified by the coordinator in `read_agent` results, not independently authenticated by all reviewers. The briefs define the requested scope; the reports below define what was actually read.

### What changed

Eight `title`/H1 pairs changed; the other six changed word cards have body edits only. Everything in this table is quoted from the two pinned snapshots, not reconstructed from a suggested replacement.

| New word card | Candidate title | Fix 1 title |
|---|---|---|
| 水蒸気 | водяной пар; горячий пар | водяной пар |
| 演劇 | театральное искусство; драматическое искусство | театральное искусство; драматическая постановка |
| 測量 | топографическая съёмка; обмер (местности, построек) | съёмка местности; измерение |
| 深まる | углубляться; крепнуть (о чувстве, связи) | углубляться; усиливаться |
| 溶け込む | полностью растворяться (в жидкости); вливаться (в коллектив, обстановку) | растворяться в чём-либо; вливаться (в коллектив, обстановку) |
| 湧く | бить ключом; хлынуть; зарождаться (о чувстве, мысли) | бить ключом; хлестать наружу; зарождаться (о чувстве, мысли) |
| 清掃 | очистка; уборка территории | очистка; уборка (помещений, улиц) |
| 混ざる | перемешиваться; оказываться среди (других); принимать участие (в игре) | перемешиваться; оказываться среди (других); присоединяться (к другим) |

**Rewritten example translations.** Japanese sentences and kana readings are unchanged. The EN column gives the corresponding translation in the frozen EN card, not a third proposed Russian gloss.

| Card:line | Frozen EN | Candidate | Fix 1 |
|---|---|---|---|
| 溶け込む:20 | The sugar dissolved into the water. | Сахар полностью растворился в воде. | Сахар растворился в воде. |
| 売り切れる:20 | The popular bread sold out during the morning. | Популярный хлеб распродали ещё утром. | Популярный хлеб был распродан ещё утром. |
| 売り切れる:21 | Let's buy tickets before they sell out. | Давайте купим билеты, пока их не распродали. | Давайте купим билеты, пока они не разошлись. |
| 湧く:21 | A good idea came to me. | Мне пришла в голову хорошая мысль. | У меня родилась хорошая мысль. |
| 混じる:18 | There were small stones mixed into the sand. | В песке попадались мелкие камешки. | К песку примешались мелкие камешки. |
| 深夜:21 | A late-night phone call woke me up. | Меня разбудил ночной телефонный звонок. | Меня разбудил телефонный звонок глубокой ночью. |

**Other edits, including both deletions:**

- `湧く:50`: `Значения «кипеть, нагревать» относятся к 沸く, даже если в каком-то списке` → `Значения «кипеть» и «нагреваться» относятся к 沸く, даже если в каком-то списке`. Lines 51–52 still warn about the list. The voice error, not the whole hedge, was removed.
- `深夜:23`: `深夜の + существительное даёт «ночной, поздненочной», как во втором примере.` → `深夜の + существительное можно передать словом «ночной» или оборотом «глубокой ночью», как во втором примере.` The context permits multiple renderings; the example uses the latter.
- `混ぜる:38`: `частицей -ся` → `постфиксом -ся` in the Russian explanation of the transition from «смешивать» to «смешиваться». The contrast of Japanese verbs, particles and argument roles remains. EN :38 uses the English verb “mix” for the comparison.
- `湿る:43`: the JMdict link/ID and both senses remain; `значение 2 дополняет значение «сырость» из исходного списка слов.` → `значение 2 дополняет физическое значение «сырость».` This changes a source-list reference, not the link.
- Deleted candidate `測量:42` in full: `測量 не значит просто «осмотреться».` Frozen EN :42 is `測量 does not simply mean "look around."` This is an English-dependent disambiguation of “survey”, not the rule about Japanese measurement. The practical spatial-information explanation, the 調査 comparison and the warning against restricting the word to land remain. Keeping one such deletion distinct from a lost source rule follows the narrow B251 precedent.
- Deleted candidate `湯気:44` in full: `Эта карточка учит слову ゆげ, а не постороннему заголовку с чтением ゆけ.` Frozen EN :44 is `This card teaches ゆげ, not an unrelated heading read ゆけ.` Unlike 測量, this deletion is about an unseen **dictionary heading**, not English polysemy. The ゆげ reading, voicing and visible-droplet/蒸気 discussion remain. Neither deletion removed an href or a footer citation.
- `kanji/劇.md:36`, candidate: `- [演劇](../words/演劇.md)（えんげき）— театр; драматическое искусство`; fix: `- [演劇](../words/演劇.md)（えんげき）— театральное искусство; драматическая постановка`. The candidate had restored the existing EN link; the fix changes **only the list gloss**, not the target, reading or number of links. `words/芝居.md:37` keeps `[演劇](演劇.md)（えんげき）тоже называет театр, драматическое искусство.` That prose comparison is not an unchanged duplicate of the full candidate title.

The fix diff has 16 paths: 14 of the 30 new word cards, this one of the nine existing navigation files, and `manifest.json`. Content-only diff: 27 insertions / 29 deletions; with manifest: 43 / 45. Manifest `contentVersion` changed from `5f4fb4d0fef20eaa` to `2501311c849efeb7`; only the corresponding 15 content hashes changed. Both manifests contain 5,709 entries (5,704 `files`, three images, two scenes). The fix changed no non-title front matter, links, exclusions or Japanese examples. None of the eight full superseded title strings occurs in the fixed tree's tracked `.md`, `.json` or `.txt` files. This is a snapshot-specific literal check, not a ban on those words elsewhere.

Three narrow precedents explain the accounting, not the verdicts. B250 counted 特長 once when reached through 特色 despite also being requested; the corresponding B253 case is 溶く through 溶かす. B246 counted a changed gloss beside the restored link in `長所:31` without counting a new link; B243 left a contextual navigation gloss at `ぞくぞく:26` unchanged. B253 distinguishes the revised `劇:36` list gloss from the unchanged `芝居:37` comparison. B251 recorded one English-dependent line removed at `射す:39`; here that category fits `測量:42` only, not the external dictionary-heading line at `湯気:44`.

### Round 1 (`c972b67`)

| Facet | Actual scope and verdict |
|---|---|
| Correctness / scoped coverage | The reviewer reports full RU **and frozen EN** reads of all 14 changed words **and** `kanji/劇.md`, the fix passages, original correctness report, dispositions and manifest delta; primary JMdict checked anew, KANJIDIC2 for 劇 and selected Russian/Japanese dictionary evidence. It matched the 15 changed SHA-256 hashes and found no change to links, non-title metadata or Japanese examples. “Verdicts: Correctness CLEAN; scoped coverage CLEAN on HEAD. C1/C2 resolved; no new actionable defect established. CLEAN is bounded to this recheck, not exhaustive certification of the repository.” |
| Consistency / quiz safety | The reviewer read the complete fix **diff**, dispositions and coordinator screen, **not the 14 full cards**. It additionally read `測量:37–end` and `湯気:39–end`, compared H1/title, other metadata, superseded strings, exclusions and hashes mechanically, and sampled stem leads. `validate.py` printed `0 error(s)`; the reviewer removed the bytecode cache. “Consistency on HEAD: CLEAN.” “Quiz safety on HEAD: CLEAN for the new overlaps. Necessity of the 14 RU-only guards stays UNVERIFIED, as in the original report (no live dictionary was consulted).” |
| Comprehensibility | The reviewer reports full reads of the 14 changed words, unchanged クリーニング (C4) and `kanji/劇.md`; it compared titles/exclusions for 測定, 増す, 掃除, 加わる, 浮かぶ, 沸く, 芝居, 公演 and used the saved screen. “Verdicts: comprehensibility CLEAN.” “Findings: none”. **No separate final scoped-coverage verdict** was issued by this reviewer. It still described C8 as partially resolved. |

## Reconciliation

The numbers C1/C2 in the correctness report and C1–C13 in the comprehensibility report are separate series. Statuses below are the original reviewer's recheck dispositions, not a blanket approval of the coordinator's edit choices.

| Original item | Recheck status | What the reviewer accepted, retained or declined |
|---|---|---|
| Correctness C1 (Medium), 湧く | **RESOLVED** | :50 now assigns intransitive «нагреваться» to 沸く; JMdict 1606680 sense 1. |
| Correctness C2 (Low; scoped coverage), 深夜 | **RESOLVED** | :21 restores lateness; :23 permits attributive/adverbial renderings without redefining 深夜 as generic 夜. JMdict 1362810. |
| Correctness optional: 湧く aspect | **RESOLVED** | Imperfective «хлестать наружу» retains the outflow sense. |
| Correctness optional: 混ぜる morphology | **RESOLVED** | «постфиксом -ся» clarifies the bound element without changing the Japanese rule. |
| Consistency F1 (Low), 溶け込む | **RESOLVED** | No «полностью» in title or sugar example; remaining title length called cosmetic. |
| Consistency F2 (Low), 温帯→適度 | **WITHDRAWN** | Decline stands: zone and degree differ, but Russian «умеренный» covers “temperate” and “moderate”. The reviewer calls keeping it harmless, not necessary. |
| Consistency F3 (Info), 水蒸気 | **RESOLVED** | Single label «водяной пар», not «горячий пар». |
| Consistency F4 (Info), 湧く and 清掃 | **OPTIONAL**, informational (湧く); **RESOLVED** (清掃) | No missing-kanji note restored; written metadata correct. 清掃 now covers indoor/outdoor cleanup, keeps «очистка» first. |
| Comprehensibility C1 (high), 水蒸気 | **resolved** | Title no longer teaches the visible cloud in place of gas; 湯気 contrast remains. |
| C2 (medium), 演劇 | **resolved** | Performance now represented in title. Suggested «спектакль» example rewrites declined, not reopened; examples natural, 芝居/公演 guarded. |
| C3 (medium), 測量 | **resolved** | «съёмка местности; измерение» restores general measurement in EN order; deletion leaves a coherent explanation; 測定 carries the guard. |
| C4 (medium), クリーニング | **withdrawn** | Re-read unchanged: first gloss already «чистка», opening gives химчистка, :24 prevents a dry-cleaning-only sense; Latin `cleaning` glossed as the etymon in the same sentence. |
| C5 (medium), 深まる | **resolved** | Season and feeling covered; accepted the unchanged autumn idiom on the strength of the following explanation. 増す guard already exists. |
| C6 (medium), 溶け込む | **resolved** | Title and sugar example no longer imply completeness; concrete social parenthetical retained. |
| C7 (medium), 売り切れる | **resolved** | Goods are grammatical subjects in both examples; Russian passive does not classify Japanese 売り切れる as a passive of 売る. |
| C8 (medium), 湧く | **partially resolved** | Literal «бить ключом» kept and anchored; imperfective «хлестать наружу», idea example and intransitive 沸く glosses accepted. “The «каком-то списке» hedge stays meta but no longer misstates the voice; not re-opened.” No remaining actionable finding filed. |
| C9 (medium), 混じる | **resolved** | Stones are subject of «примешались»; a little bookish but shows mixing. |
| C10 (low), 清掃 | **resolved** | Indoors/streets covered. 掃除 guard covers «уборка». |
| C11 (low), 混ざる | **resolved** | Joining not restricted to a game; 加わる guarded. |
| C12 (low), 湯気 | **resolved** | Invisible ゆけ heading removed; no dangling sentence, ゆげ still taught. |
| C13 (low), 湿る | **resolved** | Sense 2 retains its relationship to physical dampness without mentioning an unseen list. |

The correctness recheck separately checked the edited teaching passages (JMdict IDs include 水蒸気 1371660, 演劇 1176860, 測量 1404590, 深まる 1362660, 溶け込む 1546090, 売り切れる 1473880, 湧く 1606685, 混じる 1603930, 清掃 1378320, 混ざる 1603920, 湿る 1320390). It reports checking Daijisen on the non-obligatory completeness of 溶け込む, indoor 清掃 and the separate ゆけ heading. This is the correctness reviewer's evidence, not a fresh dictionary review by the records worker or the consistency reviewer. Comprehensibility additionally noted a loose reference to the second example at 深夜:23, **not filed** as a wrong meaning. No recheck raised a new actionable finding.

## Final exclusion set

All 150 EN entries (26 nonempty lists, 25 in-batch) remain exact ordered prefixes. Appended entries, in both signed snapshots:

| New card | Appended | Final list in persisted order |
|---|---|---|
| 演劇 | 公演, 芸術, 芸能 | `[劇, 芝居, ドラマ, 舞台, 劇場, 映画館, 公演, 芸術, 芸能]` |
| 溶かす | 溶け込む | `[溶ける, 溶く, 失う, 無くす, 潰す, 無駄, 損, 損害, 溶け込む]` |
| 溶け込む | 加わる | `[溶ける, 溶く, 混合, 合う, 合わせる, 加わる]` |
| 売り切れる | 特売 | `[切れる, 無くなる, 特売]` |
| 売り切れ | 特売 | `[売り切れる, 切れる, 無くなる, 特売]` |
| 満員 | あふれる, 大勢 | `[一杯, 込む, 混雑, ぎっしり, ぎゅうぎゅう, 詰まる, ぱんぱん, 満ちる, 売り切れ, 売り切れる, 人込み, あふれる, 大勢]` |
| 湯気 | もくもく | `[蒸気, 水蒸気, もくもく]` |
| 温帯 | 適度 | `[適度]` |
| 付き合う | 会う, お目に掛かる | `[交際, 付き合い, 交流, 従う, デート, 会う, お目に掛かる]` |
| 深夜 | 徹夜 | `[夜中, 夜, 晩, 徹夜]` |

Fourteen directed additions on ten cards (3+1+1+1+1+2+1+1+2+1), not 15; 164 total RU entries. The historical “Kept (14)” was accurate; “15” in the restart handoff was not. There was no fix-time exclusion change. The consistency reviewer classed all 14 conservative and left necessity **UNVERIFIED**; F2 was withdrawn, not promoted to a required guard.

### Title screens

| Input | Scope | Lines | `OK` | `!!` | Exact segments |
|---|---|---:|---:|---:|---|
| Both saved all-word authoring-lane screens | 30 words on the scratch lane | 327 each | 32 | 295 | 0 |
| Signed candidate | 30 words | 325 | 32 | 293 | 0 |
| Fix-time changed-title screen in dispositions | Eight retitled words | 88 | 17 | 71 | 4, all guarded |
| Signed fix | All 30 words | 296 | 36 | 260 | 4, all guarded |

The new exact segments and the **declaring** cards are: 測定→測量 «измерение», 深まる→増す «усиливаться», 清掃→掃除 «уборка», 混ざる→加わる «присоединяться». Parentheticals are stripped for the comparison. All four declarations already existed in EN; they are not four new RU exclusions. One declaration suffices for a direct symmetric pair, not for a transitive group. The fix changes the displayed wording on existing hit lines as well as the hits themselves: 117 distinct candidate output lines disappear and 88 appear, including retitled renderings. Remaining `!!` are stem-only; consistency sampled those lines rather than independently validating every possible distractor. It checked the coordinator's screen, not a fresh complete linguistic review.

## Final bounded verdicts

- **Correctness CLEAN; scoped coverage CLEAN on HEAD** — the correctness reviewer's 14-word-plus-劇 regression scope, not absolute certification.
- **Consistency on HEAD: CLEAN. Quiz safety on HEAD: CLEAN for the new overlaps.** The necessity of all 14 conservative RU-only guards stays **UNVERIFIED**.
- **Comprehensibility CLEAN** — not a second final coverage verdict. C8 remained **partially resolved**; no actionable finding remained.

## Limits

Initial reviews supply the evidence for unchanged materials. Correctness used live sources, not historical dictionary captures; fresh Gramota requests returned HTTP 429, so it used alternate or previously verified evidence. It did not reopen unchanged declined items or run a generator, validator, app or full quiz audit. Consistency did not reread the changed cards in full, verify the linguistic correctness of new wording, open a dictionary or rebuild the manifest. Comprehensibility did not reread unchanged cards other than クリーニング or re-open rare-spelling tags; it treated the manifest as hashes only. The blind reports and the coordinator's timing records are distinct from this reconciliation.

No link or exclusion regressions were found in the indicated checks. Available-target parity is not identity of EN/RU prose; a manifest match establishes bytes, not learning quality. These are qualified source-content results only. Nothing here clears tag/random fallback, voice, drawing, app imports, device/media/release, ordinary activation or full-translation completion.

## Original recheck reports (verbatim)

These are the three original returns, in delivery order, after normalizing CRLF to LF. The section labels and provenance are not part of the returns.

### Correctness — `gpt-6.1-sol`

Reviewer `f8dfbe0c-bd07-49ff-b12d-6bb92e7a61e5`; SHA-256 of the saved report before LF normalization: `0c5e9d7190d394296fc78b88b4fe899ff98b34622da905ddd77104ae871fcf70`.

Snapshot: HEAD c972b6793d49df2da0e4b62ba2636114e53a0f62; parent bbe4e485115525a1f4bd661960486449dbe4570b. HEAD verified; git status --porcelain empty at start and immediately before writing this report. Frozen EN HEAD verified: 6af98cb717755690a9ca793e5454a96ebd7a8f9f.

Scope: Full RU and frozen EN reads of words/{水蒸気,演劇,測量,深まる,溶け込む,売り切れる,湧く,混じる,清掃,混ざる,湯気,湿る,深夜,混ぜる}.md and kanji/劇.md. Reviewed every fix passage, original correctness report, supplied dispositions and manifest delta. Model identity not independently verifiable.
Scope: Primary JMdict checked anew: https://www.edrdg.org/pub/Nihongo/JMdict_e.gz (IDs below). KANJIDIC2 confirms 劇: grade 6, 15 strokes, classical radical 18, on ゲキ: https://www.edrdg.org/kanjidic/kanjidic2.xml.gz .

Verdicts: Correctness CLEAN; scoped coverage CLEAN on HEAD. C1/C2 resolved; no new actionable defect established. CLEAN is bounded to this recheck, not exhaustive certification of the repository.

Reconciliation: C1 — RESOLVED, words/湧く.md:50. «Кипеть» и «нагреваться» correctly describe intransitive 沸く (JMdict 1606680, sense 1: “to grow hot; to boil”).
Reconciliation: C2 — RESOLVED, words/深夜.md:21,23. «Глубокой ночью» restores “late-night” (JMdict 1362810). Line 23 allows contextual attributive/adverbial rendering; it does not redefine 深夜 as generic 夜. Lateness remains explicit at :16–18,21 and the broader 夜 contrast at :35.
Reconciliation: Optional 湧く aspect note — RESOLVED, :4,12: imperfective «хлестать наружу» preserves the outflow sense.
Reconciliation: Optional 混ぜる terminology note — RESOLVED, :38: «постфиксом -ся» is accurate; transitivity teaching remains. Evidence: https://ru.wiktionary.org/wiki/-ся .

New text: words/水蒸気.md:4,12 — CLEAN. «Водяной пар» covers both EN glosses (JMdict 1371660). Gas/droplet distinction remains at :31. Russian пар has scientific/everyday uses: https://ru.wiktionary.org/wiki/пар , пар I, senses 1–3.
New text: words/演劇.md:4,12 — CLEAN. Art and dramatic production are both retained, matching EN :16 and JMdict 1176860 (“drama; theatre; play”). No venue sense added.
New text: words/測量.md:4,12,42–45 — CLEAN. Both EN glosses retained (JMdict 1404590). Deleted “look around” contrast concerns English polysemy; its Japanese measurement requirement survives at :16–24,42, and :43–44 still reject a land-only restriction.
New text: words/深まる.md:4,12 — CLEAN. «Углубляться; усиливаться» matches EN “deepen; intensify” and JMdict 1362660; seasonal and relationship uses remain.
New text: words/溶け込む.md:4,12,20 — CLEAN. Physical/social/visual uses remain (JMdict 1546090, senses 1–2). Sugar example is faithful. Daijisen sense 1 permits liquid or gas without mandatory total dissolution, supporting removal of «полностью»: https://www.weblio.jp/content/溶け込む .
New text: words/売り切れる.md:20–21 — CLEAN. Goods remain subjects; Russian passive «был распродан» does not misclassify the Japanese verb. «Пока они не разошлись» means before sellout (JMdict 1473880); разойтись sense 7 supports this: https://ru.wiktionary.org/wiki/разойтись .
New text: words/湧く.md:4,12,21,50 — CLEAN. Literal outflow/figurative arising retained (JMdict 1606685, senses 1,3); «У меня родилась хорошая мысль» is faithful. Corrected 沸く warning and overlap with 浮かぶ remain.
New text: words/混じる.md:18 — CLEAN. «К песку примешались мелкие камешки» grammatically preserves the past mixed-in result and に/が roles (JMdict 1603930); Russian perfective is acceptable here.
New text: words/清掃.md:4,12 — CLEAN. Indoor/outdoor cleaning supported; garbage-collection sense remains (JMdict 1378320). Daijisen gives 室内を清掃する: https://www.weblio.jp/content/清掃 .
New text: words/混ざる.md:4,12 — CLEAN. Mixing, mingling and joining people all remain (EN title; JMdict 1603920). «Присоединяться (к другим)» avoids falsely limiting joining to a game.
New text: words/湯気.md:deleted old :44 — CLEAN. External-heading warning removed; ゆげ and voicing remain explicit at :3,12,20,26–28. Daijisen separates ゆけ (bath-related faintness) from this steam entry: https://www.weblio.jp/content/湯気 . No target-entry fact lost.
New text: words/湿る.md:43 — CLEAN. Source-list provenance removed, not a sense. Physical dampness/figurative loss of vigor and the latter's しめる restriction survive (JMdict 1320390; :29,37).
New text: words/深夜.md:21,23 — CLEAN; see C2 reconciliation.
New text: words/混ぜる.md:38 — CLEAN; only Russian morphological terminology changes, not the retained mixing/transitivity rule.
New text: kanji/劇.md:36 — CLEAN. Reading えんげき and gloss now exactly match the new 演劇 title; link target unchanged.
New text: Manifest changes are limited to contentVersion and 15 changed-card hashes; every updated SHA-256 matches the current file bytes. No non-title metadata, links or Japanese examples changed in the fix.

Findings: None new or unresolved. Counts: 0 critical, 0 high, 0 medium, 0 low. All four original items reconciled above; no optional note remains outstanding.

Limits: Original report unchanged; other reviewers' reports, prohibited batch/tracking records and author scratch material unread. Dispositions not accepted on authority; unchanged declined items not reopened. No generator, validator, app or full quiz audit run. No repository/worktree writes or Python bytecode. Live dictionaries, not historical captures; fresh Gramota requests returned 429, so alternate entries/prior verified evidence used. Only this new report written.

### Consistency — `claude-sonnet-5.5`

Reviewer `99dd73a9-bf30-4991-870c-6ced97d29aca`; SHA-256 of the saved report before LF normalization: `39fd35d841968d86bc50c560473c17252813d89b0afb850ac0c03f2eb993181a`.

Snapshot: HEAD c972b6793d49df2da0e4b62ba2636114e53a0f62, parent bbe4e485. `git status --porcelain` was empty at the start and is empty at the time of writing. `tools/__pycache__` was removed after `validate.py`. The validator printed 0 error(s).

Scope: I read the whole fix diff (`git diff bbe4e485 c972b679`: 14 cards, kanji/劇.md, manifest.json), the dispositions file and the coordinator screen. I did not re-read the 14 cards in full; I checked them by diff context, plus full text of 測量:37-end and 湯気:39-end. Mechanical checks (front matter, titles, manifest hashes, whole-repo grep for superseded titles, `quiz_exclusions` lookup) were run by script. I could not verify which model produced the edits.

Verdicts:
- Consistency on HEAD: CLEAN.
- Quiz safety on HEAD: CLEAN for the new overlaps. Necessity of the 14 RU-only guards stays UNVERIFIED, as in the original report (no live dictionary was consulted).

Reconciliation:
- F1 溶け込む «полностью»: RESOLVED. The title and H1 are now «растворяться в чём-либо; вливаться (в коллектив, обстановку)» and the example reads «Сахар растворился в воде». The title is still long, which is cosmetic.
- F2 温帯→適度 guard: WITHDRAWN. I accept the disposition. Russian «умеренный» translates both "temperate" and "moderate", so the guard answers an overlap that the Russian titles introduce. It is harmless to keep.
- F3 水蒸気: RESOLVED. The title and H1 are «водяной пар», with no «горячий пар».
- F4 湧く kanji-card note: OPTIONAL, informational, as dispositioned. The kanji metadata is unchanged.
- F4 清掃 narrower than EN: RESOLVED. The title is «очистка; уборка (помещений, улиц)». «очистка» stays first and covers the broader sense.

New text (regression notes):
- Checked by script on all 14 cards: the H1 gloss equals `title`. Every front-matter line other than `title` is identical to the parent. Only 8 cards changed `title` (水蒸気, 演劇, 測量, 深まる, 溶け込む, 湧く, 清掃, 混ざる); the other 6 changed body text only. The titles match the 8 given in the brief verbatim.
- 水蒸気 «водяной пар»: no exact segment match with 蒸気 «пар», 湯気 «клубы пара (над горячим)» or 湯 «горячая вода». 水蒸気 already lists 蒸気, and 湯気 lists 水蒸気.
- 測量–測定 «измерение»: the guard is carried by 測定 (`quiz_exclusions` contains 測量). 測量 itself does not list 測定. The RU `docs/content-format-reference.md:98` defines `quiz_exclusions` as «прямые симметричные пары», so the one-sided entry excludes the pair.
- 深まる–増す «усиливаться»: the guard is carried by 深まる (it lists 増す). 増す is «увеличиваться; усиливаться». Same contract.
- 清掃–掃除 «уборка»: the guard is carried by 清掃 (it lists 掃除). 掃除 is «уборка». Same contract.
- 混ざる–加わる «присоединяться»: the guard is carried by 混ざる (it lists 加わる). 加わる is «присоединяться; добавляться». Same contract.
- 溶け込む «растворяться в чём-либо»: this is not an exact segment of 溶ける «таять; растворяться» or 溶かす «плавить; растворять». Both pairs are guarded anyway: 溶け込む lists 溶ける, and 溶かす lists 溶け込む.
- `!!` stem-only lines: sampled and judged low-risk. 演劇 vs 人工/衛星/運河 (искус-) and 供給/決定 (поста-); 測量 vs 地/土地/地域/田舎 (местн-) and 単位 (измер-); 深まる vs 努力/協力/ド (усили-); 溶け込む vs 同僚/集団 (колле-) and 酸性 (раств-); 湧く vs the many «чувств-» words; 清掃 vs the «помещ-» words and 雑巾 (уборк-); 混ざる vs つまり (други-). These are unrelated senses or ordinary vocabulary overlap, and none is a real confusion risk. 演劇 vs 幕/能 (театр) is topical only, as already noted.
- Superseded titles: the whole-repo grep over `.md`, `.json` and `.txt` files found none of «горячий пар», «полностью растворяться», «крепнуть (о чувстве, связи)», «уборка территории», «принимать участие (в игре)», «хлынуть», «театр; драматическое искусство», «топографическая съёмка» or «обмер (местности». `kanji/劇.md:36` now quotes «театральное искусство; драматическая постановка», the new 演劇 title.
- manifest.json: 15 entries changed (14 cards plus kanji/劇.md), plus `contentVersion`. All 15 hashes match their file bytes, and no other entry changed.
- Link and footer integrity: `validate.py` reports 0 errors. The 測量 deletion (the 「осмотреться」 sentence) leaves the paragraph coherent, with the 寸法 link intact and the footer unchanged. The 湯気 deletion (the ゆけ sentence) leaves the ending of the card coherent and the footer lines unchanged. The 湿る footer line was reworded only. The 売り切れる, 湧く, 深夜 and 混じる example and remark edits do not touch links.

Findings: none.

Limits:
- I did not open a dictionary. I treated exact-segment and stem screens as lexical evidence, not as a necessity verdict.
- I did not re-verify linguistic correctness of the new Russian wording; that belongs to the correctness facet.
- I did not run `build_manifest.py`. The hash check was a read-only SHA-256 comparison.

### Comprehensibility — `grok-4.7`

Reviewer `20c8cfac-fabd-488d-9861-f1b1f56f9bfd`; SHA-256 of the saved report before LF normalization: `9885a69dc03c4d437d93fa2c6ec68d9c758a95de632c56673c26302c30296f22`.

Snapshot: c972b6793d49df2da0e4b62ba2636114e53a0f62; parent bbe4e485115525a1f4bd661960486449dbe4570b; uncommitted changes? none at start and at write (`git status --porcelain` empty; HEAD matches).
Scope: comprehensibility recheck of fix 1. Read in full: words/水蒸気.md, 演劇.md, 測量.md, 深まる.md, 溶け込む.md, 売り切れる.md, 湧く.md, 混じる.md, 清掃.md, 混ざる.md, 湯気.md, 湿る.md, 深夜.md, 混ぜる.md, クリーニング.md (unchanged; C4), kanji/劇.md. Compared titles/exclusions of 測定, 増す, 掃除, 加わる, 浮かぶ, 沸く, 芝居, 公演. Screen file confirms guarded segment overlaps only (測定, 増す, 掃除, 加わる); stem hits not treated as findings. Model: not verifiable from this session.
Verdicts: comprehensibility CLEAN.
Reconciliation:
C1 resolved. Title/H1 «водяной пар» drops «горячий пар». The shades paragraph still assigns the visible cloud to 湯気, so the quiz label no longer stores that sense.
C2 resolved. Title now includes «драматическая постановка». Declined «спектакль» examples are natural Russian and are equated on the card («смотреть спектакль»); 芝居 and 公演 stay in quiz_exclusions. Not re-opened.
C3 resolved. «съёмка местности; измерение» restores general measurement and is no longer land-only. Deleted «осмотреться» leaves a coherent shades paragraph; the questionnaire warning remains above it. Shared «измерение» is in 測定's exclusions.
C4 withdrawn. Decline holds on the card: the first gloss is already «чистка»; the opening sentence names химчистка before the example; line 24 blocks a dry-cleaning-only label. Latin cleaning is glossed in the same sentence as the etymon. The title/example skew is taught, not a contradiction.
C5 resolved. «углубляться; усиливаться» covers the season and the feeling. The declined idiom is bridged by the next sentence (the season advances, not a pit) and by «стало глубже». Shared «усиливаться» is excluded against 増す.
C6 resolved. Title drops «полностью»; «Сахар растворился в воде.» matches the sentence. The social parenthetical is concrete.
C7 resolved. «был распродан» and «они не разошлись» keep the goods as subject, matching the intransitive note and the existing title «быть распроданным». The note still says the Japanese verb is not a passive of 売る.
C8 partially resolved. «бить ключом» kept and anchored by the spring example plus imperfective «хлестать наружу». :21 «У меня родилась хорошая мысль.» ties to «зарождаться» and no longer copies 浮かぶ. :50 now says «кипеть» и «нагреваться», matching 沸く. The «каком-то списке» hedge stays meta but no longer misstates the voice; not re-opened.
C9 resolved. «К песку примешались мелкие камешки.» shows mixing, stones as subject.
C10 resolved. «очистка; уборка (помещений, улиц)» covers indoors and streets. «уборка» overlap with 掃除 is excluded.
C11 resolved. «(в игре)» is gone; «присоединяться (к другим)» matches the people example. Overlap with 加わる is excluded.
C12 resolved. The learner-invisible ゆけ sentence is gone. The shades paragraph ends on the 湯気/蒸気 warning; the reading section already gives ゆげ.
C13 resolved. Footer no longer names an unseen list: «значение 2 дополняет физическое значение «сырость».»
New text:
水蒸気: single gloss is clear and matches both examples. No regression.
演劇: title/H1 match kanji/劇.md:36. Examples still say «спектакль»; the card teaches that phrase, so the declined rewrite is not a hole. No regression.
測量: shades section starts cleanly on spatial data, then warns that «измерение» is not land-only. Coherent.
深まる: title is a usable quiz label. The idiom does not literally say «углубляться», but the following sentence supplies the season reading. No regression.
溶け込む: title is long but two learnable glosses. The sugar example no longer overstates completeness.
売り切れる: passive Russian in :20 matches the title; :21 is intransitive. Both keep the goods as subject. No regression.
湧く: three glosses are concrete. «хлестать наружу» is imperfective and fits gushing water. :50–52 now name the right 沸く glosses; the list hedge is skippable.
混じる: «примешались» is a little bookish but shows the mix. No regression.
清掃: parenthetical distinguishes the place scope without hiding indoor cleanup.
混ざる: three glosses; the last two overlap slightly but the game narrowing is gone. Clear.
湯気: deletion does not leave a dangling sentence.
湿る: footer is learner-readable.
深夜: :21 «глубокой ночью» is precise. :23 offers «ночной» or «глубокой ночью», «как во втором примере», though the example shows only the latter. Loose pointer, not a wrong meaning; not filed.
混ぜる: «постфиксом -ся» is a grammar term, but the pair «смешивать»/«смешиваться» makes the point. Not a regression.
kanji/劇.md:36: list gloss matches the new 演劇 title and does not fight the kanji card's own «драма; пьеса».
Findings: none
Limits: unchanged cards other than クリーニング were not re-read. Rare-spelling tags not re-opened. manifest.json is hashes only. No native-speaker or learning-effectiveness claim.
