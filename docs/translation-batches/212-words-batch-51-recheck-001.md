# Batch 212 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `d5fd0d933b7590c71fceadde93af255a14c4e0c0` | `e25b42695c1de0f449a934e1fd3152047e1f92a3` | Initial review snapshot: the signed candidate, pushed before review. |
| `2cb512c0d3a519ed75f04d9dcdce6c157c55c56c` | `ba5afad22984902da0ecbcad90d0b6469833db1e` | Fix 1 (final candidate): the consistency finding, both comprehensibility findings, three adopted optional notes, two coordinator guards and the intake refresh, committed signed and pushed before the rechecks. |

Fix 1 changed five word files and regenerated `manifest.json` (`contentVersion` `9ea98e5abdb9dbf5`, 4,474 entries) and the
intake:
- `完全`: title and H1 «полный (без изъянов); совершенный» instead of «совершенный; безупречный» (comprehensibility K1,
  modified wording). EN is "complete; perfect" and JMdict 1211510 "perfect; complete"; line 16 and the first example
  teach полнота. The reviewer's «цельный» was not used, because it means "whole, of one piece" rather than "with nothing
  missing"; the qualifier restates line 16 («нет недостающей части или дефекта») and separates the title from 一杯's
  container sense. The first example now reads «Это не полное решение.» without «проблемы», which 解決 does not contain.
  `quiz_exclusions: [全く, 全然, 一杯, 太い]` instead of `[全く]`: 全然 «совсем не; совершенно» shares the «совершенн-» stem
  as 全く does, and JMdict 全然 also has an affirmative "completely" use (consistency F1). The new title shares the exact
  segment «полный» with 一杯 «полный; одна чашка (порция)» and 太い «толстый; полный (о телосложении)», so the coordinator
  added both guards; 太い is conservative because its qualifier differs.
- `学習`: title and H1 «учёба; процесс изучения» instead of «освоение знаний; учебный процесс» (comprehensibility K2). EN
  is "learning; study". «Учебный процесс» names a school's organized instruction, and «освоение» can suggest the mastery
  that line 40 denies. The exact segment «учёба» shared with 勉強 «учёба; изучение» is guarded by EN's 学習→勉強.
- `好み`: title and H1 «предпочтение; личный вкус» instead of «пристрастие; вкусы (человека)» (adopted comprehensibility
  optional note, modified wording). EN is "preference; personal taste"; «пристрастие» leans towards a strong fondness. The
  exact segment «личный вкус» shared with 趣味 «хобби; личный вкус» is guarded by EN's 好み→趣味.
