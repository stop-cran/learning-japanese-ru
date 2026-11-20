# Batch 218 — independent review 001

## Snapshot and scope

- Reviewed commit: `4cc28f4411ca8c4cc1d94c5a7cfc02e25752f746` (tree `b193110e748f6063dcdcc5a24c49e17bffecd066`), branch
  `full-ru-218-words-57`, parent `6591e0e`. The candidate was signed and pushed before review.
  - The content was authored in a scratch worktree on the Batch 217 candidate `4af7ea72f6c372d31a810a783ca4b8655dd4ba44`.
    Before copying, the coordinator checked two things: that the 26 navigation files were unchanged between `4af7ea7` and
    the candidate's parent `6591e0e`, and that none of the 30 new cards existed there. The Batch 217 fixes touched only
    借金, 克服, 共に, 共通, 処理 and 出会い, none of which is in this batch's path set.
  - The coordinator byte-compared all 56 scratch content files with the primary checkout twice: after copying and again
    at commit time. Its byte scan found no BOM or CR, and every file ends with a newline, as `.gitattributes` requires.
  - No held wraps were carried into this batch.
  - The coordinator made one layout change before the candidate: in 何で's dialogue, the second speaker's line is now an
    indented continuation of the same bullet instead of a separate bullet, as in EN.
  - The candidate differs from the published baseline in four ways:
    - 30 new word cards;
    - 26 files with 31 restored navigation links;
    - `manifest.json` (`contentVersion` `a6d6e50ba30af4a6`, 4,659 entries);
    - the intake.
- Published baseline recorded in the intake: `6a5ae7566481a01d89b3596fd755a8ca3f78a421` (Batch 217 merge). Parent
  `6591e0e` adds only the Batch 217 publication-verification record.
- Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
- Before the candidate commit, the coordinator's phase-1 screens reported:
  - `tools/validate.py`: 0 errors;
  - unit tests: OK;
  - content budget: OK, 4,676 entries / 13.23 MB;
  - navigation-only check: 26 files and 31 links, with no problem;
  - title screen: no unguarded exact title-segment overlap.
- Common sample: all three reviewers read all 30 new word cards in full.
  - Correctness and comprehensibility read each card against its full EN original.
  - Consistency compared each card's front matter, link targets and exclusions with EN.
- Correctness review scope:
  - Read the binding RU instructions in full.
  - Read the existing 勝つ, 直す, 礼儀, 曲, 自宅, 夏休み, 昼休み and 同僚 cards in full; other comparison cards at title and
    guard level only; and the navigation changes as a bounded diff.
  - Read the JMdict-backed Jisho API records for all 30 headwords; Digital Daijisen on Kotobank for 勝つ, 直す, 何で and
    仲良く; and English Wiktionary's usage notes for なんで.
  - Checked all EN Japanese example sentences against RU, ignoring Markdown and translation wrappers, and read the inline
    forms and explanations by hand.
  - Russian sources: Kuznetsov entries on Gramota (вверить, усмотрение, антракт, излишек, лишний, творение, работа,
    товарищ, компания, взаимоотношения, кредит, доверие, уверенность, кое-как, пример, сравнение, сочинение, культура,
    этикет, физкультура, житель, жильё, жилой, член, отпуск, перерыв and впредь). Gramota HTTP 429 failures were replaced
    by successful fetches, not treated as evidence.
  - Ran `tools/validate.py` (0 errors). It ran no generator.
- Consistency review scope:
  - Read all 30 cards and all 26 navigation diffs in full.
  - Checked the manifest (30 added and 26 changed entries, equal to the content diff; hashes of the 56 changed files match
    the committed blobs) and the intake path list (56 paths, equal to the content diff).
  - Confirmed that the absent link targets 余る, そのうち, メンバー and 今後 are absent.
  - Classified the RU-added exclusions from the RU titles and from JMdict senses fetched through the Jisho API for 頼む,
    例え, 何で and 休憩 only. It did not run `tools/validate.py`.
  - It also reported that the stroke JSON manifest entries did not match the raw blob hashes, outside the batch. The
    coordinator withdrew this by evidence: `tools/build_manifest.py` hashes the bytes after CRLF→LF normalisation, and
    those stroke blobs are CRLF byte copies marked `-text`, so the committed hashes are current.
  - It noted that `kanji/信.md` has a pre-existing 信号 link that EN lacks; it is not a batch change.
