# Batch 206 — independent review 001

## Snapshot and scope

- Reviewed snapshot: candidate tree `6bfa34bee12a8bc1e805693a49888fb65cfd7331`, staged in a scratch worktree, not a commit.
  - Batches 197–205 had been reviewed and their fixes rechecked, but their signed commits could not yet be made because the
    signing key's passphrase cache had expired. Rather than wait, Batch 206 was authored on top of the reviewed Batch 205 tree
    `84dc60f36a87e9d9830a88933c63105d0aad4bf4`, at detached HEAD `5dd9a78` in a separate worktree.
  - The candidate differs from `84dc60f` by 48 paths: 30 new word cards, 17 navigation-only files (20 restored links) and
    `manifest.json`.
  - Before staging the candidate, the coordinator made one change to the author's output: 文's exclusions became
    `[文章, 案, 提案]`. The author had declined 文–提案 because both titles are qualified; the coordinator's title screen showed
    that 文 «предложение (грамматическое)» and 提案 «предложение (на рассмотрение)» share the segment «предложение», the same
    homonym for which the author had already declared 文–案. All three reviewers read the candidate with this pair present.
  - Reviewers were told to read the staged tree and not to rely on HEAD. No unsigned commit was made.
- After Batch 205 was published as `2d963b0a37793153a0d63ee54b015361f0061907`, branch `full-ru-206-words-45` was cut from that merge. Its parent commit
  `63e4f31e0b4a1a82cea1ef905cac2a02a10383a9` adds only the Batch 205 publication record. The final reviewed content tree was copied there and committed signed as
  `b1e17bfcf168731f0a6cfea0fe922f171abc7434`, together with the intake. `git diff b8df8df b1e17bf -- words kanji strokes articles manifest.json` is empty;
  see the recheck record for the revised tree `b8df8df`.
- Published baseline recorded in the intake: `2d963b0a37793153a0d63ee54b015361f0061907` (Batch 205 merge).
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers against their EN originals.
  - Correctness also read the changed regions of all 17 navigation-only files, the binding RU instructions and the existing RU
    普段 and 新しい cards in full. It ran `tools/validate.py` (0 errors).
  - Consistency read the complete `-U0` diffs of the 17 navigation-only files and confirmed that each changes only link markup at
    an existing EN link position. It recomputed every changed `.md` hash in the manifest, ran `tools/validate.py` (0 errors), and
    script-screened every new title and title segment against all RU word titles, together with EN exclusion retention, link
    existence, EN link parity and front-matter parity.
  - Comprehensibility read the existing RU 暮らし, 普段, 生活, 光, もう, 旅行, 新しい, 文化, 字, 費用, テキスト, 尊敬 and 月日 for
    the colliding titles and conventions, read the navigation diffs, and ran the shared `link_parity.py` on the 30 new paths.
  - The intake was generated after review from the same paths. Its payload hashes are checked by the final validation receipt.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that the worktree's index tree was
  still `6bfa34b`, that the working tree equalled the index and that nothing was untracked or ignored. No fix was applied until all
  three reports were complete.
- All three launch messages allowed running validators on the working tree, forbade `tools/build_manifest.py` and any other
  generator, and named the report as the only file a reviewer writes. All three reports state that no generator was run.
