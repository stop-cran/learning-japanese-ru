# Batch 220 — independent review 001

## Snapshot and scope

- Reviewed commit: `19bcfe00f202ae1368ffc4422b38d9b1da172c2e` (tree `6c90c32e275e1f0b28692443c41fdd228aad6c76`), branch
  `full-ru-220-words-59`, parent `ff8310d`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 219 candidate `f72537721d86b0d72485aecb4a758b10ef241a20`.
    Before copying, the coordinator checked two things: that the 17 navigation files edited there were unchanged between
    `f725377` and the candidate's parent `ff8310d`, and that none of the 30 new cards existed there. The Batch 219 fixes
    touched only 主義, 今にも, 人込み, 予測, 主婦, 世間 and 代表; of these only 世間 is in this batch's path set, and it was
    not copied from the scratch worktree (see the held link below).
  - The coordinator byte-compared the 47 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 48 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - One held wrap was carried into this batch: Batch 219's 世間 had left its EN link to 世の中 as plain text because 世の中
    is a Batch 220 word. The coordinator wrapped that mention at EN's position (世間 line 29) in the primary checkout, on
    top of the published, fixed 世間 card; it is the only change to that card.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 18 files with 19 restored navigation links (including the held 世間→世の中 link);
    - `manifest.json` (`contentVersion` `38324799df00beb4`, 4,719 entries);
    - the intake.
- Published baseline recorded in the intake: `cf78e9c5fd2ea264b4940b4dbb2f4b216b6e0fbd` (Batch 219 merge). Parent
  `ff8310d` adds only the Batch 219 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK;
  - content budget: OK, 4,736 entries;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 18 files and 19 links, with no problem;
  - title screen: no unguarded exact title-segment overlap;
  - link parity: eleven RU-only links (不足→欠ける, 不安→緊張, 下り→下りる, 上京→東京, 一致→合う, 一生→命, 一体→全体,
    一人一人→個人, ヨーロッパ→欧州, メンバー→委員 and メモ→手紙). EN mentions 東京 (in 上京) and 欧州 (in ヨーロッパ)
    without a link; the other nine targets are introduced by a comparison sentence added in RU.
- Common sample: all three reviewers read all 30 new word cards in full.
  - Correctness and comprehensibility read each card against its full EN original.
  - Consistency compared each card's front matter, H2 count, link set and exclusions with EN by script; it did not
    re-read the EN bodies line by line.
- Correctness review scope:
  - Read in full the existing RU 欠ける, 緊張, 下りる, 東京, 合う, 命, 全体, 個人, 欧州, 委員 and 手紙 (the eleven RU-only
    link targets) and 世間 (the held-link card); inspected the complete navigation diffs in
    `articles/numbers-and-counters.md`, `kanji/不.md` and the 16 existing word cards; read the three binding RU
    instruction and format documents.
  - Read the JMdict-backed Jisho API records for all 30 headwords and the eleven RU-only link targets (three lookups
    initially rate-limited, 不正, 下り and 一瞬, were retrieved successfully later); Digital Daijisen for 一人一人, 合う
    (sense 4, 答えが合う), 委員 and 一層; Takoboto entries 1147220 and 2862534 for the two ロケット words (the Japanese
    explanation automatically attached to the locket entry concerns a rocket and was not used as evidence).
  - Russian sources: Kuznetsov entries on Gramota (стеснённый and стеснённость, рядовой, всеобщий, единодушие, семейство,
    медальон, пометка/помета, злоупотребление, мир, ограниченный, столица, совпадение, целый and более) and Russian
    Wiktionary (общество, неприемлемый, спуск, участник); japandict for 一層. Some ancillary lookups returned HTTP 429 or
    403; only successfully inspected entries are claimed.
  - Ran no generator or validator.
