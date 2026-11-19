# Batch 190 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `0462ca5d05879b79e3fc4c28893b707b1c7af588` | `f66a5366d520e9b7e13e22f2b03a8d2e854c6538` | Initial review snapshot. |
| `2f666c945b2e926454eb3728b6ac4cfdb73d6b94` | `c248a7890bdc12122b18ed29447b25e741473c2d` | Final candidate: `近代` retitled «эпоха модернизации» with matching example and compound glosses, «(1868)» and a qualified «новое время» caution; `辺り` and `迷惑` contrast passages rewritten with demonstrating examples; `丸` gives 円（えん）and its まる spelling; `通じる` restores the "not every" qualification; `輪` drops «часто»; `通す`/`通じる` drop the «исходного списка» frame; `轢く`→`引っ越す` withdrawn; manifest and intake regenerated. |

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks used the same assigned model variants and facets as review 001: `gpt-6.1-sol` correctness, `claude-sonnet-5.5` consistency/quiz safety, `grok-4.7` comprehensibility. Model assignments are recorded from the task-runner runtime listing; reviewer prose did not expose separate serving IDs.
They ran serially. Each reviewer received only its own original findings, the coordinator's dispositions of them, the revised snapshot and the actual diff `0462ca5..2f666c9`.
Process note: the consistency reviewer checked out `2f666c9` detached to run the validator; the coordinator switched back to the branch at the same commit before the next recheck, and the working tree had no content changes.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | `2f666c9` | F1 and F2 (b, c) resolved; F2 (a), card-local Russian citations, withdrawn under the evidence-location convention; the 近代 caution checked against freshly inspected Warodai/Jardic and ru.wikipedia evidence; no regression; correctness and scoped coverage **CLEAN**. |
| Consistency | `2f666c9` | 轢く→引っ越す resolved; the 農業→産業 concern withdrawn under the generic-label rule; «эпоха модернизации» unique in the pool; link parity, validator and manifest check clean; consistency, quiz safety and cross-file integration **CLEAN**. |
| Comprehensibility | `2f666c9` | F1–F4 and both accepted optional items resolved; no regression in any changed passage; comprehensibility and scoped coverage **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1, categorical 通る/通じる separation | **Resolved** | `通じる.md:37` now says «Он заменяет 通じる не во всех значениях, связанных с общением», restoring frozen EN's "not a replacement for every communication use". JMdict 通る senses 10–11 establish overlap without unrestricted substitution. |
| Correctness F2 (a), Russian-only lexical notes cite only JMdict | **Withdrawn** by the reviewer as a card-local requirement | Cards cite Japanese dictionaries by repository convention; the reviewer's Kuznetsov evidence for 農民, 丸, 輪, 軍隊/軍, 身長 and 自身 is recorded in `190-words-batch-29-independent-review-001.md`. The recheck confirmed that the evidence supports the qualified notes. |
| Correctness F2 (b), 輪 «часто понимают как украшение» | **Resolved** | `輪.md:31` now says «может обозначать и украшение»; Kuznetsov кольцо sense 2 establishes the sense, not its frequency. |
| Correctness F2 (c), 近代 «Новое время» periodization claim (UNVERIFIED) | **Resolved** | `近代.md:33` now acknowledges that the translation «новое время» occurs and cautions against equating it with 近代 without qualification, because the general-history period begins long before Meiji. The reviewer freshly inspected Warodai/Jardic (近代 «новое время, новые времена»; «новейшее время (в Японии с 1868 г.)») and ru.wikipedia «Новое время», Периодизация (starting points 1440–1640). This supports the bounded caution, not a prohibition. |
| Comprehensibility F1, 辺り synonyms undemonstrated | **Resolved** | `辺り.md:29` contrasts 駅の近く with 池の周りを歩く, defines 近所, and says 辺（へん）in この辺 overlaps この辺り but is a separate word, while 来週あたり belongs to あたり. The reviewer's proposed «来週あたり нельзя заменить на へん» was not adopted because it was unverified; the recheck agreed that attributing the time example is enough. 近所 and 辺 stay unlinked for EN link parity. |
| Comprehensibility F2, 迷惑 «хлопоты» shared with 面倒/手間/苦労 | **Resolved** | `迷惑.md:35–43` adds 手間がかかる and 苦労, the 面倒 example この手続きは面倒です, keeps 邪魔/困る and ends with 迷惑 as inconvenience caused to others (迷惑をかける) or experienced (迷惑する). 手間 and 苦労 stay unlinked; 迷惑 already excludes 面倒, 手間 and 苦労. |
| Comprehensibility F3, 近代 title «новое время» | **Resolved with modification** | Title and H1 are the single label «эпоха модернизации», matching EN's single label. The proposed second segment «недавняя историческая эпоха» was screened out for stem overlap with 最近, さっき, このあいだ (недав-) and 歴史 (истор-). Glosses use «эпохи модернизации» rather than «эпохи 近代»; line 16 keeps the broader recent-era sense. The title screen reports only 時代 and 現代 as overlaps, and both are excluded. |
| Comprehensibility F4, bare 円 in 丸 | **Resolved with modification** | `丸.md:28` gives 円（えん）«иена; круг» and says まる on 円 is a dictionary spelling of 丸 itself. 円 stays unlinked: frozen EN links `words/円.md`, which RU lacks, and a substitute kanji link would not match EN. |
| Comprehensibility optional: remove «исходного списка» in 通す/通じる | **Resolved** | `通す.md:44` and `通じる.md:48` no longer refer to a source list; the «пропустить» and bare «понимать» warnings remain. |
| Comprehensibility optional: «(1868)» after Мэйдзи | **Resolved** | Added at `近代.md:21`. |
| Comprehensibility optional: 〜を通じて and intermediary 通して | **Optional, declined** | Frozen EN omits them; this would be expansion, not a lost point. |
| Consistency optional: 轢く→引っ越す unjustified | **Resolved** | Removed; `轢く.md:9` is `quiz_exclusions: [移る]`. The 引っ越す title «переезжать (менять жильё)» already disambiguates, and the 轢く body says this «переехать» is not changing residence. |
| Consistency optional: 農業→産業 unjustified | **Kept; concern withdrawn in recheck** | The 産業 title «промышленность; отрасль экономики» contains a generic label that agriculture satisfies, which the RU generic-label rule (`content-structure.instructions.md`, 車/電車) covers. The reviewer withdrew the concern and kept it optional. |
| Consistency optional: approximation guards on 辺り | **Optional, declined** | 辺り→頃 is kept as conservative because the body teaches 来週あたり and 頃's title is «около (о времени)». ころ, くらい, ほど and およそ have titles that do not overlap 辺り's. |
| Consistency optional: homophones 轢く/引く/弾く and 辞める/止める | **Optional, declined** | Spelling or reading alone is not an exclusion basis, the Russian titles share no meaning and EN has no pair. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
