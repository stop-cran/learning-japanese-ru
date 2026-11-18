# Batch 178 — recheck of fix commit `5731eb5`

## Snapshot
- Fix commit `5731eb5` ("Fix batch 178 review findings"); its parent is `43f30e7`, the candidate reviewed earlier.
- 12 files changed: 11 `words/*.md` and `manifest.json`; 25 lines added and 25 removed. No other files.
- RU working tree clean. No `__pycache__` was created; the only file written is this report.

## Scope
- `git diff --word-diff` 43f30e7..5731eb5 over every changed passage, read in context.
- `manifest.json`: the sha256 of each of the 11 changed blobs at `5731eb5` is present in the manifest.
- Each new exclusion target (中心, 支給, 然る) exists as a RU word card.

## Reconciliation

| Item | Status | Note |
|---|---|---|
| F1 基地:33 English "base" | **Resolved** | Now «по-русски обе можно назвать «базой» или «основой»». No Latin text left in the line. |
| F2 区別:21 gloss with a person as subject | **Resolved** | «различить невозможно; разницы не видно» is impersonal and agrees with the next sentence. |
| F3 副作用:35 ungrammatical sentence | **Resolved** | «Выражение «побочный эффект» по-русски употребляют и в переносном смысле — о последствиях решений; …» is grammatical. |
| Q1 幹–中心 | **Resolved** | 幹 `quiz_exclusions` now ends with `骨, 中心`, and the 中心 card exists. |
| Opt 台:32 | Resolved | «температура тридцать с лишним градусов» is natural. |
| Opt 同一:18 | Resolved | «Эти две вещи — один и тот же продукт.» |
| Opt 寅:24 / 卯:24–25 | Resolved | «значения в шестидесятилетнем цикле»; the base-60 reading is gone. Phrasing is identical in both files and the 卯 line wrap is intact. |
| Opt 地盤:21 | Resolved (see N1) | «опору кандидата в избирательном округе» matches Daijisen sense 3, but adds a second «опору» to the sentence. |
| Opt 副作用:16 | Resolved | «меня стало клонить в сон» shows the onset. |
| Opt 発行–支給 | Resolved | `[出す, 支給]`; the 支給 card exists. |
| Opt 同様–然る | Resolved | `…, そんな, 然る]`; the 然る card exists. |
| Opt 副作用: Japanese figurative sense | **Withdrawn** | Declining it is accepted. It is content beyond the EN source, so not a defect. |

## Regression check
- **N1** — optional polish, non-blocking — `words/地盤.md:21`
  - Issue: the sentence now reads «основу, опору, в том числе политическую базу поддержки, опору кандидата в избирательном округе». «Опору» appears twice. It is grammatical and the meaning is right, but it reads repetitively.
  - Optional fix: «…в том числе политическую базу поддержки кандидата в избирательном округе», or replace the first «опору» with «фундамент».
  - Confidence: high that it is stylistic only.
- 寅/卯: «Чтение かんし зафиксировано для этого значения в шестидесятилетнем цикле» is slightly compressed but clear. Not a defect.
- No new Latin text, broken links, or changes to Japanese strings or readings in any changed passage. Front matter stays valid; only the exclusion lists were extended.
- **Manifest:** only `contentVersion` and the 11 hashes of the edited word files changed. Each new hash equals the sha256 of the blob at `5731eb5`.

## Final verdicts
- **Correctness: CLEAN**
- **Scoped coverage: CLEAN.** No EN content dropped. The declined addition is outside EN scope.
- **Comprehensibility: CLEAN.** F1–F3 are resolved; N1 is optional polish.
- **Quiz safety: CLEAN.** Q1, 発行–支給 and 同様–然る are now guarded.

## Limits
- The app quiz pool and build were not run. Quiz safety rests on reading the titles and exclusions by hand.
- Only the delta 43f30e7..5731eb5 was re-read. Unchanged passages keep the verdicts from the first review.
- The author report and the intake rationale were not read.

## N1 follow-up (commit `a414b65`, parent `5731eb5`)
- Diff 5731eb5..a414b65 touches two files: `words/地盤.md` (one line) and `manifest.json` (two lines).
- 地盤:21 now reads «…в том числе политическую базу поддержки кандидата в избирательном округе.» The only text change is the removal of «, опору». The phrase is grammatical, the duplicate «опору» is gone, and the meaning still matches Daijisen sense 3. Nothing else in the file changed: front matter, Japanese text, readings and links are untouched.
- Manifest: only `contentVersion` and the `words/地盤.md` hash changed. The new hash equals the sha256 of the 地盤 file at `a414b65`.
- **N1: Resolved.**
- **Final verdicts unchanged:** correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety CLEAN.
