# Full Russian translation: execution after the two pilots

## Frozen scope and present state

The owner's 2026-11-04 request is to review and execute the remaining roadmap, not
another arbitrarily small pilot. The target is **every runtime object in the current
English edition**, not a claim that the English edition itself completes the JLPT syllabus.
Freeze EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f` before the next work; later English
changes are drift, not moving inputs to an in-flight translation.
RU baseline is `4d84c90f7cffa70b5ee1e296595d5cc7ce306f6f`;
app baseline is `5c000bd5596d2189ef878da572687bd01ab3bb5f`.

| Family | Frozen EN objects | RU objects at pilot baseline |
| --- | ---: | ---: |
| Kanji | 1,062 | 12 |
| Words | 5,020 | 47 |
| Articles | 57 | 2, both deliberately scoped |
| Counter files | 138 | 2; legacy reverse rows deliberately omitted |
| Grammar sets | 88 | 1 |
| Curriculum catalogs | 1 | 0 |
| Word scene catalogs | 201 | 2 |
| Legacy listening passages | 36 | 0 runtime; one reviewed text draft |
| Japanese listening tasks | 40 | 0 runtime; one reviewed text draft |
| Stroke files | 1,062 | 12 |
| Word images | 398 | 3 |
| Legacy audio | 36 | 0 |
| Task audio | 128 | 0 |
| Task images | 11 | 0 |
| **Total** | **8,278** | **81** |

At that pilot baseline, 8,197 target paths were absent; presence does not establish full translation:
the two articles and legacy counter unit retain explicit partial coverage. Source kanji
levels are N5 80 / N4 166 / N3 367 / N2 367 / N1 82; word levels are
N5 672 / N4 636 / N3 1,625 / N2 1,739 / N1 2, with 346 intentionally unlabelled.
Do not infer levels for those words or invent missing upstream N1 coverage.

The complete 81-object pilot stage is independently reviewed for its adopted scope;
its original sources remain A `3196c3a...` and B `5f460b8...`, not this new target.
Preserve the old provenance/review files as historical records. A new source inventory,
tracking ledger and drift report must not relabel old work as newly translated.

## Remaining work and dependency order

1. **R0 — reconcile scope and guidance.** Inventory every manifest map and every active
   instruction/agent, including changed `applyTo` and normative references. Compare the
   fresh frozen source against both pilot sources. Independent plan review precedes new
   implementation. This inventory is not linguistic approval or a synchronization tag.
2. **R1 — finish the manual provenance loop (RU #2).** Add deterministic read-only
   fixed-revision inventory/drift/checkpoint checks, with focused tests. Track added,
   changed, removed/renamed, untranslated, RU-modified and partial objects separately.
   Preserve RU-specific adaptations and immutable old receipts. Every review record binds
   exact source and Russian hashes plus evidence; matching bytes do not create approval.
   A checkpoint rejects unresolved adopted objects and guidance. Prove a reproducible
   real two-snapshot report before considering optional scheduled automation.
3. **R2 — finish or explicitly block C6 operations (RU #6).** New-cohort Word Type needs
   its real reverse prerequisite; legacy counter suffix/full typing needs a second real
   Choose day. Do not change clocks, gates or saved state. Both reviewed Russian audio
   adaptations need fresh exact-package authority before runtime publication and genuine
   playback/interruption acceptance. Prepare exact binding evidence without inventing
   approval or regenerating paid media.
4. **R3 — C7 owner-device/release acceptance.** APK `0293a7ba...`, built from app `5c000bd`,
   was copied to the physical phone and fully read back over MTP on 2026-11-04.
   This is delivery, not installation, Japanese-IME, playback or phone approval.
   Preserve the applicable API29/API35/enlarged-text/source/history acceptance matrix.
   Ordinary RU defaults remain disabled until the required gates pass.
5. **R4 — translate the complete inventory (RU #3).** The owner's subsequent
   2026-11-04 authorization starts authoring now, without waiting for C6/C7 device
   acceptance; those gates still govern release/activation and restricted media packages.
   Execute coherent dependency-closed batches, starting with remaining N5 kanji/words,
   then N4/N3/N2/N1 and unlabelled words; complete all articles, counters, grammar and
   curriculum alongside the units they support. Scenes/media/listening are separate
   exact-package lanes, never omitted from the backlog. A batch closes required examples,
   direct negative references, prerequisites and licensed media before authoring; optional
   navigation does not recursively force the whole corpus into one review.
6. **R5 — review, integrate and advance only warranted checkpoints.** Independently review
   all learner-facing branches for Japanese correctness, actual adopted coverage and
   Russian comprehensibility; adjudicate, correct and re-review affected material.
   Run the actual validators, vocabulary reviews, budgets, manifest and real-reader/native
   gates. Recheck all combined-tree Russian option ambiguity, canonical app hint vocabulary
   and source-bound history. Exact reused Japanese bytes retain licenses, not RU approval.
7. **R6 — maintain alignment.** A tested manual cycle may later support a least-privilege
   report-only Action. No report self-translates, self-approves, merges, advances immutable
   tags or affects offline study. New upstream content remains pending until adopted.

The later authorization removes C6/C7 as a prerequisite to translation authoring.
It does not authorize paid media, fabricated phone acceptance, transfer of audio-package
approval or ordinary RU activation. Reviewed text batches may be integrated while the
separate release gates remain open.
The official `ru-pilot-a` and controlled `ru-pilot-b` runtime pins remain unchanged.

## Completion evidence

Full translated-corpus coverage means every frozen target object has a complete reviewed Russian unit
or an explicit justified non-translatable asset disposition, all necessary dependencies
are closed, and all changed guidance/source semantics are reconciled. Runtime publication
of restricted packages and release/activation additionally require their applicable
authority/device gates. Report translated text, runtime parity and release readiness
separately. Partial articles, blocked drafts, absent files, copied English
prose, hashes and a generated manifest cannot satisfy that definition.

Current work items remain the authority for outstanding acceptance: RU #2 provenance,
RU #3 staged corpus, RU #5 integration, RU #6 structured/media pilot, and app #28.
Keep the historical C0–C7 evidence in IMPLEMENTATION-PLAN; update its current summary,
not the old reports. Record each verified tooling/method finding in active instructions.

## Manual provenance commands

From the RU root, with an isolated clone containing the two immutable source commits:

```powershell
python tools\translation_progress.py inventory --upstream <EN-clone> --revision 5f460b85b391404e7da01be0a0cded78243b7538 --output <artifacts>\before.json
python tools\translation_progress.py inventory --upstream <EN-clone> --revision 6af98cb717755690a9ca793e5454a96ebd7a8f9f --output <artifacts>\after.json
python tools\translation_progress.py report --before <artifacts>\before.json --after <artifacts>\after.json --ledger docs\translation-tracking.json --output <artifacts>\progress-next.json
python tools\translation_progress.py checkpoint --before <artifacts>\before.json --after <artifacts>\after.json --ledger docs\translation-tracking.json --scope <reviewed-paths.json> --output <new-checkpoint.json>
```

Outputs must be new paths: old receipts/checkpoints are never overwritten. After reviewing a
fresh report, explicitly replace the mutable current `docs/translation-progress.json` and
commit that update. Inventory hashes actual Git blobs against every manifest entry, including
raw binary/stroke identity; an uncommitted EN worktree cannot silently retarget it.
Checkpoint recomputes the current RU tree and manifest instead of trusting an old report.
It needs a nonempty explicit adopted scope, complete current review, reconciled guidance,
the exact batch target and an explicit human authority record. It records exact source/RU
hashes; it is not release approval. Renames are candidates, never automatic identity/review moves.
Changed English-only prose still expires review even when the invariant projection is unchanged.

`translation-tracking.json` retains the 51 Pilot A and30 Pilot B runtime review records and
two separately blocked audio text reviews without rewriting the historical ledgers.
Its `checkpointAuthority` remains null. No tag or checkpoint is advanced by this inventory.

## Verified execution checkpoint: 2026-11-04

R0/R1 are implemented and independently accepted, not merely planned.
[Review and regression record](full-translation-review.json) separates the initial
NEEDS FIX finding from its accepted correction: raw literal and escaped-equivalent
duplicate JSON keys now fail before decoding can collapse them. The real suite passes
124 tests with no failures, errors or skips; the actual RU validator reports zero errors.
Both immutable full inventories still regenerate exactly. The final manual report is
byte-reproducible, SHA256
`e9e549154fb17af30bab3ca7f66fa714fa8d0ac6129fcb4744428f26fdc88f28`.
It detects six added/four modified source paths, none in the adopted runtime stage.
All three changed guidance dispositions since C2 are independently accepted.
Current statuses remain 78 reviewed-current / three partial / two reviewed runtime-blocked
drafts / 8,195 pending. The actual checkpoint CLI still exits 1 and creates no checkpoint.
Runtime bytes, old provenance and both reviewed audio drafts remain unchanged.

The owned API29 lab also completed a previously missing C6 path on the exact signed
`0293a7bab3e5e0ad752e15c822c610b11d9fc2c4cc5a45de27ca31bfa3125bde` APK.
Its runtime was the authorized `stop-cran/learning-japanese-ru-integration-test`
`ru-pilot-b` at `7ce81c74e72fc189185a1bebe71d775379792124`,
content version `24362f736bc17328`, not the complete new EN target or ordinary RU main.
Four real ten-question Russian-to-Japanese extra-practice sessions earned reverse
memory normally; no clock, database, gate or daily limit was changed. Five words then
actually opened Word Type. Their reverse records are Review/reps 4/stability
2.7899488574439086 days; three correct answers on other words still yield
1.9818197930436123 days, below the unchanged two-day gate.
The actual five-question Word Type session passed 5/5, including Russian canonical
metadata labels, automatic field focus and visible IME before each helper input,
correct feedback and committed Next records.
The five actually typed words were ぺらぺら, きらきら, つやつや, つるつる and ぬるぬる;
this is not all 13 onomatopoeia words.
Every original 36 state / 90 log / 18 session row remains unchanged; legitimate new
practice yields 53 / 135 / 23. This is native UI/history evidence, not proof of
learning effectiveness or Japanese-keyboard acceptance: the lab retained its existing
Latin IME and used the disclosed input-only helper.
The lab was restored through normal validated Settings to official RU `ru-pilot-a`
at `544dd15f...`, explicit Russian, N5 and the original effective daily limit of 10.
The final private snapshot retains every original and legitimate new learning row.
The helper and 155 individually resolved remote XML files were removed, adbd was
returned to UID2000, and only the verified owned emulator was stopped; its ports closed.

Remaining R2/R3 blockers are still real: a second distinct CounterChoose day,
fresh exact-package authority for both Russian audio adaptations followed by actual
playback/interruption tests, and physical-phone/Japanese-IME/release acceptance.
[The exact authority request](pilot-b-media-authority-request.json) is prepared, not
approved. Ordinary RU activation and broad R4 authoring have not been unlocked.
At that checkpoint the complete 8,197 absent-path backlog plus partial units remained visible; this
checkpoint is not a claim that the full corpus has been translated.

## Subsequent owner authorization: sequential background authoring

The owner subsequently requested continuous background translation against the **same**
`6af98cb717755690a9ca793e5454a96ebd7a8f9f` target. ETA is not a constraint.
The earlier R2/R3 observations remain historical evidence, not a reason to idle the
independent text lane. Translate restricted listening packages as non-runtime drafts
until their actual publication authority is obtained; continue other families meanwhile.

Use one authoring lane and at most one read-only reviewer at a time, with serialized
tests/builds; do not launch fleets, extra authoring sessions or unattended competing writers.
Freeze convenient dependency-closed batches before authoring, review every adopted
learner-facing surface, resolve and recheck findings, then validate the combined tree.
Update exact per-file provenance and the mutable current report without rewriting old receipts.

Keep branches short-lived: pull/fetch before each batch and before integration, reconcile
concurrent work without overwriting it, commit recoverable progress periodically and push
without asking for confirmation. Use normal signed commits and normal pushes, never
force-push, amend or discard unrelated work. Integrate accepted batches frequently;
unreviewed WIP remains explicitly unaccepted on its own branch or excluded draft lane.
Record each completed batch and actual remaining scope so interrupted work can resume
without repeating, losing or falsely approving it. Do not silently retarget to later EN main.

## Reviewed source batches

Batch **001 — demonstratives** completes 23 full word articles from the frozen target:
20 retain N5, two retain N4 and one retains N3. All Japanese examples, readings, source
senses and qualifications survive. An independent complete three-facet review identified
Russian answer-label overlap; an independent narrow recheck accepted exactly 30 additional
direct pairs, with all earlier pairs preserved and no transitive expansion.
[Exact source/Russian hashes and review boundaries](translation-batches/001-demonstratives-review.json)
remain separate from the unchanged historical pilot receipts and release/device/media gates.
After batch 001, runtime membership was 104 objects; full-target statuses were 101 reviewed-current,
three partial, two reviewed runtime-blocked drafts and 8,172 pending. The 8,174 absent runtime
paths and three partial units remain work, not a completion claim.
Continue the remaining N5 vocabulary/kanji/support batches, then all later levels and families.

Batch **002 — people and family** adds three complete N5 kanji, 23 complete word articles
and three raw-identical KanjiVG stroke files. The dependency-closed family includes 女子/婦人;
all source levels and absent levels remain unchanged. A separately frozen amendment restores
the now-required 休 link in 休日 and includes that whole baseline article in re-review.
One independent reviewer actually read all 27 RU/EN learner pairs and all 23 captured dictionary
queries; Japanese correctness, actual adopted coverage and Russian comprehensibility are CLEAN
for this bounded scope, with no findings. The 32 direct answer pairs have individual evidence;
exact matching titles deduplicate without inventing transitive exclusions.
[Exact candidate hashes, actual scope and limits](translation-batches/002-people-family-review.json)
remain distinct from device, activation and restricted-media authority.

After batch 002, runtime membership was **133 objects**: 15 kanji, 93 words, 15 strokes and the unchanged
other baseline families. Full-target statuses were **130 reviewed-current**, three partial,
two reviewed runtime-blocked drafts and **8,143 pending**; **8,145 runtime paths remain absent**.
Continue the next safe sequential batch; neither this milestone nor source publication completes
the full translation objective.

Batch **003 — kinship and relationships** completes 19 more word articles. One full
independent review found two real quiz ambiguities: 男の子 also means «сын», and 奥さん
has a married-woman address use. An independent narrow recheck accepted exactly six new
direct guards, preserving the original 38 pairs and all learner body facts. The neutral
wife label is «жена другого человека (уважительно)».
[Full review, exact corrections and bounded recheck](translation-batches/003-kinship-relationships-review.json)
separate actual reading from unchanged-body reliance and record all limitations.

After batch 003, runtime membership was **152 objects**: 15 kanji, 112 words, 15 strokes and unchanged
other families. Full-target statuses were **149 reviewed-current**, three partial,
two reviewed runtime-blocked drafts and **8,124 pending**; **8,126 runtime paths remain absent**.
Continue sequential authoring against the same frozen source; release/device/media gates remain.

Batch **004 — entry and exit** completes two N5 kanji, 14 full word articles and two
byte-identical KanjiVG files. Independent full reading of all 16 RU/EN texts and captured
dictionary evidence returned CLEAN on all three facets, including the inherited 入り口
reading-table correction and the bounded Russian ～出す/～始める comparison. The latter is
not adoption of the whole optional source article.
[Exact hashes, actual review scope and limits](translation-batches/004-entry-exit-review.json)
remain separate from public-archive CI evidence and all release/device/media gates.

After batch 004, runtime membership was **170 objects**: 17 kanji, 126 words, 17 strokes and unchanged
other families. Full-target statuses were **167 reviewed-current**, three partial,
two reviewed runtime-blocked drafts and **8,106 pending**; **8,108 runtime paths remain absent**.

Batch **005 — books and study** completes 本, 28 full word articles and one byte-identical
KanjiVG file. The required negative-reference closure added six complete perception/calendar
articles before authoring; no source distractor was discarded to shrink scope.
Independent whole reading of all29 RU/EN texts,31 exact dictionary objects and154 actual
Russian answer labels returned CLEAN on all three facets, with no established finding.
The source-based 生 suffix clarification and six individually justified direct guards are
recorded with exact hashes and real scope/limits in the
[batch review](translation-batches/005-books-study-review.json).

After batch005, runtime membership was **200 objects**: 18 kanji,154 words,18 strokes and unchanged
other families. Full-target statuses were **197 reviewed-current**, three partial,
two reviewed runtime-blocked drafts and **8,076 pending**; **8,078 runtime paths remain absent**.

Batch **006 — listing and examples** completes the previously partial article, preserving all
469 frozen English lines' substantive coverage, examples, distinctions and citations.
The previously reviewed57-line Russian adaptation remains as an explicitly bounded supplement;
its four existing exercises and reviewed vocabulary contexts are unchanged.
Independent whole reading of source,536-line Russian candidate and prior adaptation returned
CLEAN on all three facets. One optional reviewer-proposed phrase now explicitly describes
not eating rather than possible food unavailability; all other article bytes are unchanged.
[Exact full review, optional correction and limited narrow recheck](translation-batches/006-listing-examples-review.json)
distinguish actual reading scope from the terse recheck result.

After batch006, membership remained **200 runtime objects**; full-target statuses became
**198 reviewed-current**, **two partial**, two reviewed runtime-blocked drafts and
**8,076 pending**. The other article and the legacy counter unit still require completion;
**8,078 runtime paths remain absent**. No checkpoint, media authority or release/device gate moved.

Batch **007 — numbers and counters article** completes all856 frozen source lines, preserving
all67 citation URL occurrences and the separately reviewed77-line general-count lesson.
The existing 時間 link remains; only20 genuinely absent optional destinations become plain labels,
without deleting teaching content. Broad practice descriptions and future Grammar navigation
are explicitly distinguished from the currently available Russian exercise sets.
One independent reviewer actually read all987 Russian lines, all856 source lines, all77 prior
Russian lines and the declared normative evidence; all three facets returned CLEAN, no findings.
The original reviewer's exact optional duration phrase was adopted verbatim, with a sole-replacement
proof and real corrected serial checks; no additional post-edit reread is claimed.
[Actual scope, hashes and limits](translation-batches/007-numbers-counters-article-review.json)
do not approve the counter families, grammar exercises or media merely mentioned by the article.

After batch007, membership remained **200 runtime objects**; statuses were **199 reviewed-current**,
**one partial** (`counters/tsu.json`), two reviewed runtime-blocked drafts and **8,076 pending**.
Both formerly partial articles are now complete; **8,078 runtime paths remain absent**.
No frozen pilot ref, checkpoint authority, ordinary activation or device/media/release gate moved.
Continue the finite remaining corpus without retargeting the frozen English revision.

Batch **008 — food, drinks and meals** completes27 full word articles:26 source-classified N5
words and the mandatory direct N4 食事 dependency. One independent reviewer actually read every
complete RU/EN pair, all27 captured dictionary queries/31 objects/73 senses and all181 actual
combined answer labels. A real missing 昼/昼御飯 lunch guard was found from the already taught
meaning in the baseline card's body, despite its different short title.
The guard was added only to the new card; two exact optional wording proposals were adopted.
One bounded independent recheck read all four affected/relevant full pairs, verified all27
current hash records and resolved the finding. Baseline 昼 and the other24 new cards remained
raw-identical. [Actual full reading and corrective closure](translation-batches/008-food-drinks-review.json)
distinguish their respective scopes; no whole-batch reread by the narrow reviewer is claimed.

After batch008, membership was **227 runtime objects**:18 kanji,181 words,18 strokes and unchanged other
families. Statuses were **226 reviewed-current**, **one partial** (`counters/tsu.json`),
**two reviewed runtime-blocked drafts** and **8,049 pending**; **8,051 runtime paths remain absent**.
All earlier tracking records and immutable receipts are preserved; checkpoint authority is null.

An actionable **external app-hint localization gap** is pinned in the008scope: committed
app `5c000bd...` falls back to raw IDs for `food`, `drinks`, `animal`, `polite-prefix`,
`suru-verb`, `meals`—26 occurrences across22 new cards, with some IDs already in baseline.
Canonical IDs remain unchanged; the concurrent app checkout was not edited or built.
The app owner still needs Russian mappings; no current dirty-app fix, phone rendering or ordinary
RU activation is claimed. This renderer/release follow-up does not stop independent source authoring.
Continue the remaining frozen corpus, with original media/device/release gates and pilot refs intact.

Batch **009 — clothing and accessories** completes23 full source-N5 word articles.
One independent reviewer actually read every complete RU/frozen-EN pair, all27 dictionary
queries/29 entries/96 senses/52 Japanese forms and all204 actual combined answer labels,
plus relevant baseline bodies and actual spelling/etymology evidence. The four direct symmetric
guards are individually justified, not a clothing-category clique. The previously reviewed
`時間` candidate-pool adaptation remains unchanged; `時計` explicitly names a physical device.

The full reviewer found one low-severity **provenance** error, not a learner-text defect:
an editorial receipt incorrectly claimed that an additional reading appeared in the capture.
The clarification and active evidence guidance were corrected; the original frozen receipt
remains historical. One actual bounded recheck read the complete relevant pair/query and
corrected records, resolved the finding and verified all23 learner files raw/LF-unchanged.
[Actual full and narrow review scopes](translation-batches/009-clothing-accessories-review.json)
are distinct; no second whole-batch linguistic reread or native certification is claimed.

After batch009, membership was **250 runtime objects**:18 kanji,204 words,18 strokes and unchanged
other families. Statuses were **249 reviewed-current**, **one partial** (`counters/tsu.json`),
**two reviewed runtime-blocked drafts** and **8,026 pending**; **8,028 runtime paths remain absent**.
All227 earlier tracking records are unchanged; fresh strict progress preserves null checkpoint authority.

The pinned renderer follow-up additionally records `clothing`, `sports`, `everyday`,
`special-reading`, `weather`, `irregular-reading`, `actions`:25 occurrences across23 new cards.
Canonical IDs are preserved and the concurrent app remains untouched; no current phone rendering,
native option-pool, media, activation or release acceptance follows from source review.
Continue the remaining finite frozen target; no device gate or pilot/controlled ref has moved.

Batch **010 — home and furniture** completes25 full word articles:24 source-N5 words
and the mandatory direct N4 会話 dependency. One independent read-only reviewer actually read
all25 complete Russian/frozen-English pairs, the complete frozen マンション comparison,
all32 complete dictionary queries/32 entries/82 sense records/58 forms and every one
of229 actual answer-label/metadata records. Nine relevant baseline bodies were read in full;
other baseline objects received fingerprint/metadata checks, not whole linguistic rereview.
The24 Wikipedia records are capture provenance, not lexical proof.
All three facets returned CLEAN, with no established consequential defect or optional polish.
[Exact actual scope, fingerprints and limits](translation-batches/010-home-furniture-review.json)
record100 candidate RAW/LF comparisons,50 frozen-source comparisons and all275 manifest hashes.

The seven direct Russian guards are individually justified. In particular, shared «кухня»
in 台所/料理 would be an ambiguous answer label even though the bodies distinguish a cooking
room from a culinary tradition; only the new 台所 card adds that guard and clarification.
No housing/furniture/category or transitive clique was introduced. Separate fully read
電力/汽車 evidence supports conservative electrical-power terminology and qualified
dated/rural train senses; neither auxiliary article was adopted.
A mistakenly retained provisional sentence in the signed freeze receipt is explicitly corrected
by the new adjudication; its original historical bytes are preserved. Active guidance now
requires checking stage claims before final freeze and explicit correction of immutable errors.

After batch010, membership was **275 runtime objects**:18 kanji,229 words,18 strokes and unchanged
other families. Fresh strict8278-entry progress had **274 reviewed-current**, **one partial**
(`counters/tsu.json`), **two reviewed runtime-blocked drafts** and **8,001 pending**;
**8,003 runtime paths remain absent**. All250 earlier tracking records and their non-record
sections are preserved. Checkpoint authority remains null and checkpointReady false.

Actual serialized checks:0 validator errors,124 tests passed in28.009s, final budget
282files/291entries/880178retained/893595inflated/476833localZIP bytes after manifest generation.
Version is `08b6d0fe34307bea`. The pinned external app follow-up covers17 canonical IDs,
29 occurrences across24 new cards; some IDs already existed. IDs and concurrent app checkout
remain untouched. Source review is not native, rendering, phone, package/media, ordinary activation
or release acceptance. All four frozen pilot/controlled refs remain separately fixed.
Continue the remaining finite frozen corpus; no independent safe authoring lane is blocked.

Batch **011 — stationery and personal objects** completes21 full source-N5 word articles.
One independent read-only reviewer actually read every complete Russian/frozen-English pair:
699 English lines and848 Russian lines. All23 complete queries/24entries/57sense records/36forms,
all250 actual answer-label/metadata records and four complete baseline EN/RU pairs were read.
The19 Wikipedia records and the independent same-reading ＰＥＮ organization entry were not
used as ordinary stationery lexical evidence. The complete GogenYurai origin article was freshly
read; 鞄 remains qualified as uncertain borrowing, not inferred native history from its kanji.
All three facets returned CLEAN, no consequential finding or optional polish.
[Exact actual review and limits](translation-batches/011-stationery-personal-objects-review.json)
distinguish the full assigned scope from the other229 baseline bodies, which were not freshly
linguistically rereviewed. The reviewer did not verify signature authenticity or rerun author tests.

Three direct Russian guards are individually justified: ペン/ボールペン, ペン/万年筆,
and 新聞/雑誌. The last protects broad «периодическое издание» in the displayed Russian label;
it does not assert Japanese interchangeability. No inferred ボールペン/万年筆 edge,
publication/category clique or transitive closure was added. All source teaching survives27
optional-link flattenings; 紙→新聞 remains. カメラ retains its legitimate three-section structure.
Selected fountain-pen reading does not deny captured variants; the paper homophone comparison
does not invent pitch data, and photographic spelling/mnemonics do not guarantee image truth.

At the batch011 milestone membership was **296 runtime objects**:18 kanji,250 words,18 strokes
and unchanged other families. That strict8278-entry progress had **295 reviewed-current**, **one partial**
(`counters/tsu.json`), **two reviewed runtime-blocked drafts** and **7,980 pending**;
**7,982 runtime paths remain absent**. All275 previous tracking records/non-record sections
and canonical runtime Git blobs are unchanged. Checkpoint authority remains null and
checkpointReady false. This is not completion of the full corpus.

Actual serialized checks:0 validator errors,124 tests passed in30.629s, final budget
303files/312entries/927602retained/941019inflated/502457localZIP bytes after manifest generation.
Version is `5a0e500cfdbc372d`. Pinned app follow-up covers17 canonical IDs/22occurrences/19cards,
not all newly introduced. Canonical IDs, concurrent app checkout and all frozen pilot/controlled
refs remain untouched. No ordinary activation, native/rendering/phone, package/media or release
approval follows. Continue the next safe source batch against the same finite frozen target.

Batch **012 — N5 legacy-counter dependency closure** completes the full ten-file schema1
component: nine new files and the two previously omitted reverse fixtures in `tsu.json`.
This is124 forward cards,20 reverse fixtures,80 actual referenced noun contexts and191 Russian
learner-text leaves, not124 runtime paths or completion of all N5 content.
[Actual composite review](translation-batches/012-n5-counter-closure-review.json) preserves
the initial whole254EN/259RU-line review and its genuine findings. Six source-derived
wrong `回` choices allowed ordinary action-frequency meanings; bare `お茶` was also a valid
`本` reverse answer for bottled tea. Exactly seven negative-choice sites were separately frozen,
corrected and independently adjudicated. Original prompts, quantities, accepted tiers/readings,
IDs and all191 Russian leaf values stayed unchanged. Active counter guidance records the lesson.

The narrower evidence adjudicator read12 complete current/source/initial records, the changed
fixture's four live nouns, actual direct usage/range evidence and relevant guidance.
F1/F2 and the complete `五六本`→`ごろっぽん` language/bounded-answer-policy question resolved
CLEAN. This was not a second124-pair review. A generic interim “no significant issues” result
did not supply reading scope or resolve U1 and is not substituted for the actual adjudication.
The historical range capture remains immutable even though the fresh haiku-page RAW changed;
the actual target fields were checked, and original printed-book consultation is not claimed.

At the batch012 milestone membership was **305 runtime objects**, including11 counter files. Its strict8278-entry
progress had **305 reviewed-current**, **no partial units**, **two reviewed runtime-blocked drafts**
and **7,971 pending**; **7,973 runtime paths remain absent**. Only the current partial-tsu
tracking record was replaced after real full-scope review; its Pilot B receipts remain historical.
All295 other earlier tracking records/canonical runtime blobs and all non-record sections stay
unchanged. Checkpoint authority remains null and checkpointReady false.

Actual final serialized checks:0 validator errors,124 tests passed in43.252s; final budget
312files/321entries/984818retained/998235inflated/520508localZIP bytes. Version is
`e82c69299a2d0bbe`. No word labels/guards/tags, assets/media or concurrent app files changed.
Native/editor certification, exhaustive counter alternatives, Android range/full-phrase grading
and ordinary activation/device/media/release tests remain unperformed/separately gated; source
acceptance does not erase those bounds or move any frozen pilot/controlled ref.
The next proposed lane at that time was eleven missing N5 schema2 number/time files.
It was subsequently frozen, authored and reviewed as013 below.

Batch **013 — N5 number/time expressions** completes eleven schema2 files and122 expressions:
age/floor, clock/minutes, calendar months/dates and durations in hours/days/weeks/months/years.
All255 learner-text leaves are Russian;392 written-answer and149 reading-answer occurrences retain
the exact frozen Japanese values, canonical-versus-alternate-reading boundaries, IDs and metadata.
The single already-reviewed native expression and complete numbers article are unchanged support,
not new013 acceptance objects or duplicated exercise identities.

[Actual composite review](translation-batches/013-n5-number-time-expressions-review.json) preserves
whole2064EN/2064RU-line reading, all122 complete pairs and full987RU/856EN-line article support.
Japanese correctness and adopted coverage were CLEAN; one actual Russian finding required
`24 дней` → `24 дня`. The exact one-cue repair was independently read and rechecked, together with
the two added active-guidance lines about actual numeral declensions. Other254 Russian leaves,
all Japanese/technical/accepted forms, other ten new files and all305 baseline RAW runtime objects
remain unchanged. This narrower proof is not a second whole122-expression semantic review.
The original NEEDS FIX report remains historical; all three composite source/text facets are CLEAN.

At the batch013 milestone membership was **316 runtime objects**:18 kanji,250 words,18 strokes,2 articles,22 counter
files,1 grammar set,2 scene catalogs and3 images. Its strict8278-entry progress had
**316 reviewed-current**, **no partial units**, **two reviewed runtime-blocked drafts** and
**7,960 pending**; **7,962 runtime paths remain absent**. All305 earlier tracking records and
non-record sections are unchanged. Checkpoint authority remains null and checkpointReady false.
This is not completion of the full corpus or all N5 teaching.

Actual final serialized checks:0 validator errors,124 tests passed in28.490s; final budget
323files/332entries/1077037retained/1090454inflated/534880localZIP bytes. Version is
`2d5ac8dd3491a7de`. Explicit date-validity/day-only,週間 andか月-unit constraints survive;
unlisted readings are not declared impossible. No new word-quiz guards/tags, grammar-vocabulary
contexts, media/assets or concurrent app changes were made. Original PDFs/printed dictionaries
were not newly consulted, and automated editorial evidence is not native/exhaustive/parser/
Android/phone/IME/media/activation/release approval. C6/C7 and four frozen pilot/controlled refs
remain separate and unchanged. Continue remaining N5 calendar/time words, freezing their actual
direct dependency/negative-reference closure before authoring, then continue all remaining families.

Batch **014 — calendar/time vocabulary** completes38 full word articles:34 N5 roots and four
mandatory negative-reference dependencies. Source levels remain35 N5/two N4/one N3; no N1 coverage
is invented. The15 original direct exclusions/distractors survive. Six additional individually
evidenced Russian guards protect shared morning meaning and actual breakfast/dinner senses against
the inspected baseline labels. They are not a transitive daypart/meal clique or blanket adoption
of every captured sense. All316 prior runtime RAW objects and tracking records remain unchanged.

[Actual composite review](translation-batches/014-calendar-time-words-review.json) preserves full
1302EN/1271RU-line reading, all38 titles and152 sections, all288 actual displayed meanings and seven
complete supporting baseline bodies. All45 complete dictionary entries/70 forms were inspected;
81 returned sense objects comprise64 lexical senses and17 Wikipedia pseudo-definitions, not81
lexical senses plus17. The latter are not lexical proof. Source-specific reading restrictions,
mixed on/kun classification, calendar periods versus durations and recurrence versus all-night
activity remain explicit. Optional navigation has49 retained/64 flattened references, with no
substantive teaching removed or English placeholder cards added.

One genuine minor finding narrowed夕方 to time before evening. The exact clause was corrected to
«конец дня или ранний вечер» and independently rechecked against the complete original/current/source
朝 articles and existing晩/夜 comparisons. Other37 new files, all Japanese/technical fields and
all316 baseline RAW objects are unchanged. Two active boundary-meaning guidance lines accompany the
repair; three earlier API-pseudo-definition guidance lines remain. This is a whole38 review plus
a real narrow correction proof, not two whole38 semantic reviews. The initial NEEDS FIX receipt
is preserved; all three final composite source/text facets are CLEAN.

At the batch014 milestone membership was **354 runtime objects**:18 kanji,288 words,18 strokes,2 articles,22 counter
files,1 grammar set,2 scene catalogs and3 images. That strict8278-entry progress had
**354 reviewed-current**, **no partial units**, **two reviewed runtime-blocked drafts** and
**7,922 pending**; **7,924 runtime paths remain absent**. All316 old tracking records/non-record
sections remain unchanged. Checkpoint authority remains null and checkpointReady false.
Actual final serialized checks:0 errors/124 tests32.911s; budget361files/370entries/
1163599retained/1177016inflated/581157localZIP bytes; version `636066eada6c6783`.

The immutable pinned app function exposes seven unmapped canonical IDs across21 occurrences/
20 new cards; some IDs were already known. This is a recorded app-hint follow-up, not permission
to edit the concurrent app or translate technical IDs. No grammar contexts/assets/media or app
changes were made. Source publication does not grant native/device/IME/C6/C7/media/package/
activation/release/checkpoint authority or move any frozen runtime ref. Continue the next safe
remaining N5 kanji/words/support batch, then every remaining level and source family against6af98cb.

Batch **015 — calendar/count word prerequisites** completes37 full word articles: nine calendar
months, eleven date/duration forms, nine native counts,十,一人/二人 and five numeral/currency
forms. Source23 N5/14 unlabelled classifications remain unchanged. The frozen target has no
二月/十一月/十二月 word paths; their substantive inline examples remain, with no invented files.
Source37 have zero negative-reference edges. Two individually reviewed direct Russian guards
protect一日–日 and一人–人 against actual bare singular labels, not a generic/transitive clique.

[Actual composite review](translation-batches/015-calendar-count-words-review.json) records complete
1134EN/1138RU-line reading,37 titles/148 sections, all325 actual displayed meanings and complete
日/人 source/RU supporting pairs. All56 complete dictionary query objects were read:57 entry
occurrences/177 forms/136 returned sense objects, including12 Place and4 Wikipedia objects;
120 lexical occurrences remain. Occurrences are not asserted unique or blanket learner adoption.
Counter-specific sound changes replace overgeneralized initial-letter rules; attested五日ごにち/
二十日にじゅうにち are not falsely prohibited. Actual named Japanese definitions support both
五月晴れ senses and the old-calendar link. Current BOJ denominations support bounded note claims.

One genuine minor finding exposed an unsupported added一千円 spelling claim and a false positive
attribution to the captured千円 entry. The added claim was removed; the original ordinary-use
contrast remains, without declaring the spelling universally invalid. An explicit superseding
erratum withdraws the false claims in historical scope/preauthoring/adjudication records without
rewriting them. An independent exact-delta/evidence recheck resolved B015-R1 at high confidence;
other36 new words/all354 baseline RAW objects remain unchanged. This is a whole37 review plus
a real narrow recheck, not two whole37 semantic reviews. All final composite facets are CLEAN.

At the015 milestone membership was **391 runtime objects**:18 kanji,325 words,18 strokes,2 articles,22 counter
files,1 grammar set,2 scene catalogs and3 images. Fresh strict8278-entry progress has
**391 reviewed-current**, **no partial units**, **two reviewed runtime-blocked drafts** and
**7,885 pending**; **7,887 runtime paths remain absent**. All354 prior tracking records and
non-record sections remain unchanged; checkpoint authority null/Ready false.
Actual final serialized checks:0 errors/124 tests32.014s; budget398files/407entries/
1234441retained/1248458inflated/620416localZIP bytes; version `95a8d5dc2948138c`.

The immutable pinned app function has11 unmapped canonical IDs across56 occurrences in this
batch; preserve those IDs and leave the concurrent app untouched. Eight directly related
guidance lines and the JMnedict/ENAMDICT provenance attribution accompany the work; no assets,
grammar contexts or media were added. C6/C7/native/device/IME/media/package/activation/release/
checkpoint authority and frozen runtime refs remain separate. Continue the next safe required-word
support batch for the actual57-new-kanji distractor component, then all remaining frozen families;
mandatory distractors are not dropped to shrink the scope.

Batch **016 — everyday reading-word prerequisites** completes25 full word articles:19 roots
and six mandatory source negative-reference dependencies. Source24 N5/one N3 classifications and
all eight directed source edges remain unchanged. Eight individually reviewed additional direct
Russian guards protect actual car/transport, knowledge, departure/appearance and birth-appearance
overlaps. The足–お金pair is narrowly conservative: its witness is colloquial and usually
prefixedお, not proof that ordinary bare足means money. No transitive family clique is inferred.

[Actual whole review](translation-batches/016-everyday-reading-words-review.json) records complete
820EN/844RU-line reading,25 titles/100 sections, all350 actual displayed meanings and nine complete
unchanged Russian baseline bodies totalling310lines. All73 complete dictionary query/entry
occurrences were read:126forms/289objects=270lexical+twoPlace+17Wikipedia; occurrences are not
unique lexemes or blanket sense adoption. Both complete textual Japanese Tokyo-pitch sections
confirm雨HL/飴LH, without audio-listening claims. No consequential finding or required correction
was established; all three scoped source/text facets are CLEAN after the actual whole review.

Source手–足is correctly a body-part comparison, not a strict antonym pair. Both毎年readings,
intransitive birth, know/understand qualifications, lending direction, half/minute and colour
conventions remain explicit. Two related active-guidance lines document the source-label issue.
All391 prior runtime RAW objects/tracking records and non-record sections remain unchanged.

Current membership is **416 runtime objects**:18kanji,350words,18strokes,2articles,22counterfiles,
onegrammarset,2scenecatalogs and3images. Fresh strict8278-entry progress has **416reviewed-current**,
**no partial units**, **two reviewed runtime-blocked drafts**, **7,860pending** and **7,862runtime
paths absent**. Checkpoint authority remains null/Readyfalse.
Actual serialized checks:0errors/124tests48.039s; final budget423files/432entries/
1294859retained/1308876inflated/651417localZIPbytes; version `faa2fe07d4ce9f22`.

The immutable pinned app function has11 unmapped canonical IDs across13 occurrences in this batch.
Keep canonical IDs stable and the concurrent app untouched. All25new working texts are CRLF;
Git/public LF domains are separately verified, not falsely equated with working RAW.
No new assets/grammar contexts/media or native/device/IME/C6/C7/package/activation/release/checkpoint
authority follows. Continue the next safe required-word support batch, the real57-new-kanji
mandatory-distractor component and every remaining frozen family.
