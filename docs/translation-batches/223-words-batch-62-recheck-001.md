# Batch 223 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `13805217f9159dadc5849e7e0060bfbc1d2ffc4a` | `4ad1f061cda9d497acf9fc7d5c8b5856d91b254b` | Initial review snapshot: the signed candidate, pushed before review. |
| `8de42d05bc648bcc554d3341078f37a7dfe831c5` | `b1ded6c879a7c2c08d032bf55d0961063b97d2f4` | Fix 1 (final candidate). It covers the three correctness findings and U1, six of the seven comprehensibility findings, three adopted optional items and the intake refresh. Signed and pushed before the rechecks. |

Fix 1 changed eleven word files and regenerated `manifest.json` (`contentVersion` `5d449dcb7c353764`, 4,809 entries; the
candidate had `dc744d5ab990c38a`) and the intake:
- `アイロン` (lines 17 and 20; correctness C1, the reviewer's remedy): EN's first example is restored as the first bullet,
  «シャツにアイロンをかけました。— Я погладил рубашку.». The example is kana-only, so it has no parenthesised reading, as on
  グランド, サイン and くだらない. The prose sentence that had carried the dictionary-form pattern becomes «Первый пример
  описывает действие, а アイロンがある просто сообщает, что утюг есть.»
- `アイスクリーム` (line 28; correctness C2, the reviewer's remedy with «подсказки» for «помогающего»): «[クリーム](クリーム.md)
  обычно означает сливки или крем; словарь отмечает и сокращённое значение «мороженое», но без подсказки контекста полное
  アイスクリーム яснее.» instead of the categorical «…; само по себе это слово не называет замороженный десерт». JMdict 1044480
  sense 2 (abbreviation of アイスクリーム), which the new クリーム card itself teaches.
- `もっとも` (lines 4 and 12; correctness C3a and comprehensibility C5, merged): title and H1 «разумный; обоснованный;
  впрочем» instead of «разумный (о доводе); впрочем». «Обоснованный» keeps EN's two-way scope; the card's もっともな質問
  example is no longer narrower than its title. Gramota обоснованный.
- `まるで` (correctness C3b):
  - Lines 4 and 12: title and H1 «словно; совершенно; совсем не» instead of «словно; совсем не», after EN's affirmative
    "completely" (JMdict 1216280 sense 3).
  - Line 16: «…С отрицательным сказуемым оно может значить «совсем не», а с утвердительным — «совершенно».»
  - Line 21: «Утвердительное употребление усиливает, например, различие: 前とはまるで違う… — «Совершенно отличается от того,
    что было раньше».» instead of «Ещё оно усиливает различие: … — «Совсем не так, как раньше».», whose negative rendering
    hid the affirmative predicate.
  - Line 9: `quiz_exclusions` gains 完全 «…; совершенный», a conservative guard for the new «совершенно» (an "entirely"
    reading of the adjective is plausible). The exact segment «совершенно» belongs to 全く and 全然, already guarded.
- `だって` (correctness C3c and comprehensibility C6, merged):
  - Lines 4 and 12: title and H1 «потому что; но; даже; тоже» instead of «потому что (оправдываясь); даже; тоже», after EN
    "because; but; even; too" (JMdict 2643970 senses 1–2). The body still says that the reason use can sound like an excuse.
  - Line 19 (comprehensibility C6, the reviewer's remedy): «— «Но есть ещё то, что я хочу посмотреть».» instead of «Но я
    ещё не всё посмотрел, что хотел», which asserted a partially completed viewing that まだ見たい物があるよ does not state.
  - Line 9: `quiz_exclusions` gains しかし, けれど and けれども. The new «но» is the exact title segment of those three cards;
    でも and だけど were already guarded.
- `キャンプ` (correctness U1 and comprehensibility C2, merged):
  - Lines 4 and 11: title and H1 «лагерь на природе; стоять лагерем» instead of «кемпинг; лагерь на природе» (the
    comprehensibility reviewer's title).
  - Line 15: the definition drops «, кемпинг», and キャンプに行く is glossed «поехать отдыхать в лагерь на природе».
  - Line 18: the example translation «Я собираюсь с друзьями поехать отдыхать в лагерь на природе.» instead of «…в кемпинг».
  - Line 24: キャンプ場 «место для лагеря на природе; оборудованное такое место по-русски может называться кемпингом.»
  - Line 32: «Русское «кемпинг» обычно значит оборудованный лагерь для автотуристов, а キャンプ такого объекта не требует.» is
    added, and «Фраза о поездке в лагерь на природе…» replaces «…в кемпинг…». Evidence: Kuznetsov and Krysin кемпинг on
    Gramota, Ozhegov кемпинг and Russian Wiktionary кемпинг define an equipped camp for motor tourists; JMdict 1042200
    sense 1 covers camp and camping.
- `エネルギー` (lines 4 and 12; comprehensibility C3, the reviewer's remedy): title and H1 «энергия» instead of «энергия;
  запас сил», which fitted neither the solar nor the food sense taught on the card (JMdict 1029430 senses 1–4). The exact
  segment «энергия» belongs to 活気 «оживление; энергия», already guarded both ways.
- `アウト` (comprehensibility C4, accepted with modified wording):
  - Line 16: «…например, мяч за линией в теннисе. В бейсболе это другое решение — вывод игрока нападения из игры, а не выход
    мяча за линию.» instead of «…мяч за линией в теннисе или аут в бейсболе.»
  - Line 21: «…«второй аут в бейсболе»: здесь это второй вывод игрока нападения из игры.»
  - Line 29: «В бейсболе セーフ противопоставлено такому выводу из игры. В теннисе и похожих играх アウト противопоставлено
    イン — решению, что мяч попал в поле.» instead of «セーフ противопоставлено ауту в бейсболе, а イン — мячу за пределами
    поля.», which could teach イン as the out ball. The reviewer's «イン — решению, что мяч ещё в поле», placed as the
    object of «противопоставлен», would itself have inverted the pair, so the sentence was restructured. JMdict 1014680
    senses 1 and 2.
- `ところが` (line 19; comprehensibility C7, the reviewer's remedy): «— Я достаточно потренировался. А на самом выступлении
  всё же потерпел неудачу.» instead of «Я хорошо подготовился. А на самом выступлении всё же ошибся.», following
  十分に練習しました and 失敗しました.
- `まさに` (line 33; comprehensibility optional item, adopted): «…; здесь まさに не заменяет 正しく.» instead of «…; まさに там
  正しく не заменяет.»
- `キャプテン` (line 15; correctness and comprehensibility optional item, adopted): «Типичный контекст — спортивная команда,
  …» instead of the calque «Полезная обстановка для этого слова — …».
- The intake note now names the fixed cards, and the eleven candidate hashes were refreshed.

Before the fix commit, the coordinator's word title screen ran on the changed titles (もっとも, まるで, だって, キャンプ and
エネルギー):
- Every exact-segment overlap is guarded: まるで with 全く and 全然 («совершенно», «совсем не») and with さっぱり and ちっとも
  («совсем не»); だって with けれど, けれども, しかし, だけど and でも («но») and with なぜなら («потому что»); エネルギー with
  活気 («энергия»).
- Stem-only neighbours, with different referents or word classes, got no guard: もっとも with もちろん «разумеется»; まるで
  with 上達, 成人, 真っ赤 and 際; キャンプ with 天然, 樹脂 and 自然 («природ») and 立つ «стоять; вставать»; エネルギー with
  きびきび and ごしごし («энергично»). «Обоснованный» has no exact segment elsewhere.

Net change from the candidate:
- five retitles (もっとも, まるで, だって, キャンプ, エネルギー);
- body wording in アイスクリーム, まるで, キャンプ, アウト, まさに, キャプテン and アイロン's pointer sentence;
- one restored EN example (アイロン) and three example translations (だって, キャンプ, ところが);
- four added exclusion entries on two cards (だって, まるで).

No Japanese example sentence was altered, and no sourced reading, EN exclusion or link changed. The content diff is eleven
word files, 28 lines added and 27 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, one reviewer at a time, all on fix 1, in this order: correctness, consistency, comprehensibility.
No recheck raised a new finding, so no second fix was needed.

Each reviewer appended to its own report file, which stayed in its session context. Each recheck brief gave the reviewer:
- the fix commit, the reviewed candidate as the base, and the read-only rules;
- the actual content diff `1380521..8de42d0`;
- the coordinator's evidence for every change, the title-screen results and the declined items, stated without the other
  reviewers' reports;
- the reviewer's original verdicts and the disposition of each of its own findings. The comprehensibility brief stated
  the coordinator's reasons for not adopting C1 in this batch and asked the reviewer whether it maintained the finding.

The three briefs, each longer than about 20 KB, were delivered as session files that the reviewers were told to read in full.

All recheck messages forbade running `tools/build_manifest.py` or any other generator. Every recheck section states that
none was run. The correctness and consistency reviewers each ran `tools/validate.py` once (0 errors each); the
comprehensibility reviewer did not report running a validator. The fix script checked `git status --porcelain` after the
fix commit. Before the comprehensibility recheck and after it, the coordinator confirmed that HEAD was `8de42d0` and that
`git status --porcelain --ignored` was empty.

### Round 1 (`8de42d0`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer read the whole recheck packet, verified that the supplied word diff was identical to the actual Git diff, and read all eleven revised cards in full; it did not re-review unchanged cards. C1 is resolved: the past-tense shirt-ironing example is restored verbatim with an accurate completed-action translation, and an all-kana example needs no duplicate reading. C2 is resolved: the recorded abbreviated ice-cream sense is acknowledged, and contextual clarity replaces the categorical exclusion. C3a, C3b and C3c are resolved: もっとも's broader adjective label agrees with its question and opinion examples, まるで keeps affirmative completeness, and だって keeps the adversative «но»; removing the excuse qualifier is safe because the body keeps the defensive register. U1 is resolved by the changed wording, not by verifying a broad Russian «кемпинг»: the noun and the explained suru activity cover camp and camping without requiring equipped premises for motor tourists. The キャプテン optional item is resolved (adopted). Regression checks: だって keeps the current wish, ところが the sufficient practice and the actual failure, まるで comparison, negative emphasis and affirmative completeness; エネルギー's single title covers all four retained domains; アウト now separates the baseball retirement of a batter or runner from the tennis line call and pairs セーフ and イン by sport. Evidence: JMdict 1042200, 1014680 and 1216280 re-inspected; デジタル大辞泉 アウト 1a/1b on Kotobank confirms the baseball and tennis senses and their opposite calls; Gramota обоснованный. Correctness and scoped coverage are **CLEAN**. |
| Consistency | Navigation: the diff touches no link target; the changed link lines (アイスクリーム→クリーム and 氷, アウト→外, キャンプ→テント) keep their hrefs, so there are still seven navigation links and six RU-only links. All eleven changed cards match their `manifest.json` SHA-256, and the validator passes. New exclusions: だって→しかし, けれど and けれども are **required** (exact «но» segment; titles «однако; но» and «но; хотя»); まるで→完全 is **conservative** («совершенно» against «полный (без изъянов); совершенный»). Both lists are well-formed, and every target exists. Titles: だって overlaps by exact segment only with the guarded しかし, けれど, けれども, だけど, でも and なぜなら; まるで's «совершенно» is guarded against 全く, 全然 and 完全; もっとも has only stem neighbours (無理 «неразумный», 慎重 «благоразумный», もちろん), which are not defensible answers; キャンプ has no exact overlap (テント and 自然 are stem-level) and carries no exclusions; エネルギー→活気 stays required (exact «энергия»), and エネルギー→余裕 stays conservative because 余裕's title still contains «сил», so no guard is orphaned. The アイロン ore sentence and the きちんと/丁寧 guard were withdrawn as optional items: Russian «утюг» has no such polysemy, and no guard is needed. No regression was found. Consistency, quiz safety and scoped integration are **CLEAN**. |
| Comprehensibility | The reviewer read the eleven changed cards. C1 is **withdrawn**: the reviewer no longer maintains it. The notes already name the source language in Russian, the kana point does not need the Latin token, and the same line is the reviewed pattern (`words/ゴール.md:27`; also ビデオ, ホーム and グランド), so dropping it on seven cards would split that convention; the unread token is an unused citation, not a misreading. C2 is resolved: the title, H1 and trip gloss no longer use «кемпинг» as the activity, and the body limits it to an equipped camp for motor tourists, which キャンプ does not require. C3 is resolved: the title is «энергия», with the solar and food senses in the body. C4 is resolved: tennis keeps the ball out, baseball is a putout rather than the ball leaving the field, and line 29 pairs セーフ with the putout and イン with the in-field call, so イン is not the out ball; the reviewer judged this clearer than its own remedy. C5 is resolved: «(о доводе)» is gone, «разумный» still leads and the question example stays «разумный вопрос». C6 is resolved: the title has «но» and no longer defines an excuse, and the second translation no longer states a partial completed viewing. C7 is resolved: «достаточно потренировался» is practising, and «потерпел неудачу» matches 失敗しました. The まさに and キャプテン optional items are adopted and clear; アイロン's restored past example removes the tense point; なぜなら already has two Russian sentences; もしも «а если» stays optional. Regressions: none; アイスクリーム now agrees with `クリーム.md` on the short ice-cream sense, and まるで's «совершенно» matches affirmative 違う and is separated from the negative. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: アイロン's first EN example replaced by a prose pattern (minor) | **Resolved** | `アイロン.md:17,20`; frozen EN `アイロン.md:20`; JMdict 1014590 sense 1. |
| Correctness C2: アイスクリーム categorically denies クリーム's ice-cream sense (minor) | **Resolved** | `アイスクリーム.md:28`; JMdict 1044480 sense 2; RU `クリーム.md:33`. |
| Correctness C3a: もっとも «(о доводе)» narrows the adjective (minor) | **Resolved** (jointly with comprehensibility C5) | `もっとも.md:4,12`; JMdict 1535810 sense 2; Gramota обоснованный. |
| Correctness C3b: まるで omits the affirmative "completely" (minor) | **Resolved** | `まるで.md:4,9,12,16,21`; JMdict 1216280 sense 3. |
| Correctness C3c: だって omits the adversative "but" (minor) | **Resolved** (jointly with comprehensibility C6) | `だって.md:4,9,12`; JMdict 2643970 sense 2. |
| Correctness U1: キャンプ equates the activity with Russian «кемпинг» (unverified qualification) | **Resolved** by changed wording (jointly with comprehensibility C2) | `キャンプ.md:4,11,15,18,24,32`; Kuznetsov and Krysin кемпинг on Gramota; Russian Wiktionary кемпинг. The broad Russian use was not verified; the card no longer relies on it. |
| Correctness optional: キャプテン «Полезная обстановка» calque | **Optional, adopted** | `キャプテン.md:15`. |
| Consistency optional: restore アイロン's first EN example | **Optional, adopted** (through correctness C1) | `アイロン.md:17`. |
| Consistency optional: restore アイロン's EN closing sentence on iron supplements and ore | **Withdrawn** | It answers the English polysemy of "iron"; the RU card names only the clothes iron and the hair iron, and Russian «утюг» has no such polysemy. The reviewer agreed in its recheck. |
| Consistency optional: やや's dropped community-source remark; the RU-only text on まさに, まあ and エネルギー | **Accepted as reviewed** | The reviewer judged the omission and the additions sensible; «запас сил» later left エネルギー's title (comprehensibility C3). |
| Consistency optional: an きちんと/丁寧 guard | **Withdrawn** | No exact or near-exact title overlap; the reviewer agreed that it is not needed. |
| Comprehensibility C1: Latin-script source names in seven loanword notes (minor) | **Withdrawn** by the reviewer at recheck | Not adopted in fix 1: naming the source word after the source language («заимствование из английского …») is the provenance convention on published reviewed cards, including `ゴール.md:27`, ビデオ, ホーム and グランド, and no explanation on these cards depends on knowing the English word. The reviewer withdrew the finding rather than split the convention. |
| Comprehensibility C2: キャンプ «кемпинг» narrower than the Japanese (minor) | **Resolved** (merged with correctness U1) | `キャンプ.md:4,11,15,18,24,32`; Ozhegov кемпинг; JMdict 1042200 sense 1. |
| Comprehensibility C3: エネルギー «запас сил» fits neither solar nor food energy (minor) | **Resolved** | `エネルギー.md:4,12`; JMdict 1029430 senses 1–4. |
| Comprehensibility C4: アウト's baseball sense read as the ball leaving the field; イン read as the out ball (minor) | **Resolved** (modified wording) | `アウト.md:16,21,29`; JMdict 1014680 senses 1–2; デジタル大辞泉 アウト 1a/1b on Kotobank. |
| Comprehensibility C5: もっとも «(о доводе)» (minor) | **Resolved** (merged with correctness C3a) | `もっとも.md:4,12`. |
| Comprehensibility C6: だって's excuse-defining title and partial-viewing translation (minor) | **Resolved** | `だって.md:4,12,19`; JMdict 2643970 senses 1–2. |
| Comprehensibility C7: ところが turns practice into readiness and softens failure (minor) | **Resolved** | `ところが.md:19`. |
| Comprehensibility optional: まさに's last nuance sentence | **Optional, adopted** | `まさに.md:33`. |
| Comprehensibility optional: なぜなら:18 as two Russian sentences | **Optional, not adopted** | RU follows EN's one-sentence translation; the Japanese shows なぜなら sentence-initially, and example 1 already keeps two Russian sentences. The reviewer accepted this at recheck. |
| Comprehensibility optional: アイロン:19 tense of the pattern gloss | **Resolved** through correctness C1 | The past example is restored, and the pointer sentence no longer glosses a pattern. |
| Comprehensibility optional: もしも «а если» | **Optional, not adopted** | «А если» is an ordinary Russian opener for an emphatic supposition and distinguishes もしも from もし «если» (guarded); the examples render the conditional itself. The reviewer kept it optional. |
| Exclusion classification | **Reviewer's classification adopted** | The author's and the consistency reviewer's candidate classifications differ only in strength (table in review 001); the reviewer rates four author-"conservative" entries as required. For the fix entries the reviewer classed だって→しかし, けれど and けれども as required and まるで→完全 as conservative, as the coordinator's dispositions had. |

Cross-batch note: links to absent targets stay plain. Six EN link targets in this batch's new cards are absent from RU:
オーバーコート, インキ, 墨, ところで, えっと and ちゃんと. ところで (from ところが) and ちゃんと (from きちんと) are Batch 224
words, so those two links are held for that batch; the other four targets are not in Batch 224. The テント→キャンプ link held
by Batch 222 was restored in this batch.

## Final exclusion set

All 55 EN exclusion entries (18 lists) are retained. Twenty direct, one-sided entries are added on 12 new cards (two of them
new lists, クラシック and ウイスキー):

- Required (15): クラシック→音楽, オーバー→越す, エネルギー→活気, だけど→でも, もしも→もし, まるで→ちっとも, まさに→もうすぐ and
  そっくり→似る; the four entries the reviewer raised from the author's "conservative", namely ウイスキー→酒, ウイスキー→お酒,
  やや→少々 and そっくり→全体; and, added in fix 1, だって→しかし, だって→けれど and だって→けれども.
- Conservative (5): オーバー→越える, エネルギー→余裕, まさに→すなわち and まあ→あ, and, added in fix 1, まるで→完全.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the fix (アイロン, アイスクリーム, もっとも, まるで, だって; キャンプ's U1 resolved by wording).
- Scoped coverage: **CLEAN** after the fix (アイロン's restored example and the もっとも, まるで and だって titles).

- Comprehensibility: **CLEAN** after the fix (キャンプ, エネルギー, アウト, もっとも, だって, ところが); C1 withdrawn by the reviewer.

- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** throughout, including the fix-1 entries on だって and まるで. This covers the reviewed batch and the
  directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the cards needed to judge them. The unchanged cards rest on review
  001's full reading.
- The broad modern Russian use of «кемпинг» for any nature camp was not verified; the card no longer depends on it.
- The comprehensibility reviewer sampled the loanword provenance pattern rather than recounting it. The dispositions and
  the recheck brief put the convention at 65 published cards, which was an overcount. A later regex recount found 51
  published cards before this batch that name a Latin-script source word after the source language. It counts the shared
  wording only and does not review each card. The withdrawal rests on the reviewed pattern, not on the figure.
- Outside this batch's diff, the published `words/最も.md` calls 尤も «часто записываемое», while JMdict 1535810 and this
  batch's もっとも card call it rare. It is recorded for a follow-up and was not changed here.
- No native certification was obtained for «вывод игрока нападения из игры», «потерпел неудачу» or «а если». The
  comprehensibility reviewer could not open JMdictDB, which was password-gated, and relied on Jisho and Ozhegov on gufo.me.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.
