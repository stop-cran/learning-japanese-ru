# Batch 206 — independent recheck 001

## Snapshots

| Snapshot | Tree | Change |
|---|---|---|
| Staged candidate (scratch worktree) | `6bfa34bee12a8bc1e805693a49888fb65cfd7331` | Initial review snapshot, on top of the reviewed Batch 205 tree `84dc60f`. |
| Staged revision (scratch worktree) | `b8df8dfa7d68e8b1c072208a7d7fa19d09411f6a` | Review fixes; the snapshot read by the rechecks. |
| `b1e17bfcf168731f0a6cfea0fe922f171abc7434` | `a58b2b3b410cf106ecc50270949e47d15ffb4e60` | Signed candidate on `full-ru-206-words-45`: the content of `b8df8df` plus the intake. |

The revision changes seven word files and regenerates `manifest.json`:
- `放す`: lines 21-22, «Второй пример буквально описывает, как рука отпускает шарик.», become lines 21-23: «Во втором примере
  буквально сказано «отпустил руку от шарика»: 手を — «руку», 風船から — «от шарика».» The Japanese example, its kana and its
  natural translation «Ребёнок выпустил воздушный шарик из рук.» are unchanged.
- `日付`: «Оттенки значения» (lines 39-40) now opens «日付 — только календарная дата. Романтическое свидание по-японски
  называется デート, а не 日付.» デート is plain text because RU has no デート card; the existing form-format sentence follows.
- `方々`: lines 31-32 replace «Основное чтение и тип в этой карточке описывают слово со значением «люди».» with «Основное
  чтение карточки и пометка wago («исконное слово») относятся к слову «люди» — かたがた.» Lines 45-46 replace the source-list
  sentence («Исходный список слов, на котором основана карточка, смешивал переводы обоих слов, поэтому ни одно из чтений не должно
  наследовать их все.») with a learner rule: «Заголовок карточки, как и некоторые списки слов, даёт переводы обоих слов сразу. Это
  значения двух разных слов: каждое чтение берёт только своё.» The merged title is kept, as in frozen EN.
- `日常`: lines 25-27 add Digital Daijisen's adverbial example 日常用いる道具（にちじょうもちいるどうぐ）«предметы, которыми
  пользуются в обычной жизни». Lines 41-46 add a paragraph contrasting 生活 (how one lives and supports oneself; 生活する),
  暮らし (way of life and livelihood) and 日常 (the habitual course of days: 日常に戻る, 日常の会話), noting their overlap in
  日常生活 and 普段's frequent adverbial use, with 普段は自転車で行きます（ふだんはじてんしゃでいきます）«Обычно я езжу на
  велосипеде». It ends «Словарь толкует 日常 и через ふだん, поэтому это пересечение значений, а не запрет замены.» 生活, 暮らし and
  普段 stay plain text, because EN does not link them there and an RU-only link would break EN link parity. Line 54 adds the
  Digital Daijisen 日常 citation.
- `支出`: lines 34-37 replace «[費用](費用.md)（ひよう）называет издержки или затраты, связанные с чем-либо.» with «[費用](費用.md)
  （ひよう）— деньги, которых требует определённое дело, его стоимость: 旅行の費用（りょこうのひよう）— «расходы на поездку». 支出
  смотрит со стороны бюджета: это деньги, которые из него ушли. Одну и ту же выплату можно назвать обоими словами, глядя с разных
  сторон.» Line 45 adds Digital Daijisen citations for 支出 and 費用 sense 1.
- `故郷`: the first example (line 20) is translated «На летних каникулах я поеду домой, в родной город.» instead of «…я поеду в
  родной город.», restoring the return-home sense of 帰ります.
- Quiz exclusions only: `日光.md:9` adds `quiz_exclusions: [光]` after `tags:`.
- Only these seven word hashes and `contentVersion` change in the manifest. No title, internal link, reading or existing Japanese
  example changes; the only front-matter change is the 日光 exclusion line.

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
- the coordinator's dispositions of its findings and optional items;
- a short description of each change made in response to the other reviewers, without their reports;
- the revised snapshot;
- the actual diff from `6bfa34b` to `b8df8df`.

The prompts took the changed-file count from the diff (seven word files plus the manifest), and all three reports agree.
One disposition message to the comprehensibility reviewer misspelled 暮らし in its own summary of the 日常 change; a follow-up
message corrected the typo, and the reviewer read and quoted the card's actual text (`日常.md:42`, 暮らし).

Commit signing was still unavailable: the signing key's passphrase cache had expired. Both snapshots were therefore staged trees
in a scratch worktree, and reviewers were told to read those trees rather than HEAD. No unsigned commit was made. After Batch 205
was published, the reviewed content was committed signed as `b1e17bf`. `git diff b8df8df b1e17bf -- words kanji strokes
articles manifest.json` is empty.

