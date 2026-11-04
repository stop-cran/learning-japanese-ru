# Full Russian translation: execution after the two pilots

## Frozen scope and present state

The owner's 2026-11-04 request is to review and execute the remaining roadmap, not
another arbitrarily small pilot. The target is **every runtime object in the current
English edition**, not a claim that the English edition itself completes the JLPT syllabus.
Freeze EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f` before the next work; later English
changes are drift, not moving inputs to an in-flight translation.
RU baseline is `4d84c90f7cffa70b5ee1e296595d5cc7ce306f6f`;
app baseline is `5c000bd5596d2189ef878da572687bd01ab3bb5f`.

| Family | Frozen EN objects | Present RU objects |
| --- | ---: | ---: |
| Kanji | 1,062 | 12 |
| Words | 5,020 | 47 |
| Articles | 57 | 2, both deliberately scoped |
| Counter files | 138 | 2; legacy reverse rows deliberately omitted |
| Grammar sets | 88 | 1 |
| Curriculum catalogs | 1 | 0 |
| Word scene catalogs | 201 | 2 |
| Legacy listening passages | 36 | 0 runtime; one reviewed text draft |
| Japanese listening tasks | 40 | 0 runtime; one reviewed text draft |
| Stroke files | 1,062 | 12 |
| Word images | 398 | 3 |
| Legacy audio | 36 | 0 |
| Task audio | 128 | 0 |
| Task images | 11 | 0 |
| **Total** | **8,278** | **81** |

Thus 8,197 target paths are absent, and presence does not establish full translation:
the two articles and legacy counter unit retain explicit partial coverage. Source kanji
levels are N5 80 / N4 166 / N3 367 / N2 367 / N1 82; word levels are
N5 672 / N4 636 / N3 1,625 / N2 1,739 / N1 2, with 346 intentionally unlabelled.
Do not infer levels for those words or invent missing upstream N1 coverage.

The complete 81-object pilot stage is independently reviewed for its adopted scope;
its original sources remain A `3196c3a...` and B `5f460b8...`, not this new target.
Preserve the old provenance/review files as historical records. A new source inventory,
tracking ledger and drift report must not relabel old work as newly translated.

## Remaining work and dependency order

1. **R0 — reconcile scope and guidance.** Inventory every manifest map and every active
   instruction/agent, including changed `applyTo` and normative references. Compare the
   fresh frozen source against both pilot sources. Independent plan review precedes new
   implementation. This inventory is not linguistic approval or a synchronization tag.
2. **R1 — finish the manual provenance loop (RU #2).** Add deterministic read-only
   fixed-revision inventory/drift/checkpoint checks, with focused tests. Track added,
   changed, removed/renamed, untranslated, RU-modified and partial objects separately.
   Preserve RU-specific adaptations and immutable old receipts. Every review record binds
   exact source and Russian hashes plus evidence; matching bytes do not create approval.
   A checkpoint rejects unresolved adopted objects and guidance. Prove a reproducible
   real two-snapshot report before considering optional scheduled automation.
3. **R2 — finish or explicitly block C6 operations (RU #6).** New-cohort Word Type needs
   its real reverse prerequisite; legacy counter suffix/full typing needs a second real
   Choose day. Do not change clocks, gates or saved state. Both reviewed Russian audio
   adaptations need fresh exact-package authority before runtime publication and genuine
   playback/interruption acceptance. Prepare exact binding evidence without inventing
   approval or regenerating paid media.
4. **R3 — C7 owner-device/release acceptance.** APK `0293a7ba...`, built from app `5c000bd`,
   was copied to the physical phone and fully read back over MTP on 2026-11-04.
   This is delivery, not installation, Japanese-IME, playback or phone approval.
   Preserve the applicable API29/API35/enlarged-text/source/history acceptance matrix.
   Ordinary RU defaults remain disabled until the required gates pass.
5. **R4 — translate the complete inventory (RU #3).** After the applicable C6/C7 gates,
   execute coherent dependency-closed batches, starting with remaining N5 kanji/words,
   then N4/N3/N2/N1 and unlabelled words; complete all articles, counters, grammar and
   curriculum alongside the units they support. Scenes/media/listening are separate
   exact-package lanes, never omitted from the backlog. A batch closes required examples,
   direct negative references, prerequisites and licensed media before authoring; optional
   navigation does not recursively force the whole corpus into one review.
6. **R5 — review, integrate and advance only warranted checkpoints.** Independently review
   all learner-facing branches for Japanese correctness, actual adopted coverage and
   Russian comprehensibility; adjudicate, correct and re-review affected material.
   Run the actual validators, vocabulary reviews, budgets, manifest and real-reader/native
   gates. Recheck all combined-tree Russian option ambiguity, canonical app hint vocabulary
   and source-bound history. Exact reused Japanese bytes retain licenses, not RU approval.
7. **R6 — maintain alignment.** A tested manual cycle may later support a least-privilege
   report-only Action. No report self-translates, self-approves, merges, advances immutable
   tags or affects offline study. New upstream content remains pending until adopted.

This request does not waive the existing C6/C7 dependency or authorize paid media,
fabricated phone acceptance or ordinary RU activation. Inventory and contributor tooling
can proceed now; blocked release gates must not be bypassed to claim corpus completion.
The official `ru-pilot-a` and controlled `ru-pilot-b` runtime pins remain unchanged.

## Completion evidence

Full translation means every frozen target object has a complete reviewed Russian unit
or an explicit justified non-translatable asset disposition, all necessary dependencies
are closed, all changed guidance/source semantics are reconciled, and applicable
runtime/device gates pass. Partial articles, blocked drafts, absent files, copied English
prose, hashes and a generated manifest cannot satisfy that definition.

Current work items remain the authority for outstanding acceptance: RU #2 provenance,
RU #3 staged corpus, RU #5 integration, RU #6 structured/media pilot, and app #28.
Keep the historical C0–C7 evidence in IMPLEMENTATION-PLAN; update its current summary,
not the old reports. Record each verified tooling/method finding in active instructions.

## Manual provenance commands

From the RU root, with an isolated clone containing the two immutable source commits:

```powershell
python tools\translation_progress.py inventory --upstream <EN-clone> --revision 5f460b85b391404e7da01be0a0cded78243b7538 --output <artifacts>\before.json
python tools\translation_progress.py inventory --upstream <EN-clone> --revision 6af98cb717755690a9ca793e5454a96ebd7a8f9f --output <artifacts>\after.json
python tools\translation_progress.py report --before <artifacts>\before.json --after <artifacts>\after.json --ledger docs\translation-tracking.json --output <artifacts>\progress-next.json
python tools\translation_progress.py checkpoint --before <artifacts>\before.json --after <artifacts>\after.json --ledger docs\translation-tracking.json --scope <reviewed-paths.json> --output <new-checkpoint.json>
```

Outputs must be new paths: old receipts/checkpoints are never overwritten. After reviewing a
fresh report, explicitly replace the mutable current `docs/translation-progress.json` and
commit that update. Inventory hashes actual Git blobs against every manifest entry, including
raw binary/stroke identity; an uncommitted EN worktree cannot silently retarget it.
Checkpoint recomputes the current RU tree and manifest instead of trusting an old report.
It needs a nonempty explicit adopted scope, complete current review, reconciled guidance,
the exact batch target and an explicit human authority record. It records exact source/RU
hashes; it is not release approval. Renames are candidates, never automatic identity/review moves.
Changed English-only prose still expires review even when the invariant projection is unchanged.

`translation-tracking.json` retains the 51 Pilot A and30 Pilot B runtime review records and
two separately blocked audio text reviews without rewriting the historical ledgers.
Its `checkpointAuthority` remains null. No tag or checkpoint is advanced by this inventory.

## Verified execution checkpoint: 2026-11-04

R0/R1 are implemented and independently accepted, not merely planned.
[Review and regression record](full-translation-review.json) separates the initial
NEEDS FIX finding from its accepted correction: raw literal and escaped-equivalent
duplicate JSON keys now fail before decoding can collapse them. The real suite passes
124 tests with no failures, errors or skips; the actual RU validator reports zero errors.
Both immutable full inventories still regenerate exactly. The final manual report is
byte-reproducible, SHA256
`e9e549154fb17af30bab3ca7f66fa714fa8d0ac6129fcb4744428f26fdc88f28`.
It detects six added/four modified source paths, none in the adopted runtime stage.
All three changed guidance dispositions since C2 are independently accepted.
Current statuses remain 78 reviewed-current / three partial / two reviewed runtime-blocked
drafts / 8,195 pending. The actual checkpoint CLI still exits 1 and creates no checkpoint.
Runtime bytes, old provenance and both reviewed audio drafts remain unchanged.

The owned API29 lab also completed a previously missing C6 path on the exact signed
`0293a7bab3e5e0ad752e15c822c610b11d9fc2c4cc5a45de27ca31bfa3125bde` APK.
Its runtime was the authorized `stop-cran/learning-japanese-ru-integration-test`
`ru-pilot-b` at `7ce81c74e72fc189185a1bebe71d775379792124`,
content version `24362f736bc17328`, not the complete new EN target or ordinary RU main.
Four real ten-question Russian-to-Japanese extra-practice sessions earned reverse
memory normally; no clock, database, gate or daily limit was changed. Five words then
actually opened Word Type. Their reverse records are Review/reps 4/stability
2.7899488574439086 days; three correct answers on other words still yield
1.9818197930436123 days, below the unchanged two-day gate.
The actual five-question Word Type session passed 5/5, including Russian canonical
metadata labels, automatic field focus and visible IME before each helper input,
correct feedback and committed Next records.
The five actually typed words were ぺらぺら, きらきら, つやつや, つるつる and ぬるぬる;
this is not all 13 onomatopoeia words.
Every original 36 state / 90 log / 18 session row remains unchanged; legitimate new
practice yields 53 / 135 / 23. This is native UI/history evidence, not proof of
learning effectiveness or Japanese-keyboard acceptance: the lab retained its existing
Latin IME and used the disclosed input-only helper.
The lab was restored through normal validated Settings to official RU `ru-pilot-a`
at `544dd15f...`, explicit Russian, N5 and the original effective daily limit of 10.
The final private snapshot retains every original and legitimate new learning row.
The helper and 155 individually resolved remote XML files were removed, adbd was
returned to UID2000, and only the verified owned emulator was stopped; its ports closed.

Remaining R2/R3 blockers are still real: a second distinct CounterChoose day,
fresh exact-package authority for both Russian audio adaptations followed by actual
playback/interruption tests, and physical-phone/Japanese-IME/release acceptance.
[The exact authority request](pilot-b-media-authority-request.json) is prepared, not
approved. Ordinary RU activation and broad R4 authoring have not been unlocked.
The complete 8,197 absent-path backlog plus partial units remains visible; this
checkpoint is not a claim that the full corpus has been translated.
