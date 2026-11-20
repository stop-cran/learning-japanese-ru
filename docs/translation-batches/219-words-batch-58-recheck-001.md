# Batch 219 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `f72537721d86b0d72485aecb4a758b10ef241a20` | `ea1be965b31c1cc36dc04bbe0cacaaacc3b3e6b5` | Initial review snapshot: the signed candidate, pushed before review. |
| `dae224d17525ae793140fbbef00eb2a478704167` | `f3eff416476e70b4a0e6b98fd019bfb3c328b24e` | Fix 1 (final candidate). It covers the three correctness findings, the three comprehensibility findings, one adopted consistency optional item, two adopted correctness optional items and the intake refresh. Signed and pushed before the rechecks. |

The fix changed seven word files and regenerated `manifest.json` (`contentVersion` `9d21053b31ef3d53`, 4,689 entries; the
candidate had `bc7ef19587f3f1e0`) and the intake:
- `主義` (line 19): «Он не изменил свои принципы.» instead of «Он не изменил своим принципам.» (correctness C1, as proposed).
  Kuznetsov «изменить» 2, sense 3 («Нарушить верность чему-л.», example «И. своим принципам»); JMdict 変える sense 1; EN
  "He did not change his principles."
- `今にも` (line 29): the RU-only 今に comparison now ends «…; само по себе оно не подчёркивает непосредственную близость
  события так, как 今にも.» instead of «…; оно не описывает того, что уже вот-вот произойдёт.» (correctness C2, as
  proposed). Digital Daijisen 今に 1, with the example この空では今に雨が降る.
