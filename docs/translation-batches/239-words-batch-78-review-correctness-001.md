# B239 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `39b6bd13afc5eec5371ce27cd611ce1ff581f19a` (tree `d966f81d76a25657d6aad60cb77733f2f9631bfd`),
> the signed candidate pushed before review.
> Later reconciliation is in `239-words-batch-78-recheck-001.md`.

Snapshot: RU 39b6bd13afc5eec5371ce27cd611ce1ff581f19a on full-ru-239-words-78; reviewed against parent 3f56e1abab4f7ec9edb9961e75554b5deca9c6b9 and frozen EN 6af98cb. Final HEAD matches; git status --porcelain empty; working-tree and cached diffs empty. No repository files changed.

Scope: Correctness and scoped coverage. Each of the following was read IN FULL, paired with its complete frozen EN original:
words/清書.md; words/複写.md; words/裏口.md; words/裂く.md; words/被せる.md; words/カバー.md; words/表紙.md; words/衣食住.md; words/街角.md; words/行列.md; words/儀式.md; words/行事.md; words/血液.md; words/血圧.md; words/蝋燭.md; words/コック.md; words/蛇口.md; words/蚊.md; words/虹.md; words/思い付く.md; words/蘇る.md; words/薬缶.md; words/薬指.md; words/薬局.md; words/薬品.md; words/薄暗い.md; words/薄める.md; words/蕎麦.md; words/栓.md; words/蓋.md.
Also checked candidate runtime backlink changes, metadata, relative-link parity, selected baseline comparisons, and manifest validation. Russian comprehensibility is outside the assigned facets. Actual model identity: not independently verifiable.

Verdicts:
- correctness NEEDS FIX: C1 and C2. No actionable correctness defect established in the other 28 assigned articles.
- coverage NEEDS FIX: C2 in words/被せる.md. No other actionable scoped-coverage defect established; the recall sense in 思い付く remains in the body, despite its misleading title.
- Russian comprehensibility UNVERIFIED: outside assigned facets; the optional observation below is not a comprehensive assessment.

Findings:

C1; medium; correctness; words/思い付く.md:4 (repeated at :12).
Claim/impact: “вспоминать (о мысли, пришедшей на ум)” restricts the recall gloss to remembering a previously occurring thought. The Japanese sense also covers remembering something forgotten, such as an urgent errand; it is not limited to recalling an earlier idea. This misleading restriction appears in the quiz-facing title, notwithstanding the more accurate body at :16 and :40–43.
Remedy: use `title: придумывать, додумываться; вспоминать` and `# 思い付く（おもいつく）— придумывать, додумываться; вспоминать`. Keep the body's practical distinction from 思い出す and the existing direct quiz exclusion; the correction does not claim universal interchangeability.
Evidence: https://kotobank.jp/word/思い付く-454672 — Digital Daijisen, おもい‐つ・く, sense 2: “忘れていたことを思い出す”, example “急用を―・く”. The same page's Seisenban entry [2] includes 思い出す. Full JMdict entry 1589330, sense 2, also gives “to remember; to recall”: https://www.edrdg.org/pub/Nihongo/JMdict_e.gz.
Confidence: high for the Japanese sense; medium-high for the title's misleading Russian restriction.

C2; medium; correctness and scoped coverage; words/被せる.md:20.
Claim/impact: 料理に蓋をかぶせておきました is translated only as “Я накрыл еду крышкой.” The covering action is retained, but the auxiliary ておく's leaving/maintaining the resulting state is lost. Frozen EN explicitly preserves it (“I left a lid over the food”, :20). As presented, the learner-facing translation does not distinguish this construction from simple かぶせました.
Remedy: “Я накрыл еду крышкой и оставил её накрытой.” This preserves the stated result without inventing a particular future purpose.
Evidence: https://www.weblio.jp/content/置く — Digital Daijisen, おく【置く】, auxiliary sense 12㋑: “その状態を続けさせる。そのままにする”, with 窓を開けておく. Sense 12㋐ separately describes advance preparation. Full JMdict entry 1484320 confirms the underlying covering verb; the defect is the omitted auxiliary, not its lexical meaning or transitivity.
Confidence: high.

Optional:
- Outside assigned facets, nonblocking comprehensibility polish: words/コック.md:44, “Исходная строка объединяет значения двух записей”, refers to an author-facing source row without explaining that referent to the learner. Consider “Здесь рассматриваются два разных слова с одинаковым написанием.” The factual separation itself is correct: JMdict 1050310 (cook, Dutch kok) versus 2862559 (tap/cock and other English-derived senses). No correctness finding is attached to this observation.

Checks and limits:
- All 64 bulleted Japanese example sentences and their kana readings match EN as strings; full-width Russian reading wrappers replace EN's ASCII wrappers. This formatting localization is not treated as a Japanese-reading defect. Examples and the additional inline Japanese constructions were reviewed in context, not approved merely through string equality.
- Front matter's word, reading, level, type, kanji, tags and existing exclusions are preserved. Added RU exclusions are conservative guards, not replacements of EN exclusions. All 30 N2 labels independently match the pinned community vocabulary CSV: https://raw.githubusercontent.com/stephenmk/yomitan-jlpt-vocab/b062d4e38c4bdd0950ae1d4ec55f04b176182e03/original_data/n2.csv. These are article-level study labels, not official JLPT assignments of every sense.
- Read the full current JMdict entries for all 30 main words, additional cited entries and relevant comparisons. Checked component readings using https://www.edrdg.org/pub/Nihongo/kanjidic2.xml.gz after kanjiapi requests failed. Dictionary readings were not used as proof of historical etymology.
- Actual Japanese dictionary definitions and Russian lexical entries were inspected where consequential: notably 裂く/割く, 蘇る, 被せる/着せる, コック, 蛇口, 清書, 行事, 薬缶, 栓, and the Russian glosses вспарывать, додумываться, химикат, сумрачный, полутёмный, дубликат, восполнять, служба and чёрный ход. No additional actionable defect established.
- No broken RU relative link found. Every dropped EN card link has an absent RU target, so plain text follows the stated convention. Added links and existing-card backlinks preserve appropriate comparisons. The read-only RU validator completed with 0 errors and exit 0; this is structural evidence, not semantic acceptance.
- Evidence uses current dictionaries rather than a historical dictionary capture. Jisho rate limiting was superseded by full JMdict retrieval. No consequential unresolved claim is being silently classified CLEAN.
- No native-speaker, app/device, learning-effectiveness or complete whole-pool quiz acceptance is claimed. No new curated quiz_distractors were added; automatic-selection semantics and complete quiz-pool ambiguity testing are outside these assigned facets. Russian comprehensibility remains unassessed as a facet.
- Blindness maintained: no other session-files prompt/report, forbidden RU tracking/draft/batch record, or scratch worktree was read. Only this designated report was written; no generators, commits, pushes or checkout changes.
