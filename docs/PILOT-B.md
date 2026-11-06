# Pilot B: structured lessons and bounded media adaptation

## Plan and frozen scope

This is the next C6 pilot, not full N5 coverage, EN/RU parity or C7/general activation.
The owner's request is to merge the three reviewed working branches, plan and implement a
wider Russian pilot, then improve tooling/instructions using observed findings.
No new paid media is authorized. Existing Japanese assets may be reused only with their
licenses, exact hashes and separate Russian-package review/publication boundaries.

The three reviewed branches were merged before selecting this cohort:

| Repository | Accepted main |
| --- | --- |
| Android | `30b0719210e972f03a575cd4d4438204a9b3b7b2` |
| English content | `5f460b85b391404e7da01be0a0cded78243b7538` |
| Russian content baseline | `98046a9babe31aee4035a212c7c880d45a298ffc` |

EN required a signed two-parent merge with the newer `e91eec0c` main; only the generated
manifest conflicted. Regeneration preserved all 8,272 incoming runtime entries/hashes.
368 tool tests, validation, budgets, vocabulary checks and current/released readers passed.
All 8,279 exported file bodies in the immutable public ZIP equal the tested prefixed local ZIP.
This does not claim that GitHub Actions ran or that the local main refs had already moved.
Unrelated authoring worktrees, caches and JSON files were preserved.

The initial pre-authoring objects, Japanese IDs, media hashes, instruction inventory and
planned omissions are frozen in [pilot-b-sources.json](pilot-b-sources.json).
The actual validator exposed ten required exclusion references missing from that plan.
Their finite directed closure is frozen separately in [pilot-b-closure.json](pilot-b-closure.json)
before authoring the additional 18 word articles; it does not overwrite the initial freeze.
Existing Pilot A content is reused unchanged; it is not silently relabelled as translated
from the new EN snapshot. Its own per-object provenance remains authoritative.

### Adopted runtime cohort

| Family | Whole selected teaching unit | Dependencies and bounded adaptation |
| --- | --- | --- |
| Grammar | All four exercises and both facets in `grammar/n5-foundation-connections.json`; complete `n5-foundation-connections-linking` introduction group | Both constructions and the relationship retained; `requires: []`. The advisory `next` edge to unadopted `listing-tari` is omitted, not reclassified as a prerequisite. |
| Grammar article | `articles/japanese-listing-and-examples.md` | A scoped Russian companion for ordinary verb-て and noun-predicate-で connections, based on the source's corresponding section and the complete selected exercises. Other listing constructions are not claimed translated. Explain the supplied forms, roles and time interpretation locally, not through an unavailable EN article. |
| Vocabulary | Every vocabulary span in all four grammar exercises | Preserve prompt hash, offsets, Japanese surface/reading/headword; translate every gloss. These are in-place tips, not a claim that separate word articles were adopted. |
| Counters v1 | All 12 `cards` and all vocabulary in `counters/tsu.json` | Preserve Japanese prompts, answer alternatives, canonical phrase/readings and distractors. Replace `en` with neutral `translation`. The two cross-family `reverse` rows are explicitly out of scope; their referenced 人/匹 lessons are not fabricated or imported just to fill the pool. |
| Counters v2 | Complete `counters/native.json`, including its one expression | Preserve `十`/`10`, `とお`, Japanese unit and stable IDs; translate cue, title and explanation. |
| Counter article | `articles/numbers-and-counters.md` | Scoped Russian companion for this adopted つ series, whole-expression writing/reading and distinction between alternative units and readings. The source's wider time/date/N4 syllabus is not claimed translated. |
| Word pictures | Complete `words/きらきら.md`, `words/にこにこ.md` and corresponding `scenes/*.json` | Retain Japanese examples, dictionary identity, levels/absence of a level, tags and direct quiz exclusions. All comparative explanations remain Russian; unadopted related pages are not unresolved clickable prerequisites. |
| Required word closure | The 18 additional articles enumerated in `pilot-b-closure.json`, making 20 new word articles in total | Preserve every source direct exclusion/distractor reference. These are required negative-edge dependencies, not quota-filling pages or inferred transitive exclusions. Optional pictures/scene catalogs of these dependencies are not adopted. |
| Existing pictures | `images/きらきら.webp`, `images/きらきら--sparkling-interested-eyes.webp`, `images/にこにこ.webp` | Reuse exact three source binaries with attribution. Retain the source's two quiz-eligible scenes and its explicitly non-eligible sparkling-eyes scene. Inspect actual files, not just descriptions. No new generation. |