- Consistency review scope:
  - Read all 30 cards and all 18 navigation diffs in full (19 link occurrences), and compared link counts and path forms
    with EN.
  - Re-hashed every manifest file entry (the report says 4714 entries: it counted the `files` map, without the three
    image and two scene entries): Markdown matches on the raw bytes, and the CRLF `strokes/*.json` files match after LF
    normalisation, which it identified as the repository convention; it raised no issue.
  - Checked the intake only for its path list, candidate SHA-256 values and the absence of learner content, as its
    prompt permitted.
  - Read the RU content-structure instructions for the quiz and link rules; ran `tools/validate.py` (0 errors) and ran
    `word_title_screen.py` itself.
  - Classified the RU-added exclusions from the RU titles and from JMdict senses that it cited from memory; it re-fetched
    no dictionary and used those senses as the basis of the classification, not of a verdict.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN, and read RU 世間 and 欧州 in full for the restored link and the Europe pair;
    sampled the titles of the other comparison cards without reading each in full.
  - Read JMdict entries through Jisho pages and dictionary entries from Ozhegov and Kuznetsov on gufo.me and from
    Russian Wiktionary. It did not report running the content validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; each report says its model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time. Each report records the snapshot `19bcfe0` with an empty
  `git status --porcelain`. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `220-words-batch-59-review-correctness-001.md`
  - `220-words-batch-59-review-consistency-001.md`
  - `220-words-batch-59-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`, except
    that the consistency reviewer checked only the intake's path list and hashes;
  - the scratch worktrees;
  - one another's reports.

  The correctness report confirms that it read no author or reviewer report, intake or batch record, translation draft
  or tracking file, or scratch worktree; the consistency report confirms that it read no author report, title-screen
  output or batch record. The comprehensibility report does not restate the rules.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** (C1, minor; the other 29 cards are clean in this facet). Scoped coverage **CLEAN**
for all 30 cards and the inspected navigation changes.

- C1 (minor; high confidence), `一人一人.md:30`: the RU-only comparison with 個人 said that 一人一人 «перебирает всех
  членов группы по очереди». The unqualified «по очереди» makes sequential order part of the word's meaning and
  contradicts the card's own line 34 (一人一人の意見 does not specify a speaking order), so a learner can wrongly infer
  that the phrase excludes simultaneous or unordered individual contributions. Remedy: end the clause «一人一人 же
  выделяет каждого члена группы в отдельности, не обязательно задавая порядок». Evidence: Digital Daijisen 一人一人
  sense 1 「多くの中のそれぞれの人。めいめい。各人」 (example 一人一人の自覚が大切だ, awareness, not a sequence); JMdict
  sense 1 "each (person); individually" alongside contextual "one by one; in turn"; EN line 32 says no particular
  speaking order is required.

What the reviewer confirmed:
- All source metadata other than the localised titles and expanded exclusion lists match EN, and every EN exclusion is
  retained. No new link is broken, no EN link to an existing RU target was dropped, missing targets stay plain text, and
  the restored 世間→世の中 comparison remains consistent.
- All 60 main Japanese examples and their readings were compared directly; the only removed Japanese occurrence belongs
  to 一般's English-only "liberal" note, which is dispensable. English-only contrast and source-list remarks were
  appropriately omitted.
- The eleven RU-added comparisons have direct dictionary support (shortage, tension, descent, Tokyo, lifespan, whole,
  individual, Europe and addressed written communication); 答えが合う is attested (Daijisen 合う 4), and 委員's elected or
  appointed duties are supported (Daijisen 委員). They do not claim mutually exclusive semantic compartments.
- The two ロケット entries (rocket, locket) are separate lexical items, and Kuznetsov «медальон» 1 supports the locket
  sense.
- The Russian glosses стеснённость, рядовой, всеобщий, единодушие, семейство, пометка and the localised choices for
  мир, ограниченный, столица, совпадение and целый are supported in the cited senses. «Злоупотребление» is narrower than
  all of 不正, but the other title glosses and the body keep the broader dishonesty and technical incorrectness.

Optional: for the degree adverb in `一層.md:4,12,16`, «ещё больше; ещё сильнее» is clearer than «ещё сильнее; тем
более». This is a nonblocking refinement, not a claim that «тем более» can never render a contextual "all the more".
Evidence: Digital Daijisen 一層 (程度がいちだんと進むさま); japandict «[ещё] больше; [ещё] более»; Kuznetsov lists «тем
более» under «более» as an emphatic particle, «=Особенно».

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; scoped coverage (cross-file integration) **CLEAN**; quiz safety **NEEDS FIX** (F1 and
F2, both minor).

