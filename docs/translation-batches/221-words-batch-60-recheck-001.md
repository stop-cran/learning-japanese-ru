# Batch 221 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `f888c34e8eb7c8d29c76c0433dbb3b0035ee8e3b` | `0fb4d226b4ec03bd217f2acb300a050473e1e0b1` | Initial review snapshot: the signed candidate, pushed before review. |
| `47a07db9a160199733eba93fccffcb853f1b8544` | `285d9be2eb4e2e8d0155750a879de9253be18a2f` | Fix 1 (final candidate). It covers the three correctness limits, the consistency finding, the six comprehensibility findings, the adopted correctness optional item and the intake refresh. Signed and pushed before the rechecks. |

The fix changed eight word files and regenerated `manifest.json` (`contentVersion` `ed79c25a2ea1dcbd`, 4,749 entries; the
candidate had `a55f101dcc2ed0b6`) and the intake:
- `ドライブ` (lines 4, 9 and 12): title and H1 «поездка или прогулка на машине» instead of «поездка на машине;
  автопрогулка» (correctness L1 and its optional item). The body already said «поездку или прогулку на машине»;
  Kuznetsov «прогулка» explicitly includes travel by car, while no entry for the compound «автопрогулка» was found.
  `quiz_exclusions: [運転, 旅行, 散歩]` instead of `[運転, 旅行]`: the newly exposed standalone «прогулка» matches 散歩
  «прогулка», parallel to the existing 旅行 «поездка» guard.
- `バン` (lines 4, 12, 24 and 26), correctness L2 and comprehensibility C4, resolved together:
  - Title and H1 «пучок (причёска); фургон; сеть передачи данных (VAN)» instead of «…; сеть с добавленной стоимостью»,
    after EN "VAN network".
  - Line 24: «ＶＡＮ, которое пишут и как VAN, — сеть передачи данных с дополнительными услугами (от английского
    value-added network)…» instead of «…значит «сеть с добавленной стоимостью» — сеть передачи данных с дополнительными
    услугами…».
  - Line 26: «— Эта компания пользуется сетью передачи данных с дополнительными услугами.» instead of «…сетью с
    добавленной стоимостью.»
  - Evidence: Multitran EN→RU "value-added network" gives «сеть с дополнительными услугами» under Communications (the
    Microsoft glossary entry and the data-protection entry agree), while «сеть с "добавленной стоимостью"» appears only in
    quotation marks under computer networks; English Wiktionary value-added network, noun sense 1; JMdict ＶＡＮ/バン.
    The reviewer's «сеть передачи данных с услугами» was not adopted as the title because it is clumsy in Russian.
