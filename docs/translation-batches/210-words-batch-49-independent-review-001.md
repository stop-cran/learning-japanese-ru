# Batch 210 — independent review 001

## Snapshot and scope

- Reviewed commit: `9d9c00961ef457eac80eb8f37e9ca7e8522245fa` (tree `6ee737bce5f742105ab95f7cffbfb99f12dd0bde`), branch
  `full-ru-210-words-49`, parent `f28fc34`. The candidate was committed signed directly and pushed before review.
  - The content was authored in a scratch worktree on the Batch 209 candidate `5f015601f1ff714f7c63b0edfa85215c8f99f071`.
    Before copying, the coordinator checked that the 22 navigation files were unchanged between `5f01560` and the published
    Batch 209 tree and that none of the 30 new cards existed there; before committing, it byte-compared all 52 content files
    between the scratch worktree and the primary checkout.
  - The coordinator made no content change to the author's output before the candidate. The author's last change before
    handing over dropped «кровля» from 屋根's draft title «крыша; кровля», because ru.wiktionary marks «кровля» as книжн.;
    the candidate title is «крыша».
  - The candidate differs from the published baseline by 30 new word cards, 22 navigation-only files (35 restored links),
    `manifest.json` (`contentVersion` `101a57ab85e1681f`, 4,414 entries) and the intake. The candidate intake's note
    miscounted the restorations as twenty-three; the fix commit corrected it to thirty-five. The payload paths and hashes
    were unaffected.
- Published baseline recorded in the intake: `26120f88e4c9f4a20889c222a329d94894ad3566` (Batch 209 merge). Parent `f28fc34`
  adds only the Batch 209 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards, read in full by all three reviewers against their EN originals.
  - Correctness inspected every changed passage of the 22 navigation-only files (changed-passage review, not a full
    re-review of those files) and the binding RU instruction and format documents. It checked the titles and relevant
    passages of the comparison cards 老人, 等しい, 帰る, 帰り, うとうと, いる, いらっしゃる, おいでになる, 参る, 習う, 座る, 世界, 職,
    職業, 店員 and 男の子 without fully re-reviewing them, and read the frozen EN source-list rows for 帯, 就職 and ボーイ. It
    queried the Jisho/JMdict entries for all 30 written forms and the comparison words, the Digital Daijisen entries 居眠り,
    おび, おる (sense 5) and 平均 (sense 3), 日本大百科全書 国籍, and the cited 着く and 就く seating entries. Russian-side
    evidence came from the Kuznetsov entries «национальность», «невольный», «дремота», «опоясать», «полоса», «мир» (both
    homonyms), «трудоустройство», «служащий» and «скромный»; where Gramota search pages failed, it used the entry pages or
    raw entry HTML instead of search summaries. It ran `tools/validate.py` (0 errors).
  - Consistency read all 22 navigation diffs in full, recomputed the SHA-256 of every changed manifest entry, checked the
    intake's path list and candidate hashes, ran `tools/validate.py` (0 errors) and the link-parity tool on the navigation
    files, screened the new titles against every RU word title by exact segment, read the titles and exclusions of about 75
    comparison cards, and scanned `words/`, `kanji/` and `articles/` for EN/RU link-count differences for the 30 titles. It
    classified every added exclusion. Its JMdict senses for the exclusion pairs came from the cards' cited sources and its
    own knowledge rather than fetched entries, and it relied on the prompt's statement of the app's exclusion contract
    without reading `Words.kt`.
  - Comprehensibility read the link text of the 22 navigation restorations, checked comparison-card titles without
    rereading those cards, ran the link-parity tool on the 30 new cards, and cited the published RU 乗り物, 様, 次第,
    ベッド and カーテン cards for convention. Its evidence included the Digital Daijisen おる senses 3 and 5 and the JMdict
    entries 1231890 (居眠り), 1410410 and 1410420 (帯), 1331670 (就職) and 1331840 (州). It does not report running the
    validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent listing exposed these assigned model variants. Reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time. Before each next review, the coordinator checked that HEAD was still `9d9c009`
  and that `git status --porcelain` was empty. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator and named the report as the only file a
  reviewer writes. The correctness and consistency reports state that no generator was run; the initial comprehensibility
  report does not mention generators, and its recheck states that none was run. The consistency reviewer also wrote a
  temporary dump, `b210-cons-scratch2.txt`, in the coordinator's session folder outside the repository and deleted it
  afterwards; its report discloses this. The coordinator found the tree clean after each review.
