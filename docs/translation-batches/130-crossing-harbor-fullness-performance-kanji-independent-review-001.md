## Snapshot and scope

**Candidate:** `e539cf3c51bfe5fb38621e36fc172effa2f37003`  
**Comparison:** `6a1bb488ecfc1926f6fb2e57962b1fee40174fc2` → candidate. The supplied base is an ancestor, but not the candidate’s direct parent; the direct parent is `6648ea9ce6f0b9521479ae7793810beea471eeab`.

Read the requested Russian instructions, format/methodology documents, and all three reviewer-agent files; the signed batch-130 intake, semantic freeze, and both pre-mutation navigation amendments; both actual primary-capture files; all four Russian lessons and frozen English counterparts; all four stroke files; the five amended word pages; and the six existing direct-provider cards.

The scoped runtime changes are the four lessons, four stroke files, and five word pages, plus the generated `manifest.json`. The broader base-to-candidate diff also contains documentation changes; I did not review the other plan updates or the batch-129 record.

## Verdicts

- **C1 — Japanese correctness/evidence: UNVERIFIED.** No supported Japanese-content defect found. KANJIDIC2 capture records support the four cards’ readings, stroke counts, grades, and classical radical; the read JMdict records support the checked word forms, readings, and cited senses. The capture does not include a standalone `バス` record, so it does not independently establish the naturalness of `バスは満員です`; the example is preserved from the frozen source.
- **C2 — Scope/dependencies/quiz coverage and safety: UNVERIFIED.** The inspected runtime scope matches the batch: seven optional wrappers were removed as amended, and the five existing word changes are exactly the authorized single-link insertions. The four stroke files’ raw bytes match the frozen source. All 12 direct distractor directions remain **UNVERIFIED**: the cards and Russian meanings were compared, but no app/runtime operation or sense-guard evidence was inspected, so metadata or title differences do not establish quiz safety.
- **C3 — Russian novice comprehensibility: UNVERIFIED.** The text-only pass found no supported novice-blocking defect. This is not a native-speaker assessment.

## Findings

**None supported in the reviewed scope.**

## Material limits

No validator, app/runtime, frequency, device, visual/handwriting, or release acceptance was performed. Stroke verification was byte-only. This review is not native-speaker acceptance or approval of quiz guards.
