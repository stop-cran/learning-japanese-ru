# Batch 241 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `5e43b26c27b09f0e00c766db801c20954a827654` | `81db4ea431574bf2d6d8de974150fd4ffa35bdf0` | Initial review snapshot: the signed candidate, on `origin/full-ru-241-words-80`. |
| `9cf16009eacc4755caa30876b3006427d1720f4e` | `7a3d05e30f872cf2654f499a186e6a5d85cdd58d` | Fix 1 (final candidate). It covers correctness C1 to C3, the correctness optionals on 一段's wording and 広める:32 (through comprehensibility C1 and C12), and comprehensibility C1 to C6 and C8 to C12 (C2, C3, C8 and C11 as modified dispositions). Comprehensibility C7 was declined. It adds no exclusion, removes none, and adds or removes no link. Signed; on `origin/full-ru-241-words-80`. |

Fix 1 changed ten word files and regenerated `manifest.json` (`contentVersion` `026792faf1f03aa1`, 5,349 entries:
5,344 `files` + 3 images + 2 scenes; the candidate had `6b287c38009cd16d`). The intake was not refreshed; it still records
the candidate's 34 payload hashes. Its message reads "Retitle うんと, 広める, 余計, 一段, ばからしい, 大層, 格別, あわただしい
and 予備; fix example renderings in 一段, ばからしい, 余計, 大層, 宣伝, あわただしい; remove the metadata remark from 広める.
なんとも C7 declined with rationale."
- `うんと` (lines 4 and 12; correctness C1 = comprehensibility C6): title and H1 «много; очень; намного (при сравнении)»
  instead of «в большом количестве; намного (при сравнении)», restoring the non-comparative degree sense taught at line 16
  (Digital Daijisen sense 2 via kotobank; Jisho sense 1). The comprehensibility remedy «много; очень; намного» was
  adopted with the qualifier «(при сравнении)» kept.
- `広める` (lines 4 and 12; correctness C2 = comprehensibility C4): title and H1 «распространять; расширять» instead of
  «распространять; расширять (знания)» (Digital Daijisen sense 1 via weblio, 範囲を広くする; EN "disseminate; broaden").
- `広める` (line 32, now removed; comprehensibility C12, also the correctness optional): «Она не добавляет 弘 в метаданные
  основной записи этой карточки.» is deleted; line 31 «弘める — другая словарная запись ひろめる.» is unchanged.
- `余計` (lines 4, 12 and 18; correctness C3, and comprehensibility C3 modified): title and H1 «сверх необходимого;
  ненужный; ещё больше» instead of «сверх необходимого; ненужный; сильнее прежнего»; line 18's body gloss «значить «ещё
  больше», «ещё сильнее».» instead of «значить «больше», «ещё сильнее».» The comprehensibility remedy «тем более» was not
  used ("a discourse connective in Russian and fits the adverb less directly").
- `余計` (line 21; comprehensibility C3, modified): «— Я невольно сказал то, чего не нужно было говорить.» instead of «— Я
  сказал то, что было совсем не нужно.», restoring てしまう without «совсем». The remedy «Я в итоге сказал лишнее.» was not
  used.
- `一段` (lines 4, 12, 17 and 19; comprehensibility C1, also the correctness optional): title and H1 «в ещё большей
  степени; одна ступень» instead of «ещё заметнее; одна ступень»; line 17 «оно значит «ещё больше», «в ещё большей
  степени».» instead of «оно значит «ещё заметнее», «в ещё большей степени».»; example «— После дождя стало ещё
  холоднее.» instead of «— После дождя похолодало ещё заметнее.» The remedy's title «ещё больше; одна ступень» was not
  used. The RU-only link at 一段:32 and the kanji link at 一段:28 are unchanged.
- `ばからしい` (lines 4, 12 and 20; comprehensibility C2, modified): title and H1 «нелепый; глупый; смехотворный» instead
  of «нелепый; смехотворный», keeping all three EN senses ("absurd; foolish; ridiculous") rather than dropping
  «смехотворный» as proposed; example «— Верить таким слухам глупо.» instead of «— Верить таким слухам нелепо.»
