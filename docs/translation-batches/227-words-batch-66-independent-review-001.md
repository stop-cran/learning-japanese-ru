# Batch 227 — independent review 001

## Snapshot and scope

- Reviewed commit: `5cf2313776672567fd1454fffd027b253bb10278` (tree `b8e291d86716374cd700fba67aaccfa3900d3caf`), branch
  `full-ru-227-words-66`, parent `0d431aa`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 226 candidate `bebdf808fd419165e2b6098bd25d815f7c41c235`.
    Before copying, the coordinator checked two things: that the 5 navigation files edited there were unchanged between
    `bebdf80` and the candidate's parent `0d431aa`, and that none of the 30 new cards existed in the primary checkout. The
    Batch 226 fix touched only 刺す, 強化, 挙げる, 挿す, 裁縫, 飽くまで, 飾り, 餅, 騒々しい, 騒がしい, 驚かす, 高層, 高等 and
    高級; none of them is in this batch's path set.
  - The coordinator byte-compared the 35 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 35 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - No wraps were held from Batch 226, and the coordinator applied none separately; all twelve navigation links were
    copied from the authoring worktree.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 5 files with 12 restored navigation links (two kanji cards and three word cards);
    - `manifest.json` (`contentVersion` `e6f5556bb7dcb4ba`, 4,929 entries);
    - the intake.
- Published baseline recorded in the intake: `7732568ec57a0daa799f081fa4e0968a5c525903` (Batch 226 merge). Parent
  `0d431aa` adds only the Batch 226 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK (the authoring worktree run reported 124 tests);
  - content budget: OK;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 5 files and 12 links, with no problem;
  - title screen: no unguarded exact title-segment overlap (159 stem-only `!!` lines and 28 `OK` lines);
  - link parity: no EN link lost where the RU target exists, and one new RU-only link, 突っ込む→引き出す, which restates
    EN's remark that 引き出す ("pull out") can reverse putting something inside but does not reverse every figurative use.
