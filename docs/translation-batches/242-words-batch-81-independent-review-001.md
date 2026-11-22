# Batch 242 — independent review 001

## Snapshot and scope

- Reviewed commit: `8cada6dfbe469d4905e64c9ba8e8e2377f1d0b6f` (tree `06db481b65bf56830aa81d275089b6c4af319389`), branch
  `full-ru-242-words-81`, parent `f02299a`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 241 scratch commit
    `268ca423eee2789298e8fe6a4609083d4469bde8` (scratch commit `7e656bc472a0a8be691c67e35f4a52982eeae5dc`). Before
    copying, the coordinator's candidate script checked two things: that the four navigation files edited there
    (`kanji/児.md`, `kanji/生.md`, `words/要領.md` and `words/風船.md`) were unchanged between `268ca42` and the
    candidate's parent `f02299a`, and that none of the 30 new cards existed in the primary checkout. It also checked that
    the branch, HEAD and `origin/main` were the expected ones and that the tree was clean.
  - The script byte-compared the 34 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 35 batch paths plus `manifest.json`. Its byte scan of all
    35 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 35 committed
    blobs at `8cada6d` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - One link was held from Batch 241 and applied by the coordinator: after the Batch 241 publication the script replaced
    the anchor «広げる（ひろげる）тоже значит», which had to occur exactly once, with «[広げる](広げる.md)（ひろげる）тоже
    значит» in the published `words/広める.md`. The other four navigation files were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made no content edit; the 34 lane files were copied
    unchanged. Its adjudication record states:
    - "Screens rerun by the coordinator with RU_ROOT = lane: `validate.py` 0 errors; `navonly.py HEAD --only kanji/児.md
      kanji/生.md words/要領.md words/風船.md` reports 4 files, 6 links added, 0 problems; the lane's changed-path set is
      exactly 34 paths (30 new cards + 4 restoration files, `b242-lane-paths.txt`) plus manifest.json (5,379 files per
      the author run).";
    - `link_parity.py`: "only kanji/生.md EXTRA 牛. That RU-only similar-sign link is already published (8ef0597,
      identical on origin/main), so it is not a B242 change. No LOST.";
    - per-occurrence navigation parity against EN: "児:20/42 → 育児 (EN 20/42), 生:47 → 生き生き (EN 46), 要領:36 → 能率
      (EN 38), 風船:21 → 膨らます/膨らむ (EN 21–22). The surrounding prose is pre-existing published text; only the
      bracket and href are added. The published glosses (児 «уход за ребёнком; воспитание», 生 «живо, энергично; с
      живостью») differ slightly from the new titles; they remain prose glosses, as EN also differs from its own titles.";
    - `word_title_screen.py` over the 30 words (`b242-screen.txt`, 287 lines): "3 segment hits, all おかけください
      «присаживайтесь, пожалуйста» against ください, どうぞ and 頂戴 on «пожалуйста». They arise only because the screen
      splits on commas; under the app/title «;» convention the whole title is one segment and «присаживайтесь» decides
      it." EN has the same "please" overlap and guards none of these pairs; "**Open question 1 decided: no guard.**" "The
      remaining 284 lines are stem-only (35 guarded OK, 249 unguarded) and were reviewed with the author's declined-pairs
      list; coordinator spot checks: 習字–ぴかぴか/澄む «чисто» (shine/clear water; declined), 耕す–薄める «возде»
      (noise).";
    - "Titles compared with EN one by one (`b242_cmp.py`). Every EN `quiz_exclusions` entry is retained in EN order; RU
      additions are appended.";
    - "RU-added exclusions: 7 pairs on 6 cards — required 能率→効果 («эффект»/«эффективность»); conservative 活躍→役割/役
      («роль»), 育児→育てる («воспит»), 肯定→主張 («утвержд»), 職人→名人 («мастер»), 習字→清書 («чисто-»). Accepted as
      harmless direct pairs, consistent with earlier batches.";
    - "Open question 2 decided: keep 学力 «уровень знаний; учебная подготовка». Kuznetsov (БТС, gramota.ru) «подготовка»
      sense 2: «Определённый запас каких-л. знаний, приобретённых в процессе обучения, занятий» — the acquired-knowledge
      sense matches EN "academic ability" without introducing «способности» (which would collide with 知能 «умственные
      способности»).";
    - dictionary checks: "«чистописание» — «Учебный предмет в начальной школе, имеющий целью выработать у учащихся
      красивый почерк» (fits 習字 as a school subject); «усаживаться» — imperfective of «усесться» (fits 腰掛ける).
      «раздольный» and «ремесленник» were checked by the author (report § Russian dictionary evidence).";
    - author deviations accepted: "Russian sense notes replace English "scholarship"/"science" notes (学力, 学術),
      "cultivate" (耕す), "I envy"/"jealous" (羨ましい: «завидую…/мне завидно»; not romantic «ревность»); 職人 RU-only note
      on the pejorative figurative «ремесленник»; 能率 «выработка» (avoids 生産 «производ-»); 実績 «послужной список»
      (avoids 経験 «опыт»); 敷く Weblio footer and «развернуть сеть охраны».";
    - a dependency on Batch 240: "no B242 card quotes any B240 title changed in fix 3544d75 (撒く 芯 芸能 若々しい 著す 蒸す;
      grep over the 34 lane paths for those words and their old wordings is empty). The lane screen used the pre-fix B240
      titles, so the title screen for the 30 words is rerun on the published B240+B241 tree before the candidate
      commit.";
    - open question 3: "words/広める.md:36 «広げる（ひろげる）тоже значит…» gains the first-mention link
      `[広げる](広げる.md)` (EN 36) in the candidate, after B241 publishes 広める. Candidate path set: 35 paths = 34 lane
      paths + words/広める.md; navigation 5 files, 7 links.";
    - left to the blind review: "naturalness of «раздольный» (広々), «утвердительное суждение» (肯定; logic-flavoured),
      «предмет для сидения» (腰掛け), «силовое воздействие» (実力), «необъятный» (膨大), «закреплять за собой» (押さえる),
      and the conservative guards above.";
    - "Missing kanji (plain, no link): 腰 線 績 肯 肌 耕 (plus 羨 肘 膨 etc. not linked in EN either). Unavailable words
      left plain: 敷地, 活力, 児童, 手首, 工員, 憎む, 恨む.";
    - candidate-time checks on the published Batch 241 tree (main `10e6ae4`): "the held link landed on words/広める.md
      **line 35** (the «:36» above was the lane-time estimate; EN line 36). `b242_cand.ps1` phase 1: manifest 5,379
      files; validate 0 errors; unittest OK; budget OK; diff --check and byte scan clean; link parity over the 35 paths
      reports only the already-adjudicated kanji/生.md EXTRA 牛; navonly 5 files, 7 links, 0 problems. The rerun title
      screen (`b242-cand-screen.txt`) still has exactly the 3 adjudicated おかけください «пожалуйста» segment hits; 広げる
      «раскладывать; делать шире; разворачивать» has no segment or stem hit against the B241-fixed 広める
      «распространять; расширять», and 広げる already excludes 広める." It adds that no B242 path quotes a title retitled
      by the Batch 241 fix `9cf1600` or the Batch 240 fix `3544d75`: "the only mentions are quiz_exclusions entries and
      the 広げる:39 contrast, which agrees with the new 広める title."

    The committed manifest records 5,379 entries (5,374 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The
    correctness and consistency reviewers also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 5 files with 7 restored navigation links (the kanji cards 児 and 生 and the word cards 要領, 風船 and 広める);
    - `manifest.json` (`contentVersion` `bffc2456054c4cd0`, 5,379 entries);
    - the intake, whose note reads "B242 30-card adaptation with seven navigation-only link restorations in five
      existing files; candidate before blind review."
- Published baseline recorded in the intake: `10e6ae41abadd21c4181bacc8286807ea8e7ce2a` (Batch 241 merge, PR #125).
  Parent `f02299a` adds only the Batch 241 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 5 files (7 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b242-cand-screen.txt`, 283 lines): 35 `OK` lines for pairs already guarded by an exclusion and 248
    `!!` lines, of which exactly 3 are exact-segment hits, all the adjudicated おかけください «пожалуйста» comma-segment
    hits against ください, どうぞ and 頂戴 (open question 1: no guard); the other 245 are stem-only;
  - link parity: only `kanji/生.md` EXTRA 牛, the pre-existing published RU-only link (`8ef0597`); no LOST link. For this
    record link parity was verified again at `5e64cd7` with the same single, pre-existing result.
