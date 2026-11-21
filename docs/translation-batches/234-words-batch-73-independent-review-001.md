# Batch 234 — independent review 001

## Snapshot and scope

- Reviewed commit: `1e7c04d20795a3f0efac996855d00f233ebe566b` (tree `02023ebe35e7f52010e453f8711aa47bf99c56ae`), branch
  `full-ru-234-words-73`, parent `931612d`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 233 candidate `5218a9afd4d733f79b5d88fc1f826c760dd93a8c`.
    Before copying, the coordinator's candidate script checked two things: that the five navigation files edited there
    (`kanji/埋.md`, `words/パーティー.md`, `words/追う.md`, `words/隙間.md` and `words/面接.md`) were unchanged between
    `5218a9a` and the candidate's parent `931612d`, and that none of the 30 new cards existed in the primary checkout. It
    also checked that the branch, HEAD and `origin/main` were the expected ones and that the tree was clean.
  - The script byte-compared the 35 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 35 batch paths plus `manifest.json`. Its byte scan of all
    35 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 35 committed
    blobs at `1e7c04d` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from Batch 233; all six restored links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made no content edits: no title edit, no exclusion
    append and no held link; the 35 lane files were copied unchanged. Its adjudication record states:
    - "Titles compared with EN one by one; no coordinator title edit. Phrase-like titles (お先に, 応対, 催促 with its verbal
      second gloss, 近々's distance sense) follow EN's two senses and are left for the blind comprehensibility review
      rather than pre-empted.";
    - "RU-added exclusions accepted as reported: 19 pairs on 12 cards; 退ける→しまう and 退ける→収める required (identical
      segment «убирать»), the other 17 conservative and harmless. 船便→速達 targets a B233 card whose title may change in
      the B233 fix round; the candidate screen is rerun on the published B233 tree before the B234 commit.";
    - "Screens rerun by the coordinator with RU_ROOT = lane: `word_title_screen.py` over the 30 words reports 0
      unguarded exact segments (output `b234-lane-screen.txt`); `link_parity.py` over the 35 paths reports only the
      intended RU-only link 追い掛ける:40 → 追い付く (substantive comparison with an existing RU card); `navonly.py HEAD
      --only` over kanji/埋, words/パーティー, 追う, 隙間 and 面接 reports 5 files, 6 links added, 0 problems; `validate.py`
      0 errors.";
    - "The 埋 kanji gloss «закапывать; заполнять пробел» stays unchanged (navigation-only restoration; outside the batch
      scope).";
    - "Unverified Russian words to hand to the reviewers: «застолье», «посторониться», «пускаться в погоню»,
      «земледельческая деревня», «средства сообщения».";
    - "Lane check after the B233 fix: none of the 35 changed lane paths links to or quotes a B233 card changed by fix
      1d78dd8 (成立, 送料, 出勤, 通り掛かる, すれ違う, 効力, 清い, 逆さ, さわやか, 通路, 透き通る, 澄む) or their old wording
      («принятие (закона)», «вверх ногами; наоборот», «проход для людей», «Защита теста»); no lane path is a B233 path.
      B234 titles are screened against the fixed B233 titles at candidate time.";
    - "Candidate screen on the published B233 tree (main 1e14f14; b234-cand-screen.txt): 0 unguarded exact segments; the
      3 exact shared segments are guarded (送別–見送り «проводы», 退ける–しまう and 退ける–収める «убирать»). Against the
      fixed B233 titles, only stem hits remain: お先に «проходите первым…» and 退ける «убирать (с прохода, с места)» share
      «прохо» with the noun 通路 «проход…; проход или проезд» (a polite phrase and a verb whose qualifier names the place;
      different part of speech and sense; no guard), and 船便~速達 «отпра» is already guarded. No change from the lane
      adjudication."

    The committed manifest records 5,139 entries (5,134 `files`, 3 images and 2 scenes); the correctness and consistency
    reviewers' `tools/validate.py` runs on the candidate reported 0 errors.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 5 files with 6 restored navigation links (the kanji card 埋 and the word cards パーティー, 追う, 隙間 and 面接);
    - `manifest.json` (`contentVersion` `b06ec272fee34a3d`, 5,139 entries);
    - the intake, whose note reads "B234 30-card adaptation with six navigation-only link restorations in five existing
      files; candidate before blind review."
