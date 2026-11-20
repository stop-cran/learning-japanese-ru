# B199 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `b99047ab07da1b5364690335e4fede1db79dca76`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 198 tree `80c7336` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `199-words-batch-38-recheck-001.md`.

Snapshot: candidate tree b99047ab07da1b5364690335e4fede1db79dca76 (base 80c7336), worktree learning-japanese-ru-b198, HEAD 5dd9a78. Verified: `git diff-index --cached --quiet <tree>` = 0, `git diff --quiet` = 0, no untracked files; no uncommitted differences beyond the expected staged delta. No `__pycache__` left.
Scope: 30 new word cards (all read against their EN originals' front matter/links; bodies read in full), 13 navigation-only restorations (diff inspected line by line), manifest.json. Facets: consistency, quiz safety, cross-file integration. Model: not verifiable from inside the session.
Checks run (read-only, -X utf8 -B): tools/validate.py = 0 errors; build_manifest.build_manifest() imported (no write) equals manifest.json exactly; changed-file list = 30 new + 13 nav + manifest = 44 (no unrelated/generated files); own link audit over all 43 files: no broken link, no RU-only link, every EN link either restored or its RU target is absent (kanji 硬/貨/砂/炭/県/接/銅, words 仲間/スタート/到着/意志/重ねる); scan of ALL RU/EN cards for EN links to batch words not restored in RU: none; link_parity.py OK (43 files). Exclusion scan against all 2,623 RU word cards: no EN exclusion lost (either side); no batch title segment exactly equal to another card's title segment without a direct guard (own script, segments split on `;`, parentheticals stripped).

Verdicts:
- Consistency: CLEAN
- Quiz safety: CLEAN (no required guard missing; see classification below)
- Scoped coverage of cross-file integration: CLEAN

Findings: none.

Extra quiz_exclusions beyond EN (all one-sided direct pairs; dictionary basis; necessity classification)
- 確実→確か: JMdict 確か "certain; sure; reliable" vs 確実 "certain; reliable" (titles «достоверный; кажется» / «несомненный; надёжный»). required.
- 確実→堅い: JMdict 堅い sense "reliable; steady"; RU titles share the exact segment «надёжный». required (segment rule).
- 確実→違いない: 違いない "no doubt; certain". Conservative (real basis, body teaches the に違いない contrast).
- 確実→きっと: きっと "surely; undoubtedly". Conservative (title «почти несомненно»).
- 確かめる→調べる: 調べる "to examine; to check"; titles share the exact segment «проверять». required.
- 情報→案内: 案内 sense "information; guidance"; RU titles share the exact segment «информация». required.
- 知らせ→知らせる: 知らせる "to notify; to inform" vs 知らせ "notice; notification"; shared stem «уведом-». Conservative (different POS; weak necessity, harmless).
- 真剣→重大, 真剣→大変: 重大 "serious; grave", 大変 "serious; terrible"; Russian «серьёзный» shared with «серьёзно настроенный». Conservative (the card teaches this contrast; real Russian-gloss overlap, necessity unestablished).
- 真似→写す, 真似→コピー: JMdict 真似 includes "imitation; mimicry; copying"; 写す "to copy"; コピー "copy". Conservative (card teaches the contrast).
- 真っ赤→赤い, 真っ赤→赤: 赤い "red", 赤 "red; red colour"; titles «красный» / «красный цвет» vs «ярко-красный; совсем красный». Conservative-to-required (a bare «красный» is a defensible answer for 真っ赤; matches existing 赤→赤い).
- 県→都: 都 "Tokyo metropolis; metropolitan prefecture"; 都's title contains «префектура». Conservative (card itself says «префектура» may render 都/府).
- 直接→まっすぐ: まっすぐ "straight; direct"; «напрямик» ≈ «напрямую». Required-leaning (Russian near-synonyms), mirrors すぐに→まっすぐ.
- ゴール→ため, 目標→ため: ため "purpose; goal; objective" (cf. EN 目的→ため). 目標→ため: required by parity with EN 目的→ため (title «намеченная цель» vs «цель; ради»). ゴール→ため: conservative (ゴール's title lacks «цель»; body does teach «конечная цель»).
- 指導→教育, 指導→教える: 指導 "guidance; instruction; coaching" vs 教育 "education; training", 教える "to teach". Conservative (real gloss overlap; body teaches the contrast).
- 監督→管理: JMdict 管理 "control; management; administration; supervision" vs 監督 "supervision; control". required (genuine gloss overlap).
- 登山→登る: 登る "to climb"; 登山 "mountain climbing". Conservative, weakest in the set (noun vs verb; titles «восхождение на гору» / «взбираться; подниматься»). Harmless; retain or drop at the owner's discretion.
None is classified unjustified.

Optional (nonblocking, not recommended as required):
- Stem-level leads adjudicated, no guard required: 直に vs 自身 («лично» vs «сам (лично); собственный»: different words/POS); 相手 vs 向こう (side-of-room sense only); 真剣 vs 集中 (adjective vs noun «сосредоточение»; a guard would be conservative at most); 情報 vs 通信 (no shared defensible answer).
- 指導 vs 管理 («руководство» vs «управление; контроль») could be added conservatively; not established as necessary (指導's body does not teach 管理).

Limits: Quiz presentation in the Android app was not run; "defensible answer" judged from Russian titles, card bodies and cited JMdict senses as recalled/indicated by the cards (no live dictionary fetch). Linguistic correctness and comprehension are other reviewers' facets and were not judged; batch intake record, ledger and progress files are out of scope and were not read.