- Common sample: all three reviewers read all 30 new word cards in full against their complete frozen EN originals. The
  correctness reviewer also inspected the five navigation changes; the consistency reviewer read all five navigation
  diffs in full (`-U0` diffs plus the EN lines at the cited positions) and checked the intake record (paths only). The
  comprehensibility report makes no statement about the navigation files.
- Correctness review scope:
  - "Model identity not independently verifiable. Each following RU file AND its same-path EN original has now been
    read in full (including front matter, all sections, examples, readings and citations)", followed by the 30 cards.
    "Also inspected candidate navigation-only changes in kanji/児.md, kanji/生.md, words/広める.md, words/要領.md and
    words/風船.md."
  - Inspected exact Jisho/JMdict entries for all 30 words; matched all 30 N2 identities and readings to the pinned
    vocabulary CSV (stephenmk `b062d4e`; "a community study label, not an official exhaustive JLPT list"); read Digital
    Daijisen via kotobank and weblio; checked Russian entries in Kuznetsov (gramota.ru), Ozhegov/Shvedova and
    ru.wiktionary, "including coercive силовой, knowledge/skill-level подготовка and non-mandatory extended-sitting
    усаживаться"; read a 1920 Cabinet record at the National Archives of Japan for F2.
  - "Read-only validation: python -X utf8 -B tools/validate.py in RU primary checkout, exit 0, 0 error(s). No
    generators executed."
