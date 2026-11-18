Snapshot: learning-japanese-ru `8a7a43c` (parent `c3f1c45`), branch full-ru-181-words-20; HEAD = 8a7a43c; worktree clean (no uncommitted changes).
Scope: Recheck of the fix diff c3f1c45..8a7a43c: words/公演.md, 煮える.md, 煮る.md, 武士.md, 叫ぶ.md and the manifest.json hash entries for those files. I re-read each changed passage in context. I confirmed that every new quiz_exclusions target exists as a RU word card: 演説, スピーチ, ぐつぐつ, ことこと. I confirmed that the manifest hashes match the committed file bytes. The rest of the batch is unchanged since the original review, so the c3f1c45 assessment carries over. Reviewer: independent read-only reviewer (Claude).
Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety CLEAN

Findings (reconciliation):
- F1 (Medium, quiz safety, words/公演.md): resolved. The 公演 card now guards both スピーチ («выступление перед слушателями») and 演説 («публичная речь; выступление») directly. Keeping the title is acceptable, since the guard was one of the two proposed remedies. Both pairs are justified by the shared «выступление» and the existing スピーチ–演説 precedent. Neither pair is over-broad: 公演 itself is never a speech. No regression.
- F2 (Low, quiz safety, words/煮える.md:9, words/煮る.md:9): resolved.
  - 煮える–ぐつぐつ and 煮える–ことこと are justified: «кипеть» and «томиться» cover the liquid-boiling and simmering uses of 煮える, and the RU ぐつぐつ card itself glosses 煮える as «вариться, томиться».
  - 煮る–ことこと is justified: «тушить» against «томиться на медленном огне», and the 煮る article says gentle simmering fits.
  - No 煮る–ぐつぐつ pair was added. I agree it is not needed: a transitive «варить; тушить» is not a defensible answer for «булькать на огне; кипеть», and the reverse question is weaker.
  - Neither new guard is unjustified.
- F3 (Low, comprehensibility, words/武士.md:28-29): resolved. The line now reads «эти слова не являются ни повсеместно противоположными, ни полностью взаимозаменяемыми терминами». It is grammatical and the meaning is still that of the EN line ("not universally opposites or perfectly interchangeable technical labels"). No regression.
- Optional 叫ぶ (line 25): resolved. «переход в ん в 叫んで и 叫んだ» is clear and still accurate (撥音便 in godan ぶ-verbs).
- Optional うきうき «всплывающего»: kept as optional, declined. This is acceptable; it is not a defect.
- Optional がやがや/ざわざわ–うるさい and 公演–コンサート: kept as optional, declined. This is acceptable; the overlap is weak and matches EN.

Optional: none new.
Limits: The quiz app and repo validator were not run. Dictionary URLs and JMdict entry numbers were not re-fetched; they are unchanged from EN. The pre-existing extra 兆候 link in kanji/候.md remains outside this batch's scope.
