# Batch 136 — independent review

**Snapshot:** Candidate `db6dd58af523317fd016aad237db29c17cc31257` on `full-ru-136-mutual-certainty-show-department-extent-kind-kanji`; parent is signed freeze commit `8aa5f8d5a98d10af7992a6a5517ae186f26aa85a`; RU baseline is `2c5afc95fc9cea2740f574b0d53b0603ce8d338b`. The freeze signature verified as good. The frozen EN checkout’s `HEAD` is the specified `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. The worktree also contains an untracked `tools/__pycache__/`, outside the candidate commit.

**Materials read:** The complete candidate and frozen-EN lessons for 相/確/示/科/程/種; the complete RU and frozen-EN lessons for the 13 distinct direct-edge targets 休/本/目/研/集/短/赤/小/木/料/秋/私/重; the batch intake, signed semantic freeze, and pre-mutation navigation amendment; all five modified word pages; and the applicable repository instructions, three reviewer rubrics, translation methodology, and kanji-format guidance. I read all six KANJIDIC2 records and all 18 cited JMdict entries in the supplied primary captures.

**C1 — Japanese correctness: CLEAN, qualified.** I found no concrete mismatch in the checked readings, stroke counts, classical radicals, cited word spellings/readings/senses, or preserved Japanese examples. The N3 classification comes from the frozen community list; I did **not** infer it from KANJIDIC2’s legacy `jlpt=2`. The supplied current KANJIDIC2 and JMdict archives are explicitly **not byte-identical** to their frozen snapshot archives, so the checked capture records are not evidence of frozen-archive identity. This is not a native-speaker or independent naturalness certification.

**C2 — Source completeness, scope, dependencies, and quiz semantics: UNVERIFIED overall.** The selected six characters match the frozen order and scope. The 18 direct edges match the candidate metadata; the only dependency closure within the six-item batch is 程→種, with the other 17 targets already present at baseline. I did not turn the edges into a transitive clique. The five word-page changes match the preauthorized single-wrapper replacements byte-for-byte; the six optional word-link wrappers and one optional article reference are omitted as authorized. I found no new word/article pages or quiz/grading changes. **All 18 ordinary negative/fallback directions remain `UNVERIFIED`; there is no grading approval.**

Directions: 相→休/本/目; 確→研/集/短; 示→赤/小/木; 科→料/秋/私; 程→秋/種/私; 種→重/秋/私.

**C3 — Russian novice clarity: NEEDS FIX.** One confirmed cross-card terminology issue is below. No native-speaker certification is implied.

## Issue: Explain the reading-type labels for beginners
**File:** `C:\Users\stop-\learning-japanese-ru\kanji\相.md:30–32` (same pattern in `確.md:30–32`, `示.md:30–31`, `科.md:31–32`, `程.md:31–32`, and `種.md:31–32`)
**Severity:** Medium
**Problem:** The reading tables label entries only `он` and `кун` without explaining what those categories mean. A beginner cannot tell how the labels relate to the readings and example words.
**Evidence:** The Russian methodology gives “онное чтение (онъёми) / кунное чтение (кунъёми)” as the terms and says to explain them when needed; the comprehension rubric calls for explaining necessary terminology. These are first-encounter lessons for novice learners.
**Suggested fix:** Add a brief learner-facing explanation of both categories in these lessons, or use labels that explain the distinction directly.

**Hash and evidence boundaries:** For all six stroke files, I independently compared raw bytes against the frozen EN source and found them identical. The following pairs are **raw SHA-256 / Git blob ID** respectively; these are distinct hash domains, and both source and candidate matched:

| Kanji | Raw SHA-256 | Git blob ID |
|---|---|---|
| 相 | `3ec451679796dece97ffc60eee2b3df475616b65c3f551a4aea6684ed0057b84` | `57cb1c15b2c9f01e0694d20f8ebfc832bd6d147c` |
| 確 | `6d99b6fb623bd9f263216e1af1fc9489e47d3ebe1f59fa586b0fef0df8eb2c80` | `d6e86b00b05b851b6714cadb9e85f37dd0223207` |
| 示 | `ab8c29ff453ed89e6f4ef09d3312214c20c2131a28a047b0e997461be0185ca6` | `54d17154598b34e1b6f6bed3d139c7ba7765c92e` |
| 科 | `82db27c13e2ff63211d68aa2c22a58c2146f1fd7ab949a555c6cb898aae411c6` | `b92090d03ee2f220e34492b79488e55dabbfd3eb` |
| 程 | `a1c9360949f468bd41b7f9bd119525facfb3fe238fc3337184f5214092543736` | `36d732b24658dbb656b25b782ec111477b9bf4bb` |
| 種 | `7ffafa8ec7a8bb9e260aaf4700951bf36fd8d14954da10ed7879a6b1691b5710` | `a10f708a4e4df53963c17a8c6a64b058dcdaf29b` |

The capture JSON hashes, compressed archive hashes, frozen snapshot archive hashes, lesson Git blobs, and stroke hashes are separate domains; I have not treated them as interchangeable. No glyph-pixel inspection, frequency assessment, runtime/device/media/release testing, or activation approval was performed. No validator or test suite was run in this review. **The candidate is not yet accepted or published.**
