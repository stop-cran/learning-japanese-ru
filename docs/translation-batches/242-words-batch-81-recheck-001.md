# Batch 242 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `8cada6dfbe469d4905e64c9ba8e8e2377f1d0b6f` | `06db481b65bf56830aa81d275089b6c4af319389` | Initial review snapshot: the signed candidate, on `origin/full-ru-242-words-81`. |
| `872649eb119a463b2268af820899c43d399ec330` | `e4167b2ab9eb24f8e7dc896d33e8c3e927ec8db7` | Fix 1. It covers correctness F1 to F3 and comprehensibility C1, C2, C4, C5, C6, C8, C11, C12, C17, C18 and C19 (C1, C8, C11, C17 and C19 in modified form; C2, C5, C6 and C12 partially). It retitles 広々, 職人, 生き生き, 膨らむ and 実力 and aligns the kanji/生.md:47 list gloss. It adds or removes no exclusion and no link. Signed; on `origin/full-ru-242-words-81`. |
| `66e49ae6d539c9cab1467a4803ae7b7fa50636f9` | `b3429e5e3ab292234fffce3525ac190f7fa2d536` | Fix 2: the one-sided exclusion 生き生き→明るい. Signed. |
| `5e64cd7e5e1971f0b5b64e01c3add788851b1fa0` | `8e7a9940517ef1122bae358cba7adfc2e17e04b6` | Fix 3 (final candidate): correctness recheck R1, one sentence at 実力:37. Signed; on `origin/full-ru-242-words-81`. |

Each fix regenerated `manifest.json`; every snapshot records 5,379 entries (5,374 `files` + 3 images + 2 scenes).
`contentVersion` is `bffc2456054c4cd0` at the candidate, `205b99199a06a27c` after fix 1, `5fdde160b3d4230c` after fix 2
and `1bf36d1e1085a758` after fix 3. The intake was not refreshed; it still records the candidate's payload hashes. The
commit messages read:
- fix 1: "B242 words batch 81: review fixes / Correctness F1 (耕す), F2 (功績), F3 (職人 citation); comprehensibility C1,
  C2, C4, C5, C6, C8, C11, C12, C17, C18, C19 (accepted or partial). Retitled 広々, 職人, 生き生き, 膨らむ, 実力; aligned
  kanji/生.md list gloss.";
- fix 2: "B242 words batch 81: guard 生き生き against 明るい / The retitle adds «ярко», sharing stems with 明るい «светлый;
  яркий; жизнерадостный» alongside «полный жизни»; add a one-sided RU exclusion.";
- fix 3: "Batch 242 fix 3: correctness recheck R1 (実力 scoped coverage)".

Fix 1:
- `耕す` (lines 43–44 and the old 50–51; correctness F1, comprehensibility C6 partial): the two sentences claiming a
  figurative Russian «возделывать» become «Не считайте, что любое переносное «взращивание» — способностей или отношений —
  можно передать через 耕す.»; the N2-coverage paragraph is deleted; the test-guard ids at :49 stay.
- `功績` (line 45; correctness F2): «…（きふ）; 功績 называет заслугу или ценимый результат, а не само действие передачи
  денег.» instead of the categorical «功績 не имеет отношения к передаче денег.»
