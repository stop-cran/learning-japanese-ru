# Batch 243 — independent review 001

## Snapshot and scope

- Reviewed commit: `73cef33b421a2937376b84f06ad0c9908bc93346` (tree `0dc620083dfbf22c3f2b5550ecb4b76d3ebcbe2e`), branch
  `full-ru-243-words-82`, parent `bf6220b`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the commit `eec3d2d046168133818aba86f5bccd18f80a2542`, which holds
    the Batch 241 and Batch 242 lane drafts on the Batch 240 fix `3544d75` (scratch commit
    `556daa95a6abb058dbe62e1af26fe523a834d14b`). Before copying, the coordinator's candidate script checked that the ten
    navigation files edited there were unchanged between `eec3d2d` and the candidate's parent `bf6220b`, and that none of
    the 30 new cards existed in the primary checkout. It also checked that the branch, HEAD and `origin/main` were the
    expected ones and that the tree was clean.
  - The script byte-compared the 40 scratch content files with the primary checkout after copying and again at commit
    time, and checked that the changed path set was exactly the 40 batch paths plus `manifest.json`. Its byte scan of all
    40 content paths prints any BOM, CR or missing final newline rather than stopping; for this record the 40 committed
    blobs at `73cef33` were checked: none has a BOM or CR, and every file ends with a newline, as `.gitattributes`
    requires.
  - No link was held from an earlier batch; all ten navigation files were copied from the authoring worktree.
  - After authoring and before the candidate commit, the coordinator made no content edit; the 40 lane files were copied
    unchanged. Its adjudication record states:
    - "No coordinator text edits were needed; the lane is adopted as authored.";
    - "Screens rerun by the coordinator with RU_ROOT = lane: `validate.py` 0 errors; the changed-path set is exactly 40
      paths (30 new cards + 10 restoration files, `b243-lane-paths.txt`) plus manifest.json.";
    - "`navonly.py HEAD --only <10 files>`: 10 files, 12 links added, 0 problems (傾:31/40 → 傾く, 再:30/38 → 再三, 物:40 →
      編物, ぞくぞく:26 → 続々, ペンキ:28 → 絵の具, 井戸:39 → 緯度, 繋ぐ:35 → 接続, 缶:35 → 缶詰, 赤道:33 → 緯度, 首相:33 →
      総理大臣 with 内閣 left outside the link).";
    - "Navigation completeness: a scan of every RU words/kanji/articles file outside the batch finds 0 EN links to the 30
      B243 words that the RU file lacks.";
    - `link_parity.py`: "no LOST; two RU-only EXTRA links, both accepted under the B214 rule (EN mentions the word as plain
      text in a substantive comparison and the card exists in this batch): words/編む.md:34 → 編集, words/編物.md:34 →
      縫う.";
    - a dependency note: "no B243 card links to any B241 or B242 word, so the candidate depends only on published content.
      Because B241/B242 titles may still change in review, the title screen for the 30 words is rerun on the published
      B242 tree before the B243 candidate commit (the author's adjudications of 敷く in 絨毯, 脱線 vs 線路 and 育児 vs 美容
      are rechecked then).";
    - `word_title_screen.py` over the 30 words (`b243-screen.txt`, 205 lines, "identical to the author's final run"): "one
      exact segment hit, 繋がり/パイプ «связи», guarded. The remaining 204 lines are stem-only (29 guarded OK, 175
      unguarded) and were reviewed with the author's declined-pairs list; coordinator spot checks agree (generic stems
      «поезд», «прави», «друго», «перес», «начал», «рисов», «данны»; qualifier-only 傾く/緩い~坂/急 «(о склоне)»,
      編集~映画/ビデオ «(фильма, видео)»).";
    - "Titles compared with EN one by one (`b243_cmp.py`). Every EN `quiz_exclusions` entry is retained in EN order; RU
      additions are appended.";
    - "RU-added exclusions: 9 pairs on 8 cards, all conservative, none required — 群れ→混雑 («толпа»/«давка; скопление
      людей»), 缶詰→滞在 («пребывание»), 繋がり→パイプ/付き合い, 編物→製品 («изделие»), 総理大臣→政府, くれぐれも→要求
      («настойчивая просьба»), 始終→飽くまで («до конца»), 絶えず→継続 («непрерывн-»). Accepted as harmless direct pairs,
      consistent with earlier batches.";
    - "**Declined: 再三~また «снова и снова» / «снова; также».** EN "again and again; repeatedly" / "again" shares the same
      overlap unguarded, and the RU titles do not introduce it (same basis as the B242 おかけください decision). Left to the
      blind review.";
    - "総理大臣~大臣 «министр (член кабинета)» stays unguarded (EN prime minister/minister, unguarded); 首相 is guarded from
      EN.";
    - "Russian check (Kuznetsov, gramota.ru, «туго»): «Т. схватывать, понимать что-л.» supports colloquial «туго
      соображающий» (のろい). Other Russian vocabulary is ordinary and not dictionary-checked here.";
    - author deviations accepted: "美容 «косметические процедуры» (instead of the lead «наведение красоты»); 繋げる
      «подсоединять» (instead of «сцеплять»); Russian notes replacing English-dependent remarks in 線路 («путь»), 絵の具
      («краска») and 編集 («редакционный»); dropped English-only notes in 統計 ("scattering") and 編物 ("web").";
    - left to the blind review: 緩い's title «слабо затянутый», "narrower than EN "loose""; 総理大臣's title «глава
      правительства (премьер-министр)», which "puts the core gloss in parentheses"; and the "Naturalness of «пребывание
      взаперти» (缶詰 sense 2), «связывать воедино» (繋げる), «сковывать (свободу)» (縛る), «сбор статистических данных»
      (統計), and the conservative guards above.";
    - "Missing kanji (plain, no link): 群 毛 缶 詰 接 鈍 編 線 総 臣; unavailable words left plain: 毛皮, 火口, 片寄る, 社説."

    The committed manifest records 5,409 entries (5,404 `files`, 3 images and 2 scenes); the coordinator's lane
    `validate.py` run and its phase-1 `tools/validate.py` run on the candidate content reported 0 errors. The
    correctness and consistency reviewers also ran the validator on the candidate (0 errors).
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 10 files with 12 restored navigation links (the kanji cards 傾, 再 and 物 and the word cards ぞくぞく, ペンキ, 井戸,
      繋ぐ, 缶, 赤道 and 首相);
    - `manifest.json` (`contentVersion` `1cd2bb5be75b134a`, 5,409 entries);
    - the intake, whose note reads "B243 30-card adaptation with twelve navigation-only link restorations in ten existing
      files; candidate before blind review."

    Against the published baseline the candidate changes 43 files (1,757 insertions, 23 deletions), including the
    parent's publication record; the candidate commit itself changes 42 files.