- `大層` (lines 4, 12 and 21; comprehensibility C5): title and H1 «в большой степени; внушительный; преувеличенный»
  instead of «изрядно; внушительный; раздутый (о словах)» (EN "very; grand; exaggerated"); example «— Я получил
  внушительный подарок.» instead of «— Мне преподнесли внушительный подарок.»
- `宣伝` (lines 20 and 21; comprehensibility C8, modified wording): «— Сотрудники магазина рекламируют новый товар.» instead
  of «— Продавцы рекламируют новый товар.»; «— Я попросил друга прорекламировать школьный фестиваль.» instead of «— Я
  попросил друга рассказать всем о школьном фестивале.» The remedy's «порекламировать» was replaced by «прорекламировать»
  ("the standard perfective"). The title is unchanged.
- `格別` (lines 4, 12 and 16; comprehensibility C9): title and H1 «необычайный; в особенности» instead of «особенный; в
  особенности»; line 16 «нечто особенное, необычайное, выходящее из ряда» instead of «нечто особенное, выходящее из
  ряда».
- `あわただしい` (lines 4, 12, 16 and 21; comprehensibility C10): title and H1 «суматошный; спешный» instead of
  «суматошный; торопливый»; line 16 «спешную деятельность» instead of «торопливую деятельность»; example «— С самого утра
  я спешно готовлюсь.» instead of «— С самого утра я торопливо готовлюсь.»
- `予備` (lines 4 and 12; comprehensibility C11, modified): title and H1 «резерв; запасная вещь; предварительная
  подготовка» instead of «резерв (запасные вещи, силы); предварительная подготовка», keeping EN "spare" while dropping the
  definition-style parenthetical and untaught «силы». The remedy «резерв; предварительная подготовка» was not used.

Declined or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Comprehensibility C7 (なんとも:22) was declined: "«Меня это вовсе не волнует» renders 何とも思いません idiomatically and
  matches EN "I do not care about that at all"; 何とも思わない is the fixed expression "to not care / think nothing of".
  The proposed «Я об этом вовсе так не думаю» means "I do not think so at all", which mistranslates it. The nuance
  section (negation belongs to 思わない) remains taught in prose. Disagreement preserved for recheck." At recheck the
  comprehensibility reviewer withdrew C7, and the correctness reviewer independently judged the existing rendering
  accurate.
- The correctness optional "explain итидан at first use" was declined: "collection-standard term (docs
  glossary/methodology), used across published cards; a glossary pass is a tracked corpus-wide follow-up".
- The correctness optional on 特殊:29 and やたら:30 and the matching comprehensibility optionals were declined: "both are
  faithful to EN (EN 特殊/やたら carry the same remarks) and match 16 published RU cards with
  «метаданные»/«список кандзи пуст» sentences; a corpus-wide decision is recorded as a follow-up rather than diverging
  card-by-card".
- Consistency's five extra guards (格別–別に, いきなり–意外, でたらめ–くだらない, 余計–贅沢, 臨時–追加) were declined:
  "reviewer marked low confidence; displayed labels do not share a segment and the senses are distinct". The 一段 → 段
  link was confirmed, with no action; the missing kanji cards acknowledged in prose took no action.
- The other comprehensibility optionals: 自習:41's JMdict framing was declined ("source attribution is the collection's
  convention"); 傑作:20 «один из» and :23 «Дайдзисэн» were declined ("match EN ("one of his masterpieces"; the attributed
  dictionary example)"); 臨時:4 «дополнительный» was declined ("unguarded segment collision with 追加"); 臍:4
  «средоточие» was declined ("apt for 物事の中心 and avoids 中心/中央 «центр»"); 稽古:20 «кэндо» took no action
  ("reviewer: established loanword").

The dispositions' post-fix screen reads "Exact-segment overlaps of the 10 changed titles against the RU primary plus the
B242/B243 draft pool: 11, all already guarded (うんと×7, 余計×2, ばからしい–馬鹿, 大層–オーバー)." They record
`tools/build_manifest.py` (5,349 files), `tools/validate.py` 0 errors, the unit tests (124) OK and the content budget
within limits in the post-fix state. The consistency recheck's own exact-segment screen of the nine new titles against
all RU word titles found "every shared segment is guarded on at least one side (zero unguarded)", with the dispositions'
11 hits; it judged the stem-level near-hits acceptable (あわただしい «спешный» vs 急行 «спешно направляться» and
そそっかしい «поспешный»; 予備 «запасная вещь» vs 非常口 «запасный выход»; 余計 and 一段 vs 一層/更に, guarded) and found
no remaining quote of the removed title wordings in the tree, the remaining hits being "non-title prose".

