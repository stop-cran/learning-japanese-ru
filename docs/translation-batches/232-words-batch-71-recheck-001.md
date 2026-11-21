# Batch 232 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `56da736ec2499c2e67dc01cd65078098c31e2716` | `e27c0b79e91de862b493efe3dffbc9683aa33060` | Initial review snapshot: the signed candidate, on `origin/full-ru-232-words-71`. |
| `97a39cfbd4ff4f3f8403b7fb1951fd702592a2af` | `f28e119438f3863c6ee74ca9def0b6efa248ef2f` | Fix 1 (final candidate). It covers correctness C1 and C2 and comprehensibility C1–C6, C8, C9, C11 and C12 (C2, C6, C8 and C11 with adapted wording; C3 and C4 partially adopted), and adds the RU exclusion 方面→針路 after 方面's retitle. Signed; on `origin/full-ru-232-words-71`. |

Fix 1 changed eleven word files and regenerated `manifest.json` (`contentVersion` `01cd8a2e02ee1c38`, 5,079 entries; the
candidate had `963e050e25bb648e`). The intake was not refreshed; it still records the candidate's 33 payload hashes.
- `角度` (lines 4 and 12; correctness C1 and comprehensibility C1): title and H1 «величина угла; ракурс (точка обзора)»
  instead of «величина угла (в градусах); ракурс (точка обзора)». The 角度→角 exclusion stays.
- `遊園地` (lines 31–32; correctness C2): «[公園](公園.md)（こうえん）— общественный парк: там можно отдыхать или играть, но
  он не обязательно является парком аттракционов.» instead of «… но это не парк аттракционов.»; the following 娯楽 sentence
  is unchanged.
- `方面` (comprehensibility C2, adapted wording):
  - lines 4 and 12: title and H1 «направление (к месту); сфера, область (деятельности)» instead of «в сторону (какого-либо
    места); сфера, область (деятельности)». The lead is now a noun, matching EN "direction". «сфера» was kept, although
    the reviewer proposed dropping it because of the overlap with 球, which the candidate already guards; it also supports
    the example «Он активно работает в сфере музыки.»;
  - line 9 adds 針路 «курс (судна, самолёта); направление движения», a noun direction sense that now shares
    «направление» with 方面's lead and had no guard:
    `quiz_exclusions: [方向, 方角, 方, 地方, 地域, 地区, 地帯, 区域, 辺, 分野, 場, 面, 角度, 郡, 道, 畑, 球, 針路]`.
- `道順` (lines 4 and 12; comprehensibility C3, partially adopted): title and H1 «маршрут (по улицам); как пройти
  (куда-либо)», the same glosses in EN order, instead of «как пройти (куда-либо); маршрут (по улицам)».
- `遡る` (lines 4 and 12; comprehensibility C4, partially adopted): title and H1 «подниматься вверх по течению;
  обращаться к прошлому» instead of «…; обращаться к прошлому (вести отсчёт назад)». The retroactive sense stays taught in
  the body (四月に遡って適用する).
- `部品` (lines 4 and 12; comprehensibility C8, adapted wording): title and H1 «деталь (механизма, устройства);
  комплектующие» instead of «деталь (механизма, устройства); запчасть». The plural «комплектующие» is the normal form and
  matches the body; the reviewer's singular «комплектующая» was not used.
- `超過` (lines 4 and 12; comprehensibility C9): title and H1 «превышение (лимита, нормы)» instead of «превышение (лимита,
  нормы); перерасход».
- `作製` (line 20; comprehensibility C5): «Мы изготавливаем чертёж новой детали.» instead of «Мы готовим чертёж новой
  детали.»; line 19 «сделали» stays (EN "made").
- `原料` (line 20; comprehensibility C6, adapted word order): «Сырьём для этой бумаги служит древесина.» instead of «Эту
  бумагу делают из древесины.»
- `過剰` (line 19; comprehensibility C11, adapted wording): «Чрезмерное беспокойство не идёт на пользу здоровью.» instead
  of «Чрезмерное беспокойство вредно для здоровья.»
- `逸れる` (lines 16 and 19; comprehensibility C12): «逸れる значит отклоняться от курса, проходить мимо цели или уходить
  от темы разговора.» instead of «… пролетать мимо цели …», and «Мяч прошёл мимо мишени.» instead of «Мяч пролетел мимо
  мишени.» (the reviewer cited the ball example as line 18; it is on line 19).

