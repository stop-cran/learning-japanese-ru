# Batch 226 — independent review 001

## Snapshot and scope

- Reviewed commit: `bebdf808fd419165e2b6098bd25d815f7c41c235` (tree `acea83488c876c2f725c512d68e7db0c9584fba9`), branch
  `full-ru-226-words-65`, parent `b61f341`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 225 candidate `56996a024ba2641a8d5e846d8c63e1981beeccff`.
    Before copying, the coordinator checked two things: that the 5 navigation files edited there were unchanged between
    `56996a0` and the candidate's parent `b61f341`, and that none of the 30 new cards existed in the primary checkout. The
    Batch 225 fix touched only ぐっすり, いつまでも, お目に掛かる, おめでとう, いわゆる, ごめんなさい and 鳴らす; none of them is
    in this batch's path set.
  - The coordinator byte-compared the 35 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 35 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - No wraps were held from Batch 225, and the coordinator applied none separately; all eight navigation links were
    copied from the authoring worktree.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 5 files with 8 restored navigation links (three kanji cards and two word cards);
    - `manifest.json` (`contentVersion` `016ea287bd61d6c7`, 4,899 entries);
    - the intake.
- Published baseline recorded in the intake: `2df70e04d517e89422bfdfef07334cf85fb3005f` (Batch 225 merge). Parent
  `b61f341` adds only the Batch 225 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK (124 tests);
  - content budget: OK;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 5 files and 8 links, with no problem;
  - title screen: no unguarded exact title-segment overlap (136 stem-only `!!` lines and 24 `OK` lines);
  - link parity: no EN link lost where the RU target exists, and one new RU-only link, 強化→固まる, in the Russian
    restatement of EN's English-dependent "solidify" remark, which compares 固まる/固める with 強化.