Coordinator correction after the rechecks: the dispositions add a final section correcting their post-fix screen. "the
10 changed titles" should read "the 9 changed titles": "The fix changed ten word cards but nine titles (あわただしい, うんと,
ばからしい, 一段, 予備, 余計, 大層, 広める, 格別); 宣伝 changed only its example translations." Their rerun on the nine
retitled words against the RU primary at `9cf1600` (`b241-postfix-screen.txt`; 39 `OK` lines for guarded pairs and 124
stem-only `!!` lines) "finds the same 11 exact-segment overlaps, all guarded, and no unguarded exact segment". The
recheck briefs had also said "10 changed titles"; the consistency recheck itself checked "all nine changed cards", so no
recheck verdict depends on the uncorrected count. The dispositions also credit the consistency reviewer with "scoped
coverage CLEAN"; its report gives no separate scoped-coverage verdict (its verdicts are consistency, navigation-only
restorations, quiz safety and intake record CLEAN, and at recheck consistency, quiz safety and cross-file integration
CLEAN).

Net change from the candidate:
- titles and H1s of うんと, 広める, 余計, 一段, ばからしい, 大層, 格別, あわただしい and 予備;
- example translations in 余計, 一段, ばからしい, 大層, 宣伝 (two) and あわただしい;
- prose in 余計 (line 18), 一段 (line 17), 格別 (line 16) and あわただしい (line 16), and the deletion of 広める:32;
- no exclusion added or removed;
- no link added or removed.

No Japanese example sentence, sourced reading, navigation file, kanji card, quiz exclusion or link changed. The content
diff `5e43b26..9cf1600 -- words` is ten word files, 29 lines added and 30 removed; with `manifest.json` the commit changes
11 files, 40 lines added and 41 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the recheck sections do not restate the model, and the initial reports state "Model identifier not independently
verifiable.", "Model: not verifiable from inside the session." and "Model: not verifiable."

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. This ordering rests on the coordinator's session records; the recheck sections do not record times.
Each recheck covered the full diff `5e43b26..9cf1600` (10 word cards and `manifest.json`). No recheck raised a new
finding, so there was no fix 2.

Each reviewer appended its recheck to its own report file under `## Recheck (9cf1600)`. The correctness section records
that "All 10 changed RU cards and EN originals reread."; the consistency section records checks of titles and H1s, front
matter, `quiz_exclusions`, the manifest, an exact-segment title screen and removed wording; the comprehensibility
section reconciles each of its findings against the changed passages ("Ten passages match the diff.") and records
"Regressions: none."

All three rechecks state that no generator was run. The correctness reviewer states "No generator/test run, repository
edits or draft-pool audit; previous limits remain."; the consistency reviewer ran `validate.py` (0 errors), rebuilt the
manifest in memory only and records "status empty at start and end (my `tools/__pycache__` from validate/import was
removed)"; the comprehensibility reviewer records "No generator was run." and no validator run. The correctness section
records HEAD `9cf16009eacc4755caa30876b3006427d1720f4e`, "parent verified; initial/final status clean"; the consistency
section records HEAD `9cf16009eacc4755caa30876b3006427d1720f4e` with an empty status at start and end; and the
comprehensibility section records HEAD `9cf16009eacc4755caa30876b3006427d1720f4e`, parent `5e43b26` and "status empty".
The recheck records include no separate coordinator status check after the rechecks; when these records were drafted, a
read-only check showed the RU checkout on `full-ru-241-words-80` at HEAD `9cf16009eacc4755caa30876b3006427d1720f4e` with
`git status --porcelain --ignored` printing nothing.

### Round 1 (`9cf1600`)

