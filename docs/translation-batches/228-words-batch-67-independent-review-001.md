# Batch 228 — independent review 001

## Snapshot and scope

- Reviewed commit: `e2b0bdba512f72ca587ad5d2cb553b0edb22016a` (tree `4b3cf06ecc0f1d128d13dbd4629a2239bfb59bd4`), branch
  `full-ru-228-words-67`, parent `f833f88`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 227 candidate `5cf2313776672567fd1454fffd027b253bb10278`.
    Before copying, the coordinator checked two things: that the 10 navigation files edited there were unchanged between
    `5cf2313` and the candidate's parent `f833f88`, and that none of the 30 new cards existed in the primary checkout. The
    Batch 227 fix touched only コレクション, 区切る, 境界, 時間割, 突く, 突っ込む, 集金, 雑音, 響き, 頂点, 預かる, 頭脳, 頼もしい
    and 飛び込む; none of them is in this batch's path set.
  - The coordinator byte-compared the 40 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 40 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - No wraps were held from Batch 227, and the coordinator applied none separately; all ten navigation links were
    copied from the authoring worktree.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 10 files with 10 restored navigation links (one article, three kanji cards and six word cards);
    - `manifest.json` (`contentVersion` `7a0ab3a14eee3339`, 4,959 entries);
    - the intake.
- Published baseline recorded in the intake: `7333eaf6d25bc802468c7b1d4730165229bf6a62` (Batch 227 merge). Parent
  `f833f88` adds only the Batch 227 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK (the authoring worktree run reported 124 tests);
  - content budget: OK;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 10 files and 10 links, with no problem;
  - title screen: no unguarded exact title-segment overlap (190 stem-only `!!` lines and 27 `OK` lines);
  - link parity: no EN link lost where the RU target exists, and six new RU-only links to existing cards at substantive
    comparisons: 広さ→面積, インタビュー→面接, 電球→明るい, 交流→直流, 交流→合流 and 乾電池→電池. EN names each target in
    plain text at the same place, except 交流→合流: there RU adds the sentence «[合流](合流.md)（ごうりゅう）— слияние потоков
    или присоединение к группе, а не взаимный обмен.», and EN mentions 合流 only in 交流's exclusions.
