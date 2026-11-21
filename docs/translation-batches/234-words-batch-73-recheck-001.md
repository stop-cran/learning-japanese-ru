# Batch 234 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `1e7c04d20795a3f0efac996855d00f233ebe566b` | `02023ebe35e7f52010e453f8711aa47bf99c56ae` | Initial review snapshot: the signed candidate, on `origin/full-ru-234-words-73`. |
| `b8501046350dd38a7d4f7f4a31b1765e5b496b02` | `9a065539eb0efaa9d37ac764ce77e3957613caf4` | Fix 1 (final candidate). It covers correctness F1 and F2 and comprehensibility C1 and C3–C8 (F1 with C7 and C3 with adapted wording; C4 and C5 partially adopted). It adds and removes no exclusion and no link. Signed; on `origin/full-ru-234-words-73`. |

Fix 1 changed seven word files and regenerated `manifest.json` (`contentVersion` `3c63f4a9bf69b5bc`, 5,139 entries:
5,134 `files` + 3 images + 2 scenes; the candidate had `b06ec272fee34a3d`). The intake was not refreshed; it still records
the candidate's 35 payload hashes.
- `近々` (lines 4, 12 and 19; correctness F1 with comprehensibility C7, adapted wording): title and H1 «в ближайшем
  будущем; совсем близко (о расстоянии)» instead of «в ближайшие дни (о предстоящем); совсем близко (о расстоянии)», and
  the moving example «В ближайшее время я собираюсь переехать.» instead of «В ближайшие дни я собираюсь переехать.» The
  reviewers' «в ближайшее время» (F1) and «скоро» (C7) were not used in the title, because they are exact title segments of
  そのうち and もうすぐ, both EN-guarded; line 16 already says «скоро, в ближайшее время», so C7's added sentence was not needed.
- `補う` (line 42; correctness F2): «Само по себе 補う не означает выплату возмещения по закону:» instead of «補う не означает
  выплату возмещения по закону:», keeping EN's "does not automatically mean paying legal damages".
- `退く` (line 21; comprehensibility C1): the kana reading `（すみません、そこをどいていただけますか。）` added after the Japanese
  sentence, as in EN.
- `農薬` (lines 20–21; comprehensibility C3, adapted wording): «— Я выращиваю овощи без сельскохозяйственных химических
  средств.» instead of «— Я выращиваю овощи без пестицидов.», and «— Используйте этот препарат строго в установленном
  количестве.» instead of «— Используйте этот пестицид строго в установленном количестве.» «агрохимикаты» was avoided,
  because in Russian regulatory usage it denotes fertilizers and soil amendments.
- `農薬` (line 42; comprehensibility C4, partially adopted): «Не сводите 農薬 к «пестицидам» в узком смысле: регуляторы
  роста тоже входят в эту категорию.» instead of «В названии карточки к «пестицидам» добавлены регуляторы роста, чтобы они
  не выпали из категории незаметно.» The sentence was reworded, not deleted, because EN :49–50 has the equivalent note.
- `催促` (lines 4 and 12; comprehensibility C5, partially adopted): title and H1 «напоминание (об ответе, оплате);
  побуждение поторопиться (с ответом)» instead of «…; торопить (с ответом)». The proposed body sentence with a 急ぐ link was
  not added: it would add an RU-only link, and 催促→急ぐ is already guarded.
- `接する` (lines 4, 12 and 16; comprehensibility C6): title and H1 «соприкасаться; граничить (с чем-либо); обходиться (с
  людьми)» instead of «…; вести себя (с людьми)», and line 16 «…или «обходиться с людьми, иметь с ними дело».» instead of
  «…или «вести себя с людьми, обходиться с ними».»
- `交通機関` (lines 4 and 12; comprehensibility C8): title and H1 «транспорт (поезда, автобусы и т. п.); транспортная
  система» instead of «…; средства сообщения».

