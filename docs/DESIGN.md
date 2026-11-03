# Russian edition: agreed design and implementation boundaries

This document records the agreed design, not implemented capabilities or translated coverage.
The repository is intentionally not app-loadable until the language contract, compatible app,
Russian authoring instructions, and a reviewed content stage are ready.

## Language and repositories

- English source: `stop-cran/learning-japanese`; Russian edition: `stop-cran/learning-japanese-ru`.
- One stable repository-wide base language across branches, initially `en` or `ru`; target language is `ja`.
- Authored language metadata must feed the generated manifest and content version. Exact transport
  version and legacy compatibility belong to the linked schema work item, not an improvised bootstrap manifest.
- New Russian packages must be safely refused by older apps, not silently treated as legacy English content.
- Newly generated English packages must remain readable by the currently released English app unless their own
  format change needs a separately staged compatible-APK-first rollout. RU reader versioning must not silently
  raise every EN manifest's version.
- Stable Japanese identities, filenames, readings, exercise IDs, structural metadata, and existing
  persisted app mode identifiers do not become Russian prose.
- Separate repository-scoped progress initially; switching back restores that repository's history.
  Built-in Kana keeps its existing repository-independent history and Latin romaji.

## Coordinated app behavior

- One user-facing language setting: System default, English, and Russian, integrated with Android per-app languages.
- New installs resolve a supported device language; upgrades retain English and their current source
  until explicitly changed. Unsupported device languages resolve to English.
- A user language change chooses the new language's default source. A mismatched custom source
  requires confirmation; an already aligned custom source remains selected.
- Validate a user-selected repository and its language before activation, then align the interface.
  Repository-driven alignment must not trigger another replacement with the default source.
- This intentionally replaces the current eager custom-source switch followed by asynchronous sync.
  Pending candidates remain distinct from the active accepted source; cancellation, navigation away,
  draft edits and later selections cannot be overridden by stale validation completions.
- Change the UI immediately after an approved language change. Use a matching accepted cache offline,
  or a localized download/retry state. Never substitute untranslated English lessons.
- Retain previous caches, source selections and progress without deleting or merging them.
- Reject unsupported language/target declarations and unexpected language changes in ordinary sync.
  Pending requests, stale completions, process interruption and Android Settings changes need explicit state rules.
- Do not replace an active question or listening capture. Ordinary sessions finish or explicitly leave;
  durable listening resumes under its captured source/language with a disclosed return policy.

## Russian teaching and publication

- Translate every learner-facing meaning, explanation, instruction, rationale, glossary, caption,
  curriculum label and feedback surface. Developer documentation and technical identifiers may stay English.
- Treat the reviewed English source and its evidence as a reliable starting point, not an infallible authority.
  Preserve unchanged Japanese claims and source qualifications; flag known defects or unresolved evidence.
- Re-inventory active EN instruction/agent entry points at a fresh pinned revision immediately before RU
  instruction authoring, compare with the planning snapshot and reconcile intervening changes before adoption.
  Explicitly close inherited scoped-guidance gaps for grammar, counters, scenes/images and curriculum;
  copying the planning snapshot's six files does not establish completeness.
- Remove comparisons that require English knowledge while retaining the Japanese rule they explained.
  For `words/待つ.md`, removing the English "wait for" comparison must not remove awaited-person `を`
  or waiting-place `で` guidance. Useful Russian-specific clarifications need their own scoped review.
- Adapt natural Russian meaning and terminology, not word-for-word glosses. Do not map Japanese
  particles mechanically to Russian cases or Japanese aspect to Russian perfective/imperfective pairs.
- Preserve Japanese examples, answer classes, IDs, evidence placement, levels and dependency ownership
  unless a separately justified teaching correction is reviewed. Translated choices need a fresh ambiguity check.
- Reuse verified unchanged Japanese audio, text-free images and strokes with their licenses and hashes.
  New content/package approval is not inherited from an English edition's prior device or spending approval.
- Add applicable `NOTICE.md` and source-specific license/attribution records with the first adopted third-party
  material; the repository's default license does not override asset or dictionary exceptions.
- Publish coherent reviewed stages, with all required links and prerequisites present and no English fallback.
  Select the first exact file/ID cohort in its own work item; no full-corpus or native-speaker claim is implied.

## Keeping editions aligned

- Pin exact English commit SHAs; immutable tags are readable milestones, not a mutable "caught up" pointer.
- A Russian-owned contributor ledger tracks the adopted scope, per-document English source hashes/revisions,
  reviewed Russian revisions/hashes, explicit pending/out-of-scope items, and intentional adaptation decisions.
- Advance a scoped checkpoint only when every relevant change in that scope has been reconciled.
  Initial planning baseline is not an alignment checkpoint; the initial translated set is empty.
- Report added/changed/removed/renamed files, structured Japanese metadata changes, links, prerequisites,
  media and guidance changes. Hash comparisons detect change, not linguistic validity.
- Automated reports may propose update work but never merge English over Russian prose or publish unchecked translations.
- Contributor drift-report availability never gates offline study or last-known-good accepted content.
- Preserve Russian-specific notes and different Russian quiz exclusions as explicit adaptations.
  Japanese teaching defects discovered in Russian work should be reported upstream rather than silently diverging.

## Planning source and work items

The source snapshot inspected for planning is English commit
[`f11187ad9eda7da8fbea2da90e8f9a77e46b2c36`](https://github.com/stop-cran/learning-japanese/tree/f11187ad9eda7da8fbea2da90e8f9a77e46b2c36).
It establishes provenance only; no translation is claimed to be complete at that revision.

| Work | Issue |
| --- | --- |
| Complete Russian contributor instruction adaptation | [RU #1](https://github.com/stop-cran/learning-japanese-ru/issues/1) |
| Upstream provenance and drift reports | [RU #2](https://github.com/stop-cran/learning-japanese-ru/issues/2) |
| First coherent reviewed Russian publication | [RU #3](https://github.com/stop-cran/learning-japanese-ru/issues/3) |
| Shared language contract and compatibility | [EN #61](https://github.com/stop-cran/learning-japanese/issues/61) |
| Complete app localization | [Android #28](https://github.com/stop-cran/kanji-cards-android/issues/28) |
| Coordinated app language/source transitions | [Android #127](https://github.com/stop-cran/kanji-cards-android/issues/127) |

Independent plan review and maintainer reconciliation belong to these work items.
They do not replace later review of implemented instructions or actual translated content.

The [cross-repository plan review](https://github.com/stop-cran/learning-japanese-ru/issues/4#issuecomment-6599252027)
and [dedicated instruction-plan review](https://github.com/stop-cran/learning-japanese-ru/issues/1#issuecomment-6599291063)
have been reconciled with their original reviewers; no unresolved plan findings remain from those bounded reviews.
Actual instruction implementation and Russian publication remain open work items.
