# Batch 149 independent review

## Candidate and verdict

- Initial reviewed candidate: `eca81ad7ab5805bd0c6118f452268f0019698067`
- Final candidate after focused corrections: `63207618ebb7ab34234e25764b8cdd13d88e2126`
- Branch: `full-ru-149-n3-346-355-kanji`
- Frozen English source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`
- Published baseline: `5f6932e4c9d314fc9194374bb48eece0faab4cce`
- Final verdict: **PASS WITH QUALIFICATIONS**

The initial read-only review found three actionable issues. All three were
corrected in the final candidate and independently confirmed in the focused
follow-up below. The initial findings apply to the initial candidate; the final
verdict applies to the final candidate SHA above and remains qualified as
described here.

## Actionable findings

1. **P2 — Preserve the noun sense of 陽気; high confidence.** At
   `kanji/陽.md:39`, “жизнерадостный; о погоде или времени года — тёплый,
   приятный” teaches weather/season as adjectives and omits the frozen source's
   explicit noun senses. Restore the distinction, for example:
   “жизнерадостный; как существительное — погода; время года”. This compares
   the frozen lesson and does not claim a fresh dictionary review.
2. **P2 — Restore the ケン reading-table example; high confidence.** At
   `kanji/険.md:34`, the ケン row omits 冒険（ぼうけん）— adventure, present in
   the frozen reading table. Its occurrence in prose and the common-word list
   does not preserve the table example required by the semantic freeze. Restore
   it in the row, without creating a word page.
3. **P3 — Preserve existing source navigation; high confidence.** At
   `kanji/険.md:21`, the source-linked 危険 occurrence was made plain text,
   despite `words/危険.md` being available in the published baseline. At
   `kanji/静.md:24`, the source links from 青 and 争 to the sibling lessons
   `kanji/青.md` and `kanji/争.md` were also removed; both targets exist in the
   baseline. Restore these three links without changing their visible text.
   The existing unavailable-reference amendments do not cover these available
   targets.

## Reviewed scope and positive checks

The reviewer read all ten Russian lessons and frozen English counterparts:
`kanji/除.md`, `kanji/険.md`, `kanji/陽.md`, `kanji/際.md`, `kanji/雑.md`,
`kanji/難.md`, `kanji/雪.md`, `kanji/静.md`, `kanji/非.md`, and `kanji/面.md`;
all ten stroke assets; the complete diffs for the twelve authorized reciprocal
word pages; the full manifest delta and builder algorithm; and the intake,
semantic freeze, source-link amendments 001–005, and manifest-generation
amendment.

- Frozen lesson byte lengths and SHA-256 values match intake. The frozen N3
  snapshot hash also matches. Japanese front-matter fields other than
  intentionally translated titles match the frozen source, including IDs,
  JLPT, tags, strokes, radical glyphs/numbers, complete reading lists, and
  ordered direct distractors. Cited JMdict entry-ID sequences are preserved.
- Mnemonics are framed as modern visual aids, not historical etymologies;
  JLPT is qualified as a community list.
- All ten stroke assets are byte-identical to frozen source and match the
  intake lengths and hashes: 除 2461 bytes; 険 2689; 陽 2916; 際 3366; 雑 3374;
  難 4282; 雪 2698; 静 3372; 非 2014; 面 2240.
- Each of the twelve reciprocal word-page diffs is navigation-only: removing
  the kanji-link wrappers reproduces the baseline text. No metadata, readings,
  examples, quiz exclusions, or other teaching content changed in those pages.
- Unavailable source references remain visible, with readings and no Markdown
  links: 除く three occurrences (`kanji/除.md:20,32,38`), 雑草 three
  (`kanji/雑.md:21,31,38`), 有難い one (`kanji/難.md:40`), and 非常口 three
  (`kanji/非.md:21,31,37`). No corresponding word page is added or modified.
  `kanji/面.md` correctly retargets its single 顔 reference to the existing
  `../words/顔.md`; that word page is unchanged and no 顔 kanji lesson is added.
- The candidate commit changes exactly 33 authorized runtime paths: ten new
  lessons, ten new stroke assets, twelve existing reciprocal word pages, and
  the manifest. There are no quiz/grading/answer/exclusion/fallback-code
  changes or additional candidate paths. Eleven documentation paths differ
  from the published baseline only through the preceding documentation,
  publication, and freeze commits.
- The manifest has exactly twenty new registrations and the twelve authorized
  existing hash changes, no removals or unrelated hashes, and no unrelated
  top-level changes. Baseline manifest SHA-256:
  `47b338aa1a4cd7aa09eeb030d4e0b15024b30f6b9560dc0ba230f31ee277caf8`.
  Candidate manifest SHA-256:
  `e3f95676704ee0e94f5367968d2a1c197dc240364351eb9a62a7bb7173584340`.
  An in-memory builder recomputation reproduced the exact manifest object and
  serialized bytes, including normalized text hashes and contentVersion
  `673b1de0a1f88034`. This establishes content consistency, not historical
  proof of which command authored it.

## Direct negative/fallback boundary

All **30** directions remain **UNVERIFIED**:

- 除→降, 除→院, 除→都
- 険→限, 険→院, 険→験
- 陽→院, 陽→場, 陽→際
- 際→陽, 際→院, 際→題
- 雑→難, 雑→集, 雑→新
- 難→雑, 難→集, 難→親
- 雪→電, 雪→帰, 雪→書
- 静→青, 静→持, 静→帰
- 非→北, 非→耳, 非→年
- 面→目, 面→百, 面→同

The four internal directions are 陽→際, 際→陽, 雑→難, and 難→雑. The
21 distinct external target lessons exist in the published baseline. That
establishes direct target availability only—not transitive closure,
negative/fallback behavior, or quiz safety. The intake, freeze, and amendments
retain the explicit UNVERIFIED limitation; this review does not upgrade it.

## Qualifications and read-only assurance

This was the single independent review; no other reviewer was spawned. No files
or Git state were intentionally modified, and no checkout, switch, commit,
stash, reset, or frozen-source alteration was performed. Candidate workspace
contents match the exact SHA (allowing checkout CRLF normalization); HEAD
remained the candidate. The pre-existing untracked `tools/__pycache__/` was
left untouched. Builder equivalence was checked in memory only. The parent's
reported builder, validator, 124 unit tests, and content-budget results were
not rerun or represented as fresh review executions.

This is bounded static source, translation, navigation, and manifest review
only. It does not establish a fresh record-level JMdict review, native-speaker
frequency/naturalness certification, runtime/device/media/activation/release
approval, checkpoint authority, or full translation completion.

The complete findings, exact candidate SHA, reviewed scope, and qualifications
were sent directly to the coordinating writer by reviewer session
`f7d3cb80-c5d5-4ec6-b305-1d6ce07ddb8b`.

## Focused follow-up

- Final candidate: `63207618ebb7ab34234e25764b8cdd13d88e2126`
- Initial candidate: `eca81ad7ab5805bd0c6118f452268f0019698067`
- Verdict: **No remaining actionable finding within the focused correction
  scope.** This is not runtime, activation, or release approval.
- Reviewer session: `e877613a-57f9-4fd0-bd11-51b3b418b4ff`

The follow-up confirmed:

- `kanji/陽.md:39` retains “жизнерадостный; как существительное — погода; время
  года”, preserving the noun senses of 陽気 alongside the adjective sense.
- `kanji/険.md:34` restores 冒険（ぼうけん）— приключение in the ケン reading
  table, and `kanji/険.md:21` restores the link to `../words/危険.md`.
- `kanji/静.md:24` restores `[青](青.md)` and `[争](争.md)` without changing
  their visible Japanese or surrounding sentence.
- All three targets exist in both the frozen source and published baseline,
  resolve in the candidate, and are unchanged since the initial candidate.
  The complete three-lesson correction diff has only these intended changes;
  no unrelated metadata, readings, examples, or surrounding teaching content
  changed.
- The runtime correction commit changes exactly three lessons and generated
  `manifest.json`. Three added documentation paths in the preceding scope
  commit—this review report, manifest-generation amendment 002, and
  source-link amendment 006—are evidence records, not runtime drift.
- Since the initial candidate, only hashes for `kanji/陽.md`, `kanji/険.md`,
  and `kanji/静.md` change in the manifest, with contentVersion
  `e6af7c1b1614f5ca`; no registration is added or removed and no other payload
  changes. Final manifest SHA-256:
  `44297ce2093d442d2316e14682ccedc0aea557583e9353977b49564b602c9c6a`.
  The unchanged manifest delta from the published baseline remains twenty new
  registrations, twelve pre-authorized existing word hash changes, no
  removals, and no unrelated hashes.

All thirty direct negative/fallback directions remain **UNVERIFIED**. No
transitive closure, negative/fallback behavior, or quiz safety is inferred.
The follow-up independently inspected the correction diff, the three lessons
and frozen counterparts, target continuity, amendment scopes, manifest hashes,
and builder hashing/serialization rules. It did not execute the builder,
validator, tests, or budget check; those are parent-provided successful results.
No files, Git state, or frozen source were modified by the reviewer. No fresh
JMdict record-level review, native-speaker frequency/naturalness certification,
runtime/device/media/activation/release approval, checkpoint authority, or full
translation completion is claimed.

The complete focused follow-up findings, exact candidate SHA, scope, and
qualifications were sent directly to the coordinating writer by reviewer
session `e877613a-57f9-4fd0-bd11-51b3b418b4ff`.
