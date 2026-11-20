# Batch 215 — independent review 001

## Snapshot and scope

- Reviewed commit: `2ae93fbb0633b03857d1ae4bade78a29dccba880` (tree `f3c26c5c643abd893a8e005cbc9d79d84a255f74`), branch
  `full-ru-215-words-54`, parent `1a4cb33`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 214 candidate `a371c734a15f44e674e87a3a9ea0c9f147961d90`.
    Before copying, the coordinator checked two things: that the 31 navigation files were unchanged between `a371c73` and
    the candidate's parent `1a4cb33`, and that none of the 30 new cards existed there.
  - The coordinator byte-compared all 61 scratch content files with the primary checkout twice: after copying and again
    at commit time. The author report said its files were CRLF, but the coordinator's byte scan found no CR in them. The
    committed files are LF without BOM, as `.gitattributes` requires.
  - No held wraps were carried into this batch.
  - The coordinator made no content change before the candidate. Before handing over, the author had already retitled its
    own 取り上げる draft to «конфисковать; выносить на обсуждение; брать в руки», because a «рассматривать» gloss collided
    with 論じる.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 31 files with 45 restored navigation links;
    - `manifest.json` (`contentVersion` `47b45533665ed11c`, 4,569 entries);
    - the intake.
- Published baseline recorded in the intake: `30b2be5bc1652e58df14b46b8f330064ab1c6e92` (Batch 214 merge). Parent
  `1a4cb33` adds only the Batch 214 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Common sample: all three reviewers read all 30 new word cards in full.
  - Correctness and comprehensibility read each card against its full EN original.
  - Consistency compared each card's front matter, link targets and exclusions with EN.
- Correctness review scope:
  - Read in full the three binding RU instruction and format files.
  - Read in full the comparison cards 上手, 合う, 怒る, 注意, 野, 美術館, 医者 and 科学.
  - Read the link-only hunks of all 31 navigation files.
  - Read the JMdict-backed Jisho API records for all 30 headwords.
  - Compared all 59 primary Japanese examples verbatim.
  - Gramota dictionary entries (Kuznetsov and Babenko): мастер (and «Мастер своего дела»), подгонять, подогнать,
    отчитывать, выговор, удовлетворительно, проходной, сойти, сходить, вынести, плод, образец, справочный, луг, равнина,
    пустошь, степь, музей, доктор, просто, медицина, официальный, макияж and плотный. It also ran a dictionary search for
    однояйцевой, with Russian Wiktionary.
  - Other sources: Digital Daijisen 化 and 参考 (Kotobank); Nipponica 医師; English Wiktionary "credit"; Russian Wikipedia
    «Зачётная единица трудоёмкости».
  - Failed requests (404, 429, 403) were not treated as evidence.
  - It ran `tools/validate.py` (0 errors) and delegated nothing.
- Consistency review scope:
  - Read all 30 cards and all 31 navigation diffs.
  - Checked the SHA-256 of all 61 changed kanji and word files against `manifest.json`. The manifest diff is 31 hash
    changes, 30 additions and the `contentVersion`, and nothing else.
  - Read only the intake header and payload format.
  - Confirmed that no existing RU card names a new word in a stale or misdirected exclusion. 承認, 許す and 認める
    exclude 許可, not 可.
  - Classified every RU-added exclusion from the RU titles and JMdict senses.
  - Did not run `tools/validate.py`, `link_parity.py` or any generator. It used its own title-screen run, which showed
    only the covered pairs 共同/協力 and 医師/医者.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN.
  - Consulted the RU review and link contract, the content-structure word section, the content-format headings and the
    translator glossary.
  - Used `word_title_screen.py` and `link_parity.py` as leads only. Link parity found no dropped EN link whose RU target
    exists.
  - Opened Jisho/JMdict for 単に, 名人, 博士 and 可能.
  - Used the comparison cards 小川, 医者 and できる, and the title lines of the named contrasts.
  - Ran no validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier.
