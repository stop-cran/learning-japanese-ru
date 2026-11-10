# Batch 140 Independent Review 001

- Reviewer: `ru-b140-reviewer` (read-only)
- Scope: `kanji/育.md`, `kanji/背.md`, `kanji/能.md`, `kanji/腹.md`, `kanji/舞.md`, `kanji/船.md`; `strokes/育.json`, `strokes/背.json`, `strokes/能.json`, `strokes/腹.json`, `strokes/舞.json`, `strokes/船.json`; `words/背中.md`, `words/船.md`, `words/教育.md`, `words/育てる.md`, `words/背.md`, `words/背広.md`, `words/お見舞い.md`; batch-140 pre-mutation records.
- Frozen source baseline: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`

## C1 — Japanese correctness / scope fidelity

**CLEAN WITHIN REVIEWED SCOPE.**
Reviewer reported that Japanese forms/readings/examples/metadata for six lessons match frozen source scope; six stroke files are byte-identical to frozen source; reviewed word-page edits are navigation-only.

## C2 — Dependencies / quiz semantics

**CLEAN WITHIN REVIEWED SCOPE** for link/dependency edits.
Reviewer confirmed added wrappers target newly present kanji lessons and optional wrappers to absent word pages were removed per amendment scope.

## C3 — Russian comprehensibility

**NEEDS FIX (bounded).**
`kanji/舞.md` wording “движение чего-то в воздухе по спирали” was judged too narrow versus source “turning through the air.”
Requested fix: remove the spiral-specific narrowing and keep broader motion phrasing.

## Residual UNVERIFIED

- Direct negative/fallback quiz safety remains **UNVERIFIED** for all 18 directions:
  `育→背/青/有`, `背→育/北/青`, `能→育/背/北`, `腹→服/朝/背`, `舞→年/毎/足`, `船→服/朝/台`.
- Native-speaker naturalness and universal frequency claims remain **UNVERIFIED**.

## Overall verdict

**BLOCKED** pending the single C3 wording correction in `kanji/舞.md`.
