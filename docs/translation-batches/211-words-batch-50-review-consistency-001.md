# B211 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `53d6950b1b8c0d254414e1f2ba4d967b2ca3b43a` (tree `154fb77da0097183389a794e442bf915ed34d075`),
> the signed candidate pushed before review.
> Later reconciliation is in `211-words-batch-50-recheck-001.md`.

Snapshot: RU `53d6950b1b8c0d254414e1f2ba4d967b2ca3b43a` (branch full-ru-211-words-50). `git rev-parse HEAD` matched; `git status --porcelain` empty before and after my checks. No uncommitted changes. Parent diffed: `eb270c7`. Frozen EN `6af98cb`.

Scope: Facets CONSISTENCY + QUIZ SAFETY + cross-file integration (scoped coverage). Model not verifiable from inside the session. Read IN FULL (front matter + body, against the EN original for front matter, headings, links and exclusions): all 30 new cards (少女 小麦 小屋 包み 小包 小 専攻 対象 対 審判 密 寄付 宿 宿泊 家賃 家具 実験 実施 実行 実現 実は 宝石 宝 宜しく パス 券 定期 信仰 宗教 完成). Read in full as diffs: all fourteen navigation files (numbers-and-counters, kanji 券 包 完 宝 専 成, words 実に 実際 提案 滞在 範囲 貢献 少年), plus manifest.json diff and the intake record (path list only). Mechanical checks run: `tools/validate.py` (0 errors; read-only), my own sha256 check of manifest md entries, a script comparing front matter/links/exclusions with EN, a title-segment collision scan against all RU word titles, and `word_title_screen.py` as lead only. Not run: build_manifest or any generator. Not read: author reports/prompts, other reviews, batch records/drafts/tracking.

Verdicts:
- Consistency: CLEAN (all 30 cards; all 14 navigation files; manifest; intake).
- Quiz safety: CLEAN (all 30 cards). No missing required guard; no unjustified exclusion. Optional conservative candidates listed below.
- Scoped cross-file integration (links, manifest, intake): CLEAN.
- Linguistic correctness and comprehensibility of card prose: not assessed (other facets).

Verification evidence
1. Front matter: for all 30 cards `word, reading, jlpt, type, kanji, tags` equal EN; only `title` is translated; no extra keys other than `quiz_exclusions` where listed below. Heading set is identical (`## Значение / Как сочетаются кандзи / Синонимы и антонимы / Оттенки значения` + dictionary line); LF endings; no CR.
2. EN exclusions: every EN `quiz_exclusions` entry is retained (少女, 包み, 小包, 審判, 密→親しい, 宿, 宿泊, 実行→実施, 実は→実際, 宝石→玉, パス, 券, 定期, 宗教). No EN card lacking exclusions was given one except the RU-introduced entries below.
3. Links: no Russian-only link in any card. EN links missing in RU are exactly the ten whose RU targets do not exist (kanji 麦 象 泊; words 学ぶ ところで お願いします 信じる 信用 完了 完全), each left as plain text, per convention. Every RU link target in the 30 cards exists. A corpus-wide EN-vs-RU comparison of links to the 30 batch words found no dropped link whose RU target exists (the only count difference, kanji/少.md → `小.md`, is the kanji card, pre-existing and unrelated).
4. Navigation: 24 restored links in the 14 files, matching the specified distribution (numbers 1; 券 2; 包 2; 完 3; 宝 4; 専 2; 成 3; 実に, 実際, 提案, 滞在, 範囲, 貢献, 少年 1 each). After removing link markup, 13 files are byte-identical in prose to the parent; 少年 differs only in the gloss «девочка» → «девочка, юная девушка». Each restored link exists in the EN file at the same position (counts match). No other prose touched.
5. Manifest: 30 added + 14 changed md/article entries, none removed; every md hash recomputed OK; no md/kanji/article file missing from the manifest. (My sha256 of `strokes/*.json` entries differs under raw-byte hashing, 110 files, none touched by this candidate; presumably the manifest uses normalised text — unverifiable without the generator; unrelated to this change.) No generated/unrelated files in the commit.
6. Intake record: 44 payload paths equal the 44 content paths of the diff exactly; no learner content added.
7. Title collisions: scan against every RU word title found only four identical title segments: 密~親しい and 近い («близкий»), 宿~ホテル («гостиница»), 宝石~玉 («драгоценный камень»), 完成~仕舞い («завершение»). Each pair has a direct exclusion on at least one side (密 lists 親しい and 近い; 宿 lists ホテル; 宝石 lists 玉; 完成 lists 仕舞い). No new title equals another card's whole title.

