# Batch 240 — independent review 001

## Snapshot and scope

- Reviewed commit: `d0d977cad025983c702361e0408d9c9be4b8b085` (tree `401f953909d959a255de1b8abeeb08406c7d4054`), branch
  `full-ru-240-words-79`, parent `e67e771`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 239 candidate `39b6bd13afc5eec5371ce27cd611ce1ff581f19a`.
    Before copying, the coordinator's candidate script checked two things: that the four navigation files edited there
    (`kanji/花.md`, `words/忘れ物.md`, `words/花.md` and `words/足袋.md`) were unchanged between `39b6bd1` and the
    candidate's parent `e67e771`, and that none of the 30 new cards existed in the primary checkout. It also checked that
    the branch, HEAD and `origin/main` were the expected ones and that the tree was clean.
  - The script byte-compared the 34 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 34 batch paths plus `manifest.json`. Its byte scan of all
    34 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 34 committed
    blobs at `d0d977c` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from Batch 239; all six restored links were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made no content edit and no title edit; all 34 lane
    files were copied unchanged. Its adjudication record states:
    - "Screens rerun by the coordinator with RU_ROOT = lane: `validate.py` 0 errors; `navonly.py HEAD --only kanji/花.md
      words/忘れ物.md words/花.md words/足袋.md` reports 4 files, 6 links added, 0 problems; the lane's changed-path set is
      exactly the 34 paths (30 new cards + 4 restoration files) plus manifest.json (5,319 entries).";
    - per-occurrence navigation parity against EN: "kanji/花 links 花火 in the はな reading row (RU 40, EN 30) and the
      word list (RU 52, EN 35); RU 22 stays plain (EN 22 plain prose mention). 忘れ物 links 落とし物 at RU 36 (EN 26 first
      mention) and leaves RU 38 plain (EN 26 second mention plain). words/花:28 → 花火 (EN 19). 足袋:35 → 草履 and 下駄
      (EN 39).";
    - `link_parity.py` over the 34 paths (`b240-lane-parity.txt`): "蒸す LOST べたべた — EN:47–49 is the English
      "sticky/close" homonym paragraph (with AHD citations) that the brief directs to drop as English-only; the guard list
      is kept unchanged. Expected, recorded as an adaptation. kanji/花 EXTRA 北, 花瓶, 花見 — identical at the base
      `39b6bd1`, not added by B240. No RU-only links.";
    - `word_title_screen.py` over the 30 words: "one exact-segment overlap, 花嫁–嫁 «невеста», guarded by EN";
    - stem-only leads declined without guards, among them 湿度 «влажн»/«возду»/«показ», 蒸す «готов»/«прогр»/«погод»,
      撒く «погон»/«уходи», 著す «автор» (著者 guarded), 落第 «экзам» (合格 antonym, fair distractor), 若々しい «свежи»
      (新鮮), 教養 «культ»/«круго», 芸能 «искус»/«испол»/«досто», 芯 «сердц» (心 guarded), 散る/散らす «рассе»/«раски»
      and 蒸発 «челов»/«исчез» (消える guarded);
    - "Titles compared with EN one by one (`b240_titles.py`): no coordinator title edit. Every EN `quiz_exclusions` entry
      is retained in EN order; RU additions are appended.";
    - RU-added exclusions: 3 pairs on 2 cards — "required 散る→はらはら; conservative 散る→跳ねる («разлет…», no exact
      segment) and 若々しい→さわやか (shared qualifier «(о голосе, манере[ах])» and «свеж»). Accepted as harmless direct
      pairs, consistent with earlier batches.";
    - "Coordinator edits: none.";
    - author deviations accepted: 花火 mirrors EN's older format (no example list, no Dictionary line, no exclusions);
      English-only notes dropped or adapted in 蒸す/蒸し暑い ("sticky/close" paragraphs, guards kept), 下駄 "clog", 茂る
      "luxurious", 落第 "make the grade", 蒸気 "vapour" and 英和's language-order remark; 芸能 "accomplishments" and 艶
      "glaze" kept once in parentheses with a Russian gloss;
    - left to the blind review: 芸能's second title segment «освоенное искусство (как достоинство человека)», 若々しい's
      qualifier «(о голосе, манерах)» and the conservative さわやか guard, the 散る→跳ねる guard, 下駄 «на подставках»,
      散らす:21 «Я раскидываю рубленый зелёный лук поверх салата» and 花火's «ручные бенгальские огни» for 手持ち花火 versus
      «маленькие бенгальские огни» for 線香花火;
    - unverified Russian usage: "«дзори» (no Lopatin entry; Polivanov transliteration, consistent in title and body);
      other ordinary Russian wording not dictionary-checked (gramota.ru HTTP 429); «гэта» confirmed in Lopatin.";
    - a dependency on Batch 239: "葬式 excludes and links 儀式 (EN). After any B239 fix to 儀式's title, re-check 葬式 and
      rerun the title screen for the 30 words on the published B239 tree." Batch 239's fix `8cc7216` did not change
      `words/儀式.md` (`git diff --stat 39b6bd1 8cc7216 -- words/儀式.md` is empty), and its title «церемония; обряд,
      ритуал» is identical at `39b6bd1` and at the published `bbc2be2`;
    - missing kanji with EN links (plain text, no link): 嫁 履 撒 暑 湿 第 艶 芯 芸 茂 著 葬 蒔 蒸 養 駄 "where EN links them";
      unavailable words left plain: 液体, 乾燥, 巻く, 枯れる, さっさと.

    The committed manifest records 5,319 entries (5,314 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The consistency
    reviewer also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 4 files with 6 restored navigation links (the kanji card 花 and the word cards 忘れ物, 花 and 足袋);
    - `manifest.json` (`contentVersion` `c8706e72790b4f7f`, 5,319 entries);
    - the intake, whose note reads "B240 30-card adaptation with six navigation-only link restorations in four existing
      files; candidate before blind review."
- Published baseline recorded in the intake: `bbc2be2cdb84a3330a2c422a426765313041194a` (Batch 239 merge, PR #123).
  Parent `e67e771` adds only the Batch 239 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 4 files (6 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b240-cand-screen.txt`): no unguarded exact title-segment overlap (39 `OK` lines for pairs already
    guarded by an exclusion and 363 stem-only `!!` lines). The one exact shared segment, 花嫁–嫁 «невеста», is guarded by
    the EN pair on 花嫁;
  - link parity: its output was not saved with the candidate records. For this record the link targets at `d0d977c` were
    compared with frozen EN by full relative path: the only EN link lost where the RU target exists is 蒸す → べたべた (EN
    :48, in the dropped English-only "sticky/close" paragraph); every other EN link whose RU target is absent stays plain
    text; there is no RU-only link in the 34 paths apart from the pre-existing kanji/花 links to 北, 花瓶 and 花見,
    identical at the published baseline.
