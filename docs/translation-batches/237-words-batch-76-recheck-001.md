# Batch 237 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `be448e7c8309d0b9fe6296bd3bc75b2508312556` | `3fdba75c00a9a083e212398d0b36c726a2e6f7e7` | Initial review snapshot: the signed candidate, on `origin/full-ru-237-words-76`. |
| `42f9bcc7843174d2935eb88007b36d862dc58153` | `a82a7eecb894f7277a816e62b7007aca21d77013` | Fix 1. It covers consistency Q1–Q3 (adopted as conservative guards), comprehensibility C237-1 (with a shorter wording than proposed), C237-2, C237-4 and C237-5 (C237-5 with adapted wording at line 16), and the comprehensibility optionals on 言付ける:19 and 応ずる's サ変. It adds four exclusions (すまない→悪い, おじゃまします→すまない, 言付ける→頼む and 言い付ける→頼む) and removes none; it adds and removes no link. Signed; on `origin/full-ru-237-words-76`. |
| `6ff71fb669b6c808d7b41778560cdc9674f0783a` | `fb34b174d42657083f00192ffcc567b9ed815483` | Fix 2 (final candidate). It aligns the comparison in ごめんください:31 with the fix-1 おじゃまします title (a follow-up to comprehensibility C237-5). It changes no exclusion and no link. Signed; on `origin/full-ru-237-words-76`. |

Fix 1 changed seven word files and regenerated `manifest.json` (`contentVersion` `00d911225ab65858`, 5,229 entries: 5,224
`files` + 3 images + 2 scenes; the candidate had `40af8534a08ba712`). The intake was not refreshed; it still records the
candidate's 37 payload hashes.
- `覗く` (lines 4 and 12; comprehensibility C237-1): title and H1 «заглядывать; выглядывать (показываться частично)» instead
  of «заглядывать, подглядывать; выглядывать (показываться частично)», the counterpart of EN :4 "peek; show partly". The
  co-equal «подглядывать» put secrecy into the quiz gloss, although the card's note at :34 says it is not obligatory. The
  proposed qualifier «(в отверстие, ненадолго)» was not added, because the body (:16, :30) already explains the hole and
  quick-look frames.
- `覗く` (line 26; comprehensibility C237-1): «… нельзя понять, заглядывает ли кто-то или предмет выглядывает сам.» instead
  of «… подглядывает ли кто-то …».
- `おじゃまします` (lines 4 and 12; comprehensibility C237-5): title and H1 «простите за беспокойство (входя к кому-либо)»
  instead of «простите за беспокойство (входя к кому-либо); я вхожу»: «я вхожу» reads as the ordinary first person of 入る,
  and the entering situation stays in the qualifier.
- `おじゃまします` (line 16; comprehensibility C237-5, adapted wording): «おじゃまします — вежливое приветствие, которое
  говорят, входя в чужой дом: «простите за беспокойство».» instead of «… «простите за беспокойство» или «я вхожу».». The
  proposed ««простите за беспокойство» — формула, которую говорят, входя.» was not used.
- `おじゃまします` (line 9; consistency Q2): すまない appended to `quiz_exclusions` (now [すみません, ごめんなさい, すまない]), a
  conservative guard: both RU titles are "sorry for the trouble" apologies (すまない «…прости за хлопоты»).
- `すまない` (line 9; consistency Q1): 悪い appended to `quiz_exclusions` (now 15 entries), a conservative guard: すまない
  «извини, виноват; …» and 悪い «плохой; виноватый» share «виноват-», and the 悪い card teaches 悪いね as an apology.
- `言付ける` (line 9; consistency Q3) and `言い付ける` (line 9; consistency Q3): 頼む «просить; поручать» appended to both
  lists (now 5 and 9 entries), conservative guards for the shared «поручать» and the commanding sense. 依頼 «просьба;
  поручение», which the reviewer also mentioned, was not added: it is a noun and shares no exact segment.
