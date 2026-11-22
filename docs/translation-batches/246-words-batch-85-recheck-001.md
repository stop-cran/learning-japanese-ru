# Batch 246 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `008ef28b7b8bb7986f863bea017c0e0e8165a058` | `75d0f14a1b55fc23d71f03565846f577eae947fd` | Initial review snapshot: the signed candidate, on `origin/full-ru-246-words-85`. |
| `c1767c6f40b555fbaac3c1c619d2e95a84dfd481` | `8445ed50bb459b78ac43bc5ab67fd71a45385d27` | Fix 1 (final candidate). It covers correctness Q1, the correctness optional on 破く's title aspect, and comprehensibility C1 to C5 (C1, C3 and C4 with modification). It retitles 破く and 破片, rewrites example translations and prose in 短所, 破く, 破片, 睨む and 短編, changes the quoted gloss on the navigation-only file 長所:31, adds one exclusion and changes no link. Signed; on `origin/full-ru-246-words-85`. |

The fix regenerated `manifest.json`; both snapshots record 5,499 entries (5,494 `files` + 3 images + 2 scenes).
`contentVersion` is `31859f0c07e58ed7` at the candidate and `cc9db27bbbea5cc7` after fix 1. The intake was not
refreshed; it still records the candidate's payload hashes. The commit message reads "Batch 246 fix 1: apply review
dispositions", followed by "Comprehensibility C1-C5 and correctness Q1 on candidate 008ef28:" and one bullet each for
短所/長所, 破く, 破片, 睨む, 短編 and 湯飲み.

Fix 1:
- `短所` (lines 16–18, 20, 23–24, 34 and 41; comprehensibility C1, with modification): the meaning line reads «短所 —
  отрицательная сторона или минус. … а также к минусам вещи или плана.» and the pattern line «**Nの短所** — «минусы N»,
  «отрицательные стороны N».» instead of «短所 — недостаток, слабая сторона или минус. … а также к недостаткам вещи или
  плана.» and «**Nの短所** — «недостатки N».»; the example reads «Мой минус в том, что я легко теряюсь.» instead of «Мой
  недостаток…»; lines 23–24 read «называется минусом.» and «есть минус» instead of «называется недостатком.» and «есть
  недостаток»; line 34 glosses 欠点 «недостаток; слабая сторона» (its own title) instead of «изъян, слабое место»; line
  41 opens «短所 не обязательно означает полную неспособность или недавнюю ошибку.» instead of «Недостаток не
  обязательно означает…». The title «отрицательная сторона; минус» is unchanged.
- `長所` (line 31; comprehensibility C1; navigation-only file): «[短所](短所.md)（たんしょ）— «отрицательная сторона;
  минус» — прямая противоположность.» instead of «…— «недостаток, слабая сторона» — прямая противоположность.» The link
  and brackets are unchanged.
- `破く` (lines 4, 12 and 16; comprehensibility C2 and the correctness optional): title and H1 «рвать; разрывать
  (бумагу, ткань)» instead of «порвать; разорвать»; «破く значит рвать или разрывать что-либо, например бумагу или
  ткань. Это переходный глагол-годан;» instead of «破く значит порвать или разорвать…». The paragraph breaks restored by
  the coordinator are intact, and the past example translations keep «порвал»/«разорвал».
- `破片` (lines 4, 12 and 16–17; comprehensibility C3, with modification): title and H1 «осколок; обломок» instead of
  «осколок; обломок; щепка»; «破片 — осколок или обломок: кусок разбитого стекла или керамики, деревянная щепка или
  другая часть, оставшаяся после того, как что-то разбилось или сломалось. Это существительное.» instead of «破片 —
  осколок или обломок: кусок стекла, щепка или часть, оставшаяся…».
- `睨む` (line 22; comprehensibility C4, with modification): «— За ним с подозрением следит полиция.» instead of «—
  Полиция подозревает его и следит за ним.»
- `短編` (lines 19 and 22; comprehensibility C5, verbatim): «— Перед сном я прочитал один короткий рассказ.» instead of
  «…один рассказ.»; «短編小説（たんぺんしょうせつ）прямо означает «короткий рассказ»;» instead of «…«рассказ, новелла»;».