- Full blind reports:
  - `210-words-batch-49-review-correctness-001.md`
  - `210-words-batch-49-review-consistency-001.md`
  - `210-words-batch-49-review-comprehensibility-001.md`
- Initial reviewers did not read the author report, the author prompt, the coordinator's title-screen output or notes, or one
  another's reports.

## Initial verdicts and findings

### Correctness

Verdict: correctness **NEEDS FIX** (差別, 居眠り, 帯; the other 27 cards clean); scoped coverage **NEEDS FIX** (岩, 帯; the
other 28 cards clean).

- C1 (minor, high confidence), `差別.md:20`: 国籍 is rendered «национальность», which ordinary Russian reads as ethnic
  affiliation (Kuznetsov sense 1), whereas 国籍 is citizenship or state membership (JMdict "nationality; citizenship";
  日本大百科全書 国家の構成員であることを示す資格). Remedy: «Нельзя дискриминировать людей по гражданству.»
- C2 (minor, high confidence), `居眠り.md:4,12,16,21`: the title «невольный сон» and the definition «сам того не собираясь»
  make unintendedness part of the word, which contradicts line 21, where the regretted result comes from てしまいました.
  Evidence: JMdict "nodding off (while sitting); dozing"; Daijisen 座ったり腰かけたりしたままで眠ること. Remedy: title and H1
  «дремота; сон сидя», with a neutral definition.
- C3 (minor, high confidence for the omission, low impact), `岩.md:33`: EN's note that music called "rock" is ロック is
  omitted. The Russian rock/boulder explanation is not wrong, but the Japanese vocabulary point is lost. Evidence: frozen EN
  `岩.md`; the JMdict ロック entry whose first sense is rock music. Remedy: one Russian sentence naming ロック.
- C4 (minor, high confidence), `帯.md:4,11,15–17`: «опоясывающая полоса» / «полосу, охватывающую что-либо» narrows EN's
  "band or strip" to things that encircle something. Evidence: JMdict おび sense 3 "band; belt; strip"; Daijisen おび sense
  3 1に似た形のもの (shape-based), with 帯紙; Kuznetsov «опоясать» sense 2 and «полоса» senses 1–2. Remedy: title and H1
  «пояс кимоно; длинная узкая полоса», and a shape-based line 17.

The reviewer checked all 60 Japanese example sentences as exact retained strings, found original metadata and exclusions
preserved, and found no EN link to an existing RU target lost; it raised no finding against the changed navigation
passages. It confirmed that the 帯 and 就職 source-list passages do not claim to recover the compiler's intention and that
ボーイ adds no unsupported provenance claim. No optional notes.

### Consistency and quiz safety

Verdict: consistency **CLEAN**; quiz safety **NEEDS FIX** (one missing guard; the rest optional); cross-file integration
**CLEAN**.

- F1 (minor, medium confidence), `屋根.md` front matter: Russian «крыша» also names the rooftop («пойти на крышу»), so with
  屋上 «площадка на крыше» shown, 屋根 «крыша» is a defensible answer. EN's distinct glosses (roof/rooftop) prevented the
  overlap in EN, so EN declares no guard. Remedy: `quiz_exclusions: [屋上]` on 屋根.
- Front matter of all 30 cards equals EN apart from the translated titles and the added exclusions; all EN exclusions are
  retained. Every RU card's link set is a subset of EN's, all relative links resolve, and the dropped links (一生, 公平, ベルト,
  少女 and kanji 巨, 根, 岩, 届) have no RU target. Every navigation change is a bracket or href at an EN-linked position, with
  no prose, whitespace or line-ending change, and the corpus scan found no remaining EN/RU link-count difference for the 30
  titles. The manifest diff is `contentVersion`, 22 modified hashes and 30 new entries, each matching its file; the 52
  intake paths are exactly the content diff, with matching hashes.
