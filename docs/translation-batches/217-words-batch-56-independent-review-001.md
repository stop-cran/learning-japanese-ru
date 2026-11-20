# Batch 217 — independent review 001

## Snapshot and scope

- Reviewed commit: `4af7ea72f6c372d31a810a783ca4b8655dd4ba44` (tree `7d76a5cff85d39b882c357ad2718d0fd71662b5c`), branch
  `full-ru-217-words-56`, parent `28c7578`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 216 candidate `034ab7ea9034db0f24f7d8dfdad1f16af819e788`.
    Before copying, the coordinator checked two things: that the 24 navigation files were unchanged between `034ab7e` and
    the candidate's parent `28c7578`, and that none of the 30 new cards existed there. The Batch 216 fix touched only
    切れる, 劇, 分, 助手, 到着, 前者 and 刈る, none of which is in this batch's path set.
  - The coordinator byte-compared all 54 scratch content files with the primary checkout twice: after copying and again
    at commit time. Its byte scan found no BOM or CR, and every file ends with a newline, as `.gitattributes` requires.
  - No held wraps were carried into this batch.
  - The coordinator made one content change before the candidate: a conservative 優勝→勝ち exclusion, because
    優勝's title «победа в чемпионате; первое место (в соревновании)» is a hyponym of 勝ち «победа; выигрыш». The author had left the pair
    unguarded while Batch 216's 勝ち title was still under review.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 24 files with 29 restored navigation links;
    - `manifest.json` (`contentVersion` `11784b5b84fabdd0`, 4,629 entries);
    - the intake.
- Published baseline recorded in the intake: `0bbd15e72862bba9c9bc9bcffbd06e20cd989b83` (Batch 216 merge). Parent
  `28c7578` adds only the Batch 216 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK;
  - content budget: OK, 4,646 entries / 13.14 MB;
  - navigation-only check: 24 files and 29 links, with no problem;
  - title screen: no unguarded exact title-segment overlap.
- Common sample: all three reviewers read all 30 new word cards in full.
  - Correctness and comprehensibility read each card against its full EN original.
  - Consistency compared each card's front matter, link targets and exclusions with EN.
- Correctness review scope:
  - Read the binding RU instructions and reference files.
  - Read the existing ナイフ, 出身, 流れ, 一緒, このあいだ and 勝ち cards in full, and the changed hunks of the five kanji
    cards and nineteen word cards that received navigation links.
  - Read the JMdict-backed Jisho API records for all 30 headwords and for 皆, この間, 勝ち and 運転免許.
  - Compared all 60 primary Japanese examples and their kana lines with EN by hand; an exact-substring check also
    covered 59 sentence/kana pairs. 冗談's quoted dialogue was checked by hand, because its closing quotation mark falls
    outside that check's pattern.
  - Russian sources: Kuznetsov entries on Gramota (выходец, вытечь, встреча, знакомство, обработка, покрыться, лёд, вновь,
    повторный, иена, круг, воплощение, конкретный, общий, сообща, общенациональный, весь, целый, партия, лицензия,
    чемпионат, незначительный, остановка, заём, кандидат, вариант and способность); the Большой универсальный словарь
    entry «на днях»; and Russian Wiktionary катана, уладить, преодолеть, превзойти and лишь. Gramota HTTP 429 and
    Wiktionary HTTP 403 failures were replaced by successful fetches, not treated as evidence.
  - Ran `tools/validate.py` (0 errors). It ran no generator.
- Consistency review scope:
  - Read all 30 cards and all 24 navigation diffs in full.
  - Checked the manifest hashes, the intake path list (54 paths, equal to the content diff) and `tools/validate.py`
    (0 errors).
  - Confirmed that the absent link targets, including `kanji/補.md`, are absent.
  - Classified the RU-added exclusions from the RU titles and from its recollection of JMdict senses. It did not fetch
    dictionary pages.
  - It also reported that the 118 `strokes/*.json` manifest entries did not match the working tree, outside the batch.
    The coordinator withdrew this by evidence: `tools/build_manifest.py:19` hashes the bytes after CRLF→LF normalisation,
    and those stroke blobs are CRLF byte copies marked `-text`, so the committed hashes are current.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN, and the titles of 紹介, 会, 会合 and 出会う.
  - Read JMdict entries on Jisho (JMdictDB required a password) and Digital Daijisen 出会い on Weblio.
  - Ran `link_parity.py`, which reported no lost links. `word_title_screen.py` produced no output before the reviewer
    stopped it, so it used no title-screen leads.
  - Did not review the kanji edits or quiz-pair machinery, which were not its facet.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier.
