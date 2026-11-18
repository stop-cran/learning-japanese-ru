Snapshot: RU repo `learning-japanese-ru`, branch `full-ru-177-words-16`, fix commit `2097b18` (parent `0abb3aa`, the review-001 snapshot). Working tree clean; no uncommitted changes.

Scope: recheck of `git diff 0abb3aa 2097b18`. That diff touches only words/増す.md, words/昇る.md, words/松竹梅.md, words/梅.md and manifest.json. I re-read the changed passages in context, checked the manifest hashes, and checked the commit tree for generated files. Reviewer: the same independent read-only reviewer as review 001 (Claude-family model; exact version not exposed).

Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety CLEAN

Findings:
- F1 (Medium, quiz safety, words/増す.md:9): resolved. The line now reads `quiz_exclusions: [増える, 拡大, 上がる, 上げる]`, matching the 増える precedent. Nothing else in the file changed.
- F2 (Low, comprehensibility, words/松竹梅.md:18): resolved. «таке» is now «такэ», consistent with «умэ» and the Polivanov spelling used elsewhere in the repo. The Japanese text and kana are unchanged.
- Optional 昇る–進む: adopted and correctly applied. words/昇る.md:8 now reads `quiz_exclusions: [上がる, 登る, 増加, 進む]`. All earlier exclusions are kept, and the guard is justified by the shared bare «продвигаться».
- Optional 松竹梅:18 «Комплексные обеды»: adopted. The line now reads «Комплексные меню в этом ресторане делятся на разряды…». It is grammatical, fits the plural subject, and is consistent with line 20 («названия разрядов меню»).
- Optional 梅:40 «базовый комплекс»: adopted. The text now reads «…может означать самый простой вариант меню, а не блюдо из умэ. Контекст отделяет это подтверждённое значение разряда от названия растения.» Only the line breaks moved; the meaning is unchanged, and it still matches EN ("the basic course, not a meal made from ume").
- Optional 漁業:20: declined by the owner. I accept that; the line is accurate and acceptable as written. Status: optional (no change needed).
- Optional 水産 title: declined by the owner. I accept that; the title is accurate for EN "aquatic products; fisheries". Status: optional (no change needed).
- manifest.json: no regression. Only `contentVersion` and the hashes for the four edited files changed. The hashes of every non-stroke entry (all md files, including the four new hashes) match the SHA-256 of the files on disk.
- Generated files: none. The 2097b18 tree contains no `__pycache__` or `.pyc` files.

Optional: none new.

Limits:
- 118 `strokes/*.json` entries do not match a raw-byte SHA-256 of the file on disk. The batch does not touch those files, and the fix-commit manifest diff does not change their entries. The cause is most likely a different hashing or normalisation convention for stroke JSON; I did not investigate it further, and I do not attribute it to this batch.
- I did not re-run the title screen for the whole batch. The fix changes no titles, only the exclusions on 増す and 昇る.
