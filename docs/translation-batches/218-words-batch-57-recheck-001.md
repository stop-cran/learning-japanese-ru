# Batch 218 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `4cc28f4411ca8c4cc1d94c5a7cfc02e25752f746` | `b193110e748f6063dcdcc5a24c49e17bffecd066` | Initial review snapshot: the signed candidate, pushed before review. |
| `d45ff3275fed1596df9749c5f73f0afe139cb7fe` | `b884ae59f7775d12a2a9e50dfd88c0dfb8640e40` | Fix 1. It covers the correctness finding, both consistency findings, both comprehensibility findings, three adopted consistency optional items, one adopted correctness optional item and the intake refresh. Signed and pushed before the first recheck. |
| `867e749a0faa4e51ecb7a1014f271a1a8917f1b5` | `c3f144691e13e438a987e8900164eb8d4a381f15` | Fix 2. It qualifies the register of «антракт» in 休憩 after the first correctness recheck, and refreshes the manifest and intake. Signed and pushed before the next rechecks. |
| `40e30b5961c44f4d1e8836d29cd65b4d3755396e` | `3526015c1b950f9d49f74966acd796ad7e992534` | Fix 3 (final candidate). It removes an English gloss from 以来's note after the first comprehensibility recheck, and refreshes the manifest and intake. Signed and pushed before the final rechecks. |

Together the fixes changed nine word files and regenerated `manifest.json` (`contentVersion` `9bd4efcc2f80dfbe`, 4,659
entries; fix 1 produced `653f6b0be469a931` and fix 2 `1c1766e061ca96de`) and the intake:
- `余分` (line 24): «Онные чтения складываются как よ + ぶん.» instead of «…как ヨ + ブン.» (correctness F1, as proposed).
  EN `余分.md:29` joins the readings in hiragana; JMdict 1544520 (よぶん).
- `休憩` (lines 4 and 12): title and H1 «перерыв на отдых; антракт (в спектакле, концерте)» instead of «перерыв; антракт»
  (comprehensibility C1, adapted).
  - C1 proposed the title «перерыв» alone. EN's title is "rest break; intermission", so the title keeps both parts and
    restricts the second.
  - Evidence: JMdict 1227720 sense 1 (rest, break, recess, intermission); Russian Wiktionary marks «антракт» theatrical.
- `休憩` (line 33): the «Оттенки значения» section adds «В спектакле или на концерте такой перерыв по-русски называют
  «антракт»; на совещании или в пути в нейтральной речи говорят «перерыв», а «антракт» там звучит разговорно.»
  - Fix 1 added C1's contrast as «…на совещании или в пути это обычный «перерыв», а не антракт.»
  - Fix 2 qualified that clause (correctness recheck R1): Kuznetsov «антракт» sense 1 records «Разг. Перерыв в
    каком-либо действии, процессе», so a conversational general break is attested and must not be excluded outright.
- `何とか` (line 17): «Я спешил и с трудом, но успел вовремя.» instead of «Я спешил и кое-как успел вовремя.»
  (comprehensibility C2, adapted by adding «но»). Russian Wiktionary «кое-как» sense 1 is «плохо, небрежно», which JMdict
  1188420 does not give 何とか; EN "somehow managed to make it in time".
