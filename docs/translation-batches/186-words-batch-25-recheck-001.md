# Recheck — RU batch 186 (186-words-batch-25), fix round

## Snapshot
- Repo `C:\Users\romanko\repos\learning-japanese-ru`.
- Base `ff841a6`; the staged index tree is still `4fdfa8d52a569a9e17217c477f8faab0cc715b70` (`git write-tree`, unchanged).
- The fix round is unstaged working-tree changes: `words/預ける.md`, `words/頼る.md`, `words/雷.md` and `manifest.json` (diff stat: 4 files, +10/−9).
- I did not modify anything (read-only).

## Scope
- I read the full working-tree diff, matching `b186-fix.diff`, and re-read the changed passages in context.
- The manifest hashes for the 3 changed files match the SHA-256 of the files on disk, and `contentVersion` was bumped.
- `link_parity.py` passes for the 3 changed files.
- The other 39 files in the batch are unchanged since the first review, so those verdicts carry over.

## Reconciliation
| Original item | Status | Note |
|---|---|---|
| F1 預ける–頼む guard (Minor) | **Resolved** | `quiz_exclusions: [頼む]` was added to the 預ける front matter, after `tags` and before `---`. The YAML is valid. The direction is right: 頼む is suppressed as a distractor when 預ける is the answer. |
| 依頼 extra guard (conservative) | Optional, declined | Acceptable. 依頼 is a noun, so the risk is weak. |
| 頼る title «на кого-л.» | **Resolved** | The title and H1 are identical: «полагаться; опираться (на кого-л./что-л.)». This now fits the body's uses with maps and experience. |
| 雷 L16–18 wording | **Resolved** | The English comparison was removed, and «предоставить глаголу уточнять» was replaced with «а что именно происходит, уточняет глагол». |
| Extra guards 離れる–別れる, 非常–急, 非常–珍しい, 表面–外 | Optional, declined | Acceptable. Each card teaches the contrast, and EN has no guard. |
| 問い title widening | Optional, declined | Acceptable. The body explains the wider use. |
| 預ける «на ресепшене» | Optional, declined | Acceptable. «стойки регистрации» is correct. |

## Regression check
- **雷 paragraph.** The grammar is correct.
  - «японский может обозначать словом 雷 грозовое явление в целом» has correct government (обозначать что словом).
  - The subordinate clause «а что именно происходит, уточняет глагол» is punctuated correctly.
  - The meaning is unchanged from EN (one word for the phenomenon; the verb specifies).
  - Dropping the English parallel is a valid Russian-reader adaptation.
- **頼る.** The title and H1 agree. «на кого-л./что-л.» is the standard dictionary convention.
  - No body, link or front-matter field changed apart from `title`.
- **預ける.** Only the front matter changed; the guard target 頼む exists in RU. No other field moved.
- No new defects found.

## Verdicts
- Correctness: **CLEAN**
- Scoped coverage: **CLEAN**
- Comprehensibility: **CLEAN**
- Quiz safety: **CLEAN** (F1 resolved)

## Findings
None open.

## Optional
These items were declined as optional and remain optional. None of them blocks the batch:
- Guards 離れる–別れる, 非常–急, 非常–珍しい, 表面–外 and 依頼.
- Widening the 問い title.
- «на ресепшене» in the first 預ける example.

## Limits
- No native-speaker check.
- I did not run quiz behaviour in the app or the full content validator.
- I assume the app applies the exclusion when the excluding card (預ける) is the quiz answer. I did not test the reverse direction, 頼む as the answer with 預ける as a distractor.
  - With 頼む as the answer, prompts are «просить; поручать», and 預ける's title says neither, so the reverse risk is low.
- The Ožegov citation for F1 comes from reference knowledge. I did not fetch it.
- 急's "emergency" sense and ごろごろ's child-language "thunder" sense are still unverified; these were optional items only.
- I did not read the author's report, the batch docs, drafts, tracking files or prior reviews.
