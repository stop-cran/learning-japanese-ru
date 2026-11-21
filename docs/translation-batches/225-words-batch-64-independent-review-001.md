# Batch 225 — independent review 001

## Snapshot and scope

- Reviewed commit: `56996a024ba2641a8d5e846d8c63e1981beeccff` (tree `cec94999a3e5496f49132267a073e5e56aa92d24`), branch
  `full-ru-225-words-64`, parent `a195c33`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 224 candidate `49a8838b1abf3b83582d77fc211ea3915cbf700e`.
    Before copying, the coordinator checked two things: that the 7 navigation files edited there were unchanged between
    `49a8838` and the candidate's parent `a195c33`, and that none of the 30 new cards existed in the primary checkout. The
    Batch 224 fix touched only それぞれ, たった, たっぷり, ちゃんと, とにかく and どんなに; none of them is in this batch's
    path set.
  - The coordinator byte-compared the 37 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 40 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - Four held wraps in three files were applied in the primary checkout, on top of the published cards. すみません's EN
    links to ごめんなさい and ありがとう had stayed plain in Batch 224 because both are Batch 225 words. 申し訳 (→ごめんなさい)
    and ぶかぶか (→きつい) already carried Batch 224 navigation edits, so the author was told not to touch them. The
    coordinator wrapped these mentions at EN's positions; they are the only changes to those three files.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 10 files with 11 restored navigation links (including the four held links);
    - `manifest.json` (`contentVersion` `5cebfe295a2192a6`, 4,869 entries);
    - the intake.
- Published baseline recorded in the intake: `b45dcc6152cfb9acb06b8ac84c8fae5209f6fc34` (Batch 224 merge). Parent
  `a195c33` adds only the Batch 224 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK (124 tests);
  - content budget: OK;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 10 files and 11 links, with no problem;
  - title screen: no unguarded exact title-segment overlap (169 stem-only `!!` lines and 31 `OK` lines);
  - link parity: no EN link lost where the RU target exists, and one new RU-only link, ごめんなさい→申し訳, on the
    sentence that contrasts the formal apology 申し訳ありません. The screen also listed すみません→済む, an RU-only link
    published in Batch 224.
- Common sample: the correctness and comprehensibility reviewers each read all 30 new word cards in full against their
  full EN originals. The consistency reviewer compared EN prose line by line for the first eight cards only (ごめんなさい
  to かもしれない) and checked the other 22 against EN by script on front matter and links (see its scope below).
- Correctness review scope:
  - Read all 30 cards in full in RU and frozen EN, all ten navigation diffs, and in full the existing RU すみません, 申し訳,
    ぶかぶか, あまり, すやすや and いらっしゃる.
  - Read the JMdict-backed senses of all 30 headwords through the Jisho API (selecting 御 for お rather than the first hit
    尾) and verified all 30 cited entry ids plus ご (1270190) against the word pages. Inspected the spelling notes for
    こんにちわ, 嗽/漱, 凡ゆる/有らゆる, 彼方此方 and the rare/ateji kanji spellings of おめでとう. For 梺, which Jisho's
    display omits, used the frozen EN dictionary-family capture (`batch-75.json`, entry 1611440).
  - Japanese sources beyond Jisho: Weblio and Digital Daijisen entries for こんにちは, 麓 (ふもと heading), 鳴らす (senses
    1–4), 御免, ごめんなさい and お茶.
  - Russian sources: Gramota and Kuznetsov entries for беспробудный, урчать, гудеть, реветь, выспаться, очень, вероятность,
    можно, крепкий, полоскание, подножие, тесный and аппетит; Russian Wiktionary миленький, умилительный, изматывать, как
    назло and так называемый; MAS/Ushakov excerpts for иметь честь on kartaslov. Some fetches returned HTTP 429 or omitted
    the requested entry; these were not counted as evidence.
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Checked the 30 cards' front matter, titles, exclusions and links against EN, and all ten navigation diffs. EN prose
    was compared line by line only for the first eight cards; the other 22 were compared by script on front matter and
    links. The launch prompt asked for a full read of all 30 cards and file-by-file attestation; the report gives neither
    for the other 22 and did not mark them UNVERIFIED. Its CLEAN verdicts therefore rest, for those cards, on the front
    matter, link, exclusion and integration checks it did perform; prose fidelity of all 30 cards rests on the correctness
    and comprehensibility reviewers' full reads.
  - Checked the SHA-256 of the 40 added or changed `words/` entries in `manifest.json` against the files (no mismatch) and
    the intake for its path list and the absence of learner prose.
  - Took dictionary senses from memory of JMdict glosses, without fetching entries, and did not run `tools/validate.py` in
    the initial review (it ran it at recheck).
