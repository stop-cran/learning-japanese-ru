# Batch 143 independent review

- Frozen English source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`
- Initial candidate reviewed: `d5d613cad6fdbb48dd649d7dc0abc9c12b72115e`
- Review type: independent, read-only
- Result: **NEEDS FIX** for one medium reading-transcription error; scope and coverage otherwise complete.

## Scope and evidence

Reviewed the six new lessons `kanji/{解,記,訪,許,認,誤}.md`, their frozen English lessons and stroke assets, the four NAV-only edits `words/{理解,日記,訪ねる,記号}.md`, and the Batch 143 intake, freeze, navigation, and manifest amendments. Japanese metadata, readings, examples, stroke counts, radicals, and direct distractor IDs matched the frozen source except for the Russian prose error below. All six stroke assets were byte-identical to the frozen source. All relative Markdown links in the ten assigned lesson and word files resolved.

The candidate manifest contained exactly 12 authorized registrations and four authorized word-page hash updates, plus the derived `contentVersion`. No other candidate runtime paths were changed.

## Finding

**Medium — `kanji/許.md:29` (confidence 10/10).** The Russian sentence said that metadata retains reading `も`, while both the metadata and frozen English lesson specify `もと`. This makes the reading inaccurate and could confuse learners. Correct the sentence to say `もと`.

No optional polish was identified.

## Limits

All 18 direct negative/fallback directions remain **UNVERIFIED**; no transitive closure or quiz-safety claim was inferred. The frozen dictionary capture identities and cited entries were recorded, but no fresh record-level dictionary re-review or native-speaker naturalness/universal-frequency claim is made. This review does not certify runtime, device, media, activation, release, or full-translation readiness.