| Facet | Scope and result |
|---|---|
| Correctness | HEAD `9cf1600`, "parent verified; initial/final status clean"; "All 10 changed RU cards and EN originals reread." "C1–C3 resolved: degree, broadening and non-temporal comparison restored." Optionals: "一段 wording and 広める metadata prose resolved; итидан explanation and 特殊/やたら prose remain optional. Deletion loses no Japanese fact; 弘める remains." "All rewrites are at least as accurate": 一段 "degree/step and colder example are faithful"; ばからしい "preserves absurd/foolish/ridiculous; rumor example improved"; 予備, 格別 and あわただしい retain their senses ("hurried activity, not merely urgency"); 大層 "retains degree/grand/exaggerated; “received” accurately renders humble いただく"; 宣伝 "staff/publicize renderings are faithful"; "余計's “невольно” is a legitimate unintended-result reading of てしまう, not its universal definition." On comprehensibility C7: "“not care at all” is accurate; proposed “I do not think so” wrongly adds disagreement." Evidence: gramota.ru «спешный»; weblio しまう (6b), いただく (4), 何とも (3). Correctness **CLEAN** and scoped coverage **CLEAN**. |
| Consistency | HEAD `9cf1600`, status empty at start and end; no generator; manifest rebuilt in memory only. "Title = H1 for all nine changed cards … scripted, all match. Front matter otherwise unchanged in the diff; `quiz_exclusions` untouched." `validate.py` 0 errors; "In-memory `build_manifest(Path('.'))` equals the committed `manifest.json`." Exact-segment screen of the nine new titles: "zero unguarded"; stem-level near-hits acceptable; no orphaned removed title wording. Optionals: the five extra guards "withdrawn/optional" ("格別's new title «необычайный» widens the gap from 別に further"); "一段 → 段 link: resolved (kept, correct)"; missing kanji cards "unchanged; still explicit coverage gaps acknowledged in prose"; 展開 formatting "optional, unchanged". Consistency **CLEAN**, quiz safety **CLEAN** and cross-file integration **CLEAN**; "No new findings." Limits: "semantic near-hit judgments are mine, from the Russian titles. Dictionary senses were not re-fetched. Translation accuracy of the new wordings is outside my facets. Disagreement on なんとも:22 is not in my facets." |
| Comprehensibility | HEAD `9cf1600`, parent `5e43b26`, status empty; "Ten passages match the diff. No generator was run." C1 to C6 and C8 to C12 are **resolved**, accepting the modified dispositions (for example "Accept «в ещё большей степени» over «ещё больше»" for C1, "Do not maintain dropping «смехотворный»" for C2, "Do not maintain «тем более» (discourse connective)" for C3, "Accept «прорекламировать» (ordinary perfective; no «всем») and «сотрудники магазина»" for C8, "Do not maintain dropping «запасная вещь»" for C11); C7 is **withdrawn** ("Do not maintain. なんとも思わない means “not care”; «не волнует» matches EN. «так не думаю» would mean “I disagree”. Nuance section still ties negation to 思わない."). Optionals "not maintained". "Regressions: none." Comprehensibility **CLEAN** and scoped coverage **CLEAN**. Limits: "dictionaries not re-opened; title screen not re-run. No native-speaker claim." |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: うんと's title lacks the noncomparative high-degree sense (medium; correctness and scoped coverage) | **Resolved** | `うんと.md:4,12`; Digital Daijisen sense 2 via kotobank; Jisho sense 1. |
| Correctness C2: 広める «расширять (знания)» restricts broadening to knowledge (medium; correctness and scoped coverage) | **Resolved** | `広める.md:4,12`; Digital Daijisen sense 1 via weblio; Jisho sense 2. |
| Correctness C3: 余計 «сильнее прежнего» makes the comparison temporal (medium) | **Resolved** | `余計.md:4,12,18`; Digital Daijisen adverb section via weblio; Jisho sense 3. |
| Correctness optional: 一段 wording | **Resolved** (through comprehensibility C1) | `一段.md:4,12,17,19`. |
| Correctness optional: explain итидан at first use | **Optional**; declined, remains optional at recheck | Collection-standard term; glossary pass is a corpus-wide follow-up. |
| Correctness optional: implementation remarks at 特殊:29, やたら:30 and 広める:32 | 広める:32 **resolved** (through comprehensibility C12); 特殊:29 and やたら:30 **optional**, declined | Faithful to EN; 16 published RU cards carry such sentences; corpus-wide follow-up. |
| Consistency classification: 一段→段 and 予備→余裕 required; あわただしい→騒ぎ and the other entries conservative or conservative-weak | **Recorded**; all sixteen pairs present | "No entry is unjustified"; the coordinator classed あわただしい→騒ぎ as required. |
| Consistency O1 to O5: extra guards 格別–別に, いきなり–意外, でたらめ–くだらない, 余計–贅沢, 臨時–追加 (low confidence) | **Optional**; declined, withdrawn/optional at recheck | Displayed labels share no segment; senses distinct. |
| Consistency O6: RU-only 一段 → 段 sentence and link | **Recorded**; kept, resolved at recheck | `一段.md:32`; "kept, correct". |
| Consistency O7: 展開 inline code | **Optional**; unchanged | "already used in 35 other word cards". |
| Comprehensibility C1: 一段 «ещё заметнее» (medium) | **Resolved** at recheck (modified: «в ещё большей степени» rather than «ещё больше») | `一段.md:4,12,17,19`. |
| Comprehensibility C2: ばからしい's title drops "foolish"; «смехотворный» bookish (medium) | **Resolved** at recheck (modified: «глупый» added, «смехотворный» kept; not maintained) | `ばからしい.md:4,12,20`; EN "absurd; foolish; ridiculous"; 馬鹿 excluded. |
| Comprehensibility C3: 余計 «сильнее прежнего»; example drops てしまう and adds «совсем» (medium) | **Resolved** at recheck (modified: «ещё больше» rather than «тем более»; not maintained) | `余計.md:4,12,18,21`. |
| Comprehensibility C4: 広める «расширять (знания)» (medium) | **Resolved** (= correctness C2) | `広める.md:4,12`. |
| Comprehensibility C5: 大層 «изрядно», «раздутый (о словах)», «Мне преподнесли» (medium) | **Resolved** | `大層.md:4,12,21`; EN "very; grand; exaggerated"; オーバー excluded. |
| Comprehensibility C6: うんと's title lacks non-comparative degree (medium) | **Resolved** (= correctness C1) | `うんと.md:4,12`. |
| Comprehensibility C7: なんとも:22 «Меня это вовсе не волнует» hides 思いません (medium) | **Withdrawn** at recheck; declined | `なんとも.md:22` unchanged; EN "I do not care about that at all"; the correctness recheck judged the rendering accurate. |
| Comprehensibility C8: 宣伝 «Продавцы», «рассказать всем» (medium) | **Resolved** at recheck (modified wording: «прорекламировать») | `宣伝.md:20,21`. |
| Comprehensibility C9: 格別 «особенный» repeats 特別 (medium) | **Resolved** | `格別.md:4,12,16`. |
| Comprehensibility C10: あわただしい «торопливый» describes a person (medium; medium confidence) | **Resolved** | `あわただしい.md:4,12,16,21`; 急行 «спешно направляться» a different sense. |
| Comprehensibility C11: 予備 definition-style title and «силы» (medium) | **Resolved** at recheck (modified: «запасная вещь» kept; not maintained) | `予備.md:4,12`; EN "spare"; 非常口 «запасный выход» shares no segment. |
| Comprehensibility C12: 広める:32 metadata sentence (low) | **Resolved** | `広める.md` (line 32 deleted); 弘める stays on line 31. |
| Comprehensibility optionals: やたら:30, 特殊:29, 自習:41, 傑作:20/:23, 臨時:4, 臍:4, 稽古:20 | **Optional**; declined or no action, not maintained at recheck | Reasons in the dispositions, quoted above. |

