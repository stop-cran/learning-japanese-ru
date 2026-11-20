# Batch 211 — independent review 001

## Snapshot and scope

- Reviewed commit: `53d6950b1b8c0d254414e1f2ba4d967b2ca3b43a` (tree `154fb77da0097183389a794e442bf915ed34d075`), branch
  `full-ru-211-words-50`, parent `eb270c7`. The candidate was committed signed directly and pushed before review.
  - The content was authored in a scratch worktree on the Batch 210 candidate `9d9c00961ef457eac80eb8f37e9ca7e8522245fa`.
    Before copying, the coordinator checked that the 13 navigation files and `words/少年.md` were unchanged between
    `9d9c009` and the published Batch 210 tree and that none of the 30 new cards existed there; after copying, it
    byte-compared all 43 scratch content files between the scratch worktree and the primary checkout.
  - Before the candidate, the coordinator changed three author titles and one definition:
    - 宝石: «самоцвет; ювелирный камень» became «драгоценный камень; самоцвет»; line 16 already said «драгоценный камень,
      самоцвет». The exact segment «драгоценный камень» shared with 玉 is guarded by EN's 宝石→玉.
    - 宿: «место ночлега; постоялый двор» became «место ночлега; гостиница», because «постоялый двор» is dated. The shared
      segment «гостиница» with ホテル is guarded by EN's 宿→ホテル.
    - 完成: «завершённость (работы, изделия); законченный вид» became «завершение (изделия, произведения); законченный
      вид», with line 16 rewritten to match, because 完成 names reaching completion (EN "completion"; Daijisen
      「完全にできあがること」), not a state of completeness. The new segment «завершение» is shared with 仕舞い, so the
      coordinator added the direct guard 完成→仕舞い.
  - The coordinator also restored the link to 少女 in `少年.md:33`, at its EN-linked position, and widened that comparison
    gloss from «девочка» to «девочка, юная девушка». The candidate's 少女 title was the author's «юная девушка».
  - The candidate differs from the published baseline by 30 new word cards, 14 files with 24 restored navigation links
    (13 navigation-only files plus 少年, whose gloss also changed), `manifest.json` (`contentVersion` `d0469eb4b98a4499`,
    4,444 entries) and the intake.
- Published baseline recorded in the intake: `4a479720e9b6f387fabb96c74ffb98530aa5eb4e` (Batch 210 merge). Parent `eb270c7`
  adds only the Batch 210 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers against their EN originals, and the changed
  `少年.md` synonyms line.
  - Correctness also reviewed the other navigation-only diffs (changed passages, not a full re-review of those files),
    the three binding RU instruction and format files, and the relevant frozen EN `n3-vocabulary-sources.tsv` rows. It
    read the comparison cards 女の子, お嬢さん, 彼女, 荷物, 近い, 泊まる, 行う, 仕舞い, 石, 玉, 切符 and 経験 in full;
    other comparison cards were not audited exhaustively. It inspected the live Jisho/JMdict entries for all 30 headwords
    and for 彼女, 近い, 泊まる, 行う, 仕舞い, 経験, 実際, 玉, 正直, 完了, 完全, 未完成 and 荷物. Russian-side evidence came
    from the Kuznetsov entries «камень», «опыт», «близкий», «пожертвование», «взнос», «размещение», «ввести», «график»,
    «законченный», «талон» and «вердикт»; the ru.wiktionary entries «девушка», «узел», «посылка», «судья», «самоцвет»,
    «вообще-то», «благосклонность», «путь», «проездной», «проводить», «выполнять» and «исполнять»; and the Финам entry
    for «исполнение программы», read from raw HTML. Several Gramota requests returned HTTP 429; no conclusion was drawn
    from those failures. It ran `tools/validate.py` (0 errors).
  - Consistency read all 14 navigation diffs, the `manifest.json` diff and the intake path list. It recomputed the
    SHA-256 of every Markdown manifest entry, compared front matter, links and exclusions with EN by script, scanned the
    new titles against every RU word title by exact segment, used `word_title_screen.py` as leads only, ran
    `tools/validate.py` (0 errors), and compared EN and RU link counts to the 30 titles across the corpus. It classified
    every added exclusion. Its JMdict senses for the exclusion pairs came from its own knowledge, not re-opened entries.
  - Comprehensibility ran the link-parity tool on the 30 cards and checked the JMdict entries 1321040 (実行), 1321020
    (実現) and 1593290 (小包) on jisho.org; it cited the Kuznetsov «претворить» entry and the published RU 石, 普通, 札 and
    はあ cards. It did not run `tools/validate.py`. Its report mentions title-screen overlaps only as leads; the prompt
    offered the screen tool among the optional tools, and the report does not say which output it saw.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD was still `53d6950`
  and that `git status --porcelain` was empty. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator and named the report as the only file a
  reviewer writes. The correctness and consistency reports state that no generator was run; the comprehensibility report
  states that the manifest was not regenerated, and its recheck states that no generator was run. The coordinator found
  the tree clean after each review.
