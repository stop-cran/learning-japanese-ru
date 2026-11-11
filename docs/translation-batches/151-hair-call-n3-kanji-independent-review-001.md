# Batch 151 independent review 001

**Verdict: changes requested** within the bounded static-review scope
(high confidence).

**Candidate:** `23ee92cc6ef668da2b4c99aeaaa512dea0c3f90b` on
`full-ru-151-n3-366-367-kanji`. **Frozen English source:**
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`. **Published baseline:**
`3c862d7edc3466feb273fbcf03390e7fbda73177`.

## Findings

1. **P3 — restore source navigation, high confidence.** `kanji/鳴.md:25`
   omitted the frozen source's link from 口 to the existing `kanji/口.md`,
   removing direct navigation to the component lesson.
2. **P3 — preserve the spatial contrast, high confidence.** `kanji/鳴.md:50`
   translated that 問 contains 口 but omitted that 口 is enclosed inside 門.
   The frozen lesson contrasts this layout with 口 beside 鳥 in 鳴.

Both corrections were authorized in
`151-hair-call-n3-kanji-correction-amendment-001.json`.

## Evidence and scope

The review read both complete Russian lessons, `kanji/髪.md` and `kanji/鳴.md`,
and their complete frozen English counterparts, plus the intake, semantic
freeze, source-link and manifest-generation records. Frozen source lengths,
SHA-256 values and Git blobs match the intake. Japanese front matter, readings,
examples, cited JMdict IDs, and direct distractor IDs match the frozen source
apart from the reported spatial detail. Mnemonics remain explicitly modern
visual aids. Both stroke assets are byte-identical to the frozen source.

All remaining local links resolve. The source word links appear three times in
each lesson. The three reciprocal edits in `words/髪.md`, `words/鳴く.md`, and
`words/鳴る.md` add only the authorized wrappers; stripping them reproduces the
prior text. The manifest delta is exactly four added registrations and three
changed word hashes, with no removals or unrelated changes. The first
candidate's content version is `37ecb8db9a16974f`.

## Qualifications

The six direct negative/fallback directions 髪→長/友/夏 and 鳴→鳥/問/駅
remain **UNVERIFIED**. No transitive closure or quiz-safety conclusion is
inferred. This is not runtime, device, media, activation, release, checkpoint,
or full-completion approval. No fresh JMdict record-level review or
native-speaker frequency/naturalness certification is claimed. The review was
read-only; the pre-existing `tools/__pycache__/` was left untouched.