- Common sample: all three reviewers read all 30 new word cards in full and the five navigation diffs. The correctness
  and comprehensibility reviewers read each card against its full EN original; the consistency reviewer compared front
  matter, links and line counts with EN by script and read EN prose in full only for 突く.
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN, attesting each file, the five navigation diffs, and in full the
    existing RU 入る, 引き出す, 決まり, 印象, 脳 and 預ける.
  - Inspected the Jisho entries of all 30 word families, then streamed the official JMdict English XML: all 49 distinct
    entry ids cited in the cards' source footers are present, and their definitions and spelling annotations were checked
    (for example 句切る rare, 頼母しい search-only, 風船's aerostat sense dated).
  - Japanese sources beyond Jisho: Digital Daijisen entries on Weblio for 入る, 飛び込む, 突っ込む, 漢語, 区切る, the separate
    コレクション【collection】 and 【correction】 entries, 頭脳, 領収, 時間割, 響き and 受取.
  - Russian sources: Gramota and Kuznetsov entries for расписка, апогей, тёплый (figurative sense 5), порядок and further
    definitions (вникать, размечать, разгородить, аэростат, графа, рубрика, поочерёдно, пересуды, пихать, помеха, квитанция,
    граница, предел); Russian Wiktionary мозговой центр and фуросики; the Russian Wikipedia article Ламповый звук for the
    "warm sound" metaphor. Initial rate limits were resolved; oversized outputs were not counted as full reads.
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 cards in full and the complete diffs of the five navigation files; compared front matter, links and line
    counts with EN by read-only script for all 30 cards, and EN prose in full for 突く.
  - Checked the intake's 35 payload paths and hashes against the changed files, that the manifest adds the 30 cards and
    updates the 5 navigation hashes with no missing or extra entry, and that every `.md` hash recomputes.
  - Ran `tools/validate.py` (0 errors). Its `check_content_budget` run timed out and was not completed. It did not
    recheck dictionary entries or JMdict ids.
- Comprehensibility review scope:
  - Read all 30 cards in full against EN, the five navigation diffs, and compared nearby RU titles, including 刺す, 押す,
    叩く, 確実, 堅い and 批判.
  - Used JMdict through Jisho (1456890, 1051540, 1548380 and 1430240), Ozhegov and Gramota пихать and the Gramota /
    Bolshoi tolkovyi slovar entry апогей, from search extracts. It ran `link_parity.py` on the 30 cards; its report records no validator run.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; all three reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time; the coordinator verified HEAD `5cf2313` and a clean tree before each
  launch. Each report records the snapshot `5cf2313` with an empty `git status --porcelain` (the correctness reviewer
  before and after its checks). No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `227-words-batch-66-review-correctness-001.md`
  - `227-words-batch-66-review-consistency-001.md`
  - `227-words-batch-66-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The correctness report says that it read no prohibited reports or records. The consistency report says that it did not
  read author reports, title-screen outputs or batch, draft or tracking records; it read the intake JSON only to check it
  against the diff, which its assignment included. The comprehensibility report says that it did not read batch records,
  author reports or other review reports.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for 飛び込む, 突っ込む and 区切る, **CLEAN** for the other 27 new cards; scoped coverage
**NEEDS FIX** for 飛び込む and 区切る, **CLEAN** for the other 28. Comprehensibility and full quiz/manifest integration were
not assessed.

- C1 (minor, correctness and scoped coverage; high confidence on the omitted qualification), `飛び込む.md:34`: 入る is
  described as entering «без порыва или прыжка». EN says "without requiring a rush or leap": the broader verb does not
  specify those manners rather than excluding them, so the RU wording can teach a false incompatibility with hurried or
  jumping entry. Remedy: «[入る](入る.md)（はいる）значит «входить» в более широком смысле: само слово не указывает,
  происходит ли вход с разбега или прыжком.» Evidence: frozen EN 飛び込む; Digital Daijisen 入る sense 1 (no manner
  restriction) and 飛び込む senses 1 and 3 on Weblio.
- C2 (minor; high confidence), `突っ込む.md:43`: «Основные значения — «ринуться, врезаться во что-то» и «углубиться во
  что-то»; остальные употребления полезно узнавать при чтении.» turns EN's note on "the selected N2 source gloss" into a
  general main-versus-other ranking and demotes the physical insertion the card teaches first. Remedy: delete the
  sentence. Evidence: JMdict 1456940 senses 1–6 (official XML), which give no frequency hierarchy; Digital Daijisen
  突っ込む, which includes putting a hand in a pocket.
- C3 (minor, correctness and scoped coverage; high confidence), `区切る.md:26`: EN's app-local grouping ("The app groups
  this on-first mixed form under kango") became «относят к канго — словам китайского происхождения», adding a blanket
  origin definition that the sentence's own final disclaimer contradicts; kango also includes words coined in Japan.
  Remedy: «В приложении эта смешанная форма с онным началом условно отнесена к канго: …», keeping the disclaimer. Evidence:
  frozen EN 区切る:27; Digital Daijisen 漢語 sense 1 and 区切る on Weblio.

What the reviewer confirmed:
- Front matter is preserved apart from the titles and the added direct 順序→決まり exclusion, which 決まり's title «правило;
  установленный порядок» supports as a conservative ambiguity guard. No EN link whose RU target exists was dropped; the
  new 突っ込む→引き出す link keeps the physical-only reverse-action qualification.
- Japanese examples, readings, constructions, polarity, argument roles and qualifications match EN; the くる viewpoint,
  する/non-する distinctions, mixed readings and godan/ichidan warnings remain explicit. Contextual masculine Russian past
  forms do not assert that the Japanese marks the speaker male.
- No defect was established in «расписка», «мозговой центр» (Wiktionary includes an individual specialist), «фуросики»,
  «порядок» or the warm-sound metaphor (Kuznetsov тёплый sense 5).

Optional: fuller titles for 時間割 («расписание; расписание занятий») and 響き (adding «впечатление от звучания»), since the
bodies keep those senses; 雑音's figurative sense is already explicit in the body; 集金's «собирать счета или взносы» could be
«получать оплату по счетам или собирать взносы».

Limits: bounded editorial review, not native-speaker certification, historical reconstruction, corpus-frequency
measurement or a full quiz audit; the exact frequency of «тёплое звучание» was not established.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; scoped coverage (cross-file integration) **CLEAN**; quiz safety **NEEDS FIX** (two minor
items). Correctness and comprehensibility were not assessed.

- F1 (minor; medium confidence), `境界.md:10`: an RU-only label collision between 境界's «разделительная линия» and 線
  «линия; провод» (EN "boundary" and "line" needed no guard). Remedy: add 線 to 境界's `quiz_exclusions`. The reviewer
  classed it conservative.
- F2 (minor; medium confidence), `雑音.md:10`: 雑音 «помехи (в сигнале)» beside じゃま «помеха; вмешательство». Remedy: add
  じゃま to 雑音's `quiz_exclusions`. The reviewer classed it conservative.

What the reviewer confirmed:
- RU front matter equals EN apart from the titles and the one added exclusion; all EN exclusions are retained.
- Links match EN except absent RU targets left as plain text (点く, 突き当たり, 膨らます, 膨らむ, 乾燥 and the kanji cards 境,
  脳, 領, 預 and 順) and the RU-only 突っ込む→引き出す, whose target exists and which is acceptable. Every link target exists.
- The 12 restored navigation links match EN's positions and path forms, with no prose change.
- The intake's 35 payload paths equal the 35 changed content files and their hashes match; the manifest adds the 30 cards
  and updates the 5 navigation hashes, with no missing or extra entry; all `.md` hashes recompute.
- The only RU-added exclusion at the candidate, 順序→決まり, is **required**: 決まり «правило; установленный порядок» collides
  on «порядок», and 決まり already excludes 順 and 順番.

Optional (low confidence, no fix required): 預かる «хранение» with 保存; 突っ込む «засовывать» with 挿す; 頼もしい with 堅い
«надёжный» and 信頼; 頭脳 with 中心; 突く with 突き当たる. Limits: dictionary entries and JMdict ids were not independently
rechecked; EN prose was compared line by line only for 突く; 118 `strokes/*.json` manifest entries did not equal the
SHA-256 of the working-tree bytes, which the reviewer took to be a CRLF artifact outside the batch (unverified; see the
recheck record); `check_content_budget` was not completed.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** for 突く, コレクション, 頼もしい, 頂点 and 響き (six findings; the other 25 cards
CLEAN on this facet); scoped coverage **CLEAN** for all 30. The incidental navigation edits have no comprehensibility
defect.

- C1 (moderate; high confidence), `突く.md:4`: the title gloss «пихать» is an unqualified colloquial verb whose ordinary
  second sense is stuffing things into a space, not the poke, thrust and cane uses the card teaches; a learner can equate
  突く with 突っ込む or with rude shoving. Remedy: «тыкать; ткнуть; делать выпад», not «колоть» or «толкать», the titles of
  刺す and 押す. Evidence: JMdict 1456890 senses 1–3; Ozhegov пихать 2 «заталкивать, запихивать»; Gramota пихать.
- C2 (minor; high confidence), `コレクション.md:25,33`: learner prose equates the word with English **collection**, tells the
  reader to reconstruct the spelling from English letters and explains the separate borrowing through English
  *correction*. Remedy: drop the English words from the body; the dictionary names may stay. Evidence: JMdict 1051540; the
  RU instruction that learner text must be understandable without English.
- C3 (moderate; high confidence), `頼もしい.md:16` (the example at line 18): «Она надёжный друг» uses «надёжный», the title
  word of 確実 «несомненный; надёжный» and 堅い «твёрдый; надёжный». Remedy: «Она внушает доверие: помогает мне, когда я в
  беде.» Evidence: JMdict 1548380 senses 1–2.
- C4 (minor; high confidence that the note is author-facing), `頼もしい.md:33` (the note at line 34): «написание 頼母しい
  словарь отмечает как встречающееся только при поиске» is dictionary-internal search-only metadata in a learner section.
  Remedy: delete the clause, or «Пишите 頼もしい. Редкое написание 頼母しい не нужно запоминать как обычный вариант.»
- C5 (minor; high confidence), `頂点.md:4`: «апогей» is never used or limited in the body, and its first Russian sense is
  astronomical. Remedy: «пик; высшая точка; вершина (угла)». Evidence: JMdict 1430240 senses 1–4; Gramota / Bolshoi
  tolkovyi slovar апогей 1 (astronomy) and 2 (bookish, highest degree).
- C6 (minor; high confidence), `響き.md:16` (the example at line 18): «звук отлично резонирует» is stronger than いい.
  Remedy: «В этом зале звук хорошо резонирует.» Evidence: EN "Sound resonates well".

Optional: 区切る's «размечать» is not repeated in the body; 突っ込む's «вникать» could carry «(перен.)»; 区域 «территория» and
頭脳 «мозговой центр» are broad or narrow but qualified by the bodies; 雑音:19 renders one 雑音 as both «пересуды» and
«критику» and softens 惑わされず to «не отвлекаясь» (polish, not a missing distinction); 時間割's «Я посмотрел» is weaker than
確認しました («проверил»); 順序 does not name 決まり, but its «порядок» note already excludes tidiness and rules. Limits:
Daijisen's separate correction headword was not reopened; the Russian citations for «пихать» and «апогей» come from search
extracts; not a correctness or quiz-exclusion audit.

## Exclusion classification

All 169 EN exclusion entries (27 lists) are retained in EN order; 風船, 顕微鏡 and 領事 have none. Sixteen of them lie inside
the batch. At the candidate, one direct, one-sided entry was added on one new card; it is not a new list and does not
target a batch word.

| Entries | Author | Consistency reviewer |
|---|---|---|
| 順序→決まり (1) | conservative | required |

The reviewer classed the entry as required because 決まり «правило; установленный порядок» shares «порядок» with 順序
«порядок следования; процедура»; the author had added it as a conservative guard matching 決まり's existing guards on 順
and 順番. The entry is kept either way. The correctness reviewer called it a conservative ambiguity guard without auditing
quiz safety, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions added by the fix and the final verdicts are in
`227-words-batch-66-recheck-001.md`.