- Full blind reports:
  - `211-words-batch-50-review-correctness-001.md`
  - `211-words-batch-50-review-consistency-001.md`
  - `211-words-batch-50-review-comprehensibility-001.md`
- Initial reviewers were told not to read the author report or prompt, the coordinator's title-screen output or notes, the
  batch records, or one another's reports; the correctness and consistency reports confirm this.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (包み); scoped coverage **NEEDS FIX** (包み, 宝石, 少女, パス). No other actionable defect
was established in the reviewed passages.

- C1 (minor, high confidence), `包み.md:29`: «[荷物] включает багаж и посылки, завёрнутые так или иначе» presupposes
  wrapping and drops EN's "whether wrapped this way or not", the very boundary the comparison teaches. Evidence: frozen EN
  `包み.md:29`; RU `荷物.md:15,25,29`; JMdict 荷物 sense 1 (luggage, baggage, package) has no wrapping restriction.
  Remedy: «…независимо от того, завёрнуты они таким образом или нет».
- C2 (minor, high confidence on the omitted distinction), `宝石.md:18–19`: both examples render 宝石 with bare «камень» /
  «камни», the whole title of 石, although EN says "gemstone/gems" and the card teaches the 宝石/石 boundary. Kuznetsov
  «камень» sense 2 does allow a jewelry stone, so the renderings are intelligible; the finding concerns the taught
  distinction, not Russian grammaticality. Remedy: «драгоценный камень», «драгоценные камни».
- C3 (minor, medium-high confidence), `少女.md:4,12`: the title «юная девушка» omits the childhood part of the selected sense,
  while the body says «девочка или юная девушка» and the first example is a twelve-year-old. Evidence: frozen EN
  `少女.md:4,16,18`; JMdict 少女 sense 1 "girl (usually 7–17); young lady"; ru.wiktionary «девушка» sense 1. Remedy:
  title and H1 «девочка; юная девушка».
- C4 (minor, high confidence on the omission, medium on the wording), `パス.md:4,12`: the title lists the ball, exam and
  file senses but omits the admission pass and passing one's turn, which EN's broad "pass" and RU lines 16 and 34 teach.
  Evidence: JMdict パス senses 1–4 and the separate computing entry. Remedy proposed: «пас; сдача экзамена; пропуск
  (документ; хода); путь к файлу», keeping the pass/path explanation.

Optional notes: kana for the RU-only 訓練を行う in `実施.md:29`; links to existing 彼女 (少女:29), 行う (実施:29, 実行:29),
実際 (実は:29) and 玉 (宝石:29) in RU-added comparisons; and «билет» in 券's title, without claiming «талон; купон» is
wrong. Limit: whether 小包's postal-only title «почтовая посылка» was too narrow remained **UNVERIFIED**; JMdict's
"parcel; package" and the Russian «посылка» entry did not settle it.

The reviewer found original metadata and EN exclusions preserved, every EN full-stop example retained, no dropped EN link
with an existing RU target, and the 少年 change accurate. It did not call «вердикт» in 審判's title false: Kuznetsov
restricts it to juries, but JMdict 審判 sense 1 includes "verdict" and the body explains the broader decision sense.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **CLEAN**; cross-file integration **CLEAN**. No findings.

