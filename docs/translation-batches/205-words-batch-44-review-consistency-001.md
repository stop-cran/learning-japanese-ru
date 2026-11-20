# B205 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `e26a8e9466a82a925d4a0c429efe08a701323ae3`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 204 tree `d9a9765` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `205-words-batch-44-recheck-001.md`.

Snapshot: candidate tree e26a8e9466a82a925d4a0c429efe08a701323ae3 (base d9a9765) in worktree learning-japanese-ru-b198, detached HEAD 5dd9a78. Index and working tree both equal the candidate (`git diff-index --cached --quiet` = 0, `git diff --quiet` = 0, no untracked files). `tools\validate.py` reports 0 errors. Running `build_manifest.py` rewrote manifest.json byte-identically (tree still equals the candidate), so there is no stale hash. No other uncommitted changes.

Scope: Facets: CONSISTENCY, QUIZ SAFETY, cross-file integration coverage. Read in full against the frozen EN source (front matter and body): all 30 new cards (札 本物 本人 未来 木曜 服装 有能 有効 有利 月曜 最高 最終 最低 最中 替える 書類 書斎 更に 曜日 暮らす 暮らし 暗記 景気 普段 時刻 昨 明後日 元 旧 日曜). Read in full: all 22 navigation diffs (kanji 低 効 暮 未; words 上等 亥 卯 基 巳 時期 書物 期間 松竹梅 火曜 現在 精々 素 自身 過ごす 過去 酉 金曜). Also checked: manifest.json integrity; EN-vs-RU link parity for the 30 cards (every EN link target either linked in RU or absent from RU: kanji 札/装/替/普/旧, words 効果/不利/換える/資料/以前/人生/日付, and the kaeru article, all absent); parity over every RU file that EN links to a batch word (no unrestored links); the navigation files unlinked and compared with their base (all 22 are identical after link markup is stripped, only added link brackets/hrefs); title screening against all 2803 RU word titles (word_title_screen.py used as a lead only; every segment/stem hit has a guard). Reviewer model: not verifiable from inside the session. Authoring, batch records and other reviewers' reports not read (blind).

Verdicts:
- Consistency: CLEAN (front matter, section structure, title/heading match, EN link parity, navigation-only changes, manifest all verified).
- Quiz safety: NEEDS FIX (two minor missing guards, F1 and F2; all EN exclusions retained; all identical-title/segment collisions are guarded).
- Cross-file integration (scoped coverage): CLEAN.

Findings:
- F1; Minor; quiz safety; words/暮らす.md:11 (`quiz_exclusions: [住む, 生きる]`); the verb 暮らす «вести жизнь; жить (где, как, с кем)» has no direct pair with 生活 «повседневная жизнь; быт». The 生活 card itself teaches 生活する — «жить; вести свою жизнь» (words/生活.md, Значение), and JMdict records 生活する as "to live", so 生活 is a defensible answer for 暮らす. The repository already treats this overlap as guard-worthy: 暮らし↔生活 (EN pair) and 生きる→生活. The EN-derived 暮らす card has only [住む]. Remedy: `quiz_exclusions: [住む, 生きる, 生活]`. Evidence: JMdict くらす/暮らす "to live; to get along"; 生活 (sense: life, living; suru-verb "to live"). Confidence: medium (real basis; the guard is not mandated by the EN file).
- F2; Minor (conservative-to-required); quiz safety; words/暗記.md:9-10 (no `quiz_exclusions`); 暗記 «заучивание наизусть», taught as 暗記する (a transitive suru-verb: «выучить наизусть»), vs 覚える «запоминать; помнить». JMdict 覚える sense 1 is "to remember; to memorize", so 覚える is a defensible answer for 暗記. 記憶 «память; воспоминание» is already guarded against 覚える, which shows the same domain is treated that way. Neither EN card has this pair. Remedy: add `quiz_exclusions: [覚える]` to words/暗記.md (placed after `tags:`). Confidence: medium.

