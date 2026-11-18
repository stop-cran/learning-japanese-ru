Snapshot: learning-japanese-ru commit 8647411 (parent d91f970), HEAD = 8647411; working tree clean. EN source: learning-japanese-en-frozen 6af98cb.
Scope: The full diff from d91f970 to 8647411 (6 files: きりきり, ぐびぐび, ごくごく, ごぼごぼ, じゅうじゅう, manifest.json). I reread the changed passages in context and ran word_title_screen.py and link_parity.py on the 5 changed cards. I checked the requested overlaps by meaning against JMdict (via the Jisho API). I verified manifest.json by recomputing the SHA-256 of every listed file. Reviewer model: Claude (Anthropic). Read-only.
Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety NEEDS FIX (one low-severity pre-existing pair, Q3; not a regression)

Status of earlier items:
- Q1, resolved: ごぼごぼ.md:8 is now `[ぐつぐつ, ぶくぶく, ぷくぷく, ぽちゃん, 沸く]`.
- Q2, resolved: ちびちび was removed. ぐびぐび.md:8 is `[ぐいぐい, 飲む]` and ごくごく.md:8 is `[がぶがぶ, ぐびぐび, ぐいぐい, 飲む]`. All EN exclusions are still present. The がぶがぶ, ぐびぐび and ごくごく cards are now consistent with each other.
- Optional きりきり, resolved: lines 4, 11 and 17 now read «острая, сжимающая боль». This matches body line 15 and EN "gripping". JMdict lists "hurting sharply", and «сжимающая» is a natural Russian description of a gripping stomach pain.
- Optional じゅうじゅう, resolved: lines 4 and 10 now read «шкворчать (при жарке)». This covers EN "on a hot surface" (pan or griddle) and fits example 2 (鉄板).
- Optional ぐびぐび, optional (declined, accepted): «громкими глотками» is a fair rendering of "audible gulps" and matches both examples.

Regression check:
- No text changed outside the reported lines. link_parity reports no lost or extra links in the 5 cards.
- きりきり vs ぎゅうぎゅう «битком набитый; туго сжимать»: the shared stem «сжима» from the fix is not a shared meaning. One describes pain and the other physical pressing, so the fix creates no new risk. JMdict does, however, show an independent overlap that existed before the fix (Q3).
- ごぼごぼ vs 沸かす «кипятить; нагревать жидкость»: no guard is needed. 沸かす is transitive ("to boil something"), and ごぼごぼ is an intransitive sound with no "boil (something)" sense in JMdict ("gurgling; burbling; bubbling; glugging"). Neither title is a defensible answer for the other. The «клокотать = кипеть» risk is covered by the new 沸く pair.
- じゅうじゅう vs 焼く «выпекать; жарить»: no guard is needed. In «(при жарке)» the brackets only say when the sound occurs. 焼く names the cooking action and じゅうじゅう names the sound (JMdict: "sizzling (of cooking meat, fish, etc.)"). Neither title answers the other. EN has no such pair, and the RU screen tool does not flag it.
- Manifest: all 3634 listed files match. 3516 match by raw SHA-256; 118 CRLF `strokes/*.json` files match after CRLF-to-LF normalization, which is the existing convention for those files (`-text` attribute) and was not touched by this fix. All 5 changed word hashes were updated, contentVersion changed (a48ba8e789fa5e9b → 391fde400d898afe), and no word file is missing from the manifest. I did not run the official generator (see Limits).

Findings:
Q3; low; quiz safety; words/きりきり.md:8. This overlap was there before the fix: my first review missed it, and the recheck surfaced it. JMdict records a tight-binding or tightening sense for both words. きりきり sense 2 is "binding tightly; pulling tight (e.g. a bow)", and ぎゅうぎゅう sense 3 is "hard (pressing, tying, twisting, etc.); tightly; with force". The きりきり body (line 15) also teaches «тугое затягивание». So ぎゅうぎゅう's title «туго сжимать» can be defended as a correct answer for a きりきり prompt. A secondary overlap: ぎゅうぎゅう sense 1 "creaking; squeaking" sits close to きりきり «скрежет», which is "grinding". There is no direct pair on either side. Remedy: `quiz_exclusions: [痛み, 痛い, 苦痛, 頭痛, しくしく, ずきずき, ひりひり, ちくちく, ぎゅうぎゅう]`. Evidence: https://jisho.org/api/v1/search/words?keyword=きりきり and https://jisho.org/api/v1/search/words?keyword=ぎゅうぎゅう (JMdict senses). Confidence: medium. This is a conservative guard based on secondary dictionary senses; I have no data on how often they are used.

Optional: none new.
Limits: I did not run the RU validator, manifest generator or budget commands. Manifest consistency is my own hash recomputation, not the C1 generator's output. JMdict senses come from the Jisho API, not the raw JMdict XML. Q3 is about meanings not shown in the titles; how often they come up in real quizzes is unverified.

## Recheck 2

Snapshot: learning-japanese-ru commit bbdbe01 (parent 8647411), HEAD = bbdbe01; working tree clean. EN source: learning-japanese-en-frozen 6af98cb.
Scope: The full diff from 8647411 to bbdbe01 (2 files: words/きりきり.md and manifest.json, 3 lines changed). I recomputed the hash of the changed card and checked the target card words/ぎゅうぎゅう.md. Reviewer model: Claude (Anthropic). Read-only.
Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety CLEAN

Final statuses:
- Q1, resolved (no change since Recheck 1).
- Q2, resolved (no change since Recheck 1).
- Q3, resolved: words/きりきり.md:8 now ends with ぎゅうぎゅう, matching the remedy exactly. The 8 earlier exclusions are kept in their original order. words/ぎゅうぎゅう.md exists, so the exclusion points to a real card.
- Optional きりきり, resolved (adopted in 8647411).
- Optional じゅうじゅう, resolved (adopted in 8647411).
- Optional ぐびぐび, optional (declined, accepted).

Regression check:
- The diff changes only the exclusions line in the front matter. The title, body, examples and links are unchanged, and the YAML list is still well formed.
- Adding an exclusion can only remove distractors, never add an ambiguous one. きりきり still has many unexcluded cards that can serve as distractors.
- Manifest: only contentVersion (391fde400d898afe → ec0b40fb1c54288b) and the きりきり hash changed. The recomputed SHA-256 of words/きりきり.md (cb9ade9c…3726) matches the manifest entry. All other entries are unchanged from 8647411, which I verified in full in Recheck 1.

Findings: none.
Optional: none.
Limits: I did not run the RU validator or manifest generator. In this recheck I recomputed only the hash of the changed file; the other entries carry over from the full Recheck 1 recomputation.
