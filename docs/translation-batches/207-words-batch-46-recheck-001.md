# Batch 207 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `ec1539c9b30591d1c207da84d96fa008d29c8e80` | `612e941814aefda3a8cbcf6072c15b22ba72bae2` | Initial review snapshot: the signed candidate, pushed before review. |
| `9fb6ed874252b9ff6edfb5ed6c13efcc7cef2d22` | `5c935d5f175d01c25e51cd5f1830fc08c8d31a6a` | Final candidate: review fixes plus the intake refresh, committed signed and pushed before the rechecks. |

The final candidate changes 11 word files and regenerates `manifest.json` (`contentVersion` `210f3259d83cc10f`) and the intake;
only those 11 word hashes differ in the manifest:
- `提出`: line 15 defines the noun as the act, «提出 — существительное со значением «подача, сдача чего-либо».», instead of
  «…: то, что представляют или сдают». Line 33 quotes 出す as «выносить; сдавать», following EN's contextual quote "put out; hand
  in", instead of «вынимать; сдавать», which matched neither EN nor the RU 出す title «вынимать; выносить».
- `不利` (line 29), `握手` (29), `批評` (27-28) and `批判` (29): the reading joins return to EN's hiragana, «ふ + り», «あく + しゅ»,
  «ひ + ひょう» with the following «ひょう», and «ひ + はん». The surrounding «Онные чтения»/«Чтение» follows each EN sentence.
- `不利`: line 42 says «одни и те же условия могут быть 不利…» instead of «одно и то же устройство…», for EN "arrangement".
- `指す`: the title and H1 become «указывать на что-либо» instead of «указывать (пальцем); иметь в виду» (EN "point; indicate").
  No other file quoted the old title.
- `手品`: lines 41-42 delete «В английских глоссах словаря встречается и устаревший перевод juggling («жонглирование»), но на
  него не стоит опираться.» and rewrap; the Russian contrast with жонглирование is kept.
- `抱く`: line 26 ends «…Это тоже переходный глагол годан.» without «…но в просмотренной записи он не помечен как сленг».
- Quiz exclusions only: `交換` `[取り替える, 代わり, 両替]`, `掴む` `[握る, 捕まえる, 理解]`, `持ち上げる` `[上げる, 立てる]`.
- No internal link, reading or Japanese example changes; the only front-matter changes are the 指す title and the three
  exclusion lists.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer reread its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

Rechecks ran serially.
Each reviewer received only:
- its facet's original blind report;
- the coordinator's dispositions of its findings and optional items;
- a short description of each change made in response to the other reviewers, without their reports;
- the revised snapshot;
- the actual diff command `git diff ec1539c 9fb6ed8`.

The disposition message to the comprehensibility reviewer misquoted 持ち上げる's frozen EN title as "lift; raise; flatter"; the
actual title is "lift up; flatter". The reviewer read the card itself, and the item it concerned stayed optional and unchanged.

