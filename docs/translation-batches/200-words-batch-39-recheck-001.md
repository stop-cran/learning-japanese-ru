# Batch 200 — independent recheck 001

## Snapshots

| Snapshot | Tree | Change |
|---|---|---|
| Staged candidate (scratch worktree) | `117374d47cec40b00dcaae3eb8cff40bfba29c1e` | Initial review snapshot, on top of the reviewed Batch 199 tree `841bc8c`. |
| Staged revision (scratch worktree) | `00107e197ba7aa3968b2b9db9069694484bf4edd` | Review fixes; the snapshot read by the rechecks. |
| `2eaed77d122d352a7c4685486e1125f3c01e4a5a` | `bb0885c9935a539403dd01b7196629eed9d43648` | Signed candidate on `full-ru-200-words-39`: the content of `00107e1` plus the intake. |

The revision changes nine word files and regenerates `manifest.json`:
- `状況`: line 9 adds 都合 to the exclusions, giving `[状態, 様子, 場合, 都合]`.
- `玉`: line 9 drops 銅貨 from the exclusions, leaving `[硬貨]`.
- `生じる`: line 23 reads «Во втором выражение порождает недоразумение.», putting the causal roles in subject-first order
  as in この表現は誤解を生じる.
- `命`: lines 46–48 say that いのち is sometimes written 生命 but 生命 is not always read いのち, assign «приказ, повеление» to
  the reading めい rather than いのち, and state that JMdict marks «судьба, рок» under いのち as archaic. The sentences about a
  community source mixing up the senses and about a «редкое написание» are gone.
- `生`: line 38 drops the sentence about the community source's rows; the rule against reading the beer order as せい and the
  生のデータ sentence remain.
- `現金`: line 36 now ends at «Оба значения относятся к одной словарной записи.»; the warning about mercenaries and
  «корыстный» is removed.
- `生地`: line 33 replaces the author note («Исходный список…», with the English gloss "birthplace") with a learner rule:
  the same spelling read せいち or しょうち is a separate word meaning «место рождения», and 生地（きじ）does not have that
  sense. Line 35 adds the footer citation «отдельная запись 生地（せいち; しょうち）— «место рождения»».
- `画家` and `申し訳`: one of two consecutive blank lines before «Оттенки значения» is removed.
- Only these nine word hashes and `contentVersion` change in the manifest. Titles do not change; front matter changes only in
  the two exclusion lines; no link is added or removed.

The coordinator verified the separate 生地【せいち; しょうち】 "birthplace" entry in WWWJDIC and Jisho before rewriting line 33.
Its JMdict sequence number could not be retrieved, so the footer identifies it by headword, readings and gloss.

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
- the actual diff from `117374d` to `00107e1`.

The prompts took the changed-file count from the diff (nine word files plus the manifest), and all three reports agree.

Commit signing was still unavailable: the signing key's passphrase cache had expired. Both snapshots were therefore staged trees
in a scratch worktree, and reviewers were told to read those trees rather than HEAD. No unsigned commit was made. After Batch 199
was published, the reviewed content was committed signed as `2eaed77`. `git diff 00107e1 2eaed77 -- words kanji strokes
articles manifest.json` is empty.

