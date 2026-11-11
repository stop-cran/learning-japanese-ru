# Independent review: 空 card amendment

**Review date:** 2026-11-11  
**Scope:** Read-only review of the proposed amendment in the isolated candidate clone (branch `ru-sora-nav-amendment`, based on `f940768c96f7a556d2e6cf71303d53190bf48828`); the clone's local path is omitted from this persisted copy. No candidate source files were edited by the review.

**Persisted copy.** This file is an LF transcription of the report body written by the independent reviewer session `a5da29cd-cb6d-4a24-be85-c7e20079cf88`, changed only for provenance and portability. The reviewer's saved report file was 9253 bytes with CRLF line endings (SHA-256 `307dfe7b4c8ed4cf071afe3fa9d11859157b6836627b3458ef3f6a274559d6b5`); its LF-normalized text was 9177 bytes (SHA-256 `70da0a1d1d4c678e3e0e270b544e484647101533d7c3842113361e9dae558368`). These hashes identify the saved report file, not the bytes of the message actually returned. Edits in this copy: this note; the local path of the reviewed clone replaced by a portable description; and example text and renderings taken from restricted WARODAI or Kotobank entries replaced by article/entry references or `[omitted]` markers, keeping only expression headwords that JMdict (CC BY-SA 4.0) independently supports. Findings, the Q1–Q5 verdicts and the C2 boundaries are unchanged. Line numbers, hashes and status statements in the body describe the candidate as reviewed: the evidence record was revised for provenance afterwards (its `revision` block records the superseded hash), and the "six intended candidate paths" in the workspace note predate adding this report.

## Verdict

**APPROVE the card/link/phrase amendment for integration into the excluded draft only.** The navigation link is correct, the added secondary-sense paragraph is supported by the checked dictionary records and is appropriately bounded, and the records maintain the draft's excluded/pending status. This approval is **not** runtime acceptance: both protected quiz pairs remain **C2 UNVERIFIED** in both quiz directions.

## Findings

- **Blocking for runtime adoption — `[空, 遠く]` remains C2 UNVERIFIED.** There is verified Japanese remote-place/away-from-home usage, but no checked source directly adjudicates the actual Russian title labels as a translation of bare 空. Neither a safe distractor nor an exclusion is established. See the pair analysis below.
- **Blocking for runtime adoption — `[空, 遠い]` remains C2 UNVERIFIED.** The noun sense does not establish a Russian adjectival caption equivalence or its rejection. No exclusion or clean status should be inferred.
- **No blocking issue for the excluded-draft amendment.** `words/空.md` remains pending; no quiz exclusions, runtime card, manifest, activation, or release authority was added.
- **Non-blocking workspace note:** the proposal clone's latest `git status --short` also showed untracked `tools/__pycache__/`, outside the six intended candidate paths. I left it untouched; exclude it from any staging.

## Q1 — Navigation

**Verified: yes, navigation-only and correct for the runtime location.** At `docs/translation-drafts/033-nature-outdoor-activity/words/空.md:24`, `[空](../kanji/空.md)` matches the frozen English sentence and existing `[青](../kanji/青.md)` convention. `kanji/空.md` exists. The link is runtime-relative: it resolves as intended when the candidate is installed at `words/空.md`, not as standalone draft navigation.

`tools/validate.py:560-570` checks that each character in a word's `kanji` field that has a card is linked from the article. I ran the check in memory with the runtime path: the old unlinked sentence reports `kanji '空' has a card but the article does not link to it`; the amended sentence reports no errors. Thus the link fixes that validator failure.

## Q2 — New paragraph

**Verified and approved for the excluded draft.** The supplied JMdict release (SHA-256 `3a77bf9af599c1264deef9780b8b1a9f53ea16e1aab30ebaf3c64a6f816ccc4f`) contains:

- Entry **1245290**, reading `そら`, sense 3, POS noun, glosses “far-off place; distant place.”
- Entry **1839300**, `旅の空（たびのそら）`, POS expression, glosses “away from home; while travelling.”

The card at lines 38–41 accurately distinguishes a noun sense from the adverbial caption `далеко`, keeps `небо` as the primary title (line 4), and describes the translation as belonging to an attested expression rather than asserting bare `空 = далеко/вдали/далёкий`. It makes no exhaustive construction or blanket literary claim. “Вдали от дома; в пути” is natural Russian for the whole expression; the paragraph is clear that `そら` is a noun there. This directly fulfills the request for individual verified cases rather than a blanket gloss.

This is user-directed material beyond the frozen English card: the amendment record says so and records the user direction. Attribution remains to J. W. Breen / EDRDG and CC BY-SA 4.0 at lines 55–58. The candidate adds no wording copied from WARODAI or proprietary Kotobank entries.

## Q3 — Possible ambiguity with 遠く/遠い

**No wording change is required for this excluded draft.** The body phrase `вдали от дома` (line 39) echoes one word in 遠く's title, but it is a translation of the entire `旅の空` expression, not a claimed translation of bare 空; line 40 marks the noun/adverb distinction. The actual quiz captions remain `空: небо`, `遠く: далеко; вдали`, and `遠い: далёкий; далеко`. The echo is worth noting, but does not establish direct caption equivalence or justify an exclusion. The current text does not claim that bare 空 translates as any of those captions.

