# Batch 241 — independent review 001

## Snapshot and scope

- Reviewed commit: `5e43b26c27b09f0e00c766db801c20954a827654` (tree `81db4ea431574bf2d6d8de974150fd4ffa35bdf0`), branch
  `full-ru-241-words-80`, parent `b5311dd`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 240 candidate `d0d977cad025983c702361e0408d9c9be4b8b085`
    (scratch commit `268ca423eee2789298e8fe6a4609083d4469bde8`). Before copying, the coordinator's candidate script
    checked two things: that the three navigation files edited there (`kanji/着.md`, `words/あわてる.md` and
    `words/広告.md`) were unchanged between `d0d977c` and the candidate's parent `b5311dd`, and that none of the 30 new
    cards existed in the primary checkout. It also checked that the branch, HEAD and `origin/main` were the expected ones
    and that the tree was clean.
  - The script byte-compared the 33 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 34 batch paths plus `manifest.json`. Its byte scan of all
    34 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 34 committed
    blobs at `5e43b26` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - One link was held from Batch 240 and applied by the coordinator: after the Batch 240 publication the script replaced
    the anchor «さっさと пересекается», which had to occur exactly once, with «[さっさと](さっさと.md) пересекается» in the
    published `words/早速.md`. The other three links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made one content edit, to `words/自習.md`; the other
    32 lane files were copied unchanged. Its adjudication record states:
    - "Screens rerun by the coordinator with RU_ROOT = lane: `validate.py` 0 errors; unit tests OK; budget OK; `navonly.py
      HEAD --only kanji/着.md words/あわてる.md words/広告.md` reports 3 files, 3 links added, 0 problems; the lane's
      changed-path set is exactly 33 paths (30 new cards + 3 restoration files) plus manifest.json (5,349 files). The
      candidate adds the held 早速→さっさと link, so the candidate path set is 34 (`b241-paths.txt`) and navigation is 4
      files, 4 links.";
    - per-occurrence navigation parity against EN: "kanji/着:53 links 着替え in the word list (EN 45); あわてる:39 links
      あわただしい (EN 39); 広告:28 links 宣伝 (EN 33, first mention)."; "Held for the candidate: 早速:31 «さっさと
      пересекается…» → link (EN 28, first mention)";
    - `link_parity.py` over the 33 lane paths (`b241-lane-parity.txt`): "only 一段 EXTRA 段 (RU-only link, below). No
      LOST.";
    - `word_title_screen.py` over the 30 words (`b241-screen.txt`): "no exact-segment overlap. 43 guarded and 190
      unguarded stem-only lines reviewed with the author's adjudication (report § declined pairs)."; among the leads,
      さっさと–ぐずぐず «мешка» (antonym, fair distractor), 至急–速達 «срочн» (postal service) and 余計–必要 (inherited from
      EN "necessary/unnecessary"), with 自習–授業/教室 «занят», the 着替え «одежда» family and 特殊–別に «особ» declined;
      "Counts are unchanged after the 自習 edit below (rerun: 233 lines, 0 exact).";
    - "Titles compared with EN one by one (`b241_titles.py`). Every EN `quiz_exclusions` entry is retained in EN order;
      RU additions are appended.";
    - RU-added exclusions: 16 pairs on 11 cards — required あわただしい→騒ぎ («сумат»), 一段→段 («ступень»/«ступенька») and
      予備→余裕 («запас»); conservative 自然科学→自然 («естеств»), 自治→管理 («управл»), やたら→余る («сверх»), 一段→だいぶ
      («заметн»), うんと→もっと/一層/更に («больше»), なんとも→別に/あんまり («(с отрицанием)»), 展開→流れ («событий»),
      宣伝→進める («продвиг») and 広める→発展/流行 («расшир»/«распростр»); "Accepted as harmless direct pairs, consistent
      with earlier batches.";
    - "Coordinator edit: 自習 title and heading «самостоятельные занятия; самоподготовка» → «самостоятельные занятия».
      Kuznetsov (БТС, gramota.ru) defines «самоподготовка» as «Самостоятельные занятия, самостоятельная подготовка к
      чему-л. (обычно в армии или военных учебных заведениях)»; EN has the single gloss "self-study", which the first
      segment already renders. Lane revalidated: manifest 5,349 files (version 8aaa8073ffe99ba9), validate 0 errors,
      tests OK, budget OK.";
    - the RU-only link at 一段:32–33, «Отдельное слово [段](段.md)（だん）«ступенька; ярус» называет саму ступень; 一段
      считает одну такую единицу или служит наречием степени.»: "Accurate, and it explains the added 一段→段 exclusion (RU
      «одна ступень» vs «ступенька» is closer than EN "one level" vs "step"). Same precedent as the B239 RU-only links.";
    - author deviations accepted: English-dependent notes rewritten in 甚だしい, 傑作, 大層 (adding «層 само по себе
      значит «слой»»), 自衛 (English pun dropped) and 自然科学; うんと's second segment narrowed to «намного (при
      сравнении)» "to keep the comparative use distinct from «в большом количестве»"; ばからしい folding EN "foolish" into
      «нелепый; смехотворный»;
    - left to the blind review: the naturalness of «изрядно» and «раздутый (о словах)» (大層), «несуразный» (めちゃくちゃ),
      «смехотворный» (ばからしい), «уморительная нелепость» (傑作), «средоточие» (臍), «ещё заметнее» (一段), «отработка
      навыков» (稽古) and «особого рода» (特殊), and the conservative guards above;
    - unverified Russian usage: "the wording listed above is ordinary dictionary Russian but was not entry-checked by the
      coordinator (only «самоподготовка» was checked)";
    - a dependency on Batch 240: "さっさと and 至急 exclude and link 早速; 広める excludes 散らす. After any B240 fix to those
      titles, re-check these three cards and rerun the title screen for the 30 words on the published B240 tree." Its
      candidate-time recheck on the published Batch 240 tree (main `144cb25`) records "titles of 早速 and 散らす unchanged;
      the B240 fix changed only 早速:21's example translation". The titles are indeed unchanged (早速 «без промедления; не
      откладывая», 散らす «раскидывать; рассеивать»), but Batch 240's fix `3544d75` changed two example translations on
      these cards, not one: 早速:21 «Спасибо за быстрый ответ.» → «Спасибо за скорый ответ.» and 散らす:21 «Я раскидываю
      рубленый зелёный лук поверх салата.» → «Я посыпаю салат рубленым зелёным луком.» Neither B241 card quotes either
      sentence. The same recheck records the candidate screen (`b241-cand-screen.txt`: "unguarded exact 0; 191 stem-only
      lines") and one new stem lead since Batch 240's retitle, 稽古 «отработка навыков» ~ 芸能 «… освоенные искусства и
      навыки» (stem «навык»), judged "the practice activity vs the arts/skills themselves" with "no guard added";
    - missing kanji (plain text, no link): 傑 宣 展 層 替 殊 甚 稽 臍 臨 至 衛, "EN links only 層 and 替"; unavailable words
      left plain: なんとなく (from なんとも) and 広げる (from 広める).

    The committed manifest records 5,349 entries (5,344 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The consistency
    reviewer also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 4 files with 4 restored navigation links (the kanji card 着 and the word cards あわてる, 広告 and 早速);
    - `manifest.json` (`contentVersion` `6b287c38009cd16d`, 5,349 entries);
    - the intake, whose note reads "B241 30-card adaptation with four navigation-only link restorations in four existing
      files; candidate before blind review."
- Published baseline recorded in the intake: `144cb258d859b75936bd36d52e74f9e705f5d730` (Batch 240 merge, PR #124).
  Parent `b5311dd` adds only the Batch 240 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 4 files (4 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b241-cand-screen.txt`): no unguarded exact title-segment overlap (43 `OK` lines for pairs already
    guarded by an exclusion and 191 stem-only `!!` lines);
  - link parity: its output was not saved with the candidate records; the coordinator's candidate-time note records
    "link_parity: only the RU-only 一段→段 link". For this record the link targets at `5e43b26` were compared with frozen
    EN by full relative path: no EN link is lost where the RU target exists; the four EN link occurrences whose RU targets
    are absent (大層 → kanji 層, なんとも → なんとなく, 着替え → kanji 替 and 広める → 広げる) stay plain text; the one RU-only
    link is 一段 → `段.md`, beside EN's kept kanji link to 段.
