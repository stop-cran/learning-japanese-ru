# Batch 202 — independent recheck 001

## Snapshots

| Snapshot | Tree | Change |
|---|---|---|
| Staged candidate (scratch worktree) | `fdf29ba137faa929ab8a81876d0e252c83d1c416` | Initial review snapshot, on top of the reviewed Batch 201 tree `7d283bd`. |
| Staged revision (scratch worktree) | `459ddeffdbb0a737d9bcc2062726e49627199462` | Review fixes; the snapshot read by the rechecks. |
| `b75403d780edb7a2327a2b320955258acf5cb8f1` | `e5a0af056295cbfc342c5c6209d83db1394e679b` | Signed candidate on `full-ru-202-words-41`: the content of `459ddef` plus the intake. |

The revision changes nine word files and regenerates `manifest.json`:
- `温度`: line 21 says that 温度が下がる describes the temperature falling «без указания причины» instead of «понижается сама»,
  using the correctness reviewer's text.
- `濠`: line 33 adds «В источнике N2 указаны оба значения — «ров» и «канал».», and line 35 adds «Написание 堀 из источника N2 и
  стабильное написание 濠 этой карточки относятся к одной записи JMdict 1522060 с чтением ほり; сохранён уже имевшийся уровень
  N3.». Both restore EN's source notes at their EN positions (EN `濠.md:33,35`).
- `温暖`: line 16 reads «な-прилагательное» instead of Latin «na-прилагательное».
- `灰`: line 15 reads «О количестве золы говорит остальное предложение: особой формы для этого у слова нет.» instead of the reversed
  «Количество золы задаёт остальное предложение…». The coordinator chose this wording over the reviewer's suggested sentence; it
  keeps the same rule.
- `涙`: line 18 translates 彼女はうれしくて涙を流しました as «Она от радости пролила слёзы.» instead of «Она плакала от радости.»,
  using the comprehensibility reviewer's text.
- Optional rewordings adopted:
  - `満足`: line 15 «То, чем человек доволен…» instead of «Тем, чем…».
  - `体温`: line 33 «Для изучения этого слова важно…» instead of the calque «Для словаря важно…».
  - `海外`: line 19 «…другу, который живёт за рубежом.» instead of «…другу за рубежом.».
  - `流行`: line 18 «Среди молодёжи эта песня сейчас в моде.» instead of «Эта песня популярна среди молодёжи.».
- Only these nine word hashes and `contentVersion` change in the manifest. No title, front matter, link or exclusion changes.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer reread its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

Rechecks ran serially.
Each reviewer received only:
- its facet's original blind report;
- the coordinator's dispositions of its findings;
- the revised snapshot;
- the actual diff from `fdf29ba` to `459ddef`.

The prompts took the changed-file count from the diff (nine word files plus the manifest), and all three reports agree.

Commit signing was still unavailable: the signing key's passphrase cache had expired. Both snapshots were therefore staged trees
in a scratch worktree, and reviewers were told to read those trees rather than HEAD. No unsigned commit was made. After Batch 201
was published, the reviewed content was committed signed as `b75403d`. `git diff 459ddef b75403d -- words kanji strokes
articles manifest.json` is empty.

