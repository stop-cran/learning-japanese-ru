# B256 — scoped rechecks at the signed learner fix

The [initial review and dispositions](256-words-batch-95-independent-review-001.md) concern candidate `599b9e5b657468ea8c26bd651fe5cc9a4493ce64`. All rechecks below concern its signed child `ce3a9636e75286046db0c050b9a338a704d8f3b3`, tree `c27d61e7e15dcdefe0bbccdff0acdcd98ab58251`, with frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. Each reviewer returned every complete word diff for the 16 changed words. The other 14 new words and seven navigation edits were not re-audited. The 63 Japanese sentence/reading blocks did not change. Full public reports follow; their hashes identify the original UTF-8 report bodies, not stdout wrappers or the full file. Each report also appeared in read-only tool output.

**Order and reviewer identity.** The original Claude correctness reviewer finished its follow-up before the original Grok comprehension reviewer received its follow-up. Both `write_agent` and `read_agent` for the exact original GPT consistency ID `62b1adc2-db43-40ba-a9f7-fee0fda60ef1` returned “No agent found”; no recheck was dispatched to that ID. Its original report was retained. After Grok's last response and observed idle notification, the coordinator-authorized fresh consistency instance `2ce1cec7-3737-4c18-a0e0-76cf325340e3` started at 03:49:57.277Z. The complete original brief and verbatim report, same source/comparison access, and all cumulative fix diffs were supplied; their returned text was checked. Its first dispatch, all responses and the report identify `gpt-6.2-astra`. This was a **replacement recheck, not an original-agent recheck**, and not a repeated blind review. For the two original follow-ups the end time is the final report's `assistant.turn_end` followed by the observed idle notification, not a second `subagent.completed` event.

**Outcome.** Correctness F1–F5, comprehensibility F1–F4, and consistency F1–F5 resolved on the same fix. The supplementary initial report's findings are addressed in the reconciliation, not counted as a fourth recheck. No further change to learner bytes was necessary. The optional caution about 東洋's last sentence is retained as optional: the preceding sentence explicitly marks the sense as dated and used in China. The softer criticism of さすが's ability wording and the incidental overlap of 果たして with already excluded やはり/やっぱり do not reopen a finding. The evidence does not establish runtime distractor behavior, learner or device outcomes, frequency, publication or release readiness.

**Tooling-only stage.** After the last learner recheck, signed `ccf6702840837f57cb31331dd04d4f4f7e3c386c` changed exactly four files: counter validator and test, format reference and B012 choice-preservation guidance. The language-aware v1 check requires `translation` in RU, preserves legacy EN `en`, rejects both aliases together, and leaves v2 processing separate. No counter card was translated. All 5,799 manifest payloads and the raw manifest stayed as at the learner fix (manifest SHA-256 `1b2d9c4188514b74d83bad730df781f8b97aa1b10bd954b994b0d332e9e6936c`). At both stages the four serial gates passed: manifest `5481a3ac3cb1e345`, validator 0 errors, 124 tests, ZIP budget 8,422,089 bytes. The [final validation](256-words-batch-95-final-validation-001.json) separately identifies the signed records revision tested.

## Correctness — original reviewer

`6ea4c257-32b0-4378-b463-653132a6d129` · `claude-opus-5.5` (24 responses); 2026-11-24T03:30:52.881Z – 2026-11-24T03:44:27.703Z. Contiguous cumulative diff blocks: 16/16. Verbatim report body: 8713 UTF-8 bytes, SHA-256 `bbb79466a8c94670b7b0e08719c4a21618b8ce210656b82f748f8a0487c8a3be`.

B256-FIX1-CORRECTNESS - original-reviewer recheck (read-only)