The comprehensibility reviewer's C2 (the Latin `wago` label in さようなら:29 and 船便:26) was not adopted, nor were its
wording «скоро (в ближайшее время)» and added day-count sentence for 近々, its longer second 農薬 translation, its deletion of
the 農薬:42 sentence or its added 急ぐ sentence in 催促; its optional notes (お先に's speech-act title, さようなら «прощайте»,
送別 «прощальный», 宴会 «застолье», 農村 «земледельческая деревня», 応対's long title, 述語's commentary, 追い掛ける «пускаться в
погоню», 近寄る «этой машине» and «Ко мне подошла кошка», 補う «окуригана» and the unlinked absent targets) led to no
action. The consistency reviewer's optional notes led to no action. The dispositions gave the reasons (see the
reconciliation table).

The coordinator's post-fix title screen of the four changed titles (`b234-postfix-screen.txt`) found one exact shared
segment: 接する's «обходиться (с людьми)» with 済ませる «заканчивать (дело); обходиться (чем-л.)», deliberately left
unguarded because the displayed labels carry different complements and neither word has the other's sense. Everything else
is stem-only: 近々's «будущ-» meets 今に «в скором будущем» (guarded), 先, 将来 and 未来, and its «ближа-» meets そのうち «в
ближайшее время; из них (о части названного)» (guarded); 催促 has no exact segment and no stem lead outside parentheses (急ぐ
is guarded anyway); 交通機関's «систе-» meets 制度 «учреждённая система (в обществе, организации)», 機関 (guarded) and 級, and
its «транс-» leads were already present through «транспорт». Fix 1 adds no link and removes none, and changes no exclusion.
The one RU-only link at the candidate, 追い掛ける:40 → 追い付く, is unchanged. `tools/validate.py` reported 0 errors and the unit
tests (124) passed before the fix commit.

Net change from the candidate:
- titles and H1s of 近々, 催促, 接する and 交通機関;
- example translations in 近々 and 農薬;
- prose in 補う (line 42), 接する (line 16) and 農薬 (line 42);
- the kana reading line in 退く;
- no exclusion or link change.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`1e7c04d..b850104 -- words` is seven word files, 15 lines added and 15 removed; with `manifest.json` the commit changes
8 files, 23 lines added and 23 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs; the
initial reports state that the model is not verifiable from inside the session.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. No recheck raised a new finding, so there was no fix 2.

Each reviewer appended its recheck to its own report file. Each brief included the full words diff `1e7c04d..b850104`, the
coordinator's evidence and rationale for the edits, the declined items and that reviewer's original verdicts with their
dispositions. The correctness section records that it read the complete recheck instructions, rationale and supplied diff,
verified the live diff and read all seven changed cards in full against frozen EN; the consistency section records the
reviewed scope as the actual diff (7 word cards + manifest) checked against the full RU word pool; the comprehensibility
section records that it re-read the changed passages and reconciles each of its findings. The recheck sections do not
reproduce the briefs, so this record does not claim their further contents.

All three rechecks state that no generator was run. The correctness and consistency reviewers each ran
`tools/validate.py` (0 errors each); the comprehensibility reviewer did not re-run the validator. Each recheck section
records snapshot `b850104` with a clean tree; the consistency reviewer records that it removed an untracked
`tools/__pycache__` created by its own validate run. After the three rechecks the coordinator confirmed, read-only, that
the RU checkout is on `full-ru-234-words-73` at HEAD `b8501046350dd38a7d4f7f4a31b1765e5b496b02` (`git rev-parse HEAD`) and
that `git status --porcelain --ignored` prints nothing, so no tracked, untracked or ignored file was left by the rechecks.

### Round 1 (`b850104`)