- Comprehensibility review scope:
  - Read the 30 cards in full against EN, and compared the existing RU titles of the named near-synonyms.
  - Read JMdict entries through the Jisho API, Russian Wiktionary (антракт, кое-как) and dictionary snippets from MAS,
    Ushakov, Kuznetsov and Efremova.
  - Used the title-overlap and link-parity checks only as leads: no EN link whose RU target exists was dropped. It did not
    run the content validator.
- Each reviewer was assigned a model from a different family:

  | Facet | Model |
  |---|---|
  | Correctness | `gpt-6.1-sol` |
  | Consistency/quiz safety | `claude-sonnet-5.5` |
  | Comprehensibility | `grok-4.7` |

  The runtime agent status exposed these assigned model variants. Reviewer prose did not expose a lower-level serving
  identifier.
- Reviews ran serially, one reviewer at a time. Each reviewer reports that HEAD was `4cc28f4` and the working tree was
  clean when it started. No fix was applied until all three reports were complete, and the coordinator confirmed
  afterwards that HEAD was still `4cc28f4` and that `git status --porcelain --ignored` was empty.
- All three launch messages forbade `tools/build_manifest.py` and any other generator, and named the report as the only
  file a reviewer writes. No repository file was written.
- Full blind reports:
  - `218-words-batch-57-review-correctness-001.md`
  - `218-words-batch-57-review-consistency-001.md`
  - `218-words-batch-57-review-comprehensibility-001.md`
- Initial reviewers were told not to read:
  - the author report or prompt;
  - the coordinator's title-screen output;
  - anything under `docs/translation-batches/`, `docs/translation-drafts/` or `docs/translation-tracking.json`;
  - the scratch worktrees;
  - one another's reports.

  The correctness report confirms that it read no forbidden report, batch, draft or tracking record, or scratch checkout.
  The comprehensibility report confirms that it read no other review report, disposition or batch record. The consistency
  report does not restate the rules.

## Initial verdicts and findings

### Correctness

Verdicts: correctness **CLEAN** for all 30 cards. Scoped coverage **NEEDS FIX** (F1, 余分); the other 29 cards are clean
in this facet.

- F1 (minor; high confidence), `余分.md:24`: EN's reading join "The on readings combine as よ + ぶん." became «ヨ + ブン».
  The sound is the same, and RU correctly calls them on readings, so this is not a reading error; it breaks the rule that
  Japanese source text keeps its script. Remedy: «Онные чтения складываются как よ + ぶん.» Evidence: EN `余分.md:29`;
  JMdict 1544520 (よぶん, noun and na-adjective, "extra; excess; surplus").

What the reviewer confirmed:
- All EN Japanese example sentences remain present. Every main example was checked for polarity, aspect, event stage,
  voice and roles. Masculine first-person forms and «мой друг» select a possible context and make no claim that 私 or 友達
  encodes sex; 姉 and 彼女 stay female. «Коллегами» correctly renders 仕事の仲間, using JMdict 仲間's coworker sense, and the
  card does not equate every 仲間 with 同僚.
- Source IDs, readings, levels, types, kanji lists, tags, exclusions and dictionary references are retained. The seven
  added guards are 倒す–勝つ, 修正–直す, 作法–礼儀, 作品–曲, 住宅–自宅, 休暇–夏休み and 休憩–昼休み. Every EN link with an
  available RU target survives, and every new card has a manifest entry.
- JMdict distinctions survive translation: 保証 alone carries the warranty sense (保障 only the general assurance); 作法
  restricts etiquette to さほう; 例え's spellings are preferences, not sense restrictions; 仲間 includes colleague and the
  group or category senses; 以来 has suffixal and standalone adverbial use.
