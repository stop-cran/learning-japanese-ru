# Batch 148 independent review

## Candidate and verdict

- Final candidate: `c7a0b4d2c990c29ae43c6aaf7705b3f26f1cbc95`
- Initial reviewed candidate: `f8c66d02d88cc961daedc0c2d1172cf99495531e`
- Frozen English source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`
- Published baseline: `541d6c0fbc737d0079ec41cd55f95ef4650b4ce8`
- Verdict after focused follow-up: **PASS WITH QUALIFICATIONS**

The initial read-only review found one P2 issue at `kanji/酒.md:20`: an unavailable source-word reference had been rendered as `[酒](酒.md)`, a relative self-link rather than the authorized plain Japanese text. The writer changed it to `酒 さけ` and regenerated the manifest. Focused follow-up on the final candidate confirmed the reference is plain text, the self-link is gone, the manifest hash matches, and the complete follow-up diff is exactly that one-line correction plus the generated `manifest.json` update. No issue remains.

## Scope and checks

Reviewed the ten new lessons `適, 選, 部, 都, 配, 酒, 閉, 関, 降, 限`, their ten stroke assets, and the nineteen authorized reciprocal word-link edits in `お酒, 全部, 心配, 玄関, 適当, 選ぶ, 部屋, 部長, 都, 都会, 都合, 閉まる, 閉める, 関係, 降りる, 降り出す, 降る, 降ろす, 首都`. Also reviewed `manifest.json`, the methodology/instructions update, Batch 147 search evidence, and the Batch 148 intake, semantic freeze, manifest authorization, and source-link amendments 001–003 against the corresponding frozen source lessons and assets.

- Japanese IDs, metadata, readings, examples, and direct distractor IDs align with the frozen source; mnemonic claims are framed as modern visual aids.
- All ten stroke assets are byte-identical to frozen-source assets.
- Each word-page diff is exactly its authorized one-line reciprocal link; local links resolve.
- `words/適切.md`, `words/酒.md`, and `words/限る.md` remain absent. Their authorized visible Japanese references are plain text.
- Manifest scope is exactly 20 new registrations, 19 changed existing hashes, and no removals. Hashes and final content version `7751295c874d5227` recompute.
- The Batch 147 methodology note leaves `空–遠く` and `空–遠い` at C2 **UNVERIFIED** and does not change those lessons or word pages.
- No other runtime paths or quiz/grading changes are present in the batch.

## Qualifications

All 30 direct negative/fallback directions remain **UNVERIFIED**; no transitive closure or quiz-safety inference is made. The review does not claim a fresh JMdict lookup, native-speaker frequency/naturalness validation, runtime/device/media/activation/release approval, or full translation completion.

The reviewer reported no file or Git/worktree changes. The pre-existing untracked `tools/__pycache__/` was left untouched.

## Reviewed paths

- Lessons: `kanji/{適,選,部,都,配,酒,閉,関,降,限}.md`
- Stroke assets: `strokes/{適,選,部,都,配,酒,閉,関,降,限}.json`
- Word pages: `words/{お酒,全部,心配,玄関,適当,選ぶ,部屋,部長,都,都会,都合,閉まる,閉める,関係,降りる,降り出す,降る,降ろす,首都}.md`
- Other: `manifest.json`, `.github/copilot-instructions.md`, `docs/translation-methodology.md`, `docs/translation-batches/147-sora-search-validation-qualification-001.json`, and the Batch 148 intake, semantic-freeze, manifest-generation amendment, and source-link amendments 001–003.
- Frozen evidence: the matching ten `kanji/*.md` and `strokes/*.json` files in the frozen source checkout, plus `ru-sora-search-verification-20261111.json`.

The complete initial findings and focused follow-up were sent directly to the coordinating writer by reviewer session `4e9e4dfc-9fe0-4dc9-9338-2ab429e16aba`.
