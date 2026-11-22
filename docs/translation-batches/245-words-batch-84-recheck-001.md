# Batch 245 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `004903db88a34b30524ca68ffc5b8dfbc085bbfa` | `86483e2d7614ce9f762d411eb04dc4c869602984` | Initial review snapshot: the signed candidate, on `origin/full-ru-245-words-84`. |
| `1dc38a81c432b574cf7cb4923ddcf89c458c879a` | `b0000529b1786cb784280eb3f7054cc5fd84bfd8` | Fix 1 (final candidate). It covers correctness F01 and the correctness optional on 祭る, consistency F1, the optional F2 and the optional removal of 社会科学→自然科学, and comprehensibility C245-01 to C245-15 (C245-03 through the F01 alternative; C245-05 shortened; C245-10 reworded; C245-14 partially). It retitles おやすみ, 符号, 空っぽ, 祖先, 先祖, 敬う, 立ち止まる and 空想, adds three exclusions and one reviewed RU-only link, removes one RU-added exclusion and no link. Signed; on `origin/full-ru-245-words-84`. |

The fix regenerated `manifest.json`; both snapshots record 5,469 entries (5,464 `files` + 3 images + 2 scenes).
`contentVersion` is `28eee95d59bb55f0` at the candidate and `a42418646b3ad082` after fix 1. The intake was not
refreshed; it still records the candidate's payload hashes. The commit message reads "Batch 245 fix 1: apply
blind-review dispositions", followed by a paragraph each for correctness/comprehensibility, comprehensibility and
consistency.

Fix 1:
- `おやすみ` (lines 4, 9, 12 and 30; correctness F01 by its alternative resolution, comprehensibility C245-03 and
  C245-04): title and H1 «выходной; отдых; спокойной ночи» instead of «выходной день (вежливо); отход ко сну
  (уважительно); спокойной ночи»; 佚 appended to `quiz_exclusions`; «Само заголовочное слово записано каной, без
  кандзи.» instead of «Заголовочное слово записано каной, поэтому в его метаданных нет кандзи.»
- `祭る` (lines 16, 20–21 and 36; comprehensibility C245-01 and the correctness optional): the meaning line reads
  «祭る значит «помещать в святилище, обожествлять», а также «молиться, поклоняться».» instead of «祭る значит «почитать
  как божество, помещать в святилище для поклонения», а также «молиться, поклоняться».»; the examples read «— Это
  святилище посвящено богу моря.» and «— На домашнем алтаре помещено божество для поклонения.» instead of «— В этом
  святилище почитают бога моря.» and «— Мы почитаем божество на домашнем алтаре.»; a new line 36 is the reviewed RU-only
  link «[敬う](敬う.md)（うやまう）— «уважать, чтить» человека или божество; это отношение, а не помещение божества в
  святилище.» The title «помещать в святилище; поклоняться (божеству)», set by the coordinator's edit, is unchanged.
- `秤` (line 34; comprehensibility C245-02, verbatim): «Линейка и термометр тоже что-то измеряют, но от этого не
  становятся 秤.» instead of «…но 秤 от этого не становятся.»
- `符号` (lines 4 and 12; comprehensibility C245-05, shortened): title and H1 «условное обозначение; код; знак числа»
  instead of «условное обозначение; кодовое обозначение; знак числа (плюс или минус)».
- `空っぽ` (lines 4, 12, 18 and 33; comprehensibility C245-06 and C245-07): title and H1 «пустой; полый» instead of
  «совсем пустой; полый»; «— Коробка внутри была пустой.» instead of «— Коробка внутри была совсем пустой.»; the sentence
  «Пустая бутылка — 空っぽ, даже если никто не предлагает ею воспользоваться.» is deleted, so line 33 now starts with the
  coordinator's sentence «Свободное время для записи обычно называют 空き, а не описывают как ёмкость без содержимого.»
- `祖先` (lines 4, 12 and 21; comprehensibility C245-08 and C245-15): title and H1 «предок; предшествующие поколения»
  instead of «предок; предшествующие поколения (рода)»; «— Бережём землю, унаследованную от предков.» instead of «— Мы
  бережём землю, унаследованную от предков.»