- Reviews ran serially, one reviewer at a time. Before each review the coordinator checked that HEAD was still `2ae93fb`
  and that `git status --porcelain --ignored` was empty. No fix was applied until all three reports were complete.
- All three launch messages forbade `tools/build_manifest.py` and any other generator. They named the report as the only
  file a reviewer writes. The correctness and consistency reports state that no generator was run; the comprehensibility
  report states it in its recheck section.
- Full blind reports:
  - `215-words-batch-54-review-correctness-001.md`
  - `215-words-batch-54-review-consistency-001.md`
  - `215-words-batch-54-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch worktrees;
  - one another's reports.

  The correctness and comprehensibility reports confirm that no author or reviewer report, batch record or draft was read.
  The consistency report confirms that no other reviewer report, author report or batch record was read.

## Initial verdicts and findings

### Correctness

Verdicts:
- Correctness: **UNVERIFIED** for the batch, solely because of limit L1. The other 29 cards are **CLEAN**.
- Scoped coverage: **NEEDS FIX** (化粧); the other 29 cards are **CLEAN**.

Finding and limit:
- F1 (minor; high confidence, limited impact), `化粧.md:28–29`. EN says explicitly that け + しょう are on readings ("The
  on readings here are…"). The RU note «Чтения здесь — け + しょう» keeps the hiragana and the pronunciation warning but
  drops that classification. In the contrast with 化's か, EN teaches that the alternative is also an on reading.
  - Evidence: Digital Daijisen 化 (Kotobank) lists カ (漢) and ケ (呉) under ［音］ and gives 化粧 under ケ.
  - Remedy: «Онные чтения здесь — け + しょう», with the rest unchanged.
- L1 (a verification limit, not an established mistranslation), `単位.md:4,15,18,20,34`. JMdict sense 3 and English
  Wiktionary "credit" (senses 14–15) confirm the academic-credit sense. The Russian Wikipedia article «Зачётная единица
  трудоёмкости» supports the term and its workload/grade distinction.
  - The reviewer could not find an exact Russian dictionary entry for «зачётная единица». Gramota returned no exact
    entry, Russian Wiktionary compound requests returned 404, and Russian «кредит» lacks that sense.
  - It did not count an encyclopedia as dictionary evidence. It also judged that the current evidence does not justify
    replacing the translation.

What the reviewer confirmed:
- All 59 primary Japanese examples match EN verbatim.
- Inherited metadata, dictionary references and selected senses are preserved.
- No dropped EN link has an existing RU target.
- The readings added in 可能, 収穫, 及ぼす and 協力 are appropriate.

Cited entries supporting the Russian adaptations:
- 名人: «мастер» sense 2 and «Мастер своего дела».
- 合わせる: «подгонять» and «подогнать».
- 叱る: «отчитывать», and «выговор» sense 2, which is a reproach rather than a disciplinary sanction. Jisho 注意 sense 4
  supports the 叱る–注意 guard.
- 可: «удовлетворительно» sense 2 and «проходной» sense 2. The card says "like", not an exact equivalent, and claims no
  universal percentage.
- 取れる: «сойти» sense 5 and «сходить».
- 取り上げる: «вынести» sense 4.
- 収穫: «плод» sense 4.
- 参考: Daijisen 参考, «образец» and «справочный».
- 原: «луг», «равнина», «пустошь» and «степь», given as contextual alternatives.
- 博物館: «музей» sense 1, which includes art collections.
- 博士: «доктор» senses 1–2.
- 双子: «однояйцевой».
- 単に/単なる: «просто». The rentaishi classification supports the no-extra-な rule.
- 医療: «медицина».
- 医師: «официальный», read as a register cue, together with Nipponica 医師.
- 化粧: «макияж» and «плотный». Collocation frequency was not established.

The reviewer judged the RU guards 及ぼす–影響, 原–野 and 博物館–美術館 supported, without a full distractor-corpus audit.

Optional: none.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; scoped coverage (cross-file integration) **CLEAN**; quiz safety **CLEAN**. No findings.

- All 31 navigation diffs wrap a single existing text in a link, with no prose change. Every restored link exists in EN
  at the same position. 獣医 wraps the standalone 医師, not the one inside 獣医師.
- The fields word, reading, jlpt, type, kanji and tags equal EN. Links equal EN except where the target is absent in RU:
  kanji 士 and 療; words 一度に, 仲間, 分ける, 不可, 作物, 加わる, ただ and たった. Those stay plain text.
- No link was added that EN lacks. All EN exclusions are retained.
- RU-added exclusions were classified as shown below; none was judged unjustified.
- Optional notes:
  - 単に's title «…; исключительно» overlaps だけ «только» and ばかり «одно лишь». A conservative 単に–だけ pair could be
    added.
  - 協力 «сотрудничество; совместные усилия» is close to 援助/世話 «помощь».
  - 化学 and 科学 are homophones (かがく), but the 化学 card handles the contrast in its text.
- Limit noted outside the diff: RU `kanji/参.md` has an extra link to 参る. It predates the batch.

### Comprehensibility and scoped coverage

Verdicts:
- Comprehensibility: **NEEDS FIX** (博士, 単に); the other 28 cards are clean in this facet.
- Scoped coverage: **CLEAN** for all 30.

The reviewer found that the named contrasts are shown, not only labelled. It also found that English-only traps were
dropped or recast in Russian: "master" as owner, "exercise" as physical, "field" of study, "consultation" as an
appointment, and "Doctor!".

1. Minor (high confidence), `博士.md:17`: the sentence keeps the English abbreviation «(PhD)». An English-free beginner
   is not expected to know it, and «докторской степени» already states the sense.
   - Evidence: Jisho/JMdict 博士（はかせ） sense 2 glosses it "doctor, PhD, Dr." and marks it colloquial.
   - Remedy: delete the abbreviation.
2. Minor (high confidence), `単に.md:4,11,15`: the quiz title and opening gloss give «исключительно».
   - Bare Russian «исключительно» commonly means "exceptionally", the opposite of this minimizing adverb. This batch uses
     that other sense in `名人.md:15` «исключительно умело». The card separates two senses of «просто» but not of
     «исключительно».
   - Evidence: Jisho/JMdict 単に gives only "simply; merely; only; solely".
   - Remedy: title and H1 «просто (не более того)», and a meaning line «просто, всего лишь».

Optional notes:
- 名人's «знатока» repeats 博士's quiz label «знаток». 博士 already excludes 名人, and the examples say «мастер», so this
  is label hygiene, not a false sense.
- «словарь помечает» could replace "JMdict помечает" in 博士.
- The 共同 readings at lines 32–33 lack the usual parentheses.
- The reviewer itself judged these not to be defects: 原 «ручью»; 叱る's 𠮟る variant note; 博士's はくし and colloquial
  notes; 可能 «Можно ли».

The title-screen stem leads 単に–簡単 and 医療–医学, and the excluded pairs 共同–協力 and 医師–医者, were treated as quiz
leads outside this facet.

## Exclusion classification

All 9 EN exclusion entries (8 lists) are retained. At the candidate, five direct, one-sided entries were added on five new
cards. The consistency reviewer classified all five and found none unjustified:

| Entry | Author | Consistency reviewer |
|---|---|---|
| 原→野 | required | required (JMdict: both "field, plain") |
| 博物館→美術館 | conservative | required (both "museum") |
| 及ぼす→影響 | conservative | required ("exert influence" against "influence") |
| 単なる→単に | conservative | required (adnominal "mere" against adverb "merely") |
| 叱る→注意 | conservative | conservative, defensible (注意's warning and reprimand sense) |

The fix added two more guards, 単に→だけ and 単に→ばかり, adopting the consistency reviewer's optional note; its recheck
classified them. The correctness reviewer judged 及ぼす–影響, 原–野, 博物館–美術館, 単なる–単に and 叱る–注意 supported,
without auditing quiz safety exhaustively. The comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fix and the final verdicts are in
`215-words-batch-54-recheck-001.md`.