- F1 (minor; medium confidence), `ワイン.md:7-8` (front matter, no `quiz_exclusions`): ワイン «вино» is a kind of 酒
  «алкогольный напиток; сакэ», so in a ワイン question that option is a defensible correct answer. The RU
  content-structure rule requires a direct pair for a generic label inside a title (as with 車/電車), and the repository
  already guards the same hypernym relation (酒 excludes アルコール, お酒 and 飲み物; テニス excludes スポーツ). The card
  itself links 酒 and calls it broader. Remedy: add `quiz_exclusions: [酒]` and regenerate the manifest. Evidence:
  JMdict ワイン "wine" and 酒 "alcohol; sake"; the RU 酒 title begins «алкогольный напиток». EN has no guard; the pair is
  driven by the RU titles.
- F2 (minor; low to medium confidence), `ラケット.md:7-8` (no `quiz_exclusions`): 道具 «инструмент; приспособление;
  средство» is a generic label that fits a racket as sports equipment, so «приспособление» is arguably a correct answer.
  The card links 道具 and calls it «более широкая категория». Remedy: add `quiz_exclusions: [道具]`, or, if hypernym
  pairs without a title clash are not accepted, record it as a conservative optional pair without blocking. Evidence:
  JMdict 道具 "tool; implement; equipment"; no existing guard on ラケット.

What the reviewer confirmed:
- Front matter (`word`, `reading`, `jlpt`, `type`, `kanji`, `tags`) and H2 counts match EN for all 30 cards, all EN
  exclusions are retained, and the retained 世の中→世間 guard resolves against the revised 世間 card.
- The 18 navigation files differ from the parent only by the restored link brackets; all 19 occurrences match EN's
  positions and path forms. The 48 payload paths equal the content diff, and no unrelated or generated file is
  committed.
- Every EN link in the 30 cards is restored to an existing RU target, except those to absent files: the kanji 層 and 般,
  ウイスキー and ビール.
- All eleven RU-only link targets exist. Nine are introduced by an added comparison sentence and 上京→東京 and
  ヨーロッパ→欧州 by a substantive mention of a target EN names without a link; each addition is covered by a guard.
- The title-collision screen found no unguarded exact title or segment duplicate; ロケット «ракета» and ラケット «ракетка»
  are distinct.

Optional: the over-guards メンバー→参加 and 一言→要するに could be dropped (harmless; dropping them is not required);
一瞬 against ちょっと «ненадолго» is an EN-linked pair with weak overlap, not claimed as a defect. Limit: `kanji/杯.md`
links `[不](不.md)` although EN does not; the link was already present at `ff8310d` and is outside this batch.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (一般, 不正, 一層, 上京, ロケット and メモ; the other 24 cards are clean in this
facet); scoped coverage **CLEAN**.