- Front matter of all 30 cards equals EN apart from the translated titles and the added exclusions; all EN exclusions are
  retained. No card has a Russian-only link; the EN links missing in RU are exactly the ten whose RU targets do not exist
  (kanji 麦, 象, 泊; words 学ぶ, ところで, お願いします, 信じる, 信用, 完了, 完全), each left as plain text. The corpus scan found
  no dropped link to the 30 titles whose RU target exists.
- The 24 restorations in the 14 files match the specified distribution; after link markup is removed, 13 files are
  byte-identical in prose to the parent, and 少年 differs only in the gloss. The manifest adds 30 entries and changes 14,
  and every Markdown hash matches its file; the 44 intake paths are exactly the content diff.
- Exact title segments are shared only by 密/親しい/近い «близкий», 宿/ホテル «гостиница», 宝石/玉 «драгоценный камень» and
  完成/仕舞い «завершение»; each pair is guarded on at least one side.
- Optional guards: O1 定期→期間, O2 実験→試験, O3 パス→道, O4 小屋→家 (or dropping «домик»). O5: the «девушка» stem in
  少女, 彼女 and 恋人, and «размер» in 小 and 大小, are distinguished by qualifiers. O6: the 少年 gloss follows the new 少女
  card. EN declares none of O1–O4.
- Limits: the raw SHA-256 of 110 `strokes/*.json` files does not match the manifest; the reviewer could not explain this
  without running the generator. The manifest hashes text after CRLF→LF normalization, as recorded in Batch 209.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (パス, 実行, 定期, 宝石, 少女, 対, 密); scoped coverage **CLEAN**. The other 23 cards
and the 少年 line are clean.

- K1 (minor, high confidence), `パス.md:16,26`: the two-word split is labelled with bold English **pass** / **path**, and
  line 26 says English pass and path converge, so a learner without English cannot see why the computing noun is a
  separate word. All senses are present, so this is not a coverage gap. Remedy: state the split in Russian.
- K2 (minor; high confidence that the pair does not contrast, medium that the gloss exceeds the Japanese),
  `実行.md:18,21` with `実現.md:19,29`: 実行します is «претворим этот план в жизнь» and 実現しましょう is «воплотим этот план
  в реальность». Kuznetsov «претворить» sense 2 is «воплотить во что-л. реальное», the end state the card assigns to 実現,
  so the paired examples fail to show the card's contrast. Remedy: «выполним этот план»; 実行に移す «перейти к делу».
- K3 (minor, high confidence), `定期.md:29`: the 普通 contrast works only through English "regular" and implies that 普通
  sometimes means "on schedule"; Russian «регулярный» means periodic, never «обычный» (普通's title).
- K4 (minor, high confidence), `宝石.md:16,18,19`: definition and examples use 石's title «камень», undoing the gem/stone
  split; the reviewer proposed «самоцвет».
- K5 (minor; high confidence that the clauses are author-facing, medium that they should go despite the series pattern),
  `少女.md:33`, `対.md:34`, `密.md:33`: source-list clauses sit in learner text, and 少女 names «девственница», adding the
  very gloss the card rejects. Remedy: delete the clauses, keeping the rules and the ritsuryō age note.

Optional notes: the 少年 gloss needs no fix; 少女's title is narrower than the examples' «девочка»; 宜しく's title is stiff;
«омограф» in `パス.md:34` is unexplained; 家賃 and 実は name wago/kango; 小包's «почтовая посылка» is narrower than JMdict
"parcel; package". The reviewer found no Cyrillic transliteration of a reading and no learner sentence about app quiz
mechanics.

## Exclusion classification

All 25 EN exclusion entries (14 lists) are retained. At the candidate, seven direct, one-sided entries were added on seven
new cards; the consistency reviewer classified all seven and found none unjustified:

| Entry | Author or coordinator | Consistency reviewer |
|---|---|---|
| 密→近い | required (shared «близкий») | required |
| 宿→泊まる | conservative | conservative |
| 宿泊→泊まる | required | required, or at least strongly justified |
| 実施→行う | required | required |
| 実行→行う | conservative | conservative |
| 実現→実行 | conservative | conservative |
| 完成→仕舞い | required (coordinator; shared «завершение») | required |

The correctness reviewer checked the Japanese side of the added pairs for relevant lexical overlap without auditing the
exclusions exhaustively; the comprehensibility reviewer did not score them.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`211-words-batch-50-recheck-001.md`.
