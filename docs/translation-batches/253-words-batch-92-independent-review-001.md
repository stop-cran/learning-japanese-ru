# Batch 253 — independent review 001

## Snapshot and scope

| Role | Pinned revision |
|---|---|
| Frozen EN source | `6af98cb717755690a9ca793e5454a96ebd7a8f9f` |
| Published RU baseline | `6efe3ec4f81c0fb39b6478cbfd15d46199db1fc7` (B252, PR #136) |
| Candidate parent | `7126ab8be4bf9ea8358b57a02e673fef007278f4`, the B252 publication-verification record; no learner-content change |
| Local-only authoring snapshot | `c9212638ef7ee4fe60adcd1a677f5829e888b032`, tree `dc7399d5c77399acb4e8c5f268a835b7d5139962`, parent `e21a513f272f4a0ba4cceb74279063c48a51ec5d` (B252 lane scratch) |
| Signed blind candidate | `bbe4e485115525a1f4bd661960486449dbe4570b`, tree `a46d590fde1002c23b72346587efb6c17d0ea7c7`; original content branch `full-ru-253-words-92` |

Word batch 92 is chunk 45 of the 72-batch general word queue computed after B207 from 2,157 remaining EN words: 807 remained after B252; 777 remain after this batch. The requested and closed sets are the same 30 words:

演劇 漁師 滝 溶岩 混合 溶かす 溶く 溶け込む 満点 売り切れる 売り切れ 満員 湿る 水蒸気 湯気 湧く 測量 測定 温泉 温帯 温室 渇く クリーニング 清掃 混ぜる 付き合う 混じる 混ざる 深夜 深まる.

`closureAdded` records `{"溶く":"溶かす"}`: traversal reached 溶く through 溶かす, but 溶く was already requested. This is not a thirty-first word or a new guard. `deferredGuards` is empty. The intake has 39 payloads and no held path. Relative to its parent the candidate changes 41 paths: 30 new cards, nine existing cards, `manifest.json` and the intake. The 39 content blobs match the local scratch blobs. The candidate script checked the scratch parent, the nine navigation bases against the published content, the absence of all 30 new paths, the copied files, the changed path set and the ledger new-path set. It regenerated the manifest on the publication base. No three-way merge, held link or scratch ancestry was imported into the candidate.

### Before the blind reviews

The coordinator recorded reading the 30 complete lane cards against frozen EN and the nine navigation edits. It changed one sentence in 清掃 from «вывоз мусора; широкую службу очистки или нет — определяет контекст.» to «вывоз мусора; идёт ли речь о более широкой службе очистки, определяет контекст.» The latter is also the final wording. The coordinator accepted the author's change of 混ぜる's last title glosses to avoid near-duplication with 統一; it did not retitle the cards in its own text edit.

The author's EN-title table is a summary, not a verbatim source for two entries: it gives 演劇 as `theater; drama` and 溶かす as `melt; dissolve`; the pinned EN `title` fields are `theatre; drama` and `melt or dissolve something` respectively. This is a records distinction, not a new finding against the RU cards.

The guard criterion was “keep where titles share a lexeme or are near-synonyms with overlapping sense; drop antonyms, topical-only pairs, shared-component pairs, pairs the titles already disambiguate, and redundant reciprocals (the app applies exclusions in both directions).” Six draft entries were dropped: 溶け込む→溶かす (duplicate reciprocal), 溶け込む→慣れる (topical), 湿る→濡らす (transitivity contrast), 水蒸気→蒸発 (substance/process), 清掃→雑巾 (object/action) and 混ぜる→加える (adding/mixing). Fourteen remained; see the actual lists below.

The coordinator recorded checking the art/building uses of «театр» in Russian Wiktionary, keeping the hiragana on-reading notation for 測定/測量, the 湯気 external-heading remark and plain mentions where EN used no link. Its statement “Russian lexis judged natural, not dictionary-checked: «отсыревать», «сникать», «бить ключом», «топографическая съёмка»” describes this lane adjudication, not the later correctness review. The initial author report's unsuccessful dictionary check was not itself confirmation. Fix 1 subsequently removed the 湯気 heading sentence, retitled 測量 and changed the kanji/劇 gloss; it did not remove «бить ключом».

Lane checks are not candidate or fix checks. The adjudication records “manifest 5,709 files (version ff8ca0411d861cff); validate 0 errors; unittest OK; budget OK (5,726 entries; localZipBytes 8,287,991)” and 39 paths with no LOST/EXTRA, nine navigation links and zero unguarded exact overlaps. The signed candidate manifest has 5,709 **entries** (5,704 `files`, three images, two scenes), version `5f4fb4d0fef20eaa`. The candidate title screen has 325 lines: 32 guarded `OK`, 293 `!!`, zero exact segments. Its `!!` lines are stem leads, not findings. The initial and final lane screens each have 327 lines (32/295), identical to each other and also without exact segments. The lane-only lines are 溶け込む~物騒 and 湧く~発想; 満員~一通り displays a different neighbour title. These two lane outputs are not evidence of the committed fix.

### Navigation and source coverage

Each existing RU file gained one link, where frozen EN links the same word. At the candidate the entire change to each line is wrapping the word; old glosses are not title changes.

| Existing file | RU line | EN line | Restored href |
|---|---:|---:|---|
| `kanji/乾.md` | 52 | 50 | `../words/渇く.md` |
| `kanji/劇.md` | 36 | 36 | `../words/演劇.md` |
| `kanji/帯.md` | 37 | 37 | `../words/温帯.md` |
| `words/乾く.md` | 29 | 24 | `渇く.md` |
| `words/泉.md` | 25 | 25 | `温泉.md` |
| `words/濡らす.md` | 39 | 41 | `湿る.md` |
| `words/熱帯.md` | 28 | 28 | `温帯.md` |
| `words/芝居.md` | 37 | 35 | `演劇.md` |
| `words/零点.md` | 37 | 38 | `満点.md` |

`words/乾く.md:43` retains unlinked 喉が渇く as at EN :32; `kanji/乾.md:52` has a separate 喉が乾く. 熱帯 retains its 暑い link and plain 寒帯. The later gloss edit on `kanji/劇.md:36` did not add a tenth link. `words/芝居.md:37` keeps its contextual «театр, драматическое искусство», not a copy of the new title. No RU-only href or lost link to an available RU target in the 39 paths at either content snapshot.

In the new cards 23 EN `.md` href occurrences to 14 distinct targets are left plain because the RU **target path** is absent. These are the 13 kanji cards 漁 (漁師), 溶 (溶岩, 溶かす, 溶く, 溶け込む), 岩 (溶岩), 混 (混合, 混ぜる, 混じる, 混ざる), 湿 (湿る), 蒸 (水蒸気), 湯 (湯気), 測 (測量, 測定), 量 (測量), 温 (温泉, 温帯, 温室), 泉 (温泉), 清 and 掃 (清掃), and the word card 噴火 (溶岩). A separate href check of the 30 EN originals finds **no `../articles/` link**. Comparing only basenames hides the missing kanji hrefs for 岩 and 泉: the distinct word links `words/岩.md` and `words/泉.md` are present and kept. No word-card link substitutes for a missing kanji-card link.

Sixteen written characters have no RU kanji card: 岩 掃 泉 混 清 渇 温 測 湧 湯 湿 溶 滝 漁 蒸 量. Of these, 渇, 湧 and 滝 have no EN kanji card or EN kanji href in the new cards either; they are not three more missing EN links. The initial consistency report groups them with missing targets. This qualification preserves its reported verdict without repeating the grouping as an href count.

All 19 EN href occurrences between new word cards are retained: 溶かす→溶く; 溶く→溶かす, 混合; 溶け込む→混合; 売り切れる→売り切れ; 売り切れ→売り切れる; 湯気→水蒸気; 測量→測定; 測定→測量; 混ぜる→混ざる, 混じる, 混合, 溶く; 混じる→混ざる, 混ぜる, 付き合う; 混ざる→混じる, 混ぜる, 混合. This hyperlink set is **not** the exclusion graph.

### Review process and evidence

All initial briefs concerned the same signed candidate. Reviews ran serially, without a fix between them: correctness, consistency/quiz safety, then comprehensibility. Each finished normally. The briefs prohibited author/adjudication material, saved title screens, other reviews and scratch lanes; consistency alone could inspect the intake for path parity and learner content. The three full initial reports are separate from the later rechecks:

| Facet | Runtime model / original reviewer | Initial report |
|---|---|---|
| Correctness and scoped coverage | `gpt-6.1-sol` · `f8dfbe0c-bd07-49ff-b12d-6bb92e7a61e5` | `253-words-batch-92-review-correctness-001.md` |
| Consistency and quiz safety | `claude-sonnet-5.5` · `99dd73a9-bf30-4991-870c-6ced97d29aca` | `253-words-batch-92-review-consistency-001.md` |
| Comprehensibility and scoped coverage | `grok-4.7` · `20c8cfac-fabd-488d-9861-f1b1f56f9bfd` | `253-words-batch-92-review-comprehensibility-001.md` |

Runtime model identities and completion/order come from the coordinator's records (`read_agent` for model identities), not from a reviewer's ability to authenticate its serving model. Initial report write times were 18:31:40Z, 18:39:56Z and 18:54:57Z on 2026-11-23; timestamps alone would not establish serial completion. Each reported the assigned HEAD and a clean tracked tree. Consistency reports that `validate.py` created an untracked bytecode cache which it removed; the other reviewers did not claim to have run that check.

## Initial verdicts and findings

### Correctness

“**Correctness: NEEDS FIX** — C1. No further actionable correctness defect established in the other 29 cards.” “**Scoped coverage: NEEDS FIX** — C2. No further actionable teaching-content omission established in the other 29 cards.” The 29-card qualification applies **separately** to each facet; C1 and C2 concern different cards. Russian comprehensibility and exhaustive quiz suitability were not certified.

The reviewer reports full reads of all 30 RU and frozen EN originals, including forms, examples, notes, comparisons and footers; its report gives RU/EN ranges for each card. It inspected the nine navigation **changes**, relevant linked titles/passages and a manifest excerpt, not the entire baseline kanji cards as new content. It reports checking all 30 vocabulary labels on Jisho, including the additional N1 listing for 付き合う; comparing Japanese example and kana strings, footer URLs and target paths; reading JMdict XML and KANJIDIC2, selected Digital Daijisen entries, and actual Russian dictionary entries. It distinguished historical captures from live evidence, used primary KANJIDIC2 after bulk kanjiapi failures, and did not reconstruct historical sense numbering for 付き合う. It did not run a generator, validator, app/device test or full quiz-pool audit.

| Finding | Candidate evidence and requested change | Disposition |
|---|---|---|
| C1, Medium, correctness; high confidence | `湧く:50` gives 沸く the transitive «нагревать». JMdict 1606680 sense 1 and Daijisen describe intransitive heating/boiling. | ACCEPT. Final `湧く:50` reads «Значения «кипеть» и «нагреваться» относятся к 沸く, даже если в каком-то списке». |
| C2, Low, scoped coverage/example accuracy; high confidence | `深夜:21` renders a **late**-night call only as «ночной». EN :21, JMdict 1362810 and Daijisen support the narrower time. | ACCEPT. Final translation «Меня разбудил телефонный звонок глубокой ночью.»; :23 now permits «ночной» or «глубокой ночью» in context. |
| Optional, aspect | `湧く:4,12`: perfective «хлынуть» is possible, but unlike its neighbours. | ACCEPT: «хлестать наружу». |
| Optional, terminology | `混ぜる:38`: «частицей -ся» risks confusion with Japanese particles. | ACCEPT: «постфиксом -ся». The transitivity rule remains. |

The deleted-at-authoring absence-of-kanji bookkeeping in 湧く was not a Japanese teaching-content omission. This does not imply acceptance of its separate 沸く voice error.

### Consistency and quiz safety

“Consistency: **PASS** with minor, non-blocking notes (2 Low, 2 Info).” “Quiz safety: **PASS, with conservative guards noted.** No EN guard was dropped. No guard is a self-reference or duplicate. No unguarded pair that I found is a real confusion risk. Necessity of the RU-only guards is **UNVERIFIED**, not CLEAN.”

The reviewer reports reading all 30 RU cards and all nine navigation diffs, the brief and quiz rules. Against frozen EN it mechanically compared metadata, links, footer URLs and targets; against the manifest it checked hashes for the 39 paths (not a rebuild). It inspected the intake only for path parity/learner content. `validate.py` printed `0 error(s)`. Its EN line-count comparisons on eight cards went only to footer-URL level; it did not enumerate every adaptation. It did not perform a linguistic correctness review or open JMdict or a live dictionary.

| Finding | Candidate evidence and impact | Disposition |
|---|---|---|
| F1 Low, medium confidence | 溶け込む title and sugar example add «полностью» to EN “dissolve into; blend in”. | ACCEPT, merged with comprehension C6. |
| F2 Low, low confidence | 温帯→適度: climate zone vs degree; weak basis despite «умеренный». The reviewer allowed keeping it or removing it if the pool matters. | DECLINE removal; keep the direct guard for the overlap introduced in Russian. Necessity not established. |
| F3 Info | 水蒸気: «горячий пар» risks blurring the visible 湯気 distinction; no missing guard. | Merged with comprehension C1. |
| F4 Info | 湧く omits the missing-kanji bookkeeping; 清掃's «уборка территории» is narrower than its body. | No action on 湧く; 清掃 merged with comprehension C10. |

The optional in-batch and external stem/topical pairs listed in the original report were not submitted as required additions. The reviewer distinguished topical relations (e.g. 水蒸気–温泉, 満点–満員, 温帯–温室) from defensible alternatives. No claim about every generated choice or empirical necessity follows.

### Comprehensibility and scoped coverage

“Verdicts: comprehensibility NEEDS FIX; scoped coverage NEEDS FIX.” The reviewer reports reading all 30 new cards against EN and checking comparison titles, running link parity on the **30 new cards** and using title-screen stems as leads. It did **not** review the nine navigation changes, manifest or intake. It did not re-open the rare-spelling tags beyond the cited material and did not certify correctness.

Its both-facets-clean group was 漁師, 滝, 溶岩, 混合, 溶かす, 溶く, 満点, 売り切れ, 満員, 測定, 温泉, 温帯, 温室, 渇く, 混ぜる, 付き合う, 深夜. Comprehensibility-only findings concerned 溶け込む, 売り切れる, 湿る, 湯気, 湧く, 混じる, 清掃, 混ざる. Both assigned facets were implicated for 演劇, 水蒸気, 測量, クリーニング, 深まる. For example, the comprehensibility verdict on 深夜 does not override the correctness reviewer's separate C2 coverage finding.

| ID; severity | Reported problem | Coordinator disposition at fix 1 |
|---|---|---|
| C1; high | 水蒸気 title teaches the visible hot cloud distinguished from gas at :31. | ACCEPT: «водяной пар». |
| C2; medium | 演劇 label names the art twice but not the performance shown in the examples. | ACCEPT title only: «театральное искусство; драматическая постановка»; sync `kanji/劇.md:36`. Keep natural «спектакль» examples and existing 芝居/公演 guards. |
| C3; medium | 測量 title too specialised/land-only; :42 warns against the English “survey” sense. | ACCEPT modified: «съёмка местности; измерение» follows EN order; delete :42, keep the measurement and 調査 distinctions. |
| C4; medium | クリーニング title «услуги прачечной» vs dry-cleaning examples, Latin `cleaning` in prose. | DECLINE: laundry service is an EN gloss, :24 rules out dry-cleaning-only, and `cleaning` is the glossed etymon. |
| C5; medium | 深まる title limits intensification to feelings/relationships; question about the autumn translation. | ACCEPT title only: «углубляться; усиливаться»; keep «Осень всё больше вступает в свои права» as idiomatic. |
| C6; medium | 溶け込む's long label and sugar example overstate completeness. | ACCEPT: retain the physical/social contrast, drop «полностью» in both. |
| C7; medium | 売り切れる examples make the goods objects of indefinite-personal Russian verbs. | ACCEPT modified: «был распродан» / «пока они не разошлись», keeping goods as subjects. |
| C8; medium | 湧く: idiom/aspect, idea example overlapping 浮かぶ, and a meta warning assigning 沸く the wrong voice. | PARTIAL: keep literal «бить ключом» and the list hedge; change «хлынуть», the idea example and the 沸く gloss. Do not equate this with full resolution. |
| C9; medium | 混じる «попадались» does not show mixing. | ACCEPT modified: «К песку примешались мелкие камешки.» |
| C10; low | 清掃 label excludes indoor cleanup. | ACCEPT modified: «очистка; уборка (помещений, улиц)»; «очистка» remains first, and 掃除 is guarded. |
| C11; low | 混ざる restricts joining people to a game. | ACCEPT modified: «присоединяться (к другим)»; 加わる is guarded. |
| C12; low | 湯気:44 references an external ゆけ heading the learner cannot see. | ACCEPT deletion, not a replacement reading rule. |
| C13; low | 湿る:43 names an unseen source list. | ACCEPT modified: «значение 2 дополняет физическое значение «сырость».» |

Confidence was high except C12 (medium). Optional observations on the profession/hobby distinction for 漁師, stiff 滝 wording, 混ぜる, 深夜, 温泉, 猟師's reading, missing-target links and egg-beating 溶く were not additional required edits. The original report records the affected comparisons and JMdict IDs, rather than a second new dictionary audit by these records.

## Exclusion classification

At the candidate **and** fix, all 150 direct EN entries are retained as ordered prefixes across 26 EN lists. EN has none on 漁師, 滝, 温帯 or 温室. There are 25 internal EN entries: 溶かす→溶く; 溶く→溶かす, 混合; 溶け込む→溶く, 混合; 売り切れ→売り切れる; 満員→売り切れ, 売り切れる; 湯気→水蒸気; 測定→測量; 清掃→クリーニング; 混ぜる→混合, 溶く, 溶け込む; 混じる→混ぜる, 混合, 付き合う, 溶く, 溶け込む; 混ざる→混じる, 混ぜる, 混合, 付き合う, 溶く, 溶け込む. The other 125 EN entries target existing RU cards.

| Card | Appended RU entries, in order | Consistency classification |
|---|---|---|
| 演劇 | 公演, 芸術, 芸能 | conservative: performance/art overlaps |
| 溶かす | 溶け込む | conservative: dissolution |
| 溶け込む | 加わる | conservative: joining |
| 売り切れる | 特売 | conservative: «распрод…» |
| 売り切れ | 特売 | conservative: same lexical family |
| 満員 | あふれる, 大勢 | conservative: crowd/capacity |
| 湯気 | もくもく | conservative: billows |
| 温帯 | 適度 | conservative; weakest basis, F2 |
| 付き合う | 会う, お目に掛かる | conservative: meeting |
| 深夜 | 徹夜 | conservative: night |

The additions have arities **3,1,1,1,1,2,1,1,2,1 = 14** on ten cards: 164 RU entries in all. The restart handoff's “15” was a miscount; the historical coordinator heading “Kept (14)”, the consistency reports and the actual Git lists agree. No fifteenth pair and no fix-time exclusion change. The reviewer found none unjustified but did **not** verify necessity. Android's documented exclusion-aware rule applies each declaration in both directions, not transitively (frozen EN `docs/content-format.md:162–165`); that contract is not a live app test.

The three original reviewers rechecked one subsequent fix. See `253-words-batch-92-recheck-001.md` for exact changes, dispositions and final bounded verdicts. This record covers source review only, not release, device, media, ordinary activation, learner outcomes or all quiz fallback paths.