- `湯飲み` (line 9; correctness Q1, verbatim): `quiz_exclusions: [カップ, ちゃわん]` instead of `[カップ]`.

Six are new Batch 246 cards; 長所 is a navigation-only file published in Batch 230. Navigation totals stay at 9 files /
21 links, all EN-position restorations; fix 1 changed only the quoted gloss on 長所:31.

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Comprehensibility C1 was accepted with modification. "Not adopted: «а не имя любого изъяна», which would add a
  distinction not made by EN or JMdict 1418760 (EN says the words overlap; the quiz already excludes 欠点). «Минус» in
  this sense is colloquial-neutral Russian (Gramota, Kuznetsov sense 4, per the correctness review); the title still
  leads with the neutral «отрицательная сторона»." At recheck the reviewer judged that dropping that clause "does not
  restore the collision".
- Comprehensibility C3 was accepted with modification: "Line 16 keeps EN's "splinter" coverage but scopes it to wood".
- Comprehensibility C4 was accepted with modification: the new sentence "keeps him as the topic, as in the passive, and
  drops 疑う's quiz verb «подозревает». The suggested «под подозрительным наблюдением» was not used because
  «подозрительный» would describe the watching as suspicious-looking."
- The correctness optional on imperfective titles was adopted for 破く (with C2) and declined for 破れる: "«порваться;
  протереться; сорваться» is clearer than imperfective «рваться; срываться», which also mean "be eager" / "break loose";
  the comprehensibility reviewer read 破れる in full and raised nothing." At recheck the correctness reviewer recorded
  "Title-aspect suggestion PARTIALLY RESOLVED: 破く RESOLVED; unchanged 破れる OPTIONAL".
- Consistency O1 (append 知り合い to 知人) was declined: "Android's word quiz already rejects any distractor whose title
  equals the target's or an already chosen option's title (`kanji-cards-android` origin/main
  `core/.../words/Words.kt:180,185,188`: `usedTitles` seeded with `target.title`), so the two cards cannot appear
  together as answer and distractor. The reviewer listed the client behaviour as unverified; the correctness reviewer
  independently relied on the same documented contract. EN parity is kept." The consistency recheck left O1
  "UNRESOLVED, still optional".
