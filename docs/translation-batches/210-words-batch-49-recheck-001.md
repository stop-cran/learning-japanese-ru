# Batch 210 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `9d9c00961ef457eac80eb8f37e9ca7e8522245fa` | `6ee737bce5f742105ab95f7cffbfb99f12dd0bde` | Initial review snapshot: the signed candidate, pushed before review. |
| `3930d4a3853a2ca5693c1953fb28ea93f0e5aa70` | `c50ea4eb7ffde408dd02c2dfa33eac279e6b0d6d` | Fix 1 (final candidate): findings from all three facets, one adopted optional note and the intake refresh, committed signed and pushed before the rechecks. |

Fix 1 changed seven word files and regenerated `manifest.json` (`contentVersion` `7026651c57803749`, 4,414 entries) and the
intake:
- `差別` (line 20): 国籍で人を差別してはいけません is rendered «Нельзя дискриминировать людей по гражданству.» instead of «…по
  национальности.» (correctness C1).
- `居眠り`: title and H1 «дремота; сон сидя» instead of «дремота сидя; невольный сон»; line 16 «居眠り — это когда человек
  дремлет или задрёмывает, особенно сидя.» without «сам того не собираясь» (correctness C2); line 19 «Пожалуйста, не
  дремлите на уроке.» instead of «…не спите на уроке.» (comprehensibility M4; the reviewer's «не засыпайте сидя» was not
  used because sitting is implied in class).
- `岩` (line 33): adds «Музыкальный жанр «рок» по-японски называется ロック, а не 岩.» (correctness C3).
- `帯`: title and H1 «пояс кимоно; длинная узкая полоса» instead of «пояс кимоно; опоясывающая полоса», and line 18 «и
  вообще длинную узкую полосу, по форме похожую на пояс.» (correctness C4; «лента» was rejected because it is an exact
  segment of テープ «лента; клейкая лента»). The source-list passage was condensed from two sentences to EN's one: «Карточка
  сохраняет слово и чтение おび из исходного списка слов, но исправляет его несовпадающий перевод; что имел в виду составитель
  списка, остаётся неясным.» (comprehensibility M2, partially accepted). New conservative guards `quiz_exclusions: [縞, 筋]`,
  because the plain shape gloss now sits next to 縞 «полоса; полосатый узор» and 筋 «сухожилие; полоса; сюжет».
- `屋根`: new `quiz_exclusions: [屋上]` (consistency F1).
- `居る`: `quiz_exclusions: [いる, いらっしゃる, おいでになる]` without 参る (consistency O1, adopted); line 33 «**ます-основа +
  おる** (основа, к которой присоединяется ます)» instead of «**основа на -masu + おる**» (comprehensibility M1; the proposed
  負け + おる example was not added because EN gives none and it was not independently verified).
- `年寄り`: line 33 (formerly 32) «[老人](老人.md)（ろうじん）— другое существительное, связанное с возрастом.», as in EN,
  without naming 老人's quiz title; lines 17–18 add that the examples render polite お年寄り with the softer «пожилой человек»
  (comprehensibility M5, partially accepted; the examples are unchanged).
- The intake note now counts thirty-five restorations instead of twenty-three and names the fixed cards.

Net change from the candidate: two titles with their H1 headings (居眠り, 帯), two example translations (差別, 居眠り), two
definition sentences (居眠り, 帯), three explanatory edits (岩, 居る, 年寄り), one condensed provenance passage, three added
exclusions and one removed exclusion. No Japanese example, reading or internal link changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially. Each reviewer appended to its own report file, which stayed in its session context, and each
recheck message gave it:
- the revised snapshot, its parent and the read-only rules;
- the actual content diff (`git diff 9d9c009 3930d4a -- words`);
- the coordinator's evidence for every change, and the declined items from all three facets with their reasons, without
  the other reviewers' reports;
- the coordinator's disposition of each of its own findings and optional notes.

The shared opening said that the edits came from all three blind reviewers and asked each reviewer to judge every change on
its evidence rather than its origin.

The recheck prompts forbade running `tools/build_manifest.py` or any other generator; all three recheck sections state that
none was run. The correctness and consistency reviewers ran `tools/validate.py` (0 errors); the comprehensibility reviewer
does not report running it. After every recheck the coordinator confirmed that HEAD was unchanged and that
`git status --porcelain --ignored` was empty.