Cross-batch note: links to absent targets stay plain. Four EN link occurrences in this batch's new cards, to four
targets, are absent from RU: 大層 → kanji 層, なんとも → なんとなく, 着替え → kanji 替 and 広める → 広げる. The other written
kanji without an RU kanji card, 傑, 宣, 展, 殊, 甚, 稽, 臍, 臨, 至 and 衛, have none in EN either. The one RU-only link is
一段:32 → `段.md`, present at the candidate and unchanged by fix 1, beside EN's kept kanji link to 段 at 一段:28. The
link held from Batch 240, 早速:31 → さっさと, was applied by the coordinator's candidate script after that batch's
publication; fix 1 changed no navigation file. さっさと and 至急 exclude and link the Batch 240 card 早速, and 広める
excludes 散らす; their titles (早速 «без промедления; не откладывая», 散らす «раскидывать; рассеивать») are identical at the
authoring base and the published baseline. Batch 240's fix `3544d75` changed only example translations on those cards
(早速:21 and 散らす:21), and the coordinator's candidate-time note mentions only 早速:21; no B241 card quotes either
sentence. The dispositions record that "B242's 広げる (draft) already excludes 広める"; that card is a lane draft, not
published content, and the 広める → 広げる EN link stays plain until it exists. The corpus-wide glossary pass for итидан
and the corpus-wide decision on the «метаданные»/«список кандзи пуст» sentences are follow-ups recorded in the
dispositions; this record does not claim that any issue comment was posted.