- `学者` (lines 17–18): «Слово может называть и просто образованного, учёного человека, а не только исследователя.» instead
  of «Слово может описывать и просто учёного, образованного человека.» (adopted optional note; EN "It can also describe a
  learned person.").
- `奥` (line 19): «в глубину ящика» instead of «в самую глубину ящика» (adopted optional note; EN "at the back of the
  drawer").
- The intake note now names the fixed cards, and the five candidate hashes were refreshed.

Net change from the candidate: three titles with their H1 headings (完全, 学習, 好み), two example translations (完全, 奥), one
explanatory sentence (学者) and three added exclusions on 完全. No Japanese example, reading or link changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially. Each reviewer appended to its own report file, which stayed in its session context, and each
recheck message gave it:
- the revised snapshot, its parent and the read-only rules;
- the actual content diff (`git diff d5fd0d9 2cb512c -- words`), saved as a file;
- the coordinator's evidence for every change, and the declined items from all three facets with their reasons, without
  the other reviewers' reports;
- the coordinator's disposition of each of its own findings and optional notes.

The shared opening said that the edits came from the consistency and comprehensibility reviewers, with two
coordinator-added quiz guards, and asked each reviewer to judge every change on its evidence rather than its origin.

The recheck prompts forbade running `tools/build_manifest.py` or any other generator; all three recheck sections state that
none was run. The correctness and consistency reviewers ran `tools/validate.py` (0 errors); the comprehensibility reviewer
states that it did not. After every recheck the coordinator confirmed that HEAD was unchanged and that
`git status --porcelain --ignored` was empty.

### Round 1 (`2cb512c`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer had no findings to reconcile and treated the supplied rationales as hypotheses. It read the full content diff and reread 完全, 学習, 好み, 学者 and 奥 in full against their frozen EN originals. 完全's qualified title keeps completeness and perfection, and «без изъянов» excludes the filled-container and body-size senses of «полный»; «Это не полное решение» still negates completeness, not every solution. The three added guards preserve the earlier guard and all EN metadata, and conservative exclusions assert no lexical equivalence. 学習 covers learning and study without promising mastery or an institution; 好み keeps preference and personal taste in neutral register; 学者 keeps the learned-person sense without a professional restriction; 奥 loses only an unsupported extreme. It freshly inspected the Jisho/JMdict entries for all five words (1211510, 1206820, 1277500, 1206800, 1179320) and the Kuznetsov entries «полный» (adjective senses 4–5), «изъян» (sense 1), «учёба» and «предпочтение». `tools/validate.py` reported 0 errors. Correctness and scoped coverage are **CLEAN**; no regression. |
| Consistency | The reviewer confirmed that the fix touches seven files (five cards, the manifest and the intake). F1 is resolved by the 全然 guard. It classified 完全→一杯 as required, because «полный» is an exact shared segment and JMdict 一杯 has the sense "full", and 完全→太い as conservative, because 太い's qualifier «(о телосложении)» leaves ordinary-quiz necessity unestablished. Its scripted regression screen of the three retitled cards against all RU titles, by exact segment and 5-character stem, found no unguarded exact collision: «полный» is guarded with 一杯 and 太い, «совершенн-» with 全く and 全然, «учёба» with 勉強, and «личный вкус» with 趣味; the remaining stem hits (上達, 成人, ぴんぴん, 留学, 予想, 想像) are not defensible answers. All 3,733 Markdown manifest hashes and all 51 intake candidate hashes match the working tree. It accepted the declined 宇宙→世界 as optional. Consistency, quiz safety and cross-file integration are **CLEAN**. |
| Comprehensibility | The reviewer read the five changed passages in full context. K1 is resolved: the new 完全 title matches line 16, the first example, EN and the unchanged sibling gloss `完成.md:31`; the parenthetical keeps «полный» from reading as 一杯's full cup. K2 is resolved: «учёба; процесс изучения» matches the examples and line 38, and the body's «освоение знаний» is not a new defect while line 40 still denies automatic mastery. The adopted 好み, 学者 and 奥 notes read clearly and match EN; «учёного» in 学者 agrees with «человека» as the adjective "learned". It accepted the declined 嫌う:20 and 学期:20–21 notes without promoting them. No EN teaching point was removed. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness | **No findings** | Review 001 reported none; the recheck found no regression. |
| Consistency F1: no 完全→全然 guard | **Resolved** | `完全.md:9`; JMdict 全然 (affirmative "completely" use); shared «совершенн-» stem. Severity unchanged (minor). |
| Consistency optional: guard 宇宙→世界 | **Optional, not adopted** | EN declares no such pair; no exact title segment is shared; the body teaches the contrast; the app deduplicates exact titles only. Reviewer accepted the decline. |
| Consistency classification of the 13 RU-added candidate entries (8 required, 5 conservative, none unjustified) | **Unchanged** | The recheck kept it and classified the two coordinator guards (below). |
| Consistency limit: 向かう and 汚す lack an EN exclusion in RU | **No action; deliberate earlier withdrawals** | Outside this batch. 汚す–土 was withdrawn as English soil homography (`docs/translation-batches/028-colour-shape-size-intake.json:5517`; `028-colour-shape-size-review-resolution-freeze.json:172`); 向かう–顔 as English face homography (`073-movement-direction-and-transfer-authoring-freeze.json:1747`; `073-movement-direction-and-transfer-corrected-candidate-001.json:163`). |
| Consistency limit: 118 strokes raw-hash differences | **No action** | `tools/build_manifest.py` hashes text after CRLF→LF normalization, as recorded in Batch 209; untouched by this batch. |
| Comprehensibility K1: 完全 title keeps only the quality sense | **Resolved** (modified wording) | `完全.md:4,12,16,19`; JMdict 1211510; frozen EN `完全.md:4`; `完成.md:31`. |
| Comprehensibility K2: 学習 title «учебный процесс» / «освоение» | **Resolved** | `学習.md:4,12,38,40`; JMdict 1206820. |
| Comprehensibility optional: 好み «пристрастие» | **Resolved** (adopted, modified) | `好み.md:4,12`; EN "preference; personal taste"; Kuznetsov «предпочтение». |
| Comprehensibility optional: 学者:17–18 wording | **Resolved** (adopted) | `学者.md:17–18`; EN "It can also describe a learned person." |
| Comprehensibility optional: 奥:19 «в самую глубину» | **Resolved** (adopted) | `奥.md:19`; EN "at the back of the drawer". |
| Comprehensibility optional: 嫌う:20 «Из неприязни к толпе…» | **Optional, not adopted** | «Не желая попасть в толпу» renders EN "to avoid the crowds", and line 22, as in EN, states the aversion; reviewer did not promote it. |
| Comprehensibility optional: 学期:20–21 «учебный период» | **Optional, not adopted** | Lines 15–18 and 23 explain the school dependence and 今学期; the examples show both common renderings; reviewer did not promote it. |
| Coordinator guards 完全→一杯 and 完全→太い | **Added** | Exact segment «полный» created by the K1 retitle; consistency recheck: 一杯 required, 太い conservative. |
| Exclusion classification | **Reviewer differs from author on 7 entries** | The author called 12 of the 13 candidate entries conservative; the consistency reviewer rated 完全→全く, 完了→完成, 完了→仕舞い, 宅→お宅, 学者→研究者, 嫌う→避ける and 不思議→謎 required, on the evidence in the independent record. The reviewer's classification is recorded as final. |

Cross-batch note: the three links held in Batch 211 cards, `完成.md:27` (完了), `完成.md:31` (完全) and `専攻.md:28` (学ぶ), are
restored at their EN-linked positions with EN's href forms, and all three reviewers judged them in review 001 with no
finding. `完成.md:31`'s gloss «полный; совершенный» now agrees with 完全's revised title.

## Final exclusion set

All 32 EN exclusion entries (15 lists) are retained. Sixteen direct, one-sided entries are added on nine new cards:

- Required (10): 完全→全く, 完全→全然, 完全→一杯, 完了→完成, 完了→仕舞い, 宅→お宅, 学者→研究者, 存在→ある, 嫌う→避ける,
  不思議→謎.
- Conservative (6): 完全→太い, 完了→終わる, 完了→終える, 完了→済む, 妙→奇しい, 好み→好む.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** throughout.
- Scoped coverage: **CLEAN** throughout.
- Comprehensibility: **CLEAN** after fixes (完全, 学習; optional polish in 好み, 学者 and 奥).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after fixes (完全→全然, with 完全→一杯 and 完全→太い added for the retitle), for the reviewed batch
  and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

Limits: the rechecks reread only the changed passages and the cards needed to judge them; unchanged cards rest on review
001's full reading. The comprehensibility reviewer did not reread `完成.md:31` in the recheck; agreement rests on its
review-001 reading of an unchanged line. The consistency reviewer's JMdict senses came from its own knowledge, with only
世界 fetched, and it did not read EN bodies line by line or re-check `strokes/*.json` in the recheck. The comprehensibility
reviewer did not run `tools/validate.py`. No native-speaker, learner, app-import, device, media, activation or release
acceptance is claimed.