- Consistency review scope:
  - "Read in full (body text; front matter checked field by field programmatically against frozen EN, see Limits): all
    30 new cards". "All five navigation diffs read in full (`-U0` diffs plus the EN lines at the cited positions)".
  - "Also checked: `manifest.json` (in-memory rebuild equals the committed file, contentVersion included), the intake
    record (paths only), `python tools/validate.py` (0 errors), footers (every URL and entry/sense number of all 30
    cards equals EN), kanji links, link targets."
  - It ran `word_title_screen.py` "only to a temporary file for a lead"; "JMdict was not consulted online"; it compared
    prose fidelity to EN "by eye only for 押さえる, 職人, 育児, 能率 and 実力", recording the translation accuracy of those
    bodies as UNVERIFIED by itself.
- Comprehensibility review scope:
  - "comprehensibility and scoped coverage only. All 30 new cards read in full against frozen EN `6af98cb`". "Validator
    matches the full title string; comma/semicolon splits are a learner lead, not an app bug."
  - Its limits record "link_parity on the 30 paths reported no lost/extra links" and that the 布く/藉く "search-only" tags
    were not re-checked in JMdict. It records no validator or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `ec03518c-9a93-4e9b-97ad-ede278cd4de8`,
  `fa1940bb-7c7c-4e58-b36a-9da724c26cdb` and `5a107db6-bd75-447c-87da-7f0bc262b85d`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model identity
  not independently verifiable.", the consistency report "Model: not verifiable from inside this session.", and the
  comprehensibility report "Model not verifiable."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "HEAD matched and git status --porcelain was empty
  initially and at the completion-stage recheck"; the consistency report records `git rev-parse HEAD` = `8cada6d` and
  an empty `git status --porcelain` at start, and that the untracked Python bytecode cache created by
  `tools/validate.py` was deleted, "and the tree is clean again"; the comprehensibility report records "`git status
  --porcelain` empty. No uncommitted changes." No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No repository, branch, index or commit modified; only this
  report written." and "No generators executed."; the consistency report says "I never ran `build_manifest.py` as a
  writer: I imported `build_manifest.build_manifest()` in memory with bytecode off and compared the result to
  `manifest.json`."; the comprehensibility report records no generator or validator run. No reviewer reported changing
  a tracked repository file.
- Full blind reports:
  - `242-words-batch-81-review-correctness-001.md`
  - `242-words-batch-81-review-consistency-001.md`
  - `242-words-batch-81-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  As in earlier batches, the consistency brief made one exception: the intake record, for its path check. The
  consistency report records "the intake record (paths only)" and that "no author/reviewer material in FILES was read".
  The correctness report states "Forbidden batch records, scratch worktrees and other reviewers' material were not
  opened."; the comprehensibility report makes no statement about unread materials beyond its stated scope.

