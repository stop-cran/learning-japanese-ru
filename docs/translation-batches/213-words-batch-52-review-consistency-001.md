# B213 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `3c8461447a0a88352701ecb3fc7183b5c545a07b` (tree `2e363e3eaf674dd400edb587315ee26cfe455597`),
> the signed candidate pushed before review.
> Later reconciliation is in `213-words-batch-52-recheck-001.md`.

Snapshot: RU branch full-ru-213-words-52, HEAD 3c8461447a0a88352701ecb3fc7183b5c545a07b (confirmed by `git rev-parse HEAD`); `git status --porcelain` empty before and after my work (I ran no generator; manifest recomputed in memory only). Frozen EN 6af98cb.
Scope: Facets CONSISTENCY, QUIZ SAFETY and cross-file integration. Model not verifiable from inside the session.
  Read in full (front matter + body, RU): all 30 new cards: 夫婦 夫人 大部分 大臣 大統領 大戦 大家 大半 大使 大会 大 夢中 夜明け 夜中 外交 外す 夕べ 売れる 墓 境 塔 塀 報告 よる 基づく 城 埃 地球 地域 地方.
  Navigation diffs: all 21 files (35 link restorations) read in full as diffs, plus a scripted check: removing link markup from the new text gives text identical to the parent for every file, the added link count per file matches the brief (告/報/夫/婦/球 3 each, 城/域/塔 2 each, 首相 2, the other 13 files 1 each = 35), and every added link also exists in EN (same path form; 発表 keeps `../words/`).
  EN originals: compared by script (front matter fields, link lists, quiz_exclusions); EN prose was not read line by line (that is the correctness facet).
  Also: manifest.json, intake record, `tools/validate.py` (0 errors).
Verdicts:
  Consistency: CLEAN. No exceptions.
  Quiz safety: NEEDS FIX (one Minor, F1; everything else CLEAN).
  Scoped coverage of cross-file integration: CLEAN.
Findings:
  F1; Minor; quiz safety; words/大.md:7 (`quiz_exclusions`); 大's Russian title «большой размер; огромный (как приставка)» introduces the word «огромный», and 巨大 «громадный; гигантский» (existing card, `quiz_exclusions: [莫大]`) is a near-synonym that is a defensible correct answer for it (and vice versa), with no guard on either side. The batch itself guards 莫大 «огромный; колоссальный» for the same reason (shared «огромный»), so 巨大 is the closer, unguarded case. The EN pair (large; great vs huge; gigantic) was not overlapping, so this overlap is RU-introduced by the title wording.
    Remedy: `quiz_exclusions: [大きい, 大きな, 莫大, 巨大, 大小]` in words/大.md, then the coordinator regenerates manifest.json.
    Evidence: JMdict 巨大 (adj-na) "huge; gigantic; enormous"; 大 sense 1 "large; big; great" (prefix, e.g. 大成功 «огромный успех»). Confidence: medium (it depends on how strictly "defensible" is read; a title-side alternative would be to drop «огромный» from the title, but the body uses it for 大成功).
Quiz exclusion audit:
  EN exclusions: all retained (大半 [大部分], 大 [大きい, 大きな], 外す [除く], 境 [限界], 報告 [レポート], 大戦 [戦争], 夫人 [妻, 奥さん], 夕べ [昨夜, 晩, 夜, 夕方], 売れる [売る], 塀 [壁], 基づく [よる, 生じる], 地方 [地域]). RU front matter otherwise equals EN (word, reading, jlpt, type, kanji, tags) for all 30.
  Additions beyond EN (dictionary basis; necessity in an ordinary quiz):
    大部分→ほとんど: JMdict ほとんど "most; the majority; almost all" vs 大部分 "greater part"; RU titles share «большая часть». Required.
    大部分→たいてい: たいてい has "most; the majority" sense, RU titles share «большинство». Required.
    大半→ほとんど: same basis; 大半 «большинство; в основном» vs «почти; большая часть». Required.
    大半→たいてい: RU titles share «большинство». Required.
    大→莫大: 莫大 "enormous; vast"; titles share «огромный». Required.
    大→大小: 大小 "large and small; size"; 大 title «большой размер» vs «размер; большое и малое». Required.
    夢中→熱中: 熱中 "being absorbed in; enthusiasm" vs 夢中 "absorbed in; engrossed"; titles «поглощённый» / «поглощённость». Required.
    外す→下ろす: 下ろす (降ろす) "to take down; to take off (from a hook, shelf)"; titles share «снимать». Required.
    境→瞬間: 瞬間 "moment; instant"; basis is only the shared word «момент» (境 sense 2 is «переломный момент», not an instant). Conservative.
    報告→レポート: pre-existing EN pair. 報告→リポート: リポート "report"; shares «отчёт». Required.
    報告→知らせる: 知らせる "to notify; to advise"; related but different focus (noun «отчёт» vs verb). Conservative.
    報告→伝える: 伝える sense "to convey; to report; to transmit"; title shares «сообщение/сообщать». Conservative (real gloss basis, necessity not established).
    よる→次第: 次第 "depending on (N次第)" vs よる sense 1 "to depend on"; titles «зависеть от» / «в зависимости от». Required.
    地方→州: 州 "state; province; continent"; titles share «провинция». Required.
  None unjustified (none merely guards a contrast or topical relation that the article teaches). Every exact-segment title overlap between a new card and any existing RU card is guarded (scripted check: большинство, большая часть, огромный, снимать, вечер, отчёт, провинция; «основываться на» in よる/基づく is covered by the EN pair 基づく→よる).
  Directness/transitivity: all pairs are declared directly on one side; no reverse or transitive pair was assumed.
  Unguarded close pairs I checked and judged not required (EN parity, differing sense or part of speech, the article itself teaches the contrast): 夫人/婦人, 大臣/首相, 大会/会議・試合・競技, 夜中/夜, 夜明け/朝, 外す/脱ぐ, 地方/田舎, 頼る/よる, 大戦/戦い, 大家/借りる・貸す.
Consistency checks passed: headings equal `word（reading）— title`; no duplicate keys; 0 validator errors; all in-body relative links in the 30 cards resolve to existing RU files; no Russian-only links; EN links to kanji/臣.md, kanji/領.md, kanji/境.md and words/代表.md remain plain text and those four files are absent from RU (verified); manifest.json recomputed in memory equals the committed file (4,504 entries, contentVersion 2266857bdb63c3be); the intake record's 51 payload paths equal the candidate's content diff (30 new + 21 modified), all candidateRawSha256 values match the files, and it contains only paths, hashes, baseline and a note (no learner content). No generated or unrelated files were committed (the only non-content files are manifest.json and the intake record).
Optional:
  - Further RU-title overlaps with existing cards that mirror EN, with no required action: 地球 «планета Земля» vs 地 «земля; местность» (地.md itself teaches the planet/ground split), 地域 «округа» vs 近所 «окрестности», 報告 «сообщение» vs 教える «…; сообщать». Consider guards only if the owner wants stricter RU-specific screening.
Limits:
  - This review did not check Japanese-language correctness or EN-prose fidelity line by line (correctness facet); I only compared front matter, links and exclusions with EN.
  - Pre-existing differences from EN in files outside this batch's diff (38 EN-link differences in older cards such as 入口/出口, 理解, 国内 and many kanji cards) were seen and not evaluated; none targets a word in this batch.
  - The dictionary senses cited are from my knowledge of JMdict entries and were not re-fetched online.
