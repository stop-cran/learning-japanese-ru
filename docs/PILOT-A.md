# Pilot A execution dossier

Status: exact pilot A authored and packaged for the first app/content experiment;
independent teaching review accepted; app/import/native/publication acceptance pending.
Execution follows [C0-C5](IMPLEMENTATION-PLAN.md). This dossier does not activate the ordinary Russian default.
C2 adoption: `df6839f4292a52e3316cf040450de38b6adf9add`,
[independent implemented-instruction review](https://github.com/stop-cran/learning-japanese-ru/issues/1#issuecomment-6602318753).

## Frozen sources

- EN content/instruction baseline: `3196c3a273b9db8375bb79bede01ab8db5bce0d0`.
- Android committed baseline: `fec3c0a9d7485b50be3f13212098ff8772fb665b`, with earlier unrelated Home/quiz UX
  edits preserved in the worktree. Localization validation must identify those combined test inputs.
- RU baseline: `ede53dc2e562b93997736fc14d279523daa1a92a`.
- Shared language tooling is a separate C1 change from these sources; record its accepted commit with the final package.
- The fresh instruction inventory/adaptation matrix belongs to C2. A source SHA alone is not instruction or translation acceptance.

## Exact candidate scope

Kanji (12): `日`, `月`, `火`, `水`, `木`, `山`, `川`, `人`, `大`, `口`, `待`, `時`.
Each retains source readings, level, tags, radical/stroke metadata and an unchanged licensed stroke file.

Primary words (23): `日`, `月`, `火`, `水`, `木`, `山`, `川`, `人`, `大きい`, `口`, `時間`,
`火山`, `山水`, `水中`, `大木`, `日中`, `月日`, `休日`, `小川`, `川上`, `人口`, `大人`, `待つ`.

Required synonym/exclusion support (4): `太陽`, `河`, `昼`, `昼間`. This slightly exceeds the provisional
15-25-word sizing target to retain actual source exclusion dependencies, rather than weakening the quiz.
All 27 words receive complete Russian bodies, not English support-only pages.

Required `quiz_exclusions` from the selected source are retained: 日 -> 太陽; 川 -> 河; 日中 -> 昼/昼間.
Curated distractors outside this bounded edition and optional broader navigation receive explicit per-file dispositions
in the provenance ledger. Replacement kanji distractors must remain distinct, available and linguistically reviewed;
word option-pool tests must use real classes/exclusions and maintain normal grading/gates.

No unsupported N5 claim: source levels remain unchanged, including 待/口 N4 and vocabulary such as 火山/月日 N2.
Words without explicit source level retain the application's existing fallback; no translation relabels them.
Native coverage uses cumulative filters or disclosed disposable review states, not relaxed prerequisites.

## Navigation and teaching boundaries

Internal links within this cohort remain app-renderable and close under Back navigation.
References to unadopted kanji/words may retain Japanese text, its Russian explanation and reading without a link;
each removed optional link is accounted for by path. This is not removal of a Japanese rule, example, qualifier
or assessed prerequisite. No broken local link or silent EN teaching fallback is permitted.
All learner-visible example translations, notes, table labels, source labels and related-word glosses are Russian.
Dictionary titles/technical URLs and stable internal identifiers can remain in their original form.

Pilot A deliberately omits runtime grammar/counters/scenes/listening. They remain unavailable, not partly translated.
C1 synthetic format tests and C3 localized UI tests cover transport/chrome but do not certify those teaching families;
the real structured/media cohort is C6 after first-gate corrections.

## Evidence checklist

| Gate | Required evidence | Current state |
| --- | --- | --- |
| C1 | language metadata hashing, EN schema1/RU schema2, invalid declarations, neutral counter alias | tooling/current-main and actual new/released-reader checks pass; reported parser/authority findings resolved at bounded code-review boundary; native importer/publication gates separate |
| C2 | full RU author/reviewer instructions, fresh inventory, independent review/reconciliation | independently reviewed and adopted; all identified source-rule omissions resolved |
| C4 | complete 12/27 translated files, 12 unchanged strokes, exact hashes/links/exclusions, notices, independent correctness/coverage/RU review | independent bounded content acceptance after all eight corrections; app/import/native/publication acceptance pending |
| C3 | complete app strings/labels/speech, safe locale/source/cache transitions, focused tests/build/native shell | retained correction batches pass; all reported code findings reconciled and final one-issue review CLEAN; native shell/C5 remains pending |
| C5 | exact signed APK/public runtime archive, real API29/35 sync/quiz/article/IME/offline/source-history evidence | integration pending |

Record meaningful verified defects, ownership, fixes, affected checks and instruction/plan updates here or in RU #5.
No finding quota; no inherited EN, plan, media or physical-device acceptance. No phone installation/testing is claimed.

## First actual runtime candidate

Frozen EN source: `3196c3a273b9db8375bb79bede01ab8db5bce0d0`.
Manifest: schema 2, `ru`/`ja`, `contentVersion` `dc8682928fc5e0a8`.
Candidate artifact: `ru-pilot-a-dc8682928fc5e0a8.zip`,
SHA-256 `9fdc03d7679c183541c19e0a6b3a8261b54facbbc9b486de591d6966ed2e8a51`.
It is a local frozen review/import input, not a public runtime release; future corrections require a new exact package.
The 51-entry ledger records each adopted Markdown/stroke hash, unavailable optional navigation/distractors
and pending Russian exclusion adaptations. Its checkpoint remains null until the applicable review/integration gates.

Executed against the actual translated working tree:

```text
python tools\build_manifest.py
python -m unittest discover -s tools -p "test_*.py"  -> 108 tests, OK
python tools\validate.py                           -> 0 errors
python tools\check_content_budget.py               -> passed
```

All 51 manifest runtime hashes matched; all 12 source stroke files were byte-identical.
The archive budget check retained 116,268 bytes and inflated 125,788 bytes across 58 files/62 entries.
The source metadata and required word exclusions were preserved.
These checks do not approve Russian meanings/distractor semantics, UI rendering or native quiz behavior.
Independent actual-content review covers all 39 Markdown cards separately from the already accepted C2 instructions.
[Owner-attributed authoring/check evidence](https://github.com/stop-cran/learning-japanese-ru/issues/3#issuecomment-6602692493)
records this pending-acceptance boundary.

## Actual-content review and corrections

The fresh independent reviewer completely read all 39 RU Markdown cards and their exact frozen EN sources.
Original verdicts: correctness **NEEDS FIX**, bounded coverage **CLEAN**, Russian comprehensibility **NEEDS FIX**.
Eight actionable findings were reported; the author implemented evidence-grounded corrections and affected-content
re-review accepted the corrected pilot. The original full report and actual-read/source evidence are preserved as session artifacts;
the review did not test Android or broaden pilot A.
[Owner-attributed findings and correction record](https://github.com/stop-cran/learning-japanese-ru/issues/3#issuecomment-6603031593).

| Finding | Concrete correction | State |
| --- | --- | --- |
| F1 | Direct 川/小川 Russian meaning exclusion, retaining 川/河 and no transitive river clique | resolved |
| F2 | 材木 (ざいもく) belongs in 木's モク row, not ボク | resolved |
| F3 | 大木 selects attested タイ/ボク, not an invented ダイ-to-タイ conversion | resolved |
| F4 | 山火事 is 山 plus 火事, not reversed two-kanji 火山 | resolved |
| F5 | 昼 retains ordinary daytime meaning; noon/lunch is contextual | resolved |
| F6 | 水玉 means droplet/polka-dot pattern, not an unqualified pea | resolved |
| F7 | 改札口 retains ticket-control entry/exit restriction, not ordinary station exit | resolved |
| F8 | Retained suffix -ま.ち must not be evidenced by an initial 待ち合わせる stem | resolved |

Own-row voiced/name-reading dispositions are corrected in the same batch: 火山 under ザン, 出口/入口 under -ぐち,
and 日本 explicitly special rather than mechanical ニチ evidence. Source reading metadata/levels remain unchanged.
Nonblocking unrelated editorial suggestions are not expanded into additional pilot work.
F2-F4 include inherited source explanation errors, reported with owner attribution in
[EN #62](https://github.com/stop-cran/learning-japanese/issues/62); reliable source evidence does not make those
claims infallible. Reusable examples are recorded in the active translation methodology.

The conservative export gate also caught a parent status update to exported `README.md` during review.
All 51 runtime hashes and the immutable original archive/ledger still matched; this was not teaching drift.
The complete exported receipt nevertheless became stale. Freeze and verify the next complete export after all
status/provenance edits, preserve the first archive, and use a new export-hash-suffixed artifact for follow-up.
Do not repeat all unchanged linguistic review solely because a developer-facing status file changed.

## Corrected content acceptance

[Independent corrected-content review and actual-read ledger](https://github.com/stop-cran/learning-japanese-ru/issues/3#issuecomment-6603245447):
correctness **CLEAN**, bounded coverage **CLEAN**, Russian comprehensibility **CLEAN**.
The reviewer completely read all 11 changed articles and their affected interactions, reusing the original complete
evidence for 28 byte-unchanged articles. F1-F8 and all coupled reading-row/name dispositions are resolved.
No consequential content issue remains in this bounded review; optional editorial polish remains optional.

Accepted teaching input: `contentVersion` `afe5c99e66524d95`, schema 2 `ru`/`ja`;
archive `ru-pilot-a-afe5c99e66524d95-2cb44ff2374c.zip`,
SHA-256 `4d346f4446104cb8a6ad6bc3d5481849ee5fefc2b27ac3951872c718d80f01e7`.
Review report SHA-256 `98ba6de798295e2da8329d0b9208cfb81488dd63d3b346b00d0c2b306c71b705`;
evidence SHA-256 `6e9f0b7676f1f504c294f598e5b02d51d90931a9928d20602b83ab15ed48ffb1`.
All 58 export entries and 51 runtime/ledger entries matched before/after the follow-up, without drift.
The corrected actual RU tree again passed 108 adopted tests, validator 0 and budget checks
(116,685 retained bytes, 126,700 inflated bytes).

After the detached review result, contributor status and per-file ledger entries are reconciled to content-reviewed.
These non-teaching edits do not rewrite the immutable reviewed archive or alter any accepted runtime hash.
The historical reviewed ledger remains identified in the review record; the current ledger records this later
status reconciliation explicitly. Its checkpoint stays null pending app/integration acceptance.
This is bounded content acceptance, not native quiz/voice/IME, importer, publication, full N5/parity or physical-device approval.

## Android static handoff and native evidence boundary

Retained JUnit XML records **12 current-reader tests** with zero failures/errors/skips:
language/schema/counter aliases, actual EN/RU archives and normal four-choice word exclusions/readings,
source transitions, Russian plurals, superseded-import rollback and legacy EN/ja metadata migration.
An isolated baseline reader at `fec3c0a9d7485b50be3f13212098ff8772fb665b` passed **2 actual-archive tests**
with zero failures/errors/skips: newly generated EN schema 1 accepted, actual RU schema 2 refused.
The archives retain the exact hashes already recorded above and in the implementation handoff.
These results are parser/state regressions, not completed user-driven native integration.

Android lint and signed release build passed. Final detekt reports two findings in the pre-existing
`ComposeUiTest` UX changes; both were reproduced from the original UX-only snapshot, while clean baseline
detekt passed. No localization-related detekt finding remains. Original UX snapshot hashes were verified;
unrelated changes are preserved and excluded from the intended localization publication.
The initial independent changed-feature review and targeted followup have returned; the followup still
requires fixes before the next bounded native batch. Its dispositions and evidence are recorded below.

The implementation agent reported a prior API 35 article/locale/Back smoke at enlarged system text,
but did not retain its complete raw instrumentation output. Its two summarized status lines cannot
be independently verified from the persisted handoff, so that run is **not counted as native acceptance**.
Repeat the applicable cases in the bounded API 29/35 batch with retained raw `-w -r` output and status 0
for every selected non-skipped case. No physical-device test or general-release approval is inherited.
The concrete preservation gap reinforces the existing raw-result rule; it does not justify a new test quota.

## Independent Android findings and refreshed EN compatibility

[Owner-attributed Android review record](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6605902288)
preserves the six initial feature defects: durable cache/source activation, cached-pilot rollout admission,
fresh continuation language admission, duplicate raw manifest declarations, rejected-candidate retry cleanup,
and app-owned English Grammar guidance. The author corrected all six and retained 85 passing tests
across 11 suites, with zero failures/errors/skips. Targeted independent followup returned **NEEDSFIX**:

| Initial finding | Targeted disposition |
| --- | --- |
| F1 durable source/cache acceptance | partially resolved: candidate cache/authority commit is atomic, but a queued ordinary sync can later overwrite the accepted branch cache |
| F2 cached-pilot rollout admission | partially resolved: ordinary Home entry is gated, but fresh typed Drawing bypasses admission |
| F3 fresh continuation language admission | partially resolved: registered legacy captures are handled, but typed Drawing continuation remains unconditional; same defect as F2, not another finding |
| F4 duplicate raw manifest declarations | resolved by production-path review and a fresh five-input parser probe, including escaped-equivalent keys and retained malformed-JSON cause |
| F5 rejected-candidate retry cleanup | resolved in the real generation-owned Settings lifecycle; rendered-UI retry acceptance still pending |
| F6 app-owned English Grammar guidance | partially resolved: localized notices still interpolate English scope labels and display raw evidence diagnostics |

The parent preserved the full returned findings, read ranges, evidence limits and matching start/end
identities in `ru-app-targeted-f1-f6-review.md`, SHA-256
`47fd0273656b0bdd75b1b8dc1abdf719e5c12ae1c96aafcad1d1b2b370f26ea4`.
[Verified owner-attributed followup](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6607127068).
The original report remains unchanged. The author completed a bounded correction/validation batch
for the three remaining defects; independent disposition remains pending. The parent verified the five
retained JUnit suites: 40 tests, zero failures/errors/skips (12 core Grammar-focus; 4 candidate-import;
6 navigation; 17 Grammar ViewModel; 1 Compose Grammar-localization test). This does not mean 40
native acceptance cases or replace the earlier retained 85-case baseline.
The release APK is 51,514,998 bytes, SHA-256
`60f46b154fa3adf6d76311bfdab41cc16c548ecc9ae249f8f5bf93e723c0929a`;
the parent verified its size/hash and all three original UX snapshot hashes.
Lint/release tasks succeeded; lint reports 149 warnings and 7 hints, not a clean report.
Detekt retains the two reproduced pre-existing UX findings. Evidence is retained in
`ru-app-correction-turn3`; no native run, staging or commit occurred in this batch.
The second focused independent review has now returned; its bounded dispositions are recorded below.
These are app defects, not reopened Russian teaching-content findings.
Supplied green tests and in-memory simulated recovery do not establish native rendering, actual
process-death/disk recovery or full localization parity. Fix/re-review before the next affected native batch.

These concrete code traces established app-instruction corrections: atomic candidate
acceptance must cover all ordinary cache writers; fresh admission must cover typed as well as legacy
routes without inheriting a captured-session exemption; localized templates require localized arguments
and typed evidence notices rather than raw English diagnostics. The app author owns these instruction
updates with the fix batch; the second reviewer inspected the new guidance and actual correction paths.
They are not new teaching-content claims or a required finding quota.

### Second targeted app followup

The second reviewer verified that the queued ordinary request can no longer overwrite an accepted
branch cache, and that fresh typed Drawing dispatch/ViewModels use language/rollout admission while
registered captures can finish. Drawing is **resolved at the code-review boundary**, not native-tested.
The original Grammar scope interpolation and group-evidence English renderers are also corrected.
The same review returned **NEEDSFIX** for two directly coupled leftovers:

- A historical accepted non-default EN branch row survives intentional EN/RU/default-EN source
  selection. The new ordinary-sync guard then rejects the genuinely selected EN default, even for
  forced retry, and returns `UpToDate` without updating. Intentional default transitions must advance
  or invalidate authority through the same serialized protocol, without reopening stale writes.
- Practice `Preview.message` still renders English interruption, expired-consent, changed
  content/scope/availability and empty-queue guidance verbatim. These learner notices require typed
  localized outcomes; localizing scope/evidence helpers alone does not cover the actual renderer.

The full returned findings, matching start/end identity, actual read ranges and evidence limits are
preserved in `ru-app-targeted-followup-review.md`, SHA-256
`0273bbf60d91529ccf80c8793885c7a2c9e2af84ac3060ec7fd2512294169dfe`.
[Verified owner-attributed second followup](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6607986336).
Earlier reports remain unchanged. The reviewer inspected the same 40 retained passing cases, not
40 new executions, and performed no native run. Explicit-pilot Drawing test admission reaches
`NoStrokeCards`; it does not demonstrate a populated/rendered pilot Drawing session.
The author completed the bounded two-fix batch with production default-transition and actual
Practice-notice regressions. Intentional built-in transitions now use the serialized durable-authority
protocol; Preview recovery/stale/consent/empty notices are typed and rendered through EN/RU resources.
These are author corrections awaiting narrow independent disposition, not native acceptance.
The parent verified six retained JUnit suites: 25 actual passing cases, zero failures/errors/skips
(6 candidate-import; 3 language/source transitions; 6 navigation; 7 targeted Grammar ViewModel;
2 Grammar-localization; 1 affected existing Compose Preview test). Full command stdout/stderr and
exit statuses, the two earlier failed attempts, final XML, lint and signing output are retained in
`ru-app-correction-turn4`. Final focused tests, lint/release, signing and diff checks exit 0;
Detekt retains only the two known original UX findings. Lint remains 149 warnings/7 hints, not clean.
The current APK is 51,517,714 bytes, SHA-256
`78e1c13570272211fe359664ed44f98b071716c85170a84f8efc57c9f6ba3f7b`.
The parent verified its size/hash and unchanged original UX snapshot hashes. The pre-existing
Compose Preview test was adjusted only for the directly dependent typed-notice API.
App guidance now records intentional selection writers and recovery/consent notices; the narrow
review has checked those paths. No native run or commit occurred.
No teaching-content review is reopened, and C5/native/publication/C7 gates remain outstanding.

### Language-intent marker followup

The narrow reviewer confirmed closure of the original intentional-default permanent-sync rejection
and **resolved** all four Practice Preview learner notices. One directly coupled defect remains:
source authority compares only repository/branch, so a newer English/System choice on the same
default branch is mirrored only to preferences. Startup restores the older language encoded in the
durable selection marker, undoing the learner's latest intent (also in the reverse direction).
System and explicit English are different intents even when their current effective locale/source match.

The full returned findings, unchanged start/end identity, actual read ranges and limits are preserved
in `ru-app-targeted-language-marker-review.md`, SHA-256
`ef06ce1d0d5584c869d7db0240754eb6c1a1ef3c213cca58c1898f101aa6c0dd`.
[Verified owner-attributed marker followup](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6608742008).
Earlier reports remain unchanged. The reviewer reused the 25 retained passing executions and
performed no native run. The author completed the surgical marker correction: each approved intent
has a pending token, selection/platform-locale application/exact-token acknowledgement are serialized,
and startup recovers only the current pending intent. The real writer/recovery regressions cover
EN/System in both same-branch orders and retained custom-source recovery. These are author
corrections awaiting independent disposition, not physical process-death acceptance.

The parent verified two retained suites with 12 actual passing cases and zero failures/errors/skips
(6 language/source transitions and 6 candidate-import regressions). This is a focused new execution
of overlapping coverage, not 12 additional native cases or an additive unique-test total.
Full logs/statuses/XML are retained in `ru-app-correction-turn5`. Final tests/lint/release, signing
and diff checks succeed; the initial combined command stops on the same two original UX Detekt
findings. Lint remains 149 warnings/7 hints.
The current APK is 51,517,714 bytes, SHA-256
`060cbc50787d2d22d12355a591adca7f2904bc67c7f5da56452c395a4de5bd5a`;
the parent verified size/hash, actual signature and unchanged certificate plus original UX snapshots.
App guidance now distinguishes latest intent from source/effective-language equality.
The one-issue followup has returned; no native test, staging or commit occurred in the correction batch.
This does not reopen accepted Practice/content evidence or replace any C5/native gate.

### Final bounded code acceptance and first C5 batch

The latest-language-marker followup returned **CLEAN**: fresh intent tokens, checked preference
persistence, platform-locale application, exact-token acknowledgement and startup-only pending
recovery resolve the reported same-branch intent defect. The reviewer established no strictly
coupled actionable regression and reused prior resolved findings rather than re-auditing unchanged
localization. All reported app findings are now reconciled across the retained review sequence.

Full returned acceptance, matching start/end identity, actual read ranges and limits:
`ru-app-final-marker-acceptance.md`, SHA-256
`6ce7b149fe58ce39f3dfb20e79daf2c867c1fc81d5101ebda0d41ff9cf4e65c5`.
[Verified owner-attributed bounded acceptance](https://github.com/stop-cran/kanji-cards-android/issues/127#issuecomment-6609232814).
This is code-correction acceptance, **not** whole-app translation parity, physical process-death/disk
recovery, native Android locale acceptance, C5 completion or general C7 release.

The first bounded C5 batch passed reviewed RU import/article/readings, locale recreation,
source-bound retention and Back on API 29 and API 35 at font scales 1.0 and 1.5.
The parent verified all four complete raw `-w -r` streams: exactly one selected completion with
status 0 per run and no skipped/assumed case. The applicable earlier missing raw smoke evidence is
now replaced by these fresh runs; the original shell-437 claim remains historical, not retroactively
verified. Both failed initial viewport/loading assertions and their test-only fixes remain recorded.

This is **debug instrumentation** of an explicit fixture HTTP pilot source, not a signed-release
public-repository import or real in-app Language-selector test. The test uses programmatic `AppLocale`
changes; it verifies the article's `Чтения` section, not the reading quiz or normal four-choice pool.
Debug app SHA-256: `4eb35e1d0f134a60386c24691993eba053178440abcbfc6d25781fb6216a4a6a`.
API 29 test APK: `f2e24f70292dc64ceecac7ff8451f66640f0e20657919de1af897b47aeb0512b`;
API 35 test APK: `bd0fd5f6415173ac0d4ed1da7cb687ccb5b5d43c89192bb5bcafd866566dd8cd`.
Exact raw/config/package/restoration artifacts: `ru-app-c5-native-batch1`.
The immutable signed release copy still hashes to
`060cbc50787d2d22d12355a591adca7f2904bc67c7f5da56452c395a4de5bd5a`;
its separate API 35 smoke installs and launches actual release `MainActivity`, but does not import RU.

The next bounded batch is actual signed-release Settings English/System choice and normal-restart
persistence at both APIs/font sizes. As explicitly allowed by C4, the reviewed runtime is being
prepared for the public `ru-pilot-a` candidate branch so the subsequent signed-release import uses
the real delivered repository instead of an HTTP fixture. Public archive identity will be recorded
separately from the accepted teaching-export hash; RU `main`/ordinary C7 activation remains closed.
Production remains frozen unless a proven defect is reported. All broader Settings/source/offline/
progress/IME/drawing/capture/voice/notification C5 gates remain separately open.

The current EN main refresh is now checked in an isolated worktree at
`625cc3229e767ae5314847e7c1781640fcaff5c6`, preserving its four incoming N1 sets:
360 tests passed, validator 0, budget passed, 8,214 runtime hashes verified.
Manifest schema 1 `en`/`ja`, `contentVersion` `915b4bfbca5b5d57`;
archive SHA-256 `3b57952c7d67f316b015d57d874b102e0b971f53c906cda550189feec562fc43`.
The isolated released EN reader executed two passing, non-skipped tests against this new archive and
the reviewed RU archive, including the newly added EN cards and continued RU schema-2 refusal.
[Verified owner compatibility record](https://github.com/stop-cran/learning-japanese/issues/61#issuecomment-6605902291).
The refreshed package is not published, and the RU teaching-source SHA remains frozen.

## First verified implementation findings

- C1 accepted Russian H2 labels, but the existing validator still found reading rows only under literal `Readings`.
  Its selector now uses the adopted base-language `Чтения` heading. The focused regression preserves/requires the
  row's own linked word example; removing that link fails. This mechanism is recorded in EN/shared instructions,
  and must also guide the app's reading-helper extraction.
- A parent current-EN archive comparison incorrectly LF-normalized every manifest section, including binary WebP.
  `images/うんざり.webp` then appeared mismatched despite raw-byte identity with the accepted archive.
  The verifier now follows the existing format: text maps normalize CRLF to LF; image/audio maps hash raw bytes.
  All 8,202 runtime hashes at EN `954ec1f59bbacf76c718cb771d7af15e30c50fcf` match the accepted archive
  (573 raw binary, 7,629 normalized text). This was a verification-helper defect, not a content/parser defect.
  Incoming EN `625cc3229e767ae5314847e7c1781640fcaff5c6` adds four N1 kanji/word/stroke sets;
  refresh shared-contract/current-main reader evidence before publication without moving the frozen RU teaching source.
- Copied upstream current-file smoke tests referenced EN's `休`/`休む` outside pilot A. RU's smoke uses its genuine
  selected `日`/`待` and `待つ`/`休日` files instead; missing fixtures are failures, not skips. The four pre-authoring
  missing-file errors remain expected preparation failures until the real translated pilot exists.
- EN's grammar/task test files also contain full-corpus content assertions and contributor media fixtures.
  They are not adopted as RU pilot tests: their original full suite still passes in EN, while RU runs the shared
  language/front-matter/counter/scene/listening and vocabulary-format tests plus real pilot smoke. No validator is
  relaxed, no missing case silently skipped, and no nonexistent RU structured/media corpus counted as accepted.
