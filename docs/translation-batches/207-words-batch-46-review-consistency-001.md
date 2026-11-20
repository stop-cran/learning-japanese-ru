# B207 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `ec1539c9b30591d1c207da84d96fa008d29c8e80` (tree `612e941814aefda3a8cbcf6072c15b22ba72bae2`),
> the signed candidate pushed before review.
> Later reconciliation is in `207-words-batch-46-recheck-001.md`.

Snapshot: RU primary checkout, HEAD = ec1539c9b30591d1c207da84d96fa008d29c8e80 (confirmed). `git status --porcelain` was empty before I started. After my `python tools/validate.py` run it shows only `?? tools/__pycache__/`, which the validator created (untracked, not part of the candidate). Nothing else changed. I ran no generator and no git write command.

Scope: I read in full all 30 new word cards (front matter and body) against their frozen-EN front matter and link sets. I also read in full all ten navigation diffs (kanji/抜, 抱, 術; words/叩く, 攻撃, 替える, 有利, 苦しむ, 評価, 震える). I checked manifest.json (diff and per-file hashes) and the intake record (paths and hashes only). I screened all 30 titles and exclusions against all RU word titles, including every title listed in the prompt. Facets: consistency and quiz safety. Model: not verifiable.

Verdicts:
- Consistency (front matter, format, links, navigation, manifest, intake): CLEAN.
- Quiz safety: NEEDS FIX. Three required-class guards are missing (F1, F2, F3); optional items are listed below.

Checks behind the consistency verdict:
- `validate.py`: 0 errors.
- Front matter matches EN field for field (same key order, tags, kanji, type, jlpt) in all 30 cards. The only differences are 交換 (+代わり) and 扱う (+操作) in `quiz_exclusions`.
- All 30 have the 4 sections in order: Значение, Как сочетаются кандзи, Синонимы и антонимы, Оттенки значения.
- No Russian-only links: RU links are a subset of EN links in every card. Every RU link target exists.
- EN links omitted in RU all point to targets with no RU file: kanji/損, 換, 替, 扱; words/利益, 広告, 勧める, 取れる, 処理; articles/kaeru-change-replace-and-return.md. They are correctly left as plain text (per the repository convention in the review prompt).
- Navigation: all ten diffs are bracket and href changes only at existing mention positions (3 hunks each in the kanji files, 1 in each word file). No prose changed. Reciprocal links are present (有利↔不利, 苦しむ→我慢, 評価/叩く/攻撃→批判, 震える→振る, 替える→換える).
- Manifest: contentVersion and exactly 40 file entries changed (30 new, 10 nav). All non-strokes entries match actual file sha256. 118 `strokes/*.json` entries differ from raw bytes of the working tree. These files are untouched by the candidate and the mismatch is pre-existing (autocrlf=true working tree), so it is not a defect of this batch.
- Intake record: its 40 payload paths equal the content diff paths exactly. The candidateRawSha256 values match the files. It holds only hashes, paths and a note; no learner content.
- Every EN `quiz_exclusions` entry is retained: 損, 交換, 換える, 掴む, 振る, 指す, 持ち上げる, 抱える, 抜ける, 抜く, 批判, 戻す.
- No new title equals another card's whole title.
- Shared-segment overlaps were screened. 損/損害 (убыток), 換える/取り替える (обменивать), 指す/示す (указывать) and 抜く/引き出す (вытаскивать) are guarded. 抜ける/降る «выпадать» carry different qualifiers (о зубах, волосах / об осадках), so no guard is needed.
- No other title contains a «мы» segment, so 我々 is safe. Nothing in the batch uses a bare «держать», «объявление», «арест» or «операция» segment.

Findings:
- F1; medium (learning impact: a defensible wrong-answer collision in the quiz); quiz safety; words/交換.md line 11 (`quiz_exclusions`) or words/両替.md front matter.
  - Claim: 交換 «обмен; замена одного другим» vs 両替 «обмен валюты; размен купюр» have no direct exclusion on either side.
  - Impact: «обмен…» is a defensible correct answer for 両替. The EN file pairs 換える with both words but not 交換–両替, and the Russian titles make the collision closer than the EN ones.
  - Remedy: change 交換 to `quiz_exclusions: [取り替える, 代わり, 両替]` (or add `quiz_exclusions: [交換]` to 両替).
  - Evidence: JMdict 両替 (1553820) sense 1 "money exchange" shares the head noun «обмен» with 交換 (1271750) sense 1 "exchange".
  - Confidence: medium-high.
