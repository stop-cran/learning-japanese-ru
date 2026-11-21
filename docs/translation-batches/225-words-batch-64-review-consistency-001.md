# B225 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `56996a024ba2641a8d5e846d8c63e1981beeccff` (tree `cec94999a3e5496f49132267a073e5e56aa92d24`),
> the signed candidate pushed before review.
> Later reconciliation is in `225-words-batch-64-recheck-001.md`.

Snapshot: RU repo branch full-ru-225-words-64, commit 56996a024ba2641a8d5e846d8c63e1981beeccff (clean tree, committed content only); EN frozen 6af98cb.
Scope: consistency, quiz safety and cross-file integration of the 30 new word cards, the 10 navigation-only link edits, manifest.json and the intake JSON. Reviewer: single reviewer (no sub-reviewers); read-only.
Verdicts:
- Consistency/integration: CLEAN
- Quiz safety: CLEAN (two optional, low-confidence notes)
- Scoped coverage: CLEAN (all EN links/exclusions retained; omissions are explained by absent RU targets/images)
- Comprehensibility/correctness: not assessed (other reviewers' facets)

Findings: none actionable.
Checked and found consistent:
- Navigation: all 10 diffs are one-line bracket additions; each matches the single linked occurrence in the EN source (すみません has two links on one line, すやすや wraps the first ぐっすり, as EN does). Intake's "eleven links in ten files" agrees.
- Front matter: all 30 cards equal EN apart from title; every EN quiz_exclusions entry is retained; これら, お, うがい, いわゆる have none in EN either.
- Links: all card-to-card links resolve. EN links omitted in RU have absent RU targets (kanji/漱, kanji/麓, two onomatopoeia articles) and are plain text. ぐっすり omits EN image/image_scene, consistent with RU convention (almost no RU word cards carry images).
- One extra RU link: ごめんなさい→申し訳. It is substantive, the target exists, and it matches the new guard; acceptable.
- Manifest: all 40 added/changed words/ entries match the SHA-256 of the files on disk; no stale word entries anywhere; only contentVersion plus those entries changed. Intake payload paths equal the 40 changed words/ files exactly and add no learner content. Hashes were verified without running the generator.
- H1: いただきます H1 ("перед началом еды") differs from its title, mirroring EN's own H1/title split ("before starting a meal"); not a defect.
- RU-added exclusions (all justified by shared label tokens or a taught sense): こんなに→そんなに/それほど/あんなに; きつい→狭い/急激; おめでとう→お祝い/祝う/祝い/希望; うなる→吠える; いけない→不可/禁止; ありがとう→感謝; 鳴らす→掛ける; あんまり→別に; あっ→しまった; あいにく→残念; いただきます→ありがとう/いただく; ごめんなさい→申し訳; こんにちは/いらっしゃい→あいさつ; いらっしゃい→寄る; あらゆる→様々. The last group (あいさつ, 寄る, いただく, 希望, 様々, 祝い) is conservative: a real basis exists but necessity is not established; retaining them is harmless. None is unjustified.
- Declined pairs judged acceptable (distinct labels or incidental shared morphemes): これら–これ/この, きつい–鋭い/苦しい/強い, かわいらしい–すてき, かもしれない–多分/おそらく, お互い–両方, あらゆる–一種, いつまでも–いつも/ずっと, and the stem-only screen hits.
Optional:
- ごめんなさい–謝る: すみません→謝る exists as precedent; consider adding the guard (low severity, the POS contrast is already taught in the card).
- ごめんなさい–許す (RU label «позволять; прощать» vs title "простите меня" shares the verb прощать); low confidence, not required.
- あっ–まあ: only incidental "ах" overlap; no action needed.
Limits: EN prose was compared line by line only for the first 8 cards (ごめんなさい…かもしれない); the other 22 were compared by script on front matter and links only. Dictionary senses are cited from memory of JMdict glosses, not re-fetched. validate.py was not run (not asserted to be read-only). Correctness and comprehension are outside this facet.
