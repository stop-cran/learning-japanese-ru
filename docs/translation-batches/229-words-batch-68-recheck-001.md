# Batch 229 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `af5541a48700cdb110c81f127f63f226ead77ae7` | `c17dd3521821d417879b7f68fd6d1d74c9cd88c8` | Initial review snapshot: the signed candidate, pushed before review. |
| `ffe4626c50453e391f40921a0f9832e03c6a0c49` | `b9ec6d296f01fcbee27ffa3d6e44115b3a56b78e` | Fix 1 (final candidate). It covers correctness F1, consistency F1, comprehensibility F1–F7 (F5 and F7 with adapted wording), the adopted optional items (学会's 社会 link, 防止:31, 終了:19 and ストップ:18) and the intake refresh. Signed and pushed before the rechecks. |

Fix 1 changed twelve word files and regenerated `manifest.json` (`contentVersion` `f2f2457002df53c6`, 4,989 entries; the
candidate had `a8cdce1105990d1c`) and the intake:
- `障子` (line 19; comprehensibility F1): «Я переклеил бумагу на сёдзи.» instead of «Я заменил бумагу на сёдзи.», which
  parsed as заменить A на B (JMdict 張り替える "to re-cover; to repaper"; EN "I replaced the paper on the shoji").
- `開通` (lines 19–20; comprehensibility F2): «Телефонная линия заработала.» instead of «Телефонную линию подключили, и
  она заработала.», and «Дорога, которая была перекрыта, снова открылась для движения.» instead of «Дорогу, которая была
  перекрыта, снова открыли для движения.» Both now render the intransitive 開通する with its own subject.
- `締め切る` (line 19; comprehensibility F3): «Завтра мы закроем приём заявок на участие.» instead of «Приём заявок на участие
  закончится завтра.», matching the transitive verb and EN "We will close applications".
- `防犯` (line 18; comprehensibility F4): «Чтобы предотвратить преступления, я на ночь всегда запираю дверь.» instead of
  «Чтобы защититься от преступников, …» (EN "To prevent crime").
- `期限` (lines 4 and 12; comprehensibility F5, adapted wording): title and H1 «крайний срок; отведённый срок» instead of
  «срок действия; отведённый срок» (EN "deadline; term; time limit"). The reviewer's «установленный срок» was not used,
  because it is 定期's lead segment; «крайний срок» is unique in the word pool.
- `関わる` (line 18; comprehensibility F6): «Я вовлечён в новый проект.» instead of «Я участвую в новом проекте.», which used
  the verb the card assigns to 参加 at line 29 (EN "I am involved").
- `隔てる` (lines 4 and 12; comprehensibility F7, adapted wording): title and H1 «разделять (собой); отгораживать» instead
  of «отгораживать; стоять между» (EN "separate; have between"). The reviewer's «иметь между собой» is unidiomatic; the
  identical segment «разделять» shared with 分ける is guarded by EN's 隔てる→分ける.
- `締め切り`:
  - line 9 (consistency F1): `quiz_exclusions: [期限, 終わり, 仕舞い, 締め切る, 期間]`, adding 期間;
  - line 27 (correctness F1, adapted wording): «Отдельное физическое значение — закрывание двери или окна; в этом значении
    пишут и 閉め切り, с [閉](../kanji/閉.md). Переводы «закрыто» и «входа нет» подходят только к надписи на табличке и
    зависят от контекста: физически закрытый проход может объяснять табличку о закрытом входе, а приём заявок тоже может
    быть закрыт к сроку. Само по себе 締め切り не означает любой запрет входа.» instead of «Отдельное физическое значение —
    закрытая дверь или окно; его пишут и как 閉め切り, с [閉](../kanji/閉.md). На табличке 締め切り может сообщать, что
    приём закрыт; это не общее обозначение запрета входа.» (JMdict 1594590 sense 2 "closing (a door, window, etc.)";
    frozen EN 締め切り:29). The reviewer's added "a place closed in that way" is not in EN or JMdict sense 2 and was not
    added.
- `終了` (line 19; comprehensibility optional item): «На этом я заканчиваю объяснение.» instead of «На этом объяснение
  закончено.», matching the transitive 説明を終了します (EN "This concludes the explanation").
- `ストップ` (line 18; comprehensibility optional item): «Механизм внезапно остановился.» instead of «Машина внезапно
  остановилась.», which reads as a car; 機械's RU title is «машина; механизм».
- `学会` (line 33; correctness optional item and consistency O1): «как [社会](社会.md)（しゃかい）.» instead of plain
  «как 社会（しゃかい）.» The comparison is the RU adaptation's own replacement for EN's English "society" remark, so it
  is recorded as an RU-only link.
- `防止` (line 31; correctness and comprehensibility optional items): «…, поэтому эти слова нельзя считать совсем не
  связанными.» instead of «…; эти слова не совсем не связаны между собой.»
- The intake note now names the fixed cards, and the twelve candidate hashes were refreshed.

Comprehensibility F8 (締め切り:16 «написание из исходного списка»), the 開始 link in 終了, consistency's O3 (drop 障子→雨戸)
and the comprehensibility optional notes on 集会 «митинг», 随筆 «очерк» and 間接 «опосредованность» were not adopted; the
dispositions gave the reasons (see the reconciliation table). F8 renders EN's "the spelling in the source list", and the
same provenance phrase occurs in published RU cards, so it is deferred to the corpus-wide provenance-convention
follow-up.

The coordinator's post-fix title screen of the two changed titles (期限 and 隔てる) is recorded in its dispositions. 期限 «крайний
срок; отведённый срок» has no hit. 隔てる's only exact title segment shared with another card is «разделять», the title of
分ける, which 隔てる's EN exclusion of 分ける already guards; its other hits are stem-only. Fix 1 adds one RU-only link,
学会→社会, to an existing card at a substantive comparison; no EN link was lost where the RU target exists. `tools/validate.py`
reported 0 errors before the fix commit.

Net change from the candidate:
- titles and H1s of 期限 and 隔てる;
- example translations in 障子, 開通 (two), 締め切る, 防犯, 関わる, 終了 and ストップ;
- prose in 締め切り (line 27) and 防止 (line 31);
- one exclusion (締め切り→期間) and one link (学会→社会).

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`af5541a..ffe4626 -- words` is twelve word files, 16 lines added and 16 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs; the
comprehensibility recheck states that it is the same reviewer with no additional model.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. Each brief was sent only after the previous reviewer had replied. No recheck raised a new finding, so
there was no fix 2.

Each reviewer appended its recheck to its own report file, which stayed in its session context. The correctness and
consistency recheck sections record that they received the fix diff (`b229-fix1.diff`), and the correctness reviewer
confirmed that it matches the committed words diff; the correctness section records that it read the coordinator's
dispositions. The recheck sections do not reproduce the briefs, so this record does not claim their further contents.

The correctness recheck states that no generator ran, and the consistency and comprehensibility rechecks state that no
edits were made. The correctness and consistency reviewers each ran `tools/validate.py` (0 errors each); the
comprehensibility reviewer ran no validator. Each recheck section records snapshot `ffe4626` with a clean tree. The fix
script checked `git status --porcelain` after the fix commit, and after the last recheck the coordinator confirmed that
HEAD was `ffe4626` and that `git status --porcelain --ignored` was empty.

### Round 1 (`ffe4626`)

| Facet | Scope and result |
|---|---|
| Correctness | Bounded recheck of every changed passage in the twelve-card diff against the Japanese and frozen EN, plus its original F1 and three optional items; it did not re-review unchanged passages. F1 is **resolved**: 締め切り:27 now names the closing of a door or window, restores the physical closed-passage explanation, separates the closure of applications and keeps the warning against a general entry ban; the reviewer's closed-place extension has Daijisen support but is not needed beyond EN and JMdict. The 社会 link and 防止:31 optional items are **resolved**; the 締め切り:16 provenance item stays **optional** and deferred. No regression: 障子 expresses repapering; 開通 keeps the operational and reopening senses with intransitive subjects; 締め切る's «мы» matches EN; 防犯 renders 防犯のために; 期限's title covers deadline and term; 関わる's participle describes present involvement; 隔てる's title is a supported compact gloss and the body still teaches を隔てて; 終了 keeps the performative closing act; ストップ's «Механизм» fits 機械. Fresh Jisho/JMdict entries: 張り替える, 機械, 開通, 隔てる and 期限. Validator 0 errors. Correctness and scoped coverage are **CLEAN**, with no new finding. |
| Consistency | Snapshot `ffe4626` with a clean tree. F1 is **resolved**: 締め切り:9 excludes 期間, and all EN exclusions are retained. O1 is **resolved** for 社会 (the link resolves to 社会 «общество (социум)» at a substantive contrast); the declined 開始 link is accepted as EN-plain. O2 is **closed** (no guard; the retitle removed «между»), and O3 is **closed** (障子→雨戸 kept as a harmless over-guard). Title re-screen over the whole RU pool: 期限 has no lead (期間, 締め切り, 延期 and 定期 checked by meaning); 隔てる's 分ける is EN-guarded, 境界, 部分, 弁当, 誘う and 連れる are unrelated, and 離す and 離れる are already excluded. No card quotes the old titles; ストップ's «Механизм» matches 機械. Validator 0 errors; the manifest hashes of the twelve changed words match, and the intake's 32 payload hashes match HEAD. Optional: 期限 does not exclude 締め切り (EN does not either); the reviewer did not verify the app's symmetry. Consistency, quiz safety and scoped coverage are **CLEAN**, with no new finding. |
| Comprehensibility | Snapshot `ffe4626` with a clean tree; read the twelve changed cards and the titles of 定期, 分ける, 社会 and 機械, not the other 18 cards. F1–F4 and F6 are **resolved**: 障子 now means repapering, 開通's sentences are intransitive, 締め切る's has a closer, 防犯 matches the prevention gloss and 関わる matches its title. F5 and F7 are **resolved** by the adapted titles: 期限 drops the validity-period lead, and keeping 定期's «установленный срок» out of the title is the right adaptation; 隔てる is no longer intransitive, and «(собой)» keeps the between-sense. F8 is **withdrawn** for this batch: the reviewer accepted the decline as consistent with published RU cards and the corpus-wide follow-up; it is not an unresolved disagreement. The adopted 終了, ストップ and 防止 items and the 締め切り:27 rewrite show no regression; the declined 集会, 随筆 and 間接 glosses are accepted. Comprehensibility and scoped coverage are **CLEAN**, with no new finding. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 締め切り:27 physical sense and notice context (minor, correctness and coverage) | **Resolved** (adapted wording) | `締め切り.md:27`; frozen EN 締め切り:29; JMdict 1594590 sense 2; Digital Daijisen しめ‐きり sense 1. |
| Correctness optional: link 社会 in 学会:33 | **Optional, adopted**; resolved at recheck | `学会.md:33`; `社会.md` exists; recorded as an RU-only link. |
| Correctness optional: 締め切り:16 provenance wording | **Optional, not adopted**; deferred (see comprehensibility F8) | Renders EN "the spelling in the source list". |
| Correctness optional: 防止:31 «не совсем не связаны» | **Optional, adopted** (comprehensibility wording); resolved at recheck | `防止.md:31`. |
| Consistency F1: 締め切り «срок сдачи» and 期間 «срок; период» (minor, quiz safety) | **Resolved** | `締め切り.md:9`; 期間's title; EN guards 期限 against 期間. |
| Consistency optional O1: links to 社会 (学会) and 開始 (終了) | **社会 adopted; 開始 not adopted**; both closed at recheck | `学会.md:33`; EN 終了 leaves 開始 plain in its antonym line. |
| Consistency optional O2: 隔てる–間 and 差し支え–困る/困難 | **Closed**; no guard needed | Different part of speech and sense; the 隔てる retitle removed «между». |
| Consistency optional O3: drop 障子→雨戸 | **Optional, not adopted**; closed at recheck | Harmless over-guard; keeping it avoids churn. |
| Consistency recheck optional: 期限 does not exclude 締め切り | **No action** | 締め切り→期限 is an EN exclusion, and Android applies each declaration in both directions (EN `docs/content-format.md:162–165`). |
| Comprehensibility F1: 障子 «заменил бумагу на сёдзи» (moderate, also coverage) | **Resolved** | `障子.md:19`; JMdict 張り替える sense 1; EN "I replaced the paper on the shoji". |
| Comprehensibility F2: 開通 agentive translations (moderate, also coverage) | **Resolved** | `開通.md:19–20`; JMdict 開通 senses 1–2; EN "reopened". |
| Comprehensibility F3: 締め切る intransitive translation (moderate, also coverage) | **Resolved** | `締め切る.md:19`; EN "We will close applications". |
| Comprehensibility F4: 防犯 «защититься от преступников» (moderate, also coverage) | **Resolved** | `防犯.md:18`; JMdict 防犯 sense 1; EN "To prevent crime". |
| Comprehensibility F5: 期限 lead gloss «срок действия» (moderate) | **Resolved** (adapted wording) | `期限.md:4,12`; EN "deadline; term; time limit"; 定期 leads with «установленный срок». |
| Comprehensibility F6: 関わる «участвую» (minor, also coverage) | **Resolved** | `関わる.md:18`; `関わる.md:29`; EN "I am involved". |
| Comprehensibility F7: 隔てる «стоять между» (minor) | **Resolved** (adapted wording) | `隔てる.md:4,12`; EN "separate; have between"; EN 隔てる→分ける. |
| Comprehensibility F8: 締め切り:16 «написание из исходного списка» (minor) | **Declined; withdrawn** by the reviewer at recheck | Renders EN's "the spelling in the source list"; the phrase occurs in published RU cards; deferred to the corpus-wide provenance-convention follow-up. |
| Comprehensibility optional: 終了:19 resultative translation | **Optional, adopted**; no regression at recheck | `終了.md:19`; 説明を終了します; EN "This concludes the explanation". |
| Comprehensibility optional: ストップ:18 «Машина» | **Optional, adopted**; no regression at recheck | `ストップ.md:18`; 機械 «машина; механизм». |
| Comprehensibility optional: 集会 «митинг», 随筆 «очерк», 間接 «опосредованность» | **Optional, not adopted**; accepted at recheck | Each body explains the term; no learner-blocking gap. |
| Comprehensibility outside-facet notes: 閉会 omits 開会; 期限 omits 締め切り | **No action** | 開会 and 閉会 are a taught antonym pair; 締め切り→期限 already exists and applies in both directions. |
| Consistency limit: `strokes/*.json` manifest entries do not match working-tree bytes | **Not a defect**; pre-existing and outside the batch | `tools/build_manifest.py` hashes text files after CRLF→LF normalization; the stroke files are CRLF byte copies of EN blobs kept by `.gitattributes` (`strokes/*.json -text`), as established in Batch 226. The batch touches no `strokes/` file. |
| Exclusion classification: the eight RU-added candidate guards | **Agreed**; all kept | 締め切り→締め切る and 関わる→関連 required in practice; 険しい→困難, 険しい→大変, 終了→卒業 and 開通→繋ぐ conservative with a real basis; 障子→雨戸 and 関わる→扱う conservative and harmless. |

Cross-batch note: links to absent targets stay plain. Eight EN link targets in this batch's new cards (9 occurrences)
are absent from RU: the kanji cards 筆 (from 随筆), 防 (from 防止 and 防犯) and 接 (from 間接); and the word cards 学科 (from
学会), 解散 (from 集合), 埋める (from 隙間), スタート (from ストップ) and 解放 (from 開放). EN has kanji cards for all three of
those kanji; the other written kanji without an RU kanji card, 妨, 属, 締, 附, 随, 隔, 隙 and 障, have none in EN either. 開始
in 終了:31 stays plain, as in EN. No links were held from Batch 228.

## Final exclusion set

All 174 EN exclusion entries (27 lists) are retained in EN order. Nine direct, one-sided entries are added on six new
cards (no new list):

- Required in practice (2): 締め切り→締め切る and 関わる→関連, added at the candidate.
- Conservative with a real basis (5): 険しい→困難, 険しい→大変, 終了→卒業 and 開通→繋ぐ, added at the candidate; 締め切り→期間,
  added by fix 1 (consistency F1).
- Conservative, harmless (2): 障子→雨戸 and 関わる→扱う, added at the candidate.

Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added; the author's reverse 締め切る→締め切り was removed before the
candidate commit.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (締め切り); the 社会 link and 防止 optional items were adopted.
- Scoped coverage: **CLEAN** after fix 1 (締め切り, 障子, 開通, 締め切る, 防犯 and 関わる).
- Comprehensibility: **CLEAN** after fix 1 (障子, 開通, 締め切る, 防犯, 期限, 関わる and 隔てる; the 終了, ストップ and 防止
  optional items adopted); the declined F8 was withdrawn for this batch, and the 集会, 随筆 and 間接 notes remain optional.
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after fix 1 (締め切り→期間), including the 期限 and 隔てる retitles. This covers the reviewed batch
  and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them; the comprehensibility recheck did not
  re-read the other 18 cards. The unchanged cards rest on review 001, in which the correctness and comprehensibility
  reviewers read all 30 cards in full against EN and the consistency reviewer read all 30 cards in full and compared
  their front matter and links with EN.
- The correctness recheck was a bounded diff recheck; it reused initial-review evidence where the Japanese and the claim
  were unchanged and fetched fresh Jisho/JMdict entries only for 張り替える, 機械, 開通, 隔てる and 期限. The consistency
  reviewer did not reopen dictionary pages, and its necessity classes are judgements, not measurements. The
  comprehensibility reviewer did not re-fetch dictionaries, run the validator or audit quiz exclusions at recheck.
- The correctness reviewer's initial Gramota requests met HTTP 429, and no raw JMdict XML check is claimed;
  «состоять при учреждении» received no independently fetched Russian dictionary example.
- The consistency reviewer saw CR bytes in the working tree, which uses checkout line-ending conversion; the
  coordinator's byte scan found no CR in the 32 candidate content files.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