- Consistency O2 needed no action ("plain EN links without RU targets; RU-only links resolve — no action.").
- The comprehensibility optionals were declined or needed no action: 潰れる's title ("It is faithful to EN "be crushed; go
  out of business", and line 46 already explains the passive-looking Russian."); the 椀/碗 counter gloss ("A shorter
  «счёт мисок» would blur counting bowls with counting bowlfuls."); 矢印:28, くるむ:31 and the terms годан/итидан/окуригана
  ("These are EN-parity sentences or terms already used throughout the published RU deck; none teaches a wrong
  meaning."); «вместилище» and «конфронтация» ("The reviewer judged them acceptable, and each card also gives a plain
  gloss."). The other correctness optionals (first-use definitions, trimming contributor-oriented sentences, a «разг.»
  mark on «минус») were not implemented and remain optional.

Post-fix screen: a saved rerun at the committed `c1767c6` over all 30 batch words (`b246-postfix-screen.txt`, 232 lines)
has 38 `OK` lines for pairs already guarded by an exclusion and 194 `!!` lines. Its exact-segment lines are 椀–ボール
«миска», 椀–碗 «миска» and «счётное слово для порций в мисках», 碗–ボール «миска» and 破く–破る «рвать» and «разрывать»,
all guarded by the batch cards' own lists (椀→ボール and 碗, 碗→ボール and 椀, 破く→破る), and the unguarded 知り合い–知人
«знакомый» (consistency O1, declined). Against the candidate screen (223 lines) it adds 11 lines and removes 2, all from
the 破く title change: added `OK` 千切る–破く, 破く–びりびり and 破く–破る and `!!` stem-only 破く–切れる, 差, 布, 書類,
生地, 紙, 組織 and 絞る; removed `!!` 潰れる–破く and `OK` 破く–破れる. The dispositions record: "破く's new stem matches
(紙, 布, 書類, 生地, 組織, 絞る, 差, 切れる) are topical, or the titles already separate them (noun vs verb,
intransitive «рваться»), so no guard was added." The consistency recheck found that "No other title has the exact pair
«рвать; разрывать»" and that no other title shares 破片's «осколок» or «обломок».

Net change from the candidate:
- titles and H1s of 破く and 破片;
- example translations in 短所, 睨む and 短編;
- prose in 短所 (meaning, pattern, notes, the 欠点 comparison and line 41), 破く (line 16), 破片 (lines 16–17), 短編
  (line 22) and 長所 (line 31, quoted gloss only);
- one exclusion added (湯飲み→ちゃわん);
- no link added, removed or retargeted.

No Japanese example sentence, sourced reading, kanji card, EN exclusion or link target changed. The content diff
`008ef28..c1767c6 -- words` is 7 word files, 20 lines added and 20 removed; with `manifest.json` the fix changes 8
files, 28 lines added and 28 removed.

Fix 1 validation, as recorded in the dispositions: "`tools/validate.py` 0 errors; manifest rebuilt (5,499 entries =
5,494 files + 3 images + 2 scenes); 124 unit tests OK; `git diff --check` clean; link parity unchanged from the
candidate (only the three reviewed RU-only links 湯飲み→ちゃわん, 知り合い→知人 and 短所→長所, plus the two pre-existing
kanji/短 extras 知 and 短い); title screen: 破片 has no overlaps." For this record link parity was verified again over
the 39 batch paths at `c1767c6`: in the 30 new cards the only EN links missing from RU are the eight plain-text
occurrences to absent targets listed in the cross-batch note, and the only extras are the three reviewed RU-only links;
the navigation files' remaining differences from EN (kanji/短 → kanji/知 and words/短い, kanji/印 → words/印, and EN
links to the absent words 包帯, 包丁 and 寝間着 and kanji 矛) already exist at the baseline `1608f45`.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the correctness recheck states "Model identity not independently verifiable.", the consistency recheck "Model
identity is not stated." and the comprehensibility recheck "Model: not verifiable from this session."; the dispositions
label each reviewer's model "per runtime status".

The rechecks ran serially, one reviewer at a time, in one round: comprehensibility, then correctness, then consistency,
each on the fix diff `008ef28..c1767c6` (7 word files and `manifest.json`). This ordering rests on the coordinator's
session records; the recheck reports do not record times. There was no second fix and no follow-up exchange.

Rechecks were returned as separate reports rather than appended to the initial review files: the full texts are in
`b246-recheck-correctness.md`, `b246-recheck-consistency.md` and `b246-recheck-comprehensibility.md` in the
coordinator's session folder, and their content is recorded in the round table below. The recheck briefs were sent
through the agent-messaging channel and were not saved as files; each recheck's scope is described here from its own
Snapshot and Scope lines.

No recheck ran a generator. The correctness reviewer records "Read-only; only this report written." and "No generators,
repository writes or full validator/unit-test reruns; coordinator tests are not independent evidence."; the consistency
reviewer ran `python -B tools/validate.py` (0 errors) and records "The generator was not run."; the comprehensibility
reviewer records "No generators run." The correctness recheck records HEAD `c1767c6f40b555fbaac3c1c619d2e95a84dfd481`
and parent `008ef28b7b8bb7986f863bea017c0e0e8165a058` with "Initial/final status --porcelain empty"; the consistency
recheck records `c1767c6f40b555fbaac3c1c619d2e95a84dfd481` with "`git status --porcelain` empty; no __pycache__ in the
tree"; the comprehensibility recheck records `c1767c6f40b555fbaac3c1c619d2e95a84dfd481` ("`git rev-parse HEAD`
matches"), parent `008ef28b7b8bb7986f863bea017c0e0e8165a058` and "`git status --porcelain` empty". The untracked
`tools/__pycache__/` that the initial comprehensibility review recorded had been removed by the coordinator before fix 1;
its cause was not established. When these records were drafted, a read-only check showed the RU checkout at HEAD
`c1767c6f40b555fbaac3c1c619d2e95a84dfd481` with `git status --porcelain --ignored` printing nothing.

### Round 1 (`c1767c6`)