- `先祖` (lines 4 and 12; comprehensibility C245-08): title and H1 «предки рода; родоначальник» instead of «предки
  (рода); родоначальник».
- `敬う` (lines 4 and 12; comprehensibility C245-09): title and H1 «уважать; чтить» instead of «уважать; почитать».
- `標識` (line 45; comprehensibility C245-10, reworded): «— «языковой показатель» (например, показатель грамматической
  роли);» instead of «— «показатель, маркер» (например, грамматический);».
- `架空` (line 35; comprehensibility C245-11): «Словарь приводит и чтение がくう…» instead of «Просмотренная словарная
  статья приводит и чтение がくう…».
- `磁石` (line 40; comprehensibility C245-12): the citation ends «словарная статья о магните и компасе.» instead of
  «словарная статья о магните и компасе, а не отдельно приведённое название пьесы.»
- `立ち止まる` (lines 4 and 12; comprehensibility C245-13): title and H1 «останавливаться на ходу; делать паузу» instead
  of «останавливаться на ходу; приостанавливаться».
- `空想` (lines 4, 12 and 16; comprehensibility C245-14, partially): title and H1 «мечтание; фантазия; воображаемая
  картина» instead of «грёзы; фантазия; воображаемая картина»; the meaning line opens «空想 — мечтание, фантазия или
  воображаемая картина» instead of «空想 — грёзы, фантазия или воображаемая картина».
- `移転` (line 20) and `確率` (line 19; comprehensibility C245-15): «— Головной офис перевели в Токио.» and «— Рассчитали
  вероятность успеха.» instead of «— Мы перевели головной офис в Токио.» and «— Мы рассчитали вероятность успеха.»
- `童話` (line 9; consistency F1, verbatim): `quiz_exclusions: [話, 物語, 歴史]` instead of `[話, 物語]`.
- `社説` (line 9; consistency optional F2): `quiz_exclusions: [記事, 論文, 評論]` instead of `[記事, 論文]`.
- `社会科学` (line 9; consistency optional): `quiz_exclusions: [科学]`, EN parity, instead of `[科学, 自然科学]`.

All 18 are new Batch 245 cards. No navigation-only file changed after the candidate, so navigation totals stay at 3
files / 3 links (all EN-position restorations, including the held 編集→社説 link).

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Correctness F01 was accepted by an alternative resolution rather than the proposed «сон или отдых (уважительно)»: "The
  comprehensibility review independently found the three-part title too long (C245-03), so the title and H1 now mirror
  EN "day off; rest; good night": «выходной; отдых; спокойной ночи». The register notes remain in the body." The new
  «отдых» segment overlaps 佚 «отдых; непринуждённость», "so 佚 is added to おやすみ's exclusions". At recheck the reviewer
  judged it "RESOLVED by alternative wording. … Exact wording from my proposed remedy is unnecessary."
- Comprehensibility C245-03 was accepted "via the F01 alternative above" instead of the proposed «выходной (вежливо);
  спокойной ночи».
- Comprehensibility C245-05 was accepted in shortened form, «условное обозначение; код; знак числа», "closer to EN
  "symbol; sign; code"; コード is already guarded and the plus/minus detail stays in the body", although the review had
  advised against bare «код».
- Comprehensibility C245-10 was accepted with reworded remedy text: «языковой показатель» (например, показатель
  грамматической роли) instead of «(например, признак грамматической роли)».
- Comprehensibility C245-14 was adopted partially: "«грёзы» → «мечтание»; «воображаемая картина» kept for EN parity
  ("daydream; fantasy; imagined vision")". At recheck the reviewer called it "partially resolved; leftover accepted, not
  a defect."
