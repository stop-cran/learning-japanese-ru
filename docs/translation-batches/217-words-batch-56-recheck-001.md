# Batch 217 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `4af7ea72f6c372d31a810a783ca4b8655dd4ba44` | `7d76a5cff85d39b882c357ad2718d0fd71662b5c` | Initial review snapshot: the signed candidate, pushed before review. |
| `a82ecc2ea18cd13b427a7516b72a732d53e56782` | `e69d9cec500b0dc7fcfc3af51a98aab1586f3384` | Fix 1. It covers the correctness finding, the three consistency findings, two adopted consistency optional items, the comprehensibility finding and the intake refresh. Signed and pushed. |
| `2b35d629ada03718c9404e7d748c8bb28101a04f` | `e0075909cb9303f52193f61748bcc4ef328bd508` | Fix 2 (final candidate). It adds one coordinator guard, 出会い→迎え, and refreshes the manifest and intake. Signed and pushed before the rechecks. |

Together the fixes changed six word files and regenerated `manifest.json` (`contentVersion` `3d6ad02960559405`, 4,629
entries; fix 1 alone produced `c60ee51dc906d149`) and the intake:
- `克服` (line 15): «克服 — преодоление трудности, взятие её под контроль» instead of «…, способность взять её под контроль»
  (correctness F1, as proposed). The following を and たい guidance is unchanged.
- `共に` (line 9): `quiz_exclusions: [一緒, 両方]` (consistency Q1). 共に «сообща; вместе с кем-либо; и тот и другой» and
  両方 «оба; обе стороны»; JMdict 共に lists "both; alike". EN "together; both" / "both" is unguarded in EN.
- `出会い` (lines 4, 12, 16, 19, 21, 31): title and H1 «встреча (с человеком или чем-либо)» instead of «встреча и знакомство
  (с кем-либо или чем-либо)» (comprehensibility C1, exactly as proposed).
  - Line 16 now reads «первая встреча с человеком или встреча с чем-либо»; line 19 «В поездках случаются новые встречи.»;
    line 21 «есть возможность кого-то встретить»; line 31 «не прямая замена такой встречи».
  - Line 35 («не ограничено романтическими знакомствами») stays, because it correctly limits one reading.
  - Evidence: Digital Daijisen 出会い sense 1 「思いがけなくあうこと／めぐりあい」, with 知り合うこと as a separate sense 6; JMdict
    1338400 "meeting; rendezvous; encounter"; EN title "meeting; encounter".
- `出会い` (line 9): `quiz_exclusions: [出会う, 会合, 会, 迎え]` (consistency Q2, adapted to the new title).
  - Q2 proposed 会合 and 紹介. 会合 «встреча; собрание» was added, and 会 «встреча; объединение» too, because it leads with the
    same «встреча».
  - 紹介 «представление; знакомство» was not added: the retitle removed «знакомство», so the two titles share no segment or
    stem.
  - Fix 2 added 迎え «встреча прибывающего; встречающий». Its published card already excludes 会 and 会合 for the same
    leading «встреча». EN leaves "meeting; encounter" / "meeting an arrival; pickup" unguarded.
  - The title screen after both fixes reports no unguarded exact segment overlap. The remaining unguarded stem hits are
    «встре» in 会う «встречаться с человеком» (a verb; EN 出会い does not exclude 会う either), ばったり «с размаху (упасть);
    неожиданно (встретить)» (an adverb that already excludes 出会う) and パーティー «вечеринка; праздничная встреча» (a specific
    festive event), plus «челов» in about 25 person nouns such as 人, 人間 and 老人 (false friends).
- `処理` (line 9): `quiz_exclusions: [解決, 治める]` (consistency Q3, extended). 処理 «обработка; улаживание дел» against
  解決 «решение (проблемы); урегулирование» and 治める «управлять (страной); улаживать (спор)»: уладить ≈ урегулировать, and
  治める shares the stem and the settling sense. EN 処理 has no exclusions.
