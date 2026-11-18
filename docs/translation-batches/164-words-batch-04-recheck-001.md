Snapshot: a934d95 (branch full-ru-164-words-04; working tree clean). Fix diff 0501fab..a934d95. EN frozen source 6af98cb.
Scope: Recheck only. Read the full diff 0501fab..a934d95: words/文句.md, 句.md, くるくる.md, ころころ.md, だらだら.md, and the manifest.json hash/contentVersion lines. Reread the changed passages in context for regressions. validate.py: 0 error(s); no __pycache__ was left behind. words/反対.md exists. Reviewer: Claude (independent reviewer agent; same reviewer as the first pass). The repo was not modified.
Verdicts: correctness CLEAN; scoped coverage CLEAN; Russian comprehensibility CLEAN; quiz safety CLEAN.

Findings (reconciliation):
Q1 - resolved. words/文句.md:9 is now quiz_exclusions: [句, 表現, 言葉, 反対]. This is the direct 文句–反対 pair («возражение»), and the validator accepts it. No other quiz fields changed.
C1 - resolved. words/句.md:17-20 now reads: «группа слов, меньшая, чем предложение… словосочетание; ср. «именная группа»… Русское «фраза» в подписи понимайте в этом узком смысле». The surrounding lines still say that in broader textual discussion 句 can mean a passage, and that context sometimes justifies «предложение». This matches JMdict 1243940 s.1-2: the narrow-label instruction concerns the linguistic/title sense and does not contradict the broader sense. The example «именная группа» (名詞句) still follows. No regression.
O1 - resolved (optional). words/くるくる.md:36 now reads «Предмет может вращаться на одном месте, никуда не перемещаясь,». It flows into «поэтому くるくる само по себе не означает движения по маршруту» with correct grammar.
O2 - resolved (optional). words/ころころ.md:20 now reads «Он то и дело говорит то одно, то другое.» It translates 言うことがころころ変わる naturally, and the Japanese and kana are unchanged.
O3 - resolved (optional). words/だらだら.md:15 now reads «течёт не переставая — струйками или ручьями». This agrees with the title «литься ручьём» and the example «пот лил ручьями», and still fits JMdict's trickling sense.
O4 - optional, declined. I accept the rationale: these are weak overlaps also present in EN, not RU-specific defects.
O5 - optional, declined. I accept the rationale: the title is concise and the sense is kept in the body.

Optional: none new.
Limits: Only the changed passages and the reconciliation were rechecked. The unchanged content stands on the first-pass review of 0501fab, with that review's limits (Ожегов from reviewer knowledge; title screen by stem plus targeted semantic list).
