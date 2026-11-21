# B232 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `56da736ec2499c2e67dc01cd65078098c31e2716` (tree `e27c0b79e91de862b493efe3dffbc9683aa33060`),
> the signed candidate pushed before review.
> Later reconciliation is in `232-words-batch-71-recheck-001.md`.

Snapshot: RU `56da736ec2499c2e67dc01cd65078098c31e2716` (branch `full-ru-232-words-71`); `git rev-parse HEAD` matched, `git status --porcelain` empty (no uncommitted changes). Frozen EN `6af98cb`.

Scope: Read in full (front matter + body) all 30 new cards `words/` 部首 原料 成分 部品 郡 裏返す お帰り 返る 遡る 遠足 対策 方角 方針 地帯 角度 方面 道順 過失 過半数 余る 超過 過剰 遊園地 逸れる 統一 連合 作製 作成 製作 造船, and the full diffs of `kanji/余.md`, `kanji/帯.md`, `words/余分.md`. Programmatic checks against frozen EN: front matter (all keys but `title`), link multiset per card, link-target existence, exclusion lists (order and additions), `link_parity.py`, `tools/validate.py` (0 errors), SHA-256 of every `manifest.json` entry (5074 entries, 0 stale/missing), intake record paths/candidate hashes vs the diff (33 payload paths = 33 content files, all hashes match, no learner content). Quiz screening of every batch title against all 3613 RU word titles (own segment/whole-word script plus `word_title_screen.py` segment hits) and a keyword grep of RU titles. Model: not verifiable from inside the session. No dictionary lookups were performed for this facet (see Limits). Did not read author reports, batch records, drafts or tracking.

Verdicts:
- Consistency (format, terminology, links, navigation-only files, manifest, intake): CLEAN
- Quiz safety (EN guards retained, RU-introduced guards, gaps): CLEAN
- Scoped coverage of cross-file integration (reciprocal/EN-position links, plain-text pointers): CLEAN

Findings: none actionable. No defect established; no manufactured findings.

Evidence per check:
1. EN guards: for all 27 cards that have EN `quiz_exclusions`, the RU list equals the EN list in EN order, with additions only appended at the end (方針 +線, 角度 +角, 方面 +球, 作成 +建設, 製作 +作製; 余る new key with 残る, 余分). 部首 and 遊園地 have no key, as in EN. Every pair in the prompt's must-stay list is present (checked by exact list equality, not by sampling).
2. Front matter: no difference from EN except `title` (Russian) and the guard additions above. All tags/type/kanji/jlpt equal EN.
3. Links: no RU link lost relative to EN where the RU target exists. Differences from EN: removed (target absent, text kept as plain, nothing dropped): 資料, kanji/裏, いってらっしゃい, article kaeru-change-replace-and-return, kanji/角 (方角, 角度), kanji/針, kanji/順, kanji/超, 娯楽, 制作, kanji/造. Added (all targets exist, all accurate): 郡→市/町/村, 地帯→帯, 余る→残る/足りる. No broken link in any new card.
4. Navigation files: byte-identical apart from link brackets/hrefs. 余.md lines 21, 37, 50 = EN positions (prose, あま.る row, word list); 帯.md lines 28, 39 = EN positions (タイ row, word list), 包帯 correctly left plain (no RU card); 余分.md line 28 = EN position (`余る.md`, word-file form kept). No other 余る/地帯 mention in these files left plain that EN links. Path forms match EN.
5. Manifest hashes verified for every entry; contentVersion changed; no generated/unrelated files in the diff (35 files: 30 cards + 3 nav + manifest + intake).

