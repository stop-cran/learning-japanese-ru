# Batch 224 — independent review 001

## Snapshot and scope

- Reviewed commit: `49a8838b1abf3b83582d77fc211ea3915cbf700e` (tree `53bc3a1a7f1ada5c3e8156209e43a4f516946c34`), branch
  `full-ru-224-words-63`, parent `a5a6d09`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 223 candidate `13805217f9159dadc5849e7e0060bfbc1d2ffc4a`.
    Before copying, the coordinator checked two things: that the 13 navigation files edited there were unchanged between
    `1380521` and the candidate's parent `a5a6d09`, and that none of the 30 new cards existed there. The Batch 223 fixes
    touched only アイロン, アイスクリーム, もっとも, まるで, だって, キャンプ, エネルギー, アウト, ところが, まさに and キャプテン;
    of these, only ところが is in this batch's path set, and it was not copied from the scratch worktree.
  - The coordinator byte-compared the 43 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 45 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - Two held wraps were carried into this batch. Batch 223's きちんと and ところが had left their EN links to ちゃんと and
    ところで as plain text because both are Batch 224 words. The coordinator wrapped those mentions at EN's positions in
    the primary checkout, on top of the published cards; they are the only changes to those two cards.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 15 files with 16 restored navigation links (including the two held links);
    - `manifest.json` (`contentVersion` `24168b4b2d433970`, 4,839 entries);
    - the intake.
- Published baseline recorded in the intake: `2a8548351a71d2cb61d8ba935afcdde6ff01f809` (Batch 223 merge). Parent
  `a5a6d09` adds only the Batch 223 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK;
  - content budget: OK;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 15 files and 16 links, with no problem;
  - title screen: no unguarded exact title-segment overlap;
  - link parity: no EN link lost where the RU target exists, and nine RU-only links (どんなに→どう, できれば→可能,
    できれば→必ず, それと→それとも, それでも→まだ, そのまま→まま, すみません→済む, しゃべる→黙る and しまった→しまう). Each
    sits on a comparison, a component or a source-verb sentence; EN mentions these targets unlinked or not at all.
- Common sample: all three reviewers read all 30 new word cards in full, each against its full EN original.
- Correctness review scope:
  - Also read in full the existing RU きちんと, ところが, まま, 済む and しまう and all changed baseline comparison lines.
  - Inspected the JMdict-backed senses of all 30 headwords through Jisho and verified all 30 cited entry ids, correcting
    the API's homograph selection for 所為/せい; inspected full-page spelling notes for the rare forms of さて, しかも,
    しまった, せい, そこで, それぞれ, ただ, たまたま and どこか, and the ateji notes of 素敵 and 兎に角.
  - Confirmed ずうっと's search-only status in the frozen EN dictionary-family capture (batch-42, entry 1006380), using
    only dictionary-family data from that record. Checked せい's tentative しょい derivation in the 精選版 日本国語大辞典
    entry on Kotobank and ぴったり's sudden-stop sense in Digital Daijisen ぴたり sense 3.
  - Russian sources: Gramota and Kuznetsov entries for вволю, исправный, прелестный, уйма, неотразимый, совсем, ничего,
    как, выйти (sense 7), вот; Russian Wiktionary причём, всего-навсего, незадача and в связи с; Reverso and Russian
    Wikipedia for the terms годан, итидан and атэдзи. Guessed entry URLs that failed or lacked a definition were not
    counted as evidence.
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 cards in full and all 15 navigation diffs (`diff -U0`), and checked the intake for its path list and the
    absence of learner prose only.
  - Checked the SHA-256 of all 3,373 `words/` entries in `manifest.json` against the files (no mismatch).
  - Ran `tools/validate.py` (0 errors) and `word_title_screen.py` itself, judging its mostly stem-level hits by hand;
    took dictionary senses from the Jisho (JMdict-derived) API.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN, and きちんと and ところが in full; spot-checked the synonym section of 実は and
    inspected the other link-wrap diffs as diffs.
  - Used Kuznetsov on Gramota and Ozhegov for Russian usage and Jisho for JMdict senses. It did not run
    `word_title_screen.py` or `link_parity.py` (quiz-label collisions are outside its facets) or report running the
    content validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; each report says its model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time; the coordinator verified HEAD `49a8838` and a clean tree before each
  launch. Each report records the snapshot `49a8838` with an empty `git status --porcelain`. No fix was applied until
  all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `224-words-batch-63-review-correctness-001.md`
  - `224-words-batch-63-review-consistency-001.md`
  - `224-words-batch-63-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`, except
    that the consistency reviewer checked only the intake's path list and the absence of learner prose;
  - the scratch worktrees;
  - one another's reports.

  The correctness report confirms that it read no author or reviewer report, batch or tracking record or excluded scratch
  worktree. The consistency report confirms that it read no author report, title-screen output, batch or draft record or
  tracking file beyond the permitted intake check. The comprehensibility report confirms that it read no author report,
  title-screen output or `docs/translation-batches/` record, and did not read the intake.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **CLEAN**; scoped coverage **CLEAN** for all 30 new cards. No finding was established.

