Snapshot: learning-japanese-ru `full-ru-170-words-09` @ 0c9b9df (parent c526abc); worktree clean. EN source: learning-japanese-en-frozen @ 6af98cb.
Scope: I reviewed the actual diff `git diff c526abc 0c9b9df`. It touches six files: words/ころ, ばかり, ほぼ, 一応, 後輩 and manifest.json. The manifest change only updates five hashes and contentVersion, and all five hashes match the committed file bytes. tools/validate.py reports 0 errors. I re-ran rutools/word_title_screen.py for ころ and ばかり. The rest of the batch is unchanged since my first review of c526abc. Reviewer: the same blind reviewer (Claude). I did not read the author report.
Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety CLEAN.

Reconciliation:
F1 (ばかり–ほぼ pair): resolved. words/ばかり.md:8 is now `[ほど, ころ, それほど, 大体, 程度, さっき, 約, およそ, ほぼ]`. One direct exclusion is enough, so the ほぼ side does not need to change. No regression.
F2 (後輩.md:21): resolved. «Он мой младший товарищ по университету.» is natural Russian, works for a current or a former student, and matches EN "a junior from my university".
F3 (後輩.md:41): resolved. «новичок старше по возрасту может быть младшим по времени прихода или опыту» now says "older than the others" without implying old age. Grammar and agreement are correct.
Optional ほぼ.md:28-29: resolved. «Словарь приводит 略 и 粗 как редкие кандзи-написания этого наречия.» reads naturally. The next sentence and the meaning are unchanged, and the paragraph still reflows correctly.
Optional 一応.md:20: resolved. «Подготовка более-менее закончена.» is no longer tautological, and «более-менее» still conveys 一応.
Optional ころ guards: resolved. ころ.md:9 is now `[くらい, ほど, 時間, 約, ほぼ, およそ]`. ころ «время, когда; около (о времени)» now excludes every "approximately" word that could be read as «около».
Optional のんき–悠々/平気: declined; I accept this as optional, not a defect. The titles share no sense word, and I rated the overlap as loose.
Optional hypernym guards (動物/家畜) for the bird and fish words: declined; I accept this. It comes from EN, and a hyponym and its hypernym are distinguishable answers.
Limits item 常→非常に extra link / 常·非 kanji wording: outside scope. These cards predate this batch, so it is not counted against it.

Regression check, distractor pools:
- ころ now has 6 exclusions and ばかり has 9, out of 1753 word cards. Neither article has a curated `distractors` field, so the quiz draws from the general pool, and a 9-entry exclusion list leaves it ample.
- The new guards remove only answers that were genuinely ambiguous. Non-synonymous time and degree neighbours are still available as distractors. For ころ these include, for example, いつ, 最近 and 季節, all of which the title screen lists as present.
- The remaining title-screen hits for ころ and ばかり are stem false positives on «время»/«время…». They were already present at c526abc and are distinguishable, so they are not new.
- No other front matter changed.

Optional: none new.

Limits:
- I re-read only the diff and the surrounding passages. The 25 unchanged articles were reviewed at c526abc and were not re-read.
- I did not check rendering, app behaviour or audio.
- I did not run the quiz engine itself; the distractor-pool judgement is based on the pool size and the exclusion lists.
