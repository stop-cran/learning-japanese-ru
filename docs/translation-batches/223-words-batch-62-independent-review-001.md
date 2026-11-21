# Batch 223 — independent review 001

## Snapshot and scope

- Reviewed commit: `13805217f9159dadc5849e7e0060bfbc1d2ffc4a` (tree `4ad1f061cda9d497acf9fc7d5c8b5856d91b254b`), branch
  `full-ru-223-words-62`, parent `8a759e5`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 222 candidate `d0d6d08431a1e7dd81d6eaa151a8c841c37c297e`.
    Before copying, the coordinator checked two things: that the 6 navigation files edited there were unchanged between
    `d0d6d08` and the candidate's parent `8a759e5`, and that none of the 30 new cards existed there. The Batch 222 fixes
    touched only カード, ダイヤ, スター, スタンド, ソファー, トラック, デート, スープ and ジュース; none of them is in this batch's
    path set.
  - The coordinator byte-compared the 36 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 37 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - One held wrap was carried into this batch: Batch 222's テント had left its EN link to キャンプ as plain text because
    キャンプ is a Batch 223 word. The coordinator wrapped that mention at EN's position (テント line 28) in the primary
    checkout, on top of the published テント card; it is the only change to that card.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 7 files with 7 restored navigation links (including the held テント→キャンプ link);
    - `manifest.json` (`contentVersion` `dc744d5ab990c38a`, 4,809 entries);
    - the intake.
- Published baseline recorded in the intake: `85b913449b7dac1efacf8d72578ef94a5a87f04c` (Batch 222 merge). Parent
  `8a759e5` adds only the Batch 222 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK;
  - content budget: OK;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 7 files and 7 links, with no problem;
  - title screen: no unguarded exact title-segment overlap;
  - link parity: no EN link lost where the RU target exists, and six RU-only links (クリーム→アイスクリーム, エネルギー→活気,
    まさに→ちょうど, まさに→もうすぐ, まあ→あ and くっつける→結婚). EN mentions アイスクリーム, ちょうど and the marriage noun
    unlinked in the same comparison; 活気, もうすぐ and あ are RU-added comparisons that explain the corresponding quiz
    guards.
- Common sample: all three reviewers read all 30 new word cards in full, each against its full EN original. The
  consistency reviewer compared them by script and by eye.
- Correctness review scope:
  - Read in full the existing RU あ, ああ, 活気, ちょうど, もうすぐ and 結婚 (the RU-only link targets and the あ/ああ
    contrast) and テント (the held-link card); inspected the changed passages in ざっと, ふと, ワイン, 万一, 思わず and 流れる;
    read the three binding instruction and format files.
  - Fetched the Jisho (JMdict) page of every headword and checked the cited entry ids, including 1044480 (クリーム),
    1042200 (キャンプ), 1029430 (エネルギー), 1014680 (アウト), 1014590 (アイロン), 1535810 (もっとも, distinguished from
    最も), 1216280 (まるで) and 2643970 (だって), with the spelling notes for 態と, 稍, 尤も, 若しも, 丸で and 真逆.
  - Russian sources: Gramota and Kuznetsov entries for the food, captain, overcoat and limit, energy and reserve, sports,
    connective, degree and manner glosses, among them разумный, довод, кемпинг, лагерь, полно, поскольку, впрочем,
    вплотную, придвинуть, держаться and запас; Russian Wiktionary кемпинг.
  - Ran `tools/validate.py` (0 errors); ran no generator. Initial Gramota HTTP 429 responses and oversized dictionary and
    diff outputs were followed by successful bounded reads; a search summary whose page fetch failed was not counted as
    evidence.