- `以来` (line 33): «Словарь приводит для 以来 и перевод «отныне», но это не разрешение заменять словом 以来 любое
  выражение будущего.» The candidate read «Не считайте словарный перевод «впредь» разрешением заменять 以来 любое выражение
  будущего.»
  - Fix 1 adopted the correctness optional item: the card never showed the warned-against «впредь», so the note now names
    the dictionary rendering it qualifies. «Отныне» also avoids reusing 今後's «впредь». Evidence: JMdict 1155210 sense 1
    "since; henceforth"; Kuznetsov [отныне](https://gramota.ru/meta/otnyne) «начиная с настоящего времени; впредь».
  - Fix 1's wording added «(англ. henceforth)» and «заменять им». Fix 3 (comprehensibility recheck R1) removed the English
    gloss from the learner prose and replaced the ambiguous «им» with «словом 以来», as EN line 33 says "replace every
    future expression with 以来".
- `例え` (line 9): `quiz_exclusions: [例, 比較]` (consistency Q1). 例え «пример (для пояснения); образное сравнение»
  contains the whole title of 比較 «сравнение»; JMdict 例え sense 2 "simile; metaphor".
- `任せる` (line 9): `quiz_exclusions: [預ける, 頼む]` (consistency Q2). 任せる «вверять (дело); оставлять на (чьё-л.)
  усмотрение» against 頼む «просить; поручать»; JMdict 頼む has "to entrust to".
- `住民` (line 9): `quiz_exclusions: [市民, 人口]` (consistency optional, adopted as conservative). 住民 «жители; житель»
  against 人口 «население»; the published 市民 already excludes 人口.
- `仲間` (line 9): `quiz_exclusions: [友, 連れ, 同僚, 友達]` (consistency optional, adopted as conservative). 仲間 «товарищ;
  член группы» against 友達 «друг»; 仲間 already excludes 友 «друг; спутник».
- `会員` (line 9): `quiz_exclusions: [仲間]` (consistency optional, adopted as conservative). 会員 «член (клуба,
  общества)» and 仲間 «товарищ; член группы» both offer «член»; EN メンバー excludes both 会員 and 仲間.
- The intake note now names the fixed cards, and the nine candidate hashes were refreshed.

Net change from the candidate: one reading-join correction back to EN's kana (余分), one retitle with one nuance sentence
(休憩), two prose edits (以来, 何とか) and five added exclusion entries on five cards. No Japanese example sentence, sourced
reading, EN exclusion or link changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, one reviewer at a time, in three rounds:
1. correctness on fix 1;
2. correctness, then consistency, then comprehensibility, on fix 2;
3. comprehensibility, then correctness, then consistency, on fix 3.

Each reviewer appended to its own report file, which stayed in its session context. The first recheck message to each reviewer
gave it:
- the fix commits, the reviewed candidate as fix 1's parent, and the read-only rules;
- the actual content diff from `4cc28f4` to the fix under review, inline;
- the coordinator's evidence for every change, including the declined and withdrawn items, stated without the other
  reviewers' reports;
- the coordinator's disposition of each of its own findings.

Later recheck messages gave the new fix commit, its actual diff or the `git diff` command for it, the changed sentence with its
evidence, and the disposition of the finding it answered.

The first correctness recheck brief reversed the reviewer's original verdict attribution. The reviewer corrected it in its
recheck: the original verdicts were correctness CLEAN and scoped coverage NEEDS FIX (F1). Review 001 records the corrected
attribution.

All recheck messages forbade running `tools/build_manifest.py` or any other generator, and every recheck section states that
none was run. The correctness reviewer ran `tools/validate.py` in its first recheck and the consistency reviewer in both of
its rechecks (0 errors each time); the other rechecks report no validator run. After every recheck the coordinator confirmed
that HEAD was unchanged and that `git status --porcelain --ignored` was empty.

### Round 1 (`d45ff32`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer inspected the actual `4cc28f4..d45ff32` diff of all nine changed cards and reread the revised 以来, 休憩 and 何とか with their EN originals. F1 is resolved: 余分:24 keeps よ + ぶん and labels them on readings. The 以来 optional item is resolved: live JMdict sense 1 lists "since; henceforth", and Kuznetsov «отныне» supports the rendering; the past-anchor guidance is intact. 何とか:17 keeps successful arrival despite difficulty without asserting carelessness. 休憩's title and H1 preserve EN "rest break; intermission", and the theatrical/concert restriction is valid for neutral Russian. The added guards lose no source sense or Japanese text. It raised **R1** (minor; high confidence in the evidence), `休憩.md:33`: «на совещании или в пути … не антракт» excluded the conversational sense that Kuznetsov «антракт» 1 records («Разг.»). Verdicts: correctness **NEEDS FIX** (R1); scoped coverage **CLEAN**. |

### Round 2 (`867e749`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer confirmed that the `d45ff32..867e749` word diff contains only 休憩:33, and read the complete card. R1 is resolved: the sentence now distinguishes neutral «перерыв» from conversational «антракт» outside a performance instead of excluding it, as Kuznetsov sense 1 records; the Russian is natural, and the meeting example still uses «перерыв». Correctness and scoped coverage are **CLEAN**, with no new findings. |
| Consistency | The reviewer confirmed that the diff from `4cc28f4` touches nine word cards, the manifest and the intake. Q1 and Q2 are resolved (比較 and 頼む exist). The three adopted guards are resolved: each target exists, each is a direct pair, 会員's new `quiz_exclusions` follows `tags` as in other cards, and none masks a needed distinction. No other title contains «антракт» or «перерыв на отдых»; neither segment of the new 休憩 title equals a published title; 休み and 昼休み stay guarded; the 休む stem hit is a verb, unguarded in EN too; and 公演, 芝居 and コンサート match only inside the restriction. The 余分, 以来 and 何とか edits are prose only. Every changed card matches its manifest hash after LF normalisation, the manifest key set equals the files on disk, and the intake's 56 paths equal the content diff. It kept its strokes-hash note withdrawn. Consistency, quiz safety and cross-file integration are **CLEAN**, with no open findings. |
| Comprehensibility | The reviewer read the nine changed passages. C1 is resolved: the restricted title and the nuance sentence remove the co-equal misreading, and the conversational clause matches the sense already cited. C2 is resolved: «с трудом, но успел» cannot mean «небрежно» and still means arriving in time; it offered «Я спешил и с трудом успел вовремя.» as optional smoothing. 余分:24 is clear, and the quiz-only edits change no learner prose. It raised **R1** (minor; high confidence), `以来.md:33`: fix 1's «(англ. henceforth)» put an English gloss in Russian learner prose, which an English-free beginner cannot use and the point does not need. Verdicts: comprehensibility **NEEDS FIX** (R1); scoped coverage **CLEAN**. |

### Round 3 (`40e30b5`)

| Facet | Scope and result |
|---|---|
| Comprehensibility | R1 is resolved: 以来:33 drops the English gloss, and «заменять словом 以来» names the word and matches EN's restriction without an ambiguous «им». No regression. Comprehensibility and scoped coverage are **CLEAN**. |
| Correctness | The reviewer inspected the actual diff and reread the complete 以来 card against EN. The earlier optional item stays resolved: removing the parenthetical loses no Japanese teaching point, «отныне» stays supported by JMdict 1155210 sense 1 and Kuznetsov, and «заменять словом 以来» matches EN. The Russian is natural, and the following past-anchor explanation and examples are unchanged. Correctness and scoped coverage are **CLEAN**, with no new findings. |
| Consistency | The reviewer confirmed that the diff from `867e749` touches only 以来:33, the manifest and the intake; that 以来's front matter is unchanged; and that its manifest hash and its single intake hash are current (`contentVersion` `9bd4efcc2f80dfbe`). Consistency, quiz safety and scoped coverage are **CLEAN**, with no open findings. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 余分's reading join in katakana instead of EN's hiragana (minor) | **Resolved** | `余分.md:24`; EN `余分.md:29`; JMdict 1544520. Severity unchanged. |
| Correctness R1 (round 1): 休憩:33 excludes conversational «антракт» outright (minor) | **Resolved** (fix 2) | `休憩.md:33`; Kuznetsov «антракт» 1 «Разг.». Adopted in substance: «…в нейтральной речи говорят «перерыв», а «антракт» там звучит разговорно» rather than the proposed «…употребляется разговорно или переносно». |
| Correctness optional: 以来:33 warns against a «впредь» the card never shows | **Optional, adopted** | `以来.md:33`; JMdict 1155210 sense 1; Kuznetsov «отныне». Its first wording raised comprehensibility R1, fixed in fix 3. |
| Correctness optional: «творение» register mark (作品), «стали хорошо ладить» (仲), the 住宅 «житель» remark | **Optional, not adopted** | No defect shown: 作品's second title gloss gives the ordinary «художественное произведение», and «подружились» fits the 仲よくなる example. |
| Correctness note: navigation gaps 住宅→住民, 自宅→住宅, 昼休み→休憩 | **No action** | EN leaves all three unlinked. |
| Consistency Q1: 例え lacks a 比較 guard (minor) | **Resolved** | `例え.md:9`; JMdict 例え sense 2. Severity unchanged. |
| Consistency Q2: 任せる lacks a 頼む guard (minor) | **Resolved** | `任せる.md:9`; JMdict 頼む "to entrust to". Severity unchanged. |
| Consistency optional: 住民–人口, 仲間–友達, 会員–仲間 | **Optional, adopted** | `住民.md:9`, `仲間.md:9`, `会員.md:9`; all conservative. |
| Consistency optional: 会員–委員, 休憩–休む, 何で–どう, 作法–方法, 伝統–習慣, 体育–運動, and a 何時か→いつ link | **Optional, not adopted** | 会員's parenthesis separates it from 委員; 休む is a verb, unguarded in EN too; the others are weak overlaps unguarded in EN, and EN leaves いつ plain in 何時か. The consistency recheck kept them optional. |
| Consistency note: `strokes/*.json` manifest hashes do not match the raw blobs | **Withdrawn** | `tools/build_manifest.py` hashes bytes after CRLF→LF normalisation; the stroke blobs are CRLF byte copies marked `-text`. The reviewer kept it withdrawn in its recheck. |
| Consistency note: `kanji/信.md` has a 信号 link that EN lacks | **No action** | Pre-existing; not a batch change. |
| Comprehensibility C1: 休憩 offers «антракт» as an equal, unqualified gloss (minor) | **Resolved** (adapted) | `休憩.md:4,12,33`; JMdict 1227720 sense 1; EN "rest break; intermission". Severity unchanged. |
| Comprehensibility C2: 何とか's «кое-как» can read as «небрежно» (minor) | **Resolved** (adapted) | `何とか.md:17`; Russian Wiktionary «кое-как» senses 1–2; JMdict 1188420 sense 2. Severity unchanged. |
| Comprehensibility R1 (round 2): English gloss «(англ. henceforth)» in 以来's learner prose (minor) | **Resolved** (fix 3) | `以来.md:33`; EN `以来.md:33`. Also clarified «заменять им» as «заменять словом 以来». |
| Comprehensibility optional: C2 smoothing «Я спешил и с трудом успел вовремя.» | **Optional, not adopted** | Editorial preference; the reviewer judged the current sentence resolved. |
| Comprehensibility optional: 仲間 «коллега», 会員 «регистрация участника», the 住宅 «житель» wording, 作法 not explaining 行儀 | **Optional, not adopted** | The reviewer judged none a finding; each matches EN. |
| Author open question: 例え–比較 guard considered and declined | **Superseded** | The consistency review raised it as Q1, and fix 1 added it. |
| Author open question: 31 inline links at EN positions against 28 target pairs | **No action** | Kept EN-position parity; the consistency review confirmed that the 31 links match EN's positions and path forms. |
| Exclusion classification | **Reviewer and author agree on the candidate entries** | Both called all seven candidate RU-added entries required. |

Cross-batch note: links to absent targets stay plain. One of this batch's 14 unwrapped EN link occurrences targets a Batch 219
word: 以来's link to 今後, which is held for Batch 219. The other ten absent targets are not in Batch 219.

## Final exclusion set

All 28 EN exclusion entries (21 lists) are retained. Twelve direct, one-sided entries are added on twelve new cards:

- Required (9): 倒す→勝つ (whole title «побеждать»), 修正→直す (correcting), 作法→礼儀 («этикет»), 作品→曲
  («произведение»), 住宅→自宅 («жильё»), 休暇→夏休み («отпуск»), 休憩→昼休み («перерыв»), 例え→比較 («сравнение») and
  任せる→頼む (entrusting).
- Conservative (3): 住民→人口 (residents against population), 仲間→友達 (a companion against a friend) and 会員→仲間 (the
  shared «член»).

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN**. The first recheck's finding on fix 1's 休憩 register clause was resolved by fix 2.
- Scoped coverage: **CLEAN** after the fix (余分).
- Comprehensibility: **CLEAN** after the fixes (休憩, 何とか; 以来, fix 3).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after the fixes (例え, 任せる). This covers the reviewed batch and the directly adjudicated pairs.
  Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the cards needed to judge them. The unchanged cards rest on review
  001's full reading.
- The round 2 and round 3 correctness rechecks reused dictionary evidence inspected in earlier rounds. The consistency
  reviewer carried over 頼む's JMdict evidence from its first review. The comprehensibility reviewer did not re-read the
  other cards or the dictionary entries, and ran no validator.
- 休憩 remains unguarded against 休む «отдыхать; отсутствовать» (a verb, unguarded in EN too), 久しぶり «после долгого
  перерыва» (which shares only the stem «перер») and 公演, 芝居 and コンサート (which match only inside the restriction). The
  coordinator's recheck evidence listed all five. The consistency recheck explicitly judged 休む and the last three safe and
  raised no finding for 久しぶり.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
