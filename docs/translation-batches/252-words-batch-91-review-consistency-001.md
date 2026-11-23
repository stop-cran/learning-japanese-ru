# B252 consistency and quiz-safety review (blind, read-only)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `ac62348651051d98995df3cb458c512a93488d4f` (tree `3265cdbc606c1dda0bb1e974126e789e9c8398dc`),
> the signed candidate pushed before review.
> Later reconciliation is in `252-words-batch-91-recheck-001.md`.

## Snapshot
Candidate `ac62348651051d98995df3cb458c512a93488d4f` in `learning-japanese-ru`. HEAD matches. `git status --porcelain` is empty before and after. `python tools/validate.py` reports 0 errors. No `__pycache__` was created (verified).

## Scope
Read in full: the 30 new word cards and the diffs of the 9 navigation-only files (`kanji/停.md`, `kanji/各.md`, `words/下降|派手|潰れる|火山|無限|突く|転々.md`). I compared them against frozen EN and read the intake JSON for path parity, hashes and absence of learner content only. I did not read the author reports, the title-screen output, the reviewer reports or the translation-batches, translation-drafts and tracking files (apart from the intake JSON). Model identity is not verifiable. I ran my own title screen, but it was only partly triaged (see Limits).

## Verdicts
- Structure and front matter vs EN: PASS. All 30 cards are identical to EN apart from the translated `title`.
- Nav restorations: PASS. 17 link occurrences, byte-identical apart from the link brackets and hrefs. Line numbers match EN.
- Links: PASS. Nothing is broken. The dropped EN links all point to cards that are absent in RU. The RU-only links 断水→停電 and 地味→派手 are justified.
- Footers and source URLs, entry IDs and sense numbers: PASS. They equal EN. No RU-only source was added.
- EN quiz_exclusions retained: PASS. All are present, in EN order, with the RU additions appended.
- RU-added guards: PASS with notes. 22 guards were added; none is unjustified. See the classification below.
- Missing guards: one finding (F1).
- Manifest: PASS. It is current (see Limits).
- Intake JSON: PASS. The 39 payload paths equal 30 cards plus 9 nav files. The hashes match, `held` is empty, and there is no learner content.
- Titles: PASS with optional polish (O1–O3).

## Findings

### F1 — Missing guard 為替 ~ 翻訳 (Medium, confidence medium)
- `words/為替.md:9` has `quiz_exclusions: [両替, 交換, 換える, 替える, 案, 通貨]`.
- The 為替 title segment «денежный перевод» (line 12) shares the bare word «перевод» with `words/翻訳.md`, whose title is «перевод». EN has no such overlap. It is RU-introduced homonymy that makes a learner-visible wrong answer ambiguous.
- Remedy: change line 9 to `quiz_exclusions: [両替, 交換, 換える, 替える, 案, 通貨, 翻訳]`. Alternatively, drop the bare «перевод» from the title. The body already says «Перевод — денежный, а не текста» (為替:43).

### F2 — Unguarded in-batch pairs (Low, confidence medium; no action required)
These pairs share only a topic, with no shared title segment: 停電~断水, 停車~停電/断水/不通, 無数~無地, 点く~点々, 灯油~灯台, 灯台~オイル, 火口~火傷 and 濁る~濃度. EN has no guards for them either, so I judge guards unnecessary. 停電↔断水 are explicitly contrasted in the body and each links to the other. If a guard is wanted anywhere, 断水→停電 is the only candidate.

### RU-added guard classification
Dictionary basis was taken from the sense IDs cited in the footers, which equal EN. I did not look up JMdict independently.
- Required: 停止→停留所 (bare «остановка»); オイル→バター («масло»; the オイル/油 pair is already guarded); 一通り→そっくり (segment «целиком»).
- Conservative (real basis, necessity unestablished; keep):
  - 停車→停留所, 駐車, 駐車場, 立ち止まる, 終点
  - 停止→止む
  - 無沙汰→久しぶり, 黙る
  - 地味→謙遜
  - 各地→全国
  - 一通り→おおざっぱ, 完全, セット
  - 平凡→日常
  - 為替→通貨
  - 潰す→殺す («убивать время»)
  - 潜る→水中
  - 漢和→漢字, 日中
- Unjustified: none. The extra guards cost only a little distractor variety.

## Optional
- O1: the 無沙汰 title segment «давно не давать о себе знать» is a verb phrase inside a noun title. The ご register is already signalled in the body.
- O2: the 潜る title «уходить под воду» is stilted. «нырять» would be natural, and its closest card 飛び込む is guarded.
- O3: the 為替 «валютный обмен» is narrower than the EN «financial exchange». The 無地 «однотонный» could imply a single colour, though the body clarifies it. 点々 mixes an adverb and a plural noun.
- Pre-existing, outside the batch: `words/火山.md:23` has a mismatched bracket «（かこう, кратер)». `kanji/各.md` keeps 各々 and 各自 plain because the targets are absent. The 火傷 tag `suru` vs the vocabulary `suru-verb` is inherited from EN.

## Limits
- I accidentally ran `python tools/build_manifest.py --help`. It executed the generator and printed `manifest.json: 5679 files, version 42a30cef229b3b48`. `git status` stayed empty afterwards, so the manifest is byte-identical and current. No diff resulted.
- The title screen was only partly triaged. Exact segment hits (停止~ストップ, 停止~停留所, オイル~油) are guarded. I reviewed the stem-only rows by spot checks and targeted lookups of 翻訳, 射す, 英和, 澄む, 被害, 乾く, 割合, 久しぶり, 日常 and 通貨, not exhaustively. 点く~射す, 濁る~澄む and 漢和~英和 showed no shared segment.
- Dictionary senses were not independently looked up.
- Other model-reviewer outputs were not consulted, by design.