- Reviews ran serially, one reviewer at a time. Each reviewer reports that HEAD was `4af7ea7` and `git status
  --porcelain` was empty when it started. No fix was applied until all three reports were complete, and the coordinator
  confirmed afterwards that HEAD was still `4af7ea7` and that `git status --porcelain --ignored` was empty.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. The consistency reviewer wrote its report under a different file name in the same session
  folder; the coordinator copied it verbatim to the assigned name. No repository file was written.
- Full blind reports:
  - `217-words-batch-56-review-correctness-001.md`
  - `217-words-batch-56-review-consistency-001.md`
  - `217-words-batch-56-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch worktrees;
  - one another's reports.

  The correctness report confirms that it read no author or reviewer report, tracking ledger, batch record or scratch
  worktree. The consistency and comprehensibility reports do not restate the rules.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** (F1, 克服); the other 29 cards are clean in this facet. Scoped coverage **CLEAN**
for all 30 cards.

- F1 (minor; high confidence), `克服.md:15`: «克服 — преодоление трудности, способность взять её под контроль» defines
  克服 partly as an ability. EN says "overcoming or bringing a difficulty under control", and JMdict gives the action, not
  a capacity; Kuznetsov «способность» sense 1 is the possibility or ability to act. A learner could call a mere
  capability 克服. The rest of the card describes overcoming correctly, so the defect is localized. Remedy: «克服 —
  преодоление трудности, взятие её под контроль.», keeping the following を and たい guidance.

What the reviewer confirmed:
- All primary Japanese examples and kana lines match EN, and the reading-join passages keep EN's katakana. It found no
  consequential tense, polarity, voice, transitivity or end-state mismatch. Masculine first-person past forms such as
  «я переехал» are contextual renderings, not a claim about the speaker; 彼女 stays female.
- The たい goal in 克服 and the ongoing repayment in 借金 stay distinct from completion. 運転免許 is naturally «водительские
  права», and the card does not call Russian driving papers «водительская лицензия».
- Metadata keeps EN values except the translated titles and the RU-added guards. No live EN link was dropped, and absent
  targets stay plain. Omitted English-dependent commentary removes no Japanese teaching point.

Cited evidence supporting the Russian adaptations:
- 刀: Wiktionary «катана» sense 1 (a traditional Japanese sword); the card qualifies it beside «меч».
- 出: Kuznetsov «выходец» 1–2 and «вытечь»; JMdict 出 sense 4 supports the graduate meaning.
- 処理: «обработка» and Wiktionary «уладить» 1–2 (bringing a matter to a result; settling disagreements).
- 凍る: «покрыться» 2 and «лёд» 1 support frozen over, not necessarily frozen through.
- 再び: «вновь» and «повторный»; the card keeps the caveat against inferring a total count.
- 円: «иена» and «круг» 1.
- 具体: «воплощение» 2 and «конкретный», without making bare 具体 an adjective.
- 共通 and 共に: «общий» 3–4, 8 and 10; «сообща». JMdict 共に's separate "both" sense keeps both-parents-are-doctors
  from being read as joint work.
- 全国: «общенациональный» is offered as a possible attributive rendering, not as a claim that 全国 is an adjective.
- 全, 全て, 全体 and 全員: «весь» 1 and 3, «целый» 2 and 4 and «в целом»; the cards keep context-limited scope and
  partial negation.
- 党: «партия» 1, 4 and 6; the card does not equate 党 with a batch of goods or a game.
- 免許: «лицензия» 1–3.
- 先日: the Большой универсальный словарь «на днях» separates near future from recent past; 先日 is restricted to the
  past.
- 優勝: «чемпионат» and JMdict 優勝 sense 1 (overall victory), not winning a single round.
- 優れる: Wiktionary «превзойти» 1.
- 僅か: «незначительный» 1 and Wiktionary «лишь» 1.
- 停留所: «остановка» 1–2; the card teaches the place.
- 借金 and 候補: «заём»; «кандидат» 1 and «вариант» 1–2, without implying an election or a completed selection.

Optional: none.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **NEEDS FIX** (minor); cross-file integration **CLEAN**.

- Q1 (minor; medium confidence), `共に.md:9`: 共に's «и тот и другой» overlaps 両方 «оба»; JMdict 共に has the sense
  "both; alike". Remedy: `quiz_exclusions: [一緒, 両方]`.
- Q2 (minor, conservative; low-medium confidence), `出会い.md:9`: the title shares «встреча» with 会合 and «знакомство»
  with 紹介, and the card teaches «встречи и знакомства». EN leaves the pair unguarded too. Remedy:
  `quiz_exclusions: [出会う, 会合, 紹介]`.
- Q3 (minor, conservative; low confidence), `処理.md`: «улаживание дел» is close to 解決 «урегулирование». Remedy:
  `quiz_exclusions: [解決]`.
- The three RU-added exclusions: 全て→皆 required (JMdict 皆 "all; everyone; everything"; shared «всё»); 先日→このあいだ
  required (identical segment «на днях»); 優勝→勝ち required or conservative (JMdict 勝ち "win; victory").
- Every EN exclusion is retained.
- The RU-only links 円→丸, 先日→このあいだ and 借金→借りる are substantive mentions or comparisons, acceptable under the RU
  link rule. 候補's EN link to `kanji/補.md` has no RU target, so plain text is correct.
- Navigation: 29 links restored in 24 files, brackets and hrefs only, in EN's path forms: 処 three; 停, 再 and 凍 two each;
  党 one; one in each word file. いくら wraps «иен» at EN's "yen" link position. 別れ and 劣る changed only by the link.
- Manifest: no stale hash among kanji, words and articles; all 30 new cards are present. Intake: 54 paths, equal to the
  content diff.

Optional: guards for 共通–同じ, 全–皆, 冗談–悪戯 and 借金–貸し would be conservative only.

Limits it recorded: its dictionary claims come from recollection of JMdict, not live fetches; it did not investigate the
strokes hash observation beyond the CRLF indication (withdrawn above).

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (出会い only; the other 29 cards are clean in this facet); scoped coverage
**CLEAN**.

- C1 (minor; high confidence), `出会い.md:4,12,16,19,21,31`: the title and several glosses join «встреча» and «знакомство»
  with «и», so a learner can treat every 出会い as both a meeting and an acquaintance. That does not fit coming across a
  thing, and «знакомство» overlaps 紹介's title «представление; знакомство». The body already frames 出会い with a person or
  thing (+ との出会い; books and ideas), so scoped coverage stays clean.
  - Remedy: title and H1 «встреча (с человеком или чем-либо)»; line 16 «или встреча с чем-либо»; line 19 «— В поездках
    случаются новые встречи.»; line 21 «кого-то встретить»; line 31 «такой встречи». Line 35 («не ограничено романтическими
    знакомствами») correctly limits one reading and stays.
  - Evidence: JMdict 1338400 on Jisho, "meeting; rendezvous; encounter" and "meeting for the first time; coming across",
    not acquaintance; Digital Daijisen on Weblio, sense 1 「思いがけなくあうこと／めぐりあい」 with 「一冊の本との―」, and
    知り合うこと as a separate sense 6.

Optional: 出's «вытекание (воды)» is narrower than EN "outflow" and the card's own «выход наружу», but the taught
example is water and the body does not restrict the sense, so no change is needed.

Checked and not findings: 刀 «катана» beside «меч» and against ナイフ/包丁; 出 «выходец» against the particle で; 処理,
解決 and 対処; 凍る, 冷える and 凍らせる; 冗談を言う against 嘘; 冒険, 旅行 and 危険; 再び, また and もう一度; 円 against まる
and number + 円; 具体 against 具体的 and the ban on 具体な; 共通 against 同じ; 共に against 一緒に, with «оба» against joint
action; 公平 against 平等; 全国, 全体 and 国; 全員で against 全員が; 全て, its contextual scope and partial negation; 全 against
全部の; 全体 against 全部 and 一体全体; 党 against パーティー; 免許 against 許可/資格; 克服 against 解決; 先日 and future «на
днях»; 優勝 against 勝つ; 優れる against 上手/得意; 僅か + number; 傷 against 怪我; 健康 against 元気/丈夫; 停留所 against
駅/バス停; 借金 against 借りる/貸す; 候補 against 選択/推薦. No English leftover, Latin-script learner word or Cyrillic
reading transliteration was found, and the English-only contrasts were replaced by the Japanese rule or a Russian
false-friend note.

## Exclusion classification

All 27 EN exclusion entries (14 lists) are retained. At the candidate, three direct, one-sided entries were added on
three new cards:

| Entry | Author or coordinator | Consistency reviewer |
|---|---|---|
| 全て→皆 | required (author) | required (shared «всё») |
| 先日→このあいだ | required (author) | required (identical segment «на днях») |
| 優勝→勝ち | conservative (coordinator) | required or conservative |

The author had considered and declined 共に–両方 and 出会い against 会, 会合 and 紹介, judging the titles distinct; the
consistency reviewer raised them as Q1 and Q2. The fixes added eight more entries: Q1, Q3 and Q2's 会合, the two adopted
optional items and three coordinator extensions (会, 迎え and 治める); Q2's 紹介 was not added. The correctness reviewer checked the guard comparison words in JMdict without auditing quiz
safety, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`217-words-batch-56-recheck-001.md`.
