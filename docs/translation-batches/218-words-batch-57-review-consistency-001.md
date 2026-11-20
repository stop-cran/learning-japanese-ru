# B218 consistency and quiz-safety review (218-words-batch-57)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `4cc28f4411ca8c4cc1d94c5a7cfc02e25752f746` (tree `b193110e748f6063dcdcc5a24c49e17bffecd066`),
> the signed candidate pushed before review.
> Later reconciliation is in `218-words-batch-57-recheck-001.md`.

Snapshot: 4cc28f4411ca8c4cc1d94c5a7cfc02e25752f746 (clean tree; parent 6591e0e). Nothing was modified, staged or run through a generator.

Scope: facets consistency, quiz safety, and scoped cross-file coverage.
- I read all 30 new word cards in full: 倒す 修理 修正 信じる 信用 信頼 保証 価値 例え 作物 作法 作曲 作品 余分 何時か 何とか 何でも 何で 体育 住民 住宅 伝統 会員 休暇 休憩 企業 任せる 仲間 仲 以来.
- I read all 26 navigation-only diffs in full (3 kanji, 23 words).
- I read manifest.json and checked the intake JSON paths only.
- Reviewer model: not verifiable.

Verdicts:
- Consistency: CLEAN.
  - The 26 nav diffs are byte-identical to their parents apart from restored batch-target links, and the 31 links match the frozen EN positions and path forms.
  - The manifest delta (30 added, 26 changed) equals the content-diff .md set. Hashes of all changed files match the committed blobs. There are no removed entries and no disk/manifest mismatch.
  - The intake JSON lists exactly the 56 content paths and adds no learner content.
  - Front-matter keys and headings match EN.
- Scoped coverage (cross-file integration): CLEAN.
  - Missing links to 余る, そのうち, メンバー and 今後 are correct, because those target files do not exist.
  - There is no RU file where EN links a batch target and the link is missing.
- Quiz safety: NEEDS FIX for 例え.md and 任せる.md (both minor). All other cards are CLEAN.

Findings:
1. Minor; quiz safety; words/例え.md line 9 (quiz_exclusions).
   - Claim: the RU title «пример (для пояснения); образное сравнение» contains «сравнение», which is the entire title of 比較. JMdict 例え sense 2 is "simile; metaphor; allegory; fable; parable", and «сравнение» is the Russian term for a simile.
   - Impact: in a Russian-gloss quiz the labels are ambiguous. The EN titles did not overlap, so this is RU-introduced.
   - Remedy: `quiz_exclusions: [例, 比較]`, which adds 比較 to the current [例] (to be checked against the 比較 card's own list). Then regenerate the manifest.
   - Evidence: the card title and the 比較 title. Confidence: medium.
2. Minor; quiz safety; words/任せる.md line 10 (quiz_exclusions).
   - Claim: the RU 頼む card title is «просить; поручать», and «поручать» is close to 任せる «вверять (дело)». JMdict 頼む has the sense "to entrust to". EN 頼む is "request", so this overlap is RU-introduced.
   - Remedy: `quiz_exclusions: [預ける, 頼む]`.
   - Confidence: medium.

RU-added exclusion guards (beyond EN). Each was checked against the displayed titles and a dictionary sense.
- 倒す→勝つ: required. The 倒す title contains 勝つ's whole title «побеждать». JMdict 倒す has the sense "defeat". It also adds a link, which is fine.
- 修正→直す: required. JMdict 直す has the sense "to correct", and 修正する is "correct/amend". It also adds a link, which is fine.
- 作法→礼儀: required. «правила этикета» overlaps 礼儀 «этикет; правила вежливости».
- 作品→曲: required. «художественное произведение» overlaps 曲 «музыкальное произведение»; the card body mentions music.
- 住宅→自宅: required. «жильё» overlaps 自宅 «своё жильё». EN has [家,宅].
- 休暇→夏休み: required. «отпуск» overlaps «летний отпуск».
- 休憩→昼休み: required. «перерыв» overlaps «обеденный перерыв».
None is unjustified. All other exclusions equal EN, and no existing RU or kanji card excludes a batch word.

Optional (nonblocking; each has the same lack of guard in EN or is a weak overlap):
- 休憩 (suru) «отдыхать» vs 休む.
- 何で body sense "how" vs どう.
- 住民 vs 人口.
- 作法 (さくほう sense) vs 方法.
- 会員 vs 仲間 / 委員.
- 伝統 vs 習慣.
- 体育 vs 運動.
- 仲間 vs 友達.
- 何時か: いつ/何時 exist and the card compares いつか with いつ, so an optional link to いつ.

Limits:
- Dictionary checks used the Jisho/JMdict API for 頼む, 例え, 何で and 休憩 only.
- I did not review the Russian prose for linguistic correctness, since that is outside this facet.
- tools/validate.py was not run, and neither was build_manifest.py (not allowed).
- Hashes were verified by SHA-256 of the committed blobs for the 56 changed files. The 100 stroke JSON entries do not match raw blob hashes, and this is not caused by the batch. The strokes/*.json files are untouched by it, so the likely cause is a line-ending or normalization difference in how the generator hashes them; I did not investigate.
- kanji/信.md has a pre-existing 信号 link that EN lacks. It is not a batch change.