- Common sample: all three reviewers read all 30 new word cards in full against their complete frozen EN originals. The
  consistency reviewer also read the four navigation-file diffs and checked the intake path list and hashes; the
  correctness reviewer read the navigation changes as changed hunks and the comprehensibility reviewer as link-only diffs.
- Correctness review scope:
  - "Full RU/EN paired reading completed for each of" the 30 cards; also checked "exact current titles and relevant
    meaning explanations of existing linked cards, plus full critical dependencies 段, 一層, 馬鹿, 早速 and 散らす". "The
    four navigation-only support changes (kanji/着.md; words/あわてる.md, 広告.md, 早速.md) were reviewed as changed hunks,
    not as full independent card audits." "all 35 reviewed runtime paths match candidate Git blobs after newline
    normalization."
  - Read the actual JMdict entries for all 30 IDs (`JMdict_e.gz`) and Jisho word objects; direct KANJIDIC2
    ("kanjiapi.dev requests returned HTTP 403"); all 30 rows in the pinned N2 source list; Digital Daijisen via kotobank
    and weblio.
  - Russian entries inspected (Gramota/Kuznetsov): средоточие, несуразный, смехотворный, уморительный + нелепость,
    раздуть, отработка + отработать, заметный and исконный; "When Gramota rate-limited, actual Wiktionary entries
    supplied изрядно (very significantly/strongly), кэндо and род sense 4 (kind)." "These establish senses/term usage,
    not experimentally measured beginner familiarity."
  - "No validator or generator run." "No repository files written; only this report was created and updated."