The comprehensibility reviewer's C7 (成分) and C10 (超過:48, cited as :49) were not adopted, nor were its wordings
«объяснение пути» (道順), «восходить к прошлому» (遡る) and the optional «точка зрения» (角度); its other optional notes
(過失 order, 方角, 遠足, 道順:19 «туда», 原料:21, 方針:19, 過半数:9 and 作製:19) led to no action. The consistency reviewer's
O1, O3 and O4 led to no action, and O2 was superseded by the 方面 retitle. The dispositions gave the reasons (see the
reconciliation table).

The coordinator's post-fix title screen of the six changed titles is recorded in its dispositions (10 `OK` lines for
guarded pairs, 55 stem-only `!!` lines). The exact title segments that a changed title shares with another card are all
guarded: 方面's «направление» with 方向 «направление; курс» and 方角 «сторона света; направление (по сторонам света)», its
«область» with 分野 «область (знаний, деятельности)» and its «сфера» with 球 «сфера; мяч»; 道順's «маршрут» with コース
«маршрут; курс (обучения)»; and 超過's «превышение» with オーバー «превышение (предела); преувеличенный; пальто». All but 球
are guarded by EN exclusions of 方面, 道順 and 超過, and 球 by the candidate's RU exclusion. 角度, 遡る and 部品 have no exact
hit. The screen listed 方面–針路 as a stem-only lead («напра»); it is now guarded by the new exclusion. Fix 1 adds no link
and removes none: the only changed link line is 遊園地:31, where the 公園 link and its target are unchanged. The six RU-only
links of the candidate (郡→町, 郡→村, 郡→市, 地帯→帯, 余る→残る and 余る→足りる) stand unchanged. `tools/validate.py` reported
0 errors and the unit tests (124) passed before the fix commit.

Net change from the candidate:
- titles and H1s of 角度, 方面, 道順, 遡る, 部品 and 超過;
- example translations in 作製, 原料, 過剰 and 逸れる;
- prose in 逸れる (line 16) and 遊園地 (lines 31–32);
- one exclusion (方面→針路) and no link change.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`56da736..97a39cf -- words` is eleven word files, 20 lines added and 20 removed; with `manifest.json` the commit changes
12 files, 32 lines added and 32 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs; the
initial reports state that the model is not verifiable from inside the session.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. No recheck raised a new finding, so there was no fix 2.

Each reviewer appended its recheck to its own report file. Each brief included the full words diff `56da736..97a39cf`, the
coordinator's evidence and rationale for the edits (the post-fix screen and the reasons for the declined items) and that
reviewer's original verdicts with their dispositions. The correctness section records that it read the complete
eleven-card diff and all eleven revised cards in full, comparing frozen EN lines 1–24; the consistency section records
the changed paths as the eleven cards plus `manifest.json`; the comprehensibility section reconciles each of its findings
against the changed lines. The recheck sections do not reproduce the briefs, so this record does not claim their further
contents.

All three rechecks state that no generator was run; the consistency recheck names `build_manifest`. The correctness and
consistency reviewers each ran `tools/validate.py` (0 errors each); the comprehensibility reviewer did not re-run the
validator. Each recheck section records snapshot `97a39cf` with a clean tree. After the three rechecks the coordinator
confirmed, read-only, that the RU checkout is on `full-ru-232-words-71` at HEAD
`97a39cfbd4ff4f3f8403b7fb1951fd702592a2af` (`git rev-parse HEAD`) and that `git status --porcelain --ignored` prints
nothing, so no tracked, untracked or ignored file was left by the rechecks.

### Round 1 (`97a39cf`)

