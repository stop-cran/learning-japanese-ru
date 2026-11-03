# Russian edition: working instructions during localization bootstrap

Audience: Russian speakers learning Japanese without needing English. Japanese and Latin romaji remain learning
content; developer prose and stable technical IDs may remain English.

Read [the design](../docs/DESIGN.md) and [checkpoint implementation plan](../docs/IMPLEMENTATION-PLAN.md) before changes.
Full family-specific authoring/reviewer instructions are still [RU #1](https://github.com/stop-cran/learning-japanese-ru/issues/1),
not completed by this short working guide. Adopt its independently reviewed C2 revision before runtime pilot authoring;
do not copy the EN instruction set or claim that all content guidance already exists here.

## Established adaptation and planning lessons

- Re-inventory all active EN instruction/agent entry points at a fresh pinned SHA before instruction authoring and
  reconcile intervening changes before adoption. The six-file planning snapshot is not a permanent completeness test.
- Deliberately close inherited scoped-guidance gaps for grammar, counters, scenes/images and curriculum, with explicit
  namespace ownership; shared scoped files are sufficient. Evidence: [RU #1 plan reconciliation](https://github.com/stop-cran/learning-japanese-ru/issues/1#issuecomment-6599291063).
- Reviewed EN articles and their evidence are a reliable base, not infallible truth or Russian translation approval.
  Retain Japanese rules, IDs, examples, qualifiers and source provenance. For `待つ`, removing the English "wait for"
  comparison must retain awaited-person `を` and waiting-place `で`. Russian-specific additions need scoped verification,
  not mechanical particle/case or aspect equivalences; see [RU #1](https://github.com/stop-cran/learning-japanese-ru/issues/1).
- A reviewed plan, source hash, parser fixture or copied media approval is not reviewed Russian teaching content.
  Publish complete dependency-closed pilot packages only; no dangling references, English lesson fallback or
  weakened choices/prerequisites merely to make a small pilot run.
- Reuse unchanged verified Japanese assets with notices and exact hashes; no new paid generation or copied phone/
  linguistic approval is implicit. Language metadata must use the adopted compatible format, not an improvised manifest.

## Required correction loop for this project

At each pilot integration gate, reproduce and adjudicate findings before changing behavior. Fix the defect, review
affected code/content, and run affected regressions. Record reusable verified mechanisms/invariants in the corresponding
app, EN/shared-format or RU/translation instructions in that correction batch, linking the actual finding/evidence.
Update the checkpoint plan when scope/dependencies change. No finding quota, speculative mandatory rules or unrelated
instruction churn; unresolved claims stay labeled pending.

Use independent bounded read-only reviews and preserve their scope/dispositions; authoring does not certify naturalness.
Check exact source/RU revisions and item/dependency inventory. Do not delete or merge learner progress, silently overwrite
RU adaptations with EN changes, or move immutable checkpoint tags. Contributor drift services never gate offline study.

## Current limits

No runtime lessons or manifest are present at bootstrap. The interim guide does not waive missing validators, source
notices, authoring guidance, independent actual-content review or release/device acceptance. Implemented capabilities
and unperformed tests must remain distinguishable in every checkpoint report.