- C1 (moderate; high confidence), `一般.md:4,9,15` as cited (the library example is at line 18): the title «рядовой;
  всеобщий» and the example gloss «посторонние посетители» do not teach the card's own sense. As a bare answer «рядовой»
  reads as the military rank or a rank-and-file person (Ozhegov), the body never uses it, and «всеобщий» is stronger than
  the card's note that 一般に does not make every case identical; «посторонние» suggests outsiders who do not belong.
  Remedy: title and H1 «общий; обычный»; example «Этой библиотекой могут пользоваться и обычные посетители.»; the 普通
  exclusion already covers the shared «обычный». Evidence: JMdict 1165790 senses 1–2 ("general; universal"; "ordinary;
  average; common"); Ozhegov «рядовой».
- C2 (minor; high confidence), `不正.md:4,8` as cited (the H1 is at line 11): the unqualified second gloss
  «злоупотребление» also covers misuse of a substance (Kuznetsov), while JMdict 1493370 is injustice, wrongdoing,
  impropriety, irregularity, dishonesty and fraud; the body never uses the word. Remedy: title and H1 «нечестность;
  неправильность».
- C3 (minor; high confidence), `一層.md:4,9,13` as cited (title, H1 and opening at lines 4, 12 and 16): «тем более» is
  the particle "especially; let alone", not the degree adverb the examples show («ещё холоднее», «ещё больше»); no example
  uses it. Remedy: title and H1 «ещё сильнее; ещё больше»; opening «наречие со значением «ещё сильнее» или «ещё больше»».
  Evidence: JMdict 1164340 sense 1 "even more; still more; all the more"; Russian Wiktionary «тем более».
- C4 (minor; high confidence), `上京.md:15,17` as cited (the example is at line 20): «Я переехал в Токио…» states a change
  of residence, although the card says 上京 need not be a permanent move and JMdict gives "going to the capital (Tokyo)".
  Remedy: «Я поехал в Токио, чтобы поступить в университет.» Evidence: JMdict 1352980 sense 1; the card's own text.
- C5 (minor; high confidence), `ロケット.md:22` as cited (the sentence is at line 24): «Английские rocket и locket…» works
  only through English words a learner may not know. Remedy: «Оба слова пишутся одинаково катаканой, с маленьким ッ
  перед ト. Это разные заимствования, а не два значения одного слова; кандзи, по которым можно восстановить различие,
  нет.» Evidence: the methodology rule to drop comparisons that work only through English; JMdict 1147220 and 2862534
  are separate entries.
- C6 (minor; high confidence), `メモ.md:4,9,24` as cited (the kanji-section sentence is at line 25): the title leads with
  «пометка» (Ozhegov: an inscription or mark, for example in a margin) and the verb phrase «записать для памяти», while
  the body and `要点.md` call the noun «записка»; the verb phrase is not a short answer gloss, and line 24 equates the word
  with English «memo». Remedy: title and H1 «записка; заметка», and a line 24 without the English equation («Это
  катаканное заимствование…»). Evidence: Ozhegov «пометка»; JMdict 1133830 sense 1; the RU rule that a title is a short
  quiz sense and that English must not be required.

Optional: 不自由 «стеснённость» is bookish but bounded by the first paragraph and the money example; 一家 «семейство»
(Ozhegov 1, «то же, что семья») is carried by the lead «вся семья»; ヨーロッパ's italic *Europa* is unnecessary Latin
script; no ラケット/ロケット cross-note is needed (EN omits it, and the titles differ); ラケット's «Дайте» for 貸してください
loses "lend". Limits: Jisho pages rather than the raw JMdict data; no dictionary proof of a strict everyday/formal split
between ヨーロッパ and 欧州 beyond `欧州.md`, which the new card does not contradict; 世間 and 世の中 do not contradict
each other.

## Exclusion classification

All 26 EN exclusion entries (15 lists) are retained. At the candidate, 24 direct, one-sided entries were added on 16 new
cards:

| Entries | Author | Consistency reviewer |
|---|---|---|
| 上京→東京, 一致→偶然, ヨーロッパ→欧州 | required | required |
| 不足→欠ける, 不可→禁止, 下り→下りる, 下り→方向, 一致→合う, 一体→全体, メモ→手紙 | conservative | required (下り→下りる borderline) |
| 不安→緊張, 不安→はらはら, 一生→命, 一人一人→個人 | conservative | conservative to required |
| 不自由→制限, 下り→降りる, 下り→坂, 一言→要するに, 一方→方, 一度に→同時, メンバー→委員, メモ→記録, メモ→栞 | conservative | conservative (一言→要するに "conservative at best, arguably over-guarding") |
| メンバー→参加 | conservative | unjustified, mild over-guarding (harmless) |

The author and reviewer differ in how much necessity they established; the records adopt the reviewer's classification,
counting its "conservative to required" entries as conservative. Only メンバー→参加 was called unjustified, and the reviewer
did not require its removal. The correctness reviewer identified the added exclusions without auditing quiz safety, and
the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`220-words-batch-59-recheck-001.md`.