The corrected scope adds 30 runtime files to Pilot A's 51: one grammar JSON, two counter JSONs,
20 word articles, two companion articles, two scene JSONs and three existing images.
The initial 12-file candidate was rejected by the real validator; its failed output is retained.
The additional word set follows required references only and leaves the image/media cohort unchanged.
File counts describe packaging, not learning depth. The bounded reader/native observations and
remaining earned-history gates below distinguish packaging from actual operation coverage.

### Complete audio adaptations, initially blocked outside runtime

Prepare full Russian drafts, not a selection of convenient correct-answer fields:

| Family | Exact source | Kept Japanese operation | Initial acceptance boundary |
| --- | --- | --- | --- |
| Legacy listening | `listening/n5-a-phone-message.json` | All three turns, three questions, twelve options/rationales, evidence, speakers and vocabulary | Draft in `docs/pilot-b-drafts/listening/`; omit only the optional `word: 電話` link to an unadopted article, retaining/localizing its complete inline tip. Source audio identity retained in provenance. No inherited `audioReview` or fabricated listening/native pass. |
| Japanese task | `listening-tasks/n5-task-borrow-umbrella.json` | Complete quick-response package: instruction, utterance and all three heard replies; numbered Japanese labels, stages, evidence and exposure identity | Draft in `docs/pilot-b-drafts/listening-tasks/`; all Russian translations/help/feedback reviewed. No inherited `approval`, owner-testing exception or EN media binding. |

Both validators hash the semantic package, including translated text. Therefore the unchanged
Japanese recordings do **not** make an EN `contentSha256`/approval valid for the RU package.
Record source media identities separately; do not generate or rebind audio under an invented
approval. These drafts stay outside manifest/runtime namespaces until fresh exact-package
publication authority is established. General listener/physical-phone acceptance remains separate.
No missing family counts green, and no English fallback substitutes for it.

## Testable checkpoints

1. **B0 — source and plan.** Pin the three main commits, source objects/IDs, real dependency
   closure, licenses, media identities, instruction delta and intentional omissions before
   authoring. File the bounded work item and obtain independent read-only plan review.
2. **B1 — Russian adaptation.** Translate the entire selected units and all visible branches.
   Preserve Japanese content/identity; make the two scoped articles honest about their scope.
   Keep both audio drafts outside runtime. Record intentional adaptations separately from
   translation completion. Preserve all Pilot A runtime bytes.
3. **B2 — independent content review and structural gates.** Review every new learner-facing
   field, all options, both articles, all scenes and both complete audio drafts against the
   frozen source. Assess Japanese correctness, scoped coverage and Russian comprehensibility
   separately. Adjudicate findings with evidence, correct and re-review affected material.
   Run the actual RU tool suite, validators, budgets, vocabulary check and generated-manifest
   reproducibility. Use the real candidate ZIP with a single GitHub-style root directory for
   reader checks; a flat `git archive` is not that input format.
4. **B3 — bounded real integration.** Use the exact signed compatible APK and published candidate
   archive in the existing owner-authorized controlled public integration repository if the
   official named-pilot gate excludes this new branch. Record the actual source identity,
   branch and content version; do not weaken the ordinary RU-main gate or silently advance
   the frozen `ru-pilot-a`. Use only the owned disposable lab, retaining its earlier progress.
5. **B4 — reflection and persistence.** Fix observed app/tool/content defects in their owning
   repository, rerun affected checks and put verified reusable mechanisms into the active
   instructions in the same correction batch. Reconcile stale “testing branch only” wording
   with the owner's explicit main-merge authorization without implying C7 activation.
   Publish scoped commits, work-item evidence and outstanding acceptance boundaries.

### B3 operation matrix

