# B257 — original reviews preserved; source acceptance blocked

**Status: not accepted.** Candidate `bd3cb7293fa63d0b8ad59692524d561e2df91678`
(tree `8b50554614afa6e0e4d5f91895425ced03b43387`) remains the unchanged learner snapshot.
The required three distinct actual model families were not obtained. Two original
facets ran once each, serially, under configured default routing; both actually used
GPT. No third reviewer, fixes, rechecks or source acceptance followed.

## Snapshot and preparation

Frozen EN is `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. The candidate's sole parent is
signed seed `8ddfa6793f162d6e896a91417d81b77c511df39e`, whose sole parent is published
B256 `f6b5413d57f17d720301fb9ff8c4130d7e83cfed`. The seed and candidate were GitHub-verified;
their local signing fingerprint matched `D4C9A275A218AF747B787AFA9D94B9D311BD26A7`.

Scope: **30 new N2 word cards, five navigation files with six link insertions,
and the separate existing N3 B203 card 汗**. This is 36 learner payloads, not 31 new
translations or six navigation files. The [intake](257-words-batch-96-intake.json)
separates source/raw/Git/LF hashes, scratch hashes, predecessor and final candidate
hashes. All 35 materializer controls and all 36 final payload controls matched on
the actual seed. Neither scratch history nor its manifest/ledger/progress was copied.

The 61 new-card Japanese sentence/reading layouts were restored before review.
Existing 汗 retains its original B203 full-width-bracket layout, with the same
Japanese sentences and readings as EN; only its Russian explanatory paragraph
changed. 光線's English-only comparison and the two available links to 桁 and 軽い
are explicitly omitted, not recorded as zero lost source links.

Four serial candidate gates passed before signing: manifest generation,
validation (0 errors), 124 unit tests, and archive budget. Content version:
`8280df1bcb5f9963`; local ZIP: 8,468,448 bytes. These are candidate structural
checks, not final acceptance gates or linguistic clearance.

## Same-snapshot original reviews

All reviewers received the unchanged common packet: 31 full numbered EN/RU pairs,
five navigation diffs, separate 汗 before/after diff, 31 dictionary packets,
31 metadata packets, a manifest-verified 4,363-word pool, all 417 heuristic
comparison lines and the same three neutral supplemental locator files.
The packet contains 30 frozen N2 mappings plus 汗's separate N3:22 noun mapping;
the latter does not establish the sentence verbs or particles.

The inventory SHA-256 is `d6a27d79c3a7ff1a5a6a1bc17375b575372701628f42734d7f3ac24b52d1078d`.
Neither author rationale nor another reviewer's findings were supplied in either
original brief. Both reports have **37/37 complete primary units** matched to actual
successful tool returns: 31 pairs, five navigation diffs and the correction diff.
This establishes returned scope, not comprehension.

| Facet | Reviewer ID | Actual responses | UTC interval on 2026-11-24 | Original body bytes / SHA-256 |
|---|---|---|---|---|
| [Correctness / source coverage](257-words-batch-96-review-correctness-001.md) | `11bc0117-0bc5-40ef-9e3c-ba8effd1ae26` | 36 × `gpt-6-astra` | 04:22:36.070–04:39:56.578 | 10804 / `ae3b365a5a8315960837c9042924b4ca843134bbfeb8c9f41a5738e288f3d10a` |
| [Consistency / quiz integration](257-words-batch-96-review-consistency-001.md) | `506797e8-0707-4fcc-91c2-fcccd4d3717f` | 47 × `gpt-6-astra` | 04:40:32.690–04:54:58.568 | 9950 / `7f54fe1d5162278394174a384fe4c49937dbd6c074eb64820a8f20797d40c6d5` |

The first lifecycle start/completion labels named `claude-opus-5.5`, but its
configuration, 118 actual tool-dispatch records and all 36 responses named
`gpt-6-astra`. It is **not** counted as Claude. The second facet's configuration,
73 tool dispatches and all 47 responses also named GPT. Its start followed the
first observed completion. No explicit model overrides were supplied.

Both exact public report bodies also occurred in successful read-only stdout
before their final responses. The [execution record](257-words-batch-96-review-execution-001.json)
preserves lifecycle/configuration/response evidence, source-packet inventory and
actual returned ranges. Report-body hashes, logged tool-content hashes and network
bytes are distinct domains.

## Unresolved contributions

These are preserved reviewer findings, **not completed author adjudications or
approved fixes**. The facet assignments differ; the reports are not model rankings.

| Report finding | Contribution | Status |
|---|---|---|
| Correctness F1 | Proposed direct 工夫–発想 exclusion: the current 発想 answer «идея; подход (к задаче)» can describe the supported result sense of 工夫. | unresolved; no edit or recheck |
| Consistency F1 | Proposed direct 昼寝–夢 exclusion: Russian «сон» in the existing 夢 label can denote sleep as well as a dream. | unresolved; no edit or recheck |
| Consistency F2 | Proposed direct 工夫–仕方 exclusion: «способ; приём» can describe 工夫's resulting method. | unresolved; no edit or recheck |

The reports retain their source citations, optional observations and individual
limits. In particular, metadata-admissible option sets were not observed runtime
sampling; the complete word pool was not semantically rereviewed in every article.
No general Russian-comprehensibility facet was run.

## Stop boundary and retained history

After the first actual-family mismatch, the coordinator required one default-routed
attempt of the distinct consistency facet. If that repeated an already used family,
the instruction was to retain the complete report and stop before fixes or
acceptance, without rerunning a facet in search of another model. That condition
occurred. The three-family requirement was not waived.

Both original reviewer instances reached observed idle state and remain the exact
IDs above for possible bounded follow-up; no replacement reviewer was started.
This documentation-only retention does not change the candidate learner bytes.

The original B203 汗 ledger row, its original adaptation and all six historical
evidence links are unchanged. There is no additional 汗 progress row and no B257
ledger/progress promotion. A final correction note has **not** been appended:
it must describe and bind the final reviewed bytes after the remaining review
requirements and adjudication are resolved.

No signed source-acceptance record or records-revision final-gate receipt has been
created. No milestone issue post, publication, pin change, next batch, device,
media, voice or ordinary activation clearance follows from this retained work.