- `人込み` (lines 4, 12 and 31): title and H1 «толпа людей» instead of «толпа; толчея» (correctness C3 and comprehensibility
  F2, accepted jointly with C3's first remedy; F2 had proposed «толпа»).
  - «Толпа людей» is EN's title "crowd of people" and the body's own gloss. Kuznetsov «толчея» 1, sense 1 «Разг. Давка,
    толкотня»; `混雑.md` already glosses 混雑 «давка; скопление людей».
  - The «Синонимы» section adds: «[大勢](大勢.md)（おおぜい）, «много людей», указывает на количество: 大勢の人 могут стоять
    и свободно, без тесноты. [混雑](混雑.md)（こんざつ）— переполненность места, транспорта или дороги, причём не
    обязательно людьми; 人込み говорит именно о плотном скоплении людей.» Evidence: Daijisen 混雑 2
    「たくさんの人が集まって込み合うこと」, example 「人と車で混雑する観光地」; JMdict 混雑 "congestion; crush; crowding;
    jam". EN leaves both words unlinked, so these are two new RU-only links; both targets were already 人込み's exclusions.
- `予測` (lines 4 and 12): title and H1 «прогнозирование; предварительная оценка» instead of «прогнозирование; оценка
  наперёд» (correctness optional item, adopted). Kuznetsov «наперёд» is «Нар.-разг.»; the new wording matches the body's
  «прогноз, предварительная оценка» and EN "prediction; estimation".
- `主婦` (line 17): «Мама много лет была домохозяйкой и не занималась оплачиваемой работой.» instead of «…и не работала вне
  дома.» (correctness optional item, adopted), matching line 20 «не работает за плату» and EN "full-time homemaker".
- `世間` (lines 4, 9, 12, 16 and 18), comprehensibility F3, adapted:
  - Title and H1 «окружающие люди; люди вообще» instead of «общественность; люди в целом». Kuznetsov «общественность»
    («Часть общества, активно участвующая в общественной жизни…») and MAS («Передовая часть, передовые круги общества»)
    narrow EN "society; the public"; `社会.md` already glosses 世間 «окружающие люди, общественная среда».
  - Line 16 drops «общественность» from the definition and adds «речь об обычных окружающих людях, а не об
    «общественности» как активной части общества или общественных организациях».
  - Line 18: «Эта новость привлекла всеобщее внимание.» instead of «…внимание общественности.» (EN "The news attracted
    public attention."). F3 had proposed «…внимание людей.»
  - `quiz_exclusions: [社会, 人, 周囲, 環境]` instead of `[社会]`. 人 «человек; люди» is the consistency reviewer's
    optional 世間–人 lead, adopted as conservative. 周囲 «окружение; периметр» and 環境 «окружающая среда; окружение» were
    added as conservative because the new «окружающие» is a stem neighbour of «окружение», which can also name one's circle
    of people.
- `代表` (lines 4, 12 and 16): title and H1 «представитель; характерный образец» instead of «представитель;
  представительство», and line 16 opens «代表 — существительное: представитель группы или характерный образец категории.»
  (comprehensibility F1, adapted).
  - Ozhegov «представительство» names an office; `代わり.md` uses the word for 代理. JMdict 1412170 sense 2 ("being
    representative; exemplification") is already taught by the second example and line 21.
  - F1's proposed «а не … действие от чужого имени» was declined because 全員を代表して does mean acting on a group's
    behalf; 代理 stays contrasted in «Синонимы».
- The intake note now names the fixed cards, and the seven candidate hashes were refreshed.

Before the commit, the coordinator's word title screen on the four changed titles found no exact segment overlap with any
published word title. Stem-only neighbours were listed in the recheck briefs: 型, 特徴, 独特 and 例え for 代表; 列 for
人込み; 予約, 評価 and 可 for 予測; 周囲 and 環境 (now guarded), 囲む, 実は and 物事 for 世間.

Net change from the candidate: four retitles (人込み, 予測, 世間, 代表) with a new definition sentence in 代表 and 世間, one
new comparison paragraph with two RU-only links (人込み), three example translations (主義, 主婦, 世間), one qualified
comparison (今にも) and three added exclusion entries on one card (世間). No Japanese example sentence, sourced reading, EN
exclusion or EN link changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, one reviewer at a time, in one round: correctness, then consistency, then comprehensibility, all
on fix 1. Each reviewer appended to its own report file, which stayed in its session context. Each recheck brief gave the
reviewer:
- the fix commit, the reviewed candidate as its parent, and the read-only rules;
- the actual content diff from `f725377` to `dae224d`, inline;
- the coordinator's evidence for every change, the title-screen results and the declined and withdrawn items, stated
  without the other reviewers' reports;
- the reviewer's original verdicts and the disposition of each of its own findings.

All recheck messages forbade running `tools/build_manifest.py` or any other generator, and every recheck section states that
none was run. The correctness and consistency reviewers ran `tools/validate.py` (0 errors each); the comprehensibility
reviewer ran no validator. After every recheck the coordinator confirmed that HEAD was `dae224d` and that
`git status --porcelain --ignored` was empty.

### Round 1 (`dae224d`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer read the brief, the actual seven-card diff, all seven revised cards, the existing RU 大勢 and 混雑, and frozen EN 代表, 世間 and 人込み, and re-fetched JMdict senses for 代表, 世間, 混雑 and 大勢 through the Jisho API. C1 is resolved: the accusative restores changing rather than betraying principles. C2 is resolved: the emphasis contrast no longer prohibits imminent uses of 今に. C3 is resolved: «толпа людей» removes the jostling and register implication. The adopted 予測 and 主婦 items are resolved as polish. Regression checks: 代表's title and opening are supported by JMdict sense 2, and acting for a group is still explained; 世間 keeps people generally and contextual social judgment, and its qualification rejects only the institutional sense; «всеобщее внимание» is an idiomatic general-public rendering; 人込み's contrasts correctly separate number from density, and human crowds from congestion that can include vehicles; the new exclusions remove no taught sense. Correctness and scoped coverage are **CLEAN**, with no findings outstanding. |
| Consistency | The reviewer confirmed that the diff touches exactly the seven cards, `manifest.json` and the intake. The 世間–人 lead is resolved: all four 世間 targets exist, the list is well-formed, and the additions guard the stem neighbours and the "people" sense without masking a needed distinction (the body contrasts 世間 with 社会 and teaches no contrast with 人, 周囲 or 環境). The four declined leads stay optional, and none of the changed titles touches them. The four new titles are unique across `words/*.md`; the listed stem neighbours are not alternate answers or are guarded. 人込み's two new links resolve to existing words in the batch's `X.md` form, with a substantive comparison. 主義, 主婦 and 世間:18 are prose-only. All 4,684 `words/*.md` hashes in the manifest (after CRLF→LF normalisation) match the tree, and the intake carries the seven new hashes. It kept the strokes-hash note withdrawn. Consistency, scoped coverage and quiz safety are **CLEAN**, with no new findings. |
| Comprehensibility | The reviewer read the seven changed cards. F1 is resolved: «представительство» is gone, the new title and line 16 match both taught senses, declining «а не действие от чужого имени» is right because the class example still teaches acting for a group, and 代理 stays the proxy contrast. F2 is resolved: the 大勢 and 混雑 paragraph agrees with `混雑.md`, and «толчея» is not reused. F3 is resolved: the title matches 社会's gloss of 世間, and line 16 warns against the organisational sense; «всеобщее внимание» is slightly broader than EN "public attention", but the surrounding text keeps the circle contextual, so this is not a remaining defect. The other four edits add no regression. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 主義:19 «изменил своим принципам» reads as betrayal (minor) | **Resolved** | `主義.md:19`; Kuznetsov «изменить» 1 against 2.3; JMdict 変える sense 1. Severity unchanged. |
| Correctness C2: 今にも:29 bans imminent uses of 今に (minor) | **Resolved** | `今にも.md:29`; Daijisen 今に 1 and 今にも. Severity unchanged. |
| Correctness C3: unqualified «толчея» in 人込み's title (minor) | **Resolved** (jointly with F2) | `人込み.md:4,12`; Kuznetsov «толчея» 1.1; JMdict 人込み sense 1. Severity unchanged. |
| Correctness optional: 予測 «оценка наперёд» is popular-colloquial | **Optional, adopted** | `予測.md:4,12`; Kuznetsov «наперёд». Resolved as polish. |
| Correctness optional: 主婦:17 «не работала вне дома» | **Optional, adopted** | `主婦.md:17`; line 20. Resolved as clarification. |
| Correctness optional: «того и гляди» register (今にも); «прогнозирование» process against result (予測) | **Optional, not adopted** | The reviewer found «того и гляди» semantically supported, and the H1 pairs it with neutral «на грани чего-либо»; 予測's companion gloss keeps the result sense. |
| Consistency optional: 世間–人 | **Optional, adopted** | `世間.md:9`; conservative. Resolved in the recheck. |
| Consistency optional: 主に–たいてい, 以前–昔, 主要–中心, 今後–未来 | **Optional, not adopted** | No shared title segment; EN guards none of them. The consistency recheck kept them optional. |
| Consistency note: 110 `strokes/*.json` manifest hashes did not match in a working-tree check | **Withdrawn** | `tools/build_manifest.py` hashes bytes after CRLF→LF normalisation; the stroke blobs are CRLF byte copies marked `-text`; the batch touches no stroke file. The reviewer kept it withdrawn in its recheck. |
| Comprehensibility F1: 代表 «представительство» reads as an office or as 代理 (moderate) | **Resolved** (adapted) | `代表.md:4,12,16`; Ozhegov «представительство»; JMdict 1412170 senses 1–2. Severity unchanged. |
| Comprehensibility F2: 人込み «толчея» echoes 混雑; no 大勢/混雑 contrast (minor; scoped coverage) | **Resolved** (adapted) | `人込み.md:4,12,31`; Daijisen 混雑 2; JMdict 混雑. Severity unchanged. |
| Comprehensibility F3: 世間 «общественность» narrows "the public" (minor) | **Resolved** (adapted) | `世間.md:4,12,16,18`; Kuznetsov and MAS «общественность»; `社会.md`. Severity unchanged. |
| Comprehensibility optional: 代理 «не должность заместителя» | **Optional, not adopted** | Line 33 already says a 代理 does not permanently take the other's place, and 部長代理 is an established job title, so a categorical «не должность» would be inaccurate. |
| Comprehensibility optional: tie 今にも:33's «в любую минуту» to «того и гляди» | **Optional, not adopted** | Editorial; the reviewer found no defect. |
| Exclusion classification | **Reviewer's classification adopted** | The author called 2 of the 35 candidate RU-added entries required; the consistency reviewer called 15 required and 20 conservative. Neither called any entry unjustified. |

Cross-batch note: links to absent targets stay plain. Five EN link occurrences in this batch's files target four absent RU
files: 世間→世の中, 交際→デート, 予測→kanji 測, and 予算 and 計算→kanji 算. 世の中 is a Batch 220 word; its link from
世間 is held for that batch. The other targets are not in Batch 220.

## Final exclusion set

All 20 EN exclusion entries (15 lists) are retained. Thirty-eight direct, one-sided entries are added on 18 new cards:

- Required (15): 以前→先, 以前→過去, 今にも→もうすぐ, 代表→典型, 代理→代わり, 付き合い→関係, 付き合い→仲, 人生→生命,
  今回→度, 今回→場合, 人込み→混雑, 主張→見解, 主に→大半, 主に→大部分 and 事務→仕事. The consistency reviewer found a
  basis for each in the visible Russian titles or the dictionary.
- Conservative (23): 以前→元, 以前→まず, 今後→将来, 今後→先, 今にも→今に, 人生→生, 人生→生活, 交際→関係, 交際→恋,
  交際→仲, 交際→連絡, 予測→予期, 予測→読み, 予測→天気予報, 主要→要点, 主義→思想, 主張→要求, 主に→主要, 中止→止める,
  中止→止む, and, added in the fix, 世間→人, 世間→周囲 and 世間→環境.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the fix (主義, 今にも, 人込み).
- Scoped coverage: **CLEAN** after the fix (人込み).
- Comprehensibility: **CLEAN** after the fix (代表, 人込み, 世間).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** throughout. This covers the reviewed batch and the directly adjudicated pairs. Exclusions are
  direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the cards needed to judge them. The unchanged cards rest on review
  001's full reading.
- The consistency reviewer took the dictionary evidence for the new glosses from the brief and hash-checked only the
  manifest's `words/` entries. The comprehensibility reviewer did not re-fetch dictionary entries and ran no validator.
- «Всеобщее внимание» (世間:18) is slightly broader than EN "public attention"; both the correctness and comprehensibility
  rechecks judged it idiomatic and not a defect.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
