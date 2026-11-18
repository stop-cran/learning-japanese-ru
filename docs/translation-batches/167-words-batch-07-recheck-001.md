Snapshot: RU learning-japanese-ru branch full-ru-167-words-07 @fa12b59 (fix commit on top of reviewed 1d2c5b6); worktree clean, no uncommitted changes.
Scope: Recheck of the complete diff 1d2c5b6..fa12b59. It touches 6 files: words/ぐにゃぐにゃ.md, 似合う.md, 単純.md, 安易.md, 浮く.md (one line each) and manifest.json. I checked each changed line in context and confirmed that every added exclusion target has an RU word page (楽, 易しい, いい, べちゃべちゃ). For the 5 changed files, the manifest SHA-256 values match the files on disk. Not re-read: unchanged lines of the 30 articles, which are byte-identical to the reviewed 1d2c5b6. Reviewer: same Claude-based reviewer as the initial review.
Verdicts: correctness CLEAN; scoped coverage CLEAN; Russian comprehensibility CLEAN; quiz safety CLEAN.
Findings:
F1 (安易–楽): resolved. words/安易.md:9 is now `[易しい, 容易, 簡単, 単純, 適当, 粗末, 軽い, 楽]`, which is the exact remedy. No regression.
F2 (単純–易しい): resolved. words/単純.md:9 is now `[簡単, 易しい]`. No regression.
F3 (似合う–いい): resolved. words/似合う.md:9 is now `[適する, 合う, いい]`. No regression.
F4 (ぐにゃぐにゃ–べちゃべちゃ): resolved. words/ぐにゃぐにゃ.md:8 now adds べちゃべちゃ. Keeping the title was one of the two remedies I offered, and the guard closes the identified overlap. No regression.
Optional items:
- 浮く example: resolved. Line 20 now reads «Древесина держится на воде.» It is a correct rendering of 木 as a material and keeps the generic present tense; no regression.
- そっと–静か guard: optional; declined, and I accept that. It was never established as a defect.
- 単純 title qualifier: optional; declined. The author's rationale (keeping it distinct from 簡単) is reasonable, and the body covers the wider use.
- Pre-existing unlinked mentions (易しい, 苦しい, kanji/示): optional; deferred to a separate navigation sweep. They were outside this batch's restoration diff.
New findings: none.
Optional: none beyond the above.
Limits: Initial-review limits still apply. In particular, the quiz distractor-selection logic was not inspected, and the intake JSON was not audited. I did not re-run the title screen tool, because the titles are unchanged; only exclusion lists changed.
