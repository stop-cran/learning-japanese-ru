# Batch 143 correction follow-up review

- Frozen English source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`
- Corrected candidate: `d206576631135f27b43fd0136d18652cb2ba96fc`
- Pre-mutation correction amendment: `3eb40c5cb9d0185ccd89abfff369a815984b4a37`
- Review type: independent, read-only, focused follow-up
- Result: **PASS WITH QUALIFICATIONS**; the reported correction resolves the finding.

`kanji/許.md` now says `もと`, consistent with its `kunyomi: [ゆる.す, もと]` metadata and the frozen English source. Rebuilding the manifest in memory produces the same manifest as the corrected candidate. Relative to the pre-correction candidate, the manifest changes exactly the `kanji/許.md` hash and derived `contentVersion`, from `57dc9b54ea36d5c9` to `fdcb38de679a3f19`. The correction commit changes only `kanji/許.md` and `manifest.json`; no other runtime paths changed.

No remaining or new actionable issue was found within this focused scope.

All 18 direct negative/fallback directions remain **UNVERIFIED**, with no transitive closure. This is not candidate acceptance and does not imply runtime, device, media, activation, or release approval.
