Snapshot: 47741c1 (fix commit over candidate 1cb7fd3; diff 1cb7fd3..47741c1: 8 word files + manifest.json hash updates)
Scope: Recheck of findings F1-F4 and applied optional items from b165-review.md; changed passages in words/叩く, かたかた, ことこと, からから, ぶくぶく, 象, ぶうぶう, 震える and the manifest hunks. Reviewer model: Claude (independent reviewer session).
Verdicts: correctness CLEAN / scoped coverage CLEAN / comprehensibility CLEAN / quiz safety CLEAN

Reconciliation:
- F1 (叩く dust sense): RESOLVED. words/叩く.md:43-44 now attribute «выбивать пыль» to the separate entry 叩く（はたく）, matching JMdict 2829135 and leaving たたく (1416170, cited as senses 1 and 2) without the dust sense. The wording is natural, and the reading in full-width brackets follows card style.
- F2 (叩く exclusions): RESOLVED. 叩く was added to かたかた.md:8 and ことこと.md:8. Target exists.
- F3 (ことこと/からから): RESOLVED. からから was added to ことこと.md:8. Target exists.
- F4 (ичидан): RESOLVED. 震える.md:16 now reads «итидан», per the glossary in docs/translation-methodology.md:138.
- Optional applied: ぶくぶく+沸く, からから+乾く (both justified by shared «кипеть/бурлить» and «сохнуть/пересохший» glosses; targets exist); 象 hedge «хобот в обычной речи называют просто 鼻» is accurate and grammatical; ぶうぶう «Какая сцена имеется в виду, понятно по подлежащему и контексту.» is natural. All accepted.
- Optional declined: 鳴る guard (ごろごろ precedent), 者 «перезвонит», 研究→kanji/者 (pre-existing). These are nonblocking, and declining them is acceptable.

Regression check: Only front-matter quiz_exclusions lines and the quoted prose lines changed; titles, Japanese text, readings, links and other front matter are untouched. manifest.json changes are only contentVersion and the hashes of the 8 edited files. validate.py: 0 errors (no __pycache__ left). Working tree clean.

Findings: none.

Optional: 鳴る «звенеть; звучать» remains unguarded against がちゃがちゃ/がたがた/かたかた (declined, precedent-based); 研究.md lacks the EN link to kanji/者 (pre-existing, out of scope).

Limits: No native Russian speaker review. I did not recompute the manifest hashes; I relied on the validator and the diff showing only the edited files' entries changed. Recheck limited to the 1cb7fd3..47741c1 diff; the rest of the batch keeps the first review's verdict basis.