| Facet | Scope and result |
|---|---|
| Comprehensibility | HEAD `c1767c6`, parent `008ef28`, porcelain empty. "recheck of comprehensibility and scoped coverage only. Judged the fix diff and the changed text in `words/短所.md`, `長所.md:31`, `破く.md`, `破片.md`, `睨む.md`, `短編.md`, and `湯飲み.md` front matter." C1 to C5 **resolved**: C1 "Dropping «а не имя любого изъяна» does not restore the collision."; C2 "The parenthetical repeats the card's own scope and does not revive the aspect mix-up with 破る."; C3 "«Щепка» is no longer a quiz gloss; in the body it is scoped as `деревянная щепка`"; C4 "`За ним с подозрением следит полиция.` is natural, keeps him as the topic … Active Russian for a Japanese passive with a named agent is not a new defect."; C5 "Shortness is back in the sentence a learner would use as proof." "No new comprehensibility or scoped-coverage defect in the changed passages." Optional: "unchanged and still nonblocking". Verdicts: "Comprehensibility: CLEAN. Scoped coverage: CLEAN." Limits: "recheck of the fix, not a fresh read of all 30 cards. `manifest.json` not reviewed as prose. No generators run." |
| Correctness | Snapshot `c1767c6` against parent `008ef28`, "Initial/final status --porcelain empty". "all seven revised RU cards and frozen EN counterparts in full: words/{短所,長所,破く,破片,睨む,短編,湯飲み}.md. Existing RU ちゃわん also read fully. Every changed passage independently checked." "Q1 — RESOLVED, high confidence." (JMdict 1597530 sense 1 "rice bowl; tea cup; teacup"; 1612130 "teacup"; "The direct overlap is real, not inferred transitively through カップ."). Changed passages judged correct: 短所 and 長所:31 (JMdict 1418760/1430030 sense 1); 破く ("These are transitive imperfective glosses of the dictionary verb"; JMdict 1983750 sense 1; Daijisen やぶく "紙や布などを、引き裂く。破る"; "The direct 破く–破る exclusion remains justified by their tearing overlap."); 破片 ("removing “щепка” from the short title does not remove EN splinter coverage"; JMdict 1471420); 睨む:22 ("Russian active syntax does not reverse the Japanese passive"; JMdict 1569880 sense 4; Daijisen にらむ sense 4); 短編:19,22 (JMdict 1597300; "No sense loss."). "all seven cards' Japanese example sentences and complete kana readings equal frozen EN"; "No Japanese examples, readings, citations, links, classifications or existing guards were removed by fix 1." "this recheck's dictionary-filtered request returned HTTP 429, so no new successful Gramota access is claimed." Correctness **CLEAN**; scoped coverage **CLEAN** "for batch 246 at c1767c6. No per-article exception." "Findings: None new in the assigned facets." Optional: "Title-aspect suggestion PARTIALLY RESOLVED: 破く RESOLVED; unchanged 破れる OPTIONAL, its perfective change-of-state glosses still correct." The other optionals "remain OPTIONAL, unimplemented and nonblocking." Limits: "Delta recheck, not a corpus-wide quiz audit, native-speaker assessment or client/manifest acceptance; original unchanged-scope limits remain." |
| Consistency | `c1767c6`, `git status --porcelain` empty; `python -B tools/validate.py` 0 errors. "Read in full: the whole fix diff (`git diff -U1 008ef28 c1767c6 -- words`), the manifest diff, the front matter of the affected and neighbouring cards. Searched all RU word titles for the changed segments and stems." Coverage/links/navigation, duplicates and conflicts, distractors/quiz_exclusions, tags and metadata, manifest/generated files and formatting/H1-title agreement **CLEAN**; "UNVERIFIED: app-side title dedupe (unchanged limit)." "O1 … UNRESOLVED, still optional."; "O2 … WITHDRAWN as a concern, informational only. The fix adds no link and removes none."; 破く→破る "RESOLVED/still required, and now more necessary (see F1)" (the report contains no item labelled F1; its 破く check states that "the stems are now identical"); 湯飲み→ちゃわん "conservative, defensible … Not required."; 長所:31 "only the quoted gloss changed … The link and brackets are unchanged. Navigation is still 9 files / 21 links"; "all 7 changed entries match the SHA-256 of the committed file (CRLF-normalised). The diff changes only contentVersion (31859f0c07e58ed7 → cc9db27bbbea5cc7) and those 7 lines." "No new defects. Nothing is NEEDS FIX." Optional: O1, and "ちゃわん could reciprocate 湯飲み: not required, because the exclusion is applied symmetrically, and it would change an earlier-batch card." Limits: "Model identity is not stated. App title dedupe is not verified. Linguistic correctness is outside my facet." |

