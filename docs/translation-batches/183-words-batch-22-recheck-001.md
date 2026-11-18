# Batch 183 recheck: 183-words-batch-22

## Snapshot

- **Repository:** C:\Users\romanko\repos\learning-japanese-ru, branch `full-ru-183-words-22`.
- **Commits:** recheck of 51aa24d, a single commit on top of the reviewed candidate b538ac4. `git log --show-signature` reports a good signature: G, EDDSA key D4C9A275…D311BD26A7.
- **Diff (`git diff b538ac4 51aa24d`):** 9 files, 19 lines added and 19 removed. Files:
  - ざぶざぶ, すやすや, ずけずけ, ずるずる, にやにや, ばしゃばしゃ, ぱんぱん and 睡眠 under `words/`.
  - `manifest.json`.
- **Working tree:** clean before and after the recheck. Running the tools created an untracked `tools/__pycache__/`, which I deleted. The final `git status` is empty.

## Scope

- Every hunk of the fix diff.
- The full current text of `words/ざぶざぶ.md`.
- A title-collision screen of the new ざぶざぶ, ずけずけ and ぱんぱん titles against all RU word titles and exclusions, using `word_title_screen.py`.
- A corpus search for «брест/плеск» in word cards.
- `tools/build_manifest.py` and `tools/validate.py`.

I did not re-read the unchanged parts of the batch; they were covered by the original review.

## Verdicts

| Facet | Verdict |
| --- | --- |
| Correctness | CLEAN |
| Scoped coverage | CLEAN |
| Comprehensibility | CLEAN |
| Quiz safety | CLEAN |

## Reconciliation of the original findings

| ID | Status | Evidence |
| --- | --- | --- |
| F1 ずけずけ–まっすぐ | Resolved | `words/ずけずけ.md:8` exclusions are now `[きっぱり, 言う, 話す, まっすぐ]`. |
| F2 ぱんぱん–あふれる | Resolved | `words/ぱんぱん.md:8` now ends with `あふれる`. |
| F3 ざぶざぶ title | Resolved | `words/ざぶざぶ.md:4` and `:11` now read «шумно плескать; с громким плеском». The second segment is adverbial and fits JMdict 2097030 "splashing; sloshing" and the EN "sloshing and splashing". Wading is kept only as the usage example at line 18 and the じゃぶじゃぶ note at line 22, both of which match EN. |
| ずるずる:19 | Resolved | «Обсуждение всё тянулось, а к выводу так и не пришли.» is grammatical and faithful to 結論を出さずに…続いた. |
| すやすや:24 | Resolved | «すやすや и ぐっすり пересекаются…» is now explicit. This reading is sound: ぐっすり (deep sleep) and うとうと (dozing) contrast rather than overlap, while すやすや (sleeping peacefully) does overlap ぐっすり. |
| 睡眠:16 | Resolved | 睡眠を取る is now glossed «спать, поспать». Keeping «как следует выспался» for 十分な睡眠を取りました is correct, because 十分な carries the "enough" meaning. |
| ばしゃばしゃ:26 | Resolved | The text now reads «относится только к варианту с глухим согласным (ぱしゃぱしゃ)». This is accurate: ぱ is the unvoiced counterpart of ば. The note that the camera-shutter sense belongs only to ぱしゃぱしゃ is unchanged and correct. |
| にやにや:18 | Resolved | «Он, видимо, знал ответ и многозначительно ухмыльнулся.» is natural and faithful to らしく…にやにやと笑った. |

## Regression checks

- **New ざぶざぶ title:** the screen finds no segment-level collision. The only stem-level hits are:
  - «громк» against げらげら «громко хохотать», ばきばき «с громким треском» and わんわん «громко реветь»;
  - «шумно» against ずるずる «шумно втягивать (лапшу)».

  None of these are water or splashing meanings, so a learner would not take any of them as a correct answer for ざぶざぶ, and none needs a guard. The closest real neighbour, ばしゃばしゃ, still guards ざぶざぶ through its own exclusions `[ざぶざぶ, ぽちゃん, ぺたぺた]`. ぽちゃん is still guarded directly.
- **Removing とぼとぼ:** this is safe. とぼとぼ is «понуро брести», and its exclusions are `[のろのろ, 歩く, しょんぼり]`. It shares no meaning segment or stem with the new ざぶざぶ title. «брести» now appears only in とぼとぼ's own title and heading.
- **Edited ずけずけ, ぱんぱん and 睡眠 cards:**
  - The ずけずけ and ぱんぱん exclusions only got longer.
  - The ぱんぱん stem hits on «отказ» (捨てる, 遠慮) are the polysemous «до отказа» against «отказываться/отказ». They predate this fix, carry unrelated meanings, and need no guard.
  - The 睡眠 gloss change does not touch its title.
- **Front matter:** in all 8 cards the YAML and other front-matter fields are unchanged. Japanese text and kana readings in the edited lines are unchanged.

## Generated files and validation

- **Manifest:** `manifest.json` changed only in `contentVersion` (c2f91886412024cb → 3e9b665c67b93909) and in the hashes of the 8 edited cards. Running `python tools/build_manifest.py` rebuilt it with version 3e9b665c67b93909 and left `git status` clean, so the committed manifest matches the builder.
- **Validation:** `python tools/validate.py` reports 0 errors.

## Findings

None.

## Optional

None new.

## Limits

- The recheck is limited to the fix diff, the collision screen and the tool runs above.
- The title screen is lexical (segments and stems). Judging the stem-only hits as harmless is my reviewer judgment.
- No native-speaker review.
