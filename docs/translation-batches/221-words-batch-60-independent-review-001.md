# Batch 221 — independent review 001

## Snapshot and scope

- Reviewed commit: `f888c34e8eb7c8d29c76c0433dbb3b0035ee8e3b` (tree `0fb4d226b4ec03bd217f2acb300a050473e1e0b1`), branch
  `full-ru-221-words-60`, parent `98f8927`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 220 candidate `19bcfe00f202ae1368ffc4422b38d9b1da172c2e`.
    Before copying, the coordinator checked two things: that the 7 navigation files edited there were unchanged between
    `19bcfe0` and the candidate's parent `98f8927`, and that none of the 30 new cards existed there. The Batch 220 fixes
    touched only 一人一人, ワイン, ラケット, 一般, 不正, 一層, 上京, ロケット and メモ; of these only ワイン is in this batch's
    path set, and it was not copied from the scratch worktree (see the held link below).
  - The coordinator byte-compared the 37 scratch content files with the primary checkout after copying and again at
    commit time. Its byte scan of all 38 content paths found no BOM or CR, and every file ends with a newline, as
    `.gitattributes` requires.
  - One held wrap was carried into this batch: Batch 220's ワイン had left its EN link to ビール as plain text because ビール
    is a Batch 221 word. The coordinator wrapped that mention at EN's position (ワイン line 36) in the primary checkout, on
    top of the published, fixed ワイン card; it is the only change to that card.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 8 files with 8 restored navigation links (including the held ワイン→ビール link);
    - `manifest.json` (`contentVersion` `a55f101dcc2ed0b6`, 4,749 entries);
    - the intake.
- Published baseline recorded in the intake: `f6ff0ae9d83b2ab689c785626de74a5a4f1559ac` (Batch 220 merge). Parent
  `98f8927` adds only the Batch 220 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK;
  - content budget: OK, 4,766 entries;
  - `git diff --check` and the byte scan: clean;
  - navigation-only check: 8 files and 8 links, with no problem;
  - title screen: no unguarded exact title-segment overlap;
  - link parity: five RU-only links (ホーム→帰宅, ドラマ→テレビ, ビール→ビル, バイオリン→弾く and トン→キログラム). EN mentions
    each target unlinked in a substantive comparison.
- Common sample: all three reviewers read all 30 new word cards in full.
  - Correctness and comprehensibility read each card against its full EN original.
  - Consistency read the first 10 EN originals in full and compared the other 20 with EN by script (front matter, links,
    line counts).
- Correctness review scope:
  - Read in full the existing RU 帰宅, テレビ, ビル, 弾く and キログラム (the five RU-only link targets) and ワイン (the
    held-link card); inspected the eight existing-word and article integration diffs; read the binding instructions.
  - Read the JMdict-backed Jisho API records for all 30 headwords, including the separate ミス, ホーム, ボール and バン/ＶＡＮ
    identities (initial HTTP 429 responses for パスポート and ド were resolved by later successful reads), and the full
    Jisho page for 屯 (the three ton spellings).
  - Russian sources: Kuznetsov entries on Gramota (краска, играть, смесь, мисс, мама, мастер, миска, труба, трубка, связь,
    сумка, красивый, поход, платье, пучок, фургон, магистр, перрон, видеомагнитофон, паспорт, совершенный and килограмм)
    and Russian Wiktionary (по-домашнему, сдерживание, сдерживать); Digital Daijisen and Seisen Nihon Kokugo Daijiten on
    Kotobank for ハンサム (a Kotobank URL that redirected to an unrelated entry was rejected); English Wiktionary
    value-added network; the Russian Wikipedia baseball-terminology glossary.
  - Ran `tools/validate.py` (0 errors); ran no generator.
- Consistency review scope:
  - Read all 30 cards and all 8 navigation diffs in full, and compared link counts and path forms with EN.
  - Checked that every Markdown manifest hash matches the file on disk and that no file is missing (4,744 file entries:
    it counted the `files` map, without the three image and two scene entries). It reported that 118 `strokes/*.json`
    hashes differ from the raw file hash, unchanged from the parent.
  - Checked the intake only for its path list, candidate SHA-256 values and the absence of learner content, as its
    prompt permitted.
  - Ran `tools/validate.py` (0 errors) and its own read-only title-overlap and link-parity screens.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN, and read RU テレビ, パン, ワイン and ビル in full for convention and the restored
    ワイン link; read the link-only diffs of the other seven navigation files; checked the titles of the named comparison
    cards, and read お母さん and 牛乳 through their contrast sections.
  - Read JMdict entries through the Jisho API's English definitions. It did not report running the content validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier; each report says its model is not verifiable from inside the session.
