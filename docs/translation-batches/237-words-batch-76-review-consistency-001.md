# B237 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `be448e7c8309d0b9fe6296bd3bc75b2508312556` (tree `3fdba75c00a9a083e212398d0b36c726a2e6f7e7`),
> the signed candidate pushed before review.
> Later reconciliation is in `237-words-batch-76-recheck-001.md`.

Snapshot: RU HEAD = be448e7c8309d0b9fe6296bd3bc75b2508312556 (confirmed); `git status --porcelain` empty (a __pycache__ I created by importing build_manifest was deleted; tree clean again). `python tools/validate.py`: 0 errors.

Scope: read in full (front matter + body) all 30 new cards: おじゃまします ごめんください お待ちどおさま お待たせしました ごめん すまない 詫びる 評論 診断 診る 訳す 言葉遣い 言付ける 言い付ける 解説 応ずる 回答 解答 溶ける 解散 占う 観測 アイデア アイディア 観念 親類 親指 覗く 見送る 慰める. Read in full all seven navigation diffs (付, 占, 言, 応じる, 解ける, 説明, 集合; -U0 diffs, every changed line seen). Compared every new card's front matter (except title), heading count and .md link set against the frozen EN card by script; checked all RU runtime links resolve; checked EN-link parity in every EN file that links a new word; compared manifest.json with `build_manifest.build_manifest()` in memory (no write): identical; checked the intake record path list against the diff. Model: not verifiable.

Verdicts:
- Consistency: CLEAN
- Quiz safety: NEEDS FIX (three low-severity missing guards, see Q1-Q3; all EN exclusions retained, RU-added exclusions all justified)
- Cross-file integration: CLEAN

Findings:
- Q1; low; quiz safety; words/すまない.md:8 (quiz_exclusions) and words/悪い.md (title «плохой; виноватый»): the new すまない title «извини, виноват; …» contains «виноват», and 悪い's RU title is «плохой; виноватый»; the 悪い card itself teaches 悪いね as «Извини за это». Neither side declares the pair, so 悪い can be offered as a distractor for すまない (and the reverse) with "виноват" defensible for both. EN titles ("sorry; apologetic gratitude" / "bad; poor; at fault") did not collide this way; the overlap is introduced by the RU wording. Remedy: すまない line 8 add `悪い` -> `quiz_exclusions: [すみません, ごめん, ごめんなさい, ありがとう, 謝る, 申し訳, 恐縮, あいにく, お待ちどおさま, お待たせしました, どうも, 感謝, 御礼, 礼, 悪い]`. Evidence: 悪い card body («Разговорное извинение 悪いね»), JMdict 悪い sense "(col) sorry". Confidence: medium.
- Q2; low; quiz safety; words/おじゃまします.md:8: title «простите за беспокойство (входя к кому-либо)» vs すまない «…прости за хлопоты» are both "sorry for the trouble" apologies in the same RU register; neither side declares it (おじゃまします only lists すみません, ごめんなさい; すまない lists neither おじゃまします). EN had no guard, so this is a RU-wording-level gap, defensible only for the parenthetical-less reading. Remedy: おじゃまします line 8 -> `quiz_exclusions: [すみません, ごめんなさい, すまない]` (or add おじゃまします to すまない). Confidence: low-medium (conservative; not required by EN).
- Q3; low; quiz safety; words/言付ける.md:8 and words/言い付ける.md:8: 頼む (title «просить; поручать»; exclusions [呼ぶ]) shares «поручать» with 言付ける «…поручать доставку (вещи)» and 言い付ける «велеть (сделать что-либо)»; 依頼 «просьба; поручение» likewise. No side declares these pairs. EN did not either; conservative. Remedy: 言付ける line 8 -> `[伝える, 預ける, 送る, 任せる, 頼む]`; 言い付ける line 8 -> `[言う, 伝える, 教える, 命じる, 命令, 報告, レポート, リポート, 頼む]`. Confidence: low.

RU-added exclusions beyond EN (dictionary basis; necessity):
- 回答 + 応対: JMdict 応対 "dealing with, receiving (visitors/callers)", 回答 "reply"; RU title of 応対 «ответ на обращения» overlaps 回答 «ответ на вопрос (запрос…)» -> required (title level).
- 解散 + 終了, 閉会: JMdict 解散 sense 1 "breaking up (of a meeting)"; 終了 "end", 閉会 "closing of a meeting"; titles «окончание сбора» vs «окончание (мероприятия…)» / «закрытие собрания» -> 終了 required, 閉会 conservative-to-required. Note: 解散 has no EN-guard against 別れる sense conflict problem (already kept).
- 観測 + 読み: 読み sense "(ability to) read a situation; forecast", titles «прогнозная оценка» vs «оценка ситуации» -> required.
- 親類 + 親戚: JMdict 親戚 = "relative" same sense, titles «родственник; родня…» vs «родственник; родня» -> required.
- 見送る + 省く, 飛ばす: JMdict 省く "to skip", 飛ばす "to skip over", 見送る "to let pass"; shared «пропускать» in titles -> required at title level, conservative dictionary-wise.
- 慰める + 落ち着く: JMdict 落ち着く "to calm down", 慰める "to comfort; to soothe the heart"; «успокаивать (душу)» vs «успокаиваться» differ in transitivity -> conservative (real Russian-root overlap, necessity unestablished). No unjustified entries found; none guards a contrast the article teaches.
All EN exclusions are retained in every card (script diff: RU is a superset everywhere; 慰める had none in EN). アイデア/アイディア carry identical titles; per the repository's rule identical titles deduplicate, and the pair is not declared (same as EN).

Checked and clean (evidence): front matter keys/values identical to EN for all 30 except the six cards that only add exclusions above; heading counts and section order equal EN; link sets equal EN except where the RU target is absent (悔やむ, 敬語 words; kanji/訳, 溶, 測 absent from RU; unlinked plain text is correct) and one RU-only link 言付ける -> 言い付ける.md (target exists, substantive comparison at the "Оттенки" line, EN links it nowhere; acceptable and helpful); no broken links in any RU kanji/words/articles file; for every EN file linking a new word, the RU counterpart either does not exist or has the same number of links (0 count mismatches). Navigation files: each diff changes only link brackets/hrefs at EN positions (付:51; 占:20,32,37, plain mention at 44/footer left plain like EN; 言:41; 応じる:39; 解ける:35; 説明:36; 集合:31), path forms match EN, 9 occurrences/7 files confirmed. Glosses beside new titles do not mislead (付/言 «велеть; сообщать/донести…» vs 言い付ける; 占 «гадать; предсказывать»; 集合 «расходиться; роспуск»; 説明 «объяснение или комментарий»; 解ける «таяние или растворение»). manifest.json equals an in-memory rebuild (no stale hash; contentVersion consistent). Intake record: 37 payload paths = the 30 cards + 7 navigation files; diff additionally contains only intake itself and manifest.json; notes line adds no learner content. No generated/unrelated files committed.

Optional: none.

Limits: no title-screen tool output was read; semantic screening was done by my own title review plus pair coverage matrices (apology/thanks family, answer, decision, show/see, group/end clusters, title-stem overlaps against all RU word titles). Dictionary senses cited from memory of JMdict/titles in cards, not re-fetched. Linguistic correctness (readings, nuance) is not in this facet beyond observed inconsistencies.