### Round 1 (`3930d4a`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer inspected the complete words diff, reread the seven revised cards in full, and read the 縞, 筋 and 屋上 guard targets and frozen EN 年寄り. C1–C4 are resolved: 差別 keeps 国籍 as citizenship; 居眠り no longer makes unintendedness lexical, while the first example keeps it on てしまいました and «не дремлите» preserves the second example's request; 岩 restores the ロック note without an English-dependent pun; 帯 gives the shape-based strip sense, keeps おび versus たい, and its condensed provenance keeps EN's correction and uncertain-intention boundary. It found no regression: ます-основа explains the attachment without changing register; dropping 参る removes no EN exclusion; 年寄り's softer gloss is presented as a choice for these examples, and it newly inspected JMdict お年寄り and the Kuznetsov «пожилой» entry. `tools/validate.py` reported 0 errors. Correctness and scoped coverage are **CLEAN**. |
| Consistency | The reviewer confirmed that the fix touches nine files (seven cards, the manifest and the intake). F1 and O1 are resolved. It screened the retitled 居眠り and 帯 by normalized segment against every current RU word title and found no shared segment; the new guards 帯→縞, 帯→筋 and 屋根→屋上 point to existing files and are valid direct pairs. It accepted the declined O2–O4 as optional, because no quiz collision was demonstrated. Exactly seven hashes and `contentVersion` changed among the 4,414 manifest entries, all matching their files, and all 52 intake hashes match HEAD. `tools/validate.py` reported 0 errors and `git diff --check` was clean. Consistency, quiz safety and cross-file integration are **CLEAN**. |
| Comprehensibility | The reviewer read the seven-card diff and the changed passages, the unchanged 就職:32, the EN counterparts and the published RU provenance notes in 便, 変化 and はあ. M1, M4 and M5 are resolved. M2 is partially resolved: the おび/たい warning stays and the title no longer requires encircling; the remaining compiler-intention sentence matches EN and the published series, and is skippable provenance rather than a Japanese-rule error, so the remainder is optional. M3 is reclassified as optional: the first sentence already gives the employment restriction in Russian, and removal is a series-wide editorial question. The original optional notes stay optional. No regression: the 岩 sentence does not depend on English, «по гражданству» avoids the ethnic reading, and the exclusion changes do not alter learner prose. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 差別 «по национальности» reads as ethnicity | **Resolved** | `差別.md:20`; JMdict 国籍; 日本大百科全書 国籍; Kuznetsov «национальность» sense 1. |
| Correctness C2: 居眠り title and definition make unintendedness lexical | **Resolved** | `居眠り.md:4,12,16`; frozen EN `居眠り.md:15,20`; Daijisen 居眠り. |
| Correctness C3: 岩 omits EN's ロック note | **Resolved** | `岩.md:33`; frozen EN `岩.md`; JMdict ロック. |
| Correctness C4: 帯 «опоясывающая» narrows "band or strip" | **Resolved** | `帯.md:4,12,18`; JMdict おび sense 3; Daijisen おび sense 3. |
| Consistency F1: 屋根 «крыша» vs 屋上 «площадка на крыше» | **Resolved** | `屋根.md:9` `quiz_exclusions: [屋上]`. |
| Consistency O1: 居る→参る has no shared sense | **Resolved** (adopted) | `居る.md:9`; 参る's guards for おいでになる/いらっしゃる rest on come/go senses that 居る lacks. |
| Consistency optional guards 差別↔区別/違い, 常に↔いつでも, 帰宅↔戻る | **Optional, not adopted** | EN declares none; the titles share no exact segment; 年中 already guards the いつでも/常に cluster; the app deduplicates exact titles only. Reviewer accepted the decline. |
| Consistency limit: RU-only links in kanji 和 and 居 | **Out of scope** | Identical on published main; untouched by this batch. |
| Consistency limit: 118 strokes raw-hash differences | **No action** | `tools/build_manifest.py` hashes text after CRLF→LF normalization, as recorded in Batch 209; the reviewer's recheck notes it as not a defect. |
| Comprehensibility M1: 居る «основа на -masu» is an English label | **Resolved** | `居る.md:33`; published RU `様.md:18`, `乗り物.md:26`. The proposed 負け + おる example was not adopted. |
| Comprehensibility M2: 帯 provenance passage | **Partially resolved**; remainder **optional** | `帯.md:44-45` condensed to frozen EN `帯.md:34`'s single sentence; series precedent `便.md:44-47`, `変化.md:58`, `はあ.md:34`. |
| Comprehensibility M3: 就職 source-list note | **Optional, not adopted** | `就職.md:32` renders frozen EN `就職.md:32` faithfully; same series precedent. Reviewer reclassified it as optional. |
| Comprehensibility M4: 居眠り «не спите» borrows 眠る/寝る's title | **Resolved** | `居眠り.md:19`; frozen EN "Please do not doze off during class." |
| Comprehensibility M5: 年寄り examples use 老人's announced title | **Resolved** | `年寄り.md:17-18,33`; frozen EN `年寄り.md:28`; examples kept as natural renderings of polite お年寄り. |
| Comprehensibility optional notes on ボーイ, 年月, 差別 «как покончить», 州 vs 大陸 | **Optional, not adopted** | Non-blocking and consistent with EN. Reviewer kept them optional. |
| Exclusion classification | **Differences recorded** | The consistency reviewer rated 居眠り→うとうと required and the two 居る honorific guards conservative-leaning-required; the guards are identical under either rating. |

Cross-batch note: `少年.md:33` glosses 少女 as «девочка». Batch 211 introduces the 少女 card and links and aligns that gloss;
it is reviewed with that batch.

## Final exclusion set

All 26 EN exclusion entries (16 lists) are retained. Fourteen direct, one-sided entries are added on nine new cards:

- Required (8): 年寄り→老人, 平和→世界, 帰宅→帰る, 居る→いらっしゃる, 居る→おいでになる, 就く→習う, 就く→就職, 屋根→屋上.
- Conservative (6): 帰宅→帰り, 平等→等しい, 居眠り→うとうと, 就く→座る, 帯→縞, 帯→筋.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fixes (差別, 居眠り, 帯).
- Scoped coverage: **CLEAN** after fixes (岩, 帯).
- Comprehensibility: **CLEAN** after fixes (居る, 居眠り, 年寄り, with 帯 partially and 就職 not changed; both remainders
  optional).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** after fixes (屋根→屋上), for the reviewed batch and the directly adjudicated pairs. Exclusions are
  direct pairs, not transitive groups.

Limits: the rechecks reread only the changed passages and the cards needed to judge them; unchanged cards rest on review
001's full reading. Only the correctness reviewer inspected new dictionary entries in the recheck; the consistency and
comprehensibility reviewers did not re-fetch dictionaries. The consistency reviewer read the changed cards' link sets from
the diff rather than rerunning link parity, and did not read the app's `Words.kt`. No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
