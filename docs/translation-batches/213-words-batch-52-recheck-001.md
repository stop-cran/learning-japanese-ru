# Batch 213 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `3c8461447a0a88352701ecb3fc7183b5c545a07b` | `2e363e3eaf674dd400edb587315ee26cfe455597` | Initial review snapshot: the signed candidate, pushed before review. |
| `fdd485e31e5ff65ad9c39357f6c3ac0b49bca310` | `3358b8e5c6af9dab2b9eb296e7d1bc87e587e514` | Fix 1 (final candidate): the consistency finding, the three comprehensibility findings and the intake refresh, committed signed and pushed before the rechecks. |

Fix 1 changed four word files and regenerated `manifest.json` (`contentVersion` `eaaff46553296873`, 4,504 entries) and the
intake:
- `大` (line 9): `quiz_exclusions: [大きい, 大きな, 莫大, 巨大, 大小]` instead of `[大きい, 大きな, 莫大, 大小]` (consistency F1).
  大's title «большой размер; огромный (как приставка)» introduces «огромный», and 巨大 «громадный; гигантский» (JMdict
  1232180 "huge; gigantic; enormous") is a defensible answer for it; the batch already guarded 莫大 for the same overlap.
  The title is kept, because its «огромный (как приставка)» matches the body's 大成功 example.
- `地方` (line 35): the closing sentence «Это слово не значит «побережье»…» is deleted (comprehensibility C1). It rejected an
  English word-list gloss that the RU card never presents, and its denial was absolute although JMdict and Digital
  Daijisen (Kotobank 地方, じかた sense 3) give the coast sense to the separate reading じかた. The 都会 and 東北地方
  sentences remain, and no じかた explanation is added. This supersedes the correctness reviewer's optional O1.
- `大統領` (line 32): «JMdict также отмечает отдельное фамильярное обращение, особенно к актёру, — что-то вроде «шеф!» или
  «дружище!».» instead of a comparison with «шеф!» or «молодчина!» (comprehensibility C2, modified wording). «Молодчина!»
  is praise, not a form of address. JMdict 1414650 sense 2 is "big man; boss; buddy; mate", familiar and vocative,
  especially of an actor; Digital Daijisen (Kotobank 大統領-557914) sense 2 is a friendly call to an actor on stage
  («待ってました、大統領»). The reviewer's added «а не похвала вроде «молодец!»» was not adopted, because that actor call is
  itself an encouraging cheer, so a flat no-praise contrast would overstate the evidence.