- Reviews ran serially, one reviewer at a time. Each report records the snapshot `f888c34` with an empty
  `git status --porcelain`. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `221-words-batch-60-review-correctness-001.md`
  - `221-words-batch-60-review-consistency-001.md`
  - `221-words-batch-60-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`, except
    that the consistency reviewer checked only the intake's path list and hashes;
  - the scratch worktrees;
  - one another's reports.

  The correctness report confirms that it read no author prompt, other report, batch record, tracking file or scratch
  worktree. The consistency and comprehensibility reports do not restate the rules.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **UNVERIFIED** only for three exact Russian lexical labels (L1–L3); correctness **CLEAN** for the
other 27 cards and the reviewed integration changes. Scoped coverage **CLEAN** for all 30 cards and the integration
changes. No content defect was established; L1–L3 are evidence limitations, not assertions that the translations are
wrong.

- L1 (high confidence in the limit), `ドライブ.md:4,12`: no actual entry for the exact compound «автопрогулка» was
  obtained (Gramota returned no entry; Russian Wiktionary returned 404). Kuznetsov's авто- and прогулка entries (the
  latter explicitly including travel by car) support the compositional meaning but are not the exact entry. To close:
  an inspectable exact entry, or the dictionary-attested «прогулка на машине».
- L2 (high confidence in the limit), `バン.md:4,12,24,26`: JMdict verifies ＶＡＮ/バン as value-added network and English
  Wiktionary defines its added communications functions, but no inspectable Russian dictionary or terminological entry
  for the exact «сеть с добавленной стоимостью» was obtained. The Japanese identity and EN-sense coverage are verified.