- Common sample: all three reviewers read all 30 new word cards in full against their complete frozen EN originals. The
  consistency reviewer also read the four navigation-file diffs in full and checked the intake path list and the manifest
  hashes; the comprehensibility reviewer read the navigation changes as link-only diffs.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file); also inspected the binding RU instructions and
    format reference, the actual linked and excluded RU titles and comparison cards "(including 儀式, 式, べたべた, はらはら,
    跳ねる, さわやか)"; a full link-set comparison across all 30 cards found the one dropped link to an existing RU target
    (C3 below).
  - Inspected the actual JMdict XML entries for all 29 explicitly cited main-word IDs and Jisho lexical entries for all 30
    words; current KANJIDIC2 (header 2026-11-22) for the component-reading labels; kanjiapi "succeeded through web_fetch
    after direct Python requests returned 403"; Digital Daijisen 勉強 and し直す (Weblio); and the official 著す spelling
    PDF (entry 015, printed p. 6).
  - Russian dictionaries consulted for the flagged distinction and several title terms: моложавый, новобрачный, глянец,
    фитиль, сердцевина, раскидывать, пар, дзори, прогревать and погоня; "Some Gramota queries were rate-limited;
    available Wiktionary entries were used where appropriate." Scoped meaning checks, not frequency claims.
  - "No validator, generator, staging, commit, push, checkout, branch switch or repository edit was performed. The only
    authored file is this report."