- Exact title segments are shared only by 年代/時代 «эпоха», 常に/いつも «всегда», 平和/世界 «мир», 居る/いる/いらっしゃる/
  おいでになる «находиться»/«быть» and ボーイ/少年/男の子 «мальчик»; every such pair is guarded on at least one side.
- Optional: O1, `居る.md`: the 参る entry has no shared sense with 居る ("be"), only the humble register; dropping it would
  keep the distractor pool larger, but retention is harmless. O2, 差別↔区別/違い (差別's neutral sense «различие» is taught in
  the body); O3, 常に↔いつでも; O4, 帰宅↔戻る. EN declares none of O2–O4.
- Limits: `kanji/和.md` (link to 味) and `kanji/居.md` (links to いる and 今) carry RU-only links that are identical in parent
  `f28fc34` and untouched by this batch. A raw SHA-256 of 118 `strokes/*.json` files does not match the manifest; the
  reviewer attributed this to the generator's line-ending normalization without investigating further. The manifest hashes
  text after CRLF→LF normalization, as recorded in Batch 209.

### Comprehensibility and scoped coverage

Verdict: comprehensibility **NEEDS FIX** (帯, 就職, 居る, 居眠り, 年寄り); scoped coverage **CLEAN**. The navigation
restorations have no comprehensibility defect.

- M1 (minor, high confidence), `居る.md:33`: «основа на -masu + おる» names the contempt construction with an English label,
  so an English-free beginner cannot separate it from humble おる and ～ております. Published RU cards use «ます-основа»
  (`様.md:18`, `乗り物.md:26`). The reviewer also proposed adding a 負け + おる example.
- M2 (minor, high confidence), `帯.md:42-45`: after the おび/たい warning, four lines narrate the source list and the
  compiler's unclear intention, which does not help a beginner use 帯. Remedy proposed: keep the warning and replace the
  provenance with a dictionary-lookup hint.
- M3 (minor, high confidence), `就職.md:32`: after correctly rejecting inauguration and opening-ceremony senses, the card
  cites the source list's English gloss and the compiler's unknown intention. Remedy proposed: keep only the first sentence
  and the employment sense.
- M4 (minor, high confidence), `居眠り.md:19`: «не спите на уроке» uses the general «спать», the quiz title of 寝る and 眠る,
  and contradicts the card's own "dozing while sitting" note. Evidence: JMdict 1231890 "nodding off (while sitting);
  dozing".
- M5 (minor, high confidence that the glosses collide; medium that a learner would merge the words), `年寄り.md:19-20`,
  set up at 16 and 32: line 32 names «пожилой человек» as 老人's title, and both examples then gloss お年寄り with that same
  label, so the examples do not show the distinction the synonyms section announces.

Optional notes: `ボーイ.md:25` could reduce the English-uses clause to a parenthetical «мальчик»; `年月.md:29` "wago" is
glossed and not blocking; `差別.md:19` «как покончить» slightly narrows ために, following EN; `州.md` renders JMdict
"continent" as «часть света», and a one-clause contrast with 大陸 would be optional because EN has none. The reviewer found
no Cyrillic transliteration of a Japanese reading and no learner sentence about app quiz mechanics.

## Exclusion classification

All 26 EN exclusion entries (16 lists) are retained. At the candidate, the author had added twelve direct, one-sided
entries on seven new cards; the coordinator's notes agreed with the author's classification:

| Entry | Author and coordinator | Consistency reviewer |
|---|---|---|
| 年寄り→老人 | required | required |
| 平和→世界 | required | required |
| 帰宅→帰る | required | required |
| 帰宅→帰り | conservative | conservative |
| 平等→等しい | conservative | conservative |
| 居眠り→うとうと | conservative | required |
| 居る→いらっしゃる | required | conservative-leaning-required |
| 居る→おいでになる | required | conservative-leaning-required |
| 居る→参る | conservative | unjustified (optional removal, O1) |
| 就く→習う | required | required |
| 就く→就職 | required | required |
| 就く→座る | conservative | conservative |

The classification differences do not change any guard except 居る→参る. The correctness reviewer inspected the Japanese
side of the added pairs and the comparison cards' relevant passages; it did not audit exclusions exhaustively.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`210-words-batch-49-recheck-001.md`.