No recheck raised a new finding, so there was no second fix.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness Q1: no direct 湯飲み–ちゃわん exclusion (outside its facets; medium learning impact) | **Resolved** | `湯飲み.md:9`; JMdict 1597530 sense 1, 1612130; consistency recheck "conservative, defensible … Not required". |
| Correctness optional: imperfective 破く/破れる titles | **Partially resolved**; 破れる optional | `破く.md:4,12,16`; correctness recheck "破く RESOLVED; unchanged 破れる OPTIONAL". |
| Correctness optionals: first-use term definitions, contributor-oriented sentences, «разг.» on «минус» | **Optional**; no change | Correctness recheck "remain OPTIONAL, unimplemented and nonblocking". |
| Consistency classification of 破く→破る ("required") | **Recorded**; retained | See the final exclusion set; consistency recheck "RESOLVED/still required". |
| Consistency O1: 知人/知り合い identical title without an exclusion (optional, low) | **Optional**; declined (EN parity, client title deduplication) | Consistency recheck "UNRESOLVED, still optional"; client behaviour unverified by the reviewers. |
| Consistency O2: plain EN links and RU-only links (information) | **Withdrawn** | Consistency recheck "WITHDRAWN as a concern, informational only". |
| RU-only links 湯飲み:34 → ちゃわん, 短所:37 → 長所, 知り合い:34 → 知人 (candidate) | **No action**; acceptable | Correctness review "their claims fit the target meanings"; consistency review "all resolve. Nothing to fix." |
| Comprehensibility C1: 短所 body and 長所:31 use 欠点's title (medium) | **Resolved** (with modification) | `短所.md:16–18,20,23–24,34,41`; `長所.md:31`; JMdict 1418760/1430030. |
| Comprehensibility C2: perfective 破く title (medium) | **Resolved** | `破く.md:4,12,16`; JMdict 1983750; Daijisen やぶく. |
| Comprehensibility C3: «щепка» in 破片's title (medium) | **Resolved** (with modification) | `破片.md:4,12,16–17`; JMdict 1471420. |
| Comprehensibility C4: 睨む:22 uses 疑う's «подозревает» (medium) | **Resolved** (with modification) | `睨む.md:22`; JMdict 1569880 sense 4; Daijisen にらむ sense 4. |
| Comprehensibility C5: 短編 example drops shortness (medium; scoped coverage) | **Resolved** | `短編.md:19,22`; JMdict 1597300. |
| Comprehensibility optionals: 潰れる title, 椀/碗 counter gloss, 矢印:28, くるむ:31, «вместилище», «конфронтация» | **Optional**; declined or no action, non-blocking | Comprehensibility recheck "unchanged and still nonblocking". |
| Coordinator's unverified Russian register («вместилище» bookish, «минус» colloquial) | **UNVERIFIED**; not defects | Correctness review found no bookish label for «вместилище» in Kuznetsov and Kuznetsov sense 4 colloquial for «минус»; the correctness recheck's Gramota request returned HTTP 429. |
| Untracked `tools/__pycache__/` at the initial comprehensibility review | **Removed** by the coordinator before fix 1; cause not established | All three recheck reports record an empty status. |