- L3 (high confidence in the limit), `ボール.md:21`: JMdict verifies the baseball sense, and the Russian «бол» is attested
  in the Russian Wikipedia baseball-terminology glossary, but not in the requested dictionary class (Gramota's and
  Russian Wiktionary's actual results are unrelated).

What the reviewer confirmed:
- All sections, taught senses, examples, explanations and citations were compared in all 30 pairs. All 60 complete
  Japanese example sentences and their kana reading lines match EN, including hiragana ベンチ/ドライブ readings and
  full-width ＶＡＮ; RU's full-width parentheses are formatting.
- Stable front matter is preserved and the EN exclusions retained. No EN internal link was dropped where the RU target
  exists; 絵の具, ソファー and 楽器 stay plain text. The five added RU links preserve the existing Japanese distinctions and
  add no Japanese sentence; ワイン→ビール and the other restored links read coherently.
- The formula, proprietress, mastery-verb, microphone and pro abbreviations, Dutch pek/bier, the dated picnic sense, the
  four video senses, pipe connections, VAN readings, violin spelling, the intensifying prefix and the metric-ton
  qualification are verified. The Russian labels in the Kuznetsov entries listed above are supported in the cited
  senses; «совершенный» (first entry, sense 2) supports an absolute intensifier, not "flawless". The "usually male"
  qualifier on ハンサム comes from Daijisen and Seisen Nihon Kokugo Daijiten, not from English handsome.
- First-person past-tense gender choices (for example feminine была in ドレス) are contextual translation choices, not
  claims about the Japanese.

Optional: replace «автопрогулка» in ドライブ's title and H1 with «прогулка на машине», an evidence-backed alternative that
closes L1 without changing the Japanese lesson.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; scoped coverage (cross-file integration) **CLEAN**; quiz safety **NEEDS FIX** (F1,
minor).

- F1 (minor; medium confidence), `パイプ.md` front matter and title: the RU title adds «связи, канал общения между
  людьми» to EN's "pipe; tube; communication channel", but only 管 and 付き合い are guarded. Unguarded titles with the same
  meaning: 関係 «связь; отношения», 連絡 «связь; контакт» and 仲 «взаимоотношения (между людьми)». 付き合い already
  declares [関係, 仲], showing a confusable cluster. Impact: a learner could defensibly choose 関係 or 連絡 for the パイプ
  title. Remedy: `quiz_exclusions: [管, 付き合い, 関係, 連絡]` (optionally 仲), or retitle closer to EN.

What the reviewer confirmed:
- Front matter is identical to EN apart from title and quiz_exclusions for all 30 cards, and the heading pattern matches
  existing RU cards. All EN exclusions are retained.
- The navigation diffs are single-line link wrappers at the EN link positions with EN's path forms.
- No EN link was lost. The five RU-only links have existing targets that EN mentions unlinked in a substantive
  comparison. ソファー, 楽器 and 絵の具 have no RU file and stay plain text.
- `manifest.json` has 4,744 file entries; all Markdown hashes match disk and no file is missing. The intake's 38
  payloads equal the candidate content diff, its candidate SHA-256 values equal disk and manifest, its held list is
  empty and it adds no learner content.
- Every lexically overlapping pair in the dense-cluster list is guarded on at least one side. Other screens (ベンチ/席,
  ドレス/服, ペンキ/色, パスポート/パス, バン/パン, ビデオ/映画, トン/キログラム, ホーム/駅, ミルク/素, マスター/覚える/学ぶ)
  showed no defect.

Optional: consider dropping プロ→職業 (a possible over-guard; no change needed). Limits: the 118 stroke-file hash
differences (pre-existing, probably normalized hashing); pre-existing differences from EN in files touched only by
navigation edits (for example ワイン:36's plain ウイスキー, EN 帯:28's link to 紐 and EN いす:27's link to 席) are out of
scope.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (ママ, ボール, バン, ビデオ, ド and トンネル; the other 24 cards are clean in
this facet); scoped coverage **CLEAN** for all 30 cards and the restored links. No EN teaching point was lost, and the
English-only contrasts (miss someone, brake/break, bun vs bread roll, dress warmly, handsome profit, tonne/ton) were
adapted rather than copied.

- C1 (minor; high confidence), `ド.md:4` (H1 line 12): the gloss «совершенный» is the ordinary word for "perfect", and
  完全 is already titled «полный (без изъянов); совершенный», so a learner can take the prefix as praise or as 完全. The
  card's examples say «полный дилетант» and «полный новичок». Remedy: title and H1 «усилительная приставка (самый,
  полный)». Evidence: JMdict ど/ド prefix ("extreme; ultra; totally; precisely"; dismissive "damn; stupid").
- C2 (minor; high confidence), `ボール.md:21`: «засчитывается как «бол», в противоположность страйку» works only through
  baseball jargon; «бол» is not an ordinary Russian word and «страйк» ordinarily means a strike or a bowling strike.
  Remedy: describe the pitch outside the strike zone. Evidence: JMdict ボール sense 2.
- C3 (minor; medium confidence), `ママ.md:4` (H1 line 12): «по-домашнему» ordinarily means homestyle or casually, not the
  family's word for mum, and it is the title's only distinction from お母さん «мать; мама». Remedy: «мама (фамильярно);
  хозяйка бара». Evidence: JMdict 1129240 senses 1–2.
- C4 (minor; medium confidence), `バン.md:4` (also 12, 24, 26): «сеть с добавленной стоимостью» uses the economic phrase
  «добавленная стоимость» (value added, VAT), so a beginner can memorize a tax meaning; the paragraph's «сеть передачи
  данных с дополнительными услугами» is not in the title or the example. Remedy: title and H1 «пучок (причёска); фургон;
  сеть передачи данных с услугами»; example «— Эта компания пользуется сетью передачи данных с дополнительными
  услугами.»
- C5 (minor; medium confidence), `ビデオ.md:32`: «кассету VHS» is an unexplained Latin abbreviation in learner prose; the
  Japanese claim is right. Remedy: «Видео само по себе не означает именно старую видеокассету.»
- C6 (minor; high confidence), `トンネル.md:18`: «выехали» adds travel by vehicle, while 出る only marks leaving the place
  and EN says "came out". Remedy: «— Когда мы вышли из туннеля, стало видно море.»

Optional: ホーム «перрон» (a recognized equivalent; «платформа (на станции)» would be polish), ブレーキ «сдерживание»
(anchored by «тормоз» and defined in the body), ミルク «детская смесь» (restricted in the first paragraph), ドライブ
«автопрогулка» (bookish but not false; «прогулка на машине» would be plainer) and パイプ's long but clear third gloss.
Latin source-language names in etymology lines match the published パン «pão» and were not treated as defects. Limits:
Jisho API definitions rather than the raw EDRDG XML; no native-speaker or frequency check; comparison cards other than
those named were not read in full; quiz exclusions were not scored on this facet.

## Exclusion classification

All 19 EN exclusion entries (11 lists) are retained. At the candidate, 14 direct, one-sided entries were added on 11 new
cards (six of them new lists):

| Entries | Author | Consistency reviewer |
|---|---|---|
| ハンサム→美しい, ハンサム→きれい, バン→束, ドライブ→旅行, ド→いちばん, ド→完全 | required | required |
| ボール→ちゃわん, マスター→上達, ドラマ→出来事, ハイキング→観光, パイプ→付き合い | conservative | conservative but justified |
| ビール→酒, ビール→お酒 | added by the coordinator (hypernym, as on ワイン) | conservative but justified |
| プロ→職業 | conservative | possible over-guard (harmless) |

The author and reviewer agree on every entry except プロ→職業, which the reviewer called a possible over-guard without
requiring its removal. The correctness reviewer identified the added exclusions without auditing quiz safety, and the
comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`221-words-batch-60-recheck-001.md`.
