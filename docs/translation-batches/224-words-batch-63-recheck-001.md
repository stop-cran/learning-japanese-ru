# Batch 224 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `49a8838b1abf3b83582d77fc211ea3915cbf700e` | `53bc3a1a7f1ada5c3e8156209e43a4f516946c34` | Initial review snapshot: the signed candidate, pushed before review. |
| `af84dc1afcae9931311a84a2ed64430d86a0cd8a` | `6dd0f4827c1a46d4450039dea8a3c2d3c4a1c689` | Fix 1 (final candidate). It covers comprehensibility C1–C3, the consistency guard recommendation, both correctness optional items, one comprehensibility optional item and the intake refresh. Signed and pushed before the rechecks. |

Fix 1 changed six word files and regenerated `manifest.json` (`contentVersion` `624d407c656ea3bf`, 4,839 entries; the
candidate had `24168b4b2d433970`) and the intake:
- `とにかく` (line 19; comprehensibility C1 and the correctness optional item, merged, with the correctness reviewer's
  wording): «— Если оставить цену в стороне, качество хорошее.» instead of «Не говоря уже о цене, качество хорошее.», which is
  commonly read additively ("not to mention"). The card's note at line 21 says that Nはとにかく names what is set aside, and
  EN has "Leaving the price aside". JMdict 1443990 sense 2.
