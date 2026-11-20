# B200 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `117374d47cec40b00dcaae3eb8cff40bfba29c1e`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 199 tree `841bc8c` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `200-words-batch-39-recheck-001.md`.

Snapshot: candidate tree 117374d47cec40b00dcaae3eb8cff40bfba29c1e (base 841bc8c), scratch worktree learning-japanese-ru-b198. `git diff-index --cached --quiet <tree>` = 0, `git diff --quiet` = 0, `git ls-files --others --exclude-standard` empty: index and working tree equal the candidate, nothing untracked. No repository writes made (manifest recomputed in memory only).

Scope: 30 new `words/*.md` read in full against frozen EN (6af98cb) front matter/links; 19 navigation-only files (diff inspected); `manifest.json`. Facets: consistency, quiz safety, cross-file integration. Mechanical checks run: `tools/validate.py` -> 0 errors; `build_manifest.build_manifest()` recomputed in memory == committed manifest (4114 entries, contentVersion 19253db6bb19cddf); all `.md` links in words/kanji/articles/strokes resolve (only non-file "broken" hit is an external https URL in 出す.md, pre-existing, not in scope); EN-link parity for all 30 cards; repo-wide check that no EN file links to a new card while its RU counterpart left it unlinked (none). Title overlap screen against all RU word titles done with my own script (stem/segment overlap, not the optional tools). Model: not verifiable by me.

Verdicts:
- Consistency: CLEAN. Front-matter keys and order identical to EN in all 30 cards (only difference is the added `quiz_exclusions` lines noted below). Links: every EN link whose RU target exists is present; the 14 omitted EN-only links all have absent RU targets (報告, 信じる, すみません, ごめんなさい, 就職, ボール, カード, 人生, 地球, 事情, kanji 訳/防/布/瓶/境/玉/象/況) and the prose stays as plain text; no Russian-only links. Navigation-only files change only at link brackets/hrefs (kanji 命/留/疑/表 and the 15 word files; no prose change). Manifest consistent, no stale hash, no stray files.
- Quiz safety: NEEDS FIX (two minor items: F1 missing guard, F2 over-broad guard). All EN exclusions retained (verified per card, see table). No other missing required guard found.
- Scoped coverage of cross-file integration: CLEAN (navigation restorations complete for the new targets; no orphaned plain mentions where EN links).

Findings:
F1; Minor; quiz safety; words/状況.md:11 (quiz_exclusions); 状況 title «положение вещей; совокупность обстоятельств» vs existing 都合 «обстоятельства; удобство» (JMdict 都合 1 "circumstances; conditions", 2 "convenience"). The RU title segment «обстоятельств(а)» makes 都合 a defensible wrong-vs-right answer in either direction; no guard on either side (都合 excludes [便利]; 場合 excludes 都合 as precedent for the same “обстоятельства” overlap). EN does not have it because EN titles are "situation; state of affairs" vs "circumstances; availability", so this is a RU-title-introduced overlap. Remedy: `quiz_exclusions: [状態, 様子, 場合, 都合]` in words/状況.md (then regenerate the manifest). Evidence: titles from front matter of both cards; JMdict senses as above (from memory of the entry, not re-fetched). Confidence: medium (title overlap certain; practical ambiguity moderate).

F2; Minor (trivial learning impact); quiz safety (over-guard); words/玉.md:10; `quiz_exclusions: [硬貨, 銅貨]` goes beyond EN (EN 玉 has none). Basis: JMdict 玉 (1240530) has a coin-counter suffix sense (-だま as in 百円玉), and the card itself says 玉 is not an independent «монета». 硬貨 «монета»: real but necessity unestablished (玉's title says «суффикс монет», not «монета») -> conservative. 銅貨 «медная монета»: only reached by chaining 玉~硬貨 and 硬貨~銅貨 (the app does not apply exclusions transitively, and the contract forbids inferring them) -> unjustified. Remedy: `quiz_exclusions: [硬貨]` (or remove the line entirely; the brief's “玉 vs 硬貨” screen is satisfied either way as an optional guard). Confidence: high that 銅貨 is unjustified; medium on 硬貨.

