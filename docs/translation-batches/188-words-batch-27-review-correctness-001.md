# B188 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `c721e1cb63f33938081927e236dc7f9674f073b6`.

## Snapshot and reviewer

- **RU:** `C:\Users\romanko\repos\learning-japanese-ru`  
  Branch: `full-ru-188-words-27`  
  Commit: `c721e1cb63f33938081927e236dc7f9674f073b6`
- **Frozen EN:** `C:\Users\romanko\repos\learning-japanese-en-frozen`  
  Commit: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`
- Both working trees were clean. No uncommitted changes included.
- **Model and family:** not exposed in verifiable execution metadata; neither can be reliably identified. One direct reviewer; no subagents.

## Complete scope

Read the front matter and every learner-facing section, example, translation, inline construction, comparison and citation in all 30 `words/<name>.md` cards, alongside their exact frozen EN articles:

違いない, 道路, 道徳, 過去, 過ごす, 幸い, 幸運, 運, 遅刻, 遂に, 改善, 上達, 前進, 進歩, 進学, 進める, 週, 週間, 逮捕, 連続, 連想, 友, 連れ, 速度, 通行, 合格, 通過, 通学, 通信, 通り過ぎる.

Inspected applicable repository instructions, content-format rules and vocabulary-level policy. No author report, author prompt, title-screen output or other reviewer report was consulted.

## Verdicts

| Articles | Correctness | Scoped coverage | Russian comprehensibility |
|---|---|---|---|
| 週間 | **NEEDS FIX** | **CLEAN** | **UNVERIFIED** |
| Other 29 cards listed above | **CLEAN** | **CLEAN** | **UNVERIFIED** |
| **Batch overall** | **NEEDS FIX** | **CLEAN** | **UNVERIFIED** |

CLEAN means no actionable defect established within this review—not exhaustive certification. Russian translation semantics were checked under correctness; standalone Russian comprehensibility was unassigned.

## Finding

### F1 — Minor · Correctness · Unresolved

**Location:** `words/週間.md:40–41`

**Claim:**  
> 毎週（まいしゅう）указывает на повторение раз в неделю

This defines 毎週 as recurrence **once a week**.

**Correct fact and learning impact:** 毎週 means **every week**; it does not itself specify one occurrence per week. The Russian restriction can mislead learners about schedules involving several occurrences each week. Frozen EN `words/週間.md:33` says only “expresses recurrence”; the once-only restriction is introduced in RU.

**Remedy:** Replace the clause with:

> 毎週（まいしゅう）значит «каждую неделю».

If once-weekly frequency is needed, teach `週に一回` separately.

**Direct evidence:**

- [Shogakukan, Digital Daijisen: 毎週](https://kotobank.jp/word/%E6%AF%8E%E9%80%B1-632956): 「1週間ごと。週がかわるたび。」
- [JMdict via Jisho: 毎週／まいしゅう](https://jisho.org/api/v1/search/words?keyword=%E6%AF%8E%E9%80%B1), sense 1: “every week.”

**Confidence:** HIGH. This is a localized semantic correction, not a request for broader coverage.

## Evidence and coverage basis

- Inspected all **35 distinct JMdict IDs cited by the cards**, including relevant senses and restrictions, in the [canonical live XML](https://www.edrdg.org/pub/Nihongo/JMdict_e.gz). All cited identities were found. Supplemented these with comparison entries, named Kotobank dictionary sections and the JLPT Sensei に違いない attachment lesson.
- Checked all 30 N3 spelling/reading rows against the [pinned vocabulary source](https://raw.githubusercontent.com/stephenmk/yomitan-jlpt-vocab/b062d4e38c4bdd0950ae1d4ec55f04b176182e03/original_data/n3.csv), independently of kanji difficulty.
- No separate necessary teaching dependency or scoped-content omission was established. Explicit local article links and quiz-exclusion targets resolve.
- Five metadata-listed kanji lack RU cards: 徳, 遂, 改, 善, 逮. The validator expressly exempts kanji without cards; their absence is not treated as a requirement to author additional cards in B188.

## Optional

None.

## Limitations

- No corpus-wide frequency measurement, native-speaker panel or learner testing. Dictionary recognition was not treated as proof of unrestricted interchangeability or frequency. Examples were assessed linguistically; not every authored sentence was independently corpus-attested.
- Live dictionary evidence does not reconstruct the EN author’s historical source captures. Inherited claims were not accepted merely because they appeared in EN; lexical verification does not independently establish historical etymology.
- No whole-repository quiz-pool audit, baseline-card review, kanji-card fact audit, media/device testing or publication-validator run. Direct dependency checks do not certify the release package.
- Initial Jisho rate limits and an alternate EDRDG-host TLS failure were overcome using the canonical XML; no cited lexical entry remained unavailable.
- **Read-only maintained:** no edits, staging, commits, pushes, issues or PRs.