- `言付ける` (line 19; comprehensibility optional): «— Я поручил другу передать маме гостинец.» instead of «— Я передал через
  друга гостинец для мамы.», which could read as completed delivery; closer to EN "entrusted" and to the title «поручать
  доставку». The proposed «… отвезти маме подарок» was not used.
- `言い付ける` (line 21; comprehensibility C237-2): «— Я наябедничал учителю о проделке друга.» instead of «— Я рассказал
  учителю о проделке друга.», so the tell-on example shows the sense the title and note teach (JMdict 1264230 sense 2). EN
  :21's neutral "told" relies on the English title "tell on".
- `親類` (line 20; comprehensibility C237-4): «— Неподалёку живёт родственник.» instead of «— Неподалёку живёт наш
  родственник.», as the Japanese and EN "A relative lives nearby".
- `応ずる` (line 37, now lines 37–38; comprehensibility optional): «… через более старое спряжение サ変（さへん）—» /
  «неправильное спряжение по образцу する — и» instead of «… через более старое спряжение サ変 и», following the published
  論ずる precedent.

Fix 2 changed one line, found after fix 1 by the coordinator's corpus grep for the removed wording (the post-fix screen
checks titles only), and regenerated `manifest.json` (`contentVersion` `8ccc25b6a1d48b02`, 5,229 entries):
- `ごめんください` (line 31; follow-up to comprehensibility C237-5): «[おじゃまします](おじゃまします.md) — «простите за
  беспокойство» при входе к кому-либо — признаёт, что гость входит в пространство хозяина.» instead of «… — «простите за
  беспокойство; я вхожу» — признаёт, …», which still quoted the old おじゃまします title. The following sentence, which
  contrasts ごめんください as calling the host before an invitation, is unchanged. The fix-2 commit message calls this check
  "the coordinator's cross-file quote check".

That grep found no other quote of the removed wording except the published `見る:37` related-expressions gloss «覗く のぞく —
заглядывать, подглядывать; …» (EN "peek"), which is outside the batch and was left unchanged; it is on the follow-up list.

The correctness reviewer raised no finding and no optional note. Comprehensibility C237-3 (ごめん's «нет уж, увольте») was
not adopted, nor were the comprehensibility optionals on 観測:21 «прогноз», 見送る:40 «в долгий ящик» and すまない:4
«виноват». The comprehensibility observations on the identical アイデア/アイディア titles, the one-sided お待ちどおさま
declaration and the long titles of 応ずる, 解散, 観測 and 見送る led to no action. The dispositions gave the reasons (see the
reconciliation table).

The coordinator's post-fix title screen of the two changed titles after fix 1 (`b237-postfix-screen.txt`; pool: the RU
primary word cards plus the Batch 238 lane words; parentheses stripped) found both H1s equal to their titles and no exact
shared segment. 覗く's remaining first segment «заглядывать» occurs in no other title. おじゃまします keeps only stem leads
from its unchanged first segment «простите за беспокойство», all present at the candidate: ごめん, ごめんなさい, すまない and
すみません (guarded, すまない by fix 1) and うろうろ, お待ちどおさま, かまう, きょろきょろ, 単に, 単純, 広い, 広がる, 心配,
混乱, 無駄, 簡単, 荒れる, 風邪 and 騒々しい (unguarded; shared «прост» or «беспо» stems only). Neither fix adds or removes a
link. The one RU-only link at the candidate, 言付ける:35 → 言い付ける, is unchanged. The dispositions record
`tools/validate.py` 0 errors, the unit tests (124) OK, the content budget OK and a 5,229-entry manifest after each fix.