The worktree's index tree, working tree and untracked-file list were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `459ddef` | C1 and C2 are resolved. `温度.md:21` describes 温度が下がる as the temperature falling without stating a cause, keeping EN's subject-versus-object contrast (EN `温度.md:21`). `濠.md:33,35` restore the N2 source's moat/canal senses, the source spelling 堀 versus the stable 濠, the shared JMdict 1522060 entry with ほり and the retained N3 level, without extending EN's claims. The optional 満足 slip is resolved; the reviewer's original `:16` reference was off by one. Regression check of every changed passage: 温暖 keeps its noun use and 温暖な/温暖です guidance; 灰 still says that the sentence supplies the quantity; the 涙 translation keeps the cause, the past event and explicit 涙; «другу, который живёт за рубежом» is an acceptable contextual rendering of 海外の友人に and is not presented as a lexical meaning; «сейчас в моде» renders 流行しています and stays compatible with the 人気 contrast; 体温 keeps EN's vocabulary-learning scope. The manifest diff contains only the nine word hashes and `contentVersion`. Correctness and scoped coverage are **CLEAN**. |
| Consistency | tree `459ddef` | F1 is resolved: `温暖.md:16` reads «Это な-прилагательное…», and a search finds no remaining Latin «na-прилагательн» in `words/`. The optional 濠 item is resolved: both EN sentences are restored at EN's positions (`濠.md:33,35`), and the JMdict number matches the card's dictionary line. The exclusion classifications stand, because no title, front matter or `quiz_exclusions` changed. Regression check: front matter and link-target lists of all nine changed cards are identical to `fdf29ba`, so EN link parity is unchanged and no new title collision is possible; the reworded passages keep the cards' terminology; `流行.md:18` «сейчас в моде» fits the title «мода; массовое распространение», and line 31's contrast with 人気 and the 人気 guard are intact. All non-stroke manifest hashes match the worktree bytes; only the nine word hashes and `contentVersion` differ. The reviewer ran the validator (0 errors). Stroke hashes remain unverifiable from the CRLF checkout, and this revision does not touch them. Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `459ddef` | C1, C2 and C3 are resolved. `灰.md:15` now makes the rest of the sentence the subject that conveys the amount, matching EN "The amount is supplied by the sentence"; the wording differs from the reviewer's suggestion, but the reversal is gone. `涙.md:18` «Она от радости пролила слёзы.» matches the card's gloss «проливать слёзы» and no longer uses «плакала», the verb for 泣く. `温暖.md:16` reads «な-прилагательное», and the next sentence still shows 温暖な. The adopted optional items are resolved: 体温 «Для изучения этого слова» removes the calque; 海外 «другу, который живёт за рубежом» attaches the place to the friend (the reviewer noted «живёт» is slightly more residential than a temporary stay, not a new defect); 流行 «сейчас в моде» shows the fashion sense without colliding with line 31's 人気 «популярность». The reviewer withdrew the three declined optional items (消費/費用, 濠's first 堀, 泳ぎ方) on the coordinator's evidence. Regression check of every changed passage: 温度 «без указания причины» is clearer than «сама» and keeps the contrast with 温度を下げる; 満足 «То, чем…» is now a grammatical subject; 濠:33 is grammatical, and 濠:35 is stiffer («стабильное написание», «сохранён уже имевшийся уровень N3» follow the EN card's own learner-visible provenance) but readable, and it does not hide the 運河 overlap or the moat-first rule. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 温度が下がる «понижается сама» | **Resolved** | `温度.md:21`, the reviewer's text. |
| Correctness C2: 濠 drops EN's N2-source/堀/JMdict/N3 note | **Resolved** | `濠.md:33,35`. |
| Correctness optional: 満足 «Тем, чем» | **Optional, adopted** | `満足.md:15`. |
| Consistency F1: 温暖 Latin «na-прилагательное» | **Resolved** | `温暖.md:16`. |
| Consistency optional: 濠 source sentences | **Optional, adopted** | `濠.md:33,35`, as correctness C2. |
| Comprehensibility C1: 灰 «задаёт» reverses the relation | **Resolved** | `灰.md:15`, coordinator wording. |
| Comprehensibility C2: 涙 «плакала» conflates 涙を流す with 泣く | **Resolved** | `涙.md:18`, the reviewer's text. |
| Comprehensibility C3: 温暖 «na-» | **Resolved** | `温暖.md:16`, as consistency F1. |
| Comprehensibility optional: 体温 «Для словаря» calque | **Optional, adopted** | `体温.md:33`. |
| Comprehensibility optional: 海外 «другу за рубежом» attachment | **Optional, adopted** | `海外.md:19`. |
| Comprehensibility optional: 流行 «популярна» next to 人気 | **Optional, adopted** | `流行.md:18`. |
| Comprehensibility optional: 消費 «расходы» without naming 費用 | **Withdrawn** | EN does not teach 費用 on this card, and the titles do not collide; the reviewer withdrew the item on recheck. |
| Comprehensibility optional: 濠 uses 堀 before the spelling note | **Withdrawn** | `濠.md:25` explains 堀 in EN's order, and line 35 now also links 堀 and 濠; the reviewer withdrew the item on recheck. |
| Comprehensibility optional: 泳ぎ does not name 泳ぎ方 | **Withdrawn** | EN's body does not name 泳ぎ方; the reviewer withdrew the item on recheck. |
| Comprehensibility, outside the facet: exclusions not reciprocated | **Not adopted** | Exclusions are direct one-sided pairs by design; the app applies a pair declared on either card. |
| Comprehensibility, outside the facet: 火災 昨夜 «вчера вечером» | **Not adopted** | A standard rendering of 昨夜; the correctness review raised no finding. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN** after fixes.
- Scoped coverage: **CLEAN** after fixes.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN** after fixes.
- Quiz safety: **CLEAN**, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive
  groups.

Limits: the rechecks did not refetch dictionary entries; unchanged lexical facts rest on the dictionary inspection in review
001. Unchanged cards were not reread in the rechecks. No native-speaker, learner, app-import, device, media, activation or
release acceptance is claimed.