- `職人` (lines 4, 12, 20 and 51; correctness F3, comprehensibility C8 modified): title and H1 «ремесленник; мастер
  ремесла» instead of «ремесленник; мастер ручного труда»; example «Он мастер по изделиям из кожи.» instead of «Он
  ремесленник по коже.»; added «Русское значение: [Викисловарь, ремесленник](https://ru.wiktionary.org/wiki/ремесленник),
  значение 2 (перен., неодобр.).»
- `広々` (lines 4, 12, 22 and 47; comprehensibility C1 modified): title and H1 «просторно; раздольно» instead of
  «раздольный; дающий ощущение простора»; «В этом парке просторно.» instead of «…раздольно.»; «не просторно» instead of
  «непросторный».
- `膨大` (lines 36–37; comprehensibility C2 partial): «Русские слова вроде «обширный» могут подойти к обоим, но японские
  слова не взаимозаменяемы без ограничений.»; the title «необъятный» is kept.
- `学力` and `学術` (line 31 each; comprehensibility C4): 学力 now begins «Здесь речь о знаниях и способностях к учёбе, а не
  о деньгах, которые выдают учащемуся.»; 学術's last sentence reads «Денежную поддержку учащемуся называет
  [奨学金](奨学金.md)（しょうがくきん）, а не 学術.»
- `羨ましい` (line 22; comprehensibility C5 partial): «Этому действительно можно позавидовать.» instead of «Это
  действительно завидная история.»; the partner sentence stays.
- `背負う` (line 21; comprehensibility C11 modified, also the correctness optional): «Он несёт на своих плечах заботу о
  жизни семьи.» instead of «Он взвалил на себя ответственность за жизнь семьи.»
- `実績` (lines 17–18; comprehensibility C12 partial): «…результаты в работе, бизнесе или другой деятельности, в том числе
  послужной список человека.»; the title is kept.
- `生き生き` (lines 4, 12 and 21–22; comprehensibility C17 modified): title and H1 «полный жизни; оживлённо; ярко»
  instead of «полный жизни; с живостью»; examples «Дети оживлённо играют.» and «Этот роман ярко описывает мой родной
  край.»
- `kanji/生.md` (line 47; C17): the list gloss after the 生き生き link reads «живо; ярко; энергично» instead of «живо,
  энергично; с живостью» (EN 46 "lively; vividly; energetically"); link, target and line unchanged.
- `膨らむ` (lines 4 and 12; comprehensibility C18): title and H1 «надуваться; нарастать» instead of «надуваться;
  увеличиваться в объёме».
- `実力` (lines 4, 12 and 37; comprehensibility C19 modified): title and H1 «реальные способности; применение силы» instead
  of «реальные способности; силовое воздействие»; the «эффективность» and «оружие» sentences at :37 become «Во втором
  значении речь о принуждении, в том числе вооружённом, а не о руках или мастерстве — их называет [腕](腕.md).»

Fix 2: `生き生き.md:9` adds `明るい` at the end of `quiz_exclusions`. The new «ярко» and «полный жизни» overlap 明るい
«светлый; яркий; жизнерадостный» in meaning.

Fix 3: `実力.md:37` adds «Перевод efficiency («эффективность») в англоязычном словаре JMdict относится к значению
компетентности и не делает 実力 универсальным обозначением эффективности процесса.» The reviewer's proposed wording is kept
for the boundary; the source clause is the coordinator's.

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Comprehensibility C2's title point: the dispositions kept «необъятный» ("renders "vast"") and named the proposed
  «непомерный» an exact title segment of 極端. At recheck the reviewer withdrew the point, agreeing the collision is real
  and correcting the owner: «непомерный» is a segment of 甚だしい «крайний (о степени); непомерный», not of 極端.
- C5's partner sentence stays: EN teaches it, and «ревновать» also has an envy sense («ревновать к чужим успехам»); the
  reviewer withdrew that point.
- C6's test-guard ids at 耕す:49 stay as a house convention; the reviewer accepted them as a footer convention.
- C12: 実績's title stays (a person's track record is a real sense); the reviewer's partial accept is recorded.
- C1: «раздольно» stays beside «просторно»; the reviewer did not accept that it fits a room but required no further edit.
- C3 (おかけください), C9 (腰掛け), C10 (腰掛ける), C13 (活躍 «заметная роль», guarded by 役割/役), C14 (膨らます
  «раздувать»), C15 (能率 «выработка», output per unit of time) and C16 (押さえる:48, EN-faithful cross-reference) were
  withdrawn by the coordinator with reasons and withdrawn by the reviewer at recheck.
- C7 (肘's «метаданные» remark) was withdrawn and deferred to the corpus-wide «метаданные» follow-up (EN-faithful; about
  110 published RU cards use it); the reviewer withdrew it "with the published «метаданные» pattern".
- The correctness optional on 背負う:21 established no defect; fix 1 rewrote the example under C11, and the correctness
  recheck kept the point OPTIONAL, "partially addressed". The UNVERIFIED 布く/藉く and 展げる labels are unchanged.