- Common sample: all three reviewers read all 30 new word cards in full and the ten navigation diffs. The correctness
  and comprehensibility reviewers read each card against its full EN original; the consistency reviewer compared each
  card's front matter and link set with EN and checked the EN lines it cited.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN, the ten link-only navigation passages, the binding content rules and
    selected existing RU cards for terminology.
  - Found all 30 primary JMdict ids in the actual Jisho pages ("Edit in JMdict" links) and inspected their glosses; API
    requests supplied readings, senses and restrictions where available. Initial API requests hit HTTP 429, and failed
    responses were not used. The official raw JMdict archive failed certificate hostname validation; TLS verification
    was not disabled, and no raw-XML check is claimed.
  - Japanese sources beyond Jisho: Digital Daijisen entries on Weblio for 静まる, 面接, 組み合わせ, 合同, 合流, 電力, 採点,
    点数, 零点, 乾電池, 青少年 and 打ち合わせ, and the Nipponica article 乾電池 on Kotobank.
  - Russian sources: Gramota and Kuznetsov entries for муторный, тугодум, габарит, гробовой, протяжённость, батарея,
    аккумулятор, площадь, элемент, лампа, тряпка, слить and the tailoring sense of запа́х; Russian Wiktionary конгруэнтный;
    Russian-language geometry and algebra lessons for equal triangles and «нуль функции» (usage checks, not certification
    of those courses).
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 cards in full and the complete `-U0` diffs of the ten navigation files, and compared every mention of
    each target in EN and RU (10 of 10).
  - Hashed all 4,836 non-stroke `manifest.json` entries against the working tree (0 mismatches) and checked that the
    intake's 40 payload paths equal the 40 changed content paths.
  - Ran `tools/validate.py` (0 errors), `word_title_screen.py` on the 30 words (191 stem-only lines, 0 whole-segment
    overlaps) and its own keyword screen of all RU word titles. It did not reopen dictionary pages.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN and the ten link-only navigation hunks (diffs only), and sampled nearby RU
    cards for term conventions.
  - Fetched Digital Daijisen on Weblio for 打ち合わせ, 青少年 and 電力; other cited entries were not reopened one by one.
    It did not screen whole-deck title collisions, and its report records no validator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time; the coordinator verified HEAD `e2b0bdb` and a clean tree before each
  launch. Each report records the snapshot `e2b0bdb` with an empty `git status --porcelain`. No fix was applied until all
  three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `228-words-batch-67-review-correctness-001.md`
  - `228-words-batch-67-review-consistency-001.md`
  - `228-words-batch-67-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch worktrees holding the author's working copy.

  The correctness report says that it read no batch records, author reports, other review reports or excluded scratch
  worktrees. The consistency report says that it did not read batch records, the ledger, progress files, other reviews or
  scratch worktrees; it checked the intake's path list against the diff, which its assignment included. The
  comprehensibility report records its read set, which contains none of the excluded material.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **CLEAN** for all 30 new cards; scoped coverage **NEEDS FIX** for 青少年, 鈍い and 打ち合わせ, **CLEAN**
for the other 27. Russian comprehensibility and quiz safety were not assessed.

- C1 (minor, scoped coverage; high confidence), `青少年.md:39–47`: the age-boundary warning survives, but both concrete
  source definitions that EN teaches disappear: about 12–25 in the general sense and under 18 in the youth-protection
  context. Without them the contrast that explains why a single age cutoff is unsafe is lost. Remedy: after line 43, «В
  общем значении цитируемый словарь указывает примерно 12–25 лет; в контексте постановлений об охране молодёжи — младше
  18 лет. Это определения источника, а не единая действующая юридическая граница». Evidence: frozen EN 青少年:39–44;
  JMdict 1381570 senses 1–2 on Jisho; Digital Daijisen 青少年, whose historical ordinance wording the reviewer warned
  against generalizing into current law.
- C2 (minor, scoped coverage; high confidence), `鈍い.md:58–59`: the main entry and the separate のろい entry survive, but
  EN's seven comparison-entry citations are dropped; the comparison prose remains, so this is lost traceability, not a
  wrong comparison. Remedy: append «Сопоставления: статьи 1174890, 1421970, 1010040, 1013050, 1008190, 1596750 и
  2121270». Evidence: frozen EN 鈍い:42; Jisho 鈍い confirms main entry 1582430 and its five senses. The reviewer did not
  re-audit the seven comparison entries.
- C3 (minor, scoped coverage; high confidence), `打ち合わせ.md:46–49`: EN excludes both the clothing-overlap sense and the
  archaic exact-matching sense from the taught meaning; RU keeps the clothing overlap but replaces the second boundary
  with generic «другие употребления», so the archaic sense and its status are no longer recoverable. Remedy: «Карточка
  учит значению „предварительное согласование“, а не отдельному значению „запа́х пол одежды“ или устаревшему „точное
  подгоняние одного к другому“». Evidence: frozen EN 打ち合わせ:43; JMdict 1588140 senses 1–3 (sense 3 Archaic) on Jisho;
  Digital Daijisen 打ち合わせ, which separates the clothing and matching uses.

What the reviewer confirmed:
- Main readings, Japanese examples and original metadata were retained; kana readings were added in places. No EN
  runtime link was dropped where the RU target exists, and the six RU-only links resolve. The two RU-added exclusions
  delete no EN guard; their quiz justification is outside its facets.
- しーん omits EN's `image` and `image_scene` because `images/しーん.webp` is absent in RU; this is not a text-coverage
  defect and does not authorize media adoption. Unavailable article, kanji and word targets correctly remain plain text.
- No defect was established in contextual «у меня»/«мой», a possible male speaker in Russian past-tense examples, plural
  readings of unmarked Japanese nouns, «впадает» in the river example, or the naturally shared translations of 広さ/面積
  and 乾電池/電池. «гробовая тишина» follows the source's own "as the grave"; «конгруэнтность (в геометрии)» and «нуль
  функции» match the cited usage; 電力's energy-supply example does not confuse watt-hours with power.

Optional: 零点:20 «К сожалению, я получил ноль баллов за тест» would make the unwelcome result of 取ってしまいました explicit;
outside its facets, «запа́х (наложение пол одежды)» would avoid the smell reading of «запахе полочек», and 広さ's title could
foreground «площадь; ширина» (Kuznetsov протяжённость includes width, so the existing word is not established as false).

Limits: bounded editorial review, not a fresh historical or etymological audit, native-speaker certification, corpus
search, full comparison-card audit, media or device review, or certification of every quiz pair; grammatical labels were
assessed as the cards' qualified teaching classifications; frozen EN is the translation baseline, not independently
re-proven in full.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **CLEAN**; scoped coverage (cross-file integration) **CLEAN**. No finding.
Correctness and comprehensibility were not assessed.

What the reviewer confirmed:
- `jlpt`, `type`, `kanji`, `tags`, `reading` and `word` equal EN on all 30 cards; `quiz_exclusions` equals EN on 28,
  and the only differences are the RU additions 採点→勘定 and 打ち合わせ→話し合う. インタビュー, 直流 and 乾電池 have no
  exclusion key, as in EN. しーん's omitted `image`/`image_scene` follows the established word-only adaptation (ざわざわ
  has no image field either).
- Links equal EN's per card, except absent RU targets left as plain text (the kanji cards 接, 鈍, 灯, 蛍, 波, 池, 柱, 採 and
  零; the word cards 体積, 接近 and 満点; the articles japanese-onomatopoeia and onomatopoeia-motion-and-sound) and the six
  RU-only links, each at a substantive contrast or comparison, which it accepted. No EN link was dropped where the RU
  target exists.
- Each of the ten navigation diffs is exactly one line, adding only link brackets and an href at the mention EN links,
  in EN's path form, with no prose change.
- Every non-stroke manifest entry matches the working tree; the 30 new cards are present; the intake's 40 payload paths
  equal the 40 content-diff paths.
- All 27 EN exclusion lists are retained card by card. One-way in-batch declarations suffice because the app applies
  them symmetrically. The unguarded in-batch pairs it examined (直流–交流, 電流–電力, スケジュール–合同, 採点–零点, 電波–電池,
  電池–電力, 組み合わせ–打ち合わせ and 組み合わせ–交流) are acceptable as in EN: none is a defensible correct answer for the
  other. It agreed that none of the pairs the author had declined to guard is required, and its own keyword screen found
  no further pair needing a guard.

Optional: O1, 広さ reads 二十平方 as にじゅっ while 面積 reads にじゅう; EN has the same split, and the reviewer did not
establish that にじゅっ is wrong. O2, outside its facets: 打ち合わせ's «например о запахе полочек одежды» uses a rare
tailoring term and drops EN's archaic matching sense, a wording matter for the comprehensibility reviewer. Limits: the
dictionary basis for the RU-added guards came from the reviewer's knowledge of the entries and the senses the cards cite,
without reopening dictionary pages, and necessity classes are judgements, not measured ambiguity; translation accuracy
was not assessed; the 118 `strokes/*.json` manifest entries could not be recomputed from working-tree bytes (see the
recheck record); it attributed the CR bytes it saw in the working tree to checkout line-ending conversion.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** for 打ち合わせ, 広さ, 面積, 直流, 交流, 電球, 合同 and 電力 (the other 22 new cards
CLEAN on this facet); scoped coverage **NEEDS FIX** for 青少年 and 打ち合わせ, **CLEAN** for the other 28. The changed lines of
the navigation hunks have no Russian-wording defect.

- F1 (moderate, also coverage; high confidence), `打ち合わせ.md:46–47`: «например о запахе полочек одежды» reads as the
  smell of clothing shelves, so a learner either cannot parse the exclusion or learns a false second sense. Remedy: «Здесь
  разбирается заранее согласованная встреча, а не нахлёст переда одежды (передние полочки, наложенные друг на друга) и не
  устаревшее «подходить друг другу».» Evidence: Digital Daijisen 打ち合わせ sense 2 (the overlapping front panels of a
  garment) and the matching sense; EN excludes clothing overlap and archaic matching, not a smell.
- F2 (minor; high confidence on the collision, medium on quiz impact), `広さ.md:4,16,19` and `面積.md:19`: both room
  examples read «Площадь этой комнаты — двадцать квадратных метров», using 面積's title word for 広さ, and the title's lead
  «протяжённость» ordinarily means length or duration, so it does not show the extent-versus-measured-area split. Remedy:
  title «величина пространства; ширина»; drop or gloss «протяжённость» on line 16; translate 広さ's room example «По
  величине эта комната — двадцать квадратных метров». Evidence: the identical lines; EN titles "spatial extent; width" and
  "measured area".
- F3 (minor; high confidence), `直流.md:15,32`, `交流.md:23` and `電球.md:23`: learner prose keeps unexplained Latin DC, AC
  and LED, although the Russian terms are present. Remedy: delete «(международное сокращение DC)» and both «(AC)», and
  explain LED電球 as a Japanese spelling. Evidence: the cited lines; 電流.md:33 uses only the Russian terms.
- F4 (minor; high confidence), `交流.md:25`: «Эта машина работает на переменном токе» for 機械 can be read as a car.
  Remedy: «Этот механизм работает на переменном токе.» Evidence: 直流.md:18 uses «устройство» for 装置.
- F5 (minor; high confidence on the mismatch, medium on impact), `合同.md:22`: «совместную презентацию» for 説明会 suggests
  a slide talk or a launch. Remedy: «Две компании совместно провели разъяснительную встречу.» Evidence: EN "joint
  information session".
- F6 (minor; high confidence), `電力.md:4,12,17,20`: the unqualified title gloss «электроэнергия» equates 電力 with the
  energy quantity that lines 17 and 39 separate from power. Remedy: title and H1 «электрическая мощность»; «о подаче
  электричества» on line 17. Evidence: Digital Daijisen 電力 (work per unit time, unit watt).
- F7 (minor, scoped coverage; high confidence), `青少年.md:42–44`: the card says there is no single age cutoff but drops the
  only qualified ranges. Remedy: after line 43, the general range of about 12 to 25 and, in youth-protection provisions,
  unmarried people under 18, as source definitions. Evidence: Digital Daijisen 青少年; EN teaches the same qualification.

Optional: 乾電池:18 and 電池:19 share «Я заменил батарейки в пульте»; the reviewer judged the titles and second examples
sufficient. The glosses «габариты», «муторный», «комбинация», «гробовая тишина», «тугодум (устар.)» and «конгруэнтность (в
геометрии)» are disambiguated in the bodies; «окуригана» and «годан» are established course terms; しーん's unlinked see-also
is not a defect. Limits: not a native-speaker or corpus-frequency certification; whole-deck title collisions and quiz
pairing were not screened; comparison cards were sampled, not read in full.

## Exclusion classification

All 140 EN exclusion entries (27 lists) are retained in EN order; インタビュー, 直流 and 乾電池 have none. Eighteen of them lie
inside the batch. At the candidate, two direct, one-sided entries were added on two new cards; neither is a new list or
targets a batch word.

| Entries | Author | Consistency reviewer |
|---|---|---|
| 採点→勘定 (1) | conservative | conservative |
| 打ち合わせ→話し合う (1) | conservative | conservative, close to required by parity with the EN guard on 相談 |

採点 «выставление оценок; подсчёт очков» shares «подсчёт» with 勘定 «подсчёт; счёт (к оплате)»; the reviewer found the
lexical basis real but necessity unestablished, because 採点 is primarily grading and 勘定's quiz senses are counting money
and bills. 打ち合わせ «предварительное обсуждение; согласование деталей» shares «обсуждение/обсуждать» with 話し合う «обсуждать
вместе», as 相談 «консультация; обсуждение», which EN already guards, does. Both entries are kept. The correctness reviewer
noted that they delete no EN guard without auditing quiz safety, and the comprehensibility reviewer did not score the
guards.

Reconciliation, the coordinator's dispositions, both fixes and the final verdicts are in
`228-words-batch-67-recheck-001.md`.
