# Batch 230 — independent review 001

## Snapshot and scope

- Reviewed commit: `5ec190a7c89f162bdb1673eca213fab94aab9624` (tree `6d3c31bd01596be9b29662885a4d2cae61c73bac`), branch
  `full-ru-230-words-69`, parent `8a4f655`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 229 candidate `af5541a48700cdb110c81f127f63f226ead77ae7`.
    Before copying, the coordinator's candidate script checked two things: that the navigation file edited there
    (`words/ベル.md`) was unchanged between `af5541a` and the candidate's parent `8a4f655`, and that none of the 30 new
    cards existed in the primary checkout. The Batch 229 fixes touched only ストップ, 学会, 期限, 終了, 締め切り, 締め切る,
    開通, 関わる, 防止, 防犯, 隔てる and 障子; none of them is in this batch's path set.
  - The script byte-compared the 31 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly those 31 paths plus `manifest.json`. Its byte scan of all 31
    content paths found no BOM or CR, and every file ends with a newline, as `.gitattributes` requires.
  - No wraps were held from Batch 229, and the coordinator applied none separately; the one navigation link was copied
    from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made no content edits. Its adjudication record
    states:
    - "Classification: only 四角い:27 and 鉢:29 mention kango, each mirroring an EN body sentence (EN :27, :29); no added
      kango/wago body sentence (B229 lesson honoured).";
    - "RU-added exclusions (3), each one-directional; targets do not declare them back: 丼→料理, 鉢→植木, 過程→途中.
      Checked titles: 料理 «готовка; кухня; блюдо», 植木 «садовое дерево; растение в горшке», 途中 «по пути; в процессе».
      Not added: 丼 vs お皿 «тарелка; блюдо для подачи» / 鍋 «кастрюля; горячее блюдо набэ» (distinct dish/vessel
      segments).";
    - "No RU-only links. 長方形 kept plain where EN is plain.";
    - "Author incident (relative-path line-ending rewrite of 30 EN files in the EN session worktree) verified reverted:
      `git status` there shows only the pre-existing `words/能力.md` change". The frozen EN commit itself was not
      affected.

    After copying, `tools/build_manifest.py` recorded 5,019 files and `tools/validate.py` reported 0 errors.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 1 file with 1 restored navigation link (the word card ベル);
    - `manifest.json` (`contentVersion` `cf8e1ff9dcb79ff6`, 5,019 entries);
    - the intake, whose note reads "B230 30-card adaptation with one navigation-only link restoration in one existing
      file; candidate before blind review."
- Published baseline recorded in the intake: `d90e5eae566e22f9cb1dbba5f0a45c837f3ad316` (Batch 229 merge). Parent
  `8a4f655` adds only the Batch 229 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK (the authoring worktree run reported 124 tests);
  - content budget: OK;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 1 file and 1 link, with no problem;
  - title screen: no unguarded exact title-segment overlap (29 `OK` lines for pairs already guarded by an exclusion and
    279 stem-only `!!` lines);
  - link parity: no EN link lost where the RU target exists, and no RU-only link.
