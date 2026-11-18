# Batch 185 (185-words-batch-24) — recheck 1

## Snapshot
- RU repo `learning-japanese-ru`, branch `full-ru-185-words-24`, fix commit `d6deb71` (parent `60c84eb`, the reviewed candidate). Worktree clean before and after recheck.
- Reviewer: same independent blind reviewer as the initial review; author rationale, batch/draft docs and tracking JSON not read.

## Scope
- `git diff 60c84eb d6deb71`: 4 files, 7+/7−.
  - `words/高価.md` line 9: `[高い]` → `[高い, 大切, 大事]`
  - `words/食物.md` line 9: `[食べ物, 食料, 食料品]` → `[食べ物, 食料, 食料品, 食事]`
  - `words/駐車.md` line 9: `[駐車場]` → `[駐車場, 止める]`
  - `manifest.json`: `contentVersion` + the three hashes above only.
- No other text, file or link changed. No generated/cache files committed.
- Manifest: the three SHA-256 values equal `Get-FileHash` of the committed files, and an in-memory `build_manifest(root)` (tools/build_manifest.py, not written to disk) equals the committed `manifest.json` exactly, including `contentVersion`.

## Verdicts
| Facet | Verdict |
|---|---|
| Correctness | CLEAN |
| Scoped coverage | CLEAN |
| Comprehensibility | CLEAN |
| Quiz safety | CLEAN |

## Findings reconciliation
| ID | Status | Note |
|---|---|---|
| F1 高価 → 大切, 大事 | resolved | exact proposed line applied |
| F2 食物 → 食事 | resolved | exact proposed line applied |
| F3 駐車 → 止める | resolved | exact proposed (conservative) line applied |
| Opt 空–からから | optional (declined, accepted) | card reading そら; から reading not taught; low risk |
| Opt 骨折–折れる | optional (declined, accepted) | 骨折 article does not teach 折れる; not a defect |
| Opt 騒ぎ–騒音/音 | optional (declined, accepted) | noise sense of 騒ぎ not established (Jisho: "uproar; disturbance") |
| Opt かぎり–間 | optional (declined, accepted) | weak, unestablished |

## Regression screen
- All targets exist (大切, 大事, 食事, 止める).
- `word_title_screen.py 高価 食物 駐車`: every flagged stem overlap is now either guarded (大切, 大事, 高い, 食べ物, 飯) or a false positive — «дорог-» = "road" (道, 坂, 渋滞, カーブ), «парко-» in ほかほか «с парком» (steam), and 高速 «высокая скорость» vs «высокой цены» (shared «высок-», different meaning; no ambiguity).
- The new guards remove only semantically overlapping distractors; each card keeps a large pool of unrelated candidates, so no fallback/starvation risk is introduced.
- No new defects found.

## Optional
- None beyond the four declined items above, which remain optional and do not block.

## Limits
- Recheck limited to the fix diff and its quiz consequences; the 30 articles were not re-read (unchanged since the initial review).
- No native Russian speaker check; full JMdictDB not consulted (password-gated); Jisho used.
- Quiz necessity remains a reasoned judgement; live distractor frequency not measured.