| Operation | Required evidence | Explicit non-claim |
| --- | --- | --- |
| Admission | Actual Russian source accepted; Home sees the new structured/image inventory, not merely a parsed fixture | No ordinary official RU-main activation |
| Grammar | Choice and typed answers; supplied Japanese fragment; answer-independent Russian instruction before answering; full explanation after; actual vocabulary tips and companion article/Back | Four exercises are not evidence of mastery or whole grammar coverage |
| Counters | v1 context/suffix, full written phrase and canonical kana reading; v2 `十` and `とお`; alternative unit does not become a reading of the displayed phrase | Omitted reverse rows are not passed |
| Pictures | Actual reused files; both eligible targets; Russian scene/accessibility text without the Japanese answer; non-eligible scene stays out of quiz selection | Decoding alone is not visual or phone approval |
| Encounter/recovery | Capture exact question/check phase and source; background/recreation and language/source return where supported; record progress and any unsupported path honestly | Force-stop/relaunch alone is not proof of a mid-import death window or saved encounter restoration |
| Listening | Draft structural/semantic review only while blocked; later actual playback, transcript, all feedback, captured interruption and recreation after permission | No listening/native/phone pass from source hashes or a draft |

## Status and evidence

**B0 plan reviewed:** one independent read-only review checked all selected source units,
the complete plan/inventory, all three actual images, dependency closure and approval boundaries.
Its sole minor finding was the legacy `電話` optional article link; the disposition above
and in the frozen-source inventory resolves it without importing an unselected word article.
The report did not review authored Russian or perform native tests. Its source-closure conclusion
was superseded by the actual validator failure above: reading metadata had not proven that all
negative-edge references resolved in the candidate. The bounded closure amendment was independently
accepted before those dependencies were authored. As a consequence, the corrected source cohort also
meets the existing four-word thematic-stack rule; this was not the reason for expanding it.
Record the actual stack, gates and option counts; do not relabel levels or weaken gates.
A legitimate two-candidate picture pool has two options, not a fabricated four.

The independent amendment review verified the exact 20-word closure, all 43 source direct
exclusion edges, all 18 additional immutable source objects and all 18 proposed localized app tags.
It accepted the amendment with no blocking findings; authored text and implementation still
require separate review. The sync-mode first reviewer could not accept follow-up messages, so
this narrower amendment used one fresh background reviewer rather than pretending continuity.

**B1 and bounded content review completed:** the independent reviewer read all 29 new learner-facing
text files, the full selected source counterparts and all three actual 512 px pictures. The one minor
finding was misleading “Краткое” before とお in the counter companion; only that adjective was removed,
and focused recheck accepted the correction. All four grammar-vocabulary proposals / 15 spans were
explicitly approved, recorded with the actual reviewer and applied using the existing tool.
Its grammar rewrite was verified semantically identical; the changed raw hash is formatting, not
an unreviewed replacement. The renderer-only app change and separate three real-archive tests also
received bounded acceptance. [pilot-b-review.json](pilot-b-review.json) records per-object hashes,
actual report identities, the resolved finding and nonclaims.

The corrected runtime version is `24362f736bc17328`, not the original review snapshot's
`6f879eef5e83e952`. Actual checks pass: validator 0 errors, vocabulary 4/4 complete, 109 Python
tests, reproducible manifest and the 88-file / 97-entry export budget. All 39 baseline text bodies
remain unchanged after normalization; all 12 strokes and three reused pictures match raw bytes.
The three working-archive domain cases passed before F1; that receipt is retained, not relabelled
as final-public-archive execution.

The app's old/new hint tests pass 2/0/0/0, Android lint and signed release succeed. Detekt still
fails only on unchanged `ComposeUiTest.kt:81`/`:345`; no global green claim. The new APK is
`af1d22014b0d278cc81bba7cb16e099de9900344edb851458a091b31005ec214`, 51,548,294 bytes,
signer `c059f19f7f7eef8f984618632b525f3cf7479afd834984dda169910640b4ad1f`.
It was built from app `30b0719` plus the frozen reviewed localization patch, before publication.

### Final public package and bounded native observations

Both repositories published the same signed runtime commit
`7ce81c74e72fc189185a1bebe71d775379792124`. Their immutable public ZIPs have different root names/raw
hashes but all 88 exported bodies equal the signed local archive. All 81 runtime hashes and all 51
Pilot A file bodies were verified, the latter raw-byte identical to baseline. The three final
controlled-public-archive reader/domain cases execute **3/0/0/0** (tests/failures/errors/skipped).
Desktop ZIP verification is not a claim about the raw HTTP bytes downloaded by Android.