- Common sample: all three reviewers read all 30 new word cards in full against their full EN originals, and the
  `words/ベル.md` navigation change. The consistency reviewer also compared each card's front matter and link set with EN
  by script.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN (attested file by file with line ranges), the three binding RU
    references, the existing RU cards ちゃわん, ベル and 合う in full for conventions and comparisons, the ベル link-only
    change and the manifest diff.
  - Inspected the Jisho/JMdict forms, senses, restrictions and parts of speech for all 30 headwords and checked each
    word page's JMdict ID against the card; inspected the rare-form notes for 錆 (銹/鏽), 鉱物 (礦物) and 鉄砲 (鉄炮) and
    the forms and restrictions of 銅.
  - Japanese sources beyond Jisho: Digital Daijisen headings on Weblio for 四角, 四角い, 長方形, 鑑賞, 鉢, 鉄橋, 鉄砲 and
    鈴, and モーラ for its optional item.
  - Russian sources: Kuznetsov entries for бубенчики, бубенцы and достоинство; Gramota's Babenko entry череп; Russian
    Wiktionary entries for темпура, благоустройство, техобслуживание, уравновешиваться, соразмерный, горшок, курс and
    звоночек; a Russian Hokkaido University page; a Russian Buddhist-dictionary entry for патра; Russian running text
    using донбури (usage evidence only, not normative registration); a Russian teaching text for итидан and годан
    (spelling only); and Rybin's 2009 article on syllable and mora.
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 cards in full against EN (front matter and body), the full `words/ベル.md` diff, the manifest diff and
    the intake record; compared the front matter and links of all 31 files with EN by script and checked RU target
    existence.
  - Checked that the manifest holds the correct SHA-256 for all 31 changed files and that the intake's 31 payload paths
    and hashes equal the candidate diff.
  - Ran `tools/validate.py` (0 errors), its own `word_title_screen.py` run (no unguarded identical-segment overlap, 29
    guarded) and stem scans of all RU titles. It did not re-fetch dictionary pages.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN and `words/ベル.md` in full. Comparison cards were not all read in full, and
    title-screen overlaps were used as leads only.
  - Took senses from the cards' cited JMdict entry IDs, Digital Daijisen on Weblio and public JMdict mirrors (JMdictDB
    itself asked for a password). It ran `link_parity.py` on the 31 paths, which printed only "checked 31"; it ran no
    validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. Each report records
  the snapshot `5ec190a` with an empty `git status --porcelain`. No fix was applied until all three reports were
  complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `230-words-batch-69-review-correctness-001.md`
  - `230-words-batch-69-review-consistency-001.md`
  - `230-words-batch-69-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - the scratch worktrees;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The correctness report says that it did not read the prohibited drafts, author or reviewer reports, tracking file or
  RU batch records. The consistency report says that it did not read the author's batch records or the other reviewers'
  reports; it read the intake record, whose payload paths and hashes it checked. The comprehensibility report makes no
  separate statement on this point.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for 鈴 (title only), **CLEAN** for the other 29 new cards; scoped coverage **CLEAN**
for all 30. Russian comprehensibility and comprehensive quiz safety were not assigned.

- C1 (minor, correctness; high confidence in the lexical distinction, medium-high in the learning impact),
  `鈴.md:4,12` (compare :16, 38–39): the unqualified title «бубенчик» narrows EN "bell (often globular)" to the
  spherical, rattling subtype. The reviewer framed this as a shape restriction, not a claim that a large shrine bell
  cannot be a бубенец; the body correctly denies a universal shape or size rule, but the standalone title does not keep
  that breadth. Remedy: broaden the title and H1 together, for example «колокольчик; бубенец; храмовый колокол», keeping
  the shape/use explanation and the direct guards with ベル and 鐘, and verify that any shorter label does not make the
  spherical construction compulsory. Evidence: Digital Daijisen すず【鈴】 on Weblio (sense 1, the slit hollow sphere,
  explicitly including large shrine examples; sense 2, the hanging 風鈴 type with a suspended tongue); Kuznetsov
  БУБЕНЧИКИ (=Бубенцы) and БУБЕНЦЫ (hollow metal balls with metal pieces inside) on Gramota; frozen EN's title and
  :38–40.

What the reviewer confirmed:
- The JMdict forms, senses, restrictions and parts of speech match all 30 cards, and every card's JMdict ID agrees with
  its word page. Rare-form labels for 錆, 鉱物 and 鉄砲 match; 銅's sense 2 is restricted to どう and marked as an
  abbreviation. 錆びる is ichidan and intransitive; 長引く, 揃う, 仕上がる and 釣り合う are godan as stated; 継続 permits
  both transitivities.
- Daijisen supports 四角's な/の attachment, 四角い's noun-plus-adjective formation, the inclusive rectangle definition,
  artistic appreciation in 鑑賞, Sanskrit pātra via 鉢多羅, and the specialized firearm senses of 鉄砲. The kango remarks
  identify the collection classification rather than deriving etymology.
- Russian adaptations such as темпура, благоустройство, техобслуживание, уравновешиваться, соразмерный, черепная
  коробка, достоинство, горшок and курс are supported without categorical substitution bans; донбури and патра have
  usage or historical evidence, not normative registration, and each card supplies its own Russian description.
- Translations keep tense, aspect, polarity, roles and event/result distinctions; the reviewer judged «никак не
  проходит», «должна быть готова», «бронзу» and «в сборе» defensible for correctness. Original metadata other than the
  translated titles agrees with EN; the EN exclusions are retained with the three disclosed RU additions; no EN link
  whose RU target exists is dropped; all full Japanese sentence strings found in EN are retained unchanged.

Optional: outside its facets, 録音:31 could read «Сохраняйте все четыре моры (ритмические единицы): ろ・く・お・ん; не
выбрасывайте く», avoiding the unexplained «слога-моры»; the reviewer did not present the original as a wrong count
(Digital Daijisen モーラ; Rybin 2009). Limits: a complete paired review of these 30 cards, not of the whole comparison
pool, a corpus study or a native-speaker or device check; some initial returns failed or were truncated, and only
successful entries support the conclusions; no normative-dictionary registration was established for донбури or патра;
syllable/mora terminology is optional because analyses differ.

### Consistency and quiz safety

Verdicts: consistency **CLEAN** (two optional-grade link notes, F2 and F3); quiz safety **NEEDS FIX** (one minor
finding); scoped coverage (cross-file integration) **CLEAN**. Correctness and comprehensibility were not assessed.

- F1 (minor, quiz safety; medium-high confidence), `長所.md:9`: 長所 «достоинство; преимущество» is not guarded against
  武器 «оружие; сильная сторона». 武器's figurative sense, in its title and body, equals 長所's own definition («сильная
  сторона, достоинство или преимущество»); the RU guard 得意–武器 was added for the same «сильная сторона» collision,
  and EN has no such pair because its titles differ. Remedy: `quiz_exclusions: [得意, 利益, 味噌, 武器]`. Evidence:
  JMdict 長所 sense 1 against 武器's figurative "asset/advantage" sense, resting on the RU card text; the dictionary was
  not re-fetched.
- F2 (minor, optional-grade, consistency/links; medium confidence), `四角.md:27`, `四角い.md:35` and `正方形.md:34`:
  長方形（ちょうほうけい）is glossed and contrasted next to the 正方形 comparison but left plain for EN parity, although
  its RU card now exists in this batch, and the RU rule is to link existing cards at a substantive introduction or
  comparison. Remedy: `[長方形](長方形.md)（ちょうほうけい）` at those three positions.
- F3 (minor, optional-grade, consistency/links; medium confidence), `鐘.md:29`: 鈴（すず）is a glossed comparison next to
  the linked ベル, and 鈴.md now exists. Remedy: `[鈴](鈴.md)（すず）`. The reviewer called the same remedy for 撮る at
  `録音.md:47` a weaker, optional link.

What the reviewer confirmed:
- `words/ベル.md` passes: the diff is exactly `鐘（かね）` → `[鐘](鐘.md)（かね）` at line 38; EN links 鐘 once in the same
  sentence, and 鈴 and チャイム stay plain, as in EN; no other prose changed. No other RU file has an EN link to a new
  card that is still plain.
- All EN `quiz_exclusions` are retained in EN order on all 28 keyed cards; 錆 and 銅 have no key, as in EN. Front matter
  equals EN except for the titles and the three RU additions. One-way declarations suffice, because the app applies
  pairs symmetrically; all 29 title-screen overlaps are guarded.
- Every kanji and word link resolves, and every dropped EN link has no RU target (the kanji 角, 賞, 録, 銅, 鉱, 鉄, 橋, 針
  and 課; the words 三角, 仮定, 学科, 短所 and 釜). The kanji 整 has no RU card, so 整備's statement is accurate.
  `kanji:` metadata equals EN.
- The manifest holds the correct SHA-256 for all 31 changed files; the intake's 31 payload paths and hashes equal the
  candidate diff, with no learner content; no generated or unrelated file was committed.
- The unguarded in-batch pairs (長男/長女, 鉄砲/鉄橋, 銅/鉱物, 銅/針金, イコール/釣り合う, 仕上がる/整備 and 錆/銅) are
  distinct from their titles. It judged many further pairs not to need a guard because the titles differ in sense or
  part of speech, among them 長男–兄, 長女–姉, 四角–角, 長所–特徴, 丼–皿/鍋, 鉢–花/花瓶/鍋, 録音–撮る and 過程–結果.

Optional: 長女–お嬢さん and 長所–プラス «положительный фактор» are weak hyponym or gloss overlaps and not required; 長女–娘
already follows the EN pattern. Limits: the dictionary senses for F1 were not re-fetched; linguistic correctness and
comprehensibility are outside this facet; the model identity is unverified; the author's batch records and the other
reviewers' reports were not read.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** for 四角, 継続, 鈴, 揃える, 揃う, 銅, 仕上がる and 長引く (the other 22 new cards
and the ベル link CLEAN on this facet); scoped coverage **NEEDS FIX** for 揃える and 揃う, **CLEAN** for the other 28.

- C1 (moderate, also coverage; high confidence), `揃う.md:20,31` and `揃える.md:20,30–31`: the shared frame
  必要な書類を揃えました / が揃いました is translated as active and passive of one verb («Я собрал» / «собраны»), and both
  kanji notes repeat «документы … собраны» for the intransitive 揃う, so a learner can take 揃う as the passive of
  揃える and miss "the set is present". Remedy: 揃う:20 «Все необходимые документы теперь в сборе.»; 揃う:31 and
  揃える:30 «документы все в сборе». Evidence: JMdict 1406110 senses 1–2 (completeness, uniformity); EN "I assembled"
  against "are now together".
- C2 (minor; high confidence), `四角.md:19` (against :16): «прямоугольными кусками» names rectangular pieces and uses the
  長方形 adjective for a shape that includes a square. Remedy: «Я нарезал этот хлеб в виде четырёхугольника.» Evidence:
  card line 16; JMdict 1307090 sense 1.
- C3 (minor; high confidence), `継続.md:22`: «Это состояние сохраняется» is maintenance, the territory of 維持 on line 36.
  Remedy: «Это состояние продолжается.» Evidence: JMdict 1251810 sense 1; EN "This state is continuing".
- C4 (moderate; high confidence), `鈴.md:4,12,19–23,39`: the title and every example equate 鈴 with «бубенчик», and line
  39 calls large shrine bells «бубенцы», whereas Daijisen すず sense 1 includes large shrine bells of the same hollow form.
  Remedy: title «колокольчик; бубенчик (типичный небольшой)»; line 39 «鈴 называет и большие храмовые колокольчики, не
  только бубенчики.»; keep «бубенчик» in the cat example. Evidence: JMdict 1557580 "bell (often globular)"; Digital
  Daijisen 鈴, sense 1.
- C5 (minor; high confidence), `銅.md:4,11`: «(сокращ.)» is a dictionary abbreviation, not a learner gloss. Remedy: title
  «медь; бронзовая медаль (сокращение)». Evidence: JMdict 1582390 sense 2; EN spells out "abbreviation".
- C6 (minor; high confidence), `銅.md:27`: «переносят на себя сокращение» is an unreadable calque of EN "do not all
  inherit". Remedy: «Не каждое из этих чтений, которыми называют металл, относится и к сокращению «медаль».» Evidence:
  JMdict's restriction of sense 2 to どう.
- C7 (minor; high confidence), `仕上がる.md:19`: «должна быть готова» adds obligation to 予定です. Remedy: «Эта картина, по
  плану, будет готова к завтрашнему дню.» Evidence: the Japanese example; JMdict 1305130.
- C8 (minor; medium-high confidence), `長引く.md:4,12`: the second title gloss «длиться дольше ожидаемого» makes
  definitional what line 17 calls «Часто». Remedy: title «затягиваться (по времени)». Evidence: Digital Daijisen 長引く.
- C9 (minor; high confidence), `長引く.md:22`: «никак» adds an intensifier absent from 風邪が長引いています and EN. Remedy:
  «Моя простуда долго не проходит.»

Optional: 四角い:18 «прямоугольную коробку» picks one valid shape (line 19 keeps both, so this is not an error); 長男:19 and
長女:19 «Мой/Моя» follow EN's narrative possessors; 鉄砲 «ружьё» is supported by Daijisen and qualified by «(общее
название)»; 整備's «метаданных» and 過程's «путь … на пути» are inherited awkwardness, not lost rules. Outside its facets,
it noted the title overlaps 継続/続き, 長引く/ずるずる/だらだら, 鉄砲/銃, 仕上がる/できる and 鉱物/鉱石. Limits: not a
native-speaker or full-corpus check; comparison cards were not all read in full; Japanese correctness was re-audited only
where it affected the findings. It checked and did not treat as defects «донбури» beside どんぶり, Sanskrit «патра», the
established «темпура», «равно пяти», the contextual «благоустройство», «ржавые» for 錆びている, and the qualified
«восприятие» and «чаша».

## Exclusion classification

All 121 EN exclusion entries (28 lists) are retained in EN order; 錆 and 銅 have none. Seventeen of them lie inside the
batch. At the candidate, three direct, one-sided entries were added on three new cards; none is a new list or targets a
batch word.

| Entries | Consistency reviewer |
|---|---|
| 丼→料理 (1) | real basis; conservative, necessity not established but plausible; keep |
| 過程→途中 (1) | real basis; conservative, plausible for an ordinary quiz; keep |
| 鉢→植木 (1) | real basis only as a topic; conservative and marginal, but harmless; no change required |

丼's rice-dish sense («блюдо из риса с добавками (донбури)») overlaps 料理 «готовка; кухня; блюдо», and 過程 «процесс; ход
развития» overlaps 途中 «по пути; в процессе». 鉢's flowerpot sense is a topic neighbour of 植木 «садовое дерево; растение
в горшке», but a container is not the plant, so the reviewer did not expect a learner to confuse them defensibly. All
three entries are kept. The correctness reviewer noted that the original exclusions are retained with the three
disclosed RU additions, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`230-words-batch-69-recheck-001.md`.