- Published baseline recorded in the intake: `1e14f14552d91362cbd0bcb4e9e2bb562fffeb7b` (Batch 233 merge). Parent
  `931612d` adds only the Batch 233 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests (the authoring worktree run reported 124 tests);
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 5 files (6 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen: no unguarded exact title-segment overlap (54 `OK` lines for pairs already guarded by an exclusion and
    408 stem-only `!!` lines);
  - link parity: no EN link lost where the RU target exists; the only RU-only link is 追い掛ける:40 → 追い付く; for this
    record, no pre-existing RU-only link sits in a batch path.
- Common sample: all three reviewers read all 30 new word cards in full, and the five navigation-file diffs. The
  correctness and comprehensibility reviewers read each card against its complete frozen EN original. The consistency
  reviewer also checked front matter, links and exclusions against EN, and the intake and manifest hashes.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (listed file by file), the runtime link additions in kanji/埋 and the
    word cards パーティー, 追う, 隙間 and 面接, relevant existing RU comparison cards, stable front matter, retained
    citations, Japanese example and reading text, and available-target link parity.
  - Inspected the actual JMdict XML entries for all 30 primary IDs and all additional IDs cited by these cards, including
    search-only, rare, irregular and obsolete flags and reading-local restrictions (distribution `JMdict_e.gz`, retrieved
    XML SHA-256 `a2049d4702b3bacb806f129281992a9bec604ac71f8f7492e313f6538ea699cf`; a live distribution, not the
    author's historical snapshot).
  - Japanese sources beyond JMdict: Kotobank 送り仮名, 応対 and 応接; Digital Daijisen on Weblio for the consequential
    lexical contrasts (cited: 近々, 補う and 補償); Jisho kanji-reading sections.
  - Russian sources: Russian lexical entries and usage, and the Russian statutory definition of «пестициды» (growth
    regulators fall within it); scoped meaning checks, not frequency claims.
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 RU cards and all five navigation diffs in full. Read the frozen EN originals of お先に, さようなら and
    送別 and the start of 送り仮名 in full and compared the rest programmatically (front matter, `quiz_exclusions`, link
    targets and occurrence counts, footers).
  - Checked the intake's 35 payload paths against the content diff, re-hashed the manifest (all 5,134 file hashes match,
    CRLF-normalised) and checked that the manifest diff changes only `contentVersion`, the 埋 hash and the new entries;
    ran `tools/validate.py` (0 errors).
  - Took dictionary bases from the JMdict and Daijisen entries cited in the cards; it performed no web or dictionary
    lookups.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN; inspected the link-only diffs of kanji/埋 and the word cards パーティー, 追う,
    隙間 and 面接 as diffs, not as full articles.
  - Re-fetched the dictionary senses it cites: Digital Daijisen on Weblio (農薬, 催促, 接する and 交通機関), JMdict
    1578110 via japandict, Kotobank 近近 and 実用日本語表現辞典 on Weblio (近々). It reports that `link_parity` found no lost
    EN link whose RU target exists and used title overlap as a lead only; it records no validator or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. Each report records
  the snapshot `1e7c04d` with a clean tree. No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No reviewer reported running a generator: the correctness report says no repository edits,
  generators, commits, pushes or issues and that final status and staged/unstaged diff checks confirmed the repository
  and index unchanged; the consistency report says author reports, batch records and drafts were not read and ran only
  `tools/validate.py` and a manifest re-hash; the comprehensibility report records no validator or generator run, and its
  recheck says no generator was run. No tracked repository file was changed.
- Full blind reports:
  - `234-words-batch-73-review-correctness-001.md`
  - `234-words-batch-73-review-consistency-001.md`
  - `234-words-batch-73-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch worktrees.

  The consistency brief made the intake record's path list the single exception, for its path check. The correctness
  report says that prohibited author and reviewer materials were not consulted. The consistency report says that author
  reports, batch records and drafts were not read. The comprehensibility report says that author reports,
  translation-batches, drafts and tracking were not read.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for 近々 and 補う, **CLEAN** for the other 28 new cards; scoped coverage **NEEDS FIX**
for 補う only, **CLEAN** for 近々 (the broader temporal sense remains in its body) and the other 28. Comprehensibility and
quiz safety were not separately assigned or certified.

- F1 (minor, correctness; high confidence), `近々.md:4,12,19`: the title and the first translation say «в ближайшие дни»,
  whereas EN says "in the near future"; this introduces a days-based horizon absent from the Japanese sentence and turns
  a context-dependent possibility into the general displayed gloss. Line 16 correctly retains «скоро, в ближайшее время»,
  limiting the defect; the spatial sense and its reading restriction are also retained. Remedy: «в ближайшее время (о
  предстоящем)» at lines 4 and 12 and «В ближайшее время я собираюсь переехать.» at line 19, preserving the spatial gloss.
  Evidence: JMdict 1578110 sense 1 "soon; before long; shortly; in the near future", without a days restriction; Digital
  Daijisen ちかぢか sense 1 ごく近いうちに, and its きんきん entry 近い将来 / 近いうちに.
- F2 (minor, correctness/scoped coverage; high confidence about the lost qualification, moderate about a categorical
  reading), `補う.md:42–43`: EN qualifies the contrast, "does not automatically mean paying legal damages"; RU «補う не
  означает выплату возмещения по закону» drops "automatically" and can read as excluding the legal-payment interpretation.
  Remedy: «補う само по себе не указывает на юридическое возмещение ущерба; для этого значения полезно сравнить
  補償する（ほしょうする）.» Evidence: JMdict 1514460 sense 1 ("compensate for", "cover (a shortage, loss, etc.)") and
  1514650 ("compensation; reparation"); Digital Daijisen 補う sense 2 and 補償 sense 1.

What the reviewer confirmed:
- The other 28 cards are CLEAN within this scope; no other actionable omission of an EN sense, teaching note, example,
  citation or available-target link was established.
- Original exclusions and external citations are retained; stable metadata differences are additive quiz exclusions.
- Russian-only expansions were checked against their Japanese senses and Russian usage: agricultural produce includes
  livestock products in Daijisen, and growth regulators fall within «пестициды» in the inspected Russian statutory
  definition. No unsupported consequential Russian-only claim remained established beyond the two findings.

Optional: none within the assigned facets. Limits: bounded review, not exhaustive linguistic certification or
native-speaker approval; the JMdict XML is a live distribution, not a reproduction of the author's historical snapshot;
Gramota and some Jisho requests failed, and incomplete aggregator snippets were not treated as verified dictionary
articles.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **CLEAN** (no required guard is missing and none is unjustified; several
RU-added guards are conservative); scoped coverage of navigation and link integration **CLEAN**. Findings: none that
require a fix. Comprehensibility was not assigned to this review.

What the reviewer confirmed:
- `tools/validate.py` 0 errors; all 5,134 manifest file hashes match (CRLF-normalised SHA-256), and no content file is
  missing from the manifest; the manifest diff changes only `contentVersion`, the 埋 hash and the new entries.
- The intake's 35 payload paths equal the content diff exactly and add no learner content; the held list is empty.
- Front matter is identical to EN for all 30 cards, except that 近付ける carries RU-only `quiz_exclusions`; every EN
  `quiz_exclusions` list is kept as a prefix of the RU list, in the same order; 送り仮名, 迷信 and 述語 have no key in EN or
  RU.
- Links have parity with EN by target and by occurrence count. The only dropped EN links point to targets with no RU file
  (仮名, ずらす, 主語 and kanji 補, 述, 接, 農, 村, 輸) and remain plain text; no broken link. The one RU-only link,
  追い掛ける's «догнать» to 追い付く, is a substantive contrast and the target exists.
- The navigation files change only link brackets and hrefs, at EN positions: kanji/埋 wraps 埋める at lines 29 and 38 (the
  うずめる row and the prose stay plain, as in EN); パーティー→宴会, 追う→追い掛ける, 隙間→埋める and 面接→接近.
- EN links from existing RU cards to the new words are all restored; the remaining non-links point to words with no RU
  file. The footers of 応接, 応対 and 交通機関 mirror EN's shape and source names.
- Title screen: only three exact shared segments exist, and all three are guarded (送別–見送り «проводы», 退ける–しまう,
  退ける–収める); the «прохо» stem hit between 通路 and お先に/退ける is unrelated in meaning. The declined pairs 催促–返事,
  迫る–返事 and 接する–境界 and the in-batch unguarded pairs (お先に–送別, 追い越す–追い掛ける, 埋める–追加, 応対–宴会,
  接する–近寄る/迫る/近付ける, 催促–応対, 近々–接近, the 農薬/農産物/農村 pairs and 船便–交通機関) are separated by title.

Optional (nonblocking; necessity UNVERIFIED): ずれる «смещаться; не совпадать (по времени, сути)» vs 相違 «расхождение;
несовпадение» and 逸れる; 応対 vs 答える «отвечать» and 応じる «откликаться; соглашаться (на просьбу)»; 近付ける vs
くっつける «приклеивать; придвигать вплотную» (optional remedy: append `ずれる`: [相違, 逸れる]; `応対`: [答える, 応じる];
`近付ける`: [くっつける]); 休み is a plain example in 送り仮名, as in EN, although an RU card exists. Limits: no web or
dictionary lookups, so the necessity of the conservative guards is UNVERIFIED; EN originals were fully read for only
three cards and compared programmatically for the rest; Japanese accuracy, translation quality and comprehensibility
were not covered; no device or app test.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (eight minor items in 退く, さようなら, 船便, 農薬, 催促, 接する, 近々 and 交通機関);
**CLEAN** for the other 22 cards; scoped coverage **NEEDS FIX** for 農薬 and 近々, **CLEAN** for the other 28.

- C1 (minor; high confidence), `退く.md:21`: the second example has no kana reading line, unlike the example above it
  and the EN original. Remedy: `- すみません、そこをどいていただけますか。（すみません、そこをどいていただけますか。）— Извините,
  не могли бы вы отойти оттуда?`
- C2 (minor; high confidence), `さようなら.md:29` and `船便.md:26`: learner prose uses the Latin tag `wago`, and 船便 also
  explains an authoring-format gap («отдельной категории для смешанных чтений в формате нет»). Remedy: rewrite both
  sentences without the tag or the format remark.
- C3 (minor; high confidence that the translations are narrower), `農薬.md:20-21`: both worked translations say only
  «пестицид». Remedy: «— Я выращиваю овощи без сельскохозяйственных химических средств.» and «— Используйте это
  химическое средство для растений строго в установленном количестве.» Evidence: EN "without using agricultural
  chemicals" and "use this agrochemical"; Digital Daijisen 農薬 農業用の薬剤, including 生長促進剤・発芽抑制剤. Severity
  minor, because lines 16–17 already state the wider scope.
- C4 (minor; high confidence), `農薬.md:42`: «В названии карточки к «пестицидам» добавлены регуляторы роста…» talks about
  the card title, not about Japanese. Remedy: delete the sentence. The reviewer said the sentence is not in the EN
  article.
- C5 (minor; high confidence for the part-of-speech mismatch), `催促.md:4,12`: the noun's quiz title ends in the verb
  infinitive «торопить», which collides with 急ぐ «спешить; торопиться». Remedy: title and H1 «напоминание (об ответе,
  оплате); побуждение поторопиться (с ответом)», and an added body sentence linking [急ぐ](急ぐ.md). Evidence: Digital
  Daijisen 催促 ［名］(スル); EN "pressing for action; urging".
- C6 (minor; high confidence about the dictionary sense), `接する.md:4,16`: «вести себя (с людьми)» is ordinary Russian for
  how one behaves, not for dealing with someone; the worked example already says «обходится». Remedy: title and H1
  «соприкасаться; граничить (с чем-либо); обходиться (с людьми)», and line 16 ending «или «обходиться с людьми, иметь с
  ними дело».» Evidence: Digital Daijisen 接する sense 3 応対する.
- C7 (minor; high confidence), `近々.md:4,12,19`: «в ближайшие дни» is narrower than the card's own «скоро, в ближайшее
  время» and EN "in the near future". Remedy: title and H1 «скоро (в ближайшее время); совсем близко (о расстоянии)», the
  example «— В ближайшее время я собираюсь переехать.» and an added remark that there is no fixed span of a few days.
  Evidence: JMdict 1578110 via japandict; Digital Daijisen ごく近いうちに (Kotobank 近近); 実用日本語表現辞典 数日から数週間.
- C8 (minor; medium-high confidence), `交通機関.md:4,12`: «средства сообщения» is not a clear modern equivalent of trains
  and buses and can look like a second, equal sense. Remedy: title and H1 «транспорт (поезда, автобусы и т. п.);
  транспортная система», with no new body sentence. Evidence: EN "means of transport; transport system"; Digital Daijisen
  交通機関 多く、運輸施設をいう.

Optional: お先に's speech-act title; さようなら «прощайте»; 送別 «прощальный» and 宴会 «застолье» (qualified in their
bodies); 農村 «земледельческая деревня» (bookish but clear); 応対's long title; 述語's commentary inside translations;
追い掛ける «пускаться в погоню» (more inchoative; «гнаться» would match the examples better); 近寄る «этой машине» and «Ко мне
подошла кошка»; 補う «окуригана»; the unlinked absent targets. None was scored. Limits: not a correctness or quiz-safety
review; exclusion lists were not audited; not every cited dictionary page was re-fetched; title overlap was only a lead;
model identity not verifiable.

## Exclusion classification

All 140 EN exclusion entries (26 lists) are retained in EN order; 送り仮名, 迷信, 述語 and 近付ける have none in EN.
Nineteen of them lie inside the batch. At the candidate, nineteen direct, one-sided entries were added on twelve new
cards: eighteen appended to eleven existing lists and one new list on 近付ける (four entries); none targets a batch word
other than 近付ける's 近寄る and 接近.

| Entries | Consistency reviewer |
|---|---|
| 退ける→しまう, 退ける→収める (2) | Required: identical segment «убирать» |
| 農産物→製品 (1) | Required or near-required: shared «продукция» |
| 迫る→収める, 近付ける→近寄る, 接近, 寄る, 近い, 船便→郵送, 船便→速達, 交通機関→車, 農村→地域 (9) | Conservative: real sense overlap, titles separate them (交通機関→車: 車 «автомобиль; транспортное средство» is the closest competitor) |
| お先に→譲る, 送別→送る, 追い掛ける→走る, 応対→付き合い, 返事, 答, 催促→急ぐ (7) | Conservative and weakest: plausible semantic basis, necessity unestablished; none unjustified |

The author classed 退ける→しまう and 退ける→収める as required for the identical segment «убирать» and the other seventeen as
conservative; the coordinator accepted all nineteen as reported. The reviewer's classes differ in one place: it classed
農産物→製品 as required or near-required, where the author had it as conservative. The reviewer found no entry unjustified
and no EN guard dropped; all nineteen entries are kept. The correctness reviewer noted that stable metadata differences
are additive quiz exclusions, and the comprehensibility reviewer did not audit the exclusion lists.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`234-words-batch-73-recheck-001.md`.
