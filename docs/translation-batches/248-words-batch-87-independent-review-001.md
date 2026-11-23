# Batch 248 — independent review 001

## Snapshot and scope

- Reviewed commit: `14cc61a3526acddf05f23db55318f168a6d55b44` (tree `6813010a904c7b243be5fd05a86333b6e79affa8`), branch
  `full-ru-248-words-87`, parent `848abad`. The candidate was signed and pushed before review.
  - The content was authored in the scratch lane `learning-japanese-ru-b248`, whose local-only scratch commit `2d85e8d`
    ("B248 lane drafts on B242-B247 scratch") sits on `bca83ec` ("B247 lane drafts on B242-B246 scratch"), itself on
    `4ef6fa4` ("B242 fixes 1-3 synced onto B246 lane scratch") and the earlier lane scratch commits `b37a987` and
    `282ea33`. The coordinator's candidate script checked that the lane was clean at `2d85e8d` with parent `bca83ec`,
    that the branch, HEAD~1 and `origin/main` were the expected published baseline, that the primary tree, including
    ignored files, was clean, that the four navigation files edited in the lane were unchanged between `bca83ec` and the
    published HEAD, and that none of the 30 new word files already existed.
  - The script copied 34 lane files (the 30 new cards and the navigation files `kanji/外.md`, `words/目下.md`,
    `words/課程.md` and `words/過程.md`); no follow-up edit from an earlier fix was applied. It then regenerated the
    manifest, checked that the changed path set was exactly the 34 batch paths plus `manifest.json` and byte-compared
    all 34 copies with the lane. No link was held from an earlier batch. The script's byte scan of the content paths
    prints any BOM, CR or missing final newline rather than stopping; for this record the 34 committed blobs at
    `14cc61a` (and again at the final fix `c43dd9f`) were checked: none has a BOM or CR, and every file ends with a
    newline, as `.gitattributes` requires.
  - After authoring and before the candidate commit, the coordinator edited lane cards: it split four paragraph merges
    in 盛る, 盆地, 盆 and 皮膚, removed empty exclusion lists from four cards, re-encoded one footer URL in 盆 and
    reworded examples or prose in 皮膚, 的確, 推定, 目安, 標準, 発想, 発揮, あたりまえ, 中身, 盗難, 発電, 仮定 and 狙う; the
    four navigation files were copied unchanged. Its adjudication record (lane `learning-japanese-ru-b248`, base
    `bca83ec`, uncommitted) states:
    - "Scope: all 30 new cards read in full (Russian prose, examples, title/H1, links, footers) against frozen EN
      6af98cb via an aligned EN/RU paragraph dump (b248-adj-read.txt); non-title metadata compared mechanically with EN
      (b248_cmp.py: all match except five cards carrying the six RU-added exclusions below). Link audit (rutools
      link_parity, 34 files): no lost links; one RU-only link (狙う → [目指す](目指す.md), accepted below). EN targets
      not yet published stay plain (kanji 派 身 狙 標 準 仮 推 盆 案 的 典 揮 射 盛 皮 膚; words 地味 平野 撃つ 上司 仮説
      退場 トレー 事典 処方する 率直 大盛り). Nav edits: 4 files / 4 links (kanji/外 41; words/目下 33; words/課程 33;
      words/過程 33); glosses unchanged; navonly 0 problems."

      That plain list mixes three kinds of item: the 16 written kanji without an RU kanji card (EN links only 準, 皮
      and 膚 among them); the two absent EN word link targets 地味 (from 派手) and 平野 (from 盆地); and nine words that
      EN mentions only in plain text and RU names in prose (撃つ in 発射, 上司 in 目上, 仮説 in 仮定, 退場 in 登場, トレー in
      盆, 事典 in 百科事典, 処方する and 大盛り in 盛る, and 率直 in 皮肉). A mechanical count of `.md` link targets in EN
      finds 6 EN link occurrences to 5 absent RU targets (派手→words/地味, 標準→kanji/準, 盆地→words/平野, 皮膚→kanji/皮
      and kanji/膚, 皮肉→kanji/皮);
    - the edits, each with its recorded reason:
      - 盛る, 盆地, 盆 and 皮膚: "split 4 RU merges back into separate paragraphs (盛る: «Дополнительное разговорное
        значение — …»; 盆地: the [盆](盆.md) paragraph; 盆: the [祭](祭.md) paragraph; 皮膚: «Эти различия не
        создают…»)" ("the drafts merged one EN paragraph into the previous one; the corpus keeps EN paragraph structure;
        paragraph parity now matches EN for all 30");
      - 盆地, 百科事典, 発電 and 発射: "removed `quiz_exclusions: []`" ("EN has no key on these cards and RU adds none;
        no-key precedent");
      - 盆: "footer URL `…/wiki/Обон_(праздник)` → `…/wiki/Обон_%28праздник%29`" ("parentheses inside a Markdown link
        target truncate in naive link parsers; page existence re-verified");
      - 皮膚: «Кожный покров сухой.» → «Кожа сухая.»; «…наносят на кожный покров.» → «…наносят на кожу.» ("the title
        term is unnatural in everyday example translations");
      - 的確: «Нужно меткое суждение, попадающее в точку.» → «Нужно меткое, точное суждение.»; «Учитель метко, точно в
        цель объяснил…» → «Учитель точно, по существу объяснил проблемные места.» ("redundant/calqued phrasing");
      - 推定: «…дали косвенную оценку размера…» → «По следам мы оценили размер животного.»; prose «умозаключению» →
        «выводу» ("natural Russian; title gloss is not forced into examples");
      - 目安: «…взяв за ориентировочную норму…» → «Я хожу, ориентируясь примерно на десять тысяч шагов в день.»
        ("natural Russian");
      - 標準: «Мой рост — примерно средний уровень, норма.» → «У меня примерно средний рост.» ("natural Russian");
      - 発想: «Интересная концепция.» → «Интересная мысль.» ("fits 面白い発想 in everyday speech");
      - 発揮: ex1 → «На матче я показал, на что способен на самом деле.»; ex2 → «Она проявила лидерские качества.»
        ("natural Russian, faithful to EN");
      - あたりまえ: ex2 → «Я принимал как должное, что водой можно пользоваться каждый день.» ("natural Russian");
      - 中身: ex2 → «Речь длинная, но по существу в ней ничего нет.» ("natural Russian");
      - 盗難: ex1 → «Во время поездки у нас украли багаж.» ("natural Russian (victim-side framing kept)");
      - 発電: ex2 → «Растёт выработка солнечной электроэнергии.» ("natural Russian");
      - 仮定: ex1 → «Я сделаю расчёт, допустив, что население…»; ex2 → «Допустим, что расходы…» ("natural Russian,
        faithful to EN");
      - 狙う: «целиться в цель» → «целиться в мишень» ("tautology");
    - accepted as drafted: "Faithful as drafted: 派手 目立つ 目次 狙い 目指す 思い込む 目上 案外 思いがけない 皮肉 百科事典
      白髪 登場 発射 (plus the edited cards' unchanged prose).";
    - "RU-only link 狙う → [目指す](目指す.md): a substantive synonym comparison where EN has plain text; target in this
      batch.";
    - "RU-only source footers kept: 狙う (ru.wiktionary «метить», homonym II); 盆 (ru.wikipedia «Обон (праздник)»);
      職人 precedent.";
    - "RU-added exclusions (direct pairs on new cards only): 発揮→現れ (required: shared «проявление»); 中身→内容,
      推定→観測, 推定→読み, 目安→観測, 案外→ところが (conservative). 狙う keeps the EN set [望む, 望み, 希望, 考える].";
    - "English-dependent EN notes dropped: 派手 "loud", 盆 "Lantern Festival", 思いがけない "casual", 盆地 "basin"
      reading remark (RU keeps «Читается ぼん + ち» and adapts the last note to «бассейн»). RU notes added: 目次
      «Содержание» (≠ 内容); 狙う «метить» (aim, not «ставить метку»).";
    - "仮定 follows the EN example (人口が毎年一パーセント増えると仮定して…), not the prompt's variant.";
    - "Nav glosses «неожиданно» (kanji/外) and «предположение» (課程, 過程) left unchanged (navigation-only edits).";
    - "Unverified Russian (not defects): Lopatin spelling of «Бон/Обон» (gramota.ru HTTP 429); the title follows
      ru.wikipedia.";
    - "Validation after edits (lane): manifest 5,559 files; validate 0 errors; 124 tests OK; budget OK (localZipBytes
      8,053,551); link parity: only the accepted RU-only 狙う→目指す link (34 files); navonly 4 files / 4 links / 0
      problems; diff --check clean; no BOM/CR/missing EOL in the 35 changed files; paragraph parity with EN for all
      30."

    Fix 1 later changed two of these passages again (see the recheck record): 発想:18 now reads «Интересная идея.»
    (comprehensibility C7), and the split 盛る paragraph on line 23 now opens «Дополнительное сленговое значение — …»
    (C8). Fix 1 also retitled 皮膚 «кожа; кожный покров» (C10); the coordinator's 皮膚 example «Кожа сухая.» stands. Fix
    1 also changed 派手, 目立つ, 目次, 白髪, 百科事典, 登場 and 発射, which the coordinator had accepted as drafted. The split
    paragraphs stand.

    The committed manifest records 5,559 entries (5,554 `files`, 3 images and 2 scenes; `contentVersion`
    `b4e194062bc4c700`); the coordinator's lane `validate.py` run and its phase-1 `tools/validate.py` run on the
    candidate content reported 0 errors. The correctness and consistency reviewers also ran the validator on the
    candidate (0 errors each).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 4 files with 4 restored navigation links (the kanji card 外 and the word cards 目下, 課程 and 過程);
    - `manifest.json` (`contentVersion` `b4e194062bc4c700`, 5,559 entries);
    - the intake, whose note reads "B248 30-card adaptation with four navigation-only link restorations in four
      existing files; candidate before blind review."

    Against the published baseline the candidate changes 37 files (1,390 insertions, 9 deletions), including the
    parent's publication record; the candidate commit itself changes 36 files (1,310 insertions, 9 deletions).
- Published baseline recorded in the intake: `cf24376058ba2acefd18cb772eadc519da4a6042` (Batch 247 merge, PR #131).
  Parent `848abad` ("Record B247 publication verification") adds only the Batch 247 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 4 files (4 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b248-cand-screen.txt`, 284 lines): 26 `OK` lines for pairs already guarded by an exclusion and 258
    `!!` lines. Its one exact-segment line, 狙い–考え «замысел», is `OK`, guarded by 狙い's EN entry 考え; all other lines
    are stem-only. Three lane screens exist; the two later ones have the same lines (they differ only in line endings).
    `b248-screen.txt` and `b248-screen2.txt` (284 lines each, the same lines) differ from the candidate screen in two
    stem-only lines: the 目安~純粋 line (stem «приме») and the 登場~おやすみ line (stem «выход») show different 純粋 and
    おやすみ titles (the published titles after the Batch 244 fix `149b7d7`, «чистый (без примесей); неподдельный», and
    after Batch 245's fix 1, «выходной; отдых; спокойной ночи», against the lane's pre-publication «чистый;
    неподдельный; без примесей» and «выходной день (вежливо); отход ко сну (уважительно); спокойной ночи»). No
    exact-segment line differs. `b248-screen1.txt` (288 lines: 21 `OK`, no exact-segment line) is an earlier screen with
    狙い's pre-adjudication title «прицел; нацеленность; намеченный результат» and without the RU-added guards;
  - link parity: "checked 34", no LOST link and one EXTRA, the RU-only link `words/狙う.md` → `words/目指す.md`. For this
    record link parity was verified again at `c43dd9f` with the same result; fix 1 changed no link target.
- Common sample: all three reviewers read all 30 new word cards in full, with the coverage of the EN side stated per
  reviewer below, and all three read the four navigation diffs. The consistency reviewer also read the manifest diff
  and the intake paths; the correctness reviewer inspected the manifest changes and checked the link targets and
  contextual glosses in the current RU tree.
- Correctness review scope:
  - "Model identity not verifiable."; "Each path below was read IN FULL, including front matter, every example,
    explanation, comparison, note and footer, against its frozen EN counterpart read IN FULL", followed by the 30 cards;
    "Also inspected permitted runtime diff, manifest changes and link-only patches in kanji/外.md and words/目下.md,
    words/課程.md, words/過程.md."
  - "Actual Jisho/JMdict entries were inspected for all 30 principal words, not merely search snippets or footer
    reachability; all principal cited entry IDs match."; component readings were checked via kanjiapi.dev "for all 43
    distinct characters" ("Direct shell requests failed with 403; web_fetch subsequently returned the actual
    KANJIDIC-based JSON."); «метить» was checked in ru.wiktionary and gramota.ru, the festival name and the terms
    «онное чтение» and «исконно японских слов» in ru.wikipedia, and "All 30 N2 labels match the frozen EN policy and
    pinned vocabulary source rows in docs/n2-vocabulary-sources.tsv".
  - "Permitted RU read-only validator completed: 0 error(s). This supports structural validation only."
- Consistency review scope:
  - "Read in full (front matter and body): all 30 new cards"; "Read in full: the diffs of kanji/外.md, words/目下.md,
    words/課程.md, words/過程.md."; "Also read: the manifest diff and the intake paths."
  - "EN comparison was programmatic (front matter minus title; set of .md link targets). It was not a line-by-line
    prose read."
  - "`tools/validate.py`: 0 errors."; "`build_manifest.build_manifest()` called in memory (no write) equals the
    committed manifest.json, so there is no stale hash."
  - Limits: "Dictionary senses are cited from memory of JMdict/Daijisen and the cards' own notes, and were not
    re-fetched."; "Semantic neighbour screening used the lexical title screen plus a keyword scan of RU titles, not a
    human pass over all RU titles."; "Translation accuracy was not reviewed line by line; other facets cover it."
- Comprehensibility review scope:
  - "Read in full, RU and EN:" followed by the 30 cards; "Link-only diffs in kanji/外.md, words/目下.md, words/課程.md,
    words/過程.md read. Related RU titles sampled, not every comparison card in full. Model: not verifiable from this
    session."
  - Its limits record "Did not re-read every comparison card in full, only titles and the pairs cited above. JMdict
    senses cited from the public Jisho API (jmdict attribution), not a passworded JMdictDB page. Register of 盛る sense
    6 taken from that tag and from EN, not from a separate Daijisen style label. No generator was run." It records no
    validator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `0fd72f46-6ae9-4fdd-b92d-7bcdd1d6bc01`,
  `ad3cf6a1-7139-4fc5-8d18-55f3cc20dcd1` and `7f7bbf8c-fe57-4e8a-bf7a-49232c6b51c1`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model identity
  not verifiable.", the consistency report "Model not verifiable." and the comprehensibility report "Model: not
  verifiable from this session."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "HEAD matches; status --porcelain empty at initial and
  final checks."; the consistency report records "`git status --porcelain` empty. Nothing edited, staged or
  generated."; the comprehensibility report records "no uncommitted changes (HEAD matches; git status --porcelain
  empty)". No fix was applied until all three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No repository edits, staging, commits, pushes or branch
  changes."; the consistency report says "Nothing edited, staged or generated." and called `build_manifest()` only in
  memory ("no write"); the comprehensibility report says "No generator was run." No reviewer reported changing a
  tracked repository file.
- Full blind reports:
  - `248-words-batch-87-review-correctness-001.md`
  - `248-words-batch-87-review-consistency-001.md`
  - `248-words-batch-87-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch lane worktrees.

  As in earlier batches, the consistency brief made one exception: the intake record, "check only that its path list
  matches the candidate's content diff and that it adds no learner content". The consistency report records "The
  intake path list (34) equals the content diff (34). It holds only hashes and notes, with `held: []` and no learner
  content." and "BLIND honoured: no author report, batch record, ledger or scratch worktree was read." The correctness
  report states "No author reports, other reviewer reports, translation-batch/draft records or tracking file were
  read."; the comprehensibility report makes no statement about these sources.

## Initial verdicts and findings

### Correctness

Verdicts: "Correctness: NEEDS FIX — words/目次.md (F1), words/目立つ.md (F2). Other 28 cards: CLEAN within the checked
scope, meaning no actionable defect established, not exhaustive correctness."; "Scoped coverage: CLEAN for all 30
cards."; "Russian comprehensibility and corpus-wide quiz quality: outside assigned facets; no verdict."

- F1 (medium; correctness; confidence high), `words/目次.md:18`: "探しました is translated as «Я нашёл в оглавлении
  главу, которую хотел прочитать.» EN says “I looked for…”. 探す describes searching, not successful finding." Remedy:
  «Я искал в оглавлении главу, которую хотел прочитать.» Evidence: Digital Daijisen さがす【捜す／探す】 via Weblio,
  definition "見つけ出そうとして…".
- F2 (low; correctness; confidence high), `words/目立つ.md:19`: "彼は背が高いので、よく目立ちます。 becomes «Он высокий,
  поэтому всегда на виду.» よく qualifies conspicuousness here; it does not establish “always”." Remedy: «Он высокий,
  поэтому хорошо заметен.» Evidence: Digital Daijisen よく sense 2 (high degree) and sense 6 (frequently) via Weblio;
  the report also cites EN as "stands out easily", which its recheck corrected to EN's actual "He stands out because he
  is tall".

What the reviewer confirmed: "Spelling-specific annotations checked in full Jisho entries: 中味 is marked ateji
(1599430); 思い掛けない is marked rarely-used kanji form (1610630); 的確/適確 and てきかく/てっかく occur in 1437290; 白髪
includes はくはつ alongside しらが (1583050); 案外 has the cited na-adjective sense (1154820). No mismatch established.";
"The constructions «метить в чемпионы» and «мечу в победители» fit aspiration toward a role/status."; "Festival naming:
https://ru.wikipedia.org/wiki/Обон_%28праздник%29 explicitly states «Обон … или Бон». This is actual established Russian
usage supporting the added note, not proof of normative spelling-dictionary coverage."; "No broken RU links or lost EN
links to available RU targets established. Plain text for unavailable 準, 皮/膚, 地味 and 平野 targets is justified.
狙う's added 目指す link targets an existing card. Added exclusion targets have existing cards and plausible overlapping
senses."

Optional: "Outside facets; words/発射.md:30 still uses English “catapult” in a learner-facing explanation. The
action-versus-apparatus point is retained, so this is not a coverage omission or false Japanese claim. Russian-only
replacement: «発射 называет действие запуска, а не пусковое устройство.»"; "Outside facets; English “robbery” in 盗難
and “exhibition” in 発揮 have Russian parenthetical glosses; source-list references in 盛る, 百科事典 and 白髪 may be less
useful to learners without the English source. These are accessibility observations, not additional correctness
findings." Limits: "Dictionary and RU/EN comparison evidence do not constitute a native-speaker corpus study of every
example or historical research into every component association. Festival-name usage was verified, but normative
Russian spelling-dictionary attestation remains unverified"; "This review does not certify global semantic uniqueness
of automatically selected quiz answers."

### Consistency and quiz safety

Verdicts: "Consistency: CLEAN."; "Quiz safety: CLEAN. No missing required guard. Two optional leads (O1, O2).";
"Navigation-only restorations (外, 目下, 課程, 過程): CLEAN."; "Manifest/intake integration: CLEAN." Findings: "none."

What the reviewer confirmed: "Front matter equals EN for all fields except the translated title."; "The only
`quiz_exclusions` differences are the 6 RU-appended entries on 5 cards (中身, 推定, 目安, 案外, 発揮); every EN entry is
retained."; "All relative .md links in the 30 cards resolve."; "EN links left as plain text have no RU file: 地味, 平野,
仮説, 上司, 予想どおり, 退場, トレー, 撃つ, 部下, kanji 準/皮/膚. This follows the repository convention." (Of these, only
地味, 平野 and kanji 準, 皮 and 膚 are EN link targets; 仮説, 上司, 予想どおり, 退場, トレー and 撃つ are plain text in EN, and
部下 does not appear in the batch cards. The coordinator's link audit and the records' link parity list five plain
targets.); "No dropped EN link has an existing RU target."; "One RU-only link: 狙う:29 → 目指す (in-batch sibling, a
real synonym comparison). It is useful and harmless."; navigation: "Nav files each change one line, link wrap only, at
the EN link position, and the path forms match EN", with "Surrounding prose, the pre-existing «курс» remarks and the
過程:9 exclusion are untouched." and "The old glosses are compatible with the new titles, so no change is needed.";
"Inherited from EN, not a batch defect: 的確 and 盆地 have no `kango` tag although their type is kango. The validator
passes."; "目上/目下: link only, no guard. The antonym titles «вышестоящий»/«нижестоящий» cannot be correct answers for
each other."; stem-only screen neighbours: "Each shares a stem but not a sense, so none is a defensible correct answer
and no guard is needed. The one segment hit, 狙い–考え «замысел», is guarded."; "中身 «наполнение» alone is thin for
«суть», but the 内容 guard and the body cover it."; "皮膚 «кожный покров» is deliberately formal to avoid colliding with
肌 «кожа»; 肌 and 皮 are guarded."

Optional (non-blocking, low confidence):
- O1: "発射 «пуск (ракеты, снаряда)» vs 飛ばす «запускать (в воздух)» (飛ばす guards 省く, 投げる). JMdict 飛ばす has a
  «launch» sense, so it is a possible near-answer. POS differs, EN does not guard it, and I did not verify the sense. If
  wanted: add `quiz_exclusions: [飛ばす]` to 発射 (currently none)."
- O2: "登場 vs 誕生 «появление на свет; возникновение» share the stem «появление», but the senses are birth vs entrance.
  Not exact, and EN does not guard it. If wanted: add 誕生 to 登場's list. A guard for 目安 vs 目印 is not recommended."

Limits: the dictionary, screening and translation-accuracy limits quoted above, and "BLIND honoured".

### Comprehensibility and scoped coverage

Verdicts: "comprehensibility NEEDS FIX (findings below; clean for this facet: 目次, 狙う, 狙い, 目指す, あたりまえ, 標準,
思い込む, 仮定, 推定, 目上, 盆, 案外, 思いがけない, 皮肉, 的確, 登場, 発電); scoped coverage CLEAN".

All ten findings are comprehensibility findings; C1–C8 are medium severity and C9 and C10 low; confidence is high
except for C10 (medium).
- C1 (medium), `words/発射.md:30`: "Latin-script English in learner prose, and the remark warns against a confusion only
  the English gloss invites."; "Same pattern: words/盗難.md:33 «robbery» and words/発揮.md:31 «exhibition»". Remedy:
  delete the catapult sentence; replacement sentences for 盗難 and 発揮.
- C2 (medium), `words/白髪.md:33`: "The sentence points at «список источника» and a bleaching gloss the learner cannot
  see."; "Same unseen-source pointer: words/盛る.md:21 «прописывать» «в источнике» (the card never shows that gloss) and
  words/百科事典.md:15 «Кана источника» (the reading is already in the heading)." Remedy: delete the 白髪 and 百科事典
  sentences and reword 盛る:21.
- C3 (medium), `words/派手.md:31`: "«Не путайте его грамматику な-прилагательного с окончанием い-прилагательного» has no
  Russian target." Remedy: «Перед существительным нужно 派手な, а не форма на い.»
- C4 (medium), `words/目立つ.md:19`: "«всегда на виду» adds a frequency よく does not have." Remedy: «Он высокий, поэтому
  часто бросается в глаза.»
- C5 (medium), `words/中身.md:4`: "Title «содержимое; наполнение» keeps the filling sense and drops substance. Line 19
  teaches the substance sense". Remedy: title and H1 «содержимое; суть».
- C6 (medium), `words/中身.md:25`: "«атэдзи» is not in the RU glossary and is not explained." Remedy: replace the
  term with an explanation that 味 is used for its sound, not for the meaning «вкус».
- C7 (medium), `words/発想.md:4`: "Title «образ мысли; подход (к задаче); концепция» misses the everyday "idea" sense
  and puts «концепция», which in Russian is a formal framework. Line 18 «Интересная мысль.» uses 考え's headword «мысль»
  and none of the title glosses". Remedy: title and H1 «идея; подход»; line 18 «Интересная идея.»
- C8 (medium), `words/盛る.md:23`: "«Разговорное» is a milder register than the cited dictionary. JMdict tags the
  exaggerate/heavy-makeup sense Slang; EN says slang." Remedy: «Дополнительное жаргонное значение — …».
- C9 (low), `words/盆地.md:18`: "«В межгорной впадине, окружённой горами» says "between mountains" twice." Remedy: «В
  котловине, окружённой горами, поднялся туман.»
- C10 (low; confidence medium), `words/皮膚.md:4`: "Quiz title «кожный покров» is more formal and narrower than the
  card's own everyday line 18 «Кожа сухая.»". Remedy: title and H1 «кожа; кожный покров».

Optional: "目安.md:4 is long"; "狙い.md:4 «нацеленность» is stiff"; "的確.md:19 «по существу» can be read as
"essentially""; "盛る.md:37 «подавать» rejects a gloss the card never shows."; "中身.md:33 names no other entry"; "狙う.md:25
«окуригана» is unexplained"; "皮膚.md:35 «два технических слоя» does not say it means the two kanji."; "発電 «выработка»
shares a stem with 能率 «выработка» and is not quiz-excluded; titles as wholes still differ."; it also judged several
passages clear ("派手.md:19 «швыряли направо и налево» and «вдвоём» are natural. 目次 «Содержание», 盆地.md:32 «бассейн»,
盆 naming note, 目安.md:25 «дешёвые глаза», and the 思い込む memory aid are clear.") and noted outside its facet that "盆地,
百科事典, 発電 and 発射 have no quiz_exclusions, matching EN; title-screen hits were stem overlaps, not identical gloss
segments." Limits: the comparison-card, JMdict and register limits quoted above.

## Exclusion classification

All 145 EN exclusion entries (26 lists; EN has none on 盆地, 百科事典, 発電 or 発射) are retained in EN order. 14 of them
lie inside the batch, and the other 131 target existing RU cards. At the candidate, six direct, one-sided entries were
added on five new cards, each appended at the end of its list; none targets a batch word. The reverse sides do not
declare these pairs (the consistency reviewer: "内容 has no `quiz_exclusions`; 観測 lists 予想 予測 意見 考え 見解 説 見当
見る 予報 占う 読み; ところが lists しかし でも だけど; 現れ lists 表現 言葉.").

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 中身→内容 (1) | "(conservative)" | "REQUIRED. JMdict 中身 «contents; substance» overlaps 内容. The titles «содержимое; наполнение» and «содержание; суть» overlap, and the article says so." |
| 推定→観測 (1) | "(conservative)" | "CONSERVATIVE. Basis: 観測 sense «forecast/outlook». Titles «косвенная оценка» and «прогнозная оценка (…)» share «оценка». … Real basis, necessity not established, harmless." |
| 推定→読み (1) | "(conservative)" | "CONSERVATIVE. Basis: 読み «guess; estimate». «оценка ситуации» vs «косвенная оценка»." |
| 目安→観測 (1) | "(conservative)" | "CONSERVATIVE. Same 観測 basis. «приблизительная оценка» vs «прогнозная оценка»." |
| 案外→ところが (1) | "(conservative)" | "REQUIRED by title collision. 案外 «вопреки ожиданиям» vs ところが «однако (вопреки ожиданию)». The dictionary senses differ (adverb vs conjunction), but the titles collide." |
| 発揮→現れ (1) | "(required: shared «проявление»)" | "REQUIRED by title collision. «проявление в деле» vs «проявление; выражение». 現れ had no guard for 発揮." |

The consistency reviewer added "None is unjustified."; the coordinator and the reviewer therefore differ only on whether
中身→内容 and 案外→ところが are required or conservative. The correctness reviewer found that "Added exclusion targets have
existing cards and plausible overlapping senses." without a classification, and the comprehensibility reviewer noted
outside its facet that 盆地, 百科事典, 発電 and 発射 have no exclusions, matching EN. The consistency reviewer's optional
leads O1 (発射→飛ばす) and O2 (登場→誕生) are not candidate entries; fix 1 adopted both.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`248-words-batch-87-recheck-001.md`.