The recheck prompts forbade running `tools/build_manifest.py` or any other generator; all three reports state that none was
run. The correctness reviewer ran `tools/validate.py` with `PYTHONDONTWRITEBYTECODE=1`; the consistency reviewer ran it and
deleted the `tools/__pycache__` it created. After every recheck the coordinator confirmed that HEAD was still `9fb6ed8` and
that `git status --porcelain --ignored` was empty.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | `9fb6ed8` | The reviewer read every changed passage with its EN and RU context, and the new exclusion targets as needed. C1 is resolved: `提出.md:15` defines the act, matching EN and Digital Daijisen, and keeps the 提出する sentence. C2 is resolved: the four cards reproduce EN's hiragana joins, including the second ひょう. Regression check against freshly inspected Jisho/JMdict entries: 出す senses 2-3 support «выносить; сдавать»; «условия» renders EN's "arrangement"; «указывать на что-либо» covers pointing and indication without a literal finger; the deleted 手品 and 抱く remarks were editorial and remove no Japanese teaching rule; the four new exclusions are direct overlaps supported by 交換/両替 (exchange; money exchange), 捕まえる sense 2, 理解 sense 1 and 立てる sense 1. `tools/validate.py` reported 0 errors. Correctness and scoped coverage are **CLEAN**; no optional items. |
| Consistency | `9fb6ed8` | The reviewer read the full diff, checked the new exclusions for format, conflicts and reverse references across all RU cards, screened the new 指す title against all RU titles, and checked manifest and intake hashes. F1, F2 and F3 are resolved; the reviewer accepted the low-severity reassessment of F1 as an overlap inherited from EN. F4 is resolved with the modified remedy: «выносить; сдавать» is an EN-parity contextual gloss, and 出す's body mentions сдача. The new 指す title creates no collision: 示す «показывать; указывать» stays guarded, and 権利's «(на что-либо)» is only a qualifier. The optional 掲示→放送 and 手術→作業 guards stay not adopted. Every non-strokes manifest hash and all 40 intake hashes match; `tools/validate.py` reported 0 errors. Consistency and quiz safety are **CLEAN**. |
| Comprehensibility | `9fb6ed8` | The reviewer read the 11 changed passages with their surrounding paragraphs. C1 is resolved: the 指す title and H1 match the body's pointing, clock and shogi examples and its statement that a finger is not required. C2 is resolved: 手品 keeps the Russian contrast, and the rewrapped paragraph is grammatical. C3 is resolved: 抱く keeps the bookish register and the feeling sense. The optional 不利 wording is adopted and resolved. Regression check: 提出's act definition sits naturally beside its を/に pattern; the hiragana joins match the word readings and keep the long vowel in ひょう; the exclusion edits are metadata only. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 提出 defines the submitted item, not the act | **Resolved** | `提出.md:15`; frozen EN 提出; Digital Daijisen 提出. |
| Correctness C2: katakana reading joins in 不利, 握手, 批評, 批判 | **Resolved** | `不利.md:29`, `握手.md:29`, `批評.md:27-28`, `批判.md:29`; frozen EN. |
| Consistency F1: 交換–両替 unguarded | **Resolved** (severity reassessed low; conservative guard) | `交換.md:9`. |
| Consistency F2: 掴む–捕まえる and 掴む–理解 unguarded | **Resolved** | `掴む.md:9`. |
| Consistency F3: 持ち上げる–立てる unguarded | **Resolved** | `持ち上げる.md:9`. |
| Consistency F4: 提出 misquotes 出す | **Resolved** (modified remedy: EN's contextual quote rather than the RU title) | `提出.md:33`; frozen EN 提出. |
| Consistency optional: 掲示→放送 and 手術→作業 guards | **Optional, not adopted** | 掲示's and 手術's titles are qualified; the reviewer rated both nonblocking and agreed on recheck. |
| Comprehensibility C1: 指す title teaches a finger restriction and an untaught sense | **Resolved** | `指す.md:4,12`. |
| Comprehensibility C2: English-dependent juggling aside in 手品 | **Resolved** | `手品.md:40-42`. |
| Comprehensibility C3: dictionary-markup aside in 抱く | **Resolved** | `抱く.md:25-26`. |
| Comprehensibility optional: 不利 «условия» | **Optional, adopted** | `不利.md:42`. |
| Comprehensibility optional: 持ち上げる title leads with «приподнимать» | **Optional, unchanged** | The title renders EN "lift up; flatter", the body says «поднимать», and the 立てる overlap is now guarded. |
| Comprehensibility title-screen leads: 抜ける/降る, 手術/作業 | **Optional, unchanged** | Disjoint qualifiers; 手術 is limited to surgery. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN** after fixes (提出).
- Scoped coverage: **CLEAN** after fixes (verbatim reading joins).
- Comprehensibility: **CLEAN** after fixes (指す, 手品, 抱く).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after fixes, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

Limits: the rechecks reread only the changed passages and the cards needed to judge them; unchanged cards rest on review 001's
full reading. The correctness reviewer freshly inspected the Jisho/JMdict entries for 出す, 捕まえる, 理解, 立てる, 指す, 手品 and
抱く; the consistency and comprehensibility reviewers did not refetch dictionary pages. No native-speaker, learner, app-import,
device, media, activation or release acceptance is claimed.