- F2; medium; quiz safety; words/掴む.md line 11 (`quiz_exclusions`).
  - Claim: 掴む «хватать рукой; схватывать (суть)» has a direct pair only with 握る. 捕まえる «ловить; захватывать» (JMdict sense "seize, catch") and 理解 «понимание» are not guarded.
  - Impact: хватать≈захватывать/ловить, and «схватывать (суть)» is the sense 掴む teaches for understanding. The 掴む article itself says 理解 overlaps with it.
  - Remedy: change to `quiz_exclusions: [握る, 捕まえる, 理解]`.
  - Evidence: JMdict 掴む 1433650: "to catch hold of; to seize; to grasp" and "to grasp (meaning)". 捕まえる: "to seize; to catch".
  - Confidence: medium. 捕まえる is the stronger case; 理解 is a verb/noun-sense collision.
- F3; low-medium; quiz safety; words/持ち上げる.md line 11 (`quiz_exclusions`).
  - Claim: 持ち上げる «приподнимать; захваливать» is paired with 上げる only. 立てる «ставить вертикально; поднимать» has the segment «поднимать», which is nearly identical to «приподнимать».
  - Impact: the repository already treats the «поднимать» collision with 上げる as requiring a guard, and 立てる's own exclusion list contains 上げる.
  - Remedy: change to `quiz_exclusions: [上げる, 立てる]`.
  - Evidence: JMdict 立てる: "to raise; to lift up".
  - Confidence: medium.
- F4; low; accuracy of internal citation (not quiz safety); words/提出.md, section «Синонимы и антонимы», first paragraph.
  - Claim: the card quotes 出す as «вынимать; сдавать», but the RU 出す title is «вынимать; выносить».
  - Impact: a mis-cited gloss. The 出す body does mention «сдаче».
  - Remedy: write `«вынимать; выносить»`, or reword to «вынимать, выносить; в обычных выражениях — сдавать».
  - Confidence: high.

Classification of exclusions beyond the EN file:
- 交換 → 代わり: basis JMdict 代わり «замена» (substitute; replacement) vs 交換 «замена одного другим» (EN title includes "replacement"). Conservative: real basis, necessity unestablished, harmless. Keep.
- 扱う → 操作: basis JMdict 操作 (operation; handling; manipulation) vs 扱う sense 1 (to handle; to deal with). In Russian «обращение с устройством» and «обращаться с вещами» are near-identical. Required. Keep.
- Nothing is unjustified.

Optional (nonblocking):
- 掲示 vs 放送 «…; объявление»: a learner may map 掲示 «объявление» onto 放送's segment. Conservative guard: `quiz_exclusions: [放送]` on 掲示.
- 手術 vs 作業 «…; операция»: «операция» is shared, but 手術 is «хирургическая операция». Low risk. Optional `[作業]`.
- 戻す «класть обратно» vs 置く «класть»: low risk, no guard.
- 我慢 «выдержка» vs 遠慮 «сдержанность»: low risk, no guard.
- Same-reading pairs 或/ある, 振る/降る, 指す/差す: titles are unrelated. Not guarded, consistent with the existing 差す and 降る cards.
- Decisions on the prompt's other open questions:
  - 換える vs 変える: no shared segment, no guard needed (the article contrasts them).
  - 抜ける vs 抜く: no shared title segment, no guard needed.
  - 握る vs 持つ: no bare «держать», no guard needed.
  - 提出 vs おつり «сдача»: «сдача на проверку» is not a bare «сдача», no guard needed.

Limits:
- Dictionary senses are cited from the article text and my own JMdict knowledge, not re-fetched.
- Quiz necessity is judged semantically. I did not run the app's quiz generator, so the Words.kt exclusion behaviour was not re-tested.
- The title-screen tool was not used (BLIND rule); I used my own segment-overlap script. Linguistic accuracy and readings are outside my facet.