- Consistency review scope:
  - Read all 30 cards in full (front matter and body) and compared them with EN front matter and links by script; read
    all four navigation diffs ("Each diff is exactly one changed line and only adds the link brackets/href."); ran the
    validator (0 errors).
  - Rebuilt the manifest in memory ("equal to the committed file (contentVersion 6b287c38009cd16d)"); checked the
    intake's path list and hashes only ("It adds no learner content.").
  - Quiz screening: "every new title against all 3883 RU word titles and their `quiz_exclusions`", by Russian
    title-segment and stem overlap, the prompt's clusters and its own sense-based candidate lists. It did not run
    `rutools/link_parity.py` or `word_title_screen.py`, using its own EN-versus-RU scripts; "I did not query JMdict
    itself, so the dictionary senses cited are from my knowledge of its entries."
- Comprehensibility review scope:
  - Read all 30 cards in full, each against its EN original; read "the four learner-facing diffs (kanji/着.md,
    words/あわてる.md, 広告.md, 早速.md): link additions only"; compared the titles of 特別, 特に, 一層, 更に, 大いに, とても,
    非常に, 馬鹿, 余分, 準備, 用意, 段 and 中心.
  - "Title-screen stem hits treated as leads, not verdicts." "JMdict/Daijisen pages were not re-opened; sense claims
    rest on the Japanese sentences, the EN cards, and the entries the RU cards already cite." It records no validator or
    generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `e886c8ff-1827-4557-89f3-8449d3a57d0c`,
  `351ac265-84f5-44ee-928a-ba333de13a6d` and `a3984c15-df64-4995-b798-82684f9ef0d4`). Reviewer prose did not expose a
  lower-level serving identifier; the correctness report says "Model identifier not independently verifiable.", the
  consistency report "Model: not verifiable from inside the session.", and the comprehensibility report "Model: not
  verifiable."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "initial HEAD confirmed and git status --porcelain
  empty" and finally "RU HEAD still 5e43b26c27b09f0e00c766db801c20954a827654; final git status --porcelain empty"; the
  consistency report records `git rev-parse HEAD` = `5e43b26` and an empty `git status --porcelain` at start, and that
  the untracked `tools/__pycache__/` created by `tools/validate.py` was deleted, "and status is empty again"; the
  comprehensibility report records "git status --porcelain empty; HEAD matches. No uncommitted changes." No fix was
  applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No validator or generator run." and "No repository files
  written"; the consistency report says "No tracked file was changed, and I did not run `build_manifest.py` as a
  writer.", rebuilding the manifest in memory only, and records a `tools/validate.py` run (0 errors); the
  comprehensibility report records no generator or validator run. No reviewer reported changing a tracked repository
  file.