## Initial verdicts and findings

### Correctness

Verdicts: "CORRECTNESS: NEEDS FIX (F1–F3). Per-article exceptions: the exact pinned “rare/search-only” labels for
布く/藉く in words/敷く.md:35 and 展げる in words/広げる.md:31–32 remain UNVERIFIED; see Limits. These exceptions are not
asserted defects." "SCOPED COVERAGE: CLEAN. All 30 pairs read completely; no missing EN teaching point, example,
citation, original exclusion or existing-target link established. CLEAN is bounded to this translation scope, not
exhaustive lexical or quiz certification."

- F1 (P2; correctness), `words/耕す.md:43–44`: «Русское «возделывать» может употребляться и переносно, например о
  развитии способностей.» "transfers the English gloss “cultivate” and its talent-development polysemy to a Russian verb
  whose inspected standard dictionary senses are agricultural." Evidence: Kuznetsov ВОЗДЕЛАТЬ senses 1–2 and
  КУЛЬТИВИРОВАТЬ sense 3 (gramota.ru); Ozhegov/Shvedova ВОЗДЕЛАТЬ; Jisho 耕す sense 1. Remedy: «耕す относится к обработке
  сельскохозяйственной почвы. Для развития способностей или отношений выбирайте другое слово по контексту.» Confidence:
  "medium-high for the unsupported standard-usage adaptation; no exhaustive corpus claim."
- F2 (P2; correctness), `words/功績.md:44–45`: «功績 не имеет отношения к передаче денег.» "The EN warning only excludes
  treating 功績 as a generic instruction to donate. RU instead categorically excludes any connection with giving money,
  misleading learners about recognition of meritorious donations." Evidence: JMdict 1275070 sense 1; National Archives,
  Cabinet record dated 1920-01-23, "公益の為に為したる寄附にして其功績を認め得る". Remedy: «Слово «вклад» может обозначать и
  денежное пожертвование, как [寄付](寄付.md)（きふ）. 功績 называет заслугу или ценимый результат, а не само действие
  передачи денег.» Confidence: high.
- F3 (P3; correctness, "evidence-contract defect"), `words/職人.md:45–47,49–50`: the RU-only note on the disapproving
  figurative sense of «ремесленник» "cites only JMdict and Japanese Daijisen. Neither cited entry supports a claim about
  the Russian word's connotations. The note itself is correct; this is missing claim-specific support, not a
  mistranslation." Remedy: add a ru.wiktionary «ремесленник» sense 2 citation. Confidence: "high; low learning impact,
  explicit task evidence requirement."

What the reviewer confirmed:
- "All Japanese example sentences and kana payloads match the EN originals."
- "IDs/word identity, reading, type, kanji, tags and levels are preserved. Original exclusions are preserved.
  Additional RU guards: 活躍 → 役割/役; 能率 → 効果; 育児 → 育てる; 肯定 → 主張; 職人 → 名人; 習字 → 清書. No unsupported
  deletion established."
- The 30 N2 identities against the pinned CSV (押さえる entry 1589080; 肯定 1281180, "not homophone 校庭"); the rare kanji
  forms 脹らむ, 厖大/尨大 and 肱/臂; Daijisen's 押さえる meanings and contrast with 抑える.
- "Link comparison found no RU-only word-card links, no missing RU target and no dropped EN link with an existing RU
  target." "The five navigation patches only wrap existing text in valid links."

Optional: `words/背負う.md:21`, «Он несёт ответственность за обеспечение своей семьи» "makes the livelihood sense
explicit" (Daijisen 背負う sense 2, 一家の生活を背負って立つ); "No aspect-only defect established: “взвалил на себя” can
express a resulting burden." "Inherited process commentary and awkward titles are comprehensibility/quiz polish, not
findings here." Limits: raw JMdict spelling annotations were unavailable (EDRDG certificate failure; JMdictDB
authentication gate; "Neither was bypassed"), so the two label checks "remain UNVERIFIED, not CLEAN and not fabricated
defects"; some requests failed (403/429); "Not every comparison/guard ID or Russian collocation was separately
dictionary-verified. No exhaustive comparison-corpus or quiz fallback audit."; "No historical-phonetic or native-device
audit".