- Consistency review scope:
  - Read all 30 cards against EN, the seven navigation diffs and the RU quiz and link rules in full, and compared front
    matter, link pairs, exclusion lists and path forms with EN by script.
  - Checked all 37 changed or new content hashes against `manifest.json` (no mismatch). It checked the intake only for its
    keys and the absence of learner prose; it did not compare the path list entry by entry.
  - Ran `tools/validate.py` (0 errors) and its own read-only title-overlap screen over all RU word titles, judging the
    stem hits by hand.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN and テント in full; opened あ, ああ, もし, 最も and 万一 for the named contrasts; and
    inspected the restored-link hunks in ざっと, ふと, ワイン, 思わず and 流れる.
  - Ran the coordinator-supplied read-only `link_parity.py` (no lost link) and `word_title_screen.py`, using the screen
    only as a lead. Checked senses on Jisho's public pages (JMdictDB was password-gated) and Russian usage in Ozhegov
    on gufo.me. It did not report running the content validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; each report says its model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time; the coordinator verified HEAD `1380521` and a clean tree before each
  launch. Each report records the snapshot `1380521` with an empty `git status --porcelain`. No fix was applied until
  all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `223-words-batch-62-review-correctness-001.md`
  - `223-words-batch-62-review-consistency-001.md`
  - `223-words-batch-62-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`, except
    that the consistency reviewer checked only the intake's keys and the absence of learner prose;
  - the scratch worktrees;
  - one another's reports.

  The correctness report confirms that it consulted no author or reviewer material, batch or tracking record or scratch
  worktree. The consistency report confirms that it read no author report, title-screen output, batch or draft record,
  tracking file or scratch worktree. The comprehensibility report does not restate the rules; it ran the title-screen
  tool itself rather than reading the coordinator's output.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** (アイスクリーム; the もっとも title qualifier); scoped coverage **NEEDS FIX** (アイロン,
もっとも, まるで, だって). キャンプ's Russian activity equivalence is **UNVERIFIED** (U1). The other new cards are **CLEAN**
in both facets.

- C1 (minor; high confidence), `アイロン.md:17–19`: EN's first example シャツにアイロンをかけました。 is replaced by the
  dictionary-form pattern シャツにアイロンをかける in prose; the construction survives, but the required verbatim example
  and its past-tense translation do not. Remedy: restore it as the first bullet with «— Я погладил рубашку.». Evidence:
  frozen EN `アイロン.md:20`; JMdict 1014590 sense 1.
- C2 (minor; high confidence), `アイスクリーム.md:28`: «само по себе это слово не называет замороженный десерт» makes a
  categorical exclusion for クリーム, although the new クリーム card itself correctly teaches that クリーム abbreviates
  アイスクリーム; the unqualified sentence can teach a learner to reject a recorded meaning. The defect is inherited from EN,
  but inheritance does not reconcile the contradiction. Remedy: «[クリーム](クリーム.md) обычно означает сливки или крем;
  словарь отмечает и сокращённое значение «мороженое», но без помогающего контекста полное アイスクリーム яснее.» Evidence:
  JMdict 1044480 sense 2 "ice cream", tagged abbreviation, see also アイスクリーム; RU `クリーム.md:33`. The evidence
  supports recognition, not a frequency ranking.
- C3 (minor; high confidence on the omissions, medium-high on «о доводе»): three short titles prune the source title
  although the bodies keep most of the teaching:
  - `もっとも.md:4,12`: «разумный (о доводе)» restricts the adjective below the card's own もっともな質問 and もっともな意見;
    a question is not necessarily a «довод». Remedy: «разумный; обоснованный; впрочем». Evidence: JMdict 1535810 sense 2;
    Kuznetsov разумный sense 3 and довод.
  - `まるで.md:4,12`: «словно; совсем не» omits EN's affirmative "completely"; RU line 21 still teaches the positive
    predicate 違う, but its rendering «не так» hides that point. Remedy: «словно; совершенно; совсем не», with «Совершенно
    отличается от того, что было раньше» at line 21. Evidence: JMdict 1216280 sense 3.
  - `だって.md:4,12`: «потому что (оправдываясь); даже; тоже» omits EN's independent adversative "but", which RU line 19
    correctly renders «Но». Remedy: add «но». Evidence: JMdict 2643970 sense 2.
- U1 (minor; unresolved evidence qualification), `キャンプ.md:4,15,18,24,32`: the card equates the activity with Russian
  «кемпинг» and translates going camping as going to a «кемпинг», while the inspected dictionaries define «кемпинг»
  more narrowly as an equipped camp for motor tourists; キャンプ sense 1 covers both camp and camping. This is not proof
  that a broader modern use is impossible. Remedy: supply evidence for the broader use, or make the activity explicit,
  for example «отдых в лагере на природе; лагерь на природе», キャンプに行く «поехать отдыхать в лагерь на природе», and
  mention «кемпинг» only as a possible kind of site. Evidence: JMdict 1042200 sense 1; Kuznetsov and Krysin кемпинг on
  Gramota; Russian Wiktionary кемпинг; Kuznetsov лагерь sense 2.