The owned API-29 lab actually accepted `stop-cran/learning-japanese-ru-integration-test`,
branch `ru-pilot-b`, head `7ce81c7…`, content version `24362f736bc17328`. The accepted cache contains
12 kanji, 47 words, two counter files, one grammar set, three pictures and three scenes.
There is no RU audio runtime; cached English recordings do not become fallback RU lessons.

| Actual operation | Observed result and boundary |
| --- | --- |
| Grammar | All four exercises: two noun-choice and two typed verb-fragment answers, 4/4 correct. Only `て` was entered for the supplied verb stem. Russian instruction precedes the answer; completed Japanese and full Russian feedback follow it. The five-entry vocabulary list and actual `学生`/`がくせい` Russian gloss were opened; this does not claim that every one of the 15 tips was opened natively. Companion article/Back preserves the checked answer. |
| Counters | Actual legacy context `りんごを二（　）食べました。` accepts `つ`; feedback shows `二つ (ふたつ)` and Russian meaning. Whole-expression v2 accepts `十`. Kana reading accepts `やっつ`, `とお`, and `ふたつ`; intentionally entered `にこ` is rejected as the reading of displayed `二つ`. The reading session ends 3/4 because of that deliberate negative case. Russian companion/Back works. `10`, `十つ`/`じゅう` and declared legacy whole alternatives have real-archive domain coverage, not claimed native entry here. |
| Pictures | Both `きらきら` and `にこにこ` were seen, visually inspected and graded in both actual directions, 2/2 each. Each question legitimately has two choices. Russian scene/accessibility text contains no Japanese answer. The article-only sparkling-eyes scene remains non-eligible in the real-archive domain check; the native sessions use only the two eligible scenes. |
| Earned history | The 13-word thematic stack is available under the existing four-word rule, independently of JLPT unlocking; source levels/absent levels are unchanged. One ordinary 13-answer session and five ordinary ten-answer extra-practice sessions earned both picture targets. After just two correct answers, `きらきら` had stability 1.41 days, insufficient for the two-day Word gate. No clocks, DB states or thresholds were changed. |
| Question/check and recovery | Normal Home/background/return preserves the reverse-picture question and its checked answer. Language replacement requires explicit consent, uses the English default, and validating the controlled RU source realigns the interface to Russian. All controlled-source learning rows (28 states / 79 logs / 13 sessions, including earlier controlled-pilot rows) remain exactly equal across that roundtrip and a later force-stop/relaunch. This proves committed history, not saved transient encounters or a crash during import. |

The new cohort exposed a second app defect: the counter-reference caption stayed English even though
its RU resource existed. `CounterHome` used application-context resources inside a retained producer.
The minimal correction resolves the current Compose string and keys the producer on that caption.
Its same-source/content EN → RU → EN regression was genuinely red before the fix; independent
two-file review accepted the correction. The four CounterHome and two Word-hint tests pass **6/0/0/0**;
lint and signed release succeed. Detekt still has only the two unchanged findings above.
The supplemental review report SHA-256 is
`ec096f0d9830ee1803edd946461e1e5f6b6b673a048e42f43adfad6d25b3c176`;
its accepted raw inputs are `CounterHome.kt`
`a166047729a64bc76695eaf53316eca1c994b7770e5b5aafa5727b8e66014490` and
`CounterHomeTest.kt` `69de8eef4aa176ba21463c3db4cff05178b8b1345348bba41ef754fba4edb80f`.
The original review receipt remains historical: its pre-native boundaries are not overwritten.

The corrected signed APK is
`190561ef590dba2c65c6360a2c90fc09febf75f5c28fc8957a3d51d27610167d`,
with the same `c059f19f…` signer; actual installed `base.apk` bytes match it. It was built from app
`30b0719` plus the reviewed hint/counter patches, before their source commit. Earlier grammar/counter
observations retain their `af1d2201…` APK scope; the new reference caption and subsequent words/pictures/
language/relaunch observations use `190561ef…`. Neither receipt is silently retargeted.