SNAPSHOT
- RU candidate ce3a9636e75286046db0c050b9a338a704d8f3b3, tree c27d61e7e15dcdefe0bbccdff0acdcd98ab58251, parent 599b9e5b657468ea8c26bd651fe5cc9a4493ce64 (my blind candidate); signature G (Roman Konstantinovskiy); "Reconcile B256 wording and direct quiz exclusions", 2026-11-24T04:30:23+01:00. HEAD = candidate; `git status --porcelain --ignored` 0 lines at start and end; no uncommitted files.
- Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f, clean.
- Runtime model ID/metadata: not available to me; not guessed.
- No edits, no agents. Disclosure: one early helper script contained json.dump(..., open("NUL","w")) (Windows null device); verified that no file was created and the worktree stayed clean.

SCOPE
- 599b9e5..ce3a963: 17 files (manifest.json + 16 words/*.md), 53+/55-. All 16 packet diffs in b256-recheck-fix1 returned completely (4 per call, untruncated); each is byte-identical to `git diff -U2 599b9e5 ce3a963 -- words/<w>.md`.
- manifest.json: contentVersion + 16 hash lines; sha256 of all 16 new blobs matches (0 mismatches). Not otherwise reviewed.
- 7 navigation files and 14 other cards: empty diff; not re-reviewed.
- Full RU/EN pairs: 果たして, 櫛. Changed lines with context vs EN (parent where relevant): 山林 L12-34 (parent L19/27/31); 本来 L18-22, 36; 有無 L18-24; 朗らか L9, 19; さすが L16-20, 24-29, 42-46; 東洋 L1-48 (parent L41-46); 枚数 L1-23 (parent L18/23); 桁 L16-23, 37-41; 構造 L42-44; 枕 L16, 27-30; 校舎 L36-41; 次ぐ L9, 48-49; 末っ子 L9; 欄 L9, 17, 22. Declined optionals rechecked: 欠伸 L25-29, 東西 L4-21, 未満/以下/以内 front matter.
- Archived JMdict packets (b256-blind/dictionary): 東洋 1448230, 欄 1549350, 山林 1303230, 桁 1253800, 枕 1524860; from blind pass 果たして 1600780, さすが 1552390, 本来 1523270, 有無 1541610, 朗らか 1560710.
- Front-matter diff of the 16 cards; title/exclusion scan of all 4333 words/*.md at ce3a963 around the changed pairs.

FINDING STATUSES
- F1 山林:31 - RESOLVED. «Выбирайте перевод по контексту: при описании пейзажа это может быть «лес в горах», а когда речь идёт об использовании земли — «лесные угодья».» Direction is now context -> translation; keeps EN's no-altitude point, land-use sense and the unforested-山 caveat. Aggregate (title «лесистые горы; лесные угодья», L16, L18 «лесные угодья», L19 «горный лес», L27 new link [森林](森林.md), target exists) fits JMdict 1303230 s1 "mountain forest; forest land; woodland", s2 "mountains and forests".
- F2 本来:18 - RESOLVED. «Это не изначальная цель.» is no longer a past-time adverb. L19 «По идее, сегодня должен быть выходной.» and L36 «...речь об ожидании, а не о прошлом» match EN L19/36.
- F3 有無:21 - RESOLVED. «Работу навязали, не дав даже возразить.» Indefinite agent as in EN "They imposed..."; no added recipient; idiomatic; consistent with L23-24.
- F4 朗らか - RESOLVED. L9 adds 楽しい; L19 «Дети весело засмеялись.» (EN "laughed cheerfully") makes the guard more pertinent.
- F5 さすが:27 - RESOLVED. «Обычно さすが пишут каной. В словаре встречается и написание 流石: всё сочетание читается さすが.» No origin claim; L28-29 keep the irregular-reading warning; consistent with JMdict 1552390 (gikun/jukujikun reading, kana usual).

BOUNDED VERDICTS (16 changed cards: changed lines plus needed context)
- Japanese correctness: CLEAN.
- EN->RU coverage: CLEAN.
- Russian meaning preservation of changed lines: CLEAN (one optional note).
- Quiz-exclusion dispositions: CLEAN (acceptable).
- Navigation and 14 unchanged cards: unchanged.
In this bounded scope, no fixable defect was found; this does not certify whole cards.

CHECKED CHANGES
- 果たして L4/L12 «как и ожидалось; в самом ли деле (в вопросе)» = JMdict 1600780 s1 "as was expected; sure enough" + s2 "really... (interrogative)"; same order as EN "sure enough; really?". Body «и правда» (L20, L42) remains a valid s1 ("sure enough") rendering.
- さすが:20 «Даже учитель при всём своём умении растерялся...» renders さすがの...も (s3 "even..."). L45 adapts EN's English-"still" note accurately; まだ/じっと links kept.
- 次ぐ:48-49 now unambiguous (a rank by one measure need not hold by population vs area).
- 桁:20-21 accurate (六桁 = six digits; 三桁の数 = three-digit number). 桁:39 is non-categorical, fits JMdict 1253800 s1 beam/girder (+"column") vs s2 digit/order of magnitude, and covers EN L39.
- 構造:44 non-categorical («не любой декоративный рисунок или узор»); EN's English-"pattern"-gloss framing reasonably adapted.
- 枚数:18 parallels EN "number of copied sheets"; :23 accurate (枚 counts thin flat items + 数).
- 枕:16 rakugo lead-in = JMdict 1524860 s2 "introduction (e.g. to a rakugo story); lead-in"; :29 gloss equals はじめに's current title «для начала; вступление (в книге)».
- 櫛:32 correctly describes both examples (櫛で髪をとかしました; 櫛をかばんに入れておきました) and avoids EN L32's "を marks the hair" over-generalization for example 2.
- 校舎:39-40 = EN L39-40. 東洋:43-44 match JMdict 1448230 s2 "Japan" [dated; used in China]; dropping EN's English "the Orient" remark is acceptable.

EXCLUSION DISPOSITIONS
- 果たして -実は: 実は «на самом деле; вообще-то» is declarative/disclosing; the new title marks expected-outcome and interrogative use, and 果たして's title fails for 実は. Accept.
- 果たして keeps 実に («действительно» can render "sure enough" or "really?"): reasonable conservative guard. まさに «именно; поистине; вот-вот» not added: as a whole title neither interrogative nor expected-outcome. Accept.
- New «как и ожидалось» stem: やはり/やっぱり (same phrase), さすが, 本当, 実際, 現に already excluded; はず «ожидается; должно быть», 案外/意外 (contrary), 予期/期待 (nouns) are not reasonable either-direction answers.
- 次ぐ -占める: «следовать за...; занимать следующее место» vs «занимать (долю, место)» = succession vs occupying a share/place; EN has no pair. Accept; residual risk via 第二位を占める-type use is not demonstrated.
- 枚数 -枚: count vs counter; EN parity. Accept.
- 末っ子 +子: «ребёнок» is a plausible answer for 末っ子; parity with 子供. Accept. 弟/妹 are gender-specific relative terms; not needed.
- 欄 +ページ: JMdict s1 glosses include "page"; L22 スポーツ欄. Accept.
- 東洋 +東: «восток» is a plausible short answer for 東洋. Accept. 東西 «восток и запад» is not a reasonable match.
- Declined optionals, not material: 欠伸:27 stays an explicitly labelled memory aid; 東西 title omits the cultural sense but L16/L19 supply it; 未満/以内: titles state the boundary explicitly («не включая границу» vs «не более»), and 未満's list equals EN. Note that 以下 is equally inclusive, so "inequality differs" does not distinguish it from 以内; the outcome is unchanged.

OPTIONAL (non-blocking)
1. 東洋:45 «Для современного японского это не основное значение.» can suggest a live secondary modern sense, whereas JMdict marks it dated and used in China. EN-parallel wording: «В современном японском 東洋 обычно не означает одну Японию.» Confidence low-medium.

LIMITS
- The recheck is limited to the 16 changed cards (changed lines plus the context needed to judge them). Unchanged lines elsewhere in those cards, the 14 unchanged cards and the 7 navigation files were not re-reviewed.
- Dictionary evidence is the archived JMdict packets; Daijisen/weblio were not re-fetched. Glosses do not by themselves prove Russian naturalness or frequency.
- The overlap scan is regex-based over titles/exclusions; it shows candidates, not learner behavior. Link-parity policy for the added 森林 link was not assessed.
- No native-speaker, learner, device or release claims.

## Russian comprehensibility — original reviewer

`3749ffd7-8b4a-4efc-8740-346de4c8f21e` · `grok-4.7` (11 responses); 2026-11-24T03:45:47.733Z – 2026-11-24T03:49:32.044Z. Contiguous cumulative diff blocks: 16/16. Verbatim report body: 5602 UTF-8 bytes, SHA-256 `0c4f914baa54485f9485f1d284c21c6e78087da10c18e0a3a6783863ec9119d2`.

# B256-FIX1 comprehension recheck

Snapshot: fix ce3a9636e75286046db0c050b9a338a704d8f3b3 (tree c27d61e7e15dcdefe0bbccdff0acdcd98ab58251), parent 599b9e5b657468ea8c26bd651fe5cc9a4493ce64. EN frozen 6af98cb717755690a9ca793e5454a96ebd7a8f9f unchanged. Runtime model id: not supplied.

## Scope

Read in full, via tool output, all 16 diffs in b256-recheck-fix1, in groups of four: さすが, 構造, 東洋, 本来; 校舎, 朗らか, 枕, 櫛; 果たして, 次ぐ, 山林, 有無; 末っ子, 枚数, 桁, 欄. No checksum substitute. Extra read-only git show at the fix commit, titles only: はじめに, 実に, 実は, やはり, やっぱり, さすが, 果たして. Not reread: 14 unchanged cards (欠伸, 機関車, 楕円, 森林, キャンパス, 校庭, 枯れる, ナンバー, 東西, 来日, 杉, 本部, 未満, 望遠鏡), seven old navigation diffs, dictionary JSON, frozen sources, other reviewer reports.

## Original findings

F1 さすが.md:45 «still» — FIXED. New text: «Здесь «всё же» выражает уступку. まだ означает «всё ещё, до сих пор», а じっと может описывать неподвижность. Это три разных значения.» English is gone; the three-way contrast and the links remain. No regression in this sentence.

F2 本来.md:18 — FIXED. Example is now «Это не изначальная цель.» Present and attributive, matching これは本来の目的ではありません and EN «This is not the original purpose.» Related edits stay consistent: «По идее, сегодня должен быть выходной» and «по идее, это должно получаться… речь об ожидании, а не о прошлом.» No regression.

F3 構造.md — FIXED. «構造 может обозначать схему расположения частей, но не любой декоративный рисунок или узор.» The English word pattern is gone; the warning against a decorative узор remains. No regression.

F4 東洋.md — FIXED. «the Orient» is gone. The new paragraph still says the «страны Востока» sense is not one country, that boundaries varied by period, and that the dated Chinese use «Япония» is not the modern default. quiz_exclusions now also lists 東; that is metadata, not a prose defect. No regression.

## Verdicts

- Changed-text Russian comprehensibility: CLEAN
- Scoped coverage of these 16 diffs against the paired EN senses: CLEAN
- F1–F4: all FIXED, none reopened
- New 果たして label and 櫛 particle contrast: CLEAN
- Unchanged cards and old navigation diffs: not re-audited

## Assessed changes, no defect

果たして title/H1 is now «как и ожидалось; в самом ли деле (в вопросе)». Full label stays intelligible and distinguishable from current labels やはり / やっぱり «всё-таки; как и ожидалось», さすが «как и следовало ожидать; даже такой», 実は «на самом деле; вообще-то», and 実に «действительно; очень». The shared phrase «как и ожидалось» is not the whole label; the question clause separates it. Exclusion swap 実は → 実に is not learner-facing prose. The unchanged example still has «и правда»; that is the same confirmation sense, not a contradiction.

櫛 now contrasts the two examples: 櫛で / 髪を in the first (instrument vs what is combed), 櫛を in the second (the comb itself is put in the bag). This describes the Japanese role of で and を, not a Russian case. The ban on 櫛する remains. Improvement, not a regression.

校舎 now names the person entering the building. 朗らか example is «Дети весело засмеялись», matching EN. 枕 explains ракуго as «японском искусстве устного рассказа», and the はじめに quote now matches that card’s title «для начала; вступление (в книге)».

Other prose edits keep the EN point and are clearer: 次ぐ (one ranking measure does not fix the others); 山林 («горный лес» plus an explicit landscape vs land-use choice, and a link to 森林); 枚数 («количество скопированных листов»); 桁 («шесть цифр», «трёхзначное число», beam vs digit place). 有無 «Работу навязали, не дав даже возразить» matches EN «without allowing any objection»; the next unchanged sentence still teaches consent-or-refusal. Metadata-only diffs (末っ子 adds 子; 欄 adds ページ; 枚数 drops 枚; 次ぐ drops 占める) are not new learner prose.

## Optional

- 果たして’s first clause repeats the phrase in やはり’s label and no longer uses the example’s «и правда». Full labels still differ. Not a collision finding.
- さすが example now says «при всём своём умении». That highlights ability; the next sentence still includes положение. Mild narrowing, not a blocker.
- さすが:41 «даже мне», the Latin binomial, and links to unavailable targets are unchanged, as stated. Not reopened.

## Limits

CLEAN means no confirmed defect in the changed learner text of these 16 diffs, not a native-speaker certification and not a second audit of unchanged cards. Japanese dictionary claims were not re-checked against external sources. No separate Japanese fact finding.

## Consistency — replacement reviewer

`2ce1cec7-3737-4c18-a0e0-76cf325340e3` · `gpt-6.2-astra` (10 responses); 2026-11-24T03:49:59.238Z – 2026-11-24T03:53:20.267Z. Contiguous cumulative diff blocks: 16/16. Verbatim report body: 6386 UTF-8 bytes, SHA-256 `3b191eeee6e7d62798cc6bc6e3d2115eef68b419a9645b3ddad580f0079f83d9`.

# B256-FIX1 — replacement consistency recheck

**Verdict: all five original findings are resolved.** No new quiz, link or manifest regression was substantiated in the fix delta. I am the replacement rechecker, not the author of the original report. This was not a second blind audit.

**Snapshot and scope.** RU candidate `599b9e5b657468ea8c26bd651fe5cc9a4493ce64` is the direct parent of fix `ce3a9636e75286046db0c050b9a338a704d8f3b3`, tree `c27d61e7e15dcdefe0bbccdff0acdcd98ab58251`. Frozen EN: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. I read the full original brief and report, and all 16 supplied card patches, header through final context, in four groups of four. Each matched `git diff -U2 --abbrev=8` for its path. The only other changed file is `manifest.json`; the other 14 B256 cards and all seven prior navigation edits are unchanged. I used immutable Git blobs, the supplied dictionary records and relevant fix-title-screen hits; Python ran with `-X utf8 -B` and `RU_ROOT` set to the isolated checkout. No other reviewer report, agent or file edit.

### Five original findings — CLEAN on recheck

I checked both endpoints’ actual labels and declarations. One declaration blocks a direct pair in both directions; a missing reverse declaration is not a defect. For each removal below, neither endpoint still declares the other.

| Original finding | Status and evidence on the fix |
|---|---|
| F1 · 末っ子–子 | **Resolved.** `words/末っ子.md:9` now excludes both 子供 and 子. Each displays the complete answer «ребёнок». A youngest child is someone’s child, but 子 does not specify birth order. Neither 弟 nor 妹 was added. JMdict 1584380; `words/子.md:4,16`. |
| F2 · 欄–ページ | **Resolved.** `words/欄.md:9` adds ページ. For newspaper 欄, «страница» is defensible: JMdict 1549350 sense 1 explicitly includes *page* for らん. In reverse, ページ does not denote a form field or specifically a newspaper column (`words/ページ.md:4,15–20`). |
| F3 · 次ぐ–占める | **Resolved.** `words/次ぐ.md:9` removes only 占める. Ranking *next to/after* something does not express occupying a share; occupying a position does not imply being next. Compare JMdict 1316400 with the share and space examples in `words/占める.md:16–21`. |
| F4 · 枚数–枚 | **Resolved.** `words/枚数.md:9,29` removes the exclusion but keeps the link and 三枚 example. The count of sheets is not the counter, and 枚数 cannot occupy 枚’s slot after 三. JMdict 1524630 sense 1; `words/枚.md:15–20`. |
| F5 · 果たして–実は | **Resolved.** `words/果たして.md:4,9,12,16–24` drops 実は and gives the same revised title in metadata and H1: «как и ожидалось; в самом ли деле (в вопросе)». The rain confirms a prediction; the question leaves arrival open (JMdict 1600780 senses 1–2). Neither function is the disclosure in `words/実は.md:16–20`; conversely the moving-house disclosure expresses no fulfilled expectation or doubt. |

### Optional dispositions and new guards

- **朗らか–さわやか: optional, retained.** `words/朗らか.md:4,9` and `words/さわやか.md:4` overlap on a pleasant-sounding voice, not on refreshing weather or open personality. Melodious/cheerful sound (1560710 sense 1) is not identical to clear voice/fluent speech (1399520 sense 2). Retention is defensible, not required. The new direct 楽しい guard is also defensible: «весёлый; приятный» is a plausible choice for 朗らか in its merry sense; the reverse does not make 楽しい a word for clear skies or an open disposition.
- **東洋–東: optional concern addressed.** `words/東洋.md:4,9,43–45` adds 東, not 日本. For «страны Востока; восточный мир», the bare option «восток» permits a regional reading. In reverse, [Digital Daijisen, ひがし【東】](https://kotobank.jp/word/%E6%9D%B1-25590), sense 2, explicitly gives 東洋; sense 1 is the direction used in the station example on 東. This supports the guard, not a frequency claim. JMdict 1448230 marks the separate Japan sense dated and used in China.
- **果たして–実に: acceptable conservative addition; no まさに guard needed.** «Действительно» can report that the predicted rain did come; it does not follow that 果たして means the degree intensifier «очень» or that 実に expresses interrogative doubt. The exact label on `words/実に.md:4` is «действительно; очень». The unblocked `words/まさに.md:4` offers «именно; поистине; вот-вот»: emphasis, an exact match and imminence do not themselves confirm a prediction. The direct guards for やはり and やっぱり remain; both labels actually contain «как и ожидалось». No transitive exclusion through 実に is warranted.
- **山林→森林: optional enhancement implemented.** `words/山林.md:27` links the comparison to the signed word ID 森林, not to a kanji card. This is a prose link; the existing direct quiz exclusion is declared by 森林 and did not change.

### Integration — CLEAN for this delta

Across the 16 changed cards, frozen EN exclusion lists remain in source order as prefixes. Stable metadata, Japanese examples, Russian section headings and external source URL order are preserved. All 16 supplied dictionary records matched the corroborating source-only records. All 62 local link occurrences resolved; word and kanji targets matched their IDs. No previous link was lost. The revised 果たして title is unique in the signed word pool; the quotation of はじめに on `words/枕.md:29` matches its target title.

Manifest schema 2, `ru` → `ja`: no entry added or removed; only the 16 word hashes changed. I checked all **5,799** listed payload hashes against fix blobs (5,794 files, three images, two scenes) and independently reproduced contentVersion `5481a3ac3cb1e345`.

**Limits — UNVERIFIED:** exhaustive pool semantics, generated draws or option counts, device presentation and learner comprehension. I did not rerun the repository validator or smoke suite, rereview the 30 complete EN/RU pairs, or issue a blanket Japanese-accuracy, Russian-style or release verdict. The original validator result belongs to the candidate, not this fix.
