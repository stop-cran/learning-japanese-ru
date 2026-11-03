# EN/RU implementation: small checkpoints before broad translation

Status: approved design, independently reviewed execution checkpoints; no implementation or acceptance tests are claimed.
The [design](DESIGN.md) remains authoritative for language/source behavior. This plan changes delivery order,
not the agreed independent histories, Japanese target, Latin romaji or no-English-fallback policy.
[Independent review and reconciliation](https://github.com/stop-cran/learning-japanese-ru/issues/5#issuecomment-6599641819):
no blockers; clarified validated-candidate retention and C0 candidate versus C4 final cohort ownership.

## Ownership and sequence

| Checkpoint | Result | Work item |
| --- | --- | --- |
| C0 | Frozen source, scope and acceptance dossier | [RU #4](https://github.com/stop-cran/learning-japanese-ru/issues/4) |
| C1 | Language-aware transport/import contract tested before publication | [EN #61](https://github.com/stop-cran/learning-japanese/issues/61) |
| C2 | Complete reviewed RU instruction set, first usable revision | [RU #1](https://github.com/stop-cran/learning-japanese-ru/issues/1) |
| C3 | Russian app shell smoke-tested, then complete app localization and safe switching | [Android #28](https://github.com/stop-cran/kanji-cards-android/issues/28), [#127](https://github.com/stop-cran/kanji-cards-android/issues/127) |
| C4 | Reviewed, dependency-closed kanji/word pilot A | [RU #3](https://github.com/stop-cran/learning-japanese-ru/issues/3) |
| C5 | First real app/content integration and methodology correction gate | [RU #5](https://github.com/stop-cran/learning-japanese-ru/issues/5) |
| C6 | Small representative pilot B for structured content/media, second correction gate | RU #3 and #5 |
| C7 | Release acceptance, scoped checkpoint, then broader translation | RU #3, [RU #2](https://github.com/stop-cran/learning-japanese-ru/issues/2), #5 |

C1 and C2 start in parallel, but C2's executable format instructions must agree with C1 before adoption.
C3's string inventory can start immediately; its source transition implementation needs C1's contract.
C4 requires adopted C1/C2 and a minimal provenance ledger, not scheduled drift automation.
C5 requires complete C3 and reviewed C4; C6 starts only after C5 findings affecting the next batch are reconciled.
C7 requires C6 acceptance. Broad translation and optional automated drift reports follow this learning loop.

## C0: freeze a bounded experiment

Planning inspection: EN `e27e8aaa61f374fd79216de792f37fd4d2102907`, Android
`8118c2ea4e3c94bf089340360edb644ee0c0cf5c`, RU bootstrap `5713d2fe605a2b2b936b6241abc17b15b047cb8a`.
These are not translation-alignment checkpoints; execution must refresh the source/instruction inventory below.

- Record exact EN/app commits, fresh instruction-entry inventory, current release compatibility baseline,
  locale/source transition table and the exact learning behaviors each pilot must exercise.
- Record pilot-A candidate IDs and provisional support scope. C4 owns the final dependency-closed item inventory
  and freezes it before translation; pilot B is selected separately at C6 after first-gate corrections.
- Create one acceptance dossier with source/item inventories, dependencies, expected UI strings, actual app/content
  revisions, test commands/results, reviewer dispositions and known gaps. Evidence belongs in contributor docs,
  not learner runtime or a second authoritative app state.
- Initialize minimal RU provenance records: adopted scope, EN source hashes, RU reviewed hashes/revisions,
  intentional adaptations and pending/out-of-scope. Initially no translated item or completed checkpoint exists.
- Freeze each batch's upstream SHA while it is authored. Reconcile later upstream changes before checkpoint
  advancement rather than continuously moving the source during review.

Exit: concrete inventories/test cases exist; no open transport/state decision blocks C1.
This is planning evidence, not a translation tag or linguistic approval.

## C1: prove the contract with small fixtures

- Settle authored base/target language configuration, deterministic metadata hashing/versioning, language-neutral
  fields/headings and legacy adapters, repository-language stability, cache metadata and migration boundaries.
- Implement generator/validator/importer support together, keeping the currently released EN reader compatible
  with a freshly generated EN package. RU must fail safely on that old reader, retaining its accepted EN data.
- Use small synthetic fixtures across supported kanji/word/articles, counter v1/v2, grammar/curriculum,
  scenes and both listening transports. These are format tests, not reviewed Russian teaching packages.
- Cover absent legacy EN metadata, malformed/unsupported language/target, unexpected repository-language change,
  metadata-only version change, localized sections, corrupt hashes, missing dependencies and source isolation.
- Run focused existing Python/core/import/migration tests. Verify both old-reader/new-EN and old-reader/RU refusal
  with actual released parser behavior, not only static old-manifest fixtures.

Exit: compatibility matrix and exact transport are green and documented. Do not point an existing learner's
app at a draft RU package or raise the live EN schema just to exercise RU rejection.

## C2: complete instructions before teaching-content authoring

- Freshly enumerate EN instructions, scoped authoring files, reviewer agents and normative references;
  compare with the planning inventory and document retain/adapt/replace/remove decisions.
- Implement the complete RU overall/authoring/reviewer guidance for all content families. Close inherited
  path-scoped gaps; use shared guidance rather than requiring one new file or reviewer for every namespace.
- Include a compact terminology/translation guide and worked adaptations: `待つ` without the English comparison
  but retaining awaited-person `を` and waiting-place `で`, plus a complete constrained grammar/task example.
  Samples remain explicitly non-runtime until separately admitted to a content pilot.
- Preserve verified Japanese facts/IDs, naturalness and evidence boundaries; review new Russian comparisons,
  translated answer labels, context-sensitive distractors and pre-/post-answer information.
- Independently review the entire resulting instruction set and samples, reconcile findings, check local references
  and format consistency. Recheck EN instruction changes before adoption.

Exit: a complete, independently reviewed first instruction revision is usable for C4.
It is not frozen forever: C5/C6 can refine it with real integration evidence before expansion.

## C3: translate the app and prove safe language/source transitions

First small testable slice: Russian Home/Settings/section labels, unavailable/download states, standard quiz
chrome and built-in Kana. Native smoke-test real locale contexts and enlarged Russian text before translating
every screen. Use isolated format fixtures; never put English lessons behind a Russian production selector.

Then finish all app-owned surfaces: question/answer/status/error text, mode/deck labels, drawing feedback,
articles/help/accessibility, notifications, listening/recovery/results, export UI, plurals and dates/numbers.
Russian meaning voice uses Russian on-device support or localized unavailability, never English/cloud fallback.
Latin romaji and stable stored enums/IDs are retained; no grading/FSRS change is part of localization.

Implement one source/locale transition owner, including explicit pending versus accepted states:

- New install versus existing EN upgrade; supported device language and System default changes.
- Same-language custom repo retention and confirmed mismatched custom replacement.
- A validated candidate repo aligns UI language without recursively replacing that repo with the UI language's default source.
- Offline matching cache versus localized retry; invalid source/language and failed imports retain accepted data.
- Rapid changes, navigation/cancel/draft edits, stale sync/validation completion, process restart and backup restoration.
- Android Settings changes are observed outside the in-app picker. If confirmation/finish-session is needed while
  backgrounded, persist the pending decision and disclose/resolve it on return; do not silently replace custom content.
- Ordinary active questions explicitly finish/leave; durable listening retains captured content and language.

Test native API 29 and 35, with actual enlarged system text (including dialogs), focused inputs and settled IME.
Test Russian plurals with representative 1/2/5/11/21 quantities, notifications using the app locale, and ambiguous
voice hypotheses/unavailable support. Fixture review states may expose gated modes only in a disposable DB.

Exit: complete app-owned EN/RU coverage and source-switch tests pass; signed candidate release builds.
The early smoke slice is not called complete app translation. Ordinary RU activation remains gated until C7.

## C4: small coherent pilot A, not the full N5 corpus

Target a manageable first batch, provisionally 8-12 kanji and 15-25 words, including `待`/`待つ` and the linked
examples needed by their retained readings. These are sizing targets, not permission to truncate dependencies.
C0 records candidates; C4 freezes final exact paths/IDs and support dependencies before writing. Adjust the batch
or choose simpler cards if closure grows too large.

- Include enough permitted candidates for real meaning/reading choice pools; verify actual expected option counts,
  not a passing quiz with only its correct answer. No gate/exclusion weakening to accommodate a tiny dataset.
- Include full linked article and reading-example support, verified unchanged stroke files and their notices.
  Required examples, assessment prerequisites and references must resolve.
- For optional navigation to untranslated broader material, explicitly retain unlinked Japanese text or omit the
  optional link with a reviewed ledger disposition; never leave dangling links or point silently into English.
  Do not remove teaching rules, claimed reading evidence or scored prerequisites just to shrink the batch.
- Translate all learner-visible fields and bodies. Check Russian label uniqueness/semantic ambiguity and mark
  intentional adaptations; unchanged Japanese provenance is reused without restarting every source investigation.
- Independently review content for correctness, bounded coverage and Russian comprehensibility; reconcile, validate
  and regenerate the exact runtime manifest. Publish only on an explicitly named RU testing branch/revision until C7.

Exit: reviewed pilot A archive is dependency-closed, format/budget checks pass, and source/RU hashes are recorded.
App-wide localization is broader than pilot teaching coverage; missing content families must be disclosed as unavailable.

## C5: integrate the actual app with pilot A and correct the method

Use the signed candidate APK and exact public candidate archive with its generated manifest. Exercise the real sync,
import, Home queues, quiz/typing/drawing/readings, feedback, linked article Back and progress persistence. Do not
substitute parser fixtures or authoring-only files for delivered lessons. Avoid changing personal learner data.

Check EN to RU to EN, source-specific history restoration, built-in Kana continuity, no English fallback, corrupted/
interrupted updates, offline after sync, unsupported/undeclared repo handling, custom alignment and Android Settings.
Compare visible Russian text, voice/IME behavior and actual selectable options with the approved pilot content.
Retain the exact APK/EN/RU revisions and raw non-skipped native results; record public archive hashes separately
from linguistic approval. Require the old EN reader regression to remain green against the integrated new EN tooling.

For each meaningful finding, identify app, schema/tool, translation, instruction or test-harness ownership. Reproduce
before changing behavior; retain unresolved evidence. Fix/re-review affected content/code, rerun the smallest affected
checks, and update corresponding instructions with a concise mechanism/invariant and a concrete finding reference.
Amend this plan/dependencies when a finding changes the next checkpoint. Do not turn one anecdote into a universal rule.

Exit: no unresolved consequential pilot-A issue; applicable guidance and plan corrections are persisted.
If none are found, say so: no mandatory finding count or instruction churn.

## C6: pilot B exercises structured and media boundaries

After C5, add a small dependency-closed representative set: one compact complete grammar group/set and companion
article/vocabulary/prerequisites; bounded counter v1/v2 examples; at least two permitted word-picture candidates;
one complete legacy listening passage and one existing supported Japanese task package with localized help/feedback.
Choose exact source objects and their true dependency closure before authoring; do not extract arbitrary JSON rows
or inherit package approvals. Synthetic C1 format fixtures are not actual-content acceptance.

Reuse unchanged verified Japanese audio/artwork only, with licenses and fresh package bindings/approval boundaries.
If suitable media or approval is absent, narrow the candidate with an explicit blocked/missing case instead of
generating paid media or claiming that family passed. New media needs separate authorization.

Run second real integration: grammar choice/type and answer-information placement; counter full phrase/readings;
scene descriptions/accessibility without answer leakage; listening playback, transcript/feedback and captured
encounter interruption, process recreation and source/language return. Use isolated review states where necessary.
Apply C5's finding -> correction -> guidance -> affected-regression loop again before expanding the collection.

Exit: all planned pilot-B families genuinely reviewed and integrated, or blocking cases openly recorded.
Unsupported/missing families cannot be counted green or silently replaced with EN content.

## C7: candidate acceptance, then scale the validated process

- Revalidate the integrated published tree, budgets, links, metadata, current EN reader compatibility, release build,
  source transitions, both native API matrices and independent changed-content/code review.
- Provide a version/commit-suffixed release APK in the phone's `Internal storage\Download` when owner testing is
  requested/authorized. Record exact installed APK/content and genuine phone feedback; do not infer it from emulator
  success. Delivering an APK is not installing or approving it.
- Keep owner-testing publication distinct from general release. Enable ordinary RU default/new-install selection
  only after the required compatible app, reviewed runtime stages and applicable release acceptance gates pass.
- Record immutable scoped RU/EN checkpoints only for the adopted, reconciled inventory. Whole-corpus parity remains
  pending; reuse correct earlier review records but re-review changed Russian text or teaching semantics.
- Choose subsequent translation work by coherent content family and review complexity, using refined instructions.
  Add scheduled drift-report/PR automation after a tested manual diff/checkpoint cycle; its availability never gates study.

## Methodological notes recorded now

The reconciled [instruction-plan review](https://github.com/stop-cran/learning-japanese-ru/issues/1#issuecomment-6599291063)
exposed the fixed-inventory and path-scope gaps; the [cross-repository review](https://github.com/stop-cran/learning-japanese-ru/issues/4#issuecomment-6599252027)
identified new-EN/old-reader acceptance ambiguity and the eager-versus-pending source switch change.
Those mechanisms are recorded in corresponding EN/RU/app instructions now.

During this localization work, persist verified reusable findings in the relevant repository's active instructions
in the same correction batch. Keep reproduction, evidence, scope and disposition in the work item; code/linguistic
errors must be fixed, not merely documented. Pending hypotheses stay explicit and do not become mandatory rules.
This is the user's requested methodology for this project, not an assertion that future integration has already passed.