- `借金` (line 9): `quiz_exclusions: [貸し]` (consistency optional, adopted as conservative). 貸し «ссуда; должок (за услугу)»
  against 借金 «денежный долг; заём»: «ссуда» ≈ «заём», «должок» ≈ «долг».
- `共通` (line 9): `quiz_exclusions: [同じ]` (consistency optional, adopted as conservative). 同じ «одинаковый; тот же»
  against 共通 «общий (для нескольких); совпадающий».
- The intake note now names the fixed cards, and the six candidate hashes were refreshed.

Net change from the candidate: one definition fix (克服), one retitle with four gloss edits (出会い), and eight added
exclusion entries on five cards. No Japanese example, reading, EN exclusion or link changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, in the order correctness, consistency, comprehensibility. Each reviewer appended to its own report
file, which stayed in its session context. Every recheck message gave it:
- both fix commits, the reviewed candidate as fix 1's parent, and the read-only rules;
- the actual content diff from `4af7ea7` to `2b35d62` inline;
- the coordinator's evidence for every change, including the declined and withdrawn items, stated without the other
  reviewers' reports;
- the coordinator's disposition of each of its own findings.

Both fixes were committed before the first recheck, so all three rechecks reviewed the final candidate `2b35d62`. The recheck
messages forbade running `tools/build_manifest.py` or any other generator, and all three recheck sections state that none
was run. The correctness and consistency reviewers ran `tools/validate.py` with `-B` (0 errors); the comprehensibility
recheck reports no validator run. After every recheck the coordinator confirmed that HEAD was unchanged and that `git status
--porcelain --ignored` was empty.

### Round 1 (`2b35d62`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer inspected the actual candidate-to-HEAD word diff and read the six changed cards in full, plus frozen EN 克服 and 出会い. It re-fetched JMdict 克服 sense 1 and 出会い senses 1–2, and Digital Daijisen 出合い／出会い senses 1 and 6 on Kotobank: encounter and acquaintance are separate senses. F1 is resolved: «взятие её под контроль» names the act, is natural explanatory Russian, and keeps the を construction and the unachieved たい goal. The retitled 出会い keeps encounter, first meeting with a person and coming across something; «В поездках случаются новые встречи» renders 旅先では新しい出会いがあります faithfully, and «есть возможность кого-то встретить» keeps EN's opportunity-to-meet explanation without requiring acquaintance. No teaching sense, Japanese text, kana, citation or link was lost, and the added exclusions change no lexical claim. Correctness and scoped coverage are **CLEAN**, with no new findings. |
| Consistency | The reviewer confirmed that the commits change only the six word cards, the manifest and the intake. Q1 is resolved (両方 exists). Q2 is resolved: with «знакомство» gone from the title, dropping 紹介 is sound; 会合 and 会 exist; 迎え shares «встреча», and its own card already excludes 会 and 会合, so the guard is a conservative extra with a real basis. The remaining stem hits (会う as a verb, ばったり, パーティー) are not a defensible same-answer pair, and EN leaves 会う unguarded too. Q3 is resolved (解決 and 治める exist; 治める is a conservative extra). The adopted optional guards 借金–貸し and 共通–同じ are valid; it accepted the declines of 全–皆 and 冗談–悪戯 as optional with no defect established. It withdrew its strokes-hash note: after CRLF→LF normalisation all 118 stroke hashes match, and no other manifest entry is stale. The manifest and the intake `candidateRawSha256` values are current for all six changed files. Consistency, quiz safety and cross-file integration are **CLEAN**, with no regressions. |
| Comprehensibility | The reviewer read the full content diff, the current 出会い and 克服 in full, and the quiz-only front matter of 借金, 共に, 共通 and 処理. C1 is resolved: lines 4, 12, 16, 19, 21 and 31 match the proposed replacements, and line 35 was correctly left. The repeated «встреча» in line 16 is clear (a first meeting with a person, or a meeting with a thing), and line 21's «кого-то встретить» matches EN "meet someone". 克服:15 is easier to follow than the old mix of an act and an ability; both nouns name the act, and «её» refers to «трудности». The quiz-only edits change no title, gloss or example. The optional 出 «вытекание (воды)» remains optional. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 克服 defines an ability, not the act (minor) | **Resolved** | `克服.md:15`; JMdict 克服 sense 1; Kuznetsov «способность» sense 1. Severity unchanged. |
| Consistency Q1: 共に lacks a 両方 guard (minor) | **Resolved** | `共に.md:9`; JMdict 共に "both; alike". Severity unchanged. |
| Consistency Q2: 出会い lacks 会合 and 紹介 guards (minor, conservative) | **Resolved** (adapted) | `出会い.md:9`; 会合 added, with 会 and 迎え for the same leading «встреча»; 紹介 not added because the C1 retitle removed the shared «знакомство». The consistency recheck accepted the adaptation. |
| Consistency Q3: 処理 lacks a 解決 guard (minor, conservative) | **Resolved** | `処理.md:9`; 解決 added, extended to 治める «улаживать (спор)». |
| Consistency optional: 借金–貸し and 共通–同じ | **Optional, adopted** | `借金.md:9`, `共通.md:9`; both conservative. |
| Consistency optional: 全–皆 and 冗談–悪戯 | **Optional, not adopted** | 全's «весь (приставка)» marks the prefix use; 冗談 «шутка» against 悪戯 «шалость; проделка», and the card teaches the contrast. The consistency recheck accepted both declines. |
| Consistency note: 118 `strokes/*.json` manifest hashes do not match | **Withdrawn** | `tools/build_manifest.py:19` hashes bytes after CRLF→LF normalisation; the stroke blobs are CRLF byte copies marked `-text`. The reviewer withdrew it after recomputing. |
| Comprehensibility C1: 出会い joins «встреча» and «знакомство» (minor) | **Resolved** | `出会い.md:4,12,16,19,21,31`; Digital Daijisen 出会い senses 1 and 6; JMdict 1338400. Severity unchanged. |
| Comprehensibility optional: 出 «вытекание (воды)» narrower than EN "outflow" | **Optional, not adopted** | The taught example is water, and the body does not restrict the sense; the reviewer judged no change needed. |
| Author open question: いくら wraps the Russian «иен» at EN's "yen" link position | **No action** | The consistency review confirmed that the position corresponds. |
| Exclusion classification | **Reviewer and author agree on the candidate entries** | Both called 全て→皆 and 先日→このあいだ required. The reviewer rated 優勝→勝ち required or conservative; it is recorded as conservative, the coordinator's class, because 優勝 names a specific kind of victory. |

