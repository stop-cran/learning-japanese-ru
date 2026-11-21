# Batch 225 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `56996a024ba2641a8d5e846d8c63e1981beeccff` | `cec94999a3e5496f49132267a073e5e56aa92d24` | Initial review snapshot: the signed candidate, pushed before review. |
| `830487df91fde22b72df1a8220623a226a713296` | `11b678f5eb1de7c89fbb5ef102a796f193976ab9` | Fix 1 (final candidate). It covers correctness C1, comprehensibility C1–C4, the consistency guard suggestion, one correctness and one comprehensibility optional item, and the intake refresh. Signed and pushed before the rechecks. |

Fix 1 changed seven word files and regenerated `manifest.json` (`contentVersion` `9a92c8704e78d687`, 4,869 entries; the
candidate had `5cebfe295a2192a6`) and the intake:
- `ぐっすり` (line 18; correctness C1, the reviewer's wording): «— Прошлой ночью мне удалось крепко поспать.» instead of
  «…я смог крепко выспаться», which adds the result of having slept enough. EN has "I was able to sleep soundly last night".
  JMdict 1004060 sense 1; Kuznetsov выспаться.
- `いつまでも` (line 33; correctness optional item O1, the reviewer's wording): «всё ещё, спустя столько времени» instead of
  the ungrammatical «всё ещё, после стольких-то времени», after EN "still, after all this time".
- `お目に掛かる` (line 19; comprehensibility C1, alternative wording): «— Завтра я с вами встречусь.» instead of «Увидимся
  завтра», a casual, reciprocal goodbye against the card's rule (lines 16 and 29) that the phrase is a humble, speaker-side
  meeting. EN has "I will see you tomorrow". The reviewer's «Завтра буду иметь честь вас видеть» was not used: it is stilted
  for a model sentence, the title already carries «иметь честь встретиться», and the humility is carried by the Japanese
  verb, while the Russian keeps the speaker as the one who meets.
- `おめでとう` (line 33; comprehensibility C2, partially accepted): a closing note sentence, «"Наилучшие пожелания" в
  заголовке — пожелание по радостному поводу; おめでとう не служит заключительной формулой письма вроде "С наилучшими
  пожеланиями".» (with «» quotes in the card). The title «поздравляю!; наилучшие пожелания» is kept: it mirrors EN
  "congratulations; best wishes" and JMdict 1270700 sense 1 ("congratulations!; well done!; best wishes!; all the best!").
  The coordinator's dispositions placed the note at line 12; it was appended to the usage paragraph at line 33.
- `いわゆる` (line 17; comprehensibility C3, the reviewer's wording): «— Это то, что называют энергоэффективным домом.»
  instead of «Это так называемый энергоэффективный дом», which models the often dismissive «так называемый» that line 32
  warns about. EN has "what is called". The title «так называемый; что называется» is kept (EN "so-called").
- `ごめんなさい` (line 26; comprehensibility C4, and correctness O2 for this card): «Элемент ごめん китайского
  происхождения (канго) соединён с исконным японским окончанием なさい, так что это смешанное выражение.» instead of the
  unglossed «Канго-элемент…» with the English-audience clause «а не заимствование из английского». The wording agrees with
  `お.md:29` in this batch («китайские (канго)»). The rest of the remedy, advice to learn the word as a fixed formula, was
  already the next sentence and was not duplicated.
- `ごめんなさい` (line 9; consistency optional guard): `quiz_exclusions: [すみません, 申し訳, 謝る]` instead of
  `[すみません, 申し訳]`. The card contrasts the verb 謝る in its synonyms section, and すみません→謝る is the published
  precedent. The guard is conservative and one-way; Android applies it in both directions.
- `鳴らす` (line 33; comprehensibility optional item): «славился как великий питчер (подающий в бейсболе)» instead of the
  bare «питчер».
- The intake note now names the fixed cards, and the seven candidate hashes were refreshed.

Correctness O2's request to gloss «годан» (`お目に掛かる.md:21`, `うなる.md:16`, `鳴らす.md:16`) and «онные чтения»
(`こんにちは.md:25`) was not adopted, and the ごめんなさい–許す guard was not added; the dispositions gave the reasons,
which the recheck briefs put to the reviewers (see the reconciliation table).

No title, H1 or link changed, so the coordinator's title screen and link parity were unchanged from the candidate: no
unguarded exact title-segment overlap, no EN link lost where the RU target exists, and the same single RU-only link.

Net change from the candidate:
- example translations in ぐっすり, お目に掛かる and いわゆる;
- note wording in いつまでも, ごめんなさい and 鳴らす, and one appended note sentence in おめでとう;
- one added exclusion entry (ごめんなさい→謝る).

No Japanese example sentence was altered, and no sourced reading, EN exclusion or link changed. The content diff is seven
word files, 8 lines added and 8 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, one reviewer at a time, all on fix 1, in this order: correctness, consistency, comprehensibility.
No recheck raised a new finding, so no second fix was needed.

Each reviewer appended to its own report file, which stayed in its session context. Each recheck brief gave the reviewer:
- the fix commit, the reviewed candidate as the base, and the read-only rules;
- the actual content diff `56996a0..830487d`;
- the coordinator's evidence for every change and the declined items, stated without the other reviewers' reports;
- the reviewer's original verdicts and the disposition of each of its own findings and optional items. The
  comprehensibility brief stated why お目に掛かる used other wording than the proposed remedy and why おめでとう's title was
  kept, and asked whether the reviewer maintained C1 and C2.

The three briefs were delivered as session files that the reviewers were told to read in full.

After the correctness brief had been sent, the coordinator found that its O2 rationale overstated the corpus: it implied
that «годан» and «онные чтения» are used without a gloss throughout. Several word cards gloss «годан» in passing (for
example `伸ばす.md:16` «глагол годан (пятиступенчатого спряжения)», `似合う.md:16` and `受け取る.md:16`). A correction was
sent to the correctness reviewer before its recheck section was written, and the consistency and comprehensibility briefs
carried the corrected rationale: practice is mixed with no settled rule, and a corpus-wide convention is an owner-level
question. The correctness reviewer accepted the corrected account and noted that it did not audit the counts. For this
record the counts were rechecked at `830487d`: «годан» appears in 326 files under `words/`, `kanji/` and `articles/`, and
547 of the 718 kanji cards label reading-table rows «онное». The briefs also cited 681 for «онн* чтени…»; that figure could
not be reproduced (a case-insensitive search for «онн…» followed by «чтени…» finds 306 files repo-wide). The disposition
does not depend on the exact counts.

All recheck messages forbade running `tools/build_manifest.py` or any other generator. Every recheck section states that
none was run. The correctness and consistency reviewers each ran `tools/validate.py` (0 errors each) and removed the
bytecode cache it created; the comprehensibility reviewer did not run it. The fix script checked `git status --porcelain`
after the fix commit. Each recheck section records HEAD `830487d` with a clean tree (the consistency reviewer before and
after its checks), and after the last recheck HEAD was `830487d` with an empty `git status --porcelain --ignored`.

### Round 1 (`830487d`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer read the seven-card diff against `56996a0`, and reread お目に掛かる, おめでとう and ごめんなさい in full for context. C1 is **resolved**: «удалось крепко поспать» keeps sound sleep and the successful potential past without asserting restorative sufficiency. O1 is **resolved**. O2 is **partially resolved** and optional: ごめんなさい now explains канго; glossing «годан» and «онные чтения» would also fit corpus practice, and declining it leaves an owner-level convention choice, not a correctness defect. No regression: お目に掛かる keeps the speaker-side meeting, with the humble layer carried by the title and the surrounding guidance; いわゆる is an accurate neutral paraphrase; the ごめんなさい explanation is accurate, and the 謝る exclusion contradicts nothing; the おめでとう note distinguishes event-bound good wishes from a letter valediction; the 鳴らす gloss is accurate. Validator 0 errors; `git diff --check` clean. Correctness and scoped coverage are **CLEAN**. |
| Consistency | Snapshot `830487d` with a clean tree before and after. The ごめんなさい–謝る guard is **resolved**: the list is well-formed, `謝る.md` exists and has no reverse entry. ごめんなさい–許す is **withdrawn**, accepting the disposition; あっ–まあ needs no action. Titles and `.md` link multisets are unchanged in the seven cards; navigation stays 10 files, and the only RU-only link is still ごめんなさい→申し訳. Recomputed against EN: 25 RU-added exclusions on 15 cards and 35 EN exclusions kept, none lost. The prose edits add no quiz-relevant label. All 40 batch `words/` manifest entries and all 40 intake candidate hashes match the tree. Consistency, quiz safety and scoped integration are **CLEAN**. |
| Comprehensibility | The reviewer read the seven changed passages. C1 is **resolved**, and the reviewer no longer maintains that the example needs «иметь честь»: the new sentence removes the casual goodbye, keeps the speaker as the one who meets and matches お目に掛かります. C2 is **partially resolved**: the reviewer maintains no title change, the note blocks the letter-closing reading, and «поздравляю!» stays the lead and the spoken example; its residual, that a bare «наилучшие пожелания» is odd to say aloud, is now qualified and optional. C3 and C4 are **resolved**. The 鳴らす optional item is resolved; the すみません exclusion suggestion is **withdrawn**. No regression, including ぐっすり, いつまでも and the 謝る guard. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: ぐっすり «выспаться» adds sufficiency (minor) | **Resolved** | `ぐっすり.md:18`; JMdict 1004060 sense 1; Kuznetsov выспаться. |
| Correctness O1: いつまでも «после стольких-то времени» ungrammatical | **Optional, adopted** | `いつまでも.md:33`; frozen EN "still, after all this time". |
| Correctness O2: gloss «канго», «онные чтения» and «годан» | **Partially resolved**; optional residual | `ごめんなさい.md:26` glosses канго (with comprehensibility C4). «годан» and «онные чтения» are left as an owner-level corpus convention; corpus practice is mixed. |
| Consistency optional: ごめんなさい–謝る guard (low severity) | **Resolved** | `ごめんなさい.md:9`; the card contrasts 謝る; precedent すみません→謝る. |
| Consistency optional: ごめんなさい–許す (low confidence) | **Withdrawn** by the reviewer at recheck | The titles share no segment, and the card does not contrast 許す. |
| Consistency optional: あっ–まあ | **No action needed** | The reviewer found none needed; the shared «ах» is incidental. |
| Comprehensibility C1: お目に掛かる «Увидимся завтра» (moderate) | **Resolved** (alternative wording) | `お目に掛かる.md:16,19,29`; JMdict お目に掛かる sense 1; frozen EN "I will see you tomorrow". |
| Comprehensibility C2: おめでとう title «наилучшие пожелания» (minor) | **Partially resolved**; optional residual | `おめでとう.md:4,12,33`; frozen EN "congratulations; best wishes"; JMdict 1270700 sense 1. The title is kept; the note excludes the letter-closing reading. |
| Comprehensibility C3: いわゆる example «так называемый» (minor) | **Resolved** | `いわゆる.md:17,32`; frozen EN "what is called". |
| Comprehensibility C4: ごめんなさい «Канго-элемент» unglossed (minor) | **Resolved** | `ごめんなさい.md:26`; `お.md:29`. |
| Comprehensibility optional: 鳴らす «питчер» | **Optional, adopted** | `鳴らす.md:33`. |
| Comprehensibility optional: a reverse すみません–ごめんなさい exclusion | **Withdrawn** by the reviewer at recheck | ごめんなさい declares すみません, and Android applies declarations in both directions. |
| Comprehensibility optional: いただきます H1, あいにく «как назло», あんまり «не очень-то», きつい title scope | **Optional, not adopted** | The H1/title split mirrors EN; «как назло» is an attested adverse-coincidence idiom (correctness reviewer, Russian Wiktionary); きつい's exclusions guard 狭い and 急激. The reviewer kept them optional at recheck. |
| Consistency limit: raw-byte hash mismatch on 118 `strokes/*.json` manifest entries | **Withdrawn** as a defect; pre-existing and outside the batch | `tools/build_manifest.py` hashes text files after CRLF→LF normalization (line 19). All 718 `strokes/` entries match the normalized hash; exactly those 118 files contain CRLF, and they are byte copies of EN blobs kept by `.gitattributes` (`strokes/*.json -text`). The batch touches no `strokes/` file. |
| Exclusion classification | **Reviewer's classification adopted** | The author's and the consistency reviewer's classifications differ only in strength (table in review 001). The fix entry ごめんなさい→謝る is conservative, as the dispositions had it; the reviewer reconfirmed the 25/15 and 35 counts at recheck but did not restate the required/conservative split. |

Cross-batch note: links to absent targets stay plain. Three EN link targets in this batch's new cards are absent from RU:
the articles `japanese-onomatopoeia` and `onomatopoeia-sound-patterns` (both from ぐっすり) and the kanji card 漱 (from
うがい). 麓 has no kanji card in RU or EN. The すみません→ごめんなさい and すみません→ありがとう links held by Batch 224 were
restored in this batch.

## Final exclusion set

All 35 EN exclusion entries (19 lists) are retained. Twenty-five direct, one-sided entries are added on 15 new cards (seven
of them new lists: こんにちは, こんなに, おめでとう, うなる, いらっしゃい, いただきます and あいにく):

- Required (17): こんなに→そんなに, それほど and あんなに, きつい→狭い and 急激, おめでとう→お祝い and 祝う, うなる→吠える,
  いけない→不可 and 禁止, ありがとう→感謝, 鳴らす→掛ける, ごめんなさい→申し訳, いただきます→ありがとう, あんまり→別に,
  あっ→しまった and あいにく→残念.
- Conservative (8): こんにちは→あいさつ, いらっしゃい→あいさつ and 寄る, いただきます→いただく, おめでとう→希望 and 祝い,
  あらゆる→様々 and, added in fix 1, ごめんなさい→謝る.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the fix (ぐっすり); O1 adopted, O2 partially adopted with an optional residual.
- Scoped coverage: **CLEAN** throughout.
- Comprehensibility: **CLEAN** after the fix (お目に掛かる, いわゆる, ごめんなさい; おめでとう partially resolved with an optional
  residual).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN**, including the fix-1 entry on ごめんなさい. This covers the reviewed batch and the directly
  adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them (the correctness reviewer also reread
  three changed cards in full). The unchanged cards rest on review 001: the correctness and comprehensibility reviewers'
  full reading of all 30 cards, and the consistency reviewer's line-by-line comparison of eight cards plus a scripted
  front-matter, exclusion and link check of the other 22.
- The comprehensibility reviewer did not re-fetch JMdict 1270700; it accepted the cited sense 1 "best wishes" as the basis
  for keeping the wish gloss.
- Whether to gloss «годан» and «онные чтения» corpus-wide is left to the owner. The counts above are text searches, not a
  review of each card.
- The consistency reviewer's dictionary senses came from memory of JMdict, and its initial report listed a `kanji/麓` link
  among omitted EN links; EN `麓.md` has no kanji link. The actual omitted EN links are those in the cross-batch note.
- The author did not look up its Russian glosses in a dictionary; the correctness reviewer verified the flagged ones.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
