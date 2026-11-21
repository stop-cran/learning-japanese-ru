# Batch 229 — independent review 001

## Snapshot and scope

- Reviewed commit: `af5541a48700cdb110c81f127f63f226ead77ae7` (tree `c17dd3521821d417879b7f68fd6d1d74c9cd88c8`), branch
  `full-ru-229-words-68`, parent `963e9ba`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 228 candidate `e2b0bdba512f72ca587ad5d2cb553b0edb22016a`.
    Before copying, the coordinator checked two things: that the 2 navigation files edited there were unchanged between
    `e2b0bdb` and the candidate's parent `963e9ba`, and that none of the 30 new cards existed in the primary checkout. The
    Batch 228 fixes touched only 交流, 合同, 広さ, 打ち合わせ, 鈍い, 零点, 電力, 青少年 and 面積; none of them is in this
    batch's path set.
  - The coordinator byte-compared the 32 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 32 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - No wraps were held from Batch 228, and the coordinator applied none separately; all three navigation links were
    copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made these edits:
    - removed the author-added sentence «Это канго — слово, построенное на онных чтениях кандзи.» from 20 cards (学会 期限
      終了 警備 閉会 開会 開放 開通 間接 間隔 関東 関西 防止 防犯 附属 限度 随筆 障子 集会 集合): EN keeps kango only in front
      matter (type/tags), and 0 of 1,487 published RU kango cards carry such a body sentence;
    - kept 属する:25's kango framing, because EN :29 itself says "The Chinese-derived base is read ぞく here, followed by
      する", rendered with the qualified wording «условно отнесено к канго — словам, построенным на онных чтениях кандзи»;
    - removed the reverse exclusion 締め切る→締め切り (the author had added both directions; the app applies exclusions
      symmetrically) and kept the RU-added 締め切り→締め切る;
    - kept the RU-only link 開会→閉会 (reciprocal of EN 閉会→開会; both cards are in the batch) and flagged it to the
      reviewers as RU-only.

    After these edits `tools/build_manifest.py` recorded 4,989 files and `tools/validate.py` reported 0 errors.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 2 files with 3 restored navigation links (one kanji card and one word card);
    - `manifest.json` (`contentVersion` `a8cdce1105990d1c`, 4,989 entries);
    - the intake.
- Published baseline recorded in the intake: `5c318874d589b0383e8c1f7bffa0373a39c991aa` (Batch 228 merge). Parent
  `963e9ba` adds only the Batch 228 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK (the authoring worktree run reported 124 tests);
  - content budget: OK;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 2 files and 3 links, with no problem;
  - title screen: no exact title-segment overlap (291 stem-only `!!` lines and 43 `OK` lines);
  - link parity: no EN link lost where the RU target exists, and one new RU-only link to an existing card at a substantive
    comparison: 開会→閉会. EN 開会:29 names 閉会 in plain text at the same place, and EN 閉会:31 links 開会.
