# Batch 190 — independent review 001

## Snapshot and scope

- RU candidate commit: `0462ca5d05879b79e3fc4c28893b707b1c7af588` (tree `f66a5366d520e9b7e13e22f2b03a8d2e854c6538`), branch `full-ru-190-words-29`, parent `5bfe405`.
- Published baseline recorded in the intake: `e32c081` (B189 merge); parent `5bfe405` adds only the B189 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all 30 new word cards. Correctness and consistency also inspected the eight navigation-only files; consistency additionally covered `manifest.json` and the intake.
- Reviewers were assigned three distinct model families: correctness — `gpt-6.1-sol`; consistency/quiz safety — `claude-sonnet-5.5`; comprehensibility — `grok-4.7`. The runtime agent listing exposed these assigned model variants; reviewer prose did not expose a lower-level serving identifier.
- Reviews ran serially, one reviewer at a time.
- Full blind reports: `190-words-batch-29-review-correctness-001.md`, `190-words-batch-29-review-consistency-001.md` and `190-words-batch-29-review-comprehensibility-001.md`.
- Initial reviewers did not read the author report, the author prompt, the title-screen output or one another's reports.

## Initial verdicts and findings

| Reviewer facet | Verdict | Findings |
|---|---|---|
| Correctness and scoped coverage | Correctness **NEEDS FIX**; coverage **NEEDS FIX** (`通じる` only) | F1 (minor, high confidence): `通じる.md:36–37` said 通る «не заменяет 通じる в значениях, связанных с общением», dropping EN's "not … every"; JMdict 通る senses 7, 10 and 11 establish overlap. F2 (minor): Russian-only lexical notes on 近代, 農民, 丸, 輪, 軍隊, 軍, 身長 and 自身 cited only JMdict; the reviewer found Kuznetsov entries supporting the six lexical notes, but not 輪's «часто», and left the 近代 «Новое время» periodization claim **UNVERIFIED**. |
| Consistency and quiz safety | Consistency, quiz safety and coverage **CLEAN** | No actionable finding. All 25 EN pairs are retained; the 27 RU-added pairs were classified (table below). Optional: 農業→産業 and 轢く→引っ越す judged unjustified but harmless; approximation guards on 辺り are inconsistent (頃 only); ひく and やめる homophones need no guard. Validator, link parity, manifest hashes and intake hashes were independently rechecked. |
| Comprehensibility and scoped coverage | Comprehensibility **NEEDS FIX** (`辺り`, `迷惑`, `近代`, `丸`); coverage **NEEDS FIX** (`辺り` only) | F1 (minor): `辺り` named 近く and 周り without a demonstrating pair and did not separate 近所 or 辺（へん）. F2 (minor): `迷惑`'s «хлопоты» is shared with 面倒, 手間 and 苦労, but the section did not contrast 手間 or 苦労. F3 (minor): the `近代` title «новое время» was the equation that the card's own caution withdraws. F4 (minor): bare 円 in `丸.md:28` had no reading. Optional: remove the «исходного списка» frame in 通す/通じる and add «(1868)» after Мэйдзи. |

No finding established a missing requested card or a necessary prerequisite omission.
Optional suggestions are kept in the complete reviewer reports rather than promoted to defects.

### Russian evidence cited by the correctness reviewer

Cards cite only Japanese dictionaries by repository convention; the Russian lexical evidence for correctness F2 is recorded here.
The reviewer inspected Kuznetsov's dictionary via gramota.ru:
[крестьянин](https://gramota.ru/poisk?query=крестьянин&mode=slovari) (farming person; separate pre-1917 estate sense),
[месяц](https://gramota.ru/meta/mesyats) (time unit; conversational "moon"),
[кольцо](https://gramota.ru/poisk?query=кольцо&mode=slovari&dicts%5B%5D=42) (sense 1 hoop-shaped object; sense 2 finger jewellery),
[армия](https://gramota.ru/poisk?query=армия&mode=slovari) (all armed forces vs land forces),
[рост](https://gramota.ru/poisk?query=рост&mode=slovari&dicts%5B%5D=42) (growth/development vs stature) and
[сам](https://gramota.ru/poisk?query=сам&mode=slovari&dicts%5B%5D=42) (personal participation vs independent action).
These support the qualified notes on 農民, 丸, 輪, 軍隊/軍, 身長 and 自身; they do not support a frequency claim.

For 近代 the coordinator inspected:
- [Warodai/Jardic](https://www.jardic.ru/search/search_r.php?q=近代&pg=0&dic_jardic=1&dic_warodai=1&sw=1920): Warodai «1) ист. новейшее время (в Японии с 1868 г.); 2) новое время, новые времена», 近代史 «история нового времени»; Jardic «современность; новое (нынешнее) время; новейшее время Японии (с 1868 г.)».
- [ru.wikipedia «Новое время», Периодизация](https://ru.wikipedia.org/wiki/Новое_время#Периодизация): the period's proposed starting points are c. 1440, 1453, 1492, 1517 and 1640 (the last citing Маныкин 2004), and the introduction notes that not all peoples entered the period simultaneously.

The translation «новое время» is therefore attested for 近代, while the Russian general-history period begins long before 1868.
This supports a qualified caution, not a prohibition of that translation.

## Exclusion classification: author and consistency reviewer

The author report and the blind consistency reviewer classified the 27 RU-added exclusion pairs independently.
The differences are preserved here rather than resolved by vote. Classification does not change runtime behaviour: every kept pair is declared.

| Pair | Author | Consistency reviewer |
|---|---|---|
| `瞬間`→`際` | conservative | required (titles share «момент») |
| `迷惑`→`厄介` | conservative | required («хлопоты»/«хлопотный»; same cluster as the EN guards) |
| `辺り`→`側`, `辺り`→`隣` | conservative | required (titles share «рядом») |
| `現代`→`現在` | required | conservative (real basis, necessity unestablished) |
| `迎え`→`迎える` | required | conservative |
| `身`→`肉` | required | conservative |
| `農業`→`産業` | required | unjustified (hypernym/topical; harmless) |
| `轢く`→`引っ越す` | conservative | unjustified (the 引っ越す title already disambiguates; harmless) |

The remaining 18 pairs are classified the same way by both:
- required: `迷惑`→`不便`; `迷子`→`子`/`子供`; `現代`→`時代`; `近代`→`時代`; `農家`→`家族`/`家庭`; `輪`→`指輪`; `転ぶ`→`落ちる`; `身長`→`成長`/`増加`;
- conservative: `辺り`→`頃`; `迎え`→`会`/`会合`; `農家`→`家`; `通す`→`極める` (reviewer: weak); `轢く`→`移る`; `身`→`中心`.

The author's counts are 15 required and 12 conservative, 27 in total, which matches the reviewer's table.
The disposition of `農業`→`産業` and `轢く`→`引っ越す` is in the recheck record.

Reconciliation, the coordinator's dispositions and the final verdicts are in `190-words-batch-29-recheck-001.md`.