What the reviewer confirmed:
- All cited sense ranges match the meanings taught. The hedged kango origin of せい is supported by the dictionary's
  tentative 「字音『しょい』の変化した語か」; ぴったり's sudden-stop translation is supported (Digital Daijisen ぴたり
  sense 3; JMdict 1010900), and ちゃんと's mimetic label is a JMdict class, not a claim that it imitates a sound.
- The flagged Russian glosses («вдоволь», «исправно», «прелестный», «уйма», «неотразимый», «совсем ничего», «как надо»,
  «так вышло», «вот незадача», «всего-навсего», «в связи с этим») are supported by the inspected entries. Repeated
  near-synonyms in a short title are not additional unsupported Japanese senses.
- The nine RU-only links were checked against the relevant lexemes; the added どうやって作りますか is natural and carries
  its reading. そのうち's approximate near future is dictionary-supported and qualified; «неотразимый» has the required
  attraction sense. Russian masculine past forms are contextual renderings, not claims about Japanese gender.
- Front matter, readings, levels, types, tags, kanji and the original exclusions are retained; no EN teaching point or
  link to an available RU target was dropped. Both held restorations, きちんと→ちゃんと and ところが→ところで, stay accurate
  beside their new targets; the latter is a contrast, not a demonstrated quiz-label overlap.

Optional:
- `とにかく.md:19` «Не говоря уже о цене…» could teach the set-aside more transparently as «Если оставить цену в стороне,
  качество хорошее». The reviewer expressly did not call the existing phrase a mistranslation (Ushakov via kartaslov and
  Russian Wiktionary «не говоря уже о» include «оставляя в стороне»).
- `ちゃんと.md:33` could say «перевод … может преувеличивать: говорящий не обязательно утверждает…», closer to EN's
  "can therefore overstate … need not mean".

Limits: online dictionaries are current observations, not pinned archives; not every related comparison card was read in
full; quiz-pool safety and comprehensibility are outside the facet; no native-speaker, device or app acceptance.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; quiz safety **CLEAN**, with one recommended guard. Comprehensibility and translation
fidelity were not assigned.

- Recommendation 1 (minor, non-blocking; medium confidence), `どんなに.md`: どんなに «как сильно; как бы ни» and どう «как;
  каким образом» share the title word «как», and the card itself contrasts degree with manner and links どう. The author
  declined the pair and EN has no guard. Remedy: `quiz_exclusions: [いくら, どう]`.

What the reviewer confirmed:
- 45 payload paths equal the 45 `words/` files of the candidate diff (47 files with `manifest.json` and the intake); the
  intake holds hashes and metadata only, and `held` is empty.
- Each of the 15 navigation files changes exactly one line, wrapping an existing word as `[X](X.md)`. The positions of
  all 16 occurrences match EN: 単なる links only the first ただ, 実は links the first ところで and keeps its reading, and
  単に links ただ and たった. No EN link is lost in any of the 45 files.
- Every EN exclusion is present in RU. All RU-added guards have a dictionary or title basis; none is unjustified.
- Each of the nine RU-only links targets an existing RU card at a sentence that explains it. ありがとう, ごめんなさい, 有料
  and ともかく have no RU card and correctly stay plain; たまらない→辛い is fine because that card teaches つらい.
- Declined pairs judged acceptable because the titles separate them and the cards teach the contrast: ところで–ところが,
  ずっと–もっと, たった–ばかり, どんなに–そんなに, できれば–できるだけ, ちゃんと–丁寧 and まじめ, たまたま–ばったり,
  たっぷり–一杯, ただ–普通, それと–しかも, それでも–けれども, それぞれ–みんな, そのまま–すぐに, そのうち–今度, せい–おかげ
  and 理由, すてき–きれい, しゃべる–言う, しまった–残念 and ぴったり–似合う.

