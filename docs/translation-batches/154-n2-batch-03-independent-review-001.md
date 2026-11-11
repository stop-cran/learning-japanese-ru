# Batch 154 review evidence status

- Candidate: `5a1614d1ee055b2cb309d0811f324baf068a7022`
- Parent: `2af442b36de22a2883247292429dc0dc049542ee`
- Frozen English source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`
- Published Russian baseline: `f940768c96f7a556d2e6cf71303d53190bf48828`
- Status: **The methodology-required semantic review and final copy-edit review are complete; acceptance/publication work remains pending.**

## Original review attempts

The authenticated GitHub REST attempt could not access the unpushed candidate,
its parent, or the stated frozen-source commit. That attempt was not a content
review.

The coordinator reports that the original reviewer's first local mechanical
script exited 1 because paths were not normalized. Its corrected link script
also exited 1, due to Unicode output handling. Neither command is a successful
check, and neither is recorded as one. The exact command strings and returned
outputs are preserved in the separate coordinator session artifact
`C:\Users\stop-\.copilot\session-state\68a44f7f-62db-4755-8296-fd586c861a35\files\batch-154-reviewer-failed-command-evidence-20261111.json`
(SHA-256 `198b9edbd7f1627914044ca8dcf62a9ef1d00b8d2e5bbdd9ca654caccdc0ede4`).

The reviewer report did not separately state verdicts for Japanese factual
accuracy, completeness/fidelity of the declared teaching scope, and Russian
clarity, as required by `docs/translation-methodology.md`. The general approval
and mechanical/metadata observations do not substitute for those judgments.

## Coordinator's separate mechanical rerun

The coordinator separately reports a successful read-only rerun (exit 0)
against the exact candidate and frozen source: 38 expected diff paths; all 15
source lesson byte lengths, SHA-256 values and Git blob IDs match the freeze;
all 15 stroke blobs match the frozen source and their recorded length, hash and
blob IDs; all 34 added/changed manifest hashes match candidate bytes; the four
existing-word edits are navigation-only; all lesson links resolve; and
`git diff --check` passes. This is coordinator-run mechanical evidence, not
the reviewer's semantic verdict or a pass for either failed reviewer command.

## Semantic review and copy-edit follow-up

The actual 15-card semantic reviewer's full returned report is preserved
separately in
`docs/translation-batches/154-n2-batch-03-semantic-review-001.md`. It gives
distinct per-card verdicts for Japanese factual accuracy, source-scope fidelity,
and Russian clarity, with the recorded evidence limitations. Its disposition
is a qualified pass with minor Russian copy edits recommended; it identifies
no supported Japanese-content blocker. That report does not include the
coordinator's mechanical rerun or treat the original failed scripts as passes.

The same reviewer first checked the six copy-only edits and resolved five,
while flagging an unsupported “rare” characterization in the 卒 reading. That
actual report is preserved separately in
`docs/translation-batches/154-n2-batch-03-semantic-review-followup-001.md`.
After removing `редкое`, the same reviewer completed a final read-only
follow-up with **PASS**: all six current file hashes and base blobs match the
hash-bound amendment record, the other five edits remain within the approved
copy-edit scope, and the final 卒 wording retains the Jōyō explanation without
the unsupported frequency claim. The actual final report is preserved in
`docs/translation-batches/154-n2-batch-03-semantic-review-followup-002.md`;
the exact base and six base/candidate blob and SHA-256 values are recorded in
`docs/translation-batches/154-n2-batch-03-review-copy-amendment-001.json`.
The reviewer slot was released back to N1 after this PASS.

The six reviewed card changes and regenerated manifest remain uncommitted at
the exact reviewed base `5a1614d1ee055b2cb309d0811f324baf068a7022`. Thus the
review stage is complete, but acceptance records and publication are still
pending.

## Amended-candidate mechanical checks

After the six copy edits, the author regenerated `manifest.json`; the builder
reported 2,834 files and manifest version `bf7b6777ce64110f`. The subsequent
`python tools\\validate.py` run reported `0 error(s)`. The required serial
checks then passed: `python -m unittest discover -s tools -p "test_*.py"`
ran 124 tests successfully, and `python tools\\check_content_budget.py`
reported 2,842 files, 2,851 entries and 7,869,207 retained bytes. These are
author-run checks for the amended candidate, separate from the coordinator's
earlier mechanical rerun of the original `5a1614d` files and from all reviewer
verdicts.

The parent session also independently checked structural invariants for the
same six-card worktree snapshot: unchanged `5a1614d` frontmatter, Japanese-token
multisets, ordered Markdown links and seven-digit source IDs. This was
structural evidence only, not a semantic review; its six reported blob IDs
match the hash-bound amendment record.

All 45 direct distractor directions remain **UNVERIFIED**; no transitive
closure or quiz-safety conclusion is inferred. No fresh record-level JMdict
adjudication, native-speaker certification, runtime/device/media release or
ordinary activation approval, checkpoint authority, or full-translation
completion is claimed.