| Facet | Scope and result |
|---|---|
| Correctness | Snapshot `b850104`, parent `1e7c04d`, HEAD verified before and after, clean working tree and index. Read the complete recheck instructions, rationale and supplied diff, verified the live diff and read all seven changed RU cards in full against their frozen EN originals. F1 is **resolved**: 近々:4,12,19 now preserves near-future timing without a days restriction, and the temporal/spatial coverage and reading restrictions remain (JMdict 1578110; previously inspected Daijisen entries). F2 is **resolved**: 補う:42 adds «Само по себе», restoring the non-implication qualification, and the comparison at :43 remains appropriate (JMdict 1514460/1514650). No regression: 交通機関's «транспортная система» is at least as accurate and matches EN's transport-system sense (JMdict 1272320), with the wider sense still at :38–39; 催促's nominal urging gloss matches EN and JMdict 1292200; 接する's «обходиться … иметь с ними дело» is at least as accurate for treating/dealing with people (JMdict 1385350, sense 2); 農薬:20–21 match EN's agricultural-chemical wording, and :42 keeps the growth-regulator inclusion with «в узком смысле» avoiding a universal claim (JMdict 1470780; the former examples were also defensible under the statutory definition); 退く:21's kana transcription matches EN exactly. Validator 0 errors; the coordinator-reported unit tests were not rerun. Correctness **CLEAN** and scoped coverage **CLEAN** for the revised batch within the original scope; no new actionable regression or unresolved disagreement. |
| Consistency | Snapshot `b850104`, parent `1e7c04d`, clean worktree (it removed an untracked `tools/__pycache__` created by its validate run). Reviewed the actual diff `1e7c04d..b850104` (7 word cards + manifest) against the full RU word pool. Validator 0 errors; all 5,134 manifest file hashes match the tree (CRLF-normalised sha256); the diff touches only the 7 stated cards and `manifest.json`. Title equals H1 for 交通機関, 催促, 接する and 近々, and no other card carries the new title segments. The diff adds or removes no link and orphans no reference; the exclusions are unchanged, including the 19 RU additions. New titles: 近々 «в ближайшем будущем», 催促 «побуждение поторопиться» and 交通機関 «транспортная система» have no exact segment elsewhere (今に, 制度, 機関 and 級 are stem leads only; 急ぐ is already guarded). 接する «обходиться (с людьми)» shares an exact segment word with 済ませる «заканчивать (дело); обходиться (чем-л.)», but the complements differ and neither word has the other's sense; the reviewer judged it not a defensible-answer ambiguity, so no guard is required, and recorded a guard 接する→済ませる as a **new optional** (conservative, necessity UNVERIFIED). The other rewrites (補う, 退く, 農薬, the 近々 example) are wording only; no regression. The earlier optional notes stay optional. Consistency, quiz safety and scoped integration are **CLEAN**, with no finding. |
| Comprehensibility | Snapshot `b850104`, parent `1e7c04d`, clean status; re-read the changed passages in the working tree, not all 30 cards. C1 is **resolved**: 退く:21 has the kana reading. C2 is **withdrawn**: EN さようなら and 船便 have the same sentences, including the format clause, and RU glosses wago at once as «исконное слово», as do published 家賃, 年月 and 方々; a corpus-wide label change is outside this batch. C3 is **resolved**: «без сельскохозяйственных химических средств» restores the EN scope and «этот препарат» matches the card's «другие препараты»; the reviewer does not maintain its longer second-example wording, and «агрохимикаты» would collide with fertilizers. C4 is **resolved**: the card-title remark is gone, the new sentence is learner-facing, and deletion is not required. C5 is **resolved**: the title and heading are nominal; the reviewer does not maintain the 急ぐ sentence (the collision is gone, 急ぐ is excluded, and a new link would exceed EN parity). C6 is **resolved**: no leftover «вести себя»; the 済ませる «обходиться» overlap is not a card-text defect, because the complements differ, and quiz display is outside these facets. C7 is **resolved**: the reviewer does not maintain «скоро» or the extra day-count sentence; «в ближайшем будущем» matches EN and avoids the そのうち and もうすぐ segments. C8 is **resolved**: «транспортная система», with the wider связь sense still qualified in the body. No regression in 補う. The optional notes stay optional. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 近々's title, H1 and moving example «в ближайшие дни» narrow "in the near future" (minor) | **Resolved** (adapted wording, merged with comprehensibility C7) | `近々.md:4,12,19`; JMdict 1578110 sense 1 "soon; before long; shortly; in the near future"; Digital Daijisen ちかぢか ごく近いうちに; EN "in the near future". |
| Correctness F2: 補う:42 drops EN's "not automatically" qualification (minor, correctness/scoped coverage) | **Resolved** | `補う.md:42`; EN :43 "does not automatically mean paying legal damages"; JMdict 1514460 and 1514650. |
| Consistency optional: ずれる vs 相違/逸れる, 応対 vs 答える/応じる and 近付ける vs くっつける unguarded | **Optional, not adopted**; kept optional at recheck | The reviewer judged the pairs separated by title and the guards not required (necessity UNVERIFIED). |
| Consistency optional: 休み left unlinked in 送り仮名 | **Optional, not adopted**; kept optional at recheck | EN also leaves it unlinked. |
| Consistency classification of the 19 RU-added exclusions | **Agreed** that all stay; no action at recheck | The reviewer's classes differ from the author's in detail (see the final exclusion set below); it found none unjustified. |
| Consistency new optional at recheck: guard 接する→済ませる for the shared «обходиться» | **Optional, not adopted** | `接する.md:4`; 済ませる «заканчивать (дело); обходиться (чем-л.)»; different complements; the reviewer judged it not a defensible-answer ambiguity (necessity UNVERIFIED). |
| Comprehensibility C1: 退く:21 lacks the kana reading line (minor) | **Resolved** | `退く.md:21`; EN gives the same reading line. |
| Comprehensibility C2: the Latin `wago` label in さようなら:29 and 船便:26 (minor) | **Withdrawn** at recheck (declined) | EN さようなら:26 and 船便:23 have the same sentences; published 家賃:24, 年月:29 and 方々:31 gloss the label as «wago («исконное слово»)». The corpus-wide question is recorded for the Issue #7 follow-up list. |
| Comprehensibility C3: 農薬:20–21 translate 農薬 only as «пестицид» (minor) | **Resolved** (adapted wording); the longer second translation not maintained at recheck | `農薬.md:20–21`; EN "agricultural chemicals" and "this agrochemical"; Digital Daijisen 農薬 農業用の薬剤. |
| Comprehensibility C4: 農薬:42 talks about the card title (minor) | **Resolved** (partial adoption: reworded, not deleted); deletion not maintained at recheck | `農薬.md:42`; EN :49–50 has the equivalent note on growth regulators. |
| Comprehensibility C5: 催促's title ends in the verb «торопить», colliding with 急ぐ (minor) | **Resolved** (partial adoption: title accepted, the 急ぐ sentence declined); the sentence not maintained at recheck | `催促.md:4,12`; EN "pressing for action; urging"; Digital Daijisen 催促 ［名］(スル); 催促→急ぐ is guarded. |
| Comprehensibility C6: 接する «вести себя (с людьми)» reads as behaviour (minor) | **Resolved** | `接する.md:4,12,16`; Digital Daijisen 接する sense 3 応対する; EN "treat people"; the example at :22 already says «обходится». |
| Comprehensibility C7: 近々 «в ближайшие дни» is narrower than the body and EN (minor) | **Resolved** (merged with correctness F1); «скоро» and the day-count sentence not maintained at recheck | `近々.md:4,12,19`; :16 already says «скоро, в ближайшее время». |
| Comprehensibility C8: 交通機関 «средства сообщения» is unclear (minor) | **Resolved** | `交通機関.md:4,12`; EN "means of transport; transport system"; Digital Daijisen 多く、運輸施設をいう. |
| Comprehensibility optionals: お先に's speech-act title, さようなら «прощайте», 送別 «прощальный», 宴会 «застолье», 農村 «земледельческая деревня», 応対's long title, 述語's commentary, 追い掛ける «пускаться в погоню», 近寄る «этой машине» and «Ко мне подошла кошка», 補う «окуригана» and the unlinked absent targets | **Optional, not adopted**; kept optional at recheck | The reviewer classed them as acceptable. |

