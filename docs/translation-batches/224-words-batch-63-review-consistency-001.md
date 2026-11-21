# B224 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `49a8838b1abf3b83582d77fc211ea3915cbf700e` (tree `53bc3a1a7f1ada5c3e8156209e43a4f516946c34`),
> the signed candidate pushed before review.
> Later reconciliation is in `224-words-batch-63-recheck-001.md`.

Snapshot: RU 49a8838b1abf3b83582d77fc211ea3915cbf700e, clean tree (`git status --porcelain` empty); EN frozen 6af98cb. No edits, staging or generator runs.
Scope: consistency + quiz safety + cross-file integration for 224-words-batch-63. Read in full: all 30 new cards, all 15 navigation diffs (`diff -U0`), manifest hashes (read-only), intake JSON (path list and content check only). Reviewer model not verifiable by me.
Verdicts:
- Consistency: CLEAN
- Quiz safety: CLEAN (one optional guard recommended, below)
- Scoped coverage / comprehensibility / translation fidelity: not assigned (other facets)

Checks performed
- `python tools/validate.py`: 0 errors.
- Manifest: SHA-256 of all 3373 words/ entries matches the files on disk (0 mismatches).
- Intake: 45 payload paths = the 45 words/ files in the candidate diff (47 files total = 45 + manifest.json + intake). The intake holds only hashes and metadata; no learner content. `held` is empty.
- Navigation: each of the 15 files changes exactly one line, wrapping the existing word in `[X](X.md)`. Positions match EN for all 16 occurrences (単なる links only the first ただ; 実は links the first ところで and keeps the reading; 単に links ただ and たった). No EN link is lost in any of the 45 files.
- Quiz exclusions: every EN exclusion is present in RU. All extra RU guards (pairs listed below) have a dictionary or title basis; none is unjustified.

Findings
1. Minor / quiz safety / words/どんなに.md / recommended, not blocking.
   - Claim: どんなに (title «как сильно; как бы ни») and どう («как; каким образом») share the title word «как». The card itself says Russian «как» covers both degree and manner. The author declined this pair; EN has no guard.
   - Impact: a learner could face a near-duplicate pair of labels.
   - Remedy: `quiz_exclusions: [いくら, どう]`.
   - Confidence: medium. Severity is minor because the card teaches the contrast.

Extra RU guards, judged justified (all required unless noted conservative)
- さて→ところで (conservative); しかも→更に; しきりに→しばしば (conservative, parity with EN たびたび)
- しゃべる→ぺらぺら, べらべら, おしゃべり (shared «болтать»)
- すてき→見事, かわいい; すみません→申し訳, どうも, 謝る
- ずっと→年中; せい→原因 (conservative), 悪い; そのまま→まま
- それでも→しかし, でも (conservative); それと→それから (conservative)
- ただ→だけ, ばかり, サービス (conservative); たった→だけ
- たっぷり→十分 (conservative); たまたま→たまに (conservative)
- できれば→なるべく; とにかく→何とか
- とんでもない→いえ; →ひどい, 凄い (conservative)
- どうしても→なかなか, 絶対; →ぜひ, 必ず (conservative)
- どこか→どこ, 辺り; なにも→別に (conservative)

Declined pairs, judged acceptable (titles separate them and the cards teach the contrast)
ところで–ところが, ずっと–もっと, たった–ばかり, どんなに–そんなに, できれば–できるだけ, ちゃんと–丁寧/まじめ, たまたま–ばったり, たっぷり–一杯, ただ–普通, それと–しかも, それでも–けれども, それぞれ–みんな, そのまま–すぐに, そのうち–今度, せい–おかげ/理由, すてき–きれい, しゃべる–言う, しまった–残念, ぴったり–似合う.

RU-only links (9), all justified
どんなに→どう, できれば→可能 and 必ず, それと→それとも, それでも→まだ, そのまま→まま, すみません→済む, しゃべる→黙る, しまった→しまう. Each target exists as an RU card; EN has plain mentions. ありがとう, ごめんなさい, 有料 and ともかく have no RU card, so they correctly stay plain text. The たまらない→辛い link is fine because that card teaches つらい.

Optional
- なにも–全然 and なにも–全く: JMdict なにも "(not) at all" matches 全然, and the titles share «совсем». The existing 全然 guard covers 何 but not なにも.
- ずっと–ずいぶん: «гораздо»≈«значительно», but ずっと leads with «всё это время». Weak.
- しきりに–よく (よく glosses «часто»); しまった–失敗 (неудача overlap). Weak.
- RU-added prose beyond EN, a justified adaptation: できれば adds a 可能 gloss; どんなに adds a «как» degree-vs-manner comparison with the new example どうやって作りますか. Both translate the teaching rule rather than an English-only comparison.

Limits
- Dictionary evidence came from the Jisho (JMdict-derived) API, not exact JMdict entry IDs.
- I did not inspect the app's quiz selection algorithm.
- Whole-card EN-vs-RU translation fidelity belongs to the other facets.
- Pre-existing differences from EN outside this batch, not judged: ばったり lacks two article links; ぶかぶか lacks きつい and article links; 申し訳 lacks 訳 and ごめんなさい links; 豊富 lacks the 豊 link.
- I did not read author reports, FILES title-screen outputs, or RU translation-batches/drafts/tracking beyond the permitted intake check. I ran `word_title_screen.py` myself; its output was mostly stem noise.