Net change from the candidate:
- titles and H1s of 覗く and おじゃまします;
- example translations in 言い付ける, 言付ける and 親類;
- prose in 覗く (line 26), おじゃまします (line 16), 応ずる (line 37, now lines 37–38) and ごめんください (line 31);
- four appended exclusions (すまない→悪い, おじゃまします→すまない, 言付ける→頼む and 言い付ける→頼む); no link change.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`be448e7..6ff71fb -- words` is eight word files, 16 lines added and 15 removed; fix 1 alone changes 8 files (seven word
files and `manifest.json`), 23 lines added and 22 removed, and fix 2 alone changes 2 files (ごめんください and
`manifest.json`), 3 lines added and 3 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs;
the correctness report says its model identity is not independently verifiable, the consistency report "Model: not
verifiable." and the comprehensibility report "Model: not verifiable from this session".

The rechecks ran serially, one reviewer at a time, in two rounds. Round 1: correctness on fix 1 (`42f9bcc`), before fix 2
existed. Round 2, on fix 2 (`6ff71fb`): correctness, narrowly on the fix-2 change, then consistency and comprehensibility,
each rechecking both fixes once (combined diff `be448e7..6ff71fb`). No recheck raised a new finding, so there was no fix 3.

Each reviewer appended its recheck to its own report file; the correctness report has two recheck sections. The
correctness round-1 section records that it read the complete 170-line recheck brief and all seven changed cards in full
and inspected the manifest diff; its round-2 section records that the actual words diff contains only ごめんください:31,
which it read in full together with 見る's comparison in context, as a narrow fix-2 recheck. The consistency section
records its regression checks of titles, exclusions, removed wording, links and the manifest at `6ff71fb`; the
comprehensibility section records that it read the eight changed word cards and the cited passages of 観測, 見送る, 論ずる
and 通じる, not the other 22 batch cards in full, and reconciles each of its findings. Apart from the correctness round-1
brief's length, the recheck sections do not reproduce the briefs, so this record does not claim their contents.

All four recheck sections state that no generator was run. The consistency reviewer ran `tools/validate.py` (0 errors)
and compared `manifest.json` with an in-memory `build_manifest()` result run with `-B` (equal; no file written); the
correctness reviewer states that no generator or validator was run, and the comprehensibility reviewer records that it
did not rerun `validate.py`, the title screen or `link_parity`. The correctness sections record HEAD verified as `42f9bcc`
and then `6ff71fb` with a clean working tree, the consistency section `6ff71fb` with an empty `git status --porcelain`
before and after, and the comprehensibility section `6ff71fb` with an empty status. The recheck records include no
separate coordinator status check after the rechecks; when these records were drafted, a read-only check showed the RU
checkout on `full-ru-237-words-76` at HEAD `6ff71fb669b6c808d7b41778560cdc9674f0783a` with `git status --porcelain
--ignored` printing nothing.

### Round 1 (`42f9bcc`)

| Facet | Scope and result |
|---|---|
| Correctness | Snapshot `42f9bcc`, HEAD verified, working tree clean. Read the complete recheck brief and all seven changed cards in full; inspected the manifest diff. 覗く:4,12,26: the shortened title and formation wording remain at least as accurate; the hole, shop, ticket and non-secret microscope uses stay explicit, and removing «подглядывать» deletes no taught sense (JMdict 1470840:1,3–6). 言い付ける:21: «наябедничал» is at least as accurate and preserves telling on a friend to a teacher (Daijisen いいつける:2 告げ口する; Kuznetsov on gramota.ru, наябедничать with a teacher example). 言付ける:19: at least as accurate, and it avoids implying completed delivery (Daijisen ことづける:1). おじゃまします:4,12,16: the visiting qualifier, the guest/host exchange and the entering explanation preserve the formula (JMdict 1002050:1). 親類:20: deleting «наш» loses nothing. 応ずる:37–38: the gloss is confirmed by Daijisen (サ行変格活用, which includes voiced 応ずる) and Seisenban (応ずる labelled サ行変). The four new exclusions are conservative and remove no teaching or original exclusion. Declined C237-3: no correctness problem or unresolved disagreement (Kuznetsov definition 3 and the universal dictionary on gramota.ru support «нет уж, увольте» as a refusal). No generator or validator was run; the supplied test and screen results were not reproduced. Correctness **CLEAN** and scoped coverage **CLEAN**; no regression; high confidence. |