During the English return, live EN/main had legitimately advanced to
`b189ed637bf27f388b0ac8f3e8b31aee634504cc`, version `1a13e8e6d637bc5b`
(1,061 kanji / 5,019 words). It was imported normally. Pilot B's translation provenance remains frozen
at `5f460b8…`; this roundtrip is not a substantive review of the newer EN corpus.

### Remaining gates and restoration

The following is the original bounded B3/restoration receipt. Its then-unearned Word Type
observation is historical; the subsequent five-target observation below updates that boundary
without rewriting the original APK/history receipt or passing the other remaining gates.

- **Counter suffix / legacy whole-phrase typing:** native-deferred until the existing two-distinct-days
  Choose prerequisite is genuinely earned. One actual Choose day is recorded; do not advance the clock
  or inject state to complete the matrix.
- **New-cohort Word Type:** the separate Russian-to-Japanese prerequisite has not been earned.
  The 18-label real-composable regression passes, but no new-cohort native Type pass is claimed.
- **Listening:** both complete reviewed Russian adaptations remain outside runtime pending fresh
  exact-package publication authority and subsequent playback/interruption checks.
- **Release:** physical phone, Japanese-capable IME, C7, ordinary RU defaults and whole-corpus parity
  are not accepted by this bounded lab.

The daily limit was temporarily raised by ordinary Settings presets/input (20, then 30); it was restored
to effective 10 and the word stack to N5 through the ordinary selector. Original official
`stop-cran/learning-japanese-ru` / `ru-pilot-a` was normally revalidated at pinned `544dd15…`,
version `afe5c99e66524d95`, with explicit Russian. All original 10 states / 13 logs / six sessions remain
unchanged; totals are now 36 / 90 / 18 because real controlled-pilot practice is retained.
The previously absent daily-limit/word-stack preferences are now explicit defaults; the legitimate
article-navigation counter advanced from 1 to 2. Raw preferences are not claimed identical.
The input-only helper was removed, all 421 exact task-created device XML paths were individually checked
absent, the original Latin IME and non-root ADB UID 2000 were restored, and only the owned emulator/process/
5582–5583 listeners were stopped. Foreign emulator 5556 was not addressed and remained present.
Private DB/preferences/command evidence stays local; it is not uploaded with these aggregate observations.

Current status: **B0/B1/B2 complete; the observed B3 subset passes with the explicit deferred gates above;
B4 instructions, reflection, signed branch publication and fast-forward main integration completed.**
These new source merges do not activate ordinary Russian defaults or count the deferred native paths as passed.

### Subsequent recorded C6 observation: five genuinely unlocked Word Type paths

The [later C6 record](https://github.com/stop-cran/learning-japanese-ru/issues/6#issuecomment-6633295530)
documents an already performed owned API29 run, not a new test in translation batch036.
Exact signed APK SHA-256 `0293a7bab3e5e0ad752e15c822c610b11d9fc2c4cc5a45de27ca31bfa3125bde`
used app `5c000bd` and the unchanged authorized integration-test `ru-pilot-b`
`7ce81c74e72fc189185a1bebe71d775379792124`, version `24362f736bc17328`.
Forty ordinary reverse-practice answers genuinely earned the unchanged prerequisite.
Native Word Type then passed **5/5**: ぺらぺら / きらきら / つやつや / つるつる / ぬるぬる,
with automatic focus, visible IME, correct feedback/Next and committed own-mode history.
This is not all 13 words, Japanese-keyboard acceptance or physical-phone acceptance;
the record discloses the Latin IME and input-only helper.

Second distinct real CounterChoose day, exact new-RU audio-package authority and actual
playback/interruption for both excluded drafts, phone/JapaneseIME and C7 remain unpassed.
The earlier grammar/counter/picture observations above remain actual bounded passes.
Later native findings may require correction and independent re-review of affected source batches.
That possibility does not supersede the owner's authorization to continue independent source authoring,
and none of these records activates ordinary Russian defaults.
The controlled runtime branch stays at `7ce81c7…`; the Russian follow-up commit changes documentation only.
The two audio families are **BLOCKED for runtime publication** pending fresh package authority;
their complete Russian text and source reuse plan remain part of the implementation/review scope.
C7, ordinary RU defaults, physical-phone acceptance and whole-corpus synchronization remain separate.