What the reviewer confirmed:
- Source `word`, `reading`, `jlpt`, `type`, `kanji` and `tags` are unchanged and the original exclusions are retained.
  Every EN link whose RU target exists is retained, and links to absent targets are plain text; the restored
  テント→キャンプ link is coherent. Apart from C1, no changed Japanese example or reading and no lost body teaching point
  was found. オーバー keeps EN's hiragana reading おーばー; dropping English-only contrast, pronunciation and community-source
  remarks was not mechanically required.
- The six RU-only links were checked against the target cards and dictionary meanings, and no unsupported substitution
  ban was found. あ is the interjection 2394370, not 亜; 活気 is liveliness, not physical or food energy; もうすぐ's
  nearness contrasts appropriately with the immediate-stage まさに…としている; the matchmaking sense of くっつける is
  colloquial.
- まあ's female-language label is attached only to the exclamatory sense. Calming «полно» is attested in conversational
  use (Gramota полно sense 2), «поскольку» means «так как, потому что», «впрочем» introduces a qualification, and
  «вплотную», «придвинуть», «держаться» and «запас» are supported by their dictionary senses.

Optional: キャプテン:15 «Полезная обстановка для этого слова» is an awkward calque; «Типичный контекст — спортивная команда»
reads more naturally. Limits: U1 is unresolved; no native-speaker, frequency or whole-pool quiz certification; validation
is structural, not semantic.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **CLEAN**; scoped integration (links, manifest, intake) **CLEAN**. No finding
was established.

What the reviewer confirmed:
- Every card's front matter other than `quiz_exclusions` equals EN, and every EN exclusion is retained. Exclusions are
  direct pairs, not transitive groups.
- Every RU link target exists. EN links to absent targets (オーバーコート, インキ, 墨, ところで, えっと and ちゃんと) stay plain
  text, and the kanji link to 付 resolves.
- Each navigation diff changes only the link brackets at the EN-linked position: ざっと→きちんと, ふと and 思わず→わざと,
  テント→キャンプ, ワイン→ウイスキー, 万一→もしも (line 28, at EN line 32; line 34 stays unlinked, as at EN line 39) and
  流れる→インク. Paths use the `X.md` form.
- Each of the six RU-only links sits on a substantive comparison sentence and is acceptable.
- All 37 changed or new content hashes match `manifest.json`, and the manifest touches no unrelated file.
- Pairs deliberately left unguarded, with which the reviewer agreed, included キャンプ/テント, キャプテン/チーム,
  オーバー/限界, わざと/偶然, わざと/つもり and 意思, アイスクリーム/クリーム (the EN guard sits on クリーム), クリーム/バター,
  きちんと/丁寧, やや/くらい, まるで/真っ赤, くっつく/態度 and 浮く. Reverse pairs are covered where an existing card already
  excludes the new one (ところが/だが, なぜなら/だって).

Optional: restore アイロン's first EN example and its closing sentence that neither sense is an iron supplement or ore
(fidelity polish only); やや drops EN's remark on the community-source interjection, and まさに, まあ and エネルギー add
RU-only text (the もうすぐ comparison, the あ/ああ note and «запас сил»), all judged sensible; an きちんと/丁寧 guard could be
added conservatively but is not needed. Limits: dictionary senses were taken from the cited JMdict entries and the
titles, without a fresh online check; the screen's stem noise was judged by hand; the intake path list was not compared
entry by entry; no device or app quiz run.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (アイスクリーム, クリーム, クリスマス, クラシック, キャンプ, キャプテン, エネルギー,
アウト, だって, ところが and もっとも; the other 19 cards are clean in this facet); scoped coverage **CLEAN** for all 30.

- C1 (minor; high confidence), `アイスクリーム.md:24`, `クリーム.md:25`, `クリスマス.md:24`, `クラシック.md:25`,
  `キャンプ.md:24`, `キャプテン.md:24` and `エネルギー.md:25`: the loanword notes name the Latin-script source word (ice
  cream, cream, Christmas, classic or classical, camp, captain, Energie). A beginner without English cannot use it, and
  the spelling lesson does not need it. Remedy: drop the foreign name and keep the kana note, for example «Это
  заимствование, записанное катаканой; кандзи для разбора здесь нет.», and for エネルギー «Словарь указывает немецкий
  источник.» Evidence: the RU audience rule that learner text must be understandable without English.