RU-introduced exclusions (beyond EN) — dictionary basis and necessity
- 密→近い: JMdict 近い sense 1 "near; close; nearby" vs 密 sense 2 "close (relationship)"; identical title segment «близкий». REQUIRED (the pre-existing 親しい→近い makes the same point, and 親しい↔密 is an EN pair).
- 宿→泊まる: JMdict 宿 sense 1 "inn; lodging" vs 泊まる "to stay at (a hotel); to lodge"; «место ночлега» vs «останавливаться на ночлег», different parts of speech. CONSERVATIVE (real basis, necessity unestablished).
- 宿泊→泊まる: JMdict 宿泊 "lodging; accommodation" vs 泊まる; «ночёвка» vs «ночевать» share a root and the 宿泊 card itself says 泊まる fits the same hotel example. REQUIRED, or at least strongly justified.
- 実施→行う: JMdict 実施 "implementation; enforcement" vs 行う "to carry out; to conduct"; «проведение» vs «проводить» are the same lexeme family, and the card's own body notes 行う can be said of the same event. REQUIRED.
- 実行→行う: JMdict 実行 "execution; carrying out" vs 行う "to carry out; to perform"; «исполнение» vs «выполнять» near-synonyms. CONSERVATIVE.
- 実現→実行: JMdict 実現 "realization; materialization" vs 実行 "execution; carrying out"; «осуществление» vs «претворение в жизнь» are close in Russian; the 実現 card contrasts them in its body. CONSERVATIVE (real basis; the contrast is taught, so the guard is defensible rather than redundant).
- 完成→仕舞い: JMdict 完成 "completion" vs 仕舞い "end; finish; close"; shared segment «завершение». REQUIRED.
None is unjustified (none guards a mere topical relation or an antonym).

Findings: none. No actionable defect established in the consistency or quiz-safety facets.

Optional (nonblocking; all unguarded in EN too, so these are parity-consistent choices, not defects):
- O1. 定期 «установленный срок» vs 期間 «срок; период»: overlapping stem; the 定期 card teaches the "fixed term" sense. If wanted, add `期間` to 定期's `quiz_exclusions`: `quiz_exclusions: [パス, 切符, 券, 期間]`.
- O2. 実験 «эксперимент» vs 試験 «экзамен; испытание»: the 実験 card says 試験 "may overlap" for equipment testing; no guard exists in either card. If wanted, add `quiz_exclusions: [試験]` to 実験.
- O3. パス «…путь к файлу» vs 道 «дорога; путь»: the card contrasts them in its body; a learner choosing «путь» for the computer sense is unlikely but possible.
- O4. 小屋 «…домик» vs 家 «дом; жилище»: the RU gloss «домик» (EN: "hut; shed; cabin") adds a diminutive stem to 家; the card itself teaches the distinction. If wanted, add `家` to 小屋's `quiz_exclusions`, or drop «домик».
- O5. 少女 «юная девушка» shares the stem «девушка» with 彼女 «девушка (в отношениях)» and 恋人 «…парень или девушка»; qualifiers make a defensible mixup unlikely. 小 «малый размер» vs 大小 «размер; большое и малое» shares «размер» likewise; no guard needed.
- O6. 少年 now glosses 少女 as «девочка, юная девушка» where EN says "girl"; this follows the new RU title (EN title "young girl"; RU «юная девушка» is wider). It is a deliberate gloss alignment, not a defect; correctness of the RU title wording is for the correctness reviewer.

Limits:
- Dictionary senses above are quoted from my knowledge of JMdict/Japanese dictionaries; I did not re-open the entries online in this review, so entry numbers were not independently re-verified (the cards' own cited entry IDs were not checked).
- Necessity classifications of exclusions are judgments about plausible quiz confusion, not demonstrated app behaviour; no app/quiz run was performed.
- Linguistic accuracy of Russian prose and examples, and comprehensibility, were not assessed here.
- The manifest's raw-hash mismatch for strokes JSON is outside this candidate and unexplained without running the generator (not permitted).
