# B223 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `13805217f9159dadc5849e7e0060bfbc1d2ffc4a` (tree `4ad1f061cda9d497acf9fc7d5c8b5856d91b254b`),
> the signed candidate pushed before review.
> Later reconciliation is in `223-words-batch-62-recheck-001.md`.

Snapshot: 13805217f9159dadc5849e7e0060bfbc1d2ffc4a (clean tree; `git status --porcelain` empty) vs base 8a759e5a. 39 files: 30 new cards, 7 link restorations, manifest.json, intake JSON.
Scope: consistency, quiz safety and cross-file integration of batch 223 (words batch 62). Blind: no author reports/title-screen outputs in FILES/docs batches/drafts/tracking/scratch worktrees read. Actual reviewer model: not verifiable from inside the session (stated limit). Read-only; no generator run (validate.py run read-only: 0 errors).
Read in full: all 30 RU cards against the EN originals in learning-japanese-en-frozen; the 7 navigation diffs (-U0, full changed lines); RU quiz/link rules in content-structure.instructions.md.
Programmatic: front matter (all fields except quiz_exclusions identical to EN); link parity; exclusion superset; manifest sha256 for all 37 changed/new non-manifest files (0 mismatches; 4804 entries); own title-overlap screen over all RU word titles.

Verdicts:
- Consistency: CLEAN
- Quiz safety: CLEAN
- Scoped integration (links, manifest, intake): CLEAN
(CLEAN = no actionable defect established within scope, not exhaustive correctness.)

Findings: none established.

Evidence summary:
- Every EN quiz exclusion is retained on every card. Direct pairs only, no transitive cliques.
- Links: all RU targets exist. EN links to targets absent in RU (オーバーコート, インキ, 墨, ところで, えっと, ちゃんと) stay plain text per convention. Kanji link 付 exists.
- Navigation diffs: each changes only bracket/href at one EN-link position (ざっと→きちんと, ふと/思わず→わざと, テント→キャンプ, ワイン→ウイスキー, 万一→もしも line 28 = EN line 32; 万一 line 34 mention is unlinked as at EN 39, 流れる→インク). Paths in `X.md` form.
- Six RU-only links (クリーム→アイスクリーム, エネルギー→活気, まさに→ちょうど, まさに→もうすぐ, まあ→あ, くっつける→結婚): each sits on a substantive comparison sentence in the RU body; acceptable.
- Manifest: all 37 hashes match file bytes; no unrelated files. Intake JSON has keys baseline/batchId/held/notes/payloads/schemaVersion/sourceCommit; checked only for the absence of learner prose (Cyrillic body text absent); the path list was not compared entry by entry beyond that.

RU-introduced guards (classification; dictionary basis JMdict senses reflected in the titles):
| Card→excluded | Class | Basis |
|---|---|---|
| クラシック→音楽 | required | «музыка» is the generic head of the title «классическая музыка» |
| オーバー→越す | required | 越す «превышать» vs «превышение (предела)» |
| オーバー→越える | conservative | 越える exceed-limit sense; plausible answer |
| エネルギー→活気 | required | both titled «энергия» |
| エネルギー→余裕 | conservative | «запас сил» vs «запас (… сил)» |
| ウイスキー→酒, お酒 | required (precedent) | ビール/ワイン already guard both on the same generic-label basis |
| やや→少々 | required | parallel to EN guards 少し/ちょっと/多少; all «немного» |
| だけど→でも | required | both «но» |
| もしも→もし | required | «а если» ≈ «если» |
| まるで→ちっとも | required | parallel to 全く/全然/少しも; «совсем не» |
| まさに→もうすぐ | required | shared «вот-вот» |
| まさに→すなわち | conservative | «именно» vs «а именно» |
| まあ→あ | conservative | «ах!» vs あ interjection |
| そっくり→似る | required | «похожий» vs «быть похожим» |
| そっくり→全体 | required | shared «целиком» |
None unjustified. Reverse pairs are covered where the existing card already excludes the new one (ところが/だが, なぜなら/だって).
Pairs checked and deliberately left unguarded (agree): キャンプ/テント (no gloss overlap), キャプテン/チーム, オーバー/限界, わざと/偶然 (antonym taught), わざと/つもり/意思, アイスクリーム/クリーム (EN guard sits on クリーム), クリーム/バター, きちんと/丁寧 (partial «аккуратно» vs «тщательный», different part of speech, EN has none), やや/くらい etc. (stem «степени» only), まるで/真っ赤, くっつく/態度, 浮く.

Optional:
- アイロン: RU dropped EN's first bullet example (シャツにアイロンをかけました。; now only in prose) and the closing sentence that neither sense is iron supplement/ore. Fidelity polish only; no quiz or accuracy impact.
- やや: RU dropped EN's remark on the community-source interjection identity; まさに, まあ, エネルギー title add RU-only text (もうすぐ comparison, あ/ああ, «запас сил»). All sensible additions, none contradicts EN.
- きちんと/丁寧 guard could be added conservatively; not needed.

Limits:
- Dictionary senses taken from the cards' own cited JMdict entries and titles; no fresh online dictionary check for correctness (correctness is another reviewer's facet).
- Part of my title-screen output was machine-generated lexical overlap (stem noise); judged manually.
- Intake JSON path list not compared entry-by-entry with the diff.
- No device/app quiz run.
