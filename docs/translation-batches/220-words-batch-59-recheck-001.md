# Batch 220 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `19bcfe00f202ae1368ffc4422b38d9b1da172c2e` | `6c90c32e275e1f0b28692443c41fdd228aad6c76` | Initial review snapshot: the signed candidate, pushed before review. |
| `024fc98e70c09c7c7ea6e14d28e5910fb34783bb` | `7f9dab57f301e1066ac71d78f95cfeddbdbeb290` | Fix 1 (final candidate). It covers the correctness finding, the two consistency findings, the six comprehensibility findings, the adopted correctness optional item, the adopted comprehensibility optional item and the intake refresh. Signed and pushed before the rechecks. |

The fix changed nine word files and regenerated `manifest.json` (`contentVersion` `c99920e2800e90d6`, 4,719 entries; the
candidate had `38324799df00beb4`) and the intake:
- `一人一人` (line 30): the 個人 comparison now ends «一人一人 же выделяет каждого члена группы в отдельности, не
  обязательно задавая порядок.» instead of «…перебирает всех членов группы по очереди.» (correctness C1, as proposed).
  Digital Daijisen 一人一人 1 「多くの中のそれぞれの人。めいめい。各人」; the card's line 34 and EN line 32.
- `一層` (lines 4, 12 and 16): title and H1 «ещё сильнее; ещё больше» instead of «ещё сильнее; тем более», and the opening
  reads «наречие со значением «ещё сильнее» или «ещё больше».» (correctness optional item and comprehensibility C3,
  adopted jointly). japandict «[ещё] больше; [ещё] более»; EN "even more"; Kuznetsov lists «тем более» as an emphatic
  particle («=Особенно»), and Russian Wiktionary as a particle introducing a further argument. «Тем более» is no longer
  used; no example used it.
- `ワイン` (line 9): `quiz_exclusions: [酒, お酒]` (consistency F1, accepted and extended). 酒 «алкогольный напиток;
  сакэ» is a hypernym; お酒's title «алкогольный напиток» repeats 酒's first segment, so it is a second answer of the same
  kind. 飲み物 was not added: no existing drink card (コーヒー, お茶, 紅茶, 水, 牛乳) guards it.
- `ラケット` (lines 9 and 21): `quiz_exclusions: [道具]` (consistency F2, adopted as a conservative guard; the card calls
  道具 the broader category, and ピアノ→道具 is a precedent), and «Одолжите мне, пожалуйста, ракетку для настольного
  тенниса.» instead of «Дайте…» for 貸してください (comprehensibility optional item, adopted; EN "Please lend me").