### Round 2 (`6ff71fb`)

| Facet | Scope and result |
|---|---|
| Correctness | Snapshot `6ff71fb`, HEAD verified, working tree clean; the actual words diff contains only ごめんください:31. Read that card in full and 見る's comparison in context. ごめんください:31 is accurate and at least as faithful: the entering qualifier keeps おじゃまします as the guest's entry formula, and the following sentence still contrasts ごめんください as calling the host before an invitation (JMdict 1002050:1 and 1270690:1; Daijisen ごめんください). No correctness problem with the unchanged 見る:37 gloss «заглядывать, подглядывать»: a related-expression list need not reproduce the full card title (Daijisen 覗く, definitions 1 and 4, freshly inspected). A narrow fidelity/coverage recheck, not a whole-card audit of 見る or a certification of the corpus grep; no generator or validator was run. Correctness **CLEAN** and scoped coverage **CLEAN**; high confidence. |
| Consistency | Snapshot `6ff71fb`, empty `git status --porcelain` before and after; `tools/validate.py` 0 errors; `manifest.json` equal to an in-memory rebuild (`-B`, no file written); no generator. Q1, Q2 and Q3 are **resolved**: すまない ends with 悪い, おじゃまします declares すまない, and both 言付ける and 言い付ける declare 頼む. Titles of おじゃまします and 覗く equal their H1s; no other RU word title carries «заглядывать», and there is no unguarded exact-segment collision (its own grep of RU word titles, not a rerun of the coordinator's screen); おじゃまします only lost «я вхожу», and its pair with すまない is now declared. A grep of `words/` and `kanji/` finds the removed «я вхожу» and «подглядывать» only in 見る:37, a list gloss, not a quiz title, for which the follow-up record is acceptable; ごめんください:31 now matches the new title. The diff touches no link target; the RU-only link 言付ける → 言い付ける is unchanged. The 応ずる サ変 gloss is grammatical and consistent with the 論ずる precedent; the example edits are body text only. Consistency **CLEAN**, quiz safety **CLEAN** and cross-file integration **CLEAN**. |
| Comprehensibility | Snapshot `6ff71fb`, empty status; no generator. Read the eight changed word cards and the cited passages of 観測, 見送る, 論ずる and 通じる; the other 22 cards were not re-read in full. C237-1 is **resolved** ("The extra title qualifier is unnecessary. Not partial."); C237-2 and C237-4 are **resolved**; C237-5 is **resolved**, including the fix-2 quote in ごめんください:31; C237-3 is **withdrawn** («от такой работы увольте» is a refusal for a Russian speaker, glossed «мне этого не надо» at :16 and labelled a refusal at :21; :27–30 keep the old official sense of the noun 御免; the echo is the real exemption link, not a false merge, and the title collides with no other card). The adopted 言付ける:19 and 応ずる:37–38 optionals are **resolved**; the 観測:21, 見送る:40 and すまない:4 optionals are **withdrawn**; the published 見る gloss is accepted as outside the batch. The added exclusions remove no teaching text, and the English teaching points in the edited passages remain in Russian. It did not rerun `validate.py`, the title screen or `link_parity`, and did not re-query dictionaries. Comprehensibility **CLEAN** and scoped coverage **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Consistency Q1: すまない «виноват» vs 悪い «плохой; виноватый», undeclared (low) | **Resolved** (fix 1) | `すまない.md:9`; the 悪い card teaches 悪いね as an apology. |
| Consistency Q2: おじゃまします vs すまない, both "sorry for the trouble", undeclared (low) | **Resolved** (fix 1) | `おじゃまします.md:9`; conservative, not required by EN. |
| Consistency Q3: 言付ける and 言い付ける vs 頼む «поручать», undeclared (low) | **Resolved** (fix 1); 依頼 not added | `言付ける.md:9`, `言い付ける.md:9`; 依頼 is a noun and shares no exact segment; the reviewer's remedy adds only 頼む. |
| Comprehensibility C237-1: 覗く's title «подглядывать» implies secrecy (medium) | **Resolved** (shorter wording than proposed) | `覗く.md:4,12,26`; :34; JMdict 1470840; Daijisen 覗く definitions 1 and 4; EN :4 "peek; show partly"; the qualifier «(в отверстие, ненадолго)» was not added because the body (:16, :30) explains it, and the reviewer judged it unnecessary. |
| Comprehensibility C237-2: 言い付ける:21 neutral «рассказал» (medium) | **Resolved** | `言い付ける.md:21`; JMdict 1264230 sense 2; Daijisen いいつける:2; Kuznetsov (наябедничать). |
| Comprehensibility C237-3: ごめん's «нет уж, увольте» can merge with dismissal (medium) | **Withdrawn** at recheck; declined | «Увольте!» — просьба избавить от чего-л., отказ (Ozhegov); Kuznetsov definition 3 and the universal dictionary on gramota.ru; `ごめん.md:16` «мне этого не надо» and :21 (refusal); :27–30 etymologically related (exemption); no title collision. |
| Comprehensibility C237-4: 親類:20 adds «наш» (medium) | **Resolved** | `親類.md:20`; EN :20 "A relative lives nearby". |
| Comprehensibility C237-5: おじゃまします «я вхожу» reads as the verb 入る (medium) | **Resolved** (adapted wording at :16), including the fix-2 quote | `おじゃまします.md:4,12,16`; `ごめんください.md:31`; JMdict 1002050:1. |
| Comprehensibility optional: 言付ける:19 can read as completed delivery | **Resolved** (adopted, adapted wording) | `言付ける.md:19`; EN "entrusted"; Daijisen ことづける:1. |
| Comprehensibility optional: 応ずる:37 unexplained サ変 | **Resolved** (adopted) | `応ずる.md:37–38`; Daijisen サ行変格活用; Seisenban 応ずる; 論ずる precedent. |
| Comprehensibility optional: 観測:21 «прогноз» is 予報's headword | **Withdrawn** at recheck; declined | An example translation, not a title; the 観測 title «прогнозная оценка (развития событий)» and :18 frame the sense; EN :4 "prediction". |
| Comprehensibility optional: 見送る:40 «в долгий ящик» is too strong | **Withdrawn** at recheck; declined | It renders EN "shelving a plan"; the next sentence says this neither promises a new date nor always means cancellation. |
| Comprehensibility optional: すまない:4 «виноват» is guilt-flavoured | **Withdrawn** at recheck; declined | The collision risk is handled by Q1; «виноват» is an ordinary colloquial apology. |
| Comprehensibility observations: identical アイデア/アイディア titles; お待ちどおさま does not declare お待たせしました | **No action** | One lexeme (JMdict 1014210), identical titles deduplicated, no mutual exclusion as in EN; quiz_exclusions are symmetric pair declarations and the reverse declaration exists. |
| Comprehensibility observation: long titles of 応ずる, 解散, 観測 and 見送る (82–85 characters) | **No action** | Within the existing range (恐縮 88, パス 84); no length rule. |
| Follow-up: published 見る:37 gloss «覗く のぞく — заглядывать, подглядывать» (EN "peek") | **Outside the batch**; unchanged; on the follow-up list | 覗く does include the secret-peeping sense and the list gloss is not a quiz label; changing it would widen the batch. Correctness found no problem, consistency judged the follow-up record acceptable, and comprehensibility accepted it as outside the batch. |

Cross-batch note: links to absent targets stay plain. Five EN link targets in this batch's new cards (5 occurrences) are
absent from RU: the word cards 悔やむ (from 詫びる) and 敬語 (from 言葉遣い) and the kanji cards 訳 (from 訳す), 溶 (from
溶ける) and 測 (from 観測). The other written kanji without an RU kanji card, 応, 慰, 覗, 診, 評, 詫 and 遣, have none in EN
either. No links were held from Batch 236, and none is held from this batch.

## Final exclusion set

All 171 EN exclusion entries (29 lists; 慰める has none in EN) are retained in EN order; 19 of them lie inside the batch,
and the other 152 target existing RU cards. Twelve direct, one-sided entries are added on ten new cards, all appended at
the end of their lists: eight on six cards from the authoring lane, at the candidate, which the coordinator accepted as
reported (慰める's on a new `quiz_exclusions` line), and four from fix 1 (すまない→悪い, おじゃまします→すまない,
言付ける→頼む and 言い付ける→頼む; consistency Q1–Q3). Fix 2 changed no exclusion. The author and the coordinator classed
親類→親戚, 見送る→省く and 見送る→飛ばす as required and the other five lane entries as conservative; the fix-1 entries are
conservative. The consistency reviewer classed the lane entries as follows:

- Required (4): 回答→応対 (at title level), 解散→終了, 観測→読み and 親類→親戚.
- Conservative-to-required (1): 解散→閉会.
- Required at title level, conservative dictionary-wise (2): 見送る→省く and 見送る→飛ばす.
- Conservative (1): 慰める→落ち着く (real Russian-root overlap, necessity unestablished).

It found no unjustified entry and, at recheck, confirmed the four fix-1 entries as stated. Every RU addition is appended
at the end of its list; nothing is removed or reordered. Android applies each declaration symmetrically, so no reverse
declarations were added to baseline cards. アイデア and アイディア carry the identical title «идея; задумка» and, as in EN,
declare no mutual exclusion.

## Final bounded verdicts

- Correctness: **CLEAN** throughout (no initial finding); confirmed after fix 1 and fix 2.
- Scoped coverage: **CLEAN** throughout in both the correctness and the comprehensibility reviews.
- Comprehensibility: **CLEAN** after fixes 1 and 2 (覗く, 言い付ける, 親類, おじゃまします and ごめんください); C237-3 and the
  declined optionals were withdrawn at recheck.
- Cross-file consistency: **CLEAN** throughout; the RU-only link 言付ける:35 → 言い付ける and the nine restored navigation
  links in seven files stand.
- Quiz safety: **CLEAN** after fix 1 (Q1–Q3), including the 覗く and おじゃまします retitles. This covers the reviewed batch
  and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed cards or passages and the lines needed to judge them; the comprehensibility
  recheck did not re-query dictionaries or rerun the validator, the title screen or `link_parity`, and did not re-read
  the 22 unchanged cards in full. The unchanged cards rest on review 001, in which all three reviewers read all 30 cards
  in full.
- The correctness round-2 recheck was a narrow fidelity/coverage recheck of the fix-2 change, not a whole-card audit of
  見る or a certification of the coordinator's corpus grep. The correctness rechecks ran no validator or unit tests, and
  the original dictionary-version, whole-pool, app and native-acceptance limits remain.
- The consistency reviewer cited dictionary senses from memory, and its necessity classes are judgements, not
  measurements; its title-collision check at recheck was its own grep of RU word titles, not a rerun of the coordinator's
  screen, and it did not examine the Batch 238 drafts. Its initial report cites line 8 for the quiz_exclusions field,
  which is on line 9 of the committed cards.
- The published 見る:37 gloss «заглядывать, подглядывать» is unchanged and outside the batch; it is on the follow-up list.
- The intake was not refreshed by either fix, so its payload hashes describe the candidate `be448e7`, not `6ff71fb`.
- Frequency and preferred register (for example «нет уж, увольте», «задумка», «доносить», «наябедничал», «гостинец») were
  not certified. Online dictionaries were current observations, not pinned archives. The app's quiz selection was not
  inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
