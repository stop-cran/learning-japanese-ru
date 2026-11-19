# Batch 189 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `9251965ace4abea93cac73e84a2d32d76243abc5` | `6a7e3aff3e6da31527e2480e035cd9276878cde6` | Initial review snapshot. |
| `18ab3a6409b68b8dd958e56ceaa67f164b685edd` | `02e9a2b3d557b70b5f0eaaf16cc66a55d384a89f` | Final candidate: `避ける` reading-overlap qualification with a デジタル大辞泉 source line; `都市` gloss «город; городское поселение»; `鉄` and `銀` declare `金属`; manifest and intake regenerated. |

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks used the same assigned model variants and facets as review 001: `gpt-6.1-sol` correctness, `claude-sonnet-5.5` consistency/quiz safety, `grok-4.7` comprehensibility. Model assignments are recorded from the task-runner runtime listing; reviewer prose did not expose separate serving IDs.
They ran serially. Each reviewer received only its own original findings, the coordinator's dispositions of them, the revised snapshot and the actual diff `9251965..18ab3a6`.
The consistency reviewer was additionally given the correctness reviewer's outside-facet Q1 for adjudication; that recheck is therefore not blind to Q1.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | `18ab3a6` | C1 resolved against the cited dictionary text; no regression in the changed passages; correctness and scoped coverage **CLEAN**. |
| Consistency | `18ab3a6` | F1 resolved; Q1 decline confirmed; no new collision from the `都市` title; manifest hashes verified; consistency, quiz safety and scoped coverage **CLEAN**. |
| Comprehensibility | `18ab3a6` | F1 resolved; the rewritten `避ける` passage is followable; comprehensibility and scoped coverage **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1, categorical よける/さける split in `避ける` | **Resolved** (inherited-source correction) | The passage now says the JMdict split belongs to that entry, gives the overlap 水たまりをさけて歩く / 水たまりをよけて歩く from the デジタル大辞泉 usage note, keeps よける as the physical-dodge emphasis and says only さける takes a situation, question or responsibility. The editorial «Исходная глосса…» aside was removed and a source line added. The primary さける teaching and examples are unchanged. Frozen EN `避ける.md:32` keeps the categorical wording; the RU correction is recorded here rather than silently attributed to the source. |
| Correctness Q1, `鉄`–`鉄道` | **Optional, declined** | Coordinator adjudication, confirmed by the consistency recheck: JMdict 鉄 sense 4 "railway" is tagged Abbreviation and used as a prefix or suffix (私鉄, 地下鉄); sense 5 is colloquial. The RU card teaches and cites senses 1–3 only. «железо» and «железная дорога» share a stem, not a meaning, and frozen EN has no pair. A learner cannot reasonably accept either title for either word. |
| Consistency F1, `鉄`/`銀`→`金属` | **Resolved** | `鉄.md:9` and `銀.md:9` declare `quiz_exclusions: [金属]`; one-sided, with no reverse YAML on `金属`. |
| Comprehensibility F1, `都市` «городской центр» | **Resolved** | Title, H1 and the definition line read «город; городское поселение», matching the existing composition line. Nothing on the card says «центр», so the overlap with 中央/中心/真ん中 is gone; the existing `都会`/`市`/`町` guards still cover «город». |
| Comprehensibility suggestion: add a 都心 sentence | **Optional, declined** | With the misleading gloss removed, the card no longer suggests a city-centre reading, and the sentence would introduce an unlinked new word. The comprehensibility recheck agreed that it is unnecessary. |
| Comprehensibility optional, `便.md:44–47` source-list provenance paragraph | **Optional, declined** | It mirrors the frozen EN card's own paragraph and is kept for parity. |
| Comprehensibility optional, `重大` vs `大変` sentence | **Optional, declined** | `重大` already excludes `大変` directly, and the examples keep 重大 on consequences. |
| Comprehensibility optional, `避ける.md:41` editorial aside | **Resolved** | Removed as part of the C1 rewrite. |
| Consistency recheck optional note: «городское поселение» is also a Russian municipal-law term | **Optional, declined** | The phrase is also used in its general sense, and `都市.md:41–43` already says the word does not define administrative status and is not a formal municipal category. There is no quiz impact. |
| Consistency optional: future EN-pair obligations naming batch words (e.g. ピストル/鉄砲→銃, 硬貨/通貨→銅貨) | **Deferred** | These EN pairs are declared on cards with no RU card yet; they are carried when those cards are translated. |
| Consistency optional: 金庫–銀行, 違反–障害, 数 vs date cards, 重視–重大/かまう and the other examined leads | **Optional, declined** | The reviewer found no defensible overlap beyond the existing guards. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