RU-introduced guards (seven):
- 製作→作製: REQUIRED. Titles share «изготовление» (作製 «изготовление (модели, образца, чертежа)», 製作 «…; изготовление (вещей)»); EN titles identical and unguarded. A learner asked either could defend the other.
- 余る→残る: REQUIRED. 残る title «оставаться» is the whole prefix of 余る «оставаться лишним…»; a learner choosing «оставаться» for 余る (JMdict 余る sense 1 "to remain; to be left over") is defensible.
- 余る→余分: CONSERVATIVE. Real basis: «лишним» in 余る vs 余分 «излишек; лишний» (same root idea, JMdict 余分 "extra; surplus"); necessity unestablished because POS/gloss differ (verb vs noun/adjective).
- 角度→角: CONSERVATIVE. Real basis: 角度 senses "angle" vs 角 «угол»; 角 card title is exactly «угол», 角度 «величина угла»; necessity in a quiz not established but plausible.
- 方針→線: CONSERVATIVE. Shared whole word «линия» in 方針 «линия (организации, руководства)» and 線 «линия; провод»; senses differ (abstract policy vs physical line), so necessity unestablished; harmless.
- 方面→球: CONSERVATIVE. Shared «сфера» in 方面 «сфера, область (деятельности)» vs 球 «сфера; мяч»; Russian homonymy, senses differ; harmless.
- 作成→建設: CONSERVATIVE. Shared «создание» (作成 «создание (файла, учётной записи)» vs 建設 «строительство; создание»); the qualifiers separate them; harmless.
All seven are one-sided; the app applies pairs symmetrically, so one side suffices (also for the one-way EN in-batch pairs). None is unjustified (no antonym/contrast or mere topical guard). The title-based pairs I would otherwise have flagged are all covered by EN or RU guards.

Declined/untouched pairs judged from titles: 原料–部品, 部首–部品, 遠足–遊園地, 方角–角度, 方針–方面, 方針–道順, 地帯–道順, 過半数–超過/過剰/余る, 過失–過剰, 統一–作成, 作成–造船: distinct titles, no guard needed. 部首–漢字/字, 原料–製品, 郡–国/町, 裏返す–裏/表/変える, 遡る–流れ/過去/歴史/昔, 遠足–ドライブ, 遊園地–公園/乗り物/遊び, 対策–防ぐ/抵抗/解決, 方針–指導, 方角–角/どちら, 過失–違反/責任/罪, 過半数–半分 («больше половины» vs «половина» is explicit), 余る–残り/残す/余裕/あまり, 逸れる–断る/異常/狂う/迷子, 作製–設計/図: acceptable unguarded. 統一–会/組合: 統一 «объединение в одно целое…» shares only the word «объединение» with 会 «встреча; объединение» and 組合 «объединение по интересам; профсоюз»; qualifiers separate them (EN also unguarded) — acceptable.
Titles: 方針, 方面, 作成 fit their senses. 作製 (модель, образец, чертёж), 作成 (документ, учётная запись) and 製作 (мебель, фильмы, вещи) are distinguishable by their parenthetical qualifiers; 方針 «курс действий» stays distinct from コース «маршрут; курс (обучения)» and 針路 «курс (судна…)» (both guarded). 部首 vs 鍵 «ключ»: see Optional.

Optional:
- O1 (very low): 部首 «ключ иероглифа…» and 鍵 «ключ» share «ключ»; a Russian speaker could weigh «ключ» as a loose answer for 部首. Qualifier makes 部首's title unambiguous for a careful learner, EN had no guard. If the owner wants maximum caution add `quiz_exclusions: [鍵]` to `words/部首.md` (a new key, so it is a content decision, not required).
- O2 (very low): 方面 «в сторону (какого-либо места)» partially overlaps あちら/そちら «в ту сторону»; demonstrative vs noun; no guard needed.
- O3 (cosmetic): `words/お帰り.md` line 28 mentions 帰る plain although an RU card exists; EN also plain and the mention is incidental, so not a link defect.
- O4 (outside batch): restored line `kanji/余.md:21` keeps the pre-existing bare gloss «оставаться; быть в избытке» beside the card title «оставаться лишним; быть сверх нужного». «оставаться» alone is closer to 残る; the 余る card's 残る comparison and guard handle this, and prose edits are out of this batch's navigation-only scope. `kanji/帯.md` «область; зона» beside «зона (местность с общей особенностью)» is consistent. `words/余分.md` «оставаться, быть в избытке» is consistent.

Limits:
- Dictionary entries/senses were not re-looked-up for this facet; basis statements above rest on the card text, JMdict sense wording as quoted in the cards, and my general knowledge, so necessity classifications of the conservative guards are judgments, not verified frequencies.
- Existing EN cards that exclude batch words (e.g. 余計, 制作, 脱線) have no RU file, so no RU retention question arose.
- Translation accuracy of Russian prose against EN was not line-reviewed (correctness/comprehension are other facets); structure, links, exclusions and titles were.
- The title screen for stem-only hits was heuristic; I inspected whole-segment/whole-word overlaps against all RU titles and a keyword grep, not every stem pair (~431 reported by the author).