- Comprehensibility review scope:
  - Read all 30 cards in full against EN, and the restored-link passages in the ten navigation files.
  - Used JMdict through the Jisho API (not the password-gated JMdictDB page) and a CyberLeninka article on the Russian
    wish speech act. It did not run the validator and did not read batch records.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; the correctness and comprehensibility reports say their model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time; the coordinator verified HEAD `56996a0` and a clean tree before each
  launch. The correctness and comprehensibility reports record the snapshot `56996a0` with an empty
  `git status --porcelain`; the consistency report records commit `56996a0` with a clean tree. No fix was applied until
  all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `225-words-batch-64-review-correctness-001.md`
  - `225-words-batch-64-review-consistency-001.md`
  - `225-words-batch-64-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - any reviewer report;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`.

  The correctness report confirms that it read no author or reviewer report, tracking, batch or draft record or scratch
  worktree. The comprehensibility report says that it did not read batch records. The consistency report does not state
  what it did not read; it checked the intake's path list and hashes, which its assignment included.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **NEEDS FIX** for ぐっすり (one finding), **CLEAN** for the other 29 new cards; scoped coverage
**CLEAN** for all 30. No Japanese factual defect was established in the restored baseline comparisons.

- C1 (minor; high confidence on the added meaning), `ぐっすり.md:18`: «Прошлой ночью я смог крепко выспаться» adds the
  result of having slept enough and rested, which 昨夜はぐっすり眠れました does not state (EN "I was able to sleep soundly
  last night"). It blurs depth of sleep with sufficiency, although the card elsewhere distinguishes them. Remedy: «Прошлой
  ночью мне удалось крепко поспать». Evidence: JMdict 1004060 sense 1 "soundly (sleeping); fast (asleep)"; Digital
  Daijisen ぐっすり sense 1; Kuznetsov выспаться «Проспав достаточно, хорошо отдохнуть».

What the reviewer confirmed:
- All cited JMdict ids match. あんまり's sense 1 is restricted to あまり and its selected senses 2–4 support the teaching;
  おまえ's formerly honorific status, お目に掛かる's modern humble sense 1 and archaic sense 2, and the extended senses of
  うなる and 鳴らす are supported. The 梺 spelling is search-only in the frozen source and is not promoted on the card.
- こんにちは's daytime greeting and retained は, 麓's mountain-foot sense (separately from ろく), 鳴らす's reputation and
  complaint senses, and the ごめんなさい formula discussion are supported. お's お/ご rule is qualified as a tendency.
- The flagged Russian glosses are supported: «беспробудно спать» is an attested deep-sleep use, «миленький» and
  «умилительный» are not only ironic, «урчать» covers a quiet engine, «изматывающий» covers exhausting work, and «как
  назло» is an adverse-coincidence idiom. «Увидимся завтра» on お目に掛かる was judged a natural contextual translation
  beside an explicit humble-role rule, not a categorical register error; «иметь честь» is a dated, formal formula.
- The RU-only contrasts (можно, крепкий, полоскание, подножие, тесный, аппетит, так называемый) are supported and are not
  turned into substitution rules. Masculine first-person Russian forms are contextual choices.
- Japanese runs, metadata and links match EN; the only lower run count is 申し訳ありません, split by the added link.

Optional:
- O1 (outside the facet), `いつまでも.md:33`: «после стольких-то времени» is ungrammatical, not merely stylistic. Remedy:
  «всё ещё, спустя столько времени».
- O2 (non-blocking terminology): explain «канго» (`ごめんなさい.md:26`), «онные чтения» (`こんにちは.md:25`) and «годан»
  (`お目に掛かる.md:21`, `うなる.md:16`, `鳴らす.md:16`) at first use. The classifications were not called wrong.

Limits: not an exhaustive corpus, frequency, native-speaker, media, app or quiz-pool certification; only the six named
comparison cards were read in full beyond the ten diffs; the illustration omission on ぐっすり (EN has image metadata) is
outside the text batch; Jisho's live display is not pinned spelling data.

### Consistency and quiz safety

Verdicts: consistency/integration **CLEAN**; quiz safety **CLEAN**; scoped coverage **CLEAN**. No actionable finding.
Correctness and comprehensibility were not assessed.

What the reviewer confirmed:
- Each of the ten navigation diffs is a one-line bracket addition matching EN's linked occurrence (すみません has two
  links on one line; すやすや wraps the first ぐっすり, as EN does); the intake's "eleven links in ten files" agrees.
- Front matter equals EN apart from titles; every EN exclusion is retained; これら, お, うがい and いわゆる have none in EN.
- All card-to-card links resolve; EN links omitted in RU have absent RU targets and stay plain. The report lists "kanji/麓"
  among them; EN 麓.md has no kanji link (neither RU nor EN has a 麓 kanji card), so the actual omitted EN links are
  ぐっすり's two onomatopoeia articles and うがい's kanji 漱. ぐっすり omits EN's image metadata, consistent with RU word cards.