- Consistency review scope:
  - Read all 30 RU cards in full (front matter and body) against EN, programmatically and by reading, and all four
    navigation diffs in full with the EN link positions; ran the validator (0 errors).
  - Recomputed all 34 changed `words`/`kanji` hashes against `manifest.json` (0 mismatches) and checked that the intake's
    34 payload paths equal the content diff paths exactly: "I checked only that".
  - Read the RU cards はらはら, 跳ねる, さわやか, 棒 and 忘れ物 for guard analysis; ran `word_title_screen.py` as a lead
    and its own stem scan of all RU word titles. "Dictionary senses (JMdict/Daijisen) are cited from memory of those
    entries, not re-fetched".
- Comprehensibility review scope:
  - Read all 30 cards in full in RU and against EN; read the link-only diffs of `kanji/花.md`, `words/花.md`,
    `words/忘れ物.md` and `words/足袋.md`, the glossary table in `docs/translation-methodology.md` and the front-matter
    titles of the named near-synonyms.
  - Ran `word_title_screen.py` "as a lead only"; "`link_parity.py` was not run; the named plain-text pointers were checked
    by reading." "JMdict was not re-fetched, so sense numbers are the cards' own citations." It records no validator run
    and states "No generator was run."
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; the correctness report says "Actual model identity is not exposed/verifiable; no model name claimed.", the
  consistency report "Model: not verifiable from inside the session (unknown).", and the comprehensibility report
  "Model: not verifiable from this session."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. The correctness
  report records HEAD matching `d0d977c` at start and finish with an empty `git status --porcelain` and empty working-tree
  and index diffs; the consistency report records `git rev-parse HEAD` printing `d0d977c` and an empty
  `git status --porcelain`; the comprehensibility report records that the tracked tree matches `d0d977c` and that
  `git status --porcelain` showed only an untracked `tools/__pycache__/`, "Not part of the candidate". No fix was applied
  until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No validator, generator, staging, commit, push, checkout, branch
  switch or repository edit was performed."; the consistency report says "I did not run build_manifest.py or any
  generator." and records a `tools/validate.py` run (0 errors); the comprehensibility report says "No generator was run."
  and that the untracked `tools/__pycache__/` "was not inspected". No reviewer reported changing a tracked repository
  file.
