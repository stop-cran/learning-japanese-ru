Snapshot: RU repo `C:\Users\romanko\repos\learning-japanese-ru`, branch `full-ru-187-words-26`, HEAD `cc6b8f13ebceb4be3a1b13194f53efa9e27e0bc9` (base `cc6b8f1`). Staged review tree `git write-tree` = `1597f0853220fbaeb521bab731c807b81e62373e`, confirmed before reading and again after the read-only review (unchanged). Staged changes included: 30 new `words/*.md`, 17 navigation-only Markdown edits, `manifest.json`, `docs/translation-batches/187-words-batch-26-intake.json`. Untracked `tools/__pycache__/` is outside the tree and was not reviewed. Frozen EN source: `C:\Users\romanko\repos\learning-japanese-en-frozen` at `6af98cb717755690a9ca793e5454a96ebd7a8f9f` (matches intake `sourceCommit`).

Scope: Comprehensibility is primary; scoped coverage is the assigned batch against frozen EN. All 30 new cards were read in full: 離す, 雇う, 集団, 集中, 会, 会合, 集まり, 隠れる, 隠す, 障害, 回, 度, 際, 陰, 限界, 守る, 防ぐ, 関連, 関心, 関する, 誤り, 間違い, 始まり, 開始, 閉じる, 長期, 鎖, 鍋, 鋭い, 鋏. Navigation hunks reviewed, not a fresh full read of those baseline articles: `kanji/団.md`, `kanji/守.md`, `words/ぼんやり.md`, `words/仕舞い.md`, `words/利口.md`, `words/団体.md`, `words/対する.md`, `words/感心.md`, `words/永久.md`, `words/破る.md`, `words/約束.md`, `words/紐.md`, `words/組織.md`, `words/表す.md`, `words/達する.md`, `words/違い.md`, `words/離れる.md`. Manifest membership and intake payload paths checked. Reviewer: requested family/model Grok / `grok-4.7`; this session did not expose a verifiable runtime model identifier, so no confirmed model ID is claimed. Author report, author prompt, and other reviewers' reports were not read.

Verdicts: comprehensibility NEEDS FIX; scoped coverage CLEAN; correctness UNVERIFIED except the particle-role sentence in `words/集中.md:26-27`, which is a directly established misstatement; quiz safety UNVERIFIED. Other facets UNVERIFIED.

Findings:

1. Moderate; comprehensibility, and a directly established correctness defect for this sentence; `words/集中.md:26-27`.
   Learning impact: After the transitive example 注意を一点に集中する, both particles are described as the target. «を обозначает то, на чём сосредотачиваются» is "that on which one concentrates"; «に — место или цель» is the same role. A learner who follows the rule rather than the example can swap を and に. Line 18 is fine: there に really is the focus of 勉強に／駅に. Lines 26-27 erase the what/where split.
   Remedy: «を обозначает то, что сосредотачивают (здесь — внимание), а に — точку или цель.»
   Evidence: Lines 24-25 are 注意を一点に集中する, "сосредоточить внимание на одной точке." Frozen EN `words/集中.md`: "を identifies what is focused; に identifies where."
   Confidence: high.

2. Minor; comprehensibility; `words/関する.md:23`.
   Learning impact: The example that teaches Nに関して translates both 問題 and 質問 as «вопрос»: «У меня есть вопрос по этому вопросу.» The topic and the question about it collapse. The Japanese and the readings remain; the gloss does not support the split the example is for.
   Remedy: «У меня есть вопрос по этой проблеме.»
   Evidence: この問題に関して質問があります. Frozen EN: "I have a question concerning this issue."
   Confidence: high.

3. Minor; comprehensibility; `words/鍋.md:16` and `words/鍋.md:37`.
   Learning impact: The opening calls 鍋 a кастрюля or a сковорода. Line 37 then says フライパン is a сковорода and a different, related vessel. The learner cannot tell which word is the frying pan. Frozen EN keeps "pot or pan, including a saucepan" distinct from "frying pan."
   Remedy: Open with «кастрюля или сотейник, в том числе небольшая кастрюля»; keep フライパン as «сковорода».
   Evidence: The same Russian word «сковорода» is used for both on lines 16 and 37. EN `words/鍋.md` opening versus its フライパン sentence.
   Confidence: high that the glosses collide. «Сотейник» is a teaching remedy, not a new dictionary claim.

Optional:

- `words/際.md:25` lists 利用する際 and 訪れた際 without kana. The past/nonpast contrast is readable later at line 47 (来た際に／来る際に). Frozen EN omits those readings too. Adding りようするさい and おとずれたさい would help; it is not required to recover the distinction.
- `words/鋭い.md:22` writes 刃は as はは. That hiragana is 刃（は）plus the topic particle and matches frozen EN, but 刃 is not glossed elsewhere, so a learner can store はは as the reading. Optional: add 刃（は）before the sentence.
- `words/誤り.md:35` mentions 誤解 five lines before 誤解（ごかい）on line 40. Repeat the reading at the first mention.
- `words/会.md:44` says to compare 読書会 with a sentence that is not on the card. The next sentence already says one name can be the group or the event. Same shape as EN.
- `words/集まり.md:20` «насколько хорошо люди приходят» is vague until the turnout example. `words/隠れる.md:35` «или по-английски» is unnecessary on a Russian card. `words/障害.md:34` «не является оценкой человека» is slightly cryptic; «не оценка достоинства человека» would track the EN point more clearly.
- годан, итидан, онное, окуригана, and ваго are unlabeled. The useful forms are listed beside them, so this is house style, not a blocked lesson.

Limits:

- Japanese readings, register, and dictionary senses were not re-checked in dictionaries except where a card contradicts its own example or the frozen EN wording. No native-speaker, phone, or app check.
- Quiz safety was not audited (displayed options, both directions, existing pool). Not established, only noticed: 間違い excludes 誤り, while 誤り excludes 失敗 and not 間違い.
- Scoped coverage compared example sentences, titles, and stated distinctions with frozen EN, not every synonym line. EN links absent from RU all point at cards that do not exist in this tree. Comparison words that remain have readings, aside from the short 誤解 delay noted as optional.
- The 17 navigation edits are link wraps; `words/違い.md` also adds （まちがい）. Those hunks add no new prose problem. Baseline text outside the hunks was not re-reviewed.
- Intake `notes` were empty. Intake hashes were not recomputed. Manifest check was membership (30 added, 17 changed, none removed) and `contentVersion`, not every hash.
- Author report, author prompt, and other reviewers' reports were not read.

Confirmed: the full 30-card scope was read. `git write-tree` remains `1597f0853220fbaeb521bab731c807b81e62373e`.