Cross-batch note: links to absent targets stay plain. Eight EN link occurrences in this batch's new cards, to 8
targets, are absent from RU: words 潰す (from 潰れる), 名所 (from 目印) and 対照 (from 対立), and kanji 湯 (from 湯飲み), 装
(from 包装), 片 (from 破片), 編 (from 短編) and 矛 (from 矛盾). The other written kanji without an RU kanji card, 修, 器,
崩, 椀, 潰, 盾, 睨, 瞳, 矢, 砕, 碁 and 碗, have none in EN either. No EN link to an existing card is dropped. There are three
reviewed RU-only links to existing cards, all present at the candidate at substantive comparisons where EN has plain
text: 湯飲み:34 → ちゃわん, 短所:37 → 長所 and 知り合い:34 → 知人. No link was held from an earlier batch, and none is held
for a later one. Exclusions that the coordinator recorded as depending on earlier lane drafts (崩れる/砕ける→下降,
目印→気配, 目印/矢印→標識/符号) and 研修→稽古 resolve to cards published at the baseline.

## Final exclusion set

All 212 EN exclusion entries (29 lists; EN has none on 碁) are retained in EN order; 31 of them lie inside the batch, and
the other 181 target existing RU cards. Two direct, one-sided entries are added on two new cards, both appended at the
end of their lists; neither targets a batch word. One was present at the candidate and one was added by fix 1.

- Candidate (1), accepted by the coordinator as "required": 破く→破る (破る «рвать; разрывать»). 破く's final list is
  `[破れる, 裂く, 千切る, びりびり, ばりばり, 破る]`.
- Fix 1 (1): 湯飲み→ちゃわん (ちゃわん «миска для риса»; correctness Q1). 湯飲み's final list is `[カップ, ちゃわん]`.

The consistency reviewer classed 破く→破る as "required" at review and "RESOLVED/still required" at recheck, after 破く's
retitle made the two titles share both stems; it classed 湯飲み→ちゃわん at recheck as "conservative, defensible … Not
required". 知人 and 知り合い keep the identical title «знакомый» without an exclusion, as in EN (O1, declined). The
guarded exact-segment pairs in the post-fix screen are covered by the batch cards' own lists (椀→ボール and 碗, 碗→ボール
and 椀, 破く→破る). Every RU addition is appended at the end of its list, and no EN entry is removed or reordered. Android
applies each declaration symmetrically (EN `docs/content-format.md`, lines 162–165), so no reverse declarations were
added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** throughout (no finding in its facets at review; CLEAN at recheck).
- Scoped coverage: **CLEAN** after fix 1 in the comprehensibility recheck (短編 C5); CLEAN throughout in the correctness
  review and recheck.
- Comprehensibility: **CLEAN** after fix 1 (短所, 長所:31, 破く, 破片 and 睨む); the modified dispositions of C1, C3 and C4
  stand as accepted.
- Cross-file consistency: **CLEAN** throughout; the 21 restored navigation links in nine files (with 長所:31's gloss
  updated by fix 1) and the three reviewed RU-only links stand.
- Quiz safety: **CLEAN** after fix 1 (湯飲み→ちゃわん added; 破く→破る retained after the retitle), including the two
  retitles. 知人/知り合い remain unguarded, as in EN, on the client's exact-title deduplication, which the reviewers did
  not verify. This covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

## Limits

- The rechecks reread the changed cards or passages and the lines needed to judge them; the unchanged cards rest on review
  001, in which all three reviewers read all 30 cards in full against EN. The comprehensibility recheck was "not a fresh
  read of all 30 cards".
- The correctness reviewer's recheck was a delta recheck with no generator or full validator/unit-test rerun; its
  initial review met an HTTP 403 from kanjiapi.dev (replaced by KANJIDIC2), and its recheck's Gramota request returned
  HTTP 429. The comprehensibility reviewer could not fetch JMdictDB and cited JMdict senses from the Jisho API, and it did
  not read all related cards in full. The consistency reviewer did not audit pre-existing prose in older navigation cards
  beyond the changed links, and neither consistency report verified the app's title deduplication. Necessity classes are
  judgements, not measurements.
- The cause of the untracked `tools/__pycache__/` recorded by the initial comprehensibility review was not established.
- The recheck briefs were not saved as files; each recheck's scope is taken from its own report.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fix, so its payload hashes describe the candidate `008ef28`, not `c1767c6`.
- Frequency and preferred register (for example «вместилище», «минус», «конфронтация», «отрицательная сторона» and
  «рвать; разрывать (бумагу, ткань)») were not certified. Online dictionaries were current observations, not pinned
  archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