- Common sample: all three reviewers read all 30 new word cards in full against their full EN originals, and the five
  navigation diffs.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN, attesting each file, the five navigation diffs, and in full the
    existing RU うるさい, 驚く, 慣れる and 塩.
  - Inspected the Jisho/JMdict entries, senses and ids of all 30 headwords and of 39 further numbered comparison
    citations; read public JMdict XML for the labels and restrictions of 飽くまで, 飢饉 and 飢える and for 餅's search-only
    餠, which Jisho's API omits.
  - Japanese sources beyond Jisho: Digital Daijisen entries for 高級, 高度, 高等, 高層, 香水, 食塩, 増大, 挿す, 刺す and 餅;
    Kotobank definitions for 拡充 and 拡張; the Daijisen and Seisenban entries for 騒騒しい on Kotobank; Daijisen 裁縫 on
    Weblio.
  - Russian sources: Gramota and Kuznetsov entries for шумливый, галдеть, рукоделие, элитный, приручиться, порядок,
    удивить, шум («наделать шуму»), привить and Morkovkin's кусать; Russian Wiktionary сугубо; dic.academic.ru (Моти) and
    food.ru for the mochi and puffed-rice contrast. Initial Gramota HTTP 429 responses and the password-gated JMdictDB
    interface were replaced by successful reads; they were not counted as evidence.
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 cards in full against EN and the complete diffs of the five navigation files; compared front matter,
    headings and link multisets with EN by read-only script.
  - Checked the SHA-256 of all 4,776 non-stroke (`kanji/`, `words/`, `articles/`) manifest entries against the committed
    blobs (no mismatch), and the intake's 35 payload paths and candidate hashes.
  - Ran `tools/validate.py` (0 errors) and, read-only, `word_title_screen.py`. Took dictionary senses from the cards'
    citations and general JMdict knowledge, without fresh lookups.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN, the five navigation diffs, and in full the existing RU ビル, 空く and 塩.
  - Used JMdict through Jisho (the live JMdictDB entry 1518320 was password-gated), Digital Daijisen 高層 on Weblio,
    Gramota орнамент and the Ozhegov and Malyi akademicheskii (MAS) entries for галдеть and элитный on gufo.me. It ran
    `link_parity.py`; it did not run the validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time; the coordinator verified HEAD `bebdf80` and a clean tree before each
  launch. Each report records the snapshot `bebdf80` with an empty `git status --porcelain --ignored` (the correctness
  and consistency reviewers before and after their checks). No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `226-words-batch-65-review-correctness-001.md`
  - `226-words-batch-65-review-consistency-001.md`
  - `226-words-batch-65-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The correctness report confirms that it read no author or reviewer report, tracking, batch or draft record or scratch
  worktree. The consistency report says that it did not read author reports, batch records or drafts; it checked the
  intake's path list and hashes, which its assignment included. The comprehensibility report says that it did not read
  batch records, author reports or other reviewer reports.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for 騒がしい, 騒々しい and 裁縫, **CLEAN** for the other 27 new cards; scoped coverage
**NEEDS FIX** for 挙げる, 驚かす and 強化, **CLEAN** for the other 27. Comprehensibility and full-pool quiz safety were not
assessed.

- C1 (minor; high confidence), `騒がしい.md:4,12` and `騒々しい.md:4,12`: the lead glosses «шумливый» and «галдящий» narrow
  general noisiness, including the noisy room the cards teach, to a noise-making agent and to people shouting together;
  the bodies correctly use «шумный». Remedy: «шумный; неспокойный (о времени)» and «шумный; неспокойный (об обстановке)».
  Evidence: Kuznetsov шумливый «Склонный шуметь» and галдеть (colloquial, «Громко, беспорядочно говорить, кричать всем
  одновременно»); JMdict 1403000 and 1596440 senses 1–2 through Jisho; Digital Daijisen 騒騒しい on Kotobank, which gives
  noisy-room usage including nonhuman sounds.
- C2 (minor, scoped coverage; high confidence), `挙げる.md:4,12` and `驚かす.md:4,12`: the titles «приводить (пример);
  перечислять» and «удивлять; поражать» each give two near-synonyms for one side and drop the EN title senses "raise" and
  "frighten", although the bodies keep 手を挙げる and the frightened-child example. Remedy: «поднимать (руку); приводить
  пример» and «удивлять; пугать». Evidence: frozen EN lines 4, 12, 23–24 and 4, 12, 18; JMdict 2864818 senses 9 and 1 and
  1238650 sense 1.
- C3 (minor; high confidence), `裁縫.md:4,12,16`: an unqualified «рукоделие» in the title admits knitting and other crafts
  beyond the sewing taught here. Remedy: «шитьё» or «кройка и шитьё», with a matching definition. Evidence: Daijisen 裁縫
  on Weblio (布地を裁って衣服などに縫いあげること); JMdict 1296200 sense 1; Kuznetsov рукоделие sense 1 («шитьё, вязание и
  т.п.»).
- C4 (minor; high confidence), `騒々しい.md:32–35`: the card defines its category as «словам китайского происхождения с
  онными чтениями», asserting Chinese origin, and then says the classification is not a claim about origin. Remedy: a
  collection-local classification by the on-reading stem, keeping the note on competing origins. Evidence: frozen EN lines
  32–35; the Seisenban entry and etymological note on Kotobank, which discuss possible 当て字 and competing derivations.
- C5 (minor, scoped coverage; high confidence), `強化.md:35`: the RU-only contrast introduces 固める without its reading;
  RU has no 固める card. Remedy: «固める（かためる）». Evidence: the RU scoped instruction to give the confirmed reading of
  an unavailable comparison word; JMdict 1266570.

What the reviewer confirmed:
- All source front-matter fields are retained apart from the translated titles and four added RU exclusion members
  (激増→急激, 高める→上がる, 驚かす→驚く, 飢饉→飢える); no EN exclusion is removed. All 30 cards' Japanese example
  sentences match EN. No EN link whose RU target exists was dropped, and no new-card Markdown target is broken.
- No defect was established in «один из лучших», «элитный» (Kuznetsov sense 2), «наращивание», «приручаться» (Kuznetsov
  приручиться sense 1) or «сугубо». Gramota entries support «удивить»/«удивляться», «наделать шуму», grafting under
  «привить» and mosquito biting under «кусать»; the mochi description and the RU-only puffed-rice contrast are attested.
- Gender-neutral Japanese permits the contextual masculine Russian translations; no gender rule is asserted.

Optional: 飾り's «орнамент» could become «декоративный элемент»; 高等's «высокого порядка» could become the plainer
«высокого уровня». Neither was established as a defect.

Limits: not a full-pool quiz audit, native-speaker certification, frequency study or complete comparison-card review;
live dictionary entries do not certify byte identity with the frozen 2026-10-21 snapshot.

### Consistency and quiz safety

Verdicts: consistency/integration **CLEAN**; quiz safety **CLEAN**; scoped coverage of cross-file integration **CLEAN**.
No actionable finding. Correctness and comprehensibility were not assessed.

What the reviewer confirmed:
- For all 30 cards, `word`, `reading`, `jlpt`, `type`, `kanji` and `tags` equal EN, and `quiz_exclusions` equal EN apart
  from the four RU additions; 高める drops nothing. おどかす and 餅 have no exclusions, as in EN. Each card has the same
  four `##` headings as EN and the published RU cards, and the H1 form is consistent.