- `ボール` (line 21): «В бейсболе ボール называет ещё и неточную подачу — мяч, поданный мимо зоны удара.» instead of «…может
  называть и подачу, которая засчитывается как «бол», в противоположность страйку.» (correctness L3 and comprehensibility
  C2, resolved together, with the reviewer's remedy reworded). JMdict ボール sense 2.
- `パイプ` (line 9): `quiz_exclusions: [管, 付き合い, 関係, 連絡, 仲]` instead of `[管, 付き合い]` (consistency F1,
  accepted with 仲). 仲 «взаимоотношения (между людьми)» shares the exact substring «между людьми»; 関係 «связь; отношения»
  and 連絡 «связь; контакт» share the stem «связ» with the RU-added «связи». 付き合い already guards [関係, 仲]. The title
  is unchanged.
- `ド` (lines 4 and 12): title and H1 «усилительная приставка (самый, полный)» instead of «…(самый, совершенный)»
  (comprehensibility C1, the reviewer's remedy). It matches the card's «полный дилетант» and «полный новичок»; JMdict ど/ド
  prefix "extreme; ultra; totally". 完全 and いちばん stay guarded.
- `ママ` (lines 4 and 12): title and H1 «мама (в семейной речи); хозяйка бара» instead of «мама (по-домашнему); хозяйка
  бара» (comprehensibility C3, accepted in modified form). JMdict 1129240 sense 1 is marked familiar language. The
  reviewer's «фамильярно» was not adopted, because in Russian it can imply over-familiarity or disrespect. お母さん and 母親
  stay guarded.
- `ビデオ` (line 32): «ビデオ само по себе не означает именно старую видеокассету.» instead of «…именно кассету VHS.»
  (comprehensibility C5, the reviewer's remedy).
- `トンネル` (lines 18 and 20): «— Когда мы вышли из туннеля, стало видно море.» instead of «…выехали…» (comprehensibility
  C6, the reviewer's remedy; EN "came out"). The coordinator applied the same correction to the particle note on line 20:
  «…に отмечает место, в которое входят.» instead of «…куда въезжают.» (EN "the place entered").
- The intake note now names the fixed cards, and the eight candidate hashes were refreshed.

Before the commit, the coordinator's word title screen on the changed titles found every exact segment overlap guarded:
ド–完全 and ド–いちばん, ママ–お母さん and ママ–母親, バン–束, ドライブ–旅行 and ドライブ–散歩, and パイプ–管, パイプ–付き合い
and パイプ–仲. Stem-only neighbours were listed in the recheck briefs: 一杯 «полный; одна чашка», 太い, 満ちる and ぴんぴん
(«полн») for ド, which differ from an explicit prefix title; 上京 «поездка или переезд в столицу» («поездка», a different
destination-bound sense) for ドライブ; and 関係 and 連絡 («связ», now guarded) for パイプ.

Net change from the candidate: four retitles (ドライブ, バン, ド, ママ), body wording in バン, ボール, ビデオ and トンネル, two
example translations (バン, トンネル) and four added exclusion entries on two cards (ドライブ, パイプ). No Japanese example
sentence, sourced reading, EN exclusion or link changed.

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
- the actual content diff from `f888c34` to `47a07db`, inline;
- the coordinator's evidence for every change, the title-screen results and the declined items, stated without the other
  reviewers' reports;
- the reviewer's original verdicts and the disposition of each of its own findings.

All recheck messages forbade running `tools/build_manifest.py` or any other generator. Every recheck section states that
none was run. The correctness and consistency reviewers ran `tools/validate.py` (0 errors each); the consistency reviewer
deleted the untracked `tools/__pycache__` its own validator run had left. The comprehensibility reviewer reported running no validator. After every recheck the
coordinator confirmed that HEAD was `47a07db` and that `git status --porcelain --ignored` was empty.

### Round 1 (`47a07db`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer checked the actual eight-card diff against the previously reviewed full cards and their EN originals, treating the supplied dispositions as hypotheses. It reopened English Wiktionary value-added network (noun sense 1) and freshly inspected JMdict ボール (1123550, sense 2) and the ＶＡＮ entry and readings. L1 is resolved: ドライブ uses the dictionary-attested phrase for a trip or stroll by car, and the unverified compound is gone; the optional title item is adopted in substance. L2 is resolved: バン describes a data network with additional services, keeping the VAN identity without the disputed Russian label. L3 is resolved: the outside-the-strike-zone paraphrase matches JMdict sense 2; it is a lexical explanation, not a complete scoring rule. Regression checks: ド's title covers both the exact-centre and complete-beginner examples, and the register warnings remain; ママ's family-register qualifier matches JMdict's familiar-language sense, and the proprietress sense remains; ドライブ keeps travel by car without implying the speaker drove; バン keeps all three identities; トンネル's wording keeps leaving and entering without vehicle travel; ビデオ still separates tape, digital content and recorder; the added exclusions alter no reading or learner prose. Correctness and scoped coverage are **CLEAN**, closing the three former UNVERIFIED exceptions, with no findings. |
| Consistency | The reviewer confirmed that the fix touches exactly the eight cards, `manifest.json` and the intake. F1 is resolved: `[管, 付き合い, 関係, 連絡, 仲]` is well-formed and all five targets exist; it classed 仲 as required (the exact substring «между людьми»), 関係 and 連絡 as conservative to required (the «связ» stem), 付き合い as required or conservative and 管 as required. No unguarded exact segment overlap remains; stem-only neighbours (扱う «людьми», 畔 and 間 «между», 運河 «канал») are not defensible swaps. The プロ→職業 lead stays optional and is not contested. Regression checks: ド keeps 完全 and いちばん guarded, and its «полн» and «самый» stem neighbours (一杯, ぴんぴん, 太い, ちょうど, 最低) are different senses next to an explicit prefix title; ママ keeps お母さん and 母親 guarded, and マスター «хозяин бара» against ママ «хозяйка бара» is an EN-inherited pair of different genders, optional only; バン keeps 束 guarded, and its body still matches the title; ドライブ's `[運転, 旅行, 散歩]` is well-formed, with 散歩 conservative but justified, 旅行 required and 運転 retained from EN; 上京's shared «поездка» is not a defensible swap. ボール, ビデオ and トンネル changed only body prose. Every Markdown entry in the manifest (`contentVersion` `ed79c25a2ea1dcbd`, 4,744 file entries) matches its file after CRLF-to-LF normalisation; the intake lists the same 38 payloads, its candidate raw hashes equal disk, its held list is empty and its note names the eight fixes. Consistency, quiz safety and scoped coverage of cross-file integration are **CLEAN**. |
| Comprehensibility | The reviewer reread the eight changed cards in full. C1 is resolved: ド's title and H1 read «усилительная приставка (самый, полный)», matching «полный дилетант» and «полный новичок», and «совершенный» is gone. C2 is resolved: «бол» and «страйк» are gone, and «неточную подачу» is defined in the same sentence as a pitch past the hitting zone. C3 is resolved: «в семейной речи» does not read as homestyle; «фамильярно» remains only in the body, where the form of address is explained. C4 is resolved: «добавленная стоимость» is gone, «сеть передачи данных (VAN)» is readable Russian with the term's own abbreviation, and lines 24 and 26 keep «с дополнительными услугами». C5 is resolved: «старую видеокассету» keeps the point without VHS. C6 is resolved, including line 20: «вышли» and «входят» leave no vehicle manner. The ドライブ optional item is resolved: the title and H1 match the opening sentence. The ホーム, ブレーキ, ミルク and long パイプ title items stay optional and declined. No regressions: ド still teaches the prefix rather than praise or the musical note; ボール still separates мяч, миска and the pitch; ママ still separates the family address from the bar proprietress; バン still teaches three entries; ビデオ and トンネル keep their sense and particle limits; パイプ's learner text is unchanged, and its new exclusions are outside this facet. The reviewer did not re-fetch Jisho or score the exclusions. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness L1: ドライブ «автопрогулка» has no exact dictionary entry (UNVERIFIED limit) | **Resolved** | `ドライブ.md:4,12`; Kuznetsov «прогулка»; the card's body. The label was replaced, not newly verified. |
| Correctness L2: バン «сеть с добавленной стоимостью» has no Russian terminological entry (UNVERIFIED limit) | **Resolved** (jointly with comprehensibility C4) | `バン.md:4,12,24,26`; Multitran "value-added network"; English Wiktionary value-added network; JMdict ＶＡＮ. |
| Correctness L3: ボール «бол» attested only in a Wikipedia glossary (UNVERIFIED limit) | **Resolved** (jointly with comprehensibility C2) | `ボール.md:21`; JMdict 1123550 sense 2. |
| Correctness optional: ドライブ title «прогулка на машине» | **Optional, adopted** | `ドライブ.md:4,12`. Adopted in substance as «поездка или прогулка на машине», with a conservative 散歩 guard. |
| Consistency F1: パイプ leaves 関係, 連絡 and 仲 unguarded (minor) | **Resolved** | `パイプ.md:9`; RU 関係, 連絡 and 仲 titles; 付き合い's existing [関係, 仲]. Accepted with 仲. |
| Consistency optional: drop the プロ→職業 over-guard | **Optional, not adopted** | Harmless conservative guard; the reviewer did not require removal. Retained. |
| Consistency limit: 118 `strokes/*.json` manifest hashes differ from raw bytes | **Not a defect** | `tools/build_manifest.py:18-19` hashes text payloads after CRLF-to-LF normalisation, and the byte-copied EN stroke files contain CRLF; unchanged from the parent. |
| Comprehensibility C1: ド «совершенный» reads as "perfect" and as 完全 (minor) | **Resolved** | `ド.md:4,12`; JMdict ど/ド prefix; the card's examples. |
| Comprehensibility C2: ボール «бол»/«страйк» relies on baseball jargon (minor) | **Resolved** (jointly with correctness L3; reworded) | `ボール.md:21`; JMdict 1123550 sense 2. |
| Comprehensibility C3: ママ «по-домашнему» can read as "homestyle" (minor) | **Resolved** (modified) | `ママ.md:4,12`; JMdict 1129240 sense 1. «в семейной речи» instead of the reviewer's «фамильярно». |
| Comprehensibility C4: バン «добавленная стоимость» reads as a tax term (minor) | **Resolved** (modified; jointly with correctness L2) | `バン.md:4,12,24,26`; Multitran; EN "VAN network". |
| Comprehensibility C5: ビデオ unexplained «кассету VHS» (minor) | **Resolved** | `ビデオ.md:32`. |
| Comprehensibility C6: トンネル «выехали» adds vehicle travel (minor) | **Resolved** (extended to line 20) | `トンネル.md:18,20`; EN "came out" and "the place entered". |
| Comprehensibility optional: ホーム «перрон», ブレーキ «сдерживание», ミルク «детская смесь», パイプ's long third gloss | **Optional, not adopted** | The reviewer called each a recognized equivalent or bounded by the body, not a defect. Declined. |
| Comprehensibility optional: ドライブ «автопрогулка» | **Optional, adopted** | Adopted through correctness L1. |
| Exclusion classification | **Reviewer's classification adopted** | The author and the consistency reviewer agreed on every candidate entry except プロ→職業, which the reviewer called a harmless possible over-guard. For the fix entries the reviewer classed パイプ→仲 as required, パイプ→関係 and パイプ→連絡 as conservative to required and ドライブ→散歩 as conservative. |

Cross-batch note: links to absent targets stay plain. Three EN link occurrences in this batch's new cards target three
absent RU files: ペンキ→絵の具, ベンチ→ソファー and バイオリン→楽器. ソファー is a Batch 222 word; its link from ベンチ is held
for that batch. 絵の具 and 楽器 are not in Batch 222.

## Final exclusion set

All 19 EN exclusion entries (11 lists) are retained. Eighteen direct, one-sided entries are added on 11 new cards (six of
them new lists):

- Required (7): ハンサム→美しい, ハンサム→きれい, バン→束, ドライブ→旅行, ド→いちばん, ド→完全 and, added in the fix,
  パイプ→仲.
- Conservative (10): ボール→ちゃわん, マスター→上達, ドラマ→出来事, ビール→酒, ビール→お酒, ハイキング→観光 and
  パイプ→付き合い, and, added in the fix, パイプ→関係 and パイプ→連絡 (the reviewer's "conservative to required") and
  ドライブ→散歩. Batch 220 recorded the parallel ワイン→酒 and ワイン→お酒 as required; here the reviewer classed the ビール
  hypernym guards as conservative but justified. The guards are retained either way.
- Retained over-guard (1): プロ→職業. The titles already separate the cards; the guard only shrinks the distractor pool,
  and its removal was declined.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the fix (ドライブ, バン, ボール; the three UNVERIFIED labels were replaced).
- Scoped coverage: **CLEAN** throughout.

- Comprehensibility: **CLEAN** after the fix (ド, ボール, ママ, バン, ビデオ, トンネル).

- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after the fix (パイプ). This covers the reviewed batch and the directly adjudicated pairs.
  Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the cards needed to judge them. The unchanged cards rest on review
  001's full reading.
- The replaced labels («автопрогулка», «сеть с добавленной стоимостью», «бол») were removed, not newly verified.
- The consistency reviewer compared 20 of the 30 EN originals by script; the correctness and comprehensibility reviewers
  read all 30 pairs in full.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