The initial reviews read the complete 30-card common sample. The rechecks were bounded to their findings and the `9251965..18ab3a6` diff.
No reviewer re-audited the complete Russian word pool or executed the quiz UI.

## Final validation

On the final candidate `18ab3a6409b68b8dd958e56ceaa67f164b685edd`:

- `tools/build_manifest.py`: 3,789 files; content version `31917211355352d9`; the consistency recheck confirmed the in-memory build equals the committed manifest.
- `tools/validate.py`: 0 errors.
- `python -X utf8 -B -m unittest discover -s tools -p 'test_*.py'`: 124 tests passed.
- `tools/check_content_budget.py`: 3,797 archive files; 3,806 entries; 10,624,526 inflated bytes; 5,338,237 local ZIP bytes.
- Link parity on the 30 new cards: no lost or extra relative link; `避ける` adds one external Kotobank source link.
- Navigation-only files: the eight restoration files differ from `6bd7b05` only by 12 added links; text is identical after link stripping.
- `git diff --check`: clean. The intake was regenerated after the fixes; its hashes cover all 38 payloads.

## Limits

No native-speaker, device, learner, voice, drawing, runtime import, activation or ordinary-release acceptance is claimed.
Quiz-safety judgements rest on displayed titles, article text and dictionary senses, not a quiz-engine simulation. The standalone
frequency of 鉄 "railway" was not measured. The exact model variants above are the assigned models recorded by the task runner;
no serving-build identifiers were available.

## Appendix: recheck reports (verbatim)

### Correctness recheck (`gpt-6.1-sol`)