### Consistency and quiz safety

Verdicts: consistency (format, front matter, terminology, links, footers, manifest, intake) **CLEAN**; navigation-only
restorations (5 files, 7 occurrences) **CLEAN**; quiz safety **CLEAN** ("No missing required guard. All EN exclusions are
retained in EN order, with the RU additions appended."); cross-file integration **CLEAN**. "No blocking or actionable
defects." The report gives no separate scoped-coverage verdict.

What the reviewer confirmed:
- F1, the RU-added exclusions, classified below; F2, "学力↔学術 is declared on both sides (EN)"; F3, the in-batch pairs,
  agreeing with every pair the author declined ("学力–水準/予習, 実力–知能, 膨大–量, 活躍–順調, 学術–学会, 肯定–正しい/判断,
  職人–工場, 功績–評価, 習字–ぴかぴか/澄む"); F4, おかけください, "no guard needed. 座る (EN guard) is the real confusable and
  it is guarded."; F5, weak leads (学力–成績, 実力 «воздействие»–影響, 能率–有効, 肯定–確認) left unguarded.
- F6 links: "every RU link resolves to an existing file. There are no RU-only links."; the EN links not carried over
  are exactly those whose RU target does not exist.
- F7 navigation: "Each of the five diffs changes only link brackets/hrefs", with 広める.md l.35 → `広げる.md` ("EN l.36;
  the later mention at RU l.37 stays plain, as in EN l.38"); "7 occurrences in total. No prose change."
- F8 manifest and intake: the in-memory rebuild equals the committed manifest; "The intake's 35 `.md` payload paths
  equal the candidate's `.md` content diff exactly …, `held` is empty, and the record contains no learner content".
- F9: PASS.

Optional:
- P1: 活躍 «заметная роль» is narrower than EN; «заметный вклад» would need a 貢献 guard; "I do not ask for a change".
- O1: 広める l.35 mentions 広げる before the title senses; "Same as EN (EN 広める:36). The following lines resolve it; no
  change needed."
- O2: 脱線's 戻る stays plain; "EN leaves it unlinked, so this is not a defect".
- O3: 職人's RU-only paragraph is "accurate and helpful … acceptable adaptation"; «ручного труда» narrows it slightly.

Limits: front matter compared programmatically; "Prose fidelity to EN was compared by eye only for 押さえる, 職人, 育児,
能率 and 実力 … translation accuracy of those bodies is UNVERIFIED by me."; JMdict not consulted online; the F5 screen is
not exhaustive; the title-screen tool was run only to a temporary file for a lead.

### Comprehensibility and scoped coverage

Verdicts: "Comprehensibility NEEDS FIX (clean on this facet: 敷く, 広げる, 脱線, 功績, 性能, 育児, 肯定, 肌着, 習字, 羨む).
Scoped coverage CLEAN — EN distinctions are present; English-only contrasts below are bad Russian, not missing
coverage. No correctness verdict."

- C1 (high; high confidence), `広々.md:4`: «раздольный» does not fit a room or the park, and «дающий ощущение простора»
  is a definition. Remedy: title «просторно»; :22 «В этом парке просторно.»; :47 «не просторно».
- C2 (medium; high), `膨大.md:4` and `:36`: «необъятный» is stronger than «огромны»; «в переводе» has no Russian target.
  Remedy: «непомерный по количеству»; rewrite :36–37.
- C3 (medium; medium), `おかけください.md:4`: the comma presents «пожалуйста» as a separate gloss. Remedy: «прошу сесть».
- C4 (medium; high), `学力.md:31` and `学術.md:31`: «учёность» is 学's title and does not concern money.
- C5 (medium; high), `羨ましい.md:22` and `:42–43`: «завидная история»; the partner-jealousy sentence.
- C6 (medium; high), `耕す.md:43–44`, `:49` and `:51–52`: «возделывать» is not "develop abilities"; the N2-coverage
  paragraph and the test-guard note are author notes.
- C7 (low; high), `肘.md:41–42`: «карточка кандзи»/«метаданных». Remedy: delete.
- C8 (high; high), `職人.md:4` and `:20`: «мастер ручного труда» narrows; «Он ремесленник по коже» is a calque. Remedy:
  «ремесленник; мастер ремесла»; :20 «Он мастер по обработке кожи.»
- C9 (medium; high), `腰掛け.md:4`: definition-style title. Remedy: «сидячая опора».
- C10 (high; high), `腰掛ける.md:4` and `:21`: «присаживаться» implies a short sit. Remedy: «сесть на опору».
- C11 (medium; high), `背負う.md:21`: «взвалил» drops ている. Remedy: «Он несёт на себе обеспечение семьи.»
- C12 (high; high), `実績.md:4` and `:17`: «послужной список» is a person's record. Remedy: «фактические результаты».
- C13 (high; high), `活躍.md:4` and `:19`: «роль». Remedy: «энергичная деятельность; заметные успехи».
- C14 (medium; high), `膨らます.md:4`: «раздувать» reads as "exaggerate". Remedy: «надувать; увеличивать в объёме».
- C15 (high; high), `能率.md:4` and `:21`: «выработка» is units produced. Remedy: «эффективность; темп работы».
- C16 (medium; high), `押さえる.md:4` and `:48`: «(суть)» repeats 掴む; the :48 cross-reference. Remedy: «уяснять важный
  момент»; delete :48.
- C17 (medium; high), `生き生き.md:4` and `:21–22`: «с живостью». Remedy: «оживлённо; ярко», with matching examples.
- C18 (medium; high), `膨らむ.md:4`: «увеличиваться в объёме» does not cover 期待が膨らむ. Remedy: «надуваться;
  нарастать».
- C19 (medium; high), `実力.md:4` and `:37`: «силовое воздействие» is bureaucratic; :37 rejects a gloss the card never
  shows. Remedy: «реальные способности; применение силы»; delete the sentence.

Optional: 肯定 «утвердительное суждение» is stiff; 膨らます:49 «Заглавие карточки»; Мы/свой; 広げる's segments; 育児
«уход»; 習字 vs 書道; 功績 «вклад». Limits: the 布く/藉く tags were not re-checked; unlinked pointers to missing RU files
are not defects; "link_parity on the 30 paths reported no lost/extra links"; the RU-added exclusions are outside these
facets ("drop 活躍’s 役割/役 only if C13 removes «роль»"); "Model not verifiable."

## Exclusion classification

All 165 EN exclusion entries (27 lists; EN has none on 育児, 肘 or 羨む) are retained in EN order. Nineteen of them lie
inside the batch, and the other 146 target existing RU cards. At the candidate, seven direct, one-sided entries were
added on six new cards, all appended at the end of their lists; none targets a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 能率→効果 (1) | Required («эффект»/«эффективность») | Required |
| 活躍→役割, 役 (2) | Conservative («роль») | Required (given the current RU title) |
| 育児→育てる (1) | Conservative («воспит») | Conservative ("real basis, necessity unestablished"; "EN has no list on 育児") |
| 肯定→主張 (1) | Conservative («утвержд») | Conservative |
| 職人→名人 (1) | Conservative («мастер») | Conservative |
| 習字→清書 (1) | Conservative («чисто-») | Conservative, leaning unjustified ("Harmless over-guard; may stay or go (nonblocking)") |

The two classifications differ on 活躍→役割/役 (coordinator conservative, consistency reviewer required given the RU title
«заметная роль») and on 習字→清書 (coordinator conservative, consistency reviewer conservative leaning unjustified); both
keep all seven. The consistency reviewer summarized "1 required, 4 conservative, 1 conservative-leaning-unjustified, and
1 required-because-of-the-RU-title", counting the two 活躍 entries together, and wrote "Over-guarding is limited to that
one entry." The correctness reviewer raised no exclusion finding ("Original exclusions are preserved."), and the
comprehensibility reviewer left the RU-added exclusions outside its facets, tying 活躍's 役割/役 to C13.

Reconciliation, the coordinator's dispositions, the fixes and the final verdicts are in
`242-words-batch-81-recheck-001.md`.
