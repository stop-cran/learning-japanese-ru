# B206 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `6bfa34bee12a8bc1e805693a49888fb65cfd7331`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 205 tree `84dc60f` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `206-words-batch-45-recheck-001.md`.

Snapshot: RU scratch worktree C:\Users\romanko\repos\learning-japanese-ru-b198, candidate tree 6bfa34bee12a8bc1e805693a49888fb65cfd7331 (base 84dc60f). `git diff-index --cached --quiet <tree>` exit 0, `git diff --quiet` exit 0, `git ls-files --others --exclude-standard` empty: index and working tree equal the candidate; no uncommitted differences. No generator run; no repository file modified.

Scope: Facets CONSISTENCY, QUIZ SAFETY and scoped cross-file integration. Read in full (front matter + body, against the frozen EN original for front matter/links/exclusions): all 30 new cards 日常 日光 日付 既に 旗 旅 方向 方々 新鮮 新た 断る 文明 文字 文 敵 数字 数える 敬意 教科書 教授 教師 出身 故郷 政府 放す 攻撃 支店 支出 操作 損害; all 17 navigation diffs (kanji/師 [3 positions], words/単語 [2 links on one line], 句 太陽 害 尊敬 数 曜日 生まれ 生徒 腐る 衝突 被害 計る 計算 議会 離す) in full (`-U0` diffs; each changes only link brackets/hrefs at an existing EN link position, no prose change). manifest.json diff inspected; every .md entry hash recomputed from the tree and matched; all 30 new files listed; no unlisted .md. `tools/validate.py`: 0 errors. Scripted screening: every new title/segment (parentheticals stripped) against ALL RU word titles; EN exclusion retention; link existence/parity/RU-only links; front-matter parity with EN. Dictionary checks: Jisho/JMdict API for 離す and 放す. Reviewer model: not verifiable by me.

Verdicts:
- Consistency (front matter, terminology, links, navigation, manifest, no stray files): CLEAN
- Quiz safety: CLEAN
- Scoped coverage of cross-file integration (links to existing RU targets, EN pairs retained, no Russian-only links): CLEAN

Findings: none.
- All 30 cards: front matter matches EN except title/quiz_exclusions (translated/extended); all internal links resolve to existing RU files; no RU-only links; no EN link with an existing RU target dropped (unlinked pointers such as 国会, 日差し, 本店, 味方 are plain text because no RU file exists - allowed by convention); LF endings, final newline.
- All 17 navigation files: link restored at the EN link position only; kanji/師.md uses ../words/教師.md, words/ files use sibling paths; all targets exist.
- manifest.json: all new/changed .md hashes match their bytes. (118 strokes/*.json show a hash mismatch against the Windows working-tree bytes, but none is in the diff and all are unchanged from base; this is the manifest's newline normalisation, not a batch defect. contentVersion not recomputable without the generator - Limits.)
- EN exclusions: all retained in every card (日常 暮らし/普段/生活; 既に もう; 旅 旅行; 新た 新しい/新鮮; 文明 文化; 文字 字; 文 文章; 敵 相手; 敬意 尊敬/尊重; 教科書 テキスト; 教授 指導; 教師 先生; 故郷 出身; 攻撃 討つ; 支出 費用/消費; 操作 運転; 損害 被害/害).
- No new title or title segment equals another card's title/segment without a direct pair (screened against all RU word titles; new exact-segment collisions: 日付/月日, 方々/人, 文/案, 文/提案, 旅/旅行, 既に/もう - all guarded).

Exclusions beyond EN (dictionary basis; necessity):
- 日付 -> 月日: JMdict 日付 sense 1 "date" vs 月日 sense "date (calendar)"; RU «дата» vs «календарная дата». Required.
- 方々 -> 人: 人 «люди» equals segment «люди (уважительно)» after parenthetical strip; JMdict 人 "person; people" vs 方々 sense 1 "people (hon.)". Required.
- 方々 -> 方: 方 sense "person (polite)" vs 方々 かたがた. Conservative (real basis, necessity unestablished).
- 新鮮 -> 新しい: JMdict 新鮮 "fresh"; 新しい has a "fresh" sense (the card itself teaches 新しい魚). Conservative.
- 断る -> 遠慮: JMdict 遠慮 includes "declining (an offer)"; RU title «вежливый отказ». Required.
- 文 -> 案, 提案: 文 «предложение (грамматическое)» vs 案 «предложение; проект» / 提案 «предложение (на рассмотрение)»; same Russian word, different Japanese senses (JMdict 文 "sentence", 案/提案 "proposal"). Required (the card also teaches this trap).
- 数える -> 計算: JMdict 数える "to count" vs 計算 "calculation; counting on"; the card states both can be rendered «посчитать». Conservative.
- 教授 -> 教える: 教授 sense 1 "teaching; instruction" vs 教える "to teach"; Conservative. 教授 -> 教師: 教授 sense 2 "professor" vs 教師 "teacher"; real basis, Conservative.
- 出身 -> 生まれ: JMdict 出身 "native of; graduate of" vs 生まれ "birth; birthplace". Required/conservative (shared "откуда родом"; no RU 出身 pair existed on 生まれ side).
- 故郷 -> 田舎: JMdict 田舎 sense "hometown; native place"; RU 田舎 title segment «родные места». Required. 故郷 -> 生まれ: 生まれ «место рождения» vs 故郷 «родной город». Required/conservative.
- 支出 -> 支給: JMdict 支給 "payment; provision; allowance" vs 支出 "expenses"; both money-out. Conservative (weakest; harmless).
None unjustified (no antonym/topical-only guards). No missing required guard found. 放す vs 離す: JMdict 離す = "to separate; to part; to divide; to keep apart" (no "let go" sense); 放す = "to release; let go; set free" - the sense sets and RU titles do not overlap, so no guard needed. 放す vs 話す: different title meaning; no guard needed.

Optional:
- 日光 «солнечный свет» has no guard against 光 «свет» (光 already excludes 日 but not 日光) or 明かり; titles are not equal and the specific "солнечный" qualifier distinguishes them, so not required; a conservative 日光->光 line could be added if wanted.
- 方々 keeps the EN merged title «люди (уважительно); повсюду» (two lexical identities in one title, faithful to frozen EN "people (respectful); here and there"); the card body explicitly separates かたがた and ほうぼう. Not a defect; noted only because the cluster brief flags it.

Limits: manifest contentVersion not recomputed (generator forbidden); strokes JSON hashes not comparable in this working tree; dictionary evidence beyond 離す/放す rests on my knowledge of JMdict senses (not individually re-fetched) and card citations; Japanese/Russian linguistic correctness and comprehensibility are other reviewers' facets.