Optional (nonblocking; no finding):
- 書類 «документы; бумаги» vs 紙 «бумага»: stems «бумаг» overlap; the body already separates paper material from documents. Defensibility of «бумага» for 書類 is weak, so conservative: `quiz_exclusions: [紙]` if the owner wants it.
- 服装 «форма одежды; манера одеваться» vs 格好 «внешний вид; форма»: the 格好 card teaches the clothing sense («как человек одет»), so a conservative guard would be `[衣服, 服, 格好]`. No title-segment collision.
- 書斎 «кабинет (комната в доме)» vs 研究室 «…кабинет преподавателя»: different qualifiers; no guard needed in my view.
- 元 «бывший; источник» vs 基 «основа; база» / 素: all share JMdict もと 1260670, but «источник» is not a defensible answer for «основа». The 基 card already notes the overlap. No guard needed.
- 時刻 «время по часам; момент времени» vs 何時 «который час; во сколько»: question-form title; unlikely to be defensible.
- 暮らす vs 過ごす «проводить время»: the (baseline) 過ごす card states the overlap in "вести образ жизни"; the 過ごす title is not defensible for 暮らす. No guard needed.

Beyond-EN quiz_exclusions entries (dictionary basis; necessity):
- 木曜→木曜日, 月曜→月曜日, 日曜→日曜日: JMdict 木曜/月曜/日曜 are abbreviated forms of 木曜日 etc. Identical Russian titles (precedent 火曜/金曜). REQUIRED.
- 明後日→あさって: JMdict 明後日 (あさって / みょうごにち) one entry, identical title «послезавтра». REQUIRED.
- 最中→盛り: 盛り "height (of season); prime" vs 最中 "middle; height of"; segment «разгар» equal to 最中's «разгар (какого-либо дела)» core. REQUIRED.
- 暮らす→生きる: 生きる "to live; to exist"; segment «жить» identical to 暮らす «…жить…». REQUIRED.
- 元→種: 種 (たね) "seed; source; cause"; segment «источник» identical. REQUIRED.
- 本物→本当: 本当 "truth; reality; genuine/real"; 本物 "genuine article". No segment equality («настоящий» vs «подлинная вещь»), real overlap. CONSERVATIVE (real basis, necessity unestablished).
- 本人→自身, 自分: 自分/自身 "oneself"; 本人 "the person in question; the person themself". «сам…» overlap in all three titles. CONSERVATIVE. Not unjustified: the sense overlap is real and the cards cross-reference.
- 更に→それに: それに "besides; moreover"; 更に "furthermore; moreover". «вдобавок» vs «к тому же» are near-synonyms; no segment equality. CONSERVATIVE.
- None of the additions guard an antonym/contrast the article merely teaches; none unjustified.
- EN exclusions: all present (未来 [将来,先], 服装 [衣服,服], 最終 [最後], 最中 [途中], 替える [取り替える,変える,変更], 更に [もっと], 暮らす [住む], 暮らし [生活], 普段 [普通,たいてい,いつも], 時刻 [時間,時], 旧 [元]).
- Identical-title/segment screen: 木曜/月曜/日曜/明後日 (long forms), 普段 vs 普通/たいてい/いつも (EN), 旧 vs 元, 元 vs 種, 暮らす vs 住む/生きる, 最中 vs 盛り, 未来 vs 将来 all guarded on at least one side. No unguarded segment equality found.

Limits: Dictionary evidence for the F1/F2 bases and the Optional items is from memory of JMdict senses and the cards' own taught senses; I did not re-fetch the dictionary entries. The app's actual displayed answer text (full title vs segments) was not inspected; segment-based conclusions follow the review contract. Correctness of Japanese/Russian content (the other facets) was not reviewed beyond what consistency required. The batch record, ledger, progress files and the manifest intake record are out of scope.