- The one RU-only link, ごめんなさい→申し訳, is substantive, its target exists, and it matches the card's guard.
- All 40 added or changed `words/` manifest entries match the files; the intake's payload paths equal the 40 changed
  `words/` files and add no learner content.
- いただきます's H1 differs from its title, mirroring EN's own split.
- All RU-added exclusions are justified by a shared label token or a taught sense; none is unjustified. Six targets —
  あいさつ (on こんにちは and いらっしゃい), 寄る, いただく, 希望, 様々 and 祝い — were marked conservative: a basis exists
  but necessity is not established.
- Declined pairs judged acceptable: これら–これ and この, きつい–鋭い, 苦しい and 強い, かわいらしい–すてき, かもしれない–多分
  and おそらく, お互い–両方, あらゆる–一種, いつまでも–いつも and ずっと, and the stem-only screen hits.

Optional: a ごめんなさい–謝る guard (low severity; すみません→謝る is the precedent, and the card contrasts the verb);
ごめんなさい–許す (low confidence; «прощать» in 許す's label); あっ–まあ (incidental «ах»; no action needed). Limits:
EN prose compared line by line for eight cards only; senses from memory of JMdict; `tools/validate.py` not run.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (four findings; the other 26 cards CLEAN on this facet); scoped coverage
**CLEAN**.

- C1 (moderate; high confidence), `お目に掛かる.md:19`: «Увидимся завтра» is a casual, reciprocal goodbye, against the
  card's rule (lines 16 and 29) that the phrase is a humble, speaker-side meeting. Remedy: «Завтра буду иметь честь вас
  видеть.» Evidence: JMdict お目にかかる sense 1 (humble, "to meet (someone of higher status)"); line 18 keeps the direction.
- C2 (minor; high confidence), `おめでとう.md:4,12`: the second title gloss «наилучшие пожелания» is the ordinary
  letter-closing formula, not the spoken congratulation that the card models as «Поздравляю!». Remedy: drop it from the
  title and H1. Evidence: the card's example; 祝う's gloss «Поздравляю!»; a CyberLeninka study placing wish formulas with
  farewells.
- C3 (minor; high confidence), `いわゆる.md:17`: the first example uses «так называемый», which line 32 warns is often
  dismissive; EN renders the sentence neutrally ("what is called"). Remedy: «Это то, что называют энергоэффективным
  домом.»
- C4 (minor; high confidence), `ごめんなさい.md:26`: «Канго-элемент» is unglossed, and «не заимствование из английского» is
  an English-audience remark. Remedy: gloss канго as in this batch's お.md:29 («китайские (канго)») and add advice to learn
  the word as a fixed formula.

Optional: いただきます's H1 does not repeat the title (EN has the same split); あいにく's «как назло» is stronger than «к
сожалению»; あんまり's «не очень-то» is slightly more dismissive than the body's «не очень»; きつい does not name 狭い or
急激, whose titles share «тесный» and «резкий»; 鳴らす's «питчер» may be opaque; and, outside the facet, すみません does not
exclude ごめんなさい although the new card excludes すみません. Restored links read consistently with the new cards.
Limits: JMdict through the Jisho API; validator not run; the plain «См. японскую ономатопею и звуковые модели» is not a
defect, because the two articles and kanji/漱 are absent in RU.

## Exclusion classification

All 35 EN exclusion entries (19 lists) are retained; none lies inside the batch. At the candidate, 24 direct, one-sided
entries were added on 15 new cards (seven of them new lists: こんにちは, こんなに, おめでとう, うなる, いらっしゃい,
いただきます and あいにく). Two of them target batch words: こんなに→あんなに and いただきます→ありがとう.

| Entries | Author | Consistency reviewer |
|---|---|---|
| こんなに→そんなに, それほど and あんなに, きつい→狭い and 急激, おめでとう→お祝い and 祝う, うなる→吠える, いけない→不可, ありがとう→感謝, 鳴らす→掛ける (11) | required | justified, not marked conservative |
| ごめんなさい→申し訳, いただきます→ありがとう, いけない→禁止, あんまり→別に, あっ→しまった, あいにく→残念 (6) | conservative | justified, not marked conservative |
| おめでとう→祝い (1) | required | conservative |
| こんにちは→あいさつ, いらっしゃい→あいさつ and 寄る, いただきます→いただく, おめでとう→希望, あらゆる→様々 (6) | conservative | conservative |

The reviewer judged all 24 justified and none unjustified; the author's and reviewer's classifications differ only in
strength. The reviewer did not use the word "required"; these records treat the entries it did not mark conservative as
required (17), as in earlier batches. The correctness reviewer checked that the original exclusions are retained without
auditing quiz safety, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusion added by the fix and the final verdicts are in
`225-words-batch-64-recheck-001.md`.