- `一般` (lines 4, 9, 12, 18 and 21), comprehensibility C1, accepted:
  - Title and H1 «общий; обычный» instead of «рядовой; всеобщий» (EN "general; ordinary"; Ozhegov «рядовой»: rank and
    file, the military rank; «всеобщий» was stronger than the card's own note that 一般に is not universal).
  - Line 18: «Этой библиотекой могут пользоваться и обычные посетители.» instead of «…и посторонние посетители.»
  - Line 21: 一般的な is glossed «общий; типичный» instead of «общий; обычный», so that it does not repeat the new title
    verbatim (JMdict 一般的 "general; popular; typical").
  - `quiz_exclusions: [普通, 共通, いつも, たいてい, 普段]` instead of `[普通]`. 共通 «общий (для нескольких);
    совпадающий» shares the exact segment «общий» (RU-introduced; EN "shared; in common"), so it is required; いつも,
    たいてい and 普段 share only the stem «обычн» («обычно»), a cluster that 普通 and 普段 already guard internally, so they
    are conservative.
- `不正` (lines 4 and 11): title and H1 «нечестность; неправильность» instead of «нечестность; злоупотребление;
  неправильность» (comprehensibility C2, accepted). Kuznetsov «злоупотребление» includes misuse of a substance; EN
  "wrongdoing; dishonesty; irregularity"; the body is unchanged.
- `上京` (line 20): «Я поехал в Токио, чтобы поступить в университет.» instead of «Я переехал…» (comprehensibility C4,
  accepted). Line 18 says 上京 does not require a permanent move; EN "I went to Tokyo to attend university".
- `ロケット` (line 24), comprehensibility C5, adapted: «Оба слова пишутся одинаково катаканой, с маленьким ッ перед ト.
  Это разные заимствования из английского: катакана передаёт английские звуки «р» и «л» одним и тем же рядом
  ラ・リ・ル・レ・ロ, поэтому оба слова совпали. Кандзи, по которым можно было бы восстановить различие, нет.» instead of
  «…Английские rocket и locket совпали в виде ロケット, включая маленькое ッ перед ト.…». It keeps the loan-origin point
  without requiring the English words; the reviewer's «а не два значения одного слова» is already stated in «Оттенки
  значения».
- `メモ` (lines 4, 9, 12, 16, 25 and 30), comprehensibility C6, accepted:
  - Title and H1 «записка; заметка» instead of «пометка; записать для памяти» (Ozhegov «пометка»: a mark or inscription,
    for example in a margin; EN "note; memo; jot down"; メモする stays taught in the body).
  - Body: «записка; заметка», «делать заметки» and «короткая заметка» instead of «пометка», «пометки» and «пометка».
  - Line 25: «メモ — катаканное заимствование из английского языка.» instead of «…соответствующее английскому memo —
    «памятная записка».», since «памятная записка» is in Russian a formal (diplomatic) memorandum, which line 34 says
    the word need not be.
  - `quiz_exclusions: [記録, 手紙, 栞, 記事]`: 記事 «статья (в СМИ); заметка» shares the exact segment «заметка»
    (RU-introduced; EN "article; news story"), so it is required.
- The intake note now names the fixed cards, and the nine candidate hashes were refreshed.

Before the commit, the coordinator's word title screen on the changed titles found every exact segment overlap guarded:
一般–普通 and 一般–共通, 一層–更に, メモ–手紙 and メモ–記事. Stem-only neighbours were listed in the recheck briefs: いつも,
たいてい and 普段 (now guarded) for 一般; 嘘 «ложь; неправда» («непра», unchanged from the candidate title; EN guards
neither) for 不正; incidental «больш» and «сильн» stems for 一層, whose «сильн» neighbours already existed with the
candidate title; だいぶ and てかてか («замет») and 予約 and 申し込む («запис», already present with the candidate title) for
メモ; and ロケット «ракета; медальон» for ラケット (different answers, pre-existing).

Net change from the candidate: four retitles (一般, 不正, 一層, メモ) with an adjusted opening in 一層 and body wording in
メモ, three example translations (一般, 上京, ラケット), one qualified comparison (一人一人), one rewritten kanji-section
sentence (ロケット), one 一般的な gloss and eight added exclusion entries on four cards (ワイン, ラケット, 一般, メモ). No
Japanese example sentence, sourced reading, EN exclusion or link changed.

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
- the actual content diff from `19bcfe0` to `024fc98`, inline;
- the coordinator's evidence for every change, the title-screen results and the declined items, stated without the other
  reviewers' reports;
- the reviewer's original verdicts and the disposition of each of its own findings.

All recheck messages forbade running `tools/build_manifest.py` or any other generator. Every recheck section states that none was run. The consistency reviewer ran `tools/validate.py` (0 errors); the correctness reviewer ran no validator, and the comprehensibility reviewer reported running none and did not re-run the title screen. After every recheck the coordinator confirmed that HEAD was `024fc98` and that `git status --porcelain --ignored` was empty.

### Round 1 (`024fc98`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer read every changed passage in the nine cards, each complete revised RU card and its complete frozen EN original, and re-inspected JMdict entries (through the Jisho API) for 一般, 一般的, 不正, 上京, メモ and 貸す. C1 is resolved: the replacement removes obligatory order and agrees with the card's nuance section. The adopted 一層 refinement is resolved: the degree gloss agrees with the examples. Regression checks: 一般's title keeps general/ordinary, «обычные посетители» fits the general public here and the public/special-group distinction is retained, and 一般的な keeps adjectival attachment; 不正's shorter title loses no necessary sense; 上京's translation keeps past travel to Tokyo without asserting relocation; ロケット's ラ-row sentence correctly explains the spelling convergence; メモ's noun title fits the examples and the body still teaches メモする; ラケット's request correctly asks the listener to lend; ワイン and the added exclusions introduce no linguistic regression. Correctness and scoped coverage are **CLEAN**, with no findings outstanding. |
| Consistency | The reviewer confirmed that the diff from `19bcfe0` touches exactly the nine cards, `manifest.json` and the intake. F1 is resolved: `[酒, お酒]` is well-formed and both targets exist; 酒 is required as the hypernym and お酒 repeats 酒's first title segment. F2 is resolved as the conservative guard it suggested: 道具 exists and the card calls it the broader category; «Одолжите» is faithful to EN "lend". The over-guard leads メンバー→参加 and 一言→要するに stay optional and declined. Regression checks: of the new exclusions, 共通 (exact segment «общий») and 記事 (exact segment «заметка») are required and いつも, たいてい and 普段 (stem «обычн» only) conservative; the four changed titles were screened against all published word titles, and every exact segment overlap is guarded (一般–共通/普通, 一層–更に, メモ–手紙/記事) while stem neighbours have different answers or are guarded; ロケット's edit is prose-only and it stays distinct from ラケット; `word`, `reading`, `jlpt`, `type`, `kanji` and `tags` are unchanged and no link was added or removed; all 4,714 `files` entries in the manifest re-hash correctly after LF normalisation, and the intake hashes match the nine changed cards. Consistency, quiz safety and scoped coverage of cross-file integration are **CLEAN**. |
| Comprehensibility | The reviewer reread the changed passages. C1 is resolved: 一般's title, H1 and library example read «общий; обычный» and «обычные посетители», the opening still bounds «общий» as ordinary or general rather than shared, and 一般的な «общий; типичный» does not repeat the title. C2 is resolved: «злоупотребление» is gone, and the body still separates cheating, improper conduct and technical irregularity from a mistake. C3 is resolved: «тем более» is gone and the examples still show degree. C4 is resolved: «Я поехал в Токио…» no longer contradicts the note that no permanent move is required. C5 is resolved as adapted: the ラ-row sentence explains the spelling collision without requiring the English words. C6 is resolved: the title is «записка; заметка», the English memo is gone and メモする remains in the body. The optional ラケット item is resolved: «Одолжите мне, пожалуйста» matches 貸してください. No regressions: the 一人一人 sentence agrees with the shade paragraph, and ワイン and the new exclusions change no learner prose. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 一人一人:30 «по очереди» makes sequential order part of the meaning (minor) | **Resolved** | `一人一人.md:30`; Daijisen 一人一人 1; JMdict 一人一人; the card's line 34 and EN line 32. |
| Correctness optional: 一層 «ещё больше; ещё сильнее» instead of «тем более» | **Optional, adopted** | `一層.md:4,12,16`; japandict; Kuznetsov «более». Adopted jointly with comprehensibility C3. |
| Consistency F1: ワイン has no guard against its hypernym 酒 (minor) | **Resolved** (extended) | `ワイン.md:9`; JMdict ワイン and 酒; RU 酒 and お酒 titles; テニス→スポーツ precedent. Extended to お酒. |
| Consistency F2: ラケット has no guard against generic 道具 (minor) | **Resolved** (as a conservative guard) | `ラケット.md:9`; JMdict 道具; the card's «более широкая категория»; ピアノ→道具 precedent. Adopted as conservative. |
| Consistency optional: drop the over-guards メンバー→参加 and 一言→要するに | **Optional, not adopted** | Harmless conservative guards; the reviewer did not require removal. Retained. |
| Consistency optional: 一瞬–ちょっと | **Optional, not adopted** | The reviewer found the overlap weak and claimed no defect; EN guards neither. |
| Consistency limit: `kanji/杯.md` links `[不](不.md)` where EN does not | **Outside this batch** | Present at `ff8310d`; outside this batch's path set. |
| Comprehensibility C1: 一般 «рядовой; всеобщий» and «посторонние посетители» (moderate) | **Resolved** | `一般.md:4,9,12,18,21`; Ozhegov «рядовой»; JMdict 1165790 senses 1–2; JMdict 一般的. |
| Comprehensibility C2: 不正 unqualified «злоупотребление» (minor) | **Resolved** | `不正.md:4,11`; Kuznetsov «злоупотребление»; JMdict 1493370. |
| Comprehensibility C3: 一層 «тем более» is a particle, not the degree adverb (minor) | **Resolved** (jointly with the correctness optional item) | `一層.md:4,12,16`; JMdict 1164340; Russian Wiktionary «тем более». Adopted jointly with the correctness optional item. |
| Comprehensibility C4: 上京 «Я переехал» asserts a change of residence (minor) | **Resolved** | `上京.md:20`; JMdict 1352980; the card's line 18. |
| Comprehensibility C5: ロケット's sentence works only through English rocket/locket (minor) | **Resolved** (adapted) | `ロケット.md:24`; JMdict 1147220 and 2862534. Adapted: the ラ-row explanation replaces the English words. |
| Comprehensibility C6: メモ «пометка; записать для памяти» and the memo equation (minor) | **Resolved** | `メモ.md:4,9,12,16,25,30`; Ozhegov «пометка»; JMdict 1133830. 記事 guard added. |
| Comprehensibility optional: ラケット «Дайте» loses "lend" | **Optional, adopted** | `ラケット.md:21`; EN "Please lend me". Adopted: «Одолжите». |
| Comprehensibility optional: 不自由 «стеснённость», 一家 «семейство», ヨーロッパ *Europa* | **Optional, not adopted** | The reviewer found each bounded by the body; *Europa* is the cited JMdict loan source, as in EN. Declined. |
| Comprehensibility optional: ラケット/ロケット cross-note | **Optional, not adopted** | EN omits it, and the Russian titles «ракетка» and «ракета» differ. Declined. |
| Exclusion classification | **Reviewer's classification adopted** | The author called 3 of the 24 candidate RU-added entries required; the consistency reviewer called 10 required, 4 conservative to required, 9 conservative and one (メンバー→参加) an unjustified but harmless over-guard. |

Cross-batch note: links to absent targets stay plain. Four EN link occurrences in this batch's new cards target four
absent RU files: 一般→kanji 般, 一層→kanji 層, ワイン→ビール and ワイン→ウイスキー. ビール is a Batch 221 word; its link
from ワイン is held for that batch. The other targets are not in Batch 221.

## Final exclusion set

All 26 EN exclusion entries (15 lists) are retained. Thirty-two direct, one-sided entries are added on 19 new cards:

- Required (14): 不足→欠ける, 不可→禁止, 下り→下りる, 下り→方向, 上京→東京, 一致→合う, 一致→偶然, 一体→全体,
  ヨーロッパ→欧州, メモ→手紙, and, added in the fix, 一般→共通, ワイン→酒, ワイン→お酒 and メモ→記事. The consistency
  reviewer found a basis for each candidate entry in the visible Russian titles or the dictionary; the fix entries share
  an exact title segment (共通, お酒, 記事) or are a direct hypernym (酒).
- Conservative (17): 不安→緊張, 不安→はらはら, 一生→命 and 一人一人→個人 (the reviewer's "conservative to required"),
  不自由→制限, 下り→降りる, 下り→坂, 一言→要するに, 一方→方, 一度に→同時, メンバー→委員, メモ→記録, メモ→栞, and, added
  in the fix, ラケット→道具, 一般→いつも, 一般→たいてい and 一般→普段.
- Retained over-guard (1): メンバー→参加. The titles already separate the cards; the guard only shrinks the distractor
  pool, and its removal was declined.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the fix (一人一人).
- Scoped coverage: **CLEAN** throughout.

- Comprehensibility: **CLEAN** after the fix (一般, 不正, 一層, 上京, ロケット, メモ).

- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after the fix (ワイン, ラケット). This covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the cards needed to judge them. The unchanged cards rest on review
  001's full reading.
- The consistency reviewer cited JMdict senses from memory rather than fresh lookups in its initial review; they support
  its guard classification, not a verdict.
- The pre-existing `kanji/杯.md`→不 link is outside this batch and unchanged.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