| Facet | Scope and result |
|---|---|
| Correctness | Bounded recheck of the complete eleven-card diff and all eleven revised cards, read in full, against `56da736` and frozen EN lines 1–24, using the original review's full EN reads and dictionary evidence. C1 is **resolved**: 角度's title and H1 no longer restrict angular magnitude to degrees, and both literal and figurative senses remain. C2 is **resolved**: 遊園地 now says a 公園 is not necessarily an amusement park, removing the false categorical exclusion. No regression in the comprehensibility-driven rewrites: 方面's noun-first direction gloss is at least as accurate as the former phrase, and the added 針路 exclusion does not assert unrestricted interchangeability; 道順's reordering preserves accuracy and coverage; 遡る keeps the origin/date-back and retroactive applications in the body; 部品's «комплектующие» is broader than replacement-only «запчасть»; dropping «перерасход» from 超過 loses no necessary sense (the old narrower alternative was acceptable, not a proven error); 作製's «изготавливаем» keeps the ongoing production and technical register; 原料's new sentence names the taught role; 過剰's «не идёт на пользу» matches よくありません without strengthening it to a harm claim; 逸れる's «проходить/прошёл мимо» keeps missing the target without requiring flight. All six revised titles match their H1s. Validator 0 errors. Correctness and scoped coverage are **CLEAN**, carrying forward the original full 30-card review, with no new finding; optional: none. |
| Consistency | Snapshot `97a39cf` with a clean tree; the changed paths are the eleven cards plus `manifest.json`. Title equals H1 on all six retitled cards. Segment and whole-word screen of the six new titles against all RU word titles: the only hits are 方面~方向, 方面~方角, 道順~コース and 超過~オーバー, all guarded by existing direct exclusions; 部品 «комплектующие», 角度 «величина угла» and 超過 «превышение (…)» have no other-card overlap. 方面's exclusions are the prior 17 entries in order plus 針路, appended; the addition is justified, because 針路 is a noun «направление движения». All EN exclusions and the earlier RU-added guards remain, and the other ten cards' lists are unchanged. The body-only edits touched no links, and every `.md` link target in the eleven changed cards resolves. Manifest: 5,074 entries, 0 stale after normalising CRLF; the content-path set is unchanged (33). O1 stays optional, left open by author decision; O2 is **resolved**, superseded by the 方面 retitle; O3 and O4 stay optional. Validator 0 errors. Consistency, quiz safety and scoped integration are **CLEAN**, with no new finding. |
| Comprehensibility | Snapshot `97a39cf` with an empty `git status --porcelain`; reconciled each finding against the changed passages, not a full reread of all 30 cards. C1, C5, C9 and C12 are **resolved** as proposed. C2, C6, C8 and C11 are **resolved** in the adapted wordings, which the reviewer accepted: it does not maintain dropping «сфера» from 方面, because it is paired with «область (деятельности)», the music example uses «в сфере музыки» and 球 stays excluded, and the new 針路 exclusion is not a learner-facing regression; «Сырьём для этой бумаги служит древесина» keeps the taught role; «комплектующие» is the ordinary term and matches line 16; «не идёт на пользу здоровью» is weaker than «вредно» and claims no harm. C3 is **resolved** by the partial adoption: the lead is now «маршрут (по улицам)», and the reviewer withdrew «объяснение пути», because the word is the route itself and «как пройти» is the idiomatic second gloss for EN "directions". C4 is **resolved**: the counting parenthetical is gone, and the reviewer accepted not using «восходить к прошлому», because its stem meets 昇る and the Edo example already says «восходит к». C7 is **withdrawn** (EN 成分 uses "composition", 構成 is already excluded, and a new contrast would exceed EN scope). C10 is **withdrawn** for this card (the sentence translates the only EN provenance line; a corpus-wide cleanup is outside this fix). The optional «точка зрения» for 角度 stays declined, because it is the exact lead of 見解; the other optional notes are unchanged and not promoted. The revised 遊園地 sentence matches the Daijisen inclusion and does not contradict the later warning not to call every park 遊園地. Comprehensibility and scoped coverage are **CLEAN**, with no actionable defect in the changed passages. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 角度 «величина угла (в градусах)» restricts the measure to degrees (minor) | **Resolved** (with comprehensibility C1) | `角度.md:4,12`; Digital Daijisen 角度 sense 1 (ラジアン・度・分・秒); Seisenban definition 1 on Kotobank; EN "angle; viewpoint". |
| Correctness C2: 遊園地:31–32 says a 公園 is never an amusement park (minor) | **Resolved** | `遊園地.md:31–32`; Digital Daijisen 公園 sense 1 (publicly provided 庭園や遊園地); EN 遊園地:32 "can be … without being". |
| Correctness non-defect notes: «запчасть», «перерасход», «состав», phrase-like titles | **Reconciled on the evidence** with comprehensibility C3, C7, C8 and C9 | «запчасть» and «перерасход» replaced as narrower senses (Gramota's Kuznetsov entries cited by the correctness reviewer); «состав» kept (C7); the correctness recheck judged every rewrite at least as accurate. |
| Consistency optional O1: 部首 «ключ иероглифа (для поиска в словаре); радикал» and 鍵 «ключ» (very low) | **Optional, not adopted**; left open at recheck | The segments differ, the qualifier makes 部首 unambiguous, and EN has no guard; recorded as a follow-up for a possible owner decision. |
| Consistency optional O2: 方面 «в сторону» against あちら «вон там; в ту сторону» and そちら «туда; ваша сторона» (very low) | **Resolved** (superseded) | `方面.md:4,12`; the retitle removes «в сторону». |
| Consistency optional O3: お帰り:28 mentions 帰る plain (cosmetic) | **Optional, not adopted**; kept optional at recheck | EN is also plain; the mention is incidental. |
| Consistency optional O4: `kanji/余.md:21` keeps the bare gloss «оставаться; быть в избытке» | **Out of scope**; kept optional at recheck | Pre-existing prose outside the navigation-only scope; the 余る→残る guard covers the quiz risk. |
| Comprehensibility C1: 角度 «(в градусах)» (minor) | **Resolved** (duplicate of correctness C1) | `角度.md:4,12`; line 38 still says degrees are one unit. |
| Comprehensibility C2: 方面's phrase lead «в сторону (какого-либо места)» and bare «сфера» (minor) | **Resolved** (adapted wording) | `方面.md:4,9,12`; EN "direction; area; field"; 球 and the new 針路 excluded. |
| Comprehensibility C3: 道順's clause lead «как пройти (куда-либо)» (minor) | **Resolved** (partial adoption); «объяснение пути» withdrawn at recheck | `道順.md:4,12`; Daijirin 道順 (目的地へ行く道の順序); explaining is done by 教える and 説明する in both examples. |
| Comprehensibility C4: 遡る «(вести отсчёт назад)» (minor) | **Resolved** (partial adoption); not using «восходить к прошлому» accepted at recheck | `遡る.md:4,12`; the retroactive sense stays in the body (四月に遡って適用する); the stem «восходить» would meet 昇る «восходить (о солнце)». |
| Comprehensibility C5: 作製:20 «готовим» (minor) | **Resolved** | `作製.md:20`; EN "We are producing"; the title «изготовление». |
| Comprehensibility C6: 原料:20 drops the raw-material role (minor) | **Resolved** (adapted word order) | `原料.md:20`; EN "This paper uses wood as its raw material". |
| Comprehensibility C7: 成分:20 «состав продукта» and no 構成 contrast (minor, also coverage) | **Withdrawn** at recheck (declined) | EN renders the example "I investigated the food's composition"; JMdict 成分 includes "composition"; 構成 is already EN-guarded and EN adds no contrast. |
| Comprehensibility C8: 部品 «запчасть» (minor) | **Resolved** (adapted wording) | `部品.md:4,12`; Gramota's Kuznetsov entries запчасти and комплектующие (cited by the correctness reviewer); EN "parts; components; accessories". |
| Comprehensibility C9: 超過 «перерасход» (minor) | **Resolved** | `超過.md:4,12`; JMdict 1429410; the examples cover quantity, limits and time; オーバー guards the shared «превышение». |
| Comprehensibility C10: 超過 provenance sentence, cited as line 49 (minor) | **Withdrawn** at recheck (declined) | `超過.md:48` «Метка N2 взята из закреплённого списка слов сообщества.» translates EN's own "Level provenance" line, the only EN word card with one; RU instructions allow provenance in learner files. |
| Comprehensibility C11: 過剰:19 «вредно для здоровья» (minor) | **Resolved** (adapted wording) | `過剰.md:19`; 体によくありません; EN "is not good for your health". |
| Comprehensibility C12: 逸れる «пролетать / пролетел» adds flight, cited as lines 16 and 18 (minor) | **Resolved** | `逸れる.md:16,19`; EN "went wide of the target". |
| Comprehensibility optional: 角度 «точка зрения» instead of «ракурс» | **Optional, not adopted**; kept declined at recheck | It would be the exact lead of 見解 «точка зрения; позиция»; Ozhegov sense 3 supports «ракурс» as viewpoint. |
| Comprehensibility optionals: 過失 order, 方角, 遠足, 道順:19 «туда», 原料:21, 方針:19, 過半数:9 and 作製:19 | **Optional, not adopted**; kept optional at recheck | The reviewer classed them as acceptable. |
| Exclusion classification: the seven RU-added candidate guards | **Agreed**; all kept | 製作→作製 and 余る→残る required; 余る→余分, 角度→角, 方針→線, 方面→球 and 作成→建設 conservative and harmless. |
| Consistency recheck: «5074 entries» and the author's 5,079 not verified | **Not a discrepancy** | `manifest.json` at `97a39cf` has `contentVersion` `01cd8a2e02ee1c38`, `files` (5,074 entries), `images` (3) and `scenes` (2); the generator's 5,079 is the 5,074 `files` plus 3 images and 2 scenes. The candidate `56da736` has the same split. |
| Consistency recheck: a raw-byte manifest check on the Windows checkout showed line-ending differences | **Not a defect**; pre-existing and outside the batch | `tools/build_manifest.py` hashes text files after CRLF→LF normalisation. The 118 CRLF files are the stroke JSON byte copies committed under `.gitattributes` (`strokes/*.json -text`); every other tracked text file is LF in the index and working tree. Re-hashing all 5,074 `files` entries at `97a39cf` with the generator's normalisation matches the manifest, while a raw-byte hash differs for exactly those 118 files. Fix 1 touches no `strokes/` file. |
| Line citations in the comprehensibility report (C10 at :49, C12's ball example at :18) | **Noted; no action** | The provenance sentence is `超過.md:48` and the ball example `逸れる.md:19` at both snapshots; the findings were adjudicated on the cited text. |
| Corpus-wide convention for provenance lines in learner files (from C10) | **Out of scope**; recorded as a follow-up | Not changed by this batch; the comprehensibility recheck called a corpus-wide cleanup outside this fix. |

Cross-batch note: links to absent targets stay plain. Eleven EN link targets in this batch's new cards (12 occurrences)
are absent from RU: the word cards 資料 (from 原料), いってらっしゃい (from お帰り), 娯楽 (from 遊園地) and 制作 (from 製作); the
article kaeru-change-replace-and-return (from 返る); and the kanji cards 裏 (from 裏返す), 角 (from 方角 and 角度), 針 (from
方針), 順 (from 道順), 超 (from 超過) and 造 (from 造船). EN has kanji cards for 裏, 角, 針, 順, 超 and 造; the other written
kanji without an RU kanji card, 郡, 遡, 策, 剰, 逸, 統 and 製, have none in EN either. No links were held from Batch 231, and
none is held from this batch.

## Final exclusion set

All 177 EN exclusion entries (27 lists; 部首, 余る and 遊園地 have none) are retained in EN order. Eight direct, one-sided
entries are added on six new cards (one new list, 余る):

- Required (2): 製作→作製 and 余る→残る, added at the candidate.
- Conservative, nonblocking (5): 余る→余分, 角度→角, 方針→線, 方面→球 and 作成→建設, added at the candidate (the last three
  by the coordinator after its title screen).
- Added by fix 1 (1): 方面→針路, after 方面's retitle to «направление (к месту); сфера, область (деятельности)».

Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added; the targets do not declare these pairs back.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (角度 and 遊園地).
- Scoped coverage: **CLEAN**; the 成分 coverage item (C7) was withdrawn at recheck, keeping EN scope.
- Comprehensibility: **CLEAN** after fix 1 (角度, 方面, 道順, 遡る, 作製, 原料, 部品, 超過, 過剰 and 逸れる); C7 and C10 were
  withdrawn, and the optional notes remain optional.
- Cross-file consistency: **CLEAN** throughout; the six RU-only links and the six restored navigation links of the
  candidate stand.
- Quiz safety: **CLEAN** throughout, including the 角度, 方面, 道順, 遡る, 部品 and 超過 retitles and 方面→針路. This
  covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them; the comprehensibility recheck did not
  re-read all 30 cards. The unchanged cards rest on review 001, in which all three reviewers read all 30 cards in full
  against EN.
- The correctness recheck was a bounded diff recheck with no fresh dictionary fetch, comprehensive quiz/title-pool audit or
  unit-test rerun; its original evidence and model limitations remain. The consistency reviewer performed no dictionary
  lookups, its title screen was heuristic (whole segment and word, not every stem pair), and its necessity classes are
  judgements, not measurements; it did not re-run the unit tests. The comprehensibility recheck did not re-run
  `validate.py`, did not re-audit quiz symmetry beyond the new 方面–針路 pair and was not a fresh full-batch reread.
- Some of the correctness reviewer's initial live requests returned HTTP 429 or 403 and were read through another fetch
  path; only successfully inspected entries support its conclusions.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `56da736`, not `97a39cf`.
- The O1 部首/鍵 decision and the corpus-wide provenance convention were not resolved here and are left as follow-ups.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