## Final exclusion set

All 297 EN exclusion entries (30 lists) are retained in EN order; 29 of them lie inside the batch, and the other 268
target existing RU cards. Sixteen direct, one-sided entries are added on eleven new cards, all appended at the end of
their lists and all present at the candidate (from the authoring lane as adjudicated by the coordinator). Fix 1 added
and removed none. The coordinator classed them as follows:

- Required (3): あわただしい→騒ぎ (騒ぎ «переполох; суматоха»), 一段→段 (段 «ступенька; ярус; дан») and 予備→余裕 (余裕
  «запас (времени, денег, сил); невозмутимость»).
- Conservative (13): 自然科学→自然, 自治→管理, やたら→余る, 一段→だいぶ, うんと→もっと, 一層 and 更に, なんとも→別に and
  あんまり, 展開→流れ, 宣伝→進める, and 広める→発展 and 流行.

The consistency reviewer classed 一段→段 and 予備→余裕 as required, あわただしい→騒ぎ as conservative, うんと→一層/更に and
やたら→余る as conservative-weak and the others as conservative, and found "No entry is unjustified" and "None needs
removal". At recheck it confirmed `quiz_exclusions` "untouched". Every RU addition is appended at the end of its list, and
no EN entry is removed or reordered. Android applies each declaration symmetrically, so no reverse declarations were
added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (うんと C1, 広める C2 and 余計 C3).
- Scoped coverage: **CLEAN** after fix 1 (うんと and 広める in the correctness review; CLEAN throughout in the
  comprehensibility review).
- Comprehensibility: **CLEAN** after fix 1 (一段, ばからしい, 余計, 広める, 大層, うんと, 宣伝, 格別, あわただしい and 予備);
  the modified dispositions stand as accepted, and C7 is withdrawn.
- Cross-file consistency: **CLEAN** throughout; the four restored navigation links in four files and the RU-only 一段 →
  段 link stand.
- Quiz safety: **CLEAN** throughout, including the nine retitles. This covers the reviewed batch and the directly
  adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread the changed cards or passages and the lines needed to judge them; the unchanged cards rest on review
  001, in which all three reviewers read all 30 cards in full against EN.
- The correctness reviewer's dictionary downloads are current observations, "not claims about an archived dictionary
  capture"; its recheck ran no generator or test and did not audit the draft pool. The consistency reviewer cited
  dictionary senses from its knowledge and did not re-fetch them, and did not rerun the unit tests or content budget. The
  comprehensibility reviewer did not re-open dictionaries or rerun the title screen. Necessity classes are judgements,
  not measurements.
- The comprehensibility review read the navigation files as link-only diffs and used title-screen output as a lead only.
- The Russian wording the coordinator left to the blind review (among it «изрядно», «несуразный», «смехотворный»,
  «уморительная нелепость», «средоточие», «отработка навыков» and «особого рода») "was not entry-checked by the
  coordinator (only «самоподготовка» was checked)"; the correctness reviewer inspected Russian entries for several of
  them.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `5e43b26`, not `9cf1600`.
- Frequency and preferred register (for example «в большой степени», «спешный», «необычайный», «запасная вещь» and «Меня
  это вовсе не волнует») were not certified. Online dictionaries were current observations, not pinned archives. The
  app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