- `大部分` (line 29): after the 全部 sentence, «ほとんど тоже может значить «большая часть; большинство», но у него есть ещё
  значение «почти», а с отрицанием — «почти не». Значения «почти не» у 大部分 словари не дают: оно называет большую
  часть.» (comprehensibility C3, modified wording). JMdict 1414850 gives 大部分 as a noun only ("most part; greater part;
  majority") and ほとんど as an adverb "almost; nearly", with a negative "hardly". Digital Daijisen (Kotobank 大部分-558279)
  notes an adverbial use («仕事は大部分終わった») and Nihon Kokugo Daijiten gives an adverb sense «ほとんど。たいてい。
  おおかた», so the sentence denies only the negative «почти не», not «почти». ほとんど stays plain text, because EN has no
  link there and a RU-only link would break EN link parity; the sentence adds no Japanese example and does not mention
  titles or the quiz.
- The intake note now names the fixed cards, and the four candidate hashes were refreshed.

Net change from the candidate: one added exclusion (大), one deleted sentence (地方), one reworded sentence (大統領) and one
added two-sentence contrast (大部分). No title, Japanese example, reading or link changed.

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
- the actual content diff (`git diff 3c84614 fdd485e -- words`) and the brief, saved as a file;
- the coordinator's evidence for every change, and the declined items from all three facets with their reasons, without
  the other reviewers' reports;
- the coordinator's disposition of each of its own findings and optional notes.

The recheck prompts forbade running `tools/build_manifest.py` or any other generator; all three recheck sections state that
none was run. The correctness and consistency reviewers ran `tools/validate.py` (0 errors); the comprehensibility reviewer
states that it did not. After every recheck the coordinator confirmed that HEAD was unchanged and that
`git status --porcelain --ignored` was empty.

### Round 1 (`fdd485e`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer had no findings to reconcile; O1 is resolved by the deletion, with no sentence left to qualify. It compared the actual diff against `3c84614` and checked each changed passage. The 巨大 guard keeps all earlier exclusions and teaches no new equivalence. The 地方 deletion removes only EN's source-list coast rejection, not a sense, example, reading or the urban/rural distinction, and RU never offers coast as a gloss. For 大統領 it re-read JMdict 1414650 (sense 2 "big man; boss; buddy; mate", familiar, vocative, especially of an actor), Digital Daijisen sense 2 (a friendly call to an actor) and Nihon Kokugo Daijiten sense 3 (flattering or praising calls); the qualified «что-то вроде» rendering keeps the register and does not wrongly exclude an encouraging cheer, and the political sense and corporate-title boundary are intact. For 大部分 it re-read the Jisho entries for 大部分 and ほとんど and Kotobank 大部分-558279 (Digital Daijisen recovered from the page HTML; also readable on Weblio): the sentence denies only the negative «почти не», not adverbial use or positive "almost; mostly" overlap. `tools/validate.py` reported 0 errors. Correctness and scoped coverage are **CLEAN**; no new findings. |
| Consistency | The reviewer confirmed that the fix touches six files (four cards, the manifest and the intake). F1 is resolved: 大's list is `[大きい, 大きな, 莫大, 巨大, 大小]`, all earlier entries are kept and 巨大 exists as an RU card. No title or front-matter field other than 大's exclusions changed, so no new title or segment overlap arises and the original exact-segment guard audit still holds. The 地方 deletion leaves the preceding text and its 都会 link intact; 大統領 is a wording-only change; 大部分's ほとんど contrast is plain text with no RU-only link and leaves its title and exclusions unchanged. The in-memory manifest equals `manifest.json`, the 51 intake paths equal the content diff against `1269d26` and all candidate hashes match. It accepted the declined title-overlap notes as optional. Consistency, quiz safety and cross-file integration are **CLEAN**. |
| Comprehensibility | The reviewer read the four changed passages in context and the sibling glosses in ほとんど, 大半 and 巨大. C1 is resolved: the «побережье» sentence is gone, the 都会 contrast and 東北地方 sentence remain, and no coast claim dangles. C2 is resolved: «шеф!» and «дружище!» are forms of address, not praise; it agreed that the declined «а не похвала» clause would overclaim, since the actor call can itself be an encouraging cheer; the 社長 warning remains. C3 is resolved: the plain-text ほとんど sentence matches ほとんど.md («почти»; negative «почти не»; noun «большая часть», «большинство»), keeps 大半 as a close substitute and does not ban adverbial «в основном». 大's added guard changes no learner prose. The optional notes stay optional. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness | **No findings** | Review 001 reported none; the recheck found no regression. |
| Correctness optional O1: qualify the 地方:35 «побережье» denial by the reading ちほう | **Resolved** (superseded) | The sentence was deleted for C1; no passage in 地方 presents «побережье». Reviewer accepted. |
| Consistency F1: no 大→巨大 guard | **Resolved** | `大.md:9`; JMdict 1232180; shared «огромный» sense with 莫大 already guarded. Severity unchanged (minor). |
| Consistency optional: 地球–地, 地域–近所, 報告–教える | **Optional, not adopted** | Each mirrors an EN pair without an exact shared title segment; 地 teaches the planet/ground split. Reviewer accepted the decline. |
| Consistency classification of the 14 RU-added candidate entries (11 required, 3 conservative, none unjustified) | **Unchanged** | The recheck kept it; 大→巨大 was added as the F1 remedy. |
| Consistency limit: 38 pre-existing EN-link differences in older cards outside the diff | **No action** | Outside this batch; none targets a batch word. |
| Comprehensibility C1: 地方:35 rejects an English gloss, too absolutely | **Resolved** | `地方.md:34–35`; JMdict and Digital Daijisen じかた sense 3. |
| Comprehensibility C2: 大統領:32 «молодчина!» | **Resolved** (modified wording) | `大統領.md:32`; JMdict 1414650 sense 2; Digital Daijisen 大統領 sense 2. The proposed no-praise contrast was not adopted; reviewer agreed. |
| Comprehensibility C3: 大部分 not separated from ほとんど | **Resolved** (modified wording) | `大部分.md:29`; JMdict 1414850 and ほとんど; Digital Daijisen and Nihon Kokugo Daijiten 大部分 adverbial use. ほとんど kept unlinked for EN link parity. |
| Comprehensibility optional notes (よる:26, 夢中/熱中, 基づく/よる, 報告/レポート, 大戦, 売れる «Мой», 大家, 地域 «округа») | **Optional, not adopted** | Each is inherited from EN or repaired by the following sentence; the reviewer marked them polish and did not promote them. |
| Exclusion classification | **Reviewer differs from author on 6 entries** | The author report announced 15 RU-added pairs but listed the 14 that reached the candidate, calling 5 required; the consistency reviewer also rated 大部分→たいてい, 大半→たいてい, 大→莫大, 大→大小, 外す→下ろす and 報告→リポート required, on the evidence in the independent record. The reviewer's classification is recorded as final. |
| Coordinator retitles before the candidate (大部分, 大半, 報告, 外交) and stress-mark removal | **Reviewed in 001** | All three reviewers judged the candidate titles with no title finding; the new exact segments are guarded. |

Cross-batch note: no link is held for a later batch.

## Final exclusion set

All 18 EN exclusion entries (12 lists) are retained. Fifteen direct, one-sided entries are added on nine new cards:

- Required (12): 大部分→ほとんど, 大部分→たいてい, 大半→ほとんど, 大半→たいてい, 大→莫大, 大→巨大, 大→大小, 夢中→熱中,
  外す→下ろす, 報告→リポート, よる→次第, 地方→州.
- Conservative (3): 境→瞬間, 報告→知らせる, 報告→伝える.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** throughout.
- Scoped coverage: **CLEAN** after fixes (大部分).
- Comprehensibility: **CLEAN** after fixes (地方, 大統領, 大部分).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after fixes (大→巨大), for the reviewed batch and the directly adjudicated pairs. Exclusions are
  direct pairs, not transitive groups.

Limits: the rechecks reread only the changed passages and the cards needed to judge them; unchanged cards rest on review
001's full reading. The consistency reviewer did not re-fetch JMdict or check the linguistic accuracy of the reworded 大統領
and 大部分 passages, which belongs to the correctness facet. The comprehensibility reviewer took the Digital Daijisen and
Nihon Kokugo Daijiten notes from the recheck brief without reopening Kotobank and did not run `tools/validate.py`; the
correctness reviewer reopened those entries. No native-speaker, learner, app-import, device, media, activation or release
acceptance is claimed.