- C2 (minor; high confidence), `キャンプ.md:4,15,18,32`: the lead gloss «кемпинг» is used as both the activity and the
  camp, but ordinary Russian «кемпинг» is an equipped summer camp for motor tourists. Remedy: title «лагерь на природе;
  стоять лагерем» and a body note that «кемпинг» usually means such an equipped camp, while キャンプ does not require one.
  Evidence: Ozhegov кемпинг; JMdict 1042200 sense 1.
- C3 (minor; high confidence), `エネルギー.md:4`: «запас сил» is narrower than the taught range and adds a stockpile the
  Japanese does not require; it fits neither solar nor food energy, both taught on the card. Remedy: title «энергия».
  Evidence: JMdict 1029430 senses 1–4.
- C4 (minor; high confidence), `アウト.md:16,21,29`: «аут в бейсболе» and «второй аут» will be read as the ball leaving the
  field, but the baseball sense is a putout; and «а イン — мячу за пределами поля» uses the card's definitional dash, so
  イン can be learned as the out ball. Remedy: describe the baseball sense as putting the batter out, not the ball leaving
  the field, and pair セーフ with that putout and イン with the ball being in the field. Evidence: JMdict 1014680 sense 1
  (see also イン) and sense 2 (baseball, see also セーフ); Ozhegov аут.
- C5 (minor; high confidence), `もっとも.md:4`: the qualifier «(о доводе)» is narrower than the card's own rule and its
  «разумный вопрос» example. Remedy: «разумный; впрочем». Evidence: JMdict 1535810.
- C6 (minor; high confidence), `だって.md:4,19`: the title makes excuse-giving definitional and omits «но», although the
  body says only that the reason use can sound like an excuse, and the second example is an objection. Its translation
  «я ещё не всё посмотрел, что хотел» states a partially completed viewing, whereas まだ見たい物があるよ says only that
  there are still things the speaker wants to see. Remedy: title «потому что; но; даже; тоже»; translation «Но есть ещё
  то, что я хочу посмотреть». Evidence: JMdict 2643970 senses 1–2.
- C7 (minor; high confidence on 練習, medium on «ошибся»), `ところが.md:19`: «Я хорошо подготовился» states a readiness
  result, whereas 十分に練習しました is the act of practising enough, and «ошибся» is softer than 失敗しました. Remedy: «Я
  достаточно потренировался. А на самом выступлении всё же потерпел неудачу.»

What the reviewer confirmed: no Cyrillic reading, quiz-behaviour sentence or author note; the restored links are
consistent; the title-screen stem hits it examined (рожде, класс, запас, полно) are not usable answers for one another.

Optional: まさに's last nuance sentence «まさに там 正しく не заменяет» is hard to parse («здесь まさに не заменяет 正しく» is
enough); なぜなら:18 could keep two Russian sentences so that なぜなら stays visibly sentence-initial; アイロン:19's pattern
gloss matches its dictionary form, so a full past sentence would only be polish; キャプテン:16 «Полезная обстановка» is a
stiff calque; もしも's «а если» adds a contrastive «а» that the examples do not. Limits: やや «без に» was not contradicted by
the sources found but is not certified; the verb-class terms were not re-audited deck-wide; the pre-existing
`words/最も.md` calls 尤も «часто записываемое», while this card and JMdict 1535810 call it rare, which is outside this diff;
JMdict was read through Jisho rather than JMdictDB; no native-speaker or frequency claim.

## Exclusion classification

All 55 EN exclusion entries (18 lists) are retained. At the candidate, 16 direct, one-sided entries were added on 11 new
cards (two of them new lists, クラシック and ウイスキー):

| Entries | Author | Consistency reviewer |
|---|---|---|
| クラシック→音楽, オーバー→越す, エネルギー→活気, だけど→でも, もしも→もし, まるで→ちっとも, まさに→もうすぐ, そっくり→似る | required | required |
| ウイスキー→酒, ウイスキー→お酒, やや→少々, そっくり→全体 | conservative | required (ウイスキー on the ビール and ワイン precedent) |
| オーバー→越える, エネルギー→余裕, まさに→すなわち, まあ→あ | conservative | conservative |

The reviewer judged all 16 justified and none unjustified; the author's and reviewer's classifications differ only in
strength. The correctness reviewer checked that the original exclusions are retained without auditing quiz safety, and
the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fixes and the final verdicts are in
`223-words-batch-62-recheck-001.md`.