Snapshot: RU `18ab3a6409b68b8dd958e56ceaa67f164b685edd`, one commit after `9251965ace4abea93cac73e84a2d32d76243abc5`; clean working tree. Frozen EN HEAD remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`, clean.

Scope: Read-only recheck of my original correctness/scoped-coverage report and the allowed `9251965..18ab3a6` diff. Read all four changed cards from Git objects at the revised commit; assessed changed passages and their immediate context, not a fresh review of the unchanged batch. Inspected the actual dictionary entries cited below. No sub-agents; actual model identifier not independently verifiable in-session.

Reconciliation:
- C1; resolved; the former Minor correctness defect is removed in `words/避ける.md:38–46`. The JMdict restrictions are now explicitly entry-specific, and the physical-context overlap is demonstrated rather than prohibited. The [actual Jisho/JMdict entry](https://jisho.org/api/v1/search/words?keyword=%E9%81%BF%E3%81%91%E3%82%8B) restricts sense 1 to よける and sense 2 to さける. The [actual デジタル大辞泉 さける entry, sense 3 and 用法](https://kotobank.jp/word/%E9%81%BF%E3%81%91%E3%82%8B-510015) gives 「水たまりをさけて（よけて）歩く」, licenses overlap for consciously avoiding harmful/unwelcome things, reserves the discussed abstract-object uses for さける, and associates よける with concrete bodily movement aside. The card's two expanded Japanese forms, みずたまり／あるく readings and «обходить лужу» translation match that evidence. «Обычно» appropriately qualifies the physical-dodge preference. The editorial source-gloss aside is removed and the precise supporting dictionary section is linked. No residual actionable defect; confidence high.
- Q1; optional; the original 鉄／鉄道 observation was an explicitly unadjudicated, outside-facet quiz-safety lead, not a correctness finding. No direct exclusion was added; the coordinator's decision to decline it is recorded without treating that decision as independent proof of quiz safety. The revised 鉄 card still explicitly selects JMdict senses 1–3 (`words/鉄.md:46`). No in-facet fix is required; any runtime ambiguity determination remains with the assigned quiz-safety review.

Regression check:
- `words/避ける.md:38–46`: checked every replacement/addition against the entries above, including Japanese, kana, translation, source attribution and the distinction between overlap and unrestricted interchangeability. None found.
- `words/都市.md:4,12,16`: «город; городское поселение» consistently replaces «город; городской центр». The [actual JMdict lexical entry](https://jisho.org/api/v1/search/words?keyword=%E9%83%BD%E5%B8%82), distinct from the separate Wikipedia block, supplies とし, noun status and town/city meanings. The new gloss is compatible with those meanings; the retained context at lines 40–43 explicitly avoids defining an administrative status. None found.
- `words/鉄.md:9` and `words/銀.md:9`: the only changes are `quiz_exclusions: [金属]`; they introduce no Japanese, reading or meaning claim. No correctness/scoped-coverage regression found; comprehensive quiz-safety adjudication is outside this assignment.
- `manifest.json`: inspected the changed version/hash lines and independently matched all four revised card hashes against LF-normalized committed bytes, without regeneration. No mismatch found.

Verdicts: correctness CLEAN; scoped coverage CLEAN, within the bounded revised-passages/reconciliation scope. These verdicts do not extend to quiz safety or constitute a new full-batch review.

Limits: No author materials, other reviewers' reports/rechecks, translation batch/draft directories or translation-tracking JSON were read; those paths were excluded from the diff. No repository files were written, staged, committed, pushed or regenerated. Only this report was written. No app/device tests, corpus-wide quiz audit, validator/build, dictionary-frequency study or native-speaker certification was performed. Live Jisho data supports the inspected senses/restrictions, not independent verification of a historical JMdict numeric ID. No consequential unresolved in-facet claim remains.

### Consistency and quiz-safety recheck (`claude-sonnet-5.5`)

Snapshot: RU `full-ru-189-words-28` at `18ab3a6409b68b8dd958e56ceaa67f164b685edd` (single commit on top of `9251965`); `git status --short` empty at start and at end; frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f` read only. Committed content only; nothing was edited, staged, committed or regenerated (tools were run with `-B`/no bytecode; `build_manifest.build_manifest()` was called in memory, not its `main()`).

Scope: my original finding F1; the coordinator's 鉄–鉄道 question; every changed passage in `git diff 9251965 18ab3a6 -- manifest.json words` (`words/鉄.md`, `words/銀.md`, `words/都市.md`, `words/避ける.md`, `manifest.json`); quiz-collision effects of the new 都市 title on 中央/中心/真ん中/町/都会/市/郊外 and on every other card whose title contains город/поселение/центр; manifest/hash verification. The diff also touches the intake JSON, which the brief makes off-limits; it was excluded from the diff and not evaluated. Reviewer: the same single reviewer as before; the actual model family is not verifiable from inside the session, so no independence claim is made. No sub-agents.