The recheck prompts forbade running `tools/build_manifest.py` or any other generator; all three reports state that none was run.
After every recheck the coordinator confirmed that `git write-tree` still printed `b8df8df…`, that the working tree equalled the
index, and that no untracked or ignored file existed.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | tree `b8df8df` | The reviewer confirmed the supplied diff equals the actual Git diff and read all seven revised cards in full, plus the RU 光 and 費用 cards. C206-01 is resolved: `放す.md:21-23` makes 手を the object and 風船から the source, so the hand is no longer the agent; the example, its kana and 放した/放さない are unchanged. C206-02 is resolved: `日付.md:39-40` restores the デート comparator with its romantic sense, as plain text, without inventing a Russian ambiguity of «дата». Regression check: it freshly fetched Digital Daijisen 日常 (definition «つねひごろ。ふだん。平生», example 日常用いる道具), 支出 and 費用 sense 1, and the Jisho/JMdict entries for 生活, 暮らし, 普段, both 方々 entries and 帰る. The 日常 contrast permits overlap rather than inventing exclusive meanings; 支出/費用 are distinguished by perspective, not as exclusive categories; 方々 attaches wago only to かたがた; 故郷 «поеду домой» carries 帰る sense 1. Each changed file's LF-normalized hash matches the manifest, and `tools/validate.py` reported 0 errors. Correctness and scoped coverage are **CLEAN**; no optional items. |
| Consistency | tree `b8df8df` | The optional 日光→光 guard is adopted and resolved: it follows `tags`, is a direct one-sided pair applied symmetrically by the app, has a real JMdict basis («солнечный свет» vs «свет»), and conflicts with no existing list (光 and 明かり do not list 日光). The optional note on 方々's merged title needs no action: the title is faithful to frozen EN, and the body now states that each reading takes only its own meanings. Regression check: in all seven files the RU internal links equal EN's; 生活, 暮らし, 普段 and デート are plain text, and the new Daijisen links are external. Titles, tags and other front matter are unchanged apart from 日光's exclusion; all EN exclusions are retained. All seven hashes match the manifest, whose entry count (4,294) is unchanged; no stray file exists; `tools/validate.py` reported 0 errors. Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | tree `b8df8df` | C1 is resolved: `方々.md:31-32,45-46` explains wago and ties it to かたがた, and the former author-facing source-list note is now a learner rule separating the two readings' meanings. C2 is resolved: `日常.md:25-27,41-46` shows the adverbial example with kana and contrasts 生活, 暮らし, 日常 and 普段 with explicit overlap rather than a ban; leaving those words unlinked is correct under EN link parity. C3 is resolved: `支出.md:34-37` defines 費用 as the money an undertaking requires and 支出 as money that has left a budget, with one payment nameable either way. The optional 故郷 change is adopted and resolved; the reviewer agreed that the 文字 «буквы» and 既に/新た register items stay declined. Regression check: 放す's literal note matches the particles; 日付's «только календарная дата» keeps the document-date teaching; 日光's change is metadata only. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C206-01: 放す's literal gloss reverses the roles of 手を and 風船から | **Resolved** | `放す.md:21-23`; Digital Daijisen 放す sense 2 (ハンドルから手を放す). |
| Correctness C206-02: 日付 drops EN's デート comparator | **Resolved** | `日付.md:39-40`; frozen EN 日付. |
| Consistency optional: 日光–光 guard | **Optional, adopted** (conservative) | `日光.md:9`. |
| Consistency optional: 方々's merged EN title | **Optional, unchanged** | Faithful to frozen EN; the body now separates the readings (`方々.md:45-46`). |
| Comprehensibility C1: 方々's «тип» and source-list note | **Resolved** | `方々.md:31-32,45-46`. |
| Comprehensibility C2: 日常 lacks contrasts with 生活, 暮らし and 普段 and an adverbial example | **Resolved** | `日常.md:25-27,41-46,54`; Digital Daijisen 日常. |
| Comprehensibility C3: 支出 and 費用 glosses collide | **Resolved** | `支出.md:34-37,45`; Digital Daijisen 支出 and 費用 sense 1. |
| Comprehensibility optional: 故郷 «поеду домой» | **Optional, adopted** | `故郷.md:20`. |
| Comprehensibility optional: 文字 «буквы» | **Optional, unchanged** | The definition two lines above covers kana, kanji and letters; the reviewer agreed on recheck. |
| Comprehensibility optional: 既に/新た register notes | **Optional, unchanged** | Not in EN; the inspected Daijisen entries mark no restriction; the reviewer agreed on recheck. |
| Comprehensibility recheck optional: 方々's «В записи для слова», 日常 «предметы» for 道具 and «определяет глагол», the デート aside | **Optional, unchanged** | The reviewer judged none an actionable defect; changing them would reopen the reviewed tree for polish only. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN** after fixes (放す).
- Scoped coverage: **CLEAN** after fixes (日付, 日常, 支出).
- Comprehensibility: **CLEAN** after fixes (方々, 日常, 支出).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** throughout, for the reviewed batch and the directly adjudicated pairs; the 日光–光 guard is conservative.
  Exclusions are direct pairs, not transitive groups.

Limits: the rechecks reread only the changed passages and the cards needed to judge them; unchanged cards rest on review 001's full
reading. The correctness reviewer freshly fetched the Digital Daijisen 日常, 支出 and 費用 entries and the Jisho/JMdict entries for
生活, 暮らし, 普段, 方々 and 帰る; the consistency and comprehensibility reviewers did not refetch dictionary pages. No
native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