- Full blind reports:
  - `206-words-batch-45-review-correctness-001.md`
  - `206-words-batch-45-review-consistency-001.md`
  - `206-words-batch-45-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the title-screen output or one another's reports.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (放す only); scoped coverage **NEEDS FIX** (日付 only). The other 29 cards were CLEAN on each
facet.

- C206-01 (minor, high confidence), `放す.md:21`: «Второй пример буквально описывает, как рука отпускает шарик» reverses the
  Japanese roles of 子供は風船から手を放しました. 子供 is the topic and agent, 手を the object, and 風船から what the hand is
  released from; making the hand the literal agent and the balloon its object can misteach を/から directly after the card's
  argument-structure rule. The idiomatic translation was fine. Evidence: the frozen EN wording "literally describes releasing one's
  hand from the balloon"; Digital Daijisen 放す sense 2 with the structurally matching example «ハンドルから手を放す»; Jisho/JMdict
  marking 放す transitive. Remedy (the reviewer's text): «Во втором примере буквально говорится об отнятии руки от шарика: 手を —
  руку, 風船から — от шарика».
- C206-02 (minor, high confidence), `日付.md:37-40`: the RU card dropped EN's whole comparison with デート, including the visible
  word label. Dropping the English "date" polysemy was appropriate, but the comparator itself belonged to the preservation scope
  and could stay as plain text while the RU target is absent. Evidence: the frozen EN 日付 card; Jisho/JMdict 日付 sense 1 "date;
  dating" and デート sense 1 "date (with someone)". Remedy: «日付 — календарная дата; романтическая встреча, свидание — デート», with
  デート unlinked and no claim that Russian «дата» has a romantic sense.

Other checks:

- All 60 main Japanese example sentences and their kana readings match EN. Stable non-title metadata is retained; exclusion
  differences are additions only, and no EN exclusion was removed. Dictionary citation IDs and sense labels are retained, with
  extra comparison citations in 文 and 数える. All 17 navigation changes are link-only.
- The reviewer inspected the Jisho/JMdict entries for all 30 spellings, distinguishing both 方々 entries and both 故郷 readings.
  Supplementary checks: Digital Daijisen 新しい sense 4㋐ («新しい魚», supporting the RU-only 新鮮 contrast), 新た senses 1–2 and
  出身 sense 1; Gramota/Kuznetsov «предложение» and «считать» for the Russian comparisons in 文 and 数える.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **CLEAN**; scoped cross-file integration **CLEAN**. No findings.

- Front matter matches EN apart from translated titles and extended exclusions. Every internal link resolves; there are no
  RU-only links and no dropped EN links with an existing RU target. All 17 navigation files restore links at EN link positions
  only. Every changed manifest hash matches its bytes, and no `.md` file is unlisted.
- All EN exclusions are retained. New exact-segment collisions (日付/月日, 方々/人, 文/案, 文/提案, 旅/旅行, 既に/もう) are all
  guarded. No new title or title segment equals another card's title or segment without a direct pair.
- 放す and 離す need no guard: JMdict gives 離す "to separate; to part; to keep apart" with no "let go" sense, and the RU titles
  do not overlap.

Optional: a conservative 日光→光 guard (光 «свет» excludes 日 but not 日光; the qualifier «солнечный» distinguishes the titles, so
the reviewer did not require it); and a note that 方々 keeps EN's merged title «люди (уважительно); повсюду», two lexical
identities in one title, which is faithful to frozen EN and separated in the body.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (方々, 日常, 支出); the other 27 cards **CLEAN**. Scoped coverage **NEEDS FIX** (日常,
支出); the other 28 cards **CLEAN**.

- C1 (minor, high confidence), `方々.md:31,45-46`: the card used the schema word «тип» for its metadata, and closed with a note
  about the source word list mixing both words' glosses. A beginner cannot tell which list or type is meant. Remedy: name the
  reading of the title word directly and delete the source-list sentence.
- C2 (minor; high confidence that the contrast is absent, medium-high that it affects learning), `日常.md:12-17,34-36`: the card
  never names 生活, 暮らし or 普段, although its examples gloss 日常 and 日常生活 as «повседневная жизнь», the title of 生活, and it
  says 日常 can be used adverbially without showing a form. Remedy: a qualified contrast, not a substitution ban, plus Digital
  Daijisen's adverbial example 日常用いる道具. Evidence: Digital Daijisen 日常 «つねひごろ。ふだん。平生», example «日常用いる道具». EN
  also lacks the contrast, so this is a Russian-audience gap rather than a dropped EN sentence.
- C3 (minor, medium-high confidence), `支出.md:15-16,35-36`: 支出 «расход, затраты» and the body's gloss of 費用 «издержки или
  затраты» collide with each other and with 費用's title «расходы; затраты», and no example shows money required by an undertaking
  versus money paid out. Remedy: define 費用 as the money a given undertaking requires (旅行の費用) and 支出 as money paid out,
  noting that one payment can fall under both. Evidence: Digital Daijisen 支出 «ある目的のために自分の所有する金銭や物品を支払う
  こと。また、その金品» (⇔収入) and 費用 sense 1 «ある事をするのに必要な金銭».

Optional: register notes that 既に and 新た often feel more written than もう and 新しい (the reviewer noted that the Daijisen
entries mark no strict restriction); 故郷's example «поеду», where sibling cards render 帰る as return; and 文字's example gloss
«буквы», narrower than the card's own definition.

The reviewer also confirmed that the English-only points of the source cards (romantic "date", "count on", surgical
"operation", English "way", "letter" and "injury") were adapted or dropped without inventing a Russian ambiguity.

## Exclusion classification: author, coordinator and consistency reviewer

All 23 EN exclusion entries (17 lists) are retained. The author added 13 direct, one-sided exclusion pairs beyond EN on 10 new
cards, the coordinator added 文–提案 before review, and 日光–光 was adopted after review from the consistency reviewer's optional
item: 15 pairs on 11 cards. The author report and the blind consistency reviewer classified the pairs independently. The
differences are preserved here rather than resolved by vote. Classification does not change runtime behaviour, because every kept
pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `日付`→`月日` | required | required |
| `方々`→`人` | required | required |
| `新鮮`→`新しい` | required | conservative |
| `数える`→`計算` | required | conservative |
| `教授`→`教える` | required | conservative |
| `断る`→`遠慮` | conservative | required |
| `文`→`案` | conservative (reclassified from required: the title is qualified) | required |
| `故郷`→`田舎` | conservative | required |
| `出身`→`生まれ` | conservative | required/conservative |
| `故郷`→`生まれ` | conservative | required/conservative |
| `方々`→`方` | conservative | conservative |
| `教授`→`教師` | conservative | conservative |
| `支出`→`支給` | conservative | conservative (weakest; harmless) |
| `文`→`提案` | declined (both titles qualified); added by the coordinator before review | required |
| `日光`→`光` | not considered | optional conservative guard |

Neither found a kept pair unjustified, and the consistency reviewer found no required guard missing. The last pair was added
after review.

Reconciliation, the coordinator's dispositions and the final verdicts are in `206-words-batch-45-recheck-001.md`.