- Published baseline recorded in the intake: `c5e702d13aac04c7e2a4645c299f80886df79df9` (Batch 242 merge, PR #126).
  Parent `bf6220b` adds only the Batch 242 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 script, which stops on a failing validation, unit-test, budget,
  whitespace or navigation-only check, passed:
  - `tools/validate.py`;
  - unit tests;
  - content budget;
  - `git diff --check`;
  - navigation-only check on the 10 files (12 links added, no other change).

  It also printed two results without a stop condition, recorded here as observed:
  - title screen (`b243-cand-screen.txt`, 205 lines, identical to the lane screen): 30 `OK` lines for pairs already
    guarded by an exclusion and 175 `!!` lines, all stem-only; the one exact-segment line, 繋がり–パイプ «связи», is an `OK`
    line;
  - link parity: only the two adjudicated RU-only EXTRA links, `words/編む.md` → 編集 and `words/編物.md` → 縫う; no LOST
    link. For this record link parity was verified again at `6aa1bca`: no LOST link, and EXTRA only for those two links
    and the two reviewed RU-only links added by fix 1 (`words/繋がる.md` → 切れる, `words/繋ぐ.md` → 繋がる).
- Common sample: all three reviewers read all 30 new word cards in full against their complete frozen EN originals. The
  correctness reviewer also inspected the ten navigation changes ("this is changed-line coverage, not a full-card
  attestation for those files"); the consistency reviewer read all ten navigation diffs in full (`-U0` diffs) and
  checked the intake record (path list only); the comprehensibility reviewer "Also read the one-line link edits in the
  same commit" and the comparison titles needed for quiz collisions.
- Correctness review scope:
  - "Model identifier not independently verifiable. The following attests actual full reading of each RU file AND its
    entire corresponding frozen EN original (not merely its title or diff)", followed by the 30 cards, each "full /
    full".
  - Inspected actual Jisho/JMdict, Digital Daijisen (weblio), Russian Wiktionary and Gramota/Kuznetsov entries;
    "Kanjiapi corroborated compound readings, not word JLPT or phonetic origins."
  - "Read-only validator: python -X utf8 -B tools/validate.py, 0 error(s). Final recheck: HEAD/branch unchanged, status
    --porcelain empty, cached diff empty (exit 0). Only this report was written."
- Consistency review scope:
  - "Read in full (front matter and body): all 30 new cards". "All ten navigation diffs read in full (`-U0` diffs of
    kanji/傾, kanji/再, kanji/物, words/ぞくぞく, ペンキ, 井戸, 繋ぐ, 缶, 赤道, 首相). Intake JSON checked for path list
    only."
  - "Machine checks run on the working tree: validate.py (0 errors); EN-frozen vs RU front matter/links/exclusions for
    all 30; link label/target existence for the 30 cards plus the 10 nav files; EN-link-to-batch-word parity across every
    file that exists in both repos; in-memory manifest rebuild; Russian-title screening of each batch word against all RU
    titles".
  - "Fidelity to the EN text and Russian linguistic quality are other reviewers' facets and were not judged."
- Comprehensibility review scope:
  - "comprehensibility and scoped coverage of batch 243. Read in full, each against its frozen EN original", followed by
    the 30 cards, plus the link edits and the comparison titles of パイプ, 次々, ウール, 育児, 敷く, 結ぶ, 関係, 遅い, 鈍い, 鉄道,
    化粧, 滞在 and 毛.
  - Its limits record that "JMdictDB live lookup was password-gated; senses are taken from the cards' cited entry IDs,
    the frozen EN articles, and the public glosses named above" and that title-screen stem hits were not treated as
    collisions. It records no validator or generator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  These are the model variants the coordinator assigned at launch (agents `c8178185-ccd4-4add-96db-b07cf8de4ff1`,
  `a772e7f5-efcb-43d8-bb96-455ac130885b` and `89526504-ed23-4489-9001-af85b71cd898`, as shown in the runtime agent
  listing). Reviewer prose did not expose a lower-level serving identifier; the correctness report says "Model
  identifier not independently verifiable.", the consistency report "Model: not verifiable by me.", and the
  comprehensibility report "Model: not verifiable."
- Reviews ran serially, one reviewer at a time: correctness, then consistency, then comprehensibility. This ordering
  rests on the coordinator's session records (each reviewer launched after the previous one finished); the reports
  themselves do not record times. The correctness report records "HEAD matched and git status --porcelain was empty at
  initial inspection" and, at its final recheck, "HEAD/branch unchanged, status --porcelain empty"; the consistency
  report records `git rev-parse HEAD` = `73cef33` and an empty `git status --porcelain` "at start and at end", and that
  the untracked Python bytecode cache created by `tools/validate.py` was deleted, "so the tree is clean again"; the
  comprehensibility report records "`git status --porcelain` empty; no uncommitted changes." No fix was applied until all
  three reports were complete.
- All three launch briefs forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The correctness report says "No repository edits, staging, commits, checkouts or generators."
  and "Only this report was written."; the consistency report says "No tracked file was touched, no generator was run;
  the manifest was recomputed in memory only."; the comprehensibility report says "No file in the repository was
  edited." No reviewer reported changing a tracked repository file.
- Full blind reports:
  - `243-words-batch-82-review-correctness-001.md`
  - `243-words-batch-82-review-consistency-001.md`
  - `243-words-batch-82-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - any author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  As in earlier batches, the consistency brief made one exception: the intake record, for its path check. The
  consistency report records "Intake JSON checked for path list only." The correctness report states
  "Publication/draft records and other reviewers' materials were not read."; the comprehensibility report states
  "Author reports, other reviewers, and docs/translation-batches were not read."

## Initial verdicts and findings

### Correctness

Verdicts: "CORRECTNESS: NEEDS FIX — C01, C02, C06." "SCOPED COVERAGE: NEEDS FIX — C03, C04, C05." "No additional
actionable defect established in the other sampled cards. Specific source-verification exceptions: 絨毯's search-only
spelling assertion and 接続's Russian train-connection wording remain UNVERIFIED as described under Limits; these are not
CLEAN certifications."

- C01 (medium; correctness; high confidence), `words/編物.md:20`: «Я неделю довязывал своё вязанье» "states an
  ongoing/process activity without asserting completion. 一週間かけて編み物を仕上げました explicitly reports finishing the
  work". Evidence: Digital Daijisen 仕上げる sense 1; frozen EN "finished". Remedy: «Я за неделю закончил вязать
  изделие.»
- C02 (medium; correctness; high), `words/絵の具.md:20`: «Я взял немного красной краски» "asserts taking/selecting paint,
  whereas 赤い絵の具を少し使いました asserts using it." Evidence: Digital Daijisen 使う sense 2; frozen EN "used". Remedy: «Я
  использовал немного красной краски.»
- C03 (medium; scoped coverage; high), `words/緩い.md:4,12,16–18`: «Слабо затянутый» and the opening definition "omit the
  loose-fit sense: shoes/clothing may fit loosely without being badly tightened." Evidence: Digital Daijisen ゆるい sense
  1 (くつがゆるい); frozen EN:16–18 and 42–43. Remedy: add a qualified loose-fit gloss to the title and heading and a
  loose-fit sentence to the definition.
- C04 (medium; scoped coverage; high), `words/編集.md:4,12`: "The EN title's “compilation” is replaced by video montage
  rather than retained." Evidence: frozen EN 編集:4,12,16; JMdict 1603240 sense 1. Remedy: «редактирование; составление
  сборника; монтаж (фильма, видео)».
- C05 (medium; scoped coverage; high), `words/くれぐれも.md:4,12`: «Настоятельно; убедительно (о просьбе)» "gives two
  insistence glosses and drops EN “repeatedly.”" Evidence: frozen EN くれぐれも:4,12,23–24; JMdict 1269140 sense 2.
  Remedy: «настоятельно; снова и снова».
- C06 (medium; correctness; high), `words/緩い.md:50–51`: «Отдельное слово ぬるい “тепловатый” тоже можно записать как 緩い»
  "attaches the alternative spelling to the temperature gloss without its sense restriction", an overbroad association
  "inherited from EN:54–55". Evidence: JMdict 1183300 ("usu. written as 緩い" under sense 2); Digital Daijisen ぬるい
  (「緩い」とも書く under sense 2). Remedy: limit the 緩い spelling to the "нестрогий" sense.

What the reviewer confirmed: metadata parity and retained exclusions ("RU adds quiz guards; no original guard
removed"); retained Japanese example sentences and kana reading tokens; "Every actual card-link target checked exists";
"Exactly two added card links without EN link counterparts, 編む→編集 and 編物→縫う, connect existing cards in substantive
comparisons and are appropriate."; dictionary support for qualified «некрутой», «туго соображающий», «монтаж»,
«наискосок», «беспрестанно», «чередой», «воедино», «взаперти», «сковывать» and a carpet runner as a carpet subtype.

Optional: "Outside these facets, clarify the target of 美容's figure warning and 傾く's weakening/refusing contrast,
remove absent-kanji-card references, and introduce technical reading terminology." Limits: 絨氈's search-only
restriction "was not" visible "and JMdictDB required authentication"; 接続's «стыковка поездов» "Naturalness remains
unverified, not an established false translation"; "Exact Russian terminology «онные чтения» remains independently
unverified; no contrary evidence found"; "JLPT labels match EN; no fresh full recalculation"; "Automatic fallback/answer
uniqueness not exercised or certified".

### Consistency and quiz safety

Verdicts: consistency (format, front matter, terminology, links, navigation-only files, manifest, no stray files)
**CLEAN**; quiz safety **NEEDS FIX** ("two low-severity missing direct guards, F1 and F2; all EN exclusions retained;
every RU-introduced guard has a real basis"); cross-file integration / coverage of the ten navigation restorations
**CLEAN**. The report gives no separate scoped-coverage verdict.

- F1 (low; quiz safety; medium confidence), `words/繋がり.md:9`: 交際 «социальные контакты; романтические отношения» is
  not guarded; "The batch already guards the sibling people-relations words 仲, 付き合い and パイプ against 繋がり; 交際 is
  the same cluster but was missed." Remedy: append 交際.
- F2 (low; quiz safety; medium), `words/編集.md:9`: 修正 «исправление; правка» is not guarded; "In Russian «правка» is the
  ordinary rendering of "editing"". Remedy: `quiz_exclusions: [編む, 修正]`.

What the reviewer confirmed: every relative link resolves and every label equals its target stem; EN links whose RU
target is absent stay plain; "the only link differences against EN involving batch words are the two RU-added ones
above (編む→編集, 編物→縫う). No missed restoration anywhere"; the ten navigation files carry "exactly 12 link
occurrences, at the stated lines …, only brackets/hrefs changed, no prose change"; "Adjacent glosses do not mislead
beside the new titles."; the in-memory manifest rebuild equals the committed `manifest.json` (contentVersion
`1cd2bb5be75b134a`); the intake's 40 payload paths are exactly the content diff, `held` is empty and it adds no learner
content. The report also says "42 files changed in total", which matches the candidate commit's own diff against its
parent `bf6220b`.

Optional: 下降→下げる "Consider adding … low confidence, not required"; 作成 for 編集 "together with F2. Low confidence";
the RU-only links 編む→編集 and 編物→縫う "allowed …, no action". Limits: "Dictionary evidence is from my knowledge of
JMdict/Daijisen senses (and the cards' own cited entry numbers), not fresh lookups"; "Translation fidelity to EN and
Russian prose quality … were not assessed in this facet."; the manifest equality is an in-memory comparison.

### Comprehensibility and scoped coverage

Verdicts: "Comprehensibility NEEDS FIX (defects below; the other in-scope cards are clean on this facet). Scoped coverage
CLEAN."

- C1 (medium; high confidence), `のろい.md:4` and `:20`: «неповоротливый» and «Эта машина неповоротлива» teach
  clumsiness; :21 «Он медленно реагирует» uses 遅い's gloss. Remedy: «вялый; туго соображающий»; «Эта машина движется
  вяло.»; «Реакция у него вялая.»; drop «неповоротливость» from the 遅い contrast.
- C2 (medium; high), `傾く.md:43`: the weaken/refuse contrast exists only because English "decline" means both. Remedy:
  «В примере с компанией речь об упадке дел, а не об отказе: отказ передаёт [断る](断る.md)（ことわる）.»
- C3 (medium; high), `繋がり.md:4`: «связи (с людьми)» reuses «связи» from パイプ. Remedy: «взаимосвязь; узы».
- C4 (medium; high), `絨毯.md:4`: «ковровая дорожка» promotes a subtype and drops «коврик». Remedy: «ковёр; коврик».
- C5 (medium; high), `美容.md:4` and `:41`: «косметические процедуры» is a clinical narrowing, and the figure warning has
  no target. Remedy: «уход за внешностью; наведение красоты»; delete the figure sentence.
- C6 (low; high), `線路.md:20`: «железной дорогой» is 鉄道's title. Remedy: «Я живу рядом с железнодорожными путями.»
- C7 (low; high), `なだらか.md:42`: rejects «лёгкий», a gloss the card never shows. Remedy: «Не считайте, что каждый
  なだらかな путь безопасен или не требует усилий.»
- C8 (low; high), `絵の具.md:20`: «взял» changes "used". Remedy: «Я использовал немного красной краски.»
- C9 (low; high), `編物.md:20`: the imperfective «довязывал» need not report completion. Remedy: «Я за неделю довязал
  вязание.»
- C10 (low; high), `繋がる.md:40` and `繋ぐ.md:35`: substantive comparisons leave the existing cards 切れる and 繋がる
  plain. Remedy: `[切れる](切れる.md)（きれる）` and `[繋がる](繋がる.md)（つながる）`.

Optional: 縫う:21 «покрепче»; 繋がり:19 «нашего района»; 絨毯:18 «Мы постелили»; ぞくぞく:26's gloss of 続々 «один за другим»
(次々's title; the line was touched only to add a link); 始終:45 «устаревшими»; the «в этой коллекции нет» notes ("meta but navigational; not a
defect"); 缶詰 «засел» and «стыковка (рейсов, поездов)» judged adequate. Limits: JMdictDB was password-gated; stem hits
"(косме, проце, данны, друго, беспр) were not treated as collisions"; "No file in the repository was edited."

## Exclusion classification

All 169 EN exclusion entries (28 lists; EN has none on 緯度 or 絨毯) are retained in EN order. Fifteen of them lie inside
the batch, and the other 154 target existing RU cards. At the candidate, nine direct, one-sided entries were added on
eight new cards, all appended at the end of their lists; none targets a batch word.

| Entries | Coordinator | Consistency reviewer |
|---|---|---|
| 群れ→混雑 (1) | Conservative | "REQUIRED by parity" |
| 缶詰→滞在 (1) | Conservative («пребывание») | "CONSERVATIVE" |
| 繋がり→パイプ (1) | Conservative | "REQUIRED" |
| 繋がり→付き合い (1) | Conservative | "REQUIRED by parity (CONSERVATIVE at minimum)" |
| 編物→製品 (1) | Conservative («изделие») | "CONSERVATIVE" |
| 総理大臣→政府 (1) | Conservative | "UNJUSTIFIED (harmless, over-restrictive; no fix required; optional removal)" |
| くれぐれも→要求 (1) | Conservative («настойчивая просьба») | "REQUIRED/CONSERVATIVE (real title overlap)" |
| 始終→飽くまで (1) | Conservative («до конца») | "CONSERVATIVE" |
| 絶えず→継続 (1) | Conservative («непрерывн-») | "CONSERVATIVE" |

The coordinator classed all nine as conservative ("all conservative, none required"); the consistency reviewer classed
群れ→混雑, 繋がり→パイプ and 繋がり→付き合い as required, くれぐれも→要求 as required or conservative, and 総理大臣→政府 as
unjustified but harmless; both keep all nine. The consistency reviewer headed its list "all 10 entries", although it
classifies the nine entries above, and added two missing guards (F1, F2). The correctness reviewer raised no exclusion
finding ("RU adds quiz guards; no original guard removed."), and the comprehensibility reviewer's C3 concerned the
繋がり title, which パイプ, 関係 and 付き合い already guard.

Reconciliation, the coordinator's dispositions, the fix and the final verdicts are in
`243-words-batch-82-recheck-001.md`.
