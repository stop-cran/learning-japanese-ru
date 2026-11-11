# Batch 151 focused correction follow-up

**Verdict: pass for the two authorized corrections** (high confidence within
scope).

**Candidate:** `49b94223bb7e1a7a3de7529332f9130d92bbe6c8` (verified current
HEAD). **Initial candidate:** `23ee92cc6ef668da2b4c99aeaaa512dea0c3f90b`.
**Amendment:** `docs/translation-batches/151-hair-call-n3-kanji-correction-amendment-001.json`.

Compared the complete `kanji/鳴.md` delta between the candidates, read the
amendment and corrected lesson, checked the `kanji/口.md` target, and compared
the manifests. The only lesson edits are the two authorized corrections:
restore `[口](口.md)` in the modern-shape mnemonic and state that 口 is inside
門 in 問. The linked targets `kanji/口.md` and `kanji/問.md` both exist.

No other lesson text, metadata, readings, examples, citations, stroke assets,
or word pages changed. The candidate delta paths are the lesson,
`manifest.json`, and the added correction amendment. The manifest changes only
the `kanji/鳴.md` hash and `contentVersion`, with no registration changes; its
lesson hash matches the file's SHA-256. Initial findings B151-R1 (missing
navigation) and B151-R2 (lost enclosure contrast) are both **resolved**. No
remaining actionable issue was found in the focused correction scope.

The frozen English source commit is recorded in the amendment as
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`, but was not present in the
reviewer's checkout, so this follow-up did not independently reopen it. The
initial review did inspect the exact frozen source and established the reported
baseline findings.

The six direct negative/fallback directions 髪→長/友/夏 and 鳴→鳥/問/駅
remain **UNVERIFIED**. No transitive closure or quiz-safety conclusion is
inferred. No fresh JMdict record-level review, native-speaker certification,
runtime, device, media, activation, release, checkpoint, or full-completion
approval is claimed.