- Link multisets equal EN except for EN-only targets with no RU file (kanji 層, 片 and 香; words 揚げる, 増減, 生け花 and
  刺さる), which stay plain, and the RU-only 強化→固まる, which is substantive, has an existing target and is acceptable.
  Every RU link target exists; the 21 written kanji without an RU kanji card are not linked.
- Each navigation diff touches only the eight link occurrences (刺: 刺す at lines 20, 31 and 40; 固: 固まる at line 32;
  塩: 食塩 at lines 28 and 34; アクセサリー: 飾り at line 35; 片付ける: 片付く at line 50), at EN's positions and in EN's
  path forms. Kanji 刺's EN links to 刺さる, its line-47 mention and 塩's line-20 食塩 stay plain, as in EN or because the
  target is absent.
- All 4,776 non-stroke manifest hashes match the committed blobs, every tracked content `.md` is listed, and only the 35
  batch entries and `contentVersion` changed. The intake's 35 payload paths are exactly the 30 new cards and five
  navigation files, its candidate hashes equal the manifest, and it adds no learner content.
- Title screen: the only exact-segment overlap is 刺す «колоть» with ちくちく «колоть; покалывать», which the retained EN
  guard 刺す→ちくちく covers. In-batch pairs stay visibly distinct.
- All four RU-added exclusions have a real basis and were marked conservative ("real basis, necessity unestablished;
  keep"); none is unjustified.
- Declined pairs judged acceptable: 一流–アナウンサー, 高級–クラス, 高度–水準, 高層–大気, 挙げる–行う and 動かす, 拡充 and
  強化–円高, 激増–急に, 片付く–処理 and 治める, 驚かす–びっくり and 意外, 騒がしい–激しい and 荒い, 飽くまで–通す,
  飢饉–ぺこぺこ and 挿す–乗せる, and the stem-only screen hits. The retained EN guards it listed are all present.

Optional: recheck 激増's «резк-» against the then-unpublished previous-batch draft; 刺す's «Это не просто ещё один способ
сказать, что её кусает насекомое.» reads awkwardly after the 雑巾 example. Limits: 118 `strokes/*.json` manifest entries
do not equal the SHA-256 of the committed bytes (pre-existing, outside the batch; see the recheck record); dictionary
senses from the cards' citations and general JMdict knowledge; necessity classes are judgements, not measurements.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** for 高層, 飾り, 騒々しい, 高等, 高級, 飽くまで, 挿す and 餅 (nine findings; the
other 22 cards CLEAN on this facet); scoped coverage **CLEAN** for all 30.

