# Russian translation handoff, 2026-11-25

**Public Russian `main` is still B256 (`f6b5413d57f17d720301fb9ff8c4130d7e83cfed`), the last published batch.** Everything newer is private or unreviewed: the offline reader, the sealed manuscripts, the B257 recheck records and the scratch branches. No unit below has independent acceptance, and the overall translation is not complete. This record gives the next owner the exact state of each unit, the gate that stops it and the evidence behind a few rules in the instructions. It is a status receipt, not a review, acceptance, release or device test.

## Snapshot

| Item | Revision |
|---|---|
| Russian `main` (B256) | `f6b5413d57f17d720301fb9ff8c4130d7e83cfed` |
| English frozen translation source | `6af98cb717755690a9ca793e5454a96ebd7a8f9f` |
| English guidance merge, [stop-cran/learning-japanese#66](https://github.com/stop-cran/learning-japanese/pull/66) | `dd057663ae8ed6c89647704655311082a8551a02` |
| English example correction merge, [stop-cran/learning-japanese#67](https://github.com/stop-cran/learning-japanese/pull/67) | `c70ee4543565a7a9ed175969940a9bf5f27fce43` |
| English `main` when last checked (not adopted) | `74cecafa6bfdbaa2320880f76466ab7292a16001` |
| Android `main` (code read, not built or run) | `91e1d4b578859f7bfb582f7b9c6acf48c6ca6a75` |
| B257 fix 4 (signed) | `fc7d195e010a02dc0bc163fb7da877bfdbade803` |
| B257 branch tip: fix 4 plus four recheck records (signed, no PR) | `a1de18054b228dd8c6438aed1ee24548597a342b` |

The newest complete private offline reader is `private-1574-quantity-contrast-on-017.zip`: 1,570 pending exercises plus four pilots on top of library 017. It was never published or sent as a library 018. The earlier `private-1574-hoka-on-017.zip` is superseded by it.

Tracking:

- Russian repository: [#7](https://github.com/stop-cran/learning-japanese-ru/issues/7) roadmap and acceptance gates, [#6](https://github.com/stop-cran/learning-japanese-ru/issues/6) Pilot B, [#5](https://github.com/stop-cran/learning-japanese-ru/issues/5) pilot checkpoints and methodology, [#4](https://github.com/stop-cran/learning-japanese-ru/issues/4) localization roadmap, [#3](https://github.com/stop-cran/learning-japanese-ru/issues/3) staged rollout, [#1](https://github.com/stop-cran/learning-japanese-ru/issues/1) instructions.
- English repository: [stop-cran/learning-japanese#61](https://github.com/stop-cran/learning-japanese/issues/61) language-aware schema and tooling, [stop-cran/learning-japanese#62](https://github.com/stop-cran/learning-japanese/issues/62) three inherited explanation errors.
- Android: [stop-cran/kanji-cards-android#127](https://github.com/stop-cran/kanji-cards-android/issues/127) language and repository selection, [stop-cran/kanji-cards-android#28](https://github.com/stop-cran/kanji-cards-android/issues/28) app strings, accessibility and voice.

## What this handoff pushed

- Russian repository: the B257 branch tip above (four recheck records, no PR); four `scratch/*-do-not-merge` branches (listed below, no PRs); and the pull request that adds this record together with the instruction updates.
- English repository: [#66](https://github.com/stop-cran/learning-japanese/pull/66) and [#67](https://github.com/stop-cran/learning-japanese/pull/67), both merged after green checks. Their guidance text had no independent review.
- Nothing else. No learner content, manifest, progress ledger, published reader, release or Android file changed, and no private manuscript, archive or reader page was pushed.

## Owner sessions

The private artifacts live in the `files` folder of each Copilot session-state directory on the project owner's machine and in no repository. Sessions may not survive an app restart; their `files` folders do. Recover the original owners before allocating a new slot. Check each pause handoff, the files on disk and any signed head, and do not infer acceptance from a partial file or from the four B257 recheck records.

| Prefix | Session ID | Role and state |
|---|---|---|
| `d5123981` | `d5123981-0a00-4cc2-b316-43f95155663b` | Coordinator: private offline reader integration, this handoff |
| `e7df86ac` | `e7df86ac-f4ff-4011-a20b-f01264c7c6ea` | B257 records owner (paused; reviewer slot released) |
| `10354058` | `10354058-ec93-43d8-8699-ee562290418e` | Author of the 16-exercise `ずつ` unit; holds the single author slot |
| `b5028318` | `b5028318-f66b-4733-adb5-093e73f514ee` | Quantity author (manuscript 001 sealed; slot released) |
| `f28a2f6c` | `f28a2f6c-608d-4485-9fb4-153f5482c3c2` | Hoka exclusion author (manuscript 002 sealed; slot released) |
| `263c2174` | `263c2174-7c1e-4635-90ff-7fa875494ab8` | Restriction and inclusion author (manuscript 002 sealed; slot released) |
| `907edb63` | `907edb63-9b53-471b-bf27-544ac10b48ab` | Particle-neighbors author (manuscript 002 sealed; slot released) |
| `5e8890f6` | `5e8890f6-0314-4707-a985-621e51353630` | Correctness reviewer for the restriction article (stopped, idle, no verdict) |

No session automation was running on the coordinator or on the two paused owners.

## Work in flight

The project allows one learner author and at most one reviewer at a time. After the `ずつ` author releases the slot, the order is: the quantity author (`b5028318`) on `quantity-combined-repair-author-input-001`, then the Hoka author (`f28a2f6c`) on `hoka-combined-repair-author-input-001`, then the sibling companion sets. Do not start the quantity and Hoka repair authors in parallel.

| Unit | State at handoff | Next step | Gate |
|---|---|---|---|
| B257 (words batch 96) | Fix 4 signed; four recheck records pushed; `257-words-batch-96-review-execution-003.json` not written | Write that record, then accept the source as a separate step | Source acceptance, ledger, progress, tracking and the four serial gates are later steps; no publication clearance |
| `ずつ` (16 exercises) | Partial checkpoint: draft labels, instruction templates, questions, claims, glosses | Finish explanations and option rationales, build, seal, release the slot | Author-only draft; needs independent review |
| Quantity (52 exercises and an article) | Manuscript 001 sealed; repairs listed below | Repair author works from the combined repair input | Review of the repaired text |
| Hoka exclusion (12 exercises) | Manuscript 002 sealed; repairs listed below | Repair author works from the combined repair input | Review of the repaired text |
| Restriction and inclusion (50 exercises and an article) | Manuscript 002 sealed | Three-family blind review of the complete article from the prepared specimen | No verdict yet, so no clearance |
| Particle neighbors (15 exercises) | Manuscript 002 sealed; five contexts corrected | Same-reviewer recheck of the five contexts; coordinator integration | All 15 lexical records pending; the `訳` link decision below |
| Companion sets (24 and 24) | Source packets prepared | Author after the units above | None accepted or integrated |
| Wording backlog | Listed below | Unscheduled | Each item needs an author, then review |

## B257 (words batch 96)

- Branch `romanko-microsoft-russian-batch-257` is at `a1de18054b228dd8c6438aed1ee24548597a342b`. Its only parent is fix 4 `fc7d195e010a02dc0bc163fb7da877bfdbade803` (tree `4691d166cddf3d033b850c2f7264203a7e4b65c4`, content version `edfb911307b5669f`). The owner session reported these gates for fix 4: 5,829 manifest entries, 0 validation errors, 124 tests and an 8,468,430-byte archive. I did not re-run them.
- The tip adds the four recheck records below and nothing else: no ledger, progress or tracking change, and no source acceptance. There is no pull request because the source is not accepted.

| Record | Bytes | SHA-256 |
|---|---|---|
| `257-words-batch-96-recheck-001.md` | 23,566 | `c76f80270e60ea73e178a183dccd922e8e3f4fd7ec7a5183c9c1a02f773cd79a` |
| `257-words-batch-96-recheck-002.md` | 10,453 | `90c6e810900e21611c1a306bfcd0d467b5b7216c680ca543d77e06fd0b1b18fe` |
| `257-words-batch-96-recheck-003.md` | 45,011 | `fdebd700f7355618179d52c8fc1cff5d0ab66ff53768039aed2cfa8c55d8c783` |
| `257-words-batch-96-recheck-004.md` | 38,266 | `6022f024fd6ca6a1f5201549008e7aaecfe88b0b85061f778b765daf6591801a` |

- All four records link to `257-words-batch-96-review-execution-003.json`. That file does not exist, and no partial copy exists, so those links dangle until it is written. The same applies to its two generator scripts.
- The owner's design has ten rechecks. The final rechecks #8 to #10 on fix 4 are reported clean on three distinct actual model families (GPT, Claude, Grok), and the intended flags are: source not accepted, ledger and progress not updated, publication not approved. The original consistency reviewer has been unreachable since 06:10Z on 2026-11-24; a replacement made rechecks #7 and #8. Four idle reviewer instances (`2244d4c0`, `fbadf36a`, `881b23c8`, `6ec8511a`) may not survive a restart, and none is needed for the remaining steps.
- Resume steps: re-verify the state (branch tip, the four hashes above); write the execution-003 generator with its assertions and a public-path scan (no local path, no CR in the output); make a signed commit of exactly the five records; re-run the coordinator's body verifier `b257_exact_recheck_bodies.py` (it passed earlier on ten bodies, 72,707 bytes); push as stop-cran and check that GitHub reports the commit verified. Details are in `b257-recovery-note.md` and `b257-r003-exec003-design.md` (Preserved artifacts).
- Source acceptance is a separate later step: finalize independent-review-001 from the draft folder, run `reviewed_source.py`, update the 汗 ledger note keeping its six B203 links, update progress and tracking, make signed commits, run `batch.py validate` and the four serial gates, then report. No device, media, voice, drawing, activation or publication clearance exists.
- Three lines in `recheck-003` (two) and `recheck-004` (one) quote a local reviewer-input directory verbatim. The sealed bytes were left unaltered, so the execution-003 record needs its own public-path scan, and the later acceptance step should decide whether to redact with a documented transformation.
- B258 to B270 drafts exist only as session material. A signed-fix cumulative replay through B270 has the receipt `b258-b270-on-signed-b257-fix-001.json` (390 new words, final manifest `0d9fef6b321f63e9`, 6,214 file entries, 124 tests, 0 errors). It is not a signed B258 seed and not a promotion.

## Restriction and inclusion, and the `歩く` and `飲む` word pointers

The unit is 50 exercises in 8 groups (8, then 6 in each of seven groups), 42 example keys, 128 base options plus 8 extra, 129 accepted strings and a new Russian article, `only-and-unexpected-inclusion.md`. The sealed successor 002 replaces 001; 001 and its control stay unchanged. The 50 exercises were already delivered to the project owner as `russian-restriction-practice-50.zip`; do not resend it.

What 002 changed against 001 (the author checked it by object equality; I did not re-derive it):

- #25 and #26: translation only («…подходящую выделительную частицу из этого урока или сочетание таких частиц…»). No Japanese answer is printed, and keys, options and feedback are unchanged. The frozen English wording still says "combination" while accepting single particles; that is inherited and English is unchanged.
- Glosses: #20 «не могу заниматься»; #21 and #22 «ошибаются; отвечают неверно».
- Article lines 313 and 314 now link `quantity-ranges-and-frequency.md` and the false sentence was removed.
- The active `word` pointer is omitted for `歩く` (#37) and `飲む` (#43), explained next.

Counts: 97 lexical spans and 227 exclusions; 92 active pointers to 32 cards and 2 withheld (source: 94 pointers to 33 cards). All 97 rows are pending and unapplied. The lexical reports are kept only as evidence because they reviewed 001. The grammar validator reports 0 errors and one expected warning (topic-inclusion), and the complete-coverage check blocks on 50 pending reviews, as intended.

**Why `word` is omitted.** For these two spans the reading, headword and gloss stay and the historical pointer is kept under `sourcePointer` with `reference: null`.

- RI-RU-01, #37 (`restrict-station-end`, span `歩きました` [4,9)): `words/歩く.md:18` holds «駅まで歩きます。（えきまで あるきます。）— Я дойду до станции пешком.» This valid full-card example reveals the endpoint relation the task tests; the local gloss «шёл пешком» does not. A `word` pointer would put that example one tap before the answer.
- RI-RU-02, #43 (`restrict-tea-suggestion`): `words/飲む.md:15` holds お茶を飲みませんか — не хотите чаю? It is an invitation, but it does not prove the tested でも contrast. The pointer was withheld as a precaution. The 001 notes cited line 16; line 15 is correct. 飲む keeps three pointers (the water-dake item, #47 and #48).
- Mechanism: in the Android reader the "read the article" button appears only when the span's `word` is a key of the installed cards (`lookupHasArticle()`, code read at Android `91e1d4b5`, not a device check). Omitting `word` removes the button before the answer.
- Both decisions are author judgments with no independent review.

Open gate: the three-family blind review of the complete article. The specimen `restriction-complete-article-blind-001.zip` is ready. Its correctness reviewer (`5e8890f6`) confirmed the archive hash and the article's presence, then stopped. No section, example or cited source was checked, so there is no correctness or coverage verdict and no clearance. Begin with the full article on the same specimen. Integration into the offline reader beyond the delivered practice ZIP is not done.

## The reused article and the `訳` link

The particle-neighbors manuscript reuses the sealed Russian article `koto-wake-and-formal-nouns.md` unchanged (SHA-256 `5d5df589bf4f0e3963f91e06b6e8928e34beb62604970bbded029d280f8a4302`, 239,806 bytes, no CR).

- It links `../words/訳.md` at line 57 and `../kanji/訳.md` at line 58. The English source at `6af98cb7` links the same targets at lines 54 and 55, and `kanji/訳.md` exists there.
- Russian `main` (`f6b5413d`) has `words/訳.md` but no `kanji/訳.md` and no copy of the article, and `validate.py` reports 0 errors on it, so this is not a defect on `main`.
- According to the particle-neighbors author's fixture on the materialized B256 baseline, adding the article yields exactly one error: `articles/koto-wake-and-formal-nouns.md: broken link: ../kanji/訳.md`. I did not re-run that fixture. The article therefore needs a reviewed Russian `kanji/訳.md` card or a separate link decision before it is published.
- The author's earlier note that the broken links target missing articles was wrong; the single broken target is the kanji card.
- Two observations the author left unchanged: article line 1259 says «почти только и делаю» while the task says «только и делаю»; and article lines 1251 to 1253 mention the quantity supplement without the English link to `quantity-ranges-and-frequency.md`.

## Particle neighbors (15 exercises)

- Manuscript 002 (57 members) keeps the exact Japanese, keys, options, accepted strings, stored order, graph, article and source-record hashes. It corrects exactly 10 Russian fields on #8, #10, #12, #13 and #15: quantity rather than identity; sweets stay sweets and dinner stays dinner; leisure completion rather than friends parting; #15 distinguishes recently finishing leisure from just arriving home. The optional six-front refinement was not taken.
- At #8 the span [26,28) なく is now a function exclusion; the separate counters [4,6), [18,20), [22,24) and [29,31) remain. Effective segmentation: 99 spans and 115 exclusions (64 function, 36 punctuation, 15 target), a full 214-segment exact tiling and zero word pointers.
- All 15 lexical records remain pending, and neither older review transfers to the corrected contexts. The five corrected contexts and the one changed occurrence need a same-reviewer recheck. Update hashes for the five contexts are in the control and `pending/rows.json`.
- Integration is the coordinator's job and is not done: `evidence/integration-boundary.json` records all 196 old block hashes and exactly 191 required-unchanged blocks (181 earlier and 10 untouched new). No page was patched or rendered, so rendered-successor preservation is unclaimed. Keep the actual mixed display order separate from the JSON option order.

## Quantity set (52 exercises and an article)

Manuscript 001 has 52 exercises in 10 groups (38 distinct keys; 4 formation and 48 interpretation tasks), 116 ordered options, 94 accepted entries and the new article `quantity-ranges-and-frequency.md`. All 52 contexts are pending and no hint was applied. Repairs still needed:

- Remove the ordered Japanese ingredient list from the #33 and #34 directions.
- Neutralize the "stated" speed in #39; treat #37 and #39 as guided menus.
- Fix the word «unit» at #32.
- Fix the stock-versus-current wording at #43 and #45.
- Fix one group label.

## Hoka exclusion (12 exercises)

Manuscript 002 supersedes 001 (001 is retained; the candidate, inventory and proposal bytes are identical, and 002 adds the exact 117-ID check and disables helper bytecode writes). All twelve records are pending with no word pointers. Of the twelve, #1, #2, #5 and #6 intersect the frozen 117-ID quantity reuse list in four IDs; the other eight are compatibility-only. The `ほか` routes are integrated in the private offline reader only. Repairs still needed:

- At #11, distinguish the only route currently available in a dictionary from mere possibility.
- At #7, `まだ` already supplies «ещё».
- At #8, do not gloss `呼ばれ` as «после того как».

## `ずつ` unit (16 exercises)

The author (`10354058`) holds the single author slot. The partial checkpoint `quantity-zutsu-partial-checkpoint-001.json` parses as JSON, and a check against the frozen English prompts confirmed 16 IDs, 8 questions and 8 claims.

- Done: source and reader ZIPs verified, source extracted, references read, draft Russian wording saved (labels, instruction templates, 8 questions, 8 claims, shared evidence, explanation format, glosses) with uncertainties and drafted departures.
- Not done: Russian explanations and the 32 option rationales; reconciling the 言える and 言えない instruction with the installed ease-methods formula; the implications heading and the singular «в другом задании» evidence wording; the reader's section 7 heading id; the author-input JSON and build script; build, readback and seal; the handoff and slot release.
- Eight adjacent pairs share seven Japanese messages, so the pair guidance in the reader mechanics applies. Vary the order of the supported claim on the lesson and the roadmap for the pairs #11 and #12 and #15 and #16.
- No new quantity reader exercises should enter the combined 1,574 parent without an author handoff.

## Wording backlog (unscheduled)

- **Topic and inclusion choices.** Basic-particle exercises 57 and 58 (as numbered in the private review `bb654ba1`): both the Russian and the frozen English prompt say to add one of は or も, but each three-choice menu shows only the correct candidate. The typed keys are correct, and the source construction's case framing covers both labels, so do not simply add an incorrect option with the same ID as the correct one. Reconcile with source-safe choices or scaffold the task explicitly. No hint, card or public change yet.
- **Noun-role wording.** Basic 10: the と distractor does not mark the person summoned and need not be comitative. Basic 11: use a neutral same-owner «свою». Basic 12, 39 and 42: 学校の先生 does not encode «этой». Treat supplied copula forms, negative pieces and the の heading as guided practice, not unassisted mastery. Rebind changed contexts and verify the real learner blocks. Author-ready input `41d1bf0e` covers 13 tasks and 17 fields across the first three panels and binds 8 overlapping lexical overlays; it is not itself the repair.
- **Places wording.** Clarify the #23 pre-answer cue (medium versus direct object of 話す, two different roles) without printing either で or を; keys and feedback are sound. For #17, #18, #21 and #22, restore the basic and everyday scope if formal にて is excluded. Recognize the paired cue and feedback exposures 14 to 18, 21 to 25, 22 to 26 and 27, and 27 to 28 as guided contrasts, not independent recall. No lexical apply; rebind edited contexts.
- **Range wording.** #45 and #46 both already give から and まで while まで is visibly supplied: judge them as scaffolded, or repair without admitting より, which is contrary to the basic register. #48: separate the endpoint of working from a deadline to complete a different action; keep the caveat about work that is not uninterrupted, and 迄. Do not mix this with the lexical recheck.
- **Foundation particle cues.** The verified author input `3c8d66f5` holds the real shared page, the exact English and reader set and article, the ledger scaffold boundary, the old initial review and recheck, and separate base and pending layers. Six tasks: 02 and 04 translation, 09 to 12 evidence, explanation and both rationales. Protect the other 70 page blocks; 05 and 07 stay disjoint from the lexical overlay. No second author was started and no repair is claimed.
- **Existing intentions companion.** The 12 つもり exercises are integrated into the private reader's formal-nouns lesson (six N5 members across three contexts and six ungrouped N2 contrasts). The English and Russian vocabulary inventories for all twelve remain pending.

## Reader mechanics (private offline reader)

- Reader aliases are `q-` plus the first 16 hex characters of the SHA-256 of `ru-offline-practice:<taskID>`.
- Append quantity cards as following siblings, not wrapped; wrapping breaks the choices toggle.
- URL fragments must be answer-neutral. Fragments such as `#hoka-only-…`, `#naka-none-…` and numerical `-supported` or `-unsupported` ids leaked the key. A private-session script fixed them while preserving quiz ids and bookmarks: 64 real keyboard routes and two shelf links now land on focused neutral fragments, and 1,510 other blocks are untouched.
- Do not lead a claim set with the supported statement, and vary the order (#43 and #44: the correct displayed responses are now 1,2 and 2,1 and 1,2).
- Paired or repeated-message items share Japanese messages, so one reveal can supply the next answer, and distinct labels do not imply independent contexts. Use "answer both before reveal" guidance as a separate reader prompt at repeated-message attempts (a deep link skips a page-top note). It is guidance, not a lock. There are 11 exact adjacent message pairs, with 22 neutral reciprocal links, and 22 of 22 routes were checked.
- The source focus chapter is not alphabetical: preserve the frozen order filtered to the present groups. English fixture bodies never count as Russian, the 117 older reused IDs are never new, basic particles are not in the overlay, and the reader search index uses the unchanged 017 filter.

## Scratch branches and local stack checks

Local commits holding unreviewed B241 to B244 and B253-fix and B263 lane drafts were pushed to the Russian repository as backups. They are not merge candidates, no pull request exists, and no CI has run on them (Russian CI triggers on pushes to `main` and `ru-pilot-a` and on pull requests). Their SHAs were re-read with `git ls-remote` just before this record was written.

| Remote ref | SHA | Unique commits |
|---|---|---|
| `scratch/b241-b242-lane-drafts-do-not-merge` | `7e656bc472a0a8be691c67e35f4a52982eeae5dc` | 2 |
| `scratch/b243-b244-lane-drafts-do-not-merge` | `fe1dfd3db9640d26783ce70b4b997d77436bf10d` | 3 |
| `scratch/b253fix-b263-lane-chain-do-not-merge` | `2b1878132bd19a174f2f5c77e9b24ade0970e5a9` | 30 |
| `scratch/b263-lane-draft-sync-do-not-merge` | `290738658fae4e14654821fb243775dfc5ea4d57` | 31 |

- The union is 37 commits. The chain's tip `2b187813` is "B253 fix c972b679 synced onto B263 lane scratch"; the `-sync` branch adds `33724b0a` and `29073865`.
- Of the 749 files in the 30-commit chain compared with `origin/main` (`f6b5413d`), 436 are identical, 133 differ from `main` and 180 are absent from `main`. The 180 are all `words/` drafts of lanes B257 to B263 and are the only unique content; they are unreviewed. My reading that the 133 are superseded drafts of published B242 to B256 cards is unverified.
- Android (code read at `91e1d4b5`) syncs one configured source and branch, and its built-in default is English `main`; scratch branches are not a built-in source. That does not make them harmless: the source parser accepts any valid branch name, and I did not check the source-setup screen.
- English local stack: the coordinator's local English branch `romanko-microsoft-russian-translation-takeover` (HEAD `fb3182f3`) holds 18 signed commits that are on no remote and stays local-only. Its guidance commits reached English `main` as re-signed copies through #66 and #67. Its two content commits (`aa0db991`, `0c93cbc3`) duplicate English `main`'s `6b988091` and `491ecfd9`: `git cherry -v origin/main <branch>` printed `-` for them. They were dropped, because re-applying them conflicts in `manifest.json`. The local branch `b157-candidate-pre-resign` is superseded by re-signed copies and must not be pushed.

## English follow-ups

- [stop-cran/learning-japanese#66](https://github.com/stop-cran/learning-japanese/pull/66) and [#67](https://github.com/stop-cran/learning-japanese/pull/67) are merged. #67 corrected two vocabulary-support examples in `docs/content-format.md`: the 勉強 link now points to the real `勉強する` span (`grammar/basic-particles.json`, lines 3893 to 3901), and the 本 sentence became a conditional authoring rule.
- Optional data follow-up, needing owner authorization and independent review because English grammar data is frozen: the 本 span of `basic-book-object` (`grammar/basic-particles.json`, lines 1280 to 1288) still links `word: 本`, while `words/本.md:15` shows 本を読む. By the rule #67 states, that example reveals the particle tested in `妹が本____読みます。`. This is my reading of the card line against the prompt, not an app run. The Russian card has the same line (`words/本.md:15`). Nothing was changed.
- Okurigana: the Russian instructions now require separating the reading of a whole part from the sounds the kanji itself writes. Russian `words/待ち合わせる.md` does not exist yet (its progress status is `pending`), and its frozen source attributes まち to 待 and あわ to 合. English corrected that earlier, in [`e824da99`](https://github.com/stop-cran/learning-japanese/commit/e824da99c8a19479bfede4e6fbe88b1f21a4180b) (2026-11-24); the card at `c70ee454`, the merge listed in the table above, has the same corrected lines 28 to 30. The batch author must correct the explanation separately from the preserved metadata and report it upstream. Other English cards corrected after `6af98cb7` were not swept.
- English `74cecafa` (N1 hand-off documentation) was not adopted or reviewed in detail. It records that Android's CI clones English `main` at run time; that concerns English N1 content and is not adopted here.
- The instruction comparison is in [the inventory section](../instruction-source-inventory.md#сверка-после-en-pr-66-и-67-2026-11-25); the adopted rules are in [the instructions](../../.github/copilot-instructions.md), [the listening instructions](../../.github/instructions/listening-authoring.instructions.md) and [the methodology](../translation-methodology.md). All the new Russian text is unreviewed.

## Local environment notes

These are machine-specific; the general rules are in the section «Локальные рабочие деревья и публикация» of [the instructions](../../.github/copilot-instructions.md#локальные-рабочие-деревья-и-публикация).

- The English repository's `.git` is under OneDrive, so every `git -C <English worktree>` prints a harmless "failed to delete … Permission denied" line; filter it. `git worktree add` for English takes minutes, and other git commands run during checkout show every file as deleted (a false alarm). Windows long paths are off and the deepest tracked English path is 165 characters, so create English worktrees under a short root (30 characters worked) and use `--no-track`. The deepest Russian path is 156 characters.
- Locate private artifacts by their exact path (`<session-state>\<full session ID>\files\<name>`). A wildcard `Get-ChildItem` across about 1,200 session folders returned nothing even for files that exist.
- The default credential helper pushes with the wrong account and gets 403. Push and write through GitHub as stop-cran, taking the token from `gh auth token --user stop-cran` without printing it. `gh pr merge --merge --match-head-commit <sha>` produced GitHub-verified merge commits.
- After every push, check `gh api repos/<repo>/commits/<sha> --jq .commit.verification`: GitHub rates commits signed with the Microsoft key `unknown_key` and those signed with the stop-cran key `valid`, while locally both show `G`.
- In the English worktree on Windows (`core.autocrlf=true`), regenerating `manifest.json` leaves it modified although its content equals the blob; restore it with `git checkout -- manifest.json`.

## Preserved artifacts

All files below are private, outside every repository, and in the `files` folder of the named session. Sizes are in bytes. Archive and control hashes were recomputed from the saved files when this record was written and matched the values each sub-session reported.

**Coordinator, `d5123981`**

- `private-1574-quantity-contrast-on-017.zip`: 794,970 bytes, SHA-256 `4affe99aa289cb3ccd8d9ef2a9e2654932d0091d9c7c75121634261492f2a71e`.
- `private-1574-quantity-contrast-on-017-check.json` (check report): 11,218 bytes, SHA-256 `7ccbcd1fe545a03246242ffa4d4638f008c0f5e3e37213ddabcc4688fab5d4f3`.
- `private-1574-hoka-on-017.zip` (superseded): 792,213 bytes, SHA-256 `d08f18306e07335e9d35bc5aede59c6799e94a69836442c0f21be539273fe0bf`.
- `private-1574-hoka-on-017-check.json` (check report): 10,911 bytes, SHA-256 `0b1cd6ae4f871625831aa11a2eef9c9e8ba03c927116b65cf03c9fbe600a1770`.
- `restriction-complete-article-blind-001.zip`: 508,141 bytes, SHA-256 `de193009d4e43749fbd1948317a5122f672ab30e1f63793b76e9f68997205ace`.
- `russian-restriction-practice-50.zip`: 22,646 bytes, SHA-256 `14fb08d94b64d0e25c97d1cf991a3e9a446086394556008e6561e8cb7b582ff5`.
- `quantity-combined-repair-author-input-001.zip`: 1,119,793 bytes, SHA-256 `1d83b18fe34eb9d43288c8c27a880dfb2076496e8c33b594035ac879b200a3ba`.
- `quantity-combined-repair-author-input-001.json`: 14,879 bytes, SHA-256 `ee0e7eaaf1bc90392d5053a5aca8eab3f63190daf8a6e09ab7b8b8f679f8317c`.
- `hoka-combined-repair-author-input-001.zip`: 277,437 bytes, SHA-256 `c1431243fcf348da3d766c3b7d9aa58a1a1ecbef89895276de9ebaed1567c02e`.
- `hoka-combined-repair-author-input-001.json`: 8,224 bytes, SHA-256 `43aeee6969f83bb37ba6844bd410484490626d44fe19a1c0e0ca9367e707ecdd`.
- `b258-b270-on-signed-b257-fix-001.json`: 6,125 bytes, SHA-256 `0cc787ac0b073013327d0b381da1da087214f67ec5c145188126973e514b8745`.
- `RESUME-after-restart.md` (living recovery index, hashed as it stood when this record was written): 368,853 bytes, SHA-256 `089678b4fc86465a6c8e53e10b87b2ff1dc28c6a9c4094928629c0833797f20d`.

Also held by the coordinator, names and sizes only (not hashed here): `private-1574-neutral-practice-on-017.zip` (794,535), `private-1574-paired-quantity-on-017.zip` (794,926), `hoka-private-review-001.zip` (478,901), `particle-neighbors-private-review-input-001.zip` (465,257), `particle-neighbors-repaired-live-recheck-001.zip` (656,027), `restriction-002-reader-recheck-001.zip` (523,567), `restriction-wording-author-input-001.zip` (617,045), `quantity-exercise-repair-author-input-001.zip` (1,031,574), `quantity-zutsu-ru-sibling-author-input-001.zip` (148,309), `quantity-private-review-panel-01-001.zip` (300,826), `quantity-private-review-panel-02-001.zip` (310,918), `restriction-private-review-panel-01-001.zip` (295,401), `restriction-private-review-panel-02-001.zip` (298,225), and the per-reviewer `*-initial-exercise-review-001.json` and `*-initial-lexical-review-001.json` files for Hoka, particle neighbors, quantity (first four and last six groups) and restriction (first 26 and last 24 exercises).

**Restriction and inclusion, `263c2174`**

- `restriction-inclusion-manuscript-001.zip`: 1,105,565 bytes, SHA-256 `6b826de1847ab7f5ff4d158a62be386792818f3051fb997e149be4d724473d6b`.
- `restriction-inclusion-manuscript-001.control.json`: 3,514 bytes, SHA-256 `627614cc06ffb78c061b9e6b34bb655f1a1d683150afe182b9cd00cc7ee9d0cd`.
- `restriction-inclusion-manuscript-002.zip` (32 members, root `restriction-inclusion-manuscript-002/`): 1,892,566 bytes, SHA-256 `498cc09d9b392b748126a9f3737f963b556e5566ec2f544a7aa82721fa215221`.
- `restriction-inclusion-manuscript-002.control.json`: 5,307 bytes, SHA-256 `ecd0c2ad4bfa7a4467975d6ab53cf2ebd19f85394dd867aa6373928b8bd0ab46`.

**Particle neighbors, `907edb63`**

- `particle-neighbors-ru-manuscript-001.zip`: 323,596 bytes, SHA-256 `b6e6730ec4ecd7b3428360e877d2c4cea0cb935c1f5b56852689d1b0a4b024c5`.
- `particle-neighbors-ru-manuscript-001-member-control.json`: 6,029 bytes, SHA-256 `fcf1164161fd8d7a52890286a28d47603e97a0d12444972bfc54db29c09d3d34`.
- `particle-neighbors-ru-manuscript-001-erratum-001.json`: 3,053 bytes, SHA-256 `59401819c3533d61483caf814095516f580d1615685d698e367b09dc4eeac4fd`.
- `particle-neighbors-ru-manuscript-002.zip` (57 members, root `particle-neighbors-ru-manuscript-002/`): 1,029,388 bytes, SHA-256 `779dc1f89c62e66993db4dea5a42fc0beadb5e4494d4e06b55a8066eeb03495d`.
- `particle-neighbors-ru-manuscript-002-member-control.json`: 10,881 bytes, SHA-256 `a4482b3366669e7dd9906bfd6ea4986458d427b48d39eefaa522d99c6165a1ce`.

**Quantity, `b5028318`**

- `quantity-scope-manuscript-001.zip` (root `quantity-scope-manuscript-001/`): 764,311 bytes, SHA-256 `902d962b5c45b8e34d0d06f8bbd04473e2334b3688fd18cce5ecdf95f1909a1b`.
- `quantity-scope-manuscript-001.control.json`: 2,746 bytes, SHA-256 `ab77be78712934b4d6c76fe9ceb63385f4f80fe347730319ffd0986a5f2edb74`.

**Hoka exclusion, `f28a2f6c`**

- `hoka-exclusion-ru-author-002.zip` (root `hoka-exclusion-ru-author-002/`): 1,315,700 bytes, SHA-256 `97811141a8fc22f6bf070c3ee7b2de5fa85635c2e582e961ecee5ccd66d3229e`.
- `hoka-exclusion-ru-author-002.control.json`: 6,868 bytes, SHA-256 `30e6ca2e7c3ae569233dcdb53f8847160c5d4d603617909682c0e2b2acdf07b3`.
- `hoka-exclusion-ru-author-002.seal.json`: 1,726 bytes, SHA-256 `801ff28c03b5912bc2f78d6713f2195dda3f7513d12f21f35d823ffcc837e986`.
- `hoka-exclusion-ru-author-001.zip` (superseded by 002): 1,313,566 bytes, SHA-256 `bd28f24c5df41bea3e923c1bfec062cb944ec4c90b917c3ff671dc3da65760a9`.

**`ずつ` author, `10354058`**

- `quantity-zutsu-partial-checkpoint-001.json`: 18,493 bytes, SHA-256 `63c931f5de8cdc07664a0a4292d0fd17f2d24e15210903af0c3119489ffbfefd`.

**B257 records owner, `e7df86ac`**

- `b257-recovery-note.md`: 6,697 bytes, SHA-256 `06e1e00668f322fd63bf91167563bf645a586e69fd7df1056032b858020141a6`.
- `b257-r003-exec003-design.md`: 9,057 bytes, SHA-256 `3c98378b45053dc12e33caee9fe25eb4ab2cfb7769dde617419aab2553bc097a`.

Key member hashes quoted from the sub-session hand-offs:

- Restriction 002: raw-members `d0441c1528ab962f22c0f7f5d5c8fd8ed65b2f70e89fe3ec94d3520e8d65143d`; article `e0d5787a3712b84b53335218673b2ff35c3f24d0199c473b4fe0f5c1ad6078b4` (001: `4f846c2f…`); grammar `192a132952817089647e4c3b0634717f00190cf991b5e6e995a9de9c67d1c570` (001: `b34a6632…`); `audit/successor-002-deltas.json` `a0764f9eec8e7722f1581d33af6d8c7e40128a61b2ac3d39dc46f9ad9dbe61fd`; `AUTHOR-NOTES.md` `ba7c003b335dec06c5d931c0dce389f914eaaffcc8f142c5a6e2627b2dd07a69`.
- Particle neighbors 002: `drafts/grammar/particle-neighbors.json` `17736b479da86448103036f468bc3a18597b2d6a81cdb9a442661924d731225c`; `evidence/vocabulary-proposals.json` `9dc88cd003112f10d8abb3927449cd913b31de69532417adde9e147f55637a3b`; `evidence/pending-context-inventory.json` `bfe025d75dea3c5a7b37561baae5bd0228259ba590cb7d0ff607baf6cbd7b822`; `pending/rows.json` `5ab9231ad9ce31d904e557586d5bef4a3853c1c1f97fdaed384fee6e0618efe1`; reused article `inputs/ru/articles/koto-wake-and-formal-nouns.md` `5d5df589bf4f0e3963f91e06b6e8928e34beb62604970bbded029d280f8a4302`.
- Quantity 001: raw-members `3c8041aaa1d9b921ffa6ab2bf0941aceed334044b4eda76c7d0275a761a91136`; `manuscript/articles/quantity-ranges-and-frequency.md` `18d04d324075608438c246632743ce585f81d3c5f0cc884d5383b5e124bbc103`; `manuscript/grammar/quantity-scope.json` `f1553a93c80c4c20bf9503009839e07bcccbb7024eb43d1e5286729e7382d6b7`.
- Hoka 002: `grammar/formal-nouns-hoka-exclusion.json` `1bf8d16811738699b4843786755b40e96dd90c70220fa891e9e707655f21062a`.

These are saved-file hashes, not claims about the content's correctness or about network-message bytes. The member hashes are quoted from the sub-session hand-offs. This receipt is author-maintained and is not an independent review of itself.

## Not done and unverified

- No device, Android, media, voice, drawing or audio acceptance exists for anything here. No independent review exists for any sealed manuscript, for the private reader pages, or for the new Russian instruction text.
- No public release of the private offline reader, no library 018, no B258 and no paid media.
- B257: the execution-003 record, source acceptance, and all ledger, progress and tracking updates.
- `validate.py` was not re-run with the reused particle-neighbors article materialized; the single `訳` error comes from the author's fixture.
- Not checked: the Android source-setup screen, the body of `ordinarySourceIsCurrent`, and what the gated state shows the user.
- English changes after `6af98cb7` were not swept beyond the instruction files, `docs/content-format.md` and the cards named above. English `74cecafa` was not reviewed in detail.
- My reading of the 133 differing scratch files as superseded drafts is unverified.

**Handoff:** The coordinator session `d5123981` wrote this record on 2026-11-25 at the project owner's request to save all ongoing work. Each unit stays with the owner listed above. The single learner-author slot is held by the `ずつ` author, and no reviewer is running. Acceptance of every unit, any reader release and any change to published learner content stay separate steps that need independent review and the project owner's authorization. Apart from the pushes listed under "What this handoff pushed", no repository, runtime, manifest, progress, release, Android or media action was taken.