Exclusions beyond EN, with dictionary basis and necessity classification:
| Card | Added entry | Basis (entry/sense) | Class |
|---|---|---|---|
| 画家 | 作家 | JMdict 作家 sense 2 "artist; creator" (RU 作家 «автор творческих работ» overlaps «художник»; EN titles share "artist") | conservative |
| 男子 | 男の人 | JMdict 男の人 "man"; RU «мужчина» = 男子 «мужчины», same as already-guarded 男/男性 | required |
| 男子 | おじさん, おじいさん | JMdict おじさん 2 "middle-aged man"; おじいさん 2 "old man"; mirrors the existing 男/男性/男の人 cluster of those cards | conservative (necessity unestablished; the sense is narrower than «мужчины») |
| 申し訳 | 謝る | JMdict 謝る 1 "apologize" vs 申し訳 "apology; excuse"; same «извин-» concept, different POS | conservative |
| 予防 | 防ぐ | JMdict 防ぐ "defend against; prevent"; «предотвращение» vs «предотвращать» | required |
| 使用 | 用 | JMdict 用 "use; service" (sense 2); 用 already guards 使う/利用 and 適用 guards 用 | conservative |
| 用いる | 利用 | JMdict 利用 "use; utilization"; 利用 title «использование; пользоваться» vs «использовать» (brief notes no EN guard) | required |
| 瓶 | 缶 | JMdict 缶 "can; tin" ; RU titles both contain «банка» | required |
| 玉 | 硬貨; 銅貨 | see F2 | conservative; unjustified |
| 現金 | お金, 金, 金銭 | JMdict 現金 1 "cash; ready money" vs お金/金/金銭 "money" (matches 金融's guard cluster) | conservative |
| 光景 | 景色, 眺め | JMdict 景色 "scenery; view"; 眺め "view; scene" (EN guards only 風景; RU 風景 «сцена» shares a word with 光景) | conservative |
| 事態 | 状況 | JMdict 状況 "situation; circumstances; state of affairs"; EN titles identical "situation; state of affairs" | required |
EN exclusions retained in all cards (疑問, 男子, 用心, 使用, 用いる, 生地, 命, 生, 生命, 生じる, 環境, 球, 状況, 光景, 場面, 事態) — verified by script, none dropped.

Screened with no guard needed (observed, no finding): 発表 vs 出版/紹介/説明/報告 (titles «оглашение; презентация» are not interchangeable with «публикация», «представление; знакомство», «объяснение»); 発明 vs 発見/製造/作る; 疑う vs 疑わしい/奇しい (verb vs adjective «подозрительный»); 異常 vs 非常/変/珍しい/特別/普通 (title «отклонение от нормы; аномальный» shares no segment; 普通 is the taught contrast); 留学 vs 留学生/留守/勉強; 女子/男子 (taught contrast); 布 vs 生地 (guarded) /組織 «биологическая ткань»/材料; 生地 vs パン/粉/材料; 命/生/生命 vs 生活 (EN has only 命→生活); 生じる vs 起きる/誕生; 環境 vs 都会/自然; 理想 vs 現実/夢/希望/目標; 球/玉 vs 丸い/輪; 現象 vs 出来事/事件; 場面 vs 場合/状況/光景 (guarded); 光景 vs 風景 (guarded). No new title equals another card's whole title; segment-level exact overlaps are all guarded: 使用/利用 «использование», 命/生/生命 «жизнь», 玉/球.

Optional: (1) 生 «…сырой (о пище)» shares the bare word «сырой» with じとじと «липко-влажный; сырой» and じめじめ «сырой и душный»; the parenthetical and different sense make a guard unnecessary, mention only. (2) 用いる/使用 vs 適用 «применение (правила или метода)»: the 用いる article teaches «применить новый метод», but 適用 is a noun restricted to rules/methods; not required. (3) 発表 closes with «Лексика: [JMdict]» where the corpus norm is «Словарь:» (2169 vs 4 uses); cosmetic. (4) 画家.md and 申し訳.md contain a doubled blank line before «Оттенки значения»; cosmetic.

Limits: JMdict senses cited above are from my knowledge of the entries and the cards' own citations; I did not re-fetch them. Necessity classifications for “conservative” entries rest on title overlap only (the app's real distractor selection was not simulated). Linguistic correctness of the card prose was outside my assignment (correctness/comprehensibility facets). Model identity is not verifiable from within this session.