- Common sample: all three reviewers read all 30 new word cards in full and the two navigation diffs. The correctness
  and comprehensibility reviewers read each card against its full EN original; the consistency reviewer compared each
  card's front matter and link set with EN by script and read the RU text in full.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN, the runtime changes to `kanji/了.md`, `words/感覚.md` and
    `manifest.json`, the binding RU instructions and format reference, and the baseline convention samples 付く, 厳しい,
    作文 and 直接 in full.
  - Read the complete matching Jisho/JMdict API entries for all 30 words, including every returned sense, reading,
    spelling and grammatical tag. Japandict entries for 険しい, 峻しい, 隨筆 and 距てる corroborated entry ids and
    search-only tags. No raw-XML check is claimed.
  - Japanese sources beyond Jisho: Digital Daijisen headings on Weblio for 集会, 集合, 障子, 随筆, 険しい, 属する, 附属,
    締め切り, 締め切る, 終了, 差し支え, ストップ and チェック.
  - Russian sources: Kuznetsov entries for хмурый, очерк and эссе; Russian Wiktionary entries for сёдзи, отгораживать,
    состоять, прилагать, недопущение, косвенность, опосредованность, настежь, митинг, съезд and общество; Efremova
    труднопроходимый; Lingust lesson 6 and Japanese Simple lesson 4 for ваго, канго, гайрайго and «онные чтения»
    (terminology checks, not endorsement of those courses); a Japan encyclopedia entry for Кансай. Gramota later
    returned HTTP 429, and inaccessible pages were not used.
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 cards in full, compared their front matter and link multisets with EN by script, and read the `-U0`
    diffs of the two navigation files against EN 了 lines 28 and 33 and EN 感覚 line 33.
  - Recomputed the SHA-256 of the manifest entries against the working tree (every non-stroke entry matches) and checked
    that the intake's 32 payload paths equal the 30 words plus `kanji/了.md` and `words/感覚.md`.
  - Ran `tools/validate.py` (0 errors), `word_title_screen.py` (used as leads only), a link-resolution script and a Jisho
    API lookup for 雨戸, 困難, 大変, 卒業, 関連, 扱う, 繋ぐ, 障子, 隔てる and 間. It did not open Daijisen or Weblio pages.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN and the link-only diffs of `kanji/了.md` and `words/感覚.md`, and compared the
    titles of named near-synonyms where those RU cards exist.
  - Limited dictionary re-fetches to the claims behind its findings. It did not machine-screen whole-deck title
    collisions (`word_title_screen.py` and `link_parity.py` not run), and it ran no validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. Each report records
  the snapshot `af5541a` with an empty `git status --porcelain`. No fix was applied until all three reports were
  complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `229-words-batch-68-review-correctness-001.md`
  - `229-words-batch-68-review-consistency-001.md`
  - `229-words-batch-68-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The correctness report says that it consulted no author or reviewer reports, tracking ledger or scratch worktrees. The
  consistency report says that it did not read any author report, other review report, `docs/translation-batches/`
  (apart from the intake path list) or `docs/translation-drafts/`; it checked the intake's path list, which its
  assignment included. The comprehensibility report says that it did not read other review reports, batch records or
  scratch worktrees.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for 締め切り, **CLEAN** for the other 29 new cards; scoped coverage **NEEDS FIX** for
締め切り, **CLEAN** for the other 29. Comprehensibility and whole-deck quiz safety were not assessed.

- F1 (minor, correctness and scoped coverage; high confidence), `締め切り.md:27`: «Отдельное физическое значение — закрытая
  дверь или окно» turns the physical closing or keeping-closed action into the door or window itself, and the rest of the
  paragraph explains only an applications notice, dropping EN's explanation that a physically closed opening can account
  for an entry notice. The deadline sense and examples are sound, so severity stays minor. Remedy: describe the closing
  of a door or window and keeping it closed, add that the word can name a place closed that way, and restore the
  context-dependent notice explanation. Evidence: JMdict 1594590 sense 2 "closing (a door, window, etc.)", also written
  閉め切り, on the Jisho API; Digital Daijisen しめ‐きり sense 1 «戸・窓などを、閉じたままにすること。また、閉じられたままの場所»;
  frozen EN's corresponding paragraph.

What the reviewer confirmed:
- Japanese main examples were preserved; original reading, level, type, kanji and tags were retained. Existing exclusions
  were retained, with additional exclusions on six cards. No broken link or dropped EN link with an available RU target
  was found; untranslated references left as plain text were not penalized. The baseline runtime edits are links to new
  cards, not changed Japanese explanations.
- Suru transitivity is correctly distinguished for 終了, ストップ, 開通, 開会, 開放 and 閉会; the Russian translations need
  not mechanically copy Japanese voice when the event and the explicit Japanese rule remain accurate.
- Daijisen チェック sense 4 covers screening that keeps unsuitable things out, so 防止's qualification is not an invented
  sense. «хмурый» is not confined to sadness, and «очерк» and «эссе» support practical overlapping glosses for 随筆.
  The 学会 contrast between an association and society at large is substantively sound, and «митинг» fits the
  peace-rally example without being imposed as 集会's only meaning.
- 隔てる's «стоять между» is compressed, but its river example and the explicit が/を versus を隔てて explanation preserve
  the roles; JMdict 1206360's senses do not establish a categorical error.

Optional: link 社会 in 学会:33 as `[社会](社会.md)（しゃかい）`, since the sentence introduces it as a substantive RU-only
comparison and `社会.md` exists; outside its facets, drop the process wording «написание из исходного списка» from
締め切り:16, and reword 防止:31's «не совсем не связаны». Limits: public dictionary mirrors, not a pinned raw JMdict XML
snapshot; Gramota returned HTTP 429 and several alternative sites blocked requests, and «состоять при учреждении» did not
receive an independently fetched Russian dictionary example; regional naming and instructional terminology received usage
checks only; no native-speaker, frequency-corpus, device or exhaustive cross-deck title/exclusion audit is claimed.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **NEEDS FIX** (one minor finding); scoped coverage (cross-file integration)
**CLEAN**. Correctness and comprehensibility were not assessed.

- F1 (minor, quiz safety; medium confidence), `締め切り.md:9`: the RU title «срок сдачи; окончание приёма (заявок)»
  introduces the bare word «срок», which EN's "deadline; closing" does not, so 期間 «срок; период» reads as a defensible
  correct answer for 締め切り, and neither card declares the pair (期間 declares only 時間, 時代 and 間). EN guards 期限
  against 期間 and 定期 for the same lead word. Remedy: `quiz_exclusions: [期限, 終わり, 仕舞い, 締め切る, 期間]`; 定期
  «установленный срок; по графику; проездной» is a weaker analogue that the reviewer did not require. Confidence is medium
  because the classification of «срок» as defensible is a judgement about Russian usage; the missing direct pair is
  certain.

What the reviewer confirmed:
- Front matter and tags equal EN on all 30 cards apart from the eight RU-added exclusions; every EN exclusion is retained
  in EN order, with the RU additions appended at the end; 関西, 関東 and 間接 have no `quiz_exclusions` key, as in EN. No
  dangling, duplicate or self exclusion.
- Link-target multisets equal EN on all 30 cards except the absent targets left as plain text (学科, 解散, 埋める, スタート
  and 解放; the kanji 筆, 防 and 接) and the RU-only link 開会→閉会, which it accepted as an antonym pointer with its own
  gloss. Every RU link resolves. 附属's statement that neither 附 nor 属 has a card is accurate.
- `kanji/了.md` lines 28 and 33 and `words/感覚.md` line 42 differ from the parent only by the added link brackets and
  hrefs, in EN's href forms; no other 終了 or 間隔 mention remains plain in those files.
- Every non-stroke manifest entry matches the working tree; the intake's 32 payload paths equal the content diff, with
  `held: []` and no learner content. `contentVersion` changed once, and no generated or unrelated file is in the diff.
- One-way in-batch declarations suffice because the app applies them symmetrically. The in-batch groups (学会/集会/集合,
  間隔/隙間, 期限/限度/締め切り/締め切る, 属する/附属, 差し支え/妨げる, 終了/ストップ/閉会, 防止/警備/防犯, 関西/関東 and
  開通/開会/開放) stay visibly distinct. It agreed that none of the pairs the author had declined to guard is required.

Optional: O1, 学会's «как 社会（しゃかい）» and 終了's «開始（かいし）— «начало»» could link the existing `社会.md` and
`開始.md` (parity-neutral either way); O2, 隔てる–間 and 差し支え–困る/困難 share a Russian word or root but differ in part
of speech and sense, and need no guard; O3, 障子→雨戸 could be dropped without loss. Limits: dictionary evidence for the
classification came from the JMdict entries cited in the cards and the Jisho API, without Daijisen or Weblio pages;
defensibility judgements concern displayed Russian titles, not the app's actual distractor selection; the app source was
not read; translation accuracy was not assessed; the `strokes/*.json` manifest mismatches it saw were attributed to the
local CRLF checkout, not verified against a clean LF checkout.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** for 障子, 開通, 締め切る, 防犯, 期限, 関わる, 隔てる and 締め切り (the other 22 new
cards CLEAN on this facet); scoped coverage **NEEDS FIX** for 障子, 開通, 締め切る, 防犯 and 関わる, **CLEAN** for the other
25. The link-only 了 and 感覚 edits have no new learner-text defect.

- F1 (moderate, also coverage; high confidence), `障子.md:19`: «Я заменил бумагу на сёдзи» parses as заменить A на B, so
  the learner is told the paper was replaced by a shoji, reversing 障子の紙を張り替えました. Remedy: «Я переклеил бумагу на
  сёдзи.» Evidence: JMdict 張り替える sense 1 "to re-cover; to repaper"; EN "I replaced the paper on the shoji".
- F2 (moderate, also coverage; high confidence), `開通.md:19–20`: 開通する is taught as intransitive, but «Телефонную
  линию подключили» and «Дорогу … снова открыли» are agentive, so a learner can take the forbidden 道路を開通する pattern
  from the Russian. Remedy: «Телефонная линия заработала.» and «Дорога, которая была перекрыта, снова открылась для
  движения.» Evidence: JMdict 開通 senses 1–2; EN "The road that had been closed to traffic reopened".
- F3 (moderate, also coverage; high confidence), `締め切る.md:19`: the card teaches a transitive godan verb, but «Приём
  заявок на участие закончится завтра» is intransitive and has no closer. Remedy: «Завтра мы закроем приём заявок на
  участие.» Evidence: JMdict 締め切る senses 1–2; EN "We will close applications".
- F4 (moderate, also coverage; high confidence), `防犯.md:18`: «Чтобы защититься от преступников» turns crime prevention
  into self-defence against criminals. Remedy: «Чтобы предотвратить преступления, я на ночь всегда запираю дверь.»
  Evidence: JMdict 防犯 sense 1 "prevention of crime"; EN "To prevent crime, I always lock up at night".
- F5 (moderate; high confidence), `期限.md:4,12`: the lead gloss «срок действия» names the validity period of a document,
  contract or medicine, while the examples are an application deadline and a return deadline. Remedy: title and H1
  «установленный срок; крайний срок». Evidence: JMdict 期限 senses 1–2; EN "deadline; term; time limit".
- F6 (minor, also coverage; high confidence that the example fails the card's contrast, medium that a dictionary would
  forbid the verb), `関わる.md:18`: «Я участвую в новом проекте» uses the verb the same card assigns to 参加 at :29 and
  hides that contrast. Remedy: «Я вовлечён в новый проект.» Evidence: card line 29; EN "I am involved in the new project".
- F7 (minor; high confidence), `隔てる.md:4,12`: the title segment «стоять между» adds standing and sounds intransitive,
  while the body and examples use «находиться или иметь что-то между», «разделяет» and «сели … через стол». Remedy: title
  and H1 «отгораживать; иметь между собой». Evidence: JMdict 1206360 senses 1–3; EN "separate; have between".
- F8 (minor; high confidence), `締め切り.md:16`: «написание из исходного списка» is an editorial note, and a beginner has no
  source list. Remedy: «**締切** и **締切り** передают то же слово с тем же чтением.» Evidence: EN has the same note, which
  the reviewer held does not make it learner Russian.

Optional: 終了:19 «На этом объяснение закончено» is resultative while 説明を終了します is the speaker ending it («На этом я
заканчиваю объяснение»); ストップ:18 «Машина внезапно остановилась» reads as a car («Механизм внезапно остановился»); 集会
«митинг», 随筆 «очерк» and 間接 «опосредованность» are narrower or harder than the bodies, which explain them; 防止:31's
«не совсем не связаны» is awkward. Outside its facets and unscored: 閉会's exclusions omit 開会, and 期限's omit 締め切り.
Limits: whole-deck title collisions were not machine-screened; named risk-pair titles were checked directly; dictionary
re-fetches were limited to the claims behind its findings; no native-speaker or frequency claim; no validator run.

## Exclusion classification

All 174 EN exclusion entries (27 lists) are retained in EN order; 関西, 関東 and 間接 have none. Eighteen of them lie inside
the batch. At the candidate, eight direct, one-sided entries were added on six new cards; none is a new list or targets a
batch word except 締め切り→締め切る.

| Entries | Consistency reviewer |
|---|---|
| 締め切り→締め切る, 関わる→関連 (2) | required in practice |
| 険しい→困難, 険しい→大変, 終了→卒業, 開通→繋ぐ (4) | conservative with a real basis |
| 障子→雨戸, 関わる→扱う (2) | conservative; necessity not established, harmless |

締め切り «срок сдачи; окончание приёма (заявок)» and 締め切る «плотно закрывать; прекращать приём (заявок)» share «приём
(заявок)», and 関わる «быть вовлечённым; иметь отношение (к чему-либо)» is a sense neighbour of 関連 «связь; отношение к
теме», whose sibling 関係 EN already guards. 険しい's figurative difficult-road sense shares «трудный» with 困難 «трудность;
трудный» and 大変 «трудный; серьёзный», consistent with EN's 険しい→難しい; 終了 «окончание (мероприятия, процесса)» shares
«окончание» with 卒業 «окончание учёбы»; 開通 «открытие движения; подключение (линии связи)» shares «подключ-» with 繋ぐ
«соединять; подключать». 障子 «сёдзи (бумажная раздвижная перегородка)» and 雨戸 «наружная раздвижная защитная ставня»
share only «раздвижная», and 関わる and 扱う «иметь дело (с чем-либо); обращаться (с людьми, вещами)» name different senses;
the reviewer kept both as harmless. All eight entries are kept. The correctness reviewer noted that the additions delete
no EN guard without auditing quiz safety, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`229-words-batch-68-recheck-001.md`.
