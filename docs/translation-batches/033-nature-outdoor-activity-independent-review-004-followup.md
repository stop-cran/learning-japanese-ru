# Review 004 follow-up: provenance corrections

**Final verdict reported by the reviewer: APPROVE WITH NOTES.** No blockers remain
in the corrections reviewed. The timing note is satisfied by adding this record
before commit; the plan's existing link now has a target.

**Date:** 2026-11-11.
**Reviewer session:** `a5da29cd-cb6d-4a24-be85-c7e20079cf88`, the same independent
reviewer as [review 004](033-nature-outdoor-activity-independent-review-004.md).
**Snapshot:** uncommitted candidate on `ru-sora-nav-amendment`, based on
`f940768c96f7a556d2e6cf71303d53190bf48828`; exact final bytes are listed below.
**Scope:** the source-handling and review-status corrections to the excluded
draft's supporting records, not a new linguistic adjudication of the quiz pairs.

This is an author-maintained summary of the reviewer's two read-only follow-up
reports, not a further independent review of this summary. Saved-report hashes
below identify the reviewer's saved files, including their CRLF line endings;
they are not hashes of message, stdout-wrapper or network-return bytes.

## Round 1: rejected, then corrected

The reviewer reported **REJECT current delta pending two narrow corrections**.
The saved report was 6,726 bytes, SHA-256
`241a4f8481401ec13452616fe7fb6884384bd615565872d20ee21952b9889c03`.

| Finding in round-1 bytes | Correction | Final status |
| --- | --- | --- |
| Evidence record lines 56/70 claimed no source renderings were reproduced, but isolated WARODAI-derived words remained at lines 152/219/289. This was a provenance-claim inconsistency, not a legal infringement finding. | Replaced the source-specific words in V2, K1 and the unsupported-claims note with descriptions; separated project/search terms from source material in the citation policy. | Resolved in round 2. |
| Plan lines 6853-6854 said the follow-up had already checked the corrections before it was recorded. | Replaced the result claim with an outcome-neutral pointer to this record. | Resolved in round 2; target added before commit. |

Other round-1 findings: source licence identities and case facts were supported;
the persisted review-004 copy contained only the declared portability,
provenance-note and example-omission changes. Its findings, Q1-Q5 and C2 boundaries
were intact. The reviewer confirmed the original amendment/evidence hashes
`7fa75ff68c1340320e288bb8b1608274bdc4d666a03d95f8b63d90fd014d9364` and
`34a56380ac754bc3621a0a5639365b9c7b06afd50edf4061fc34884a9e5f3653`.
No local absolute/session-store path was found in the reviewed scope.

Round-1 evidence was 15,210 bytes,
`0109fa2a0430eeee1e5097e1553702d8690dcf573512e2cf516ddc86a4e0aef0`;
amendment was 8,990 bytes,
`ba8cf023c050c55e3bc93a62566da6df40aaac4c3f0f3b186098926924d1b1d4`;
plan was 499,072 bytes,
`56ed975cb167281705aa9a57a1141a3683336f9965e9451f1f989c646be0839c`.

Reported read coverage: complete evidence, amendment and persisted review-004
records; complete plan and methodology diffs; tracking diff around
`unverifiedDrafts[0]` only (amendment review, evidence paths, card hashes and
unchanged status/runtime fields). The reviewer hashed all seven candidate files,
compared the persisted report with the saved original, parsed the cited JMdict
IDs from the supplied gzip release, and checked these sources:

- [EDRDG licence](https://www.edrdg.org/edrdg/licence.html), section 3.
- [WARODAI source LICENSE](https://github.com/WarodaiProject/warodai-source/blob/master/LICENSE);
  footers of [About](https://warodai.ru/about/),
  [README](https://warodai.ru/about/readme/) and
  [lookup](https://warodai.ru/lookup/index.php), plus the About history statement.
- [Kotobank terms](https://kotobank.jp/rule/) and the
  [first](https://kotobank.jp/word/%E7%A9%BA-54809) and
  [second](https://kotobank.jp/word/%E6%97%85%E3%81%AE%E7%A9%BA-562279)
  entries cited in the evidence record.
- WARODAI API articles 001-51-23, 009-24-70, 007-27-85, 002-00-71,
  001-19-42, 003-00-60 and 006-02-83, and the two no-hit exact-string lookups
  described in the evidence record; this repository's LICENSE, README and NOTICE.

## Round 2: approved with notes

The saved report was 2,708 bytes, SHA-256
`b74b4d18f8bfded60299d46ad4feb11547cb088e7670f9dcabc9e2d81f1bbf10`.
The reviewer reported all five checks **PASS**:

1. The evidence record's no-reproduction statements now hold; no
   WARODAI/Kotobank entry-body wording is copied.
2. The citation policy and unsupported-claims note distinguish project/search
   terms from source material without attributing them as source renderings.
3. Plan lines 6852-6856 state no follow-up outcome and distinguish review 004
   from further C2 work. The sole timing note requires this record before commit.
4. Amendment lines 114-129 correctly record the round-1 and final evidence
   sizes/hashes; JSON parses and the final size/hash match the evidence file.
5. Both round-1 blockers are resolved; no other round-1 finding remains open.

Exact reported round-2 read coverage: full evidence and amendment records;
plan lines 6847-6860, with its full-file hash computed. Review 004, tracking,
methodology and the card were hash-only unchanged context in this round.
The reviewer parsed JSON with `python -X utf8 -B`, checked cross-record size/hash
fields, and ran `git diff --check` successfully. No dictionary pages were reopened.

## Final candidate bytes

All paths are repository-relative. These are full-file raw SHA-256 hashes, not
claims that every file was read in full in round 2; read coverage is stated above.

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| `docs/translation-batches/033-nature-outdoor-activity-sky-sense-evidence-qualification-001.json` | 15864 | `0a5bd448483961846e29e058ce687bdb6c6aaf5066c599b1ae68dc9835e719dd` |
| `docs/translation-batches/033-nature-outdoor-activity-sky-draft-amendment-001.json` | 9441 | `b79f11d3e0e54de3c5eb55c2cdf5918b75a1c8a4f2bf44287531663de1b72a0d` |
| `docs/FULL-TRANSLATION-PLAN.md` | 499159 | `8286a9a1e781b4f52e3ed977ccd6c5c80d0f732e3f9b14f9161f77d12b174be7` |
| `docs/translation-batches/033-nature-outdoor-activity-independent-review-004.md` | 10818 | `47d4c6cd988a7a2fe82424ca0bf8688c72e2debe82a1134470da25672828929e` |
| `docs/translation-tracking.json` | 8369125 | `b4685ebaa3b13f5144fca03d8aadef13da0a567dc117b74c437dbae5e89948ab` |
| `docs/translation-methodology.md` | 32929 | `d7b047f51a214b640c3f30e05eaabb6456db46bd5ea550fdcff1e5429c4c7840` |
| `docs/translation-drafts/033-nature-outdoor-activity/words/空.md` | 3857 | `97613d8959309dda4233a4f63ad2de635db4f09e6c229103860d1140640ae5d9` |

This follow-up record is the only candidate file added after round 2. The seven
files listed above retain the reviewed bytes; their follow-up pointers were
already present during review.

## Limits

The amendment remains approved for the excluded draft only. Both pairs
`[空, 遠く]` and `[空, 遠い]` remain C2 **UNVERIFIED** in both Japanese-to-Russian
and Russian-to-Japanese directions. Neither CLEAN nor DIRECT EXCLUSION WARRANTED
is established, and no new guards are added. Further direct Russian-usage
evidence or adjudication for the actual quiz titles is still required.

The card remains runtime-absent and pending; no manifest or progress change is
part of this amendment. This narrow read-only follow-up is not a legal opinion,
native-speaker certification, broader content approval, C2 resolution, or runtime,
device, media, activation, release or checkpoint authority.