- Full blind reports:
  - `241-words-batch-80-review-correctness-001.md`
  - `241-words-batch-80-review-consistency-001.md`
  - `241-words-batch-80-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the `-b198`, `-b216` and `-b243` scratch worktrees;
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  As in Batch 240, the consistency brief made one exception: the intake record, for its path check. The consistency
  report records that check ("checked only the path list and hashes") and that "A directory-wide text search listed the
  file names under `docs/translation-batches/` and `docs/translation-drafts/` as matches for a transliteration term. I
  did not open them." The correctness report states "Prohibited author/reviewer reports, draft worktrees and RU
  tracking/batch directories were not read."; the comprehensibility report makes no statement about unread materials
  beyond its stated scope, and treated title-screen hits only as leads.

## Initial verdicts and findings

### Correctness

Verdicts: "Correctness NEEDS FIX (うんと, 広める, 余計); scoped coverage NEEDS FIX (うんと, 広める). For the other 27 cards,
correctness CLEAN in this review boundary; coverage CLEAN for the other 28." "Russian comprehensibility and exhaustive
quiz-pool suitability were not assigned verdicts."

- C1 (medium; high confidence; correctness and scoped coverage), `うんと.md:4,12`: «в большом количестве; намного (при
  сравнении)» "restricts its second gloss to comparison, while its first gloss covers quantity only; the noncomparative
  high-degree sense taught at line 16 has no title equivalent." Evidence: Digital Daijisen sense 2 via kotobank
  ("explicitly distinguishes extreme degree from a large comparative difference"); Jisho sense 1 "very much / a lot".
  Remedy: «много; очень; намного (при сравнении)» and the matching H1.
- C2 (medium; high confidence; correctness and scoped coverage), `広める.md:4,12`: «расширять (знания)» "restricts the
  broadening sense to knowledge, although both EN and RU:17,50–51 retain general broader extent." Evidence: Digital
  Daijisen sense 1 via weblio, "範囲を広くする", examples 知識 and 勢力; Jisho sense 2 broaden/extend/widen/enlarge. Remedy:
  «распространять; расширять» and the matching H1.
- C3 (medium; high confidence), `余計.md:4,12`: «сильнее прежнего» "makes the adverb's comparison necessarily temporal
  (“than before”)"; the lexical meaning is "all/even the more", "not necessarily one's earlier state". Evidence: Digital
  Daijisen via weblio, nominal/adjectival sense 2 (人より余計な苦労) and the adverb section (もっと・なおさら); Jisho sense 3
  "all the more / even more". Remedy: «сверх необходимого; ненужный; ещё больше» and the matching H1.

What the reviewer confirmed:
- "Every original metadata value is retained except translated titles and added exclusions; no original exclusion was
  removed." "Only 一段→段 is an added card link, and its distinction is accurate."
- "The only removed link targets are kanji 層 and 替 and words なんとなく and 広げる; all four are absent in RU and
  correctly remain plain text. Existing linked-card descriptions, including 早速 and 散らす, do not establish another
  correctness defect."
- "All original example sentence and kana contents were retained (132 Japanese sentence occurrences additionally
  checked mechanically)."
- JMdict form and ateji tags, the cited IDs and sense numbers, the three "combine as" passages in 稽古, 自習 and 自治, and
  the KANJIDIC2 readings match; "No defect established in conjugation, gemination, voicing or component classification."

Optional: "Nonblocking Russian comprehensibility polish, outside assigned facets: 一段:4,17,19 would be more direct with
“в ещё большей степени” and “После дождя стало ещё холоднее” than “ещё заметнее”. Explain итидан at first use and move
implementation-oriented remarks out of learner prose (特殊:29; やたら:30; 広める:32). No further correctness finding is
implied." Limits: "Current dictionary downloads are not claims about an archived dictionary capture."; "No exhaustive
collision/fallback certification, frequency measurement, native-speaker validation, corpus proof of relative register,
or app/device acceptance is claimed."

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; navigation-only restorations **CLEAN**; quiz safety **CLEAN** ("There are five
low-confidence optional leads"); intake record **CLEAN**. "Findings: none actionable." The report gives no separate
scoped-coverage verdict.

What the reviewer confirmed:
- `word, reading, jlpt, type, kanji, tags` equal EN on all 30 cards; every EN `quiz_exclusions` entry is retained; every
  `.md` link resolves; the EN links absent in RU are all to targets with no RU file (大層 → `../kanji/層.md`; なんとも →
  `なんとなく.md`; 着替え → `../kanji/替.md`; 広める → `広げる.md`); one RU-only link, 一段 → `段.md`; "Repo-wide EN→RU
  link-count parity for the 30 targets found no dropped link and no RU-only link in any existing file."
- "no new word title duplicates any RU word title, and no new `;`-separated title segment equals a segment of another
  word title."
- Restorations: kanji/着.md:53 (EN line 45) "The mention occurs only on that line."; あわてる:39 (EN line 39); 広告:28 (EN
  line 33) and 早速:31 (EN line 28), each "the only mention"; "Glosses beside the new titles do not mislead", with 着's
  «смена одежды; одежда на смену» a body gloss "as in EN (EN gloss vs EN title differ the same way)".
- The manifest's hashes, the intake's `candidateRawSha256`, no CR, tab, BOM or trailing whitespace in the new cards, and
  "No generated or unrelated file is in the commit (36 files: 30 new + 4 modified + manifest + intake)". Terminology
  (итидан, атэдзи, «Digital Daijisen через Weblio», Дайдзисэн) "matches existing cards".

Optional:
- O1 (low confidence): 格別 → 別に, for 格別問題はありません; "not required".
- O2 (low): いきなり vs 意外 «неожиданный»; "The title «без предупреждения; с ходу» does not itself match 意外."
- O3 (low): でたらめ «чепуха; как попало» vs くだらない «вздорный»; "Not required."
- O4 (low): 余計 vs 贅沢 «роскошь; излишество»; "Not required."
- O5 (low): 臨時 body «дополнительный поезд» vs 追加 «дополнительный»; "the pair is not a defensible quiz match".
- O6 (nonblocking): the RU-only 一段 sentence and `段.md` link "is accurate and useful, and it supports the required
  一段 → 段 guard. Judge it under the fidelity facet."
- O7 (nonblocking): 展開's inline code for `a(b + c) = ab + ac` "is already used in 35 other word cards, so this is
  acceptable."

Limits: "Lexical-overlap screening is a lead generator, not a verdict."; dictionary senses from its knowledge; "The
manifest rebuild was done in memory by importing `build_manifest`. The file on disk was not written."; "Prose accuracy,
Russian style and translation fidelity (the other reviewers' facets) were read for consistency only and were not
audited in depth."; tags equal to EN were judged as EN parity.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX**; scoped coverage **CLEAN**.

- C1 (medium; high confidence), `一段.md:4` and `:19`: «ещё заметнее» "teaches “more noticeably”, not 一段と “even more /
  to a further degree”", and the example becomes «похолодало ещё заметнее». Remedy: title and H1 «ещё больше; одна
  ступень»; example «После дождя стало ещё холоднее.»
- C2 (medium; high), `ばからしい.md:4` and `:20`: the title drops the foolish/not-worth-it sense taught at line 16, and
  «смехотворный» "is bookish and pulls the quiz answer toward 傑作’s humorous absurdity". Remedy: «глупый; нелепый»;
  example «Верить таким слухам глупо.»
- C3 (medium; high), `余計.md:4` and `:21`: «сильнее прежнего» "narrows “all the more” to “stronger than before”"; the
  example drops てしまう and adds «совсем». Remedy: «сверх необходимого; ненужный; тем более»; example «Я в итоге сказал
  лишнее.»
- C4 (medium; high), `広める.md:4`: «расширять (знания)» makes the second sense knowledge-only. Remedy: «распространять;
  расширять».
- C5 (medium; high), `大層.md:4` and `:21`: «изрядно» is colloquial against the card's own register note at line 45,
  «раздутый (о словах)» "is not a natural gloss for exaggerated speech", and «Мне преподнесли» misrenders humble
  いただきました. Remedy: «в большой степени; внушительный; преувеличенный»; example «Я получил внушительный подарок.»
- C6 (medium; high), `うんと.md:4`: the title drops the non-comparative degree the article states. Remedy: «много;
  очень; намного».
- C7 (medium; high), `なんとも.md:22`: «Меня это вовсе не волнует» "replaces 思いません with “doesn’t worry me”", hiding
  the verb the nuance section depends on. Remedy: «Я об этом вовсе так не думаю.»
- C8 (medium; high), `宣伝.md:20` and `:21`: «Продавцы» narrows 店の人, and «рассказать всем» "adds «всем», and collapses
  the example toward 広める". Remedy: «Сотрудники магазина рекламируют новый товар.» and «Я попросил друга
  порекламировать школьный фестиваль.»
- C9 (medium; high), `格別.md:4`: «особенный» "is the gloss 特別 already teaches". Remedy: «необычайный; в особенности».
- C10 (medium; medium confidence), `あわただしい.md:4`: «торопливый» "ordinarily describes a person or a manner", undoing
  the contrast with あわてる. Remedy: «суматошный; спешный».
- C11 (medium; high), `予備.md:4`: the title "reads as a definition, not a quiz label", and «силы» is not in the
  examples. Remedy: «резерв; предварительная подготовка».
- C12 (low; high), `広める.md:32`: «метаданные основной записи» refers to front matter the learner cannot see. Remedy:
  delete «Она не добавляет 弘 в метаданные основной записи этой карточки.»

Optional: やたら:30 (delete the empty-kanji-list sentence); 特殊:29 (drop «в этой коллекции нет»); 自習:41 (drop the
JMdict-entry framing); 傑作:23 («Дайдзисэн») and :20 («один из»); 臨時:4 (add «дополнительный»); 臍:4 («средоточие» is
bookish; "avoid bare «центр»: 中心/中央"); 稽古:20 («кэндо», "a one-word gloss is optional"). It found the subject
pronouns, several other renderings and notes "clear enough for a Russian reader". Limits: "Title-screen output was a lead
only. Quiz-exclusion asymmetry (やたら excludes でたらめ; でたらめ does not exclude やたら) is outside these facets. No
native-speaker or learning-effectiveness claim."

## Exclusion classification

All 297 EN exclusion entries (30 lists) are retained in EN order. Twenty-nine of them lie inside the batch, and the
other 268 target existing RU cards. At the candidate, sixteen direct, one-sided entries were added on eleven new cards,
all appended at the end of their lists; none targets a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| あわただしい→騒ぎ (1) | Required («сумат») | Conservative ("Shared Russian root and sense (uproar/commotion vs hectic); POS differs.") |
| 一段→段 (1) | Required («ступень»/«ступенька») | Required ("EN-link only; this direct pair is needed") |
| 予備→余裕 (1) | Required («запас») | Required ("«запас» = «резерв» in Russian, and the parentheticals overlap («силы»)") |
| 自然科学→自然 (1) | Conservative («естеств») | Conservative |
| 自治→管理 (1) | Conservative («управл») | Conservative ("a real title trap; harmless") |
| やたら→余る (1) | Conservative («сверх») | Conservative-weak |
| 一段→だいぶ (1) | Conservative («заметн») | Conservative |
| うんと→もっと (1) | Conservative («больше») | Conservative |
| うんと→一層, 更に (2) | Conservative («больше») | Conservative-weak ("harmless") |
| なんとも→別に, あんまり (2) | Conservative («(с отрицанием)») | Conservative ("Same negative-polarity slot") |
| 展開→流れ (1) | Conservative («событий») | Conservative |
| 宣伝→進める (1) | Conservative («продвиг») | Conservative ("Russian-title trap, not a dictionary synonym") |
| 広める→発展, 流行 (2) | Conservative («расшир»/«распростр») | Conservative |

The two classifications differ only on あわただしい→騒ぎ (coordinator required, consistency reviewer conservative); both
keep it. The consistency reviewer found "No entry is unjustified: each has a real dictionary or Russian-title basis and
an ordinary-quiz risk. None needs removal. A reader who prefers the narrowest lists could drop うんと → 一層/更な and やたら
→ 余る as weakest." (sic: 更な for 更に), and in its dense-cluster check "every pair in the prompt's clusters has a direct
exclusion on at least one side. … I did not infer transitive pairs." Its five optional extra guards are listed above.
The correctness reviewer raised no exclusion finding ("no original exclusion was removed"), and the comprehensibility
reviewer noted the existing exclusions beside several of its remedies (for example 一層/更に for 一段, 馬鹿 for ばからしい,
とても and 非常に for うんと) and left the やたら/でたらめ asymmetry outside its facets.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`241-words-batch-80-recheck-001.md`.