- Digital Daijisen 勝つ sense 1 shows competition with に, and 直す 1イ/2イ distinguishes repairing from correcting, both
  with を; with JMdict's intransitive 勝つ and transitive 直す and 倒す, they support the added contrasts. English
  Wiktionary's なんで usage notes (chiefly informal, compatible with polite endings) support the «разг.» qualifier in 何で's
  title without contradicting its polite example.

Cited evidence supporting the Russian adaptations:
- 任せる: Kuznetsov «вверить» (to place in someone's charge or care; to entrust) and «усмотрение» (a judgement or
  decision).
- 休憩: «антракт» sense 1 is the interval between acts or concert sections, with a conversational extension to any break;
  the title corresponds to EN "intermission". «Перерыв» sense 3.
- 余分: «излишек» sense 1 (what remains beyond the amount needed) and «лишний» senses 1–3, which include extra or
  additional as well as unnecessary, so a useful spare onigiri does not contradict the RU example.
- 作品: «творение» sense 1 (a creative product, marked elevated, not requiring a famous professional) and «работа» senses 2,
  4, 5 and 6, which support the adapted distinction between a job, a task and a created work.
- 仲間 and 仲: «товарищ» senses 1–2, «компания» senses 1–2 (a social group against a business) and «взаимоотношения»; the
  title's «между людьми» supplies 仲's narrower domain.
- 信用 and 信頼: «кредит» senses 1–2 (lending and commercial creditworthiness; the accounting homonym was not used),
  «доверие» and «уверенность» sense 1, without a feelings-against-finance split.
- 何とか: «кое-как» sense 1, "with great difficulty", fits «кое-как успел вовремя»; sense 2 separately means carelessly.
  No careless-action error was established in this facet.
- 例え, 作曲, 作物, 作法 and 体育: «пример» sense 1, «сравнение» sense 2, «сочинение» senses 1–3, «культура» sense 7
  (cultivated plant varieties), «этикет», «физкультура».
- 住民, 住宅, 会員 and 休暇: «житель», «жильё» sense 2 and «жилой», «член» sense 4 and «отпуск» sense 2 (release from
  duties for rest or other purposes, not only a paid annual trip).
- 以来: «впредь» is future time. The warning keeps the Japanese past-anchor rule, but its quoted "dictionary translation"
  adapts EN "henceforth" rather than a Russian gloss the card offers.

Optional:
- Mark «творение» as elevated, and consider «стали хорошо ладить» beside «подружились» in 仲; Digital Daijisen 仲良く
  describes amicable terms, while «подружиться» establishes a friendship. The contextual example remains possible.
- 以来:33 could state the past-anchor rule without warning against a Russian dictionary translation the card does not
  show.
- Outside its facets: navigation gaps 住宅→住民, 自宅→住宅 and 昼休み→休憩 (EN leaves all three unlinked), and quiz leads
  住民–人口 and 仲間–友達, referred to the quiz reviewer and not counted as findings.

### Consistency and quiz safety

Verdicts: consistency **CLEAN**; scoped coverage (cross-file integration) **CLEAN**; quiz safety **NEEDS FIX** (例え and
任せる, both minor).

- Q1 (minor; medium confidence), `例え.md:9`: the title «пример (для пояснения); образное сравнение» contains «сравнение»,
  the whole title of 比較. JMdict 例え sense 2 is "simile; metaphor; allegory; fable; parable", and «сравнение» is the
  Russian term for a simile. The EN titles do not overlap, so this is RU-introduced. Remedy: `quiz_exclusions: [例, 比較]`.
- Q2 (minor; medium confidence), `任せる.md:10`: 任せる «вверять (дело)» is close to 頼む «просить; поручать»; JMdict 頼む
  has the sense "to entrust to". EN 頼む is "request", so this overlap is RU-introduced too. Remedy:
  `quiz_exclusions: [預ける, 頼む]`.
