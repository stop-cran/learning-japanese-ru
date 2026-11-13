# Candidate-byte-review status clarification

**Scope:** Focused follow-up to the independent changed-byte review of the post-B158 held 空 (C2) candidate. This note addresses only whether its `candidate-byte-review-pending` status would be accurate if the exact candidate tracking bytes were published as current. It does not revise the prior review verdict, re-adjudicate the linguistic basis, or authorize publication, runtime adoption, or any candidate edit.

## Assessment

The status `coordinator-accepted-conservative-exclusions; candidate-byte-review-pending` is stale for a live publication after completion of the independent post-B158 candidate-byte review. The field has no timestamp or qualifier that makes “pending” explicitly historical or attributable to another review gate. Publishing it as current would suggest a review step remains outstanding when the scoped review has completed.

This conclusion is separate from the C2/runtime disposition, which remains unresolved and held. The candidate must retain its conservative, qualified scope and must not imply that runtime behavior is approved.

## Precise evidence

- In `candidate/docs/translation-tracking.json`, the sole `unverifiedDrafts` record for `words/空.md` has `c2DirectExclusionDisposition.status` equal to `coordinator-accepted-conservative-exclusions; candidate-byte-review-pending`.
- That same record independently retains `facets.C2: UNVERIFIED`, `reviewStatus: unverified`, `runtimeAcceptance: blocked-by-evidenced-linguistic-uncertainty`, `runtimeAuthority: null`, `targetObjectRemainsPending: true`, both `openQuestions` (`空`–`遠く` and `空`–`遠い`), and `runtimeGuardActive: false`. These represent the still-valid conservative/runtime hold, not a pending byte review.
- `candidate/docs/translation-batches/033-sora-c2-direct-exclusion-qualification-001.json` likewise says `status: coordinator disposition recorded in candidate; changed-byte review pending`; its `limits` say the new guard and tracking bytes require separate independent review before acceptance. These statements describe the review state when the candidate was prepared, not a separately identified outstanding gate after the review completed.
- The prefatory note in `candidate/docs/translation-batches/033-sora-c2-changed-byte-review-001.md` says the historical review covers the pre-B158 candidate and that the post-B158 tracking rebind and transformed evidence need separate independent review. This identifies the pending review that the completed follow-up addressed.
- The completed follow-up is the read-only independent review saved at `docs/translation-batches/033-sora-c2-post-b158-rebind-independent-review-001.md`, SHA-256 `e19d49462472c7200bf7a560bcfd6fe1e509cbc19a482cefe05674afb6de7fb7`. Its verdict is acceptable only as an isolated, held, non-runtime candidate and expressly does not approve publication or runtime acceptance.

## Recommendation and boundary

Before publishing these bytes as current, update only the candidate-byte-review status/provenance to record completion and reference the post-B158 review. Preserve C2 `UNVERIFIED`, its open questions, null runtime authority, pending target, and inactive runtime guard. If retaining the existing bytes as a historical snapshot instead, label the artifact clearly as an as-of-pending record so it cannot be mistaken for live status.

No candidate or prior report was edited as part of this clarification. No claim is made that this note itself authorizes the proposed amendment or any publication/runtime action.