Cross-batch note: links to absent targets stay plain. Nine EN link targets in this batch's new cards (13 occurrences) are
absent from RU: the words 仮名 (from 送り仮名), ずらす (from ずれる) and 主語 (from 述語), and the kanji cards 補 (from 補う), 述
(from 述語), 接 (from 応接, 接する and 接近), 農 (from 農薬, 農産物 and 農村), 村 (from 農村) and 輸 (from 輸送). The other written
kanji without an RU kanji card, 仮, 宴, 応, 催, 促 and 迫, have none in EN either. No links were held from Batch 233, and none
is held from this batch. The Latin `wago` label in learner prose across published cards (comprehensibility C2) is out of
scope and recorded for the Issue #7 follow-up list; it changes no other files here.

## Final exclusion set

All 140 EN exclusion entries (26 lists; 送り仮名, 迷信, 述語 and 近付ける have none in EN) are retained in EN order; 19 of them
lie inside the batch, and the other 121 target existing RU cards. Nineteen direct, one-sided entries are added on twelve new
cards (18 appended to eleven existing lists and one new list of four on 近付ける), all from the authoring lane and all at the
candidate; the coordinator added none, and fix 1 added and removed none. The author classed 退ける→しまう and 退ける→収める as
required (identical segment «убирать») and the other seventeen as conservative; the coordinator accepted them as reported
("the other 17 conservative and harmless"). The consistency reviewer classed them as follows:

- Required (2): 退ける→しまう and 退ける→収める.
- Required or near-required (1): 農産物→製品 (shared «продукция»).
- Conservative (9): 迫る→収める, 近付ける→近寄る, 近付ける→接近, 近付ける→寄る, 近付ける→近い, 船便→郵送, 船便→速達, 交通機関→車 and
  農村→地域.
- Conservative and weakest (7): お先に→譲る, 送別→送る, 追い掛ける→走る, 応対→付き合い, 応対→返事, 応対→答 and 催促→急ぐ; it judged
  their necessity unestablished and none unjustified.

Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added; the targets do not declare these pairs back. 接する→済ませる is not
guarded (consistency new optional, above).

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (近々, F1; 補う, F2).
- Scoped coverage: **CLEAN** after fix 1 (補う, F2; 農薬 and 近々, C3 and C7).
- Comprehensibility: **CLEAN** after fix 1 (退く, 農薬, 催促, 接する, 近々 and 交通機関); C2 was withdrawn, and the optional
  notes remain optional.
- Cross-file consistency: **CLEAN** throughout; the one RU-only link (追い掛ける:40 → 追い付く) and the six restored
  navigation links of the candidate stand.
- Quiz safety: **CLEAN** throughout, including the 近々, 催促, 接する and 交通機関 retitles. This covers the reviewed batch and
  the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them; the comprehensibility recheck did not
  re-read the other cards or re-fetch dictionary pages. The unchanged cards rest on review 001, in which all three reviewers
  read all 30 cards in full against EN   (the consistency reviewer read three EN originals and the start of a fourth in full and
    compared the rest programmatically).
- The correctness recheck was a bounded bilingual recheck using previously verified dictionary evidence, not a fresh full-batch
  or quiz audit; it did not re-run the coordinator-reported unit tests, and its original evidence and model limitations
  remain. The consistency reviewer performed no web or dictionary lookups, and its necessity classes are judgements, not
  measurements. The comprehensibility recheck did not re-run `validate.py`.
- The correctness reviewer's Gramota and some Jisho requests failed; only successfully inspected entries support its
  conclusions, and its JMdict XML was a live distribution, not the author's historical snapshot.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `1e7c04d`, not `b850104`.
- The `wago` label in published learner prose is left for the Issue #7 follow-up list.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