Reconciliation:
- F1 (Minor, quiz safety: 鉄/銀 vs 金属): **resolved**. `words/鉄.md:9` and `words/銀.md:9` now declare `quiz_exclusions: [金属]` as a single top-level line between `tags:` and the closing `---`, as proposed; no body change. `金属.md` correctly declares nothing (one-sided, as 金→金属 already is in the frozen EN). No `quiz_distractors` anywhere in `words/` names 鉄, 銀 or 金属, so there is no distractor/exclusion contradiction. `python -B tools\validate.py` → `0 error(s)` (shape, duplicates, self/missing targets). 金's title is «деньги; золото», 金属's «металл»: no new sibling-metal label overlap is created (銀/金/鉄 remain distinct specific labels).
- Coordinator question, 鉄 «железо» vs 鉄道 «железная дорога» — no direct exclusion: **decline confirmed; not a defect (optional only)**; confidence medium-high. Evidence: (1) Jisho's JMdict rendering of 鉄 (1437780) gives s1 iron, s2 steel, s3 "iron (will, discipline…)", s4 "railway" tagged *Abbreviation*, parts of speech "Noun, used as a suffix / used as a prefix", see-also 鉄道, and s5 "railway enthusiast" (*Colloquial*, suffix). s4/s5 are combining-form/abbreviation uses attached to other morphemes (私鉄, 地下鉄, …), not an ordinary standalone secondary sense of the written word 鉄; the card honestly cites only 1–3 (`鉄.md:36`). The RU rule on secondary senses requires either a sense the old card's body already explains or an *ordinary* sense that fits another word's label; neither holds (`鉄.md` never mentions railway). (2) The exclusion test is "a learner could reasonably accept either `title` as the answer for either word" (frozen `docs/content-format.md`, "When to add one"). Prompt 鉄: «железо» is the standard answer and «железная дорога» is a different referent. Prompt «железная дорога»: 鉄道 is the exact word and 鉄 standalone does not name a railway system in ordinary usage. The labels share only a Russian morphological stem, not a meaning or a hyponym relation, unlike the repo's guarded pairs (水道–水 «водопроводная вода»⊃«вода», 車–電車 generic label, 火事–火, 自転車–車, 毛糸–糸), each of which rests on overlapping label content. (3) The shared kanji 鉄 makes the pair likelier to co-occur by the app's design (shared-kanji candidate scoring), which is the intended "plausible but clearly different" distractor case, not an ambiguity. (4) The frozen EN pair ("iron" / "railway; rail transport") has none, and `鉄道.md:23-24` already explains that 鉄 contributes «железо». Not weakening anything: if the coordinator nevertheless wants maximum caution, one direct pair `鉄道 → [鉄]` (one-sided, non-transitive, no effect on 鉄–道 or 鉄–金属) would be harmless but is unjustified by the contract and would set a stem-sharing precedent; I do not recommend it. Optional, scoped-coverage only: a one-line mention that 鉄 also abbreviates 鉄道 in compounds could be added later; not required for the stated scope.
- 都市 title «город; городской центр» → «город; городское поселение» (`都市.md:4,12,16`): **no new collision; one optional note**. Heading, front-matter title and the `## Значение` line are consistent with one another and with `## Как сочетаются кандзи` («называют городское поселение»); no other file quotes the old title (the only repo hit for «городской центр» is `町.md:40`, a JMdict gloss of 街, unrelated). Removing «центр» only reduces overlap: 中央 «центр; середина», 中心 «центр; ядро; главная часть», 真ん中 «самая середина; центр» no longer share any label word with 都市, so no 都市–中央/中心/真ん中 pair is needed (none existed before). «город» is retained, so the existing `[都会, 市, 町]` (labels «город; городская среда», «город», «городок; район») remain necessary and sufficient. No other word title contains «поселени» (checked all `words/*.md` titles for поселени/город/городск/центр/столиц/мегаполис). 郊外 «пригород; окраина города» needs nothing: its head noun is «пригород/окраина», «города» is only a dependent genitive, and it declares its own guards `[辺, 近所, 近く]`. Optional, non-blocking, outside this facet's authority: «городское поселение» is also a Russian municipal-law term; the body already disclaims legal status (`都市.md:36-38`), so there is no quiz impact; accuracy/comprehension reviewers adjudicate the wording.
- 避ける «Оттенки значения» rewrite and added source line (`避ける.md:38-46`): **no consistency or quiz-safety defect**. Title/heading/front matter unchanged, so no label collision; there is no `words/よける.md`, so the よける overlap creates no pair. The new text is consistent with the card's own `## Как сочетаются кандзи` («не взаимозаменяемы свободно»: partial overlap, not full interchangeability) and with the unchanged JMdict line (`s2`, contrast `s1`). The added `Пересечение чтений:` line follows the repo precedent of extra Kotobank/Daijisen lines (e.g. 公立, 入口, 休む). I fetched the cited page (`kotobank.jp/word/%E9%81%BF%E3%81%91%E3%82%8B-510015`): デジタル大辞泉 さける has sense 3 「よける」 and a 〔用法〕 note that さける/よける are interchangeable for consciously moving away from something harmful or unwanted (例 水たまりをさけて（よけて）歩く), さける alone takes abstract objects, よける stresses the concrete sideways movement — matching the new prose (sense numbering and example included). Link-parity: the EN link `[逃げる](逃げる.md)` is intact; one external link added, none lost.
- Manifest/hash integrity: **verified**. The generator's in-memory `build_manifest()` equals the committed `manifest.json` (3784 files, `contentVersion` `31917211355352d9`); SHA-256 of `git show 18ab3a6:<file>` equals the manifest entry for 避ける, 都市, 鉄 and 銀 (all LF). The manifest diff is exactly those four entries plus `contentVersion`; no entry added or removed; the commit changes six files (four cards, manifest, the off-limits intake JSON).