Cross-batch note: links to absent targets stay plain. None of this batch's 23 unwrapped EN link occurrences targets a word in
the next batch, so no link is held for it.

## Final exclusion set

All 27 EN exclusion entries (14 lists) are retained. Eleven direct, one-sided entries are added on eight new cards:

- Required (3): 全て→皆 (shared «всё»), 先日→このあいだ (identical segment «на днях») and 共に→両方 («и тот и другой»
  against «оба»).
- Conservative (8): 優勝→勝ち (hyponym), 出会い→会合, 出会い→会 and 出会い→迎え (shared leading «встреча»), 処理→解決 and
  処理→治める (settling a matter), 借金→貸し («заём» against «ссуда») and 共通→同じ («совпадающий» against «одинаковый»).

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the fix (克服).
- Scoped coverage: **CLEAN** throughout.
- Comprehensibility: **CLEAN** after the fix (出会い).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after the fixes (共に, 出会い, 処理). This covers the reviewed batch and the directly adjudicated
  pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the cards needed to judge them. The unchanged cards rest on review
  001's full reading.
- The consistency reviewer took its dictionary senses from the coordinator's evidence and its own recollection, without
  re-fetching them. The comprehensibility reviewer did not re-read the other 24 cards or the dictionary entries, and ran no
  validator.
- 出会い remains unguarded against 会う, ばったり and パーティー, which share only the stem «встре»; the consistency recheck
  judged none of them a defensible same-answer pair.
- «катана» in 刀 rests on Russian Wiktionary; Gramota has no exact headword for it.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