- Comprehensibility C245-08 was accepted as proposed ("parentheses removed; the pair remains directly guarded"), and
  C245-06 with the title «пустой; полый» rather than the proposed «пустой (без содержимого)» ("Intensifier «совсем»
  dropped").
- The consistency optionals on 上京/移転, 祭日/祭, 税関, 秤, 私立, 磁石, tag parity and the 習慣 link needed no action
  ("reviewer: not required"); the reviewer called them "unchanged and still acceptable" at recheck.
- The comprehensibility optionals (祝日's two title segments, 祭日:25, 社説 «передовица», 童話's «сказку», 私立's long
  title, 窓口, 私鉄 and the notes on 税関 and 祭日) needed no change ("Optionals — no action.").

Post-fix screen: a saved rerun at the committed `1dc38a8` over all 30 batch words (`b245-postfix-screen.txt`, 287
lines; byte-identical to the pre-commit run) has 37 `OK` lines for pairs already guarded by an exclusion and 250 `!!`
lines, all stem-only. Its five exact-segment lines are all guarded by the batch card's own list: 符号–コード «код»
(符号→コード), 空っぽ–からから «пустой» (空っぽ→からから), おやすみ–休み «выходной» and «отдых» (おやすみ→休み), おやすみ–休日
«выходной» (おやすみ→休日) and おやすみ–佚 «отдых» (おやすみ→佚, added by fix 1). The candidate screen had no
exact-segment line; the new おやすみ, 符号 and 空っぽ titles produce these segments. The consistency recheck's exact-segment
screen of the 11 new or changed titles against all 4,003 RU word titles found that none "shares an exact `;`-segment with
any other RU title unless the pair is already guarded".

Net change from the candidate:
- titles and H1s of おやすみ, 符号, 空っぽ, 祖先, 先祖, 敬う, 立ち止まる and 空想;
- example translations in 祭る (two), 空っぽ, 祖先, 移転 and 確率;
- prose in 祭る (meaning line), 秤, おやすみ, 空っぽ (one sentence deleted), 標識, 架空, 磁石 and 空想 (meaning line);
- three exclusions added (おやすみ→佚, 童話→歴史 and 社説→評論) and one RU-added exclusion removed (社会科学→自然科学);
- one reviewed RU-only link added (祭る:36 → 敬う); no link removed or retargeted.

No Japanese example sentence, sourced reading, kanji card or EN exclusion changed. The content diff
`004903d..1dc38a8 -- words` is 18 word files, 35 lines added and 34 removed; with `manifest.json` the fix changes 19
files, 54 lines added and 53 removed.

Fix 1 validation, as recorded in the dispositions: "manifest 5,469 files; validate 0 errors; unittest OK; budget
localZipBytes 7,911,612; `git diff --check` clean; link parity over 18 changed cards: LOST none, EXTRA only 祭る→敬う
(intended); title screen over the 30 batch words: 0 unguarded exact overlaps." The "5,469 files" is the entry count
above. For this record link parity was verified again over the 33 batch paths at `1dc38a8`: LOST only 税関→習慣, and
EXTRA only 祭日→祝日 and 祭る→敬う.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the correctness recheck states "Model identity not verifiable.", the consistency recheck "Model: not verifiable."
and the comprehensibility recheck "Model not verifiable from the session."; the dispositions record comprehensibility as
"grok-4.7 requested; model not verifiable in-session".

The rechecks ran serially, one reviewer at a time, in one round: correctness, then consistency, then comprehensibility,
each on the fix diff `004903d..1dc38a8` (18 word cards and `manifest.json`). This ordering rests on the coordinator's
session records; the recheck reports do not record times. There was no second fix and no follow-up exchange.

Rechecks were returned as separate reports rather than appended to the initial review files: the full texts are in
`b245-recheck-correctness.md`, `b245-recheck-consistency.md` and `b245-recheck-comprehensibility.md` in the
coordinator's session folder, and their content is recorded in the round table below. The recheck briefs were sent
through the agent-messaging channel and were not saved as files; each recheck's scope is described here from its own
Snapshot and Scope lines.

No recheck ran a generator. The correctness reviewer records "No validator, generator, app or media tests run;
coordinator validation claims are not my results. Only this report was written; repositories, HEAD and index
unchanged."; the consistency reviewer ran `python -X utf8 -B tools/validate.py` (0 errors) and records "No repository
file was edited, and no generator was run."; the comprehensibility reviewer records "No repository file edited." and that
it did not "re-run title-screen or link-parity". The correctness recheck records HEAD
`1dc38a81c432b574cf7cb4923ddcf89c458c879a` against parent `004903db88a34b30524ca68ffc5b8dfbc085bbfa` with "Initial/final
worktree and index clean"; the consistency recheck records `1dc38a81c432b574cf7cb4923ddcf89c458c879a` ("HEAD matches")
with an empty `git status --porcelain`; the comprehensibility recheck records HEAD
`1dc38a81c432b574cf7cb4923ddcf89c458c879a` and parent `004903db88a34b30524ca68ffc5b8dfbc085bbfa`, "`git rev-parse HEAD`
matched; `git status --porcelain` empty". The recheck records include no separate coordinator status check after the
rechecks; when these records were drafted, a read-only check showed the RU checkout on `full-ru-245-words-84` at HEAD
`1dc38a81c432b574cf7cb4923ddcf89c458c879a` with `git status --porcelain --ignored` printing nothing.

### Round 1 (`1dc38a8`)

| Facet | Scope and result |
|---|---|
| Correctness | Snapshot `1dc38a8` against parent `004903d`, "Initial/final worktree and index clean". "Correctness and scoped coverage of EVERY changed passage; supplied words/ diff confirmed identical to commit diff. Reviewed all 18 changed files". "Original F01 (LOW), おやすみ:4,12 — RESOLVED by alternative wording. "выходной; отдых; спокойной ночи" restores EN's rest sense without restricting it to bedtime." (JMdict 1612680 senses 1–3). "Original optional, 祭る:20–21 — RESOLVED as an implemented optional improvement, not reclassified as a defect." (JMdict 1295250 senses 1–2; Daijisen 祭る sense 2). The new 敬う comparison "correctly includes people AND deities and contrasts reverence with enshrinement; it does not ban religious uses of 敬う" (Daijisen 敬う includes 神仏を敬う). Changed passages checked: 符号 (JMdict 1497710), 空想 «мечтание» (JMdict 1245730; Kuznetsov), 敬う «уважать; чтить» (JMdict 1250700), 立ち止まる «делать паузу» (JMdict 1551350), 標識:45 (JMdict 1488700 sense 2), 先祖/祖先, the subjectless translations («бережём» "still grammatically encodes first-person plural and must not be described as fully number-neutral"), 空っぽ ("The deleted bottle sentence is not strictly English-only, contrary to the disposition's rationale; nevertheless its emptiness-versus-availability boundary survives at :16,19,29,33. No missing Japanese rule established."), the editorial wording of おやすみ:30, 架空:35, 磁石:40 and 秤:34, and the exclusions ("No original EN exclusion is lost."). "Read-only comparison confirmed all 37 Japanese example/kana pairs in the 18 changed cards match both parent and frozen EN." "New findings: none". Correctness **CLEAN**; scoped coverage **CLEAN** "for this recheck". Optional: "None newly raised." Limits: "Delta recheck, not an exhaustive corpus, comprehensibility, quiz-pool or native-speaker audit. No validator, generator, app or media tests run; coordinator validation claims are not my results." |
| Consistency | `1dc38a8` ("HEAD matches"), `git status --porcelain` empty; `tools/validate.py` 0 errors. Diff `004903d..1dc38a8` "read in full". "F1 童話→歴史: RESOLVED."; "Optional F2 社説→評論: RESOLVED (taken)."; "Optional 社会科学→自然科学 removal: RESOLVED (taken). words/社会科学.md is now `[科学]`, which matches EN."; "Other optionals: unchanged and still acceptable". Screened the 11 new or changed titles against all 4,003 RU word titles (exact segments in code; stems by hand): "No new unguarded overlap was found." "佚 guard (words/おやすみ.md:8, appended `佚`): justified and sufficient", "conservative, with a real lexical basis. EN has no guard because its titles do not share a word." "RU-only link 祭る→[敬う](敬う.md) (words/祭る.md, Синонимы): acceptable." Changed body text "contains no fact that conflicts with the sibling cards". "the sha256 of all 18 changed word files equals the manifest entry. The manifest diff is 18 file entries + contentVersion (38 lines)." Consistency **CLEAN**; quiz safety **CLEAN**; manifest/validation **CLEAN**; "Findings: none." "Optional: none." Limits: "The stem screen of the changed titles against all 4,003 titles used keyword patterns I chose, not an exhaustive semantic check."; "EN prose was not re-compared line by line."; "Reverse-direction guards were not required and were not checked." |
| Comprehensibility | HEAD `1dc38a8`, parent `004903d`, porcelain empty. "Read in full: 祭る, おやすみ, 符号, 空っぽ, 敬う. Read the changed passages of 秤, 標識, 架空, 磁石, 確率, 社会科学, 社説, 祖先, 先祖, 移転, 空想, 立ち止まる, 童話." C245-01, C245-02, C245-04, C245-06 to C245-09, C245-11 to C245-13 and C245-15 **resolved**; C245-03, C245-05 and C245-10 "resolved (other remedy)"; "C245-14 partially resolved; leftover accepted, not a defect." On C245-05: "Bare «код» does not recreate the コード problem: コード is excluded". On C245-15: "«Бережём землю…» still has a first-person ending, which Russian present tense requires; it does not name a new actor." "Regressions: none in the changed prose. 祭る’s contrast does not collapse the cards when the object is a deity." Optional: "unchanged 祭る:16 «почитаемое божество» and :33 «почитание» still use the attitude word, but they are not the definition or 敬う’s title. 祖先’s meaning line still says «поколения рода», then widens to 人類; the title no longer hides that. Not findings." Verdicts: "Comprehensibility: PASS. Scoped coverage: PASS. No remaining finding. Prior coverage exceptions 祭る and 秤 are fixed." Limits: "did not re-read the 12 unchanged batch cards or re-run title-screen or link-parity. Dictionary tags were not re-opened. Model not verifiable from the session." |

The comprehensibility recheck used PASS rather than the report contract's CLEAN label; its wording is quoted as written.
Its optional's line numbers refer to the passages at lines 17 («почитаемое божество») and 34 («почитание») of
`words/祭る.md` at `1dc38a8`. No recheck raised a new finding, so there was no second fix.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F01: おやすみ «отход ко сну (уважительно)» narrows the sonkeigo "sleep; rest" sense (low; correctness and scoped coverage) | **Resolved** (alternative wording) | `おやすみ.md:4,12`; JMdict 1612680 senses 1–3; frozen EN :4. |
| Correctness optional: 祭る:20–21 enshrined-deity wording | **Resolved** under comprehensibility C245-01 | `祭る.md:20–21`; JMdict 1295250; Daijisen 祭る sense 2. |
| Correctness limits and coordinator's unverified gramota.ru checks (神様 «Бог»/«бог», 秤 «весы», 標識 «знак»; HTTP 429) | **UNVERIFIED**; not defects, unchanged | Correctness review checked «весы» and «знак» in actual entries and Бог/бог against Lopatin §180; the coordinator's own checks were rate-limited. |
| Consistency F1: 童話 lacks 歴史 (low) | **Resolved** | `童話.md:9`. |
| Consistency optional F2: 社説→評論 | **Resolved** (taken) | `社説.md:9`. |
| Consistency optional: remove the RU-added 社会科学→自然科学 | **Resolved** (taken); EN parity `[科学]` | `社会科学.md:9`. |
| Consistency classification of the RU-added exclusions | **Recorded** | See the final exclusion set. |
| Consistency optionals: 上京/移転, 祭日/祭, 税関, 秤, 私立, 磁石, tag parity | **No action**; acceptable at recheck | "unchanged and still acceptable". |
| LOST link 税関→習慣 (EN line 35, English-homonym note dropped) | **Accepted**; unchanged | Coordinator, correctness, consistency and comprehensibility reviews; consistency recheck "習慣 plain-text omission" acceptable. |
| RU-only link 祭日:29 → 祝日 (candidate) | **No action**; acceptable | Consistency review "It is acceptable."; correctness review cites Daijisen 祭日 sense 2. |
| Comprehensibility C245-01: 祭る examples and meaning line blur with 敬う (high; comprehensibility and scoped coverage) | **Resolved** | `祭る.md:16,20–21,36`. |
| Comprehensibility C245-02: 秤:34 word order (medium; comprehensibility and scoped coverage) | **Resolved** | `秤.md:34`. |
| Comprehensibility C245-03: おやすみ title too long (medium) | **Resolved** (by the F01 alternative) | `おやすみ.md:4,12`. |
| Comprehensibility C245-04: おやすみ:30 metadata remark (medium) | **Resolved** | `おやすみ.md:30`. |
| Comprehensibility C245-05: 符号 title (medium) | **Resolved** (shortened remedy) | `符号.md:4,12`; JMdict 1497710; コード guarded. |
| Comprehensibility C245-06: 空っぽ «совсем» (medium) | **Resolved** | `空っぽ.md:4,12,18`; JMdict 1245380. |
| Comprehensibility C245-07: 空っぽ:33 bottle sentence (medium) | **Resolved** | `空っぽ.md:33`; correctness recheck: not strictly English-only, but the boundary survives at :16,19,29,33. |
| Comprehensibility C245-08: 祖先/先祖 titles (medium) | **Resolved** | `祖先.md:4,12`; `先祖.md:4,12`. |
| Comprehensibility C245-09: 敬う «почитать» (medium) | **Resolved** | `敬う.md:4,12`; JMdict 1250700. |
| Comprehensibility C245-10: 標識:45 «показатель, маркер» (low) | **Resolved** (reworded remedy) | `標識.md:45`; JMdict 1488700 sense 2. |
| Comprehensibility C245-11: 架空:35 editorial remark (low) | **Resolved** | `架空.md:35`. |
| Comprehensibility C245-12: 磁石:40 dictionary-page remark (low) | **Resolved** | `磁石.md:40`. |
| Comprehensibility C245-13: 立ち止まる «приостанавливаться» (low) | **Resolved** | `立ち止まる.md:4,12`; JMdict 1551350. |
| Comprehensibility C245-14: 空想 «грёзы» and the third segment (low) | **Partially resolved**; leftover accepted, not a defect | `空想.md:4,12,16`; JMdict 1245730; EN parity for «воображаемая картина». |
| Comprehensibility C245-15: added «Мы» subjects (low) | **Resolved** | `移転.md:20`; `確率.md:19`; `祖先.md:21`; «Бережём» still encodes first person plural. |
| Comprehensibility optionals (initial review) | **Optional**; no change, non-blocking | As listed above. |
| Comprehensibility recheck optionals: 祭る:16/:33 (actual lines 17 and 34), 祖先 «поколения рода» | **Optional**; no change | "Not findings." |

Cross-batch note: links to absent targets stay plain. Thirteen EN link occurrences in this batch's new cards, to 11
targets, are absent from RU: words 国立 (from 私立) and 子孫 (from 先祖 and 祖先), and kanji 符 (from 符号), 競 (from 競馬),
童 (from 童話), 税 (from 税関), 移 (from 移転), 鉄 (from 私鉄), 祭 (from 祭日 and 祭る), 敬 (from 敬う) and 祝 (from 祝日).
The other written kanji without an RU kanji card, 架, 標, 率, 磁 and 秤, have none in EN either. One EN link to an
existing card is deliberately dropped: EN 税関:35 reads "English "customs" here does not mean [習慣](習慣.md), habits or
customs."; the RU card omits that English-dependent passage, so link parity reports 税関→習慣 as LOST. There are two
reviewed RU-only links to existing cards, both at substantive comparisons where EN has plain text: 祭日:29 → 祝日
(present at the candidate, accepted by the coordinator) and 祭る:36 → 敬う (added by fix 1). One link was held from an
earlier batch: 編集:33 → 社説 (EN line 34), applied by the candidate script, because 編集 is a Batch 243 card published
before 社説 existed.

## Final exclusion set

All 93 EN exclusion entries (26 lists; EN has none on 税関, 秤, 私立 or 磁石) are retained in EN order; 9 of them lie
inside the batch, and the other 84 target existing RU cards. Four direct, one-sided entries are added on three new cards,
all appended at the end of their lists; none targets a batch word. One was present at the candidate and three were added
by fix 1; fix 1 also removed the candidate's 社会科学→自然科学.

- Candidate (1), accepted by the coordinator "on the B224 precedent": 社説→論文 (論文 «научная статья; диссертация»).
- Fix 1 (3): 童話→歴史 (歴史 «история»; consistency F1), 社説→評論 (評論 «критический анализ (произведений, событий);
  критическая статья»; consistency optional F2) and おやすみ→佚 (佚 «отдых; непринуждённость»; needed once おやすみ gained
  «отдых»), each judged resolved or "justified and sufficient" at the consistency recheck.
- Present at the candidate and removed by fix 1: 社会科学→自然科学 (自然科学 «естественные науки»), which the consistency
  review classed as "unjustified (guards a contrast the article itself teaches; shared «науки» only). It is harmless …
  Optional: remove it, or keep it as conservative."; the dispositions removed it because the titles "are disambiguated
  by their modifiers".

The consistency reviewer classed 社説→論文 as "conservative: it exists only because of the title overlap «статья».
Necessity in an ordinary quiz is not established. It is harmless and may stay.", raised 童話→歴史 as F1 (low, on the RU
precedent of 歴史's own guard), offered 社説→評論 as an optional on the same standard, and classed おやすみ→佚 at recheck as
"conservative, with a real lexical basis". The five exact-segment pairs in the post-fix screen are guarded by the batch
cards' own lists (符号→コード, 空っぽ→からから, おやすみ→休み, 休日 and 佚). Every RU addition is appended at the end of
its list, and no EN entry is removed or reordered. Android applies each declaration symmetrically (EN
`docs/content-format.md`, lines 162–165), so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (おやすみ F01 by its alternative resolution).
- Scoped coverage: **CLEAN** after fix 1 in the correctness recheck (おやすみ F01) and "Scoped coverage: PASS" in the
  comprehensibility recheck (祭る C245-01 and 秤 C245-02); CLEAN throughout in the consistency review.
- Comprehensibility: "Comprehensibility: PASS. Scoped coverage: PASS. No remaining finding." after fix 1 (祭る, 秤,
  おやすみ, 符号, 空っぽ, 祖先, 先祖, 敬う, 標識, 架空, 磁石, 立ち止まる, 空想, 移転 and 確率); the partial C245-14 and the
  modified dispositions stand as accepted.
- Cross-file consistency: **CLEAN** throughout; the three restored navigation links in three files (including the held
  編集→社説 link), the two reviewed RU-only links and the accepted LOST 税関→習慣 stand.
- Quiz safety: **CLEAN** after fix 1 (童話→歴史, 社説→評論, おやすみ→佚 and the removal of 社会科学→自然科学), including
  the eight retitles. This covers the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not
  transitive groups.

## Limits

- The rechecks reread the changed cards or passages and the lines needed to judge them; the unchanged cards rest on review
  001, in which all three reviewers read all 30 cards in full against EN. The comprehensibility recheck did not re-read
  the 12 unchanged batch cards.
- The correctness reviewer's recheck was a delta recheck with no validator, generator, app or media test; its initial
  review met throttled Jisho, kanji API and Gramota requests. The coordinator's gramota.ru checks of 神様, 秤 and 標識
  were rate-limited (HTTP 429) and remain unverified. The consistency reviewer's stem screen used keyword patterns it
  chose, it did not re-compare EN prose line by line, and it did not check reverse-direction guards. The comprehensibility
  reviewer did not rerun the title screen or link parity and did not re-open dictionary tags. Necessity classes are
  judgements, not measurements.
- The recheck briefs were not saved as files; each recheck's scope is taken from its own report.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fix, so its payload hashes describe the candidate `004903d`, not `1dc38a8`.
- Frequency and preferred register (for example «мечтание», «делать паузу», «чтить», «обожествлять», «языковой
  показатель» and «предки рода») were not certified. Online dictionaries were current observations, not pinned archives.
  The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
