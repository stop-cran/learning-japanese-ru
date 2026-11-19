# B194 consistency and quiz-safety review (batch `194-words-batch-33`)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `6947a60b9c7d3731fd7f76d426d5721db87c55ee` (tree `b3d62aa2c27ac5821b90274487ade692874be11f`),
> the signed candidate pushed before review.
> Later reconciliation is in `194-words-batch-33-recheck-001.md`.

Snapshot: RU `6947a60b9c7d3731fd7f76d426d5721db87c55ee` on `full-ru-194-words-33`, parent `afec4b7`; working tree clean (`git status --short` empty before and after running the validators). Frozen EN `6af98cb` as source.
Scope: all 30 new `words/*.md` cards read in full against their EN originals; 12 navigation-only restorations (diffed line by line); `manifest.json`; `docs/translation-batches/194-words-batch-33-intake.json` (structure and hashes only). Facets: consistency, quiz safety, scoped cross-file coverage. Blind: no author report, title-screen output, prior reviewer report or batch/draft/tracking record was read (I re-ran `word_title_screen.py` myself as a lead). Reviewer model: not verifiable from inside this session.
Checks run: `tools/validate.py` -> 0 errors; `tools/build_manifest.py` left the tree clean (manifest is current, 3939 files); `tools/check_content_budget.py` OK (3947 files / 11.1 MB retained). Own scripts (in FILES, not committed): front-matter parity vs EN (every key except title/quiz_exclusions identical for all 30), heading and example-bullet counts equal EN, every EN exclusion retained, all exclusion targets exist as RU cards, link parity vs EN, reverse link scan of all EN words/kanji/articles/strokes for links to the 30 new words, exact title-segment collision scan against all RU titles, intake `candidateRawSha256` = file bytes for all 42 payloads and `sourceRawSha256` = EN bytes.

Verdicts:
- Consistency: CLEAN
- Quiz safety: NEEDS FIX (two Minor missing guards, F1 and F2; no Major/blocking defect)
- Scoped coverage (cross-file integration): CLEAN

Findings:
- F1; Minor; quiz safety; `words/見事.md` front matter line 10; `見事` («замечательный; восхитительный», JMdict 1259620 sense 1 "splendid; magnificent; admirable; superb") is a defensible correct answer for `凄い` («потрясающий; невероятный», sense "amazing; wonderful; great") and vice versa, yet no pair exists. `凄い` already guards its praise neighbours (すばらしい, 立派, 優秀, 偉大, 大した, 結構…), and `見事` already guards the same neighbours (すばらしい, 立派, 偉い, 感心, 優秀, 上等), so `見事` is the one praise adjective in this cluster left unpaired with `凄い`. Remedy: replace line 10 with `quiz_exclusions: [すばらしい, 立派, 偉い, 感心, 優秀, 上等, 凄い]` (one side suffices; the app applies it symmetrically; this keeps all six EN entries). Evidence: `words/凄い.md` title/exclusions, `words/見事.md` body "хвалит что-либо как великолепное, превосходное"; pool precedent すばらしい↔凄い. Confidence: medium (Russian glosses are near-synonyms; "обычно 凄い" register difference could be argued, so this is an edge).
- F2; Minor; quiz safety; `words/解決.md` line 10; the card teaches `解決する` as «решать что-либо» / «разрешаться» (body, lines 15–16), which is the same Russian verb as the title of `決める` («решать; определять»), and the batch already treats that overlap as quiz-ambiguous (`解く` → `決める`; `解ける` → `決まる`). `解決` declares `答, 決定, 解く, 解ける` but neither `決める` nor `決まる`. JMdict 解決 1198960 sense 1 "settlement; solution; resolution" vs 決める "to decide; to determine", so the basis is the Russian rendering «решать», not the Japanese sense; this is therefore a consistency gap with the batch's own guards rather than a hard error. Remedy: replace line 10 with `quiz_exclusions: [答, 決定, 解く, 解ける, 決める]`; `決まる` optional (see below). Confidence: low-to-medium.