- C1 (moderate; high confidence), `高層.md:4`: the lead «многоэтажный» conflicts with the body and the station example,
  which say «высотное здание», and sits next to ビル «многоэтажное здание». Remedy: «высотный; верхние слои атмосферы» and
  «к высотному зданию». Evidence: Digital Daijisen 高層 on Weblio (sense 2 «階を重ねた高い建物», sense 1 high air); EN
  "high-rise; upper atmosphere".
- C2 (moderate; high confidence), `飾り.md:4,12,16`: «орнамент» is a calque of English "ornament"; in Russian it is a
  repeating decorative pattern, while the examples translate «украшение». Remedy: «украшение» and «飾り — украшение: то,
  что украшает предмет, человека или место.» Evidence: Gramota орнамент (Kuznetsov; Babenko).
- C3 (moderate; high confidence), `騒々しい.md:4,12`: «галдящий» is a colloquial word for people talking loudly together,
  never used in the body. Remedy: «крикливый; беспокойный (об обстановке)», avoiding a «шумный» lead shared with うるさい.
  Evidence: Ozhegov галдеть on gufo.me; JMdict 1596440 senses 1–2; EN "noisy; boisterous; unsettled".
- C4 (minor; high confidence on the mismatch), `高等.md:4,12,16`: «высокого порядка» never appears in the body, which
  teaches «высокий разряд, ступень или уровень». Remedy: «высшей ступени; высокого разряда».
- C5 (minor; medium confidence), `高級.md:4,12,16`: «элитный» is only in the title and can read as "intended for the
  elite", blurring the quality sense with the rank sense. Remedy: «высокого класса; класса люкс». Evidence: MAS and the
  gallicisms dictionary on gufo.me.
- C6 (minor; high confidence), `飽くまで.md:41`: the English JMdict gloss "after all" is used to explain why あくまで is not
  やはり. Remedy: delete it and keep the Russian point.
- C7 (minor; high confidence), `飽くまで.md:23`: «из исходного списка» refers to an authoring list. Remedy: drop it.
- C8 (minor; high confidence), `挿す.md:23`: the English gloss "graft" sits in learner prose. Evidence: JMdict 1399830 sense
  2 through Jisho ("to plant (a cutting)").
- C9 (minor; high confidence), `餅.md:29`: «вариант только для поиска в закреплённом словаре» is project jargon. Remedy:
  «餠 — редкий вариант написания, его не нужно учить.»
- Q1 (outside the facet): ビル does not exclude 高層 although 高層 excludes ビル and their titles shared «многоэтажн-».

Optional: 一流's «один из лучших» is narrower than the body's «ведущий»; 騒がしい's «шумливый» is unused in the body;
裁縫's «рукоделие» is broader than Daijisen; 馴れる's «приручаться» is uncommon; 騒々しい's «атэдзи» is not glossed here,
but it is the deck's established term; 刺す's «поисковый вариант» for 螫す is workflow-facing; 高層's example «высотных
воздушных течений» is less clear than «на большой высоте». Limits: comparison cards other than ビル, 空く and 塩 were
checked by title; the validator was not run; unlinked pointers to absent RU targets were not treated as defects.

## Exclusion classification

All 157 EN exclusion entries (28 lists) are retained in EN order; おどかす and 餅 have none. Twenty-two of them lie inside
the batch. At the candidate, 4 direct, one-sided entries were added on 4 new cards; none is a new list and none targets a
batch word.

| Entries | Author | Consistency reviewer |
|---|---|---|
| 激増→急激, 驚かす→驚く, 飢饉→飢える, 高める→上がる (4) | conservative | conservative |

The author and the reviewer agree; neither classed any entry as required. The correctness reviewer checked that the
original exclusions are retained without auditing quiz safety, and the comprehensibility reviewer did not score the
guards.

Reconciliation, the coordinator's dispositions, the exclusions added by the fix and the final verdicts are in
`226-words-batch-65-recheck-001.md`.