The worktree's index tree, working tree and untracked-file list were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `00107e1` | No original findings. O1 is resolved: `命.md:46` now says "sometimes written", matching the "sometimes written as 生命" note in JMdict 1531940 sense 1, without a rare-form label. O2 is resolved by the 生じる rewrite. The withdrawn 発表 attachment lead is unchanged. Regression check of all nine cards: the 命 rewrite keeps めい "order; command; decree" apart from いのち and keeps "fate; destiny" archaic under いのち only (JMdict 1531940 sense 5); the removed 生 and 現金 sentences carried no Japanese rule; the reviewer independently fetched the Jisho/JMdict results for 生地, which return a separate object 生地/せいち, 生地/しょうち with the sole sense "birthplace", apart from 生地・素地/きじ; and the 状況→都合 and dropped 玉→銅貨 exclusions agree with the 都合 and 銅貨 entries. Correctness and scoped coverage are **CLEAN**. |
| Consistency | tree `00107e1` | F1 and F2 are resolved: 状況 excludes 都合, and 玉 keeps only the conservative 硬貨 guard. The optional 生–じとじと/じめじめ and 用いる/使用–適用 guards stay unadded; the reviewer withdrew its 発表 «Лексика:» optional on the precedent of 言葉, 覚える and 訪ねる; and the doubled blank lines are resolved. The reviewer reran the validator (0 errors), rebuilt the manifest in memory (equal to `manifest.json`) and found titles and links unchanged in all nine cards. The 生地 rewrite adds no title or link; the only RU title containing «место рождения» is 生まれ, which is unrelated to 生地's title. Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `00107e1` | C1–C5 are resolved. C2 was rewritten rather than deleted; the reviewer judged the rewrite clearer than deletion and checked Digital Daijisen, which lists せいち and しょうち【生地】 as "birthplace" apart from きじ. The optional 発表 «оглашение», 状況/事態 and 現金 «взялся помогать» items stay declined. Regression check: the shortened 生 and 現金 paragraphs and the rewritten 生地 and 命 passages are complete, natural Russian. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Consistency F1: 状況 lacks a guard against 都合 | **Resolved** | `状況.md:9`. Direct, one-sided pair; 場合→都合 is the precedent. |
| Consistency F2: 玉→銅貨 is reached only by chaining | **Resolved** | `玉.md:9`. The 玉→硬貨 guard remains. |
| Comprehensibility C1: 生じる roles reversed | **Resolved** | `生じる.md:23`. Also correctness optional O2. |
| Comprehensibility C2: 生地 author note with an English gloss | **Resolved, in modified form** | `生地.md:33,35`. The reviewer proposed deleting the paragraph; it was rewritten as a Russian learner rule about the separate word せいち/しょうち, which the reviewer accepted. |
| Comprehensibility C3: 命 adjudication instead of a learner rule | **Resolved** | `命.md:46-48`. |
| Comprehensibility C4: 生 editorial clause | **Resolved** | `生.md:38`. |
| Comprehensibility C5: 現金 false lead about mercenaries | **Resolved** | `現金.md:36`. |
| Correctness optional O1: 命 «редкое написание» | **Optional, adopted** | `命.md:46` now says «иногда записывают». |
| Correctness optional O2: 生じる role order | **Optional, adopted** | Same fix as comprehensibility C1. |
| Correctness lead: 発表 «на занятии» attachment | **Withdrawn** | Withdrawn by the reviewer in review 001; the card is unchanged. |
| Consistency optional: 生 vs じとじと/じめじめ | **Optional, declined** | The qualifier and different sense make a guard unnecessary; the reviewer agreed. |
| Consistency optional: 用いる/使用 vs 適用 | **Optional, declined** | Necessity not established. |
| Consistency optional: 発表 «Лексика:» footer | **Withdrawn** | The reviewer withdrew it on the precedent of 言葉, 覚える and 訪ねる. |
| Consistency optional: doubled blank lines in 画家 and 申し訳 | **Optional, adopted** | One blank line removed in each. |
| Comprehensibility optional: 発表 «оглашение» vs the kanji card's «объявление» | **Optional, declined** | A word title and a kanji-card gloss need not coincide; the examples on the word card define the sense. |
| Comprehensibility optional: 状況/事態 near-paraphrase | **Optional, declined** | Both cards carry contrast sentences, and 事態→状況 is guarded. |
| Comprehensibility optional: 現金 «взялся помогать» | **Optional, declined** | 急に手伝うなんて comments on an action the listener has just started; the Russian perfective past is the natural rendering, as EN's "Suddenly offering to help" is. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** after fixes, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

Limits: the JMdict sequence number of 生地【せいち; しょうち】 was not obtained. Its separate existence rests on WWWJDIC, the Jisho
API and Digital Daijisen. The consistency reviewer did not re-fetch that evidence. Digital Daijisen gives せいち further senses that
the card does not mention, and the card does not claim that "birthplace" is the only one. Unchanged cards were not reread in the
rechecks. No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