- Full blind reports:
  - `240-words-batch-79-review-correctness-001.md`
  - `240-words-batch-79-review-consistency-001.md`
  - `240-words-batch-79-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the `-b198` and `-b216` scratch worktrees;
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  As in Batch 239, the consistency brief made one exception: the intake record, for its path check. The consistency
  report records that check ("I checked only that"). The correctness report states "Did not inspect author/reviewer
  reports, tracking/disposition records, forbidden session files or scratch worktrees."; the comprehensibility report
  makes no statement about unread materials beyond its stated scope, and its reviewer ran `word_title_screen.py` itself
  as a lead rather than reading the coordinator's output.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** (C1, C2 and C4); scoped coverage **NEEDS FIX** (C3); Russian comprehensibility
**UNVERIFIED** ("outside the two assigned facets"). "Japanese sentences and kana reading strings match EN; no
reading/conjugation defect established. The two source-attribution findings are inherited from EN, not Japanese-text
translation mutations."

- C1 (moderate; high confidence), `落第.md:20`: «Я провалил экзамен и заново выучил материал.» adds successful
  acquisition: «выучить» means to memorize or assimilate, whereas もう一度勉強し直しました reports studying again. Evidence:
  Digital Daijisen 勉強 sense 1 and し直す (Weblio); Kuznetsov «выучить» sense 1, «Уча, запомнить, усвоить»; frozen EN
  :21 "studied the material again". Remedy: «Я провалил экзамен и снова занимался, повторяя материал.»
- C2 (low; high confidence for the current source discrepancy), `茂る.md:28`: «滋る помечено как устаревшее» is stronger
  than the cited JMdict entry 1533740, which marks 滋る as a "rarely used kanji form", not obsolete. EN 茂る:25 contains
  the same stronger claim. Remedy: «滋る помечено как редкое написание; в этих примерах используйте 茂る.»
- C3 (low; high confidence; scoped coverage), `蒸す.md:42`: frozen EN :48 links べたべた, whose RU card exists; removing
  the English-only "sticky/close" discussion also removed this existing-target comparison and link. "The English framing
  can be omitted, but the explicit link-retention contract is not satisfied." Remedy: a Russian comparison sentence,
  «[べたべた](べたべた.md) описывает липкость поверхности или тесное льнущее поведение, а не само по себе жаркую влажную
  погоду.», without restoring the English labels or the American Heritage citations.
- C4 (low; high confidence for the current dictionaries), `艶.md:45`: «Среди английских переводов в словаре есть «glaze»
  (глазурь)» attributes "glaze" to the card's dictionary, but JMdict 1177680 sense 1 is gloss/luster/shine/sheen/polish;
  "glaze" is a KANJIDIC2 character gloss. EN 艶:45 contains the same framing. Remedy: «Блеск поверхности не означает ни
  материал глазури, ни само покрытие керамики глазурью.», keeping the following distinction sentence.

What the reviewer confirmed:
- Japanese example sentences and kana reading strings match EN; no reading or conjugation defect.
- "No broken runtime links or other dropped links to existing RU cards established."
- No defect from illustrative pronoun or gender choices, the omitted overt «один», result-state «разрослась» or timely
  «быстрый ответ»; English-dependent-only passages in 気体, 蒸す, 蒸し暑い, 下駄 and 茂る "need not be restored merely for
  literal English parity".
- The official 著す spelling source "matches the card".

Optional: outside its facets, explain годан/итидан/окуригана/дзюкудзикун at first use; «посыпаю салат рубленым зелёным
луком» instead of «раскидываю … поверх салата» (散らす:21); «салютные заряды» rather than «салютные залпы» (花火:25).
"These are not counted as established correctness findings." Limits: current dictionaries rather than reconstructed
historical captures; "This is not dictionary authentication of every Russian collocation or a native-speaker readability
claim."

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **CLEAN** ("optional notes only; all EN exclusions retained, 3 RU additions
classified"); scoped coverage / cross-file integration **CLEAN**. "Findings: none (no actionable defect established)."

What the reviewer confirmed:
- Front matter word, reading, jlpt, type, kanji and tags are identical to EN on all 30 cards; every EN `quiz_exclusions`
  entry is retained in EN order; the only additions are 散る +[はらはら, 跳ねる] and 若々しい +[さわやか]; all relative
  links resolve.
- Link sets equal EN except EN-only links whose RU targets are absent (the kanji cards 蒸, 湿, 著 and 芸; the word cards
  液体, 乾燥, 巻く, 枯れる and さっさと), rendered as plain text; and 蒸す → べたべた (EN :48), inside the dropped English-label
  paragraph: "no RU sentence remains for it to sit in, so I do not count it a defect". "RU has no link without an EN
  counterpart." No inbound links are owed.
- The four navigation diffs are "bracket/href only"; kanji/花 :22 and 忘れ物 :38 stay plain as in EN; the glosses beside
  the new links do not conflict with the new titles.
- Footers match EN apart from the two dropped AHD links in 蒸す and 蒸し暑い; the manifest's 34 changed hashes equal the
  file bytes; 葬式's «похороны» stays consistent with 儀式 «церемония; обряд, ритуал» and 式 «церемония; формула».
- 花嫁–嫁 «невеста» is the only exact shared title segment, guarded by EN's 花嫁→嫁. The unguarded in-batch pairs are
  separated by their titles; its own stem scan (for example 芯 versus 棒, 著す versus 作文, 蒔く versus 挿す, 早速 versus
  直/もうすぐ/ぺろり) "found no further defensible correct-answer pair". No title was found misleading.

Optional:
- O1: 蒸す and 蒸し暑い keep six guards (べたべた, 密, 近い, 親しい, 閉じる, 閉まる) whose only EN rationale (English labels
  'sticky'/'close') was dropped; "harmless dead weight with no in-card explanation"; they must stay, and "蒸す→べたべた
  could be re-linked there".
- O2: 撒く's title «уходить от погони» reads intransitive while the verb is transitive (追っ手をまく); «отрываться от
  погони» "is a wording preference only, not required".
- O3: 気体→物質 and 落とし物→物 could be added as conservative guards (hypernym overlap); "not required by the contract".

Limits: dictionary senses cited from memory, not re-fetched; 花火 has no `quiz_exclusions` and no dictionary footer,
"mirroring EN's older card format; acceptable parity, worth recording as a limit rather than a defect"; the manifest was
not regenerated; pre-existing differences from EN in the navigation files (for example kanji/花 → 花見) were left
unreviewed as out of batch.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX**; scoped coverage **NEEDS FIX** for 花火 and 著す, **CLEAN** for the other 28
cards; correctness **UNVERIFIED** ("outside the assigned facets; not a full audit").

- C1 (medium), `湿気.md:18`: «из исходного списка» has no referent for a learner. Remedy: delete line 18.
- C2 (medium), `蒸す.md:42`: «прямых исключений в тестах» is quiz-metadata talk, not a Japanese distinction. Remedy:
  delete that sentence.
- C3 (medium), `蒸す.md:4`: the title is too long to choose as a quiz option, and «прогревать паром» is a stiff register.
  Remedy: «готовить на пару; душно и влажно (о погоде)».
- C4 (medium), `芸能.md:40`: a warning about the English gloss «accomplishments», which the card never shows. Remedy:
  replace the sentence without the English word.
- C5 (medium), `芸能.md:4`: the second title segment is long, «достоинство» ordinarily means a virtue or merit, and it
  stem-overlaps 長所 «достоинство; преимущество». Remedy: «исполнительские искусства; развитые умения».
- C6 (medium), `艶.md:45` and `:31`: «glaze» is English in learner prose and rejects a gloss the card never offers; line
  31 is about the card set. Remedy: delete lines 31 and 45.
- C7 (high; comprehensibility and scoped coverage), `著す.md:4` and `:19`: the title and both examples teach a state of
  being an author, while 著しました / 著した are past acts of writing or publishing. Remedy: «написать (книгу, труд);
  издать своё сочинение», with «Она написала книгу об истории Японии.» and «Этот учёный написал много книг.»
- C8 (medium), `教養.md:21`: «Она образованный, культурный человек» reads awkwardly, and «культурный» blurs the contrast
  with 文化. Remedy: «Она — человек широкой образованности.»
- C9 (medium), `教養.md:19`: 教養を深めたい is translated «расширить свой кругозор», but 深める is deepen (EN "deepen").
  Remedy: «Я хочу углубить свою образованность с помощью чтения.»
- C10 (medium), `若々しい.md:4` and `:20`: «юношески свежим» is an odd voice for 母, and «свежий» sits next to 新鮮 and
  さわやか. Remedy: title «молодой облик; моложавый» and «Мама говорит молодо звучащим голосом.»
- C11 (medium), `散らす.md:21`: «раскидываю» for a garnish fights the card's own deliberateness note. Remedy: «Я посыпаю
  салат рубленым зелёным луком.» and title «рассеивать; посыпать».
- C12 (medium), `花火.md:21`: «дзюкудзикун» is not in the RU glossary and is not explained; «(рэндаку)» on line 20 is the
  same class. Remedy: drop «(рэндаку)» and restate line 21 without the term.
- C13 (medium; comprehensibility and scoped coverage), `花火.md:15` and `:25`: 手持ち花火 and 線香花火 are both «бенгальские
  огни», split only by «ручные» versus «маленькие». Remedy: title «фейерверк; ручной бенгальский огонь» and distinct
  glosses on lines 15, 25 and 30.
- C14 (medium), `芯.md:4`: the title omits the pencil-lead sense the first example teaches. Remedy: «сердцевина;
  грифель; фитиль».
- C15 (medium), `早速.md:21`: «быстрый ответ» uses 速い's quiz word «быстрый», which the card calls the wrong contrast.
  Remedy: «Спасибо за ответ без промедления.»
- C16 (medium), `落とし物.md:20`: «полицейскую будку» differs from 交番's title «полицейский пост». Remedy: «…на
  полицейском посту.»
- C17 (medium), `撒く.md:4` and `:18`: «уходить от погони» leaves out the unwanted companion the same sentence names.
  Remedy: «рассыпать, разбрызгивать; отделаться от преследователя» and delete « — уходить от погони» on line 18.
- C18 (medium), `花嫁.md:19`: «Невеста была в белом платье» is the same Russian frame as 嫁:19. Remedy: add a contrast
  sentence.
- C19 (low), `草履.md:20`: the two first-person examples switch gender. Remedy: genderless plural forms.
- C20 (low), `茂る.md:20`: 木の葉 is translated as the subject «деревья». Remedy: «…листья деревьев густо
  разрастаются.»
- C21 (low), `散る.md:27` and `艶.md:29`: «окуригана» is not in the RU glossary and is not glossed. Remedy: gloss it
  inline.

Optional: it checked and did not file 蒸気 «пар», 気体 «газообразное вещество», the 湿度 and 蒸発 qualifiers, 落第's
warning, 英和's language-order remark, 英文's «текст»/«предложение», the dropped English notes in 下駄 and 茂る, 蒔く
«поле», 散る's broken-glass scene, 撒く «разбрызгал», годан/итидан, the unlinked plain-text pointers and the link-only
navigation edits. Limits: correctness not audited card by card; JMdict not re-fetched; `word_title_screen.py` used as a
lead only; `link_parity.py` not run.

## Exclusion classification

All 132 EN exclusion entries (28 lists) are retained in EN order; 湿度 and 花火 have none in EN. Twenty of them lie
inside the batch, and the other 112 target existing RU cards. At the candidate, three direct, one-sided entries were added
on two new cards, all appended at the end of their lists; none targets a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 散る→はらはら (1) | Required | Required (titles «плавно опадать» and «опадать (о цветах, листьях)» near-identical) |
| 散る→跳ねる (1) | Conservative («разлет…», no exact segment) | Conservative (shared «разлетаться»; "necessity unestablished") |
| 若々しい→さわやか (1) | Conservative (shared qualifier «(о голосе, манере[ах])» and «свеж») | Conservative ("it guards a qualifier overlap") |

The consistency reviewer found "No over-guarding found" and raised no missing guard; its optional O3 suggested two
conservative additions. The correctness reviewer inspected はらはら, 跳ねる and さわやか among the comparison cards and raised
no exclusion finding, and the comprehensibility reviewer noted that 花嫁 already excludes 嫁 and that for 若々しい "さわやか is
excluded in metadata but never explained in the body".

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`240-words-batch-79-recheck-001.md`.