## Q4 — Records, hashes, boundaries

**Verified: accurate, including the requested K3 correction.**

- Recomputed card working-byte and LF-normalized SHA-256: `97613d8959309dda4233a4f63ad2de635db4f09e6c229103860d1140640ae5d9` (both). `git hash-object` returns `14a3396f82a892584b45d4fdf163e8e67888502d`, matching the amendment record.
- The amendment record says there are zero guard and quiz/exclusion changes, no runtime word page, no manifest change, pending progress, and no activation/release authority. Its status appropriately requires this independent review.
- `docs/translation-tracking.json` records the same three hashes, `reviewStatus: unverified`, runtime acceptance blocked by linguistic uncertainty, `runtimeAuthority: null`, and the target still pending.
- `docs/FULL-TRANSLATION-PLAN.md:6837-6848` and `docs/translation-methodology.md:29-31` preserve those boundaries and state that a dictionary sense or its absence does not itself settle the pair.
- The latest evidence record's **K3** (`...sky-sense-evidence-qualification-001.json:132-135`) now says only that the inspected examples of `秋の空` (JMdict 2709640) and `男心と秋の空` (JMdict 2520160) are rendered as sky/weather [example text and renderings omitted; the inspected WARODAI articles are cited by ID in the evidence record]; it expressly rejects a rule for all non-place nouns or from `N+の空` alone. This is accurate and avoids the prior overgeneralization.

The three relevant JSON files parse successfully. I did not independently re-open every prior Russian-headword or WARODAI query listed in the evidence record; none is used here to infer safety or to decide either pair.

## Q5 — Pair-specific verdicts

The actual word cards show `空` title `небо` (`docs/translation-drafts/033-nature-outdoor-activity/words/空.md:4`), `遠く` title `далеко; вдали` (`words/遠く.md:4`), and `遠い` title `далёкий; далеко` (`words/遠い.md:6`). The frozen content-format documentation says the word title is used in the quiz and that exclusions apply symmetrically in both Japanese-to-Russian and Russian-to-Japanese directions. The RU format reference also says exclusions are direct symmetric pairs, not transitive.

| Pair | Japanese → Russian | Russian → Japanese | Verdict |
|---|---|---|---|
| 空–遠く | **C2 UNVERIFIED** | **C2 UNVERIFIED** | JMdict verifies a noun sense “far-off place” and a phrase-level “away from home” use. Neither is direct evidence that bare `そら` takes the Russian adverbial title `далеко; вдали`; the phrase `вдали от дома` alone cannot establish that equivalence. Conversely, the evidence does not establish that the captions cannot overlap in relevant use. |
| 空–遠い | **C2 UNVERIFIED** | **C2 UNVERIFIED** | The noun gloss “far-off place; distant place” is not by itself a Russian adjectival use `далёкий`, but it also does not reject one. No source establishes actual caption overlap or its absence. |

For both pairs, **CLEAN** would improperly infer safety from a lack of a checked direct Russian equivalent; **DIRECT EXCLUSION WARRANTED** would overstate the evidence. Keep both pairs unresolved, with no new guard.

## Sources checked

- EDRDG **JMdict** release: <http://ftp.edrdg.org/pub/Nihongo/JMdict_e.gz>; entries **1245290** sense 3 and **1839300** directly extracted from the supplied gzip release.
- Kotobank, デジタル大辞泉, `そら【空】` sense 3 and its examples: <https://kotobank.jp/word/%E7%A9%BA-54809>.
- Kotobank, `旅の空` entry (separate phrase senses): <https://kotobank.jp/word/%E6%97%85%E3%81%AE%E7%A9%BA-562279>.
- WARODAI API, article `たび【旅】` **001-51-23**, queried phrase `旅の空`: <https://warodai.ru/api/v1/corpus/lookup/?keyword=%E6%97%85%E3%81%AE%E7%A9%BA&corpus=warodai>. Its example built on the `旅の空` expression (JMdict 1839300) with a locative particle is rendered as a locative phrase that keeps a word for “sky” with a “foreign” modifier [example text and rendering omitted]; it does not establish the Russian caption for bare 空.
- Frozen source format contract: <https://raw.githubusercontent.com/stop-cran/learning-japanese/6af98cb717755690a9ca793e5454a96ebd7a8f9f/docs/content-format.md>.
- Frozen confusable-word policy: <https://raw.githubusercontent.com/stop-cran/learning-japanese/6af98cb717755690a9ca793e5454a96ebd7a8f9f/docs/confusable-words.md>.

## Commands/checks run

- `git -C <proposal> -c core.quotepath=false --no-pager diff` and `git status --short` (read-only).
- `python -X utf8 -B` to decompress/parse the supplied JMdict release and print the cited entries.
- `Get-FileHash` and `git hash-object` on the candidate card; Python JSON parsing on the amendment, evidence, and tracking records.
- In-memory calls to `tools.validate.check_word_kanji_links` for the old and amended runtime-path sentences; no candidate file was placed or changed.
- Direct source fetches for the Kotobank entries, WARODAI result, and frozen format contract.