Exclusions beyond the EN file (all targets exist; all EN exclusions are retained everywhere):
| Card → target | Dictionary basis | Classification |
|---|---|---|
| 解決 → 決定 | 決定 «решение; постановление» — same Russian word «решение» as 解決's title; 決定 1 "decision; determination" | required |
| 解決 → 解く, 解ける | 解く 3 "to solve", 解ける 2 "be solved": same family, titles «решать (задачу)» / «решаться (о задаче)» | required (sense-sharing family; one side suffices, declared on 解決 and on 解ける) |
| 解ける → 解く | 解く 1/3 vs 解ける 1–2, intransitive/transitive pair, body contrasts them | required |
| 解ける → 決まる | 決まる "to be decided" vs 解ける 2 "be solved"; only Russian «решаться» / «быть решённым» overlap | conservative |
| 解く → 決める | 決める "to decide" vs 解く 3 "to solve"; basis is the shared Russian «решать» | conservative |
| 覚ます → 起す | 起す «будить» is exactly 覚ます's first title segment; 覚ます 1 "to awaken" | required |
| 見舞い → 訪問 | 訪問 «визит; посещение» vs 見舞い «визит к больному»; 見舞い 1 "visiting someone ill"; `訪問` already declares お見舞い | required |
| 見舞い → 訪ねる, 伺う | 訪ねる 1 "to visit", 伺う 1 "to visit (humble)"; mirrors `お見舞い` which declares exactly these two | conservative (follows the pool's お見舞い precedent) |
| 偉い → 立派 | 立派 «впечатляющий; достойный» vs 偉い «достойный похвалы»; 立派 1 "splendid; fine", 偉い 1 "admirable"; EN 偉い body names 立派 as the contrast | required |
| 偉い → 感心 | 感心 «восхищение; похвальный» vs «достойный похвалы»; 感心 (adj-na) "admirable; praiseworthy" | required |
| 偉い → 偉大 | 偉大 "great; grand" vs 偉い 1 "great; eminent"; 偉い 人 ≈ 偉大な人; EN 偉い body names 偉大 | required-leaning (real basis; titles «великий; выдающийся» vs «высокопоставленный») |
| 偉い → 優秀 | 優秀 "excellent; superior" vs 偉い "admirable"; topical praise relation, no title segment shared | conservative (necessity unestablished; harmless) |
| 偉い → 大した | 大した 1 "considerable; great" vs 偉い 2 "important/eminent"; «выдающийся» vs «высокопоставленный» | conservative (necessity unestablished; harmless) |
| 上等 → すばらしい | すばらしい "wonderful; splendid" vs 上等 2 "fine; good; excellent"; Russian «превосходный» vs «прекрасный; великолепный» | conservative (real basis; EN guarded 上等→優秀 on the same ground) |
| 製品 → 品物 | 品物 "goods; article" vs 製品 "manufactured goods"; «вещь; товар» vs «изделие; продукция»; precedent 食料品→品物 | conservative |
| 被る → 着る, 履く | 着る 1 "to wear (upper body)", 履く 1 "to wear (lower body)", 被る 1 "to put on (head)": all «надевать»; 着る/履く already guard each other | required (shared verb «надевать» in all three titles) |
| 要素 → 部分 | 部分 "part; portion" vs 要素 "component; element"; «составляющая» ≈ «часть» | conservative |
| 要点 → 中心 | 中心 «…главная часть» vs 要点 «главное»; 要点 1 "main point; gist" vs 中心 "center; core" | conservative |
| 親友 → 友人, 友達, 友 | 友人/友達 "friend", 友 "friend; companion": 親友 is a kind of friend and every title contains «друг» | required (友達/友人 titles «друг» ⊂ 親友 «близкий друг») |
None is unjustified (none guards an antonym or contrast the article itself teaches, or a purely topical relation without a lexical hook), apart from 偉い→優秀 / 偉い→大した, which sit at the weak end of "conservative" and cost nothing; no removal is recommended.

Checked and found no guard needed (judgement calls, so listed for the requester): 解く↔結ぶ and 解ける↔溶ける (antonym/homophone taught in articles, targets absent); 観察/観光 vs 見物 (guarded: «наблюдение…», «осмотр достопримечательностей»); 観客 vs 客, 選手; 覚める/覚ます vs 起きる, 寝る, 眠る, 酔う, 覚える; 覚悟 vs 準備/諦める/決める/備える/できる (titles «готовность…решимость» vs noun «подготовка»/verbs; EN left the same English "preparedness" overlap unguarded, so no RU-specific tightening); 見解 vs 意見/説 (guarded), 点; 覆う vs 隠す (guarded), 隠れる, 包む (article teaches the contrast; EN unguarded), 被る; 要するに ↔ すなわち (つまり overlaps both, but 要するに «если коротко» vs すなわち «то есть» are not defensible substitutes; exclusions are direct, not transitive); つまり/すなわち vs 言わば, 例えば; 裸 vs 脱ぐ/服; 裏切る vs 裏 («предавать» vs «изнанка»); 裁判 vs 訴える («подавать в суд» is a different act), 判断, 決定, 法律; 害 vs 障害, 怪我; 被害 vs 事故, 怪我 (card itself contrasts 怪我); 袖 vs シャツ/上着; 袋 vs 手袋, ビニール, 箱, プラン («пакет услуг» ≠ «пакет»); 上等 vs 質/高価 (adjective vs noun / quality vs price). Exact title-segment scan found only three collisions, all guarded (観光/見物 «осмотр достопримечательностей», 覚ます/起す «будить», 上等/優秀 «превосходный»).

Consistency detail (all clean): front matter keys, order, `jlpt`, `type`, `kanji`, `tags` equal EN for all 30; titles/headings are Russian and follow the existing RU convention; no Latin-letter romanization; same heading and example counts as EN; every kana reading present. Links: RU links equal EN links except where the EN target is absent in RU (溶ける, 結ぶ, 俳優, 仲間, 決心, 考え, 最高, 全体, メモ, 商品, 信頼, 犯罪, 損害, 被せる, 衣服 and kanji 裏, 被, 袋 — all verified missing, so plain text is correct); no RU-only link. Reverse scan: every EN link to a new word from an existing RU file is restored (the twelve files); the remaining reverse hits are EN files that do not exist in RU, and 手袋→袋 is an EN kanji-page link to a missing page. Navigation-only diffs change only bracket/href at EN link positions (no prose change) — 3+3+3+3 in 偉/害/察/観, one each in the eight word files; the ビニール, 上, 偉大, 友人, 親しい, 言わば, 訪問, すばらしい links point to existing sibling files. Manifest: regenerated, no stale hash, no unrelated or generated files in the commit; intake payload hashes match the files and EN sources (42 payloads).

Optional:
- 解決 → 決まる (see F2): add only if 決まる is judged ambiguous with 解決する «разрешаться»; low confidence.
- 親友 vs 親しい («близкий» / «близкий друг», body of both cards contrasts them): unguarded in EN as well; a quiz-taker would not defensibly pick the adjective for the noun, so no action needed. Add 親しい only if you want symmetrical caution.
- 被る body (last paragraph) quotes the English gloss «to suffer» and "исходный список слов"; it mirrors the EN card but is jargon for a Russian reader — comprehensibility facet, not mine.

Limits: Quiz-ambiguity judgements rest on Russian titles and JMdict senses as I know them; I did not re-fetch JMdict entries online, and "defensible answer" is a judgement, hence F1/F2 are Minor with stated confidence. Did not verify Android `Words.kt` in this session (contract taken from the review prompt). Did not review linguistic correctness or comprehensibility (other facets). Batch records, ledger, progress and tracking JSON were not inspected by instruction.