Optional: なにも–全然 and なにも–全く (JMdict なにも "(not) at all"; shared «совсем»); ずっと–ずいぶん, しきりに–よく and
しまった–失敗, all weak; the RU-added 可能 gloss on できれば and the «как» degree-versus-manner comparison on どんなに were
judged justified adaptations of the teaching rule. Limits: JMdict senses through the Jisho API rather than exact entry
ids; the app's quiz selection was not inspected; pre-existing EN/RU link differences outside this batch (ばったり,
ぶかぶか, 申し訳, 豊富) were noted and not judged.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (five findings); scoped coverage **CLEAN**. The EN contrasts named in the
assignment are present; the findings are Russian renderings, not dropped EN teaching points.

- C1 (moderate; high confidence), `とにかく.md:19`: «Не говоря уже о цене, качество хорошее» is commonly read additively
  ("not to mention"), against the card's own note at :21 that Nはとにかく names what is set aside and EN "Leaving the price
  aside". Remedy: «Цена — вопрос отдельный, а качество хорошее.» or «О цене умолчим: качество хорошее.» Evidence: JMdict
  1443990 sense 2.
- C2 (moderate; high confidence on :18, medium-high on :19), `たっぷり.md:18–19`: «побольше воды» means "a little more
  water", not «вдоволь; обильно» or EN "plenty of water", and «уйма времени» is a colloquial overstatement. Remedy: «Налейте,
  пожалуйста, в кастрюлю воды вдоволь.» and «До отправления времени у нас вдоволь.» Evidence: JMdict 1007240 sense 1;
  Kuznetsov побольше and уйма.
- C3 (moderate; high confidence), `それぞれ.md:4,12,16,19`: «соответственно» was said to mean "likewise", "properly" or
  "according to" but not "respectively", so «живут соответственно в Токио и Осаке» could read as "accordingly". Remedy:
  title «каждый (из нескольких); каждому своё»; example «Старший брат живёт в Токио, а младшая сестра — в Осаке.»
  Evidence: Kuznetsov соответственно.
- C4 (minor; high confidence that the gloss is narrower), `たまらない.md:4,11`: «неотразимый» was said not to cover «не могу
  сдержаться» or unbearable heat, so a learner could store たまらない as "charming". Remedy: title «невыносимый; невозможно
  сдержать».
- C5 (minor; high confidence that it is author-facing), `せい.md:27`: «Категория канго следует этому разбору…» was said to
  be an author-facing classification note with «канго» and しょい unexplained. Remedy: delete it, or say in learner terms
  that the proposed link is uncertain and not needed for use.

Optional: ちゃんと's «исправно» could take a parenthetical; たった:19 «можно дойти» adds walking that EN "reach" does not
specify, and «добраться» would be closer. The reviewer found the following already qualified or consistent: そのまま
«сразу», たまたま «Так вышло», ところで's «даже если», そこで «в связи с этим», しきりに «настойчиво», the «атэдзи» notes on
すてき and とにかく, the verb classes on しゃべる and できれば, and the held-link wording on きちんと, ところが and 実は.
Limits: no native-speaker check; quiz-label collisions outside the facets; Wiktionary's unfinished «не говоря уже» page was
not used to clear C1.

## Exclusion classification

All 53 EN exclusion entries (18 lists) are retained. Two of them lie inside the batch: しかも–それでも and たった–ただ. At the
candidate, 36 direct, one-sided entries were added on 21 new cards (nine of them new lists: すみません, せい, そのまま, できれば,
とにかく, とんでもない, どうしても, どこか and なにも):

| Entries | Author | Consistency reviewer |
|---|---|---|
| どうしても→なかなか and 絶対, とんでもない→いえ, とにかく→何とか, そのまま→まま, すみません→申し訳 and どうも, しゃべる→ぺらぺら (8) | required | required |
| しかも→更に, しゃべる→べらべら and おしゃべり, すてき→見事 and かわいい, すみません→謝る, ずっと→年中, せい→悪い, ただ→だけ and ばかり, たった→だけ, できれば→なるべく, どこか→どこ and 辺り (14) | conservative (たった→だけ unmarked) | required |
| さて→ところで, しきりに→しばしば, せい→原因, それでも→しかし and でも, それと→それから, ただ→サービス, たっぷり→十分, たまたま→たまに, とんでもない→ひどい and 凄い, どうしても→ぜひ and 必ず, なにも→別に (14) | conservative | conservative |

The reviewer judged all 36 justified and none unjustified; the author's and reviewer's classifications differ only in
strength. In the initial report's grouped list, the "(conservative)" mark after ただ's three targets applied to サービス
only; the reviewer confirmed this reading at the recheck. The correctness reviewer checked that the original exclusions
are retained without auditing quiz safety, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusion added by the fix and the final verdicts are in
`224-words-batch-63-recheck-001.md`.