- Consistency: F1's classification needed no change (習字→清書 kept: "one-sided declarations are harmless and the pair
  would otherwise be judged only by stem"); P1 (活躍) was left to comprehensibility and withdrawn as a consistency matter
  at recheck; O1 (広める:35, as EN) needed no change and stays optional; O2 (脱線/戻る plain, as EN) was withdrawn at
  recheck; O3 (職人's RU-only paragraph) was kept, cited per correctness F3, and resolved at recheck.
- The comprehensibility optionals (肯定 «утвердительное суждение», 膨らます:49, Мы/свой, 広げる segments, 育児 «уход»,
  習字 vs 書道, 功績 «вклад») needed no change and remain non-blocking.

Post-fix screen: before fix 2 the coordinator screened the five retitled words for exact segments and stem leads and
found no exact-segment hit; its stem-level near-hits were listed in the consistency recheck brief. A saved rerun at
`66e49ae` against the RU primary (`b242-postfix-screen.txt`, 59 lines), generated after the first recheck briefs were
written, finds no exact-segment hit, 7 already guarded stem leads (広々–広い, 職人–名人, 生き生き–ぴんぴん/活気/賑やか,
膨らむ–膨らます, 実力–能力) and 52 unguarded stem-only leads, left to the consistency recheck. That recheck judged them
guarded or needing no guard (below).

Net change from the candidate:
- titles and H1s of 広々, 職人, 生き生き, 膨らむ and 実力;
- example translations in 広々, 生き生き (two), 羨ましい, 職人 and 背負う;
- prose in 耕す (and the deletion of its N2-coverage paragraph), 功績, 職人 (citation), 広々, 膨大, 学力, 学術, 実績 and
  実力 (two changes), and the list gloss at kanji/生.md:47;
- one exclusion added (生き生き→明るい), none removed;
- no link added, removed or retargeted (the 職人:51 Wiktionary URL is an external citation).

No Japanese example sentence, sourced reading, kanji card front matter or EN exclusion changed. The content diff
`8cada6d..5e64cd7 -- kanji words` is 14 files, 29 lines added and 32 removed (13 word files, 28 and 31); with
`manifest.json` the three fixes change 15 files, 44 lines added and 47 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the initial reports state "Model identity not independently verifiable.", "Model: not verifiable from inside this
session." and "Model not verifiable.", and the comprehensibility recheck repeats "model not verifiable".

The rechecks ran serially, one reviewer at a time, in two rounds. In round 1 the correctness reviewer rechecked fixes 1
and 2 together (diff `8cada6d..66e49ae`: 13 word cards, kanji/生.md:47 and `manifest.json`) and raised R1. After fix 3,
round 2 ran correctness on fix 3 alone (`66e49ae..5e64cd7`: words/実力.md:37 and `manifest.json`), then consistency, then
comprehensibility, the last two each on the full diff `8cada6d..5e64cd7`. The briefs sent were the correctness round-1
brief and then one round-2 brief per reviewer. This ordering rests on the coordinator's session records; the recheck
sections do not record times. No round-2 recheck raised a new finding, so there was no fix 4.

Each reviewer appended its recheck to its own report file: correctness under `## Recheck (66e49ae)` and
`## Recheck (5e64cd7)`, consistency and comprehensibility under `## Recheck (5e64cd7)`.

No recheck ran a generator. The correctness reviewer ran `tools/validate.py` at `66e49ae` ("Validator: 0 error(s), exit 0",
and no bytecode cache created) and recorded "validator not rerun for this one-sentence fix" at `5e64cd7`; the consistency
reviewer ran `tools/validate.py` (0 errors), rebuilt the manifest in memory only ("In-memory `build_manifest()` equals the
committed manifest.") and removed the untracked Python bytecode cache it created ("nothing written in any repository");
the comprehensibility reviewer records "No generator run." and no validator run. The correctness sections record HEAD
`66e49ae6d539c9cab1467a4803ae7b7fa50636f9` with a "clean RU checkout; fix ancestry verified" and HEAD
`5e64cd7e5e1971f0b5b64e01c3add788851b1fa0` with a "clean RU checkout; parent 66e49ae verified"; the consistency section
records HEAD `5e64cd7e5e1971f0b5b64e01c3add788851b1fa0` and an empty `git status --porcelain`; the comprehensibility
section records HEAD `5e64cd7e5e1971f0b5b64e01c3add788851b1fa0` and "porcelain empty". The recheck records include no
separate coordinator status check after the rechecks; when these records were drafted, a read-only check showed the RU
checkout on `full-ru-242-words-81` at HEAD `5e64cd7e5e1971f0b5b64e01c3add788851b1fa0` with `git status --porcelain
--ignored` printing nothing.

### Round 1 (`66e49ae`)

| Facet | Scope and result |
|---|---|
| Correctness | HEAD `66e49ae`, "clean RU checkout; fix ancestry verified"; "all changes in 13 word cards and kanji/生.md:47 against EN 6af98cb; actual diff/manifest inspected." "F1 RESOLVED: the hedged figurative-cultivation warning removes the unsupported Russian lexical claim and preserves EN's “not every use” boundary." "F2 RESOLVED: merit/result is distinguished from the donation action without excluding meritorious donations." "F3 RESOLVED: 職人:51 now cites the actual Russian entry … sense 2; reread and confirmed." "背負う:21 remains OPTIONAL, partially addressed". Raised R1 (P3; scoped coverage; `words/実力.md:37`): "EN words/実力.md:39's competence-versus-process-efficiency warning is lost. … Both primary senses remain correct." Evidence: JMdict 1321530 sense 1 (jisho.org); Daijisen senses 1–2 (weblio); "Confidence high for the omission; limited learning impact." "Other rewrites are at least as accurate" (広々, 膨大, 学力/学術, 羨ましい, 耕す, 職人, 実績, 生き生き with kanji/生.md:47, 膨らむ, 実力). "Japanese examples/kana unchanged." Correctness **CLEAN** for the rechecked changes, with the inherited spelling-label exceptions UNVERIFIED; scoped coverage **NEEDS FIX** (R1). |

### Round 2 (`5e64cd7`)

| Facet | Scope and result |
|---|---|
| Correctness | HEAD `5e64cd7`, "clean RU checkout; parent 66e49ae verified"; "actual fix-3 diff and words/実力.md:37 against frozen EN:39; manifest delta inspected." "R1 RESOLVED. The restored sentence explicitly preserves the competence-versus-process-efficiency boundary. Its source clause is accurate". "No correctness or scoped-coverage regression established." "F1–F3 remain resolved; 背負う precision remains optional." Correctness **CLEAN** for reviewed changes and scoped coverage **CLEAN**. Limits: "inherited 布く/藉く and 展げる spelling-label checks remain UNVERIFIED. No expanded quiz/native audit; validator not rerun for this one-sentence fix." |
| Consistency | HEAD `5e64cd7`, status empty; "Fix 3 … touches only `words/実力.md` (one body line, :37) and `manifest.json`; no title, link or exclusion change." `validate.py` 0 errors; in-memory manifest equal. Title = H1 for the five retitled cards; old titles absent except «силовое воздействие» as the gloss of 実力行使 at 実力:23, "intentional and consistent with the new title". "Fix 2 exclusion: 生き生き→明るい is well formed … so the guard is justified." Stem near-hits guarded (広々–広い, 職人–名人, 生き生き–ぴんぴん/活気/賑やか/明るい, 膨らむ–膨らます, 実力–能力) or needing no guard (陽気, 真っ赤, 神様, 工場, 用/適用/体力/軍隊/武器). Optionals: P1 withdrawn as a consistency matter; O1 optional and unchanged; O2 withdrawn; O3 resolved. Consistency **CLEAN**, navigation restorations **CLEAN** (生.md:47 "matching the new 生き生き title segments"), quiz safety **CLEAN** and cross-file integration **CLEAN**. Limits: "The semantic screen is a judgment, not exhaustive. JMdict was not consulted online. b246 was not fully scanned". |
| Comprehensibility | HEAD `5e64cd7`, "porcelain empty. Changed passages re-read. No generator run." C4, C6, C8, C11 and C17 to C19 **resolved** (C19 "including fix 3": ":37 now shows «эффективность» and limits it to competence, so the “gloss never shown” problem is gone"); C1, C5 and C12 **partial**, not reopened; C2, C3, C7, C9, C10 and C13 to C16 **withdrawn**. "Correctness edits: 功績:45 is clearer and still points at 寄付. 職人 and 耕す add no regression." Comprehensibility **CLEAN** and scoped coverage **CLEAN**; "No open defect maintained." Limits: "布く/藉く not re-audited; title screen not re-run; model not verifiable." |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 耕す:43–44 claims a figurative Russian «возделывать» (P2) | **Resolved** | `耕す.md:43–44`; Kuznetsov ВОЗДЕЛАТЬ and КУЛЬТИВИРОВАТЬ via gramota.ru; Ozhegov/Shvedova. |
| Correctness F2: 功績:44–45 categorically excludes money (P2) | **Resolved** | `功績.md:45`; JMdict 1275070 sense 1; 1920 Cabinet record, National Archives of Japan. |
| Correctness F3: 職人's Russian note lacks Russian support (P3) | **Resolved** | `職人.md:51`; ru.wiktionary «ремесленник», sense 2. |
| Correctness optional: 背負う:21 livelihood sense | **Optional**; partially addressed by C11 | `背負う.md:21`; "livelihood/support could still be explicit". |
| Correctness limits: 布く/藉く (敷く:35) and 展げる (広げる:31–32) labels | **UNVERIFIED**; not defects, unchanged | Raw JMdict annotations unavailable; EN wording inherited. |
| Correctness recheck R1: 実力:37 loses EN:39's competence-versus-process-efficiency boundary (P3; scoped coverage) | **Resolved** by fix 3 | `実力.md:37`; JMdict 1321530 sense 1; Daijisen senses 1–2. |
| Consistency F1: classification of the RU-added exclusions | **Recorded**; all seven kept | See the final exclusion set. |
| Consistency F2 to F9 | **Recorded**; no action | Checks passed; no defect. |
| Consistency P1: 活躍 «заметная роль» narrower than EN | **Withdrawn** as a consistency matter at recheck | Guarded by 役割/役; see comprehensibility C13. |
| Consistency O1: 広める:35 mentions 広げる before its title senses | **Optional**; unchanged | Same as EN 広める:36. |
| Consistency O2: 脱線's 戻る plain | **Withdrawn** at recheck | Mirrors EN's unlinked mention. |
| Consistency O3: 職人's RU-only paragraph | **Resolved** at recheck | Kept; cited at `職人.md:51`. |
| Comprehensibility C1: 広々 title and examples (high) | **Partially resolved**; not reopened | `広々.md:4,12,22,47`; reviewer does not accept «раздольно» for a room but requires no edit. |
| Comprehensibility C2: 膨大 «необъятный» and «в переводе» (medium) | Title point **withdrawn**; :36–37 **resolved** | `膨大.md:36–37`; «непомерный» is a segment of 甚だしい (the dispositions had named 極端). |
| Comprehensibility C3: おかけください's comma (medium) | **Withdrawn** | Segments split on «;»; one seating formula. |
| Comprehensibility C4: 学力/学術 «учёность» (medium) | **Resolved** | `学力.md:31`, `学術.md:31`. |
| Comprehensibility C5: 羨ましい:22 and the partner sentence (medium) | **Partially resolved**; partner point withdrawn | `羨ましい.md:22`; «ревновать» overlaps envy. |
| Comprehensibility C6: 耕す «возделывать», N2 paragraph, test-guard note (medium) | **Resolved** (test-guard ids accepted as a footer convention) | `耕す.md:43–44`; N2 paragraph deleted. |
| Comprehensibility C7: 肘:41–42 «метаданные» (low) | **Withdrawn**; corpus-wide follow-up | EN-faithful; published pattern. |
| Comprehensibility C8: 職人 title and :20 (high) | **Resolved** (modified wording) | `職人.md:4,12,20`. |
| Comprehensibility C9, C10: 腰掛け and 腰掛ける titles | **Withdrawn** | EN "seat; bench"; 腰掛ける:49 already denies "only briefly". |
| Comprehensibility C11: 背負う:21 drops ている (medium) | **Resolved** (modified wording) | `背負う.md:21`. |
| Comprehensibility C12: 実績 «послужной список» (high) | **Partially resolved**; partial accept | `実績.md:17–18`; title kept. |
| Comprehensibility C13 to C16: 活躍, 膨らます, 能率, 押さえる | **Withdrawn** | Guarded, ordinary or EN-faithful, as the dispositions and recheck state. |
| Comprehensibility C17: 生き生き «с живостью» (medium) | **Resolved** (modified) | `生き生き.md:4,12,21–22`; `kanji/生.md:47`; 明るい guarded by fix 2. |
| Comprehensibility C18: 膨らむ title (medium) | **Resolved** | `膨らむ.md:4,12`. |
| Comprehensibility C19: 実力 title and :37 (medium) | **Resolved**, including fix 3 | `実力.md:4,12,37`. |
| Comprehensibility optionals | **Optional**; no change, non-blocking | As listed above. |

Cross-batch note: links to absent targets stay plain. Sixteen EN link occurrences in this batch's new cards, to 13
targets, are absent from RU: words 敷地, 活力, 児童, 手首, 工員, 憎む and 恨む, and kanji 腰, 線, 績, 肯, 肌 and 耕. The
other written kanji without an RU kanji card, 功, 敷, 率, 羨, 肘, 脱, 膨 and 躍, have none in EN either. There is no
RU-only link. The link held from Batch 241, 広める:35 → 広げる, was applied by the coordinator's candidate script after
that batch's publication; no fix changed a navigation link, and the only navigation-file change is the kanji/生.md:47
gloss. No B242 path quotes a title retitled by the Batch 241 fix `9cf1600` or the Batch 240 fix `3544d75`; the only
mentions are `quiz_exclusions` entries and the 広げる:39 contrast, which agrees with the published 広める title. The
consistency recheck's scan of the B243 to B245 draft lanes found only those lanes' pre-fix scratch copies of B242 cards
(実力, 生き生き) and 真っ赤, which are rebuilt from the published text; its B246 scan was cut short and is UNVERIFIED. The
corpus-wide «метаданные» decision and the contributor-provenance N2-coverage paragraph that EN also carries in 竹 are
follow-ups recorded in the dispositions; this record does not claim that any issue comment was posted.

## Final exclusion set

All 165 EN exclusion entries (27 lists; EN has none on 育児, 肘 or 羨む) are retained in EN order; 19 of them lie inside
the batch, and the other 146 target existing RU cards. Eight direct, one-sided entries are added on seven new cards, all
appended at the end of their lists. Seven were present at the candidate (from the authoring lane as adjudicated by the
coordinator) and one was added by fix 2; no fix removed one.

- Required (1): 能率→効果 (効果 «эффект; действенность»).
- Conservative (6): 活躍→役割 and 役 (役割 «роль; круг обязанностей», 役 «роль; обязанность»), 育児→育てる (育てる
  «растить; воспитывать»), 肯定→主張 (主張 «утверждение; настаивание на своём»), 職人→名人 (名人 «мастер своего дела») and
  習字→清書 (清書 «чистовик; переписывание начисто»).
- Fix 2 (1): 生き生き→明るい (明るい «светлый; яркий; жизнерадостный»), judged "well formed" and "justified" at the
  consistency recheck.

The consistency reviewer classed 能率→効果 and 活躍→役割/役 (given the current RU title) as required, 育児→育てる, 肯定→主張
and 職人→名人 as conservative, and 習字→清書 as conservative leaning unjustified ("Harmless over-guard; may stay or go
(nonblocking)"); the coordinator kept it. おかけください takes no guard against ください, どうぞ or 頂戴: title segments split on
«;», and EN guards none of these pairs. Every RU addition is appended at the end of its list, and no EN entry is removed
or reordered. Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (耕す F1, 功績 F2, 職人 F3); the 布く/藉く and 展げる spelling labels remain
  UNVERIFIED and are not asserted defects.
- Scoped coverage: **CLEAN** after fix 3 (R1, 実力:37); CLEAN throughout in the comprehensibility review.
- Comprehensibility: **CLEAN** after fixes 1 to 3 (広々, 膨大, 学力, 学術, 羨ましい, 耕す, 職人, 背負う, 実績, 生き生き,
  膨らむ and 実力); the partial and modified dispositions stand as accepted, and the withdrawn findings are withdrawn.
- Cross-file consistency: **CLEAN** throughout; the seven restored navigation links in five files stand.
- Quiz safety: **CLEAN** throughout, including the five retitles and the 生き生き→明るい guard. This covers the reviewed
  batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread the changed cards or passages and the lines needed to judge them; the unchanged cards rest on review
  001, in which all three reviewers read all 30 cards in full against EN.
- The correctness reviewer could not retrieve raw JMdict annotations, so the 布く/藉く and 展げる labels remain UNVERIFIED;
  its fix-3 recheck did not rerun the validator. The consistency reviewer did not consult JMdict online, its semantic
  screen is a judgment, and its B246 lane scan was cut short. The comprehensibility reviewer did not re-audit 布く/藉く
  or rerun the title screen. Necessity classes are judgements, not measurements.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fixes, so its payload hashes describe the candidate `8cada6d`, not `5e64cd7`.
- Frequency and preferred register (for example «раздольно», «необъятный», «послужной список», «заметная роль» and
  «выработка») were not certified. Online dictionaries were current observations, not pinned archives. The app's quiz
  selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