- `たっぷり` (lines 18–19; comprehensibility C2, the reviewer's remedies): «— Налейте, пожалуйста, в кастрюлю воды вдоволь.»
  instead of «…побольше воды» ("a little more water"), and «— До отправления времени у нас вдоволь.» instead of «…у нас уйма
  времени», a colloquial overstatement. «Много» was not used, because the card contrasts たっぷり with たくさん «много».
  JMdict 1007240 sense 1; Kuznetsov побольше and уйма; Gramota вдоволь.
- `それぞれ` (line 19; comprehensibility C3, partially accepted): «— Старший брат и младшая сестра живут в Токио и Осаке
  соответственно.» instead of «…живут соответственно в Токио и Осаке», where the mid-sentence word could read as
  "accordingly". The end position is the usual place for «соответственно» after an enumeration, and line 21 already pairs
  the brother with Tokyo and the sister with Osaka. The title, H1 and line 16 gloss «каждый (из нескольких);
  соответственно» are kept: English Wiktionary lists «соответственно» sense 3 "respectively", its "respectively" entry gives
  «соответственно» and «в указанном порядке», and the title mirrors EN "each; respectively" (JMdict 1596690). The reviewer's
  alternative title «каждому своё» is an idiom ("to each his own") with a different meaning and was not adopted.
- `ちゃんと` (line 33; correctness optional item, the reviewer's wording): «Поэтому перевод «идеально, безупречно» может
  преувеличивать: говорящий не обязательно утверждает, что всё сделано без единого изъяна.» instead of the categorical
  «…преувеличивает: говорящий не утверждает…», after EN "can therefore overstate … need not mean".
- `たった` (line 19; comprehensibility optional item): «— До станции можно добраться всего за пять минут.» instead of «…можно
  дойти…», since 着きます and EN "reach" do not specify walking.
- `どんなに` (line 9; consistency recommendation 1): `quiz_exclusions: [いくら, どう]` instead of `[いくら]`. どんなに «как
  сильно; как бы ни» and どう «как; каким образом» share «как», and the card contrasts degree with manner and links どう. The
  EN titles ("how much; no matter how" and "how; in what way") share "how", so the overlap is inherited rather than
  Russian-introduced. The guard is conservative and one-way; Android applies it in both directions.
- The intake note now names the fixed cards, and the six candidate hashes were refreshed.

Comprehensibility C4 (たまらない's title) and C5 (せい's «Категория канго…» sentence) were not adopted; the dispositions
gave the reasons, which the recheck brief put to the reviewer (see the reconciliation table).

No title, H1 or link changed, so the coordinator's title screen and link parity were unchanged from the candidate: no
unguarded exact title-segment overlap, no EN link lost where the RU target exists, and the same nine RU-only links.

Net change from the candidate:
- example translations in とにかく, たっぷり (two), それぞれ and たった;
- one note sentence in ちゃんと;
- one added exclusion entry (どんなに→どう).

No Japanese example sentence was altered, and no sourced reading, EN exclusion or link changed. The content diff is six
word files, 7 lines added and 7 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, one reviewer at a time, all on fix 1, in this order: correctness, consistency, comprehensibility.
No recheck raised a new finding, so no second fix was needed.

Each reviewer appended to its own report file, which stayed in its session context. Each recheck brief gave the reviewer:
- the fix commit, the reviewed candidate as the base, and the read-only rules;
- the actual content diff `49a8838..af84dc1`;
- the coordinator's evidence for every change and the declined items, stated without the other reviewers' reports;
- the reviewer's original verdicts and the disposition of each of its own findings. The comprehensibility brief stated
  the coordinator's reasons for not adopting C4 and C5 and asked the reviewer whether it maintained them. The
  consistency brief asked the reviewer to confirm the coordinator's reading of its required/conservative guard list.

The three briefs were delivered as session files that the reviewers were told to read in full.

Before the briefs were sent, the coordinator corrected one claim in the consistency and comprehensibility briefs (the
correctness recheck had already run): the C5 disposition had said that «канго» is used without a gloss in 29 published RU
files. A case-sensitive recount at the baseline `2a85483` found 27 files (25 word cards and 2 kanji cards), several of
which explain the term in passing (for example `せっけん.md:24` «китайско-японское слово, канго»). The corrected briefs
said that there is no settled no-gloss rule and rested the disposition on EN fidelity and on the preceding sentence's
explanation. The correctness reviewer had independently qualified the original count in its recheck, counting 29 files at
`af84dc1` (27 word cards and 2 kanji cards). A case-insensitive recount for this record reconciles the two: 28 files at the
baseline (26 word cards, including `軍.md:25` with a capitalized «Канго», and 2 kanji cards) and 29 at `af84dc1`, the
addition being `せい.md`. The briefs' 27 missed that one capitalized use; the disposition does not depend on the exact count.

All recheck messages forbade running `tools/build_manifest.py` or any other generator. Every recheck section states that
none was run. The correctness and consistency reviewers each ran `tools/validate.py` (0 errors each); the
comprehensibility reviewer states that it did not run it. The fix script checked `git status --porcelain` after the fix
commit. Before each recheck launch and after the last one, the coordinator confirmed that HEAD was `af84dc1` and that
`git status --porcelain` was empty (with `--ignored` after the last).

### Round 1 (`af84dc1`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer read the changed passages against frozen EN and the relevant dictionary entries. Both optional items are resolved as proposed: the price is now explicitly set aside, and the ちゃんと modal qualification keeps context-dependent standards without claiming that perfection is impossible. The たっぷり, それぞれ and たった changes are supported (Gramota вдоволь; English Wiktionary соответственно sense 3; 着く "reach"). The どんなに guard causes no correctness regression. Within its facets the reviewer found the C4 and C5 withdrawals supported, and it qualified the C5 corpus argument: the «канго» files are not 29 proven unglossed uses, because `せっけん.md:24` glosses the term. Validator 0 errors; no repository file was written. Correctness and scoped coverage are **CLEAN**. |
| Consistency | Snapshot `af84dc1` with an empty status before and after. Recommendation 1 is **resolved**: `どんなに.md` has `quiz_exclusions: [いくら, どう]`, both targets exist, and `どう.md` has no reverse entry. The diff touches six cards, `manifest.json` and the intake; no title, H1 or link line changed, so navigation stays 15 files and 16 links and the nine RU-only links are unchanged. The five prose edits add no link, kana or quiz-relevant label. All `words/` manifest hashes and all 45 intake candidate hashes match the tree. Recomputed against EN: 37 RU-added exclusions on 22 cards and 53 EN exclusions kept, none missing. The reviewer corrected the coordinator's reading of its guard list: the "(conservative)" mark after ただ's three targets applied to サービス only, so ただ→だけ and ただ→ばかり are required, giving 15 conservative and 22 required entries; the mark after それでも's two targets applied to both. Consistency, quiz safety and scoped integration are **CLEAN**. |
| Comprehensibility | The reviewer read the six changed passages and the frozen-EN lines needed for C4, C5 and the ちゃんと note. C1 is resolved: the sentence matches the set-aside note and EN. C2 is resolved: «вдоволь» matches the title and JMdict "plentifully; amply", and «много» is correctly avoided; the word order is slightly inverted but not misleading. C3 is **partially resolved**: the end position and the pairing sentence remove the mid-sentence "accordingly" reading, and the reviewer withdrew its title remedy «каждому своё» and maintains no actionable defect; it notes that English Wiktionary's "respectively" sense is uncited and that Kuznetsov and Russian Wiktionary lack it, while «каждый» and the pairing sentence carry the distinction. C4 is **withdrawn**: the title mirrors EN "unbearable; irresistible", Kuznetsov sense 2 matches the aroma sentence, and the cannot-contain use is taught separately with the て-form. C5 is **withdrawn**: the sentence renders EN, the preceding sentence explains しょい, and a corpus-wide «канго» gloss is an owner convention, not a defect in this card. The たった optional item is resolved. No regression in ちゃんと or in どんなに's prose. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness optional: とにかく «Не говоря уже о цене» | **Optional, adopted** (jointly with comprehensibility C1) | `とにかく.md:19`; JMdict 1443990 sense 2. |
| Correctness optional: ちゃんと's categorical «преувеличивает: … не утверждает» | **Optional, adopted** | `ちゃんと.md:33`; frozen EN "can therefore overstate … need not mean". |
| Consistency recommendation 1: どんなに–どう guard (minor) | **Resolved** | `どんなに.md:9`; titles «как сильно; как бы ни» and «как; каким образом». |
| Consistency optional: なにも–全然 and 全く, ずっと–ずいぶん, しきりに–よく, しまった–失敗 | **Optional, not adopted** | The reviewer called them weak; the titles separate them and the cards teach the contrasts. |
| Comprehensibility C1: とにかく reads additively (moderate) | **Resolved** | `とにかく.md:19,21`. |
| Comprehensibility C2: たっぷり «побольше воды» and «уйма времени» (moderate) | **Resolved** | `たっぷり.md:18–19`; JMdict 1007240 sense 1; Kuznetsov побольше and уйма; Gramota вдоволь. |
| Comprehensibility C3: それぞれ «соответственно» (moderate) | **Partially resolved**; no actionable defect remains | `それぞれ.md:19,21`; English Wiktionary соответственно sense 3 and "respectively"; JMdict 1596690. The title is kept; the reviewer withdrew its title remedy. |
| Comprehensibility C4: たまらない «неотразимый» narrower than the cannot-contain use (minor) | **Withdrawn** by the reviewer at recheck | `たまらない.md:4,11,20,32`; frozen EN "unbearable; irresistible"; JMdict 1211340 senses 1–3; Kuznetsov неотразимый sense 2. |
| Comprehensibility C5: せい «Категория канго…» author-facing (minor) | **Withdrawn** by the reviewer at recheck | `せい.md:26–27`; frozen EN "The `kango` classification follows that analysis without treating the proposed origin as certain"; 精選版 日本国語大辞典 on Kotobank. |
| Comprehensibility optional: たった «можно дойти» | **Optional, adopted** | `たった.md:19`. |
| Comprehensibility optional: a parenthetical for ちゃんと «исправно» | **Optional, not adopted** | It would change the title; JMdict 1007720 sense 2 includes "in good condition; regularly; properly", and line 16 adds «с должной внимательностью». The reviewer kept it optional. |
| Comprehensibility observations on そのまま, たまたま, ところで, そこで, しきりに, the атэдзи notes, the verb classes and the held links | **No action needed** | The reviewer found each already qualified or consistent. |
| Exclusion classification | **Reviewer's classification adopted** | The author's and the consistency reviewer's classifications differ only in strength (table in review 001); the reviewer rates fourteen author-"conservative" or unmarked entries as required. The fix entry どんなに→どう is conservative, as the dispositions had it; the reviewer confirmed the 15/22 split at recheck. |

Cross-batch note: links to absent targets stay plain. Two EN link targets in this batch's new cards are absent from RU:
ごめんなさい and ありがとう (both from すみません). The きちんと→ちゃんと and ところが→ところで links held by Batch 223 were
restored in this batch.

## Final exclusion set

All 53 EN exclusion entries (18 lists) are retained. Thirty-seven direct, one-sided entries are added on 22 new cards (nine
of them new lists: すみません, せい, そのまま, できれば, とにかく, とんでもない, どうしても, どこか and なにも):

- Required (22): どうしても→なかなか and 絶対, とんでもない→いえ, とにかく→何とか, そのまま→まま, すみません→申し訳, どうも and
  謝る, しゃべる→ぺらぺら, べらべら and おしゃべり, しかも→更に, すてき→見事 and かわいい, ずっと→年中, せい→悪い, ただ→だけ and
  ばかり, たった→だけ, できれば→なるべく, and どこか→どこ and 辺り.
- Conservative (15): さて→ところで, しきりに→しばしば, せい→原因, それでも→しかし and でも, それと→それから, ただ→サービス,
  たっぷり→十分, たまたま→たまに, とんでもない→ひどい and 凄い, どうしても→ぜひ and 必ず, なにも→別に and, added in fix 1,
  どんなに→どう.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** throughout (two optional items adopted).
- Scoped coverage: **CLEAN** throughout.
- Comprehensibility: **CLEAN** after the fix (とにかく, たっぷり, それぞれ); C4 and C5 withdrawn by the reviewer.
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN**, including the fix-1 entry on どんなに. This covers the reviewed batch and the directly adjudicated
  pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them. The unchanged cards rest on review
  001's full reading.
- The "respectively" sense of «соответственно» rests on English Wiktionary (uncited) and on ordinary Russian use after
  enumerations; Kuznetsov and Russian Wiktionary do not list it separately. No native certification was obtained.
- Whether to gloss «канго» corpus-wide is left to the owner. At the baseline, 28 published files use the term (29 at
  `af84dc1`, with `せい.md`), some as a bare category name (`だめ.md:33`, `御礼.md:31`, `曲.md:24`) and some with a passing
  explanation (`せっけん.md:24`, `絵.md:30`, `十.md:22`). This count is a case-insensitive search for the term, not a
  review of each card.
- The author did not look up its Russian glosses in a dictionary; the correctness reviewer verified the flagged ones.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