Regression check: changed passages — `鉄.md` front matter (+1 line), `銀.md` front matter (+1 line), `都市.md` title/heading/definition (3 lines), `避ける.md` `## Оттенки значения` and source lines — and `manifest.json` (4 hashes + contentVersion). New defects: **none**. Optional only: the municipal-law reading of «городское поселение» (above, for accuracy/comprehension adjudication) and the optional 鉄→鉄道 abbreviation note (above, scoped coverage). Neither is actionable under this facet.

Verdicts:
- Consistency (front matter, headings, source lines, links, manifest): **CLEAN**.
- Quiz safety: **CLEAN** (F1 resolved; 鉄–鉄道 decline confirmed; no new collision from the 都市 title).
- Scoped coverage (cross-file integration): **CLEAN**.

Limits:
- Intake JSON and its hash updates were not evaluated (off-limits by the brief); this report does not cover it.
- JMdict was read through Jisho's rendering; standalone frequency of 鉄 "railway" was not measured, so "not an ordinary standalone sense" is a judgment from JMdict's own tags (Abbreviation, prefix/suffix) and the card's cited scope, not a corpus result.
- Quiz defensibility is a judgment about displayed RU labels, not an execution of the app's candidate builder.
- Russian wording accuracy and pedagogy of the rewritten 避ける passage and the 都市 label belong to the accuracy/comprehension reviewers; I checked only consistency, sources' existence/consistency with the text, and quiz effects.
- Reviewer model not verifiable; no independence claim.

### Comprehensibility recheck (`grok-4.7`)

Snapshot: 18ab3a6409b68b8dd958e56ceaa67f164b685edd (full-ru-189-words-28; parent 9251965; working tree clean). Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f.
Scope: recheck of F1 and the three original optionals; changed learner passages in words/都市.md and words/避ける.md; quiz-exclusion-only edits in words/鉄.md and words/銀.md and hash-only manifest.json checked for facet regressions. Intake JSON not evaluated. Model not verifiable in-session.
Reconciliation: F1; resolved; words/都市.md:4,12,16 now read «город; городское поселение». Examples still say «в этом городе» / «в города», and the composition line already names «городское поселение». Nothing on the card says «центр», so the downtown reading and the 中央/中心/真ん中 title collision are no longer invited. The omitted 都心 sentence is not needed for clarity and would name an unlinked word.
Reconciliation: Optional 便.md:42–45; optional; declined for parity with the frozen EN provenance paragraph; passage unchanged; not elevated.
Reconciliation: Optional 重大 vs 大変; optional; declined; card unchanged; the direct 大変 exclusion and consequence examples were the stated reason; not elevated and not re-reviewed.
Reconciliation: Optional 避ける.md:41; resolved; «Исходная глосса смешивала эти значения» is gone.
Regression check: Checked words/都市.md:4,12,16; words/避ける.md:36–46; words/鉄.md and words/銀.md quiz_exclusions lines (no learner prose); manifest.json hash updates only. No new defect. The rewritten 避ける passage tells a beginner to use よける for a physical dodge or a blow, either reading when deliberately walking around something unpleasant (水たまりをさけて歩く（みずたまりをさけてあるく） / 水たまりをよけて歩く — «обходить лужу»), and only さける for a situation, question or responsibility. The puddle pair is Daijisen's own usage-note example; Jisho shows JMdict 1583260 sense 1 restricted to よける and sense 2 to さける. The second puddle example omits a repeated reading, but よ is written in kana and みずたまり was just given. The unchanged kanji line «не взаимозаменяемы свободно» still fits the qualified overlap.
Verdicts: comprehensibility CLEAN; scoped coverage CLEAN.
Limits: Not a native-speaker certification. Unchanged cards were not re-reviewed. The EDRDG entry page for 1583260 required a password; sense restrictions were read on Jisho. Intake JSON was not opened.