- The seven RU-added exclusions are all required: 倒す→勝つ (the title contains 勝つ's whole title «побеждать»; JMdict 倒す
  "defeat"), 修正→直す (JMdict 直す "to correct"), 作法→礼儀 («этикет»), 作品→曲 («произведение»), 住宅→自宅 («жильё»),
  休暇→夏休み («отпуск») and 休憩→昼休み («перерыв»). All other exclusions equal EN, and no existing RU card excludes a batch
  word.
- The RU-only links 倒す→勝つ and 修正→直す are acceptable.
- Navigation: the 26 diffs are identical to their parents apart from the restored links, and the 31 links match EN's
  positions and path forms. Front-matter keys and headings match EN.

Optional: guards for 休憩–休む, 何で–どう, 住民–人口, 作法–方法, 会員–仲間, 会員–委員, 伝統–習慣, 体育–運動 and 仲間–友達, each
unguarded in EN too or a weak overlap; and a link from 何時か to いつ.

### Comprehensibility and scoped coverage

Verdicts: comprehensibility **NEEDS FIX** (休憩 and 何とか; the other 28 cards are clean in this facet); scoped coverage
**CLEAN** for all 30 cards.

- C1 (minor; high confidence), `休憩.md:4,12`: the title «перерыв; антракт» presents «антракт» as an equal, unqualified
  gloss. A beginner can take 休憩 for a theatrical interval, or call a meeting break «антракт»; the card's own examples are
  a general rest and a ten-minute meeting break. Because the title is the quiz answer, the unqualified second gloss is what
  the learner memorises. Remedy: the title «перерыв», and a nuance sentence reserving «антракт» for a performance.
  Evidence: JMdict 1227720 sense 1 is one general sense (rest, break, recess, intermission); Russian Wiktionary marks
  «антракт» theatrical, while Ushakov sense 2 and Kuznetsov mark a general break as conversational. The reviewer did not
  claim that «антракт» can never mean a break.
- C2 (minor; high confidence), `何とか.md:17`: «Я спешил и кое-как успел вовремя» uses «кое-как», whose first ordinary sense
  is slipshod work, which JMdict does not give this adverb; a learner can extract 何とか = «небрежно». Remedy: «Я спешил и с
  трудом успел вовремя.» Evidence: EN "somehow managed to make it in time"; JMdict 1188420 sense 2; Russian Wiktionary
  «кое-как» senses 1 («плохо, небрежно») and 2 («с большим трудом»).

Optional (judged not findings): 仲間's «коллега» against 同僚 (optional «с товарищами по работе»); 会員:32 «регистрация
участника» (optional «регистрация члена»); 住宅:33 rejecting a «житель» gloss the card never offers; 作法 explains 礼儀 but
not 行儀, as in EN. Outside its facets, it noted that some new cards exclude an existing card one way only (信用 excludes
信じる but not 信頼, while 信頼 excludes 信用), which is quiz pairing.

Checked and not findings: «кредит», «компания», «член (клуба, общества)» and «вверять (дело)» are already qualified.

## Exclusion classification

All 28 EN exclusion entries (21 lists) are retained. At the candidate, seven direct, one-sided entries were added on seven
new cards:

| Entry | Author | Consistency reviewer |
|---|---|---|
| 倒す→勝つ | required | required (whole title «побеждать») |
| 修正→直す | required | required (correcting) |
| 作法→礼儀 | required | required («этикет») |
| 作品→曲 | required | required («произведение») |
| 住宅→自宅 | required | required («жильё») |
| 休暇→夏休み | required | required («отпуск») |
| 休憩→昼休み | required | required («перерыв») |

The author had considered and declined a conservative 例え–比較 guard, judging that the head noun «пример» separates the
titles, and listed it as an open question; the consistency reviewer raised it as Q1. The fixes added five more entries: Q1,
Q2 and three adopted optional items. The correctness reviewer checked the guard comparison words in JMdict without auditing
quiz safety, and the comprehensibility reviewer did not score the guards.

Reconciliation, the coordinator's dispositions, the exclusions changed by the fixes and the final verdicts are in
`218-words-batch-57-recheck-001.md`.
